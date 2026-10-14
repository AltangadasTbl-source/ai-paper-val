# Independent candidate and screening audit: part 1

Pending Human Adjudication.

Runtime ID: 01a12c70-5a35-7fc1-9c30-a421a32d87bf. Model: gpt-6.1-sol. Reasoning effort: high. Fresh bounded quality-control auditor. Candidate-card scope: C001, C002, C003, C004, C005, C006, C007. Additional scope: all 30 initial finding decisions and all 45 initial checker excluded observations, checked in both directions against QUALITY_CONTROL_SCOPE.md. The complete current ledger, initial screen, complete source-recheck fact handoff, complete excluded-observation handoff and complete pass-2 coverage summary were read. No earlier candidate set, other package or external evidence was used. No candidate-count target controlled these decisions.

Exact-source facts in the independently generated mechanical recheck are the source-confirmation basis. Additional visual confirmation used seven source-matched images: DOC-001 pp.3,6; DOC-002 pp.53,84; DOC-003 pp.5,15,16. Five are current-run CPU images; DOC-003 pp.5,16 are existing reusable raw page images at `.ai_paper_validation/document_outputs/DOC-003/page_images/page-005.png` and `page-016.png`. No new rendering, OCR, scientific orchestration script or source modification was performed. Arithmetic was recomputed directly with numerical interval operations. Physical PDF pages are used throughout; DOC-001 p.3 is printed journal page338, p.6 is341; DOC-002 p.53 has printed component page12 and p.84 has printed SAP page7. Links deliberately use physical PDF pages.

Seven assigned candidate audits are CONFIRMED and none is QUESTIONED. Among the 30 initial screening decisions, 29 are supported and one is QUESTIONED for its inclusion premise, F-ST1-008/C008; its original INCLUDE decision and stable ID remain unchanged. No new independent issue was identified. Two exclusions require a duplicate crosswalk to already included C006/C004 rather than a new issue or stable ID. Coverage/provenance audits of source units, complete relationship inventories, runtime manifests and other candidate cards are assigned to distinct auditor parts; this part does not claim that it independently inspected every source page.

## Classification values for assigned candidates

These values agree between the ledger's table and its candidate cards and are supported by the source recheck. The coordinator must copy the inclusion values and maintain exact equality in the report.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.16,53 and SAP p.80 vs REPORT DOC-001 pp.1,3 | reproduced | CONFIRMED | F-NUM-104, F-XS-005 |
| C002 | protocol_report | P_R | P_R | PLAN DOC-002 pp.11,49 vs REPORT DOC-001 pp.2,4 and DOC-003 p.3 | reproduced | CONFIRMED | F-XS-008 |
| C003 | protocol_report | P_R | P_R | PLAN DOC-002 SMS log pp.101,103,104,109 vs REPORT DOC-001 p.3 | reproduced | CONFIRMED | F-XS-006 |
| C004 | protocol_report | P_R | P_R | PLAN DOC-002 pp.8,47,84 vs REPORT DOC-001 p.3 | reproduced | CONFIRMED | F-XS-007 |
| C005 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP pp.91,92 and REPORT DOC-001 p.3 | reproduced | CONFIRMED | F-XS-001, F-ST1-003 |
| C006 | statistical_results | S_W | S_W | REPORT DOC-001 p.3 method vs REPORT DOC-001 p.6 RR labels; REPORT DOC-003 pp.11,13,14 affected displays | reproduced | CONFIRMED | F-ST1-002 |
| C007 | protocol_report | P_R | P_R | PLAN DOC-002 SAP p.92 vs REPORT DOC-001 pp.3,4,6 and DOC-003 p.14 | reproduced | CONFIRMED | F-XS-003, F-ST1-005 |

## C001 — SMS transmission totals and phase schedules

Pending Human Adjudication.

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route B. B1: the randomized intervention's planned message dose/duration is an expressly permitted planned-versus-reported element. B2: each protocol paragraph pairs a per-participant total with a frequency schedule that cannot produce it even under widened half-unit allowances; pilot-refinement permission does not name the governing revised schedule. B3: the extractable intervention schedule attached to the primary six-month abstinence RR3.0 is unresolved. The issue is bounded to printed intervention specifications.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.16,53 and SAP p.80 vs REPORT DOC-001 pp.1,3

**Evidence state:** reproduced

**Finding IDs:** F-NUM-104, F-XS-005

**Qualifying route:** Route B

**Source and calculation audit:** Exact pages [protocol p.16](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=16>), [protocol p.53](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=53>), [SAP p.80](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=80>), [report p.1](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>) and [report p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) support all compared statements. For the earlier schedule, nominal minimum56×4+56×2+56/7=344; widened range[213,725.178571] versus178±.5 gives gap34.5/178=.193820. For the later schedule, nominal minimum288; widened range[171,636.607143] versus134±.5 gives36.5/134=.272388. Widening each two-month segment to1.5–2.5 months enlarges the feasible range, so enforcing the exact six-month sum cannot remove these lower-bound discrepancies. Later protocol month2 lower rate4/day±.5 versus report1/day±.5 gives gap2 and relative2.0. Report100+30+4=134 reconciles. No finding rests merely on the disclosed178→134 change.

