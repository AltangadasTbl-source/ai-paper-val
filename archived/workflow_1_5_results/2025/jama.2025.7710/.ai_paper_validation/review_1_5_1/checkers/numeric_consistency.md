# Numeric-Consistency Review

## Scope and approach

This independent numeric lane reviewed every canonical relationship N001--N080 in `relationships/numeric_relationship_inventory.md`, against the exact supplied PDFs: DOC-001 `jama_kumar_2025_oi_250034_1750956984.08518.pdf` (pp. 1--11), DOC-002 `joi250034supp1_prod_1750956984.09018.pdf` (pp. 1--26), DOC-003 `joi250034supp2_prod_1750956984.11521.pdf` (pp. 1--29), and DOC-004 `joi250034supp3_prod_1750956984.12018.pdf` (pp. 1--6). I also used the current extraction maps and the two mapper relationship shards as locators, but direct PDF text/table inspection is the authority for the checks below. No web source, historical candidate/report conclusion, or external evidence was used.

Unless otherwise stated, percentage tolerance is ordinary one-decimal display rounding: a printed percentage is compatible when its absolute difference from `100*n/N` is at most 0.05 percentage points after allowing the source's displayed decimal precision. Count/addition identities require equality. A listed denominator is respected where the table explicitly distinguishes a nonmissing, infant, maternal, safety, or treatment-received population. An apparent cross-table difference is not a candidate if those printed populations explain it.

## Relationship-by-relationship results

