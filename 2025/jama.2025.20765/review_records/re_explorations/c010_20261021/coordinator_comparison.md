# C010 bounded source re-exploration and historical-record comparison

Date: 2026-10-21. This is a targeted follow-up, not a complete Workflow 1.6.2 rerun or human adjudication. No original source or earlier review record was changed. New local files are confined to this directory.

## Independent scope and tools

The existing C010 entry was used to locate the question. The coordinator directly inspected SAP pp92-93 and99, main article pp3 and5, the complete subgroup display in results-supplement p12, the eTable7 association display on pp10-11, and report-wide native-text occurrences of gender, sex, male/female and subgroup terms. Detailed historical conclusions were then compared. A fresh source-only inclusion screener, `/root/c010_source_independent`, was assigned a separate check without access to earlier scientific conclusions. Its assigned artifact is independent_source_check.md.

Direct Poppler pdftotext produced main_p3_p5_layout.txt and results_p12_layout.txt. Source-matched existing images were reused; no new rendering or OCR was needed. Plan text with unusable character mapping was not treated as authority. The independent subtask was restricted to writing only its assigned artifact, with no derivative creation permitted. No external sources, custom Python, raw data or model fitting were used.

## Direct evidence

| Source role and location | Observation |
|---|---|
| PLAN, Supplement1 PDF p92, printed SAP p15, section38, lines2936-2939 | Subgroup sensitivity analyses are specified to evaluate stability of the primary treatment effect; the sentence lists age and continues on p93. |
| PLAN, Supplement1 PDF p93, printed SAP p16, lines2940-2942 | Planned factors include education, occupation, gender (male vs. female), and smoking duration. |
| PLAN, same p93, lines2943-2952 | Each subgroup has a mixed-effects model with site-level random intercept; RR and95%CI are to be computed. The plan calls for qualitative comparison of subgroup RRs/CIs and disclosure of missing confidence intervals, acknowledging limited statistical power and exploratory character. |
| PLAN, Supplement1 PDF p99, printed SAP p22 | Blank Gender/Male/Female rows in a prospective table shell corroborate the plan. They are not a results table with unfilled observed results. |
| REPORT, main PDF p3, printed p338, final Statistical Analysis paragraph | The stated prespecified subgroup list contains age, education, employment and smoking duration, without male/female subgroups. The separate covariate-adjustment description includes sex; that does not provide within-sex treatment effects. |
| REPORT, main PDF p5, printed p340, subgroup-results paragraph | The consistency narrative lists age, education, employment, ability to read SMS and smoking duration, referring to eTable8. It supplies no male/female subgroup treatment effect. |
| REPORT, results-supplement PDF p12, complete eTable8 | All; Age; Education; Occupation; Smoking Duration; Reading SMS. No male/female subgroup rows or missing-CI/nonestimation explanation appears. |
| REPORT, main PDF p5, Table1 | Male counts698/720 and345/360; female counts22/720 and15/360. Total females37/1080. These baseline counts establish composition, not subgroup abstinence numerators or model estimability. |
| REPORT, main PDF p8, Limitations | The text acknowledges participants were almost entirely male (>96%). It does not explicitly connect that limitation to omission or nonestimation of the planned subgroup models. |
| REPORT, results-supplement PDF pp10-11, eTable7 | Cluster characteristics include Male,n(%); the associated RR at the bottom is0.83 (95%CI0.34-2.02). It is not a pair of mHealth-versus-usual-care treatment RRs within male and female subgroups. |

## Planned versus reported subgroup factors

| Factor in the relevant SAP paragraph | Counterpart in complete eTable8 |
|---|---|
| Age | Present |
| Education | Present |
| Occupation | Present |
| Gender, male/female | No subgroup treatment-effect counterpart |
| Smoking duration | Present |

Reading SMS is an additional reported factor; its presence does not supply the absent gender comparison. This bounded follow-up does not register a separate issue about that factor. Gender/sex wording differences are not the issue.

## Historical trajectory

