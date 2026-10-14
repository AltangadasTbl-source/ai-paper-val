use strict; use warnings; local $/; my $b='.ai_paper_validation/review_1_6_2';
open my $ci,'<',"$b/coverage_manifest.md" or die $!; my $cov=<$ci>;close $ci;
my $ids=join(', ',map{sprintf('C%03d',$_)}1..19);
$cov =~ s/(^\| inclusion_screening \| (?:screen-001|registration-handoff) .*?\| )(?:PLANNED|IN_PROGRESS)( \|)$/${1}COMPLETE$2/mg;
$cov =~ s/Included finding set, pending stable IDs/$ids/; $cov =~ s/(^\| candidate_registration[^\n]*\| )PLANNED( \|)$/${1}COMPLETE$2/mg;
$cov =~ s/Complete stable candidate set, pending stable IDs/$ids/g;
$cov =~ s/Complete stable candidate set and all screening\/exclusion\/coverage records/$ids; all screening, exclusion, and coverage records/;
$cov =~ s/(^\| evidence_recheck[^\n]*\| )PLANNED( \|)$/${1}IN_PROGRESS$2/mg;
for my $s(1..3){my($f,$l)=($s==1?(1,7):$s==2?(8,13):(14,19));my $scope=join(', ',map{sprintf('C%03d',$_)}$f..$l);$cov.=sprintf("| candidate_registration | ledger-part-%03d | %s | ledger_parts/candidates_%03d.md | COMPLETE |\n| evidence_recheck | recheck-part-%03d | %s | verification/parts/recheck_%03d.md | IN_PROGRESS |\n",$s,$scope,$s,$s,$scope,$s);}
open $ci,'>',"$b/coverage_manifest.md" or die $!;print $ci $cov;close$ci;
open my $o,'>',"$b/checkers/excluded_observations_all.md" or die $!;print $o "# Complete initial checker excluded-observation handoff\n\nAll 46 observations copied verbatim from current-run checkers, with provenance. No screening decisions are replaced.\n\n";
for my $n(qw(numeric_consistency cross_source_consistency statistical_pass_1)){open my $i,'<',"$b/checkers/$n.md" or die$!;my $t=<$i>; print $o "## Provenance: checkers/$n.md\n\n";while($t =~ /(^## Excluded observations\n.*?)(?=^## |\z)/msg){print $o "$1\n";}}close$o;
open my $si,'<',"$b/statistics/relationship_inventory.md" or die$!;my$t=<$si>;close$si;
for my $s(1..2){my($f,$l)=($s==1?(1,72):(73,114));my @rows=grep{my($id)=/^\| S(\d{3}) \|/;defined($id)&&$id>=$f&&$id<=$l}split/\n/,$t;open my$p,'>',"$b/statistics/pass2_relationships_00$s.md" or die$!;print$p "# Statistical pass 2 disjoint relationship scope\n\n", join("\n",grep{/^\| S ID|^\|---/}split/\n/,$t),"\n",join("\n",@rows),"\n";close$p;}
print "Stage inputs prepared.\n";
