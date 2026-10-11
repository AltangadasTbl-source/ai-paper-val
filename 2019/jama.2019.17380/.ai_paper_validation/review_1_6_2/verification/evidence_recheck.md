# Workflow 1.6.2 Mechanical Evidence Recheck

Scope: all 18 stable IDs, C001–C018, including every registered occurrence of the repeated patterns. This is an evidence record. Every ID remains **Pending Human Adjudication**. Source roles were determined from the compared content. No assigned ID was removed.

Final authority: the supplied PDFs at the linked physical pages. Fresh direct Poppler `pdftotext -layout` extraction of the complete main, plan, results-supplement and data-sharing PDFs produced `preprocessing/evidence_recheck/main-full.txt`, `plan-full.txt`, `supp-full.txt` and `sharing-full.txt`. Direct CPU `pdftoppm` rendering produced `plan-32.png`, `main-8.png` and `supp-17.png` in that directory. The exact-source CPU renders `preprocessing/numeric_checker/supp2-18.png` and `supp2-19.png` were independently visually reread; native text on those pages contains captions but omits plotted content. Text and rendered derivatives served as transcription aids for these identified supplied pages. Engines: direct Poppler text/layout and rendering; device: CPU, as recorded in `tooling_record.md`. No OCR, external evidence, source alteration or fallback environment was needed.

For display-precision checks, integer copies receive ±0.5, sums of two displayed integers receive ±1, percentages printed to whole percent receive ±0.5 percentage points, and other numeric inputs receive half their last displayed unit. A positive interval gap divided by the absolute reference value must exceed 0.05. Operational definitions and model-term comparisons are logical checks; their numbers do not become rounded eligibility or analysis rules merely because interval arithmetic is supplied as a conservative supplementary check.

## Classification confirmation

| ID | Compared content roles | Primary relationship | All relationships | Review domain | Evidence state | Classification change |
|---|---|---|---|---|---|---|
| C001 | Original PLAN; amended PLAN; REPORT | P_R | P_R, P_P | protocol_report | reproduced | None; disclosed amendment retained |
| C002 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C003 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C004 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C005 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C006 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C007 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C008 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C009 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C010 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C011 | PLAN; REPORT | P_R | P_R | protocol_report | reproduced | None |
| C012 | Main REPORT; results-supplement REPORT | S_C | S_C, S_W | statistical_results | reproduced | None |
| C013 | Main REPORT; results-supplement REPORT | S_C | S_C, S_W | statistical_results | reproduced | None |
| C014 | PLAN; PLAN | P_P | P_P | plan_material | reproduced | None |
| C015 | PLAN; PLAN | P_P | P_P | plan_material | reproduced | None |
| C016 | Results-supplement REPORT; same REPORT | S_W | S_W | statistical_results | reproduced | None |
| C017 | Results-supplement REPORT; same REPORT | S_W | S_W | statistical_results | reproduced | None |
| C018 | Results-supplement REPORT; same REPORT | S_W | S_W | statistical_results | reproduced | None |

P_R takes precedence over P_P in C001. S_C takes precedence over S_W in C012–C013. Corroborating plan/report content does not add a relationship in C014–C015 or C018. No location or value in the current ledger needed a transcription correction. In particular, C005 already cites reference 145 on physical plan p.30.

## C001 — Documented outcome-hierarchy and composite amendment

