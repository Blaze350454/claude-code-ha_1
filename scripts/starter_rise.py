#!/usr/bin/env python3
"""Measure the sourdough starter's rise from the P1S timelapse, for a command_line sensor.

Emits ONE line of JSON on stdout and ALWAYS exits 0. That is deliberate: a
command_line sensor whose command fails goes `unavailable` and throws the reason
away, which is the "an error became an empty result" failure the house rules
exist to prevent. Instead every outcome - including every failure - is a `phase`
plus a human-readable `error`, so HA can display what went wrong.

    phase: no-reference    the reference frame is unset or missing
           could-not-look  the folder, band or frames could not be read
           quiet           reference is good, nothing has crossed the noise floor
           rising          the level has moved and is still moving
           turned          the rise rate has collapsed - this is the peak

HOW IT MEASURES (see the Recipes starter log, 2026-08-27/28, for the full story)
The camera is fixed and the chamber light is held on, so anything that CHANGES
between two frames is the culture moving. Compare each frame to a reference and
find the highest row that has materially changed; that row is the top of the
moving mass, without ever having to segment a pale surface against pale glass.

Three faults were paid for on the first night, all of which produced confident,
plausible, WRONG numbers, and none of which was findable by reading the output:

 1. Auto-detecting the jar's columns latched onto the DIAL THERMOMETER standing
    beside it, and would have measured a needle all night. Hence the band is
    pinned by hand and never detected. There is no auto mode here on purpose.
 2. The change threshold was set at 12 when the real contrast (residue-coated
    glass ~114 against body ~125) is about 11, so it would have sat silent
    through the entire rise. Hence MIN_DELTA 9: above the 6.5 noise floor and
    below the signal.
 3. Differencing on ABSOLUTE value read splash residue DRYING on the glass as a
    75 % rise - wet film is glossy and bright, dried film matte and translucent,
    so the jar darkened 5 grey levels over two hours while control regions held
    to 0.2. Hence the difference is SIGNED: a rise replaces residue-coated glass
    with body and can only BRIGHTEN the region. That kills the whole class of
    false positive by physics rather than by tuning a threshold.

BAND: --band X0,X1,Y0,Y1,SURFACE,BASE is per-jar and must be re-set every feed,
because the jar is replaced every feed and the mark is redrawn. X0,X1 bound the
jar's columns clear of both glass edges and of the thermometer; Y0,Y1 bound the
search between a row no plausible rise reaches and just above the fill mark;
SURFACE is the row of the mark at t=0 and BASE the row of the jar's base, which
together set the fill depth that rise % is measured against.
"""
import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime

STAMP = re.compile(r"_(\d{8})_(\d{4})\.jpg$", re.I)
MIN_DELTA = 9.0       # grey levels of BRIGHTENING that count as changed
MIN_RUN = 6           # consecutive rows required, so one glare flicker cannot fire

# --- Calling the turn -------------------------------------------------------
# The turn is "it stopped making new maxima", NOT "its rate collapsed".
#
# The rate rule alone was measured on 2026-08-28 to be SILENT at three of the
# four paces this starter has actually run at. It required a peak of more than
# 8 px/h before a collapse counted, and on a 175 px fill that is 4.6 % of fill
# per hour: feed 7's pace peaks at 12 px/h and fires, but feed 8's peaks at
# exactly 8.0 and fails the comparison, and feed 11's peaks at 4.0. In those
# cases the phase stayed `rising` through a six-hour dead-flat plateau - which
# is the silence that looks exactly like a calm jar, and it bites hardest when
# the culture is degraded, i.e. when the measurement matters most.
#
# The stall rule has no absolute rate in it, so it works at any pace, and the
# window ADAPTS: three times the recent interval between new maxima. A fast
# rise makes a new maximum every few minutes and is called ~1.5 h after peak;
# a crawl makes one every hour or so and is given up to 4 h before being
# called, which is proportionate on a 30 h cycle. The rate rule is kept as a
# fast path, since when it does fire it fires sooner.
NEW_MAX_PX = 2        # improvement that counts as a new maximum; 1 px would let
                      # jitter on a plateau keep resetting the stall clock
