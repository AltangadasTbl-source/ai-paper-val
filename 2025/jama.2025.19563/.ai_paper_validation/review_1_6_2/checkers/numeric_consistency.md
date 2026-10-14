# Complete numeric consistency review — Workflow 1.6.2

Mechanical union of three disjoint fresh-agent reviews: DOC-001 main, DOC-002 plan, and DOC-003 support report. All 188 canonical numeric relationships are checked; each constituent cell retains its source population. Three threshold-qualified checker findings await independent inclusion screening. Each part retains its own Excluded observations table, all of which are covered by screening, statistical pass 2, and audit.

# Main-report numeric consistency review

Assigned scope: DOC-001 main REPORT, all PDF pp.1–11, printed pp.2079–2089, and all 80 main numeric relationship groups N001–N080. All constituent participant-flow branches, baseline count/percentage cells, forest count/denominator cells, matrix cells/margins and conditional percentages were checked. Numeric relationships and complete audit arithmetic are in [numeric relationship inventory](../relationships/numeric_relationship_inventory.md). Support-report and plan numeric relationships are separate assigned shards. Cross-document and inferential-statistical decisions are not duplicated here.

Evidence inspected: the supplied source identity jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf; source-matched reusable rendered PDF pages5–9 visually in full, reusable native text pages1–4 and10–11, and the fresh main evidence map. All quantitative printed values used in calculations retain their source populations and units. Derived text/images are transcription aids; no old candidate/report/checker conclusions were read. The supplied PDF locations remain the authority. No new OCR or rendering was required in this shard.

## Findings

No qualifying main-report numeric finding. All applicable count/denominator relationships reconcile under the stated display-precision rule. This result follows complete assigned coverage and does not imply a disposition on statistical or cross-source findings from other agents.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [p.1 abstract](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=1), [p.4 baseline narrative](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4), [p.6 Table](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=6), N010–N011/N038 | Abstract Hispanic6% differs from narrative5.4%; 20/368=5.435%. Printed-copy intervals[5.5,6.5] and[5.35,5.45] have gap0.05pp, relative discrepancy0.05/5.4=0.00926, below0.05. The abstract/body comparison therefore meets the display-precision exclusion despite differing integer rounding. Narrative White61.0% versus225/368=61.141% has interval overlap after half-unit count/denominator allowance, as documented in the inventory. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [p.6 Table](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=6), N026–N066 | Independently rounded categorical percentages may sum99.9% or100.1%, while every count partition totals183/185 and every individual percentage passes the half-unit overlap check. Examples: AI BMI30.1+38.3+18.0+13.7=100.1%;human race0.5+8.6+26.5+60.0+2.7+1.1+0.5=99.9%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [p.8 Figure3 footnote a](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=8), [p.6 BMI row](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=6), N050/N080 | Figure footnote labels baseline32.2(28.2–35.9)/32.5(29.3–37.7)kg/m² as weight; explicit kg/m² and the identical Table BMI values make the quantity immediately identifiable. No printed number changes, and this is not a substituted numeric value or a changed event-result assignment. | TERMINOLOGY_OR_WORDING |

## Coverage and precision record

N001–N080 each has NUMERIC_CHECK_COMPLETE status by the inventory's scope-wide convention and an individual source/inputs/check record. Eleven of eleven pages inspected; pages10–11 contain no new applicable trial count/result. All nine prescreening components, four exclusion reasons, nested withdrawals, medication-exclusion categories, every baseline cell, all four binary outcome rows, every engagement matrix cell/margin, and all twelve conditional percentages are covered. Overall baseline copy differences were checked under the stipulated display rule. No observation in an always-register category was screened out by a general context reason. The terminology observation changes no printed number and cannot meet route A category2.

Risk-difference labels in Figure2 are compatible with percentages expressed as AI minus human percentage-point differences; no OR,RR,HR,rate or person-time label is printed. The binomial-regression model is stated, so crude computations are scale checks rather than imposed inferential reproductions. Composite component counts are explicitly overlapping; the HbA1c component denominator130/130 is explained by baseline eligibility. Primary ITT183/185, complete follow-up313 and restricted151/149 are not conflated. Exact source inputs do not establish a numeric contradiction in this shard.

