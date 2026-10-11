# Extended numeric relationships and exhaustive pooling diagnostics

Owner /root/numeric_review. Additional companion relationships N136–N140 extend N001–N135 without renumbering. REPORT sources: [main Table1 pp5–6](../../../jama_thille_2019_oi_190108.pdf#page=5), [main continuation p6](../../../jama_thille_2019_oi_190108.pdf#page=6), [main outcomes/stratum risk p8](../../../jama_thille_2019_oi_190108.pdf#page=8), [results eTable2 p3](../../../joi190108supp2_prod.pdf#page=3), [results eTable2 p4](../../../joi190108supp2_prod.pdf#page=4), [results outcomes p6](../../../joi190108supp2_prod.pdf#page=6), [results outcomes p7](../../../joi190108supp2_prod.pdf#page=7), [results center table p8](../../../joi190108supp2_prod.pdf#page=8). Every source here is REPORT.

## N136 — NIV pre-SBT PaCO2 pooled dispersion

Companion N046/S096. Main mean(SD)40(8)mmHg; subgroups n276 with37(8), n63 with51(8). If these n identify the same complete measured partition, the pooled sample variance is [(276−1)×8²+(63−1)×8²+(276×63/339)×(37−51)²]/338=93.553961, SD9.672330mmHg. Mean39.601770 rounds40 and is coherent. For integer-printed subgroup SD8 and means37/51, choose smallest permitted SD7.5 and mean gap13; minimum pooled SD9.040442. The main rounded SD8 implies [7.5,8.5), which is disjoint. Direct observations: cells/labels/group headers. Derived diagnostic: pooling under identical measured n/population. Missing definition: per-variable measured n and identical measurement subset across main/subgroups. B19 preserves the condition; no missingness imputation.

## N137 — all main/stratum means and SD under rounding

Every pooled mean was tested with input and output half-last-unit intervals: if all displayed means have resolution r, midpoint pooled mean may differ from main by up to r because input and output rounding both contribute. All18 paired row means overlap their main rounding intervals. All36 SD checks use the variance identity above, with SD endpoints shifted by half the printed last unit and between-stratum mean gap shifted by a full last unit. The sole disjoint SD is N136; the table retains every other interval.

| Row | Arm | Pooled SD midpoint | Feasible pooled SD interval from printed rounding | Main printed SD | Rounding ranges overlap? |
|---|---|---:|---|---:|---|
| age | HF | 9.833666 | 9.334856–10.339000 | 10 | YES |
| age | NIV | 10.206038 | 9.685214–10.738952 | 10 | YES |
| BMI | HF | 6.254391 | 5.706115–6.814810 | 6 | YES |
| BMI | NIV | 7.489367 | 6.945140–8.046632 | 7 | YES |
| SAPS | HF | 17.687344 | 17.177341–18.204116 | 17 | YES |
| SAPS | NIV | 19.886088 | 19.354137–20.423820 | 20 | YES |
| SOFA | HF | 2.567670 | 2.515166–2.620585 | 2.5 | YES |
| SOFA | NIV | 2.695236 | 2.645160–2.745860 | 2.7 | YES |
| PS | HF | 2.752233 | 2.698068–2.806719 | 2.8 | YES |
| PS | NIV | 2.878308 | 2.825417–2.931612 | 2.9 | YES |
| PEEP | HF | 1.615051 | 1.563914–1.666918 | 1.6 | YES |
| PEEP | NIV | 1.580785 | 1.529682–1.632744 | 1.6 | YES |
| tidal | HF | 125.294795 | 124.731236–125.858877 | 125 | YES |
| tidal | NIV | 143.531992 | 143.032233–144.032802 | 144 | YES |
| tidalkg | HF | 2.331165 | 2.275800–2.386853 | 2.4 | YES |
| tidalkg | NIV | 2.462008 | 2.411189–2.513395 | 2.5 | YES |
| RR | HF | 6.851382 | 6.343176–7.376555 | 7 | YES |
| RR | NIV | 6.186930 | 5.688733–6.696626 | 6 | YES |
| FIO2 | HF | 9.265184 | 8.719386–9.819682 | 10 | YES |
| FIO2 | NIV | 10.834987 | 10.315373–11.366133 | 11 | YES |
| PF | HF | 92.281438 | 91.726065–92.837617 | 93 | YES |
| PF | NIV | 89.414856 | 88.863989–89.966808 | 89 | YES |
| pH | HF | 0.058906 | 0.053593–0.064376 | 0.06 | YES |
| pH | NIV | 0.050530 | 0.045102–0.056148 | 0.05 | YES |
| preCO2 | HF | 8.012384 | 7.395266–8.629788 | 8 | YES |
| preCO2 | NIV | 9.672330 | 9.040442–10.304385 | 8 | NO; N136/B19, conditional measured n |
| SBP | HF | 20.892246 | 20.365508–21.423925 | 21 | YES |
| SBP | NIV | 22.615142 | 22.112826–23.123889 | 22 | YES |
| DBP | HF | 13.945822 | 13.406367–14.491646 | 14 | YES |
| DBP | NIV | 15.981062 | 15.477054–16.493985 | 16 | YES |
| HR | HF | 17.315279 | 16.805055–17.832400 | 17 | YES |
| HR | NIV | 18.078584 | 17.543431–18.619895 | 18 | YES |
| endRR | HF | 6.001210 | 5.490856–6.530400 | 6 | YES |
| endRR | NIV | 6.186930 | 5.688733–6.696626 | 6 | YES |
| SpO2 | HF | 3.083276 | 2.522570–3.662841 | 3 | YES |
| SpO2 | NIV | 3.095219 | 2.526512–3.685040 | 3 | YES |

Inputs for all rows remain in main/support inventories N015–N055 and S075–S107. Gas end-SBT PaO2/pH/PaCO2 are separately reviewed, with main n221/241 but stratum measured n absent: no pooled identity using254/48/276/63 is imposed. Medians/IQRs for ventilation/trial/stays are not averaged across strata.

## N138 — center distribution identities

Companion N059,N125–N134. Every center count/percentage was recalculated. All30 numerator and denominator row sums agree; center event totals95=55+40 and population641=302+339.
HF denominator order statistics:
1,2,2,2,3,4,5,5,6,7,7,8,10,10,10,10,11,11,12,12,12,13,14,14,15,16,17,19,19,25.
NIV:
2,2,3,4,5,5,6,7,7,7,9,9,11,12,12,13,13,13,13,13,13,14,16,16,17,17,17,19,21,23.
HF median10 and NIVmedian12.5 support printed10/13. Linear sample quartiles HF5.25–13.75, NIV7–15.5; Tukey median-of-halves HF5–14,NIV7–16. Printed HF9–25 andNIV9–23 do not describe these IQRs under ordinary sample quartile conventions; B17/B18. To avoid substituting an unspecified quantile algorithm, the discrepancy is grounded also in order-statistic position:9 absent fromHF values nearQ1; upper25/23 are sole maxima, not75th percentiles. Human must identify intended center population, quantity and quantile definition.

## N139 — exact subgroup sums and conditional event totals

Companion S111–S136 and mainS002–S015. HF/NIV sums:
day7 reintubation10+45=55/5+35=40;
ARF24+64=88/14+56=70;
48h4+32=36/2+22=24;
72h9+38=47/4+26=30;
ICUreintubation10+49=59/6+35=41;
criteria11+54=65/7+42=49;
ICUmortality5+21=26/2+19=21;
composite11+53=64/6+45=51;
reintubatedmortality4+17=21/2+9=11 with denominators10+49=59/6+35=41;
hospitalmortality7+39=46/8+46=54;
day90mortality11+54=65/12+50=62.
All partition totals exactly agree. Mortality-or-reintubation identity |M unionR|=|M|+|R|−|MintersectionR| holds mainHF26+59−21=64 andNIV21+41−11=51; each stratum also holds. Temporal reintubation counts nondecreasing from48h→72h→day7→ICU for every arm/stratum. These are count identities, not censored survival risk-table identities.

## N140 — every figure risk partition/time/scale

Companion N069–N076. Eight day0–7 risk sums:
HF[48,44,44,39,38,37,37,37]+[254,232,221,214,210,209,207,206]=[302,276,265,253,248,246,244,243].
NIV[63,63,61,59,58,58,58,58]+[276,258,253,249,247,236,234,233]=[339,321,314,308,305,294,292,291].
All16 additions agree exactly, all riskrows nonincreasing and <=baseline n. Risk decline not equated with event count in presence of censoring/death.
Survival eFigure N135 day90 remaining237/277 equals302−65 and339−62 respectively; no impossible risk ordering. Curves only qualitatively read, no exact diagnostic estimated by pixels. Survival title/axis mismatch is B24.

Complete: five extended N groups; all pooled mean/SD, center, stratum-sum and risk-partition cells inspected. Conditional per-variable n limitation explicitly retained, no scientific source coverage gap.

