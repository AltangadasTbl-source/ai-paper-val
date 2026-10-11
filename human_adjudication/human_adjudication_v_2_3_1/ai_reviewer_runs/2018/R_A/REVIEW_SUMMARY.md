# v.2.3.1 primary review: 2018, role R_A (AI-simulated reviewer)

Reviewer ID: `AI-sim-ClaudeOpus5.5-2018-R_A`. This is an AI-simulated second-stage review, not a human adjudication. It was done independently of R_B: no R_B, other-year, pipeline (`.ai_paper_validation/`, `workflow_*`, `meta_report/`, `archived/`) or earlier-version material was read.

## Outputs

- `judgments.json`: 119 rows, each with D/E/H–L, a workbook note (R, 400 characters or fewer), the evidence pages inspected and a full rationale with the recomputations.
- `human_adjudication_v_2_3_1_2018_R_A_completed.xlsx`: built with `fill_review.py` from the unmodified release template. The template's SHA-256 still matches `release/output_hashes.json`.

## Counts

| Field | Counts |
|---|---|
| D (disposition) | retain 118, exclude 1, discuss 0 |
| E (domain) | statistical_results 75, report_internal_inconsistency 22, protocol_report 11, plan_material 11 |
| E changed from AI suggestion | 7 (all report_internal_inconsistency → statistical_results) |
| D differing from AI disposition | 2 (0156::C008 discuss → retain; 6496::C002 retain → exclude) |
| H (retained statistical_results, n=74) | confirmed_issue 74 |
| I | substantive 23, minor_presentation 49, indeterminate 2 |
| J (optional) | direct 28, possible 4, unlikely 42 |
| K (retained internal / plan, n=33) | substantive_inconsistency 2, minor_presentation 31 |
| L (retained protocol_report, n=11) | substantive_difference 8, minor_presentation 3 |

### E changes

I moved these to `statistical_results` because the Codebook directs specifically numerical or statistical reporting issues there, and the same kind of defect was already classed that way elsewhere in the set:

- 2017.21906::C002: repeated effect estimate (RD 6.69 vs 6.63; OR 1.48 vs 1.47)
- 2018.14282::C017: CI endpoint, abstract vs Results
- 2018.14282::C023 and C024: Figure 3 HR orientation (see below)
- 2018.17075::C002: sign of the primary risk difference in the abstract
- 2018.17075::C005 and C006: reversed count/percentage cells in eTable 10

## Discuss list

None. Every candidate could be settled from the supplied PDFs, so none met the "genuinely insufficient after checking" bar. The AI's only `discuss` item (0156::C008) was resolvable (see below).

## Main substantive findings (confirmed)

- **2018.14280, C012–C021 (Table 2, all 10 binary RRs).** The printed RRs and 95% CIs match, to within 0.01, those from a 2×2 table transposed so that rows are event/no event, i.e. P(low arm | event)/P(low arm | no event), for every row. The chi-square P values are correct. Correct crude RRs differ, and the CIs are much wider for rare events: pneumothorax is 1.38 (0.48–3.93), not 1.16 (0.73–1.84). The abstract repeats four of these RRs.
- **2018.14282, C023/C024 (Figure 3A/3B).** For all 26 rows, the HR direction matches standard vs high-flow, not high-flow vs standard, under axis labels that say HR<1 favors high-flow. The overall HRs are near-reciprocals of Table 2 (0.98 → 1.02; 0.85 → 1.17). This includes the only significant interaction (hematologic malignancy, P = .01), which is plotted in the reverse direction.
- **2018.17075, C003/C004.** RR, CI and P for intracranial and extracranial bleeding are swapped between adjacent Table 2 rows. Recomputation and eTable 6 confirm this.
- **2018.0156, C004.** The per-protocol survival CI (−10 to 9.7) is about five times too wide. The Wald method reproduces the neighboring rows (−2.00 to 2.04 expected).
- **2018.18020, C010/C011; 2018.8802, C008.** In each, the CI crosses 0 while P < .05 and the interval is off-center. Each looks like a sign error: an upper limit of −0.51, a lower limit of +1.96, and an upper limit of −0.2 would re-center them.
- **2018.18020, C001.** The abstract says 22% men, but 22 of 30 enrolled were men (73%).
- **Protocol/report:** the primary-endpoint amendment on baseline disability is not reflected in the report (0156::C007). Planned and reported endpoint definitions differ for technique failure (0156::C008), intubation duration and the hypoxemia window (6496::C003/C004), and the SCDE fluid component (0948::C001). Subgroups called prespecified are absent from or different in the SAP (21906::C004/C006). The described control-condition dose differs (9128::C012).

## Disagreements with the AI rationale

