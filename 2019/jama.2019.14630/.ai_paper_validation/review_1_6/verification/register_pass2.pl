use strict; use warnings;
my $d='.ai_paper_validation/review_1_6';
open my $f,'<',"$d/candidate_ledger.md" or die $!; local $/; my $ledger=<$f>; close $f;
my @spec=(['C059','PASS2-N01','Pastries baseline mean-versus-median labels across reports','REPORT main article p6 narrative; REPORT results supplement p5 eTable 2 baseline pastries.'],['C060','PASS2-N02','Vegetables baseline mean-versus-median labels across reports','REPORT main article p6 narrative; REPORT results supplement p3 eTable 2 baseline vegetables.']);
my $rows='';for my $s(@spec){$rows.="| $s->[0] | Measure, label, or scale inconsistency | S_C | S_C | $s->[3] | report_internal_inconsistency | Pending recheck | Pending recheck |\n";}
$ledger =~ s/(^\| C058 \|[^\n]*\n)/$1$rows/m or die 'table anchor';
open my $n,'<',"$d/checkers/statistical_pass_2_new_candidates.md" or die $!;my $new=<$n>;close $n;
for my $s(@spec){my($body)=$new =~ /^## \Q$s->[1]\E[^\n]*\n(.*?)(?=^## |\z)/ms or die 'appendix scope';$body =~ s!\.\./\.\./\.\./!../../!g;$ledger.="\n## $s->[0] — $s->[2]\n\n**Status:** Pending Human Adjudication\n\n**Category:** Measure, label, or scale inconsistency\n\n**Relationship type:** S_C\n\n**All relationships:** S_C\n\n**Compared document roles:** $s->[3]\n\n**Review domain:** report_internal_inconsistency\n\n**Checker provenance:** $s->[1] from statistical pass 2 fresh runtime 01a1289d-2ec2-73a1-bcae-13562fddd276; checkers/statistical_pass_2_new_candidates.md.\n\n$body";}
$ledger =~ s/58 distinct candidate comparisons/60 distinct candidate comparisons/;
$ledger.="\nStatistical pass2 appended C059 and C060 after exact duplicate checking; all prior IDs remain unchanged. No new statistical relationship IDs were required because each comparison cross-references the existing fully registered food-result relationships.\n";
open my $o,'>',"$d/candidate_ledger.md" or die $!;print $o $ledger;close $o;
