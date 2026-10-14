"""Rewrite pipe-table separator rows so dash counts are proportional to column content width
(CJK = 2 units, capped), letting pandoc's markdown reader assign relative p{} widths."""
import sys, re, unicodedata
src, dst = sys.argv[1], sys.argv[2]
def w(s):
    return sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in s)
lines = open(src, encoding="utf-8").read().split("\n")
out, i = [], 0
while i < len(lines):
    if lines[i].startswith("|") and i + 1 < len(lines) and re.fullmatch(r"\|(\s*:?-+:?\s*\|)+", lines[i + 1].strip()):
        j = i + 2
        while j < len(lines) and lines[j].startswith("|"):
            j += 1
        rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines[i:j] if l is not lines[i + 1]]
        rows = [r for k, r in enumerate([[c.strip() for c in l.strip().strip("|").split("|")] for l in lines[i:j]]) if k != 1]
        n = len(rows[0])
        widths = [max(9, min(60, max(w(r[c]) for r in rows if c < len(r)))) for c in range(n)]
        seps = [c.strip() for c in lines[i + 1].strip().strip("|").split("|")]
        new = []
        for c in range(n):
            right = seps[c].endswith(":"); left = seps[c].startswith(":")
            d = "-" * widths[c]
            new.append((":" if left else "") + d + (":" if right else ""))
        out += [lines[i], "|" + "|".join(new) + "|"] + lines[i + 2:j]
        i = j
    else:
        out.append(lines[i]); i += 1
open(dst, "w", encoding="utf-8").write("\n".join(out))
