# Cross-Source Consistency Check

## Scope and method

This check covers every canonical numeric relationship N001-N031 and statistical relationship S001-S017 in the current inventories. It used the current extraction maps and provisional mapping parts as locators, then compared the exact supplied PDFs. A comparison was called only after matching the trial population, analysis set, time point, arm orientation, model/test, measure, scale/unit, reference group, and printed precision. Planned protocol/SAP quantities were not compared as though they were observed trial results. No legacy candidate, checker, verifier, quality, or report artifact was consulted.

Direct-source links below are relative to this artifact. `DOC-001` is the main article; `DOC-002` is the protocol/update; `DOC-003` is the SAP; `DOC-004` is the eTable/eFigure supplement; `DOC-005` is the data-sharing supplement.

## Candidate proposals requiring human verification

### Proposal A — Randomization age-stratum boundary differs from the final protocol update

**Category:** Cross-document numeric inconsistency.

**Exact linked locations and printed statements:**

- Main article, randomization: [DOC-001 PDF p. 2](<../../../jama_parsons_2020_oi_190140.pdf#page=2>) prints age strata as “`<70 years vs ≥70 years`.”
- Protocol Update 10: [DOC-002 PDF p. 2](<../../../joi190140supp1_prod.pdf#page=2>) explicitly states that the age-stratification factor “was corrected from `< 70 years vs. ≥ 70 years` to `≤ 70 years vs. > 70 years`,” to match the schema.
- Final-protocol schema: [DOC-002 PDF p. 5](<../../../joi190140supp1_prod.pdf#page=5>) prints “Age: Men `≤70 years`; Men `>70 years`.”
- SAP randomization definition: [DOC-003 PDF p. 2](<../../../joi190140supp2_prod.pdf#page=2>) prints age “`≤ 70; > 70 years`.”

**Comparison logic:** These are the same randomized-trial stratification variable, at registration, with the same two age groups. The main-article wording places an exactly-70-year-old participant in the older stratum; the final protocol update, final schema, and SAP place that participant in the younger stratum. This is an inequality-boundary identity mismatch, not a rounding difference.

**Supported alternatives:** The protocol update may document an amendment/correction that was not propagated to the article’s methods text; the main wording may instead reflect a historic randomization implementation. The supplied sources do not identify which wording governed the randomization data used for the reported analysis.

**Human verification steps:** Check the randomization-system specification, amendment history, and analysis dataset’s stratum coding for participants aged exactly 70 years. Confirm whether the article should reproduce the corrected `≤70`/`>70` boundary or whether a dated implementation exception applies.

### Proposal B — Eligibility age boundary differs from the final protocol and SAP

**Category:** Measure, label, or scale inconsistency.

**Exact linked locations and printed statements:**

- Main article eligibility: [DOC-001 PDF p. 2](<../../../jama_parsons_2020_oi_190140.pdf#page=2>) permits ISUP grade group 1 in men “younger than 70 years” and grade group 2 or less in those “aged 70 years and older.”
- Final-protocol eligibility/schema: [DOC-002 PDF p. 5](<../../../joi190140supp1_prod.pdf#page=5>) specifies Gleason score `≤6` for men `≤70 years` and `≤(3+4)=7` for men `>70 years`.
- SAP eligibility statement: [DOC-003 PDF p. 1](<../../../joi190140supp2_prod.pdf#page=1>) specifies men `≤70` and men `>70` must have Gleason scores `≤6` and `≤(3+4)=7`, respectively.

**Comparison logic:** These sources describe the same eligibility age/Gleason rule for the trial population. The grade-group/Gleason labels correspond (group 1 = Gleason 6; group 2 or less includes 3+4=7), but the boundary allocates exactly age 70 differently: the article permits grade group 2 at 70, while the final protocol and SAP reserve that allowance for ages above 70. This is a population-definition threshold mismatch with a potential concrete eligibility-classification consequence.

**Supported alternatives:** The article may be describing an earlier protocol version, or the protocol/SAP boundary may have been amended before the final analysis. The supplied package does not provide the eligibility decision record for any participant aged exactly 70 years.

**Human verification steps:** Inspect the dated protocol/amendment history and eligibility source forms for participants aged exactly 70 years. Confirm the operational eligibility rule and whether the main-article wording is an unupdated version-specific description.

### Proposal C — Fourth intervention phase is printed as 16 months in the article and 17 months in the protocol

**Category:** Cross-document numeric inconsistency.

**Exact linked locations and printed values:**

- Main article: [DOC-001 PDF p. 3](<../../../jama_parsons_2020_oi_190140.pdf#page=3>) describes four phases and prints the fourth as “`8 calls over 16 months`.” The preceding phases are 1, 2, and 4 months.
- Final-protocol schema: [DOC-002 PDF p. 5](<../../../joi190140supp1_prod.pdf#page=5>) says the first three phases are completed in 7 months and the fourth is “`8 calls over a 17-month period`.”
- Protocol intervention section: [DOC-002 PDF p. 29](<../../../joi190140supp1_prod.pdf#page=29>) again prints the fourth phase as “`8 calls over a 17-month period`,” following three phases completed in 7 months.

**Comparison logic:** All occurrences concern the same Arm-A counseling schedule: 22 calls in four phases over the stated 24-month intervention. The article’s phase durations sum to 23 months (1+2+4+16), whereas the protocol’s durations sum to 24 months (1+2+4+17). Both preserve eight fourth-phase calls, so the mismatch is the printed maintenance-phase duration, not a count-versus-rate comparison.

**Supported alternatives:** The article may use a different convention for the boundary between phase 3 and phase 4, or may summarize actual delivery rather than the protocol schedule. No supplied source explains a 16-month maintenance phase or identifies it as an intentional implementation deviation.

**Human verification steps:** Check the counseling manual, dated protocol amendments, and participant-contact schedule. Establish whether the intended/reported phase duration was 16 or 17 months and whether phase dates overlap under a documented convention.

### Proposal D — The 12-month narrative calls gram-per-day values “cruciferous servings”

**Category:** Measure, label, or scale inconsistency.

**Exact linked locations and printed values:**

- Main narrative: [DOC-001 PDF p. 5](<../../../jama_parsons_2020_oi_190140.pdf#page=5>) calls the result “cruciferous servings” and prints intervention change `43.10 g/d` (95% CI, `35.21 to 50.99`) versus control `6.44 g/d` (95% CI, `−1.39 to 14.26`).
- Main Table 2: [DOC-001 PDF p. 7](<../../../jama_parsons_2020_oi_190140.pdf#page=7>) labels the matched 12-month row “Cruciferous, `g/d`” and prints the same arm changes; a separate “Cruciferous, `servings/d`” row instead prints `0.71` versus `0.12`.
- eTable: [DOC-004 PDF p. 2](<../../../joi190140supp3_prod.pdf#page=2>) likewise labels `43.10` and `6.44` as the “Cruciferous, `g/d`” row and retains a separate servings/d row.

**Comparison logic:** Population (diet-assessment participants at 12 months), time, intervention-versus-control contrast, linear mixed-model display, values, confidence intervals, and precision match. The numeric values are therefore the gram-per-day result, yet the narrative noun says “servings.” The separate servings/d row demonstrates that this is not a unit conversion or an alternate scale.

**Supported alternatives:** The word “servings” in the narrative may be a wording omission while the attached `g/d` units correctly specify the measure. The supplied sources do not state that `43.10 g/d` was converted to servings before reporting.

**Human verification steps:** Verify the final production text against the authors’ Table 2 source and dietary-analysis output. Confirm whether the narrative should say “cruciferous vegetables” or “cruciferous quantity” in grams per day, and retain the current printed numeric values only if their scale is confirmed.

## Checked matched relationships and noncandidates

The following records document completed cross-source matching. “No cross-document comparator” means the assigned relationship is a source-specific definition, context item, or explicitly no-applicable unit, not that it was omitted.

| ID | Comparison scope and result | Status |
|---|---|---|
| N001 | Main abstract/flow allocation 478, 237/241, 443, and 91 sites matched main narrative and protocol/SAP planned-trial identity; planned 464 was not substituted for observed 478. | Matched / definition-aware noncandidate |
| N002 | Abstract age 64 (7) and PSA 4.9 (2.1) describe all randomized participants; Table 1 has modified-ITT arm data and is not a same-population comparator. | Population-mismatched; noncandidate |
| N003 | Eligibility numeric thresholds otherwise match protocol/SAP; the age/Gleason boundary mismatch is recorded in Proposal B. | Proposal B; remaining items matched |
| N004 | Race and biopsy-time strata match; main `<70`/`≥70` differs from corrected protocol/SAP `≤70`/`>70` (Proposal A). | Proposal A; remaining items matched |
| N005 | 24-month duration, 22 calls, target, and assessment schedule match after distinguishing protocol table formatting; fourth-phase duration is Proposal C. | Proposal C; remaining items matched |
| N006 | PSA `≥10`, PSADT `<3 years`, pathology thresholds, origin, and censoring match the final protocol/SAP when age-specific pathology wording is retained. | Matched |
| N007 | PSADT log(2)/least-squares-log(PSA) formulation and three-value rule match; protocol’s “all available” rule is compatible with the main article’s 9-month-onward clarification. | Matched |
| N008 | Main observed study versus protocol/SAP planning quantities (418, 57 events, 464) were kept distinct; HR 2.1/2.118 is display precision under the same planning orientation. | Definition-aware noncandidate |
| N009 | Main Figure 1 flow is article-specific observed reporting; no same-result support occurrence. | No cross-document comparator |
| N010 | Per-protocol completion figures have no matched support result. | No cross-document comparator |
| N011 | Table 1 variable-specific denominators are not comparable with all-randomized protocol figures. | Population-mismatched; noncandidate |
| N012 | Completion/censoring and biopsy figures are observed article results; protocol/SAP provide definitions only. | Definition-aware noncandidate |
| N013 | Abstract, main narrative, and Figure 2 agree on 245 events, 124/121, KM 43.5%/41.4%, and the distinct TTP measures. | Matched |
| N014 | Active-treatment counts and rates are observed article results; protocol/SAP define planned methods only. | No same-result comparator |
| N015 | Narrative and Table 2/eTable match by arm, time, mixed-model contrast, values, and units except Proposal D. | Proposal D; remaining results matched |
| N016 | Figure 2 risk-set numbers and follow-up values have no duplicate support result. | No cross-document comparator |
| N017 | Main Table 2 and DOC-004 eTable shared row labels, units, and most values match at displayed precision; later statistical passes identified the P-value discrepancies registered as C009-C012 and the deep-yellow control-change discrepancy registered as C013. Vegetable juice is supplement-only. | Matched except registered later statistical discrepancies |
| N018 | DOC-004 eFigure is descriptive with no printed numerical comparator; eTable’s shared values match main Table 2. | Matched / no numeric figure comparator |
| N019 | Abstract, discussion, and conclusion align with the nonsignificant primary TTP result; protocol/SAP planning is not an observed comparator. | Matched |
| N020 | Pilot allocation/table values are a separate pilot population and six-month horizon, not the phase-III trial results. | Population/time-mismatched; noncandidate |
| N021 | Pilot carotenoid values use mmol/L and a separate sample; they are not the main trial’s dietary μg/d or plasma log-μmol/L results. | Scale/population-mismatched; noncandidate |
| N022 | Pilot satisfaction and planned enrollment counts have no matched main-result comparator. | No cross-document comparator |
| N023 | Protocol outcome schedules/units are planning definitions, reconciled with main schedules where same measure/time; no conflicting observed result. | Matched |
| N024 | Biospecimen quantities and time points are support definitions only; no competing observed main result. | No cross-document comparator |
| N025 | QOL scales, direction, and time points are protocol/SAP definitions; no published QOL estimate requires a matched numerical comparison. | No cross-document comparator |
| N026 | Correlative assay/power material is planned/substudy information, not a duplicate observed result. | No cross-document comparator |
| N027 | Interim/recalculation values are protocol planning rules; HR 2.118 and .472 have reverse orientations and are not conflicting observed estimates. | Definition-aware noncandidate |
| N028 | Consent timing and volumes are consent-specific planned information; optional-substudy volumes were not treated as all-participant samples. | Definition-aware noncandidate |
| N029 | SAP ITT/modified-ITT and final local-follow-up-pathology rules distinguish planning/analysis provenance; no printed observed number conflicts with the main 443 primary set. | Definition-aware noncandidate |
| N030 | SAP alpha, multiplicity, missing-data, and transformations are planned definitions; no same-result main numerical comparison exists. | No cross-document comparator |
| N031 | Explicit support no-applicable pages/administrative units contain no matched quantitative result. | No cross-document comparator |
| S001 | Abstract/main/Figure 2 agree: unadjusted HR .96 (.75-1.24) and log-rank P=.76; adjusted HR .97 (.76-1.25), P=.84 remains a distinct model. | Matched |
| S002 | Main biopsy-only HR 1.40 (.79-2.46), P=.24 matches Figure 2B log-rank P=.24 after retaining the sensitivity endpoint. | Matched |
| S003 | Main, protocol, and SAP sample-size plans agree after retaining planning status and reciprocal/reference-arm HR convention. | Matched |
| S004 | Main and SAP both specify KM/log-rank/Cox, stratification adjustment, ITT support, and sensitivity analyses; central/local pathology appendix is not a conflicting numerical result. | Matched / definition-aware noncandidate |
| S005 | Main Table 2 and eTable agree on mixed-model framework, categorical time, interaction, and within- versus between-group P-value semantics. | Matched |
| S006 | Fisher exact P=.75 and time-to-treatment HR 1.38 (.39-4.90), P=.61 are separate measures and have no support duplicate. | No cross-document comparator |
| S007 | Plasma-carotenoid contrast .10 (.02-.18) log-μmol/L, P=.01 has no duplicate support result; dietary μg/d values were not treated as the same measure. | Scale-mismatched; noncandidate |
| S008 | Pilot P values/footnotes are distinct pilot analyses and are not the phase-III Table 2 P values. | Population/model-mismatched; noncandidate |
| S009 | Protocol/SAP PSADT analysis definitions match the main framework after preserving version-specific details and planned-versus-observed status. | Matched |
| S010 | Protocol endpoint/timepoint definitions are planning specifications; no conflicting published secondary result. | No cross-document comparator |
| S011 | Protocol biomarker analysis is planned; the main plasma result is a different realized analysis and no same estimate is printed twice. | Model/result-mismatched; noncandidate |
| S012 | Protocol/SAP planned QOL/diet models are not interchangeable with Table 2’s realized mixed-model dietary results. | Model/status-mismatched; noncandidate |
| S013 | Interim alpha and futility rules are distinct decision rules; P=.5 futility language is not compared to the .0025 efficacy boundary. | Definition-aware noncandidate |
| S014 | Recalculation HR .472 is the reciprocal planning orientation of HR 2.118; it is not an observed effect estimate. | Reference-group/status-matched noncandidate |
| S015 | SAP QOL plans and DOC-004 dietary mixed-model results concern different measures and analyses. | Measure/model-mismatched; noncandidate |
| S016 | SAP scale definitions and eFigure plotting definitions concern different instruments/outputs; eFigure prints no numerical summary statistic. | No numeric comparator |
| S017 | DOC-004 footnotes match DOC-001 Table 2 semantics: `*` is within-group follow-up versus baseline and `†` is change-versus-change. | Matched |

## Limitations

- The supplied package does not include randomization-system records, participant-level age/eligibility decisions, counseling logs, or the production source for the narrative sentence. Those records are needed to resolve the four proposals.
- Protocol and SAP materials include amendments and planning definitions. They were used as comparators only where they identify the same population, time, contrast, and measure; no planning assumption was treated as a conflicting observed result.
- DOC-004 eFigure is graphical and has no printed quartiles, means, or whisker endpoints to reconcile numerically.

## Compact completion record

- **Assigned scope:** N001-N031 and S001-S017; abstract, narrative, tables, Figure 1/2, captions/footnotes, DOC-002 protocol/update/consent, DOC-003 SAP, DOC-004 eTable/eFigure, and DOC-005 data-sharing source.
- **Relationships checked:** 48/48 canonical IDs.
- **Concrete candidate proposals:** 4 distinct proposals (A-D); no stable C IDs and no AI adjudication assigned.
- **Noncandidate/matched records:** 44 ID-level records have an explicit matched, definition-aware, population/scale-mismatched, or no-comparator record above; IDs with a proposal retain their other matched facts.
