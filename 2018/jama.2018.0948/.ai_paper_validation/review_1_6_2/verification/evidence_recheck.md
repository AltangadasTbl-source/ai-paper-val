# Independent Direct-Source Evidence Recheck — Workflow 1.6.2

Runtime ID: 01a129cc-2272-79d1-9061-1f09b51d95da. Fresh gpt-6.1-sol/high evidence rechecker. Exact assigned stable scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012. All remain Pending Human Adjudication. This artifact records evidence facts and classification; it assigns no human disposition.

The complete START_PROMPT.md, QUALITY_CONTROL_SCOPE.md, PERFORMANCE_PROFILE.md, review_contract.md, report_spec.md and settings.toml were read. The current ledger, independent screen and current evidence maps supplied the frozen comparisons and locators. No earlier-run candidate conclusions or external evidence were used. Current supplied PDF pages were visually inspected as final authority; text/maps were locators and coverage aids. Each occurrence below is separately confirmed, including repeated-pattern locations and corroborating-only locations.

## Recheck provenance and absence coverage

Compute device: CPU, as recorded in tooling_record.md. Direct engines: Poppler pdftoppm and pdftotext 25.03.0. No OCR, Office conversion or fallback environment was used. No source or reused asset was changed. New derivatives are confined to preprocessing/.

Current-source-confirmed renders reused and visually read: screen-main4.png, screen-main5.png, screen-main6.png, screen-main7.png; screen-protocol12.png, screen-protocol14.png, screen-protocol16.png, screen-protocol24.png, screen-protocol29.png; screen-sap1.png through screen-sap6.png; screen-results6.png, screen-results12.png; sap-results-DOC004-p2.png and sap-results-DOC004-p4.png. Their production engines/device are recorded in the current screen/map artifacts; these are current-review direct-source renders, not independent scientific authority apart from the supplied pages they faithfully render.

| Supplied source units | Fresh derivative paths | Engine/device and command pattern |
|---|---|---|
| Main physical pages 1, 2, 3, 8, 9, 10, 11 | preprocessing/recheck-main1.png, preprocessing/recheck-main2.png, preprocessing/recheck-main3.png, preprocessing/recheck-main8.png, preprocessing/recheck-main9.png, preprocessing/recheck-main10.png, preprocessing/recheck-main11.png | Poppler pdftoppm 25.03.0; CPU; `pdftoppm -f N -l N -r 110 -singlefile -png jama_parshuram_2018_oi_180015.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck-mainN` |
| Protocol physical pages 1, 10, 11 | preprocessing/recheck-protocol1.png, preprocessing/recheck-protocol10.png, preprocessing/recheck-protocol11.png | Poppler pdftoppm 25.03.0; CPU; same rendering options with joi180015supp1_prod.pdf |
| Results physical pages 1, 3, 5, 7, 8, 9, 10, 11, 13, 14 | preprocessing/recheck-results1.png, preprocessing/recheck-results3.png, preprocessing/recheck-results5.png, preprocessing/recheck-results7.png, preprocessing/recheck-results8.png, preprocessing/recheck-results9.png, preprocessing/recheck-results10.png, preprocessing/recheck-results11.png, preprocessing/recheck-results13.png, preprocessing/recheck-results14.png | Poppler pdftoppm 25.03.0; CPU; same rendering options with joi180015supp3_prod.pdf |
| Complete main physical pages 1–11 | preprocessing/recheck-main-complete.txt | Poppler pdftotext 25.03.0; CPU; `pdftotext -layout jama_parshuram_2018_oi_180015.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck-main-complete.txt` |
| Complete results physical pages 1–14 | preprocessing/recheck-results-complete.txt | Poppler pdftotext 25.03.0; CPU; same complete-layout command with joi180015supp3_prod.pdf |
| SAP physical page 7 | preprocessing/recheck-sap7.txt | Poppler pdftotext 25.03.0; CPU; `pdftotext -layout -f 7 -l 7 joi180015supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck-sap7.txt` |

Absence comparisons C005, C006, C007, C009 and C012 use the complete current main/results maps, complete fresh layout extractions, searches for subgroup, interaction, sensitivity, model, DNR, mixed, GLMER, quasi and weighted, and visual inspection of every main/results physical page. Main pages 1–2 contain abstract, Key Points and design; page 3 contains flow/documentation; pages 4–5 contain definitions, methods and baseline table; pages 6–7 contain documentation and treatment-effect results; page 8 contains hospital-mortality graph and other outcomes; page 9 contains discussion/limitations; pages 10–11 contain contributions and references. Results page 1 lists its contents; pages 2–3 show mortality graph/caption; pages 4–5 documentation graph/caption; pages 6–8 definitions; pages 9–10 all-cause/non-DNR descriptive hospital mortality; page 11 descriptive SCDE/arrest results; pages 12–13 per-patient ICU outcomes and methods; page 14 power assumptions/post-trial calculations. Neither full report contains a subgroup/interaction effect set, alternative-model sensitivity effect set, original size-stratified weighted hospital-logit primary output, or modeled following-DNR mortality output. The already reported baseline-adjusted GEE and identity-link fallback results are explicitly excluded from claims of absent outputs.

By content, the main article and results definitions/results are REPORT. Protocol version 005 dated 23 February 2011 and SAP analysis specifications are PLAN. The SAP is undated and mixes retrospective model wording with prospective subgroup wording; PLAN classification does not establish when it was adopted. Supplemental filenames do not determine document roles.

## Final classification handoff

No source-value or cited-source-location transcription correction was needed for any registered ID. The C010 auxiliary baseline-rate arithmetic is refined below; it is not a change to a source value/location. All 12 evidence states are reproduced. The classification fields below agree with the frozen ledger; no relationship/domain correction is needed.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article SCDE interval vs REPORT main article P value (pp. 1, 6, 7) | reproduced |
| C002 | protocol_report | P_R | P_R | PLAN protocol pp. 12, 14, 16 vs REPORT main article pp. 3, 4, 6 | reproduced |
| C003 | protocol_report | P_R | P_R, S_C | PLAN protocol pp. 10, 11, 24 vs REPORT main article p. 4 and REPORT results supplement p. 6 | reproduced |
| C004 | protocol_report | P_R | P_R, S_W | PLAN protocol pp. 11, 12, 16 and PLAN SAP p. 5 vs REPORT main article pp. 4, 7 | reproduced |
| C005 | protocol_report | P_R | P_R, P_P | PLAN protocol p. 16 vs PLAN SAP pp. 1-4 and REPORT main article pp. 4, 5, 7 | reproduced |
| C006 | protocol_report | P_R | P_R | PLAN protocol p. 16 and PLAN SAP pp. 2, 3 vs REPORT main article pp. 5, 7 | reproduced |
| C007 | protocol_report | P_R | P_R | PLAN protocol p. 16 and PLAN SAP p. 6 vs REPORT main article p. 5 and complete REPORT result set | reproduced |
| C008 | statistical_results | S_W | S_W | REPORT main article p. 6 respiratory-rate interval vs REPORT main article p. 6 Holm-adjusted P value; significance rule p. 5 | reproduced |
| C009 | protocol_report | P_R | P_R | PLAN protocol pp. 10, 16 vs REPORT main article pp. 6, 7, 9 and complete REPORT result set | reproduced |
| C010 | protocol_report | P_R | P_R, P_P | PLAN protocol p. 12 vs PLAN SAP p. 5 and REPORT main article p. 7 | reproduced |
| C011 | plan_material | P_P | P_P | PLAN protocol p. 14 mortality power input vs PLAN protocol p. 29 power appendix | reproduced |
| C012 | protocol_report | P_R | P_R | PLAN SAP pp. 4, 5 vs REPORT main article pp. 4-7 and complete REPORT results supplement | reproduced |

