# Results-supplement evidence map

- Agent: `results_supplement_extractor`
- Document: `JAMA2025-16450-SUPP04-RESULTS` - `joi250072supp4_prod_1761000786.6988.pdf`
- Scope read: PDF pages 2-16 only (eTables 1-8). Native normalized text was checked against the retained page renders. No protocol, SAP, manual, external source, or diagnostic conclusion was used.
- Conventions: B+S = Budesonide + Surfactant; SA = Surfactant Alone. Unless stated otherwise, B+S / SA values appear in that order.

## Population and linking anchors

| Analysis population | Source location | Denominator / composition |
|---|---|---|
| ITT | PDF p.2, eTable 1 | n=641: B+S 323 (50.4%), SA 318 (49.6%); treatment group is **as randomized**. |
| ITT excluding untreated | PDF p.2, eTable 1 | n=635: B+S 320 (50.4%), SA 315 (49.6%); as randomized. |
| Safety (SAF) | PDF p.2, eTable 1 | n=635: B+S 322 (50.7%), SA 313 (49.3%); **as treated**. This is the denominator for eTables 2-4 and 6-8. |
| Per-protocol (PP) | PDF p.2, eTable 1 | n=617: B+S 309 (50.1%), SA 308 (49.9%); as treated. Defined as randomized, treated, and without major protocol violation. |

Primary-endpoint completion in those populations is 639/641 (99.7%), 634/635 (99.8%), 634/635 (99.8%), and 617/617 (100.0%), respectively; early end is 2, 1, 1, and 0. GDB status (ITT / ITT-minus-untreated / SAF / PP) is discharged home 340/337/337/329, in hospital at 120 days 189/189/189/184, transferred 16/16/16/15, and death 86/86/86/84 (PDF p.2, eTable 1).

## eTable-level evidence

### eTable 1 - Analysis Populations and Participant Disposition

**Location:** PDF p.2. **Rows and columns:** the four population columns above; each disposition percentage uses that column's n. The SAF and PP columns are as-treated; the two ITT columns are as-randomized. Key anchors: treated = 635/641 (99.1%), 635/635 (100.0%), 635/635 (100.0%), 617/617 (100.0%). See population table for all denominators and disposition counts.

### eTable 2 - Extent of Exposure, Safety Population

**Location:** PDF pp.3-4. **Columns/denominators:** B+S n=322 and SA n=313, as treated; dose-2 subsets B+S n=102 and SA n=118; B+S budesonide dose-1 subset n=319.

- One/two doses: 220 (68.3%)/102 (31.7%) versus 195 (62.3%)/118 (37.7%).
- Postnatal age at dose 1, mean (SD): 4.05 (7.47) versus 3.70 (6.80) h; median (Q1-Q3) 1.7 (0.5-3.6) versus 1.6 (0.6-3.3); range 0.0-48.4 versus 0.0-49.2. Dose 2: mean 23.09 (11.81) versus 21.98 (10.12); median 17.8 (13.7-29.7) versus 18.6 (14.3-25.9); range 7.6-59.9 versus 9.5-49.4.
- Not treated per-protocol: 36 (11.2%) versus 29 (9.3%); component counts are group-assignment violation 3/1, dose-volume violation 31/27, and administration violation 2/1. Footnote states an infant may have multiple non-compliance reasons.
- Surfactant-volume compliance (%), dose 1: mean 99.35 (5.22) versus 100.03 (4.73), median 100.0 (99.6-100.3) versus 100.0 (99.8-100.5), range 49.9-120.0 versus 51.2-120.0. Dose 2: mean 102.12 (14.71) versus 101.70 (10.67), median 100.0 (99.1-101.5) versus 100.1 (99.6-101.6), range 80.0-201.0 versus 74.1-191.3.
- B+S budesonide-volume compliance: dose 1 (n=319) mean 102.29 (24.06), median 100.0 (100.0-100.0), range 25.0-400.0; dose 2 (n=102) mean 99.76 (7.83), median 100.0 (100.0-100.0), range 25.0-109.9. SA cells are NA. Footnote defines 90%-110% as protocol compliant.

