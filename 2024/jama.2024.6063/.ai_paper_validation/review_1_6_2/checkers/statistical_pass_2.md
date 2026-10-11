# Statistical consistency review — pass 2 — Workflow 1.6.2

Runtime ID: 01a129ce-662d-78e3-ae0a-28ba82dc65c9. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. The agent is distinct from pass 1 runtime 01a129b5-1c4b-7ed3-955e-c6ca5e85d0b6. Complete scope and review contract were read. The complete 104-record S inventory, full pass 1 artifact, all 13 stable candidate cards/classifications, all 24 initial screening decisions, mechanical recheck of every C001–C013 and all 49 checker excluded-observation rows were independently revisited. No legacy conclusions, external literature or web evidence was used.

Scope: every S001–S104, comprising 68 current result tuples and 36 method/design/ancillary/historical records, all 19 main Table 2 rows, all 3 primary sensitivity rows, all 62 eTable 4 rows and every supplied inference/decision specification. Source coverage remains 41/41 pages. Population, denominator, contrast, scale, outcome, time, model, count and recheck implications were considered for every record, including nonsignificant results. All 104 receive PASS_2_COMPLETE in the canonical inventory and individual records below.

One new finding is emitted for independent pass-2 screening. Thirty-seven unique excluded observations are listed once, consolidating repeated upstream observations. All existing stable candidates remain Pending Human Adjudication; none is deleted, re-emitted, disposed of or corrected here.

## Findings

### F-ST2-001

**Title:** The 24-week WOMAC total-pain contrast interval does not reproduce the interval-width rule supported by the other time points for the same outcome.

**Relationships:** S003; same-display witnesses S027,S028,S029,S030,S031. **Focus area:** B and C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W. All compared locations are REPORT. Both report copies contain the same discrepancy within their own display; they agree with each other, so no conflicting S_C relationship is added.

