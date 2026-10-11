# Independent inclusion screen — statistical pass 2

Runtime agent ID: `01a1297a-84be-7ae2-8e92-e70e71758da0`. Runtime task: `/root/inclusion_screen_pass_2`. Model: `gpt-6.1-sol`; reasoning effort: `high`; start mode: `FRESH_SPAWN`. This screener is distinct from the initial screener and all statistical checkers. Exact assigned scope: F-ST2-101 in `checkers/parts/statistical_pass_2_protocol.md`; one finding screened independently. QUALITY_CONTROL_SCOPE.md and the complete inclusion-screen section of the 1.6.2 review contract were read. This artifact supplies the row and notes for coordinator merging; it does not edit the canonical screening table or assign a candidate ID.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-ST2-101 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C010 |

**F-ST2-101:** Route A, category 5 qualifies because the directly confirmed final protocol includes AST/ALT exactly 5×ULN and leukocytes exactly 1,000/µL in immediate serious laboratory failure, while the repeated report definitions use strict >5×ULN and <1,000/µL cutoffs with a separate persistence branch, and both documents explicitly make serious laboratory failure a component of the six-month primary treatment-success outcome.

## Independent source reproduction

All page numbers below are physical supplied PDF pages. PLAN roles are assigned by prospective protocol/manual content; the article and non-plan results supplement are REPORT content.

