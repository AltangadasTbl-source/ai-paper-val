# Statistical consistency review — pass 1

## Completed scope

This pass independently reviewed canonical relationships `S001`-`S777` in `.ai_paper_validation/review_1_5_1/statistics/relationship_inventory.md`: all 55 assigned main-paper relationships and 722 support-table/definition/figure relationships. The support result-table relationships are individually defined in the inventory's fixed tuple ordering and have no gaps or unallocated IDs.

Checks applied where the direct source supplied the needed definitions were point-estimate containment, interval endpoint ordering, sign/direction, effect-measure/unit/scale labels, population/time/contrast identity, and repeated-location agreement. CI/P compatibility was assessed only for the two-sided mixed-effects results that printed 95% CIs and P values, with ordinary display rounding allowed. Test-statistic/SE calculations were not attempted where source definitions were absent.

## Non-candidate coverage observations

- All reviewed CIs have their displayed point estimate within ordered endpoints, except no point estimate is printed for graphical eFigure marks.
- For the two-sided mixed-effects differences, printed P values below .05 coincide with CIs excluding zero and P values at or above .05 coincide with CIs including zero, within display precision.
- Main-text/abstract/table repetitions of the primary score, selected food results, energy/nutrient results, waist, and systolic BP agree at their printed precision after matching population, time, and model.
- No coherent finite-precision P display zero was found. Accordingly, no candidate concerns a literal `P = 0` or equivalent notation.

## Preliminary candidates for coordinator registration

These are preliminary pass-1 observations only. They have no `C` IDs and remain pending human adjudication. The coordinator should merge only genuine duplicates with other lanes before stable candidate registration.

### QC-S001 — eTable 2 second treatment-group header conflicts with its group identity

- **Provisional category:** Measure, label, or scale inconsistency.
- **Canonical relationship:** S093.
- **Exact source locations:** `DOC-004`, `joi190106supp3_prod_1635377898.49725.pdf#page=3`, Supplemental eTable 2 header; comparator in the same table continuation `#page=7` and main Table 2/3 in `DOC-001` `jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5`/`#page=7`.
- **Direct observation:** On eTable 2 p.3, the columns read “Intervention group N=3,272” and “Intervention group N=3,311.” The later continuation prints the N=3,311 column as “Control group,” and the main article consistently identifies the N=3,311 group as control.
- **Rule:** For the same two-arm result table, a group column's printed label must identify the population denoted by its displayed denominator; a repeated N=3,311 control column cannot simultaneously be labelled intervention without an explicit differing population definition.
- **Diagnostic:** The between-group differences in eTable 2 are directionally compatible with intervention minus the N=3,311 column, supporting a header-label issue rather than a recalculation claim. This is diagnostic reasoning, not a reconstructed analysis.
- **Human question:** Is “Intervention group” above N=3,311 an uncorrected column-heading label, or does an authoritative source define a distinct N=3,311 intervention analysis population for p.3?

### QC-S002 — printed red-wine baseline median lies outside its printed IQR

- **Provisional category:** Numeric or arithmetic inconsistency.
- **Canonical relationship:** S093 (eTable 2 structural/baseline display; linked to the red-wine effect tuples within S094-S225).
- **Exact source location:** `DOC-004`, `joi190106supp3_prod_1635377898.49725.pdf#page=7`, Supplemental eTable 2, Red wine (g/week), intervention baseline.
- **Direct observation:** The table labels baseline data as “median (IQR)” and prints intervention red wine as `33 (0, 29)`.
- **Rule:** With an IQR reported as lower quartile and upper quartile, the printed median must satisfy lower quartile <= median <= upper quartile. Here `0 <= 33 <= 29` is false.
- **Diagnostic:** This check uses only the stated median/IQR display convention; it does not infer the intended median or alter the printed value.
- **Human question:** Should the median, an IQR endpoint, or the row alignment be corrected in the source table?

### QC-S003 — Figure 4 threshold labels use strict inequalities while Methods defines inclusive thresholds

- **Provisional category:** Measure, label, or scale inconsistency.
- **Canonical relationships:** S044-S054.
- **Exact source locations:** `DOC-001`, `jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4`, Outcomes; and `#page=10`, Figure 4.
- **Direct observation:** Methods defines clinically meaningful reductions as “at least 5%” for BMI, weight, waist, total/LDL/non-HDL cholesterol, and cholesterol:HDL ratio; “at least 5 mm Hg” systolic and “at least 2.5 mm Hg” diastolic; and “at least 5%” HDL increase. Figure 4 labels the corresponding categories `Reduction >5%`, `Increase >5%`, `Reduction >5 mm Hg`, and `Reduction 2.5 mm Hg`.
- **Rule:** A reporting label should preserve the stated boundary operator for the same clinically meaningful-change outcome. `At least` is inclusive, while `>` is strict; the diastolic label also omits an explicit operator.
- **Diagnostic:** The evidence does not establish whether any participant had exactly the threshold value, so this observation does not claim that a reported percentage is numerically wrong.
- **Human question:** Which threshold operator was used to classify Figure 4 participants, and should the Methods or figure labels be harmonized?

