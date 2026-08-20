# Numeric Consistency Review

## Scope and method

Independent fresh-source review of all 64 canonical relationships: N001-N043 (43) and N1001-N1021 (21). Native/layout extraction was cross-checked against the fresh page renders for the affected eTables/eFigure. Exact fraction checks use the displayed count and denominator; a one-decimal percentage is accepted when it differs from the unrounded percentage by at most 0.05 percentage points. Adjusted-risk differences are checked only against the displayed adjusted risks, while recognizing that model-derived intervals and transformed estimates need not be reconstructible from raw counts. Planned values were not treated as observed results. A display-zero P value alone was not a candidate.

## Explicit N-ID disposition index

Each listed ID was checked under the fuller row-level coverage below. `Checked—none` means no distinct qualifying provisional candidate; candidate references are provisional only.

| N ID | Result | N ID | Result | N ID | Result | N ID | Result |
|---|---|---|---|---|---|---|---|
| N001 | Checked—none | N002 | Checked—none | N003 | Checked—none | N004 | Checked—none |
| N005 | Checked—none | N006 | Checked—none | N007 | Checked—none | N008 | Checked—none |
| N009 | Checked—none | N010 | Checked—none | N011 | Checked—none | N012 | Checked—none |
| N013 | Checked—none | N014 | Checked—none | N015 | Checked—none | N016 | Checked—none |
| N017 | Checked—none | N018 | Checked—none | N019 | Checked—none | N020 | Checked—none |
| N021 | Checked—none | N022 | Checked—none | N023 | Checked—none | N024 | Checked—none |
| N025 | Checked—none | N026 | Checked—none | N027 | Checked—none | N028 | Checked—none |
| N029 | Checked—none | N030 | Checked—none | N031 | Checked—none | N032 | Checked—none |
| N033 | Checked—none | N034 | Checked—none | N035 | Checked—none | N036 | Checked—none |
| N037 | Checked—none | N038 | Checked—none | N039 | Checked—none | N040 | Checked—none |
| N041 | Checked—none | N042 | Checked—none | N043 | Checked—none | N1001 | Checked—none |
| N1002 | Checked—none | N1003 | Checked—none | N1004 | Checked—none | N1005 | Checked—none |
| N1006 | Checked—none | N1007 | Checked—none | N1008 | Checked—none | N1009 | NUM-CAND-001 |
| N1010 | NUM-CAND-002 | N1011 | NUM-CAND-003 | N1012 | Checked—none | N1013 | Checked—none |
| N1014 | Checked—none | N1015 | Checked—none | N1016 | Checked—none | N1017 | Checked—none |
| N1018 | Checked—none | N1019 | Checked—none | N1020 | Checked—none | N1021 | NUM-CAND-004 |

## Complete relationship-level check coverage