**Classification rationale:** Prospective protocol and SAP content are PLAN; implemented intervention descriptions are REPORT. Internal protocol schedule/total contrasts and protocol–SAP contrast give P_P; protocol–report gives P_R, which has precedence. Agreeing report abstract/SAP passages corroborate the implemented side and do not create S_C.

**Classification ambiguity:** Unique templates or branching might differ from per-person transmissions; pilot refinement is expressly possible. Actual transmissions and the applied schedule revision are absent.

**Evidence-card completeness and impact audit:** Every affected protocol occurrence, report occurrence, SAP occurrence and amendment-context p.77 is already linked in the ledger. Missing logs/template definitions and the alternative interpretations are named; no delivered participant dose or change in efficacy is inferred. C001 consolidates repeated total/frequency mismatches. C003 instead concerns endpoint time anchors and dated reminders; the primary-start rule is distinct and remains separately registered. Potential reuse is limited to copying the intervention dose/calendar without identifying the governing revision. No supportable field omission or classification change is needed.

## C002 — Operational eligibility rules

Pending Human Adjudication.

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route B. B1: the explicitly planned recent-stop/reduction exception and the reported operational reader exclusion bear on the primary analysis population. B2: phone access is not an immediate equivalent of an available SMS reader, and the finite plan lists do not map the exception to the≥25-day condition. B3: eligibility definitions attached to the1080-participant primary trial can be copied differently. No changed participant count is inferred.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.11,49 vs REPORT DOC-001 pp.2,4 and DOC-003 p.3

**Evidence state:** reproduced

**Finding IDs:** F-XS-008

**Qualifying route:** Route B

**Source and calculation audit:** [PLAN p.11](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=11>) and [p.49](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=49>) permit smoking reduction/cessation since TB diagnosis and personal mobile access. [REPORT p.2](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2>) defines recent daily smoking by≥25days; [Figure1 p.4](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) and [eTable1 p.3](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=3>) give236 reader-related exclusions and7069 recent-smoking-related exclusions. This is finite-list matching, with no continuous-number precision comparison. Overlapping reasons prohibit deriving a uniquely additional236-person exclusion population.

**Classification rationale:** Planned prospective eligibility versus actual selection gives P_R/protocol_report. Report and results supplement agree on the exclusion and are corroborating locations, not an S_C conflict.

**Classification ambiguity:** Some recently reduced smokers could meet25days; a later operational amendment could govern. Criterion overlap and amendment provenance are missing.

**Evidence-card completeness and impact audit:** Complete plan lists, operational criteria and reason counts are linked; alternatives and overlap limitations are explicit. The report statement of daily smoking and its≥25-day definition alone would be terminology, but the planned reduction exception and actual reader exclusion supply the reproduced population-specification comparison. Potential reuse is limited to which eligibility rules are attributed to this primary trial. No numerical RR shift or population-size deficit is claimed. No field repair is needed.

## C003 — Quit-date anchor and reminder dates

Pending Human Adjudication.

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route B. B1: quit date defines the primary continuous-abstinence start, and the dated reminders define the randomized intervention calendar. B2: Q(−8), the ordinal8th-day wording and5days after enrollment are not mapped by the supplied clock definitions or immediate report description. B3: the extractable endpoint-start/intervention timing differs. Participant-level implementation and outcome reclassification are not inferred.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SMS log pp.101,103,104,109 vs REPORT DOC-001 p.3

**Evidence state:** reproduced

**Finding IDs:** F-XS-006

**Qualifying route:** Route B

**Source and calculation audit:** [REPORT p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) gives5days and monthly reminders in months3–6. [PLAN log p.101](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=101>), [p.103](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=103>), [p.104](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=104>) and [p.109](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=109>) contain enrollment Q(−8)/Tx(+1), Q(−1)/Tx(+8), ordinal quit day and final Q(+52),Q(+112),Q(+180) reminder dates. Eight versus five half-unit intervals give gap2/5=.40; inclusive ordinal counting could give seven elapsed days, still gap1/5=.20. Three versus four reminder counts touch under half-unit precision and do not independently qualify. The dates and clock mapping remain the basis.

**Classification rationale:** A prospective operational message log is PLAN by content; actual reported endpoint/intervention timing is REPORT. This is P_R/protocol_report. No plan-only clock contrast is registered separately.

**Classification ambiguity:** Joining, enrollment, quit-date and treatment clocks require a supplied crosswalk; ordinal counting and pilot refinement are alternative explanations.

