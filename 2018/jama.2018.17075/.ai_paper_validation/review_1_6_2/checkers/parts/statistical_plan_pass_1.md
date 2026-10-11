# Statistical pass 1 — PLAN method/design shard

- Runtime agent: 01a129bb-2346-7d93-89e3-266a9f7a3f14.
- Model / effort / start mode: gpt-6.1-sol / high / FRESH_SPAWN.
- Pass record: PASS_1_COMPLETE.
- Exact scope: DOC-002 physical PDF pp.1–194, PLAN statistical design and method relationships, with supplied DOC-001 methods pp.2–4 as REPORT comparators. Monitoring printed inferential/count rows pp.189–194 belong to a separate high shard; this shard covers their method, population and decision-rule definitions.
- Stable relationships: 82, S401–S482; each explicitly PASS_1_COMPLETE in statistics/parts/plan.md.
- Findings: 5, F-ST1-201–F-ST1-205. Excluded observations: 17.
- Complete QUALITY_CONTROL_SCOPE.md and review contract read. Source-linked current-run mapper assets only; no old conclusions, candidate IDs, external SAP text, web, or raw-data assumptions.

Source authority: exact supplied PDF text via direct Poppler pdftotext25.03.0; source-matched reusable text/images serve as locators. All four current-run plan maps were read, original shardA before its full raw-source appendix; administrative/background/pointer units retain complete page accounting. Images pp.152,183,187 inspected. A fresh CPU direct pdftoppm25.03.0 stdout-only rendering of p187 at220dpi confirmed an apparent mapper inequality discrepancy as '<48', so it is not emitted. No durable derivative produced. Direct source p69,p77,p83–86,p97–101,p108–110,p118–119,p132,p139,p174–175,p178–180,p188 and REPORT pp3–4 opened for source-grounded checks.

Evidence links resolve from this part directory. Coordinator canonical merge should preserve truthful supplied-PDF links and physical page anchors. Proposed classifications are for independent screening and recheck; no adjudication or correction is assigned.

## Findings

### F-ST1-201

**Title:** Final protocol gives different anchors for the required hypothermia duration.

**Relationship:** S416. **Focus area:** D. **Proposed review domain:** plan_material. **Proposed primary/all relationships:** P_P / P_P.

