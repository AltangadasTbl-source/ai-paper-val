# DOC-003 quantitative plan mapping: physical pages 33–64

Scope: joi190092supp2_prod.pdf, every physical PDF page 33–64 inclusive, 32 units. Document role: PLAN throughout. Physical pp.33–63 have printed folios 32–62 and the September 4, 2012 Manual of Operation and Procedures header; p.64 is the January 06, 2017 Version 4.5 MOP title page. The page-number offset is physical page = printed folio + 1 in this shard. No report results, participant counts, event estimates, confidence intervals, P values, power inputs, allocation ratios, analysis-population definitions, multiplicity thresholds, subgroup specifications, imputation procedures, or workbook formulas/caches occur in this scope. Operational definitions and prospective measurement/analysis statements are recorded below without assessing candidate status.

Runtime ID: 01a12954-c5d7-7741-96c0-704c55754ff2.

Evidence: reusable .ai_paper_validation/review_1_5_1/preprocessing/protocol_pp033_064_layout.txt read for all pages. Fresh direct-source confirmation: `pdftotext -layout -f 33 -l 64 joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/protocol_002/direct_pp033_064_layout.txt`, Poppler 26.01.0 on CPU. `cmp` confirmed identical direct and reusable layout output. The existing p.47 image .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/page-047.png was visually read for the Davis scale figure: labels 0–8 in a 3×3 grid, in row order, increasingly obscured fundus images. No OCR required; no fresh-required units at assignment. Source PDF remains authority. Every physical page has been opened in text; image-only quantitative content on p.47 was additionally inspected visually.

## Per-page coverage

| Physical page | Printed folio | Content opened and mapped | Coverage |
|---:|---:|---|---|
| 33 | 32 | Refraction definition; 4 m and 1 m transition; acuity-dependent trial-lens table heading | COMPLETE |
| 34 | 33 | Trial-lens table all rows; 20/10–20/80 refraction sphere/cylinder sequence | COMPLETE |
| 35 | 34 | Cylinder-axis step-size table; power/spherical-equivalent rules; sphere refinement | COMPLETE |
| 36 | 35 | Sphere refinement continuation; 20/100–20/200 refraction protocol | COMPLETE |
| 37 | 36 | Cylinder-axis step-size table repeated; cylinder power and spherical equivalent | COMPLETE |
| 38 | 37 | 0.50 D refinement; <20/200 transition to 1 m; accommodation +0.75 D | COMPLETE |
| 39 | 38 | Low-acuity cylinder-axis table and power refinement | COMPLETE |
| 40 | 39 | Low-acuity sphere refinement; visual acuity is secondary outcome; 14-line charts | COMPLETE |
| 41 | 40 | Chart use, logMAR/letters/Snellen example, illumination and lane specifications | COMPLETE |
| 42 | 41 | Each-eye each-visit acuity, masked examiner, row stop and <10-letter distance transition | COMPLETE |
| 43 | 42 | 1 m first six rows; low-vision thresholds; count-fingers/hand-motion/light-perception tests; scoring opening | COMPLETE |
| 44 | 43 | Acuity-score rules, max100, Snellen ≥4/5 criterion; certification | COMPLETE |
| 45 | 44 | Anterior chamber cells/flare and vitreous cells grade tables and endpoint inclusion/exclusion | COMPLETE |
| 46 | 45 | NEI vitreous haze grade table and Figure1; planned Davis/NEI/photo comparison | COMPLETE |
| 47 | 46 | Davis Figure2 labels0–8 visually read; inter-observer assessment; primary measurement selection; OCT setup | COMPLETE |
| 48 | 47 | Heidelberg volume-scan 20°×20°,49 sections,16 frames; follow-up reference scan | COMPLETE |
| 49 | 48 | Heidelberg seven-line scan 30°×5°,7 sections,25 frames; quality≥20; central subfield thickness | COMPLETE |
| 50 | 49 | Zeiss macular cube and five-line raster; printed cube designation512×218 | COMPLETE |
| 51 | 50 | Zeiss signal strength≥5; central subfield thickness; fundus-photo times/masked grading | COMPLETE |
| 52 | 51 | Laboratory timing/measures; temporary drug cessation/resumption and failure; AE definitions start | COMPLETE |
| 53 | 52 | Non-serious/serious AE thresholds, reporting and death notifications | COMPLETE |
| 54 | 53 | Data forms, double entry and data completion procedures; no inferential specification or reported result | COMPLETE |
| 55 | 54 | Missing data coded NA; observation-row variable-column datasets; units/codebooks; quality checks | COMPLETE |
| 56 | 55 | Unmasked dataset/randomization merge; R report generation; monthly monitoring; no specified inferential model | COMPLETE |
| 57 | 56 | Compliance missed-dose logs/pill counts each visit; otherwise operations; no result estimate | COMPLETE |
| 58 | 57 | Personnel duties, database cleaning/lock and final analysis; no additional result-relevant quantitative relation | COMPLETE |
| 59 | 58 | Both-eye acuity/OCT and fundus photo schedule; otherwise organization; no new numerical result | COMPLETE |
| 60 | 59 | Prespecified interim when one-third complete study; DSMC stopping authority | COMPLETE |
| 61 | 60 | Conservative early stopping authority continuation; otherwise committees/pharmacy/communications; no threshold | COMPLETE |
| 62 | 61 | Bibliography refs1–23, all opened; no applicable prospective analysis or trial result relation | COMPLETE |
| 63 | 62 | Bibliography refs24–33, all opened; no applicable prospective analysis or trial result relation | COMPLETE |
| 64 | — | January06,2017 Version4.5 MOP title; plan-version boundary; no statistical relation on title page | COMPLETE |

