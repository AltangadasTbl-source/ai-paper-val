# Support quantitative map: support-003

Runtime agent: /root/support_mapper_3. Scope: DOC-002, `joi240158supp1_prod_1742927563.7611.pdf`, PDF pages 153–229 inclusive, 77 pages. All assigned content is PLAN. Pages 153–154 finish RSA C version 3.0, 3 June 2020. Pages 155–229 form the full 75-page RSA C version 6.0, 7 November 2022. Version applicability to reported analyses is left for cross-source review. No findings or candidate judgments are made.

Coverage: 77/77 pages mapped, 76 reusable-backed and 1 fresh-required (p187), zero scientific coverage gaps. No Office, workbook or CSV sources are assigned; workbook formulas/cached values are not applicable. Graph heights without printed values are not represented as exact numbers. Historical preclinical results are separated from prospective clinical relationships.

## Evidence and tooling

Read complete QUALITY_CONTROL_SCOPE.md and review_contract.md, and current coverage, source inventory, evidence inventory and tooling record. Read all 77 form-feed segments in the canonical reusable `review_1_5_3/preprocessing/support-003/doc002_p153_p229_native.txt`. Used its layout counterpart for schedule alignment on pp163–168; companion OCR and page images for pp174,175,177–183,195,213–221. Figures pp174,175,177–183,195 were visually inspected. Legacy derivative engines are UNKNOWN_LEGACY. Original PDF remains final authority; no sources or reused assets were modified.

Fresh p187: `/home/juliz/venvs/stt/bin/python workflow_1_6_2/scripts/pdf_tools.py text joi240158supp1_prod_1742927563.7611.pdf --first 187 --last 187 .ai_paper_validation/review_1_6_2/preprocessing/support-003/p187_native.txt`, then the same helper's `render` command with `--page 187` and output `preprocessing/support-003/p187.png`. Engine: PyMuPDF 1.28.0. Rendering: CPU, 200 dpi. Direct visual inspection with view_image confirms blank body and only RSA C version 6.0 footer/internal page 33 of 75. No OCR was necessary. The user requested GPU OCR; this shard needed no new OCR.

All source links below resolve relative to this artifact. Matching main-paper keys name outcomes or methods for coordinator matching; unassigned main-paper pages were not read.

## Prospective relationships

### SP3-N001 — Allocation and sample size

[p163](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=163), pp186,188. Approximately 160 randomized participants. Allocation 3:1 active:placebo, explicitly 120:40. Active participants equally split: 60 at 30 mg/day and 60 at 60 mg/day. Approximately 60 US centers is an administrative detail. Matching key: randomized count and dose allocation.

### SP3-S001 — Enrollment stopping

[p163](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=163). Enrollment stops when predefined regimen futility criteria are met or target randomization reached. No futility probability threshold appears on this page. Matching key: stopping rule.

### SP3-N002 — Treatment and follow-up duration

[p163](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=163), pp164,188. Maximum placebo-controlled treatment 24 weeks. Screening 6 weeks, safety follow-up4 weeks, total up to 34 weeks/about 8 months and approximately 10 visits. Follow-up call 28 days after last dose unless entering OLE. Matching key: randomized intervention duration and outcome horizon.

### SP3-N003 — Placebo-controlled visit windows

[p164](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=164), pp165–166. Master screening −42 to −1 days; regimen screening −41 to 0; baseline day 0; W 2 day 14±3; W 4 day 28±7; W 8 day 56±7; W 12 day 84±3; W 16 day 112±7; W 20 day 140±3; W 24/early termination day 168±7. Follow-up28±3 days after last dose. Maximum interval between visits 64 days. Matching key: endpoint observation windows.

### SP3-N004 — Assessment schedule

[p164](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=164), pp165–166. ALSFRS-R at screening, baseline, W 4,W 8,W 12,W 16,W 20,W 24. SVC at screening, baseline, W 8,W 16,W 24. Muscle strength at baseline,W 8,W 16,W 24. CNS-BFS at baseline,W 8,W 16,W 24. ALSAQ-40 schedule row at baseline,W 24. Voice at baseline,W 4,W 8,W 16,W 24 and twice weekly at home. ECG at screening,W 24. Safety labs at screening,baseline,W 4,W 8,W 16,W 24. Matching key: outcome trajectories and PRO schedules.

### SP3-S002 — Vital-status definition and ascertainment

