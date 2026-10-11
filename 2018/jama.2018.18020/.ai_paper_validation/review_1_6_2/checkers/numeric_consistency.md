# Numeric consistency review

Scope: all 83 supplied PDF pages through the complete fresh main/support maps and the 89 canonical relationships N001–N089. Document roles by content: DOC-001 main article REPORT; DOC-002 prospective protocol PLAN; DOC-003 results/methods supplement REPORT; DOC-004 data-sharing statement REPORT. All count, denominator, total, numerator/percentage, range, score-unit and effect-identity relationships were checked. Complete canonical coverage is in [numeric inventory](../relationships/numeric_relationship_inventory.md). Background and administrative units were read and mapped. No web, old conclusions, source modification, or auxiliary scientific Python used.

Tooling: recorded Poppler pdftotext 25.03.0; targeted current-source reads of DOC-001 pp.1–5,7–8 and DOC-003 pp.3–6 confirmed printed inputs. Full source-linked mapper transcriptions and graphical inspections supply remaining unit coverage. Compute device CPU. No new derivative files generated. No scientific coverage gap. Source limitations: individual raw daily data, per-outcome paired sample membership, covariance matrices and exact numerical graph coordinates are not supplied.

Four self-screened findings; six excluded observations. All findings remain observations for independent inclusion screening; no C IDs or adjudication labels assigned. Count values are exact integers. Half-unit intervals apply to displayed continuous/percentage values. The statistical lane independently reviews all CI/test logic, Table 2 contrast direction and dependent-t reproduction; the cross-source lane independently reviews planned sample size, decision thresholds, endpoint and analysis elements.

### F-NUM-001

**Title:** Abstract male percentage does not reconcile with enrolled male count.

**Relationships:** N003; N060. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; DOC-003 merely corroborates the body count and is not a separate conflicting relationship.