**Evidence-card completeness and impact audit:** All dated-log occurrences, footnote definitions, reminder labels and report statements appear in the ledger/recheck. No silent normalization of ordinal8th-day to8elapsed days occurs. Impact is bounded to endpoint-start and calendar extraction; no changed abstinence count is demonstrated. The distinct primary time-anchor rule prevents treating this as an unmerged occurrence of C001's frequency-total rule. No repair is needed.

## C004 — Cotinine decision-specification crosswalk

Pending Human Adjudication.

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route B. B1: this compares explicit planned and implemented primary biochemical endpoint decision specifications. B2: the named graded NicAlert level<3 rule and binary-negative AllTest rule do not supply a common concentration definition; assay names do not establish equivalence. B3: the verification criterion attached to primary abstinence among concomitant smokeless-tobacco users cannot be extracted as a single supplied numeric criterion. This is not a demonstrated concentration change or changed event count.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.8,47,84 vs REPORT DOC-001 p.3

**Evidence state:** reproduced

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Source and calculation audit:** [PLAN p.8](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=8>), [p.47](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>) and [SAP p.84](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>) give0–6grades and level<3, described as100–200ng/mL. [REPORT p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) names a different assay and binary-negative decision. No AllTest concentration cutoff is printed, so no numeric difference or relative-discrepancy calculation is possible. The printed comparison is the endpoint decision specification, not a diagnostic test preference.

**Classification rationale:** Protocol/SAP endpoint rules are PLAN; the implemented endpoint procedure is REPORT. All relationships are P_R, hence protocol_report. Agreement among plan passages introduces no P_P.

**Classification ambiguity:** Equivalent classifications by the two assays remain possible. The cutoff crosswalk and applicable assay amendment are absent.

**Evidence-card completeness and impact audit:** Exact assays/decision outputs and absence of a crosswalk are source supported. The card explicitly separates this from a numerical threshold contradiction. Potential reuse is limited to attributing a primary verification threshold/procedure; it cannot establish actual reclassification or conclusion impact. Statistical-pass-1 exclusion13 addresses these same locations and should be linked to C004 as a duplicate of the bounded specification issue, while preserving its caution about an unestablished numerical difference. No candidate field or evidence-state change is needed.

## C005 — Primary model-family specification

Pending Human Adjudication.

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route A, category5: the planned Poisson/log-link primary analysis has no supplied reported counterpart, and SAP/report name logistic analysis for that categorical primary endpoint. SAP/report agreement or a possible superseding plan is an alternative explanation, not removal of this always-register planned-analysis comparison.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP pp.91,92 and REPORT DOC-001 p.3

**Evidence state:** reproduced

**Finding IDs:** F-XS-001, F-ST1-003

**Qualifying route:** Route A, category 5

**Source and calculation audit:** [Protocol p.28](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>) and [p.66](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>) explicitly name log link/Poisson with cluster random intercept andRRs. [SAP p.91](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), [p.92](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>) and [REPORT p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) name logistic mixed-effects analysis. The separately headed clinical statistical-analysis paragraph is not restricted by preceding economic prose. Log probability versus logit probability is a categorical method contrast, without display-precision arithmetic. Header/bundle order does not establish supersession; amendment p.77 supplies no model-family crosswalk.

**Classification rationale:** Protocol–SAP gives P_P; protocol–report gives P_R. P_R takes precedence, giving protocol_report. A physical supplement containing the plan remains PLAN.

**Classification ambiguity:** Final plan hierarchy, actual fitted family/link and whether a separate Poisson analysis exists remain unknown.

**Evidence-card completeness and impact audit:** Repeated protocol occurrences and SAP/report counterparts are consolidated; model provenance for primaryRR3.0/3.2 is named. No actual fitted model, preferable analysis, numerical efficacy change or conclusion consequence is inferred. C006 uses a separate method-to-estimand rule within report content and is not a second registration of this protocol-replacement rule. No repair is needed.

## C006 — Logistic-to-risk-ratio derivation

Pending Human Adjudication.

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route B. B1: a source-grounded model-to-effect-measure chain is statistical method logic. B2: logistic regression plus anRR label alone does not identify the required prediction/conversion or different fitted link, and immediate methods/table notes do not state one. B3: the conditional or marginal risk estimand attached to primaryRR3.0/3.2 and its uncertainty is unresolved. This is not a demonstration that a coefficient odds ratio was numerically printed as a risk ratio.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.3 method vs REPORT DOC-001 p.6 RR labels; REPORT DOC-003 pp.11,13,14 affected displays

**Evidence state:** reproduced

**Finding IDs:** F-ST1-002

**Qualifying route:** Route B

**Source and calculation audit:** [Main methods p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) state logistic mixed effects; [Table2 p.6](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) suppliesRR labels, primary3.0[2.0,4.9] and adjusted3.2[2.2,5.2]. [eTable7 p.11](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=11>), [eTable9 p.13](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>) and [notes p.14](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) repeat risk labels without the needed bridge. Exponentiating a logit treatment coefficient yields anOR; anRR can coherently arise from predicted risks, standardization or conversion, but the generating operation is unidentified. No comparison with unclustered crude ratios supplies the candidate and no numeric precision test can identify the missing operation.

