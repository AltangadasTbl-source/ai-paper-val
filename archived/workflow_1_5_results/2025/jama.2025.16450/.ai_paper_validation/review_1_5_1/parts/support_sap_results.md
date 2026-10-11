# Support Evidence Mapping: SAP and Results Supplement (support-004)

## Scope, identity, and methods

| Source | Direct file | PDF pages | SHA-256 | Mapping method | Status |
|---|---|---:|---|---|---|
| DOC-004 | `joi250072supp3_prod_1761000786.6988.pdf` | 48 | `9f981e26f7519c53d2a0641edf01b560618a67bc1d4ac456a5466d40346b929a` | Fresh `pdftotext` native and layout extraction for every page; targeted rendered-page review where readable | COMPLETE coverage record; see extraction limitation |
| DOC-005 | `joi250072supp4_prod_1761000786.6988.pdf` | 16 | `dacea759a76a4ee3ebaf648df46529a630d5be5c9aed85c5709fba8e12c5887b` | Reusable per-page native text, confirmed against direct PDF and fresh direct layout text | COMPLETE |

Fresh DOC-004 native/layout outputs are retained in `preprocessing/sap_results/doc004_sap_native.txt` and `preprocessing/sap_results/doc004_sap_layout.txt`. Direct DOC-005 layout output is `preprocessing/sap_results/doc005_results_direct_layout.txt`; direct page text is in `preprocessing/sap_results/results_pages/`.

**DOC-004 extraction limitation.** The direct PDF has 48 pages, but its embedded font encoding produces non-semantic text in both native and layout extraction. CPU Tesseract was attempted on rendered source pages; it produced empty output in this runtime. Rendered source pages were retained under `preprocessing/sap_results/sap_pages/`. Consequently, this record separates directly visually confirmed SAP content from pages for which only a no-applicable/encoding-limited coverage record can truthfully be made. No old AI candidate/checker/report material was read.

## Page-by-page coverage

| Source/page(s) | Coverage result |
|---|---|
| DOC-004 pp. 1-7 | Administrative front matter, revision/change-log and contents. No result values mapped; direct text encoding unreadable. |
| DOC-004 p. 8 | Background and protocol history: planned intervention 2.5 mL/kg surfactant plus 1.0 mL/kg budesonide versus 2.5 mL/kg surfactant; 22 0/7 to 28 6/7 weeks or birthweight <1000 g; primary composite BPD/death at 36 weeks PMA; 1:1 allocation and 15 centres. `SAP-N001`, `SAP-S001`. |
| DOC-004 p. 9 | Objectives/outcomes: primary efficacy objective and secondary-outcome definitions. `SAP-N002`, `SAP-S002`. |
| DOC-004 p. 10 | Primary outcome; secondary and exploratory endpoint definitions, including BPD support categories and 2-year NDI thresholds. `SAP-N003`, `SAP-S003`. |
| DOC-004 pp. 11-14 | Outcome/safety definitions, including 7-day/168-hour usual AE window, 30-day window for SIP/PVL, and 120-day clinical-outcome window. Directly visual review of p.13 confirmed 72-hour and DOL 5-7 intracranial-haemorrhage timing, DOL 28 PVL assessment, and 30-day SIP/PVL definition. `SAP-N004`, `SAP-S004`. |
| DOC-004 p. 15 | Treatment and eligibility timing: first dose within 48+2 h; randomization/decision <=48 h; maximum two doses; AE monitoring 7 days/168 h and SIP/PVL 30 days; primary at 36 weeks PMA; follow-up 22-26 months adjusted age. Inclusion: 22 0/7-28 6/7 weeks or 401-1000 g, <=48 h PNA (dose to 50 h). `SAP-N005`, `SAP-S005`. |
| DOC-004 pp. 16-48 | All pages were freshly extracted and assigned. Embedded text is unreadable and rendered/OCR text unavailable in this runtime; no additional result-relevant relationship can be transcribed without inventing content. Retained as explicit encoding-limited coverage records, not assumed empty. |
| DOC-005 p. 1 | Supplement title and eTable inventory; no result values. |
| DOC-005 p. 2 | eTable 1 analysis populations/disposition. `RES-N001`. |
| DOC-005 pp. 3-4 | eTable 2 exposure/compliance. `RES-N002`. |
| DOC-005 pp. 5-6 | eTable 3 participant-level AE/SAE experience and effect estimates. `RES-N003`; `RES-S001`-`RES-S003`. |
| DOC-005 pp. 7-8 | eTable 4 clinical/growth outcomes and analysis definitions. `RES-N004`; `RES-S004`. |
| DOC-005 pp. 9-10 | eTable 5 protocol deviations/violations. `RES-N005`. |
| DOC-005 pp. 11-12 | eTable 6 event-frequency AE summary. `RES-N006`. |
| DOC-005 pp. 13-14 | eTable 7 event-frequency SAE summary. `RES-N007`. |
| DOC-005 pp. 15-16 | eTable 8 in-hospital deaths/cause-of-death counts. `RES-N008`. |

