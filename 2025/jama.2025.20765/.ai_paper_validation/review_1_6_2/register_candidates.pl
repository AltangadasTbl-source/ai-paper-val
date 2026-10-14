use strict; use warnings; local $/;
my $base='.ai_paper_validation/review_1_6_2';
open my $in,'<',"$base/screening/registration_handoff.md" or die $!; my $draft=<$in>;
my @chunks=$draft =~ /(^## ISSUE-\d{3} —[^\n]*\n.*?)(?=^## ISSUE-\d{3} —|^## ISSUE-014 detailed|\z)/msg;
die scalar(@chunks) unless @chunks==19;
my ($table)=$draft =~ /(\| ID \| Review domain.*?)(?=\n## ISSUE-)/s;
my ($detail)=$draft =~ /(^## ISSUE-014 detailed interval reconstruction.*?)(?=^## Consolidation)/msg;
my %map; while($table =~ /^\| ISSUE-(\d{3}) .*?\| (F-[^\n|]+) \|$/mg){my($n,$f)=($1,$2); for($f =~ /(F-(?:NUM|XS|ST1)-\d{3})/g){die "duplicate $_" if exists $map{$_}; $map{$_}="C$n";}}
die 'membership' unless keys(%map)==29;
my %drop=map{$_=>1}('Reported-versus-comparator','Reasoning procedure','Mechanical evidence recheck','Potential downstream evidence impact');
my @cards;
for my $chunk(@chunks){my($heading)=$chunk =~ /^(##[^\n]+)/; my $card="$heading\n\nPending Human Adjudication.\n\n"; while($chunk =~ /(\*\*([^*\n]+):\*\*.*?)(?=\n\*\*[^*\n]+:\*\*|\z)/sg){$card.="$1\n" unless $drop{$2};} $card.=$detail if $heading =~ /ISSUE-014 /; $card =~ s/ISSUE-(\d{3})/C$1/g; $card =~ s!\.\./\.\./\.\./!../../!g; push @cards,$card;}
$table =~ s/ISSUE-(\d{3})/C$1/g;
open my $out,'>',"$base/candidate_ledger.md" or die $!; print $out "# Workflow 1.6.2 Candidate Ledger\n\nPending Human Adjudication. All 19 source-ordered candidates originate from the independent screen of 30 findings: 29 INCLUDE findings and one SCREENED_OUT finding. Full original handoff is preserved in screening/registration_handoff.md. Stable IDs remain assigned through all subsequent stages.\n\n$table",join("\n",@cards); close $out;
for my $shard(0..2){my @bounds=([0,6],[7,12],[13,18]); my($first,$last)=@{$bounds[$shard]}; my $part="# Stable candidate recheck scope\n\nPending Human Adjudication. Canonical ledger: ../candidate_ledger.md.\n\n"; $part.=join("\n",grep{my($n)=/^\| C(\d{3})/; defined($n)&&$n>=$first+1&&$n<=$last+1} split(/\n/,$table))."\n\n"; $part.=join("\n",@cards[$first..$last]); $part =~ s!\.\./\.\./(?=(?:jama_zahid|joi250093))!../../../!g; open my $p,'>',sprintf("$base/ledger_parts/candidates_%03d.md",$shard+1) or die $!; print $p $part; close $p;}
open my $sc,'<',"$base/screening/inclusion_screen.md" or die $!; my $screen=<$sc>; close $sc; $screen =~ s/^(\| (F-[^ |]+) .*?\| INCLUDE \| MEETS_THRESHOLD \| )PENDING( \|)$/$1.$map{$2}.$3/emg; $screen =~ s/ISSUE-(\d{3})/C$1/g; $screen =~ s/Candidate IDs[^\n]*remain PENDING\./Stable candidate IDs C001–C019 are assigned by the coordinator./g; open $sc,'>',"$base/screening/inclusion_screen.md" or die $!; print $sc $screen;
print "Registered 19 candidates; mapped 29 findings.\n";