**Classification rationale:** Main method-to-label comparison is inside one REPORT, giving S_W/statistical_results. Supplementary risk labels repeat affected output conventions; they do not conflict with main risk labels and therefore do not create S_C. A corroborating SAP is not a relationship.

**Classification ambiguity:** A legitimate predicted-risk derivation, another fitted link or separate analysis is possible. Conditional versus marginal estimand andCI construction are missing definitions.

**Evidence-card completeness and impact audit:** All affected displays, model text, printed primary results and source-grounded alternatives are preserved. Interpretation is bounded to which effect measure/estimand a data extractor copies, with no established odds-ratio relabeling or numerical correction. Numeric exclusion6's coefficient-relabeling hypothesis is itself conditional; its source context should also cross-reference the already included C006 method-logic issue without promoting that hypothesis. No field/state/classification repair is needed.

## C007 — Tobacco-use-form adjustment

Pending Human Adjudication.

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route A, category5: the explicitly planned tobacco-use-form term in the fully adjusted primary model has no counterpart in repeated finite reported adjustment lists or a separately supplied planned-model result. Possible omission from the description is an alternative, not evidence that the planned result was supplied.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP p.92 vs REPORT DOC-001 pp.3,4,6 and DOC-003 p.14

**Evidence state:** reproduced

**Finding IDs:** F-XS-003, F-ST1-005

**Qualifying route:** Route A, category 5

**Source and calculation audit:** [SAP p.92](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>) includes tobacco-use form. [Main p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), [p.4](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), [Table2 p.6](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) and [eTable9 notes p.14](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) repeatedly list age, sex, education, occupation and smoking duration. The finite-list comparison has no rounding operation. No effect of adding/removing the term is computed.

**Classification rationale:** Prospective SAP adjustment rule versus reported model descriptions gives P_R/protocol_report. Agreement among reported lists is corroboration, without S_C/S_W conflict.

**Classification ambiguity:** The term might be fitted but omitted in prose, aliased, intentionally removed or amended. Actual model formula, term mapping and planned-model result are absent.

**Evidence-card completeness and impact audit:** Primary adjustedRR3.2[2.2,5.2] and death-excluded adjustedRR3.1[1.9,6.5] are the named affected values. All repeated affected descriptions are consolidated. Potential reuse is confined to adjustment/prespecification metadata attached to those estimates; no actual fitted omission, confounding effect or changed clinical conclusion is established. No repair is needed.

## Audit of all initial screening decisions

Each original finding has exactly one original screening row. All29 INCLUDE rows map to a stable candidate; the single SCREENED_OUT row has one permitted reason. Consolidation preserves the distinct finding provenance. The table audits the original decision without overwriting it. The full source-confirmed facts for all19 IDs were considered for screening, while candidate-card responsibility remains C001–C007.

