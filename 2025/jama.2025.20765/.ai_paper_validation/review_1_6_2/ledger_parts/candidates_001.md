# Current stable candidate scope

Pending Human Adjudication. Canonical ledger: ../candidate_ledger.md.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.16,53 and SAP p.80 vs REPORT DOC-001 pp.1,3 | reproduced | CONFIRMED | F-NUM-104, F-XS-005 |
| C002 | protocol_report | P_R | P_R | PLAN DOC-002 pp.11,49 vs REPORT DOC-001 pp.2,4 and DOC-003 p.3 | reproduced | CONFIRMED | F-XS-008 |
| C003 | protocol_report | P_R | P_R | PLAN DOC-002 SMS log pp.101,103,104,109 vs REPORT DOC-001 p.3 | reproduced | CONFIRMED | F-XS-006 |
| C004 | protocol_report | P_R | P_R | PLAN DOC-002 pp.8,47,84 vs REPORT DOC-001 p.3 | reproduced | CONFIRMED | F-XS-007 |
| C005 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP pp.91,92 and REPORT DOC-001 p.3 | reproduced | CONFIRMED | F-XS-001, F-ST1-003 |
| C006 | statistical_results | S_W | S_W | REPORT DOC-001 p.3 method vs REPORT DOC-001 p.6 RR labels; REPORT DOC-003 pp.11,13,14 affected displays | reproduced | CONFIRMED | F-ST1-002 |
| C007 | protocol_report | P_R | P_R | PLAN DOC-002 SAP p.92 vs REPORT DOC-001 pp.3,4,6 and DOC-003 p.14 | reproduced | CONFIRMED | F-XS-003, F-ST1-005 |

## C001 — Protocol SMS totals and frequency schedules do not reconcile

Pending Human Adjudication.

**Candidate statement:** Protocol SMS totals and frequency schedules do not reconcile.

**Source-order key:** DOC-001 PDF p. 1.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.16,53 and SAP p.80 vs REPORT DOC-001 pp.1,3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: the randomized intervention's planned message dose/duration is an expressly permitted planned-versus-reported element. B2: each protocol paragraph pairs a per-participant total with a frequency schedule that cannot produce it even under widened half-unit allowances; pilot-refinement permission does not name the governing revised schedule. B3: the extractable intervention schedule attached to the primary six-month abstinence RR3.0 is unresolved. The issue is bounded to printed intervention specifications.

**Finding IDs:** F-NUM-104, F-XS-005

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 1](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), abstract intervention; REPORT.
- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Intervention; REPORT.
- [DOC-002 — PDF p. 16](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=16>), lines386–390, earlier-component dose paragraph; PLAN.
- [DOC-002 — PDF p. 53](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=53>), lines1526–1530, later-component dose paragraph; PLAN.
- [DOC-002 — PDF p. 77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), change note; PLAN.
- [DOC-002 — PDF p. 80](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=80>), lines2532–2536, SAP dose; PLAN.

**Source evidence:** The earlier-component paragraph says each participant receives 178 SMS over six months: first two months 4–5/day, next two months 2–3/day, final two months 1–2/week. The later-component paragraph says 134 SMS: first two months 4–5/day, next two months 1–2/day, final two months 1/week. SAP says 134 over six months, 3–4/day in month1, 1/day in month2, then 1/month for months3–6. The report says 100 in month1,30 in month2,and4 monthly thereafter,134 total.

**Calculation:** Nominal conservative 28-day-month minima are344 and288, respectively. Allow every two-month duration [1.5,2.5] months, every frequency endpoint ±0.5, and calendar months28–31days: earlier enclosure [213,725.178572], later [171,636.607143]; totals178±0.5 and134±0.5 yield gaps34.5/178=.193820 and36.5/134=.272388. For month2, later-protocol lower4/day±.5 and report1/day±.5 yield gap2/day,relative2.0. The categorical duration/frequency schedules also differ. The amendment between178 and134 totals is context, not an independent finding.

**Affected result or extracted value:** Planned per-participant intervention dose and the delivered schedule attached to the primary abstinence RR3.0[2.0,4.9].

**Why context does not resolve it:** The same protocol paragraphs state per-participant receipts and transmission schedules; immediate pilot-refinement permission does not identify which quantitative schedule governs or reconcile the internal totals. This is intervention dose in the permitted cross-comparison tier, not general intervention critique.

