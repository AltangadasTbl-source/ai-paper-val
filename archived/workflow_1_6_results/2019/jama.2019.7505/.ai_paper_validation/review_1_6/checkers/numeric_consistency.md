# Numeric consistency checker: narrative and baseline

Fresh numeric baseline checker runtime01a1286a-d1a0-78a3-b596-ad02e44f539b, fixed gpt-6.1-sol/medium. Scope102 compound mapping records: M01-M28/B01-B74, stable N001-N102. All completed; no stopping or candidate-count target. Every compared location below is REPORT by content (main trial article); no PLAN discrepancy is introduced by background corroboration. Candidates use local keys only; no stable C IDs, severity, validity or disposition assigned. All require human adjudication. Independent checker shards may emit the same narrative/outcome identities; merge only exact comparator/rule duplicates while preserving these narrative locations.

Methods: direct Poppler26.01.0 layout text from source PDF pp.1-6,9-10; reusable source-matched Table1 images pp.5-6 visually inspected. The map supplied page-linked narrative locators pp.8,11-12. All calculations use printed integers and arithmetic; conventional rounding tolerance is±0.05 percentage point for one decimal and±0.005 for two-decimal RR. Bounds are diagnostic display assumptions, not claimed undocumented study conventions. Counts/labels/exact matched signs use zero tolerance. Complete no-candidate checks and missingness alternatives are in the inventory. No web, old conclusions, raw data, GPU or Python scientific review.

## Compact candidate index

| Local key | Exact row/location | Printed inputs | Comparator rule | Suggested primary category |
|---|---|---|---|---|
| NB-PCT-B32-H | Table1 PDF p.5, Reflux,n/N(%), H | 332/986, 33.6% | 100×n/N=33.671399594%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B33-H | Table1 PDF p.5, Diabetes,n/N(%), H | 294/988, 29.7% | 100×n/N=29.757085020%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B34-H | Table1 PDF p.5, Diabetes oral medication,n/N(%), H | 209/294, 71.0% | 100×n/N=71.088435374%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B36-L | Table1 PDF p.5, Obstructive sleep apnea,No.(%), L | 264/987, 26.8% | 100×n/N=26.747720365%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B37-H | Table1 PDF p.5, Tobacco never,n/N(%), H | 549/987, 55.5% | 100×n/N=55.623100304%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B37-L | Table1 PDF p.5, Tobacco never,n/N(%), L | 525/985, 53.2% | 100×n/N=53.299492386%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B38-H | Table1 PDF p.5, Tobacco previous,n/N(%), H | 273/987, 27.6% | 100×n/N=27.659574468%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B39-L | Table1 PDF p.5, Tobacco current,n/N(%), L | 186/985, 18.8% | 100×n/N=18.883248731%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B63-H | Table1 PDF p.6, Antibiotic prophylaxis,n/N(%), H | 938/987, 94.8% | 100×n/N=95.035460993%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-PCT-B63-L | Table1 PDF p.6, Antibiotic prophylaxis,n/N(%), L | 949/985, 96.1% | 100×n/N=96.345177665%; nearest-one-decimal±0.05 | Denominator, proportion, or total inconsistency |
| NB-ALLOC | Abstract INTERVENTIONS p.1 vs Figure1 p.3 |989/987 vs1011/1002 |Exact randomized population identity | Analysis-unit or population inconsistency |
| NB-HYPO-CI | Abstract p.1 vs Table3 p.9 hypoxemia |95%CI upper+6.1 vs−6.1 |Matched endpoint/sign equality | Cross-document numeric inconsistency |
| NB-APPROACH | Table1 p.6 abdominal/nonabdominal |H894/986 vs92/987;L884/987 vs102/986 |Complementary categories share observed denominator | Denominator, proportion, or total inconsistency |
| NB-RR-PPC | Abstract p.1/narrative p.8/Table3 p.9/Figure2 p.10 |211/989 vs233/987;RR0.93 |Risk ratio identity gives0.903748096 | Measure, label, or scale inconsistency |
| NB-RR-HYPO | Table3 p.9/abstract risk repeat p.1 |49/989 vs134/987;RR0.51 |Risk ratio identity gives0.364932164 | Measure, label, or scale inconsistency |
| NB-RR-MILD | Narrative p.8/Table3 p.9 |135/989 vs154/987;RR0.92 |Risk ratio identity gives0.874850630 | Measure, label, or scale inconsistency |
| NB-RR-EFFUSION | Narrative p.8/Table3 p.9 |43/989 vs21/987;RR1.35 |Risk ratio identity gives2.043478261 | Measure, label, or scale inconsistency |
| NB-MILD-DIFF | Narrative p.8/Table3 p.9 |135/989 vs154/987;difference−1.9 |Count risk difference−1.952685 exceeds±0.05 | Numeric or arithmetic inconsistency |


## Candidates

### NB-PCT-B32-H: Reflux,n/N(%), high group

- Relationship: N060; mapped B32. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Reflux,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 332/986 (33.6%); explicit denominator 986.
- Reproducible rule/calculation: patient percentage=100×n/N;100×332/986=33.671399594%, which rounds to33.7% under nearest-one-decimal rounding. Printed33.6% differs by0.071399594 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Reflux,n/N(%) percentage33.6%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B33-H: Diabetes,n/N(%), high group

- Relationship: N061; mapped B33. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Diabetes,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 294/988 (29.7%); explicit denominator 988.
- Reproducible rule/calculation: patient percentage=100×n/N;100×294/988=29.757085020%, which rounds to29.8% under nearest-one-decimal rounding. Printed29.7% differs by0.057085020 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Diabetes,n/N(%) percentage29.7%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B34-H: Diabetes oral medication,n/N(%), high group

- Relationship: N062; mapped B34. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Diabetes oral medication,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 209/294 (71.0%); explicit denominator 294.
- Reproducible rule/calculation: patient percentage=100×n/N;100×209/294=71.088435374%, which rounds to71.1% under nearest-one-decimal rounding. Printed71.0% differs by0.088435374 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Diabetes oral medication,n/N(%) percentage71.0%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B36-L: Obstructive sleep apnea,No.(%), low group

- Relationship: N064; mapped B36. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Obstructive sleep apnea,No.(%), L cell numerator/denominator; REPORT same cell percentage; REPORT same-page group header L n=987 and footnote a on p.6.
- Printed inputs: 264 (26.8%); header population 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×264/987=26.747720365%, which rounds to26.7% under nearest-one-decimal rounding. Printed26.8% differs by0.052279635 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell and header values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: footnote a permits unreported variable-specific missingness; an undocumented denominator could account for a small display difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Obstructive sleep apnea,No.(%) percentage26.8%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B37-H: Tobacco never,n/N(%), high group

