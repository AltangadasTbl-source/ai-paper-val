# Support quantitative evidence extraction — complete lane

## Scope and evidence basis

Freshly mapped direct-source units: DOC-002 PDF pp.1-129, DOC-003 PDF pp.1-5, and DOC-004 PDF p.1. Evidence used only current native/layout page assets under `preprocessing/native_text/pages/` and `preprocessing/layout_text/pages/`, with rendered-page confirmation where supplied. Source links below are package-relative direct PDFs with a `#page=` locator; page assets are stated where a visual table/figure requires it.

## Complete page coverage

| Source and pages | Mapping disposition |
|---|---|
| DOC-002 pp.1-5 | Contents, identifiers, investigators and administrative material; no result relationship. |
| DOC-002 pp.6-7 | Initial-protocol English/French abstract: planned design, eligibility, endpoints, sample calculation. |
| DOC-002 pp.8-19 | Background/device definitions and external-literature context; only device and outcome definitions at p.10 directly retained. |
| DOC-002 pp.20-30 | External-literature/preliminary-study summary and Figure 3; retained only matching comparator definitions/printed preliminary values, not treated as trial results. |
| DOC-002 pp.31-37 | Background/participating-centre administration and recruitment table; no current-trial result relationship. |
| DOC-002 pp.38-55 | Initial protocol: planned endpoint, population, intervention, randomisation, sample size and statistical rules. |
| DOC-002 pp.56-69 | eCRF/ethics/safety/reference material; no result relationship. |
| DOC-002 pp.70-81 | Final-protocol cover, patient information/consent; pp.72-73 retain planned N=778, superiority aim, duration and 10-mL blood draw; remaining pages no result relationship. |
| DOC-002 pp.82-83 | Original statistical plan: planned estimands and models. |
| DOC-002 pp.84-89 | Published-protocol author/affiliation material; no result relationship. |
| DOC-002 pp.90-105 | Published protocol: planned superiority design, eligibility, N, intervention, randomisation and statistical plan. |
| DOC-002 pp.106-121 | Discussion/status/references. p.107 retains enrollment status (686); all other pages no result relationship. |
| DOC-002 pp.122-128 | Reprinted device/outcome-definition tables and external-literature table. pp.122-123 retain definitions; pp.124-128 external-literature/context only. |
| DOC-002 p.129 | Blank terminal page; no result relationship. |
| DOC-003 pp.1-5 | Results supplement: eTable and three eFigures, including displayed risk sets and labels. |
| DOC-004 p.1 | Data-sharing statement; no result-relevant quantitative relationship. |

## Extracted evidence groups

### DOC-002 protocol/SAP and supporting definitions