## C001 — SCDE absolute-effect interval and displayed P value give different null readings

**Evidence state:** reproduced

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article SCDE interval vs REPORT main article P value (pp. 1, 6, 7).

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| REPORT [main p.1 abstract Results](../../../jama_parshuram_2018_oi_180015.pdf#page=1) | Yes. RD −0.34, 95% CI −0.73 to 0.05; adjusted RR 0.77, 95% CI 0.61 to 0.97; P=.03. The final P value follows the ratio in a sentence also presenting the absolute effect; the source does not expressly identify it as a separate RD test. |
| REPORT [main p.6 Secondary Outcome](../../../jama_parshuram_2018_oi_180015.pdf#page=6) | Yes. 386 events (127 versus 259), rates 0.50 versus 0.84 per 1000 patient-days, P=.03; baseline-adjusted RR 0.77 (0.61–0.97), RD −0.34 (−0.73–0.05). |
| REPORT [main p.7 Table 3 SCDE row and footnotes a/f](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | Yes. Same RD, ratio, intervals and P. Footnote a explicitly says SCDE RD is not adjusted for baseline; footnote f describes baseline-adjusted Poisson ratio with hospital clustering. |
| REPORT [main p.5 significance methods](../../../jama_parshuram_2018_oi_180015.pdf#page=5) | Yes. Two-sided P=.05 regarded as significant. |

- **Consistency rule applicable:** Route A category 1, interval versus P/test. For a zero-null RD, the displayed 95% interval includes zero, while P=.03 is below .05. This records the differing null readings, without asserting that the source explicitly gives an RD-specific P value.
- **Calculation/logical comparison and display precision:** −0.73 < 0 < 0.05; .03 < .05. RR 0.77 lies within 0.61–0.97, entirely below 1, and agrees with .03. Endpoint bounds [−0.735,−0.725] and [0.045,0.055], and P bounds [.025,.035], retain the distinct readings. Route A category 1 is exempt from the relative .05 rounding exclusion.
- **Necessary inputs available:** Printed 95% level, both estimates/intervals, P value, .05 threshold and model/adjustment footnotes suffice for the stated comparison. **Exact missing inputs/definitions:** A separate absolute-effect P value/test and fitted-model covariance/test output are absent; these prevent assigning .03 to the RD or reconstructing its exact test.
- **Source-grounded alternative interpretation:** The .03 P value belongs to the baseline-adjusted RR, and the non-baseline-adjusted RD interval belongs to a different analysis. Table 3 and the abstract's ordering strongly support this interpretation. Category 1 expressly retains comparisons accompanied by different-analysis explanations.
- **Direct observation versus inferred explanation:** The numerical readings and differing adjustment labels are direct observations. Attributing .03 solely to the RR is a supported interpretation rather than a separately printed RD-test definition. No mechanism behind the pairing is inferred.
- **Classification confirmation:** Both compared inferential elements occur in one REPORT document, giving S_W and statistical_results. Supplementary event counts corroborate the outcome and add no conflicting relationship. No correction; ambiguity None.
- **Determining recheck fact:** All three report occurrences contain an absolute interval spanning zero alongside .03 and a ratio interval excluding 1; the registered distinct-reading comparison is reproduced with the alternative retained.
- **Exact remaining human question:** Which test applies to the absolute SCDE difference, and should P=.03 be extracted only with the relative effect?

## C002 — Planned all-seven documentation analysis is replaced by last-set ≥5 completeness

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp.12,14,16 vs REPORT main pp.3,4,6.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [protocol p.12 documentation process outcome](../../../joi180015supp1_prod.pdf#page=12) | Yes. Frequency of vital signs and other score components in 24 hours, randomly selected patients each week. |
| PLAN [protocol p.14 documentation measurement](../../../joi180015supp1_prod.pdf#page=14) | Yes. Number of each component documented in the preceding 24 hours. |
| PLAN [protocol p.16 documentation analysis](../../../joi180015supp1_prod.pdf#page=16) | Yes. Compare individual component counts and number of times all seven items were documented. |
| REPORT [main p.3 final methods paragraph](../../../jama_parshuram_2018_oi_180015.pdf#page=3) | Yes. Documentation-completeness analysis revised from protocol method before analyses. |
| REPORT [main p.4 continuation](../../../jama_parshuram_2018_oi_180015.pdf#page=4) | Yes. Last set replaces all sets; threshold reduced from 7 to 5 for minimum score-calculation requirements. |
| REPORT [main p.6 Table 2 row/footnotes](../../../jama_parshuram_2018_oi_180015.pdf#page=6) | Yes. Observation sets with ≥5 vital signs; effect 38.1 (20.8–55.4), P<.001; last-set abstraction described in footnote a. |
| REPORT corroboration [results p.4 eFigure 2](../../../joi180015supp3_prod.pdf#page=4) and [p.5 caption](../../../joi180015supp3_prod.pdf#page=5) | Both found. Graph uses most recent documentation and caption describes last set and ≥5 threshold; corroborates reported definition without conflicting with it. |

- **Consistency rule applicable:** Route A category 5, changed prespecified constructed endpoint/analysis definition, focus D.
- **Calculation/logical comparison and display precision:** A last set with 5 or 6 components satisfies reported ≥5 but fails all-seven membership; counting all sets differs from classifying a single last set. Integer definition cutoffs are exact specifications, not rounded numerical estimates. No relative discrepancy interval applies to this categorical replacement. The 38.1 effect is an affected result, not a crude subtraction challenge.
- **Necessary inputs available:** Both operational definitions and explicit revision statement suffice. **Exact missing inputs/definitions:** Dated revision/amendment, planned all-seven/all-set effect and patient-level observation-set data are absent; these prevent quantifying change in membership or comparing fitted effects.
- **Source-grounded alternative interpretation:** A clinically justified prospective revision may have been made; the report expressly discloses that it preceded analysis and explains the minimum score requirement.
- **Direct observation versus inferred explanation:** Replacement and rationale are printed. No claim is made about when relative to access to outcomes it occurred, affected sample count, or changed effect magnitude.
- **Classification confirmation:** Prospective protocol specification is PLAN and published constructed outcome is REPORT; P_R → protocol_report. The results figure/caption agrees with the main report and adds no S_C. No correction. Ambiguity: revised before analysis, formal dated amendment unavailable.
- **Determining recheck fact:** Main explicitly identifies both changes against the protocol and prints the revised endpoint's effect; categorical definitions remain distinct.
- **Exact remaining human question:** What prospective amendment establishes last-set ≥5 completeness, and is the planned all-seven/all-set comparison available?

## C003 — SCDE composite components differ between protocol and report, with a report fluid-boundary difference

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** PLAN protocol pp.10,11,24 vs REPORT main p.4 and REPORT results p.6.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [protocol p.10 main-secondary definition](../../../joi180015supp1_prod.pdf#page=10) | Yes. Composite uses therapies around transfer and death without DNR on inpatient ward; points to Table 5. The one-hour post-transfer window for therapies does not redefine the explicit ward-death row. |
| PLAN [protocol p.11 continuation/clinical deterioration](../../../joi180015supp1_prod.pdf#page=11) | Yes. Deterioration scale and first-hour interventions described; no printed replacement of Table 5 ward-death membership. |
| PLAN [protocol p.24 Table 5 category 4](../../../joi180015supp1_prod.pdf#page=24) | Yes. >60 mL/kg fluid in preceding 12 h **and** any inotrope/vasopressor at transfer or preceding 12 h. |
| PLAN [protocol p.24 Table 5 category 7](../../../joi180015supp1_prod.pdf#page=24) | Yes. Death on inpatient ward without DNR; no transfer from ward. |
| REPORT [main p.4 SCDE definition](../../../jama_parshuram_2018_oi_180015.pdf#page=4) | Yes. One-or-more composite, vasoactive medication **or** fluids 60 mL/kg **or greater**; also death within first hour of ICU admission. |
| REPORT [results p.6 eTable 1](../../../joi180015supp3_prod.pdf#page=6) | Yes. >60 mL/kg fluid **and/or** inotrope/vasopressor; death on ward **or within an hour** of urgent ICU admission without DNR. |
| Affected outputs: REPORT [main p.1](../../../jama_parshuram_2018_oi_180015.pdf#page=1), [p.7 Table 3](../../../jama_parshuram_2018_oi_180015.pdf#page=7), [results p.11 eTable 3](../../../joi180015supp3_prod.pdf#page=11) | All found. Main RR 0.77 (0.61–0.97), RD −0.34 (−0.73–0.05); main/supplement events 127 versus 259, total 386. These are affected-output occurrences rather than additional definition conflicts. |

- **Consistency rule applicable:** Route A category 5, changed composite definition, focus D.
- **Calculation/logical comparison and display precision:** Fluid-only or vasoactive-only cases satisfy OR membership but fail category-4 AND membership, unless another component independently qualifies. A first-hour ICU death without other qualifying components satisfies reported death membership but fails planned ward-only category 7. Exactly 60 meets main ≥60 but not results >60. These are exact logical definitions; rounding interval arithmetic does not make AND equal OR or exact threshold cutoffs identical. No boundary-case count is inferred.
- **Necessary inputs available:** Complete composite definitions and affected aggregate outputs suffice to reproduce the definition contrast. **Exact missing inputs/definitions:** Event-level component memberships, exact fluid doses, ICU death timing and dated amendment/operational-rule records are absent; aggregate counts cannot quantify the impact or establish the applied rule.
- **Source-grounded alternative interpretation:** A later amendment may govern; main threshold may summarize the detailed table; some first-hour deaths may already meet another SCDE component. These possibilities bound numerical impact but do not equate all printed memberships.
- **Direct observation versus inferred explanation:** Changed membership language and ≥60/>60 are printed. Any actual event addition/removal, operational protocol, or production mechanism is unknown.
- **Classification confirmation:** Protocol definitions are PLAN; main and non-plan result definitions are REPORT. PLAN–REPORT contrasts give P_R, main–results threshold contrast gives S_C. P_R has precedence and domain protocol_report. No correction. Ambiguity: amendment timing and analyzed membership unavailable.
- **Determining recheck fact:** Every cited composite location contains the registered AND/OR, ward/ICU death or fluid-boundary statement; no source transcription change is needed.
- **Exact remaining human question:** Which circulatory combination, fluid boundary and death-location window generated the analyzed SCDE events, and where is the corresponding prespecified or amended definition?

## C004 — Planned secondary outcome/analysis status differs from reported post-hoc or nonprespecified status

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_W

**Compared document roles:** PLAN protocol pp.11,12,16 and PLAN SAP p.5 vs REPORT main pp.4,7.

| Pattern occurrence and exact supplied-source locations | Location found; source/comparator matched |
|---|---|
| Potentially preventable arrest: PLAN [protocol p.11 secondary outcome 2](../../../joi180015supp1_prod.pdf#page=11); REPORT [main p.4 prespecified list](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.7 Post hoc Outcomes](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | All found. Named secondary/planned outcome is also main-prespecified, while its Table 3 result is under Post hoc Outcomes. |
| ICU readmission <48 h: PLAN [protocol p.12 outcome 4](../../../joi180015supp1_prod.pdf#page=12); REPORT [main p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | All found. Planned/prespecified outcome appears under post-hoc heading. Denominator comparison belongs separately to C010. |
| Hospital readmission <48 h: PLAN [protocol p.12 outcome 3](../../../joi180015supp1_prod.pdf#page=12); REPORT [main p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | All found. Planned/prespecified outcome appears under post-hoc heading. |
| Immediate resuscitation-team calls: PLAN [protocol p.12 process outcome 2](../../../joi180015supp1_prod.pdf#page=12); REPORT [main p.4 process list](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | All found. Planned process outcome matches displayed post-hoc named outcome. |
| Immediate physician calls: PLAN [protocol p.12 process outcome 1](../../../joi180015supp1_prod.pdf#page=12); REPORT [main p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | All found. Planned stat calls match immediate physician calls and the displayed post-hoc named outcome. |
| Urgent ICU consultations: PLAN [protocol p.12 process outcome 3](../../../joi180015supp1_prod.pdf#page=12); REPORT [main p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | All found. Planned new urgent ICU/MET consultation corresponds to displayed urgent <15-minute ICU consultation under post-hoc heading. |
| PIM2 score analysis: PLAN [protocol p.16 continuous model list item c](../../../joi180015supp1_prod.pdf#page=16); REPORT [main p.4 nonprespecified list](../../../jama_parshuram_2018_oi_180015.pdf#page=4) | Both found. Protocol expressly names PIM2 score, whereas main says PIM2 score at ICU admission was not prespecified. It is distinct from PIM2 predicted mortality. |
| PIM2 analyzed-score corroboration: REPORT [results p.12 eTable 4](../../../joi180015supp3_prod.pdf#page=12) | Found. Score difference 0.13 (−0.11–0.37), P=.29; makes no independent status claim and adds no S_C. |
| Overall ICU mortality on both displayed denominator scales: REPORT [main p.4 prespecified overall/urgent mortality list](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.7 first two post-hoc rows](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | Both found. Overall ICU mortality is main-prespecified and main-post-hoc on ICU-discharge and hospital-discharge scales: this supplies S_W. It is not equated with protocol urgent-admission mortality. |
| Urgent ICU admissions: PLAN [SAP p.5 shell row](../../../joi180015supp2_prod.pdf#page=5); REPORT [main p.4 not-prespecified list](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.7 post-hoc row](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | All found. Shell row contains the named analysis; main calls outcome nonprespecified/post-hoc. Undated SAP timing limits the temporal interpretation. |
| REPORT [main p.7 footnote g](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | Found. Post-hoc outcomes exploratory; Holm-adjusted P values >.99 for these 10. This is interpretation context, not an additional timing contrast. |

- **Consistency rule applicable:** Route A category 5, changed outcome/analysis status, focus D. Repeated named status contrasts are one candidate; unsupported population matches are not added.
- **Calculation/logical comparison and display precision:** Exact matched named outcomes/score are planned or main-prespecified yet described as post hoc/not prespecified. This categorical status comparison has no half-unit numeric interval. Numeric result values merely identify the affected analyses.
- **Necessary inputs available:** Plan status, explicit score analysis, main status lists, Table 3 heading and footnote suffice. **Exact missing inputs/definitions:** Whether status denotes collection, model selection or multiplicity treatment; dated SAP/adoption/amendment sequence; per-analysis status register. These prevent inferring original-plan timing for the SAP shell row.
- **Source-grounded alternative interpretation:** Post hoc may refer to analysis model or multiplicity treatment rather than outcome collection; SAP may document a later specification. Such interpretation needs the missing status definition, rather than equating different ICU populations.
- **Direct observation versus inferred explanation:** Names/headings/status words are printed. Their intended timing referent and adoption sequence are not established. No prospective timing is inferred from an undated SAP.
- **Bounded occurrences preserved:** Protocol urgent-ICU mortality and results urgent-ICU mortality agree in population; no independent post-hoc contrast is assigned to that pair. Mortality without DNR under Primary Outcome is compatible with primary-family sensitivity and is not a claimed outcome-status elevation. Overall cardiac arrest lacks a matched explicit planned status and is not independently registered within this pattern.
- **Classification confirmation:** PLAN–REPORT status comparisons give P_R; main p.4 versus Table 3 gives S_W for the matched main-prespecified occurrences, including overall ICU mortality. P_R takes precedence → protocol_report. Corroborating score output adds no S_C. No correction. Ambiguity: status referent and SAP timing remain bounded.
- **Determining recheck fact:** Every retained occurrence is found with its stated status contrast; narrowed population/status exclusions remain outside the reproduced pattern.
- **Exact remaining human question:** For each matched result, does post hoc/nonprespecified refer to the outcome, analysis model or multiplicity treatment, and what dated specification establishes PIM2-score and urgent-admission analysis status?

## C005 — Protocol weighted hospital-logit primary analysis differs from SAP/reported GEE specification

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol p.16 vs PLAN SAP pp.1–4 and REPORT main pp.4,5,7.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [protocol p.16 primary analysis](../../../joi180015supp1_prod.pdf#page=16) | Yes. Response is logit of hospital mortality proportion; treatment, baseline mortality logit, hospital-size stratum; weighted by hospital size. |
| PLAN [protocol p.16 secondary model paragraphs](../../../joi180015supp1_prod.pdf#page=16) | Yes. Identical primary logit for named secondary mortality/readmission; hospital-level Poisson counts with baseline/size stratum; within-hospital mean continuous model, baseline/size stratum and hospital-size weights. Documentation also retains baseline and strata, without hospital-size weighting because equal sample counts. |
| PLAN [SAP p.1 model/predictors](../../../joi180015supp2_prod.pdf#page=1) and [p.2 binary code](../../../joi180015supp2_prod.pdf#page=2) | Both found. Binomial exchangeable hospital GEE; treatment plus baseline; cbind(x,n−x) response. No size-stratum predictor in the shown model. |
| PLAN [SAP p.3 count code](../../../joi180015supp2_prod.pdf#page=3) and [p.4 individual continuous GEE](../../../joi180015supp2_prod.pdf#page=4) | Both found. Hospital GEE count specification; individual continuous model with intervention plus hospital baseline mean and clustering. No size-stratum predictor is listed. |
| REPORT [main p.4 GEE methods](../../../jama_parshuram_2018_oi_180015.pdf#page=4) | Yes. Exchangeable center GEE; binary logistic, count Poisson, continuous Gaussian. |
| REPORT [main p.5 predictors/analysis units and strata](../../../jama_parshuram_2018_oi_180015.pdf#page=5) | Yes. Two predictors: treatment and center baseline value; patient-level urgent ICU analyses; planned stratification removed because only 3 hospitals had >200 eligible beds. |
| REPORT [main p.7 primary output](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | Yes. OR 1.01 (0.61–1.69), P=.96; RD 0.01 (−0.80–0.81), footnotes specify GEE/adjustment. |

- **Consistency rule applicable:** Route A category 5, replacement/nonreporting of planned primary analysis; linked common model/size-stratum changes remain one pattern, focus D.
- **Calculation/logical comparison and display precision:** Printed response/model descriptions and predictor sets differ: planned size-stratum covariate is removed; primary hospital-logit weighted specification is replaced by binomial GEE and two predictors. Associated count/continuous specifications follow the same pattern. This is a specification comparison, not a reconstructed effect. Display precision is inapplicable to covariate/model membership. No comparison of adjusted estimates to crude effects is used.
- **Necessary inputs available:** Plan equations/descriptions, SAP formulas and main implementation/removal statement suffice. Complete REPORT coverage finds no original weighted/stratified primary result. **Exact missing inputs/definitions:** Dated adopted analysis specification, model weight details/equivalence, code actually executed and original-model output; without these one cannot infer numerical weight equivalence or impact.
- **Source-grounded alternative interpretation:** SAP could be approved later revision; GEE could be treated as a related implementation of a broad logit description. Stratification removal is disclosed. No preferred model is proposed.
- **Direct observation versus inferred explanation:** Predictor/model changes and removal reason are printed; fitted-effect change or equivalence of weighting is not established. C006 separately concerns SCDE RD baseline removal and is not duplicated here.
- **Classification confirmation:** Protocol and SAP model descriptions are PLAN; main specification/output is REPORT. Protocol–main gives P_R, protocol–SAP gives P_P, with P_R precedence → protocol_report. SAP/main agreement is corroboration, not another conflicting relationship. No correction. Ambiguity: undated SAP and unestablished weight equivalence/adoption sequence.
- **Determining recheck fact:** Direct plan/report specifications contain the different responses/predictor sets and explicit stratification removal; original planned primary output is absent from the complete supplied REPORT set.
- **Exact remaining human question:** What dated analysis specification governs the primary result, and how were the planned hospital-logit response, hospital weights and size stratum changed or implemented in the reported GEE?

## C006 — Key-secondary SCDE absolute-effect analysis omits SAP baseline adjustment

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p.16 and PLAN SAP pp.2,3 vs REPORT main pp.5,7.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [SAP p.2 count identity introduction](../../../joi180015supp2_prod.pdf#page=2) | Yes. Count GEE Poisson, log and identity analyses both including person-time; next-page predictors apply to both. |
| PLAN [SAP p.3 count predictors and identity code](../../../joi180015supp2_prod.pdf#page=3) | Yes. Intervention and hospital baseline rate; identity fit contains Nlin, GNlin and BNlin. |
| PLAN corroboration [protocol p.16 SCDE model](../../../joi180015supp1_prod.pdf#page=16) | Yes. SCDE Poisson analysis includes baseline event rate. General corroboration of baseline adjustment; does not separately define the SAP identity-scale model. |
| REPORT [main p.5 fallback](../../../jama_parshuram_2018_oi_180015.pdf#page=5) | Yes. If identity-link GEE fails to converge, differences/intervals use corresponding model without baseline adjustment. |
| REPORT [main p.7 SCDE row and footnotes a/f](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | Yes. Footnote a explicitly excludes baseline adjustment for SCDE difference −0.34 (−0.73–0.05); ratio 0.77 (0.61–0.97) remains baseline adjusted. |
| REPORT affected output [main p.1 abstract](../../../jama_parshuram_2018_oi_180015.pdf#page=1) | Yes. RD −0.34 (−0.73–0.05); adjusted label does not by itself create S_W because hospital clustering still applies. |

- **Consistency rule applicable:** Route A category 5, replaced planned key-secondary absolute-effect specification, focus D.
- **Calculation/logical comparison and display precision:** Planned identity-rate covariates include baseline, while the printed SCDE RD footnote excludes it. The baseline-adjusted ratio does not provide a baseline-adjusted absolute effect. Covariate inclusion is categorical; no numeric discrepancy interval applies. Complete seven-page SAP reading finds no baseline-removal/nonconvergence fallback statement.
- **Necessary inputs available:** Planned predictors and explicit row-level adjustment footnote suffice. **Exact missing inputs/definitions:** SCDE identity-model convergence output, prospective fallback amendment, and planned adjusted-RD estimate/interval. Their absence prevents reproducing the fitted alternatives or asserting which fit failed.
- **Source-grounded alternative interpretation:** Main gives nonconvergence as the fallback rationale; it may have been prospectively approved outside the supplied plan. The statement explains a change without supplying dated adoption/convergence records.
- **Direct observation versus inferred explanation:** Baseline specification/omission and general fallback rule are directly printed. SCDE-specific nonconvergence is inferred from their combination, not supplied as a separate fit log.
- **Classification confirmation:** SAP model is PLAN, published fit/footnote REPORT; P_R → protocol_report. Protocol only corroborates baseline intent; no P_P is established. No additional S_W from adjusted wording. No correction. Ambiguity: timing of fallback and exact fit/convergence facts.
- **Determining recheck fact:** SAP retains the baseline predictor in its identity-rate model and main explicitly identifies the SCDE RD as without baseline adjustment.
- **Exact remaining human question:** Was baseline-removal fallback prospectively specified for the SCDE RD, and which SCDE fit/convergence facts explain replacement of the SAP baseline-adjusted absolute-effect model?

## C007 — Planned subgroup analyses of primary/key-secondary effects are not supplied

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p.16 and PLAN SAP p.6 vs REPORT main p.5 and complete REPORT result set.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [protocol p.16 A-priori Subgroup analyses](../../../joi180015supp1_prod.pdf#page=16) | Yes. Four planned subgroup analyses: <200/≥200 eligible ward beds; with/without medical emergency teams; with/without ECMO; ward-initiated urgent PICU admission. |
| PLAN [SAP p.6 Subgroup Analysis Plan](../../../joi180015supp2_prod.pdf#page=6) | Yes. ECMO and MET groups; treatment effect within each, single GEE with one-term treatment-by-subgroup interaction. |
| REPORT [main p.5 statement spanning columns](../../../jama_parshuram_2018_oi_180015.pdf#page=5) | Yes. Four planned subgroup analyses including with/without rapid response teams were described in protocol, but are not reported herein. |
| Complete REPORT main [p.1](../../../jama_parshuram_2018_oi_180015.pdf#page=1) through [p.11](../../../jama_parshuram_2018_oi_180015.pdf#page=11); results [p.1](../../../joi180015supp3_prod.pdf#page=1) through [p.14](../../../joi180015supp3_prod.pdf#page=14) | Every physical page visually inspected and complete current maps/layout searched. No subgroup treatment estimates/intervals or MET/ECMO interaction tests appear. Baseline service counts and hospital-specific descriptive tables/graphs are not subgroup treatment effects. |

- **Consistency rule applicable:** Route A category 5, planned primary/key-secondary subgroup outputs not reported, focus D.
- **Calculation/logical comparison and display precision:** Specified treatment-effect/interaction analyses are compared with the complete supplied output set and explicit nonreporting statement. No absent effect is numerically reconstructed; half-unit arithmetic is inapplicable to absence. Do not invent a four-by-all-outcomes matrix: subgroup outcome assignment is not fully spelled out for every protocol subgroup.
- **Necessary inputs available:** Planned subgroup list/method and complete REPORT output set suffice for supplied-output absence. **Exact missing inputs/definitions:** Subgroup estimates/intervals/tests; exact outcomes for every planned subgroup; date/adoption of narrower SAP specification; amendment/removal rationale.
- **Source-grounded alternative interpretation:** Analyses may exist in a separate publication or may have been deferred/revised. Size-stratum removal from adjusted models does not provide missing subgroup analyses. Only absence within the supplied package is established.
- **Direct observation versus inferred explanation:** Main's nonreporting statement and SAP's specific treatment/interaction requirements are printed. Whether the analyses were performed, their findings and why absent are unknown.
- **Classification confirmation:** Planned subgroup specification is PLAN; nonreporting/output set REPORT. P_R → protocol_report. The narrower SAP list alone does not contradict protocol or establish P_P. No correction. Ambiguity: undated SAP and outcome-specific subgroup scope.
- **Determining recheck fact:** Explicit planned analyses and main nonreporting statement coexist; exhaustive supplied REPORT inspection provides no corresponding effect/interaction results.
- **Exact remaining human question:** Which planned primary/key-secondary subgroup effects and MET/ECMO interactions were performed, where are their outputs, and which prospective change explains any omission?

## C008 — Respiratory-rate interval excludes zero while Holm-adjusted P is nonsignificant

**Evidence state:** reproduced

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main p.6 respiratory-rate interval vs REPORT main p.6 Holm-adjusted P value; significance rule p.5.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| REPORT [main p.6 Table 2 respiratory-rate row](../../../jama_parshuram_2018_oi_180015.pdf#page=6) | Yes. Mean difference 0.85, 95% CI 0.02–1.68; raw P=.05; adjusted P=.18. |
| REPORT [main p.6 Table 2 footnotes c/d](../../../jama_parshuram_2018_oi_180015.pdf#page=6) | Yes. Difference from baseline/hospital-adjusted GEE; adjusted P from Holm procedure. |
| REPORT [main p.5 significance/multiplicity](../../../jama_parshuram_2018_oi_180015.pdf#page=5) | Yes. Two-sided .05 threshold; post-hoc Holm applied to 21 prespecified outcomes. |

- **Consistency rule applicable:** Route A category 1, interval versus P/test, focus B; distinct multiplicity adjustments remain an explicit alternative under this rule.
- **Calculation/logical comparison and display precision:** 0.02 > 0 so displayed 95% interval excludes zero; .18 > .05 so adjusted test is nonsignificant. Lower-limit bounds [.015,.025] remain positive, upper-limit bounds [1.675,1.685] remain positive, and adjusted-P bounds [.175,.185] remain above .05. Category 1 does not use the relative .05 rounding exclusion. Raw P=.05 lies in [.045,.055] and is not independently claimed to conflict. Optional normal-Wald diagnostic: half-width .83/1.96 gives SE≈.4235 and z≈2.007; its raw P near .045 is compatible with displayed .05. This is not a reconstruction of the reported GEE test.
- **Necessary inputs available:** CI level, null, adjusted P, threshold and procedure labels suffice. **Exact missing inputs/definitions:** Multiplicity-adjusted confidence interval and exact fitted-model test output/family ranking. These prevent rebuilding the adjusted interval or exact Holm calculation.
- **Source-grounded alternative interpretation:** The interval is marginal/unadjusted for multiplicity while .18 is Holm-adjusted. Table labels explicitly distinguish the P columns; no source claim of a family-adjusted CI is made.
- **Direct observation versus inferred explanation:** Differing null readings and Holm label are printed. Unadjusted-CI attribution is supported by labels but not printed as an explicit adjustment qualifier on the interval; diagnostic approximation is separately identified.
- **Classification confirmation:** All compared inferential elements are in one REPORT document; S_W → statistical_results. No PLAN comparator or extra relationship. No correction; ambiguity None.
- **Determining recheck fact:** Exact Table 2 row shows a positive lower 95% bound and Holm P=.18, with different multiplicity adjustment retained.
- **Exact remaining human question:** Is the displayed 95% interval intended solely for the unadjusted inference, and which interval/test pairing should accompany Holm-adjusted P=.18 in extraction?

## C009 — Planned mortality-following-DNR sensitivity is not matched by displayed mortality-without-DNR output

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp.10,16 vs REPORT main pp.6,7,9 and complete REPORT result set.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [protocol p.16 secondary analysis d](../../../joi180015supp1_prod.pdf#page=16) | Yes. An identical primary logit model for all-cause mortality following DNR orders. |
| PLAN [protocol p.10 primary-outcome rationale](../../../joi180015supp1_prod.pdf#page=10) | Yes. Frequency of DNR orders and analyses of patients with and without DNR are planned. This broader rationale is retained. |
| REPORT [main p.6 Primary Outcome](../../../jama_parshuram_2018_oi_180015.pdf#page=6) | Yes. 244 hospital deaths, 155 after DNR; displayed comparative sensitivity is mortality without DNR, OR 2.05 (0.64–6.61), P=.23, RD 0.36 (−0.53–1.25). |
| REPORT [main p.7 Table 3 non-DNR row](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | Yes. Without-DNR deaths 42 versus 47, all-cause 97 versus 147; same comparative effect/interval/test. |
| REPORT [main p.9 sixth limitation](../../../jama_parshuram_2018_oi_180015.pdf#page=9) | Yes. Rationale for sensitivity analysis of mortality after DNR order; no associated modeled following-DNR result printed there. |
| REPORT corroboration [results p.9 eTable 2](../../../joi180015supp3_prod.pdf#page=9) and [p.10 denominator note](../../../joi180015supp3_prod.pdf#page=10) | Both found. Descriptive all-cause and without-DNR mortality, with hospital-discharge denominators; no following-DNR fitted treatment effect. Complete REPORT main/results inspection supplies the absence scope. |

- **Consistency rule applicable:** Route A category 5, named planned primary-mortality sensitivity output not supplied, focus D.
- **Calculation/logical comparison and display precision:** 244−42−47=155; 97−42=55 and 147−47=100 describe after-DNR complementary deaths. They do not reproduce a baseline-adjusted following-DNR OR/CI/P. Counts are exact event counts; arithmetic reconciles and is not a separate count candidate. Even allowing half-unit display bounds produces [153.5,156.5] for the total complement and overlaps 155's display interval [154.5,155.5]. The planned-output absence is categorical and needs no relative numeric discrepancy. No crude OR substitutes for the absent modeled output.
- **Necessary inputs available:** Explicit following-DNR model, displayed without-DNR fit, aggregate mortality counts and complete report outputs suffice. **Exact missing inputs/definitions:** Following-DNR fitted effect/CI/test, definition of the report's after-DNR sensitivity, and relevant baseline/model inputs for recreating the planned fit.
- **Source-grounded alternative interpretation:** After-DNR sensitivity may mean removing deaths following DNR rather than modeling the following-DNR subset. Protocol with/without rationale supports a broad sensitivity intent. This alternative leaves identity of the specifically named model output unresolved.
- **Direct observation versus inferred explanation:** Labels and counts are printed; complementary counts are arithmetic inferences. No inference assigns OR 2.05 to the after-DNR subset or establishes that a fitted following-DNR analysis was never performed.
- **Classification confirmation:** PLAN specification versus REPORT output set gives P_R → protocol_report. Main p.9 is context, not proof of internal effect misattribution; no S_W. Descriptive supplement corroboration adds no S_C. No correction. Ambiguity: meaning of after-DNR sensitivity.
- **Determining recheck fact:** The planned following-DNR model is explicit; complete supplied REPORT set displays without-DNR effects and no identified following-DNR fitted effect.
- **Exact remaining human question:** Which output corresponds to the planned mortality-following-DNR analysis, and does the stated after-DNR sensitivity instead mean the displayed without-DNR analysis?

## C010 — ICU-readmission rate denominator changes from planned hospital to reported ICU discharges

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol p.12 vs PLAN SAP p.5 and REPORT main p.7.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [protocol p.12 ICU-readmission definition and denominator sentence](../../../joi180015supp1_prod.pdf#page=12) | Yes. PICU mortality and unplanned hospital/PICU readmission represented per thousand **hospital discharges**. |
| PLAN [SAP p.5 unplanned ICU-readmission row](../../../joi180015supp2_prod.pdf#page=5) | Yes. B_icur/B_PatientDischargesICU and P_icur/P_PatientDischargesICU; ICU discharges are explicit denominator names. |
| REPORT [main p.7 Table 3 ICU-readmission row and footnote h](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | Yes. Baseline 64 (34.43), 73 (28.09); intervention 94 (28.40), 108 (21.25); per 1000 **ICU discharges**. RD 4.95 (−1.62–11.52), OR 1.11 (0.77–1.61), P=.58. |
| REPORT [main p.5 Table 1 baseline volume](../../../jama_parshuram_2018_oi_180015.pdf#page=5) | Yes. Baseline ICU discharges 1859 and 2599; hospital discharges 26664 and 46718. |
| REPORT [main p.7 Table 3 header](../../../jama_parshuram_2018_oi_180015.pdf#page=7) and [p.3 flow](../../../jama_parshuram_2018_oi_180015.pdf#page=3) | Both found. Intervention hospital discharges 50173 and 94366. Exact intervention ICU-discharge totals are not supplied here. |

- **Consistency rule applicable:** Route B, focus D. Denominator definition changes the extractable endpoint's population/unit; broad protocol wording or a later SAP could explain intent, but no adopted amendment/timing record reconciles the specifications. This is a statistical endpoint contrast, not a peripheral contributor-count copy.
- **Calculation/logical comparison and display precision:** Baseline ICU rates are 64/1859×1000=34.42711135 and 73/2599×1000=28.08772605, matching printed 34.43/28.09. The former refines the ledger's auxiliary 34.4260 approximation without changing any source transcription. Hospital-denominator point counterparts are 2.40024002 and 1.56256689 at baseline, and 1.87351763 and 1.14448000 at intervention. For all displayed inputs, deliberately conservative half-unit count/denominator intervals give:

| Comparison to printed ICU rate | Recomputed hospital-rate interval | Printed interval | Interval gap | Relative gap using printed rate |
|---|---:|---:|---:|---:|
| Baseline BedsidePEWS, 64/26664 vs 34.43 | [2.38144349,2.41903726] | [34.425,34.435] | 32.00596274 | 0.92959520 |
| Baseline usual care, 73/46718 vs 28.09 | [1.55184777,1.57328624] | [28.085,28.095] | 26.51171376 | 0.94381323 |
| Intervention BedsidePEWS, 94/50173 vs 28.40 | [1.86353354,1.88350192] | [28.395,28.405] | 26.51149808 | 0.93350345 |
| Intervention usual care, 108/94366 vs 21.25 | [1.13917545,1.14978461] | [21.245,21.255] | 20.09521539 | 0.94565719 |

Each exceeds .05. Baseline ICU-denominator intervals [34.14896478,34.70540759] and [27.88997884,28.28554936] overlap printed ICU-rate intervals, with gap zero. These calculations illustrate the changed denominator quantity; they do not dispute adjusted OR/RD by crude arithmetic.

- **Necessary inputs available:** Denominator definitions, four event/rate occurrences and hospital volumes suffice. **Exact missing inputs/definitions:** Intervention ICU-discharge totals and dated amendment/adoption of ICU denominator. The missing ICU totals prevent an exact intervention ICU-rate recomputation, but are unnecessary to confirm the printed denominator contrast.
- **Source-grounded alternative interpretation:** Protocol sentence may summarize endpoint families too broadly, or the undated SAP may supersede it. The reported ICU unit is explicit; prospective adoption is unresolved.
- **Direct observation versus inferred explanation:** Denominator names and event/rate values are printed. Hospital-denominator counterfactual rates are recomputed illustrations, not reported effects or claims of implemented denominators. No intervention ICU total is reverse-engineered as exact.
- **Classification confirmation:** Protocol and SAP endpoint specifications are PLAN; Table 3 unit is REPORT. Protocol–main gives P_R and protocol–SAP P_P; P_R precedence → protocol_report. SAP/report agree and add no conflicting relationship. No source-value/location or classification correction. Ambiguity: broad wording versus later undated SAP revision.
- **Determining recheck fact:** Protocol explicitly says hospital discharges, while SAP and main explicitly name ICU discharges; the printed readmission rates correspond to a different denominator quantity beyond precision.
- **Exact remaining human question:** Was the ICU-readmission endpoint denominator prospectively revised from hospital discharges to ICU discharges, and which specification defines the intended endpoint for comparison/extraction?

## C011 — Protocol mortality power appendix prints 0.9% versus body 0.09%

**Evidence state:** reproduced

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol p.14 mortality power input vs PLAN protocol p.29 power appendix.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [protocol p.14 section 2.11](../../../joi180015supp1_prod.pdf#page=14) | Yes. Baseline 5.1 per thousand; 18% relative reduction; absolute reduction 0.09%; 20 hospitals, two-sided alpha .05, power 80%. |
| PLAN [protocol p.29 mortality power paragraph](../../../joi180015supp1_prod.pdf#page=29) | Yes. 18% relative reduction corresponds to absolute reduction **0.9%**, printed with percent sign. |
| PLAN [protocol p.29 scenario table/assumptions](../../../joi180015supp1_prod.pdf#page=29) | Yes. Relative reduction .178 with baseline 5.1/1000; 20 hospitals, alpha .05, z=1.96, 80% power. This scenario corroborates the smaller implied absolute-percent scale rather than supplying another conflicting scenario. |
| PLAN corroboration [protocol p.1 summary](../../../joi180015supp1_prod.pdf#page=1) | Yes. Absolute reduction 0.9 deaths/1000 admissions, relative reduction 18%, baseline 5.1/1000. |
| REPORT corroboration [main p.4 sample-size paragraph](../../../jama_parshuram_2018_oi_180015.pdf#page=4) | Yes. Absolute reduction 0.9 per 1000 hospital discharges, alpha .05 and 80% power. This agrees with body scale; no P_R conflict. |

- **Consistency rule applicable:** Route A category 2, printed magnitude difference in primary power assumption, focus D/C.
- **Calculation/logical comparison and display precision:** Baseline risk 5.1/1000=.51%; 18% reduction implies .0918% absolute. Half-unit baseline [5.05,5.15]/1000 and relative reduction [17.5%,18.5%] give [.088375%,.095275%]. Appendix .9% interval [.85%,.95%] is separated by .754725 percentage points; relative gap .754725/.9=.83858333>.05. Body .09% interval [.085%,.095%] overlaps the recomputed interval. Body–appendix copy comparison gives gap .755 and relative gap .83888889 using appendix .9 as reference; using body .09 gives 8.38888889, also above .05. Appendix scenario .178×5.1/10=.09078%, not .9%.
- **Necessary inputs available:** Source percentages, rate scale and relative reduction suffice for magnitude comparison. **Exact missing inputs/definitions:** Executed power-calculation input record and intended unit of appendix absolute-reduction phrase; not needed to reproduce the printed discrepancy but needed to establish intended input.
- **Source-grounded alternative interpretation:** Appendix may intend 0.9 per thousand or 0.09%. Surrounding inputs reconstruct the smaller scale. No alternative high-risk baseline for its mortality paragraph is identified.
- **Direct observation versus inferred explanation:** Both percentages and scenario inputs are printed. Smaller reconstructed scale is arithmetic; a proposed production mechanism or final correction is not assigned.
- **Classification confirmation:** Both conflicting inputs are PLAN content within protocol, P_P → plan_material. Protocol summary and main merely corroborate smaller scale and add no relationship. No correction; ambiguity None.
- **Determining recheck fact:** Visually printed 0.9% remains separated from printed 0.09% and recomputed absolute-percent interval by relative gap above .05.
- **Exact remaining human question:** Which absolute mortality-reduction value and unit were used, and how should the appendix .9% reconcile with the body .09% and summary .9/1000?

## C012 — SAP model-choice sensitivity outputs for primary/key-secondary effects are not supplied

**Evidence state:** reproduced

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP pp.4,5 vs REPORT main pp.4–7 and complete REPORT results supplement.

| Exact supplied-source location | Location found; source/comparator matched |
|---|---|
| PLAN [SAP p.4 Sensitivity to model choice](../../../joi180015supp2_prod.pdf#page=4) | Yes. Models for odds ratios, probabilities and rate ratios were also run using several approaches; eight relative-scale approaches explicitly listed. |
| PLAN [SAP p.4 probability/rate list](../../../joi180015supp2_prod.pdf#page=4) and [p.5 continuation](../../../joi180015supp2_prod.pdf#page=5) | Both found. Five identity-scale approaches, including baseline-adjusted GEE. Wording is retrospective and no SAP adoption date appears. |
| REPORT [main p.4 methods](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [p.5 fallback/predictors](../../../jama_parshuram_2018_oi_180015.pdf#page=5), [p.6 treatment-effect narrative](../../../jama_parshuram_2018_oi_180015.pdf#page=6), [p.7 Table 3/footnotes](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | All found. Baseline-adjusted GEE and selected non-baseline identity fallback effects are supplied; mortality OR 1.01/RD 0.01, SCDE RR 0.77/RD −0.34. These supplied approaches are not called absent. |
| Complete REPORT main [p.1](../../../jama_parshuram_2018_oi_180015.pdf#page=1) through [p.11](../../../jama_parshuram_2018_oi_180015.pdf#page=11), results [p.1](../../../joi180015supp3_prod.pdf#page=1) through [p.14](../../../joi180015supp3_prod.pdf#page=14) | Every physical page visually inspected, complete maps/fresh layouts searched. No alternative-model primary/key-secondary effect set or robustness summary is supplied. Hospital descriptive mortality plots and Bayesian recalculation of power coefficient k are distinct displays, not listed treatment-model sensitivity outputs. |

- **Consistency rule applicable:** Route A category 5, named primary/key-secondary sensitivity output set not supplied, focus D; timing remains bounded because the SAP is undated/retrospective.
- **Calculation/logical comparison and display precision:** Relative list: post-only GEE/GLMER; pre/post time-treatment GEE/GLMER; baseline-adjusted post GEE/GLMER; inverse-variance weighted linear; quasi-binomial logistic/Poisson. Absolute list: post-only GEE; pre/post GEE; baseline-adjusted GEE; weighted linear; quasi-binomial/Poisson identity. Compare these lists with actual complete outputs. The baseline-adjusted GEE entry is already reported; the additional specified sensitivity approaches have no supplied estimates or robustness summary. Absence is a categorical comparison; no display rounding interval or fabricated effect applies.
- **Necessary inputs available:** SAP model lists and complete supplied report set suffice for output-availability comparison. **Exact missing inputs/definitions:** Alternative-model effect estimates/intervals/tests, applicable primary/key-secondary model assignments, dated SAP/adoption sequence and any omitted-analysis amendment.
- **Source-grounded alternative interpretation:** Retrospective SAP wording may document completed internal checks rather than a prospective publication commitment; results may exist outside the package. PLAN classification follows analysis-specification content, not a claim that its timing preceded every analysis.
- **Direct observation versus inferred explanation:** Lists and retrospective tense are printed; supplied outputs are exhaustively bounded. No inference establishes that listed models were not run, their results differed, or the SAP preceded outcome access.
- **Classification confirmation:** SAP specification is PLAN by content; actual output set is REPORT, giving P_R → protocol_report. No P_P or report-internal conflict is established. No correction. Ambiguity: undated retrospective model-choice specification.
- **Determining recheck fact:** Additional stated model-choice approaches are identified, but complete supplied REPORT pages contain no corresponding primary/key-secondary sensitivity effect set or summary; reported GEE is excluded from absent approaches.
- **Exact remaining human question:** Which listed sensitivity models applied to mortality and SCDE, what were their estimates/intervals, and when was the sensitivity specification adopted?

## Completion and unresolved evidence limits

Covered stable IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012. Twelve individually documented rechecks; twelve reproduced; zero source-value/location transcription corrections; zero not_reproduced. Classification unchanged: statistical_results 2, protocol_report 9, plan_material 1; primary relationships S_W 2, P_R 9, P_P 1. No assigned ID is deleted or suppressed.

No cited occurrence remains unread. Human questions remain about exact test/CI attribution and multiplicity, dated amendments/SAP adoption, outcome-status referents, SCDE operational memberships, model weighting/convergence, planned subgroup/sensitivity outputs, following-DNR model identity and intervention ICU-discharge totals. They bound interpretation or fitted-model reproduction and do not represent omitted direct-source confirmation. The C010 baseline recomputation refinement changes no printed count, location, comparison or evidence state. Included anchors and copied duplicate provenance remain in the coordinator's ledger/screen records; duplicates are not treated as independent source observations.
