# Statistical relationship inventory — monitoring displays, pass 1

Runtime agent: 01a129be-d2f9-73e3-94d5-a2df0a75cd43; model gpt-6.1-sol; effort high; fresh spawn. Exact scope DOC-002, `joi180132supp1_prod.pdf`, physical pp.189–194. All locations are PLAN by content: prospective DSMC monitoring records bound into the protocol/SAP material. This part contains 85 stable relationships, S601–S685. No source, reused derivative, or other agent artifact was modified.

Authority: complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Locator: current `extraction/support_plan_d.md`, PD055–PD058. Direct source native/layout text read using `pdftotext -layout -f 189 -l 194 joi180132supp1_prod.pdf -`; all six source-matched reusable page images visually inspected. The p192 cumulative-chart observation was confirmed by a fresh direct-source CPU render: Poppler pdftoppm 25.03.0, `pdftoppm -f 192 -l 192 -scale-to 2200 -singlefile -png joi180132supp1_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat-monitoring-source-192`. Derivative `preprocessing/stat-monitoring-source-192.png` is a confirmation image, not source authority in place of the PDF.

Table notation below retains X/Y coding; no assignment identity is inferred. A category-row relationship includes its two counts, percentages, group denominators, GOSE category, six-month time point, and printed P value. A block relationship includes both X/Y mortality and GOSE-outcome numerator/denominator pairs, their corresponding bars, and their contribution to cumulative counts. There are no printed confidence intervals, test statistics, standard errors, or score ranges in these pages. The parenthesized GOSE-score dispersion is not explicitly named. Means reproduce from the GOSE frequency tables; sample-SD calculations are labelled diagnostic. Specific tests, sidedness, variance estimation, and any adjustment for the table P values are absent; they are not inferred from convention. No exact-P finding rests on an assumed test.

Percentage checks used input half-unit intervals and each printed percentage's half-unit interval. Every table count/percentage pair overlaps the permitted interval or has relative discrepancy at most .05. Counts also reconcile exactly as discrete totals. No displayed table P value crosses .05, and none crosses the interim .001 threshold described in the supplied monitoring charter; no stopping conclusion is stated on pp.189–194. Rules/population definitions elsewhere in the bundle belong to the separate PLAN-method shard.

## December 2015 monitoring: table and population

| S ID | PLAN location | Printed relationship | Pass-1 check and outcome | Pass 1 |
|---|---|---|---|---|
| S601 | p189, GOSE=1 | X27/140 (19%); Y27/133 (20%); P=.83 | Percentages reconcile; death direction retained; no interval/test conflict printed. | PASS_1_COMPLETE |
| S602 | p189, GOSE=2 | X1/140 (1%); Y2/133 (2%); P=.61 | Percentages reconcile with display intervals; sparse counts do not establish the exact test. | PASS_1_COMPLETE |
| S603 | p189, GOSE=3 | X25/140 (18%); Y28/133 (21%); P=.5 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S604 | p189, GOSE=4 | X10/140 (7%); Y12/133 (9%); P=.57 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S605 | p189, GOSE=5 | X32/140 (23%); Y30/133 (23%); P=.95 | Percentages reconcile; near-equal displayed proportions do not require an identical P value to other rows. | PASS_1_COMPLETE |
| S606 | p189, GOSE=6 | X15/140 (11%); Y17/133 (13%); P=.6 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S607 | p189, GOSE=7 | X19/140 (14%); Y9/133 (7%); P=.06 | Percentages reconcile; P is nonsignificant and no interval implies otherwise. | PASS_1_COMPLETE |
| S608 | p189, GOSE=8 | X11/140 (8%); Y8/133 (6%); P=.55 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S609 | p189, GOSE score | X4.39 (2.23); Y4.08 (2.11); P=.23 | Frequency-weighted means 4.392857/4.075188 reproduce. Diagnostic sample SDs 2.227030/2.105635 reproduce parenthesized values; dispersion definition absent. | PASS_1_COMPLETE |
| S610 | p189, unfavourable GOSE1–4 | X63/140 (45%); Y69/133 (52%); P=.26 | Category sums 63/69 and percentages reconcile; chart sums match. | PASS_1_COMPLETE |
| S611 | p189, unfavourable survival GOSE2–4 | X36/140 (26%); Y42/133 (32%); P=.28 | Counts equal unfavourable totals less deaths; percentages use all GOSE participants, consistent with displayed values. | PASS_1_COMPLETE |
| S612 | p189, header and group headings | Outcome273; consent refusals7; lost20; X140/Y133; 12 blocks ending300 | 140+133=273 and 273+7+20=300. Mortality/unfavourable block denominators each sum140/133. | PASS_1_COMPLETE |

## December 2015 monitoring: all block and cumulative relationships

