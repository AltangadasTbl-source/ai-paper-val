# Independent supplied-count and explicitly labelled log-Wald diagnostics.
z <- qnorm(.975)
x <- data.frame(id=c('S004','S005','S010','S024','S026','S027','S028','S030','S032','S045','S046','S047','S048','S049','S052','S053','S054'),a=c(26,28,18,35,4,7,29,36,4,59,63,35,49,4,4,1,12),b=c(23,26,9,36,4,6,38,39,5,61,55,29,48,1,1,2,4))
for(i in seq_len(nrow(x))) {
 a <- x$a[i]; b <- x$b[i]; rd <- 100*(a/101-b/104)
 rr <- (a/101)/(b/104); se <- sqrt(1/a-1/101+1/b-1/104)
 cat(x$id[i],': RD=',format(rd,digits=10),'; RR=',format(rr,digits=10),'; diagnostic log-RR CI=',format(exp(log(rr)+c(-1,1)*z*se),digits=10),'\n')
}
y <- data.frame(id=c('S001','S002','S003','S011','S012','S013','S105-dose','S106'),est=c(1.02,.72,1.32,1.15,.91,1.57,2.45,.47),lo=c(.74,.37,.62,.82,.46,.72,1.11,.28),hi=c(1.39,1.38,2.79,1.62,1.82,3.44,5.40,.79))
for(i in seq_len(nrow(y))) {
 se <- (log(y$hi[i])-log(y$lo[i]))/(2*z)
 cat(y$id[i],': diagnostic log-Wald SE=',format(se,digits=9),'; two-sided P=',format(2*pnorm(-abs(log(y$est[i])/se)),digits=9),'\n')
}
cat('D60 mortality categorical Yates diagnostic P=',chisq.test(matrix(c(28,73,26,78),2,byrow=TRUE),correct=TRUE)$p.value,'\n')
cat('Events diagnostic=',4*(qnorm(.975)+qnorm(.8))^2/log(1.75)^2,'; target CIF diagnostic=',1-(1-.5)^1.75,'\n')
cat('Naive subject diagnostic interval=',100.5/.505,101.5/.495,'; gap=',205.5-101.5/.495,'; relative gap=',(205.5-101.5/.495)/206,'\n')
cat('KRT zero-nonrecipient diagnostic remains conditional; no duration distribution recomputed.\n')
cat('MACE placebo component-union gap=',37.5-36.5,'; relative=',(37.5-36.5)/36,'\n')
cat('SAE frequency totals: ',sum(c(42,22,19,8,2,4,2,2)),sum(c(43,31,13,4,6,3,1,2,1)),'; weighted events=',sum(c(0,1,2,3,4,5,6,8)*c(42,22,19,8,2,4,2,2)),sum(c(0,1,2,3,4,5,6,8,9)*c(43,31,13,4,6,3,1,2,1)),'\n')
cat('Diagnostic calculations do not replace fitted models or classify findings.\n')