| Finding ID | Original decision / C ID | Audit outcome | Concrete threshold reason |
|---|---|---|---|
| F-NUM-001 | INCLUDE / C012 | Supported | Route B: 4.8% TB-attributed risk conflicts with32/1080≈3.0%; outcome attribution changes extraction. |
| F-NUM-002 | INCLUDE / C013 | Supported | Route A2: any-irritability/anxiety printed directions reverse the arm percentages beyond.05; severity alternative retained. |
| F-NUM-101 | INCLUDE / C017 | Supported | Route A3: two1(7.4%) cells versus27 deaths have relative gap.228327. |
| F-NUM-102 | INCLUDE / C018 | Supported | Route A4:5(7.5) fails the N40 rule fitting other death cells; relative gap.474815. |
| F-NUM-103 | INCLUDE / C019 | Supported | Route A2: positive.5 reverses the common signed failure contrast; relative gap1.367585. |
| F-NUM-104 | INCLUDE / C001 | Supported | Route B: per-person totals and transmission rates remain separated under widened precision allowances. |
| F-XS-001 | INCLUDE / C005 | Supported | Route A5: planned primary Poisson/log-link versus SAP/report logistic specification. |
| F-XS-002 | INCLUDE / C009 | Supported | Route B: separately headed broad MAR statement versus deterministic primary smoking-status assignment; economic restriction not explicit. |
| F-XS-003 | INCLUDE / C007 | Supported | Route A5: planned tobacco-form primary adjustment lacks a matched reported result/list term. |
| F-XS-004 | INCLUDE / C010 | Supported | Route A5: prespecified male/female primary effect analyses and unavailable-CI disclosure absent from complete report results. |
| F-XS-005 | INCLUDE / C001 | Supported | Route B: finalized protocol phase-specific message dose differs from SAP/report; same issue as F-NUM-104. |
| F-XS-006 | INCLUDE / C003 | Supported | Route B: primary quit-start anchor and dated intervention reminders lack a clock/revision crosswalk. |
| F-XS-007 | INCLUDE / C004 | Supported | Route B: explicit primary graded assay criterion versus implemented binary criterion lacks a common decision specification. |
| F-XS-008 | INCLUDE / C002 | Supported | Route B: planned reduction exception and reported reader exclusion affect primary eligibility; not inferred unique participant counts. |
| F-XS-009 | INCLUDE / C015 | Supported | Route B: competing month5/month6 plan windows define the abstract key-secondary failure result. |
| F-XS-010 | INCLUDE / C011 | Supported | Route B: current10%/20% primary-data assumptions remain different; gap9/10=.90. |
| F-XS-011 | INCLUDE / C016 | Supported | Route B: current primary power inputs16/18 intervention clusters have gap1/16=.0625; Phase4 remains peripheral. |
| F-XS-012 | INCLUDE / C012 | Supported | Route B: supplemental cause counts corroborate32TB/52total; mortality value attribution remains different. |
| F-XS-013 | INCLUDE / C013 | Supported | Route A2: same arm-direction pattern; supplement severity is a bounded alternative quantity. |
| F-ST1-001 | INCLUDE / C014 | Supported | Route A4:14 rows exceed.05 under the rule fitting other rows; literal42 and nonsymmetric-method alternative retained. |
| F-ST1-002 | INCLUDE / C006 | Supported | Route B: source-grounded model-to-RR bridge unidentified, distinct from an assumed coefficient-relabeling calculation. |
| F-ST1-003 | INCLUDE / C005 | Supported | Route A5: same planned-primary model-family comparison, consolidated. |
| F-ST1-004 | INCLUDE / C009 | Supported | Route B: same primary missing-outcome architecture comparison, consolidated. |
| F-ST1-005 | INCLUDE / C007 | Supported | Route A5: same planned fully adjusted primary model comparison, consolidated. |
| F-ST1-006 | INCLUDE / C010 | Supported | Route A5: same unreported prespecified primary gender analyses, consolidated. |
| F-ST1-007 | SCREENED_OUT / — | Supported | CONDITIONAL_OR_UNREPORTED: country-stratified lists can implement country/volume minimization; no incompatible algorithm or result is printed. |
| F-ST1-008 | INCLUDE / C008 | QUESTIONED | Primary-construct blocks contain CO<6 sensitivity analyses, while main p.3 and supplement table title expressly state post hoc sensitivity. An actual status promotion is unestablished (Route A5), and immediate context resolves the grouping (Route B2). Original INCLUDE and stable C008 remain unchanged. |
| F-ST1-009 | INCLUDE / C016 | Supported | Route B: same current Phase3 cluster/power comparison; disclosed amendment does not label retained paragraph historical. |
| F-ST1-010 | INCLUDE / C011 | Supported | Route B: same current primary-data attrition input comparison; no alternative power calculation inferred. |
| F-ST1-011 | INCLUDE / C015 | Supported | Route B: same categorical key-secondary failure-window comparison; no observed event reclassification inferred. |

No initial SCREENED_OUT finding independently qualifies. No stable candidate rests solely on a display-zero P value. Initial-screen provenance and explicit statements support absence of a count target in screening; discovery-control verification belongs to the coverage audit part.

## Audit of all initial checker excluded observations

The row keys below are audit locators, not finding IDs. NUM-01–NUM-20 cover the8 main numeric rows plus12 support numeric rows; XS-01–XS-11 cover all11 cross-source rows; ST1-01–ST1-14 cover all14 statistical-pass-1 rows. Each row has one final audit reason code. Original checker records are preserved unchanged. A duplicate crosswalk to a stable included issue is not a new scientific issue and does not change the original30-finding denominator.

