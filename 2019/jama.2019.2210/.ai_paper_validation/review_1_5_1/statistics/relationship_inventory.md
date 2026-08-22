# Canonical Statistical Relationship Inventory

Stable global IDs S001-S083 cover every mapped inferential-statistical relationship across all 96 direct-source pages. Full source details are preserved below from the four disjoint mapper parts. Statistical pass statuses are initialized here and finalized after both fresh reviews.

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE

## DOC-001 main article
# Main Statistical Relationship Part — DOC-001

This part inventories local inferential-statistical relationships `S001`-`S015` from the complete main-article PDF pp. 1-9. These are provisional local keys only; a later reviewer assigns global `S` IDs and assesses compatibility without inferring unreported model details.

| Key | Exact direct PDF locations | Population, time, contrast, model/measure | Printed estimate, interval, statistic/P value | Relationship and cross-document match key |
|---|---|---|---|---|---|
| S001 | pp. 1,4,6 Figure 2A | All randomized (251 vs 166); relapse or death; time since randomization; Cox HR. | HR 0.76, 95% CI 0.50-1.14, P=.18; 5-y RFS 77% vs 69%. | CI contains 1 and P is non-significant at .05; repeated across abstract/narrative/figure. `XMAIN-RFS5-77-69`. |
| S002 | pp. 1,4,6 Figure 2B | All randomized; all-cause death; Cox HR. | HR 0.95, 95% CI 0.57-1.57, P=.83; 5-y OS 82% vs 81%. | CI contains 1 and P is non-significant; repeated abstract/narrative/figure. `XMAIN-OS5-82-81`. |
| S003 | pp. 1,4-5,7 Figure 3A | Baseline 25(OH)D middle 20-40 ng/mL (vitamin D n=142, placebo n=90); relapse or death; Cox HR. | HR 0.46, 95% CI 0.24-0.86, P=.02; 5-y RFS 85% vs 71%. | CI excludes 1 and P<.05; narrative/figure match. `XMAIN-25OHD-MIDDLE-RFS`. |
| S004 | pp. 4-5,7 Figure 3B | Baseline 25(OH)D low <20 ng/mL (102 vs 71); relapse or death; Cox HR. | HR 1.15, 95% CI 0.65-2.05, P=.63. | CI contains 1 and P non-significant; narrative/figure match. `XMAIN-25OHD-LOW-RFS`. |
| S005 | pp. 1,5,7 Figure 3 | Low-versus-middle baseline 25(OH)D interaction for relapse/death in the stated Cox interaction model. | P=.04 for interaction. | The interaction P is distinct from within-subgroup P values; high group excluded. `XMAIN-25OHD-RFS-INTERACTION`. |
| S006 | pp. 5,7 Figure 3C | Middle 25(OH)D (142 vs 90); all-cause death; Cox HR. | HR 0.60, 95% CI 0.28-1.30, P=.20. | CI contains 1; narrative/figure match. `XMAIN-25OHD-MIDDLE-DEATH`. |
| S007 | pp. 5,7 Figure 3D | Low 25(OH)D (102 vs 71); all-cause death; Cox HR. | HR 1.36, 95% CI 0.66-2.81, P=.41. | CI contains 1; narrative/figure match. `XMAIN-25OHD-LOW-DEATH`. |
| S008 | pp. 5,7 Figure 3 | Low-versus-middle interaction for all-cause death. | P=.13 for interaction. | Distinct interaction analysis. `XMAIN-25OHD-DEATH-INTERACTION`. |
| S009 | pp. 6-7 Table 2/Figure 2C | All randomized; relapse with non-relapse death as competing risk; competing-risk regression subdistribution HR. | Subdistribution HR 0.75, 95% CI 0.48-1.17, P=.21. | Measure is subdistribution HR, not ordinary Cox HR; CI includes 1. `XMAIN-COMPETING-RISK-RELAPSE`. |
| S010 | pp. 6-7 Table 2 | Low 25(OH)D: competing-risk relapse subdistribution HR 1.18 (0.64-2.19), P=.59. Middle: 0.44 (0.21-0.89), P=.02. Low-vs-middle interaction P=.04. | Same population subgroup definition as S003/S004 but distinct outcome/model measure. | Table-label distinction is required for cross-source matching. `XMAIN-COMPETING-RISK-25OHD`. |
| S011 | p. 7 Table 2 | Cancer-specific death, HR (95% CI): total 1.09 (0.58-2.01), P=.80; low 1.45 (0.63-3.38), P=.38; middle 0.78 (0.29-2.10), P=.63; interaction P=.35. | Cox HR; vitamin-D direction footnote says HR>1 indicates decreased probability with vitamin D. | All listed CIs contain 1. `XMAIN-CANCER-SPECIFIC-DEATH`. |
| S012 | p. 7 Table 2 | Noncancer death, HR (95% CI): total 0.70 (0.29-1.73), P=.44; low 1.11 (0.26-4.65), P=.89; middle 0.39 (0.11-1.39), P=.15; interaction P=.27. | Cox HR; same directional footnote. | All listed CIs contain 1. `XMAIN-NONCANCER-DEATH`. |
| S013 | p. 6 | Age-quartile-adjusted analysis, all randomized: relapse/death adjusted HR 0.66 (0.43-0.99), P=.048; death adjusted HR 0.81 (0.48-1.36), P=.42. Stage-I-adjusted analyses: no significant differences (no numeric estimates printed). | Adjustment changes from unadjusted main analysis; stage-I numeric values unavailable. | Estimate/CI/P compatibility is assessable for age-adjusted values; do not infer stage-I estimates. `XMAIN-AGE-ADJUSTED`. |
| S014 | p. 6 | Within-group Wilcoxon signed-rank and between-group Mann-Whitney analyses: 25(OH)D vitamin D P<.001, placebo P=.91; 1-y change ratio 87% vs 0%, P<.001. Calcium vitamin D P=.09, placebo P=.44; change ratio 0% vs 0%, P=.10. | Test labels and sidedness are not restated for each displayed P value. | Displayed `<.001` values are not display-zero values. `XMAIN-BIOCHEMICAL-PVALUES`. |
| S015 | pp. 3,6 | Proportional-hazards assumption test not significant; 7 missing 25(OH)D observations; 50-imputation results consistent with primary results; SNP and listed post hoc subgroup interactions not significant, without numeric outputs on these pages. | Qualitative statistical claims with named methods but no printed statistic/P value. | Must be retained as matching narrative claims but cannot be mechanically reconstructed further from DOC-001 alone. `XMAIN-QUALITATIVE-STAT-CLAIMS`. |

