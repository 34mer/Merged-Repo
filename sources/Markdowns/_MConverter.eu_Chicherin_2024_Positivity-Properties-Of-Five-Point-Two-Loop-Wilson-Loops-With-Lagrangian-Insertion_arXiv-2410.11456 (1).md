MPP-2024-194

Prepared for submission to JHEP

LAPTH-052/24

Positivity properties of five-point two-loop Wilson

loops with Lagrangian insertion

Dmitry Chicherina Johannes Hennb Jaroslav Trnkac Shun-Qing Zhangb

aLAPTh, Université Savoie Mont Blanc, CNRS, B.P. 110, F-74941 Annecy-le-Vieux, France bMax-Planck-Institut für Physik, Werner-Heisenberg-Institut, Boltzmannstr. 8, 85748 Garching, Germany

cCenter for Quantum Mathematics and Physics \(QMAP\), University of California, Davis, 95616

CA, USA

E-mail: chicherin@lapth.cnrs.fr, henn@mpp.mpg.de, trnka@ucdavis.edu, 

sqzhang@mpp.mpg.de

Abstract: In this paper we discuss the geometric integrand expansion of the five-point Wilson loop with one Lagrangian insertion in maximally supersymmetric Yang-Mills theory. 

We construct the integrand corresponding to an all-loop class of ladder-type geometries. 

We then investigate the known two-loop observable from this geometric viewpoint. To do so, we evaluate analytically the new two-loop integrals corresponding to the negative geometry contribution, using the canonical differential equations method. Inspecting the analytic result, we present numerical evidence that in this decomposition, each piece has uniform sign properties, when evaluated in the Amplituhedron region. Finally, we present an alternative bootstrap approach for the ladder-type geometries. We find that certain minimal bootstrap assumptions can be satisfied at two loops, but lead to a contradiction at three loops. This suggests to us that novel alphabet letters are required at this loop order. Indeed studying planar three-loop Feynman integrals, we do identify novel pentagon alphabet letters. 

arXiv:2410.11456v1 \[hep-th\] 15 Oct 2024

Contents

1

Introduction

2

2

Two-loop negative geometry decomposition of the Lagrangian insertion

in the Wilson loop

4

3

Momentum-twistor integrands for the negative geometries

9

4

Integrated negative geometries in five-particle kinematics

19

5

Two-loop nonplanar Feynman integrals for the negative geometries

24

6

Results for integrated negative geometries and positivity properties

35

7

d’Alembertian differential equation for the ladder-type geometries

45

8

Symbol bootstrap of the ladder-type negative geometries

48

9

Summary and discussion

53

A Two-loop alphabet letters

56

B Pentagon functions

59

C Soft, collinear, and multi-Regge limits

61

D Four-cusp negative geometries

68

– 1 –

1

Introduction

Scattering amplitudes are central ingredients in the description of particle interactions, for example at collider experiments. Starting from the Lagrangian of a quantum field theory Feynman rules provide a definition of scattering amplitudes in perturbation theory. 

However, in recent years, alternative ways of thinking about scattering amplitudes have been found. In fact, a host of new formulations and surprising dualities are known \(for reviews, see \[1, 2\]\). This is interesting for both conceptual and practical reasons. 

One of the new formulations takes a geometric starting point. Based on Hodges’ initial observation that certain tree-level six-particle amplitudes can be viewed as the canonical form of a polytope defined in kinematic space \[3\], Arkani-Hamed and Trnka proposed the Amplituhedron \[4\], which applies to all planar scattering amplitudes in maximally supersymmetric Yang-Mills theory \(sYM\). Their finding defines tree-level amplitudes, and loop-level integrands in that theory, as canonical forms associated to the Amplituhedron geometry. 

Once one thinks of \(the integrand of\) a scattering amplitude as \(the canonical form of\) some geometric object, it becomes natural to consider triangulations, as well as other ways of decomposing that object in terms of smaller building blocks. One example are the Britto-Cachazo-Feng-Witten recursion relations \[5\], which may be thought of as such a triangulation. Similarly, there are different possible decompositions and representations of loop-level integrands that may be derived from geometry. The important example of that are local triangulations where the individual building blocks are local integrands without any spurious poles \[6–9\]. In that case the triangulation is external, so the individual terms do overlap but regions outside the Amplituhedron cancel. 

An important conceptual and practical question, once a loop integrand is known, is that of carrying out the loop integrations. This gives rise, in general, to transcendental functions \(of the kinematic variables\). While there are well-developed beautiful techniques for Feynman integral computations, the latter are often one of the bottlenecks of state-of-the-art perturbative computations. We think that leveraging the underlying positive geometry properties when evaluating the integrals could lead to significant progress. 

A technical obstacle is that scattering amplitudes typically have infrared divergences. 

Although those are known in principle, and only the \(suitably-defined\) finite part of a given scattering amplitude is truly new, dealing with the infrared-divergent parts of the amplitudes is an important practical concern. Since our main focus in this paper is on exploring properties of transcendental functions associated to positive geometries, we choose as objects of study directly a suitably defined finite version of a scattering amplitude. \(We work in maximally supersymmetric Yang-Mills theory, so the scattering amplitudes do not require UV renormalization.\)

The objects we study in this paper can be conceptualized in different ways. One definition is as that of the correlation function of a Wilson loop – defined on polygonal contours – with a Lagrangian, normalized by the vacuum expectation value of the Wilson loop. Thanks to taking the ratio, this object is free from divergences. This object is related \(at least, conjecturally\) to correlation functions of local operators, and to scattering

– 2 –

amplitudes in that theory. A good way of thinking about this triality is in terms of the integrands of the three objects. To define an integrand of an L-loop observable, one uses the Lagrangian insertion technique. This naturally gives a formulation where the integrand is given by a rational function. Assuming the triality, if one starts with the \(L \+ 1\)-

loop integrand of the logarithm of the maximally-helicity-violating \(MHV\) amplitude, and performs L of the integrations, then this is equivalent to the above ratio of Wilson loops. 

In summary, Wilson loops with a Lagrangian insertion are finite observables in maximally supersymmetric Yang-Mills theory. In the large Nc limit, their integrand is given directly by the MHV loop Amplituhedron. Therefore the question of what transcendental functions arise from those positive geometries can be formulated in a transparent and direct way, without the need of infrared regularization of subtractions. 

Wilson loops with a Lagrangian insertion have been first studied in references \[10–12\]. 

Perturbative results for four and five points are known to three and two loops from references

\[13–15\], and \[16, 17\], respectively. The integrated functions obtained from canonical forms associated to geometries have a number of interesting properties. Due to the dual conformal symmetry of sYM, they depend on \(3n − 11\) cross-ratios \[10\]. This is the same number of variables as n-particle on-shell scattering amplitudes in generic theories depend on. One may use dual conformal transformations to send the Lagrangian insertion point to infinity, which suggests that a connection to Wilson loops in non-dual conformal theories, without Lagrangian insertion. The latter are kinematically equivalent to non dual-conformal scattering amplitudes. Indeed, the function space encountered in perturbative calculations so far matches that of generic scattering amplitudes. Being finite, the results have a similarity with infrared finite parts of scattering amplitudes. 

The results have a structure reminiscent of next-to-MHV \(NMHV\) scattering amplitudes: they can be expanded in terms of transcendental functions and leading singularities. 

The leading singularities were studied in \[16\]. It was conjectured that they are given by a Grassmannian formula that enjoys both a dual conformal and a conformal symmetry \(in a special dual conformal frame\). The latter does not automatically follow from the Yangian symmetry of sYM \[18\], since the Lagrangian integration point is not integrated over. 

The underlying Amplituhedron geometry motivates studying positivity properties of the integrated answers, as in the case of scattering amplitudes \[19\]. While in the latter case one needs to choose an infrared subtraction scheme, the Wilson loops with Lagrangian insertion are infrared finite. Very interestingly, the results computed so far have been observed to be positive, when evaluated inside certain kinematic regions that are suggested by the geometry \[17, 20\]. This positivity comes about as a non-trivial cancellation of different contributions, and involves an interplay of the leading singularities and the transcendental functions. 

One of the motivations of the present paper is to explore further the connection between geometry of integrands and posivity properties of integrated functions. We therefore wish to provide more detailed perturbative data. Indeed, a “negative geometry” expansion of the Wilson loop has been proposed in reference \[20\], which further decomposes the answer in terms of building blocks that each have a geometric interpretation. This decomposition in general is different from a Feynman diagram expansion. At two loops, there are

– 3 –

three contributions: a factorized, one-loop squared contribution, which is trivially known; a

“ladder-type” contribution \(in terms of the geometry\), and a “loop-type” contribution. Since the full five-point answer is already known \[17\], it is sufficient to compute the “ladder-type” 

contribution, in order to be able to provide the full decomposition. This is the goal of the present paper. 

The geometric decomposition goes beyond standard Feynman diagram expansions. 

Therefore we define more general Feynman integrals, and compute them via the differential equations method, generalizing the work done in references \[21\]. The ladder-type geometries are also known to satisfy a particular d‘Alembertian differential equation \[20, 22\]. In a complementary analysis, we study how this equation may be used to perform a symbol bootstrap of the answer. This may have higher-loop applications. However, as we also discuss, further information about the relevant function space is required to implement this program. 

The outline of this paper is as follows: In section 2, we recall the definition of the Wilson loop with Lagrangian insertion, and how it may be decomposed in terms of “negative” 

geometries. In section 3, we construct an infinite class of ladder-type geometries at five points. We then proceed, in section 4, to discuss the structure of integrated loop corrections at five points. Sections 5 and 6 are devoted to evaluating the ladder-type geometries via differential equations, and investigate positivity properties of Wilson loop observable and negative geometries in the Amplituhedron region. Sections 7 and 8 provide an alternative, bootstrap approach to evaluating ladder-type negative geometries. We derive, in section 7, 

a powerful d‘Alembert-type differential equation, and in section 8, we combine this equation with a suitable ansatz for the pentagon function space, which allows one to uniquely fix the answer. We demonstrate this to two loops for a minimal ansatz, and find that at three loops novel alphabet letters are required, for which we make a proposal. We present a summary and conclusion in section 9. Appendix A contains the relevant information on the function spaces used in this paper. Appendix B reviews pentagon functions and their derivatives. Appendix C explores various kinematic limits of the integrated negative geometries, including the soft/collinear limits, where the observables reduce to the four-cusp case recalled in appendix D. 

2

Two-loop negative geometry decomposition of the Lagrangian inser-

tion in the Wilson loop

We consider an n-cusp polygon \[x1, . . . , xn\] with light-like edges, 

\(xi − xi\+1\)2 = 0 , 

i = 1, . . . , n , 

\(2.1\)

embedded in Minkowski space, and xn\+1 ≡ x1. Along this polygonal contour, we define the Wilson loop in the fundamental representation of the gauge group SU\(Nc\), 



I



WF\[x1, . . . , xn\] = trF Pexp i gYM ta

Aaµdxµ . 

\(2.2\)

– 4 –

The main object of our interest is the following ratio of the correlation functions, 1

⟨WF\[x1, . . . , xn\]L\(x0\)⟩

Fn\(x0; x1, . . . , xn\) =

, 

\(2.3\)

π2

⟨WF\[x1, . . . , xn\]⟩

which we refer to as the Lagrangian insertion in the Wilson loop. The composite operator L

is the chiral Lagrangian of N = 4 sYM, which is a conformal operator of dimension 4. Due to the ultra-violet finiteness of the theory and the conformal nature of the Lagrangian, the correlators in \(2.3\) are free from ultra-violet divergences. However, they do contain cusp divergences \[23, 24\], which come from gluon exchanges in the vicinity of the Wilson loop cusps. The cusp divergences cancel out in the ratio \(2.3\), so Fn is finite in four space-time dimensions. 

We consider the weak coupling

N

g2 ≡ g2YM c perturbative expansion of F

16

n in the large

color Nc → ∞ limit, 

X

Fn =

\(g2\)1\+LF \(L\)

n

, 

\(2.4\)

L≥0

which starts at order g2. The simplest nondegenerate light-like polygonal contour has n = 4

cusps. The Born-level contribution \(0\)

\(1\)

Fn

and one-loop correction Fn have been calculated

for any number of cusps

\(L\)

n in \[16\]. In the four-cusp case, the perturbative corrections F4

are known up to order

\(2\)

L = 3 \[13–15\]. In the five-cusp case, the two-loop correction F

is

5

available \[17\]. 

The cancellation of divergences in the ratio \(2.3\), conformal invariance of the quantum theory, and conformal nature of the involved operators lead to conformal covariance of Fn. 

Due to the nontrivial conformal weight of the Lagrangian, Fn carries conformal weight

\+4 with respect to x0 and zero conformal weight with respect to the cusp coordinates. 

The conformal symmetry severely restricts the kinematic dependence of Fn. Because of relations to scattering amplitudes, we adopt the amplitude terminology and refer to the space-time conformal symmetry as the dual-conformal symmetry. In the four-cusp case, the dual-conformal symmetry implies that F4 is a nontrivial function of one variable. In what follows we are mainly interested in the five-cusp case, n = 5, and we tacitly omit index the n. Up to a rational prefactor that absorbs the dual-conformal weight, F5 is a function of four independent dual-conformal cross-ratios, which we can choose as follows, x2 x2 x2

x2 x2

x2 x2

x2 x2 x2 

u =

10 40 25 , 40 13 , 10 24 , 10 40 35

, 

\(2.5\)

x2 x2 x2

x2 x2

x2 x2

x2 x2 x2

20 50 14

30 14

20 14

30 50 14

where x2 := \(x

ab

a − xb\)2. 

The correlator ratio Fn is intimately related to MHV scattering amplitudes and their four-dimensional integrands. The kinematics of amplitudes is specified by n light-like momenta \(p2 = 0\) satisfying the momentum conservation, 

i

p1 = xn − x1 , 

pi = xi − xi−1 , 

i = 2, . . . , n . 

\(2.6\)

The vacuum expectation values of the null Wilson loop, ⟨WF\[x1, . . . , xn\]⟩, are equal to n-particle MHV amplitudes in the large color limit \[24–26\] provided dimensional regularizations D = 4−2ϵ of the two objects are properly identified. Then, applying the Lagrangian

– 5 –

insertion formula \[10–12, 27\], we obtain the following relation between Fn and the logarithm of the MHV amplitude, 

Z

dDx0

g2∂g2 log⟨WF⟩ =

Fn\(x0\) . 

\(2.7\)

i D

π 2

Namely, according to eq. \(2.7\), 

\(L\)

L-loop correction Fn

is obtained from the \(L \+ 1\)-loop

integrand of the logarithm of the MHV amplitude where L loop integrations are carried out. The remaining loop integration is divergent and requires a regularization in eq. \(2.7\). 

It corresponds to cusp divergences of log⟨WF⟩ which manifest themselves as poles 1/ϵ2. 

In order to describe the loop integrand of the Lagrangian insertion in the Wilson loop and negative geometries, and relate it to the Amplituhedron construction, we employ the momentum twistors \[3\]. The momentum twistor variables are very convenient for massless scattering since they automatically resolve the momentum conservation and take into account the light-like nature of the momenta. A space-time coordinate \(dual momenta\) is equivalent to a line in momentum twistor space, which can be specified by a pair of momentum twistors belonging to it. For example, the Lagrangian coordinate is represented as follows, x0 ∼ ZAZB where ZA = \(λα, x ˙ααλ

, x ˙ααλ

A

0

A α\) and ZB = \(λα

B

0

B α\), and λA, λB is

a pair of helicity spinors. Similarly, each loop variable is represented by a pair momentum twistors. In what follows, we label the loop variables of the integrands as ABi, i = 1, . . . , L, and x0 ∼ AB0. The cusps of the Wilson loop contour are light-like separated that is equivalent to intersection of the corresponding momentum twistor lines. These n intersecting momentum twistors lines are specified by n momentum twistors \{Zi\}n located at their i=1

intersections and xi ∼ ZiZi\+1, with i = 1, . . . , n and n \+ 1 ≡ 1. They have the following explicit expressions, Zi = \(λα, x ˙ααλ

= ˜

λ ˙αλα. 

i

i

i α\) where λi, ˜

λi is a pair of helicity spinors, p ˙αα

i

i

i

Let us briefly recall the Amplituhedron construction of the MHV loop integrand in the planar N = 4 sYM theory, and the connection to the Wilson loop with the Lagrangian insertion. In the Amplituhedron picture \[4, 28\] we consider a space of L lines ABi, i =

1, 2, . . . , L which are subject to a set of inequalities:

For each loop: ⟨ABi j j\+1⟩ > 0 for j = 1, 2, . . . , n−1, and ⟨ABi1n⟩ > 0

sequence \{⟨ABi1j⟩\} for j = 2, . . . , n has 2 sign flips

\(2.8\)

For each pair of loops: ⟨ABiABj⟩ > 0

\(2.9\)

The n-point MHV L-loop integrand then corresponds to the canonical differential form ΩL

with logarithmic singularities on the boundaries of this space. We call such integrands

“dlog” forms. 

A variation of this picture leads to the definition of negative geometries. To specify a particular negative geometry we use a graphic representation where the vertices correspond to loop lines ABi, each of them satisfying the one-loop Amplituhedron conditions \(2.8\), 

while links represent mutual negativity conditions ⟨ABiABj⟩ < 0. Each negative geometry is then equipped with a canonical form Ω with logarithmic singularities on the boundaries of the space. 

– 6 –



As was proven in \[20\], we can construct the integrand for the logarithm of the amplitude e

ΩL as a sum of dlog forms on all connected negative geometries:

X

e

ΩL =

\(−1\)E\(g\) e

Ωg , 

\(2.10\)

g with L nodes

where the subscript g sums all connected graphs at L loops, i.e. graphs with L nodes, and E\(g\) denotes number of edges in a graph. The full integrand for logarithm of the amplitude as an expansion in g is given by

∞

X

e

Ω =

g2L e

ΩL . 

\(2.11\)

L=1

Note that the individual terms eΩg have unit leading singularities but the overall sign is not fixed \(because both eΩg and −eΩg have correct singularity properties\). The ambiguity of these signs in \(2.10\) is completely fixed once we require that the integrand of the logarithm of the amplitude can be also expressed in terms of products of ordinary loop integrands – these are represented as certain special positive geometries: graphs with L nodes and positive links, where nodes are divided into subgroups that each separately form a complete graph \(this is equivalent to having products of amplitudes\). As result, the only sign ambiguity is the overall sign of eΩL. 

For example, for L = 2 there is only one negative geometry, i.e. one graph, while for L = 3 we have two different negative geometries:

e

Ω2 = −

, 

\(2.12\)

e

Ω3 =

−

. 

\(2.13\)

In all these pictures the complete symmetry in all ABi is implied. 

The integrand for the amplitude logarithm has very special infrared \(IR\) properties \(which are equivalent to the ultraviolet, cusp properties, of the Wilson loop discussed above\): when integrated over all loop momenta ABi at any loop order L, its leading divergence is a 1/ϵ2 pole, as opposed to a naive 1/ϵ2L one. Furthermore, if one of the loops is kept frozen \(i.e, not integrated over\), the result is finite. The resulting function is equal to \(L\)

Fn , see eqs. \(2.3\) and \(2.4\), the L-loop contribution to the Wilson loop with Lagrangian insertion. The role of the insertion point is played by the frozen loop, which we denote by AB0. We introduce a graphical notation where the marked point AB0 is indicated by a crossed circle, while all other ABi, i = 1, 2, . . ., L are indicated by black vertices, as before. 

The following graph serves as an example, 

\(2.14\)

. 

– 7 –

In this picture all loops, except for the one corresponding to the marked point AB0, are integrated over. This results in certain transcendental functions \(with rational prefactors\) in AB0 and in the external kinematic variables\). We will refer to objects such as eq. \(2.14\)

as integrated negative geometries. 

Note that because of the total symmetry of the integrand in all ABs, the integrated negative geometries pick up symmetry factors. For example, at the first two loop orders, 

−→

, 

\(2.15\)

1

−→

\+

, 

\(2.16\)

2

−→

. 

\(2.17\)

We see in the middle equation that a single negative geometry leads to two different contributions to the Wilson loop, according to where the frozen loop is located. The contributions to the L-loop function in eq. \(2.4\) is obtained by performing L integrations on eΩL\+1 with AB0 frozen 1

Z

F \(L\) = −g2

e

ΩL\+1\(AB0, AB1, .., ABL\) . 

\(2.18\)

AB1,...,ABL

In this notation, the one-and two-loop functions F \(1\) and F \(2\) are expressed as follows, F \(1\) = F \(

\) , 

\(2.19\)

1

1

\(

\)

F \(2\) = − F \(

\) − F \(

\) \+ F

, 

\(2.20\)

2

2

where F \(g\) denotes the contribution from a specific graph, 

Z

F \(g\) = −g2

e

Ωg\(AB0, AB1, .., ABL\) . 

\(2.21\)

AB1,...,ABL

Note that there is a shift in the loop order: an \(L \+ 1\)-loop integrand is associated to an L-loop integrated result F \(L\), as we are freezing one of the loops. 

The detailed discussion of the four-point case is presented in \[20\]. In that case the integrands for all tree negative geometries, i.e. graphs with no cycles, were found in a very compact form. A special form of these integrands allowed to derive a differential equation for the integrated negative geometries and found the result at all loops. This also allowed for the strong coupling expansion and surprisingly good qualitative agreement for the cusp anomalous dimension. Negative geometries with internal cycles are more complicated: canonical forms for all geometries with one cycles were found in \[22\], but the 1To avoid clutter of notation, we refrain from introducing FL, used in \[20\], to denote the integrated loop form. Instead, we directly define the F \(L\) in \(2.4\) via performing L integrations on e ΩL\+1. Strictly

speaking, the RHS of eqs. \(2.21\) is a differential form in AB0. For simplicity of notation, in this and in the following, we will tacitly drop a measure factor when identifying integrated negative geometries with F \(L\). 

– 8 –





same differential method does not work. The evaluation and resummation of a subclass of these diagrams is work in progress \[29\]. 

Most of this remarkable progress is limited to n = 4. The decomposition of the integrand of the amplitude logarithm as the sum of dlog forms on negative geometries is valid for any n, as well as the equality between the Wilson loop with a Lagrangian insertion and the integrated negative geometries with a marked point. However, the integrand for the negative geometries is more complicated, and also the integrated results are more complex: they depend on multiple cross-ratios and we also have non-trivial prefactors \(leading singularities\) unlike in the four-point case. In this paper we focus on the n = 5 case. The next section is dedicated to deriving canonical forms for its geometric integrand decomposition. 

3

Momentum-twistor integrands for the negative geometries

Having reviewed the geometric expansion of the Wilson loop with Lagrangian insertion, we now discuss what this implies in terms of loop integrands. To find the dlog form for complicated negative geometries is a challenging open problem. A conceptually clear procedure to find the integrands for negative geometries is to triangulate the associated spaces. In principle, this is a straightforward procedure of solving inequalities, but in practice it becomes very complicated even for a low number of loops. In this paper we will use a hybrid triangulation / unitarity-based method to calculate the integrand. As we will discuss presently, this is particularly efficient for the ladder geometries, which are as follows, 

. 

\(3.1\)

Note that this is very different from the ladder Feynman diagrams. This was also the first approximation considered for n = 4 \[20\]. 

We consider a general ladder negative geometry

, 

\(3.2\)

where here we labeled all loops: ABk, k = 1, 2, . . ., L and a marked point AB0. While we will construct here the integrand for this geometry, we will later integrate over all loops except for AB0. 

The marked point AB0 can be also located in the middle of the chain. We refer to this as product ladder negative geometry, 

, 

\(3.3\)

where here we denoted the loops on one side ABk for k = 1, . . ., L1 and from the other side CDl for l = 1, . . ., L2 such that L1 \+ L2 = L. Note that the integrands for both of these pictures are the same \(up to relabeling of the loops\) but we consider them separately because the integration procedure obviously distinguishes between them. 

– 9 –



3.1

Generalized-unitarity-inspired derivation of the ladder integrand

Our goal is to present the integrand for the ladder negative geometry in the following way: X

\(k\)

ΩL =

Ωk × Ω

\(AB

0

0\) , 

\(3.4\)

k

where Ωk can be written as a sum of dlog forms in AB1 . . . ABk, i.e. the integrand has unit leading singularities when we localize all

\(k\)

ABk on cuts. The “coefficients” Ω

\(AB

0

0\)

are dlog forms in AB0 and do not depend on any of the ABk loops. As we do not think about AB0 as the loop to integrate over but a fixed point, we later tacitly drop a measure in AB0. 

This expansion \(3.4\) is reminiscent of the generalized unitarity approach when we write the integrand for the amplitude as a sum of basis integrands multiplied by coefficients \(leading singularities\) which only depend on external kinematics. Here Ωk are not planar diagrams in the usual sense, but they can be written in the momentum twistor space. This organization of the result is motivated by the structure after integration, X

\(k\)

F ladder

L

=

fk × Ω

\(AB

0

0\) , 

\(3.5\)

k

where the

\(k\)

fk are transcendental functions, and Ω

\(AB

0

0\) are rational prefactors2 \(both

depend on cross ratios of external kinematics and on AB0\). The latter can be interpreted as leading singularities of the integrand. The classification of the complete set of all such factors that can appear in any negative geometry or in the full observable is an important question \[16\], which will be further addressed in \[30\]. 

In order to write down the form Ω without the need of triangulation of the space we use the chiral box expansion \[31–33\]. This is a refinement of the generalized unitarity where we pre-diagonalize the basis according to the list of cuts we wish to match. It is a one-loop version of the prescriptive unitarity approach to construct higher-loop integrands \[34–36\]. 

The chiral box expansion uses a convenient infrared-friendly basis which nicely separates IR finite and IR divergent integrals, which is especially advantageous when dealing with infrared-finite objects. In fact, we will write Ωladder in a form where each term is infrared L

finite. 

According to the generalized unitarity strategy, we ensure that the terms in this expansion match exactly one physical cut of interest and vanishes on all other cuts. Once all the physical cuts are matched, we check that all spurious cuts cancel. This then concludes the proof that the obtained formula is correct. Let us first show a few low loop examples, before formulating the general procedure. 

Two-loop integrand

Let us first demonstrate it the simplest case of L = 1, i.e. the two-loop integrand Ω1 which is given as the canonical form on the negative geometry, 

. 

\(3.6\)

2We have tacitly dropped a measure factor in AB0. 

