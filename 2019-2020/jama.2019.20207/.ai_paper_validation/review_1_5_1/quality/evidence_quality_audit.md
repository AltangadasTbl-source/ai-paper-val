# Evidence-Quality Audit

## Audit status and scope

This is a neutral quantitative quality-control audit. Every stable candidate remains **Pending Human Adjudication**. The audit does not assign a scientific disposition, importance level, or prescribed change.

- **Stable candidate set audited:** C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013.
- **ID-set result:** The candidate ledger and mechanical evidence recheck each contain all 13 stable IDs exactly once as sections. This quality artifact also contains all 13 IDs exactly once as sections.
- **Direct-source coverage:** Five PDFs, 84 PDF-page units total. Reusable-backed units are 12 and fresh-required units are 72; `12 + 72 = 84`. Mapped units are 84. Every source row has reusable plus fresh-required units equal to total units, mapped units equal to total units, and status `COMPLETE`.
- **Coverage-manifest result:** Every current manifest row has exactly one plain relative artifact path. All current artifact targets resolve after creation of this audit. The coordinator must mark the `evidence_quality` row `COMPLETE` and add the required `report_generation` row, enumerating C001-C013 and naming one report artifact, when report assembly occurs.
- **Quantitative relationship coverage:** The canonical numeric inventory is continuous from N001 through N031. The numeric checker and cross-source checker each document their full assigned relationship scope. Provisional numeric units are continuous within every mapper shard and are retained as provenance.
- **Statistical relationship coverage:** The canonical statistical inventory is continuous from S001 through S017. Both passes explicitly record all 17 relationships as complete. Pass 1 and pass 2 use distinct fresh runtime IDs, `root/statistical_pass_1` and `root/statistical_pass_2`, each recorded as `gpt-5.6-terra`, high effort, `FRESH_SPAWN`, with one artifact path in `agent_execution_manifest.md`.
- **Discovery boundary:** The durable artifacts document page-complete mapping, continuous N and S inventories, full checker scopes, and a 13-ID ledger. No top-N boundary, old candidate list, review queue, or count target controlled the current discovery.
- **Display-zero exclusion:** No assigned source displays `P = 0`, `p = 0.000`, or equivalent, and no stable candidate depends on such a display. The values `P<.001` in C009 and C012 are inequality displays, not display zero.
- **Integrity and reproducibility:** The five direct-source hashes and all reused-artifact hashes pass `sha256sum -c`. Candidate arithmetic was reproduced from the cited direct PDF pages. After coordinator repair, local source links in checker and mapper-part artifacts resolve from their containing directories and end in truthful `#page=N` fragments.

## Artifact coherence and repairs

The coordinator repaired the following supportable omissions or stale statements without deleting, merging, renumbering, ranking, or suppressing a stable ID:

1. The C009 and C010 recheck records now state that the eTable prints component changes and a labelled cross-group P value but does not print the full contrast or confidence interval.
2. The C013 recheck now uses the source-matched interval `-0.02 to 0.11`, consistent with the corrected ledger.
3. The N006 numeric-checker precursor is retained for provenance but explicitly qualified by the direct recheck and pass 2; the stable C003 framing records that the proposed opposite endpoint boundary was not reproduced.
4. The N017 cross-source row now acknowledges the later C009-C013 table discrepancies.
5. Pass-1 proposals SP1-P02 and SP1-P03 retain their original provenance but now carry later pass-2/recheck qualifications that control the current comparator framing.
6. Thirty-four PDF links in four checker/mapper-part artifacts were repaired from an incorrect four-level parent traversal to the package-root three-level traversal.

The initial proposal record and its later qualification must be read together where a precursor statement was narrowed. The final report should use the ledger and recheck wording, not the superseded precursor wording.

## Evidence-card field audit

The candidate ledger is a registration artifact rather than the final report. For every C ID below, its ledger section does not yet use all exact final-card labels required by `report_spec.md`. In particular, the exact labels **Candidate statement**, **Source evidence**, **Reported-versus-comparator**, **Reasoning procedure**, **Mechanical evidence recheck**, **Quality-control relevance**, **Potential downstream evidence impact**, **Human verification steps**, and **Human adjudication fields** remain to be instantiated during report assembly. The underlying evidence for those fields is available in the ledger, recheck, checker provenance, and this audit. The report generator must populate every required label for every C ID and must preserve the blank human template exactly.

