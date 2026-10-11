# Numeric and source-coverage audit part — Workflow 1.6.1

Runtime agent: `/root/numeric_coverage_auditor`. Assigned disjoint scope: all 39 parent numeric relationships N001–N028 and N101–N111, all subordinate numeric rows, all 83 mapper page-coverage rows, direct-source identity and document roles, all 95 reused evidence assets, all 13 current-run visual derivatives, coverage paths, tooling and execution controls. This part does not replace the separate candidate/screening audit or the separate statistical-relationship audit. It assigns no candidate ID or human disposition. Scientific coverage: COMPLETE. New threshold findings: none.

The complete scope and review-contract controls, settings, performance controls, numeric inventory and numeric checker were read. Both mapper page ledgers and every numeric family and subordinate table were reviewed. Source, coverage, evidence-asset, hash, tooling, routing, execution and run-state controls were audited. Old scientific decision records and other packages were not read. No web or Python scientific review was used. Direct Poppler PDF text was streamed for main Table 1 and Table 2 and support baseline, individual-outcome, adverse-reaction and simulation tables; no new evidence derivative was created by this auditor.

## Direct-source closure

| Source | Content-assigned role | Physical pages | Reusable | Fresh-required | Mapped | Audit result |
|---|---|---:|---:|---:|---:|---|
| DOC-001, jama_stunnenberg_2018_oi_180136.pdf | REPORT: completed main investigation | 10 | 10 | 0 | 10 | COMPLETE; page ledger is consecutive 1–10. |
| DOC-002, joi180136supp1_prod.pdf | PLAN: prospective June 2011 version 2 protocol | 55 | 55 | 0 | 55 | COMPLETE; page ledger is consecutive 1–55, including blank, background and administrative/reference pages. |
| DOC-003, joi180136supp2_prod.pdf | REPORT: retrospective results, figures, tables and model/simulation methods | 17 | 17 | 0 | 17 | COMPLETE; page ledger is consecutive 1–17, including the image-based eligibility table and all figures. |
| DOC-004, joi180136supp3_prod.pdf | REPORT: retrospective data-sharing statement | 1 | 1 | 0 | 1 | COMPLETE; page 1 opened and explicitly records no result-relevant numeric relationship. |

All four rows close independently: reusable plus fresh-required equals total, mapped equals total, and each is COMPLETE. The two mapper scopes are disjoint and exhaust 83 physical pages: 28 REPORT and 55 PLAN. Page-ledger parsing found no duplicate, missing or nonconsecutive unit. A page without an applicable quantitative result has an explicit opened-content record; it is not omitted.

Recursive source-file inventory found precisely the four supplied PDFs and no supplied DOC, DOCX, XLS, XLSX or CSV source. Current direct `pdfinfo` confirms 10/55/17/1 pages and no encryption. Current native `pdftotext` streams are byte-identical to all four reused native text files, and current `pdfinfo` streams are byte-identical to all four reused metadata records. Every source SHA-256 matches `source_hashes_before.sha256`: four of four checks passed. The content descriptions support the roles; physically attaching a prospective protocol as a supplement does not turn DOC-002 into REPORT content. DOC-003 contains retrospective method descriptions rather than a separate supplied prospective plan component.

## Reusable and fresh evidence assets

The asset inventory and before-hash manifest have identical sets of 95 package-relative paths. Independent `sha256sum -c` checks matched all 95. Inventory counts reproduce: four native text files, four layout text files, four metadata records and 83 PNG page images; 88 USABLE, six PARTIAL and one DUPLICATE. Source-family totals are DOC-001 13, DOC-002 58, DOC-003 20 and DOC-004 4 assets. Unique source-unit coverage remains 83; multiple derivatives never inflate page counts.

PARTIAL text assets are complemented by explicitly source-linked usable page images. The union closes every source page, so zero fresh-required pages is supported. The support mapper records visual inspection of the image-based DOC-003 p2 criteria table, figures on pp7–9, simulation tables on pp16–17, and the protocol schematic/schedule/decision graphics. The main mapper records visual inspection of all main table and figure pages. Missing OCR and Office conversion capabilities therefore leave no assigned unit uncovered. Legacy image-generator versions remain unknown and complete image pixel identity is not asserted; current native identity, metadata identity, page-family location mapping and direct-source authority are explicitly retained.

All 13 newly generated PNGs exist, have PNG signatures and dimensions compatible with their recorded source geometry and render settings, and appear individually in both the asset inventory and coverage manifest. Each inventory row records one exact physical source page, Poppler `pdftoppm` 25.03.0, the rendering command and purpose. Their scopes are: main p5 and plan p39 cross-source confirmation; main p5 statistical-pass-1 confirmation; main pp6–8 screening confirmation; main pp3–5, plan p41, and results pp10/11/13 recheck confirmation. They are additional confirmation assets and are correctly excluded from the reused-asset hash set.

## Complete numeric relationship audit

Every family has a complete checker-register row. Subordinate rows are retained under their parent and are not sampled. The canonical main and support maps plus numeric inventory total 128622 bytes before the small audit repair, below the 200000-character shard bound; 39 parent numeric families are below the 120-relationship bound. The bound controls context size and does not control observations or candidate discovery.