[p166](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=166), footnote 13. Vital status means date of death/death equivalent or last known alive. Determine for every randomized participant at end of placebo-controlled follow-up, generally W 24; if alive then, ascertain again at regimen last patient last visit. Later public-source ascertainment is allowed under master §8.15. Matching key: survival definition and follow-up after week 24.

### SP3-N005 — Sampling and screening adaptations

[p166](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=166), footnotes 12,15,18. Predose whole blood/plasma at baseline,W 24; predose plasma at W 4,W 8. Optional CSF collection at W 16 may move to W 24 for logistics. Pandemic screening eligibility may use FVC measured by pulmonary lab or approved home spirometer, or sustained phonation. Matching key: biomarker sampling and respiratory eligibility.

### SP3-S003 — Primary efficacy endpoint/model

[p184](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=184). Primary objective: CNM-Au8 versus placebo on ALS progression. Primary endpoint: change in ALSFRS-R total score using a Bayesian repeated-measures model accounting for loss to follow-up due to mortality. Matching key: primary functional/survival analysis and model.

### SP3-S004 — Secondary outcome status

[p184](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=184). Secondary efficacy endpoints are respiratory function change by SVC; muscle-strength change by isometric HHD and grip strength; survival. These are printed as secondary endpoints. Matching key: secondary endpoint hierarchy.

### SP3-S005 — Safety outcome status

[p184](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=184). Safety endpoints: treatment-emergent adverse and serious adverse events; laboratory changes and treatment-emergent clinically significant abnormalities; ECG changes and treatment-emergent clinically significant abnormalities; suicidal ideation and behavior. Matching key: safety definitions and grouping.

### SP3-S006 — Exploratory outcome status and threshold

[p184](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=184), p185. Exploratory efficacy endpoints: quantitative voice changes; active-versus-placebo difference in proportion experiencing ≥6-point ALSFRS-R decline from baseline to W 24; neurodegeneration biofluid biomarkers; patient-reported outcomes; respiratory change by home spirometry. No death component appears in the printed ≥6-point endpoint definition here. Matching key: responder threshold, composite components, PRO/voice/biomarker hierarchy.

### SP3-N006 — Intervention and eligibility

[p186](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=186), pp188–191. Multicenter randomized placebo-controlled trial of oral daily 30 mg or 60 mg CNM-Au8 versus color-matched placebo. Riluzole and edaravone permitted concomitantly. Master eligibility applies; additional regimen exclusion is allergy to gold, gold salts or colloidal gold. Double-blind treatment approximately 24 weeks. Matching key: intervention and eligible population.

### SP3-N007 — Dose, composition and administration

[p189](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=189), pp171,190–191. Table 2: 30 mg arm=250μg/mL×60 mL×2 bottles/day; 60 mg arm=500μg/mL×60 mL×2; placebo=2×60 mL. All daily volume 120 mL, oral once daily at same time±1 hour, at least 30 min before food. Table 3 per 60 mL bottle: NaHCO 3 32.8 mg; Au 15 mg or 30 mg. OLE 120 mL bottle: NaHCO 3 65.5 mg, Au 30 mg. Gastric tube administration allowed, with 20–30 mL water flush before/after. Matching key: randomized dose and administration.

### SP3-N008 — Dose changes and OLE version distinction

[p192](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=192). Tolerability-related reduction to one bottle/day only with medical monitor approval; two-bottle rechallenge may be approved; remain at one bottle if rechallenge not tolerated; no drug holidays. OLE initially maintains blinded active dose, with former placebo participants re-randomized to 30 mg or 60 mg. After topline blinded-phase results, OLE dose adjusted to 30 mg following Clene/sponsor consultation; original dose assignment remains blinded. Matching key: dose adaptation and OLE versus randomized phase.

### SP3-S007 — Compliance/per-protocol rule

[p196](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=196). Overall treatment compliance for per-protocol analysis set should be 80%–120% of planned dose. Bottle counts at clinic visits; compliance checks during phone visits. Noncompliance may lead to discontinuation after investigator/monitor consultation. Matching key: per-protocol population rule.

### SP3-S008 — Completion, withdrawal and OLE eligibility

[p186](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=186), p203. Placebo-controlled participation ends after planned visits on/off drug, early termination plus safety call, or consent withdrawal/loss to follow-up. Drug discontinuation with continued protocol participation does not require early-termination visit/safety call. OLE eligibility described as completion of placebo-controlled trial on drug. OLE runs until primary 24 week results available or support/development terminated. Matching key: follow-up population and OLE eligibility.

### SP3-N009 — OLE observation windows

