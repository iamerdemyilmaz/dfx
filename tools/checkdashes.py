"""Fail if any em dash or en dash appears in the given files. Usage: python tools/checkdashes.py file..."""
import sys
bad = 0
for f in sys.argv[1:]:
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        if "\u2014" in line or "\u2013" in line:
            bad += 1
            print(f"{f}:{i}: {line.strip()[:120]}")
print("dashes found:", bad)
sys.exit(1 if bad else 0)