| Family | Numeric audit result |
|---|---|
| N001 | COMPLETE: 38−8=30 and 1+7=8; randomized/treated totals match flow and narrative. |
| N002 | COMPLETE: 30−3=27 and 2+1=3; completer/analysis totals retained. |
| N003 | COMPLETE: age mean/dispersion/range and 22 men plus 8 women retained; the abstract percent-symbol observation is catalogued. |
| N004 | COMPLETE: 16+11=27 analyzed; enrolled genotype allocation is distinguished from completer allocation and the complete roster. |
| N005 | COMPLETE: all recruitment, visit and follow-up dates are mapped as administrative/calendar comparisons. |
| N006 | COMPLETE: 200×3=600 mg/day; 4+1+4+2=11 weeks; one to four sets and 4–16 visits mapped. |
| N007 | COMPLETE: IVR windows, scales, direction and observed zero values retained without silent normalization. |
| N008 | COMPLETE: period/set and measurement timings recorded; explicit four-week treatment periods resolve the wording. |
| N009 | COMPLETE: 24+3=27; 24/27=88.8889% and 3/27=11.1111%; patient 11 exception retained. |
| N010 | COMPLETE: stopping thresholds and 80%-displayed outcomes assessed with half-unit display intervals and advisory decisions. |
| N011 | COMPLETE: 23+4=27; 23+2×4=31; all four two-set patient identifiers retained. |
| N012 | COMPLETE: 773/868=89.0553%, 2676/2728=98.0938%, and 31×28=868. Unprinted measurement allocations are not invented. |
| N013 | COMPLETE: baseline, arm-score scale and Bayesian arm quantities retained; 5.56−2.50=3.06. |
| N014 | COMPLETE: all 14 Table 1 rows, subgroup denominators and definitions retained. The 5/11 versus 46% summary was repaired as recorded below. |
| N015 | COMPLETE: consecutive-patient claim, series axis and probability labels retained; graphical values are identified as approximate. |
| N016 | COMPLETE: all INQoL scale definitions and summaries retained; source-bound quartile and dispersion checks reproduce. Candidate inclusion audit is assigned to the separate candidate audit. |
| N017 | COMPLETE: both SF-36 components, bounded baseline distributions, units and change directions retained; marginal means are not assumed to define paired effects. |
| N018 | COMPLETE: all first/fifth/mean clinical tests and walking measurement units/timing retained. |
| N019 | COMPLETE: all dynamometry and paresis rows retained; 0–600 N and 0–100% bounds, timing and model/paired distinctions recorded. |
| N020 | COMPLETE: EMG grade 0–3 and measurement timing retained; baseline absence is explicit. |
| N021 | COMPLETE: .75/3.85=19.4805%, .75/1.75=.428571, 2/3.85=51.9481% and 2/1.75=1.142857; approximate clinical translations are separated from exact extraction inputs. |
| N022 | COMPLETE: GI 21/30=70% and serious event 1/30=3.3333%; matched report occurrences retained. |
| N023 | COMPLETE: the no-observed-cardiac-abnormality statement is retained without inventing a printed count or percentage. |
| N024 | COMPLETE: serum concentration mean/SD/range and dose-reference quantities retain their distinct units. |
| N025 | COMPLETE: two subtherapeutic patient IDs, .11/.27 concentrations and .5 lower reference boundary retained. |
| N026 | COMPLETE: 94% adherence and two below 75% retained; absent contributor/pill denominators bound mechanical reconstruction. |
| N027 | COMPLETE: 26/31=83.8710% treatment-set preference; explicit denominator and later shorthand are distinguished. |
| N028 | COMPLETE: all 24 continued responders and 18–31-month follow-up retained. |
| N101 | COMPLETE: all eligibility, QT/QRS and medication washout thresholds and the report counterpart mapped. |
| N102 | COMPLETE: prospective 200/400/600 mg/day titration, treatment/washout periods and 11–44-week range mapped. |
| N103 | COMPLETE: every primary observation week at successive 11-week offsets and every endpoint scale/window mapped. |
| N104 | COMPLETE: all schedule starts/ends, evaluation/washout cells, measurement visits and visual diagram groups mapped. |
| N105 | COMPLETE: all contraction, relaxation, force, duration, percentage and grading definitions retained. |
| N106 | COMPLETE: seven plus eight reporting days, three DSMB members, and 10% of 30=3 assessed; safety decision definitions remain separately tracked. |
| N107 | COMPLETE: 30=20+10, chloride/sodium allocation and all center/cohort calendar figures mapped without converting administrative differences into efficacy findings. |
| N108 | COMPLETE: all 30 patient baseline rows and all numeric columns retained; 22 men/8 women and 18 CLCN1/12 SCN4A reproduce. Removing patients 3/6/7 yields analyzed 16/11. |
| N109 | COMPLETE: all 27 individual primary-outcome tuples, interim numbers, probabilities and treatment decisions retained; continued 24/stopped 3 and 31 sets reproduce. |
| N110 | COMPLETE: all 12 adverse-reaction/category rows in both arms and the serious-event figure retained. Percentage checks distinguish the 2/30 versus 6% display; unestablished category exhaustiveness does not permit a union calculation. |
| N111 | COMPLETE: both six-column/eight-row simulation summaries, all 96 summary cells, 12 valid/missing pairs and both frequency tables retained. 315+685=1000, 685/1000=68.5%, 1.29−1.75=−.46, 4.65−4.58=.07 and 4.67−3.38=1.29 reproduce. |

