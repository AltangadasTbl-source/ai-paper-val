# Workflow 1.6 Limitations

- Only the three supplied PDFs are scientific evidence; raw data and external publications are outside scope.
- Historical extraction/render engine metadata is unavailable. Curator comparisons establish current-source text agreement; legacy engines are recorded as UNKNOWN rather than inferred.
- Eight pages lack legacy rendered PNGs (DOC-001 p.11; DOC-002 pp.1-4,23-25), but all have usable source-matched native/layout text and direct rendering is available. This is a derivative gap, not a scientific coverage gap.
- Direct OCR and Office conversion are unavailable. All supplied sources are readable PDFs and usable text covers all 49 pages; no fallback environment or installation was needed.
- DOC-003 combines REPORT results and a PLAN operational form; document roles must follow compared content, including prospective-rule quotations.
- The user explicitly overrides the workflow's OpenRouter requirement in favor of the current provider. The current interactive session's launch command and coordinator runtime model are not independently exposed. Named role model/effort settings are exposed and match the fixed matrix. The original validator hard-codes provider and launch-context values; any remaining failure is reported without fabricating those values or changing workflow controls.

Source-specific missing statistical definitions and candidate-specific human questions are recorded below and in the completed review artifacts. All candidates remain Pending Human Adjudication.

Statistical reconstruction limits: exact chi-square implementation/continuity correction and analytic count-table definitions, binary interval formulas, interaction link/variance, rank/tie corrections, cluster sizes/covariance/algorithm, and Cox event times/test output are unavailable. Six printed-P diagnostic differences (etomidate, grade 2 view, pneumothorax, faculty operator, no device, any complication) remain named comparison limits after both statistical passes because exact test alignment is not established. Printed grade-4 CI and P come from unspecified distinct inferential constructions, so test/interval duality cannot be imposed.

Candidate-specific limits: no paired cuff/blade timestamps, no primary missing-data implementation log, no arm-specific resistance numerator, no extra initial-saturation exclusion definition, no final-operator episode data, and no actual difficult-subgroup interim calculation. C008 retains its stable ID with record_input_error because its conditional numerator/population match is unsupported.

## Six diagnostic P-value comparison limits and human questions

The six differences below were explicitly retained after both statistical passes. Selected Pearson and Yates reconstructions are DIAGNOSTIC_APPROXIMATION calculations, not identified author analyses. All are compared with the REPORT methods on [jama_driver_2018_oi_180054.pdf — PDF p. 4](<../../jama_driver_2018_oi_180054.pdf#page=4>). Exact implementation, test statistic and analytic count table are missing. These differences neither establish a printed P value as correct nor establish a source-compatible contradiction; they are not stable candidates. They are not attributed to rounding by assumption.

| S ID / result | Source location (REPORT) | Printed inputs; P | Pearson diagnostic | Yates diagnostic | Exact human question |
|---|---|---|---|---|---|
| S007 etomidate | [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 | 332/381 vs 333/376; .54 | .548618 → .55 | .625129 → .63 | Which precise chi-square implementation, statistic and analytic count table generated .54? |
| S029 grade 2 view | [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 | 74/373 vs 62/359; .39 | .371672 → .37 | .424697 → .42 | Which exact implementation, statistic and analytic count table generated grade-2 .39? |
| S054 pneumothorax | [jama_driver_2018_oi_180054.pdf — PDF p. 9](<../../jama_driver_2018_oi_180054.pdf#page=9>), Table 5 | 9/381 vs 9/376; .99 | .977373 → .98 | 1.000000 → 1.00 | Which exact implementation, statistic and analytic count table generated .99? |
| S021 faculty operator | [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 | 8/381 vs 5/376; .42 | .414910 → .41 | .592294 → .59 | Which analytic row inputs and exact test generated .42, given unresolved final-operator counts in C003? Do not change a count to force agreement. |
| S034 no device | [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 | 5/381 vs 6/376; .75 | .744575 → .74 | .982394 → .98 | Which implementation, statistic and analytic count table generated .75? |
| S052 any complication | [jama_driver_2018_oi_180054.pdf — PDF p. 9](<../../jama_driver_2018_oi_180054.pdf#page=9>), Table 5 | 66/381 vs 63/376; .83 | .835511 → .84 | .911640 → .91 | Which implementation, statistic and analytic count table generated .83? |

Both passes retain S025 as an implementation example: printed .02 is reproduced by Yates .017877 rather than Pearson .014630. S049 grade-4 success difference 60 (17–100), P=.09 has Pearson diagnostic .089686; the supplied source does not establish that its difference interval and chi-square P are inferential inversions. Neither observation yields a separate candidate. Clustered/unclustered duration algorithms, rank/tie information and time-to-event output remain unavailable.

## Execution-context validation boundary

Scientific source and relationship coverage is complete. The unchanged workflow validator requires four strict routing literals (Status PASS, Provider openrouter, Execution mode INTERACTIVE_CLI, Launch command codex --approve-for-me). Current-provider authorization and unavailable original-launch attestation are recorded truthfully rather than replaced with those literals. Strict execution-context validation cannot pass those requirements under the current record. Final rendering, source/reuse hash recomputation and actual validation JSON are coordinator completion steps; no unconditional validator PASS is claimed.

