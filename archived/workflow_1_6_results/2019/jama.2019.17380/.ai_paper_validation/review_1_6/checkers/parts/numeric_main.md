# Main-report numeric consistency checker

Scope: DOC-001 main REPORT, PDF pages 1–11; all 120 map bundles independently checked. Numeric relationships N001–N120 in relationships/parts/numeric_main_inventory.md. Twenty-six distinct local candidates are emitted below. No stable C IDs, severity, validity, final correction, or disposition is assigned. Every candidate requires human adjudication. Identical topics or shared apparent production mechanisms do not merge distinct subgroup or time-specific comparisons.

Evidence: complete current mapper source transcription, direct Poppler layout extraction of supplied PDF pages 7–9, and visual inspection of reusable source-page renderings 5,7,8,9. Direct-source text confirmed every Figure 2–4 count and caption input. Source excerpts are locators; mechanical recheck remains a separate stage. All compared locations have REPORT role by content. The arithmetic and classification boundaries are QUALITY_CONTROL_SCOPE.md and workflow_1_6/review_contract.md. No old candidate/checker/report conclusions or external source was used.

Main checks with no candidate: Figure 1 all integer totals/overlaps and baseline missingness; Table 1 all arm percentages under the nonmissing-response footnote, category sums, duration median and valid IQR; Table 2 six Ns, means, signs, units, independently rounded modeled differences; Table 3 rates/contrasts/event totals and distinctions among count/risk/person-time/Cox HR; retention percentages and deaths; adverse event totals; 0.75×5=3.75; main internal repeated estimates. Underlying person-time and some Table 1 response Ns are unprinted, preventing exact recalculation without inventing inputs. These do not create candidates.

## NUM-M01: Narrative minority percentage versus explicit race-category totals

- **Relationship IDs:** N009
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), abstract Results.
  - REPORT, DOC-001 [PDF page 4](../../../../jama_de_boer_2019_oi_190122.pdf#page=4), Participant Characteristics.
  - REPORT, DOC-001 [PDF page 5](../../../../jama_de_boer_2019_oi_190122.pdf#page=5), Table 1 Race/ethnicity rows and nonmissing denominator footnote.
- **Printed inputs:** Narrative: 31% racial or ethnic minority. Table 1 nonmissing race N=361+327+284+314=1286; non-Hispanic white=240+211+199+207=857; other race/ethnicity categories total 429, including Other=9+8+2+9=28.
- **Reproducible rule:** If minority means every non-Hispanic-white category in the displayed race/ethnicity table, its narrative percentage must match that denominator.
- **Calculation / identity:** (1286−857)/1286×100=33.3593%, rounding to 33%; 429/1312×100=32.6982%, also 33%; excluding Other gives 401/1286×100=31.18196%, rounding 31%.
- **Tolerance:** ±0.5 percentage points for integer display.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** A source-specific minority definition may exclude the 28 Other responses. That exactly explains 31%, but the main article does not explicitly define this exclusion. This is a conditional definition/denominator question, not a claim that the percentage necessarily is wrong.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Does the reported 31% exclude the Other category, and what exact minority numerator and denominator were used?
- **Status:** Pending Human Adjudication.

## NUM-M02: Figure 2B omega-3 eGFR participant counts at baseline

- **Relationship IDs:** N080
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7), Figure 2B, No. of participants, baseline.
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Table 2 Omega-3 Fatty Acids, baseline, active and placebo No.
- **Printed inputs:** Figure 2B placebo=607, omega-3=701; Table 2 same-time placebo=651, omega-3=657.
- **Reproducible rule:** Counts of participants contributing the same serum eGFR at the same time under the same treatment label should agree.
- **Calculation / identity:** Figure−Table placebo=-44; active=44. Both totals agree (1308), but treatment-specific counts differ.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Figure 2 caption explicitly says numbers are participants contributing data at each time point. Table 2 may conceivably use an undisclosed different eligible subset, but exact duplication of Figure 2A count rows across all times is a direct observation, not proof of a copying mechanism.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which treatment-specific eGFR participant counts belong in Figure 2B at baseline, or what stated population distinction explains the differences?
- **Status:** Pending Human Adjudication.

## NUM-M03: Figure 2B omega-3 eGFR participant counts at year 2

- **Relationship IDs:** N080
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7), Figure 2B, No. of participants, year 2.
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Table 2 Omega-3 Fatty Acids, year 2, active and placebo No.
- **Printed inputs:** Figure 2B placebo=459, omega-3=531; Table 2 same-time placebo=491, omega-3=499.
- **Reproducible rule:** Counts of participants contributing the same serum eGFR at the same time under the same treatment label should agree.
- **Calculation / identity:** Figure−Table placebo=-32; active=32. Both totals agree (990), but treatment-specific counts differ.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Figure 2 caption explicitly says numbers are participants contributing data at each time point. Table 2 may conceivably use an undisclosed different eligible subset, but exact duplication of Figure 2A count rows across all times is a direct observation, not proof of a copying mechanism.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which treatment-specific eGFR participant counts belong in Figure 2B at year 2, or what stated population distinction explains the differences?
- **Status:** Pending Human Adjudication.

