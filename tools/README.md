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
