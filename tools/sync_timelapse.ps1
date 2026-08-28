<#
.SYNOPSIS
  Mirror the grow-tent timelapse frames to this PC and rebuild the offline gallery.

.DESCRIPTION
  Pulls every timelapse frame from the HA VM -- both the current-month window under
  www/timelapse/<cam>/ and the rolled-off months under ~/timelapse_archive/<cam>/ --
  into <Dest>\<cam>\, then regenerates <Dest>\index.html from
  tools\timelapse_gallery.html.

  Incremental: only files missing locally are fetched, streamed as a single tar per
  batch (one ssh connection per ~200 files, not one per file). Movies re-download
  when the remote size changes.

.EXAMPLE
  pwsh -File tools\sync_timelapse.ps1
  pwsh -File tools\sync_timelapse.ps1 -Dest E:\backup\timelapse -NoOpen
#>
[CmdletBinding()]
param(
  [string]$Dest   = 'D:\Claude\Pictures\timelapse',
  [string]$Remote = 'homeadmin@192.168.2.151',
  [int]   $Batch  = 200,
  [switch]$NoOpen,          # don't launch the gallery when finished
  [switch]$GalleryOnly      # skip the network sync, just rebuild index.html
)

$ErrorActionPreference = 'Stop'
$tplPath = Join-Path $PSScriptRoot 'timelapse_gallery.html'
$tmpDir  = Join-Path $env:TEMP 'timelapse_sync'
$sshOpts = @('-o', 'ConnectTimeout=10', '-o', 'BatchMode=yes')

# Remote roots. Anything matching <root>/<cam>/ is treated as a camera folder;
# "movies" is carried through as a pseudo-camera holding the rendered mp4s.
$WWW     = '~/homeassistant/.config/www/timelapse'
$ARCHIVE = '~/timelapse_archive'

function Say([string]$m, [string]$c = 'Gray') { Write-Host $m -ForegroundColor $c }

# Ship a shell snippet without fighting three layers of quoting.
# CRLF must be stripped -- bash chokes on the trailing \r ("$'\r': command not found").
function RemoteCmd([string]$script) {
  $b64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes(($script -replace "`r`n", "`n")))
  "echo $b64 | base64 -d | bash"
}

function Prettify([string]$id) {
  ($id -split '[_-]' | ForEach-Object {
    if ($_.Length -le 1) { $_.ToUpper() } else { $_.Substring(0,1).ToUpper() + $_.Substring(1) }
  }) -join ' '
}

New-Item -ItemType Directory -Force -Path $Dest, $tmpDir | Out-Null

# ---------------------------------------------------------------- inventory ---
if (-not $GalleryOnly) {
  Say "Reading remote inventory from $Remote ..." Cyan

  $inv = RemoteCmd @"
for d in $WWW/*/ $ARCHIVE/*/; do
  [ -d "`$d" ] || continue
  cam=`$(basename "`$d")
  src=A; case "`$d" in *www*) src=W;; esac
  find "`$d" -maxdepth 1 -type f \( -name '*.jpg' -o -name '*.mp4' \) ! -name latest.jpg -printf "`$cam|`$src|%f|%s\n"
done
"@

  $lines = & ssh @sshOpts $Remote $inv
  if ($LASTEXITCODE -ne 0) { throw "ssh inventory failed (exit $LASTEXITCODE). Is $Remote reachable?" }

  $remoteFiles = @(foreach ($l in $lines) {
    $p = $l -split '\|'
    if ($p.Count -eq 4) { [pscustomobject]@{ Cam = $p[0]; Src = $p[1]; Name = $p[2]; Size = [int64]$p[3] } }
  })
  if (-not $remoteFiles.Count) { throw "Remote inventory came back empty - check the paths in `$WWW / `$ARCHIVE." }
  Say ("  {0} files across {1} folders" -f $remoteFiles.Count, ($remoteFiles.Cam | Sort-Object -Unique).Count)

  # ------------------------------------------------------------------ pull ---
  $pulled = 0
  foreach ($g in $remoteFiles | Group-Object Cam, Src) {
    $cam = $g.Group[0].Cam
    $src = $g.Group[0].Src
    $srcDir  = if ($src -eq 'W') { "$WWW/$cam" } else { "$ARCHIVE/$cam" }
    $camDir  = Join-Path $Dest $cam
    New-Item -ItemType Directory -Force -Path $camDir | Out-Null

    $local = @{}
    Get-ChildItem -LiteralPath $camDir -File -ErrorAction SilentlyContinue |
      ForEach-Object { $local[$_.Name] = $_.Length }

    # jpgs never change once written; movies get re-rendered, so compare size too
    $want = @($g.Group | Where-Object {
      -not $local.ContainsKey($_.Name) -or
      ($_.Name -like '*.mp4' -and $local[$_.Name] -ne $_.Size)
    })
    if (-not $want.Count) { continue }

    Say ("  {0,-14} {1}  <- {2} new file(s)" -f $cam, $(if ($src -eq 'W') { 'current' } else { 'archive' }), $want.Count) Green

    for ($i = 0; $i -lt $want.Count; $i += $Batch) {
      $chunk = $want[$i .. [Math]::Min($i + $Batch - 1, $want.Count - 1)]
      $tar   = Join-Path $tmpDir 'chunk.tar'
      $err   = Join-Path $tmpDir 'chunk.err'
      $cmd   = RemoteCmd ("tar -cf - -C $srcDir " + (($chunk.Name) -join ' '))

      # Start-Process (not the PS pipeline) so the tar stream stays byte-exact.
      $p = Start-Process -FilePath 'ssh' -ArgumentList ($sshOpts + @($Remote, $cmd)) `
             -RedirectStandardOutput $tar -RedirectStandardError $err `
             -NoNewWindow -Wait -PassThru
      if ($p.ExitCode -ne 0) { throw "tar stream failed for ${cam}: $(Get-Content $err -Raw)" }

      & tar -xf $tar -C $camDir
      if ($LASTEXITCODE -ne 0) { throw "local extract failed for $cam" }
      $pulled += $chunk.Count
    }
  }
  Remove-Item (Join-Path $tmpDir 'chunk.*') -ErrorAction SilentlyContinue
  Say ("Sync done - {0} new file(s)." -f $pulled) Cyan
}