– 10 –

For simplicity we denote CD ≡ AB1 and AB ≡ AB0. The space of all CD lines is just a one-loop Amplituhedron with the extra condition ⟨CDAB⟩ < 0. When we perform the quadruple cut on CD \(not cutting ⟨ABCD⟩\), the list of all allowed leading singularities is CD = 13, 24, 35, 14, 25 . 

\(3.7\)

Note that all leading singularities of the type CD = i i\+1 are not allowed because they would imply ⟨AB i i\+1⟩ < 0 which would violate the one-loop Amplituhedron inequalities for AB. The absence of these leading singularities is also related to infrared finiteness. Each of the five allowed leading singularities in eq. \(3.7\) can be matched by a chiral pentagon integral. Namely, for the leading singularity at CD = 13, we write down

⟨CD\(512\)∩\(234\)⟩⟨AB13⟩

C13\(CD, AB\) =

, 

\(3.8\)

⟨CD12⟩⟨CD23⟩⟨CD34⟩⟨CD15⟩⟨ABCD⟩

and similar for the other Cii\+2. In total we have five cyclically related terms, and each of them gives a unit leading singularity on one of the quadruple cuts \(3.7\), and vanishes on all other four cuts. 

Note that eq. \(3.8\) has support on singularities of other quadruple cuts involving the

⟨ABCD⟩ propagator, but these are not in our list of cuts to match \(they are redundant in this logic and must be matched automatically\). In principle, we could also consider an integrand of the form

\#

, 

\(3.9\)

⟨CD15⟩⟨CD12⟩⟨CD34⟩⟨ABCD⟩

which has no support on any of the leading singularities \(3.7\) and has non-vanishing residues on quadruple cuts involving ⟨ABCD⟩ = 0. However, this integral is necessarily IR divergent

– in the cut structure this is manifest by the presence of a spurious leading singularities CD = \(512\) ∩ \(134\). This singularity is obviously absent in all Ci i\+2 integrands, and is also absent in the form Ω1 for the negative geometry \(3.6\). Hence, \(3.9\) has no place in the expansion for Ω1 and we can write

X

Ω1 =

C13\(CD, AB\) × Ω13−\(AB\) . 

\(3.10\)

0

cycl

The coefficient Ω13−\(AB\) is the dlog form on the remaining geometry when we localize 0

CD on the leading singularity, CD = 13. We get a one-loop Amplituhedron with an extra condition ⟨AB13⟩ < 0 which originates from ⟨ABCD⟩ < 0 for CD = 13. For us this coefficient is the leading singularity of the form Ω1 as the loop AB is frozen for us \(and treated as external data\). 

In order to calculate the form Ω13− we have to go back to the triangulation of the five-0

point one-loop Amplituhedron. According to eq. \(2.8\), we have to impose ⟨AB i i\+1⟩ > 0

and the series\{⟨AB1i⟩\} for i = 2, 3, 4, 5 has two sign flips. Because now we impose explicitly

⟨AB13⟩ < 0 we get a more stringent sign flip condition, 



\! 

⟨AB12⟩ ⟨AB13⟩ ⟨AB14⟩ ⟨AB15⟩

. 

\(3.11\)

\+

−

∗

\+

– 11 –



As a result, we get two terms depending on the sign of ⟨AB14⟩. Each of them is just a simple kermit form \[37\] \(eq. \(32\)\) with known dlog form, 

⟨1234⟩2

∗ = \+ :

\[123, 134\] =

≡ −B

⟨

5

\(3.12\)

AB12⟩⟨AB23⟩⟨AB34⟩⟨AB14⟩

⟨AB\(123\) ∩ \(145\)⟩2

∗ = − :

\[123, 145\] =

. 

\(3.13\)

⟨AB12⟩⟨AB13⟩⟨AB23⟩⟨AB14⟩⟨AB15⟩⟨AB45⟩

While the first term is a box integral \(we denoted it as B5\), the second term is a general kermit. For our purpose it is useful to choose the following basis of the AB-forms \[16, 17\], 

B = \{B1, B2, B3, B4, B5, Atree\}

\(3.14\)

5

where Bj are box integrands: B1\(2345\), B2\(3451\), B3\(4512\), B4\(5123\), B5\(1234\) where the propagator structure is obvious from B5 above. We also denoted

Atree ≡ I1−loop

5

\(AB\) = \[123, 134\] \+ \[123, 145\] \+ \[134, 145\]

\(3.15\)

5

which is the one-loop five-point MHV integrand for the loop AB. We rewrite the kermit term as

\[123, 145\] =Atree −

5

\[123, 134\] − \[134, 145\]

\(3.16\)

=Atree

5

\+ B5 \+ B2 , 

and we get for Ω13−\(AB\), 

0

Ω13−\(AB\) =\[123, 134\] \+ \[123, 145\]

0

\(3.17\)

=Atree

5

\+ B2 . 

The other forms are related by cyclic shifts. 

Ω14−\(AB\) =

Atree

\(AB\) = Atree

0

5

\+ B5, 

Ω24−

0

5

\+ B3, 

Ω25−\(AB\) =

Atree

\(AB\) = Atree

0

5

\+ B1, 

Ω35−

0

5

\+ B4 . 

Note that, interestingly, only five linear combinations of the six basis elements B appear in the expansion for Ω1. To conclude, we can write the form Ω1 for the two-loop ladder in the following way, 

X

Ω1 =

Cab\(CD, AB\) × Ωab−\(AB\) , 

\(3.18\)

0

ab

where the sum is over ab = 13, 24, 35, 14, 25. 

Three-loop integrand

Let us consider the next case, which is an integrand for the three-loop ladder corresponding to the two-loop problem, 

. 

\(3.19\)

– 12 –



We are supposed to integrate over CD, EF keeping AB fixed. We start with the chiral box expansion on the EF loop. We get

X

Ω2 =

C13\(EF, CD\) × Ω13−

1

\(CD, AB\) , 

\(3.20\)

cycl

where the leading singularities in EF are matched by chiral boxes. Using the same argument as before, no other EF -dependent term can appear in Ω2 \(otherwise we would introduce spurious singularities that do not cancel\). Next, we want to do the chiral box expansion on the object Ω13−\(CD, AB\) which is just a two-loop negative ladder with an extra condition 1

⟨CD13⟩ < 0, i.e. 

. 

\(3.21\)

This space now has an extra boundary ⟨CD13⟩ = 0 which shows up as the pole in the denominator. This makes the chiral box expansion tricky, since a pole ⟨CD13⟩ is always spurious in the amplitude, but we can use a small trick to avoid the problem. We perform the chiral box expansion on the AB loop \(this is a regular one-loop Amplituhedron\). This gives us the correct form for Ω13−\(CD, AB\). Once this is obtained, we use it as a reference 1

formula, and rewrite the result as a chiral box expansion on CD with coefficients in AB. 

The chiral box expansion on AB is easily obtained: it is the usual one with five leading singularities, 

X

Ω13−

C

1

\(CD, AB\) =

ab\(AB, C D\) × Ω13−,ab−\(C D\) . 

\(3.22\)

0

ab

Now we need to calculate the coefficients, i.e. the Ω0\(CD\) terms. Note that the superscript indicates which conditions ⟨CDij⟩ < 0 are imposed on CD on the top of just being in the one-loop Amplituhedron. Some of these terms are just regular kermits and sums of kermits, namely

⟨CD\(123\) ∩ \(145\)⟩2

Ω13−\(CD\) =

0

⟨CD12⟩⟨CD23⟩⟨CD13⟩⟨CD14⟩⟨CD15⟩⟨CD45⟩

⟨1234⟩2

\+

, 

\(3.23\)

⟨CD12⟩⟨CD23⟩⟨CD34⟩⟨CD14⟩

⟨CD\(123\) ∩ \(345\)⟩2

Ω13−,35−\(CD\) =

, 

\(3.24\)

0

⟨CD34⟩⟨CD35⟩⟨CD45⟩⟨CD13⟩⟨CD23⟩⟨CD12⟩

⟨CD\(123\) ∩ \(145\)⟩2

Ω13−,14−\(CD\) =

. 

\(3.25\)

0

⟨CD12⟩⟨CD13⟩⟨CD23⟩⟨CD14⟩⟨CD15⟩⟨CD45⟩

Note that the term Ω13−,35− can be obtained directly as one kermit from the sign flip series 0

starting with 3:



\! 

⟨CD34⟩ ⟨CD35⟩ ⟨CD13⟩ ⟨CD23⟩

. 

\(3.26\)

\+

−

−

\+

– 13 –

the term Ω13− is just a sum of two kermits: Ω13−,35− and

0

0



\! 

⟨CD34⟩ ⟨CD35⟩ ⟨CD13⟩ ⟨CD23⟩

. 

\(3.27\)

\+

\+

−

\+

and Ω13−,14−\(CD\) is again just a single kermit, 

0



\! 

⟨CD12⟩ ⟨CD13⟩ ⟨CD14⟩ ⟨CD15⟩

. 

\(3.28\)

\+

−

−

\+

The last two terms Ω13−,ab−\(CD\) for ab = 24, 25 in \(3.22\) are more interesting because they 0

do not correspond to a kermit. Let us start with Ω13−,24−\(CD\). This form can be obtained 0

by starting with ⟨CD13⟩ < 0 space – that is a sum of two kermits \[123, 134\] and \[123, 145\], and impose additional ⟨CD24⟩ < 0 condition. The first kermit incorporates this condition automatically, and the form is given by B5, see eq. \(3.12\). The other kermit geometry gets effectively “chopped” by the ⟨CD24⟩ < 0 condition. To obtain the canonical forms for these spaces we start in the kermit space and solve extra inequalities. As a result the space has six boundaries, and the associated canonical form has six poles and two distinct numerator factors, 

⟨CD\(451\) ∩ \(123\)⟩⟨CD\(234\) ∩ \(451\)⟩

Ω13−,24−\(CD\) =

0

⟨CD14⟩⟨CD23⟩⟨CD13⟩⟨CD15⟩⟨CD45⟩⟨CD24⟩

⟨1234⟩2

\+

, 

\(3.29\)

⟨CD12⟩⟨CD23⟩⟨CD34⟩⟨CD14⟩

and similarly, 

⟨CD\(123\) ∩ \(345\)⟩⟨CD\(345\) ∩ \(512\)⟩

Ω13−,25−\(CD\) =

0

⟨CD35⟩⟨CD12⟩⟨CD13⟩⟨CD34⟩⟨CD45⟩⟨CD25⟩

⟨1235⟩2

\+

. 

\(3.30\)

⟨CD12⟩⟨CD23⟩⟨CD15⟩⟨CD35⟩

This finishes the construction of the form Ω2. However, we want to reorganize the expansion for Ωij−\(CD, AB\) and write it as an expansion in CD with coefficients in AB, rather than 1

the other way around. Using eq. \(3.22\) as a reference result, together with a simple hybrid method of ansatz, and imposing cuts we can rewrite it in the following form, X

Ω13−\(CD, AB\) =

C

\(AB\) , 

\(3.31\)

1

13,ab\(C D, AB\) × Ωab−

0

ab

– 14 –

where we denoted

⟨1235⟩⟨AB13⟩

⟨1234⟩⟨AB13⟩

C13,13 =

−

, 

⟨CD51⟩⟨CD13⟩⟨CD23⟩⟨ABCD⟩

⟨CD34⟩⟨CD13⟩⟨CD12⟩⟨ABCD⟩

⟨CD\(123\) ∩ \(345\)⟩⟨AB24⟩

C13,24 =

, 

⟨CD12⟩⟨CD23⟩⟨CD34⟩⟨CD45⟩⟨ABCD⟩

⟨CD\(123\) ∩ \(451\)⟩⟨AB35⟩

C13,35 = −

, 

⟨CD23⟩⟨CD13⟩⟨CD45⟩⟨CD51⟩⟨ABCD⟩

⟨CD\(123\) ∩ \(345\)⟩⟨AB14⟩

C13,14 = −

, 

⟨CD12⟩⟨CD13⟩⟨CD34⟩⟨CD45⟩⟨ABCD⟩

⟨CD\(123\) ∩ \(451\)⟩⟨AB25⟩

C13,25 =

. 

\(3.32\)

⟨CD12⟩⟨CD23⟩⟨CD45⟩⟨CD51⟩⟨ABCD⟩

The AB leading singularities Ωij−\(AB\) have been calculated before, see eqs. \(3.17\) and \(3.18\). 

0

Note that \(3.22\) and \(3.31\) represent the same expression, just organized differently. It was easy for us to write \(3.22\) using chiral box expansion as there were not extra conditions imposed on the line AB, so we can treat it as a one-loop Amplituhedron and expanded the integrand in terms of building blocks. On the other hand, in \(3.31\) we expand in CD but there is an additional condition ⟨CD13⟩ < 0 imposed so the standard chiral box expansion naively does not work as we can not treat the CD space as the one-loop Amplituhedron. 

Our result \(3.31\) does provide an extension of the chiral box expansion to the space where additional condition ⟨CD13⟩ < 0 is imposed. 

As a result, this allows us to write the final result for the canonical form Ω2 of the three-loop ladder as

X

Ω2 =

Cab\(EF, CD\) × Cab,cd\(CD, AB\) × Ωcd−\(AB\) , 

\(3.33\)

0

ab,cd

where the sum runs over ab, cd = 13, 24, 35, 14, 25 and Cab,cd are related with C13,ij by cyclic shifts. Note that C13,cd\(CD, AB\) has a pole ⟨CD13⟩ in the denominator, but it is canceled by the numerator of C13\(EF, CD\). 

Just for convenience, we collect together all terms in eq. \(3.33\) that multiply the AB-basis elements in Ω2, and reorganize the sum as

5

X

\(k\)

Ω2 = Ωtree ×

×

2

Atree

5

\+

Ω

B

2

k . 

\(3.34\)

k=1

Writing now

Ωtree

2

= ΩA \+ ΩB \+ ΩC \+ ΩD \+ ΩE , 

\(3.35\)

– 15 –



where we have

⟨CD13⟩⟨CD\(123\) ∩ \(345\)⟩⟨EF \(512\) ∩ \(234\)⟩⟨AB24⟩

ΩA = ⟨EF51⟩⟨EF12⟩⟨EF23⟩⟨EF34⟩⟨CDEF⟩⟨CD12⟩⟨CD23⟩⟨CD34⟩⟨CD45⟩⟨ABCD⟩

⟨CD13⟩⟨CD\(123\) ∩ \(451\)⟩⟨EF \(512\) ∩ \(234\)⟩⟨AB25⟩

ΩB = ⟨EF51⟩⟨EF12⟩⟨EF23⟩⟨EF34⟩⟨CDEF⟩⟨CD12⟩⟨CD23⟩⟨CD45⟩⟨CD51⟩⟨ABCD⟩

⟨CD\(123\) ∩ \(451\)⟩⟨EF \(512\) ∩ \(234\)⟩⟨AB35⟩

ΩC = − ⟨EF51⟩⟨EF12⟩⟨EF23⟩⟨EF34⟩⟨CDEF⟩⟨CD23⟩⟨CD45⟩⟨CD51⟩⟨ABCD⟩

⟨CD\(123\) ∩ \(345\)⟩⟨EF \(512\) ∩ \(234\)⟩⟨AB14⟩

ΩD = − ⟨EF51⟩⟨EF12⟩⟨EF23⟩⟨EF34⟩⟨CDEF⟩⟨CD12⟩⟨CD34⟩⟨CD45⟩⟨ABCD⟩

⟨EF \(512\) ∩ \(234\)⟩⟨AB13⟩⟨1235⟩

ΩE = \+ ⟨EF51⟩⟨EF12⟩⟨EF23⟩⟨EF34⟩⟨CDEF⟩⟨CD51⟩⟨CD23⟩⟨ABCD⟩

⟨EF \(512\) ∩ \(234\)⟩⟨AB13⟩⟨1234⟩

−

, 

\(3.36\)

⟨EF 51⟩⟨EF 12⟩⟨EF 23⟩⟨EF 34⟩⟨CDEF ⟩⟨CD12⟩⟨CD34⟩⟨ABCD⟩

and the B1 coefficient is

\(1\)

Ω

= Ω

2

A\(\+3\) \+ ΩB \(0\) \+ ΩC \(\+2\) \+ ΩD \(\+1\) \+ ΩE \(\+4\) , 

\(3.37\)

where we denoted Ω\(\+x\) a cyclic shift of external momentum twistors of Ω by \+x. Interestingly, the five integrals ΩA, ΩB, ΩC, ΩD, ΩE we need to calculate have pretty compact nice forms. 

General problem

The procedure outlined above generalizes to ladders of arbitrary length. We outline the general setup here. Consider the L-loop ladder, 

, 

\(3.38\)

where each point is in the n-pt MHV one-loop Amplituhedron, and for neighboring points we have ⟨ABiABj⟩ < 0. The strategy to write down the canonical form for this space is the following:

1. Start from the left and write down the chiral box expansion for the ABL loop \(no other integrals are allowed because of the absence of spurious cuts\). This matches all leading singularities in ABL. The prefactors are functions which depend on the other L − 1 loops. 

2. Each term in this expansion has support on one leading singularity ABL = ij, so the form of the remaining L − 1 loops corresponds to a negative geometry with an extra condition ⟨ABL−1ij⟩ < 0. 

X

ΩL =

Cij\(ABL, ABL−1\) × Ωij− \(AB

L−1

L−1, . . . AB0\) , 

\(3.39\)

ij

where Cij are chiral boxes, see eq. \(3.8\). 

– 16 –



3. Continue this procedure recursively until one reaches AB1. Then the coefficients Ωab−

0

depend on AB0 only, and can be expressed in the basis B of leading singularities, see eqs. \(3.14\), \(3.17\) and \(3.18\). 

Collect all pieces for the final result, we find

X

ΩL =

Ci

\(AB

\(AB

\(AB

1j1

L, ABL−1\) × Ci1j1,i2j2

L−1, ABL−2\) × Ci2j2,i3j3

L−2, ABL−3\) . . . 

· · · × Ci

\(AB

\(AB

L−1jL−1,iLjL

1, AB0\) × ΩiLjL−

0

0\) , 

\(3.40\)

where all the building blocks Cab, Ccd,ef and ΩiLjL−\(AB

0

0\) have been calculated above in

\(3.8\), \(3.32\), and \(3.17\). This simple expansion gives us the integrand for a general ladder of an arbitrary length. 

Note that each term in \(3.40\) is manifestly absent of spurious poles which appear in individual Cab, Ccd,ef, because of pairing of indices. The term Ccd,ef\(ABk, ABk−1\), which has a spurious pole ⟨ABkcd⟩ is always multiplied by Cab,cd\(ABk\+1, ABk\) which has the same factor in the numerator. Hence each term in \(3.40\) has only physical poles ⟨ABkj j\+1⟩, 

⟨ABkABl⟩. 

3.2

Product of ladders

The second negative geometry topology is when the marked point AB0 is in the middle of the ladder. As mentioned before, the integrand is the same \(up to relabeling of the loops\) as the integrand for the ladder with AB0 as the endpoint. 

However, for our purposes, we wish to present the result in the form \(3.4\), where the leading singularities in AB0 are explicit. This requires a reorganization of the integrand, which we discuss presently. 

We start with the L = 2 example, i.e. the three-loop ladder, 

. 

\(3.41\)

We perform a double chiral box expansion on CD and EF . As these two loops do not

“communicate” with each other \(via the mutual inequality on ⟨CDEF ⟩\), we can do these expansions independently, 

X

Ω2 =

Cab\(CD, AB\) × Ccd\(EF, AB\) × Ωab−,cd−\(AB\) . 

\(3.42\)

0

ab,cd

Here the AB-geometry is the one-loop Amplituhedron with additional conditions ⟨ABab⟩ < 0 and ⟨ABcd⟩ < 0. We have already encountered these spaces above, in the context of the chiral box expansion of Ω13−\(CD, AB\) in AB \(rather than CD\). Hence we can immediately 1

– 17 –



write down the result, 

⟨AB\(123\) ∩ \(145\)⟩2

Ω13−,13−\(AB\) = Ω13−\(AB\) =

0

0

⟨AB12⟩⟨AB23⟩⟨AB13⟩⟨AB14⟩⟨AB15⟩⟨AB45⟩

⟨1234⟩2

\+

, 

\(3.43\)

⟨AB12⟩⟨AB23⟩⟨AB34⟩⟨CD14⟩

⟨AB\(123\) ∩ \(345\)⟩2

Ω13−,35−\(AB\) = −

, 

\(3.44\)

0

⟨AB34⟩⟨AB35⟩⟨AB45⟩⟨AB13⟩⟨AB23⟩⟨AB12⟩

⟨AB\(123\) ∩ \(145\)⟩2

Ω13−,14−\(AB\) = −

, 

\(3.45\)

0

⟨AB12⟩⟨AB13⟩⟨AB23⟩⟨AB14⟩⟨AB15⟩⟨AB45⟩

⟨AB\(451\) ∩ \(123\)⟩⟨AB\(234\) ∩ \(451\)⟩

Ω13−,24−\(AB\) =

0

⟨AB14⟩⟨AB23⟩⟨AB13⟩⟨AB15⟩⟨AB45⟩⟨AB24⟩

⟨1234⟩2

\+

, 

\(3.46\)

⟨AB12⟩⟨AB23⟩⟨AB34⟩⟨AB14⟩

⟨AB\(123\) ∩ \(345\)⟩⟨AB\(345\) ∩ \(512\)⟩

Ω13−,25−\(AB\) =

0

⟨AB35⟩⟨AB12⟩⟨AB13⟩⟨AB34⟩⟨AB45⟩⟨AB25⟩

⟨1235⟩2

\+

. 

\(3.47\)

⟨AB12⟩⟨AB23⟩⟨AB15⟩⟨AB35⟩

The first three terms can be written in terms of the leading singularities B, cf. eq. \(3.14\), 

as follows, 

Ω13−,13−\(AB\) = Atree

0

5

\+ B2, 

Ω13−,35−\(AB\) = Atree

\(3.48\)

0

5

\+ B2 \+ B4 , 

Ω13−,14−\(AB\) = Atree

0

5

\+ B2 \+ B5 . 

However, the other two terms introduce new leading singularities. We can write Ω13−,24−\(AB\) =B

0

5 \+ C5 , 

\(3.49\)

Ω13−,25−\(AB\) =B

0

4 \+ C4 , 

where we introduced

⟨AB\(123\) ∩ \(345\)⟩⟨AB\(345\) ∩ \(512\)⟩

C4 ≡

, 

\(3.50\)

⟨AB35⟩⟨AB12⟩⟨AB13⟩⟨AB34⟩⟨AB45⟩⟨AB25⟩

and similarly for four other terms Ck, which are obtained by cyclic rotations. Hence our leading singularity basis has now a total of 11 terms, compared to the 6 terms in B \(3.14\). 

They appear in 10 combinations \(6 terms from B and 5 combinations Bi \+ Ci\). 

The construction for a general ladder is analogous. 

, 

\(3.51\)

where L1 \+ L2 = L. The form ΩL can be then written as

X

ΩL =

Ci

\(AB

, AB

\(AB

\(AB

1j1

L1

L1−1\) × Ci1j1,i2j2

L1−1, ABL1−2\) . . . CiL

j

1, AB0\)

1−1jL1−1,iL1 L1

× Ck \(CD , CD

\(CD

\(CD

1l1

L2

L2−1\) × Ck1l1,k2l2

L2−1, CDL2−2\) . . . CkL

l

1, AB0\)

2−1lL2−1,kL2 L2

i

j

−,k

l

−

× Ω L1 L1

L2 L2

\(AB

0

0\) . 

\(3.52\)

– 18 –

The logic of this formula is straightforward: we just apply twice the procedure from the previous subsection, once from the left on ABL , . . . , AB

1

1 and once from the right on

CDL . . . CD

2

1. The leading singularity is now the dlog form on the AB0 one-loop Amplituhedron with two extra conditions ⟨AB0iL j ⟩ < 0 and ⟨AB

l

⟩ < 0. 

1

L1

0kL2 L2

To summarize, in this section we have obtained the integrand for all five-point ladder geometries. Furthermore, as the main result of this section, eqs. \(3.40\) and \(3.52\) are written in a way that makes the leading singularities manifest. This is useful when discussing the structure of the integrated results in terms of transcendental functions, and prefactors \(given by the leading singularities\). This will be explored in the following sections. 

In addition to the six leading singularities known from references \[16, 17\], we saw that further leading singularities may arise from product-type geometries. However, it is known from the above references that at two loops, these additional leading singularities drop out in the full observable. This topic will be explored in more detail in reference \[30\]. 

4

Integrated negative geometries in five-particle kinematics

In the previous section we have obtained the loop integrands for ladder-type geometries, and identified their leading singularities. In this section, we discuss the structure one expects after integration. 

4.1

Five-particle kinematics

The Lagrangian insertion in the Wilson loop \(2.3\) and the individual negative geometries in its decomposition are dual-conformal covariant. In particular, the momentum twistor expressions for the integrands of the ladder geometries \(3.40\) and \(3.52\) make the dual conformal symmetry manifest. In the following, we find it convenient to fix the frame x0 → ∞ that corresponds to identifying AB0 with the infinity bi-twistor. In this frame, F

\(2.3\) and the negative geometries have residual Lorentz covariance. 

Then we switch from the dual-momenta, which are space-time coordinates of the polygonal contour cusps, to momenta variables. We assign five light-like momenta \{pµ\}5

to

i

i=1

the edges of the Wilson loop contour, 

pi = xi − xi−1 , 

\(pi\)2 = 0 , 

i = 1, . . . , 5 , 

\(4.1\)

where we assume that the labels take cyclic values from \{1, . . . , 5\}. Thus, the kinematics in the five-cusp case is the same as for the five-particle massless scattering, e.g. the kinematics of five-gluon scattering amplitudes in QCD. We choose bi-particle adjacent Mandelstam variables to specify the kinematic configuration, 

X := s



12 = x2

\(4.2\)

25 , s23 = x2

13 , s34 = x2

24 , s45 = x2

35 , s15 = x2

14

where sij := \(pi \+ pj\)2, and the non-adjacent bi-particle Mandelstam variables are linear combinations of \(4.2\), 

si i\+2 = si\+3 i\+4 − si i\+1 − si\+1 i\+2 , 

i = 1, . . . , 5 , 

\(4.3\)

– 19 –