STALL_MIN_H = 1.5     # never call a turn on less stillness than this
STALL_MAX_H = 4.0     # ... and never wait longer than this, however slow it is
STALL_DEFAULT_H = 2.0 # used until there are two maxima to measure an interval from
TURN_MIN_RISE = 10.0  # % of fill; below this a "stall" is noise, not a peak
TURN_MIN_RATE = 8.0   # fast path only: px/h the rise must have reached ...
TURN_FRACTION = 0.25  # ... before a collapse to this share of peak counts


def out(**kw):
    """Emit the sensor payload and stop. Always exit 0 - see the module docstring."""
    payload = {"state": None, "phase": "could-not-look", "error": None,
               "rise_pct": None, "front_row": None, "brightening": None,
               "elapsed_h": None, "rate_px_h": None, "peak_rate_px_h": None,
               "stall_h": None, "stall_limit_h": None,
               "frames": 0, "latest_frame": None, "reference": None,
               "measured_at": datetime.now().strftime("%Y-%m-%d %H:%M")}
    payload.update(kw)
    if payload["state"] is None:
        payload["state"] = "unknown"
    sys.stdout.write(json.dumps(payload))
    sys.exit(0)


def stamp(path):
    m = STAMP.search(os.path.basename(path))
    return datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M") if m else None


