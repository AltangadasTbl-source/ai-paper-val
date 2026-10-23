TRACE-Q — compact manuscript

Copy/paste file: trace_q_draft.tex
Rendered main paper: trace_q_draft.pdf (10 pages, including references)
Supplement: supplement.pdf

OVERLEAF
Copy the entire contents of trace_q_draft.tex into Overleaf main.tex.
Select XeLaTeX and Recompile. Overleaf runs the passes needed for references.
The main TeX file contains all sections, tables, the TikZ workflow diagram,
and the 12 bibliography entries. No other manuscript files, figure upload,
BibTeX run, or ZIP bundle is needed for the main paper.
The extended per-paper results, full comparison table, codebook, and count
plot are preserved in the separate supplement.pdf.

EDITING LOCALLY
trace_q_draft.tex is the generated standalone file.
manuscript_source.tex is the modular source wrapper.
sections/*.tex contains the editable section text.
references.bib contains the full bibliographic metadata.
bibliography.tex is generated from it, using compact author initials and
up to six names followed by et al.; DOIs/preprint versions are preserved.
project_origin_sources.txt maps the project-origin account to supplied notes.

From this directory, run:
  bash build.sh
This regenerates trace_q_draft.tex from the modular sources and analysis CSVs,
then compiles the main paper and supplement with XeLaTeX. It does not use BibTeX.
If editing the standalone file directly, compile it directly with XeLaTeX;
running build.sh will instead regenerate it from the modular source files.

STATISTICS
The final human-reviewed Excel decisions remain authoritative: 44 papers,
440 candidates, 413 retained, 27 excluded. The sample was selected by availability.
The comparison uses 19 papers from 2018–2019 and 25 from 2024–2025.
All hypothesis tests are exact, two-sided paper-level permutation tests.
Bootstrap confidence intervals are separately identified (20,000 resamples,
seed 20261022); they are not permutation intervals.
The R analysis and original data remain in ../analysis and
../review_results_2_4_1_Rbulun_copy. To rerun from the project root:
  Rscript analysis/analyze_results.R
Then run bash manuscript/build.sh to refresh the rendered paper.

The initial project motivation and the separation of descriptive protocol
findings from temporal endpoints were checked against the newly supplied
meeting notes and correspondence. Historical preliminary numbers are not
used as final results. Two GPT-6-Astra/high agents condensed and checked the
scientific content; a GPT-6.1-sol/high agent checked language against the
supplied template and reviewed citation handling.

Author names, affiliations, final funding/conflict statements, and the public
release location remain for the authors to finalize before submission.
The previous 16-page draft is preserved under ../archive.