- **0156::C008 (AI: discuss).** I retained it as a substantive protocol–report difference. The AI's bound (27 > 21) treated 54/1022 as deaths when those are survivors. With the correct 968/1022 deaths, any composite that includes 28-day mortality would be about 95%, so the reported 2.1% "failure" can only be the procedural component.
- **6496::C002 (AI: retain).** I excluded it. 366 vs 364 is explained by the composite definition: a failed first attempt is a composite failure even without a waveform. 366 = 364 + 2 (ETT arm, 48 failures); 371 = 371 (bougie arm).
- **21906::C005.** The AI called it substantive; I rated it minor. The SAP itself defined the composite with "heparin", so eTable 6 carries over the plan wording for the same outcome.
- **14282::C018.** The AI called it communication only; I rated it a confirmed, substantive error. As written, 153 vs 31 patients "randomized to" each arm (39.4% vs 8.0% of 388) contradicts "no statistical difference". The percentages are of 776.
- **14280::C012–C021, 14282::C023/C024, 17075::C003/C004.** The AI left the mechanism open ("estimator not supplied", "reference group not printed"). In each case I established the mechanism from the printed counts (transposed table, reversed orientation, row swap), which moves these from possible to confirmed and substantive.
- **Rounding candidates (14282::C001–C016, C019–C021; 8802::C003–C006).** These are retained as confirmed but minor. In 14282 no single convention explains Table 1: 11 cells are consistent with truncation, 1 is a forced complement, and most others round conventionally. Two cells (C004 liver, C005 kidney) are true count/percentage conflicts of 1.7 and 2.6 points, which I rated substantive.
- **0948::C006.** Noted that the printed 1.45 equals 8.13 × 0.178, the mortality RRR, which points to a carry-over rather than an unexplained value.

## Judgment conventions used

- **substantive vs minor:** substantive when an extractable estimate, interval or key descriptive value is wrong and its correct value is not recoverable from the paper, or when the direction or precision of an effect is misrepresented. minor when the intended value is recoverable (CI symmetry, the counts, another location) or the deviation is about 0.1 point.
- **I = indeterminate (18020::C009, C012):** the CI and the P value are mutually incompatible, but which one is wrong cannot be determined.
- **Retain vs exclude:** a real but trivial discrepancy without a stated convention explaining it is retained as confirmed and minor. Exclusion is reserved for a discrepancy that a valid rule fully explains.

## Sources and tooling limits

- All cited PDFs were readable. The Read tool's `pages` option failed because `pdftoppm` is not installed. Instead I extracted text and split pages with the system Python `fitz` (PyMuPDF), which the venv lacks. Layout-dependent pages were split and viewed rendered with the Read tool: 21906 and 0156 main articles in full; 14280 main article; 14282 p.7 (Figure 3); 18020 pp.5–8 (Tables 1–2); 9128 pp.3 and 7 (Figures 1–2). Everything else was read from the extracted PDF text. No source was unreadable.
- I used the venv interpreter for all workbook work and statistics (openpyxl, scipy).

## Observations outside the candidate set (not adjudicated)

These are verified arithmetic, recorded for the coordinator only:

- **8802, Table 3:** in-hospital death 11/2400 vs 23/2400 (crude RR 0.48) is printed with HR 0.96 (0.90–1.02).
- **0156, Table 2:** per-protocol survival to admission, −4.0 (−7.6 to 0.6), does not reproduce. The Wald interval is −8.16 to 0.08.
- **0948, protocol p.30:** code blue 150/(55,963 × 4) × 1000 = 0.67 per 1000 patient-days; 0.75 is printed.
- **9128, eTable 1:** at 3 months the difference is −0.01 but the CI (−0.12, 0.13) has midpoint 0.005.
- **21906, p.7:** the text says tobacco cessation counseling was >95% in both groups, but Table 3 shows 94.7% in the intervention group.

## Workbook and script notes

- The scripts ran without error. Note that `recalc_check.py` reports Checks row 6 "Unfinished rows" as `0.0` (a float), not `0`; this is cosmetic.
- Codebook typos: the field header is "Statistcal_or_numerical issue", and the section numbering skips 5 (it goes 4 → 6).
- **Process risk:** the session scratchpad is shared with other concurrent runs (folders for 2019, 2024 and an R_B). I did not open them, but kept my working files in a private subfolder. Shared scratch space is a channel through which independence between R_A and R_B could be broken.
- **Process risk:** reading a PDF in a paper folder caused that folder's pipeline `AGENTS.md` (workflow instructions for the AI pipeline) to be injected into my context by a hook. I ignored it, but it exposes reviewers to pipeline material.

## recalc_check output

```
G: {'PRIMARY READY': 119}
Checks 1 Check -> Result
Checks 2 Reviewer role -> R_A
Checks 3 Candidates -> 119
Checks 4 Primary ready rows -> 119
Checks 5 Discuss / unresolved rows -> 0
Checks 6 Unfinished rows -> 0.0
Checks 7 Workflow status -> PRIMARY READY
Checks 8 Meaning -> PRIMARY READY means independent entry is complete. Discuss remains unresolved and is not counted as absence of error.
Checks 9 Next action -> Inspect G on paper sheets and readiness in Decisions. Save and deliver this file after review.
```
