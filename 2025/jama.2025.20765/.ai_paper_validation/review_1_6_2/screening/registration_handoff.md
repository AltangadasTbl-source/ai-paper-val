# Independent screening registration handoff

Pending Human Adjudication. This is a provisional ledger draft, not a stable candidate ledger. Runtime: 01a12c4f-b7b6-7203-8c95-cfee2debbcc0; gpt-6.1-sol/high. All 30 initial findings were independently screened: 29 INCLUDE findings consolidate into 19 issues; F-ST1-007 is screened out as CONDITIONAL_OR_UNREPORTED. Candidate IDs in the canonical screening table remain PENDING. Each ISSUE group below names every included Finding ID, and the coordinator assigns stable IDs without further selection.

Source-order keys use conflicting locations, excluding general corroboration; DOC-001, then DOC-002, then DOC-003, earliest affected PDF page, with ties retained in displayed order. ISSUE-012 has DOC-001 p.5 as its earliest conflicting location (TB-specific32/52 versus p.8 attribution); p.1 enrollment and p.4 total deaths are corroborating count/denominator locations. ISSUE-013 also begins at DOC-001 p.5. ISSUE-015 uses DOC-002 p.47 as its current conflicting location; p.9 is historical/amendment context and report failure counts identify impact without a competing threshold. Source links below resolve from this screening artifact; transfer to a review-root ledger requires changing ../../../ to ../../.

All source locations were confirmed from exact source-matched pages: the screener's 32-page visual scope plus the separately assigned 14-page plan confirmation (source_confirmation_plan.md, runtime 01a12c50-f19c-7ce1-aab5-f9cdca5b913f), read completely before decisions. No new rendering/OCR, web, legacy scientific conclusions, severity, validity or disposition is used. PENDING_RECHECK and PENDING_AUDIT are stage placeholders only and must be replaced by the independent later stages.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| ISSUE-001 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.16,53 and SAP p.80 vs REPORT DOC-001 pp.1,3 | PENDING_RECHECK | PENDING_AUDIT | F-NUM-104, F-XS-005 |
| ISSUE-002 | protocol_report | P_R | P_R | PLAN DOC-002 pp.11,49 vs REPORT DOC-001 pp.2,4 and DOC-003 p.3 | PENDING_RECHECK | PENDING_AUDIT | F-XS-008 |
| ISSUE-003 | protocol_report | P_R | P_R | PLAN DOC-002 SMS log pp.101,103,104,109 vs REPORT DOC-001 p.3 | PENDING_RECHECK | PENDING_AUDIT | F-XS-006 |
| ISSUE-004 | protocol_report | P_R | P_R | PLAN DOC-002 pp.8,47,84 vs REPORT DOC-001 p.3 | PENDING_RECHECK | PENDING_AUDIT | F-XS-007 |
| ISSUE-005 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP pp.91,92 and REPORT DOC-001 p.3 | PENDING_RECHECK | PENDING_AUDIT | F-XS-001, F-ST1-003 |
| ISSUE-006 | statistical_results | S_W | S_W | REPORT DOC-001 p.3 method vs REPORT DOC-001 p.6 RR labels; REPORT DOC-003 pp.11,13,14 affected displays | PENDING_RECHECK | PENDING_AUDIT | F-ST1-002 |
| ISSUE-007 | protocol_report | P_R | P_R | PLAN DOC-002 SAP p.92 vs REPORT DOC-001 pp.3,4,6 and DOC-003 p.14 | PENDING_RECHECK | PENDING_AUDIT | F-XS-003, F-ST1-005 |
| ISSUE-008 | protocol_report | P_R | P_R, S_C | PLAN DOC-002 p.84 primary definition vs REPORT DOC-003 p.13 primary block; REPORT DOC-001 pp.3,6 sensitivity definition | PENDING_RECHECK | PENDING_AUDIT | F-ST1-008 |
| ISSUE-009 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP p.91 and REPORT DOC-001 pp.3,4 | PENDING_RECHECK | PENDING_AUDIT | F-XS-002, F-ST1-004 |
| ISSUE-010 | protocol_report | P_R | P_R | PLAN DOC-002 SAP pp.92,93,99 vs REPORT DOC-001 pp.3,5 and DOC-003 p.12 | PENDING_RECHECK | PENDING_AUDIT | F-XS-004, F-ST1-006 |
| ISSUE-011 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.48,62 vs PLAN DOC-002 pp.63,64,83 and REPORT DOC-001 p.3 | PENDING_RECHECK | PENDING_AUDIT | F-XS-010, F-ST1-010 |
| ISSUE-012 | report_internal_inconsistency | S_C | S_C, S_W | REPORT DOC-001 p.8 discussion vs REPORT DOC-001 pp.4,5,6 and DOC-003 p.6 | PENDING_RECHECK | PENDING_AUDIT | F-NUM-001, F-XS-012 |
| ISSUE-013 | statistical_results | S_W | S_W | REPORT DOC-001 p.5 prevalence pairs vs same-paragraph direction; REPORT DOC-003 p.15 corroborates and supplies severity alternative | PENDING_RECHECK | PENDING_AUDIT | F-NUM-002, F-XS-013 |
| ISSUE-014 | statistical_results | S_W | S_W | REPORT DOC-001 p.6 Table2 within-display rows and REPORT DOC-003 pp.12,13 respective within-display rows | PENDING_RECHECK | PENDING_AUDIT | F-ST1-001 |
| ISSUE-015 | plan_material | P_P | P_P | PLAN DOC-002 pp.9,47,77,85; REPORT DOC-001 pp.1,3,6 identifies affected result | PENDING_RECHECK | PENDING_AUDIT | F-XS-009, F-ST1-011 |
| ISSUE-016 | plan_material | P_P | P_P | PLAN DOC-002 pp.48,63,65,77,83; PLAN p.64 peripheral Phase4context | PENDING_RECHECK | PENDING_AUDIT | F-XS-011, F-ST1-009 |
| ISSUE-017 | statistical_results | S_W | S_W | REPORT DOC-003 p.6 affected cells vs same-table death total | PENDING_RECHECK | PENDING_AUDIT | F-NUM-101 |
| ISSUE-018 | statistical_results | S_W | S_W | REPORT DOC-003 p.9 site2008 vs same-table count/percentage pattern; REPORT DOC-003 p.8 corroborates denominator | PENDING_RECHECK | PENDING_AUDIT | F-NUM-102 |
| ISSUE-019 | statistical_results | S_W | S_W | REPORT DOC-003 p.13 treatment-failure cell vs same-display arm risks and common contrast; p.14 defines difference | PENDING_RECHECK | PENDING_AUDIT | F-NUM-103 |

