# Independent pass-2 screening calculation record

Runtime: /root/pass2_screen; gpt-6.1-sol/high. Engine: local JavaScript V8 arithmetic via functions.exec. No Python extraction, review or orchestration; no new PDF/OCR derivative. Direct source transcriptions were independently read visually from current-source CPU PyMuPDF1.26.4 renders of DOC-005 pp15/17/18 and DOC-001 pp4/11. Existing calculation witnesses were then recomputed against those source values; they were not accepted solely from the checker.

Diagnostic family: normal 95% symmetric intervals with z=1.959963984540054; three additive contrasts a=PT−UC,b=HC−UC,c=b−a; vj=(hj/z)^2; u=(va+vb−vc)/2; Q=(vb*a*a+va*b*b−2*u*a*b)/(va*vb−u*u); chi-square2 tail P=exp(−Q/2). Exact author CI distribution, omnibus df/reference distribution and covariance/estimand mapping are not inferred.

A witness passes only when every point and both symmetric endpoints are within ±.05 of the corresponding exact printed source value, contrast additivity holds, covariance is positive definite and P is inside the printed numeric ±.0005 interval or below .001. Floating-point comparison tolerance 1e−12 is arithmetic tolerance only; it does not enlarge display precision materially. All 19 witnesses pass.

S601: d=(-0.549, -0.549, 0), h=(0.199, 0.199, 0.15); Q=34.07757034424387; P=3.9824434848564686e-8; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S602: d=(-0.6, -0.6, 0), h=(0.25, 0.25, 0.15); Q=24.31516791999795; P=0.0000052484174757098945; maximum point/endpoint distance=0.05000000000000002; positive definite=true; precision-feasible=true.

S603: d=(-0.549, -0.449, 0.1), h=(0.201, 0.199, 0.15); Q=29.340551304593312; P=4.253831042488272e-7; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S604: d=(-0.398, -0.349, 0.049), h=(0.152, 0.199, 0.199); Q=28.892830604387807; P=5.321101595622016e-7; maximum point/endpoint distance=0.04999999999999999; positive definite=true; precision-feasible=true.

S605: d=(-0.449, -0.449, 0), h=(0.199, 0.199, 0.15); Q=22.79379384597234; P=0.000011230279251209615; maximum point/endpoint distance=0.05000000000000002; positive definite=true; precision-feasible=true.

S606: d=(-0.349, -0.249, 0.1), h=(0.201, 0.101, 0.15); Q=23.3547545519287; P=0.000008483586375187048; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S607: d=(-0.6, -0.649, -0.049), h=(0.25, 0.199, 0.199); Q=41.6418814616595; P=9.069437087770563e-10; maximum point/endpoint distance=0.04999999999999999; positive definite=true; precision-feasible=true.

S608: d=(-0.7, -0.7, 0), h=(0.25, 0.25, 0.25); Q=40.15604953898926; P=1.9064465560944537e-9; maximum point/endpoint distance=0.04999999999999999; positive definite=true; precision-feasible=true.

S609: d=(-0.649, -0.549, 0.1), h=(0.201, 0.201, 0.15); Q=41.341524438018205; P=1.053906375038834e-9; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S610: d=(1.151, 1.4, 0.249), h=(0.899, 0.75, 0.701); Q=13.411989542704678; P=0.0012235549409462044; maximum point/endpoint distance=0.050000000000000266; positive definite=true; precision-feasible=true.

S611: d=(1.751, 1.451, -0.3), h=(0.899, 0.699, 0.65); Q=18.441295421977827; P=0.0000989745599564621; maximum point/endpoint distance=0.050000000000000266; positive definite=true; precision-feasible=true.

S612: d=(1.802, 1.351, -0.451), h=(0.948, 0.801, 0.799); Q=15.726369531825087; P=0.0003846469082521871; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S613: d=(0.551, 0.552, 0.001), h=(0.701, 0.798, 0.849); Q=3.1015875121749525; P=0.21207956755105883; maximum point/endpoint distance=0.0500000000000001; positive definite=true; precision-feasible=true.

S616: d=(-0.798, -0.949, -0.151), h=(0.148, 0.099, 0.101); Q=375.44126858216026; P=2.978272202145129e-82; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S617: d=(-0.7, -0.7, 0), h=(0.15, 0.15, 0.15); Q=111.54458205274791; P=6.003461973882689e-25; maximum point/endpoint distance=0.05000000000000002; positive definite=true; precision-feasible=true.

S618: d=(-0.7, -0.6, 0.1), h=(0.15, 0.15, 0.15); Q=97.88606180139102; P=5.550239861837153e-22; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S619: d=(-0.8, -1.149, -0.349), h=(0.15, 0.099, 0.101); Q=611.3408299000998; P=1.774293682102904e-133; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S620: d=(-0.6, -0.8, -0.2), h=(0.15, 0.15, 0.15); Q=118.37384217842641; P=1.9744528631018523e-26; maximum point/endpoint distance=0.050000000000000044; positive definite=true; precision-feasible=true.

S621: d=(-0.649, -0.7, -0.051), h=(0.199, 0.15, 0.101); Q=93.61534705352003; P=4.695541427886272e-21; maximum point/endpoint distance=0.049999999999999996; positive definite=true; precision-feasible=true.

Conservative proof: d'V^−1d is convex in d for fixed positive-definite V and convex in V for fixed d; V is affine in the three contrast variances. An outer Cartesian product of point polygon and variance box therefore has a maximum at point and variance vertices. Ignoring exact point/endpoint halfwidth coupling enlarges the domain. Every variance vertex here is positive definite, implying positive definiteness throughout its affine convex hull.

Physical6: a∈[1.05,1.15],b∈[.35,.45],c∈[−.65,−.55],c=b−a restricts the point polygon to (1.05,.40),(1.05,.45),(1.10,.45). Full-endpoint halfwidth boxes [.75,.85],[.65,.75],[.70,.80] enlarge the feasible domain. All24 combinations checked.

Physical12: outer rectangle a∈[1.15,1.25],b∈[.85,.95], with four corners; omitting the c constraint is conservative. Full-endpoint halfwidth boxes [.75,.85],[.85,.95],[.85,.95]. All32 combinations checked.

physical6: minimum determinant=0.01195380636846352; maximum Q=8.556087823817016 at a=1.1,b=0.45,h=(0.75, 0.75, 0.7); thus diagnostic P≥0.013869766053172373; printed P interval=[0.0045000000000000005, 0.0055]; gap divided by printed P=1.6739532106344746.

physical12: minimum determinant=0.02217991416023505; maximum Q=12.281125558721055 at a=1.25,b=0.95,h=(0.75, 0.85, 0.95); thus diagnostic P≥0.0021537112129520757; printed P interval=[0.0005, 0.0015]; gap divided by printed P=0.6537112129520757.

These are lower bounds under the tested reconstruction, not replacement P values or estimates of the actual author covariance. The grid's extrema were not used as proof. The 19 witness rows empirically support the reconstruction in the same display; the two target rows remain outside it even after conservative half-unit allowance. Whether distinct inferential definitions apply to the target rows is retained as the human question.

