use strict;use warnings;my$d='.ai_paper_validation/review_1_6';open my$f,'<',"$d/candidate_ledger.md"or die$!;local$/;my$t=<$f>;close$f;
my$row="| C061 | Statistical reporting inconsistency | S_W | S_W | REPORT main article p7 Table 3 total-alcohol twelve-month contrast, interval and P-value in the same row. | statistical_results | Pending recheck | Pending recheck |\n";
$t =~ s/(^\| C060 \|[^\n]*\n)/$1$row/m or die 'anchor';$t =~ s/60 distinct candidate comparisons/61 distinct candidate comparisons/;
$t.='\n';$t.=<<'CARD';

## C061 — Twelve-month total-alcohol interval and P-value require a construction definition

**Status:** Pending Human Adjudication

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article p7 Table 3 total-alcohol twelve-month contrast, interval and P-value in the same row.

**Review domain:** statistical_results

**Checker provenance:** S026 statistical pass1/pass2 definition-limited observation; fresh quality auditor recommendation; coordinator conditional registration under QUALITY_CONTROL_SCOPE Candidate threshold. Pass2 original conservative non-registration assessment is preserved; no common construction is asserted.

**Exact source locations:** [Main physical p7 Table 3 total alcohol twelve-month change](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7); [main physical p4 Statistical Analysis](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [main physical p8 Table 3 footnotes](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8).

**Source printed inputs:** The intervention-minus-control twelve-month total-alcohol contrast is −0.2 percentage points/day,95%CI−0.4 to+0.1,P=.01; main table change means are−0.3 and−0.1. Two-sided tests and mixed models/multiple imputation are described, but the interval/P common construction is not explicitly established.

**Conditional consistency rule:** If this95%interval and two-sidedP refer to the same contrast and compatible test/variance/construction at the5%level, an interval spanning zero and P=.01 do not reconcile. This is a conditional reporting question; the package does not establish every necessary compatibility condition. No inverse-Wald calculation or exact replacementP is made.

**Direct observation versus diagnostic reasoning:** The same-row interval spans zero and P=.01 is directly printed. The upper endpoint+0.1 cannot be explained merely as a zero endpoint rounded from a small negative number. A definite test/CI contradiction, shared variance estimator, identical degrees of freedom, or intended correction is not inferred.

**Named missing definition:** Whether the CI and P correspond to exactly the same modeled contrast; CI construction; test statistic; common variance estimator; multiple-imputation pooling; degrees of freedom; model-adjustment identity and confidence/test compatibility.

**Alternative source-grounded interpretations:** Different documented CI and P constructions or pooling conventions might reconcile the displays; the supplied package does not fully identify those constructions. A transcription difference is also possible but unproven. The six-month upper endpoint0 is a separate rounded-endpoint situation and is not treated as this same comparison.

**Human question:** What exact CI and P constructions generated the twelve-month total-alcohol row, are they compatible for the same contrast, and do they explain the positive upper endpoint alongsideP=.01?

**Quality-control relevance:** A data extractor could copy an interval containing zero together with a nominalPbelow.05 without a construction definition. Resolve that conditional extraction question; no paper conclusion or methodological verdict is asserted.
CARD
open my$o,'>',"$d/candidate_ledger.md"or die$!;print $o $t;close$o;
