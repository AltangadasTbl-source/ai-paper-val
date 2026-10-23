#!/usr/bin/env Rscript
# Run from paper_writting/main. Final human Excel values are authoritative.
options(stringsAsFactors = FALSE)
Sys.setenv(TZ = 'America/Phoenix')
suppressPackageStartupMessages(library(readxl))
dir.create('analysis', showWarnings = FALSE)
dir.create('manuscript/tables', recursive = TRUE, showWarnings = FALSE)
dir.create('manuscript/figures', recursive = TRUE, showWarnings = FALSE)
years <- c(2018L, 2019L, 2024L, 2025L)
cols <- c('key', 'title', 'source_location', 'disposition', 'domain', 'complete',
          'validation_hint', 'issue', 'substantiveness', 'impact', 'internal',
          'protocol', paste0('unused', 13:17), 'notes')
all <- list(); index <- list()
for (year in years) {
  path <- sprintf('review_results_2_4_1_Rbulun_copy/human_adjudication_v_2_4_1_%s_R_Bulun_completed.xlsx', year)
  ix <- as.data.frame(read_excel(path, sheet = 'Papers', col_types = 'text'))
  ix <- ix[!is.na(ix[[1]]) & nzchar(ix[[1]]), 1:3]
  names(ix) <- c('paper', 'sheet', 'expected_candidates'); ix$year <- year
  ix$expected_candidates <- as.integer(ix$expected_candidates)
  index[[as.character(year)]] <- ix
  for (sheet in ix$sheet) {
    x <- as.data.frame(suppressMessages(read_excel(path, sheet = sheet, range = cell_cols('A:R'), col_types = 'text')))
    names(x) <- cols
    x[is.na(x)] <- ''
    x <- x[nzchar(x$key), ]
    x$year <- year; x$paper <- sub('^C_', '', sheet)
    x$workbook <- basename(path); x$sheet <- sheet; x$excel_row <- seq_len(nrow(x)) + 1L
    stopifnot(nrow(x) == ix$expected_candidates[ix$sheet == sheet])
    all[[paste(year,sheet)]] <- x
  }
}
d <- do.call(rbind, all); rownames(d) <- NULL
ix <- do.call(rbind, index); rownames(ix) <- NULL
stopifnot(!anyDuplicated(d$key), nrow(d) == 440L, nrow(ix) == 44L,
          all(d$complete == 'primary_done'), all(d$disposition %in% c('retain', 'exclude')))
allowed_domains <- c('statistical_results', 'report_internal_inconsistency', 'protocol_report', 'plan_material')
stopifnot(all(d$domain %in% allowed_domains))
ret <- d$disposition == 'retain'
st <- ret & d$domain == 'statistical_results'
incon <- ret & d$domain %in% c('report_internal_inconsistency', 'plan_material')
stopifnot(all(d$issue[st] %in% c('confirmed_issue','probable_issue','not_issue','indeterminate')),
          all(d$substantiveness[st] %in% c('substantive','minor_presentation','indeterminate')),
          all(d$internal[incon] %in% c('substantive_inconsistency','minor_presentation','non_inconsistency','indeterminate')))
prov <- read.csv('analysis/candidate_provenance.csv')
m <- match(d$key, prov$key); stopifnot(!anyNA(m), setequal(d$key,prov$key))
d$original_domain <- prov$domain[m]; d$relationship <- prov$relationship_type[m]
d$report_relationship <- d$relationship %in% c('S_C','S_W')
d$primary <- st & d$report_relationship & d$issue %in% c('confirmed_issue','probable_issue') & d$substantiveness == 'substantive'
d$strict <- d$primary & d$issue == 'confirmed_issue'
d$secondary <- ret & d$report_relationship & d$domain == 'report_internal_inconsistency' & d$internal == 'substantive_inconsistency'
d$combined <- d$primary | d$secondary
d$confirmed_report <- ret & d$report_relationship & ((d$domain == 'statistical_results' & d$issue == 'confirmed_issue') |
                        (d$domain == 'report_internal_inconsistency' & d$internal %in% c('substantive_inconsistency','minor_presentation')))