where we assume the cyclicity of the labels. Also, the parity-odd Lorentz invariant is required to distinguish kinematic configurations of opposite parity, 

ϵ5 = 4iϵµνρσpµpν pσ

p p p p

1 2 pρ

3 4 = tr \(γ5 b1 b2 b3 b4\)

\(4.4\)

which value is fixed up to sign by the parity-even Mandelstam variables, 

\(ϵ5\)2 = ∆5 ≡ det \(sij|i,j=1,...,4\) . 

\(4.5\)

Although the Wilson loop is parity-even, the Lagrangian operator is chiral. Thus, the parity-odd ϵ5 appears in the expression for the correlator ratio F \(2.3\). 

4.2

Leading singularities in momentum space notation

In the four-cusp case, all negative geometries are proportional to the unique leading singularity, see appendix D. The five-cusp case is much more nontrivial, and eleven rational prefactors \(leading singularities\) are required to describe the two-loop negative geometries. 

Indeed, constructing the momentum-twistor integrands of the ladder negative geometries in section 3, we introduced the B basis \(3.14\) consisting of six elements, and we extended it with five \{Ci\}5 \(3.50\) considering product ladders. 

i=1

In order to establish a connection with definitions in \[17\], we introduce the following basis of 11 rational prefactors in the frame x0 → ∞, 

r0, r1, . . . , r5, r1, . . . , r5 , 

\(4.6\)

which have the following explicit expressions in momentum variables, 

r0 = tr− \(\(p

p

p

p

p

p

p

p

b1 \+ b2 \)\( b2 \+ b3 \)\( b3 \+ b4 \)\( b4 \+ b5 \)\) , 

\(4.7\)

si\+2 i\+3

ri =

tr− \(pi\+1 pi\+2 pi\+3 pi\+4\) , 

\(4.8\)

s

b

b

b

b

i\+1 i\+4

si i\+1si i\+4

ri =

tr− \(pi\+1 pi\+2 pi\+4 pi\+3\) , 

i = 1, . . . , 5 , 

\(4.9\)

s

b

b

b

b

i\+1 i\+3si\+2 i\+4

where we assume cyclicity of the momenta and Mandelstam labels, e.g. p6 ≡ p1, and we use the shorthand notation for the chiral trace

tr

1

− \(p p p p

tr \(\(1 − γ p p p p

bi bj bk bl \) :=

5\) i j k l\) . 

\(4.10\)

2

b b b b

The chiral traces in eqs. \(4.7\) to \(4.9\) evaluate as follows in terms of the Mandelstam variables and the parity-odd ϵ5 \(4.4\), 

2tr− \(\(p

p

p

p

p

p

p

p

b1 \+ b2 \)\( b2 \+ b3 \)\( b3 \+ b4 \)\( b5 \+ b1 \)\) = −s12 s23 − s23 s34 − s34 s45 − s15 s12 − ϵ5 , 2tr− \(p

p

p

p

bi\+1 bi\+2 bi\+3 bi \) = si\+1 i\+2 si\+3 i\+4 − si\+1 i\+3 si\+2 i\+4 \+ si\+1 i\+4 si\+2 i\+3 − ϵ5 , 2tr− \(p

p

p

p

bi\+1 bi\+2 bi\+4 bi\+3 \) = si\+1 i\+2 si\+3 i\+4 − si\+1 i\+4 si\+2 i\+3 \+ si\+1 i\+3 si\+2 i\+4 \+ ϵ5 . 

\(4.11\)

– 20 –

Relations between the momentum-twistor basis of the leading singularities B \(3.14\) and

\{Ci\}5

\(3.50\) in the frame x

i=1

0 → ∞ and the momentum-space basis \(4.6\) are as follows Atree → −

5

r0 , 

Bi → ri , 

Ci → r0 − ri − ri\+2 − ri\+3 − ri , 

i = 1, . . . , 5 . \(4.12\)

The Lagrangian insertion in the Wilson loop \(2.3\) and the negative geometries are invariant under the discrete group of dihedral transformations, which is generated by the cyclic shift transformation τ and the inversion ρ. For the five-cusp contour, they act on the momenta variables, which are the edges of the contour, and on the dual momenta, which are cusps of the contour, as follows, 

τ \(pi\) = pi\+1 , 

ρ\(pi\) = p6−i , 

τ \(xi\) = xi\+1 , 

ρ\(xi\) = x6−i , 

i = 1, . . . , 5 , 

\(4.13\)

where we recall cyclicity of the labels, p6 ≡ p1 and x6 ≡ x1. The rational prefactor r0 is dihedral invariant

τ \(r0\) = ρ\(r0\) = r0 , 

\(4.14\)

whereas \{ri\}5 and \{r

form the cyclic orbits, 

i=1

i\}5

i=1

τ \(r5\) = r1 , 

τ \(ri\) = ri\+1 , 

τ \(r5\) = r1 , 

τ \(ri\) = ri\+1 , 

i = 1, . . . , 4 , 

\(4.15\)

ρ\(ri\) = r6−i , 

ρ\(ri\) = r6−i , 

i = 1, . . . , 5 . 

\(4.16\)

As observed in \[16, 38, 39\], the six rational prefactors \{ri\}5 are conformal invariant i=0

in momentum space when normalized by the Parke-Taylor prefactor, 

1

PT =

\(4.17\)

Q5

⟨jj \+ 1⟩

j=1

where ⟨ij⟩ := λ

˜

i αλα are spinor brackets of the helicity spinors, and pµσ ˙

αα

λ ˙α. The

j

i

µ

= λα

i

i

nontrivial part of the conformal symmetry statement is that the rational prefactors are annihilated by the conformal boost generator, 

5

X

∂2

Kα ˙α =

, 

Kα ˙α \(PT ri\) = 0 , 

i = 0, . . . , 5 . 

\(4.18\)

∂λα∂ ˜

λ ˙α

j=1

j

j

Let us note that the remaining five \{ri\}5 are not conformal. 

i=1

4.3

The structure of the five-point integrated negative geometries

The Lagrangian operator is conformal and carries weight \(\+4\). Then, using the amplitude terminology, the Lagrangian insertion in the five-cusp Wilson loop F \(2.3\) carries the dual-conformal weight \(\+4\) with respect to the Lagrangian coordinate x0. This weight has to be canceled out when fixing the frame x0 → ∞, 

F \(L\)\(X\) ≡ lim \(x20\)4 F \(L\)\(x0; x1, . . . , x5\) . 

\(4.19\)

x0→∞

– 21 –

In the following, we tacitly assume that the frame x0 → ∞ is chosen and the loop corrections F \(L\) are functions of five Mandelstam variables X \(4.2\), as well as of the parity-odd ϵ5. In the five-cusp case, F is known up to the two-loop order \[17\]. The perturbative corrections F \(L\) are expanded in the basis of the rational prefactors \{ri\}5 , introduced in i=0

eqs. \(4.7\), \(4.8\), as follows, 

F \(0\) = r0 , 

\(4.20\)

5

X

\(1\)

F \(1\) =

\(ri − r0\)g

, 

\(4.21\)

i

i=1

5

\(2\)

X

\(2\)

F \(2\) = r0 g

\+

r

, 

\(4.22\)

0

i gi

i=1

where \(L\)

g

are pure polylogarithmic functions of the transcendental weight 2L. More pre-i

cisely, they are expressed in terms of the planar pentagon functions \[40, 41\], whose definitions are recalled in section 6.2. The one-loop functions \(1\) g

have simple expressions as the

i

classical dilogarithms, whereas the two-loop functions \(2\)

g

are known as iterated integrals

i

with dlog kernel. 

In the present work, we are interested in the analogous expressions for their negative geometry decomposition. According to section 3, the ladder geometries involve five leading singularities Ωab−\(AB

0

0\) only, see eq. \(3.40\). 

Carrying out the loop integration over

AB1, . . . , ABL, the L-loop ladder takes the form

Z

X

\(L\)

ΩL\(AB0, AB1, .., ABL\) =

Ωab−\(AB

\(AB

0

0\) hab

0\) , 

\(4.23\)

AB1,...,ABL

ab

where the summation is over

\(L\)

ab = 13, 24, 35, 14, 25, and where h

are pure functions. 

ab

According to eqs. \(3.18\) and \(3.33\), at L = 1, 2 they are given by the following integrals, Z

\(1\)

h

\(AB

C

ab

0\) =

ab\(AB1, AB0\) , 

\(4.24\)

AB1

Z

\(2\)

X

h

\(AB

C

ab

0\) =

cd\(AB2, AB1\) Ccd,ab\(AB1, AB0\) . 

\(4.25\)

cd AB1,AB2

The building blocks Cab and Cab,cd of the integrands are defined in eqs. \(3.8\) and \(3.32\). 

Similar to F \(L\) in eq. \(4.19\), we consider the ladders in the frame x0 → ∞. Their leading singularities are linear combinations of the rational prefactors \{ri\}5 , i=0

Ω25− = r

= r

= r

0

1 − r0 , 

Ω13−

0

2 − r0 , 

Ω24−

0

3 − r0 , 

Ω35− = r

= r

0

4 − r0 , 

Ω14−

0

5 − r0 , 

\(4.26\)

where we tacitly imply that the dual-conformal weight of Ωab− at point x

0

0 is canceled out

and x0 → ∞ as in eq. \(4.19\). These relations follow from eqs. \(3.17\), \(3.18\) and \(4.12\). 

We can label the five leading singularities of the ladders either by pair of indices ab as in

– 22 –

eq. \(4.23\), or by a single index i = 1, . . . , 5. Introducing an analogous labeling for the pure functions of the ladders, we define

\(L\)

\(L\)

\(L\)

\(L\)

\(L\)

\(L\)

\(L\)

\(L\)

\(L\)

\(L\)

h

≡ h

, 

h

≡ h

, 

h

≡ h

, 

h

≡ h

, 

h

≡ h

. 

\(4.27\)

25

1

13

2

24

3

35

4

14

5

Then the integrated one-loop and two-loop ladders have the following form, 5

X

\(1\)

F \(

\) =

\(ri − r0\) h

, 

\(4.28\)

i

i=1

5

X

\(2\)

F \(

\) =

\(ri − r0\) h

. 

\(4.29\)

i

i=1

Since the one-loop negative geometry decomposition involves only the ladder-type negative geometry, i.e. F \(1\) = F \( \) according to eq. \(2.19\), then the pure functions in eqs. \(4.21\)

and \(4.28\) coincide, 

\(1\)

\(1\)

g

= h

, 

i = 1, . . . , 5 . 

\(4.30\)

i

i

Performing the one-loop integrations of the integrand \(4.24\), we find \[16, 31\], 





\(1\)

π2

si i\+1

si i\+4

si i\+1

si i\+4

g

=

− log

log

− Li

1 −

− Li

1 −

. 

i

2

2

6

si\+2 i\+3

si\+2 i\+3

si\+2 i\+3

si\+2 i\+3

\(4.31\)

The integration of the two-loop ladder \(4.25\), to be discussed in the following seciton, constitutes one of the main goals of the present work. 

The factorizable two-loop negative geometry

is easy to evaluate. Indeed, its

integrand \(3.42\) requires only one-loop integrations, which are the same as for the one-loop ladder in eq. \(4.24\), 

X

\(1\)

\(1\)

F \(

\)\(AB0\) =

Ωab,cd−\(AB

\(AB

\(AB

0

0\)hab

0\)hcd

0\) . 

\(4.32\)

ab,cd

In the frame x0 → ∞, it results in the sum of products of the one-loop pure functions

\{ \(1\)

g

\}5

\(4.31\). As compared to the ladders and non-decomposed F \(L\), this negative i

i=1

geometry involves all eleven rational prefactors \(4.6\), 



2





5

5

5

5

X

\(1\)

X

\(1\)

X

\(1\)

\(1\)

X

\(1\)

\(1\)

F \(

\) = −r0

−



g

\+

r

g

\+ 2

g

\+ 2

r

g

, 

\(4.33\)

j



i 

i

j

 gi

i gi\+2 i\+3

j=1

i=1

j=1

i=1

where we tacitly assume cyclicity of the summation indices, i.e. 6 ≡ 1, and use relations

\(4.12\). 

Once the two-loop ladder

\(4.29\), the factorized negative geometry

\(4.33\), and

the nondecomposed F \(2\) \(4.22\) are known, the decomposition equation \(2.20\) immediately

– 23 –

provides an expression for the “loop” negative geometry . The latter involves all eleven rational prefactors \(4.6\), 

2













5

5

\(2\)

X

\(1\)

X

\(2\)

F

=r0

−

−

2g

g

2

h

0



j



j



j=1

j=1





5

5

5

X

\(2\)

\(2\)



\(1\)2

\(1\) X

\(1\)

X

\(1\)

\(1\)

\+

ri

−

2g

\+ 2h

g

\+ 2g

g

r

g

. 

i

i

i

i

j

 \+ 2

i gi\+2 i\+3

i=1

j=1

i=1

This completes the discussion of the general structure of the two-loop corrections. The only unknown terms are the functions \(2\)

h

. The next section is devoted to their computation. 

j

5

Two-loop nonplanar Feynman integrals for the negative geometries

We are going to perform loop integrations in the integrand of the two-loop ladder

, 

see eq. \(4.25\). In order to achieve this goal, we rely on a conventional Feynman integral calculation. Namely, we rewrite the momentum-twistor integrand as a linear combination of two-loop scalar Feynman integrals in the dimensional regularization, and then we calculate the contributing Feynman integrals. This is a universal approach of perturbative calculations in a QFT. However, a considerable drawback of this universal approach is that all nice properties of the negative geometry \(e.g. its finiteness\) are not manifest at the intermediate steps of the calculation. 

In \[17\], the Lagrangian insertion in the Wilson loop at two-loop order, F \(2\) \(2.4\), also has been calculated from the Feynman integrals in dimensional regularisation. In that case, the relevant family of Feynman integrals is the planar penta-box \[40, 42\]. The planar penta-box family is depicted in section 6.1. It turns out that the two-loop ladder integrand from section 3 involves a larger family of two-loop Feynman integrals. One can also easily understand it from the momentum twistor expression for the integrand \(3.33\), which is essentially nonplanar – its propagators cannot be drawn as planar graphs in the dual-momentum space. In this section, we identify a family of two-loop Feynman integrals which is required in our calculation of the two-loop ladder

, and we analytically calculate these

Feynman integrals using a differential equation approach \[43, 44\]. 

5.1

Two-loop five-point eleven-propagator family of Feynman integrals

We consider the following family of two-loop Feynman integrals in D = 4 − 2ϵ dimensions which have kinematics of the five-particle massless scattering, see section 4.1, 

Z

dDk

Z

1dD k2

1

dDx6dDx7

1

G⃗a\(X, ϵ\) :=

=

, 

\(5.1\)

\(iπD/2\)2 Q11 Dai

\(iπD/2\)2 Q11 Dai

i=1

i

i=1

i

where we recall that X denotes the set of five-particle Mandelstam variables, ⃗a := \{a1, . . . a11\}

is a vector of integer numbers, and the 11 propagators are defined as follows in terms of momenta and space-time coordinates \(dual momenta\), see eq. \(4.1\), 

– 24 –

*p*

*x*

*x*

*x*

1

5

1

5

*x*

*p* 2

*p*

1

5

*x*

*x*

2

4

*p* 1

1

*p* 5

10

1

5

11

9

*p* 3

*p* 4

2

*p*

*x*

*x* 6

*x*

2

7

8

7

4

*x*

*x*

3

6

*x*

*x*

6

8

7

4

3

3

6

4

*p*

*p*

4

4

7

5

2

3

*p* 3

*x* 2

*p* 1

*x*

*p*

*x*

2

3

*x* 3

4

*p* 5

*x*

*p*

5

*x* 1

2

\(a\)

\(b\)

Figure 1: Diagram \(a\) represents a penta-box diagram contained in integral family \(5.1\) in the dual-momentum variables. Diagram \(b\) represents the complete 11-propagator integral family \(5.1\) in the dual-momentum variables. 

Di in p-space

Di in x-space

Di in p-space

Di in x-space

1

k2

x2

6

\(k

1

57

2 − p4 − p5\)2

x236

2

\(k1 \+ p1\)2

x2

7

\(k

17

2 − p5\)2

x246

3

\(k1 \+ p1 \+ p2\)2

x2

8

\(k

27

1 − k2\)2

x267

4

\(k1 − p4 − p5\)2

x2

9

\(k

37

1 − p5\)2

x247

5

k2

x2

10

\(k

2

56

2 \+ p1\)2

x216

11

\(k2 \+ p1 \+ p2\)2

x226

The family \(5.1\) is closed under dihedral permutations \(4.13\), which act on the dual momenta x1, . . . , x5. Namely, a dihedral permutation σ of G⃗a generates a permutation σ\(⃗a\) of the list ⃗a, 

σ \(G⃗a\) = Gσ\(⃗a\) . 

\(5.2\)

The planar penta-box family \[40\], which involves 8 propagators, is contained in eq. \(5.1\). 

For example, if a9, a10, a11 ∈ Z≤0 then D9, D10, D11 could appear only in the numerator, and the corresponding graph is depicted in fig. 1a. The graph is planar both in momentum and dual-momentum space. The kinematics is that of five-particle massless scattering, i.e. 

the momentum space graph has five legs which carry light-like momenta p1, . . . , p5. Let us note that fig. 1a is not the only way to identify the planar penta-box among eq. \(5.1\). 

Acting with dihedral permutations on fig. 1a we find further penta-box subtopologies in the 11-propagator family \(5.1\). 

As compared to the 8-propagator penta-box, the 11-propagator family \(5.1\) is nonplanar in the dual-momentum space. In general, the Feynman integrals \(5.1\) cannot be drawn as planar graphs on the penta-box 8-propagator family. We find it convenient to avoid drawing nonplanar graphs by introducing a double covering of external coordinates x1, . . . , x5, see fig. 1b. For example, let us consider a six-propagator Feynman integral \(5.1\)

specified by

⃗a = \{0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1\} . 

\(5.3\)

– 25 –

*x*

*p*

5

1

*x*

*x*

1

2

*x*

*x*

*p*

1

5

2

*p* 5

*x* 4

1

*p* 5

*p* 1

5

11

10

1

*p*

9

3

*p*

2

*x*

4

7

8

*x* 6

*p*

*x*

*x* 6

8

*x* 7

2

7

4

*x*

6

3

*x*

4

3

3

6

4

*p* 4

*p* 4

7

5

2

3

*p* 3

*x* 2

*p* 1

*p*

*x*

*x*

3

*x*

4

3

*p* 5

*p* 2

*x*

*x*

2

5

1

\(a\)

\(b\)

Figure 2: The diagrams show a non-planar six-propagator Feynman integral drawn in the \(a\) penta-box 8-propagator family \(b\) 11-propagator family. The red lines denote the propagators in the dual-momentum space. Note the non-planarity means the crossing of x2 and x2 in diagram \(a\). However, the same Feynman integral drawn in diagram \(b\) 26

37

avoids this crossing by introducing double covering of external x1, . . . , x5. The diagram \(b\) allows us to translate back from dual-momentum coordinates and draw a momentum space box-triangle diagram BT2 in Fig.3

Non-planar Planar penta-box One-loop factorized Total MI

135

140

66

341

Table 1: Counting of the MIs in the family \(5.1\). 

We depict it in fig. 2a as a nonplanar graph, and as a planar graph using the double covering in fig. 2b. Let us stress that non-planarity refers to the dual-momentum space, but not the momentum space\! In general, the Feynman integrals \(5.1\) are not the usual amplitude Feynman integrals \(planar or nonplanar\) with five massless legs. Drawn in momentum space, they have up to 10 massless legs carrying momenta p1, . . . , p5, p1, . . . , p5, see fig. 1b. 

For example, the six-propagator Feynman integral \(5.3\) depicted in momentum space is BT2 in fig. 3, which is obtained from fig. 2b by pinching 5 propagators, and which carries external momenta p1, p2 \+ p3, −p3, p3 \+ p4, p5. 

There are Q\(X\)-linear dependences among Feynman integrals of the family \(5.1\) that follow from IBP relations \[45, 46\],. Using standard terminology, we refer to a basis of linearly independent Feynman integrals as master integrals \(MIs\). Further, we perform IBP reductions of the family \(5.1\) relying on the computer codes \[47–49\] to identify MIs in various sectors. As usual, we say that \{ai\}11 belongs to the sector \{θ\(a

, which is

i=1

i ≥ 1\)\}11

i=1

a list of 0’s and 1’s. We say that \{µi\}11 is a subsector of \{λ

iff µ

i=1

i\}11

i=1

i ≤ λi for i = 1, . . . , 11

and P µ

λ

of Feynman integrals comprises integrals from the

i

i < Pi

i. A family \{µi\}11

i=1

sector \{µi\}11 and all its subsectors. 

i=1

We find 341 master integrals \(MIs\) for the 11-propagator family \(5.1\). Among them, we identify those which are well-known in the literature. Indeed, 66 MIs factorize into products of one-loop pentagon integrals, i.e. they have a8 = 0. 140 MIs belong to the

– 26 –

\# propagators

5

6

7

8

9

≤ 9

\# sectors

5 15 20 10 10

60

\# sectors \(mod dihedral\) 1

2

3

1

2

9

Table 2: Number of non-planar sectors in the family \(5.1\) for a given number \(up to 9\) of propagators. 

sector

KT

BT1

BT2

PT

DB1

DB2

PBnp

DP1

DP2

\# propagators

5

6

6

7

7

7

8

9

9

\# MIs

10

16

29

42

26

55

82

147

155

\# MIs on cuts

4

1

6

1

2

3

3

1

1

Table 3: Number of MIs, and MIs on maximal cuts, for each non-planar sector. 

planar penta-box family \[40, 42\], i.e. they can be mapped by dihedral transformations \(5.2\)

onto the sector \{1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0\}, depicted in fig. 1a, and its subsectors. We refer to the remaining 135 MIs as non-planar, see table 1. 

Let us discuss the 135 non-planar MIs in detail. The Feynman integrals \(5.1\) with 10

and 11 propagators are IBP-reduced to Feynman integrals with nine or fewer propagators. 

Thus, the highest nonreducible sectors of the family \(5.1\) contain 9 propagators. The nonplanar MIs are categorized into 60 sectors, which are 9 independent sectors after modding out dihedral permutations \(5.2\). The counting of sectors for a given number of propagators is provided in table 2. We depict the nine independent non-planar sectors in fig. 3 and give them the following names: kite \(KT\), two box-triangles \(BT1, BT2\), penta-triangle \(PT\), two double-boxes \(DB1, DB2\), non-planar penta-box \(PBnp\), and two double-pentagons \(DP1, DP2\). In table 3, we summarize the counting of MIs in these nonplanar families. 

The number of MIs on the maximal cut is the number of MIs in the given family modulo its lower subsectors. The 9-propagator non-planar sectors DP1 and DP2, 

⃗aDP = \{0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1\} , 

1

⃗aDP = \{0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1\} , 

\(5.4\)

2

are the highest independent IBP-irreducible sectors. All nonplanar sectors are contained in DP1 and DP2 and their dihedral permutations \(5.2\). 

5.2

Constructing the pure basis

We calculate the Feynman integrals \(5.1\) relying on the method of differential equations \(DE\) \[43, 44\], in their canonical form \[43\]. Let T be a family of Feynman integrals, which is contained in \(5.1\), and let ⃗uT denote \(a particular choice\) for its set of MIs. By definition, the MIs are closed under taking derivatives in kinematic variables. We say that ⃗uT is pure if it satisfies the following system of DEs \[43\], 

∂ ⃗uT\(X, ϵ\) = ϵ AT,v\(X\)⃗uT\(X,ϵ\) , 

v ∈ X

\(5.5\)

∂v

– 27 –

*p*

*p*

1

5

*p*

*p*

2

1

*p*

*p*

5

*p*

*p* 5

1

*p*

5

3

2

2

5

*p*

*p*

4

2

4

*p* 2

9

7

10

*p*

*p*

3

3

4

8

11

*p* 3

*p* 3

8

8

4

*p* 4

3

6

11

*p*

*p*

3

4

7

*p* 4

*p*

*p* 2

*p* 2

5

*p*

*p*

5

2

*p*

*p*

*p*

1

4

*p* 5 1

*p* 1

\(a\) KT \(4 MIs\)

\(b\) BT1 \(1 MI\)

\(c\) BT2 \(6 MIs\)

*p*

*p*

5

5

*p* 1 *p* 2

*p* 4

*p*

5

*p* 5 *p*

1

*p*

1

4

*p*

*p* 2

5

3

*p* 3

2

7

6

*p*

7

2

3

*p* 3

2

*p*

8

*p* 4

3

*p* 4

9

11

8

4

8

4

*p* 3

*p*

11

3

11

10

*p*

9

5

10

9

*p* 1

*p* 2

*p* 4

*p* 4

*p* 2

*p*

*p* 5 *p*

2

*p* 1 *p* 5

1

\(d\) PT \(1 MI\)

\(e\) DB1 \(2 MIs\)

\(f\) DB2 \(3 MIs\)

*p*

*p*

*p*

*p*

2

5

*p*

5

2

*p*

*p* 4

5

*p* 1

1

*p*

2

1

*p*

5

2

3

5

5

2

3

*p*

*p*

7

2

*p*

3

3

7

6

4

*p* 4

*p* 3

*p*

4

8

3

*p* 3

8

8

4

11

11

4

*p* 3

11

9

9

10

*p*

10

9

*p*

10

4

4

*p*

*p*

*p*

2

*p*

*p*

4

2

*p*

*p*

5 *p*

1

*p* 5

1

5

1

*p* 2

\(g\) PBnp \(3 MIs\)

\(h\) DP1 \(1 MIs\)

\(i\) DP2 \(1 MI\)

Figure 3: The independent nonplanar sectors with up to 9 propagators, and the counting of corresponding MIs on the maximal cuts. 

where we take derivatives in the Mandelstam variables X of eq. \(4.2\). The entries of connection matrices AT,v are algebraic functions of the kinematics. 

The pure bases for the planar penta-box family and the product of one-loop pentagons, are known \[40, 42\]. Furthermore, some of the subsectors of the remaining integral families can be identified with Feynman integrals for which a pure basis is known in the literature. 

For example, consider the five-propagator kite integral \(KT\) shown in fig. 4a. This sector coincides with a four-point two-mass two-loop family of Feynman integrals calculated in \[50\], see fig. 4a, if we identify the kinematics P1 = −p3 , 

