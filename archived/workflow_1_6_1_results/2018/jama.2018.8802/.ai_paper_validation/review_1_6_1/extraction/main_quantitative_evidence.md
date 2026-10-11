# Main-paper quantitative evidence map — Workflow 1.6.1

## Scope, provenance and boundaries

DOC-001, `jama_wang_2018_oi_180070.pdf`, REPORT, all PDF pages 1–10 (journal pages 245–254). Scientific mapping is freshly reconstructed. The assigned source has 10 reusable-backed units, zero fresh-required units, and 10 mapped units. This artifact contains 80 local relationship groups M001–M080; these are mapper keys, not candidate IDs or the final N/S inventory. Every table row, figure panel, caption and matching narrative occurrence is included. No candidate diagnosis, inclusion decision or adjudication is made here.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md; current tooling_record.md, source_inventory.md, source_coverage.md and evidence_asset_inventory.md. Eligible locators: review_1_5_2/preprocessing/native_text/DOC-001.txt, layout_text/DOC-001.txt and coordinate layout_text/DOC-001.tsv. Native/layout assets are source-matched per curator; native abstract and TSV header/positions were consulted. Direct PDF layout text was additionally inspected for all 10 pages using installed Poppler `pdftotext -layout -f FIRST -l LAST jama_wang_2018_oi_180070.pdf -`, in bounded page blocks. Source-matched rendered PNGs DOC-001-p07.png and DOC-001-p08.png were visually inspected to clarify Table 2/3 column alignment, signs, Figure 2 labels, risk counts and caption. Historical text extraction is attributed to Acrobat COM and the historical PNG engine is unspecified. Current direct checks use Poppler pdftotext 25.03.0. No derivative file, OCR, conversion or fallback environment was produced by this mapper. The missing legacy p10 image does not create a coverage gap: direct native/layout text is readable and that page contains article metadata and references without trial-result tables or figures.

Links below are relative to this artifact in extraction/ and terminate in truthful PDF page anchors. All CIs in result tables are printed 95% CIs. I = multifaceted quality improvement intervention; C = routine care plus stroke registry participation. Printed percentages are preserved. Adjusted absolute differences are separate reported quantities from the descriptive percentages; the source explicitly identifies adjustment. No crude difference is substituted for an adjusted result. A dash in the mapping denotes no printed value, not zero.

## Page coverage

| PDF page | Journal page | Complete mapped content | Status |
|---|---:|---|---|
| 1 | 245 | Abstract population, dates, intervention arms, endpoint definitions, primary and vascular results, conclusion; bibliographic numbers are non-result metadata | COMPLETE |
| 2 | 246 | Key Points, background numerical context, trial design, hospital frame, patient eligibility, follow-up and baseline-survey purpose | COMPLETE |
| 3 | 247 | Randomization/stratification, intervention timing/intensity, collection, all nine measure definitions, composite/all-or-none definitions and decision rule, secondary endpoints | COMPLETE |
| 4 | 248 | Sample-size inputs, all statistical/model/adjustment and missing-data statements, enrollment and follow-up narrative | COMPLETE |
| 5 | 249 | Figure 1 complete hospital/patient flow and footnote; primary-result, vascular, disability, mortality and safety narrative; sensitivity results; discussion | COMPLETE |
| 6 | 250 | All 25 baseline Table 1 data rows and notes, discussion matches and historical numerical context | COMPLETE |
| 7 | 251 | All 11 Table 2 rows, both inferential columns, ICCs and every footnote; discussion including 30-day curve interpretation | COMPLETE |
| 8 | 252 | All 10 Table 3 rows and notes; both Figure 2 panels, all risk counts/axes/effects and caption; sensitivity interpretation | COMPLETE |
| 9 | 253 | Limitations and conclusions with trial-result quantitative references; article information/affiliations/contributions/disclosures have no additional trial-result relationships | COMPLETE |
| 10 | 254 | Remaining investigator/funding metadata and 31 bibliographic references: no additional trial-result numeric/statistical relationships; numbers in cited titles, grants and references are explicitly nonapplicable | COMPLETE |

## Population, enrollment and endpoint relationships

