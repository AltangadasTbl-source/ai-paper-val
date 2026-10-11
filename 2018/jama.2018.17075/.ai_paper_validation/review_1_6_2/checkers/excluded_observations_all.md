# Complete first-pass excluded-observation handoff

Mechanical verbatim collection from the three canonical checker artifacts. All seven shard tables retained. Relative source links remain valid from checkers/. Scientific pass 2 and audit independently reread every row against supplied sources and inclusion rules.

## numeric_consistency excluded table 1

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p.1 abstract Results versus p.5 Table1 sex | Abstract402 men(80.2%) among500; Table1 men207+194=401. Printed count-copy intervals[401.5,402.5] and[400.5,401.5] touch, gap0. Within abstract, 100×[401.5/500.5,402.5/499.5]=[80.219780,80.580581]% overlaps printed80.2 interval[80.15,80.25], gap0. The workflow precision rule screens the observation. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.5 Table1, normothermia Injury Severity Score | Median20.0 is below printed Q1=20.5 in IQR20.5–35.0. Medianinterval[19.95,20.05], Q1interval[20.45,20.55], gap0.40; relative discrepancy0.40/20.0=0.020≤0.05. This descriptive IQR is not an estimate confidence interval versus P value/test (Route A category1); the specified display rule screens this numerical ordering observation. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.4 Results target temperature versus same paragraph's27% never33°C | 71.5% reached33°C implies28.5% never under a common denominator, versus printed27%. Complement interval[28.45,28.55] and printed[26.5,27.5] yield gap0.95/27=0.035185≤0.05. eTable7 p.11 has primary-evaluable never65/240=27.083% and a different population from186/260 target attainment, supporting distinct denominators; numerical discrepancy does not meet precision threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p.8 eTable4, noradrenaline>15mcg/min days P value | Source-matched visual page prints P<.000; native locator wraps a trailing1 on the next row. Taken literally as display-zero small P, this is covered by the explicit display-zero P exclusion. No independent numeric-count contradiction found for this row. | ROUNDING_OR_DISPLAY_PRECISION |

## numeric_consistency excluded table 2

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-003 p21 eTable12 mostlikely H cell, N243 | Literal 133/260=51.1538% would ordinarily round to51.2 rather than printed 51.1. Allowing printed integer half units gives[50.8637,51.4451]%, overlapping printed 51.1 interval[51.05,51.15]; gap 0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 pp14,19,22 adjusted rows, N207,N227,N247 | Severity-adjusted RR 1.04 and1.11 or time-adjusted OR 0.95 need not equal crude effects from event counts. Counts alone cannot establish an adjusted label/identity discrepancy; modeled estimates are explicitly identified. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 pp13–14 and18–19 mortality denominators, N208,N209,N228,N229 | Normothermia death denominators 160/195 are one below baseline 161/196. There is no printed claim of complete mortality ascertainment for every baseline participant; treating baseline totals as mandatory death denominators would require an unsupported completeness assumption. Each displayed count/denominator/percentage reconciles. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 p15 eFigure4 axis, N217 | Time-bin label37–41 is followed by43–48 among six-hour positions. The apparent axis-label slip changes no reported count, estimate, interval or effect direction and the timeline reading is evident. | NOTATION_OR_TYPOGRAPHY |

## statistical_pass_1 excluded table 1