| Audit locator / source provenance | Observation or exact location | Audit reason code | Independent rationale / precision check |
|---|---|---|---|
| NUM-01 / numeric_consistency | Main p.4 exclusion reasons total above8152 | CONTEXT_RESOLVES | Figure1 footnote expressly permits multiple reasons; no exclusive partition conflict. |
| NUM-02 / numeric_consistency | Main p.5 low-addiction514(75.7),212(65.0) | NOT_REPRODUCED | Cigarette-user679/326 populations reproduce percentages; full-arm denominator assumption is unsupported. |
| NUM-03 / numeric_consistency | Main p.5 TB-stage totals100.1% | ROUNDING_OR_DISPLAY_PRECISION | Counts partition720/360; independent percentage half-units permit rounded sum100.1%, with no reproduced gap above.05. |
| NUM-04 / numeric_consistency | Main pp.4,5 average versus median smoking summaries | TERMINOLOGY_OR_WORDING | Same numbers and immediate table summary labels identify the quantity; no numerical contradiction. |
| NUM-05 / numeric_consistency | Main pp.3,6 modelRR versus aggregate risk ratio | MODEL_VERSUS_CRUDE | Explicit clustering/model context permits model-based estimates; aggregate ratio is not the identified generating method. |
| NUM-06 / numeric_consistency | Main pp.3,6 logistic/RR coefficient-relabeling hypothesis | DUPLICATE_OF_INCLUDED | Cross-reference C006's bounded method-to-measure gap. The distinct claim that a coefficient OR was printed asRR remains unestablished and is not added to that card. |
| NUM-07 / numeric_consistency | Main pp.1,5,6 treatment-failure2/360 versus.5% | ROUNDING_OR_DISPLAY_PRECISION | Required range[.416089,.695410]% overlaps[.45,.55]%; relative gap0. |
| NUM-08 / numeric_consistency | Main pp.5,6 TB outcome sums691/344 | CONDITIONAL_OR_UNREPORTED | Display is not declared exhaustive; a partition equality would require an unstated category rule. |
| NUM-09 / numeric_consistency | Supplement p.3 ineligibility reasons13856 versus8146 | CONDITIONAL_OR_UNREPORTED | Reasons need not be mutually exclusive; no printed exclusivity requirement or primary population mismatch. |
| NUM-10 / numeric_consistency | Supplement p.4 absent site2012 quit-attempt row | PERIPHERAL_COMPARISON | Baseline descriptive omission does not change a primary/key-secondary result or analysis-population size. |
| NUM-11 / numeric_consistency | Supplement p.5 monthly mean sums versus174.3/178.0 | ROUNDING_OR_DISPLAY_PRECISION | Direct source sum29.87+29.59+29.39+29+28.56+27.88=174.29, rather than the checker handoff's174.19. Half-unit range[173.765,174.815] overlaps[174.25,174.35]. Control sum177.7 has range[177.4,178.0], overlapping[177.95,178.05]. Both relative gaps0; preserved original observation needs an audit arithmetic correction. |
| NUM-12 / numeric_consistency | Supplement pp.6,8,15,16 small percentages | ROUNDING_OR_DISPLAY_PRECISION |8/52 at15.2% gives[14.285714,16.504854]%;40/527 at7.5% gives[7.488152,7.692308]%; both overlap. Whole/one-decimal symptom outputs and counts likewise fit inputs or remaining gaps≤.05. C017/C018 retain distinct qualifying cells. |
| NUM-13 / numeric_consistency | Supplement pp.3,8 screen9232 versus site sum9240 | ROUNDING_OR_DISPLAY_PRECISION | Even treating9240 as one integer copy gives gap7/9232=.000758; permitting independently rounded constituents only widens feasible inputs. |
| NUM-14 / numeric_consistency | Supplement pp.15,16 epigastric698 versus other symptom699 | ROUNDING_OR_DISPLAY_PRECISION | Integer-copy half-unit ranges touch, gap0; no explicit shared denominator is printed. Percentage fits cannot establish a discrepancy above.05. |
| NUM-15 / numeric_consistency | Supplement pp.13,14 modelRR versus unclustered ratio | MODEL_VERSUS_CRUDE | Mixed-effects/ICC context does not identify the simple participant ratio as the reported computation. |
| NUM-16 / numeric_consistency | Plan pp.63,64 printed704,1036,1080,1620 products | ROUNDING_OR_DISPLAY_PRECISION | Rounded input products: [700.8675,707.9375] for587×1.20;[1031.8825,1041.7225] for864×1.20;[1051.7325,1060.2725] for704×1.50;[1610.2025,1622.1225] for1036×1.56. First,second,fourth overlap outputs; third relative gap.017803≤.05. |
| NUM-17 / numeric_consistency | Plan p.62 pilot in-each-site wording | TERMINOLOGY_OR_WORDING | Adjoining diagram and first16 pilot statement resolve the aggregate count; it does not define reported primary allocation. |
| NUM-18 / numeric_consistency | Plan p.64 Phase3 label inside Phase4 diagram | TERMINOLOGY_OR_WORDING | Phase4 title, arm labels,36sites and1620 participants resolve phase; no changed numeric rule. |
| NUM-19 / numeric_consistency | Plan p.85 MPSS five domains/5-point scale/5–35 | TERMINOLOGY_OR_WORDING | Scale wording supplies no reconstructable reported participant statistic; plan-internal peripheral instrument description is outside statistical-design elements relied on by the reported primary analysis. |
| NUM-20 / numeric_consistency | Plan pp.54,55 TAM30% versus20% | PERIPHERAL_COMPARISON | Unreported process-substudy target does not change a reported primary/key-secondary result, analysis population or decision rule. |
| XS-01 / cross_source_consistency | Main pp.3,6 versus SAP pp.91,92 PP/complete-case label | TERMINOLOGY_OR_WORDING | Exact667/318 denominators and omission rule identify available-primary-outcome sensitivity at once. |
| XS-02 / cross_source_consistency | Main pp.3,6/supplement p.13 CO<6 primary block | TERMINOLOGY_OR_WORDING | Immediate main post hoc statement and supplemental post hoc table title support grouping sensitivities of the primary construct. C008 inclusion is QUESTIONED; actual formal outcome promotion is unestablished. |
| XS-03 / cross_source_consistency | Plan pp.27,65 economic additional quitter called secondary | TERMINOLOGY_OR_WORDING | Economic passage does not identify a competing continuous-abstinence result or changed primary endpoint status. |
| XS-04 / cross_source_consistency | Plan pp.47,84 exactCO10 override not named | CONDITIONAL_OR_UNREPORTED | Strict<10 positive criterion identifies success; no observed exact10 classification is printed in conflict. |
| XS-05 / cross_source_consistency | Plan pp.13,51 versus main p.2 minimization/stratification | CONDITIONAL_OR_UNREPORTED | No incompatible implemented randomization algorithm is supplied; original F-ST1-007 remains screened out. |
| XS-06 / cross_source_consistency | Plan pp.11,49 retreatment omitted in shortened report wording | CONDITIONAL_OR_UNREPORTED | No printed enrolled-retreatment count or incompatible population exists; omission differs from C002's actual operational criteria. |
| XS-07 / cross_source_consistency | Plan p.55 TAM target discrepancy | PERIPHERAL_COMPARISON | Same unreported process-substudy comparison as NUM-20, outside the permitted result/design tier. |
| XS-08 / cross_source_consistency | Plan pp.51,63,77,83 1096/1080 and2716/2700 | ROUNDING_OR_DISPLAY_PRECISION | Half-unit gaps15/1080=.013889 and15/2700=.005556≤.05; no separate ITT rule change is established. |
| XS-09 / cross_source_consistency | Main p.7 lowest graphical point versus supplement p.8 zero site | NOT_REPRODUCED | No exact plotted value or source-ID crosswalk identifies a unique matched numeric conflict. |
| XS-10 / cross_source_consistency | Plan pp.85,92,97 absent additional results | CONDITIONAL_OR_UNREPORTED | None is abstract-reported or designated primary/key-secondary, and no contrary reported status/composite is identified. Gender primary analyses are separately C010. |
| XS-11 / cross_source_consistency | SAP p.91 promised primary-model P value omitted from main p.6 | CONDITIONAL_OR_UNREPORTED | RR/CI supplied; absent statistic alone is not a replaced analysis or conflicting printed interval/P/test. |
| ST1-01 / statistical_pass_1 | Main p.6/supplement pp.11–14 modelRR versus counts | MODEL_VERSUS_CRUDE | Same model-versus-simple-ratio distinction; no method that generates the printed values is contradicted by these aggregate ratios. |
| ST1-02 / statistical_pass_1 | Plan pp.63,64 initial n587/864 versus diagnostic540/969 | CONDITIONAL_OR_UNREPORTED | Unspecified original equation/software is not replaced by a diagnostic normal approximation; no reproducing same-display method established. |
| ST1-03 / statistical_pass_1 | Plan pp.63,64 additive versus division attrition inflation | ROUNDING_OR_DISPLAY_PRECISION | Additive rule explicitly reproduces. Even counterfactual exact-number comparisons give≤.043, below.05 before allowing intervals; no route A contradiction. |
| ST1-04 / statistical_pass_1 | Plan pp.63,64,83/main p.3 products/design effects | ROUNDING_OR_DISPLAY_PRECISION |704×1.50 input product[1051.7325,1060.2725] versus1080±.5 gives.017803; Phase4 product overlaps1620±.5;1.56 versus1.50 gives.05/1.50=.033333. All≤.05. |
| ST1-05 / statistical_pass_1 | Main p.6/supplement p.12 other log-symmetry rows | ROUNDING_OR_DISPLAY_PRECISION | Listed relative gaps .01622,.04562,.03983,.03053,.000571,.043561,.012204,.017970 are all≤.05;14 above-threshold rows remain C014. No interval/P or stated-test conflict is used. |
| ST1-06 / statistical_pass_1 | Main pp.6,8 ICC.18/.19 | ROUNDING_OR_DISPLAY_PRECISION | [.175,.185] and[.185,.195] touch, gap0. |
| ST1-07 / statistical_pass_1 | Main pp.3,6 PP/complete case | TERMINOLOGY_OR_WORDING | Methods and exact denominators define the same set; no unclear extracted result. |
| ST1-08 / statistical_pass_1 | Main p.5/supplement p.11 modified/prognostic wording | TERMINOLOGY_OR_WORDING | Immediate covariate-predictor context has no claimed interaction statistic or competing primary effect. |
| ST1-09 / statistical_pass_1 | Main pp.3,7 Bayesian prior/MCMC/graphical endpoints absent | CONDITIONAL_OR_UNREPORTED | No printed probability or method claim conflicts; exact numeric graphical endpoints are not supplied. |
| ST1-10 / statistical_pass_1 | Plan pp.85,86,91,92,97 absent non-key analyses | PERIPHERAL_COMPARISON | Non-key omissions alone do not fit route A5; separately planned primary gender analyses are included as C010. |
| ST1-11 / statistical_pass_1 | Plan pp.64,65,83 Phase4 18/18 versus20/20 | PERIPHERAL_COMPARISON | Separately unreported noninferiority-phase allocation is peripheral to reported Phase3; C016 is limited to Phase3 power inputs. |
| ST1-12 / statistical_pass_1 | Supplement pp.15,16 Pearson diagnostic statistics | ROUNDING_OR_DISPLAY_PRECISION | Exact-count diagnostic versus printed-half-unit gaps: dry mouth(31.842−31.25)/31.2=.018974;headache(2.787−2.75)/2.7=.013704;insomnia(6.991−6.95)/6.9=.005942. All≤.05. Exact-test-marked rows are distinct analyses; significance/interval-P contradictions are not rounded away. |
| ST1-13 / statistical_pass_1 | Plan p.84/main p.3 cotinine decision criterion | DUPLICATE_OF_INCLUDED | C004 already includes the bounded explicit criterion comparison through Route B. Missing numeric cassette cutoff prohibits claiming a numerical threshold change but does not create another issue. |
| ST1-14 / statistical_pass_1 | Plan pp.8,47,84 exactCO10 override | CONDITIONAL_OR_UNREPORTED | Definite primary<10 criterion with no supplied exact10 observation in conflict; same distinction as XS-04. |