**No-applicable record:** DOC-001 PDF p. 9 has no main-study inferential statistic; bibliographic reference numerals are excluded from this inventory.

## DOC-002 protocol/SAP and DOC-004 data-sharing statement
# Protocol Statistical Relationship Inventory

All identifiers are provisional `PS` keys for coordinator reconciliation. All are planned statistical relationships except the explicitly labelled background citations.

| Provisional key | Planned or observed | Statistical definition or relationship | Exact source location | Main/results matching key |
|---|---|---|---|---|
| S016 | Planned | Sample size uses a two-sample survivor-function log-rank test, Freedman method: null H0 S1(t)=S2(t); alpha=0.0500 two-sided; power=0.8000; survivor functions s1=0.6200 and s2=0.7500; displayed h ratio=0.6018; p1=0.4000; withdrawal=1.00%; E=120; N=400; N1=160; N2=240. Stata command: `st power log rank 0.62 0.75, n ratio(1.5) wd prob (0.01)`. | DOC-002 PDF p. 30 | Design-stage RFS power calculation; do not equate with observed HR, event count, or study N. |
| S017 | Planned | Annual interim analyses are planned after entry of 200 patients; Peto stopping-boundary significance threshold is P<0.001. The final SAP does not state that an interim analysis occurred. | DOC-002 PDF p. 31 | Interim analysis; threshold and timing only. |
| S018 | Planned | RFS and OS: intent-to-treat Kaplan-Meier survival curves and Cox proportional-hazards model; effect measure HR with 95% CI. | DOC-002 PDF pp. 19, 31 | Endpoint=RFS or OS; population=ITT; model=Cox; effect=HR; CI=95%. |
| S019 | Planned | Changes in 25(OH)D levels use Wilcoxon signed-rank tests. | DOC-002 PDF p. 31; initial plan p. 14 | Biomarker=25(OH)D; within-person/change analysis; test=Wilcoxon signed-rank. |
| S020 | Planned | Baseline/patient-characteristic comparisons: Student t test for normally distributed continuous variables, Mann-Whitney test for non-normal continuous variables, and chi-square tests for dichotomous outcomes. | DOC-002 PDF p. 31; initial plan p. 14 | Baseline characteristics; contrast=Vitamin D vs placebo; test conditional on variable distribution/type. |
| S021 | Planned | Relapse and safety outcomes are to be evaluated using risk ratio (RR). | DOC-002 PDF p. 31; initial plan p. 14 | Outcome=relapse/safety; effect=RR; distinguish from HR for time-to-event endpoints. |
| S022 | Planned | All reported P values are two-sided; P<0.05 is the stated statistical-significance convention. | DOC-002 PDF p. 31; initial plan p. 14 | General P-value convention; interpret only with matched model/endpoint. |
| S023 | Planned | Subgroup interaction: P for interaction is computed using multiplicative variables; results are not corrected for multiple comparisons. Page 31 defines 25(OH)D strata as <20, >=20 to <=40, and >40 ng/mL; p. 23 prints the high stratum as `high (40 ng/mL)` without an inequality. VDR strata are FokI/BsmI/CDX2/TaqI/ApaI and DBP strata are DBP1/DBP2. | DOC-002 PDF p. 31; pp. 23, 27 | Subgroup/interactions; model interaction P; no multiplicity adjustment; retain both printed cutoff labels. |
| S024 | Planned/version history | Initial SAP (2008-12-25) has blank sample-size and interim-analysis sections, while final SAP specifies the 400-person calculation and interim plan. Change summary states target N=400 was fixed before trial start (2009-10-08). | DOC-002 PDF pp. 14-15, 30-31, 45 | Protocol-version comparator; not a conflicting observed result. |
| S025 | Background only, not trial result | External background citation reports FokI genotype median-survival comparison with log-rank P=0.005. This is not a study analysis plan or observed AMATERASU result. | DOC-002 PDF pp. 3, 6, 18, 21-22 | No main-paper match; background-only statistical citation. |
| S026 | Background only, not trial result | External COPD genetic association: rs7041 homozygous at-risk T-allele carriers have 25% lower 25(OH)D; cited P<0.0001. This is not an AMATERASU result. | DOC-002 PDF p. 22 | No main-paper match; background-only statistical citation. |