Scientific coverage gaps:None. Derivative limitation: historical extraction/rendering versions are incompletely recorded by reused assets; complete visual source-matched table/figure inspection and existing native pages cover the assigned units. Figure3 does not print participant-level exact heights; axes, goals, directions and population labels were inspected without inventing unprinted numbers. No source, reused asset or other agent artifact was modified.

Scope counts:80 numeric relationship groups;0 findings;3 excluded-observation rows;11/11 source pages inspected. Stable C IDs and adjudications are not assigned by this checker.
# Numeric consistency review — DOC-002 PLAN, PDF pp.1–90

Fresh reviewer `/root/numeric_plan`; complete assigned scope: all 44 numeric mapper blocks in plan_001, plan_002 and plan_003, plus eight related allocation, engagement, recruitment and administrative arithmetic relationships. Stable inventory N101–N152 is in `relationships/parts/numeric_plan.md`. 52 relationships checked; two findings emitted; five excluded observations. Sample-size power/test logic and report counterparts are assigned to distinct specialists and are not inferred here. All locations below are PLAN by content, within the same supplied protocol/SAP bundle.

## Findings

### F-NUM-101

**Title:** Recruitment-pool portal-access percentages do not reconcile with the displayed counts.

**Relationships:** N148. **Focus area:** A. **Proposed review domain:** `plan_material`. **Proposed relationship type:** `P_P`; **All relationships:** `P_P`.

