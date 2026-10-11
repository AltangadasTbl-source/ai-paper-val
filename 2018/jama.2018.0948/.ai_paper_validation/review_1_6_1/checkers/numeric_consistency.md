# Numeric consistency review

Scope: all 110 canonical grouped relationships N001–N065 and N101–N145, all component cell tuples in both fresh quantitative evidence maps, and all 69 mapped direct-source pages. Complete numeric stage. Findings: 0. Excluded observations: 15 consolidated patterns. No candidate IDs assigned.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely. Sources used: main REPORT jama_parshuram_2018_oi_180015.pdf (11 pages); PLAN joi180015supp1_prod.pdf (37 pages); PLAN joi180015supp2_prod.pdf (7 pages); REPORT joi180015supp3_prod.pdf (14 pages). Source-matched maps and canonical inventory were scientific locators; no legacy checker, screening, candidate, or report conclusion used. Direct pdftotext 25.03.0 was used to reread main pp.3,5–6, supplement REPORT pp.9,11–14, and protocol pp.14–15,29–30. Available tooling follows tooling_record.md. No web, Python review orchestration, OCR, or GPU used.

## Explicit relationship coverage

Each listed ID received NUMERIC_REVIEW_COMPLETE, including every component in its group. The following partition enumerates all 110 IDs once. Checks include count/rate identity, means and dispersions, range containment, sum relationships, repeated-value matching with population/time/denominator identification, and effect-measure identity. Statistical-method or design distinctions remain available to their mandatory specialist lanes; this review does not interpret an absent covariance matrix as a numerical contradiction.

| IDs | Numeric checks and result |
|---|---|
| N001, N002, N003, N004, N005 | Screened/randomized/completed/withdrawn hospitals, arm totals, follow-up and durations reconcile after distinguishing 23 randomized from 21 analyzed. Administrative counts not substituted for analysis populations. |
| N006, N007, N008, N009, N010, N011, N012 | Means equal arm totals divided by hospital count within half-unit precision; ranges contain means; baseline and intervention arm sums reconcile. Two cross-document range endpoints are peripheral (excluded below). |
| N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025 | Every hospital n/% cell checked against 10/11; size and ward staffing category sums checked; ICU category exhaustiveness is not established. Beds, nurse FTE quantities and ICU discharges kept distinct. |
| N026, N027, N028, N029, N030, N031, N032, N033, N034, N035 | All documentation n/% tuples, four-column mean/SD tuples, raw and Holm P labels, narrative repetitions and assessment sums reviewed. Adjusted contrasts not replaced by crude differences. |
| N036, N037, N038, N039, N040, N041, N042 | Every primary/key-secondary count/rate tuple and repeated occurrence reconciles with supplied discharge/day denominators; DNR and urgent-admission fractions reconcile. |
| N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053 | Every Table 3 count/rate tuple checked with correct denominator; all exploratory event totals and preventable fractions checked. ICU post-discharge denominators are not directly supplied; no invented denominator. OR and rate-ratio labels agree with stated links. |
| N054, N055, N056, N057, N058, N059 | ICU patient/event distinction, rounded mean-to-total relationships, hospital zero/low-death counts, mortality range and relative CI-width narrative checked. Plot coordinates matched to exact hospital table rather than treated as printed pixel values. |
| N060, N061, N062, N063, N064, N065 | Sample-size inputs, windows, documentation revision, estimator adjustment distinctions, outcome hierarchy and dates reviewed. No uniquely specified power formula printed; no unsupported reconstruction asserted. |
| N101, N102, N103, N104, N105 | Allocation, timing, sample frequency, outcome windows, analysis variables/weights examined for numerical identities and definition-specific denominator matching. Design comparisons belong to cross-source/statistical lanes. |
| N106, N107, N108, N109, N110 | All mortality/SCDE/code-blue/stat-call power inputs and printed reductions reviewed; historical sums/rates not substituted for trial denominators. Unit slips resolvable from context excluded below. |
| N111, N112, N113, N114, N115, N116 | All SAP numerator/denominator/link/offset/time-scale and per-patient aggregation specifications examined. No result computed from illustrative code asserted without executed output. |
| N117, N118, N119 | All 21 mortality hospital coordinates linked to their exact table values; histogram populations/visual bins and outcome-scale/window definitions checked without inventing precise bar percentages. |
| N120, N121, N122 | All 21 discharge B/P/total rows, four arm aggregates, all 84 hospital mortality/no-DNR count-rate pairs and aggregate pairs checked. Every row total and arm-column sum reconciles; all rates reconcile within displayed precision. |
| N123, N124, N125, N126 | All 21 patient-day B/P rows and all 126 hospital SCDE/arrest/preventable count-rate pairs plus aggregates checked. Every arm-column sum reconciles; all displayed rates reconcile. Preventable counts never exceed arrest counts. |
| N127, N128, N129, N130, N131, N132, N133, N134, N135, N136, N137, N138, N139, N140, N141, N142 | All 19 eTable 4 descriptive rows and 15 modeled contrast triples reviewed. Every observed binary n/% tuple matches its period-specific 393/686/531/967 population. Predicted counts retain half-unit intervals. Means/SDs and median/IQR relationships and known score bounds coherent. |
| N143, N144, N145 | Entire anticipated/actual eTable 5 population/event/rate/variation table reviewed. Historical score tables retained as contextual PLAN material, not trial-result comparisons. |