## Statistical no-applicable units and limitations

- DOC-004 PDF p. 1 reports availability conditions only; it has no observed or planned statistical result.
- The source supplies no observed treatment effect, confidence interval, P value, subgroup result, sensitivity result, model coefficient, standard error, or analyzed denominator. Consequently these records are comparison keys and definitions for matching elsewhere, not inferential consistency conclusions.
- The protocol does not specify covariate adjustment, proportional-hazards diagnostics, missing-data method, or the exact interaction model parameterization beyond multiplicative variables. Those omissions must not be filled by inference.

## DOC-003 results supplement pp. 1-21
# DOC-003 Results Supplement, Shard A: Statistical Relationship Inventory

Provisional statistical keys are local to this shard. Locations refer to `joi190023supp2_prod.pdf` PDF pages. All reported intervals are printed as 95% CIs. These records map reported inferential relationships and do not diagnose candidates.

## Average 25(OH)D Cox model (eTable 1)

Reference stratum is <20 ng/mL. `HR` lines and `AHR` lines are distinct reported models; the sole printed adjustment is vitamin D supplementation. Match base: `AVG25OHD|OUTCOME|STRATUM|MODEL`.

| Provisional key | p. | Outcome; stratum; model | HR (95% CI); P |
|---|---:|---|---|
| S027 | 4 | Relapse/death; 20-<30 ng/mL; HR | 0.62 (0.37 to 1.02); .06 |
| S028 | 4 | Relapse/death; 20-<30; AHR | 0.61 (0.37 to 1.01); .05 |
| S029 | 4 | All-cause death; 20-<30; HR | 0.66 (0.35 to 1.24); .20 |
| S030 | 4 | All-cause death; 20-<30; AHR | 0.64 (0.34 to 1.20); .16 |
| S031 | 4 | Relapse/death; 30-<40; HR | 0.47 (0.27 to 0.84); .01 |
| S032 | 4 | Relapse/death; 30-<40; AHR | 0.44 (0.24 to 0.82); .009 |
| S033 | 4 | All-cause death; 30-<40; HR | 0.39 (0.18 to 0.84); .02 |
| S034 | 4 | All-cause death; 30-<40; AHR | 0.33 (0.15 to 0.74); .007 |
| S035 | 4 | Relapse/death; 40-<50; HR | 0.29 (0.11 to 0.74); .01 |
| S036 | 4 | Relapse/death; 40-<50; AHR | 0.26 (0.10 to 0.71); .008 |
| S037 | 4 | All-cause death; 40-<50; HR | 0.44 (0.17 to 1.16); .10 |
| S038 | 4 | All-cause death; 40-<50; AHR | 0.34 (0.12 to 0.96); .04 |
| S039 | 4 | Relapse/death; >=50; HR | 0.44 (0.21 to 0.96); .04 |
| S040 | 4 | Relapse/death; >=50; AHR | 0.40 (0.18 to 0.92); .03 |
| S041 | 4 | All-cause death; >=50; HR | 0.55 (0.24 to 1.29); .17 |
| S042 | 4 | All-cause death; >=50; AHR | 0.43 (0.17 to 1.08); .07 |