d$period <- ifelse(d$year < 2020, '2018--2019', '2024--2025')
write.csv(d,'analysis/candidate_results.csv',row.names=FALSE)
p <- ix[c('year','paper')]
metrics <- c('primary','strict','secondary','combined','confirmed_report')
for (metric in metrics) p[[metric]] <- vapply(p$paper,function(id) sum(d[[metric]][d$paper==id]),numeric(1))
p$candidates <- vapply(p$paper,function(id) sum(d$paper==id),numeric(1))
p$retained <- vapply(p$paper,function(id) sum(d$paper==id & ret),numeric(1))
p$excluded <- p$candidates-p$retained
p$period <- ifelse(p$year<2020,'2018--2019','2024--2025')
metadata <- read.csv('analysis/package_metadata.csv')
mm <- match(p$paper,metadata$paper); stopifnot(!anyNA(mm))
p$documents <- metadata$documents[mm]; p$pages <- metadata$pages[mm]
write.csv(p,'analysis/paper_results.csv',row.names=FALSE)

# Exact two-sided permutation test for difference in mean integer counts.
# dp[k+1,s+1] counts all size-k subsets with integer sum s; ties retained.
exact_mean_permutation <- function(x, earlier) {
  stopifnot(all(x>=0), all(x==round(x)), length(x)==length(earlier))
  n <- length(x); k <- sum(earlier); total <- sum(x)
  dp <- matrix(0,k+1,total+1); dp[1,1] <- 1; seen <- 0L
  for (v in x) {
    for (j in seq.int(min(k,seen+1L),1L)) {
      s <- 0:(total-v)
      dp[j+1L,s+v+1L] <- dp[j+1L,s+v+1L]+dp[j,s+1L]
    }
    seen <- seen+1L
  }
  weights <- dp[k+1L,]; denom <- choose(n,k)
  stopifnot(abs(sum(weights)/denom-1)<1e-10)
  observed <- mean(x[!earlier])-mean(x[earlier])
  null <- (total-(0:total))/(n-k)-(0:total)/k
  c(difference=observed,p=sum(weights[abs(null)>=abs(observed)-1e-12])/denom)
}
# A direct enumeration cross-check verifies zero-count handling and ties.
toy <- c(0,0,1,1,3,4); early <- seq_along(toy)<=3
observed <- mean(toy[!early])-mean(toy[early])
brute <- combn(seq_along(toy),3,function(i) mean(toy[-i])-mean(toy[i]))
stopifnot(abs(exact_mean_permutation(toy,early)['p']-mean(abs(brute)>=abs(observed)-1e-12))<1e-12)
set.seed(20261022)
B <- 20000L; earlier <- p$year<2020
boot_early <- replicate(B,sample(which(earlier),sum(earlier),replace=TRUE))
boot_later <- replicate(B,sample(which(!earlier),sum(!earlier),replace=TRUE))
comparisons <- list()
for (metric in c('primary','secondary','strict','combined')) {
  for (scale in c('count','any')) {
    x <- p[[metric]]; if(scale=='any') x <- as.integer(x>0)
    test <- exact_mean_permutation(x,earlier)
    bootdiff <- colMeans(matrix(x[boot_later],nrow=sum(!earlier)))-colMeans(matrix(x[boot_early],nrow=sum(earlier)))
    ci <- quantile(bootdiff,c(.025,.975),names=FALSE,type=7)
    comparisons[[paste(metric,scale)]] <- data.frame(metric,scale,early_total=sum(x[earlier]),late_total=sum(x[!earlier]),
      early_mean=mean(x[earlier]),late_mean=mean(x[!earlier]),difference=unname(test['difference']),
      lower=ci[1],upper=ci[2],p=unname(test['p']))
  }
}
cmp <- do.call(rbind,comparisons); rownames(cmp)<-NULL
# Label all p-values exploratory; no confirmatory family or alpha declared.
write.csv(cmp,'analysis/period_comparisons.csv',row.names=FALSE)

year_summary <- do.call(rbind,lapply(years,function(y) {
  a <- d[d$year==y,]; z<-p[p$year==y,]
  data.frame(year=y,papers=nrow(z),documents=sum(z$documents),pages=sum(z$pages),
    candidates=nrow(a),retained=sum(a$disposition=='retain'),excluded=sum(a$disposition=='exclude'),
    primary=sum(a$primary),primary_papers=sum(z$primary>0),strict=sum(a$strict),secondary=sum(a$secondary))
}))
write.csv(year_summary,'analysis/year_summary.csv',row.names=FALSE)
domain_summary <- do.call(rbind,lapply(allowed_domains,function(dom){
 a<-d[d$domain==dom,]
 data.frame(domain=dom,candidates=nrow(a),retained=sum(a$disposition=='retain'),excluded=sum(a$disposition=='exclude'))
}))
write.csv(domain_summary,'analysis/domain_summary.csv',row.names=FALSE)