**Locations found; source and comparator matched:** Original PLAN [p.11 aims](../../../joi190122supp1_prod.pdf#page=11), [p.17 VI.b–c](../../../joi190122supp1_prod.pdf#page=17), and [p.19 Table 2](../../../joi190122supp1_prod.pdf#page=19) were found. The narrative specifies four-year continuous ACR as primary and eGFR as secondary, whereas Table 2 calls the continuous outcomes co-primary. The original composite includes ACR doubling with final ACR ≥30 mg/g, absolute eGFR loss ≥12 mL/min, ESRD and/or death. Amended PLAN [p.31 dates](../../../joi190122supp1_prod.pdf#page=31) and [p.32 §15b](../../../joi190122supp1_prod.pdf#page=32) explicitly identify submission March 2, 2015 and implementation February 24, 2016, promote five-year eGFR change, retain continuous ACR as secondary, and specify ≥40% eGFR loss/ESRD/death without ACR progression in the composite. REPORT [p.1 primary outcome](../../../jama_de_boer_2019_oi_190122.pdf#page=1), [p.2 Outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=2), [p.3 secondary definitions](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 composite narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4), and [p.9 Table 3](../../../jama_de_boer_2019_oi_190122.pdf#page=9) match the ledger, including HRs 0.92 and 1.11. The report explicitly discloses the primary-outcome revision in 2016.

**Rule applicable and comparison reproduced:** Item-by-item outcome-status, time-window and composite-component comparison reproduces the original-versus-amended changes. The latest supplied plan agrees with the report. Route A category 5 concerns the reproduced prespecified status/component change; this record does not assert an undisclosed latest-plan departure. Display precision cannot reconcile different endpoint status or component definitions; 12 mL/min absolute loss and 40% relative loss are distinct criteria without a universal conversion.

**Inputs available / exact missing inputs:** Both component lists, original narrative hierarchy, dated addendum, reported definitions and amendment disclosure are available. An intervening plan connecting the original four-year narrative/co-primary table to the addendum's account of previous two-year outcomes is absent. Participant baseline eGFR values needed to translate absolute to relative loss are absent and were not assumed.

**Alternative and observation versus explanation:** A prospectively authorized, documented revision is directly supported. Original wording and amended wording differ; whether that history requires any further interpretation is a human decision. An undisclosed departure or a reason for changing endpoints is not inferred.

**Classification:** Confirmed PLAN/PLAN/REPORT, primary P_R, all P_R and P_P, domain protocol_report. Classification ambiguity: the latest plan and report agree, and the revision is disclosed; incomplete intervening history remains contextual. No correction.

**Evidence state:** reproduced. Determining fact: the exact original and amended/reported hierarchy and component lists differ as registered, with the dated amendment retained.

**Remaining human question:** Which hierarchy and composite should be tagged as original versus amended prespecification, and how should the documented 2016 revision be handled in evidence extraction?

## C002 — Age eligibility thresholds differ between plan and report

**Locations found; source and comparator matched:** PLAN [p.4 abstract](../../../joi190122supp1_prod.pdf#page=4), [p.11 aims/population](../../../joi190122supp1_prod.pdf#page=11) and [p.12 Table 1/population](../../../joi190122supp1_prod.pdf#page=12) all give men ≥60 years and women ≥65 years. REPORT [p.2 Study Population](../../../jama_de_boer_2019_oi_190122.pdf#page=2) gives men ≥50 and women ≥55. PLAN [p.31](../../../joi190122supp1_prod.pdf#page=31), [p.32](../../../joi190122supp1_prod.pdf#page=32) and [p.33](../../../joi190122supp1_prod.pdf#page=33) were read; that analytic addendum does not revise eligibility ages.

**Rule applicable and comparison reproduced:** The explicit primary-analysis population eligibility differs. Conservative half-unit intervals [59.5,60.5] versus [49.5,50.5], and [64.5,65.5] versus [54.5,55.5], have gap 9 years; 9/60=0.150 and 9/65=0.13846 exceed 0.05. These are operational thresholds. Route B concerns the eligible population attached to the primary eGFR contrasts, not an estimate of affected participant numbers.

**Inputs available / exact missing inputs:** The sex-specific criteria and actual N=1312 are supplied. A dated parent-trial eligibility amendment and participant-level ages identifying any membership change are absent.

**Alternative and observation versus explanation:** A later parent-trial revision could connect the criteria, but is not supplied. Different printed thresholds are direct observations; changed membership or impact on the treatment estimate is not inferred.

**Classification:** PLAN versus REPORT; P_R only; protocol_report; confirmed without correction. Ambiguity: a later unsupplied eligibility version may exist.

**Evidence state:** reproduced; the exact eligibility limits differ beyond display precision.

**Remaining human question:** Which dated eligibility amendment connects these limits, and which criteria defined the recruited ancillary cohort?

## C003 — Diabetes exclusion criteria use different insulin rules

**Locations found; source and comparator matched:** PLAN [p.12 Table 1 and population narrative](../../../joi190122supp1_prod.pdf#page=12) and [p.14 IV.a enrollment algorithm](../../../joi190122supp1_prod.pdf#page=14) exclude diagnosis before age 30 and initial treatment with insulin. REPORT [p.2 Study Population](../../../jama_de_boer_2019_oi_190122.pdf#page=2) instead specifies diagnosis before age 30 treated with insulin for more than 20 years. Both parts of each conjunction were matched.

**Rule applicable and comparison reproduced:** Initial treatment and accumulated treatment duration are different Boolean criteria for the primary cohort. Initial insulin use with duration ≤20 years can satisfy one and not the other; later insulin initiation with duration >20 years can give the converse. These are logical examples, not claims about observed participants. Display precision does not apply to the changed condition; the shared age threshold agrees. Route B applies to the primary-population definition.

**Inputs available / exact missing inputs:** Both exclusion rules are available. Screening records, individual insulin histories and any prospective revised exclusion specification are absent.

**Alternative and observation versus explanation:** The duration condition may represent a later operational proxy for type 1 diabetes. That explanation is not established by the supplied text; differing printed conjunctions are directly observed.

**Classification:** PLAN versus REPORT; P_R only; protocol_report; confirmed, no role or type correction. Ambiguity: an unsupplied operational revision.

**Evidence state:** reproduced; the insulin criteria are not logically equivalent.

**Remaining human question:** Which insulin criterion was implemented, and where was the revised exclusion specified?

## C004 — Randomization stratifiers differ between plan and report

**Locations found; source and comparator matched:** PLAN [p.14 IV.c Treatment Assignment](../../../joi190122supp1_prod.pdf#page=14) states a computer-generated random-number table, stratification by five-year age group, blocks of eight and two participants per factorial combination. REPORT [p.2 Interventions](../../../jama_de_boer_2019_oi_190122.pdf#page=2) states computer-generated blocks of eight stratified by age, sex and race. PLAN [pp.31–33 analytic addendum](../../../joi190122supp1_prod.pdf#page=31) was fully read, with [p.32](../../../joi190122supp1_prod.pdf#page=32) and [p.33](../../../joi190122supp1_prod.pdf#page=33) containing no allocation-stratum revision.

**Rule applicable and comparison reproduced:** Item-by-item statistical allocation-design comparison gives matching block size and factorial arms, but adds sex/race stratifiers only in the report. No inference about omitted regression adjustment is involved. Display precision does not apply to a stratifier list. Route B concerns the planned/reported randomization specification accompanying the primary randomized contrasts.

**Inputs available / exact missing inputs:** Both explicit design descriptions are available. The final prospective allocation specification and randomization records are absent; no changed cohort count or statistical effect is calculated.

**Alternative and observation versus explanation:** The report may describe later parent-trial procedures. That possible history is not in the supplied addendum. The list difference is direct; its implementation cause remains inferred.

**Classification:** PLAN versus REPORT; P_R only; protocol_report; unchanged. Ambiguity: later parent-trial procedures may resolve the history, but no supplied text establishes them.

**Evidence state:** reproduced; sex/race appear in the reported stratification list and not in the explicit supplied allocation specification.

**Remaining human question:** Which allocation strata were implemented, and which prospective specification added sex and race?

## C005 — Primary eGFR estimator identity differs from the supplied plan

**Locations found; source and comparator matched:** PLAN [p.17 VI.c Equation 1](../../../joi190122supp1_prod.pdf#page=17) prints 177.6 × SCr^(−0.65) × CysC^(−0.57) × age^(−0.20) ×0.82 if female ×1.11 if black. Its reference 145 is physically on [p.30](../../../joi190122supp1_prod.pdf#page=30), Stevens et al., 2008. Amended PLAN [p.32 §15b](../../../joi190122supp1_prod.pdf#page=32) promotes eGFR but does not identify a replacement estimator. REPORT [p.3 Outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=3) identifies the CKD-EPI creatinine/cystatin C equation, citing reference 19 on [p.11](../../../jama_de_boer_2019_oi_190122.pdf#page=11), Inker et al., 2012. REPORT supplement [p.2](../../../joi190122supp2_prod.pdf#page=2), [p.3](../../../joi190122supp2_prod.pdf#page=3) and [p.4](../../../joi190122supp2_prod.pdf#page=4) describe assay QC, cystatin C calibration and harmonization; they do not specify the original-to-reported equation replacement.

**Rule applicable and comparison reproduced:** Estimator identity, not simply shared input analytes, differs between the explicit plan equation/citation and named report equation/citation. Route B concerns the estimator constructing the primary change and decline endpoints. This is a logical identity comparison. Display-precision intervals cannot reconcile different referenced estimator identities. No coefficients from the cited external publications were imported, and no individual eGFR difference was calculated.

**Inputs available / exact missing inputs:** The original formula, both supplied citations, report estimator name and calibration narrative are available. The complete reported formula, individual laboratory/age records, implemented outcome-construction code and a final estimator amendment are absent.

**Alternative and observation versus explanation:** The plan's phrase about the most precise serologic methods available may permit updating, or another amendment may specify it. These possibilities do not identify a dated final estimator in this package. Distinct printed identities are direct; magnitude of any participant-level consequence is unmeasured.

**Classification:** PLAN versus REPORT; P_R only; protocol_report. QC report locations corroborate measurement history, not an additional conflicting relationship. Confirmed; no correction. Ambiguity: possible intended update permission or unsupplied amendment.

**Evidence state:** reproduced; the supplied estimator identities differ. Physical p.30 already matches the current ledger, so no transcription-correction state is needed.

**Remaining human question:** Which final plan specified the reported CKD-EPI equation, and which equation generated every baseline and follow-up outcome value?

## C006 — Standalone categorical ACR analysis is called prespecified

**Locations found; source and comparator matched:** PLAN [p.17 original composite](../../../joi190122supp1_prod.pdf#page=17), [p.32 §15b/e](../../../joi190122supp1_prod.pdf#page=32), and [p.33 categorical-model continuation](../../../joi190122supp1_prod.pdf#page=33) were matched. They provide an original composite ACR-progression component, revised continuous log-ACR analysis and revised eGFR-based categorical endpoints. REPORT [p.3 Outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=3) calls ACR change prespecified as both continuous and standalone time to doubling with final ACR ≥30 mg/g; [p.4 secondary narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4) and [p.9 Table 3 and footnote a](../../../jama_de_boer_2019_oi_190122.pdf#page=9) match the registered analysis. The standalone HRs are 1.34 (1.00–1.80), P=.05, and 1.08 (0.81–1.44), P=.60.

**Rule applicable and comparison reproduced:** Match endpoint, standalone-versus-composite status and model. An original composite component is not an explicit standalone amended five-year Cox analysis. Full fresh plan text and the detailed endpoint/model sections do not supply that standalone prespecification. Route A category 5 applies to the printed prespecified claim versus supplied plan contents. Display precision is inapplicable to analysis status; this candidate does not infer a separate CI/P conflict from rounded boundary values.

**Inputs available / exact missing inputs:** Original/revised endpoint lists, revised log-continuous model, report prespecified statement and standalone Cox results are supplied. A prospective standalone categorical ACR specification or documented addition is absent.

**Alternative and observation versus explanation:** The authors may intend a separate analysis of an original component or refer to an unsupplied final plan. The report's claim and the supplied plan's scope are direct observations; prespecification outside the package is not asserted absent everywhere.

**Classification:** PLAN versus REPORT; P_R only; protocol_report; confirmed without correction. Ambiguity: possible additional prospective material.

**Evidence state:** reproduced; the cited standalone prespecified analysis is not specified by the supplied original/amended endpoint-model sections.

**Remaining human question:** Where was standalone time to ACR doubling with final ACR ≥30 mg/g prespecified, and how was it classified relative to revised continuous ACR?

## C007 — Adherence sensitivity populations use different criteria

**Locations found; source and comparator matched:** PLAN [p.19 VI.g](../../../joi190122supp1_prod.pdf#page=19) specifies ≥80% medication adherence; amended PLAN [p.33 §15g](../../../joi190122supp1_prod.pdf#page=33) specifies continuous adherence to ≥80%. REPORT [p.3 Covariates/Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3) specifies at least two-thirds, and [p.4 sensitivity narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4) points to the adherent analyses. REPORT supplement [p.6 eTable 1 footnote](../../../joi190122supp2_prod.pdf#page=6), [p.10 eTable 5 definition](../../../joi190122supp2_prod.pdf#page=10), and [p.13 eTable 8 definition](../../../joi190122supp2_prod.pdf#page=13) all give ≥2/3 on ≥4 of six questionnaires through year 5, N=1032 per intervention. eTable 5 primary eGFR contrasts 0.89 (−0.74,2.52) and 0.42 (−1.22,2.06), and eTable 8's parallel ACR analyses were matched.

**Rule applicable and comparison reproduced:** Both consumption threshold and continuity rule differ for the same sensitivity analysis. Two-thirds is exact 66.6667%; allowing printed 80% its interval [79.5,80.5]% leaves gap 12.8333 percentage points, relative 12.8333/80=0.16042. Qualifying on four of six questionnaires does not require continuous qualifying use. Route B concerns the defined sensitivity population for the primary effects, rather than per-visit adherence copies.

**Inputs available / exact missing inputs:** Both rules, report N and sensitivity contrasts are available. Individual questionnaire histories, a ≥80%-continuous subset count/result and an amendment connecting rules are absent.

**Alternative and observation versus explanation:** A later questionnaire-based operational rule could explain the report. Different thresholds and continuity requirements are direct; changed subset membership count or impact on estimates is not inferred.

**Classification:** PLAN versus REPORT, including report locations in both main and results supplement; P_R only; protocol_report. The report locations consistently describe the same criterion and do not add S_C. Confirmed, no correction. Ambiguity: possible unsupplied revision.

**Evidence state:** reproduced; the explicit planned and reported sensitivity-set definitions differ beyond precision.

**Remaining human question:** Which adherence rule governed the intended sensitivity analysis, and were results for continuously ≥80% adherent participants generated?

## C008 — Primary analysis population drops the planned follow-up condition

**Locations found; source and comparator matched:** PLAN [p.32 §15c](../../../joi190122supp1_prod.pdf#page=32) includes participants returning at least one follow-up biosample regardless of adherence or other postrandomization characteristics. REPORT [p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3) explicitly includes all randomized participants regardless of adherence or follow-up. [p.4 Retention](../../../jama_de_boer_2019_oi_190122.pdf#page=4) gives 1090 with ≥1 follow-up blood sample and 1091 with ≥1 urine sample; [p.6 Figure 1](../../../jama_de_boer_2019_oi_190122.pdf#page=6) has primary analysis boxes 370/333/289/320; [p.8 Table 2 footnotes](../../../jama_de_boer_2019_oi_190122.pdf#page=8) identifies multiple-imputation primary changes over all participants.

**Rule applicable and comparison reproduced:** Planned conditional inclusion versus reported unconditional randomized inclusion differs directly. Primary box counts sum to 1312. This is Route A category 5 replacement of a planned primary-population rule. The blood shortfall is 222, but neither 1090 nor 1091 is the union of blood/urine responders. Display precision is inapplicable to the population condition; no numeric planned population is manufactured. In particular, aggregate counts allow a blood/urine union between 1091 and 1312, so they alone do not prove the exact number failing the general biosample condition.

**Inputs available / exact missing inputs:** Both explicit rules, randomized total and specimen-specific totals are supplied. Participant-level blood/urine return linkage, the exact union, any general-biosample operational definition and an amended all-randomized rule are absent.

**Alternative and observation versus explanation:** The condition may have been formally removed in unsupplied material, or a broad biosample union may determine membership differently from blood-only inclusion. The text-rule difference is direct; an exact excluded planned count or estimate effect is not inferred.

**Classification:** PLAN versus REPORT; P_R only; protocol_report; confirmed without correction. Ambiguity: missing final population amendment and union definition.

**Evidence state:** reproduced; the printed analysis inclusion conditions differ independently of the unreported union count.

**Remaining human question:** Was the follow-up requirement formally removed, and what participants and biosample-return definition governed the planned and reported imputation populations?

## C009 — Primary imputation count differs between plan and report

**Locations found; source and comparator matched:** PLAN [p.32 §15c](../../../joi190122supp1_prod.pdf#page=32) combines results from ten chained-equations imputation datasets using Rubin rules. REPORT [p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3) gives M=20 and Rubin pooling; [p.8 Table 2 footnotes](../../../jama_de_boer_2019_oi_190122.pdf#page=8) associates imputation with primary results.

**Rule applicable and comparison reproduced:** The primary missing-data setting is 10 versus 20. Half-unit intervals [9.5,10.5] and [19.5,20.5] have gap 9, relative 9/10=0.90 against plan and 9/20=0.45 against report. Both exceed 0.05. Route B concerns extraction of the primary imputation specification. No claim about a quantified SE or conclusion effect follows.

**Inputs available / exact missing inputs:** The two dataset counts, pooling method and matched primary analysis are supplied. Implemented imputation code, Monte Carlo diagnostics and a prospective count revision are absent.

**Alternative and observation versus explanation:** Twenty datasets could be an intentional computational update. The two printed settings are direct; reason and effect of updating are unmeasured.

**Classification:** PLAN versus REPORT; P_R only; protocol_report; confirmed, no correction. Ambiguity: possible subsequent specification.

**Evidence state:** reproduced; the primary imputation counts differ beyond display precision.

**Remaining human question:** Which final imputation specification governed the primary results, and when was the count revised from ten to twenty?

## C010 — Reported primary covariates differ from the planned primary model

**Locations found; source and comparator matched:** PLAN [p.32 §15e Equation 2 and conditional sensitivity clause](../../../joi190122supp1_prod.pdf#page=32), continued on [p.33](../../../joi190122supp1_prod.pdf#page=33), has treatment, categorical time, treatment×time and participant random intercept; baseline-characteristic terms are introduced conditionally as sensitivity analyses for imbalance. REPORT [p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3) explicitly includes age, sex, their time interactions and, for eGFR, baseline ACR and its time interaction. [p.8 Table 2 footnote a](../../../jama_de_boer_2019_oi_190122.pdf#page=8) confirms the primary adjusted model. REPORT supplement [p.9 eTable 4](../../../joi190122supp2_prod.pdf#page=9) and [p.10 eTable 5](../../../joi190122supp2_prod.pdf#page=10) likewise give adjusted sensitivity results, rather than an explicitly identified counterpart to unadjusted planned Equation 2.

**Rule applicable and comparison reproduced:** Term-by-term and analysis-role comparison reproduces fixed-covariate/time-interaction additions to the primary model. The conditional sensitivity allowance does not state that the listed covariates replace the primary equation. Route A category 5 concerns the planned primary model versus reported primary model. Display precision is inapplicable to term lists; no preference for either model is expressed.

**Inputs available / exact missing inputs:** Both primary specifications, conditional adjustment clause and labeled primary result table are supplied. Fitted code, evidence of the specified imbalance condition, a final primary-model revision and the planned-model primary contrast are absent.

**Alternative and observation versus explanation:** A later model amendment or elevation of an imbalance sensitivity could explain the reported primary model. Explicit term/role differences are direct; which process produced them remains inferred.

**Classification:** PLAN versus REPORT; P_R only; protocol_report; confirmed without correction. Consistent report adjustment in both documents is corroboration, not S_C. Ambiguity: later authorization or sensitivity-role change.

**Evidence state:** reproduced; the printed planned primary equation and reported primary fixed-effect terms differ.

**Remaining human question:** Were Equation 2 primary results produced, and what final plan authorized the reported covariate-adjusted model as primary?

## C011 — Planned bioavailable vitamin-D subgroup result is absent

**Locations found; source and comparator matched:** PLAN [p.33 §15f](../../../joi190122supp1_prod.pdf#page=33) explicitly lists baseline total and bioavailable serum 25(OH)D as separate primary eGFR subgroup dimensions. REPORT [p.3 subgroup methods](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.8 Figure 3](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [p.9 interpretation](../../../jama_de_boer_2019_oi_190122.pdf#page=9), [p.10 interpretation/disclosure](../../../jama_de_boer_2019_oi_190122.pdf#page=10), and REPORT supplement [p.18 eFigure 2](../../../joi190122supp2_prod.pdf#page=18) were read. Figure 3 and eFigure 2 contain one 25(OH)D partition, <20/20–<30/≥30 ng/mL, and no separate bioavailable-defined subgroup. Direct full-text search of both complete report PDFs finds the main p.10 bioavailable occurrence only in a patent disclosure. Supplement [p.17 eFigure 1](../../../joi190122supp2_prod.pdf#page=17), visually read, explicitly uses change in total 25(OH)D and is not the missing subgroup result. All supplied report result tables/figure inventories contain no bioavailable-defined primary analysis result.

**Rule applicable and comparison reproduced:** Compare every planned subgroup dimension with the reported primary subgroup inventory. The plan explicitly separates total and bioavailable measures, and the supplied report provides only one concentration partition. The additional REPORT [data-sharing statement p.1](../../../joi190122supp3_prod.pdf#page=1) contains access information and no analysis result. Route A category 5 applies to an unreported planned primary-outcome analysis, not to a generic unreported detail. Display precision is inapplicable to the omitted dimension.

**Inputs available / exact missing inputs:** The explicit planned dimension and complete supplied report inventory are available. Bioavailable assay values, subgroup cut points/results, fitted analysis output or a prospective removal are absent.

**Alternative and observation versus explanation:** The analysis may have been unavailable, discontinued or reported outside the package. No source supplies that explanation. Presence in the plan and absence from the supplied reported result inventory are direct; absence from all possible publications is not asserted.

**Classification:** PLAN versus REPORT; P_R only; protocol_report; unchanged. Ambiguity: unavailable assay or unsupplied amendment is possible but undocumented.

**Evidence state:** reproduced; no counterpart to the explicit bioavailable-defined planned primary subgroup is reported in the supplied documents.

**Remaining human question:** Was the prespecified bioavailable 25(OH)D subgroup analysis performed, and where are its result or documented removal?

## C012 — Forest figures associate counts with opposite treatment columns

**Locations found; source and comparator matched:** REPORT [main p.8 Figure 3 and Table 2](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [main p.9 Figure 4](../../../jama_de_boer_2019_oi_190122.pdf#page=9), [supplement p.18 eFigure 2](../../../joi190122supp2_prod.pdf#page=18), and [supplement p.19 eFigure 3](../../../joi190122supp2_prod.pdf#page=19) were read in full, including all count columns and headers. Comparators were REPORT [main p.1 allocation](../../../jama_de_boer_2019_oi_190122.pdf#page=1), [p.5 Table 1](../../../jama_de_boer_2019_oi_190122.pdf#page=5), [p.6 Figure 1](../../../jama_de_boer_2019_oi_190122.pdf#page=6), [supplement p.11 eTable 6](../../../joi190122supp2_prod.pdf#page=11), and [p.16 eTable 11 marginal allocations](../../../joi190122supp2_prod.pdf#page=16). All four displays reproduce the registered count-column pattern. The full affected count transcription below is in the printed order placebo/active; equal cells and subthreshold cells remain occurrences of the single pattern, not independent discrepancies.

| Row | Figure 3 and eFigure 2 placebo/active counts | Figure 4 and eFigure 3 placebo/active counts |
|---|---|---|
| Overall | 703 / 609 | 659 / 653 |
| White; Black | 451 / 406; 148 / 130 | Not displayed |
| Baseline ACR <30; ≥30 | 635 / 559; 67 / 50 | 596 / 598; 62 / 55 |
| Baseline 25(OH)D <20; 20–<30; ≥30 | 110 / 85; 230 / 203; 332 / 297 | Not displayed |
| Baseline eGFR ≥60; <60 | 612 / 531; 89 / 76 | Not displayed |
| BMI <25; 25–<30; ≥30 | 87 / 87; 228 / 205; 364 / 294 | Not displayed |
| Other randomized intervention placebo; active | 333 / 320; 370 / 289 | 289 / 320; 370 / 333 |
| EPA/DHA ≤2.2; >2.2 | Not displayed | 332 / 347; 308 / 292 |
| hsCRP ≤0.2; >0.2 | Not displayed | 334 / 335; 323 / 316 |
| Fish intake <1.5; ≥1.5 servings/week | Not displayed | 354 / 329; 295 / 310 |

**Rule applicable and comparison reproduced:** Counts should be attributed to their specified randomized treatment column. Allocation gives D active 370+333=703, D placebo 289+320=609, omega active 370+289=659 and omega placebo 333+320=653. Figure 3/eFigure 2 place the D totals under opposite headers. Table 1 gives D-active/placebo white 240+211=451 /199+207=406, black 73+75=148 /59+71=130, and 25(OH)D categories 62+48=110 /41+44=85, 109+121=230 /87+116=203, and 184+148=332 /146+151=297; these are likewise printed under opposite count headers. The four factorial cells independently demonstrate the same issue in all four figures. Route A category 2 applies to these printed count substitutions; no replacement is asserted for subgroup rows lacking independent arm-specific comparators.

**Display-precision calculation:** Derived D totals receive ±1. Printed placebo 703 [702.5,703.5] versus allocated placebo 609 [608,610] gives gap 92.5/609=0.15189; printed active 609 [608.5,609.5] versus allocated active 703 [702,704] gives gap 92.5/703=0.13158. White gaps are 43.5/406=0.10714 and 43.5/451=0.09645; black 16.5/130=0.12692 and 16.5/148=0.11149. Three vitamin-D-category gaps are 23.5/85=0.27647 and /110=0.21364; 25.5/203=0.12562 and /230=0.11087; 33.5/297=0.11279 and /332=0.10090. For allocation-cell copies, intervals ±0.5 each give gap |a−b|−1: D figures' omega-active stratum gives 80/289=0.27682 and 80/370=0.21622; omega-placebo stratum gives 12/320=0.03750 and 12/333=0.03604, below threshold alone. Omega figures' D-placebo stratum gives 30/320=0.09375 and 30/289=0.10381; D-active stratum gives 36/333=0.10811 and 36/370=0.09730. Overall omega 659-versus-653 alone is subthreshold: against a marginal sum allowance, gap 4.5 divided by either total is <0.007. ACR 635+67=702 gives [701,703], overlapping printed overall 703 [702.5,703.5]; it corroborates the column's D-active-sized population, not a separate subtotal discrepancy.

**Inputs available / exact missing inputs:** All plotted count cells, allocation cells, race/concentration marginals, overall modeled outcome changes and their treatment labels are available. Independent arm-specific ACR/eGFR/BMI/omega biomarker subgroup population lists and fitted output linking each subgroup outcome summary to participant IDs are absent. No unsupported numeric replacement for those rows is inferred.

**Alternative and observation versus explanation:** Overall outcome labels match independent tables: Figure 3 placebo −13.1/active −12.3 matches Table 2; eFigure 2 placebo 3.02/active 2.97 and eFigure 3 placebo 3.05/active 2.94 match eTable 6. Thus a wholesale exchange of count and outcome columns is not established as resolution. Count-column transposition is a possible production mechanism, not a source-confirmed explanation. Opposite count attribution at the independently matched rows is direct.

**Classification:** All compared locations are REPORT. Main-internal comparisons establish S_W and supplement-versus-main allocation comparisons establish S_C; S_C has precedence. Domain statistical_results, because the issue is counts paired with outcome summaries. No classification correction. Ambiguity: whether only counts or additional subgroup outcome summaries have different allocation associations remains unresolved.

**Evidence state:** reproduced; independently supplied allocations/marginals disagree with the printed treatment-column counts beyond precision across the registered repeated pattern.

**Remaining human question:** Which participant counts accompany each treatment-specific subgroup result in all four figures, and were count columns alone transposed or also subgroup outcome summaries associated with different allocation cells?

## C013 — Omega-3 contributor rows repeat vitamin-D counts

**Locations found; source and comparator matched:** REPORT [main p.7 Figure 2 A–D and caption](../../../jama_de_boer_2019_oi_190122.pdf#page=7) calls the rows participants contributing data. Panels A and B print the same eGFR rows, placebo 607/459/438 and active 701/531/496 at baseline/year 2/year 5; panels C and D print the same ACR rows, placebo 609/463/440 and active 702/529/505. REPORT [main p.8 Table 2](../../../jama_de_boer_2019_oi_190122.pdf#page=8) instead gives omega eGFR active 657/499/472 and placebo 651/491/462; REPORT [supplement p.11 eTable 6](../../../joi190122supp2_prod.pdf#page=11) gives omega ACR active 658/502/478 and placebo 653/490/467. REPORT [main p.1 allocation](../../../jama_de_boer_2019_oi_190122.pdf#page=1) supports the omega-active population cap of 659.

**Rule applicable and comparison reproduced:** Match outcome, intervention and time point, then compare contributor counts. The B/D rows copy their respective A/C counts and differ from matched omega tables. Route A category 2 applies to count cells changing magnitude, and the baseline over-allocation count independently affects primary population interpretation. This does not reconstruct model-based estimates from crude counts.

**Display-precision calculation:** Each printed copy has ±0.5, so gap=|difference|−1. eGFR B active relative gaps are 43/657=0.06545, 31/499=0.06212 and 23/472=0.04873; placebo 43/651=0.06605, 31/491=0.06314 and 23/462=0.04978. The year-5 eGFR cells do not independently exceed 0.05. ACR D active gaps are 43/658=0.06535, 26/502=0.05179 and 26/478=0.05439; placebo 43/653=0.06585, 26/490=0.05306 and 26/467=0.05567. Example intervals: eGFR active baseline [700.5,701.5] versus [656.5,657.5], gap 43; ACR active year 5 [504.5,505.5] versus [477.5,478.5], gap 26. Allocation sum 370+289=659 gives [658,660], versus panel B active baseline [700.5,701.5], gap 40.5/659=0.06146.

**Inputs available / exact missing inputs:** Every A–D contributor cell, matched table count, caption and allocated arm size is available. Participant records defining graph populations and underlying plotted observations are absent. No claim about the distribution values themselves is made.

**Alternative and observation versus explanation:** A distinct graph population could change some contributor counts, but cannot supply 701 or 702 distinct omega-active participants from 659 randomized. Exact copying is directly visible in the count rows; a particular production mechanism or misassociation of plotted distributions remains unconfirmed.

**Classification:** All locations REPORT; S_C and S_W, primary S_C by precedence; statistical_results; unchanged. Ambiguity: underlying graph population/data attribution remains to be clarified.

**Evidence state:** reproduced; the complete copied-row pattern contains multiple matched count discrepancies beyond precision and an over-allocation baseline contributor count.

**Remaining human question:** Which intervention-specific populations and counts accompany each omega-3 panel time point, and do the plotted distributions use the same populations as Table 2/eTable 6?

## C014 — Plan gives two microgram equivalents for the same vitamin-D dose

**Locations found; source and comparator matched:** PLAN [p.15 V.e.1](../../../joi190122supp1_prod.pdf#page=15) gives each active study pill as 2000 IU (40 µg); PLAN [p.21 VII.a](../../../joi190122supp1_prod.pdf#page=21) repeats the intervention as 2000 IU (40 µg) and identifies an upper intake limit as 50 µg or 2000 IU. REPORT [main p.2 intervention](../../../jama_de_boer_2019_oi_190122.pdf#page=2) corroborates only the 2000-IU dose, with no conflicting microgram quantity.

**Rule applicable and comparison reproduced:** Equivalent quantities for the same substance using the supplied paired units should yield the same µg quantity for the same IU amount. The internal comparator, without an external conversion, implies 50 µg for 2000 IU versus the intervention's 40 µg. Route A category 2 applies to printed dose magnitude; no safety critique or preferred dose is added.

**Display-precision calculation:** Allow both IU values ±0.5 and comparator 50 µg ±0.5. The recomputed equivalent is [1999.5×49.5/2000.5, 2000.5×50.5/1999.5]=[49.47526,50.52526] µg. Printed 40 µg interval [39.5,40.5] has gap 8.97526/40=0.22438. Direct 40/50 equivalent copies give gap 9/50=0.18. Both exceed 0.05.

**Inputs available / exact missing inputs:** Both printed paired-unit statements and repeated intervention dose are available. A source-supplied statement selecting the intended microgram equivalent or product-dose specification is absent. No outside conversion was used.

**Alternative and observation versus explanation:** Either study-pill microgram equivalent or upper-limit paired-unit equivalence could account for the differing reading. Distinct equivalents are direct; which numeric transcription produced them is not established. The accompanying lower-than-limit wording is contextual and not a separate registered item.

**Classification:** Both compared locations PLAN; P_P only; plan_material. REPORT corroborates IU and does not add P_R. Confirmed, no correction. Ambiguity: which paired equivalence governs extraction.

**Evidence state:** reproduced; the supplied µg equivalents for the same 2000 IU do not reconcile beyond precision.

**Remaining human question:** Which microgram equivalent accompanies the planned 2000-IU cholecalciferol dose, and which supplied paired-unit statement explains 40 versus 50 µg?

## C015 — Plan interaction and primary models specify different time terms

**Locations found; source and comparator matched:** Exact PLAN [p.32 §15d Equation 1 and §15e Equation 2](../../../joi190122supp1_prod.pdf#page=32) was visually read from a fresh CPU source rendering. Equation 1 contains intercept, D, omega, D×omega, D×time, omega×time, D×omega×time, participant random intercept and residual, with no common time main effect. Equation 2 contains intercept, treatment, common time, treatment×time, participant random intercept and residual. The printed text models time categorically at 0,2,5 and uses the three-way coefficient's P<.05 to choose four-group versus marginal factorial comparison. REPORT [main p.3](../../../jama_de_boer_2019_oi_190122.pdf#page=3) describes categorical-time primary modeling and [p.4](../../../jama_de_boer_2019_oi_190122.pdf#page=4) reports interaction P=.42; these identify the relied-on decision, not an additional equation conflict.

**Rule applicable and comparison reproduced:** Set both treatment indicators to zero. Every printed time-dependent fixed term in Equation 1 disappears, leaving a constant double-placebo fixed mean; Equation 2 retains its common time trajectory. A participant random intercept changes a person's level, not a common fixed trajectory. The printed interaction/primary models therefore specify different time structures relevant to the interaction decision. Route B concerns a complete model-term discrepancy, not a solitary symbol or a preference for another analysis. Display precision is inapplicable to term presence.

**Inputs available / exact missing inputs:** Both full equations, treatment coding, time definition and interaction decision rule are available. Implemented interaction-model code, coefficient output, categorical contrast coding and a statement making common time implicit in Equation 1 are absent. P=.42 cannot be numerically refitted from aggregate summaries.

**Alternative and observation versus explanation:** The implementation may include an unprinted common time effect or intentionally apply the printed restriction. The complete printed term difference and its zero-treatment consequence are direct logical observations; actual fitted-code omission is not inferred.

**Classification:** Compared equations are both PLAN; P_P only; plan_material. Main REPORT corroborates analysis reliance and does not add P_R. Confirmed, no correction. Ambiguity: implemented term list is unavailable.

**Evidence state:** reproduced; visual exact-page inspection confirms the absence/presence of common time in the compared equations and the resulting model difference.

**Remaining human question:** Did the fitted interaction model include categorical time main effects, and what exact model generated interaction P=.42?

## C016 — Year-5 SGLT2 count and percentage do not reconcile

**Locations found; source and comparator matched:** REPORT [supplement p.7 eTable 2](../../../joi190122supp2_prod.pdf#page=7) prints D-placebo year-5 biguanides 313 (74%), SGLT2 inhibitors 21 (4%), D-active SGLT2 25 (6%), overall 46 (5%) and omega active/placebo 24 (5%)/22 (5%). All SGLT2 cells and the full footnote were read. The footnote says percentages use nonmissing responses, with overall N=916 at year 5; it gives no drug-specific denominator exception. Other same-column year-5 entries include sulfonylureas 120 (28%), insulin 59 (14%) and DPP-4 inhibitors 56 (13%), consistent with approximately 423 respondents.

**Rule applicable and comparison reproduced:** Under the table's common year/arm response interpretation, a count/percentage must reconcile with the same-column respondent denominator. The support is the common nonmissing-response footnote and mutually compatible same-column rows; randomized N=609 was not imposed. Route A category 3 applies to count/percentage/denominator within one display. A medication-specific denominator remains an explicit alternative, not an established exception.

**Display-precision calculation:** 313±0.5 and 74±0.5% imply denominator [312.5/0.745,313.5/0.735]=[419.46309,426.53061]. 21±0.5 then implies percentage [100×20.5/426.53061,100×21.5/419.46309]=[4.80622,5.12560]%. Printed 4% interval [3.5,4.5]% has gap 0.30622/4=0.07655>0.05. The 21 (4%) pair itself requires denominator [20.5/0.045,21.5/0.035]=[455.55556,614.28571], disjoint from the biguanide-derived interval. Count 25+21=46 reconciles. The active 25 (6%) comparison does not independently exceed 0.05 after full half-unit allowances (gap at most 0.27504/6=0.04584). Overall/omega SGLT2 cells do not independently establish this discrepancy.

**Inputs available / exact missing inputs:** Same-column counts/percentages, all SGLT2 cells and common total-response footnote are available. Exact year-5 arm-specific respondent denominators, item-specific missingness counts and an explicit common-versus-drug-specific response definition are absent. A denominator around 423 is supported, not assigned as a final value.

**Alternative and observation versus explanation:** SGLT2 may use a distinct response set, but the table does not describe that exception. A percentage taken from another arm is another possible production mechanism. Printed counts/percentages and interval incompatibility under the footnote-supported common population are direct; specific denominator choice or switching mechanism is inferred.

**Classification:** Same results-supplement REPORT throughout; S_W only; statistical_results; unchanged. Classification ambiguity: none as to role/domain; shared response-set interpretation and absent medication-specific definition remain evidence limitations.

**Evidence state:** reproduced; the source-footnote-supported common response interpretation gives a nonoverlapping percentage interval with relative gap 0.07655. This fact does not determine which field or denominator a human should use.

**Remaining human question:** What exact D-placebo year-5 denominator produced 21 (4%), and did it differ from the response population underlying 313 (74%) and the other medication rows?

## C017 — Paired-urine exclusion accounting does not reconcile

**Locations found; source and comparator matched:** REPORT [supplement p.12 eTable 7](../../../joi190122supp2_prod.pdf#page=12) title gives N=944; baseline/year-5 D rows 504+440 and omega rows 477+467 each sum to 944. The complete footnote gives 1312 enrolled, 1311 baseline urine donors, 991 donating year-5 urine and expressly included, 320 baseline-but-not-year-5 exclusions, and one no-baseline exclusion.

**Rule applicable and comparison reproduced:** A stated paired-sample inclusion/exclusion partition within one table should reconcile with its title/body population. Footnote 991+320=1311 reconciles internally, but title/body imply 1311−944=367 exclusions rather than 320. Route A category 3 applies to the exclusion accounting; 991-versus-944 alone is not the qualifying calculation.

**Display-precision calculation:** Baseline donors [1310.5,1311.5] minus title included [943.5,944.5] gives excluded [366,368]. Printed exclusions [319.5,320.5] have gap 45.5/320=0.14219>0.05. Using two body-cell sums gives included [943,945], implied exclusions [365.5,368.5], gap 45/320=0.140625. The two included copies 991 and 944 have gap 46/991=0.04642 or 46/944=0.04873, below 0.05. The full total partition 944+320+1=1265 versus 1312 likewise does not independently exceed the relative threshold. These subthreshold checks remain context for the exclusion discrepancy.

**Inputs available / exact missing inputs:** Complete title/body/footnote accounting is available. A source-defined additional eligibility filter explaining the 47-person included-count difference, individual paired specimen eligibility and source output populations are absent.

**Alternative and observation versus explanation:** Footnote numbers could describe a different available-sample set, but explicitly say that 991 were included in this analysis. An additional filter or reused historical footnote is possible, not documented. The printed partition difference is direct; a 47-person mechanism is inferred.

**Classification:** All locations within one results-supplement REPORT; S_W only; statistical_results; unchanged. Ambiguity: no role/type ambiguity; population filter absent.

**Evidence state:** reproduced; the implied excluded-count interval does not reconcile with printed 320 beyond precision.

**Remaining human question:** How many baseline urine donors were included and excluded in eTable 7, and what source-defined filter reconciles N=944 with footnote 991 included/320 excluded?

## C018 — Albuminuria forest favor labels reverse the ratio direction

**Locations found; source and comparator matched:** REPORT [supplement p.18 eFigure 2](../../../joi190122supp2_prod.pdf#page=18) and [p.19 eFigure 3](../../../joi190122supp2_prod.pdf#page=19) were visually read, including both ratio headers, ticks, null lines and all favor arrows. Each header states ratio of change, active/placebo (95% CI); left-of-1 is labeled Favors Placebo, right-of-1 Favors Vitamin D/Omega-3. Axis ticks are 0.5,0.7,1,1.3,1.7. Overall placebo/active change ratios are D 3.02/2.97 and omega 3.05/2.94. REPORT [supplement p.11 eTable 6](../../../joi190122supp2_prod.pdf#page=11) defines follow-up/baseline changes and active-to-placebo ratio. REPORT [main p.3 ACR progression definition](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 threefold increase narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4), and PLAN [p.11 slower-progression hypotheses](../../../joi190122supp1_prod.pdf#page=11), [p.17 ACR definition](../../../joi190122supp1_prod.pdf#page=17) were matched as direction corroboration. The shared axes govern every plotted overall and subgroup row in both figures.

**Rule applicable and comparison reproduced:** For positive follow-up/baseline ACR changes, active/placebo ratio <1 means smaller ACR increase with active; >1 means larger increase with active. The printed favor labels assert the reverse of that defined direction. Route A category 2 applies to a direction/reference statement reversing the quantity's meaning. This is not a model-versus-crude ratio comparison. Display precision does not reconcile a reversed favor direction; ticks 0.5 and 1.7 remain far from null under half-unit allowances. No model effect estimates were recomputed from crude summaries.

**Inputs available / exact missing inputs:** Axis definition, null, direction arrows, underlying change definition and progression direction are supplied. Implemented plot contrast coding and an author statement choosing between axis-reference text and favor arrows are absent. All rows share the confirmed direction conflict; no row-specific P/CI discrepancy is asserted.

**Alternative and observation versus explanation:** The favor labels could be exchanged, or the intended plotted reference could be placebo/active despite the printed active/placebo header. The report tables support the printed active/placebo quantity but do not select a final action. Opposing header-defined and arrow-labeled directions are direct; production mechanism is inferred.

**Classification:** Conflicting ratio/direction content is within the same results-supplement REPORT: S_W only, statistical_results. Main REPORT and PLAN corroborate quantity/benefit direction, so they do not add S_C or P_R. Confirmed without correction. Ambiguity: intended plot reference or favor orientation remains a human question.

**Evidence state:** reproduced; both exact-source figures visibly place placebo favor on the below-1 side of an active/placebo ACR-change ratio, opposite the source-defined progression direction.

**Remaining human question:** Are the forest ratios active/placebo or placebo/active, and which side of 1 represents the intended treatment-favor direction?

## Recheck completion and limitations

Covered IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017 and C018. Counts: 18 reproduced; 0 reproduced_after_transcription_correction; 0 not_reproduced. Classification changes: 0. All cited supplied physical locations were found. Every registered repeated-pattern display and count cell was inspected; independently unsupported replacement counts were not manufactured.

Unresolved source inputs are identified separately in each card: final/intervening amendments, participant-level eligibility/adherence/specimen linkage, blood/urine union, estimator and fitted-model code, bioavailable subgroup output, exact medication responder populations, paired-urine filters and plot-reference coding. These do not constitute omitted source-location coverage. Evidence states record what the supplied statements/values reproduce and do not decide a human disposition. The coordinator should carry each card's alternative interpretation and exact remaining question into the report. C016 in particular must retain the common-response interpretation and missing medication-specific denominator definition; C001 must retain latest-plan/report agreement and explicit amendment disclosure.