| IDs checked | Checks applied | Result |
|---|---|---|
| N001-N013 | repeated design/date identity; planning totals; time, outcome-direction, odds-ratio/aRD scale and population labels | No qualifying inconsistency. N012 and N1001/N1007 planning identities reconcile (16x100=1600; 4x400=1600; 80%x400=320). |
| N014 | site-flow components and total | No candidate: 6+8+2=16; 32-16=16. |
| N015 | all G1 flow transitions, ineligibility components, hospital summary/range | No candidate: 73+45+3+6+16=143; 740+143=883; 740-153=587; 587-187=400; 389+11=400; 305+95=400. |
| N016 | all G2 flow transitions, components, hospital summary/range | No candidate: 100+81+15+23+17=236; 585+236=821; 585-43=542; 542-142=400; 399+1=400; 303+97=400. |
| N017 | all G3 flow transitions, components, hospital summary/range | No candidate: 72+45+7+12+4=140; 936+140=1076; 936-117=819; 819-419=400; 397+3=400; 335+65=400. |
| N018 | all G4 flow transitions, components, hospital summary/range | No candidate: 129+110+14+14+10=277; 676+277=953; 676-74=602; 602-202=400; 395+5=400; 320+80=400. |
| N019 | aggregate arm flow, proportion, enablement total | No candidate: assessed=3733, eligible=2937, completed=1263, lost=337 and enablement failures=20 all sum from N015-N018; 2937/3733=78.67%, displayed 78.7%. |
| N020-N027 | every Table 1 arm/category count sum, one-decimal percent, unknown/missingness label, and respondent aggregate | No qualifying inconsistency. Each displayed category sum matches 305/303/335/320 when an explicit unknown row is supplied; fractions reproduce the displayed percentages within rounding. |
| N028 | loss threshold, observed label, imputation count | No candidate: planned `>20%` trigger and descriptive `approximately 20%` observed loss are not contradictory. |
| N029-N032 | SAFE arm and total numerators/denominators, fractions, outcome definitions | No candidate. Each total numerator/denominator is the sum of its four displayed arms and fractions round to the printed percent. Different outcome-specific denominators are appropriately distinguished. |
| N033-N036 | recruitment flow, percent, outcome and abstract/Table 3 repetitions | No candidate: 2937-387=2550; 2550-? consent/refusal pathway is consistent with the Figure; 1600/2550=62.75% (62.7% displayed); 1263/1600=78.94% (78.9% displayed). The four narrative aR/aRD results reproduce abstract and Table 3 after matching mHealth main-effect context. |
| N037-N038 | all Table 3 raw count/denominator/percent cells, arm position, outcome labels | No candidate. All 16 fractions reproduce their printed one-decimal percentages within tolerance; different denominators by outcome are labeled and are not interchanged. |
| N039-N041 | adjusted-risk subtraction, CI order, control/intervention and interaction labels | No candidate. Examples: 78.5-80.2=-1.7; 82.8-80.2=2.6; 89.6-80.2=9.4. Every displayed aRD is between its ordered CI bounds; model footnotes identify transformed estimates. |
| N042-N043 | model/transform/repeated value, response/loss bounds and unit labels | No qualifying inconsistency. 917/1263=72.60% supports the main paper's 72.6% statement; the separately displayed supplement value is addressed in NUM-CAND-001. |
| N1001-N1008 | protocol allocation, approximate recruitment yield, response projection, timing, factorial/model labels | No candidate. `~160x.85x.75=102` is compatible with approximate target 100; these are projections, not observed denominators. |
| N1009 | respondent/nonrespondent total and follow-up-age count/proportion | Provisional candidate NUM-CAND-001 (the 917/1263 percentage). All counts otherwise reconcile: 1263+337=1600 and 917+172+87+87=1263. |
| N1010 | eTable 2 category sums, denominators, percentages, P-value/display labels | Provisional candidate NUM-CAND-002 (unlabeled row-specific denominators/missingness in education and marital status). Other category rows reconcile. |
| N1011 | eTable 3 group totals, category sums, percentages and declared column N | Provisional candidate NUM-CAND-003 (unlabeled row-specific denominators/missingness for specified race, education and marital rows). Other rows reconcile. |
| N1012-N1015 | four imputed cells/outcome: count/400 and percent; imputation/definition labels | No candidate. Every printed percentage reproduces its count/400 within tolerance. |
| N1016 | aR/aRD definition, covariate/SAFE-rate exception, rate-versus-count | No candidate. The footnote explicitly distinguishes model-derived aR/aRD from raw counts and identifies the soft-bedding SAFE-rate exception. |
| N1017-N1020 | every eTable 5 stratum count/denominator/percent, subgroup aggregate and outcome labels | All checked eTable 5 fractions reproduce their displayed percentages within tolerance except the N1018 all-race control room-sharing cell, where 205/291 is printed as 70.5%; that matched conflict is registered as C001 through the cross-source and statistical lanes. The `All` denominator appropriately differs by outcome and equals the sum of displayed race-stratum denominators where shown. |
| N1021 | exact eTable/eFigure age eligibility label, plot/table identity and axis scale | Provisional candidate NUM-CAND-004 (incompatible `>=60` versus `>60` labels). |

## Provisional document-grounded candidates

### NUM-CAND-001 — eTable 2 follow-up-age percentage conflicts with its printed count/denominator and main article

