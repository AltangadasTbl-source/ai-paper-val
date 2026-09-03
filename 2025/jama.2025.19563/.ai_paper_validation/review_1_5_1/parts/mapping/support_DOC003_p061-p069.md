# Support Quantitative Evidence Map — DOC-003 PDF pp. 61-69

## Scope and evidence handling

- **Source ID:** DOC-003 (`joi250084supp2_prod_1765403089.61751.pdf`), PDF pp. 61-69.
- **Scope status:** COMPLETE for the assigned nine PDF pages. This is an extraction and relationship map, not a candidate disposition or adjudication.
- **Reusable-backed pages:** pp. 61-66. Source-linked native text was used as a locator; the paired pre-existing rendered pages were visually checked for eTables 18a, 18b, 19a, 19b, and 20a-d where column placement matters.
- **Fresh-required pages:** pp. 67-69. Direct native and layout extraction were written to `preprocessing/DOC-003/p061-p069/page-067-native.txt`, `page-067-layout.txt`, `page-068-native.txt`, `page-068-layout.txt`, `page-069-native.txt`, and `page-069-layout.txt`. Pages 67-68 were also directly rendered at 180 dpi as `page-067.png` and `page-068.png` for column confirmation. CPU OCR was attempted for page 67 but did not yield usable text; its zero-byte output is retained as a preprocessing limitation and native/layout plus rendering were usable.
- **Cross-occurrence note:** This shard records within-scope table occurrences and their internal keys. Matching to the main paper and other supplement pages is deferred to the canonical merge/cross-source stage.

## Page-level map

### PDF p. 61 — eTables 18a and 18b

**D3C-N01 — Primary-endpoint sensitivity scenario counts and percentages.**

- **eTable 18a:** *Sensitivity Analysis of Primary Endpoint: “Best-Case” Scenario for Actigraph Non-Wear Periods*.
- Population/contrast: AI-Based Diabetes Prevention Program versus Human-Coach-Based Diabetes Prevention Program; primary outcome is diabetes risk reduction at 12 months.
- AI arm: 58/183 (31.7%); human-coach arm: 60/185 (32.4%).
- The footnote defines the best-case scenario: people not meeting actigraphy compliance are assumed to have achieved 150 minutes of weekly physical activity had they worn the device.
- **eTable 18b:** *Sensitivity Analysis of Primary Endpoint: Assuming Attainment of Physical Activity Goal for all participants*.
- Same printed outcome and arm values: 58/183 (31.7%) versus 60/185 (32.4%). Its footnote assumes every participant attained the 150 minute/week physical-activity guideline.
- Exact source location: DOC-003 PDF p. 61.
- Internal arithmetic locator: 58/183 = 31.69% and 60/185 = 32.43%, consistent with the displayed one-decimal percentages under ordinary rounding.

**D3C-S01 — One-sided confidence-bound reporting for eTables 18a and 18b.**

- Both tables label the contrast as **Risk Difference (One-Sided 95% CI)** in percentage points.
- Printed risk difference and one-sided bound: -0.74 (-8.8), for AI minus human-coach values shown above.
- Direction/scale: negative percentage-point risk difference corresponds to 31.7% minus 32.4%; the displayed percentages give an approximate -0.7 percentage-point difference, compatible with the more precise printed -0.74.
- The tables print only a one-sided endpoint, not a two-sided interval; no test statistic or P value is supplied on this page.
- Exact source location: DOC-003 PDF p. 61.

### PDF p. 62 — eTables 19a and 19b

**D3C-N02 — Cluster-robust sensitivity scenario counts and percentages.**

- **eTable 19a:** *Sensitivity Analysis Using Cluster-Robust Standard Errors by DPP Site*; primary outcome at 12 months: AI 58/183 (31.7%) and human-coach 59/185 (31.9%).
- Footnote/model definition: standard errors clustered by DPP site; the four Human-DPPs are distinct clusters (1-4), and all AI-DPPs are assigned to a fifth cluster.
- **eTable 19b:** *Sensitivity Analysis Using Cluster-Robust Standard Errors by Site and Month of Randomization*; same printed arm counts and percentages: 58/183 (31.7%) and 59/185 (31.9%).
- Footnote/model definition: participants clustered into cohorts by DPP site (four Human-DPP clusters and one AI-DPP cluster) and month of randomization.
- Exact source location: DOC-003 PDF p. 62.
- Internal arithmetic locator: 58/183 = 31.69% and 59/185 = 31.89%, consistent with the displayed percentages at one decimal place.

