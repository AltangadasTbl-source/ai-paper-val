# Initial screening — complete registration handoff

Agent: /root/inclusion_screener; fresh gpt-6.1-sol/high. All 26 assigned findings independently qualify, consolidated into 17 issue groups. G labels are handoff locators, not stable candidate IDs. No severity, acceptance or adjudication is assigned. Every later candidate remains Pending Human Adjudication. Groups use positive report anchors in source order; report-internal issues precede later support-only displays. The coordinator may order stable IDs by its established source-order key without changing membership.

## Source authority and exact identity

- DOC-001 REPORT: [main article](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=1),14 physical pages.
- DOC-002 PLAN: [protocol](../../../joi250046supp1_prod_1755300121.14087.pdf#page=1),77 physical pages, operative version5.0.
- DOC-003 PLAN: [SAP](../../../joi250046supp2_prod_1755300121.15087.pdf#page=1),29 physical pages, version6.0,18July2024; analytical SAP takes precedence over protocol where supplied.
- DOC-004 REPORT: [TIDieR](../../../joi250046supp3_prod_1755300121.15087.pdf#page=1),7 physical pages; delivered-intervention description, not a prospective plan.
- DOC-005 REPORT: [results supplement](../../../joi250046supp4_prod_1755300121.15587.pdf#page=1),19 physical pages.
- DOC-006 REPORT: [results workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx),worksheet eTable3,A1:J115.

Fresh direct Poppler pdftotext26.01.0 CPU outputs: preprocessing/screen_initial/main.txt, results.txt and tidier.txt. Exact workbook ZIP/XML: preprocessing/screen_initial/sheet1.xml and sharedStrings.xml; mechanical Node-decoded525 nonempty exact cells: preprocessing/screen_initial/cells.tsv. No formulas were recalculated. Direct-source page images reread include main9–11; protocol43,56–58; SAP2–4,19–23; results7–10,14,17, with direct text rereads for the other cited REPORT paragraphs and footnotes. These derivatives identify exact supplied source pages; they are not additional documents or independent authority.

## Group-to-screen-row membership

| Group | Included Finding IDs | Proposed review domain | Primary type | All relationships |
|---|---|---|---|---|
| G001 | F-XS-004, F-ST1-004 | statistical_results | S_W | S_W |
| G002 | F-XS-001 | protocol_report | P_R | P_R |
| G003 | F-ST1-222 | protocol_report | P_R | P_R, P_P |
| G004 | F-XS-002, F-ST1-221 | protocol_report | P_R | P_R, S_C, S_W |
| G005 | F-XS-003, F-ST1-223 | protocol_report | P_R | P_R |
| G006 | F-NUM-001 | statistical_results | S_W | S_W |
| G007 | F-XS-005 | protocol_report | P_R | P_R |
| G008 | F-ST1-003 | statistical_results | S_W | S_W |
| G009 | F-NUM-103, F-ST1-001 | statistical_results | S_W | S_W |
| G010 | F-ST1-005, F-ST1-105 | statistical_results | S_C | S_C, S_W |
| G011 | F-NUM-101, F-ST1-002 | statistical_results | S_W | S_W |
| G012 | F-NUM-102 | statistical_results | S_W | S_W |
| G013 | F-ST1-103 | statistical_results | S_W | S_W |
| G014 | F-ST1-104 | statistical_results | S_W | S_W |
| G015 | F-NUM-104, F-ST1-101, F-ST1-102 | statistical_results | S_W | S_W |
| G016 | F-ST1-401 | statistical_results | S_W | S_W |
| G017 | F-NUM-002, F-ST1-106 | statistical_results | S_W | S_W |

Compound F-ST1-002 qualifies for G011's interval rule and is assigned to that screening row only; its point-standardization component is fully preserved in G012's evidence and may be cited as supporting checker provenance, but G012's classification Finding IDs remains F-NUM-102 so each screen row has one eventual candidate cell. This does not lose any component or location. G003 retains P_P because SAP19's primary-versus-triggered role and SAP4's amendment wording also constitute the same unresolved PLAN-internal role; P_R takes precedence. G010 is a shared presentation-rule pattern across two REPORT documents, so S_C has precedence over its within-display S_W components. G016's main scale definition corroborates the internal supplement header/value conflict; it does not itself conflict with another REPORT value, so S_W is the best-supported primary classification, while the checker's S_C alternative is retained for mechanical recheck.

## G001 — Significant-benefit prose versus physical-function pairwise intervals

**Finding IDs:** F-XS-004, F-ST1-004. **Qualifying route:** Route A, category1. **Classification:** statistical_results; S_W; all S_W; REPORT main narrative versus REPORT main Table3. No plan is a conflicting comparator. Classification ambiguity: possible intended restriction of a general prose summary.

**All source locations:** [main1 abstract Results](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=1); [main7 Secondary Outcomes](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7); [main10 physical-function3/6-month rows](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10); [main4 test level](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

**Source evidence:** Main7 says “significantly better scores for both” active groups versusUC at3months, “persisting over12-month follow-up”; abstract1 describes “Statistically significant benefits” for both groups at6/12months for severity and other secondary pain/functioning outcomes. Physical-function PT−UC3months0.4(95%CI−0.1,0.9); HC−UC6months0.4(−0.1,0.9). Corresponding omnibusP=.02/.05; all tests two-sidedα=.05.

**Rule/calculation:** Both named95% pairwise intervals include zero; an omnibus hypothesis of any group difference cannot imply significance for both specified active-versusUC contrasts. Route A1 never uses the display rounding exclusion. The endpoints cross zero, independent of any exact test reconstruction.

**Named impact and inclusion:** The significance reading of PT physical function at3months andHC physical function at6months differs between prose and intervals. Category1 requires inclusion. Alternative: prose summarizes general patterns, the omnibus test, or only some secondary endpoints; record that narrower intended scope without supplying an unprinted pairwise test. The HC3-month and both12-month active/UC physical-function intervals are not implicated. Human question: Which outcome/contrast scope or different analysis supports the significant-both wording?

## G002 — Online-session duration in report versus protocol

**Finding IDs:** F-XS-001. **Qualifying route:** Route B. **Classification:** protocol_report; P_R; all P_R; PLAN protocol regimen versus REPORT main/TIDieR delivered-intervention descriptions. TIDieR corroborates the report side, so no S_C conflict. Ambiguity: expected versus empirically typical completion time is not distinguished.

**All source locations:** [protocol43 §10.1.1](../../../joi250046supp1_prod_1755300121.14087.pdf#page=43); [main3 Online Program](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=3); [TIDieR3 Procedures](../../../joi250046supp3_prod_1755300121.15087.pdf#page=3); [TIDieR4 delivery/dose continuation](../../../joi250046supp3_prod_1755300121.15087.pdf#page=4).

**Source evidence:** Protocol: “Each session takes45–60minutes to complete”; main: “Each session requires approximately30to45minutes to complete”; TIDieR describes eight online sessions30–45minutes each. All concern the same eight-session weekly program, intended within12weeks; year-long access is a different quantity.

**Precision/rule:** Lower endpoints45±.5 versus30±.5 leave14minutes,14/45=.3111; upper60±.5 versus45±.5 leave14,14/60=.2333. The ranges touching45 does not equate their endpoint descriptions. Eight-session descriptive totals360–480 versus240–360minutes are illustration, not measured exposure.

**B1/B2/B3:** Randomized duration/dose is an eligible report-plan statistical-design comparison; the text does not distinguish revised content/duration from observed completion time; extracting the intervention paired with primary severityRR1.28 would select differing expected session minutes. Alternative: actual completion proved shorter without changing content; this is source-plausible but not explicitly the reason for the ranges. Human question: Which duration description applies and what amendment or empirical definition connects them? Coaching60 versus approximately45–60minutes remains outside this group.

## G003 — Primary MAR versus triggered MNAR analysis role

**Finding IDs:** F-ST1-222. **Qualifying route:** Route A, category5. **Classification:** protocol_report; P_R; all P_R, P_P; PLAN SAP primary/sensitivity role and amendment versus REPORT primary role. P_R has precedence. Ambiguity: the SAP's “first approach” and IPW amendment can support a conditional-primary reading.

**All source locations:** [SAP19 §11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19); [SAP4 July17,2024 IPW amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4); [main4 primary missing-data methods](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [results4 Missing Data first paragraph](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [results7 eTable1 completeness](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [results11 complete-case sensitivity eTable7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).

**Exact statements:** SAP19: “For the primary analyses,we will analyze those patients who have follow-up data”; missing data assumedMAR conditional on baseline covariates; “conduct sensitivity analyses as required” if>15%3-month missingness or differential missingness, then its “first approach” is pattern-mixture imputation relaxingMAR plusIPW, and its second explicitly a worst/best-case sensitivity. SAP4 says “Current missing data approach imputes data using pattern mixture approach” for those with≥1follow-up and addingIPW permits an all-randomized interpretation. Results4 says criteria in theSAP prespecified the primary analysis to useMNAR plus weighting/adjustment. Main4 implements that as primary; eTable7 calls the complete-case adjusted approach sensitivity.

**Calculation/context:** Completeness77.1% implies missingness22.9±.05%, entirely above15±.5%; arm completeness79.9/69.8/81.6% establishes the trigger. The trigger itself is met and is not the discrepancy. Method identity is inSAP; claimed primary-versus-sensitivity role is the issue. The prespecified-primary-MNAR claim is not expressly stated as a replacement of the earlier primaryMAR role; the same role tension remains insideSAP19/4.

**Inclusion and alternatives:** Category5 includes a primary analysis replaced or a claimed prespecified role absent from its corresponding explicit plan language. Preserve the substantial alternative that the first triggered approach was intended as conditional primary and only the second as sensitivity; SAP4 further supports current pattern-mixture implementation. Do not claim MNAR/IPW was absent from the plan or preferMAR. Named result: main3-month adjusted severityMCID rates,RRs and confidence intervals. Human question: Does the supplied trigger/amendment replace the express primaryMAR analysis role, and which passage establishes that hierarchy?

## G004 — Age in claimed prespecified fixed base adjustment

**Finding IDs:** F-XS-002, F-ST1-221. **Qualifying route:** Route A, category5. **Classification:** protocol_report; P_R; all P_R,S_C,S_W; PLAN fixed-primary list versus REPORT added-age prespecification; REPORT main list versus REPORT supplement list; supplement4 first list versus later base list. PLAN takes precedence. Ambiguity: broad candidate-variable authorization versus mandatory base adjustment.

**All source locations:** [protocol56 §15.5](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56); [SAP20 §13/14](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20); [SAP2 age subgroup amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=2); [SAP3 amendments](../../../joi250046supp2_prod_1755300121.15087.pdf#page=3); [SAP4 amendments](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4); [SAP22 age moderator plan](../../../joi250046supp2_prod_1755300121.15087.pdf#page=22); [main4 adjustment list](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [results4 Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [results5 Non-Response Weighting](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5); [results8 imputation age row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [results9 estimation age row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [results10 weight age row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); [results11 sensitivity adjustment footnote](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).

**Source comparison:** Plan primary lists baseline severity,sex,site,rural/underserved residence,multisite pain andmental-health condition; main4 and results4 first sentence repeat that set. Results4 later calls the base list “pre-specified adjustment variables” and addsage; results5 usesage as a base weighting predictor. Fitted age terms appear in all three models: imputation.19(.12,.27),estimationRR1.15(1,1.33),weightOR.97(.70,1.35). Sensitivity footnote includesage. SAP13 lists age among candidate demographics/predictors, SAP16 prespecifies moderation; amendment2 addsage subgroup analyses, not mandatory primary adjustment.

**Rule and inclusion:** Set membership is discrete, no half-unit calculation applies. The affirmative claim of fixed-base prespecification versus the supplied fixed list qualifies byA5; it does not criticize age inclusion or the openly selectededucation/employment covariates. Named extraction: whether primary imputation/estimation/weighting and sensitivity adjustment included prespecifiedage. Alternative: broad candidate-variable clause was intended to authorizeage, or an additional fixed-model revision is outside the package. Human question: Which prospective primary-model passage establishesage's fixed-base role and which models useit?

## G005 — Own-baseline secondary covariate addition

**Finding IDs:** F-XS-003, F-ST1-223. **Qualifying route:** Route B. **Classification:** protocol_report; P_R; all P_R; PLAN secondary covariate paragraph versus REPORT stated addition. Ambiguity: plan list could have been intended as a minimum under “same proposed approach.”

**All source locations:** [protocol57 §15.6](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57); [SAP21 §15](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21); [main4 secondary adjustment sentence](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [main9 intensity/interference responder rows](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9); [main10 intensity/interference/social/physical rows](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10); [main11 continuous-table continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).

**Source comparison:** Operative plans specify “baseline levels of pain severity and all stratification variables” as secondary covariates; report uses same primary modeling structures “with added adjustment for the given baseline secondary outcome.” Baseline intensity,interference,social/physical function differ from the compositebaseline severity.

**B1/B2/B3:** In-scopeanalysis specification for key-secondary outcomes listed inabstract; explicit own-baseline addition is not equated by immediate context with the plan's different stated covariates; extraction of the covariate sets underlying Table2MCID andTable3continuous contrasts could differ. Numeric rounding does not apply. Alternative: “same proposed approach” permitted endpoint-specific baseline adjustment or plan lists were minimums; no explicit addedown-baseline provision is supplied. Do not include continuousseverity as a separate difference (samebaseline quantity), orPGIC (no baselinePGIC collection). Human question: Was endpoint-specific baseline adjustment prospectively specified, and which exact sets produced the listedsecondary results?

## G006 — Therapeutic-dose count/percentage

**Finding IDs:** F-NUM-001. **Qualifying route:** Route A, category3. **Classification:** statistical_results; S_W; all S_W; REPORT main paragraph/flow. Ambiguity: none in printed numerator/denominator; hypothetical alternative denominator is unprinted.

**All source locations:** [main4 Results session paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [main5 Figure1 painTRAINER allocation/sessioncategories](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5).

**Source evidence/calculation:** “371(43%)completed at least6sessions” among randomizedpainTRAINER; n776 with flow371+156+249=776. Sameparagraph527(68%)completed≥1; coach660(85%)and548(70%)forn778. 100×371/776=47.8093%. Inputbands[370.5,371.5]/[775.5,776.5] yield[47.714102%,47.904578%];43±.5% gives[42.5,43.5],gap4.214102,relative.0980024. The other session percentages reconcile.

**Inclusion/context/impact:** A3 count/denominator/percentage insideoneparagraph; ability to reconstruct near47.8 does not remove printed43. Namedextraction: fraction receiving≥6sessiontherapeuticdose. Alternative43% could use another population, but denominatornear863 exceeds randomized776 and no such definition isprinted. Humanquestion: Which numerator/denominator/percentage applies?

## G007 — Prespecified primary-outcome analyses without report counterparts

**Finding IDs:** F-XS-005. **Qualifying route:** Route A, category5. **Classification:** protocol_report; P_R; all P_R; PLAN specified additionalprimary-outcome analysisfamilies versus complete REPORT package. Ambiguity: primarywithinAim1b/1c versus mainclinical-efficacy publication scope; some power prose describes subgroup work assecondary. Retain that hierarchy nuance.

**All PLAN/source anchors:** [SAP21 §16 heading](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21); [SAP22 moderator/primarymediation text](../../../joi250046supp2_prod_1755300121.15087.pdf#page=22); [SAP23 mediationcontinuation](../../../joi250046supp2_prod_1755300121.15087.pdf#page=23); [protocol57 §15.7](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57); [protocol58 mediation](../../../joi250046supp1_prod_1755300121.14087.pdf#page=58).

**Complete REPORT absence scope:** [main1–14 startingpage](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=1), outcomes/results [main7](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), [main9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), [main10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), [main11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [TIDieR1–7startingpage](../../../joi250046supp3_prod_1755300121.15087.pdf#page=1); [results1contents](../../../joi250046supp4_prod_1755300121.15587.pdf#page=1) andall19pages, model/resultdisplays [results7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [results8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [results9](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9), [results10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10), [results11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11), [results14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), [results15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15), [results16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16), [results17](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17), [results18](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18); [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx)eTable3!A1:J115. These are inspectedabsence scopes, not fictionalpages with missingresults.

**Matchedcomponents:** Separateprimaryoutcome moderator×arm×time analyses for sex,age,race/ethnicity,rural/underserved,residential/multiplepainconditions,mentalhealthmooddisorders,negativeSDOH (sevenfamilies; residency andmultiplepain areseparate), primaryinteractioncomparison at3months. Three mediatorfamilies: catastrophizing,self-efficacy,perceivedsupport; separateactivearmversusUC mediation of6-monthseverityMCID. SAP explicitly calls them “Primary mediation analyses” and conditionsthem onsignificant6-montheffects. Gate met by PT/UC1.44(1.21,1.70),HC/UC1.62(1.39,1.90). Main/tablemodelcovariatemaineffects, selectionPvalues and baselinecharacteristics are notmoderatorinteractions ormediation estimates.

**Inclusion/impact:** No counterpart for moderatorinteractiontests/estimates ormediator/direct/indirect effects in thesuppliedREPORT package; A5 applies toplannedprimaryanalysisnonreporting. No numericrounding comparison applies. Alternative: additionalaims reserved forseparatemanuscripts; absenceonly in thispackage, not proofanalyses wereunperformed ornotelsewherereported. Humanquestion: Where are theseplannedprimaryoutcome families reported, orwhatsuppliedamendment/reporting-scope statement relocatesthem? Economic/tertiaryanalyses remainoutside thisgroup.

## G008 — Later modality no-difference claim versus global-general contrast

**Finding IDs:** F-ST1-003. **Qualifying route:** Route A, category1. **Classification:** statistical_results; S_W; all S_W; REPORT mainDiscussion versusTable3. Ambiguity: intendedrestriction toprimaryseverity.

**All source locations:** [main8Discussion](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=8); [main11 global-general6-monthHC/PTcells](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [main4 α=.05](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

**Evidence/rule:** “Outcomes between the2remote CBT-CP programs at6-and12-month follow-up did not differ”; HC−PT6-monthglobal-generaladjusteddifference−.2(−.4,−.1),SMD−.24(−.41,−.07),omnibusP<.001. Bothpairwise95%intervals excludezero; α=.05andLSDgateopen. Noomnibus/pairwise conflation. A1has norounding exclusion; upperMDband[−.15,−.05]doesnotreachzero.

**Impact/alternatives:** Extractedlatermodalityconclusion versusnamedglobal-general6-month result. Narrativecould intendonlyprimaryseverity,whoseHC/PTlaterRRintervals include1,ora differentmultiplicityanalysis; sentence'spluraloutcomesfollowssecondary/globaldiscussion anddoesnotstate therestriction. Humanquestion: Doesno-differenceclaimexclude thisendpoint,orwhichdifferenttestproduces thatclaim?

## G009 — HC/PT NNT confidence-set pattern and containment

**Finding IDs:** F-NUM-103, F-ST1-001. **Qualifying route:** Route A, category1. **Classification:** statistical_results; S_W; all S_W; REPORT main Table2 confidence sets versus same-table RR sets and primary narrative. Ambiguity: different RR/RD interval procedures, or omitted disconnected-branch signs.

**All source locations:** [main9 Table2 HC/PT RR/NNT columns and footnotes d/e](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9); [main7 last Primary Outcomes sentence](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7); [main4 NNT definition/test level](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

| Outcome/time, HC/PT | RR (95%CI) | NNT (95%CI) | Component |
|---|---|---|---|
| Severity6months |1.13(.98,1.30)|24(12,186)|Null-containing RR and stated later-primary nonsignificance versus finite positive NNT endpoints|
| Severity12months |1.07(.96,1.19)|41(17,76)|Same|
| Intensity3months |1.11(.93,1.33)|37(14,57)|Null-containing RR versus finite positive NNT endpoints|
| Intensity6months |1.18(1.00,1.40)|21(11,5524)|Printed RR boundary includes null; unrounded boundary is a specific alternative|
| Intensity12months |1.05(.92,1.20)|63(18,38)|Null conflict and point above upper NNT bound|
| Interference6months |1.10(.96,1.27)|26(11,67)|Null-containing RR versus finite positive NNT endpoints|
| Interference12months |1.07(.97,1.18)|39(16,79)|Same|

**Calculation/rule:** NNT=1/adjusted response-probability difference. Footnote e explicitly describes an RD interval containing0 as a positive NNT lower branch to infinity plus a negative NNH upper branch to negative infinity. No affected row prints that negative branch. For intensity12,63∉[18,38]; even bands[62.5,63.5] versus upper[37.5,38.5] leave24,24/63=.38095. A1 does not apply rounding exclusions to interval/test/null conflicts. The six non-boundary RR lower bounds remain below1 with±.005; intensity6's printed1.00 can hide an unrounded limit above1 and remains a bounded component with that alternative. Main7 explicitly says HC/PT severity differences are no longer significant at6/12months.

**Inclusion/impact/alternatives:** A1 applies independently to the containment and stated interval/test readings. The underlying risk-difference CI/covariance construction is not supplied; RR andRD could use different procedures, and endpoints could be intended as disconnected branches with an omitted sign. Preserve those alternatives rather than claiming mathematical identity of unspecified interval estimators. Named extraction: all seven HC/PT NNT confidence sets, especially63(18,38). Human question: What signed/disconnected NNT/NNH confidence sets and underlyingRD intervals apply, and how do they relate to the reported nonsignificant later severity comparisons?

## G010 — NNT reciprocal definition and integer presentation

**Finding IDs:** F-ST1-005, F-ST1-105. **Qualifying route:** Route A, category4. **Classification:** statistical_results; S_C; all S_C,S_W; REPORT main and results supplement repeat the same supplied reciprocal definition and presentation pattern. No plan comparator. Ambiguity: a source-supported ceiling convention fully reproduces these points, but is not expressly defined in either source footnote.

**All source locations:** [main4 NNT Methods](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [main9 Table2 HC/UC6-month severity/interference points and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9); [results14 eTable8 reminder-letter6-month PT/UC point and footnote d](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14); [results11 eTable7 complete-case3-month points](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11), which supply evidence for the alternative integer convention rather than another discrepancy.

| Exact row | Response percentages | Recomputed reciprocal interval allowing±.05 percentage points per input | Printed point band | Gap | Relative gap |
|---|---|---|---|---:|---:|
| Main severity6 HC/UC |37.1−22.9|[6.993007,7.092199]|8±.5=[7.5,8.5]|.407801|.050975|
| Main interference6 HC/UC |40.9−24.3|[5.988024,6.060606]|7±.5=[6.5,7.5]|.439394|.062771|
| Reminder6 PT/UC |35.6−21.3|[6.944444,7.042254]|8±.5=[7.5,8.5]|.457746|.057218|

**Normative reproduction and qualification:** The supplied quantity is the reciprocal of the adjusted response difference. Under the workflow's prescribed input/output half-unit comparison these three remaining relative gaps exceed.05. The same reciprocal comparison reproduces the other25 main points and44 sensitivity points within the prescribed tolerance; thereforeA4 applies. This is not an adjusted-versus-crude comparison. No assertion is made that nearest-integer presentation is necessary, or that ceiling presentation is unsupported. The missing presentation definition is the human question, as required when a method reproduces other rows but a numeric reading does not.

**Complete main-table source-supported alternative:** Ceiling of an unrounded reciprocal within each interval below can reproduce every printed Table2 NNT integer, including both affected points; hence no main NNT point is incompatible with that concrete policy. Contrast order PT/UC;HC/UC;HC/PT.

| Outcome/time | Inverse intervals | Printed NNTs |
|---|---|---|
| Severity3 |[16.9492,17.5439];[8.8496,9.0090];[18.1818,18.8679]|18;9;19|
| Severity6 |[9.9010,10.1010];[6.9930,7.0922];[23.2558,24.3902]|10;8;24|
| Severity12 |[11.2360,11.4943];[8.8496,9.0090];[40.0000,43.4783]|12;9;41|
| Intensity3 |[14.9254,15.3846];[10.6383,10.8696];[35.7143,38.4615]|16;11;37|
| Intensity6 |[16.9492,17.5439];[9.2593,9.4340];[20.0000,20.8333]|18;10;21|
| Intensity12 |[17.2414,17.8571];[13.5135,13.8889];[58.8235,66.6667]|18;14;63|
| Interference3 |[13.6986,14.0845];[8.1301,8.2645];[19.6078,20.4082]|14;9;21|
| Interference6 |[7.8125,7.9365];[5.9880,6.0606];[25.0000,26.3158]|8;7;26|
| Interference12 |[10.9890,11.2360];[8.4746,8.6207];[35.7143,38.4615]|12;9;39|

Additional explicit alternative evidence: eTable7 complete-case3 PT/UC100/(32.2−24.0)=12.195→13; eTable8 reminder3 HC/UC100/(34.1−20.5)=7.353→8. For reminder6 PT/UC, values just above7 in[6.944444,7.042254] yield ceiling8. Some other rows' unrounded values can lie below the displayed central reciprocal, so the alternative is checked using input rounding intervals, not a requirement to ceiling central values. Both sources give the reciprocal definition but do not state the integer ceiling policy.

**Named impact and human question:** NNT point extraction for the three named rows and whether reported integers represent reciprocal estimates or a specific presentation transformation. Which integer presentation rule and unrounded adjusted risks generated them? Do not propose a replacement integer or preferred policy. This issue's point-presentation rule is separate fromG009's confidence-set and containment rule.

## G011 — SMD interval block: order, containment and null reading

**Finding IDs:** F-NUM-101, F-ST1-002 (interval component). **Qualifying route:** Route A, category1; endpoint reversals also meet category2. **Classification:** statistical_results; S_W; all S_W; REPORT main Table3 points, intervals, unstandardized contrasts and stated scale definition. Ambiguity: distinct interval construction or column associations; no single reordering is asserted.

**All source locations:** [main10 Table3 severity/intensity/interference/social/physical blocks](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10); [main11 Table3 global-pain/general continuation and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [main4 adjusted SMD Methods](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4). Every affected outcome/time/contrast is specified below;PT/UC,HC/UC,HC/PT is the actual source order.

**All18 reversed social/physical SMD pairs:**

| Outcome/time | PT/UC SMD (CI) | HC/UC SMD (CI) | HC/PT SMD (CI) |
|---|---|---|---|
| Social3 |.12(.23,.11)|.01(.12,−.00)|.20(.29,.19)|
| Social6 |.18(.23,.05)|.06(.11,−.06)|.26(.30,.15)|
| Social12 |.19(.21,.01)|.07(.09,−.10)|.27(.28,.12)|
| Physical3 |.09(.16,.07)|−.02(.05,−.04)|.16(.22,.15)|
| Physical6 |.15(.09,−.06)|.02(−.03,−.18)|.22(.16,.05)|
| Physical12 |.20(.18,−.03)|.07(.04,−.16)|.27(.25,.09)|

**All14 point-containment components, even after sorting descending pairs:** Physical6 all three points(.15,.02,.22) and physical12 all three(.20,.07,.27) lie outside their respective sorted endpoint sets above. Further cells:

| Outcome/time/contrast | Point | Printed CI |
|---|---:|---|
| Severity12 PT/UC |−.25|−.24,.01|
| Severity12 HC/UC |−.36|−.35,−.12|
| Intensity12 HC/UC |−.27|−.26,−.12|
| Interference12 PT/UC |−.26|−.25,.01|
| Interference12 HC/UC |−.37|−.36,−.11|
| Global pain12 PT/UC |−.55|−.50,.05|
| Global pain12 HC/UC |−.57|−.54,−.08|
| Global pain12 HC/PT |−.29|−.25,.14|

**Full union of null-membership components:** Footnote d defines SMD as the adjusted between-group mean difference divided by the positive UC change SD at the given outcome/time; that simple rescaling preserveszero inclusion. Preserve all these pairs, including F-ST1-002 components beyond F-NUM-101's shorter examples.

| Outcome/time/contrast | Adjusted mean-difference CI | SMD CI, printed order |
|---|---|---|
| Severity12 PT/UC |−.6,−.2|−.24,.01|
| Intensity12 PT/UC |−.4,−.1|−.16,.00|
| Interference12 PT/UC |−.7,−.3|−.25,.01|
| Social3 PT/UC |.0,1.5|.23,.11|
| Social3 HC/UC |.8,2.2|.12,−.00|
| Social3 HC/PT |−.0,1.4|.29,.19|
| Social6 HC/UC |.8,2.2|.11,−.06|
| Social6 HC/PT |−.4,1.1|.30,.15|
| Social12 HC/UC |.6,2.1|.09,−.10|
| Social12 HC/PT |−.7,.9|.28,.12|
| Physical3 PT/UC |−.1,.9|.16,.07|
| Physical3 HC/UC |.2,1.2|.05,−.04|
| Physical3 HC/PT |−.2,.8|.22,.15|
| Physical6 PT/UC |.1,1.2|.09,−.06|
| Physical6 HC/UC |−.1,.9|−.03,−.18|
| Physical6 HC/PT |−.8,.3|.16,.05|
| Physical12 PT/UC |.3,1.5|.18,−.03|
| Physical12 HC/UC |.2,1.4|.04,−.16|
| Physical12 HC/PT |−.7,.5|.25,.09|
| Global pain12 PT/UC |−.8,−.5|−.50,.05|

**Precision/component conclusions:** A1 containment and interval/test/null conflicts do not use rounding exclusion, including printed boundary0/−0.00 alternatives. Numeric endpoint reversal is not merely a dash glyph: social3PT/UC first.23±.005 versus second.11±.005 leaves reversal gap.110,relative1.000; everydescending pair remains reversed beyond.05relative allowance. Physical6PT pointband[.145,.155] versus sortedupperband[.085,.095] leaves.050. Sorting alone does not resolve fourteen containment cases. The zero-boundary mean-difference/SMD components may hide a nonzero unrounded endpoint; retain that alternative instead of treating it as an independently reconstructed test. Independent non-boundary containment and null conflicts establish inclusion without those boundary components.

**Impact/alternatives/human question:** Extracted standardized-effect95%CIs, their contrast association and statistical-support reading for every listed cell. Alternative: columns/endpoints were associated with other contrasts, or another interval procedure was used; unknown numerical SD/covariance prevents full construction, but does not remove the printed containment category. Which ordered limits, point estimates and contrast assignments should be extracted under the stated definition? Do not prescribe limits. The different point-standardization rule isG012 rather than another occurrence of this interval rule.

## G012 — SMD points versus shared positive UC SD definition

**Finding IDs:** F-NUM-102. Additional checker provenance: F-ST1-002's point component, preserved without assigning its single screening row to two candidates. **Qualifying route:** Route B; same-display method reproduction also supplies category4 for the directidentity component. **Classification:** statistical_results; S_W; all S_W; REPORT main Table3 points/differences/footnote d. Ambiguity: another standardization population or contrast association could explain the points but is not the printed definition.

**All source locations:** [main10 Table3 all affected severity/intensity/interference/social/physical rows](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10); [main11 all global-pain/general rows and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [main4 SMD definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

**Rule:** Source defines adjusted mean difference divided by UC changeSD at that outcome/time. A common positive SD meansC=B−A for SMDsA=PT/UC,B=HC/UC,C=HC/PT. Each two-decimal input permits±.005,soB−A permitscentral±.010 andC±.005. Full17 identity gaps:

| Outcome/time | A;B;C | Recomputed B−A interval | Printed C interval | Relative gap |
|---|---|---|---|---:|
| Severity3 |−.25;−.34;−.13|[−.100,−.080]|[−.135,−.125]|.19231|
| Intensity6 |−.17;−.27;−.04|[−.110,−.090]|[−.045,−.035]|1.12500|
| Intensity12 |−.16;−.27;−.03|[−.120,−.100]|[−.035,−.025]|2.16667|
| Interference3 |−.25;−.34;−.13|[−.100,−.080]|[−.135,−.125]|.19231|
| Interference6 |−.27;−.37;−.14|[−.110,−.090]|[−.145,−.135]|.17857|
| Social3 |.12;.01;.20|[−.120,−.100]|[.195,.205]|1.47500|
| Social6 |.18;.06;.26|[−.130,−.110]|[.255,.265]|1.40385|
| Social12 |.19;.07;.27|[−.130,−.110]|[.265,.275]|1.38889|
| Physical3 |.09;−.02;.16|[−.120,−.100]|[.155,.165]|1.59375|
| Physical6 |.15;.02;.22|[−.140,−.120]|[.215,.225]|1.52273|
| Physical12 |.20;.07;.27|[−.140,−.120]|[.265,.275]|1.42593|
| Global pain3 |−.62;−.62;−.37|[−.010,.010]|[−.375,−.365]|.95946|
| Global pain6 |−.54;−.55;−.29|[−.020,.000]|[−.295,−.285]|.91379|
| Global pain12 |−.55;−.57;−.29|[−.030,−.010]|[−.295,−.285]|.87931|
| Global general3 |−.66;−.66;−.40|[−.010,.010]|[−.405,−.395]|.96250|
| Global general6 |−.46;−.50;−.24|[−.050,−.030]|[−.245,−.235]|.77083|
| Global general12 |−.53;−.58;−.28|[−.060,−.040]|[−.285,−.275]|.76786|

**Three further rows:** Additivity itself reconciles, but source-defined commonSD normalization of the adjusted differences still does not. Infer allowablepositiveSD from PT/UC adjusted difference andSMD, each with fullinput rounding; propagate HC/PT adjusted difference throughthat range.

| Outcome/time | PT/UC difference;SMD | UC SD interval | HC/PT difference;SMD | Recomputed HC/PT SMD interval | Printed point band | Relative gap |
|---|---|---|---|---|---|---:|
| Severity12 |−.4;−.25|[1.37255,1.83673]|.0;−.11|[−.03643,.03643]|[−.115,−.105]|.62340|
| Intensity3 |−.3;−.21|[1.16279,1.70732]|−.0;−.08|[−.04300,.04300]|[−.085,−.075]|.40000|
| Interference12 |−.5;−.26|[1.69811,2.15686]|.0;−.12|[−.02944,.02944]|[−.125,−.115]|.71296|

All20 rows above exceed.05 after interval propagation. Severity6alone: B−A[−.110,−.090] versusC−.12±.005 leaves.005/.12=.04167 and direct sharedSDcomparison only.0119relative; it does not independently qualify and is not presented as affected. Sign examples within the same20-rowpattern: physical3HC/UC difference+.7 versusSMD−.02; physical6HC/PT difference−.3 versusSMD+.22; physical12HC/PT difference−.1 versusSMD+.27; globalpain12HC/PT difference+.1 versusSMD−.29.

**B1/B2/B3 and alternatives:** Statistical-method/estimate identity is in focus; footnote specifies a common positive denominator, andno immediate singlecolumn or separate-normalization explanation is supplied; a systematicreview could extractdifferentdirection/magnitude from theprintedSMDpoints versusstatednormalization. NumericalUC SDs areunprinted,but noSDnumerical value isneeded for theidentity. Other standardization populations/contrast associations arepossible, notprinted; do not substitute acrude estimator orassume which numbershouldreplace another. Humanquestion: Whatdenominator/contrast mapping producedall20rows underfootnote d? This logical-point identity isdistinct fromG011's confidence-interval rule.

## G013 — Binary education selection versus fitted parameterization

**Finding IDs:** F-ST1-103. **Qualifying route:** Route B. **Classification:** statistical_results; S_W; all S_W; REPORT supplement final-selection summary versus fitted model tables. Ambiguity: different selection/final model stages may explain the parameterization.

**All source locations:** [results7 eTable2 final selected imputation/estimation variables](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [results8 eTable3 three education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [results9 eTable4 three education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [results4 selection procedure](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4).

**Source evidence/rule:** eTable2 nameseducation “any college vs.HS degree or less” as final selection. Fitted imputation education coefficients−.02,.16,.39 and fitted primary-estimationRRs.97,1.16,1.35 appear as three separate education parameters withHSorlessreference (twoAA labels,thenGraduate). A singlebinary variable againstone reference givesonecoefficient; thetableprints three. Nohalfunit arithmetic applies todiscreteparametercount.

**B1/B2/B3:** Model specification inprimary analysis; immediatecontextdoesnot distinguishcollapsedselectioncoding fromexpandedfinalfit; extractionofprimaryimputation/estimationcovariaterepresentationchanges. DuplicateAAwording alone isnot registered; theone-versus-three parameter mismatch istheissue. Alternative: eTable2 describesselectionstage, withmultilevelcoding retained only infinalmodels,butthatmapping isnot stated inits “FINAL VARIABLES SELECTED” section. Humanquestion: Whichcodingwasused atwhichstage andhowdo thethreeparameters relateto thelistedbinarycontrast?

## G014 — Selected weighting covariates versus fitted weighting model

**Finding IDs:** F-ST1-104. **Qualifying route:** Route B. **Classification:** statistical_results; S_W; all S_W; REPORT supplement selected list versus fitted weight table. Workbook selection P cells corroborate the inclusion basis, not a separate conflict. Ambiguity: incomplete fitted summary or a different selection stage.

**All source locations:** [results5 nonresponse selection rule](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5); [results6 fitted-model reference](../../../joi250046supp4_prod_1755300121.15587.pdf#page=6); [results7 eTable2 final weight variables](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [results10 eTable5 all rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx)eTable3!H12:J12,H18:J18,H39:I39,H81:I81,H84:I84,H108:I108.

**Source evidence:** Additional selectedweightcovariates:PEG,PHQ8,GAD7,anynegativeSDOH,education. Base listdoesnotincludeemployment. FitprintsPEG.96,PHQ8.97,GAD7.99,nonegativeSDOH1.34,andnotemployed1.49(1.11,2.00),P=.008,withoutanyeducationrow. ExactworkbookemploymentH18<.001,I18=.0228,J18=.0591;educationH12=.0156,J12=.05,I12blank. Other corroboratingrows:H39=.0636/I39=.0196;H81<.001/I81=.0095;H84=.0327/I84=.0331;H108=.0245/I108=.0405. TheblankI12 isnot treated asP=0or asproofof a failedtest.

**B1/B2/B3:** Covariatemembershipdeterminesnonresponseweightsusedintheprimarymodel; twodisplaysbothnamedfinalmodelinformationdonotidentifytheactualmembership; extractionoftheprimaryweightingspecificationcouldtakeeducationoremployment. Rounding isnotapplicabletosetmembership. Alternative:educationrowisomittedfromanincompletefitsummary,employmententeredunderanotherselectionrule,orthetablesdescribe differentstages. Humanquestion: Whichexactcovariatesproducedtheprimaryweights andhowareeTable2/5mapped? Do notinfer a missingcoefficientvalue.

## G015 — Model-table printed interval/P conflicts

**Finding IDs:** F-NUM-104,F-ST1-101,F-ST1-102. **Qualifying route:** Route A, category1. **Classification:** statistical_results; S_W; all S_W; each pair of conflicting inferential values is within the same REPORT supplement row. Repeated same-rule pattern across imputation,estimation andweighting model tables. Ambiguity: unroundednull-boundarylimits orseparateinferential procedures.

**All source locations:** [results8 eTable3 exactsevenrows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [results9 eTable4 age andsecondAAeducation](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [results10 eTable5PEG](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); methodcontext [results4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [results5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [main4 α=.05](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

| Exact row | Estimate |95%CI | P |
|---|---:|---|---:|
| eTable3 Pattern2observed follow-ups |−.28|−.47,−.08|.150|
| eTable3 Pattern1observed follow-up |−.20|−.36,−.03|.226|
| eTable3 Pattern2×PT |−.30|−.58,−.02|.280|
| eTable3 Pattern2×HC |−.47|−.74,−.19|.090|
| eTable3 Site3 |.19|.08,.29|.069|
| eTable3 Site4 |.15|.05,.24|.124|
| eTable3 secondEducationAA |.16|.07,.25|.077|
| eTable4 Age≥65 |1.15|1,1.33|.046|
| eTable4 secondEducationAA |1.16|1,1.33|.046|
| eTable5PEG |.96|.92,1.00|.037|

**Reproduction/components:** Firstseven coefficientintervalsexcludezero whileP>.05. Theirnearest-null endpointsremain−.075,−.025,−.015,−.185,.075,.045,.065 even with±.005display allowances,and Pbandsdonotapproach.05. Lastthreeprintedratiointervalsincludenull1attheboundary whileP<.05. Theprintedlower1 in eTable4isnottranscribedas a sourceprinted1.00; the significance comparison usesitsprintednullboundary. A1 isnever excludedbyrounding,includinglastthree. No exactnormal-Wald orunknownDFbackcalculation replacesreportedtests.

**Impact/alternative/human question:** Modelcoefficients'interval/testsignificance readingsusedtodescribetheprimaryimputation,estimationandnonresponseprocess. Alternative: underlyingage/educationlowerlimitsareslightlyabove1orPEGupperlimitbelow1;differentvariance/reference-distributionoranalysiscouldproduceCIs andPvalues. These aresource-grounded possibilities,nottheprintedstatement; no separateattributionisidentified. Whichinterval/testspecificationsandunroundedboundsapply toeachrow? Duplicatededucationlabelsareseparatelyterminologyobservations, notgroundsforremovingnumericA1 conflicts.

## G016 — Global-impression raw median summary identity

**Finding IDs:** F-ST1-401. **Qualifying route:** Route B. **Classification:** statistical_results; S_W; all S_W; REPORT supplement raw-median header versusnumericcells, with main scale definition ascorroboration. Classificationambiguity: checker'sS_C isanalternative ifthemainmeasurementdefinitionistreatedas aconflictingcomparator ratherthancorroboration; best-supportedprimary isS_W.

**All source locations:** [results17 eTable11 rawmedian/quartileheader andfivecells](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17); [results18 footnote b GEE mean contrasts](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18); [results15 narrative referringto eTable11unadjustedmeansecondaryoutcomes](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15); [main11 Table3h/i single-item1–7definitions](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [main4globalmeasurement](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

**Source-specific rule:** Bothglobaloutcomesareindividualone-item1–7responseswithsevenintegercategories. Ordinaryrawsamplemedian mustbe anintegerorhalf-integer (averageoftwocentralintegers),not a generalcontinuousmean. Printedone-decimalcenterallows±.05; categoricalpermissiblemediansareexact,notroundedestimates. Nearestpermissiblemedianmakesgapconservative.

| Exact global-impression cell | Printed center/parentheses | Center band | Nearest permissible median | Gap/printedcenter |
|---|---|---|---:|---:|
| Pain6PT |2.8(2.7,2.9)|[2.75,2.85]|3.0|.15/2.8=.05357|
| Pain12PT |2.8(2.7,2.9)|[2.75,2.85]|3.0|.05357|
| Pain12UC |2.2(2.1,2.3)|[2.15,2.25]|2.0|.06818|
| General3PT |2.7(2.6,2.7)|[2.65,2.75]|2.5|.05556|
| General6UC |1.8(1.7,1.9)|[1.75,1.85]|2.0|.08333|

**B1/B2/B3:** Statisticalsummaryquantityidentity; thetable'smedian/IQRcaption/header,theGEEfootnoteonlydefiningbetween-groupmeancontrasts,andp15'smean-outcomeprosedonotidentifyauniformrawgroupstatistic; extractingmedian/IQRversusmean/CI oranother fitted/interpolatedsummary changes thequantitytaken. SomeHC3-monthcells,pain2.0(1.0,3.0)andgeneral2.0(1.0,2.0),arecompatiblewithgenuinemedians/quartiles,so immediatecontextdoesnotsupplyoneuniformreplacementsummaryfor allcells. Modelmeancontrasts are not testedbysubtractingmedians.

**Alternatives/limits:** Fittedmeans/CIscouldexplainfractionalcentersandnarrowparentheses;nonordinaryinterpolation,preprocessed/nonintegerresponses ormixedsummaries arepossiblebutnotdefined. Remainingfractionalcenters2.9,2.1,1.9,1.6,2.6have gaprelative≤.05andarenotindependentlyqualifyingnumericcells;donotaddthemasdistinctcomponents. Humanquestion: Whichrawgroupstatistic/limits andpreprocessingapplytothefivenamedcells? This isnotaraw-dataaudit oraclaimaboutactualunprintedmedians.

## G017 — All-observed depression workbook percentage

**Finding IDs:** F-NUM-002,F-ST1-106. **Qualifying route:** Route A, category3. **Classification:** statistical_results; S_W; all S_W; REPORT workbookonedisplay. Ambiguity:noneintheprinteddenominatorrule;unprintedsubsetexplanationsremainalternatives.

**All exact source cells:** [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx),eTable3!A82,E82,E2,E3,E83,A110,comparatorB82:D82,B83:D83,B3:D3. ExactXMLdecoderindependentlyconfirmsE82“711(73.2)”,E3“(N=1568)”,E83numeric2;A110:“Missing isreported asn butexcludedfromthedenominatorinthe%reported.” E2“AllObserved”;A82currentdepressionPHQ-8≥10.

**Calculation:** Documenteddenominator1568−2=1566;100×711/1566=45.402299%. Conservativebandsnumerator[710.5,711.5],population[1567.5,1568.5],missing[1.5,2.5] give denominator[1565,1567] andpercentage[45.341417,45.463259]. Printed73.2±.05 gives[73.15,73.25],gap27.686741,relative.3782342. Ignoringmissingnessstillgives45.3444%. Same-rowcomparatorsB1116(47.9)withN2331missing2,C162(54.9)withN295missing0,D243(51.9)withN468missing0reconcile;162+243+711=1116.

**Inclusion/impact/alternatives:** A3 applieswithina baselineworksheetdisplay,notaperipheralcopycomparison. Namedextraction:currentdepressionprevalenceinparticipantswithallprimaryfollow-upsobserved. Unprinteddenominatornear971wouldproduce73.2,butno suchsubsetisidentified. Humanquestion: Whichcount/denominator/percentagecorrespondtotheAllObserveddepressionentry? Do not infera provenance explanation orreplacementvalue.

## Registration order, complete component closure and limits

Use specific positive anchors, with DOC-001 preceding DOC-002/DOC-003, then DOC-005/DOC-006: G001(main1 abstract);G002(main3 duration);G003(main4 MissingData);G004(main4 primaryadjustment);G005(main4 secondaryadjustment);G006(main4 adherence);G008(main8 Discussion);G009(main9 NNTconfidence);G010(main9 NNTpoints);G011(main10 SMDintervals);G012(main10 SMDpoints);G007(protocol57 operativeprimarymoderatorplan, continued58 andSAP21–23);G013(results7 finaleducation);G014(results7 finalweights);G015(results8 firstmodelinterval/Pconflict);G016(results17 rawmedianheader);G017(workbookE82). G007 is anabsencefinding andisanchored tofirstoperativepositivePLANdefinition,not to aninventedREPORTabsencepage. Withinmain4,coordinatormayapplyphysicalreadingordertoitsdifferentparagraphanchorswithoutalteringthegroupmembership.

All26findingcomponentsandallcitedlocationshavebeenreread; nofindingwasremovedbyacounttarget. NoassignedCIDs,evidencestatesorinclusionauditdecisionsare supplied. Futuremechanicalrecheck must confirmclassification,includingG003P_Pcontext,G010S_CpatternclassificationandG016S_Wcorroborationreading. Individualdata,unroundedrisks/bounds,numericalUCSDs,modelcovariancesandprospectivespecificationsoutsidepackagearenot supplied. Theabsencegroupisonlyabounded supplied-packagecomparison. These limitsdo not create a scientificcoveragegap in this screening scope.