## SAP relationships and matching keys

| Provisional ID | Exact source | Relationship / definition | Cross-source match key |
|---|---|---|---|
| SAP-N001 | DOC-004 p.8 | Planned intervention: surfactant 2.5 mL/kg + budesonide 1.0 mL/kg vs surfactant 2.5 mL/kg; 1:1 allocation; primary composite physiologic BPD or death by 36 weeks PMA. | `POP=extremely preterm; ARM=BUD+SF vs SF; OUTCOME=BPD/death; TIME=36w PMA` |
| SAP-S001 | DOC-004 p.8 | Site is incorporated by stratification and covariate adjustment; 15 centres planned. | `MODEL=site adjustment; RANDOMIZATION=1:1` |
| SAP-N002 | DOC-004 p.9 | Primary objective: early intratracheal combination within 50 h of birth reduces physiologic BPD/death at 36w PMA; secondary outcomes include death, BPD severity, postnatal steroids, and 2-year NDI/death. | `OUTCOME=BPD/death; TIME=36w PMA or 22-26mo CA` |
| SAP-S002 | DOC-004 p.9 | BPD severity is classified by support: room air; nasal cannula <=2 L/min; nasal cannula >2 L/min/noninvasive pressure; invasive ventilation. | `SCALE=Jensen 2019 BPD severity; TIME=36w PMA` |
| SAP-N003 | DOC-004 p.10 | Primary endpoint is physiologic BPD/death at 36w PMA in all randomized infants; secondary endpoint definitions include severe NDI: BSID-IV cognitive or motor composite <70, GMFCS 4-5, severe hearing impairment, or bilateral severe visual impairment. | `POP=all randomized; OUTCOME=BPD/death; TIME=36w PMA` |
| SAP-S003 | DOC-004 p.10 | Severe NDI/death follow-up is planned at 22-26 months corrected age. | `OUTCOME=NDI/death; TIME=22-26mo CA` |
| SAP-N004 | DOC-004 pp.11-14 | Prespecified safety timing: usual AEs through 7 days/168 h after final dose; SIP/PVL through 30 days; clinical outcomes include in-hospital death before 120 days chronological age. | `POP=safety; TIME=168h/720h/120d` |
| SAP-S004 | DOC-004 p.13 | ICH usually occurs in first 72 h (90% by 72 h), routine head ultrasound DOL 5-7 with 3-day grace; PVL usually DOL 28. | `OUTCOME=ICH/PVL; WINDOW=DOL` |
| SAP-N005 | DOC-004 p.15 | Dosing/eligibility values: first dose within 48+2 h, decision/randomization <=48 h, dose may be given to 50 h; max 2 doses; eligibility 22 0/7-28 6/7 weeks or 401-1000 g. | `POP=eligible randomized; EXPOSURE=dosing window` |
| SAP-S005 | DOC-004 p.15 | Planned follow-up/endpoints distinguish 36w PMA primary assessment from 22-26 month adjusted-age follow-up. | `TIME=36w PMA vs 22-26mo CA` |

## DOC-005 numeric relationship inventory

### RES-N001 — eTable 1, analysis populations and disposition (p.2)

ITT n=641; ITT excluding untreated n=635; safety n=635; per-protocol n=617. Treated: 635/641 (99.1%), 635/635 (100.0%), 635/635 (100.0%), 617/617 (100.0%). Treatment-arm counts, respectively: BUD+SF 323/320/322/309 and SF alone 318/315/313/308. Primary-endpoint status completed: 639 (99.7%), 634 (99.8%), 634 (99.8%), 617 (100.0%); ended early: 2 (0.3%), 1 (0.2%), 1 (0.2%), 0. GDB status discharged/still hospital/transferred/death: ITT 340/189/16/86; untreated-excluded 337/189/16/86; safety 337/189/16/86; PP 329/184/15/84. Population labels: ITT randomized/as randomized; safety received >=1 dose/as treated; PP received >=1 dose without major violations/as treated. Match key: `POP=ITT/SAF/PP; ARM=as randomized/as treated; TIME=36w PMA or 120d PNA`.

### RES-N002 — eTable 2, exposure and compliance (pp.3-4)

