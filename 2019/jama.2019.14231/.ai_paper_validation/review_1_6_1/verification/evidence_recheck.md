# Mechanical evidence recheck

Stage: evidence_rechecker. Runtime agent: `/root/evidence_recheck`. Fresh `qc161_evidence_rechecker`, model `gpt-6.1-sol`, reasoning effort `high`. Scope: the complete current stable-ID set, C001, including all five affected Table 2 rows and every cited context/comparator location. The complete scope, review contract, START_PROMPT, tooling record, source inventory, current ledger, inclusion screen and three checker findings were read. No legacy review conclusions or external material were used. Sources and reused assets were preserved.

Source authority was the supplied PDFs. Direct CPU-only Poppler 26.01.0 extraction was independently run as `pdftotext -layout -f N -l N SOURCE.pdf -` for main physical PDF pages 1, 4, 7 and 8, and results-supplement physical page 7. Outputs were read directly from stdout rather than from an earlier transcription. Main Table 2 was also independently visually read in the existing fresh source rendering [main page 7 image](../extraction/main_direct_page_007.png), whose recorded engine is Poppler 26.01.0 `pdftoppm -f 7 -l 7 -r 110 -singlefile -png`. This rendering and direct source text agree. No additional derivative, OCR, fallback environment or GPU was needed.

## C001 — Five component-outcome eight-year absolute risk contrasts

**Status:** Pending Human Adjudication

**Evidence state:** reproduced

**Determining recheck fact:** All five registered marginal-risk pairs and printed absolute risk differences match the direct source. For each row, the entire control-minus-surgery interval allowed by one-decimal input precision is disjoint from the interval allowed by the printed contrast's precision. Footnote a supplies the eight-year subtraction direction; methods specify Kaplan–Meier cumulative incidence and bootstrap confidence intervals, without a separate point-contrast definition that reconciles those displays. No transcribed value or source location needed correction.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 cumulative-incidence columns versus REPORT main article Table 2 absolute eight-year risk-difference column and footnote a. All other cited locations are REPORT context or corroboration.

**Classification correction:** None. The conflicting numerical representations occur in one report document. The results supplement agrees with the marginal risks and adds no conflicting cross-document relationship. No PLAN content is a side of the registered inconsistency. The content concerns numerical effect identity and analysis specification, so the domain is statistical_results. The only relationship is S_W; precedence P_R > P_P > S_C > S_W therefore selects S_W without ambiguity. A plan that only corroborates one side would not add a relationship.

**Classification ambiguity:** None from the supplied compared content.

### Location found and source/comparator matched

Every location below was found in the physical PDF pagination, with document role determined from content.

