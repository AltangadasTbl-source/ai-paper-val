# Limitations and Missing Definitions

## Package identity and cross-document scope

The supplied package joins sources from two article identities. DOC-001,
`jama_flint_2019_oi_190079.pdf`, identifies DOI `10.1001/jama.2019.10517`. DOC-002 and DOC-003,
`joi180151supp1_prod.pdf` and `joi180151supp2_prod.pdf`, identify DOI
`10.1001/jama.2018.20578`. The package does not contain the matching main article for DOC-002/DOC-003
and does not contain the matching supplement for DOC-001. Consequently, internal matching within
DOC-001 and between DOC-002 and DOC-003 was completed, but a main-article-to-supplement quantitative
comparison could not be performed for either article identity. No cross-identity clinical-result match
was manufactured.

## Evidence and reproducibility limits

- No raw participant data, table-production files, analysis code, or trial-level person-time mapping
  was supplied.
- Unrounded Cox and mixed-model outputs, raw P values and Holm-adjustment inputs, unrounded fixed-effect
  I2, MCMC diagnostics, unrounded ARDs, the ARD display scale, the NNT/NNH integer convention, and the
  Egger model output were not supplied.
- DOC-001 PDF page 8 has unusable native-text reading order. Its rotated Table 4 was confirmed visually
  against a direct-source render; no value was accepted from the broken reading order alone.
- DOC-003 eFigure 2 has no numeric segment labels. Candidate C018 therefore combines exact eTable 2
  category counts with a reproducible but approximate visual-axis comparison.
- DOC-003 forest-plot values on PDF pages 22-26 are embedded as graphic text. Targeted CPU OCR was used
  only as a transcription aid, followed by direct visual confirmation of every recorded value.
- C014 is conditional on an ordinary nearest-rounding, same-estimand reciprocal interpretation. The
  source does not state the NNH integer-display convention or prove that ARD and NNH use the identical
  unrounded estimand.
- Several source cells explicitly state that a definition is not specified, not defined, not reported,
  or blank. Those absences were retained and were not filled by inference.

## Review boundary

This review checks supplied-source numeric, denominator, inferential-statistical, label/scale,
rate/count, and cross-location consistency. It does not fit replacement statistical models, audit raw
data, or evaluate broad study design, clinical importance, novelty, misconduct, or paper-level
validity. Diagnostic calculations are checks of printed relationships, not substitutes for the
reported analyses. Every candidate remains **Pending Human Adjudication**.
