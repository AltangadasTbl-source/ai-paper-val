# Workflow 1.6 cross-source consistency review

Fresh cross-source checker. Complete package: DOC-001 REPORT article pp1–10; DOC-002 REPORT results supplement pp1–16; DOC-003 PLAN protocol/MOP pp1–153, retaining original and final version boundaries and amendments; DOC-004 PLAN SAP pp1–83, retaining original and final versions; DOC-005 REPORT data-sharing p1. All supplied maps and page registers were read; raw-transcription appendices were used only for targeted lookups. No old candidate conclusions, web sources, raw-data audit, or general study-design assessment was used. No source or reused asset changed.

The complete matching record is split into two bounded artifacts: `checkers/cross_source_parts/report_matches.md` and `checkers/cross_source_parts/plan_matches.md`. Each records fewer than120 matching families, while expanded row vectors include every mapped component rather than sampling. The checker reviewed the complete497 numeric/definition and103 statistical mapped groups as the source union; cross-location matching families are not a replacement count for that complete map. Exact source roles accompany every observation below. Coordinator assigns stable IDs and classifications; the names below are local descriptive references only. Every observation is Pending Human Adjudication.

## Direct-source provenance

Poppler26.01.0 `pdftotext -layout` was used against current supplied sources: article pp2–4 (`preprocessing/cross_main_methods.txt`), pp6–8 (`preprocessing/cross_main_results.txt`); results p5–6 (`preprocessing/cross_ae_defs.txt`),p11 (`preprocessing/cross_results11.txt`),p12 (`preprocessing/cross_results12.txt`),p14 (`preprocessing/cross_results14.txt`); final SAP pp60–61 (`preprocessing/cross_sap_models.txt`),pp71–72 (`preprocessing/cross_sap_population.txt`). The direct rendered protocol p81 image `preprocessing/protocol_middle_p81.png` and finalSAP p61 image `preprocessing/sap_early_p061.png` were opened visually; these new-run source derivatives confirm exact inequality signs and wording. Reused source-linked layout assets and fresh extraction maps are locators. The mandatory evidence rechecker must confirm final candidate transcription against exact sources. Direct tools available; fallback unnecessary; CPU only.

## Distinct quality-control observations

### Six-month numbness/tingling patient counts differ

- REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), nonserious systemic “Numbness or tingling”: MTX25(23.4%),MMF18(16.7%). REPORT [results eTable6 p12](../../../joi190092supp1_prod.pdf#page=12), “Numbness/tingling”: MTX13(12.1%),MMF11(10.2%). Both are six-month counts of patients reporting at least one event; MTX denominator107,MMF exposed denominator108. The article header109 issue is separately recorded below.
- Direct observation: paired numerators differ by12 MTX and7 MMF; displayed percentages in both locations reflect their own numerators and the exposed safety denominators. This cannot be a precision difference, an event-count versus patient-count difference, or a6-versus12-month difference.
- Comparison rule: the same symptom, arm, period and patient-at-least-one measure should agree if these are the same safety variable. eTable6 is explicitly “Patient-Reported Other Systemic” and could instead represent a separately collected additional-symptom field. The printed package does not explain a separate numbness variable or relation between these two rows.
- Supported alternative: main structured neurologic-field responses and supplement free-text/additional-event responses may differ legitimately; if so, the apparently identical labels need a supplied distinction for downstream extraction. No assertion that either count is wrong.
- Human verification: match the data-dictionary field IDs, deduplication rules and visit aggregation behind both rows; establish whether25/18 and13/11 refer to the same field or different event streams, then confirm the intended table labels/counts.

### Six-month self-reported mood patient total exceeds supplement any-mood total

- REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8): “Mood changes (self-reported, not requiring therapy)” MTX33(30.8%),MMF26(24.1%). REPORT [results eTable5 p11](../../../joi190092supp1_prod.pdf#page=11): “Six-Month Patient-Reported Mood-Related Adverse Events,” “Any mood-related adverse event” MTX22(20.6%),MMF19(17.6%),denominators107/108.
- Direct observation: the narrower printed self-reported/no-therapy category exceeds the printed any-mood union by11 MTX and7 MMF. This is a set-containment comparison, not a sum of overlapping mood rows.
- Comparison rule: if “Any mood-related” encompasses the article's self-reported mood changes in the same six-month safety population, the subset count cannot exceed the union. Actual data fields/coding are not supplied, so this is conditional on that natural printed alignment.
- Supported alternative: the mood appendix may list additional open-ended mood responses separate from the article's structured mood-change item. No such distinction is printed in the table title/union label.
- Human verification: check questionnaire items and union membership for the main33/26 versus supplement22/19; identify whether appendix “Any” denotes all mood events or only its additional-response stream.

### Six-month MMF safety denominator printed109 versus exposed108

- REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8): MMF header “n=109”; footnote b says one patient never received MMF. Fatigue59(54.6%),headache45(41.7%),eye pain4(3.7%) are among the affected rows. REPORT [results eTables4–6 pp10–12](../../../joi190092supp1_prod.pdf#page=10): MMF N108, footnote explicitly108 received medication. REPORT [article Figure1 p3](../../../jama_rathinam_2019_oi_190092.pdf#page=3) corroborates109 randomized/108 received.
- Direct arithmetic:59/108=54.6296% rounds54.6;59/109=54.1284% rounds54.1.45/108=41.6667% rounds41.7;45/109=41.2844% rounds41.3. The six-month exposed denominator108 reconciles the printed safety percentages.
- Comparison rule: a patient proportion's displayed denominator must identify the denominator actually used. The article header may intentionally show randomized allocation size while percentages use exposed participants, but this mixed convention needs clarification; supplement exposes108 directly. PLAN [finalSAP p71 §4.1](../../../joi190092supp3_prod.pdf#page=71) safety population “all patients who receive any amount” corroborates the exposed denominator and does not independently create a report-plan discrepancy relationship.
- Human verification: confirm header convention and denominator for every Table3 MMF row. This observation does not conflate randomized efficacy109 with treated safety108.

### Ocular-hypertension boundary24mmHg differs across report definitions

- REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8): nonserious ocular hypertension “>24mmHg”,10(9.3%)/13(12.0%). REPORT [results eTable1 p5](../../../joi190092supp1_prod.pdf#page=5): nonserious ocular hypertension “≥24mmHg”. Article footnote a explicitly points to eTable1 for these definitions. REPORT [results eTables8/9 pp14–15](../../../joi190092supp1_prod.pdf#page=14) also use>24 in the nonserious row; their6–12-month counts are not compared to the six-month counts.
- Rule and direct difference: exactly24 meets≥24 and fails>24. PLAN [finalprotocol p136 §6.1](../../../joi190092supp2_prod.pdf#page=136) saysIOP>24 and corroborates the article, not a separate mismatch.
- Alternative: row abbreviation or inequality transcription could explain the discrepancy; actual24 readings are unknown. Human verification: confirm intended threshold and whether exact24 observations contribute to any displayed ocular-hypertension count.

### Creatinine boundary1.5mg/dL differs between report row and defining materials

- REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8): nonserious elevated creatinine “>1.5 to<2mg/dL lasting<28d”,1(0.9%)/0. REPORT [results eTable1 p5](../../../joi190092supp1_prod.pdf#page=5): “≥1.5 to<2mg/dL” for<28days. PLAN [finalprotocol p81 Table3](../../../joi190092supp2_prod.pdf#page=81) and [p136 §6.1](../../../joi190092supp2_prod.pdf#page=136):≥1.5 to<2.
- Rule: exactly1.5mg/dL belongs to≥1.5 and not>1.5. Both report-report and plan-report defining inequalities conflict; no patient count correction is inferred. SI conversion×88.4 is coherent and separate.
- Alternative/human verification: establish whether the article abbreviated an inclusive cutpoint or used a different rule; inspect exact-boundary laboratory observations and the safety code before deciding if its printed1/0 counts change.

### Fever threshold39°C differs from supplement103°F/39.5°C definition

- REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8): “Fever<39°C for12h”,11(10.3%)/18(16.7%). REPORT [results eTable1 p6](../../../joi190092supp1_prod.pdf#page=6): nonserious fever for12hours “>100.6 to103°F/39.5°C”, serious“≥103°F/39.5°C”. REPORT [results eTables8/9 pp14–15](../../../joi190092supp1_prod.pdf#page=14): “Fever<103degrees for12hours”; these later-period counts remain distinct.
- Rule: C=(F−32)×5/9;103°F=39.444…°C, consistent with39.5 displayed to0.5°C but not the article's39°C cutpoint.39°C=102.2°F. Source duration12hours matches; time-period differences do not explain differing category boundaries.
- Alternative: a rounded/abbreviated category label, unit conversion, or revised threshold might explain it. Human verification: confirm unit/inequality and category definition used for the11/18 counts; inspect temperatures39.0–39.5 and whether printed integer39 was intended only as coarse prose.

### Hemoglobin exact6.5g/dL inclusion differs from final plan

- REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8): nonserious low hemoglobin “>6.5 to<9g/dL lasting<28d”,2(1.9%)/3(2.8%). REPORT [results eTable1 p5](../../../joi190092supp1_prod.pdf#page=5):>6.5 to<9 for<28days, serious<6.5 or<9 for≥28days. REPORT [eTables8/9 pp14–15](../../../joi190092supp1_prod.pdf#page=14) retain>6.5 for nonserious rows. PLAN [finalprotocol p81 Table3](../../../joi190092supp2_prod.pdf#page=81): nonserious“≥6.5 to<9g/dL”,serious<6.5; persistence28days promotes laboratorySAE.
- Rule: exactly6.5 for<28days is nonserious under the final plan but excluded by the report's>6.5 and<6.5 immediate categories. Original protocol thresholds>6.4/<10 are different historical rules and are not silently aligned as current comparators.
- Alternative/human verification: obtain final lab-category code and amendment history for≥ versus>; establish intended treatment of exact6.5 and whether any printed counts include such observations.

### Leukocyte exact1000/µL serious boundary differs from final plan

- PLAN [finalprotocol p81 Table3](../../../joi190092supp2_prod.pdf#page=81): serious≤1000/µL;nonserious>1000 to<2500/µL. REPORT [results eTable1 p5](../../../joi190092supp1_prod.pdf#page=5): serious<1000/µL or<2500 for≥28days;nonserious>1000 and<2500 for<28days. REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8) nonserious3(2.8%)/1(0.9%) uses>1000 and<2500; no serious leukocyte row printed.
- Rule: exactly1000 for<28days is immediately serious under finalPLAN≤1000 but meets neither acuteREPORT threshold. The absence of a serious-results row alone is not the candidate; the explicit defining inequality is.
- Alternative/human verification: confirm units and exact-boundary coding; determine whether≤1000 was intended in eTable1 or whether a later documented rule changed the threshold. No unprinted event count inferred.

### ALT/AST exact5×ULN serious boundary differs from final plan

- PLAN [finalprotocol p81 Table3](../../../joi190092supp2_prod.pdf#page=81) and [p136 §6.2](../../../joi190092supp2_prod.pdf#page=136): nonserious2 to<5×ULN,serious≥5×ULN. REPORT [results eTable1 p5](../../../joi190092supp1_prod.pdf#page=5): nonserious2–5×ULN for<28days;serious>5×ULN or2–5×ULN for≥28days. REPORT [article Table3 p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8) repeats latter rule,nonserious14/8,serious3/2; REPORT [eTable8 p14](../../../joi190092supp1_prod.pdf#page=14) repeats that boundary for its distinct later-period7/0 and2/0 counts.
- Rule: exactly5×ULN for<28days is serious underPLAN≥5 and nonserious underREPORT2–5/>5. Persistence≥28days is otherwise coherent. This is independent of P-value display or observed liver-event count totals.
- Alternative/human verification: establish the inclusive endpoint of report“2 to5” and whether a documented amendment changed≥5 to>5; inspect boundary5 laboratory readings and SAE coding before inferring any count impact.

### Per-protocol sensitivity label uses different adherence cutoff

- REPORT [article Figure2 p7 model4/footnote e](../../../jama_rathinam_2019_oi_190092.pdf#page=7): “Per protocol”,patients who missed<20% of study medication,n184,MTX61/90,MMF54/94,OR1.56(0.84–2.96),P.17; [p6 narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6) repeats<20%-missed sensitivity. PLAN [finalSAP p71 §4.1](../../../joi190092supp3_prod.pdf#page=71): per-protocol excludes major deviations or noncompliance defined<50% received,byselfreport/pillcounts. OriginalSAP[p31](../../../joi190092supp3_prod.pdf#page=31) matches final50%,so disclosed final version alone does not reconcile it.
- Rule: <20%missed means>80%received; excluding<50%received retains≥50% with respect to adherence. E.g.70%received meets plan cutoff and fails report cutoff. This creates a concrete definition mismatch for the named n184/OR1.56 result, not merely an analysis-population complaint. Major-deviation exclusions may also differ, but their omission is not inferred from the report's compressed label.
- Alternative/human verification: an extra80%adherence sensitivity may legitimately be reported under a broad per-protocol shorthand. Confirm whether model4 was intended to implement SAPper-protocol or a distinct adherent-subset analysis; obtain the rule and participant exclusions behind90/94 without presuming different estimates.

### Noninferiority lower-bound decision inequality differs from supplied plan

- PLAN [finalSAP p61 item16](../../../joi190092supp3_prod.pdf#page=61):10%margin; “Methotrexate will be considered non-inferior to mycophenolate if the lower limit of the95%CI for treatment success at6months is less than10%”;one-sidedcomparison. REPORT [article p4 noninferiority results](../../../jama_rathinam_2019_oi_190092.pdf#page=4): lower95%CI risk-difference bound−5.3%“excluded the prespecified10%noninferioritymargin”provides evidence ofMTXnoninferiority. Main risk difference isMTX−MMF9.5%(−5.3,21.8) and methods specify10%absolute margin. Direct visualSAPp61 confirms“less than10%”.
- Comparison rule: for reportedMTX−MMF difference and10%allowable deficit, exclusion is lower bound>−10%;−5.3 satisfies this. The printedPLANlower bound<+10% is a different direction/sign and would also admit lower bounds below−10%. This diagnostic uses report's declared effect orientation, not an assumed raw-risk model. The SAP clause does not explicitly name its contrast, so that uncertainty remains essential.
- Alternative/human verification: the PLANmay contain a sign/inequality typo or intended reverse difference with a different bound; the report's conclusion might use an amended rule. Confirm signed estimand, lower/upper bound, margin sign and formal test from the original analysis specification. No conclusion-impact claim made. This should merge with a statistical-lane observation only if its compared statements and rule are identical.

### Switching-treatment OR model label differs from planned rescue adjustment

- PLAN [finalSAP p61 §3.2.3](../../../joi190092supp3_prod.pdf#page=61): rescue logistic predictors treatment group and reason for first-drug failure,lack of efficacy versus anyotherreason. REPORT [article p4 Methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4): same primary logistic model applied at12months;primary treatmentfixed,site random. REPORT [Table2 p6 footnote b and switched row](../../../jama_rathinam_2019_oi_190092.pdf#page=6): OR4.17(1.32–13.16),P.02 for20/29vs7/20,footnote b“treatment group as a fixed effect and study site as a prespecified random effect.” [p7 narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=7) rounds4.2(1.3–13.2),P.02 coherently.
- Rule: the suppliedPLANrescue primary treatment coefficient conditional on failure reason differs from the labeledREPORTprimary treatment+site model. Main extends the same primary model to all12month results, while its rescueORhas the appropriate new-drug contrast; contrast reversal is not the candidate. Nothing establishes that site and failure-reason models have numerically different ORs, and covariates may have been included but omitted from compressed labels.
- Alternative/human verification: rescueanalysis amendment, supplementary rather thanprimary model, or incompletely described adjustment. Confirm actual design matrix and coefficient output behind4.17 and intended linkage to Aim2; record whether reason-for-failure adjustment was used or an explicitly changed model generated the result. No accusation of protocol violation.

### Dose-reduction comparison test differs from final planned test

- PLAN [finalSAP p61 item15](../../../joi190092supp3_prod.pdf#page=61):“Dose reduction will be compared by arm using logistic regression based on treatment,and other covariates as needed.” REPORT [article p4 StatisticalAnalyses](../../../jama_rathinam_2019_oi_190092.pdf#page=4):“Dose reductions and protocol deviations were compared between treatment groups using a Fisher exact test.” REPORT [p6 dose-reduction result](../../../jama_rathinam_2019_oi_190092.pdf#page=6):MTX21(19.6%),MMF15(13.8%),P.27.
- Rule: logistic-model coefficient inference and Fisher exact comparison are different specified inferential procedures for the same six-month arm-comparison outcome. The counts are not disputed; no alternate P is reconstructed. SAP§4.2 Fisher rule applies to major deviations, not explicitly dose reductions, so does not reconcile this declared dose-reductiontest pair.
- Alternative/human verification: a final analysis amendment or unadjusted supplementary Fisher comparison could explain it. Confirm the statistic/test behindP.27 and whether planned logistic inference was separately performed or the reporting label should identify the changed/supplementary method.

## Handoff and limitations

13 distinct observations emitted without stable C IDs or AI disposition/severity. Boundary inequalities are separate comparisons rather than one vague safety-definition finding. Exact-boundary patients, questionnaire variable identities, rescue-model output, adherence exclusions and noninferiority signed estimand are not supplied; each conditional question is named above. These evidence limitations do not create uncovered source units. All original/final version differences that are explicitly amended remain in the matching register, without candidates solely for changed enrollment thresholds, sites, model versions or projected dates. No source alleges conclusions are wrong; possible downstream extraction impact is limited to the named counts, labels, definitions and inferential results.