## ISSUE-001 — Protocol SMS totals and frequency schedules do not reconcile

**Candidate statement:** Protocol SMS totals and frequency schedules do not reconcile.

**Source-order key:** DOC-001 PDF p. 1.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.16,53 and SAP p.80 vs REPORT DOC-001 pp.1,3

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

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

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Nominal conservative 28-day-month minima are344 and288, respectively. Allow every two-month duration [1.5,2.5] months, every frequency endpoint ±0.5, and calendar months28–31days: earlier enclosure [213,725.178572], later [171,636.607143]; totals178±0.5 and134±0.5 yield gaps34.5/178=.193820 and36.5/134=.272388. For month2, later-protocol lower4/day±.5 and report1/day±.5 yield gap2/day,relative2.0. The categorical duration/frequency schedules also differ. The amendment between178 and134 totals is context, not an independent finding.

**Affected result or extracted value:** Planned per-participant intervention dose and the delivered schedule attached to the primary abstinence RR3.0[2.0,4.9].

**Why context does not resolve it:** The same protocol paragraphs state per-participant receipts and transmission schedules; immediate pilot-refinement permission does not identify which quantitative schedule governs or reconcile the internal totals. This is intervention dose in the permitted cross-comparison tier, not general intervention critique.

**Alternative source-grounded interpretations:** Totals could denote unique templates/branches rather than actual transmissions, or the protocol could retain a preliminary schedule. SAP/report could implement a pilot-refined schedule. The affected paragraphs do not define those substitutions. Actual delivery logs and a schedule revision crosswalk are absent.

**Exact remaining human question:** What per-participant totals and phase-specific transmission schedules governed Phase3, and how do the protocol's178/134 totals and printed daily/weekly segments map to the SAP/report's134-message schedule?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Both protocol/SAP internal conflicts and a protocol-report dose conflict are part of the same frequency-paragraph issue; P_R takes precedence over P_P. REPORT abstract/main methods agree with the SAP side.

**Classification ambiguity:** The early and later bundle-component descriptors do not establish precise version chronology, particularly given V6 headers elsewhere; the paired within-paragraph discrepancies do not require that chronology.

**Checker provenance:** F-NUM-104, F-XS-005; checkers/numeric_consistency.md; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-002 — Operational eligibility criteria differ from the plan list

**Candidate statement:** Operational eligibility criteria differ from the plan list.