## Baseline 25(OH)D multiple-imputation Cox model (eTable 2)

Match base: `BASELINE25OHD|OUTCOME|STRATUM|MULTIPLE_IMPUTATION`. The table prints HR rather than adjusted-HR and gives no additional model-adjustment label.

| Provisional key | p. | Outcome; baseline stratum | HR (95% CI); P |
|---|---:|---|---|
| S043 | 6 | Relapse/death; 0-<20 ng/mL | 1.15 (0.65 to 2.05); .63 |
| S044 | 6 | Relapse/death; 20-40 ng/mL | 0.46 (0.24 to 0.86); .02 |
| S045 | 6 | All-cause death; 0-<20 ng/mL | 1.36 (0.66 to 2.81); .41 |
| S046 | 6 | All-cause death; 20-40 ng/mL | 0.60 (0.28 to 1.30); .20 |

## eFigure 1 post hoc curve annotations

These chart annotations match eTable 1 unadjusted HR results for the respective outcome/stratum, but eTable 1 calls its comparison stratum <20 ng/mL whereas the chart title abbreviates it as `~20 ng/mL`.

| Provisional key | p. | Outcome; comparison | HR (95% CI); P | Main-paper matching key |
|---|---:|---|---|---|
| S047 | 2 | Relapse/death; ~20 vs 40-50 ng/mL | 0.29 (0.11 to 0.74); .01 | `AVG25OHD_POSTHOC|RELAPSE_DEATH|40_50_VS_LT20|UNADJUSTED_HR` |
| S048 | 3 | All-cause death; ~20 vs 30-40 ng/mL | 0.39 (0.18 to 0.84); .02 | `AVG25OHD_POSTHOC|ALL_CAUSE_DEATH|30_40_VS_LT20|UNADJUSTED_HR` |

## Prespecified SNP-subgroup curve annotations (eFigure 3A-O)

Every panel is a relapse/death cumulative-hazard comparison of vitamin D versus placebo in the named polymorphism subgroup. The panel prints a treatment HR, 95% CI, two-sidedness/test/model/adjustment not stated, P, and P interaction. Match base: `SNP|GENOTYPE|RELAPSE_DEATH|VITAMIND_VS_PLACEBO`.