## C001 — Randomization age-stratum boundary differs across the main article and final support documents

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` follows the controlled scope because the same randomization and adjusted-analysis factor places exactly age 70 in different strata across supplied documents.
- **Quality and evidence facts:** The main article at `jama_parsons_2020_oi_190140.pdf#page=2` prints `<70` versus `>=70`. Protocol Update 10 and final support definitions at `joi190140supp1_prod.pdf#page=2`, `#page=5`, and `#page=40`, plus `joi190140supp2_prod.pdf#page=2` and `#page=5`, print `<=70` versus `>70` and identify the boundary as a correction.
- **Arithmetic or logic:** The two partitions differ only at age 70. Zero tolerance applies to membership in a stated boundary set.
- **Unsupported assumptions and missing inputs:** The sources do not establish the randomization-system configuration, participant ages, amendment implementation date, or adjusted-Cox encoding. No effect on an estimate or conclusion may be assumed.
- **Pagination and relationship identity:** All cited PDF pages exist. This is distinct from C002 eligibility and C003 endpoint definitions because the variable, operational use, and consistency rule differ.
- **Conclusion and downstream-impact bounds:** The package supports a metadata and reproducibility question, not a claim that the primary conclusion changes. If confirmed, a trial-data extractor or analysis reproducer could copy the wrong age-stratum definition.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; no candidate-specific source field is otherwise absent from the ledger/recheck pair.
- **Exact remaining human question:** Which age boundary was implemented in the randomization system and adjusted Cox analysis, and which supplied description represents that implementation?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Eligibility age/Gleason boundary differs across the main article, protocol, and SAP

- **Status:** Pending Human Adjudication.
- **Category audit:** `Analysis-unit or population inconsistency` is permitted as a secondary category because the boundary creates a concrete difference in the printed eligibility rule at exactly age 70.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=2` assigns age 70 to the group permitted grade group 2 or less. `joi190140supp1_prod.pdf#page=5`, `#page=15`, and `#page=16`, plus `joi190140supp2_prod.pdf#page=1`, assign age 70 to the group limited to Gleason 6 or less. Page 15 is the eligibility-section start; the exact protocol rule is on page 16.
- **Arithmetic or logic:** `<70/>=70` and `<=70/>70` differ only at 70, where the stated pathology allowance also differs.
- **Unsupported assumptions and missing inputs:** Participant-level ages, screening decisions, governing version dates, and eligibility records are absent. The evidence does not establish that any participant was classified differently.
- **Pagination and relationship identity:** All cited pages exist. This is not a duplicate of C001 because it concerns eligibility and pathology allowance rather than randomization strata; it is not C003 because eligibility and progression are separate rules.
- **Conclusion and downstream-impact bounds:** No paper-level conclusion effect is demonstrated. If confirmed, an eligibility extractor could encode the age-70 criterion incorrectly.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final card must retain the distinction between direct boundary text and inferred participant consequences.
- **Exact remaining human question:** Which age-specific pathology eligibility rule governed participants exactly age 70, and which protocol version governed screening?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Composite-progression age-boundary comparator requires version confirmation

- **Status:** Pending Human Adjudication.
- **Category audit:** The ledger retains `Measure, label, or scale inconsistency` for the versioned endpoint-label question. The current supplied endpoint pages do not reproduce an opposite age boundary, so the final card must not state that they do.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=3`, `joi190140supp1_prod.pdf#page=31`, and `joi190140supp2_prod.pdf#page=2` all assign age 70 to the older progression-threshold group using `<70` and `>=70`. The `<=70/>70` statement at `joi190140supp2_prod.pdf#page=1` is an eligibility definition, not the cited progression endpoint.
- **Arithmetic or logic:** The cited endpoint partitions match at age 70. The initially proposed opposite-boundary comparison was not reproduced from these pages.
- **Unsupported assumptions and missing inputs:** An alternative versioned endpoint definition, event-level classifications, and implemented endpoint code are absent. Carrying the eligibility boundary into the endpoint would be an unsupported cross-rule assumption.
- **Pagination and relationship identity:** All cited pages exist. C003 is retained separately from C002 because it addresses progression-endpoint versioning, but no duplicate eligibility mismatch should be asserted.
- **Conclusion and downstream-impact bounds:** The current package supports a version-confirmation question only. It does not support a claim that an endpoint event, estimate, or conclusion differs. If another governing definition exists, a review extractor could need a version-qualified endpoint label.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies. The final card must include the narrowed direct evidence, the nonreproduced original comparison, and the exact missing version input.
- **Exact remaining human question:** Is there another supplied or governing progression-endpoint version using `<=70/>70`, or did the analysis use the matching `<70/>=70` definitions on the cited pages?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Fourth counseling phase is printed as 16 months versus 17 months

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` matches the controlled scope because the duration of the same intervention phase differs across source locations.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=3` prints eight calls over 16 months. `joi190140supp1_prod.pdf#page=5` and `#page=29` print eight calls over 17 months within the same 24-month, 22-call schedule.
- **Arithmetic or logic:** Article durations give `1 + 2 + 4 + 16 = 23` months; protocol durations give `1 + 2 + 4 + 17 = 24` months. Both call-count sequences give `6 + 4 + 4 + 8 = 22` calls.
- **Unsupported assumptions and missing inputs:** Exact phase anchors, an inclusive-boundary convention, actual call logs, and a planned-versus-delivered distinction are absent.
- **Pagination and relationship identity:** All cited pages exist. No other stable ID compares this phase duration.
- **Conclusion and downstream-impact bounds:** No outcome conclusion effect is demonstrated. If confirmed, an intervention-characteristics extractor could copy an inconsistent maintenance-phase duration.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final reasoning field must state that boundary counting could reconcile the wording only if source documentation supports it.
- **Exact remaining human question:** Was phase 4 intended or delivered over 16 or 17 months, and does a documented phase-boundary convention reconcile the descriptions?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Per-protocol completion percentages do not reproduce from the stated arm denominators