Main subordinate coverage is all 14 baseline rows and all 34 Table 2 outcome rows, plus the four interaction references. Support subordinate coverage is all 30 baseline patients, all 27 individual outcomes, all 12 adverse-reaction/category rows and every simulation cell and frequency-table entry. Numeric scale, unit, count, rounding, sign and effect-measure identity checks preserve statistical-model distinctions. A difference of marginal quantiles is not substituted for a quantile of within-replicate differences.

The INQoL corroborating bound reproduces with half-unit mean precision: for n=27 and m=96.885, maximum sample SD is approximately 17.7032; the weaker all-n≥2 bound is approximately 24.5681. Both remain below the printed SD interval [38.485,38.495). Upper-quartile rounding intervals [110.25,110.35) and [119.95,120.05) do not intersect 0–100. This calculation concerns reported scale/summary reconciliation; it does not establish that the treatment contrast itself violates a bounded-change rule.

## Coverage paths, execution and discovery controls

The coverage manifest contains one plain relative artifact path per row, including one separate row for each derivative and each audit shard. Existing COMPLETE paths resolve. Audit assembly, its currently running shard outputs and report generation were still pending at inspection; these are workflow-ordering items for the coordinator to close, not source-unit omissions. Forty-two explicit PDF-link occurrences across the assigned mapper/numeric/checker artifacts resolve to supplied files and have physical page numbers within the independently confirmed page bounds. Other numeric locators name truthful physical page/table/paragraph locations.

The execution manifest records distinct fresh `root/statistics_pass_1` and `root/statistics_pass_2`, both `gpt-6.1-sol`/`high`, and a distinct fresh `root/inclusion_screener` under the same model/effort contract. Mapper, numeric and cross-source mandatory stages are separately identified; the rechecker, primary quality auditor and two optional audit shards each have distinct fresh IDs. This audit runtime appears exactly once. Routing preflight records PASS, INTERACTIVE_CLI, CURRENT_SESSION and the ten required presets. Report-generator registration remains the coordinator's subsequent stage. No stage reuse or duplicate manifest ID is present in the inspected manifest.

The package-specific 25–40-minute target has a bounded source/tooling/complexity basis. It is a timing target, not a candidate-count target. Neither mapper scope nor numeric inventory/checker contains a count-driven discovery or screening rule. The artifacts explicitly retain complete unit and relationship coverage and distinguish context limits from finding limits. The recorded evidence input paths are supplied sources or extraction assets. This auditor used no old candidate list as an input; observable records support fresh source-based discovery. This audit cannot reconstruct provider-internal execution events beyond the supplied routing/runtime manifest and durable agent artifacts.

## Repairs and reasons

| Repair | Reason | Completed evidence |
|---|---|---|
| Numeric checker and N014 register now distinguish 5/11 from printed 46%. | 100×5/11=45.4545% lies below [45.5,46.5), so describing the display as nearest-whole rounding reconciliation did not reproduce. The explicit count and denominator immediately resolve the baseline extraction quantity; no named primary/key-secondary result changes. | Coordinator repair reread: numeric summary corrected; a `CONTEXT_RESOLVES` row added to `Excluded observations`; N014 register updated. Numeric exclusions are now 21. No stable candidate or finding decision changed. |
| Tooling record now states that completed source inventory found no Office or CSV source and all 83 PDF pages are mapped. | The previous prospective wording about Office inventory was stale after inventory/mapping completion. | Coordinator repair reread in `Tooling limitations`; unavailable OCR/Office capabilities affect no source unit. |

No further numeric screening repair or threshold finding was identified in this assigned shard. Every scientific input and every reused asset remains unchanged. Final after-hash manifests, canonical audit/report assembly, final timing, HTML and validator completion belong to coordinator closure after the running audits finish.

## Limitations and handoff

There is no scientific source-unit or numeric-family coverage gap. Mechanical reconstruction remains bounded by unreported paired contributor sets, adherence denominators and adverse-category exhaustiveness, and by nonnumeric graphical readouts. Legacy image-generator versions and complete pixel identity are not established; direct supplied PDF evidence remains authority. Statistical estimate/test/method compatibility, every stable C ID, every screening decision and every checker exclusion are audited in the separately assigned statistical and candidate/screening parts and must be merged by the coordinator.

Covered numeric IDs: N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N101, N102, N103, N104, N105, N106, N107, N108, N109, N110, N111. Counts: 39/39 parent families, 83/83 physical pages, 4/4 direct-source hash matches, 95/95 reused-asset hash matches, 13/13 inventoried current-run derivatives; two completed documentation repairs and zero new threshold findings.
