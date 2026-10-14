# Independent inclusion screen — initial stage

The fresh inclusion screener read QUALITY_CONTROL_SCOPE.md and the complete Workflow 1.6.2 review contract, then independently reread the exact supplied source pages for both initial findings. Scope: numeric_consistency_reviewer, no findings; cross_source_consistency_reviewer, F-XS-001; statistics_pass_1, F-ST1-001. The 24 checker exclusions remain separate observations for statistical pass 2 and the audit; they do not receive finding rows here. No old AI conclusions, external sources or count target were used.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | — |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |

**F-XS-001 justification:** The SAP explicitly reserves the nature/details of future exploratory clinical analyses for a later stage and permits additional non-prespecified exploratory analyses, while the report describes log-rank estimation and prints no clinical-event hypothesis-test result or claim that these rate-ratio analyses were prespecified, so an analysis conflict is conditional on an unsupported exclusivity/testing assumption or an unreported provenance detail and satisfies neither Route A nor all Route B criteria.

**F-ST1-001 justification:** Route A, category 4 applies because the visually confirmed 34% power in protocol Table 4, age <75 / total 5000 / two-sided .01, remains separated from a full conservative printed-input precision enclosure of 27.225032–29.972784% by a relative gap of 0.103742 under a continuity-corrected two-proportion reconstruction that satisfies the scope precision rule for all other 23 same-display power cells.

## Independent source facts for F-XS-001

Content-based roles: the SAP is PLAN; the main article is REPORT. This is an eligible analysis-specification comparison, rather than a peripheral comparison. The proposed P_R / protocol_report relationship would be applicable if a conflicting specification were reproduced.

Exact supplied locations reread visually:

