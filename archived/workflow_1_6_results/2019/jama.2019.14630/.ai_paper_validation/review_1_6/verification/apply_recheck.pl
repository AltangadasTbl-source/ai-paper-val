use strict;
use warnings;
my $dir='.ai_paper_validation/review_1_6';
open my $tf,'<',"$dir/verification/classification_recheck.tsv" or die $!;
my %facts;
while(<$tf>){chomp;my @v=split /\t/,$_,-1;next if $v[0] eq 'ID';die 'classification columns' unless @v==10;$facts{$v[0]}=\@v;}
close $tf;
open my $lf,'<',"$dir/candidate_ledger.md" or die $!;local $/;my $text=<$lf>;close $lf;
$text =~ s/^\| (C\d{3,}) \|.*$/my $v=$facts{$1} or die "missing $1"; '| '.join(' | ',@$v[0..7]).' |'/gme;
sub update_card {
my($heading,$id,$body)=@_;my $v=$facts{$id} or die "missing $id";
my @labels=('Category','Relationship type','All relationships','Compared document roles','Review domain');
for my $i(0..4){my $value=$v->[$i+1];$body =~ s/^\*\*$labels[$i]:\*\*.*$/**$labels[$i]:** $value/m;}
my $add="\n\n**Evidence state:** $v->[6]\n\n**Suggested review disposition:** $v->[7]\n\n**Classification rationale:** $v->[8]\n\n**Classification ambiguity:** $v->[9]";
$body =~ s/^(\*\*Review domain:\*\*.*)$/$1$add/m;
return $heading.$body;
}
$text =~ s/(^## (C\d{3,})[^\n]*\n)(.*?)(?=^## C\d{3,}|\z)/update_card($1,$2,$3)/gmse;
$text =~ s/Classification is provisional pending exact-source recheck; evidence-state and disposition fields will be finalized mechanically from recheck facts\./Classification is confirmed by the fresh exact-source recheck. Evidence-state and suggested-disposition fields are mechanical pre-fills from recheck facts, not human adjudications./;
open my $out,'>',"$dir/candidate_ledger.md" or die $!;print $out $text;close $out;
