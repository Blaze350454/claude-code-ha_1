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

Three more were paid for on the night of 2026-08-27/28, all the same shape:
something OTHER than the culture brightened part of the band, and a top-down
search believed it.

 4. Splash residue can dry BRIGHTER, not darker. Fault 3 watched a film dry
    matte and translucent; feed 13's jar was coated far more heavily, and its
    film dried opaque and pale, brightening rows 300-345 by 10-15 levels over
    nine hours. The signed difference from fault 3 passes that straight through.
 5. Daylight moves. A control patch OUTSIDE the jar drifted +8 levels from dawn
    and +15 through the afternoon, and the jar - a white body behind glass -
    swung +24. That clears MIN_DELTA on its own, on any sunny day, whatever the
    reference is. Normalising it away does not work either: the top of the jar
    carries the thickest residue, so it brightens for two unrelated reasons at
    once, and subtracting it takes the real signal to nothing. Measured.
 6. Both of those brighten a region ABOVE the culture, and the old top-down scan
    returned the FIRST run it met coming down - so it locked onto residue at the
    ceiling of the band and read 122.9 % of fill for ten hours while the true
    level was near 20 %. It also handed the turn's fast path a 396 px/h peak
    rate, so the next frame's zero rate called a peak at +9 h that never
    happened.

The answers to 4-6 are structural, not another threshold:

  * The front is found by walking UP FROM THE MARK, stopping at the first gap.
    The body is physically continuous with the mark it was levelled to, so a
    disconnected bright patch higher up can never be taken for it, whatever
    caused the patch.
  * A reading implying the front jumped more than MAX_STEP_PX since the last
    accepted one is refused outright.
  * A front at the very ceiling of a hand-set band is could-not-look, because Y0
    is chosen as a row no plausible rise reaches: arriving there means the band
    is wrong, not that the starter is at 122 %.

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

# --- Refusing a reading the culture cannot have produced ---------------------
# The fastest rise ever recorded here is 12 px/h (feed 7), so 30 px between one
# accepted reading and the next is ten times the fastest real pace at the 15 min
# cadence - it cannot clip a rise. Every artefact measured on 2026-08-28 cleared
# it by a wide margin: 73, 328, 416 and 736 px/h.
#
# Deliberately a bound PER STEP, not per hour. Per hour the allowance grows while
# readings are being refused, so a long contaminated stretch ends by admitting
# exactly the reading it refused at the start. That leak was measured: it let a
# 442 px front through after a 2.25 h gap.
MAX_STEP_PX = 30
REJECT_MAX_H = 3.0    # refusing this long in a row is lost tracking, and says so

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
# called, which is proportionate on a 30 h cycle.
#
# THE RATE "FAST PATH" WAS DELETED 2026-08-29, and must not come back. It called
# a turn when the rate fell below a quarter of its peak, and on feed 14 - the
# first cycle of the rebuilt rig - it called a peak at +5 h 45 m on a front that
# was still climbing monotonically, every single frame. What tripped it was one
# 10 px step between two frames, which set peak_rate to 22 px/h; the ordinary
# 4 px/h pace that followed is under a quarter of that. A BRIEF ACCELERATION
# FOLLOWED BY A RETURN TO NORMAL PACE reads to it as a collapse.
#
# It cannot recover, either: peak_rate is a running MAXIMUM, so once set high
# the phase stays `turned` for the rest of the cycle whatever the culture does,
# and the real turn becomes unobservable.
#
# It was also silently mis-scaled by geometry. 8 px/h was 4.6 % of fill per hour
# on a 175 px fill; on the 295 px fill of the cardboard-slot rig it is 2.7 %/h.
# A rule that needs re-deriving every time the jar moves is the wrong rule.
#
# The stall rule was tracking correctly underneath it the whole time - 0.25 h
# against a 1.5 h limit - and would not have fired. It is now the only rule.
NEW_MAX_PX = 2        # improvement that counts as a new maximum; 1 px would let
                      # jitter on a plateau keep resetting the stall clock
STALL_MIN_H = 1.5     # never call a turn on less stillness than this
STALL_MAX_H = 4.0     # ... and never wait longer than this, however slow it is
STALL_DEFAULT_H = 2.0 # used until there are two maxima to measure an interval from
TURN_MIN_RISE = 10.0  # % of fill; below this a "stall" is noise, not a peak