## Reproduced numerical checks

Counts are exact integers when observed, not rounded measurements. A displayed d-decimal measurement retains its half-unit interval ±0.5×10^-d; a rate or percentage passes if the corresponding interval intersects the recomputation interval. Rounded predicted death counts retain ±0.5 because the source explicitly calls them rounded. Whole-number percentages have ±0.5 percentage-point precision. A modeled contrast is not required to equal a crude difference.

- Hospital flow: 34−11=23; 11 exclusions=1+10; 23=12+11; 12−2=10; 10+11=21. The withdrawal footnote places both intervention withdrawals before implementation. Zero discharges lost in the intervention period does not imply zero pre-implementation hospital withdrawals.
- Population sums: 26,664+46,718=73,382 baseline discharges; 129,700+162,497=292,197 baseline days. 50,173+94,366=144,539 intervention discharges; 251,859+307,584=559,443 intervention days. 937+1,148=2,085 ward beds. Every eTable 2 row B+P equals its total and every hospital column sums to its arm aggregate; all eTable 3 day and event columns also sum exactly.
- eTable 2 intervention aggregates B/P: discharges26,664/50,173; deaths52/97; no-DNR26/42. Control aggregates:46,718/94,366; deaths61/147; no-DNR16/47. Every hospital-level mortality and no-DNR printed rate passes count/discharge×1000 with its own displayed precision.
- eTable 3 intervention B/P totals: days129,700/251,859; SCDE80/127; arrests15/27; preventable11/21. Control:days162,497/307,584; SCDE144/259; arrests18/32; preventable12/29. Every hospital-level displayed rate passes event/day×1000.
- Mortality:97+147=244; 244/144,539×1000=1.688126→1.69; 97/50,173×1000=1.933311→1.93; 147/94,366×1000=1.557764→1.56. 42+47=89 without DNR and244−89=155 with DNR;155/244×100=63.52459→63.5%.
- Main secondary:127+259=386;127/251,859×1000=0.50425→0.50;259/307,584×1000=0.842046→0.84;127/828×100=15.3382→15.3%;259/1178×100=21.9864→22.0%. Arrests27+32=59, and8/59×100=13.5593→14%. Preventable21/27=77.7778% and29/32=90.625% match77.8%/90.6% and narrative78%/91%.
- Process totals:126+179=305 resuscitation calls;1727+1157=2884 physician calls;1015+1694=2709 urgent consultations. 828+1178=2006 urgent admission events is distinct from686+967=1653 individuals in the per-patient analysis.
- Documentation:1270+2588+1419+2832=8109;21×5×(26+52)=8190;8109/8190=99.011%. Completeness960/1270=75.5906%;2563/2588=99.0340%;883/1419=62.2269%;1725/2832=60.9110%, all matching printed one-decimal percentages.
- ICU observed deaths42+67=109. All technology-use percentages reproduce from their period-specific patient counts. For predicted baseline control mortality, printed25 implies underlying[24.5,25.5), giving[4.61394%,4.80226%) at n531, intersecting printed4.8% interval[4.75%,4.85%). This is not an observed25-death numerator.
- Resource totals:686×4.1+967×3.7=6390.5 ventilation days; with half-unit one-decimal means, interval[6307.85,6473.15) includes6400. The total ICU-days check likewise includes15,212; printed usual-care9 has whole-unit precision and must not be silently assigned a tenth-unit interval.
- Hospital distribution: eTable 2 has four zero-death baseline hospitals (A,B,L,M), one post hospital (A), and13 post hospitals with fewer than10 deaths. Largest post mortality is hospitalH21/4034×1000=5.20575→5.21.
- eTable 5:99,389×5.1/1000=506.8839→507 deaths;397,556×2/1000=795.112→795 SCDE; actual386/559,443×1000=.689973→.69. Mortality.00076/.0051=.1490 coheres with anticipated k.15; actual rounded sigma/rate permit k.43. Rounded mean beds119.85×20=2397 matches anticipated table beds. Historical hospital bed totals are not established to be the identical planned population.

## Findings

No F-NUM finding meets all four inclusion criteria. This is a numeric-lane conclusion only; it does not preempt independent statistical/design findings.

