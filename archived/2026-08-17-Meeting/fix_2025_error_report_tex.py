#!/home/juliz/venvs/stt/bin/python
"""Mechanically constrain Pandoc longtables to the printable text width."""

from __future__ import annotations

import re
from pathlib import Path


PATH = Path(__file__).resolve().parent / "2025_paper_error_report.tex"
text = PATH.read_text(encoding="utf-8")


def replace_table(match: re.Match[str]) -> str:
    prefix, spec, suffix = match.groups()
    count = len(spec)
    width = 0.88 / count
    align = {
        "l": r">{\raggedright\arraybackslash}",
        "r": r">{\raggedleft\arraybackslash}",
        "c": r">{\centering\arraybackslash}",
    }
    columns = "".join(f"{align[kind]}p{{{width:.4f}\\linewidth}}" for kind in spec)
    return f"{prefix}{columns}{suffix}"


pattern = re.compile(r"(\\begin\{longtable\}\[\]\{@\{\})([lcr]+)(@\{\}\})")
text, count = pattern.subn(replace_table, text)
if count == 0:
    raise SystemExit("No simple Pandoc longtable specifications found")

PATH.write_text(text, encoding="utf-8")
print(f"Reformatted {count} longtable column specifications in {PATH}")
