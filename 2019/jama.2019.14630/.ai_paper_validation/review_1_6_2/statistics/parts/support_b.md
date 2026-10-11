# Statistical relationship inventory: support shard B, pass 1

Runtime agent: `/root/stat1_support_b`; model: `gpt-6.1-sol`; reasoning effort: `high`; fresh spawn. This shard owns exactly S420, S421, S422 and S534–S640: 110 grouped relationships, including 107 change rows. Every eTable9 row includes both MI and completer analyses. Source role throughout: REPORT, DOC-004, `joi190106supp3_prod_1635377898.49725.pdf`. This is an inventory part for the coordinator's canonical merge.

The complete source-linked arm estimates, intervals, population headers, units and continuations are preserved in `extraction/support_sap_results.md` and the byte-identical reusable `.ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt`. I read source PDF pages 14–24 with all continuation lines and statistical footnotes. eTable5 is completers (I/C 2862/2883 at M6, 2833/2943 at M12); eTables6–8 replace missing observations with baseline (I/C 3272/3311). eTable9 compares MI (3272/3311) and completers (2840/2946). Changes are means with 95% CI from mixed models with site and couple random factors. The eTable9 MI predictor list, outcome-specific imputed percentages and conversion factors were read at p.24. No stated noninferiority, equivalence, interim or stopping claim applies to these displays.

Checks for every table row: containment of both arm estimates and the contrast in their respective intervals; endpoint order; I-minus-C direction and coarse-display subtraction; null inclusion versus printed P at .05; model/population/time/unit matching. All arm and contrast estimates are contained in ordered intervals. Half-unit ranges permit the small printed arm-minus-arm versus contrast differences; these model estimates are not replaced by crude recomputations. Exact P reconstruction is not asserted: denominator degrees of freedom, contrast covariance, variance estimator and exact test implementation are not printed. Normal/Wald approximations were used only as diagnostics to locate issues; no discrepancy dependent on those unreported definitions is emitted. All significant/nonsignificant interval–P classifications reconcile except the two alcohol M6 rows recorded below. No source-grounded contradiction in the stated mixed-model method is reproduced here.

For rows marked `RECONCILES`, the above complete checks produced no qualifying observation. `F-ST1-201` and `F-ST1-202` designate self-screened findings, not adjudications. No Pass 2 review is claimed.

