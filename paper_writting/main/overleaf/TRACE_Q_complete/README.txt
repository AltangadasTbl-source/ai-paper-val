TRACE-Q: source-only Overleaf project

Upload TRACE_Q_Overleaf_ready.zip as a new Overleaf project, then select XeLaTeX as the compiler. The project root contains all selectable main documents. No shell escape, network access, R, Python, or raw workbooks are needed to compile.

WORKFLOW MARKDOWN
workflow_1_6_2_EN.md and workflow_1_6_2_CN.md follow the original 13 steps.
Workflow slides 2–5 were removed; former page 6 is now page 2, unchanged.

MAIN DOCUMENTS
main.tex (default) or slides_main.tex: self-contained 17-slide Beamer presentation
in three sections. Either file can be copied alone and compiled with XeLaTeX.
All tables, TikZ chart coordinates and the hidden Chinese speaking script are
embedded. No project fonts, figures, tables, R or Python are needed for the deck.
speech_notes_cn_main.tex: Chinese speaking notes, with one section per slide (17 sections); thumbnails are optional.
task3_report_main.tex: concise Task 3 report (5 pages); full candidate records remain in data/review_notes/statistical_issue_recategorization.xlsx and companion CSV/JSON files.
supplemental_reference_main.tex: complete workflow explanation, role matrix, source locators and other-domain comparison reference. This is an archival reference, separate from the concise report and the presentation.

In Overleaf, change the project's Main document setting to the desired root .tex file. Keep XeLaTeX selected. Recompile twice if cross-references or the table of contents change. No local compilation was performed for the current revision.

EDITING AND FIGURES
Edit the standalone main.tex or slides_main.tex for slides. documents/slides.tex
is an identical compatibility copy. tables/ retains historical table sources
for reference; the deck embeds its charts and does not load external graphics. Other document bodies are
in documents/. The Task 3 report follows the final concise revision.

The Chinese speaking notes now explicitly use the four final completed
workbooks in review_results_2_4_1_Rbulun_copy. All 440 judgments and the
paper-level inputs were checked, including 32 exact permutation tests.
There are 413 retained and 27 excluded candidates; the statistical endpoints
remain 139 confirmed and 37 confirmed substantive. The retained Notes cells
are blank, so prior Notes-based mechanisms are labelled supplementary analysis.
supporting/review_results_verification.json records source hashes and checks.

OPTIONAL THUMBNAILS: notes compile without a PDF dependency. If thumbnails are
wanted, compile main.tex on Overleaf, download its PDF and upload it to the
project as trace_q_slides.pdf before compiling the notes. No rendered PDFs or
preview images are included in this source-only package.

FONTS
The deck uses standard TeX Live fonts. Other documents use fonts bundled in
fonts/, with licenses and attribution. The renamed Noto CJK subsets have been
refreshed to include the revised speaking notes and all existing document
glyphs, Latin and common punctuation. New characters outside that coverage
may require replacement with full Noto CJK fonts. Font subsetting changes
storage only; no Chinese text has been shortened or replaced.

For future Chinese edits that produce a "Missing character" log entry, obtain the full Simplified Chinese OTF faces from the Noto CJK project (https://github.com/notofonts/noto-cjk), including Regular and Bold for Serif and Sans, and keep the accompanying OFL license. Place them in fonts/ and change the CJK declarations in documents/speech_notes_cn.tex and documents/supplemental_reference.tex, for example:
  \setCJKmainfont{NotoSerifCJKsc}[Path=fonts/,Extension=.otf,UprightFont=*-Regular,BoldFont=*-Bold]
  \setCJKsansfont{NotoSansCJKsc}[Path=fonts/,Extension=.otf,UprightFont=*-Regular,BoldFont=*-Bold]
Only the Chinese notes use both families; the supplemental reference uses Serif. Alternatively, regenerate subsets containing all newly added characters. Recompile and check the log for missing characters. A full font bundle is larger, so keep Overleaf's upload limits in mind.

AUDIT MATERIALS
The data/ directory preserves CSV, XLSX, JSON, TSV and text analysis artifacts. data/review_notes/statistical_issue_recategorization.xlsx contains the full recategorization table. Supporting source references, validation records and source metadata are in supporting/. Archived planning and analysis text is retained for provenance; where a historical planning note differs from the final deliverable, the current deck and concise report are the presentation versions. No raw reviewer workbook is required for typesetting. supporting/reproduction_scripts.zip preserves the analysis and document-generation scripts at their original relative paths for audit. Those scripts are optional and are not called by XeLaTeX; rerunning the underlying analyses requires the original source-workbook paths and appropriate R/Python dependencies. The included precomputed data and TeX suffice for every document in this package.

SCOPE
Only 139 final confirmed statistical_results findings were recategorized, including the nested 37 substantive findings. The 440-row Notes extraction is a source index. Earlier publication cohorts are 2018–2019 (19 papers); later cohorts are 2024–2025 (25 papers). Copied workbook labels were subsequently human reviewed; raw Notes were AI-authored. The new mechanism coding is LLM-assisted and does not constitute a new human review or change final labels.

SOURCE VALIDATION
Local rendered PDFs, previews and build files have been removed. The current
revision was checked at the source level only; it has not been rendered locally.
supporting/overleaf_validation.json records those static checks, and
supporting/package_sha256.csv records packaged-file hashes.

The deck loads fix-cm before its class to support small math sizes, explicitly
declares every monospace face, and preserves the 17 remaining presentation frames.
After replacing an older file on Overleaf, select XeLaTeX and recompile from
scratch. main.tex, slides_main.tex and documents/slides.tex are synchronized.

The source data are not recomputed during compilation. Original analysis labels
and values are preserved.

UPLOAD COMPATIBILITY
The archive contains root main documents with no enclosing top-level folder. Explicit text fonts are bundled. Common editable LaTeX sources are well below the 7 MB project limit; CSV/JSON/XLSX files are supporting audit data rather than compilation inputs. The archive is checked against the 50 MB upload limit. Overleaf documentation consulted: https://docs.overleaf.com/managing-projects-and-files/uploading-a-project and https://docs.overleaf.com/managing-projects-and-files/adding-files-to-a-project/uploading-files-to-a-project .
