# Cross-Source Consistency Check

**Scope:** Fresh direct-source comparison of DOC-001 (`jama_barkin_2018_oi_180075.pdf`, pp. 1-11), DOC-002 (`joi180075supp1_prod.pdf`, pp. 1-113), and DOC-003 (`joi180075supp2_prod.pdf`, pp. 1-8), using the canonical fresh relationship inventories and the two fresh mapping artifacts. This is a discovery artifact, not a candidate ledger and not an adjudication. All provisional items below require human verification; no stable `C` ID is assigned here.

**Comparison rule:** A difference was called only when population, arm/contrast, time point, quantity/scale, and representation were aligned. Planned-versus-observed differences were not called solely for being different. A protocol/SAP statement was called only when its own declared count/list or measure label conflicts with a same-study schedule or analysis description. Display-zero P-value formatting was not used as a candidate basis.

## Complete relationship coverage

### Numeric/reporting relationships checked

`N001`, `N002`, `N003`, `N004`, `N005`, `N006`, `N007`, `N008`, `N009`, `N010`, `N011`, `N012`, `N013`, `N014`, `N015`, `N016`, `N017`, `N018`, `N019`, `N020`, `N021`, `N022`, `N023`, `N024`, `N025`, `N026`, `N027`, `N028`, `N029`, `N030`, `N031`, `N032`, `N033`, `N034`, `N035`, `N036`, `N037`, `N038`, `N039`, `N040`, `N041`, `N042`, `N043`, `N044`, `N045`, `N046`, `N047`, `N048`, `N049`, `N050`, `N051`, `N052`, `N053`, `N054`, `N055`, `N056`, `N057`, `N058`, `N059`, `N060`, `N061`, `N062`, `N063`, `N064`.

### Inferential/statistical relationships checked

`S001`, `S002`, `S003`, `S004`, `S005`, `S006`, `S007`, `S008`, `S009`, `S010`, `S011`, `S012`, `S013`, `S014`, `S015`, `S016`, `S017`, `S018`, `S019`, `S020`, `S021`, `S022`, `S023`, `S024`, `S025`, `S026`, `S027`, `S028`, `S029`, `S030`, `S031`, `S032`, `S033`, `S034`, `S035`, `S036`, `S037`, `S038`, `S039`, `S040`, `S041`, `S042`, `S043`, `S044`, `S045`, `S046`, `S047`, `S048`, `S049`, `S050`, `S051`, `S052`, `S053`, `S054`, `S055`, `S056`, `S057`, `S058`, `S059`, `S060`, `S061`, `S062`, `S063`, `S064`, `S065`, `S066`, `S067`, `S068`, `S069`, `S070`, `S071`.

## Matched representations with no provisional candidate

| Checked cross-source representation | Relationships | Direct observation and matching logic | Result |
|---|---|---|---|
| Trial frame, allocation, eligibility, intervention phases, and ITT population | N001-N004, N009, N045-N047, N051 | DOC-001 reports 610 randomized (304/306), ages 3-5 years and BMI eligibility 50th to <95th percentile; the support documents contain the same eligibility, 36-month phase structure, and an ITT mixed-model plan. The protocol's planned 600 is explicitly prospective and is not equated to the observed 610. | Matched or planned-versus-observed; no candidate. |
| Enrollment and 36-month retention | N005-N008, N012, N034-N035, N056-N060 | The abstract's overall 90.2% retention equals 550/610 after rounding, where the CONSORT diagram gives 278+272 retained (550) and the arm percentages are 91.4% and 88.9%. Figure 2 and eTable 1 agree with each other at every printed follow-up BMI mean and displayed total. The separate Figure 1 count discrepancies are enumerated below. | No other candidate. |
| Primary outcome measure and reported result | N003, N034, N037, N044, N060; S001-S005, S023-S032 | DOC-001 abstract, Results, Figure 3, and DOC-003 eTable 1 agree on 36-month BMI means 17.8 (2.2) and 17.8 (2.1), adjusted I-C difference 0.05 (95% CI -0.29 to 0.38), and P=.79; DOC-001's joint LRT P=.39 agrees with the final SAP's 2-df joint test definition. The original-protocol BMI-percentile wording is separately enumerated below. | Matched; no candidate for the reported result. |
| Secondary and post-hoc results | N038-N043; S006-S021 | Abstract, narrative, Tables 2-3, and the supplied eTable/eFigure references agree after direction is aligned: `-99.4 kcal` I-C is the same as narrative `99.4 kcal fewer`; center-use 56.8%/44.4%, RR 1.29 (1.08-1.53), corrected P=.006 agrees; 3-month obesity RR 0.51 (0.29-0.92) agrees with the narrative. Percentages, RRs, and counts were not interchanged. | Matched; no candidate. |
| Baseline table labels and support moderation populations | N013-N033, N049, N063; S033-S070 | Table 1 scale and denominator footnotes supply the relevant units/definitions. DOC-003 eTable 2 identifies moderator-specific analytic denominators and BMI/year or BMI/year² units; the eFigures supply no printed coordinates that could be reconciled numerically. No aligned repeated numerical comparator contradicts these records. | No candidate. |
| Sample-size and final-analysis plan | N011, N052-N054; S022-S025 | The main article's 90%-power, standardized-effect-size .4, required final n=480 statement agrees with the final SAP power table (effect .4, 90% power, n=480). The original and final SAP intentionally differ in primary-test specification, and DOC-002 p. 113 documents that change; no candidate is based on that documented amendment. | Matched/documented plan change; no candidate. |
| Qualitative supplementary figures | N061-N063; S071 | DOC-003 eFigures 1-3 show model-estimated trajectories/risk difference but do not print coordinates, effect values, denominators, or endpoints sufficient for a numerical equality rule. Their labels are not equated to a different printed estimand. | No candidate; limited by graphical precision. |
| Appended revised-protocol schedule and control exposure | N064 | DOC-002 p. 64 repeats the revised-protocol six-versus-seven time-point/list conflict and the 7×45-minute control-program description. Its implications are already registered in stable `C010` (schedule) and `C012` (control exposure); it supplies no new distinct comparator or candidate. | Checked; no new candidate. |

