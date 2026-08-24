# Canonical Support Quantitative Evidence

## Scope, source basis, and shard union

This canonical record losslessly indexes the completed disjoint fresh support mappings. Its evidence is the complete union of the three listed part files; no part has been replaced, edited, or excluded. `DOC-002` is `joi180004supp1_prod.pdf` and `DOC-003` is `joi180004supp2_prod.pdf`.

| Shard | Direct-source units | Complete evidence record | Result-relevant content retained |
|---|---|---|---|
| support-001 | DOC-002 pp. 1-50 | `extraction/parts/support_001_pp001_050.md` | Protocol V1.3 endpoint, population, sample-size, interval/test, follow-up, recruitment, centre, and mRS definitions; labelled external background values. |
| support-002 | DOC-002 pp. 51-100 | `extraction/parts/support_002_pp051_100.md` | Protocol V1.4/V2 scales, IDS/VAS/Han definitions, repeated endpoint and analysis rules, recruitment/centre/follow-up definitions, and labelled external background values. |
| support-003 | DOC-002 pp. 101-134; DOC-003 pp. 1-3 | `extraction/parts/support_003_pp101_134_doc003.md` | Amendment and SAP definitions, centre amendment, eTable 1 centre contributions, and eTable 2 post-hoc results. |

The part files above are integral records of this canonical artifact: they preserve the complete page-by-page coverage tables, every extracted value, all table rows, exact locations, and extraction limitations. They are linked by a single plain relative artifact path per shard and are not old-audit derivatives.

## Complete quantitative evidence index

| Evidence family | Exact locations | Quantities/definitions and comparison controls |
|---|---|---|
| Primary endpoint and follow-up | DOC-002 pp. 9-11, 15-21, 36-37, 64-66, 71-76, 90-92, 110, 119-124 | Day-28 survival with favourable neurologic function is CPC <=2; the amendment permits unchanged pre-randomization disability. Vital status is day 28, assessed within day 28 +7 where needed. Match BMV minus TI/BVM minus tracheal, ITT/PP/AT population, and time point before comparing values. |
| Planned design | DOC-002 pp. 10-11, 24, 64-66, 79, 90-92, 120-124 | 3% BMV/BVM versus 2% TI; 1% NI margin; 956/group; power .8; type-I error .025; 2,000 recruitment; 5,000 simulations; interim 50%/75%; 20 initial centres, 24 months. Planning inputs are not observed outcomes. |
| Analysis definitions | DOC-002 pp. 11, 36-37, 66, 90-92, 121-124 | ITT/PP/AT definitions; primary missing ITT endpoint=no success; conditional sensitivity/multiple imputation; primary two-sided 95% CI for pi(BVM)-pi(TI), lower bound > -0.01; secondary chi-square, OR/difference CI, t/Mann-Whitney and safety Fisher options as specified. |
| Measure and scale definitions | DOC-002 pp. 50-54, 79-80, 101-105, 122-124 | mRS 0-6 (6=dead, higher=worse); CPC 1-5; IDS component sum and categories; VAS 0-100; Han 0-4. A scale score is not a rate/count. Categorical percentages use non-missing denominators, one decimal, and can round away from 100%. |
| Recruitment/centre context | DOC-002 pp. 10, 17, 24, 72, 79, 108, 112-113; DOC-003 p. 2 | Original 20 centres (15 France/5 Belgium); amendment: centre 19 withdrew and centres 21-26 added, giving 25 (20-1+6). eTable 1 has 21 contributing labels and group denominators BMV 1018/ETI 1022; do not interpret absent centres as zero-participant contradictions. |
| eTable 1 all rows | DOC-003 p. 2 | The complete 21 centre rows and percentages are preserved in support-003. BMV counts sum to 1018, ETI counts sum to 1022, and every percentage is compatible with its group denominator to one decimal. |
| eTable 2 row 1 | DOC-003 p. 3 | Excluding ECMO-CPR/uncontrolled donation: BMV 43/971 (4.4%), ETI 39/978 (4.0%), BMV%-ETI%=0.4 pp, 95% CI [-2.2,1.3], P=.63. Compare only in its post-hoc population. |
| eTable 2 row 2 | DOC-003 p. 3 | Reclassification before ROSC: BMV 41/863 (4.8%), ETI 45/1174 (3.8%), BMV%-ETI%=0.9 pp, 95% CI [-.9,2.7], P=.31. Compare only in its post-hoc population. |
| Protocol background/administration | DOC-002 pp. 12-13, 26-30, 43, 67-69, 78, 81-89, 97 | External-study values, deadlines, blank forms, and retention rules remain mapped and explicitly labelled. They are not CAAM observed results absent exact population/outcome matching. |

## Coverage limitations

All assigned units are represented in their disjoint part records. DOC-002 p. 52 uses user-authorized, source-hash-matched supplied OCR only; no OCR engine was run. DOC-002 pp. 108-109 and 126-133 likewise use authorized supplied OCR where fresh text was empty. DOC-002 p. 134 is empty in both fresh text modes and has no authorized OCR, so it contributes no relationship.
