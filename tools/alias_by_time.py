r"""Give every timelapse frame a second, human-readable name - without renaming it.

WHY NOT JUST RENAME THE FRAMES
------------------------------
`starter_20260827_2240.jpg` already carries the capture time, but `20260827_2240`
has to be decoded by eye, so in Explorer the time is effectively invisible and
you end up in Properties.

Renaming is still the wrong fix. The pattern `<cam>_YYYYmmdd_HHMM.jpg` is load
bearing in four places: starter_watch.py and starter_level.py parse it, the
gallery's stampOf() parses it, and the sync decides "do I already have this
frame" by basename - so renamed local copies would be re-downloaded under their
old names, duplicating every frame.

So: keep the canonical name, and hardlink a readable alias beside it.

    <root>\starter\starter_20260827_2240.jpg      <- canonical, parsers read this
    <root>\by-time\starter\2026-08-27 22-40.jpg   <- hardlink, same bytes, 0 extra disk

A hardlink is a second directory entry pointing at the same data, so this costs
no space (it matters - D: sits at 97% full), and opening or deleting either name
reaches the same picture. Sorting by name sorts by time, which the raw stamp
also did but unreadably.

IDEMPOTENT. Run it as often as you like; it only touches what changed.

    uv run --no-project python alias_by_time.py [--root <dir>] [--cams starter]
                                                [--quiet] [--no-prune]

EXIT STATUS (machine-wide rule: an error must never look like an empty result)
    0  linked / pruned / nothing to do - the alias tree matches the frames
    1  ran but at least one link failed - some frames have no alias
    2  COULD NOT LOOK - root missing or unreadable
"""
import argparse
import os
import re
import sys

STAMP = re.compile(r"_(\d{8})_(\d{4})\.jpg$", re.I)
ALIAS_DIR = "by-time"
SKIP = {ALIAS_DIR, "movies"}


def alias_name(fname):
    """starter_20260827_2240.jpg -> '2026-08-27 22-40.jpg'. None if unparseable."""
    m = STAMP.search(fname)
    if not m:
        return None
    d, t = m.group(1), m.group(2)
    return "%s-%s-%s %s-%s.jpg" % (d[0:4], d[4:6], d[6:8], t[0:2], t[2:4])


def same_file(a, b):
    try:
        sa, sb = os.stat(a), os.stat(b)
    except OSError:
        return False
    return sa.st_ino == sb.st_ino and sa.st_dev == sb.st_dev


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=r"D:\Claude\Pictures\timelapse")
    ap.add_argument("--cams", help="comma-separated camera folders; default = all of them")
    ap.add_argument("--quiet", action="store_true",
                    help="print only when something changed or broke. For calling in a loop - "
                         "but note that a failure still prints, because silence must never be "
                         "the success signal.")
    ap.add_argument("--no-prune", action="store_true",
                    help="keep aliases whose source frame has gone away")
    a = ap.parse_args()

    if not os.path.isdir(a.root):
        print("COULD NOT LOOK: not a directory: %s" % a.root)
        return 2
    try:
        entries = os.listdir(a.root)
    except OSError as e:
        print("COULD NOT LOOK: cannot read %s: %s" % (a.root, e))
        return 2

    if a.cams:
        cams = [c.strip() for c in a.cams.split(",") if c.strip()]
    else:
        cams = sorted(d for d in entries
                      if d not in SKIP and os.path.isdir(os.path.join(a.root, d)))
    if not cams:
        print("COULD NOT LOOK: no camera folders under %s" % a.root)
        return 2

    linked = pruned = failed = 0
    unparsed = []
    for cam in cams:
        src_dir = os.path.join(a.root, cam)
        if not os.path.isdir(src_dir):
            print("MISSING camera folder: %s" % src_dir)
            failed += 1
            continue
        dst_dir = os.path.join(a.root, ALIAS_DIR, cam)
        try:
            os.makedirs(dst_dir, exist_ok=True)
        except OSError as e:
            print("FAILED to create %s: %s" % (dst_dir, e))
            failed += 1
            continue

        wanted = {}
        for f in os.listdir(src_dir):
            if not f.lower().endswith(".jpg"):
                continue
            n = alias_name(f)
            if n is None:
                unparsed.append("%s/%s" % (cam, f))
                continue
            wanted[n] = os.path.join(src_dir, f)

        for n, src in sorted(wanted.items()):
            dst = os.path.join(dst_dir, n)
            if os.path.exists(dst):
                if same_file(src, dst):
                    continue
                try:                      # stale alias - the source was replaced
                    os.remove(dst)
                except OSError as e:
                    print("FAILED to replace stale alias %s: %s" % (dst, e))
                    failed += 1
                    continue
            try:
                os.link(src, dst)
                linked += 1
            except OSError as e:
                print("FAILED to link %s -> %s: %s" % (n, src, e))
                failed += 1

        if not a.no_prune:
            for f in os.listdir(dst_dir):
                if f not in wanted:
                    try:
                        os.remove(os.path.join(dst_dir, f))
                        pruned += 1
                    except OSError as e:
                        print("FAILED to prune %s: %s" % (f, e))
                        failed += 1

    if unparsed:
        print("NO TIMESTAMP IN NAME (%d, not aliased): %s"
              % (len(unparsed), ", ".join(unparsed[:5]) + (" ..." if len(unparsed) > 5 else "")))
    if failed:
        print("alias by-time: %d linked, %d pruned, %d FAILED - some frames have no alias"
              % (linked, pruned, failed))
        return 1
    if linked or pruned or not a.quiet:
        print("alias by-time: %d linked, %d pruned, %d camera(s) -> %s"
              % (linked, pruned, len(cams), os.path.join(a.root, ALIAS_DIR)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