## Provisional cross-source consistency items

### XSR-001 — Intervention 3-month BMI-observation count differs between the CONSORT diagram and Figure 2/eTable 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [Figure 1 — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>); DOC-001 [Figure 2 — PDF p. 7](<../../jama_barkin_2018_oi_180075.pdf#page=7>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Figure 1 states `288 BMI measured at 3 mo` for intervention. Figure 2 gives intervention `Total No.` `279` at 3 months, and eTable 1 gives intervention `No.` `279` at 3 months.
- **Comparison logic:** Each location describes observed/collected child BMI for the intervention arm at the 3-month time point. Figure 1's caption says the retained number represents children for whom BMI was collected; Figure 2's caption calls its values observed child BMI; eTable 1 gives means (SD) for its reported No. A single same-time, same-arm observation count should agree unless an explicit differing analysis/cleaning definition is supplied.
- **Supported alternatives and human verification:** The eTable/Figure 2 count may represent a post-cleaning analytic subset while the CONSORT number represents collection, but no supplied caption defines that distinction. Verify the analysis dataset and whether three-month BMI records were excluded after collection.

### XSR-002 — Control 3-month BMI-observation count differs between the CONSORT diagram and Figure 2/eTable 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [Figure 1 — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>); DOC-001 [Figure 2 — PDF p. 7](<../../jama_barkin_2018_oi_180075.pdf#page=7>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Figure 1 states `277 BMI measured at 3 mo` for control. Figure 2 and eTable 1 each print control `271` at 3 months.
- **Comparison logic:** Same child-BMI quantity, control arm, and 3-month visit; apply the same count-identity rule as XSR-001.
- **Supported alternatives and human verification:** A post-collection analytic exclusion could explain the six-record difference, but it is not supplied. Verify the control 3-month measurement and analysis denominators.

### XSR-003 — Intervention 9-month BMI-observation count differs between the CONSORT diagram and Figure 2/eTable 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [Figure 1 — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>); DOC-001 [Figure 2 — PDF p. 7](<../../jama_barkin_2018_oi_180075.pdf#page=7>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Figure 1 prints intervention `282 BMI measured at 9 mo`; Figure 2 and eTable 1 print intervention `280` at 9 months.
- **Comparison logic:** Same observed child-BMI arm/time representation; expected identical count absent an expressly different denominator.
- **Supported alternatives and human verification:** Verify whether two collected intervention records were not included in the Figure 2/eTable display and document any pre-specified exclusion.

### XSR-004 — Intervention 12-month BMI-observation count differs between the CONSORT diagram and Figure 2/eTable 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [Figure 1 — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>); DOC-001 [Figure 2 — PDF p. 7](<../../jama_barkin_2018_oi_180075.pdf#page=7>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Figure 1 prints intervention `275 BMI measured at 12 mo`; Figure 2 and eTable 1 print intervention `274` at 12 months.
- **Comparison logic:** Same observed child-BMI arm/time representation; expected identical count absent an expressly different denominator.
- **Supported alternatives and human verification:** Verify whether one collected intervention record was not included in the Figure 2/eTable display and document any exclusion.