**D3C-S02 — One-sided cluster-robust confidence-bound reporting.**

- Both eTables label the measure **Risk Difference (One-Sided 95% CI)** in percentage points, for AI minus human-coach.
- eTable 19a: -0.20 (-4.8). eTable 19b: -0.20 (-6.8).
- The common point estimate is directionally compatible with 31.7% minus 31.9%; the differing one-sided lower bounds occur under the two stated clustering rules.
- No P value, test statistic, or two-sided interval is supplied for these tables.
- Exact source location: DOC-003 PDF p. 62.

### PDF p. 63 — eTable 20a, adverse events by category

**D3C-N03 — Participant-level adverse-event occurrence and event-level category distribution.**

- Table population denominators: AI-based program N=183; human-coach-based program N=185.
- Participants with at least one event: AI 66/183 (36.1%); human-coach 21/185 (11.4%). Footnote 1 defines these as participant-level counts and percentages.
- Category counts and percentages are explicitly event-level (footnote 2), so their denominators are total events rather than participants. The category values are:

| Category | AI events (% of AI events) | Human-coach events (% of human-coach events) |
|---|---:|---:|
| Musculoskeletal and connective-tissue disorders | 15 (15.0%) | 5 (20.0%) |
| Infections and infestations | 14 (14.0%) | 6 (24.0%) |
| Gastrointestinal disorders | 11 (11.0%) | 2 (8.0%) |
| Nervous-system disorders | 11 (11.0%) | 0 (0.0%) |
| General disorders and administration-site conditions | 8 (8.0%) | 2 (8.0%) |
| Respiratory, thoracic, and mediastinal disorders | 7 (7.0%) | 1 (4.0%) |
| Injury, poisoning, and procedural complications | 6 (6.0%) | 2 (8.0%) |
| Renal and urinary disorders | 6 (6.0%) | 1 (4.0%) |
| Cardiac disorders | 5 (5.0%) | 2 (8.0%) |
| Neoplasms (benign, malignant, and unspecified) | 4 (4.0%) | 1 (4.0%) |
| Surgical and medical procedures | 4 (4.0%) | 1 (4.0%) |
| Immune-system disorders | 3 (3.0%) | 1 (4.0%) |
| Endocrine disorders | 3 (3.0%) | 0 (0.0%) |
| Hematologic disorders | 2 (2.0%) | 0 (0.0%) |
| Psychiatric disorders | 1 (1.0%) | 1 (4.0%) |

- Exact source location: DOC-003 PDF p. 63.
- Internal aggregation locator: category counts sum to 100 AI events and 25 human-coach events; the displayed event-level percentages correspond to those totals. The participant-level percentages are compatible with 66/183 and 21/185 under one-decimal rounding.

### PDF pp. 64-65 — eTables 20b and 20c

**D3C-N04 — Adverse-event grade totals and intervention-relatedness totals.**

- **eTable 20b, Adverse Events by Grade:** AI/human-coach counts are Grade 1 (mild) 13/5; Grade 2 (moderate) 42/11; Grade 3 (severe) 43/8; Grade 4 (life-threatening) 2/1; total events 100/25.
- **eTable 20c, Adverse Events by Relatedness to Assigned Intervention:** Definitely related 0/0; probably related 0/0; possibly related 0/0; not related 100/25.
- Exact source locations: DOC-003 PDF pp. 64-65, respectively.
- Internal aggregation locators: grade counts sum to 100 AI and 25 human-coach events; relatedness categories also sum to 100 and 25, matching the totals printed in eTable 20b and the event-level category totals on p. 63.

### PDF pp. 66-68 — eTable 20d, adverse events by condition and grade

**D3C-N05 — Condition-by-grade event-count table, continued across three pages.**