**Compared locations and document roles:** REPORT [main PDF p.1 abstract Results](../../../jama_stunnenberg_2018_oi_180136.pdf#page=1), REPORT [main PDF p.4 Baseline Data](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4). Corroborating REPORT [results supplement pp.3–4 eTable 2](../../../joi180136supp2_prod.pdf#page=3).

**Printed inputs:** Abstract: “30 patients enrolled” and “22% men.” Body: 22 men and 8 women among 30 enrolled. eTable 2 contains 22 male and 8 female rows.

**Rule and calculation:** Sex percentage = 100 × male count / enrolled count. Counts exact: 100×22/30 = 73.333333%. Recomputed interval [73.333333,73.333333]; abstract whole-percentage interval [21.5,22.5]. Gap = 50.833333 percentage points; relative discrepancy = 50.833333/22 = 2.310606, above .05. Enrolled counts 22+8=30 reconcile.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Male percentage of the enrolled analysis population as taken from the abstract.

**Why context does not resolve it:** Route A category 2 applies to a printed percentage whose magnitude changes the reading; reconstructing 73.3% from the body does not remove the conflicting abstract number.

**Alternatives and missing definitions:** The abstract “22%” may have been intended as the count 22 rather than a percentage. No alternative enrolled denominator is stated that yields 22%.

**Exact human question:** What male percentage or male count should be extracted for the 30 enrolled participants, and how should the abstract “22% men” be read?

### F-NUM-002

**Title:** Genotype subgroup enrollment and primary-analysis denominators do not reconcile with the individual genotype rows.

**Relationships:** N003, N020, N060, with N037, N038, N043, N057 and N059 supplying analyzed-population context. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C; **All relationships:** S_C. The cross-document relationship is the main enrolled counts versus results supplement individual rows. Main enrolled19/11 and analyzed16/11 imply three CLCN1 withdrawals, whereas the explicitly named withdrawals include patient7, whose individual supplement genotype is SCN4A.

**Compared locations and document roles:** REPORT [main p.1 abstract Results](../../../jama_stunnenberg_2018_oi_180136.pdf#page=1); REPORT [main p.4 Baseline Data/Numbers Analyzed and Figure 1](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4); REPORT [main p.5 Table 1 and Figure 2 subgroup labels](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5); REPORT [main p.6 Figure 3 group labels](../../../jama_stunnenberg_2018_oi_180136.pdf#page=6); REPORT [main p.8 Table 2 footnote a](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8); REPORT [supplement p.3 eTable 2 patients1–19](../../../joi180136supp2_prod.pdf#page=3), REPORT [supplement p.4 eTable 2 patients20–30](../../../joi180136supp2_prod.pdf#page=4), REPORT [supplement p.5 eTable 3 genotype rows/dropout footnote](../../../joi180136supp2_prod.pdf#page=5).

**Printed inputs:** Main enrolled: CLCN1 19, SCN4A 11, total30. Main analyzed: CLCN1 16, SCN4A 11, total27. eTable 2 CLCN1 IDs1,2,3,5,6,14,15,16,17,18,23,24,25,26,27,28,29,30 =18. SCN4A IDs4,7,8,9,10,11,12,13,19,20,21,22 =12. eTable 3 removes3,6,7 and shows CLCN1 IDs1,2,5,14,15,16,17,18,23,24,25,26,27,28,29,30 =16; SCN4A IDs4,8,9,10,11,12,13,19,20,21,22 =11.

**Rule and calculation:** Tally each individual row once by printed gene label. eTable 2 yields18 CLCN1+12 SCN4A=30. The main19/11 enrolled counts differ by one in each subgroup. Exact-count discrepancy relative to main CLCN1=1/19=.052632 and SCN4A=1/11=.090909, both above .05. Exact-count intervals [18,18]/[12,12] versus [19,19]/[11,11]; gap1. Removing CLCN1 patients3/6 and SCN4A patient7 yields18−2=16 and12−1=11, which fully reconciles with main analyzed16/11. Consequently the finding is confined to the enrolled genotype breakdown and its implied withdrawal allocation; analyzed subgroup labels reconcile.

**Literal half-unit sensitivity:** If the workflow half-unit rule treats printed counts as continuously rounded quantities, main19 has interval[18.5,19.5] and main11 interval[10.5,11.5]. The enumerated row tallies18 and12 are exact; resulting gaps are.5/19=.026316 and.5/11=.045455, each at most.05. If the tallied counts themselves also receive half-unit intervals[17.5,18.5] and[11.5,12.5], both paired intervals touch and gaps are zero. Thus this issue does not pass a continuous half-unit interpretation. Emission rests on the alternative that an enumerated participant count and a printed participant count are exact integers: restricting each half-unit interval to attainable integer counts restores the exact discrepancy above. The independent inclusion screen must determine which reading of the precision rule applies; the sensitivity is not suppressed.

**Qualifying route:** Route B.

**Affected result or extracted value:** Enrolled genotype distribution and genotype-specific attrition into the primary stiffness analysis: the reported19/11 enrolled breakdown implies three CLCN1 withdrawals, whereas the patient-linked data show two CLCN1 and one SCN4A withdrawal.

**Why context does not resolve it:** The enrolled subgroup counts are explicitly stated in both abstract and body and the individual gene labels identify a different subgroup breakdown. Neither location identifies a reclassification, duplicate patient, or alternative population. A reader cannot select the enrolled breakdown or subgroup-specific attrition without choosing between conflicting printed sources.

**Alternatives and missing definitions:** An enrolled patient's genotype may have been classified differently for the aggregate enrollment summary; no such change is disclosed. The analyzed16/11 totals provide context and reconcile with the individual records but do not determine which enrolled genotype count is intended.

**Exact human question:** Were the 30 enrolled patients divided18 CLCN1/12 SCN4A or19 CLCN1/11 SCN4A, and which genotype-specific withdrawal counts should be extracted?

### F-NUM-003

**Title:** “Any” adverse-reaction count does not reconcile with the listed reaction counts and the multiple-reaction rows.

**Relationships:** N061. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; all compared values are in one REPORT display.

**Compared location and document role:** REPORT [results supplement p.6 eTable 4, mexiletine adverse-reaction column](../../../joi180136supp2_prod.pdf#page=6). Denominator corroboration: REPORT [main p.8 Adverse Events](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), explicitly GI21 of30.

**Printed inputs:** In the nonserious “Adverse reactions” section: GI21, tremor2, palpitations2, headache1, insomnia1; Any27(90%); >1 adverse reactions2(7%); >2 adverse reactions0(0%). Separate “Serious adverse reactions” section: allergic skin reaction1(3%).

**Rule and calculation:** When the listed reaction categories count affected patients, their sum is21+2+2+1+1=27 patient-category memberships. Exactly two patients have more than one reaction and none more than two; each such patient contributes one duplicated membership. The unique affected count for these listed nonserious reactions is therefore27−2=25. Recomputed exact-count interval [25,25] versus printed Any [27,27]; gap2 and relative discrepancy2/27=.074074>.05. At denominator30, unique percentage83.333333% versus printed90% interval[89.5,90.5], gap6.166667 and relative gap6.166667/90=.068519>.05.

**Literal half-unit sensitivity:** If the five nonserious category counts are treated as continuously rounded, their sum lies[24.5,29.5]; the printed two patients with more than one reaction has interval[1.5,2.5]. Even taking the printed zero greater-than-two count as exactly zero, the resulting union can lie[22,28], overlapping printed Any27 interval[26.5,27.5]. The corresponding percentage can also overlap90%. Thus this continuous interpretation does not reproduce a discrepancy. The calculation above depends on exact attainable integer counts and the nonserious category scope, both disclosed for the independent screen.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** Number and percentage of patients with any adverse reaction on mexiletine.

**Why context does not resolve it:** Route A category3 applies to within-display counts and percentages. The table supplies both individual categories and explicit multiple-reaction counts; the “Any” value equals the sum of category counts while the multiple-reaction rows imply overlap.

**Alternatives and missing definitions:** “Any” could count reaction occurrences rather than unique patients, or could include unlisted reaction categories; neither is defined. If “Any” also includes the separately tabulated serious skin reaction, the largest unique count under these inputs is26, and its discrepancy from27 falls within the workflow .05 rule. This sensitivity is explicit: the qualifying arithmetic uses the separately headed nonserious section as its scope, so the human must establish what “Any” counts and whether the display's category list is complete.

**Exact human question:** Does “Any27(90%)” denote patients, reaction occurrences, or a broader category set, and how does it reconcile with two patients having more than one listed reaction?

### F-NUM-004

**Title:** INQoL displayed baseline quartiles exceed the stated composite-score range.

**Relationships:** N010, N034, N046. **Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.

**Compared locations and document roles:** REPORT [main p.5 Table 1 INQoL row and footnote f](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5); corroborating REPORT [main p.8 Table 2 footnote g](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8).

**Printed inputs:** INQoL composite score: CLCN1 median84.0(IQR74.5–110.3); SCN4A median98.0(IQR56.0–120.0). Footnote f: “Scale,0 to100; a higher score indicates greater disease severity.” Table2 footnote g repeats0–100 for INQoL.

**Rule and calculation:** A quartile of a variable bounded0–100 must lie within0–100. Scale endpoints define exact bounds. Upper quartile110.3 has display interval[110.25,110.35]; gap from maximal attainable100 =10.25; relative discrepancy10.25/110.3=.092928>.05. Upper quartile120.0 has interval[119.95,120.05]; gap19.95; relative19.95/120=.16625>.05. Both median and lower-quartile readings are preserved; only upper quartiles violate the described bound.

**Qualifying route:** Route B.

**Affected result or extracted value:** Baseline INQoL composite distributions, including whether the displayed values use the stated0–100 composite or a different aggregate scale.

**Why context does not resolve it:** The table and its adjacent footnote give incompatible numeric units/ranges. No summation, transformed score, or alternative upper bound is specified, so the reader cannot identify which score scale produced the displayed quartiles.

**Alternatives and missing definitions:** The values may represent a sum or another transformation while the footnote describes a normalized composite; alternatively one or more printed quartiles may refer to a different scale. The supplied report/protocol does not give a formula that chooses between them.

**Exact human question:** What INQoL scoring range and aggregation produced upper quartiles110.3 and120.0, and which scale should a data extractor attach to the Table1 distributions?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-003 p.6 eTable4 placebo Any2(6%), denominator30 corroborated mainp.8 | 2/30=6.666667%; printed6 interval[5.5,6.5] leaves gap.166667/6=.027778≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.5 Table1 other antimyotonic SCN4A5(46%),n11 | 5/11=45.454545%; printed46 interval[45.5,46.5] leaves gap.045455/46=.000988≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 pp.3,5,8 IVR scale1–9; DOC-003 p.5 patient11 footnote and baseline scores | Zero scores appear below stated minimum1, but same-source footnote explicitly defines0 as symptom absence; no ambiguity about the zero observations or their direction remains. | CONTEXT_RESOLVES |
| DOC-001 p.7 IVR weakness/SCN4A stiffness fitted effects versus period means | Crude differences1.47 and2.06 differ from fitted1.56 and1.89; IVR effects explicitly use mixed models. | MODEL_VERSUS_CRUDE |
| DOC-002 p.27 Table3 historical Kwiecinski NI12+9+9=30 versus p.25 narrative22 | Background historical sample sizes; no current primary/key secondary value, analysis-population size or decision rule depends on the comparison. | PERIPHERAL_COMPARISON |
| DOC-002 p.29 historical classIA OR1.19% | Isolated percent notation conflicts with odds-ratio units but the quantity is evident from OR label and interval; no printed digit changes. | NOTATION_OR_TYPOGRAPHY |

## Completion record

NUMERIC_CHECK_COMPLETE for all89 canonical relationships. Every supplied unit is mapped; all participant flow, sex, genotype, safety, simulation totals and within-display percentages checked. Each table-family relationship retains all original cells via explicit complete mapper row locators. Main/supplement baseline descriptive copies were reviewed but are peripheral unless affecting analysis populations; no attempt to reconstruct medians or within-patient tests from aggregate summaries. All inferential and planned-design implications are handed to their assigned fresh lanes for complete statistical and cross-source review.