**Alternative source-grounded interpretations:** Totals could denote unique templates/branches rather than actual transmissions, or the protocol could retain a preliminary schedule. SAP/report could implement a pilot-refined schedule. The affected paragraphs do not define those substitutions. Actual delivery logs and a schedule revision crosswalk are absent.

**Exact remaining human question:** What per-participant totals and phase-specific transmission schedules governed Phase3, and how do the protocol's178/134 totals and printed daily/weekly segments map to the SAP/report's134-message schedule?

**Classification rationale:** Prospective protocol and SAP content are PLAN; implemented intervention descriptions are REPORT. Internal protocol schedule/total contrasts and protocol–SAP contrast give P_P; protocol–report gives P_R, which has precedence. Agreeing report abstract/SAP passages corroborate the implemented side and do not create S_C.

**Classification ambiguity:** Unique templates or branching might differ from per-person transmissions; pilot refinement is expressly possible. Actual transmissions and the applied schedule revision are absent.

**Checker provenance:** F-NUM-104, F-XS-005; checkers/numeric_consistency.md; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.



## C002 — Operational eligibility criteria differ from the plan list

Pending Human Adjudication.

**Candidate statement:** Operational eligibility criteria differ from the plan list.

**Source-order key:** DOC-001 PDF p. 2.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.11,49 vs REPORT DOC-001 pp.2,4 and DOC-003 p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: the explicitly planned recent-stop/reduction exception and the reported operational reader exclusion bear on the primary analysis population. B2: phone access is not an immediate equivalent of an available SMS reader, and the finite plan lists do not map the exception to the≥25-day condition. B3: eligibility definitions attached to the1080-participant primary trial can be copied differently. No changed participant count is inferred.