M = 180-day mortality; U = unfavourable GOSE1–4; each pair is X then Y. All numerator≤denominator checks reconcile. All bar heights agree with the printed numerator counts. Every block's cumulative contribution is checked in S625.

| S ID | PLAN location/block | M pairs X; Y | U pairs X; Y | Pass 1 |
|---|---|---|---|---|
| S613 | pp189–190, 0–25 | 1/11; 3/13 | 1/11; 6/13 | PASS_1_COMPLETE |
| S614 | pp189–190, 26–50 | 4/14; 0/8 | 6/14; 6/8 | PASS_1_COMPLETE |
| S615 | pp189–190, 51–75 | 3/6; 0/16 | 4/6; 5/16 | PASS_1_COMPLETE |
| S616 | pp189–190, 76–100 | 3/14; 2/10 | 7/14; 5/10 | PASS_1_COMPLETE |
| S617 | pp189–190, 101–125 | 1/13; 1/10 | 4/13; 2/10 | PASS_1_COMPLETE |
| S618 | pp189–190, 126–150 | 1/11; 2/12 | 6/11; 6/12 | PASS_1_COMPLETE |
| S619 | pp189–190, 151–175 | 2/14; 2/8 | 5/14; 5/8 | PASS_1_COMPLETE |
| S620 | pp189–190, 176–200 | 2/11; 3/12 | 4/11; 7/12 | PASS_1_COMPLETE |
| S621 | pp189–190, 201–225 | 2/9; 4/14 | 5/9; 8/14 | PASS_1_COMPLETE |
| S622 | pp189–190, 226–250 | 1/10; 4/12 | 6/10; 7/12 | PASS_1_COMPLETE |
| S623 | pp189–190, 251–275 | 5/14; 4/9 | 11/14; 7/9 | PASS_1_COMPLETE |
| S624 | pp189–190, 276–300 | 2/13; 2/9 | 4/13; 5/9 | PASS_1_COMPLETE |
| S625 | pp189–190, cumulative plots and table | M cumulative X1,5,8,11,12,13,15,17,19,20,25,27; Y3,3,3,5,6,8,10,13,17,21,25,27 | U cumulative X1,7,11,18,22,28,33,37,42,48,59,63; Y6,12,17,22,24,30,35,42,50,57,64,69. Both figures agree with these sums, table outcomes, axes and coding. | PASS_1_COMPLETE |

## July 2016 monitoring: table and population

| S ID | PLAN location | Printed relationship | Pass-1 check and outcome | Pass 1 |
|---|---|---|---|---|
| S626 | p191, GOSE=1 | X34 (20%); Y32 (21%); P=.88 | GOSE denominators168/153 from complete category sums; percentages reconcile. | PASS_1_COMPLETE |
| S627 | p191, GOSE=2 | X1 (1%); Y2 (1%); P=.61 | Percentages reconcile; exact test undefined. | PASS_1_COMPLETE |
| S628 | p191, GOSE=3 | X33 (20%); Y30 (20%); P=.99 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S629 | p191, GOSE=4 | X14 (8%); Y16 (10%); P=.51 | Percentages reconcile including Y10.4575% within 10±.5 display interval. | PASS_1_COMPLETE |
| S630 | p191, GOSE=5 | X36 (21%); Y32 (21%); P=.91 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S631 | p191, GOSE=6 | X16 (10%); Y20 (13%); P=.31 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S632 | p191, GOSE=7 | X22 (13%); Y11 (7%); P=.08 | Percentages reconcile; no interval implying significance supplied. | PASS_1_COMPLETE |
| S633 | p191, GOSE=8 | X12 (7%); Y10 (7%); P=.83 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S634 | p191, GOSE score | X4.27 (2.22); Y4.10 (2.14); P=.49 | Weighted means4.267857/4.098039 reproduce; diagnostic sample SDs2.217171/2.139124 reproduce. | PASS_1_COMPLETE |
| S635 | p191, unfavourable GOSE1–4 | X82 (49%); Y80 (52%); P=.53 | Category sums and percentages reconcile; no reported interval/test conflict. | PASS_1_COMPLETE |
| S636 | p191, favourable GOSE5–8 | X86 (51%); Y73 (48%); P=.53 | Category sums/percentages reconcile; same P for complementary binary outcomes coherent; p192 block counts sum86/73. | PASS_1_COMPLETE |
| S637 | p191, unfavourable survival | X48 (29%); Y48 (31%); P=.58 | 82−34=48 and80−32=48; all-GOSE percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S638 | p191, 180 mortality | X34 (19%); Y32 (20%); P=.78 | Mortality denominators181/160 from block sums;34/181=18.7845%,32/160=20%; distinct GOSE versus survival denominators explicitly disclosed. | PASS_1_COMPLETE |
| S639 | p191, header/footnote |350 enrolled;321 GOSE;7 refusals;22 missing;20/22 missing GOSE known survivors; survival341 |321+7+22=350;321+20=341; GOSE168+153=321; survival181+160=341. Additional13 X and7 Y survivors yield no added deaths. | PASS_1_COMPLETE |