- [SAP p. 20, §6.4.4](../../../joi250068supp2_prod_1760999665.29862.pdf#page=20): future long-term clinical analyses will report numbers and proportions of hospitalisations, ischemic stroke, major bleeding and all-cause/cardiovascular death, with no hypothesis testing; the following paragraph expressly reserves the nature of the analyses and outcome identification for later specification.
- [SAP p. 5, §2](../../../joi250068supp2_prod_1760999665.29862.pdf#page=5): subsequent additional non-prespecified exploratory analyses are not bound by the described strategy; SAP deviations will be described and justified in the final report.
- [SAP p. 21, §6.6](../../../joi250068supp2_prod_1760999665.29862.pdf#page=21): additional analyses may be performed and will be identified as exploratory and non-prespecified.
- [Main article p. 3, Outcomes and Statistical Analysis](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=3): stroke/death are exploratory; time to first stroke/death uses log-rank methods; no clinical-event null-hypothesis result or clinical-event-specific claim of prespecification appears.
- [Main article p. 7, Figure 4B and caption](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7): 2.5-year death/stroke event counts and proportions, rate ratios from time-to-event analyses and 95% CIs are printed; clinical-event P values or significance conclusions are absent.
- [Main article p. 1, abstract](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1) and [p. 5, Results](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5): any-stroke 69 versus 64 and RR 1.08 are reported without a hypothesis-test claim; the abstract's explicit prespecified-subgroup phrase refers to the primary AF analysis, not stroke/death rate ratios.

The source facts do establish an extension from counts/proportions to comparative time-to-event estimates, but the SAP does not say that counts/proportions exhaust all permissible estimation, and it expressly leaves the nature of these analyses for later definition. A log-rank estimate and interval do not by themselves establish that a prohibited clinical-event hypothesis test was performed. The report is explicit about the method that generated the extracted ratios; unresolved timing/provenance of its exploratory extension alone supplies no contradictory printed prespecification statement.

Route A category 5 does not apply: no clinical-event status/composite change, clinical-event analysis claimed prespecified but absent from plan, or replacement/omission of a planned primary/key secondary analysis is reproduced. Route A category 1 does not apply: there is no clinical-event P value, test conclusion or point-estimate/interval conflict. For Route B, the comparison is in focus (B1), but the proposed issue depends on a missing provenance detail or an assumed prohibition of estimation, rather than a conflicting supplied definition that prevents interpretation/extraction (B2/B3). Display precision is not applicable to this logical decision.

## Independent reproduction for F-ST1-001

Content-based roles: all compared and affected table specifications are PLAN. The proposed review domain is plan_material, primary/all relationship P_P. The single affected location is [protocol p. 22, Table 4, age <75 row, total 5000 / 2p<.01 column](../../../joi250068supp1_prod_1760999665.28862.pdf#page=22). Every same-display comparator cell is also on p. 22; [protocol p. 20, Table 2](../../../joi250068supp1_prod_1760999665.28862.pdf#page=20), which explicitly labels continuity-corrected sample sizes, and [p. 21, Table 3](../../../joi250068supp1_prod_1760999665.28862.pdf#page=21) supply contextual design support rather than additional conflicting locations.

Direct source reading confirms population 25%, patch AF 2.52%, total active AF 2.96%, active/control ratio 2.5, implied control AF 1.18%, 90%-power sample sizes 2924/.05 and 4048/.01, and powers 41%, 20%, 52%, 34% in the four columns 4000/.05, 4000/.01, 5000/.05, 5000/.01. The rightmost printed number is 34%, independently read from the source render.

The diagnostic reproducing method uses equal allocation, total subgroup size Tf and per-arm m=Tf/2. Set d=p1−p0, A=√[(p0+p1)(1−(p0+p1)/2)], B=√[p0(1−p0)+p1(1−p1)] and z=Φ⁻¹(1−α/2). Power in percent is 100{Φ[(√m d−zA−1/√m)/B]+Φ[(−√m d−zA−1/√m)/B]}. The subtraction 1/√m is the continuity-correction term. This is a same-display reconstruction, not a claim that the exact source software is known.

Independent central reconstructed powers, in the table's four-column order, with printed values in parentheses:

- Age <80: 88.977875% (89%); 72.845978% (73%); 94.860067% (95%); 84.476660% (85%).
- Age ≥80: 95.857850% (96%); 86.766868% (87%); 98.603992% (99%); 94.288019% (95%).
- Age <75: 41.851152% (41%); 20.530754% (20%); 52.055448% (52%); 28.585280% (34%).
- Age ≥75: 99.557460% (100%); 97.723140% (98%); 99.926443% (100%); 99.479987% (100%).
- Males: 97.938182% (98%); 92.261244% (92%); 99.443747% (99%); 97.260074% (98%).
- Female: 80.516912% (80%); 59.595357% (60%); 89.005329% (89%); 72.889321% (75%).

All other 23 power outputs satisfy the display-precision rule, including the female 5000/.01 output: its central 72.889321% gives gap (74.5−72.889321)/75=0.021476, below .05 even before varying inputs. Using the half-unit input boxes, the only remaining nonzero comparator gaps are males 5000/.01, relative 0.000254, and female 5000/.01, relative 0.006505; both are below .05. The 12 sample-size outputs also track the same continuity-corrected reconstruction: Age <80 2644.027/3662.921 versus 2642/3658; Age ≥80 1129.398/1564.024 versus 1135/1571; Age <75 2905.288/4024.585 versus 2924/4048; Age ≥75 1565.495/2168.427 versus 1563/2164; Males 1457.054/2018.125 versus 1458/2018; Female 2373.467/3288.083 versus 2367/3276 (all central discrepancies under 1%).

For the affected cell, p0∈[.01175,.01185], p1∈[.02955,.02965], f∈[.245,.255] and, conservatively, T∈[4999.5,5000.5]. The stated significance threshold .01 is an exact decision rule, rather than a rounded observation. Letting the control/active rates vary independently is conservative: imposing the displayed ratio and patch-rate/multiplier relationships can only narrow this box. Every possible permitted unrounded input is therefore covered.

Endpoint evaluation gives 27.350760–29.844731%. Separately, full interval arithmetic without requiring endpoint monotonicity gives the wider guaranteed enclosure 27.225032–29.972784%: m∈[612.43875,637.56375], d∈[.0177,.0179], A∈[.201114780660,.201590860408], B∈[.200720539557,.201197552172], first CDF argument ∈[−.606021786852,−.525184440686] and second argument ∈[−5.040078175893,−4.948728272239]. The printed 34% interval is [33.5,34.5]%, so the conservative minimum gap is 33.5−29.972784=3.527216 percentage points and relative discrepancy is 3.527216/34=0.103742, greater than .05. Normal-CDF approximation precision is below 0.00002 percentage point and cannot affect this result.

The affected extracted value is the planned age-under-75 subgroup power at total trial size 5000 and two-sided .01. No claim about the primary reported treatment-effect result follows. The exact implementation is not supplied; a distinct cell-specific correction/input could be an alternative explanation, but under Route A category 4 it is the human question rather than an exclusion. An uncorrected calculation may approach 34% but does not reproduce the same row's 20% at 4000/.01. The issue remains one included issue, with every affected/comparator location retained.

## Provenance, counts and limitations

Source page visuals were authoritative. Existing current-run protocol p. 20–22 images and cross-checker main p. 3/7 / SAP p. 20 images were inspected directly. Four additional source renders are preprocessing/screen-initial-main1.png, preprocessing/screen-initial-main5.png, preprocessing/screen-initial-sap5.png and preprocessing/screen-initial-sap21.png. Engine: recorded package-local pdf_tools.py / PyMuPDF 1.26.4, CPU, 200 dpi. No new OCR was performed; approved protocol GPU OCR served only as a locator. JavaScript V8 performed arithmetic; the durable computation record is [screen-initial-power-computation.json](../preprocessing/screen-initial-power-computation.json).

Initial totals: 2 findings, 1 INCLUDE, 1 SCREENED_OUT (CONDITIONAL_OR_UNREPORTED), 1 distinct included issue, 0 consolidations. Included Candidate ID is C001 after coordinator registration. Limitations: exact Table 4 power implementation and later clinical-analysis specification are not supplied; neither prevents checking the cited source facts and applying this inclusion decision. No source/reused artifact was modified and no assigned source location remains uninspected.
