use strict; use warnings; local $/;
my $f='.ai_paper_validation/review_1_6_2/extraction/support_quantitative_evidence.md';
open my $i,'<:encoding(UTF-8)',$f or die $!; my $t=<$i>; close$i;
my($a,$b)=split(/(?=## Full page-text locator appendix)/,$t,2);
my @pairs=(
['CHA2 DS2','CHA2DS2'],['2 VASc','2VASc'],['Nationaldataup','National data up'],['andno','and no'],['orafter','or after'],['randomizedirrespective','randomized irrespective'],['ratesstarred','rates starred'],['sevenpost-randomizationGP','seven post-randomization GP'],['AFbefore','AF before'],['arrhythmiasplus','arrhythmias plus'],['burdenpercentage','burden percentage'],['heart-ratebeats','heart-rate beats'],['and2.5-years','and 2.5 years'],['1.75%2.5-years','1.75% at 2.5 years'],['2.5-years','2.5 years'],['power2p','power 2p'],['power90%','power 90%'],['alpha.05','alpha .05'],['totaln','total n'],['power2500','power 2500'],['ratio2.52','ratio 2.52'],['AFat','AF at'],['5-yearsecondary','5-year secondary'],['AFat','AF at'],['AFtodate','AF to date'],['mean timewith','mean time with'],['known AFoverall','known AF overall'],['Secondarytime','Secondary time'],['Nationaldata','National data'],['GPfollowuplength','GP follow-up length'],['withAF','with AF'],['5yearfollow','5-year follow'],['source-specificfollow','source-specific follow'],['GP AF;censor','GP AF; censor'],['Sensitivity primary and secondary outcomes using AF in GP orHES','Sensitivity primary and secondary outcomes using AF in GP or HES'],['simulations difference','simulations with difference'],['s=#simulations','s = number of simulations'],['n=total','n = total'],['primary and secondarysource','primary and secondary source'],['Timewith','Time with'],['at2.5 years','at 2.5 years'],['meantime','mean time'],['daysfirst','days from first'],['post-randomizationGP','post-randomization GP'],['andsex','and sex'],['all randomized ITT','all randomized, ITT'],['noAF','no AF'],['age<','age <'],['age≥','age ≥'],['SAS9.4/R4.2.2/RStudio2024.12.1','SAS 9.4/R 4.2.2/RStudio 2024.12.1'],['sex0–1','sex 0–1'],['CI.16','CI .16'],['95%CI','95% CI'],['CIunadjusted','CI unadjusted'],['25years','25 years'],['group1','group 1'],['group3','group 3'],['groups1/2','groups 1/2'],['AF/102','AF / 102'],['6s','6 s'],['≥30s','≥30 s'],['30s AF','30 s AF'],['stage≥','stage ≥'],['≥80','≥80'],['all13','all 13'],['AF89','AF 89'],['age80','age 80'],['means','means'],['firstpost','first post'],['primary and secondary outcomes','primary and secondary outcomes'],['first6','first 6'],['Complete11','Complete 11'],['complete11','complete 11'],['all13','all 13'],['and166','and 166'],['primary2.5','primary 2.5'],['30months','30 months'],['day0','day 0'],['25years','25 years'],['2week','2-week'],['Controlwithin','Control within'],['Power4000','Power 4000'],['Power5000','Power 5000']
);
for(@pairs){my($x,$y)=@$_;$a=~s/\Q$x\E/$y/g;}
$a=~s/(?<=[,;])(?=[A-Za-z])/, /g if 0; # Delimiter-specific rules below preserve punctuation.
$a=~s/,(?=[A-Za-z])/, /g; $a=~s/;(?=[A-Za-z0-9]) /; /g;
$a=~s/;(?=[A-Za-z])/; /g;
$a=~s/\)(?=vs)/) /g; $a=~s/\bvs(?=\d)/vs /g;
$a=~s/\bratio(?=\d)/ratio /g;
$a=~s/\bRD(?=[\d.])/RD /g;
$a=~s/\b(page|pages|pp)(?=\d)/$1 /g;
$a=~s/\bAge(?=[<≥])/Age /g;
$a=~s/\bBMI(?=≥)/BMI /g;
$a=~s/\bScore(?=[≥])/Score /g;
$a=~s/(\d)\((?=[\d.])/$1 (/g;
$a=~s/\b(ECG|AF|P|n)(?=\d)/$1 /g;
$a=~s/\btrend(?=\w)/trend /g;
$a=~s/11 metrics\/reason rows/metrics and reason rows/g;
open my $o,'>:encoding(UTF-8)',$f or die$!; print $o $a,$b; close$o;
