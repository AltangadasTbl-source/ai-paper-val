# Canonical Numeric and Reporting Relationship Inventory

## Inventory rule

One `N` record is a distinct printed numeric/reporting relationship. Repeated occurrences are merged only where population, time, contrast, value/precision, and rule are the same; all locations and mapper provenance are retained. `PROSPECTIVE` means protocol/SAP planning, not an observed result. Mapper observations are retained without adjudication or C IDs.

| Stable ID | Relationship / printed values | Source locations and status | Mapper provenance | Enabled checks |
|---|---|---|---|---|
| N001 | Trial identity, 97 sites, randomised 16,500; conservative/usual 8258/8242 | DOC-001 pp.1,4; DOC-003 pp.15-16; OBSERVED | MAIN-N001,N002,N012,N014; D3-N009 | totals; cross-source population |
| N002 | Participant flow: 52,747 screened; 49,233 inclusion; 38,479 potentially eligible; 21,979 not randomised; 16,500 randomised | DOC-001 p.4 Figure 1; OBSERVED | MAIN-N009--N014 | arithmetic; flow totals |
| N003 | Removal/primary-data populations: removed 66 (28/38); primary analysis 16,434 (8230/8204); known primary outcomes 16,394 (8211/8183); 40 unlinked | DOC-001 pp.1,4,8; DOC-003 p.24; OBSERVED | MAIN-N003,N012--N014,N032; D3-S003 | denominator; cross-source |
| N004 | Intervention target/range: SpO2 90%, 88%-92%, through ICU discharge or 90 d; usual care clinician discretion/no upper alarm | DOC-001 pp.1,3; DOC-002 pp.20-22,57-62,83-85,117,120; PROSPECTIVE support plus OBSERVED main description | MAIN-N002,N006; D2A-N010; D2C-N001,N014; D2E-N001 | label; version; scale |
| N005 | Eligibility: adult, invasive MV, supplemental oxygen/FIO2 >.21; 90-d prior randomisation/ECMO exclusions | DOC-002 pp.7,15-17,122; PROSPECTIVE | D2A-N002,N008; D2E-S003 | population; definition |
| N006 | Planning sample-size scenarios: 34% to 31.5% with 5% allowance (v1.1); 37% to 34.5%, 2.5 pp, 90% power, 5% alpha, 15,444 plus 6% to target 16,500 (later protocol/SAP) | DOC-001 p.3; DOC-002 pp.26,29,70,117; PROSPECTIVE | MAIN-N008; D2A-N012; D2B-N002; D2C-N009; D2E-N002 | arithmetic; version; planning-v-observed |
| N007 | Interim sizes 4,500/10,000 and Peto-Haybittle P<.001 | DOC-001 p.3; DOC-002 pp.30,71,119; PROSPECTIVE | MAIN-N008; D2B-N003; D2C-N010; D2E-S002 | rule/label; version |
| N008 | Enhanced collection plan: 14,000 basic +2,500 enhanced (15%); first 10/site and subsequent random sampling | DOC-002 pp.66-67,119; PROSPECTIVE | D2C-N004,N005; D2E-N003 | arithmetic; sampling label |
| N009 | Observed enhanced subset 2,489=1252/1237; strata 952/1537/13,945=16,434 | DOC-001 pp.4,7; DOC-003 pp.9-10,19-20; OBSERVED | MAIN-N017,N034,N035; D3-N006,N012 | totals; cross-source population |
| N010 | Baseline sex/age: median 60 (48-71) both arms; female 2803/7340 and 2849/7465=38.2%; total 5,652 | DOC-001 pp.1,4-5; DOC-003 pp.17-18; OBSERVED | MAIN-N003,N015,N018,N019; D3-N010,N011 | proportions; cross-source |
| N011 | Baseline categories: ethnicity, BMI, diagnosis, SpO2, PaO2/FIO2, severity values with outcome/linkage-qualified denominators | DOC-001 p.5; DOC-003 pp.17-20; OBSERVED | MAIN-N020--N027; D3-N010--N012 | subgroup sums; denominator; labels |
| N012 | Exposure scale: room air .21; 1 h FIO2 1.0 or 2 h .605 = one 100%-equivalent O2 hour | DOC-001 p.3; DOC-002 pp.71,120; DOC-003 pp.2,21; definition | MAIN-N007; D2E-N004; D3-N001,N013 | formula; unit; cross-source |
| N013 | Mean FIO2 .31(.14) vs .35(.15); total O2 20.3 vs 28.7 h; -8.4 h (95% CI -10.8,-6.0), -29.3% | DOC-001 pp.1,6; DOC-003 pp.21-23,27; OBSERVED | MAIN-N004,N028; D3-N013,N014,N017 | difference; unit; cross-source |
| N014 | SpO2/PaO2: 93.3%(2.8)/71.5(13.9) vs 95.1%(2.4)/79.5(17.9) mm Hg | DOC-001 p.6; DOC-003 pp.21,27; OBSERVED | MAIN-N029; D3-N013,N017 | unit/label; cross-source |
| N015 | Exposure times: target 88-92 62.6 vs27.2 h; room-air >92 39.7 vs26.1; <88 3.2 vs2.3 | DOC-001 p.6; DOC-003 pp.21-23; OBSERVED | MAIN-N030; D3-N013,N014 | unit; cross-source |
| N016 | Conservative adherence: 526/1252=42.1%; 10.6% ICU time; 2,271 periods and causes 857+413+127+265+609 | DOC-001 pp.6,10; OBSERVED | MAIN-N031,N041 | arithmetic; denominator; label |
| N017 | Figure 2 longitudinal denominators and category labels, days 0/2/4/6/8/10 | DOC-001 p.7; DOC-003 pp.9-10; OBSERVED | MAIN-N034--N036; D3-N006 | cross-source; time/population |
| N018 | Primary 90-d deaths 2908/8211=35.4% vs2858/8183=34.9%; unadjusted RD .5 pp | DOC-001 pp.1,6,8; OBSERVED | MAIN-N004,N032 | proportion; cross-source |
| N019 | ICU and hospital duration summaries and survivor/nonsurvivor subcounts | DOC-001 p.8; DOC-003 p.25; OBSERVED | MAIN-N037,N038; D3-N015 | sums; population |
| N020 | 30-d DAWOS distributions: medians 16(-1,25) both arms; 30-d deaths 2435/7449 vs2427/7573; survivor values 23(16,26)/23(15,26) | DOC-001 p.8; DOC-003 pp.7,13,25; OBSERVED | MAIN-N039; D3-N003,N008,N015 | scale; denominator; cross-source |
| N021 | Main Figure 3 diagnosis/COVID/ethnicity subgroup event counts/denominators | DOC-001 p.9; OBSERVED | MAIN-S017--S020 (numeric components) | subgroup sums; population |
| N022 | Post-hoc Figure 7 subgroup event counts/denominators, including first-10 200/486 vs159/465 | DOC-003 p.14; OBSERVED | D3-S002 | proportion; subgroup/label |
| N023 | One-year time-to-death at-risk/event rows and follow-up IQR; 66 removed and 342 missing death dates | DOC-003 p.12; OBSERVED | D3-S001 | population; time; censoring |
| N024 | Missingness: baseline PaO2/FIO2 1176(7.2%); primary 40(.2%); secondary outcome counts and 13,052 reached 1 y | DOC-001 pp.4,8; DOC-003 p.24; OBSERVED | MAIN-N013,N014; D3-S003 | denominator; cross-source |
| N025 | SAE patients 58(.7%) vs29(.4%) and specified event/patient counts | DOC-001 p.6; DOC-003 p.26; OBSERVED | MAIN-N033; D3-N016 | rate-v-count; cross-source |
| N026 | Site counts sum to 16,500; 97 named sites | DOC-003 pp.15-16; OBSERVED | D3-N009 | arithmetic; source total |
| N027 | Representativeness trial/CMP 16,500 vs207,857 and associated demographics | DOC-003 p.18; OBSERVED | D3-N011 | denominator; population label |
| N028 | Outcome/collection definitions: 90-d death; 60-d/1-y; ICU/hospital censoring; DAWOS death=-1 and organ-support components | DOC-002 pp.7-8,29,69,116,125; DOC-003 pp.3-7; planning/observed definition | D2A-N003,N007; D2B-N001; D2C-N008; D3-N002,N003 | time point; measure label |
| N029 | Economic definitions: 90-d costs/QALYs/NMB, decedent zero QALYs, GBP20,000/QALY, lifetime projections | DOC-002 pp.30-31,71-72,116,128-131; PROSPECTIVE | D2B-N004; D2C-N011; D2E-N001 | time/scale/label |
| N030 | Pilot traffic-light boundaries (sites, recruitment, separation, adherence) | DOC-002 pp.69-70,118; PROSPECTIVE | D2C-N007; D2E-N001 | thresholds; cross-reference |
| N031 | Historical/background quantities and cited estimates in protocol | DOC-002 pp.12-14; CONTEXT, not UK-ROX result | D2A-N005,N006 | source/status/measure |
| N032 | Contents/table identity: DOC-003 p.1 eTable 1-4 titles versus actual p.15-19 identities | DOC-003 pp.1,15-19; OBSERVED mapper observation | D3-C01 | label/identity; cross-location |
| N033 | SAP p.118 broken internal reference after separation/adherence definition | DOC-002 p.118; PROSPECTIVE mapper observation | D2E-O001 | internal cross-reference |

No candidate ID, adjudication, severity, or disposition is assigned in this inventory.
