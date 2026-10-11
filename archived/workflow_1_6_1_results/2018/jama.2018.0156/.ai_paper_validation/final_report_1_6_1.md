# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication**

This report prepares candidate reporting issues for human review. Evidence reproduction and inclusion audit describe the review record; they do not decide validity, importance, action, or a correction. All four candidates remain Pending Human Adjudication.

## Executive Quality-Control Summary

Complete review of the three supplied PDFs identified **4 stable candidates**: two comparisons of planned and reported primary/key-secondary analysis elements, one safety-population membership inconsistency within the article, and one post-hoc population-conservation inconsistency between report documents. All four have evidence state `reproduced` and inclusion audit `CONFIRMED`. Six checker findings underwent independent screening: five INCLUDE rows were consolidated into four distinct issues, and one duplicate was screened out.

All 146 physical source pages were mapped, including 145 reusable-backed pages and one freshly inspected page. The canonical inventories contain 155 numeric relationships and 33 statistical relationships. Two distinct fresh statistical reviewers completed every statistical relationship. The independent quality audit covered all stable IDs, screening decisions, checker exclusions, classifications, and coverage records. These findings do not establish changed event totals, changed trial conclusions, or realized downstream propagation.

Abbreviations used below: BMV, bag-mask ventilation; ETI, endotracheal intubation; CPC, cerebral performance category; ROSC, return of spontaneous circulation; ITT, intention to treat; PP, per protocol; AT, as treated; NI, noninferiority; SAP, statistical analysis plan. Differences expressed as percentages are absolute percentage-point differences unless stated otherwise.

## Package and Reused-Evidence Provenance

The package contains a randomized-trial article comparing BMV with ETI during out-of-hospital cardiac-arrest resuscitation, a bound prospective protocol/amendment/SAP supplement, and a separate results supplement. Document roles were assigned from content.

| Stable source | Actual filename | Role | Physical PDF pages | SHA-256 |
|---|---|---|---:|---|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | REPORT | 9 | `114e922542bbb1f8369ca9b5c19be65d93856e16cf4ff295c483439e4e208839` |
| DOC-002 | joi180004supp1_prod.pdf | PLAN | 134 | `70106d31b08e3a9d7eaac8a0e035bbf8d92a43b51f2483b634d7349b0c5f6913` |
| DOC-003 | joi180004supp2_prod.pdf | REPORT | 3 | `937e18794fc87074907b1e9ab792f9a35d2f2d895d586dd27e7cbf44d5ed8d46` |

The curator inventoried and hashed 104 existing source-linked text, OCR, rendered-page, and provenance assets. Twelve whole-document native/layout files use physical-page form-feed locators; six alternate PyMuPDF extractions overlap coverage. Current Poppler extraction matched existing native/layout text. Source-hash-matched OCR and page images supplied locators for scanned plan pages. Historical derivative engine versions are incomplete for some assets; source PDFs remain the authority. Candidate recheck used current direct-source visual confirmations rather than treating OCR as final evidence. This run was CPU-only, invoked no GPU or fresh OCR, and preserved supplied sources and reused assets.

