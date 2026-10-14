# Printed-count diagnostics only; fitted-model results are not replaced.
z <- qnorm(.975)
x <- data.frame(label=c('death30','death60','ventricular','MACE30','LVAD30','stroke30and60','dialysis30','MACE60','LVAD60','anySAE','anyarrhythmia','AF','supraventricular','bradycardia','electricshock','hypokalemia','anycessation'),a=c(26,28,18,35,4,7,29,36,4,59,63,35,49,4,4,1,12),b=c(23,26,9,36,4,6,38,39,5,61,55,29,48,1,1,2,4))
for(i in seq_len(nrow(x))) {
 a <- x$a[i]; b <- x$b[i]; rd <- 100*(a/101-b/104)
 rr <- (a/101)/(b/104); se <- sqrt(1/a-1/101+1/b-1/104)
 cat(x$label[i],': RD=',format(rd,digits=9),'; RR=',format(rr,digits=9),'; log-RR CI=',format(exp(log(rr)+c(-1,1)*z*se),digits=9),'\n')
}
cat('Program does not derive absolute bootstrap intervals or classify findings.\n')