lines <- c('TRACE-Q final human workbook analysis',sprintf('R: %s; readxl: %s',R.version.string,packageVersion('readxl')),
           'Availability sample; publication cohort year from workbooks, not DOI year.',
           '44 packages and 440 candidate rows; every row primary_done; keys unique; catalog matches.',
           'All original source-file and final-report hashes checked by collect_provenance.py.',
           'Primary: retained, report relationship S_C/S_W, statistical_results, confirmed/probable AND substantive.',
           'Secondary: retained, S_C/S_W, report_internal_inconsistency AND substantive_inconsistency.',
           'Original P_R/P_P relationships excluded from period endpoints despite editable human domain.',
           'Exact two-sided paper-label permutation; 19 vs 25 papers; difference later minus earlier.',
           '95% percentile bootstrap CIs, 20,000 within-period paper resamples, seed 20261022.',
           'P-values exploratory and unadjusted; no causal interpretation.', '',capture.output(year_summary),
           '',capture.output(domain_summary),'',capture.output(cmp),
           '\nRetained statistical issue status:',capture.output(table(d$issue[st])),
           '\nStatistical status x substantiveness:',capture.output(table(d$issue[st],d$substantiveness[st])),
           '\nInternal status by domain:',capture.output(table(d$domain[incon],d$internal[incon])),
           '\nProtocol interpretation:',capture.output(table(d$protocol[ret & d$domain=='protocol_report'])),
           '\nStatistical downstream impact:',capture.output(table(d$impact[st])),
           '\nEdited domains:',capture.output(d[d$domain!=d$original_domain,c('key','original_domain','domain','relationship','internal')]),
           '\nConfirmed report issues per package:',capture.output(summary(p$confirmed_report)),
           sprintf('Packages with a confirmed report issue: %d/%d',sum(p$confirmed_report>0),nrow(p)),
           sprintf('Packages with a primary eligible issue: %d/%d',sum(p$primary>0),nrow(p)),
           sprintf('Exact paper-yield CI: %s',paste(round(100*binom.test(sum(p$primary>0),nrow(p))$conf.int,1),collapse=' to ')))
writeLines(lines,'analysis/analysis_summary.txt')
writeLines(capture.output(sessionInfo()),'analysis/sessionInfo.txt')

fmt <- function(x,digits=2) formatC(ifelse(abs(x)<0.5*10^(-digits),0,x),format='f',digits=digits)
fp <- function(x) ifelse(x<.001,'$<0.001$',fmt(x,3))
tex <- function(x) gsub('_','\\_',as.character(x),fixed=TRUE)
row <- function(x) paste0(paste(x,collapse=' & '),' \\\\')
write_table <- function(file,caption,label,align,head,body,note='') {
 writeLines(c('\\begin{table}[tbp]','\\centering\\small',paste0('\\caption{',caption,'}'),paste0('\\label{',label,'}'),
  paste0('\\begin{tabular}{',align,'}'),'\\toprule',row(head),'\\midrule',body,'\\bottomrule','\\end{tabular}',
  if(nzchar(note)) paste0('\\par\\vspace{4pt}\\begin{minipage}{0.97\\linewidth}\\footnotesize ',note,'\\end{minipage}'),
  '\\end{table}'),paste0('manuscript/tables/',file,'.tex'))
}
ys <- year_summary
yb <- apply(ys[,c('year','papers','documents','pages','candidates','retained','excluded')],1,row)
yb <- c(yb,'\\midrule',row(c('Total',colSums(ys[,c('papers','documents','pages','candidates','retained','excluded')]))))
write_table('cohort','Paper packages and final human dispositions by publication year.','tab:cohort','lrrrrrr',
 c('Year','Papers','PDFs','Pages','Candidates','Retained','Excluded'),yb,
 'The 44 packages were selected by availability. PDF page counts exclude one supplementary XLSX file (one worksheet) in the 2025 cohort. Year is the recorded publication cohort and need not match the DOI year. Retention does not imply that every candidate is a confirmed reporting issue.')
domain_labels <- c('Statistical results','Report internal inconsistency','Protocol--report','Planning material')
db <- vapply(seq_len(nrow(domain_summary)),function(i) row(c(domain_labels[i],unlist(domain_summary[i,2:4]),
 fmt(100*domain_summary$retained[i]/domain_summary$candidates[i],1))),character(1))