### eTable 3 - Adverse Event Experience, Safety Population

**Location:** PDF pp.5-6. **Columns:** participant-level B+S n=322, SA n=313; relative risks (RRs) compare B+S with SA. Robust Poisson models adjust for gestational-age strata and pooled center unless the footnote specifies another approach.

- Any AE: 242 (75.4%) vs 202 (64.5%), RR 1.16 (95% CI 1.05-1.28); any AE of interest: 240 (74.8%) vs 193 (61.7%), RR 1.20 (1.09-1.33). Category AEs, respectively: ET tube blockage 3/4, RR 0.73 (0.16-3.28); prolonged hypoxemia+bradycardia 2/3, 0.65 (0.11-3.90); pulmonary air leak 16/18, 0.86 (0.45-1.66); hypotension 56/59, 0.92 (0.67-1.27); hypertension 28/21, 1.28 (0.75-2.10); hyperglycemia 214/156, 1.33 (1.17-1.51); intracranial hemorrhage 40/37, 1.03 (0.69-1.54); early sepsis 9/8, 1.06 (0.41-2.75); late sepsis 70/70, 0.93 (0.70-1.24); PVL 15/13, 1.09 (0.52-2.26); SIP 17/9, 1.82 (0.83-4.02); other 27/32, 0.80 (0.50-1.30), including pulmonary hemorrhage 11/14, 0.75 (0.35-1.62).
- AE burden: mean (SD) 1.6 (1.5) vs 1.3 (1.4), Wilcoxon P=0.004; median (IQR) 1 (1-2) vs 1 (0-2).
- Any SAE: 64 (19.9%) vs 54 (17.3%), RR 1.13 (0.82-1.55); SAE of interest 53 (16.5%) vs 42 (13.4%), 1.20 (0.83-1.73); fatal SAE 22 (6.9%) vs 25 (8.0%), 0.84 (0.49-1.44). SAE categories: ET blockage 1/1, 0.98 (0.06-15.66); hypoxemia+bradycardia 1/2, 0.49 (0.04-5.39); air leak 5/12, 0.37 (0.13-1.06); hypotension 13/8, 1.53 (0.64-3.63); hypertension 0/1, NA; hyperglycemia 8/3, 2.64 (0.69-10.05); intracranial hemorrhage 17/19, 0.85 (0.45-1.58); early/late sepsis 4/2, 1.96 (0.36-10.79) and 5/2, 2.46 (0.47-12.78); PVL 0/0, NA; SIP 15/9, 1.61 (0.72-3.61); other 18/20, 0.84 (0.46-1.55), pulmonary hemorrhage 8/8, 0.94 (0.35-2.48).
- SAE burden: mean (SD) 0.3 (0.6) vs 0.3 (0.6), P=0.42; median (Q1-Q3) 0 (0-0) vs 0 (0-0).

### eTable 4 - Clinical and Growth Outcomes, Safety Population

**Location:** PDF pp.7-8. **Columns:** B+S n=322, SA n=313, but every binary row uses its printed n/N nonmissing denominator. RR/MD compares B+S with SA and has 95% CI; binary outcomes use robust Poisson models unless noted, continuous outcomes use robust normal-identity models; both adjust for gestational-age strata and pooled center.

