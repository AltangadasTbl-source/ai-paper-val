# Stable Candidate Ledger

All five candidates are Pending Human Adjudication. Independent initial screening produced five distinct included issues from ten findings, consolidating five duplicate checker descriptions. Registration follows the earliest affected main-report location and within-page reading order, then support locations. IDs are permanent. Recheck and audit fields are pending until those fresh stages finish. No count target was used.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN protocol p.19 and addendum p.33 vs REPORT main pp.3-4 and results supplement pp.6,10,13 | reproduced | CONFIRMED | F-XS-004 |
| C002 | protocol_report | P_R | P_R | PLAN addendum pp.32-33 vs REPORT main pp.3,8; REPORT supplement pp.9-10 corroborates | reproduced | CONFIRMED | F-XS-003 |
| C003 | protocol_report | P_R | P_R | PLAN addendum pp.31-32 vs REPORT main pp.3-4,6,8 | reproduced | CONFIRMED | F-XS-002 |
| C004 | statistical_results | S_C | S_C, S_W | REPORT main pp.5-6,8-9 vs REPORT results supplement pp.11,16,18-19; internal REPORT comparisons | reproduced | CONFIRMED | F-NUM-001 |
| C005 | statistical_results | S_W | S_W | REPORT results supplement p.12 title and rows vs same p.12 footnote; REPORT main p.4 and supplement p.11 corroborates | reproduced | CONFIRMED | F-NUM-002 |

## C001 — Planned and reported adherence sensitivity definitions differ

Status: Pending Human Adjudication. Included finding F-XS-004; duplicate checker provenance F-ST1-003. Statistical relationships S127 and sensitivity families S013-S018, S031-S036.
Classification rationale: PLAN specifies the prospective restriction, REPORT defines the applied restriction; the discrepancy is P_R and protocol_report. The original plan corroborates the implemented addendum, rather than creating a separate P_P conflict. Classification ambiguity: No later adherence amendment is supplied.


**Title:** The reported adherent sensitivity population differs from the implemented plan's adherence restriction.