- checkers/cross_source_consistency.md line75: F-XS-004 identifies absent planned male/female treatment-effect results.
- checkers/statistical_pass_1.md line110: F-ST1-006 independently identifies the same planned primary-outcome subgroup analysis; relationship S097.
- screening/inclusion_screen.md lines20 and35: both findings are INCLUDE / MEETS_THRESHOLD and consolidate as C010; RouteA category5.
- verification/evidence_recheck.md line305: confirms source wording and absence from complete report displays; reproduced, with no classification correction. Its historical PENDING_AUDIT field predates the completed audit.
- checkers/statistical_pass_2.md line331: S097 PASS_2_COMPLETE; existing C010 retained without duplicate registration.
- quality/evidence_quality_audit.md line435: inclusion audit CONFIRMED; explicitly distinguishes the eTable7 sex-related association from subgroup treatment contrasts.
- final_report_1_6_2.md line692: stable C010 retained as protocol_report / P_R, all relationships P_R, evidence state reproduced, inclusion audit CONFIRMED; Pending Human Adjudication.

Record paths except the final report are relative to .ai_paper_validation/review_1_6_2/; the final report is directly in .ai_paper_validation/.

## Interpretation and limits

The reproduced observation is a planned exploratory/sensitivity subgroup analysis of the primary outcome with no identified reported male/female treatment RR/CI or corresponding explanation in the complete supplied report package. It does not mean that the entire primary analysis is absent, that sex was omitted as an adjustment covariate, or that two new co-primary endpoints were planned.

Baseline composition, sex adjustment, a sex/cluster-characteristic association, the pooled All subgroup row and sex-specific intervention contrasts are different quantitative relationships. None of the first four replaces the planned male/female treatment-effect results. In particular, an overall predominantly male sample does not make the overall result a male-specific result.

The female baseline total37 is directly supported. Nonestimability, absent outcome variation, model failure or a removal amendment are possible explanations, not reported facts established from that total. The plan's missing-CI disclosure clause gives an explicit source-grounded reason to look for such an explanation, without requiring a preferred replacement analysis. No missing interaction-P finding is asserted: the quoted plan describes qualitative RR/CI comparison, and this follow-up concerns the specified subgroup results.

The source establishes that the supplied SAP specifies the analysis. It does not independently establish when the SAP was locked relative to data access. The existing registration's word prespecified should be understood with that provenance limit. Absence from the supplied package cannot establish that the analyses were never performed. The independent source-only screener separately reached the same bounded RouteA category5 assessment after complete native-text searches of both supplied REPORT documents and direct visual inspection of the relevant displays.

Roles support P_R and protocol_report: prospective SAP versus report methods/results. The article and results supplement agree in not providing the gender rows; their agreement supplies no separate S_C or S_W conflict. Both male/female missing counterparts and both initial checker findings remain one issue.

## Bounded downstream impact

The registered domain is protocol_report, not statistical_results. Potential reuse concerns the availability and recorded scope of planned sex-specific sensitivity evidence. An extractor could overstate coverage by saying all planned subgroup analyses were reported, mistake the eTable7 association RR0.83 for a sex-specific intervention effect, or treat the pooled All estimate as a male-specific result. These are possible extraction pathways, not observed propagation. The article's stated consistency list does not itself claim consistency across sex.

No male/female treatment RR,95%CI, subgroup abstinence numerator or model output is supplied from which to estimate an omitted effect. No change to the overall primary RR, statistical significance, meta-analysis weight, subgroup difference, bias direction or clinical conclusion can be quantified. The absent result does not imply no subgroup difference or an effect favoring either group.

## Integrity

All three original source hashes matched source_hashes_before.sha256 at the start and final checks of this follow-up. The final check of reused_artifact_hashes_before.sha256 produced no failures. The independent screener confirmed that it wrote only its assigned artifact; the coordinator confirmed the four new files are in the allowed c010 directory and no c010 derivatives were created in the older preprocessing directory. No original ledger, screening decision, recheck, audit, report, classification or candidate ID was rewritten.