| Key | Exact source location | Source-grounded numeric/statistical relationship and matching occurrence |
|---|---|---|
| M001 | [Abstract](../../../jama_wang_2018_oi_180070.pdf#page=1); [Key Points/Methods](../../../jama_wang_2018_oi_180070.pdf#page=2); [Results](../../../jama_wang_2018_oi_180070.pdf#page=4); [Figure 1](../../../jama_wang_2018_oi_180070.pdf#page=5) | Cluster-randomized trial: 40 public hospitals, 4800 AIS patients; 20 I hospitals/2400 I patients and 20 C hospitals/2400 C patients. Open-label trial. Hospitals are randomization units; patients and eligible care opportunities are outcome-analysis units as separately described under M063–M066. All 4800 prospectively enrolled and included in primary analysis in Results. |
| M002 | [Abstract](../../../jama_wang_2018_oi_180070.pdf#page=1); [Methods](../../../jama_wang_2018_oi_180070.pdf#page=2); [Limitations](../../../jama_wang_2018_oi_180070.pdf#page=9) | Enrollment August 10, 2014–June 20, 2015; 12-month follow-up through July 30, 2016. Methods: telephone outcomes 3, 6 and 12 months after stroke onset/initial stroke. Limitations: intervention studied over an 11-month period; follow-up beyond 1 year discussed as future work. |
| M003 | [Abstract](../../../jama_wang_2018_oi_180070.pdf#page=1); [Results](../../../jama_wang_2018_oi_180070.pdf#page=4); [Table 1](../../../jama_wang_2018_oi_180070.pdf#page=6) | Overall mean age 65 years; women 1757 (36.6%) of 4800. Table 1 presents separate group age medians and men counts (M022–M023), not a pooled mean. |
| M004 | [Abstract](../../../jama_wang_2018_oi_180070.pdf#page=1); [Results](../../../jama_wang_2018_oi_180070.pdf#page=4); [Figure 1](../../../jama_wang_2018_oi_180070.pdf#page=5) | 3980 (82.9%) completed 12-month follow-up; I 2003 (83.5%)/2400, C 1977 (82.4%)/2400. Figure 1: no hospital lost to follow-up, I 397 patients lost, C 423 patients lost; terminal boxes label I 20 hospitals and 2003 patients, C 20 hospitals and 1977 patients as included in primary analysis. Complete text of each population label is preserved rather than harmonized. |
| M005 | [Results](../../../jama_wang_2018_oi_180070.pdf#page=4); [Figure 1/footnote](../../../jama_wang_2018_oi_180070.pdf#page=5) | Results: 40 hospitals from 18 provinces initially recruited; 3 hospitals with unexpected inability to conduct trial replaced according to characteristics; final 40; none subsequently excluded. Figure 1: 40 invited, 3 excluded (declined), 37 agreed, 3 replacements added, 40 randomized; each arm 20 allocated, 20 implemented allocation, 2400 enrolled and 2400 received allocation. Footnote: 40 eligible hospitals randomly selected/invited from 563 by hospital grade (tertiary/secondary) and region (eastern/central/western). |
| M006 | [Results](../../../jama_wang_2018_oi_180070.pdf#page=4) | Cluster enrollment duration median I 207 days (IQR 182–225), C 204 (159–262). Mean patients/cluster 120, range 102–145. Hospital narrative: 72.5% tertiary, 62.5% stroke unit, 62.5% teaching; median annual number of neurological ward beds 77 (IQR 61–178). Table 1 bed row labels simply number of neurological ward beds (M019). |
| M007 | [Hospitals/Patients](../../../jama_wang_2018_oi_180070.pdf#page=2) | Sampling frame 563 hospitals, 27 provinces plus 4 municipalities = 31 locations. Three hospital grades; only secondary/tertiary public hospitals with ED, neurology ward and rtPA capacity eligible; primary, private and rural excluded. Patients age ≥18, CT/MRI-confirmed AIS within 7 days after onset, admitted directly or via ED; other listed cerebrovascular/noncerebrovascular disease excluded. |
| M008 | [Randomization](../../../jama_wang_2018_oi_180070.pdf#page=3) | Forty eligible hospitals randomly selected and stratified by province, capacity (secondary/tertiary) and baseline stroke-care quality; randomization 1:1 using SAS 9.3 generated numbers by independent statistician. Outcome evaluators/statisticians blinded; intervention nature permits no personnel blinding. |
| M009 | [Intervention and collection](../../../jama_wang_2018_oi_180070.pdf#page=3); [Results](../../../jama_wang_2018_oi_180070.pdf#page=5) | Four intervention components: clinical pathway, care protocols, full-time quality coordinator, monitoring/feedback. Two professionals/hospital attend a 2-day workshop. Daily pathway for first 7 admission days plus discharge. Monitoring checked at least weekly; median monitoring-to-feedback interval 7 days. Data-quality meeting monthly. These timings establish intervention exposure and measurement context, not standalone clinical outcomes. |
| M010 | [Abstract](../../../jama_wang_2018_oi_180070.pdf#page=1); [Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3); [Clinical Events](../../../jama_wang_2018_oi_180070.pdf#page=5); [Table 3 note](../../../jama_wang_2018_oi_180070.pdf#page=8) | Nine performance measures, six designed as GWTG measures; four beginning-hospitalization, five discharge (all definitions below). Clinical secondary outcomes: in-hospital death; new vascular event = ischemic stroke, hemorrhagic stroke, MI or vascular death; disability mRS 3–5; all-cause death at 3/6/12 months. Outcomes section and Table 3 note say after initial symptom/stroke onset; Clinical Events introductory paragraph says after discharge. Figure 2 axis says days after stroke symptom onset. Retain all time labels for matching. |

## Table 1 complete baseline numeric inventory

Exact source for every row: [PDF p6, Table 1](../../../jama_wang_2018_oi_180070.pdf#page=6). Columns are baseline survey (B), I and C; hospital counts use hospital denominators 40/20/20; patient counts use 801/2400/2400. Counts and printed percentages are retained as displayed; medians are followed by IQRs. There are no Table 1 P values, effect estimates or CIs. Results p4 summarizes balance except length of stay and supplies pooled demographics (M003, M006).

| Key | Row/quantity | B | I | C |
|---|---|---|---|---|
| M011 | Hospitals, No. | 40 | 20 | 20 |
| M012 | Grade: tertiary, No. (%) | 29 (72.5) | 15 (75.0) | 14 (70.0) |
| M013 | Grade: secondary, No. (%) | 11 (27.5) | 5 (25.0) | 6 (30.0) |
| M014 | Region: eastern, No. (%) | 20 (50) | 10 (50.0) | 10 (50.0) |
| M015 | Region: central, No. (%) | 9 (22.5) | 4 (20.0) | 5 (25.0) |
| M016 | Region: western, No. (%) | 11 (27.5) | 6 (30.0) | 5 (25.0) |
| M017 | Stroke unit, No. (%) | 25 (62.5) | 14 (70.0) | 11 (55.0) |
| M018 | Teaching hospital, No. (%) | 25 (62.5) | 13 (65.0) | 12 (60.0) |
| M019 | Neurological ward beds, median (IQR), count | 77 (61–178) | 70 (60–138) | 80 (61–152) |
| M020 | Annual stroke discharges, median (IQR), count/year | 401 (321–761) | 365 (317–710) | 417 (321–785) |
| M021 | Patients, No. | 801 | 2400 | 2400 |
| M022 | Age, median (IQR), years | 65 (57–75) | 65 (57–73) | 64 (56–74) |
| M023 | Men, No. (%) | 486 (60.7) | 1553 (64.7) | 1490 (62.1) |
| M024 | Prior ischemic stroke, No. (%) | 271 (33.8) | 666 (27.8) | 722 (30.1) |
| M025 | Diabetes, No. (%) | 193 (24.1) | 577 (24.0) | 509 (21.2) |
| M026 | Hypertension, No. (%) | 542 (67.7) | 1550 (64.6) | 1540 (64.2) |
| M027 | Dyslipidemia, No. (%) | 65 (8.1) | 305 (12.7) | 291 (12.1) |
| M028 | CAD/previous MI, No. (%) | 126 (15.7) | 311 (13.05) | 298 (12.4) |
| M029 | Atrial fibrillation, No. (%) | 67 (8.4) | 118 (4.9) | 127 (5.3) |
| M030 | Ever smoking, No. (%) | 339 (42.3) | 1057 (44.0) | 1059 (44.1) |
| M031 | Admission NIHSS, median (IQR), score | 4 (2–8) | 4 (2–6) | 4 (2–6) |
| M032 | Transported to ED by EMS, No. (%) | 112 (14.0) | 265 (11.0) | 236 (9.9) |
| M033 | Symptom onset–ED arrival within 2 h; row says proportion, %, cells show No. (%) | 96 (12.0) | 254 (10.6) | 238 (9.9) |
| M034 | LDL, median (IQR), mg/dL | 111.97 (88.80–135.14) | 103.08 (81.85–126.25) | 103.86 (80.69–128.57) |
| M035 | Length of stay, median (IQR), days | 13 (10–15) | 13 (10–15) | 12 (9.5–15) |

Notes: NIHSS range 0–42, with 42 most severe; LDL mg/dL ×0.0259 = mmol/L. CAD, ED, EMS, IQR, LDL and NIHSS expansions are supplied in source. “Baseline Survey” is a separate prerandomization sample, not a third randomized arm.

## Table 2 complete primary/performance inventory

Exact source for every row: [PDF p7, Table 2](../../../jama_wang_2018_oi_180070.pdf#page=7). I and C are “No. of Events/Total Patients (%)” except the explicitly labeled composite mean (SD). Difference is adjusted absolute difference in percentage points, printed column label `%`; ORPA is adjusted population average odds ratio, I relative to C. Each row below separately preserves P for absolute difference and P for ORPA. Positive absolute values favor I according to footnote a. Printed ICC is last column. There are 11 rows: 2 co-primary and all 9 individual measures.

| Key | Measure | I | C | Adjusted difference (95% CI), % | P difference | Adjusted ORPA (95% CI) | P ORPA | ICC |
|---|---|---|---|---|---|---|---|---|
| M036 | Composite, mean (SD) | 88.2 (15.1) | 84.8 (18.2) | 3.5 (0.7–6.4) | .02 | 1.39 (1.12–1.72) | .003 | 0.02 |
| M037 | All-or-none | 1290/2400 (53.8) | 1147/2400 (47.8) | 6.7 (−0.4 to 13.8) | .06 | 1.19 (0.85–1.67) | .31 | 0.07 |
| M038 | Intravenous rtPA within 3 h onset | 46/212 (21.7) | 23/204 (11.3) | 7.3 (−5.3 to 19.9) | .26 | 3.18 (0.94–10.78) | .06 | 0.28 |
| M039 | Early antithrombotics | 2307/2353 (98.0) | 2253/2330 (96.7) | 1.5 (−0.3 to 3.2) | .10 | 1.93 (0.94–3.95) | .07 | 0.03 |
| M040 | Dysphagia screening | 2255/2328 (96.9) | 2040/2139 (95.4) | 1.6 (−2.1 to 5.3) | .41 | 2.49 (0.84–7.40) | .10 | 0.24 |
| M041 | DVT prophylaxis | 178/645 (27.6) | 66/592 (11.1) | 15.6 (3.3–27.9) | .01 | 2.42 (1.02–5.72) | .04 | 0.36 |
| M042 | Discharge antithrombotics | 2272/2324 (97.8) | 2141/2305 (92.9) | 4.2 (−0.6 to 8.9) | .09 | 2.29 (0.86–6.11) | .10 | 0.23 |
| M043 | Discharge anticoagulation for AF | 63/155 (40.6) | 39/137 (28.5) | 12.9 (−5.8 to 31.6) | .18 | 1.80 (0.68–4.75) | .23 | 0.25 |
| M044 | Discharge lipid-lowering, LDL >100 mg/dL | 1415/1481 (95.5) | 1439/1547 (93.0) | 2.4 (−1.6 to 6.4) | .25 | 1.35 (0.67–2.73) | .40 | 0.16 |
| M045 | Discharge antihypertensive | 1510/1838 (82.2) | 1372/1771 (77.5) | 6.1 (−0.6 to 12.7) | .07 | 1.44 (0.94–2.20) | .10 | 0.08 |
| M046 | Discharge antidiabetic | 653/728 (89.7) | 557/663 (84.0) | 5.0 (0.8–9.3) | .02 | 1.57 (1.08–2.28) | .02 | 0.03 |

Matching exact narrative occurrences:

- M036: [abstract p1](../../../jama_wang_2018_oi_180070.pdf#page=1) 88.2% vs 84.8%; difference 3.54% (0.68% to 6.40%), P=.02; [Key Points p2](../../../jama_wang_2018_oi_180070.pdf#page=2) same percentages and significant difference; [primary Results p5](../../../jama_wang_2018_oi_180070.pdf#page=5) same exact difference/CI/P plus ORPA 1.39 (1.12–1.72), ICC .02, P=.003. [Limitations p9](../../../jama_wang_2018_oi_180070.pdf#page=9) labels between-group composite difference 3.4% versus detectable 5%. Conclusions p1/p9 call improvement significant but small when composite, without a new value.
- M037: abstract p1 and primary Results p5 53.8% vs 47.8%; difference 6.69% (−0.41% to 13.79%), P=.06. Results p5 also ORPA 1.19 (0.85–1.67), ICC .07, P=.31. Key Points p2 and discussion p6 say no significant all-or-none improvement. Key Points says adherence to all nine, while Outcomes specifies all for which patient eligible (M062).
- M038–M046: primary Results p5 says all nine adherence percentages higher in I and only DVT and antidiabetic medication individually significant. Discussion p5–6 repeats the two measures, says this does not imply only those two responded, and describes all-or-none as giving no credit for some but not all required measures.

Table 2 complete footnote/definition map:

- a: Both inferential columns adjusted for age, sex, ischemic stroke history, hypertension disease, diabetes, hyperlipidemia, AF, CAD/prior MI, ever smoking, admission NIHSS, hospital grade, region, stroke unit, teaching status and number neurological ward beds. Same covariate list recurs in Data Analysis p4 and Table 3 p8.
- b rtPA: arrival within 2 h after initial symptom onset, treatment within 3 h. Outcomes p3 states rtPA within 3 h; Table 2 title addresses eligible patients.
- c early antithrombotics: prescribed within 48 h hospitalization.
- d dysphagia: screening prior to any oral intake during hospitalization.
- e DVT: nonambulatory patients by end hospital day 2.
- f discharge antithrombotics: aspirin, clopidogrel, ozagrel, dipyridamole, ticlopidine, cilostazol, low-molecular-weight heparin, unfractionated heparin and warfarin.
- Outcomes p3 additionally gives anticoagulation for AF/flutter; lipid agent for LDL >100 mg/dL **or undocumented LDL**; antihypertensive and diabetes treatment. LDL conversion ×0.0259 mmol/L; eligibility/contraindications point to Supplement 2 eTable 1, whose mapping is owned by support mapper.

## Table 3 complete clinical-event inventory

Exact source for every row: [PDF p8, Table 3](../../../jama_wang_2018_oi_180070.pdf#page=8). Separate descriptive event fraction, adjusted absolute difference/P and adjusted HR or OR/P are preserved. Difference columns are printed `%`, CI95%. I vs C comparison. HR applies to vascular events/death; OR to disability. Table 3 title: new vascular events, disability and death. Disability header mRS 3–5.

| Key | Outcome/time | I events/total (%) | C events/total (%) | Adjusted difference (95% CI), % | P difference | Effect label and value (95% CI) | P effect |
|---|---|---|---|---|---|---|---|
| M047 | Vascular, 3 mo | 93/2400 (3.9) | 127/2400 (5.3) | −2.0 (−3.5 to −0.6) | .007 | HR 0.65 (0.49–0.86) | .002 |
| M048 | Vascular, 6 mo | 150/2400 (6.3) | 186/2400 (7.8) | −2.2 (−4.0 to −0.4) | .02 | HR 0.72 (0.57–0.90) | .004 |
| M049 | Vascular, 12 mo | 218/2400 (9.1) | 282/2400 (11.8) | −3.1 (−5.3 to −1.0) | .005 | HR 0.72 (0.60–0.87) | <.001 |
| M050 | Disability, 3 mo | 418/2180 (19.2) | 443/2105 (21.0) | −3.7 (−6.7 to −0.8) | .01 | OR 0.76 (0.63–0.91) | .002 |
| M051 | Disability, 6 mo | 326/2058 (15.8) | 360/2009 (17.9) | −3.9 (−6.6 to −1.1) | .006 | OR 0.74 (0.61–0.89) | .002 |
| M052 | Disability, 12 mo | 236/1852 (12.7) | 264/1798 (14.7) | −3.1 (−5.8 to −0.5) | .02 | OR 0.74 (0.59–0.93) | .01 |
| M053 | Death, in hospital | 11/2400 (0.5) | 23/2400 (1.0) | −0.7 (−1.1 to 0.2) | .009 | HR 0.96 (0.90–1.02) | .14 |
| M054 | Death, 3 mo | 66/2400 (2.8) | 76/2400 (3.2) | −1.0 (−2.1 to 0.1) | .08 | HR 0.81 (0.57–1.15) | .23 |
| M055 | Death, 6 mo | 103/2400 (4.3) | 101/2400 (4.2) | −0.5 (−1.7 to 0.6) | .38 | HR 0.97 (0.73–1.29) | .81 |
| M056 | Death, 12 mo | 139/2400 (5.8) | 160/2400 (6.7) | −1.5 (−3.0 to −0.0) | .05 | HR 0.86 (0.68–1.09) | .21 |

Table 3 footnote a repeats complete adjustment list in Table 2 a. Footnote b: disability mRS 3–5 function status at 3, 6, 12 months after stroke onset; mixed model with binary link; OR demonstrates intervention benefit on function status. Table 3 layout and literal positive upper endpoint `0.2` in in-hospital difference interval were visually read from p08 image; the native text was not altered.

Matching exact narrative occurrences [Clinical Events p5](../../../jama_wang_2018_oi_180070.pdf#page=5):

| Key | I vs C percentages | Narrative difference (95% CI), % | Narrative effect (95% CI) | Additional match |
|---|---|---|---|---|
| M047 | 3.9 vs 5.3 | −2.03 (−3.51 to −0.55) | HR .65 (.49–.86) | Abstract p1 also P=.007 and same exact difference/CI |
| M048 | 6.3 vs 7.8 | −2.18 (−4.0 to −0.35) | HR .72 (.57–.90) | Abstract p1 also P=.02 and same exact difference/CI |
| M049 | 9.1 vs 11.8 | −3.13 (−5.28 to −0.97) | HR .72 (.60–.87) | Abstract p1 also P=.005; Figure 2A p8 HR .72 (.60–.87), P<.001 |
| M050 | 19.2 vs 21.0 | −3.72 (−6.7 to −0.79) | OR .76 (.63–.91) | Narrative calls lower disability at each time |
| M051 | 15.8 vs 17.9 | −3.86 (−6.60 to −1.13) | OR .74 (.61–.89) | Same narrative direction |
| M052 | 12.7 vs 14.7 | −3.13 (−5.80 to −0.46) | OR .74 (.59–.93) | Same narrative direction |
| M053–M056 | No new mortality fractions in narrative | No new difference values | No new HR values | Clinical Events p5 says no significant total-mortality difference in hospital or 3/6/12 mo; Figure 2B supplies 12-mo HR and P; discussion p5 says improved vascular outcomes/disability, not mortality |

## Figures, safety and sensitivity

| Key | Exact source location | Complete relationship |
|---|---|---|
| M057 | [Figure 2A/caption](../../../jama_wang_2018_oi_180070.pdf#page=8); [discussion](../../../jama_wang_2018_oi_180070.pdf#page=7) | New vascular events; y-axis cumulative incidence 0, .05, .10, .15; x-axis Days After Stroke Symptom Onset 0, 90, 180, 270, 360. I curve below C. HR .72 (95% CI .60–.87), P<.001. No. at risk aligned at x ticks: C 2400/2275/2003/1891/1839; I 2400/2308/2098/1989/1952. Caption median follow-up I 364 d (IQR 364–365), C 365 d (364–365). Caption says log-rank test compares days after symptom onset to occurrence of new clinical vascular events or death. Discussion p7 calls these “HR curves” and says almost completely separated in first 30 days. Exact continuous curve coordinates not printed and not invented; plotted direction and labels mapped. |
| M058 | [Figure 2B/caption](../../../jama_wang_2018_oi_180070.pdf#page=8) | Deaths; same axes/ticks/scales as panel A. I curve slightly below C at end. HR .86 (95% CI .68–1.09), P=.21. At risk C 2400/2327/2080/1979/1951; I 2400/2334/2146/2041/2023. Same follow-up/caption/statistical-test statement as panel A; no separate figure event fractions. |
| M059 | [Clinical Events](../../../jama_wang_2018_oi_180070.pdf#page=5); [definition](../../../jama_wang_2018_oi_180070.pdf#page=4) | Symptomatic intracerebral hemorrhage after IV rtPA: I 1/46 (2.2%), C 2/23 (8.7%), P=.26; described not significantly different. Definition any type intracerebral hemorrhage on posttreatment imaging related to any neurological worsening. No CI, effect measure or specific test name printed for this safety comparison. Denominators match treated rtPA counts M038. |
| M060 | [Sensitivity Analysis](../../../jama_wang_2018_oi_180070.pdf#page=5); [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4); [discussion](../../../jama_wang_2018_oi_180070.pdf#page=8) | Include patients with contraindications in overall denominator. Composite I 85.3%, C 80.91%; adjusted absolute difference 4.20% (95% CI 1.77–6.63); adjusted ORPA 1.36 (1.11–1.67), P=.003. Reference Supplement 2 eTable 4. No P explicitly attached to the difference separately in this sentence. Discussion p8 says significant effect preserved when no documented-contraindication patients excluded, interpreting increased receipt rather than more documentation. |

## Statistical specification and rule relationships

These rows map literal statistical statements independently of their assessment. The two inferential columns in Tables 2–3 remain separate; no assumption that they use identical fitted links, standard errors or transformations is inserted. No numerical SE or test statistic is printed for this trial in the main article.

| Key | Exact source location | Full source-grounded relationship |
|---|---|---|
| M061 | [Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3) | Co-primary adherence summaries: all-or-none and composite. Trial interpreted as positive if either statistically significant. Nine predefined measures, including four admission and five discharge. |
| M062 | [Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3); [discussion](../../../jama_wang_2018_oi_180070.pdf#page=6) | All-or-none = proportion receiving every performance measure for which patient eligible. Composite = number of eligible measures performed divided by number for which given patient eligible; calculated for each patient then averaged. Discussion all-or-none gives no credit for some but not all required measures. Table 2 composite is mean (SD), all-or-none count/2400. |
| M063 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4) | Intention-to-treat used for all outcomes. Multivariable regression compares I vs C; GEE accounts for within-hospital correlation. Logistic regression for binary all-or-none and disability. Effects described as population-average OR. Randomization is cluster level (M008); Table 2 reports ICC each row. |
| M064 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4) | Inferential composite expressed as odds of fulfilling eligible care opportunities; each opportunity contributes binary 1 = met, 0 = not met. Literal example: eligible for 5 of 7 measures, receives 3; contributes 5 observations, 3 outcome 1 and 2 outcome 0. This example is recorded alongside the nine actual trial measures and patient-averaged descriptive definition, without making it a candidate. |
| M065 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4); [Table 3](../../../jama_wang_2018_oi_180070.pdf#page=8) | Clinical vascular events and mortality at discharge and 3/6/12 mo after initial symptom onset analyzed as time-to-event; outcomes demonstrated by Kaplan–Meier curves and assessed using multivariable Cox proportional hazards. Table 3 shows HR for vascular and death. Figure 2 caption separately states log-rank test (M057–M058). |
| M066 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4); [Table 3 note b](../../../jama_wang_2018_oi_180070.pdf#page=8) | Mixed model with binary link for disability at 3/6/12 mo; Table 3 note b explicitly assigns OR to disability mRS 3–5 function status. Earlier Data Analysis also lists logistic regression for disability (M063); both statements retained. |
| M067 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4); [Table 2 a](../../../jama_wang_2018_oi_180070.pdf#page=7); [Table 3 a](../../../jama_wang_2018_oi_180070.pdf#page=8) | All multivariable models adjust for age, sex, ischemic stroke history, hypertension disease, diabetes, hyperlipidemia, AF, CAD/prior MI, ever smoking, admission NIHSS; hospital capacity tertiary/secondary, region, stroke unit, teaching status, neurology beds. All comparative outcomes show cumulative incidences and absolute differences with 95% CIs adjusted for patient/hospital baseline characteristics. Tables attach covariate footnote to absolute differences and ratio columns. |
| M068 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4) | No adjustment for multiple comparisons for co-primary measures. Secondary analyses exploratory. P<.05 considered statistically significant; all tests 2-sided. All analyses SAS 9.3. These rules contextualize every P in Table 2/3, safety and sensitivity results without prescribing additional rules. |
| M069 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4); [Limitations](../../../jama_wang_2018_oi_180070.pdf#page=9) | Missing categorical values imputed by modes, continuous by medians. Smoking highest missing 1.42%, replaced by no smoking history; one missing NIHSS replaced by median 3. Limitations acknowledges imputing all missing smoking as nonsmoking. Table 1 NIHSS medians 4 refer to separate descriptive summaries; no missing-outcome imputation method is stated in this main-paper paragraph. |
| M070 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4) | Continuous baseline variables summarized median/IQR; categorical frequency/percentage. Wilcoxon rank-sum and χ² tests for continuous/categorical data respectively, comparing groups for cluster differences. Table 1 does not print the resulting test statistics or P values. |
| M071 | [Sample Size](../../../jama_wang_2018_oi_180070.pdf#page=4) | Prerandomization survey mean composite 80%. Required 4800 at 40 hospitals, median 120 AIS/hospital; detect 5% improvement, 80% power, 5% significance, ICC .02. Required 2400/group. No SD, variance formula or sample-size test formula printed here. Sample-size sentence cites GWTG evidence, historical context separately M072. |
| M072 | [Sample Size](../../../jama_wang_2018_oi_180070.pdf#page=4) | Historical GWTG first-year increase 4.33%, baseline 83.52% to 87.85%; invoked to motivate assumed 5% detectable change. This is supplied contextual evidence, not an effect estimate from the current trial. |
| M073 | [Sample Size](../../../jama_wang_2018_oi_180070.pdf#page=4) | Web management monitors accrual; each group stops enrollment when 2400 eligible patients recruited. No interim efficacy/stopping threshold or noninferiority/equivalence margin appears in the main source. This row records the actual accrual rule, not a criticism of absent rules. |
| M074 | [Baseline survey](../../../jama_wang_2018_oi_180070.pdf#page=2); [continuation](../../../jama_wang_2018_oi_180070.pdf#page=3); [Results](../../../jama_wang_2018_oi_180070.pdf#page=4); [Table 1](../../../jama_wang_2018_oi_180070.pdf#page=6) | Survey obtained baseline adherence, comparability and sample-size estimate; methods/results Supplement 2 eAppendix A. Table 1 survey n801/40 hospitals. Results says patient/hospital characteristics balanced except length of stay. Baseline descriptive tests are under M070, complete rows M011–M035. |
| M075 | [Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4); [Sensitivity Analysis](../../../jama_wang_2018_oi_180070.pdf#page=5) | Sensitivity denominator includes patients with contraindications to distinguish increased numerator from documentation-driven smaller denominator. Result values M060. Primary individual eligible denominators M038–M046; supplementary contraindication-inclusive results owned by support mapper. |

## Remaining matching claims and contextual numeric content

| Key | Exact source location | Complete relationship or explicit nonapplicable content |
|---|---|---|
| M076 | [Background](../../../jama_wang_2018_oi_180070.pdf#page=2) | Context: estimated 2.4 million new China stroke events in 2013; developing countries up to 78% global stroke burden. No current-trial denominator, estimate or statistical test attached. Recorded for page completeness; do not substitute as trial results. |
| M077 | [Discussion](../../../jama_wang_2018_oi_180070.pdf#page=5); [discussion](../../../jama_wang_2018_oi_180070.pdf#page=6) | Context: public hospitals account for 92% of China admissions. Historical GWTG 2003–2009 composite improvement 83.52% to 93.97%; Target: Stroke uses 10 strategies. These are contextual comparisons to externally cited work only as stated within supplied paper. Current trial conclusion improved care, lower vascular events/disability, individual significance only DVT and diabetes, and no all-or-none improvement matches M036–M056. |
| M078 | [Discussion](../../../jama_wang_2018_oi_180070.pdf#page=7); [discussion](../../../jama_wang_2018_oi_180070.pdf#page=8) | Historical PRISMM: 5 of 10 performance measures same as trial, other intervention/feedback differences. Current-trial vascular curves described separated within 30 days (M057). Discussion cautions clinical effect much greater than process effect, proposes overall-care contribution, and reiterates preserved sensitivity effect M060. No new numerical effect/interval is supplied. |
| M079 | [Limitations/Conclusions](../../../jama_wang_2018_oi_180070.pdf#page=9) | Composite 3.4% observed descriptive contrast versus 5% sample-size improvement; 11-month intervention, possible mortality differences beyond 1 year; hospital-based intervention, postdischarge adherence, unrecorded against-advice discharge and smoking imputation limitations. Concludes among 40 hospitals statistically significant but small composite improvement, no all-or-none improvement. No new inferential values or numerical SE introduced. |
| M080 | [Article information](../../../jama_wang_2018_oi_180070.pdf#page=9); [remaining metadata/references](../../../jama_wang_2018_oi_180070.pdf#page=10) | Nonapplicable units explicitly inspected: p9 publication dates, affiliations, contributions, disclosures, investigator/committee/hospital names; p10 remaining hospital names, grant identifiers, sponsor role, disclaimer and 31 references. Bibliographic years, volumes, pages, DOIs, cited-title participant count (e.g. 480687) and grant numbers are not current-trial quantitative relationships. No additional trial counts/estimates/tests found on p10. |

## Handoff summary and limitations

All 10 assigned direct-source pages are mapped, including nonapplicable page content. Eighty grouped mapper relationships include 25 complete baseline data rows, 11 complete adherence rows with 22 inferential estimate/CI/P sets and ICCs, 10 complete clinical outcome rows with 20 inferential estimate/CI/P sets, all narrative/abstract matching values, full hospital/participant flow, two figure panels with 20 risk counts, all endpoint/eligibility/model/adjustment/decision and sample-size inputs, safety and sensitivity results. Grouping retains every displayed value and is not a finding limit.

Scientific coverage gaps: none. Derivative limitations: legacy p10 image absent; historical extractor/rendering version unavailable. These do not prevent scientific mapping; direct native/layout text covers every assigned page, and reusable visual evidence clarifies dense tables/figure symbols. Continuous Figure 2 coordinates are not printed; only visible direction, axes, annotation and risk table are mapped. Missing numerical SEs/test statistics/sample-size variance formula and unspecified safety test are facts about supplied reporting, not mapper diagnoses. Final N/S inventory construction, checks, inclusion screening and any candidate registration belong to subsequent fresh agents.
