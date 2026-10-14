# Independent Quality-Control Audit

Runtime agent: 01a12c01-a608-7bc0-b71b-7490dfdfa493. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. This is the mandatory independent audit after both statistical passes, screening, registration and exact-source recheck. Scope: C001, C002, C003, C004, C005, C006, C007; all 203 direct-source units; N001–N131; S001–S132; every checker finding and excluded-observation row; all classifications and execution records. All stable IDs remain Pending Human Adjudication.

QUALITY_CONTROL_SCOPE.md and the complete review contract were read. The new main map and every authored per-page map, relationship description and source locator in all seven support parts were read in bounded batches. Pagewise transcription appendices were checked as coverage aids, with exact current-source readings used for candidate and disputed screening facts. Truncated bulk outputs were revisited in bounded portions; no truncated output established completeness. The canonical support merge, inventories, screening, ledger, recheck, four checker artifacts, coverage manifest, source coverage, routing, tooling, run state and execution manifest were audited. No older candidate, decision, classification or report was a scientific input, and no external evidence was used. No candidate-count target controlled this audit.

## Coverage, integrity and routing audit

| Audited requirement | Independent result |
|---|---|
| Complete direct-source inventory and content roles | Three PDFs, no supplied Office/CSV source. DOC-001 is REPORT, DOC-002 is a non-plan results REPORT, DOC-003 is PLAN throughout, including its prospective protocol/SAP versions and amendments. Roles are established by content. |
| DOC-001 partition and closure | 11 reusable + 0 fresh-required = 11 total; 11 mapped, COMPLETE. All 11 pages have individual map rows, including references-only p11. |
| DOC-002 partition and closure | 25 reusable + 0 fresh-required = 25 total; 25 mapped, COMPLETE. All operational, raster-figure and table pages have individual map rows; empty p12 OCR is covered visually from its source-linked image. |
| DOC-003 partition and closure | 165 reusable + 2 fresh-required = 167 total; 167 mapped, COMPLETE. Fresh raster-table inspections on pp46/48 close the reusable gaps. The otherwise blank p144 and line-number-only p167 are explicitly mapped. |
| Total source coverage | 201 reusable + 2 fresh-required = 203 total; 203 mapped. No scientific coverage gap. The seven support parts partition 25 + 32 + 32 + 32 + 32 + 32 + 7 = 192 pages, disjoint from 11 main pages. |
| Numeric inventory | 131 distinct stable N records, each explicitly COMPLETE. Grouped cells retain complete source arrays and do not select significant or interesting rows. |
| Statistical inventory | 132 distinct S records, all explicitly PASS_1_COMPLETE and PASS_2_COMPLETE. Every displayed treatment result, interaction and PH test is represented with the applicable model, null and named missing inputs. |
| Statistical-agent separation | Pass 1 runtime 01a12bd6-b838-7691-a3a4-d96d154fa89c and pass 2 runtime 01a12bfa-a0fa-7f83-ab7f-56520b3f2690 are distinct fresh gpt-6.1-sol/high agents. Pass 2 began after the complete ledger/screen/recheck gate. |
| Independent inclusion screen | Runtime 01a12bda-b512-7c60-aec2-49d5c05b840c is a distinct fresh gpt-6.1-sol/high agent. Fifteen checker findings have exactly one screening decision each. Pass 2 emitted no new findings, so a second screener is not applicable. |
| Execution manifest | Coordinator is listed once. All completed mandatory specialists and optional mapper shards have distinct runtime IDs, fixed run model, required effort and one primary artifact. This audit's row and the future report-generator row are coordinator-managed completion entries. No stage promotion or effort substitution was observed. |
| Coverage manifest | Every examined row has exactly one plain relative artifact path. Source assignments are disjoint; canonical merge rows are explicitly joins rather than additional source units. Both statistical scopes enumerate all S IDs; candidate scopes enumerate all seven C IDs. Audit/report rows are legitimately IN_PROGRESS at this pre-report stage and require completion after their artifacts exist. |
| Source identity and integrity | Direct-source SHA-256 checks and all 472 reused-asset SHA-256 checks independently passed with sha256sum --check --quiet. No direct source or reused artifact was modified. Final before/after hash files remain a coordinator completion requirement. |
| Local evidence links | Mechanical Perl filesystem checks of ledger, screening, recheck and all checker Markdown links found zero unresolved local links. PDF evidence uses actual physical #page=N anchors. No contents-page pointer is substituted for actual SAP pagination. |
| Evidence precedence | Current PDF source readings govern; reusable text/OCR/images serve as locators. The source disability threshold ≥2 supersedes derivative >2. Original SAP BMI line2358 was corrected before registration, so it does not require a post-registration transcription evidence state. |
| Discovery independence | New maps span every supplied page and include noncandidate numeric families, full outcome lists and disclosed amendments. Checker records document complete source gates and no old scientific inputs. Neither elapsed-time target nor previous asset naming established candidate scope. No count calibration was observed. |

