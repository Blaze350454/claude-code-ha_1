<#
.SYNOPSIS
  Wrapper that lets Task Scheduler run sync_timelapse.ps1 unattended.

.DESCRIPTION
  Two reasons this exists rather than pointing the task straight at the sync:

  1. TASK SCHEDULER HANDS A JOB A MINIMAL PATH. It reads no shell profile, so
     `uv` (in %USERPROFILE%\.local\bin) and ssh are not necessarily resolvable
     even though they work fine in an interactive terminal. The sync shells out
     to both. This wrapper puts them on PATH explicitly and FAILS LOUDLY if
     either is missing, rather than letting the sync half-work.

  2. AN UNATTENDED JOB THAT FAILS SILENTLY IS WORSE THAN NO JOB. Every run
     appends a timestamped line to sync.log beside the frames, so "why is the
     folder stale" is answerable by opening one file. The log is trimmed so it
     cannot grow without bound.

  Exit codes are the sync's own, plus 2 for "could not look" (a prerequisite is
  missing), matching the house convention that an error must never be reported
  as an empty result.

.EXAMPLE
  pwsh -NoProfile -File tools\sync_timelapse_scheduled.ps1
#>
[CmdletBinding()]
param(
  [string]$Dest    = 'D:\Claude\Pictures\timelapse',
  [string]$LogPath = 'D:\Claude\Pictures\timelapse\sync.log',
  [int]   $MaxLogLines = 2000
)

# --- THE TASK MUST RUN AS S4U, NOT INTERACTIVE -------------------------------
# With LogonType=Interactive, Task Scheduler hands this script a real console
# window that appears over whatever the user is doing, every 15 minutes. Nothing
# in here can prevent that: the console exists from the moment pwsh starts, and
# the earliest a script can hide it is after the engine boots and compiles a
# P/Invoke - a few hundred ms at best, on a 2-3 s run. Hiding it from inside was
# tried on 2026-08-29 and the flash remained.
#
# The fix belongs on the task, and needs elevation:
#
#   Set-ScheduledTask -TaskName 'Timelapse Sync' -Principal (
#     New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" `
#       -LogonType S4U -RunLevel Limited)
#
# S4U runs it in a non-interactive session, so there is no console at all. It
# works here because the sync needs only local disk and an SSH KEY - S4U has no
# network credentials, so a mapped drive or password auth would break under it.
# If this task is ever recreated, recreate it as S4U.

$ErrorActionPreference = 'Stop'
$started = Get-Date

function Write-Log([string]$msg) {
  $line = '{0}  {1}' -f $started.ToString('yyyy-MM-dd HH:mm:ss'), $msg
  try {
    $dir = Split-Path $LogPath -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force $dir | Out-Null }
    Add-Content -Path $LogPath -Value $line -Encoding utf8
  } catch {
    # A logging failure must not take the sync down, but must not vanish either.
    Write-Host "sync_timelapse_scheduled: cannot write $LogPath - $($_.Exception.Message)"
  }
  Write-Host $line
}

# --- PATH: the whole reason for this wrapper ---------------------------------
$uvDir  = Join-Path $env:USERPROFILE '.local\bin'
$sshDir = Join-Path $env:WINDIR 'System32\OpenSSH'
foreach ($d in @($uvDir, $sshDir)) {
  if ((Test-Path $d) -and ($env:PATH -notlike "*$d*")) { $env:PATH = "$d;$env:PATH" }
}

$missing = @()
foreach ($exe in 'uv', 'ssh') {
  if (-not (Get-Command $exe -ErrorAction SilentlyContinue)) { $missing += $exe }
}
if ($missing.Count) {
  Write-Log ("COULD NOT LOOK - not on PATH: {0}. Frames not synced." -f ($missing -join ', '))
  exit 2
}

$sync = Join-Path $PSScriptRoot 'sync_timelapse.ps1'
if (-not (Test-Path $sync)) {
  Write-Log "COULD NOT LOOK - missing $sync. Frames not synced."
  exit 2
}

# --- run it ------------------------------------------------------------------
try {
  $out  = & $sync -Dest $Dest -NoOpen 2>&1
  $code = $LASTEXITCODE
} catch {
  Write-Log ("FAILED - {0}" -f $_.Exception.Message)
  exit 1
}

$text    = ($out | Out-String)
$newFiles = 0
if ($text -match 'Sync done - (\d+) new file') { $newFiles = [int]$Matches[1] }
$secs = [int]((Get-Date) - $started).TotalSeconds

if ($code -ne 0) {
  Write-Log ("FAILED (exit {0}) after {1}s. Last output: {2}" -f $code, $secs,
             (($text -split "`n" | Where-Object { $_.Trim() } | Select-Object -Last 1) -replace '\s+', ' '))
  exit $code
}

# Quiet on success, but never silent: one line, so a stale folder is explicable.
Write-Log ("ok - {0} new frame(s) in {1}s" -f $newFiles, $secs)

# --- keep the log bounded ----------------------------------------------------
try {
  if (Test-Path $LogPath) {
    $lines = @(Get-Content $LogPath)
    if ($lines.Count -gt $MaxLogLines) {
      $lines[($lines.Count - $MaxLogLines)..($lines.Count - 1)] |
        Set-Content -Path $LogPath -Encoding utf8
    }
  }
} catch { }

exit 0
