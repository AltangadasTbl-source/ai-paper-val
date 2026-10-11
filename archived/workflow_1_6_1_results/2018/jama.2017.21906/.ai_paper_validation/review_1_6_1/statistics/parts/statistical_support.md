# Statistical Relationship Inventory — Support Baseline and Graph Shard

Pass: 1. Runtime agent: `/root/statistics_1_support`; model `gpt-6.1-sol`; reasoning effort `high`; fresh statistical specialist. Assigned scope is REPORT DOC-004 physical pp. 17–20 and 24–27, with p. 1 contents as local context. No PLAN family, main-paper relationship, or eTable 5–7 outcome tuple is assigned to this shard. The coordinator reassigned eTables 5–7 to a separate fresh high-effort agent after discovering that eTable 2 has 51 tuples rather than only 17 difference tuples. This shard covers 83 stable relationships, S155–S237: 68 printed estimate/95% CI tuples, 12 graphical families, and 3 method/context families. Grouped graphical families have exhaustive cohort/step visual inspection records below; no plotted interval is sampled.

Source: `joi170166supp3_prod.pdf`; document role at every assigned location is REPORT. Exact PDF page locators in this part use paths relative to this part's directory. When merged to the canonical inventory, adjust the relative path depth without changing pages. Locator and visual evidence are source-matched native/layout extraction and reusable renders `review_1_5_2/preprocessing/rendered_pages/DOC-004-17.png` through `DOC-004-20.png` and `DOC-004-24.png` through `DOC-004-27.png`; no old conclusions were read. All eight assigned result pages were visually inspected. Direct source p. 1 was read with available Poppler 25.03.0 `pdftotext -f 1 -l 1 -layout ... -`; no new derivative was produced. Tool routing and source role follow the current tooling and source inventories.

## Rules and supplied definitions

For each printed tuple, verify lower ≤ estimate ≤ upper and lower ≤ upper. For differences, compare direction with the immediately adjacent groups, allowing half a displayed unit on each input. In eTable 1, headers are complete and missing follow-up, not intervention and control; the rows identify missing minus complete despite the footnote's group names. The immediate direction is clear. In eTable 2, the footnote explicitly defines intervention-minus-control differences of marginal effects from mixed-effects logistic, linear, or quantile regression with a hospital random effect and temporal trend. CI covariance, interval construction, degrees of freedom, row-specific model assignment, test statistic, standard error, and sidedness are not supplied for these baseline tuples. They must not be invented. Tables give 95% confidence levels but no P values. A compatible containment/direction check is not a reconstruction of an unreported test.

All table tuples below have ordered endpoints and contain their point estimate. The last column records the exact pass status of each relationship. For zero-width displayed creatinine CI 1.0–1.0, display precision allows a nonzero underlying width; no inference of zero uncertainty is made.

## eTable 1 — all 17 difference/95% CI tuples