- Table title and measures: *eTable 20d. Adverse Events by Condition and Grade*; columns are number of adverse events in the AI-based and human-coach-based programs. Blank cells are displayed as no count; this map does not convert blanks to a newly printed value.
- **Grade 1 subtotal (p. 66):** AI 13, human-coach 5. Conditions: COVID-19 5/4; exacerbation of asthma 1/blank; facial laceration 1/blank; generalized anxiety disorder 1/blank; hypertension blank/1; influenza 1/blank; osteopenia 1/blank; plantar fasciitis 1/blank; sinusitis 1/blank; trigger finger 1/blank.
- **Grade 2 subtotal (p. 66):** AI 42, human-coach 11. Page-66 conditions: abdominal pain 1/blank; anemia 1/blank; anxiety blank/1; back pain 1/1; bacterial vaginosis 1/blank; benign prostatic hyperplasia blank/1; bleeding postoperative blank/1; bronchitis blank/1; COVID-19 2/blank; chest pain 1/1; concussion 1/blank; dermatitis allergic 3/blank; diarrhea 1/blank; diverticulitis 1/blank; eye injury blank/1; foreign body, ear 1/blank; fracture of the distal radius 1/blank; gallbladder polyps 1/blank; gastroparesis 1/blank; gout 1/blank; heel spur 1/blank; hip injury 1/blank; hypercalcemia 1/blank; hypercholesterolemia 1/blank; hypertension 1/blank; inflammatory bowel disease 1/blank; influenza blank/1; leg pain blank/1; lipoma excision blank/1; lumbar vertebral fracture 1/blank; meniscus tear 1/1.
- **Grade 2 continuation (p. 67):** migraine 2/blank; nasal polyp 1/blank; nephrolithiasis 2/blank; neuralgia 1/blank; neuropathy 1/blank; neutropenia 1/blank; prostate cancer 1/blank; sialoadenitis 1/blank; sinusitis 2/blank; sleep apnea 1/blank; urinary tract infection 2/blank; vomiting 1/blank. The p. 66 and p. 67 condition values sum to the printed Grade-2 subtotal, 42/11.
- **Grade 3 subtotal (p. 67):** AI 43, human-coach 8. Conditions: AV block 1/blank; allergic reaction blank/1; ankle fracture 1/blank; atrial fibrillation 3/blank; back pain blank/1; brain tumor 1/blank; breast cancer 2/1; COVID-19 4/1; chest pain 3/blank; diabetes 1/blank; diarrhea blank/1; ear pain 1/blank; flank pain 3/blank; foot drop 1/blank; foot surgery 1/blank; hammer toe surgery 1/blank; headache 1/blank; hip fracture blank/1; hip pain 1/blank; inflammatory bowel disease 1/blank; interstitial lung disease 1/blank; knee pain blank/1; melanoma 1/blank; meniscus tear 1/blank; nephrolithiasis 1/blank; pancreatitis 1/blank; Parkinson's disease 1/blank; prostate cancer 1/blank; rectal bleeding 1/blank; rotator cuff surgery 1/blank; stem cell procedure 1/blank; supraventricular tachycardia blank/1; surgical and medical procedures 2/blank; syncope 1/blank; temporal arteritis 1/blank.
- **Grade 3 continuation (p. 68):** vasovagal syncope 1/blank; vertigo 1/blank; wrist surgery 1/blank. These continuation values complete the printed Grade-3 subtotal of 43/8.
- **Grade 4 subtotal (p. 68):** AI 2, human-coach 1. Conditions: appendicitis 1/blank; perforated gallbladder blank/1; pulmonary embolism 1/blank. These condition values equal the Grade-4 subtotal.
- Exact source locations: DOC-003 PDF pp. 66-68. Page 67 and p. 68 column assignments were confirmed from fresh direct rendering.
- Cross-table locators: grade subtotals reproduce eTable 20b (p. 64), and their combined totals are 100/25. This is a source-location and quantitative relationship map; it does not adjudicate whether similarly named conditions across different grades are clinically the same event.

### PDF p. 69 — references

**D3C-N06 — No result-relevant support relationship.**

- Page 69 contains references 1-8 only. It has bibliographic volume/issue/page/year/DOI numerals but no study result, outcome count, denominator, effect estimate, interval, P value, table, figure, formula, analysis definition, or matching main-paper quantitative occurrence.
- Exact source location: DOC-003 PDF p. 69.

## Extraction limitations and handoff notes

- No statistical P value, test statistic, standard error, or two-sided confidence interval is printed on pp. 61-69. The sensitivity tables explicitly provide one-sided 95% confidence bounds only.
- The condition table spans three pages; blank table cells are preserved as displayed blanks rather than inferred zeroes. The only explicit zeroes in this scope appear in eTable 20a category counts (pp. 63) and eTable 20c relatedness counts (p. 65).
- Provisional keys in this shard are `D3C-N01` through `D3C-N06` and `D3C-S01` through `D3C-S02`; canonical N/S IDs, cross-source matching, and any candidate assessment remain for later stages.
