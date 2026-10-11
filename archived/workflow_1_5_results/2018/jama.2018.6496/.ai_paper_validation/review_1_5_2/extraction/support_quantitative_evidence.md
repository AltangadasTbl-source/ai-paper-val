# Support-source quantitative evidence mapping

## Scope and method

Fresh, source-first mapping of `DOC-002` (`joi180054supp1_prod.pdf`, protocol, pages 1-25) and `DOC-003` (`joi180054supp2_prod.pdf`, supplementary online content, pages 1-13). Evidence was read from the new native and layout assets in `preprocessing/` and checked against the supplied PDF page locations. No prior audit derivative, candidate record, or final report was used. This is a candidate-free map: observations below are printed-source facts and relationship definitions, not adjudications.

Links use the supplied PDF and exact PDF page: [DOC-002](../../../joi180054supp1_prod.pdf#page=1) and [DOC-003](../../../joi180054supp2_prod.pdf#page=1).

## DOC-002 — protocol evidence units (25/25 pages)

| PDF page | Evidence unit and mapped result-relevant content |
|---:|---|
| [1](../../../joi180054supp1_prod.pdf#page=1) | Protocol title *Bougie use in Emergency Airway Management (BEAM)*; Phase IV; versions 1.0 (15 December 2015) and 1.1 (18 May 2016). Context only. |
| [2](../../../joi180054supp1_prod.pdf#page=2) | Contents: primary outcome page 8; secondary outcomes and measurement page 9-10; study design pages 11-12; population pages 13-16; procedures pages 17-18; planned statistics pages 19-21. Context/index only. |
| [3](../../../joi180054supp1_prod.pdf#page=3) | Contents identifies planned sample-size, analysis-population, outcome-analysis, missing-data, and interim-analysis sections. Context/index only. |
| [4](../../../joi180054supp1_prod.pdf#page=4) | Definitions: AE adverse event; DSMB data safety and monitoring board; ED; ETT endotracheal tube; GEB gum-elastic bougie; ITT intention-to-treat; SAE serious adverse event. |
| [5](../../../joi180054supp1_prod.pdf#page=5) | Background: first-pass success approximately 85%; GEB described as a 60- or 70-cm stylet with approximately 30-degree tip angle. These are cited external-background statements, not trial results. |
| [6](../../../joi180054supp1_prod.pdf#page=6) | Cited background: 99% success during 301 difficult intubations over 8 years; 199/200 GEB placements successful; randomized-study rescue within 45 seconds; another randomized difficult-view study reports GEB 96% versus stylet 66% after first two attempts. External background only. |
| [7](../../../joi180054supp1_prod.pdf#page=7) | Cited rescue-device success: 20/26 (76.9%) and 70/88 (79.6%) attempts; cited multicenter first-attempt GEB use 3.5%. External background only. |
| [8](../../../joi180054supp1_prod.pdf#page=8) | Proposed population: adults receiving ED orotracheal intubation with a Macintosh blade (video or direct) for any indication, randomized to GEB use on first attempt. Primary outcome named first-pass success. |
| [9](../../../joi180054supp1_prod.pdf#page=9) | **Primary definition:** ETT placed in trachea on first attempt. Attempt starts when laryngoscope enters mouth and ends when it leaves mouth or when operator switches from first tube device (ETT/GEB) to another even if blade remains. Secondary definitions: success without hypoxemia; hypoxemia = SpO2 <90%, or if baseline <90%, drop >10%, from first-attempt start to 1 minute after cuff inflation; time to intubation = start to cuff inflation with tube in trachea; esophageal intubation requires ETT in esophagus with ventilation then removal; hypoxemia as above. |
| [10](../../../joi180054supp1_prod.pdf#page=10) | Measurement: assistant and physician record number of attempts; video resolves discrepancies. SpO2 recorded at start and every 20 seconds through 1 minute after cuff inflation, plus nadir even off-interval; stopwatch records time; physician form records esophageal intubation. |
| [11](../../../joi180054supp1_prod.pdf#page=11) | Two-arm unblinded single-center design; stated aim is >9% absolute difference. 1:1 allocation; permuted block sizes 2, 4, 6, 8, 10; two randomization strata: (1) cervical collar, obesity (gestalt), or apparent facial/neck trauma, versus (2) none. |
| [12](../../../joi180054supp1_prod.pdf#page=12) | If first device fails, second attempt may use any device/strategy. Participation ends 1 minute after successful intubation; no further data/EMR collection. |
| [13](../../../joi180054supp1_prod.pdf#page=13) | Primary analysis subgroup = any difficult-airway characteristic; all enrolled patients secondary analysis. Listed characteristics: cervical immobility, obesity, large tongue, short neck, small mandible, facial/neck trauma, airway edema, blood/vomit in airway. Inclusion age presumed >=18; exclusions include upper-airway/perilaryngeal distortion, prisoner/arrest, known/suspected pregnancy. |
| [14](../../../joi180054supp1_prod.pdf#page=14) | Consent/administrative context. Residents perform approximately 98% of ED intubations. |
| [15](../../../joi180054supp1_prod.pdf#page=15) | Consent/representativeness narrative; no trial result. |
| [16](../../../joi180054supp1_prod.pdf#page=16) | Objection prevents enrollment; study complete 1 minute after successful intubation. |
| [17](../../../joi180054supp1_prod.pdf#page=17) | Baseline vital signs immediately after randomization; difficult-airway characteristics and attempt data on structured form; second attempt after failed initial device. |
| [18](../../../joi180054supp1_prod.pdf#page=18) | AE monitoring continuously in ED; related severe/unexpected/life-threatening/fatal SAE notification generally within 24 hours; DSMB assessment within 5 working days. |
| [19](../../../joi180054supp1_prod.pdf#page=19) | Planned summaries: categorical n (%), including missing category as needed; continuous n, mean, median, SD, min, max; time-to-event Kaplan-Meier 25th/50th/75th percentiles with two-sided 95% CI and censored percentage. Formal tests for primary/key secondary at two-sided alpha .05. Sample calculation: GEB 95%, non-GEB 86%, absolute difference 9%, 80% power, 374 (187/group) difficult-airway patients; annual intubations approximately 1500; planned enrolled total 1000, expected difficult airway 30-40%, 1 calendar year or 1000 enrollment first. Command: `sampsi 0.95 0.86, p(0.8)`. |
| [20](../../../joi180054supp1_prod.pdf#page=20) | ITT primary population: randomized, intubated patients, excluding non-Macintosh device; no-attempt patients are screening failures. Primary analysis is difficult-airway subset; all enrolled presented secondarily. Primary comparison uses chi-square. Secondary categorical/continuous outcomes use appropriate CI of between-group difference, stratified by difficult-airway presence. Missing primary/secondary values: video review, otherwise exclusion from relevant analysis. |
| [21](../../../joi180054supp1_prod.pdf#page=21) | Interim after 500 enrolled, primary outcome only; early stop only futility. Sensitivity analysis assumes total n=1000 equal allocation, non-GEB rate unchanged in latter half, GEB rate 15% absolute higher (capped at 100%); stop if no first-pass difference. |
| [22](../../../joi180054supp1_prod.pdf#page=22) | Administrative monitoring: SAE assessment within five working days; no trial results. |
| [23](../../../joi180054supp1_prod.pdf#page=23) | References 1-13; bibliographic context only. |
| [24](../../../joi180054supp1_prod.pdf#page=24) | References 14-25; bibliographic context only. |
| [25](../../../joi180054supp1_prod.pdf#page=25) | References 26-34; bibliographic context only. |

## DOC-003 — supplement evidence units (13/13 pages)

| PDF page | Evidence unit and mapped result-relevant content |
|---:|---|
| [1](../../../joi180054supp2_prod.pdf#page=1) | Index: eTable 1 (physician-clustered outcome analysis), eFigure 1 (first-attempt duration), eFigure 2 (bevel maneuver), eAppendix 1 (interim), eAppendix 2 (postintubation form). |
| [2](../../../joi180054supp2_prod.pdf#page=2) | **eTable 1.** Clustered-by-physician analysis. Primary, difficult-airway N=380: Bougie N=381, 191/198 (96%; 95% CI 93-99); ETT N=376, 150/182 (82%; 76-88); difference 14% (7-21%); P<.001; interaction P=.35. Secondary difficult-airway N=380: success without hypoxemia 156/191 (82%; 76-87) vs 123/177 (69%; 63-76), difference 12% (2-22%), P=.015, interaction .61; first-attempt duration median (IQR) 39 s (29-52) vs 40 s (27-63), difference -1 s (-6 to 3), P=.31, interaction .17. All patients N=757: overall first success 373 (98%; 96-99) vs 328 (87%; 83-90), difference 11% (6-15), P<.001, interaction n/a; success without hypoxemia 317/371 (85%; 81-89) vs 282/366 (77%; 72-81), difference 8% (2-15), P=.02; duration 38 s (29-51) vs 36 s (25-54), difference 1 s (-1 to 4), P=.95. |
| [3](../../../joi180054supp2_prod.pdf#page=3) | eTable footnotes: values n (%; 95% CI) except duration; difference is proportion or median with 95% CI; interaction n/a for all-patient analyses. Bougie/ETT columns unchanged; differences/P/interaction recalculated for physician clustering. ICC <.001 (95% CI <.001 to .03), upper CI bound used. Hypoxemia definition and realtime recording; valid waveform unavailable for all patients. **Supplement duration definition:** time from laryngoscope blade entering mouth to blade removal. |
| [4](../../../joi180054supp2_prod.pdf#page=4) | eFigure 1: Kaplan-Meier time until successful intubation, all patients. Hazard ratio for first-attempt success, Bougie versus ETT+stylet reference = 1.12 (95% CI 0.97-1.30). Vertical ticks mark one or more failed attempts; proportional-hazards assumption not upheld. |
| [5](../../../joi180054supp2_prod.pdf#page=5) | eFigure 2 procedural illustration: if arytenoid resistance, withdraw ETT 1-2 cm, rotate 90 degrees counterclockwise, then readvance. No comparative outcome value. |
| [6](../../../joi180054supp2_prod.pdf#page=6) | Interim protocol quoted: analysis after 500; total projection n=1000 equal allocation; non-GEB unchanged, GEB +15% absolute/capped 100%; futility if no difference. Observed after 507 enrolled: Bougie 250/257 (97%), ETT+stylet 213/250 (85%); trial not stopped for futility. |
| [7](../../../joi180054supp2_prod.pdf#page=7) | Data-form variables: prehospital attempt yes/no; intubator level; mutually exclusive one best medical or trauma indication categories; trauma blunt/penetrating. Definitions/fields, no aggregate result. |
| [8](../../../joi180054supp2_prod.pdf#page=8) | Data form: preoxygenation level coded 0-9; oxygen flow <=15 LPM or flush rate; head-of-bed >=30 degrees yes/no; nasal cannula during attempts yes/no. Definitions/fields, no aggregate result. |
| [9](../../../joi180054supp2_prod.pdf#page=9) | Data form: sedative, paralytic, order, position; difficult-characteristic check-all fields (blood/vomit, short neck, cervical immobilization, small mandible, obesity, obstruction/edema, facial trauma, large tongue). Definitions/fields, no aggregate result. |
| [10](../../../joi180054supp2_prod.pdf#page=10) | Attempt 1 begins blade insertion and ends blade removal. Device/video-screen/first-passed fields; success/switch options distinguish ETT passed over bougie from true switch. Definitions/fields. |
| [11](../../../joi180054supp2_prod.pdf#page=11) | Attempt-1 condition and direct/video fields; attempt-2 start/end definition and device/first-passed fields. Definitions/fields. |
| [12](../../../joi180054supp2_prod.pdf#page=12) | Attempt-2 success/switch; subsequent course; bougie clicks/hard-stop; arytenoid resistance responses; ETT confirmation fields. Definitions/fields. |
| [13](../../../joi180054supp2_prod.pdf#page=13) | Complication fields: airway injury, aspiration, cardiac arrest during/within 5 min, cardiac arrest/death in ED, bleeding, pharyngeal/dental/lip injury, esophageal intubation. Definitions/fields. |

## Provisional numeric/reporting relationship register

| ID | Relationship, exact scope, and mapping observation |
|---|---|
| UN001 | Primary endpoint key: first-attempt success is ETT in trachea on first attempt; compare protocol page 9 and data-form page 10. Main-paper matching key: first-attempt success. |
| UN002 | Attempt-boundary key: protocol page 9 ends on blade removal **or** device switch; data-form pages 10-11 defines blade insertion/removal. Both locations are retained because the device-switch rule is material to first-attempt classification. |
| UN003 | Hypoxemia key: SpO2 <90%, or baseline <90% then >10% absolute decrease; window to 1 minute after cuff inflation (protocol pp.9-10) / during or within 1 minute after completion (supplement p.3). Main-paper matching key: success without hypoxemia. |
| UN004 | Duration key: protocol = attempt beginning to cuff inflation with tracheal tube (p.9); supplement = blade entering to blade removal (p.3); table medians use supplement definition. Main-paper matching key: first-attempt duration. |
| UN005 | Primary eTable arithmetic: 191/198 displayed 96% and 150/182 displayed 82%; difference 14% with CI 7-21 (DOC-003 p.2). |
| UN006 | Primary denominators: difficult-airway N=380, while treatment-column headers N=381/376 are randomization totals; 198+182=380 (DOC-003 p.2). Population/time/contrast must be matched before any cross-location comparison. |
| UN007 | Difficult-airway success-without-hypoxemia: 156/191=82% and 123/177=69%; displayed difference 12% (2-22) (DOC-003 p.2). |
| UN008 | Difficult-airway duration: medians 39 versus 40 s; displayed difference -1 s (CI -6 to 3); IQRs 29-52 and 27-63 s (DOC-003 p.2). |
| UN009 | All-patient success: 373 and 328 displayed as 98% and 87%; difference 11% (6-15); total 373+? is not a denominator because entries are counts with percentages and are not slash fractions (DOC-003 p.2). |
| UN010 | All-patient success-without-hypoxemia: 317/371=85%, 282/366=77%, difference 8% (2-15) (DOC-003 p.2). |
| UN011 | All-patient duration: 38 versus 36 s, difference 1 s (CI -1 to 4), IQRs 29-51 and 25-54 s (DOC-003 p.2). |
| UN012 | Interim result: after 507, 250/257=97% versus 213/250=85%, an observed rounded percentage contrast of 12 points (DOC-003 p.6); matched scope is interim/all enrolled, not final difficult-airway primary outcome. |
| UN013 | Protocol sample-size/planning identity: 95%-86%=9%; 374=187+187; planned all-enrolled cap 1000 and predicted difficult-airway proportion 30-40% (DOC-002 p.19). |
| UN014 | Randomization identity: 1:1 allocation, blocks 2/4/6/8/10, two strata; compare realized analysis denominators only after accounting for eligibility and analysis-population definitions (DOC-002 pp.11,20). |
| UN015 | Procedure/risk metric: eFigure 2 uses distance 1-2 cm and rotation 90 degrees; distinct from any intubation duration measure (DOC-003 p.5). |

## Provisional inferential-statistical relationship register

| ID | Relationship, exact scope, and mapping observation |
|---|---|
| US001 | Primary clustered result: difference 14% (95% CI 7-21), P<.001, interaction P=.35; difficult-airway subgroup (DOC-003 p.2). |
| US002 | Secondary clustered success-without-hypoxemia: 12% (2-22), P=.015, interaction P=.61; difficult-airway subgroup (DOC-003 p.2). |
| US003 | Secondary clustered duration: median difference -1 s (-6 to 3), P=.31, interaction P=.17; difficult-airway subgroup (DOC-003 p.2). |
| US004 | All-patient clustered success: difference 11% (6-15), P<.001; interaction n/a because not subgroup analysis (DOC-003 pp.2-3). Displayed `<0.001` is not a display-zero issue. |
| US005 | All-patient clustered success-without-hypoxemia: 8% (2-15), P=.02; interaction n/a (DOC-003 p.2). |
| US006 | All-patient clustered duration: 1 s (-1 to 4), P=.95; interaction n/a (DOC-003 p.2). |
| US007 | Physician-cluster adjustment definition: only Difference/P/interaction recalculated; columns unchanged; ICC <.001 (CI <.001-.03), upper CI bound used (DOC-003 p.3). |
| US008 | Kaplan-Meier result: HR 1.12 (95% CI .97-1.30), ETT+stylet reference; proportional-hazards assumption not upheld (DOC-003 p.4). |
| US009 | Formal-analysis plan: primary/key secondary tests two-sided alpha .05; categorical/continuous summaries specified; time-to-event uses Kaplan-Meier percentile estimates/two-sided 95% CI (DOC-002 p.19). |
| US010 | Primary planned analysis: chi-square; difficult-airway primary and all-enrolled secondary (DOC-002 p.20). |
| US011 | Sample-size assumptions: 95% vs 86%, absolute 9%, 80% power, n=374, STATA `sampsi 0.95 0.86, p(0.8)` (DOC-002 p.19). |
| US012 | Interim decision rule: after n=500, sensitivity projection to n=1000 equal allocation, +15% absolute GEB assumption capped 100%, stop for futility if no difference (DOC-002 p.21; DOC-003 p.6). |
| US013 | Interim observed outcome and decision: n=507; 250/257 vs 213/250; protocol-stated futility rule reported as not met (DOC-003 p.6). |

## Mapping limitations

DOC-002 is a protocol: its cited prior-study values are background and its analysis statements are planned rather than observed trial results. DOC-003 page 4 graph coordinates are not natively tabulated; its caption supplies the HR/CI and proportional-hazards statement, which were mapped. The source assets were usable; no OCR was needed. No candidate diagnosis or external comparison was performed in this mapping stage.
