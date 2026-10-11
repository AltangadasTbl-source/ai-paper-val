# Workflow 1.6.2 Mechanical Evidence Recheck

Runtime task: `/root/evidence_rechecker`. Fresh named `qc162_evidence_rechecker`, run model `gpt-6.1-sol`, reasoning effort `high`. Scope: every assigned stable ID, C001, C002, C003, C004, C005 and C006, including every cited comparison and affected repeated-pattern cell. All six remain **Pending Human Adjudication**. These evidence states record mechanical facts and are not dispositions.

The complete scope and review contract, current ledger, initial independent screen and current checker evidence were read. Supplied PDFs are authority; maps and derivative text were locators. Direct CPU Poppler `pdftotext -layout` extraction covered main PDF pp.1–9, plan PDF pp.1–45, results supplement pp.1–41 and data-sharing supplement p.1. Issue-bearing main pp.2,4,5,6,7,8 were directly rendered anew with CPU Poppler `pdftoppm -r 120 -singlefile -png`; main p.3 and plan pp.14,19,25,31 were inspected in existing current-run direct-source page rasters. Plan p.45 was additionally rendered at 180 dpi to resolve paragraph-specific date transcription. No reusable image was final authority, no OCR was required, and no source/reused artifact was modified.

Fresh derivatives, all under `preprocessing/`: `recheck-main-p1-p9.txt`, `recheck-plan-p1-p45.txt`, `recheck-report-supp2-p1-p41.txt`, `recheck-report-supp3-p1.txt`, `recheck-main-p2.png`, `recheck-main-p4.png`, `recheck-main-p5.png`, `recheck-main-p6.png`, `recheck-main-p7.png`, `recheck-main-p8.png`, and `recheck-plan-p45.png`. Text engine: direct Poppler `pdftotext -layout`; raster engine: direct Poppler `pdftoppm`, CPU. Current-run images reused without modification: `cross-main-p3.png`, `support-core-plan-p14.png`, `st1-plan-p19.png`, `cross-plan-p25.png`, `cross-plan-p31.png` and `st1-plan-p45.png`. The high-resolution recheck p.45 independently confirms the paragraph-specific dates below.

| ID | Evidence state | Primary relationship type | All relationships | Review domain | Classification correction |
|---|---|---|---|---|---|
| C001 | reproduced_after_transcription_correction | P_R | P_R, P_P | protocol_report | None; paragraph-specific date transcription corrected |
| C002 | reproduced | P_R | P_R | protocol_report | None |
| C003 | reproduced | P_R | P_R | protocol_report | None |
| C004 | reproduced | P_R | P_R | protocol_report | None |
| C005 | reproduced | S_W | S_W | statistical_results | None |
| C006 | reproduced | S_W | S_W | statistical_results | None |

## C001 — De novo cancer outcome hierarchy

**Location found / source value matched / comparator matched:**

