# RAW pass-2 calculation provenance

Engine: local JavaScript V8 arithmetic via functions.exec; no Python review or orchestration. Inputs transcribed from exact-source eTable 11 p17 visually read in this pass. Current pinned PyMuPDF1.26.4 CPU page renders p17/18 are authority; no new PDF/OCR derivative.

This is a diagnostic normal-95%-CI/common-covariance/two-dimensional chi-square Wald reconstruction, not an assertion of the authors' exact procedure. For a=PT−UC,b=HC−UC,c=HC−PT, d=(a,b), s_j=h_j/1.959963984540054, v_j=s_j^2 and u=(v_a+v_b−v_c)/2. Q=(v_b a²+v_a b²−2uab)/(v_a v_b−u²); diagnostic P=exp(−Q/2). True d_j and endpoint intervals respect each printed ±.05; c=b−a. Halfwidth admissibility: h_j in [max(d_j−L_j−.05,U_j−.05−d_j),min(d_j−L_j+.05,U_j+.05−d_j)].

The grid uses .001 steps for a,b inside their ±.05 intervals, exact additive c, and all8 halfwidth corners plus midpoint. Positive-definite covariance only. Grid limits are diagnostic sampled ranges, never exhaustive proofs. A separate conservative convexity bound supplies the physical6/12 nonreproduction proofs under this candidate method.

| S ID | Printed P | Precision-feasible witness d=(a,b,c) | Witness halfwidths | Diagnostic Q | Diagnostic P | Sampled feasible P range |
|---|---|---|---|---:|---:|---|
| S601 | <.001 | -0.549000, -0.549000, 0.000000 | 0.199000, 0.199000, 0.150000 | 34.077570 | 3.982443e-8 | [4.643331e-31, 2.154532e-4] |
| S602 | <.001 | -0.600000, -0.600000, 0.000000 | 0.250000, 0.250000, 0.150000 | 24.315168 | 5.248417e-6 | [6.002260e-11, 9.484804e-4] |
| S603 | <.001 | -0.549000, -0.449000, 0.100000 | 0.201000, 0.199000, 0.150000 | 29.340551 | 4.253831e-7 | [1.401437e-9, 1.242972e-3] |
| S604 | <.001 | -0.398000, -0.349000, 0.049000 | 0.152000, 0.199000, 0.199000 | 28.892831 | 5.321102e-7 | [4.795401e-7, 2.928311e-3] |
| S605 | <.001 | -0.449000, -0.449000, 0.000000 | 0.199000, 0.199000, 0.150000 | 22.793794 | 1.123028e-5 | [3.861633e-20, 4.501383e-3] |
| S606 | <.001 | -0.349000, -0.249000, 0.100000 | 0.201000, 0.101000, 0.150000 | 23.354755 | 8.483586e-6 | [below floating-point range, 4.837096e-2] |
| S607 | <.001 | -0.600000, -0.649000, -0.049000 | 0.250000, 0.199000, 0.199000 | 41.641881 | 9.069437e-10 | [1.289883e-18, 1.556549e-5] |
| S608 | <.001 | -0.700000, -0.700000, 0.000000 | 0.250000, 0.250000, 0.250000 | 40.156050 | 1.906447e-9 | [5.387691e-15, 1.615156e-5] |
| S609 | <.001 | -0.649000, -0.549000, 0.100000 | 0.201000, 0.201000, 0.150000 | 41.341524 | 1.053906e-9 | [6.402447e-14, 1.174769e-4] |
| S610 | 0.001 | 1.151000, 1.400000, 0.249000 | 0.899000, 0.750000, 0.701000 | 13.411990 | 1.223555e-3 | [1.777655e-4, 1.804800e-3] |
| S611 | <.001 | 1.751000, 1.451000, -0.300000 | 0.899000, 0.699000, 0.650000 | 18.441295 | 9.897456e-5 | [4.165246e-6, 2.133388e-4] |
| S612 | <.001 | 1.802000, 1.351000, -0.451000 | 0.948000, 0.801000, 0.799000 | 15.726370 | 3.846469e-4 | [1.052514e-4, 1.153899e-3] |
| S613 | 0.212 | 0.551000, 0.552000, 0.001000 | 0.701000, 0.798000, 0.849000 | 3.101588 | 2.120796e-1 | [1.531427e-1, 3.099075e-1] |
| S614 | 0.005 | No witness in diagnostic grid | — | — | — | [1.576919e-2, 3.991779e-2] |
| S615 | 0.001 | No witness in diagnostic grid | — | — | — | [3.609354e-3, 2.027679e-2] |
| S616 | <.001 | -0.798000, -0.949000, -0.151000 | 0.148000, 0.099000, 0.101000 | 375.441269 | 2.978272e-82 | [below floating-point range, 6.543682e-34] |
| S617 | <.001 | -0.700000, -0.700000, 0.000000 | 0.150000, 0.150000, 0.150000 | 111.544582 | 6.003462e-25 | [5.559356e-78, 3.935904e-11] |
| S618 | <.001 | -0.700000, -0.600000, 0.100000 | 0.150000, 0.150000, 0.150000 | 97.886062 | 5.550240e-22 | [6.104959e-67, 5.770726e-10] |
| S619 | <.001 | -0.800000, -1.149000, -0.349000 | 0.150000, 0.099000, 0.101000 | 611.340830 | 1.774294e-133 | [below floating-point range, 1.382256e-45] |
| S620 | <.001 | -0.600000, -0.800000, -0.200000 | 0.150000, 0.150000, 0.150000 | 118.373842 | 1.974453e-26 | [1.828393e-79, 1.294463e-12] |
| S621 | <.001 | -0.649000, -0.700000, -0.051000 | 0.199000, 0.150000, 0.101000 | 93.615347 | 4.695541e-21 | [below floating-point range, 1.182449e-9] |

Conservative bounds: Q is convex in d and in positive-definite V separately. V is affine in (v_a,v_b,v_c), so a maximum over an outer rectangular variance box is attained at its vertices. All box vertices used here are positive definite. Maximize over point polygon vertices and variance-box vertices; ignoring point/halfwidth coupling enlarges the feasible set, so the maximum is an upper bound.

Physical6: a∈[1.05,1.15],b∈[.35,.45],b−a∈[−.65,−.55]. Feasible point polygon vertices (1.05,.40),(1.05,.45),(1.10,.45). Halfwidth boxes [.75,.85],[.65,.75],[.70,.80]. Maximum Q≤8.556087823817016, attained at outer-box vertex a1.10,b.45,halfwidths .75,.75,.70. P≥.013869766053172373.

Physical12: allow full outer point rectangle a∈[1.15,1.25],b∈[.85,.95] (omitting the c constraint conservatively), halfwidth boxes [.75,.85],[.85,.95],[.85,.95]. Maximum Q≤12.281125558721055 at a1.25,b.95,halfwidths .75,.85,.95. P≥.0021537112129520757.

Printed P intervals: physical6[.0045,.0055],physical12[.0005,.0015]. Conservative lower-bound gaps .008369766/.005=1.6739532 and .000653711/.001=.6537112. These gaps are descriptive; Route A category1 is not removed through precision.

No author covariance, CI critical value, degrees of freedom or replacement P has been inferred. Different CI distributions, Wald reference distributions, or separate omnibus covariance/estimand mappings remain alternatives.
