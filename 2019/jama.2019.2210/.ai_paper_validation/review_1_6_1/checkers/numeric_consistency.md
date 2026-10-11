# Numeric consistency review

- Stage: numeric_consistency_reviewer, mandatory fresh specialist.
- Runtime ID: 01a128df-e823-7a12-8733-878a92b6489c.
- Exact disjoint scope: M-N001–M-N086 main REPORT numeric units and P-N101–P-N130 support-core numeric units. Complete116-unit stable inventory: relationships/numeric_relationship_inventory.md, N001–N116. DOC-003 pp.22–41 risk-table numeric checking belongs to the separately assigned shard and is not counted here.
- Source roles: DOC-001 REPORT; DOC-002 PLAN including all versions and amendment p.45; DOC-003 REPORT; DOC-004 REPORT sharing statement with no applicable numeric result.
- Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely. Read both canonical fresh mapper artifacts; independently applied the inclusion threshold to all assigned units. No old findings, screening decisions, candidate lists, or reports were used. No web, external literature, Python scientific review or raw-data inference was used.
- Evidence method: complete source-linked mapper inputs and usable reusable text as locators; direct Poppler pdftotext26.01.0 layout reads from exact main PDF pp.4,5,6,7,8 and results PDF p.4 for potential observations; source-linked fresh PLAN layouts pp.9,12,45 reconfirmed dose/amendment context. Those direct source values supersede any derivative ambiguity. No new derivative or OCR was needed; no supplied source or reused artifact was changed.

## Checks and results

All116 assigned relationships have explicit inputs, compared roles, arithmetic or matching rule and completed result in the inventory. Participant flow439−22=417, allocation251+166=417, all randomized/treated/analyzed counts, nonadherence24+19=43, follow-up416/417, baseline-serum410+7=417, genotype available-category totals, efficacy counts, safety numerators and all24 safety percentages, subgroup risk vectors, mean-serum413-person partition and initial risk-table sums were checked. Count inputs are exact; displayed continuous inputs keep half-unit intervals. Categorical sums and variable-specific available counts were not silently treated as randomized allocation totals.

Primary/key-secondary repeated numeric outcomes reconcile: relapse/death50/251 and43/166;death37/251 and25/166;baseline middle142+90=232;five-year relapse-free77%/69%,overall82%/81%,middle85%/71%. Cancer/noncancer death partitions27+10=37 and16+9=25. Survival estimates and HRs retain source-established censoring/model definitions. No OR/RR/RD substitution, person-time denominator or source-established crude-hazard identity is printed. Complete support eTable1 allocation rows sum248/165 and combined413; all corresponding eFigure1 initial counts match. Risk vectors are nonnegative, nonincreasing and begin with the printed subgroup/allocation counts.

Safety denominator reconstruction uses first-year discontinuation timing:251−(3nonmedical+4medical+1lost)=243 and166−(2nonmedical+4medical)=160;full-study251−24=227 and166−19=147. Each of the24 Table3 count/percentage cells agrees at0.1percentage-point display precision with its explicitly labeled denominator. Abstract/narrative safety numbers match the until-censoring set, not the first-year or randomized set.

## Findings

No observation in this assigned numeric scope met all four inclusion criteria. Finding count:0. This is a completed numeric-stage result, not human adjudication or a finding-count target. Statistical-method and estimate/test compatibility are covered independently by the mandatory statistical agents; this review did not replace those checks with approximations.

## Excluded observations