[p167](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=167), pp204–207. OLE schedule days 14+3,28±7,56±7,84±3,112±7,140±3,168±3,196±14, then every 12 weeks±14 days; safety call 28±7 days after last dose. Narrative p204 prints W 2=14±3 and W 4=28±10; p205 W 8=56±7,W 12=84±3; p206 W 16=112±7,W 20=140±3,W 24=168±3; p207 W 28=196±14. These location-specific windows are preserved without diagnosis. Matching key: OLE timepoints, separate from randomized outcomes.

### SP3-N010 — OLE assessments and maximum intervals

[p168](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=168), pp191,204–207. Maximum visit interval 64 days through W 16,96 days thereafter. OLE biomarkers atW 16,W 28,W 52, regimen-specific collection every 24 weeks thereafter. ALSAQ-40 atW 28 and every 24 weeks thereafter. ALSFRS-R atW 4,W 8,W 12,W 16,W 20,W 24,W 28/Q 12; SVC/home spirometry atW 4,W 8,W 16,W 28/Q 12; CNS-BFS atW 8,W 16,W 28/Q 12. Matching key: OLE assessment schedule.

### SP3-N011 — Narrative regimen visits

[p201](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=201), pp200–203. Baseline day 0 includes ALSAQ-40,CNS-BFS,home spirometry,voice and PK/PD. W 4/W 8 voice and plasmaPK, home spirometry/CNS-BFS only W 8. W 16 includes ALSAQ-40,home spirometry,CNS-BFS,voice. W 24/early termination includes PROs,home spirometry,voice,whole-bloodPK/PD,plasmaPD,urinePD. No regimen-specific procedures at W 2,W 12,W 20 phone visits. Safety call 28±3 days after last dose. Matching key: PRO/sampling schedule.

### SP3-N012 — Laboratory alerts

[p198](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=198). ALT/AST>3×ULN; creatinine>1.5×baseline; platelet count<75,000/mm³. Alerts informative only, without mandatory dose reduction/discontinuation. Investigator determines follow-up/management. Matching key: safety assessment definitions.

### SP3-S009 — Remote-visit adaptations and missing procedures

[p199](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=199), p204. Remote W 4,W 8,W 16 permitted for pandemic/other safety needs. Voice remotely; home spirometry/CNS-BFS atW 8,W 16. No home-health PK/PD blood collection; record missing procedures. OLE remote options includeW 4,W 8,W 16,W 28,W 40; no remote blood/urine PK/PD. Matching key: remote assessments/missing data context.

### SP3-N013 — Assessment instruments

[p208](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=208), p209. Voice twice weekly:5 fixed and 5 random sentences, consonant-vowel sequence, sustained phonation, single-breath counting. English-only app, no caregiver language assistance. ALSAQ-40 has 40 self-report questions; CNS-BFS has 21 questions in 3 domains (swallowing,speech,salivation); caregiver help allowed with both. Home FVC uses MIR Spirobank Smart with video/phone coaching and 3–5 maneuvers. Matching key: voice/PRO/respiratory methods.

### SP3-S010 — PK/PD analyses and first 40 review

[p210](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=210), p211. Predose whole-blood Au PK, separate PK analysis plan. Riluzole population PK under separate plan: first 40 participants taking riluzole randomized toRegimenC and reachingW 8 reviewed by DSMB/unblinded PK designee for CNM-Au8-versus-placebo changes atW 4/W 8. Predose plasma/whole blood/urine PD; separate PD analysis plan. Matching key: PK interim review and biomarker plans.

### SP3-S011 — Statistical design and success interim

[p212](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=212). Regimen follows default master AppendixI design with one deviation: no interim analyses for early success. Operating characteristics quantified by clinical-trial simulation; details in regimen SAP. No power or decision-threshold numbers printed in this shard. Matching key: success interim and operating characteristics.

### SP3-S012 — Shared controls

[p212](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=212). Primary analysis includes sharing all controls from other regimens, justified by minor eligibility differences and no expected systematic primary-endpoint differences. No borrowing-weight formula appears here. Matching key: primary control population.

### SP3-N014 — ALSAQ-40 questionnaire

