## Downstream Evidence-Chain Considerations

If a human confirms any candidate, a data extractor could copy the affected number, denominator,
unit, interval type, outcome definition, or summary label into a systematic review, meta-analysis,
guideline evidence table, or later publication. This is a bounded possibility, not evidence that
propagation occurred. Small preventable reporting defects can matter in aggregation even when they do
not change the source paper's conclusion. This review makes no claim of conclusion change or harm.

## Limitations and Missing Definitions

The package does not supply raw participant data, table/figure production files, analysis code,
trial-level person-time mapping, unrounded Cox/mixed-model outputs, Holm inputs, unrounded I2, MCMC
diagnostics, unrounded ARDs, an explicit ARD scale, an NNT/NNH integer convention, or Egger model
output. Those missing inputs bound the mechanical checks and are named in the relevant cards.

DOC-001 page 8 required direct rendering because native text reading order is unusable. DOC-003
eFigure 2 has no numeric segment labels, so C018's graphical comparison is approximate. DOC-003
forest text required targeted CPU OCR as a locator, followed by direct visual checking. C014 is
explicitly conditional on ordinary nearest rounding and a common unrounded estimand.

Most importantly, the package contains two article identities and no matched main/supplement pair:
DOC-001 is DOI `10.1001/jama.2019.10517`; DOC-002/DOC-003 are DOI `10.1001/jama.2018.20578`.
Therefore, package-level main-to-supplement matching is incomplete by source availability.

## Human Adjudication Checklist

- Confirm each cited page and transcription in the direct supplied PDF.
- Retrieve the named unrounded output, source dataset, coding dictionary, table input, or analysis code.
- Confirm that comparator records use the same population, time, contrast, outcome, model, measure,
  scale, and analysis version.
- Reproduce the stated arithmetic or inferential relationship with the source's actual precision and
  rounding convention.
- Decide whether a source-grounded alternative fully explains the observation.
- Record validity, importance, action, initials, and notes only in the blank fields on each card.
- If a change is warranted, determine the final correction from authoritative source materials; this
  report does not prescribe one.

## Reproducibility and Source-Integrity Metadata

- Profile: `1.3.1`; CPU-only; reusable evidence first; targeted Tesseract only where graphic text could
  not otherwise be transcribed.
- Direct sources inventoried before review: 3 PDFs, 46 pages, 3 SHA-256 records.
- Reused assets inventoried before review: 47 files, 47 SHA-256 records; no reused artifact was
  modified.
- Direct inspection tools: `sha256sum` (uutils coreutils 0.8.0), `file` 5.46, Poppler 26.01.0
  (`pdfinfo`, `pdftotext`, `pdftoppm`), Tesseract 5.5.0 with Leptonica 1.86.0, and Ghostscript 10.06.0
  for readable orientation of temporary DOC-001 page 8 confirmation.
- [Source inventory](<review_1_3_1/source_inventory.md>),
  [reused-evidence inventory](<review_1_3_1/evidence_asset_inventory.md>),
  [coverage manifest](<review_1_3_1/coverage_manifest.md>), and
  [limitations record](<review_1_3_1/limitations.md>) are package-local review artifacts.
- Candidate ID conservation target: ledger = recheck = quality audit = report = `C001`-`C024`.
- Statistical completion target: `S001`-`S053` each have both pass records.
- Final source and reused-artifact hash comparison and workflow validation are recorded in
  `review_1_3_1/review_validation.json` after report generation.

All candidates remain **Pending Human Adjudication**.
