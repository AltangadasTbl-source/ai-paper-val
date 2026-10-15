# Statistical pass 2 — RAW-score shard

Fresh runtime: `/root/stat2_raw`; run model `gpt-6.1-sol`, reasoning effort `high`, fresh spawn distinct from `/root/stat1_raw`. Exact assignment: S601, S602, S603, S604, S605, S606, S607, S608, S609, S610, S611, S612, S613, S614, S615, S616, S617, S618, S619, S620, S621, S622, S623, S624, S625, S626. REPORT DOC-005 physical PDF pp.17–18, all 21 eTable11 outcome/time rows, 63 raw summaries, 63 GEE contrast/95%CI tuples,21 omnibus Ps, both notes and the summary/method/test families. Source-method context: REPORT DOC-005 pp.2,4–5,15–16 and DOC-001 pp.4,11. No other result display is assigned for fresh row-level checking.

QUALITY_CONTROL_SCOPE.md and the complete review contract were read. The complete current candidate ledger, screening log, mechanical recheck and literal packet of all 47 original checker excluded observations were read. Exact current-source renders were independently visually reread; OCR/text was a locator only. No legacy conclusions, web input, source modification or other Python was used. New native p2 text used the allowed pinned PyMuPDF1.26.4 fallback helper, CPU. Current p17/18, p15, p16, mainp4/p11 and methods p2/p4/p5 renders retain that engine provenance. Auxiliary numerical calculations use JavaScript and are preserved in `preprocessing/stat2_raw/calculation_record.md`.

All 26 relationships receive PASS_2_COMPLETE in `statistics/parts/pass2_raw.md`. All 63 points lie inside ordered intervals; all 63 raw centers lie inside ordered percentile bounds. Rounded additive contrast identities are feasible for all 21 rows. No pairwise P value, explicit standard error or statistic is printed. Omnibus versus one pairwise interval is not treated as the same null test. Physical3 P=.212 and all null-containing CIs reconcile at the .05 level; the other20 rows have a significant omnibus P and at least one null-excluding interval. No noninferiority, equivalence, interim or stopping statement occurs in this scope. The Fisher LSD gate is source-defined and no physical3 pairwise-superiority claim contradicts it. Raw medians are not equated with fitted means.

## Existing cross-lane implications

C016 already retains the p15 mean narrative versus p17 median/quartile labels, all 21 raw rows, five ordinary-PGIC-median diagnostics, both HC three-month PGIC cells and p18 note. Mechanical recheck confirms REPORT internal S_W, statistical_results: mainp11 scale definition is corroboration only. This question is not re-emitted. C003/C010 concern adjusted SMD columns absent from eTable11; no SMD values are transplanted into this raw display. C005/C006/C007/C011–C014 concern specified adjusted, weighted, imputed or subset models; p15 expressly identifies eTable11 as no adjustment, weighting or imputation, so those different-result comparisons are not matching numeric copies. C015's subset denominators do not supply the unreported eTable11 per-outcome sample sizes.

## New finding

### F-ST2-1001

**Observation:** The six- and twelve-month physical-function eTable11 omnibus P values do not reproduce under the common contrast/CI-to-Wald reconstruction that reproduces the other 19 rows of that display within their printed precision.

**Exact compared locations and document roles:** REPORT [DOC-005 p17, eTable11 Physical Functioning six- and twelve-month rows, all three MD/95%CI columns and omnibus P column](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=17). REPORT [DOC-005 p18 note b](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=18) defines unadjusted linear-GEE MDs and95%CIs. REPORT [DOC-005 p15 Additional Unadjusted Data and Analyses](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15) says this replicates Table3 without adjustment, weighting or imputation. REPORT [DOC-001 p11 Table3 note c](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) names a Wald omnibus test for differences among three groups; [p4 Statistical Analysis](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) states two-sided tests, alpha=.05, GEE and robust sandwich standard errors. Main method definitions corroborate the diagnostic family; they are not conflicting numeric copies and add no S_C relationship.

**Printed values:** Contrasts are PT−UC;HC−UC;HC−PT. Physical6:1.1(.3,1.9);.4(−.3,1.1);−.6(−1.4,.1); omnibusP=.005. Physical12:1.2(.4,2.0);.9(.0,1.8);−.3(−1.2,.6); omnibusP=.001. Both interval and omnibus columns are read exactly as printed.