## Inclusion and classification summary

| ID | Review domain | Relationship type | All relationships | Evidence state | Inclusion audit | Independent qualifying reason |
|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | reproduced | CONFIRMED | Route A5: the exact reported BMI partition called prespecified is absent from all supplied subgroup specifications. |
| C002 | statistical_results | S_C | S_C, S_W | reproduced | CONFIRMED | Route A3: exhaustive S7 totals do not reconcile within one display; Route B additionally applies to conflicting matched PP population sizes. |
| C003 | statistical_results | S_C | S_C | reproduced | CONFIRMED | Route B: matching primary observed counts differ beyond precision without a stated population/window change, changing extractable event counts. |
| C004 | statistical_results | S_W | S_W | reproduced | CONFIRMED | Route A1: the point lies outside its own interval, which excludes zero beside a nonsignificant same-row test. |
| C005 | statistical_results | S_W | S_W | reproduced | CONFIRMED | Route A3: a literal count, percentage and denominator within one figure do not reconcile beyond precision. |
| C006 | protocol_report | P_R | P_R | reproduced | CONFIRMED | Route B: explicit planned Fisher and reported chi-square test specifications differ, leaving producing-method identity unclear. |
| C007 | plan_material | P_P | P_P | reproduced | CONFIRMED | Route B: a printed original event forecast and its one-year risk/allocation inputs do not connect; the extractable original design quantity remains unclear. |

Classification precedence P_R > P_P > S_C > S_W is satisfied. The seven evidence states agree with the exact-source recheck. Every conflicting location has its content role assigned. Corroborative locations are kept separate from actual relationships. All seven candidates concern counts, estimates, tests or statistical specifications, so none requires report_internal_inconsistency instead of its assigned domain. Domain totals are statistical_results 4, protocol_report 2, plan_material 1, report_internal_inconsistency 0; primary relationship totals are S_W 2, S_C 2, P_R 2, P_P 1.

## C001 — BMI subgroup partition and prespecification