Only apparent observations that were not emitted are listed; successful checks remain in the S inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p 5 Table 1 ISS, S025 | N median 20.0 is below descriptive IQR lower limit 20.5. Half-unit intervals[19.95,20.05] and[20.45,20.55] leave gap.40/20.0=.02≤.05. This is an IQR, not an effect confidence interval; descriptive quantile ordering was explicitly checked, and the scope display threshold screens the size. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p 8 eTable 4 noradrenaline-duration P, S056 | Source visually prints P <.000. This very small P display is not a finding by itself; the two medians lie within their IQRs and no CI/test contradiction is supplied. Native text's wrapped “1” is not treated as authority over the page. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p 11 eTable 7 row-specific intervals, S090, S091, S092, S093 | Diagnostic binomial normal intervals 23.2366–50.2327,29.9811–53.6010,41.5249–66.9497,48.0904–71.9096 differ modestly from printed 22.8–50.7,29.6–53.9,41.2–67.3,47.8–72.2. Endpoint gaps after.05 half-units are all≤.05relative; CI engine unspecified; no independent containment or decision conflict in these marginal intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp 4,6 Figure 2 temperature claim, S029 | The precise test behind “significantly lower” is not supplied; visual direction agrees and no contradictory numeric estimate, interval or P is printed. Missing test alone cannot register a candidate. | CONDITIONAL_OR_UNREPORTED |

## statistical_pass_1 excluded table 2

Only apparent issues considered and not emitted appear below. Reconciled checks are in the relationship inventory. Each row has one scope reason code.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-003 pp.16,20, PP/as-treated sensitivity methods, S234/S270 | Majority of first72h is described using degree×hours AUC below35°C, but a numeric AUC cutoff is not supplied locally. The source points to the SAP; an omitted local cutoff alone is not a contradiction, and the plan shard owns exact specification alignment. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 pp.14,19, adjusted rows, S219/S256 | PP row labels favorable outcome whereas as-treated row labels unfavorable outcome. They concern different populations; individual adjusted model outputs/outcome coding are unavailable. Inferring that1.11 necessarily used the favorable event from its similarity to a crude OR/RR would invent a mapping; no same-analysis numerical conflict is reproduced. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 p.21 eTable12 most-likely RR, S286/S288 | The stratified RR CI.95–1.06 is narrower than a diagnostic unstratified log-RR interval from rounded counts (approximately.85–1.21). The source explicitly specifies CMH for this scenario, unlike the unadjusted worst/best rows. Strata, dataset-specific values and pooling definition are absent; neither the null/P decision nor a source-established same-analysis value conflicts. The diagnostic is not treated as the reported model. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 p.21 eTable12 most-likely H count/percentage, S284 | 133/260=51.153846%, compared with51.1%. With exact counts the gap to the printed percentage interval[51.05,51.15] is.003846 percentage points, relative.0000753. Allowing half-unit intervals for displayed inputs gives overlap and gap0. Both satisfy the display-precision screen. | ROUNDING_OR_DISPLAY_PRECISION |

## statistical_pass_1 excluded table 3

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

## statistical_pass_1 excluded table 4

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-002 pp189,191,193, monitoring-table P columns and GOSE-score rows | Specific tests, sidedness, variance estimation and the name of the parenthesized GOSE dispersion are not supplied. Exact P reproduction or a claimed method/data conflict would depend on additional assumptions; all means and diagnostic sample SDs reconcile and no confidence interval or printed test conclusion contradicts these P values. | CONDITIONAL_OR_UNREPORTED |

