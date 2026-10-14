# Workflow 1.6.2 Mechanical Evidence Recheck

Pending Human Adjudication. Three fresh distinct high-effort specialists cover disjoint stable candidate scopes; source pages remain authoritative. All parts are merged without loss, changing only relative source-link depth.

# Mechanical source recheck: C001–C007

Pending Human Adjudication. Fresh runtime ID: 01a12c63-86c3-78d0-84d8-ccea451f5769; model gpt-6.1-sol; reasoning effort high. Scope: C001, C002, C003, C004, C005, C006, C007. All seven assigned IDs were rechecked independently against the supplied PDFs, not derivative text.

Direct-source confirmation used 26 unique source-page images freshly rendered by bundled `pdf_tools.py`, PyMuPDF 1.26.4, CPU, 150 dpi. Paths are `preprocessing/recheck001-DOC-001-pN.png` for N=1,2,3,4,6; `preprocessing/recheck001-DOC-002-pN.png` for N=8,11,16,28,47,49,53,66,77,80,84,91,92,101,103,104,109; and `preprocessing/recheck001-DOC-003-pN.png` for N=3,11,13,14. These paths are relative to the review root. No fresh OCR was necessary. All quoted quantities and statements below were visually matched to these exact source pages. DOC-001 is trial-report content; DOC-002 cited protocol, SAP and prospective SMS-log passages are PLAN content; DOC-003 cited result tables are REPORT content. No source or reused artifact was modified.

## C001 — Protocol SMS totals and frequency schedules do not reconcile

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.16,53 and SAP p.80 vs REPORT DOC-001 pp.1,3

**Evidence state:** reproduced

**Finding IDs:** F-NUM-104, F-XS-005

**Location found; source and comparator matched:** Every cited location was found. REPORT [DOC-001 p.1](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>) states daily messages for two months, then monthly for four; [p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) specifies 134 unique messages: 100 in month 1, 30 in month 2, four thereafter. PLAN [DOC-002 p.16](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=16>), lines386–390, prints each participant receiving 178 over six months, first two months 4–5/day, next two 2–3/day, final two 1–2/week. PLAN [p.53](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=53>), lines1526–1530, prints 134, first two months 4–5/day, next two 1–2/day, last two 1/week. PLAN SAP [p.80](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=80>), lines2532–2536, prints 134: month1 3–4/day, month2 1/day, final four months 1/month. PLAN [p.77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>) change note was found; it lists sample-size, outcome and operational changes but does not supply a schedule crosswalk. Adjacent pp.16,53,80 permit pilot refinement.

**Rule; comparison and display precision reproduced:** Treat the paired statements as per-participant transmission schedules, as printed. Using nominal 28-day months, minima are 56×4+56×2+56/7=344 and 56×4+56×1+56/7=288. A deliberately wider rounding enclosure allows each two-month duration [1.5,2.5] months, days/month [28,31], and each displayed frequency endpoint ±0.5. For p.16, enclosure is [1.5×28×3.5+1.5×28×1.5+1.5×28×0.5/7, 2.5×31×5.5+2.5×31×3.5+2.5×31×2.5/7]=[213,725.178571]. Against 178±0.5, gap34.5 and relative34.5/178=0.193820. For p.53 the analogous enclosure is [171,636.607143]; against134±0.5, gap36.5 and relative36.5/134=0.272388. Both exceed0.05. Month2 protocol lower4/day versus report1/day gives rounded gap3.5−1.5=2/day, relative2/1=2. The report's100+30+4=134 reconciles; 178-versus134 alone is not the basis.

**Inputs available; exact missing inputs:** All printed totals, phase lengths and frequencies are available. Actual per-person transmission logs, whether counts denote unique templates rather than transmissions, and the implemented pilot-revision crosswalk are absent.

**Alternative; observation versus inference:** Different branches or unique templates could explain a total unlike repeated transmissions; pilot refinement could explain the SAP/report schedule. These are explanations, not observed definitions in the affected paragraphs. Direct observation is the printed per-participant total/schedule mismatch and protocol-report month2 schedule difference; actual dose received is not inferred.

**Classification rationale:** Confirmed unchanged. Protocol-to-SAP conflicts give P_P, protocol-to-report dose conflict gives P_R, which takes precedence. The agreeing abstract/SAP are corroboration.

**Classification ambiguity:** Bundle order alone does not establish version chronology; unique templates versus actual transmissions remains undefined.

**Determining recheck fact:** Both within-paragraph totals remain below conservative rounded schedule minima, and the month2 protocol/report schedules remain separated.

**Exact remaining human question:** What per-participant totals and phase-specific transmission schedules governed Phase3, and how do the protocol's178/134 totals map to the SAP/report134-message schedule?

## C002 — Operational eligibility criteria differ from the plan list

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.11,49 vs REPORT DOC-001 pp.2,4 and DOC-003 p.3

**Evidence state:** reproduced

**Finding IDs:** F-XS-008

**Location found; source and comparator matched:** Every cited location was found. PLAN [DOC-002 p.11](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=11>), lines235–255, and [p.49](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=49>), lines1375–1395, contain complete participant lists: daily smoking OR stopping/reducing below daily only since diagnosis, and personal-mobile access; neither lists a ≥25-day or SMS-reader criterion. REPORT [DOC-001 p.2](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2>) defines daily smoking as at least one puff on ≥25 days in the last month. [p.4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) Figure1 prints236 unable to read with nobody at home able to read SMS; REPORT [DOC-003 p.3](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=3>) eTable1 prints the corresponding236 and7069 not smoking at least25 days in the past month.

**Rule; comparison and display precision reproduced:** Item-match finite eligibility lists. Recent reduction is explicitly permitted in the plan; the report's retrospective ≥25-day condition and operational reader exclusion have no matching planned term. This is a population-selection specification comparison; no percentage recomputation or unique added-exclusion count is asserted, so display-precision arithmetic does not apply. Figure1 expressly allows multiple exclusion reasons.

**Inputs available; exact missing inputs:** Printed criteria and reason counts are available. Individual criterion overlap, the number uniquely excluded by each changed rule, and any implementing amendment are absent.

**Alternative; observation versus inference:** Some recently reduced smokers could still meet25 days, and an amendment could explain the reader rule. The actual eligibility-list difference is observed; how many participants it changed is not inferred.

**Classification rationale:** Confirmed unchanged: prospective participant rules are PLAN, actual selection descriptions/results are REPORT; P_R/protocol_report concerns the primary population. The two report displays corroborate the operational side and do not add S_C.

