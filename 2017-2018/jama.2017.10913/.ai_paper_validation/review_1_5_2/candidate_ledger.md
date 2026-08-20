# Stable Candidate Ledger

**Status:** Pending Human Adjudication.

Nine distinct supplied-source quality-control candidates were registered after merging only genuine duplicate provisional records with the same printed values, comparator, and rule. Cross-source/statistical duplicates of C006 and C008 were merged before stable IDs. The provisional eTable 4 Cox HR/CI/P diagnostic was not registered: the supplied package does not establish that its P value and CI use compatible tests, sidedness, variance, and construction rules, so it does not meet the workflow's statistical-candidate threshold. No candidate is deleted, merged, or renumbered after this ledger.

## C001 — Discontinuation-reason counts do not exhaust the stated 65 recipients stopping before 4 L

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-001, `jama_andrews_2017_oi_170091.pdf#page=4`, Hemodynamic Interventions, left column.
- **Printed inputs/comparator:** The article states that 41/106 (38.7%) received 4 L or more and that, “Among the remaining **65 patients (61.3%)**,” fluids “were discontinued prior to a total volume of 4 L due to” respiratory-rate/oxygen-saturation change **32**, JVP >=3 cm **9**, transfusion **5**, and other reasons **4**.
- **Rule and calculation:** If the four printed reasons are the complete explanation introduced by “due to,” their counts should total the stated remaining population: 32+9+5+4=**50**, not 65; residual=65−50=**15 patients**. The displayed reason percentages also total 47.2% of 106, consistent with 50 people rather than 65.
- **Tolerance:** Exact integer-partition rule; no rounding tolerance applies.
- **Direct observation vs inference:** Directly observed are the quoted 65 and four counts. The inference is that the sentence presents the four categories as reasons for that 65-person group; no fifth category or overlapping-category statement is printed.
- **Source-grounded alternatives:** The categories may be non-exhaustive despite the phrasing; some patients may have had multiple reasons; or 15 may have stopped for an unlisted operational/time reason. The supplied source does not specify which interpretation applies.
- **Quality-control relevance:** The number and reasons for not reaching the intended fluid volume can be extracted as an intervention-adherence/process result; the unreconciled total can change how that process result is tabulated.
- **Human question:** Do the four listed counts intentionally represent only a subset or overlapping reasons among the 65, and if so, what denominator/category statement should accompany them?

## C002 — Usual-care fluid-bolus percentage does not reconcile with its printed count and arm denominator

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-001, `jama_andrews_2017_oi_170091.pdf#page=4`, Hemodynamic Interventions, left column.
- **Printed inputs/comparator:** The text states: “In the usual care group, only **50 patients (48.3%)** received any intravenous fluid bolus.” The immediately applicable usual-care analysis denominator is **103**, printed in the same article's Figure 1/primary-analysis display on p.4 and Table 2 header on p.6.
- **Rule and calculation:** 50/103×100=**48.54%**, which rounds to **48.5%** at one decimal, not 48.3%.
- **Tolerance:** One-decimal percentage tolerance ±0.05 percentage point; the discrepancy from the exact percentage is 0.24 points.
- **Direct observation vs inference:** Directly observed are the 50 count, 48.3% display, and n=103 usual-care population. The inference is only that at least one displayed element or its unprinted denominator differs; no replacement value is asserted.
- **Source-grounded alternatives:** The exact denominator back-calculated from 50/0.483 is nonintegral (about 103.52), and neither 103 nor 104 produces 48.3% under ordinary nearest-tenth rounding; the count or percentage may be misprinted, or an unstated denominator or calculation rule may have been used.
- **Quality-control relevance:** This is a reported usual-care process proportion and is used to characterize between-group fluid exposure; an unreconciled denominator can affect extraction of that measure.
- **Human question:** What denominator was used for the printed 50 (48.3%) usual-care bolus result, and should the count, percentage, or population label be revised/qualified?

