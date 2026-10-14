#!/usr/bin/env bash
# Render ../REVIEWER_GUIDE_CN.md to ../REVIEWER_GUIDE_CN.pdf with pandoc + XeLaTeX (ctexart, Noto CJK fonts).
# Usage: bash render.sh   (run from any directory; builds in a temporary folder)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../REVIEWER_GUIDE_CN.md"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
python3 -I "$HERE/widths.py" "$SRC" "$TMP/guide_pre.md"
sed -i '1s/.*/# v.2.4.1 人工复核工作指南/' "$TMP/guide_pre.md"
pandoc "$TMP/guide_pre.md" -f markdown-auto_identifiers -t latex -s --columns=20 --shift-heading-level-by=-1 \
  -V documentclass=ctexart -V classoption=fontset=none -V classoption=a4paper -V fontsize=10.5pt \
  -V geometry:margin=2.2cm -V colorlinks=true -V linkcolor=blue -V urlcolor=blue \
  -V subtitle="Excel independent primary review" -V date="$(date +%F)" \
  --highlight-style=tango -H "$HERE/header.tex" -o "$TMP/REVIEWER_GUIDE_CN.tex"
(cd "$TMP" && for i in 1 2; do xelatex -interaction=nonstopmode -halt-on-error REVIEWER_GUIDE_CN.tex >/dev/null; done)
cp "$TMP/REVIEWER_GUIDE_CN.pdf" "$HERE/../REVIEWER_GUIDE_CN.pdf"
echo "wrote $HERE/../REVIEWER_GUIDE_CN.pdf"