## Relationships and main-paper matching keys

Identifiers below are shard-local, so the coordinator can assign canonical N/S identifiers without collisions. These are extraction records, not findings. Main-paper matching keys are concepts for matching; this mapper did not open main-paper units.

### S-P002-01 — Secondary visual-acuity measurement and scale

[Source pp.40–44](../../../../joi190092supp2_prod.pdf#page=40), sections5.2.2–5.2.3, PLAN. Visual acuity explicitly necessary for the secondary outcome. Measured at each study visit, separately for each eye, after refraction; examiner has no prior clinical examination/treatment results. Chart1 for right eye, Chart2 for left, ChartR for refraction;14 high-contrast tumbling-E lines; geometric letter-size progression corresponds to arithmetic log minimum-angle-of-resolution progression. Test starts at4 m. If3 or fewer letters identified on any row from row3 down, stop on that row; if fewer than10 letters read at4 m, retest at1 m, first6 rows only; fewer than10 at1 m triggers low-vision testing. One response per letter; previous responses cannot be revised after advancing.

Main matching key: change in best-corrected visual acuity, logMAR, eye-level outcome, masking, visits.

### S-P002-02 — Acuity scoring as printed

[Source pp.43–44](../../../../joi190092supp2_prod.pdf#page=43), Scoring Best Corrected Visual Acuity, PLAN. Biostatistician calculates visit score from recorded letters. Opening condition on p.43 states “10 or more letters of the first line” at4 m; score on p.44 is number read at4 m plus30. Other printed conditions:3 or fewer letters of largest line at4 m → score equals letters read at1 m;3 or fewer letters at1 m → low-vision classification converted to logMAR using Visual Acuity Calculation Table. Highest4 m score100. Snellen equivalent is hardest line on which at least4 of5 letters are read. p.41 gives example third row:0.8 logMAR,45 letters,20/125 Snellen. No low-vision-to-logMAR numeric table appears in this shard. Preserve the distinct printed testing and scoring conditions rather than silently harmonizing them.

Main matching key: logMAR conversion and best-corrected acuity scoring; secondary analysis measurement.

### N-P002-01 — Low-vision response thresholds

[Source p.43](../../../../joi190092supp2_prod.pdf#page=43), PLAN. Count fingers at1 m:1,2,or5 fingers presented in random order,5 presentations;3/5 identifies count-fingers vision. Hand motion at0.5 m:vertical/horizontal motion about1 back-and-forth/second,5 presentations;4/5 identifies hand motion. Light perception at0.5 m:light directed four times; recorded when examiner convinced subject sees light, otherwise no-light-perception. These define categorical observations subsequently converted to logMAR.

### N-P002-02 — Refraction numeric rules supporting secondary acuity

[Source pp.33–40](../../../../joi190092supp2_prod.pdf#page=33), PLAN. Contact-lens removal precedes refraction by30 min. Refraction usually4 m; worse than20/200 (missing≥2 largest-line letters) →1 m, with+0.75 D accommodation adjustment. Trial-lens guide, columns sphere power/increment; JCC axis,power/increment; sphere refinement power/increment:

| Vision tier | Sphere testing and change | Cylinder axis JCC / power JCC | Cylinder change | Sphere refinement testing / change |
|---|---|---|---|---|
| 6/3–6/24 or20/10–20/80 at4 m | +0.50/+0.50;−0.37/−0.25; repeated+0.50/+0.50 | 0.50 D /0.25 D | +0.25;−0.25 | +0.37/+0.25;−0.37/−0.25; repeated+0.37/+0.25 |
| 6/30–6/60 or20/100–20/200 at4 m | +1.00/+1.00;−1.00/−1.00; repeated+1.00/+1.00 | 1.00 D /1.00 D | +1.00;−1.00 | +0.50/+0.50;−0.50/−0.50; repeated+0.50/+0.50 |
| <6/60 or<20/200 at1 m | +2.00/+2.00;−2.00/−2.00; repeated+2.00/+2.00 | 1.00 D /1.00 D | +1.00;−1.00 | +1.00/+1.00;−1.00/−1.00; repeated+1.00/+1.00 |

Axis steps, repeated pp.35,37,39: cylinder<1 D→10°;1–<2 D→5°;2–<3 D→3°;3–<5 D→2°;5–<8 D→1°. Initial tested axes90°,180°,45°,135°; subsequent comparisons±45° around axis; equal initial positions prompt15° axis rotation; change to negative cylinder prompts testing90° from prior axis. For cylinder≥1 D, each0.5 D cylinder change is accompanied by0.25 D sphere change of opposite sign to preserve spherical equivalent. End with plus-lens refinement. These are measurement procedures, not randomized intervention doses or statistical estimates.

### S-P002-03 — Ocular-inflammation components and grading

[Source p.45](../../../../joi190092supp2_prod.pdf#page=45), PLAN. Ophthalmologist exam each visit. Anterior chamber cells SUN grades,1×1 mm slit-lamp field in dark room:0:<1;0.5+:1–5;1+:6–15;2+:16–25;3+:26–50;4+:>50. Flare measured but explicitly not a criterion for controlled inflammation:0 none;1+ faint;2+ moderate with clear iris/lens;3+ marked with hazy details;4+ intense fibrin/plastic aqueous. Vitreous cells collected but explicitly not a controlled-inflammation criterion:0 no cells;0.5+:0–5;1+:6–10;2+:11–20;3+:21–50;4+:>50, field1×0.5 mm after dilation. Main matching key: primary treatment-success inflammation components and thresholds.

### S-P002-04 — Vitreous-haze endpoint scales and exploratory comparisons

[Source pp.46–47](../../../../joi190092supp2_prod.pdf#page=46), PLAN. NEI haze grading used for all primary and secondary outcome measures. Indirect ophthalmoscope mid-power with20 D lens, disc region last view; dark room. NEI grades:0 clear;0.5+ slight disc-margin blurring/nerve-fiber striations and reflex not seen;1+ opacities without obscuring retinal detail;2+ mild optic-nerve/vessel-detail blurring;3+ significant blurring but still visible;4+ dense opacity obscuring nerve head. Figure1 illustrative photographs p.46 accompany table. Additional Davis nine-point scale Figure2 p.47 shows grades0,1,2/3,4,5/6,7,8 in3×3 grid. Prespecified exploratory analysis correlates NEI/Davis measurements; clinical haze compared with objective photograph grades. Main matching key: primary success haze threshold and exploratory scale comparison.

### S-P002-05 — Inter-observer assessment and primary measurement selection

[Source p.47](../../../../joi190092supp2_prod.pdf#page=47), section5.3.2, PLAN. Inter-observer agreement assessed at6th-month,12th-month visit or treatment failure, “whichever is earlier”; following sentence arranges two certified physicians at Month6 and12 or declaration of failure. Measures:anterior chamber cells,flare,vitreous cells,haze. Inter-observer variation will be reported. Primary ophthalmologist measurements used for primary analysis. No agreement statistic specified here. Main matching key: prespecified secondary/ancillary agreement assessment and primary-analysis assessor.

### S-P002-06 — OCT outcome measurement and stable instrument

[Source pp.47–51](../../../../joi190092supp2_prod.pdf#page=47), PLAN. SD-OCT measures macular thickness and change; each site chooses Heidelberg Spectralis or Zeiss Cirrus at initiation and retains scanner for every patient throughout study. Each eye scanned. Heidelberg volume20°×20°,49 sections,16 ART frames; additional seven-line30°×5°,7 sections,25 ART frames. Follow-up uses baseline reference scan. Good quality score≥20, repeat poor/incomplete scans. Central subfield thickness recorded and immediately available for macular-edema decisions. Zeiss scans:macular cube (designation printed “512x218”),5-line raster; quality signal≥5, repeat poor/incomplete scans; record central subfield thickness. Heidelberg export central macular image and scan4 of7-line scan plus thickness-map PDF; Zeiss exports cube/raster images each eye. No macular-edema micrometer threshold appears here. Main matching key: central macular thickness, edema resolution, scanner adjustment/measurement definition.

### S-P002-07 — Fundus photograph grading timing

[Source pp.51,59](../../../../joi190092supp2_prod.pdf#page=51), PLAN. Color fundus photos at baseline,6 months,12 months or failure; reflex and nonstereoscopic images; masked graders assess NEI/Davis haze. p.59 repeats both-eye photo schedule and each-visit both-eye acuity and OCT. Main matching key: masked outcome grading and prespecified photograph comparison.

### S-P002-08 — Lab-dependent temporary interruption, resumption, and treatment failure

[Source p.52](../../../../joi190092supp2_prod.pdf#page=52), PLAN. Hemoglobin/hematocrit,platelet,WBC and percent neutrophils/lymphocytes; AST,ALT,creatinine,pregnancy test. Baseline samples within14 days of official visit; follow-up within visit window. Abnormalities causing non-serious AE,example AST/ALT twice upper limit of normal,stop drug immediately; allow1 month to regain eligibility and resume if normal (testing/resumption before1 month allowed). Otherwise failure and exit. Uncontrolled inflammation during interruption can cause lack-of-efficacy failure if at6-month visit. Severe-event threshold causes immediate cessation and exit. Main matching key: treatment-success composite, failures due tolerability/safety, analysis handling of cessation.

### N-P002-03 — Adverse-event thresholds and populations

[Source pp.52–53](../../../../joi190092supp2_prod.pdf#page=52), PLAN. Non-serious AEs any unfavorable occurrence in ever-treated patients regardless of causal relation. Examples:IOP>24 mmHg; AST/ALT>2 but<5×ULN;creatinine≥1.5 to<2 mg/dL;WBC below2.5 (no unit printed in this passage),accident/illness,preexisting symptom worsening,GI upset,nausea,vomiting,fatigue. Serious:A​​ST/ALT≥5×ULN,death,nonelective surgery/hospitalization,MI/stroke,life-threatening drug experience,persistent/significant disability/incapacity,other event classified severe. Each visit records onset/resolution; SAE/death to medical monitor within24 h. Main matching key: supplement/main safety definitions, safety analysis population, AE severity thresholds.

### S-P002-09 — Dataset structure and missing-value representation

[Source pp.54–56](../../../../joi190092supp2_prod.pdf#page=55), PLAN. Double entry by coordinator and independent operators; incomplete forms queried with original observer. Analysis exports Excel worksheets,one header,variables in columns/observations in rows;missing values explicitly character “NA”;categorical labels preferred to numeric codes,continuous units e.g.logMAR explicit,dated codebook accompanies each dataset version. NA is storage representation, not a stated imputation or analysis strategy. Data Analysis Committee merges unmasked data and randomization list,performs statistics and reports using R. No statistical model identified on these pages. Main matching key: missing data handling and final primary model should be obtained from SAP/other assigned plan scope.

### S-P002-10 — Adherence measurement

[Source p.57](../../../../joi190092supp2_prod.pdf#page=57), PLAN. Patient diaries of missed doses; medications brought to each follow-up;coordinator records number missed in adherence log; pill counts each visit. No adherence cutpoint or compliance-based analysis population specified. Main matching key: pill-count/self-report adherence and treatment discontinuation.

### S-P002-11 — Interim/stopping timing

[Source pp.60–61](../../../../joi190092supp2_prod.pdf#page=60), section10.4–10.5, PLAN. DAC conducts prespecified interim analysis when1/3 of patients complete study and supplies data to DSMC for stopping-guideline evaluation. Independent NEI-appointed DSMC reviews protocol before enrollment and periodically monitors data/recruitment/retention/outcomes; authorized conservative early stopping rule. No alpha spend,efficacy/futility cutoff,formal stopping boundary,or definition of “complete study” specified in this shard. Main matching key: interim timing and stopping rules; numerical boundaries require other plan/SAP scope.

## Administrative and no-applicable units

pp.54–61 also contain data-handling turnaround times,storage/security,weekly/biweekly/monthly reports,staff duties,committee structure,site visits,pharmacy and communication arrangements. These were opened completely. They add no randomized dose,primary/key-secondary outcome hierarchy,power assumption,multiplicity threshold,or result estimate beyond relationships above. pp.62–63 are bibliography only;reference sample sizes and article pagination are not trial quantitative results. p.64 marks new plan version,Version4.5 dated January06,2017; no endpoint or analysis definition appears on the title page. No supplied raw workbook exists within this shard, so no formula/cached-value distinction applies.

Coverage counts:32/32 mapped,32 reusable-backed,0 fresh-required at assignment,1 fresh confirmation derivative,1 existing image visually inspected,0 OCR steps,11 statistical-design/measurement relationship groups and3 numeric-definition groups. No source-unit mapping gap. Limitations: some referenced conversion tables/checklists and formal stopping boundaries are outside this assigned scope and must be mapped by their responsible shards; they have not been assumed absent from the package.
