# Numeric relationship inventory part: DOC-002, PDF pages 31-60

This part records support-side numeric relationships only. Provisional identifiers are local to this shard and must be reconciled by the coordinator with matching main-paper keys.

| Provisional numeric ID | Direct location | Relationship and matching key | Values, units, population/time/contrast |
|---|---|---|---|
| P2-N001 | PDF p. 31 | Main endpoint definition / `MAIN_KEY: progression composite` | PSADT <3 years; PSA >=10 ng/mL; biopsy >=25% positive cores, >50% of one core, Gleason >=7 (<70) or >=4+3=7 (>=70); active-surveillance participants. |
| P2-N002 | PDF p. 31 | Follow-up, censoring, and repeat-PSA rule / `MAIN_KEY: follow-up and progression handling` | Intervention 24 months; repeat suspected-spurious PSA within 2 weeks; use repeat if <10, first if repeat >=10; censor elective treatment at treatment start. |
| P2-N003 | PDF pp. 32-34 | QOL outcome definitions / `MAIN_KEY: exploratory QOL outcomes` | Seven instruments; FACT-P 27+12 items with most 0-4; MAX-PC 18 items; IPSS 8; EPIC-26 26 and domains 0-100 higher=favorable; nutrition scale 5 items on five-point Likert; satisfaction 26 items at 12/24 months. |
| P2-N004 | PDF p. 34 | Exploratory QOL contrast / `MAIN_KEY: QOL between-arm change` | Scores each time point and changes over time, intervention versus control. |
| P2-N005 | PDF p. 35 | Carotenoid correlation objectives / `MAIN_KEY: carotenoid, PSADT, pathological progression` | Plasma carotenoid concentration: arm contrast, correlation with PSADT, and correlation with pathological progression. |
| P2-N006 | PDF p. 36 | Assay/sample definition / `MAIN_KEY: carotenoid/cholesterol biospecimens` | HPLC plasma carotenoids; storage <=-70 degrees C; cholesterol assay 10 uL specimen; serum banked. |
| P2-N007 | PDF p. 37 | Genetic substudy endpoints / `MAIN_KEY: MnSOD-XRCC1-GST outcomes` | Polymorphisms versus PSADT and time to pathological progression; intervention versus no intervention. |
| P2-N008 | PDF p. 38 | Tissue substudy sample/power / `MAIN_KEY: correlative biomarker substudy` | 10 x 5 um sections, one core/slide; 80% of 418 -> n=334; 95% power for coefficient/log-HR .4 per 1 SD, alpha .05, assumed 85% 2-year PFS. |
| P2-N009 | PDF pp. 39-40 | Tissue biomarker predictor set / `MAIN_KEY: correlative biomarker PFS models` | Ki-67, cleaved caspase 3, composite growth rate; AR and 5-alpha-reductases 1/2/3; microRNAs 141/375 and approximately 200 further microRNAs. |
| P2-N010 | PDF p. 40 | Randomization/sample-size design / `MAIN_KEY: randomized population and primary PGR contrast` | N=464, 232/arm, equal probability; accrual 15/month for ~3 years, follow-up 2 years; 418 eligible gives 80% power for 20% control vs 10% experimental PGR, HR 2.118, alpha .05 two-sided; 10% dropout. |
| P2-N011 | PDF p. 41 | PSADT calculation / `MAIN_KEY: PSADT derivation` | PSADT=log(2)/least-squares slope of log(PSA); first at month 6 with months 0/3/6 if complete. |
| P2-N012 | PDF pp. 41-42 | Sensitivity/secondary endpoint and monitoring / `MAIN_KEY: eligible versus randomized; interim PGR` | Main eligible plus all-randomized sensitivity; biopsy-only secondary endpoint; if control PGR=10%, stated 50% power with 418; interim at 400 enrolled; if PGR<20%, example 18% -> 466 eligible (+11%); maximum increase 20%. |
| P2-N013 | PDF pp. 50-52 | Consent schedule corroboration / `MAIN_KEY: participant schedule and sample timing` | About 464 men; recalls run-in and months 12/24; PSA q3mo; clinic/questionnaires q6mo; blood and diet recall 12/24; biopsy 24; 22 Arm-A calls over 2 years. |
| P2-N014 | PDF p. 57 | Optional related-study sample timing / `MAIN_KEY: optional biospecimen substudy` | Additional 4 teaspoons baseline, 2 teaspoons each at months 12/24; diagnostic tissue only, no extra biopsy. |

## Numeric cross-location observations for later checking

- `P2-O001`: The planned enrollment is consistently about/exactly 464 in protocol §11.1 (PDF p. 40) and model consent (PDF p. 50); protocol allocation is 232 per arm, and 232+232=464.
- `P2-O002`: The protocol's 24-month follow-up appears in §§8.7/11.1-11.2 (PDF pp. 31,40) and consent schedule/duration (PDF pp. 51-52). Consent provides a more granular operational schedule rather than a conflicting duration.
- `P2-O003`: The age-specific repeat-biopsy progression criteria on PDF p. 31 agree with §11.2 and the biopsy-only secondary definition on PDF pp. 40-41. The rendered direct source was used to resolve extraction-garbled inequality characters.
- `P2-O004`: Page 40 states an HR of 2.118 for control 20% versus experimental 10% progression; page 42 uses HR=.472 for sample-size recalculation. These values are approximate reciprocals (1/2.118≈.472), consistent with reversal of reference-arm orientation; a later cross-source check should retain the orientation labels rather than treat the two displays as directly comparable.