- Relationship: N065; mapped B37. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco never,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 549/987 (55.5%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×549/987=55.623100304%, which rounds to55.6% under nearest-one-decimal rounding. Printed55.5% differs by0.123100304 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Tobacco never,n/N(%) percentage55.5%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B37-L: Tobacco never,n/N(%), low group

- Relationship: N065; mapped B37. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco never,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 525/985 (53.2%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×525/985=53.299492386%, which rounds to53.3% under nearest-one-decimal rounding. Printed53.2% differs by0.099492386 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Tobacco never,n/N(%) percentage53.2%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B38-H: Tobacco previous,n/N(%), high group

- Relationship: N066; mapped B38. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco previous,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 273/987 (27.6%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×273/987=27.659574468%, which rounds to27.7% under nearest-one-decimal rounding. Printed27.6% differs by0.059574468 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Tobacco previous,n/N(%) percentage27.6%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B39-L: Tobacco current,n/N(%), low group

- Relationship: N067; mapped B39. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco current,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 186/985 (18.8%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×186/985=18.883248731%, which rounds to18.9% under nearest-one-decimal rounding. Printed18.8% differs by0.083248731 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Tobacco current,n/N(%) percentage18.8%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B63-H: Antibiotic prophylaxis,n/N(%), high group

- Relationship: N091; mapped B63. Compared locations and roles: REPORT [main PDF p.6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Antibiotic prophylaxis,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 938/987 (94.8%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×938/987=95.035460993%, which rounds to95.0% under nearest-one-decimal rounding. Printed94.8% differs by0.235460993 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Antibiotic prophylaxis,n/N(%) percentage94.8%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B63-L: Antibiotic prophylaxis,n/N(%), low group

- Relationship: N091; mapped B63. Compared locations and roles: REPORT [main PDF p.6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Antibiotic prophylaxis,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 949/985 (96.1%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×949/985=96.345177665%, which rounds to96.3% under nearest-one-decimal rounding. Printed96.1% differs by0.245177665 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Antibiotic prophylaxis,n/N(%) percentage96.1%, and which printed component should be used when the cell is reconciled?

### NB-ALLOC: abstract randomized-group populations equal analyzed populations

- Relationships:N002,N007,N008.
- Compared locations and roles: REPORT [main PDF p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), abstract INTERVENTIONS, “Patients were randomized” H n=989/L n=987; REPORT [main PDF p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), Figure1 allocated H1011/L1002 and primary-analysis H989/L987; REPORT [main PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Results2013 randomized and1976 analyzed.
- Printed inputs:989,987 vs1011,1002;2013 randomized;1976 analyzed.
- Rule/calculation: randomized group counts should describe the same allocation population;989+987=1976 vs1011+1002=2013. Differences22 high and15 low sum37, equal2013−1976.
- Tolerance:zero for exact counts and population labels.
- Direct observation: identical abstract and Figure1 analysis counts are called randomized in the abstract; flow separately labels the larger randomized counts. Inference: abstract may have inserted analysis sizes into intervention description.
- Alternatives: abstract may conventionally summarize treatment groups using their analyzed sizes; that resolves the intended referent if expressly relabeled, but does not make the literal allocation populations equal.
- Quality-control relevance: extraction of allocated versus analyzed denominators may differ by37 patients.
- Exact human question: Should the abstract INTERVENTIONS group sizes describe randomized allocation1011/1002 or analyzed patients989/987?

### NB-HYPO-CI: matched hypoxemia confidence-limit sign differs

- Relationship:N005.
- Compared locations and roles: REPORT [main PDF p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), abstract Results hypoxemia difference−8.6%,95%CI−11.1% to positive6.1%,P<.001; REPORT [main PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 hypoxemia same difference−8.6%,95%CI−11.1 to−6.1,P<.001.
- Printed inputs:upper endpoint+6.1 versus−6.1; same outcome,groups,time,difference and P.
- Rule/calculation: matching confidence limits should agree at equal display precision;(+6.1)−(−6.1)=12.2 percentage points. Abstract interval crosses0 while Table3 interval does not.
- Tolerance:zero for matched signs; endpoint display±0.05 cannot reconcile12.2.
- Direct observation: sign mismatch; inference: a minus sign may have been omitted. No CI convention needs to be assumed for matched-source equality.
- Alternatives: no distinct model/population is labeled for the abstract estimate; a separate analysis would need identification. Source layout text expressly retains the positive sign.
- Quality-control relevance: interval crossing of the null differs for downstream extraction.
- Exact human question: Which signed upper confidence limit belongs to the abstract hypoxemia difference, and is the abstract intended to reproduce Table3?

### NB-APPROACH: complementary surgical-approach rows switch denominators

- Relationships:N098,N101; contextual N003,N099,N100.
- Compared locations and roles: REPORT [main PDF p.6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Surgical approach “Type of abdominal incision” H894/986(90.7),L884/987(89.6); REPORT same table “Nonabdominal” H92/987(9.3),L102/986(10.3); REPORT same footnotes a (some characteristics missing) and i (abdominal open/endoscopic definitions).
- Printed inputs:high denominators986 versus987;low987 versus986;high counts894+92;low884+102.
- Rule/calculation: abdominal and nonabdominal are complementary labels for one surgical-approach classification and would ordinarily share an observed-population denominator. Both count sums=986, while the displayed denominators alternate986/987. High count sum agrees abdominal denominator986 but differs nonabdominal987 by1; low count sum agrees nonabdominal986 but differs abdominal987 by1. Endoscopic+open sums exactly894/884.
- Tolerance:zero for exact denominators/sums.
- Direct observation: denominator switches and count sums. Inference: denominator transposition or differently missing category indicators; a common underlying population is a label-based assumption.
- Alternatives: independently missing category-specific binary indicators could legitimately use different denominators; footnote a permits missingness but does not describe such separate indicators or explain complementary rows.
- Quality-control relevance: denominator and missingness extraction for surgical approach becomes ambiguous.
- Exact human question: Were abdominal and nonabdominal surgery measured as one mutually exclusive classification; if so what common denominator applies in each group, and if not why do their category-specific denominators differ?

### NB-RR-PPC: labeled risk ratio differs from printed patient-risk ratio

- Relationship:N004. Exact compared locations and roles: REPORT main p.1 abstract Results;p.8 Primary Outcome narrative;Table3 p.9 primary PPC;Figure2 p.10 pooled row; REPORT [main PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 primary pulmonary complications within5days count cells/H989 L987 headers and “Risk Ratio” estimate; REPORT [main PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods binary outcome RR/Wald-likelihood-approximation rule. Additional location links: [p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1),[p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8),[p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Printed inputs:H211/989,L233/987;RR0.93.
- Rule/calculation: unadjusted high-versus-low risk ratio=(H events/H patients)/(L events/L patients)=(211/989)/(233/987)=0.903748096, displaying0.90; printed0.93 differs by0.026251904.
- Tolerance:±0.005 for a two-decimal ratio. Exact patient counts used; direction high/low stated.
- Direct observation versus inference: printed counts and ratio label are direct; arithmetic mismatch follows the ordinary risk-ratio definition. An estimate from another model/population or another effect measure is an inferred possible mechanism.
- Alternatives: covariate/site adjustment, transformation, or a different population could produce another estimate, but none is labeled for this repeated result; Wald CI approximation alone does not redefine the ratio of observed risks. Statistical checkers examine the inferential method and any alternative scale independently.
- Quality-control relevance: effect-size extraction as patient risk ratio differs from reconstructing it from counts, potentially affecting secondary evidence synthesis; no paper-level conclusion asserted.
- Exact human question: What estimand, model, reference group and analysis population generated the printed0.93 “risk ratio” for primary pulmonary complications within5days, and how does it relate to the printed211/989 versus233/987 patient risks?

### NB-RR-HYPO: labeled risk ratio differs from printed patient-risk ratio

- Relationship:N005. Exact compared locations and roles: REPORT main Table3 p.9 hypoxemia;abstract p.1 printed risks5.0%/13.6%; REPORT [main PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 intraoperative hypoxemia count cells/H989 L987 headers and “Risk Ratio” estimate; REPORT [main PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods binary outcome RR/Wald-likelihood-approximation rule. Additional location links: [p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1),[p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8),[p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Printed inputs:H49/989,L134/987;RR0.51.
- Rule/calculation: unadjusted high-versus-low risk ratio=(H events/H patients)/(L events/L patients)=(49/989)/(134/987)=0.364932164, displaying0.36; printed0.51 differs by0.145067836.
- Tolerance:±0.005 for a two-decimal ratio. Exact patient counts used; direction high/low stated.
- Direct observation versus inference: printed counts and ratio label are direct; arithmetic mismatch follows the ordinary risk-ratio definition. An estimate from another model/population or another effect measure is an inferred possible mechanism.
- Alternatives: covariate/site adjustment, transformation, or a different population could produce another estimate, but none is labeled for this repeated result; Wald CI approximation alone does not redefine the ratio of observed risks. Statistical checkers examine the inferential method and any alternative scale independently.
- Quality-control relevance: effect-size extraction as patient risk ratio differs from reconstructing it from counts, potentially affecting secondary evidence synthesis; no paper-level conclusion asserted.
- Exact human question: What estimand, model, reference group and analysis population generated the printed0.51 “risk ratio” for intraoperative hypoxemia, and how does it relate to the printed49/989 versus134/987 patient risks?

### NB-RR-MILD: labeled risk ratio differs from printed patient-risk ratio

- Relationship:N022. Exact compared locations and roles: REPORT main p.8 Primary Outcome narrative;Table3 p.9 mild respiratory failure; REPORT [main PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 mild respiratory failure count cells/H989 L987 headers and “Risk Ratio” estimate; REPORT [main PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods binary outcome RR/Wald-likelihood-approximation rule. Additional location links: [p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1),[p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8),[p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Printed inputs:H135/989,L154/987;RR0.92.
- Rule/calculation: unadjusted high-versus-low risk ratio=(H events/H patients)/(L events/L patients)=(135/989)/(154/987)=0.874850630, displaying0.87; printed0.92 differs by0.045149370.
- Tolerance:±0.005 for a two-decimal ratio. Exact patient counts used; direction high/low stated.
- Direct observation versus inference: printed counts and ratio label are direct; arithmetic mismatch follows the ordinary risk-ratio definition. An estimate from another model/population or another effect measure is an inferred possible mechanism.
- Alternatives: covariate/site adjustment, transformation, or a different population could produce another estimate, but none is labeled for this repeated result; Wald CI approximation alone does not redefine the ratio of observed risks. Statistical checkers examine the inferential method and any alternative scale independently.
- Quality-control relevance: effect-size extraction as patient risk ratio differs from reconstructing it from counts, potentially affecting secondary evidence synthesis; no paper-level conclusion asserted.
- Exact human question: What estimand, model, reference group and analysis population generated the printed0.92 “risk ratio” for mild respiratory failure, and how does it relate to the printed135/989 versus154/987 patient risks?

### NB-RR-EFFUSION: labeled risk ratio differs from printed patient-risk ratio

- Relationship:N023. Exact compared locations and roles: REPORT main p.8 Primary Outcome narrative;Table3 p.9 pleural effusion; REPORT [main PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 pleural effusion count cells/H989 L987 headers and “Risk Ratio” estimate; REPORT [main PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods binary outcome RR/Wald-likelihood-approximation rule. Additional location links: [p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1),[p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8),[p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Printed inputs:H43/989,L21/987;RR1.35.
- Rule/calculation: unadjusted high-versus-low risk ratio=(H events/H patients)/(L events/L patients)=(43/989)/(21/987)=2.043478261, displaying2.04; printed1.35 differs by0.693478261.
- Tolerance:±0.005 for a two-decimal ratio. Exact patient counts used; direction high/low stated.
- Direct observation versus inference: printed counts and ratio label are direct; arithmetic mismatch follows the ordinary risk-ratio definition. An estimate from another model/population or another effect measure is an inferred possible mechanism.
- Alternatives: covariate/site adjustment, transformation, or a different population could produce another estimate, but none is labeled for this repeated result; Wald CI approximation alone does not redefine the ratio of observed risks. Statistical checkers examine the inferential method and any alternative scale independently.
- Quality-control relevance: effect-size extraction as patient risk ratio differs from reconstructing it from counts, potentially affecting secondary evidence synthesis; no paper-level conclusion asserted.
- Exact human question: What estimand, model, reference group and analysis population generated the printed1.35 “risk ratio” for pleural effusion, and how does it relate to the printed43/989 versus21/987 patient risks?

### NB-MILD-DIFF: narrative mild-failure absolute difference is outside nearest-decimal tolerance

- Relationship:N022. Compared locations and roles: REPORT [main PDF p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), Primary Outcome narrative mild respiratory failure135(13.7%) vs154(15.6%), difference−1.9%; REPORT [main PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 same counts,headers989/987,and difference−1.9%.
- Printed inputs:135/989,154/987,−1.9 percentage points.
- Rule/calculation: exact count-based difference=100×135/989−100×154/987=-1.952685211 percentage points, nearest-one-decimal−2.0, differing from−1.9 by0.052685211 point.
- Tolerance:±0.05 point; exceedance approximately0.002685 point beyond tolerance.
- Direct observation: printed counts and difference; reproducible arithmetic. Inference: subtraction of already-rounded13.7−15.6=−1.9 or truncation toward zero can reproduce display.
- Alternatives: deliberate subtraction of rounded group percentages or truncation can explain this very small difference; a modeled difference or alternative denominator is possible but unreported. Preserve that explanation rather than asserting an arithmetic failure under all conventions.
- Quality-control relevance: small precision inconsistency affects mechanically reconstructed risk difference; no clinical consequence inferred.
- Exact human question: Was the−1.9-point mild-failure difference computed from rounded percentages, truncation, raw risks or a modeled estimate, and what display convention should govern its reconciliation?

## Completed coverage and limitations

All102 compound records checked;18 local candidates:10 baseline percentage cells,1 allocation-label comparison,1 CI sign repetition,1 complementary-denominator comparison,4 repeated risk-ratio identities,1 repeated mild-failure difference. Flow,percentages,treatment values,repeated sites/countries,category sums,population totals,continuous scale checks and missingness were examined without general design auditing. No coherent display-zero P occurs in this scope. Statistical inference/sample-size exact reconstruction remains assigned to statistical specialists; missing variance/design conventions do not create unsupported candidates. White-cell scale diagnostic lacks a second matched baseline measurement and is recorded as a limitation in inventory. Missing baseline observed populations cannot be reconstructed from footnote a alone. Candidate rounding checks state conditional display assumptions explicitly. No source changes or scientific coverage gap.



# Numeric consistency checker: outcome tables and subgroup figure

Runtime: 01a1286a-f70e-7670-b0f7-a0db7e2ab04a; gpt-6.1-sol/medium; fresh auxiliary numeric checker. Exact scope: T01–T59, O01–O45, F01–F11 and five Figure 2 partition relationships, N121–N240. Complete printed inputs and 120 relationship checks are in numeric_inventory_outcomes.md. This file emits 59 candidate occurrences for coordinator genuine-duplicate consolidation; no stable candidate IDs, severity, validity, evidence-state or disposition is assigned. All compared documents are the main REPORT by content. Source PDF physical pp.7–10 directly inspected in Poppler layout extraction and source-matched page renders. No old candidate/report conclusions used.

## Candidate index

| Local key | Exact source row | Printed values | Comparator/rule | Proposed primary category |
|---|---|---|---|---|
| NUM-O01-RR | O01; PDF p.9 | H 211/989; L 233/987; printed RR0.93(0.83 to1.04) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (211/989)/(233/987) = 0.903748; printed point = 0.93. Nearest two-decimal identity display would be 0.90; discrepancy=0.026252. | Measure, label, or scale inconsistency |
| NUM-O02-RR | O02; PDF p.9 | H 135/989; L 154/987; printed RR0.92(0.80 to1.05) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (135/989)/(154/987) = 0.874851; printed point = 0.92. Nearest two-decimal identity display would be 0.87; discrepancy=0.045149. | Measure, label, or scale inconsistency |
| NUM-O03-RR | O03; PDF p.9 | H 42/989; L 58/987; printed RR0.83(0.65 to1.05) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (42/989)/(58/987) = 0.722674; printed point = 0.83. Nearest two-decimal identity display would be 0.72; discrepancy=0.107326. | Measure, label, or scale inconsistency |
| NUM-O04-RR | O04; PDF p.9 | H 30/989; L 36/987; printed RR0.90(0.69 to1.18) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (30/989)/(36/987) = 0.831648; printed point = 0.90. Nearest two-decimal identity display would be 0.83; discrepancy=0.068352. | Measure, label, or scale inconsistency |
| NUM-O05-RR | O05; PDF p.9 | H 44/989; L 55/987; printed RR0.88(0.70 to1.10) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (44/989)/(55/987) = 0.798382; printed point = 0.88. Nearest two-decimal identity display would be 0.80; discrepancy=0.081618. | Measure, label, or scale inconsistency |
| NUM-O06-RR | O06; PDF p.9 | H 43/989; L 21/987; printed RR1.35(1.14 to1.62) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (43/989)/(21/987) = 2.043478; printed point = 1.35. Nearest two-decimal identity display would be 2.04; discrepancy=-0.693478. | Measure, label, or scale inconsistency |
| NUM-O07-RR | O07; PDF p.9 | H 14/989; L 18/987; printed RR0.87(0.59 to1.29) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (14/989)/(18/987) = 0.776205; printed point = 0.87. Nearest two-decimal identity display would be 0.78; discrepancy=0.093795. | Measure, label, or scale inconsistency |
| NUM-O08-RR | O08; PDF p.9 | H 17/989; L 9/987; printed RR1.31(0.99 to1.74) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (17/989)/(9/987) = 1.885069; printed point = 1.31. Nearest two-decimal identity display would be 1.89; discrepancy=-0.575069. | Measure, label, or scale inconsistency |
| NUM-O09-RR | O09; PDF p.9 | H 12/989; L 10/987; printed RR1.09(0.74 to1.60) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (12/989)/(10/987) = 1.197573; printed point = 1.09. Nearest two-decimal identity display would be 1.20; discrepancy=-0.107573. | Measure, label, or scale inconsistency |
| NUM-O10-RR | O10; PDF p.9 | H 10/989; L 10/987; printed RR0.99(0.64 to1.55) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (10/989)/(10/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978. | Measure, label, or scale inconsistency |
| NUM-O11-RR | O11; PDF p.9 | H 2/989; L 1/987; printed RR1.33(0.60 to2.97) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (2/989)/(1/987) = 1.995956; printed point = 1.33. Nearest two-decimal identity display would be 2.00; discrepancy=-0.665956. | Measure, label, or scale inconsistency |
| NUM-O12-RR | O12; PDF p.9 | H 3/989; L 1/987; printed RR1.50(0.85 to2.64) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (3/989)/(1/987) = 2.993933; printed point = 1.50. Nearest two-decimal identity display would be 2.99; discrepancy=-1.493933. | Measure, label, or scale inconsistency |
| NUM-O13-RR | O13; PDF p.9 | H 1/989; L 3/987; printed RR0.50(0.09 to2.72) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (1/989)/(3/987) = 0.332659; printed point = 0.50. Nearest two-decimal identity display would be 0.33; discrepancy=0.167341. | Measure, label, or scale inconsistency |
| NUM-O14-RR | O14; PDF p.9 | H 116/989; L 134/987; printed RR0.91(0.80 to1.05) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (116/989)/(134/987) = 0.863921; printed point = 0.91. Nearest two-decimal identity display would be 0.86; discrepancy=0.046079. | Measure, label, or scale inconsistency |
| NUM-O15-RR | O15; PDF p.9 | H 167/989; L 150/987; printed RR1.06(0.95 to1.19) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (167/989)/(150/987) = 1.111082; printed point = 1.06. Nearest two-decimal identity display would be 1.11; discrepancy=-0.051082. | Measure, label, or scale inconsistency |
| NUM-O16-RR | O16; PDF p.9 | H 93/989; L 83/987; printed RR1.06(0.91 to1.22) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (93/989)/(83/987) = 1.118216; printed point = 1.06. Nearest two-decimal identity display would be 1.12; discrepancy=-0.058216. | Measure, label, or scale inconsistency |
| NUM-O17-RR | O17; PDF p.9 | H 18/989; L 15/987; printed RR1.09(0.79 to1.49) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (18/989)/(15/987) = 1.197573; printed point = 1.09. Nearest two-decimal identity display would be 1.20; discrepancy=-0.107573. | Measure, label, or scale inconsistency |
| NUM-O18-RR | O18; PDF p.9 | H 7/989; L 10/987; printed RR0.82(0.46 to1.45) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (7/989)/(10/987) = 0.698584; printed point = 0.82. Nearest two-decimal identity display would be 0.70; discrepancy=0.121416. | Measure, label, or scale inconsistency |
| NUM-O19-RR | O19; PDF p.9 | H 7/989; L 8/987; printed RR0.93(0.54 to1.60) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (7/989)/(8/987) = 0.873231; printed point = 0.93. Nearest two-decimal identity display would be 0.87; discrepancy=0.056769. | Measure, label, or scale inconsistency |
| NUM-O20-RR | O20; PDF p.9 | H 65/989; L 56/987; printed RR1.07(0.90 to1.28) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (65/989)/(56/987) = 1.158367; printed point = 1.07. Nearest two-decimal identity display would be 1.16; discrepancy=-0.088367. | Measure, label, or scale inconsistency |
| NUM-O25-RR | O25; PDF p.9 | H 31/989; L 32/987; printed RR0.98(0.76 to1.26) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (31/989)/(32/987) = 0.966791; printed point = 0.98. Nearest two-decimal identity display would be 0.97; discrepancy=0.013209. | Measure, label, or scale inconsistency |
| NUM-O30-RR | O30; PDF p.9 | H 29/989; L 23/987; printed RR1.11(0.87 to1.42) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (29/989)/(23/987) = 1.258320; printed point = 1.11. Nearest two-decimal identity display would be 1.26; discrepancy=-0.148320. | Measure, label, or scale inconsistency |
| NUM-O31-RR | O31; PDF p.9 | H 9/989; L 9/987; printed RR0.99(0.63 to1.59) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (9/989)/(9/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978. | Measure, label, or scale inconsistency |
| NUM-O32-RR | O32; PDF p.9 | H 2/989; L 2/987; printed RR0.99(0.37 to2.66) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (2/989)/(2/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978. | Measure, label, or scale inconsistency |
| NUM-O33-RR | O33; PDF p.9 | H 1/989; L 0/987; printed RR2.00(1.91 to2.09) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (1/989)/(0/987) = undefined because the control-event risk is zero; printed point = 2.00. A finite value2.00 requires an additional estimator/continuity rule. | Measure, label, or scale inconsistency |
| NUM-O35-RR | O35; PDF p.9 | H 22/989; L 26/987; printed RR0.91(0.66 to1.24) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (22/989)/(26/987) = 0.844443; printed point = 0.91. Nearest two-decimal identity display would be 0.84; discrepancy=0.065557. | Measure, label, or scale inconsistency |
| NUM-O36-RR | O36; PDF p.9 | H 41/989; L 32/987; printed RR1.12(0.91 to1.38) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (41/989)/(32/987) = 1.278659; printed point = 1.12. Nearest two-decimal identity display would be 1.28; discrepancy=-0.158659. | Measure, label, or scale inconsistency |
| NUM-O39-RR | O39; PDF p.9 | H 49/989; L 134/987; printed RR0.51(0.40 to0.65) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (49/989)/(134/987) = 0.364932; printed point = 0.51. Nearest two-decimal identity display would be 0.36; discrepancy=0.145068. | Measure, label, or scale inconsistency |
| NUM-O40-RR | O40; PDF p.9 | H 313/989; L 170/987; printed RR1.43(1.31 to1.56) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (313/989)/(170/987) = 1.837453; printed point = 1.43. Nearest two-decimal identity display would be 1.84; discrepancy=-0.407453. | Measure, label, or scale inconsistency |
| NUM-O41-RR | O41; PDF p.9 | H 98/989; L 59/987; printed RR1.27(1.11 to1.45) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (98/989)/(59/987) = 1.657658; printed point = 1.27. Nearest two-decimal identity display would be 1.66; discrepancy=-0.387658. | Measure, label, or scale inconsistency |
| NUM-O42-RR | O42; PDF p.9 | H 12/989; L 5/987; printed RR1.41(0.95 to1.81) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (12/989)/(5/987) = 2.395147; printed point = 1.41. Nearest two-decimal identity display would be 2.40; discrepancy=-0.985147. | Measure, label, or scale inconsistency |
| NUM-O43-RR | O43; PDF p.10 | H 59/989; L 166/987; printed RR0.49(0.39 to0.62) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (59/989)/(166/987) = 0.354703; printed point = 0.49. Nearest two-decimal identity display would be 0.35; discrepancy=0.135297. | Measure, label, or scale inconsistency |
| NUM-O44-RR | O44; PDF p.10 | H 491/989; L 439/987; printed RR1.10(1.01 to1.21) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (491/989)/(439/987) = 1.116189; printed point = 1.10. Nearest two-decimal identity display would be 1.12; discrepancy=-0.016189. | Measure, label, or scale inconsistency |
| NUM-F01-RR | F01; PDF p.10 | H 79/240; L 74/253; printed 1.09(0.90-1.32) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (79/240)/(74/253) = 1.125394; printed point = 1.09. Nearest two-decimal identity display would be 1.13; discrepancy=-0.035394. | Measure, label, or scale inconsistency |
| NUM-F02-RR | F02; PDF p.10 | H 130/740; L 156/727; printed 0.88(0.77-1.01) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (130/740)/(156/727) = 0.818694; printed point = 0.88. Nearest two-decimal identity display would be 0.82; discrepancy=0.061306. | Measure, label, or scale inconsistency |
| NUM-F03-RR | F03; PDF p.10 | H 76/336; L 94/376; printed 0.93(0.77-1.13) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (76/336)/(94/376) = 0.904762; printed point = 0.93. Nearest two-decimal identity display would be 0.90; discrepancy=0.025238. | Measure, label, or scale inconsistency |
| NUM-F04-RR | F04; PDF p.10 | H 135/653; L 139/611; printed 0.94(0.82-1.08) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (135/653)/(139/611) = 0.908755; printed point = 0.94. Nearest two-decimal identity display would be 0.91; discrepancy=0.031245. | Measure, label, or scale inconsistency |
| NUM-F05-RR | F05; PDF p.10 | H 88/317; L 112/342; printed 0.88(0.74-1.06) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (88/317)/(112/342) = 0.847679; printed point = 0.88. Nearest two-decimal identity display would be 0.85; discrepancy=0.032321. | Measure, label, or scale inconsistency |
| NUM-F06-RR | F06; PDF p.10 | H 123/672; L 121/645; printed 0.99(0.86-1.13) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (123/672)/(121/645) = 0.975686; printed point = 0.99. Nearest two-decimal identity display would be 0.98; discrepancy=0.014314. | Measure, label, or scale inconsistency |
| NUM-F07-RR | F07; PDF p.10 | H 32/126; L 25/126; printed 1.16(0.89-1.53) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (32/126)/(25/126) = 1.280000; printed point = 1.16. Nearest two-decimal identity display would be 1.28; discrepancy=-0.120000. | Measure, label, or scale inconsistency |
| NUM-F08-RR | F08; PDF p.10 | H 179/863; L 208/861; printed 0.90(0.80-1.02) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (179/863)/(208/861) = 0.858583; printed point = 0.90. Nearest two-decimal identity display would be 0.86; discrepancy=0.041417. | Measure, label, or scale inconsistency |
| NUM-F09-RR | F09; PDF p.10 | H 97/467; L 100/457; printed 0.97(0.83-1.13) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (97/467)/(100/457) = 0.949229; printed point = 0.97. Nearest two-decimal identity display would be 0.95; discrepancy=0.020771. | Measure, label, or scale inconsistency |
| NUM-F10-RR | F10; PDF p.10 | H 98/447; L 112/449; printed 0.92(0.78-1.08) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (98/447)/(112/449) = 0.878915; printed point = 0.92. Nearest two-decimal identity display would be 0.88; discrepancy=0.041085. | Measure, label, or scale inconsistency |
| NUM-F11-RR | F11; PDF p.10 | H 211/989; L 233/987; printed 0.93(0.83-1.04) | RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (211/989)/(233/987) = 0.903748; printed point = 0.93. Nearest two-decimal identity display would be 0.90; discrepancy=0.026252. | Measure, label, or scale inconsistency |
| NUM-T07-RD | T07; PDF p.7 | H 972(98.3); L 11(1.1); difference 97.1(96.1 to98.2) | 100*(972/989−11/987)=97.166604 pp; printed 97.1 pp; discrepancy=-0.066604 pp; nearest one-decimal value=97.2 pp. Displayed percentage subtraction=97.200000 pp. | Numeric or arithmetic inconsistency |
| NUM-T38-PCT-L | T38; PDF p.7 | L 264/987 (26.8%) using header L n987 | 100*264/987=26.747720%; printed 26.8%; discrepancy=0.052280 pp; nearest one-decimal value=26.7%. | Denominator, proportion, or total inconsistency |
| NUM-T38-RD | T38; PDF p.7 | H 274(27.7); L 264(26.8); difference 0.9(−3.0 to4.9) | 100*(274/989−264/987)=0.957032 pp; printed 0.9 pp; discrepancy=-0.057032 pp; nearest one-decimal value=1.0 pp. Displayed percentage subtraction=0.900000 pp. | Numeric or arithmetic inconsistency |
| NUM-T45-PCT-H | T45; PDF p.8 | H 632/982 (64.9%) | 100*632/982=64.358452%; printed 64.9%; discrepancy=0.541548 pp; nearest one-decimal value=64.4%. | Denominator, proportion, or total inconsistency |
| NUM-T45-PCT-L | T45; PDF p.8 | L 651/984 (67.7%) | 100*651/984=66.158537%; printed 67.7%; discrepancy=1.541463 pp; nearest one-decimal value=66.2%. | Denominator, proportion, or total inconsistency |
| NUM-T46-PCT-H | T46; PDF p.8 | H 724/982 (74.3%) | 100*724/982=73.727088%; printed 74.3%; discrepancy=0.572912 pp; nearest one-decimal value=73.7%. | Denominator, proportion, or total inconsistency |
| NUM-T46-PCT-L | T46; PDF p.8 | L 723/984 (75.2%) | 100*723/984=73.475610%; printed 75.2%; discrepancy=1.724390 pp; nearest one-decimal value=73.5%. | Denominator, proportion, or total inconsistency |
| NUM-T46-RD | T46; PDF p.8 | H 724/982(74.3); L 723/984(75.2); difference 0.2(−3.6 to4.1) | 100*(724/982−723/984)=0.251478 pp; printed 0.2 pp; discrepancy=-0.051478 pp; nearest one-decimal value=0.3 pp. Displayed percentage subtraction=-0.900000 pp. It is negative while the reported difference is positive; the count-defined difference itself is positive. | Numeric or arithmetic inconsistency |
| NUM-O02-RD | O02; PDF p.9 | H 135(13.7); L 154(15.6); difference −1.9(−5.1 to1.2) | 100*(135/989−154/987)=-1.952685 pp; printed -1.9 pp; discrepancy=0.052685 pp; nearest one-decimal value=-2.0 pp. Displayed percentage subtraction=-1.900000 pp. | Numeric or arithmetic inconsistency |
| NUM-O28-PCT-H | O28; PDF p.9 | H 7/31 (22.5%) | 100*7/31=22.580645%; printed 22.5%; discrepancy=-0.080645 pp; nearest one-decimal value=22.6%. | Denominator, proportion, or total inconsistency |
| NUM-O29-PCT-H | O29; PDF p.9 | H 2/31 (6.4%) | 100*2/31=6.451613%; printed 6.4%; discrepancy=-0.051613 pp; nearest one-decimal value=6.5%. | Denominator, proportion, or total inconsistency |
| NUM-O43-RD | O43; PDF p.10 | H 59(6.0); L 166(16.8); difference −10.8(−13.6 to−8.1) | 100*(59/989−166/987)=-10.853021 pp; printed -10.8 pp; discrepancy=0.053021 pp; nearest one-decimal value=-10.9 pp. Displayed percentage subtraction=-10.800000 pp. | Numeric or arithmetic inconsistency |
| NUM-T47-ESTIMAND | T47; PDF p.8 | H median1.5L (IQR1.0–2.5); L median1.6L (IQR1.0–2.5); Absolute Difference+0.02L (95%CI−0.11 to0.14),P=.79 | If the difference column subtracts the displayed central statistic, medianH−medianL=1.5−1.6=−0.10L. One-decimal rounded medians permit true median difference from−0.20 to0.00L; the two-decimal+0.02 permits0.015 to0.025L. Those ranges do not overlap. | Measure, label, or scale inconsistency |
| NUM-T30-LABEL | T30/T31/T32; PDF p.7 | Table 2 row heading Heat rate, mean(SD),beats/min; H/L after intubation76.5(15.8)/76.0(14.3), first hour72.6(13.4)/73.1(14.0), last hour73.5(13.0)/74.9(13.8). | A beat count per minute is a cardiac rate measurement; the printed label Heat rate denotes a different physical quantity and is incompatible with beats/min. The same article explicitly calls bradycardia a heart rate measurement in beats/min. | Measure, label, or scale inconsistency |
| NUM-F09-UNIT | F09/F10; PDF p.10 | Figure 2 heading Waist-to-hip ratio,cm; thresholds<1.0/≥1.0; H97/467 and98/447; L100/457 and112/449. | A waist-to-hip ratio equals waist circumference/hip circumference; common length units cancel. Its unit is dimensionless, so cm is incompatible with the ratio label and threshold1.0. | Measure, label, or scale inconsistency |

## Candidate evidence records

### NUM-O01-RR: Primary PPC within5days: labeled RR versus printed patient risks

- **Numeric relationships:** N180.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O01 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 211/989; L 233/987; printed RR0.93(0.83 to1.04). Complete source-row components: Primary PPC within5days; 211(21.3); 233(23.6); −2.3(−5.9 to1.4); RR0.93(0.83 to1.04); .23.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (211/989)/(233/987) = 0.903748; printed point = 0.93. Nearest two-decimal identity display would be 0.90; discrepancy=0.026252.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (211/(211+233))/(778/(1532))=0.935791. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Primary PPC within5days, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.93, and is this value intended as the H/L event risk ratio from 211/989 and 233/987 or a differently defined model quantity?

### NUM-O02-RR: Mild respiratory failure: labeled RR versus printed patient risks

- **Numeric relationships:** N181.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O02 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 135/989; L 154/987; printed RR0.92(0.80 to1.05). Complete source-row components: Mild respiratory failure; 135(13.7); 154(15.6); −1.9(−5.1 to1.2); RR0.92(0.80 to1.05); .22.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (135/989)/(154/987) = 0.874851; printed point = 0.92. Nearest two-decimal identity display would be 0.87; discrepancy=0.045149.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (135/(135+154))/(854/(1687))=0.922769. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Mild respiratory failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.92, and is this value intended as the H/L event risk ratio from 135/989 and 154/987 or a differently defined model quantity?

### NUM-O03-RR: Moderate respiratory failure: labeled RR versus printed patient risks

- **Numeric relationships:** N182.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O03 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 42/989; L 58/987; printed RR0.83(0.65 to1.05). Complete source-row components: Moderate respiratory failure; 42(4.2); 58(5.9); −1.6(−3.6 to0.3); RR0.83(0.65 to1.05); .10.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (42/989)/(58/987) = 0.722674; printed point = 0.83. Nearest two-decimal identity display would be 0.72; discrepancy=0.107326.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (42/(42+58))/(947/(1876))=0.832017. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Moderate respiratory failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.83, and is this value intended as the H/L event risk ratio from 42/989 and 58/987 or a differently defined model quantity?

### NUM-O04-RR: Severe respiratory failure: labeled RR versus printed patient risks

- **Numeric relationships:** N183.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O04 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 30/989; L 36/987; printed RR0.90(0.69 to1.18). Complete source-row components: Severe respiratory failure; 30(3.0); 36(3.6); −0.6(−2.2 to1.0); RR0.90(0.69 to1.18); .45.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (30/989)/(36/987) = 0.831648; printed point = 0.90. Nearest two-decimal identity display would be 0.83; discrepancy=0.068352.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (30/(30+36))/(959/(1910))=0.905299. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Severe respiratory failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.90, and is this value intended as the H/L event risk ratio from 30/989 and 36/987 or a differently defined model quantity?

### NUM-O05-RR: Atelectasis: labeled RR versus printed patient risks

- **Numeric relationships:** N184.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O05 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 44/989; L 55/987; printed RR0.88(0.70 to1.10). Complete source-row components: Atelectasis; 44(4.4); 55(5.6); −1.1(−3.0 to0.8); RR0.88(0.70 to1.10); .25.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (44/989)/(55/987) = 0.798382; printed point = 0.88. Nearest two-decimal identity display would be 0.80; discrepancy=0.081618.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (44/(44+55))/(945/(1877))=0.882775. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Atelectasis, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.88, and is this value intended as the H/L event risk ratio from 44/989 and 55/987 or a differently defined model quantity?

### NUM-O06-RR: Pleural effusion: labeled RR versus printed patient risks

- **Numeric relationships:** N185.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O06 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 43/989; L 21/987; printed RR1.35(1.14 to1.62). Complete source-row components: Pleural effusion; 43(4.3); 21(2.1); 2.2(0.7 to3.8); RR1.35(1.14 to1.62); .005.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (43/989)/(21/987) = 2.043478; printed point = 1.35. Nearest two-decimal identity display would be 2.04; discrepancy=-0.693478.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (43/(43+21))/(946/(1912))=1.357955. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Pleural effusion, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.35, and is this value intended as the H/L event risk ratio from 43/989 and 21/987 or a differently defined model quantity?

### NUM-O07-RR: New pulmonary infiltrates: labeled RR versus printed patient risks

- **Numeric relationships:** N186.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O07 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 14/989; L 18/987; printed RR0.87(0.59 to1.29). Complete source-row components: New pulmonary infiltrates; 14(1.4); 18(1.8); −0.4(−1.5 to0.7); RR0.87(0.59 to1.29); .47.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (14/989)/(18/987) = 0.776205; printed point = 0.87. Nearest two-decimal identity display would be 0.78; discrepancy=0.093795.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (14/(14+18))/(975/(1944))=0.872308. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For New pulmonary infiltrates, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.87, and is this value intended as the H/L event risk ratio from 14/989 and 18/987 or a differently defined model quantity?

### NUM-O08-RR: Cardiopulmonary edema: labeled RR versus printed patient risks

- **Numeric relationships:** N187.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O08 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 17/989; L 9/987; printed RR1.31(0.99 to1.74). Complete source-row components: Cardiopulmonary edema; 17(1.7); 9(0.9); 0.8(−0.2 to1.8); RR1.31(0.99 to1.74); .12.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (17/989)/(9/987) = 1.885069; printed point = 1.31. Nearest two-decimal identity display would be 1.89; discrepancy=-0.575069.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (17/(17+9))/(972/(1950))=1.311728. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Cardiopulmonary edema, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.31, and is this value intended as the H/L event risk ratio from 17/989 and 9/987 or a differently defined model quantity?

### NUM-O09-RR: Bronchospasm: labeled RR versus printed patient risks

- **Numeric relationships:** N188.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O09 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 12/989; L 10/987; printed RR1.09(0.74 to1.60). Complete source-row components: Bronchospasm; 12(1.2); 10(1.0); 0.2(−0.7 to1.1); RR1.09(0.74 to1.60); .67.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (12/989)/(10/987) = 1.197573; printed point = 1.09. Nearest two-decimal identity display would be 1.20; discrepancy=-0.107573.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (12/(12+10))/(977/(1954))=1.090909. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Bronchospasm, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.09, and is this value intended as the H/L event risk ratio from 12/989 and 10/987 or a differently defined model quantity?

### NUM-O10-RR: Pulmonary infection: labeled RR versus printed patient risks

- **Numeric relationships:** N189.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O10 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 10/989; L 10/987; printed RR0.99(0.64 to1.55). Complete source-row components: Pulmonary infection; 10(1.0); 10(1.0); 0(−0.9 to0.9); RR0.99(0.64 to1.55); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (10/989)/(10/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (10/(10+10))/(979/(1956))=0.998979. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Pulmonary infection, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.99, and is this value intended as the H/L event risk ratio from 10/989 and 10/987 or a differently defined model quantity?

### NUM-O11-RR: Aspiration pneumonitis: labeled RR versus printed patient risks

- **Numeric relationships:** N190.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O11 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 2/989; L 1/987; printed RR1.33(0.60 to2.97). Complete source-row components: Aspiration pneumonitis; 2(0.2); 1(0.1); 0.1(−0.2 to0.4); RR1.33(0.60 to2.97); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (2/989)/(1/987) = 1.995956; printed point = 1.33. Nearest two-decimal identity display would be 2.00; discrepancy=-0.665956.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (2/(2+1))/(987/(1973))=1.332658. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Aspiration pneumonitis, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.33, and is this value intended as the H/L event risk ratio from 2/989 and 1/987 or a differently defined model quantity?

### NUM-O12-RR: ARDS: labeled RR versus printed patient risks

- **Numeric relationships:** N191.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O12 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 3/989; L 1/987; printed RR1.50(0.85 to2.64). Complete source-row components: ARDS; 3(0.3); 1(0.1); 0.2(−0.2 to0.6); RR1.50(0.85 to2.64); .62.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (3/989)/(1/987) = 2.993933; printed point = 1.50. Nearest two-decimal identity display would be 2.99; discrepancy=-1.493933.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (3/(3+1))/(986/(1972))=1.500000. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For ARDS, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.50, and is this value intended as the H/L event risk ratio from 3/989 and 1/987 or a differently defined model quantity?

### NUM-O13-RR: Pneumothorax: labeled RR versus printed patient risks

- **Numeric relationships:** N192.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O13 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 1/989; L 3/987; printed RR0.50(0.09 to2.72). Complete source-row components: Pneumothorax; 1(0.1); 3(0.3); −0.2(−0.6 to0.2); RR0.50(0.09 to2.72); .37.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (1/989)/(3/987) = 0.332659; printed point = 0.50. Nearest two-decimal identity display would be 0.33; discrepancy=0.167341.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (1/(1+3))/(988/(1972))=0.498988. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Pneumothorax, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.50, and is this value intended as the H/L event risk ratio from 1/989 and 3/987 or a differently defined model quantity?

### NUM-O14-RR: Severe postoperative PPC: labeled RR versus printed patient risks

- **Numeric relationships:** N193.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O14 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 116/989; L 134/987; printed RR0.91(0.80 to1.05). Complete source-row components: Severe postoperative PPC; 116(11.7); 134(13.6); −1.8(−4.8 to1.1); RR0.91(0.80 to1.05); .22.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (116/989)/(134/987) = 0.863921; printed point = 0.91. Nearest two-decimal identity display would be 0.86; discrepancy=0.046079.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (116/(116+134))/(873/(1726))=0.917370. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Severe postoperative PPC, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.91, and is this value intended as the H/L event risk ratio from 116/989 and 134/987 or a differently defined model quantity?

### NUM-O15-RR: Postoperative extrapulmonary composite: labeled RR versus printed patient risks

- **Numeric relationships:** N194.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O15 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 167/989; L 150/987; printed RR1.06(0.95 to1.19). Complete source-row components: Postoperative extrapulmonary composite; 167(16.9); 150(15.2); 1.7(−1.5 to4.9); RR1.06(0.95 to1.19); .31.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (167/989)/(150/987) = 1.111082; printed point = 1.06. Nearest two-decimal identity display would be 1.11; discrepancy=-0.051082.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (167/(167+150))/(822/(1659))=1.063241. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Postoperative extrapulmonary composite, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.06, and is this value intended as the H/L event risk ratio from 167/989 and 150/987 or a differently defined model quantity?

### NUM-O16-RR: Systemic inflammatory response syndrome: labeled RR versus printed patient risks

- **Numeric relationships:** N195.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O16 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 93/989; L 83/987; printed RR1.06(0.91 to1.22). Complete source-row components: Systemic inflammatory response syndrome; 93(9.4); 83(8.4); 1.0(−1.5 to3.5); RR1.06(0.91 to1.22); .44.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (93/989)/(83/987) = 1.118216; printed point = 1.06. Nearest two-decimal identity display would be 1.12; discrepancy=-0.058216.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (93/(93+83))/(896/(1800))=1.061536. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Systemic inflammatory response syndrome, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.06, and is this value intended as the H/L event risk ratio from 93/989 and 83/987 or a differently defined model quantity?

### NUM-O17-RR: Sepsis: labeled RR versus printed patient risks

- **Numeric relationships:** N196.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O17 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 18/989; L 15/987; printed RR1.09(0.79 to1.49). Complete source-row components: Sepsis; 18(1.8); 15(1.5); 0.3(−0.8 to1.4); RR1.09(0.79 to1.49); .60.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (18/989)/(15/987) = 1.197573; printed point = 1.09. Nearest two-decimal identity display would be 1.20; discrepancy=-0.107573.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (18/(18+15))/(971/(1943))=1.091471. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Sepsis, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.09, and is this value intended as the H/L event risk ratio from 18/989 and 15/987 or a differently defined model quantity?

### NUM-O18-RR: Severe sepsis: labeled RR versus printed patient risks

- **Numeric relationships:** N197.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O18 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 7/989; L 10/987; printed RR0.82(0.46 to1.45). Complete source-row components: Severe sepsis; 7(0.7); 10(1.0); −0.3(−1.1 to0.5); RR0.82(0.46 to1.45); .46.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (7/989)/(10/987) = 0.698584; printed point = 0.82. Nearest two-decimal identity display would be 0.70; discrepancy=0.121416.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (7/(7+10))/(982/(1959))=0.821433. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Severe sepsis, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.82, and is this value intended as the H/L event risk ratio from 7/989 and 10/987 or a differently defined model quantity?

### NUM-O19-RR: Septic shock: labeled RR versus printed patient risks

- **Numeric relationships:** N198.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O19 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 7/989; L 8/987; printed RR0.93(0.54 to1.60). Complete source-row components: Septic shock; 7(0.7); 8(0.8); −0.1(−0.9 to0.7); RR0.93(0.54 to1.60); .79.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (7/989)/(8/987) = 0.873231; printed point = 0.93. Nearest two-decimal identity display would be 0.87; discrepancy=0.056769.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (7/(7+8))/(982/(1961))=0.931908. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Septic shock, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.93, and is this value intended as the H/L event risk ratio from 7/989 and 8/987 or a differently defined model quantity?

### NUM-O20-RR: Gastrointestinal failure: labeled RR versus printed patient risks

- **Numeric relationships:** N199.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O20 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 65/989; L 56/987; printed RR1.07(0.90 to1.28). Complete source-row components: Gastrointestinal failure; 65(6.6); 56(5.7); 0.9(−1.2 to3.0); RR1.07(0.90 to1.28); .40.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (65/989)/(56/987) = 1.158367; printed point = 1.07. Nearest two-decimal identity display would be 1.16; discrepancy=-0.088367.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (65/(65+56))/(924/(1855))=1.078450. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Gastrointestinal failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.07, and is this value intended as the H/L event risk ratio from 65/989 and 56/987 or a differently defined model quantity?

### NUM-O25-RR: Acute kidney failure: labeled RR versus printed patient risks

- **Numeric relationships:** N204.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O25 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 31/989; L 32/987; printed RR0.98(0.76 to1.26). Complete source-row components: Acute kidney failure; 31(3.1); 32(3.2); −0.1(−1.6 to1.4); RR0.98(0.76 to1.26); .89.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (31/989)/(32/987) = 0.966791; printed point = 0.98. Nearest two-decimal identity display would be 0.97; discrepancy=0.013209.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (31/(31+32))/(958/(1913))=0.982586. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Acute kidney failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.98, and is this value intended as the H/L event risk ratio from 31/989 and 32/987 or a differently defined model quantity?

### NUM-O30-RR: Extrapulmonary infection: labeled RR versus printed patient risks

- **Numeric relationships:** N209.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O30 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 29/989; L 23/987; printed RR1.11(0.87 to1.42). Complete source-row components: Extrapulmonary infection; 29(2.9); 23(2.3); 0.6(−0.8 to2.0); RR1.11(0.87 to1.42); .40.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (29/989)/(23/987) = 1.258320; printed point = 1.11. Nearest two-decimal identity display would be 1.26; discrepancy=-0.148320.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (29/(29+23))/(960/(1924))=1.117708. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Extrapulmonary infection, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.11, and is this value intended as the H/L event risk ratio from 29/989 and 23/987 or a differently defined model quantity?

### NUM-O31-RR: Hepatic failure: labeled RR versus printed patient risks

- **Numeric relationships:** N210.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O31 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 9/989; L 9/987; printed RR0.99(0.63 to1.59). Complete source-row components: Hepatic failure; 9(0.9); 9(0.9); 0(−0.8 to0.8); RR0.99(0.63 to1.59); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (9/989)/(9/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (9/(9+9))/(980/(1958))=0.998980. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Hepatic failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.99, and is this value intended as the H/L event risk ratio from 9/989 and 9/987 or a differently defined model quantity?

### NUM-O32-RR: Coma: labeled RR versus printed patient risks

- **Numeric relationships:** N211.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O32 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 2/989; L 2/987; printed RR0.99(0.37 to2.66). Complete source-row components: Coma; 2(0.2); 2(0.2); 0(−0.4 to0.4); RR0.99(0.37 to2.66); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (2/989)/(2/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (2/(2+2))/(987/(1972))=0.998987. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Coma, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.99, and is this value intended as the H/L event risk ratio from 2/989 and 2/987 or a differently defined model quantity?

### NUM-O33-RR: Disseminated intravascular coagulation: labeled RR versus printed patient risks

- **Numeric relationships:** N212.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O33 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 1/989; L 0/987; printed RR2.00(1.91 to2.09). Complete source-row components: Disseminated intravascular coagulation; 1(0.1); 0; 0.1(−0.1 to0.3); RR2.00(1.91 to2.09); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (1/989)/(0/987) = undefined because the control-event risk is zero; printed point = 2.00. A finite value2.00 requires an additional estimator/continuity rule.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (1/(1+0))/(988/(1975))=1.998988. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Disseminated intravascular coagulation, what exact event orientation, reference group, denominator and point-estimate estimator produced 2.00, and is this value intended as the H/L event risk ratio from 1/989 and 0/987 or a differently defined model quantity?

### NUM-O35-RR: Impaired postoperative wound healing: labeled RR versus printed patient risks

- **Numeric relationships:** N214.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O35 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 22/989; L 26/987; printed RR0.91(0.66 to1.24). Complete source-row components: Impaired postoperative wound healing; 22(2.2); 26(2.6); −0.4(−1.8 to0.9); RR0.91(0.66 to1.24); .55.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (22/989)/(26/987) = 0.844443; printed point = 0.91. Nearest two-decimal identity display would be 0.84; discrepancy=0.065557.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (22/(22+26))/(967/(1928))=0.913823. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Impaired postoperative wound healing, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.91, and is this value intended as the H/L event risk ratio from 22/989 and 26/987 or a differently defined model quantity?

### NUM-O36-RR: UnexpectedICU admission/readmission: labeled RR versus printed patient risks

- **Numeric relationships:** N215.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O36 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 41/989; L 32/987; printed RR1.12(0.91 to1.38). Complete source-row components: UnexpectedICU admission/readmission; 41(4.1); 32(3.2); 0.9(−0.8 to2.6); RR1.12(0.91 to1.38); .29.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (41/989)/(32/987) = 1.278659; printed point = 1.12. Nearest two-decimal identity display would be 1.28; discrepancy=-0.158659.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (41/(41+32))/(948/(1903))=1.127435. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For UnexpectedICU admission/readmission, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.12, and is this value intended as the H/L event risk ratio from 41/989 and 32/987 or a differently defined model quantity?

### NUM-O39-RR: Intraoperative hypoxemia: labeled RR versus printed patient risks

- **Numeric relationships:** N218.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O39 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 49/989; L 134/987; printed RR0.51(0.40 to0.65). Complete source-row components: Intraoperative hypoxemia; 49(5.0); 134(13.6); −8.6(−11.1 to−6.1); RR0.51(0.40 to0.65); <.001.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (49/989)/(134/987) = 0.364932; printed point = 0.51. Nearest two-decimal identity display would be 0.36; discrepancy=0.145068.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (49/(49+134))/(940/(1793))=0.510737. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Intraoperative hypoxemia, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.51, and is this value intended as the H/L event risk ratio from 49/989 and 134/987 or a differently defined model quantity?

### NUM-O40-RR: Intraoperative hypotension: labeled RR versus printed patient risks

- **Numeric relationships:** N219.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O40 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 313/989; L 170/987; printed RR1.43(1.31 to1.56). Complete source-row components: Intraoperative hypotension; 313(31.6); 170(17.2); 14.4(10.7 to18.2); RR1.43(1.31 to1.56); <.001.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (313/989)/(170/987) = 1.837453; printed point = 1.43. Nearest two-decimal identity display would be 1.84; discrepancy=-0.407453.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (313/(313+170))/(676/(1493))=1.431233. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Intraoperative hypotension, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.43, and is this value intended as the H/L event risk ratio from 313/989 and 170/987 or a differently defined model quantity?

### NUM-O41-RR: Intraoperative bradycardia: labeled RR versus printed patient risks

- **Numeric relationships:** N220.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O41 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 98/989; L 59/987; printed RR1.27(1.11 to1.45). Complete source-row components: Intraoperative bradycardia; 98(9.9); 59(6.0); 3.9(1.5 to6.3); RR1.27(1.11 to1.45); .001.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (98/989)/(59/987) = 1.657658; printed point = 1.27. Nearest two-decimal identity display would be 1.66; discrepancy=-0.387658.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (98/(98+59))/(891/(1819))=1.274329. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Intraoperative bradycardia, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.27, and is this value intended as the H/L event risk ratio from 98/989 and 59/987 or a differently defined model quantity?

### NUM-O42-RR: Mortality during hospital stay: labeled RR versus printed patient risks

- **Numeric relationships:** N221.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O42 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 12/989; L 5/987; printed RR1.41(0.95 to1.81). Complete source-row components: Mortality during hospital stay; 12(1.2); 5(0.5); 0.7(−0.1 to1.5); RR1.41(0.95 to1.81); .09.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (12/989)/(5/987) = 2.395147; printed point = 1.41. Nearest two-decimal identity display would be 2.40; discrepancy=-0.985147.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (12/(12+5))/(977/(1959))=1.415377. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Mortality during hospital stay, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.41, and is this value intended as the H/L event risk ratio from 12/989 and 5/987 or a differently defined model quantity?

### NUM-O43-RR: Post hoc rescue strategy for desaturation: labeled RR versus printed patient risks

- **Numeric relationships:** N222.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), O43 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 59/989; L 166/987; printed RR0.49(0.39 to0.62). Complete source-row components: Post hoc rescue strategy for desaturation; 59(6.0); 166(16.8); −10.8(−13.6 to−8.1); RR0.49(0.39 to0.62); <.001.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (59/989)/(166/987) = 0.354703; printed point = 0.49. Nearest two-decimal identity display would be 0.35; discrepancy=0.135297.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (59/(59+166))/(930/(1751))=0.493711. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Post hoc rescue strategy for desaturation, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.49, and is this value intended as the H/L event risk ratio from 59/989 and 166/987 or a differently defined model quantity?

### NUM-O44-RR: Post hoc vasoactive drugs: labeled RR versus printed patient risks

- **Numeric relationships:** N223.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), O44 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 491/989; L 439/987; printed RR1.10(1.01 to1.21). Complete source-row components: Post hoc vasoactive drugs; 491(49.6); 439(44.5); 5.2(0.8 to9.6); RR1.10(1.01 to1.21); .02.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (491/989)/(439/987) = 1.116189; printed point = 1.10. Nearest two-decimal identity display would be 1.12; discrepancy=-0.016189.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Header and footnote b label the estimate risk ratio; footnote a identifies reference patients989/987 unless otherwise indicated. Footnote b says Wald likelihood-ratio approximation; no row-specific adjustment or reversed outcome definition is stated. Alternative reverse group-membership diagnostic: (491/(491+439))/(498/(1046))=1.108922. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Post hoc vasoactive drugs, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.10, and is this value intended as the H/L event risk ratio from 491/989 and 439/987 or a differently defined model quantity?

### NUM-F01-RR: Nonlaparoscopic: labeled RR versus printed patient risks

- **Numeric relationships:** N225.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F01 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 79/240; L 74/253; printed 1.09(0.90-1.32). Complete source-row components: Nonlaparoscopic; 79/240; 74/253; 1.09(0.90-1.32); .08 shared withF02.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (79/240)/(74/253) = 1.125394; printed point = 1.09. Nearest two-decimal identity display would be 1.13; discrepancy=-0.035394.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (79/(79+74))/(161/(340))=1.090407. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Nonlaparoscopic, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.09, and is this value intended as the H/L event risk ratio from 79/240 and 74/253 or a differently defined model quantity?

### NUM-F02-RR: Laparoscopic: labeled RR versus printed patient risks

- **Numeric relationships:** N226.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F02 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 130/740; L 156/727; printed 0.88(0.77-1.01). Complete source-row components: Laparoscopic; 130/740; 156/727; 0.88(0.77-1.01); same.08.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (130/740)/(156/727) = 0.818694; printed point = 0.88. Nearest two-decimal identity display would be 0.82; discrepancy=0.061306.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (130/(130+156))/(610/(1181))=0.880030. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Laparoscopic, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.88, and is this value intended as the H/L event risk ratio from 130/740 and 156/727 or a differently defined model quantity?

### NUM-F03-RR: BMI<40: labeled RR versus printed patient risks

- **Numeric relationships:** N227.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F03 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 76/336; L 94/376; printed 0.93(0.77-1.13). Complete source-row components: BMI<40; 76/336; 94/376; 0.93(0.77-1.13); .97 shared withF04.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (76/336)/(94/376) = 0.904762; printed point = 0.93. Nearest two-decimal identity display would be 0.90; discrepancy=0.025238.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (76/(76+94))/(260/(542))=0.931946. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For BMI<40, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.93, and is this value intended as the H/L event risk ratio from 76/336 and 94/376 or a differently defined model quantity?

### NUM-F04-RR: BMI≥40: labeled RR versus printed patient risks

- **Numeric relationships:** N228.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F04 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 135/653; L 139/611; printed 0.94(0.82-1.08). Complete source-row components: BMI≥40; 135/653; 139/611; 0.94(0.82-1.08); same.97.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (135/653)/(139/611) = 0.908755; printed point = 0.94. Nearest two-decimal identity display would be 0.91; discrepancy=0.031245.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (135/(135+139))/(518/(990))=0.941648. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For BMI≥40, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.94, and is this value intended as the H/L event risk ratio from 135/653 and 139/611 or a differently defined model quantity?

### NUM-F05-RR: SpO2<96%: labeled RR versus printed patient risks

- **Numeric relationships:** N229.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F05 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 88/317; L 112/342; printed 0.88(0.74-1.06). Complete source-row components: SpO2<96%; 88/317; 112/342; 0.88(0.74-1.06); .35 shared withF06.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (88/317)/(112/342) = 0.847679; printed point = 0.88. Nearest two-decimal identity display would be 0.85; discrepancy=0.032321.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (88/(88+112))/(229/(459))=0.881921. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For SpO2<96%, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.88, and is this value intended as the H/L event risk ratio from 88/317 and 112/342 or a differently defined model quantity?

### NUM-F06-RR: SpO2≥96%: labeled RR versus printed patient risks

- **Numeric relationships:** N230.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F06 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 123/672; L 121/645; printed 0.99(0.86-1.13). Complete source-row components: SpO2≥96%; 123/672; 121/645; 0.99(0.86-1.13); same.35.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (123/672)/(121/645) = 0.975686; printed point = 0.99. Nearest two-decimal identity display would be 0.98; discrepancy=0.014314.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (123/(123+121))/(549/(1073))=0.985241. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For SpO2≥96%, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.99, and is this value intended as the H/L event risk ratio from 123/672 and 121/645 or a differently defined model quantity?

### NUM-F07-RR: Peripheral incision: labeled RR versus printed patient risks

- **Numeric relationships:** N231.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F07 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 32/126; L 25/126; printed 1.16(0.89-1.53). Complete source-row components: Peripheral incision; 32/126; 25/126; 1.16(0.89-1.53); .11 shared withF08.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (32/126)/(25/126) = 1.280000; printed point = 1.16. Nearest two-decimal identity display would be 1.28; discrepancy=-0.120000.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (32/(32+25))/(94/(195))=1.164614. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Peripheral incision, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.16, and is this value intended as the H/L event risk ratio from 32/126 and 25/126 or a differently defined model quantity?

### NUM-F08-RR: Upper abdominal: labeled RR versus printed patient risks

- **Numeric relationships:** N232.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F08 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 179/863; L 208/861; printed 0.90(0.80-1.02). Complete source-row components: Upper abdominal; 179/863; 208/861; 0.90(0.80-1.02); same.11.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (179/863)/(208/861) = 0.858583; printed point = 0.90. Nearest two-decimal identity display would be 0.86; discrepancy=0.041417.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (179/(179+208))/(684/(1337))=0.904102. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Upper abdominal, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.90, and is this value intended as the H/L event risk ratio from 179/863 and 208/861 or a differently defined model quantity?

### NUM-F09-RR: Waist-to-hip<1.0: labeled RR versus printed patient risks

- **Numeric relationships:** N233.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F09 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 97/467; L 100/457; printed 0.97(0.83-1.13). Complete source-row components: Waist-to-hip<1.0; 97/467; 100/457; 0.97(0.83-1.13); .65 shared withF10.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (97/467)/(100/457) = 0.949229; printed point = 0.97. Nearest two-decimal identity display would be 0.95; discrepancy=0.020771.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (97/(97+100))/(370/(727))=0.967472. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Waist-to-hip<1.0, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.97, and is this value intended as the H/L event risk ratio from 97/467 and 100/457 or a differently defined model quantity?

### NUM-F10-RR: Waist-to-hip≥1.0: labeled RR versus printed patient risks

- **Numeric relationships:** N234.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F10 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 98/447; L 112/449; printed 0.92(0.78-1.08). Complete source-row components: Waist-to-hip≥1.0; 98/447; 112/449; 0.92(0.78-1.08); same.65.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (98/447)/(112/449) = 0.878915; printed point = 0.92. Nearest two-decimal identity display would be 0.88; discrepancy=0.041085.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (98/(98+112))/(349/(686))=0.917287. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Waist-to-hip≥1.0, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.92, and is this value intended as the H/L event risk ratio from 98/447 and 112/449 or a differently defined model quantity?

### NUM-F11-RR: All patients: labeled RR versus printed patient risks

- **Numeric relationships:** N235.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F11 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 211/989; L 233/987; printed 0.93(0.83-1.04). Complete source-row components: All patients; 211/989; 233/987; 0.93(0.83-1.04); not printed.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (211/989)/(233/987) = 0.903748; printed point = 0.93. Nearest two-decimal identity display would be 0.90; discrepancy=0.026252.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Direct observation versus inference:** Direct: the counts, populations, effect label and point estimate appear together. Derived diagnostic: the count-defined H/L event-risk identity does not reproduce that labeled estimate under nearest rounding. Figure title/header identify a risk ratio for PPC and the axis favors high PEEP below1. The Methods binomial GLM is described for interactions; no marginal row-RR adjustment rule is stated. Alternative reverse group-membership diagnostic: (211/(211+233))/(778/(1532))=0.935791. This is a ratio of the high-group fraction among event patients to its fraction among non-event patients, not the H/L event-risk ratio; approximate agreement is an inference about a possible mechanism, not proof of the fitted analysis.
- **Source-grounded alternatives:** A separately adjusted/model-based risk ratio, a different outcome/reference orientation, continuity correction when a cell is zero, or a disclosed truncation convention could explain some comparisons. No such row-specific rule is supplied in these locations; conventional Wald interval calculation alone does not identify a different point-estimate target. Small equal-count differences may be display truncation; large differences remain independently observable.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For All patients, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.93, and is this value intended as the H/L event risk ratio from 211/989 and 233/987 or a differently defined model quantity?

### NUM-T07-RD: Any recruitment,No.(%): absolute difference versus exact printed risks

- **Numeric relationships:** N127.
- **Compared locations and content roles:** REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), T07 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 972(98.3); L 11(1.1); difference 97.1(96.1 to98.2). Complete source-row components: Any recruitment,No.(%); 972(98.3); 11(1.1); 97.1(96.1 to98.2); <.001.
- **Reproducible rule and calculation:** 100*(972/989−11/987)=97.166604 pp; printed 97.1 pp; discrepancy=-0.066604 pp; nearest one-decimal value=97.2 pp. Displayed percentage subtraction=97.200000 pp.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Any recruitment,No.(%), was the absolute difference 97.1 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

### NUM-T38-PCT-L: Noninvasive ventilation,No.(%): L printed percentage identity

- **Numeric relationships:** N158.
- **Compared locations and content roles:** REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), T38 L count/denominator cell and L n987 header; REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** L 264/987 (26.8%) using header L n987. Complete source-row components: Noninvasive ventilation,No.(%); 274(27.7); 264(26.8); 0.9(−3.0 to4.9); .64.
- **Reproducible rule and calculation:** 100*264/987=26.747720%; printed 26.8%; discrepancy=0.052280 pp; nearest one-decimal value=26.7%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 26.8% for L 264/987 in Noninvasive ventilation,No.(%), and should the printed denominator or percentage be interpreted differently?

### NUM-T38-RD: Noninvasive ventilation,No.(%): absolute difference versus exact printed risks

- **Numeric relationships:** N158.
- **Compared locations and content roles:** REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), T38 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 274(27.7); L 264(26.8); difference 0.9(−3.0 to4.9). Complete source-row components: Noninvasive ventilation,No.(%); 274(27.7); 264(26.8); 0.9(−3.0 to4.9); .64.
- **Reproducible rule and calculation:** 100*(274/989−264/987)=0.957032 pp; printed 0.9 pp; discrepancy=-0.057032 pp; nearest one-decimal value=1.0 pp. Displayed percentage subtraction=0.900000 pp.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Noninvasive ventilation,No.(%), was the absolute difference 0.9 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

### NUM-T45-PCT-H: Monitoring neuromuscular function,n/N(%): H printed percentage identity

- **Numeric relationships:** N165.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T45 H count/denominator cell; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** H 632/982 (64.9%). Complete source-row components: Monitoring neuromuscular function,n/N(%); 632/982(64.9); 651/984(67.7); −1.8(−6.0 to2.4); .40.
- **Reproducible rule and calculation:** 100*632/982=64.358452%; printed 64.9%; discrepancy=0.541548 pp; nearest one-decimal value=64.4%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding. The alternate parent blockade denominator is 974; its use would approximately reproduce this percentage, but it is not the denominator printed in the cell.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 64.9% for H 632/982 in Monitoring neuromuscular function,n/N(%), and should the printed denominator or percentage be interpreted differently?

### NUM-T45-PCT-L: Monitoring neuromuscular function,n/N(%): L printed percentage identity

- **Numeric relationships:** N165.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T45 L count/denominator cell; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** L 651/984 (67.7%). Complete source-row components: Monitoring neuromuscular function,n/N(%); 632/982(64.9); 651/984(67.7); −1.8(−6.0 to2.4); .40.
- **Reproducible rule and calculation:** 100*651/984=66.158537%; printed 67.7%; discrepancy=1.541463 pp; nearest one-decimal value=66.2%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding. The alternate parent blockade denominator is 961; its use would approximately reproduce this percentage, but it is not the denominator printed in the cell.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 67.7% for L 651/984 in Monitoring neuromuscular function,n/N(%), and should the printed denominator or percentage be interpreted differently?

### NUM-T46-PCT-H: Reversal,n/N(%): H printed percentage identity

- **Numeric relationships:** N166.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T46 H count/denominator cell; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** H 724/982 (74.3%). Complete source-row components: Reversal,n/N(%); 724/982(74.3); 723/984(75.2); 0.2(−3.6 to4.1); .90.
- **Reproducible rule and calculation:** 100*724/982=73.727088%; printed 74.3%; discrepancy=0.572912 pp; nearest one-decimal value=73.7%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding. The alternate parent blockade denominator is 974; its use would approximately reproduce this percentage, but it is not the denominator printed in the cell.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 74.3% for H 724/982 in Reversal,n/N(%), and should the printed denominator or percentage be interpreted differently?

### NUM-T46-PCT-L: Reversal,n/N(%): L printed percentage identity

- **Numeric relationships:** N166.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T46 L count/denominator cell; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** L 723/984 (75.2%). Complete source-row components: Reversal,n/N(%); 724/982(74.3); 723/984(75.2); 0.2(−3.6 to4.1); .90.
- **Reproducible rule and calculation:** 100*723/984=73.475610%; printed 75.2%; discrepancy=1.724390 pp; nearest one-decimal value=73.5%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding. The alternate parent blockade denominator is 961; its use would approximately reproduce this percentage, but it is not the denominator printed in the cell.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 75.2% for L 723/984 in Reversal,n/N(%), and should the printed denominator or percentage be interpreted differently?

### NUM-T46-RD: Reversal,n/N(%): absolute difference versus exact printed risks

- **Numeric relationships:** N166.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T46 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 724/982(74.3); L 723/984(75.2); difference 0.2(−3.6 to4.1). Complete source-row components: Reversal,n/N(%); 724/982(74.3); 723/984(75.2); 0.2(−3.6 to4.1); .90.
- **Reproducible rule and calculation:** 100*(724/982−723/984)=0.251478 pp; printed 0.2 pp; discrepancy=-0.051478 pp; nearest one-decimal value=0.3 pp. Displayed percentage subtraction=-0.900000 pp. It is negative while the reported difference is positive; the count-defined difference itself is positive.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Reversal,n/N(%), was the absolute difference 0.2 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

### NUM-O02-RD: Mild respiratory failure: absolute difference versus exact printed risks

- **Numeric relationships:** N181.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O02 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 135(13.7); L 154(15.6); difference −1.9(−5.1 to1.2). Complete source-row components: Mild respiratory failure; 135(13.7); 154(15.6); −1.9(−5.1 to1.2); RR0.92(0.80 to1.05); .22.
- **Reproducible rule and calculation:** 100*(135/989−154/987)=-1.952685 pp; printed -1.9 pp; discrepancy=0.052685 pp; nearest one-decimal value=-2.0 pp. Displayed percentage subtraction=-1.900000 pp.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Mild respiratory failure, was the absolute difference -1.9 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

### NUM-O28-PCT-H: Kidney failure,n/N(%): H printed percentage identity

- **Numeric relationships:** N207.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O28 H count/denominator cell; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** H 7/31 (22.5%). Complete source-row components: Kidney failure,n/N(%); 7/31(22.5); 5/32(15.6); not printed; not printed; same.97.
- **Reproducible rule and calculation:** 100*7/31=22.580645%; printed 22.5%; discrepancy=-0.080645 pp; nearest one-decimal value=22.6%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 22.5% for H 7/31 in Kidney failure,n/N(%), and should the printed denominator or percentage be interpreted differently?

### NUM-O29-PCT-H: Kidney loss,n/N(%): H printed percentage identity

- **Numeric relationships:** N208.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O29 H count/denominator cell; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** H 2/31 (6.4%). Complete source-row components: Kidney loss,n/N(%); 2/31(6.4); 2/32(6.2); not printed; not printed; same.97.
- **Reproducible rule and calculation:** 100*2/31=6.451613%; printed 6.4%; discrepancy=-0.051613 pp; nearest one-decimal value=6.5%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 6.4% for H 2/31 in Kidney loss,n/N(%), and should the printed denominator or percentage be interpreted differently?

### NUM-O43-RD: Post hoc rescue strategy for desaturation: absolute difference versus exact printed risks

- **Numeric relationships:** N222.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), O43 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 59(6.0); L 166(16.8); difference −10.8(−13.6 to−8.1). Complete source-row components: Post hoc rescue strategy for desaturation; 59(6.0); 166(16.8); −10.8(−13.6 to−8.1); RR0.49(0.39 to0.62); <.001.
- **Reproducible rule and calculation:** 100*(59/989−166/987)=-10.853021 pp; printed -10.8 pp; discrepancy=0.053021 pp; nearest one-decimal value=-10.9 pp. Displayed percentage subtraction=-10.800000 pp.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Post hoc rescue strategy for desaturation, was the absolute difference -10.8 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

### NUM-T47-ESTIMAND: Total fluids: difference estimand accompanying median summaries

- **Numeric relationships:** N167.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), Table 2 Total fluids median(IQR), L H/L cells; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same row Absolute Difference cell and Table 2 footnotes.
- **Printed inputs:** H median1.5L (IQR1.0–2.5); L median1.6L (IQR1.0–2.5); Absolute Difference+0.02L (95%CI−0.11 to0.14),P=.79. Complete source-row components: Total fluid,median(IQR),L; 1.5(1.0 to2.5); 1.6(1.0 to2.5); 0.02(−0.11 to0.14); .79.
- **Reproducible rule and calculation:** If the difference column subtracts the displayed central statistic, medianH−medianL=1.5−1.6=−0.10L. One-decimal rounded medians permit true median difference from−0.20 to0.00L; the two-decimal+0.02 permits0.015 to0.025L. Those ranges do not overlap.
- **Tolerance:** 0.05L for each one-decimal median and0.005L for the two-decimal difference. Applicability is explicitly conditional on a median-difference estimand.
- **Direct observation versus inference:** Direct: median/IQR labels accompany a positive absolute-difference point estimate. Derived diagnostic: it is incompatible with a literal difference of those medians under rounding. No Table 2 footnote defines whether this effect is a mean difference, rank-based shift, or median difference.
- **Source-grounded alternatives:** A mean difference or rank-based location shift can legitimately coexist with differently signed group median subtraction. This candidate is the concrete displayed estimand/summary mismatch requiring its rule to be named; it does not assert that a difference of medians was actually estimated.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** What estimand and calculation produced+0.02L for total fluids: mean difference, rank-based location shift, or difference of medians? How should the absolute-difference column be interpreted alongside the two reported medians?

### NUM-T30-LABEL: Heat rate label versus beats-per-minute measurements

- **Numeric relationships:** N150, N151, N152.
- **Compared locations and content roles:** REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), Table 2 heading and T30–T32 numeric rows; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnote k heart-rate definition.
- **Printed inputs:** Table 2 row heading Heat rate, mean(SD),beats/min; H/L after intubation76.5(15.8)/76.0(14.3), first hour72.6(13.4)/73.1(14.0), last hour73.5(13.0)/74.9(13.8).. Complete source-row components: Printed “Heat rate”/intubation,beats/min; 76.5(15.8); 76.0(14.3); 0.6(−0.7 to1.9); .38 / Printed “Heat rate”/first hour; 72.6(13.4); 73.1(14.0); −0.6(−1.8 to0.6); .36 / Printed “Heat rate”/last hour; 73.5(13.0); 74.9(13.8); −1.4(−2.6 to−0.2); .02.
- **Reproducible rule and calculation:** A beat count per minute is a cardiac rate measurement; the printed label Heat rate denotes a different physical quantity and is incompatible with beats/min. The same article explicitly calls bradycardia a heart rate measurement in beats/min.
- **Tolerance:** Exact label/unit identity; no rounding tolerance. No numerical value is re-estimated.
- **Direct observation versus inference:** Direct: the Table 2 heading spells Heat rate, and its unit is beats/min. The Table 3 bradycardia definition explicitly says heart rate less than50beats/min. Inference: the missing r is plausibly a typographic error, not a new heat measurement.
- **Source-grounded alternatives:** Readers can infer the intended heart-rate quantity from units/context. This is a bounded measure-label proofreading candidate, not an additional physiologic numerical discrepancy.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Is the Table 2 Heat rate heading intended to read Heart rate, and should all three beats/min rows be indexed under that measurement label?

### NUM-F09-UNIT: Waist-to-hip ratio assigned a length unit

- **Numeric relationships:** N233, N234.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2 waist-to-hip ratio,cm heading and F09/F10 rows; REPORT [PDF p. 5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table 1 waist-to-hip ratio row and<1.0/≥1.0 classifications.
- **Printed inputs:** Figure 2 heading Waist-to-hip ratio,cm; thresholds<1.0/≥1.0; H97/467 and98/447; L100/457 and112/449.. Complete source-row components: Waist-to-hip<1.0; 97/467; 100/457; 0.97(0.83-1.13); .65 shared withF10 / Waist-to-hip≥1.0; 98/447; 112/449; 0.92(0.78-1.08); same.65.
- **Reproducible rule and calculation:** A waist-to-hip ratio equals waist circumference/hip circumference; common length units cancel. Its unit is dimensionless, so cm is incompatible with the ratio label and threshold1.0.
- **Tolerance:** Exact dimensional identity; no numeric rounding tolerance.
- **Direct observation versus inference:** Direct: Figure 2 attaches cm to the named ratio. Derived: length divided by length is dimensionless. The main Table 1 waist-to-hip ratio also uses values1.01/1.00 rather than a length threshold.
- **Source-grounded alternatives:** cm may be a stray inherited circumference unit; threshold1.0 and subgroup denominators identify the intended dimensionless ratio. Actual circumference lengths in cm would require a different variable definition.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Is cm an unintended unit on the Figure 2 waist-to-hip ratio heading, or does the figure use a different waist measurement than the stated ratio?

## Coverage facts and limitations

All 115 compound rows and all5 paired subgroup partitions checked. Counts/percentages, missingness, denominator bounds, reference directions, units, central/difference scales, SD/IQR ordering, all printed effect/interval components, repeated values, and patient-count versus risk versus person-time identities are retained in the inventory. Head elevation, anesthesia type, epidural types, kidney categories and all Figure 2 partitions were exhaustively totaled. GI severity totals49/46 versus parent65/56 identify16/10 unclassified severity observations without inventing a contradictory total. Recruitment timepoint counts overlap, composite components can overlap, and blood-product types can overlap; they are not falsely summed into mutually exclusive patient totals. The pooled Figure 2 RR occurrence duplicates O01 for coordinator consolidation; all other displayed rows use different populations or outcomes. Continuous rounded mean differences reconcile within propagated precision. Identical medians/IQRs and same recruitment-timepoint counts are plausible repeats, not standalone candidates. Hospital-free days footnote h specifies the mean-difference exception; mortality5days is explicitly a Cox HR. No supplied person-time denominators, statistics or SEs occur in this assigned source scope. No P-value display zero exists in these assigned main rows.

Limitations: binary row-RR point-estimate estimator/adjustment orientation and Table 2 continuous/median difference estimands are incompletely specified. Small nearest-rounding mismatches may reflect truncation or unstated complete-case denominators. Candidate cards explicitly preserve those alternatives and human questions; no scientific-coverage gap remains. Statistical interval/P/test consistency and source matches beyond corroborating these rows remain owned by the separately assigned specialists.



# Numeric consistency checker: results-supplement tables

Status: COMPLETE. Runtime ID: 01a1286e-c7cc-7cd0-a901-f092deade378. Exact owned scope: DOC-005 eTables 1–9, physical PDF pages 22–30. All nine table pages and all 119 compound relationships N241–N359 were checked. Every numeric table cell, reference category, denominator, dispersion, estimate, interval, P value, unit, model and footnote is retained in the companion inventory. No target, minimum, maximum or top-N finding rule was applied. Three distinct document-grounded local candidates are emitted below. These keys are handoff identifiers, not stable C IDs.

## Candidate index

| Local key | Relationship | Exact question scope | Compared document locations and roles |
|---|---|---|---|
| SUPPORT-NUM-01 | N269 | Different P values for the matched synthetic-colloid participant-count comparison | DOC-001 Table 2 p.8 REPORT; DOC-005 eTable 3 p.24 REPORT |
| SUPPORT-NUM-02 | N327 | Conditional mean/SD inconsistency on the supplied 10 cm VAS scale | DOC-005 eTable 7 p.28 REPORT; DOC-002 protocol p.17 and p.20 PLAN |
| SUPPORT-NUM-03 | N355 | Conditional mismatch of the high-arm mean event count with the sum of 12 component counts | DOC-005 eTable 9 p.30 REPORT; DOC-001 Table 3 p.9 REPORT |

## SUPPORT-NUM-01 — matched synthetic-colloid count P values

**Assigned relationship:** N269.

**Compared locations and document roles:**

- [DOC-001 main article, physical PDF p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), printed p.2299, Table 2 continued, Synthetic colloids, No. (%), H/L participant counts and its P-value column: REPORT.
- [DOC-005 results supplement, physical PDF p.24](../../../joi190055supp4_prod_16092.pdf#page=24), eTable 3, Synthetic colloids, No. (%), H/L participant counts and its P-value column: REPORT.
- Same DOC-005 p.24 immediately following synthetic-colloid quantity row is a local alternative-check location, REPORT; it prints a separate continuous summary, not the count row.

**Printed inputs:** Both matched count rows use high n = 989 and low n = 987, with 74 (7.5%) versus 56 (5.7%). Main Table 2 prints P = .09; eTable 3 prints P = 0.10. The eTable 3 quantity row immediately below prints 50 (211) versus 35 (171), P = 0.09. Main Table 2 quantity summary instead uses median (IQR), 0.5 (0.5–0.7) versus 0.5 (0.5–0.5) L, P = .50.

**Reproducible rule and calculation:** A matched result means the same participant numerator, denominator, comparison, and count label. Compare the two count-row P cells: 0.10 − 0.09 = 0.01. Count percentages separately reconcile: 100 × 74 / 989 = 7.48231%, and 100 × 56 / 987 = 5.67376%, rounding to 7.5% and 5.7%. The quantity summaries and their P values are not substituted for the count comparison.

**Tolerance:** Each P is printed to two decimal places, ordinarily allowing ±0.005. Rounding intervals [0.085, 0.095) and [0.095, 0.105) do not share an interior; a value exactly at 0.095 with different tie handling is an explicit alternative. The discrepancy is a printed repeated-value difference, not an attempt to reconstruct either test.

**Direct observation versus inference:** Direct source images confirm the same displayed counts, percentage labels, populations and different printed P values. The hypothesis that one P was copied from the neighboring continuous row is inference only, not a finding. The article does not supply a table-specific test rule establishing that both count comparisons used exactly the same test.

**Alternatives and missing definition:** Different tests, continuity corrections, exact versus asymptotic calculations, an unreported effective denominator, or exact-boundary rounding could produce different P values. Identical printed inputs and labels do not identify a disclosed reason. The row with 50 (211) and 35 (171) is a distinct quantity comparison, so its P = .09 is not proof of copying.

**Quality-control relevance:** A small matched P-value discrepancy can propagate as conflicting extracted comparison metadata. No claim about study conclusions follows.

**Exact human question:** “Do the P = .09 in main Table 2 and P = .10 in eTable 3 refer to the same synthetic-colloid participant-count comparison of 74/989 versus 56/987; if so, which test, denominator and rounding convention generated each displayed P value?”

## SUPPORT-NUM-02 — conditional thoracic VAS mean/SD bound

**Assigned relationship:** N327.

**Compared locations and document roles:**

- [DOC-005 results supplement, physical PDF p.28](../../../joi190055supp4_prod_16092.pdf#page=28), eTable 7, VAS thoracic – cm, mean (SD), No., Day 2, low PEEP cell: REPORT.
- [DOC-002 protocol, physical PDF p.17](../../../joi190055supp1_prod_16092.pdf#page=17), printed protocol p.16, version 2.6, actual organ function evaluation bullet defining “Visual Analogue Scale (10 cm): evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.
- [DOC-002 protocol, physical PDF p.20](../../../joi190055supp1_prod_16092.pdf#page=20), printed protocol p.19, postoperative assessment continuation bullet “VAS evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.

**Printed inputs:** eTable 7 low PEEP day-2 thoracic VAS mean 1.4 cm, SD 3.9 cm, n = 841; high PEEP mean 1.3 cm, SD 0.8 cm, n = 838; P = .34. Arm headings are high989 and low987. The protocol specifies a 10 cm VAS for the same named symptoms and repeats the assessment postoperatively. It does not explicitly print the numerical scoring endpoints or a normalization rule.

**Reproducible rule and calculation:** Conditional on the reported cm scores being distance along the supplied 10 cm line, measured from a zero origin and bounded 0–10 cm, any sample with mean m and sample SD s obeys s² ≤ n/(n−1) × m × (10−m). At the printed mean, the maximum sample SD is sqrt(841/840 × 1.4 × 8.6) = 3.47194 cm, below 3.9 cm. With rounding admitted, m can range from 1.35 to 1.45; the largest permitted bound on that interval is sqrt(841/840 × 1.45 × 8.55) = 3.52310 cm. The printed SD interval begins at 3.85 cm. Thus even the most permissive rounding leaves a gap of at least 3.85 − 3.52310 = 0.32690 cm.

**Tolerance:** Mean/SD displayed to one decimal permit ±0.05 cm; n = 841 is exact. The n/(n−1) factor allows the usual sample SD convention and is slightly more permissive than population SD. This calculation is a moment bound, not a reconstructed P value.

**Direct observation versus inference:** The mean, SD, n, cm unit, mean(SD) header and protocol 10 cm scale wording are direct source observations. The numerical 0–10 support and zero-origin scoring convention are explicitly conditional inferences from that supplied line-length and cm-unit description. They are not independently printed endpoints. Protocol p.17 describes baseline organ-function assessment; p.20 repeats the same named VAS postoperatively but does not restate its length. Applying the 10 cm definition to eTable 7 is an identity question retained for human review.

**Alternatives and missing definition:** A transformed or shifted scoring convention, a differently normalized postoperative scale, a larger allowed range, a different underlying statistic despite the mean(SD) label, or a transcription error could explain the display. Without zero origin, a line of length10 alone permits SD up to about5.00 cm and does not establish the mean-dependent contradiction. An alternative 0-based scale would need an upper endpoint at least11.66026 cm even with the rounding allowances, to accommodate the minimum printed SD3.85 at mean1.45. No external VAS convention is used.

**Quality-control relevance:** The reported dispersion may be reused as a summary SD in quantitative evidence synthesis. The candidate is confined to the consistency of that reported summary with the supplied scale definition; it is not a raw-data or clinical plausibility audit.

**Exact human question:** “Were the postoperative thoracic VAS scores in eTable 7 recorded as 0–10 cm distance scores on the protocol’s 10 cm scale, and does the low-PEEP Day 2 cell correctly report mean 1.4 cm, SD 3.9 cm and n = 841; if a different origin, range or transformation was used, what was it?”

## SUPPORT-NUM-03 — conditional event-count mean versus component total

**Assigned relationship:** N355.

**Compared locations and document roles:**

- [DOC-005 results supplement, physical PDF p.30](../../../joi190055supp4_prod_16092.pdf#page=30), eTable 9, Sensitivity analysis for the primary outcome, Count events row, high/low summary cells and n = 989/987 headings: REPORT.
- [DOC-001 main article, physical PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), printed p.2300, Table 3, all 12 Components of the Primary Outcome, high/low No. of Events columns and n = 989/987 headings: REPORT.
- DOC-005 p.30 model footnotes referring to all12 components are corroborative REPORT context, not a new discrepancy relationship.
- [DOC-001 main article, physical PDF p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), Figure 1 randomized high 1011/low 1002, REPORT: source-grounded alternative denominator, not an additional discrepancy relationship.

**Printed inputs:** eTable 9 Count events row gives high0.35 (0.88), low0.38 (0.86), above separately labeled Median (IQR)0 (0–0) for both arms. The Count events row does not explicitly say mean(SD). Main Table 3 high component counts, in its printed order, are mild135, moderate42, severe30, atelectasis44, pleural effusion43, new infiltrates14, cardiopulmonary edema17, bronchospasm12, pulmonary infection10, aspiration2, ARDS3, pneumothorax1. Low counts in the same order are154,58,36,55,21,18,9,10,10,1,1,3.

**Reproducible rule and calculation:** Conditional on “Count events” summary0.35/0.38 being the arithmetic mean of the number of these same12 binary components per participant in the displayed full-arm populations, the mean must equal the sum of all component numerators divided by n. Overlap between components does not defeat this identity; each counted component contributes separately. High sum135 + 42 + 30 + 44 + 43 + 14 + 17 + 12 + 10 + 2 + 3 + 1 = 353; 353 / 989 = 0.356926, which rounds to0.36. Low sum154 + 58 + 36 + 55 + 21 + 18 + 9 + 10 + 10 + 1 + 1 + 3 = 376; 376 / 987 = 0.380952, which rounds to0.38 and reconciles.

**Tolerance:** At two-decimal rounding,0.35 ordinarily implies a mean in [0.345,0.355), hence a total in [341.205,351.095) at n989; integer totals compatible with that interval are342–351. The printed component total353 exceeds the largest compatible integer total by2. The exact mean exceeds the upper rounding boundary0.355 by0.001926. Counts and denominator have zero tolerance. The low-arm summary is within its rounding interval.

**Direct observation versus inference:** Direct images confirm all12 main component counts, populations, and the eTable 9 summary0.35 (0.88). The arithmetic sum and conditional mean identity are derived. Interpreting the unlabeled first summary as mean(SD), and interpreting “Count events” as counting each of the same12 binary components, are named inferences rather than printed definitions.

**Alternatives and missing definition:** The summary may use a different statistic, component grouping (for example collapsing multiple respiratory-failure severities to one event), time rule, population, event definition, weighting or complete-case denominator. Main Figure 1 supplies randomized high 1011/low 1002: 353/1011 = 0.349159 and 376/1002 = 0.375250, which round to 0.35/0.38. Thus a count calculation using all randomized participants could explain both summary means, but that denominator differs from eTable 9 headings 989/987 and requires the population and missing-participant handling to be named. This is an arithmetic alternative, not proof that the authors used it. Truncation rather than rounding would also produce 0.35 from 0.356926 but is not stated. Different component overlap is not by itself an explanation if the count is the sum of those same 12 indicators; alternative grouping would change the count definition and should be specified.

**Quality-control relevance:** Event burden means and their dispersions can be extracted separately from binary-composite risks; a missing aggregation definition or mismatched displayed mean can lead to an incorrect extracted endpoint. No claim about treatment effect or conclusion follows.

**Exact human question:** “Is 0.35 (0.88) in the high-PEEP Count events row the mean (SD) of the count of the same 12 primary-outcome components reported in main Table 3 among 989 participants; if so, how does it reconcile with 353 component occurrences and 353/989 = 0.356926, and if not, what statistic, grouping, time rule and denominator does it represent?”

## Complete noncandidate checks and limitations

The companion numeric inventory gives an explicit checked result for each of119 relationships. Count/percentage rows in eTables3–5 and8 reconcile at their displayed precision. eTable6 category sums reconstruct available denominators984/982 for priority,985/986 for position,986/986 for wound; all printed percentages then reconcile. Missing counts are5/5,4/1 and3/1 respectively. Every VAS observed n is within its arm population; each scale/day missing count is retained, with no inferred cause.

All11 nonreference ARISCAT coefficients reproduce their integer scores and are compatible with printed ORs after beta/OR rounding. Four reference categories have absent coefficient/score cells, not printed zeros. Maximum component score123 agrees with the main scale range. Rescue sequences retain all19 populated arm-step pairs, FiO2 as fractions and PEEP as cmH2O; the absent low-arm step10 is not zero. Continuous amount rows remain distinct from main medians and from count rows. Overlapping drug/solution/component counts are not forced to sum to binary totals.

Per-protocol917 + 912 =1829 matches main flow; losses72/75 sum147, matching1976 −1829. Each per-protocol component/composite numerator is within its matched full-analysis numerator. “Effect Estimate” in eTable8 remains a generic effect label; raw RR arithmetic is not imposed without a supplied measure definition. All point estimates are within ordered intervals, and directions/units remain compatible. Statistical same-test CI/P reconstruction is referred to the independently assigned statistical checkers, particularly eTable8 cardiopulmonary edema and eTable9 average relative effect. Proportional-odds CI and Wilcoxon P are explicitly distinct calculations. No person-time rate is supplied. No display-zero P appears; printed zero doses and medians are retained as finite-precision quantities.

Tool engines: Poppler26.01.0 pdftotext/pdftoppm, reusable source-matched native/layout text, five rendered candidate/comparator pages. Unique derivatives are under preprocessing/numeric_support_tables/. Fresh source extraction includes assigned tables22–30 and targeted protocol17/20. Complete scientific coverage of the assigned scope; no missing source unit. Named unresolved definitions are only the specific candidate alternatives above. Sources and reused assets preserved; no old candidate/report conclusions, web, external literature, Python scientific orchestration, or GPU used. No stable C IDs, severity, validity, evidence disposition or adjudication assigned.



# Numeric consistency checker: PLAN and supplementary methods/figures

Status: COMPLETE. Fresh runtime 01a1286f-0335-7023-bd65-6ab8f678399d, required model gpt-6.1-sol/medium. Scope and all120 relationships N361–N480 are in relationships/parts/numeric_inventory_planplots.md. Assigned PLAN 43/43 pages; REPORT eMethods 4/4 and eFigures 12/12 checked. Main pp6–10 used only for matched comparators. Distinct candidate local keys: 16. No stable C IDs, severity, evidence disposition or adjudication assigned. Sources and reused assets preserved.

The inventory checks all relevant arithmetic, totals, subgroup/threshold partitions, numerator/denominator, missingness/population, percent/rounding, effect labels/scales/units/reference groups, risk/count/person-time and repeated values. Exact source print is authoritative; direct Poppler26.01.0 text and supplied page images locate it. Statistical test/CI reconstruction remains separately tracked in the S inventory. An unchanged printed row alone, a missing model detail alone, or unusual clinical unit alone was not treated as contradiction. No external literature or old candidates read.

| Local key | Candidate | Compared roles |
|---|---|---|
| NP-P01 | Current protocol retains incompatible recruitment totals | PLAN / PLAN |
| NP-M01 | Mild respiratory failure uses equality rather than the main report's inclusive oxygen threshold | REPORT / REPORT |
| NP-F01 | Mortality figure caption attaches the percentages to another outcome | REPORT / REPORT |
| NP-F02 | Four-day median follow-up and day-five numbers at risk require incompatible time definitions | REPORT / REPORT |
| NP-F03 | Collapsed-composite forest row changes the effect label to odds ratio | REPORT / REPORT |
| NP-R01 | Mild respiratory failure: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R02 | Moderate respiratory failure: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R03 | Severe respiratory failure: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R04 | Aspiration: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R05 | Bronchospasm: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R06 | ARDS: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R08 | Atelectasis: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R09 | Cardiopulmonary edema: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R10 | Pleural effusion: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R11 | Pneumothorax: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R12 | Pulmonary infiltrates: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |

## NP-P01 — Current protocol retains incompatible recruitment totals

**Compared locations and document roles:** [joi190055supp1_prod_16092.pdf, PDF p. 10](../../../joi190055supp1_prod_16092.pdf#page=10) recruitment target, PLAN; [joi190055supp1_prod_16092.pdf, PDF p. 11](../../../joi190055supp1_prod_16092.pdf#page=11) revised sample size, PLAN; [joi190055supp1_prod_16092.pdf, PDF p. 12](../../../joi190055supp1_prod_16092.pdf#page=12) section 7 procedure total, PLAN.

**Printed inputs:** Pages 10–11 specify 2013 patients after re-estimation; page 12 says “A total of 748 patients will be included.” Page 11 labels 748 as the original total.

**Reproducible rule and calculation:** A current protocol procedure total should either match the revised current total or explicitly identify the retained historical total. 2013 − 748 = 1265 participants.

**Tolerance:** Exact integer identity; no rounding tolerance.

**Direct observation versus inference:** Both totals and the original-versus-revised history are direct printed observations. Inferring that section 7 intended the current total is diagnostic; the paragraph does not label 748 as historical.

**Alternatives:** An original paragraph may have been retained intentionally, but its current procedural framing leaves the numeric enrollment target ambiguous. No claim about actual recruitment or treatment allocation follows.

**Quality-control relevance:** An outdated target can be copied as the planned study size.

**Exact human question:** Should section 7's 748 be read as historical, and what is the intended current procedural recruitment total after the 2013-patient revision?

## NP-M01 — Mild respiratory failure uses equality rather than the main report's inclusive oxygen threshold

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 20](../../../joi190055supp4_prod_16092.pdf#page=20) eMethods section 2.8, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) Table 3 footnote d, REPORT.

**Printed inputs:** Supplement: responding to supplemental oxygen “= 2 L/min”; moderate responds only to “> 2 L/min”. Main footnote: responding to “2 L or less” is mild; >2 is moderate.

**Reproducible rule and calculation:** Equality and an inclusive upper bound define different categories. A response at 1 L/min satisfies oxygen ≤2 L/min but not oxygen =2 L/min. Neither definition changes the shared PaO₂<60 mmHg or SpO₂<90% threshold.

**Tolerance:** Exact categorical relation; no rounding tolerance at a dose below the boundary.

**Direct observation versus inference:** The equals sign was visually confirmed on the direct-source page image; the main inclusive phrase is directly printed. The 1 L/min example is a derived counterexample, not an observed participant.

**Alternatives:** The equals sign may represent a lost ≤ glyph or an intended standard test flow. No supplied count establishes how many participants were affected.

**Quality-control relevance:** A numeric endpoint definition can change downstream interpretation of mild-event counts.

**Exact human question:** Was the supplementary equality intended to mean ≤2 L/min, or was response at exactly 2 L/min a different operational definition from the main Table 3 footnote?

## NP-F01 — Mortality figure caption attaches the percentages to another outcome

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41) eFigure 11 title, y-axis, HR annotation and caption, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40) eFigure 10 caption, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) Table 3 5-day mortality row, REPORT.

**Printed inputs:** Figure 11 title is probability of death in the first 5 days, axis “5-Day Mortality”, HR1.67 (0.40–6.97), P=.484. Caption names “postoperative extra-pulmonary complications” for high0.5%/low0.3%. Figure 10 extra-pulmonary rates are16.9%/15.2%. Main 5-day deaths are5/989 and3/987.

**Reproducible rule and calculation:** 100×5/989=.50556%→0.5%;100×3/987=.30395%→0.3%. Thus the Figure11 percentages identify mortality, while its caption outcome name identifies the distinct Figure10 outcome.

**Tolerance:** Percentage rounding ±.05 percentage points; incompatible outcome names have no numeric rounding tolerance.

**Direct observation versus inference:** Title, axis, caption and comparator counts are direct observations; assigning the percentages to mortality follows the printed outcome/count match.

**Alternatives:** A copied caption phrase could explain the label; the HR/CI remain coherent with mortality. No conclusion impact is inferred.

**Quality-control relevance:** The labeled percentages could be extracted under the wrong secondary outcome.

**Exact human question:** Does “postoperative extra-pulmonary complications” in the Figure11 caption refer to mortality here, and which outcome label belongs with 0.5% and0.3%?

## NP-F02 — Four-day median follow-up and day-five numbers at risk require incompatible time definitions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 38](../../../joi190055supp4_prod_16092.pdf#page=38) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 39](../../../joi190055supp4_prod_16092.pdf#page=39) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41) caption and all risk-table cells, REPORT.

**Printed inputs:** Each caption states median follow-up4 (2–5) days. Day5 low/high at-risk counts are756/785,756/785,845/828,986/985. Baseline counts are987/989, total1976.

**Reproducible rule and calculation:** If follow-up means the observed time governing those risk tables, at least half of1976 follow-up times must be ≤4 for median4. Thus at most988 can remain at risk on day5 (even allowing both central order statistics and ties). Printed day5 sums1541,1541,1673,1971 exceed988 by553,553,685,983. Even within arms every listed day5 count exceeds half the baseline arm.

**Tolerance:** Counts exact. A median rounded to integer4 would ordinarily lie below4.5, still below5; it cannot explain >half at risk at day5. A distinct follow-up variable could reconcile the statements.

**Direct observation versus inference:** The caption and all48 risk counts are directly printed and checked. The incompatibility is conditional inference that caption follow-up and risk-table follow-up refer to the same observed time.

**Alternatives:** Median4 may refer to postoperative assessment duration while risk tables retain patients through administrative day5, or “number at risk” may be a different denominator. Neither alternative is defined locally. Event/censor timing need not be reconstructed. Identical primary/severe rows alone were not used as a candidate.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Exact human question:** What exact follow-up duration has median4 (2–5), what removes patients from each Figure8–11 risk table, and how can more than half remain at risk on day5 under that duration?

## NP-F03 — Collapsed-composite forest row changes the effect label to odds ratio

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 lower Global Tests header and Collapsed Composite row, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 primary row and arm sizes, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest header “Odds Ratio (95% CI)”, collapsed composite0.93[0.83,1.04]. Main primary row has the identical tuple under “Risk Ratio”; events211/989 versus233/987. Footnote calls the estimates risk ratios.

**Reproducible rule and calculation:** Binary marginal OR=[211/(989−211)]/[233/(987−233)]=(211×754)/(778×233)=.877644; raw RR=(211/989)/(233/987)=.903748. The same printed0.93 tuple carries different effect labels. The raw diagnostics do not decide which model produced0.93.

**Tolerance:** Printed estimate ±.005; .877644 differs from0.93 by.052356 and does not round0.93. Exact matched-label distinction independent of arithmetic.

**Direct observation versus inference:** Different headers and identical tuple are direct observations. Marginal OR/RR calculations are derived diagnostics under the displayed binary counts.

**Alternatives:** The forest could intentionally use an adjusted odds model; no model identity is specified for this particular row. That alternative still requires identifying why the tuple is identical to the main RR.

**Quality-control relevance:** An effect label determines extraction scale and any later transformation.

**Exact human question:** Is the collapsed-composite forest tuple an odds ratio from a separate model or the main reported risk-ratio tuple, and which calculation and label apply?

## NP-R01 — Mild respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Mild respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.92[0.76,1.12],99.58%CI; matched main events high135/989,low154/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(135/989)/(154/987)=0.874851. Printed 0.92 differs by0.045149. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Mild respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.92, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R02 — Moderate respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Moderate respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.83[0.59,1.17],99.58%CI; matched main events high42/989,low58/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(42/989)/(58/987)=0.722674. Printed 0.83 differs by0.107326. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Moderate respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.83, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R03 — Severe respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Severe respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.91[0.61,1.34],99.58%CI; matched main events high30/989,low36/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(30/989)/(36/987)=0.831648. Printed 0.91 differs by0.078352. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Severe respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.91, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R04 — Aspiration: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Aspiration row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.33[0.41,4.30],99.58%CI; matched main events high2/989,low1/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(2/989)/(1/987)=1.995956. Printed 1.33 differs by0.665956. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Aspiration forest row, what population, contrast, numerator/denominator and estimator produced1.33, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R05 — Bronchospasm: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Bronchospasm row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.09[0.62,1.91],99.58%CI; matched main events high12/989,low10/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(12/989)/(10/987)=1.197573. Printed 1.09 differs by0.107573. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Bronchospasm forest row, what population, contrast, numerator/denominator and estimator produced1.09, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R06 — ARDS: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 ARDS row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.50[0.65,3.44],99.58%CI; matched main events high3/989,low1/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(3/989)/(1/987)=2.993933. Printed 1.50 differs by1.493933. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the ARDS forest row, what population, contrast, numerator/denominator and estimator produced1.50, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R08 — Atelectasis: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Atelectasis row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.88[0.64,1.23],99.58%CI; matched main events high44/989,low55/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(44/989)/(55/987)=0.798382. Printed 0.88 differs by0.081618. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Atelectasis forest row, what population, contrast, numerator/denominator and estimator produced0.88, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R09 — Cardiopulmonary edema: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Cardiopulmonary edema row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.31[0.87,1.98],99.58%CI; matched main events high17/989,low9/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(17/989)/(9/987)=1.885069. Printed 1.31 differs by0.575069. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Cardiopulmonary edema forest row, what population, contrast, numerator/denominator and estimator produced1.31, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R10 — Pleural effusion: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pleural effusion row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.36[1.05,1.76],99.58%CI; matched main events high43/989,low21/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(43/989)/(21/987)=2.043478. Printed 1.36 differs by0.683478. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pleural effusion forest row, what population, contrast, numerator/denominator and estimator produced1.36, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R11 — Pneumothorax: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pneumothorax row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.50[0.04,5.96],99.58%CI; matched main events high1/989,low3/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(1/989)/(3/987)=0.332659. Printed 0.50 differs by0.167341. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pneumothorax forest row, what population, contrast, numerator/denominator and estimator produced0.50, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R12 — Pulmonary infiltrates: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pulmonary infiltrates row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.87[0.49,1.55],99.58%CI; matched main events high14/989,low18/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(14/989)/(18/987)=0.776205. Printed 0.87 differs by0.093795. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pulmonary infiltrates forest row, what population, contrast, numerator/denominator and estimator produced0.87, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?


## Complete non-candidate and limitation record

All 120 relationships are checked; candidate-free entries explicitly retain the applicable rule and reason in the inventory. All 19 rescue-step rows reconcile and all15 historical rows preserve bivariate versus multivariate populations/reference groups. All 11 historical nonreference ORs are positive and inside their own CIs; exp(beta) agrees the adjusted OR at one-decimal precision and the supplied repeated REPORT score conversion round(10beta) reproduces every score. Three blank-reference coefficient/score domains plus age reference are not assigned zero without a rule. The n1627 versus1624 model difference is not unexplained arithmetic.

Original total748 is consistent with712×1.05 rounded, though direct retention inversion would yield750; absent inflation convention alone is not a candidate. Revised1912/.95 rounds2013. Exact interim totals reproduce50%/75%/100% of1912. Final efficacy-crossing sum.801 lies within rounding of80% and futility increments sum.200.99.58% reproduces the Bonferroni rule. Historical amendments explaining different numbers remain historical PLAN material.

All 48 risk counts are nonnegative integer counts, individually bounded by the appropriate baseline arm and nonincreasing across printed times. Both primary/severe row vectors repeat exactly; without event/censoring data that repetition alone does not prove a contradiction. NP-F02 instead specifies the incompatible median/risk definitions. HRs, binary proportions, count-component burden, ordinal-count ORs and GEE measures are not treated as interchangeable. “Rate” beside a percentage does not itself establish person-time incidence; no person-time denominator is printed.

All 16 forest intervals are positive/ordered and contain their point estimates. Pulmonary infection RR1.00 agrees10/989 divided by10/987=.997978 within.005, so no forest count-versus-RR candidate is emitted for that row. Different99.58% versus95% CI levels are preserved; no invalid interval identity comparison is made. The separate-model three global rows match eTable9 tuple labels exactly. Small point differences between main95% rows and forest99.58% rows are retained in the full inventory but not independently diagnosed without matching estimator details.

All plot ticks, five repeated-time labels, direction/reference lines, percentage/fraction conversions, confidence-bar labels and interaction-test labels are checked. Exact unlabeled point/interval coordinates and early stopping-curve coordinates are not supplied, so no decimal values are reconstructed from pixel positions. Peak and plateau pressure are kept distinct. The original plan's adjacent “odds ratio relative risks” phrase is preserved as ambiguity without a numerical estimate to arbitrate. Hemoglobin7mg/dL and lactate4mmol/dL appear unusual but lack a supplied conflicting conversion/measurement; no clinical-plausibility-only candidate is registered. DIC thresholds can be read hierarchically; no forced overlap arithmetic candidate.

Administrative/bibliography/qualitative PLAN pages retain explicit no-applicable mapper records, including DOC006p1. No Office/workbook/CSV source exists. No scientific unit omitted; limits concern absent exact graph coordinates, variance/model details, dropout conventions, and the caption/risk follow-up definition. All human questions are precisely attached to printed quantitative contradictions above.