## C003 — Usual-care lactate-change IQR differs between narrative and Table 2 and is nonascending in the narrative

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001, `jama_andrews_2017_oi_170091.pdf#page=4`, Hemodynamic Interventions, right column; comparator DOC-001, `jama_andrews_2017_oi_170091.pdf#page=6`, Table 2, “Change in lactic acid concentration from baseline to 6 h after enrollment.”
- **Printed inputs/comparator:** p.4 gives usual care median **−0.5 mmol/L; IQR, 2.2 to 1.1 mmol/L**. Table 2 gives usual care **−0.5 (−2.2 to 1.1)** mmol/L.
- **Rule and calculation:** A displayed IQR lower endpoint must not exceed its upper endpoint, and matched narrative/table values should agree. The p.4 printed order is 2.2>1.1 and differs by the sign of the lower endpoint from Table 2 (2.2 versus −2.2).
- **Tolerance:** Endpoint order/sign identity rule; no rounding tolerance applies.
- **Direct observation vs inference:** Directly observed are both printed IQRs. The inference is that the p.4 lower endpoint may have lost a minus sign; that is not asserted as a correction.
- **Source-grounded alternatives:** The narrative may contain a sign/transcription error; Table 2 may instead be the discrepant location; or the two locations may refer to differently defined usual-care subsets, although neither printed passage identifies such a distinction.
- **Quality-control relevance:** The lactate-change distribution is a reported process/physiologic result; an incorrect sign reverses the apparent direction of the lower tail.
- **Human question:** Which lower IQR endpoint and sign are intended for usual-care lactate change, and do the two locations describe the identical analysis population/timepoint?

## C004 — Respiratory-compromise oxygen-saturation threshold is labelled inconsistently

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-001, `jama_andrews_2017_oi_170091.pdf#page=3`, Outcomes definition (decrease in oxygen saturation of **>=3%**); comparator `jama_andrews_2017_oi_170091.pdf#page=6`, Table 2 footnote b (decrease in oxygen saturation of **more than 3%** from baseline). p.4 Results also reports “decrease … of **3% or greater**.”
- **Printed inputs/comparator:** The methods/results definition includes an exactly 3-percentage-point decrease; Table 2’s footnote excludes it by using “more than 3%.”
- **Rule and calculation:** Threshold identity for a matched reported outcome requires the same boundary. `>=3%` includes 3%; `>3%` does not. The difference is the boundary set `{3%}`.
- **Tolerance:** Logical threshold-label rule; no numerical rounding tolerance applies.
- **Direct observation vs inference:** Directly observed are the distinct threshold words. The inference is that patients exactly at 3% could be classified differently; the source lacks individual values, so any numerical impact is unknown.
- **Source-grounded alternatives:** “More than 3%” may be informal wording for the intended >=3% threshold; one definition may be a typographical error; or the table may use a deliberately stricter analysis definition that is not disclosed.
- **Quality-control relevance:** The threshold defines the Table 2 respiratory-compromise count and the reported safety outcome (38/106 versus 23/103); inconsistent boundary wording can affect extraction and replication of that outcome.
- **Human question:** Was respiratory compromise defined at oxygen-saturation decrease >=3% or >3%, and was the Table 2 count calculated under the same definition as the methods/results text?

## C005 — Figure 2’s 94.2% vital-status percentage does not reconcile with the displayed modified-ITT/28-day counts

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-001, `jama_andrews_2017_oi_170091.pdf#page=4`, Figure 1 (106 and 103 primary-analysis participants; 9 and 6 lost after discharge; 97 each in 28-day analysis); comparator `jama_andrews_2017_oi_170091.pdf#page=6`, Figure 2 caption (“Vital status was known through study day 28 for **194 patients (94.2%)**”).
- **Printed inputs/comparator:** Figure 1 gives 97+97=**194** with known 28-day status and 106+103=**209** in the primary analysis; it also displays 9+6=**15** losses, so 209−15=194. Figure 2 pairs 194 with **94.2%**.
- **Rule and calculation:** Using the displayed 209-person modified-ITT cohort, 194/209=**92.8%**, not 94.2%. Conversely, 194/0.942≈**206**, but no 206-person denominator is printed for this vital-status statement.
- **Tolerance:** One-decimal percentage requires agreement within 0.05 percentage point; discrepancy is 1.4 points.
- **Direct observation vs inference:** Directly observed are the two figures’ counts and printed percentage. The inference is that Figure 2’s percentage uses an unprinted denominator of approximately 206 or is misprinted; no correction is assumed.
- **Source-grounded alternatives:** A three-person exclusion from a denominator not stated in the caption could explain 194/206; the 94.2% may be a typographical or calculation error; or “known” may use a population different from Figure 1’s 28-day-analysis population.
- **Quality-control relevance:** Follow-up completeness is a quantitative outcome-supporting denominator; an ambiguous percentage can alter assessment of missing 28-day vital status.
- **Human question:** What is the denominator for the Figure 2 94.2% statement, and how does it relate to the 209 modified-ITT participants and 194 participants shown in Figure 1’s 28-day analysis?