**Rule and calculation:** Diagnostic reconstruction, explicitly labeled: a single fitted contrast vector a=PT−UC,b=HC−UC,c=HC−PT has c=b−a. For a normal95%CI, h=(upper−lower)/2, s=h/1.959963984540054. Its three contrast variances imply u=Cov(a,b)=(s_a²+s_b²−s_c²)/2; this is algebra inside the diagnostic method, not an asserted author covariance. The joint two-dimensional Wald statistic is Q=(s_b²a²+s_a²b²−2uab)/(s_a²s_b²−u²), with diagnostic chi-square2 tail exp(−Q/2). The supplied text's Wald/GEE family and reproducibility across the same table support testing this method; no unreported reference distribution is claimed as established.

All displayed points/endpoints receive ±.05 and displayed numeric Ps ±.0005. A precision-feasible search over additive points and symmetric CI halfwidths reproduces17 rows' <.001 reading plus social3's .001 and physical3's .212. Explicit witnesses include social3 d=(1.151,1.400,.249),h=(.899,.750,.701),Q13.411990,P.00122355; physical3 d=(.551,.552,.001),h=(.701,.798,.849),Q3.101588,P.21207957. All19 witnesses, their exact formulas and point/endpoint constraints are in the calculation record. The two physical rows do not reproduce: sampled diagnostic P ranges are [.015769,.039918] and [.003609,.020277]. These sampled ranges are not proofs or replacement Ps.

A separate conservative bound proves nonreproduction under this diagnostic method. Q is convex separately in the point vector and in its positive-definite covariance matrix; the latter is affine in the three contrast variances. Maximizing over vertices of an enlarged point/variance region therefore bounds every precision-feasible Q, including points not reached by a grid. Physical6 permits the point polygon (a,b) with vertices(1.05,.40),(1.05,.45),(1.10,.45) after enforcing c∈[−.65,−.55]; its enlarged halfwidth boxes are [.75,.85],[.65,.75],[.70,.80]. Thus Q≤8.556088 and P≥.01386977, exceeding printedP[.0045,.0055]. Physical12's enlarged rectangle a∈[1.15,1.25],b∈[.85,.95] and halfwidth boxes[.75,.85],[.85,.95],[.85,.95] give Q≤12.281126 and P≥.00215371, exceeding printedP[.0005,.0015]. All variance-box vertices used are positive definite. Ignoring point/halfwidth coupling enlarges each region, making these bounds conservative. Corresponding gap/printed-P values are(.01386977−.0055)/.005=1.673953 and(.00215371−.0015)/.001=.653711. Category1 is exempt from precision-based removal.

**Focus area:** B, C.

**Proposed review domain:** statistical_results.

**Proposed relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route A, category 1. This is an interval/test compatibility question under a method that reproduces other rows of the same display; the same-display method-reproduction principle prevents disposing of it solely because the exact CI/test mapping is unstated.

**Affected result or extracted value:** The unadjusted six- and twelve-month physical-function omnibus tests and their relationship to the three reported MD95%CIs. This can change extraction of their exact omnibus significance strength or which analysis the P values represent; all remain below.05 as printed, so no .05-level superiority reversal is asserted.

**Why context does not resolve it:** Route A category1 concerns the reported interval/test combination, not an isolated missing detail. The source identifies linear-GEE intervals and a replicated Wald-test display but does not identify why these two rows require a different mapping while the same calculation reproduces the other 19. Different analyses are an alternative to establish explicitly, not an automatic resolution.

**Source-grounded alternatives and exact missing definitions:** The actual eTable11 confidence critical value/reference distribution may differ from normal1.95996; omnibus reference distribution or degrees of freedom may differ from the two-dimensional chi-square diagnostic; CIs and omnibus Ps may use different covariance estimators or fitted analyses; or omnibus Ps may represent another estimand/time-specific comparison. The source does not explicitly map those choices to eTable11. No covariance, degrees of freedom, denominator, exact test implementation or replacement number is asserted from convention. Mainp11 describes the adjusted Table3 Wald family, while p15's replication phrase may be broader than an identical inferential implementation. This alternative is preserved rather than concealed.

**Exact human question:** Which fitted analysis, contrast covariance, confidence-interval reference distribution/critical value and omnibus test reference distribution/degrees of freedom produced the six- and twelve-month physical-function eTable11 tuples; do the printed P=.005/.001 and three MD95%CIs refer to the same outcome/time/model, and what reported values should be extracted if their inferential constructions differ?

## Excluded observations

