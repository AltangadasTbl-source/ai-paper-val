# Tooling record

- **Probe UTC:** 2026-10-11T18:28:39Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Linux direct PDF and OCR executables absent; pinned PDF fallback and reusable extraction/page images cover all units. Glyph-corrupted PLAN text was mapped visually from readable source-page images. Windows GPU was confirmed through PowerShell; no new OCR was necessary.

The user requested RTX 5070 Laptop through PowerShell 5.1/7 and /home/juliz/venvs/stt/bin/python. Bootstrap was invoked through that interpreter. The initial sandboxed installation could not access the package index (INSTALL_FAILED); the authorized network retry installed the pinned packages into the temporary package-local environment. No global installation was performed. Final successful bootstrap is logged in tooling/bootstrap_log.json.

PowerShell 5.1 read-only nvidia-smi query confirmed NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56, total memory 8151 MiB. Sandbox WSL interop and NVML access are blocked; authorized read-only PowerShell calls work outside that sandbox. Windows tesseract.exe exists at C:\msys64\ucrt64\bin\tesseract.exe; it is a CPU engine and has not been used.

Use .ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py for missing PDF info/text/layout/render capabilities. Engine: PyMuPDF 1.26.4; rendering device: CPU. Reuse source-matched OCR first. Inspect rendered pages visually when quantitative text is unreliable; request coordinator help for an actual OCR gap. No new OCR derivative has yet been produced. The user explicitly authorized GPU use; a GPU OCR engine has not yet been selected or used.

Fresh direct-source derivative coverage: DOC-002 pp.55-64 were rendered at 200 dpi to preprocessing/plan2/page-55.png through page-64.png by the supplied helper (PyMuPDF 1.26.4, CPU). Native and sorted reading-order text for these ten pages were also extracted to preprocessing/plan2/native-55-64.txt and layout-55-64.txt; glyph corruption persists, so readable direct-source images supply the scientific mapping. No new OCR was required for these units. The plan2 mapper records exact derivative provenance in its artifact.

Additional fresh derivative: DOC-002 p18 was freshly rendered at200dpi by PyMuPDF1.26.4 CPU to preprocessing/plan1/page-18.png because the retained image could not be decoded. The fresh render was fully mapped; p18 is counted fresh-required. Eleven units now require fresh direct-source mapping, all completed. Retained p71 has a readable alternative page image, so no fresh derivative is required there.

Numeric source confirmation: DOC-003 p22 rendered to preprocessing/numeric-page-22.png by supplied pdf_tools.py, PyMuPDF1.26.4,200dpi,CPU; original table numerals and column alignment visually confirmed. No new OCR. Exact command is recorded in relationships/numeric_relationship_inventory.md.

Mechanical recheck provenance: verification/evidence_recheck.md records 31 fresh source-page renders in preprocessing/recheck-wave1/ and preprocessing/recheck-wave2/, with each command and source page in their provenance.md files. Full DOC-001 and DOC-003 native text was extracted to preprocessing/recheck-wave1/main-full-native.txt and preprocessing/recheck-wave2/report-full-native.txt. All derivatives use the bundled helper with PyMuPDF 1.26.4; page rendering is CPU at 200 dpi.

The results-candidate recheck records eleven fresh source-page renders in preprocessing/recheck_results/: DOC-003 pages 22, 27, 29, 44, 51, 52, 53; DOC-001 pages 6, 7, 8; DOC-002 page 70. Each derivative and command template is recorded in verification/results_candidates_recheck.md. Engine: PyMuPDF 1.26.4; CPU; 200 dpi. No new OCR or GPU computation was needed. GPU_USER_REQUESTED records the user's authorized preference, not a claim that these CPU PDF derivatives used the GPU.

After standalone HTML rendering, the supplied bootstrap_tooling.py remove command was run through /home/juliz/venvs/stt/bin/python. It removed the temporary tooling/venv and tooling/pip-cache; the bootstrap log retains pinned-version and removal metadata. Every source and reusable derivative remains unchanged. No new OCR derivative was produced anywhere in this run.
