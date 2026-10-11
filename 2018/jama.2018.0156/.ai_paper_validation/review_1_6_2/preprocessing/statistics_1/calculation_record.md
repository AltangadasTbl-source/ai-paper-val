# Statistical pass-1 direct-source derivatives and calculations

Owner runtime:01a129b8-92ad-7b63-b00a-a605a8e9f04a. Compute device:CPU. Source roles: jama_jabre_2018_oi_180004.pdf REPORT; joi180004supp1_prod.pdf PLAN; joi180004supp2_prod.pdf REPORT.

Direct engine: Poppler pdftotext and pdftoppm25.03.0. All outputs are under .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/. No new OCR, Python extraction, external source or legacy scientific conclusions were used.

Commands producing derivatives:

```bash
pdftotext -layout jama_jabre_2018_oi_180004.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/main-layout.txt
pdftotext -layout joi180004supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/results-layout.txt
pdftotext -layout -f 120 -l 124 joi180004supp1_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/sap-layout.txt
pdftoppm -f 6 -l 6 -singlefile -scale-to 2200 -png jama_jabre_2018_oi_180004.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/main-p6
pdftoppm -f 3 -l 3 -singlefile -scale-to 1800 -png joi180004supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/results-p3
pdftoppm -f 130 -l 130 -singlefile -scale-to 1700 -png joi180004supp1_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/plan-p130
pdftoppm -f 121 -l 121 -singlefile -scale-to 1700 -png joi180004supp1_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/plan-p121
```

Targeted direct stdout inspections also used pdftotext -layout -f/-l for PLAN pp36–37,64–71,90–92,110 and REPORT pages. Fresh image inspections confirmed Table2/3 alignment and signed/native SAP hypothesis signs.

## Same-display reproducing calculation

Arithmetic engine: JavaScript Number, auxiliary calculations only. This does not establish the unnamed source CI method. For two independent binomial proportions, d=100(a/n−b/m); SE=100√[p(1−p)/n+q(1−q)/m]; 95% interval=d±1.95996398454SE. It reproduces all unaffected comparable Table2 rows and the eTable2 companion row under the normative display rule. A distinct method could explain an affected row; that missing definition is retained as the human question under Route A category4.

| Display row | Recomputed difference | Recomputed SE | Recomputed lower CI | Recomputed upper CI | Conservative lower-endpoint input-rounding interval | Conservative upper-endpoint input-rounding interval |
|---|---:|---:|---:|---:|---|---|
| ITT day28 | 0.11899315 | 0.99585794 | -1.83285255 | 2.07083886 | [-1.94548947, -1.72017775] | [1.95816451, 2.18347623] |
| ITT admission | -3.70301308 | 2.04132378 | -7.70393417 | 0.29790800 | [-7.83540044, -7.57246424] | [0.16643678, 0.42937298] |
| ITT ROSC | -4.66072534 | 2.12944386 | -8.83435860 | -0.48709207 | [-8.97083872, -8.69787464] | [-0.62357776, -0.35061368] |
| PP day28 | 0.01886420 | 1.02875615 | -1.99746080 | 2.03518921 | [-2.11638896, -1.87849692] | [1.91621931, 2.15411135] |
| PP admission | -4.04066995 | 2.10213883 | -8.16078633 | 0.07944644 | [-8.29971929, -8.02185733] | [-0.05949222, 0.21836974] |
| PP ROSC | -5.60693180 | 2.19356225 | -9.90623480 | -1.30762879 | [-10.05074456, -9.76172934] | [-1.45214509, -1.16312988] |
| ECMO excluded | 0.44069424 | 0.90959080 | -1.34207097 | 2.22345945 | [-1.46026215, -1.22381737] | [2.10520688, 2.34165166] |
| crossover | 0.91781966 | 0.91560503 | -0.87673322 | 2.71237253 | [-0.99260274, -0.76077350] | [2.59644548, 2.82827471] |
| difficulty | 4.65718766 | 1.61652520 | 1.48885649 | 7.82551883 | [1.36892116, 1.60879787] | [7.70557626, 7.94545296] |
| failure | 4.60362852 | 0.90350785 | 2.83278567 | 6.37447138 | [2.71912775, 2.94649615] | [6.26075992, 6.48812832] |
| regurgitation | 7.68236591 | 1.39623415 | 4.94579725 | 10.41893457 | [4.82936125, 5.06224578] | [10.30248678, 10.53537132] |

Every integer input was allowed its half-unit ±.5 interval, even though the printed counts are exact discrete counts. Proportion and variance bounds follow endpoint monotonicity over these narrow ranges; conservative CI bounds combine the minimum/maximum difference and SE separately. This widens, rather than narrows, the admissible recomputation. Printed decimal endpoints allow±.05 and whole-number−10 allows±.5. Findings quote the remaining interval gap divided by the absolute printed endpoint.

No CI/P threshold conflict occurs in the source results. Point containment and order are satisfied. Primary NI has lower bound below−1 and P above.025. For the primary ITT and PP results, interval-derived normal-tail checks are diagnostic only: z≈(d+1)/[(d−L)/1.959964] gives approximately.107 and.122 tail probabilities. Actual primary CI/P algorithms are not supplied; no exact-model equality is asserted.

Sample-size diagnostic (not a replacement for the reported5000 simulations): independent-normal approximation n=(.03×.97+.02×.98)(1.95996398454+.84162123357)^2/(.03−.02+.01)^2=955.6011, rounding to956/group. The supplied Newcomb-Wilson simulation implementation and seed are absent; no reproduced sample-size contradiction was found.

Excluded low-precision rows: PP day28 difference input range[−.09000715,.12772954] overlaps printed.1±.05; PP admission lower endpoint gap≤.37186/7.6=.04893. PP CPC1 ETI34/943 yields rounding percentage range[100×33.5/943.5,100×34.5/942.5]=[3.550609,3.660477] and tiny remaining gap≤.000609/3.5=.000174. PP ROSC377/943 printed30.0 has recomputed percentage range[39.90461049,40.05305040]; gap9.85461049/30=.328487.

Limitations concern supplied definitions only: unnamed CI algorithms and row-specific test choices, continuous summaries/test dispersion, interim thresholds, and imputation triggers. No scientific-coverage gap remains.