Each row records one distinct apparent discrepancy or tightly related pattern, with exactly one scope reason code. Ordinary successful checks remain in the116-unit inventory and are not repeated as excluded observations.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp.1,4,Figure1;N001 | Abstract7 excluded after operation versus flow5 not meeting inclusion+2 other reasons:7=5+2;with15 declined total22. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.4 Figure1/narrative;N003–N005 | Figure says23 stopped D medication plus separate1lost; narrative includes lost patient among15 nonmedical stops.14+1=15 and23+1=24;43/417=10.3118% explains10.3%. | CONTEXT_RESOLVES |
| REPORT DOC-001 pp.1,4,Table1 p.5;N008 | Mean age66 in abstract versus median66 in text are distinct quantities;site fractions10%,42%,48% are descriptive abbreviated categories, with small bowel2/417=.480% separately explicit. Intended population417 is clear. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.4 narrative andp.5 Table1;N008,N039 | StageII stated26% versus111/417=26.619% (display26 interval25.5–26.5 excludes recomputation). Exact stage counts63+48=111 are explicit and total417 unchanged;descriptive percentage does not alter primary or key-secondary extracted outcome or its analysis population. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.5 Table1 header/categories;N022–N025,N044–N068,N069 | BMI/serum/genotype category totals below251/166;variable-specific missingness explains available categories, with serum248/162 plus3/4 missing matching417. No requirement that all characteristics have identical available-case denominators. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.5 Table1;N045,N058 | MiddleD142(58) gives57.258% using derived248;ApaIP61(40) gives40.667% using derived150. These exceed respective half-unit percentage intervals. Table does not print variable-specific denominators, but affected counts142 and61 are explicit and corroborated in outcome/subgroup displays; no ambiguity about extracted primary/key-secondary count or outcome is left. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.5 Table1;N048–N068 | Genotype column percentages can sum99% or101%;this is allowed when each cell is rounded independently. All count partitions were preserved without replacing by rounded percentages. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp.1,4,6,7;N010–N014 | Five-year survival77/69,82/81 and85/71 does not equal1minus crude full-follow-up event proportion;time horizon and censoring differ. CoxHR0.76 and0.95 are not crude event ratios. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p.4 efficacy paragraph;N010,N011 | Relapse41/36 plusdeath37/25 exceeds composite50/43;events overlap and composite is first relapse or death, not disjoint event sum. Cancer/noncancer death partitions reconcile. | CONTEXT_RESOLVES |
| REPORT DOC-001 pp.4,6,7 observation times;N006,N076,N077 | Follow-up medians3.5y differ from relapse/death observation times3.3/3.0y and subgroup-specific periods;event endpoints and subgroup samples differ, and medians all lie within their IQRs. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.7 Figure3C caption/risk row;N074,N077 | Caption says panelC risk numbers not given because of weighting,while full seven-entry risk rows are visible. Immediate figure shows the actual counts90/142 at0 and later rows;this caption pointer does not change primary/key-secondary result or analysis size. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p.6 biomarkers;N078,N079 | Patient25(OH)D change87% is not required to equal(41−21)/21=95.238%;ratio from marginal medians is not median paired change. Calcium medians9.3→9.3 androunded0% changes do not imply identical paired observations. Source does not establish those assumptions. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 pp.1,6,8 Table3;N080–N084 | Different fracture/stone counts across until-censoring,first-year,andrandomized columns have different explicitly labeled adherence populations;all percentages and matched narrative columns reconcile. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp.9,12,25,28,45 versusREPORT DOC-001 pp.1,2;N088 | Initial two600-IU daily capsules/1200IU versus initial bottle1000IU andfinal two1000IU/2000IU;amendment explicitly discloses increase before trial2009.10.8. Actual reported dose2000IU matches final plan;historical inconsistency does not leave intervention extraction unclear. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp.19,25,45 versusREPORT DOC-001 p.8;N090 | De-novo cancer separately tertiary after2012.12.8 disclosed amendment,while synopsis retains safety wording;counts remain distinctly labeled andno mutually exclusive safety sum is stated. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp.9,24,38;N091 | Age30–90 versus registration age<90:source does not establish any participant exactly90 or resulting altered efficacy-population size. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp.12,27,36 andREPORT DOC-001 p.3,Table1 andDOC-003 genotype panels;N093,N108–N110 | FokI identifier strings differ andCDK2/Cdx2 spelling varies;same named subgroup andprinted allele counts make matched numerical populations identifiable. No external identifier-equivalence claim or changed reported numeric result is inferred. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-003 pp.2–4;N096–N099 | Mean-exposure available413 differs from baseline-serum available410;definitions use average levels overtrial versusbaseline measurements. Source does not assert identical missing-data membership. Everymean-group table/figurecount matches. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 pp.2–4;N096,N097 | “~20 vs40~50”/.29 and“~20 vs30~40”/.39 comparison annotations aregroup naming,with<20 explicit reference in eTable1;table andfigure HR/CI/P match. No reverse ratio is required by informalvs phrase. | CONTEXT_RESOLVES |
| REPORT DOC-003 p.5 versusDOC-001 p.6;N100 | Exact boxplot quartiles/whiskers/contributor counts are unprinted;approximate graphic mediansdo not supply exact extra arithmetic inputs or patient-level ratios. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 p.6 versusDOC-001 p.7;N101 | Imputed andcomplete-case baseline subgroupHR/CI/P printed identically;source doesnot require that estimates afterimputation differ at display precision.3+4 missingcounts match7. | NOT_REPRODUCED |
| REPORT DOC-001 pp.2,3,8 andPLAN DOC-002 assay/background material;N086,N092,N093 | Prior-study participantnumbers,doses,risk summaries,labtemperature/cycles andhistorical risk estimates are retained locator inputs;they do not represent currenttrial primary/keysecondary resultcounts ordecision rules. | OUT_OF_FOCUS |

## Limitations and handoff

Assigned numerical units: 116; completed: 116; findings: 0; excluded observations: 22. The support-risk-table shard is disjoint and will be merged by the coordinator. No scientific gap exists in this assigned scope. Unprinted plot coordinates, individual participant histories, and variable-specific denominators not separately stated in Table1 limit reconstruction; source-printed counts and named models remain available for extraction. Reused rendered-image engine provenance is not recorded historically; fresh mapper visual alignment and direct-source layout reads supported the inputs used here. No inference relies on a fabricated denominator, unreported crude model or external SNP lookup.