def front_row(ref, frame, x0, x1, y0, y1):
    """Highest row whose mean BRIGHTENING clears MIN_DELTA for MIN_RUN rows."""
    d = (frame[:, x0:x1] - ref[:, x0:x1]).mean(axis=1)
    y1 = min(y1, len(d))
    hot = d >= MIN_DELTA
    run = 0
    for y in range(max(0, y0), y1):
        run = run + 1 if hot[y] else 0
        if run >= MIN_RUN:
            return y - MIN_RUN + 1, float(d[y0:y1].max())
    return None, float(d[y0:y1].max())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frames", default="/config/www/timelapse/starter")
    ap.add_argument("--ref", default="")
    ap.add_argument("--band", default="")
    a = ap.parse_args()

    try:
        import numpy as np
        from PIL import Image
    except ImportError as e:
        out(error="missing dependency inside the HA container: %s" % e)

    ref_name = (a.ref or "").strip()
    if not ref_name or ref_name in ("unknown", "unavailable", "none", "-"):
        out(phase="no-reference",
            error="no reference frame set - press 'Set Reference To Latest Frame' about an "
                  "hour after feeding, once the splash has drained off the glass")

    parts = [p.strip() for p in (a.band or "").split(",") if p.strip()]
    if len(parts) != 6:
        out(error="--band needs 6 numbers X0,X1,Y0,Y1,SURFACE,BASE - got %r" % a.band)
    try:
        x0, x1, y0, y1, surf, base = (int(p) for p in parts)
    except ValueError:
        out(error="--band values must all be integers - got %r" % a.band)
    if not (x0 < x1 and y0 < y1 and surf < base):
        out(error="--band must satisfy X0<X1, Y0<Y1, SURFACE<BASE - got %r" % a.band)

    if not os.path.isdir(a.frames):
        out(error="not a directory: %s" % a.frames)
    ref_path = os.path.join(a.frames, ref_name)
    if not os.path.exists(ref_path):
        out(phase="no-reference", reference=ref_name,
            error="reference frame is no longer in %s: %s" % (a.frames, ref_name))

    ref_t = stamp(ref_path)
    if ref_t is None:
        out(reference=ref_name, error="reference name carries no timestamp: %s" % ref_name)

    try:
        ref = np.asarray(Image.open(ref_path).convert("L"), dtype=np.float32)
    except Exception as e:                        # noqa: BLE001 - report, never swallow
        out(reference=ref_name, error="cannot read reference %s: %s" % (ref_name, e))
    if not (0 <= x0 < x1 <= ref.shape[1] and 0 <= y0 < y1 <= ref.shape[0]):
        out(reference=ref_name,
            error="band is outside a %dx%d frame: %r" % (ref.shape[1], ref.shape[0], a.band))

    files = sorted((f for f in glob.glob(os.path.join(a.frames, "*.jpg")) if stamp(f)),
                   key=stamp)
    series = [f for f in files if stamp(f) >= ref_t]
    if not series:
        out(reference=ref_name, error="no frames at or after the reference")

    hist, best_row, latest = [], None, None
    bright = 0.0
    for f in series:
        try:
            im = np.asarray(Image.open(f).convert("L"), dtype=np.float32)
        except Exception:                         # a half-written frame; skip this one only
            continue
        if im.shape != ref.shape:
            continue
        y, dmax = front_row(ref, im, x0, x1, y0, y1)
        latest = (stamp(f), os.path.basename(f), y, dmax)
        bright = max(bright, dmax)
        if y is not None:
            hist.append((stamp(f), y))
            best_row = y if best_row is None else min(best_row, y)

    if latest is None:
        out(reference=ref_name, error="every frame since the reference failed to decode")

    elapsed = (latest[0] - ref_t).total_seconds() / 3600.0
    fill = float(base - surf)

    if best_row is None:
        out(phase="quiet", state=0.0, rise_pct=0.0, brightening=round(bright, 1),
            elapsed_h=round(elapsed, 2), frames=len(series), reference=ref_name,
            latest_frame=latest[1])

    # Rise is measured from the HIGHEST point reached, not from the latest reading.
    # This starter has never been observed to fall, so a lower later reading is
    # noise - and a phase allowed to run backwards would re-fire every alert built
    # on it. Monotonic by construction rather than by de-bouncing in the automation.
    rise = round(100.0 * (surf - best_row) / fill, 1)

    # Every point at which the level reached a new maximum, at least NEW_MAX_PX
    # better than the previous one. The gaps between these are the natural clock
    # of this particular rise, whatever its pace.
    maxima = []
    cur = None
    for t, y in hist:
        if cur is None or y <= cur - NEW_MAX_PX:
            cur = y
            maxima.append((t, y))

    stall_h = stall_limit = None
    if maxima:
        stall_h = (latest[0] - maxima[-1][0]).total_seconds() / 3600.0
        gaps = [(maxima[i + 1][0] - maxima[i][0]).total_seconds() / 3600.0
                for i in range(len(maxima) - 1)]
        if gaps:
            recent = sorted(gaps[-5:])
            typical = recent[len(recent) // 2]          # median, so one long gap cannot skew it
            stall_limit = min(max(3.0 * typical, STALL_MIN_H), STALL_MAX_H)
        else:
            stall_limit = STALL_DEFAULT_H

    rate = peak = None
    phase = "rising"
    if len(hist) >= 5:
        def slope(i, j):
            dt = (hist[j][0] - hist[i][0]).total_seconds() / 3600.0
            return (hist[i][1] - hist[j][1]) / dt if dt > 0 else 0.0
        rate = slope(-3, -1)
        peak = max((slope(k, k + 2) for k in range(len(hist) - 3)), default=0.0)

    # Primary rule: it has risen far enough to have a peak worth calling, and has
    # made no new maximum for longer than its own recent rhythm allows.
    if rise >= TURN_MIN_RISE and stall_h is not None and stall_limit is not None \
            and stall_h >= stall_limit:
        phase = "turned"
    # Fast path, for a rise quick enough that the rate rule resolves it sooner.
    elif rate is not None and peak is not None \
            and peak > TURN_MIN_RATE and rate < TURN_FRACTION * peak:
        phase = "turned"

    out(phase=phase, state=rise, rise_pct=rise, front_row=best_row,
        brightening=round(bright, 1), elapsed_h=round(elapsed, 2),
        rate_px_h=None if rate is None else round(rate, 1),
        peak_rate_px_h=None if peak is None else round(peak, 1),
        stall_h=None if stall_h is None else round(stall_h, 2),
        stall_limit_h=None if stall_limit is None else round(stall_limit, 2),
        frames=len(series), reference=ref_name, latest_frame=latest[1])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:                        # noqa: BLE001 - a crash must still be a reading
        out(error="unhandled: %r" % (e,))