**Source locations and roles:** PLAN [DOC-002 PDF p18, Table1, eligible-patient and patient-portal-access rows](../../../joi250084supp1_prod_1765403089.61351.pdf#page=18), Johns Hopkins Medicine and Reading Health System columns; PLAN same PDF p18 §5.5.1, first paragraph, sentences stating the eligible and portal counts (the page-image margin shows line-label trailing digits40–42; no uncropped full line number is asserted). Authoritative confirmation: fresh source render `preprocessing/numeric-plan-page018.png`, bundled pdf_tools.py, PyMuPDF1.28.0,200dpi,CPU. Current GPU OCR agrees but is only a locator.

**Printed inputs:** Table1 gives Johns Hopkins eligible21,346, portal13,910(56%); Reading eligible8,751, portal4,892(60%). Paragraph gives21,410eligible Johns Hopkins patients and13,910(56%) signed up for portal messages.

**Rule and calculation:** For each location, displayed portal percentage should equal100×portal count/eligible count if the two rows/paragraph use the printed eligible pool as denominator. Allow each integer count±0.5 and each whole-number percentage±0.5 percentage points.

| Location | Recomputed central percentage | Recomputed half-unit interval | Printed percentage interval | Gap, percentage points | Relative discrepancy |
|---|---:|---|---|---:|---:|
| Johns Hopkins table |65.164434|[65.160565,65.168302]|[55.5,56.5]|8.660565|0.154653|
| Reading table |55.902182|[55.893275,55.911091]|[59.5,60.5]|3.588909|0.059815|
| Johns Hopkins paragraph |64.969640|[64.965788,64.973493]|[55.5,56.5]|8.465788|0.151175|

All relative discrepancies exceed0.05. The Johns Hopkins table-versus-paragraph eligible count difference alone is separately screened out; either printed pool denominator leaves the56% portal percentage unreconciled. These three occurrences are consolidated as one portal-denominator/percentage pattern; no unsupported production mechanism is asserted.

**Qualifying route:** Route A, category 3 (counts within one display).

**Affected result or extracted value:** Portal access of the eligible recruitment pool:56% in Johns Hopkins and60% in Reading, or the corresponding eligible/portal counts. These are prospective recruitment-pool values, not the randomized-trial analysis denominators or primary endpoint results.

**Why context does not resolve it:** The cited count/denominator/percentage combinations reproduce category3. The table names the eligible population and the paragraph explicitly says “Of these participants”; no different denominator for the displayed percentages is supplied. The immediately intended percentage or denominator cannot be established from those statements.

**Alternatives and missing definition:** The portal percentages could use a different, unprinted EMR-query population, or counts and percentages could come from different query snapshots. The supplied page does not state either. The prospective-pool context limits the relevance to efficacy interpretation but does not itself reconcile within-display arithmetic. A human may need to decide the scope/classification of this plan-only recruitment display independently.

**Classification ambiguity:** All compared passages are PLAN, hence P_P/plan_material is the best-supported available classification. The quantities concern prospective recruitment context rather than a statistical-design element relied on by the reported primary analysis. The independent inclusion screener must assess this boundary alongside the normative always-register category3 rule, which prohibits peripheral/out-of-focus exclusion of a reproduced category3 observation.

**Exact human question:** Which eligible-patient denominators, portal-access counts and percentages belong together in Table1 and its paragraph, and are the displayed56%/60% based on an unprinted population?

### F-NUM-102

**Title:** The listed Reading recruitment-pool race percentages do not form a complete partition.

**Relationships:** N149. **Focus area:** A. **Proposed review domain:** `plan_material`. **Proposed relationship type:** `P_P`; **All relationships:** `P_P`.

**Source locations and roles:** PLAN [DOC-002 PDF p18, Table1, Reading Health System column, Race% rows](../../../joi250084supp1_prod_1765403089.61351.pdf#page=18). Same table's Johns Hopkins race rows and both ethnicity partitions establish the display structure. Exact direct-source confirmation is the same fresh source render described in F-NUM-101.

**Printed inputs:** Reading race White83%, Black/African American3%, Unknown Race4%, Asian1%, American Indian0%, Native Hawaiian/Pacific Islander0%. Sum91%. Johns Hopkins corresponding categories52+33+9+6+0+0=100%; ethnicity in both columns totals100%.

**Rule and calculation:** The listed mutually exclusive race categories, including unknown, should partition the eligible population if the display is exhaustive. Reading sum=83+3+4+1+0+0=91%. Allow half-unit intervals for whole-number percentages, constrain0% rows to[0,0.5] because percentages cannot be negative: the sum interval is[89,94]%. Even allowing a whole-number100% total its interval[99.5,100.5], the minimum gap is5.5percentage points; relative discrepancy=5.5/100=0.055>0.05. With the exact partition target100%, gap6points andrelative0.06. No printed total100% row exists:100% is the exhaustive-partition target, supported by the table's category structure and complete comparator partitions, not quoted as a printed Reading total.

**Qualifying route:** Route A, category 3 (counts/subgroup totals within one display), under the explicitly stated exhaustive-partition rule.

**Affected result or extracted value:** Reading eligible-pool race distribution; nine percentage points of the printed population are unaccounted for by the displayed race rows. This is recruitment-pool description, not randomized baseline demographics or a primary analysis-population count.

**Why context does not resolve it:** Under an exhaustive partition, this is a reproduced category3 discrepancy beyond display precision. The table already includes unknown race and shows no additional category or missing-percentage footnote. It does not identify the unrepresented group or a different denominator.

**Alternatives and missing definition:** An unlisted race category, different denominators for rows, or a nonexhaustive display could account for the residual. The supplied page does not state these possibilities; the source contains no printed counts to distinguish them. This finding is distinct from the portal fractions because its rule is completeness of a categorical partition rather than recomputation of a printed numerator/denominator percentage.

**Classification ambiguity:** PLAN/P_P/plan_material is the available document-grounded assignment. As in F-NUM-101, the display concerns prospective recruitment context; the scope boundary and the applicability of category3 to an implied exhaustive percentage total require independent screening. If the display is established as intentionally nonexhaustive, the missing-total rule would not be reproduced.

**Exact human question:** Are the Reading race rows intended as a complete distribution of eligible patients, and which category, denominator or value accounts for the percentage not represented in the listed rows?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-002 p18 §5.5.1 vs Table1; N150 | Eligible Johns Hopkins pool21,410 versus21,346. Half-unit gap63/21,346=0.00295, below0.05. This does not eliminate the independent portal fraction discrepancy. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p20 Figure1; N151 |13participants/month for9months then14for18months implies369 versus final368, with final figure increment13. Half-unit intervals overlap and one-person relative gap is below0.05; an administrative accrual projection. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p9 schedule vs p22 kit mailing; N102/N106 | Original mailing day7+2 versus narrative8–12days differ in an operational dispatch window; amendments pp76/77 disclose further windows. No printed primary or key secondary result, analysis-population size or statistical decision rule changes here. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp56–58 NPART; N130 | Heading28items equals footnote36−8, while form contains multiple subquestions and31closed response prompts if every employment/social/technology row is counted separately. No aggregate score denominator or reported quantitative result depends on that item-count convention; predictor analysis contains no scored total. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 p26 hDPP; N107 |“Bi-monthly”maintenance wording versus3sessions each in months7–9and10–12. The explicit six-session schedule determines the intended offered dose immediately; no number conflicts. | TERMINOLOGY_OR_WORDING |

## Coverage, provenance and limitations

All52 assigned relationships complete. Every44 local numeric mapper block is represented inN101–N144; design, engagement and recruitment arithmetic isN145–N152. Reconciled calculations and distinct clocks, units, denominators and modified plan versions remain in the relationship inventory rather than in excluded observations. No preferred clinical/statistical analysis proposed. No C IDs, adjudications or dispositions assigned.

Sources and reusable assets preserved. Supplied maps were read in full, relevant current GPU OCR used only as a locator, and exact source p18 freshly rendered and visually inspected for both findings. Source p61 also freshly rendered to confirm scored-item denominator155; fresh p54 mapper replacement visually inspected. Rendering usedCPU under the tooling record; GPU RapidOCR remains the user-approved coordinator engine. No fresh OCR, external sources, old candidates/reports, unapproved Python, or package installation used by this reviewer.

Limitations: no row counts or explicit Reading race-total row are printed; F-NUM-102 therefore states the exact exhaustive-partition assumption and alternatives. Recruitment-pool relevance/classification is explicitly bounded. Historical reusable image renderer provenance is unavailable. No scientific unit omitted from the assigned numeric scope.
# Numeric consistency review: DOC-003 REPORT results supplement

Scope: every assigned quantitative relationship on all PDF pages 1–69 of `joi250084supp2_prod_1765403089.61751.pdf`. Read `QUALITY_CONTROL_SCOPE.md`, the complete 1.6.2 contract, tooling record, and both complete fresh results mapping parts. Numeric inventory N201–N256 covers all 56 numeric blocks and every constituent count, percentage, total and figure row. The inventory also records coherent checks, distinguishing participants from events and mutually exclusive categories from overlaps. Model, interval and test logic remains assigned to the statistical reviewer; no alternative analysis is proposed.

Direct source confirmation: newly rendered PDF p37, bundled `pdf_tools.py render`, user-authorized `/home/juliz/venvs/stt/bin/python`, PyMuPDF 1.28.0, 200 dpi, CPU. Derivative: `preprocessing/numeric-support-p037.png`. No fresh OCR or new package installation was needed. The direct PDF remains final authority.

## Findings

### F-NUM-201

**Title:** Two version-exposure percentages do not reconcile with the stated AI primary-analysis denominator.

**Source locations and document roles:** REPORT [DOC-003 PDF p37, eTable1b](../../../joi250084supp2_prod_1765403089.61751.pdf#page=37), rows `11.100.131 (September 2023)` and `122.100.407 (December 2024)`, each printed `5 (5)`, column headed `Number of Participants Exposed (% of Primary Analysis population assigned to AI-DPP)`. REPORT [DOC-003 PDF p27, cohort definition](../../../joi250084supp2_prod_1765403089.61751.pdf#page=27) defines primary analysis as all randomized participants; REPORT [DOC-003 PDF p41, eTable4](../../../joi250084supp2_prod_1765403089.61751.pdf#page=41) prints AI randomized N=183. REPORT [DOC-003 PDF p34, eFigure3](../../../joi250084supp2_prod_1765403089.61751.pdf#page=34) also prints 183 as AI primary-outcome denominator. These latter locations establish the named denominator; both affected percentage cells lie in the same display.

**Relationship:** N227; proposed relationship type S_W; all relationships S_W.

**Printed inputs:** Each affected row n=5, displayed percentage 5%; AI randomized/primary-analysis denominator 183. The preceding seven exposure rows use percentages consistent with183: 58(32),102(56),109(60),103(56),99(54),105(57),104(57).

**Rule and reproduced calculation:** Percent of the named arm population is 100n/N. Central calculation100×5/183=2.73224%. For the required conservative display-precision rule, n∈[4.5,5.5],N∈[182.5,183.5], giving recomputed percentage [2.45232%,3.01370%]. Printed5% has interval[4.5%,5.5%]. Their gap is4.5−3.01370=1.48630 percentage points; relative discrepancy1.48630/5=.297260, above.05. Both rows independently reproduce the same pattern and are consolidated here. Even allowing half-unit input intervals, they do not reconcile.

**Focus area:** A (counts and denominators).

**Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** The percentages of AI primary-analysis participants exposed to the September2023 and December2024 application versions; an extractor could take either printed5% or the percentage represented by5of183.

**Why context does not resolve it:** Route A category3 applies to the count/denominator/percentage relationship in a display. The column explicitly names the full AI primary-analysis population. Its seven preceding rows reproduce that denominator, and neither affected row supplies a smaller denominator or a revised meaning for its percentage.

**Alternatives:** A later-version subgroup denominator near100 might explain5%, or one of the printed counts or percentages might represent a different quantity. The supplied display does not identify any such change. Version exposures overlap and need not sum to183; this overlap does not alter the percentage denominator named in the column.

**Exact human question:** What denominator and exposure counts apply to the September2023 and December2024 version rows, and which percentages should be extracted for those two versions?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-003 p55 eTable12, Human A+B combination | Printed10(19%) among59 composite achievers versus central16.949%. Conservative half-unit count/denominator inputs produce[15.9664%,17.9487%]; printed19 has[18.5%,19.5%], gap.55128pp/19=.02901≤.05. Other combinations, totals and component marginals reconcile. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p39 eTable3, Not Hispanic or Latino | Printed343(93.5%) among368 versus central93.2065%; half-unit recomputed[92.9444%,93.4694%] overlaps printed[93.45%,93.55%]. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p36 eTable1a, August2022 starting version | Printed60(32.76%) among183 versus central32.7869%; half-unit input interval includes32.76 and no reproduced discrepancy remains. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p8 device table versus p46/p51 completion totals | Follow-up device entries282+30+0=312 versus313 completers; sum-input interval[310.5,313.5] overlaps313 half-unit interval[312.5,313.5], relative gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 baseline actigraphy footnotes pp40,43,45,47,54 versus p49 eTable8b | Repeated baseline footnotes say n=3 without valid data; missingness table gives8+5=13. This comparison concerns baseline observation counts across locations; total randomized and endpoint-eligible analysis sizes remain explicitly368 and260. No source establishes that the same missingness category is meant or that a primary/key secondary result changes. | PERIPHERAL_COMPARISON |
| REPORT DOC-003 p34 eFigure3, all four adjusted rows | Adjusted RD−2.0,−3.4,.3,−1.6 differ from crude count differences, including equal A1C counts35/130 in both arms; the figure explicitly specifies age adjustment. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 p59 eTable16 MI sensitivity | MI-pooled percentages32.2/31.9 differ by.3pp while displayedRD is−1.1pp; a crude difference of pooled arm percentages need not reproduce a separately modeled/pool-combined estimate. Numeric comparison alone does not establish method identity; statistical reviewer owns the supplied-method check. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 p61 eTables18a–b | Two distinct activity-imputation scenarios produce identical58/183 and60/185 primary counts. They can coincide when their additionally affected participants do not change the composite; individual participant outcomes are not supplied to contradict that possibility. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 pp39–54 baseline BMI displays | Median BMI appears under a count/percentage-style heading in one baseline display; units and the fractional median/IQR pattern identify a continuous BMI summary immediately, without changing printed values. | NOTATION_OR_TYPOGRAPHY |

## Completion and limitations

Completed all56 numeric blocks,N201–N256,with one finding containing both affected rows and9excluded observations. Every categorical total, numerator/denominator/percentage pair, subgroup partition, composite marginal, missing-outcome total and adverse-event condition/grade total was checked in the complete inventory. Neither outcome overlap nor multiple events per participant was treated as mutually exclusive.

No numeric scientific coverage gaps. Model reconstruction is limited by unavailable raw participant data and the unsupplied R helper function; those do not restrict printed arithmetic checks. The native figure extractions omit plotted numbers, but complete fresh visual mappings cover every plotted row. No C IDs, severity, adjudication, or correction was assigned.