| Exact supplied-source location | Role by content | Location found | Source value/text matched | Comparator or contextual function matched |
|---|---|---|---|---|
| [Main article p. 7, Table 2, heart failure row](../../../jama_aminian_2019_oi_190103.pdf#page=7) | REPORT: outcome result table | Yes; two risk columns, risk-set columns and ARD column | Surgery 6.8 (4.9–8.6), N=2049; control 18.9 (17.6–20.2), N=10093; ARD 12.9 (10.4–15.1) | Matched outcome, eight-year horizon, surgery/control labels and control-minus-surgery direction. Supplement Year 8 row repeats both risks and their CIs. |
| [Main article p. 7, Table 2, coronary artery disease row](../../../jama_aminian_2019_oi_190103.pdf#page=7) | REPORT: outcome result table | Yes; all compared cells | Surgery 7.9 (5.9–9.8), N=2050; control 11.6 (10.5–12.6), N=10331; ARD 4.2 (1.9–6.8) | Same row identity, time and group contrast; supplement Year 8 pair/CIs match. |
| [Main article p. 7, Table 2, cerebrovascular disease row](../../../jama_aminian_2019_oi_190103.pdf#page=7) | REPORT: outcome result table | Yes; all compared cells | Surgery 4.1 (2.7–5.5), N=2245; control 5.6 (4.9–6.3), N=11077; ARD 1.8 (−0.03 to 3.4) | Same row identity, time and group contrast; supplement Year 8 pair/CIs match. The lower ARD limit is negative 0.03, not positive 0.03. |
| [Main article p. 7, Table 2, nephropathy row](../../../jama_aminian_2019_oi_190103.pdf#page=7) | REPORT: outcome result table | Yes; all compared cells | Surgery 6.1 (4.4–7.8), N=1937; control 16.3 (15.0–17.6), N=9190; ARD 11.1 (8.8–13.6) | Same row identity, time and group contrast; supplement Year 8 pair/CIs match. |
| [Main article p. 7, Table 2, atrial fibrillation row](../../../jama_aminian_2019_oi_190103.pdf#page=7) | REPORT: outcome result table | Yes; all compared cells | Surgery 7.9 (6.1–9.7), N=2135; control 13.6 (12.5–14.7), N=10734; ARD 6.5 (4.4–8.7) | Same row identity, time and group contrast; supplement Year 8 pair/CIs match. |
| [Main article p. 7, Table 2 headings and footnotes a/b](../../../jama_aminian_2019_oi_190103.pdf#page=7) | REPORT: result definitions | Yes | Risks labeled cumulative incidence at 8 y, % (95% CI); contrast labeled absolute 8-year risk difference, % (95% CI), superscript a. Footnote a describes 95% bootstrap CIs, 1000 samples, for the difference in eight-year absolute risk, nonsurgical control group minus metabolic surgery. | Footnote b explicitly assigns HRs, HR intervals and P values to adjusted Cox models, with Table 1 baseline variables. This does not supply a distinct adjusted absolute-risk point definition. |
| [Main article p. 4, Statistical Analysis continuation](../../../jama_aminian_2019_oi_190103.pdf#page=4) | REPORT: methods used in the reported cohort analysis | Yes | Kaplan–Meier cumulative-incidence estimates for eight years after index date and absolute risk differences were calculated for each outcome. Difference CIs used the percentile method from 1000 bootstrap iterations. | Fully adjusted Cox models are described separately. No bootstrap mean/median for the point difference, alternative risk population or separate adjusted-risk estimator is specified in these paragraphs. |
| [Main article p. 1, abstract outcomes and results](../../../jama_aminian_2019_oi_190103.pdf#page=1) | REPORT: study abstract | Yes | Secondary endpoints comprise three-component MACE and the six individual primary components; results say all seven prespecified secondary outcomes showed significant differences favoring surgery. | This is qualitative abstract reporting of the affected secondary results, establishing scope context. The abstract does not print the five affected ARD points and is not an additional numerical side of the discrepancy. |
| [Main article p. 8, Figure 3 B–F, title and caption](../../../jama_aminian_2019_oi_190103.pdf#page=8) | REPORT: outcome curves and risk-population description | Yes; all five named panels and caption | Figure title identifies eight-year Kaplan–Meier cumulative incidence; B heart failure, C coronary artery disease, D cerebrovascular disease, E nephropathy, F atrial fibrillation. Baseline surgery/control risk sets are respectively 2049/10093, 2050/10331, 2245/11077, 1937/9190 and 2135/10734. | Caption excludes a patient's history of each nonmortality outcome from that outcome's risk assessment. Initial risk sets agree with Table 2. No separate ARD risk set is printed. Unlabeled curve ordinates were not digitized into exact risks. |
| [Results supplement p. 7, eTable 5, Year 8 heart failure row](../../../joi190103supp1_prod.pdf#page=7) | REPORT: non-plan results supplement | Yes | Surgery 6.8 (4.9, 8.6); nonsurgical 18.9 (17.6, 20.2) | Both points and marginal CIs exactly corroborate the main row. |
| [Results supplement p. 7, eTable 5, Year 8 coronary artery disease row](../../../joi190103supp1_prod.pdf#page=7) | REPORT: non-plan results supplement | Yes | Surgery 7.9 (5.9, 9.8); nonsurgical 11.6 (10.5, 12.6) | Both points and marginal CIs match. |
| [Results supplement p. 7, eTable 5, Year 8 cerebrovascular disease row](../../../joi190103supp1_prod.pdf#page=7) | REPORT: non-plan results supplement | Yes | Surgery 4.1 (2.7, 5.5); nonsurgical 5.6 (4.9, 6.3) | Both points and marginal CIs match. |
| [Results supplement p. 7, eTable 5, Year 8 nephropathy row](../../../joi190103supp1_prod.pdf#page=7) | REPORT: non-plan results supplement | Yes | Surgery 6.1 (4.4, 7.8); nonsurgical 16.3 (15.0, 17.6) | Both points and marginal CIs match. |
| [Results supplement p. 7, eTable 5, Year 8 atrial fibrillation row](../../../joi190103supp1_prod.pdf#page=7) | REPORT: non-plan results supplement | Yes | Surgery 7.9 (6.1, 9.7); nonsurgical 13.6 (12.5, 14.7) | Both points and marginal CIs match. Supplement heading identifies cumulative incidence after index date; no ARD is printed there. |

All numeric risk/contrast values are percentages, interpreted arithmetically as percentage points for subtraction. Parentheses contain the source-reported 95% CIs. Risk-set counts identify the rows/populations; they are not denominators used to recompute Kaplan–Meier risks.

### Consistency rule applicable and calculation reproduced

**Consistency rule applicable:** Yes, for the contrast as described. Footnote a supplies nonsurgical control minus metabolic surgery for eight-year absolute risk, and the same-row adjacent columns supply eight-year group risks. The recheck compares these supplied time-to-event risks, not crude count ratios. The separate Cox HR estimand is not substituted for the ARD estimand. The source does not state that the ARD point is a bootstrap mean, median, adjusted risk or contrast of differently defined populations.

**Display-precision rule:** Each displayed one-decimal risk and ARD is allowed its full half-unit interval, ±0.05 percentage points. For displayed surgery risk S, control risk C and ARD A, the allowed risk subtraction is [C−S−0.10, C−S+0.10] and the allowed ARD is [A−0.05, A+0.05]. Closed boundaries are used conservatively: their disjointness also implies disjointness for customary half-open rounding intervals. No assumption about unseen trailing digits is needed.

| Outcome | Displayed subtraction | Surgery half-unit interval | Control half-unit interval | Allowed control-minus-surgery interval | Printed ARD half-unit interval | Comparison reproduced |
|---|---|---|---|---|---|---|
| Heart failure | 18.9−6.8=12.1 | [6.75, 6.85] | [18.85, 18.95] | [12.00, 12.20] | [12.85, 12.95] | Yes: 12.20 < 12.85; minimum separation 0.65 percentage points. |
| Coronary artery disease | 11.6−7.9=3.7 | [7.85, 7.95] | [11.55, 11.65] | [3.60, 3.80] | [4.15, 4.25] | Yes: 3.80 < 4.15; minimum separation 0.35. |
| Cerebrovascular disease | 5.6−4.1=1.5 | [4.05, 4.15] | [5.55, 5.65] | [1.40, 1.60] | [1.75, 1.85] | Yes: 1.60 < 1.75; minimum separation 0.15. |
| Nephropathy | 16.3−6.1=10.2 | [6.05, 6.15] | [16.25, 16.35] | [10.10, 10.30] | [11.05, 11.15] | Yes: 10.30 < 11.05; minimum separation 0.75. |
| Atrial fibrillation | 13.6−7.9=5.7 | [7.85, 7.95] | [13.55, 13.65] | [5.60, 5.80] | [6.45, 6.55] | Yes: 5.80 < 6.45; minimum separation 0.65. |

For context, the other Table 2 rows reproduce their printed differences: primary 47.7−30.8=16.9, secondary composite 27.6−17.0=10.6, mortality 17.8−10.0=7.8. All five registered ARD points are contained in their own printed CIs. The recheck reproduces a point-contrast discrepancy, not a CI-containment or adjusted-HR test discrepancy. Marginal CI endpoints were not subtracted to reconstruct a difference CI; such subtraction would not reproduce a paired/bootstrap uncertainty calculation.

### Necessary inputs and exact missing definitions

**Necessary inputs available:** Yes for the registered mechanical comparison: all ten marginal risk points, five ARD points, precision, percentage scale, eight-year time, group direction, outcome identities, same-row risk-set labels, Kaplan–Meier description and explicit contrast direction. All five source ARD CIs and all corresponding marginal CIs are also available. No cited unit is inaccessible or unreadable.

**Necessary inputs missing for original-analysis reconstruction:** Unrounded original Kaplan–Meier point estimates; the actual point-estimate operation producing the ARD column, including whether it was the original-sample contrast or a summary over bootstrap replicates; any separate risk inputs or adjustment model used for that contrast; confirmation of the event, censoring and population definitions actually used in each contrast calculation; individual event/censoring histories or equivalent original analysis output; bootstrap replicate contrasts and the resampling implementation needed to regenerate the confidence limits. These omissions prevent determination of the intended extraction value and independent regeneration of the supplied CIs. They do not prevent the displayed-precision comparison above.

### Source-grounded alternatives and direct observation versus explanation

**Direct observation:** The direct source supplies ten risks, five ARDs and an explicit contrast direction, with interval pairs that remain disjoint after precision allowance. The supplement repeats the same marginal risks. The main methods assign percentile bootstrapping to the risk-difference intervals and adjusted Cox modeling to HRs. The figure gives the same endpoint-specific initial risk sets. These are observations from the supplied evidence.

**Source-grounded alternative interpretation:** Because bootstrap analysis is reported, the ARD points might be a summary of resampled contrasts rather than the difference of original-sample risks. Alternatively, they might use distinct risk inputs, population or censoring definitions not described for the contrast. These possibilities are inferred explanations only; neither is specified or demonstrated by the supplied compared content. The bootstrap CI description alone does not establish a separate point estimator. An original-output reconciliation may identify which display represents the intended quantity, but this recheck does not select a replacement value or attribute a cause.

The repeated pattern is retained as one candidate, with all five rows. The other rows' arithmetic does not determine the cause of this pattern. No consequence for adjusted HR significance or the overall study conclusion is inferred.

**Exact remaining human question:** For each of heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation, which point estimator, unrounded eight-year group risks, analysis population and event/censoring rules generated the printed Table 2 ARD and its bootstrap interval; do those inputs match the adjacent Kaplan–Meier columns, and which absolute risk contrast should a data extractor use?

## Scope completion

Stable IDs covered: C001 (1/1). Repeated-pattern rows checked: 5/5. All cited pages and their affected source/comparator locations found and read; direct source/transcription disagreements: none. Classification changes: none. Evidence states: C001 reproduced. Remaining limits concern the original point-estimator definition and analysis inputs, as named above; there is no recheck coverage gap. Human adjudication remains pending. This artifact makes no disposition and preserves C001.
