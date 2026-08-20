# Statistical consistency review — pass 2

## Independent pass-2 scope and evidence boundary

This fresh pass-2 review revisited every canonical statistical relationship `S001` through `S777` in `statistics/relationship_inventory.md` after the complete cross-lane stable-candidate ledger (`C001`-`C008`) and the mechanical evidence recheck were available. It used the supplied PDFs as authority, with current source-matched mappings and page-preserving text only as locators/transcription aids. No legacy scientific output was used.

For each relationship, the checks were: denominator/population and time/contrast identity; arithmetic only where the source establishes an arithmetic identity; point-estimate containment; ordered interval endpoints; sign/direction; effect-measure, unit, scale, reference-group, and duplicate-value labels; matched cross-location repetitions; and recheck implications. Interval/P-value/test/statistic/SE compatibility was checked only where the printed source supplied a two-sided mixed-effects comparison, 95% CI, and P value. The source does not supply contrast-specific SEs, test statistics, degrees of freedom, covariance, variance estimator, sidedness for the SAP screening table, or an estimate-to-P calculation rule; none was inferred or reverse engineered.

`S001`-`S777` are partitioned into the seven deterministic pass-2 shards below. Every range denotes every zero-padded integer ID in its inclusive interval, with no omitted member; the counts sum to 777. This is an explicit `PASS_2_COMPLETE` record for every individual S ID.

| Pass-2 shard | Exact canonical membership | Count | Direct-source scope revisited | Result |
|---|---|---:|---|---|
| P2-001 | S001-S120 | 120 | DOC-001 pp.4-10; DOC-003 p.14; DOC-004 pp.2-7 | `PASS_2_COMPLETE` |
| P2-002 | S121-S240 | 120 | DOC-004 pp.3-10 | `PASS_2_COMPLETE` |
| P2-003 | S241-S360 | 120 | DOC-004 pp.10-13 | `PASS_2_COMPLETE` |
| P2-004 | S361-S480 | 120 | DOC-004 pp.13-16 | `PASS_2_COMPLETE` |
| P2-005 | S481-S600 | 120 | DOC-004 pp.16-19 | `PASS_2_COMPLETE` |
| P2-006 | S601-S720 | 120 | DOC-004 pp.19-24 | `PASS_2_COMPLETE` |
| P2-007 | S721-S777 | 57 | DOC-004 pp.23-27 | `PASS_2_COMPLETE` |

## Canonical-record pass-2 register

The fixed record definitions and tuple order in the inventory were retained. The following register maps every atomic S ID to the exact source block and records the pass-2 outcome. A listed range includes every individual ID in the interval.