| Provisional key | p. | Subgroup | HR (95% CI); P | P interaction |
|---|---:|---|---|---|
| S049 | 7 | FokI CC | 0.65 (0.34 to 1.26); .20 | .65 |
| S050 | 8 | FokI CT | 0.77 (0.42 to 1.43); .41 | .90 |
| S051 | 9 | FokI TT | 0.97 (0.32 to 2.88); .95 | .67 |
| S052 | 10 | BsmI AA | 0.44 (0.03 to 7.16); .56 | .66 |
| S053 | 11 | BsmI AG | 0.60 (0.24 to 1.48); .27 | .50 |
| S054 | 12 | BsmI GG | 0.86 (0.52 to 1.41); .55 | .38 |
| S055 | 13 | CDK2 GG | 0.69 (0.34 to 1.38); .29 | .64 |
| S056 | 14 | CDK2 GA | 0.72 (0.39 to 1.32); .28 | .63 |
| S057 | 15 | CDK2 AA | 1.82 (0.48 to 6.88); .38 | .19 |
| S058 | 16 | ApaI GG | 1.00 (0.49 to 2.05); .99 | .35 |
| S059 | 17 | ApaI GT | 0.70 (0.38 to 1.27); .24 | .63 |
| S060 | 18 | ApaI TT | 0.53 (0.15 to 1.84); .32 | .49 |
| S061 | 19 | TaqI TT | 0.87 (0.52 to 1.46); .60 | .35 |
| S062 | 20 | TaqI TC | 0.49 (0.22 to 1.10); .08 | .20 |
| S063 | 21 | TaqI CC | HR/CI not estimable: printed `-` (`- to -`); P=1.00 | `-` |

## Source-linked duplicate match records

eFigure 1A annotation (S047) and eTable 1 relapse/death 40-<50 unadjusted HR (S035) print the identical HR, CI, and P. eFigure 1B annotation (S048) and eTable 1 all-cause-death 30-<40 unadjusted HR (S033) print the identical HR, CI, and P. They are matched repeated presentations of the same result and should be cross-referenced rather than treated as independent estimates in a merged inventory.

## DOC-003 results supplement pp. 22-41
# Support Results Shard B — Statistical Relationship Inventory

## Scope and statistical definition

Provisional `BS` records cover every displayed inferential result in DOC-003 PDF pages 22-41: a subgroup-specific hazard ratio for relapse or death, its printed 95% confidence interval, its P value, and the printed P interaction.  `P interaction` is printed without a stated interaction model, test, degrees of freedom, sidedness, or adjustment.  The pages also do not specify the hazard-ratio reference orientation.  Those omissions are recorded as matching limitations; no model/test relationship is inferred.

