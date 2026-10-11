# Statistical consistency review — pass 1

Runtime agent ID: 01a12955-bf9a-7752-8bc3-60a9eb6b0913. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN.

Exact scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Rebuilt the canonical statistical inventory from the current main/support maps and exact source text. No legacy scientific decisions or other current checkers' findings were used as discovery inputs. All 82 relationships have PASS_1_COMPLETE, including every constituent comparison, in statistics/relationship_inventory.md. Results: 11 findings and 9 excluded observations. No source access was blocked. A different fresh agent must complete pass 2.

Every inferential tuple was checked for estimate containment, endpoint order, null/95% CI/.05 P agreement, and direction. No categorical interval-versus-P conflict or estimate outside its interval was observed. Numerical centered-interval discrepancies are registered separately below. Statistical method and prospective design relationships were reviewed without questioning internally coherent choices. Normal and two-proportion calculations are labelled diagnostics; they do not identify unstated tests, variance estimators, MI degrees of freedom, or covariance matrices. No severity, disposition, correction, or clinical recommendation is assigned.

## Findings

### F-ST1-001

**Issue:** The total sample-size requirement and four cell requirements do not reconcile.

**Locations and roles:** REPORT [main article PDF p.4, Sample Size](../../../jama_bot_2019_oi_190007.pdf#page=4). S005. Relationship S_W; proposed review domain statistical_results; focus A/C.

**Printed values:** “392 participants (196 in each of the 4 possible intervention combinations)” were needed; 22% attrition and 250 per combination. Expected incidence was 20% versus 30%, with two-sided alpha .05 and power .90.

**Rule and calculation:** Four combinations of 196 require 784 participants, twice 392. Four cells are fixed by the factorial design. The printed 196 half-unit interval [195.5,196.5] gives a recomputed total interval [782,786]. The printed 392 interval [391.5,392.5] leaves a gap 389.5, relative discrepancy 389.5/392=.9936. A standard equal-size two-proportion **diagnostic** gives approximately 391.95 per comparison group, hence approximately 196 per factorial cell. This suggests a possible factor-level-versus-total reading but does not identify the authors' sample-size algorithm. The count conflict needs no assumed test.

**Qualifying route:** Route B. **Affected result or extracted value:** Total planned analyzable sample size and number needed per factorial cell for the primary MDD comparison. **Why context does not resolve it:** The paragraph prints 392 as a participant requirement and 196 for each of four combinations. A reader must choose whether 392 means total participants or each factor-level group. The attrition target supports one reading but does not reconcile the printed identity.

**Alternatives and missing definition:** 392 may mean participants in each marginal intervention/control level rather than total participants. The grouping meant by 392 is absent. **Human question:** What participant grouping does 392 refer to, and what total analyzable sample size corresponds to 196 in each of the four combinations?

### F-ST1-002

**Issue:** The expected intervention incidence used in the reported power assumptions differs from the supplied protocol.

**Locations and roles:** PLAN [protocol PDF pp.16–17, section 4.4](../../../joi190007supp1_prod.pdf#page=16); REPORT [main PDF p.4, Sample Size](../../../jama_bot_2019_oi_190007.pdf#page=4). S005/S202. Relationship P_R; proposed review domain protocol_report; focus D.

**Printed values:** Protocol: control 30%, intervention 15%, powered difference 25%, 180 per group, .90 power, 20% dropout, 250 per arm. Article: control 30%, active 20%, 33% relative reduction, the 392/196 sample-size counts, .90 power, 22% attrition, 250 per cell.

**Rule and calculation:** The primary one-year MDD power assumption has intervention incidence 15% in PLAN and 20% in REPORT. Half-unit intervals [14.5,15.5]% and [19.5,20.5]% leave 4 percentage points; relative discrepancy 4/20=.20. Corresponding expected risk differences are 15 versus 10 percentage points, and relative reductions are 50% versus approximately 33%. The protocol's separate “25%” target is not silently identified as either absolute or relative. The 20% versus 22% attrition difference alone falls within the workflow precision rule and is excluded. Standard two-proportion calculations of approximately 160.78 per group at 30%/15%, versus 391.95 at 30%/20%, are **diagnostics** only: the protocol explicitly discusses additive interaction without giving its full formula.

**Qualifying route:** Route B. **Affected result or extracted value:** Expected intervention MDD incidence and power/sample-size assumptions supporting the primary comparison. **Why context does not resolve it:** Both sources assign these expected incidences to the primary one-year MDD sample-size calculation. No supplied statement explains the revision from 15% to 20% or the protocol's 25% target.

**Alternatives and missing definition:** A prospective recalculation or amendment may have changed the effect target. The supplied final-amendment protocol and article do not document that mapping; no earlier protocol version is supplied. **Human question:** Which intervention incidence and contrast governed the actual power calculation, and what documented revision connects the supplied 15% and 20% assumptions?

### F-ST1-003

**Issue:** Outcome hierarchy differs among the protocol, SAP, and article.

**Locations and roles:** PLAN [protocol PDF p.28, sections 8.1.1–8.1.2](../../../joi190007supp1_prod.pdf#page=28); PLAN [SAP PDF p.2, Outcomes](../../../joi190007supp2_prod.pdf#page=2); REPORT [main PDF p.4, Outcomes](../../../jama_bot_2019_oi_190007.pdf#page=4). S203/S207/S007/S009. Primary relationship P_R; all relationships P_R, P_P; proposed review domain protocol_report; focus D.

**Printed statements:** The protocol lists both 12-month MDD incidence and IDS symptomatology under “Main study parameter/endpoint.” The SAP labels cumulative MDD “Primary,” PHQ and IDS “Secondary,” and GAD and quality of life “Other.” The article labels PHQ, IDS, GAD, and utility secondary trial outcomes and MDD alone primary.

**Rule and calculation:** The same IDS measure and time points move from a main endpoint in the protocol to secondary in the SAP/article. GAD and utility move from SAP “Other” to article secondary. This is a source-text hierarchy comparison; display precision does not apply. The occurrences are consolidated as one outcome-status pattern.

**Qualifying route:** Route A, category 5. **Affected result or extracted value:** Prespecified hierarchy and analysis status of IDS depression severity and GAD/utility results, including Table 3 effects. **Why context does not resolve it:** A changed prespecified outcome status is an always-register category. The governing hierarchy is not identified by a supplied amendment.

**Alternatives and missing definition:** The SAP may intentionally supersede the IDS main status. “Other” may be organizational wording rather than a formal hierarchy level for GAD/utility. These alternatives preserve the distinctions for human review. **Human question:** What prospective hierarchy governed IDS, GAD, and utility, and which supplied plan or amendment establishes it?

### F-ST1-004

**Issue:** Protocol analysis specifications differ from the SAP/report, with planned primary analyses not supplied as such.

**Locations and roles:** PLAN [protocol PDF p.43, sections 10.1–10.2](../../../joi190007supp1_prod.pdf#page=43); PLAN [SAP PDF p.3](../../../joi190007supp2_prod.pdf#page=3); REPORT [main PDF p.4, Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4), [Table 2 p.6](../../../jama_bot_2019_oi_190007.pdf#page=6), [Table 3 p.8](../../../jama_bot_2019_oi_190007.pdf#page=8). S204/S205/S208/S006/S007/S009/S036. Primary relationship P_R; all relationships P_R, P_P; proposed review domain protocol_report; focus D.

**Printed statements:** Protocol primary analyses specify Kaplan–Meier/log-rank/Cox, two-way and four-way comparisons, and additional mixed models using baseline/3/6/12-month assessments for MDD and IDS, addressing repeated participants and country clustering. Secondary analyses use mixed models allowing country clustering. The SAP specifies logistic cumulative MDD and mixed models or GEE for secondary outcomes. The report uses logistic primary MDD, post hoc Cox, overall GEE, and robust linear 12-month analyses, with site/history/baseline adjustment.

**Rule and calculation:** These are distinct printed specifications for the same endpoint and IDS trajectory. REPORT materials supply no protocol-designated primary KM/log-rank/four-way results or additional repeated-MDD mixed-model results. Table 2 supplies logistic/Cox main-effect and interaction ratios. Reported site adjustment is acknowledged; it is not declared incapable of accounting for country. The question concerns the governing model revision, including the expressly planned correlation structure. Display precision does not apply.

**Qualifying route:** Route A, category 5, for replacement or nonreporting of planned primary analyses. **Affected result or extracted value:** Which model and comparison defined primary MDD evidence, including Table 2 ORs/HRs and protocol-designated repeated MDD/IDS analysis. **Why context does not resolve it:** Planned primary analysis replacement/nonreporting is always registered. The SAP supports the reported logistic/GEE choices but does not document their relationship to the supplied protocol.

**Alternatives and missing definition:** A later prospective SAP or amendment may deliberately replace protocol choices. Site covariates may implement country adjustment. No preferred model is proposed. **Human question:** Which prospective specification governed MDD and IDS analysis, and where is replacement or nonreporting of the protocol-designated primary analyses documented?

### F-ST1-005

**Issue:** Analyses specified prospectively in the supplied SAP are called post hoc in the article.

**Locations and roles:** PLAN [SAP PDF pp.4–5, Secondary analysis/Effect modification](../../../joi190007supp2_prod.pdf#page=4); PLAN [protocol PDF pp.43–44](../../../joi190007supp1_prod.pdf#page=43); REPORT [main PDF p.4](../../../jama_bot_2019_oi_190007.pdf#page=4), [p.8, Effect Modification](../../../jama_bot_2019_oi_190007.pdf#page=8). S008/S011/S012/S013/S038/S204/S206/S213. Relationship P_R; proposed review domain protocol_report; focus D.

**Printed statements:** The SAP says a secondary analysis will study time to MDD using Cox and a secondary analysis will test history/center modification. The protocol specifies Cox and country interaction. The article calls time to first MDD/Cox post hoc and calls site/history/baseline symptom modification post hoc in its results. Only baseline severity is explicitly post hoc in article methods; that part is not registered as absent from prespecification.

**Rule and calculation:** Prospective PLAN text includes Cox and site/history analyses whose status is reported as post hoc. These are one repeated analysis-status pattern. No arithmetic or display-precision calculation applies.

**Qualifying route:** Route A, category 5. **Affected result or extracted value:** Prespecified versus post hoc status of primary-endpoint Cox HRs 1.05/.91/.91 and site/history modification, including the utility site interaction. **Why context does not resolve it:** Analysis status changes are always registered; the package does not establish timing and provenance sufficiently to choose the governing designation.

**Alternatives and missing definition:** The SAP may have been finalized after a particular decision, or the article may use post hoc to denote analyses additional to its primary model. The SAP date/timing and governing meaning of post hoc are not supplied. **Human question:** Were Cox and site/history modification analyses specified before outcome inspection, and how should their post hoc designation reconcile with the supplied SAP?

### F-ST1-006

**Issue:** The planned primary-endpoint additive-interaction sensitivity analysis is not reported.

**Locations and roles:** PLAN [SAP PDF p.4, Interaction of intervention strategies](../../../joi190007supp2_prod.pdf#page=4); REPORT [main PDF pp.4,6–7](../../../jama_bot_2019_oi_190007.pdf#page=6), [results supplement PDF pp.18–22](../../../joi190007supp3_prod.pdf#page=18). S212/S003/S013/S020. Relationship P_R; proposed review domain protocol_report; focus D.

**Printed statements:** The SAP specifies both multiplicative logistic A×B interaction and additive sensitivity using RERI, a linear OR model, likelihood-based 95% CI, and preventive-condition recoding using the lowest-risk joint reference. The article/supplement report multiplicative OR/HR interaction and secondary-score moderation/sensitivity/CACE, but no RERI, additive CI, or additive null test.

**Rule and calculation:** Multiplicative interaction OR .93 (.76,1.14), P .48 does not report the planned additive RERI estimand. One scale's nonsignificance does not state another scale's result. Complete REPORT maps contain no RERI/additive primary analysis. No RERI is inferred from crude data, and display precision does not apply to the absent specified analysis.

**Qualifying route:** Route A, category 5. **Affected result or extracted value:** Planned additive interaction between supplements and therapy on primary MDD. **Why context does not resolve it:** A planned primary analysis not reported is always registered; no supplied report identifies the additive result or withdrawal of that plan.

**Alternatives and missing definition:** Results may exist outside the package, or the analysis may have been replaced by amendment. External material was not consulted. **Human question:** Was the primary RERI sensitivity analysis conducted, and where are its result or prospectively documented replacement reported?

### F-ST1-007

**Issue:** The CACE explanation does not identify how its stated ratio to the original effect yields the primary MDD estimates.

**Locations and roles:** REPORT [results supplement PDF p.15, eAppendix 7](../../../joi190007supp3_prod.pdf#page=15), [p.16, therapy adherence](../../../joi190007supp3_prod.pdf#page=16), [p.22, eAppendix 12](../../../joi190007supp3_prod.pdf#page=22); REPORT [main PDF p.6, Table 2](../../../jama_bot_2019_oi_190007.pdf#page=6), [p.8, CACE](../../../jama_bot_2019_oi_190007.pdf#page=8). S001/S002/S037/S211/S215/S216/S234/S235. Primary relationship S_C; all relationships S_C, S_W; proposed review domain statistical_results; focus C/B.

**Printed values/statements:** eAppendix 7 describes the CACE estimate as the ratio of the original intervention effect estimate to the treatment-arm proportion of compliers. Main ITT ORs are supplement 1.06 (.87,1.29) and therapy .93 (.76,1.13). CACE ORs are supplement .84 (.67,1.07) and therapy .78 (.64,.95). Therapy compliance is 71.9% and 70.7% in the two equal 256-person therapy cells, N=512. The CACE table identifies logistic MDD analysis, MI, site/history adjustment, and −1/+1 effect coding.

**Rule and calculation:** Under the literal documented ratio mapping, a proportion 0<c≤1 cannot reverse a positive original effect. On the log-OR scale, log(1.06)/c>0 implies OR>1; on the OR scale, 1.06/c≥1.06. Original OR rounding interval [1.055,1.065] and CACE [.835,.845] remain separated under either mapping; gap at least .210, relative discrepancy .210/.84=.25. For therapy, observed mean compliance interval [.7125,.7135] and original OR [.925,.935] give a **log-OR ratio diagnostic** exp(log OR/c)∈[.89635,.91010]. Printed CACE [.775,.785] leaves gap .11135, relative discrepancy .11135/.78=.1428. This diagnostic checks the supplied explanation; it is not an assumed SEM implementation or a comparison between a model estimate and a crude effect.

**Qualifying route:** Route B. **Affected result or extracted value:** Supplement CACE MDD OR .84 and adherence-based significant therapy OR .78. **Why context does not resolve it:** The only supplied mapping to an original effect does not identify the original effect, scale, or model producing the ORs. Both tables have the same endpoint and stated coding, yet supplementation direction reverses under the documented mapping.

**Alternatives and missing definition:** The ratio may be only a linear-effect illustration; the logistic latent/SEM model may use a different original effect or conditional population. Such a model could produce the table, but its numerator, scale, compliance probability, and connection to the published ITT model are not identified. **Human question:** Which original effect, scale, compliance proportion, and CACE/SEM model yield these MDD ORs, and how does that mapping relate to eAppendix 7's ratio and Table 2's ITT values?

### F-ST1-008

**Issue:** Three site rows do not reproduce the centered coefficient/CI relationship followed by other rows of the same moderation table.

**Locations and roles:** REPORT [results supplement PDF p.19, Table B, Spain/United Kingdom/Germany](../../../joi190007supp3_prod.pdf#page=19), compared with its remaining coefficient rows. S218. Relationship S_W; proposed review domain statistical_results; focus B.

**Printed tuples:** Spain B .107, 95% CI −.424 to .520, P .694; UK B .117, CI −.371 to .638, P .637; Germany B .058, CI −.401 to .606, P .804. A fresh current-source CPU rendering confirms all values and nine nonreference rows.

**Rule and reproducing-method calculation:** The centered relationship B=(L+U)/2 reproduces all six other rows within half-unit input/output intervals: supplements −.107, therapy −.054, history −.3175, baseline GAD .4645, therapy×baseline −.016, and supplement×baseline .062. It does not reproduce the three site coefficients. Both CI endpoints are printed to .001 in each affected row.

| Site | Printed B interval | Recomputed midpoint interval | Gap | Relative discrepancy using printed B |
|---|---|---|---:|---:|
| Spain | [.1065,.1075] | [.0475,.0485] | .0580 | .5421 |
| United Kingdom | [.1165,.1175] | [.1330,.1340] | .0155 | .1325 |
| Germany | [.0575,.0585] | [.1020,.1030] | .0435 | .7500 |

For completeness, the upper endpoint implied by 2B−L is .638, .605, and .517 respectively. Recomputed rounding intervals [.6365,.6395], [.6035,.6065], [.5155,.5185] compare with printed [.5195,.5205], [.6375,.6385], [.6055,.6065]. Relative upper-limit gaps are .2231, .0486, and .1436. The UK upper-limit comparison alone falls within the .05 rule; its registered observation concerns the coefficient-versus-midpoint gap .1325, not that upper-limit comparison. The tuple does not identify which member uses another method or value.

**Qualifying route:** Route A, category 4. **Affected result or extracted value:** Spain, UK, and Germany coefficient/95% CI pairs in the overall GAD moderation model. **Why context does not resolve it:** The same-display reproducing-method category always registers. This method works for all other rows, while these printed tuples do not follow it.

**Alternatives and missing definition:** A specifically asymmetric construction may apply to site rows, or coefficients and CIs may come from different models. No such distinction is stated. This does not claim all valid CIs must be symmetric. All point estimates remain within ordered CIs, and all significance decisions are nonsignificant. These three occurrences form one pattern. **Human question:** What coefficient/CI construction was used for each site row, and why do these tuples not follow the centered construction reproduced by the remaining rows?

### F-ST1-009

**Issue:** Planned standardized 12-month effect uncertainty is not supplied with the standardized point values.

**Locations and roles:** PLAN [SAP PDF p.3, Fourth analysis](../../../joi190007supp2_prod.pdf#page=3); PLAN [protocol PDF p.28, IDS main endpoint](../../../joi190007supp1_prod.pdf#page=28); REPORT [main PDF p.8, Table 3, Cohen D/footnote e](../../../jama_bot_2019_oi_190007.pdf#page=8). S208/S022/S024/S026/S028/S036. Relationship P_R; proposed review domain protocol_report; focus D.

**Printed statements/values:** The SAP promises standardized mean differences with 95% CI and P values for T12 continuous outcomes. Table 3 gives PHQ D .10/−.02 and IDS D .05/.006 as point values alone. CI/P columns apply to unstandardized regression coefficients. Footnote e defines D using baseline/12-month means and pooled SD, a separate calculation.

**Rule and calculation:** Uncertainty for an adjusted unstandardized coefficient does not by itself identify uncertainty for a separately calculated standardized change contrast. No other supplied REPORT gives standardized CIs. No pooled SD/covariance is assumed. Precision does not apply to absent explicitly planned uncertainty.

**Qualifying route:** Route B. **Affected result or extracted value:** Standardized 12-month PHQ/IDS contrasts and uncertainty for evidence reuse, especially the protocol's IDS main endpoint. **Why context does not resolve it:** The SAP promises standardized CI/P; the table's available CI/P attach to another estimand and cannot be identified as those values without the missing mapping.

**Alternatives and missing definition:** D may intentionally be descriptive, with unstandardized tests providing inference, under an amended display plan. No supplied amendment identifies that revision. **Human question:** Where are the planned standardized PHQ/IDS 95% CIs and P values, or which prospective revision explains supplying only Cohen D points?

### F-ST1-010

**Issue:** Planned missing-data sensitivity is not supplied for primary MDD estimates.

**Locations and roles:** PLAN [SAP PDF p.5, Missing data and drop-out](../../../joi190007supp2_prod.pdf#page=5); REPORT [main PDF p.4, Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4), [p.8, Sensitivity](../../../jama_bot_2019_oi_190007.pdf#page=8); REPORT [results supplement PDF p.21, eAppendix 11](../../../joi190007supp3_prod.pdf#page=21). S214/S006/S010/S039/S001/S002/S003. Relationship P_R; proposed review domain protocol_report; focus D.

**Printed statements:** After specifying 100 MI datasets for the primary outcome under MAR/Rubin pooling, the SAP says sensitivity analyses will be conducted and reported because missing-mechanism assumptions cannot be validated. Main methods/results describe GEE without MI for secondary depression/anxiety/utility. The supplement sensitivity table contains PHQ/IDS/GAD/utility, not MDD. Primary Table 2 and CACE use MI.

**Rule and calculation:** Supplied REPORT materials contain no primary MDD missing-mechanism sensitivity estimate alongside the MAR-imputed ORs. Secondary GEE without MI and MI-CACE do not state that primary result. No preferred alternative is proposed. Precision does not apply to the absent planned analysis.

**Qualifying route:** Route A, category 5. **Affected result or extracted value:** Robustness of primary MDD ORs 1.06/.93/.93 under the planned missingness assessment. **Why context does not resolve it:** The primary MI/MAR paragraph promises reported missing-mechanism sensitivity, but the report identifies only secondary-outcome sensitivity. This planned-primary-analysis observation requires human review.

**Alternatives and missing definition:** The SAP's general sensitivity sentence may have been intended to be satisfied only by secondary GEE, rather than a primary MDD alternative; it does not name the exact primary sensitivity. Results may exist outside the supplied package. **Human question:** Which primary MDD analysis fulfilled the reported missing-data-sensitivity commitment, or was that commitment formally limited to secondary outcomes?

### F-ST1-011

**Issue:** The detailed protocol primary endpoint uses a diagnostic edition different from the article and other protocol locations.

**Locations and roles:** PLAN [protocol PDF p.28, section 8.1.1](../../../joi190007supp1_prod.pdf#page=28); PLAN [protocol PDF p.8, main parameter](../../../joi190007supp1_prod.pdf#page=8), [pp.33–34, MINI assessment definitions](../../../joi190007supp1_prod.pdf#page=33); REPORT [main PDF p.4, Primary Outcome](../../../jama_bot_2019_oi_190007.pdf#page=4). S203/S007. Primary relationship P_R; all relationships P_R, P_P; proposed review domain protocol_report; focus D.

**Printed statements:** Protocol p.28 defines MDD using DSM-5 criteria and MINI V5.01. Its p.8 summary and pp.33–34 assessment table specify DSM-IV criteria using MINI. The report specifies Fourth Edition criteria and MINI 5.0.

**Rule and calculation:** Different editions are explicitly named as the case-definition authority for the same primary cumulative endpoint. The package alone does not identify them as the same definition; external instrument history is not used. This concerns diagnostic criteria, not version punctuation. Numeric precision does not apply.

**Qualifying route:** Route B. **Affected result or extracted value:** Diagnostic case-definition metadata for the 105 MDD onsets and primary ORs. **Why context does not resolve it:** The detailed endpoint text and report name different criteria, without a supplied mapping or amendment showing which governed cases.

**Alternatives and missing definition:** DSM-5 may be only a wording slip, given MINI and DSM-IV elsewhere, or administration may have used modified criteria. No changed patient classification is claimed. **Human question:** Which DSM criteria were specified and used for primary MDD cases, and how should protocol p.28's DSM-5 definition reconcile with its DSM-IV assessment table and the article?

## Excluded observations

Only apparent issues self-screened without findings appear here. Reconciled checks remain in the S records. Each row has one reason code; none is an unregistered route-A finding.

| Location | Observation | Reason code |
|---|---|---|
| REPORT results supplement PDF p.19, baseline GAD | P=0 denotes a displayed very small P value; the positive CI and significance reading agree, with no independent conflict | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT results supplement PDF p.21, T12 B(SE), particularly PHQ FBA −.22/.11 P .052 and IDS supplement .28/.28 P .30 | Point-number normal diagnostics give approximately .046/.317, but all printed P values are attainable within half-unit input/output intervals; no exact robust test is assumed | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT results supplement PDF p.20, C1/C2 supplement B .000, P .952/.944/.935 | Rounded zero coefficients permit small nonzero actual estimates; CIs contain the null | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main PDF p.8, Table 3 versus mean-difference narrative | Small nonexact doubling of PHQ/IDS endpoints and coefficients reconciles within half-unit intervals; the table explicitly instructs multiplying by 2 | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main PDF pp.6–7, Table 2 versus crude event odds | Adjusted, effect-coded factorial OR/HR values are not defined as crude treated/control ratios | MODEL_VERSUS_CRUDE |
| REPORT main PDF p.8, IDS therapy T12 B −.28 versus D +.006 | Adjusted robust-regression B and mean/pooled-SD change D have different explicit definitions; raw-change D is not an adjusted coefficient | MODEL_VERSUS_CRUDE |
| PLAN SAP PDF p.5, outliers/distributions versus REPORT | Outlier-with/without and transformations are conditional on relevant observations; supplied evidence does not establish those conditions occurred | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol PDF pp.43–44 and SAP p.3 versus REPORT supplement | Missing ancillary mediation, biomarker/adherence trajectories and non-key outcomes do not identify a primary/key-secondary result conflict; SAP explicitly defers other moderators to a separate paper | PERIPHERAL_COMPARISON |
| PLAN protocol PDF p.16, 20% dropout versus REPORT main PDF p.4, 22% attrition | [19.5,20.5]% versus [21.5,22.5]% leaves 1 point; relative gap 1/20=.05 or 1/22=.04545, within the precision rule | ROUNDING_OR_DISPLAY_PRECISION |

## Limits and source authority

The package lacks raw data, model code, MI covariances/degrees of freedom, exact robust test definitions, fitted CACE compliance probabilities, and precise graph coordinates. These limits did not omit any S record or source-mapped inference. No exact P reconstruction is claimed without the necessary definition. Current source-linked maps, new selected direct extracts, and a fresh p.19 rendering under preprocessing/statistics_pass_1 were used: Poppler 26.01.0, CPU. No OCR, GPU, web, other paper, legacy candidate conclusion, or Python review orchestrator was used. Findings are prepared for independent screening and human adjudication; no C IDs are assigned here.