**Exact locations and printed values:** REPORT [main p6, Table 2 WOMAC total pain24](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6) prints krill change −87 (95% CI −110 to −63), placebo change −83 (−106 to −59), contrast 3.0 (−24 to 31), P=.81. REPORT [results p5, eTable 4 total pain24 and all five earlier total-pain time points](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5) repeats those changes/intervals and prints contrast3 (−24 to31), P=.81. REPORT [main p4 methods](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7 continuation](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7), and [results p6 adjustment footnote](../../../joi240048supp3_prod_1727199125.83025.pdf#page=6) identify modeled arm changes and linear-combination contrasts; WOMAC total pain is baseline-adjusted. No different 24-week variance calculation is identified.

**Rule and calculation:** The empirical diagnostic rule takes each arm-change CI half-width h and forms the contrast half-width sqrt(hK²+hP²). It is a same-display reproducing rule, not an assertion that the producing model necessarily has zero covariance or a common critical value. The exact row-specific covariance/critical values remain the human question. It reproduces all five earlier WOMAC total-pain rows, which share the outcome and adjustment description:

| WOMAC total-pain time | K change CI | P change CI | Root-sum-square half-width | Printed contrast half-width | Precision result |
|---|---|---|---:|---:|---|
| 4 weeks | −45 to−20 | −50 to−25 | 17.677670 |18| Arm endpoint allowances yield[16.970563,18.384776], overlapping printed-width[17.5,18.5]. |
| 8 weeks | −64 to−37 | −67 to−40 | 19.091883 |19| Recomputed[18.384776,19.798990] overlaps[18.5,19.5]. |
| 12 weeks | −69 to−40 | −72 to−43 | 20.506097 |21| Recomputed[19.798990,21.213203] overlaps[20.5,21.5]. |
| 16 weeks | −83 to−51 | −84 to−52 | 22.627417 |23| Recomputed[21.920310,23.334524] overlaps[22.5,23.5]. |
| 20 weeks | −90 to−54 | −85 to−49 | 25.455844 |25.5| Recomputed[24.748737,26.162951] overlaps[25,26]. |
| 24 weeks | −110 to−63 | −106 to−59 | 33.234019 |27.5| Recomputed[32.526912,33.941125] does not overlap[27,28]. |

Allowing each integer arm endpoint ±.5 yields both arm half-widths[23,24] and root-sum-square half-width[32.5269119,33.9411255]. At main printed estimate3.0±.05, the recomputed lower endpoint is[−30.9911255,−29.4769119] and upper[35.4769119,36.9911255]. Printed lower−24±.5 gives[−24.5,−23.5], gap4.9769119/24=.2073713. Printed upper31±.5 gives[30.5,31.5], gap3.9769119/31=.1282875. Both exceed.05. Even the wider supplement estimate3±.5 gives lower[−31.4411255,−29.0269119], upper[35.0269119,37.4411255], with gaps4.5269119/24=.1886213 and3.5269119/31=.1137714. The discrepancy survives all displayed allowances in both copies.

The modeled point subtraction itself overlaps the printed3.0 after rounding. The CI contains0 and P=.81 is nonsignificant. No categorical null/P conflict is claimed, and no exact P reconstruction is imposed. This observation is distinct from C008 point-contrast algebra and is not the already screened glucose12 occurrence C012.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The 24-week WOMAC total-pain treatment-contrast confidence interval, whose width supplies its precision and weight in evidence synthesis.

**Why context does not resolve it:** A method reproducing every earlier time point of the same adjusted outcome does not reproduce the printed 24-week interval beyond permitted precision. Always-register category4 applies; unreported covariance or a row-specific method becomes the human question rather than a conditional exclusion. An unchanged nonsignificant interpretation does not equate the two extractable intervals.

**Alternatives and missing definitions:** The contrast and arm intervals could use different covariance, degrees of freedom, critical values, marginalization or variance calculations specifically at24weeks. A model with shared coefficients can yield nonzero arm covariance; it is not assumed absent. A different row-specific calculation may therefore explain the printed width, but none is stated and the empirical rule reproduces all five earlier same-outcome rows. No raw fitted output or exact CI convention is supplied. No production mechanism or preferred analysis is asserted.

**Exact human question:** What row-specific covariance, critical value or interval calculation produced the 24-week WOMAC total-pain contrast3.0(−24 to31), and why does it not follow the arm-width rule that reproduces all five earlier total-pain rows?

## Complete stable-candidate reconciliation

| Stable ID | Count, estimate/test, method, cross-source and recheck implications |
|---|---|
| C001 | Exact positive Key Points and negative matched primary copies remain separated after half-unit allowances; direction extraction affected, significance unchanged. S_C/S_W precedence retained. |
| C002 | Parenthetical placebo percentages remain separated; inequalities on actual unobserved concentration do not equate printed conversions. S_W retained. |
| C003 | Primary same-day and seven-day reference windows remain distinct; no questionnaire/amendment bridge. P_R retained. |
| C004 | Item count/maxima leave scoring denominator unclear; field convention remains an alternative, not externally supplied evidence. S_W retained. |
| C005 | SD/power precision gaps and area/volume dimension differences remain; nominal130/arm does not bridge adopted inputs. P_R retained. |
| C006 | Planned change-regression and producing longitudinal mixed model remain distinct, with no original-model estimate/amendment. P_R retained. |
| C007 | Complete supplied report lacks unconditionally planned ≥80% primary per-protocol estimate; adherence counts/MI/age adjustment are different records. P_R retained. |
| C008 | All three modeled point discrepancies survive precision; no crude means imposed. Additional width signals in those same conflicting tuples do not establish an independent cause and are not re-emitted. S_W retained. |
| C009 | Explicit cough/reflux/abdominal treatment-specific counts remain separated; blanks are not zeros and adjacent1vs2 copies are not added. S_C retained. |
| C010 | Probable relatedness versus all-unrelated summary remains an unresolved mapping, without automatically treating Possible as related. S_C retained. |
| C011 | Recheck broadens n by±.5; favorable78.93133% versus claimed96% leaves relativegap.1725903. This is a labelled simple two-arm power diagnostic, not unpublished exact-model power. P_P retained. |
| C012 | Glucose12 endpoint gaps remain under rule reproducing same-page comparators; point identity/null/P agree. Missing row covariance/critical values remain explicit. S_W retained. |
| C013 | Both WORMS smaller-one-unit percentages remain separated from count/total envelopes, with sums107/109 agreeing; one repeated pattern retained. S_W retained. |

All13 mechanical evidence states remain reproduced and all13 domain/type assignments are unchanged by this pass. This is a reconciliation of supplied facts, not an inclusion-audit disposition. The screened-out F-NUM-005 remains resolved by the matching supplementary RR definition; no already screened finding was re-emitted.

## Audit of every upstream excluded-observation row

NM refers to the first9 rows in canonical numeric_consistency.md; NS to the subsequent10 support rows; XS to the19 cross_source_consistency.md rows; ST to the11 statistical_pass_1.md rows. Row labels below are bookkeeping, not finding IDs. Each row was reread against all five Route A categories and the display-precision rule. The retained-observation number refers to the row order in the unique Excluded observations table below. Repeated upstream observations are consolidated there. The audit covers49/49 rows; one Route A4 observation is emitted.

| Upstream row | Observation revisited | Pass 2 record |
|---|---|---|
| NM01 | Flow completion/discontinuation | Excluded row 1 |
| NM02 | AE participant percentage | Excluded row 2 |
| NM03 | Extremity-pain copies | Excluded row 3 |
| NM04 | Baseline count percentages | Excluded row 4 |
| NM05 | Available WORMS grades | Excluded row 5 |
| NM06 | Strength baseline copies | Excluded row 6 |
| NM07 | Modeled changes/subscale sums | Excluded row 7,8 |
| NM08 | MCII wording | Excluded row 9 |
| NM09 | Post hoc comparative narrative | Excluded row 10 |
| NS01 | Adherence167/165 | Excluded row 11 |
| NS02 | Adherence95% | Excluded row 12 |
| NS03 | Other WORMS percentages | Excluded row 13 |
| NS04 | Strength12/raw-model family | Excluded row 7 |
| NS05 | WOMAC component additivity | Excluded row 8 |
| NS06 | Responder modeled RR | Excluded row 14 |
| NS07 | Adjacent safety copies | Excluded row 15 |
| NS08 | Injury aggregate | Excluded row 16 |
| NS09 | Event aggregate copies | Excluded row 17 |
| NS10 | Glucose12 point arithmetic | Excluded row 18 |
| XS01 | Flow copies | Excluded row 1 |
| XS02 | Contributor copies | Excluded row 19 |
| XS03 | Adherence95% | Excluded row 12 |
| XS04 | Extremity-pain copies | Excluded row 3 |
| XS05 | Adjacent safety copies | Excluded row 15 |
| XS06 | Respiratory/GI aggregates | Excluded row 20 |
| XS07 | Conditional weighting | Excluded row 21 |
| XS08 | No-imputation versus MI | Excluded row 22 |
| XS09 | ICOAP collection versus analysis | Excluded row 23 |
| XS10 | Secondary exploratory caution | Excluded row 24 |
| XS11 | Maximal area ordinary secondary | Excluded row 25 |
| XS12 | BML/PPT/ultrasound availability | Excluded row 26 |
| XS13 | Conditional economics | Excluded row 27 |
| XS14 | Enrollment differences | Excluded row 28 |
| XS15 | NSAID enrollment wording | Excluded row 29 |
| XS16 | Administrative schedules | Excluded row 30 |
| XS17 | Both-leg shorthand | Excluded row 31 |
| XS18 | Post hoc comparative narrative | Excluded row 10 |
| XS19 | Broad discussion | Excluded row 32 |
| ST01 | Strength12 modeled tuple | Excluded row 7 |
| ST02 | WOMACtotal24 CI width | EMITTED F-ST2-001; Route A, category4 |
| ST03 | ICOAP intermittent P diagnostic | Excluded row 35 |
| ST04 | Adopted VAS power | Excluded row 33 |
| ST05 | Article recruited power sample | Excluded row 34 |
| ST06 | Conditional weighting | Excluded row 21 |
| ST07 | No-imputation versus MI | Excluded row 22 |
| ST08 | ICOAP collection | Excluded row 23 |
| ST09 | Secondary status | Excluded row 24 |
| ST10 | Post hoc narrative | Excluded row 10 |
| ST11 | Responder definition | Excluded row 36 |

ICOAP intermittent's earlier ROUNDING_OR_DISPLAY_PRECISION reason is not used here to dismiss a category1 conflict: the normal P inversion lacks the producing test/df, and no categorical null/P conflict exists. Its retained reason is CONDITIONAL_OR_UNREPORTED. WOMAC total24 is different: a reproducing rule established by all earlier same-outcome rows supports category4, so it is emitted despite absent covariance/critical-value definitions. Strength12's repeated back4 tuple remains internally coherent; comparison against crude means or an inferred month coding does not reproduce misattribution.

## Excluded observations

Only apparent issues considered but not emitted are listed, once per distinct theme. Successful routine checks are in the individual S records. There are37 rows, each with exactly one reason code. New interval components of C008 are retained under DUPLICATE_OF_INCLUDED, not screened out as conditional or rounding.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p3 Figure1 vs pp1/7 | Completer/discontinuer copy differences remain below .05 under half-unit precision, including21vs23. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p8 Table3 | 67/130 versus50.7% leaves only.00410 relative residual gap under required precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p8 vs main p1/p8/results p10 | Extremity pain6vs5 half-unit copy intervals touch. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p5 Table1 | Baseline BMI/medication fractions leave zero or≤.05 relative gap with all displayed allowances. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p5 Table1 WORMS | Available grades128/129 need not equal randomized130/132; missing variable values and rounded sums identify the context. | CONTEXT_RESOLVES |
| REPORT main p5 vs p6 strength baseline | 65.8vs65.9 half-unit copy intervals touch. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6/results pp5–6, especially strength12 | Modeled changes differ from descriptive final−baseline; strength12 tuple equality with back4 has no source-grounded conflicting attribution. No continuous-month coding is inferred. | MODEL_VERSUS_CRUDE |
| REPORT main p6/results p5 WOMAC component changes | Separately adjusted total and subscale fits are not stated to share additive decomposition; no reproducible common-model identity is supplied. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp3/5 MCII/MCID | Improvement phrasing does not contradict a supplied numerical classification result. | TERMINOLOGY_OR_WORDING |
| REPORT main p7 vs p6 post hoc | Adjacent comparative context identifies no between-arm effect; all three contrast CIs include0. | CONTEXT_RESOLVES |
| REPORT results p3 adherence | 167 header versus165 footnote gap1/165=.00606≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p7 vs results p3 adherence | 95% versus threshold-adherent82+81/167 has relative precision gap.01280≤.05; mean consumption is a different quantity. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT results p8 WORMS other rows | Nochange/larger1 proportions are within .05 after allowances; smaller−1 issue remains registered C013. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT results p6 responder rows | Rounded proportion ratios are not required to equal the stated log-binomial model RR. | MODEL_VERSUS_CRUDE |
| REPORT main p8 vs results pp10–11 | Nasopharyngitis/diarrhea1vs2 copies have touching half-unit intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p8 vs results pp11–12 injury category | Aggregate safety subgroup comparison is peripheral; no substituted-digit/reversed-arm reading is reproduced. | PERIPHERAL_COMPARISON |
| REPORT main pp7–8 vs results pp10–13 all-event totals | Detailed96/107 versus97/106 differ by1, copy intervals touch and combined203 agrees. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT results p6 glucose12 point | Difference.15−.09 allows[.05,.07], overlapping printed.07[.065,.075]; existing C012 is interval-specific. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6 vs results pp5–6 contributor n | Per-time-point observation copies differ without changing the matched estimates or randomized primary analysis size. | PERIPHERAL_COMPARISON |
| REPORT main p8 vs results pp10–13 respiratory/GI aggregates | Other aggregate-category comparisons are peripheral safety summaries with no independently established value slip. | PERIPHERAL_COMPARISON |
| PLAN protocol p12/SAP p1 vs REPORT main p4 | Propensity weighting is conditional as appropriate; lack of implementation detail alone does not establish a contradicted rule. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p6/results p6 vs results p2 | Original no-imputation analyses and separately identified MI sensitivity refer to different analyses. | CONTEXT_RESOLVES |
| PLAN protocol p11 vs REPORT main pp4/6 ICOAP | Prospective collection does not establish a prespecified ICOAP analysis or hierarchy. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol pp6–7 vs REPORT main p7 | Exploratory caution does not change the still-printed secondary outcome status. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p6 vs REPORT main pp3–4/results | Unreported maximal area is ordinary secondary with no key designation or abstract result; status change is not reproduced. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol pp6–7 vs REPORT main p4 | BML/PPT/ultrasound remain secondary and their availability limits are disclosed; no supplied key-secondary hierarchy or status change. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol p9 vs REPORT main p4 economics | Economic analysis conditional on primary endpoints is resolved by the negative primary trial. | CONTEXT_RESOLVES |
| PLAN protocol pp7/9 vs REPORT main pp2/9 eligibility | Clinical enrollment differences supply no changed numerical primary/key-secondary result, quantified analysis-set size or statistical decision rule. | OUT_OF_FOCUS |
| PLAN protocol pp7/9 vs REPORT main pp2/4 NSAIDs | Enrollment/concomitant medication wording appears in both records without a changed quantitative decision. | OUT_OF_FOCUS |
| PLAN protocol pp7/9/10/11 schedules | Administrative recruitment/measurement schedule differences do not change a primary/key result or decision rule. | PERIPHERAL_COMPARISON |
| REPORT main p4/results p7 strength wording | Both-leg versus index-limb shorthand does not identify a changed estimate or attribution. | TERMINOLOGY_OR_WORDING |
| REPORT main pp8–9 vs pp6–7 discussion | Broad no-effect language retains the explicit placebo effusion result and chance caveat. | CONTEXT_RESOLVES |
| PLAN protocol p12 adopted VAS power;S071 | Diagnostic273.3 versus234 reduces to nearestgap8.17/234=.0349 with prescribed display intervals;234/.90=260 reproduces. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p4 pain power;S070 | 130/arm provides the stated power conservatively rather than claiming an exact minimum119/arm. | CONTEXT_RESOLVES |
| REPORT main p6 ICOAP intermittent;S018 | Normal diagnostic P≈.58 versus.62 is not the specified producing test. Confidence level/sidedness alone do not establish exact df/critical values. No categorical null/P disagreement or reproduced exact-test conflict exists; category1 is not excluded by rounding. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p6/results p7 responder footnote;S011/S085 | Matched supplementary row identifies RR/log-binomial and resolves the main omitted footnote; screening already records F-NUM-005. | CONTEXT_RESOLVES |
| REPORT main p6 ICOAPtotal24/results pp5–6 weightbearing4/hsCRP12;S019/S032/S064 | Additional RSS-width signals concern the same already registered conflicting arm/contrast tuples in C008; no distinct producing cause is established and no existing issue is re-emitted. For ICOAPtotal lower-endpoint gap=.245847/2.64=.093124; hsCRP12 endpoint gaps=.125700/1.19=.105630 and/1.33=.094511. | DUPLICATE_OF_INCLUDED |

## Individual pass 2 completion records

Each record revisits its complete tuple or method/design relationship, not a significance-selected sample. Exact source locations, printed values, roles, scales, contributors and full-cell bindings are retained in the canonical inventory; this table records the second pass implications without changing the first pass facts.

| Relationship ID | Pass 2 assessment | Pass 2 status |
|---|---|---|
| S001 | Primary copies, arm identity, null/P and Figure 2 population revisited; C001 signed Key Points discrepancy retained. | PASS_2_COMPLETE |
| S002 | Effusion contrast, median/IQR distinction and P=.01 favoring placebo reconcile; no unstated clinical margin imposed. | PASS_2_COMPLETE |
| S003 | WOMAC total24 point subtraction overlaps; additional interval-width discrepancy emitted as F-ST2-001. | PASS_2_COMPLETE |
| S004 | Weight-bearing24 point identity, interval containment and null/P reconcile; baseline adjustment retained. | PASS_2_COMPLETE |
| S005 | Non-weight-bearing24 identity and null/P reconcile; no additive cross-fit requirement imposed. | PASS_2_COMPLETE |
| S006 | Function24 modeled contrast51 and interval/P reconcile; contributor copies remain peripheral. | PASS_2_COMPLETE |
| S007 | Hand24 modeled contrast1.3, interval order and null/P reconcile. | PASS_2_COMPLETE |
| S008 | Back24 adjusted contrast−1.3, interval order and null/P reconcile. | PASS_2_COMPLETE |
| S009 | Strength24 subtraction overlaps after precision; modeled changes are distinct from descriptive means. | PASS_2_COMPLETE |
| S010 | AQoL24 precision supports−.01 contrast; interval/null/P reconcile. | PASS_2_COMPLETE |
| S011 | Responder24 log-binomial RR, arm counts, reference group and null1/P reconcile; screened footnote issue not re-emitted. | PASS_2_COMPLETE |
| S012 | hsCRP24 point identity and interval/P reconcile; same-row variance witness retained for glucose12. | PASS_2_COMPLETE |
| S013 | TG24 contrast.15 contains0/P=.11; not conflated with significant TG12. | PASS_2_COMPLETE |
| S014 | HDL24 contrast−.03, containment and null/P reconcile. | PASS_2_COMPLETE |
| S015 | LDL24 small rounded changes support.01; containment and null/P reconcile. | PASS_2_COMPLETE |
| S016 | Glucose24 arm-width rule reproduces its contrast interval; retained C012 witness. | PASS_2_COMPLETE |
| S017 | ICOAP constant24 modeled contrast2.95 overlaps arm subtraction; null/P reconcile. | PASS_2_COMPLETE |
| S018 | ICOAP intermittent24 null/P agree; approximate normal diagnostic cannot establish exact-test incompatibility without producing test/df. | PASS_2_COMPLETE |
| S019 | ICOAP total24 point mismatch remains C008; additional width signal concerns its already registered tuple and is not re-emitted. | PASS_2_COMPLETE |
| S020 | Age-adjusted primary row remains distinct; point identity, interval and P=.94 reconcile. | PASS_2_COMPLETE |
| S021 | MI primary sensitivity row remains distinct from no-imputation main analysis; point identity and P=.92 reconcile. | PASS_2_COMPLETE |
| S022 | Knee4 rounded point subtraction, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S023 | Knee8 point subtraction, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S024 | Knee12 near-zero rounded contrast, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S025 | Knee16 point subtraction, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S026 | Knee20 point subtraction, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S027 | WOMAC total4 point identity/null/P reconcile; RSS CI half-width reproduces printed18 and supports F-ST2-001. | PASS_2_COMPLETE |
| S028 | WOMAC total8 point identity/null/P reconcile; RSS CI half-width reproduces printed19 and supports F-ST2-001. | PASS_2_COMPLETE |
| S029 | WOMAC total12 point identity/null/P reconcile; RSS CI half-width reproduces printed21 and supports F-ST2-001. | PASS_2_COMPLETE |
| S030 | WOMAC total16 point identity/null/P reconcile; RSS CI half-width reproduces printed23 and supports F-ST2-001. | PASS_2_COMPLETE |
| S031 | WOMAC total20 point identity/null/P reconcile; RSS CI half-width reproduces printed25.5 and supports F-ST2-001. | PASS_2_COMPLETE |
| S032 | Weight-bearing4 printed model tuple discrepancy remains C008; no new issue generated from its interval component. | PASS_2_COMPLETE |
| S033 | Weight-bearing8 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S034 | Weight-bearing12 zero point supported by precision; interval/null/P reconcile. | PASS_2_COMPLETE |
| S035 | Weight-bearing16 near-zero point supported by precision; interval/null/P reconcile. | PASS_2_COMPLETE |
| S036 | Weight-bearing20 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S037 | Non-weight-bearing4 arm subtraction ranges overlap printed−5; interval/null/P reconcile. | PASS_2_COMPLETE |
| S038 | Non-weight-bearing8 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S039 | Non-weight-bearing12 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S040 | Non-weight-bearing16 zero contrast supported by precision; interval/null/P reconcile. | PASS_2_COMPLETE |
| S041 | Non-weight-bearing20 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S042 | Function4 point and RSS width reproduce; identical weight-bearing arm tuples corroborate C008 without identifying mechanism. | PASS_2_COMPLETE |
| S043 | Function8 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S044 | Function12 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S045 | Function16 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S046 | Function20 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S047 | Hand4 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S048 | Hand8 positive contrast interval includes0/P=.12; no direction or significance conflict. | PASS_2_COMPLETE |
| S049 | Hand12 near-zero contrast, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S050 | Hand16 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S051 | Hand20 identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S052 | Back4 identity, interval order, containment and null/P reconcile; repeated strength12 tuple alone is not a mismatched attribution. | PASS_2_COMPLETE |
| S053 | Back8 positive contrast interval includes0/P=.11; no significance conflict. | PASS_2_COMPLETE |
| S054 | Back12 positive contrast interval includes0/P=.10; no significance conflict. | PASS_2_COMPLETE |
| S055 | Back16 positive contrast interval includes0/P=.11; no significance conflict. | PASS_2_COMPLETE |
| S056 | Back20 rounded point subtraction supports−.3; interval/null/P reconcile. | PASS_2_COMPLETE |
| S057 | Strength12 modeled tuple repeats back4 but is internally coherent; raw changes do not establish result misattribution; no new finding. | PASS_2_COMPLETE |
| S058 | AQoL12 rounded equal arm changes support near-zero contrast−.0003 and P=.98. | PASS_2_COMPLETE |
| S059 | Responder4 RR.85 reference direction, containment and null1/P reconcile; no crude-model equality imposed. | PASS_2_COMPLETE |
| S060 | Responder8 RR.87 reference direction, containment and null1/P reconcile. | PASS_2_COMPLETE |
| S061 | Responder12 RR.98 reference direction, containment and null1/P reconcile. | PASS_2_COMPLETE |
| S062 | Responder16 RR.94 reference direction, containment and null1/P reconcile. | PASS_2_COMPLETE |
| S063 | Responder20 RR1.06 reference direction, containment and null1/P reconcile. | PASS_2_COMPLETE |
| S064 | hsCRP12 modeled point mismatch remains C008; additional interval-width signal is retained as part of that registered tuple. | PASS_2_COMPLETE |
| S065 | TG12 interval excludes0/P=.01; direction favors krill and matches narrative. | PASS_2_COMPLETE |
| S066 | HDL12 point identity, interval order, containment and null/P reconcile. | PASS_2_COMPLETE |
| S067 | LDL12 upper limit+.005 includes0 and P=.06; no null/P conflict. | PASS_2_COMPLETE |
| S068 | Glucose12 existing C012 supported interval-rule discrepancy retained; point arithmetic overlaps and no new finding re-emitted. | PASS_2_COMPLETE |
| S069 | Current ICC.96 lies in.94–.97; 50-person reliability statement coherent; subtype/CI method absent. | PASS_2_COMPLETE |
| S070 | Report pain sample provides at least stated power under normal diagnostic; effusion exact dispersion missing without independent claim. | PASS_2_COMPLETE |
| S071 | Plan VAS power234 remains within stipulated≤.05 residual precision discrepancy; attrition inflation234/.9=260 exact. | PASS_2_COMPLETE |
| S072 | Plan effusion power remains C011; recheck n±.5 broadens favorable bound to78.93133%, still separated from96%. | PASS_2_COMPLETE |
| S073 | Planned versus reported SD/effusion dimension/power remains C005; same sample130 does not bridge inputs. | PASS_2_COMPLETE |
| S074 | Primary today versus past7days window remains C003; no questionnaire/amendment bridge supplied. | PASS_2_COMPLETE |
| S075 | Primary planned change-regression versus producing mixed model remains C006; no preferred analysis proposed. | PASS_2_COMPLETE |
| S076 | Conditional baseline adjustment agrees; operational P≤.10 threshold alone is not a conflict. | PASS_2_COMPLETE |
| S077 | Randomized≥1-value model includes primary130/132; safety≥1-dose criteria yield same initiators; no changed primary denominator. | PASS_2_COMPLETE |
| S078 | Conditional propensity weighting is not asserted absent; separate age/MI sensitivity scope preserved. | PASS_2_COMPLETE |
| S079 | Unconditional ≥80%-capsule primary per-protocol result remains absent from complete supplied report; C007 retained. | PASS_2_COMPLETE |
| S080 | Secondary status retained despite exploratory interpretation; no prespecified adjustment or key hierarchy inferred. | PASS_2_COMPLETE |
| S081 | Ordinary secondary availability differences retain secondary status and disclosed limits; WORMS count/percentage issue C013 reviewed. | PASS_2_COMPLETE |
| S082 | ICOAP schedule shows collection, not an explicit prespecified hierarchy/analysis; post hoc label alone not contradicted. | PASS_2_COMPLETE |
| S083 | NSAID descriptive modifications distinguished from broader collection; no numerical analysis or preferred test manufactured. | PASS_2_COMPLETE |
| S084 | AE event/person denominators and stated absence of risk tests reviewed; C009 attribution and C010 SAE classification retained. | PASS_2_COMPLETE |
| S085 | Responder composite thresholds/reference group/measure definition reconcile; screened F-NUM-005 not re-emitted. | PASS_2_COMPLETE |
| S086 | Same modeled subtraction reproduces other rows; C008 maintained; new width-rule F-ST2-001 does not require crude means. | PASS_2_COMPLETE |
| S087 | Median/IQR summaries retained separately from modeled mean-change95%CIs; no median subtraction requirement. | PASS_2_COMPLETE |
| S088 | Two-sided superiority decision matches primary null/P; effusion and TG12 significance agree; no NI/equivalence conclusion. | PASS_2_COMPLETE |
| S089 | No supplied interim/stopping/gatekeeping rule contradicted; secondary exploratory caution not an inferred correction. | PASS_2_COMPLETE |
| S090 | Historical reliability quantities remain within natural bounds and are distinct from current MRI volume ICC. | PASS_2_COMPLETE |
| S091 | Historical RR1.38(1.09,1.75),P=.01: containment/order/null/P/direction reconcile. | PASS_2_COMPLETE |
| S092 | Historical RR1.26(1.04,1.53),P=.02: containment/order/null/P/direction reconcile. | PASS_2_COMPLETE |
| S093 | Historical RR1.29(1.01,1.65),P=.04: containment/order/null/P/direction reconcile. | PASS_2_COMPLETE |
| S094 | Historical RR1.15(.92,1.43),P=.21: containment/order/null/P/direction reconcile. | PASS_2_COMPLETE |
| S095 | Historical RR1.55(1.25,1.91),P<.01: containment/order/null/P/direction reconcile. | PASS_2_COMPLETE |
| S096 | Historical RR1.14(.93,1.40),P=.20: containment/order/null/P/direction reconcile. | PASS_2_COMPLETE |
| S097 | Historical RR1.17(.97,1.41),P=.10: containment/order/null/P/direction reconcile. | PASS_2_COMPLETE |
| S098 | Historical RR1.03(.87,1.22),P=.76: containment/order/null/P/direction reconcile. | PASS_2_COMPLETE |
| S099 | Historical effusion-grade trends checked against their axes/directions; no printed point/CI to invert. | PASS_2_COMPLETE |
| S100 | Historical cartilage/BML trends checked against displayed direction; no current-trial decision inference. | PASS_2_COMPLETE |
| S101 | Historical90-person pilot direction agrees; arm n/dispersion/test definition absent, so exact P not inferred. | PASS_2_COMPLETE |
| S102 | Historical hypothetical54-person design explicitly not adopted; missing variance/effect inputs not replaced with current VAS inputs. | PASS_2_COMPLETE |
| S103 | All supplied current-trial between-arm tests match narrative exceptions effusion24/TG12; no equivalence inferred. | PASS_2_COMPLETE |
| S104 | Post hoc no-change statement resolved by adjacent between-arm context; within-arm data remain available. | PASS_2_COMPLETE |

## Provenance and bounded limitations

Current supplied-source CPU images independently viewed: preprocessing/statistical_pass_1/main-p06.png,result-p05.png,result-p06.png; preprocessing/inclusion_screener/results-p2.png; preprocessing/support_mapper/protocol-p04.png,protocol-p05.png; preprocessing/cross_source/protocol-p12.png. All are direct Poppler26.01.0 current-source renders recorded in their originating stage. Main methods and SAP were reread in the current-source direct layout derivatives; source-linked map bindings were consulted alongside the complete S inventory, ledger, screen and every mechanical recheck fact. No source or reused artifact was modified. No additional extraction/OCR/rendering was needed; interval arithmetic uses explicitly transcribed numbers above with JavaScript Math.hypot, CPU, and is completely printed in this finding.

Remaining definitions absent from the supplied evidence: exact model covariance, degrees of freedom, critical values, row-specific contrast/marginalization output, imputation implementation, exact adopted powering formula/efficiency assumptions, questionnaires/amendments and safety-relatedness mapping. These restrict exact statistical regeneration and remain named human questions; they do not leave a source-coverage gap.

Closeout:104/104 S relationships PASS_2_COMPLETE;13/13 stable candidates reconciled;24/24 initial screening decisions reviewed;49/49 upstream excluded rows audited;1 new finding;37 unique excluded observations. No scientific coverage gap, no candidate quota and no final adjudication.