**Locations and roles:** PLAN [original exploratory restriction](../../joi190122supp1_prod.pdf#page=19), [addendum §15g](../../joi190122supp1_prod.pdf#page=33); REPORT [Covariates and Data Analysis](../../jama_de_boer_2019_oi_190122.pdf#page=3), [primary robustness narrative](../../jama_de_boer_2019_oi_190122.pdf#page=4), [eTable1 definition](../../joi190122supp2_prod.pdf#page=6), [eTable5 footnote](../../joi190122supp2_prod.pdf#page=10) and [eTable8 footnote](../../joi190122supp2_prod.pdf#page=13).

**Printed values and comparison logic:** Original plan≥80% adherence is retained and made explicit as “continuous adherence to ≥80%” in addendum §15g. Report defines high adherence as use at least two-thirds of the time, and eTables5/8 specify this self-report on at least4 of6 questionnaires at6months and years1–5, N1032 per intervention. These are different medication-use thresholds and different continuity requirements; ≥2/3 at4/6 assessments does not imply continuous≥80%. A hypothetical participant reporting70% at four assessments would meet the printed report rule but not the printed plan rule; this illustrates logical nonequivalence only, without asserting that such a participant exists in the trial.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.

**Affected result or extracted value:** Primary eGFR adherence sensitivity differences vitaminD0.89 (−0.74,2.52), P=.28 and omega-3 0.42 (−1.22,2.06), P=.61, and the statement that null primary findings remain similar among consistently highly adherent participants. ACR adherence analyses use the same changed restriction.

**Why context does not resolve it:** Both source versions specify the restriction prospectively, and the reported footnotes specify the actual restriction. The numerically distinct thresholds and assessment requirements cannot be resolved as two names for the same population. No supplied amendment changes §15g's adherence criterion; consequently the reported robustness check cannot be identified as the planned ≥80% restriction.

**Supported alternatives:** A later amendment may have adopted the questionnaire-based two-thirds rule; alternatively the reported sensitivity analysis may replace the planned continuous≥80% analysis. The size and results of the latter population are not supplied and are not estimated.

**Human verification steps:** Confirm the operational adherence variable, locate any threshold amendment and compare which participants entered the planned and reported restrictions. Do not infer that the conclusions would differ.

## C002 — Planned and reported primary covariate specifications differ

Status: Pending Human Adjudication. Included finding F-XS-003; duplicate checker provenance F-ST1-002. Statistical relationships S121, S122 and primary contrasts S003, S006.
Classification rationale: The primary formula in PLAN conflicts with the applied model in REPORT; P_R takes precedence and the domain is protocol_report. Sensitivity footnotes corroborate the applied adjustment and do not constitute an independent S_C conflict. Classification ambiguity: A later covariate amendment or conditional adjustment trigger is not supplied.


**Title:** Routine primary-model covariates in the report are absent from the implemented primary hypothesis model.

**Locations and roles:** PLAN [addendum §15e Equation2](../../joi190122supp1_prod.pdf#page=32); REPORT [Data Analysis](../../jama_de_boer_2019_oi_190122.pdf#page=3), [Table2 footnote a](../../jama_de_boer_2019_oi_190122.pdf#page=8); REPORT [eTables4–5](../../joi190122supp2_prod.pdf#page=9) and [adherent eGFR analysis](../../joi190122supp2_prod.pdf#page=10) corroborate the reported adjustment.

**Printed values and comparison logic:** The addendum primary Equation2 includes intercept, treatment, categorical time, treatment×time, participant random effect and residual. Additional baseline-characteristic terms are described as sensitivity analyses conditional on imbalance. Report p3 instead includes linear age, sex, age×time and sex×time in the primary models; eGFR additionally includes baselineACR and ACR×time. Table2 states its primary estimates derive from adjustment for age, sex and baselineACR. These are explicitly routine primary terms rather than the addendum's conditional sensitivity additions. The same difference applies to both primary intervention contrasts.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.

**Affected result or extracted value:** The model specification producing primary five-year eGFR differences0.9 (−0.7,2.5), P=.25 for vitamin D and0.9 (−0.7,2.6), P=.27 for omega-3.

**Why context does not resolve it:** The source supplies a concrete primary equation and separately assigns additional baseline adjustment to sensitivity analyses. The report supplies a concrete expanded primary model. No supplied addendum or immediate report context states that routine primary covariate adjustment replaced the printed primary hypothesis equation. Random-intercept and categorical-time agreement does not make the adjustment specifications equivalent.

**Supported alternatives:** The report may implement a later expanded primary specification, or may present a covariate-adjusted sensitivity specification as its primary analysis. The package does not identify an additional covariate amendment. No numerical effect of the added terms is assumed.

**Human verification steps:** Compare the implemented primary model formula and analysis code with Equation2; identify any prospective covariate amendment and establish whether the reported tuples were designated primary or sensitivity results.

## C003 — Planned and reported primary population definitions differ

Status: Pending Human Adjudication. Included finding F-XS-002; duplicate checker provenance F-ST1-001. Statistical relationships S119, S120 and primary contrasts S003, S006.
Classification rationale: The implemented PLAN eligibility rule and REPORT all-randomized rule are the conflicting comparators, requiring P_R and protocol_report. Retention counts corroborate the reported population; blood/urine overlap does not establish an exact planned population size. Classification ambiguity: The planned any-biosample population size and any later amendment are unavailable.


**Title:** The implemented plan and report use different primary analysis populations.

**Locations and roles:** PLAN [addendum §15c](../../joi190122supp1_prod.pdf#page=32) and [addendum implementation cover](../../joi190122supp1_prod.pdf#page=31); REPORT [Data Analysis](../../jama_de_boer_2019_oi_190122.pdf#page=3), [retention and primary results](../../jama_de_boer_2019_oi_190122.pdf#page=4), [Figure1](../../jama_de_boer_2019_oi_190122.pdf#page=6), [Table2](../../jama_de_boer_2019_oi_190122.pdf#page=8).

**Printed values and comparison logic:** Addendum §15c defines intent-to-treat inclusion as “all participants who return at least one follow-up biosample.” Report p3 says all randomized participants are analyzed “regardless of adherence or follow-up (full analytic population).” Figure1 confirms370+333+289+320=1312 included in the primary analysis, despite only303+280+242+265=1090 returning at least one follow-up blood sample. Report p4 gives1091 with at least one follow-up urine sample. Even the maximum blood/urine union allowed by these marginal counts is1312, so the actual union size is not supplied; the definitions nevertheless differ explicitly, and eGFR blood-specific retention leaves222 without a follow-up blood measurement. The finding rests on the conflicting inclusion rules and confirmed full randomized analysis, not on assuming blood/urine overlap or an exact plan-eligible union count.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.

**Affected result or extracted value:** The population underlying both imputed five-year primary eGFR differences0.9 mL/min/1.73m² and their CIs, including the analysis-population size extracted as1312.

**Why context does not resolve it:** Both documents use intent-to-treat language, but the implemented plan defines inclusion by naming follow-up biosample return while the report expressly includes everyone irrespective of follow-up. The plan does not say 'only', so it may specify a minimum inclusion guarantee rather than an exhaustive eligibility condition. Immediate context does not determine which reading connects the descriptions. The reproduced issue concerns definition correspondence, not a proven difference in included participants or effects.

**Supported alternatives:** A minimum-inclusion-guarantee reading of §15c could allow the reported all-randomized imputation analysis without changing its promised inclusion. An exhaustive population-definition reading would require a linkage to the broader report rule, possibly through an unsupplied later amendment. Exact overlap between blood and urine returners, the operational planned eligibility rule and any actual difference in participants are unestablished; the 222 without follow-up blood are not proven exclusions under the any-biosample statement.

**Human verification steps:** Establish the operational population prescribed by §15c, determine the eligible biosample union, and identify any later amendment covering participants with no follow-up outcomes.

## C004 — Forest participant counts do not align with treatment summaries

Status: Pending Human Adjudication. Included finding F-NUM-001; duplicate checker provenance F-XS-001. Numeric relationships N002, N017, N021, N024, N026, N027, N068, N076, N077; statistical graphical result families retained in the complete inventory.
Classification rationale: Internal REPORT comparisons establish S_W and the repeated main-versus-results-supplement pattern establishes S_C. Precedence selects S_C over S_W; all relationships are S_C, S_W. The issue concerns participant counts paired with numerical summaries, so statistical_results applies. No PLAN comparator exists. Classification ambiguity: The source does not define which display component carries the alignment change; no primary effect reversal is inferred.


**Title:** Assignment counts and group mean summaries do not align in the primary-outcome subgroup displays, repeated in the ACR displays.

**Relationships:** N002, N017, N021, N024, N026, N027, N068, N076, N077.

**Exact compared locations and roles:** REPORT [main article Figure 1, PDF p.6](../../jama_de_boer_2019_oi_190122.pdf#page=6), REPORT [main Table 1, PDF p.5](../../jama_de_boer_2019_oi_190122.pdf#page=5), REPORT [main Table 2 and Figure 3, PDF p.8](../../jama_de_boer_2019_oi_190122.pdf#page=8), REPORT [main Figure 4, PDF p.9](../../jama_de_boer_2019_oi_190122.pdf#page=9), REPORT [supplement eTable 6, PDF p.11](../../joi190122supp2_prod.pdf#page=11), REPORT [supplement eFigure 2, PDF p.18](../../joi190122supp2_prod.pdf#page=18), REPORT [supplement eFigure 3, PDF p.19](../../joi190122supp2_prod.pdf#page=19). All figure rows are listed below, including repeated subgroup occurrences.

**Printed inputs, rule and calculation:** Figure 1 assigns 370 to D+O,333 to D+placebo,289 to placebo+O,320 to both placebos. Thus D active=703, D placebo=609, O active=659,O placebo=653. Figure 3, however, prints overall Placebo 703,mean−13.1(SD14.4); Vitamin D609,mean−12.3(SD14.8). Figure 4 prints overall Placebo 659,mean−13.1(SD14.8); Omega 3 653,mean−12.2(SD14.5). Table 2 on the same main PDF p.8 has active D change−12.3 and placebo−13.1, active O−12.2 and placebo−13.1. The means therefore follow their displayed treatment labels while the N values do not follow the source-defined assignment counts. This is more than a group-name variation: taking each displayed N,mean,SD triplet literally pairs primary-outcome summaries with the opposite assignment-size information. Exact integers have no display-precision tolerance.

Table 1 also identifies D active white 240+211=451 and D placebo white 199+207=406;Figure 3 puts 451 under Placebo and 406 underVitamin D. D active black 73+75=148 versus D placebo 59+71=130; Figure 3 again puts 148/130 under Placebo/Vitamin D. D<20 counts 62+48=110 active,41+44=85 placebo;20–<30 is 230 active/203 placebo;≥30 is 332 active/297 placebo;all printed with opposite N headings. Figure 3 other-assignment rows put D+O-placebo 333 under Placebo and both placebos 320 underVitamin D;O active row 370 under Placebo and 289 underVitamin D. Figure 4's other-assignment row has O active,D placebo 289 under Placebo and both placebos 320 under Omega 3;D active row 370 under Placebo and 333 under Omega 3.

Supplement eFigure 2 overall N703 under Placebo and 609 under Active intervention accompany geometric change 3.02 and 2.97, respectively. eTable 6 assigns 3.02 to D placebo and 2.97 to D active. eFigure 3 overall N659 under Placebo and 653 under Active accompany 3.05 and 2.94; eTable 6 assigns 3.05 to O placebo and 2.94 to O active. This repeats the count-to-summary alignment pattern without changing the modeled ratio identity.

**Every affected display row:** Pair order below is literal displayed Placebo N / Active N. The D table applies to both main Figure 3 and supplement eFigure 2; the O table applies to both main Figure 4 and supplement eFigure 3. These are affected locations of one consolidated pattern, not independent findings. No raw-data claim is made about unprinted adjusted subgroup values.

| Vitamin D display row | Printed N pair | Omega-3 display row | Printed N pair |
|---|---|---|---|
| Overall |703/609|Overall|659/653|
| White |451/406|EPA/DHA≤2.2|332/347|
| Black |148/130|EPA/DHA>2.2|308/292|
| ACR<30 |635/559|ACR<30|596/598|
| ACR≥30 |67/50|ACR≥30|62/55|
| D<20 |110/85|hsCRP≤.2|334/335|
| D20–<30 |230/203|hsCRP>.2|323/316|
| D≥30 |332/297|fish<1.5|354/329|
| eGFR≥60 |612/531|fish≥1.5|295/310|
| eGFR<60 |89/76|D placebo|289/320|
| BMI<25 |87/87|D active|370/333|
| BMI25–<30 |228/205|Not applicable|—|
| BMI≥30 |364/294|Not applicable|—|
| O placebo |333/320|Not applicable|—|
| O active |370/289|Not applicable|—|

**Focus area:** A (counts and denominators), with population-to-result attribution relevant to extraction.

**Proposed review domain:** statistical_results. Proposed relationship set S_C,S_W; internal main comparisons alone reproduce the primary-outcome alignment issue, while results supplement repeats it with internally matching mean comparators. No PLAN source is involved.

**Affected result or extracted value:** Group N attached to the five-year primary eGFR mean(SD) change in Figures 3/4, including overall and subgroup triplets; repeated group N attached to the five-year ACR geometric-change(SD) triplets. A data extractor using displayed N alongside group SD obtains a different pairing than the randomized-arm population. This qualifies through primary-outcome analysis-size extraction, rather than merely a peripheral label comparison. The overall adjusted primary difference 0.9 and reported P values are not shown to change by this comparison.

**Why context does not resolve it:** Within each figure the N/mean/SD columns are presented as belonging to one group. Neither caption discloses a different count population or independent ordering of N versus mean/SD. Swapping whole group headings would conflict with Table 2/eTable 6 means; retaining all printed cells would conflict with Figure 1 and Table 1 counts. The supplied text supports an N-column alignment explanation, but does not explicitly state which subgroup counts, dispersions or triplets should be used together. The uncertainty affects extraction of primary-outcome N with SD and extends across repeated rows, not just a missing character. Independent screening should specifically assess whether a field reader nevertheless resolves this pattern at once.

**Alternatives and missing definition:** One interpretation is that the N columns follow active/placebo order while mean columns follow placebo/active order. Another is that N denotes an undisclosed differently assigned population; no figure caption defines such a population. The second interpretation does not naturally reconcile overall counts or the known four-arm stratification. The display alone does not establish a complete alternative cell mapping.

**Exact human question:** Which treatment-group and subgroup participant counts belong with each displayed five-year eGFR mean(SD) change in Figures 3/4, and does the same count-to-summary mapping apply to eFigures 2/3?

## C005 — Complete-case ACR sample-size constructions do not reconcile

Status: Pending Human Adjudication. Included finding F-NUM-002; duplicate checker provenance F-XS-005. Numeric relationship N069; statistical sensitivity families S025-S030 and S124.
Classification rationale: Both conflicting constructions are within one REPORT supplement, giving S_W and statistical_results. The main narrative and neighboring table merely corroborate availability; neither creates S_C. Classification ambiguity: Any additional eligibility or specimen-usability exclusions connecting the constructions are unreported.


**Title:** Complete-case ACR analysis has conflicting population totals within eTable 7.

**Relationship:** N069.

**Exact compared locations and roles:** REPORT [supplement eTable 7 heading, baseline/year 5 N columns and asterisk footnote, physical PDF p.12](../../joi190122supp2_prod.pdf#page=12). REPORT [main retention text, physical PDF p.4](../../jama_de_boer_2019_oi_190122.pdf#page=4) and REPORT [supplement eTable 6 year 5 counts, physical PDF p.11](../../joi190122supp2_prod.pdf#page=11) corroborate urine availability but are not needed to reproduce the internal table discrepancy.

**Printed inputs:** Heading: “Participants With Available Baseline and Year 5 Measurements (N = 944*)”. Both baseline and year 5 rows give D active 504,placebo 440 and O active 477,placebo 467. Asterisk footnote:1312 enrolled;1311 baseline urine samples;991 of these also donated year 5 and “were included in this analysis”;320 baseline but not year 5 excluded;1 missing baseline excluded. Main text has 945 final urine samples; eTable 6 final counts 505+440=945 and 478+467=945.

**Rule and calculation:** The two marginal partitions must each sum to the same total complete-case analysis size. 504+440=944 and 477+467=944 match the heading. In the footnote,1311−320=991, and 1312−320−1=991. Thus the footnote's included count is 47 greater than the heading/table total. If 944 is the final included population,1311−944=367 baseline-sample participants are outside it, rather than 320. Exact counts cannot reconcile through rounding. Even allowing hypothetical half-unit intervals,944 has[943.5,944.5] and 991 has[990.5,991.5], which do not overlap. This interval diagnostic is unnecessary for exact integer N but confirms display precision cannot bridge 47 participants.

**Focus area:** A.

**Proposed review domain:** statistical_results. Relationship S_W (within one results supplement); main availability text is corroboration, not an independent conflicting-source relationship.

**Affected result or extracted value:** Analysis-population size and inclusion/exclusion counts for the baseline/year 5 complete-case ACR sensitivity results: vitamin D ratio 1.03(95%CI.86,1.22),P.77;omega 3 ratio.93(.78,1.11),P.44. Population size 944 versus 991 could be extracted from the same table. No change in reported treatment-effect conclusion is established.

**Why context does not resolve it:** The asterisk directly connects heading N 944 to a footnote explicitly saying 991 were included in this analysis. Immediate context supports 944 through both arm partitions, but also offers a fully self-consistent 991 included/320 excluded account. It does not explain 47 additional exclusions or distinguish returned specimens from available measurements in a way reconciling the explicit analysis inclusion claim. Choosing a population definition or treating footnote counts as a separate subset requires an unstated explanation. This is an analysis-population-size comparison, not merely a per-time-point count difference.

**Alternatives and missing definition:** The footnote may describe returned samples rather than usable measurements, leaving 47 unusable paired samples unreported; alternatively, its 991 and 320 may describe a different participant set. Neither explanation is provided, and the explicit included-in-analysis wording does not name a separate set. The heading/arm totals support 944 as one possible intended N without explaining the competing complete accounting.

**Exact human question:** Does eTable 7's complete-case ACR analysis include 944 or 991 participants, and what eligibility or measurement-availability accounting connects its baseline/year 5 arm counts to its stated included and excluded totals?


## Mechanical evidence-state update

The fresh evidence rechecker reproduced C001, C002, C003, C004 and C005 and confirmed every document role, primary relationship, all-relationship set and review domain. Its complete fact records in verification/evidence_recheck.md are controlling recheck evidence. C004 has 52 visually transcribed row occurrences; 22 have independently reconstructable arm or stratum count comparators and 30 are retained repeated-pattern occurrences without independent arm-stratum totals. C003 is a reproduced specification comparison: the plan does not say 'only', so a minimum-inclusion-guarantee reading remains a source-grounded alternative and no exact planned biosample union size is established. The ledger does not infer numerical effect changes. Inclusion-audit fields await the fresh quality-control audit.

## Final quality-control audit and source-location additions

The fresh audit confirmed the inclusion of C001, C002, C003, C004 and C005 and their evidence/classification fields. All remain Pending Human Adjudication. No screening decision changed and no candidate was added or deleted.

For C002, retain separate exact links for PLAN [addendum continuation, PDF p.33](../../joi190122supp1_prod.pdf#page=33) and REPORT [eTable4, PDF p.9](../../joi190122supp2_prod.pdf#page=9) and [eTable5, PDF p.10](../../joi190122supp2_prod.pdf#page=10). These supplement the registered primary comparator locations without changing relationships.

For C003, the plan includes all participants returning at least one follow-up biosample but does not say 'only'. The definition correspondence is unresolved; the supplied evidence does not establish an actual difference in included participants or an exact planned population size. A minimum-inclusion-guarantee reading could allow the reported broader imputation population. The alternative is an exhaustive population definition later changed in an unsupplied amendment. Preserve both interpretations and the unknown blood/urine union; do not describe the 222 participants without follow-up blood as proven exclusions under the any-biosample plan.

For C004, retain REPORT [eTable11 treatment-size headings, PDF p.16](../../joi190122supp2_prod.pdf#page=16) as a comparator/corroborating location from duplicate F-XS-001. All52 forest-row occurrences are confirmed as printed;22 have independent arm/stratum count comparators, and30 are pattern occurrences without supplied independent subgroup counts. The latter are retained occurrences, not separately demonstrated count reconstructions. Intended N/mean/SD pairings remain a human question; primary effect reversal is not established.
