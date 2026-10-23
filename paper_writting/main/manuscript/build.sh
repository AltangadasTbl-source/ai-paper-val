#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
python3 prepare_manuscript.py
xelatex -interaction=nonstopmode -halt-on-error trace_q_draft.tex > xelatex_pass1.log
xelatex -interaction=nonstopmode -halt-on-error trace_q_draft.tex > xelatex_pass2.log
xelatex -interaction=nonstopmode -halt-on-error trace_q_draft.tex > xelatex_pass3.log
if rg -n 'Undefined control sequence|undefined citations|undefined references|Overfull \\hbox|Overfull \\vbox|Missing character' trace_q_draft.log; then
  printf '%s\n' 'Build completed with a layout or reference issue; inspect trace_q_draft.log.' >&2
  exit 1
fi
xelatex -interaction=nonstopmode -halt-on-error supplement.tex > supplement_pass1.log
xelatex -interaction=nonstopmode -halt-on-error supplement.tex > supplement_pass2.log
xelatex -interaction=nonstopmode -halt-on-error supplement.tex > supplement_pass3.log
if rg -n 'Undefined control sequence|undefined citations|undefined references|Overfull \\hbox|Overfull \\vbox|Missing character' supplement.log; then
  printf '%s\n' 'Supplement has a layout or reference issue; inspect supplement.log.' >&2
  exit 1
fi
printf '%s\n' 'XeLaTeX build complete: manuscript/trace_q_draft.pdf (embedded bibliography; no BibTeX required)'