- **Status:** Pending Human Adjudication.
- **Category audit:** `Denominator, proportion, or total inconsistency` matches the controlled scope.
- **Quality and evidence facts:** The statement spanning `jama_parsons_2020_oi_190140.pdf#page=4` and `#page=5` links 183 (81.7%) and 171 (79.5%) to arm totals 226 and 217. The listed noncompletion counts independently reproduce numerators 183 and 171.
- **Arithmetic or logic:** `183/226 = 80.97%`, displayed as 81.0% to one decimal; `171/217 = 78.80%`, displayed as 78.8%. Reverse calculation suggests denominators near 224 and 215, but those denominators are not printed.
- **Unsupported assumptions and missing inputs:** The evidence does not establish that 226 and 217 were the intended percentage denominators. The actual percentage denominators and any two-person arm-specific exclusions are absent.
- **Pagination and relationship identity:** Both cited pages exist. This denominator relationship is distinct from the missing-category display in C006 and pilot population accounting in C008.
- **Conclusion and downstream-impact bounds:** No effect on the trial's primary conclusion is demonstrated. If confirmed, an adherence or intervention-fidelity extractor could copy percentages without reproducible denominators.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the calculation must preserve the distinction between printed inputs and reverse-calculated diagnostic denominators.
- **Exact remaining human question:** What exact denominators and participant exclusions produced 183 (81.7%) and 171 (79.5%)?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Table 1 PSA categories do not exhaust the printed PSA denominators

- **Status:** Pending Human Adjudication.
- **Category audit:** `Denominator, proportion, or total inconsistency` matches the controlled scope.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=5` prints PSA denominators 224 and 217, followed by only two displayed category counts, 25/99 and 30/98. `joi190140supp2_prod.pdf#page=5` supplies a planned third PSA category, greater than 5 and less than 10, but not its Table 1 counts.
- **Arithmetic or logic:** Intervention displayed counts total `25 + 99 = 124`, leaving `224 - 124 = 100`. Control counts total `30 + 98 = 128`, leaving `217 - 128 = 89`.
- **Unsupported assumptions and missing inputs:** The source does not state whether the displayed categories are exhaustive. Assigning all remainders to the SAP's third category is plausible source-grounded reasoning, not a direct observation.
- **Pagination and relationship identity:** The cited pages exist. The comparator and rule differ from C005 and C008.
- **Conclusion and downstream-impact bounds:** No conclusion effect is demonstrated. If the display is intended as exhaustive, an extractor could copy an incomplete baseline PSA distribution.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final card must state the conditional nature of the exhaustion rule.
- **Exact remaining human question:** Are the 100 intervention and 89 control participants the omitted greater-than-5-to-less-than-10 category, and was Table 1 intended as a partial or exhaustive distribution?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Narrative calls gram-per-day cruciferous values “servings”

- **Status:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency` matches the controlled scope.
- **Quality and evidence facts:** The narrative at `jama_parsons_2020_oi_190140.pdf#page=5` says “cruciferous servings” while printing 43.10 g/d and 6.44 g/d. `jama_parsons_2020_oi_190140.pdf#page=7` and `joi190140supp3_prod.pdf#page=2` label those exact values as grams/day and print a separate servings/day row with 0.71 and 0.12.
- **Arithmetic or logic:** Exact value and interval matching maps the narrative values to the grams/day row; no conversion assumption is needed.
- **Unsupported assumptions and missing inputs:** Editorial intent is absent. The noun could be colloquial while the adjacent unit identifies the formal measure.
- **Pagination and relationship identity:** All cited pages exist. No other stable ID addresses this narrative label.
- **Conclusion and downstream-impact bounds:** No primary-outcome conclusion effect is demonstrated. If confirmed, a secondary-outcome extractor could code grams/day as servings/day.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final card must avoid prescribing wording and should ask which formal measure was intended.
- **Exact remaining human question:** Was the narrative intended to identify cruciferous intake in grams/day or the distinct servings/day measure?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Pilot total of 74 does not match table arm counts totaling 68