Discovery and classification were rebuilt from source-linked assets plus fresh coverage. Earlier candidate, screening, disposition, and report records were preserved and did not determine scientific scope. See the [source inventory](review_1_6_1/source_inventory.md), [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md), and [source hash record](review_1_6_1/source_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators; estimate, interval and test logic; source-grounded statistical-method logic; and planned-versus-reported statistical design. It uses only supplied package evidence. It does not perform a participant-level, broad methodology, clinical, novelty, or misconduct audit, or propose a preferred analysis.

| Source | Unit type | Total | Reusable | Fresh-required | Mapped | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 — jama_jabre_2018_oi_180004.pdf | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 — joi180004supp1_prod.pdf | PDF_PAGE | 134 | 133 | 1 | 134 | COMPLETE |
| DOC-003 — joi180004supp2_prod.pdf | PDF_PAGE | 3 | 3 | 0 | 3 | COMPLETE |
| Total | PDF_PAGE | 146 | 145 | 1 | 146 | COMPLETE |

Main mapping covered pages 1–9. Disjoint support parts covered plan pages 1–56 and plan pages 57–134 plus results pages 1–3. All administrative, historical, bibliographic and form pages received explicit applicability records. Fresh-required [joi180004supp1_prod.pdf — PDF p. 134](<../joi180004supp1_prod.pdf#page=134>) was rendered with CPU Poppler 25.03.0 and visually inspected: it has a dated SAP header/footer and empty body. No scientific source-unit gap remains. The [coverage ledger](review_1_6_1/source_coverage.md) and [coverage manifest](review_1_6_1/coverage_manifest.md) retain the assignments and artifact handoffs.

Rounding/display precision, immediately resolved notation or wording, model-versus-crude comparisons, conditional observations, peripheral comparisons, and out-of-focus observations were excluded under the scope rules. Numeric checks allowed half-unit display intervals; participant/event counts were additionally constrained to integers. No candidate rests on a display-zero P value. Unnamed inferential algorithms were not replaced with diagnostic approximations.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) contains 155 unique N relationships: 98 main-report and 57 support relationships. Coverage includes allocation and analysis sets, safety and crossover membership, category partitions, numerator/denominator and percentage pairs, contrast direction, matched occurrences, and prospective design inputs. The [statistical inventory](review_1_6_1/statistics/relationship_inventory.md) contains 33 unique S relationships and a complete crosswalk of mapper-local groups.

Both [statistical pass 1](review_1_6_1/checkers/statistical_pass_1.md) and [statistical pass 2](review_1_6_1/checkers/statistical_pass_2.md) covered S001 through S033, with explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records for all 33. Pass 1 runtime was `01a128e8-4022-7ff0-8a20-57d007b2fa27`; pass 2 runtime was `01a128f7-8354-7f82-b8fd-4c65c1fbd3e2`. Both were fresh, distinct `gpt-6.1-sol`/`high` agents. Pass 2 considered the complete ledger, screening decisions and recheck facts and emitted no new findings.

Applicable checks included point-estimate containment, interval order, sign/reference-group agreement, matching population/outcome/time point/model, reported NI decisions against the −1-percentage-point margin, sample-size inputs, population and missing-data specifications, and planned-output requirements. The primary printed lower bounds and reported inconclusive NI decision were assessed without claiming equivalence or inferiority. The article supplies no trial test statistic or standard error, and does not identify every actual interval algorithm or row-specific test selection; exact reconstruction beyond supplied definitions was not assumed. Source-linked diagnostic calculations remained diagnostics.

## Inclusion Screening Summary

A candidate must be reproduced from exact supplied locations, fall within the quantitative focus, remain unresolved by immediate context for a statistically literate reader, and plausibly affect interpretation of a named result or its extraction. Each emitted finding received exactly one independent decision in the [screening log](review_1_6_1/screening/inclusion_screen.md).

| Decision | Reason code | Finding rows |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 5 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 1 |
| Total | All decisions | 6 |

The five included rows map to four stable issues: F-XS-001 → C001; F-XS-002 and F-ST1-003 → C002; F-NUM-001 → C003; F-ST1-002 → C004. F-ST1-001 duplicates C001 and is retained as screened-out provenance, without a separate card. Statistical pass 2 and the quality audit emitted no additional finding requiring a second screen.

Checker self-exclusions are separate from these six independently screened finding rows: numeric 33, cross-source 20, statistical pass 1 23, and statistical pass 2 27. The initial checkers therefore recorded 76 excluded observations; pass 2 recorded 27. The quality auditor assessed all 103 canonical exclusion rows, including the already registered patterns revisited in pass 2, without double-counting copied support parts. It confirmed all six screening decisions and identified no additional distinct qualifying issue.

## Review-Domain Summary

`statistical_results` covers report-material counts, estimates, tests and statistical methods. `report_internal_inconsistency` covers unresolved attribution of a number to an outcome, time point, analysis set or comparison. `protocol_report` compares prospective statistical-design/analysis content with reported content. `plan_material` covers an unresolved statistical-design inconsistency solely within prospective material.

| Review domain | Candidates |
|---|---:|
| statistical_results | 2 |
| report_internal_inconsistency | 0 |
| protocol_report | 2 |
| plan_material | 0 |
| Total | 4 |

| Primary relationship type | Meaning | Candidates |
|---|---|---:|
| P_R | PLAN versus REPORT | 2 |
| P_P | Within/between PLAN content | 0 |
| S_C | Between different REPORT documents | 1 |
| S_W | Within one REPORT document | 1 |
| Total | | 4 |

| Evidence state | Candidates |
|---|---:|
| reproduced | 4 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 4 |

All four inclusion audits are CONFIRMED; zero are QUESTIONED. Classification follows content and precedence `P_R > P_P > S_C > S_W`. Each candidate has one independent conflicting relationship; corroborating documents do not add relationship types. These counts reconcile to the [final ledger classification table](review_1_6_1/candidate_ledger.md).

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#c001--amended-primary-success-definition-and-reported-cpc-threshold) | Amended primary success condition versus explicit CPC coding | protocol_report | P_R | reproduced | CONFIRMED |
| [C002](#c002--planned-additional-population-outputs-and-identified-reported-analyses) | Planned additional-population outputs lack identified supplied counterparts | protocol_report | P_R | reproduced | CONFIRMED |
| [C003](#c003--direct-eti-crossover-and-safety-membership-accounting) | Direct ETI crossover absent from enumerated safety sets | statistical_results | S_W | reproduced | CONFIRMED |
| [C004](#c004--post-hoc-reassignment-population-and-success-totals) | Stated reassignment does not conserve displayed totals | statistical_results | S_C | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Amended primary success definition and reported CPC threshold

**Status:** Pending Human Adjudication

**Candidate statement:** The final protocol adds survival with unchanged pre-existing neurological disability as a primary favorable-survival condition, whereas the report explicitly counts CPC 1/2 only. The supplied package does not identify which operative success rule produced the reported primary numerators.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN final protocol/amendment vs REPORT main article/results supplement primary endpoint

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Classification rationale:** Prospective endpoint definitions in the final protocol and disclosed amendment are PLAN; primary and sensitivity outcome statements are REPORT. They constitute P_R and focus D. REPORT documents agree on CPC≤2. The older protocol/SAP establishes amendment chronology rather than an independent P_P inconsistency. Duplicate checker provenance F-ST1-001 was screened out as DUPLICATE_OF_INCLUDED and remains associated with C001.

**Classification ambiguity:** The historical SAP retains the prior CPC wording; actual implementation or a later withdrawal of the added disability provision is not supplied. Document roles and primary relationship remain clear.

**Exact source locations:**

| Role/function | Actual source and exact location |
|---|---|
| PLAN amended endpoint | [joi180004supp1_prod.pdf — PDF p. 71, final protocol §4.1.1](<../joi180004supp1_prod.pdf#page=71>) |
| PLAN disclosed amendment | [joi180004supp1_prod.pdf — PDF p. 110, primary-endpoint comparison row](<../joi180004supp1_prod.pdf#page=110>) |
| REPORT abstract endpoint/results | [jama_jabre_2018_oi_180004.pdf — PDF p. 1, Main Outcomes and Results](<../jama_jabre_2018_oi_180004.pdf#page=1>) |
| REPORT endpoint definition | [jama_jabre_2018_oi_180004.pdf — PDF p. 3, Outcomes](<../jama_jabre_2018_oi_180004.pdf#page=3>) |
| REPORT primary results | [jama_jabre_2018_oi_180004.pdf — PDF p. 4, Primary Outcome](<../jama_jabre_2018_oi_180004.pdf#page=4>) |
| REPORT explicit success coding | [jama_jabre_2018_oi_180004.pdf — PDF p. 6, Table 2 CPC blocks and footnote b](<../jama_jabre_2018_oi_180004.pdf#page=6>) |
| REPORT both sensitivity endpoint labels | [joi180004supp2_prod.pdf — PDF p. 3, both eTable 2 survival rows](<../joi180004supp2_prod.pdf#page=3>) |
| PLAN historical corroboration | [joi180004supp1_prod.pdf — PDF p. 15, original protocol §4.1.1](<../joi180004supp1_prod.pdf#page=15>) |
| PLAN historical SAP | [joi180004supp1_prod.pdf — PDF p. 122, SAP §6.1](<../joi180004supp1_prod.pdf#page=122>) |
| PLAN scanned SAP counterpart | [joi180004supp1_prod.pdf — PDF p. 131, SAP §6.1](<../joi180004supp1_prod.pdf#page=131>) |

**Source evidence:** The final protocol first defines day-28 favorable survival as CPC≤2, then adds survival with the same neurological disability present before randomization. The amendment comparison expressly adds this provision. The report defines favorable function as CPC 1/2 or CPC≤2, and Table 2 footnote b explicitly counts CPCs 1 and 2 as primary success. The abstract reports ITT 44/1018 versus 43/1022, difference 0.11%, one-sided 97.5% lower bound −1.64%, NI P=.11. PP has 43/995 versus 40/943, difference 0.08%, lower bound −1.74%, NI P=.12. Both supplementary sensitivity rows label CPC≤2 day-28 survival.

**Reported-versus-comparator:** REPORT success is the strict CPC 1/2 category. Amended PLAN success additionally allows unchanged pre-existing neurological disability. Historical PLAN/SAP locations use the earlier strict threshold and corroborate chronology; they do not show a later restoration of that threshold.

**Reasoning procedure:** Compare sufficient success conditions for the same primary day-28 endpoint, then connect the explicit coding footnote to category counts and primary results. This is a categorical definition comparison, not an assumption that a participant had CPC>2 or that any event count changes. Immediate REPORT context establishes its strict coding but does not reconcile the extra PLAN condition.

**Calculation:** ITT CPC 1+2 gives BMV 35+9=44 and ETI 37+6=43; PP gives 35+8=43 and 34+6=40. Percentages are respectively 4.32220%, 4.20744%, 4.32161%, and 4.24178%, consistent with displayed 4.3%/4.2% under half-unit bounds. These count/rate displays reconcile. No numerical rounding interval can add or remove the categorical unchanged-disability success condition.

**Affected result or extracted value:** The endpoint definition attached to ITT 44/1018 versus 43/1022 and PP 43/995 versus 40/943, their NI contrasts and lower bounds, and both sensitivity endpoint labels.

**Why context does not resolve it:** The supplied report does not state whether the disability provision was implemented, withdrawn, or irrelevant to the observed survivors. CPC-category sums confirm the reported numerators but do not provide baseline-to-day-28 neurological linkage or an operative amended coding rule.

**Alternative source-grounded interpretations:** The amended condition could have been implemented with abbreviated reporting; a later decision could have restored strict CPC coding; or both conditions could yield identical observed counts. None of these implementation explanations is established by the supplied aggregate documents.

**Mechanical evidence recheck:** Every affected and historical location was found and visually confirmed against current source-matched PDF renders. Printed conditions, coding footnote, CPC counts, denominators and result labels matched; the logical comparison and precision check reproduced without transcription/location revision. Necessary printed definition/count inputs are available. Missing inputs are baseline neurological disability, baseline-to-day-28 linkage, the implemented indicator for unchanged CPC>2 disability, and any later endpoint decision. Direct observations are the two printed definitions; implementation, withdrawal and equal totals are possible explanations. Remaining human question: which primary success-coding rule governed pre-existing neurological disability and produced the printed ITT/PP successes?

**Potential downstream evidence impact:** If confirmed, a systematic-review extractor could attach a different favorable-neurological-survival definition to the primary or sensitivity contrast. No altered event total, trial conclusion or actual downstream reuse is established.

**Human verification steps:** Read the final endpoint and amendment beside Table 2 footnote b; identify the operative coding specification and any later documented decision; verify how unchanged pre-existing disability was handled in the ITT/PP success indicators; reconcile that rule with the printed numerators before selecting an endpoint definition for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Planned additional-population outputs and identified reported analyses

**Status:** Pending Human Adjudication

**Candidate statement:** Prespecified AT primary/key-secondary efficacy and randomized-group ITT safety outputs are not identifiable among the supplied report's named analyses. This is one repeated planned-population-output reporting issue, covering both efficacy and airway-safety manifestations.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP population-output requirements vs REPORT main article/results supplement identified analyses

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-003

**Classification rationale:** SAP population definitions and output requirements prescribe analysis and are PLAN. The main article and results supplement identify conducted analyses and are REPORT. Focus D and P_R apply to explicit primary/key-secondary requirements. Jointly corroborating REPORT locations do not add S_C, and historical SAP wording does not create an independent P_P comparison.

**Classification ambiguity:** The SAP contains original-date and final-analysis wording. A later reporting decision or fuller population mapping is possible but not identified by the supplied amendments; roles and P_R precedence are clear.

**Exact source locations:**

| Role/function | Actual source and exact location |
|---|---|
| PLAN analysis sets | [joi180004supp1_prod.pdf — PDF p. 121, SAP §§5.1–5.3](<../joi180004supp1_prod.pdf#page=121>) |
| PLAN output requirements | [joi180004supp1_prod.pdf — PDF p. 124, SAP §§8.2.1, 8.2.3, 8.2.4](<../joi180004supp1_prod.pdf#page=124>) |
| PLAN scanned analysis sets | [joi180004supp1_prod.pdf — PDF p. 130, SAP §§5.1–5.3](<../joi180004supp1_prod.pdf#page=130>) |
| PLAN scanned methods | [joi180004supp1_prod.pdf — PDF p. 133, SAP analysis sections](<../joi180004supp1_prod.pdf#page=133>) |
| REPORT abstract efficacy/airway outcomes | [jama_jabre_2018_oi_180004.pdf — PDF p. 1, Results](<../jama_jabre_2018_oi_180004.pdf#page=1>) |
| REPORT analysis rules | [jama_jabre_2018_oi_180004.pdf — PDF p. 3, Statistical Analysis](<../jama_jabre_2018_oi_180004.pdf#page=3>) |
| REPORT flow/population/primary/adverse-event results | [jama_jabre_2018_oi_180004.pdf — PDF p. 4, Figure and results](<../jama_jabre_2018_oi_180004.pdf#page=4>) |
| REPORT named tables/sensitivity continuation | [jama_jabre_2018_oi_180004.pdf — PDF p. 6, Tables 2/3 and post-hoc text](<../jama_jabre_2018_oi_180004.pdf#page=6>) |
| REPORT ITT sensitivity output | [joi180004supp2_prod.pdf — PDF p. 3, eTable 2](<../joi180004supp2_prod.pdf#page=3>) |
| REPORT complete-output inspection, additional article pages | [jama_jabre_2018_oi_180004.pdf — PDF p. 2](<../jama_jabre_2018_oi_180004.pdf#page=2>), [PDF p. 5](<../jama_jabre_2018_oi_180004.pdf#page=5>), [PDF p. 7](<../jama_jabre_2018_oi_180004.pdf#page=7>), [PDF p. 8, protocol-violation discussion](<../jama_jabre_2018_oi_180004.pdf#page=8>), [PDF p. 9](<../jama_jabre_2018_oi_180004.pdf#page=9>) |
| REPORT complete-output inspection, supplementary contents/contributions | [joi180004supp2_prod.pdf — PDF p. 1](<../joi180004supp2_prod.pdf#page=1>), [PDF p. 2](<../joi180004supp2_prod.pdf#page=2>) |

**Source evidence:** SAP defines ITT by randomized group and AT by technique actually received. It expressly requires primary NI analysis in ITT/PP/AT, additional secondary analyses in PP/AT, and safety in ITT/AT. Report Table 2 identifies ITT and PP; the center model is post-hoc ITT. Safety is by actual treatment, including 14 ETI-assigned BMV recipients moved into BMV safety, giving full safety groups 1028/999 rather than randomized-group ITT 1018/1022. Report difficulty is 186/1027 versus 134/996, failure 69/1028 versus 21/996, and regurgitation 156/1027 versus 75/999. eTable 2 labels one-way BMV-before-ROSC reassignment ITT and reports 41/863 versus 45/1174, difference 0.9%, two-sided 95% CI [−0.9%, 2.7%], P=.31. Neither REPORT document identifies a complete AT NI counterpart or randomized-group ITT safety table.

**Reported-versus-comparator:** PLAN requires primary `{ITT, PP, AT}`, additional secondary `{PP, AT}`, and safety `{ITT, AT}` outputs. REPORT identifies ITT/PP efficacy, actual-treatment safety, center-adjusted ITT, and ITT-labeled sensitivity analyses. The one-direction sensitivity reassignment does not establish the complete SAP AT mapping or an AT NI result.

**Reasoning procedure:** Match explicitly required population-specific primary/key-secondary outputs to all named supplied results and definitions. Bound the absence statement to the nine article and three results-supplement pages. Preserve unsuccessful-intubation attribution and actual-treatment conventions. Do not equate a conventional two-sided sensitivity contrast with the explicitly planned AT NI analysis, or infer that unsupplied analyses were never performed.

**Calculation:** The BMV safety contribution list is 1014+14=1028; the explicit 14-person reassignment establishes membership distinct from randomized-group ITT. For integer 14, `[13.5,14.5)` admits only 14; rounding cannot remove the reassignment or supply a population-specific output. The available eTable 2 difference is 100×(41/863−45/1174)=0.91782 percentage points, within the 0.9% half-unit interval `[0.85,0.95)`. That effect display reconciles and is not this candidate's basis. No hypothetical AT denominator or ITT safety event count is reconstructed.

**Affected result or extracted value:** AT primary favorable-survival NI; AT day-28 survival, hospital-admission survival and ROSC; and randomized-group ITT airway difficulty, failure and regurgitation contrasts. These are primary or abstract-listed/key-secondary results, rather than peripheral exploratory outputs.

**Why context does not resolve it:** The report does not identify these additional outputs or expressly document their replacement. Its sensitivity analysis is labeled ITT and documents one direction of movement, without complete handling of dual-technique/rescue/post-ROSC recipients. Complete-report inspection, including the protocol-violation discussion, supplies no full mapping or corresponding AT NI result.

**Alternative source-grounded interpretations:** Required outputs may have been generated but not supplied; later decisions may have superseded them; or an abbreviated sensitivity result may embody some AT handling. The available labels and population definitions do not establish those explanations or complete equivalence to the planned outputs.

**Mechanical evidence recheck:** All registered SAP/native/scanned and REPORT locations were found and visually matched. All 12 REPORT pages were inspected for the bounded output comparison. Explicit population requirements, labels, reassignment and printed counts matched; logical and display-precision checks reproduced without revision. Necessary supplied inputs are available. Missing inputs are additional AT efficacy/NI outputs, randomized ITT safety outputs, crossover-specific events, complete AT handling of both techniques, and any superseding decision. Direct facts are requirements and identified outputs; nonperformance and implied equivalence remain unestablished. Remaining human question: where are the planned AT efficacy and ITT safety outputs, or what documented change and complete mapping identifies their supplied counterparts?

**Potential downstream evidence impact:** If confirmed, an extractor could lack a planned population-specific contrast or attach an available actual-treatment/sensitivity result to a distinct randomized or AT estimand. No realized reuse, alternative event count or trial-conclusion change is established.

**Human verification steps:** Compare SAP population/output sections with every named report table; locate additional outputs or a documented replacement; establish complete AT handling of dual-technique participants and the safety randomized-group mapping; verify endpoint, contrast, confidence level and NI label before assigning available estimates to planned populations.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Direct ETI crossover and safety membership accounting

**Status:** Pending Human Adjudication

**Candidate statement:** One BMV-assigned participant directly intubated without receiving BMV is absent from both explicitly enumerated safety contribution lists under the stated all-treated actual-treatment rule. The participant's overall safety membership remains unresolved.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article safety definition vs REPORT main article flow/safety tables

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Classification rationale:** The safety rule, treatment-flow branches and adverse-event denominators are all within one REPORT article. Focus A/C concerns count and membership logic, hence S_W/statistical_results. No PLAN document is an independently conflicting comparator, and no attribution-only domain is needed.

**Classification ambiguity:** None in document roles or relationship; the participant's eligibility and membership remain unresolved.

**Exact source locations:**

| Role/function | Actual source and exact location |
|---|---|
| REPORT membership rule | [jama_jabre_2018_oi_180004.pdf — PDF p. 3, Statistical Analysis safety definition](<../jama_jabre_2018_oi_180004.pdf#page=3>) |
| REPORT direct crossover | [jama_jabre_2018_oi_180004.pdf — PDF p. 4, Figure BMV treatment branch](<../jama_jabre_2018_oi_180004.pdf#page=4>) |
| REPORT enumerated BMV safety set | [jama_jabre_2018_oi_180004.pdf — PDF p. 4, Figure BMV safety box](<../jama_jabre_2018_oi_180004.pdf#page=4>) |
| REPORT ETI accounting/exclusions | [jama_jabre_2018_oi_180004.pdf — PDF p. 4, Figure ETI treatment and safety branches](<../jama_jabre_2018_oi_180004.pdf#page=4>) |
| REPORT full safety total | [jama_jabre_2018_oi_180004.pdf — PDF p. 4, safety-population narrative continuing in right column](<../jama_jabre_2018_oi_180004.pdf#page=4>) |
| REPORT affected safety denominators | [jama_jabre_2018_oi_180004.pdf — PDF p. 6, Table 3](<../jama_jabre_2018_oi_180004.pdf#page=6>) |
| REPORT eligibility context, not a resolved exclusion | [jama_jabre_2018_oi_180004.pdf — PDF p. 2, eligibility criteria](<../jama_jabre_2018_oi_180004.pdf#page=2>) |

**Source evidence:** Safety includes all treated patients by treatment actually received, with failed ETI attempts attributed to ETI. Of 1020 BMV-assigned participants, 1014 received BMV; six did not, including one directly intubated because massive regurgitation prevented BMV. The BMV safety box explicitly lists 1014 BMV-assigned recipients plus 14 ETI-assigned BMV recipients. ETI assignment is 1023: 979 received ETI, 21 had failed ETI attempts then BMV, 14 received BMV, and nine had no resuscitation. The ETI safety box excludes 14 BMV recipients, nine without resuscitation and one underage participant, leaving 999. The narrative gives total safety 2027, comprising 1028 BMV and 999 ETI. Table 3 reports ETI difficulty/failure denominators 996 and regurgitation 75/999, alongside BMV denominators 1027/1028.

**Reported-versus-comparator:** The printed 1028 and 999 contribution lists are exhausted by their stated members. The separately identified BMV-assigned direct ETI recipient is not among the 1014 BMV recipients and is additional to the ETI-assigned branch. Under the all-treated actual-treatment rule, membership requires either an ETI contribution or an additional stated exclusion.

**Reasoning procedure:** Trace the named participant through both complete safety boxes, preserving the stated attribution of failed attempts and distinguishing overall population membership from outcome-specific observation denominators. This is an analysis-population-size comparison, rather than a peripheral per-time-point contributor comparison. Do not infer event outcomes or reassign other rescue recipients.

**Calculation:** BMV safety=1014+14=1028. ETI-assigned safety=1023−14−9−1=999, equivalently 979+21−1=999. Printed total=1028+999=2027. The direct ETI recipient belongs to neither contribution list. Without a further exclusion, the stated rule implies one additional ETI contribution: 999+1=1000 and 1028+1000=2028. These are conditional rule implications, not selected replacement values. For integer count n, `[n−0.5,n+0.5)∩integers={n}`; no admissible count rounding removes the one-person membership gap.

**Affected result or extracted value:** ETI full safety-population size/membership and Table 3 denominator interpretation, including regurgitation 75/999. The individual event status and any numerator change are not established.

**Why context does not resolve it:** Neither exhausted safety box identifies this participant or an additional overall exclusion. Outcome-specific missingness at denominators 996/1027 and overlapping PP/rescue reasons do not establish placement in the full safety sets. Eligibility criteria mention suspected massive aspiration before resuscitation, but the direct-regurgitation branch does not identify this participant as excluded under that criterion.

**Alternative source-grounded interpretations:** An unstated eligibility exclusion could explain the totals, or the participant could be included through incompletely described contribution labels. These possibilities require participant-level membership/eligibility linkage; the figure does not identify an observed resolution.

**Mechanical evidence recheck:** Every cited rule, branch, contribution list, exclusion and denominator was located and visually matched. The calculation and integer display check reproduced without correction. Necessary allocation/treatment/safety inputs are supplied. Missing inputs are the direct recipient's eligibility, safety membership, any further exclusion, participant identity linkage, and airway events. Direct observations are the printed lists/rule; the additional ETI contribution follows conditionally without another exclusion. Remaining human question: was this directly intubated BMV-assigned participant included in ETI safety, and which membership or exclusion rule reconciles the printed 999 ETI and 2027 total?

**Potential downstream evidence impact:** If confirmed, an extractor could copy a safety denominator or population attribution without the membership reconciliation. No alternative adverse-event numerator, revised rate, direction change or realized downstream use is established.

**Human verification steps:** Trace the direct ETI recipient in the safety-analysis membership record; verify eligibility and any exclusion; reconcile both contribution lists and total with the stated actual-treatment rule; then establish whether any affected outcome denominator requires a distinct interpretation. Do not infer an event from the treatment-flow description alone.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Post-hoc reassignment population and success totals

**Status:** Pending Human Adjudication

**Candidate statement:** The stated ITT reassignment of 155 BMV participants to ETI does not account for three participants and one primary success absent from the displayed post-hoc cohort.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article ITT/reassignment specification vs REPORT results supplement post-hoc population

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Classification rationale:** The main REPORT supplies starting ITT counts and reassignment specification; a different REPORT supplies the resulting sensitivity fractions. The independent count-conservation comparison requires both documents, hence S_C/statistical_results, focus A/C. Main exclusion wording is resolved by consideration-in-ETI context and supplies no independent S_W conflict. There is no conflicting PLAN comparator.

**Classification ambiguity:** Additional exclusions, another starting set or a combined transfer/exclusion definition may explain the cohort, but no complete transformation is supplied. Document roles and S_C-only classification remain clear.

**Exact source locations:**

| Role/function | Actual source and exact location |
|---|---|
| REPORT ITT specification | [jama_jabre_2018_oi_180004.pdf — PDF p. 3, final Statistical Analysis paragraph, item 4](<../jama_jabre_2018_oi_180004.pdf#page=3>) |
| REPORT direction of movement | [jama_jabre_2018_oi_180004.pdf — PDF p. 4, post-hoc specification continuation](<../jama_jabre_2018_oi_180004.pdf#page=4>) |
| REPORT starting counts/successes | [jama_jabre_2018_oi_180004.pdf — PDF p. 4, Figure ITT boxes and Primary Outcome](<../jama_jabre_2018_oi_180004.pdf#page=4>) |
| REPORT 155-person movement | [jama_jabre_2018_oi_180004.pdf — PDF p. 6, lower-left post-hoc continuation](<../jama_jabre_2018_oi_180004.pdf#page=6>) |
| REPORT resulting population/successes | [joi180004supp2_prod.pdf — PDF p. 3, eTable 2 second analysis](<../joi180004supp2_prod.pdf#page=3>) |
| REPORT contextual protocol-violation statement | [jama_jabre_2018_oi_180004.pdf — PDF p. 8, discussion](<../jama_jabre_2018_oi_180004.pdf#page=8>) |

**Source evidence:** Main ITT is 1018 BMV and 1022 ETI, after original eligibility exclusions, with 44 and 43 primary favorable survivors. The named post-hoc ITT analysis considers in ETI the participants intubated after BMV and before ROSC; the main results specify n=155. eTable 2's second analysis repeats that consideration-in-ETI description under an ITT heading and displays 41/863 (4.8%) versus 45/1174 (3.8%), difference 0.9%, 95% CI [−0.9%, 2.7%], P=.31. The first eTable 2 analysis separately excludes ECMO/uncontrolled-donation patients and is not specified as this second analysis's starting set. The discussion mentions post-hoc protocol-violation removal without a complete three-person/one-success disposition.

**Reported-versus-comparator:** The main starting ITT and stated one-way reassignment imply conserved total participants and primary successes. The supplementary resulting cohort contains 2037 participants and 86 successes, compared with starting totals 2040 and 87. The available context clarifies movement into ETI but does not describe the additional loss.

**Reasoning procedure:** Match the same endpoint and ITT sensitivity specification across documents; apply participant and event conservation to pure reassignment; compare with pure exclusion as a separate logical alternative; check printed rate/difference precision independently. Do not infer participant identities, a corrected result, or an unreported inferential algorithm.

**Calculation:** Starting participants=1018+1022=2040; successes=44+43=87. Moving 155 gives BMV 1018−155=863 and ETI 1022+155=1177, preserving 2040. Printed denominators give 863+1174=2037, three fewer. Printed successes give 41+45=86, one fewer. The BMV success decrease 44−41=3 would, under pure transfer alone, imply ETI 43+3=46 rather than 45; this identifies no individual participant. Pure exclusion of 155 would give 2040−155=1885, also distinct from 2037. Integer half-unit intervals retain each exact participant/event count, so the gaps persist. Conversely, 41/863=4.750869% and 45/1174=3.833049% lie within their 4.8%/3.8% half-unit intervals. Their difference 0.9178197 percentage points lies in `[0.85,0.95)`, consistent with 0.9%; rounded rates and effect are not the candidate's basis.

**Affected result or extracted value:** The post-hoc favorable-survival cohort denominators 863/1174, successes 41/45, and population interpretation attached to the 0.9% contrast and interval.

**Why context does not resolve it:** Considering transferred participants in ETI resolves isolated exclusion wording but supplies no additional three-person/one-success disposition. Original eligibility exclusions already precede the 2040-person ITT start. The first sensitivity block and general protocol-violation discussion do not establish another starting population or a complete transformation for this second block.

**Alternative source-grounded interpretations:** Additional exclusions may accompany reassignment; the displayed counts may come from a different starting set; or 155 may combine transfers and exclusions. None is specified sufficiently to identify the cohort or actual participants and outcomes.

**Mechanical evidence recheck:** All specification continuations, starting counts, movement and resulting fractions were found and visually matched. Count/event conservation gaps reproduced; separate rate/difference rounding checks reconciled. No transcription or location revision was required. Necessary printed population, endpoint and movement inputs are supplied. Missing inputs are complete second-analysis inclusion/exclusion and reassignment rules, its actual starting set, participant/outcome linkage and whether 155 describes only transfers. Direct observations are the printed fractions and movement; additional exclusions and alternative starting sets are inferred explanations. Remaining human question: what complete transformation takes ITT 1018/1022 with 44/43 successes to 863/1174 with 41/45, accounting for the three-participant and one-success differences?

**Potential downstream evidence impact:** If confirmed, an extractor could attach the sensitivity effect to a differently defined cohort or copy population counts without their transformation. No replacement count, effect or trial conclusion is selected, and no realized downstream reuse is established.

**Human verification steps:** Establish the second sensitivity analysis's exact starting set; obtain the transfer/exclusion membership rule and success linkage; reconcile total participants and events across the transformation; verify that the printed fractions and effect correspond to that identified cohort before reuse.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Evidence reuse links an endpoint definition and analysis-population specification to numerator/denominator pairs, an effect estimate and uncertainty, then to a study record in a synthesis. A confirmed candidate could affect that linkage even where printed arithmetic or a rounded effect reconciles. C001 concerns the primary endpoint definition; C002 concerns identified population-specific outputs; C003 concerns safety membership; C004 concerns the sensitivity cohort transformation. Human review should preserve these distinctions and retain source locations with extracted values.

The package provides no evidence that any candidate has propagated to a synthesis, altered a guideline, changed a trial conclusion, or caused serious downstream harm. The considerations above describe potential extraction relevance only. No replacement result is supplied by this review.

## Limitations and Missing Definitions

There is no scientific source-page or registered-relationship coverage gap. The package supplies aggregate PDF reporting and prospective materials, without participant-level records, workbooks, CSVs or Office sources. Complete review therefore cannot resolve individual membership, event status or unsupplied analysis outputs.

Candidate-specific missing definitions are: the implemented endpoint indicator and baseline-to-day-28 neurological linkage (C001); additional AT efficacy/NI and randomized ITT safety outputs, complete dual-technique mapping, or a superseding decision (C002); the direct ETI recipient's eligibility, safety membership and adverse events (C003); and the complete post-hoc starting-set/transfer/exclusion/success transformation (C004).

Other bounded limitations are unnamed row-specific confidence-interval procedures, chi-square/Fisher selection and continuous-summary/test allocation; incomplete pause aggregation and center-random-effect model details; unavailable sample-size simulation code/seed; and numerical DSMB/futility boundaries, adaptation details and conditional-imputation implementation not fully supplied. The SAP's disclosed interim cancellation was respected. Diagnostic approximations do not establish contradictions where the applicable algorithm is unnamed.

Some reused OCR/render engine versions are unrecorded. Source-hash identity, native/layout equivalence, exact page locators and current direct-source candidate confirmations support their use as aids. Direct OCR and Office-conversion binaries were absent but were not needed; available CPU Poppler rendering closed the single reusable gap. The complete stage limitations are retained in [limitations.md](review_1_6_1/limitations.md). An absence of further candidates does not establish complete methodological adequacy.

## Human Adjudication Checklist

For each candidate, independently read every affected source location and verify the operative definitions, population, outcome, time point and comparison. Separate reproduced printed evidence from possible implementation explanations. Resolve the named missing inputs where available; preserve uncertainty when aggregate materials cannot resolve them. Decide validity, importance and action in the human fields, record initials and notes, and identify any evidence needed before extracting or revising a value. Leave unadjudicated cards Pending Human Adjudication. Inclusion-audit confirmation and evidence state are not human decisions.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The canonical record comprises the [ledger](review_1_6_1/candidate_ledger.md), [screening log](review_1_6_1/screening/inclusion_screen.md), [mechanical recheck](review_1_6_1/verification/evidence_recheck.md), [quality audit](review_1_6_1/quality/evidence_quality_audit.md), [main map](review_1_6_1/extraction/main_quantitative_evidence.md), [support map](review_1_6_1/extraction/support_quantitative_evidence.md), numeric/statistical inventories, and checker outputs. Stable ID sets are C001, C002, C003, C004 throughout ledger, recheck, audit and this report. All card classification fields copy the final ledger values.

### Source integrity and tooling

The audit independently checked all three direct-source and all 104 reused-artifact SHA-256 entries successfully. Final before/after hash comparison and mechanical report validation are coordinator completion steps. Integrity records are [source hashes before](review_1_6_1/source_hashes_before.sha256) and [reused-asset hashes before](review_1_6_1/reused_artifact_hashes_before.sha256). This report uses physical one-based source-PDF pages and truthful relative links.

[Routing preflight](review_1_6_1/routing_preflight.md) reports PASS, Coordinator inference PASS, execution mode INTERACTIVE_CLI, Provider CURRENT_SESSION, and ten named presets verified against fixed model/effort pairs. The [tooling record](review_1_6_1/tooling_record.md) records Linux; pdfinfo/pdftotext/pdftoppm/pdftocairo and Pandoc available; tesseract/libreoffice absent. Direct PDF tools use Poppler 25.03.0; Pandoc is 3.1.11.1; direct sha256sum supplies hashes. Fallback environment NOT_NEEDED; packages None; capabilities used None; environment removed NOT_CREATED. No global installation, GPU operation or external evidence was used.

### Agent execution

All 14 actual agents are recorded below, including the coordinator and two additional disjoint mapper/checker shards. Every specialist began as FRESH_SPAWN. Statistical passes have distinct runtime IDs; pass 2 emitted no new findings, so an additional pass-2 inclusion screener was not applicable. The [execution manifest](review_1_6_1/agent_execution_manifest.md) preserves their primary artifact paths.

| Stage | Actual runtime agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | 01a128db-a3c6-7261-9791-160147d8210f | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | 01a128e0-859a-7782-a0da-af74d73251b5 | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | 01a128e3-1e2a-7950-a6d7-1160d6b11d44 | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | 01a128e3-42f0-7731-8b6d-bc260f7e36ea | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper_final_shard | 01a128e3-668f-7150-ae14-6e0af41971ad | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | 01a128e7-cc36-7d53-98bd-05dedeb36905 | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer_support_shard | 01a128e7-f3a0-7770-a947-d62dbe760872 | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | 01a128e8-1808-73e3-9497-1d402cbb902e | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | 01a128e8-4022-7ff0-8a20-57d007b2fa27 | gpt-6.1-sol | high | FRESH_SPAWN |
| inclusion_screener | 01a128ef-16e2-7623-82e2-2df3868acfc6 | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | 01a128f3-ae65-7bf1-85c2-2809027f8172 | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | 01a128f7-8354-7f82-b8fd-4c65c1fbd3e2 | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | 01a128fb-ee7f-7593-b991-821cf04614d2 | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | 01a12903-6527-7393-b172-810de9923caf | gpt-6.1-sol | medium | FRESH_SPAWN |

### Reproducibility performance

The package-specific planning range does not limit coverage, relationships or candidates. Finish and observed performance values are finalized by the coordinator immediately after complete Markdown assembly; local HTML rendering and mechanical validation are outside the recorded review window.

- **Target basis:** Three PDF sources contain 146 physical pages, with 145 backed by reusable native/layout text or source-hash-matched OCR and one requiring fresh visual inspection. The 134-page plan bundle contains multiple protocols, amendments, SAP pages and scanned operational material; its 321567 layout characters require context-bounded support mapping. No Office conversion or fresh OCR is presently needed. Plan 35-55 minutes for disjoint mapping shards, concurrent numeric/cross-source/statistical checks, independent screening, recheck, a distinct second statistical pass, audit and complete report assembly; the target does not limit coverage or findings.
- **Total source units:** 146
- **Fresh-source units:** 1
- **Target elapsed minutes:** 35-55
- **Started UTC:** 2026-10-11T02:52:37Z
- **Finished UTC:** 2026-10-11T03:36:02Z
- **Observed elapsed minutes:** 43.4
- **Target status:** MET_TARGET
- **Exceedance causes:** None
