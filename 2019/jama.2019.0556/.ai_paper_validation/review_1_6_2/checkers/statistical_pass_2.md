# Statistical pass 2 — complete relationship follow-through

Runtime agent ID: 01a1296e-431b-7372-92ce-7add831babfb. Fresh qc162_statistical_consistency_reviewer, gpt-6.1-sol/high, FRESH_SPAWN. The pass-1 runtime was 01a12955-bf9a-7752-8bc3-60a9eb6b0913. QUALITY_CONTROL_SCOPE.md and the complete 1.6.2 review contract were read. Inputs were the complete current 82-record S inventory, ledger C001 through C011, 22 initial screening decisions, all eleven mechanical rechecks, and all 27 original checker Excluded observations rows. No legacy scientific decisions, external literature, or raw-data audit were used.

**Scope and result:** All 82 relationships and their constituent contrasts received PASS_2_COMPLETE. New distinct findings: 0. The 27 original exclusion rows were reread and consolidated into 20 apparent-observation records below. One original exclusion is already represented by included C003 and is recorded as DUPLICATE_OF_INCLUDED; no route-A issue is newly suppressed. No second inclusion screener is needed for this pass because it emits no new finding. Every assigned candidate remains Pending Human Adjudication.

## Source authority and inferential boundaries

REPORT means main article DOC-001, results supplement DOC-004 and administrative sharing DOC-005; PLAN means protocol DOC-002 and SAP DOC-003. Exact current-source page images, not previous classifications, establish readings. I visually inspected 31 existing CPU Poppler 26.01.0 images: initial_screen/main-p1,p2,p3,p4,p6,p7,p8; protocol-p16,p17,p20,p23,p28,p33,p34,p43,p44; sap-p2,p3,p4,p5; support-p3,p4,p15,p16,p18,p19,p20,p21,p22; and evidence_recheck/main-p9,support-p14. No new rendering/OCR was needed. Full current-source REPORT layout files were searched for the named absent analyses and all relevant result/method occurrences reread. The mapped exact source locations remain in statistics/relationship_inventory.md; references to those locations below do not substitute a legacy conclusion for source evidence.

Nulls are 1 for OR/HR and 0 for coefficients/differences. The printed confidence level is 95%, with two-sided significance .05. Containment, endpoint order, direction and null/test agreement were revisited for all six primary/Cox ratios, sixteen Table 3 contrasts, 39 moderation tuples, 24 no-MI estimates and eight CACE estimates. S035 includes two contrasts. Moderation reference rows are distinguished from coefficient rows. No noninferiority, equivalence, formal interim or stopping rule is supplied. No multiplicity-adjusted threshold is supplied; the paper's explicit exploratory caution is retained. Exact test, sidedness beyond the supplied two-sided rule, covariance, pooled degrees of freedom and fitted CACE equations are not inferred from convention.

The −1/+1 coding and Table 3's explicit instruction to double coefficients and limits identify its adjusted differences. Table 2's printed OR/HR scale is preserved. Available-data event ratios or descriptive mean differences are not substitutes for adjusted factorial or MI estimates. The repeated-measures GEE exchangeable structure is stated; the Table 3/no-MI T12 robust-linear distinction is stated in their footnotes. Missing model inputs alone do not create a finding. Normal calculations below are diagnostics, never reconstructions of an unspecified robust or Rubin-pooled test.

## Candidate and initial-screen follow-through