### XSR-005 — Control 12-month BMI-observation count differs between the CONSORT diagram and Figure 2/eTable 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [Figure 1 — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>); DOC-001 [Figure 2 — PDF p. 7](<../../jama_barkin_2018_oi_180075.pdf#page=7>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Figure 1 prints control `276 BMI measured at 12 mo`; Figure 2 and eTable 1 print control `275` at 12 months.
- **Comparison logic:** Same observed child-BMI arm/time representation; expected identical count absent an expressly different denominator.
- **Supported alternatives and human verification:** Verify whether one collected control record was not included in the Figure 2/eTable display and document any exclusion.

### XSR-006 — Intervention 24-month BMI-observation count differs between the CONSORT diagram and Figure 2/eTable 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [Figure 1 — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>); DOC-001 [Figure 2 — PDF p. 7](<../../jama_barkin_2018_oi_180075.pdf#page=7>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Figure 1 prints intervention `280 BMI measured at 24 mo`; Figure 2 and eTable 1 print intervention `278` at 24 months.
- **Comparison logic:** Same observed child-BMI arm/time representation; expected identical count absent an expressly different denominator.
- **Supported alternatives and human verification:** Verify whether two collected intervention records were not included in the Figure 2/eTable display and document any exclusion.

### XSR-007 — Control 24-month BMI-observation count differs between the CONSORT diagram and Figure 2/eTable 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [Figure 1 — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>); DOC-001 [Figure 2 — PDF p. 7](<../../jama_barkin_2018_oi_180075.pdf#page=7>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Figure 1 prints control `267 BMI measured at 24 mo`; Figure 2 and eTable 1 print control `266` at 24 months.
- **Comparison logic:** Same observed child-BMI arm/time representation; expected identical count absent an expressly different denominator.
- **Supported alternatives and human verification:** Verify whether one collected control record was not included in the Figure 2/eTable display and document any exclusion.

### XSR-008 — Intervention 36-month BMI-observation count differs between the CONSORT diagram and Figure 2/eTable 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [Figure 1 — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>); DOC-001 [Figure 2 — PDF p. 7](<../../jama_barkin_2018_oi_180075.pdf#page=7>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Figure 1 prints intervention `278 Retained at 36 mo` and its caption defines retained as children for whom BMI was collected. Figure 2 and eTable 1 print intervention `276` at 36 months.
- **Comparison logic:** The caption supplies the same BMI-collected meaning for the Figure 1 count; Figure 2/eTable 1 describe the observed child-BMI display at 36 months. The two-count difference requires a stated definition to be reconciled.
- **Supported alternatives and human verification:** `Retained` may have been used as a broader administrative count despite the caption, or two measured records may have been excluded from the displayed analysis. Verify the 36-month intervention BMI measurement and display denominator.

