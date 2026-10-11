use strict;
use warnings;
use utf8;
use open qw(:std :encoding(UTF-8));
my $root='.ai_paper_validation/review_1_6_2';
sub read_file { my($p)=@_; open my $f,'<',$p or die $!; local $/; return <$f>; }
my @rows=(
['C001','F-NUM-001','Abstract male percentage differs from the enrolled sex counts','statistical_results','S_W','S_W','REPORT main abstract p.1 vs REPORT main enrolled counts p.4','F-XS-001'],
['C002','F-XS-002','Planned primary priors and robustness analyses differ from the supplied implementation','protocol_report','P_R','P_R','PLAN protocol pp.12,40-41 vs REPORT main pp.3-4,6 and results supplement pp.10-14','F-ST1-201,F-ST1-202'],
['C003','F-XS-003','Secondary outcome status and analysis specification require reconciliation','protocol_report','P_R','P_R','PLAN protocol pp.7,31,40 vs REPORT main pp.3-4,7-8',''],
['C004','F-XS-004','Myotonia measurement definitions differ between the plan and report','protocol_report','P_R','P_R','PLAN protocol pp.32-33 vs REPORT main pp.3,5,7-8','F-XS-010,F-ST1-204'],
['C005','F-XS-005','Primary-data eligibility differs from the planned withdrawal-data rule','protocol_report','P_R','P_R','PLAN protocol p.35 vs REPORT main pp.3-4,8 and results supplement p.5','F-ST1-203'],
['C006','F-ST1-207','Planned primary treatment interactions have no identifiable reported result','protocol_report','P_R','P_R','PLAN protocol p.40 vs REPORT main pp.3-4 and results supplement pp.11-14',''],
['C007','F-XS-007','Three clinical nonresponders are attributed to a Bayesian rule met by two','statistical_results','S_C','S_C, S_W','REPORT main stopping rule p.3 and response statement p.4 vs REPORT results supplement p.5',''],
['C008','F-NUM-004','INQoL baseline upper quartiles exceed the stated scale range','statistical_results','S_W','S_W','REPORT main Table 1 row and scale footnote p.5; corroborating Table 2 scale footnote p.8',''],
['C009','F-ST1-010','Other-medication P does not reproduce the adjacent-row binary comparison','statistical_results','S_W','S_W','REPORT main Table 1 medication and sex rows plus test footnote p.5',''],
['C010','F-ST1-004','SCN4A transient-paresis interval crosses zero while its P is significant','statistical_results','S_W','S_W','REPORT main repeated narrative p.6 vs Table 2 subgroup row p.7 and test rule p.4',''],
['C011','F-ST1-008','Lower Table 2 contrast header reverses the represented effect direction','statistical_results','S_W','S_W','REPORT main Table 2 lower header and repeated outcome rows p.7 with direction footnotes p.8',''],
['C012','F-ST1-012','Physical SF-36 placebo interval does not center on its printed mean','statistical_results','S_W','S_W','REPORT main Table 2 physical SF-36 period row and comparator rows p.7; methods pp.3,8',''],
['C013','F-ST1-005','Mental SF-36 estimate and interval do not yield the printed P under the stated test','statistical_results','S_W','S_W','REPORT main Table 2 mental SF-36 row p.7 vs dependent-test methods pp.3-4,8',''],
['C014','F-ST1-001','Placebo first-handgrip mean lies outside its descending interval','statistical_results','S_W','S_W','REPORT main Table 2 first-handgrip placebo mean and interval p.7; scale and method footnotes p.8',''],
['C015','F-ST1-009','Eleven non-IVR effects do not reproduce the period-mean difference pattern','statistical_results','S_W','S_W','REPORT main Table 2 eleven named non-IVR rows p.7 vs dependent-test and availability methods pp.3-4,8',''],
['C016','F-ST1-003','SCN4A fifth-handgrip interval crosses zero while its P is significant','statistical_results','S_W','S_W','REPORT main Table 2 fifth-handgrip SCN4A row p.7 and repeated narrative p.8; rule p.4',''],
['C017','F-ST1-007','First-eyelid interval excludes zero while printed P equals the strict threshold','statistical_results','S_W','S_W','REPORT main Table 2 first-eyelid row p.7 vs strict significance rule p.4 and method footnotes p.8',''],
['C018','F-ST1-002','Placebo mean Timed Up and Go change exceeds its interval upper bound','statistical_results','S_W','S_W','REPORT main Table 2 mean Timed Up and Go placebo point and interval p.7; footnotes p.8',''],
['C019','F-ST1-006','Needle-EMG estimate and interval do not yield the printed P under the stated test','statistical_results','S_W','S_W','REPORT main Table 2 needle-EMG row p.8 vs dependent-test and two-sided methods pp.3-4',''],
['C020','F-XS-009','Plan text and diagram specify different DSMB review triggers','plan_material','P_P','P_P','PLAN protocol DSMB text p.38 vs PLAN protocol safety diagram p.39','F-ST1-206'],
['C021','F-XS-008','Plan interim text and diagram specify different prior information','plan_material','P_P','P_P','PLAN protocol noninformative-only interim text p.42 vs PLAN protocol informative-prior arrows p.43','F-ST1-205'],
);
my %finding;
for my $file(qw(numeric_consistency.md cross_source_consistency.md statistical_pass_1.md)){
 my $text=read_file("$root/checkers/$file");
 while($text=~/(^### (F-[A-Z0-9]+-\d{3})[^\n]*\n.*?)(?=^### F-|^## Excluded observations|\z)/msg){$finding{$2}=$1;}
}
my $screen=read_file("$root/screening/inclusion_screen.md");
my %notes;
while($screen=~/(^\*\*(F-[A-Z0-9]+-\d{3}) — (?:INCLUDE|SCREENED_OUT):\*\*.*?)(?=^\*\*F-|^## Consolidation|\z)/msg){$notes{$2}=$1;}
my %map;
for my $row(@rows){$map{$row->[1]}=$row->[0];for(split /,/,$row->[7]){$map{$_}=$row->[0] if length $_;}}
$screen=~s{^(\| (F-[A-Z0-9]+-\d{3}) \|[^\n]*?\| )PENDING( \|)$}{$1.(defined $map{$2}?$map{$2}:die("Missing mapping $2")).$3}mge;
open my $sf,'>',"$root/screening/inclusion_screen.md" or die$!;print $sf $screen;close$sf;
open my $lf,'>',"$root/candidate_ledger.md" or die$!;
print $lf "# Workflow 1.6.2 Candidate Ledger\n\nPending Human Adjudication. Twenty-one distinct issues were registered only after the fresh independent screen completed all 34 findings. Source order uses the earliest substantive REPORT location, then its display order, followed by PLAN-only source locations; supporting method locations do not reorder a result card. Every repeated pattern preserves all affected rows and locations. Duplicate finding provenance remains attached, while the classification Finding IDs column contains only INCLUDE findings.\n\n## Classification table\n\n| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |\n|---|---|---|---|---|---|---|---|\n";
for my $r(@rows){print $lf "| $r->[0] | $r->[3] | $r->[4] | $r->[5] | $r->[6] | PENDING_RECHECK | PENDING_AUDIT | $r->[1] |\n";}
for my $r(@rows){
 my($id,$fid,$title,$domain,$type,$all,$roles,$duplicates)=@$r;
 print $lf "\n## $id — $title\n\nPending Human Adjudication.\n\n**Review domain:** $domain\n**Relationship type:** $type\n**All relationships:** $all\n**Compared document roles:** $roles\n**Evidence state:** PENDING_RECHECK\n**Inclusion audit:** PENDING_AUDIT\n**Finding IDs:** $fid\n**Checker provenance:** $fid".($duplicates?", ".join(', ',split /,/,$duplicates):'')."\n**Classification rationale:** ";
 print $lf $type eq'P_R'?"The conflicting comparison concerns prospective PLAN content and REPORT analysis or endpoint content; report code corroborates the reported side. P_R takes precedence.\n":$type eq'P_P'?"Both conflicting specifications belong to the prospective PLAN bundle. Report material only corroborates implementation and creates no additional relationship.\n":$type eq'S_C'?"The response classification compares two REPORT documents and also an internal main-report criterion; S_C takes precedence over S_W.\n":"The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.\n";
 print $lf "**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.\n\n### Independent inclusion facts\n\n";
 my $n=$notes{$fid} or die"Missing notes $fid"; $n=~s@\.\./\.\./\.\./(joi|jama)@../../$1@g; print $lf $n;
 print $lf "\n### Source-linked checker evidence\n\n";
 for my $f($fid,split /,/,$duplicates){next unless length$f;my$t=$finding{$f} or die"Missing finding $f";$t=~s/^### /#### /mg;$t=~s@\.\./\.\./\.\./(joi|jama)@../../$1@g;print $lf $t,"\n";}
}
close$lf;