| Stable ID(s) | Exact direct source location(s) | Independent checks and outcome |
|---|---|---|
| N001--N008 | DOC-001 pp. 1--4; DOC-001 p. 3 | **No numeric inconsistency found.** Randomised allocations reconcile: `1626 + 1631 = 3257`; infants reconcile: `1634 + 1641 = 3275`. Figure 1 flow is internally consistent (see N003--N006). The 50-mg every-8-h maximum-three-dose regimen equals a maximum 150 mg. The named primary components are ten distinct displayed endpoints; this main-paper label is internally coherent. |
| N003 | DOC-001 p. 4, Figure 1 | **No inconsistency.** `3748 - 491 = 3257` randomized. Exclusion-reason missingness is expressly disclosed. |
| N004 | DOC-001 p. 4, Figure 1 | **No inconsistency.** Sildenafil flow: `1552 + 74 = 1626`; nonreceipt reasons sum `16+11+4+2+2+39=74`. |
| N005 | DOC-001 p. 4, Figure 1 | **No inconsistency.** Placebo flow: `1555 + 76 = 1631`; reasons sum `14+10+6+2+44=76`; `1627 - 2 = 1625` primary-outcome infants. |
| N006 | DOC-001 p. 4, Results and Figure 1 | **No inconsistency.** Complete/future withdrawal entries are `4+2+1+2=9`; `3257-9=3248` women and `1625+1625=3250` infants with primary outcome. The infant-versus-woman denominators are explicitly different analysis units. |
| N009 | DOC-001 p. 5, Table 1 | **No inconsistency.** Group labels are 1626 and 1631; means/SDs and weeks carry the printed units. |
| N010 | DOC-001 p. 5, Table 1; DOC-001 p. 4, Results | **No inconsistency.** Each ethnicity percentage is compatible with its printed nonmissing denominator (1624/1629). Categories sum to `1624` and `1629`. Narrative 874/1631 = 53.59% (53.6%) while Table 1 874/1629 = 53.65% (53.7%): the stated randomised versus nonmissing denominators fully explain the display difference. |
| N011--N016 | DOC-001 p. 5, Table 1 | **No inconsistency.** Smoking and all single-row percentages round to their labelled denominators. Parity sums `944+446+152+82=1624` and `966+450+153+61=1630`; preceding-birth mode sums 680 and 664; conception sums 1624 and 1630. Hypertension/diabetes rows are condition categories, not asserted mutually exclusive totals. |
| N017 | DOC-001 p. 5, Table 1; DOC-001 p. 4, Figure 1 | **No inconsistency; resolved cross-table population difference.** Dose rows sum `902+558+94=1554` and `914+549+92=1555`. The placebo-arm total equals 1555 women receiving assigned placebo. In the sildenafil-randomised arm, Figure 1 shows 1552 received sildenafil as randomised and 2 received placebo by mistake; `1552+2=1554`, explaining the two-count difference from the treatment-as-randomised figure. Percentages use randomised-arm denominators and are compatible by rounding. |
| N018 | DOC-001 p. 5, Table 1 | **No inconsistency.** Hospital counts sum `880+476+164+106=1626` and `883+476+166+106=1631`; all printed percentages round correctly. |
| N019--N020 | DOC-001 p. 6, Table 2 | **No inconsistency.** Infant sex sums `833+796=1629`, `840+797=1637`; birth-mode sums `864+466+209+86+4=1629`, `931+412+204+88+2=1637`. Percentages and infant-level units match the printed denominators. |
| N021--N025 | DOC-001 p. 6, Table 2 | **No inconsistency.** Onset-of-labor identities are `1353+268=1621` and `1348+279=1627`; analgesia sums 1621/1625. Induction-method rows are not labelled mutually exclusive and were not summed. All count/denominator percentages, including PPH and ICU rows, conform to rounding tolerance and their explicitly different missing-data denominators. |
| N026 | DOC-001 pp. 1, 6--8, Table 3/Figure 2 | **No inconsistency.** `83/1625=5.108%` -> 5.1%; `84/1625=5.169%` -> 5.2%; direct difference `5.108-5.169=-0.062` percentage points -> -0.1. Figure-2 subgroup event totals also recover 83 and 84. |
| N027--N030 | DOC-001 pp. 4, 6--7, Table 3 | **No inconsistency.** All secondary counts/denominators produce the printed one-decimal percentages and signed absolute differences within rounding tolerance. Cord-pH partition: sildenafil `1223 tested + 401 not done + 5 missing = 1629`; placebo `1159 + 474 + 4 = 1637`. “Not done assumed no event” is a disclosed primary-analysis rule, not a numerical contradiction. |
| N031 | DOC-001 p. 7, Results; DOC-004 p. 3, eTable 2 | **No inconsistency.** Site primary counts/denominators combine to main primary totals: `16+67=83`, `24+60=84`, and `883+742=1625`, `887+738=1625`. Mater PPH counts agree with DOC-004 and Table 2; the distinct denominators reflect outcome availability. |
| N032--N035 | DOC-001 p. 8, Table 4 | **No inconsistency.** Infant mode decompositions reconcile: `142+201=343`, `129+178=307`; `291+94=385`, `257+114=371`; and fetal-distress-factor totals `233+238=471`, `201+230=431`. All displayed risks/differences conform to printed denominators and one-decimal rounding. Maternal PPH, hysterectomy, rupture, ICU, mortality denominators retain disclosed missingness. |
| N036--N038 | DOC-001 p. 8, Figure 2 | **No inconsistency.** Within every binary subgroup, denominators sum to 1625 on each arm and event counts sum to 83/84: e.g., SGA `10+73=83`, `13+71=84`; multiple pregnancy `2+81=83`, `7+77=84`; and all remaining subgroup pairs obey the same identity. Percentages round correctly. |
| N039--N043 | DOC-001 pp. 2--4, 9 | **No numeric inconsistency found.** Historical phase-2 `18.0/36.7=0.490` supports RR 0.49 and a 51% relative reduction after rounding. Planning 7.0% to 4.6% is a 34.3% reduction (displayed as planned 35%; protocol/SAP give 4.55%). Site recruitment `1763/3257=54.13%` -> 54.1%; discussion values reproduce the source tables. |
| N044--N047 | DOC-002 pp. 5--10 | **No numeric inconsistency found.** Regimen, ten-component target, planning 7.0% to 4.55%, phase-2 ratios, and component-rate context are consistently labelled as design/historical values, not phase-3 observations. The component-rate total is explicitly overlap-corrected, so component percentages were not inappropriately summed. |
| N048--N051 | DOC-002 pp. 10--14 | **No numeric inconsistency found.** Population, dose, subset, and timepoint statements are planning definitions and have no conflicting observed denominator or unit. |
| N052 | DOC-002 pp. 15--16 | **Candidate proposal NC-P02 below.** The primary-composite explanatory count does not reconcile with the displayed component list. |
| N053 | DOC-002 p. 16 | **No numeric inconsistency found.** Secondary/tertiary definitions and subgroup thresholds use stated units and do not assert incompatible denominators or totals. |
| N054 | DOC-002 pp. 16--17 | **Candidate proposal NC-P01 below.** The two price-year labels state incompatible numerical labels for the same described economic evaluation. |
| N055 | DOC-002 p. 17 | **No numeric inconsistency found.** Follow-up and model horizons are distinct declared planning horizons (2--3 years corrected age, one-year model, five-year budget impact). |
| N056 | DOC-002 p. 21 | **No numeric inconsistency found.** The 50% interim timing and thresholds are clearly protocol planning values. DOC-003 repeats the threshold framework; no result is mislabeled as a protocol threshold. |
| N057--N062 | DOC-003 pp. 5--14 | **No numeric inconsistency found.** SAP design values repeat the protocol target (3200, 7% to 4.55%, 35%, alpha .05, >80%; secondary >90%) and distinguish mITT, safety treatment-received, infant sibling clustering, and cord-pH missing-data rules. These labels explain, rather than contradict, observed-result denominators. |
| N063--N065 | DOC-003 pp. 15--29 | **No numeric inconsistency found.** All table bodies inspected are blank shells (`N =`, `xxx`, or equivalent). They were not treated as results and create no arithmetic claim to test. |
| N066--N071 | DOC-004 p. 2, eTable 1 | **No numeric inconsistency found.** For each sensitivity row, yes/no/missing partitions reconcile: 10-component imputed `85+1540=1625`, `87+1538=1625`; 9-component `75+1550=1625`, `80+1545=1625`; GLM `83+1542=1625`, `84+1541=1625`. Cord-pH rows reconcile: `14+1211+404+5=1629`, `8+1154+475+4=1637`. Percentages and model labels respect their printed analysis rules. |
| N072--N078 | DOC-004 pp. 3--5, eTable 2 | **No numeric inconsistency found.** Across site strata, every directly additive outcome recovers the corresponding main-table count and its outcome-specific denominator: primary 83/84 and 1625/1625; Apgar 5/3 and 1629/1637; pH 12/5 and 1629/1637; unit admission 50/61; respiratory support 37/47; PPHN 1/3; meconium aspiration 9/5; fetal-distress operative birth 343/307; PPH 164/128. Percentages are compatible with the displayed denominators. Site-specific denominators vary by endpoint, as in the main tables; this is disclosed outcome availability, not a population mismatch. |
| N079--N080 | DOC-004 p. 6, eTable 3 | **No numeric inconsistency found.** Safety denominators reconcile exactly: `1552+1557=3109` and `3257-148=3109`. For all 14 side-effect rows, Yes + No equals each treatment-received denominator and percentages round correctly. Zero counts and displayed P=.999 are coherent finite-precision Fisher-exact displays, not candidates. |