**Compared locations and document roles:** PLAN [DOC-002 p69, final protocol V9 §6.5 synopsis](../../../../joi180132supp1_prod.pdf#page=69); PLAN [p77 §12.11](../../../../joi180132supp1_prod.pdf#page=77); PLAN [p97 §26.3.1](../../../../joi180132supp1_prod.pdf#page=97); PLAN [p99 §26.4 flowchart and late-cooling footnote](../../../../joi180132supp1_prod.pdf#page=99).

**Printed statements:** p69 reaches33°C and then maintains that temperature 'for a further72hours'. p77 assesses rewarming72hours after randomization. p97 describes72hours after severe head injury. p99 starts with '72hours post randomisation?' and says late cooling requires a minimum48hours of cooling before considering rewarming. All occur in the same final V9 dated11July2017.

**Rule and calculation:** A duration following attainment of33°C differs from elapsed time following randomization or injury. Let r be randomization and c>r attainment of33°C. The synopsis implies earliest ordinary rewarming c+72h; the detailed rule gives a randomization threshold r+72h, with late-cooling minimum c+48h and the clinical stability conditions. These are different interventions even when all stability conditions are satisfied. For a source-permitted delayed attainment more than24h after randomization, the late-cooling footnote can permit rewarming after48h actual cooling while the synopsis requires72h. This is a logical schedule comparison, not an inferred patient-level duration or subtraction of group medians. Both displayed integer durations have intervals [47.5,48.5] and [71.5,72.5]; their gap23h/72h=.3194, above.05. Injury versus randomization alone would differ by at most the enrollment window and is not the basis of the finding.

**Qualifying route:** Route B.

**Affected result or extracted value:** The randomized intervention's required hypothermia duration used to characterize the six-month favorable-GOSE comparison and adherence to sustained cooling.

**Why context does not resolve it:** The same final protocol contains the competing anchors and a48h minimum; no amendment in the supplied bundle says that its synopsis was superseded within V9. The schedules cannot be represented by one duration after target attainment.

**Alternatives and missing definition:** The detailed randomization-based bedside rule could govern practice while the synopsis describes an ideal target. Clinical instability can extend either schedule but does not reconcile different eligible starts. Missing definition: which time anchor and minimum actual duration define the final planned randomized intervention for interpretation and extraction.

**Exact human question:** Which V9 duration rule governed the planned intervention:72h after achieving33°C,72h after randomization with a48h late-cooling minimum, or72h after injury?

### F-ST1-202

**Title:** The final protocol and report give different durations of normothermic management after rewarming.

**Relationship:** S417. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R, P_P.

**Compared locations and document roles:** PLAN [DOC-002 p77 §12.11](../../../../joi180132supp1_prod.pdf#page=77), PLAN [p101 §26.5.1](../../../../joi180132supp1_prod.pdf#page=101); REPORT [DOC-001 p3 Rewarming](../../../../jama_cooper_2018_oi_180132.pdf#page=3), REPORT [p1 abstract intervention](../../../../jama_cooper_2018_oi_180132.pdf#page=1).

**Printed statements:** PLAN p77 says after reaching37°C, hypothermia-arm patients remain normothermic below38°C using pads up to a maximum7days or earlier ICU discharge. PLAN p101 says after reaching37°C, they remain normothermic using pads 'for96hours post randomisation', after which ward protocol governs, and repeats a96h pyrexia-avoidance window for all patients. REPORT p3 says once37°C is reached, automated surface cooling maintains normothermia if required 'for up to7days postrandomization'; REPORT abstract says temperature was managed7days in both groups.

**Rule and calculation:** A postrandomization device-management window of96h equals4d, whereas7d equals168h. The integer rounded windows [95.5,96.5]h and [156,180]h (allowing7d its full half-day interval) remain separated by59.5h; relative gap against96h=.6198>.05. This concerns the planned period, not actual required device use in an individual patient. No inference about body temperature after pads were discontinued is made.

**Qualifying route:** Route B.

**Affected result or extracted value:** The planned duration of randomized temperature management and the comparator/intervention definition extracted alongside six-month favorable-GOSE and mortality results.

**Why context does not resolve it:** Both PLAN statements occur in finalV9, and its appendix explicitly assigns ward protocol after96h. REPORT describes a7d window. Neither early ICU discharge nor the words 'if required' make the maximum planned management windows equal.

**Alternatives and missing definition:** p101 could retain an older bedside guidance window, or seven-day management could continue under ward protocol beyond the mandated96h device period. Missing definition: whether96h or7d is the protocolized temperature-management duration after randomization and whether the7d report includes management outside the randomized protocol.

**Exact human question:** Which temperature-management window applies to the reported trial: mandated surface-pad normothermia through96h, management through7d, or a defined combination of these?

### F-ST1-203

**Title:** The reported planned rewarming rate exceeds the final protocol's stated recommended maximum.

**Relationship:** S418. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary/all relationships:** P_R / P_R.

**Compared locations and document roles:** PLAN [DOC-002 p77 §12.11](../../../../joi180132supp1_prod.pdf#page=77); PLAN [p99 §26.4](../../../../joi180132supp1_prod.pdf#page=99); PLAN [p100 §26.5](../../../../joi180132supp1_prod.pdf#page=100); REPORT [DOC-001 p3 Rewarming](../../../../jama_cooper_2018_oi_180132.pdf#page=3). Original PLAN [p21 §12.11](../../../../joi180132supp1_prod.pdf#page=21) supplies an alternative version context only.

**Printed values:** Final PLAN p77 active gradual rewarming0.17°C/h and 'recommended maximum'0.5°C every3h; p99 rate aim0.17°C/h; p100 same schedule and approximately24h from33to37°C, with slowing0.2°C per2h and emergency faster rates at intensivist discretion. REPORT p3 gradual controlled rewarming 'at a target rate up to0.25°C/h'. Original protocol uses0.25°C/h.

**Rule and calculation:**0.5°C/3h=.1667°C/h agrees with printed0.17. A reported routine target up to0.25°C/h is greater than the final recommended maximum. Allowing0.17 and0.25 their half-hundredth intervals gives [.165,.175] and [.245,.255]; gap.070/.17=.4118>.05. This is a printed planned-rate comparison, not an assertion that patients actually rewarmed at the maximum.

**Qualifying route:** Route B.

**Affected result or extracted value:** The planned randomized intervention's rewarming rate used to characterize early sustained cooling and its six-month neurologic comparison.

**Why context does not resolve it:** The reported rate matches the original rather than final protocol. The final plan distinguishes emergency faster rewarming from its routine maximum; the REPORT paragraph presents0.25 as the ordinary target without that qualification. No supplied later amendment explicitly restores the original routine rate.

**Alternatives and missing definition:** 'Up to0.25' could be an outer safety ceiling encompassing the actual0.17 target, or it could reflect the original procedure. Emergency faster rewarming is expressly allowed in the final plan and is not itself questioned. Missing definition: whether0.25 was an amended routine ceiling, an umbrella bound, or only an emergency allowance.

**Exact human question:** What routine rewarming target and maximum governed the trial, and how does the reported up-to0.25°C/h rate relate to finalV9's0.17°C/h recommended maximum?

### F-ST1-204

**Title:** The report's primary analysis-population description omits a final-protocol exclusion class.

**Relationship:** S425. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary/all relationships:** P_R / P_R.

**Compared locations and document roles:** PLAN [DOC-002 p84 §15.2](../../../../joi180132supp1_prod.pdf#page=84); PLAN [pp174–175 V8 amendment, Section15](../../../../joi180132supp1_prod.pdf#page=174); REPORT [DOC-001 p3 Statistical Analysis](../../../../jama_cooper_2018_oi_180132.pdf#page=3); REPORT [p4 Patient Characteristics](../../../../jama_cooper_2018_oi_180132.pdf#page=4).

**Printed statements:** Final PLAN p84 includes all randomly assigned patients except those withdrawing all-data consent AND those not fulfilling inclusion criteria and never receiving intervention. V8 amendment explicitly calls this modifiedITT and describes alcohol/drug-associated altered consciousness instead of TBI as a possible member of the latter class. REPORT p3 says all a-priori analyses by randomized group, excluding consent withdrawals unless otherwise indicated. REPORT p4 says11 consent withdrawals leave500 evaluable; eligibility exclusions are described for PP/as-treated analyses separately.

**Rule and calculation:** The specified full-analysis sets differ: PLAN randomized minus consent withdrawals minus not-eligible-and-never-intervention patients; REPORT randomized minus consent withdrawals. REPORT511−11=500 reproduces its stated set. The supplied report does not quantify whether the second exclusion class is empty in the primary set. The finding is the printed membership-rule contrast, not a claim that a known number of participants must be removed or that the500 count fails arithmetic. Display precision does not apply to a set-definition change.

**Qualifying route:** Route B.

**Affected result or extracted value:** The intended primary favorable-GOSE analysis population and interpretation of the reported randomized comparison as fullITT or modifiedITT.

**Why context does not resolve it:** The final protocol and disclosed amendment explicitly retain the extra exclusion, while the report distinguishes eligibility restrictions only in sensitivity populations. The numerical511−11 description does not explain whether the planned excluded class was empty, removed elsewhere, or retained.

**Alternatives and missing definition:** There may have been no participant meeting BOTH noneligibility and never-intervention criteria, so realized sets coincide. A later published SAP could amend the rule, but only its pointer is supplied and its contents cannot be assumed. Missing definitions: occurrence/count of this class in the primary population and any final supplied amendment to its exclusion rule.

**Exact human question:** Did the primary analysis apply the final protocol's not-eligible-and-never-intervention exclusion, and if so, was that class empty or excluded separately from the11 consent withdrawals?

### F-ST1-205

**Title:** The DSMC charter's printed approximate P threshold does not match its stated normal three-SD monitoring boundary.

**Relationship:** S437. **Focus area:** D, B. **Proposed review domain:** plan_material. **Proposed primary/all relationships:** P_P / P_P.

**Compared locations and document roles:** PLAN [DOC-002 p188 Statistical Monitoring Guidelines](../../../../joi180132supp1_prod.pdf#page=188), normal-binomial boundary paragraph; PLAN [p84 §15.1.3 two-sided-tests definition](../../../../joi180132supp1_prod.pdf#page=84) supplies the overall plan's sidedness context. The source's2015 charter transcript is supplied as part of the plan bundle.

**Printed values:** Conventional Haybittle–Peto three-standard-deviation boundary '|Zk|≥3', calculated from a normal approximation to the discrete binomial difference, followed by '(approximate P<0.001 in both cases)'. The source says the two interim analyses assess dichotomized GOSE or mortality at DSMC discretion.

**Rule and calculation:** Under the explicitly stated standard-normal approximation, at|Z|=3 the two-sided tail probability2[1−Φ(3)]=.002699796, and even the one-sided tail is.001349898; neither is below.001. P<.001 corresponds to|Z|>3.290527 for a two-sided rule, rather than3. These calculations use the source's normal approximation, not an inferred exact binomial test. Display-precision cannot exclude a routeA interval/P/test conflict; even allowing a printed.001 threshold interval [.0005,.0015], the two-sided.002699796 probability remains separated by.001199796, relative1.199796>.05.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The efficacy/safety stopping threshold a reviewer extracts for the planned interim primary neurological or mortality monitoring.

**Why context does not resolve it:** This is the routeA test/P category. The statement's word 'approximate' and the overall conservative nature of the boundary do not make these numerical normal-tail thresholds the same.

**Alternatives and missing definition:** The three-SD Z rule may have governed practice, with '<.001' meant as a qualitative shorthand; alternatively an intended P<.001 boundary would require a larger criticalZ. Discrete tests can have different tail probabilities, but the supplied rule expressly specifies the normal approximation. Missing definition: whether Z≥3 or the printed P<.001 is the operative threshold.

**Exact human question:** Which stopping threshold governed the two stated interim analyses, |Z|≥3 or P<.001, and what sidedness/test definition gives the charter's printed P approximation?

## Excluded observations

Only apparent issues not emitted appear here. Reconciled checks without an apparent issue remain in the S inventory. Every row has exactly one reason code.

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-002 pp27,83; REPORT p3 |80% versus82% primary power, with different software/test approximations possible; discrepancy below5% and no reproducible precise-method conflict. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 pp83–84; REPORT p4 |Final significance .0459 versus displayed .05: copy intervals [.04585,.04595] and [.045,.055] overlap. Exact borderline stopping/decision applicability remains a named limitation, without asserting a reported significance reversal. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p84 vspp85–86 |Eleven endpoint tests versus six monitoring occasions: five dual-endpoint occasions plus one mortality-only occasion gives11; prose mixes counts of endpoints and occasions. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 pp15,19,144 |Original ICU-discharge secondary mortality absent final plan: V2→3 explicitly deletes it, so versions are not conflicting simultaneous specifications. | NOT_REPRODUCED |
| PLAN DOC-002 pp15,19,140,72–73 |Original AQOL8 versus final SF12: supplied amendment explicitly replaces instrument. | NOT_REPRODUCED |
| PLAN DOC-002 pp22,78,139,144,148; REPORT p4 |Original planned run-in count versus eight realized nonrandomized run-in participants: different versions and planned versus realized administrative count. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp72–73; REPORT pp3–4 |Prespecified secondary outcomes called exploratory for interpretation because no multiplicity adjustment; they remain labeled secondary in the REPORT outcome definition. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 pp72–73,84; REPORT p3 |Sliding-dichotomy/QOL/cost-effectiveness/CACE expressly not reported here, but supplied sources do not designate these as key secondary or put their results in abstract; omitted ordinary secondary output alone is outside required key-secondary omission category. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp25,81 vspp19,72; REPORT pp2–3 |Six-month injury versus randomization anchor differs by≤3h enrollment window and is immediately understandable for this follow-up. | CONTEXT_RESOLVES |
| PLAN DOC-002 p73; REPORT p4 |'Interaction' between time-to33°C and GOSE in cooling arm versus χ² association: intended within-arm outcome association is clear, no second interaction factor specified. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 pp84–85; REPORT pp3–4 |Absent full externally published SAP leaves exact prespecified covariate list unavailable; no printed statement conflicts merely because REPORT names IMPACT-TBI. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 p183,p187Figure2 |MapperPD053 transcribed hypothermia-to-standard early-death cooling '>48h'; exact source direct render prints '<48h' and agrees with update prose. | NOT_REPRODUCED |
| PLAN DOC-002 pp183,187 |Exactly48h compliance boundary not separately described; no actual reported classification/value at the boundary supplied. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp85–86; REPORT p3 |SAE ascertainment through7d after treatment cessation compared with adverse-event outcomes within10d: different defined quantities, no matched-window conflict. | NOT_REPRODUCED |
| PLAN DOC-002 p132 |PK appendix AUC adds concentration multiplied terminalslope, dimensional gap if slope is1/h; separate unreported substudy does not govern a parent reported result or decision rule. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp99–100 vsp131 |Propofol appendix 'passively rewarm' versus parent active rewarming: separate observational substudy description; no supplied parent result relies on that appendix wording. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 p177 vspp174–175 |Version8 adoption filename/header date difference without changed inference, population or decision rule. | PERIPHERAL_COMPARISON |

## Limitations and full-check closure

Published SAP full text and published protocol full text are external pointers only; their contents were not retrieved or inferred. Exact East design inputs/output, baseline multinomial category probabilities for ordinal power, within-subject covariances for substudies, and raw participant data are absent. These limit exact reproduction but do not create findings without source conflict. Standard-normal power calculations in S427,S462–463,S466,S469,S471 are labeled diagnostics and do not replace the source's analysis. No primary/key-secondary estimate, CI, P value or SE in the final report was independently checked by this method shard; those relationships belong to its companion high shards, including a separately commissioned monitoring-value shard. All82 assigned method/design relationships are PASS_1_COMPLETE. No coverage gap remains in this assigned scope.