| Provisional key | Exact PDF location | Subgroup / analysis label | Printed statistical result | Cross-source match key | Mapping status |
|---|---|---|---|---|---|
| S064 | DOC-003 p. 22, eFigure 3P | DBP1 TT; prespecified | HR 0.71, 95% CI 0.42 to 1.22; P=0.22; P interaction=0.63 | `relapse_or_death|HR|DBP1_TT|prespecified|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S065 | DOC-003 p. 23, eFigure 3Q | DBP1 TG; prespecified | HR 1.00, 95% CI 0.44 to 2.24; P=0.99; P interaction=0.49 | `relapse_or_death|HR|DBP1_TG|prespecified|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S066 | DOC-003 p. 24, eFigure 3R | DBP1 GG; prespecified | HR 0.65, 95% CI 0.14 to 2.92; P=0.57; P interaction=0.91 | `relapse_or_death|HR|DBP1_GG|prespecified|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S067 | DOC-003 p. 25, eFigure 3S | DBP2 CC; prespecified | HR 0.60, 95% CI 0.34 to 1.05; P=0.07; P interaction=0.16 | `relapse_or_death|HR|DBP2_CC|prespecified|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S068 | DOC-003 p. 26, eFigure 3T | DBP2 CA; prespecified | HR 1.19, 95% CI 0.55 to 2.60; P=0.66; P interaction=0.16 | `relapse_or_death|HR|DBP2_CA|prespecified|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S069 | DOC-003 p. 27, eFigure 3U | DBP2 AA; prespecified | HR 0.80, 95% CI 0.20 to 3.20; P=0.75; P interaction=1.00 | `relapse_or_death|HR|DBP2_AA|prespecified|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S070 | DOC-003 p. 28, eFigure 4A | Men; post hoc | HR 0.59, 95% CI 0.37 to 0.97; P=0.04; P interaction=0.13 | `relapse_or_death|HR|men|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S071 | DOC-003 p. 29, eFigure 4B | Women; post hoc | HR 1.18, 95% CI 0.56 to 2.51; P=0.66; P interaction=0.13 | `relapse_or_death|HR|women|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S072 | DOC-003 p. 30, eFigure 5A | Age ≤65 y; post hoc | HR 0.86, 95% CI 0.44 to 1.68; P=0.65; P interaction=0.48 | `relapse_or_death|HR|age_le_65y|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S073 | DOC-003 p. 31, eFigure 5B | Age >65 y; post hoc | HR 0.63, 95% CI 0.37 to 1.05; P=0.07; P interaction=0.48 | `relapse_or_death|HR|age_gt_65y|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S074 | DOC-003 p. 32, eFigure 6A | BMI <25 kg/m2; post hoc | HR 0.75, 95% CI 0.49 to 1.16; P=0.20; P interaction=0.87 | `relapse_or_death|HR|BMI_lt_25_kg_m2|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S075 | DOC-003 p. 33, eFigure 6B | BMI ≥25 kg/m2; post hoc | HR 0.88, 95% CI 0.22 to 3.55; P=0.86; P interaction=0.87 | `relapse_or_death|HR|BMI_ge_25_kg_m2|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S076 | DOC-003 p. 34, eFigure 7A | Esophageal cancer; subgroup analysis | HR 1.01, 95% CI 0.42 to 2.44; P=0.99; P interaction=0.65 | `relapse_or_death|HR|esophageal_cancer|subgroup|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S077 | DOC-003 p. 35, eFigure 7B | Gastric cancer; subgroup analysis | HR 0.84, 95% CI 0.40 to 1.76; P=0.64; P interaction=0.88 | `relapse_or_death|HR|gastric_cancer|subgroup|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S078 | DOC-003 p. 36, eFigure 7C | Colorectal cancer; subgroup analysis | HR 0.69, 95% CI 0.39 to 1.24; P=0.22; P interaction=0.66 | `relapse_or_death|HR|colorectal_cancer|subgroup|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S079 | DOC-003 p. 37, eFigure 8A | Stage I; post hoc | HR 0.39, 95% CI 0.14 to 1.13; P=0.08; P interaction=0.14 | `relapse_or_death|HR|stage_I|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S080 | DOC-003 p. 38, eFigure 8B | Stage II; post hoc | HR 1.20, 95% CI 0.51 to 2.80; P=0.68; P interaction=0.23 | `relapse_or_death|HR|stage_II|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S081 | DOC-003 p. 39, eFigure 8C | Stage III; post hoc | HR 0.86, 95% CI 0.51 to 1.46; P=0.58; P interaction=0.62 | `relapse_or_death|HR|stage_III|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S082 | DOC-003 p. 40, eFigure 9A | Adenocarcinoma; post hoc | HR 0.70, 95% CI 0.43 to 1.13; P=0.14; P interaction=0.47 | `relapse_or_death|HR|adenocarcinoma|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |
| S083 | DOC-003 p. 41, eFigure 9B | Non-adenocarcinoma; post hoc | HR 1.18, 95% CI 0.54 to 2.60; P=0.68; P interaction=0.47 | `relapse_or_death|HR|non_adenocarcinoma|post_hoc|Vitamin_D_vs_Placebo|95CI` | MAPPED |

## Explicit no-applicable records

- No display-zero P value is present in this shard.
- No test statistic, standard error, event count, model formula, adjustment set, stated sidedness, or stated interaction-test definition is printed in the assigned pages; none is reconstructed.
- No table footnote, protocol/SAP instruction, workbook formula/cached value, or structured-data inferential result is within this shard.
