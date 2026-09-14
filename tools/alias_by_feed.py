r"""Group the starter's timelapse frames into one folder per feed - without renaming them.

WHY
---
`starter\` is one flat run of every frame ever taken, so two cycles that behaved
completely differently sit interleaved by date with nothing marking where one
ended and the next began. Comparing "feed 13" against "feed 14" means knowing
the feed times by heart and reading timestamps.

The frames also carry a WALL CLOCK, and this project is reasoned in ELAPSED
offsets - the peak is "+12 h 36 m", never "at 11:16". So the alias carries the
offset from that feed, and sorting the folder by name sorts by elapsed time.

    <root>\starter\starter_20260828_1116.jpg                    <- canonical
    <root>\by-feed\feed-13\+13h31m starter_20260828_1116.jpg    <- hardlink

Same bytes, no extra disk (D: is tight). Deleting either name leaves the other.

DO NOT RENAME THE CANONICAL FRAMES. `<cam>_YYYYmmdd_HHMM.jpg` is parsed by
starter_rise.py on HA, by starter_watch.py and starter_level.py here, by the
gallery's stampOf(), by the sync's already-have-it check, and by
alias_by_time.py. A rename breaks a running measurement and makes the sync
re-download every frame under its old name.

WHERE THE FEED TIMES COME FROM
------------------------------
`docs\starter-log.md` in the Recipes project, which is the single source of
truth for them - rows of the form:

    | 13 | **2026-08-27, 21:45** | ...

⚠ That is also why the log must not contain OTHER tables whose rows start
`| <number> |` - they get read as feeds. Prefix summary rows (`| F7 |`). This
has already broken a parser once, on 2026-08-27.

A frame belongs to the LAST feed at or before it. Frames captured before the
first dated feed are left alone rather than guessed at. A feed still missing
from the log therefore collects its frames into the previous feed's folder,
which is the honest answer - the fix is to log the feed, not to guess here.

IDEMPOTENT. Run it as often as you like; it only touches what changed.

    uv run --no-project python alias_by_feed.py [--root <dir>] [--log <file>]
                                                [--quiet] [--no-prune]

EXIT STATUS (machine-wide rule: an error must never look like an empty result)
    0  linked / pruned / nothing to do - the tree matches the frames
    1  ran but at least one link failed, or the log had no usable feed rows
    2  COULD NOT LOOK - root or log missing or unreadable
"""
import argparse
import os
import re
import sys
from datetime import datetime

STAMP = re.compile(r"_(\d{8})_(\d{4})\.jpg$", re.I)
FEED = re.compile(r"^\|\s*(\d+)\s*\|\s*\*\*(\d{4}-\d{2}-\d{2}),\s*(\d{2}:\d{2})\*\*")
ALIAS_DIR = "by-feed"
CAM = "starter"
DEFAULT_LOG = r"D:\Claude\Projects\Recipes\docs\starter-log.md"


def die(msg, code=2):
    sys.stderr.write("alias_by_feed: %s\n" % msg)
    sys.exit(code)


def read_feeds(path):
    """[(n, datetime)] sorted by time. Raises OSError if the log cannot be read."""
    feeds = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = FEED.match(line)
            if m:
                feeds.append((int(m.group(1)),
                              datetime.strptime(m.group(2) + " " + m.group(3),
                                                "%Y-%m-%d %H:%M")))
    feeds.sort(key=lambda f: f[1])
    return feeds


def stamp_of(fname):
    m = STAMP.search(fname)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M")
    except ValueError:
        return None


def offset_name(delta, fname):
    """0:  '+08h06m starter_20260828_0646.jpg'. Zero-padded so name order = time order."""
    total = int(delta.total_seconds() // 60)
    sign = "+" if total >= 0 else "-"
    total = abs(total)
    return "%s%02dh%02dm %s" % (sign, total // 60, total % 60, fname)


def same_file(a, b):
    try:
        sa, sb = os.stat(a), os.stat(b)
    except OSError:
        return False
    return sa.st_ino == sb.st_ino and sa.st_dev == sb.st_dev


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=r"D:\Claude\Pictures\timelapse")
    ap.add_argument("--log", default=DEFAULT_LOG)
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--no-prune", action="store_true")
    a = ap.parse_args()

    src = os.path.join(a.root, CAM)
    if not os.path.isdir(src):
        die("no %s folder under %s" % (CAM, a.root))
    if not os.path.isfile(a.log):
        die("feed log not found: %s" % a.log)
    try:
        feeds = read_feeds(a.log)
    except OSError as e:
        die("cannot read %s: %s" % (a.log, e))
    if not feeds:
        sys.stderr.write("alias_by_feed: no dated feed rows in %s - nothing to group by\n" % a.log)
        sys.exit(1)

    try:
        frames = sorted(f for f in os.listdir(src) if STAMP.search(f))
    except OSError as e:
        die("cannot list %s: %s" % (src, e))

    linked = failed = skipped = 0
    wanted = {}                                   # abs alias path -> source path
    for f in frames:
        t = stamp_of(f)
        if t is None:
            continue
        prior = [(n, ft) for n, ft in feeds if ft <= t]
        if not prior:
            skipped += 1                          # older than the first dated feed
            continue
        n, ft = prior[-1]
        d = os.path.join(a.root, ALIAS_DIR, "feed-%02d" % n)
        wanted[os.path.join(d, offset_name(t - ft, f))] = os.path.join(src, f)

    for dst, s in sorted(wanted.items()):
        if os.path.exists(dst):
            if same_file(dst, s):
                continue
            try:
                os.remove(dst)                    # stale link, e.g. a feed time corrected
            except OSError as e:
                sys.stderr.write("  cannot replace %s: %s\n" % (dst, e))
                failed += 1
                continue
        try:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            os.link(s, dst)
            linked += 1
        except OSError as e:
            sys.stderr.write("  link failed %s: %s\n" % (os.path.basename(dst), e))
            failed += 1

    pruned = 0
    base = os.path.join(a.root, ALIAS_DIR)
    if not a.no_prune and os.path.isdir(base):
        for d, _, files in os.walk(base):
            for f in files:
                p = os.path.join(d, f)
                if p not in wanted:
                    try:
                        os.remove(p)
                        pruned += 1
                    except OSError as e:
                        sys.stderr.write("  cannot prune %s: %s\n" % (p, e))
                        failed += 1
        for d, dirs, files in os.walk(base, topdown=False):
            if d != base and not dirs and not files:
                try:
                    os.rmdir(d)
                except OSError:
                    pass

    if not a.quiet:
        folders = sorted({os.path.basename(os.path.dirname(p)) for p in wanted})
        print("alias by-feed: %d linked, %d pruned, %d before the first feed -> %s"
              % (linked, pruned, skipped, base))
        for name in folders:
            n = sum(1 for p in wanted if os.path.basename(os.path.dirname(p)) == name)
            print("    %-10s %4d frames" % (name, n))

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
