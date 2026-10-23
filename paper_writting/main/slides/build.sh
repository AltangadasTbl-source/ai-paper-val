#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
# The delivered TeX contains all tables and plots; analysis is a separate step.
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error trace_q_slides.tex > xelatex_pass1.log
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error trace_q_slides.tex > xelatex_pass2.log
if rg -n 'Undefined control sequence|undefined references|Overfull \\hbox|Overfull \\vbox|Missing character' trace_q_slides.log; then
  printf '%s\n' 'Inspect the XeLaTeX log for a layout or reference issue.' >&2
  exit 1
fi
printf '%s\n' 'Built slides/trace_q_slides.pdf using XeLaTeX.'
