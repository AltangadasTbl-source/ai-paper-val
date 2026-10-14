use strict;use warnings;local$/;my$b='.ai_paper_validation/review_1_6_2';
open my$i,'<',"$b/statistics/relationship_inventory.md"or die$!;my$t=<$i>;close$i;
for my$s(1..3){my($f,$l)=($s==1?(1,38):$s==2?(39,76):(77,114));my@rows=grep{my($id)=/^\| S(\d{3}) \|/;defined($id)&&$id>=$f&&$id<=$l}split/\n/,$t;open my$p,'>',"$b/statistics/pass2_relationships_00$s.md"or die$!;print {$p} "# Statistical pass 2 disjoint scope\n\n",join("\n",grep{/^\| S ID|^\|---/}split/\n/,$t),"\n",join("\n",@rows),"\n";close$p;}
open $i,'<',"$b/verification/evidence_recheck.md"or die$!;my$r=<$i>;close$i;
$r =~ s/^\*\*(?:Review domain|Relationship type|All relationships|Compared document roles|Finding IDs|Inclusion audit):\*\*[^\n]*\n\n//mg;
open my$p,'>',"$b/verification/pass2_all_recheck_facts.md"or die$!;print {$p} $r;close$p;
print"Prepared three disjoint statistical relationship scopes and complete facts with duplicate classification fields omitted.\n";