- `SUP-N001` — Initial protocol abstract: day-28 all-cause mortality; non-inferiority HFNO versus usual care; 26 centres; expected control mortality 26%; margin 9%; alpha 5%; power 80%; 408/group, 816 total; recruitment 24 months plus 6 months follow-up. [DOC-002 p.6](../../../joi180109supp1_prod.pdf#page=6), repeated French p.7.
- `SUP-N002` — Initial protocol definitions: HFNO is humidified/warmed oxygen at >15 L/min; usual oxygen includes low-flow and medium-flow named devices; oxygenation can be continuous SpO2, fixed-time PaO2, or PaO2/FiO2; ventilation PaCO2; comfort/dyspnea VAS/Borg; complications include NIV, intubation/MV, mortality. [DOC-002 p.10](../../../joi180109supp1_prod.pdf#page=10), repeated pp.122-123.
- `SUP-N003` — Initial protocol planned primary/secondary endpoint set: primary day-28 mortality; secondary intubation (days 3 and 28), VAS comfort/dyspnea, respiratory rate, lowest SpO2 D1-D3, PaO2/FiO2 D1-D3, ICU stay, ICU infection, Murray score, oxygen-/ventilation-free days at D28, reintubation, lowest median SpO2 during intubation, mortality after HFNO failure and satisfaction. [DOC-002 pp.38,46-47](../../../joi180109supp1_prod.pdf#page=38).
- `SUP-N004` — Initial planned treatment/thresholds: control target SpO2 >=95% and discharge eligibility SpO2 >=95% on <2 L/min; HFNO begins 50 L/min and FiO2 100%, rises to 60 L/min if needed, then FiO2 tapered to target; minimum 40 L/min; stop after PaO2/FiO2 >300 plus SpO2 >=95% on <2 L/min. [DOC-002 pp.44-45](../../../joi180109supp1_prod.pdf#page=44).
- `SUP-N005` — Initial planned stratification: PaO2/FiO2 <200 versus >=200 and additional organ dysfunction (SOFA definition); four pre-defined subgroups include post-randomisation intubation, post-extubation HFNO, intubated patients, and DNI patients. [DOC-002 pp.45-46](../../../joi180109supp1_prod.pdf#page=45).
- `SUP-N006` — Initial-protocol eligibility/reference population: need for O2 includes RR >30/min or SpO2 <90%; steroids >3 months or >0.5 mg/kg/day; patients with DNI eligible. [DOC-002 pp.42-43](../../../joi180109supp1_prod.pdf#page=42).
- `SUP-N007` — Initial randomisation text: two parallel groups 1:1; two stated stratification factors but text says eight lists; patient-level intervention assessment and printed statement “randomisation unit is the centre.” [DOC-002 p.50](../../../joi180109supp1_prod.pdf#page=50).
- `SUP-N008` — Initial preliminary/comparator data retained for version/comparator matching: cohort 178 split 76 (43%), 74 (42%), 20 (11%), and 8; mortality 37% versus 52%, p=0.04; iVNIctus subset 141/374 (38%). Figure 3 has labelled treatment groups n=78,24,89,42,28,53,18,42. These are non-current-trial preliminary/external values. [DOC-002 pp.29-30](../../../joi180109supp1_prod.pdf#page=29); render `preprocessing/rendered_pages/DOC-002-p030.png`.
- `SUP-N009` — Final patient information: 778 planned ARF participants; HFNO versus low/medium-flow usual care, framed as superiority for day-28 mortality; 30-month study and 6-month individual participation; nasal swab plus one 10-mL blood tube. [DOC-002 pp.72-73](../../../joi180109supp1_prod.pdf#page=72).
- `SUP-N010` — Published-protocol sample/design: superiority RCT, 30 ICUs; standard-group 30% mortality, HFNO 20%, alpha 5%, power 90%, 389/group/778 total, 30-month recruitment and 28-day additional follow-up. [DOC-002 pp.90-91](../../../joi180109supp1_prod.pdf#page=90).
- `SUP-N011` — Published-protocol population: oxygen >=6 L/min; adult >=18; immunosuppression definitions; PaCO2 >=50 mmHg excluded when NIV indicated; post-surgical D1-D6 excluded. [DOC-002 p.98](../../../joi180109supp1_prod.pdf#page=98).
- `SUP-N012` — Published intervention thresholds: standard target SpO2 >=95%, discharge <6 L/min; HFNO starts 50 L/min/FiO2 100%, increases 60 L/min, minimum 50 L/min first 3 days, stop after PaO2/FiO2 >300 and SpO2 >=95% on <6 L/min. [DOC-002 pp.99-100](../../../joi180109supp1_prod.pdf#page=99).
- `SUP-N013` — Published randomisation: time since ICU (D0/D1/D2 vs >=D3), oxygen flow < versus >=9 L/min to reach SpO2 >=95%, and catecholamine shock; 1:1 and eight lists; patient-level impact plus printed “randomization unit is the center.” [DOC-002 p.99](../../../joi180109supp1_prod.pdf#page=99).
- `SUP-N014` — Data-collection definitions: worst RR, SpO2, oxygen flow/FiO2 and blood-gas/chest-x-ray values; ICU-acquired infection is new onset >48 hours after ICU admission with a new antibiotic regimen. [DOC-002 p.101](../../../joi180109supp1_prod.pdf#page=101).
- `SUP-N015` — Published protocol status: enrollment began May 2016; first interim analysis 13 March 2017; 686 included on 13 November 2017; expected completion February 2018. [DOC-002 p.107](../../../joi180109supp1_prod.pdf#page=107).

### DOC-003 reported supplementary results

- `SUP-N016` — eTable at six hours: both randomized groups N=388. HFNO/standard, respectively: invasive MV 39 (10.0%)/46 (11.8%); RR 25 [20-30]/26 [21-31] per min; standard O2 only 0/342 (88.2%); O2 flow 50 [50-60]/8 [6-15] L/min; NIV 0/0; high-flow in non-intubated patients 349 (100%)/0; FiO2 70 [60-90]/not reported; PaO2/FiO2 150 [104-230]/119 [86-165]. [DOC-003 p.2](../../../joi180109supp2_prod.pdf#page=2); render `preprocessing/rendered_pages/DOC-003-p002.png`.
- `SUP-N017` — eFigure 1: cumulative incidence of mechanical ventilation, two labelled treatment curves; log-rank P=0.17. Numerical risk set/time values are not printed. [DOC-003 p.3](../../../joi180109supp2_prod.pdf#page=3); render `preprocessing/rendered_pages/DOC-003-p003.png`.
- `SUP-N018` — eFigure 2A RR risk sets, HFNO/standard at randomization,H6,D1,D2,D3,D4,D5,D6,D7: 388/388, 388/388, 388/388, 346/345, 346/345, 291/275, 257/237, 217/206,196/169. Asterisk at H6 only; plotted central values are graphical/unlabelled. [DOC-003 p.4](../../../joi180109supp2_prod.pdf#page=4); render `preprocessing/rendered_pages/DOC-003-p004.png`.
- `SUP-N019` — eFigure 2B PaO2/FiO2 risk sets, HFNO/standard at randomization,H6,D1,D2,D3,D4,D5,D6,D7: 388/388,318/311,388/388,293/210,293/210,193/141,158/129,138/112,126/96. Double asterisks shown H6,D1,D2,D3; plotted values graphical/unlabelled. [DOC-003 p.4](../../../joi180109supp2_prod.pdf#page=4); render `preprocessing/rendered_pages/DOC-003-p004.png`.
- `SUP-N020` — eFigure 3A comfort-VAS risk sets HFNO/standard at randomization,H6,D1,D2,D3,D4,D5,D6,D7: 388/388,321/314,298/276,174/178,174/178,126/113,99/95,81/70,63/49. [DOC-003 p.5](../../../joi180109supp2_prod.pdf#page=5); render `preprocessing/rendered_pages/DOC-003-p005.png`.
- `SUP-N021` — eFigure 3B dyspnea-VAS risk sets HFNO/standard at randomization,H6,D1,D2,D3,D4,D5,D6,D7: 388/388,309/289,218/224,156/152,156/152,117/96,89/83,76/63,61/47. [DOC-003 p.5](../../../joi180109supp2_prod.pdf#page=5); render `preprocessing/rendered_pages/DOC-003-p005.png`.

### DOC-004

- `SUP-N022` — No result-relevant quantitative relationship. The statement says data are unavailable “for now” due to an engagement to share individual-level data for a meta-analysis; no timing/count/access metric is printed. [DOC-004 p.1](../../../joi180109supp3_prod.pdf#page=1).

All relationship keys and their formal numeric/statistical map records are in the two companion lane artifacts.
