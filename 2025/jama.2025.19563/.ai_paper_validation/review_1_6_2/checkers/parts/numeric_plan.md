# Numeric consistency review — DOC-002 PLAN, PDF pp.1–90

Fresh reviewer `/root/numeric_plan`; complete assigned scope: all 44 numeric mapper blocks in plan_001, plan_002 and plan_003, plus eight related allocation, engagement, recruitment and administrative arithmetic relationships. Stable inventory N101–N152 is in `relationships/parts/numeric_plan.md`. 52 relationships checked; two findings emitted; five excluded observations. Sample-size power/test logic and report counterparts are assigned to distinct specialists and are not inferred here. All locations below are PLAN by content, within the same supplied protocol/SAP bundle.

## Findings

### F-NUM-101

**Title:** Recruitment-pool portal-access percentages do not reconcile with the displayed counts.

**Relationships:** N148. **Focus area:** A. **Proposed review domain:** `plan_material`. **Proposed relationship type:** `P_P`; **All relationships:** `P_P`.

**Source locations and roles:** PLAN [DOC-002 PDF p18, Table1, eligible-patient and patient-portal-access rows](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=18), Johns Hopkins Medicine and Reading Health System columns; PLAN same PDF p18 §5.5.1, first paragraph, sentences stating the eligible and portal counts (the page-image margin shows line-label trailing digits40–42; no uncropped full line number is asserted). Authoritative confirmation: fresh source render `preprocessing/numeric-plan-page018.png`, bundled pdf_tools.py, PyMuPDF1.28.0,200dpi,CPU. Current GPU OCR agrees but is only a locator.

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

**Source locations and roles:** PLAN [DOC-002 PDF p18, Table1, Reading Health System column, Race% rows](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=18). Same table's Johns Hopkins race rows and both ethnicity partitions establish the display structure. Exact direct-source confirmation is the same fresh source render described in F-NUM-101.

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
