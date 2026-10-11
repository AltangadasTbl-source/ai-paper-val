# Numeric consistency checker: supplementary table shard

Assigned scope: DOC-002 REPORT joi190092supp1_prod.pdf, eTables4,5,6,8,9, PDF pages10,11,12,14,15,16. The assigned scope includes every printed table row and its count/percentage/denominator relation. eTable7 at PDF p13 and all matched counts outside these tables belong to the main numeric checker. Source location links below are relative to this part artifact.

Required QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md were read completely. Tooling record reports direct Poppler tools available. Source-native authority used: Poppler26.01.0 pdftotext layout streamed directly from joi190092supp1_prod.pdf for PDF pages10–16. Relevant support extraction supplied locators, without importing checker conclusions. No old candidate or report artifact, external evidence, or extra Python was used.

## Complete scope and rules

All93 assigned rows,186 group-specific count/percentage cells,5 population-header relations and3 any-event union relations were checked. Complete provisional mapping is relationships/parts/numeric_supplement_inventory.md (NS001–NS101); the main numeric checker assigns global N identifiers losslessly.

Every count is an integer number of patients reporting at least one event. The percentage calculation is100n/D. One-decimal percentages retain half-unit display intervals, ±0.05 percentage point. Count and denominator half-unit intervals are intersected with the integer patient-count scale, leaving the printed integer. All counts satisfy0≤n≤D. The percentages are proportions of patients, not event rates, risk ratios or other between-arm effect measures. Tables supply no modeled estimate to compare with crude percentages.

The91 ordinary row relationships reconcile within one-decimal percentage intervals in both arms. Two row-level percentage observations are addressed below. The first three tables use107 MTX recipients and108 MMF recipients; their common footnote accounts for one randomized MMF patient who did not receive medication. eTable8 uses the continuation-after-success cohort62/56; eTable9 uses the switching cohort29/20. These interval-specific cohorts were not compared with randomized baseline denominators.

The any-event rows are compatible with person-level unions, with repeated category membership allowed:
- eTable4: category sums49/46, category maxima9/19, any-event30/33, population107/108.
- eTable5: category sums47/34, category maxima12/9, any-event22/19, population107/108.
- eTable6: category sums 168/131, category maxima 16/17, any-event 59/55, population 107/108.

In each arm and table, maximum category count≤any-event count≤min(population,category sum). No individual-level overlap data are supplied, so exact union arithmetic cannot be reconstructed. That is not a source contradiction.

## Findings

None. No F-NUM identifier assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [DOC-002 PDF p10](../../../../joi190092supp1_prod.pdf#page=10), eTable4, REPORT, MMF eye-floaters cell; NS004 | Printed5 (4.7), header N=108.100×5/108=4.6296296%, outside displayed4.7 interval[4.65,4.75); the expected one-decimal percentage is4.6. Both n=5 and N=108 are explicit, and neighboring MMF cells of5 are reported4.6 in the immediately adjacent tables. This isolated percentage display is resolved at once from the count and denominator, leaving the patient proportion identifiable. | CONTEXT_RESOLVES |
| [DOC-002 PDF p15](../../../../joi190092supp1_prod.pdf#page=15), eTable9, REPORT, serious systemic diarrhea MMF cell and MMF header; [p16](../../../../joi190092supp1_prod.pdf#page=16) footnote; NS092 | Printed1 (3.4), header N=20.100×1/20=5.0%, outside displayed3.4 interval[3.35,3.45). The same table reports MMF1 (5.0) for low hemoglobin, allergy and fever; MTX N=29 with1 (3.4) is printed throughout. The displayed count and header identify1/20 at once. Footnote merely names diarrhea/fatigue as drug-related serious events and gives no separate denominator. This isolated percentage display does not obscure the count or intended denominator. | CONTEXT_RESOLVES |
| [DOC-002 PDF p10](../../../../joi190092supp1_prod.pdf#page=10), [p11](../../../../joi190092supp1_prod.pdf#page=11), [p12](../../../../joi190092supp1_prod.pdf#page=12), REPORT, any-event rows versus categories; NS099–NS101 | Any-event count is not the sum of patient counts in individual categories. Patients may report more than one category; the table explicitly counts patients with at least one event and union bounds hold. | CONTEXT_RESOLVES |

## Limitations and handoff

No scientific coverage gap within the assigned scope. Patient overlap data are unavailable for exact any-event union reconstruction; displayed union bounds were fully checked. No inference was made about omitted adverse-event rows, unreported category exclusivity or unreported denominators.

Counts:101 provisional numeric relationships;93 table rows;186 count/percentage cells;0 findings;3 excluded-observation rows. Every assigned source page is covered; p16 supplies the eTable9 footnote. This checker emits no candidate ID, adjudication or proposed correction.