**Classification ambiguity:** Overlapping exclusion reasons prevent inferring a unique changed-population count; a later operational amendment is not identified.

**Determining recheck fact:** The complete planned lists retain the recent-stop/reduction exception and lack the reported recent-smoking and SMS-reader criteria.

**Exact remaining human question:** Were recent-stop/reduction smokers eligible as planned, and where were the ≥25-day and patient/household SMS-reader criteria prespecified or amended?

## C003 — Prospective quit-date and reminder calendar differ from the report

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SMS log pp.101,103,104,109 vs REPORT DOC-001 p.3

**Evidence state:** reproduced

**Finding IDs:** F-XS-006

**Location found; source and comparator matched:** Every cited location was found. REPORT [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) sets quitdate5 days after enrollment and four reminders, one/month in months3–6. PLAN prospective [DOC-002 p.101](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=101>) labels enrollment Q(−8)/Tx(+1); footnotes define Q as days to quitdate and Tx(+1) as first treatment day; message6 atQ(−7) says seven days from today. [p.103](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=103>) labels Q(−1)/Tx(+8) and message38 quitting tomorrow. [p.104](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=104>) labels QUIT DATE the8th day since joining; messages39–44 are quit-day messages. [p.109](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=109>) ends daily messages129–131 atQ(+41)/Tx(+50), then reminder132Q(+52)/Tx(+61),133Q(+112)/Tx(+121),134Q(+180)/Tx(+189), naming treatmentmonths2,4,6.

**Rule; comparison and display precision reproduced:** Printed Q(−8) versus5 days gives intervals[7.5,8.5] and[4.5,5.5], gap2, relative2/5=.40. An inclusive8th-day reading gives7 elapsed days: [6.5,7.5] versus[4.5,5.5], gap1, relative1/5=.20. Both exceed.05. Three versus four reminder counts alone has touching half-unit intervals and is not an independent qualifying discrepancy. Dated treatmentmonths2,4,6 differ from monthly reminders acrossmonths3–6.

**Inputs available; exact missing inputs:** Log timing labels, footnote definitions and report schedule are available. Delivered-log revision, enrollment/joining/treatment clock crosswalk and operational quit-date choice are absent.

**Alternative; observation versus inference:** Inclusive counting and pilot refinement remain possible; enrollment and treatment may not coincide operationally. Printed anchors/calendar differ directly; no actual participant quitdate or implemented dose is inferred.

**Classification rationale:** Confirmed unchanged: prospective SMS instructions are PLAN; report's primary start and delivered intervention description are REPORT; P_R/protocol_report.

**Classification ambiguity:** The ordinal quit-day label and distinct enrollment/joining/treatment clocks require a crosswalk; no silent elapsed-day normalization is made.

**Determining recheck fact:** The footnoted Q(−8) enrollment anchor and ordinal label cannot be matched to the reported5-day anchor by ordinary half-unit precision; no explicit clock crosswalk is printed.

**Exact remaining human question:** How do5 days after enrollment and Q(−8)/8th day since joining map, and which reminder-calendar revision was delivered?

## C004 — Primary cotinine verification lacks a planned-to-reported criterion crosswalk

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.8,47,84 vs REPORT DOC-001 p.3

**Evidence state:** reproduced

**Finding IDs:** F-XS-007