| Candidate or screened finding | Source-grounded pass-2 implication |
|---|---|
| C001 | Main pp1–2 and supplement p4 identify daily EPA+DHA 1412 mg; protocol p23 identifies 1.0 g and p20 permits 90–125%. The conservative rounded 1050×1.255 upper bound remains below 1411.5 by 93.75 mg, relative .066395. Dose identity, exposure extraction and the final-formulation alternative remain as registered; concordant REPORT copies do not add S_C. |
| C002 | Protocol p43 specifies primary KM/log-rank/Cox, four-way and repeated-MDD/IDS mixed models; SAP pp2–4 specifies logistic cumulative MDD, secondary IDS and permitted GEE, and secondary Cox. Main pp4/6/8 supplies logistic/GEE/robust-linear inference. The supplied primary suite discrepancy remains; country/site equivalence and a prospectively governing SAP revision remain alternatives. No preferred method or failed country adjustment is inferred. |
| C003 | Exact main p3 prints BMI <15 for 1451 online exclusions, while supplement p3 explicitly assigns 25–40 to online eligibility. Gap 9/25=.36; coherent flow sums do not resolve the numeric cutoff. The numeric checker's first excluded row is already represented here, rather than newly screened OUT_OF_FOCUS. Protocol eligibility corroborates without adding P_R. |
| C004 | Main p4's four 196-participant cells imply [782,786] against printed [391.5,392.5], relative gap .993622. Attrition inflation is separately precision-compatible. A pooled-factor-level interpretation remains the counting-unit question, not a numerical replacement. |
| C005 | Protocol pp16–17's active risk 15% and 180/group remain distinct from main p4's 20% and 196 beyond precision. The 20% versus22% dropout comparison alone is within .05. Additive versus main-effect power contrasts and unspecified 25% basis remain alternatives, so diagnostic independent-proportion formulas cannot identify the actual factorial algorithm. |
| C006 | Protocol pp28/43 explicitly puts IDS in main/primary parameters; SAP p2 and main pp4/8 put it in secondary outcomes. SAP Other for GAD/utility may be organizational; it does not remove the IDS status comparison. Secondary exploratory caution does not independently change its prespecified rank. |
| C007 | Protocol pp43–44 and SAP pp4–5 prospectively specify Cox/site/history analyses; main pp4/6/8 calls Cox and collectively the modifiers post hoc. Main Methods separately reserves that latter label for baseline severity. All occurrences remain one status pattern. Undated SAP chronology and collective-label scope remain alternatives; baseline-severity analyses are not alleged to be planned. |
| C008 | SAP p4 expressly commits to primary additive RERI/likelihood CI with recoding. Main pp4/6/7 and supplement pp18–22 supply multiplicative inference, secondary-score sensitivity and CACE, with no matching RERI result. A nonsignificant multiplicative interaction does not supply the additive estimand. |
| C009 | SAP p5's primary 100-MI/MAR paragraph promises missing-mechanism sensitivity. Main pp4/8 and supplement p21 show continuous-secondary no-MI sensitivity; p22 CACE retains MI. Primary missing-rate comparisons and MI-CACE do not identify primary missing-mechanism sensitivity. The generic sentence's scope remains the precise human clarification. |
| C010 | Supplement pp14–15 acknowledges latent compliance and SEM but describes original-effect/complier-proportion scaling; main p6 OR1.06 cannot yield supplement p22 OR.84 through literal OR or positive log-OR division by 0<c≤1. Minimum rounded gap .210/.84=.25. Therapy log-OR/compliance diagnostic gives [.896354,.910104] versus [.775,.785], relative gap .142762. A separate nonlinear fit or numerator could yield the reported values, so the issue remains the unidentified model/scale mapping, not an assertion that every CACE model is impossible. |
| C011 | Exact supplement p19 has Spain .107(−.424,.520), UK .117(−.371,.638), Germany .058(−.401,.606). Rounded coefficient/midpoint gaps .542056/.132479/.75 remain; all six other nonreference rows reproduce centered limits allowing .17/.52 endpoint precision. All three estimates are contained and nonsignificant consistently with P. Possible asymmetric/different-fit limits remain the construction question; the always-register category-4 comparison remains one three-site pattern. |
| F-XS-009 screened OUT_OF_FOCUS | Protocol p16 versus supplement p3 psychiatric/recruitment details do not print a changed primary endpoint, model, analysis-population size or decision rule. This is distinct from the numeric same-stage cutoff in C003; no newly reproduced route-A observation follows. |
| F-ST1-009 screened CONDITIONAL_OR_UNREPORTED | SAP p3 requests standardized CI/P; main p8 supplies standardized points with clearly unstandardized CI/P. The displayed analysis exists, and no contradictory standardized numerical value is supplied. Partial uncertainty display absence is distinct from an unreported complete primary/key-secondary analysis. |
| F-ST1-011 screened TERMINOLOGY_OR_WORDING | Protocol p28 DSM-5 wording coexists with MINI V5 and protocol pp33–34 DSM-IV operational assessments; main p4 uses the same instrument/DSM-IV. No alternate operational case definition or changed event count is supplied. A field reader can identify the operational instrument; this is not a printed estimate/count slip. |