# ------------------------------------------------------------------ gallery ---
if (-not (Test-Path $tplPath)) { throw "Gallery template not found: $tplPath" }

$camData = @()
$movies  = @()
foreach ($dir in Get-ChildItem -LiteralPath $Dest -Directory | Sort-Object Name) {
  if ($dir.Name -eq 'movies') {
    $movies = @(Get-ChildItem $dir.FullName -Filter *.mp4 | Sort-Object Name | Select-Object -ExpandProperty Name)
    continue
  }
  $frames = @(Get-ChildItem $dir.FullName -Filter *.jpg |
              Where-Object Name -ne 'latest.jpg' |
              Sort-Object Name | Select-Object -ExpandProperty Name)
  if ($frames.Count) {
    $camData += [ordered]@{ id = $dir.Name; label = (Prettify $dir.Name); frames = $frames }
  }
}
if (-not $camData.Count) { throw "No camera folders with frames under $Dest - nothing to build." }

$json = [ordered]@{
  generated = (Get-Date -Format 'yyyy-MM-dd HH:mm')
  cams      = @($camData)
  movies    = @($movies)
} | ConvertTo-Json -Depth 6 -Compress

$marker = 'const DATA = /*__DATA__*/ {"generated":"","cams":[],"movies":[]};'
$tpl    = Get-Content -LiteralPath $tplPath -Raw
if (-not $tpl.Contains($marker)) { throw "Data marker missing from $tplPath - template edited?" }

$index = Join-Path $Dest 'index.html'
[IO.File]::WriteAllText($index, $tpl.Replace($marker, "const DATA = $json;"), (New-Object Text.UTF8Encoding $false))

# Double-clickable launchers next to the pictures.
$self = $PSCommandPath
@"
@echo off
start "" "%~dp0index.html"
"@ | Set-Content (Join-Path $Dest 'Open Gallery.cmd') -Encoding ascii

@"
@echo off
where pwsh >nul 2>nul && (pwsh -NoProfile -ExecutionPolicy Bypass -File "$self") || (powershell -NoProfile -ExecutionPolicy Bypass -File "$self")
if errorlevel 1 pause
"@ | Set-Content (Join-Path $Dest 'Sync Now.cmd') -Encoding ascii

# Readable aliases beside the frames: <Dest>\by-time\<cam>\2026-08-27 22-40.jpg,
# hardlinked so they cost no space. The canonical <cam>_YYYYmmdd_HHMM.jpg name is
# parsed by the gallery, by the starter watcher and by this script's own
# already-have-it check, so it must not be renamed - hence a second name rather
# than a new one. Added 2026-08-28.
$aliaser = Join-Path $PSScriptRoot 'alias_by_time.py'
if (Test-Path $aliaser) {
  try {
    & uv run --no-project python $aliaser --root $Dest
    if ($LASTEXITCODE -ne 0) {
      Say ("  by-time aliases: FAILED (exit {0}) - frames synced, readable names not" -f $LASTEXITCODE) Yellow
    }
  } catch {
    Say ("  by-time aliases: FAILED - {0}" -f $_.Exception.Message) Yellow
  }
} else {
  Say ("  by-time aliases: SKIPPED - {0} is missing" -f $aliaser) Yellow
}

$total = ($camData | ForEach-Object { $_.frames.Count } | Measure-Object -Sum).Sum
Say ""
Say ("Gallery rebuilt: {0}" -f $index) Cyan
Say ("  {0} frames, {1} camera(s), {2} movie(s)" -f $total, $camData.Count, $movies.Count)
foreach ($c in $camData) { Say ("    {0,-16} {1,5} frames" -f $c.id, $c.frames.Count) }

if (-not $NoOpen) { Start-Process $index }