P2 = −p1 − p2 , 

P3 = p2 \+ p3 , 

P4 = p1 , 

\(5.6\)

so P 2 = P 2 = 0 and P 2, P 2 ̸= 0. This is a planar four-particle kinematics of the two-mass-1

4

2

3

easy type, and the pure MIs require the corresponding square root in their normalization, see eq. \(5.31\), 

q

q

q

\(4\)

\(S \+ T \)2 − 4P 2 P 2 =

s2 − 4 s

∆

, 

\(5.7\)

2

3

45

12s23 ≡

2

where S = \(P1 \+ P2\)2 and T = \(P1 \+ P3\)2. According to table 3, there are 4 MIs on the maximal cut of the sector KT which we choose as in \[50\]. 

– 28 –

*p*

*P*

1

4

*p* 2

*p*

*p* 5

3

2

5

*p* 4

4

8

*P* 2

*P* 3

11

*p* 3

*p* 4

*p*

*p* 2

5

*P* 1

*p* 1

\(a\)

\(b\)

Figure 4: Diagram \(a\) is a kite integral in the non-planar space with 5-point kinematics, which can viewed as a \(planar\) 4-point kite integral with 2 masses in diagram \(b\). The kinematic map between two diagrams is given in \(5.6\). 

*Z*

*p*

*Z*

4 *Z* 5

5 *p*

*p*

1

1 *Z* 2

4

*p* 2

*p* 3

7

2

*p* 3

*Z*

11

*ZC ZD*

2 *Z* 3

8

*ZA ZB*

4

*Z* 3 *Z* 4

10

9

*p* 2

*p* 4

*Z* 1 *Z* 2

*p p*

*Z*

1

5

4 *Z* 5

Figure 5: The double-box sector DB1 with 7 propagators in momentum twistor notation. 

For the remaining non-planar sectors, we use the idea that loop integrands without double poles, and with constant leading singularities are expect to give pure Feynman integrals \[31, 43\]. These integrands are called dlog integrands, as their integrand can be written as \(sums of\) products of d log x = dx/x terms. One option is to classify all such integrands, for a given propagator structure and kinematics, cf. for example \[51\]. However, here we only need to provide a suitable basis for the differential equations. We therefore proceed in a simpler way and use a four-dimensional loop-by-loop approach. This analysis of the integrands enables us to find candidates to form a pure basis of MIs on the maximal cut. 

We found the program DLOGBASIS \[51\] useful to verify the expected integrand properties. 

Once a candidate basis is found, we calculate its derivatives, and explicitly verify that they satisfy the canonical \(ϵ-factorized\) DE of eq. \(5.18\). 

We find it convenient to employ the momentum twistor parametrization of the integrands. We assign the twistor lines AB ∼ x7 and CD ∼ x6 to the loop integrations in

\(5.1\), and intersecting twistors lines ZiZi\+1 ∼ xi with cyclic i = 1, . . . , 5 to the external dual momenta. We also introduce the infinity bi-twistor I since we have to deal with non-dual-conformal Feynman integrals. 

– 29 –

For example, the MIs of the double-box sector DB1 have the following form, see fig. 5, 

\(i\)

Z

N

\(i\)

I

:=

DB1

. 

DB1

⟨AB12⟩⟨AB34⟩⟨AB45⟩⟨ABCD⟩⟨CD12⟩⟨CD23⟩⟨CD45⟩⟨ABI⟩⟨CDI⟩

AB,CD

\(5.8\)

According to table 3, there are 2 MIs on the maximal cut. In order to find these MIs in pure form, we proceed loop-by-loop working out the dlog form of the integrands. We take into account that the following CD-subintegral of \(5.8\) is a dlog four-form Ω\(4\) accompanied by the three-mass box leading singularity factor, see \(2.41\) in \[31\], 

1

d4ZCd4ZD

1

=

Ω\(4\)\(CD\) . 

\(5.9\)

⟨ABCD⟩⟨CD12⟩⟨CD23⟩⟨CD45⟩ vol\(GL\(2\)\)

⟨AB\(123\) ∩ \(245\)⟩

Choosing the following numerator

\(1\)

N

= ⟨1234⟩⟨1245⟩⟨2345⟩⟨ABI⟩⟨CDI⟩

\(5.10\)

DB1

and substituting the dlog form \(5.9\) in eq. \(5.8\), we end up with the one-mass box AB-subintegral with the unit leading singularity. Translating eq. \(5.8\) with numerator \(5.9\) in momentum notations, we obtain

\(1\)

I

= s

DB

23s34s45 G0,1,0,1,0,0,1,1,1,1,1 . 

\(5.11\)

1

A second MI on the maximal cut of DB1 can be obtained e.g. by canceling the three-mass leading singularity in \(5.9\). Namely, choosing the numerator \(2\)

N

= ⟨AB\(123\) ∩ \(245\)⟩⟨I\(124\) ∩ \(345\)⟩⟨CDI⟩

\(5.12\)

DB1

and substituting the dlog form \(5.9\) in eq. \(5.8\), we end up with the three-mass box AB-subintegral with the unit leading singularity. Rewriting the numerator \(5.12\) in momentum notations with the help of the Schouten identity, we obtain

\(2\)

I

= \(s

DB

23 − s15\) \(s34 G0,0,0,1,0,0,1,1,1,1,1 − s15 G0,1,−1,1,0,0,1,1,1,1,1\) . 

\(5.13\)

1

Similarly, we perform a dlog analysis of the remaining nonplanar sectors. Let us explain here how it works for the sectors with highest number of propagators. There are two such sectors, each containing one MI, see fig. 3. In fig. 6 we present DP1 in momentum twistor notations, 

Z

NDP

I

1

DP

:=

. 

1

⟨AB12⟩⟨AB23⟩⟨AB34⟩⟨AB45⟩⟨ABCD⟩⟨CD12⟩⟨CD23⟩⟨CD45⟩⟨CD51⟩

AB,CD

\(5.14\)

The one-loop pentagon CD-subintegral is put in dlog from upon choosing the magic numerator \[31\], 

⟨CD24⟩ ≡ ⟨CD\(123\) ∩ \(345\)⟩ . 

\(5.15\)

– 30 –

*Z*

*p*

*Z* 5 *Z* 1

1 *Z* 2

*p*

5

*p*

2

*Z*

1

*Z*

4 *Z* 5

2 *Z* 3

5

2

3

*p*

7

4

*p* 3

*p*

*Z*

*Z*

3

*C ZD*

8

*A ZB*

11

4

*Z* 3 *Z* 4

10

9

*Z* 3 *Z* 4

*p*

*p*

4

2

*p* 1 *p* 5

*Z* 1 *Z* 2

*Z* 4 *Z* 5

Figure 6: The double-pentagon, DP1, in the momentum twistor variables. 

The leading singularity 1/⟨AB25⟩ of the CD-subintegral complements the AB-subintegral to the pentagon one-loop integral, which takes the dlog form provided it has the magic numerator ⟨AB24⟩. Summarizing, the integral DP1 \(5.14\) with complex numerator NDP = ⟨AB24⟩⟨CD24⟩⟨1235⟩⟨1245⟩

\(5.16\)

1

is in dlog form with unit leading singularities. Calculating derivatives of IDP , we verify 1

that the DE is ϵ-factorized on the maximal cut. 

Similarly, the magic numerator of the pentagon one-loop sub-integral and the loop-by-loop calculation of the dlog form, enable us to identify the pure MI in the DP2 sector Z

⟨AB24⟩⟨CD24⟩⟨1235⟩⟨1245⟩

IDP :=

. 

2

⟨AB12⟩⟨AB23⟩⟨AB34⟩⟨AB45⟩⟨ABCD⟩⟨CD12⟩⟨CD23⟩⟨CD34⟩⟨CD51⟩

AB,CD

\(5.17\)

Ideally, the above analysis leads directly to differential equations in canonical form. 

However, it is sometimes convenient to find a pure basis for a sector T , we identify a pure basis on the maximal cut first. The derivatives of MIs on the maximal cut are coupled which corresponds to the diagonal block of the connection matrix. For a pure basis on the maximal cut, the diagonal block is in ϵ-factorized form. We then proceed to the off-diagonal part. 

We supplement the MIs from the maximal cut with MIs belonging to all lower subsectors of T and denote all of them ⃗IT . We choose the MIs from the lower subsectors to be pure by induction. Usually, one can easily choose a pure basis on the maximal cut such that the DE takes the pre-canonical form, 

∂ ⃗IT\(X, ϵ\) = \(BT,v\(X\) \+ ϵAT,v\(X\)\) ⃗IT\(X, ϵ\)

\(5.18\)

∂v

where v ∈ X \(4.2\). The nonzero entries of the off-diagonal block matrix BT,v correspond to an admixture of the lower subsector MIs to the maximal cut MIs. A redefinition of the maximal cut MIs eliminates BT,v and puts the DE into the ϵ-factorized form \(5.5\). We collect the full basis of MIs in an accompanying ancillary file. 

5.3

Canonical differential equations

In the previous section, we have constructed a pure basis of MIs, which satisfy DE \(5.5\). As we explained at the end of section 5.1, any nonplanar Feynman integral of the family \(5.1\)

– 31 –

can be expanded in the MIs of two independent 9-propagator families DP1 and DP2 \(5.4\)

and their dihedral permutations \(5.2\). The pure bases for the planar subtopologies and the one-loop products are known. They are not required in our calculation of the ladder negative geometry. Thus, it will be enough to consider the pure bases ⃗uT for families T = DP1, DP2. 

We combine DEs \(5.5\) into the canonical DE \[43\], 

d⃗

uT \(X, ϵ\) = ϵ dAT \(X\) ⃗uT \(X, ϵ\)

\(5.19\)

with the total differential d in all kinematic variables X, 

X

∂

d =

dv

. 

\(5.20\)

∂v

v∈X

The connection matrix dAT \(X\) is a Q-linear combinations of the dlog forms which we refer to as the alphabet letters, 

111

X

X

dAT \(X\) :=

AT,v dv =

d log \(wi\(X\)\) Ai,T , 

\(5.21\)

v∈X

i=1

Ai,T are matrices of rational numbers. In what follows, we find that the family \(5.1\) requires 111 alphabet letters \{wi\(X\)\}111 , which are algebraic functions of the kinematics X \(4.2\). 

i=1

We present them in section 5.4 and appendix A. We also provide canonical DE \(5.19\) for nonplanar families T = DP1, DP2 in ancillary files. 

In order to solve the canonical DE \(5.19\), we series expand the pure MIs in ϵ and normalize them such that their expansion starts at finite order, 

X

\(k\)

⃗

uT \(X, ϵ\) =

ϵk ⃗

u

\(X\) . 

\(5.22\)

T

k≥0

Using values of the pure basis MIs at X = X0 as initial values, we solve the DE analytically in terms of Chen iterated integrals \[52\], 

k

\(k\)

X

X



\(k−m\)



⃗

u

\(X\) =

A

\(X

\[w , . . . , w

\]

\(X\) , 

\(5.23\)

T

im,T . . . Ai1,T ⃗

uT

0\)

i1

im X0

m=0 i1,...,im

where summations i1, . . . , im run over the alphabet letters. The iterated integrals with the reference point X0 are defined starting with \[\]X = 1, 

0

Z

1

∂ log \[wi \(γ\(y\)\)\]

\[w

m

i , . . . , w

\]

\(X\) =

dy

\[w , . . . , w

\]

\(γ\(y\)\) , 

\(5.24\)

1

im X

i

i

0

1

m−1 X0

0

∂y

and the integration path γ in kinematic space connects γ\(0\) = X0 and γ\(1\) = X. Using analytic representation \(5.23\), we can immediately calculate derivatives of the pure MIs and verify that they satisfy \(5.19\), since

d \[wi , . . . , w \]

\(X\) = \[w , . . . , w

\]

\(X\) d log \(w

\(X\)\) . 

\(5.25\)

1

im X

i

i

i

0

1

m−1 X0

m

– 32 –

We choose a reference point X0 in the Euclidean region as follows, X0 = \(s12 = −1, s23 = −1, s34 = −1, s45 = −1, s15 = −1\) , 

\(5.26\)

√

and we choose the positive branch of the square root ϵ5\(X0\) = 5 \(4.5\). Note that X0

is invariant under dihedral transformations \(4.13\). The analytic solution \(5.23\) of the canonical DE involves initial values n \(k\)

o

⃗

u

\(X

. In order to calculate the negative

T

0\)

k≥0

geometries, the ϵ-expansion of the pure MIs is required up to order k = 4. Then the initial values are required up to the same order. In principle, these initial values, up to a trivial overall normalization, can be obtained by requiring absence of spurious singularities, see e.g. 

section 7 of \[51\]. Here, we evaluate them numerically with 70-digit precision using AMFlow

\[53\]. The initial values \(0\)

⃗

u

\(X

T

0\) are rational numbers. We assign the transcendental weight

\(k\)

k to the initial values ⃗u

\(X

T

0\) to make eq. \(5.23\) of uniform transcendental weight. 

Omitting the initial values of weight k ≥ 1 in eq. \(5.23\) is equivalent to not specifying the reference point of the iterated integrals that results in the symbol expression \[54\] for the pure MIs, 





X





S

\(k\)

\(0\)

⃗

u

\(X\) =

A

\(X

\[w , . . . , w \] \(X\) . 

\(5.27\)

T

ik,T . . . Ai1,T ⃗

uT

0\)

i1

ik

i1,...,ik

5.4

Nonplanar extension of the pentagon alphabet

The analytic structure of the planar penta-box family in fig. 1a is described by the 26-letter planar pentagon alphabet \[42\], 

2-loop

A

:= \{W

∪ \{W

pl

i\}20

i=1

i\}31

i=26 , 

\(5.28\)

we follow the standard convention of \[55\] labeling the planar letters Wi. It is contained in the family \(5.1\) for example as an 8-propagator sector \{1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0\} along with its subsectors. 

The nonplanar sector of the 11-propagator family \(5.1\) has a more intricate analytic structure. Constructing the pure basis of MIs and canonical differential equations \(5.19\), we find that the nonplanar sector requires the 26 planar pentagon letters \(5.28\) to be supplemented with new 85 letters. In total, a 111-letter alphabet is required to solve analytically \(5.23\) the 11-propagator family \(5.1\). We denote them uniformly \{wi\}111 and i=1

separate them into planar Wi and nonplanar f

Wi, 

\{wi\}111

∪ \{

∪ \{

i=1 = \{Wi\}20

i=1

Wi\}31

i=26

f

Wi\}85

i=1 . 

\(5.29\)

The alphabet is closed upon dihedral permutations of the kinematics, namely dlog forms of the alphabet letters linearly transform among themselves, 

σ\(d log\(wi\)\) ∈ ⟨d log\(w1\), . . . , d log\(w111\)⟩

\(5.30\)

Q

where σ = τ, ρ is a dihedral transformation \(4.13\). Thus, the alphabet letters are naturally organized into orbits of the cyclic shift τ. 

– 33 –

roots

\(i\)

\(i\)

\(i\)

\(i\)

\(i\)

\(i\+1\)

∆

∆

∆

, ∆

, ∆

, ∆

2

4

5

∆2

5

∆4

5

∆2

2

\# letters 20 = 4 × 5 15 = 3 × 5 10 = 2 × 5 10 = 2 × 5 5 = 1 × 5

5 = 1 × 5

Table 4: Couning of the non-planar algebraic letters \{

, which contain one or two

f

Wi\}85

i=21

square roots. 

The planar alphabet \(5.28\) is also closed under dihedral permutations. Among 26

planar letters, 20 letters \{Wi\}20 are linear in Mandelstam variables \(4.2\), 5 letters \{W

i=1

i\}30

i=26

√

√

are algebraic with the square root ∆5 \(4.5\), and W31 = ∆5. We recall their definitions in appendix A.1. We recall that ∆5 is dihedral invariant. 

√

Along with ∆5, the nonplanar sector requires 10 additional square roots. They are square roots of quadratic and quartic polynomials in the Mandelstam variables, \(1\)

∆

=s2 − 4s

2

12

34s45 , 

\(5.31\)

\(1\)

∆

=s2

− 2s

− 2s2

4

15s2

12 \+ s2

23s2

12

15s23s2

12

23s34s12 \+ 2s15s23s34s12

\+ 2s15s34s45s12 \+ 2s23s34s45s12 \+ s2

−

23s2

34 \+ s2

34s2

45

2s23s234s45 , 

\(5.32\)

each appearing in 5 cyclic permutations, \(i\)



\(1\)

\(i\)



\(1\)

∆

= τ i−1

∆

and ∆ = τi−1 ∆

for

2

2

4

4

i = 1, · · · , 5. We identify them as among the normalization prefactors of the pure integrals. 

q

q

For example, 

\(4\)

\(1\)

KT sector requires

∆

and BT

∆

, see fig. 3. 

2

2 sectors requires

4

Among 85 nonplanar letters f

Wi \(5.29\), there are 20 letters, which are polynomial in the Mandelsatm variables. We organize them in cyclic orbits as follows, 



\(1\)





f

Wi := τ i−1 ∆

, 

, 

2

f

W5\+i := τ i−1

f

W6





\(1\)

f

W10\+i := τ i−1

f

W11

, 

f

W15\+i := τ i−1 ∆

, 

i = 1, . . . , 5

\(5.33\)

4

and f

W6 and f

W11 are cubic in the Mandelstam variables, 

f

W6 := s12s2 −

15

s12s15s23 − s12s23s34 \+ s23s234 \+ s15s34s45 , 

\(5.34\)

f

W11 := s212s15 \+ s12s15s23 \+ s12s23s34 \+ s223s34 \+ s215s45 − 2s15s34s45 \+ s234s45 . 

\(5.35\)

The remaining 65 non-planar letters \{

are algebraic. They involve one or two

f

Wi\}85

i=21

square roots and have the following form

√

√

√

P1 − P2

R

P −

R

R

√

1

2

, 

√

√

, 

\(5.36\)

P1 \+ P2

R

P \+

R1 R2

with P1, P2, P being homogeneous polynomials in Mandelstam variables, and R, R1, R2 =

\(i\)

\(i\)

∆5, ∆ , ∆ . We count them in table 4, and provide their explicit form in appendix A.2. 

2

4

The alphabet letters appear in the canonical DE \(5.19\) as linear combinations of derivatives \{d log\(wi\)\}111 . We employed several complementary approaches to identify explicit i=1

– 34 –

expressions for the letters presented in this section. Some nonplanar letters f Wi appear in

the alphabets of subtopologies known in literature. The normalization of the pure MIs suggests some of the letters f

Wi. We also rely on computer codes \[56–58\], which implement the Landau analysis of the branch cut singularities. Let us note that using these codes we were able to identify all but the five quartic letters f

W16, . . . , f

W20. 

6

Results for integrated negative geometries and positivity properties

In the previous section, we calculated a family of nonplanar two-loop five-particle Feynman integrals \(5.1\). Using these analytic expressions for the Feynman integrals, we perform loop integrations of the two-loop five-cusp ladder negative geometry integrand constructed in section 3. As compared to Feynman integrals of section 5, we find that the two-loop ladder has a simpler analytic structure. We show that the two-loop ladder belongs to a class of the planar pentagon functions \[40, 41\], and we also recall definitions and properties of these transcendental functions. Using the two-loop negative geometry decomposition \(2.20\), we also obtain a planar pentagon function expression for the “loop” negative geometry . We discuss analytic properties and numerical evaluation of the integrated two-loop negative geometries. 

6.1

Integrating the two-loop ladder

We would like to express the two-loop ladder

in terms of the Feynman integrals \(5.1\). 

Thus, we have to rewrite the momentum twistor expression for the ladder integrand \(4.25\)

in space-time coordinates \(dual momenta\). Let us introduce short-hand notations δ\(0\) = 0 , 

δ\(1\) = 6 , 

δ\(2\) = 7 . 

\(6.1\)

The loop variables x6 and x7 from \(5.1\) and the Lagrangian coordinate x0 are the moduli parameters of the momentum twistor lines, ABj ∼ xδ\(j\), j = 0, 1, 2. We integrate over the loop variables as follows, 

d4ZA d4Z

j

Bj = ⟨ABj⟩4 d4x

vol\(GL\(2\)\)

δ\(j\) , 

j = 1, 2 . 

\(6.2\)

We rewrite the twistor four-brackets as follows, 

⟨ABjABk⟩ = ⟨ABj⟩⟨ABk⟩ x2

, 

\(6.3\)

δ\(j\) δ\(k\)

⟨ABj i i \+ 1⟩ = ⟨ABj⟩⟨i i \+ 1⟩ x2

, 

\(6.4\)

δ\(j\) i

⟨AB

⟨

j ⟩⟨i \+ 2 i⟩

AB



j i i \+ 2⟩ =

tr− pi x

x

pi\+2 , 

\(6.5\)

s

b bi δ\(j\) bδ\(j\) i\+2 b

i i\+2

where j, k = 0, 1, 2; an index i takes cyclic values from \{1, 2, . . . , 5\}; the duality relations between momenta and coordinates are given in \(4.1\); the chiral trace is defined in \(4.10\); 

and we recall definitions of the spinor-helicity brackets ⟨mn⟩ = λαmλnα. 

– 35 –

The chiral trace in \(6.5\) contains the parity-even and parity-odd parts, 2 tr



− p x

x

p

= − s

s

\(s

bi bi δ\(j\) bδ\(j\) i\+2 bi\+2

i i\+1si\+1 i\+2 \+ x2

δ\(j\) i−1 i\+1 i\+2 \+ x2

δ\(j\) i

i i\+1 − si\+3 i\+4\)

\+ x2

\(s

s

δ\(j\) i\+1

i\+1 i\+2 − si\+3 i\+4\) \+ x2

δ\(j\) i\+2 i i\+1

16

−

Gr \{pi, x

ϵ

δ\(j\) i, xδ\(j\) i\+2, pi\+2\} ; \{p1, p2, p3, p4\} . 

\(6.6\)

5

The parity-even part is given by squared distances among the cusp coordinates x1, . . . , x5

and xδ\(j\). The parity-odd part is proportional to ϵ5, see \(4.4\). We express it in terms of the Gram determinant Gr, which is a quartic polynomial in the squared distances. 

Substituting eqs. \(6.2\) to \(6.5\) in the two-loop ladder integrand \(4.25\), we verify that spinor helicities cancel out. The resulting expression is written in terms of ϵ5 and the squared distances among x0, x1, . . . , x5, x6, x7. In order to simplify the loop integrations, we choose x0 → ∞ by doing a dual-conformal transformation, see eq. \(4.19\). Then, we find that the two-loop ladder \(4.25\) in the frame x0 → ∞ is expanded over the Feynman integrals \(5.1\), 

\(2\)

X

h

\(X\) = lim

\(A

13

⃗

a\(X \) \+ ϵ5 B⃗

a\(X \)\) G⃗

a\(X \)

\(6.7\)

ϵ→0

⃗

a

where A and B are rational functions in the Mandelstam variables X \(4.2\). The sum contains 283 Feynman integrals G⃗a. We also introduced the dimensional regularization D = 4 − 2ϵ in order to render the loop integrations in each term of \(6.7\) well-defined. 

We observe that the Feynman integrals appearing in the sum \(6.7\) contain at most nine propagators. We find that each G⃗a contributing in \(6.7\) belongs to one of the four 9-propagator families, which we denote T1, . . . , T4, 

⃗aT = \{1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1\} , 

⃗a

= \{1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1\} , 

\(6.8\)

1

T2

⃗aT = \{0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1\} , 

⃗a

= \{1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1\} . 

\(6.9\)

3

T4

These four families are dihedral permutations σ \(see eq. \(5.2\)\) of the families DP1 and DP2

\(5.4\), 

⃗aT = σ

\) , 

⃗a

= σ

\) , 

1

\{1,5,4,3,2\} \(⃗

aDP1

T2

\{2,3,4,5,1\} \(⃗

aDP1

⃗aT = σ

\) , 

⃗a

= σ

\) . 

\(6.10\)

3