Only apparent assigned-scope observations not emitted are listed. Reconciled checks are in the relationship records. The new physical-function question above replaces the corresponding original conditional exclusion.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-005 p17, PGIC remaining fractional centers: Pain PT3=2.9,UC3=1.9,HC6=2.1,UC6=2.1,HC12=2.1;General UC3=1.6,PT12=2.6,HC12=1.9,UC12=1.9 | Ordinary empirical integer/half-integer median-grid gaps after ±.05 are .05, relative .017241–.031250≤.05. These individual numeric occurrences do not exceed display precision; the overall summary-identity question remains C016. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-005 pp15,17–18, all 21 raw-column/contrast rows | Raw-center subtraction under printed PT/HC/UC order differs from fitted GEE MDs; an alternative UC/PT/HC permutation fits the21 triples within rounding. Raw columns are labeled medians and MD columns means; the source does not establish their equality. The permutation does not itself reproduce an arm-label or mean-difference conflict. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-005 pp15,17–18 and corroborating REPORT mainp11 PGIC definition | Mean versus median/quartile identity and the five precision-qualified ordinary-median locations have already been screened and retained in C016/F-XS-008, with F-ST1-601 explicitly duplicate. | DUPLICATE_OF_INCLUDED |

## Revisit of every original excluded-observation row

The ordinal below preserves literal packet order: numeric7,cross-source11,main-statistical7,report-statistical9,plan-statistical10,RAW3. All 47 were reread against all five Route A categories and the display-precision exception for category1. Reassessment outside assigned RAW relationships uses the full cross-lane ledger/recheck facts and retains its exact missing-input limits; it does not claim fresh independent row-level source review of every other shard. No observation already recorded as a finding in the screening log is re-emitted.