**Finding IDs:** F-XS-008

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 2](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2>), eligibility paragraph; REPORT.
- [DOC-001 — PDF p. 4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 exclusions; REPORT.
- [DOC-002 — PDF p. 11](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=11>), lines235–255 complete participant lists; PLAN.
- [DOC-002 — PDF p. 49](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=49>), lines1375–1395 complete participant lists; PLAN.
- [DOC-003 — PDF p. 3](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=3>), eTable1 smoking and SMS-reader reasons; REPORT.

**Source evidence:** Both plan lists permit daily smoking or stopping/reducing below daily since TB diagnosis and require personal mobile access; neither lists ≥25 smokingdays or a patient/household SMS reader. Main report requires≥25days in the lastmonth. Figure1/eTable1 include236 excluded for inability to read with no household reader; eTable1 gives7069 not meeting the recent-smoking rule.

**Calculation:** Match each finite eligibility-list item. Diagnosis,age,consent,quit willingness and mobile access match; the explicit recent-reduction exception and reader criterion do not have matched counterparts. Reasons overlap, so236 is a reason count rather than an inferred additional unique exclusion deficit; no adjusted population-size arithmetic is asserted.

**Affected result or extracted value:** Selection rules for1080 randomized participants and the population to which the primary abstinence estimate applies.

**Why context does not resolve it:** These are actual operational selection rules with a printed exclusion reason, not interchangeable wording for daily smoking/phone ownership. The plan exception can permit patients failing the report's recent-smoking requirement.

**Alternative source-grounded interpretations:** Some recent reducers may meet25days; a later operational amendment might introduce the reader rule. The amount of participant overlap and any amendment are absent.

**Exact remaining human question:** Were recent-stop/reduction smokers eligible as planned, and where were the≥25-day and patient/household SMS-reader criteria prespecified or amended?

**Classification rationale:** Planned prospective eligibility versus actual selection gives P_R/protocol_report. Report and results supplement agree on the exclusion and are corroborating locations, not an S_C conflict.

**Classification ambiguity:** Some recently reduced smokers could meet25days; a later operational amendment could govern. Criterion overlap and amendment provenance are missing.

**Checker provenance:** F-XS-008; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.



## C003 — Prospective quit-date and reminder calendar differ from the report

Pending Human Adjudication.

**Candidate statement:** Prospective quit-date and reminder calendar differ from the report.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SMS log pp.101,103,104,109 vs REPORT DOC-001 p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: quit date defines the primary continuous-abstinence start, and the dated reminders define the randomized intervention calendar. B2: Q(−8), the ordinal8th-day wording and5days after enrollment are not mapped by the supplied clock definitions or immediate report description. B3: the extractable endpoint-start/intervention timing differs. Participant-level implementation and outcome reclassification are not inferred.

**Finding IDs:** F-XS-006

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Outcomes and Trial Intervention; REPORT.
- [DOC-002 — PDF p. 101](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=101>), enrollment Q(−8)/Tx(+1), message6 and footnotes; PLAN.
- [DOC-002 — PDF p. 103](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=103>), Q(−1)/Tx(+8) and quit transition; PLAN.
- [DOC-002 — PDF p. 104](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=104>), quit-date ordinal label and messages39–44; PLAN.
- [DOC-002 — PDF p. 109](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=109>), messages129–134 and follow-up phase; PLAN.

**Source evidence:** Report sets quitdate5days after enrollment and sends4 messages,1/month during months3–6. Log pairs enrollment withQ(−8)/Tx(+1), Q(−1)/Tx(+8) with a tomorrow-quit instruction, and quitdate with “8th day since joining mTB-Tobacco”; message6 atQ(−7) says7days from today. Final daily messages endQ(+41)/Tx(+50). Reminder132 isQ(+52)/Tx(+61),133Q(+112)/Tx(+121),134Q(+180)/Tx(+189), with texts naming treatmentmonths2,4,6.

**Calculation:** For the direct Q(−8) versus5-day anchors, rounded ranges[7.5,8.5] and[4.5,5.5] yield gap2/5=.40. Inclusive ordinal-day reading could yield7elapsed days; [6.5,7.5] versus[4.5,5.5] yields gap1/5=.20. Three versus four reminders alone has touching count intervals and does not qualify independently. The different dated calendar and primary-start anchors remain the basis.

**Affected result or extracted value:** Start of the primary continuous-abstinence assessment and intervention reminder timing/duration.

**Why context does not resolve it:** Neither the dated prospective log nor report maps joining,enrollment and treatment clocks to the other schedule or identifies an implemented revision; the primary endpoint is defined since quitdate.

**Alternative source-grounded interpretations:** The log may be preliminary and refined after piloting; enrollment and treatment dates may differ; ordinal day numbering may count enrollment as day1. The report's actual delivered-log revision and clock crosswalk are absent.

**Exact remaining human question:** How do the report's5days after enrollment and the log'sQ(−8)/“8th day since joining” quit anchors map, and which reminder-calendar revision was delivered?

**Classification rationale:** A prospective operational message log is PLAN by content; actual reported endpoint/intervention timing is REPORT. This is P_R/protocol_report. No plan-only clock contrast is registered separately.

**Classification ambiguity:** Joining, enrollment, quit-date and treatment clocks require a supplied crosswalk; ordinal counting and pilot refinement are alternative explanations.

**Checker provenance:** F-XS-006; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.



## C004 — Primary cotinine verification lacks a planned-to-reported criterion crosswalk

Pending Human Adjudication.

**Candidate statement:** Primary cotinine verification lacks a planned-to-reported criterion crosswalk.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.8,47,84 vs REPORT DOC-001 p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: this compares explicit planned and implemented primary biochemical endpoint decision specifications. B2: the named graded NicAlert level<3 rule and binary-negative AllTest rule do not supply a common concentration definition; assay names do not establish equivalence. B3: the verification criterion attached to primary abstinence among concomitant smokeless-tobacco users cannot be extracted as a single supplied numeric criterion. This is not a demonstrated concentration change or changed event count.

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Outcomes cotinine verification; REPORT.
- [DOC-002 — PDF p. 8](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=8>), lines158–161 primary endpoint; PLAN.
- [DOC-002 — PDF p. 47](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1298–1301 primary endpoint; PLAN.
- [DOC-002 — PDF p. 84](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2661–2665 SAP primary endpoint; PLAN.

**Source evidence:** Protocol names Accutest NicAlert strips on a0–6scale and level<3, described as100–200ng/mL, as abstinence. SAP repeats the gradedlevel<3criterion. Report names a Hangzhou AllTest rapid-test cassette and defines a negative result as verification of abstinence for concomitant smokeless-tobacco use.

**Calculation:** Match the explicit primary classification procedure and decision criterion: gradedlevel<3 on a specified strip versus a binarynegative result on a named different cassette. Numerical threshold equivalence cannot be computed because the cassette negative-result concentration is absent. No numerical threshold discrepancy or participant reclassification is asserted.

**Affected result or extracted value:** Biochemical primary-abstinence classification among baseline concomitant smokeless-tobacco users.

**Why context does not resolve it:** The supplied sources specify different decision outputs and named assays for the same primary classification, with no mapping; a reader cannot identify the operative concentration criterion from immediate report text. This is an endpoint specification comparison within focusD, not a critique of assay choice.

**Alternative source-grounded interpretations:** The cassette negative cutoff may implement exactly the planned graded threshold, or an amended criterion may have been used. Those are source-bounded alternatives; equivalence is not inferable from assay names. The assay crosswalk is absent.

**Exact remaining human question:** What concentration criterion defined a negative AllTest cassette result, and how did it implement the planned NicAlertlevel<3primary criterion?

**Classification rationale:** Protocol/SAP endpoint rules are PLAN; the implemented endpoint procedure is REPORT. All relationships are P_R, hence protocol_report. Agreement among plan passages introduces no P_P.

**Classification ambiguity:** Equivalent classifications by the two assays remain possible. The cutoff crosswalk and applicable assay amendment are absent.

**Checker provenance:** F-XS-007; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.



## C005 — Primary model changes from protocol Poisson/log link to SAP/report logistic

Pending Human Adjudication.

**Candidate statement:** Primary model changes from protocol Poisson/log link to SAP/report logistic.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP pp.91,92 and REPORT DOC-001 p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route A, category5: the planned Poisson/log-link primary analysis has no supplied reported counterpart, and SAP/report name logistic analysis for that categorical primary endpoint. SAP/report agreement or a possible superseding plan is an alternative explanation, not removal of this always-register planned-analysis comparison.

**Finding IDs:** F-XS-001, F-ST1-003

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Statistical Analysis; REPORT.
- [DOC-002 — PDF p. 28](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764 statistical-analysis paragraph; PLAN.
- [DOC-002 — PDF p. 66](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2011–2016 statistical-analysis paragraph; PLAN.
- [DOC-002 — PDF p. 77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), change note; PLAN.
- [DOC-002 — PDF p. 91](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2884–2889 primary model; PLAN.
- [DOC-002 — PDF p. 92](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926 adjusted model; PLAN.

**Source evidence:** Both protocol statistical-analysis paragraphs specify generalized linear mixed models with log link and underlyingPoisson distribution, cluster random intercept, crude/adjustedRRs and95%CIs. SAP specifies mixed-effectslogistic regression with site random effect andRR; report specifies logistic regression within the mixed-effects framework for categorical outcomes.

**Calculation:** Compare explicitly named families/links for the same primary six-month binary abstinence analysis: log(p)=η versus logit(p)=η are distinct model specifications. No display-precision rule applies to categorical model-family statements. The supplied change note identifies other amendments but gives no model-replacement mapping.

**Affected result or extracted value:** Primary ITTRR3.0[2.0,4.9],adjustedRR3.2[2.2,5.2],and their analysis-prespecification provenance.

**Why context does not resolve it:** Route A category5 registers a planned primary analysis replaced/notreported; SAP/report agreement does not remove the protocol's planned model or document its replacement.

**Alternative source-grounded interpretations:** SAP may supersede the protocol; a separate Poisson analysis may exist; the report's family wording may describe another computation. Model code, hierarchy and replacement disclosure are absent.

**Exact remaining human question:** Which family/link generated the reported primary RRs/CIs, and where is the protocol Poisson/log-link replacement or distinct-analysis mapping documented?

**Classification rationale:** Protocol–SAP gives P_P; protocol–report gives P_R. P_R takes precedence, giving protocol_report. A physical supplement containing the plan remains PLAN.

**Classification ambiguity:** Final plan hierarchy, actual fitted family/link and whether a separate Poisson analysis exists remain unknown.

**Checker provenance:** F-XS-001, F-ST1-003; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.



## C006 — Risk-ratio derivation from stated logistic analysis is unclear

Pending Human Adjudication.

**Candidate statement:** Risk-ratio derivation from stated logistic analysis is unclear.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.3 method vs REPORT DOC-001 p.6 RR labels; REPORT DOC-003 pp.11,13,14 affected displays

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: a source-grounded model-to-effect-measure chain is statistical method logic. B2: logistic regression plus anRR label alone does not identify the required prediction/conversion or different fitted link, and immediate methods/table notes do not state one. B3: the conditional or marginal risk estimand attached to primaryRR3.0/3.2 and its uncertainty is unresolved. This is not a demonstration that a coefficient odds ratio was numerically printed as a risk ratio.

**Finding IDs:** F-ST1-002

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Statistical Analysis categorical model; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 RR columns and notea; REPORT.
- [DOC-003 — PDF p. 11](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=11>), eTable7 relative-risk row; REPORT.
- [DOC-003 — PDF p. 13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9 RR columns; REPORT.
- [DOC-003 — PDF p. 14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>), eTable9 notee; REPORT.

**Source evidence:** The report states mixed-effects logistic regression for categorical outcomes. Table 2 labels primary 3.0 [2.0,4.9] and adjusted 3.2 [2.2,5.2] as RR; eTables 7/9 repeat RR labels.

**Calculation:** For logit(p)=η, exponentiating a treatment coefficient produces an OR. An RR requires prediction, standardization, conversion, or a different fitted link. No step is named between the stated logistic model and these risk-based estimates; no OR-to-RR numerical identity or crude-ratio discrepancy is asserted.

**Affected result or extracted value:** The risk-based estimand and uncertainty attached to primary RR 3.0/3.2 and other displayed RRs.

**Why context does not resolve it:** A needed estimand-producing step is absent from the stated model-to-effect-measure chain, leaving marginal versus conditional risk quantities unidentified from immediate methods and notes.

**Alternative source-grounded interpretations:** Standardized predicted risks may produce the RRs; a log-link model may have been fitted; logistic wording may describe a separate analysis. Model code, averaging distribution, conversion rule and row-specific mapping are absent.

**Exact remaining human question:** What prediction, standardization, conversion or fitted-link rule produced the printed RRs and CIs from the stated logistic mixed-effects analysis?

**Classification rationale:** Main method-to-label comparison is inside one REPORT, giving S_W/statistical_results. Supplementary risk labels repeat affected output conventions; they do not conflict with main risk labels and therefore do not create S_C. A corroborating SAP is not a relationship.

**Classification ambiguity:** A legitimate predicted-risk derivation, another fitted link or separate analysis is possible. Conditional versus marginal estimand andCI construction are missing definitions.

**Checker provenance:** F-ST1-002; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.



## C007 — Planned tobacco-use-form adjustment has no reported primary counterpart

Pending Human Adjudication.

**Candidate statement:** Planned tobacco-use-form adjustment has no reported primary counterpart.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP p.92 vs REPORT DOC-001 pp.3,4,6 and DOC-003 p.14

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route A, category5: the explicitly planned tobacco-use-form term in the fully adjusted primary model has no counterpart in repeated finite reported adjustment lists or a separately supplied planned-model result. Possible omission from the description is an alternative, not evidence that the planned result was supplied.

**Finding IDs:** F-XS-003, F-ST1-005

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), finite post hoc fixed-effect list; REPORT.
- [DOC-001 — PDF p. 4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Primary Outcome adjusted analysis; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 notea; REPORT.
- [DOC-002 — PDF p. 92](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926 fully adjusted models; PLAN.
- [DOC-003 — PDF p. 14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>), eTable9 notee; REPORT.

**Source evidence:** SAP fully adjusted models include sociodemographic variables alongside tobacco use form and other baseline characteristics. The report and Table 2/eTable 9 notes repeatedly give the finite post hoc set age, sex, education, occupation, smoking duration; tobacco form is absent. Primary adjusted RR is 3.2 [2.2,5.2] and death-excluded adjusted RR 3.1 [1.9,6.5].

**Calculation:** Item-match the explicitly planned tobacco-form term to the finite reported list. No term or result for that prespecified fully adjusted primary model is supplied; precision is inapplicable to covariate inclusion.

**Affected result or extracted value:** Adjusted primary and sensitivity RRs and whether they represent the planned fully adjusted analysis.

**Why context does not resolve it:** Route A category 5 applies to a planned primary analysis replaced or not reported; post hoc selection does not supply the planned model's result.

**Alternative source-grounded interpretations:** Tobacco form may have been fitted but omitted from repeated descriptions, dropped intentionally or merged into another variable. The fitted list and planned-model result are absent.

**Exact remaining human question:** Was tobacco use form included, and where is the planned fully adjusted primary result or its documented replacement?

**Classification rationale:** Prospective SAP adjustment rule versus reported model descriptions gives P_R/protocol_report. Agreement among reported lists is corroboration, without S_C/S_W conflict.

**Classification ambiguity:** The term might be fitted but omitted in prose, aliased, intentionally removed or amended. Actual model formula, term mapping and planned-model result are absent.

**Checker provenance:** F-XS-003, F-ST1-005; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.


