use strict;use warnings;local$/;my$b='.ai_paper_validation/review_1_6_2';my$r="# Workflow 1.6.2 Mechanical Evidence Recheck\n\nPending Human Adjudication. Three fresh distinct high-effort specialists cover disjoint stable candidate scopes; source pages remain authoritative. All parts are merged without loss, changing only relative source-link depth.\n\n";
for my$s(1..3){open my$i,'<',sprintf("$b/verification/parts/recheck_%03d.md",$s)or die$!;my$t=<$i>;$t =~ s!\.\./\.\./\.\./\.\./!../../../!g;$r.=$t."\n";}
open my$o,'>',"$b/verification/evidence_recheck.md"or die$!;print {$o} $r;close$o;
my%facts;while($r =~ /(^## (C\d{3}) [—-].*?)(?=^## C\d{3} [—-]|\z)/msg){my($t,$id)=($1,$2);my%f;for my$l('Review domain','Relationship type','All relationships','Compared document roles','Evidence state','Finding IDs','Classification rationale','Classification ambiguity'){my($v)=$t =~ /\*\*\Q$l\E:\*\*[ \t]*([^\n]*)/;die"missing $id $l"unless defined$v;$f{$l}=$v;}$facts{$id}=\%f;}
die'recheckset'unless keys(%facts)==19;
open my$l,'<',"$b/candidate_ledger.md"or die$!;my$t=<$l>;close$l;
$t =~ s{(^\| (C\d{3}) \|[^\n]+$)}{my($row,$id)=($1,$2);my@c=split(/ \| /,$row);$c[1]=$facts{$id}{'Review domain'};$c[2]=$facts{$id}{'Relationship type'};$c[3]=$facts{$id}{'All relationships'};$c[4]=$facts{$id}{'Compared document roles'};$c[5]=$facts{$id}{'Evidence state'};$c[7]=$facts{$id}{'Finding IDs'}.' |';join(' | ',@c)}emg;
$t =~ s{(^## (C\d{3}) [—-].*?)(?=^## C\d{3} [—-]|\z)}{my($s,$id)=($1,$2);for my$label(keys%{$facts{$id}}){my$v=$facts{$id}{$label};$s =~ s/(\*\*\Q$label\E:\*\*)[^\n]*/$1 $v/;} $s}emsg;
open$l,'>',"$b/candidate_ledger.md"or die$!;print {$l} $t;close$l;
open my$c,'<',"$b/coverage_manifest.md"or die$!;my$cov=<$c>;close$c;$cov =~ s/(^\| evidence_recheck[^\n]*\| )IN_PROGRESS( \|)$/${1}COMPLETE$2/mg;open$c,'>',"$b/coverage_manifest.md"or die$!;print {$c} $cov;
print"Merged 19 recheck facts and classifications.\n";
