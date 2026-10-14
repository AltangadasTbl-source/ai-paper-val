# Auxiliary diagnostics only; not a substitute for reported analyses.
cat(R.version.string,"\n")
z<-qnorm(.975)
event_diagnostic<-(z+qnorm(.8))^2/(.25*log(1.75)^2)
cat("Required events diagnostic:",event_diagnostic,"; ceiling:",ceiling(event_diagnostic),"\n")
cat("Intervention CIF at control CIF .50 and sHR1.75:",1-(1-.5)^1.75,"\n")
triples<-list(c(1.15,.82,1.62,.42),c(.91,.46,1.82,.79),c(1.57,.72,3.44,.26),c(1.02,.74,1.39,.92),c(.72,.37,1.38,.32),c(1.32,.62,2.79,.47),c(2.45,1.11,5.40,.03),c(.47,.28,.79,.004))
for(x in triples){
 se<-(log(x[3])-log(x[2]))/(2*z)
 cat("Printed estimate/L/U/P:",x,"; implied log-Wald SE diagnostic:",se,"; P diagnostic:",2*pnorm(-abs(log(x[1])/se)),"\n")
}
for(x in list(c(26,101,23,104),c(28,101,26,104),c(18,101,9,104))){
 m<-matrix(c(x[1],x[2]-x[1],x[3],x[4]-x[3]),nrow=2)
 rr<-(x[1]/x[2])/(x[3]/x[4]); se<-sqrt(1/x[1]-1/x[2]+1/x[3]-1/x[4])
 cat("Count diagnostic inputs:",x,"; RR:",rr,"; log-RR CI:",exp(log(rr)+c(-1,1)*z*se),"; Yates chi-square P:",chisq.test(m)$p.value,"; chi-square without correction P:",chisq.test(m,correct=FALSE)$p.value,"; Fisher P:",fisher.test(m)$p.value,"\n")
}
cat("MV median half-unit input intervals [20.5,21.5] and [21.5,22.5]: difference [-2,0]; printed0 interval[-.5,.5], gap0\n")
cat("Naive event-count/control-CIF sample-size diagnostic [100.5,101.5]/.5=[201,203]; printed206 interval[205.5,206.5]; gap=2.5, relative=",2.5/206,"\n")
cat("SAE weighted counts:",sum(c(0,1,2,3,4,5,6,8)*c(42,22,19,8,2,4,2,2)),sum(c(0,1,2,3,4,5,6,8,9)*c(43,31,13,4,6,3,1,2,1)),"\n")
low_N<-100.5/.505; high_N<-101.5/.495
cat("Full naive sample-size half-unit intervals: event count[100.5,101.5], control CIF[.495,.505]; N=[",low_N,",",high_N,"]; printed206=[205.5,206.5]; gap=",205.5-high_N,"; relative=",(205.5-high_N)/206,"\n")
