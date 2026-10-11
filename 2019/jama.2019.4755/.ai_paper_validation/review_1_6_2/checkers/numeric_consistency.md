# Numeric consistency review

Fresh mandatory numeric specialist; exact scope all56mappedN groups: N001–N043,N100–N106,N200–N205, all supplied-source count and denominator relationships represented by the complete new main/support maps. Source roles: DOC-001/004/005 REPORT; DOC-002/003 PLAN. Complete normative scope and1.6.2contract, current source inventory/tooling and complete maps were read. No old checker/candidate/report conclusions or external sources were used.

## Completion and result

NUMERIC_COMPLETE for every relationship in `relationships/numeric_relationship_inventory.md`. Findings:0. Excluded observations:4. Scientific coverage limitations:None. No C IDs or adjudications are assigned.

Counts checked include randomized2422; allocated1208/1214; received/colonoscopy1131/1153; analysis1075/1059; full288removed; all150postcolonoscopyexclusion reasons; every Table1row and percentage; every cell of main Table2 and its Table3derived proportions; all20eTable2sample rows and40Any-column sums; all9eTable3 and9eTable4confusion matrices and their sex-component totals; every eTable5PPV/NPV metric and visibly printed difference. Safety event and affected-participant counts preserve their distinct units. Means/SD/median/IQR and threshold/timing quantities retain units, ordering and population keys. No person-time quantity or OR/RR/HR is presented as a current-trial effect. Diagnostic proportions and percentage-point differences have the identities named in the supplied SAP, not alternative crude estimates of a model effect.

All matching copies of primary counts and effect inputs agree after population/time matching. Age bins sum1075/1059; most-advanced-finding rows sum1075/1059; nonmissing indication denominators1033/1015 explain Table1percentages. Advanced-neoplasm counts115/109 refer to full analyzed cohorts, while quantitative valid-test disease counts112/102 refer to the primary diagnostic analysis; this availability difference is represented explicitly. The approximate4% primary-analysis reduction statement is compatible with both10/224=4.464%advanced-case loss and92/2134=4.311%valid-result loss;4%display interval[3.5,4.5] overlaps both, without asserting which denominator the statement intended.

## Source confirmation and tooling

Fresh CPU Poppler26.01.0 direct layout extraction commands:
- `pdftotext -layout jama_brenner_2019_oi_190039.pdf .ai_paper_validation/review_1_6_2/preprocessing/numeric-main-layout.txt`
- `pdftotext -layout joi190039supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/numeric-supp-layout.txt`

Both derivatives are new, exclusively owned numeric confirmation outputs. Main/supplement exact table counts were compared against this direct-source layout. PLAN values were checked against the source-linked complete protocol/SAP maps and cited supplied-page locators. DOC-004p7visual distinction from the mapper's direct source render remains authoritative: women's PPV point differences are dashes, with nonvisible embedded text separately recorded. Those tokens are never treated as displayed printed values. Direct source/reused assets remain unchanged. No new OCR/render/fallback was needed.

## Findings

No observation in this numeric scope meets the reproduced inclusion threshold. Inferential interval/test and plan/report status checks are cross-referenced to the independent complete statistical and cross-source stages; this conclusion does not suppress their findings.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [DOC-001p5Table2overallquantitative17sensitivity](../../../jama_brenner_2019_oi_190039.pdf#page=5), REPORT | Printed28.6−22.5=6.1when subtracting rounded percentages, versus6.0difference. Input half-unit intervals[28.55,28.65]−[22.45,22.55]=[6.00,6.20] overlap6.0interval[5.95,6.05];gap0,relative0. Exact32/112−23/102×100=6.0224pp also rounds6.0. | ROUNDING_OR_DISPLAY_PRECISION |
| [DOC-001p5Table3menquantitative10.2PPV](../../../jama_brenner_2019_oi_190039.pdf#page=5), REPORT | Printed26.8−18.1=8.7versus8.8difference. [26.75,26.85]−[18.05,18.15]=[8.60,8.80] overlaps[8.75,8.85];gap0,relative0. Exact33/123−15/83×100=8.7570pp rounds8.8. Other one-tenth apparent difference patterns in main/supplement diagnostics were checked by the same rule and reconcile. | ROUNDING_OR_DISPLAY_PRECISION |
| [DOC-004p4eTable2actualday2](../../../joi190039supp3_prod.pdf#page=4) versus [DOC-004p6eTable4All](../../../joi190039supp3_prod.pdf#page=6), both REPORT | Actual-day2sample totals871/864quantitative and824/831qualitative versus869/862and822/829per-protocol participants. The two-unit differences are sample versus deduplicated participant quantities; [DOC-003p7](../../../joi190039supp2_prod.pdf#page=7), PLAN, explicitly selects first valid test when multiple samples occur same day. No same-denominator inconsistency is reproduced. | CONTEXT_RESOLVES |
| [DOC-004p7eTable5womenPPVdifferences](../../../joi190039supp3_prod.pdf#page=7), REPORT | Visible point cells contain only dashes; nonvisible embedded values−18.2,−25.7,−21.6are not printed comparator values. ArmPPVs and allCIlimits are displayed, but no conflicting displayed point estimate is reproduced. Missing point estimates alone supply no numeric contradiction; inferred values are retained only in arithmetic inventory. | CONDITIONAL_OR_UNREPORTED |

## Evidence boundary

Every reported numeric equality checked either reconciles exactly or has overlapping half-unit display intervals, so no residual relative discrepancy above0.05 was found. Recorded counts remain distinct from sample frequencies and from target values. Statistical-method reproduction of intervals/tests, endpoint hierarchy and omitted prespecified analyses are reviewed independently under allSrelationships. No scientific coverage gap remains in the assigned numeric scope.

