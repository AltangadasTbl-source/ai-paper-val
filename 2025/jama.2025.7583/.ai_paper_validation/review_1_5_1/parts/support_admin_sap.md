# Support Evidence Map: Administrative Addenda and Statistical Analysis Plan

## Scope and method

Assigned direct-source scope was complete and disjoint: `DOC-003-ADMIN` PDF pp. 1-23 and `DOC-005-SAP` PDF pp. 1-9 (32 PDF pages). No old candidate, checker, verifier, quality, or report artifact was consulted. Fresh native and layout text was generated independently for every page. The administrative PDF's image-only technical pages 16-22 were also visually inspected after local rendering; targeted OCR was attempted where native/layout text was empty, but the OCR output was not sufficiently reliable for transcription and the rendered direct source was used to classify content.

Fresh derivative locations:

- `preprocessing/DOC-003-ADMIN/native_text/page-001.txt` through `page-023.txt`; `preprocessing/DOC-003-ADMIN/layout_text/page-001.txt` through `page-023.txt`.
- `preprocessing/DOC-005-SAP/native_text/page-001.txt` through `page-009.txt`; `preprocessing/DOC-005-SAP/layout_text/page-001.txt` through `page-009.txt`.
- Direct-source visual corroboration for ADMIN pp. 16-22: `preprocessing/DOC-003-ADMIN/page_images/page-016.png` through `page-022.png`.

No completed participant results, analysis outputs, tables of trial results, cached workbook values, formulas, or reported inferential results occur in these two assigned sources. The SAP contains prespecified definitions and analysis rules that govern matching to reported results and are therefore mapped below. Administrative forms are blank templates and do not provide trial counts or outcomes.

## DOC-003-ADMIN — page-complete map

| Page | Content and result relevance | Relationship / disposition |
|---:|---|---|
| 1 | Cover: EMPROTECT addenda, protocol version 1.0 dated 2019-10-10, project PAOR18104. | No applicable result relationship. |
| 2 | Contents listing addenda, forms, CE/data-sheet material, and radiological classification. | No applicable result relationship. |
| 3 | Investigator/contact roster, Ile-de-France. | No applicable result relationship. |
| 4 | Investigator/contact roster, provincial centres. | No applicable result relationship. |
| 5 | Centre pairs of neurosurgeon and interventional neuroradiologist. | No applicable result relationship. |
| 6 | Blank serious-adverse-event (SAE) reporting form begins. It identifies PAOR18104, risk C, group fields, and blank age/weight/height/treatment fields. | No reported value; blank data-collection template only. |
| 7 | Continuation of blank SAE form: procedure timeline and event/outcome fields. | No reported value; blank template only. |
| 8 | Continuation of blank SAE form: seriousness criteria and adverse-event description fields. | No reported value; blank template only. |
| 9 | Continuation of blank SAE form, notification/follow-up fields. | No reported value; blank template only. |
| 10 | Blank incident/defect reporting form begins. | No reported value; blank template only. |
| 11 | Continuation of blank incident/defect form. | No reported value; blank template only. |
| 12 | Blank pregnancy notification/follow-up form begins. | No reported value; blank template only. |
| 13 | Continuation: blank pregnancy procedure, medication, and exposure fields. | No reported value; blank template only. |
| 14 | Continuation: blank pregnancy outcome/newborn fields, including units for weight, height, head circumference, and APGAR timepoints. | No reported value; blank template only. |
| 15 | Form signature page. | No applicable result relationship. |
| 16 | CE certificate for EmboSphere arterial-embolization material; certificate dates are administrative/device evidence only. | No trial-result relationship. |
| 17 | Device identification table lists EmboSphere nominal microsphere-size bands (40-120 through 900-1200 micrometres), packaging volumes, codes, and class III. | Product specification, not a reported treatment-result measure; no applicable relationship. |
| 18 | French technical sheet for EmboSphere. It repeats size bands, records syringe volumes of 1 or 2 mL, and states seven size ranges. | Product specification, not a reported treatment-result measure; no applicable relationship. |
| 19 | Technical sheet continuation: handling/storage/sterilization information, including displayed 3-year validity. | Product specification, not a reported treatment-result measure; no applicable relationship. |
| 20 | Technical-sheet continuation. | No applicable trial-result relationship. |
| 21 | Technical-sheet continuation. | No applicable trial-result relationship. |
| 22 | Technical-sheet continuation/end material. | No applicable trial-result relationship. |
| 23 | Radiological-classification addendum. Nakaguchi categories are homogeneous, laminar, separated, and trabecular. Park CT-density classification lists hypodensity <25 HU, homogeneous isodensity 25-35 HU, layered, and mixed. | **AS-N001** (definition): Park classification is an eligibility/baseline covariate definition referenced as an imputation variable in SAP p. 8; no actual classifications or outcomes reported here. |

