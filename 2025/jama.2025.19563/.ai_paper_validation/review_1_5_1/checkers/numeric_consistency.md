# Numeric Consistency Check — Complete N001–N117

## Scope and method

Checked every canonical numeric/reporting relationship N001–N117 against the current 1.5.1 mapping artifacts and, for every provisional issue below, against the cited direct PDF page using direct layout extraction. Checks covered displayed arithmetic, mutually exclusive totals, numerator/denominator/percentage reconciliation, population identity, repeated values, units/scales/labels, and count-versus-rate distinctions. Protocol definitions were compared with reported results only after matching population, time point, and analysis condition. Ordinary display rounding was accepted (one decimal percentage: maximum half of 0.1 percentage point; whole-count values: exact). No `P = 0` display occurs in this numeric scope.

`PROVISIONAL CANDIDATE` is a quality-control flag only. It is not a stable candidate ID, adjudication, severity, validity finding, or disposition.

## Provisional candidate records

### NUM-CAND-001 — Figure 3 calls a body-mass-index value “weight”

- **Relationship:** N025 (M-N025).
- **Direct observations:** DOC-001 PDF p. 8, Figure 3 footnote a prints: “Baseline median (IQR) **weight**: 32.2 (28.2-35.9) **kg/m2** in the AI-led DPP group and 32.5 (29.3-37.7) kg/m2 in the human-led DPP group.” DOC-001 PDF p. 6, Table 1 prints the same 32.2 (28.2-35.9) and 32.5 (29.3-37.7) values in the row labelled “Body mass index (BMI) — kg/m2.”
- **Rule and calculation:** Weight is a mass and should have a mass unit (for example kg); kg/m2 is a BMI unit. Exact equality of both displayed value/IQR triplets across Figure 3 and the BMI row is a direct cross-location identity match, so the Figure 3 word “weight” is inconsistent with its own unit and the matched Table 1 measure.
- **Tolerance:** None: this is a measure-label/unit identity check, not a rounded numerical comparison.
- **Direct observation vs inference:** The Figure word, unit, and Table 1 values are direct observations. The likely production explanation (that “BMI” was omitted) is an inference and is not assumed.
- **Alternative interpretation:** The authors may have intended a nonstandard shorthand for body size, but the printed kg/m2 unit and identical Table 1 BMI values do not support literal body weight.
- **Quality-control relevance:** A reader extracting Figure 3 baseline descriptors could misclassify BMI as weight, creating a unit/measure error in downstream evidence tables.
- **Exact human question:** Should Figure 3 footnote a say “Baseline median (IQR) BMI” rather than “weight,” or is there another source-supported explanation for the kg/m2 values?

### NUM-CAND-002 — Follow-up A1C device counts do not reconcile with the printed complete-outcome/A1C-availability count

- **Relationship:** N069 (D3A-N004), with matched N006 and N102 (D3B-N12).
- **Direct observations:** DOC-003 PDF p. 8 lists 12-month A1C methods: Afinion 2 Analyzer 282, A1CNow+ 30, serum 0; total = 312. DOC-001 PDF p. 5 Figure 1 and p. 4 Results print 313 participants with complete 12-month outcomes. DOC-003 PDF pp. 48-50, eTables 8a-8c, prints both A1C and weight missing for 26 AI and 29 human participants (55 total) and states no A1C/weight missing among completers; 368 - 55 = 313.
- **Rule and calculation:** If the three p. 8 device rows exhaust 12-month A1C measurements, their total should equal the count with 12-month A1C available under the matched missingness statement: 282 + 30 + 0 = 312, versus 368 - (26 + 29) = 313; discrepancy = 1 participant.
- **Tolerance:** Zero counts; device-method rows are integer participant counts. This is not a percentage-rounding issue.
- **Direct observation vs inference:** All printed counts/statements are direct observations. It is an inference that the p. 8 table intends an exhaustive accounting of all 12-month A1C tests; its introductory sentence says it summarizes the number who underwent A1C testing using each device.
- **Alternative interpretation:** One completer may have a valid A1C result from an unlisted method, may be absent from the device-method table by design, or “complete outcome” may have a definition not fully visible in the flow diagram. The supplied tables do not name such an exception.
- **Quality-control relevance:** The discrepancy affects reconciliation of outcome ascertainment and the denominator available for A1C-related endpoint components.
- **Exact human question:** Is one 12-month A1C measurement omitted from the device-method table, or should the complete-outcome/missingness count be 312 for A1C availability?

