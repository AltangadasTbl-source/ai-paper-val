# DOC-001 Main-Article Quantitative Evidence Map

**Source:** `jama_thomas_2017_oi_170130.pdf` (PDF pp. 1-10; printed article pp. 1903-1912).  
**Fresh evidence used:** `preprocessing/native_text/jama_thomas_2017_oi_170130.txt`, `preprocessing/layout_text/jama_thomas_2017_oi_170130.layout.txt`, and the fresh DOC-001 page renders where tables/figures required visual confirmation. Exact locations below use PDF page numbering.

## Study identity, populations, and outcome definitions

| Location | Extracted quantitative/identity evidence |
|---|---|
| PDF p.1, abstract | Open-label randomized trial at 9 centers in Australia, New Zealand, Singapore, and Hong Kong; recruitment July 2012-October 2014; 12-month follow-up ending October 16, 2015. Included symptomatic malignant pleural-effusion patients, `n=146`, without prior IPC or pleurodesis. Randomized 1:1: IPC `n=74`, talc pleurodesis `n=72`; minimized by malignancy and trapped lung and stratified by Australia vs Asia. |
| PDF p.2, Methods/Randomization | Nine named centers. Adult eligibility; exclusion includes age `<18`, effusion depth `<2 cm`, expected survival `<3 months`, leukocytes `<1000/µL` (conversion supplied: multiply by 0.001 for ×10^9/L). Allocation probability varied `0.5-0.8`; balancing factors were mesothelioma/nonmesothelioma and trapped lung/not; regional strata Australia/New Zealand vs Singapore/Hong Kong. |
| PDF p.3, Outcomes | Primary endpoint: all hospital days from trial intervention to death or the 12-month visit; hospital/hospice admission must involve `≥1` day, one day crosses midnight; day-case procedures excluded. Secondary: pleural-effusion-related days/episodes, further pleural drainage, VAS breathlessness, VAS and modified EQ5D QoL, survival, adverse/serious adverse events. VAS breathlessness is `100 mm`, no breathlessness `100`, worst `0`; daily first `14 d`, then months `1,3,6,9,12`. EQ5D/VAS timing and EQ5D scale are documented in Table 1 notes (PDF p.4). |
| PDF p.3, Figure 1 | Eligibility: `226` assessed = `146` randomized + `80` excluded (`25` ineligible + `38` declined + `17` other). Ineligible detail: expected survival `<3 mo, n=5`; logistical inability to care for IPC `n=4`; prior pleurodesis `n=6`; nonmalignant cause `n=7`; asymptomatic `n=3` (sum `25`). IPC: `74` randomized, `72` received assigned IPC, `2` did not (severe loculation `1`, pre-treatment withdrawal `1`); talc: `72` randomized, `64` received assigned treatment, `8` did not (catheter fell out `4`, trapped lung `2`, severe loculation `1`, pre-treatment withdrawal `1`). One long-term withdrawal per arm. ITT: IPC `73`, talc `71`; one pre-treatment withdrawal excluded per arm. Per protocol: IPC `71`, talc `63`. |
| PDF pp.3-4, analysis plan | Power: detect `≥5 d`, `80%` power, `α=.05`; previous study difference `11.5 d`; estimated `65/group` based on total stay `18 d`, talc SD `9.3 d`; recruitment target `146` allows `12%` loss. Two-sided ITT analyses. Primary: Mann-Whitney U with Hodges-Lehmann (HL) location shift/95% CI; supporting negative binomial adjusted for follow-up length, minimization variables, and random center. VAS/EQ5D: linear mixed effects, treatment/time/time-dependent covariates, individual and center random effects, minimization adjustment; missing outcomes sensitivity analysis with multiple imputation. Death proportions χ²; survival log-rank and adjusted Cox. Further intervention Fisher exact. Significance `.05`, two-sided; secondary analyses exploratory/no multiplicity adjustment. |

## Baseline and flow values