- 120-day clinical outcomes: death 50/321 (15.6%) vs 44/313 (14.1%), RR 1.09 (0.76-1.57); NEC/death 77/320 (24.1%) vs 72/313 (23.0%), 1.04 (0.79-1.37); NEC 35/319 (11.0%) vs 40/308 (13.0%), 0.85 (0.56-1.29); PDA/death 182/320 (56.9%) vs 197/313 (62.9%), 0.89 (0.79-1.00); PDA 159/319 (49.8%) vs 175/308 (56.8%), 0.86 (0.75-0.99); medical-PDA/death 121/316 (38.3%) vs 128/311 (41.2%), 0.91 (0.76-1.09); medical PDA 84/315 (26.7%) vs 98/306 (32.0%), 0.80 (0.64-1.01); surgery/catheter PDA/death 54/320 (16.9%) vs 47/313 (15.0%), 1.11 (0.78-1.57); surgery/catheter PDA 5/319 (1.6%) vs 3/308 (1.0%), 1.62 (0.38-6.83); stage-3 ROP/death 87/318 (27.4%) vs 83/310 (26.8%), 1.02 (0.80-1.29); stage-3 ROP 37/277 (13.4%) vs 40/270 (14.8%), 0.87 (0.60-1.28).
- Growth at 36 weeks PMA: weight z score -1.1 (0.9) vs -1.2 (0.8), MD 0.07 (-0.08 to 0.22); <10th-percentile weight 107/261 (41.0%) vs 113/259 (43.6%), RR 0.95 (0.78-1.15); weight/death 155/309 (50.2%) vs 154/300 (51.3%), 0.98 (0.84-1.14). Length z score -2.0 (1.0) vs -2.0 (1.0), MD 0.04 (-0.12 to 0.21); <10th percentile 201/261 (77.0%) vs 201/259 (77.6%), 0.99 (0.90-1.08); length/death 249/309 (80.6%) vs 242/300 (80.7%), 1.00 (0.93-1.08). Head-circumference z score -1.5 (1.0) vs -1.6 (1.0), MD 0.04 (-0.132 to 0.203); <10th percentile 141/261 (54.0%) vs 140/258 (54.3%), 1.00 (0.85-1.16); head-circumference/death 189/309 (61.2%) vs 181/299 (60.7%), 1.01 (0.89-1.14).

### eTable 5 - Protocol Deviation and Violation Experience, ITT Population

**Location:** PDF pp.9-10. **Columns:** as-randomized B+S n=323 and SA n=318. Any protocol deviation/violation is 69 (21.4%) vs 51 (16.0%); any major deviation/violation is 11 (3.4%) vs 7 (2.2%). Footnote: participants with a major violation are excluded from PP; a major event can appear in multiple categories.

- Violation counts (%), B+S vs SA: consent 2 (0.6)/0; ineligible enrollment 3 (0.9)/4 (1.3); randomized but never treated 3 (0.9)/3 (0.9); wrong GA stratum 8 (2.5)/8 (2.5); randomized >48h PNA 0/1 (0.3); wrong study drug dose 1: 1 (0.3)/0, dose 2: 0/3 (0.9); incorrect volume/concentration dose 1: 24 (7.4)/17 (5.3), dose 2: 9 (2.8)/13 (4.1); study drug >50h PNA for dose 2: 1 (0.3)/0; preparation/administration NPP dose 1: 2 (0.6)/1 (0.3), dose 2: 0/0; unintentional unmasking 6 (1.9)/1 (0.3); indomethacin use 1 (0.3)/3 (0.9); other violation dose 1: 1 (0.3)/0, dose 2: 0/0, non-dose: 5 (1.5)/1 (0.3).
- Deviation counts (%): aged out of randomized GA strata 0/0; open-label surfactant instead of intended second dose 7 (2.2)/4 (1.3); BPD assessment not per protocol 8 (2.5)/3 (0.9); other deviation dose 1: 0/0, dose 2: 1 (0.3)/1 (0.3), non-dose: 4 (1.2)/2 (0.6).

### eTable 6 - Summary of Adverse Events, Safety Population

**Location:** PDF pp.11-12. **Columns:** B+S n=322 and SA n=313 are participant-reference denominators; values in the table are **event counts**, not participant counts.

- Total events 500 vs 403; events of interest 468 vs 366; unexpected 83 vs 65. Main category event counts: ET blockage 3/4; hypoxemia+bradycardia 2/3; pulmonary air leak 17/20; hypotension 61/63; hypertension 31/23; hyperglycemia 272/193; intracranial hemorrhage 40/37; early/late sepsis 7/5 and 13/7; PVL 5/2; SIP 17/9; other 32/37 (including pulmonary hemorrhage 11/14).
- Severity counts: mild 7/6, moderate 234/199, severe 188/128, life-threatening 43/44, fatal 28/26. Relationship: not related 124/105, unlikely 236/209, possibly 135/82, probably 5/7. Action: no change 499/402, dose interrupted 1/1. Outcomes: resolved 273/209, resolved with sequelae 4/5, resolving 71/60, not resolved 124/103, fatal 28/26.