\{1,2,3,4,5\} \(⃗

aDP2

T4

\{5,1,2,3,4\} \(⃗

aDP2

Thus, we need to calculate Feynman integrals G⃗a from the families DP1 and DP2 and to apply the dihedral transformations \(6.10\) to map them into the families T1, . . . , T4. We use FiniteFlow \[59\] to construct the IBP reduction rules for the Feynman integrals G⃗a from the families DP1 and DP2, and we expand them in the bases of pure MIs ⃗uDP and ⃗u

. 

1

DP2

The dihedral mappings \(6.10\) act on the UT Feynman integrals as follows, see eq. \(5.2\), 

⃗

uT = \(τ ρ\) \(⃗u

\) , 

⃗

u

= τ \(⃗

u

\) , 

⃗

u

= ⃗

u

, 

⃗

u

= τ −1 \(⃗

u

\) . 

\(6.11\)

1

DP1

T2

DP1

T3

DP2

T4

DP2

We calculated pure MIs bases of the families DP1 and DP2 solving the canonical DE \(5.19\), 

and we represented them as iterated integrals \(5.23\). We choose the base point of the

– 36 –

iterated integrals to be X0 \(5.26\), which is invariant under dihedral transformations of the kinematics. Thus, a dihedral transformation σ acts only on the alphabet letters, but it does not change the initial values in the iterated integral solution \(5.23\), 

k

X

X

\(k−m\)

σ \(⃗

uT \) \(X\) =

ϵk

Ai

\(X

\) , . . . , σ \(w

\)\]

\(X\)

\(6.12\)

m,T . . . Ai1,T ⃗

uT

0\) \[σ \(wi1

im

X0

k≥0

m=0

where T = DP1, DP2. Let us recall that the alphabet is closed under dihedral transformations, see eq. \(5.30\). Eq. \(6.12\) immediately provides the iterated integral expressions for all pure MIs \(6.11\), which are required in our calculation of the two-loop ladder. 

Let us note that the set \(6.11\) of 2 × 147 \+ 2 × 155 pure Feynman integrals \(see the counting of MIs in table 3\) is not linearly independent since there are overlaps among the sectors T1, . . . , T4. In order to resolve the linear relations among them, we find identical MIs G⃗a belonging to the sectors T1, . . . , T4, and then we IBP-reduce them to the pure MIs \(6.11\). 

In this way we find 345 Q-linear relations among pure Feynman integrals \{⃗uT , . . . , ⃗u \}. 

1

T4

Substituting the IBP reduction rules and their dihedral transformations \(6.10\) in eq. \(6.7\), 

we rewrite it as follows, 

\(2\)

X





h

\(X\) = lim

⃗

A

⃗

B

· ⃗

u

13

T \(X, ϵ\) \+ ϵ5

T \(X, ϵ\)

T \(X \)

\(6.13\)

ϵ→0 T∈\{T1,...,T4\}

where coefficients A and B are rational functions in Mandelstam variables X, dimensional regularization ϵ, and also the square-roots \(5.31\), \(5.32\). The square roots in the IBP

reduction rules come from the normalization of the pure MIs. For our choice of the pure MIs, they are finite ϵ = 0, see eq. \(5.22\), but the coefficients A and B do contain ϵ-poles at ϵ = 0. 

After substituting the iterated integral expressions for the pure MIs \(6.12\) in eq. \(6.13\), 

we find that

• ϵ-poles cancel out; 

• the finite part is of uniform transcendental weight four; 

• it has unit leading singularity; 

• only planar pentagon alphabet letters \(5.28\) contribute to the iterated integrals. 

In other words, eq. \(6.13\) takes the form, 

4

\(2\)

X

X

\(4−m\)

h

\(X\) =

c

\[W , . . . , W

\]

\(X\)

\(6.14\)

13

j

j

j

1,...,jm

1

m X0

m=0 j1,...,jm

where c\(k\) are transcendental weight-k constants. Namely, c\(k\) are Q-linear combination of weight-

\(k\)

o

k initial values of the pure MIs n⃗u

\(X

. Obviously, eq. \(6.14\) could not

DP

0\)

i

i=1,2

hold for arbitrary initial values. Consequently, eq. \(6.14\) is equivalent to Q-linear relations among the initial values of weight k = 0, 1, 2, 3. We obtain these linear relations. We verify

– 37 –

weight w

0

1

2

3

4

number l\(w\) of fw,a

1

5

5

3 ∗ 5 \+ 1

11 ∗ 5 \+ 1

Table 5: Counting of the planar pentagon functions \{fw,a\} of the transcendental weight w split into cyclic orbits each containing 1 or 5 functions. 

that the initial values of the pure MIs, which we evaluated numerically in section 5.3, do satisfy the exact linear relations with the expected numerical accuracy. 

The exact Q-linear relations among the boundary constants also reduce the number of Q-linear independent c’s in eq. \(6.14\), 

\(0\)

\(1\)

\(2\)

\(3\)

c

∈

= 0 , 

c

∈ ⟨π2⟩ , 

c

∈ ⟨ζ

, 

c\(4\) = c

j

Q , 

c

3, c3⟩

4

\(6.15\)

1,...,j4

j1,j2,j3

j1,j2

Q

j1

Q

where c3 and c4 are transcendental constants of weights 3,4, respectively. 

We have chosen one of the pure functions, i.e. \(2\)

\(2\)

h

≡ h

, in the decomposition of the

13

2

two-loop ladder \(4.29\). The remaining pure functions are obtained by cyclic shifts τ, which act only on the alphabet letters due to the dihedral invariance of the base point X0 \(5.26\), 

4

\(2\)

\(2\)

X

X

\(4−m\)

h

\(X\) = τ i−1h

\(X\) =

c

τ i−1 \(W \) , . . . , τ i−1 \(W \)

\(X\). 

i i\+2

13

j

j

j

1,...,jm

1

m

X0

m=0 j1,...,jm

\(6.16\)

In what follows, we rewrite the iterated integrals from the previous equation as the planar pentagon functions \[40, 41\]. 

6.2

Planar pentagon function expressions for the integrated negative geome-

tries

To express all negative geometries up to the two-loop order, we will use the planar pentagon functions, first introduced in \[40, 41\] as a basis of the transcendental functions expressing all massless planar two-loop Feynman pentabox family, see fig. 1a. 

The integrand of the two-loop correction F \(2\) involves only planar Feynman integrals belonging to the pentabox family, so F \(2\) is expressible in the planar pentagon functions of \[40, 41\], as was shown in \[17\]. However, the integrands of the two-loop ladder and the “loop” topology

from the negative geometry decomposition of F \(2\) require a

larger set of Feynman integrals, which we calculated in section 5.3 as iterated integrals over the 111-letter nonplanar alphabet \(5.29\). Thus, one may think that the planar pentagon functions are not sufficient to express these negative geometries. Despite the presence of the nonplanar letters in the expression of the individual Feynman integrals, they cancel out in the iterated integral expression for the two-loop ladder \(6.16\) such that only 25 letters of the planar pentagon alphabet contribute. Then, these iterated integrals can be reduced to the planar pentagon functions of \[40, 41\]. 

– 38 –

weight w

1

2

3

4

F \(1\) ∼

5

5

0

0

F \(2\)

5

5

16

56

5

5

16

41

5

5

0

0

5

5

16

56

Table 6: Counting of the weight-w pentagon functions contributing to the one-loop and two-loop negative geometries. 

The planar pentagon functions are defined as weight-w iterated integrals \(5.24\) over the planar pentagon alphabet with respect to the Euclidean reference point X0 \(5.26\) for w = 0, 1, . . . , 4. We denote them as \{fw,a\}w=0,...,4 where the label a discerns l\(w\) pentagon functions of weight w. This counting is summarized in table 5. Their definitions respect the discrete dihedral symmetry. Namely, they are split into cyclic orbits of length one or five. The label a specifies the orbit and position on the orbit. If the n-th orbit is of length one, then we put a = n and the pentagon function is invariant under the cyclic shift τ \(fw,n\) = fw,n, see eq. \(4.13\). If the n-th orbit is of length five, then the corresponding five pentagon functions carry labels a = \(n, 1\), . . . , \(n, 5\), and they are obtained from each other by the cyclic shifts, 

f



w,\(n,p\) = τ p−1

fw,\(n,1\) , 

p = 1, . . . , 5 . 

\(6.17\)

Obviously, at weight zero, there is only one pentagon function which is just a rational constant, which we choose f0 = 1. Then, according to table 5, there is one length-five orbit at weights one and two, which are denoted as \{f1,\(1,p\)\}5

and \{f

, respectively. 

p=1

2,\(1,p\)\}5

p=1

At weights three and four, there are three and eleven length-five orbits, i.e. \{f3,\(n,p\)\}n=1,...,3

p=1,...,5

and \{f4,\(n,p\)\}n=1,...,11. Also, at weights three and four, there are length-one orbits, \{f p=1,...,5

3,4\}

and \{f4,12\}. 

In section 6.1, we calculated the two-loop ladder

by solving the contributing

nonplanar Feynman integrals and expressed it as weight-four UT linear combinations of iterated integrals, see eq. \(6.16\). The latter involves only 25 planar pentagon letters. Now we are going to expand it in the basis of algebraically independent planar pentagon functions

\[40, 41\]. 

Let us start with F \(1\), which is the one-loop ladder

, see \(4.28\). The polylogarithmic

expressions for its pure functions \{ \(1\)

g

\}5 , see \(4.31\), are the following UT polynomials of

i

i=1

weight two in the pentagon functions, 

\(1\)

1

π2

g

= f

2f



f

\+

i

2,\(1,i\) − f2,\(1,i\+2\) \+ 2

1,\(1,i\) − f1,\(1,i\+2\) − f1,\(1,i\+4\)

1,\(1,i\+2\) − f1,\(1,i\+4\)

6

\(6.18\)

– 39 –

where we imply that index i takes cyclic values, i.e. i \+ 5 ≡ i. Substituting this expression in eq. \(4.33\), we rewrite the factorizable two-loop negative geometry as a weight-four

UT polynomial in the pentagon functions. In table 6, we summarize how many pentagon functions of various weights appear in the expression of the integrated negative geometries. 

Both

and

involve pentagon functions only of weights one and two. 

The pure functions of the two-loop ladder

\(4.29\) and the non-decomposed two-loop

F \(2\) \(4.22\) are more complicated. They are weight-four UT polynomials in the pentagon functions of the following form

\(2\)

\(2\)

X

X

X

h

, g

:

α

α

f

f

\+

β

f

f

i

i

af4,a \+

a1,a2 1,a1 3,a2

a1,a2 2,a1 2,a2

a

a1,a2

a1,a2

X

X

\+

αa

f

f

f

\+

α

f

f

f

f

1,a2,a3

1,a1 1,a2 2,a3

a1,a2,a3,a4 1,a1 1,a2 1,a3 1,a4

a1,a2,a3

a1,a2,a3,a4



\! 

X

X

X

\+ π2

βaf2,a \+

γa

f

f

\+ ζ

γ

1,a2

1,a1 1,a2

3

af1,a \+ c4

\(6.19\)

a

a1,a2

a

where α, β, γ are rational numbers, summation indices a, a1, a2, a3, a4 run over the labels of the pentagon functions, and c4 are transcendental weight-4 constants. As we can see, they involve pentagon functions of weights up to four. We also notice that according to table 6

all pentagon functions, enumerated in table 5, appear in F \(2\), but 15 weight-four pentagon functions are absent from the two-loop ladder

. Finally, substituting the pentagon

function expressions for the pure functions \(2\)

\(2\)

h

and g

in eq. \(4.34\) we rewrite the “loop” 

i

i

negative geometry

in the pentagon functions. 

Let us summarize which of the 25 planar letters \(see appendix A.1\) are present in the iterated integral expressions for the pure functions of the negative geometries:

• The one-loop ladder

\(i.e. F \(1\)\) involves ten letters W1, . . . , W5, W11, . . . , W15. 

Whereas each \(1\)

g

, i = 1, . . . , 5, involves only 5 letters, e.g. W

i

1, W3, W5, W13, W15 are

present in \(1\)

g

, and the letter content of the remaining four pure functions is obtained 1

by cyclic shifts τ \(4.13\). 

• The two-loop ladder

involves 20 letters

W1, . . . , W5, W11, . . . , W20, W26, . . . , W30 . 

\(6.20\)

The same letters appear in all its five pure functions \{ \(2\)

h

\}5 . 

i

i=1

• The nondecomposed two-loop

\(2\)

F \(2\), as well as its pure function g

, involve 25 planar

0

letters \(i.e. all planar letters except for

\(1\)

W31\), but the letter content of \{g

\}5

is

i

i=1

more restricted. Each of them contains only 22 letters. For example, W6, W8, W10 are absent from \(2\)

g

. 

1

• There are no bonus cancellations of the letters in the “loop” 

, see \(4.34\). Namely, 

the pure function accompanying

\(2\)

ri contains the same 22 letters as g

, i = 1, . . . , 5, 

i

and and the pure function accompanying r0 contains 25 letters. 

– 40 –

In section 7, we derive a d’Alembertian differential equation for the ladder-type negative geometries. We explain in sections 8.1 and 8.2 how it restricts their letter content. 

We provide both iterated integral and pentagon function expressions for the negative geometries in the ancillary files. 

6.3

Numerical evaluation of the pentagon functions

In section 6.5, we will study numerical values of the negative geometries in the Euclidean region and evaluate them in O\(105\) kinematic points. Since the integrated negative geometries are polynomials in the planar pentagon functions, we recall the numerical evaluation of the pentagon functions. 

We rely on two complementary approaches to evaluate the pentagon functions and their derivatives, see details in appendix B.2. Firstly, we use the C\+\+ code of \[17\], which relies on a rewriting of the iterated integrals as univariate integrations of logarithms and dilogarithms and performs the quadrature numerically. Evaluations are easily parallelizable, the resulting precision is ∼ 11 digits, and evaluation time is ∼ 5 min per kinematic point per CPU. 

Secondly, having at our disposal canonical DE, summarised in \(B.15\), and the boundary condition ⃗F\(X0\), we apply DiffExp \[60\] to integrate the DE numerically using the generalized series expansions. Since the initial values are known analytically, we can achieve arbitrarily high precision of evaluations. Also, using this approach, we can evaluate the pentagon functions very close to singularities. The evaluation time is comparable with the first approach, but it could vary significantly depending on the location of the kinematic point X and the choice of the integration path connecting X0 and X. 

6.4

Final result and checks

In this work, we constructed the integrand of the two-loop ladder negative geometry in section 3 and performed two-loop integration expressing the result in terms of the planar pentagon functions, see eq. \(6.19\). In the ancillary files, we provide both Chen’s iterated integral expressions and pentagon function expressions for all two-loop negative geometries. 

In this section, we would like to summarize the checks we performed on the resulting expression. 

The obtained analytic expression possesses all expected properties. Although the negative geometries are well-defined in four spacetime dimensions and finite, we had to introduce the dimensional regulator D = 4 − 2ϵ to apply the usual calculation procedure \(based on IBP-reductions\) for the two-loop Feynman integrals \(5.1\). Because of the regulator, the intermediate expressions in our calculation contain poles 1/ϵp with p = 1, . . . , 4. The poles do cancel out among each other which is a nontrivial check on the result. Then, we expect that L-loop negative geometries evaluate to weight-2L UT functions. It does hold for our explicit results. In appendix C, we calculate the soft/collinear limits of the five-cusp negative geometries and verify that they do reproduce the known four-cusp expressions, see appendix D. Finally, based on previous four-cusp and five-cusp calculations \[17, 20\], 

we could expect that the negative geometries are positive if evaluated inside the Ampli-

– 41 –

tuhedron region. In section 6.5, we provide evidence that the obtained pentagon function expressions verify this property. 

We also performed a direct numerical check of the obtained results. We evaluate them at an Euclidean point X1, 

X1 = \(s12 = −1 , s23 = −3 , s34 = −11 , s45 = −17 , s15 = −13\) . 

\(6.21\)

On the one hand side, we have a representation for the two-loop ladder pure function \(2\)

h

as a linear combination of the two-loop Feynman integrals \(before performing IBP-2

reductions\), see eq. \(6.7\). We evaluate them numerically at X1 with 70-digit precision using AMFlow \[53\]. On the other hand side, we evaluate the pentagon functions at X1, as explained in section 6.3, and find the value of \(2\)

h

. Both evaluations match at the expected

2

precision level. We also use AMFlow to check numerically the IBP reduction rules, which we apply in our calculation, and reductions of the scalar integrals to the pure bases of MIs

\(6.11\). 

We provide reference values for F \(L\) with L = 0, 1, 2 as well as for the negative geometries at X = X1, see \(6.21\), with 12-digit precision which we obtained evaluating the pentagon functions, 

F \(0\) = −269.770449477 , 

F \(1\) = 3089.22986379 , 

F \(2\) = −43647.6529114 , 

F \(

\) = 31920.5063313 , 





F \(

\) = 35083.3435008 , 

F

= 11629.0503406 . 

\(6.22\)

One can easily see that the provided values agree with the two-loop decomposition \(2.20\). 





Note that the values for each F \(

\), F \(

\), F

are defined up to a sign, as the

corresponding canonical form has a sign ambiguity. However, all these signs are fixed once we consider these negative geometries in the context of the expansion \(2.10\) where it needs to agree with the expansion in terms of products of amplitudes \(represented by specific positive geometries\). 

6.5

Positivity properties in the Amplituhedron region

One motivation for studying negative geometry is to understand the positivity of the integrated quantities, from the Lagrangian insertion in the Wilson loop, down to individual geometric objects. The results of observables expressed in terms of pentagon function, with numerical evaluation implemented in section 6.3, provide us considerable amount of data to investigate this subject. We first recall that the positivity of the four-point observable as well as negative geometries have been fully explored in \[20\]. Later, a five-point positivity hy-pothesis for the Lagrangian insertion in the Wilson loop was proposed in \[17\], which states the observable is positive/negative definite \(depending on even/odd loop order\) within the Amplituhedron region, i.e. 

\(L\)

\(L\)

F

|

|

5

Eucl\+ < 0 at even L , 

F5

Eucl\+ > 0 at odd L . 

\(6.23\)

– 42 –

Region

configuration of si,i\+2

\# subregions

\(A\)

all si,i\+2 < 0

1

\(B\)

one si,i\+2 positive, others negative

5

\(C\)

si,i\+2, si\+1,i\+3 positive, others negative

5

Table 7: The Amplituhedron subregions. 

The Amplituhedron region Eucl\+ is the five-particle one-loop MHV amplituhedron \[4\]. In the frame x0 → ∞, see section 4.1, the momenta twistor constraints specifying this region are equivalent to, see \[17\] for more details, 

Eucl\+ :

ϵ5 > 0 , 

si i\+1 > 0 , 

i = 1, . . . , 5 . 

\(6.24\)

Thus, the Amplituhedron region is a subregion of the Euclidean region, where all adjacent Mandelstam variables are positive. It is further divided into 11 subregions according to the sign of the non-adjacent Mandelstam variables, sii\+2 in \(4.3\), which are summarized in table 7. 

Apart from the positivity property of \(L\)

F

in \(6.23\), we further argue the positivity

5

property holds for individual negative geometries that decompose the full observable. At one-loop, only the ladder

contributes to the negative geometry decomposition, so its

positivity is equivalent to eq. \(6.23\) at L = 1, 



\(

\)

F



> 0 . 

\(6.25\)

5



Eucl\+

The two-loop negative geometry decomposition \(2.20\) involves three geometries, \(2\)

\(

\)

1

\(

\)

1

F

= −F

− F

\+

F

. 

\(6.26\)

5

5

2 5

2 5

We conjecture that they take positive values, 





\(

\)

\(

\)

\(2\)

F

, F

, F



> 0 , 

and

F



< 0 . 

\(6.27\)

5

5

5



5



Eucl\+

Eucl\+

With the explicit expressions for the integrated two-loop negative geometries in terms of the pentagon functions, see eqs. \(4.29\), \(4.33\), \(4.34\), \(6.18\) and \(6.19\), we examine 105 random kinematic points from Eucl\+. We evaluate the pentagon functions using the C\+\+ code \[40\]. 3 This gives strong evidence that each negative geometry is positive \(6.27\). 

3Usually, the Euclidean region is defined such that all adjacent Mandelstam variables are negative, which is opposite to our conventions in eq. \(6.24\). This is irrelevant for us, since the pure functions are dimensionless. They depend on four dual-conformal cross-ratios \(2.5\) which are ratios of the Mandelstam variables in the conformal frame x0 → ∞. In particular, they are invariant under the sign flip of all Mandelstam invariants X → −X \(4.2\). 

– 43 –





Kinematics

F \(2\)

F \(

\)

F \(

\)

F

X\(A\)

−166839.228227

95179.9740231

215781.615620

72463.1072129

X\(B\)

−457.130590830

316.229580873

448.738525078

166.936505165

X\(C\)

−18408369.7482

34472138.5938

24656713.7133

56784251.4046

Table 8: Numerical values of the two-loop Lagrangian insertion in the Wilson loop F \(2\) and the negative geometries at the kinematic points \(6.28\) from the three different Amplituhedron subregions. 

For illustrating, in table 8, we list numeric values of two-loop Lagrangian insertion in the Wilson loop and the negative geometries at the following kinematic points, which reside in the three subregions of Eucl\+, see table 7, 



102

153

13

159 

X\(A\) = s12 = 1, 

s23 =

, 

s34 =

, 

s45 =

, 

s15 =

, 

31

4

31

4



23

4

19

4 

X\(B\) = s12 = 1, 

s23 =

, 

s34 =

, 

s45 =

, 

s15 =

, 

33

11

11

33



27

9



X\(C\) = s12 = 1, 

s23 =

, 

s34 =

, 

s45 = 108, 

s15 = 135 . 

\(6.28\)

137

37

On top of the positivity of negative geometries \(6.27\), we discovered the ladder geometries can be further triangulated within specific kinematic region. We found that the individual terms of one-loop and two-loop ladders, i.e. \(1\)

\(2\)

h

and h

in \(4.28\) and \(4.29\), 

i

i

display a particularly nice positivity property within the Amplituhedron sub-region \(A\) as follows

\(1\)

\(2\)

Region \(A\) :

\(ri − r0\) > 0 , 

h

> 0 , 

h

> 0 , 

for

i = 1, ..., 5 . 

\(6.29\)

i

i

Therefore, the postitvity of F \( \) and F \(

\) in sub-region \(A\) naturally follows as each

cyclic term, as well as the accompanying leading singularity, are already positive definite in the region. However, in region \(B\) and \(C\), the positivity of ladders F \(

\) requires

summing all 5 cyclic terms in \(4.29\). 

Lastly, the negativity of F \(2\), see eq. \(6.23\), does not follow from the positivity of the individual geometries owing to the presence of both plus and minus signs in the two-loop negative geometry decomposition \(6.26\). In the soft and collinear limit, summarised in appendix C, the five-point positivity \(6.27\) reduces to the four-point positivity \[20\] at the level of individual negative geometries. In the multi-Regge limit, see detailed discussion in appendix C.5, the dominating leading logarithmic term also exhibits the positivity property, which once again is manifest at the individual geometries. 

\(L\)

F



5

\(L\)

= q

\(log δ\)2L \+ O \(log δ\)2L−1 , 

\(6.30\)

\(0\)

2L

F5

– 44 –

where \(1\)

\(2\)

\(0\)

q

= −4 and q

= 8 are consistent with \(6.23\) \(note the ratio F

is negative

2

4

5

definite within Euclidean region\). The leading two-loop term is further divided into \(

\)

\(2\)

\(

\)

1 \(

\)

1

q

= −q

− q

\+

q

, 

\(6.31\)

4

4

2 4

2 4

where the values of \(g\)

q

are of uniform sign

4

\(

\)

\(

\)

8

\(

\)

16

q

= − , 

q

= −16 , 

q

= −

, 

\(6.32\)

4

3

4

4

3

and the relative minus signs on the RHS of \(6.31\) do not spoil the positivity of \(2\) q

. 

4

7

d’Alembertian differential equation for the ladder-type geometries

The negative geometries of the ladder type have an especially simple form, at least at the integrand level. Indeed, their integrands are constructed recursively at any loop order in section 3. The form of the integrand suggests that the loop integrations could be performed much simpler than going through the Feynman graph calculation with dimensional regularization, as we did in section 6.1. Indeed, in the four-cusp case, the ladders \(as well as all negative geometries of the tree topology\) have been solved in a closed form at any loop order

\[20\]. That was possible due to a second-order differential equation of the d’Alembertian type which relates relates L-loop and \(L \+ 1\)-loop ladders. Starting with L = 0 and solving the DE recursively, one finds ladders at any L. 

In this section, we derive an analogous d’Alembertian DE for the five-cusp ladders. We explicitly verify that the one-loop and two-loop ladders, 

and

, which are expressed

in terms of the pentagon functions, see eqs. \(6.18\) and \(6.19\), satisfy the d’Alembertian DE. 

Then, instead of using the d’Alembertian DE as an extra check of our Feynman graph calculation, we find the integrated ladders by solving the DE. In this way, we bypass loop integrations in dimensional regularization. Namely, we rely on the symbol bootstrap and pin down the symbol solution of the DE. In section 8, we work out constraints that the DE imposes on the last and next-to-last entries of the symbols and perform the symbol bootstrap analysis. 

7.1

d’Alembertian differential equation in momentum twistor variables

In contrast to several previous sections where we work in the frame x0 → ∞, we restore the Lagrangian coordinate x0. Let us consider the integrand for one of the pure functions \(L\)

h

of the L-loop ladder \(4.23\). It depends on the Lagrangian coordinate AB

ij

0 ∼ x0 in a

very special way, 

Z

\(L\)

⟨AB0ij⟩

h

\(AB

I

ij

0\) =

⟨

L\(AB1, . . . , ABL\) , 

\(7.1\)

AB0AB1⟩

AB1,...,ABL

where \(ij\) = \(13\), \(24\), \(35\), \(14\), \(25\). The explicit expression for the rational function IL

follows from eq. \(3.40\), which is the product of Cab,cd’s factors \(3.32\). We aim to find a

– 45 –

differential operator acting on AB0 ∼ x0 which simplifies the right-hand side of \(7.1\). We relate the integration over the twistor line AB1 ∼ y1 with the space-time integration, d4ZA d4Z

1

B1 = ⟨AB1⟩4d4y1 , 

\(7.2\)

vol\(GL\(2\)\)

and rewrite the momentum twistor four-brackets from \(7.1\) in terms of the space-time coordinates \(dual momenta\)

⟨AB0ij⟩ = ⟨AB0⟩⟨ij⟩\(x0 − x∗\)2 , 

⟨AB0AB1⟩ = ⟨AB0⟩⟨AB1⟩\(x0 − y1\)2

\(7.3\)

where x∗ := |j⟩⟨i|xi \+ |i⟩⟨j|xj is the space-time coordinate corresponding to the twistor line ZiZj ∼ x∗. Then we notice that the second-order differential operator

1

Dij := \(x0 − x∗\)2□x

\(7.4\)

0 \(x0 − x∗\)2

freezes the loop integration over y1 in \(7.1\), 

Z

D

\(L\)

ij h

\(AB

I

ij

0\) = −4⟨AB0ij⟩⟨AB0⟩2

L\(AB0, AB2, . . . , ABL\)

\(7.5\)

AB2,...,ABL

since the propagator is a Green’s function of the d’Alembertian operator □x , 0

1

□x

= −4iπ2δ4\(x

0

0 − y1\) . 

\(7.6\)

\(x0 − y1\)2

Moreover, taking into account the explicit expression for IL, we rewrite the right hand side of \(7.5\) as a linear combination of the pure functions of \(L − 1\)-loop ladder, X

D

\(L\)

\(L−1\)

ij h

\(AB

C

\(AB

ij

0\) = −4

kl,ij \(AB0\) hkl

0\) , 

L > 1

\(7.7\)

kl

D

\(1\)

ij h

\(AB

ij

0\) = 4 Ci\+1 j\+1,ij \(AB0\) , 

\(7.8\)

where Cij,kl\(AB0\) are obtained from Cij,kl\(CD, AB0\) \(3.32\) by taking residue at CD = AB0, Cij,kl\(AB0\) := ⟨AB0⟩2 \[⟨AB0CD⟩Cij,kl\(CD, AB0\)\]|

. 

\(7.9\)

CD=AB0

7.2

Differentiating the planar pentagon functions

In order to use d’Alembertian DE \(7.8\), we need to rewrite the differential operator Dij

\(7.4\) in convenient variables. The operator acts on a dimensionless dual-conformal invariant function \(L\)

h

, which depends on x

ij

0 only via dual-conformal cross-ratios \(2.5\). We apply the chain rule and rewrite the derivatives in x0 as derivatives in the dual-conformal cross-ratios. 

A choice of four independent cross-ratios inevitably breaks the dihedral symmetry, so we would like to find a more symmetric form of Dij. In the present work, we mainly work in the frame x0 → ∞, see section 4.1. Once Dij is written as an operator in the dual-conformal cross-ratios, we can easily choose the frame x0 → ∞ replacing the cross-ratios with ratios of Mandelstam variables X \(4.2\). Finally, we can rewrite Dij as a differential operator in

– 46 –

five Mandelstam variables instead of their ratios. At this point, it is helpful to take into account that Dij acts on dimensionless functions, which are invariant under rescaling of the Mandelstam variables, 

X

∂

\(L\)

v

h

\(X\) = 0 . 

\(7.10\)

∂v ij

v∈X

Using this freedom, we obtain for example for D13, 

5

1

X

1

− D13 =

si\+1 isi i\+2si\+2 i\+1 ∂s

∂s

−

tr− \(p3p4p5p1\) \(s34∂s \+ s15∂s \)

4

i i\+1

i\+1 i\+2

s

b b b b

34

15

13

i=1

\(7.11\)

where we assume cyclicity of the indices, i.e. 6 ≡ 1 and so on, and the chiral traces are defined in \(4.10\) and evaluated in \(4.11\) in terms of the Mandelstam variables and parity-odd ϵ5 \(4.4\). The corresponding DE \(7.7\) and \(7.8\) take the following form in the frame x0 → ∞, 

1

− D

\(1\)

13 h

=s13 , 

\(7.12\)

4

13

1





− D

\(L\)

\(L−1\)

\(L−1\)

\(L−1\)

13 h

=\(s12 \+ s23\) h

− s13 h

\+ h

4

13

13

24

25



1



\(L−1\)

\+

s23 − s45 \+

tr− \(p5 p1 p2 p3\) h

s

b

b

b

b

35

35



1



\(L−1\)

\+

s12 − s45 \+

tr− \(p1 p2 p3 p4\) h

, 

L > 1 . 

\(7.13\)

s

b

b

b

b

14

14

The differential equations and Dij in the frame x0 → ∞ for the remaining four pairs \(ij\) are obtained by cyclic shifts τ \(4.13\) of the indices in \(7.11\), \(7.12\), \(7.13\). The cyclic shift alters the first-order derivatives in the differential operator \(7.11\), but the second-order derivatives are invariant. Let us stress that the d’Alembertian DE in the frame x0 → ∞, see eq. \(7.13\), and the d’Alembertian DE at arbitrary x0, see eq. \(7.7\), are equivalent. 

Let us notice that the right-hand side of eq. \(7.13\) contains four linear independent rational factors. Namely, among five rational functions in the right-hand side of d’Alembertian DE \(7.7\), 

C12,ij , C23,ij , C34,ij , C45,ij , C15,ij

\(7.14\)

with j = i \+ 2, only four of them are linear independent, since Ci\+1i\+3,ii\+2 = Ci−1i\+4,ii\+2. 

The one-loop ladder

and the two-loop ladder

, which we calculated in the

previous sections, have to satisfy the d’Alembertian DE. We choose \(ij\) = \(13\), and recall various notations for the corresponding pure function of the one-loop ladder \(1\) \(1\)

h

≡ g

≡

13

2

\(2\)

\(2\)

\(2\)

h

and of the two-loop ladder h

≡ h

, see eqs. \(4.27\) and \(4.30\). The one-loop DE

2

13

2

\(7.12\) is immediate to verify by acting with the second-order differential operator \(7.11\) on the dilogarithmic expressions for the pure functions of the one-loop ladder \(4.31\). 

Then, we would like to verify DE \(7.13\) at L = 2, which relates the one-loop and two-loop ladders. Both the one-loop and two-loop ladders are expressed as UT polynomials in the pentagon functions of the transcendental weights two and four, respectively, see

– 47 –

eqs. \(6.18\) and \(6.19\). As reviewed in appendix B.2, taking derivatives of the pentagon functions, we stay in the space of the pentagon functions. Thus, we calculate the second-order derivatives of \(2\)

h

and express them in the pentagon functions. In general, the resulting

13

expression is a polynomial in pentagon functions \(with rational coefficients in Mandesltam variables and ϵ5\), which has transcendental weight-two and weight-three components. We verify that differentiating \(2\)

h

by D

13

13 \(7.11\), the weight-three component vanishes and the weight-two component reproduces the right-hand side of eq. \(7.13\) at L = 2. 

In principle, the DE \(7.12\) and \(7.13\) supplemented with boundary conditions uniquely fix the ladders at any loop order. Instead of trying to solve the second-order partial differential equations, we work out the constraints they impose on pure functions \(L\) h

and use

ij

them in the symbol bootstrap analysis in the next section. 

8

Symbol bootstrap of the ladder-type negative geometries

We performed loop integrations of the one-loop and two-loop ladder negative geometries relying on a conventional Feynman diagram calculation and IBP-reductions, see section 6.1. 

In this approach, we had to calculate a family of the two-loop Feynman integrals \(5.1\). Their analytic structure is governed by the 111-letter alphabet, \(5.29\). However, a much smaller sub-alphabet – the planar pentagon alphabet – is required for the negative geometries up to the two-loop order. In this section, we would like to show that the loop integrations of ladders

and

can be performed in a much simpler way relying on the symbol

bootstrap. 

Due to the leading singularity analysis of the ladder integrand, we know that \(L\) h

is

ij

a pure function. The absence of double poles in the integrand suggests that \(L\) h

is UT

ij

of transcendental weight 2L. Let us assume that this function is expressible in terms of iterated integrals with dlog kernels, and that the relevant symbol alphabet is the planar pentagon alphabet \(5.28\), appendix A.1. The assumption about the alphabet is crucial for the bootstrap. 

We recall that the pure functions of the ladder are related by cyclic shifts τ. For example, once \(L\)

\(L\)

\(L\)

h

is known, other h

are obtained by cyclic shifts, \{τkh \}4 . In

13

ij

13

k=0

the following, for the sake of simplicity, we prefer to work at the symbol level omitting all transcendental constants in the iterated integral representation, see section 5.3. Each symbol term of \(L\)

h

contains 2L entries, 

ij





X

S

\(L\)

h

=

c

\[W , . . . , W

\]

\(8.1\)

ij

i1,...,i2L

i1

i2L

i1,...,i2L

where summation indices run over labels of the planar pentagon alphabet letters \(5.28\), 

and c’s are indeterminate rational numbers, which we would like to pin down using some constraints on \(L\)

h

. A symbol can be lifted to a function if and only if the symbol satisfies ij

the integrability condition for each pair of adjacent entries, 

X

ci

\[W , . . . , W

, W

, . . . , W

\] d log W

∧ d log W

= 0

\(8.2\)

1,...,i2L

i1

ik−1

ik\+2

i2L

ik

ik\+1

i1,...,iL

– 48 –

where k = 1, . . . , 2L − 1. 

According to our assumption, the symbol entries are letters of the planar pentagon alphabet \(5.28\). The pure function \(L\)

h

is dimensionless, but some of the alphabet let-

ij

ters have nonzero dimensions. So, we draw symbol entries from a set of 25 dimensionless combinations of the letters, see appendix A.1, 

2-loop

A

∪ \{

∪ \{

pl

:= \{\[W1\] − \[Wi\]\}20

i=2

\[Wi\]\}30

i=26

2\[W1\] − \[W31\]\} . 

\(8.3\)

This reduces the number of indeterminates c’s in \(8.1\). 

The first entries of the symbol specify the location of the discontinuities. If \(L\) h

has a

ij

nonzero discontinuity, then one of the adjacent Mandlestam invariants vanishes, sii\+1 = 0. 

For example, inspecting the two-loop Feynman diagrams \(5.1\), we conclude that their unitarity cuts are located at sii\+1 = 0. Thus, there are four dimensionless combinations of the letters which are allowed first entries, 

First entries :

\[W1\] − \[W2\], \[W1\] − \[W3\], \[W1\] − \[W4\], \[W1\] − \[W5\] . 

\(8.4\)

The counting of integrable weight-2L symbols with first entries drawn from eq. \(8.4\)

and other entries drawn from \(8.3\) is provided in the first column of table 10. 

8.1

The last entry condition

Differentiation acts on the last entry of the symbol. We use d’Alembertian differential equation \(7.7\) to obtain some simple constraints on the last entries of the symbol \(8.1\). Let us split weight-2L symbol \(8.1\) into weight-\(2L − 2\) and weight-2 symbols, X

S

\(L\)

h

=

S\(2L−2\) ⊗ S\(2\)

\(8.5\)

ij

a

a

a

where we arrange the terms such that both sets \{ \(2L−2\)

\(2\)

Sa

\} and \{Sa \} are linearly indepen-

dent. Acting with the second-order differential operator on an integrable weight-2L symbol results in a linear combination of weight-\(2L−1\) and weight-\(2L−2\) symbols. That means that D

\(2\)

ij Sa

is a linear combination of weight-1 and weight-0 symbols, see eq. \(5.25\), 





X

D

\(L\)

ij S

h

=

S\(2L−2\) ⊗ D

ij

a

ij S\(2\)

a

. 

\(8.6\)

a

On the other hand, the right-hand side of eq. \(7.7\) has weight \(2L − 2\), so it does not contain a weight-\(2L − 1\) symbol component. Thus, because of linear independence, each D

\(2\)

\(L\)

ij Sa

has to be a rational function. In other words, the last entries of the symbol S gij are annihilated by Dij. 

For the planar pentagon alphabet, we find 11 dimensionless weight-1 symbols that are annihilated by Dij. For example, for D13 we have, 

2-loop

ker\(D13\) ∩ Apl

= \{\[W1\] − \[W2\], \[W1\] − \[W4\], \[W3\] − \[W5\], \[W1\] − \[W11\], 

\[W4\] − \[W14\], \[W5\] − \[W15\], \[W3\] − \[W17\] − \[W26\], 

\[W3\] − \[W18\] \+ \[W27\], \[W3\] − \[W19\] \+ \[W28\], 

\[W3\] − \[W20\] − \[W29\], \[W1\] − \[W16\] \+ \[W30\]\} , 

\(8.7\)

– 49 –

weight-2 symbols integrable last entry annihilated by Dij 25 ∗ 25

394

91

65

\(2\)

Table 9: The counting of the planar pentagon weight-2 symbols \{Sa \}, which are the two rightmost entries in eq. \(8.5\), and are annihilated by the second-order differential operator Dij \(7.4\). 

as admissible last entries of 





S

\(L\)

\(L\)

h

. The last entries of S h

are obtained by cyclic

13

ij

permutations τ \(A.1\) in eq. \(8.7\). 

8.2

The next-to-last entry condition

We can obtain more constraints on \(L\)

h

, even without knowing the explicit expressions of

ij

the pure functions on the right-hand side of DE \(7.7\). Indeed, each D

\(2\)

ij Sa

\(8.6\) has to

be a linear combination of the rational functions appearing on the right-hand side of eq. 

\(7.7\). This fact imposes constraints on the next-to-last entries of the symbol S

\(L\)

h

. Let

ij

us work out these constraints more explicitly. 

The weight-2 symbols \{ \(2\)

Sa \}, which are the two rightmost entries in \(8.5\), have to be integrable in order to correspond to a pure function, i.e. eq. \(8.2\) at k = 2L − 1 has to be satisfied. For the planar pentagon alphabet, we find 394 linearly independent integrable symbols built from dimensionless combinations of the letters \(8.3\). Imposing the last letter condition \(8.7\) brings their number down to 91. Among these 91 weight-2 symbols, 65 are annihilated by Dij, see table 9. As we noted previously, among the five rational functions

\(7.14\), only four are linearly independent. For each of the four rational functions Ckl,ij, we find a solution \(2\)

Sa

in the linear space of the 91 integrable weight-2 symbols, 

DijS\(2\)

a

= Ckl,ij . 

\(8.8\)

Thus, among the 91 weight-2 symbols \{ \(2\)

Sa \} in eq. \(8.5\), only 65\+4 symbols are compatible

with the rational factors on the right-hand side of eq. \(7.7\). 

8.3

Bootstrap constraints

Let us combine together the constraints on the symbol outlined above to pin down the indeterminates c’s in eq. \(8.1\). The counting at loop order L = 1, 2, 3 is summarized in table 10. In the first column of table 10, we count the number of integrable symbols, see eq. \(8.2\), with dimensionless entries \(8.3\) and the first entries drawn from \(8.4\). In the second column, we impose the last entry condition \(8.7\). In the third column, we also constrain the next-to-last entries as explained in section 8.2. The d’Alembertian DE

provides more constraints on \(L\)

\(L−1\)

h

provided h

is known. Namely, we demand that

ij

ij

inhomogeneous d’Alembertian DE \(7.13\) with the known right-hand side is satisfied. In the fourth column, we count the number of indeterminates provided the DE is satisfied. 

– 50 –

L

integrability last entry next-to-last entry DE physical singularities

1

20

9

6

6

0

2

525

84

49

24

0

3

14990

1012

354

−

−

Table 10: The counting of indeterminates in the weight-2L symbol ansatz for the pure function \(L\)

h

of the L-loop ladder negative geometry after consecutively imposing constraints: ij

integrability of the symbol \(8.2\) built from dimensionless letters \(8.3\) of the planar pentagon alphabet and having correct first entries \(8.4\), the last entry condition \(8.7\), the next-to-last entry condition, d’Alembertian DE \(7.13\), and absence of spurious singularities \(8.9\). 

In order to fix a unique solution of the DE we need to supplement it with the boundary conditions. We fix the remaining indeterminates in the symbol expression \(8.1\) at L = 1, 2

demanding that the ladder has correct singularities. Indeed, the rational prefactor r2 − r0, which accompanies \(L\)

h

in expression \(4.29\) of the ladder, has a pole at s

13

13 = 0, see \(4.8\). 

This spurious pole should be absent from the ladder, so it has to be suppressed by the zero of \(L\)

h

at s

13

13 = 0. In appendix C.4, we checked explicitly that spurious poles are absent using explicit pentagon function expressions for the one-loop and two-loop ladders. Now, we use this property as a bootstrap constraint for the symbol \(8.1\), 





S

\(L\)

h



= 0 . 

\(8.9\)

i i\+2 si i\+2=0

In this way, we find all indeterminates c in the symbol expression \(8.1\) of the one-loop and two-loop ladders. They agree with the result of the Feynman graph calculation in section 6.1. However, we find a contradiction in the three-loop bootstrap imposing the d’Alembertian DE, see table 10. This implies that the main bootstrap assumption – the planar pentagon alphabet \(5.28\) – fails at L ≥ 3. In other words, the three-loop ladder requires a larger symbol alphabet. 

8.4

Looking into the three-loop planar pentagon alphabet

The symbol bootstrap analysis performed above suggests that the 26-letter planar pentagon alphabet \(5.28\) is not sufficient to express the three-loop ladder. Besides the three-loop ladder

, we could ask about the symbol alphabet for other three-loop negative geometries and for the three-loop Lagrangian insertion in the Wilson loop F \(3\). 

In contrast with negative geometries, the Lagrangian insertion in the Wilson loop is planar in the large color limit. The integrand of F \(L\) \(2.4\) is built from the four-dimensional loop integrands of the planar MHV amplitudes, as explained in \[13, 15, 17\]. Thus, the integrand of F \(L\) involves only planar families of Feynman integrals. More precisely, after switching to the frame x0 → ∞ and introducing momentum variables \(4.1\), the integrand of F \(L\) is decomposed in a basis of the five-particle L-loop planar families of Feynman integrals, as well as products of lower-loop planar families. For example, in the two-loop

– 51 –

case, L = 2, the planar pentabox family, fig. 1a, and the product of the one-loop pentagon families are required. In the three-loop case, L = 3, there are four five-particle three-loop planar families. 

*p*

*p*

4

5

*p* 5

*p* 3

*p* 1

*p* 4

*p* 2

*p*

*p*

3

1

*p* 2

\(a\)

\(b\)

Figure 7: Diagram \(a\) The 8-propagator sub-sector in a five-particle three-loop planar family, which requires c

W1 \(8.10\) in its iterated integral expression. Diagram \(b\) Another 8-propagator sub-sector in a five-particle three-loop planar family, which requires the square-root letter f

W16 \(5.33\) and algebraic letters f

W41, f

W46, f

W51, f

W76 in its iterated

integral expression. 

We refrain from a detailed discussion of the planar three-loop families here. We only note that they do require the 26-letter planar pentagon alphabet \(5.28\) to be extended by at least 30 new letters. We consider certain subsectors of the three-loop planar topologies, construct canonical DE on their maximal cuts, and identify new letters in them. 

Firstly, we find a cyclic orbit of 5 new letters \{

, which are quadratic in the

c

Wi\}5i=1

Mandelstam variables, 





c

Wi = τ i−1 c

W1

, 

c

W1 = s23s34 − s34s45 \+ s45s15 , 

i = 1, . . . , 5 . 

\(8.10\)

The letter c

W1 is present in the iterated integral expressions for the five-particle three-loop planar Feynman integrals depicted in fig. 7a. We constructed a pure basis of 2 MIs on the maximal cut of this 8-propagator sector and derived the canonical DE. The connection matrix of the DE does contain the letter c

W1. 

Secondly, we consider the 8-propagator planar three-loop sector in fig. 7b, and we construct a pure basis of 8 MIs of its maximal cut. Surprisingly, we find that the corresponding canonical DE involves some letters of the two-loop non-planar 11-propagator topologies discussed in section 5.4. Namely, we observe that letter

\(1\) \(5.33\) is present, as well

f

W16 = ∆4

as the algebraic letters f

W41, f

W46, f

W51, see eqs. \(A.11\) to \(A.13\), which involve the square q

q

root

\(1\)

\(1\)

∆

, and the algebraic letter

∆

and

4

f

W76 \(A.20\), which involves simultaneously

4

√∆5. In other words, this three-loop sector requires 5 new letters, which are absent in the two-loop planar topologies. Supplementing them with their cyclic permutations results in 25 new letters, i.e. the square-roots of \{ \(i\)

∆

\}5

\(5.32\) and all algebraic letters from

4

i=1

appendix A.2 involving these square roots. 

The 8-propagator sectors in figs. 7a and 7b are subsectors of the same 11-propagator family of the three-loop planar five-point Feynman integrals. We also attempted a more

– 52 –

systematic search for new letters in the planar three-loop five-point families and their subsectors using the computer codes \[56–58\], which perform the Landau analysis. Using these codes, we were able to detect letters c

W1 and f

W16 in the sectors depicted in figs. 7a and 7b, 

and we found no new letters in other inequivalent sectors of the three-loop planar families. 

Relying on this evidence, we conjecture the three-loop planar pentagon alphabet, 3-loop

2-loop

A

=

∪ \{

∪ \{

∪ \{

∪ \{

pl

Apl

c

Wi\}5i=1

f

Wi\}20

i=16

f

Wi\}55

i=41

f

Wi\}80

i=76 , 

\(8.11\)

where we recall expressions for the letters a given in eqs. \(5.28\), \(5.33\), \(8.10\), \(A.6\), \(A.11\)

to \(A.13\) and \(A.20\). This 56-letter alphabet is necessary for calculating three-loop five-particle scattering amplitudes in a massless QFT. Indeed, all 56 letters do appear in the iterated integral expressions of individual three-loop Feynman integrals. However, only a subset of letters could be necessary for the three-loop Lagrangian insertion \(3\) F

\(2.4\). 

5

Compared to the planar integrand of \(3\)

F

, the integrands of the three-loop ladder and

5

other nonfactorizable negative geometries are nonplanar. They are expanded in a basis of more complicated three-loop families of Feynman integrals, which in general require an extension of the 111-letter nonplanar alphabet \(5.29\). These nonplanar letters could in principle contribute to the three-loop ladder. In \[61\], we study this question and perform the symbol bootstrap of the three-loop ladder and other negative geometries. 

9

Summary and discussion

Let us summarize the main results of this paper. In the ancillary files, we give

• The analytic formulae of full Wilson loop observable, and its negative geometry decomposition up to L = 2, expressed as iterated integrals and pentagon functions \[40\], 

e.g. the two-loop full observable is provided in 2loop\_full − WL\_iter\_integrals.m and 2loop\_full − WL\_pent\_functions.m, with the leading singularities and constants \(numerical values\) defined in rCoefficients.m, and constant\_definitions.m \(constant\_values.m\), respectively. 

• The pure basis for two-loop five-point family \(5.1\) for negative geometry integrals, MIs\_DP\_1.txt and MIs\_DP\_2.txt, and their differential equations, Atilde\_DP\_1.m and Atilde\_DP\_2.m, in terms of the 111 letters in \(5.21\), letters.m, discussed in

Sec.5. 

• The multi-Regge limit behavior, see appendix C.5, of full Wilson loop observable and negative geometries up to L = 2, with the weight-1 and weight-3 functions defined in funct\_definitions\_regge.m. 

Using these results, we analyzed the decomposition of the five-point Wilson loop with Lagrangian insertion into geometric building blocks, to see whether this makes the observed positivity properties \[17\] of the integrated one- and two-loop expressions more manifest. 

The building blocks involve Feynman integrals that go beyond those computed in reference

\[40, 42\], so we computed the additional integral families with the help of the differential

– 53 –

equations method. This allowed us to determine the full negative geometry decomposition of the five-point two-loop Wilson loop with Lagrangian insertion. We found that the new scalar master integrals that we computed involve additional alphabet letters, which however drop out in the two-loop negative geometry building blocks. As a consistency check of our result, we evaluated soft and collinear limits. 

Having obtained the two-loop negative geometry expansion, we then investigated the positivity properties of the individual contributions. We found that each piece has a uniform sign when the kinematics is evaluated in the Amplituhedron region, cf. Table 8. 

Finally, we studied a complementary approach that may be suitable for obtaining higher-loop results. To begin with, we derived the all-loop integrand for the five-point ladder-type geometries, with the final expression given in eq. \(3.40\). We organized the integrals in a way that makes their leading singularities manifest. Interestingly, for products of ladder geometries, new leading singularities appear, which however drop out for the full observable. The general structure of leading singularities will be discussed in more detail in upcoming work \[30\]. 

From our explicit integrand expressions it is easy to see that the ladder-type integrals satisfy a d‘Alembertian differential equation, similar to the four-point case \[20\]. Such an equation is known to be powerful, especially when combined with bootstrap ideas. We therefore rederived the expression for the two-loop ladder from such a bootstrap approach. 

We then attempted to obtain the answer for the three-loop ladder from the same bootstrap ansatz, but this was unsuccessful. We conclude that at this loop order, the ansatz needs to be extended by additional symbol letters. Performing a Landau analysis of planar three-loop integrals we identified several potential new letters. A dedicated bootstrap analysis involving these additional letters will be discussed elsewhere \[61\]. 

There are several further directions for future investigations:

• Given the uniform sign properties we observed in the individual integrated negative geometries, it would be very interesting also look for possible monotonicity properties in derivatives, as suggested in reference \[62\]. 

• Furthermore, it would be interesting to derive the negative geometry integrands for six and more particles. The six-particle case would be particularly interesting in view of recent progress on the planar two-loop function space \[63\], as this could serve as a first application of those hexagon functions. 

• Multiple Lagrangian insertions in the Wilson loop are also of interest. In particular, the double Lagrangian insertion in the four-cusp Wilson loop has been considered recently in \[64\] and its positivity in the Amplituhedron region has been observed. It would be interesting to study this case from our geometric viewpoint. 

• Finally, another natural extension of this work could be to analyse similar properties for integrated negative geometries in the ABJM theory, cf. \[65–68\]. 

– 54 –

Acknowledgments

It is a pleasure to thank Taro Brown, Antonela Matijašić, Elia Mazzuchelli, Chenyu Wang, and Qinglin Yang for discussions. Funded by the European Union \(ERC, UNIVERSE

PLUS, 101118787\). Views and opinions expressed are however those of the authors only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them. D.C. is supported by ANR-24-CE31-7996. J.T. is supported by the U.S. Department of Energy, grant No. SC0009999 and the funds of the University of California. 

– 55 –

A

Two-loop alphabet letters

In this Appendix, we complement definitions of the alphabet letters outlined in section 5.4. 

A.1

Planar pentagon letters

The planar pentagon letters 2-loop

A

\(5.28\) are in accordance with the definition in the

pl

literature \[40\]. They are organized in the cyclic orbits, see \(4.13\), 

Wi\+5k = τ i−1 \(W1\+5k\) , 

i = 1, . . . , 5, 

k = 0, 1, 2, 3, 5 , 

\(A.1\)

and W31, which is the square root of the Gram determinant \(4.5\), is cyclic invariant, p

W31 =

∆5 . 

\(A.2\)

20 letters \{Wi\}20 are linear in Mandelstam variables. They are cyclic shifts of i=1

W1 = s12 , 

W6 = s34 \+ s45 , 

W11 = s12 − s45 , 

W16 = s12 \+ s23 − s45 . 

\(A.3\)

5 letters \{Wi\}30 are algebraic. They are cyclic shifts of

i=26

√

−s12s15 \+ s12s23 − s23s34 − s15s45 \+ s34s45 −

∆5

W26 =

√

. 

\(A.4\)

−s12s15 \+ s12s23 − s23s34 − s15s45 \+ s34s45 \+

∆5

Let us also note that the algebraic letters can be rewritten in terms of the chiral traces

\(4.10\) and in terms of the rational prefactors \{ri\}5 \(4.8\), 

i=1

tr− \(p4p5p1p2\)

s24 \(r3\)2

W

b b b b

26 =

\(A.5\)

tr

=

\+ \(p p p p

s

b4 b5 b1 b2 \)

12s45s3

15

√

provided we choose the branch of the square root as ∆5 = ϵ5. 

A.2

Nonplanar algebraic letters

The 11-propagator family of Feynman integrals \(5.1\) requires the planar pentagon alphabet to be extended by 85 letters \{

, see eq. \(5.29\). We presented definitions of 20

f

Wi\}85

i=1

polynomial letters \{

in section 5.4. Here we collect definitions of 65 algebraic letters f

Wi\}20

i=1

\{

, organizing them in cyclic orbits, 

f

Wi\}85

i=21





f

Wi\+5k = τ i−1 f

W1\+5k , 

i = 1, . . . , 5, 

k = 4, . . . , 16 . 

\(A.6\)

The algebraic letters involve the square roots of

\(i\)

\(i\)

∆5, ∆ , ∆ , see eqs. \(4.5\), \(5.31\)

2

4

and \(5.32\). They have the form \(5.36\) and involve one or two square roots, see table 4. 

– 56 –

45 algebraic letters involve a single square root. Indeed, 20 letters \{

involve the

f

Wi\}40

i=21

square root of \(i\)

∆

\(5.31\). They are cyclic shifts of

2

q

\(1\)

s12 −

∆2

f

W21 =

, 

\(A.7\)

q

\(1\)

s12 \+

∆2

q

\(1\)

s12 − 2 s34 −

∆2

f

W26 =

, 

\(A.8\)

q

\(1\)

s12 − 2 s34 \+

∆2

q

\(1\)

s12s15 \+ s12s34 \+ 2s23s34 − \(s15 − s34\)

∆2

f

W31 =

, 

\(A.9\)

q

\(1\)

s12s15 \+ s12s34 \+ 2s23s34 \+ \(s15 − s34\)

∆2

q

\(1\)

s12s23 \+ s12s45 \+ 2s15s45 − \(s23 − s45\)

∆2

f

W36 =

. 

\(A.10\)

q

\(1\)

s12s23 \+ s12s45 \+ 2s15s45 \+ \(s23 − s45\)

∆2

15 letters \{

involve the square root of \(i\) \(5.32\). They are cyclic shifts of f

Wi\}55

∆

i=41

4

q

−

\(1\)

s12s15 \+ s12s23 \+ 2s15s34 − s23s34 \+ s34s45 −

∆4

f

W41 =

, 

\(A.11\)

q

−

\(1\)

s12s15 \+ s12s23 \+ 2s15s34 − s23s34 \+ s34s45 \+

∆4

q

−

\(1\)

s12s15 − s12s23 \+ s23s34 − s34s45 −

∆4

f

W46 =

, 

\(A.12\)

q

−

\(1\)

s12s15 − s12s23 \+ s23s34 − s34s45 \+

∆4

q

−

\(1\)

s12s15 \+ s12s23 − s23s34 − s34s45 −

∆4

f

W51 =

. 

\(A.13\)

q

−

\(1\)

s12s15 \+ s12s23 − s23s34 − s34s45 \+

∆4

10 letters \{

involve the square root of

f

Wi\}65

∆

i=56

5 \(4.5\). They are cyclic shifts of

√

−s12s15 − s12s23 − s23s34 − s15s45 \+ s34s45 −

∆5

√

f

W56 =

, 

\(A.14\)

−s12s15 − s12s23 − s23s34 − s15s45 \+ s34s45 \+

∆5

√

q61 − \(s34 \+ s45\) ∆5

√

f

W61 =

, 

\(A.15\)

q61 \+ \(s34 \+ s45\) ∆5

where we introduce a shorthand notation for the polynomial in the Mandelstam variables, q61 := − s12s15s34 \+ s12s23s34 − s23s234 \+ s12s15s45 − s12s23s45 − s15s34s45

− s23s34s45 − s2

−

34s45 − s15s2

45

s34s245 . 

\(A.16\)

Similar to the planar case, these letters are related to the rational prefactors \{ri\}5 , see i=0

eqs. \(4.7\) and \(4.8\), 

s35 \(r0 − r4\)2

f

W61 = −

. 

\(A.17\)

s34s45

f

W13

– 57 –

The remaining 20 algebraic letters involve a pair of square roots. 10 letters \{f Wi\}75

i=66

involve the square roots of

\(i\)

∆5 and ∆

simultaneously, and they are cyclic shifts of

2

q

√

q

√

\(1\)

\(1\)

q66 −

∆

∆

q

∆

∆

2

5

71 −

2

5

f

W66 =

, 

f

W

, 

\(A.18\)

q

√

71 =

q

√

\(1\)

\(1\)

q66 \+

∆

∆

q

∆

∆

2

5

71 \+

2

5

where

q66 :=s212s15 − s212s23 \+ s12s23s34 − s12s15s45

− s12s34s45 − 2s15s34s45 \+ 2s23s34s45 \+ 2s234s45 , 

q71 := − s212s15 \+ s212s23 − s12s23s34 \+ s12s15s45

− s12s34s45 \+ 2s15s34s45 − 2s23s34s45 \+ 2s34s245 . 

\(A.19\)

5 letters \{

involving square roots of

\(i\) simultaneously are cyclic shifts of

f

Wi\}80

∆

i=76

5 and ∆4

q

√

\(1\)

q76 −

∆

∆

4

5

f

W76 =

, 

\(A.20\)

q

√

\(1\)

q76 \+

∆

∆

4

5

where

q76 := − s2

−

12s2

15 \+ 2s2

12s15s23 − s2

12s2

23

2s12s15s23s34 \+ 2s12s223s34

− s223s234 \+ s12s215s45 − s12s15s23s45 − 2s12s15s34s45 − 2s12s23s34s45

− s15s23s34s45 \+ 2s23s2

−

34s45 \+ s15s34s2

45

s234s245 . 

\(A.21\)

5 letters \{

involve the square roots of \(i\) and \(i\+1\) simultaneously, and they are

f

Wi\}85

∆

∆

i=81

2

2

cyclic shifts of

q

q

\(1\)

\(2\)

s12s23 \+ 2s15s45 \+ 2s34s45 −

∆

∆

2

2

f

W81 =

. 

\(A.22\)

q

q

\(1\)

\(2\)

s12s23 \+ 2s15s45 \+ 2s34s45 \+

∆

∆

2

2

– 58 –

B

Pentagon functions

B.1

Review of planar pentagon functions

The pentagon functions \[40, 41\] employed in section 6 have the following schematic expressions as iterated integrals

X

f1,a =

αa,i \[Wi\]

, 

\(B.1\)

X0

i

X

f2,a =

αa,ij \[Wi, Wj\]

, 

\(B.2\)

X0

i,j

X

f3,a =

αa,ijk \[Wi, Wj, Wk\]

\+ π2 X β

\+ β

X

a,i \[Wi\]

ac3 , 

\(B.3\)

0

X0

i,j,k

i

X

f4,a =

αa,ijkm \[Wi, Wj, Wk, Wm\]

\+ π2 X β

X

a,ij \[Wi, Wj \]

0

X0

i,j,k,l

i,j

X

\+

\(γa,ic3 \+ δa,iζ3\) \[Wi\]

\(B.4\)

X0

i

where summation indices i, j, k, m run over labels of the planar letters 2-loop A

\(5.28\), 

pl

α, β, γ, δ are rational numbers, and we denote by c3 a transcendental weight-3 constant.4

Taking into account transcendental weight of π2 and ζ3 constants, one can easily see that fw,a is UT of weight w. 

Since the iterated integrals vanish when evaluated at their reference point, we immediately obtain analytic values of the pentagon functions at X = X0, 

f1,a\(X0\) = f2,a\(X0\) = f4,a\(X0\) = 0 , 

f3,a\(X0\) = βac3 . 

\(B.5\)

The iterated integrals obey the shuffle algebra relations which imply that the product of two iterated integrals of weights w1 and w2 is an iterated integral of weight w1 \+ w2, X

\[Wi , . . . , W

\]

\[W , . . . , W

\]

=

\[W , . . . , W

\]

\(B.6\)

1

iw

j

j

k

k

1

X

1

w

1

w

0

2

X0

1\+w2

X0

where summation \{k1, . . . , kw

\} runs over the shuffle product \{i

\}\{j

\}. 

1\+w2

1, . . . , iw1

1, . . . , jw2

Then, the product of pentagon functions respects the weight-grading, i.e. fw f

is

1,a1

w2,a2

a weight-\(w1 \+ w2\) UT combination of the iterated integrals. The pentagon functions are defined such that they are algebraically independent, i.e. all monomials in the pentagon functions are linearly independent. Namely, for each weight w = 1, . . . , 4, all weight-w monomials

fw,a , 

fw

f

|w1,w2>0

f

f

|w1,w2,w3>0

1,a1

w2,a2 w

w

w

1\+w2=w , 

fw1,a1

2,a2

3,a3 w1\+w2\+w3=w , 

fw

f

f

f

|w1,w2,w3,w4>0

\(B.7\)

1,a1

w2,a2 w3,a3 w4,a4 w1\+w2\+w3\+w4=w

4c3 is denoted as d37,3 ≈ −6.02201193 in \[40\], and it is known analytically as a weight-3 combination of Goncharov polylogarithms. 

– 59 –

are linearly independent. 

Let us notice that the basis of the pentagon functions, as they are defined in \[40, 41\], 

can be not optimal for the negative geometries. Indeed, the iterated integral expressions

√

of the negative geometries do not contain the planar letter W31 = log\( ∆5\), whereas W31

does appear in some weight-four pentagon functions f4,a, see \(B.4\), present in \(6.19\). From this point of view, the letter W31 is spurious, and it cancels from \(6.19\) upon substitution of eqs. \(B.1\) to \(B.4\) and applying the shuffle algebra \(B.6\). A similar observation on letter W31 has been made for finite parts of five-particle amplitudes in N = 4 sYM \[69, 70\], 

maximal super-gravity \[71, 72\], and massless QCD. 

B.2

Derivatives of planar pentagon functions

In section 7, we calculate second derivatives of the negative geometries in the kinematic variables, and in appendix C, we study their singular limits. Both these tasks require differentiation of the pentagon functions. In this appendix, we calculate their first-order derivatives, reexpress them in the pentagon function basis, and derive a system of the first-order differential equations for them. The latter is also helpful for numerical evaluation of the pentagon functions. 

The pentagon functions are defined as iterated integrals, eqs. \(B.1\) to \(B.4\), so their differentiation is straightforward \(5.25\) and decreases the transcendental weight by one, X

\(i\)

dfw,a =

h

d log W

w−1,a

i

\(B.8\)

i

where w = 0, . . . , 4, summation index i runs over the planar pentagon letters, h−1 = 0, and \(i\)

h

with w = 1, . . . , 4 are weight-\(w − 1\) UT linear combinations of the iterated w−1,a

integrals. They are expandable in the pentagon function basis, i.e. they are polynomials in the pentagon functions and transcendental constants π2 and ζ3, 

\(i\)

h

= α\(i\)

0,a

a

, 

\(B.9\)

\(i\)

X

\(i\)

h

=

α

f

1,a

a,b

1,b , 

\(B.10\)

b

\(i\)

X

\(i\)

X

\(i\)

h

=

β

f

α

f

2,a

a,b 2,b \+

a,bc 1,bf1,c \+ π2β\(i\)

a

, 

\(B.11\)

b

b,c

\(i\)

X

\(i\)

X

\(i\)

X

\(i\)

\(i\)

h

=

γ

f

β

f

α

f

δ

f

3,a

a,b 3,b \+

a,bc 1,bf2,c \+

a,bcd 1,bf1,cf1,d \+ π2 X a,b 1,b \+ ζ3γ\(i\)

a

b

b,c

b,c,d

b

\(B.12\)

where α, β, γ, δ are rational constants, and indices a, b, c, d run over labels of the pentagon functions. 

Thus, the derivatives of the pentagon functions are expressed in the pentagon functions. 

In order to derive a closed system of differential equations for the pentagon functions, we need to differentiate all \{ \(i\)

hw,a\}3

from eq. \(B.8\), 

w=0

X

\(ij\)

dh\(i\)

w,a =

h

d log W

w−1,a

j

\(B.13\)

j

– 60 –

where \(ij\)

h

are weight-\(w − 1\) UT linear combinations of the iterated integrals for w =

w−1,a

1, . . . , 3, which are again expressible in the basis of the pentagon functions. Continuing iterative differentiations of \{ \(ij\)

\(ijkl\)

hw,a\}2

, we eventually end up with rational constants h

. 

w=0

0,a

Their derivatives vanish. Thus, we complement the 83 pentagon functions \(see table 5\) by their multiple derivatives

\{

\(ijk\)

fw,a\}4

\}3

\}2

