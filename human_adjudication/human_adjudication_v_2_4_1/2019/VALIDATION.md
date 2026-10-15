# v.2.4.1 validation: 2019

Scope: 9 papers, 79 candidates, taken from `2019/<paper>/.ai_paper_validation/final_report_1_6_2.md` (workflow 1.6.2). jama.2019.0556 is included; it was not part of v.2.3.1. The structural template is `human_adjudication_v_2_3_1/2018/release/human_adjudication_v_2_3_1_2018_R_A.xlsx`.

Revision (2026-10-14): jama.2019.14231 (8 candidates) is an observational study. Its paper package was moved to `archived/jama.2019.14231/`, and the workbooks were rebuilt from the remaining 9 papers. A cell-by-cell comparison with the previous build showed only three differences: the `C_jama.2019.14231` sheet is gone, Checks B3/B4/B5 drop that sheet, and the Papers rows shift up by one. The other 79 candidates in `candidates_2019.json` are unchanged. The validator was rerun, and every figure below refers to the 79-candidate build.

| Paper | Candidates | statistical_results | report_internal_inconsistency | plan_material | protocol_report |
|---|---:|---:|---:|---:|---:|
| jama.2019.0556 | 11 | 4 | 0 | 0 | 7 |
| jama.2019.10517 | 5 | 0 | 0 | 0 | 5 |
| jama.2019.12618 | 10 | 2 | 0 | 2 | 6 |
| jama.2019.14630 | 9 | 3 | 0 | 0 | 6 |
| jama.2019.14901 | 5 | 1 | 0 | 0 | 4 |
| jama.2019.17380 | 18 | 5 | 0 | 2 | 11 |
| jama.2019.2210 | 7 | 3 | 0 | 0 | 4 |
| jama.2019.4755 | 1 | 0 | 0 | 0 | 1 |
| jama.2019.7505 | 13 | 8 | 0 | 0 | 5 |
| Total | 79 | 26 | 0 | 4 | 49 |

## How to reproduce

```
PY="env PYTHONDONTWRITEBYTECODE=1 human_adjudication/human_adjudication_v_2_3_1/2019/.venv/bin/python"
$PY human_adjudication/human_adjudication_v_2_4_1/2019/build_v_2_4_1.py
$PY human_adjudication/human_adjudication_v_2_4_1/2019/validate_v_2_4_1.py --scratch-dir <scratch folder outside this directory>
```

The build is deterministic. The core-properties `modified` stamp and the zip entry times are fixed, so a rebuild gives byte-identical workbooks; this was confirmed by rebuilding into a scratch folder and comparing sha256 values. The validator writes its recalculation test copies only to `--scratch-dir`. Results are in `validation_report.json`.

## Checks performed (all PASS, 41 of 41)

1. **Counts.** For each paper, the C_ sheet row count, the Candidate Index row count, the number of `## Cnnn` cards, the Review-Domain Summary total, `candidates_2019.json` and Papers column C all agree. While building, the builder also requires each card's domain and relationship type to match its Candidate Index row, and the per-domain card counts to match the Review-Domain Summary rows.
2. **Content.** Keys are `2019::<paper>::Cnnn`, unique and sequential in report order. Every E value is one of the four domains and matches the card. D and M–R are blank and F is `no`. B and C are non-empty, equal the catalog, contain no `](`, `**`, `<a id` or backticks, and contain no "Pending Human Adjudication" text.
3. **Formulas and layout.** Every G–L formula equals the template pattern with the row, the `$A$2:$A$<last>` range and the `2019::<paper>::` prefix substituted. The pattern is first confirmed to regenerate every formula in all ten template sheets. DV and CF attributes, formulas, priorities and differential styles match the template, and their sqrefs cover exactly rows 2..last. M–Q are hidden at width 3, freeze panes are at B2, the autofilter is A1:R<last>, and column widths, row heights, cell styles (including banding) and wrap text match the template. H1 reads `Statistical_or_numerical issue`. A fidelity check is also run: fed the template's own 2018 content, the C-sheet builder reproduces every part of the template workbook byte for byte (all except `docProps/core.xml`).
4. **Sheets and Codebook.** The sheet order is Setup, Checks, Papers, the 9 C_ sheets sorted as plain strings, then Codebook. Setup B2/B3 are blank, B4 holds the role and B5 = 2019 (integer). Checks B3 = 79 (integer), and B4/B5 are COUNTIF sums over each sheet's exact row range. Codebook cell values differ from the template only in the two fixes, and the Codebook sheet XML is byte-identical to the template once those two strings are substituted. styles.xml and the theme are identical to the template. Across every cell value, R_A and R_B differ only in Setup!B4, and their zip parts differ only in the Setup sheet part.
5. **Recalculation** (Python `formulas` 1.3.4, on copies in scratch):
   - (a) In the blank file, all 79 G cells read `CHECK REVIEWER ID` and B7 reads `ACTION NEEDED`. The H–L defaults are blank in the active branch and `not_applicable` elsewhere.
   - (b) With a reviewer ID set and every row filled (D `retain` plus a valid answer for its domain: H/I for statistical_results, K for report_internal_inconsistency or plan_material, L for protocol_report), with F `primary_done`, all G read `PRIMARY READY`, B4 = B3 = 79 and B7 reads `PRIMARY READY`.
   - (c) Setting H2 = `confirmed_issue` on a protocol_report row gives `CLEAR INACTIVE VALUES` on that row, B4 = 78 and B7 `ACTION NEEDED`.
   - (d) A `discuss` row (H–L formulas restored, F `primary_done`) stays `PRIMARY READY`; B5 = 1, B4 = 79 and B7 reads `PRIMARY READY`.
6. **Source integrity.** The sha256 of every source report is identical before the build, after the build, in `candidates_2019.json`, in `output_hashes.json` and after validation. The template's hash is also unchanged.

## Pending

- Desktop Excel smoke test: **PENDING**. It covers opening in Microsoft Excel, recalculating, checking rendering and dropdowns, and saving and reopening. The `formulas` package is not Excel, so none of these steps has been carried out in Excel.

## Extraction notes

- Column C is built from the card's `**Exact source locations:**` block. The block runs up to the next bold label, so continuation bullet lists (jama.2019.12618, all cards; jama.2019.4755) and two tables (jama.2019.10517 C002 and C004) are included. Each table data row is rendered as `cell: cell` and rows are joined with `; `.
- When a link's text does not contain the target's file name, the file name is prefixed as `<file> — <link text>`. This affects most links in these reports. Two links point to review records rather than source PDFs, and they are prefixed the same way: jama.2019.14901 C004 (`evidence_recheck.md — mechanical recheck`) and jama.2019.7505 C012 (`protocol-p32-coma-detail.png — protocol glyph detail`).
- Two source-location texts refer to content that is not part of the field: "listed page by page below" (jama.2019.10517 C002; the table is included) and "Every affected cell is enumerated below" (jama.2019.2210 C005; that enumeration sits under Calculation and is not included).
- jama.2019.4755 uses a `{#C001}` heading suffix; jama.2019.12618 uses `<a id>` anchor lines. Both are removed.
- On the one-candidate sheet (jama.2019.4755), openpyxl writes the DV/CF sqref `D2:D2` as `D2`. The coverage is the same.
