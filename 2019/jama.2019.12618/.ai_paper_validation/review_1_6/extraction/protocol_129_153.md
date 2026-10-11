# Protocol tail quantitative evidence map

Scope: DOC-003 joi190092supp2_prod.pdf PDF pages 129–153 inclusive, 25/25 mapped. All content is PLAN, including revision history. MOP header version 4.5, 6 January 2017; printed MOP pages 65–83 correspond to PDF129–147. PDF148–153 are protocol revision history with explicit earlier version boundaries. Extraction is observation and relationship mapping only; no candidate diagnosis.

Evidence: hashed reusable `.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp129_153_layout.txt`, Poppler layout; all page records read. Fresh-required PDF133,134,136: direct `pdftotext -f N -l N -layout joi190092supp2_prod.pdf .ai_paper_validation/review_1_6/preprocessing/plan_tail_protocol_N_layout.txt` confirmed empty text; direct `pdftoppm -f N -l N -singlefile -r 110 -png joi190092supp2_prod.pdf .ai_paper_validation/review_1_6/preprocessing/plan_tail_protocol_N` rendered each page and each was opened using view_image. Engines Poppler26.01.0. All three contain substantive image-only operational content; direct visual mapping closes all gaps, OCR unnecessary. Redacted administrative credentials are not transcribed.

## Complete page register

| PDF page | Printed page or version | Mapping record |
|---|---|---|
| 129 | 65 | Miami nine-point haze scale figure; active retinal/choroidal inflammation and observer measurement rules; N-PT001–003 |
| 130 | 66 | Observer certification and OCT acquisition parameters; N-PT004–006 |
| 131 | 67 | OCT scan parameters, quality score and central-subfield thickness; N-PT006–007 |
| 132 | 68 | OCT storage/export naming only; no applicable numeric result or inferential relationship |
| 133 | 69 | FRESH visual: Zeiss Cirrus macular cube and five-line raster per eye, default acquisition caption; N-PT008 |
| 134 | 70 | FRESH visual: signal strength ≥5, central-subfield thickness, two operators; N-PT009–010 |
| 135 | 71 | Photo schedule, laboratory assessment, laboratory stopping/resumption/failure rules; N-PT011–013 |
| 136 | 72 | FRESH visual: AE/SAE thresholds and lab-SAE phase restriction; N-PT014–017 |
| 137 | 73 | SAE relatedness adjudication, six-month follow-up and death reporting; N-PT018 |
| 138 | 74 | Data forms review, double entry and consistency checks; operational only, no applicable numeric result/inference |
| 139 | 75 | NA and units/codebook definitions; N-PT019. Thirty-day entry-delay trigger is administrative only |
| 140 | 76 | Data security and weekly/monthly recruitment reports; no applicable numeric result/inference |
| 141 | 77 | Missed-dose logs and pill counts; N-PT020. Twice-yearly chart audits are administrative only |
| 142 | 78 | Staff duties; record BSCVA in letters and Snellen equivalents; N-PT021 |
| 143 | 79 | Photo visits, reading-center masked measurements; N-PT011,022 |
| 144 | 80 | Reading-center scale names and interim time points; N-PT022; S-PT001 |
| 145 | 81 | Site administration/pharmacy/communications; no applicable numeric result/inference |
| 146 | 82 | Bibliography only: numerals in citation titles identify historical papers, not supplied trial-result data; no applicable relationship |
| 147 | 83 | Bibliography continuation only; no applicable relationship |
| 148 | protocol revisions2.0–2.4 | Versioned primary-regression and enrollment threshold changes; S-PT002; N-PT023–025 |
| 149 | revisions2.4–3.1 | Masking operational revision, injection exclusion and eligibility time changes; N-PT026–028 |
| 150 | revision3.1 | Prior and revised enrollment definitions; N-PT029–031 |
| 151 | revisions3.2–4.0 | Prednisone taper target and enrollment-assessment windows; N-PT032–034 |
| 152 | revisions4.0–4.3 | Prior-IMT exclusion amendment; N-PT035–036 |
| 153 | revisions4.3–4.5 | Laboratory persistence threshold and PhaseII entry exception; N-PT037–039 |

## Numeric, definition, and matching-key relationships

IDs are shard-local; coordinator assigns global N/S identifiers. Every location below has role PLAN. Values separated by semicolons belong to the stated one relationship. Matching keys refer to main-paper endpoint/measurement/population keys without asserting equivalence to any report result.