Safety BUD+SF/SF n=322/313. One/two doses: 220 (68.3%)/102 (31.7%) vs 195 (62.3%)/118 (37.7%). Dose-1 PNA hours mean(SD) 4.05(7.47)/3.70(6.80), median(Q1-Q3) 1.7(0.5-3.6)/1.6(0.6-3.3), range 0.0-48.4/0.0-49.2. Dose-2 n=102/118: mean 23.09(11.81)/21.98(10.12), median 17.8(13.7-29.7)/18.6(14.3-25.9), range 7.6-59.9/9.5-49.4. Not treated per protocol 36(11.2%)/29(9.3%): assignment violation 3/1, volume 31/27, administration 2/1. Surfactant compliance dose 1 mean 99.35(5.22)/100.03(4.73), dose 2 102.12(14.71)/101.70(10.67); budesonide dose-1 n=319 mean 102.29(24.06), dose-2 n=102 mean 99.76(7.83). Compliance is administered/expected dose x100; compliant window 90%-110%; surfactant protocol 2.5 mL/kg dose 1, 1.25 mL/kg dose 2; budesonide 1 mL/kg each dose. Match key: `POP=SAF; EXPOSURE=dose 1/2; UNIT=h or %; ARM=as treated`.

### RES-N003 — eTable 3, AE/SAE participant experience (pp.5-6)

Safety n=322/313. Any AE 242(75.4%)/202(64.5%), RR 1.16 (1.05,1.28); any AE of interest 240(74.8%)/193(61.7%), 1.20 (1.09,1.33). Category counts/percent/RR: ET blockage 3(0.9)/4(1.3), 0.73(0.16,3.28); hypoxemia+bradycardia 2(0.6)/3(1.0), 0.65(0.11,3.90); air leak 16(5.0)/18(5.8), 0.86(0.45,1.66); hypotension 56(17.4)/59(18.8), 0.92(0.67,1.27); hypertension 28(8.7)/21(6.7), 1.28(0.75,2.10); hyperglycemia 214(66.7)/156(49.8), 1.33(1.17,1.51); ICH 40(12.5)/37(11.8), 1.03(0.69,1.54); early/late sepsis 9(2.8)/8(2.6), 1.06(0.41,2.75), and 70(22.4)/70(23.7), 0.93(0.70,1.24); PVL 15(4.8)/13(4.3), 1.09(0.52,2.26); SIP 17(5.3)/9(2.9), 1.82(0.83,4.02); other 27(8.4)/32(10.2), 0.80(0.50,1.30); pulmonary haemorrhage 11(3.4)/14(4.5), 0.75(0.35,1.62). AE burden mean(SD) 1.6(1.5)/1.3(1.4), P=.004; medians 1(1-2)/1(0-2).

Any SAE 64(19.9)/54(17.3), RR 1.13(0.82,1.55); SAE interest 53(16.5)/42(13.4), 1.20(0.83,1.73); fatal 22(6.9)/25(8.0), 0.84(0.49,1.44). SAE categories pp.5-6: ET 1/1, 0.98(0.06,15.66); hypoxemia 1/2,0.49(0.04,5.39); air leak 5/12,0.37(0.13,1.06); hypotension 13/8,1.53(0.64,3.63); hypertension 0/1 NA; hyperglycemia 8/3,2.64(0.69,10.05); ICH 17/19,0.85(0.45,1.58); early/late sepsis 4/2,1.96(0.36,10.79) and 5/2,2.46(0.47,12.78); PVL 0/0 NA; SIP 15/9,1.61(0.72,3.61); other 18/20,0.84(0.46,1.55); pulmonary haemorrhage 8/8,0.94(0.35,2.48). SAE burden 0.3(0.6)/0.3(0.6), P=.42; median 0(0-0)/0(0-0). Match key: `POP=SAF; OUTCOME=AE/SAE; ARM=as treated; TIME=168h (SIP/PVL 720h)`.

### RES-S001 to RES-S003 — eTable 3 statistics (pp.5-6)

`RES-S001`: RRs and 95% CIs compare BUD+SF relative to SF and use robust Poisson regression adjusted for gestational-age strata and pooled centre unless noted; alpha .05 descriptive. `RES-S002`: low-prevalence rows marked b are crude unadjusted odds-ratio approximations with exact 95% CIs, despite the displayed column heading "Relative Risk." `RES-S003`: AE/SAE burden P values use Wilcoxon rank-sum tests; RRs not applicable. The P=.004 and P=.42 displays are not display-zero cases.

### RES-N004 and RES-S004 — eTable 4 clinical/growth outcomes (pp.7-8)