- PLAN final protocol [p.80, §2.5.1](../../../../joi190092supp2_prod.pdf#page=80): six-month treatment success requires the stated ocular/steroid criteria without treatment failure at any point due to safety, tolerability or futility. This is explicitly under “Definitions for primary endpoint.” The corticosteroid-injection component is separately registered in the current ledger and is not re-emitted here.
- PLAN final protocol [p.81, §2.5.2 and Table 3](../../../../joi190092supp2_prod.pdf#page=81): AST/ALT nonserious interval is 2 to <5 times ULN; the serious interval is ≥5 times ULN. Leukocytes are nonserious at >1,000 to <2,500/µL and serious at ≤1,000/µL. Persisting nonserious abnormalities at 28 days are also classified serious, with treatment failure declared immediately. Thus persistence is an additional route into serious failure rather than a requirement for the immediate serious threshold.
- PLAN final protocol [p.136, opening paragraph and §6.2](../../../../joi190092supp2_prod.pdf#page=136): laboratory abnormalities meeting the serious threshold lead to immediate medication stopping and declaration of treatment failure; patients with laboratory serious events do not switch to Phase II. The serious-event list independently repeats ≥5 times ULN AST or ALT.
- REPORT main [p.3, Outcomes](../../../../jama_rathinam_2019_oi_190092.pdf#page=3): the primary treatment-success composite includes no declaration of treatment failure for safety or intolerability; an abnormal laboratory result meeting the serious adverse-event threshold is the printed safety-failure example. The primary-outcome link is explicit.
- REPORT main [p.6, Table 2 and safety-failure footnote](../../../../jama_rathinam_2019_oi_190092.pdf#page=6): success is 64/96 versus 56/98; safety is the reason for 3/32 versus 2/42 treatment failures. The footnote defines safety failure by an abnormal laboratory result meeting the serious adverse-event threshold. The native extraction's footnote-letter placement is not used to infer any separate reporting issue; the full printed footnote text supplies the relationship.
- REPORT main [p.7, Adverse Events](../../../../jama_rathinam_2019_oi_190092.pdf#page=7): five serious events through the primary outcome were deemed drug related, three in methotrexate and two in mycophenolate; all were elevated liver-function tests. This corroborates the safety-failure result being interpreted but does not supply individual values or durations.
- REPORT main [p.8, Table 3 laboratory rows and definition pointer](../../../../jama_rathinam_2019_oi_190092.pdf#page=8): nonserious AST/ALT is 2 to 5 times ULN lasting <28 days; serious AST/ALT is >5 times ULN or 2 to 5 times ULN for ≥28 days. The serious row prints three versus two patients. The table directs readers to eTable 1 for definitions and states all drug-related serious events were due to elevated AST/ALT.
- REPORT results supplement [p.5, eTable 1](../../../../joi190092supp1_prod.pdf#page=5): independently repeats AST/ALT serious >5 times ULN or 2 to 5 times ULN for at least 28 days; nonserious 2 to 5 times ULN for less than 28 days. Leukocytes are serious <1,000/µL or <2,500/µL for at least 28 days; the nonserious range is >1,000 and <2,500/µL for less than 28 days.

### Exact-boundary logical check

For AST/ALT exactly 5 times ULN with duration shorter than 28 days, the final PLAN's ≥5 serious branch includes the observation immediately. In the REPORT, >5 does not include it, while the 2-to-5 branch requires at least 28 days before serious classification. For leukocytes exactly 1,000/µL with duration shorter than 28 days, the final PLAN's ≤1,000 immediate-serious branch includes it, whereas the REPORT's <1,000 serious branch does not. The REPORT's nonserious >1,000 branch also leaves that exact boundary unnamed; its prolonged-abnormality serious branch can include the boundary only when the duration requirement is met.

The reproduced comparison is between two printed decision rules, without assuming that any actual participant had either exact-boundary observation. It does not reconstruct the observed primary counts or assert a changed clinical outcome, effect, P value, significance or direction.

### Original/final versions and disclosed revisions

The [original protocol physical p.16, Table 3](../../../../joi190092supp2_prod.pdf#page=16), directly reread with native extraction, specifies AST/ALT >5 times ULN as serious, 2 to 5 times ULN as nonserious, and a serious leukocyte immediate cutoff of ≤999/µL. This supplies a plausible historical source for the report's strict boundaries; it does not make the final definition identical to the report definition. No additional PLAN-only discrepancy is emitted for legitimate historical changes.

The [revision history p.148, version 2.2 of May 1, 2013](../../../../joi190092supp2_prod.pdf#page=148) explicitly notes modified wording of nonserious/serious laboratory thresholds without reproducing a full threshold table. The [revision history p.153, version 4.4 of February 26, 2016](../../../../joi190092supp2_prod.pdf#page=153) explicitly adds the 28-day persistent nonserious abnormality rule; version 4.5 describes randomization and Phase II eligibility changes. All supplied revision-history pp.148–153 were reread. They explain the presence of versions and the persistence addition, but do not identify the report's strict cutoffs as the final primary classification algorithm or disclose a later replacement for final pp.81/136.

## Inclusion-threshold decision

**Comparison tier:** This is a planned-versus-reported primary endpoint threshold/composite comparison. The concern is not a peripheral comparison of generic safety displays: the supplied text connects the serious laboratory threshold directly to primary treatment failure in both PLAN and REPORT.

**Route A:** Category 5 applies because the safety-failure component of the prespecified primary success composite has different printed exact-boundary membership. Under the normative threshold, a reproduced category-5 finding is included independently of the general Route B criteria. The planned-versus-reported definition is observable even though individual implementation is unavailable.

**Display precision:** Not applicable to this logical decision-rule comparison. Both sources print the same cutoff numerals, and the observation concerns inclusive versus exclusive membership at a fixed boundary, not a discrepancy between rounded measurements or effect estimates. There is no recomputed percentage interval or relative discrepancy to report, and no rounded laboratory observation is assumed.

**Why notation or wording does not remove this finding:** The repeated report's pairing of 2-to-5 with >5 and its separate 28-day requirement supports a coherent strict-boundary reading for AST/ALT. The final protocol's 2-to-<5 with ≥5 supports a different coherent inclusive-boundary reading. The final protocol repeats ≥5 elsewhere, and the report repeats >5 in two displays; immediate context does not identify one as the intended common rule. A missing glyph may be a possible production explanation, but the evidence does not establish an obvious symbol substitution whose reading can be resolved at once. The explicit primary-composite link gives the threshold difference the interpretation consequence required by scope. No isolated symbol slip is registered apart from the endpoint rule.

**Named affected result:** The complete six-month treatment-success/failure definition supporting 64/96 versus 56/98 and the three versus two reported safety failures. The finding concerns which exact-boundary observations qualify as immediate safety failure; it does not imply that these totals change.

**Consolidation:** AST/ALT and leukocyte boundaries form one repeated final-plan/report laboratory-threshold pattern with every affected location retained. This is distinct from C002's omitted late-injection component, C003's missing robustness outputs and the other current issue patterns because those apply different rules and have different potential explanations. No duplicate-of-included consolidation is required.

**Classification proposed for registration:** Review domain `protocol_report`; primary relationship `P_R`; all relationships `P_R`; compared roles `PLAN final protocol vs REPORT main article and results supplement`. The two REPORT locations corroborate the strict-cutoff side rather than conflict with each other; original/final historical versions provide context and do not create a separately registered `P_P` relationship. Final mechanical evidence-state assignment and stable candidate ID remain coordinator/rechecker work.

## Alternatives, missing inputs and human question

The report may abbreviate an implemented inclusive cutoff, describe a historical cutoff despite use of the final protocol, or reflect another actual threshold algorithm. Any unsupplied amendment or adjudication instruction remains possible. Individual AST/ALT values, laboratory-specific ULNs, leukocyte values, durations, event linkage and the implemented primary-failure algorithm are not supplied. A measured exact boundary is not inferred; even whether any participant could be affected remains unknown.

Human question: Which inclusive/exclusive AST/ALT and leukocyte cutoffs generated primary safety-failure classification, how was the 28-day persistence branch applied, and did any primary safety classification depend on an exact-boundary observation?

## Methods, provenance and completed scope

All cited text-bearing REPORT pages and original/revision PLAN pages were read directly using CPU Poppler `pdftotext -layout` 26.01.0 to standard output. Source-linked images were visually inspected in full for final protocol pp.80,81,136, whose raster content is decisive: current `preprocessing/evidence_recheck/protocol_p080.png` (recorded CPU Poppler derivative) and reusable `.ai_paper_validation/review_1_6_1/preprocessing/protocol_b/page-81.png` / `protocol_c/page-136.png` (legacy engine versions unrecorded). Images act as supplied-source visual transcription aids; source PDFs remain authority. No new rendering, OCR or derivative was required; no source, reused asset, canonical screening log or ledger was modified. No external evidence or earlier AI conclusions was used.

Completed: one assigned finding; one INCLUDE decision; one distinct included issue; zero screened-out findings; every screened-out reason-code count zero. All assigned source locations were independently checked. The only limitations are the unavailable individual values/durations and implemented classification rules identified above. No severity, disposition, preferred analysis, final correction or adjudication is assigned.
