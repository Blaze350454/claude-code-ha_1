# tools/

Helper scripts for the grow systems.

## build_timelapse_movies.py — grow-end timelapse renderer

Combines every captured frame for each tent camera (the rolling 30-day window in
`/config/www/timelapse/<cam>/` **plus** the long-term archive
`/archive/<cam>/`) and renders three styles:

| mode | output | what it is |
|------|--------|------------|
| `per-camera` | `<cam>.mp4` | one timelapse per camera, native aspect |
| `interleave` | `interleaved.mp4` | all cameras merged in timestamp order (cam1→cam2→overhead→…) — one continuous grow film |
| `grid` | `grid.mp4` | all cameras side-by-side, hold-last per 30-min step |

It runs **inside the Home Assistant container** (which has `ffmpeg`, `python3`,
and the frame dirs mounted). Pipe it in over SSH:

```bash
# all three styles, defaults (fps 24, 1280x720 canvas for interleave/grid)
ssh homeadmin@192.168.2.151 \
  'docker exec -i homeassistant python3 - --mode all' \
  < tools/build_timelapse_movies.py

# just the interleaved film at 30 fps
ssh homeadmin@192.168.2.151 \
  'docker exec -i homeassistant python3 - --mode interleave --fps 30' \
  < tools/build_timelapse_movies.py
```

Output lands in `/config/www/timelapse/movies/`, downloadable at
`http://192.168.2.151:8123/local/timelapse/movies/<name>.mp4`.

Frames are auto-discovered (`<cam>_*.jpg` subfolders); `latest.jpg` pointers are
ignored. Interleave/grid letterbox each frame onto the `--size` canvas so
cameras of different resolutions combine cleanly. Re-run anytime — it overwrites.

Options: `--mode`, `--cameras tent_1 tent_overhead …`, `--fps`, `--size WxH`,
`--www`, `--archive`, `--out`, `--keep-temp`. See the script's docstring.

## sync_timelapse.ps1 + timelapse_gallery.html — offline browsing on Windows

Mirrors every frame to this PC and rebuilds a self-contained gallery page.

```powershell
pwsh -File tools\sync_timelapse.ps1              # sync + rebuild + open
pwsh -File tools\sync_timelapse.ps1 -GalleryOnly # rebuild index.html only
pwsh -File tools\sync_timelapse.ps1 -Dest E:\somewhere -NoOpen
```

Lands in `D:\Claude\Pictures\timelapse\` as `<cam>\` + `movies\` + `index.html`,
plus two double-clickable launchers (`Open Gallery.cmd`, `Sync Now.cmd`).

Pulls **both** remote roots — `~/homeassistant/.config/www/timelapse/<cam>/`
(current month) and `~/timelapse_archive/<cam>/` (rolled-off months) — so the
local copy is the full history in one flat folder per camera. Incremental: only
files missing locally are fetched, streamed as one tar per ~200 files (`-Batch`)
rather than one scp per file. Movies re-download when their remote size changes.

`index.html` is generated from `timelapse_gallery.html`, whose
`const DATA = /*__DATA__*/ …;` line the script replaces with the frame index —
**keep that line byte-identical** or the build throws. The page needs no server
and no network: open it straight off disk.

- **Timelapse** view — scrub/play the frames; "All cameras" syncs the panes to a
  shared time cursor and shows *not online yet* for a camera that predates the
  cursor. Space / arrows / Home / End.
- **Contact sheet** — every frame as a thumbnail, grouped by day; click for a
  full-size lightbox with "Play from here".
- **Movies** — plays whatever `build_timelapse_movies.py` last rendered.

Gotcha worth knowing: `scp … D:\path` fails, because scp splits its destination
on the first colon and reads `D:` as a hostname. Use `/d/path` from git-bash.