All13 ROUNDING_OR_DISPLAY_PRECISION exclusion rows were explicitly checked against the.05 rule. None has a reproduced interval-versus-P-value/stated-test conflict, a point outside its interval, or another route A1 observation. The Pearson diagnostic differences are statistic-to-recomputed-statistic comparisons within precision, not permission to exclude a stated test/interval incompatibility. Exact-test superscripts on supplement pp.15,16 prevent an assumed common Pearson df from supplying a test conflict.

## Audit repairs and coordinator actions

| Repair/action | Reason | Required bounded action |
|---|---|---|
| Inclusion fields for C001,C002,C003,C004,C005,C006,C007 | Fresh audit reproduces facts and threshold routes | Coordinator sets each ledger table/card Inclusion audit to CONFIRMED, preserves all stable IDs, and propagates identical fields to report cards. |
| Numeric exclusion NUM-06 duplicate crosswalk | Same supplied method/label locations support included C006; coefficient-relabeling hypothesis remains unsupported | Preserve original checker exclusion text/code and add the audit crosswalk to C006 with final audit reason DUPLICATE_OF_INCLUDED. Do not add the numeric coefficient hypothesis to C006 or append a stable ID. |
| Statistical exclusion ST1-13 duplicate crosswalk | Same supplied primary criterion locations are already included in C004 through Route B | Preserve original exclusion and add audit crosswalk to C004 with DUPLICATE_OF_INCLUDED. Keep concentration inequivalence and event reclassification unasserted. |
| F-ST1-008/C008 inclusion premise QUESTIONED | Source-confirmed post hoc language and table title support grouping under the primary construct without establishing a status promotion | Preserve the original INCLUDE row and stable C008; record the bounded inclusion-audit concern and exact source alternative. No deletion, suppression, new candidate or scientific disposition. |
| NUM-11 monthly mean sum | Direct source inputs sum174.29 rather than174.19 in the excluded-observation handoff | Preserve the original checker artifact and record this audit arithmetic correction; rounded-input intervals still overlap the total, so ROUNDING_OR_DISPLAY_PRECISION remains. |
| ST1-12 diagnostic rounding detail | Initial exclusion uses rounded diagnostic values but does not show all direct relative-gap arithmetic | This part supplies reproducible approximate diagnostic gaps .018974,.013704,.005942; all remain≤.05. No screening decision changes. |

No F-QA new issue is emitted. No initial-screen audit override is needed for F-ST1-007. Duplicate observation crosswalks preserve provenance and original-finding coverage rather than adding another screening decision for an existing finding.

## Limitations and boundaries

This part audits supplied-source recheck facts and seven additional images; complete direct-source mapping/provenance closure is owned by other fresh audit parts. Final report equality must be checked after report assembly by the coordinator. Actual intervention delivery logs, final operational amendments, assay equivalence, fitted model formulas, risk-ratio conversion, row-specific interval methods, final plan hierarchy and participant-level outcomes are unavailable. These omissions limit explanations and human questions, not evidence transcription. No paper-level conclusion consequence or downstream propagation is demonstrated. Potential reuse claims remain limited to named values, endpoint/eligibility definitions, intervention schedules or model metadata a data extractor could copy. All seven IDs remain Pending Human Adjudication; no severity or scientific disposition is assigned.