**Source-order key:** DOC-001 PDF p. 2.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.11,49 vs REPORT DOC-001 pp.2,4 and DOC-003 p.3

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-008

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 2](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2>), eligibility paragraph; REPORT.
- [DOC-001 — PDF p. 4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 exclusions; REPORT.
- [DOC-002 — PDF p. 11](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=11>), lines235–255 complete participant lists; PLAN.
- [DOC-002 — PDF p. 49](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=49>), lines1375–1395 complete participant lists; PLAN.
- [DOC-003 — PDF p. 3](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=3>), eTable1 smoking and SMS-reader reasons; REPORT.

**Source evidence:** Both plan lists permit daily smoking or stopping/reducing below daily since TB diagnosis and require personal mobile access; neither lists ≥25 smokingdays or a patient/household SMS reader. Main report requires≥25days in the lastmonth. Figure1/eTable1 include236 excluded for inability to read with no household reader; eTable1 gives7069 not meeting the recent-smoking rule.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Match each finite eligibility-list item. Diagnosis,age,consent,quit willingness and mobile access match; the explicit recent-reduction exception and reader criterion do not have matched counterparts. Reasons overlap, so236 is a reason count rather than an inferred additional unique exclusion deficit; no adjusted population-size arithmetic is asserted.

**Affected result or extracted value:** Selection rules for1080 randomized participants and the population to which the primary abstinence estimate applies.

**Why context does not resolve it:** These are actual operational selection rules with a printed exclusion reason, not interchangeable wording for daily smoking/phone ownership. The plan exception can permit patients failing the report's recent-smoking requirement.

**Alternative source-grounded interpretations:** Some recent reducers may meet25days; a later operational amendment might introduce the reader rule. The amount of participant overlap and any amendment are absent.

**Exact remaining human question:** Were recent-stop/reduction smokers eligible as planned, and where were the≥25-day and patient/household SMS-reader criteria prespecified or amended?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Conflicting planned and operational eligibility specifications concern the primary trial population, so P_R and protocol_report apply.

**Classification ambiguity:** No exact number uniquely excluded by the changed criteria is inferable from overlapping reason counts.

**Checker provenance:** F-XS-008; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-003 — Prospective quit-date and reminder calendar differ from the report

**Candidate statement:** Prospective quit-date and reminder calendar differ from the report.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SMS log pp.101,103,104,109 vs REPORT DOC-001 p.3

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-006

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Outcomes and Trial Intervention; REPORT.
- [DOC-002 — PDF p. 101](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=101>), enrollment Q(−8)/Tx(+1), message6 and footnotes; PLAN.
- [DOC-002 — PDF p. 103](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=103>), Q(−1)/Tx(+8) and quit transition; PLAN.
- [DOC-002 — PDF p. 104](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=104>), quit-date ordinal label and messages39–44; PLAN.
- [DOC-002 — PDF p. 109](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=109>), messages129–134 and follow-up phase; PLAN.

**Source evidence:** Report sets quitdate5days after enrollment and sends4 messages,1/month during months3–6. Log pairs enrollment withQ(−8)/Tx(+1), Q(−1)/Tx(+8) with a tomorrow-quit instruction, and quitdate with “8th day since joining mTB-Tobacco”; message6 atQ(−7) says7days from today. Final daily messages endQ(+41)/Tx(+50). Reminder132 isQ(+52)/Tx(+61),133Q(+112)/Tx(+121),134Q(+180)/Tx(+189), with texts naming treatmentmonths2,4,6.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** For the direct Q(−8) versus5-day anchors, rounded ranges[7.5,8.5] and[4.5,5.5] yield gap2/5=.40. Inclusive ordinal-day reading could yield7elapsed days; [6.5,7.5] versus[4.5,5.5] yields gap1/5=.20. Three versus four reminders alone has touching count intervals and does not qualify independently. The different dated calendar and primary-start anchors remain the basis.

**Affected result or extracted value:** Start of the primary continuous-abstinence assessment and intervention reminder timing/duration.

**Why context does not resolve it:** Neither the dated prospective log nor report maps joining,enrollment and treatment clocks to the other schedule or identifies an implemented revision; the primary endpoint is defined since quitdate.

**Alternative source-grounded interpretations:** The log may be preliminary and refined after piloting; enrollment and treatment dates may differ; ordinal day numbering may count enrollment as day1. The report's actual delivered-log revision and clock crosswalk are absent.

**Exact remaining human question:** How do the report's5days after enrollment and the log'sQ(−8)/“8th day since joining” quit anchors map, and which reminder-calendar revision was delivered?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** The SMS log is prospective operational PLAN content; the primary-start/intervention-calendar comparison is P_R rather than a comparison of descriptive message wording.

**Classification ambiguity:** The exact elapsed-day interpretation of the ordinal quit label is unresolved and preserved explicitly; no silent8-day normalization is made.

**Checker provenance:** F-XS-006; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-004 — Primary cotinine verification lacks a planned-to-reported criterion crosswalk

**Candidate statement:** Primary cotinine verification lacks a planned-to-reported criterion crosswalk.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.8,47,84 vs REPORT DOC-001 p.3

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Outcomes cotinine verification; REPORT.
- [DOC-002 — PDF p. 8](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=8>), lines158–161 primary endpoint; PLAN.
- [DOC-002 — PDF p. 47](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1298–1301 primary endpoint; PLAN.
- [DOC-002 — PDF p. 84](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2661–2665 SAP primary endpoint; PLAN.

**Source evidence:** Protocol names Accutest NicAlert strips on a0–6scale and level<3, described as100–200ng/mL, as abstinence. SAP repeats the gradedlevel<3criterion. Report names a Hangzhou AllTest rapid-test cassette and defines a negative result as verification of abstinence for concomitant smokeless-tobacco use.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Match the explicit primary classification procedure and decision criterion: gradedlevel<3 on a specified strip versus a binarynegative result on a named different cassette. Numerical threshold equivalence cannot be computed because the cassette negative-result concentration is absent. No numerical threshold discrepancy or participant reclassification is asserted.

**Affected result or extracted value:** Biochemical primary-abstinence classification among baseline concomitant smokeless-tobacco users.

**Why context does not resolve it:** The supplied sources specify different decision outputs and named assays for the same primary classification, with no mapping; a reader cannot identify the operative concentration criterion from immediate report text. This is an endpoint specification comparison within focusD, not a critique of assay choice.

**Alternative source-grounded interpretations:** The cassette negative cutoff may implement exactly the planned graded threshold, or an amended criterion may have been used. Those are source-bounded alternatives; equivalence is not inferable from assay names. The assay crosswalk is absent.

**Exact remaining human question:** What concentration criterion defined a negative AllTest cassette result, and how did it implement the planned NicAlertlevel<3primary criterion?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Both compared passages concern planned versus reported primary endpoint verification; P_R/protocol_report applies.

**Classification ambiguity:** Whether the two procedures classify identically is unresolved; the candidate concerns their unlinked printed specifications, not an inferred concentration change.

**Checker provenance:** F-XS-007; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-005 — Primary model changes from protocol Poisson/log link to SAP/report logistic

**Candidate statement:** Primary model changes from protocol Poisson/log link to SAP/report logistic.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP pp.91,92 and REPORT DOC-001 p.3

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

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

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Compare explicitly named families/links for the same primary six-month binary abstinence analysis: log(p)=η versus logit(p)=η are distinct model specifications. No display-precision rule applies to categorical model-family statements. The supplied change note identifies other amendments but gives no model-replacement mapping.

**Affected result or extracted value:** Primary ITTRR3.0[2.0,4.9],adjustedRR3.2[2.2,5.2],and their analysis-prespecification provenance.

**Why context does not resolve it:** Route A category5 registers a planned primary analysis replaced/notreported; SAP/report agreement does not remove the protocol's planned model or document its replacement.

**Alternative source-grounded interpretations:** SAP may supersede the protocol; a separate Poisson analysis may exist; the report's family wording may describe another computation. Model code, hierarchy and replacement disclosure are absent.

**Exact remaining human question:** Which family/link generated the reported primary RRs/CIs, and where is the protocol Poisson/log-link replacement or distinct-analysis mapping documented?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** The protocol-report primary-model conflict givesP_R; protocol-SAP disagreement also givesP_P; P_R takes precedence.

**Classification ambiguity:** DOC-002 p.28 carriesV6.0 07.03.25 despite earlier-component descriptions, so chronological supersession cannot be assumed from the bundle position.

**Checker provenance:** F-XS-001, F-ST1-003; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-006 — Risk-ratio derivation from stated logistic analysis is unclear

**Candidate statement:** Risk-ratio derivation from stated logistic analysis is unclear.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.3 method vs REPORT DOC-001 p.6 RR labels; REPORT DOC-003 pp.11,13,14 affected displays

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-ST1-002

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Statistical Analysis categorical model; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 RR columns and notea; REPORT.
- [DOC-003 — PDF p. 11](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=11>), eTable7 relative-risk row; REPORT.
- [DOC-003 — PDF p. 13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9 RR columns; REPORT.
- [DOC-003 — PDF p. 14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>), eTable9 notee; REPORT.

**Source evidence:** The report states mixed-effects logistic regression for categorical outcomes. Table 2 labels primary 3.0 [2.0,4.9] and adjusted 3.2 [2.2,5.2] as RR; eTables 7/9 repeat RR labels.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** For logit(p)=η, exponentiating a treatment coefficient produces an OR. An RR requires prediction, standardization, conversion, or a different fitted link. No step is named between the stated logistic model and these risk-based estimates; no OR-to-RR numerical identity or crude-ratio discrepancy is asserted.

**Affected result or extracted value:** The risk-based estimand and uncertainty attached to primary RR 3.0/3.2 and other displayed RRs.

**Why context does not resolve it:** A needed estimand-producing step is absent from the stated model-to-effect-measure chain, leaving marginal versus conditional risk quantities unidentified from immediate methods and notes.

**Alternative source-grounded interpretations:** Standardized predicted risks may produce the RRs; a log-link model may have been fitted; logistic wording may describe a separate analysis. Model code, averaging distribution, conversion rule and row-specific mapping are absent.

**Exact remaining human question:** What prediction, standardization, conversion or fitted-link rule produced the printed RRs and CIs from the stated logistic mixed-effects analysis?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** The method-to-measure gap is within the main REPORT; supplement RR labels extend affected results without a conflicting cross-document measure, so S_W applies.

**Classification ambiguity:** No claim that an OR was printed as RR is made; the protocol-model replacement is a separate issue.

**Checker provenance:** F-ST1-002; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-007 — Planned tobacco-use-form adjustment has no reported primary counterpart

**Candidate statement:** Planned tobacco-use-form adjustment has no reported primary counterpart.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP p.92 vs REPORT DOC-001 pp.3,4,6 and DOC-003 p.14

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-003, F-ST1-005

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), finite post hoc fixed-effect list; REPORT.
- [DOC-001 — PDF p. 4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Primary Outcome adjusted analysis; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 notea; REPORT.
- [DOC-002 — PDF p. 92](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926 fully adjusted models; PLAN.
- [DOC-003 — PDF p. 14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>), eTable9 notee; REPORT.

**Source evidence:** SAP fully adjusted models include sociodemographic variables alongside tobacco use form and other baseline characteristics. The report and Table 2/eTable 9 notes repeatedly give the finite post hoc set age, sex, education, occupation, smoking duration; tobacco form is absent. Primary adjusted RR is 3.2 [2.2,5.2] and death-excluded adjusted RR 3.1 [1.9,6.5].

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Item-match the explicitly planned tobacco-form term to the finite reported list. No term or result for that prespecified fully adjusted primary model is supplied; precision is inapplicable to covariate inclusion.

**Affected result or extracted value:** Adjusted primary and sensitivity RRs and whether they represent the planned fully adjusted analysis.

**Why context does not resolve it:** Route A category 5 applies to a planned primary analysis replaced or not reported; post hoc selection does not supply the planned model's result.

**Alternative source-grounded interpretations:** Tobacco form may have been fitted but omitted from repeated descriptions, dropped intentionally or merged into another variable. The fitted list and planned-model result are absent.

**Exact remaining human question:** Was tobacco use form included, and where is the planned fully adjusted primary result or its documented replacement?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** SAP analysis specification versus REPORT finite adjustment list gives P_R/protocol_report.

**Classification ambiguity:** Whether this reflects only an omitted description or an actual fitted-model change remains unresolved.

**Checker provenance:** F-XS-003, F-ST1-005; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-008 — CO<6 sensitivity results appear under a primary-outcome status label

**Candidate statement:** CO<6 sensitivity results appear under a primary-outcome status label.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** PLAN DOC-002 p.84 primary definition vs REPORT DOC-003 p.13 primary block; REPORT DOC-001 pp.3,6 sensitivity definition

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-ST1-008

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), primaryCO<10 and posthocCO<6 sensitivity; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 primary and sensitivity rows; REPORT.
- [DOC-002 — PDF p. 84](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2653–2669 primary endpoint; PLAN.
- [DOC-003 — PDF p. 13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9 Primary outcomes CO<6row; REPORT.

**Source evidence:** SAP defines primary verification as CO<10 ppm. The main article explicitly calls CO<6 a post hoc sensitivity of the primary outcome. eTable 9, titled Post-hoc sensitivity analysis after excluding deaths, places CO<6 under Primary outcomes: 264/695 versus 38/333, RR 3.6 [2.4,5.4], adjusted 3.8 [2.4,6.2].

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Compare categorical outcome status for the same biochemical threshold. The primary-status block contains an alternative post hoc threshold alongside the prespecified primary threshold; numeric rounding does not apply.

**Affected result or extracted value:** Outcome-status extraction accompanying CO<6 RR 3.6/3.8 in the excluding-deaths sensitivity.

**Why context does not resolve it:** Route A category 5 applies to a reproduced planned-outcome status difference; the post hoc table title supplies a possible display convention without removing its printed Primary outcomes block.

**Alternative source-grounded interpretations:** The block may organize analyses of the primary construct, including sensitivities, rather than declare additional primary endpoints. That convention is not explicitly distinguished.

**Exact remaining human question:** Does the CO<6 row retain post hoc sensitivity status, and what status should accompany these estimates when extracted from the Primary outcomes block?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** The supplement primary label differs from the PLAN definition and main REPORT sensitivity statement; P_R takes precedence over S_C.

**Classification ambiguity:** A primary-construct block convention is preserved as a source-grounded alternative.

**Checker provenance:** F-ST1-008; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-009 — Primary missing-outcome handling differs between protocol and SAP/report

**Candidate statement:** Primary missing-outcome handling differs between protocol and SAP/report.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP p.91 and REPORT DOC-001 pp.3,4

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-002, F-ST1-004

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), missing-primary-outcome paragraph; REPORT.
- [DOC-001 — PDF p. 4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 attrition and analysis totals; REPORT.
- [DOC-002 — PDF p. 28](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764 separately headed Statistical analysis; PLAN.
- [DOC-002 — PDF p. 66](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2012–2016 separately headed Statistical analysis; PLAN.
- [DOC-002 — PDF p. 91](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2890–2892 ITT and Russell Standard; PLAN.

**Source evidence:** Protocol says outcomes primarily analyzed in a missing-at-random architecture. SAP regards dropout/incomplete data as continuing smokers. Report treats missing primary outcomes as negative/not abstinent: 53/720 and 42/360, total 95, are missing; primary ITT retains 720/360 and complete-case sensitivity discards missing.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** MAR is a stated missingness architecture; assigning all missing primary outcomes nonabstinent is a deterministic classification. No supplied passage maps them to a combined or separately identified primary analysis. No bias or alternative efficacy result is calculated.

**Affected result or extracted value:** Missing-outcome assumptions attached to ITT 300/720 versus 55/360 and RR 3.0 [2.0,4.9].

**Why context does not resolve it:** The MAR paragraph has its own Statistical analysis heading; adjacency to economic imputation does not restrict it explicitly to costs/QALYs/covariates. Complete-case sensitivity is separately stated.

**Alternative source-grounded interpretations:** MAR may concern another imputation/covariate/economic model, or SAP may supersede the protocol. Neither restriction nor replacement mapping is supplied.

**Exact remaining human question:** Which primary missing-data architecture applied, and how do MAR and missing-as-smoking map to identified analyses or amendments?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Protocol-report conflict gives P_R and protocol-SAP conflict P_P; P_R takes precedence.

**Classification ambiguity:** The separately headed analysis paragraph and economic context leave applicability unresolved; chronological precedence is not assumed.

**Checker provenance:** F-XS-002, F-ST1-004; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-010 — Prespecified gender-specific primary analyses are not reported

**Candidate statement:** Prespecified gender-specific primary analyses are not reported.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP pp.92,93,99 vs REPORT DOC-001 pp.3,5 and DOC-003 p.12

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-004, F-ST1-006

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), prespecified subgroup list; REPORT.
- [DOC-001 — PDF p. 5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), subgroup consistency narrative; REPORT.
- [DOC-002 — PDF p. 92](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2936–2939 subgroup analysis introduction; PLAN.
- [DOC-002 — PDF p. 93](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=93>), lines2940–2952, gender and interval disclosure; PLAN.
- [DOC-002 — PDF p. 99](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=99>), Gender Male/Female table shell; PLAN.
- [DOC-003 — PDF p. 12](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>), complete eTable8; REPORT.

**Source evidence:** SAP specifies primary treatment-effect sensitivity models by age, education, occupation, gender male/female, and smoking duration, each with RR and 95% CI and disclosure of missing CIs. eTable 8 and main subgroup narrative contain age, education, occupation, smoking duration, reading SMS, without gender rows/results or nonestimability explanation. Male baseline counts are 698/720 and 345/360.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Match each planned subgroup to the complete supplied subgroup display and narrative. Gender has no reported counterpart; the blank Male/Female SAP shell corroborates the planned prose and is not a result.

**Affected result or extracted value:** Planned male/female primary RRs/CIs and the robustness scope of the primary abstinence analysis.

**Why context does not resolve it:** Route A category 5 applies to an unreported planned primary analysis. Sparse female observations may explain nonestimation, but the SAP expressly anticipates unavailable-interval disclosure.

**Alternative source-grounded interpretations:** The analysis may have been infeasible, performed but omitted, or removed by amendment. No explanation or result is supplied.

**Exact remaining human question:** Where are the planned male/female primary results or the disclosed reason estimates/CIs were unavailable or removed?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** SAP primary analysis specification versus complete REPORT results gives P_R/protocol_report.

**Classification ambiguity:** The shell is a continuation; primary-analysis status and method are grounded in SAP prose pp.92–93.

**Checker provenance:** F-XS-004, F-ST1-006; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-011 — Current primary-data attrition assumptions differ

**Candidate statement:** Current primary-data attrition assumptions differ.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.48,62 vs PLAN DOC-002 pp.63,64,83 and REPORT DOC-001 p.3

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-010, F-ST1-010

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), sample-size20%attrition; REPORT.
- [DOC-002 — PDF p. 48](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1344–1347 primary-data10%; PLAN.
- [DOC-002 — PDF p. 62](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=62>), lines1861–1863 primary-data10%; PLAN.
- [DOC-002 — PDF p. 63](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1894–1898 Phase3 20%calculation; PLAN.
- [DOC-002 — PDF p. 64](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>), lines1936–1938 Phase4 contextual20%calculation; PLAN.
- [DOC-002 — PDF p. 77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), sample-sizeamendment; PLAN.
- [DOC-002 — PDF p. 83](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2624–2638 SAP20%; PLAN.

**Source evidence:** Current protocol overview/statistics introduction uses 10% missing primary outcome data. Detailed Phase 3 calculation uses 20%, 587+(587×.2)=704, then 1080. SAP and report also use 20%; Phase 4 20% is contextual rather than an additional reported result.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Printed input copies 10±0.5% and 20±0.5% give gap 9 percentage points and relative gap 9/10=0.90. The expressly stated additive inflation formula is not challenged; no alternative power result is asserted.

**Affected result or extracted value:** Attrition assumption attached to reported 90% power and 1080-participant primary design.

**Why context does not resolve it:** Current passages refer to the same primary-data assumption without distinguishing phase or missingness type; the amendment does not map surviving 10% statements to a superseded input.

**Alternative source-grounded interpretations:** Overview/introduction may retain a previous assumption while detail/SAP/report use 20%. A final hierarchy or dated calculation is absent.

**Exact remaining human question:** Which primary-data attrition assumption governed Phase 3, and how do the surviving 10% and 20% specifications relate?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** A current PLAN assumption differs from the REPORT and from other PLAN passages; P_R takes precedence over P_P.

**Classification ambiguity:** The report matches the detailed SAP side; the conflicting overview remains a direct plan-report comparison.

**Checker provenance:** F-XS-010, F-ST1-010; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-012 — All-cause mortality percentage is attributed to TB-specific mortality

**Candidate statement:** All-cause mortality percentage is attributed to TB-specific mortality.

**Source-order key:** DOC-001 PDF p. 5.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 p.8 discussion vs REPORT DOC-001 pp.4,5,6 and DOC-003 p.6

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-001, F-XS-012

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 1](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), 1080randomized,corroboratingdenominator; REPORT.
- [DOC-001 — PDF p. 4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 death25/27 and1080enrolled; REPORT.
- [DOC-001 — PDF p. 5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), TBcause32/52; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 deaths25/720and27/360; REPORT.
- [DOC-001 — PDF p. 8](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8>), discussion4.8%diedofTB; REPORT.
- [DOC-003 — PDF p. 6](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4 total52 andTB32; REPORT.

**Source evidence:** Discussion says 4.8% of trial participants died of TB within six months. Main results say TB caused 61.5% [32/52] of deaths. Figure 1/Table 2 show 25+27=52 deaths among 1080 participants. eTable 4 separately identifies 32 TB and 20 other-cause deaths.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** 32/1080×100=2.962963% versus 52/1080×100=4.814815%. TB rounded-input range is 100×[31.5/1080.5,32.5/1079.5]=[2.915317,3.010653]%, disjoint from printed 4.8±.05=[4.75,4.85]%; gap 1.739347/4.8=.362364. The all-cause ratio overlaps 4.8%.

**Affected result or extracted value:** Six-month TB-specific mortality risk, extractable as 4.8% or 32/1080≈3.0%.

**Why context does not resolve it:** The cause label changes which outcome receives the number; the report explicitly distinguishes TB from other causes and supplies no alternate cause population.

**Alternative source-grounded interpretations:** The discussion may intend all-cause mortality among participants with TB; another cause classification or denominator might underlie 4.8%, but none is stated.

**Exact remaining human question:** Does 4.8% mean all-cause mortality among participants with TB or TB-attributed deaths, and which numerator/denominator defines the latter?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Both REPORT documents and the main REPORT internally disagree about outcome attribution; S_C takes precedence over S_W and report_internal_inconsistency identifies the central issue.

**Classification ambiguity:** Counts support the comparison, but no separate count issue is registered; general enrollment/all-cause counts are corroboration.

**Checker provenance:** F-NUM-001, F-XS-012; checkers/numeric_consistency.md; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-013 — Adverse-event narrative reverses two any-symptom arm directions

**Candidate statement:** Adverse-event narrative reverses two any-symptom arm directions.

**Source-order key:** DOC-001 PDF p. 5.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.5 prevalence pairs vs same-paragraph direction; REPORT DOC-003 p.15 corroborates and supplies severity alternative

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-002, F-XS-013

**Qualifying route:** Route A, category 2

**Exact source locations:**

- [DOC-001 — PDF p. 5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), Adverse Events ordered percentages and summarysentence; REPORT.
- [DOC-003 — PDF p. 15](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=15>), eTable10 irritability/anxiety severity rows; REPORT.

**Source evidence:** Main Adverse Events fixes arm order mHealth versus usual care, prints irritability 40.5% versus 43.4% and anxiety 33.3% versus 36.8%, then says both were more common in mHealth. eTable 10 None percentages 59.5/56.6 and 66.7/63.2 corroborate those prevalences; moderate/severe frequencies are higher in mHealth.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** mHealth-minus-usual-care rounded prevalence differences are [−3.00,−2.80] and [−3.60,−3.40] percentage points. Gap/control-reference ratios are 2.80/43.4=.064516 and 3.40/36.8=.092391. Both directions remain lower mHealth. Dry mouth 62.7 versus 55.7 agrees and is contextual.

**Affected result or extracted value:** Any-irritability and any-anxiety frequency directions by randomized arm.

**Why context does not resolve it:** Route A category 2 applies to a printed direction reversing the values, even when the intended direction may be reconstructed immediately.

**Alternative source-grounded interpretations:** The sentence may refer instead to moderate/severe symptoms; eTable 10 supports that distinct quantity, but the sentence names no switch.

**Exact remaining human question:** Does more common refer to any irritability/anxiety or moderate/severe burden, and which quantity and arm direction should be extracted?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** The conflicting pairs lie in one main REPORT paragraph; the supplement corroborates and supplies an alternative, so only S_W applies.

**Classification ambiguity:** Any-symptom prevalence and severity burden remain distinct possible readings.

**Checker provenance:** F-NUM-002, F-XS-013; checkers/numeric_consistency.md; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-014 — Fourteen interval rows do not reproduce a rule fitting other display rows

**Candidate statement:** Fourteen interval rows do not reproduce a rule fitting other display rows.

**Source-order key:** DOC-001 PDF p. 6.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.6 Table2 within-display rows and REPORT DOC-003 pp.12,13 respective within-display rows

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 4

**Exact source locations:**

- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2CO10PPadjusted,CO6PPcrude/adjusted,self-reportadjusted; REPORT.
- [DOC-003 — PDF p. 12](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>), eTable8All,age≥40,primary,secondary,active,dependent,smoking<24,readingNo; REPORT.
- [DOC-003 — PDF p. 13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9CO10crude/adjusted; REPORT.
- [DOC-003 — PDF p. 14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>), population/adjustmentnotes; REPORT.

**Source evidence:** All 14 affected RR/lower/upper triples and their rounded-input reconstruction ranges are preserved in the detailed numeric list below. The Table 2 adjusted self-report upper endpoint is literally 42 in the supplied source, without a decimal point. Each source row was visually confirmed.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** Apply U*=E²/L, with range [(E−hE)²/(L+hL),(E+hE)²/(L−hL)] versus [U−hU,U+hU], using exact displayed half-units. Every listed gap/U exceeds .05. The rule reproduces other rows of each display; it is a reconstruction diagnostic rather than a claim about an unstated Wald method. No point is outside its printed CI and no CI/P conflict is inferred.

**Affected result or extracted value:** The 14 upper CI endpoints and corresponding primary/sensitivity/subgroup uncertainty.

**Why context does not resolve it:** Route A category 4 requires inclusion when a rule reproduces other display rows but fails these rows beyond precision; unknown row-specific construction is the human question.

**Alternative source-grounded interpretations:** Profile likelihood, bootstrap, marginal-risk or other nonsymmetric intervals may explain rows; procedures may differ by row. Fitted covariance/SE and construction definitions are absent.

**Exact remaining human question:** Which estimate/interval construction produced every listed row, and are the printed limits, including 42, intended for that construction?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** A repeated within-display reconstruction pattern occurs in two REPORT documents; no cross-document matched-result conflict is asserted, so S_W only.

**Classification ambiguity:** The actual mechanism is unknown; one pattern is registered without attributing a decimal-slip mechanism or selecting a correction.

**Checker provenance:** F-ST1-001; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-015 — Latest protocol and SAP prescribe different failure windows

**Candidate statement:** Latest protocol and SAP prescribe different failure windows.

**Source-order key:** DOC-002 PDF p. 47.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.9,47,77,85; REPORT DOC-001 pp.1,3,6 identifies affected result

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-009, F-ST1-011

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-002 — PDF p. 9](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=9>), lines179–180 earlier-componentmonth5definition; PLAN.
- [DOC-002 — PDF p. 47](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1319–1320month6definition; PLAN.
- [DOC-002 — PDF p. 77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2413–2415 explicit5→6amendment; PLAN.
- [DOC-002 — PDF p. 85](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=85>), lines2685–2686SAPmonth5; PLAN.
- [DOC-001 — PDF p. 1](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), key-secondaryfailureproportions; REPORT.
- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), outcomedetailpointer; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2failure1/720versus2/360; REPORT.

**Source evidence:** Earlier-component protocol and SAP define failure as remaining smear-positive at month 5 or later; later-component protocol uses month 6 or later. The amendment explicitly replaces month 5 with month 6 in v6. Report prints failure 1/720 versus 2/360 without an explicit competing window.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** These are exact categorical endpoint windows, not rounded month measurements. The amendment reconciles historical protocol changes but not the SAP's retained month-5 rule. No patient reclassification or event-count discrepancy is inferred.

**Affected result or extracted value:** Definition attached to the abstract key-secondary failure counts 1 and 2 and TB programme outcome classification.

**Why context does not resolve it:** SAP and amended protocol prescribe different windows for a reported key-secondary endpoint; the report does not identify which classified its three events.

**Alternative source-grounded interpretations:** The amended month-6 rule, SAP month-5 rule or programme-register rule may govern. A finalized endpoint dictionary is absent.

**Exact remaining human question:** Were failures classified using month 5 or later or month 6 or later, and which supplied plan rule governed the three reported events?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Only PLAN materials print the conflicting windows; REPORT counts identify impact but do not supply a competing threshold, so P_P/plan_material applies.

**Classification ambiguity:** Version descriptors on early components are bounded context; amended protocol versus SAP conflict persists independently.

**Checker provenance:** F-XS-009, F-ST1-011; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-016 — Current Phase3 power statements retain different cluster allocations

**Candidate statement:** Current Phase3 power statements retain different cluster allocations.

**Source-order key:** DOC-002 PDF p. 48.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.48,63,65,77,83; PLAN p.64 peripheral Phase4context

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-011, F-ST1-009

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-002 — PDF p. 48](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1348–1353poweroverview; PLAN.
- [DOC-002 — PDF p. 63](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1886–1907Phase3power/allocation; PLAN.
- [DOC-002 — PDF p. 64](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>), Phase4allocationcontext; PLAN.
- [DOC-002 — PDF p. 65](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=65>), lines1958–1963repeatedpowerparagraph; PLAN.
- [DOC-002 — PDF p. 77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2416–2424allocationamendment; PLAN.
- [DOC-002 — PDF p. 83](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2629–2642SAPallocation; PLAN.

**Source evidence:** Current overview/detail/SAP give Phase 3 18 intervention and 9 control clusters, total 27, 90% power at 5%, 18%/8% abstinence. The repeated current protocol paragraph gives 16 and 8 with the same power/rates. The amendment changes 16/8 to 18/9. Its Phase 4 20/20 versus other 18/18 is unreported-phase peripheral context.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** 18±.5 versus 16±.5 yields gap 1/16=.0625. Independently rounded arm sums give [26,28] versus [23,25], gap 1/24=.041667, which does not independently qualify; 9-versus-8 intervals touch. The intervention-arm power input supplies the reproduced basis.

**Affected result or extracted value:** Phase 3 allocation and power inputs underlying the 1080-participant,27-cluster primary trial.

**Why context does not resolve it:** The repeated current paragraph attaches the same power/rates to 16/8 without labeling it historical; this changes a primary analysis-population/power input rather than an administrative site copy.

**Alternative source-grounded interpretations:** The repeated paragraph may carry forward earlier text, or both allocations may have been evaluated without being distinguished. The governing final power calculation is absent.

**Exact remaining human question:** Which Phase 3 allocation and power calculation governs, and should the current 16/8 paragraph be read as historical?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Conflicting power inputs are PLAN-only; reported 27 clusters corroborate rather than conflict, so P_P applies.

**Classification ambiguity:** The unreported Phase 4 allocation remains peripheral context and does not expand included scientific scope.

**Checker provenance:** F-XS-011, F-ST1-009; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-017 — Two cause-of-death percentages do not reconcile within eTable4

**Candidate statement:** Two cause-of-death percentages do not reconcile within eTable4.

**Source-order key:** DOC-003 PDF p. 6.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.6 affected cells vs same-table death total

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-101

**Qualifying route:** Route A, category 3

**Exact source locations:**

- [DOC-003 — PDF p. 6](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4usual-careDruguser,Severepneumonia,Totaldeaths; REPORT.

**Source evidence:** eTable 4 usual-care Drug user and Severe pneumonia each print 1(7.4%), with Total deaths 27. Overall affected counts are 1 and mHealth 0. Stroke 2(7.4%) and fall 1(3.7%) support the common denominator; all cause counts sum 27.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** 100×1/27=3.703704%. Required rounded range 100×[.5/27.5,1.5/26.5]=[1.818182,5.660377]% versus [7.35,7.45]% gives gap 1.689623/7.4=.228327. Both cells fail the same within-display rule and form one issue.

**Affected result or extracted value:** Usual-care death-cause percentages associated with drug use and severe pneumonia.

**Why context does not resolve it:** Route A category 3 applies to co-located count/denominator/percentage inconsistency; recoverable percentage values do not remove the printed 7.4% readings.

**Alternative source-grounded interpretations:** 7.4% could represent two deaths or another denominator; sums corroborate one death but do not assign a correction. No cause-specific denominator is given.

**Exact remaining human question:** What counts, denominators and percentages should be used for the two affected usual-care cause rows?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Affected cells and death total are in one REPORT table; S_W applies.

**Classification ambiguity:** None.

**Checker provenance:** F-NUM-101; checkers/numeric_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-018 — Site2008 death count and percentage do not reproduce the table denominator

**Candidate statement:** Site2008 death count and percentage do not reproduce the table denominator.

**Source-order key:** DOC-003 PDF p. 9.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.9 site2008 vs same-table count/percentage pattern; REPORT DOC-003 p.8 corroborates denominator

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-102

**Qualifying route:** Route A, category 3

**Exact source locations:**

- [DOC-003 — PDF p. 9](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=9>), eTable6Controlsite2008cell5(7.5),otherdeathrows; REPORT.
- [DOC-003 — PDF p. 8](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=8>), eTable5site2008recruitmentandITT40,observed35; REPORT.

**Source evidence:** eTable 6 Control site 2008 prints 5(7.5). All other death rows use N=40, including 3(7.5),4(10.0),site2012 5(12.5). eTable 5 prints recruitment/ITT population 40 and observed contributors 35 for site 2008.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** 100×5/40=12.5%. Rounded range 100×[4.5/40.5,5.5/39.5]=[11.111111,13.924051]% versus [7.45,7.55]% gives gap 3.561111/7.5=.474815. N40 rule reproduces other death cells.

**Affected result or extracted value:** Site 2008 cluster mortality count/percentage.

**Why context does not resolve it:** Route A category 3 and category 4 apply to a co-located numeric display mismatch; it is not a peripheral copy of a contributor count.

**Alternative source-grounded interpretations:** 7.5% represents three of40, while five of40 is12.5%; another denominator would require definition. Counts sum overall52/usual-care27/mHealth25, corroborating counts without assigning a correction.

**Exact remaining human question:** What death count, denominator and percentage governs site 2008 in eTable 6?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** The inconsistency is within eTable 6; eTable 5 corroborates the denominator, so S_W applies.

**Classification ambiguity:** N40 is supported by the display's reproducing pattern and explicitly printed site ITT population.

**Checker provenance:** F-NUM-102; checkers/numeric_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-019 — Treatment-failure absolute difference has the opposite signed contrast

**Candidate statement:** Treatment-failure absolute difference has the opposite signed contrast.

**Source-order key:** DOC-003 PDF p. 13.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.13 treatment-failure cell vs same-display arm risks and common contrast; p.14 defines difference

**Evidence state:** PENDING_RECHECK

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-103

**Qualifying route:** Route A, category 2

**Exact source locations:**

- [DOC-003 — PDF p. 13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9TreatmentFailuresabsolute-difference0.5andarmrisks; REPORT.
- [DOC-003 — PDF p. 14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>), notebAbsolute difference; REPORT.

**Source evidence:** eTable 9 failure risks are mHealth 1/695,0.1%[0.01,0.8], versus usual-care 2/333,0.6%[0.1,2.2]. Absolute difference prints +0.5[-0.4,1.3]. Other rows use mHealth-minus-usual-care:43.2−16.5=26.7;38.0−11.4=26.6;50.8−22.5=28.3;57.5−24.6=32.9;3.2−2.1=1.1; success difference0.

**Reported-versus-comparator:** The compared printed statements and values are preserved above; the logical or numerical discrepancy is limited to the rule below.

**Reasoning procedure:** Match the stated endpoint, population, time, contrast and model before applying the indicated route; retain corroborating sources and alternatives separately from conflicting comparators.

**Calculation:** 100×(1/695−2/333)=−.456716 percentage points. Rounded count/denominator range [−.679989,−.233792] versus [.45,.55] gives gap .683792/.5=1.367585. Printed arm risks independently allow [−.60,−.40], remaining negative.

**Affected result or extracted value:** Signed failure risk difference in the excluding-deaths sensitivity.

**Why context does not resolve it:** Route A category 2 applies to a sign reversing the common displayed contrast; the word Absolute is an alternative interpretation rather than removal of the direction mismatch.

**Alternative source-grounded interpretations:** This row may use unsigned magnitude, reversed reference group or another model-based contrast; no row-specific switch is named. The signed interval and other rows remain printed. No CI construction is inferred.

**Exact remaining human question:** Does Treatment Failures use mHealth-minus-usual-care, and what signed difference and matching interval should be extracted?

**Mechanical evidence recheck:** PENDING_RECHECK; the later fresh rechecker must confirm all linked locations, values, rule, missing inputs and classifications from source.

**Classification rationale:** Counts,risks,point difference and common contrast are in one REPORT display; S_W applies.

**Classification ambiguity:** Unsigned magnitude is retained as an alternative; no separate interval mechanism issue is assigned.

**Checker provenance:** F-NUM-103; checkers/numeric_consistency.md; independent decision in screening/inclusion_screen.md.

**Potential downstream evidence impact:** A data extractor could carry the affected printed value, outcome label, or analysis specification into synthesis; no propagation or conclusion change is asserted.

## ISSUE-014 detailed interval reconstruction

Each line gives display/row, printed E;L;U, independently recomputed U* interval, gap, and gap/|U|. Every displayed input/output receives its own half-unit; a literal42 receives±0.5, not±0.05.

- Table2 CO10 PP adjusted: 3.1;2.1;5.2; reconstructed [4.326744,4.840244]; gap 0.309756; relative 0.059568.
- Table2 CO6 PP crude: 3.6;2.14;6.87; reconstructed [5.875291,6.240047]; gap 0.624953; relative 0.090968.
- Table2 CO6 PP adjusted: 3.8;2.3;7.7; reconstructed [5.984043,6.587778]; gap 1.062222; relative 0.137951.
- Table2 self-report adjusted: 2.8;1.9;42; reconstructed [3.878205,4.390541]; gap 37.109459; relative 0.883559.
- eTable8 All: 2.890;1.983;4.709; reconstructed [4.209332,4.214371]; gap 0.494129; relative 0.104933.
- eTable8 Age≥40: 2.953;2.048;5.092; reconstructed [4.255434,4.260397]; gap 0.831103; relative 0.163217.
- eTable8 Primary: 2.638;1.849;4.07; reconstructed [3.761236,3.766125]; gap 0.298875; relative 0.073434.
- eTable8 Secondary: 2.719;1.348;4.83; reconstructed [5.480343,5.488445]; gap 0.645343; relative 0.133611.
- eTable8 Active: 2.989;1.933;4.885; reconstructed [4.619153,4.624637]; gap 0.259863; relative 0.053196.
- eTable8 Dependent: 2.587;1.329;3.986; reconstructed [5.031954,5.039636]; gap 1.045454; relative 0.262281.
- eTable8 Smoke<24: 3.511;1.884;7.127; reconstructed [6.539459,6.546659]; gap 0.579841; relative 0.081358.
- eTable8 Reading No: 2.198;1.288;3.299; reconstructed [3.747774,3.754099]; gap 0.448274; relative 0.135882.
- eTable9 CO10 crude: 2.9;1.8;6.4; reconstructed [4.390541,4.972857]; gap 1.377143; relative 0.215179.
- eTable9 CO10 adjusted: 3.1;1.9;6.5; reconstructed [4.770513,5.363514]; gap 1.086486; relative 0.167152.

Reproducing comparators: Table 2 self-report crude 2.7 [1.8,4.1], week 9 crude 2.6 [1.8,3.9]/adjusted 2.7 [1.8,4.3], month 6 crude 2.7 [2.0,3.8]/adjusted 2.7 [1.9,4.0], and success 1.2 [.9,1.6]/1.2 [.9,1.5] have overlapping reconstruction/printed intervals. In eTable 8, age <40 gives [4.846799,4.853725] versus [4.8565,4.8575], relative gap .000571; smoking ≥24 gives [3.857124,3.862770] versus [3.9105,3.9115], relative gap .012204; no formal education and reading Yes also pass the .05 rule. In eTable 9, CO<6 3.6 [2.4,5.4]/3.8 [2.4,6.2], week 9 2.5 [1.7,3.6]/2.6 [1.7,3.8], month 6 2.58 [1.8,3.6]/2.7 [1.8,4.0], and success 1.1 [.7,1.6]/1.1 [.7,1.5] have overlapping intervals. These source-confirmed comparators establish the observed reproducing rule without asserting a universal inferential construction.

## Consolidation and boundaries

NUM104/XS005 share the unresolved protocol frequency paragraph and belong to one dose issue, retaining both internal paragraph failures and the finalized-plan/report schedule comparison. XS006 has distinct dated quit-start/reminder anchors and remains separate. XS001/ST1-003 is a primary-model replacement, while ST1-002 is the distinct result-producing RR derivation gap within REPORT. The repeated interval reconstruction is one issue preserving all 14 rows; no cause or preferred correction is inferred. Phase 4 cluster differences in XS011 are peripheral context, with only Phase 3 providing the included basis. All 29 included findings occur exactly once in the classification table and exactly one group.

DOC-002 pp. 8, 13 and 28 carry V6.0 07.03.25 headers, despite checker earlier-component descriptors. The quoted MAR paragraph has its own Statistical analysis heading adjacent to economic text. Plan allocation prose on pp. 13/51 covers the broader three-arm 2:2:1 design and does not establish that volume minimization was absent from the reported two-arm lists; F-ST1-007 identifies an unreported compatible implementation detail and is screened out on that basis. The SMS log's ordinal “8th day since joining” and Q/Tx anchors are preserved, including possible inclusive-day counting. Lower diagram clipping on pp. 13/51 does not obscure cited prose. Actual raw data, delivered logs, assay crosswalk, model code, row-specific CI construction and final plan hierarchy remain absent; they bound the exact questions rather than permit fabricated values.