def out(**kw):
    """Emit the sensor payload and stop. Always exit 0 - see the module docstring."""
    payload = {"state": None, "phase": "could-not-look", "error": None,
               "rise_pct": None, "front_row": None, "brightening": None,
               "elapsed_h": None, "rate_px_h": None, "peak_rate_px_h": None,
               "stall_h": None, "stall_limit_h": None,
               "control_drift": None, "refused_frames": 0, "reading_age_h": None,
               "elapsed_from": "reference", "ref_offset_h": None,
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
    """Top of the brightened column ROOTED AT THE MARK - see faults 4-6 above.

    Walks up from y1 (just above the mark) and returns the top of the first run
    of MIN_RUN changed rows, stopping at the first gap. Scanning the other way
    returns whatever is highest in the band, which on a smeared jar is residue
    or glare rather than culture.

    The rows immediately above the mark are usually NOT changed - they were body
    in the reference too - so the run is sought below the front, not at y1.
    """
    d = (frame[:, x0:x1] - ref[:, x0:x1]).mean(axis=1)
    y1 = min(y1, len(d))
    y0 = max(0, y0)
    hot = d >= MIN_DELTA
    run, top = 0, None
    for y in range(y1 - 1, y0 - 1, -1):
        if hot[y]:
            run, top = run + 1, y
        else:
            if run >= MIN_RUN:
                break
            run, top = 0, None
    return (top if run >= MIN_RUN else None), float(d[y0:y1].max())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frames", default="/config/www/timelapse/starter")
    ap.add_argument("--ref", default="")
    ap.add_argument("--band", default="")
    ap.add_argument("--fed", default="",
                    help="When the culture was fed, 'YYYY-MM-DD HH:MM[:SS]'. Elapsed time is "
                         "reported FROM THIS when given, and from the reference frame only as "
                         "a fallback. The reference is set an hour or more after the feed, and "
                         "after a mid-cycle recalibration it can be many hours after - so the "
                         "fallback understates time-to-peak, which is the number this whole "
                         "script exists to produce. See elapsed_from in the payload.")
    ap.add_argument("--control", default="",
                    help="X0,X1,Y0,Y1 of a patch OUTSIDE the jar. Diagnostic only - it "
                         "reports how far the scene lighting has drifted from the "
                         "reference, which is what fault 5 above looks like from HA. It is "
                         "NOT subtracted from the band: see fault 5 for why that fails.")
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

    fed_t = None
    fed_raw = (a.fed or "").strip()
    if fed_raw and fed_raw not in ("unknown", "unavailable", "none", "-"):
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
            try:
                fed_t = datetime.strptime(fed_raw, fmt)
                break
            except ValueError:
                continue
        if fed_t is None:
            out(error="--fed is not a date I can read: %r (want 'YYYY-MM-DD HH:MM')" % fed_raw)

    ctl = None
    if (a.control or "").strip():
        cparts = [c.strip() for c in a.control.split(",") if c.strip()]
        if len(cparts) != 4 or not all(c.lstrip("-").isdigit() for c in cparts):
            out(error="--control needs 4 integers X0,X1,Y0,Y1 - got %r" % a.control)
        ctl = tuple(int(c) for c in cparts)
        if not (ctl[0] < ctl[1] and ctl[2] < ctl[3]):
            out(error="--control must satisfy X0<X1 and Y0<Y1 - got %r" % a.control)

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

    ctl_ref = None
    if ctl:
        cx0, cx1, cy0, cy1 = ctl
        if not (0 <= cx0 < cx1 <= ref.shape[1] and 0 <= cy0 < cy1 <= ref.shape[0]):
            out(reference=ref_name, error="--control is outside a %dx%d frame: %r"
                % (ref.shape[1], ref.shape[0], a.control))
        ctl_ref = float(ref[cy0:cy1, cx0:cx1].mean())

    hist, best_row, latest = [], None, None
    bright = 0.0
    drift = None            # scene lighting, latest frame vs the reference
    last_ok_t = None        # when the front was last actually READ, not merely captured
    accepted = None         # ... and what it read, which the step bound is measured from
    refused = 0
    for f in series:
        try:
            im = np.asarray(Image.open(f).convert("L"), dtype=np.float32)
        except Exception:                         # a half-written frame; skip this one only
            continue
        if im.shape != ref.shape:
            continue
        t = stamp(f)
        y, dmax = front_row(ref, im, x0, x1, y0, y1)
        latest = (t, os.path.basename(f), y, dmax)
        bright = max(bright, dmax)
        if ctl_ref is not None:
            drift = round(float(im[cy0:cy1, cx0:cx1].mean()) - ctl_ref, 1)
        if y is None:
            continue
        # A jump the culture cannot have made is residue or light, not a level.
        # Refusing it costs one reading; believing it costs the whole cycle.
        if accepted is not None and y < accepted - MAX_STEP_PX:
            refused += 1
            continue
        accepted, last_ok_t = y, t
        hist.append((t, y))
        best_row = y if best_row is None else min(best_row, y)

    if latest is None:
        out(reference=ref_name, error="every frame since the reference failed to decode")

    # Elapsed is measured FROM THE FEED whenever HA knows it. Measuring from the
    # reference is only a fallback: the reference is set an hour or more after
    # the feed, so it runs short - and after a mid-cycle recalibration it ran
    # NINE hours short on 2026-08-28, in the one number that matters.
    if fed_t is not None:
        elapsed = (latest[0] - fed_t).total_seconds() / 3600.0
        elapsed_from = "feed"
        ref_offset = round((ref_t - fed_t).total_seconds() / 3600.0, 2)
    else:
        elapsed = (latest[0] - ref_t).total_seconds() / 3600.0
        elapsed_from = "reference"
        ref_offset = None
    fill = float(base - surf)
    age = None if last_ok_t is None else (latest[0] - last_ok_t).total_seconds() / 3600.0
    common = dict(brightening=round(bright, 1), elapsed_h=round(elapsed, 2),
                  elapsed_from=elapsed_from, ref_offset_h=ref_offset,
                  control_drift=drift, refused_frames=refused,
                  reading_age_h=None if age is None else round(age, 2),
                  frames=len(series), reference=ref_name, latest_frame=latest[1])

    if best_row is None:
        out(phase="quiet", state=0.0, rise_pct=0.0, **common)

    # Y0 is set by hand as a row no plausible rise reaches, so arriving there is
    # not a 122 % starter - it is a band that no longer describes this jar, or a
    # brightening that runs off the top of it. Say so; do not publish a number.
    if best_row <= y0:
        out(phase="could-not-look", front_row=best_row,
            error="the front reached row %d, the very top of the search band - the band "
                  "is describing the wrong jar, or something above the culture has "
                  "brightened. Re-set the reference and band for the current jar." % y0,
            **common)

    # Readings can be refused for a while - a passing patch of sun does it - but
    # once that runs long enough, the number on the dashboard is history, and a
    # stale number presented as current is the failure this whole file exists to
    # avoid.
    if age is not None and age >= REJECT_MAX_H:
        out(phase="could-not-look", front_row=best_row,
            error="no usable reading for %.1f h (%d frames refused as impossible jumps); "
                  "scene lighting has drifted %s levels from the reference"
                  % (age, refused, "unmeasured" if drift is None else "%+.1f" % drift),
            **common)

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

    # Stall is measured from the last frame that was actually READ. Counting
    # refused frames toward it would let a sunny afternoon call a turn.
    stall_h = stall_limit = None
    if maxima:
        stall_h = (last_ok_t - maxima[-1][0]).total_seconds() / 3600.0
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

    # THE ONLY RULE: it has risen far enough to have a peak worth calling, and
    # has made no new maximum for longer than its own recent rhythm allows.
    # rate and peak are still computed and reported, but they are DIAGNOSTICS
    # ONLY and must never decide the phase again - see the deleted fast path.
    if rise >= TURN_MIN_RISE and stall_h is not None and stall_limit is not None \
            and stall_h >= stall_limit:
        phase = "turned"

    out(phase=phase, state=rise, rise_pct=rise, front_row=best_row,
        rate_px_h=None if rate is None else round(rate, 1),
        peak_rate_px_h=None if peak is None else round(peak, 1),
        stall_h=None if stall_h is None else round(stall_h, 2),
        stall_limit_h=None if stall_limit is None else round(stall_limit, 2),
        **common)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:                        # noqa: BLE001 - a crash must still be a reading
        out(error="unhandled: %r" % (e,))