| Canonical IDs | Count | Pass-2 checks and outcome |
|---|---:|---|
| S001 | 1 | Main-model definition rechecked: three-level mixed-effects linear model, site/participant/cluster-family random intercepts, two-sided tests, and no secondary type-I adjustment. Compatible model scope is supplied; SE, statistic, degrees of freedom, covariance, and variance estimator are not. `PASS_2_COMPLETE`. |
| S002-S009 | 8 | Main Table 2 score contrasts: estimate containment, ordered 95% CI, higher-is-better direction, score ranges, population/time/contrast labels, repetitions, and two-sided CI/P coherence rechecked. No new inconsistency. `PASS_2_COMPLETE`. |
| S010 | 1 | Contextual HRs retain estimates within ordered CIs and the sub-1 direction; they are not trial contrasts. `PASS_2_COMPLETE`. |
| S011 | 1 | The reported 55% relative score increase remains directionally compatible with the 12-month score result. Calculation and uncertainty definitions are absent, so no diagnostic reconstruction was treated as a contradiction test. `PASS_2_COMPLETE`. |
| S012-S016 | 5 | Narrative food contrasts retain contained, ordered CIs, stated direction, g/week labels, and matched eTable 2 repetitions. `PASS_2_COMPLETE`. |
| S017-S042 | 26 | Main Table 3 contrasts retain contained ordered CIs, signed intervention-minus-control direction, nutrient units/scales, and two-sided CI/P display coherence. No raw subtraction of rounded group summaries was imposed on modelled contrasts. `PASS_2_COMPLETE`. |
| S043 | 1 | Main narrative repetitions of energy, carbohydrate, and MUFA match Table 3 at printed precision after matched population/time/model. `PASS_2_COMPLETE`. |
| S044-S054 | 11 | Figure 4 percentages lie in ordered CIs and P labels are directionally coherent. The established Methods-versus-figure boundary-label observation remains C008; it is not expanded into a new numeric claim. `PASS_2_COMPLETE`. |
| S055 | 1 | Explicit waist/SBP narrative repetitions match the MI eTable 9 panel. The broad narrative lacks values for further exact reconciliation. `PASS_2_COMPLETE`. |
| S056-S068 | 13 | Protocol/SAP definitions, targets, populations, and historical model wording rechecked. Planned assumptions were not treated as comparators for observed results without a shared estimand, population, time, and model. `PASS_2_COMPLETE`. |
| S069-S088 | 20 | SAP screening comparisons rechecked for printed group labels, sign, scale, and P display. Test, sidedness, model, and variance definitions are not supplied, so no inferential reconstruction was made. `PASS_2_COMPLETE`. |
| S089-S092 | 4 | eTable 1 score ranges, scoring rules, and higher-is-better labels agree with the main table and eFigure 1. `PASS_2_COMPLETE`. |
| S093 | 1 | eTable 2 structural model/population/unit/header/baseline conventions rechecked. C001-C003 already capture the distinct header, IQR-order, and cross-table baseline discrepancies. No additional distinct contradiction. `PASS_2_COMPLETE`. |
| S094-S225 | 132 | eTable 2 food-result tuples rechecked: each printed point lies in an ordered CI; contrast signs agree with group-change direction to display precision; g/week, MI all-randomized population, and mixed-effects labels are retained; P/CI coherence is compatible with supplied two-sided convention. `PASS_2_COMPLETE`. |
| S226 | 1 | eTable 3 completer populations, time-specific denominators, marked er-MedDiet analysis counts, scales, and mixed-effects labels rechecked; the marked counts are explicitly distinct rather than a duplicate-value contradiction. `PASS_2_COMPLETE`. |
| S227-S250 | 24 | eTable 3 score tuples rechecked for containment, endpoint order, direction, scale, population, and CI/P coherence. `PASS_2_COMPLETE`. |
| S251 | 1 | eTable 4 structural labels rechecked. One new label conflict is recorded separately as QC-S2-001: the total-olive-oil baseline row says mean (SD) whereas the table footnote states food baselines are median (IQR). All other structural labels are compatible. `PASS_2_COMPLETE`. |
| S252-S383 | 132 | eTable 4 food-result tuples rechecked for containment, endpoint order, signed direction, g/week unit, completer denominators, model label, and CI/P coherence. No further distinct contradiction. `PASS_2_COMPLETE`. |
| S384 | 1 | eTable 5 completer population, units, baseline summary conventions, contrast label, and model definition rechecked. `PASS_2_COMPLETE`. |
| S385-S462 | 78 | eTable 5 nutrient tuples rechecked for containment, endpoint order, direction, units/scales, population, and CI/P coherence. `PASS_2_COMPLETE`. |
| S463 | 1 | eTable 6 all-randomized baseline-value-replacement population, imputation label, score ranges, and model definition rechecked. C004 is the separate cross-location PDQS baseline discrepancy. `PASS_2_COMPLETE`. |
| S464-S487 | 24 | eTable 6 score tuples rechecked for containment, endpoint order, direction, scale, and CI/P coherence. `PASS_2_COMPLETE`. |
| S488 | 1 | eTable 7 all-randomized baseline-value-replacement population, unit, and model labels rechecked. C003 remains the separate eTable 2/eTable 7 red-wine baseline comparison. `PASS_2_COMPLETE`. |
| S489-S620 | 132 | eTable 7 food tuples rechecked for containment, endpoint order, signed direction, g/week unit, population/model labels, and CI/P coherence. `PASS_2_COMPLETE`. |
| S621 | 1 | eTable 8 all-randomized baseline-value-replacement population, units, and model labels rechecked. C005 remains the separate main-Table-3/eTable-8 intervention-energy-SD comparison. `PASS_2_COMPLETE`. |
| S622-S699 | 78 | eTable 8 nutrient tuples rechecked for containment, endpoint order, direction, units/scales, and CI/P coherence. `PASS_2_COMPLETE`. |
| S700 | 1 | eTable 9 MI/completer populations, imputation predictors/percentages, unit/conversion labels, baseline versus change columns, and model definition rechecked. C006 and C007 remain the separate matched-main-table weight/BMI baseline comparisons. `PASS_2_COMPLETE`. |
| S701-S766 | 66 | eTable 9 risk-factor tuples rechecked for containment, endpoint order, signed direction, unit/rate/count distinction, population label, and CI/P coherence. `PASS_2_COMPLETE`. |
| S767 | 1 | eFigure 1 ranges, higher-is-better direction, and P-label definition agree with its matching score tables. `PASS_2_COMPLETE`. |
| S768-S775 | 8 | eFigure 1 P labels are directionally coherent with the table results. Point/CI coordinates are graphical and not printed; no numerical values were inferred. `PASS_2_COMPLETE`. |
| S776 | 1 | eFigure 2 percentage-comparison P-label definition and MUFA/MUFA:SFA labels rechecked. The graphical intervention values/denominators are not reliably supplied, so no unsupported arithmetic was applied. `PASS_2_COMPLETE`. |
| S777 | 1 | eFigure 3 baseline-SD scale and nutritional-variable labels rechecked against nutrient tables; graphical marker/CI coordinates are not printed. `PASS_2_COMPLETE`. |