## Missing definitions and limitations

- No source-supplied SE, test statistic, degrees of freedom, covariance structure, variance estimator, or contrast-specific multiplicity adjustment allowed exact recomputation of table P values from CIs.
- The source does not define the calculation or uncertainty propagation for the 55% relative score increase, so an approximate ratio calculation was not used as a contradiction test.
- SAP planned values and historical protocol values were not treated as observed paper results without exact population/estimand/model matching.
- eFigure coordinate labels that are only graphical were not converted to invented exact numeric effects.

**Pass-1 result:** 777 canonical relationships complete; 3 preliminary candidates; 0 display-zero P-value candidates.

## Exact atomic pass-1 completion index

S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140, S141, S142, S143, S144, S145, S146, S147, S148, S149, S150, S151, S152, S153, S154, S155, S156, S157, S158, S159, S160, S161, S162, S163, S164, S165, S166, S167, S168, S169, S170, S171, S172, S173, S174, S175, S176, S177, S178, S179, S180, S181, S182, S183, S184, S185, S186, S187, S188, S189, S190, S191, S192, S193, S194, S195, S196, S197, S198, S199, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271, S272, S273, S274, S275, S276, S277, S278, S279, S280, S281, S282, S283, S284, S285, S286, S287, S288, S289, S290, S291, S292, S293, S294, S295, S296, S297, S298, S299, S300, S301, S302, S303, S304, S305, S306, S307, S308, S309, S310, S311, S312, S313, S314, S315, S316, S317, S318, S319, S320, S321, S322, S323, S324, S325, S326, S327, S328, S329, S330, S331, S332, S333, S334, S335, S336, S337, S338, S339, S340, S341, S342, S343, S344, S345, S346, S347, S348, S349, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S395, S396, S397, S398, S399, S400, S401, S402, S403, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419, S420, S421, S422, S423, S424, S425, S426, S427, S428, S429, S430, S431, S432, S433, S434, S435, S436, S437, S438, S439, S440, S441, S442, S443, S444, S445, S446, S447, S448, S449, S450, S451, S452, S453, S454, S455, S456, S457, S458, S459, S460, S461, S462, S463, S464, S465, S466, S467, S468, S469, S470, S471, S472, S473, S474, S475, S476, S477, S478, S479, S480, S481, S482, S483, S484, S485, S486, S487, S488, S489, S490, S491, S492, S493, S494, S495, S496, S497, S498, S499, S500, S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533, S534, S535, S536, S537, S538, S539, S540, S541, S542, S543, S544, S545, S546, S547, S548, S549, S550, S551, S552, S553, S554, S555, S556, S557, S558, S559, S560, S561, S562, S563, S564, S565, S566, S567, S568, S569, S570, S571, S572, S573, S574, S575, S576, S577, S578, S579, S580, S581, S582, S583, S584, S585, S586, S587, S588, S589, S590, S591, S592, S593, S594, S595, S596, S597, S598, S599, S600, S601, S602, S603, S604, S605, S606, S607, S608, S609, S610, S611, S612, S613, S614, S615, S616, S617, S618, S619, S620, S621, S622, S623, S624, S625, S626, S627, S628, S629, S630, S631, S632, S633, S634, S635, S636, S637, S638, S639, S640, S641, S642, S643, S644, S645, S646, S647, S648, S649, S650, S651, S652, S653, S654, S655, S656, S657, S658, S659, S660, S661, S662, S663, S664, S665, S666, S667, S668, S669, S670, S671, S672, S673, S674, S675, S676, S677, S678, S679, S680, S681, S682, S683, S684, S685, S686, S687, S688, S689, S690, S691, S692, S693, S694, S695, S696, S697, S698, S699, S700, S701, S702, S703, S704, S705, S706, S707, S708, S709, S710, S711, S712, S713, S714, S715, S716, S717, S718, S719, S720, S721, S722, S723, S724, S725, S726, S727, S728, S729, S730, S731, S732, S733, S734, S735, S736, S737, S738, S739, S740, S741, S742, S743, S744, S745, S746, S747, S748, S749, S750, S751, S752, S753, S754, S755, S756, S757, S758, S759, S760, S761, S762, S763, S764, S765, S766, S767, S768, S769, S770, S771, S772, S773, S774, S775, S776, S777. Every listed relationship is `PASS_1_COMPLETE`.