## cross_source_consistency excluded table 1

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 abstract/Table 1 | 402 versus 207+194=401 men: copy half-unit intervals meet and relative difference ≤.05; within-display count/percent reproduction is separately checked. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 methods/Figure 3; DOC-002 outcome/follow-up definitions | Six months after injury versus randomization, with enrollment within three hours and same cohort/outcome evident. | TERMINOLOGY_OR_WORDING |
| DOC-001 p.3; DOC-002 pp.77/99/100 | Report rate up to .25°C/hour includes planned .17; urgent faster-rate exceptions stated. | CONTEXT_RESOLVES |
| DOC-001 p.3; DOC-002 pp.83/84 | Report 82% versus fixed 80%/updated 82.3% power and 364/366 evaluable: contexts differ and precision discrepancy ≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-002 pp.152/85/188 | Second interim 256 versus 250: half-unit gap 5, relative 5/250=.02. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-002 pp.84–86/178–179 | Eleven analyses versus six recruitment looks: five looks×two endpoints plus mortality at 450 explains eleven endpoint assessments; awkward “ten…both” wording does not establish added recruitment looks. | TERMINOLOGY_OR_WORDING |
| DOC-002 p.187; PD053 locator | Apparent >48-hour death crossover in map: source prints <48 hours and aligns with p.183/eFigure 6; new map corrected by coordinator. | NOT_REPRODUCED |
| DOC-002 p.85 versus update pp.183/187 | Earlier PP subset versus all controls superseded by explicit updated eligibility/compliance exclusions, followed by report. | CONTEXT_RESOLVES |
| DOC-001 p.4; DOC-002 secondary list | Interpret secondary results as exploratory because no multiplicity adjustment; report still calls them secondary, so no formal status change. | TERMINOLOGY_OR_WORDING |
| DOC-001 p.3; DOC-002 secondary analyses | Sliding dichotomy, QOL, economics and CACE expressly not reported; SACE/adjusted secondary Cox absent. No supplied “key secondary” designation or abstract result establishes a missing primary/key analysis in this observation. | OUT_OF_FOCUS |
| DOC-003 eTable 5; DOC-002 survivor outcomes | Favorable versus unfavorable among actual survivors are complements; SACE is a separate target, not an extracted primary/key result here. | TERMINOLOGY_OR_WORDING |
| DOC-001 p.3/5; DOC-002 pp.85/86 | Ten-day AEs versus SAE notification through seven days after cessation are different event/reporting definitions. | NOT_REPRODUCED |
| DOC-001 abbreviated eligibility; full report/plan criteria | Ages 18–60 versus ≥18/<60 resolved by detailed report criteria matching plan. | TERMINOLOGY_OR_WORDING |
| Original/final plan amendments | Age/BP/window, AQOL→SF12, ICU mortality removal, run-in/sample changes explicitly documented prospectively. | CONTEXT_RESOLVES |
| DOC-001 p.4/8; DOC-003 eTable 3 | Never reaching 33°C versus premature withdrawal and cause-qualified subsets; 27% versus 28.5% also within precision. | CONTEXT_RESOLVES |
| Main and sensitivity baseline tables | Different baseline values concern different ITT/PP/as-treated/adequate-dose sets, not copied primary/key results. | PERIPHERAL_COMPARISON |
| Main/supplement figures | Rewarming versus postrandomization anchors, PP/ITT, box medians versus least-squares means are different quantities. | NOT_REPRODUCED |
| DOC-003 eFigure 2 versus article | Log-rank .5349 versus Cox .54 are separate tests. | CONTEXT_RESOLVES |
| DOC-002 pp.76/92/146 | Motor withdrawal <4 versus ≤4/worded withdrawal is clinically resolved procedural wording; no analysis-set count/result differs. | TERMINOLOGY_OR_WORDING |
| DOC-002 TEG pp.124/168 | “48 and 72 hours” versus 48–72 hours is one sampling window in immediate context. | TERMINOLOGY_OR_WORDING |
| DOC-002 propofol p.131 versus parent cooling guide | Passive-rewarming description in separate PK substudy does not alter a supplied primary/key result or paired temperature comparison. | OUT_OF_FOCUS |
| DOC-002 propofol p.132 | Terminal AUC formula is a separate substudy method, not used for a supplied parent primary/key result. | OUT_OF_FOCUS |
| DOC-002 pp.174–177/180 | Amendment dates, administrative site counts and projected calendar copies do not change statistical decision rules or primary population. | PERIPHERAL_COMPARISON |
| DOC-003 pp.8/15 | Contributor counts and 37–41 time label are peripheral displays; display-zero P not a finding. | PERIPHERAL_COMPARISON |
| DOC-002 SAP pointer pages | Absent full published SAP/depth thresholds cannot establish that its prespecified depth analyses were replaced or absent. | CONDITIONAL_OR_UNREPORTED |