## Cross-lane ledger and mechanical-recheck implications

All stable IDs were revisited as evidence inputs only; no disposition, validity, severity, acceptance, rejection, or correction is assigned here.

| Stable ID | Related S relationship(s) | Pass-2 implication |
|---|---|---|
| C001 | S093 | Direct PDF header comparison remains a distinct group-label conflict; it does not establish an effect-estimate recalculation error. |
| C002 | S093; S094-S225 | The direct median/IQR ordering contradiction remains confined to the eTable 2 intervention red-wine baseline display. |
| C003 | S093, S488 | The two all-randomized red-wine baseline displays remain numerically different at printed precision; the supplied PDFs do not give row-specific baseline denominators or a rule resolving the comparison. |
| C004 | S009, S463 | The matched PDQS baseline displays remain 21.1 versus 21.0 with unchanged printed group Ns and scale; unrounded values/baseline handling are unavailable. |
| C005 | S017, S621 | The intervention baseline energy SD remains 555 versus 544 while matched control values agree; source lacks row-specific baseline calculation inputs. |
| C006 | S700 | The main/eTable 9 baseline weight summaries remain different under matched printed arm Ns; outcome-specific baseline denominator/handling is unavailable. |
| C007 | S700 | The main/eTable 9 baseline BMI means remain different under matched printed arm Ns; derivation, denominator, and rounding path are unavailable. |
| C008 | S044-S054 | The Methods inclusive thresholds versus Figure 4 strict/omitted operator labels remain a label-boundary issue; no individual boundary-case counts or implemented operator are supplied. |

## Newly emitted pass-2 candidate

### QC-S2-001 — eTable 4 labels total-olive-oil baseline as mean (SD) despite its median (IQR) table convention

- **Provisional category:** Measure, label, or scale inconsistency.
- **Canonical relationship:** S251 (eTable 4 structural definition; the label applies to the first food-row baseline display).
- **Exact source locations:** DOC-004, `joi190106supp3_prod_1635377898.49725.pdf#page=10`, Supplemental eTable 4, Total olive oil (g/week), baseline row; comparator in the same table on `#page=11`, footnote `Baseline data are median (IQR)`. The matching food-table baseline convention is also printed in eTable 2, `#page=3`, and eTable 7, `#page=17`.
- **Direct observation:** eTable 4 p.10 prints the total-olive-oil row label `Baseline, mean (SD)` beside `350 (175, 350)` in both arms. Its continuing p.11 footnote defines the table's baseline data as `median (IQR)`. The other food baseline rows in the same eTable use `Baseline, median (IQR)` or its line-wrapped equivalent.
- **Rule:** Within one table, a row-level summary label must agree with the table footnote that defines the same baseline food summaries. Mean (SD) and median (IQR) are different summary measures and cannot both define the same displayed parenthetical values without an explicit row-specific exception.
- **Diagnostic:** The values `350 (175, 350)` have the same printed form as the matching olive-oil median (IQR) displays in eTable 2 and eTable 7. That cross-location comparison supports a labelling observation only; it does not identify the intended raw-data summary or reconstruct an analysis.
- **Exact missing definition:** The source supplies no row-specific exception stating that total olive oil alone uses mean (SD), no calculation output, and no participant-level values.
- **Human question:** Was the eTable 4 total-olive-oil baseline intended to be labelled median (IQR), or does a source-supported row-specific mean (SD) rule exist?

## Display-zero treatment and limitations