### DOC-003 definition record

- **AS-N001 — Park cSDH CT-density classification.** Direct observation: ADMIN p. 23 states hypodensity `<25 HU` and homogeneous isodensity `25-35 HU`, alongside layered and mixed types. Cross-source key: SAP p. 8 lists `Park classification` among variables used in the primary-endpoint multiple-imputation phase. This support source supplies the classification label/thresholds, but neither source reports a participant classification distribution or an effect estimate. No candidate inference is made.

## DOC-005-SAP — page-complete map and statistical inventory

| Page | Result-relevant content | Relationship IDs |
|---:|---|---|
| 1 | SAP version 2, dated 2024-03-20, for PAOR18104/NCT04372147; signed/dated 2024-04-15. | Administrative version identity; no results. |
| 2 | Contents. | No applicable relationship. |
| 3 | Trial objective and primary-endpoint definition. Primary endpoint is 6-month cSDH recurrence after index burr-hole surgery; components include homolateral CSDH with midline shift >5 mm or symptomatic homolateral SDH including death; maximal thickness >10 mm at 6-month CT; repeated homolateral surgery; or related new admission. | **AS-S001**, **AS-N002**. |
| 4 | Secondary endpoints and their definitions; sample-size calculation begins. mRS disability/dependency is mRS >=4 at 1 and 6 months, scale 0-6. Major/minor complication definitions specify renal-function persistent decrease >10 points among major complications. Flow chart must present eligible/included/randomized/analyzed counts and lost follow-up per arm. | **AS-S002**, **AS-N003**, **AS-S003**. |
| 5 | Sample size: assumed recurrence 15% control vs 5% intervention, 80% power, overall two-sided alpha 5%; 142/group before loss allowance; Lan-DeMets/O'Brien-Fleming sequential design, interim at 129 participants/37.5% information fraction/nominal alpha 0.001, final alpha 0.05; 20% loss assumption; total 342 (171/group). ITT primary population; modified sensitivity exclusion. Descriptive summary rules. Interim mixed-logistic model, adjustments and deceased-without-prior-recurrence rule. | **AS-S004**, **AS-S005**, **AS-S006**, **AS-S007**. |
| 6 | Conditional power and stopping context; interim reportedly did not meet predefined stopping rule and DSMB recommended continuation. Final primary mixed-logistic model; adjusted absolute risk difference and 95% bootstrap CI; multiple imputation; neurological/undetermined deaths without recurrence considered treatment failures. Prespecified subgroups and sensitivity analyses. | **AS-S008**, **AS-S009**, **AS-S010**. |
| 7 | Secondary-analysis tests/models; two-sided alpha 5%, interim exception 0.001; stopping criteria. | **AS-S011**, **AS-S012**. |
| 8 | Multiple imputation: MICE, 10 datasets, Rubin's rules; specified variables include recurrence, age/sex, unilateral/bilateral status, anticoagulant/antiplatelet, Park classification, baseline and surgical variables. SAP version/change table: version 1 dated 2022-07-11 interim; version 2 dated 2024-02-28 final, with death-definition and wrongly-included-patient sensitivity changes. | **AS-S013**, **AS-N004**. |
| 9 | Completion of change table and software: latest R. | **AS-S013** (completion); no reported result. |

### SAP relationship records

