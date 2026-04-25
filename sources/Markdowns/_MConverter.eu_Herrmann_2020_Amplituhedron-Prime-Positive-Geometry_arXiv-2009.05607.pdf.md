Prepared for submission to JHEP

Positive geometry, local triangulations, and

the dual of the Amplituhedron

Enrico Herrmann,1 Cameron Langer,2,3 Jaroslav Trnka,2 Minshan Zheng,2

1 SLAC National Accelerator Laboratory, Stanford University, Stanford, CA 94039, USA 2 Center for Quantum Mathematics and Physics \(QMAP\), 

Department of Physics, University of California, Davis, CA 95616, USA

3 Institute for Gravitation and the Cosmos, Department of Physics, 

Pennsylvania State University, University Park, PA 16892, USA

E-mail: eh10@stanford.edu, cklanger@ucdavis.edu, 

trnka@ucdavis.edu,mszheng@ucdavis.edu

Abstract: We initiate the systematic study of local positive spaces which arise in the context of the Amplituhedron construction for scattering amplitudes in planar maximally supersymmetric Yang-Mills theory. We show that all local positive spaces relevant for one-loop MHV amplitudes are characterized by certain sign-flip conditions and are associated with surprisingly simple logarithmic forms. In the maximal sign-flip case they are finite one-loop octagons. Particular combinations of sign-flip spaces can be glued into new local positive geometries. These correspond to local pentagon integrands that appear in the local expansion of the MHV one-loop amplitude. We show that, geometrically, these pentagons do not triangulate the original Amplituhedron space but rather its twin “Amplituhedron-Prime.” This new geometry has the same boundary structure as the Amplituhedron \(and therefore the same logarithmic form\) arXiv:2009.05607v1 \[hep-th\] 11 Sep 2020

but differs in the bulk as a geometric space. On certain two-dimensional boundaries, where the Amplituhedron geometry reduces to a polygon, we check that both spaces map to the same dual polygon. Interestingly, we find that the pentagons internally triangulate that dual space. This gives a direct evidence that the chiral pentagons are natural building blocks for a yet-to-be discovered dual Amplituhedron. 

Contents

1

Introduction

2

2

Amplituhedron geometry

4

2.1

Topological sign-flip definition of the Amplituhedron

7

2.2

One-loop MHV and MHV spaces

9

2.3

Boundaries of MHV amplitudes

10

2.4

Positivity and the dual Amplituhedron

18

3

Geometry of d log forms

21

3.1

d log forms for pentagon integrands

22

3.2

From d log’s to geometry

25

3.3

No-go theorem for external triangulation

33

4

Sign-flip regions

35

5

Local geometries and the Amplituhedron-Prime

45

5.1

Chiral regions for boxes and pentagons

46

5.2

Two-dimensional projections

49

5.3

Gluing regions

54

5.4

Amplituhedron-Prime

60

6

Triangulation of the dual Amplituhedron

67

6.1

Dualizing polygons

67

6.2

Dual spaces of chiral pentagons

70

6.3

Two-dimensional triangulations

73

7

Conclusion

80

A Configuration of lines in momentum twistor space

82

B External triangulations

86

C Fixed signs in sign-flip-zero, two and four spaces

98

D Gluing local geometries from two-dimensional projections

103

– 1 –

1

Introduction

The Amplituhedron \[1\] is a geometric object encapsulating the tree-level amplitudes and all-loop integrands of planar maximally supersymmetric Yang-Mills theory \(N =4

sYM\) \[2, 3\]. It is a particular example of a positive geometry \[4\] and is defined as a certain geometric region in the space of positive external data. Another example of a positive geometry is the Associahedron \[5\], which is relevant for φ3 amplitudes and is also connected to cluster polytopes and string amplitudes \[6, 7\]. For a review of these geometric ideas, see \[8\], and for attempts to include other interactions and matter, c.f. \[9–13\]. Recent advances have also uncovered positive geometries in conformal field theory correlation functions \[14\] and in cosmology \[15–17\]. 

The original definition of the Amplituhedron \[1\] involved an auxiliary kinematic space. In contrast, the more recent reformulation of the Amplituhedron defines the geometry directly in momentum-twistor space \[18\] using certain sign-flip conditions

\[19\] on sequences of twistor invariants. In this geometric setup, amplitudes correspond to differential forms defined by the property of having logarithmic singularities on all boundaries of the Amplituhedron. All physical properties of scattering amplitudes, such as unitarity and locality, are consequences of the Amplituhedron geometry \[20, 21\]. 

While there is no direct derivation of this geometric construction from first principles of quantum field theory, by now we have ample evidence for the relation between the Amplituhedron geometry and scattering amplitudes. In particular, one can explicitly compute the differential forms by triangulating the Amplituhedron and comparing them to existing tree-level amplitudes and loop integrands available in the literature

\[19, 22–24\]. The geometric picture has also been used to obtain a large amount of all-loop data \[20, 25, 26\] not currently accessible by any conventional amplitude methods. In parallel, there has also been significant progress trying to understand more formal aspects of the Amplituhedron, including its boundary and combinatorial structure \[27–31\], the connection to symbol alphabets, properties of final amplitudes \(rather than integrands\) \[32–35\], and many others \(see e.g., \[36–40\]\). Despite this progress, there are many open questions, including the determination of the all-loop four-point integrand \(see recent progress \[20, 41, 42\]\). 

The Amplituhedron arises as a generalization of the positive Grassmannian \[43–48\]

which appears in the context of on-shell diagrams and all-loop recursion relations \[49\]

in planar N = 4 sYM. Despite their origin in maximally supersymmetric Yang-Mills theory, on-shell diagrams and the associated construction in the Grassmannian can be defined in various other theories \[48, 50–56\]. This naturally leads to the question whether or not Amplituhedron-like structures also exist more generally. Even within N = 4 sYM theory, the striking similarity of the analytic structure of planar and non-

– 2 –

planar integrands \[57–59\], and the natural non-planar extension of on-shell diagrams

\[60–62\] suggests that an Amplituhedron-like object should exist for N = 4 sYM amplitudes beyond the planar limit. A crucial first step in this direction has been achieved at tree-level by formulating the geometry of the Amplituhedron directly in momentum space \[63, 64\]. The momentum space formulation seems crucial beyond the planar limit, since we no longer have access to momentum-twistor variables \[18\] which are at the heart of the kinematic space underlying the original Amplituhedron. At loop-level, the main obstruction is the non-uniqueness of the non-planar loop momentum, although recent works \[65, 66\] suggest possible paths to remedy this situation. 

In this paper, we revisit one major open question central to Amplituhedron research. In particular, we investigate the rôle of “local triangulations” of the Amplituhedron and their relation to a putative dual Amplituhedron space. The original idea of interpreting scattering amplitudes as volumes appeared in the work of Andrew Hodges \[18\] where the original momentum twistor space formulation for planar N = 4

sYM amplitudes was defined. In \[18\], the six-point NMHV tree-level amplitude is given by the volume of a certain polyhedron in dual momentum-twistor space and the BCFW

expansion of the amplitude \[67, 68\] was interpreted as a particular triangulation of this volume. This picture was later extended to all NMHV tree-level amplitudes \[69\]. In contrast, higher k tree-level amplitudes and loop integrands have not as of yet been directly identified as volumes. Instead, the Amplituhedron is defined in momentum twistor space, where tree-level amplitudes and all-loop integrands are differential forms rather than volumes. The existence of a dual Amplituhedron where amplitudes are interpreted as literal volumes is a very natural and important open problem. Nontrivial evidence for the existence of such a dual picture was given in \[4, 70, 71\]. In particular, it was shown for many examples that both tree-level amplitudes and loop integrands are positive when evaluated inside the Amplituhedron, which is reminiscent of the volume positivity. Interestingly, this property also seems to hold for some IR

safe quantities post integration \[35\]. Here, we make a further major step in this direction. In particular, we show that the local expansion of the one-loop MHV amplitudes in terms of chiral pentagon integrals \[72\] can be naturally interpreted as the internal triangulation of the putative dual Amplituhedron. We make this statement precise on two-dimensional boundaries of the full geometry, where the space reduces to polygons and the dualization procedure is well-defined. Our main tool is the reformulation of the Amplituhedron using sign flips \[19\]. In the process of interpreting the chiral pentagons geometrically, we introduce more general positive spaces defined by sign-flip conditions. 

Surprisingly, the logarithmic forms of the maximal sign-flip spaces are chiral octagons, originally introduced in \[72\] as local building blocks for one-loop integrands. 

– 3 –

Our paper is organized as follows: In section 2, we introduce the Amplituhedron geometry and then focus on the MHV one-loop case, where we discuss the projective geometry of lines in

3

P and the positions of physical and unphysical singularities. We

also pose the question of the rôle of the chiral pentagon expansion in the context of the dual Amplituhedron. In sections 3 and 4, we discuss how to associate a geometric space to a d log form and classify all such one-loop geometries. We show that the set of these one-loop spaces is bounded by the number of sign flips in the propagator space, and we determine the logarithmic forms for all of these spaces. In section 5, we discuss the geometry of chiral pentagons in detail and show that they naturally triangulate a different positive space which we call the Amplituhedron-Prime. This space has an identical boundary structure as the original Amplituhedron and therefore corresponds to the same logarithmic form. 

In section 6, we show that on all two-dimensional

boundaries both spaces map under dualization to the same geometry, and the chiral pentagons internally triangulate this dual Amplituhedron space. We finally conclude with some future directions in section 7. Various technical details are covered in four appendices. 

2

Amplituhedron geometry

Momentum twistors and the Amplituhedron’s kinematic space

Scattering amplitudes in planar N = 4 sYM are naturally described in momentum twistor space \[18\]. Since the same kinematic space also plays a major rôle in the definition of the Amplituhedron geometry \[1\], we briefly review some of the salient features of projective geometry and momentum twistor space that are relevant to our discussions. These concepts are of course well known \(see e.g. \[18, 20, 72\]\), but for convenience we recall them telegraphically. 

A key feature of the twistor correspondence \[73\] is the relation between points x in Minkowski spacetime and lines L in twistor space. For planar scattering amplitudes, the relevant “spacetime” is dual momentum space where region momenta xa are related to cyclically ordered external momenta pa via pa = xa − xa−1. Dual momentum space trivializes momentum conservation by the identification xn\+1 = x1. 

The kinematic data for n-point massless planar scattering amplitudes can be efficiently encoded in n momentum twistors \[18\], denoted ZI , where a = 1, . . . , n labels a

the particles and I = 1, . . . , 4 is an SL\(4\) index on which dual conformal symmetry acts linearly. The natural SL\(4\) invariant is the antisymmetric contraction of four momentum twistors with the Levi-Civita tensor, which we denote as

habcdi := IJKLZIZJ ZKZL . 

\(2.1\)

a

b

c

d

– 4 –

Scattering amplitudes in planar N = 4 sYM are invariant under both SL\(4\) transformations and the action of the little group i.e., the rescaling Za 7→ taZa. This rescaling invariance implies that the external data lives in the projective space 3

P . Moreover, 

in terms of the Za the amplitudes are invariant under a \(twisted\) cyclic symmetry: for the NkMHV helicity sector the amplitude is invariant under the transformation Z1 7→ Z2, Z2 7→ Z3, . . . , Zn 7→ ˆ

Z1 := \(−1\)k−1Z1 of the external data. 

Incorporating \(dual\) loop momenta y into the picture is achieved by associating a line L to y. We will often make use of the following notation: since lines in twistor space are characterized by the linear span of two representative points, we denote the line associated to xa ↔ La := \(Za, Za\+1\) := \(a a\+1\) and y ↔ Ly := \(AB\). For each loop, we can represent the corresponding line by two arbitrary momentum twistors ZA and ZB, defined modulo GL\(2\) transformations that leave the line invariant. We can furthermore expand ZA and ZB in an arbitrary basis of four linearly independent twistors Zi, Zj, Zk, and Zànd fix the GL\(2\) redundancy,1