## NUM-M04: Figure 2B omega-3 eGFR participant counts at year 5

- **Relationship IDs:** N080
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7), Figure 2B, No. of participants, year 5.
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Table 2 Omega-3 Fatty Acids, year 5, active and placebo No.
- **Printed inputs:** Figure 2B placebo=438, omega-3=496; Table 2 same-time placebo=462, omega-3=472.
- **Reproducible rule:** Counts of participants contributing the same serum eGFR at the same time under the same treatment label should agree.
- **Calculation / identity:** Figure−Table placebo=-24; active=24. Both totals agree (934), but treatment-specific counts differ.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Figure 2 caption explicitly says numbers are participants contributing data at each time point. Table 2 may conceivably use an undisclosed different eligible subset, but exact duplication of Figure 2A count rows across all times is a direct observation, not proof of a copying mechanism.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which treatment-specific eGFR participant counts belong in Figure 2B at year 5, or what stated population distinction explains the differences?
- **Status:** Pending Human Adjudication.

## NUM-M05: Figure 2D baseline omega-3 ACR count exceeds allocated group

- **Relationship IDs:** N082
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7), Figure 2D baseline No. of participants, Omega-3 fatty acids.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions four randomized groups.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 randomized treatment groups.
- **Printed inputs:** Figure 2D omega-3 baseline ACR N=702; randomized omega-3 arms 370 and 289; Figure 2C vitamin-D baseline ACR N=702.
- **Reproducible rule:** A treatment-arm baseline measurement subset cannot exceed all participants randomized to that treatment.
- **Calculation / identity:** Allocated omega-3 maximum 370+289=659; 702−659=43 more participants than allocated.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** A panel-label/count-row error or undocumented reassignment could explain the row. Missing observations only decrease an arm's observed count; the repeated vitamin-D row is observed but copying is inferred.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Does 702 belong to the vitamin-D intervention, and what is the correct randomized omega-3 baseline ACR count?
- **Status:** Pending Human Adjudication.

## NUM-M06: Figure 2 caption reverses quartile border labels

- **Relationship IDs:** N083
- **Primary category for coordinator consideration:** Measure, label, or scale inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7), Figure 2 caption top/bottom box-border definition.
  - REPORT, DOC-001 [PDF page 7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7), Figure 2 panels A–D increasing vertical numeric axes.
- **Printed inputs:** Caption: top and bottom box borders indicate first and third quartiles, respectively. eGFR axes increase 0→200 upwards; ACR axes increase 0.1→10000 upwards.
- **Reproducible rule:** Quartile order and monotone axis direction must agree with border labels.
- **Calculation / identity:** First quartile Q1≤Q3 third quartile; increasing vertical scales require bottom≤top. Caption assigns top=Q1 and bottom=Q3, implying top≤bottom contrary to displayed nonzero-height boxes.
- **Tolerance:** Ordinal identity; no numeric rounding allowance can invert Q1/Q3.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Likely order of first/third or top/bottom was reversed in caption; actual box-generating quantiles are not printed, so no claim about their values.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which quartile labels should be assigned to the upper and lower borders?
- **Status:** Pending Human Adjudication.

## NUM-M07: Figure 3 overall vitamin-D count labels versus allocation

