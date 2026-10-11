# Main-paper quantitative evidence map — DOC001

Scope: `jama_driver_2018_oi_180054.pdf`, PDF pages 1–11 (printed pp. 2179–2189). This is a fresh map from the assigned OCR text and rendered pages. `N` IDs are numeric/reporting relationships and `S` IDs are inferential relationships. All locations below are direct-PDF links. A repeated abstract, Key Points, narrative, table, figure, caption, or footnote occurrence is retained as matched evidence rather than treated as a separate outcome.

## Page dispositions

| PDF page | Printed page | Disposition |
|---:|---:|---|
| 1 | 2179 | Mapped: abstract randomized totals, demographics, primary/all-patient success, duration, hypoxemia. |
| 2 | 2180 | Mapped: Key Points repeat of primary result; design/sample-definition and result-relevant eligibility context. |
| 3 | 2181 | Mapped: randomization/device units; outcome definitions; sample-size and analysis rules. |
| 4 | 2182 | Mapped: Figure 1 flow, allocation/adherence and difficult-airway totals; analysis methods. |
| 5 | 2183 | Mapped: primary/secondary narrative results and Table 1 baseline values/footnotes. |
| 6 | 2184 | Mapped: Table 2 process measures, denominators, contrasts, intervals, P values and footnotes. |
| 7 | 2185 | Mapped: Table 3 primary, planned-secondary and subgroup outcomes; first-failure total. |
| 8 | 2186 | Mapped: Figure 2, Table 4 rescue techniques and discussion repeats. |
| 9 | 2187 | Mapped: Table 5 complications and narrative repeats. |
| 10 | 2188 | Mapped: limitations with 7% protocol violation and proportional-hazards qualification; no new outcome display. |
| 11 | 2189 | No new trial result display; references only. |

## Design, population, and analysis definitions

