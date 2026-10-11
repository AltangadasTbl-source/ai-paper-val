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

- Relationship: N060; mapped B32. Compared locations and roles: REPORT [main PDF p.5](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Reflux,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 332/986 (33.6%); explicit denominator 986.
- Reproducible rule/calculation: patient percentage=100×n/N;100×332/986=33.671399594%, which rounds to33.7% under nearest-one-decimal rounding. Printed33.6% differs by0.071399594 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Reflux,n/N(%) percentage33.6%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B33-H: Diabetes,n/N(%), high group

- Relationship: N061; mapped B33. Compared locations and roles: REPORT [main PDF p.5](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Diabetes,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 294/988 (29.7%); explicit denominator 988.
- Reproducible rule/calculation: patient percentage=100×n/N;100×294/988=29.757085020%, which rounds to29.8% under nearest-one-decimal rounding. Printed29.7% differs by0.057085020 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Diabetes,n/N(%) percentage29.7%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B34-H: Diabetes oral medication,n/N(%), high group

- Relationship: N062; mapped B34. Compared locations and roles: REPORT [main PDF p.5](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Diabetes oral medication,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 209/294 (71.0%); explicit denominator 294.
- Reproducible rule/calculation: patient percentage=100×n/N;100×209/294=71.088435374%, which rounds to71.1% under nearest-one-decimal rounding. Printed71.0% differs by0.088435374 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Diabetes oral medication,n/N(%) percentage71.0%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B36-L: Obstructive sleep apnea,No.(%), low group

- Relationship: N064; mapped B36. Compared locations and roles: REPORT [main PDF p.5](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Obstructive sleep apnea,No.(%), L cell numerator/denominator; REPORT same cell percentage; REPORT same-page group header L n=987 and footnote a on p.6.
- Printed inputs: 264 (26.8%); header population 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×264/987=26.747720365%, which rounds to26.7% under nearest-one-decimal rounding. Printed26.8% differs by0.052279635 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell and header values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: footnote a permits unreported variable-specific missingness; an undocumented denominator could account for a small display difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Obstructive sleep apnea,No.(%) percentage26.8%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B37-H: Tobacco never,n/N(%), high group

- Relationship: N065; mapped B37. Compared locations and roles: REPORT [main PDF p.5](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco never,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 549/987 (55.5%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×549/987=55.623100304%, which rounds to55.6% under nearest-one-decimal rounding. Printed55.5% differs by0.123100304 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Tobacco never,n/N(%) percentage55.5%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B37-L: Tobacco never,n/N(%), low group

- Relationship: N065; mapped B37. Compared locations and roles: REPORT [main PDF p.5](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco never,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 525/985 (53.2%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×525/985=53.299492386%, which rounds to53.3% under nearest-one-decimal rounding. Printed53.2% differs by0.099492386 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Tobacco never,n/N(%) percentage53.2%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B38-H: Tobacco previous,n/N(%), high group

- Relationship: N066; mapped B38. Compared locations and roles: REPORT [main PDF p.5](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco previous,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 273/987 (27.6%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×273/987=27.659574468%, which rounds to27.7% under nearest-one-decimal rounding. Printed27.6% differs by0.059574468 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Tobacco previous,n/N(%) percentage27.6%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B39-L: Tobacco current,n/N(%), low group

- Relationship: N067; mapped B39. Compared locations and roles: REPORT [main PDF p.5](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco current,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 186/985 (18.8%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×186/985=18.883248731%, which rounds to18.9% under nearest-one-decimal rounding. Printed18.8% differs by0.083248731 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Tobacco current,n/N(%) percentage18.8%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B63-H: Antibiotic prophylaxis,n/N(%), high group

- Relationship: N091; mapped B63. Compared locations and roles: REPORT [main PDF p.6](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Antibiotic prophylaxis,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 938/987 (94.8%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×938/987=95.035460993%, which rounds to95.0% under nearest-one-decimal rounding. Printed94.8% differs by0.235460993 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Antibiotic prophylaxis,n/N(%) percentage94.8%, and which printed component should be used when the cell is reconciled?

### NB-PCT-B63-L: Antibiotic prophylaxis,n/N(%), low group

- Relationship: N091; mapped B63. Compared locations and roles: REPORT [main PDF p.6](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Antibiotic prophylaxis,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 949/985 (96.1%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×949/985=96.345177665%, which rounds to96.3% under nearest-one-decimal rounding. Printed96.1% differs by0.245177665 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Antibiotic prophylaxis,n/N(%) percentage96.1%, and which printed component should be used when the cell is reconciled?

### NB-ALLOC: abstract randomized-group populations equal analyzed populations

- Relationships:N002,N007,N008.
- Compared locations and roles: REPORT [main PDF p.1](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), abstract INTERVENTIONS, “Patients were randomized” H n=989/L n=987; REPORT [main PDF p.3](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), Figure1 allocated H1011/L1002 and primary-analysis H989/L987; REPORT [main PDF p.4](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Results2013 randomized and1976 analyzed.
- Printed inputs:989,987 vs1011,1002;2013 randomized;1976 analyzed.
- Rule/calculation: randomized group counts should describe the same allocation population;989+987=1976 vs1011+1002=2013. Differences22 high and15 low sum37, equal2013−1976.
- Tolerance:zero for exact counts and population labels.
- Direct observation: identical abstract and Figure1 analysis counts are called randomized in the abstract; flow separately labels the larger randomized counts. Inference: abstract may have inserted analysis sizes into intervention description.
- Alternatives: abstract may conventionally summarize treatment groups using their analyzed sizes; that resolves the intended referent if expressly relabeled, but does not make the literal allocation populations equal.
- Quality-control relevance: extraction of allocated versus analyzed denominators may differ by37 patients.
- Exact human question: Should the abstract INTERVENTIONS group sizes describe randomized allocation1011/1002 or analyzed patients989/987?

### NB-HYPO-CI: matched hypoxemia confidence-limit sign differs

- Relationship:N005.
- Compared locations and roles: REPORT [main PDF p.1](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), abstract Results hypoxemia difference−8.6%,95%CI−11.1% to positive6.1%,P<.001; REPORT [main PDF p.9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 hypoxemia same difference−8.6%,95%CI−11.1 to−6.1,P<.001.
- Printed inputs:upper endpoint+6.1 versus−6.1; same outcome,groups,time,difference and P.
- Rule/calculation: matching confidence limits should agree at equal display precision;(+6.1)−(−6.1)=12.2 percentage points. Abstract interval crosses0 while Table3 interval does not.
- Tolerance:zero for matched signs; endpoint display±0.05 cannot reconcile12.2.
- Direct observation: sign mismatch; inference: a minus sign may have been omitted. No CI convention needs to be assumed for matched-source equality.
- Alternatives: no distinct model/population is labeled for the abstract estimate; a separate analysis would need identification. Source layout text expressly retains the positive sign.
- Quality-control relevance: interval crossing of the null differs for downstream extraction.
- Exact human question: Which signed upper confidence limit belongs to the abstract hypoxemia difference, and is the abstract intended to reproduce Table3?

### NB-APPROACH: complementary surgical-approach rows switch denominators

- Relationships:N098,N101; contextual N003,N099,N100.
- Compared locations and roles: REPORT [main PDF p.6](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Surgical approach “Type of abdominal incision” H894/986(90.7),L884/987(89.6); REPORT same table “Nonabdominal” H92/987(9.3),L102/986(10.3); REPORT same footnotes a (some characteristics missing) and i (abdominal open/endoscopic definitions).
- Printed inputs:high denominators986 versus987;low987 versus986;high counts894+92;low884+102.
- Rule/calculation: abdominal and nonabdominal are complementary labels for one surgical-approach classification and would ordinarily share an observed-population denominator. Both count sums=986, while the displayed denominators alternate986/987. High count sum agrees abdominal denominator986 but differs nonabdominal987 by1; low count sum agrees nonabdominal986 but differs abdominal987 by1. Endoscopic+open sums exactly894/884.
- Tolerance:zero for exact denominators/sums.
- Direct observation: denominator switches and count sums. Inference: denominator transposition or differently missing category indicators; a common underlying population is a label-based assumption.
- Alternatives: independently missing category-specific binary indicators could legitimately use different denominators; footnote a permits missingness but does not describe such separate indicators or explain complementary rows.
- Quality-control relevance: denominator and missingness extraction for surgical approach becomes ambiguous.
- Exact human question: Were abdominal and nonabdominal surgery measured as one mutually exclusive classification; if so what common denominator applies in each group, and if not why do their category-specific denominators differ?

### NB-RR-PPC: labeled risk ratio differs from printed patient-risk ratio

- Relationship:N004. Exact compared locations and roles: REPORT main p.1 abstract Results;p.8 Primary Outcome narrative;Table3 p.9 primary PPC;Figure2 p.10 pooled row; REPORT [main PDF p.9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 primary pulmonary complications within5days count cells/H989 L987 headers and “Risk Ratio” estimate; REPORT [main PDF p.4](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods binary outcome RR/Wald-likelihood-approximation rule. Additional location links: [p.1](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=1),[p.8](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=8),[p.10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Printed inputs:H211/989,L233/987;RR0.93.
- Rule/calculation: unadjusted high-versus-low risk ratio=(H events/H patients)/(L events/L patients)=(211/989)/(233/987)=0.903748096, displaying0.90; printed0.93 differs by0.026251904.
- Tolerance:±0.005 for a two-decimal ratio. Exact patient counts used; direction high/low stated.
- Direct observation versus inference: printed counts and ratio label are direct; arithmetic mismatch follows the ordinary risk-ratio definition. An estimate from another model/population or another effect measure is an inferred possible mechanism.
- Alternatives: covariate/site adjustment, transformation, or a different population could produce another estimate, but none is labeled for this repeated result; Wald CI approximation alone does not redefine the ratio of observed risks. Statistical checkers examine the inferential method and any alternative scale independently.
- Quality-control relevance: effect-size extraction as patient risk ratio differs from reconstructing it from counts, potentially affecting secondary evidence synthesis; no paper-level conclusion asserted.
- Exact human question: What estimand, model, reference group and analysis population generated the printed0.93 “risk ratio” for primary pulmonary complications within5days, and how does it relate to the printed211/989 versus233/987 patient risks?

### NB-RR-HYPO: labeled risk ratio differs from printed patient-risk ratio

- Relationship:N005. Exact compared locations and roles: REPORT main Table3 p.9 hypoxemia;abstract p.1 printed risks5.0%/13.6%; REPORT [main PDF p.9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 intraoperative hypoxemia count cells/H989 L987 headers and “Risk Ratio” estimate; REPORT [main PDF p.4](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods binary outcome RR/Wald-likelihood-approximation rule. Additional location links: [p.1](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=1),[p.8](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=8),[p.10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Printed inputs:H49/989,L134/987;RR0.51.
- Rule/calculation: unadjusted high-versus-low risk ratio=(H events/H patients)/(L events/L patients)=(49/989)/(134/987)=0.364932164, displaying0.36; printed0.51 differs by0.145067836.
- Tolerance:±0.005 for a two-decimal ratio. Exact patient counts used; direction high/low stated.
- Direct observation versus inference: printed counts and ratio label are direct; arithmetic mismatch follows the ordinary risk-ratio definition. An estimate from another model/population or another effect measure is an inferred possible mechanism.
- Alternatives: covariate/site adjustment, transformation, or a different population could produce another estimate, but none is labeled for this repeated result; Wald CI approximation alone does not redefine the ratio of observed risks. Statistical checkers examine the inferential method and any alternative scale independently.
- Quality-control relevance: effect-size extraction as patient risk ratio differs from reconstructing it from counts, potentially affecting secondary evidence synthesis; no paper-level conclusion asserted.
- Exact human question: What estimand, model, reference group and analysis population generated the printed0.51 “risk ratio” for intraoperative hypoxemia, and how does it relate to the printed49/989 versus134/987 patient risks?

### NB-RR-MILD: labeled risk ratio differs from printed patient-risk ratio

- Relationship:N022. Exact compared locations and roles: REPORT main p.8 Primary Outcome narrative;Table3 p.9 mild respiratory failure; REPORT [main PDF p.9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 mild respiratory failure count cells/H989 L987 headers and “Risk Ratio” estimate; REPORT [main PDF p.4](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods binary outcome RR/Wald-likelihood-approximation rule. Additional location links: [p.1](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=1),[p.8](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=8),[p.10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Printed inputs:H135/989,L154/987;RR0.92.
- Rule/calculation: unadjusted high-versus-low risk ratio=(H events/H patients)/(L events/L patients)=(135/989)/(154/987)=0.874850630, displaying0.87; printed0.92 differs by0.045149370.
- Tolerance:±0.005 for a two-decimal ratio. Exact patient counts used; direction high/low stated.
- Direct observation versus inference: printed counts and ratio label are direct; arithmetic mismatch follows the ordinary risk-ratio definition. An estimate from another model/population or another effect measure is an inferred possible mechanism.
- Alternatives: covariate/site adjustment, transformation, or a different population could produce another estimate, but none is labeled for this repeated result; Wald CI approximation alone does not redefine the ratio of observed risks. Statistical checkers examine the inferential method and any alternative scale independently.
- Quality-control relevance: effect-size extraction as patient risk ratio differs from reconstructing it from counts, potentially affecting secondary evidence synthesis; no paper-level conclusion asserted.
- Exact human question: What estimand, model, reference group and analysis population generated the printed0.92 “risk ratio” for mild respiratory failure, and how does it relate to the printed135/989 versus154/987 patient risks?

### NB-RR-EFFUSION: labeled risk ratio differs from printed patient-risk ratio

- Relationship:N023. Exact compared locations and roles: REPORT main p.8 Primary Outcome narrative;Table3 p.9 pleural effusion; REPORT [main PDF p.9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 pleural effusion count cells/H989 L987 headers and “Risk Ratio” estimate; REPORT [main PDF p.4](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods binary outcome RR/Wald-likelihood-approximation rule. Additional location links: [p.1](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=1),[p.8](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=8),[p.10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Printed inputs:H43/989,L21/987;RR1.35.
- Rule/calculation: unadjusted high-versus-low risk ratio=(H events/H patients)/(L events/L patients)=(43/989)/(21/987)=2.043478261, displaying2.04; printed1.35 differs by0.693478261.
- Tolerance:±0.005 for a two-decimal ratio. Exact patient counts used; direction high/low stated.
- Direct observation versus inference: printed counts and ratio label are direct; arithmetic mismatch follows the ordinary risk-ratio definition. An estimate from another model/population or another effect measure is an inferred possible mechanism.
- Alternatives: covariate/site adjustment, transformation, or a different population could produce another estimate, but none is labeled for this repeated result; Wald CI approximation alone does not redefine the ratio of observed risks. Statistical checkers examine the inferential method and any alternative scale independently.
- Quality-control relevance: effect-size extraction as patient risk ratio differs from reconstructing it from counts, potentially affecting secondary evidence synthesis; no paper-level conclusion asserted.
- Exact human question: What estimand, model, reference group and analysis population generated the printed1.35 “risk ratio” for pleural effusion, and how does it relate to the printed43/989 versus21/987 patient risks?

### NB-MILD-DIFF: narrative mild-failure absolute difference is outside nearest-decimal tolerance

- Relationship:N022. Compared locations and roles: REPORT [main PDF p.8](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), Primary Outcome narrative mild respiratory failure135(13.7%) vs154(15.6%), difference−1.9%; REPORT [main PDF p.9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 same counts,headers989/987,and difference−1.9%.
- Printed inputs:135/989,154/987,−1.9 percentage points.
- Rule/calculation: exact count-based difference=100×135/989−100×154/987=-1.952685211 percentage points, nearest-one-decimal−2.0, differing from−1.9 by0.052685211 point.
- Tolerance:±0.05 point; exceedance approximately0.002685 point beyond tolerance.
- Direct observation: printed counts and difference; reproducible arithmetic. Inference: subtraction of already-rounded13.7−15.6=−1.9 or truncation toward zero can reproduce display.
- Alternatives: deliberate subtraction of rounded group percentages or truncation can explain this very small difference; a modeled difference or alternative denominator is possible but unreported. Preserve that explanation rather than asserting an arithmetic failure under all conventions.
- Quality-control relevance: small precision inconsistency affects mechanically reconstructed risk difference; no clinical consequence inferred.
- Exact human question: Was the−1.9-point mild-failure difference computed from rounded percentages, truncation, raw risks or a modeled estimate, and what display convention should govern its reconciliation?

## Completed coverage and limitations

All102 compound records checked;18 local candidates:10 baseline percentage cells,1 allocation-label comparison,1 CI sign repetition,1 complementary-denominator comparison,4 repeated risk-ratio identities,1 repeated mild-failure difference. Flow,percentages,treatment values,repeated sites/countries,category sums,population totals,continuous scale checks and missingness were examined without general design auditing. No coherent display-zero P occurs in this scope. Statistical inference/sample-size exact reconstruction remains assigned to statistical specialists; missing variance/design conventions do not create unsupported candidates. White-cell scale diagnostic lacks a second matched baseline measurement and is recorded as a limitation in inventory. Missing baseline observed populations cannot be reconstructed from footnote a alone. Candidate rounding checks state conditional display assumptions explicitly. No source changes or scientific coverage gap.