## Rechecked mapper proposals and distinct candidate proposals

### NC-P01 — inconsistent price-year label for the planned economic evaluation

- **Direct observation:** DOC-002 p. 16, section 7.2.3, says “All costs will be presented in 2024/25 dollars, with no discounting applied.” DOC-002 p. 17, section 8.2, describes the same payer-perspective, one-year modelled cost-utility analysis and five-year budget-impact analysis, but says “All costs will be presented in 2023/24 dollars, with no discounting applied.”
- **Rule and reproducible check:** for one declared analysis, compare its printed price-year label. Required identity: stated price year A = stated price year B. Direct text comparison gives `2024/25 != 2023/24`; no rounding or unit conversion applies (tolerance 0 years).
- **Observation versus inference:** Direct observation is the two conflicting labels. The inference is limited to a reporting/planning inconsistency; this review does not infer which year was applied, whether an economic analysis was executed, or any impact on trial results.
- **Alternatives considered:** The sections could have been intended to describe separately updated versions of an analysis; neither section states that distinction. Their matching payer perspective and one-/five-year horizons make a same-analysis reading reasonable.
- **Quality-control relevance:** A price year determines the monetary scale of cost and cost-effectiveness quantities and can propagate to economic evidence synthesis.
- **Exact human question:** Which financial year was prespecified and used for the cost-utility and budget-impact analysis, and should one of these two protocol labels be corrected or qualified?

### NC-P02 — primary-composite explanatory count does not reconcile with the displayed list

- **Direct observation:** DOC-002 p. 15 displays ten bulleted primary-composite endpoints, numbered 7.1.1 through 7.1.10 across pp. 15--16. DOC-002 p. 16, section 7.2.1, says “There are ten items because outcomes (i) and (viii) each contain two individual components.”
- **Rule and reproducible check:** count the displayed endpoint bullets: `10`. If two of those ten outcomes each contain two separately counted components, the stated counting rationale adds two components to the ten displayed items (`10 + 1 + 1 = 12`), not ten. Conversely, treating the ten bullets as the ten items leaves no need for the stated two-outcome expansion. Tolerance is 0 components.
- **Observation versus inference:** The bullet count and explanatory sentence are direct text observations. The inference is confined to an internal definition/counting ambiguity; no conclusion is made about actual event coding or the trial result.
- **Alternatives considered:** “Outcome (i)” may be a drafting reference to a different, unstated grouping, and “Special Care or Intensive Care” may have been intended as two settings within one endpoint. Neither alternative makes the printed arithmetic rationale unambiguous, especially because intrapartum stillbirth and 28-day neonatal death are separately displayed.
- **Quality-control relevance:** The primary composite's component definition controls outcome interpretation, component tabulation, and comparability in downstream evidence products.
- **Exact human question:** What are the authoritative ten components of the primary composite, and which (if any) two listed outcomes were intended to contain separately counted components?

## Non-candidate diagnostics

- Mapper proposal MP-MN01 is resolved by printed nonmissing versus randomised denominators, as documented under N010.
- Dose-count difference in N017 is resolved by the two sildenafil-randomised women who received placebo by mistake; it is not a numerator/denominator discrepancy.
- Neither DOC-004 P=.999 rows nor any coherent displayed zero count/P value is a candidate.

## Result

- Canonical relationship coverage: **80 of 80** (N001--N080).
- Distinct document-grounded candidate proposals: **2** (NC-P01, NC-P02); no stable C IDs, severity, validity label, or disposition assigned.
- Limitation: This lane assessed reporting arithmetic, labels, populations, denominators, units, and direct cross-document relationships. It did not audit raw data, reproduce fitted models, or adjudicate which conflicting protocol wording is correct.