Exact location for every row: [REPORT DOC-004 physical p. 17, eTable 1](../../../../joi170166supp3_prod.pdf#page=17), named characteristic and Difference column. Complete n=21079; missing n=295. Group descriptive values below are printed mean, percentage, or median values; SD and IQR are transcribed fully in the source map, and are not mistaken for inferential CIs.

| S ID | Characteristic; unit | Complete; missing | Difference (95% CI) | Pass-1 check | Status |
|---|---|---|---|---|---|
| S155 | Age; years | 60.6; 60.0 | −0.6 (−2.0 to 0.8) | Containment/order; missing−complete −0.6 | PASS_1_COMPLETE |
| S156 | Male; percentage points | 75.8; 71.2 | −4.6 (−9.8 to 0.6) | Containment/order; direction negative | PASS_1_COMPLETE |
| S157 | Tobacco history; percentage points | 30.8; 42.4 | 11.6 (5.9 to 17.3) | Containment/order; direction positive | PASS_1_COMPLETE |
| S158 | Diabetes history; percentage points | 44.4; 45.1 | 0.7 (−5.0 to 6.4) | Containment/order; direction positive | PASS_1_COMPLETE |
| S159 | Transferred; percentage points | 39.2; 44.4 | 5.2 (−0.5 to 10.9) | Containment/order; direction positive | PASS_1_COMPLETE |
| S160 | No insurance; percentage points | 72.7; 74.6 | 1.9 (−3.1 to 6.9) | Containment/order; direction positive | PASS_1_COMPLETE |
| S161 | STEMI; percentage points | 64.1; 59.3 | −4.8 (−10.4 to 0.9) | Containment/order; direction negative | PASS_1_COMPLETE |
| S162 | Symptom-to-door time; minutes | 246; 266 | 21 (−38 to 80) | Containment/order; integer-input half-unit intervals allow 21 | PASS_1_COMPLETE |
| S163 | Body weight; kg | 63.5; 62.6 | −0.9 (−2.0 to 0.2) | Containment/order; direction negative | PASS_1_COMPLETE |
| S164 | Systolic blood pressure; mmHg | 138.5; 138.9 | 0.4 (−2.9 to 3.7) | Containment/order; direction positive | PASS_1_COMPLETE |
| S165 | Heart rate; bpm | 79.9; 82.9 | 3.0 (0.8 to 5.2) | Containment/order; direction positive | PASS_1_COMPLETE |
| S166 | Initial troponin; ng/ml | 1.3; 4.6 | 3.3 (0.1 to 6.5) | Containment/order; direction positive; main P<.001 is not established as the same test | PASS_1_COMPLETE |
| S167 | LDL cholesterol; mg/dl | 122.4; 131.4 | 9.0 (3.2 to 14.8) | Containment/order; direction positive | PASS_1_COMPLETE |
| S168 | Triglycerides; mg/dl | 121; 128 | 7 (−3 to 17) | Containment/order; direction positive | PASS_1_COMPLETE |
| S169 | Serum creatinine; mg/dl | 1.0; 1.0 | 0.1 (−0.2 to 0.3) | Containment/order; one-decimal half-unit intervals allow difference 0.1 | PASS_1_COMPLETE |
| S170 | Fasting glucose; mg/dl | 127; 128 | 1 (−6 to 8) | Containment/order; direction positive | PASS_1_COMPLETE |
| S171 | Hemoglobin; mg/dl | 13.2; 13.2 | 0.0 (−0.3 to 0.2) | Containment/order; rounded equality consistent | PASS_1_COMPLETE |

## eTable 2 — all 51 marginal/difference estimate/95% CI tuples

Exact location for every row: [REPORT DOC-004 physical p. 18, eTable 2](../../../../joi170166supp3_prod.pdf#page=18), named characteristic and column. Control n=10066; intervention n=11308. C=Control marginal effect, I=Intervention marginal effect, D=Difference. Every point and both endpoints are retained individually. Differences are marginal intervention-minus-control effects; percentages differ in percentage points.

| S ID | Characteristic; unit | Column | Estimate (95% CI) | Pass-1 check | Status |
|---|---|---|---|---|---|
| S172 | Age; years | C | 60.7 (60.0 to 61.3) | Containment/order | PASS_1_COMPLETE |
| S173 | Age; years | I | 60.7 (60.1 to 61.3) | Containment/order | PASS_1_COMPLETE |
| S174 | Age; years | D | 0.0 (−0.5 to 0.6) | Containment/order; rounded I−C=0.0 | PASS_1_COMPLETE |
| S175 | Male; % | C | 75.3 (73.2 to 77.4) | Containment/order | PASS_1_COMPLETE |
| S176 | Male; % | I | 75.7 (73.8 to 77.6) | Containment/order | PASS_1_COMPLETE |
| S177 | Male; percentage points | D | 0.4 (−1.6 to 2.4) | Containment/order; positive I−C | PASS_1_COMPLETE |
| S178 | Tobacco history; % | C | 30.9 (27.2 to 34.5) | Containment/order | PASS_1_COMPLETE |
| S179 | Tobacco history; % | I | 29.1 (25.6 to 32.6) | Containment/order | PASS_1_COMPLETE |
| S180 | Tobacco history; percentage points | D | −1.8 (−3.9 to 0.4) | Containment/order; negative I−C | PASS_1_COMPLETE |
| S181 | Diabetes history; % | C | 45.4 (42.6 to 48.2) | Containment/order | PASS_1_COMPLETE |
| S182 | Diabetes history; % | I | 47.9 (45.2 to 50.6) | Containment/order | PASS_1_COMPLETE |
| S183 | Diabetes history; percentage points | D | 2.5 (0.1 to 4.8) | Containment/order; positive I−C | PASS_1_COMPLETE |
| S184 | Transferred; % | C | 28.5 (23.4 to 33.5) | Containment/order | PASS_1_COMPLETE |
| S185 | Transferred; % | I | 35.2 (29.7 to 40.7) | Containment/order | PASS_1_COMPLETE |
| S186 | Transferred; percentage points | D | 6.7 (4.8 to 8.7) | Containment/order; positive I−C | PASS_1_COMPLETE |
| S187 | No insurance; % | C | 78.5 (72.5 to 84.5) | Containment/order | PASS_1_COMPLETE |
| S188 | No insurance; % | I | 78.0 (72.0 to 84.0) | Containment/order | PASS_1_COMPLETE |
| S189 | No insurance; percentage points | D | −0.5 (−2.1 to 1.1) | Containment/order; negative I−C | PASS_1_COMPLETE |
| S190 | STEMI; % | C | 66.5 (60.7 to 72.3) | Containment/order | PASS_1_COMPLETE |
| S191 | STEMI; % | I | 64.7 (58.8 to 70.5) | Containment/order | PASS_1_COMPLETE |
| S192 | STEMI; percentage points | D | −1.8 (−3.7 to 0.2) | Containment/order; negative I−C | PASS_1_COMPLETE |
| S193 | Symptom-to-door time; minutes | C | 243 (193 to 293) | Containment/order | PASS_1_COMPLETE |
| S194 | Symptom-to-door time; minutes | I | 265 (162 to 368) | Containment/order | PASS_1_COMPLETE |
| S195 | Symptom-to-door time; minutes | D | 22 (−82 to 126) | Containment/order; positive I−C | PASS_1_COMPLETE |
| S196 | Body weight; kg | C | 64.6 (63.8 to 65.5) | Containment/order | PASS_1_COMPLETE |
| S197 | Body weight; kg | I | 63.7 (62.9 to 64.6) | Containment/order | PASS_1_COMPLETE |
| S198 | Body weight; kg | D | −0.9 (−1.4 to −0.5) | Containment/order; negative I−C | PASS_1_COMPLETE |
| S199 | Systolic blood pressure; mmHg | C | 140.0 (137.7 to 142.2) | Containment/order | PASS_1_COMPLETE |
| S200 | Systolic blood pressure; mmHg | I | 139.4 (137.3 to 141.6) | Containment/order | PASS_1_COMPLETE |
| S201 | Systolic blood pressure; mmHg | D | −0.6 (−1.9 to 0.8) | Containment/order; negative I−C | PASS_1_COMPLETE |
| S202 | Heart rate; bpm | C | 80.7 (79.6 to 81.8) | Containment/order | PASS_1_COMPLETE |
| S203 | Heart rate; bpm | I | 80.9 (79.8 to 81.9) | Containment/order | PASS_1_COMPLETE |
| S204 | Heart rate; bpm | D | 0.2 (−0.7 to 1.1) | Containment/order; positive I−C | PASS_1_COMPLETE |
| S205 | Initial troponin; ng/ml | C | 1.7 (0.9 to 2.5) | Containment/order | PASS_1_COMPLETE |
| S206 | Initial troponin; ng/ml | I | 1.1 (0.8 to 1.5) | Containment/order | PASS_1_COMPLETE |
| S207 | Initial troponin; ng/ml | D | −0.6 (−1.3 to 0.1) | Containment/order; negative I−C | PASS_1_COMPLETE |
| S208 | LDL cholesterol; mg/dl | C | 124.0 (121.0 to 127.0) | Containment/order | PASS_1_COMPLETE |
| S209 | LDL cholesterol; mg/dl | I | 122.5 (119.6 to 125.4) | Containment/order | PASS_1_COMPLETE |
| S210 | LDL cholesterol; mg/dl | D | −1.5 (−3.8 to 0.8) | Containment/order; negative I−C | PASS_1_COMPLETE |
| S211 | Triglycerides; mg/dl | C | 121 (109 to 133) | Containment/order | PASS_1_COMPLETE |
| S212 | Triglycerides; mg/dl | I | 121 (113 to 130) | Containment/order | PASS_1_COMPLETE |
| S213 | Triglycerides; mg/dl | D | 1 (−11 to 12) | Containment/order; integer-input half-unit intervals allow difference 1 | PASS_1_COMPLETE |
| S214 | Serum creatinine; mg/dl | C | 1.0 (0.9 to 1.1) | Containment/order | PASS_1_COMPLETE |
| S215 | Serum creatinine; mg/dl | I | 1.0 (1.0 to 1.0) | Containment/order; rounded CI width may be nonzero | PASS_1_COMPLETE |
| S216 | Serum creatinine; mg/dl | D | 0.0 (−0.1 to 0.1) | Containment/order; rounded I−C=0.0 | PASS_1_COMPLETE |
| S217 | Fasting glucose; mg/dl | C | 124 (114 to 134) | Containment/order | PASS_1_COMPLETE |
| S218 | Fasting glucose; mg/dl | I | 130 (125 to 135) | Containment/order | PASS_1_COMPLETE |
| S219 | Fasting glucose; mg/dl | D | 6 (−3 to 14) | Containment/order; positive I−C | PASS_1_COMPLETE |
| S220 | Hemoglobin; mg/dl | C | 13.2 (13.1 to 13.4) | Containment/order | PASS_1_COMPLETE |
| S221 | Hemoglobin; mg/dl | I | 13.2 (13.0 to 13.3) | Containment/order | PASS_1_COMPLETE |
| S222 | Hemoglobin; mg/dl | D | 0.0 (−0.1 to 0.1) | Containment/order; rounded I−C=0.0 | PASS_1_COMPLETE |

## Graphical and method relationships

| S ID | Exact source location; REPORT role | Relationship and supplied definition | Pass-1 result and named limit | Status |
|---|---|---|---|---|
| S223 | DOC-004 p. 24 eFigure 1A, full ranked display and caption; p. 1 contents context | All hospital residual points and 95% CIs; hospital random effect with temporal adjustment; zero is mean; lower-rate hospitals left, higher-rate hospitals right; nonoverlap zero represents 5% level | Every plotted stem/point inspected, including both tails and all zero crossings; visible intervals contain points and endpoints are ordered. Ascending rank/direction agrees with caption. Contents expected−observed wording differs, but the figure's own direction is explicit. No exact per-hospital estimates, residual scale transformation, interval construction, or hospital identities printed. | PASS_1_COMPLETE |
| S224 | DOC-004 p. 25 eFigure 1B, full ranked display, axis, legend, caption | Unadjusted decrease in 30-day MACE = control−intervention, percentage points; bubbles scaled to recruited participants; cohorts 1–5 | Every bubble inspected from highest positive to lowest negative; descending rank/direction agrees with control−intervention axis. No interval or test is plotted; no adjusted treatment effect is inferred. Exact hospital rates/IDs and scaling coefficient are not printed. | PASS_1_COMPLETE |
| S225 | DOC-004 p. 26 eFigure 2A cohort 1, all steps 0–5 | Unadjusted hospital MACE percentages/95% CIs; hollow control then filled intervention from step 1 | Complete six-cell inspection recorded below; all visible point/stem pairs contain point, endpoints ordered, direction/time phase coherent; exact hospital rates/counts/CI method absent | PASS_1_COMPLETE |
| S226 | DOC-004 p. 26 eFigure 2A cohort 2, all steps 0–5 | Same outcome; intervention from step 2 | Complete six-cell inspection below; same checks; overlapping or point-only symbols are not given invented intervals | PASS_1_COMPLETE |
| S227 | DOC-004 p. 26 eFigure 2A cohort 3, all steps 0–5 | Same outcome; intervention from step 3 | Complete six-cell inspection below; same checks and graphical limits | PASS_1_COMPLETE |
| S228 | DOC-004 p. 26 eFigure 2A cohort 4, all steps 0–5 | Same outcome; intervention from step 4 | Complete six-cell inspection below; same checks and graphical limits | PASS_1_COMPLETE |
| S229 | DOC-004 p. 26 eFigure 2A cohort 5, all steps 0–5 | Same outcome; intervention from step 5 | Complete six-cell inspection below; same checks and graphical limits | PASS_1_COMPLETE |
| S230 | DOC-004 p. 27 eFigure 2B cohort 1, all steps 0–5 | Unadjusted hospital 30-day mortality percentages/95% CIs; intervention from step 1 | Complete six-cell inspection below; all visible point/stem pairs contain point, endpoints ordered, phase coherent; exact values and CI method absent | PASS_1_COMPLETE |
| S231 | DOC-004 p. 27 eFigure 2B cohort 2, all steps 0–5 | Same mortality outcome; intervention from step 2 | Complete six-cell inspection below; same checks and graphical limits | PASS_1_COMPLETE |
| S232 | DOC-004 p. 27 eFigure 2B cohort 3, all steps 0–5 | Same mortality outcome; intervention from step 3 | Complete six-cell inspection below; same checks and graphical limits | PASS_1_COMPLETE |
| S233 | DOC-004 p. 27 eFigure 2B cohort 4, all steps 0–5 | Same mortality outcome; intervention from step 4 | Complete six-cell inspection below; same checks and graphical limits | PASS_1_COMPLETE |
| S234 | DOC-004 p. 27 eFigure 2B cohort 5, all steps 0–5 | Same mortality outcome; intervention from step 5 | Complete six-cell inspection below; same checks and graphical limits | PASS_1_COMPLETE |
| S235 | DOC-004 p. 17 eTable 1 title, headers, all rows and footnote | Complete versus missing follow-up baseline contrasts; mean/SD versus median/IQR distinguished; footnote intervention−control versus complete/missing headers | Immediate table values identify missing−complete. CI method, test type/sidedness, covariance, per-variable available-case counts, and row-specific estimation definitions not printed. No analysis-population count contradiction: 21079+295=21374. Absent implementation detail alone does not establish a logical gap. | PASS_1_COMPLETE |
| S236 | DOC-004 p. 18 eTable 2 title, all columns and footnote | Marginal baseline effects from mixed-effects logistic, linear, or quantile regression, random hospital effect and temporal trend | Stated clustering/time structure is coherent; all 17 marginal contrasts agree within precision. Mixed modeling is not replaced with crude arm estimates. No specified row covariance, interval construction, or test/SE for reconstruction. No statistical decision conclusion is attached to these baseline CIs. | PASS_1_COMPLETE |
| S237 | DOC-004 pp. 19–20 eTables 3–4, every step/arm column and creatinine footnote | Descriptive n/%, mean/SD and median/IQR, not inferential CIs; step/arm design and collection timing context | Every printed descriptive row/cell inspected; all available medians lie between their ordered quartiles; SDs nonnegative. eTable 3 creatinine first three columns NA, agreeing with eTable 4 not collected until step 3. Step totals correspond across tables. No P value, estimate/CI treatment contrast or decision rule is supplied here. Numeric denominator/cell accounting belongs to numeric checker. | PASS_1_COMPLETE |

Graph source links: [eFigure 1A p. 24](../../../../joi170166supp3_prod.pdf#page=24), [eFigure 1B p. 25](../../../../joi170166supp3_prod.pdf#page=25), [eFigure 2A p. 26](../../../../joi170166supp3_prod.pdf#page=26), [eFigure 2B p. 27](../../../../joi170166supp3_prod.pdf#page=27), [eTable 3 p. 19](../../../../joi170166supp3_prod.pdf#page=19), [eTable 4 p. 20](../../../../joi170166supp3_prod.pdf#page=20), [contents p. 1](../../../../joi170166supp3_prod.pdf#page=1).

## Exhaustive visual graph inspection record

The graphical scope is the complete source display. Within each cohort/step cell below, inspection moved left to right across every visible hospital symbol and its entire visible stem, including both endpoints, zero-rate markers, tall stems and isolated symbols. No hospital was selected as a sample. A separate stable S ID per cohort avoids pretending that unlabeled hospital marks have identified records. These visual checks do not assert source-printed numerical coordinates, reconstruct an interval hidden by overplotting, or infer hospital denominators. Hollow/filled phase and outcome identity were checked in every cell. `ALL` means every visible mark and every visible interval in the named cell, including overlaps; limits of individual endpoint separation are retained.

| Source panel; S ID | Step 0 | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 |
|---|---|---|---|---|---|---|
| eFigure 2A cohort 1; S225 | ALL; control; zero/tall stems checked | ALL; intervention; zeros and high marks checked | ALL; intervention; zeros/tall stems checked | ALL; intervention; zero and positive marks checked | ALL; intervention; zeros/tall stems checked | ALL; intervention; zero and positive marks checked |
| eFigure 2A cohort 2; S226 | ALL; control; zeros/tall stems checked | ALL; control; zero and positive marks checked | ALL; intervention; zeros/tall stems checked | ALL; intervention; zeros/high/point-only marks checked | ALL; intervention; zeros/high/point-only marks checked | ALL; intervention; zero and positive marks checked |
| eFigure 2A cohort 3; S227 | ALL; control; zeros/high/point-only marks checked | ALL; control; zeros/high/point-only marks checked | ALL; control; zero and positive marks checked | ALL; intervention; zero and positive marks checked | ALL; intervention; zeros/positive/point-only marks checked | ALL; intervention; zero and positive marks checked |
| eFigure 2A cohort 4; S228 | ALL; control; zero and positive marks checked | ALL; control; zero and positive marks checked | ALL; control; zeros/high/point-only marks checked | ALL; control; zero and positive marks checked | ALL; intervention; zeros/high/point-only marks checked | ALL; intervention; zeros/positive/point-only marks checked |
| eFigure 2A cohort 5; S229 | ALL; control; zeros/high/point-only marks checked | ALL; control; zero and positive marks checked | ALL; control; zero and positive marks checked | ALL; control; zero and positive marks checked | ALL; control; zeros/high/point-only marks checked | ALL; intervention; zero and positive marks checked |
| eFigure 2B cohort 1; S230 | ALL; control; zeros/high/point-only marks checked | ALL; intervention; zeros/tall stems checked | ALL; intervention; zeros/tall stems checked | ALL; intervention; zeros/tall stems checked | ALL; intervention; zero and positive marks checked | ALL; intervention; zero and positive marks checked |
| eFigure 2B cohort 2; S231 | ALL; control; zeros/tall stems checked | ALL; control; zeros/tall stems checked | ALL; intervention; zero and positive marks checked | ALL; intervention; zeros/high/point-only marks checked | ALL; intervention; zeros/high/point-only marks checked | ALL; intervention; zeros/positive/point-only marks checked |
| eFigure 2B cohort 3; S232 | ALL; control; zeros/high/point-only marks checked | ALL; control; zero and positive marks checked | ALL; control; zeros/high/point-only marks checked | ALL; intervention; zero and positive marks checked | ALL; intervention; zero and positive marks checked | ALL; intervention; zero and positive marks checked |
| eFigure 2B cohort 4; S233 | ALL; control; zero and positive marks checked | ALL; control; zeros/high/point-only marks checked | ALL; control; zero and positive marks checked | ALL; control; zero and positive marks checked | ALL; intervention; zeros/high/point-only marks checked | ALL; intervention; zero and positive marks checked |
| eFigure 2B cohort 5; S234 | ALL; control; zeros/high/point-only marks checked | ALL; control; zero and positive marks checked | ALL; control; zero and positive marks checked | ALL; control; zero and positive marks checked | ALL; control; zero and positive marks checked | ALL; intervention; zero and positive marks checked |

For every visible stem/marker pair in the sixty cells, the marker lies between the visible lower and upper endpoint; no reversed stem or displayed treatment-phase contradiction was observed. Some isolated marks do not have separately resolvable stems, and some upper endpoints approach or pass the visible scale maximum. Their numeric limits are not available from the source and no method or numeric interpretation is supplied to replace them. Confidence-level computation, clipping and interval construction cannot be reconstructed without hospital counts and the stated interval method. This is a graphical extraction limitation, not a scientific-coverage gap.

eFigure 1A S223: all ranked marks were checked sequentially, rank positions 1–10, 11–20, 21–30, 31–40, 41–50, 51–60, and all final positions beyond rank 60. Both extreme tails, all large stems and every zero crossing were inspected. Every marker lies within its visible interval; endpoint order and increasing residual rank are coherent. Caption directions follow the display. Whether a point's near-zero endpoint touches zero cannot be resolved numerically from an unlabeled graph; no exact significance list is invented.

eFigure 1B S224: all ranked bubbles were checked sequentially through the same exhaustive rank partitions and the final positions beyond 60. Positive, zero and negative marks agree with the control-minus-intervention y axis and decreasing order. No confidence interval is present. Bubble-size formula and hospital values are unreported, so neither count reconstruction nor crude-versus-modeled comparisons are attempted.

## Pass-1 completion and limitations

All 83 relationships explicitly record PASS_1_COMPLETE. No finding meets the inclusion threshold within this disjoint scope; observations and one reason code each are in `checkers/parts/statistical_support.md`. No pass-2 completion is asserted. Limitations are exact unprinted graph coordinates/IDs, unresolved stems under overlap or point-only marks, and unreported test/interval construction for baseline/graphical quantities. These prevent invented reconstruction but leave no assigned source unit or inferential tuple unreviewed. No superiority, noninferiority, equivalence, multiplicity, interim, stopping, or sample-size conclusion is newly stated in these assigned support displays; such conclusions in main/PLAN scopes are assigned elsewhere.
