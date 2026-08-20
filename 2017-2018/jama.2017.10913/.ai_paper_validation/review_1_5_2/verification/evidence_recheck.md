# Mechanical Evidence Recheck

**Scope:** Every stable candidate in `candidate_ledger.md` was rechecked separately against the cited supplied-source PDF page. Fresh native text, layout text, and rendered pages were used only as locators and visual aids; the direct PDFs remained the authority.

**Status:** Every candidate remains Pending Human Adjudication. The records below are source and comparison facts, not dispositions.

## C001 — Discontinuation-reason counts do not exhaust the stated 65 recipients stopping before 4 L

**Status:** Pending Human Adjudication.

- **Cited location found:** Found in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](../../../jama_andrews_2017_oi_170091.pdf#page=4), Hemodynamic Interventions, left column.
- **Source printed value/text matched:** The page prints 41 patients (38.7%) receiving 4 L or more and then identifies “the remaining 65 patients (61.3%)” whose fluids were discontinued before 4 L.
- **Comparator printed value/text matched:** The same sentence prints four reasons and counts: respiratory-rate increase or oxygen-saturation decrease, 32; JVP of 3 cm or greater, 9; blood transfusion through an intravenous line, 5; and other reasons, 4.
- **Consistency rule applicable:** An exact integer partition applies if the four reasons introduced by “due to” are intended to exhaust the 65 patients and are assigned once per patient. The source does not state whether the list is exhaustive or whether reasons can overlap, so applicability of a complete-partition rule remains conditional.
- **Calculation or logical comparison reproduced:** `32 + 9 + 5 + 4 = 50`; `65 - 50 = 15`. The four displayed percentages sum to `30.2% + 8.5% + 4.7% + 3.8% = 47.2%`, consistent with 50 of 106 at one decimal and not with all 65 of 106.
- **Necessary inputs available or missing:** The 65-person comparator and all four listed counts are available. Missing are an explicit exhaustive/non-exhaustive statement, a mutually-exclusive/overlapping-reasons definition, and the reason assignment for the residual 15 patients if the categories are exhaustive.
- **Source-grounded alternative interpretation:** The four reasons may be non-exhaustive, patients may have more than one reason, or an unlisted operational or time-based reason may account for some patients. None of those qualifications is printed in the supplied passage.
- **Direct observation versus inferred explanation:** Direct observation is limited to the printed 65, the four labels, and the counts 32, 9, 5, and 4. The 50 sum and 15 residual are reproduced arithmetic. Any explanation involving omissions, overlap, or another stopping reason is inferred.
- **Exact remaining human question:** Were the four printed reasons intended to be exhaustive and mutually exclusive for the 65 patients who stopped before 4 L; if not, what category, overlap, and denominator qualification should be stated?

## C002 — Usual-care fluid-bolus percentage does not reconcile with its printed count and arm denominator

**Status:** Pending Human Adjudication.

- **Cited location found:** The process statement is present in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](../../../jama_andrews_2017_oi_170091.pdf#page=4), Hemodynamic Interventions, left column. The arm denominator is also present on p. 4 in Figure 1 and in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 6](../../../jama_andrews_2017_oi_170091.pdf#page=6), Table 2 header.
- **Source printed value/text matched:** The narrative prints: “In the usual care group, only 50 patients (48.3%) received any intravenous fluid bolus.”
- **Comparator printed value/text matched:** Figure 1 prints 103 usual-care participants included in the primary analysis, and Table 2 labels the usual-care column `n = 103`.
- **Consistency rule applicable:** Count-percentage identity applies if the bolus process result uses the displayed 103-person usual-care analysis population. The process sentence does not print a separate denominator or available-case qualifier, so the identity is source-supported but its denominator assignment still requires confirmation.
- **Calculation or logical comparison reproduced:** `50 / 103 x 100 = 48.543689%`, which rounds to 48.5% at one decimal, not 48.3%. Under ordinary nearest-tenth rounding, no integer denominator near the stated arm size produces 48.3% from a numerator of 50: 50/103 is 48.5% and 50/104 is 48.1% at one decimal.
- **Necessary inputs available or missing:** The printed count, percentage, and two occurrences of the 103-person arm denominator are available. Missing are the denominator actually used for this process measure, any available-case population definition, and any nonstandard percentage calculation or rounding rule.
- **Source-grounded alternative interpretation:** The bolus result may use an unstated process-measure population; alternatively, the count or percentage may be a transcription error. A different integer denominator alone does not reproduce 48.3% under ordinary nearest-tenth rounding near the displayed arm size.
- **Direct observation versus inferred explanation:** Direct observation is the printed 50 (48.3%) and the repeated usual-care `n = 103`. The recalculated 48.5% is arithmetic. Any unstated denominator, population, or transcription mechanism is inferred.
- **Exact remaining human question:** What exact denominator and rounding rule generated the printed 50 (48.3%) usual-care bolus result, and does it use the same 103-person usual-care population shown in Figure 1 and Table 2?

## C003 — Usual-care lactate-change IQR differs between narrative and Table 2 and is nonascending in the narrative

**Status:** Pending Human Adjudication.

- **Cited location found:** Found in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](../../../jama_andrews_2017_oi_170091.pdf#page=4), Hemodynamic Interventions, right column, and in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 6](../../../jama_andrews_2017_oi_170091.pdf#page=6), Table 2, lactate-change row.
- **Source printed value/text matched:** The p. 4 narrative prints usual-care median change `-0.5 mmol/L; IQR, 2.2 to 1.1 mmol/L`.
- **Comparator printed value/text matched:** Table 2 prints usual-care change `-0.5 (-2.2 to 1.1)` mmol/L. It labels the same baseline-to-6-hour change and the same usual-care group.
- **Consistency rule applicable:** An IQR's lower endpoint must not exceed its upper endpoint, and matched narrative and table displays for the same group, measure, and time point should preserve endpoint signs. Both rules apply directly because no different subset, scale, or time point is printed.
- **Calculation or logical comparison reproduced:** In the narrative, `2.2 > 1.1`, so the endpoints are nonascending. Across locations, the lower endpoint is `2.2` on p. 4 and `-2.2` in Table 2; the difference is the sign of that endpoint.
- **Necessary inputs available or missing:** Both displayed medians, both IQR endpoint pairs, units, group, and time point are available. Missing are the underlying observations or source analysis output needed to determine which lower endpoint is intended.
- **Source-grounded alternative interpretation:** The narrative may have lost a minus sign, Table 2 may contain the discrepant sign, or the two displays may use different unlabelled subsets. The last interpretation has no printed population qualifier supporting it.
- **Direct observation versus inferred explanation:** Direct observation is the two printed displays and the narrative's reversed endpoint order. Inferring a dropped minus sign as the production mechanism is plausible but not established by the supplied source.
- **Exact remaining human question:** What is the intended lower IQR endpoint for usual-care lactate change, and do the narrative and Table 2 use the identical analysis population and baseline-to-6-hour definition?

## C004 — Respiratory-compromise oxygen-saturation threshold is labelled inconsistently

**Status:** Pending Human Adjudication.

- **Cited location found:** Found in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 3](../../../jama_andrews_2017_oi_170091.pdf#page=3), Outcomes; DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](../../../jama_andrews_2017_oi_170091.pdf#page=4), results text; and DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 6](../../../jama_andrews_2017_oi_170091.pdf#page=6), Table 2 row and footnote b.
- **Source printed value/text matched:** The Outcomes definition on p. 3 prints a decrease in oxygen saturation of `>=3%`; p. 4 reports a decrease of `3% or greater`; and the Table 2 row label on p. 6 again prints oxygen saturation decreased by `>=3%`.
- **Comparator printed value/text matched:** Table 2 footnote b on p. 6 defines respiratory compromise using “a decrease in oxygen saturation of more than 3% from baseline.”
- **Consistency rule applicable:** Matched outcome definitions require threshold-set identity. `>=3%` includes an exactly 3-percentage-point decrease, whereas `>3%` excludes it. This logical boundary rule applies directly to the printed labels.
- **Calculation or logical comparison reproduced:** The symmetric difference between the printed threshold sets is the boundary value `{3%}`. No numerical rounding calculation is needed.
- **Necessary inputs available or missing:** The competing threshold texts, outcome label, and displayed counts of 38/106 versus 23/103 are available. Missing are the operational coding rule, individual oxygen-saturation changes, and a statement identifying which threshold was used to calculate the table counts.
- **Source-grounded alternative interpretation:** “More than 3%” may be informal wording intended to include 3%, the footnote or the methods/results label may be typographically imprecise, or the table may have used a deliberately stricter threshold that was not separately disclosed.
- **Direct observation versus inferred explanation:** Direct observation is the `>=3%`/“3% or greater” wording versus “more than 3%.” The possibility that any participant or displayed count changes at the boundary is inferred because individual measurements are not supplied.
- **Exact remaining human question:** Was the respiratory-compromise oxygen-saturation criterion `>=3%` or `>3%`, and which exact rule was applied to produce the 38/106 and 23/103 Table 2 counts?

## C005 — Figure 2’s 94.2% vital-status percentage does not reconcile with the displayed modified-ITT/28-day counts

**Status:** Pending Human Adjudication.

- **Cited location found:** Found in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](../../../jama_andrews_2017_oi_170091.pdf#page=4), Figure 1, and DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 6](../../../jama_andrews_2017_oi_170091.pdf#page=6), Figure 2 risk set and caption.
- **Source printed value/text matched:** Figure 2 states: “Vital status was known through study day 28 for 194 patients (94.2%).” Its day-zero risk set prints 106 sepsis-protocol and 103 usual-care participants.
- **Comparator printed value/text matched:** Figure 1 prints 106 and 103 participants in the primary analysis, 9 and 6 lost after hospital discharge, and 97 and 97 included in the 28-day mortality analysis. Thus it displays 209 primary-analysis participants and 194 with 28-day status.
- **Consistency rule applicable:** A count-percentage identity applies to the caption if its denominator is the 209-person modified-ITT cohort displayed in the two figures. Figure 2 does not state a different denominator, but the exact denominator underlying 94.2% is not printed in the caption.
- **Calculation or logical comparison reproduced:** `97 + 97 = 194`; `106 + 103 = 209`; `9 + 6 = 15`; and `209 - 15 = 194`. However, `194 / 209 x 100 = 92.822967%`, which rounds to 92.8%, not 94.2%. Conversely, `194 / 206 x 100 = 94.174757%`, which rounds to 94.2%, but no 206-person denominator is printed for this statement.
- **Necessary inputs available or missing:** The cohort, loss, and 28-day-known-status counts needed for the 209-person comparison are available. Missing are the caption's intended percentage denominator and any definition or exclusion accounting for a denominator of 206 rather than 209.
- **Source-grounded alternative interpretation:** The percentage may use an unstated 206-person eligible subset, the percentage may be a calculation or transcription error, or “known” may refer to a population different from Figure 1's 28-day analysis. The supplied figures do not define such a distinction.
- **Direct observation versus inferred explanation:** Direct observation is the printed 194 (94.2%), the 106/103 risk set, the 97/97 analysis counts, and the 9/6 losses. The 209 denominator follows exact displayed addition; a hypothetical denominator of 206 and any associated three-person exclusion are inferred.
- **Exact remaining human question:** What denominator produced Figure 2's 94.2%, and if it is not the 209-person modified-ITT cohort, which three participants are excluded and by what printed population rule?

## C006 — Protocol Table 2 column headers and row percentages use incompatible denominators

**Status:** Pending Human Adjudication.

- **Cited location found:** Found in DOC-002, [joi170091supp1_prod.pdf — PDF p. 9](../../../joi170091supp1_prod.pdf#page=9), Table 2, “Baseline characteristics in SSSP participants.”
- **Source printed value/text matched:** The table headers print `Total n=76`, `SSSP n=36`, and `Control n=44`.
- **Comparator printed value/text matched:** Control cells print HIV positive `31 (78)`, confusion `27 (68)`, respiratory rate greater than 40 `14 (35)`, SBP less than 90 or MAP less than 65 `13 (33)`, metabolic acidosis `13 (33)`, and acidotic or hypotensive `17 (42)`. The row counts also add across arms to the total-column counts, such as `26 + 31 = 57` and `22 + 27 = 49`.
- **Consistency rule applicable:** For the two arm headers of a total-column baseline table, exact partition identity requires `Total n = SSSP n + Control n`. Absent a row-specific denominator note, each count-percentage pair should also use its column header denominator. The table supplies no exception footnote, so both rules apply to the printed display.
- **Calculation or logical comparison reproduced:** The headers give `36 + 44 = 80`, not 76. Against `n=44`, the six control percentages calculate as 70.5%, 61.4%, 31.8%, 29.5%, 29.5%, and 38.6%, not 78%, 68%, 35%, 33%, 33%, and 42%. Against a denominator of 40, the corresponding exact percentages are 77.5%, 67.5%, 35.0%, 32.5%, 32.5%, and 42.5%, each within 0.5 percentage point of the printed whole-number display; `36 + 40 = 76` also reproduces the total header.
- **Necessary inputs available or missing:** All headers, row counts, and displayed whole percentages are available. Missing are the intended table population, any available-case denominator by row, the rounding convention for exact half-percentage values, and confirmation whether the control header should be 40, 44, or another value.
- **Source-grounded alternative interpretation:** The control header may have been intended as `n=40`; alternatively, the total header, row percentages, or population label may come from different preliminary table versions or from an unstated subset. The nearby 89 enrolled and 74 with primary-outcome data are differently labelled stages and do not resolve the table's internal header conflict.
- **Direct observation versus inferred explanation:** Direct observation is the printed 76/36/44 headers and all listed cells. The sums and percentage recalculations are reproduced arithmetic. Treating 40 as the intended control denominator or attributing the display to version mismatch is inferred.
- **Exact remaining human question:** What are the intended Total, SSSP, and Control denominators for protocol Table 2, what rounding rule was used for its whole percentages, and do all displayed rows use those same denominators?

## C007 — Printed 28-day usual-care mortality percentage does not round from the displayed follow-up and total-death counts

**Status:** Pending Human Adjudication.

- **Cited location found:** Found in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 5](../../../jama_andrews_2017_oi_170091.pdf#page=5), Clinical Outcomes; DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](../../../jama_andrews_2017_oi_170091.pdf#page=4), Figure 1; and DOC-003, [joi170091supp2_prod.pdf — PDF p. 5](../../../joi170091supp2_prod.pdf#page=5), eMethods section D.
- **Source printed value/text matched:** DOC-001 p. 5 states that vital status was known for 97 patients in each group and prints 28-day mortality of 67.0% for the sepsis-protocol group versus 45.3% for usual care.
- **Comparator printed value/text matched:** Figure 1 independently prints 97 participants per arm in the 28-day analysis. DOC-003 p. 5 prints 109 deaths among 194 patients with 28-day follow-up.
- **Consistency rule applicable:** Count-percentage identity and ordinary nearest-tenth rounding apply if the 109/194 supplement total and the 97-per-arm main-article results describe the same 28-day cohort. Their labels and totals match, but exact arm-specific death counts and the rounding convention are not directly printed.
- **Calculation or logical comparison reproduced:** With denominator 97, 67.0% uniquely corresponds to 65 deaths under ordinary nearest-tenth rounding. The supplied total then gives `109 - 65 = 44` usual-care deaths. `44 / 97 x 100 = 45.360825%`, which rounds to 45.4%, not 45.3%. The same derived counts give protocol risk 67.0103% and a difference of 21.6495 percentage points, consistent with the printed 67.0% and 21.6% at one decimal.
- **Necessary inputs available or missing:** Available are the 97-per-arm denominators, both printed arm percentages, the 109/194 total, and the printed 21.6-point difference. Missing are directly printed arm-specific 28-day death counts, an explicit statement tying the supplement total to the exact same arm analysis, and the percentage rounding or truncation convention.
- **Source-grounded alternative interpretation:** The source may truncate rather than round the usual-care percentage; the supplement total may use a differently defined 194-person population despite the matching outcome label; or one count or percentage may be misprinted.
- **Direct observation versus inferred explanation:** Direct observation is limited to 97 per arm, 67.0% versus 45.3%, and 109/194 total deaths. The 65 and 44 arm death counts are derived from those displays under ordinary nearest-tenth rounding; any production explanation is inferred.
- **Exact remaining human question:** What are the exact arm-specific 28-day death counts, does DOC-003's 109/194 total use the same 97-per-arm cohort, and was 45.3% produced by rounding, truncation, or another rule?

## C008 — HIV-negative subgroup risk ratio does not reconcile with its printed deaths and denominators

**Status:** Pending Human Adjudication.

- **Cited location found:** Found in DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 7](../../../jama_andrews_2017_oi_170091.pdf#page=7), Figure 3, HIV-negative row.
- **Source printed value/text matched:** The row prints 9 sepsis-protocol and 9 usual-care patients, with deaths `3 (33.3%)` and `5 (55.6%)`.
- **Comparator printed value/text matched:** The same row prints `Relative Risk 0.75 (95% CI, 0.23-2.44)`. The figure labels the columns “No. of Patients,” “In-hospital Mortality, No. (%),” and “Relative Risk (95% CI).”
- **Consistency rule applicable:** The crude risk ratio from the displayed deaths and denominators should equal the displayed row RR if the figure uses an unadjusted ratio of the two displayed risks. The source does not state that the subgroup RR is adjusted, weighted, standardized, or calculated from a different population, so the crude identity is the directly reproducible rule but the exact estimator remains an essential missing definition.
- **Calculation or logical comparison reproduced:** `(3 / 9) / (5 / 9) = 3 / 5 = 0.60`, not 0.75. The component percentages do reconcile: 3/9 is 33.3% and 5/9 is 55.6% at one decimal. The printed 0.75 is inside its ordered CI and is directionally below 1, so the reproduced issue is the point estimate versus the displayed counts, not interval order or direction.
- **Necessary inputs available or missing:** The deaths, denominators, percentages, RR, CI, population label, and outcome are available. Missing are the exact row-specific RR estimator, any adjustment or weighting variables, variance/CI construction, and confirmation that all row elements use the same subgroup population.
- **Source-grounded alternative interpretation:** The RR may come from an undisclosed non-crude estimator or different analysis population; alternatively, one displayed count, denominator, or RR may be transcribed incorrectly. The figure provides no printed adjustment label resolving the difference.
- **Direct observation versus inferred explanation:** Direct observation is the complete printed row. The 0.60 crude RR is direct arithmetic. Any non-crude method, alternative population, or transcription mechanism is inferred.
- **Exact remaining human question:** Which estimator and analysis population generated the HIV-negative RR of 0.75, and do the printed 3/9, 5/9, RR, and CI all arise from that same analysis?

## C009 — Protocol background culture-yield percentage does not round from its printed count and denominator

**Status:** Pending Human Adjudication.

- **Cited location found:** Found in DOC-002, [joi170091supp1_prod.pdf — PDF p. 7](../../../joi170091supp1_prod.pdf#page=7), “Blood cultures and antibiotics” background paragraph.
- **Source printed value/text matched:** The paragraph states that, after excluding probable contaminants, 36 patients had positive aerobic blood cultures.
- **Comparator printed value/text matched:** The same sentence prints `36 (22.3%) of 161 septic patients`.
- **Consistency rule applicable:** Exact count-denominator percentage identity with ordinary nearest-tenth rounding applies because the numerator, denominator, and one-decimal percentage are printed together without an available-case or approximate qualifier.
- **Calculation or logical comparison reproduced:** `36 / 161 x 100 = 22.360248%`, which rounds to 22.4% at one decimal, not 22.3%. The exact value differs from the displayed 22.3% by approximately 0.060 percentage point.
- **Necessary inputs available or missing:** The numerator, denominator, population label, exclusion qualifier, and displayed percentage are available. Missing are the source's rounding convention and any indication that 36 or 161 is approximate or that another denominator was used.
- **Source-grounded alternative interpretation:** The percentage may have been truncated to one decimal, or one of the printed count/denominator/percentage values may be transcriptional or contextual shorthand. No alternative denominator or rounding rule is printed.
- **Direct observation versus inferred explanation:** Direct observation is the full printed count-percentage-denominator statement. The 22.360248% calculation is reproduced arithmetic. Truncation or transcription is an inferred explanation.
- **Exact remaining human question:** Was 22.3% intentionally truncated, and if not, what exact numerator, denominator, and rounding convention were intended for this culture-yield statement?