## Every-S-ID pass-2 follow-through

Each row below follows the exact source/constituent scope in the canonical inventory. The canonical inventory contains the same follow-through and retains PASS_1_COMPLETE. Checks that reconcile are recorded here, not counted as excluded observations.

| S ID | Pass-2 source-grounded follow-through |
|---|---|
| S001 | Main pp1/6/7 OR1.06(.87,1.29),P.57 contains1 and repeats consistently; 54/512 versus51/513 is adjusted/effect-coded context; original-to-CACE mapping remains C010. |
| S002 | Main pp1/6/7 OR.93(.76,1.13),P.47 contains1 with consistent nonsignificance; 48/512 versus57/513 is not its crude estimator; C010 retains mapping question. |
| S003 | Main abstract explicitly calls combination interaction; OR.93(.76,1.14),P.48 contains1 and agrees across pp1/6/7. Planned additive counterpart remains C008. |
| S004 | Main p2 individual four-arm blocks8–12/site-history strata match 257/256/256/256 allocations and modeled adjustment; no clustered randomization or changed analysis unit is inferred. |
| S005 | Main p4 count identity remains C004; 196 attrition inflation to250 overlaps at printed precision; planned active-rate/group-size changes remain C005, with actual factorial algorithm unspecified. |
| S006 | Main p4 ITT all1025, joint factors/interaction, site/history, MAR100MI/Rubin are explicit and coherent. Plan-suite/CACE/missingness implications remain C002/C010/C009; raw covariance is unavailable. |
| S007 | Main p4 cumulative binary MDD at3/6/12 agrees with SAPp2 any-positive definition. Protocol primary model suite remains C002; DSM edition wording stays screened F-ST1-011. |
| S008 | Main p4 Cox first-onset/last-available schedule and Schoenfeld P>.05 have no supplied numeric contradiction; C007 retains planned/post-hoc status. No residual test statistic is invented. |
| S009 | Main p4 repeated3/6/12 GEE explicitly addresses within-participant dependence and baseline adjustment; SAPp3 permits GEE. Protocol distinction is C002; exploratory caution is explicit. |
| S010 | Main pp4/6 identifies no-MI continuous sensitivity, mean/SD-based D, MI-CACE/STATA, R/geepack/mice and two-sided.05. C009/C010 remain; standardized uncertainty has existing screened finding. |
| S011 | Main pp6/7 HR1.05(.86,1.27),P.65 contains1, with nonsignificance and event direction consistent. Planned/post-hoc status remains C007. |
| S012 | Main pp6/7 HR.91(.75,1.10),P.32 contains1; therapy nonsignificance is consistent. C007 covers status, not an invented event-ratio identity. |
| S013 | Main pp6/7 interaction HR.91(.75,1.11),P.36 contains1. C008 is the separately absent planned additive result; this multiplicative HR is not its substitute. |
| S014 | Main p6 explicit effect-coding footnote resolves model scale alongside placebo/no-therapy reference labels; interaction NA counts are not missing denominators to manufacture. |
| S015 | Main pp3/6 arm missing counts47/54/41/52 sum194; four-arm total1025 and printedP.47 align with Pearson diagnostic. Exact test is unreported, so no exact algorithm is claimed. |
| S016 | Main pp3/6 missing63/71/59/61 sum254 and align with printedP.62 by four-arm diagnostic; no primary analysis-population change follows from MI. |
| S017 | Main pp3/6 missing65/62/58/61 sum246 and align with printedP.91. Table2's239 excludes earlier-MDD cases by its explicit definition; these are distinct counts. |
| S018 | Main pp6/7 secondary missing counts agree with plotted contributor totals; no arm-specific secondary missingness P is supplied, so that assertion cannot be exactly reconstructed and supplies no printed conflict. |
| S019 | Main p6 footnote states MI/site/history/joint-factor/effect-coding matchingp4. No supplied variance/test statistic supports stronger exact P reconstruction; C002 governs plan specification. |
| S020 | Main p7 interaction range.41–.98 is explicitly nonsignificant and p8 omits interaction accordingly. Supplementp21 no-MI interactions are a different fit; their P values are not matched copies. |
| S021 | Main p8 PHQ overall .33(.12,.53),P.002 excludes0; doubling intervals overlaps narrative .65(.25,1.06). Positive symptom direction agrees. |
| S022 | Main p8 PHQ T12 .28(.05,.50),P.02 excludes0; doubled estimate/limits overlap .56(.11,1.01). D.10 has a separately stated mean/SD basis. |
| S023 | Main p8 PHQ therapy overall−.13(−.33,.07),P.19 contains0; no significant therapy effect is claimed. |
| S024 | Main p8 PHQ therapyT12−.17(−.39,.06),P.14 contains0. D−.02 is not a conflicting adjusted coefficient; no-MI−.22 is a different fit. |
| S025 | Main p8 IDS overall .60(.15,1.05),P.01 excludes0; narrative1.20(.29,2.10) overlaps doubled input intervals. IDS hierarchy remains C006. |
| S026 | Main p8 IDS T12 .36(−.19,.90),P.20 contains0; D.05 is separately defined. No positive significance is claimed. |
| S027 | Main p8 IDS therapy overall−.23(−.67,.22),P.32 contains0 and agrees with narrative nonsignificance. |
| S028 | Main p8 IDS therapyT12−.28(−.83,.27),P.31 contains0; D+.006 is mean/SD-change-based, so its sign is not a matched adjusted-estimand conflict. |
| S029 | Main p8 GAD overall .25(.08,.42),P.004 excludes0; doubled .50(.16,.84) matches narrative higher anxiety. |
| S030 | Main p8 GAD T12 .14(−.04,.33),P.13 contains0. No-MI/CACE estimates are distinct analyses, not conflicting copies. |
| S031 | Main p8 GAD therapy overall−.16(−.32,.01),P.06 includes0 with nonsignificance; no interval/test conflict is rounded away. |
| S032 | Main p8 GAD therapyT12−.24(−.42,−.06),P.01 excludes0; doubled−.48(−.84,−.12) and lower-anxiety narrative match exactly. |
| S033 | Main p8 utilityoverall−.006(−.012,.000),P.052 includes printed0; nonsignificance agrees. No hidden endpoint sign is inferred. |
| S034 | Main p8 utilityT12−.002(−.008,.005),P.61 includes0; direction/nonsignificance agree, with separately definedD−.07. |
| S035 | Both mainp8 therapyutility contrasts checked: overall.002(−.003,.008),P.44 andT12.004(−.002,.009),P.23 contain0 and agree with no claimed significant utility main effect. |
| S036 | Mainp8 footnotes identify joint main effects/no interaction, overallGEE versusT12robustlinear, MI, adjustment, ×2 and mean/SDD. SAPGEE allowance does not resolve protocol distinctionC002; partial standardized uncertainty remains screened. |
| S037 | Mainp8 therapyCACE OR.78(.64,.95) excludes1 and supports its significant adherence-accounted narrative. Supplementp22 matches; mapping question remainsC010. |
| S038 | Mainpp4/8 moderation directions match supplementpp18–20: negativeFBA×PHQ, positive supplement×GAD, positiveFBA×UK. Main/history coefficient significance is not a history-interaction test; status remainsC007. |
| S039 | Mainp8 sensitivity statement identifies a different no-MI fit; all its supplementp21 contrasts checked. ConcealmentP<.001 direction agrees withp23 counts; primarymissingness promise remainsC009. |
| S040 | Mainp9 no statistically significantMDD benefit agrees with all primary/Cox null-containing intervals; T12GAD/CACE therapy claims agree with significant intervals. Lower incidence has no numerical attained-power claim to reconstruct. |
| S201 | Protocol pp 15/29 specifies individual factorial randomization, four cells of 250 (total 1000), and center/history strata matching the main design. Achieved enrollment 1025 is distinct from the target 1000. |
| S202 | Protocol pp 16/17 retains additive/synergistic power contrasts and an undefined 25% basis; the main risk/group inputs remain C005. No two-arm algorithm is imposed. The 20%/22% attrition comparison alone is within precision. |
| S203 | Protocol pp 28/33/34 supports MDD at 0/3/6/12 and the separate 24-month extension. IDS primary status remains C006; the same MINI operational DSM-IV assessment resolves the edition wording. |
| S204 | Protocol p 43 primary KM/log-rank/Cox/four-way/mixed suite versus SAP/main remains C002. ITT 1025 matches. Supplement p 15 distinguishes CACE from conventional per-protocol selection; no CACE subgroup is equated to an ITT denominator. |
| S205 | Protocol p 43 secondary mixed models and the reported GEE/robust fit remain part of C002; SAP permits GEE. Protocol p 42 supplies no DSMB/formal interim decision requiring a stopping-rule test. |
| S206 | Protocol pp 43/44 ancillary mediation/biomarker and broader modifiers concern non-key analyses; SAP p 4 defers other modifiers. Planned country/site analysis status remains C007. |
| S207 | SAP p 2 any-positive-at 3/6/12 MDD definition matches the main cumulative endpoint; history/center covariates match. IDS hierarchy remains C006, with the Other-heading ambiguity retained. |
| S208 | SAP p 3 logistic OR/CI/P and effect coding match main p 6; its mixed/GEE allowance matches overall inference. Protocol suite C002 remains. Standardized points are present despite the screened uncertainty-display omission. |
| S209 | SAP p 3 biomarker/diet longitudinal adherence models versus supplemental descriptive changes concern ancillary/non-key analyses; these are not missing primary/key-secondary results. |
| S210 | SAP p 3 two-sided p 0.05 notation is evident. Main R and task-specific STATA are identified; no numeric significance-threshold or software contradiction is supplied. |
| S211 | SAP p 4 weighted-jar/self-report≥70% and therapy≥8/21 definitions match the report. Full-sample CACE differs from crude complier selection; C010 asks the actual mapping without inferring fitted compliance probabilities. |
| S212 | SAP p 4 primary RERI/likelihood-CI sensitivity remains absent in the complete REPORT set. C008 retains recoding/scale questions; a multiplicative interaction does not supply that result. |
| S213 | SAP pp 4/5 expressly specifies secondary Cox/history-center analyses; reported post hoc status remains C007. Supplement p 18 reports no history moderation; no missing individual statistic is invented as a contradiction. |
| S214 | SAP p 5 100-MI/MAR/Rubin specification matches the main analysis. Planned primary-context missingness sensitivity remains C009. Outlier/transformation commitments are conditional, with no supplied triggering observation. |
| S215 | Supplement pp 8/9/12/p 16 distinguishes≥8 of 21 total sessions from maintenance-group attendance; pill≥70% matches SAP. Main more-than 70% wording has no supplied numeric boundary-participant conflict. |
| S216 | Supplement pp 14/15 latent classes/IV/SEM and ratio explanation were considered jointly. A separate nonlinear fit is plausible, but the original-effect/scale mapping remains C010 against the named MDD ORs. |
| S217 | All 9 nonreference PHQ tuples on supplement p 18 were reread: containment/order/null/P agree. History−.536 is a covariate main effect; negative FBA×PHQ−.064 supports moderation direction. No additional coefficient is invented. |
| S218 | All 9 tuples on supplement p 19 were reread: containment/order/null/P agree; baseline P 0 is display zero. All 3 site-construction gaps remain C011 against 6 controls; positive supplements×GAD.062 supports higher anxiety. |
| S219 | All 13 nonreference C 1 tuples and 3 reference labels on supplement p 20 were checked. Only baseline utility and FBA×UK exclude 0, with P<.001/.041. Positive UK interaction supports the narrative; no global site P is inferred. |
| S220 | All 4 UK C 2 tuples on supplement p 20 were checked: supplement/history nonsignificant; FBA.013(.001,.024),P.033 and baseline.738(.620,.856),P<.001 significant. The subgroup fit is distinct from the interaction fit. |
| S221 | All 4 Netherlands C 2 tuples on supplement p 20 were checked: supplement/FBA/history contain 0 with nonsignificant P; baseline.509(.400,.619),P<.001 excludes 0. No between-subgroup test is constructed without covariance. |
| S222 | Supplement p 21 PHQ supplement overall.30(.11,.49),P.002 excludes 0; T 12.28(SE.11),P.013 fits the rounded normal diagnostic.00664–.01679. The no-MI fit is explicitly distinct. |
| S223 | Supplement p 21 PHQ therapy overall−.14(−.34,.05),P.14 contains 0; T 12−.22(.11),P.052 fits rounded normal.03212–.06154. Point-number.046 is not an independently reproduced test conflict. |
| S224 | Supplement p 21 PHQ interaction overall−.01(−.20,.18),P.94 contains 0; T 12.02(.11),P.84 fits rounded normal.81181–.89622. |
| S225 | Supplement p 21 IDS supplement overall.55(.11,.99),P.01 excludes 0; T 12.28(.28),P.30 overlaps rounded normal.30003–.33459 through printed P interval.295–.305. |
| S226 | Supplement p 21 IDS therapy overall−.26(−.70,.18),P.25 contains 0; T 12−.36(.28),P.20 fits rounded normal.18442–.21291. |
| S227 | Supplement p 21 IDS interaction overall−.01(−.45,.43),P.96 contains 0; T 12.12(.28),P.66 fits rounded normal.64944–.68657. |
| S228 | Supplement p 21 GAD supplement overall.24(.08,.40),P.004 excludes 0; T 12.17(.09),P.07 fits rounded normal.03951–.08241. No-MI estimates are not copies of MI Table 3. |
| S229 | Supplement p 21 GAD therapy overall−.16(−.32,.00),P.06 includes 0; T 12−.26(.09),P.005 fits rounded normal.00182–.00727. Different time/model results do not establish an interval/test conflict. |
| S230 | Supplement p 21 GAD interaction overall.04(−.13,.20),P.66 contains 0; T 12.03(.09),P.74 fits rounded normal.68051–.79243. |
| S231 | Supplement p 21 utility supplement overall−.006(−.011,.000),P.055 includes 0; T 12−.001(.003),P.66 fits rounded normal.54851–.88640. A hidden endpoint sign is not inferred. |
| S232 | Supplement p 21 utility therapy overall.002(−.004,.007),P.51 contains 0; T 12.004(.003),P.23 fits rounded normal.07186–.31731. |
| S233 | Supplement p 21 utility interaction overall−.002(−.008,.003),P.42 contains 0; T 12.001(.003),P.65 fits rounded normal.54851–.88640. |
| S234 | Supplement p 22 therapy MDD CACE.78(.64,.95) contains its estimate/excludes 1; the P<.05 star agrees with main p 8. C010 remains the methods-mapping issue without re-emission. |
| S235 | Supplement p 22 supplement MDD CACE.84(.67,1.07) contains its estimate/includes 1 and has no star; main nonsignificance agrees. Positive ITT-to-negative CACE mapping remains C010. |
| S236 | Supplement p 22 therapy PHQ CACE−.22(−.59,.15) is contained/includes 0/has no star. Its complier estimand differs from the main T 12 robust fit; fitted mapping is unavailable. |
| S237 | Supplement p 22 supplement PHQ CACE.43(.08,.77) is contained/excludes 0 and its star agrees. No exact latent compliance fraction or original numerator is inferred. |
| S238 | Supplement p 22 therapy IDS CACE−.42(−1.24,.40) is contained/includes 0/has no star; direction agrees with ITT. CACE and ITT are not matched copies. |
| S239 | Supplement p 22 supplement IDS CACE.47(−.33,1.27) is contained/includes 0/has no star; positive direction agrees with ITT, without a significance claim. |
| S240 | Supplement p 22 therapy GAD CACE−.31(−.60,−.02) is contained/excludes 0 and its star agrees; lower-anxiety narrative is compatible with the negative coefficient. |
| S241 | Supplement p 22 supplement GAD CACE.18(−.11,.47) is contained/includes 0/has no star. Positive direction agrees with ITT but nonsignificance is retained. |
| S242 | Supplement p 23 all 12 count/percentage pairs use arm totals 195/193/188/183, sum 759. Allocation-belief association agrees with P<.001;307/759=40.448% versus main 40.4% is precision-compatible. Exact test remains unspecified. |