| S ID | Exact source location; quantity | Printed contrast (95% CI); P, or graphical relationship | Pass 1 result | Pass 1 status |
|---|---|---|---|---|
| S420 | DOC-004 p.25 eFigure1, four scores at baseline/M6/M12 | Baseline P .13/.42/.98/.76; all M6/M12 P<.001; colored means and 95% CI | RECONCILES: higher scores favor intervention at follow-up; individual-arm intervals are not contrast intervals | PASS_1_COMPLETE |
| S421 | DOC-004 p.26 eFigure2, seven favorable dietary changes M12 | In-bar I/C percentages 34/32,72/77,79/86,58/63,56/64,60/62,59/58; P .14,<.001,<.001,<.001,<.001,.08,<.001 | F-ST1-202: labels conflict with colored-bar direction and plotted 95% intervals | PASS_1_COMPLETE |
| S422 | DOC-004 p.27 eFigure3, 12 nutrients M6/M12 | Common baseline-SD units, I/C box-and-whisker displays; no printed numerical endpoints or tests | Directions reconcile; whisker rule not specified, no contradictory inferential claim | PASS_1_COMPLETE |
| S534 | DOC-004 p.14 eTable5 SFA M6 | -0.4 (-0.6,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S535 | DOC-004 p.14 eTable5 SFA M12 | -0.4 (-0.5,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S536 | DOC-004 p.14 eTable5 MUFA M6 | 1.2 (0.9,1.4); <.001 | RECONCILES | PASS_1_COMPLETE |
| S537 | DOC-004 p.14 eTable5 MUFA M12 | 0.9 (0.6,1.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S538 | DOC-004 p.15 eTable5 MUFA:SFA M6 | 0.3 (0.2,0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S539 | DOC-004 p.15 eTable5 MUFA:SFA M12 | 0.2 (0.2,0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S540 | DOC-004 p.15 eTable5 PUFA M6 | 0.5 (0.4,0.6); <.001 | RECONCILES | PASS_1_COMPLETE |
| S541 | DOC-004 p.15 eTable5 PUFA M12 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S542 | DOC-004 p.15 eTable5 alcohol %E M6 | -0.2 (-0.4,0); .02 | F-ST1-201: printed CI includes null, P<.05 | PASS_1_COMPLETE |
| S543 | DOC-004 p.15 eTable5 alcohol %E M12 | -0.3 (-0.4,-0.1); .01 | RECONCILES | PASS_1_COMPLETE |
| S544 | DOC-004 p.15 eTable5 fiber M6 | 24 (20,27); <.001 | RECONCILES | PASS_1_COMPLETE |
| S545 | DOC-004 p.15 eTable5 fiber M12 | 19 (16,22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S546 | DOC-004 p.15 eTable5 omega-3 M6 | 0.7 (0.5,0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S547 | DOC-004 p.15 eTable5 omega-3 M12 | 0.7 (0.5,0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S548 | DOC-004 p.15 eTable5 cholesterol M6 | -53 (-93,-13); .009 | RECONCILES | PASS_1_COMPLETE |
| S549 | DOC-004 p.15 eTable5 cholesterol M12 | -12 (-52,29); .58 | RECONCILES | PASS_1_COMPLETE |
| S550 | DOC-004 p.15 eTable5 sodium M6 | -1.2 (-1.5,-0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S551 | DOC-004 p.15 eTable5 sodium M12 | -1.3 (-1.7,-1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S552 | DOC-004 p.16 eTable6 er-MedDiet M6 | 2.1 (2,2.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S553 | DOC-004 p.16 eTable6 er-MedDiet M12 | 2.0 (1.9,2.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S554 | DOC-004 p.16 eTable6 MDS M6 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S555 | DOC-004 p.16 eTable6 MDS M12 | 0.4 (0.4,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S556 | DOC-004 p.16 eTable6 MEDAS M6 | 1.0 (0.9,1.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S557 | DOC-004 p.16 eTable6 MEDAS M12 | 0.9 (0.8,1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S558 | DOC-004 p.16 eTable6 PDQS M6 | 2.1 (1.9,2.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S559 | DOC-004 p.16 eTable6 PDQS M12 | 1.9 (1.7,2.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S560 | DOC-004 p.17 eTable7 olive oil M6 | -3 (-9,3); .27 | RECONCILES | PASS_1_COMPLETE |
| S561 | DOC-004 p.17 eTable7 olive oil M12 | -7 (-13,-2); .01 | RECONCILES | PASS_1_COMPLETE |
| S562 | DOC-004 p.17 eTable7 refined olive oil M6 | -1 (-5,4); .72 | RECONCILES | PASS_1_COMPLETE |
| S563 | DOC-004 p.17 eTable7 refined olive oil M12 | 3 (-2,7); .26 | RECONCILES | PASS_1_COMPLETE |
| S564 | DOC-004 p.17 eTable7 EVOO M6 | -3 (-9,4); .47 | RECONCILES | PASS_1_COMPLETE |
| S565 | DOC-004 p.17 eTable7 EVOO M12 | -10 (-17,-3); .004 | RECONCILES | PASS_1_COMPLETE |
| S566 | DOC-004 p.17 eTable7 nuts M6 | 43 (36,51); <.001 | RECONCILES | PASS_1_COMPLETE |
| S567 | DOC-004 p.17 eTable7 nuts M12 | 28 (20,35); <.001 | RECONCILES | PASS_1_COMPLETE |
| S568 | DOC-004 p.17 eTable7 fruits M6 | 162 (92,233); <.001 | RECONCILES | PASS_1_COMPLETE |
| S569 | DOC-004 p.17 eTable7 fruits M12 | 154 (83,224); <.001 | RECONCILES | PASS_1_COMPLETE |
| S570 | DOC-004 p.17 eTable7 vegetables M6 | 171 (124,218); <.001 | RECONCILES | PASS_1_COMPLETE |
| S571 | DOC-004 p.17 eTable7 vegetables M12 | 169 (121,216); <.001 | RECONCILES | PASS_1_COMPLETE |
| S572 | DOC-004 p.17 eTable7 cereals M6 | -82 (-108,-55); <.001 | RECONCILES | PASS_1_COMPLETE |
| S573 | DOC-004 p.17 eTable7 cereals M12 | -96 (-123,-70); <.001 | RECONCILES | PASS_1_COMPLETE |
| S574 | DOC-004 p.18 eTable7 whole grains M6 | 184 (160,208); <.001 | RECONCILES | PASS_1_COMPLETE |
| S575 | DOC-004 p.18 eTable7 whole grains M12 | 141 (117,165); <.001 | RECONCILES | PASS_1_COMPLETE |
| S576 | DOC-004 p.18 eTable7 refined grains M6 | -303 (-332,-273); <.001 | RECONCILES | PASS_1_COMPLETE |
| S577 | DOC-004 p.18 eTable7 refined grains M12 | -264 (-294,-235); <.001 | RECONCILES | PASS_1_COMPLETE |
| S578 | DOC-004 p.18 eTable7 legumes M6 | 19 (15,23); <.001 | RECONCILES | PASS_1_COMPLETE |
| S579 | DOC-004 p.18 eTable7 legumes M12 | 17 (13,22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S580 | DOC-004 p.18 eTable7 fish M6 | 55 (40,71); <.001 | RECONCILES | PASS_1_COMPLETE |
| S581 | DOC-004 p.18 eTable7 fish M12 | 63 (47,79); <.001 | RECONCILES | PASS_1_COMPLETE |
| S582 | DOC-004 p.18 eTable7 meat M6 | -25 (-42,-8); .01 | RECONCILES | PASS_1_COMPLETE |
| S583 | DOC-004 p.18 eTable7 meat M12 | -9 (-26,8); .31 | RECONCILES | PASS_1_COMPLETE |
| S584 | DOC-004 p.18 eTable7 red meat M6 | -40 (-51,-30); <.001 | RECONCILES | PASS_1_COMPLETE |
| S585 | DOC-004 p.18 eTable7 red meat M12 | -33 (-43,-22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S586 | DOC-004 p.18 eTable7 processed meat M6 | -17 (-24,-10); <.001 | RECONCILES | PASS_1_COMPLETE |
| S587 | DOC-004 p.18 eTable7 processed meat M12 | -9 (-16,-1); .02 | RECONCILES | PASS_1_COMPLETE |
| S588 | DOC-004 p.18 eTable7 pastries M6 | -52 (-61,-43); <.001 | RECONCILES | PASS_1_COMPLETE |
| S589 | DOC-004 p.18 eTable7 pastries M12 | -39 (-48,-30); <.001 | RECONCILES | PASS_1_COMPLETE |
| S590 | DOC-004 p.19 eTable7 dairy M6 | 144 (83,205); <.001 | RECONCILES | PASS_1_COMPLETE |
| S591 | DOC-004 p.19 eTable7 dairy M12 | 137 (76,198); <.001 | RECONCILES | PASS_1_COMPLETE |
| S592 | DOC-004 p.19 eTable7 yogurt M6 | 95 (69,122); <.001 | RECONCILES | PASS_1_COMPLETE |
| S593 | DOC-004 p.19 eTable7 yogurt M12 | 81 (54,107); <.001 | RECONCILES | PASS_1_COMPLETE |
| S594 | DOC-004 p.19 eTable7 fermented dairy M6 | 89 (61,117); <.001 | RECONCILES | PASS_1_COMPLETE |
| S595 | DOC-004 p.19 eTable7 fermented dairy M12 | 76 (49,104); <.001 | RECONCILES | PASS_1_COMPLETE |
| S596 | DOC-004 p.19 eTable7 low-fat dairy M6 | 228 (170,285); <.001 | RECONCILES | PASS_1_COMPLETE |
| S597 | DOC-004 p.19 eTable7 low-fat dairy M12 | 234 (177,292); <.001 | RECONCILES | PASS_1_COMPLETE |
| S598 | DOC-004 p.19 eTable7 whole-fat dairy M6 | -49 (-78,-20); .001 | RECONCILES | PASS_1_COMPLETE |
| S599 | DOC-004 p.19 eTable7 whole-fat dairy M12 | -44 (-72,-15); .003 | RECONCILES | PASS_1_COMPLETE |
| S600 | DOC-004 p.19 eTable7 alcohol g/week M6 | -6 (-10,-3); .001 | RECONCILES | PASS_1_COMPLETE |
| S601 | DOC-004 p.19 eTable7 alcohol g/week M12 | -7 (-10,-3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S602 | DOC-004 p.19 eTable7 red wine M6 | -1 (-3,1); .36 | RECONCILES | PASS_1_COMPLETE |
| S603 | DOC-004 p.19 eTable7 red wine M12 | -1 (-3,1); .36 | RECONCILES | PASS_1_COMPLETE |
| S604 | DOC-004 p.21 eTable8 energy M6 | -85 (-108,-61); <.001 | RECONCILES | PASS_1_COMPLETE |
| S605 | DOC-004 p.21 eTable8 energy M12 | -88 (-111,-64); <.001 | RECONCILES | PASS_1_COMPLETE |
| S606 | DOC-004 p.21 eTable8 protein M6 | 0.9 (0.8,1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S607 | DOC-004 p.21 eTable8 protein M12 | 0.9 (0.8,1.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S608 | DOC-004 p.21 eTable8 carbohydrate M6 | -1.3 (-1.6,-1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S609 | DOC-004 p.21 eTable8 carbohydrate M12 | -1.2 (-1.5,-0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S610 | DOC-004 p.21 eTable8 fat M6 | 0.6 (0.3,0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S611 | DOC-004 p.21 eTable8 fat M12 | 0.4 (0.1,0.8); .006 | RECONCILES | PASS_1_COMPLETE |
| S612 | DOC-004 p.21 eTable8 SFA M6 | -0.4 (-0.5,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S613 | DOC-004 p.21 eTable8 SFA M12 | -0.3 (-0.4,-0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S614 | DOC-004 p.21 eTable8 MUFA M6 | 1.0 (0.8,1.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S615 | DOC-004 p.21 eTable8 MUFA M12 | 0.7 (0.5,1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S616 | DOC-004 p.22 eTable8 MUFA:SFA M6 | 0.2 (0.2,0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S617 | DOC-004 p.22 eTable8 MUFA:SFA M12 | 0.2 (0.1,0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S618 | DOC-004 p.22 eTable8 PUFA M6 | 0.5 (0.4,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S619 | DOC-004 p.22 eTable8 PUFA M12 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S620 | DOC-004 p.22 eTable8 alcohol %E M6 | -0.2 (-0.3,0); .02 | F-ST1-201: printed CI includes null, P<.05 | PASS_1_COMPLETE |
| S621 | DOC-004 p.22 eTable8 alcohol %E M12 | -0.2 (-0.3,-0.1); .01 | RECONCILES | PASS_1_COMPLETE |
| S622 | DOC-004 p.22 eTable8 fiber M6 | 21 (18,24); <.001 | RECONCILES | PASS_1_COMPLETE |
| S623 | DOC-004 p.22 eTable8 fiber M12 | 16 (13,19); <.001 | RECONCILES | PASS_1_COMPLETE |
| S624 | DOC-004 p.22 eTable8 omega-3 M6 | 0.6 (0.4,0.7); <.001 | RECONCILES | PASS_1_COMPLETE |
| S625 | DOC-004 p.22 eTable8 omega-3 M12 | 0.6 (0.4,0.7); <.001 | RECONCILES | PASS_1_COMPLETE |
| S626 | DOC-004 p.22 eTable8 cholesterol M6 | -44 (-79,-8); .02 | RECONCILES | PASS_1_COMPLETE |
| S627 | DOC-004 p.22 eTable8 cholesterol M12 | -6 (-41,30); .75 | RECONCILES | PASS_1_COMPLETE |
| S628 | DOC-004 p.22 eTable8 sodium M6 | -1.1 (-1.4,-0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S629 | DOC-004 p.22 eTable8 sodium M12 | -1.1 (-1.4,-0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S630 | DOC-004 p.23 eTable9 weight M12, MI / completers | -2.9 (-3.2,-2.6),<.001 / -3.1 (-3.4,-2.7),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S631 | DOC-004 p.23 eTable9 waist M12, MI / completers | -3.3 (-3.6,-2.9),<.001 / -3.3 (-3.7,-3.0),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S632 | DOC-004 p.23 eTable9 BMI M12, MI / completers | -1.1 (-1.2,-1.0),<.001 / -1.1 (-1.3,-1.0),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S633 | DOC-004 p.23 eTable9 cholesterol M12, MI / completers | -1.1 (-2.9,0.7),.23 / -1.1 (-2.8,0.7),.24 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S634 | DOC-004 p.23 eTable9 LDL M12, MI / completers | -0.6 (-2.2,1.0),.48 / -0.6 (-2.2,1.0),.45 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S635 | DOC-004 p.23 eTable9 HDL M12, MI / completers | 1.1 (0.7,1.6),<.001 / 1.3 (0.8,1.7),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S636 | DOC-004 p.24 eTable9 nonHDL M12, MI / completers | -1.9 (-3.6,-0.3),.02 / -2.5 (-4.2,-0.8),.004 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S637 | DOC-004 p.24 eTable9 cholesterol:HDL M12, MI / completers | -0.1 (-0.2,-0.1),<.001 / -0.1 (-0.2,-0.1),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S638 | DOC-004 p.24 eTable9 triglycerides M12, MI / completers | -9.9 (-13.6,-6.3),<.001 / -10.4 (-14,-6.9),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S639 | DOC-004 p.24 eTable9 SBP M12, MI / completers | -1.9 (-2.7,-1.1),<.001 / -1.7 (-2.6,-0.9),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S640 | DOC-004 p.24 eTable9 DBP M12, MI / completers | -1 (-1.4,-0.5),<.001 / -1.0 (-1.5,-0.6),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |

Limitations: individual graphical endpoints are not printed; visual bounds in the checker are deliberately conservative diagnostic readings of the source axes, not digitized numerical estimates. Unreported degrees of freedom, covariance and exact variance/test implementation prevent exact reconstruction of every P value; this limitation does not excuse the unconditional printed CI–P conflict. No scientific scope gap remains in this shard.