write_table('dispositions','Candidate dispositions using the final human review domains.','tab:dispositions','lrrrr',
 c('Review domain','Candidates','Retained','Excluded','Retained (\\%)'),db,
 'Five candidates changed domain during human review. Protocol--report differences and planning-material findings are descriptive; they do not enter the temporal endpoints.')
cb <- vapply(seq_len(nrow(cmp)),function(i) {
 labels<-c(primary='Substantive statistical',secondary='Substantive report inconsistency',strict='Confirmed statistical only',combined='Combined substantive report')
 a<-cmp[i,]; if(a$scale=='count') vals<-c(fmt(a$early_mean),fmt(a$late_mean),paste0(fmt(a$difference),' (',fmt(a$lower),', ',fmt(a$upper),')')) else vals<-c(paste0(a$early_total,'/19'),paste0(a$late_total,'/25'),paste0(fmt(100*a$difference,1),' (',fmt(100*a$lower,1),', ',fmt(100*a$upper,1),')'))
 row(c(paste0(labels[a$metric],if(a$scale=='any') ' (any)' else ' (count)'),vals,fp(a$p)))
},character(1))
write_table('temporal','Exploratory comparison of report-material outcomes between publication periods.','tab:temporal','>{\\raggedright\\arraybackslash}p{5.0cm}rrrr',
 c('Outcome','2018--2019','2024--2025','Difference (95\\% CI)','$P$'),cb,
 'Count rows show the mean number per paper; any rows show papers with at least one eligible issue. Differences are later minus earlier, in issues per paper or percentage points, respectively. Principal-endpoint eligibility includes confirmed or probable statistical issues judged substantive. The confirmed-only and combined endpoints are sensitivity analyses. Confidence intervals use 20,000 paper bootstrap resamples within periods; two-sided permutation $P$ values are exact and unadjusted. No protocol--report or planning-material finding contributes.')
body <- vapply(seq_len(nrow(p)),function(i)row(c(p$year[i],paste0('\\texttt{',p$paper[i],'}'),p$candidates[i],p$retained[i],p$primary[i],p$strict[i],p$secondary[i])),character(1))
writeLines(c('\\small','\\begin{longtable}{llrrrrr}',
 '\\caption{Per-paper counts derived from the final human workbooks.}\\label{tab:perpaper}\\\\',
 '\\toprule',row(c('Year','Paper DOI suffix','Candidates','Retained','Primary','Strict','Secondary')),'\\midrule','\\endfirsthead',
 '\\toprule',row(c('Year','Paper DOI suffix','Candidates','Retained','Primary','Strict','Secondary')),'\\midrule','\\endhead',
 '\\bottomrule','\\endfoot',body,'\\end{longtable}','\\normalsize',
 '\\noindent\\footnotesize DOI prefix is 10.1001/. Primary = substantive confirmed/probable statistical issues; strict = substantive confirmed statistical issues; secondary = substantive report-internal inconsistencies. All three require an original report-only relationship.\\normalsize'),
 'manuscript/tables/perpaper.tex')

pdf('manuscript/figures/period_counts.pdf',width=8,height=4.1,family='Helvetica',useDingbats=FALSE)
par(mfrow=c(1,2),mar=c(4.2,4.1,2.0,0.8),mgp=c(2.4,.7,0),las=1,bty='l')
for (metric in c('primary','strict')) {
 x<-p[[metric]]
 boxplot(x~factor(p$period,levels=c('2018--2019','2024--2025')),outline=FALSE,col=c('#E4EEF5','#E6EFE9'),border='#5A6670',
   xaxt='n',xlab='',ylab='Eligible issues per paper',ylim=c(0,max(5,max(x))+.5),
   main=if(metric=='primary') 'A  Confirmed or probable' else 'B  Confirmed only',cex.main=.95)
 axis(1,at=1:2,labels=c('2018-2019','2024-2025'),tick=FALSE,line=.2,mgp=c(3,1,0))
 mtext(c('(n = 19)','(n = 25)'),side=1,at=1:2,line=2.3,cex=.83)
 for (g in 1:2) {
  val<-x[if(g==1) earlier else !earlier]
  offset<-ave(seq_along(val),val,FUN=function(z)seq(-.16,.16,length.out=length(z)))
  points(g+offset,val,pch=21,bg=if(g==1)'#326589' else '#3D7656',col='white',cex=1.1)
 }
}
dev.off()
cat(paste(lines[1:12],collapse='\n'),'\n')
print(year_summary); print(cmp)