# Coordinator merge: numeric results part 2

The following independently checked disjoint part completes N117–N136. Canonical numeric scope is N001–N136:136 relationships;0 findings;30 checker-excluded observations. Original part remains preserved at checkers/parts/numeric_results_22_41.md. The cross-source checker independently emitted F-XS-001 for the DBP1 population observation; its inclusion screen will apply the normative analysis-population exception.

# Numeric consistency review: results supplement pages 22–41

Runtime agent ID: 01a128e0-08d6-7511-a772-13eef531d888. Scope: DOC-003 physical PDF pp.22–41, R-N301–R-N320 → N117–N136; REPORT content. Complete scope/contract read. All 20 exact-page reusable images were visually inspected; fresh mapper text and canonical main/support maps provided locators and matching context. No old candidate/report conclusions or external evidence were used. All 160 risk entries, their row alignment, labels, time axes, nonnegative/nonincreasing rules, eight collection partitions, and source-grounded HR identity were checked. Full inputs and exact componentwise calculations are in [the assigned inventory](../relationships/parts/numeric_results_22_41.md).

## Findings

No observation in this complete shard meets all four inclusion criteria. Qualifying findings: 0; no F-NUM-201 ID is assigned. Collection sums reconcile exactly or describe source-defined partial subgroup coverage; no result-bearing extraction ambiguity remains under the applicable numeric rules.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [REPORT DOC-003 pp.22–24 DBP1](../../../joi190023supp2_prod.pdf#page=23) vs [REPORT DOC-001 p.5 Table1](../../../jama_urashima_2019_oi_190023.pdf#page=5) | DBP1 TG placebo baseline risk count59 versus descriptive Table1 genotype count57; collection baseline P150 versus main descriptive sum148. Exact integers differ, but this is baseline subgroup description/risk-table comparison; no named primary/key-secondary result or full analysis-population size changes. Consolidated single observation for the same difference. | PERIPHERAL_COMPARISON |
| REPORT DOC-003 pp.22–27 DBP collections; REPORT DOC-001 p.6 overall | Genetic-category risk sums P150/D231 below randomized P166/D251. Claiming every randomized person has available genotype data is not established; the category sums are not stated full-trial analysis denominators. | CONDITIONAL_OR_UNREPORTED |
| [REPORT DOC-003 pp.32–33 BMI](../../../joi190023supp2_prod.pdf#page=32), REPORT DOC-001 p.5 | BMI risk baseline totals P165/D249 agree with main available category sums. Difference from randomized P166/D251 is resolved by available BMI population; all residual time vectors remain nonnegative/nonincreasing. | CONTEXT_RESOLVES |
| [REPORT DOC-003 pp.34–36 site](../../../joi190023supp2_prod.pdf#page=34), REPORT DOC-001 p.5 | Three displayed sites total P165/D250; main Table1 additionally includes small-bowel P1/D1. This partial figure collection does not claim to contain that category, and residual risk vectors are coherent. | CONTEXT_RESOLVES |
| [REPORT DOC-003 p.30 age caption](../../../joi190023supp2_prod.pdf#page=30) | Caption says younger than median (≤65) while title says age65 and younger; explicit numeric threshold ≤65 and opposite >65 panel establish intended split. | TERMINOLOGY_OR_WORDING |
| [REPORT DOC-003 p.33 BMI title/caption](../../../joi190023supp2_prod.pdf#page=33) | ASCII >= and superscript/ordinary m2 notation describe the same ≥25 kg/m² threshold. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-003 pp.22–41, particularly [p.27](../../../joi190023supp2_prod.pdf#page=27), [p.33](../../../joi190023supp2_prod.pdf#page=33), [p.34](../../../joi190023supp2_prod.pdf#page=34), [p.38](../../../joi190023supp2_prod.pdf#page=38), [p.41](../../../joi190023supp2_prod.pdf#page=41) | Terminal cumulative-hazard ordering or ratio need not equal whole-follow-up Cox HR; HR is model-based, step heights are not exact printed event probabilities, and some curves cross. One consolidated quantity-identity observation covers all locations. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 pp.22–41 risk rows | Risk-set reductions cannot be converted into exact relapse/death counts without censoring histories; an asserted event numerator derived solely by baseline-minus-final risk counts would depend on an unsupported no-censoring assumption. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

20/20 numeric relationships complete, 20/20 pages inspected, 160 printed risk entries checked, eight collection calculations completed, 0 findings, 8 excluded observations. Source-derived count partition checks require no rounding relaxation because their inputs are exact integers. Two-decimal HR inputs retain half-unit 0.005 intervals when relevant; no crude ratio or digitized coordinate was substituted for a modeled HR. No scientific coverage gap. Exact event/censoring histories and individual model coefficients are absent and were not inferred. This shard neither duplicates core local N checks nor adjudicates inferential S relationships.
