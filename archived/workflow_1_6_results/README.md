# Workflow 1.6 results archive

Created 2026-10-10. Workflow 1.6 was run on 15 packages (all ten in `2019/` and five in `2018/`) and
committed in `0a806358` and `a9940323`. Those runs registered far more candidates than the v2_3_1
human-review set, mostly through rounding-level percentage checks, model-based estimates compared
with crude ratios, conditional questions, and one candidate per row for a repeated pattern. Workflow
1.6.1 (`multi_agent_template/workflow1.6.1/`) replaces it with an inclusion screen, and the 15
packages were reset for 1.6.1.

## What was done

`archive_1_6_results.py --execute` processed each of the 15 packages:

- 2,011 result files (`.ai_paper_validation/review_1_6/` and `final_report_1_6.md`/`.html`) moved
  here under `<year>/<paper>/` with their package-relative paths. Each file's SHA-256 was checked
  after the move and matches the committed version at `a9940323`.
- 405 workflow 1.6 control files (27 per package) removed. Each was byte-identical to
  `multi_agent_template/workflow1.6/`, which remains the reference copy.
- 435 workflow 1.6.1 control files (29 per package) installed from
  `multi_agent_template/workflow1.6.1/`.

`archive_manifest.csv` records every action with year, paper, package-relative path, archive or
template path, size, and SHA-256. The script refuses to run again while the manifest exists. Source
files and reusable extraction assets were not touched.

## Run status at archiving

Candidate counts are the number of `## Cnnn` cards in `final_report_1_6.md`. v2_3_1 counts are the
rows in each paper's `C_` sheet. jama.2019.0556 is not in v2_3_1.

| Package | 1.6 validator | 1.6 candidates | v2_3_1 rows |
|---|---|---:|---:|
| 2019/jama.2019.0556 | PASS | 22 | — |
| 2019/jama.2019.10517 | PASS | 15 | 3 |
| 2019/jama.2019.12618 | FAIL (report not generated; ledger had 57) | — | 8 |
| 2019/jama.2019.14231 | PASS | 18 | 11 |
| 2019/jama.2019.14630 | not run to completion | — | 9 |
| 2019/jama.2019.14901 | not run to completion | — | 6 |
| 2019/jama.2019.17380 | not run to completion (89 registered) | — | 7 |
| 2019/jama.2019.2210 | PASS | 15 | 9 |
| 2019/jama.2019.4755 | PASS | 16 | 5 |
| 2019/jama.2019.7505 | PASS | 106 | 4 |
| 2018/jama.2017.21906 | PASS | 28 | 6 |
| 2018/jama.2018.0156 | PASS | 31 | 8 |
| 2018/jama.2018.0948 | PASS | 30 | 7 |
| 2018/jama.2018.6496 | FAIL (routing preflight provider field) | 10 | 4 |
| 2018/jama.2018.8802 | FAIL (routing preflight provider field) | 19 | 8 |

Two runs failed only because the 1.6 validator required a specific provider name. Workflow 1.6.1
uses the provider of the current Codex session and records it as `CURRENT_SESSION`.

## All packages moved to workflow 1.6.1

`sync_1_6_1_controls.py --execute` then brought all 45 packages to the current 1.6.1 template:

- the 30 packages that had not run 1.6 had their 27 workflow 1.6 control files removed (each
  byte-identical to the 1.6 template; no 1.6 results existed there) and the 29 1.6.1 controls installed;
- the 15 packages reset above had their 1.6.1 controls refreshed: `OPENROUTER_SETUP.md` removed,
  `CODEX_SETUP.md` added, and changed files updated. Each file was first checked against the hash
  recorded at installation.

`sync_manifest.csv` records every removal, installation, and update with SHA-256. A git-ignored `__pycache__` file left in the
template by a validator test was copied into the packages by the first steps and then removed from
the template and every package; its `sync_manifest.csv` rows were dropped, and its 15 install rows
remain in `archive_manifest.csv`.

## Restoring

To restore a package's 1.6 results, move `<year>/<paper>/<path>` from here back to
`<year>/<paper>/<path>` in the repository. The 1.6.1 outputs use `review_1_6_1/` and
`final_report_1_6_1.*`, so they do not collide with restored 1.6 files.