### XSR-009 — Final SAP says six assessment points but enumerates five, omitting 24 months

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-002 [final SAP — PDF p. 110](<../../joi180075supp1_prod.pdf#page=110>); DOC-002 [original protocol schedule — PDF p. 15](<../../joi180075supp1_prod.pdf#page=15>); DOC-001 [Methods schedule — PDF p. 4](<../../jama_barkin_2018_oi_180075.pdf#page=4>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Final SAP p. 110 says assessments occur over `6 time points` and lists baseline, 12 weeks/3 months, 9, 12, and 36 months: five occasions. DOC-002 p. 15 explicitly lists baseline, 3, 9, 12, 24, and 36 months; DOC-001 and DOC-003 both report/use 24-month data.
- **Comparison logic:** A stated count of six time points must enumerate six distinct occasions. The aligned direct-source schedule identifies 24 months as the absent sixth occasion.
- **Supported alternatives and human verification:** This may be an editorial omission in the final-SAP prose rather than an analytical omission; the model permits individual measurement dates. Verify the final archived SAP and whether 24-month data were intentionally part of the primary model.

### XSR-010 — Revised protocol gives a self-conflicting assessment count/list and adds a 48-month occasion not present in the reported trial schedule

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-002 [revised protocol — PDF p. 64](<../../joi180075supp1_prod.pdf#page=64>); DOC-001 [Methods schedule — PDF p. 4](<../../jama_barkin_2018_oi_180075.pdf#page=4>); DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** DOC-002 p. 64 calls the collection schedule `6-points in time (T1-T6)` and then lists baseline, 3, 9, 12, 24, 36, `and one at 48-months` (seven occasions), followed by `Each of the six data collection points`. DOC-001 and DOC-003 report the six-occasion baseline-to-36-month schedule and no 48-month outcome.
- **Comparison logic:** The revised-protocol sentence is internally inconsistent (six claimed versus seven listed). Its seventh, 48-month occasion does not align with the published 36-month primary-outcome schedule.
- **Supported alternatives and human verification:** The 48-month visit may have been an approved later follow-up outside the article's 36-month trial analysis. Verify amendment/version dates and whether the p. 64 wording was intended to distinguish a separate follow-up rather than a core T1-T6 assessment.

### XSR-011 — Original protocol calls the primary outcome BMI percentile/BMI%, whereas the final analysis and reported primary results use BMI in kg/m²

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-002 [original protocol primary outcome/Table 2 — PDF p. 16](<../../joi180075supp1_prod.pdf#page=16>); DOC-002 [final SAP primary outcome/model — PDF pp. 110-111](<../../joi180075supp1_prod.pdf#page=110>) and [PDF p. 111](<../../joi180075supp1_prod.pdf#page=111>); DOC-001 [Outcomes — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>), [abstract — PDF p. 1](<../../jama_barkin_2018_oi_180075.pdf#page=1>), and DOC-003 [eTable 1 — PDF p. 2](<../../joi180075supp2_prod.pdf#page=2>).
- **Printed comparator:** Original protocol p. 16 says the primary outcome is `child's BMI Percentile` and `change of BMI%`, while its table labels the trajectory `BMI%` but gives the calculation weight (kg)/height (m²). The final SAP calls the outcome time-varying BMI, and the article/eTable report raw BMI values (e.g., 17.8) in kg/m² and a BMI trajectory.
- **Comparison logic:** BMI percentile/BMI% and raw BMI kg/m² are distinct scales. The original-protocol label/table conflicts with the scale actually reported and modeled unless `BMI%` was an erroneous shorthand or an unrecorded amendment changed the primary estimand.
- **Supported alternatives and human verification:** The formula may show that `BMI%` was a mislabeled raw-BMI measure, or a protocol amendment may have changed the primary outcome before analysis. Verify the approved protocol version/amendment trail and the analysis variable supplied to the primary model.

### XSR-012 — Control-condition session count and duration differ across supplied protocol versions and the article

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-002 [original protocol — PDF p. 14](<../../joi180075supp1_prod.pdf#page=14>); DOC-002 [revised protocol — PDF p. 64](<../../joi180075supp1_prod.pdf#page=64>); DOC-001 [abstract — PDF p. 1](<../../jama_barkin_2018_oi_180075.pdf#page=1>) and [Methods — PDF p. 3](<../../jama_barkin_2018_oi_180075.pdf#page=3>).
- **Printed comparator:** Original protocol: control `60-minute` sessions quarterly for 36 months, `12 sessions`. Revised protocol: intervention and control receive a `45-minutes school readiness/school success program` at each of `7 data collection points`. Article abstract: control `6 school-readiness sessions` over 36 months; Methods: `six 30-minute group-based activities` delivered concurrently with data-collection sessions.
- **Comparison logic:** These are each descriptions of the study's control school-readiness exposure over the trial period, but the stated total count/duration is respectively 12×60, 7×45, and 6×30 minutes. They cannot all describe one identical session schedule without a supplied distinction among planned, ancillary, and delivered components.
- **Supported alternatives and human verification:** The protocol versions may represent revised plans and the article may report the actual delivered activities; newsletters, field trips, or baseline sessions may be counted differently. Verify dated protocol versions, amendment records, intervention logs, and whether the article's six activities exclude components counted by either protocol.

## Display-zero and graphical exclusions

No compared relationship was registered because of a `P = 0`, `p = 0.000`, or equivalent display-zero form. Where a source printed `<.001`, it was treated as ordinary finite-precision reporting and did not create a cross-source candidate. DOC-003 eFigures lack numerical coordinates/denominators where noted above, so no visual interpolation was converted into a numeric discrepancy.

## Counts and limitations

- **Relationships completed:** 64 numeric/reporting (`N001`-`N064`, individually listed above) and 71 inferential/statistical (`S001`-`S071`, individually listed above).
- **Provisional cross-source items:** 12 (`XSR-001` through `XSR-012`); eight are distinct arm-by-time BMI count discrepancies, and four concern schedule, scale, or control-exposure descriptions.
- **No-candidate matched groupings:** 7 documented above; all remaining mapped records were either matched, explicitly planned-versus-observed, documented plan changes, or lacked a printed numeric comparator.
- **Limitations:** The package contains multiple protocol versions and does not always state whether a reported count is collection-level or analysis-cleaned. Supplementary eFigures do not print enough numerical coordinates for exact reconciliation. These limitations are recorded as human questions and do not resolve or suppress the provisional items.