[p213](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=213), pp214–221. Recall last 2 weeks;40 numbered items; one choice per question, Never/Rarely/Sometimes/Often/Always. Functional items add “cannot perform” to Always. No numeric score conversion, missing-item rule or formula printed. Page item ranges: p214 items 1–5 walking/falls/balance; p215 items 6–10 walking pain/stairs/standing/transfers; p216 items 11–15 arm-hand use/bed turning/objects/books/writing; p217 items 16–20 housework/feeding/grooming/dressing/washing; p218 items 21–25 swallowing/solids/liquids/conversation/comprehensibility; p219 items 26–30 stuttering/speaking/less speech/frustration/self-consciousness; p220 items 31–35 loneliness/boredom/embarrassment/hopelessness/burden; p221 items 36–40 continuing/anger/depression/future/independence. Matching key: PRO scale/recall.

### SP3-N015 — CNS-BFS scale

[p222](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=222), p223. Seven sialorrhea items, seven speech, seven swallowing. Responses 1=Does not apply,2=Rarely,3=Occasionally,4=Frequently,5=Most of the time; speech additionally 6=Unable to communicate by speaking. Separate 3 domain totals and overall score blanks; feeding-tube checkbox. Derived all-item total possible 21–112 from 7×5+7×6+7×5; this range is derived, not a printed normative range. No actual participant score. Matching key: PRO component scoring.

## Background quantities retained separately

### SP3-N016 — Particle characteristics

[p172](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=172), Table 1. Median diameter 13 nm; disc/spherical aspect 0.2/1.0; volume 2.3×10²/1.2×10³nm³; surface 3.2×10²/5.3×10²nm²; atoms 1.4×10⁴/6.8×10⁴; molecular weight 2.7×10³/1.3×10⁴kDa; total surface per mL 3.6×10²/1.2×10²cm²; particles per mL 1.1×10¹⁴/2.3×10¹³; particles per 60 mL 3.4×10¹⁵/6.8×10¹⁴. Narrative p171 gives 13,000–66,000 atoms and 100–500 trillion particles/mL at 500μg/mL. Not clinical trial results.

### SP3-N017 — Dose-justification tables and Figure 10

[p194](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=194), [p195](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=195). Table 4 human 60 kg doses 15/30/60/90 mg correspond to 9.3/18.5/37.0/55.5 mg/m². Rat 21 day NOAEL 40 mg/kg/day=240 mg/m², margins 25.9/13.0/6.5/4.3; canine 90 mg/kg/day=1800 mg/m², margins 194.6/97.3/48.6/32.4. Table 5 human 21 day AUC 32.3/41.4/50.3/66.0 ng·h/mL; rat 40 mg/kg/day AUC 106, ratios 3.3/2.6/2.1/1.6; canine 90 mg/kg/day AUC 596, ratios 18.5/14.4/11.8/9.0. Table 6 chronic rat 6 months 40 mg/kg/day AUC 209, ratios 6.5/5.0/4.2/3.2; canine 9 months 10 mg/kg/day AUC 440, ratios 13.6/10.6/8.7/6.7. Animal AUC footnote averages male/female end-of-study values. Figure 10 labels Day 21 whole-blood Au AUC 0–24 geometric means 30.6 rodent 10 mg/kg,32.3 human 15 mg,41.4 human 30 mg,50.3 human 60 mg,66.0 human 90 mg. These are background exposure comparisons.

### SP3-S013 — Historical mechanistic figures

[p174](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=174), pp175,177–180. Figure 1 NADH 26μM inNaHCO 3 5.7 mM,Au~3.4μg/mL; absorbance 339 nm over 0–30 min, CNM-Au8 versus NIST 10/30 nm; oxidation rate arbitrary units, no exact bar values. Figure 2 NAD+/NADH nM after 48 h: control,CNM-Au8 at 10 ng/mL,100 ng/mL,1μg/mL,10μg/mL,BDNF 50 ng/mL; *P<.05 versus control, one-way ANOVA+Dunnett. Crosshatched black rectangle below graphs onp175 is present in the reusable page image and does not transcribe hidden trial data.

Figure 4: SOD absorbance 450 nm cm⁻¹ at 20 minutes, arbitrary units/SEM; CNM-Au8 labels 1000,750,500,250,vehicle. ROS mean intensityAU over 0–50 seconds for control/buffer or buffer+rotenone and 0.3/1/3μg/mL, with asterisks. Figure 5: O 4 area per cell count, buffer/0.3/1/3μg/mL; ATPμM inMO 3.13 oligodendrocytes 72 h, mean±SEM, vehicle/CNM-Au8 at 0.1/0.32/1μg/mL; one-way ANOVA P<.05 caption.