| ID | Printed values / relationship | Population, contrast, unit, and exact location | Rule / matched evidence / signal |
|---|---|---|---|
| MAIN-N001 | Randomized: bougie `n=381`; endotracheal tube + stylet (ETT+stylet) `n=376`; total `757`. | Adult emergency-department orotracheal intubations; initial-attempt assigned device. [p1](../../../jama_driver_2018_oi_180054.pdf#page=1), [p4](../../../jama_driver_2018_oi_180054.pdf#page=4), [p5](../../../jama_driver_2018_oi_180054.pdf#page=5) | Allocation groups should sum to randomized total: 381+376=757. |
| MAIN-N002 | Difficult-airway subset: `198/381` bougie and `182/376` ETT+stylet; total `380`. | At least one stated difficult-airway characteristic; primary population. [p1](../../../jama_driver_2018_oi_180054.pdf#page=1), [p4](../../../jama_driver_2018_oi_180054.pdf#page=4), [p5](../../../jama_driver_2018_oi_180054.pdf#page=5) | 198+182=380; complement is 377. |
| MAIN-N003 | Mean age `46 y`; women `230 (30%)`; `757 (100%)` completed. | Randomized population. [p1](../../../jama_driver_2018_oi_180054.pdf#page=1) | Abstract-only aggregate demographics/completion. |
| MAIN-N004 | Eligibility: age `>=18 y`; study Sept 2016–Aug 2017; `109,000` annual ED visits. | Setting/eligible source population. [p1](../../../jama_driver_2018_oi_180054.pdf#page=1), [p2](../../../jama_driver_2018_oi_180054.pdf#page=2) | Context, not an outcome. |
| MAIN-N005 | Randomization 1:1; permuted block sizes `2, 4, 6, 8, 10`; two strata (obesity/cervical immobilization versus neither). | Allocation rule. [p3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Defines comparison population. |
| MAIN-N006 | Bougie device: `70 cm`, `15 French`, `5-mm` diameter; tube resistance remedy `2 cm` withdrawal and `90°` counterclockwise rotation; ETT bend `25°–35°`. | Device/procedure units. [p3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Context for device contrast. |
| MAIN-N007 | Primary outcome: successful tube placement with first device passed during first laryngoscope insertion. Hypoxemia: saturation `<90%`, or if baseline `<90%`, absolute decrease `>10%`; duration is insertion-to-removal time. | Outcome definitions. [p3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Defines denominators and units for Tables 3 and 5. |
| MAIN-S001 | Planning: `374` difficult-airway patients, `80%` power, detect absolute `9%` difference (`95%` vs `86%`), two-sided alpha `.05`; trial stopped after `>374` difficult-airway patients; no all-patient a priori calculation. | Power/stop rule. [p3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Planned versus observed difficult-airway total 380. |
| MAIN-S002 | Binary outcomes: difference in proportions/`95% CI`, chi-square; continuous: Hodges-Lehmann median difference/`95% CI`, Wilcoxon rank-sum; two-sided threshold `.05`. Duration additionally Kaplan-Meier/log-rank/unadjusted Cox HR; no multiplicity correction for exploratory subgroups. | Analysis rule. [p4](../../../jama_driver_2018_oi_180054.pdf#page=4) | Governs compatible comparisons only. |

## Flow, allocation, and baseline data

| ID | Printed values / relationship | Population, contrast, unit, and exact location | Rule / matched evidence / signal |
|---|---|---|---|
| MAIN-N008 | Figure 1: `3768` assessed; `3011` excluded; `2938` did not meet inclusion, including `2785` not intubated, `61` <18 y, `28` prisoners, `27` upper-airway distortion, `22` non-Macintosh, `15` known/expected pregnancy; `73` eligible not randomized (`30` too quick, `20` no staff, `16` physician refusal, `6` decline, `1` unknown). | Participant flow. [p4](../../../jama_driver_2018_oi_180054.pdf#page=4) | 3768−3011=757; Figure categories describe exclusion structure. |
| MAIN-N009 | Bougie arm: `381` randomized; `372` randomized device first, `4` ETT+stylet first, `5` no device first; difficult-airway subgroup `198`: `191`, `2`, `5`; included primary `198`, subgroup `381`. | Figure 1 allocation/adherence. [p4](../../../jama_driver_2018_oi_180054.pdf#page=4) | Each arm and subgroup components sum to its stated total. |
| MAIN-N010 | ETT+stylet arm: `376` randomized; `345` randomized device first, `25` bougie first, `6` no device first; difficult-airway subgroup `182`: `161`, `18`, `3`; included primary `182`, subgroup `376`. Physician-refusal data: `15`, bougie used in all; `14/15 (93%)` first-attempt success; ETT-deviation `23/25 (92%)` success. | Figure 1 allocation/adherence. [p4](../../../jama_driver_2018_oi_180054.pdf#page=4) | 345+25+6=376; 161+18+3=182. |
| MAIN-N011 | `51` unique physicians; bougie arm `44`, ETT+stylet `40`; median intubations/physician `8` (IQR `1–26`, range `1–61`); adherence `98%` and `92%`. | Results narrative. [p4](../../../jama_driver_2018_oi_180054.pdf#page=4) | Adherence matched to Figure 1 counts (372/381 and 345/376, rounded). |
| MAIN-N012 | Table 1 demographics: age mean (SD) `46 (18)` vs `46 (18)` y; men `272 (71%)` vs `255 (68%)`; BMI mean (SD) `28 (7)` vs `28 (7)`; heart rate `108 (25)` vs `107 (25)` beats/min; systolic BP `135 (30)` vs `134 (32)` mm Hg. | Bougie `n=381` vs ETT+stylet `n=376`. [p5](../../../jama_driver_2018_oi_180054.pdf#page=5), Table 1 | Baseline descriptive values. |
| MAIN-N013 | Table 1 oxygenation: median (IQR) `99 (95–100)%` vs `99 (96–100)%`; `<90%` `44/352 (13%)` vs `40/344 (12%)`; `<80%` `21/352 (6%)` vs `11/344 (3%)`. | Baseline, available-data denominators. [p5](../../../jama_driver_2018_oi_180054.pdf#page=5), Table 1 | Saturation missing: `19` vs `24`; denominators equal group minus missing. |
| MAIN-N014 | Medical indication `318 (83%)` vs `315 (84%)`: altered mental status `185 (49%)`/`173 (46%)`, cardiac arrest `32 (8%)`/`23 (6%)`, septic shock `21 (6%)`/`27 (7%)`, seizure `20 (5%)`/`28 (7%)`, asthma/COPD/heart failure/pneumonia `16 (5%)`/`23 (7%)`, other `44 (14%)`/`41 (13%)`. | Table 1, mutually described indication subcategories. [p5](../../../jama_driver_2018_oi_180054.pdf#page=5) | Medical components sum to 318/315. |
| MAIN-N015 | Trauma `63 (17%)` vs `61 (16%)`: traumatic brain injury `29 (8%)`/`23 (6%)`; other `34 (9%)`/`38 (10%)`. | Table 1. [p5](../../../jama_driver_2018_oi_180054.pdf#page=5) | Trauma components sum to 63/61; medical+trauma equals arm total. |
| MAIN-N016 | Difficult airway present `198 (52%)` vs `182 (48%)`: blood/vomit `83 (22%)`/`67 (18%)`; obesity `57 (15%)`/`68 (18%)`; cervical immobilization `49 (13%)`/`36 (10%)`; large tongue `31 (8%)`/`34 (9%)`; short neck `28 (7%)`/`28 (7%)`; facial trauma `20 (5%)`/`12 (3%)`; small mandible `14 (4%)`/`18 (5%)`; obstruction/edema `8 (2%)`/`4 (1%)`. | Table 1; categories may overlap. [p5](../../../jama_driver_2018_oi_180054.pdf#page=5) | Matches primary-subgroup counts; do not sum overlapping characteristics. |
| MAIN-N017 | Table 1 footnotes: no baseline heart-rate data `61` (`29`, `32`); no systolic-BP data `185` (`94`, `91`); no saturation `43` (`19`, `24`). BMI >=30 but clinician-not-obese: `64` vs `68`, total `132`, mean BMI `34`; clinician-obese mean BMI `37`. | Missingness/definition data. [p5](../../../jama_driver_2018_oi_180054.pdf#page=5) | Exact denominators and obesity definition context. |

## Table 2 process measures

All Table 2 entries compare bougie `n=381` with ETT+stylet `n=376`; differences are bougie minus ETT+stylet percentage points unless specified. Location: [p6](../../../jama_driver_2018_oi_180054.pdf#page=6), Table 2.

| ID | Printed values / relationship | Unit/definition and inferential display | Signal |
|---|---|---|---|
| MAIN-N018 | Non-rebreather `267 (70%)` vs `276 (73%)`, difference `−3 (−10 to 3)`, P `.31`; flush-rate: `204/267 (76%)` vs `210/276 (76%)`, `0 (−7 to 7)`, P `.93`; bag-mask `47 (12%)` vs `37 (10%)`, `2 (−2 to 7)`, P `.27`; noninvasive positive pressure `18 (5%)` vs `24 (6%)`, `−2 (−5 to 2)`, P `.32`; extraglottic `27 (7%)` vs `17 (5%)`, `3 (−1 to 6)`, P `.13`. | Preoxygenation. | Statistical values retained in S003. |
| MAIN-N019 | Any preintubation sedative `338 (89%)` vs `341 (91%)`, `−2 (−6 to 2)`, P `.37`; etomidate `332 (87%)` vs `333 (89%)`, `−1 (−6 to 3)`, P `.54`; ketamine `4 (1%)` vs `4 (1%)`, `0 (−1 to 1)`, P `.99`. | `78` without sedative; `53 (68%; 31/22)` prehospital sedation or cardiac arrest; other sedatives omitted. | Statistical values retained in S004. |
| MAIN-N020 | Any neuromuscular blockade `366 (96%)` vs `367 (98%)`, `−2 (−4 to 1)`, P `.23`; succinylcholine `214 (56%)` vs `229 (61%)`, `−5 (−12 to 2)`, P `.19`; rocuronium `147 (39%)` vs `137 (36%)`, `2 (−5 to 9)`, P `.54`. | Other drugs omitted. | Statistical values retained in S005. |
| MAIN-N021 | Sniffing `222 (58%)` vs `244 (65%)`, `−7 (−14 to 0)`, P `.06`; neutral spine `117 (31%)` vs `96 (26%)`, `5 (−1 to 12)`, P `.11`; extension without sniffing `39 (10%)` vs `32 (9%)`, `2 (−2 to 6)`, P `.42`. | Position; sniffing definition in footnote. | Statistical values retained in S006. |
| MAIN-N022 | Start saturation median (IQR) `100 (98–100)%` vs `100 (98–100)%`, median difference `0 (0 to 0)`, P `.60`; `<90%` `22/360 (6%)` vs `27/343 (8%)`, `−2 (−6 to 2)`, P `.36`; `<80%` `13/360 (4%)` vs `8/343 (2%)`, `1 (−1 to 4)`, P `.32`. | Start-attempt saturation; missing `21` vs `33`. | Statistical values retained in S007. |
| MAIN-N023 | Apneic nasal cannula `221 (58%)` vs `227 (60%)`, `−2 (−9 to 5)`, P `.51`. | Nasal cannula left in place. | S008. |
| MAIN-N024 | Senior resident/fellow `318 (83%)` vs `334 (89%)`, `−5 (−10 to 0)`, P `.03`; junior `57 (15%)` vs `37 (10%)`, `5 (0 to 10)`, P `.03`; faculty `8 (2%)` vs `5 (1%)`, `1 (−1 to 3)`, P `.42`. | Final intubator; operator changed `8` times, `4`/group. | S009. |
| MAIN-N025 | C-MAC `362 (95%)` vs `366 (97%)`, `−2 (−5 to 0)`, P `.10`; GlideScope Titanium MAC `12 (3%)` vs `8 (2%)`, `1 (−1 to 3)`, P `.38`; direct Macintosh `7 (2%)` vs `2 (1%)`, `1 (0 to 3)`, P `.10`. | Laryngoscope used. | S010. |
| MAIN-N026 | Screen never `218/377 (58%)` vs `182/372 (49%)`, `9 (2 to 16)`, P `.02`; entire attempt `78/377 (21%)` vs `90/372 (24%)`, `−4 (−9 to 2)`, P `.25`; during passage `75/377 (20%)` vs `98/372 (26%)`, `−6 (−12 to 0)`, P `.04`. | Video-screen use; four missing per arm. | S011. |
| MAIN-N027 | Cormack-Lehane grade 1 `269/373 (72%)` vs `269/359 (75%)`, `−3 (−9 to 4)`, P `.39`; grade 2 `74/373 (20%)` vs `62/359 (17%)`, `3 (−3 to 8)`, P `.39`; grade 3 `27/373 (7%)` vs `23/359 (6%)`, `1 (−3 to 4)`, P `.66`; grade 4 `3/373 (1%)` vs `5/359 (1%)`, `−1 (−2 to 1)`, P `.44`. | View definitions and missing `8` vs `17` in footnote. | S012. |
| MAIN-N028 | First device after laryngoscope: bougie `372 (98%)` vs `25 (7%)`, `91 (88 to 94)`, P `<.001`; ETT+stylet `4 (1%)` vs `345 (92%)`, `−91 (−94 to −88)`, P `<.001`; withdrawal before passage `5 (1%)` vs `6 (2%)`, `0 (−2 to 1)`, P `.75`. | Process/allocation; matches Figure 1. | S013. |

## Table 3 outcome relationships

Location for all rows: [p7](../../../jama_driver_2018_oi_180054.pdf#page=7), Table 3. Table values are event/total, percent (95% CI), bougie-minus-ETT+stylet difference (95% CI), P value, and interaction P where printed.

| ID | Printed values / relationship | Population, time, contrast, and definition | Candidate signal |
|---|---|---|---|
| MAIN-S014 | Primary success: `191/198`, `96% (93–99)` vs `150/182`, `82% (76–88)`; difference `14% (8–20)`, P `<.001`, interaction P `.36`. | Any difficult-airway characteristic, `n=380`; first attempt. Matched abstract p1, Key Points p2, narrative p5. | None at mapping. |
| MAIN-S015 | Success without hypoxemia: `156/191`, `82% (76–87)` vs `123/177`, `69% (63–76)`; difference `12% (3–21)`, P `.006`, interaction `.61`. | Difficult-airway population; valid waveform unavailable for some. | None at mapping. |
| MAIN-S016 | First-attempt duration median (IQR) `39 (29–52)` vs `40 (27–63) s`; difference `−1 (−6 to 3) s`, P `.50`, interaction `.17`. | Difficult-airway population; elapsed insertion-to-removal. | None at mapping. |
| MAIN-S017 | Overall success: `373/381`, `98% (96–99)` vs `328/376`, `87% (83–90)`; difference `11% (7–14)`, P `<.001`. | All randomized, `N=757`; matched abstract p1 and narrative p5. | None at mapping. |
| MAIN-S018 | Overall success without hypoxemia: `317/371`, `85% (81–89)` vs `282/366`, `77% (72–81)`; difference `8% (3–14)`, P `.003`. | All patients; waveform-available subset. | None at mapping. |
| MAIN-S019 | Overall first-attempt duration median (IQR) `38 (29–51)` vs `36 (25–54) s`; printed difference `1 (4 to −1) s`, P `.24`. | All randomized; matched abstract p1 reports 38 vs 36 seconds. | **Mechanical candidate signal for later checking:** displayed interval endpoints are ordered `4` then `−1`, and the printed point/interval sign relationship requires exact-rule review. No C ID or judgment assigned. |
| MAIN-S020 | Blood/vomit success `79/83`, `95% (88–99)` vs `55/67`, `82% (71–90)`; `13% (3–23)`, P `.01`, interaction `.31`; cervical immobilization `49/49`, `100% (93–100)` vs `28/36`, `78% (61–90)`; `22% (9–36)`, P `.001`, interaction `.25`; obesity `55/57`, `96% (88–100)` vs `51/68`, `75% (63–85)`; `21% (10–33)`, P `.001`, interaction `.63`. | Unplanned difficult-characteristic subgroups; footnote excludes other small subgroups. | None at mapping. |
| MAIN-S021 | No difficult characteristic: `182/183`, `99% (97–100)` vs `178/194`, `92% (87–95)`; `8% (4–12)`, P `<.001`, interaction `.36`. | `n=377`; matches complement of N002. | None at mapping. |
| MAIN-S022 | C-MAC all-patient success: `356/362`, `98% (96–99)` vs `321/366`, `88% (84–91)`; `11% (7–14)`, P `<.001`, interaction `.46`. | C-MAC use. | None at mapping. |
| MAIN-S023 | Cormack-Lehane: grade 1 `265/269`, `99% (96–100)` vs `258/269`, `96% (93–98)`, `3% (0–5)`, P `.07`, interaction `.04`; grade 2 `72/74`, `97% (91–100)` vs `41/62`, `66% (53–78)`, `31% (19–44)`, P `<.001`, interaction `.13`; grade 3 `26/27`, `96% (81–100)` vs `11/23`, `48% (27–69)`, `48% (27–71)`, P `<.001`, interaction `.17`; grade 4 `3/3`, `100% (29–100)` vs `2/5`, `40% (5–85)`, `60% (17–100)`, P `.09`, interaction `.78`. | All-patient laryngeal-view subgroups. | None at mapping. |
| MAIN-S024 | Actual first device success: `392/402`, `98% (95–99)` vs `309/355`, `87% (83–90)`; `10% (7–14)`, P `<.001`. | All patients classified by actual first device; randomized-device classification for withdrawal-before-passage. | Denominators 402+355=757; cross-over classification is intentional. |
| MAIN-S025 | Successful-first-attempt duration: `38 (29–51)` vs `34 (23–47) s`; `4 (2–7) s`, P `<.001`, interaction `.03`. | Unplanned post hoc successful-attempt subgroup. | None at mapping. |
| MAIN-N029 | `56 (7%)` total first-attempt failures; rescue included bougie in `49`, intubating laryngeal mask in `1`, cricothyrotomy in `1`. | Results narrative. [p7](../../../jama_driver_2018_oi_180054.pdf#page=7) | Matches 8+48 failures in Table 4. |

## Figure 2, Table 4, Table 5, and later narrative

| ID | Printed values / relationship | Population, contrast, unit, and exact location | Rule / signal |
|---|---|---|---|
| MAIN-S026 | Figure 2 difficult-airway time-to-success: log-rank P `.02`; unadjusted Cox HR `1.29 (95% CI 1.04–1.60)` for bougie with ETT+stylet reference. Number at risk at `0/30/60/90/120/150/180 s`: bougie `198/146/37/13/3/3/0`; ETT+stylet `182/127/56/9/3/3/1`. | Difficult-airway cohort; vertical ticks mark failures; proportional-hazards assumption not upheld. [p8](../../../jama_driver_2018_oi_180054.pdf#page=8), Figure 2; matched p5 narrative. | HR/P values match p5; later limitation repeats nonproportionality. |
| MAIN-N030 | Table 4 failures: initial bougie group `n=8`; initial ETT+stylet group `n=48`. Same insertion: bougie `0`/`34 (71%)`; ETT+stylet `0`/`1 (2%)`. Second insertion: bougie `6 (75%)`/`6 (13%)`; ETT+stylet `0`/`3 (6%)`. Different device `0`/`2 (4%)`; >2 attempts `2 (25%)`/`2 (4%)`. | Successful technique after failed first attempt. [p8](../../../jama_driver_2018_oi_180054.pdf#page=8), Table 4 | Categories are displayed as rescue-process detail, not additive independent outcomes; footnotes specify one same-attempt switch, two nonstandard rescues, and four >2 attempts. |
| MAIN-N031 | Bougie used in `444` patients; clicks `404 (91%)`; hold-up sign `283 (64%)`; tube resistance `31 (7%)`; all but `1` resolved with `90°` rotation, with the remaining patient successful on later bougie attempt. | Other outcomes. [p5](../../../jama_driver_2018_oi_180054.pdf#page=5) | 444 reflects actual bougie use, not randomized bougie allocation. |
| MAIN-N032 | Table 5 any complication `66 (17%)` vs `63 (17%)`, difference `1% (−5 to 6)`, P `.83`; hypoxemia `47/371 (13%)` vs `50/364 (14%)`, `−1% (−6 to 4)`, P `.67`; pneumothorax after intubation `9 (2%)` vs `9 (2%)`, `0% (−2 to 2)`, P `.99`; postintubation no-clear-cause pneumothorax `1 (<1%)` vs `3 (1%)`, `−1% (−2 to 1)`, P `.31`. | Complications, bougie `n=381`, ETT+stylet `n=376`. [p9](../../../jama_driver_2018_oi_180054.pdf#page=9), Table 5 | Some patients had >1 complication; composite counts once. S027. |
| MAIN-N033 | Table 5 lip laceration `7 (2%)` vs `3 (1%)`, `1% (−1 to 3)`, P `.21`; aspiration `3 (1%)` vs `1 (<1%)`, `1% (−1 to 2)`, P `.32`; iatrogenic bleeding `2 (1%)` vs `2 (1%)`, `0% (−1 to 1)`, P `.99`; dental trauma `1 (<1%)` vs `1 (<1%)`, `0% (−1 to 1)`, P `.99`; esophageal intubation `0` vs `3 (1%)`, `−1% (−2 to 0)`, P `.08`; direct airway injury `0` vs `0`. | Table 5. [p9](../../../jama_driver_2018_oi_180054.pdf#page=9) | Narrative p8 repeats 13% vs 14% hypoxemia and 0 vs 3 esophageal intubations. S028. |
| MAIN-S027 | Inferential displays for MAIN-N032: P `.83`, `.67`, `.99`, `.31` and stated differences/CIs. | Table 5. [p9](../../../jama_driver_2018_oi_180054.pdf#page=9) | No display-zero P value. |
| MAIN-S028 | Inferential displays for MAIN-N033: P `.21`, `.32`, `.99`, `.99`, `.08` and stated differences/CIs. | Table 5. [p9](../../../jama_driver_2018_oi_180054.pdf#page=9) | No display-zero P value. |
| MAIN-N034 | Discussion comparisons: external reported 78% versus study 82% (difficult ETT+stylet), 91% versus study 92% (no-difficult ETT+stylet), >`13,000` external resident intubations and 86.9% versus study 87%, >`42,000` external intubations and 84.1%, external C-MAC 91%; >`96%` initial C-MAC; study bougie C-MAC success 98%. | Contextual comparisons, not internally matched outcomes. [p8](../../../jama_driver_2018_oi_180054.pdf#page=8), [p9](../../../jama_driver_2018_oi_180054.pdf#page=9) | The study-side values match Table 3/2 rounded figures. |
| MAIN-N035 | Later narrative/limitations: postintubation resistance `7%`; ETT+stylet allocation protocol violation `7%`; proportional-hazards assumption not upheld; `>96%` C-MAC use. | Discussion/limitations. [p9](../../../jama_driver_2018_oi_180054.pdf#page=9), [p10](../../../jama_driver_2018_oi_180054.pdf#page=10) | Matched to N031/N026/figure; no new distinct result. |

## Statistical-index crosswalk

`MAIN-S003` through `MAIN-S013` are the Table 2 inferential displays embedded in `MAIN-N018` through `MAIN-N028`, respectively. `MAIN-S014` through `MAIN-S025` are the Table 3/primary statistical relationships. `MAIN-S026` is Figure 2/Cox-log-rank. `MAIN-S027` and `MAIN-S028` are Table 5. All have explicit printed P values, differences/intervals where supplied, population, contrast, and location above.

## Mapping limitations

OCR was adequate for narrative and most table text. Rendered page 7 was used to confirm the exact Table 3 all-patient duration display `1 (4 to −1)`, and rendered page 8 to confirm Table 4’s `1 (2%)` same-insertion ETT+stylet cell. Page 11 contains references only and therefore has an explicit no-new-result disposition. No candidate IDs, adjudications, or external sources were used.
