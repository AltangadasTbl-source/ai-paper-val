# Mechanical evidence recheck

Scope: every assigned stable ID, C001, C002, C003, C004, and C005, and every affected location listed in the current candidate ledger. Recheck completed against the exact supplied PDF pages, visually read through source-derived page renders. Native/layout text served only as a locator. All IDs remain **Pending Human Adjudication**. Evidence states describe source-record facts and do not suggest a disposition.

The main article is REPORT by its methods/results content; the eFigure supplement is REPORT by its model-results content; the data-sharing statement is non-plan REPORT content. The protocol and data-analytic-plan bundle is PLAN by its prospective specifications. These assignments follow content, not file names or supplement numbering.

## Source authority and processing record

Current-run source-derived renders visually inspected: main article PDF pp.3–9 in `preprocessing/main_mapping/direct-page-03.png` through `direct-page-09.png`; PLAN p.12 in `preprocessing/cross_source/plan12.png`; PLAN pp.10,14,15,16 in `preprocessing/initial_inclusion_screen/plan-10.png`, `plan-14.png`, `plan-15.png`, and `plan-16.png`. These exact current source-page images were used to avoid redundant rendering. No old review conclusion was used as source authority.

New derivatives are confined to `preprocessing/evidence_recheck/`. Engine: direct Poppler `pdftoppm` 26.01.0. Compute device: CPU, as recorded in `tooling_record.md`. No OCR or fallback environment was needed. Commands:

```text
pdftoppm -f 1 -l 2 -scale-to 1800 -png jama_flint_2019_oi_190079.pdf .ai_paper_validation/review_1_6_2/preprocessing/evidence_recheck/main
pdftoppm -f 10 -l 10 -singlefile -scale-to 1800 -png jama_flint_2019_oi_190079.pdf .ai_paper_validation/review_1_6_2/preprocessing/evidence_recheck/main-10
pdftoppm -scale-to 1500 -png joi190079supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/evidence_recheck/supp2
pdftoppm -singlefile -scale-to 1500 -png joi190079supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/evidence_recheck/supp3-1
```

The resulting 14 PNGs cover main pp.1,2,10; results supplement pp.1–10; data-sharing p.1. All were visually read. A supplementary `rg -n -i` search of the current-run complete REPORT layout texts for HOMA, homeostat, insulin, BMI, body mass, Intent-to-Attend, premorbid weight, weight loss, pattern mixture, and sensitivity located the related reported procedures. The absence comparison below rests on complete page inspection, not on keyword absence alone. No supplied source or reused evidence asset was modified.

## C001 — Primary relapse score component differs from the plan

**Location found:** Yes, for every registered location.