- **Relationship IDs:** N091
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 Overall, Placebo and Vitamin D No. of Participants.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 arm allocations.
- **Printed inputs:** Figure 3 Placebo 703, vitamin D=609; allocated D=370+333, placebo 289+320.
- **Reproducible rule:** Full imputed overall counts must match randomized intervention membership under each heading.
- **Calculation / identity:** D=703 and placebo 609; printed placebo 703−609=94; printed D=609−703=−94.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Count columns may be transposed while means remain under intended labels: Figure 3 means −13.1 placebo/−12.3D matchTable 2. No assumption is made that all numerical columns or graph points should be swapped.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Are Figure 3 overall participant counts under opposite treatment headings, and which columns beyond counts, if any, require clarification?
- **Status:** Pending Human Adjudication.

## NUM-M08: Figure 3 White subgroup counts versus Table 1

- **Relationship IDs:** N092
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 White row, Placebo and vitamin D participant counts.
  - REPORT, DOC-001 [PDF page 5](../../../../jama_de_boer_2019_oi_190122.pdf#page=5), Table 1 White counts in all four treatment arms.
- **Printed inputs:** Figure 3 Placebo 451, D=406; Table 1 P=199+207=406, D=240+211=451.
- **Reproducible rule:** Baseline subgroup counts in a full randomized/imputed subgroup analysis must preserve their treatment assignment from the arm-specific baseline table.
- **Calculation / identity:** Printed placebo−Table 1 placebo=45; printed D−Table 1 D=-45; same combined total 857.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** The N columns may be reversed. Restricting to a subset cannot increase a subgroup count beyond its same-assignment baseline count; exact reciprocal pair reinforces identity observation without proving production error.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Why are the Figure 3 White participant counts opposite to the arm-specific Table 1 sums, and what treatment label applies to each count?
- **Status:** Pending Human Adjudication.

## NUM-M09: Figure 3 Black subgroup counts versus Table 1

- **Relationship IDs:** N093
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 Black row, Placebo and vitamin D participant counts.
  - REPORT, DOC-001 [PDF page 5](../../../../jama_de_boer_2019_oi_190122.pdf#page=5), Table 1 Black counts in all four treatment arms.
- **Printed inputs:** Figure 3 Placebo 148, D=130; Table 1 P=59+71=130, D=73+75=148.
- **Reproducible rule:** Baseline subgroup counts in a full randomized/imputed subgroup analysis must preserve their treatment assignment from the arm-specific baseline table.
- **Calculation / identity:** Printed placebo−Table 1 placebo=18; printed D−Table 1 D=-18; same combined total 278.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** The N columns may be reversed. Restricting to a subset cannot increase a subgroup count beyond its same-assignment baseline count; exact reciprocal pair reinforces identity observation without proving production error.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Why are the Figure 3 Black participant counts opposite to the arm-specific Table 1 sums, and what treatment label applies to each count?
- **Status:** Pending Human Adjudication.

## NUM-M10: Figure 3 ACR<30 placebo subgroup exceeds all placebo participants

- **Relationship IDs:** N094
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 baseline urineACR<30 row, Placebo N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 allocation.
- **Printed inputs:** Figure 3 Placebo ACR<30 N=635; randomized D-placebo 289+320=609; pairedACR≥30 N=67.
- **Reproducible rule:** A subgroup under a treatment heading cannot exceed that treatment's entire randomized population.
- **Calculation / identity:** 635−609=26; full ACR subgroup sum 635+67=702, which also exceeds 609.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Figure 3 count headings may be reversed; missing baseline ACR can only reducecounts. No exact true arm-specific ACR<30 distribution is fabricated.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** What treatment assignment belongs to the 635 ACR<30 participants?
- **Status:** Pending Human Adjudication.

## NUM-M11: Figure 3 25(OH)D <20 ng/mL subgroup counts versus Table 1

- **Relationship IDs:** N096
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 25(OH)D <20 ng/mL row, Placebo and vitamin D participant counts.
  - REPORT, DOC-001 [PDF page 5](../../../../jama_de_boer_2019_oi_190122.pdf#page=5), Table 1 25(OH)D <20 ng/mL counts in all four treatment arms.
- **Printed inputs:** Figure 3 Placebo 110, D=85; Table 1 P=41+44=85, D=62+48=110.
- **Reproducible rule:** Baseline subgroup counts in a full randomized/imputed subgroup analysis must preserve their treatment assignment from the arm-specific baseline table.
- **Calculation / identity:** Printed placebo−Table 1 placebo=25; printed D−Table 1 D=-25; same combined total 195.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** The N columns may be reversed. Restricting to a subset cannot increase a subgroup count beyond its same-assignment baseline count; exact reciprocal pair reinforces identity observation without proving production error.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Why are the Figure 3 25(OH)D <20 ng/mL participant counts opposite to the arm-specific Table 1 sums, and what treatment label applies to each count?
- **Status:** Pending Human Adjudication.

## NUM-M12: Figure 3 25(OH)D 20 to <30 ng/mL subgroup counts versus Table 1

- **Relationship IDs:** N097
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 25(OH)D 20 to <30 ng/mL row, Placebo and vitamin D participant counts.
  - REPORT, DOC-001 [PDF page 5](../../../../jama_de_boer_2019_oi_190122.pdf#page=5), Table 1 25(OH)D 20 to <30 ng/mL counts in all four treatment arms.
- **Printed inputs:** Figure 3 Placebo 230, D=203; Table 1 P=87+116=203, D=109+121=230.
- **Reproducible rule:** Baseline subgroup counts in a full randomized/imputed subgroup analysis must preserve their treatment assignment from the arm-specific baseline table.
- **Calculation / identity:** Printed placebo−Table 1 placebo=27; printed D−Table 1 D=-27; same combined total 433.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** The N columns may be reversed. Restricting to a subset cannot increase a subgroup count beyond its same-assignment baseline count; exact reciprocal pair reinforces identity observation without proving production error.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Why are the Figure 3 25(OH)D 20 to <30 ng/mL participant counts opposite to the arm-specific Table 1 sums, and what treatment label applies to each count?
- **Status:** Pending Human Adjudication.

## NUM-M13: Figure 3 25(OH)D ≥30 ng/mL subgroup counts versus Table 1

- **Relationship IDs:** N098
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 25(OH)D ≥30 ng/mL row, Placebo and vitamin D participant counts.
  - REPORT, DOC-001 [PDF page 5](../../../../jama_de_boer_2019_oi_190122.pdf#page=5), Table 1 25(OH)D ≥30 ng/mL counts in all four treatment arms.
- **Printed inputs:** Figure 3 Placebo 332, D=297; Table 1 P=146+151=297, D=184+148=332.
- **Reproducible rule:** Baseline subgroup counts in a full randomized/imputed subgroup analysis must preserve their treatment assignment from the arm-specific baseline table.
- **Calculation / identity:** Printed placebo−Table 1 placebo=35; printed D−Table 1 D=-35; same combined total 629.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** The N columns may be reversed. Restricting to a subset cannot increase a subgroup count beyond its same-assignment baseline count; exact reciprocal pair reinforces identity observation without proving production error.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Why are the Figure 3 25(OH)D ≥30 ng/mL participant counts opposite to the arm-specific Table 1 sums, and what treatment label applies to each count?
- **Status:** Pending Human Adjudication.

## NUM-M14: Figure 3 eGFR≥60 placebo subgroup exceeds all placebo participants

- **Relationship IDs:** N099
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 baseline eGFR≥60 row, Placebo N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 allocation.
- **Printed inputs:** Figure 3 Placebo eGFR≥60 N=612; randomized D-placebo 609; Figure 3 corresponding <60 N=89.
- **Reproducible rule:** A baseline subgroup cannot exceed all randomized participants of that treatment heading.
- **Calculation / identity:** 612−609=3; 612+89=701, consistent with Table 2 D measured baseline N 701 rather than placebo 607.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Transposed count headings explain capacity mismatch; unreported missing observations cannot increase the population. The means/graph are not inferred to be transposed.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** What treatment assignment applies to 612 participants with baseline eGFR≥60?
- **Status:** Pending Human Adjudication.

## NUM-M15: Figure 3 BMI placebo subgroup sum exceeds all placebo participants

- **Relationship IDs:** N103
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 BMI<25,25 to<30,≥30 Placebo Ns.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 allocation.
- **Printed inputs:** BMI Placebo Ns=87,228,364; true D-placebo randomized N=609.
- **Reproducible rule:** Disjoint exhaustive BMI intervals among a treatment group cannot sum above its full randomized N; missing BMI may reduce the sum only.
- **Calculation / identity:** 87+228+364=679; 679−609=70.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Reversed count headings could explain 679≤true D=703; participant-level missingness explains a deficit but not excess. These are distinct BMI groups, not repeated measurement counts.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which assignment does the BMI count sum 679 represent, and are the treatment count columns labeled correctly?
- **Status:** Pending Human Adjudication.

## NUM-M16: Figure 3 factorial P+P participant count

- **Relationship IDs:** N104
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 Omega-3 placebo randomization row, Placebo N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions P+P allocation.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 P+P randomized/primary analysis arm.
- **Printed inputs:** Figure 3 row=Omega-3 placebo, column=Placebo implies P+P, printed N=333; allocationP+P=320.
- **Reproducible rule:** Crossing the row's other intervention assignment with the column's vitamin-D assignment identifies one unique randomized factorial arm.
- **Calculation / identity:** 333−320=13 participants.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** A transposed count column explains someFigure 3 cells; reporting counts for a different arm would require explicit label clarification. All primary groups analyze randomized N, so follow-up loss does not redefine arm allocation.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which factorial arm does Figure 3 N=333 in thisOmega-3 placebo/Placebocell represent?
- **Status:** Pending Human Adjudication.

## NUM-M17: Figure 3 factorial D+P participant count

- **Relationship IDs:** N104
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 Omega-3 placebo randomization row, Vitamin D N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions D+P allocation.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 D+P randomized/primary analysis arm.
- **Printed inputs:** Figure 3 row=Omega-3 placebo, column=Vitamin D implies D+P, printed N=320; allocationD+P=333.
- **Reproducible rule:** Crossing the row's other intervention assignment with the column's vitamin-D assignment identifies one unique randomized factorial arm.
- **Calculation / identity:** 320−333=-13 participants.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** A transposed count column explains someFigure 3 cells; reporting counts for a different arm would require explicit label clarification. All primary groups analyze randomized N, so follow-up loss does not redefine arm allocation.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which factorial arm does Figure 3 N=320 in thisOmega-3 placebo/Vitamin Dcell represent?
- **Status:** Pending Human Adjudication.

## NUM-M18: Figure 3 factorial P+O participant count

- **Relationship IDs:** N105
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 Omega-3 fatty acids randomization row, Placebo N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions P+O allocation.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 P+O randomized/primary analysis arm.
- **Printed inputs:** Figure 3 row=Omega-3 fatty acids, column=Placebo implies P+O, printed N=370; allocationP+O=289.
- **Reproducible rule:** Crossing the row's other intervention assignment with the column's vitamin-D assignment identifies one unique randomized factorial arm.
- **Calculation / identity:** 370−289=81 participants.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** A transposed count column explains someFigure 3 cells; reporting counts for a different arm would require explicit label clarification. All primary groups analyze randomized N, so follow-up loss does not redefine arm allocation.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which factorial arm does Figure 3 N=370 in thisOmega-3 fatty acids/Placebocell represent?
- **Status:** Pending Human Adjudication.

## NUM-M19: Figure 3 factorial D+O participant count

- **Relationship IDs:** N105
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), Figure 3 Omega-3 fatty acids randomization row, Vitamin D N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions D+O allocation.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 D+O randomized/primary analysis arm.
- **Printed inputs:** Figure 3 row=Omega-3 fatty acids, column=Vitamin D implies D+O, printed N=289; allocationD+O=370.
- **Reproducible rule:** Crossing the row's other intervention assignment with the column's vitamin-D assignment identifies one unique randomized factorial arm.
- **Calculation / identity:** 289−370=-81 participants.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** A transposed count column explains someFigure 3 cells; reporting counts for a different arm would require explicit label clarification. All primary groups analyze randomized N, so follow-up loss does not redefine arm allocation.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which factorial arm does Figure 3 N=289 in thisOmega-3 fatty acids/Vitamin Dcell represent?
- **Status:** Pending Human Adjudication.

## NUM-M20: Figure 4 overall omega-3 count labels versus allocation

- **Relationship IDs:** N106
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 9](../../../../jama_de_boer_2019_oi_190122.pdf#page=9), Figure 4 Overall, Placebo and Omega-3 No. of Participants.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 allocated arms.
- **Printed inputs:** Figure 4 Placebo 659, omega-3=653; trueomega-3=370+289, placebo 333+320.
- **Reproducible rule:** Full randomized/imputed intervention counts preserve allocated labels.
- **Calculation / identity:** Trueactive 659, placebo 653; printed placebo−true placebo=6; printedactive−true active=−6.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** The count columns may be transposed while means −13.1/−12.2 agreeTable 2 intendedplacebo/active. Graph or SD swapping is not inferred.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** What treatment labels belong to Figure 4 overallNs 659 and 653?
- **Status:** Pending Human Adjudication.

## NUM-M21: Figure 4 ACR placebo subgroup sum exceeds allocated placebo N

- **Relationship IDs:** N108
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 9](../../../../jama_de_boer_2019_oi_190122.pdf#page=9), Figure 4 ACR<30 and≥30 Placebo Ns.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 allocations.
- **Printed inputs:** Figure 4 ACR Placebo Ns=596 and 62; randomizedO-placebo 333+320=653.
- **Reproducible rule:** Disjoint baseline ACR categories cannot contain more distinct people than their randomized treatment group.
- **Calculation / identity:** 596+62=658; 658−653=5.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Potential transposed count labels explain 658≤true active 659. The figure'sown overall Placebo 659 also disagrees with allocation; none of these observations proves how means were computed.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which treatment assignment applies to the 658 ACR subgroup participants?
- **Status:** Pending Human Adjudication.

## NUM-M22: Figure 4 hsCRP placebo subgroup sum exceeds allocated placebo N

- **Relationship IDs:** N109
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 9](../../../../jama_de_boer_2019_oi_190122.pdf#page=9), Figure 4 hsCRP≤0.2 and>0.2mg/dL Placebo Ns.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 allocations.
- **Printed inputs:** Figure 4 hsCRP Placebo Ns=334 and 323; trueO-placebo 653.
- **Reproducible rule:** Mutually exclusive baseline hsCRP categories cannot total more participants than randomized to that treatment.
- **Calculation / identity:** 334+323=657; 657−653=4.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Potential transposed count headings explain 657≤true active 659; missing hsCRP only reduces count. Actual assay-unit conversion is a separate support-lane issue, not asserted here.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which treatment assignment applies to the 657 hsCRP subgroup participants?
- **Status:** Pending Human Adjudication.

## NUM-M23: Figure 4 factorial P+P participant count

- **Relationship IDs:** N111
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 9](../../../../jama_de_boer_2019_oi_190122.pdf#page=9), Figure 4 vitamin D randomization Placebo row, Placebo N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions P+P allocation.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 P+P arm allocation.
- **Printed inputs:** Figure 4 rowD=Placebo, columnO=Placebo implies P+P, printed N=289; allocated N=320.
- **Reproducible rule:** The column's omega-3 assignment crossed with row's vitamin-D assignment identifies a unique factorial arm with the reported allocation N.
- **Calculation / identity:** 289−320=-31 participants.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Transposed count labels are a possible explanation. Changes in measured follow-up cannot change an allocated full-imputation arm count; all printed mean/SD pairs matchFigure 3 under literal assignment labels.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which factorial arm is represented by Figure 4 N=289 in D=Placebo, O=Placebo cell?
- **Status:** Pending Human Adjudication.

## NUM-M24: Figure 4 factorial P+O participant count

- **Relationship IDs:** N111
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 9](../../../../jama_de_boer_2019_oi_190122.pdf#page=9), Figure 4 vitamin D randomization Placebo row, Omega-3 Fatty Acids N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions P+O allocation.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 P+O arm allocation.
- **Printed inputs:** Figure 4 rowD=Placebo, columnO=Omega-3 Fatty Acids implies P+O, printed N=320; allocated N=289.
- **Reproducible rule:** The column's omega-3 assignment crossed with row's vitamin-D assignment identifies a unique factorial arm with the reported allocation N.
- **Calculation / identity:** 320−289=31 participants.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Transposed count labels are a possible explanation. Changes in measured follow-up cannot change an allocated full-imputation arm count; all printed mean/SD pairs matchFigure 3 under literal assignment labels.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which factorial arm is represented by Figure 4 N=320 in D=Placebo, O=Omega-3 Fatty Acids cell?
- **Status:** Pending Human Adjudication.

## NUM-M25: Figure 4 factorial D+P participant count

- **Relationship IDs:** N111
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 9](../../../../jama_de_boer_2019_oi_190122.pdf#page=9), Figure 4 vitamin D randomization Vitamin D row, Placebo N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions D+P allocation.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 D+P arm allocation.
- **Printed inputs:** Figure 4 rowD=Vitamin D, columnO=Placebo implies D+P, printed N=370; allocated N=333.
- **Reproducible rule:** The column's omega-3 assignment crossed with row's vitamin-D assignment identifies a unique factorial arm with the reported allocation N.
- **Calculation / identity:** 370−333=37 participants.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Transposed count labels are a possible explanation. Changes in measured follow-up cannot change an allocated full-imputation arm count; all printed mean/SD pairs matchFigure 3 under literal assignment labels.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which factorial arm is represented by Figure 4 N=370 in D=Vitamin D, O=Placebo cell?
- **Status:** Pending Human Adjudication.

## NUM-M26: Figure 4 factorial D+O participant count

- **Relationship IDs:** N111
- **Primary category for coordinator consideration:** Denominator, proportion, or total inconsistency
- **Compared locations and document roles:**
  - REPORT, DOC-001 [PDF page 9](../../../../jama_de_boer_2019_oi_190122.pdf#page=9), Figure 4 vitamin D randomization Vitamin D row, Omega-3 Fatty Acids N.
  - REPORT, DOC-001 [PDF page 1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1), Interventions D+O allocation.
  - REPORT, DOC-001 [PDF page 6](../../../../jama_de_boer_2019_oi_190122.pdf#page=6), Figure 1 D+O arm allocation.
- **Printed inputs:** Figure 4 rowD=Vitamin D, columnO=Omega-3 Fatty Acids implies D+O, printed N=333; allocated N=370.
- **Reproducible rule:** The column's omega-3 assignment crossed with row's vitamin-D assignment identifies a unique factorial arm with the reported allocation N.
- **Calculation / identity:** 333−370=-37 participants.
- **Tolerance:** 0 participants.
- **Direct observation versus inference:** The cited counts, labels, caption, or percentage are printed observations. The calculation is derived from those observations. A possible column reversal, copied row, or definition choice is an explanatory inference, not an established mechanism or correction.
- **Source-grounded alternative / necessary missing definition:** Transposed count labels are a possible explanation. Changes in measured follow-up cannot change an allocated full-imputation arm count; all printed mean/SD pairs matchFigure 3 under literal assignment labels.
- **Bounded quality-control relevance:** A treatment-specific sample count, subgroup identity, summary percentage, or distribution label could be extracted with the wrong reported meaning in a downstream evidence table. No paper-level conclusion impact is inferred.
- **Exact human question:** Which factorial arm is represented by Figure 4 N=333 in D=Vitamin D, O=Omega-3 Fatty Acids cell?
- **Status:** Pending Human Adjudication.

## Complete scope and limitations

All DOC-001 pages 1–11 and all N001–N120 relationships have been checked. Graphical median/quartile/forest estimates are not printed exactly; the checker uses only ordinal placement and explicit count/label text, never invented pixel-derived estimates. The main article does not give arm-specific omega-3 ACR measurement Ns beyond Figure 2 or every response/person-time denominator. Figure 2D year 2/year 5 duplicate-lookingrows remain noted in N082 but no numeric contradiction is fabricated without a main-source comparator. Minority definition is explicitly unresolved in NUM-M01. Statistical inference, cross-document checks, and support-source quantities are delegated separately. No assigned scientific coverage gap remains.