- **Status:** Pending Human Adjudication.
- **Category audit:** `Denominator, proportion, or total inconsistency` matches the controlled scope.
- **Quality and evidence facts:** `joi190140supp1_prod.pdf#page=12` describes a 74-man pilot with 2:1 allocation and prints table headers of intervention `n=45` and control `n=23` without a subset footnote.
- **Arithmetic or logic:** `45 + 23 = 68`, six below 74; `45/23 = 1.96`, approximately 2:1 but not participant accounting.
- **Unsupported assumptions and missing inputs:** The table may be an evaluable paired-dietary subset, but original arm totals, completion criteria, arm-specific missingness, and six-participant disposition are absent.
- **Pagination and relationship identity:** The cited page exists. This pilot denominator question is separate from main-trial denominator candidates C005 and C006.
- **Conclusion and downstream-impact bounds:** This concerns pilot feasibility context, not the main trial conclusion. If confirmed, an extractor could conflate randomized and evaluable pilot populations.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final card must identify 74 versus 68 as direct and the complete-case explanation as inferred.
- **Exact remaining human question:** What population do `n=45` and `n=23` represent, and what accounts for the other six randomized participants?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Energy 24-month between-group P value differs between Table 2 and the eTable

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` matches the controlled scope.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=7` prints component changes -250.01 and -130.3 kcal/day, contrast -119.71 with interval -211.78 to -27.65, and `P=.01`. `joi190140supp3_prod.pdf#page=2` prints the same components and the labelled cross-group `P<.001`; it does not print the full contrast or interval.
- **Arithmetic or logic:** `-250.01 - (-130.3) = -119.71`. The interval-based normal calculation is diagnostic only and cannot replace the supplied mixed-model output.
- **Unsupported assumptions and missing inputs:** A shared exact model output, unrounded estimates, covariance, degrees of freedom, contrast matrix, analytic version, and exact test statistic are absent. The evidence does not establish which P value was intended.
- **Pagination and relationship identity:** Both cited pages exist. This is distinct from C010 by measure and from C011/C012 by arm-specific within-group contrasts.
- **Conclusion and downstream-impact bounds:** No primary-outcome conclusion effect is demonstrated. If confirmed, a secondary-outcome extractor or meta-analytic dataset could copy different P values for the same labelled comparison.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final card must retain the narrowed eTable comparator and must not say the eTable prints the contrast interval.
- **Exact remaining human question:** What model, contrast, analytic version, and unrounded output produced each 24-month energy P value, and which value was intended?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Deep-yellow vegetables 24-month between-group P value differs across repeated tables

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` matches the controlled scope.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=7` prints intervention/control changes 0.19/0.05 servings/day, contrast 0.14 with interval 0.05 to 0.23, and `P=.004`. `joi190140supp3_prod.pdf#page=2` prints 0.19/0.06 and the labelled cross-group `P=.003`; it does not print the contrast or interval.
- **Arithmetic or logic:** Main displayed components give `0.19 - 0.05 = 0.14`; eTable displayed components give `0.19 - 0.06 = 0.13`. Unrounded components could differ from displayed subtraction. The interval-based normal calculation is diagnostic only.
- **Unsupported assumptions and missing inputs:** Unrounded components, exact model/test output, covariance, degrees of freedom, contrast matrix, analytic version, and rounding convention are absent.
- **Pagination and relationship identity:** Both cited pages exist. C010 addresses the repeated cross-group P value; C013 separately addresses the control component estimate. They share a row but not the same printed comparator or rule and are not duplicates.
- **Conclusion and downstream-impact bounds:** No primary-outcome conclusion effect is demonstrated. If confirmed, a secondary-outcome extractor could copy inconsistent P-value or component metadata.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final card must retain the narrowed comparator and explicitly cross-reference, rather than merge with, C013.
- **Exact remaining human question:** Which unrounded components, contrast, model output, and P value were intended for the 24-month comparison?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Intervention red-meat 12-month within-group P value differs across repeated tables

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` matches the controlled scope.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=7` and `joi190140supp3_prod.pdf#page=2` both print intervention change -11.54 g/day with interval -19.03 to -4.06 for the same within-group mixed-model contrast. The P values are `.003` and `.001`.
- **Arithmetic or logic:** The identical displayed estimate, interval, arm, time, unit, and comparison semantics establish the repeated-result match. The interval-based normal calculation is diagnostic only.
- **Unsupported assumptions and missing inputs:** Exact test statistic, degrees of freedom, covariance, unrounded output, and analytic version are absent. A production-version or inferential-convention explanation is possible but not printed.
- **Pagination and relationship identity:** Both pages exist. C011 and C012 concern different arms and remain distinct relationships.
- **Conclusion and downstream-impact bounds:** No primary-outcome conclusion effect is demonstrated. If confirmed, a secondary-outcome extractor could copy different P values for the intervention-arm result.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final card must label the normal calculation as diagnostic and avoid selecting a source value.
- **Exact remaining human question:** What exact model output and test definition produced each intervention-arm P value, and which output was intended?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Control red-meat 12-month within-group P value differs across repeated tables

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` matches the controlled scope.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=7` and `joi190140supp3_prod.pdf#page=2` both print control change -9.83 g/day with interval -17.26 to -2.41 for the same within-group mixed-model contrast. The P values are `<.001` and `.01`.
- **Arithmetic or logic:** The repeated estimate, interval, arm, time, unit, and comparison semantics match. The interval-based normal calculation is diagnostic only. `<.001` is not a display-zero P value.
- **Unsupported assumptions and missing inputs:** Exact test statistic, degrees of freedom, covariance, unrounded output, and analytic version are absent. No source identifies a distinct test between tables.
- **Pagination and relationship identity:** Both pages exist. The control-arm relationship is separate from intervention-arm C011.
- **Conclusion and downstream-impact bounds:** No primary-outcome conclusion effect is demonstrated. If confirmed, a secondary-outcome extractor could copy materially different thresholded P-value reporting for this control-arm result.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; no display-zero conditional field is required because neither source prints `P=0` or equivalent.
- **Exact remaining human question:** What exact mixed-model output produced the control-arm P value, and which displayed value and test were intended?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Deep-yellow vegetables 24-month control change differs across repeated tables

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` matches the controlled scope.
- **Quality and evidence facts:** `jama_parsons_2020_oi_190140.pdf#page=7` prints control change 0.05 servings/day with interval -0.02 to 0.11. `joi190140supp3_prod.pdf#page=2` prints 0.06 with the same interval. The corrected ledger and recheck both use -0.02 to 0.11.
- **Arithmetic or logic:** The displayed point estimates differ by `0.06 - 0.05 = 0.01`. The main components give a displayed difference of 0.14; the eTable components give 0.13, while unrounded values remain unavailable.
- **Unsupported assumptions and missing inputs:** Unrounded estimates and interval endpoints, mixed-model output, analytic version, and rounding convention are absent. Identical rounded intervals do not establish identical unrounded point estimates.
- **Pagination and relationship identity:** Both pages exist. This component-estimate relationship is not a duplicate of C010's P-value relationship; the two must remain separately cross-referenced.
- **Conclusion and downstream-impact bounds:** No primary-outcome conclusion effect is demonstrated. If confirmed, a secondary-outcome extractor could copy a different component estimate and derive a different displayed subtraction.
- **Missing evidence-card fields:** The standard exact-label field gap listed above applies; the final card must use the corrected interval and must not merge or suppress this ID under C010.
- **Exact remaining human question:** Which unrounded control estimate, model output, analytic version, and displayed value were intended, and how does it relate to the adjacent cross-group result?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Duplicate, impact, and tone audit

- C001, C002, and C003 share an age-70 topic but concern randomization, eligibility, and progression-endpoint definitions, respectively; their comparators and consistency rules are distinct.
- C010 and C013 concern the same table row but different printed relationships: a cross-group P value and a control-arm component estimate. They remain separate and cross-referenced.
- C011 and C012 concern different trial arms. No stable IDs were merged or suppressed.
- Every candidate's paper-level conclusion impact is bounded to “not demonstrated.” Potential downstream language identifies only what a future extractor, evidence table, or analysis reproducer could copy if a human confirms the candidate.
- Wording remains neutral quality control. Every stable ID remains Pending Human Adjudication.

## Finalization dependencies

Scientific source coverage, relationship coverage, stable-ID recheck coverage, and this evidence-quality audit are complete. Workflow closure still requires coordinator-owned report generation, addition of the `report_generation` coverage row with C001-C013 enumerated, completion of the manifest status for this audit, exact blank adjudication fields in every final report card, token-accounting finalization, HTML rendering, and a passing mechanical validator result.