## July 2016 monitoring: all block and cumulative relationships

F = favourable GOSE5–8. Mortality denominators include additional known survivors and can exceed GOSE denominators. All numerator≤denominator checks and bar-height checks reconcile. Cumulative-curve reproduction is checked separately in S654.

| S ID | PLAN location/block | M pairs X; Y | F pairs X; Y | Pass 1 |
|---|---|---|---|---|
| S640 | pp191–192, 0–25 |1/12;3/13|10/11;7/13| PASS_1_COMPLETE |
| S641 | pp191–192, 26–50 |4/14;0/10|8/14;2/8| PASS_1_COMPLETE |
| S642 | pp191–192, 51–75 |3/8;0/16|2/6;11/16| PASS_1_COMPLETE |
| S643 | pp191–192, 76–100 |3/15;2/10|7/14;5/10| PASS_1_COMPLETE |
| S644 | pp191–192, 101–125 |1/14;1/11|9/13;8/10| PASS_1_COMPLETE |
| S645 | pp191–192, 126–150 |1/12;2/12|5/11;6/12| PASS_1_COMPLETE |
| S646 | pp191–192, 151–175 |2/16;2/8|9/14;3/8| PASS_1_COMPLETE |
| S647 | pp191–192, 176–200 |2/12;3/13|7/11;5/12| PASS_1_COMPLETE |
| S648 | pp191–192, 201–225 |2/11;4/14|5/10;6/14| PASS_1_COMPLETE |
| S649 | pp191–192, 226–250 |1/11;4/13|4/10;5/12| PASS_1_COMPLETE |
| S650 | pp191–192, 251–275 |5/14;4/9|3/14;2/9| PASS_1_COMPLETE |
| S651 | pp191–192, 276–300 |2/14;2/10|9/14;4/9| PASS_1_COMPLETE |
| S652 | pp191–192, 301–325 |2/12;4/12|3/10;3/11| PASS_1_COMPLETE |
| S653 | pp191–192, 326–350 |5/16;1/9|5/16;6/9| PASS_1_COMPLETE |
| S654 | pp191–192, cumulative plots/table |Mortality X1,5,8,11,12,13,15,17,19,20,25,27,29,34; Y3,3,3,5,6,8,10,13,17,21,25,27,31,32|Mortality agrees. Favourable X10,18,20,27,36,41,50,57,62,66,69,78,81,86 agrees; favourable Y should7,9,20,25,33,39,42,47,53,58,60,64,67,73. Blue Y curve instead follows approximately6,12,17,22,24,30,35,42,50,57,64,69,77,80, the cumulative unfavourable complements. F-ST1-301. | PASS_1_COMPLETE |

## May 2017 monitoring: table and population

| S ID | PLAN location | Printed relationship | Pass-1 check and outcome | Pass 1 |
|---|---|---|---|---|
| S655 | p193, GOSE=1 |n364; X36 (19.6%);Y35 (19.4%);P=.98|GOSE denominators184/180 from category sums; percentages reconcile.| PASS_1_COMPLETE |
| S656 | p193, GOSE=2 |n364; X1 (.5%);Y2 (1.1%);P=.62|Percentages reconcile; exact test undefined.| PASS_1_COMPLETE |
| S657 | p193, GOSE=3 |n364; X36 (19.6%);Y36 (20.0%);P=.92|Percentages reconcile; different denominators explain proportions despite equal counts.| PASS_1_COMPLETE |
| S658 | p193, GOSE=4 |n364; X16 (8.7%);Y18 (10.0%);P=.67|Percentages reconcile; no inferential contradiction supplied.| PASS_1_COMPLETE |
| S659 | p193, GOSE=5 |n364; X41 (22.3%);Y39 (21.7%);P=.89|Percentages reconcile; no inferential contradiction supplied.| PASS_1_COMPLETE |
| S660 | p193, GOSE=6 |n364; X17 (9.2%);Y24 (13.3%);P=.22|Percentages reconcile; no inferential contradiction supplied.| PASS_1_COMPLETE |
| S661 | p193, GOSE=7 |n364; X24 (13.0%);Y13 (7.2%);P=.07|Percentages reconcile; no interval implying significance supplied.| PASS_1_COMPLETE |
| S662 | p193, GOSE=8 |n364; X13 (7.1%);Y13 (7.2%);P=.95|Percentages reconcile; no inferential contradiction supplied.| PASS_1_COMPLETE |
| S663 | p193, GOSE score |n364;X4.3 (2.2);Y4.2 (2.1);P=.65|Weighted means4.288043/4.183333 reproduce; diagnostic sample SDs2.195044/2.131108 reproduce.| PASS_1_COMPLETE |
| S664 | p193, unfavourable GOSE |n364;X89 (48.4%);Y91 (50.6%);P=.68|Category sums/percentages reconcile; no interval/test conflict.| PASS_1_COMPLETE |
| S665 | p193, unfavourable survival |n364;X53 (28.8%);Y56 (31.1%);P=.63|89−36=53;91−35=56; percentages reconcile using GOSE denominators.| PASS_1_COMPLETE |
| S666 | p193, favourable GOSE |n364;X95 (51.6%);Y89 (49.4%);P=.68|Category sums/percentages reconcile; complementary binary P matches; p194 block counts sum95/89.| PASS_1_COMPLETE |
| S667 | p193, 180-day mortality |n390;X36 (18.0%);Y35 (18.4%);P=.91|Block denominators200/190; percentages reconcile; GOSE/survival distinction explicit.| PASS_1_COMPLETE |
| S668 | p193, header/footnote |400;GOSE364;refusals8;missing28;26/28 known survivors;survival390|364+8+28=400;364+26=390; GOSE184+180=364;survival200+190=390. Additional16 X and10 Y survivors add no deaths.| PASS_1_COMPLETE |

