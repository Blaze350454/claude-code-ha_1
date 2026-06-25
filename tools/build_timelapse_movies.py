#!/usr/bin/env python3
"""
Grow-end timelapse movie builder for the tent cameras.

Combines EVERY captured frame for each camera — the rolling 30-day window
(<www>/<cam>/) plus the long-term archive (<archive>/<cam>/) — and renders any
of three movie styles:

  per-camera : one timelapse .mp4 per camera, native aspect      -> <cam>.mp4
  interleave : all cameras merged in timestamp order, one film   -> interleaved.mp4
  grid       : all cameras side-by-side, hold-last per step      -> grid.mp4

Frames are named <cam>_<YYYYmmdd_HHMM>.jpg, so they sort chronologically. The
per-camera "latest.jpg" pointer is ignored (no _<timestamp> in the name).

WHERE TO RUN
------------
Run INSIDE the Home Assistant container (it has python3 + ffmpeg, and the frame
dirs are mounted there). Pipe this file to the container's python over SSH:

  ssh homeadmin@192.168.2.151 \
    'docker exec -i homeassistant python3 - --mode all' \
    < tools/build_timelapse_movies.py

Defaults assume the container paths:
  --www      /config/www/timelapse          (rolling window, per-cam subfolders)
  --archive  /archive                        (bind-mounted ~/timelapse_archive)
  --out      /config/www/timelapse/movies    (served at /local/timelapse/movies/)

So the finished films are downloadable at
  http://192.168.2.151:8123/local/timelapse/movies/<name>.mp4

OPTIONS
-------
  --mode {per-camera,interleave,grid,all}   default all
  --cameras tent_1 tent_overhead ...        default: auto-discover
  --fps N        playback frame rate            default 24
  --size WxH     canvas for interleave/grid     default 1280x720
  --keep-temp    don't delete the scratch dir (debug)

Interleave and grid letterbox every frame onto the --size canvas, so cameras of
different resolutions combine cleanly. Per-camera keeps each camera's native
aspect (rounded to even dimensions for h264).
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from glob import glob

TS_RE = re.compile(r'_(\d{8})_(\d{4})\.jpg$')


def ts_key(path):
    """Sortable 'YYYYmmddHHMM' key from a frame filename ('' if none)."""
    m = TS_RE.search(os.path.basename(path))
    return m.group(1) + m.group(2) if m else ''


def discover_cameras(www, archive):
    cams = set()
    for base in (www, archive):
        if not os.path.isdir(base):
            continue
        for d in sorted(os.listdir(base)):
            p = os.path.join(base, d)
            if os.path.isdir(p) and glob(os.path.join(p, '%s_*.jpg' % d)):
                cams.add(d)
    return sorted(cams)


def cam_frames(cam, www, archive):
    """All timestamped frames for a camera (archive + www), sorted, de-duped."""
    files = {}
    for base in (archive, www):  # www second so a dup keeps the live copy
        for f in glob(os.path.join(base, cam, '%s_*.jpg' % cam)):
            files[os.path.basename(f)] = f
    return [files[k] for k in sorted(files, key=ts_key)]


def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL,
                       stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-2500:])
        raise SystemExit('ffmpeg failed: ' + ' '.join(cmd[:8]) + ' ...')


def symlink_seq(paths, d):
    """Symlink frames into d as 000000.jpg, 000001.jpg, ... for ffmpeg image2."""
    os.makedirs(d, exist_ok=True)
    for i, p in enumerate(paths):
        os.symlink(os.path.abspath(p), os.path.join(d, '%06d.jpg' % i))
    return len(paths)


def encode_seq(seqdir, out, fps, vf):
    run(['ffmpeg', '-y', '-framerate', str(fps), '-start_number', '0',
         '-i', os.path.join(seqdir, '%06d.jpg'),
         '-vf', vf, '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
         '-movflags', '+faststart', out])


def normalize_cam(cam, frames, W, H, tmp):
    """Letterbox a camera's frames onto a WxH canvas (one ffmpeg pass).
    Returns [(ts_key, normalized_path), ...] aligned to the input order."""
    indir = os.path.join(tmp, 'in_' + cam)
    outdir = os.path.join(tmp, 'norm_' + cam)
    symlink_seq(frames, indir)
    os.makedirs(outdir, exist_ok=True)
    vf = ('scale=%d:%d:force_original_aspect_ratio=decrease,'
          'pad=%d:%d:-1:-1:color=black,setsar=1' % (W, H, W, H))
    run(['ffmpeg', '-y', '-start_number', '0',
         '-i', os.path.join(indir, '%06d.jpg'),
         '-vf', vf, os.path.join(outdir, '%06d.jpg')])
    norm = sorted(glob(os.path.join(outdir, '*.jpg')))
    return list(zip([ts_key(f) for f in frames], norm))


def build_per_camera(cams, www, archive, out, fps, tmp):
    print('[per-camera]')
    for cam in cams:
        frames = cam_frames(cam, www, archive)
        if not frames:
            print('  %s: no frames, skipped' % cam)
            continue
        d = os.path.join(tmp, 'seq_' + cam)
        symlink_seq(frames, d)
        encode_seq(d, os.path.join(out, '%s.mp4' % cam), fps,
                   'scale=trunc(iw/2)*2:trunc(ih/2)*2')
        print('  -> %s.mp4 (%d frames)' % (cam, len(frames)))


def build_interleave(normed, out, fps, tmp):
    print('[interleave]')
    allf = sorted((ts, p) for lst in normed.values() for ts, p in lst)
    if not allf:
        print('  no frames, skipped')
        return
    d = os.path.join(tmp, 'seq_interleave')
    symlink_seq([p for _, p in allf], d)
    encode_seq(d, os.path.join(out, 'interleaved.mp4'), fps, 'setsar=1')
    print('  -> interleaved.mp4 (%d frames)' % len(allf))


def build_grid(cams, normed, out, fps, tmp):
    print('[grid]')
    timeline = sorted({ts for lst in normed.values() for ts, _ in lst})
    if not timeline:
        print('  no frames, skipped')
        return
    seqdirs = []
    for cam in cams:
        lst = normed.get(cam)
        if not lst:
            continue
        d = os.path.join(tmp, 'grid_' + cam)
        os.makedirs(d, exist_ok=True)
        j, cur = 0, lst[0][1]            # hold-first before the camera's start
        for i, t in enumerate(timeline):
            while j < len(lst) and lst[j][0] <= t:   # hold-last
                cur = lst[j][1]
                j += 1
            os.symlink(os.path.abspath(cur), os.path.join(d, '%06d.jpg' % i))
        seqdirs.append(d)
    n = len(seqdirs)
    inputs = []
    for d in seqdirs:
        inputs += ['-framerate', str(fps), '-start_number', '0',
                   '-i', os.path.join(d, '%06d.jpg')]
    if n == 1:
        fc = '[0:v]setsar=1[v]'
    else:
        fc = ''.join('[%d:v]' % i for i in range(n)) + 'hstack=inputs=%d[v]' % n
    run(['ffmpeg', '-y', *inputs, '-filter_complex', fc, '-map', '[v]',
         '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
         os.path.join(out, 'grid.mp4')])
    print('  -> grid.mp4 (%d steps x %d cams)' % (len(timeline), n))


def main():
    ap = argparse.ArgumentParser(description='Build grow-end timelapse movies.')
    ap.add_argument('--mode', default='all',
                    choices=['per-camera', 'interleave', 'grid', 'all'])
    ap.add_argument('--www', default='/config/www/timelapse')
    ap.add_argument('--archive', default='/archive')
    ap.add_argument('--out', default='/config/www/timelapse/movies')
    ap.add_argument('--cameras', nargs='*')
    ap.add_argument('--fps', type=int, default=24)
    ap.add_argument('--size', default='1280x720')
    ap.add_argument('--keep-temp', action='store_true')
    a = ap.parse_args()

    W, H = (int(x) for x in a.size.lower().split('x'))
    cams = a.cameras or discover_cameras(a.www, a.archive)
    if not cams:
        raise SystemExit('No camera folders with <cam>_*.jpg under %s or %s'
                         % (a.www, a.archive))
    os.makedirs(a.out, exist_ok=True)
    print('cameras: %s | fps=%d | canvas=%dx%d | out=%s'
          % (', '.join(cams), a.fps, W, H, a.out))

    tmp = tempfile.mkdtemp(prefix='tlmovies_')
    try:
        if a.mode in ('per-camera', 'all'):
            build_per_camera(cams, a.www, a.archive, a.out, a.fps, tmp)

        if a.mode in ('interleave', 'grid', 'all'):
            # normalize once; reused by interleave and grid
            normed = {}
            for cam in cams:
                frames = cam_frames(cam, a.www, a.archive)
                if frames:
                    normed[cam] = normalize_cam(cam, frames, W, H, tmp)
            if a.mode in ('interleave', 'all'):
                build_interleave(normed, a.out, a.fps, tmp)
            if a.mode in ('grid', 'all'):
                build_grid(cams, normed, a.out, a.fps, tmp)

        print('done. movies in %s' % a.out)
    finally:
        if a.keep_temp:
            print('kept temp: %s' % tmp)
        else:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    main()
