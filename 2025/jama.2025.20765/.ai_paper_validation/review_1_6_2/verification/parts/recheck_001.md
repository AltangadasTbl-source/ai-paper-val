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

**Location found; source and comparator matched:** Every cited location was found. REPORT [DOC-001 p.1](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>) states daily messages for two months, then monthly for four; [p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) specifies 134 unique messages: 100 in month 1, 30 in month 2, four thereafter. PLAN [DOC-002 p.16](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=16>), lines386–390, prints each participant receiving 178 over six months, first two months 4–5/day, next two 2–3/day, final two 1–2/week. PLAN [p.53](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=53>), lines1526–1530, prints 134, first two months 4–5/day, next two 1–2/day, last two 1/week. PLAN SAP [p.80](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=80>), lines2532–2536, prints 134: month1 3–4/day, month2 1/day, final four months 1/month. PLAN [p.77](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>) change note was found; it lists sample-size, outcome and operational changes but does not supply a schedule crosswalk. Adjacent pp.16,53,80 permit pilot refinement.

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

**Location found; source and comparator matched:** Every cited location was found. PLAN [DOC-002 p.11](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=11>), lines235–255, and [p.49](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=49>), lines1375–1395, contain complete participant lists: daily smoking OR stopping/reducing below daily only since diagnosis, and personal-mobile access; neither lists a ≥25-day or SMS-reader criterion. REPORT [DOC-001 p.2](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2>) defines daily smoking as at least one puff on ≥25 days in the last month. [p.4](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) Figure1 prints236 unable to read with nobody at home able to read SMS; REPORT [DOC-003 p.3](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=3>) eTable1 prints the corresponding236 and7069 not smoking at least25 days in the past month.

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

**Location found; source and comparator matched:** Every cited location was found. REPORT [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) sets quitdate5 days after enrollment and four reminders, one/month in months3–6. PLAN prospective [DOC-002 p.101](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=101>) labels enrollment Q(−8)/Tx(+1); footnotes define Q as days to quitdate and Tx(+1) as first treatment day; message6 atQ(−7) says seven days from today. [p.103](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=103>) labels Q(−1)/Tx(+8) and message38 quitting tomorrow. [p.104](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=104>) labels QUIT DATE the8th day since joining; messages39–44 are quit-day messages. [p.109](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=109>) ends daily messages129–131 atQ(+41)/Tx(+50), then reminder132Q(+52)/Tx(+61),133Q(+112)/Tx(+121),134Q(+180)/Tx(+189), naming treatmentmonths2,4,6.

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

**Location found; source and comparator matched:** Every cited location was found. PLAN [DOC-002 p.8](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=8>), lines158–161, and [p.47](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1298–1301, name Accutest NicAlert strips, graded0–6, level<3, described as100–200ng/mL. PLAN SAP [p.84](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2661–2665, repeats graded0–6 andlevel<3. REPORT [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) names Hangzhou AllTest rapid-test cassette; a negative result verifies abstinence for concomitant baseline smokeless-tobacco use.

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

**Location found; source and comparator matched:** Every cited location was found. PLAN [DOC-002 p.28](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764, and [p.66](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2011–2016, state generalized linear mixed models, log link, underlying Poisson distribution, cluster random intercept and crude/adjustedRRs with95%CIs. PLAN SAP [p.91](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2884–2889, states mixed-effects logistic regression for the primary result, site random effect andRR; [p.92](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926, also names logistic. REPORT [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) states logistic regression within the mixed-effects framework for categorical outcomes. PLAN [DOC-002 p.77](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>) change note gives other amendments but no model replacement.

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

**Location found; source and comparator matched:** Every cited location was found. REPORT [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) names mixed-effects logistic regression for categorical outcomes. REPORT [p.6](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 prints primaryRR3.0[2.0,4.9], adjustedRR3.2[2.2,5.2], and RR labels for remaining fitted categorical rows; notea names mixed-effects models forRR. REPORT [DOC-003 p.11](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=11>) eTable7 ends with a relative-risk95%CI row; [p.13](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>) eTable9 prints crude/adjustedRR columns including primary2.9[1.8,6.4]/3.1[1.9,6.5]; [p.14](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) notee names mixed-effectsRR models, without a risk-conversion rule.

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

**Location found; source and comparator matched:** Every cited location was found. PLAN [DOC-002 p.92](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926, specifies fully adjusted models controlled for sociodemographic variables alongside tobacco-use form and other baseline characteristics. REPORT [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) gives post hoc fixed effects age, sex, education, occupation and smoking duration. REPORT [p.4](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) adjusted-primary paragraph repeats those five andRR3.2[2.2,5.2]; [p.6](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 notea gives the same five. REPORT [DOC-003 p.14](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) eTable9 notee repeats those five for death-excluded adjusted results. All four affected reported descriptions were matched.

**Rule; comparison and display precision reproduced:** Item-match the planned tobacco-use-form term against finite repeatedly reported adjustment lists. No corresponding term/result for that planned fully adjusted model is supplied. Route A category5 applies to a planned primary analysis not reported/replaced. Covariate-set comparison has no rounding interval.

**Inputs available; exact missing inputs:** Planned covariate and reported lists are available. Actual model matrix/formula, any alias for tobacco form, the planned-model result and documented replacement are absent.

**Alternative; observation versus inference:** Tobacco form could be fitted but omitted from descriptions, combined into another term or intentionally omitted after an amendment. The repeatedly absent reported term is observed; its actual exclusion from fitted code is not inferred.

**Classification rationale:** Confirmed unchanged: SAP model specification is PLAN and finite reported adjustment lists are REPORT; P_R/protocol_report. Report passages agree and provide no separate S_C/S_W conflict.

**Classification ambiguity:** A description omission and a fitted-model change remain distinguishable only with the model formula/result mapping.

**Determining recheck fact:** Tobacco-use form is expressly planned yet lacks a counterpart in every cited reported primary/adjusted-model list.

**Exact remaining human question:** Was tobacco-use form included, and where is the planned fully adjusted primary result or its documented replacement?

All seven IDs retain their original classification; all seven evidence states are `reproduced`. Remaining questions concern operational amendments/logs, assay equivalence and fitted analysis definitions, not unreadable cited locations. No candidate was deleted or given a disposition.