ZA = Zi \+ α1Zk \+ α2Z\` , 

ZB = Zj \+ α3Zk \+ α4Z\` . 

\(2.2\)

In this work, we make regular use of such expansions, and depending on the purpose, we chose convenient expansion twistors. Quite nicely, the four unconstrained parameters αi in the twistor expansion of eq. \(2.2\) match the four degrees of freedom of an off-shell Feynman loop momentum. 

If we consider the analog of a generic Lorentz-invariant in dual momentum space x2 = \(p

ab

a\+pa\+1 \+ · · · \+ pb−1\)2 in momentum twistor space, we realize that this quantity breaks conformal invariance, 

haa\+1b\+1i

x2 =

, 

\(2.3\)

ab

haa \+ 1ihbb \+ 1i

as signaled by the appearance of the two-brackets in the denominator. In dual-conformally-invariant quantities, all two-brackets drop out and we therefore do not discuss them any further. Crucially, such non-light-like Lorentz invariants are important to characterize loop-propagators, where any local pole of the integrand is given by

local pole ↔ hABii\+1i . 

\(2.4\)

In the following it will be important that any other four-bracket involving the loop-line \(AB\) together with an arbitrary “external” line X constitutes a spurious pole if it appears in the denominator of some integrand

spurious pole ↔ hABXi, 

if

X 6= \(ii\+1\) . 

\(2.5\)

1Note that this choice of coordinates fixes the bracket hABkì = hijkì to be a loop-momentum independent function of the external kinematics. 

– 5 –



Below, we will see many examples of spurious poles that occur in various expansions of a scattering amplitude. 

One additional feature of the twistor correspondence is the following fact: whenever two spacetime points xa and xb are null separated, the associated lines in twistor space La and Lb intersect. This leads to special configurations of lines which can be concisely summarized in the following image \[72\]

\(2.6\)

For a more detailed introduction to the twistor correspondence, we refer directly to the above references \[18, 20, 72\]. 

Finally, let us elaborate on the connection between twistor geometry and the analytic structure of scattering amplitudes that will play an important rôle in this work. There is an intimate relation between configurations of \(loop\) lines in momentum twistor space and certain restricted kinematic configurations of loop momenta on unitarity cuts of loop integrands or local integrals. At one loop, we can depict the off-shell configuration of lines in twistor space corresponding to a generic loop integrand \(either of the amplitude or of an integral\) by a set of lines corresponding to external dual momenta, together with a line \(AB\) in a generic configuration \(parameterized via eq. \(2.2\)\), 

↔

\(2.7\)

In this setup, the loop-line \(AB\) does not intersect any of the lines associated to external kinematic points. In the next step, one could go to codimension one configurations by imposing one condition, e.g. hABii\+1i = 0, which geometrically means that the lines

– 6 –

\(AB\) and \(ii\+1\) intersect. 

↔

\(2.8\)

At the level of cuts, this corresponds to setting a single propagator hABii\+1i = 0 to zero. This codimension-one configuration for the line \(AB\) can be parameterized by three degrees of freedom. The intersection implies that one of the defining points of the \(AB\)-loop lies on the line \(ii\+1\). Taking into account the projectivity of the external data, one possible parametrization is

ZA = Zi \+ α1Zi\+1 , 

ZB = Zj \+ α2Zk \+ α3Z\` . 

\(2.9\)

In subsequent steps, one can impose additional constraints to end up on codimension-two, three, or four configurations of the line \(AB\). For completeness, we have included a list of higher codimension boundaries and their associated cut configurations in appendix A. 

2.1

Topological sign-flip definition of the Amplituhedron

The Amplituhedron is defined by three types of positivity conditions \[19\]. First, we have inequalities which carve out the positive part of the external kinematic space; these conditions depend only on the helicity configuration of interest and are loop-momentum independent. For NkMHV amplitudes the conditions read

NkMHV ext. positivity:

hii\+1jj\+1i > 0 , 

\(2.10\)

sequence \{habb\+1ii\}i6=a,b,b\+1 has k sign flips, 

where the twisted cyclic symmetry implies that \(−1\)k−1hn1ii\+1i > 0. For the simplest case of MHV \(k = 0\) amplitudes the positivity of the external data as defined in eq. \(2.10\) is equivalent to all ordered brackets being positive, MHV ext. positivity:

hijkli > 0 , 

for i < j < k < l . 

\(2.11\)

Second, there are inequalities between the loop variables \(AB\) and the external data, again naturally expressed in terms of sign flips,2

NkMHV loop positivity:

hABii\+1i > 0 , 

\(2.12\)

sequence \{hABiji\}j6=i has k\+2 sign flips. 

2As we will see in subsection 2.2, for MHV and MHV amplitudes, there is an equivalent formulation of the loop-positivity given in eqs. \(2.31\) and \(2.32\), respectively. 

– 7 –

Finally, for multi-loop calculations, the third type of positivity conditions demand that all loops are mutually positive, 

multi-loop positivity:

h\(AB\)i\(AB\)ji > 0, for i 6= j = 1, . . . , L. 

\(2.13\)

The set of conditions in eqs. \(2.10\), \(2.12\), and \(2.13\) define the general loop-level Amplituhedron A\(n,k,L\) relevant for n-particle NkMHV L-loop integrands in the space of L lines \(AB\)1, . . . , \(AB\)L and n momentum twistors Z1, . . . , Zn. As such, the space defined by eqs. \(2.10\), \(2.12\), and \(2.13\) constitutes a highly nontrivial example of a positive geometry \[4\]. In this setup, the n-point NkMHV L-loop integrand is conjectured to be the unique degree 4\(k\+L\) differential form on this space defined by having logarithmic singularities on all its boundaries. We denote this form \(that is, the integrand \) by Ω\(n,k,L\),3

L

Y

Ω\(n,k,L\) =

h\(AB\)id2Aiih\(AB\)id2Bii × ω\(n,k,L\), 

\(2.14\)

i=1

where ω\(n,k,L\) is a 4k-form in external momentum twistors Za, but is simply a rational function in the loop variables \(AB\)1, . . . , \(AB\)L. The loop integrand can be obtained by replacing the differentials dZa with the fermionic Grassmann variables ηa to work directly in on-shell superspace. For MHV amplitudes, ω\(n,0,L\) is just a rational function of Za and \(AB\)i and directly constitutes the loop integrand. 

Rudiments of positive geometry

In the course of exploring the geometric properties of the local representation of loop integrands, we shall naturally encounter a variety of “spaces.” Loosely speaking, we define a geometric space in this work to be a collection of inequalities imposed on four-brackets involving the loop line \(AB\). By parametrizing \(AB\) as above in terms of four \(real\) degrees of freedom x1, . . . , x4, any four-bracket between \(AB\) and a bitwistor Xi becomes a polynomial pi\(x1, . . . , x4\) := hABXii. A more precise definition of a geometric space S is then a semialgebraic set defined by some number say, d, of inequalities

S = \{\(x1, . . . , x4\)|p1 > 0, . . . , pd > 0\}. 

\(2.15\)

Note that this definition does not require the existence of a canonical form, and thus may or may not be a positive geometry satisfying the recursive definition of \[4\]. It may happen that no line in

3

P satisfies the conditions we impose, which means eq. \(2.15\)

would be equivalent to the empty set; we shall refer to such spaces as empty. 

3We commonly use the notation that all capital forms Ω include the loop measure, whereas for lower-case forms ω the measure has been stripped off. 

– 8 –

The existence of a canonical form with logarithmic singularities on all boundaries puts further constraints on the general geometric space S. In particular, since any logarithmic form in the one-loop space is of degree four and can be written as the d log of four \(projectively invariant\) ratios,4 any one-loop positive geometry must be defined by at least five inequalities. Any space defined by four or fewer inequalities must have only the trivial form Ω = 0; throughout this work we refer to such geometries as zero form spaces. 

2.2

One-loop MHV and MHV spaces

Following the general Amplituhedron definitions above, let us now specialize to the geometry relevant to MHV one-loop amplitudes. As stated previously, for MHV integrands \(i.e., k = 0\) the positivity conditions on the external data eq. \(2.10\) simplify significantly to eq. \(2.11\). Besides the MHV integrand, there is another one-loop integrand which naturally lives in the same kinematic space: namely, its parity conjugate. 

In twistor space, spacetime parity is implemented by the duality under the exchange of points and planes, Za ↔ Wa := \(a−1aa\+1\) \(often, we will use the alternative notation a := \(a−1aa\+1\)\). Thus, we will refer to this “dual” space, as well as its corresponding canonical form, with the moniker “MHV,” despite the fact that the actual MHV

Amplituhedron corresponds to setting k = n−2, which yields a slightly different set of positivity constraints on the external data \(see eq. \(2.10\)\). Despite the fact that these two spaces are not equivalent \(because the definition of each involves different positivity conditions on the external data\!\), their canonical forms are trivially related by stripping the overall tree-level amplitude prefactor. 

Both the MHV and MHV integrands have only local poles; equivalently, the only codimension-one boundaries of both geometries are the loci where hABii\+1i = 0. We can think of the MHV and MHV spaces as being cut out from a “larger” space defined only by hijkli > 0, for i < j < k < l, and hABii\+1i > 0, without any additional constraints. For reasons which will become more clear below, we call this space an

“achiral” one-loop space. By construction, its codimension-one boundaries are the same as those of the MHV and MHV subspaces. From this perspective, it is quite nontrivial that there even exist two distinct ways of slicing the achiral space without introducing additional codimension-one \(spurious\) boundaries. Since the notion of chiralization plays a pivotal rôle in our analysis of local triangulations throughout this work, in the 4Since we can always rescale the entry of any d log form by a four-bracket involving only the external data, it is always trivial to make any entry projective in all Zi, without modifying the canonical form \(or, in the case of MHV data, affecting the overall sign of the entry\). In this work we shall often neglect to write such factors, meaning our d log entries will be manifestly projective only in \(AB\). 

– 9 –

following subsection we review some salient features of the MHV and MHV one-loop geometries. 

2.3

Boundaries of MHV amplitudes

In this subsection, we briefly discuss the geometric boundaries of the “Kermit” expansion of one-loop MHV amplitudes \[49\]. In particular, we will show how to detect whether or not certain boundaries are present in the geometry and if the corresponding poles appear in the logarithmic form. This discussion allows us to introduce the necessary notation and concepts used in our later analysis of chiral pentagons. 

The inequalities defining the one-loop MHV Amplituhedron are a special case of eq. \(2.12\), and involve the usual positivity of adjacent brackets as well as a sign-flip condition:

MHV loop positivity:

hABii\+1i > 0 , 

\(2.16\)

\{hAB12i, . . . , hAB1ni\} has two sign flips, 

where we have chosen the sequence \{hAB1ii\}i=2,...,n only for specificity and to easily handle the twisted cyclic symmetry in the last bracket of the sequence. There are a number of sign choices for the brackets appearing in eq. \(2.16\) consistent with two sign flips, which can be labelled by two indices i, j indicating the brackets hAB1ii and hAB1ji where the sign flip occurs. The geometry of these individual sign-flip patterns is completely well understood: the pattern where the sign flips occur at indices i and j is directly associated to a “Kermit” which corresponds to a particular cell in the positive Grassmannian. In the following, we make repeated use of these sign-flip patterns and often denote brackets by their respective sign, e.g., for the \(i, j\) flip term, 

\{hAB12i, . . . , hAB1ii, hAB1i\+1i, . . . hAB1ji, hAB1j\+1i, . . . , hAB1ni\}

\(2.17\)

7→ \{\+, . . . , \+, −, . . . −, \+, . . . , \+\}. 

For the \(i, j\) sign-flip region, the line \(AB\) can be conveniently parametrized as A = Z1 \+ αiZi \+ αi\+1Zi\+1, 

B = −Z1 \+ αjZj \+ αj\+1Zj\+1 . 

\(2.18\)

In this coordinate chart, the inequalities in eq. \(2.17\) are equivalent to αi, αi\+1, αj, αj\+1>0

and therefore the canonical form is simply the d log form in all variables.5 Written projectively, this yields the expression for the canonical form \(stripping off the measure hABd2AihABd2Bi\)

X

X

hAB\(1ii\+1\)∩\(1jj\+1\)i2

ω\(n,0,1\) =

ω\(i,j\) ≡

, \(2.19\)

n

hAB1iihAB1i\+1ihABii\+1ihAB1jihAB1j\+1ihABjj\+1i

i<j

i<j

5For detailed discussions and numerous examples of going from inequalities to forms, see e.g. \[19, 23\]. 

– 10 –

where \(1ii\+1\)∩\(1jj\+1\) is the line in which the planes \(1ii\+1\) and \(1jj\+1\) intersect.6

By construction, each term in this expansion is associated with a non-overlapping piece of the amplitude; in other words, this collection of cells provides an honest triangulation by introducing term-wise spurious poles of the form hAB1ii in the denominator. The fact that these individual sign-flip spaces are non-overlapping follows directly from the observation that different Kermit cells differ by the signs of at least one of the inequalities defining their regions. 

Let us provide a simple concrete five-point example where there are three different sign patterns with two sign-flips. Since the hAB12i and hAB15i brackets are forced to be positive by the loop conditions in eq. \(2.16\), the three sign patterns are labelled by the signs of hAB13i and hAB14i, i.e., 

\(i, j\)

hAB12i

hAB13i

hAB14i

hAB15i

\(3,4\)

\+

\+

−

\+

. 

\(2.20\)

\(2,3\)

\+

−

\+

\+

\(2,4\)

\+

−

−

\+

In the first column we indicate the locations \(i, j\) at which the sign flips occur, which directly match the labels in eq. \(2.19\). 

Note that although all spaces are na¨ıvely

defined by the same number of inequalities, in this table, the spaces where j = i\+1

are geometrically simpler than the generic case. To illustrate this point and make our notion of “geometric boundaries” clear, we now consider the \(3, 4\) cell in more detail. 

The analysis of the properties of this space is particularly amenable to the following parametrization:

A = Z2 \+ wZ1 \+ xZ5, 

B = Z3 \+ yZ1 \+ zZ5. 

\(2.21\)

This choice of coordinates gauge-fixes hAB15i = h1235i > 0. Imposing hABii\+1i > 0, hAB13i > 0 and hAB14i < 0 defines the \(3, 4\) Kermit space:

hAB12i = −xh1235i > 0, 

hAB23i = \(wz − xy\)h1235i > 0, 

hAB34i = −yh1234i \+ \(wz − xy\)h1345i \+ zh2345i > 0, 

hAB45i = −yh1245i \+ wh1345i \+ h2345i > 0, 

\(2.22\)

hAB15i = h1235i > 0, 

hAB13i = −zh1235i > 0, 

hAB14i = h1234i − zh1245i \+ xh1345i < 0. 

6A review of the projective geometry relevant to this work is given in section 2 and appendix A. 

– 11 –

The codimension-one boundaries of this space correspond to localizing one \(and only one\) of the variables w, x, y, z by setting one of the brackets in eq. \(2.22\) to zero. 

However, not all of the inequalities in eq. \(2.22\) are boundaries. In particular, we will now demonstrate that setting either hAB12i → 0, hAB23i → 0, or hAB14i → 0 leads to an inconsistent set of inequalities in the three remaining variables, thus proving that none of these brackets are geometric boundaries of the \(3, 4\) Kermit. First, consider hAB12i → 0 which, in our parametrization, corresponds to sending x → 0. From eq. \(2.22\), we have

hAB14i −→ h1234i − zh1245i < 0, 

\(2.23\)

x→0

which implies that z > h1234i/h1245i > 0. 

This is inconsistent with hAB13i =

−zh1235i > 0, which demands that z < 0. Thus, hAB12i → 0 is not a codimension-one boundary of the space. Next, consider hAB23i → 0, which can be parametrized as w → xy/z. In this case, the space defined by eq. \(2.22\) is equivalent to x, z < 0 and, after some algebraic manipulation, 

hAB34i −→ − yh1234i \+ zh2345i > 0, 

w→xy/z

hAB45i −→ y\(xh1345i − zh1245i\) \+ zh2345i < 0, 

\(2.24\)

w→xy/z

hAB14i −→ h1234i − zh1245i \+ xh1345i < 0. 

w→xy/z

The first inequality in eq. \(2.24\) together with z < 0 implies that y < 0. Multiplying the third inequality in eq. \(2.24\) by y and adding zh2345i to both sides, we find y\(xh1345i − zh1245i\) \+ zh2345i > −yh1234i \+ zh2345i > 0, 

\(2.25\)

which is incompatible with the second inequality of eq. \(2.24\). Finally, consider setting hAB14i → 0, which corresponds to x → \(zh1245i − h1234i\)/h1345i. In this case, eq. \(2.22\) yields

hAB34i → z \(−yh1245i \+ wh1345i \+ h2345i\) > 0, 

\(2.26\)

hAB45i → −yh1245i \+ wh1345i \+ h2345i > 0, 

which, together with z < 0, are incompatible. 

In contrast to the three examples just considered, it is straightforward to verify that no such inconsistency is found upon setting either hAB34i → 0, hAB45i → 0 or hAB13i → 0. Thus, these three brackets are geometric boundaries of the space defined in eq. \(2.22\). In fact, hAB15i → 0 is also a geometric boundary of the full projective space; while this fact is obscured in our choice of gauge-fixing, it can be proven with

– 12 –

a similar argument as above by working in an alternative parametrization \(which fixes the sign of some other four-bracket\). 

Thus, the \(3, 4\) cell has four codimension-one boundaries hAB34i, hAB45i, hAB15i and hAB13i which also correspond to the allowed poles in the associated canonical form. 

An analogous argument holds for the \(2, 3\) cell, while the \(2, 4\) cell is a generic Kermit with six accessible codimension-one boundaries. A straightforward computation yields the following expressions for the canonical forms:

h1345i2

h1234i2

ω\(3,4\) =

, 

ω\(2,3\) =

, 

5

hAB13ihAB34ihAB45ihAB15i

5

hAB12ihAB23ihAB34ihAB14i

hAB\(123\)∩\(145\)i2

ω\(2,4\) =

. 

\(2.27\)

5

hAB12ihAB23ihAB13ihAB14ihAB15ihAB45i

The spurious boundary hAB13i = 0 cancels geometrically between the first and third sign-flip terms in eq. \(2.20\). This can be seen in the parametrization of eq. \(2.21\) by sending z → 0 in both spaces, and observing that the contributions completely overlap and therefore cancel. A similar analysis shows that the spurious boundary hAB14i = 0

cancels between the second and third space in eq. \(2.20\). Algebraically, the cancellation of spurious poles can be observed between the corresponding forms in eq. \(2.27\). We will see later that the algebraic cancellation of a spurious pole in the form is not, in general, sufficient to imply a geometric cancellation of the corresponding spurious boundary. 

As indicated earlier, the one-loop MHV Amplituhedron space is a slice of a larger

“achiral” positive space given only by the hABii\+1i>0 conditions. In the five-point example, the achiral space allows for arbitrary signs of the “spurious-pole” brackets hAB13i, hAB14i. This means that in addition to the three sign-flip patterns of eq. \(2.20\), we have one additional sign-flip-zero space where both hAB13i and hAB14i are positive, 

hAB12i

hAB13i

hAB14i

hAB15i

\(2.28\)

\+

\+

\+

\+

Having zero sign flips in the sequence \{hAB1ii\} actually implies that all hABiji > 0

are positive for any i < j. The corresponding logarithmic form reproduces the five-point MHV amplitude, and the \{\+\+\} sign pattern is an example of the MHV space discussed above and is directly related to the MHV space by parity conjugation. This has a direct generalization to higher points: the MHV space has two sign flips in the

\{hAB1ii\} sequence, while the MHV parity conjugate has zero sign flips. At higher points, na¨ıvely, there are additional subregions of the larger achiral space with more

– 13 –

than two sign-flips. For example, at six points we can have hAB12i

hAB13i

hAB14i

hAB15i

hAB16i

\(2.29\)

\+

−

\+

−

\+

However, this combination of inequalities is an example of an empty space discussed in subsection 2.1. In fact, it is known \[19\] that, for MHV external data, the same is true for all spaces with more than two sign flips\! Thus, remarkably the achiral space can be cut into two \(and only two\) chiral subspaces, MHV and MHV, which have only local boundaries of the form hABii\+1i=0. 

Note that the sign-flip-zero \(MHV\) space in the five-point example of eq. \(2.28\)

was not triangulated further into simpler subspaces \(with spurious poles\). Therefore, the generalization of this space at n-points has n boundaries, while any individual sign-flip-two region only has \(up to\) six codimension-one boundaries, as can be seen from the Kermit canonical form in eq. \(2.19\). It is therefore natural to ask whether or not we can analogously slice the sign-flip-zero region into simpler spaces with fewer boundaries, just as we did with the Kermits for the sign-flip-two MHV pattern. This slicing can be achieved by realizing that both MHV and MHV spaces are related by parity, Za ↔ Wa. In particular, the n-point MHV space has an equivalent definition as the sign-flip-two space in the Wa coordinates, i.e., two sign flips in the sequence

“MHV” positivity :

hijkli > 0 , 

for i < j < k < l, 

hABii\+1i > 0, 

\(2.30\)

\{hAB12i, hAB13i, . . . , hAB1ni\}

has two sign flips, 

where the hAB1ii term in the MHV sequence eq. \(2.16\) has been replaced by hAB1ii, and \(1i\) denotes the intersection of the planes ¯

1 = −\(n12\) and ¯i = \(i−1ii\+1\). By

expanding the intersections in the first and last brackets in this sequence, we see they are invariant under conjugation \(up to a factor that only depends on the external data\) and are therefore both positive as a consequence of hAB12i, hAB1ni > 0. In this definition, the MHV space is triangulated by the collection of sign-flip-two regions of eq. \(2.30\), analogous to the Kermit triangulation of the MHV space. Using the sequence of brackets in eq. \(2.30\), we can conversely define the MHV space as the single sign-flip-zero region with all hABiji > 0, for i < j \(always accounting for the twisted cyclic symmetry when i = 1 or j = n\). 

While breaking up the MHV and MHV spaces into smaller regions using sign flips is a useful triangulation strategy, we can also characterize them in a uniform way as the sign-flip-zero regions in eq. \(2.16\) and eq. \(2.30\) respectively. In addition to

– 14 –

hABii\+1i > 0 and the k=0 conditions on the external data eq. \(2.11\), we get: alternative MHV :

hABiji > 0, 

for all i < j, 

\(2.31\)

alternative MHV :

hABiji > 0, 

for all i < j. 

\(2.32\)

As we have seen, the Kermit expansion \[49\] of the MHV one-loop integrand in eq. \(2.19\)

is in one-to-one correspondence with the sign-flip representation of the Amplituhedron, and it provides a very natural triangulation. We call this triangulation internal, emphasizing that it cuts the Amplituhedron into smaller pieces by introducing internal \(spurious\) boundaries. Each geometric space associated to a Kermit lies inside the Amplituhedron, but in addition to physical \(Amplituhedron\) boundaries it also has a number of spurious boundaries of the form hAB1ii = 0, which cancel geometrically when taking the collection of all Kermits. The analogues of Kermit expansions for higher k and L have been found in \[23\], and they involve more complicated spurious poles whose cancellations are nontrivial to demonstrate analytically. 

MHV and MHV geometry and allowed singularity structure

As we have laid out in section 2 and appendix A, taking residues of one-loop integrands in loop-momentum space is equivalent to localizing the line \(AB\) to special configurations with respect to the external \(ii\+1\) lines. On the other hand, imposing a set of inequalities \{hABX1i > 0, . . . , hABXri > 0\}, where the Xi are some lines \(involving external data\) in

3

P , effectively slices the full configuration space of \(AB\) into smaller subspaces. A given subspace will generically contain a rather small subset of the possible special configurations associated to cuts of the integrand. The constraint that a cut-configuration of the loop line \(AB\) be compatible with the inequalities defining the positive geometry of interest becomes rather severe once we go deep into the cut structure to, say, codimension-four boundaries. Checking the compatibility of certain cut configurations and the geometric inequalities will then tell us which singularities are physical and which ones are spurious. 

Let us illustrate this point explicitly in the case of the MHV one-loop geometry. As we discussed in eq. \(2.16\) and eq. \(2.31\), this space can be characterized by a simple set of inequalities, hABii\+1i > 0 and hABiji > 0 \(together with the conditions on the external data in eq. \(2.10\)\). It is easy to verify that none of the codimension-one \(eq. \(2.8\)\) or two configurations \(listed in eq. \(A.4\) of appendix A\) violate any of these inequalities, so all of these singularities are physical. However, there are two spurious codimension-three configurations which violate the MHV inequalities: the three-mass

– 15 –

triple cut where \(AB\) intersects three non-adjacent lines, not allowed in MHV:

↔

, 

\(2.33\)

as well as the configuration where \(AB\) is in the plane \(i\) and intersects a non-adjacent line \(kk\+1\), 

not allowed in MHV:

↔

. 

\(2.34\)

To prove that the three-mass triple cut of eq. \(2.33\) lies outside of the MHV Amplituhedron, we first consider the simplest six-point case where this cut first arises, hAB12i = hAB34i = hAB56i = 0. This cut can be parametrized by setting

\(AB\) = \(\(Z1 \+ xZ2\)34\)∩\(\(Z1 \+ xZ2\)56\)

\(2.35\)

= \(134\)∩\(156\) \+ x\(134\)∩\(256\) \+ x\(234\)∩\(156\) \+ x2\(234\)∩\(256\), 

where x parametrizes the intersection point of the lines \(AB\) and \(12\). Because this cut is inconsistent with both the MHV and MHV geometries, the proof that this cut configuration is spurious must follow directly from the inequalities which are valid in both spaces. For this example, these are the three inverse propagators

hAB23i = h1234i\(h1356i \+ xh2356i\) > 0, 

hAB45i = −\(h1345i \+ xh2345i\)\(h1456i \+ xh2456i\) > 0, 

\(2.36\)

hAB16i = h1256ix\(h1346i \+ xh2346i\) > 0. 

This set of inequalities is equivalent to

h1345i

h1346i

h1356i

−

< x < −

and

x > −

. 

\(2.37\)

h2345i

h2346i

h2356i

– 16 –

Non-trivially, the upper bound on x in the first inequality is inconsistent with the second lower bound given. 

Namely, by combining x < −h1346i/h2346i and x > 

−h1356i/h2356i we find, using the Schouten identity, 

h1356ih2346i − h1346ih2356i

h1236ih3456i

0 < 

= −

< 0, 

\(2.38\)

h2346ih2356i

h2346ih2356i

which is a contradiction. This proof crucially depends on the simple external data positivity conditions relevant for the MHV and MHV spaces. The general three-mass triple cut hABii\+1i = hABjj\+1i = hABkk\+1i = 0 can be shown to be spurious by the obvious generalization of the parametrization of eq. \(2.35\), and the proof depends only on the inequalities adjacent to the cut propagators. 

In contrast, the codimension-four leading singularities are much easier to analyze, as any inequality evaluated on such a configuration just reduces to a condition on the external data. In fact, simply demanding compatibility of the inequalities defining the MHV space eq. \(2.31\) evaluated on the leading singularity configurations listed in appendix A with the positivity constraints on the external data eq. \(2.10\) is enough to fix the positions of all MHV leading singularities to \(AB\) = \(ij\). Said differently, any leading singularity not of this form will explicitly violate at least one of the inequalities defining the MHV space. For example, at five points, the line \(13\) is an allowed leading singularity, but its parity conjugate \(13\) = −\(512\)∩\(234\) is not. 

allowed in MHV:

not allowed in MHV:

\(2.39\)

From the inequalities point of view, this can be clearly seen by evaluating hAB24i =

hAB\(123\)∩\(345\)i on the forbidden leading singularity \(AB\) = \(13\), which gives hAB24i

=−h\(512\)∩\(234\)\(123\)∩\(345\)i=−h1235ih2345ih1234i<0, 

\(2.40\)

\(13\)

and is incompatible with being inside the MHV Amplituhedron. This argument goes through at n-points. The leading singularities of the form \(ij\), for i < j, are allowed precisely because of the nontrivial positivity conditions \[70\]

hABkì

=hijkì>0, 

for i < j, 

\(2.41\)

\(ij\)

while the parity conjugate lines \(ij\), as well as all other codimension-four configurations listed in appendix A, are always inconsistent with at least one of the positivity constraints. Note that related analyses were performed in \[34\] in order to check admissible Landau singularities in planar N = 4 sYM. 

– 17 –

2.4

Positivity and the dual Amplituhedron

The original idea of linking scattering amplitudes to projective geometry appeared in the seminal work by Andrew Hodges \[18\] \(which pre-dates the Amplituhedron\) who showed that the six-particle NMHV tree-level amplitude can be interpreted as the volume of a polytope in dual momentum twistor space. Later it was shown that the same amplitude can also be associated with a logarithmic differential form, Ω, directly in momentum twistor space. It is this picture of amplitudes as differential forms with logarithmic singularities that was later generalized to the Amplituhedron for all n, k, and L. For many reasons, the original volume interpretation seems more fundamental than thinking about amplitudes as differential forms. This led to the conjecture of the existence of a dual Amplituhedron \[70\] whose volume calculates all scattering amplitudes in planar N = 4 sYM theory. 

The only case for which we fully understand the volume interpretation, however, remains the NMHV tree-level amplitude. There, both the Amplituhedron and the dual Amplituhedron are certain polytopes in projective space

4

P which are related by the

standard dualization procedure: vertices in the Amplituhedron space are mapped into faces of the dual Amplituhedron, and similarly for other boundaries \(codimension r subspaces of the Amplituhedron map into codimension 5 − r \+ 1 subspaces of the dual Amplituhedron\). It is not clear how to repeat the same procedure beyond NMHV

\(k > 1\) and/or at higher loops \(L > 0\) where Amplituhedra are no longer polytopes but rather their generalizations to Grassmannians and beyond \[1\]. 

Even without an explicit definition of the dual Amplituhedron, there are two important properties which follow from its presumed existence. First, volumes are naturally positive and therefore, we would expect that amplitudes exhibit a similar positivity property. While the definition of the Amplituhedron is based on a set of positivity conditions eq. \(2.10\) and eq. \(2.12\), nothing a priori predicts any positivity properties of the differential form Ω. However, if the amplitude also has a volume interpretation, then we expect that Ω is positive in some suitable sense. Indeed, it was shown in \[70\]

for many nontrivial examples that if we strip off the measure from Ω i.e., Ω\(n,k,L\) = dµ ω\(n,k,L\) , 

\(2.42\)

then the integrand ω\(n,k,L\) \(which is just the scattering amplitude\) is in fact positive if evaluated inside the positive region for both Za and Li = \(AB\)i. The positivity of ω\(n,k,L\) therefore serves as indirect evidence for the existence of a dual Amplituhedron and the volume interpretation of scattering amplitudes, 

Z

ω\(n,k,L\) =

dV. 

\(2.43\)

e

A

– 18 –

where e

A is the dual Amplituhedron space and dV is the appropriate volume form. An important clue on how to proceed in the search for the dual Amplituhedron is to investigate whether or not positivity is respected in the context of different triangulations of the Amplituhedron. Despite the fact that the full integrand ω\(n,k,L\) is positive inside the positive region, individual terms in e.g., the BCFW triangulation of An,k,L do not have definite signs inside the positive space. While individual BCFW terms internally triangulate the Amplituhedron, in the dual picture, they get mapped to spaces that are partially outside of the dual Amplituhedron and therefore do not have a uniform sign. This is easiest to understand with a simple toy example of a quadrilateral in the projective plane:

←→

\(2.44\)

dual to

=

←→

=

−

dual to

\+

The two triangles with vertices \(123\) and \(134\) triangulate the quadrilateral, but in the dual picture they correspond to triangles which lie partially outside of the dual quadrilateral. Therefore, while the triangles on the left-hand-side of \(2.44\) give an internal triangulation of the original space via the line \(13\), in the dual picture, this corresponds to an external triangulation with an external triangulation point \(13\) that is outside the dual space. In the same sense, internal triangulations of the Amplituhedron are expected to externally triangulate the dual Amplituhedron. 

In particular, the Kermit expansion of MHV amplitudes internally triangulates the one-loop Amplituhedron \[1\] and—following our discussion above—is expected to externally triangulate the putative dual Amplituhedron. This external triangulation of the dual space therefore suggests that individual Kermits will not be positive term-wise \(after stripping the measure\) despite the positivity of the full one-loop integrand. 

– 19 –

We can see this non-positivity directly by looking at the denominators of the kermit forms: each Kermit contains denominator factors like hAB1ii which do not have a fixed sign inside the Amplituhedron. Consequently, for fixed positive external data and an arbitrary point \(AB\) inside the MHV one-loop Amplituhedron, the stripped forms ω\(i,j\)

n

in eq. \(2.19\) can have arbitrary signs. 

It is very natural to ask about a term-wise positive expansion of the amplitude, which geometrically would provide an internal triangulation of the putative dual Amplituhedron. While we will not definitively establish the existence of a dual Amplituhedron in this work, it is easy to at least find a term-wise positive expansion of the amplitude. 

A priori, any such candidate expansion must have only local poles, hABii\+1i as only these terms have fixed signs, and in addition the numerator factors must be uniformly positive inside the Amplituhedron. As it turns out, the right candidate is the chiral pentagon expansion \[49, 69, 72\]7

X

X

ω\(n,0,1\) =

ω\(n\) =

ij

i<j

i<j

\(2.45\)

X

h1ijnihABiji

=

. 

hABi−1iihABii\+1ihABj−1jihABjj\+1ihAB1ni

i<j

As a consequence of the MHV loop-positivity eq. \(2.31\), together with the positivity of external data hijkli > 0 \(for i < j < k < l\) in eq. \(2.11\), it can be seen that all four-brackets in eq. \(2.45\) are manifestly positive, including the loop-momentum dependent part of the numerator. Based on this positivity property of individual terms, the natural conjecture is that these chiral pentagons internally triangulate the dual Amplituhedron \(but externally triangulate the original Amplituhedron\). In our quadrilateral analogy, this would correspond to introducing a spurious triangulation point \(12\)∩\(34\) outside 7In the representation here, we have singled out a particular propagator hAB1ni that appears in all diagrams and will also take a special rôle in our geometric considerations below. Furthermore, we point out that the chiral pentagon expansion contains various “boundary” terms that correspond to one-mass, and two-mass hard box integrands. This should be contrasted to the older representations of one-loop n-point MHV amplitudes \[74\] in terms of two-mass easy boxes that only match the parity-even sector at the integrand level but are of course equivalent upon loop integration. 

– 20 –

the quadrilateral, 

=

−

←→

=

\(2.46\)

dual to

While the chiral pentagons have only physical codimension-one poles hABii\+1i \(we also refer to them as local poles\), their higher codimension singularities are not all physical. 

For example, the generic chiral pentagon eq. \(2.45\) has a non-zero residue at the leading singularity location \(AB\) = \(ijj\+1\)∩\(in1\), which is not a physical leading singularity of MHV amplitudes and corresponds to a cut solution labeled by the following on-shell

function8

↔

\(2.47\)

As we will show, in the original Amplituhedron geometry this means that all codimension-one boundaries are given by physical hABii \+ 1i = 0 singularities analogous to the lines \(i i\+1\) in eq. \(2.46\), whereas higher codimension boundaries can be spurious \(such as the spurious triangulation vertex \(12\)∩\(34\)\). In the dual picture, some of the first boundaries of chiral pentagon spaces are spurious, analogous to the spurious triangulation line of our quadrilateral example on the right-hand-side of eq. \(2.46\). 

3

Geometry of d log forms

In this section we lay the groundwork for further study of the relation between positive geometry and local triangulations of the Amplituhedron. As a first step, we need to associate a geometric region to a particular local loop-integrand form. The most natural starting point for such an endeavour is the d log representation of local integrands. 

8Here, we make use of on-shell functions to label solutions to on-shell conditions and not the value of field theory cuts. This dual meaning of on-shell functions is common in the literature, see e.g. \[75\]. 

– 21 –

3.1

d log forms for pentagon integrands

It is our goal to associate a “local” positive geometry to each chiral pentagon and explore how they glue together into a larger geometric object. In a subsequent step, we define these new objects and find their connection to the Amplituhedron in section 5. Starting from the local representation of the one-loop MHV amplitude eq. \(2.45\), our only input information is the rational pentagon integrand. Due to the natural connection between d log forms and positive geometry, we therefore rewrite the integrands appearing in eq. \(2.45\) as d log forms \[48\], 

Ω\(n\) = hAB d2AihAB d2Bi ω\(n\) = d log f

ij

ij

1 d log f2 d log f3 d log f4 , 

\(3.1\)

where we suppress the wedge notation for differential forms and fj are ratios of four-brackets \(to be specified in eq. \(3.3\)\). We would like to interpret this d log form as the form with logarithmic singularities on a region which has fixed signs of all fj. In particular, each fj can be either positive or negative which leads to 24 = 16 different regions that each have the same d log form. Furthermore, the change of variables eq. \(3.1\) is not unique and there are many different looking d log forms that all have the same rational form appearing in eq. \(2.45\). 

For the massless scalar box integral, which can be viewed as a particular n = 4

degeneration of the chiral pentagon, there are at least two different d log forms, hABd2AihABd2Bih1234i2

Ω\(4\) =

=

\(3.2\)

23

hAB12ihAB23ihAB34ihAB14i

hAB12i

hAB23i

hAB34i

hAB14i

= d log

d log

d log

d log

hABXi

hABXi

hABXi

hABXi

where we can choose between the two solutions of the quadruple cut, X = \(13\) or X = \(24\). 

For X = \(13\) the d log form eq. \(3.2\) explicitly depends on hAB13i. 

Therefore, one might worry that this spurious pole could show up in the rational form.9

However, by construction, the d log form cannot have hAB13i or hAB24i as an actual singularity. Algebraically, the absence of the spurious poles from the rational integrand derived from the d log form eq. \(3.2\) follows from non-trivial kinematic identities. 

For more complicated integrands, various alternative d log forms for the same rational integrand might look remarkably different. This is also the case for the generic chiral pentagon we discuss next. One particular d log form for this integrand has been 9The presence of spurious poles in the arguments of d log’s is a very general feature, and in fact is relevant for understanding simplified differential equations based on d log integrands \[76\]. 

– 22 –

written down in ref. \[48\] which manifestly breaks the ij flip symmetry of the diagram, hABd2AihABd2Bih1ijnihABiji

Ω\(n\) =

=

\(3.3\)

ij

hABi−1iihABii\+1ihABj−1jihABjj\+1ihAB1ni

hABi−1ii

hABii\+1i

hABj−1ji

hABjj\+1i

= d log

d log

d log

d log

, 

hABn1i

hABn1i

hAB\(in1\)∩ji

hAB\(in1\)∩ji

with an analogous expression for i ↔ j. Here, we present a new d log form for Ω\(n\): ij

hABi−1ii

hABj−1ji

hAB\(n1i\)∩\(ij?\)i

hAB\(n1j\)∩\(ij?\)i

Ω\(n\)=d log

d log

d log

d log

, 

ij

hABii\+1i

hABjj\+1i

hAB1ni

hAB1ni

\(3.4\)

where ? corresponds to an arbitrary point in momentum twistor space. It is a highly non-trivial statement that the integrand form does not depend on the choice of ?. Let us point out that our new d log representation in eq. \(3.4\) has two nice features: \(i\) it is manifestly ij symmetric, and \(ii\) it makes the fact that the integrand vanishes for \(AB\) ∈ \(i−1ii\+1\) or \(AB\) ∈ \(j−1jj\+1\) obvious since e.g. only one d log blows up on this cut – hABi−1ii and hABii\+1i appear together in one ratio – and this is not enough to produce a non-zero residue. However, the other solution of the double cut hABi−1ii = hABii\+1i = 0, which is A = i, does produce a non-zero residue because hAB\(n1i\)∩\(ij?\)i also vanishes. In the simplest five-point case, the d log form reads hAB d2AihAB d2Bih1245ihAB24i

Ω\(5\) =

=

\(3.5\)

24

hAB12ihAB23ihAB34ihAB45ihAB15i

hAB12i

hAB34i

hAB\(512\)∩\(243\)i

hAB\(514\)∩\(243\)i

= d log

d log

d log

d log

, 

hAB23i

hAB45i

hAB15i

hAB15i

where we have chosen the special point ? = 3. 

Similar to the chiral pentagon expansion of the MHV amplitude in eq. \(2.45\), we can write an analogous formula for the MHV amplitude where the pentagon with a

– 23 –





wavy-line numerator is replaced by a dashed-line numerator of opposite chirality, X

X

ω\(n,n−2,1\) =

ω\(n\) =

ij

i<j

i<j

\(3.6\)

X

h1ijni hABiji

=

. 

hABi−1iihABii\+1ihABj−1jihABjj\+1ihAB1ni

i<j

and all statements about the “MHV” pentagons can be readily transferred to the

“MHV” pentagons as well. For completeness, we write a novel symmetric d log form \(n\)

for Ω

obtained by dualizing eq. \(3.4\), 

ij

\(n\)

Ω

=

\(3.7\)

ij

hABi−1ii

hABj−1ji

hAB\(\(n1\)∩i\)\(?∩j∩i\)i

hAB\(\(n1\)∩j\)\(?∩i∩j\)i

=d log

d log

d log

d log

, 

hABii\+1i

hABjj\+1i

hAB1ni

hAB1ni

where ? = \(x1x2x3\) is an arbitrary plane. 

Besides the two chiral pentagons appearing in eq. \(3.3\) and eq. \(3.6\), there is one additional pentagon that will play an important rôle, namely the parity-odd pentagon. 

In momentum space its numerator is proportional to the Levi-Cevita tensor and evaluates to zero upon integration over real Minkowski space. In momentum twistor space, the parity-odd numerator is the difference of two chiral numerators

N odd = hABijih1ijni−hAB ijih1ijni. 

\(3.8\)

ij

The relative minus sign between the the wavy and dashed numerators is necessary for the integrand to be unit on all codimension-four residues; a relative plus sign would give some leading singularities equal to ±2, rather than ±1. The denominator of the parity-odd pentagon is the same as in eq. \(3.3\). The d log form for this integral is very simple and involves only physical propagators:

hABi−1ii

hABii\+1i

hABj−1ji

hABjj\+1i

Ω\(n\),odd = d log

d log

d log

d log

, 

\(3.9\)

ij

hAB1ni

hAB1ni

hAB1ni

hAB1ni

where we could also reshuffle the propagators that appear in the denominator. The fact that only propagators appear as d log arguments also leads to a simple understanding of why this integral evaluates to zero from a differential equation point of view \[76\]. 

– 24 –



The difference of MHV and MHV amplitudes is the parity-odd amplitude, which integrates to zero on the parity invariant contour. However, it will play a very important rôle in our further discussion. Combining the expansions eq. \(2.45\) and eq. \(3.6\), we see that the chiral numerators combine precisely into the numerator N odd of eq. \(3.8\)

ij

and we get a sum of parity-odd pentagons





X 



X 



ωodd =

ω\(n\)−ω\(n\)

=



−



ij

ij





i<j

i<j 



\(3.10\)

N odd

X

=

ij

. 

hABi−1iihABii\+1ihABj−1jihABjj\+1ihAB1ni

i<j

Note that all “boundary terms” \(i.e. j = i\+1\) cancel between the MHV and MHV

sectors in this expansion so that there are no parity-even box integrals remaining. 

Therefore, the sum is zero at four points, gives one parity-odd pentagon at five points, and so on. 

3.2

From d log’s to geometry

In the usual Amplituhedron setup, we start with a positive geometry, and from it calculate the canonical form with logarithmic singularities on its boundaries. However, in our case the situation is reversed: we have the d log form for e.g. the pentagon integrand in eq. \(3.3\) or eq. \(3.4\), but we do not a priori know the correct geometric space associated to that differential form, let alone whether or not there is even a unique answer to that question. By construction, any space defined by demanding definite signs for the ratios of the arguments of each d log in e.g., eq. \(3.4\) gives some geometry with the appropriate canonical form. More generally, if we start with a d log form

Ω = d log f1 d log f2 d log f3 d log f4

\(3.11\)

there are 24 = 16 geometric spaces associated to it via the inequalities f1 ≶ 0, f2 ≶ 0, f3 ≶ 0, f4 ≶ 0 . 

\(3.12\)

Each d log fi factor is the correct form for both inequalities fi > 0 and fi < 0, up to a sign. \(If we did not impose any restrictions on fi, the form would vanish as there are no boundaries.\)

– 25 –

Faithful geometries and d log forms

As we have alluded to above, starting from a rational form of the integrand that only has logarithmic singularities there are often numerous ways to change variables to bring the integrand into a d log form. For the simple four-point box integrand, we found at least two solutions specified by the choice of hABXi in eq. \(3.2\). Likewise, for the chiral pentagons, we also have at least two alternative d log forms in eqs. \(3.3\) and \(3.4\). 

Combining this multitude of d log forms with the 16-fold multiplicity of geometric spaces associated to a given one-loop form encoded in the choice of inequalities in eq. \(3.12\), 

it is not hard to imagine that the number of possible geometric spaces associated to a given integrand quickly grows. It is therefore natural to ask, whether or not there exist any special subsets of geometries that have certain desirable properties. Here, and in the following, we are going to argue for faithful geometries. 

What we mean by faithful geometries is the following: for our purposes, simply getting the correct canonical form is insufficient—we also require the correct boundary structure of the geometric space itself. Concretely, we demand that all boundaries of the geometry show up as poles in the form, and furthermore that these are the only boundaries. \(Note that looking at the entries of the d log forms can be misleading as certain entries of the d logs are in fact not poles of the form. If one were to compute the residue on such a pole, one in fact finds zero. The simplest example of this is hABXi in eq. \(3.2\). This bracket is manifestly absent in the rational representation of the form so that it is clear that there is no singularity at this location.\) Checking the “faithfulness” 

of a given geometry is more intricate and requires a detailed analysis similar in spirit to the discussion of the geometric boundaries of the kermit expansion in section 2.3. 

As we will explain shortly, there are “rare” cases of d log forms that give rise to faithful geometries, i.e., there is at least one set of inequalities akin to \(3.12\) for which the resulting geometry only has the geometric boundaries appearing as singularities of the form and no others. These are the spaces of our interest in this paper. 

The presence of a boundary in the geometry which does not appear as a corresponding pole in the integrand form might seem strange, but this is in fact one of the defining features of Grassmannian geometry. As a simple example, consider the four-point box integral in eq. \(3.2\). As shown earlier, one version of the d log form contains the hABXi = hAB13i bracket while the rational integrand form does not. This d log form naively implies that there are 24 = 16 different geometries, reflecting the various sign choices for the four ratios of brackets. Geometrically, each choice would give rise to the same d log form. However, these 16 geometries are all different, and some of them actually have hAB13i = 0 as a boundary despite its absence in the differential

– 26 –

form. One concrete example of this occurs for the following sign choice10

hAB12i

hAB23i

hAB34i

hAB14i

> 0, 

> 0, 

> 0, 

< 0. 

\(3.13\)

hAB13i

hAB13i

hAB13i

hAB13i

We can always fix one of the brackets to have a definite sign, as the only relevant information is encoded in the ratios. Fixing the sign of hAB12i > 0 then implies that all four-brackets appearing in eq. \(3.13\) are positive, except for hAB14i, which is negative. The geometric region associated to the sign choice eq. \(3.13\) still has eq. \(3.2\)

as the logarithmic form, but geometrically we can now access the hAB13i = 0 boundary without violating any of the inequalities. We can see this fact explicitly in coordinates: expanding ZA = Z3 \+ xZ1 \+ yZ2, and ZB = Z4 \+ zZ1 \+ wZ2 the inequalities eq. \(3.13\)

are equivalent to

x > 0, y < 0, w > 0, \(xw − yz\) > 0. 

\(3.14\)

In this parametrization we have hAB13i = −yh1234i, so accessing the boundary corresponds to setting y → 0. In this case, the only remaining inequality sensitive to this choice is xw − yz → xw > 0, which is clearly consistent with x, w > 0. Therefore, hAB13i = 0 is an accessible boundary of the geometry. Since this singularity is absent in the differential form, we conclude that this geometry is not faithful according to our definition above. 

However, if we instead choose the geometric space where all ratios appearing in eq. \(3.13\) are positive, in the parametrization above the space becomes x > 0, y < 0, w < 0, \(xw − yz\) > 0 , 

\(3.15\)

i.e., we now have the opposite sign for w < 0. This time, sending y → 0 yields the three inequalities x > 0, w < 0 and xw > 0, which are clearly incompatible, thus demonstrating that y = 0 \(and therefore hAB13i = 0\) is not a geometric boundary of the space. According to our definition above, we would call the positive geometry associated to this choice of inequalities faithful. 

In summary, we see that each d log form gives rise to a large set of geometric spaces \(one for each sign choice of the ratios of four-brackets appearing in the d log form\) which all have the same integrand form. However, only a subset of these spaces are free of unphysical boundaries. For admissible \(faithful\) positive geometries, we demand that all boundaries of the space are directly reflected in the pole structure of the integrand form. This is true for the Amplituhedron, and we want to preserve this property here. 

10Let us note that for the ‘local spaces’ we define in this work, we do not insist on hABii\+1i > 0

which was a crucial part of the Amplituhedron definition \(2.12\). We comment on this in section 3.3. 

– 27 –

Faithful geometries from the chiral pentagon d log form For the generic chiral pentagon of eq. \(3.3\), we found two possible d log forms in eqs. \(3.3\) and \(3.4\). Starting with the original d log form in eq. \(3.3\) and checking the boundary structure of the 24 geometries arising from the respective sign choices for the entries of the d logs, we find that none of these spaces gives rise to a faithful geometry, i.e., these spaces always have certain additional geometric boundaries that do not appear as singularities of the form and are therefore unacceptable to us. 

This encourages us to consider our novel d log form presented in eq. \(3.4\). While the rational integrand in eq. \(3.3\) does not have the spurious poles hAB\(n1i\)∩\(ij?\)i or hAB\(n1j\)∩\(ij?\)i, certain sign choices for the arguments of the d log form in eq. \(3.4\)

do lead to geometric spaces with boundaries when \(AB\) intersects the lines \(n1i\)∩\(ij?\) or \(n1j\)∩\(ij?\). Only the special sign combinations where the spurious boundaries are geometrically absent are of our interest. In this case, there are exactly two choices of signs for the ratios of four-brackets in the d log form eq. \(3.4\) which do have the correct boundary structure to represent a faithful geometry. 

The two possibilities

correspond to choosing the reference point Z? to be either in the set Z?∈\{i\+1, . . ., j−1\}, or Z?∈\{1, . . . , i−1\}∪\{j\+1, . . . , n\}.11 In the first case, Z? ∈ \{i\+1, . . . , j−1\}, we find a consistent geometry defined by the following set of inequalities

hABi−1ii

hABj−1ji

hAB\(n1i\)∩\(ij?\)i

hAB\(n1j\)∩\(ij?\)i



<0, 

<0, 

<0, 

>0

. \(3.16\)

hABii\+1i

hABjj\+1i

hAB1ni

hAB1ni

We fix the sign of hAB1ni > 0 which in turn fixes the signs for the brackets with intersections, but leaves four options for the signs of the four individual propagator-type brackets, \{hABi−1ii, hABii\+1i, hABj−1ji, hABjj\+1i\}. As a result, the first consistent chiral pentagon space is a union of four sign patterns:

hABi−1iihABii\+1ihABj−1jihABjj\+1ihAB1nihABXiihABXji

−

\+

−

\+

\+

−

\+

P \(1\) ↔

\+

−

−

\+

\+

−

\+

\(3.17\)

ij

−

\+

\+

−

\+

−

\+

\+

−

\+

−

\+

−

\+

where we denoted Xi = \(n1i\)∩\(ij?\) and Xj = \(n1j\)∩\(ij?\). 

11Here, we restrict ourselves to simple momentum twistor choices for Z? that are already part of the diagram. We do not exclude the possibility that there may exist more complicated choices that yield additional choices satisfying our boundary structure criterion. Furthermore, it is also possible that there are other representations of the chiral pentagon d log form that opens up yet more options. 

It would be interesting to prove exhaustively what the set of the most general geometries that can consistently be assigned to the pentagon integrand are. 

– 28 –

The second consistent option we found is to pick ? ∈ \{1, . . . , i−1\},12 together with the following signs for the ratios of four-brackets in the d log form eq. \(3.4\)

hABi−1ii

hABj−1ji

hAB\(n1i\)∩\(ij?\)i

hAB\(n1j\)∩\(ij?\)i



<0, 

<0, 

>0, 

>0

. \(3.18\)

hABii\+1i

hABjj\+1i

hAB1ni

hAB1ni

One can check that out of the four possibilities for the signs of individual four-brackets consistent with the ratios eq. \(3.18\), only one region is actually non-empty, and we get hABi−1iihABii\+1ihABj−1jihABjj\+1ihAB1nihABX

P \(2\) ↔

iihABXj i

\(3.19\)

ij

−

\+

\+

−

\+

\+

\+

When some legs of the pentagon become massless, there are degenerate configurations which allow more sign choices in the d log form eq. \(3.4\) than in the generic case. However, upon gluing different integrands, none of these choices lead to a global geometry which is free of spurious boundaries. We return to this point in greater detail in section

5 as well as appendix D. 

Faithful geometries from the box d log form

A particular degeneration of the chiral pentagon in eq. \(2.45\) leads to the two-mass-hard integral which arises as a special case, j = i\+1. The d log form for the general box integral is similar to eq. \(3.2\). In the context of the two-mass-hard box, it reads hABd2AihABd2Bihi−1ii\+1i\+2ih1ii\+1ni

Ω\(n\) =

=

\(3.20\)

ii\+1

hABi−1iihABii\+1ihABi\+1i\+2ihAB1ni

hABi−1ii

hABii\+1i

hABi\+1i\+2i

hAB1ni

= d log

d log

d log

d log

, 

hABXi

hABXi

hABXi

hABXi

where X is one of the two solutions of the quadruple cut of the box, 

↔ Xi = \(ii\+1i\+2\)∩\(in1\), 

or

↔ Xi\+1 = \(i−1ii\+1\)∩\(i\+1n1\) . \(3.21\)

12In fact, we can also choose ? ∈ \{\(j\+1, . . . , n\}, for which the inequalities of the last two ratios in eq. \(3.18\) flip sign. For this option the geometric space is identical to the one defined by eq. \(3.18\). 

As such, it is just a different representation of the same geometry. 

– 29 –

We now repeat the same exercise as for the chiral pentagon and determine the consistent positive geometries associated to this d log form. As it turns out, fixing one of the signs of the brackets involving either Xi or Xi\+1 is sufficient to specify the space, as one inequality automatically enforces the other. Fixing hAB1ni > 0 then forces hABXi to have a definite sign depending on the sign of the ratio in the last d log. We find two different consistent sign choices for the ratios of the d logs in eq. \(3.20\), both of which have fixed signs for the hABii\+1i brackets of the diagram. The first region is given by: hABi−1iihABii\+1ihABi\+1i\+2ihAB1nihABX

B\(1\)

↔

iihABXi\+1i

\(3.22\)

1i−1,i\+2 n

−

\+

−

\+

\+

−

Consistent with the statements above, let us reiterate that fixing the sign of only one of the brackets hABXii or hABXi\+1i together with the signs of the propagator brackets is sufficient to fix the region; the sign of the other bracket is implied by the rest. 

The second allowed region has the same signs as in eq. \(3.22\) for the first four brackets, but the signs for hABXii < 0, hABXi\+1i > 0 are flipped. 

hABi−1iihABii\+1ihABi\+1i\+2ihAB1nihABX

B\(2\)

↔

iihABXi\+1i

\(3.23\)

1i−1,i\+2 n

−

\+

−

\+

−

\+

Note that the union of the two regions eq. \(3.22\) and eq. \(3.23\) constitutes a larger achiral geometric region defined only by the first four inequalities with no constraints on hABXii and hABXi\+1i. The canonical form for this achiral region trivially vanishes because four inequalities are insufficient to produce a non-trivial d log form \(simply because we cannot form four independent ratios\). Therefore, this achiral space is a particular example of a zero-form space defined in subsection 2.1. The larger space can be sliced into two subspaces by fixing the sign of hABXii, corresponding to exactly the two chiral subspaces we found in eq. \(3.22\) and eq. \(3.23\). Because the form for the achiral space vanishes, both subspaces have the same form \(up to a sign\). We can once again illustrate this feature of zero-form spaces with a simple two-dimensional example in the xy-plane. The space defined by −∞ < x < ∞, 0 < y < b has zero canonical form, so cutting the space into two pieces with x ≶ a, the respective canonical forms Ω<, Ω> differ only by a sign:

. 

−→

\(3.24\)

slicing

dx dy

dx dy

Ω = 0dddddddddddddi −→ Ω< \+ Ω> =

−

\(x−a\)y\(y−b\)

\(x−a\)y\(y−b\)

– 30 –

We can also use an alternative d log form representation for the box integrand derived directly from the degeneration of the chiral pentagon eq. \(3.4\) by setting j = i\+1. 

For this leg configuration, the integrand form eq. \(3.3\) na¨ıvely generates a double pole hABii\+1i in the denominator. However, the chiral numerator exactly cancels one power of this pole so that we end up with a two-mass-hard box. The resulting d log form obtained by this procedure has different arguments than eq. \(3.20\), but reproduces the same rational integrand. This is in complete agreement with our earlier statements about the non-uniqueness of d log representations. 

If we repeat the exercise of subsection 3.2 to associate consistent geometric regions with the appropriate boundary structure to the d log form, we find exactly the same geometric regions as in eq. \(3.22\) and eq. \(3.23\), albeit described by different inequalities. 

The brackets involving the lines Xi = \(n1i\)∩\(ii\+1?\) and Xi\+1 = \(n1i\+1\)∩\(ii\+1?\) in-herited from the pentagon simply provide an equivalent description of the same spaces. 

Once again, this simply reflects the non-uniqueness of the d log form of an integrand, and emphasizes that demanding we get the geometry correct \(rather than just the form\) is a very strong constraint. More generally, we expect \(but have no proof\) that alternative d log forms for the local integrals discussed in this section will not yield any new consistent geometries. 

In addition to the two-mass hard box discussed above, the only other box topology relevant for the local expansion eq. \(2.45\) are “one-mass” boxes. The first of these arises as a boundary term when i = n−2, j = n−1. The second one-mass box is a degeneration of the pentagon when i = 2, j = 3, and can be obtained by trivial relabelling. 

B1 n−3 =

, 

B4n =

. 

\(3.25\)

The one-mass geometries with the correct boundary structure can be specified by imposing conditions on the propagators appearing in the diagram, as well as one bracket involving \(one of\) the solutions to the quadruple cut. Thus, for e.g., B1 n−3 in eq. \(3.25\)

we can define the space by correctly choosing the signs of

\{hABn−3n−2i, hABn−2n−1i, hABn−1ni, hAB1ni\}

and

hABn−2ni. 

\(3.26\)

In the two-mass hard case there was only one choice of signs for the list of propagators i.e., eq. \(2.29\) and eq. \(3.23\) differed only in the signs of the brackets hABXii and

– 31 –

hABXi\+1i. In the one-mass case, both sign choices for the bracket hABn−2ni are also allowed. In addition, there are two allowed choices for the signs of the sequence of brackets in eq. \(3.26\) which are geometrically free of spurious boundaries—giving a total of four consistent spaces. The first two can be written compactly as hABn−3n−2ihABn−2n−1ihABn−1nihAB1nihABn−2ni

B\(1,2\) ↔

, 

\(3.27\)

1n−3

\+

−

−

\+

±

while the second pair of solutions is

hABn−3n−2ihABn−2n−1ihABn−1nihAB1nihABn−2ni

B\(3,4\) ↔

. 

\(3.28\)

4 n

−

\+

−

\+

±

In subsections 5.3 and 5.4 we consider the problem of combining the geometries associated to individual terms in the chiral pentagon expansion of the MHV one-loop integrand eq. \(2.45\). A priori, we have no reason to prefer any one of the individually well-defined spaces we have just constructed. Remarkably, however, as we shall demonstrate in section 5, it turns out that demanding a sensible global geometry whose boundary structure is identical to that of the original Amplituhedron is restrictive enough to give a unique choice for the one-mass, the two-mass hard, as well as the chiral pentagon spaces subject to the assumption that we treat all graph isomorphic topologies in a uniform way. 

Faithful geometries from the chiral hexagon d log form

In this subsection, we consider the problem of assigning faithful geometries to logarithmic forms more generally. The first example which goes beyond the results of the previous two subsections is the chiral hexagon, 

hABd2AihABd2Bi hAB24ihAB51i

Ωhex =

=

. 

\(3.29\)

hAB12ihAB23ihAB34ihAB45ihAB56ihAB16i

To identify some candidate geometries the most natural starting point is, as we have seen, a rewriting of this integrand as a single d log form. For integrals with more than five local poles, any such form must involve at least one ratio in which both

– 32 –

the numerator and denominator depend quadratically on \(AB\). For the hexagon of eq. \(3.29\) our starting point is a novel expression which is a single d log form, hAB13i

hAB34i

hAB46i

hAB23ihAB16i

Ωhex = d log

d log

d log

d log

. 

\(3.30\)

hAB23i

hAB45i

hAB56i

hAB12ihAB36i

Demanding that the geometry defined by sign conditions on the four ratios in this expression be faithful requires that the three codimension-one loci hAB13i=0, hAB46i=0

and hAB36i=0 do not appear as boundaries of the space. There are two sign choices which accomplish this:

hAB13i

hAB34i

hAB46i

hAB23ihAB16i



H\(1\) =

< 0, 

< 0, 

< 0, 

> 0

, 

\(3.31\)

hAB23i

hAB45i

hAB56i

hAB12ihAB36i

hAB13i

hAB34i

hAB46i

hAB23ihAB16i



H\(2\) =

< 0, 

< 0, 

> 0, 

> 0

. 

\(3.32\)

hAB23i

hAB45i

hAB56i

hAB12ihAB36i

Decomposing H\(i\) into subspaces where all brackets appearing in the ratios have fixed sign, we na¨ıvely generate a considerable number of non-overlapping regions. Although this is indeed the case for H\(2\), the first solution is surprisingly equivalent to a single region described by significantly simpler inequalities

n

H\(1\) =

hAB12i < 0, hAB23i > 0, hAB34i > 0, hAB45i < 0, 

\(3.33\)

o

hAB56i > 0, hAB16i > 0, hAB14i < 0 , 

which will arise in a different context in section 4 below. 

3.3

No-go theorem for external triangulation

In all previous cases, assigning a sensible \(faithful\) geometric space to a given d log form led us to consider situations where at least a subset of signs of hABii\+1i were negative. In particular, for all faithful geometries of the local integrands, we did not encounter any region for which all such brackets were positive. On the other hand, the Amplituhedron itself is defined with all hABii\+1i > 0, and is cut further either by the sign-flip conditions in eq. \(2.10\) or by the positivity of hABiji > 0 in eq. \(2.31\). This means that all geometric regions we discussed in the context of the chiral pentagon expansion are outside the Amplituhedron. 

It is actually very easy to see that even if there was some other d log representation for the pentagon or boxes, with correspondingly different geometric regions, they can not possibly be even partially inside the Amplituhedron space for the following reason: In order to fix, e.g., the MHV \(or MHV\) Amplituhedron space, we need to specify

– 33 –

n − 3 conditions in addition to the positivity of all hABii \+ 1i > 0. While there are many equivalent ways how to express these conditions, e.g., via sign flips in the sequence

\{hAB1ii\}i=2,...,n, or via sign flips in the sequence \{hAB2ii\}i=3,...,n,1, or via the positivity of hABiji > 0, we always need at least n − 3 of them. This number is irreducible and cannot be decreased. If we attempted to specify fewer conditions, the resulting space would lie inside the Amplituhedron, alas it would contain spurious boundaries. One example of this scenario is given by the individual sign-flip spaces associated to the BCFW Kermits eq. \(2.19\). The unique space with only physical boundaries inside the Amplituhedron is the whole Amplituhedron itself, and can not be cut into smaller spaces with purely physical boundaries. 

A natural follow-up question is whether or not the Amplituhedron can be contained inside a space whose logarithmic form is given by the chiral pentagon or the box. While the logarithmic form for the Amplituhedron is generally very complicated, combining the Amplituhedron space with many other spaces outside can lead to a simpler space whose form can be as simple as that of the chiral pentagon or the box. In our two-dimensional geometry toy example in subsection 2.4, this is precisely what happened in the external triangulation of the quadrilateral on the left-hand-side of eq. \(2.46\). 

There, adding a triangle outside the space gave rise to a larger triangle, for which the logarithmic form would be simpler than the one for the quadrilateral itself. So the question is whether or not we can replicate something similar for the Amplituhedron. 

For the simplest five-point case, the answer is yes. For n > 5, however, this is no longer true and there is no consistent local space based on the pentagon d log form which contains the Amplituhedron space. This can be understood heuristically by noting that in the n-point case, to define pentagon geometries that contain the amplitude we would need n−3 extra conditions, analogous to the intersections appearing in eq. \(2.31\). 

However, the d log form of the pentagon contains only four ratios of brackets, indicating that the set of conditions defining the pentagon should not grow with n. Thus, without resorting to increasingly complicated ratios of brackets at higher multiplicities a simple pentagon space cannot possibly contain the complicated Amplituhedron. The n=5 case is exceptional, as the two conditions required to cut out the Amplituhedron matches the number of conditions required to define the pentagon. 

This argument suggests the chiral pentagon expansion cannot represent a geometric triangulation \(internal or external\) of the Amplituhedron. As we will see later in section

5, the chiral pentagons triangulate a different region which has only physical boundaries and has \(almost\) all the same properties as the Amplituhedron. However, our suspicion, for which we give evidence in section 6, is that the primary purpose of the pentagons is to internally triangulate the dual Amplituhedron. 

– 34 –

4

Sign-flip regions

In this section we take a step back from the chiral pentagon expansion, and look more generally at the positive geometries which arose in the study of the local integrands, such as eqs. \(3.17\), \(3.19\), \(3.22\), \(3.23\), \(3.27\) and \(3.28\). In particular, we constructed spaces with only physical boundaries that were defined by both positive and negative signs of various hABii\+1i brackets. In \[77\] we provided an intriguing classification of these geometries using certain sign-flip conditions which are reminiscent of, but distinct from, the sign-flip characterization of the Amplituhedron \[19\]. In this section we will review these results and provide further discussions and elaborate on the properties of the various sign-flip spaces. 

Classification of sign-flip regions

In the first step we discuss achiral positive spaces that are defined by imposing fixed signs for hABii\+1i brackets only, without further constraints on any other four-bracket. 

In other words, we study geometric regions defined by the following set of n signs for the sequence of brackets

S=hABii\+1i 

:=hAB12i, hAB23i, . . . , hAB1ni . 

\(4.1\)

i∈\{1,...,n\}

From the study of the Amplituhedron, we already know of one example of such a region: the union of the MHV and MHV one-loop spaces. The corresponding logarithmic form is the parity-odd amplitude, which is given by the sum of MHV and MHV one-loop amplitudes in eq. \(3.10\) \(defined with appropriate sign\). This function integrates to zero on the parity-invariant Feynman contour. However, from a geometric point of view, it is the most natural space we can consider where all signs in S are positive, S\(0\) = \{\+, \+, . . . , \+\}. 

\(4.2\)

For obvious reasons, we also call S\(0\) a sign-flip-zero region because the sequence S has no sign flips. By drawing the n points on a circle, we can represent the sign-flip-zero space as

S\(0\) =

. 

\(4.3\)

– 35 –

where the \+ sign between points 1 and 2 denotes hAB12i > 0, and similarly for the other brackets. The only subtlety arises when we reach the arc from n to 1, where we draw a \+ sign to denote the positivity of hABnˆ

1i = hAB1ni in line with the twisted

cyclic symmetry. 

Following the same logic, we define a sign-flip-two region as sequence of signs S\(2\) =

, 

\(4.4\)

ij

where the labels i and j denote the two positions where the first and second sign flip occurs, respectively. In particular, this implies that

\{hABi i\+1i, hABi\+1 i\+2i, . . . , hABj−1ji < 0\}, 

\(4.5\)

\{hABjj\+1i, hABj\+1j\+2i, . . . , hABi−1ii > 0\}, 

where the labels 1 and n can be in either the positive or negative regions13 \(appropriately taking into account the twisted cyclic symmetry as commented on above\). 

Next, we define a sign-flip-four region with i, k, \`, j labelling the four positions where the signs in the sequence eq. \(4.1\) flip, 

S\(4\) =

. 

\(4.6\)

ik\`j

Na¨ıvely, we can continue to consider sequences of brackets eq. \(4.1\) with ever more sign flips. Remarkably, all higher sign-flip patterns correspond to empty geometric regions. 

Sign-flip-zero regions

All the sign-flip-zero, two, and four spaces are positive geometries; as such, all of these spaces have associated canonical forms with only logarithmic singularities on all 13As written, eq. \(4.4\) and eq. \(4.5\) suggest that i < j and therefore hAB1ni > 0 is in the positive region. In general, spaces hAB1ni < 0 presents no additional complications whatsoever, although we will have no use for them in this paper. 

– 36 –

boundaries. By definition, all codimension-one boundaries of the achiral spaces defined in the previous subsection have to be of the form hABii\+1i = 0. Na¨ıvely, one may expect that, at n points, all such inverse propagators hAB12i, . . . , hAB1ni will indeed be boundaries of the spaces leading to very complicated canonical forms. For the sign-flip-zero space, this is true: the associated form has n poles

N \(0\)

S\(0\) =

↔

. 

\(4.7\)

hAB12ihAB23i · · · hABn−1nihAB1ni

This means the complexity of the numerator of the canonical form grows with n, just as the complexity of MHV and MHV amplitudes does. This should not be surprising, because both of these chiral amplitude spaces in fact live inside the larger achiral space S\(0\)\! The MHV amplitude is the subspace of the achiral space defined by the additional conditions \(i\) hABiji > 0, eq. \(2.31\), while the parity conjugate MHV space uses \(ii\) hABiji > 0, eq. \(2.32\). It is quite nontrivial that imposing either set of these conditions does not introduce new codimension-one boundaries. In fact, it is straightforward to verify there is no way to impose a mixed set of conditions of type \(i\) and \(ii\), without at least one of these conditions becoming a boundary. Thus, we may think of the achiral space as having two components, neither of which has any spurious boundaries; for obvious reasons, we refer to these as chiral components. 

In other words, we can cut the sign-flip-zero space defined by hABii\+1i > 0 into two chiral components which are MHV and MHV Amplituhedra. Both of these spaces have only physical boundaries. As alluded to in subsection 3.3, we need to impose n−3

conditions to specify either one of these spaces. 

Interestingly, the achiral sign-flip zero space can be externally triangulated in terms of simpler spaces. In fact, the “parity-odd” pentagon expansion in eq. \(3.10\) exactly gives this geometric triangulation:

=

. 

\(4.8\)

– 37 –

Each parity-odd pentagon corresponds to a positive geometry with only five boundaries. 

The terms in the set are overlapping and provide an external triangulation of S\(0\). On the right-hand-side of eq. \(4.8\), ∗ = \+ ⊕ − instructs us to marginalize over both signs of the corresponding bracket. More details, including the derivation of \(4.8\) are given in appendix B. As argued above, the same procedure does not work for chiral spaces, and the chiral pentagon expansion does not provide an external triangulation of the Amplituhedron. We will get back to the precise rôle of this expansion in the next section. 

Sign-flip-two regions

Let us continue our discussion with the achiral sign-flip-two regions defined in eq. \(4.4\)

and eq. \(4.5\). First, one can check that this space has all n codimension-one boundaries so that the logarithmic form a priori has a similar structure as the one of S\(0\) in eq. \(4.7\), 

but with a different numerator. 

However, something surprising happens when we slice the achiral sign-flip-two region eq. \(4.4\) into smaller components. First, similar to the sign-flip-zero case we find that the sign-flip-two region can be again cut into two chiral components without introducing spurious boundaries. Na¨ıvely, we would expect that in order to specify each subspace we have to impose O\(n\) additional inequalities, but in fact only a single inequality suffices; for the sign-flip-two space eq. \(4.4\) the chiral components correspond to the two signs of the bracket hABiji ≷ 0, which we represent diagrammatically as S\(2\),± =

, 

for i < j . 

\(4.9\)

ij

This additional inequality is very natural as i and j are the positions where the two sign-flips occur. 

Looking more closely at one of the subspaces defined by hABiji>0, we find two interesting features: First, all brackets inside the “plus region” have fixed positive sign, hABpqi > 0 and hABpqi > 0, 

\(4.10\)

for p < q and p, q ∈ \{j, j\+1, . . . , i−1, i\}. No similar statement is true for the indices inside the “minus region.” Second, from the collection of terms hABpqi inside the plus region only the boundary terms hABjj\+1i and hABi−1ii represent boundaries. In

– 38 –

other words, hABpp\+1i for p ∈ \(j\+1, . . . , i−2\) are not poles of the logarithmic form. 

Therefore, the canonical form for this chiral region is considerably simpler, N \(2\),\+

S\(2\),\+=

↔

ij

. 

\(4.11\)

ij

hABii−1ihABii\+1i· · ·hABj−1jihABjj\+1i

In the general n-point case the form eq. \(4.11\) is still non-trivial and we will give a precise formula and its derivation in eq. \(B.16\) of appendix B. For some special cases, the structure of the form simplifies considerably. In particular, if the ‘−’ region shrinks, the number of poles decreases, as does the complexity of the form. For the special case where j = i\+2 there are only two negative brackets, hABii\+1i, hABi\+1i\+2i < 0, which means that the chiral sign-flip-two space has only four boundaries and the logarithmic form must be a box. 

hi−1 i i\+1 i\+2ihi i\+1 i\+2 i\+3i

S\(2\),\+ =

↔

i i\+2

hABi−1iihABii\+1ihABi\+1i\+2ihABi\+2i\+3i

\(4.12\)

=

. 

If we shrink the ‘−’ region even further and consider j=i\+1, the negative region consists of a single term, hABii\+1i<0, i.e., 

↔

0. 

\(4.13\)

Note, however, that this bracket hABii\+1i is exactly the one used to cut the space into chiral components. Therefore, the hABii \+ 1i > 0 subspace is actually empty, i.e., the

– 39 –

achiral space is now a single region which cannot be cut further without introducing spurious boundaries. 

Above, we have discussed S\(2\),\+ where hABiji > 0, but the same analysis can be ij

done for the opposite chirality where hABiji < 0 where the rôles of \+ ↔ − are inter-changed. Going back to the achiral space, we divide the region into chiral components, S\(2\) = S\(2\),\+ \+ S\(2\),−

ij

ij

ij

=

\+

\(4.14\)

N \(2\),\+

N \(2\),−

↔

ij

\+

ij

. 

hABi−1iihABii\+1i . . . hABjj\+1i

hABj−1jihABjj\+1i . . . hABii\+1i

While the canonical form for the achiral space eq. \(4.4\) has all hABii\+1i codimension-one boundaries present, it is in fact the sum of two simpler forms with fewer poles coming from two chiral subspaces. This feature makes the boundary structure of S\(2\) ij

simpler than that of the sign-flip-zero space S\(0\). For example, in S\(2\) there is no ij

codimension-two boundary corresponding to hABpp\+1i = hABqq\+1i = 0 where p ∈

\(i\+1, . . . j−2\) and q ∈ \(j\+1, . . . i−2\). There are several additional interesting aspects of the sign-flip-two spaces which we discuss at greater length in appendix C. 

Sign-flip-four regions

In our discussion of sign-flip-four regions we start with a few simple examples before discussing the general case \(which will be surprisingly simple\!\). Going back to our original description of one of the faithful chiral pentagon geometries in eq. \(3.19\), we see that the five-point pentagon with i = 2 and j = 4 can naturally be phrased as a chiral sign-flip-four region, 

hAB24ih1245i

↔

=

, 

\(4.15\)

hAB12ihAB23ihAB34ihAB45ihAB15i

– 40 –

where we have also indicated the additional inequalities \(hAB\(512\)∩\(241\)i > 0 and hAB\(514\) ∩ \(241\)i > 0\) imposed to define the space. Similar to what we have seen above, this is one chiral subspace of a larger achiral region defined by the signs of hABii\+1i only. In fact, the intersections appearing in eq. \(4.15\) can be replaced by a single inequality, either

hAB25i < 0 or hAB14i < 0. 

\(4.16\)

to define exactly the same space as eq. \(4.15\), 

=

. 

\(4.17\)

Note that the bracket hAB24i > 0 is positive as a consequence of the hABii\+1i signs only. From a Schouten identity, 

hAB12ihAB45i \+ hAB15ihAB24i = hAB14ihAB25i > 0, 

\(4.18\)

−

−

\+

\+

it then follows that fixing the sign of hAB14i determines the sign of hAB25i, and vice versa. Only one of the two four-brackets is necessary to define the chiral sign-flip-four space, and the other is redundant. The five-point pentagon eq. \(4.15\) space has both signs negative, while the second chiral subspace \(which corresponds to the opposite chirality pentagon diagrammatically represented by a dashed line\) has both

– 41 –

signs positive, 

hAB24ih1245i

↔

≡

, \(4.19\)

hAB12ihAB23ihAB34ihAB45ihAB15i

hAB24ih1235ih1345i

↔

≡

. \(4.20\)

hAB12ihAB23ihAB34ihAB45ihAB15i

The union of these two spaces is a larger achiral space whose form is the difference of the two chiral pentagons, earlier introduced as parity-odd pentagon eq. \(3.8\), 

N

↔

odd

, 

\(4.21\)

hAB12ihAB23ihAB34ihAB45ihAB15i

where the numerator is Nodd = hAB24ih1245i − hAB24ih1235ih1345i. 

Our next example is the achiral six-point region which can likewise be cut into two chiral components using a single additional inequality, 

=

\+

, 

\(4.22\)

where, again, the signs of the “diagonal brackets” are either both positive or both negative as a consequence of a Schouten identity. Calculating the forms associated to

– 42 –

these spaces, we find two chiral hexagons which were introduced in \[72\] as examples of IR-finite integrands, 

hAB24ihAB51i

↔

≡

, 

\(4.23\)

hAB12ihAB23i · · · hAB16i

hAB24ihAB51ih3456ih6123i

↔

≡

. 

\(4.24\)

hAB12ihAB23i · · · hAB16i

Finally, we consider an additional six-point region corresponding to yet another chiral pentagon integrand:

hAB25ih1256i

↔

≡

. 

hAB12ihAB23ihAB45ihAB56ihAB16i

\(4.25\)

We see the same pattern as in the sign-flip-two spaces: inside the ‘\+’ region the “inner boundaries” are absent; e.g., in eq. \(4.25\), hAB34i is not a pole of the form nor a boundary of the geometric space. 

Having discussed several illuminating examples at low multiplicity, we are now

– 43 –

ready to present the general sign-flip-four case:

S\(4\),± =

. 

\(4.26\)

ik\`j

where the large achiral region S\(4\) of eq. \(4.6\) is cut into two chiral subspaces by ik\`j

specifying the signs of hABiì or hABkji. In one subspace they are both positive while in the other they are both negative. In addition, all signs are uniformly fixed inside the four sign sectors. For example, all brackets of the form

hABpqi, hABpqi > 0

for p < q ∈ \{j, j\+1, . . . i\}, 

\(4.27\)

are positive, whereas the analogous brackets in the “minus region” are negative. We give further details on the fixed sign structure in appendix C. Practically, this means that the only boundaries from each of these sectors are the ones adjacent to the sign-flip positions, so the logarithmic form has exactly eight boundaries in the general case. In fact, each chiral component can be identified with a chiral octagon integrand

←→

, 

\(4.28\)

where the wavy and dashed lines indicate the respective numerators \[72\], 

hABijihABikihABkìhAB\`ji

ω\(4\),−=

. 

\(4.29\)

ik\`j

hABi−1iihABii\+1ihABk−1kihABkk\+1i

×hAB\`−1ìhAB\`\`\+1ihABj−1jihABjj\+1i

– 44 –

The form for the other chiral space, ω\(4\),\+, for which hABiì, hABkji > 0, is obtained ik\`j

by flipping the wavy and dashed lines. The chiral octagons were introduced in \[72\]

as the one-loop integrand basis elements which split the basis into parity-odd \(which integrate to zero\), IR-finite and IR-divergent integrands. While the expression for the integrand may look complicated, because of the special form of the numerator in the generic case the integrand is IR finite and evaluates to a simple combination of dilogarithms. It is very surprising that we see the same objects here in a very different setup as the integrand forms for maximal sign-flip regions. 

The chiral octagons naturally degenerate to simpler spaces when the labels i, k, \`, j become adjacent. Exactly the same happens with our regions as well, and we can indeed identify the pentagon and hexagon examples discussed above as boundary cases of the generic octagon. 

5

Local geometries and the Amplituhedron-Prime

Having discussed various aspects of more general sign-flip spaces, let us come back to the local integrands of section 3 that enter the chiral pentagon expansion of the one-loop MHV amplitude, eq. \(2.45\). After a careful analysis of consistent sign patterns for the individual local geometries, we concluded in section 3 that there are only two faithful geometric spaces which can be associated with the general chiral pentagon eqs. \(3.17\)

and \(3.19\), two choices for the two-mass-hard boxes eqs. \(3.22\) and \(3.23\), and four choices for the one-mass boxes eqs. \(3.27\) and \(3.28\), respectively. 

In the next step we discuss how to glue these geometric regions together. We are going to show that only a single choice for the pentagon and box spaces is globally consistent \(at all multiplicities\) upon gluing. By consistency, we mean the requirement that there are no unphysical boundaries left in the resulting geometry akin to our discussion of faithful geometries in section 3.2. As a tool, we make use of the classification of all relevant positive geometries in terms of the sign-flip-two and four regions summarized in sections 4 and appendix B. This allows us to write a \(conjectured\) closed formula for the final geometric space in eq. \(5.32\). 

The primary result of this section is a new positive geometry, which we name the Amplituhedron-Prime, comprised of a particular collection of chiral sign-flip-two and four regions with only physical boundaries of all codimensions. While this new space has exactly the same singularity structure as the Amplituhedron, their bulk geometries are entirely non-overlapping. This follows directly from the fact that the original Amplituhedron is comprised of a single chiral sign-flip-zero space. 

– 45 –

5.1

Chiral regions for boxes and pentagons

We start our discussion with the five-point one-loop MHV amplitude. Specializing eq. \(2.45\) to n=5, the integrand is a sum of one chiral pentagon and two boxes, ω\(5,0,1\) =

\+

\+

. 

\(5.1\)

The first box in this expression, which we label as B12, has four individually well-defined faithful geometries as described in eqs. \(3.27\)–\(3.28\), where the sign of the bracket hAB12i is unfixed. In section 3 we constructed the candidate spaces for the box \(all of which had no spurious boundaries\) by imposing conditions on hABii\+1i brackets as well as additional conditions involving its leading singularities. By expanding the unfixed sign ∗ = \+ ⊕ −, it is straightforward to identify all four choices as particular instances of sign-flip-two and four spaces described in section 4. For the box B12 we may write the options as

B\(1\) =

, 

B\(2\) =

, 

12

12

\(5.2\)

B\(3\) =

, 

B\(4\) =

. 

12

12

Note that for the choice labelled B\(1\), the missing space where hAB12i < 0 is empty. 

12

The additional inequality hAB35i ≶ 0 is needed to select one of the chiral components of the larger achiral space. As we stressed above, all four spaces B\(i\) are a priori locally 12

satisfactory as they have the correct boundary structure to represent the associated integral. However, this box has singularities which are absent in the MHV one-loop integrand. Indeed, we consider such singularities spurious from the point of view of the

– 46 –

global geometry of the Amplituhedron. Thus, the manner in which B12 glues together with the other terms in eq. \(5.1\) must be such that all spurious singularities cancel and we are left with exactly the physical singularity structure of the MHV Amplituhedron. 

The discussion of the other box integrand, B45, is analogous and we once again have four different options:

B\(1\) =

, 

B\(2\) =

, 

45

45

\(5.3\)

B\(3\) =

, 

B\(4\) =

. 

45

45

Although this suggests a total of 42 possible choices for combining the two boxes, in our analysis below we will only consider the four choices \{B\(i\), B\(i\)\}. This corresponds 12

45

to assigning uniform geometries to all permutations of one-mass boxes. While at five points it is possible to mix-and-match the box spaces and get a consistent global geometry, this is simply due to the degenerate kinematics and does not extend to the all multiplicity case. 

For the pentagon space, we have two possibilities which are geometrically consistent, as discussed in subsection 3.2. In this discussion we carved out the chiral spaces via inequalities involving hAB\(n1i\)∩\(ij?\)i and hAB\(n1j\)∩\(ij?\)i, where ? was in either of the two sets \{i\+1, . . . , j−1\} or \{1, . . . , i−1\}. However, it follows directly from the complete characterization of all sign-flip spaces given in section 4 that both solutions for the pentagon \(once expanded using ∗ = \+ ⊕ −\) must be a direct sum of either sign-flip-two or four chiral spaces. For the first option eq. \(3.17\) \(which corresponds to

– 47 –

the choice ? = 3\), the equivalent sign-flip characterization of the space is P \(1\)=

\+

\+

\+

24

\(5.4\)

where for brevity we simply label the sign-flip four spaces by a single non-adjacent chord of the circle. As discussed in section 4 above, a single condition is always sufficient to fix this space. The second option eq. \(3.19\) corresponds to either choice of ? = 5 or

? = 1 and is equivalent to a single chiral sign-flip-four space:

P \(2\) =

. 

\(5.5\)

24

As a result, considering a uniform choice for the one-mass boxes eqs. \(5.2\)–\(5.3\) together with the two choices for the chiral pentagon eqs. \(5.4\)–\(5.5\) yields eight possible global geometries as a result of gluing the individual spaces. Our task is to see which \(if any\) of these are consistent with the boundary structure of the original five-point MHV

Amplituhedron. This is a nontrivial constraint in spite of the fact that each individual space is free of spurious boundaries from the perspective of the individual local integrals. 

As described in appendix A, each local integral has many unphysical cuts from the perspective of the MHV one-loop geometry; a codimension-four example of this is the point \(AB\) = \(13\), which is an allowed singularity of the one-mass box B45 and the pentagon P24 but is not an allowed singularity of the MHV Amplituhedron, not allowed in MHV:

. 

\(5.6\)

In fact, while the cancellation of leading singularities is nontrivial, there is an even stronger constraint at the level of triple cuts which we explain in detail shortly. 

– 48 –

5.2

Two-dimensional projections

In deciding which individual geometric spaces can be consistently glued together, it is best to focus on certain two-dimensional boundaries where everything can be visualized geometrically as regions, lines, and points in the projective plane. The codimension-two boundaries of interest corresponds to configurations in momentum twistor space where the line \(AB\) intersects two adjacent lines \(i−1i\), \(i i\+1\). Codimension-two boundaries of this type are defined by solutions to hABi−1ii = hABii\+1i = 0. 

As discussed in more detail in appendix A in eqs. \(A.4\) and \(A.6\) there are two solutions to these conditions, the first of which has the geometric interpretation that the line \(AB\) passes through the point Zi. On this boundary, there are four codimension-three boundaries which correspond to setting one of the remaining three hABjj\+1i=0

together with one additional boundary which corresponds to setting hABi−1i\+1i=0. 

Geometrically, this additional cut forces \(AB\) to also lie in the plane \(i−1ii\+1\). Physically, this special configuration is a collinear cut, see eq. \(A.7\). We can furthermore look at all the higher-codimension residues that are accessible for MHV and MHV amplitudes. This can be summarized in the following picture of on-shell functions that label the respective cut solutions \[48\]. 

⟨ *A*

⟨ *AB* 45⟩ = 0

*B* 34⟩ = 0

⟨ *AB* 13⟩ = 0 ⟨ *AB* 15⟩ = 0

⟨ *AB* 15 ⟨ *AB* 34⟩

0

⟨ *A*

⟩ =

= 0

⟨

*B*

*A*

34

0

*B*

⟩=

⟩

15

\(5.7\)

=

⟨ *AB* 45⟩ = 0

⟨ *AB* 13⟩ = 0

⟨ *AB* 34⟩ =

⟩

0

0

= 0

⟨ *AB* 15

⟨ *AB* 13⟩ = 0

⟨ *AB* 45⟩ = 0

Besides the physical singularities of either MHV or MHV amplitudes depicted in eq. \(5.7\), 

there is one additional unphysical leading singularity that could in principle appear in

– 49 –

individual integrals, 

unphysical leading singularity:

. 

\(5.8\)

However, for the local representation eq. \(5.1\), this spurious singularity is absent term-by-term. Geometrically, the content of eq. \(5.7\) can be encoded in the two-dimensional configuration space for the line \(AB\) that is passing through Z2, 

←→

\(5.9\)

In this picture, lines correspond to codimension-three boundaries, i.e., configurations where \(AB\) intersects one more line in addition to passing through point Z2. The codimension-four boundaries are the points in this picture where two lines intersect, and correspond to completely fixing all four degrees of freedom in \(AB\). In other words, the line \(AB\) intersects two additional lines and passes through Z2. These vertices correspond to positions of leading singularities which are accessible from the codimension-two surface where \(AB\) = \(A2\). Note first that all triple cuts in this picture are physical, i.e., the MHV amplitude form has a non-zero residue when evaluated on all codimension-three boundaries in this picture. However, only a subset of the vertices represent actual leading singularities of the amplitude, which are what we consider physical. In particular, for the MHV amplitude only the points \(AB\) = \(ij\) are physical and all others are spurious. 

The positive geometries associated to the local integrals in eqs. \(5.2\)–\(5.5\) above correspond to regions in the plane in eq. \(5.9\), which can be identified by the signs of brackets which are nonvanishing when evaluated on the boundary \(AB\)=\(A2\). For \(AB\)=\(A2\), the non-vanishing brackets of interest are

\{hAB34i, hAB45i, hAB15i, hAB13i\}. 

\(5.10\)

– 50 –

Note that because this cut surface is defined by the conditions hAB12i=hAB23i=0, all information about the signs of these two brackets is lost upon accessing the \(AB\)=\(A2\) boundary. While the first three brackets in eq. \(5.10\) are the usual hABii\+1i propagator-type boundaries, the bracket hAB13i corresponds to a spurious codimension-one boundary that only becomes physical when evaluated on the support of this cut. On the \(AB\)=\(A2\) codimension-two boundary, sign conditions on hAB13i are equivalent to many other expressions, e.g., hAB24i → −hAB13ih2345i. 

It is a relatively simple exercise to deduce the correspondence between regions in eq. \(5.9\) and sequences of signs for the brackets in eq. \(5.10\) by looking at the relative positions of vertices with respect to certain lines and using the positivity of the external data, eq. \(2.11\). For example, the vertex \(AB\) = \(23\) is to the left of the line hAB45i. 

Taking into account h2345i > 0, we therefore conclude that the whole region to the left of the hAB45i=0 line corresponds to hAB45i > 0 while the region to the right corresponds to hAB45i < 0. Again using the vertex \(AB\) = \(23\), we get similar information about the regions where hAB15i ≶ 0. For information on hAB34i we can use the vertex \(AB\) = \(12\). Note that hAB13i vanishes for both \(AB\) = \(12\) and \(AB\) = \(23\) since both points are on this line. Instead, we can use \(AB\) = \(24\) which is on the side of hAB13i < 0. These arguments fix the labeling of all regions

←→

\(5.11\)

where we simply replace the sequence of brackets eq. \(5.10\) by their respective fixed signs in a given region. Note that since the plane is projective, certain regions “wrap around” the point at infinity and come back on the other side of the picture, and naively have all signs opposite; an example of this is region \{\+, −, \+, −\}, which wraps around at infinity to join with \{−, \+, −, \+\}. This is a simple consequence of the fact, already alluded to above in our discussion of d log forms and geometry, that it is not the inequality hABXi > 0 which is projectively meaningful, but rather an inequality involving a ratio of two four brackets, hABXi/hABY i > 0. 

In this context, this

– 51 –

means that flipping all signs in the definition of a space gives a completely equivalent description of it. In eq. \(5.11\) the regions \{\+, −, \+, −\} and \{−, \+, −, \+\} are precisely the same space. Therefore, we will use the same signs for all such instances of regions which wrap around at infinity, i.e., we identify \{\+, −, \+, −\} ∼ \{−, \+, −, \+\}. 

Note that in eq. \(5.11\) the MHV Amplituhedron corresponds to the region labelled as \{\+, \+, \+, −\}. This region is a quadrilateral with the four vertices \(12\), \(23\), \(24\) and \(25\) that correspond to the four physical leading singularities accessible from the \(AB\)=\(A2\) cut surface. In contrast, the MHV region corresponds to \{\+, \+, \+, \+\}

which is the triangle with vertices \(12\), \(23\), \(13\). 

The second solution to the cut conditions hAB12i = hAB23i = 0 has the geometric interpretation that the line \(AB\) is completely contained in the plane \(123\), 

↔

. 

\(5.12\)

Starting from the on-shell function for the double-cut, we could again write down all possible higher codimension residues that are accessible from this surface. For the sake of brevity, we refrain from doing so here and proceed directly to the geometric picture for the configuration space of the line \(AB\) that is contained in the plane \(123\). 

Analogous to eq. \(5.10\), the accessible codimension-three boundaries

\{hAB34i, hAB45i, hAB15i, hAB24i\}

\(5.13\)

correspond to lines in the two-dimensional pictures. We chose a particular bracket, hAB24i, to indicate on which side of the collinear boundary the line \(AB\) is. As mentioned above, on support of the hAB12i=hAB23i=0 cut conditions this can be re-written in various equivalent ways. The corresponding two-dimensional picture for the configuration space of the line \(AB\) ⊂ \(123\) is, 

– 52 –

←→

\(5.14\)

where we have labeled the regions in terms of the signs of the brackets in the sequence eq. \(5.13\). The MHV Amplituhedron is the region \{\+, \+, \+, −\} \(which on this cut surface has only three vertices\) while the MHV region corresponds to \{\+, \+, \+, \+\}. Note that for the MHV geometry the entire line hAB45i = 0 is an unphysical codimension-three boundary corresponding to the on-shell function

\(5.15\)

Geometrically, none of the physical leading singularities \(vertices\) lie on hAB45i=0. In the same spirit, the line hAB45i = 0 was unphysical for the MHV Amplituhedron in the previous two-dimensional picture eq. \(5.11\). 

All two-dimensional boundaries of the type where \(AB\) ⊂ \(i−1ii\+1\) or \(AB\) passes through Zi have the same geometry, and the corresponding projections can be obtained by cyclically relabelling the above examples. In principle, there is one additional class of codimension-two boundaries where we set two non-adjacent hABii\+1i brackets to zero, e.g. hAB12i=hAB34i=0. This boundary, while also two-dimensional, has a significantly more complicated stratification and is not easily visualized in the projective plane. While boundaries of this form can lead to spurious higher codimension cuts which a priori could place additional constraints on gluing together local integral spaces \(discussed in the following subsection 5.3\), we find in practice that matching all simple two-dimensional projections mentioned above is sufficient to fix a unique consistent gluing of spaces into the “Amplituhedron-Prime”. 

– 53 –

5.3

Gluing regions

While all codimension-two boundaries of the type \(AB\)⊂\(i−1ii\+1\) or \(AB\)=\(Ai\) have the same geometry, in the context of the particular local expansion eq. \(2.45\) we have to consider each case separately. The reason is that our global choice of hAB1ni>0 for the local spaces introduced in section 3.2 breaks the cyclic symmetry of the integrand and the individual contributions are different depending on the boundary we consider. 

At five points we must consider ten two-dimensional projections of the form described in section 5.2. For each projection, we demand that the combination of all local integrals has exactly the same boundary \(but not necessarily bulk\) structure as the original Amplituhedron, i.e., there are no spurious boundaries. In this section, we first give the answer for the correct spaces for the boxes and pentagons at five and six points, and subsequently state the result for the general n-point geometries. We only schematically illustrate how all spurious boundaries cancel for the final correct choice of geometries for the boxes and chiral pentagons on some representative two-dimensional planes. The details on how we find a unique solution \(under the assumptions discussed in subsection 5.1\) that holds for an arbitrary number of external points requires a careful analysis of multiple two-dimensional projections which is deferred to appendix D. 

Let us briefly start with the five-point geometries, where further details are rele-gated to appendix D. From eq. \(5.1\), there are two box integrands, B12 , B45, and one chiral pentagon P24, which we can a priori associate with a number of valid geometric spaces, see \(5.2\)–\(5.5\). Now we would like to combine these individual pieces into a single geometric object which has the same singularity structure as the original Amplituhedron. In order to find the consistent gluings which cancel all spurious singularities for the eight possible combinations of the box and pentagon spaces \{B\(i\), B\(i\), P \(1\), P \(2\)\}, 12

45

24

24

we consider projections to ten codimension-two boundaries where the loop line \(AB\) passes either through a point \(AB\) = \(Ai\) or is in a plane \(AB\) ⊂ \(i−1 i i\+1\). On these codimension-two boundaries, the configuration spaces for \(AB\) become the simple two-dimensional geometries of the form of eqs. \(5.11\) and \(5.14\). As discussed in section 5.2, in these projective pictures codimension-three boundaries are lines and codimension-four boundaries \(i.e., leading singularities\) are points. In order to determine the consistent global geometries, we demand that all spurious boundaries, i.e. 

boundaries that are not part of the original Amplituhedron, cancel. The result of this analysis is that, at five points, only two combinations of box and pentagon spaces survive:

\{B\(2\), B\(2\), P \(1\)\}, 

and

\{B\(3\), B\(3\), P \(1\)\}. 

\(5.16\)

12

45

24

12

45

24

For more details on how this was determined we refer the interested reader to appendix

D. Of these two solutions, it is the second option, \{B\(3\), B\(3\), P \(1\)\}, which generalizes to 12

45

24

– 54 –

six and higher points, as we show in appendix D. Let us briefly discuss why the second option of eq. \(5.16\) is consistent on two representative two-dimensional projections. 

For illustrative purposes, we discuss \(i\) the projection where \(AB\) ⊂ \(234\), and \(ii\) the projection where \(AB\) = \(A2\). Physically, from the on-shell function point-of-view these correspond to, 

and

\(5.17\)

On these two-dimensional boundaries the local spaces of eqs. \(5.2\)–\(5.5\) correspond to certain regions in the projective plane which are labeled by the signs of non-vanishing brackets in the sequences \{hAB45i , hAB15i , hAB12i , hAB35i\} and eq. \(5.10\), respectively. The \(projections of the\) second solution of eq. \(5.16\), which correctly generalizes to the all-multiplicity Amplituhedron-Prime, are

\(5.18\)

hAB45i hAB15i hAB12i hAB35i

hAB34i hAB45i hAB15i hAB13i

B\(3\)

−

\+

\+

\+

12

B\(3\)

−

\+

\+

\+

B\(3\)

\+

\+

−

\+

45

45

−

−

\+

\+

P \(1\)

\+

\+

−

\+

24

P \(1\)

−

\+

\+

\+

\+

\+

\+

−

24

−

\+

\+

−

−

\+

\+

\+

– 55 –

where we have color-coded the regions of the relevant local spaces eqs. \(5.2\)–\(5.5\) on both \(AB\)⊂\(234\) \(l.h.s.\) and \(AB\)=\(A2\) \(r.h.s.\) codimension-two boundaries. As already mentioned below eq. \(5.11\), spaces where we flip all signs lead to equivalent geometries; therefore, we only list one representative in the tables summarizing the contributing regions of each local integrand. This is why, e.g. on the l.h.s. of \(5.18\), 

the pentagon P \(1\) fills in both regions \{\+\+−\+\} ∼ \{−−\+−\} in the above left-hand-side 24

picture. Furthermore, not all sign patterns which are present in the full local integral contribute on a given cut surface. Thus, for P \(1\) only three of the four sign patterns in 24

eq. \(5.4\) have access to the codimension-two boundary where \(AB\) ⊂ \(234\). 

In order to show the consistency of our claimed solutions eq. \(5.16\) for the local integrand spaces on this boundary, we have to identify the cancellation of the spurious hAB15i = 0 line. In the solution \{B\(3\), B\(3\), P \(1\)\} depicted on the left of eq. \(5.18\), 

12

45

24

we trivially see the cancellation of the entire spurious line, because the regions \{− −

\+−\} , \{− \+ \+\+\} , \{\+ \+ −\+\} are double-covered by parts of the pentagon spaces as well as the boxes. For the \(AB\) = \(A2\) projection depicted on the right of eq. \(5.18\), we see that after cancelling overlapping regions we are left with the union of three regions, 

\{\+ \+ −−\}, \{− − \+\+\} and \{− \+ \+−\}. While this space has the correct boundary structure, here we can see it is non-overlapping with the original Amplituhedron which is the region \{\+ \+ \+−\} on this projection. 

Thus, at five points there is only one consistent space for the pentagon and we may cancel all spurious boundaries using two different \(uniform\) choices for the boxes. 

Both choices have exactly the same boundaries as the original Amplituhedron and are completely satisfactory at this multiplicity. However, only one of these solutions generalizes to higher points. This can be seen directly at six points, where an additional constraint arises: our five-point choice must be compatible with \(at least\) one of the two spaces eqs. \(3.22\) and \(3.23\) for the two-mass hard box. 

Next, we discuss the local representation of the one-loop six-point MHV integrand ω\(6,0,1\) =

\+

\+

\(5.19\)

\+

\+

\+

. 

Let us consider the six-point analogue of eq. \(5.9\), i.e., the two-dimensional projection

– 56 –

where \(AB\) ⊂ \(234\). 

←→

\(5.20\)

We have labeled the regions by the signs of the sequence of brackets

\{hAB45i, hAB56i, hAB16i, hAB12i, hAB35i\}, 

\(5.21\)

so that the MHV Amplituhedron is the \{\+, \+, \+, \+, −\} triangle region with vertices \(23\), \(24\), \(34\). At six points there are now two spurious lines, defined by the conditions hAB56i=0 and hAB16i=0. These have simple on-shell function interpretations analogous to eq. \(5.15\), but for brevity we do not write them explicitly here. In the chiral pentagon expansion eq. \(5.19\), three terms contribute on this cut configuration: ω\(6,0,1\)





=

\+

\+



. 

\(5.22\)

cut





cut

This is the first example where the two-mass-hard box plays a rôle. We now take the generalizations of the two consistent spaces for the one-mass box and chiral pentagons from our five-point analysis eq. \(5.16\) and augment them by two options for the two-mass hard spaces, see eqs. \(3.22\) and \(3.23\). The details of this analysis can be found in appendix D, but roughly speaking the strategy involves consistently canceling spurious boundaries on all two-dimensional projections. 

Ultimately, we find only the generalization of the second solution in eq. \(5.16\) together with the first choice B\(1\)

defined in eq. \(5.29\) is the unique \(subject to the

12,56

– 57 –

assumption that we make uniform choices for all boxes and pentagons, respectively\) candidate space which is free of all spurious boundaries on all cut surfaces. For the \(AB\) ⊂ \(234\) projection discussed above, the relevant spaces are defined by the following by-now familiar circle diagrams:

B\(3\) =

, 

\(5.23\)

456

P \(1\)=

\+

\+

\+

24

\(5.24\)

B\(1\)

=

. 

\(5.25\)

12,56

Filling in the regions corresponding to the spaces defined in eqs. \(5.23\)–\(5.25\) in the two-dimensional projection eq. \(5.20\), the result is:

– 58 –

\(5.26\)

hAB45i hAB56i hAB16i hAB12i hAB35i

B\(3\)

\+

\+

\+

−

\+

456

P \(1\)

\+

\+

\+

−

\+

24

\+

\+

\+

\+

−

−

\+

\+

\+

\+

−

−

\+

\+

\+

B\(1\)

−

\+

\+

\+

\+

12,56

−

−

\+

\+

\+

Again, we see that the chiral pentagon overlaps with the one-mass and two-mass-hard box in all regions that have spurious boundaries and therefore cancels those geometrically. On this particular two-dimensional projection, we are left with the triangle with vertices \(23\), \(24\) and \(34\) corresponding to the MHV space. We have verified the cancellation of spurious boundaries on all other two-dimensional projections. 

The five- and six-point examples heretofore considered suggest a unique conjecture for the all-multiplicity Amplituhedron-Prime. Namely, we consider the union of the

– 59 –

one-mass box spaces eq. \(3.28\) \(choosing the positive sign for the bracket involving the leading singularity\), the first pentagon space eq. \(3.17\) and the first two-mass hard box space eq. \(3.22\). 

We give explicit formulae for these spaces in terms of

the sign-flip spaces of section 4 in the following subsection. 

This encompasses all

integrand topologies that enter the n-point amplitude in the chiral pentagon expansion eq. \(2.45\). 14 Checking higher-point generalizations of projections such as eqs. \(5.18\) and

\(5.26\) is a straightforward, if tedious, exercise. At seven points, we have verified that all spurious boundaries accessible from the codimension-two configurations \(AB\) ⊂

\(i−1ii\+1\) cancel geometrically. At eight points, we have also verified by parametrizing \(AB\) with four real degrees of freedom that the spurious triple cuts which cut three non-adjacent propagators \(which are not visible in the two-dimensional projections considered above\) cancel as functions of the last remaining degree of freedom in \(AB\). 

5.4

Amplituhedron-Prime

In the previous subsection, we have seen that demanding a consistent gluing of spaces associated to general chiral pentagon and box integrands led to a unique definition for the individual local geometries. In terms of the original integrals appearing in the chiral pentagon expansion, we associate to the generic chiral pentagon the space eq. \(3.17\). 

From the results of section 4 it follows that the additional inequalities involving hABXii and hABXji can always be replaced by one of the conditions defining the sign-flip-two or four spaces. As such, the space in eq. \(3.17\) can be represented in terms of our sign-flip circle-diagrams as a direct sum of four spaces:

P \(1\)

↔

↔

\+

\(5.27\)

ij

\+

\+

. 

14Although the fully massive chiral pentagon first appears at eight points, this generates no additional complications in our analysis. 

– 60 –

The one-mass and two-mass-hard box spaces in eq. \(3.28\) and eq. \(3.22\), respectively, have the following sign-flip representations:

B\(3\)

↔

↔

1 n−3

\(5.28\)

B\(3\)

↔

↔

4 n

B\(1\)

↔

↔

\(5.29\)

1 i−1, i\+2 n

Let us now take the chiral pentagon expansion for the five- and six-particle amplitudes of eq. \(5.1\) and eq. \(5.19\) and write it in terms of the sign-flip spaces eqs. \(5.27\)–

\(5.29\). As argued in subsection 5.3, the resulting space is free of spurious singularities. 

Therefore, we call the resulting collection of geometric regions the five- and six-point Amplituhedron-Prime:

– 61 –

\(1\)

P24

z

\}|

\{

A0 \(5,0,1\) =

\+

\+

\+

\+

\+

\(5.30\)

|

\{z

\}

|

\{z

\}

\(3\)

\(3\)

B

B

12

45

\(1\)

P35

z

\}|

\{

A0 \(6,0,1\) =

\+

\+

\+

\(1\)

P24

z

\}|

\{

\+

\+

\+

\+

\(1\)

P

\(5.31\)

25

z

\}|

\{

\+

\+

\+

\+

\+

\+

\+

|

\{z

\}

|

\{z

\}

|

\{z

\}

\(3\)

\(3\)

\(1\)

B

B

B

13

46

12,56

– 62 –

In subsection 5.3, we have seen on various two-dimensional projections that the representation of the full space in terms of the local building blocks is massively overlapping. 

From the sign-flip representation in terms of the circle-diagrams in eqs. \(5.30\)–\(5.31\), 

this overlap is visible as many terms with the same sign patterns appear in different building blocks. In fact, we can exploit the results of section 4 and expand all ∗= \+ ⊕−

present in these spaces15, throwing out all patterns with more than four sign flips. It is easy to see that many terms appear multiple times throughout the expansion, which geometrically means the same space gets multiply-covered. If we cover a space an even number of times it cancels completely, while for an odd number of covers we are left with a single copy of the space. In the end, there is a surprisingly uniform non-overlapping description of the Amplituhedron-Prime directly in terms of the sign-flip-two and four spaces of section 4, which naturally generalizes to all-multiplicities. Our conjecture for the n-point, one-loop MHV Amplituhedron-Prime is16

A0\(n,0,1\) =

\+

\(5.32\)

\+

. 

Extending the five and six-point analysis of section 5 to test our all-n expression eq. \(5.32\) is a straightforward exercise. We demand that all spurious boundaries present in the individual sign-flip spaces disappear upon gluing. Just as in the five and six-point examples, the spurious codimension-three boundaries are

\(1\) \(AB\) ⊂ \(i−1ii\+1\) and \(AB\) cuts \(jj\+1\), 

\(2\) triple cuts of non-adjacent propagators, hABii\+1i=hABjj\+1i=hABkk\+1i=0

15After expanding all ∗ in the two-mass-hard box \(5.29\) into a collection of spaces with definite signs for all hABii\+1i, we can relate these spaces to the chiral sign-flip regions in \(4.9\) and \(4.26\). 

16Note that in the sum on the second line the term where j = i\+1 is an empty space as it simulta-neously requires both hABiji > 0 and hABiji < 0. 

– 63 –

We have verified at seven points that all spurious boundaries of type \(1\) and \(2\) are absent from the final space. We also performed extensive numerical checks at eight \(and higher\) points that eq. \(5.32\) satisfies many nontrivial constraints. In principle, we could repeat the exercise of section 5 at higher points and attempt to find all positive geometries which consistently glue together. Our conjecture is that the unique spurious-boundary free combination is equivalent to \(after cancelling overlapping regions\) the result eq. \(5.32\). Note that it is clear by construction, that our new Amplituhedron-Prime space is externally triangulated by the chiral pentagon expansion. 

Since the spaces constituting the Amplituhedron-Prime are always defined by \(at least\) one inequality of the form hABii\+1i<0, the bulk of this new geometry is entirely non-overlapping with the original Amplituhedron. At the same time, it has only physical boundaries and exactly the same integrand form as the Amplituhedron. This construction demonstrates there are multiple positive spaces which can be associated with loop integrands in planar N = 4 sYM and the Amplituhedron of \[1\] is only a particular example \(albeit possibly the most canonical one\). 

It is also interesting to note that while the chiral pentagon expansion externally triangulates the Amplituhedron-Prime, it also plays an even more natural rôle in the presumptive dual geometry. We will argue in section 6 that the chiral pentagons internally triangulate the \(yet-to-be discovered\) dual Amplituhedron. 

As an aside, investigating the structure of eq. \(5.32\) more carefully, we note the absence of certain sign-flip regions, such as

and

. 

\(5.33\)

While eq. \(5.32\) does provide the complete definition of the Amplituhedron-Prime space, it is an expansion in terms of elementary regions and it would be desirable to find some more uniform definition, much like the definition of the MHV one-loop Amplituhedron in eq. \(2.31\). One can verify that the following definition is equivalent to eq. \(5.32\): the Amplituhedron-Prime is the space of all lines \(AB\) which satisfy

\{hAB12i, hAB23i, . . . hABn−1ni\} has even number of sign flips

\(5.34\)

\{hAB1ni > 0, hABi1ni > 0, hABi1i−1i > 0, hABi2i−1i < 0\}, 

– 64 –

where i1,2 is the position of the first \(second\) sign flip and i−1 that of the last sign flip. 

The final two conditions in the second line of \(5.34\) are empty for the third term in eq. \(5.32\) which only has two sign flips. Also, the representative spaces \(5.33\) of terms that do not appear in \(5.32\) are ruled out by the first condition in \(5.34\) which only includes brackets up to hABn−1ni and does not “wrap around” to hAB1ni. While the definition in eq. \(5.34\) is very simple, we do not quite understand its deeper meaning at the moment and leave a detailed investigation to future work. 

Note that the chiral pentagon expansion of eq. \(5.27\) singles out the the line \(n1\) as special, as does our definition of the Amplituhedron-Prime, where hAB1ni > 0 is the only uniformly positive quantity throughout the space. While the d log form for the whole space is cyclic, the space is obviously not, as can be seen in eq. \(5.32\). By using the chiral pentagon expansion with \(ii\+1\), rather than \(1n\), fixed, we can construct n other Amplituhedron-Prime spaces by cyclically shifting eq. \(5.32\). 

Relation between A and A0

The results of this subsection suggests a natural question: how is the Amplituhedron-Prime A0 related to the original Amplituhedron space A? They are non-overlapping positive geometries which have only physical boundaries and the same canonical form. 

Therefore, it must be possible to identify a collection of zero-form spaces \(with no spurious boundaries\) which can be added to A0 to directly yield A. 

As it turns out, identifying the correct zero-form space which relates A and A0

is nontrivial, and at the moment we have no closed-form expression for this space. 

However, the process is relatively straightforward for the simplest case of the four-point one-loop integrand, as we will now demonstrate. While the Amplituhedron is the space given by hABii\+1i > 0 and hAB13i < 0, the Amplituhedron-Prime is given by a single term from the second sum in eq. \(5.32\), 

A\(4,0,1\) =

, 

A0\(4,0,1\) =

. 

\(5.35\)

– 65 –

Starting with A0, we first add the achiral space

B1 =

, 

\(5.36\)

which effectively flips the sign of hAB13i in A0. Next, we add a combination of chiral spaces B2 which is defined

hAB12i



B2 =

> 0, hAB23i > 0, hAB14i > 0, hAB13i < 0

, 

\(5.37\)

hAB34i

and obtain A as a result. Expanding B2 in terms of sign-flip-spaces, we have A\(4,0,1\) = A0\(4,0,1\) \+

\+

\+

. 

\(5.38\)

Note that even in this simple example, it is actually quite non-trivial that the spaces with vanishing form we add have only physical boundaries. In particular, if we had flipped the sign of hAB23i in the definition of B2 in eq. \(5.37\), the resulting space would still have zero form, but would have the spurious boundary where hAB13i = 0. 

As our conjecture is that A0 has only physical boundaries, the geometric difference between A and A0 must be a collection of zero-form spaces with physical boundaries only. Finding the exact combination becomes very laborious at higher points, and we do not have a closed formula for it. However, as discussed in the motivations of section 1 and as we will see in the details of section 6, the real purpose in life of the chiral pentagons is to triangulate the dual Amplituhedron, where both A and A0 are mapped under dualization. 

– 66 –

6

Triangulation of the dual Amplituhedron

In the previous section we have seen that the chiral pentagons externally triangulate the Amplituhedron-Prime, which is free of all spurious boundaries, has the same canonical form as the Amplituhedron, but is geometrically distinct. In fact, both the A and A0

spaces only intersect on various codimension boundaries. While the Amplituhedron-Prime is certainly an interesting positive geometry in its own right, we believe that the real purpose of the chiral pentagon expansion is more directly associated with the internal triangulation of the dual Amplituhedron. 

This belief was first raised in \[70\] based on the simple observation that the chiral pentagon forms are positive when evaluated inside the Amplituhedron region, and therefore provide a term-wise positive expansion for the MHV one-loop integrand. In this picture, the positivity of the loop integrand is reminiscent of the volume interpretation of the dual Amplituhedron. The volume is naturally a positive function of \(real\) geometric data \(momentum twistors\) and slicing this volume into smaller pieces via internal triangulation preserves a term-wise positivity. 

For the simplest k = 1 tree Amplituhedron the dualization procedure is well understood and involves a simple map between polytopes and their duals. However, for k > 1 tree-level \(and all loop-level amplituhedra\) the geometries become non-polytopal, and in these cases the dualization procedure has not been defined as of yet. While we do not give a complete solution of this problem in this work, in this section we provide a more direct link between the chiral pentagon expansion and the yet-to-be-found dual one-loop MHV Amplituhedron. 

In subsection 5.3 we considered a significant subset of simple codimension-two faces of the MHV one-loop Amplituhedron. In these pictures, we localize two degrees of freedom of the line \(AB\), so that the resulting projection can be viewed as a point \(and polygons\) on the projective plane. Although the correct dual of the fully off-shell line \(AB\) is not known, we can avoid this problem by working directly on codimension-two surfaces which reduce to the projective plane 2

P . By exploiting the elementary geomet-

rical fact that polygons dualize to polygons, we can explicitly construct the associated codimension-two boundaries of the dual Amplituhedron by mapping points↔lines, in a precise way that we outline below. On these dual codimension-two boundaries, we show that the chiral pentagon expansion corresponds to an internal triangulation of the dual of the MHV Amplituhedron. 

6.1

Dualizing polygons

As discussed in section 5.3 there are two different codimension-two boundaries which reduce to the geometry of a point inside a polygon on

2

P : either we localize the line

– 67 –

\(AB\) in a plane \(i−1ii\+1\) or it passes through the point Zi. 

In order to connect the chiral pentagons and the dual Amplituhedron, we dualize the

2

P geometries of subsection 5.3. In fact, these projections are structurally identical to the toy model of appendix B; only the labelling of the points and lines is different. 

Dualizing a polygon is a straightforward procedure and yields another \(dual\) polygon; this was discussed in the \(pre-\)Amplituhedron context in \[69\]. 

We begin with the five-point codimension-two boundary \(5.9\) where \(AB\) passes through Z2. The dualization procedure maps points↔lines. Thus, the vertices \(leading singularities\) in the original projection become the edges of the dual polygon, while the codimension-one boundaries hABii\+1i = 0 become the vertices in the dual space. The dualization of eq. \(5.9\) is

⇐⇒

\(6.1\)

dual to

where we use the notation that e.g., \(2, 51\) corresponds to \(AB\) passing through Z2 and cutting the line \(15\). We have also color-coded the leading singularities \(and their dual lines\) to direct the eye of the reader. For example, the red vertex \(leading singularity\) AB = \(12\) in the left figure gets mapped to the red line in the right figure. Note that we label the dual picture with conditions imposed on the line \(AB\), despite the fact that this projection is actually describing the localization of some dual line \]

\(AB\) to

an associated codimension-two boundary. From this perspective, it is crucial that the space of \(AB\) lines is four-dimensional, so the dual of a two-dimensional geometry is another two-dimensional geometry\! This gives a concrete way of constructing the faces of the dual geometry. Ideally, in the dual picture we would like to dispense with \(AB\) altogether and identify the regions and boundaries in the projection with the signs of some brackets, à la hg

AB . . .i ≷ 0; however, we do not yet know the constraints which

\]

\(AB\) should satisfy. Nevertheless, the simple structure of the dualization on these two-dimensional projections allows us to take a region in the original space and find the corresponding region in the dual space just by working in the original \(AB\) space, 

– 68 –

using a very simple prescription. The rule is that any line which intersected the region in the original space corresponds to a point in the dual space; moreover, that point must be outside the dual region. Similarly, a line which was outside the region in the original space maps to a point which must be inside the dual region. These simple rules suffice to uniquely determine the image of any region in the dual space. As an example, the dual of the Amplituhedron in the above example where \(AB\) passes through Z2 is the light-blue shaded region on the right-hand-side of:

⇐⇒

\(6.2\)

dual to

In particular, the spurious leading singularities \(13\) and \(123\)∩\(245\), which are outside the original Amplituhedron on the left, map to lines in the dual space which pass through the dual Amplituhedron on the right. 

The parity conjugate projection, where \(AB\) lies in the plane \(123\), is a slightly less trivial example of the correct dualization procedure

⇐⇒

\(6.3\)

dual to

The relative positions of lines/vertices in the dual picture on the right merit an explanation. Once again, the shaded region is the \(dual\) Amplituhedron, indicated primarily

– 69 –

for illustrative purposes. In this case, the spurious leading singularities \(24\), \(25\) and \(123\)∩\(245\) must all pass through the dual Amplituhedron region. Our convention throughout this work has been to assign the Amplituhedron to a region with finite area. To maintain this convention here requires the vertex \(2, 45\), which denotes the codimension-three boundary where the line \(AB\) lies in the plane \(123\) and cuts \(45\), to lie inside the triangle bounded by the edges corresponding to the accessible MHV

leading singularities. On this cut surface, these are \(AB\) = \{\(12\), \(13\), \(23\)\}. Importantly, the point \(2, 45\) is spurious, so it is not included in the amplitude region; to indicate this, we use an empty \(white\) vertex. All similar codimension-two boundaries \(at five points\) are obtained by simply relabeling the above examples. 

6.2

Dual spaces of chiral pentagons

Having introduced the dual two-dimensional projections, we now turn to identifying the image of the boxes and chiral pentagons under dualization using the prescription discussed above. Let us return to the five-point case, where the amplitude is a sum of two boxes and a single pentagon, c.f. eq. \(5.1\). Using the results of section 5.3

and appendix D, we can identify the dual regions corresponding to the projection summarized in eq. \(D.1\), where \(AB\) = \(A2\). The box space B\(3\) relevant for the 45

Amplituhedron-Prime and its na¨ıve dualization are

B\(3\) ↔

⇐⇒

\(6.4\)

45

dual to

This seems to suggest that the dual of the Amplituhedron-Prime is not an internal triangulation of the dual Amplituhedron as the dual of the B\(3\) box region naively lies 45

outside of the dual of the Amplituhedron in the right figure of \(6.4\). However, there is a critical feature of the dualization which has been neglected in eq. \(6.4\): namely, the lower-dimensional boundaries in the original projection on the left-hand-side, which map under dualization to infinite wedges in the dual picture on the right. The cavalier treatment of the lines and vertices on the left-hand-sides of eq. \(6.4\) causes no issue

– 70 –

from the perspective of the canonical forms because any less-than-full-rank subspace of 3

P has vanishing form. However, these same boundaries play a pivotal rôle in the dual picture because they dualize to larger spaces with nonzero \(in fact, infinite\) volume. 

Note that while the dual of a line is a point, the dual of a line segment is an infinite wedge \(with two codimension-one boundaries in the dual\) defined by the two leading singularities which bookend the line segment. Thus, the right-hand-side of eq. \(6.4\)

only represents the bulk component of the dualization and is incomplete. In fact, there is a simpler way of identifying the correct dual spaces which exploits the fact that zero-form spaces dualize to lower-dimensional boundaries. First, we can identify the region which dualizes to the triangle with vertices \(2, 51\), \(2, 13\) and \(2, 34\), with all boundaries included:

⇐⇒

\(6.5\)

dual to

In the dual picture, we use filled vertices to indicate these are included as boundaries of the region. Now, the box space on the left-hand-side of eq. \(6.4\) can be related to the left-hand-side of eq. \(6.5\) by adding a zero-form wedge in the original space, namely

⇐⇒

\(6.6\)

dual to

– 71 –

We use a white vertex to indicate that this point is excluded from boundary of the region. In the dual picture, we draw “dashed” lines to indicate that only the two orange vertices constitute the dual region. Therefore, the dualization of the box space of the left-hand-side of eq. \(6.4\) is the internal triangle with precisely this edge absent, B\(3\) ↔

⇐⇒

\(6.7\)

45

dual to

The dualization of both pentagon spaces \(D.2\) on the boundary where \(AB\) = \(A2\) can be constructed in a similar fashion. Similarly to \(6.5\), we first identify the region in the original space which maps to the second internal triangle of the dual space:

⇐⇒

\(6.8\)

dual to

– 72 –

The pentagon space P \(1\), relevant for the Amplituhedron-Prime, can be related to 24

eq. \(6.8\) by the addition of the zero form region

⇐⇒

\(6.9\)

dual to

so the correct dualization for the pentagon P \(1\) is

24

P \(1\) ↔

⇐⇒

\(6.10\)

24

dual to

For reference, the dualization for the alternative pentagon space P \(2\) is the same dual 24

bulk region, but with the vertices \(2, 51\) and \(2, 34\) missing. 

6.3

Two-dimensional triangulations

The chiral pentagon expansion triangulated the Amplituhedron-Prime space A0. Since the logarithmic forms for A and A0 are equal, by definition, their dual spaces have the same volume. Thus, a priori in the dual pictures A and A0 can only differ by zero-volume lower-dimensional boundaries which are dual to zero-form wedges in the original space. 

In fact, the same argument suggests that any choice of individual

box and pentagon geometries must match the dual Amplituhedron up to possibly its

– 73 –

vertices and edges. To demonstrate this correspondence explicitly, we carefully account for all lower-dimensional boundaries in the dualization procedure. As discussed in the previous subsection, these line segments dualize to infinite wedges which dramatically affect the resulting dual region. In general, it is easiest to understand the dualization by utilizing zero form regions in the original two-dimensional projection. 

Let us now compare the behavior of the Kermit eq. \(2.19\) and chiral pentagon eq. \(3.3\) expansions in the original and dual two-dimensional projections. As shown in section 2, the Kermit representation is by construction an internal triangulation of the Amplituhedron. By the schematic arguments of section 1, the expectation is that internal triangulations map to external triangulations of the dual, and vice versa. We now establish this for the Kermit expansion at five points on the boundary when \(AB\) passes through Z2. On this cut, the Kermits triangulate the quadrilateral using the line hAB14i=0. Excluding this line from consideration, the na¨ıve dualization reads

⇐⇒

\(6.11\)

dual to

We see that just as in eq. \(6.4\) the space remaining is not the quadrilateral representing the dual Amplituhedron. The issue here is the same as in the na¨ıve dualization attempt of the previous subsection: we have been glib about the lower-dimensional boundaries in the original space. Specifically, in the example on the left-hand-side of eq. \(6.11\), 

the segment of the line hAB14i = 0 between the points \(12\) and \(24\) dualizes to an infinite wedge with exactly these two codimension-one dual boundaries. To account for this in the dual picture requires that we add the dual of this line segment to our na¨ıve

– 74 –

picture eq. \(6.11\), i.e., 

⇐⇒

\(6.12\)

dual to

To be clear, this picture includes both the points \(12\), \(24\) as well as the line segment itself. Including this boundary with both Kermit regions eq. \(6.11\), we double-cover the points \(12\) and \(24\). Thus, to recover the dual space we must add these points back, without the line segment in between them. The dual of this piece is, by completeness, the wedge in eq. \(6.12\) minus the single point \(2, 14\):

⇐⇒

\(6.13\)

dual to

The net effect of these subtleties on our na¨ıve picture eq. \(6.11\) is the addition of the infinite wedge eq. \(6.13\), which gives exactly the dual Amplituhedron. 

\(An alternative resolution to this problem is to include the triangulation line with one of the Kermits but not the other. Upon removing the extra point \(14\) in the dual space, we recover exactly the same \(up to relabelling\) external triangulation as in the motivational example of eq. \(2.44\). This is sensible from a purely geometrical perspective. However, from the point of view of canonical forms it seems more natural

– 75 –

to include the triangulation line with its endpoints in both terms, as both forms do have nonzero residues on this boundary.\)

Using the results of eq. \(6.7\) and eq. \(6.10\), we see that the dual of the Amplituhedron-Prime on this cut surface triangulates the dual of the Amplituhedron, except for the two vertices \(2, 13\) and \(2, 45\), i.e., 

⇐⇒

\(6.14\)

dual to

Note that the original non-overlapping regions with fixed signs of hABiji brackets are now overlapping in the dual space. Therefore, it is very non-trivial that the regions corresponding to chiral pentagons triangulate internally the dual Amplituhedron without any overlaps. 

The fact that the logarithmic forms for Amplituhedron and Amplituhedron-Prime are identical means that their \(conjectured\) dual spaces have the same volume and are identical up to spaces which have zero volume. This matches the result of eq. \(6.14\), 

where we can see that A and A0 differ by lower-dimensional boundaries. This line of reasoning is also suggestive of an ambiguity in the definition of the Amplituhedron-Prime. Namely, we are always free to add any spaces which have zero form \(such as the infinite wedge of eq. \(6.6\)\) because in the dual space they correspond to zero-volume lines or points. 

To provide additional evidence that the Amplituhedron-Prime dualizes to an internal triangulation of the \(bulk\) dual Amplituhedron, we can repeat the above exercise for the cut surface \(AB\) ⊂ \(234\) which was analyzed in eq. \(5.18\). For the

– 76 –

Amplituhedron-Prime, all three local integrals contribute: B\(3\) ↔

⇐⇒

\(6.15\)

45

dual to

B\(3\) ↔

⇐⇒

\(6.16\)

12

dual to

P \(1\) ↔

⇐⇒

\(6.17\)

24

dual to

Hence the dual of the Amplituhedron-Prime triangulates the dual Amplituhedron, up

– 77 –

to a single vertex \(3, 24\) on the two-dimensional projection where \(AB\) ⊂ \(234\), 

⇐⇒

\(6.18\)

dual to

We have exhaustively verified for all remaining five and six point two-dimensional projections where \(AB\) = \(Ai\) or \(AB\) ⊂ \(i−1ii\+1\) that the Amplituhedron-Prime internally triangulates the dual Amplituhedron up to contributions with zero-volume. 

In fact, in retrospect this conclusion would follow immediately from the existence of a spurious-boundary-free, zero-form space B which connects A and A0 through A =

A0 \+ B. We wrote down an explicit expression for B at four points in eq. \(5.38\)

and, although we do not have an explicit formula for this space at n-points, we see no conceptual obstruction which would preclude its existence. We leave an explicit construction of the zero-form space connecting the Amplituhedron and Amplituhedron-Prime to future work. 

Rigidity of the dual space

We have seen in the previous discussion that a single d log form gives rise to various positive geometries. We emphasized the importance of faithful geometries in section

3.2, where all boundaries of the geometric space appear as poles in the d log form. 

Furthermore, we used these geometries to interpret the chiral pentagon expansion as external triangulation of Amplituhedron-Prime in eq. \(5.32\). From our discussion it is clear, that all these spaces have different geometries, but one can naturally ask about the duals of the positive spaces which originate from the same d log form. 

Here, we explicitly discuss different box spaces for the one-mass box B45 summarized in eq. \(5.3\). We can dualize these spaces on the two-dimensional boundary where the line \(AB\) passes through Z2, c.f. \(5.11\) and \(6.1\). We repeat the same exercise from section 6.1 for the three alternative box spaces appearing in eq. \(D.1\) even though they are irrelevant for the Amplituhedron-Prime. Because these additional box spaces are all equivalent to eq. \(6.5\) up to a zero-form region in the original two-dimensional

– 78 –

projection, they all map to the same internal piece of the dual Amplituhedron up to lower-dimensional boundaries. Indeed, the results of dualization for the alternative box spaces are, using the coloring convention of eq. \(D.1\):

B\(1\) ↔

⇐⇒

\(6.19a\)

45

dual to

B\(2\) ↔

⇐⇒

\(6.19b\)

45

dual to

B\(4\) ↔

⇐⇒

\(6.19c\)

45

dual to

– 79 –

This makes perfect sense because the positive geometries differ by spaces with vanishing form \(wedges on the two-dimensional boundaries\) which get mapped to points and lines in the dual two-dimensional geometry. Therefore, from the point of view of the dual Amplituhedron, it does not matter which positive geometry we use for a given d log form, it always represents the same dual geometry. This simply follows from the fact that the regions with vanishing d log form map to lower-dimensional objects in the dual which have zero volume. 

Therefore, it is natural to expect that while the positive geometries A and A0

are different, the putative dual Amplituhedron is unique, and the chiral pentagons triangulate it internally. We gave some evidence for this claim in this section. 

7

Conclusion

In this paper we discussed various positive geometries in the context of the one-loop Amplituhedron and its variants. We have shown that for external data satisfying the MHV positivity conditions \(2.11\), there are a number of further interesting positive geometries besides the original MHV and MHV Amplituhedra. In section 4, we classified all these spaces using topological sign-flip properties which are reminiscent of, but distinct from, the sign-flip definition of the Amplituhedron \[19\]. Furthermore, we showed that these positive spaces can be used to give a geometric interpretation of the chiral pentagon expansion of the one-loop MHV amplitude of eq. \(2.45\). In particular, the chiral pentagons externally triangulate a new Amplituhedron-Prime space

\(5.32\) which is a non-overlapping twin of the original Amplituhedron with only physical boundaries and the same logarithmic form. Finally, in section 6, we made more precise the statement that the chiral pentagon expansion can also be interpreted as the internal triangulation of the yet-to-be found dual Amplituhedron. We were able to demonstrate the internal triangulation of the dual on certain two-dimensional boundaries of the full space where the geometry reduces to that of polygons for which a dualization prescription exists. 

Our work opens the door to various new research directions. The first question is how the stories about local geometries, as well as the study and classification of sign-flip spaces, extend to higher loops and to higher NkMHV degree, where the positive external data will play a more important rôle. We already briefly touched upon this issue in \[77\] and found that sign-flip-six and higher spaces are allowed beyond MHV

kinematics. Another interesting angle is to use this framework to generate IR-finite integrands at two-loops and beyond. The logarithmic forms for sign-flip-four spaces were given by chiral octagons, which form an IR-friendly dual conformal basis \[72\] of integrands at one-loop—and separates naturally IR-divergent, IR-finite and parity-odd

– 80 –

integrands. It would be very interesting to replicate this at two-loops and find a basis of IR-finite dual conformal invariant integrands. These integrands would be perfect targets for modern integration methods \[78\] and could play an important rôle in the expansion of IR-finite quantities, such as remainder and ratio functions. 

Finally, the main open direction is the exploration of the dual Amplituhedron. 

The link between chiral pentagons and the internal triangulations of this hypothetical space provides further evidence for its presumptive existence. However, we were able to establish this connection only on certain two-dimensional boundaries where the dual Amplituhedron geometry reduced to projective polygons. Exploring other two-dimensional boundaries of non-polygonal form, as well as three-dimensional boundaries and the rôle of internal triangulations, should bring us to the ultimate goal of the discovery of the dual Amplituhedron space. 

Acknowledgements

We thank Nima Arkani-Hamed, Akshay Yelleshpur Srikant, and Ryota Kojima for stimulating discussions. This research is supported in part by U.S. Department of Energy grant DE-SC0009999 and by the funds of University of California. E.H. is supported by the U.S. Department of Energy under contract DE-AC02-76SF00515. 

The research of C.L. is supported in part by an ERC Starting Grant \(No. 757978\) and a grant from the Villum Fonden \(No. 15369\). 

– 81 –

A

Configuration of lines in momentum twistor space

There is an intimate relation between configurations of \(loop\) lines in momentum twistor space and certain restricted kinematic configurations of loop momenta on unitarity cuts of loop integrands or local integrals. At one loop, we can depict the off-shell configuration of lines in twistor space corresponding to a generic loop integrand \(either of the amplitude or of an integral\) by a set of lines corresponding to external dual momenta, together with a line \(AB\) in a generic configuration \(parameterized via eq. \(2.2\)\), 

↔

\(A.1\)

In this setup, the loop-line \(AB\) does not intersect any of the lines associated to external kinematic points. In the next step, one could go to codimension-one configurations by imposing one condition, e.g. hABii\+1i = 0, so that the lines \(AB\) and \(ii\+1\) intersect. 

↔

\(A.2\)

At the level of cuts, this corresponds to setting a single propagator hABii\+1i = 0 to zero. This codimension-one configuration for the line \(AB\) can be parameterized by three degrees of freedom. The intersection implies that one of the defining points of the \(AB\)-loop lies on the line \(ii\+1\). Taking into account the projectivity of the Z’s, one possible particular parametrization is

ZA = Zi \+ α1Zi\+1 , 

ZB = Zj \+ α2Zk \+ α3Zl . 

\(A.3\)

In a second step, one can impose an additional constraint to end up on a codimension-two configuration of the line \(AB\). Depending on the condition one imposes, there are

– 82 –

three situations to consider

\(A.4\)

\(A.5\)

which have explicit two-dimensional parametrizations of the solution for the line \(AB\) given by, 

Z\(1\) = Z

= Z

= Z

A

i \+ γ1Zi\+1 , 

Z\(2\)

A

i \+ γ1Zi\+1 , 

Z\(3\)

A

i , 

\(A.6\)

Z\(1\) = Z

= Z

= Z

B

j \+ γ2Zj\+1 , 

Z\(2\)

B

i \+ γ2Zi−1 , 

Z\(3\)

B

j \+ γ1Zk \+ γ2Zl . 

We can continue by imposing yet further constraints. At codimension-three, for the first time we encounter the situation associated with a composite residue where we localize the loop-line into a collinear configuration, depicted in the second figure below. 

\(A.7\)

\(A.8\)

Here we have omitted two special configurations where the loop line \(AB\) intersects three consecutive external lines \(i−2i−1\), \(i−1i\) and \(ii\+1\). For the solutions depicted

– 83 –

above, we can write one-parametric representations of the solution space for \(AB\). The generic solution is a bit involved, so here we only give the parametrization for the simple configuration where \(AB\) is in the plane \(i−1ii\+1\) and passes through the point Zi, Z\(2\) = Z

= Z

A

i , 

Z\(2\)

B

i−1 \+ δZi\+1. 

\(A.9\)

Finally, we can discuss codimension-four configurations of the line \(AB\) where all degrees of freedom are completely fixed. Such configurations are related to leading singularities. Again, there are various cases to consider, some of which correspond to soft composite residues that are physical, as well as spurious residues where scattering amplitudes have no support \(see the figure on the right below\)

\(A.10\)

\(A.11\)

Besides the generic “four-mass” configuration depicted in the left figure above, we can have special kinematic configurations where some of the external lines intersect

– 84 –

\(corresponding to massless corners in diagrams\) and the Schubert problem simplifies. 

↔

↔

↔

↔

↔

↔

\(A.12\)

↔

↔

↔

↔

For the maximal codimension configurations, we have explicitly written the final configuration of the loop-line \(AB\) in terms of external twistors only. In these formulae, certain geometric quantities appear that we briefly discuss for completeness. In particular, \(abc\) ∩ \(def \) denotes the intersections of two planes, spanned by twistors

\{Z

3

a, Zb, Zc\} and \{Zd, Ze, Zf \} respectively. 

In P , the intersection of two planes is a

line, which can be represented as

\(abc\) ∩ \(def \) = ZaZbhcdef i \+ ZbZchadef i \+ ZcZahbdef i

\(A.13\)

= habcdiZeZf \+ habcf iZdZe \+ habceiZf Zd

– 85 –

Additionally, there are points defined by the intersection of a line \(ab\) and a plane \(cde\), which can be represented as

\(ab\) ∩ \(cde\) = Zahbcdei \+ Zbhcdeai = −\(Zchdeabi \+ Zdheabci \+ Zehabcdi\) , \(A.14\)

which naturally reflects the antisymmetry \(ab\) ∩ \(cde\) = −\(cde\) ∩ \(ab\). 

B

External triangulations

In this section we focus on external triangulations, as a first application of the systematic classification of the sign-flip spaces introduced in section 4. As discussed briefly in section 2.4, an external triangulation of a space introduces a “larger” space outside of the original region using spurious vertices which violate the original positivity conditions. In the context of the sign-flip spaces above, this corresponds to flipping the signs of some brackets which defined the original space. As a warm-up, let us go back to the projective plane

2

3

P , where the analogue of a line \(AB\) in P is a point Y on the

plane with two degrees of freedom. As heuristically described above, we can externally triangulate the quadrilateral with vertices z1, z2, z3, z4 with two triangles, 

=

−

\(B.1\)

Note that the codimension-one boundaries of each triangle \(which are lines in 2

P \) are

subsets of boundaries of the original quadrilateral, but there is an additional spurious vertex \(12\)∩\(34\) := z1h234i − z2h134i which is used as a triangulation point that cancels between triangles.17 We can also describe this triangulation in the language of 17In this context, angle brackets denote contraction with a three-index Levi-Civita symbol, i.e., habci := IJKzI zJ zK. 

a b

c

– 86 –

the previous section as follows. The quadrilateral is defined by the following conditions:

↔ hY 12i > 0, hY 23i > 0, hY 34i > 0, hY 14i > 0, 

\(B.2\)

where we used the same circle to visualize the constraints, but now for hY ii\+1i. We can define the triangles in a similar way. Note that the first triangle with vertices

\{\(12\) ∩ \(34\), 2, 3\} in eq. \(B.1\) has an unfixed sign for hY 14i and therefore lacks this codimension-one boundary. Pictorially this will be denoted by ∗ for the relevant bracket in the circle-figures and can also be interpreted as marginalizing over both signs. Even though the second triangle with vertices \{\(12\) ∩ \(34\), 1, 4\} has hY 23i > 0 fixed, from the picture we see that this is not a boundary of the space. The two triangles are associated to the following circle diagrams:

↔

, 

\(B.3\)

↔

. 

\(B.4\)

In summary, we can re-interpret this triangulation as taking the space of the first triangle with unfixed sign of hY 14i and dividing it into two spaces: one where hY 14i > 

– 87 –

0, which is the quadrilateral, and another where hY 14i < 0 which is the second triangle. 

=

\+

\(B.5\)

=

\+

In 2

P the triangle is the simplest geometric space with non-vanishing form. If we remove one more boundary by marginalizing over the corresponding hY ii\+1i, we get a “wedge” 

defined by only two inequalities. In this case the canonical form vanishes, e.g. 

↔ Ω = 0. 

\(B.6\)

This vanishing can also be understood from the d log form perspective as we need at least three brackets to form two independent projective ratios that enter the arguments of d log’s. 

Simplest sign-flip spaces

We can almost verbatim generalize the above discussion to the configuration space of lines \(AB\) in

3

3

P relevant to the MHV one-loop positive geometry. In P , the simplest

space has four boundaries, and the corresponding logarithmic form is given by the box integrand. However, in this case we need to include one additional inequality which

– 88 –

does not correspond to a boundary but is nonetheless required to define the chiral sign-flip-four space. In the simplest four-point example, we define the space h1234i2

↔ ω\(4\),− =

≡

\(B.7\)

1234

hAB12ihAB23ihAB34ihAB14i

with hAB13i, hAB24i < 0. The second chiral region has hAB13i, hAB24i > 0 and its form is the same up to a sign, Ω\(4\),\+ = −Ω\(4\),−. The union of these two regions is an 1234

1234

achiral space which has vanishing form and unfixed signs for hAB13i and hAB24i, 

=

\+

\(B.8\)

Directly at the level of d log forms, four brackets hAB12i, hAB23i, hAB34i, hAB14i are insufficient to define four independent projective ratios that enter the arguments of the d logs, and therefore the whole form must vanish. If we additionally impose hAB13i ≶ 0 to cut the space into chiral components, we have access to one further bracket to form four independent projective ratios, e.g., hABii\+1i/hAB13i. The same argument applies to any other space with only four boundaries hABii\+1i. A less trivial example of that logic is the special sign-flip-two region we discussed in eq. \(4.12\). Even though there were many brackets with fixed signs, the space has only four boundaries

– so we get a zero-form space if we drop the chiralization condition hABii\+2i ≷ 0. 

The simplest achiral space with non-vanishing form must therefore have five boundaries, and the integrand form is the general parity-odd pentagon \(given by a suitable generalization of eq. \(3.8\) where none of the external legs need to be massless\). In fact, because the achiral space is defined by a set of inequalities which all correspond to physical codimension-one boundaries, any of the 25 sign choices are allowed and lead to the same canonical form up to a sign. \(This is distinct from the chiral components where only a subset of signs led to a consistent geometry.\) For the five-point space we

– 89 –

get

N

↔ ωodd =

odd

, 

\(B.9\)

5

hAB12ihAB23ihAB34ihAB45ihAB15i

where ± indicates an arbitrary \(but fixed\) sign for the corresponding bracket. Exactly the same is true for higher points: if we marginalize over the signs of the n − 5 brackets hABii\+1i for i /

∈ \{i1, i2, i3, i4, i5\} and pick any of the 25 possible sign choices for the remaining hABirir\+1i, we find the general parity-odd pentagon

N

↔ ωodd=

odd

, \(B.10\)

n

hABi1i1\+1ihABi2i2\+1ihABi3i3\+1i

×hABi4i4\+1ihABi5i5\+1i

where ± indicates that either sign choice is acceptable and ∗ instructs us to marginalize over both sign choices. 

In the rest of the section we will relate different sign-flip spaces via external triangulations, which allows us to write the canonical forms for more complicated spaces with many boundaries. In our discussion, we use several important facts: 1. Canonical forms of sign-flip-four spaces are chiral octagons, eq. \(4.28\), and descendants. 

2. The form for a chiral space with four boundaries is a box. 

3. The form for an achiral space with five boundaries is a parity-odd pentagon, eq. \(B.10\). 

4. Any chiral space with three or fewer boundaries has vanishing form. Any achiral space with four or fewer boundaries has vanishing form. 

5. Sign-flip-six and higher regions are empty; their form is identically zero. 

– 90 –

Triangulation of sign-flip-two regions

We first consider the chiral sign-flip-two space, with the additional condition hABiji>0: S\(2\),\+ =

. 

\(B.11\)

ij

As stated in section 4, the codimension-one boundaries of this space correspond to the four brackets adjacent to the sign flips, as well as all other ‘negative’ brackets in the upper half of the circle, i.e., 

boundaries: \{hABi−1ii, hABii\+1i, hABi\+1i\+2i, . . . , hABj−1ji, hABjj\+1i\}. \(B.12\) \(For the opposite chirality defined by hABiji < 0, the boundaries correspond to the four brackets adjacent to the sign flips, as well as the positive brackets in the lower half of the circle.\) To externally triangulate this space, we use the fact that any space defined by four or fewer inequalities has a vanishing canonical form. Thus, if we marginalize over all signs in the sequence \{hABi\+1 i\+2i, . . . , hABj−2 j−1i\} but leave all other signs unchanged, the corresponding space has four boundaries, and is therefore trivially a two-mass-easy box form:

↔

. 

\(B.13\)

This fact can now be used in a “completeness relation” to determine the canonical form for S\(2\),\+. If we expand eq. \(B.13\) in terms of regions with definite signs we encounter ij

the sign-flip-two region whose form we want to determine, a collection of sign-flip-four

– 91 –





regions, e.g., 

, 

\(B.14\)

together with a number of sign-flip-six and higher regions which are empty. From this we can express the sign-flip-two region in terms of eq. \(B.13\) and sign-flip-four regions18

=

−

\(B.15\)

Note that this is an external triangulation as also indicated by the minus sign between the two terms on the right-hand-side of eq. \(B.15\). Geometrically we remove sign-flip-four regions from eq. \(B.13\) leaving us with the chiral sign-flip-two region of interest. 

Since we already found all canonical forms associated to the regions on the right-hand-side of eq. \(B.15\), we can immediately write down the canonical form of Ω\(2\),\+, ij

Ω\(2\),\+ =

\+

−

ij

\(B.16\)

18In the achiral sign-flip-four space, hABiji > 0 is automatically satisfied once we impose the

‘external’ inequalities. More details about these spaces and their fixed brackets are summarized in appendix C. 

– 92 –

where the sum over octagons includes all degenerations. Using this formula for the six-point example we find

=

−

\(B.17\)

Ω\(2\),\+ =

\+

−

36

As we discussed earlier in section 4, there are a few special cases of sign-flip-two regions. 

The most special case is the chiral sign-flip-two region with only a single minus sign eq. \(4.13\) which is an empty space with vanishing canonical form. 

In this degenerate case, for the opposite chirality S\(2\),−, we can triangulate the ij

space using exactly the same procedure, only with different boundary data: the region where all n − 3 ‘\+’ signs are replaced by ‘±’ has vanishing form \(as it only has three boundaries\) and also the sign-flip-four regions are achiral rather than chiral. Therefore, the forms which appear on the right hand side are parity odd combinations of octagons \(and descendants\). 

Triangulation of sign-flip-zero region

As argued earlier in section 3.3, there is no external triangulation of MHV or MHV

Amplituhedra in terms of simple building blocks. However, this is not true for the achiral sign-flip-zero region eq. \(4.7\) which is defined by hABii\+1i > 0 inequalities only. There are many ways to triangulate the S\(0\) region externally. The simplest \(though certainly not the most efficient\) is to fix four plus signs and marginalize over all other signs. In light of our earlier discussions, such a region has vanishing canonical form, but when we expand ∗ = \+ ⊕ − we find the sign-flip-zero region of interest

– 93 –

together with many sign-flip-two and four regions. 

zero-form space

achiral sf0 space

z

\}|

\{

z

\}|

\{

=

achiral sf2 spaces

z

\}|

\{

\+

\+

\+ · · ·

achiral sf4 spaces

\(B.18\)

z

\}|

\{

\+

\+

\+ · · ·

empty sf6 and higher spaces with zero form

z

\}|

\{

\+

\+ other empty regions . 

We already calculated the necessary canonical forms for all regions appearing in eq. \(B.18\)

before in eqs. \(4.28\) and \(B.16\), which allows us to write the form for the sign-flip-zero space S\(0\) eq. \(4.7\) more explicitly in terms of known quantities. Note that all sign-flip-two and four regions are achiral, so we must use the relevant parity-odd forms associated to those spaces by combining both chiralities in eqs. \(4.28\) and \(B.16\). 

Having discussed the canonical forms of all sign-flip spaces, we now revisit to the chiral pentagon expansion of eq. \(2.45\), together with the parity-odd one-loop amplitude given as the difference of the MHV and MHV amplitudes. In the parity-odd case, 

– 94 –

the local expansion involves parity-odd pentagons, eq. \(3.10\), which can be associated to simple achiral spaces defined by only five inequalities \(see our discussion earlier in this section\) where the signs of these inequalities did not matter to get the correct parity-odd pentagon canonical form. The question is whether or not the parity-odd pentagon expansion eq. \(3.10\) can be understood geometrically as an external triangulation of some well-defined space. In other words: can we triangulate the sign-flip-zero space eq. \(4.7\) not via eq. \(B.18\), but in terms of spaces with five boundaries only? 

The answer is yes, and in the following we give a straightforward description of such a triangulation:

1. We start with the sign-flip-zero region S\(0\) and triangulate it externally via the space with the sign of hAB12i marginalized, 

=

−

\(B.19\)

2. For the region with hAB12i = ∗ \(i.e., hAB12i≷0 does not have a fixed sign\), we continue by marginalizing over the sign of hAB23i leaving us with two spaces, one where hAB23i = ∗, and one where hAB23i < 0. 

=

−

\(B.20\)

Whenever we encounter a space with a minus sign we stop, if we have ∗’s only we continue. This procedure results in a collection of spaces Si defined by Si := \{hAB12i≷0, . . ., hABi−2i−1i≷0, hABi−1ii<0, 

\(B.21\)

hABii\+1i>0, . . ., hAB1ni>0\}, 

i ∈ \{2, . . ., n−3\} , 

– 95 –

where, in the boundary case i = 2, we start with hAB12i< 0. Pictorially, Si is represented by the following circle diagram

Si =

. 

\(B.22\)

This procedure stops at i = n − 3 because we reach the end of the circle. Going beyond this point simply generates spaces with less than five boundaries that have vanishing form \(and are therefore irrelevant for the purpose of obtaining the canonical form\). 

3. In the third step, we continue the same procedure for each space Si but leave hABii\+1i > 0 untouched, marginalizing over hABi\+1i\+2i

=

−

. 

\(B.23\)

We again keep the spaces with two minus signs and marginalize further over the spaces where we have ∗. As a result we generate a collection of spaces Sij, Sij =

, 

i ∈ \{2, . . . , n−3\}, j ∈ \{i\+2, . . . , n−1\}. 

\(B.24\)

For each region Sij the signs of \{hABjj\+1i, . . . hAB1ni\} are all positive. However, we can freely replace all but the hABjj\+1i and hAB1ni positive signs by \+ → ∗. 

This is because Sij already has two non-adjacent minus signs; therefore, spaces where we introduce additional minus signs leads to empty sign-flip-six \(or higher\)

– 96 –

regions, e.g., 

example of an empty region:

. 

\(B.25\)

As a result, we triangulate the sign-flip-zero region S\(0\) in eq. \(4.7\) in terms of spaces with five boundaries only, 

=

, 

\(B.26\)

which, at the level of canonical forms, corresponds to the parity-odd pentagon expansion eq. \(3.10\). Note that on the right-hand side of eq. \(B.26\) we are suppressing spaces with zero-form which are necessary for the geometric triangulation, but unnecessary for the purposes of computing the canonical form. Geometrically, each space appearing in eq. \(B.26\) is equivalent to that of a pentagon where we forget about the signs of the last two brackets in eq. \(3.19\) \(see also eq. \(B.10\)\). The zero-form spaces implicit in eq. \(B.26\) demonstrates that while we were successful in interpreting the pentagon expansion eq. \(3.10\) geometrically, spaces with vanishing form had to be added in order to construct a full triangulation. 

The natural question is why we can not use the same procedure to triangulate the MHV or MHV Amplituhedra. The problem arises due to additional inequalities \(such as hABiji > 0 in eq. \(2.32\)\) that are required in the definition of the MHV Amplituhedron. 

While these additional inequalities do not correspond to any boundaries in the original MHV space, if we attempt to externally triangulate the MHV space by marginalizing over the signs of hABii\+1i brackets as \+ → ∗, the resulting spaces now have hABiji as boundaries. The corresponding canonical forms have spurious poles which can only be cancelled by adding additional spaces. Thus, this simple marginalization procedure does not extend straightforwardly to the chiral component spaces relevant for the MHV

and MHV Amplituhedra. 

– 97 –

C

Fixed signs in sign-flip-zero, two and four spaces

In this appendix, we discuss in more detail the sign-flip regions of section 4 and B. As shown in the main text, each achiral sign-flip region is defined by imposing fixed signs for certain hABii\+1i brackets only. There is a nice hierarchy of these spaces based on the number of sign-flips in the \{hABii\+1i\} sequence. The only non-empty spaces are the ones with zero, two, or four sign flips. As we argued in \(4\), the sign-flip-zero space is the most complicated, as measured by the number of boundaries and the complexity of the associated canonical form eqs. \(4.7\) and \(B.18\). The complexity of the sign-flip-two spaces is reduced \(see section 4\), and even more so for the sign-flip-four regions of section 4 which have at most eight boundaries. The corresponding logarithmic form is linked to the chiral octagon integrals, eq. \(4.28\), introduced in \[72\]. Besides the achiral spaces alluded to above, each geometry can be cut into two chiral components by imposing further constraints on additional brackets hABXi ≷ 0. 

Let us start our exposition with the achiral sign-flip-zero region S\(0\), eq. \(4.7\), 

S\(0\) : hABii\+1i > 0, 

i = 1, . . . , n

↔

\(C.1\)

No other signs of brackets are fixed inside S\(0\) besides the ones indicated in eq. \(C.1\). 

We can cut this achiral region into two chiral components, which correspond to MHV

and MHV one-loop amplitudes by imposing the inequalities of eq. \(2.31\) and eq. \(2.32\), 

respectively. We denote the corresponding chiral spaces by S\(0\)

and S\(0\) . Con-

MHV

MHV

cretely, the MHV component S\(0\)

can be defined by imposing additional n−3 condi-

MHV

tions eq. \(2.32\), 

hABii\+1i > 0 i ∈ \(1, . . . , n−1\) 

S\(0\)

:

↔

\(C.2\)

MHV

hAB1ii > 0

i ∈ \(3, . . . , n−1\)

Alternatively, imposing fixed signs for any sequence of brackets \{hAB2ii > 0\} etc. 

leads to an equivalent definition of S\(0\) . While a given set of only n − 3 fixed sings MHV

– 98 –

for the additional brackets \(such as \{hAB2ii > 0\} in eq. \(C.2\)\) is sufficient to define the MHV region, in fact all brackets hABiji > 0 \(for i < j\) are fixed inside the S\(0\) MHV

region. Let us note that no signs of any other brackets are fixed inside S\(0\) . 

MHV

The MHV chiral component is traditionally defined by a certain sign-flip constraint on the sequence \{hAB1ii\}, see the k = 0 instance of eq. \(2.12\), but we can equivalently impose the n−3 conditions of eq. \(2.31\), \{hAB1ii > 0\} , i ∈ \(3, . . . , n−1\) hABii\+1i > 0 i ∈ \(1, . . . , n−1\) 

S\(0\)

:

↔

, 

\(C.3\)

MHV

hAB1ii > 0

i ∈ \(3, . . . , n−1\)

where we used dotted lines in the circle figure eq. \(C.3\) to denote the positivity of the respective hAB1ii. While this set of signs suffices to fix the MHV region, in fact all hABiji>0 \(for i<j\) are positive inside S\(0\) , but no other signs of brackets are fixed. 

MHV

The achiral sign-flip-two space S\(2\) of eq. \(4.14\) is defined by a set of inequalities ij

on hABii\+1i brackets only that we graphically represent as

S\(2\)

↔

\(C.4\)

ij

No other signs are fixed in S\(2\). Compared to the sign-flip-zero space where we needed ij

to impose n−3 additional signs to chiralize the space, the achiral sign-flip-two region can be cut into two chiral components by fixing a single sign of the bracket hABiji. 

This bracket is extremely natural and involves the two positions i and j where the two

– 99 –

sign-flips occur, 

S\(2\),\+ : \{eq. \(C.4\), hABiji > 0\} ↔

, 

i < j, 

ij

\(C.5\)

S\(2\),− : \{eq. \(C.4\), hABiji < 0\} ↔

, 

i < j. 

ij

In the S\(2\),\+ region we have a fully positive index space for certain brackets involving ij

\(j, j\+1, . . . i−1, i\). By this we mean that all signs of the following brackets are fixed to be positive:

S\(2\),\+ : \{hABpqi > 0, hABpqi > 0\} , for p < q ∈ \{i, i\+1, . . . , j−1, j\}, \(C.6\)

ij

where the inequalities on p, q are to be understood in the cyclic sense. In contrast, for S\(2\),\+, arbitrary non-adjacent brackets of the “negative region” do not have fixed signs. 

ij

Similar to the discussion for S\(2\),\+, for S\(2\),− we have

ij

ij

S\(2\),− : \{hABpqi < 0, hABpqi < 0\}, 

, for p < q ∈ \{i, i\+1, . . . , j−1, j\}, 

\(C.7\)

ij

in the fully negative region involving \(i, i\+1, . . . , j−1, j\) the same set of brackets are fixed to be negative and the non-adjacent brackets in the “positive region” do not have a fixed sign. Note that the sign-inequalities eq. \(C.6\) and eq. \(C.7\) also apply for q = p\+1 where both hABpqi and hABpqi collapse to hABpp\+1i \(up to a positive bracket of external twistors\). 

The sign-flip-four space S\(4\) eq. \(4.6\) is given by four patches of positive and ik\`j

– 100 –

negative hABaa\+1i brackets, graphically represented as S\(4\)

↔

. 

\(C.8\)

ik\`j

In addition to these basic signs which define S\(4\) , there are many more signs which are ik\`j

fixed automatically just from the hABaa\+1i conditions alone even before cutting the achiral space into its chiral sub-components. In fact, the four patches in index space are either fully positive or fully negative. This means that all signs of the following brackets are fixed

p < q ∈ \{j, j\+1, . . . , i−1, i \} 

\{hABpqi > 0, hABpqi > 0\} , for

p < q ∈ \{k, k\+1, . . . , \`−1, \`\}

\(C.9\)

p < q ∈ \{i, i\+1, . . . , k−1, k\} 

\{hABpqi < 0, hABpqi < 0\} , for

p < q ∈ \{\`, \`\+1, . . . , j−1, j\}

Cutting S\(4\) into two chiral components can be accomplished by specifying a single ik\`j

sign of one of the diagonals, hABiì, or hABkji. The first chiral component,S\(4\),\+, ik\`j

has both signs hABiì, hABkji > 0 positive, while the second component, S\(4\),− has ik\`j

both signs hABiì, hABkji < 0 negative. But, in both cases fixing one sign implies the other. Hence we can represent the chiral components as:

S\(4\),\+ ↔

, 

S\(4\),− ↔

, 

ik\`j

ik\`j

i<k<\`<j

\(C.10\)

For each chiral component in eq. \(C.10\) the signs of many other brackets are automatically fixed. In addition to the signs eq. \(C.9\) that were already fixed in the achiral

– 101 –

space S\(4\) , we have

ik\`j

hABpqi > 0, for p ∈ \{j, j\+1, . . . , i−1, i\}, q ∈ \(k, k\+1, . . . , \`−1, \`\) S\(4\),\+ :

. \(C.11\)

ik\`j

hABpqi < 0, for p ∈ \(i, i\+1, . . . , k−1, k\), q ∈ \(\`, \`\+1, . . . , j−1, j\) Note that these inequalities also cover the signs of the diagonals hABiì>0, hABkji>0, and also hABiì<0, hABkji<0 so that in fact any single of these signs would be enough to specify the chiral subspace S\(4\),\+. 

ik\`j

The other chiral subspace S\(4\),− has a corresponding set of fixed brackets ik\`j

hABpqi < 0, for p ∈ \{j, j\+1, . . . , i−1, i\}, q ∈ \(k, k\+1, . . . , \`−1, \`\) S\(4\),− :

, \(C.12\)

ik\`j

hABpqi > 0, for p ∈ \(i, i\+1, . . . , k−1, k\), q ∈ \(\`, \`\+1, . . . , j−1, j\) which also covers the boundary cases such as hABiì < 0 which is enough to define S\(4\),−. Note that both set of signs for S\(4\),\+ and S\(4\),− are related by parity conjugation ik\`j

ik\`j

ik\`j

hABpqi ↔ hABpqi; this is a consequence of the chiral nature of these spaces. 

As usual, all the signs in this appendix are to be understood in the context of the usual twisted flips associated to the twisted cyclic symmetry. This means that hABiji > 0 is valid for 1 ≤ i < j ≤ n but we have to flip the sign if j passes n and now becomes smaller than i. Our sign-flip regions do not have an index space origin so that n can in principle be anywhere. For the explicit sign-flip regions appearing in the main text, we always fixed hAB1ni > 0, which forced the points n and 1 to be in a fully positive region. 

– 102 –

D

Gluing local geometries from two-dimensional projections

In this appendix, we summarize in detail how demanding a consistent geometry for the collection of local integral spaces selects a unique choice for the one-mass box, two-mass-hard box and chiral pentagons. This will be done by demanding that all spurious boundaries on various codimension-two projections cancel. The result of this exercise led us to the proposed spaces in section 5.3. 

Five-point discussion

First, let us look at the boundary when \(AB\) passes through the point Z2. On this cut surface, only the pentagon P24 and the box B45 in the expansion of the one-loop integrand in eq. \(5.1\) contribute. In eq. \(5.11\) we can identify the regions corresponding to the four options for the box B45 eq. \(5.3\) as well as the two different options for the pentagon eqs. \(5.4\)–\(5.5\). The B12 box does not contribute on this boundary. Using the labeling introduced in subsection 5.1, the options for the B45 spaces are: hAB34i hAB45i hAB15i hAB13i

B\(1\)

\+

\+

\+

\+

45

B\(2\)

\+

\+

\+

−

45

\+

−

\+

−

\(D.1\)

B\(3\)

−

\+

\+

\+

45

−

−

\+

\+

B\(4\)

−

\+

\+

−

45

−

−

\+

−

Note that all four distinct regions B\(i\) have three vertices, \(12\), \(23\) and \(13\), which 45

are the leading singularities of the box integral accessible from the codimension-two cut surface shown in eq. \(5.7\). The two choices for the pentagon spaces eqs. \(5.4\)–\(5.5\)

– 103 –

correspond to the regions

hAB34i hAB45i hAB15i hAB13i

P \(1\)

−

\+

\+

\+

24

\(D.2\)

−

\+

\+

−

P \(2\)

\+

−

\+

−

24

In this case both pentagon spaces have three vertices, \(24\), \(25\) and \(13\). As discussed throughout section 5.3, not all sign patterns which constitute a local integral necessarily contribute on a given cut surface; in this case, the space P \(1\) is composed of four sign 24

patterns, only two of which have the boundary \(AB\) = \(A2\). 

For our purposes, we require that upon combining the two pictures in eqs. \(D.1\) and

\(D.2\) the spaces for B45 and P24 must be such that the spurious leading singularities \(13\) and \(123\)∩\(245\) cancel geometrically \(however, since \(123\)∩\(245\) was not present in individual integrals in the first place, we do not get any constraints from this spurious leading singularity\). There are multiple ways of cancelling the spurious vertex \(13\). 

The first way of cancelling this point is by simply covering it twice with an overlapping region; an example of this is given by combining B\(2\) and P \(2\) as shown in the left 45

24

of eq. \(D.3\). Alternatively, we can cancel the spurious point by adding an additional region on one of the “other sides” of the vertex; an example of this is given by combining

– 104 –

B\(1\) and P \(2\), which is illustrated in the right of eq. \(D.3\). 

45

24

and

\(D.3\)

In the first example, we see that after cancelling overlapping regions we are left with exactly the same region \{\+, \+, \+, −\} as the original MHV Amplituhedron, while in the latter we are left with a different region which has the same boundaries. In fact, it is easy to see that any combination of the box and pentagon spaces will cancel this spurious boundary in a rather trivial fashion. The final result of any combination is equivalent to the MHV region, up to the addition of a region with zero form. The same argument holds for any other two-dimensional projection of the form \(AB\) = \(Ai\), so these pictures do not yield any constraints. 

The parity conjugate configuration where \(AB\) ⊂ \(123\) depicted in eq. \(5.12\) also leads to a trivially correct space, no matter which combination of box and pentagon spaces we take. This is a consequence of the fact that only a single local integral, B45, contributes on this cut. The chiral wavy-line numerator of the pentagon vanishes here. 

Let us now consider the configuration \(AB\) ⊂ \(234\), which corresponds to the on-shell function of eq. \(5.17\), where we have the spurious boundary when \(AB\) cuts the line \(15\), 

, 

\(D.4\)

– 105 –

which must be absent in the final space. For the boxes B12, B45 and pentagon we have, respectively, the contributions

hAB45i hAB15i hAB12i hAB35i

B\(1,3\)

−

\+

\+

\+

12

\(D.5\)

B\(2,4\)

−

\+

\+

−

12

−

\+

−

−

hAB45i hAB15i hAB12i hAB35i

B\(1,3\)

\+

\+

−

\+

45

\(D.6\)

B\(2,4\)

\+

\+

−

−

45

−

\+

−

−

hAB45i hAB15i hAB12i hAB35i

P \(1\)

\+

\+

−

\+

24

\+

\+

\+

−

\(D.7\)

−

\+

\+

\+

P \(2\)

−

\+

−

−

24

– 106 –

In these pictures the entire line hAB15i = 0 is spurious i.e., it is not a boundary of the Amplituhedron; therefore, it cannot be a boundary of the Amplituhedron-Prime either. Note that both regions for the boxes B12 and B45, as well as the pentagon regions do have access to the hAB15i = 0 boundary. As we have seen throughout this paper, the geometric cancellation of this spurious boundary is a stronger constraint than what is na¨ıvely observed at the level of adding canonical forms. There are two ways to combine these spaces to get the correct form: either we honestly cancel the boundary so it disappears from the full space, or we cover the entire line. In the latter case the codimension-three line hAB15i = 0 is a geometric boundary of the space, although the codimension-four points \(234\)∩\(351\), \(35\) and \(13\) on this line are not. 

This is unacceptable for our purposes here because geometrically it does not faithfully represent the correct boundary structure. In fact, such a combination can be seen explicitly by considering the following spaces: B\(1,3\), B\(1,3\) and P \(2\). The union of 12

45

24

these spaces has the same vertices \(23\), \(24\), \(34\) as the Amplituhedron, but also has the entire line hAB15i = 0:

hAB45i hAB15i hAB12i hAB35i

B\(1,3\)

−

\+

\+

\+

12

\(D.8\)

B\(1,3\)

\+

\+

−

\+

45

P \(2\)

−

\+

−

−

24

– 107 –

If instead we use the space P \(1\), we cancel the spurious boundary: 24

hAB45i hAB15i hAB12i hAB35i

B\(1,3\)

−

\+

\+

\+

12

B\(1,3\)

\+

\+

−

\+

45

\(D.9\)

P \(1\)

\+

\+

−

\+

24

\+

\+

\+

−

−

\+

\+

\+

Going through the eight possible combinations of spaces in eqs. \(D.5\)–\(D.7\), we see that only the following combinations cancel the spurious line hAB15i = 0: B\(1,3\), B\(1,3\), P \(1\), 

and

B\(2,4\), B\(2,4\), P \(1\) . 

\(D.10\)

12

45

24

12

45

24

Remarkably, we see that there is no uniform choice for the box spaces which cancels the spurious contributions of P \(2\) on this cut\! 

24

There are three remaining configurations \(AB\) ⊂ \(345\), \(451\), \(512\) to check. The \(345\) projection is trivially matched by any space for B12 as no other term contributes. 

For the \(451\) projection, only the box B12 and the pentagon contribute. In terms of the labeling above, on this cut surface the box choices \(1, 4\) and \(2, 3\) become

– 108 –

indistinguishable, respectively. The box B12 and pentagon correspond to the regions hAB12i hAB23i hAB34i hAB35i

B\(1,4\)

\+

\+

−

\+

12

\(D.11\)

B\(2,3\)

\+

\+

−

−

12

−

\+

−

−

hAB12i hAB23i hAB34i hAB35i

P \(1\)

−

\+

\+

\+

24

\(D.12\)

\+

−

\+

\+

P \(2\)

−

\+

\+

−

24

Demanding the cancellation of the boundary hAB23i = 0 we see that only two of the remaining four choices in eq. \(D.10\) survive, 

B\(2\), B\(2\), P \(1\), 

and

B\(3\), B\(3\), P \(1\). 

\(D.13\)

12

45

24

12

45

24

Following exactly the same procedure for the final configuration \(AB\) ⊂ \(512\) we find that both choices once again cancel the spurious boundary hAB34i = 0. 

– 109 –

Thus, at five points we are forced to choose the space, eq. \(5.4\), for the pentagon, and can cancel all spurious boundaries using two different choices for the boxes. Both choices are completely satisfactory at this multiplicity. However, only one of these solutions generalizes to higher points. This can be seen directly at six points, where an additional constraint arises: our five-point choice must be compatible with \(at least\) one of the two spaces in eqs. \(3.22\)–\(3.23\) for the two-mass hard box. 

Six-point discussion

Let us examine the natural extensions of the five-point solutions in eq. \(5.16\) relevant for the two-dimensional projection \(AB\) ⊂ \(234\), where the box and pentagon spaces are

B\(2\) =

, 

and

B\(3\) =

. 

\(D.14\)

456

456

P \(1\) =

\+

\+

\+

, 

24

\(D.15\)

For the two-mass-hard box B12,56 we have two choices, see eqs. \(3.22\)–\(3.23\):

B\(1\)

=

, 

and

B\(2\)

=

. 

\(D.16\)

12,56

12,56

– 110 –

Filling in the corresponding regions in eq. \(5.20\), the result for the one-mass box, pentagon and two-mass hard spaces are:

hAB45i hAB56i hAB16i hAB12i hAB35i

B\(2\)

\+

\+

\+

−

\+

456

−

\+

\+

−

−

−

−

\+

−

−

B\(3\)

\+

\+

\+

−

\+

456

P \(1\)

\+

\+

\+

−

\+

24

\+

\+

\+

\+

−

−

\+

\+

\+

\+

−

−

\+

\+

\+

P \(2\)

\+

−

−

\+

\+

24

\+

\+

−

\+

\+

B\(1\)

−

\+

\+

\+

\+

12,56

−

−

\+

\+

\+

B\(2\)

−

\+

\+

\+

−

12,56

−

−

\+

\+

−

−

\+

\+

−

−

−

−

\+

−

−

\(D.17\)

– 111 –

Demanding the boundaries hAB56i = 0 and hAB16i = 0 cancel fixes the choice of the two-mass hard box for both solutions:

B\(3\) , P \(1\), B\(1\) , 

and

B\(2\) , P \(1\), B\(2\) . 

\(D.18\)

456

24

12,56

456

24

12,56

We claim that while the first option works on all two-dimensional projections, the second option is incompatible with the cut surface where \(AB\) ⊂ \(345\). 

Indeed, 

repeating the above exercise, on this boundary the one-mass box B123, pentagon P35

and two-mass hard box contribute. Using the second option for the two-mass hard box B\(2\)

we find:

12,56

hAB45i hAB56i hAB16i hAB12i hAB35i

B\(2\)

−

−

\+

\+

\+

123

−

−

−

\+

\+

\+

\+

\+

\+

−

P \(1\)

\+

\+

\+

\+

−

35

−

\+

\+

\+

\+

\+

\+

\+

−

\+

\+

\+

−

−

\+

B\(2\)

\+

−

\+

\+

\+

12,56

\+

−

−

\+

\+

−

−

\+

\+

\+

−

−

−

\+

\+

\(D.19\)

We see that although the boundary hAB12i=0 is cancelled, the entire hAB16i=0

boundary is present in the final space. This selects the union of P \(1\) B\(2\) and B\(1\) as

35

456

12,56

the unique \(subject to the assumption that we make uniform choices for all boxes and pentagons, respectively\) candidate space whose boundary structure is identical to the original Amplituhedron on this cut surface. At six points, we have verified that this combination \(together with the other local integrals which did not contribute on the \(234\), \(345\) boundaries\) is free of all spurious boundaries. 

– 112 –

References

\[1\] N. Arkani-Hamed and J. Trnka, The Amplituhedron, JHEP 10 \(2014\) 030 \[1312.2007\]. 

\[2\] L. Brink, J. H. Schwarz and J. Scherk, Supersymmetric Yang-Mills Theories, 

Nucl.Phys. B121 \(1977\) 77. 

\[3\] F. Gliozzi, J. Scherk and D. I. Olive, Supersymmetry, Supergravity Theories and the Dual Spinor Model, Nucl.Phys. B122 \(1977\) 253. 

\[4\] N. Arkani-Hamed, Y. Bai and T. Lam, Positive Geometries and Canonical Forms, 

JHEP 11 \(2017\) 039 \[1703.04541\]. 

\[5\] N. Arkani-Hamed, Y. Bai, S. He and G. Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet, JHEP 05 \(2018\) 096

\[1711.09102\]. 

\[6\] N. Arkani-Hamed, S. He, T. Lam and H. Thomas, Binary Geometries, Generalized Particles and Strings, and Cluster Algebras, 1912.11764. 

\[7\] N. Arkani-Hamed, S. He and T. Lam, Stringy Canonical Forms, 1912.08707. 

\[8\] L. Ferro and T. Lukowski, Amplituhedra, and Beyond, 2007.04342. 

\[9\] P. Banerjee, A. Laddha and P. Raman, Stokes polytopes: the positive geometry for φ4

interactions, JHEP 08 \(2019\) 067 \[1811.05904\]. 

\[10\] A. Herderschee, S. He, F. Teng and Y. Zhang, On Positive Geometry and Scattering Forms for Matter Particles, 1912.08307. 

\[11\] A. Herderschee and F. Teng, Open associahedra and scattering forms, 2008.06418. 

\[12\] M. Jagadale and A. Laddha, On the Positive Geometry of Quartic Interactions III : One Loop Integrands from Polytopes, 2007.12145. 

\[13\] P. Aneesh, P. Banerjee, M. Jagadale, R. Rajan, A. Laddha and S. Mahato, On positive geometries of quartic interactions: Stokes polytopes, lower forms on associahedra and world-sheet forms, JHEP 04 \(2020\) 149 \[1911.06008\]. 

\[14\] N. Arkani-Hamed, Y.-T. Huang and S.-H. Shao, On the Positive Geometry of Conformal Field Theory, JHEP 06 \(2019\) 124 \[1812.07739\]. 

\[15\] N. Arkani-Hamed, P. Benincasa and A. Postnikov, Cosmological Polytopes and the Wavefunction of the Universe, 1709.02813. 

\[16\] N. Arkani-Hamed and P. Benincasa, On the Emergence of Lorentz Invariance and Unitarity from the Scattering Facet of Cosmological Polytopes, 1811.01125. 

\[17\] P. Benincasa and M. Parisi, Positive Geometries and Differential Forms with Non-Logarithmic Singularities I, 2005.03612. 

– 113 –

\[18\] A. Hodges, Eliminating spurious poles from gauge-theoretic amplitudes, JHEP 05

\(2013\) 135 \[0905.1473\]. 

\[19\] N. Arkani-Hamed, H. Thomas and J. Trnka, Unwinding the Amplituhedron in Binary, 

JHEP 01 \(2018\) 016 \[1704.05069\]. 

\[20\] N. Arkani-Hamed and J. Trnka, Into the Amplituhedron, 1312.7878. 

\[21\] A. Yelleshpur Srikant, Emergent unitarity from the amplituhedron, JHEP 01 \(2020\)

069 \[1906.10700\]. 

\[22\] R. Kojima, Triangulation of 2-loop MHV Amplituhedron from Sign Flips, JHEP 04

\(2019\) 085 \[1812.01822\]. 

\[23\] R. Kojima and C. Langer, Sign Flip Triangulations of the Amplituhedron, 2001.06473. 

\[24\] R. Kojima and J. Rao, Triangulation-free Trivialization of 2-loop MHV Amplituhedron, 

2007.15650. 

\[25\] N. Arkani-Hamed, C. Langer, A. Yelleshpur Srikant and J. Trnka, Deep Into the Amplituhedron: Amplitude Singularities at All Loops and Legs, Phys. Rev. Lett. 122

\(2019\) 051601 \[1810.08208\]. 

\[26\] C. Langer and A. Yelleshpur Srikant, All-loop cuts from the Amplituhedron, JHEP 04

\(2019\) 105 \[1902.05951\]. 

\[27\] S. Franco, D. Galloni, A. Mariotti and J. Trnka, Anatomy of the Amplituhedron, JHEP

03 \(2015\) 128 \[1408.3410\]. 

\[28\] S. N. Karp and L. K. Williams, The m=1 amplituhedron and cyclic hyperplane arrangements, Int. Math. Res. Not. 5 \(2019\) 1401 \[1608.08288\]. 

\[29\] S. N. Karp, L. K. Williams and Y. X. Zhang, Decompositions of amplituhedra, 

1708.09525. 

\[30\] T. Lukowski, On the Boundaries of the m=2 Amplituhedron, 1908.00386. 

\[31\] T. Lukowski and R. Moerman, Boundaries of the Amplituhedron with

amplituhedronBoundaries, 2002.07146. 

\[32\] I. Prlina, M. Spradlin, J. Stankowicz and S. Stanojevic, Boundaries of Amplituhedra and NMHV Symbol Alphabets at Two Loops, JHEP 04 \(2018\) 049 \[1712.08049\]. 

\[33\] I. Prlina, M. Spradlin, J. Stankowicz, S. Stanojevic and A. Volovich, All-Helicity Symbol Alphabets from Unwound Amplituhedra, JHEP 05 \(2018\) 159 \[1711.11507\]. 

\[34\] T. Dennen, I. Prlina, M. Spradlin, S. Stanojevic and A. Volovich, Landau Singularities from the Amplituhedron, JHEP 06 \(2017\) 152 \[1612.02708\]. 

\[35\] L. J. Dixon, M. von Hippel, A. J. McLeod and J. Trnka, Multi-loop positivity of the planar N = 4 SYM six-point amplitude, JHEP 02 \(2017\) 112 \[1611.08325\]. 

– 114 –

\[36\] G. Salvatori and S. L. Cacciatori, Hyperbolic Geometry and Amplituhedra in 1\+2

dimensions, JHEP 08 \(2018\) 167 \[1803.05809\]. 

\[37\] Y. Bai, S. He and T. Lam, The Amplituhedron and the One-loop Grassmannian Measure, JHEP 01 \(2016\) 112 \[1510.03553\]. 

\[38\] Y. Bai and S. He, The Amplituhedron from Momentum Twistor Diagrams, JHEP 02

\(2015\) 065 \[1408.2459\]. 

\[39\] T. Lam, Amplituhedron cells and Stanley symmetric functions, Commun. Math. Phys. 

343 \(2016\) 1025 \[1408.5531\]. 

\[40\] B. Eden, P. Heslop and L. Mason, The Correlahedron, JHEP 09 \(2017\) 156

\[1701.00453\]. 

\[41\] Y. An, Y. Li, Z. Li and J. Rao, All-loop Mondrian Diagrammatics and 4-particle Amplituhedron, JHEP 06 \(2018\) 023 \[1712.09994\]. 

\[42\] J. Rao, 4-particle amplituhedronics for 3-5 loops, Nucl. Phys. B 943 \(2019\) 114625

\[1806.01765\]. 

\[43\] N. Arkani-Hamed, F. Cachazo, C. Cheung and J. Kaplan, A Duality For The S Matrix, 

JHEP 03 \(2010\) 020 \[0907.5418\]. 

\[44\] L. Mason and D. Skinner, Dual Superconformal Invariance, Momentum Twistors and Grassmannians, JHEP 11 \(2009\) 045 \[0909.0250\]. 

\[45\] N. Arkani-Hamed, F. Cachazo and C. Cheung, The Grassmannian Origin Of Dual Superconformal Invariance, JHEP 03 \(2010\) 036 \[0909.0483\]. 

\[46\] N. Arkani-Hamed, J. Bourjaily, F. Cachazo and J. Trnka, Unification of Residues and Grassmannian Dualities, JHEP 01 \(2011\) 049 \[0912.4912\]. 

\[47\] N. Arkani-Hamed, J. Bourjaily, F. Cachazo and J. Trnka, Local Spacetime Physics from the Grassmannian, JHEP 01 \(2011\) 108 \[0912.3249\]. 

\[48\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. B. Goncharov, A. Postnikov and J. Trnka, Grassmannian Geometry of Scattering Amplitudes. Cambridge University Press, 4, 2016, 10.1017/CBO9781316091548, \[1212.5605\]. 

\[49\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, S. Caron-Huot and J. Trnka, The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM, JHEP 01 \(2011\)

041 \[1008.2958\]. 

\[50\] P. Benincasa, On-shell diagrammatics and the perturbative structure of planar gauge theories, 1510.03642. 

\[51\] P. Benincasa and D. Gordo, On-shell diagrams and the geometry of planar N < 4 SYM

theories, JHEP 11 \(2017\) 192 \[1609.01923\]. 

– 115 –

\[52\] E. Herrmann and J. Trnka, Gravity On-shell Diagrams, JHEP 11 \(2016\) 136

\[1604.03479\]. 

\[53\] P. Heslop and A. E. Lipstein, On-shell diagrams for N = 8 supergravity amplitudes, 

JHEP 06 \(2016\) 069 \[1604.03046\]. 

\[54\] R. Frassek, D. Meidinger, D. Nandan and M. Wilhelm, On-shell diagrams, Gramannians and integrability for form factors, JHEP 01 \(2016\) 182 \[1506.08192\]. 

\[55\] J. Kim and S. Lee, Positroid Stratification of Orthogonal Grassmannian and ABJM

Amplitudes, JHEP 09 \(2014\) 085 \[1402.1119\]. 

\[56\] Y.-t. Huang, C. Wen and D. Xie, The Positive orthogonal Grassmannian and loop amplitudes of ABJM, J. Phys. A 47 \(2014\) 474008 \[1402.1479\]. 

\[57\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo and J. Trnka, Singularity Structure of Maximally Supersymmetric Scattering Amplitudes, Phys. Rev. Lett. 113 \(2014\) 261603

\[1410.0354\]. 

\[58\] Z. Bern, E. Herrmann, S. Litsey, J. Stankowicz and J. Trnka, Logarithmic Singularities and Maximally Supersymmetric Amplitudes, JHEP 06 \(2015\) 202 \[1412.8584\]. 

\[59\] Z. Bern, E. Herrmann, S. Litsey, J. Stankowicz and J. Trnka, Evidence for a Nonplanar Amplituhedron, JHEP 06 \(2016\) 098 \[1512.08591\]. 

\[60\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. Postnikov and J. Trnka, On-Shell Structures of MHV Amplitudes Beyond the Planar Limit, JHEP 06 \(2015\) 179

\[1412.8475\]. 

\[61\] S. Franco, D. Galloni, B. Penante and C. Wen, Non-Planar On-Shell Diagrams, JHEP

06 \(2015\) 199 \[1502.02034\]. 

\[62\] J. L. Bourjaily, S. Franco, D. Galloni and C. Wen, Stratifying On-Shell Cluster Varieties: the Geometry of Non-Planar On-Shell Diagrams, JHEP 10 \(2016\) 003

\[1607.01781\]. 

\[63\] D. Damgaard, L. Ferro, T. Lukowski and M. Parisi, The Momentum Amplituhedron, 

JHEP 08 \(2019\) 042 \[1905.04216\]. 

\[64\] L. Ferro, T. Lukowski and R. Moerman, From Momentum Amplituhedron Boundaries to Amplitude Singularities and Back, 2003.13704. 

\[65\] P. Tourkine, On integrands and loop momentum in string and field theory, 1901.02432. 

\[66\] R. Ben-Israel, A. G. Tumanov and A. Sever, Scattering amplitudes — Wilson loops duality for the first non-planar correction, JHEP 08 \(2018\) 122 \[1802.09395\]. 

\[67\] R. Britto, F. Cachazo and B. Feng, New recursion relations for tree amplitudes of gluons, Nucl. Phys. B 715 \(2005\) 499 \[hep-th/0412308\]. 

– 116 –

\[68\] R. Britto, F. Cachazo, B. Feng and E. Witten, Direct proof of tree-level recursion relation in Yang-Mills theory, Phys. Rev. Lett. 94 \(2005\) 181602 \[hep-th/0501052\]. 

\[69\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. Hodges and J. Trnka, A Note on Polytopes for Scattering Amplitudes, JHEP 04 \(2012\) 081 \[1012.6030\]. 

\[70\] N. Arkani-Hamed, A. Hodges and J. Trnka, Positive Amplitudes In The Amplituhedron, JHEP 08 \(2015\) 030 \[1412.8478\]. 

\[71\] L. Ferro, T. Lukowski, A. Orta and M. Parisi, Towards the Amplituhedron Volume, 

JHEP 03 \(2016\) 014 \[1512.04954\]. 

\[72\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo and J. Trnka, Local Integrals for Planar Scattering Amplitudes, JHEP 06 \(2012\) 125 \[1012.6032\]. 

\[73\] R. Penrose, Twistor algebra, J. Math. Phys. 8 \(1967\) 345. 

\[74\] Z. Bern, L. J. Dixon, D. C. Dunbar and D. A. Kosower, One loop n point gauge theory amplitudes, unitarity and collinear limits, Nucl.Phys. B425 \(1994\) 217

\[hep-ph/9403226\]. 

\[75\] F. Cachazo, Sharpening The Leading Singularity, 0803.1988. 

\[76\] E. Herrmann and J. Parra-Martinez, Logarithmic forms and differential equations for Feynman integrals, JHEP 02 \(2020\) 099 \[1909.04777\]. 

\[77\] E. Herrmann, C. Langer, J. Trnka and M. Zheng, Positive Geometries for One-Loop Chiral Octagons, 2007.12191. 

\[78\] J. L. Bourjaily, F. Dulat and E. Panzer, Manifestly Dual-Conformal Loop Integration, 

Nucl. Phys. B 942 \(2019\) 251 \[1901.02887\]. 

– 117 –


# Document Outline

+ 1 Introduction 
+ 2 Amplituhedron geometry  
	+ 2.1 Topological sign-flip definition of the Amplituhedron 
	+ 2.2 One-loop MHV and MHV spaces 
	+ 2.3 Boundaries of MHV amplitudes 
	+ 2.4 Positivity and the dual Amplituhedron 

+ 3 Geometry of dlog forms  
	+ 3.1 dlog forms for pentagon integrands 
	+ 3.2 From dlog's to geometry 
	+ 3.3 No-go theorem for external triangulation 

+ 4 Sign-flip regions 
+ 5 Local geometries and the Amplituhedron-Prime  
	+ 5.1 Chiral regions for boxes and pentagons 
	+ 5.2 Two-dimensional projections 
	+ 5.3 Gluing regions 
	+ 5.4 Amplituhedron-Prime 

+ 6 Triangulation of the dual Amplituhedron  
	+ 6.1 Dualizing polygons 
	+ 6.2 Dual spaces of chiral pentagons 
	+ 6.3 Two-dimensional triangulations 

+ 7 Conclusion 
+ A Configuration of lines in momentum twistor space 
+ B External triangulations 
+ C Fixed signs in sign-flip-zero, two and four spaces 
+ D Gluing local geometries from two-dimensional projections