\}

w=0 , 

\{h\(i\)

w,a w=1 , 

\{h\(ij\)

w,a w=1 , 

\{h

, 

\(B.14\)

1,a

and choose a maximal Q-linear independent set ⃗F among them, which we find to contain 165 elements. We choose the first 83 entries of ⃗F to be the pentagon functions, and the last 82 entries are UT polynomials in them of weights 2, 3. Then, the iterative derivatives

\(B.8\), \(B.13\), and so on, are combined in a system of canonical DE, X

d ⃗

F\(X\) =

A\(i\)⃗

F\(X\) d log \(Wi\(X\)\)

\(B.15\)

i

where A\(i\) are 165 × 165 nilpotent matrices of rational numbers, and summation i runs over planar pentagon letters. As compared to canonical DE \(5.19\) for the pure MIs, the canonical DE \(B.15\) does not involve ϵ. 

In order to be able to solve for ⃗F, we need to supplement DE \(B.15\) with the initial values. We know values ⃗F\(X0\) at the Euclidean X0 \(5.26\), which is the reference point of the iterated integrals. Indeed, we know analytic values \{fw,a\(X0\)\} of the pentagon functions, see \(B.5\), and all entries of ⃗F are polynomial in the pentagon functions. 

C

Soft, collinear, and multi-Regge limits

In this Appendix, we calculate the asymptotics of the five-cusp negative geometries in various singular regimes. By singular regimes, we imply kinematics for which letters of the planar pentagon alphabet become infinite or vanish. In appendix C.2, we consider the soft limit when one of the pentagon contour edges shrinks to a point. In this limit, we expect the negative geometries to reduce smoothly to their four-cusp counterparts, see appendix D. 

Similarly, in the collinear limit considered in appendix C.3, when two adjacent edges of the pentagon contour become parallel, the four-cusp expressions are recovered. Let us denote with δ a small parameter that controls the approach to the soft/collinear limit. In the following, we verify

\(L\)

\(L\)

\(

\)

\(

\)

F

−

−−

→ F

, 

F

−

−−

→ F

, 

\(C.1\)

5

4

5

4

δ→0

δ→0





\(

\)

\(

\)

F

−

−−

→ F

, 

F

−

−−

→ F

\(C.2\)

5

4

5

4

δ→0

δ→0

where L = 1, 2, and we restored an index n = 4, 5 to distinguish between the four-cusp and five-cusp cases. 

In appendix C.1, we explain how we calculate asymptotics of the pentagon functions and apply these results to various singular regimes. In appendix C.4, we show that the negative geometries are finite inside the Euclidean region despite some rational prefactors in their expression having poles. In appendix C.5, we consider the multi-Regge asymptotics inherent to the five-particle scattering amplitudes. 

– 61 –

C.1

Asymptotics of the pentagon functions

We rely on the canonical DE \(B.15\) for the pentagon functions, and apply the method of

\[73, 74\] to calculate its asymptotic solution. Let us briefly summarize the main steps. We assume that the kinematics is parameterized by four variables Y = \(y1, y2, y3, y4\) and δ such that δ → 0 in the singular regime. The asymptotic solution of the DE is governed by the singular terms of its matrix. Thus, we rewrite the alphabet letters in \(δ, Y \) parametrization and series expand the matrix of the DE \(B.15\) at δ → 0, X A\(i\) d log\(Wi\) = B d log\(δ\) \+ dC\(Y \) \+ O\(δ\)

\(C.3\)

i

where B is a matrix with rational number entries and dC\(Y \) is a matrix of dlog forms in Y variables. We recall that both B and dC are nilpotent. Ignoring higher-order terms of the expansion, we omit the power corrections in the asymptotic solution. 

We are looking for an asymptotic solution of the DE in the form of iterated integrals, so we need to choose a reference point Y0. Then we use DiffExp \[60\] to transport the known values ⃗F\(X0\) of the pentagon functions to the point \(δ, Y0\) at δ → 0. Since some of the pentagon functions are singular at δ → 0, we end up with a logarithmic asymptotics, 4

⃗

X

F\(δ, Y0\) =

logp\(δ\)⃗f\(p\) \+ O δ log4\(δ\)

\(C.4\)

p=0

where ⃗f\(p\) are numerical vectors, which we can evaluate with arbitrarily high precision. The leading term of δ-expansion \(C.3\) sums up the singular logarithms in eq. \(C.4\), 

⃗

F\(δ, Y0\) = exp \(log\(δ\)B\)⃗f \+ O δ log4\(δ\)

\(C.5\)

that we use to find numerical vector ⃗f. Eqs. \(C.4\) and \(C.5\) agree, since B is nilpotent. 

Then we use \(C.5\) as the initial condition of the DE and find the asymptotic solution Z Y



⃗

F\(δ, Y \) = exp \(log\(δ\)B\) · Pexp

dC ⃗f \+ O δ log4\(δ\) . 

\(C.6\)

Y0

One can easily see that it satisfies DE \(B.15\) with the right-hand side \(C.3\). The series expansion of the path-ordered exponent Pexp in eq. \(C.6\) is truncated since dC is nilpotent. 

Thus, Pexp in eq. \(C.6\) is a linear combination of the iterated integrals \(5.24\) defined with respect to the reference point Y0. We recall that the first 83 entries of ⃗F are the planar pentagon functions \{fw,a\}, so eq. \(C.6\) provides their logarithmic asymptotics at δ → 0. 

C.2

Soft limit

We provide some details on how we calculate the soft limit p5 → 0 of the pentagon functions and of the negative geometries. We introduce the following parametrization of the kinematics

s

s

s12 =

, 

s23 = sx , 

s34 =

, 

1 \+ 1 \+ z δ

1 \+ z

x

1

2δ

sδ

sxz1z2δ

s45 =

, 

s15 =

. 

\(C.7\)

1 \+ 1 \+ z δ

1 \+ z

\(1 \+ z

x

1

1 \+ 1

x

2δ\)

– 62 –

Namely, instead of five Mandelstam variables, we specify the kinematic configuration by δ

and Y = \(s, x, z1, z2\). Let us note that the square root of the planar pentagon alphabet

√∆5 is rationalized in this parametrization. In the soft limit δ → 0, we reproduce the four-particle kinematics described by two Mandelstam invariants s and sx, s12 → s , 

s23 → sx , 

s34 → s , 

s45 → 0 , 

s15 → 0 . 

\(C.8\)

The parameters z1, z2 specify the directions in which we approach the limit. 

The rational prefactors \{ri\}5 ∪\{r

of the negative geometries are finite in the soft

i=0

i\}5

i=1

limit δ → 0 and simplify as follows, 

r0, r5 → −s2x , 

r2, r3, r1, r4, r5 → 0 , 

r2 → −r4 , 

r3 → −r1 , 

\(C.9\)

and r0, r1, r4 remain linear independent in the limit. 

In order to calculate soft asymptotics of the pentagon functions, we follow appendix C.1. 

The 26-letter planar pentagon alphabet \(5.28\) reduces to a 13-letter alphabet at δ → 0, which contains letter log\(δ\) and 12 letters present in the connection dC\(Y \) \(C.3\). The latter are the four-cusp letters

log\(s\) , log\(x\) , log\(1 \+ x\)

\(C.10\)

as well as nine spurious letters depending on z1 and z2. These spurious letters do appear in the asymptotics of the pentagon functions but they have to cancel out from the negative geometries at δ → 0. 

The reference point X0 \(5.26\) of the pentagon functions takes the following form in parametrization \(C.7\), 



1

√

1 √

1 √



X0 :

δ = 1 , s =

\(1 −

5\) , x =

\( 5 \+ 1\) , z1 = −1 , z2 =

\( 5 − 3\)

. 

\(C.11\)

2

2

2

Relying on DiffExp, we numerically integrate canonical DE \(B.15\) written in variables \(δ, Y \) from X0 \(C.11\) to a point Y0 on the surface δ = 0. This gives us the logarithmic asymptotics of the pentagon functions \(C.4\) at Y = Y0. Then, we factor out powers of log\(δ\) according to \(C.5\) and obtain the soft asymptotics \(C.6\) of the pentagon functions where we neglect power corrections in δ. Namely, the pentagon functions are polynomials in log\(δ\) whose coefficients are the iterated integrals \(5.24\) for the 12-letter alphabet and the reference point Y0. 

Substituting the asymptotics of the pentagon functions to the pure functions of the negative geometries, we find that some of them are O\(δ\), i.e. 

\(1\)

\(1\)

\(2\)

\(2\)

\(2\)

\(2\)

g

, g

, g

, g

, h

, h

→ 0 . 

\(C.12\)

1

4

1

4

1

4

The pure functions \(1\) \(1\)

\(2\)

\(2\)

g

, g

of the one-loop ladder and h , h

of the two-loop ladder

2

3

2

3

are finite and contain single letter log\(x\) in their iterated integral expression at δ → 0. 

Transforming the iterated integrals into logarithmic functions, we confirm that the one-loop and two-loop five-cusp ladders \(4.21\) and \(4.29\) reduce to their four-cusp counterparts

– 63 –

\(D.3\) and \(D.4\) in the soft limit, \(1\)



\(1\)

\(1\)

\(1\)

lim F

= s2x lim g

\+ g

= F

, 

\(C.13\)

5

2

3

4

δ→0

δ→0

\(

\)



\(2\)

\(2\)

\(

\)

lim F

= s2x lim h

\+ h

= F

. 

\(C.14\)

5

2

3

4

δ→0

δ→0

Then we notice that the last term \(4.33\) of the factorized two-loop negative geometry vanishes at δ → 0 in view of \(C.9\) and \(C.12\), 

5

X

\(1\)

\(1\)

ri g

g

→ 0 , 

\(C.15\)

i\+2 i\+3

i=1

and \(1\)

g

cancels out among the first and second term, so we obtain the expected four-cusp 5

expression \(D.5\), 

\(

\)



\(1\)

\(1\)2

\(

\)

lim F

= s2x lim g

\+ g

= F

. 

\(C.16\)

5

2

3

4

δ→0

δ→0

We recall \[17\] how the two-loop correction \(4.22\) reduces to the four-cusp expression in the soft limit due to \(C.9\) and \(C.12\), 

\(2\)



\(2\)

\(2\)

\(2\)

lim F

= −s2x lim g

\+ g

= F

. 

\(C.17\)

5

0

5

4

δ→0

δ→0

Let us note that both \(2\)

\(2\)

g

and g

contain divergent terms logp\(δ\) with p = 1, . . . , 4 and

0

5

spurious letters, but they do cancel out in the sum \(C.17\). 

Finally, the soft limit of the “loop” negative geometry \(4.34\) also reproduces the four-cusp “loop” \(D.6\), 





\(2\)

\(2\)

\(2\)

\(2\)

1 \(1\)

\(1\)2

lim F

= −2s2x lim

g

\+ g

− h

− h

−

g

\+ g

= F

. 

\(C.18\)

5

0

5

2

3

2

3

4

δ→0

δ→0

2

C.3

Collinear limit

In order to consider the collinear limit p4||p5, we find convenient the following parametrization of the kinematics

s

sz

s12 =

, 

s

, 





23 = sx , 

s34 =

1 \+ δ 1 \+ 1 1 \+ δ

1 \+ y\(1 \+ x\)\(1 − z\)δ

x

y

s\(1 \+ x\)δ2

sx\(1 − z\)

s45 =

, 

s

. 

\(C.19\)





15 =

1 \+ δ 1 \+ 1 1 \+ δ

1 \+ y\(1 \+ x\)\(1 − z\)δ

x

y

In the notations of appendix C.1, Y = \(s, x, z, y\) parametrizes the collier configuration δ = 0. Here s and sx are Mandelstam variables of the four-particle kinematics, z is the fraction of the momentum split between p4 and p5, i.e. p4 → zP and p5 → \(1 − z\)P , such that in the collinear limit δ → 0, 

s12 → s , 

s23 → sx , 

s34 → sz , 

s45 → 0 , 

s15 → sx\(1 − z\) , 

\(C.20\)

– 64 –

and y specifies the direction in which we approach the collinear limit. 

The rational prefactors \{ri\}5 ∪ \{r

of the negative geometries either vanish or are

i=0

i\}5

i=1

proportional to the four-cusp rational prefactor s2x, 

r0, r4, r5 → −s2x , 

r2 → s2x , 

r1, r2, r3, r1, r3, r4, r5 → 0 . 

\(C.21\)

In order to calculate the collinear asymptotics of the pentagon functions and pure functions of the negative geometries, we series-expand the planar pentagon alphabet \(5.28\)

at δ → 0. This results in letter log\(δ\) and 10 other letters, which depend on Y and include the four-cusp letters \(C.10\), present in the connection dC\(Y \) \(C.3\). We expect that only letters log\(x\), log\(1 \+ x\) remain in the expressions for the negative geometries at δ → 0. 

Then we employ the boundary values ⃗F\(δ, Y0\) in the collinear limit δ → 0 choosing somehow Y0. Namely, we use DiffExp to transport numerically the boundary values ⃗

F\(X0\) of DE

\(B.15\) at X0 \(5.26\), which has the following form in parametrization \(C.19\), 



1 √

1

√

1 √

1 √



X0 :

δ =

\( 5 − 1\) , s =

\(1 −

5\) , x =

\( 5 \+ 1\) , y = −1 , z =

\( 5 − 1\)

, 

2

2

2

2

\(C.22\)

to the kinematic point \(δ → 0, Y0\). In this way, eq. \(C.6\) provides the collinear asymptotics of the pentagon functions as iterated integrals with the reference point Y0. 

Taking into account the collinear limit of the rational prefactors \(C.21\), we conclude that the pure functions \(1\)

\(2\)

g

and h

with i = 1, 2, 3 contribute to the ladders, see \(4.21\)

i

i

and \(4.29\). Individually, these pure functions contain powers of the divergent logarithm log\(δ\) and spurious letters, but their sum is finite and reproduces the four-cusp ladders

\(D.3\) and \(D.4\), 

\(1\)



\(1\)

\(1\)

\(1\)

\(1\)

lim F

= s2x lim g

\+ g

\+ g

= F

, 

\(C.23\)

5

1

2

3

4

δ→0

δ→0

\(

\)



\(2\)

\(2\)

\(2\)

\(

\)

lim F

= s2x lim h

\+ h

\+ h

= F

. 

\(C.24\)

5

1

2

3

4

δ→0

δ→0

Owing to \(C.21\), the pure functions \(1\)

\(1\)

g

and g

drop out in the collinear limit from

4

5

the factorized two-loop five-cusp negative geometry

\(4.33\), 

\(

\)



\(1\)

\(1\)

\(1\)2

\(

\)

lim F

= s2x lim g

\+ g

\+ g

= F

. 

\(C.25\)

5

1

2

3

4

δ→0

δ→0

Finally, we obtain the collinear limit of the two-loop five-cusp correction \(2\) F

\(4.22\) and of

5

the “loop” negative geometry \(4.34\), 

\(2\)



\(2\)

\(2\)

\(2\)

\(2\)

lim F

= −s2x lim g

\+ g

\+ g

= F

, 

\(C.26\)

5

0

4

5

4

δ→0

δ→0





\(2\)

\(2\)

\(2\)

\(2\)

\(2\)

\(2\)

lim F

= −2s2x lim g

\+ g

\+ g

− h

− h

− h

5

0

4

5

1

2

3

δ→0

δ→0





1 

2 

−

\(1\)

\(1\)

\(1\)

g

\+ g

\+ g

= F

, 

\(C.27\)

2

1

2

3

4

where individual pure terms \(2\) \(2\) \(2\)

g

, g , g

contain powers of the divergent logarithm log\(δ\)

0

4

5

and spurious letters, which cancel out in the sum. 

– 65 –

C.4

Absence of spurious singularities

We expect the negative geometries to be smooth inside inside the Euclidean region. For example, the two-loop ladder integrand \(4.25\) does not have singularities in the Euclidean region. However, this property is not manifest in the representations \(4.28\), \(4.29\), \(4.33\), 

\(4.34\) of the integrated negative geometries. The planar pentagon functions are smooth in the Euclidean region \[40\], but the prefactors \{ri\}5 ∪ \{r

\(4.6\) become singular

i=0

i\}5

i=1

inside the Euclidean region. Indeed, the rational prefactor ri with i = 1, . . . , 5 has a pole at si\+1,i\+4 = 0, and ri with i = 1, . . . , 5 has poles at si\+1i\+3 = 0 and si\+2i\+4 = 0, see eqs. \(4.8\) and \(4.9\). In other words, the rational prefactors in the expression of the negative geometries have simple poles at zero loci of nonadjacent Mandelstam variables, sij = 0. 

We verify that the poles of the rational prefactors are suppressed by the accompanying pure functions. Using explicit polylogarithmic expression \(4.31\) for the one-loop pure functions \{ \(1\)

g

\}5 , it is easy to see

i

i=1

\(1\)

g

\(s

i

i\+1 i\+4 = 0\) = 0 , 

\(C.28\)

so the term

\(1\)

\(1\)

\(1\)

ri g

is finite in the Euclidean region. In the same way, g

and g

suppress

i

i\+2

i\+3

poles of \{

\(1\)

\(1\)

ri\}5

at s

g

of

i=1

i\+1 i\+3 = 0 and si\+2 i\+4 = 0, respectively, and the term ri gi\+2 i\+3

\(4.33\) is finite in the Euclidean region. 

A more nontrivial calculation is required at the two-loop order in order to verify suppression of the poles of \{ri\}5 by the pure functions in eqs. \(4.29\) and \(4.34\). We rely on i=1

the approach of appendix C.1. For example, for i = 1, we choose s25 = δ and Y a complementing set of four independent Mandelstam variables. We choose Y0 inside the Euclidean region, so ⃗F\(δ, Y0\) is finite at δ → 0, see \(C.4\), and ⃗F\(δ = 0, Y0\) = ⃗f, see \(C.5\). Using the iterated integral expression \(C.6\) for the pentagon functions at s25 = 0, we verify that \(2\)

\(2\)

g

\(s

\(s

1

25 = 0\) = h1

25 = 0\) = 0 . 

\(C.29\)

Thus, we have explicitly checked that all two-loop iterated negative geometries are free from unphysical poles in the Euclidean region. 

C.5

Multi-Regge limit

Another interesting asymptotic regime of the five-particle scattering is the multi-Regge kinematics. This is the high-energy scattering regime where the rapidities of the final state particles are strongly ordered and their transverse momenta are comparable. For the process 12 → 345, it is common to reach the multi-Regge regime using the following parametrization with δ → 0, 

s1s2

s1

s2

s12 =

, 

s23 = −z1z2κ , 

s34 =

, 

s45 =

, 

s15 = −\(1 − z1\)\(1 − z2\)κ , 

κδ2

δ

δ

\(C.30\)

However, instead of the three-particle production channel, we study the negative geometries in the Euclidean region with all adjacent Mandelstam invariants being positive. So we have to impose z1 > 1 and z2 < 0 or z1 < 0 and z2 > 1, and s1, s2, κ, δ > 0. 

– 66 –

In the multi-Regge limit δ → 0, the rational prefactors \{ri\}5 ∪\{r of the negative

i=0

i\}5

i=1

geometries are divergent. r0 and r4 are the most singular. We keep them and omit the remaining rational prefactors which would provide power corrections to the leading term, r0, r4 = −s1s2z1\(1 − z2\)δ−2 \+ O\(δ−1\) , 

r1, r2, r3, r5, r1 . . . , r5 = O\(δ−1\) . 

\(C.31\)

Here and in the following we assume the Euclidean region with z1 > 1 and z2 < 0. 

Then we normalize the negative geometries by the Born-level F \(0\) \(4.20\) and obtain the following expressions at one-loop level, see eq. \(4.28\), 

F \(

\)

X

\(1\)

= −

g

\+ O δ log2\(δ\) , 

\(C.32\)

F \(0\)

i

i=1,2,3,5

and at two-loop level, see eqs. \(4.29\), \(4.33\) and \(4.34\), 

F \(

\)

X

\(2\)

= −

h

\+ O\(δ log4\(δ\)\) , 

\(C.33\)

F \(0\)

i

i=1,2,3,5



2

F \(

\)

X

\(1\)

= − 

g



\+ O\(δ log4\(δ\)\) , 

\(C.34\)

F \(0\)

i

i=1,2,3,5







2

F



\(2\)

\(2\)

X

\(2\)

X

\(1\)

= 2 g

\+ g

− 2

h

− 

g



\+ O\(δ log4\(δ\)\) . 

\(C.35\)

F \(0\)

0

4

i

i

i=1,2,3,5

i=1,2,3,5

Then we apply the approach of appendix C.1 to calculate the multi-Regge asymptotics of the pentagon functions and of the pure functions from the previous equations. The planar pentagon alphabet \(5.28\) simplifies to 11 letters in the multi-Regge limit δ → 0 which are split into four alphabets depending on the nonoverlapping set of variables. Namely, letter log\(δ\) as well as ten letters, 

\{κ\} , \{s1, s2, s1 \+ s2\}, \{z1, 1 − z1, z2, 1 − z2, z1 − z2, 1 − z1 − z2\} . 

\(C.36\)

figuring in the connection dC\(Y \) \(C.3\). Let us mention that despite the set of five parameters Y = \(s1, s2, z1, z2, κ\) is redundant, the calculation procedure outlined appendix C.1

stays the same. Then, we numerically integrate canonical DE \(B.15\) and transport its boundary values at X0 in the parametrization \(C.30\), 



1

√

1

√ 

X0 =

δ = 1 , s1 = −1 , s2 = −1 , κ = −1 , z1 =

\(1 \+

5\) , z2 =

\(1 −

5\)

\(C.37\)

2

2

to a point \(δ → 0, Y0\). Eq. \(C.6\) provides the logarithmic asymptotics of the pentagon functions in the multi-Regge limit. Substituting the asymptotics in eqs. \(C.32\) to \(C.35\)

we find

2ℓ\(g\)

F \(g\)

X

\(g\)





=

q

\(z1, z2, s1, s2, κ\) logk\(δ\) \+ O δ log2ℓ\(g\)\(δ\)

\(C.38\)

F \(0\)

k

k=0

– 67 –

where

g ∈ \{

, 

, 

, 

\}

\(C.39\)

labels the negative geometries and ℓ\(g\) counts their loop order \(number of black blobs\). 

The pure functions \(g\)

q

are iterated integrals over the alphabet \(C.36\) with the reference k

point Y0. 

The functions \(g\)

q

\(C.38\) are expressible in terms of the classical polylogarithms. They k

are graded UT polynomials of the transcendental weight \(2ℓ\(g\) − k\) in the logarithms s1 

s2 

log

, log

, log\(−z1z2\) , log \(\(z1 − 1\)\(1 − z2\)\) , 

\(C.40\)

κ

κ

transcendental constants π2, ζ3, and a weight-3 UT combination of the dilogarithms and trilogarithms. We refrain from typing in here its explicit expression. The explicit expressions for \(g\)

q

are provided in the ancillary files. 

k

Let us note that this weight-3 polylogarithmic combination appears in the two-loop \(

\)

ladder \(

\)

q

and “loop” q

negative geometries with k = 3, 4. However, it cancels out

k

k

in the two-loop negative-geometry decomposition \(2.20\), 





1

1

− \(

\)

\(

\)

q

− q

\+

q

\(C.41\)

k

2 k

2 k

which involves only logarithms \(C.40\) and constants π2, ζ3. In other words, the negative geometries, including the two-loop ladder, have a more complicated form than the two-loop correction F \(2\) in the multi-Regge limit. 

D

Four-cusp negative geometries

In this Appendix, we summarise perturbative results up to the two-loop order for the Lagrangian insertion in the four-cusp Wilson loop, \(L\)

F

with L = 0, 1, 2 in eq. \(2.4\), and

4

for the corresponding negative geometries \[20\]. 

The loop corrections are harmonic polylogarithms of the dual conformal cross-ratio, x2 x2 x2

x :=

20 40 13 . 

\(D.1\)

x2 x2 x2

10 30 24

They are proportional to the unique leading singularity given by the Born-level approximation, 

\(0\)

x2 x2

F

\(x

13 24

, 

\(D.2\)

4

0; x1, . . . , x4\) = − x2 x2 x2 x2

10 20 30 40

– 68 –

and have the following form

\(1\)

\(0\)

\(

\)

\(0\)

F

/F

= F

/F

= − log2\(x\) \+ π2 , 

\(D.3\)

4

4

4

4

\(

\)

\(0\)

1

F

/F

= − π2 \+ log2\(x\) 5π2 \+ log2\(x\) , 

\(D.4\)

4

4

6

\(

\)

\(0\)

1

F

/F

= − π2 \+ log2\(x\)2 , 

\(D.5\)

4

4

6





\(0\)

F

/F

= −8H

4

4

0,0,0,0 − 8H-1,0,0,0 \+ 16H-1,-1,0,0 − 8H-2,0,0 \+ 8ζ3 \(2H−1 − H0\)

13π4

− 4π2 \(H-1,0 − 2 H-1,-1 \+ H−2\) −

, 

\(D.6\)

45

where H are the harmonic polylogarithms of argument x \[75\]. The expression for the two-loop correction \(2\)

F

follows from the two-loop negative geometry decomposition \(2.20\), 

4





\(2\)

\(

\)

1

\(

\)

1

F

= −F

− F

\+

F

. 

\(D.7\)

4

4

2 4

2 4

In the frame x0 → ∞, the kinematics is that of the four-particle scattering, see eq. \(4.19\), 

t

\(0\)

x →

, 

lim \(x2

= −st , 

\(D.8\)

s

0\)4F

x

4

0→∞

where t = x2 and s = x2 . 

13

24

References

\[1\] N. Arkani-Hamed, L. J. Dixon, A. J. McLeod, M. Spradlin, J. Trnka and A. Volovich, Solving Scattering in N = 4 Super-Yang-Mills Theory, 2207.10636. 

\[2\] G. Travaglini et al., The SAGEX review on scattering amplitudes, J. Phys. A 55 \(2022\)

443001 \[2203.13011\]. 

\[3\] A. Hodges, Eliminating spurious poles from gauge-theoretic amplitudes, JHEP 05 \(2013\) 135

\[0905.1473\]. 

\[4\] N. Arkani-Hamed and J. Trnka, The Amplituhedron, JHEP 10 \(2014\) 030 \[1312.2007\]. 

\[5\] R. Britto, F. Cachazo, B. Feng and E. Witten, Direct proof of tree-level recursion relation in Yang-Mills theory, Phys. Rev. Lett. 94 \(2005\) 181602 \[hep-th/0501052\]. 

\[6\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. Hodges and J. Trnka, A Note on Polytopes for Scattering Amplitudes, JHEP 04 \(2012\) 081 \[1012.6030\]. 

\[7\] N. Arkani-Hamed, A. Hodges and J. Trnka, Positive Amplitudes In The Amplituhedron, 

JHEP 08 \(2015\) 030 \[1412.8478\]. 

\[8\] E. Herrmann, C. Langer, J. Trnka and M. Zheng, Positive Geometries for One-Loop Chiral Octagons, 2007.12191. 

\[9\] E. Herrmann, C. Langer, J. Trnka and M. Zheng, Positive geometry, local triangulations, and the dual of the Amplituhedron, JHEP 01 \(2021\) 035 \[2009.05607\]. 

\[10\] L. F. Alday, E. I. Buchbinder and A. A. Tseytlin, Correlation function of null polygonal Wilson loops with local operators, JHEP 09 \(2011\) 034 \[1107.5702\]. 

– 69 –

\[11\] O. T. Engelund and R. Roiban, On correlation functions of Wilson loops, local and non-local operators, JHEP 05 \(2012\) 158 \[1110.0758\]. 

\[12\] O. T. Engelund and R. Roiban, Correlation functions of local composite operators from generalized unitarity, JHEP 03 \(2013\) 172 \[1209.0227\]. 

\[13\] L. F. Alday, P. Heslop and J. Sikorowski, Perturbative correlation functions of null Wilson loops and local operators, JHEP 03 \(2013\) 074 \[1207.4316\]. 

\[14\] L. F. Alday, J. M. Henn and J. Sikorowski, Higher loop mixed correlators in N=4 SYM, 

JHEP 03 \(2013\) 058 \[1301.0149\]. 

\[15\] J. M. Henn, G. P. Korchemsky and B. Mistlberger, The full four-loop cusp anomalous dimension in N = 4 super Yang-Mills and QCD, JHEP 04 \(2020\) 018 \[1911.10174\]. 

\[16\] D. Chicherin and J. M. Henn, Symmetry properties of Wilson loops with a Lagrangian insertion, JHEP 07 \(2022\) 057 \[2202.05596\]. 

\[17\] D. Chicherin and J. Henn, Pentagon Wilson loop with Lagrangian insertion at two loops in N = 4 super Yang-Mills theory, JHEP 07 \(2022\) 038 \[2204.00329\]. 

\[18\] J. M. Drummond, J. M. Henn and J. Plefka, Yangian symmetry of scattering amplitudes in N=4 super Yang-Mills theory, JHEP 05 \(2009\) 046 \[0902.2987\]. 

\[19\] L. J. Dixon, M. von Hippel, A. J. McLeod and J. Trnka, Multi-loop positivity of the planar N

= 4 SYM six-point amplitude, JHEP 02 \(2017\) 112 \[1611.08325\]. 

\[20\] N. Arkani-Hamed, J. Henn and J. Trnka, Nonperturbative negative geometries: amplitudes at strong coupling and the amplituhedron, JHEP 03 \(2022\) 108 \[2112.06956\]. 

\[21\] J. M. Drummond, J. M. Henn and J. Trnka, New differential equations for on-shell loop integrals, JHEP 04 \(2011\) 083 \[1010.3679\]. 

\[22\] T. V. Brown, U. Oktem, S. Paranjape and J. Trnka, Loops of loops expansion in the amplituhedron, JHEP 07 \(2024\) 025 \[2312.17736\]. 

\[23\] I. A. Korchemskaya and G. P. Korchemsky, On lightlike Wilson loops, Phys. Lett. B 287

\(1992\) 169. 

\[24\] J. M. Drummond, G. P. Korchemsky and E. Sokatchev, Conformal properties of four-gluon planar amplitudes and Wilson loops, Nucl. Phys. B 795 \(2008\) 385 \[0707.0243\]. 

\[25\] L. F. Alday and J. M. Maldacena, Gluon scattering amplitudes at strong coupling, JHEP 06

\(2007\) 064 \[0705.0303\]. 

\[26\] A. Brandhuber, P. Heslop and G. Travaglini, MHV amplitudes in N=4 super Yang-Mills and Wilson loops, Nucl. Phys. B 794 \(2008\) 231 \[0707.1153\]. 

\[27\] B. Eden, C. Schubert and E. Sokatchev, Three loop four point correlator in N=4 SYM, Phys. 

Lett. B 482 \(2000\) 309 \[hep-th/0003096\]. 

\[28\] N. Arkani-Hamed, H. Thomas and J. Trnka, Unwinding the Amplituhedron in Binary, JHEP

01 \(2018\) 016 \[1704.05069\]. 

\[29\] L. Dixon, U. Oktem, S. Paranjape and J. Trnka, In preparation, . 

\[30\] T. Brown, J. M. Henn, E. Mazzucchelli and J. Trnka, In preparation, . 

\[31\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo and J. Trnka, Local Integrals for Planar Scattering Amplitudes, JHEP 06 \(2012\) 125 \[1012.6032\]. 

– 70 –

\[32\] J. L. Bourjaily, S. Caron-Huot and J. Trnka, Dual-Conformal Regularization of Infrared Loop Divergences and the Chiral Box Expansion, JHEP 01 \(2015\) 001 \[1303.4734\]. 

\[33\] J. L. Bourjaily and J. Trnka, Local Integrand Representations of All Two-Loop Amplitudes in Planar SYM, JHEP 08 \(2015\) 119 \[1505.05886\]. 

\[34\] J. L. Bourjaily, E. Herrmann and J. Trnka, Prescriptive Unitarity, JHEP 06 \(2017\) 059

\[1704.05460\]. 

\[35\] J. L. Bourjaily, E. Herrmann, C. Langer, A. J. McLeod and J. Trnka, Prescriptive Unitarity for Non-Planar Six-Particle Amplitudes at Two Loops, JHEP 12 \(2019\) 073 \[1909.09131\]. 

\[36\] J. L. Bourjaily, E. Herrmann, C. Langer and J. Trnka, Building bases of loop integrands, 

JHEP 11 \(2020\) 116 \[2007.13905\]. 

\[37\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, S. Caron-Huot and J. Trnka, The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM, JHEP 01 \(2011\) 041 \[1008.2958\]. 

\[38\] S. Badger, D. Chicherin, T. Gehrmann, G. Heinrich, J. M. Henn, T. Peraro et al., Analytic form of the full two-loop five-gluon all-plus helicity amplitude, Phys. Rev. Lett. 123 \(2019\)

071601 \[1905.03733\]. 

\[39\] J. Henn, B. Power and S. Zoia, Conformal Invariance of the One-Loop All-Plus Helicity Scattering Amplitudes, JHEP 02 \(2020\) 019 \[1911.12142\]. 

\[40\] T. Gehrmann, J. M. Henn and N. A. Lo Presti, Pentagon functions for massless planar scattering amplitudes, JHEP 10 \(2018\) 103 \[1807.09812\]. 

\[41\] D. Chicherin and V. Sotnikov, Pentagon Functions for Scattering of Five Massless Particles, 

JHEP 20 \(2020\) 167 \[2009.07803\]. 

\[42\] T. Gehrmann, J. M. Henn and N. A. Lo Presti, Analytic form of the two-loop planar five-gluon all-plus-helicity amplitude in QCD, Phys. Rev. Lett. 116 \(2016\) 062001

\[1511.05409\]. 

\[43\] J. M. Henn, Multiloop integrals in dimensional regularization made simple, Phys. Rev. Lett. 

110 \(2013\) 251601 \[1304.1806\]. 

\[44\] J. M. Henn, Lectures on differential equations for Feynman integrals, J. Phys. A 48 \(2015\)

153001 \[1412.2296\]. 

\[45\] F. V. Tkachov, A theorem on analytical calculability of 4-loop renormalization group functions, Phys. Lett. B 100 \(1981\) 65. 

\[46\] K. G. Chetyrkin and F. V. Tkachov, Integration by parts: The algorithm to calculate β-functions in 4 loops, Nucl. Phys. B 192 \(1981\) 159. 

\[47\] R. N. Lee, Presenting LiteRed: a tool for the Loop InTEgrals REDuction, 1212.2685. 

\[48\] R. N. Lee, LiteRed 1.4: a powerful tool for reduction of multiloop integrals, J. Phys. Conf. 

Ser. 523 \(2014\) 012059 \[1310.1145\]. 

\[49\] A. V. Smirnov and F. S. Chuharev, FIRE6: Feynman Integral REduction with Modular Arithmetic, Comput. Phys. Commun. 247 \(2020\) 106877 \[1901.07808\]. 

\[50\] J. M. Henn, K. Melnikov and V. A. Smirnov, Two-loop planar master integrals for the production of off-shell vector bosons in hadron collisions, JHEP 05 \(2014\) 090 \[1402.7078\]. 

\[51\] J. Henn, B. Mistlberger, V. A. Smirnov and P. Wasser, Constructing d-log integrands and

– 71 –

computing master integrals for three-loop four-particle scattering, JHEP 04 \(2020\) 167

\[2002.09492\]. 

\[52\] K.-T. Chen, Iterated path integrals, Bull. Am. Math. Soc. 83 \(1977\) 831. 

\[53\] X. Liu and Y.-Q. Ma, AMFlow: A Mathematica package for Feynman integrals computation via auxiliary mass flow, Comput. Phys. Commun. 283 \(2023\) 108565 \[2201.11669\]. 

\[54\] A. B. Goncharov, M. Spradlin, C. Vergu and A. Volovich, Classical Polylogarithms for Amplitudes and Wilson Loops, Phys. Rev. Lett. 105 \(2010\) 151605 \[1006.5703\]. 

\[55\] D. Chicherin, J. Henn and V. Mitev, Bootstrapping pentagon functions, JHEP 05 \(2018\) 164

\[1712.09610\]. 

\[56\] C. Fevola, S. Mizera and S. Telen, Landau Singularities Revisited: Computational Algebraic Geometry for Feynman Integrals, Phys. Rev. Lett. 132 \(2024\) 101601 \[2311.14669\]. 

\[57\] C. Fevola, S. Mizera and S. Telen, Principal Landau determinants, Comput. Phys. Commun. 

303 \(2024\) 109278 \[2311.16219\]. 

\[58\] X. Jiang, J. Liu, X. Xu and L. L. Yang, Symbol letters of Feynman integrals from Gram determinants, 2401.07632. 

\[59\] T. Peraro, FiniteFlow: multivariate functional reconstruction using finite fields and dataflow graphs, JHEP 07 \(2019\) 031 \[1905.08019\]. 

\[60\] M. Hidding, DiffExp, a Mathematica package for computing Feynman integrals in terms of one-dimensional series expansions, Comput. Phys. Commun. 269 \(2021\) 108125

\[2006.05510\]. 

\[61\] D. Chicherin, J. M. Henn, E. Mazzucchelli, J. Trnka, Q. Yang and S.-Q. Zhang, In preparation, . 

\[62\] J. Henn and P. Raman, Positivity properties of scattering amplitudes, 2407.05755. 

\[63\] J. M. Henn, A. Matijašić, J. Miczajka, T. Peraro, Y. Xu and Y. Zhang, A computation of two-loop six-point Feynman integrals in dimensional regularization, JHEP 08 \(2024\) 027

\[2403.19742\]. 

\[64\] S. Abreu, D. Chicherin, V. Sotnikov and S. Zoia, Two-Loop Five-Point Two-Mass Planar Integrals and Double Lagrangian Insertions in a Wilson Loop, 2408.05201. 

\[65\] J. M. Henn, M. Lagares and S.-Q. Zhang, Integrated negative geometries in ABJM, JHEP 05

\(2023\) 112 \[2303.02996\]. 

\[66\] S. He, C.-K. Kuo, Z. Li and Y.-Q. Zhang, Emergent unitarity, all-loop cuts and integrations from the ABJM amplituhedron, JHEP 07 \(2023\) 212 \[2303.03035\]. 

\[67\] M. Lagares and S.-Q. Zhang, Higher-loop integrated negative geometries in ABJM, JHEP 05

\(2024\) 142 \[2402.17432\]. 

\[68\] Z. Li, Integrating the full four-loop negative geometries and all-loop ladder-type negative geometries in ABJM theory, 2402.17023. 

\[69\] S. Abreu, L. J. Dixon, E. Herrmann, B. Page and M. Zeng, The two-loop five-point amplitude in N = 4 super-Yang-Mills theory, Phys. Rev. Lett. 122 \(2019\) 121603 \[1812.08941\]. 

\[70\] D. Chicherin, T. Gehrmann, J. M. Henn, P. Wasser, Y. Zhang and S. Zoia, Analytic result for a two-loop five-particle amplitude, Phys. Rev. Lett. 122 \(2019\) 121602 \[1812.11057\]. 

– 72 –

\[71\] D. Chicherin, T. Gehrmann, J. M. Henn, P. Wasser, Y. Zhang and S. Zoia, The two-loop five-particle amplitude in N = 8 supergravity, JHEP 03 \(2019\) 115 \[1901.05932\]. 

\[72\] S. Abreu, L. J. Dixon, E. Herrmann, B. Page and M. Zeng, The two-loop five-point amplitude in N = 8 supergravity, JHEP 03 \(2019\) 123 \[1901.08563\]. 

\[73\] S. Caron-Huot, D. Chicherin, J. Henn, Y. Zhang and S. Zoia, Multi-Regge Limit of the Two-Loop Five-Point Amplitudes in N = 4 Super Yang-Mills and N = 8 Supergravity, JHEP

10 \(2020\) 188 \[2003.03120\]. 

\[74\] W. Wasow, Asymptotic expansions for ordinary differential equations, Pure and Applied Mathematics, Vol. XIV. Interscience Publishers John Wiley & Sons, Inc., New York-London-Sydney, 1965. 

\[75\] E. Remiddi and J. A. M. Vermaseren, Harmonic polylogarithms, Int. J. Mod. Phys. A 15

\(2000\) 725 \[hep-ph/9905237\]. 

– 73 –


# Document Outline

+ Introduction 
+ Two-loop negative geometry decomposition of the Lagrangian insertion in the Wilson loop 
+ Momentum-twistor integrands for the negative geometries 
+ Integrated negative geometries in five-particle kinematics 
+ Two-loop nonplanar Feynman integrals for the negative geometries 
+ Results for integrated negative geometries and positivity properties 
+ d'Alembertian differential equation for the ladder-type geometries 
+ Symbol bootstrap of the ladder-type negative geometries 
+ Summary and discussion 
+ Two-loop alphabet letters 
+ Pentagon functions 
+ Soft, collinear, and multi-Regge limits 
+ Four-cusp negative geometries