## Excluded observations

This table consolidates each repeated apparent observation once while naming every original checker row: N1–N8 are the numeric checker's rows, X1–X10 cross-source, T1–T9 statistical pass 1. Thus all 27 input rows are accounted for by 20 records, each with exactly one reason code. Initial-screen finding exclusions are followed separately above; they are not re-emitted.

| Location | Observation | Reason code |
|---|---|---|
| Main p3/supplement p3; N1 | BMI15 versus25 is already included as C003/F-XS-001, route A category2. The earlier numeric OUT_OF_FOCUS treatment does not govern this pass; no new distinct issue is emitted. | DUPLICATE_OF_INCLUDED |
| Main pp4/6,SAP p4,supplement p16; N2,X9 | ≥70% versus more-than70% wording has no supplied boundary-participant value or differing CACE result; the operative≥70% threshold is explicit. | TERMINOLOGY_OR_WORDING |
| Main p4; N3 | 196/(1−22%) versus250: recomputed[249.0446,253.5484] overlaps printed[249.5,250.5], gap0. This is distinct from included C004's total identity. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p6 footnotes d/f and abstract; N4,X1 | Repeated without-therapy wording beside22/256 is mapped to its complement by footnote f. Counts, percentages and numerical effect direction do not change. | TERMINOLOGY_OR_WORDING |
| Main pp6–8 versus available counts/means; N5,X5,T5 | Adjusted/effect-coded MI OR/HR/B are not declared crude ratios/differences; the crude comparison supplies no printed model-value conflict. | MODEL_VERSUS_CRUDE |
| Supplement p12; N6 | 211/1025 versus22%: conservative recomputed[20.5266,20.6442]%, printed[21.5,22.5]%, relative gap.03890≤.05. Within-display category3 is not reproduced under precision. | ROUNDING_OR_DISPLAY_PRECISION |
| Supplement pp12/16; N7 | Single-visit211–331 versus paired-change335/334 describes different available-data subsets; this peripheral biomarker comparison does not change a primary/key-secondary result or trial analysis-population size. | PERIPHERAL_COMPARISON |
| Protocol p35/supplement p12; N8,X6 | FFQ264/250 and TFEQ18/21 instrument descriptions do not alter a primary/key-secondary endpoint value or the1025 analysis population. | PERIPHERAL_COMPARISON |
| Protocol p28 versus pp33–34/main p4; X2 | The same MINI V5 operational DSM-IV tables identify the instrument; no changed episode components or count is supplied. Existing F-ST1-011 screening is considered above. | TERMINOLOGY_OR_WORDING |
| Main p8 Table3/narrative; X3,T4 | Small PHQ/IDS doubling differences have overlapping half-unit input/output intervals, gap0. No numerical-value discrepancy survives precision. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p8/supplement p21; X4 | MI and no-MI coefficients explicitly use different analyses; interaction inclusion also differs. They are not printed copies of one fit. | CONTEXT_RESOLVES |
| Main p7 Figure2; X7 | Nine-month axis ticks do not supply a nine-month assessment; measurements/contributors are listed at0/3/6/12. No quantitative value changes. | NOTATION_OR_TYPOGRAPHY |
| SAP p3/main p8; X8 | Standardized D points are present and unstandardized CI/P are identified. Missing D-specific uncertainty supplies neither an absent whole analysis nor a conflicting printed number; F-ST1-009 screening is retained. | CONDITIONAL_OR_UNREPORTED |
| Supplement p19; X10,T1 | Baseline GAD P=0 denotes a very small P; its positive CI agrees with significance. No independent route-A interval/test contradiction is present. | ROUNDING_OR_DISPLAY_PRECISION |
| Supplement p21 T12 B/SE/P; T2 | PHQ therapy−.22/.11,P.052 and IDS supplement.28/.28,P.30 fit rounded normal diagnostic ranges; all12 rows were checked. No identified test conflict is dismissed as rounding. | ROUNDING_OR_DISPLAY_PRECISION |
| Supplement p20 C1/C2; T3 | Rounded.000 coefficients permit nonzero underlying values; P.952/.944/.935 and null-containing intervals establish no estimate/test conflict. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p8 IDS T12; T6 | Adjusted B−.28 and mean/SD-change D+.006 are explicitly different quantities; no matched-estimand direction reversal is established. | MODEL_VERSUS_CRUDE |
| SAP p5 versus REPORT; T7 | Outlier-with/without and log transformations are conditional. No supplied observation establishes their trigger or a contradictory reported fit. | CONDITIONAL_OR_UNREPORTED |
| Protocol pp43–44/SAP p3 versus REPORT; T8 | Ancillary mediation/biomarker/adherence analyses are not primary/key-secondary comparisons; SAP defers other modifiers. Planned country/site components remain included as C007. | PERIPHERAL_COMPARISON |
| Protocol p16/main p4; T9 | Dropout20%/22% has interval gap1 point, relative1/20=.05 or1/22=.045455, within precision. Active incidence15%/20% and180/196 remain included C005. | ROUNDING_OR_DISPLAY_PRECISION |

## Limits and handoff

All 82 S IDs were revisited with the full cross-lane ledger and every recheck alternative; no scientific relationship or constituent contrast was omitted. All 27 input exclusion rows and three screened findings were checked in both route-A and route-B terms. Existing included patterns were not re-emitted. Missing definitions remain exact robust/MI variance and degrees of freedom, actual power counting unit/algorithm, governing plan amendments/chronology, primary RERI and primary missingness sensitivity result locations, fitted CACE numerator/scale/compliance equations, site-specific CI construction, and raw missingness/adherence data. These prevent certain exact model reconstructions, not source coverage. No final correction, disposition or preferred method is assigned.

Artifacts: checkers/statistical_pass_2.md and statistics/relationship_inventory.md. New derivatives: none. Sources and reused assets remain unchanged. Every existing candidate remains Pending Human Adjudication.