**Inclusion audit:** CONFIRMED. The source reproduces a two-level REPORT BMI partition <25/≥25 under an explicit prespecification claim, against three PLAN levels <25/25–30/≥30 in both protocols and both SAPs. Route A, category 5 applies; this is an analysis definition, not a group-name variation. Directly inspected [main Figure2 p7](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=7) and [final SAP p160 line2768](../../../joi240088supp2_prod_1746815064.36071.pdf#page=160); the remaining source locations and report prespecification sentence are independently source-read in the current per-page locators. The HR .48(.21–1.11) and interaction .17 belong to the combined upper group; no three-level HR/P is inferred. Display precision is inapplicable to this categorical comparison.

**Classification audit:** Retain protocol_report/P_R/all P_R/reproduced. The agreeing PLAN versions do not add P_P. **Card and impact audit:** Retain all seven directly conflicting pages and pre-registration line2358 annotation; identify an additional dated prespecification as missing. The potential impact is the status and contrast of the named BMI interaction, not the overall treatment conclusion. Do not state that pooling necessarily caused a numerical or clinical change. An unsupplied grouping amendment remains an alternative, not a source fact.

## C002 — Sensitivity-analysis population headers

**Inclusion audit:** CONFIRMED. [TableS7 p20](../../../joi240088supp1_prod_1746815064.21247.pdf#page=20) visibly gives 233+238=471 arm participants and exhaustive site totals 256+245=501. Half-unit sum intervals [470,472] and [500,502] leave 28/471=.05944798>.05, qualifying by Route A3. [TableS8 p21](../../../joi240088supp1_prod_1746815064.21247.pdf#page=21) labels PP but headers 249/252 differ from source-confirmed PP233/238 in main flow and S10: gaps15/249=.06024096 and13/252=.05158730. These are analysis-population sizes, so not peripheral time-point counts; Route B names the PP primary HR .27 and component denominators as affected extractable quantities.

**Classification audit:** Retain statistical_results/S_C/all S_C, S_W/reproduced. Cross-REPORT population copies and within-supplement totals both exist; S_C has precedence. **Card and impact audit:** Both tables and every S8 component row must remain one recorded repeated sensitivity-header pattern, without asserting a shared production cause. Do not claim each percentage independently exceeds the scope threshold. The S8 33/252 percentage residual is .0381237753 relative after half-unit propagation, still ≤.05; the checker diagnostic annotation is repaired separately below. Unprinted actual denominators remain the human question. No changed HR or significance is established by header counts alone.

## C003 — Center-adjusted primary event count

**Inclusion audit:** CONFIRMED. The [main primary table p8](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8) and overall forest row print11(4.4) under BA249, while [TableS6 p19](../../../joi240088supp1_prod_1746815064.21247.pdf#page=19) prints9(3.9) under BA249 for the matched first-year composite. Count intervals [10.5,11.5] versus[8.5,9.5] leave1/11=.09090909; percentage intervals[4.35,4.45] versus[3.85,3.95] leave.40/4.4=.09090909. Both exceed.05. Route B: primary observed counts are in focus, the source does not identify a restricted descriptive cohort/window, and the extractable balloon event count/risk differs. Adjustment of a modeled coefficient does not itself explain a changed observed n(%).

**Classification audit:** Retain statistical_results/S_C/all S_C/reproduced. Matching main occurrences only corroborate one side, and the separately screened prospective-status wording is not a PLAN relationship for this ID. **Card and impact audit:** Distinguish observed counts from adjusted HRs; .32(.16–.62) and .32(.16–.63) are not independently conflicting effects. Retain complete-case or another subset as an unconfirmed alternative. No claim that two events were actually excluded or that the primary superiority inference changes is supported.

## C004 — Outside-territory stroke difference interval

**Inclusion audit:** CONFIRMED. Exact [main Table2 p8](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8) visibly prints−.4(−2.4 to−1.7), HR.76(.17–3.40), P=.72. The point−.4 is greater than its upper limit−1.7. Even point[−.45,−.35] and upper[−1.75,−1.65] remain separated by at least1.20. Route A1 applies independently of any difference/Cox analysis attribution and is never screened as rounding. The binomial Wald diagnostic d=100(3/249−4/252)=−.38248231 and CI[−2.43616260,+1.67119798] also reproduces the other distinct difference rows, supporting an alternative reading without assigning it as an authoritative correction.

**Classification audit:** Retain statistical_results/S_W/all S_W/reproduced. **Card and impact audit:** Carry the separate-analysis alternative, actual confidence/significance conventions and absent CI-construction method. For a precision-aware diagnostic comparison, use upper-input range[+1.26489617,+2.07808401], gap2.91489617/1.7=1.71464481; a fixed-point diagnostic gap elsewhere is not the full input-propagation result. Bound impact to the outside-territory difference interval/null interpretation; this interval is not the primary efficacy CI. No replacement sign/value is adjudicated.

## C005 — Ninety-day mRS count and percentage

**Inclusion audit:** CONFIRMED. Current [FigureS4 p13](../../../joi240088supp1_prod_1746815064.21247.pdf#page=13) visibly prints BA249, mRS2 2.0(N=50). Independent arithmetic gives50/249×100=20.080321%; half-unit recomputed range[19.83967936,20.32193159] versus printed[1.95,2.05] leaves17.78967936/2=8.89483968>.05. The seven counts sum294; conservative half-unit total[290.5,297.5] versus[248.5,249.5] leaves41/249=.16465863. Route A3 qualifies even when a plausible intended count can be reconstructed.

**Classification audit:** Retain statistical_results/S_W/all S_W/reproduced. Main mRS inference is corroborative only; no cross-REPORT conflict is claimed. **Card and impact audit:** Preserve all seven printed categories, percentages and N249; do not silently use hypothetical5 or replace the distribution. The human question is the count/full ordinal input distribution. Downstream extraction of literal50 changes the supplied distribution; its effect on the actual fitted OR, CI or paper conclusion cannot be established from supplied data.

## C006 — Safety-test specification

**Inclusion audit:** CONFIRMED. Source [SAP p142](../../../joi240088supp2_prod_1746815064.36071.pdf#page=142) and [p162](../../../joi240088supp2_prod_1746815064.36071.pdf#page=162) specify grouped-AE Fisher testing, whereas three [TableS11 p24](../../../joi240088supp1_prod_1746815064.21247.pdf#page=24) rows explicitly carry chi-square footnote c. Route B: the prospective producing-test specification is in focus; no grouped-AE amendment/selection rule identifies the switch; which analysis produced .84, .35 and .02 remains an extraction question. The report's other twelve rows explicitly carry Fisher footnote d, strengthening the method-identity comparison. The source disability threshold is ≥2, resolving the derivative-only >2 observation.

Independent probability-ordering Fisher sums from counts12/14,7/12,6/18 and N249/N252 give.84091616,.35005961,.01962102, reproducing the recheck. The continuity-corrected chi-square alternatives .86496491,.36336038,.02313867 remain compatible after P half-unit allowances, with relative gaps.02376775,.02388680,0. Therefore no independent P/significance conflict is established, and no preferred chi-square variant is imposed.

**Classification audit:** Retain protocol_report/P_R/all P_R/reproduced. Agreeing plans and corroborative main P=.02 do not create additional relationships. **Card and impact audit:** Retain all three rows and both footnotes as one repeated method-label pattern. Impact is producing-test identity of the specified safety results; no altered significance, safety benefit or methodological preference is established.

## C007 — Original planned event forecast

**Inclusion audit:** CONFIRMED, with a strict historical-design boundary. Exact [original synopsis p11](../../../joi240088supp2_prod_1746815064.36071.pdf#page=11) prints686 and estimated total91 endpoint events alongside first-year arm risks12.2%/6.25%; [p18](../../../joi240088supp2_prod_1746815064.36071.pdf#page=18) supplies1:1 allocation and12-month primary hypothesis. The expected first-year count is343×(.122+.0625)=63.2835. Half-unit inputs give[63.0488625,63.5184125] versus91±.5, leaving26.9815875/91=.29650096>.05. The source risk-rate adjustment lowers rather than raises expected first-year control risk. Route B: a printed plan event/sample-size quantity is in focus; the synopsis does not identify another endpoint horizon/information/accrual quantity connecting91 to686; the original event-information quantity a reader extracts differs. The main article explicitly describes the original802 design history, establishing supplied-report relevance without turning corroboration into P_R.

**Classification audit:** Retain plan_material/P_P/all P_P/reproduced. **Card and impact audit:** Required-event target versus expected first-year count is an unresolved source-grounded alternative, not proof of a specified software-calculation failure. Preserve “90% confidence” without converting it to power. Visits through3 years do not themselves define the horizon for91 because the primary hypothesis is12 months. The explicitly disclosed revised512 design is outside this candidate's claimed discrepancy. Limit extraction impact to original91-event/686→728→802 history; no inference that the final analysis depended on91, or that final512 power or the reported primary result changes, is supported.

## Independent screening audit in both directions

Every one of the15 initial finding rows was audited against its exact compared content, routes and cross-location tiers. Seven INCLUDE decisions are supported by the candidate analyses above. The six DUPLICATE_OF_INCLUDED decisions preserve every location and do not suppress an independent issue.

| Finding | Effective decision audited | Audit reason |
|---|---|---|
| F-NUM-001 | INCLUDE → C005 | Exact-source literal50/2.0/N249; Route A3. |
| F-NUM-002 | INCLUDE → C003 | Matched primary counts11 versus9; Route B. |
| F-NUM-003 | INCLUDE → C002 | S7 within-display totals plus PP population copies; Route A3/Route B. |
| F-NUM-004 | INCLUDE → C004 | Point/interval and interval/test conflict; Route A1. |
| F-XS-001 | INCLUDE → C001 | Prespecified exact BMI partition differs; Route A5. |
| F-XS-002 | SCREENED_OUT, TERMINOLOGY_OR_WORDING | Generic planned center sensitivity is reported; the caption's exact Tiantan-versus-rest grouping can be post hoc. Neither absent planned primary sensitivity nor conflicting actual producing covariate model is established by wording alone. This is not an analysis called prespecified but absent from the plan; Route A5 is not reproduced. Doubtful prospective-status wording is screened out under the normative instruction. C003's independent count discrepancy remains. |
| F-XS-003 | SCREENED_OUT, DUPLICATE_OF_INCLUDED → C003 | Same matched primary count; all main/alternative-population locators retained. |
| F-XS-004 | SCREENED_OUT, PERIPHERAL_COMPARISON | .4% versus .8% is numerically reproduced, but is a cross-location unranked secondary one-year mRS/death copy. Neither an abstract result nor a prespecified key secondary result, changed primary population or decision rule is established. No within-display above-precision conflict is hidden by this reason. An unexplained copy difference alone does not demonstrate a substituted digit under Route A2. |
| F-ST1-001 | SCREENED_OUT, DUPLICATE_OF_INCLUDED → C004 | Same interval; Wald diagnostic and test conventions retained. |
| F-ST1-002 | SCREENED_OUT, DUPLICATE_OF_INCLUDED → C001 | Same BMI partition; all four planned occurrences retained. |
| F-ST1-003 | INCLUDE → C006 | Planned/report producing-test specification; Route B. |
| F-ST1-004 | SCREENED_OUT, DUPLICATE_OF_INCLUDED → C005 | Same literal figure count and distribution. |
| F-ST1-005 | INCLUDE → C007 | Original event-quantity gap; Route B with historical boundary. |
| F-ST1-006 | SCREENED_OUT, DUPLICATE_OF_INCLUDED → C002 | Same sensitivity-header pattern; every S8 row retained. |
| F-ST1-007 | SCREENED_OUT, DUPLICATE_OF_INCLUDED → C003 | Same center-adjusted primary count; main narrative retained. |

No screening decision reversal, added audit screening row or new F-QA finding is required. Existing IDs were not deleted, merged, ranked or suppressed.

## Excluded-observation audit

The15 numeric,15 cross-source and18 pass-1 rows were independently reconsidered, not accepted solely because pass2 retained them. Pass2's48-row audit and33-row consolidated catalogue were also read in full. Each ordinal below refers to the original checker table, not a new finding identifier. No excluded row conceals a reproduced Route A conflict. Every ROUNDING_OR_DISPLAY_PRECISION row was evaluated against its half-unit gap/absolute printed value, rather than ordinary rounding plausibility alone.

| Checker and row ordinals | Independent audit result |
|---|---|
| Numeric01–02 | Age mean/median label alone and11 versus10+1 flow description: wording/immediate context, no competing printed result/population count. Retain existing codes. |
| Numeric03 |343/501 versus69.1: recomputed[68.295115,68.631369], printed[69.05,69.15], gap.418631/69.1=.00605834≤.05. |
| Numeric04 |77/249 versus30.1: recomputed[30.661323,31.187123], printed[30.05,30.15], gap.511323/30.1=.01698746≤.05. |
| Numeric05 |51/252 versus20.5: recomputed[20,20.477137] overlaps[20.45,20.55]; zero gap. |
| Numeric06 |25/249 versus10.4: recomputed upper10.261569, printed lower10.35; gap.088431/10.4=.00850294≤.05. |
| Numeric07 |131/215 versus61.9: recomputed upper61.305361, printed lower61.85; gap.544639/61.9=.00879869≤.05. |
| Numeric08 |9/249 versus3.9: recomputed upper3.822938, printed lower3.85; relative gap.00693907≤.05. Independent C003 count-copy issue is retained. |
| Numeric09 |Every S8 count/percentage pair is below.05 after input half-units; largest relative gap33/252 versus13.9 is.0381237753. C002 independently retains conflicting population copies. The numerical annotation repair does not change the exclusion. |
| Numeric10 |ATS249/252 versus247/254 half-unit gap1/reference is≤.0040161; no above-threshold copy discrepancy. |
| Numeric11 |AMM one-year category sum249 versus252: total intervals overlap;169/252 versus67.9 has relative gap.00669181. Other categories reconcile within precision. The separate peripheral death-copy screen is not replaced by this arithmetic test. |
| Numeric12–14 |Procedural perforation copy is peripheral; Cox-versus-crude estimates concern different quantities; TableS11 “other” SAE overall is not defined as an exhaustive union including every listed stroke endpoint. No reproduced Route A contradiction. |
| Numeric15 |15%/7% half-units permit48.276–58.065% relative reduction and overlap50±.5. |
| Cross01–03 |Source≥2 matches; amendments disclose the final design; one-sided.025/two-sided.05 are different specified quantities with source-matched final reporting. No reproduced conflict. |
| Cross04 |6.25% versus6.1% intervals leave.095/6.1=.01557377≤.05. |
| Cross05–06 |Confidence is not explicitly power; historical source-arm terminology does not assign a contrary BASIS treatment risk. No invented matched quantity. |
| Cross07–09 |Detailed diabetic BP target appears in supplied report supplement; an exclusion>15mm does not establish retained10–15mm; missing unranked restenosis OR alone is not missing primary/key secondary analysis under A5. |
| Cross10–12 |Ordinal replacement is explicitly disclosed; short endpoint label is resolved by the full definition; analysis-set names do not establish different numeric populations. No analysis called prespecified but absent or changed outcome status was concealed. |
| Cross13–15 |Baseline copies, calendar/visit copies and superseded original eligibility description do not establish a changed qualifying result, population size or final planned decision rule. Peripheral codes retained. |
| Statistical1-01–04 |Source glyph matches; stratum treatment intervals and interaction P test different nulls; unstable-fit possibility has no printed contrary interval/test; half-tie generalized-OR convention gives compatible1.20745. LiteralN50 remains C005. |
| Statistical1-05 |One-year WMW diagnostic.004838 versus.01±.005 leaves.000162/.01=.0162≤.05; no opposite CI/P significance. |
| Statistical1-06–09 |Disclosed ordinal replacement, generic center sensitivity versus specific post hoc implementation, unranked restenosis omission, and confidence/power terminology do not reproduce A5 or another qualifying contradiction. |
| Statistical1-10 |Inverse-retention input interval[803.87,813.97] versus802±.5 leaves≈1.37/802=.0017≤.05; no mandated software formula is assumed. |
| Statistical1-11–12 |ATS tiny header-copy gaps and one-year AMM distribution arithmetic remain≤.05 or overlapping as above. |
| Statistical1-13–14 |Unranked secondary death copy remains peripheral;12.2% versus12% intervals overlap. |
| Statistical1-15–18 |Different specified alpha sidedness,50% versus input risk intervals, operational visit copies and BP detail/summary context do not establish a qualifying contradiction; precision calculation retained where applicable. |
| Statistical2 consolidated01–33 |All33 consolidated rows map back to the above48 reviewed occurrences. Consolidation preserves the observations and existing candidate boundaries; each has one permissible reason code. Row-number ranges here document audited coverage, not a finding limit. No additional apparent issue is left without threshold review. |

Very small display-zero P values are not the basis of any candidate. Nonsignificant interaction P values are not paired with within-stratum intervals as if they test the same null. Missing event times, ranks, covariance or software settings do not by themselves produce a candidate.

## Supportable repairs and report-card requirements

| Repair / completion item | Reason and required action |
|---|---|
| Numeric09 and pass2 reprise, S8 percentage diagnostic — COMPLETE | Coordinator corrected both current checker annotations from .03774 to .0381237753 for(13.85−100×33.5/251.5)/13.9 and retained the prior diagnostic as provenance. The formula, interval rule and exclusion remain unchanged; scientific classification/screening unaffected. |
| Historical C007 wording | Keep the event forecast comparison explicitly first-year and the quantity/horizon uncertain. Report must not expand this into a claim about final512 power or the primary finding. Existing ledger/recheck already contain the needed alternatives and boundary. |
| S010 diagnostic precision presentation | Use the full propagated upper-input interval and gap in the final card; identify any fixed-point comparison as a diagnostic point calculation. Existing ledger/recheck contain the full precision result. |
| Ledger audit fields | Coordinator writes CONFIRMED for each of C001–C007, retaining reproduced evidence states and the unchanged domain/type/all-relationships values. This is an inclusion audit, not human adjudication. |
| Report-only card fields | Report not yet assembled when this fresh audit began. Every card must copy the ledger classification fields, exact compared roles, included finding IDs and evidence state; include reported-versus-comparator, source evidence, reasoning/calculation, mechanical recheck, alternatives, missing definition, named affected value, bounded potential downstream impact and human question. Recheck facts supply these fields; no unsupported assumption is needed. |
| Final administrative completion | Add every actual runtime once to the manifest, close audit/report coverage rows, finalize timing fields immediately after Markdown assembly, recompute unchanged source/reuse hashes, render standalone HTML, remove only the temporary fallback environment, complete tooling removal record, and obtain validator PASS. These are prospective completion items, not scientific gaps or completed-report claims. |

The current ledger/recheck contain support for all evidence-card requirements. No missing candidate-source location, arithmetic dependency or classification field requires a new candidate. The report must reproduce all seven stable IDs and all seven classifications; equality with a future report cannot be claimed before it exists and remains an explicit coordinator/report-validator check.

Neutral-language audit found no prohibited characterization of a candidate, value or authors' work in the authored scientific decisions. Occurrences in retained source transcriptions are established statistical/clinical terms such as standard error, type I error and `visual defect`; they are not descriptions of the authors' reporting. No severity, scientific disposition, acceptance, ranking or final correction is assigned.

## Provenance, limitations and completion

No new derivative was needed. Existing current-run exact-source locators and source-matched renders were independently inspected. Images inspected for decisive printed readings: preprocessing/stat1-main-p8.png, stat1-supp-p13.png, stat1-supp-p24.png, evidence_rechecker/plan-p11.png, evidence_rechecker/main-p7.png, evidence_rechecker/plan-p160.png, stat1-supp-p19.png, screen-supp-p20.png and stat1-supp-p21.png. Engine provenance from the producing current reviewers is supplied pdf_tools.py/PyMuPDF1.26.4, CPU,200dpi; locators use its sorted native text mode. No OCR or GPU computation was required for this audit. Read-only shell/Perl verified hashes, source partition, pass completion and local links; JavaScript arithmetic independently reproduced precision intervals and probability-ordering Fisher sums. These computations did not select or classify candidates.

Named analytical limitations: individual event times and ranks, exact Cox options and interaction covariance/convergence, generalized-OR CI algorithm, actual chi-square variant, and original sample-size/event-information/accrual equations are unavailable. They constrain reconstruction of producing analyses while all203 source units remain scientifically mapped. Report generation, final timing, final before/after hash artifacts, HTML rendering, temporary-environment removal and validator execution follow this audit and were not represented as already complete.

Audit ID set: C001, C002, C003, C004, C005, C006, C007, exactly equal to ledger and recheck. Inclusion audit counts: CONFIRMED7, QUESTIONED0. Initial finding decisions audited15; original exclusions audited48; pass2 consolidated exclusions audited33. New F-QA findings0; screening reversals0; supportable arithmetic annotation repairs1; classification changes0; scientific coverage gaps0. All stable candidates remain Pending Human Adjudication.