- No `P = 0`, `p = 0.000`, or equivalent finite-precision display zero occurs in S001-S777. Therefore `DISPLAY_ZERO_NOT_CANDIDATE` is not required for an individual record, and no candidate was generated from P-value notation.
- P values printed as `<0.001` are finite reporting bounds, not display-zero claims. No tiny tail probability was derived.
- The source provides no contrast-specific SE, statistic, degrees of freedom, covariance, variance estimator, multiplicity mapping, or CI-to-P computational definition for the mixed-model table effects. CI/P compatibility was limited to the supplied two-sided 95%-CI/P display convention and ordinary finite display rounding.
- The SAP screening table lacks a stated test, sidedness, model, and variance definition. Its P values were not reverse engineered.
- Figure coordinates and some eFigure labels are graphical rather than printed numerical source values; no coordinates, denominators, or effects were invented.
- Planned/historical protocol and SAP parameters are not observed 12-month estimates without a stated matching population, estimand, time, and model.

**Pass-2 result:** 777 canonical relationships `PASS_2_COMPLETE`; 8 stable candidates revisited; 1 genuinely new preliminary candidate (`QC-S2-001`); 0 display-zero candidates.

## Exact atomic pass-2 completion index

S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140, S141, S142, S143, S144, S145, S146, S147, S148, S149, S150, S151, S152, S153, S154, S155, S156, S157, S158, S159, S160, S161, S162, S163, S164, S165, S166, S167, S168, S169, S170, S171, S172, S173, S174, S175, S176, S177, S178, S179, S180, S181, S182, S183, S184, S185, S186, S187, S188, S189, S190, S191, S192, S193, S194, S195, S196, S197, S198, S199, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271, S272, S273, S274, S275, S276, S277, S278, S279, S280, S281, S282, S283, S284, S285, S286, S287, S288, S289, S290, S291, S292, S293, S294, S295, S296, S297, S298, S299, S300, S301, S302, S303, S304, S305, S306, S307, S308, S309, S310, S311, S312, S313, S314, S315, S316, S317, S318, S319, S320, S321, S322, S323, S324, S325, S326, S327, S328, S329, S330, S331, S332, S333, S334, S335, S336, S337, S338, S339, S340, S341, S342, S343, S344, S345, S346, S347, S348, S349, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S395, S396, S397, S398, S399, S400, S401, S402, S403, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419, S420, S421, S422, S423, S424, S425, S426, S427, S428, S429, S430, S431, S432, S433, S434, S435, S436, S437, S438, S439, S440, S441, S442, S443, S444, S445, S446, S447, S448, S449, S450, S451, S452, S453, S454, S455, S456, S457, S458, S459, S460, S461, S462, S463, S464, S465, S466, S467, S468, S469, S470, S471, S472, S473, S474, S475, S476, S477, S478, S479, S480, S481, S482, S483, S484, S485, S486, S487, S488, S489, S490, S491, S492, S493, S494, S495, S496, S497, S498, S499, S500, S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533, S534, S535, S536, S537, S538, S539, S540, S541, S542, S543, S544, S545, S546, S547, S548, S549, S550, S551, S552, S553, S554, S555, S556, S557, S558, S559, S560, S561, S562, S563, S564, S565, S566, S567, S568, S569, S570, S571, S572, S573, S574, S575, S576, S577, S578, S579, S580, S581, S582, S583, S584, S585, S586, S587, S588, S589, S590, S591, S592, S593, S594, S595, S596, S597, S598, S599, S600, S601, S602, S603, S604, S605, S606, S607, S608, S609, S610, S611, S612, S613, S614, S615, S616, S617, S618, S619, S620, S621, S622, S623, S624, S625, S626, S627, S628, S629, S630, S631, S632, S633, S634, S635, S636, S637, S638, S639, S640, S641, S642, S643, S644, S645, S646, S647, S648, S649, S650, S651, S652, S653, S654, S655, S656, S657, S658, S659, S660, S661, S662, S663, S664, S665, S666, S667, S668, S669, S670, S671, S672, S673, S674, S675, S676, S677, S678, S679, S680, S681, S682, S683, S684, S685, S686, S687, S688, S689, S690, S691, S692, S693, S694, S695, S696, S697, S698, S699, S700, S701, S702, S703, S704, S705, S706, S707, S708, S709, S710, S711, S712, S713, S714, S715, S716, S717, S718, S719, S720, S721, S722, S723, S724, S725, S726, S727, S728, S729, S730, S731, S732, S733, S734, S735, S736, S737, S738, S739, S740, S741, S742, S743, S744, S745, S746, S747, S748, S749, S750, S751, S752, S753, S754, S755, S756, S757, S758, S759, S760, S761, S762, S763, S764, S765, S766, S767, S768, S769, S770, S771, S772, S773, S774, S775, S776, S777. Every listed relationship is `PASS_2_COMPLETE`.