| Original row | Compact locator | Route A / precision reassessment |
|---|---|---|
| 01 | Numeric: pattern totals/visits/workbookD3 | Counts can engage A3, but all stated remaining relative gaps≤.05; original precision exclusion retained. |
| 02 | Numeric: baseline copies | Cross-location descriptive copies; subthreshold gaps retained. |
| 03 | Numeric: other reciprocalNNT/SMD | A4 requires reproduced >.05 point discrepancy; original residuals≤.05. C003/C004 already retain qualifying rows. |
| 04 | Numeric: eTables10/11 medians versus modeledMD | No source-defined equality; common raw-center method does not reproduce rows under their printed quantity definitions. C016 is separate; retain conditional observation. |
| 05 | Numeric: fidelity denominators | Missing training total prevents a contradicted complete partition; no A3 discrepancy established. Reviewed counts sum299. |
| 06 | Numeric: randomized/follow-up/weights | Explicitly distinct populations/weighted quantities; no matching-value discrepancy. |
| 07 | Numeric: approximately40% versus44% | Explicit approximation, not competing result extraction. |
| 08 | Cross: narrativeseveritySMD | Half-unit gaps0/.01;relative0/.0294≤.05. |
| 09 | Cross: adjusted versus alternative analyses | Model/population matching absent by explicit source labels; no same-result conflict. |
| 10 | Cross: eTable9 adjusted title | Adjacent unadjusted definition fixes analysis identity; no numeric slip or changed quantity remains. |
| 11 | Cross: eTable10 mean/median wording | Descriptive median and fitted-MD distinction is explicit; no numerical contradiction established. |
| 12 | Cross: plan interference wording/timing | Adjacent subscale and primary3-month window identify intended outcome; no A5 status/composite change. |
| 13 | Cross:140 versus454 calendar counts | Same boundary and explicit fitted subset size; peripheral administration remains outside A5. |
| 14 | Cross: workbook468 versus471 | Relative gap.00318≤.05, not reproduced A3 count mismatch. |
| 15 | Cross: eligibility operational omissions | Report does not affirm conflicting inclusion or population count; detail absence alone. |
| 16 | Cross: moderator/mediator timing/equation | Ancillary plan-internal elements do not change supplied primary/key-secondary result or decision rule. |
| 17 | Cross: PGIC/arm/outcome terminology | Adjacent scale/arm definitions identify assignments; no numeric or outcome-status conflict. |
| 18 | Cross: ancillary outputs absent | Plans do not designate these missing outputs primary/key secondary or report them as prespecified presented analyses; A5 not established. |
| 19 | Main-stat: severity6SMD | Remaining shared-SD gap.0417≤.05; does not remove C003's other qualifying rows. |
| 20 | Main-stat: severity3 narrative | Same subthreshold comparison as row08. |
| 21 | Main-stat: physical6 P=.05 gate | Printed P interval[.045,.055] permits gateP<.05; no interval-versus-P conflict asserted. |
| 22 | Main-stat: simulation sample size | Complete simulation unavailable; no method reproducing same-display rows established. A4 not established. |
| 23 | Main-stat: PGIC mean-change heading | Adjacent single-item change-impression scale resolves wording; C016 raw-summary identity is a different comparison. |
| 24 | Main-stat: intensity/interference scoring wording | No reported score in direct conflict; not A5 outcome status/composite change. |
| 25 | Main-stat: general benefit narrative | No explicit every-contrast claim conflicting with reported direction/null coverage. |
| 26 | Report-stat: pattern counts | Same subthreshold count/visit family as row01. |
| 27 | Report-stat: otherNNT points | Maximum excluded relative gap.048611≤.05; qualifying reciprocal pattern remains C004. |
| 28 | Report-stat: additionalCI-width/P diagnostics | Exact coefficient test/CI distribution and df unavailable; no same-display reproducing method established in packet. Existing direct null-significance rows remain C014. This row is not ignored merely because details are missing; the absent reproducing premise distinguishes it from RAW row47. |
| 29 | Report-stat: imputation coefficient direction | Conditional coefficients have no conflicting supplied direction statement; no sign reversal reproduced. |
| 30 | Report-stat: weight scale2331/2036 | Adjacent sums2036 and6108 identify weighted analysis size. |
| 31 | Report-stat: baseline severity omitted list | Adjustment narrative and both complete fits explicitly contain it; omission does not create a competing fitted analysis. |
| 32 | Report-stat: eTable9 title | Same immediately resolved unadjusted definition as row10. |
| 33 | Report-stat: eTable10 medians/mean effects | Different named summaries; not same quantity. |
| 34 | Report-stat: VC labels | Arm identity evident; no result reassignment. |
| 35 | Plan-stat: sample-size normal diagnostics | Stated REPORT simulations differ from unstated normal algorithms; no method reproducing other rows established. |
| 36 | Plan-stat: relative change terminology | Active/UC table ratio explicit and arithmetic coherent. |
| 37 | Plan-stat: interference intensity word | Adjacent seven-item definition resolves wording without changed numeric outcome. |
| 38 | Plan-stat: missing measurement3-month cell | Adjacent primary timeframe and analytic text supply3months; no planned primary/key-secondary analysis absent. |
| 39 | Plan-stat: moderator6/3-month comparison | Ancillary plan-internal comparison; no changed primary/key-secondary fitted result. |
| 40 | Plan-stat: mediation equation confounder term | Ancillary unfitted result; no relevant reported primary/key-secondary value supplied. |
| 41 | Plan-stat: support mediator baseline | Protocol explicitly designates notification survey as baseline. |
| 42 | Plan-stat: historic30 versuscurrent60-day eligibility | Disclosed history/current definition difference does not establish a changed reported analysis count/result. |
| 43 | Plan-stat: qualitative framework list counts | Not trial numeric result or statistical design quantity. |
| 44 | Plan-stat: hospitalization review update | Disclosed SAP update resolves procedure; no altered event definition/status established. |
| 45 | RAW: remaining fractionalPGIC centers | Half-unit/grid relative gaps≤.05; retained in excluded-observation table above. |
| 46 | RAW: raw columns/mean contrasts | Median-versus-model-mean equality absent; retained conditional observation above; C016 covers summary identity. |
| 47 | RAW: physical6/12 omnibus reconstruction | Reopened after an explicit same-display reproduction across19 rows and conservative half-unit bounds; emit F-ST2-1001. Unknown inferential definitions remain exact human questions. |

## Counts and limitations

Pass2:26 assigned S IDs complete;21 row tuples;1 consolidated new finding, affectingS614,S615,S625;3 excluded observations;47 original exclusions reread,46 retained and1 reopened. Complete ledgerC001–C017,26 finding screen decisions and all 17 mechanical recheck cards read. No source-reading gap exists for assigned eTable11 pages. Actual eTable11 sample sizes, outcome-specific missing-data denominators, confidence reference distributions/critical values, test reference distribution/df, exact omnibus-to-CI variance mapping, unrounded tuples and participant-level observations remain unavailable. Diagnostic witnesses establish numerical same-display reproducibility, not the actual fitted implementation or a proposed replacement. No severity, validity, disposition or candidate ID is assigned.
