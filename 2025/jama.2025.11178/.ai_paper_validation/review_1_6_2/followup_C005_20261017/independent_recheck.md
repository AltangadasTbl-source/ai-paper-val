# C005 focused independent source recheck

Scope: C005 only; all registered PDF locations and workbook cells were inspected. Existing rendered source-page images were read visually as the source display; workbook cells were checked directly in the supplied XLSX XML/shared strings. No source or earlier artifact was modified, and no new extraction or rendering was needed. Status remains Pending Human Adjudication.

## Exact locations and observations

| Location | Role by content | Direct observation |
|---|---|---|
| [Main article PDF p.4, printed p.595, Statistical Analysis](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) | REPORT | Prespecified adjustment comprises baseline pain severity; sex, clinical site, rural/medically underserved residency; multisite pain; co-occurring mental health condition. Age is absent from this explicit six-factor list. |
| [Protocol PDF p.56, internal p.44, section 15.5, Version 5.0, 10 November 2022](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56) | PLAN | Primary-analysis adjustment list contains the same six factors, without age. |
| [SAP PDF p.20, sections 13–14, Version 6.0, 18 July 2024](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20) | PLAN | Section 14 repeats the six-factor primary adjustment list without age. Section 13 explicitly includes age among candidate baseline variables and specifies age ≥65 years as a subgroup. Those statements establish prospective interest in age, but do not make age a fixed primary adjustment factor. |
| [Results supplement PDF p.4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4) | REPORT | Opening sentence gives the six-factor SAP list. Later in the same paragraph, the “base set of pre-specified adjustment variables” lists baseline pain severity, **age**, sex, clinical site, residency, multisite pain and mental health conditions. Thus the same paragraph describes a seven-factor base set as prespecified. |
| [Results supplement PDF p.7, eTable 2](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7) | REPORT | “Variables included in all models” includes age ≥65 vs <65 years. Education and unemployment appear separately as additional selected imputation/estimation covariates. |
| [Results supplement PDF p.8, eTable 3, Age ≥65 row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8) | REPORT | Fitted linear imputation model includes age: coefficient 0.19, 95% CI 0.12–0.27, P=.013. |
| [Results supplement PDF p.9, eTable 4, Age ≥65 vs <65 row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9) | REPORT | Primary weighted estimation model includes age: RR 1.15, 95% CI 1–1.33, P=.046. Treatment RRs on this page are 1.28 for painTRAINER and 1.54 for health coach versus usual care plus. |
| [Results supplement PDF p.10, eTable 5, Age ≥65 row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10) | REPORT | Logistic nonresponse weighting model includes age: OR 0.97, 95% CI 0.70–1.35, P=.859. |
| [Supplied workbook, worksheet eTable 3, G2, A10 and G10](../../../joi250046supp5_prod_1755300121.16087.xlsx) | REPORT | Original XML resolves G2 to “Pre-specified Adjustment Variables”, A10 to “Age in years” with superscript c, and G10 to “X”. Shared-string indices are 138, 4 and 146 respectively. This corroborates the report's prespecified-age designation. |

## Mechanical evidence fields

- Location found: yes, all registered locations above.
- Source text/value matched: yes. Comparator matched: yes; the six-factor prospective primary-model list differs from the report's seven-factor fixed base set, and the report models visibly contain age.
- Applicable rule: Route A category 5, an analysis described as prespecified whose fixed covariate designation is not present in the supplied prospective primary-model specification. The issue is specification/status, not the statistical permissibility of adjusting for age.
- Logical comparison reproduced: age is not in the explicit section 14 primary adjustment set but is included in the report's explicitly prespecified base set. Display-precision interval check: not applicable to categorical covariate membership; no arithmetic rounding could explain membership. The age coefficient/CI/P rows are cited only as model-membership evidence here; their inferential compatibility is outside C005.
- Necessary inputs available: explicit plan and report covariate lists; report fitted-model membership; SAP section 13 prospective candidate/subgroup context; original workbook flag.
- Missing inputs/definitions: dated prospective specification explicitly fixing age in the primary base set; timing and rationale of that decision; precise mapping of SAP candidate-variable language to fixed versus selected primary covariates; otherwise identical treatment-effect fits with and without age, including identical imputation, weighting and adjustment choices; individual data and analysis code.
- Source-grounded alternative: age may have been prospectively intended under the SAP's broader baseline-candidate/subgroup provisions or in an additional specification not supplied. Report p.4 describes additional covariate selection based on missingness and outcome prediction. Such selection can explain additions to a final model, but does not by itself explain calling age a member of the already prespecified fixed base set. Age is placed in the base set before that additional selection, not presented as one of the resulting additions.
- Amendment context: SAP pp.3–4 visually inspected. The visible July 2024 amendment entries concern outcome descriptions, IPW and masking; they do not explicitly add age to the fixed base set. This is not proof that no additional specification ever existed.
- Direct observation versus explanation: the printed membership/designation discrepancy and actual fitted age rows are direct observations. A later model change, an omitted plan detail, or a reporting abbreviation are alternative explanations, not established events. Actual age inclusion does not establish post hoc decision timing, bias or an effect on significance.
- Exact remaining human question: which dated prospective specification established age ≥65 versus <65 as a fixed primary base-adjustment variable; if none was intended, how should the six-factor prospective list and seven-factor report designation be reconciled, and how much do otherwise identical primary treatment estimates change when age alone is varied?

## Classification

- Document roles confirmed: main/results supplement/workbook REPORT; protocol/SAP PLAN by prospective content.
- Primary relationship: P_R, because report prespecification is compared directly with prospective primary-model content.
- All relationships: P_R, S_C, S_W. S_C compares the main report's six-factor prespecified list with the results supplement's seven-factor list; S_W compares the two explicit lists within results-supplement p.4. No P_P: protocol and SAP primary lists agree. Workbook/model coefficient rows corroborate the report side rather than creating additional relationships by themselves.
- Review domain: protocol_report, consistent with P_R precedence. No classification correction required.
- Evidence state: **reproduced**. Determining fact: correctly read explicit lists retain the fixed-primary prespecification discrepancy despite the SAP's broader acknowledgment of age as a candidate/subgroup.

## Bounded downstream impact

The issue directly affects reproducibility and coding of which covariates were prespecified versus additionally selected. A model-based effect estimate extracted from this study should be recorded as actually age-adjusted; the main prose alone is insufficient for complete model reconstruction.

Age enters the reported imputation, estimation and weighting models, so differences in its inclusion could plausibly affect treatment RRs, uncertainty and adjusted absolute response probabilities. The magnitude and direction cannot be determined from these materials. The age RR 1.15 is an age association conditional on the fitted model, **not** a 15% change in treatment effect, and P=.046 is not evidence that adding age changes treatment significance.

For a conventional efficacy meta-analysis that extracts the published treatment RRs and intervals, C005 supplies no alternative treatment estimate and establishes no numerical alteration to the extracted RR/CI. For a review evaluating prespecification or reconstructing models, it is a substantive documentation distinction. Do not infer that the primary efficacy conclusion changes; the necessary otherwise-identical with/without-age comparison is absent.