- **AS-S001 — Primary endpoint composite and timepoint (SAP p. 3).** The reported primary outcome must be a 6-month post-index-surgery recurrence rate using the specified composite; component threshold labels are `>5 mm` midline shift and `>10 mm` maximal thickness. Match any main/supplement outcome only after confirming this population, composite, timepoint, and adjudication status.
- **AS-N002 — Primary endpoint adjudication process (SAP pp. 3-4).** An independent committee adjudicates locally reported protocol-defined recurrences and potential related admissions, unscheduled visits/imaging, surgery, or neurological symptoms. This is a definition/process key, not an outcome count.
- **AS-S002 — Secondary endpoint definitions (SAP p. 4).** Repeated homolateral surgery over 6 months; mRS >=4 at months 1 and 6 (mRS 0=no symptoms through 6=death); mortality at months 1 and 6; cumulative CSDH-related hospital duration over 6 months; and procedure-related major/minor complication rates. Comparisons must retain the named endpoint/timepoint.
- **AS-N003 — Complication classification (SAP p. 4).** Major complication includes persistent creatinine-clearance decline of more than 10 points; other major/minor categories are qualitative. This is a rate-label/definition key; no rate is reported in SAP.
- **AS-S003 — Planned flow denominators (SAP p. 4).** CONSORT display is planned to report eligible, included, randomized, analyzed, and lost-to-follow-up counts overall and by arm. This establishes terms for matching, but gives no counts.
- **AS-S004 — Sample-size/sequential-design relationship (SAP pp. 4-5).** Design assumptions are control 15% versus intervention 5%, 80% power, bilateral alpha 5%, 142 per group; two-stage Lan-DeMets/O'Brien-Fleming design with interim `n=129`, information fraction `37.5%`, nominal alpha `0.001`, and final alpha `0.05`; planned total after assumed 20% loss `342`/`171 per group`. These are planning assumptions, not observed results.
- **AS-S005 — Analysis population and sensitivity population (SAP p. 5).** Primary analysis is ITT: every randomized patient analyzed in assigned arm regardless of received treatment. A sensitivity analysis excludes experimental-group patients not embolized after CT angiography. Use this to distinguish ITT versus modified-ITT denominators.
- **AS-S006 — Descriptive analysis convention (SAP p. 5).** Categorical variables: number, percentage, and missing data by modality. Quantitative variables: mean/SD or median/IQR according to normality. This defines compatible summary labels but does not declare a normality test or output.
- **AS-S007 — Interim primary analysis (SAP p. 5).** At 129 randomized patients with known 6-month recurrence status, mixed logistic regression adjusts for treatment, anticoagulant/antiplatelet status, unilateral/bilateral cSDH as fixed effects and centre as random effect; Mantel-Haenszel alternative if nonconvergence. Death without prior recurrence is a recurrence at this interim-analysis description. It also states primary adjudicated/imputed analysis and locally assessed sensitivity analysis.
- **AS-S008 — Interim outcome/conditional-power narrative (SAP p. 6).** SAP reports the interim did not meet the predefined stopping rule and DSMB recommended continuing; no numerical test statistic, P value, event count, or conditional power is supplied. This cannot be numerically reconciled without a matched reported interim result.
- **AS-S009 — Final primary analysis and subgroup/sensitivity rules (SAP p. 6).** Final adjudicated ITT mixed logistic model uses the stated covariates; estimates adjusted absolute 6-month recurrence risk difference plus 95% bootstrap CI; imputation applies. Neurological/undetermined deaths without recurrence are treatment failures. Interactions are planned for unilateral/bilateral and anticoagulant/antiplatelet subgroups. Sensitivities include nonadjudicated, no-imputation (lost follow-up=no event), modified ITT, and exclusion of wrongly included patients.
- **AS-S010 — Death-definition version difference (SAP pp. 5-6, 8-9).** Interim wording treats patients deceased without prior recurrence as recurrence; final plan treats death without recurrence as failure only when neurological or undetermined. SAP version-change table expressly identifies this final-plan recurrence-definition change. Match observed analyses to the declared version/analysis stage before calling values inconsistent.
- **AS-S011 — Planned secondary statistical tests (SAP p. 7).** Repeated surgery/mortality/complications use chi-square or Fisher exact tests; mRS >=4 uses a GEE logistic model with arm, categorical time (1/6 months), and interaction; hospital duration uses Wilcoxon rank-sum; adverse-event and SAE counts use Poisson regression while specified patient proportions use Fisher exact. This establishes effect/test labels but no outputs.
- **AS-S012 — Alpha/stopping rule (SAP p. 7).** Analyses are two-sided alpha 5%, except interim nominal 0.001. Enrollment could stop for group difference at 0.001 or DSMB-assessed very low conditional power; trial ends after last included patient follow-up. This is a planned decision rule, not a result.
- **AS-S013 — Missing-data/SAP-version rules (SAP pp. 8-9).** Primary endpoint missingness uses MICE with 10 datasets and Rubin pooling; named covariates include Park classification (cross-key AS-N001). Version table dates are 2022-07-11 (interim) and 2024-02-28 (final), while cover identifies version 2 as 2024-03-20; the document provides no explanation for this date distinction, so it is recorded as an administrative versioning detail rather than a candidate inference.
- **AS-N004 — Imputation covariate definitions (SAP p. 8).** The named imputation inputs enumerate clinical/baseline variables and CSDH characteristics. They are model-input definitions only; no covariate values, formula output, cached value, or model coefficient is reported.

## Limits and handoff

All 32 assigned PDF pages were directly extracted and mapped. The only limitation is text extraction from image-only ADMIN pp. 16-22: local rendered-page inspection established their certificate/device-data-sheet nature; native/layout text was empty and targeted OCR was unreliable. Those pages contain device specifications, not participant-level outcomes, denominators, effect estimates, or completed statistical results. No quality-control candidate is proposed by this mapper; candidate determination is outside this assigned role.