| Location | Measure (population/scale) | IPC | Talc | Cross-location or arithmetic mapping |
|---|---|---:|---:|---|
| PDF p.1 abstract; p.4 Results | Randomized analysis base | 74 | 72 | `74+72=146`; abstract reports median age `70.5 y`, male `56.2%`. |
| PDF p.4 Table 1 | Age, median (range), years | 71.0 (38-92) | 70.5 (43-90) | Overall reported median/range p.4: `70.5 (38-92)`. |
| PDF p.4 Table 1 | Male, No. (%) | 39 (53) | 43 (60) | `39+43=82`; `82/146=56.16%`, matching abstract/Results `56.2%` after rounding. |
| PDF p.4 Table 1 | Right intervention side, No. (%) | 44 (59) | 38 (53) | Denominators are randomized arm sizes 74 and 72. |
| PDF p.4 Table 1 | Malignancy: mesothelioma / lung / breast / others | 20 (27) / 19 (26) / 14 (19) / 21 (28) | 18 (25) / 29 (40) / 4 (6) / 21 (29) | Per arm categories sum `74` and `72`; total lung `48`, mesothelioma `38`, breast `18`, as Results narrative reports. |
| PDF p.4 Table 1 | Known trapped lung, No. (%) | 2 (3) | 3 (4) | Defined as incomplete ipsilateral expansion after drainage. |
| PDF p.4 Table 1 | ECOG 0-2 / 3-4 / unknown, No. (%) | 53 (72) / 19 (26) / 2 (3) | 53 (74) / 14 (19) / 5 (17) | Counts each total 74/72. Printed talc unknown percentage is `17`; count `5/72` is about `6.9%` (this exact printed count/percentage pairing is preserved for later checking). ECOG scale 0 fully active to 5 dead. |
| PDF p.4 Table 1 | Effusion grade small (0-1) / moderate (2-3) / large (4-5) | 0 / 38 (51) / 36 (49) | 0 / 38 (53) / 34 (47) | Nonzero counts total 74/72. Grade definition: 0 no fluid, 1 blunted angle, 2-5 <25%, 25-50%, 51-75%, >75% hemithorax. |
| PDF p.4 Table 1 | Baseline VAS dyspnea mean (SD), mm | 48.4 (27.0) | 50.2 (26.0) | VAS direction: no breathlessness=100, worst=0. |
| PDF p.4 Table 1 | Baseline VAS QoL mean (SD), mm | 51.6 (26.1) | 55.9 (25.1) | Direction: best QoL=100, worst=0. |
| PDF p.4 Table 1 | Baseline EQ5D mean (SD) | 31.3 (10.5) | 32.6 (9.7) | Five domains graded 0-10; total maximum 50. |
| PDF p.4 Results | Analysis populations | 73 ITT; 71 per protocol | 71 ITT; 63 per protocol | ITT `73+71=144` after two pre-treatment withdrawals; per protocol `71+63=134`, excluding `3+9=12` not receiving full allocation. |

## Outcome/result extraction