**Location found; source and comparator matched:** Every cited location was found. PLAN [DOC-002 p.8](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=8>), lines158–161, and [p.47](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1298–1301, name Accutest NicAlert strips, graded0–6, level<3, described as100–200ng/mL. PLAN SAP [p.84](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2661–2665, repeats graded0–6 andlevel<3. REPORT [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) names Hangzhou AllTest rapid-test cassette; a negative result verifies abstinence for concomitant baseline smokeless-tobacco use.

**Rule; comparison and display precision reproduced:** Match primary endpoint decision specifications: gradedlevel<3 on the planned strip versus binarynegative on the named different cassette. The procedures are expressly different, with no decision-threshold crosswalk. No numerical threshold discrepancy can be calculated because the cassette cutoff is not printed; half-unit precision is therefore inapplicable, not evidence of a threshold change.

**Inputs available; exact missing inputs:** Named procedures and decision outputs are available; cassette concentration cutoff, grade-to-binary mapping and any assay amendment are absent.

**Alternative; observation versus inference:** The binarynegative result could implement the planned threshold exactly. Direct observation is the unlinked printed primary classification specifications; concentration inequivalence and changed participant status are not inferred.

**Classification rationale:** Confirmed unchanged: protocol/SAP endpoint criteria are PLAN and implemented endpoint description REPORT; P_R/protocol_report. Repeated plan passages corroborate one specification without a P_P conflict.

**Classification ambiguity:** Equivalent classification by the two assays remains possible; no concentration-change conclusion is made.

**Determining recheck fact:** The report uses a differently named assay/output without stating how its negative result implements the planned graded criterion.

**Exact remaining human question:** What concentration criterion defined a negative AllTest cassette result, and how did it implement planned NicAlertlevel<3?

## C005 — Primary model changes from protocol Poisson/log link to SAP/report logistic

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP pp.91,92 and REPORT DOC-001 p.3

**Evidence state:** reproduced

**Finding IDs:** F-XS-001, F-ST1-003

**Location found; source and comparator matched:** Every cited location was found. PLAN [DOC-002 p.28](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764, and [p.66](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2011–2016, state generalized linear mixed models, log link, underlying Poisson distribution, cluster random intercept and crude/adjustedRRs with95%CIs. PLAN SAP [p.91](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2884–2889, states mixed-effects logistic regression for the primary result, site random effect andRR; [p.92](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926, also names logistic. REPORT [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) states logistic regression within the mixed-effects framework for categorical outcomes. PLAN [DOC-002 p.77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>) change note gives other amendments but no model replacement.

**Rule; comparison and display precision reproduced:** Compare the named primary model families/links: log mean=η differs from logit probability=η. The adjacent preceding economic-analysis text does not alter the separately headed statistical-analysis paragraph, which expressly estimatesRRs. Both protocol occurrences conflict with the SAP/report model. Numeric rounding does not apply to model-family statements. Route A category5 is applicable to the planned primary analysis replacement/nonreporting.

**Inputs available; exact missing inputs:** Model-family text, random-effect statements and primary-analysis attribution are available. Final fitted code, protocol/SAP hierarchy, model replacement disclosure and result-to-model mapping are absent.

**Alternative; observation versus inference:** The SAP may supersede protocol; logistic wording could describe a separate computation. These are unconfirmed explanations. Direct observation is distinct named families for the primary analysis, not which was actually fitted. Header V6 on the first protocol component prevents assuming chronology from bundle order.

**Classification rationale:** Confirmed unchanged: protocol-to-report conflict P_R, protocol-to-SAP conflict P_P; P_R takes precedence and gives protocol_report. SAP/report agreement does not eliminate the conflicting protocol specification.

**Classification ambiguity:** Which plan specification superseded the other, and which family generated the reported results, are not established by component order.

**Determining recheck fact:** Both protocol model paragraphs retain Poisson/log-link while SAP/report print logistic for the primary categorical analysis.

**Exact remaining human question:** Which family/link generated primaryRRs/CIs, and where is the protocol-model replacement or separate-analysis mapping documented?

## C006 — Risk-ratio derivation from stated logistic analysis is unclear

Pending Human Adjudication.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.3 method vs REPORT DOC-001 p.6 RR labels; REPORT DOC-003 pp.11,13,14 affected displays

**Evidence state:** reproduced

**Finding IDs:** F-ST1-002

**Location found; source and comparator matched:** Every cited location was found. REPORT [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) names mixed-effects logistic regression for categorical outcomes. REPORT [p.6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 prints primaryRR3.0[2.0,4.9], adjustedRR3.2[2.2,5.2], and RR labels for remaining fitted categorical rows; notea names mixed-effects models forRR. REPORT [DOC-003 p.11](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=11>) eTable7 ends with a relative-risk95%CI row; [p.13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>) eTable9 prints crude/adjustedRR columns including primary2.9[1.8,6.4]/3.1[1.9,6.5]; [p.14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) notee names mixed-effectsRR models, without a risk-conversion rule.

**Rule; comparison and display precision reproduced:** In a logit model, exp(treatment coefficient) is an odds ratio. Obtaining anRR requires a prediction/standardization/conversion step or another link. The report names no such step for these risk-based outputs. This source-grounded method-to-measure chain is incomplete. No printedOR-versusRR numerical discrepancy or crude-versusmodeled comparison is asserted; half-unit arithmetic cannot identify an absent estimand-producing operation.

**Inputs available; exact missing inputs:** Model-family statement, risk labels and printed results are available. Fitted link per result, transformation/prediction formula, averaging distribution, conditional-versusmarginal estimand and correspondingCI procedure are absent.

**Alternative; observation versus inference:** Marginal predicted risks could produce coherentRRs, or a log-link fit could underlie the displays. The missing specified bridge is observed; the claim that anOR was printed asRR is not made.

**Classification rationale:** Confirmed unchanged: main method-to-measure gap is within one REPORT, S_W/statistical_results. Supplement risk labels extend affected displays but do not conflict with the main RR label, so no S_C. A corroborating plan is not a relationship; C005 separately covers model replacement.

**Classification ambiguity:** The actual prediction/transformation producing the risk-based estimand is unavailable; no odds-ratio mislabeling conclusion is made.

**Determining recheck fact:** The logistic statement and RR result labels are present, but no operation connecting them is stated in the cited methods/notes.

**Exact remaining human question:** What prediction, standardization, conversion or fitted-link rule produced the printedRRs andCIs from the logistic mixed-effects analysis?

## C007 — Planned tobacco-use-form adjustment has no reported primary counterpart

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP p.92 vs REPORT DOC-001 pp.3,4,6 and DOC-003 p.14

**Evidence state:** reproduced

**Finding IDs:** F-XS-003, F-ST1-005

**Location found; source and comparator matched:** Every cited location was found. PLAN [DOC-002 p.92](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926, specifies fully adjusted models controlled for sociodemographic variables alongside tobacco-use form and other baseline characteristics. REPORT [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) gives post hoc fixed effects age, sex, education, occupation and smoking duration. REPORT [p.4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) adjusted-primary paragraph repeats those five andRR3.2[2.2,5.2]; [p.6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 notea gives the same five. REPORT [DOC-003 p.14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) eTable9 notee repeats those five for death-excluded adjusted results. All four affected reported descriptions were matched.

**Rule; comparison and display precision reproduced:** Item-match the planned tobacco-use-form term against finite repeatedly reported adjustment lists. No corresponding term/result for that planned fully adjusted model is supplied. Route A category5 applies to a planned primary analysis not reported/replaced. Covariate-set comparison has no rounding interval.

**Inputs available; exact missing inputs:** Planned covariate and reported lists are available. Actual model matrix/formula, any alias for tobacco form, the planned-model result and documented replacement are absent.

**Alternative; observation versus inference:** Tobacco form could be fitted but omitted from descriptions, combined into another term or intentionally omitted after an amendment. The repeatedly absent reported term is observed; its actual exclusion from fitted code is not inferred.

**Classification rationale:** Confirmed unchanged: SAP model specification is PLAN and finite reported adjustment lists are REPORT; P_R/protocol_report. Report passages agree and provide no separate S_C/S_W conflict.

**Classification ambiguity:** A description omission and a fitted-model change remain distinguishable only with the model formula/result mapping.

**Determining recheck fact:** Tobacco-use form is expressly planned yet lacks a counterpart in every cited reported primary/adjusted-model list.

**Exact remaining human question:** Was tobacco-use form included, and where is the planned fully adjusted primary result or its documented replacement?

All seven IDs retain their original classification; all seven evidence states are `reproduced`. Remaining questions concern operational amendments/logs, assay equivalence and fitted analysis definitions, not unreadable cited locations. No candidate was deleted or given a disposition.

# Evidence recheck: C008, C009, C010, C011, C012, C013

Pending Human Adjudication. Runtime ID: 01a12c63-aaf3-7ea2-b202-3ccc33a45f88. Exact-source page images were visually read; normalized text only located the report-wide gender search. Twenty-three unique pages were inspected, below the 32-image bound. Current-run renders were produced directly from supplied PDFs with bundled pdf_tools.py/PyMuPDF 1.26.4 on CPU: cross_main_{3,4,5,8}.png; st1-main-006.png; cross_plan_{28,48,62,63,66,77,83,84,91,92,93}.png; numeric_support_plan_p64.png; cross_supp_{6,12}.png; numeric_support_p013.png. Three additional CPU renders at 160 dpi are preprocessing/recheck002_main_001.png, recheck002_plan_099.png, and recheck002_supp_015.png. Existing text/OCR was not final authority. No new OCR was required; the recorded GPU_USER_REQUESTED device authorization remains applicable to OCR.

## C008 — CO<6 rows in primary-outcome blocks

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** PLAN DOC-002 p.84 primary definition vs REPORT DOC-001 p.6 and DOC-003 p.13 primary blocks; REPORT DOC-001 p.3 sensitivity statement

**Evidence state:** reproduced_after_transcription_correction

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-ST1-008

**Location found; source and comparator matched:** All four cited locations were found. [DOC-002 p.84](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2654–2660, defines the primary endpoint as six-month continuous abstinence verified by CO<10 ppm. [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) explicitly identifies CO<6 ppm as a post hoc sensitivity of the primary outcome. [DOC-001 p.6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2, places both CO<6 rows in the Primary outcome block: ITT 264/720 versus38/360, RR3.7 [2.4,5.8]; PP264/667 versus39/318, RR3.6 [2.14,6.87]. [DOC-003 p.13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9, is explicitly titled Post-hoc sensitivity analysis (intention to treat) after excluding deaths, but its Primary outcomes block also contains CO<6:264/695 versus38/333, crudeRR3.6 [2.4,5.4], adjustedRR3.8 [2.4,6.2]. Every affected CO<6 row at the cited displays was confirmed.

**Rule and logical comparison reproduced:** A planned primary threshold and an explicitly post hoc sensitivity threshold receive the same printed primary-block status in the two displays. No numeric rounding or half-unit comparison applies to this categorical status observation. This record confirms the printed grouping; it does not infer that investigators actually promoted the sensitivity to a prespecified primary endpoint.

**Necessary inputs available; missing definitions:** Threshold definitions, table titles, and block headings are available. The missing input is the intended status convention of the primary blocks: formal endpoint hierarchy versus grouping all analyses of the primary construct.

**Alternative interpretation; direct versus inferred:** The explicit post-hoc eTable9 title and main sensitivity sentence support grouping by primary construct. A changed outcome hierarchy is an inferred interpretation, not directly observed. The direct observation is the competing primary-block and sensitivity descriptions relevant to status extraction.

**Classification rationale:** PLAN and REPORT status descriptions give P_R; main narrative versus results supplement gives S_C; main narrative versus its own Table2 gives S_W. P_R takes precedence. The registration described main p.6 as a sensitivity-definition location; visual reading instead shows a primary block, so that location description is corrected and S_W added. Printed values themselves are unchanged. This transcription/context correction determines reproduced_after_transcription_correction.

**Classification ambiguity:** The primary-construct grouping convention may reconcile the hierarchy; no supplied statement defines that convention. This evidence fact remains distinct from inclusion adjudication.

**Exact remaining human question:** Do all three CO<6 rows retain post hoc sensitivity status despite placement in primary blocks, and what outcome-status metadata should accompany their estimates?

## C009 — Missing-outcome architecture

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP p.91 and REPORT DOC-001 pp.3,4

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-002, F-ST1-004

**Location found; source and comparator matched:** [DOC-002 p.28](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764, and [p.66](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2011–2016, separately headed Statistical analysis, both state that outcomes will primarily be analyzed in a missing-at-random architecture. Both follow economic complete-case/imputation paragraphs but say Outcomes without an economic restriction. [SAP p.91](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2890–2892, explicitly identifies primary ITT and regards dropout/incomplete data as continuing smokers. [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) treats missing primary outcomes as negative/not abstinent and separately discards missing outcomes for complete-case analysis. [DOC-001 p.4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1, confirms missing53 and42, including deaths25 and27, and primary analysis totals720 and360.

**Rule and comparison reproduced:** Both protocol occurrences name MAR, whereas SAP/report explicitly assign all missing primary outcomes smoking status. The supplied passages do not map these to one combined primary analysis or restrict MAR to another outcome. Deterministic classification and MAR may coexist in different analyses, but that mapping is missing. Arithmetic53+42=95 and720+360=1080 reconciles; no count discrepancy is asserted. Half-unit/display precision does not apply to the missingness-architecture contrast.

**Necessary inputs available; missing definitions:** Printed handling statements and retained denominators are available; outcome-specific MAR applicability, the imputation model/variables, and an explicit replacement/amendment hierarchy are absent.

**Alternative interpretation; direct versus inferred:** Economic context could limit MAR to costs/QALYs, or SAP could replace the broader protocol. The separately headed Outcomes statement is directly observed; applicability to the reported primary ITT beyond its broad wording, and replacement chronology, are inferred possibilities. No bias or alternative efficacy estimate is inferred.

**Classification rationale:** All protocol/SAP passages are prospective PLAN; article methods/flow are REPORT. Protocol–report yields P_R; protocol–SAP yields P_P. Precedence/domain are confirmed without correction.

**Classification ambiguity:** Adjacent economic material is a material contextual alternative but does not expressly delimit the separately headed paragraph.

**Exact remaining human question:** Which outcomes/analyses use MAR, and how do those analyses relate to the smoking-status imputation for the primary ITT?

## C010 — Gender-specific primary analyses

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP pp.92,93,99 vs REPORT DOC-001 pp.3,5 and DOC-003 p.12

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-004, F-ST1-006

**Location found; source and comparator matched:** [SAP p.92](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2936–2939, specifies subgroup sensitivity analyses of primary treatment-effect stability. [p.93](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=93>), lines2940–2952, includes gender male/female, separate mixed-effects subgroup models, RR/95%CI, and disclosure of missing CIs. [p.99](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=99>) contains blank Gender Male/Female table-shell rows. [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) lists prespecified age, education, employment, and smoking-duration subgroups; [p.5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>) narrative adds reading SMS but reports no gender effect; its baseline table shows male698/720 and345/360, female22 and15. The complete [DOC-003 p.12](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>), eTable8, contains All, Age, Education, Occupation, Smoking Duration, Reading SMS, and no gender rows.

**Rule and comparison reproduced:** The prespecified primary-effect gender analysis has no result or missing-CI disclosure at its matched complete report displays. Source-text searches across main/report supplement locate gender only as baseline/context, not treatment-effect results. The blank shell is a prospective PLAN, not a report with absent cell values. Categorical planned-versus-reported analysis matching, Route A category5, applies; half-unit arithmetic does not address absent analyses.

**Necessary inputs available; missing definitions:** Plan models and complete reported subgroup categories are available. Male/female RR/CI outputs, sex-specific abstinence counts/model estimability, and a reason for omission/removal are absent.

**Alternative interpretation; direct versus inferred:** Sparse female enrollment is directly reported; inability to estimate gender-specific models, completed-but-omitted analysis, or an amendment are possible explanations, not observed facts. The SAP explicitly anticipates missing-CI disclosure.

**Classification rationale:** Prospective SAP versus report subgroup methods/results gives P_R/protocol_report. Main and supplement lists agree in lacking gender; they do not create S_C. No correction.

**Classification ambiguity:** Absence is bounded to the complete supplied report package, not proof that the analysis was never performed.

**Exact remaining human question:** Where are the planned male/female primary RR/CI results, or the disclosed explanation for nonestimation, omission, or removal?

## C011 — Ten versus twenty percent attrition inputs

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.48,62 vs PLAN DOC-002 pp.63,64,83 and REPORT DOC-001 p.3; PLAN DOC-002 p.77 amendment context

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-010, F-ST1-010

**Location found; source and comparator matched:** [DOC-002 p.48](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1344–1347, combined study total2716 assumes10% do not provide primary data. [p.62](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=62>), lines1861–1863, repeats2716 and10%. [p.63](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1894–1898, Phase3 assumes20% and prints587+(587×0.2)=704. [p.64](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>), lines1936–1938, Phase4 likewise uses20%,864+(864×0.2)=1036. [SAP p.83](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2624–2638, combined overview and Phase3 both use20%; Phase3 proceeds to1080. [DOC-001 p.3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) also says anticipated20% attrition in the1080-participant calculation. [DOC-002 p.77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2416–2424, discloses sample-size revisions from888 to1080 for Phase3 and1480 to1620 for Phase4, without explicitly reconciling attrition percentages.

**Rule and calculation reproduced:** Same primary-data attrition input is10% in combined-plan overview/introduction and20% in both phase calculations, SAP overview, and report. Printed integer-percent intervals[9.5,10.5] and[19.5,20.5] have gap9 percentage points; relative discrepancy9/10=0.90>0.05. The registered additive inflation convention is stated and is not independently challenged.

**Necessary inputs available; missing definitions:** Percentages, phase labels, additive formula and amendment summary are available. A dated applicable-input hierarchy or explanation distinguishing combined-study missingness from phase-specific attrition is absent.

**Alternative interpretation; direct versus inferred:** Ten percent could be a retained overview input or a combined-study assumption different from phase attrition. Printed10/20 passages are direct observations; obsolescence or differing definitions are inferred explanations. Phase4 is context supporting the combined-study comparison, not a reported efficacy result.

**Classification rationale:** Conflicting protocol–SAP/detail assumptions give P_P;10% protocol versus20% report gives P_R, which takes precedence. All supplied specifications are PLAN by prospective content; article sample-size explanation is REPORT. No substantive classification correction.

**Classification ambiguity:** The10% wording covers the combined study, while the report concerns Phase3; both phase calculations and SAP combined overview use20%, so no supplied phase distinction expressly reconciles the input.

**Exact remaining human question:** Which attrition assumption governed Phase3, and does the combined-study10% statement denote a distinct definition or a superseded input?

## C012 — Cause attribution of the 4.8% mortality value

Pending Human Adjudication.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 p.8 discussion vs REPORT DOC-001 pp.1,4,5,6 and DOC-003 p.6

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-001, F-XS-012

**Location found; source and comparator matched:** [DOC-001 p.8](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8>) explicitly attributes4.8% within six months to deaths of TB. [p.5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>) specifies TB as61.5% [32/52] of deaths. [DOC-003 p.6](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4, confirms52 total,25/27 by arm,32 TB deaths,16/16 by arm, and20 deaths across other causes. [DOC-001 p.1](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>) confirms1080 randomized; [p.4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) Figure1 confirms720/360, deaths25/27; [p.6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 Death confirms25/720 and27/360. Every cited supporting location was visually matched.

**Rule and calculation reproduced:** TB-specific risk32/1080×100=2.962963%; all-cause52/1080×100=4.814815%. Applying the mandated half-unit intervals conservatively even to exact integer counts gives TB range100×[31.5/1080.5,32.5/1079.5]=[2.915317,3.010653]%. Printed4.8 gives[4.75,4.85]%; gap1.739347 and relative gap0.362364>0.05. All-cause range[4.766312,4.863363]% overlaps printed4.8. Thus the same printed percentage reconciles with total deaths but not the labeled cause-specific numerator.

**Necessary inputs available; missing definitions:** Counts, enrollment, time horizon and cause table are available. No alternate TB-attributable cause definition, denominator, or adjudication mapping yielding4.8% is supplied.

**Alternative interpretation; direct versus inferred:** The sentence may mean all-cause mortality among people with TB; that interpretation matches52/1080. The cause-specific words,32 TB deaths and52 total deaths are direct observations. Intended all-cause wording or an alternate cause population is inferred.

**Classification rationale:** Main discussion versus main cause result gives S_W; discussion versus supplementary cause table gives S_C. Both are REPORT by result content; S_C takes precedence. Domain reflects outcome attribution, rather than a separate count discrepancy. No correction.

**Classification ambiguity:** Generic denominator/death counts corroborate the arithmetic; no PLAN relationship is introduced.

**Exact remaining human question:** Is4.8% all-cause mortality among trial participants with TB or TB-attributed mortality, and which numerator/denominator defines the latter?

## C013 — Any-irritability and any-anxiety directions

Pending Human Adjudication.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.5 prevalence pairs vs same-paragraph direction; REPORT DOC-003 p.15 corroborates and supplies severity alternative

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-002, F-XS-013

**Location found; source and comparator matched:** [DOC-001 p.5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), Adverse Events, fixes mHealth/usual-care order, prints irritability40.5%/43.4% and anxiety33.3%/36.8%, then says dry mouth, irritability and anxiety were more common in mHealth. [DOC-003 p.15](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=15>), eTable10, confirms irritability None59.5%/56.6% and anxiety None66.7%/63.2%, whose complements match those any-symptom frequencies. Moderate/severe percentages are irritability11.2+4.3=15.5% versus7.2+1.2=8.4%; anxiety6.9+2.4=9.3% versus3.6+0.3=3.9%. Both repeated affected symptoms were confirmed.

**Rule and calculation reproduced:** Any-symptom mHealth-minus-control differences are−2.9 and−3.5 percentage points. Half-unit ranges are[−3.00,−2.80] and[−3.60,−3.40], strictly lower in mHealth; relative interval gaps2.80/43.4=0.064516 and3.40/36.8=0.092391 both exceed0.05. Printed direction reverses the matched any-symptom reading, Route A category2. Dry mouth62.7%/55.7% agrees and is contextual, not an additional occurrence.

**Necessary inputs available; missing definitions:** Arm order, any-symptom percentages, and severity rows are available. The missing definition is whether more common switches from any symptom to moderate/severe burden.

**Alternative interpretation; direct versus inferred:** Moderate/severe frequencies are directly higher in mHealth in eTable10 and provide a source-grounded alternative. A switch to that severity quantity in the main sentence is inferred because it is not stated.

**Classification rationale:** The conflicting values/direction occur inside one REPORT paragraph, yielding S_W/statistical_results. Supplementary rows corroborate the prevalence and support the severity alternative; they do not conflict with main prevalences and therefore add no S_C. No correction.

**Classification ambiguity:** Prevalence and severity are separate quantities; their intended linkage is not specified.

**Exact remaining human question:** Does more common mean any irritability/anxiety or moderate/severe symptoms, and which quantity and direction should be extracted?

# Exact-source evidence recheck: C014, C015, C016, C017, C018, C019

Runtime agent: 01a12c63-ca83-7d51-ad07-f4248a018f40; model gpt-6.1-sol; reasoning effort high; fresh spawn. Every ID remains Pending Human Adjudication. Read QUALITY_CONTROL_SCOPE.md, review_contract.md, settings.toml, tooling_record.md, source_inventory.md and the complete assigned stable ledger part. Confirmed 18 unique source pages visually, within the 32-page bound: DOC-001 pp.1,3,6; DOC-002 pp.9,47,48,63,64,65,77,83,85; DOC-003 pp.6,8,9,12,13,14. Text derivatives were locators only.

Image provenance: existing current-run CPU source renders `preprocessing/st1-main-006.png`, `cross_main_3.png`, `cross_plan_47.png`, `cross_plan_48.png`, `cross_plan_63.png`, `numeric_support_plan_p64.png`, `cross_plan_65.png`, `cross_plan_77.png`, `cross_plan_83.png`, `cross_plan_85.png`, `numeric_support_p006.png`, `cross_supp_8.png`, `numeric_support_p009.png`, `cross_supp_12.png`, `numeric_support_p013.png`; reusable exact-page image `review_1_5_1/preprocessing/DOC-002/page_images/page-009.jpg`. Two new CPU renders use recorded fallback PyMuPDF 1.26.4, 200 dpi: `pdf_tools.py render` DOC-001 --page 1 to `preprocessing/recheck003_main001.png`, and DOC-003 --page 14 to `preprocessing/recheck003_supp014.png`. No OCR was needed; recorded GPU_USER_REQUESTED applies to OCR, while rendering remains CPU. No source or reusable artifact was modified. Arithmetic below was independently recomputed with direct numerical interval arithmetic.

## C014 — Fourteen interval rows

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes for every affected row in [DOC-001 p.6, Table 2](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), [DOC-003 p.12, eTable 8](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>) and [DOC-003 p.13, eTable 9](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>). [DOC-003 p.14 notes](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) identify RR, covariate adjustment and mixed-effects clustering, but no row-specific interval construction. All are REPORT by displayed trial-results content. Table 2 self-report adjusted upper endpoint is literally `42`, and its lower endpoint is `1.9`; no decimal was silently inserted.

**Consistency rule applicable; calculation reproduced:** Diagnostic log-symmetry reconstruction U*=E²/L. Independent displayed input intervals E±hE and L±hL imply [(E−hE)²/(L+hL),(E+hE)²/(L−hL)]; compare with U±hU. Half-units depend on every printed decimal count, including .5 for literal 42. The table lists all 14 independently reproduced discrepancies; relative gap is gap/|printed U|. Every value exceeds .05. This is the route A category 4 display rule supported by other rows, not a claim that every possible RR interval must be log-symmetric.

| Source display / affected row | Printed E; L; U | Recomputed U* interval | Printed U interval | Gap | Relative gap |
|---|---|---|---|---:|---:|
| Table 2 CO<10 PP adjusted | 3.1; 2.1; 5.2 | [4.326744,4.840244] | [5.15,5.25] | .309756 | .059568 |
| Table 2 CO<6 PP crude | 3.6; 2.14; 6.87 | [5.875291,6.240047] | [6.865,6.875] | .624953 | .090968 |
| Table 2 CO<6 PP adjusted | 3.8; 2.3; 7.7 | [5.984043,6.587778] | [7.65,7.75] | 1.062222 | .137951 |
| Table 2 self-report adjusted | 2.8; 1.9; 42 | [3.878205,4.390541] | [41.5,42.5] | 37.109459 | .883559 |
| eTable 8 All | 2.890; 1.983; 4.709 | [4.209332,4.214371] | [4.7085,4.7095] | .494129 | .104933 |
| eTable 8 age ≥40 | 2.953; 2.048; 5.092 | [4.255434,4.260397] | [5.0915,5.0925] | .831103 | .163217 |
| eTable 8 primary education | 2.638; 1.849; 4.07 | [3.761236,3.766125] | [4.065,4.075] | .298875 | .073434 |
| eTable 8 secondary education | 2.719; 1.348; 4.83 | [5.480343,5.488445] | [4.825,4.835] | .645343 | .133611 |
| eTable 8 active occupation | 2.989; 1.933; 4.885 | [4.619153,4.624637] | [4.8845,4.8855] | .259863 | .053196 |
| eTable 8 dependent/retired | 2.587; 1.329; 3.986 | [5.031954,5.039636] | [3.9855,3.9865] | 1.045454 | .262281 |
| eTable 8 smoking <24 years | 3.511; 1.884; 7.127 | [6.539459,6.546659] | [7.1265,7.1275] | .579841 | .081358 |
| eTable 8 reading SMS No | 2.198; 1.288; 3.299 | [3.747774,3.754099] | [3.2985,3.2995] | .448274 | .135882 |
| eTable 9 CO<10 crude | 2.9; 1.8; 6.4 | [4.390541,4.972857] | [6.35,6.45] | 1.377143 | .215179 |
| eTable 9 CO<10 adjusted | 3.1; 1.9; 6.5 | [4.770513,5.363514] | [6.45,6.55] | 1.086486 | .167152 |

Comparator rows were visually matched and independently recomputed. Table 2 self-report crude 2.7[1.8,4.1], week 9 crude 2.6[1.8,3.9]/adjusted 2.7[1.8,4.3], month 6 crude 2.7[2.0,3.8]/adjusted 2.7[1.9,4.0], and success 1.2[.9,1.6]/1.2[.9,1.5] all have overlapping reconstructed and printed upper-limit intervals. eTable 8 age <40 2.672[1.472,4.857] yields [4.846799,4.853725], relative gap .000571; no formal education 2.880[1.566,5.542] gives [5.293023,5.300083], relative gap .043561; smoking ≥24 2.446[1.550,3.911] gives [3.857124,3.862770], relative gap .012204; reading Yes 2.769[1.743,4.318] gives [4.396095,4.401796], relative gap .017970. These four satisfy the workflow precision tolerance; they are not asserted to have exact overlap. eTable 9 CO<6 3.6[2.4,5.4]/3.8[2.4,6.2], week 9 2.5[1.7,3.6]/2.6[1.7,3.8], month 6 2.58[1.8,3.6]/2.7[1.8,4.0], and success 1.1[.7,1.6]/1.1[.7,1.5] all overlap under the same half-unit rule.

**Necessary inputs available:** Every printed triple and display precision needed for this diagnostic is available. **Exact missing inputs/definitions:** Fitted coefficients/covariance, transformation from model to RR, interval-construction algorithm and any row-specific method switches are absent. No universal Wald construction, confidence-interval/P-value conflict or point-outside-interval issue is inferred.

**Alternative interpretation:** The report describes mixed-effects modeling; nonsymmetric profile, bootstrap or transformed marginal-risk intervals could produce the observed endpoints. Different row procedures could be intended. These are possible explanations, not observed algorithms.

**Direct observation versus inferred explanation:** Directly observed are the printed triples and reproduced differences under a rule fitting other display rows within the workflow tolerance. A decimal slip or production mechanism is unestablished.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.6 Table2 within-display rows and REPORT DOC-003 pp.12,13 respective within-display rows

**Finding IDs:** F-ST1-001

**Classification rationale:** The same pattern is consolidated across displays, without asserting a matched-result conflict between documents. PLAN corroboration is not used. No classification change.

**Classification ambiguity:** Row-specific interval construction is unknown; no universal inferential convention or production mechanism is asserted.

**Evidence state:** reproduced

Determining fact: all 14 printed triples match and all 14 diagnostic interval gaps remain >.05 relatively.

**Exact remaining human question:** Which estimate/interval construction produced each of the 14 rows, and are the printed limits, including literal 42, intended for that construction?

## C015 — Failure definition windows

Pending Human Adjudication.

**Location found; source value/text matched; comparator matched:** Yes. [DOC-002 p.9 lines179–180](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=9>) says month 5 or later and is headed V6.0 07.03.25; [p.47 lines1319–1320](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>) says month 6 or later; [p.77 lines2413–2415](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>) explicitly describes replacing month 5 with month 6 in v6; [SAP p.85 lines2685–2686](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=85>) retains month 5 or later. All four are PLAN by prospective endpoint/amendment content. REPORT impact locations [DOC-001 p.1 abstract](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), [p.3 Trial Outcomes](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) and [p.6 Table 2](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) contain the secondary failure result/pointer; Table 2 prints 1/720 versus 2/360. Abstract prints failure 0.1% versus0.5%; it does not itself print the event counts or define a smear window.

**Rule applicable; comparison reproduced; precision:** Month 5-or-later and month 6-or-later are categorically different endpoint windows; display rounding is inapplicable. The historical amendment explains the v4→v6 change but does not reconcile the retained month-5 SAP definition with the amended month-6 definition. No specific event is inferred to change classification.

**Inputs available/missing:** Competing definitions, explicit amendment and three reported events are available. Final endpoint dictionary, amendment/SAP hierarchy, event smear dates and programme-register classification rules actually used are absent. **Alternative interpretation:** Amended protocol could govern, SAP could govern, or programme records could apply a separately defined rule. **Direct versus inferred:** Contradictory printed windows are direct; participant reclassification or numerical outcome effects are unestablished.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.9,47,77,85; REPORT DOC-001 pp.1,3,6 identifies affected result

**Finding IDs:** F-XS-009, F-ST1-011

**Classification rationale:** REPORT does not supply a competing threshold, so it creates no P_R relationship. No classification change. Specify p.9 as an earlier-positioned component explicitly headed V6.0, rather than imply it is v4.

**Classification ambiguity:** Final protocol/SAP precedence and governing endpoint dictionary are absent; disclosed amendment does not reconcile all retained definitions.

**Evidence state:** reproduced

Determining fact: exact plan month-5 and month-6 windows remain different after reading the amendment.

**Exact remaining human question:** Which supplied plan rule and smear-positive window classified the three reported failures: month 5 or later or month 6 or later?

## C016 — Phase 3 cluster power inputs

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes. PLAN [DOC-002 p.48 lines1348–1350](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>) gives 18 intervention and 9 control clusters, 90% power, 5% level, 18%/8% abstinence; [p.63 lines1886–1907](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>) gives these rates/power and 27 clusters, 18/9 allocation, and1080 participants; [p.65 lines1958–1961](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=65>) retains 16 intervention and8 control with the same rates/power; [p.77 lines2416–2424](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>) explicitly describes increasing Phase3 v4 16/8,888 participants to v6 18/9,1080; [SAP p.83 lines2629–2638](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>) gives27 clusters,2:1,90%/5%,18%/8%,1080. All are PLAN by prospective design/power content. Peripheral PLAN [p.64 Phase4](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>) uses18/18, while the repeated p.65 Phase4 paragraph uses20/20; p.77 amendment describes40→36 Phase4 clusters. This context does not expand the included Phase3 issue.

**Rule applicable; calculation reproduced; precision:** Intervention-arm copies 18±.5 and16±.5 have intervals[17.5,18.5] and[15.5,16.5], gap1, relative1/16=.0625>.05. Control9±.5 and8±.5 touch. Independently rounded arm sums[26,28] and[23,25] have gap1/24=.041667; that sum alone does not qualify. The basis is the intervention-arm input attached to the primary trial power specification.

**Inputs available/missing:** Allocations, rates, significance/power and disclosed amendment are available. A final governing power calculation and an explicit statement that p.65 is historical or a distinct scenario are absent. **Alternative interpretation:** p.65 may retain earlier-version text; both allocations might have been evaluated without being differentiated. The source itself discloses the change, so no undisclosed amendment is asserted. **Direct versus inferred:** Direct is the incompatible repeated current-plan power-input paragraph; its production mechanism is inferred and unestablished.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.48,63,65,77,83; PLAN p.64 peripheral Phase4context

**Finding IDs:** F-XS-011, F-ST1-009

**Classification rationale:** Reported27-cluster trial only corroborates one side and adds no P_R relationship. No classification change.

**Classification ambiguity:** p.65 could preserve historical inputs without saying so. Unreported Phase4 context does not expand the included candidate.

**Evidence state:** reproduced

Determining fact: current supplied plan power paragraphs retain18 versus16 intervention clusters beyond the workflow precision threshold.

**Exact remaining human question:** Which Phase3 allocation/power calculation governs, and is the16/8 paragraph intended solely as historical text?

## C017 — Two cause-of-death percentages

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes: REPORT [DOC-003 p.6 eTable4](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>) prints usual-care Drug user1(7.4%) and Severe pneumonia1(7.4%), usual-care total deaths27, each overall affected count1 and mHealth0. Same-display stroke2(7.4%) and fall1(3.7%) corroborate the27 denominator. All usual-care cause counts sum27.

**Rule applicable; calculation reproduced; precision:** For each affected cell100×1/27=3.703704%. Half-unit input reconstruction100×[.5/27.5,1.5/26.5]=[1.818182,5.660377]%; displayed7.4% permits[7.35,7.45]%, leaving gap1.689623 and relative.228327>.05. Both occurrences are independently confirmed, one repeated pattern under route A category3.

**Inputs available/missing:** Printed count, common death total, percentages and sums are available. No separate cause-specific denominator is defined. **Alternative interpretation:** The7.4% could correspond to two deaths or another denominator, but no such switch is printed; table sums support the displayed one death in each row. **Direct versus inferred:** Count/percentage/denominator mismatch is observed; copying or other production mechanisms are unestablished.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.6 affected cells vs same-table death total

**Finding IDs:** F-NUM-101

**Classification rationale:** Both affected cells and comparator total occur within the same REPORT table; no classification change.

**Classification ambiguity:** None.

**Evidence state:** reproduced

Determining fact: both1(7.4%) cells fail the co-located27-death denominator rule beyond precision.

**Exact remaining human question:** What count, denominator and percentage should be extracted for each of the two usual-care death-cause rows?

## C018 — Site 2008 mortality cell

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes: REPORT [DOC-003 p.9 eTable6](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=9>) prints Control2008 5(7.5). All other death cells follow an N40 percentage rule, e.g. Control2002 3(7.5), Control2004 4(10.0), mHealth2012 5(12.5). REPORT [p.8 eTable5](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=8>) prints site2008 recruitment40/484 and ITT12/40, with observed12/35; denominator35 belongs to observed abstinence contributors, not a defined mortality denominator. eTable6 death counts sum52:27 control and25 mHealth.

**Rule applicable; calculation reproduced; precision:** N40 reproduces other death percentages.100×5/40=12.5%; half-unit input range100×[4.5/40.5,5.5/39.5]=[11.111111,13.924051]% versus[7.45,7.55]%, gap3.561111, relative.474815>.05. N40 is inferred from the same-display reproducing rule and explicitly corroborated by site population elsewhere; it is not printed as an N column in eTable6. Thus route A category4 supports the observation independently of the table-denominator formulation of category3.

**Inputs available/missing:** Death count, percentage, matching other cells and site population are available. A separate mortality denominator or row-specific population definition is absent. **Alternative interpretation:** Three of40 would produce7.5%, whereas five of40 produces12.5%; another denominator requires a definition. Counts/sums corroborate five without assigning a corrected value. **Direct versus inferred:** Printed5(7.5) and other-cell pattern are direct; N40 is supported inference; production mechanism is unestablished.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.9 site2008 vs same-table count/percentage pattern; REPORT DOC-003 p.8 corroborates denominator

**Finding IDs:** F-NUM-102

**Classification rationale:** Both locations are within one REPORT document; no cross-document relationship. No classification change.

**Classification ambiguity:** N40 is inferred from the same-display pattern and corroborated by the printed ITT population; eTable6 does not print a separate denominator column.

**Evidence state:** reproduced

Determining fact: the source cell does not reproduce the N40 rule fitting all other death cells, with relative gap>.05.

**Exact remaining human question:** What mortality count, denominator and percentage governs site2008 in eTable6?

## C019 — Signed treatment-failure contrast

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes: REPORT [DOC-003 p.13 eTable9](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>) prints mHealth1/695,0.1%[0.01,0.8] versus usual-care2/333,0.6%[0.1,2.2], difference0.5[-0.4,1.3]. REPORT [p.14 note b](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) identifies “Absolute difference” without a row-specific reversal. Other rows reproduce mHealth-minus-usual-care:43.2−16.5=26.7;38.0−11.4=26.6;50.8−22.5=28.3;57.5−24.6=32.9;3.2−2.1=1.1; success92.5−92.5=0.

**Rule applicable; calculation reproduced; precision:**100×(1/695−2/333)=−.456716 percentage points. Half-unit count/denominator input range[−.679989,−.233792], versus displayed positive[.45,.55], leaves gap.683792/|.5|=1.367585>.05. Rounded printed arm risks independently imply[−.60,−.40]. Thus the affected row reverses the common display contrast under route A category2. The minus sign inside the printed CI is present; no separate interval-construction issue is inferred.

**Inputs available/missing:** Counts, populations, risks, point difference, interval and other-row contrast are available. An explicit signed-reference definition or unsigned/row-specific contrast switch is absent. **Alternative interpretation:** “Absolute” may mean an unsigned magnitude, or this row could reverse the reference groups; a different model-based contrast could be intended. The common pattern and signed interval are retained rather than assuming a universal meaning of “absolute.” **Direct versus inferred:** Positive printed point difference versus negative common signed contrast is observed; intended reference or mechanism is inferred and unresolved.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.13 treatment-failure cell vs same-display arm risks and common contrast; p.14 defines difference

**Finding IDs:** F-NUM-103

**Classification rationale:** Risks, difference, common contrast and note are within one REPORT document; no classification change.

**Classification ambiguity:** An unsigned magnitude or row-specific reference switch remains an alternative interpretation.

**Evidence state:** reproduced

Determining fact: exact printed positive.5 fails the mHealth-minus-usual-care rule fitting the other rows, beyond display precision.

**Exact remaining human question:** Does the treatment-failure row use mHealth-minus-usual-care, and what signed difference and matching interval should be extracted?

All six IDs have exact-source confirmations and classification checks; no source location remained unreadable. Remaining inputs are the named row-specific statistical definitions, final plan hierarchy/power specification, outcome-event dictionary, and any alternate denominators/reference groups. These limit explanatory reconstruction and remain human questions.