## Excluded observations

Each row has exactly one scope reason code. Patterns are consolidated without finding IDs.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main pp.1,3,5–6 | 21 completing/analyzed hospitals versus23 initially randomized is reconciled by12 intervention assignments minus2 pre-implementation withdrawals and11 controls; abstract counts refer to completed trial population. | CONTEXT_RESOLVES |
| REPORT main p.1 abstract and p.3 Figure 1 | 144,539 patients wording versus144,539 discharges is immediately resolved by the stated hospital-discharge denominator and period-end discharge convention; no supplied individual deduplication numerator can establish a different primary extraction. | TERMINOLOGY_OR_WORDING |
| REPORT main p.3 Figure 1 and REPORT supplement p.9 eTable 2 | Usual-care post-discharge maximum29,956 in both Figure 1 boxes versus26,956 maximum hospitalT in eTable 2. All11 rows sum exactly to94,366, the primary denominator repeated throughout. A hospital range endpoint does not change primary/key-secondary result or total analysis population. | PERIPHERAL_COMPARISON |
| REPORT main p.3 Figure 1 and REPORT supplement p.11 eTable 3 | Control baseline-day minimum6,665 versus6,655 hospitalL. All11 day rows sum to162,497; primary and key-secondary denominators and results remain reconciled. | PERIPHERAL_COMPARISON |
| REPORT main p.5 Table 1 ICU staffing | Intervention categories2+5+1=8 rather than10; all displayed count-percent tuples use10, and no statement establishes exhaustive ICU-only overnight categories. Inferring missing category data or an analysis-population change is conditional. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.3,5–7; REPORT supplement pp.9,11–12,14 | Rounded means, rates, percentages, whole-percent category sums, resource totals, predicted counts and eTable 5 quantities reconcile when each input retains its displayed half-unit interval. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp.6–7 Table 2/Table 3; REPORT supplement pp.12–13 eTable 4 | Adjusted mean/risk/rate differences and ratios differ from crude post-period arithmetic. Sources explicitly specify baseline-adjusted cluster models and selected identity-link baseline omissions; no crude identity is claimed. | MODEL_VERSUS_CRUDE |
| REPORT main p.7 Table 3 and p.5 methods | SCDE ratio/CI/P and absolute difference/CI have different apparent significance because ratio adjusts baseline while that identity-link difference omits baseline, as explicitly disclosed. They are distinct estimators. | CONTEXT_RESOLVES |
| REPORT main pp.6–7; REPORT supplement pp.12–13 | 2006 admission events versus1653 patient records, all ICU death totals versus urgent-ICU deaths, and readmission/mortality denominators denote distinct supplied populations. | CONTEXT_RESOLVES |
| REPORT supplement pp.12–13 eTable 4 | Recomputing predicted death percentages from integer rounded predictions alone discards fractional probabilities;25/531 need not be4.8% but the explicit rounding interval permits it. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.12 eTable 4 |55 exclusions(3.2%) lack an explicitly named all-period denominator.55/(1653+55)=3.220% is compatible with the post population, but selecting an alternative denominator is unsupported. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol pp.1,14,29 | Power appendix prints absolute mortality reduction0.9% versus0.09% in main power text and0.9/1000 summary. Immediate18% reduction of5.1/1000 implies.918/1000; unit/decimal reading is identifiable at once. | NOTATION_OR_TYPOGRAPHY |
| PLAN protocol pp.29–30 | Historical event-rate/baseline data, including150 events/.75 per1000days, do not establish an identical trial or exposure population. Historical comparisons and retrospective administrative populations are peripheral. | PERIPHERAL_COMPARISON |
| PLAN protocol pp.14–15,29–30; REPORT main p.4; PLAN SAP pp.1–5 | Exact sample-power variance/cluster formula, implemented code output, post ICU discharge denominators and raw covariance are not supplied. A unique incompatible result cannot be demonstrated by assuming their values or equating illustrative scaling to executed analysis. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.8 Figure 2; REPORT supplement pp.2–5 figures | Plot styles/axis wording are resolved by captions, hospital letters and source table; histogram bar heights are visual approximations without exact printed cell counts. No primary/key-secondary numerical extraction changes. | CONTEXT_RESOLVES |

## Limitations

Every assigned relationship and component group reviewed; no scientific coverage gap. Exact ICU post-discharge denominators, raw GEE covariance, individual predicted probabilities, numerical power formula and precise histogram percentages are absent from supplied materials. These limit particular mechanical reconstructions and are not independently qualifying numeric observations. Continuous distribution checks use printed summaries and known scale bounds; individual-level raw-data arithmetic is outside this review. Other specialist lanes independently assess planned-versus-reported design and statistical method logic.