## C006 — Protocol Table 2 column headers and row percentages use incompatible denominators

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-002, `joi170091supp1_prod.pdf#page=9`, Table 2, “Baseline characteristics in SSSP participants.”
- **Printed inputs/comparator:** Headers print **Total n=76**, **SSSP n=36**, and **Control n=44**. The group headers sum to 36+44=**80**, not 76. In the Control column, HIV-positive is **31 (78)**, confusion **27 (68)**, respiratory rate >40 **14 (35)**, SBP <90 or MAP <65 **13 (33)**, metabolic acidosis **13 (33)**, and acidotic or hypotensive **17 (42)**.
- **Rule and calculation:** A three-column partition must satisfy total=group1+group2. It fails: 76≠80. The control percentages are incompatible with n=44 (31/44=70.5%, 27/44=61.4%, 14/44=31.8%, 13/44=29.5%, 17/44=38.6%). A denominator of 40 is diagnostic because the displayed percentages lie within 0.5 percentage point of 31/40=77.5%, 27/40=67.5%, 14/40=35.0%, 13/40=32.5%, and 17/40=42.5%, but no single ordinary tie-rounding rule yields both the printed 33 and 42 from the two .5 values.
- **Tolerance:** Exact count-total rule; whole-percent rounding tolerance is ±0.5 percentage point. The n=44 discrepancies range from 3.2 to 8.5 points, exceeding tolerance.
- **Direct observation vs inference:** Directly observed are the printed headers, counts, and percentages. A denominator near 40 is diagnostic only; no intended replacement denominator or rounding rule is established.
- **Source-grounded alternatives:** The total and/or one group header may be a transcription error; rows may use a different unstated available-case denominator; or the displayed table may combine mismatched versions of preliminary data. The surrounding text separately says 89 enrolled and 74 primary-outcome data, neither resolves the table header conflict.
- **Quality-control relevance:** This preliminary baseline table can be reused as a numeric description of the original SSSP study; incompatible denominators prevent reliable interpretation of its baseline frequencies.
- **Human question:** What are the intended total, SSSP, and control denominators for Table 2, and were the displayed control percentages calculated with n=40, n=44, or another population?

## C007 — Printed 28-day usual-care mortality percentage does not round from the displayed follow-up and total-death counts

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-001, `jama_andrews_2017_oi_170091.pdf#page=5`, Clinical Outcomes (97 patients per group; 67.0% versus 45.3% 28-day mortality); comparator DOC-001, `jama_andrews_2017_oi_170091.pdf#page=4`, Figure 1 (97 per group in 28-day analysis); and DOC-003, `joi170091supp2_prod.pdf#page=5`, eMethods (109/194 28-day deaths).
- **Printed inputs/comparator:** With 97 participants per group, printed protocol mortality 67.0% corresponds to **65/97** exactly. The DOC-003 total is **109/194** deaths, leaving **44/97** usual-care deaths. The p.5 usual-care percentage is printed as **45.3%**.
- **Rule and calculation:** 44/97×100=**45.36%**, which rounds to **45.4%** at one decimal, not 45.3%. The same counts give a 67.01% protocol risk and a 21.65-point difference, compatible with the printed 67.0% and 21.6% after ordinary display rounding.
- **Tolerance:** One-decimal percentage tolerance ±0.05 percentage point. 45.36% is 0.06 point from 45.3%, outside this tolerance.
- **Direct observation vs inference:** Directly observed are the 97-per-arm status counts, 67.0%/45.3% p.5 display, and 109/194 total from the supplied eMethods. The 65 and 44 arm death counts are inferred uniquely from those printed integers and ordinary percentage rounding; no correction is claimed.
- **Source-grounded alternatives:** The total 109/194 may refer to a different 28-day analysis population despite the matching label; one printed percentage may have been truncated rather than ordinarily rounded; or one count/percentage may be erroneous. The source does not state a nonstandard rounding rule.
- **Quality-control relevance:** The usual-care 28-day mortality proportion is a key secondary outcome and feeds the displayed absolute difference and RR.
- **Human question:** What are the exact arm-specific deaths and rounding convention for the 97-per-arm 28-day analysis, and is 45.3% the intended usual-care display?

