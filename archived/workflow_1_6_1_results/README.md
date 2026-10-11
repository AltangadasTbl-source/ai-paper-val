# Workflow 1.6.1 results archive

Created 2026-10-11. Workflow 1.6.1 was run on the ten packages in `2019/` and the ten in `2018/` and
committed in `8dd964a5` and `63465221`. A comparison with the substantive rows of the v2_3_1 human
review showed that the 1.6.1 checkers excluded reproduced issues under judgment codes (sign and digit
slips in result values, interval-versus-P conflicts, counts that do not reconcile within one table,
planned-versus-reported outcome changes). Workflow 1.6.2 (`multi_agent_template/workflow1.6.2/`)
relaxes those screening rules, and all 45 packages were reset for it.

## What was done

`archive_1_6_1_results.py --execute` processed all 45 packages in `2018/`, `2019/`, `2024/` and
`2025/`:

- 964 result files moved here under `<year>/<paper>/` with their package-relative paths, each
  SHA-256-checked after the move:
  - 718 workflow 1.6.1 results from the 20 packages that ran it (`review_1_6_1/` except its
    `preprocessing/` folder, and `final_report_1_6_1.md`/`.html`);
  - 246 workflow 1.6 files that the server runs re-created and committed with the 1.6.1 results:
    243 in `2019/jama.2019.0556/.ai_paper_validation/review_1_6/preserved/` (a snapshot of an
    earlier 1.6 run, including its page renders) and 3 preflight files in
    `2019/jama.2019.2210/.ai_paper_validation/review_1_6/run_20261011T024101Z/`.
- 467 files in `review_1_6_1/preprocessing/` (text extraction and page renders from 18 packages) were
  left in place as reusable extraction assets. One page render that a screener had written under
  `review_1_6_1/screening/preprocessing/` (jama.2019.12618) was archived with the results.
- 1,260 workflow 1.6.1 control files removed (28 per package), each byte-identical to
  `multi_agent_template/workflow1.6.1/`, which remains the reference copy.
- 1,260 workflow 1.6.2 control files installed (28 per package) from
  `multi_agent_template/workflow1.6.2/`.

The `review_1_5_*/preprocessing/` folders and other reusable extraction assets were not touched.
`archive_manifest.csv` records every action with year, paper, package-relative path, archive or
template path, size, and SHA-256. The script refuses to run again while the manifest exists.

## Run status at archiving

Candidate counts are the number of `## Cnnn` cards in `final_report_1_6_1.md`.

| Package | 1.6.1 validator | 1.6.1 candidates |
|---|---|---:|
| 2018/jama.2017.21906 | PASS | 2 |
| 2018/jama.2018.0156 | PASS | 4 |
| 2018/jama.2018.0948 | PASS | 1 |
| 2018/jama.2018.14280 | PASS | 1 |
| 2018/jama.2018.14282 | PASS | 10 |
| 2018/jama.2018.17075 | not run (no `review_validation.json`) | 4 |
| 2018/jama.2018.18020 | PASS | 4 |
| 2018/jama.2018.6496 | PASS | 1 |
| 2018/jama.2018.8802 | PASS | 1 |
| 2018/jama.2018.9128 | PASS | 2 |
| 2019/jama.2019.0556 | PASS | 5 |
| 2019/jama.2019.10517 | PASS | 2 |
| 2019/jama.2019.12618 | PASS | 2 |
| 2019/jama.2019.14231 | PASS | 1 |
| 2019/jama.2019.14630 | PASS | 0 |
| 2019/jama.2019.14901 | PASS | 5 |
| 2019/jama.2019.17380 | PASS | 5 |
| 2019/jama.2019.2210 | PASS | 1 |
| 2019/jama.2019.4755 | PASS | 0 |
| 2019/jama.2019.7505 | PASS | 2 |

Of the 45 v2_3_1 rows that the BulunTe review graded substantive in these papers, 28 became 1.6.1
cards (5 only partly), 15 were seen by a checker and excluded, 1 was screened out by the inclusion
screener, and 1 was not detected. Across all 20 runs the checkers listed about 2,500 excluded
observations, statistical pass 2 emitted no findings, and the auditor reversed no exclusion.

## Restoring

To restore a package's 1.6.1 results, move `<year>/<paper>/<path>` from here back to
`<year>/<paper>/<path>` in the repository. Workflow 1.6.2 writes to `review_1_6_2/` and
`final_report_1_6_2.*`, so restored 1.6.1 files do not collide with its outputs.