Figure 6 A/B/D: CNM-Au8 48 h before+48 h after injury versus riluzole 1 h before+48 h after. Groups control,control+vehicle,CNM-Au8 100 ng/mL alone,glutamate 5μM,glutamate+CNM-Au8 10/32/100/316 ng/mL/1μg/mL,riluzole 1μM. Outcomes motor-neuron survival%controlMAP 2, neurite-network%controlMAP 2, eTDP 43 area per MN%control. *P<.05 versus glutamate, one-way ANOVA followed by FisherPLSD. Micrographs use 20μM glutamate with vehicle,CNM-Au8,BDNF. These are historical background studies, not clinical outcome relationships.

### SP3-S014 — Historical human-cell and murine results

[p181](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=181), pp182–183. Figure 7: Tuj 1,Isl 1/2,ChAT positive cells%control; no treatment,vehicle,riluzole,CNM-Au8 at 30/100/300 ng/mL; ***/**** without numerical definitions onpage 181. iPSC motor-neuron co-culture withSOD1A4V astrocytes 14 days. Narrative strain lifespans~157/~129 days as printed. Rapid strain N 15/group; onset P=.13 Mantel-Cox; brainstem atrophy P<.05 unpaired t-test. Slower strain N 20 female,10/group; dosing starts 4 weeks, weekly functional tests from 8 weeks, survival benefit through 22 weeks.

Figure 8: neuroscore 0–5 mean±SEM, P=.0074 two-way ANOVA; weights mean score±SEM,P<.01 two-way ANOVA; horizontal-bar mean score±SEM,P<.05 two-way ANOVA; wheel velocity km/day±SEM, overall and early(days 71–100),mid(101–130),late(131–160), *P<.05,***P<.001,****P<.0001 two-tailed t-test; middle period marked ns. Figure 9 KM survival% by days alive 120–180; Breslow-Wilcoxon P=.0302, HR.3730 CNM-Au8 versus vehicle. Figure heights are not converted into exact estimates. These studies are historical rationale, not trial outcomes.

## Complete page ledger

Every row is COMPLETE. N/A means inspected with no applicable trial quantitative relationship.

| PDF page | RSA page/version | Inspected content and local mapping |
|---:|---|---|
|153|70/71,v 3.0|Bibliography; N/A.|
|154|71/71,v 3.0|Bibliography; N/A.|
|155|1/75,v 6.0|Title, date/version identity.|
|156|2/75,v 6.0|Contents; no results.|
|157|3/75,v 6.0|Contents; no results.|
|158|4/75,v 6.0|Contents; no results.|
|159|5/75,v 6.0|Signature/administrative; N/A.|
|160|6/75,v 6.0|Abbreviations, AUC 0–24, units, FVC/ALSAQ definitions.|
|161|7/75,v 6.0|SVC/PK/PD/OLE definitions.|
|162|8/75,v 6.0|Rationale,30/60 mg doses; N 006.|
|163|9/75,v 6.0|Sample,allocation,duration,stopping; N 001–002,S 001.|
|164|10/75,v 6.0|Placebo-controlled schedule; N 003–004.|
|165|11/75,v 6.0|Schedule continued; N 003–004.|
|166|12/75,v 6.0|Schedule footnotes; N 005,S 002.|
|167|13/75,v 6.0|OLE schedule; N 009–010.|
|168|14/75,v 6.0|OLE schedule/footnotes; N 010.|
|169|15/75,v 6.0|Background incidence 1/100000,familial 5–10%; no trial result.|
|170|16/75,v 6.0|Mechanistic background; no trial result.|
|171|17/75,v 6.0|Background GWAS 12577 cases/23475 controls,dosing,particles; N 007,N 016.|
|172|18/75,v 6.0|Particle Table 1; N 016.|
|173|19/75,v 6.0|Background age groups 21–26,33–36,59–68 years; no trial result.|
|174|20/75,v 6.0|Historical Figure 1/Figure 2 heading; S 013.|
|175|21/75,v 6.0|Historical NAD graphs/crosshatched rectangle; S 013.|
|176|22/75,v 6.0|ROS background; no trial result.|
|177|23/75,v 6.0|Historical Figure 4; S 013.|
|178|24/75,v 6.0|Historical Figure 5/E 14 culture methods; S 013.|
|179|25/75,v 6.0|Historical Figure 6 A/B/micrographs; S 013.|
|180|26/75,v 6.0|Historical Figure 6 D and 14 day human-cell method; S 013–014.|
|181|27/75,v 6.0|Historical Figure 7/murine studies; S 014.|
|182|28/75,v 6.0|Historical Figure 8 A–E; S 014.|
|183|29/75,v 6.0|Historical Figure 9/background TDP 43>90%cases; S 014.|
|184|30/75,v 6.0|Primary/secondary/safety/exploratory status; S 003–006.|
|185|31/75,v 6.0|Exploratory PRO/home spirometry; S 006.|
|186|32/75,v 6.0|Allocation,placebo,concomitant therapy,completion; N 006,S 008.|
|187|33/75,v 6.0|Fresh native/render and direct visual inspection: blank body; N/A.|
|188|34/75,v 6.0|N 160,eligibility,24 weeks; N 001–002,N 006.|
|189|35/75,v 6.0|Dose Table 2/component Table 3; N 007.|
|190|36/75,v 6.0|Table 3/storage 15–25°C,excursions 2–60°C; N 007; operational.|
|191|37/75,v 6.0|Administration,20–30 mL flush,visit windows; N 007,N 010.|
|192|38/75,v 6.0|Dose reduction/OLE/background margins; N 008,N 017.|
|193|39/75,v 6.0|Background 90 mg minimum 4×rat margin; N 017.|
|194|40/75,v 6.0|Background Tables 4–5; N 017.|
|195|41/75,v 6.0|Background Table 6/Figure 10; N 017.|
|196|42/75,v 6.0|30/60 mg selection,80–120%compliance,overdose contact 24 h; S 007,N 006.|
|197|43/75,v 6.0|Background safety 10 mg/kg canine,40 mg/kg rat,90 mg/day human 21 days; N 017.|
|198|44/75,v 6.0|Lab alerts; N 012.|
|199|45/75,v 6.0|Remote-visit adaptations; S 009.|
|200|46/75,v 6.0|Consent/baseline; N 011.|
|201|47/75,v 6.0|W 2/4/8/12/16 visits; N 011.|
|202|48/75,v 6.0|W 20/W 24/early termination/safety call; N 011.|
|203|49/75,v 6.0|Early termination/OLE eligibility; S 008.|
|204|50/75,v 6.0|Remote OLE,W 2/W 4; N 009,S 009.|
|205|51/75,v 6.0|OLE W 8/W 12/W 16; N 009–010.|
|206|52/75,v 6.0|OLE W 16/W 20/W 24; N 009–010.|
|207|53/75,v 6.0|OLE W 28/Q 12; N 009–010.|
|208|54/75,v 6.0|Voice/ALSAQ/CNS-BFS definitions; N 013.|
|209|55/75,v 6.0|CNS-BFS/homeFVC 3–5 maneuvers; N 013.|
|210|56/75,v 6.0|PK/PD,first 40 riluzole users; S 010.|
|211|57/75,v 6.0|PD storage/separate plan; S 010.|
|212|58/75,v 6.0|Success interim,simulation,shared controls; S 011–012.|
|213|59/75,v 6.0|ALSAQ instructions/2 week recall; N 014.|
|214|60/75,v 6.0|ALSAQ items 1–5; N 014.|
|215|61/75,v 6.0|ALSAQ items 6–10; N 014.|
|216|62/75,v 6.0|ALSAQ items 11–15; N 014.|
|217|63/75,v 6.0|ALSAQ items 16–20; N 014.|
|218|64/75,v 6.0|ALSAQ items 21–25; N 014.|
|219|65/75,v 6.0|ALSAQ items 26–30; N 014.|
|220|66/75,v 6.0|ALSAQ items 31–35; N 014.|
|221|67/75,v 6.0|ALSAQ items 36–40; N 014.|
|222|68/75,v 6.0|CNS-BFS sialorrhea/speech; N 015.|
|223|69/75,v 6.0|CNS-BFS speech/swallowing/totals; N 015.|
|224|70/75,v 6.0|Bibliography; N/A.|
|225|71/75,v 6.0|Bibliography; N/A.|
|226|72/75,v 6.0|Bibliography; N/A.|
|227|73/75,v 6.0|Bibliography; N/A.|
|228|74/75,v 6.0|Bibliography; N/A.|
|229|75/75,v 6.0|Bibliography; N/A.|

## Handoff

COMPLETE:77 pages mapped;17 numeric relationships and 14 statistical/design relationships (12 prospective,2 historical background); zero scientific coverage gaps. Actual clinical result estimates, intervals and P values do not occur in this protocol shard. Formula/threshold details deferred by the source to master protocol/regimen SAP or separate PK/PD plans are named without diagnosis. No old scientific conclusions were used.