- **Exact locations:** [DOC-003#page=3](../../../joi170077supp2_prod.pdf#page=3), eTable 2, `Respondent infant age at follow-up`, 8-11 weeks: `917 (72.7)`; [DOC-001#page=5](../../../jama_moon_2017_oi_170077.pdf#page=5), Table 1, 8-11-week counts 205+214+262+236=917; [DOC-001#page=8](../../../jama_moon_2017_oi_170077.pdf#page=8), `72.6%` aged 8 to 12 weeks.
- **Direct observation:** eTable 2 declares respondent N=1263 and prints 917 (72.7%) for the 8-11-week row. Table 1 arm counts independently total 917; the main text prints 72.6%.
- **Rule and calculation:** `917 / 1263 x 100 = 72.6049%`, which rounds to **72.6%** at one decimal under a maximum rounding tolerance of 0.05 percentage points. Displayed 72.7% is 0.0951 points away; it does not round from the printed count and denominator.
- **Alternative considered:** a non-1263 denominator could yield 72.7%, but the same eTable's age rows total 1263 and the table identifies respondents as N=1263. The main-table aggregation corroborates the count, not an alternate denominator.
- **Quality-control relevance:** internally inconsistent percentage reporting can affect evidence extraction and pooled descriptive denominators.
- **Human question:** Should eTable 2's 8-11-week percentage be corrected to 72.6%, or is one printed count/denominator different from the analyzed value?

### NUM-CAND-002 — eTable 2 omits row-specific denominators/missingness while labeling respondent and nonrespondent columns by their full totals

- **Exact location:** [DOC-003#page=3](../../../joi170077supp2_prod.pdf#page=3), eTable 2, education and marital-status rows; heading identifies respondents N=1263, nonrespondents N=337, total N=1600.
- **Direct observation:** Education counts sum to respondent/nonrespondent/total **1258/336/1594**, not 1263/337/1600; marital-status counts sum to **1248/332/1580**, not 1263/337/1600. Neither variable displays an unknown/missing category or a row-specific denominator.
- **Rule and calculation:** education has unaccounted differences **5/1/6**; marital status has **15/5/20**. The printed percentages demonstrate use of the reduced denominators: education `88/1258=7.00%`, and marital `640/1248=51.28%`, matching printed 7.0% and 51.3%, rather than full-column denominators (`88/1263=7.0%`; `640/1263=50.7%`).
- **Alternative considered:** implicit missing observations could be intended. This does not resolve the printed table's lack of explicit missingness or row-specific denominators, which makes the percentage bases nontransparent.
- **Quality-control relevance:** unlabelled denominator changes can lead secondary users to misinterpret reported proportions or reconstruct comparisons incorrectly.
- **Human question:** What are the intended education and marital-status denominators, and should eTable 2 identify missing data (or provide row-specific N) for each respondent-status column?

### NUM-CAND-003 — eTable 3 reports selected characteristic percentages on reduced, unlabeled denominators despite full group N headings

- **Exact location:** [DOC-003#page=5](../../../joi170077supp2_prod.pdf#page=5), eTable 3 headings N=417/387/421/379 and rows `Race/Ethnicity`, `Mother's Education`, and `Marital Status`.
- **Direct observation and calculation:** Race in BF/BF sums `155+110+99+52=416`, one short of N=417; `155/416=37.26%` gives the printed 37.3%, whereas `155/417=37.17%` rounds to 37.2%. Education in SS/SS sums `51+87+123+116=377`, two short of N=379; `51/377=13.53%` gives printed 13.5%. Marital status sums to **414** in BF/BF (short 3), **419** in BF-NQI/SS-mHealth (short 2), and **377** in SS/SS (short 2); e.g., `232/414=56.04%` gives printed 56.0%.
- **Rule:** category counts should either sum to the declared group denominator when categories are exhaustive, or the table must disclose a missing/unknown category or row-specific denominator. Here the printed percentages use reduced denominators, but the only denominators displayed are the larger group headings.
- **Alternative considered:** data may be missing for these characteristics. That explains the arithmetic but not the absent missingness indicator/row denominator; other eTable 3 variables do sum to their heading N.
- **Quality-control relevance:** the labeled denominator/percentage-base mismatch risks erroneous baseline-rate reconstruction and cross-table comparison.
- **Human question:** Were observations missing for these eTable 3 characteristics, and should the table add row-specific denominators or explicit missing categories (including 416 for BF/BF race, 377 for SS/SS education, and 414/419/377 for marital status)?

### NUM-CAND-004 — eFigure and eTable 5 give nonidentical infant-age eligibility boundaries for the same plotted comparison

- **Exact locations:** [DOC-003#page=9](../../../joi170077supp2_prod.pdf#page=9), eTable 5 title: `when infant was >=60 days of age`; [DOC-003#page=11](../../../joi170077supp2_prod.pdf#page=11), eFigure title: `when infant was >60 days of age`, with footnote directing readers to eTable 5 for sample sizes.
- **Direct observation:** The eFigure portrays the same four outcomes and control versus combined safe-sleep comparison as eTable 5, but one label includes infants exactly 60 days old and the other excludes them.
- **Rule:** a tabular result and the plot said to display its sample sizes should carry the same analysis eligibility boundary. `age >=60 days` and `age >60 days` are non-equivalent definitions; no rounding tolerance applies to an inequality label.
- **Alternative considered:** the difference may be a typographical label rather than a different analytic population. The supplied sources do not state whether any infants were exactly 60 days old, so the numerical impact cannot be inferred.
- **Quality-control relevance:** eligibility-boundary ambiguity can alter which observations are understood to underlie a displayed subgroup result.
- **Human question:** Which age criterion generated the eTable 5/eFigure data, and should one label be aligned to the other?

## Limitations

This is a document-consistency review, not a raw-data or methodological audit. It cannot determine the intended missing-data handling or whether infants were exactly 60 days old. No external sources, prior audit derivatives, or OCR-derived values were used.