### NUM-CAND-003 — eTable 7 has contradictory significance statements

- **Relationship:** N101 (D3B-N11).
- **Direct observations:** DOC-003 PDF p. 47, eTable 7 footnote 1 states: “No baseline characteristics were statistically significant different between groups (p<0.05).” Footnote 2 on the same page states: “Age differed between study groups (p = 0.014); all other baseline characteristics were similar (p > 0.05).”
- **Rule and calculation:** Under the table’s own conventional threshold, p = 0.014 is less than 0.05, so it denotes a statistically significant age difference. The “no ... significant” statement conflicts both with its parenthetical `p<0.05` (which is the opposite inequality needed for a nonsignificant statement) and with footnote 2’s age result.
- **Tolerance:** None for inequality direction and the printed p value.
- **Direct observation vs inference:** The two footnotes and p value are direct observations. The likely typographical correction (`p>0.05` and/or an exception for age) is not assumed.
- **Alternative interpretation:** Footnote 1 could be a generic carryover text and footnote 2 could be intended as the controlling table-specific statement; the source does not designate one as superseding the other.
- **Quality-control relevance:** The ambiguity can invert a baseline-comparison interpretation for completers versus dropout/lost-to-follow-up groups.
- **Exact human question:** Which eTable 7 footnote is intended, and should footnote 1 be corrected to state the age exception and/or `p>0.05` for the remaining characteristics?

### NUM-CAND-004 — eTable 10b labels its two-proportion comparison as Wilcoxon rank-sum despite the stated table method

- **Relationship:** N104 (D3B-N14), with matched method key N085 (D3A-N020).
- **Direct observations:** DOC-003 PDF p. 52, eTable 10b compares participants on prohibited medications: AI 6/183 (3.3%) and human 7/185 (3.8%), P = 0.793, with footnote “Wilcoxon Rank Sum Test.” DOC-003 PDF p. 29, the eTable 10 method description says “Chi-squared test used for comparison between study groups.”
- **Rule and calculation:** These are the same table/object, population, binary participant-level proportion, and arm comparison. A result label cannot simultaneously identify the comparison as Wilcoxon rank-sum and, in its matched method description, chi-squared without an explained distinction. The numerical P value is not recalculated because the table supplies neither underlying analysis implementation nor a test statistic.
- **Tolerance:** None: this is a test/measure-label identity comparison.
- **Direct observation vs inference:** Method and result labels are direct observations. Whether the analysis used chi-square, Wilcoxon rank-sum, or a different test is unresolved.
- **Alternative interpretation:** The p. 29 table-method synopsis may be general rather than specific to eTable 10b, or the p. 52 footnote may be a copied label. Neither page explains a separate continuous outcome.
- **Quality-control relevance:** Test-label ambiguity can lead extractors to record an incorrect analysis method for a between-arm medication-proportion comparison.
- **Exact human question:** Which test generated P = 0.793 for the 6/183 versus 7/185 comparison, and which of the p. 29 or p. 52 labels should be corrected?

## Complete relationship check register

Each row records the printed observation(s), comparator/rule, and disposition. `NO CANDIDATE` means the checked printed relationship reconciled at available precision or is a definition/context record without a matched contradictory result; it is not an adjudication.