- [PLAN initial synopsis p.4](../../../joi190023supp1_prod.pdf#page=4), direct source text: de novo cancer in organs other than the primary site after supplementation starts is included as an adverse event, not an outcome. This is historical corroboration, not a separate conflicting version by itself.
- [PLAN final synopsis p.19](../../../joi190023supp1_prod.pdf#page=19), exact current-source page raster and direct text: the same organ restriction and post-supplementation timing are stated; the synopsis explicitly includes the cancer as an adverse event, not an outcome.
- [PLAN final body p.25](../../../joi190023supp1_prod.pdf#page=25), exact current-source page raster and direct text: the same endpoint is explicitly under the heading Tertiary outcome. Safety outcomes are separately headed.
- [PLAN amendment p.45](../../../joi190023supp1_prod.pdf#page=45), exact direct 180-dpi source render and direct text: Double (triple) cancer incidence paragraph says the endpoint was initially a severe adverse event, then separated from secondary and safety outcomes and inserted as a tertiary outcome. Its paragraph-final date is **2012.12.8**. The version-3 heading is **2012.12.18**, the subgroup paragraph is **2012.12.18**, and the DBP paragraph is **2012.12.8**. The supplied page itself has these different paragraph-specific readings.
- [REPORT main p.2 Outcomes](../../../jama_urashima_2019_oi_190023.pdf#page=2), direct source render/text: introduces the Safety outcomes list, which continues on the next page.
- [REPORT main p.3 Outcomes continuation and Statistical Analysis](../../../jama_urashima_2019_oi_190023.pdf#page=3), exact current-source raster and direct text: safety includes bone fractures, urinary stones, serious admission events and new de novo cancer in other organs after study medication starts. The statistical section distinguishes randomized-group relapse/death outcomes from per-protocol adverse-event assessment.
- [REPORT main p.8 Table 3](../../../jama_urashima_2019_oi_190023.pdf#page=8), direct source render/text: heading Safety Outcomes; Cancer de novo row is 15 (6.6) / 8 (5.4) under until-censoring 227/147, 16 (6.6) / 9 (5.6) under adherent-for-1-year 243/160, and 16 (6.4) / 9 (5.4) under randomized 251/166. Footnote a defines per-protocol populations; b defines randomization group independent of adherence; d identifies the same other-organ, post-medication cancer endpoint.

**Consistency rule applicable:** Yes. Match endpoint identity by organ restriction and post-medication timing, then compare explicit outcome hierarchy. Route A, category 5 concerns a changed prespecified outcome status. The final PLAN synopsis/body comparison also establishes a plan-internal status inconsistency.

**Logical comparison reproduced / display precision:** Yes. Final body and amendment say tertiary and separated from safety; final synopsis says adverse event, not outcome; main report explicitly says safety. This is a categorical hierarchy comparison, so numerical half-unit discrepancy intervals do not apply. The differently labeled Table 3 populations reconcile as separate displays and are not claimed to be the same count/denominator. Their numerical values do not establish another inconsistency.

**Necessary inputs available:** Endpoint definition, categorical hierarchy labels, final-plan amendment statement, report safety label and all displayed analysis-population headers/footnotes are present.

**Exact missing inputs or definitions:** No supplied later hierarchy amendment or statement explaining how the final tertiary designation maps to the report's safety designation and analysis-population choice. The paragraph-specific dates do not establish which later document, if any, governed reporting.

**Source-grounded alternative interpretation:** The final synopsis may retain an earlier adverse-event description; the report may present a tertiary endpoint in a safety table. An unprovided later amendment is possible but not observed. These alternatives do not make the printed hierarchy statements identical.

**Direct observation versus inferred explanation:** Direct: tertiary/adverse-event/safety labels, matched endpoint restrictions, three explicit population columns and paragraph-specific dates. Inferred only: retained synopsis wording, rationale for safety presentation, or existence of a later amendment. No chronology or mechanism is asserted from those inferences.

**Classification confirmation:** All main pp.2,3,8 are REPORT by their trial methods/results content. Plan pp.4,19,25,45 are PLAN by their protocol/synopsis/amendment content. Report versus final plan body/amendment gives P_R; final synopsis versus final body gives P_P. Primary **P_R** has precedence over P_P; **All relationships: P_R, P_P**; **Review domain: protocol_report**. Classification ambiguity: hierarchy-version status remains a human question, but document roles and precedence are unambiguous. No classification correction.

**Evidence state: reproduced_after_transcription_correction.** Determining fact: the independent screen and registration asserted that the de novo amendment paragraph printed 2012.12.18; the exact supplied-source paragraph actually prints 2012.12.8. Correcting that transcription preserves the explicitly tertiary-versus-safety/adverse-event comparison. The date itself is not an additional candidate.

**Exact remaining human question:** What final prespecified and reported outcome hierarchy and analysis population apply to de novo cancer, and how does its tertiary status map to the safety presentation?

**Coordinator provenance update:** Retain the registration history, then append that this fresh recheck confirms version-3/subgroup dates 2012.12.18 but de novo/DBP paragraph dates 2012.12.8. Replace any assertion that every paragraph or the de novo paragraph prints 2012.12.18 with paragraph-specific source readings. Update C001's evidence state as above; preserve its ID, included finding IDs and classification.

## C002 — Planned Kaplan–Meier and reported Nelson–Aalen curves

**Location found / source value matched / comparator matched:**

- [PLAN initial SAP p.14 method 5c](../../../joi190023supp1_prod.pdf#page=14) and [PLAN final SAP p.31 method 5c](../../../joi190023supp1_prod.pdf#page=31), exact current-source rasters/direct text: Kaplan–Meier survival curves will be created on intent-to-treat analysis. Adjacent method 5d separately specifies Cox HRs and intervals for RFS and OS.
- [PLAN final synopsis p.19](../../../joi190023supp1_prod.pdf#page=19), exact current-source raster/direct text: intent to treat, Kaplan–Meier survival curves, Cox hazards models.
- [PLAN amendment p.45](../../../joi190023supp1_prod.pdf#page=45), exact direct raster/text: identifies dose, sample-size, subgroup, DBP and cancer-status changes; no Kaplan–Meier/Nelson–Aalen change is stated. The page's dates are recorded paragraph-specifically under C001; the date is context, not an analysis-method comparator.
- [REPORT main p.3 Statistical Analysis](../../../jama_urashima_2019_oi_190023.pdf#page=3), exact current-source raster/direct text: vitamin D/placebo effects on relapse/death and total death are estimated using Nelson–Aalen cumulative-hazard curves; Cox models determine HRs and 95% CIs; all randomized patients are included.
- [REPORT main p.6 Figure 2A/B and caption](../../../jama_urashima_2019_oi_190023.pdf#page=6), direct source raster/text: relapse/death and death axes are cumulative hazard; caption explicitly names Nelson–Aalen cumulative-hazard curves. Printed HRs are 0.76 (0.50–1.14), P=.18 and 0.95 (0.57–1.57), P=.83. Panel C is separately a competing-risk cumulative-incidence display.
- [REPORT main p.7 Figure 3A–D and caption](../../../jama_urashima_2019_oi_190023.pdf#page=7), direct source raster/text: subgroup relapse/death and death curves explicitly described as Nelson–Aalen cumulative hazards.
- [REPORT main p.1 abstract](../../../jama_urashima_2019_oi_190023.pdf#page=1) and [REPORT main p.4 effects](../../../jama_urashima_2019_oi_190023.pdf#page=4), direct supplied-source text, with direct p.4 raster: five-year RFS 77%/69%, OS 82%/81%; no estimator is named specifically for these percentages. The p.1 abstract HR/CI/P copies match p.4 and Figure 2.
- [REPORT results supplement pp.1–41](../../../joi190023supp2_prod.pdf#page=1), fresh direct whole-source layout extraction and complete current map: tables are Cox models and efficacy figure captions/axes describe cumulative hazards; no reported Kaplan–Meier survival-curve counterpart identified. [REPORT data-sharing statement p.1](../../../joi190023supp3_prod.pdf#page=1) supplies availability statements, not another efficacy analysis.

**Consistency rule applicable:** Yes. Compare the specifically planned primary/key-secondary survival-curve analysis with the explicitly reported estimator and displayed quantity. Survival curves and Nelson–Aalen cumulative-hazard curves are distinct named analysis displays. Route A, category 5 applies to the planned-analysis counterpart question.

**Logical comparison reproduced / display precision:** Yes. Both supplied SAP versions agree on Kaplan–Meier; report Methods and both relevant figure captions explicitly name Nelson–Aalen, with no supplied Kaplan–Meier display. The comparison is categorical; numerical half-unit discrepancy intervals and relative discrepancy are not applicable. No numeric claim is made about the printed Cox estimates or survival percentages.

**Necessary inputs available:** Planned method name, ITT population, endpoint matching, reported method name, quantity-axis labels, figure captions and complete supplied results-supplement inventory.

**Exact missing inputs or definitions:** Estimator used to calculate five-year survival percentages; whether Kaplan–Meier was also performed; any unsupplied method amendment. Individual event/censoring data and code are not supplied, and no curve values are reconstructed from pixels.

**Source-grounded alternative interpretation:** Kaplan–Meier may have generated survival percentages while Nelson–Aalen generated plotted curves. This can coexist with the report's stated Cox analysis, but the supplied report does not document that division. No estimator is assigned to percentages by inference.

**Direct observation versus inferred explanation:** Direct: plan names Kaplan–Meier; report names Nelson–Aalen and displays cumulative-hazard axes; printed survival percentages lack an explicit estimator label. Inferred only: an unreported additional Kaplan–Meier calculation or method amendment. The recheck establishes reported counterpart absence within the supplied documents, not proof that no calculation was ever performed.

**Classification confirmation:** All main locations and non-plan results/data-sharing supplements are REPORT by content; initial/final SAP, final synopsis and amendment are PLAN. **Primary relationship type: P_R**; **All relationships: P_R**; **Review domain: protocol_report**. The agreeing initial/final plans do not create P_P. Classification ambiguity: none in role/type/domain; performed-but-unreported analysis remains a human question. No classification correction.

**Evidence state: reproduced.** Determining fact: the exact planned and reported named curve analyses differ, with no supplied reported Kaplan–Meier curve counterpart; ledger's compared statements/locations match.

**Exact remaining human question:** Was the planned Kaplan–Meier analysis performed or replaced, and which estimator generated the five-year survival percentages?

## C003 — Planned risk-ratio evaluations of relapse and safety

**Location found / source value matched / comparator matched:**

- [PLAN initial SAP p.14 method 5e](../../../joi190023supp1_prod.pdf#page=14) and [PLAN final SAP p.31 method 5e](../../../joi190023supp1_prod.pdf#page=31), exact current-source rasters/direct text: relapse and safety outcomes will be evaluated using risk ratio (RR). Both versions state the same specification.
- [REPORT main p.3 post hoc methods](../../../jama_urashima_2019_oi_190023.pdf#page=3), exact current-source raster/direct text: relapse cumulative incidence treats death from other causes as a competing risk and uses subdistribution HRs and 95% CIs. Safety assessment is per protocol for continued medication use.
- [REPORT main p.6 Figure 2C and relapse narrative](../../../jama_urashima_2019_oi_190023.pdf#page=6), direct source raster/text: total subdistribution HR 0.75 (0.48–1.17), P=.21; middle 0.44 (0.21–0.89), P=.02; low 1.18 (0.64–2.19), P=.59. Caption specifies cumulative incidence under competing risk, distinct from panels A/B cumulative hazards.
- [REPORT main p.7 Table 2 relapse rows](../../../jama_urashima_2019_oi_190023.pdf#page=7), direct source raster/text: the same total/low/middle values, intervals and P values, labeled Subdistribution HR (95% CI). No RR is printed there.
- [REPORT main p.8 Table 3 all outcome rows and footnotes](../../../jama_urashima_2019_oi_190023.pdf#page=8), direct source raster/text: safety columns show counts/percentages for until-censoring, one-year adherence and randomization populations, without RR or RR interval columns. Full repeated-pattern source transcription follows; within each column-pair values are vitamin D / placebo.

| Table 3 outcome | Per protocol until censoring, 227/147 | Per protocol 1 year, 243/160 | Randomized, 251/166 |
|---|---|---|---|
| Fracture | 3 (1.3) / 5 (3.4) | 3 (1.2) / 6 (3.8) | 3 (1.2) / 6 (3.6) |
| Urinary stones | 2 (0.9) / 0 (0.0) | 4 (1.6) / 2 (1.3) | 4 (1.6) / 4 (2.4) |
| Severe adverse events | 19 (8.4) / 9 (6.1) | 20 (8.2) / 13 (8.1) | 21 (8.4) / 15 (9.0) |
| Cancer de novo | 15 (6.6) / 8 (5.4) | 16 (6.6) / 9 (5.6) | 16 (6.4) / 9 (5.4) |

Footnote a explicitly defines continuing medication until censoring or for more than one year and records one lost participant as nonadherent; b defines randomization group independent of adherence; c defines admission-related adverse events; d defines de novo other-organ cancer after medication starts. Every row and all six population columns were visually checked. Complete fresh text of the results supplement pp.1–41 and data-sharing p.1 identifies no relapse/safety RR display counterpart; efficacy tables/panels retain Cox/HR/cumulative-hazard labels.

**Consistency rule applicable:** Yes. The eligible comparison is the explicit PLAN versus REPORT analysis specification and status for the same endpoints, not equality of a crude risk ratio and a model-based subdistribution HR. Route B: focus area D admits analysis specifications; the reported post hoc competing-risk method and descriptive safety table leave the specifically planned RR evaluation's status unclear; relapse measure coding and safety treatment-comparison extraction depend on that status.

**Logical comparison reproduced / display precision:** Yes. Both plans specifically name RR; the report's matched relapse output names subdistribution HR and safety output gives descriptive cells, with no RR counterpart or explanation of its status. The measure/status comparison is categorical, so half-unit numeric discrepancy intervals are not applicable. No crude RR is substituted for a reported HR, and no numerical contradiction of the reported HRs is asserted. The three Table 2 estimates match their p.6 copies.

**Necessary inputs available:** Explicit planned measure and endpoint categories; reported relapse measure, competing-risk definition, safety population headers/footnotes and complete supplied report results inventory.

**Exact missing inputs or definitions:** Whether planned RRs were performed but not reported, replaced through an analysis amendment, or represented by a separately intended report counterpart. Planned RR time horizon, analysis-population specifics and resulting RRs/intervals are not supplied in method 5e. The displayed populations permit crude descriptive calculations but do not identify the prespecified analysis implementation.

**Source-grounded alternative interpretation:** Risk-ratio evaluation may have occurred without presentation; the competing-risk analysis may be an additional post hoc analysis; descriptive safety reporting may be deliberate. No preferred model or replacement measure is proposed.

**Direct observation versus inferred explanation:** Direct: RR wording in both SAPs, post hoc competing-risk/subdistribution-HR wording in the report, all printed safety count/percentage displays, and absence of a named RR counterpart in supplied reports. Inferred only: how or why the planned evaluation was changed, or that it was never performed. Neither inference is asserted as a fact.

**Classification confirmation:** Main pp.3,6,7,8 and results/data-sharing supplement are REPORT by content; both SAP pages are PLAN. **Primary relationship type: P_R**; **All relationships: P_R**; **Review domain: protocol_report**. Plan versions agree; no P_P. C001 separately concerns cancer hierarchy and C006 separately concerns HR direction; those do not change this measure/status classification. Classification ambiguity: none; RR implementation remains unclear. No classification correction.

**Evidence state: reproduced.** Determining fact: exact supplied method 5e specifies RR for both endpoint groups, while matched supplied report output has different measure/presentation and no RR counterpart explaining the planned analysis's status.

**Exact remaining human question:** Were the prespecified relapse and safety RR evaluations performed, replaced or unreported, and which reported quantities, time horizons and populations are their counterparts?

## C004 — Prespecified high-baseline subgroup omitted from efficacy analysis

**Location found / source value matched / comparator matched:**

- [PLAN final SAP p.31 subgroup list i and interaction rule](../../../joi190023supp1_prod.pdf#page=31), exact current-source raster/direct text: low <20, middle ≥20 to ≤40 and high >40 ng/mL are listed; interaction P values are computed with multiplicative variables. No minimum subgroup-size exception is printed in this specification.
- [PLAN amendment p.45 subgroup paragraph](../../../joi190023supp1_prod.pdf#page=45), exact direct 180-dpi raster/text: subgroup analyses stratified at 20 and 40 ng/mL were decided after trial initiation and before first midterm analysis, at **2012.12.18**. This paragraph/date matches the registered C004 provenance.
- [REPORT main p.3 Statistical Analysis](../../../jama_urashima_2019_oi_190023.pdf#page=3), exact current-source raster/text: all three baseline subgroups are described as prespecified, while interaction testing compares low/middle; high is not included because of its small patient count.
- [REPORT main p.4 subgroup population and omission](../../../jama_urashima_2019_oi_190023.pdf#page=4), direct source raster/text: low 173, middle 232, high 5; further high-baseline analyses were not conducted because of small numbers.
- [REPORT main p.5 Table 1 high row](../../../jama_urashima_2019_oi_190023.pdf#page=5), direct source raster/text: vitamin D 4 (1.6), placebo 1 (0.6). Total 4+1=5 matches p.4.
- [REPORT main p.7 Figure 3 caption and all four panels](../../../jama_urashima_2019_oi_190023.pdf#page=7), direct source raster/text: low/middle relapse/death and death panels only; caption explicitly says the high >40 group of five was not evaluated.
- [REPORT main p.8 limitations](../../../jama_urashima_2019_oi_190023.pdf#page=8), direct source raster/text: only five high-baseline patients, too few for statistical evaluation.
- [REPORT main p.1 abstract](../../../jama_urashima_2019_oi_190023.pdf#page=1), direct source text: highest group's small size and low/middle-only interactions corroborate the omission. Primary interaction .04 is printed in abstract/body; OS .13 is printed in the p.5 continuation. These values describe the two-group comparison and are not count/test conflicts here.

**Consistency rule applicable:** Yes. Compare listed prespecified efficacy subgroup scope for primary relapse/death and key-secondary survival with explicitly reported omission. Route A, category 5 includes a planned primary/key-secondary analysis not reported; the openly stated practical rationale is preserved as source context.

**Logical comparison reproduced / display precision:** Yes. The plan lists high >40 without a size exception, and the report explicitly excludes that subgroup analysis. This is categorical; discrepancy intervals/relative discrepancy are not applicable. Auxiliary counts reconcile exactly: 4+1=5, and 173+232+5=410 corresponds to baseline levels available after seven missing results among 417 randomized. Those count matches do not remove the planned-analysis scope observation.

**Necessary inputs available:** Prespecified subgroup thresholds and interaction rule, explicit exclusion statement, exact high-group counts, endpoint analysis context and disclosed small-n rationale.

**Exact missing inputs or definitions:** Any supplied final minimum-size condition, later analysis amendment, or prespecified procedure governing whether an observed very small subgroup would be omitted. The p.31 specification itself gives no such condition.

**Source-grounded alternative interpretation:** The small subgroup motivated a disclosed analysis decision; a size exception or amendment could exist outside supplied documents. The disclosed rationale is observed. No analysis of five patients is advocated, and the recheck does not challenge a clinical or statistical preference.

**Direct observation versus inferred explanation:** Direct: plan's three groups, report's three reported populations and two analyzed groups, arithmetic total, explicit small-n reason and 2012.12.18 subgroup date. Inferred only: existence of a prespecified exception/amendment outside supplied material.

**Classification confirmation:** All main locations are REPORT methods/results/limitations; SAP and amendment are PLAN. **Primary relationship type: P_R**; **All relationships: P_R**; **Review domain: protocol_report**. Classification ambiguity: none in role/type/domain; any unsupplied exception remains a human question. No classification correction. No P_P arises from the amendment merely corroborating subgroup thresholds.

**Evidence state: reproduced.** Determining fact: the matched plan includes the high-baseline efficacy subgroup and the report explicitly says it was not evaluated; registered C004's subgroup date 2012.12.18 is source-matched.

**Exact remaining human question:** Was a minimum subgroup-size condition or amendment part of the final specification governing omission of the high-baseline primary/key-secondary subgroup analysis?

## C005 — Table 1 genotype percentages and printed arm headers

**Location found / source value matched / comparator matched:** [REPORT main p.5 Table 1](../../../jama_urashima_2019_oi_190023.pdf#page=5), exact direct source raster/text, contains both halves headed No. (%) of Participants, Vitamin D (n=251), Placebo (n=166). Every BsmI, Cdx2, ApaI, TaqI, DBP1 and DBP2 cell below was independently visually matched. Footnote a says percentages may not sum to 100% because of rounding; b defines BMI; c identifies other pathology categories. None states a genotype-specific denominator exception.

**Consistency rule applicable:** Yes. Route A, category 3: count/denominator/percentage within one display. Each integer count and denominator permits ±0.5; recomputed percentage interval is [100(count−0.5)/(header+0.5), 100(count+0.5)/(header−0.5)]. Printed integer percentage permits ±0.5. Interval gap is zero if overlapping, otherwise the smallest separation; relative discrepancy is gap divided by printed percentage.

**Calculation reproduced / display precision:** Yes. Independent JavaScript arithmetic on exact visually read values reproduces 22 above-threshold cells. Complete calculations follow; gap units are percentage points. D = vitamin D, printed header 251; P = placebo, printed header 166.

| Locus / genotype | Arm (header) | Printed count (%) | Recomputed interval, % | Printed interval, % | Interval gap | Relative discrepancy |
|---|---|---|---|---|---|---|
| BsmI GG | D (251) | 175 (76) | [69.383698,70.059880] | [75.5,76.5] | 5.440120 | 0.071581 |
| BsmI GG | P (166) | 119 (79) | [71.171171,72.205438] | [78.5,79.5] | 6.294562 | 0.079678 |
| Cdx2 GG | D (251) | 89 (39) | [35.188867,35.728543] | [38.5,39.5] | 2.771457 | 0.071063 |
| Cdx2 GA | D (251) | 103 (45) | [40.755467,41.317365] | [44.5,45.5] | 3.182635 | 0.070725 |
| Cdx2 AA | D (251) | 38 (17) | [14.910537,15.369261] | [16.5,17.5] | 1.130739 | 0.066514 |
| Cdx2 GG | P (166) | 49 (33) | [29.129129,29.909366] | [32.5,33.5] | 2.590634 | 0.078504 |
| Cdx2 GA | P (166) | 77 (51) | [45.945946,46.827795] | [50.5,51.5] | 3.672205 | 0.072004 |
| ApaI GG | D (251) | 96 (42) | [37.972167,38.522954] | [41.5,42.5] | 2.977046 | 0.070882 |
| ApaI GT | D (251) | 104 (45) | [41.153082,41.716567] | [44.5,45.5] | 2.783433 | 0.061854 |
| ApaI GG | P (166) | 69 (46) | [41.141141,41.993958] | [45.5,46.5] | 3.506042 | 0.076218 |
| ApaI GT | P (166) | 61 (40) | [36.336336,37.160121] | [39.5,40.5] | 2.339879 | 0.058497 |
| TaqI TT | D (251) | 172 (74) | [68.190855,68.862275] | [73.5,74.5] | 4.637725 | 0.062672 |
| TaqI TT | P (166) | 115 (77) | [68.768769,69.788520] | [76.5,77.5] | 6.711480 | 0.087162 |
| TaqI TC | P (166) | 31 (21) | [18.318318,19.033233] | [20.5,21.5] | 1.466767 | 0.069846 |
| DBP1 TT | D (251) | 134 (58) | [53.081511,53.692615] | [57.5,58.5] | 3.807385 | 0.065645 |
| DBP1 TG | D (251) | 87 (38) | [34.393638,34.930140] | [37.5,38.5] | 2.569860 | 0.067628 |
| DBP1 TT | P (166) | 82 (55) | [48.948949,49.848943] | [54.5,55.5] | 4.651057 | 0.084565 |
| DBP1 TG | P (166) | 57 (39) | [33.933934,34.743202] | [38.5,39.5] | 3.756798 | 0.096328 |
| DBP2 CC | D (251) | 115 (50) | [45.526839,46.107784] | [49.5,50.5] | 3.392216 | 0.067844 |
| DBP2 CA | D (251) | 91 (39) | [35.984095,36.526946] | [38.5,39.5] | 1.973054 | 0.050591 |
| DBP2 CC | P (166) | 81 (54) | [48.348348,49.244713] | [53.5,54.5] | 4.255287 | 0.078802 |
| DBP2 CA | P (166) | 58 (39) | [34.534535,35.347432] | [38.5,39.5] | 3.152568 | 0.080835 |

Every relative discrepancy exceeds 0.05, including DBP2 CA vitamin D at 0.050591125 before output rounding. All other cells in these six locus groups were also read and checked; none adds another above-threshold header/percentage cell. One repeated unstated-denominator pattern is retained as one ID.

**Necessary inputs available:** All 22 printed counts/percentages, both repeated arm headers, displayed precision, all footnotes and every category count for inferred locus totals. No participant-level data are necessary for this header-based interval comparison.

**Exact missing inputs or definitions:** Explicit denominator instruction for genotype percentages; whether missing genotype results, assay exclusions or another availability rule determine each locus's population. Category sums alone do not state that rule.

**Source-grounded alternative interpretation:** Summing every visually confirmed category provides alternative available-case denominators:

| Locus | Vitamin D category sum | Placebo category sum |
|---|---|---|
| BsmI | 14+42+175=231 | 8+23+119=150 |
| Cdx2 | 89+103+38=230 | 49+77+24=150 |
| ApaI | 96+104+31=231 | 69+61+20=150 |
| TaqI | 172+54+5=231 | 115+31+4=150 |
| DBP1 | 134+87+10=231 | 82+57+9=148 |
| DBP2 | 115+91+25=231 | 81+58+11=150 |

Using these sums as alternative denominators, the recomputed and printed half-unit intervals overlap for every one of the 36 displayed genotype cells across these six loci; maximum remaining relative gap is zero. This explains the displayed percentages arithmetically but is an inferred denominator choice, not a printed Table 1 instruction. Supplemental genotype counts are corroboration only and create no S_C conflict for this candidate.

**Direct observation versus inferred explanation:** Direct: whole-arm headers, category counts, percentages and footnotes; above-threshold interval discrepancies under those headers. Inferred: category sums are the actual available-case denominators and missing genotype results account for reduced totals. The latter is plausible and source-grounded but not explicitly defined in the table.

**Classification confirmation:** Headers, rows and footnotes are in the same trial-results REPORT table. **Primary relationship type: S_W**; **All relationships: S_W**; **Review domain: statistical_results** because this concerns counts/denominators. No protocol relationship or supplement conflict is created by corroboration. Classification ambiguity: none; denominator definition remains missing. No classification correction.

**Evidence state: reproduced.** Determining fact: all 22 exact-source cells exceed the workflow's half-unit/0.05 criterion under the table's explicit 251/166 headers; alternative category-sum denominators are not explicitly assigned by its footnotes.

**Exact remaining human question:** Are the genotype percentages based on locus-specific available-case populations rather than printed arm headers, what availability rule applies, and which denominator should be retained for each baseline genotype proportion and subgroup-population extraction?

## C006 — Shared Table 2 hazard-ratio direction rule

**Location found / source value matched / comparator matched:**

- [REPORT main p.7 Table 2 footnote a](../../../jama_urashima_2019_oi_190023.pdf#page=7), direct source raster/text: HR values greater than 1 indicate vitamin D supplementation associated with decreased probability of the outcome. The wording is explicit, and the table outcomes are adverse events: relapse, cancer-specific death, noncancer death.
- All nine [REPORT p.7 Table 2](../../../jama_urashima_2019_oi_190023.pdf#page=7) comparisons were visually matched. Relapse, total/low/middle: 0.75 (0.48–1.17), P=.21; 1.18 (0.64–2.19), P=.59; 0.44 (0.21–0.89), P=.02. Cancer-specific death: 1.09 (0.58–2.01), P=.80; 1.45 (0.63–3.38), P=.38; 0.78 (0.29–2.10), P=.63. Noncancer death: 0.70 (0.29–1.73), P=.44; 1.11 (0.26–4.65), P=.89; 0.39 (0.11–1.39), P=.15. These all carry the same shared direction footnote.
- [REPORT main p.3 Statistical Analysis](../../../jama_urashima_2019_oi_190023.pdf#page=3), exact current-source raster/text: treatment compares vitamin D versus placebo on relapse/death risk; Cox HRs and relapse competing-risk subdistribution HRs are described, with no table-specific reciprocal treatment reference specified.
- [REPORT main p.4 effects](../../../jama_urashima_2019_oi_190023.pdf#page=4), direct source raster/text: vitamin D versus placebo HR 0.76 accompanies lack of significant reduction; middle-group HR 0.46 accompanies higher relapse-free survival under vitamin D. These define corroborating treatment direction, not the same numerical relapse-only estimand.
- [REPORT main p.6 relapse narrative and Figure 2C](../../../jama_urashima_2019_oi_190023.pdf#page=6), direct source raster/text: the same middle relapse result 0.44 (0.21–0.89), P=.02 is described as significantly lower cumulative incidence in vitamin D than placebo; total 0.75 matches the plotted competing-risk estimate. Figure 2C labels vitamin D/placebo accordingly.
- [REPORT main p.7 Figure 3A–D](../../../jama_urashima_2019_oi_190023.pdf#page=7), direct source raster/text: cumulative-hazard treatment labels corroborate the same treatment direction for adverse outcomes. Figure 3 is corroboration, not a claim that composite and relapse-only estimates must numerically match.

**Consistency rule applicable:** Yes. For the report's vitamin D versus placebo event-hazard contrast, above-null HR denotes higher event hazard and below-null denotes lower event hazard. The shared footnote assigns decreased outcome probability to HR>1, opposite the report's interpretation of its matching 0.44 relapse estimate. Route A, category 2 concerns a direction/reference statement reversing printed values.

**Logical comparison reproduced / display precision:** Yes. All nine point estimates keep their side of 1 throughout their two-decimal half-unit intervals:

| Outcome | Total HR interval | Low-baseline HR interval | Middle-baseline HR interval |
|---|---|---|---|
| Relapse | [0.745,0.755] | [1.175,1.185] | [0.435,0.445] |
| Cancer-specific death | [1.085,1.095] | [1.445,1.455] | [0.775,0.785] |
| Noncancer death | [0.695,0.705] | [1.105,1.115] | [0.385,0.395] |

The matched 0.44 narrative/table copies have identical half-unit intervals, so their numerical gap is zero; their direction definitions conflict. A reciprocal-reference diagnostic only gives [1/0.445,1/0.435]=[2.247191,2.298851], disjoint from [0.435,0.445], with gap 1.802191/0.44=4.095889. This is not a replacement estimate; it confirms that opposite contrast direction is not display rounding. The candidate is categorical direction reversal, so a count-derived estimate comparison is not required. No CI/P conflict is asserted for these rows.

**Necessary inputs available:** Exact shared footnote, all nine estimate/CI/P rows, named adverse outcomes, matched narrative interpretation of 0.44 and figure treatment labels. Raw data are unnecessary to establish the printed direction conflict.

**Exact missing inputs or definitions:** Table-specific treatment-reference clarification and intended above/below-null direction instruction; no explicit reciprocal reference is stated for Table 2.

**Source-grounded alternative interpretation:** The footnote may intend a reciprocal comparison or opposite inequality. Neither is specified, and a reciprocal interpretation does not harmonize the footnote with the report's interpretation of the identical 0.44 result. No numerical value is assigned replacement status.

**Direct observation versus inferred explanation:** Direct: greater-than-1/decreased footnote, nine point estimates and intervals, matched below-1/lower narrative, and treatment labels. Inferred only: whether the production mechanism involves an inequality or reference change. The recheck does not choose that explanation.

**Classification confirmation:** Every compared location is REPORT content within one main article. **Primary relationship type: S_W**; **All relationships: S_W**; **Review domain: statistical_results** because this is estimate-direction/test-interpretation logic. Plan corroboration would not add P_R. Classification ambiguity: none; intended table contrast remains a human question. No classification correction.

**Evidence state: reproduced.** Determining fact: the exact shared footnote reverses the adverse-outcome direction used in the report for the matching middle-baseline relapse estimate, and all affected values retain their null side under display precision.

**Exact remaining human question:** Which treatment-reference direction and greater/less-than-1 interpretation should be applied to all nine Table 2 HR/subdistribution-HR comparisons?

## Recheck completion

Covered IDs: C001, C002, C003, C004, C005, C006. Six complete cards; five evidence states reproduced and one reproduced_after_transcription_correction. No ID was removed and no classification field needs correction. The amendment-date transcription must be retained paragraph-specifically, particularly C001's de novo paragraph 2012.12.8 versus version/subgroup 2012.12.18. No date-only candidate is proposed.

Remaining human questions concern de novo outcome status/population, the survival-percentage estimator and planned Kaplan–Meier status, planned RR implementation/status, any high-subgroup size condition/amendment, genotype percentage denominators/availability rules, and Table 2 treatment-reference direction. Exact supplied-source confirmation is complete; those definitions are not supplied by this mechanical recheck. All stable IDs remain Pending Human Adjudication.
# Appended-ID Mechanical Evidence Recheck — Statistical Pass 2

Runtime task: `/root/pass_2_rechecker`. Fresh named `qc162_evidence_rechecker`, run model `gpt-6.1-sol`, reasoning effort `high`. Assigned scope: **C007 only**, including the target, all five same-page comparator results and the reported statistical method. C001–C006 and the canonical recheck artifact were not modified. C007 remains **Pending Human Adjudication**.

Authority: exact supplied main article PDF pp.3 and6. Direct CPU Poppler `pdftotext -layout -f 3 -l 3 jama_urashima_2019_oi_190023.pdf -` and the analogous p.6 command reread those source pages. Their current-run direct-source renders, `preprocessing/cross-main-p3.png` and `preprocessing/recheck-main-p6.png`, were inspected visually. Both tools were recorded as available in `tooling_record.md`; device CPU. No OCR, fresh derivative file, fallback, external evidence or source/reused-asset mutation was needed. The registered candidate, new checker finding and independent pass-2 screen served as locators; their source assertions were independently confirmed. The numerical calculation below was independently recomputed in JavaScript.

| ID | Evidence state | Primary relationship type | All relationships | Review domain | Classification correction |
|---|---|---|---|---|---|
| C007 | reproduced | S_W | S_W | statistical_results | None |

## C007 — Age-adjusted interval and P value lack a joint solution under a same-page reproducing calculation

**Location found / source value matched / comparator matched:** Yes, separately for every compared location:

| Exact supplied-source location | Role by content | Source-confirmed value or statement | Recheck fact |
|---|---|---|---|
| [Main PDF p.6, right-column age-quartile-adjusted relapse/death paragraph](../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Adjusted HR 0.66; 95% CI 0.43–0.99; P=.048. HRs adjusted by age quartile because the vitamin D group was older. The paragraph says relapse/death cumulative hazard was significantly less in that group. | Target attribution and all three printed numbers matched direct PDF text and source raster. |
| [Main PDF p.6, Figure 2A](../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Relapse or death: HR 0.76; 95% CI 0.50–1.14; P=.18. | S001 comparator found and matched visually and in direct source text. |
| [Main PDF p.6, Figure 2B](../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Death: HR 0.95; 95% CI 0.57–1.57; P=.83. | S002 comparator found and matched visually and in direct source text. |
| [Main PDF p.6, Figure 2C and right-column first relapse paragraph](../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Relapse by competing-risk analysis: subdistribution HR 0.75; 95% CI 0.48–1.17; P=.21. Narrative states no significant difference. | Both occurrences of S003 found; their values match. The distinct subdistribution effect label is retained. |
| [Main PDF p.6, right-column middle-baseline relapse paragraph](../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Middle baseline 25(OH)D subgroup: subdistribution HR 0.44; 95% CI 0.21–0.89; P=.02; relapse significantly lower in vitamin D group. | S009 comparator found and matched. No P value from the separate interaction or low-baseline result is substituted. |
| [Main PDF p.6, adjusted-death sentence adjacent to target](../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Adjusted death HR 0.81; 95% CI 0.48–1.36; P=.42; no significant difference. | S017 comparator found and matched; its adjacency and adjusted status are confirmed. |
| [Main PDF p.3, Statistical Analysis and post hoc analyses](../../../jama_urashima_2019_oi_190023.pdf#page=3) | REPORT | Cox proportional-hazards model determines HRs and 95% CIs; values with two-sided P<.05 are significant. Competing-risk regression uses subdistribution HRs and 95% CIs. HRs adjusted by age quartiles or stage I status are expressly post hoc. Stata14.0 named. | Relevant method, interval level, sidedness and age adjustment matched. The text does not specify the target row's named test or CI construction. |

The six result rows comprise the one target plus five supporting comparators; the comparators are not additional discrepant results. No repeated target occurrence with another printed value was registered in C007. Every registered location has been reread, including both Figure2C and its narrative copy.

**Consistency rule applicable:** Yes, with an explicit diagnostic boundary. The registered rule is symmetric log-Wald inference: b=ln(H), q=1.959963984540054, L=exp(b−q×SE), U=exp(b+q×SE), and two-sided P=2Φ(−abs(b)/SE). Joint symmetry requires H²=L×U. This calculation numerically reproduces all five other complete same-page triples, including the adjacent adjusted-death result, after allowing every input its display interval. It is not attributed to the authors as their actual method. The method names on p.3 establish outcome/model context and two-sided significance, without establishing the exact inferential construction.

**Calculation reproduced / display-precision interval check:** Yes. The target's half-unit intervals are H∈[.655,.665), L∈[.425,.435), U∈[.985,.995), and printed P∈[.0475,.0485). Allowing the HR and both CI limits jointly, rather than inserting their rounded centers separately, yields these conservative closed-bound extrema:

| Joint diagnostic extremum | H | L | U | SE | abs(b)/SE | Two-sided diagnostic P |
|---|---:|---:|---:|---:|---:|---:|
| Minimum P | .655 | .435 | .986264367816 | .208824859934 | 2.026195748348 | .042744729167580 |
| Maximum P | .655 | .431180904523 | .995 | .213324073718 | 1.983461294226 | .047315926395588 |

To confirm that these are joint extrema: for fixed H, diagnostic P increases with U; admissibility imposes U≥H²/.435. At fixed U<1, P decreases with H. On the lower-U feasibility boundary U=H²/.435, P increases with H. Thus both extrema use the minimum H=.655, with U=.995 for maximum P and L=.435 for minimum P. The feasible maximum H is additionally restricted by H²≤.435×.995; that restriction does not enlarge either bound. Closed endpoints conservatively allow more values than the actual half-open rounding intervals, so neither exclusion of the boundary .435 or .995 nor ordinary tie handling can increase the maximum.

The joint diagnostic interval **[.042744729167580,.047315926395588]** is below the printed interval [.0475,.0485). Remaining gap is **.000184073604412**; relative gap divided by printed .048 is **.003834866758583**. This small relative discrepancy is reported transparently. Under the registered Route A, category1 interval-versus-P/test rule, the general .05 relative-discrepancy exemption does not apply. The source CI excludes1 and the source P is below.05: **nominal significance agrees**, and no significance reversal is inferred.

The independently recomputed compatible examples for every supporting row are:

| Supporting relationship / printed result | Compatible unrounded H | Compatible L | Compatible U | Diagnostic P | Rounding compatibility |
|---|---:|---:|---:|---:|---|
| S001: .76 (.50–1.14); .18 | .755025 | .502246867360 | 1.135025 | .176686709753 | All four intervals satisfied |
| S002: .95 (.57–1.57); .83 | .945025 | .570644079567 | 1.565025 | .826109001109 | All four intervals satisfied |
| S003: .75 (.48–1.17); .21 | .746525 | .475025209363 | 1.173200 | .205007266743 | All four intervals satisfied |
| S009: .44 (.21–.89); .02 | .435025 | .213832095845 | .885025 | .021617031427 | All four intervals satisfied |
| S017: .81 (.48–1.36); .42 | .805025 | .477888983574 | 1.356100 | .415003737171 | All four intervals satisfied |

These are constructive numerical examples, not recovered author outputs. They confirm support for the same diagnostic calculation; they do not prove a shared actual inference method for Cox and competing-risk results.

For independent numerical verification, two-sided normal tails were computed by composite Simpson integration of the standard-normal density from the positive statistic to10, using80,000 and160,000 subintervals in JavaScript. The target extrema changed by less than3×10⁻¹⁵ when the integration resolution doubled; the comparator tails changed by less than6×10⁻¹⁴. The omitted tail beyond10 is below2×10⁻²³. The refined values agree with the independent inclusion screener; the checker's approximately4.4×10⁻⁹ normal-approximation difference is a calculation-precision refinement, not a corrected source value or location.

**Necessary inputs available:** Target HR, both CI limits, printed P, their decimal precision,95% confidence level, two-sided significance threshold, age-quartile adjustment, outcome/model attribution, and all five comparator HR/CI/P triples. These suffice for the registered bounded diagnostic and its rounding check.

**Exact missing inputs or definitions:** Actual unrounded coefficient and standard error; covariance or variance estimator; named row-specific test; test statistic and any degrees of freedom; whether the P and CI use the same test; and exact CI construction. Participant-level event/censoring data and analysis code are not supplied. Those missing inputs prevent reproducing or identifying the actual author inference, distinct from reproducing the stated diagnostic incompatibility.

**Source-grounded alternative interpretation:** The source names a Cox model,95% CI and two-sided significance without naming Wald, score or likelihood-ratio inference. A score or likelihood-ratio P with a Wald CI, a different CI construction, or a separate test could therefore explain the printed tuple. The supplied method text does not establish any such explanation. Neither Stata use nor numerical compatibility of neighboring rows is treated as proof of the actual test. No replacement P, interval or preferred method is assigned.

**Direct observation versus inferred explanation:** Direct: the target and all comparator printed tuples; age-quartile adjustment; primary relapse/death attribution;95% confidence level; two-sided threshold; and lack of a named target-row inferential construction in the cited methods. Recomputed: joint diagnostic interval separation and compatible comparator examples. Inferred only: a common actual log-Wald method, a mixed CI/test construction, a separate test or a production mechanism. None of those inferred explanations is asserted as fact.

**Classification confirmation:** Every compared location is trial methods or trial results within one main article, therefore REPORT by content. The comparison is internal to that one REPORT: **Primary relationship type: S_W**; **All relationships: S_W**; **Review domain: statistical_results**, because the issue concerns estimate/interval/test logic. No PLAN is a conflicting side and no second REPORT document is compared. Precedence is unambiguous with only S_W. Classification ambiguity: none for role/type/domain; actual inferential construction is a bounded evidence limitation. No classification correction.

**Evidence state: reproduced.** Determining fact: exact source rereading confirms all registered printed values and locations, and the joint rounding diagnostic does not yield a P in the printed [.0475,.0485) interval, while the five supporting rows have compatible solutions. Source transcription required no correction. The diagnostic nature, method alternatives and unchanged nominal significance remain explicit limits of this evidence fact; they do not become an AI disposition.

**Exact remaining human question:** Which confidence-interval and two-sided test constructions, and which unrounded coefficient/standard error or test statistic, jointly produced the age-quartile-adjusted relapse/death HR.66,95% CI.43–.99 and P=.048?

**Completion:** One assigned stable ID, C007, covered in full; seven cited source-location groups found; target plus all five comparison triples matched; both Figure2C and its narrative copy checked; diagnostic reproduced with independent interval bounds; classification confirmed without correction. Remaining unresolved item: the actual row-specific inferential construction and unrounded outputs named above. No scientific-coverage gap in this assigned scope. Pending Human Adjudication.