| Local ID | PDF source location | Printed content and quantitative rule | Main-paper matching key |
|---|---|---|---|
| N-PT001 | [p129](../../../joi190092supp2_prod.pdf#page=129) Figure2 | Miami nine-point photographic vitreous-haze scale, distinct from NEI scale. Labels are scale identity, not a reported numeric result. | haze measurement/scale |
| N-PT002 | [p129](../../../joi190092supp2_prod.pdf#page=129) retinal/choroidal inflammation | Vasculitis posterior to equator active by SUN with angiographic confirmation; isolated macular edema insufficient; bullous serous detachment with any accompanying vitreous/retinal/choroidal inflammation qualifies; ≥1+ AC inflammation, vitreous haze and/or other retinal/choroidal lesions aside from edema also active. | control of inflammation; macular edema |
| N-PT003 | [p129](../../../joi190092supp2_prod.pdf#page=129) §5.3.3 | Duplicate observers at baseline phasesI/II, month6 phasesI/II, month12 phaseI or earlier failure; primary study ophthalmologist measurements used in primary analysis; anterior cells/flare, vitreous cells/haze, retinal/choroidal lesions measured. | endpoint observer/source; month6 |
| N-PT004 | [p129](../../../joi190092supp2_prod.pdf#page=129)–p130 §5.3.4 | Physician and coordinator certification score80%; below80% instruction/retest. | measurement certification context |
| N-PT005 | [p130](../../../joi190092supp2_prod.pdf#page=130) §5.3.4 | Five uveitis patients; discrepancy >1 grade prompts further patients until five consecutive within1 level for each measurement; both observers finding zero in each area excludes that patient from five; annual assessment. | observer measurement reliability |
| N-PT006 | [p130](../../../joi190092supp2_prod.pdf#page=130)–p131 §5.4.1–2 | Heidelberg volume20°×20°,49 sections,16 ART frames; seven-line30°×5°,7 sections,25 ART frames; each eye. Preferred Heidelberg Spectralis; Zeiss Cirrus permitted if unavailable. | OCT machine/mac thickness |
| N-PT007 | [p131](../../../joi190092supp2_prod.pdf#page=131) §5.4.2–3 | Heidelberg good-quality score at least20; record central-subfield thickness of each eye. | OCT quality/mac thickness |
| N-PT008 | [p133](../../../joi190092supp2_prod.pdf#page=133) visual §5.4.5–6 | One macular cube and one five-line raster centered on macula per eye; exact printed default caption “Scan Macular Cube 512x218 HD”; no normalized correction to acquisition caption. | OCT acquisition identity |
| N-PT009 | [p134](../../../joi190092supp2_prod.pdf#page=134) visual §5.4.6–7 | “5 Line Raster HD” scan; signal strength at least5 or higher; record central-subfield thickness on data sheet; both-eyes scans exported. | OCT quality/mac thickness |
| N-PT010 | [p134](../../../joi190092supp2_prod.pdf#page=134) visual §5.4.9 | At least two qualified OCT personnel per site. | measurement acquisition context |
| N-PT011 | [p135](../../../joi190092supp2_prod.pdf#page=135) §5.5; p143 §9.10 | Fundus photography baseline,6mo,12mo or treatment failure; masked NEI and Miami grading. | haze/photo visit |
| N-PT012 | [p135](../../../joi190092supp2_prod.pdf#page=135) §5.6 | Hemoglobin/hematocrit, platelet/WBC counts, neutrophil/lymphocyte percentages, CD4 count; CD4 only UCSF/AEH/KKESH at baseline,months3,6,12. AST,ALT,creatinine,pregnancy measured; baseline labs4weeks prior, follow-up inside visit window, every visit. | safety laboratories and denominators |
| N-PT013 | [p135](../../../joi190092supp2_prod.pdf#page=135) §5.6 | Non-serious abnormality example AST/ALT twiceULN triggers immediate study-drug stop; one month to return to normal and resume (earlier normal permits earlier restart); otherwise failure; follow six-month visit. | safety failure/tolerability |
| N-PT014 | [p136](../../../joi190092supp2_prod.pdf#page=136) visual first paragraph | LabSAE threshold immediately stops drug and declares treatment failure; six-month follow-up; labSAE prohibits PhaseII switch. | laboratorySAE/failure/rescue population |
| N-PT015 | [p136](../../../joi190092supp2_prod.pdf#page=136) visual §6.1 | Non-serious AE examples IOP>24mmHg; AST/ALT≥2 but<5 timesULN; creatinine≥1.5 to<2mg/dL; white-blood-cell count2.5 or below (unit not printed here). Any unfavorable occurrence after any study medication regardless causal relationship. | nonserious AE threshold/count |
| N-PT016 | [p136](../../../joi190092supp2_prod.pdf#page=136) visual §6.2 | SAE AST/ALT≥5timesULN; also death, hospitalization/surgery, MI/stroke, life-threatening event, disability, cancer, seizure, congenital anomaly or intervention preventing permanent impairment. | SAE threshold/categories |
| N-PT017 | [p136](../../../joi190092supp2_prod.pdf#page=136) visual §6.3 | AE log onset/resolution each visit; SAE narrative submitted to medical monitor/PI/coordinator within24h. | event observation/reporting window |
| N-PT018 | [p137](../../../joi190092supp2_prod.pdf#page=137) §6.3–4 | NonlaboratorySAE requires medical-monitor attribution before declaring failure; assess safety of PhaseII switch; otherwise follow6mo; SAE by arm toDSMC each6mo; death reported24h. | attribution/failure/rescue population |
| N-PT019 | [p139](../../../joi190092supp2_prod.pdf#page=139) §7.3.3 | Analysis rows=observations, columns=variables, missing values explicit NA; continuous-variable units including logMAR unambiguous in versioned codebook. | missingness/units |
| N-PT020 | [p141](../../../joi190092supp2_prod.pdf#page=141) §8.4 | Missed doses recorded in medication log from individual calendars; pill counts every visit. | adherence denominator |
| N-PT021 | [p142](../../../joi190092supp2_prod.pdf#page=142) §9.8 | Each-eye BSCVA every visit recorded as number of letters read and Snellen equivalent. | BSCVA scale |
| N-PT022 | [p143](../../../joi190092supp2_prod.pdf#page=143)–p144 §9.11/10.3 | Reading center grades fundus haze using NEI and Miami, and OCT type of edema/epiretinal membrane; measurements distinguished from primary physician clinical examination. | photographic vs clinical outcomes |
| N-PT023 | [p148](../../../joi190092supp2_prod.pdf#page=148) revision2.1,1Mar2013 | Abnormal hemoglobin exclusion threshold changed from≤10 to≤9; historical Indian values9–10 rationale. | enrollment/lab eligibility |
| N-PT024 | [p148](../../../joi190092supp2_prod.pdf#page=148) revisions2.1/2.2 | Week2 window±3days; phaseI6–12mo lab visits added7,8,10,11; surgery planning next6mo added exclusion1May2013. | visit window/safety schedule |
| N-PT025 | [p148](../../../joi190092supp2_prod.pdf#page=148) revision2.3 | 22Jul2013 adds Melbourne/Mexico City sites, moves data collection/enrollment back3mo;2.4 adds Northwestern19Aug2013. | site membership/version |
| N-PT026 | [p149](../../../joi190092supp2_prod.pdf#page=149) revisions2.4–2.6 | Drug-name bottles placed opaque bags;2Dec2013 exclusion adds periocular/intravitreal steroid injection in previous4weeks; NSAID consent amendment1Oct2013 contains no trial numeric result. | masking and injection eligibility |
| N-PT027 | [p149](../../../joi190092supp2_prod.pdf#page=149) revision3.0,24Mar2014 | TumblingE changes to ETDRS charts; failed steroid taper window14days→4weeks; abnormal AST/ALT/CBC14days→4weeks; specified infectious-test window60days→90days. | visual-acuity scale and enrollment windows |
| N-PT028 | [p149](../../../joi190092supp2_prod.pdf#page=149) revision3.1 preamble | 8May2014 enrollment broadened; old/new details continue p150; version boundary retained. | enrolled population |
| N-PT029 | [p150](../../../joi190092supp2_prod.pdf#page=150) revision3.1 old criteria | Active last90days defined AC≥2+,haze≥2+,or active retinal/choroidal lesions; additional criterion active after4weeks1mg/kg prednisone-equivalent or4+weeks postinjection; taper rebound≥1grade or inactive→active lesion in previous4weeks; or known SUN condition. | historical eligibility |
| N-PT030 | [p150](../../../joi190092supp2_prod.pdf#page=150) revision3.1 revised criteria | Active last180days with same inflammation threshold; additional options active after4weeks1mg/kg oral steroid; rebound≥1grade/inactive→active in previous180days; ≥10mg/day prednisone-equivalent past≥90days; long-acting injection4–180days before; listed disease. Native glyph “³10” corresponds to ≥10 as eligibility inequality. | amended eligibility |
| N-PT031 | [p150](../../../joi190092supp2_prod.pdf#page=150)–p151 revision3.1 diseases | Behçet posterior involvement, multifocal choroiditis with panuveitis, serpiginous choroidopathy,birdshot,diffuse retinal vasculitis,VKH bullous serous/choroidal detachment,sympathetic ophthalmia. | disease subgroup |
| N-PT032 | [p151](../../../joi190092supp2_prod.pdf#page=151) revisions3.2/3.3 | Riyadh added29Jul2014;12Dec2014 phaseI oral prednisone target maintained7.5mg/day, not lower (clinical judgment). | sites/steroid success threshold |
| N-PT033 | [p151](../../../joi190092supp2_prod.pdf#page=151) revision3.3 | Active acuteVKH≥4weeks qualifies; enrollment eye exam/visual acuity may occur up to7days before baseline. | eligibility/baseline |
| N-PT034 | [p151](../../../joi190092supp2_prod.pdf#page=151) revisions3.4/3.5 |13Jan2015 removes mandatoryHIV specimen60day window;6Apr2015 clarifies Indian IND-VFQ additional to all-site NEI-VFQ, Miami preferred to Davis, persistent-edema injection allowed first90days both phases, NEI haze eligibility scale,14/60day old lab references corrected4week/90day. | QoL/site scales; eligibility/injection |
| N-PT035 | [p152](../../../joi190092supp2_prod.pdf#page=152) revision4.0 |30Apr2015 removes month6 from phaseI6–12mo window table, changes data entry location Madurai. | visit schedule/version |
| N-PT036 | [p152](../../../joi190092supp2_prod.pdf#page=152) revision4.1 |26Jun2015 prior-IMT exclusion changes: allow>12months earlier without prior AE; exclude noncorticosteroidIMT past12mo, priorMTX/MMF intolerance/safety/failure and biologic at any time. Form submission7→10days;4.2 adds Pondicherry21Sep2015. | priorIMT population/site |
| N-PT037 | [p153](../../../joi190092supp2_prod.pdf#page=153) revision4.4 |26Feb2016: lab remains at or above nonseriousAE threshold28days→SAE and immediate failure; CD4onlyAEH/KKESH/UCSF baseline,3,6,12mo. | labSAE/failure |
| N-PT038 | [p153](../../../joi190092supp2_prod.pdf#page=153) revision4.5 |6Jan2017: PhaseII entry ordinarily within2week window; coordinating-center exception allowed; clinical/secondary-eye-exam forms omitted if PhaseII starts different day from phaseI failure. | rescue entry/baseline |
| N-PT039 | [p153](../../../joi190092supp2_prod.pdf#page=153) revision4.5 | Secure REDCap online randomization replaces paper list holders; emergency personnel can look up assignments; revised§4.3.2. | randomization version |

## Statistical relationships

| Local ID | Source | Printed prospective statement | Matching key |
|---|---|---|---|
| S-PT001 | [p144](../../../joi190092supp2_prod.pdf#page=144) §10.5–6 | Prespecified interim primary-outcome analyses when1/3 and2/3 of primary outcome data collected; DSMC unmasked reports at these two time points; SAE arm reports every6months. No alpha boundary supplied on this page. | interim analysis/inference |
| S-PT002 | [p148](../../../joi190092supp2_prod.pdf#page=148) revision2.0,26Sep2012 | Primary regression changed to only treatment arm and site as predictors in response to firstDSMC feedback. Historical amendment, not assumed finalSAP model. | primary regression adjustment/version |

## Completion

25 unique pages mapped;22 reusable-backed and3 fresh-required.39 numeric/definition relationships and2 statistical relationships. No applicable result/inference explicitly recorded on administrative/reference pages. No uncovered page, extraction gap, or scientific gap remains. No workbook/formula-cache source is present in this assigned scope. All original sources and reusable assets preserved.