| ID | Source location and checked observation | Comparator/rule/calculation | Disposition |
|---|---|---|---|
| N001 | DOC-001 pp. 1,2,4: randomized/ITT total 368. | Matched flow allocation 183+185=368. | NO CANDIDATE |
| N002 | DOC-001 pp. 1-4: three-component endpoint and A1C range. | Component thresholds/units remain distinct; no incompatible repeat. | NO CANDIDATE |
| N003 | DOC-001 p. 5: prescreened 2944 and eight source counts. | 886+799+799+167+94+84+42+7+66=2944. | NO CANDIDATE |
| N004 | DOC-001 pp. 4-5: assessed 427, randomized 368, excluded 59. | 368+45+10+3+1=427; exclusions=59. | NO CANDIDATE |
| N005 | DOC-001 pp. 5-6: AI 183, human 185. | 183+185=368; matches N001. | NO CANDIDATE |
| N006 | DOC-001 pp. 4-5: complete 313; restricted AI151/human149; medicines 13. | 183-32=151;185-36=149;313-13=300. Matched availability issue separately flagged under N069/N102. | NO CANDIDATE |
| N007 | DOC-001 p. 5: missed visits AI26/human29 and overlapping reasons. | Reasons explicitly not mutually exclusive; no inappropriate subgroup sum imposed. | NO CANDIDATE |
| N008 | DOC-001 p. 6: overall baseline descriptors. | Overall proportions/ranges are descriptive and match N009-N018 aggregates where applicable. | NO CANDIDATE |
| N009 | DOC-001 p. 6: site AI120+63, human123+62. | Each sums to arm denominator; 120/183=65.6%,123/185=66.5%. | NO CANDIDATE |
| N010 | DOC-001 p. 6: age medians and P=.01. | Median/IQR needs no additive reconciliation; matched supplement P=.014 is precision-compatible context. | NO CANDIDATE |
| N011 | DOC-001 p. 6: female/male 121/62 and139/46. | Each sum=183/185; displayed percentages ordinary rounding. | NO CANDIDATE |
| N012 | DOC-001 p. 6: race category counts. | AI categories sum 183; human categories sum185. | NO CANDIDATE |
| N013 | DOC-001 p. 6: ethnicity category counts. | AI 5+176+1+1=183; human15+167+1+2=185. | NO CANDIDATE |
| N014 | DOC-001 p. 6: marital and education categories. | Each arm category sum equals 183/185; rounding compatible. | NO CANDIDATE |
| N015 | DOC-001 p. 6: BMI classes and kg/m2 label. | AI55+70+33+25=183; human47+57+47+34=185; unit coherent. | NO CANDIDATE |
| N016 | DOC-001 p. 6: medical-history frequencies. | Nonexclusive histories; no total required; percentages agree with arm Ns. | NO CANDIDATE |
| N017 | DOC-001 p. 6: A1C/MVPA values and invalid records=3. | Counts 54/183 and65/185 round correctly; A1C and activity units distinct. | NO CANDIDATE |
| N018 | DOC-001 p. 6: diet bands. | AI70+50+63=183; human73+58+54=185; 0-16 lower-healthier scale stated. | NO CANDIDATE |
| N019 | DOC-001 pp.1,2,4,7: 58/183,59/185,117/368. | Arm counts sum117; percentages 31.7,31.9,31.8 reconcile. | NO CANDIDATE |
| N020 | DOC-001 p.7: 31/183 vs37/185. | 16.9% and20.0% round correctly; crude difference about -3.1 pp. | NO CANDIDATE |
| N021 | DOC-001 p.7:23/183 vs23/185. | 12.6% and12.4% round correctly; crude difference about +0.1 pp. | NO CANDIDATE |
| N022 | DOC-001 p.7:35/130 in both arms. | Both 26.9%; A1C subgroup denominator explicitly 130/arm. | NO CANDIDATE |
| N023 | DOC-001 pp.1,4,9: initiation/completion counts. | 171/183,153/185,117/183,93/185 each reproduce one-decimal percentages. | NO CANDIDATE |
| N024 | DOC-001 p.4: incident A1C 4.4% vs3.8%. | Counts/denominators not printed here; no unsupported reconstruction. | NO CANDIDATE |
| N025 | DOC-001 p.8: Figure 3 footnote calls 32.2/32.5 kg/m2 “weight.” | Exact Table 1 BMI-value/unit match; see NUM-CAND-001. | PROVISIONAL CANDIDATE: NUM-CAND-001 |
| N026 | DOC-001 p.8: HbA1C change axis in pp; baseline 5.8%(0.3). | Scale/direction coherent with A1C measure. | NO CANDIDATE |
| N027 | DOC-001 p.8: PA axis min/wk, n149/151. | Correctly distinguished from count/rate; no summary to recalculate. | NO CANDIDATE |
| N028 | DOC-001 p.9: AI Figure 4 matrix. | Columns12+54+117=183; rows125+58=183; internal cells reconcile. | NO CANDIDATE |
| N029 | DOC-001 p.9: human Figure 4 matrix. | Columns32+60+93=185; rows126+59=185; internal cells reconcile. | NO CANDIDATE |
| N030 | DOC-001 pp.4,9: engagement-achievement narrative/matrix. | Exact matrix-derived percentages round to stated 25/22/37 and28/28/35. | NO CANDIDATE |
| N031 | DOC-001 p.4: sensitivity/subgroup cross-references. | No new result printed; no plan/result identity assumed. | NO CANDIDATE |
| N032 | DOC-001 p.4: AE statement defers counts. | No count/rate supplied here; matched tables checked under N114-N116. | NO CANDIDATE |
| N033 | DOC-001 p.7: human20.0%, completer22.1%. | Different denominators (185 vs149) explicitly distinguish results. | NO CANDIDATE |
| N034 | DOC-001 p.8: external contextual values. | External context is not trial numeric identity; no within-package mismatch. | NO CANDIDATE |
| N035 | DOC-001 p.7: achiever completion shares74%/56%. | Figure4:43/58=74.1%,33/59=55.9%. | NO CANDIDATE |
| N036 | DOC-002 pp.1,6: protocol identity/12 months. | Planned definition, no conflicting observed identity. | NO CANDIDATE |
| N037 | DOC-002 pp.6,8,13: planned368,184/arm. | 184+184=368; planned rather than observed counts. | NO CANDIDATE |
| N038 | DOC-002 pp.6,15: planned composite thresholds. | Units/thresholds coherent with endpoint mapping. | NO CANDIDATE |
| N039 | DOC-002 pp.6-7,15-16: secondary endpoint units/times. | Count, percentage, and PA measures distinguished. | NO CANDIDATE |
| N040 | DOC-002 pp.7,17: eligibility ranges. | Boundaries/units internally coherent. | NO CANDIDATE |
| N041 | DOC-002 pp.7-8: schedule and 7-day wear. | Time points ordered and no contradictory total. | NO CANDIDATE |
| N042 | DOC-002 pp.9-10: activity schedule windows. | Listed schedule is definition; no result arithmetic required. | NO CANDIDATE |
| N043 | DOC-002 pp.10,20: $40 visits,$10x12,max$240. | 3x$40+12x$10=$240; schedule ranges conditional, not contradiction. | NO CANDIDATE |
| N044 | DOC-002 pp.13-16: hDPP engagement example. | 4/8=50%,1/3=33%,5/11=45% (rounded). | NO CANDIDATE |
| N045 | DOC-002 pp.14,16: completer rules. | Arm-specific exposure definitions preserved; no false equivalence. | NO CANDIDATE |
| N046 | DOC-002 pp.14,16: CDC completer benchmark60%. | Denominator explicitly completers, not randomized. | NO CANDIDATE |
| N047 | DOC-002 p.20: projected accrual13 then14/month. | Projection clearly labelled; no observed-flow comparison imposed. | NO CANDIDATE |
| N048 | DOC-002 p.28: stratification bands/timing. | A1C/site strata match stated protocol rules. | NO CANDIDATE |
| N049 | DOC-002 pp.17,28-30: exclusion time windows. | Thresholds are definitions; no conflicting reported count. | NO CANDIDATE |
| N050 | DOC-002 p.31: rescue/withdrawal thresholds. | Operational definitions, not participant totals. | NO CANDIDATE |
| N051 | DOC-002 p.32: planned CONSORT368,184+184. | Exact allocation arithmetic. | NO CANDIDATE |
| N052 | DOC-002 pp.32-33: measurement precision/wear rules. | Units and <75% definition coherent. | NO CANDIDATE |
| N053 | DOC-002 pp.35-36: AE windows/thresholds. | Time windows are purpose-specific; no total required. | NO CANDIDATE |
| N054 | DOC-002 pp.36-37: 15-pp NI hypotheses. | Contrast/sign convention matches dDPP vs hDPP definition; formal check separately statistical. | NO CANDIDATE |
| N055 | DOC-002 p.37: n276,25% attrition,n368. | 276/.75=368;138/.75=184. | NO CANDIDATE |
| N056 | DOC-002 pp.37-38: populations/models. | Planned models not compared as observed estimates. | NO CANDIDATE |
| N057 | DOC-002 pp.38-39: >5% PA missingness rule. | Conditional threshold and complete-case definition coherent. | NO CANDIDATE |
| N058 | DOC-002 p.39: 3% discount/horizons. | Rate, time, and QALY/ICER labels distinct. | NO CANDIDATE |
| N059 | DOC-002 p.61: 31 items, denominator155. | 31x5=155; score range20-100% correct. | NO CANDIDATE |
| N060 | DOC-002 pp.62-63:21 items, denominator105/NPS. | 21x5=105; NPS formula is definition with no observed result. | NO CANDIDATE |
| N061 | DOC-002 pp.63-64: WHO-5 0-25 x4. | 25x4=100. | NO CANDIDATE |
| N062 | DOC-002 pp.65-66: data codes/units. | Codes and pounds/minutes label distinct measures. | NO CANDIDATE |
| N063 | DOC-002 pp.67,70: health-use counts/6mo. | Explicit counts, not rates; no misuse found. | NO CANDIDATE |
| N064 | DOC-002 p.71: COVID thresholds. | Operational thresholds only. | NO CANDIDATE |
| N065 | DOC-002 p.72: AE collection form. | No result count or denominator printed. | NO CANDIDATE |
| N066 | DOC-003 p.7: endpoint rationale external values. | Contextual values not trial estimates. | NO CANDIDATE |
| N067 | DOC-003 p.7:150 min/wk rationale. | Unit/threshold coherent; external range not matched trial result. | NO CANDIDATE |
| N068 | DOC-003 p.7:0.2-pp A1C rationale. | Percentage-point scale correctly distinguished. | NO CANDIDATE |
| N069 | DOC-003 p.8: baseline334+33+1=368; follow-up282+30+0=312. | Follow-up total conflicts with matched313 availability; see NUM-CAND-002. | PROVISIONAL CANDIDATE: NUM-CAND-002 |
| N070 | DOC-003 pp.8-9: device transitions total8(2.2%). | 6+1+0+0+1=8;8/368=2.17%, rounds2.2%. | NO CANDIDATE |
| N071 | DOC-003 p.11: GT9X baseline33/368. | Device assignment is not arm allocation; no conflicting denominator. | NO CANDIDATE |
| N072 | DOC-003 p.13: 7-day/12-visit aggregation. | Maximum11 postbaseline periods stated; time/unit coherent. | NO CANDIDATE |
| N073 | DOC-003 p.13: valid-day/nonwear/zero rule. | Missingness rule explicit; no rate/count confusion. | NO CANDIDATE |
| N074 | DOC-003 p.13: MVPA>=3941 counts/min. | Threshold/scale coherently stated. | NO CANDIDATE |
| N075 | DOC-003 pp.14-17: code-derived fields. | Code wording retained; no output value to reconcile. | NO CANDIDATE |
| N076 | DOC-003 p.20: 3 in-person visits. | Baseline,6,12 months matches schedule. | NO CANDIDATE |
| N077 | DOC-003 p.21: notifications<=10/day. | Exposure definition only. | NO CANDIDATE |
| N078 | DOC-003 p.22:19+6 lessons. | Core/maintenance phases distinct; no required total result. | NO CANDIDATE |
| N079 | DOC-003 p.23: app-data missingness. | Correctly distinct from clinical outcome missingness. | NO CANDIDATE |
| N080 | DOC-003 pp.24-26: algorithm units. | No participant count/statistic printed. | NO CANDIDATE |
| N081 | DOC-003 p.27: primary/per-protocol definitions. | Per-protocol definition matches 151/149 later tables. | NO CANDIDATE |
| N082 | DOC-003 p.28: aRD pp/AI-human/-15. | Label/direction matches eFigure context; formal interval check statistical. | NO CANDIDATE |
| N083 | DOC-003 p.28: subgroup RD definitions. | Subgroup populations remain separate. | NO CANDIDATE |
| N084 | DOC-003 pp.28-29: eTable method keys. | Definitions correctly distinguish tables and populations. | NO CANDIDATE |
| N085 | DOC-003 p.29: eTable10 says chi-squared. | Matched result label mismatch in N104; see NUM-CAND-004. | PROVISIONAL CANDIDATE: NUM-CAND-004 |
| N086 | DOC-003 p.29: eTable12 denominator=achievers. | Correct denominator rule; reconciled N106. | NO CANDIDATE |
| N087 | DOC-003 pp.29-30: diabetes-range/PP tables. | Measurement vs diagnosis distinction explicit. | NO CANDIDATE |
| N088 | DOC-003 p.30: MICE20/Rubin. | Sensitivity definition only. | NO CANDIDATE |
| N089 | DOC-003 p.30: pattern-mixture0%/37.8%. | Assumption and percentage scale explicit. | NO CANDIDATE |
| N090 | DOC-003 p.30: nonwear sensitivity definitions. | Scenarios distinct from primary zero assignment. | NO CANDIDATE |
| N091 | DOC-003 p.34: age-adjusted eFigure3 counts/RDs. | Counts/percentages reconcile; adjusted RD not required to equal crude difference. | NO CANDIDATE |
| N092 | DOC-003 p.35: subgroup eFigure4 counts. | Within each stratum counts sum to arm totals where partitions; rounded crude RDs compatible. | NO CANDIDATE |
| N093 | DOC-003 pp.36-37: version starts/exposures. | Starts sum183; exposures explicitly overlapping. | NO CANDIDATE |
| N094 | DOC-003 p.38: Human program allocation. | 63+60+3+59=185; percentages round. | NO CANDIDATE |
| N095 | DOC-003 pp.39-40: N368 baseline categories. | Race/ethnicity/marital/education category counts each sum368. | NO CANDIDATE |
| N096 | DOC-003 pp.39-40: BMI/diet/medical baseline. | BMI102+127+80+59=368; diet143+108+117=368. | NO CANDIDATE |
| N097 | DOC-003 p.41: eligibility categories. | Each arm/analysis population category totals its N; thresholds distinct. | NO CANDIDATE |
| N098 | DOC-003 pp.42-43: site baseline table. | JHU243+Reading125=368; category partitions reconcile. | NO CANDIDATE |
| N099 | DOC-003 pp.42-43: site table remaining values. | Site-specific P values are not confused with arm baseline footnote. | NO CANDIDATE |
| N100 | DOC-003 pp.44-45: A1C strata108+260. | Site/race/other strata sum their displayed denominators. | NO CANDIDATE |
| N101 | DOC-003 pp.46-47: completer313/dropout55 and footnotes. | 313+55=368; footnotes conflict; see NUM-CAND-003. | PROVISIONAL CANDIDATE: NUM-CAND-003 |
| N102 | DOC-003 pp.48-50: missingness26+29=55. | 368-55=313; matched device table discrepancy under N069. | PROVISIONAL CANDIDATE: NUM-CAND-002 |
| N103 | DOC-003 p.51: attendance/window data. | Fractions and one-decimal percentages reproduce; days outside use attendee denominators. | NO CANDIDATE |
| N104 | DOC-003 p.52: medication6/183 vs7/185,P=.793. | Proportions round; method label conflicts N085; see NUM-CAND-004. | PROVISIONAL CANDIDATE: NUM-CAND-004 |
| N105 | DOC-003 pp.53-54: per-protocol AI151/H149 baseline. | Category partitions sum to each arm population; percentages reconcile. | NO CANDIDATE |
| N106 | DOC-003 p.55: achiever patterns. | AI patterns sum58,human59,overall117; percentages round by achiever denominator. | NO CANDIDATE |
| N107 | DOC-003 p.56: diabetes-range list15 (H7,AI8). | 7+8=15; threshold is measurement, not adjudicated diagnosis. | NO CANDIDATE |
| N108 | DOC-003 p.57: continuous PP outcomes. | Median/IQR/units correctly labelled; A1C N106/103 distinct from PP N. | NO CANDIDATE |
| N109 | DOC-003 p.58: PP binary counts. | Counts/percentages and crude RDs reconcile at displayed precision. | NO CANDIDATE |
| N110 | DOC-003 p.59: MICE32.2/31.9/RD-1.1. | MI pooled percentages need not equal crude difference; sensitivity condition explicit. | NO CANDIDATE |
| N111 | DOC-003 p.60: pattern mixture58/183,70/185. | 31.7%/37.8% and crude -6.1 pp reconcile. | NO CANDIDATE |
| N112 | DOC-003 p.61: best-case/all-attainment58/183,60/185. | Both scenarios give31.7/32.4; -0.74 compatible with unrounded values. | NO CANDIDATE |
| N113 | DOC-003 p.62: cluster sensitivity58/183,59/185. | Percentages and -0.20 point estimate compatible; bounds differ by stated clusters. | NO CANDIDATE |
| N114 | DOC-003 p.63: AE participants/categories. | Category counts sum100 AI/25 human events; participant percentages use183/185, correctly distinct. | NO CANDIDATE |
| N115 | DOC-003 pp.64-65: AE grades/relatedness. | Grades13+42+43+2=100,5+11+8+1=25; relatedness totals same. | NO CANDIDATE |
| N116 | DOC-003 pp.66-68: condition-by-grade table. | Condition counts reproduce grade subtotals 13/5,42/11,43/8,2/1 and totals100/25. | NO CANDIDATE |
| N117 | DOC-003 p.69: references only. | No result-relevant numeric relationship. | NO CANDIDATE |

## Counts, limitations, and handoff

- **Relationships checked:** 117/117.
- **No-candidate records:** 111.
- **Provisional candidate records:** 4 distinct keys (NUM-CAND-001 through NUM-CAND-004). Keys may be cross-referenced by more than one N relationship; they are not stable IDs.
- **Limitations:** DOC-002 native text is glyph-encoded, so its mapped rendered-page transcription was used. Some inferential compatibility questions (confidence-bound construction, P-value/test compatibility) belong to the dedicated statistical passes and were not reconstructed here. The direct PDFs were rechecked for all four provisional records.