Safety BUD+SF/SF: death by 120d 50/321(15.6)/44/313(14.1), RR 1.09(0.76,1.57); NEC/death 77/320(24.1)/72/313(23.0),1.04(0.79,1.37); NEC 35/319(11.0)/40/308(13.0),0.85(0.56,1.29); PDA/death 182/320(56.9)/197/313(62.9),0.89(0.79,1.00); PDA 159/319(49.8)/175/308(56.8),0.86(0.75,0.99); medical-PDA/death 121/316(38.3)/128/311(41.2),0.91(0.76,1.09); medical-PDA 84/315(26.7)/98/306(32.0),0.80(0.64,1.01); surgical/catheter PDA/death 54/320(16.9)/47/313(15.0),1.11(0.78,1.57); procedure 5/319(1.6)/3/308(1.0),1.62(0.38,6.83); stage-3 ROP/death 87/318(27.4)/83/310(26.8),1.02(0.80,1.29); ROP 37/277(13.4)/40/270(14.8),0.87(0.60,1.28).

36w-PMA growth: weight z -1.1(0.9)/-1.2(0.8), MD .07(-.08,.22); <10th weight 107/261(41.0)/113/259(43.6),RR .95(.78,1.15); weight/death 155/309(50.2)/154/300(51.3),.98(.84,1.14); length z -2.0(1.0)/-2.0(1.0),MD .04(-.12,.21); <10th length 201/261(77.0)/201/259(77.6),.99(.90,1.08); length/death 249/309(80.6)/242/300(80.7),1.00(.93,1.08); HC z -1.5(1.0)/-1.6(1.0),MD .04(-.132,.203); <10th HC 141/261(54.0)/140/258(54.3),1.00(.85,1.16); HC/death 189/309(61.2)/181/299(60.7),1.01(.89,1.14). `RES-S004`: binary RRs robust Poisson; continuous least-squares MD robust normal identity-link GLM; both adjusted for GA strata/pooled centre. Outcomes have nonmissing denominators; clinical GDB through 120d PNA and growth at 36w PMA. **Label observation:** p.8 expands `RR` as "risk difference", whereas p.7 header and model text use **relative risk**; preserve for cross-source/label review, not a candidate diagnosis.

### RES-N005 — eTable 5 deviations/violations (pp.9-10)

ITT BUD+SF/SF n=323/318: any deviation 69(21.4)/51(16.0); major 11(3.4)/7(2.2). Counts by violation/deviation type are directly retained in `results_pages/doc005_page_09.txt`: lack consent 2/0; ineligible 3/4; randomized never initiated 3/3; wrong GA stratum 8/8; >48h 0/1; wrong drug D1 1/0, D2 0/3; incorrect dose D1 24/17, D2 9/13; >50h dose 2 1/0; preparation NPP D1 2/1, D2 0/0; unmasking 6/1; indomethacin 1/3; other violation D1 1/0,D2 0/0,non-dose 5/1; deviations: aged-out 0/0, open-label surfactant 7/4, BPD assessment 8/3, other D1 0/0,D2 1/1,non-dose 4/2. Footnotes identify one additionally excluded no-consent infant and state categories/events may overlap. Match key `POP=ITT; ARM=as randomized; OUTCOME=protocol compliance`.

### RES-N006 and RES-N007 — eTables 6-7 event-frequency summaries (pp.11-14)

AE events: 500/403; interest 468/366; unexpected 83/65. SAE events: 90/80; interest 70/59; unexpected 27/24. These tables explicitly count **events**, not participants; group n=322/313 is reference only. Category, severity, relationship, action, and outcome counts are transcribed in `results_pages/doc005_page_11.txt` through `doc005_page_14.txt`; category sums need not equal event totals because classifications/categories can overlap. Important cross-source match key: `POP=SAF; QUANTITY=event count (not participant incidence); ARM=as treated`.

### RES-N008 — eTable 8 deaths (pp.15-16)

Safety BUD+SF/SF: death by 120d 50/321(15.6)/44/313(14.1); by 36w 48/321(15.0)/41/313(13.1); by 7d post-last-dose 18/321(5.6)/21/313(6.7); death-age mean(SD) 21.9(22.8)/18.0(26.3), median 12(5-33)/10(2-18), range 1-89/1-115; fatal SAE 22/321(6.9)/25/313(8.0). Cause-of-death counts are event/cause listings and may be multiple per death; source states causes come from GDB and may differ from fatal-AE terms. Match key: `POP=SAF; OUTCOME=all-cause in-hospital death; TIME=120d PNA/36w PMA/7d PLD`.

## Handoff counts

Mapped direct-source units: DOC-004 48/48 coverage records; DOC-005 16/16 mapped. Provisional relationships: 8 SAP numeric, 5 SAP statistical/definition; 8 results numeric groups and 4 results statistical/definition groups. No candidate was diagnosed or registered in this mapping shard.