## May 2017 monitoring: all block and cumulative relationships

All numerator≤denominator checks and bar-height checks reconcile. Cumulative summation, population identity and outcome coding are checked in S685.

| S ID | PLAN location/block | M pairs X; Y | F pairs X; Y | Pass 1 |
|---|---|---|---|---|
| S669 | pp193–194, 0–25 |1/12;3/13|10/11;7/13| PASS_1_COMPLETE |
| S670 | pp193–194, 26–50 |4/14;0/10|8/14;2/8| PASS_1_COMPLETE |
| S671 | pp193–194, 51–75 |3/8;0/16|2/6;11/16| PASS_1_COMPLETE |
| S672 | pp193–194, 76–100 |3/15;2/10|7/14;5/10| PASS_1_COMPLETE |
| S673 | pp193–194, 101–125 |1/14;1/11|9/13;8/10| PASS_1_COMPLETE |
| S674 | pp193–194, 126–150 |1/12;2/12|5/11;6/12| PASS_1_COMPLETE |
| S675 | pp193–194, 151–175 |2/16;2/8|9/14;3/8| PASS_1_COMPLETE |
| S676 | pp193–194, 176–200 |2/12;3/13|7/11;5/12| PASS_1_COMPLETE |
| S677 | pp193–194, 201–225 |2/11;4/14|5/10;6/14| PASS_1_COMPLETE |
| S678 | pp193–194, 226–250 |1/11;4/13|4/10;5/12| PASS_1_COMPLETE |
| S679 | pp193–194, 251–275 |5/14;4/9|3/14;2/9| PASS_1_COMPLETE |
| S680 | pp193–194, 276–300 |2/14;2/10|9/14;4/9| PASS_1_COMPLETE |
| S681 | pp193–194, 301–325 |2/12;4/12|3/10;3/11| PASS_1_COMPLETE |
| S682 | pp193–194, 326–350 |5/16;1/9|5/16;6/9| PASS_1_COMPLETE |
| S683 | pp193–194, 351–375 |1/10;0/15|7/10;10/13| PASS_1_COMPLETE |
| S684 | pp193–194, 376–400 |1/9;3/15|2/6;6/14| PASS_1_COMPLETE |
| S685 | pp193–194, cumulative plots/table |Mortality X1,5,8,11,12,13,15,17,19,20,25,27,29,34,35,36;Y3,3,3,5,6,8,10,13,17,21,25,27,31,32,32,35|Favourable X10,18,20,27,36,41,50,57,62,66,69,78,81,86,93,95;Y7,9,20,25,33,39,42,47,53,58,60,64,67,73,83,89. Both figures agree with these sums and table values. p194 Y series agrees with the outcome label.| PASS_1_COMPLETE |

## Limitations and exact handoff

No source units omitted. The named table tests and parenthesized score-dispersion definitions are absent. Their absence supplies no independent finding without a printed contradiction. Cumulative figures have graphical rather than point-label precision; the finding uses a conservative graph-reading interval, separate from the exact source numerator transcription. Final individual-level data and treatment identities are unavailable and were not inferred. No raw-data audit or preferred method is proposed.

All S601–S685 are PASS_1_COMPLETE. Pass-2 records are reserved for a different fresh high-effort statistical agent. Findings: F-ST1-301, one issue/pattern. Excluded observations: one consolidated missing-test-definition observation in `checkers/parts/statistical_monitoring_pass_1.md`.