| Location | Endpoint, population, contrast/direction | Printed values and labels |
|---|---|---|
| PDF p.1 abstract; p.4; p.6 Table 2 | ITT total all-cause hospital stay, IPC vs talc, procedure to death/12 mo | Medians (IQR) `10 (3-17)` vs `12 (7-21) d`; means (SD) `12.7 (13.4)` vs `16.3 (15.2) d`; HL location difference `2.92 d (95% CI 0.43-5.84)`, `P=.03`. Narrative calls mean reduction `3.6 d/patient`. |
| PDF p.4 Results | Overall hospital burden, all randomized analysis population | Median `10.0 d (IQR 4-19)`, mean `14.5 (14.4) d`; days in trial median `7.1% (IQR 1.9%-28.3%)`, mean `21.0 (29.0)%`. |
| PDF p.4 Results | Per-protocol all-cause stay, IPC vs talc | Medians `10 (3-17)` vs `13 (7-22) d`; HL `3.38 d (0.85-6.62)`, `P=.02`; means `12.6 (13.4)` vs `17.1 (15.8)`, stated mean reduction `4.5 d/patient`. |
| PDF p.5; p.6 Table 2 | ITT effusion-related stay, IPC vs talc | Medians `1 (1-3)` vs `4 (3-6) d`; means `3.1 (4.3)` vs `4.7 (3.1) d`; HL `2.06 d (1.53-2.58)`, `P<.001`; adjusted `P<.001`. |
| PDF p.6 Table 2 | ITT non-effusion-related stay, IPC vs talc | Medians `5 (1-13)` vs `7 (2-15) d`; means `9.6 (12.7)` vs `11.6 (14.7) d`; HL `0.92 d (-1.10 to 3.73)`, `P=.37`. |
| PDF p.5 | Initial admission days, IPC vs talc | Medians `1 (1-2)` vs `3 (3-4) d`; HL `2.09 d (1.78-2.39)`, `P<.001`. |
| PDF p.5 | Subsequent effusion-related days, IPC vs talc | Medians `0 (0-1)` vs `0 (0-0.5) d`; HL `-0.18 d (-0.41 to 0.01)`, `P=.08`. |
| PDF p.5; p.6 | Further ipsilateral invasive drainage, ITT IPC vs talc | `3/73 (4.1%)` vs `16/71 (22.5%)`; Table 2 rounded display `3 (4)` vs `16 (22)`; difference in proportions `0.18 (0.08-0.29)`, `P=.001`. Pleurodesis failure `16 (22.5%)`, median to drainage `32 d (15.5-72.5)`. Subsequent treatments: IPC `10`, repeat therapeutic drainage `3`, repeat talc `2` (one repeat failure then surgery), and one thoracotomy/partial pleurectomy/pericardial window; IPC-arm further punctures `3`. |
| PDF p.5 | IPC removal among those receiving IPC | `25/83 (30.1%)`; randomized IPC `21/73 (28.8%)`; IPC after failed pleurodesis `4/10 (40%)`. |
| PDF pp.5-6; Table 2 | VAS dyspnea estimated mean (95% CI), mm, IPC vs talc; difference labelled estimated mean difference | Baseline `50.0 (37.2-62.7)` vs `52.2 (39.3-63.1)`, diff `2.27 (-5.33 to 9.88), P=.56`; day 1 `64.5 (51.4-75.5)` vs `69.7 (56.5-82.9)`, `5.25 (-3.21 to 13.71), .22`; day 30 `69.7 (56.7-82.6)` vs `72.2 (59.0-85.5)`, `2.58 (-5.91 to 11.08), .55`; month 6 `71.1 (57.8-84.5)` vs `71.2 (57.3-85.1)`, `0.03 (-9.89 to 9.96), .99`; month 12 `69.4 (55.4-83.4)` vs `59.0 (44.6-73.4)`, `-10.42 (-21.90 to 1.06), .07`. Narrative baseline means `50.8 (39.9-61.6)` and `52.8 (42.0-63.5)`; day-1 improvements `14.5 (8.4-20.7)` and `17.4 (11.1-23.7) mm`; no significant magnitude difference. |
| PDF p.6 Table 2 | VAS QoL estimated mean (95% CI), mm, IPC vs talc | Baseline `52.4 (43.4-61.4)` vs `56.7 (47.5-65.9)`, `4.24 (-3.76 to 12.25), .27`; day 2 `60.3 (50.9-69.7)` vs `58.5 (48.9-68.1)`, `-1.75 (-10.65 to 7.14), .74`; day 30 `61.5 (52.2-70.8)` vs `67.3 (57.6-77.0)`, `5.79 (-3.11 to 14.69), .17`; month 6 `67.4 (57.6-77.3)` vs `66.1 (55.5-76.7)`, `-1.27 (-11.64 to 9.09), .89`; month 12 `61.7 (50.9-72.4)` vs `56.3 (45.0-67.6)`, `-5.34 (-17.30 to 6.62), .43`. |
| PDF p.6 Table 2 | EQ5D estimated mean (95% CI), IPC vs talc | Baseline `31.2 (26.7-35.7)` vs `32.3 (27.8-36.8)`, `1.12 (-2.34 to 4.59), .46`; day 8 `34.1 (29.5-38.7)` vs `35.3 (30.6-40.0)`, `1.18 (-2.73 to 5.10), .48`; day 30 `35.2 (30.6-39.8)` vs `34.5 (29.8-39.2)`, `-0.67 (-4.59 to 3.23), .86`; month 6 `33.9 (29.1-38.7)` vs `33.1 (28.0-38.1)`, `-0.84 (-5.34 to 3.66), .84`; month 12 `32.4 (27.3-37.5)` vs `31.5 (26.2-36.8)`, `-0.92 (-6.07 to 4.22), .83`. |
| PDF pp.5-6; Table 2 | Death/survival, ITT IPC vs talc | Median follow-up `204 d`; deaths `44/73 (60.3%)` vs `51/71 (71.8%)`; Table 2 rounded `44 (60)` vs `51 (72)`, proportion difference `0.12 (-0.05 to 0.28), P=.20`; log-rank `P=.13`; adjusted HR `0.68 (0.46-1.04), P=.07`. |
| PDF p.6; Figure 2 | Post-hoc hospital time / total trial days, IPC vs talc | Medians `6.2% (1.1%-15.0%)` vs `11.1% (3.2%-37.0%)`; HL `3.11% (0.38%-7.95%)`, `P=.01`. Figure 2 shows total stay and percentage, `n=73` IPC, `n=71` talc; box medians/IQR, whiskers 10th/90th percentiles; left `P=.03`, right `P=.01`. |
| PDF pp.7-8 | Post-hoc metastatic cancer subgroup (`n=106`), IPC vs talc | Total stay medians `10.0 (4-16)` vs `14.0 (7-22) d`; HL `3.44 (0.55-7.14) d`, `P=.03`. Effusion stay `2 (1-3)` vs `4 (3-6) d`; HL `2.1 (1.48-2.71) d`, `P<.001`. |
| PDF p.8 | Post-hoc mesothelioma subgroup, IPC vs talc | Effusion stay medians `1 (1-3)` vs `3 (2-4) d`; HL `1.68 (0.90-2.42) d`, `P=.003`. |
| PDF p.8 | Post-hoc admissions, IPC vs talc | Initial admission medians `2 (1-4)` vs `3 (3-6) d`; HL `1.85 (1.30-2.41)`, `P<.001`. Subsequent admissions `4 (0-12)` vs `6 (0-16) d`; HL `0.61 (-0.68 to 3.57)`, `P=.34`. No missing hospitalization-day data; QoL/breathlessness data `19%` missing; multiple-imputation sensitivity analysis described as consistent. |
| PDF p.7 Figure 3 | Patient-reported outcomes: time/analysis unit | Linear-mixed-model estimated means with 95% CI; time 0=intervention; sample size varies owing to missing data. At sequential plotted visits, VAS dyspnea and VAS QoL group counts IPC `66,56,53,49,47,44,37,33,37,27,23`; talc `64,47,44,38,42,38,39,28,27,18,20`. EQ5D counts IPC `71,56,53,49,47,44,37,33,37,27,23`; talc `68,46,44,38,42,38,39,28,27,18,20`. Axis time 0,3,6,9,12 months; scale 0-100 VAS, 0-50 EQ5D. |
| PDF p.6; p.8 Table 3 | Adverse events, IPC vs talc | Serious-event patients `1 (1%)` vs `3 (4%)`. Event counts: pleural infection `2/1`, cellulitis `4/0`, symptomatic loculation `1/1`, catheter blockage `3/0`, pneumothorax `1/1`, procedure pain `6/4`, worsening breathlessness `4/6`, tube dislodgement `1/4`, others `7/3`; nonserious total `29/20`, serious total `1/3`, total adverse+serious `30/23`, patients affected by any event `22 (30%)/13 (18%)`. Narrative matches `30` events in `22 (30%)` IPC patients and `23` in `13 (18%)` talc patients. |

## Narrative cross-location statements retained for matching

- PDF pp.1-2 Key Points/abstract, p.4 Results, p.8 Discussion, and p.9 Conclusions all describe fewer total hospital days for IPC than talc, with primary medians 10 vs 12 days and uncertain clinical importance.
- PDF p.1 abstract, p.5, p.6 Table 2, and p.8 Discussion describe fewer further ipsilateral procedures with IPC: 3/73 (4.1%) vs 16/71 (22.5%); the discussion rounds these to 4% vs 23%.
- PDF pp.1, 5, and 8 state no significant between-group difference in breathlessness/QoL improvement; Table 2 supplies the time-specific estimated mean differences and P values.
- PDF p.1 abstract and pp.6/8 Table 3 provide the same aggregate adverse-event counts, patients, and arm-specific totals.

## Extraction limitations

Native and layout text were usable for all pages. Figure 3 exposes plotted sample-size sequences but not numerical point estimates beyond its axes; Table 2 is the exact tabular numerical source for the displayed selected time points. Page 10 contains disclosures/references and no trial-result relationship requiring extraction.