## C008 — HIV-negative subgroup risk ratio does not reconcile with its printed deaths and denominators

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Numeric or arithmetic inconsistency.
- **Exact source location:** DOC-001, `jama_andrews_2017_oi_170091.pdf#page=7`, Figure 3, HIV-negative subgroup.
- **Printed inputs/comparator:** Figure 3 prints protocol/usual-care denominators **9/9**, deaths **3 (33.3%)/5 (55.6%)**, and **RR, 0.75 (95% CI, 0.23–2.44)**.
- **Rule and calculation:** The crude risk ratio defined by the displayed numerator/denominator pairs is (3/9)/(5/9)=3/5=**0.60**, not 0.75. Both printed risks are themselves compatible with 3/9 and 5/9 at one decimal.
- **Tolerance:** Two-decimal ratio display tolerance ±0.005; 0.60 differs from 0.75 by 0.15.
- **Direct observation vs inference:** Directly observed are the denominators, deaths, percentages, and RR. The calculation is direct arithmetic. The source does not label this figure's subgroup RRs as adjusted or otherwise standardized.
- **Source-grounded alternatives:** The RR may derive from a non-crude method or an unprinted population/weighting rule; one death count, denominator, or RR may be misprinted; or the figure may have an undisclosed calculation convention. Other Figure 3 subgroup RRs are generally compatible with their displayed risks, but that comparison is contextual rather than a claimed resolution.
- **Quality-control relevance:** The effect measure and its numerical value are directly reported for a prespecified subgroup; a mismatch can affect result extraction and interpretation of direction/magnitude.
- **Human question:** Was the HIV-negative RR calculated from a non-crude method or a different population, and if not, which printed element (3/9, 5/9, or RR 0.75) is intended?

## C009 — Protocol background culture-yield percentage does not round from its printed count and denominator

**Status:** Pending Human Adjudication.

**Discovery provenance:** Numeric review shard A; duplicates merged from statistical pass 1 and cross-source review where applicable.

- **Candidate category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-002, `joi170091supp1_prod.pdf#page=7`, “Blood cultures and antibiotics” background paragraph.
- **Printed inputs/comparator:** The protocol states that, after excluding probable contaminants, “**36 (22.3%) of 161** septic patients had positive aerobic blood cultures.”
- **Rule and calculation:** 36/161×100=**22.36%**, which rounds to **22.4%** at one decimal, not 22.3%.
- **Tolerance:** One-decimal percentage tolerance ±0.05 percentage point; the discrepancy from the exact value is 0.06 point.
- **Direct observation vs inference:** The count, denominator, and percentage are directly printed. The inference is only that ordinary rounding does not reconcile them; no correction is assumed.
- **Source-grounded alternatives:** The percentage may have been truncated; the count or denominator may be rounded/contextual shorthand; or a different unprinted denominator may have been used. The protocol gives no rounding convention or alternative denominator.
- **Quality-control relevance:** Although this is background rather than an SSSP-2 outcome, it is a printed microbiological yield that can be extracted as a rate; the count/percentage pair should identify its denominator unambiguously.
- **Human question:** Was 22.3% intentionally truncated or calculated with a denominator other than 161, and what count/percentage presentation is intended?