### eTable 7 - Summary of Serious Adverse Events, Safety Population

**Location:** PDF pp.13-14. **Columns:** B+S n=322 and SA n=313 are participant-reference denominators; entries are **event counts**.

- Total SAEs 90 vs 80; events of interest 70 vs 59; unexpected 27 vs 24. Main category events: ET blockage 1/1; hypoxemia+bradycardia 1/2; air leak 5/12; hypotension 14/8; hypertension 0/1; hyperglycemia 8/3; intracranial hemorrhage 17/19; early/late sepsis 4/2 and 5/2; SIP 15/9; other 20/21 (including pulmonary hemorrhage 8/8).
- Severity: severe 19/10, life-threatening 43/44, fatal 28/26. Relationship: not related 28/23, unlikely 45/44, possibly 17/12, probably 0/1. Action: no change 90/79, dose interrupted 0/1. Outcomes: resolved 19/14, resolved with sequelae 3/1, resolving 10/11, not resolved 30/28, fatal 28/26.

### eTable 8 - In-hospital Deaths by 120 Days' Postnatal Age, Safety Population

**Location:** PDF pp.15-16. **Columns:** B+S n=322, SA n=313; printed binary rows use n/N nonmissing denominators.

- Death by 120d PNA: 50/321 (15.6%) vs 44/313 (14.1%); by 36w PMA: 48/321 (15.0%) vs 41/313 (13.1%); by 7 days post-last-dose: 18/321 (5.6%) vs 21/313 (6.7%); fatal SAEs 22/321 (6.9%) vs 25/313 (8.0%). Age at death (n=50/n=44): mean (SD) 21.9 (22.8) vs 18.0 (26.3); median (Q1-Q3) 12 (5-33) vs 10 (2-18); range 1-89 vs 1-115 days.
- Primary-cause counts (B+S/SA): RDS 5/4; RDS+severe intracranial hemorrhage 3/2; RDS+infection 1/3; RDS+massive pulmonary hemorrhage 6/4; BPD 0/2; PPHN 1/1; suspect sepsis 5/1; proven sepsis 12/2; NEC 5/4; NEC+sepsis 1/4; spontaneous perforation 0/2; severe intracranial hemorrhage 0/2; severe IVH+infection 2/0; renal failure 1/1; other 8/12. Footnote says primary cause derives from the Generic Data Base and may differ from fatal-AE terms.

## Cross-table comparison anchors (not findings)

| Anchor | Locations and exact relationship |
|---|---|
| Safety population | eTable 1 (p.2) defines SAF n=635, B+S 322 and SA 313, as treated; the same group headers appear in eTables 2-4 and 6-8 (pp.3-8, 11-16). |
| PP relation | eTable 1 (p.2) gives ITT excluding untreated n=635 and PP n=617. eTable 5 (p.9) gives 11+7=18 participants with any major deviation/violation and states these are excluded from PP; 635-18=617. |
| 120-day death | eTable 4 (p.7) and eTable 8 (p.15) both print B+S 50/321 (15.6%) and SA 44/313 (14.1%). |
| Fatal SAE participant measure | eTable 3 (p.5) gives 22 (6.9%) vs 25 (8.0%); eTable 8 (p.15) gives the same figures with exact denominators 22/321 vs 25/313. |
| AE participant/event distinction | eTable 3 (pp.5-6) reports participants with any AE: 242/322 vs 202/313, and any SAE: 64/322 vs 54/313. eTable 6 (pp.11-12) reports all AE events 500 vs 403; eTable 7 (pp.13-14) reports all SAE events 90 vs 80. |
| Fatal-event count | eTables 6 and 7 both report fatal events 28 vs 26 (pp.11-14). eTable 8 distinguishes all 120-day deaths (50 vs 44) from fatal SAEs (22 vs 25) (p.15). |

## Extraction disposition

Evidence only. No error, inconsistency, or issue diagnosis was made. Page-level source links are retained in `preprocessing/page_manifest.md` and normalized source text in `preprocessing/normalized_pages/`.