| Exact supplied location | Role by content | Source value/text matched and purpose |
|---|---|---|
| [Protocol PDF p.12, section 3.9.8, printed lines 553–568](../../../joi190079supp1_prod.pdf#page=12) | PLAN | Primary relapse is at least one listed criterion. Score criterion is 17-item HAM-D ≥18 **and** a mean absolute increase of 5 points on at least one visit relative to RCT entry. SCID psychosis is additionally qualified by SADS ≥3; psychiatric hospitalization causes are depression, psychosis, suicidality, or mania/hypomania. |
| [Main PDF p.4, Primary Outcome: Relapse](../../../jama_flint_2019_oi_190079.pdf#page=4) | REPORT | Declaring relapse requires at least one listed criterion, including 17-item HDRS 18 or higher. The additional 5-point increase is absent from this sufficient-condition list. |
| [Main PDF p.1, abstract results](../../../jama_flint_2019_oi_190079.pdf#page=1) | REPORT | 13/64 olanzapine and 34/62 placebo relapses; HR 0.25, 95% CI 0.13–0.48. This is the affected endpoint result, rather than an independently conflicting copy. |
| [Main PDF p.6, Primary Outcome](../../../jama_flint_2019_oi_190079.pdf#page=6) | REPORT | The same 13/64 and 34/62 counts and adjusted HR 0.25, 95% CI 0.13–0.48, are printed in the primary results. |
| [Main PDF p.7, Table 3 and footnotes](../../../jama_flint_2019_oi_190079.pdf#page=7) | REPORT | Table 3 supplies relapse components and permits more than one event per relapse. Footnote b limits psychiatric hospitalization to depression, psychosis, suicidality, mania, or hypomania, matching the PLAN causes. |

**Source printed value/text matched:** Yes. The PLAN conjunction and the REPORT sufficient-condition wording are directly present. The printed plan glyph is ≥18, rather than a strict greater-than threshold. HAM-D/HDRS name variation is contextually the same 17-item instrument and is not the basis of this candidate.

**Comparator printed value/text matched:** Yes. Main p.4 lists 18 or higher without the increase condition; the affected result copies on pp.1,6,7 were found. The hospitalization component reconciles through Table 3's footnote. The PLAN's SADS qualification is retained as operational context; this recheck does not expand C001 into a separate psychosis-threshold comparison.

**Consistency rule applicable:** Yes. Focus D, Route A category 5, applies to a changed printed component of the prespecified primary relapse composite. No claim that the actual operational endpoint changed is necessary to reproduce the printed definition comparison.

**Logical comparison reproduced:** Yes. Under the printed PLAN score route, satisfying the absolute score threshold alone is insufficient; an increase of 5 points relative to RCT entry is also required. Under the printed REPORT list, the score route supplies only the absolute threshold. Diagnostic illustration only: RCT-entry score 15 and subsequent score 18 gives an increase of 3, which is below 5 despite meeting 18 or higher. This example is not an observed participant or an inferred reclassified event. Other composite routes could classify the same hypothetical person as relapsed, so no event-count or HR change is calculated.

**Display-precision interval check:** Not applicable to the inconsistency: these are exact integer score decision thresholds and presence/absence of a logical conjunction, not rounded copies or recomputed effect estimates. Recomputed rounding interval and relative numerical discrepancy are therefore not defined. Allowing half-unit rounding of displayed result counts cannot restore the omitted endpoint condition.

**Necessary inputs available:** Yes for the printed-definition comparison: complete PLAN criterion, complete REPORT criterion list, trial-phase context, and affected primary result. No necessary source location is missing.

**Exact missing inputs or definitions:** Operational relapse-classification instructions used in this analysis; any endpoint amendment; participant entry and follow-up scores and which composite component established each relapse. The phrase “mean absolute increase” is not further operationalized here; the candidate does not assume its averaging convention.

**Source-grounded alternative interpretation:** Main p.4 may abbreviate an operational rule that remained unchanged, or an unprovided amendment may have revised it. The supplied source does not establish either. Such an explanation does not make the printed sufficient-condition lists identical.

**Direct observation versus inferred explanation:** Direct observation is the PLAN's extra conjunction absent from the REPORT sufficient-condition list. Abbreviation, amendment, and any effect on actual 13/64 versus 34/62 events are explanations or consequences that are not demonstrated by this package.

**Exact remaining human question:** Was the additional 5-point HDRS increase from RCT entry required to classify the relapses generating the printed 13/64 versus 34/62 counts and HR 0.25, and where is that operational rule or its amendment documented?

**Classification confirmed:** Document roles PLAN versus REPORT; primary relationship **P_R**; All relationships **P_R**; review domain **protocol_report**. A prospective endpoint definition is directly compared with its report counterpart. The agreeing report result copies and plan-confirmed hospitalization wording add context, not S_C, S_W, or P_P conflicts. No classification correction is needed. Classification ambiguity concerns operational abbreviation/amendment, not document role.

**Evidence state:** **reproduced**. Determining fact: directly read PLAN conjunction versus directly read REPORT score-only component still differs after correct threshold-glyph reading and after the hospitalization comparison is reconciled. No registered value or location needed transcription correction.

## C002 — Four prespecified key secondary counterparts are absent from the supplied reporting record

**Location found:** Yes, for every planned specification and every registered REPORT location. All four pattern locations were rechecked separately.

| Pattern member | Exact PLAN location and matched specification | REPORT counterpart comparison |
|---|---|---|
| HOMA glycemic measure | [Protocol PDF p.10, lines 484–488](../../../joi190079supp1_prod.pdf#page=10), PLAN: HOMA is the primary glycemic-function measure and is calculated when fasting glucose and insulin are measured; HbA1c is secondary. [p.14, E1, lines 687–691](../../../joi190079supp1_prod.pdf#page=14), PLAN, additionally confirms insulin resistance is a distinct planned quantity, without adding an exploratory aim to the candidate. | REPORT abstract, definitions, results, Table 4, and glucose/HbA1c plots contain glucose and HbA1c, with no HOMA/insulin-resistance outcome counterpart. Glucose alone and HbA1c are not identified as HOMA by the source. |
| Separate BMI alternative analysis | [Protocol PDF p.10, lines 477–483](../../../joi190079supp1_prod.pdf#page=10), PLAN: BMI and waist are measured, with separate secondary analyses for Aims 2–5 using each as an alternative to weight. | REPORT supplies waist and weight models/results, but no BMI alternative model/result counterpart. Reporting waist does not supply the separately named BMI analysis. |
| Depression-related weight-loss analysis | [Protocol PDF p.10, lines 473–477](../../../joi190079supp1_prod.pdf#page=10), PLAN: premorbid weight permits calculation of depression-related weight loss, which will be taken into account in a secondary statistical analysis of weight change. | REPORT supplies descriptive premorbid weight and premorbid-reference adverse weight-gain/loss definitions, but does not report a secondary weight-change model/result accounting for depression-related weight loss. These related uses do not identify that model or its result. |
| Intent-to-Attend comparison | [Protocol PDF p.16, lines 769–772](../../../joi190079supp1_prod.pdf#page=16), PLAN: RCT-entry Intent-to-Attend is to enter attrition models as a covariate, and treatment-effect estimates will be compared with models including dropout-pattern or Intent-to-Attend main effects. | REPORT supplies pattern-mixture investigation and triglyceride pattern-mixture-averaged estimates, but no Intent-to-Attend covariate/comparison counterpart. One named attrition approach does not identify the other. |

**Complete REPORT absence check:** Every supplied REPORT page was directly inspected, including the registered methods/result locations and all eFigures. The table records each individual page so that the comparison is bounded to the supplied reporting record.

| Exact page found | Role | Content inspected and absence-check fact |
|---|---|---|
| [Main p.1](../../../jama_flint_2019_oi_190079.pdf#page=1) | REPORT | Abstract names weight, waist, lipids, glucose, HbA1c as main secondary outcomes and prints eight model effects; no counterpart for the four pattern members. |
| [Main p.2](../../../jama_flint_2019_oi_190079.pdf#page=2) | REPORT | Key Points, introduction, and methods state Aims 1–2 are reported and age/genetic additional aims are not; no four-member counterpart. This bounds the issue to reported key secondary weight/metabolic analyses. |
| [Main p.3](../../../jama_flint_2019_oi_190079.pdf#page=3) | REPORT | Participant flow and remission/eligibility continuation; no four-member counterpart. |
| [Main p.4](../../../jama_flint_2019_oi_190079.pdf#page=4) | REPORT | Secondary outcome collection, mixed-model covariates, and premorbid-reference weight adverse events; no HOMA, BMI model, depression-weight-loss analysis result, or Intent-to-Attend comparison. |
| [Main p.5](../../../jama_flint_2019_oi_190079.pdf#page=5) | REPORT | Table 1 reports premorbid weight 166.6 (34.6) and 171.4 (40.2) lb; methods describe pattern-mixture and statin/hypoglycemic sensitivity analyses. None identifies the four planned counterparts. |
| [Main p.6](../../../jama_flint_2019_oi_190079.pdf#page=6) | REPORT | Table 2, primary results, descriptive safety and multiplicity methods; no four-member counterpart. |
| [Main p.7](../../../jama_flint_2019_oi_190079.pdf#page=7) | REPORT | Secondary effects for eight measures, medication-change sensitivity statement, and tolerability results; no four-member counterpart. |
| [Main p.8](../../../jama_flint_2019_oi_190079.pdf#page=8) | REPORT | Table 4 rows are weight, waist, total/LDL/HDL cholesterol, HbA1c, triglycerides, glucose; discussion likewise addresses these measures. No four-member counterpart. |
| [Main p.9](../../../jama_flint_2019_oi_190079.pdf#page=9) | REPORT | Table 5 post hoc incident high-metabolic-value counts, limitations, conclusion, and article information; no four-member counterpart. |
| [Main p.10](../../../jama_flint_2019_oi_190079.pdf#page=10) | REPORT | End matter, references, and pointer to data-sharing statement; no trial result counterpart for the four members. A reference to other work is not a supplied result. |
| [Result supplement p.1](../../../joi190079supp2_prod.pdf#page=1) | REPORT | Complete index contains eFigures 1–9 for the eight anthropometric/metabolic measures and SAS; no four-member counterpart. |
| [Result supplement p.2](../../../joi190079supp2_prod.pdf#page=2) | REPORT | eFigure 1: weight model means in randomized groups; no BMI or depression-weight-loss-adjusted comparison. |
| [Result supplement p.3](../../../joi190079supp2_prod.pdf#page=3) | REPORT | eFigure 2: waist model means in randomized groups; no BMI counterpart. |
| [Result supplement p.4](../../../joi190079supp2_prod.pdf#page=4) | REPORT | eFigure 3: total-cholesterol model means; no four-member counterpart. |
| [Result supplement p.5](../../../joi190079supp2_prod.pdf#page=5) | REPORT | eFigure 4: LDL model means; no four-member counterpart. |
| [Result supplement p.6](../../../joi190079supp2_prod.pdf#page=6) | REPORT | eFigure 5: HDL model means; no four-member counterpart. |
| [Result supplement p.7](../../../joi190079supp2_prod.pdf#page=7) | REPORT | eFigure 6: triglyceride pattern-mixture means with dropout groups; no Intent-to-Attend counterpart. |
| [Result supplement p.8](../../../joi190079supp2_prod.pdf#page=8) | REPORT | eFigure 7: glucose model means; not a HOMA/insulin-resistance counterpart. |
| [Result supplement p.9](../../../joi190079supp2_prod.pdf#page=9) | REPORT | eFigure 8: HbA1c model means; not a HOMA counterpart. |
| [Result supplement p.10](../../../joi190079supp2_prod.pdf#page=10) | REPORT | eFigure 9: Simpson-Angus total-score means; no four-member counterpart. |
| [Data-sharing statement p.1](../../../joi190079supp3_prod.pdf#page=1) | REPORT | Administrative access statement, supporting document types “None”; no analyses or quantitative counterparts are supplied on the page. |

**Source printed value/text matched:** Yes for each of the four prospective specifications, including p.14's corroborating identity context. The PLAN p.10 anthropometric and metabolic sections and p.16 Intent-to-Attend sentence are complete and legible.

**Comparator printed value/text matched:** Yes for the related printed REPORT analyses and every result-supplement title. There is no printed counterpart to transcribe for an absent result; this field means the full bounded comparison record was found and inspected. None of the related procedures is described as implementing the absent counterpart.

**Consistency rule applicable:** Yes. Focus D, Route A category 5: planned primary/key secondary outcome analyses not reported. Weight/metabolic results are main secondary results in the abstract and part of Aims 1–2. Additional age/genetic aims are expressly outside this report and are not added to C002. The same absence-of-counterpart rule applies to all four members; no assertion of nonperformance is made.

**Logical comparison reproduced:** Yes, separately for HOMA, BMI, depression-related-weight-loss modeling, and Intent-to-Attend treatment-effect comparison. Each has an explicit PLAN specification; none has a counterpart in the 21 supplied REPORT pages. Waist, glucose, HbA1c, descriptive premorbid weight, weight adverse-event definitions, and pattern-mixture results are present but are different named measures or procedures. This is a supplied-record absence comparison, not an attempt to calculate an unreported coefficient.

**Display-precision interval check:** Not applicable. There is no printed pair/recomputed number for the four absent counterparts, so no rounding intervals, interval gap, or relative numerical discrepancy can be calculated. Rounding the printed weight/waist/glucose/HbA1c values cannot generate an absent HOMA, BMI, covariate-adjusted, or Intent-to-Attend result.

**Necessary inputs available:** Yes for reproducing presence of the PLAN specifications and absence from the complete supplied REPORT record. All supplied REPORT units are available and legible.

**Exact missing inputs or definitions:** The four outcome/model results; any prospective amendment removing/replacing them; a documented scope/deferment explanation; model output identifying whether the premorbid-weight operation described in tolerability also entered the statistical weight-change analysis. Participant insulin/height/weight-loss/Intent-to-Attend data and model outputs are not supplied, so the missing coefficients or their effects cannot be calculated.

**Source-grounded alternative interpretation:** Main p.2 explicitly defers additional aims and the data-sharing page allows investigator-supported access to participant data; related analyses may exist outside the supplied reporting record. The four counterparts may have been performed elsewhere, deferred, unavailable, or modified. No supplied page identifies which explanation applies to these Aims 1–2 weight/metabolic counterparts.

**Direct observation versus inferred explanation:** Direct observation is four explicit PLAN specifications with no matching result/analysis statement in the exhaustive supplied REPORT record. Whether the analyses were performed, how an unprovided model was coded, or whether their estimates would change a conclusion is not established.

**Exact remaining human question:** Where are the HOMA, separate BMI, depression-related-weight-loss, and Intent-to-Attend treatment-effect counterparts for the reported key secondary record, or which documented amendment or scope decision accounts for each one's absence from this supplied report?

**Classification confirmed:** Compared roles PLAN specification versus REPORT outcome/analysis record; primary relationship **P_R**; All relationships **P_R**; domain **protocol_report**. The report documents agree on the supplied result scope; they do not conflict with each other and therefore do not add S_C. The PLAN corroborating exploratory paragraph is not a P_P conflict. No correction needed. Classification ambiguity is limited to unprovided scope/amendment documentation, not roles or the bounded absence fact.

**Evidence state:** **reproduced**. Determining fact: each named counterpart remains absent after direct inspection of every supplied REPORT page, while all four prospective specifications are found at their exact PLAN locations. No registration transcription or location correction is needed.

## C003 — Adverse-event reference baseline differs

**Location found:** Yes, for every registered location and both affected measures.

| Exact supplied location | Role | Source value/text matched |
|---|---|---|
| [Protocol PDF p.15, Non-Metabolic Safety Data, lines 705–717](../../../joi190079supp1_prod.pdf#page=15) | PLAN | For each phase, report numbers/percentages meeting specific adverse-event criteria who did not meet them at **acute phase baseline**. UKU criterion is an increase ≥2 points from baseline or score 3; Barnes global assessment criterion is ≥2. |
| [Main PDF p.4, Other Measures of Tolerability](../../../jama_flint_2019_oi_190079.pdf#page=4) | REPORT | Incident akathisia requires Barnes global assessment 0 at **RCT baseline** and ≥2 later. UKU adverse effects require a 2-point increase from **RCT baseline**, or score 3 or 4 plus an increase from baseline, apart from weight events. |
| [Main PDF p.7, Extrapyramidal Measures](../../../jama_flint_2019_oi_190079.pdf#page=7) | REPORT | Akathisia incidence is 4.7% olanzapine versus 4.8% placebo. |
| [Main PDF p.7, Adverse Effects](../../../jama_flint_2019_oi_190079.pdf#page=7) | REPORT | Sleepiness/sedation 7.8% versus 3.2%; orthostatic dizziness 7.8% versus 3.2%; nausea/vomiting 3.1% versus 8.1%. These are the affected UKU incidences. |

**Source printed value/text matched:** Yes. The prospective population exclusion explicitly says acute phase baseline. The generic PLAN UKU phrase “from baseline” alone does not specify its epoch; the definite acute-baseline eligibility statement is the reproduced comparison anchor, and no additional unprinted interpretation of that phrase is needed.

**Comparator printed value/text matched:** Yes. The REPORT explicitly names RCT baseline for UKU increase and Barnes incident-case eligibility and supplies the named incidence percentages. The extra score-4 phrase does not constitute a separate candidate here.

**Consistency rule applicable:** Yes. Focus D and Route B apply to a planned-versus-reported safety-event definition/reference population. Different definite eligibility epochs can change the meaning of the extracted UKU and akathisia incidence measures. Immediate context supplies no reconciliation of the prospective acute-baseline exclusion and reported RCT-baseline conditions.

**Logical comparison reproduced:** Yes for both pattern locations: UKU and akathisia. Acute enrollment precedes acute treatment and stabilization; RCT baseline follows these phases, as directly described in [main p.2](../../../jama_flint_2019_oi_190079.pdf#page=2) and [p.3](../../../jama_flint_2019_oi_190079.pdf#page=3), both REPORT. A person may meet or cease to meet a criterion between the two times, so “not present at acute baseline” and the reported RCT-baseline eligibility/change rule are not identical definitions. This is logical possibility, not evidence that a particular participant or count changed. The PLAN's acute-baseline eligibility does not numerically reconstruct the REPORT percentages without trajectories.

**Display-precision interval check:** Not applicable to the epoch/eligibility discrepancy. Half-unit percentage intervals for the affected reported incidences (e.g., 4.7% has [4.65,4.75]% and 4.8% has [4.75,4.85]%) do not compare two copies of the same group/event and do not resolve which baseline defined the event. No cross-arm percentage discrepancy is asserted; recomputed interval gap and relative discrepancy for the candidate are not defined.

**Necessary inputs available:** Yes for the definition comparison and the affected printed incidences. Both source definitions are exact and legible.

**Exact missing inputs or definitions:** Participant UKU/Barnes observations at acute entry, RCT entry, and follow-up; whether acute-baseline-positive cases were excluded from the reported incidence set; operational denominators; any safety-endpoint amendment. These are needed to calculate a count change, which this recheck does not claim.

**Source-grounded alternative interpretation:** The REPORT may intentionally define randomized-phase emergent adverse events separately from the PLAN's phase-by-phase acute-baseline criterion, or an unprovided amendment may implement that change. A generic “baseline” convention does not replace the explicit different named epochs.

**Direct observation versus inferred explanation:** Direct observation is explicit acute-baseline eligibility in PLAN and explicit RCT-baseline conditions in REPORT, attached to named incidence results. Whether this was intentional and whether any participant changes eligibility is not demonstrated.

**Exact remaining human question:** Were the reported UKU and akathisia incidences restricted by acute-phase baseline or defined solely from RCT baseline, and what specification reconciles that operational definition with the supplied plan?

**Classification confirmed:** PLAN adverse-event definition versus REPORT adverse-event definition/results; primary **P_R**; All relationships **P_R**; domain **protocol_report**. Main pp.2–3 only confirm the distinct phase times and are not S_W conflicts. No correction needed. Classification ambiguity: the actual eligibility implementation and any amendment are unavailable; document roles are unambiguous.

**Evidence state:** **reproduced**. Determining fact: the explicit acute-baseline inclusion criterion and explicit RCT-baseline incidence conditions remain different after direct reading of both printed definitions. No registration value/location correction is needed.

## C004 — Safety treatment classification differs from the plan

**Location found:** Yes for both prospective repetitions, four registered main REPORT pages, and every affected supplementary plot.

| Exact supplied location | Role | Source value/text matched |
|---|---|---|
| [Protocol PDF p.14, H2, lines 663–667](../../../joi190079supp1_prod.pdf#page=14) | PLAN | Safety analyses classify subjects based on medications taken during protocolized treatment. This is within the randomized-phase mixed-model specification. |
| [Protocol PDF p.16, lines 763–769](../../../joi190079supp1_prod.pdf#page=16) | PLAN | ITT is described for H1 survival analysis; the following safety paragraph repeats classification based on medications taken during protocolized treatment. |
| [Main PDF p.3, Figure 1](../../../jama_flint_2019_oi_190079.pdf#page=3) | REPORT | 64 and 62 randomized; 59 and 60 received randomized treatment; 5 and 2 did not. In the olanzapine arm 3 discontinued and 2 switched to open-label olanzapine; in placebo arm 1 discontinued and 1 switched to open-label olanzapine. |
| [Main PDF p.4, Statistical Analyses](../../../jama_flint_2019_oi_190079.pdf#page=4) | REPORT | Analyses included all randomized participants. Safety models include treatment group and treatment-by-time fixed effects; the medication-taken recoding algorithm is not specified. |
| [Main PDF p.7, Secondary Outcomes](../../../jama_flint_2019_oi_190079.pdf#page=7) | REPORT | Eight weight/waist/metabolic treatment-by-linear-time effects are reported as olanzapine versus placebo, including weight 0.13 lb/day, waist 0.009 inches/day, total cholesterol 0.29 mg/dL/day. |
| [Main PDF p.8, Table 4](../../../jama_flint_2019_oi_190079.pdf#page=8) | REPORT | Descriptive secondary outcomes are grouped as sertraline+olanzapine n=64 and sertraline+placebo n=62, with measure-specific contributors. This corroborates reported arm presentation but is not itself a model-coding algorithm. |
| [Result supplement p.2, eFigure 1](../../../joi190079supp2_prod.pdf#page=2) | REPORT | Weight mixed-model means explicitly titled “in Randomized Groups.” |
| [Result supplement p.3, eFigure 2](../../../joi190079supp2_prod.pdf#page=3) | REPORT | Waist mixed-model means explicitly titled “in Randomized Groups.” |
| [Result supplement p.4, eFigure 3](../../../joi190079supp2_prod.pdf#page=4) | REPORT | Total cholesterol mixed-model means explicitly titled “in Randomized Groups.” |
| [Result supplement p.5, eFigure 4](../../../joi190079supp2_prod.pdf#page=5) | REPORT | LDL mixed-model means explicitly titled “in Randomized Groups.” |
| [Result supplement p.6, eFigure 5](../../../joi190079supp2_prod.pdf#page=6) | REPORT | HDL mixed-model means explicitly titled “in Randomized Groups.” |
| [Result supplement p.7, eFigure 6](../../../joi190079supp2_prod.pdf#page=7) | REPORT | Triglyceride pattern-mixture means explicitly titled “in Randomized Groups”; legend additionally splits dropout/non-dropout. |
| [Result supplement p.8, eFigure 7](../../../joi190079supp2_prod.pdf#page=8) | REPORT | Glucose mixed-model means explicitly titled “in Randomized Groups.” |
| [Result supplement p.9, eFigure 8](../../../joi190079supp2_prod.pdf#page=9) | REPORT | HbA1c mixed-model means explicitly titled “in Randomized Groups.” |

**Source printed value/text matched:** Yes. Both prospective medication-taken classification statements are found and their separation from the primary H1 ITT discussion is confirmed.

**Comparator printed value/text matched:** Yes. Every affected model-plot title names randomized groups; main all-randomized inclusion, observed treatment departures, effects, and arm totals are found. Inclusion of all randomized participants alone does **not** establish how treatment group was coded. The direct comparison rests on the explicit randomized-group model-result titles versus the prospective medication-taken safety classification, with main analysis context corroborating it.

**Consistency rule applicable:** Yes. Focus D, Route B: treatment classification determines the contrast represented by the eight key secondary safety estimates. The printed group rules differ in a package that records deviations from assigned treatment; source context supplies no coding rule reconciling them.

**Logical comparison reproduced:** Yes, for all eight model-result labels. The PLAN's group variable is defined from medication taken; the REPORT labels model means by randomized group. Figure 1 establishes that medication exposure and randomized assignment need not be interchangeable. Its counts reconcile: 59+5=64, 60+2=62, 3+2=5, and 1+1=2. These exact participant counts are not disputed. No assumption that all 7 departures would be reclassified, and no choice between fixed or time-varying medication grouping, is imposed.

**Display-precision interval check:** Not applicable to the categorical grouping discrepancy. Figure 1 displays exact discrete counts, and its additive identities have zero gap; no rounding mismatch supports C004. Half-unit intervals for effect estimates do not identify the treatment-coding rule. Recomputed interval gap/relative numerical discrepancy for the candidate are not defined.

**Necessary inputs available:** Yes for the stated group-rule comparison, each affected title, and the existence of treatment departures. All affected locations were directly checked.

**Exact missing inputs or definitions:** Medication-taken classification algorithm; timing of medication changes and observations retained; fixed versus time-varying treatment coding; whether post-discontinuation/switch observations enter safety models; actual model design matrix; any amended safety specification. These are needed to infer reclassification or compute coefficient changes and are not supplied.

**Source-grounded alternative interpretation:** Randomized labels may describe presentation while medication-taken coding was otherwise operationalized; later observations may have been excluded such that analyzed exposures remained aligned; or the analysis may have intentionally adopted randomized assignment. The main text's follow-up after medication discontinuation and the supplement's explicit randomized labels support asking which convention applied, but do not demonstrate an individual reclassification algorithm.

**Direct observation versus inferred explanation:** Direct observations are two medication-taken PLAN statements, eight randomized-group model titles, all-randomized analysis inclusion, and Figure 1 treatment departures. Numerical impact and the actual design-matrix coding are not inferred as facts.

**Exact remaining human question:** Which treatment-classification rule generated the eight safety mixed-model contrasts and plotted means, how were discontinuation/switch observations treated, and how does that rule reconcile with the medication-taken specification in the supplied plan?

**Classification confirmed:** PLAN safety grouping versus REPORT model-group definitions/presentation; primary **P_R**; All relationships **P_R**; review domain **protocol_report**. Main and supplement support the same report side, adding no S_C conflict. Both PLAN statements agree, adding no P_P. No correction needed. Classification ambiguity is the actual operational group coding, not source roles.

**Evidence state:** **reproduced**. Determining fact: every registered randomized-group model title is printed as cited, while both exact PLAN locations specify medication-taken safety classification; no supplied algorithm reconciles those definitions. No transcription correction is required. Reproduction concerns the printed specification/presentation discrepancy, not a demonstrated coefficient change.

## C005 — Planned metabolic observation exclusion is placed in post hoc sensitivity analysis

**Location found:** Yes, for every registered location.

| Exact supplied location | Role | Source value/text matched |
|---|---|---|
| [Protocol PDF p.14, H2, lines 673–679](../../../joi190079supp1_prod.pdf#page=14) | PLAN | If new/change hyperlipidemia treatment occurs during RCT, pertinent metabolic data from then onward will be excluded from the mixed model. Measures continue to be collected for safety/DSMB reporting; exclusion is placed directly in the H2 model specification. |
| [Main PDF p.1, abstract secondary results](../../../jama_flint_2019_oi_190079.pdf#page=1) | REPORT | Headline cholesterol/lipid daily-rate effects are printed, including total cholesterol 0.29 (0.13–0.45), LDL 0.04 (−0.01–0.10), HDL −0.01 (−0.03–0.01), and triglyceride −0.153 (−0.306–0.004). These identify affected estimates, rather than discrepant numerical copies. |
| [Main PDF p.5, final Statistical Analyses paragraph](../../../jama_flint_2019_oi_190079.pdf#page=5) | REPORT | Post hoc sensitivity analyses exclude pertinent metabolic data from the point a statin or hypoglycemic agent starts/changes. |
| [Main PDF p.7, secondary/medication-change results](../../../jama_flint_2019_oi_190079.pdf#page=7) | REPORT | Statins started/changed in 12 participants (6 per arm); hypoglycemic agents in 3 (2 olanzapine, 1 placebo). These post hoc sensitivity results were qualitatively similar to analyses including all participants. |

**Source printed value/text matched:** Yes. PLAN exclusion is mandatory future-tense within H2; continued collection is separately stated. The plan does not identify the same exclusion as a post hoc sensitivity procedure.

**Comparator printed value/text matched:** Yes. REPORT p.5 places the operation in explicitly post hoc sensitivity analyses, and p.7 describes the comparison with all-participant analyses and actual drug changes. The REPORT's hypoglycemic extension is not claimed to be a planned H2 hyperlipidemia exclusion.

**Consistency rule applicable:** Yes. Focus D, Route B: a principal model observation-selection specification versus a reported post hoc sensitivity placement can change which observation rule a reader attributes to the principal lipid effects and how their prespecification is understood. This is distinct from C002 because an actual counterpart operation is reported, with a different analysis role.

**Logical comparison reproduced:** Yes. PLAN puts post-hyperlipidemia-treatment exclusion within the H2 mixed-model specification; REPORT describes exclusion for statin/hypoglycemic changes as post hoc sensitivity. The source supplies no explicit statement mapping the PLAN rule to the principal headline coefficients. Medication-change counts reconcile exactly: 6+6=12 and 2+1=3. Qualitative similarity does not identify the principal observation rule or establish equality of coefficients. Conversely, “included all participants” does **not** necessarily mean every post-drug-change observation was included: participants can remain in a model using their earlier observations. This ambiguity is explicitly retained and prevents inferring an observed numerical change.

**Display-precision interval check:** Not applicable to the specification-role comparison. No pair of principal/sensitivity coefficients is printed for recomputation, so their rounding intervals and relative discrepancy cannot be calculated. The exact participant-change counts above have zero arithmetic gap and are corroborating context only. The affected abstract coefficient intervals are not claimed to disagree with p.7.

**Necessary inputs available:** Yes for the direct placement comparison: complete PLAN H2 exclusion, complete REPORT sensitivity sentence, medication-change counts, and affected headline results.

**Exact missing inputs or definitions:** Principal-model observation-selection rule; which lipid outcomes/observations were removed after each change; separate principal and sensitivity outputs; whether “post hoc” refers to the whole exclusion or only expansion to hypoglycemic agents; any supplied amendment authorizing a different analysis role. These are needed to establish numerical impact and are not supplied.

**Source-grounded alternative interpretation:** The principal model may have retained the planned statin-related exclusion, with post hoc sensitivity referring only to extension to hypoglycemic agents; all participants may remain represented by earlier observations. Alternatively, the observation exclusion may have moved entirely to a sensitivity analysis under an unprovided amendment. Both alternatives fit aspects of the supplied wording, and the report does not identify which applies.

**Direct observation versus inferred explanation:** Direct observation is PLAN H2 exclusion placement versus REPORT post hoc sensitivity placement and the qualitative comparison. An analysis amendment, inclusion of all later observations, and any resulting numerical difference are not established.

**Exact remaining human question:** Did the principal lipid/metabolic estimates exclude post-hyperlipidemia-treatment observations as specified in H2, or was that exclusion applied only in sensitivity analyses, and does “post hoc” describe the entire operation or its hypoglycemic extension?

**Classification confirmed:** PLAN principal observation specification versus REPORT sensitivity specification/results; primary **P_R**; All relationships **P_R**; domain **protocol_report**. Main abstract/results agree as affected output and form no separate S_W conflict. No correction needed. Classification ambiguity concerns the principal model's operational observation rule and breadth of the post hoc label, not document roles.

**Evidence state:** **reproduced**. Determining fact: direct source reading confirms the planned main-model placement and reported post hoc sensitivity placement, without a supplied reconciliation; the registration already states this specification-role discrepancy rather than an absent analysis or a numeric effect. No registered transcription/location correction is needed.

## Final classification and coverage summary

| ID | Every affected location found | Source/comparator matched | Primary relationship | All relationships | Review domain | Evidence state | Classification correction |
|---|---|---|---|---|---|---|---|
| C001 | Yes | Yes | P_R | P_R | protocol_report | reproduced | None |
| C002 | Yes; all four pattern members and all 21 REPORT pages inspected | Yes; absence bounded to supplied REPORT record | P_R | P_R | protocol_report | reproduced | None |
| C003 | Yes; UKU and akathisia separately | Yes | P_R | P_R | protocol_report | reproduced | None |
| C004 | Yes; both PLAN repetitions and all eight affected plots | Yes | P_R | P_R | protocol_report | reproduced | None |
| C005 | Yes | Yes | P_R | P_R | protocol_report | reproduced | None |

Coverage: 5 stable IDs; 5 reproduced, 0 reproduced_after_transcription_correction, 0 not_reproduced. Each remains Pending Human Adjudication. No cited source-page coverage or tooling limitation remains. Remaining questions concern unavailable operational definitions, amendments, omitted results, participant trajectories, treatment coding, and model observation selection. This package cannot demonstrate that an absent analysis was never performed, quantify affected participants/observations, or calculate changes in model effects. Ledger and screening artifacts were not edited by this recheck.
