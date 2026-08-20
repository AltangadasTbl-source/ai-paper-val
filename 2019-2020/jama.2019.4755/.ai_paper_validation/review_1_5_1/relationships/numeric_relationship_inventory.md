# Stable Numeric and Reporting Relationship Inventory

## Scope and normalization rule

This inventory normalizes every numeric/reporting lane record from the completed main and support extraction maps. A stable `N` ID retains its listed lane record, direct-source provenance, and match key. No candidate assessment, consistency judgment, or suppression has occurred. Relationships that share a topic but differ in source, population, time point, analysis set, test, cutoff, or content are intentionally distinct. Exact values remain in the referenced extraction lane record.

- **Stable numeric/reporting relationships:** 62 (`N001`-`N062`).
- **Lane composition:** 34 main records (`MN001`-`MN034`) and 28 support records (`SN001`-`SN028`).
- **Genuine identical merges:** none; no lane record was removed.

| Stable ID | Lane ID | Direct source location | Relationship coverage | Match key / cross-reference |
|---|---|---|---|---|
| N001 | MN001 | DOC-001 PDF p. 1, Abstract | Randomized design, centres, recruitment/follow-up dates, age range, arm totals, dose and day-2 timing. | `RCT; randomized=2422; aspirin=1208; placebo=1214; day2` |
| N002 | MN002 | DOC-001 PDF p. 2, Trial Design and Trial Population | Advanced-neoplasm definition, 18-centre recruitment, eligibility/exclusions. | `outcome=advanced_neoplasm; definition` |
| N003 | MN003 | DOC-001 PDF p. 2, Trial Design and Trial Population | Two FITs; four kits each; baseline plus days 2/3/4 schedule; 3-month colonoscopy limit. | `FIT_schedule; baseline+day2+day3+day4` |
| N004 | MN004 | DOC-001 PDF p. 3, Randomization; Laboratory Methods | Block size/allocation, quantitative-FIT analytical range, arrival median/IQR, storage temperature. | `quantitative_FIT; analytical_range=0.03-142_ug_Hb/g` |
| N005 | MN005 | DOC-001 PDF p. 3, Outcomes | Primary cutoffs, outcome/test/analysis-set labels, and secondary-outcome list. | `primary; quantitative; sensitivity; day2_scheduled; cutoffs=10.2,17.0` |
| N006 | MN006 | DOC-001 PDF pp. 1, 3-4, Abstract/Results/Figure | Full randomized-to-analysis flow and Figure footnotes. | `flow; randomized=2422; analysis=2134; aspirin=1075; placebo=1059` |
| N007 | MN007 | DOC-001 PDF pp. 1, 3, Abstract/Results | Age/sex, colonoscopy indication, advanced-neoplasm/CRC/adenoma counts and percentages. | `analysis=2134; AN=224/2134; CRC=8; AA=216` |
| N008 | MN008 | DOC-001 PDF p. 4, Table 1 | Sex and all age-band counts/percentages by arm. | `Table1; demographics; aspirin=1075; placebo=1059` |
| N009 | MN009 | DOC-001 PDF p. 4, Table 1 and footnote | Screening/diagnostic indication and missing-indication counts by arm. | `Table1; indication; screening=1599; diagnostic=449; missing=86` |
| N010 | MN010 | DOC-001 PDF p. 4, Table 1 | Most-advanced colonoscopy-finding counts/percentages by arm. | `Table1; colonoscopy_finding; AN=115_vs_109` |
| N011 | MN011 | DOC-001 PDF p. 3, Results | Valid scheduled-day-2 quantitative and qualitative FIT samples by arm. | `valid_FIT; day2_scheduled; quantitative=1030_vs_1012; qualitative=974_vs_969` |
| N012 | MN012 | DOC-001 PDF p. 4, Adverse Events | Adverse/serious adverse event counts, types, arm assignment, recovery statement. | `adverse_events; aspirin=11/7; placebo=6/5` |
| N013 | MN013 | DOC-001 PDF p. 5, Table 2, All | Quantitative 10.2 day-2 ITS TP/FN/TN/FP, sensitivity/specificity and differences/CIs. | `T2; all; quantitative; 10.2; day2_scheduled`; related S004/S006 |
| N014 | MN014 | DOC-001 PDF p. 5, Table 2, All | Quantitative 17.0 day-2 ITS TP/FN/TN/FP, sensitivity/specificity and differences/CIs. | `T2; all; quantitative; 17.0; day2_scheduled`; related S005/S007 |
| N015 | MN015 | DOC-001 PDF p. 5, Table 2, All | Qualitative 10.2 day-2 ITS TP/FN/TN/FP, sensitivity/specificity and differences/CIs. | `T2; all; qualitative; 10.2; day2_scheduled`; related S008 |
| N016 | MN016 | DOC-001 PDF p. 5, Table 2, Men | Male quantitative 10.2 day-2 ITS counts, Se/Sp and differences/CIs. | `T2; men; quantitative; 10.2; day2_scheduled`; related S009 |
| N017 | MN017 | DOC-001 PDF p. 5, Table 2, Men | Male quantitative 17.0 day-2 ITS counts, Se/Sp and differences/CIs. | `T2; men; quantitative; 17.0; day2_scheduled`; related S009 |
| N018 | MN018 | DOC-001 PDF p. 5, Table 2, Men | Male qualitative 10.2 day-2 ITS counts, Se/Sp and differences/CIs. | `T2; men; qualitative; 10.2; day2_scheduled`; related S009 |
| N019 | MN019 | DOC-001 PDF p. 5, Table 2, Women | Female quantitative 10.2 day-2 ITS counts, Se/Sp and differences/CIs. | `T2; women; quantitative; 10.2; day2_scheduled`; related S009 |
| N020 | MN020 | DOC-001 PDF p. 5, Table 2, Women | Female quantitative 17.0 day-2 ITS counts, Se/Sp and differences/CIs. | `T2; women; quantitative; 17.0; day2_scheduled`; related S009 |
| N021 | MN021 | DOC-001 PDF p. 5, Table 2, Women | Female qualitative 10.2 day-2 ITS counts, Se/Sp and differences/CIs. | `T2; women; qualitative; 10.2; day2_scheduled`; related S009 |
| N022 | MN022 | DOC-001 PDF p. 5, Table 3, All | All-participant quantitative 10.2 day-2 ITS PPV/NPV and differences/CIs. | `T3; all; quantitative; 10.2; day2_scheduled`; related S010 |
| N023 | MN023 | DOC-001 PDF p. 5, Table 3, All | All-participant quantitative 17.0 day-2 ITS PPV/NPV and differences/CIs. | `T3; all; quantitative; 17.0; day2_scheduled`; related S010 |
| N024 | MN024 | DOC-001 PDF p. 5, Table 3, All | All-participant qualitative 10.2 day-2 ITS PPV/NPV and differences/CIs. | `T3; all; qualitative; 10.2; day2_scheduled`; related S010 |
| N025 | MN025 | DOC-001 PDF p. 5, Table 3, Men | Male quantitative 10.2 day-2 ITS PPV/NPV and differences/CIs. | `T3; men; quantitative; 10.2; day2_scheduled` |
| N026 | MN026 | DOC-001 PDF p. 5, Table 3, Men | Male quantitative 17.0 day-2 ITS PPV/NPV and differences/CIs. | `T3; men; quantitative; 17.0; day2_scheduled` |
| N027 | MN027 | DOC-001 PDF p. 5, Table 3, Men | Male qualitative 10.2 day-2 ITS PPV/NPV and differences/CIs. | `T3; men; qualitative; 10.2; day2_scheduled` |
| N028 | MN028 | DOC-001 PDF p. 5, Table 3, Women | Female quantitative 10.2 day-2 ITS PPV/NPV and differences/CIs. | `T3; women; quantitative; 10.2; day2_scheduled` |
| N029 | MN029 | DOC-001 PDF p. 5, Table 3, Women | Female quantitative 17.0 day-2 ITS PPV/NPV and differences/CIs. | `T3; women; quantitative; 17.0; day2_scheduled` |
| N030 | MN030 | DOC-001 PDF p. 5, Table 3, Women | Female qualitative 10.2 day-2 ITS PPV/NPV and differences/CIs. | `T3; women; qualitative; 10.2; day2_scheduled` |
| N031 | MN031 | DOC-001 PDF p. 4, Secondary End Points | Narrative pointer to eTable 3 multi-day outcomes and eTable 4 male per-protocol differences/CIs. | `supp3; eT3_multisample; eT4_PP_men`; related N049-N054 |
| N032 | MN032 | DOC-001 PDF p. 5, Discussion | Planned 24-percentage-point sensitivity difference and power-context restatement. | `power; diff=24pp`; related S001/S015 |
| N033 | MN033 | DOC-001 PDF p. 5, Discussion | Dose/timing context: 300 mg, 75/100 mg alternatives, day-2 primary choice. | `dose=300mg; alternatives=75/100mg; day2` |
| N034 | MN034 | DOC-001 PDF p. 6, Limitations | Quantified limitations: approximately 4% exclusions; 22% diagnostic colonoscopy; one-time screening. | `limitations; primary_exclusion~4%; diagnostic=22%; one_time` |
| N035 | SN001 | DOC-002 PDF p. 10, Summary | Preliminary observational ASA-user/non-user sensitivity, male AUC, P values, and specificity statement. | `preliminary_iFOBT_ASA_user_vs_nonuser_sensitivity_AUC_men`; related S013 |
| N036 | SN002 | DOC-002 PDF pp. 10-11, Summary/Synopsis | Proposed randomized 300-mg ASA-placebo design, planned N, timing, tests and reference standard. | `trial_design_300mg_ASA_vs_placebo_iFOBT_colonoscopy` |
| N037 | SN003 | DOC-002 PDF pp. 13-14, §§3.9-3.11 | Protocol planned randomized/primary N, sample days, safety ITT definition. | `planned_N2400_primary_N2000_protocol_day3` |
| N038 | SN004 | DOC-002 PDF pp. 18-21, Figure 2/Table 1 | Protocol kit/tube counts, sampling schedule, colonoscopy timing and ASA-free interval. | `sample_schedule_protocol_day1_day3_day4_day5_eight_kits` |
| N039 | SN005 | DOC-002 PDF pp. 19, 27 | Three-month colonoscopy limit and delay/drop-out rule. | `sensitivity_analysis_colonoscopy_delay_gt3months` |
| N040 | SN006 | DOC-002 PDF p. 24, §6.5 | Randomization-number range 1-4,000 and allocation process. | `randomization_unique_number_1_4000` |
| N041 | SN007 | DOC-002 PDF pp. 26-27, §§6.9-6.11 | Recruitment payment, planned N/duration and stopping threshold. | `protocol_recruitment_stop_25percent_half_time` |
| N042 | SN008 | DOC-002 PDF pp. 30-33, §§8.1-8.5 | Dose ranges and safety-observation/telephone timing. | `safety_single300mg_AE_day1to5` |
| N043 | SN009 | DOC-002 PDF pp. 35-44, 50-62 | Explicit no-applicable result record for administrative/appendix units. | no result match key |
| N044 | SN010 | DOC-003 PDF pp. 2-3, §§1.1-1.3 | SAP design, planned N, tests, reference and dataset/eCRF identity. | `SAP_trial_design_dataset_eCRF` |
| N045 | SN011 | DOC-003 PDF p. 4, §2.1/footnote 1 | FAS/PP/ITS definitions and protocol-to-SAP day relabeling. | `analysis_set_FAS_PP_ITS_day2` |
| N046 | SN012 | DOC-003 PDF p. 6, §3.2 | Primary variable, raw/categorical units, cutoffs and eight colonoscopy categories. | `day2_FOBGold_quantitative_10.2_17ugHbperg_advanced_neoplasms` |
| N047 | SN013 | DOC-003 PDF p. 6, §3.2 | Secondary outcomes, qualitative result levels and derived utilization measures. | `secondary_FD_HbHp_AUC_PPV_NPV_LR_NNT` |
| N048 | SN014 | DOC-003 PDF p. 7, §§3.3-4 | Day calculations and missing/invalid/multiple-sample selection rules. | `missing_invalid_excluded_first_valid_same_day` |
| N049 | SN015 | DOC-003 PDF p. 10, §8 | Explicit no-observed-result reference-page record. | no result match key |
| N050 | SN016 | DOC-004 PDF p. 4, eTable 2 | ASA quantitative returned/valid counts by scheduled and actual collection day. | `eTable2_intervention_quantitative_day2_valid1030_actual758`; related N011 |
| N051 | SN017 | DOC-004 PDF p. 4, eTable 2 | ASA qualitative returned/valid counts by scheduled and actual collection day. | `eTable2_intervention_qualitative_day2_valid974_actual719`; related N011 |
| N052 | SN018 | DOC-004 PDF p. 4, eTable 2 | Control quantitative returned/valid counts by scheduled and actual collection day. | `eTable2_control_quantitative_day2_valid1012_actual747`; related N011 |
| N053 | SN019 | DOC-004 PDF p. 4, eTable 2 | Control qualitative returned/valid counts by scheduled and actual collection day. | `eTable2_control_qualitative_day2_valid969_actual720`; related N011 |
| N054 | SN020 | DOC-004 PDF p. 5, eTable 3, All | All-participant multi-day quantitative/qualitative counts, Se/Sp and differences/CIs. | `eTable3_all_multiday_SeSp_TPFNTNFP`; related N031 |
| N055 | SN021 | DOC-004 PDF p. 5, eTable 3, Men | Male multi-day quantitative/qualitative counts, Se/Sp and differences/CIs. | `eTable3_men_multiday_SeSp`; related N031 |
| N056 | SN022 | DOC-004 PDF p. 5, eTable 3, Women | Female multi-day quantitative/qualitative counts, Se/Sp and differences/CIs. | `eTable3_women_multiday_SeSp`; related N031 |
| N057 | SN023 | DOC-004 PDF p. 6, eTable 4, All | All-participant exact-day-2 per-protocol counts, Se/Sp and differences/CIs. | `eTable4_all_day2_PP_SeSp`; related N031 |
| N058 | SN024 | DOC-004 PDF p. 6, eTable 4, Men | Male exact-day-2 per-protocol counts, Se/Sp and differences/CIs. | `eTable4_men_day2_PP_SeSp`; related N031 |
| N059 | SN025 | DOC-004 PDF p. 6, eTable 4, Women | Female exact-day-2 per-protocol counts, Se/Sp and differences/CIs. | `eTable4_women_day2_PP_SeSp` |
| N060 | SN026 | DOC-004 PDF p. 7, eTable 5, All | All-participant exact-day-2 per-protocol PPV/NPV and differences/CIs. | `eTable5_all_day2_PP_PPV_NPV` |
| N061 | SN027 | DOC-004 PDF p. 7, eTable 5, Men | Male exact-day-2 per-protocol PPV/NPV and differences/CIs. | `eTable5_men_day2_PP_PPV_NPV` |
| N062 | SN028 | DOC-004 PDF p. 7, eTable 5, Women | Female exact-day-2 per-protocol PPV/NPV and differences/CIs. | `eTable5_women_day2_PP_PPV_NPV` |

## Extraction provenance

- Main lane source: `extraction/main_quantitative_evidence.md` (`MN001`-`MN034`).
- Support lane source: `extraction/support_quantitative_evidence.md` (`SN001`-`SN028`).
- Source-location and printed-value detail is preserved in those immutable lane maps; this stable inventory supplies the exhaustive downstream coverage index.
