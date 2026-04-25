# Positive Geometries and Canonical Forms

SOURCE_PDF: sources/pdfs/Arkani-Hamed_2017_Positive-Geometries-and-Canonical-Forms_arXiv-1703.04541.pdf



<!-- page 1 -->

Prepared for submission to JHEP
Positive Geometries and Canonical Forms
Nima Arkani-Hamed,a Yuntao Bai,b Thomas Lamc
aSchool of Natural Sciences, Institute for Advanced Study, Princeton, NJ 08540, USA
bDepartment of Physics, Princeton University, Princeton, NJ 08544, USA
cDepartment of Mathematics, University of Michigan, 530 Church St, Ann Arbor, MI 48109, USA
Abstract: Recent years have seen a surprising connection between the physics of scat-
tering amplitudes and a class of mathematical objects–the positive Grassmannian, positive
loop Grassmannians, tree and loop Amplituhedra–which have been loosely referred to as
“positive geometries”. The connection between the geometry and physics is provided by a
unique diﬀerential form canonically determined by the property of having logarithmic sin-
gularities (only) on all the boundaries of the space, with residues on each boundary given
by the canonical form on that boundary. The structures seen in the physical setting of the
Amplituhedron are both rigid and rich enough to motivate an investigation of the notions
of “positive geometries” and their associated “canonical forms” as objects of study in their
own right, in a more general mathematical setting. In this paper we take the ﬁrst steps in
this direction. We begin by giving a precise deﬁnition of positive geometries and canonical
forms, and introduce two general methods for ﬁnding forms for more complicated positive
geometries from simpler ones–via “triangulation” on the one hand, and “push-forward”
maps between geometries on the other. We present numerous examples of positive geome-
tries in projective spaces, Grassmannians, and toric, cluster and ﬂag varieties, both for the
simplest “simplex-like” geometries and the richer “polytope-like” ones. We also illustrate a
number of strategies for computing canonical forms for large classes of positive geometries,
ranging from a direct determination exploiting knowledge of zeros and poles, to the use of
the general triangulation and push-forward methods, to the representation of the form as
volume integrals over dual geometries and contour integrals over auxiliary spaces. These
methods yield interesting representations for the canonical forms of wide classes of positive
geometries, ranging from the simplest Amplituhedra to new expressions for the volume of
arbitrary convex polytopes.
arXiv:1703.04541v2  [hep-th]  30 Jul 2017

<!-- page 2 -->

Contents
1 Introduction 1
2 Positive geometries 5
2.1 Positive geometries and their canonical forms 5
2.2 Pseudo-positive geometries 6
2.3 Reversing orientation, disjoint unions and direct products 7
2.4 One-dimensional positive geometries 7
3 Triangulations of positive geometries 8
3.1 Triangulations of pseudo-positive geometries 8
3.2 Signed triangulations 8
3.3 The Grothendieck group of pseudo-positive geometries in X 9
3.4 Physical versus spurious poles 10
4 Morphisms of positive geometries 11
5 Generalized simplices 12
5.1 The standard simplex 12
5.2 Projective simplices 13
5.3 Generalized simplices on the projective plane 15
5.3.1 An example of a non-normal geometry 18
5.4 Generalized simplices in higher-dimensional projective spaces 19
5.5 Grassmannians 21
5.5.1 Grassmannians and positroid varieties 21
5.5.2 Positive Grassmannians and positroid cells 21
5.6 Toric varieties and their positive parts 22
5.6.1 Projective toric varieties 22
5.6.2 The canonical form of a toric variety 23
5.7 Cluster varieties and their positive parts 24
5.8 Flag varieties and total positivity 25
6 Generalized polytopes 26
6.1 Projective polytopes 26
6.1.1 Projective and Euclidean polytopes 26
6.1.2 Cyclic polytopes 27
6.1.3 Dual polytopes 28
6.2 Generalized polytopes on the projective plane 29
6.3 A naive positive part of partial ﬂag varieties 30
6.4 L-loop Grassmannians 31
6.5 Grassmann, loop and ﬂag polytopes 33
6.6 Amplituhedra and scattering amplitudes 35
– i –

<!-- page 3 -->

7 Canonical forms 36
7.1 Direct construction from poles and zeros 36
7.1.1 Cyclic polytopes 37
7.1.2 Generalized polytopes on the projective plane 40
7.2 Triangulations 41
7.2.1 Projective polytopes 41
7.2.2 Generalized polytopes on the projective plane 43
7.2.3 Amplituhedra and BCFW recursion 43
7.2.4 The tree Amplituhedron for m = 1, 2 45
7.2.5 A 1-loop Grassmannian 49
7.2.6 An example of a Grassmann polytope 51
7.3 Push-forwards 52
7.3.1 Projective simplices 53
7.3.2 Algebraic moment map and an algebraic analogue of the
Duistermaat-Heckman measure 56
7.3.3 Projective polytopes from Newton polytopes 58
7.3.4 Recursive properties of the Newton polytope map 61
7.3.5 Newton polytopes from constraints 63
7.3.6 Generalized polytopes on the projective plane 66
7.3.7 Amplituhedra 68
7.4 Integral representations 70
7.4.1 Dual polytopes 70
7.4.2 Laplace transforms 73
7.4.3 Dual Amplituhedra 75
7.4.4 Dual Grassmannian volumes 76
7.4.5 Wilson loops and surfaces 78
7.4.6 Projective space contours part I 82
7.4.7 Projective space contours part II 88
7.4.8 Grassmannian contours 90
8 Integration of canonical forms 91
8.1 Canonical integrals 91
8.2 Duality of canonical integrals and the Aomoto form 92
9 Positively convex geometries 93
10 Beyond “rational” positive geometries 95
11 Outlook 101
A Assumptions on positive geometries 102
A.1 Assumptions on X≥0 and deﬁnition of boundary components 102
A.2 Assumptions on X 103
A.3 The residue operator 104
– ii –

<!-- page 4 -->

B Near-equivalence of three notions of signed triangulation 104
C Rational diﬀerential forms on projective spaces and Grassmannians 105
C.1 Forms on projective spaces 105
C.2 Forms on Grassmannians 106
C.3 Forms on L-loop Grassmannians 108
D Cones and projective polytopes 108
E Monomial parametrizations of polytopes 109
F The global residue theorem 114
G The canonical form of a toric variety 115
H Canonical form of a polytope via toric varieties 116
I Oriented matroids 119
J The Tarski-Seidenberg theorem 120
1 Introduction
Recent years have revealed an unexpected and fascinating new interplay between physics
and geometry in the study of gauge theory scattering amplitudes. In the context of planar
N = 4 super Yang-Mills theory, we now have a complete formulation of the physics of
scattering amplitudes in terms of the geometry of the “Amplituhedron” [1–4], which is a
Grassmannian generalization of polygons and polytopes. Neither space-time nor Hilbert
space make any appearance in this formulation – the associated physics of locality and
unitarity arise as consequences of the geometry.
This new connection between physics and mathematics involves a number of interesting
mathematical ideas. The notion of “positivity” plays a crucial role. In its simplest form
we consider the interior of a simplex in projective space Pn−1 as points with homogeneous
co-ordinates ( x0, . . . , xn−1) with all xa > 0. We can call this the “positive part” Pn−1
>0 of
projective space; thinking of projective space as the space of 1-planes in n dimensions, we
can also call this the “positive part” of the Grassmannian of 1-planes in n dimensions,
G>0(1, n).
This notion generalizes from G>0(1, n) to the “positive part” of the Grassmannian of
k-planes in n dimensions, G>0(k, n) [5, 6]. The Amplituhedron is a further extension of
this idea, roughly generalizing the positive Grassmannian in the same way that convex
plane polygons generalize triangles. These spaces have loosely been referred to as “positive
geometries” in the physics literature; like polygons and polytopes they have an “interior”,
with boundaries or facets of all dimensionalities. Another crucial idea, which gives a
– 1 –

<!-- page 5 -->

0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x
y
(a) dxdy
xy(1−x−y)
0.0 0.5 1.0 1.5 2.0
0.0
0.5
1.0
1.5
2.0
x
y (b) dxdy(12−x−4y)
x(2y−x)(3−x−y)(2−y)
/Minus1.0 /Minus0.5 0.0 0.5 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x
y
(c) (3
√
11/5)dxdy
(1−x2−y2)(y−(1/10))
/Minus1.0 /Minus0.5 0.0 0.5 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x
y (d) 2
√
3(1+2y)dxdy
(1−x2−y2)(
√
3y+x)(
√
3y−x)
/Minus1.0 /Minus0.5 0.0 0.5 1.0
/Minus1.0
/Minus0.5
0.0
0.5
1.0
x
y
(e) 0 dxdy
Figure 1: Canonical forms of (a) a triangle, (b) a quadrilateral, (c) a segment of the unit
disk with y≥ 1/10, (d) a sector of the unit disk with central angle 2 π/3 symmetric about
the y-axis, and (e) the unit disk. The form is identically zero for the unit disk because there
are no zero-dimensional boundaries. For each of the other ﬁgures, the form has simple poles
along each boundary component, all leading residues are±1 at zero-dimensional boundaries
and zero elsewhere, and the form is positively oriented on the interior.
dictionary for converting these geometries into physical scattering amplitudes, is a certain
(complex) meromorphic diﬀerential form that is canonically associated with the positive
geometry. This form is ﬁxed by the requirement of having simple poles on (and only on)
all the boundaries of the geometry, with its residue along each being given by the canonical
– 2 –

<!-- page 6 -->

form of the boundary. The calculation of scattering amplitudes is then reduced to the
natural mathematical question of determining this canonical form.
While the ideas of positive geometries and their associated canonical forms have arisen
in the Grassmannian/Amplituhedron context related to scattering amplitudes, they seem
to be deeper ideas worthy of being understood on their own terms in their most natural
and general mathematical setting. Our aim in this paper is to take the ﬁrst steps in this
direction.
To begin with, it is important to make the notion of a positive geometry precise. For
instance, it is clear that the interior of a triangle or a quadrilateral are positive geometries:
we have a two-dimensional space bounded by 1 and 0 dimensional boundaries, and there is
a unique 2-form with logarithmic singularities on these boundaries. But clearly the interior
of a circle should not be a positive geometry in the same sense, for the simple reason that
there are no 0-dimensional boundaries! See Figures 1a, 1b & 1e for an illustration.
We will formalize these intuitive notions in Section 2, and give a precise deﬁnition of
a “positive geometry”: the rough idea is to deﬁne a positive geometry by the (recursive)
requirement of the existence of a unique form with logarithmic singularities on its bound-
aries. As we will see in subsequent sections, in the plane this deﬁnition allows the interior of
polygons but not the inside of a circle, and will also allow more general positive geometries
than polygons, for instance bounded by segments of lines and conics. In Figure 1 we show
some simple examples of positive geometries in the plane together with their associated
canonical forms.
In Sections 3 and 4 we introduce two general methods for relating more complicated
positive geometries to simpler ones. The ﬁrst method is “triangulation”. If a positive
geometry X≥0 can be “tiled” by a collection of positive geometries Xi,≥0 with mutually
non-overlapping interiors, then the canonical form Ω( X≥0) of X≥0 is given by the sum of
the forms for the pieces Ω( X≥0) = ∑
i Ω(Xi,≥0). We say therefore that the canonical form
is “triangulation independent”, a property that has played a central role in the physics
literature, whose derivation we present in Section 3. The second is the “push-forward”
method. If we have a positive geometry X≥0, and if we have a morphism (a special type
of map deﬁned in Section 4) that maps X≥0 into another positive geometry Y≥0, then the
canonical form on Y≥0 is the push-forward of the canonical form on X≥0. While both these
statements are simple and natural, they are interesting and non-trivial. The “triangula-
tion” method has been widely discussed in the physics literature on Grassmannians and
Amplituhedra. The push-forward method is new, and will be applied in interesting ways
in later sections.
Sections 5 and 6 are devoted to giving many examples of positive geometries, which nat-
urally divide into the simplest “simplex-like” geometries, and more complicated “polytope-
like” geometries. A nice way of characterizing the distinction between the two can already
be seen by looking at the simple examples in Figure 1. Note that the “simplest looking”
positive geometries–the triangle and the half-disk, also have the simplest canonical forms,
with the important property of having only poles but no zeros, while the “quadrilateral”
and “pizza slice” have zeros associated with non-trivial numerator factors. Generaliz-
ing these examples, we deﬁne “simplex-like” positive geometries to be ones for which the
– 3 –

<!-- page 7 -->

canonical form has no zeros, while “polytope-like” positive geometries are ones for which
the canonical form may have zeros.
We will provide several illustrative examples of generalized simplices (i.e. simplex-
like positive geometries) in Section 5. The positive Grassmannian is an example, but we
present a number of other examples as well, including generalized simplices bounded by
higher-degree surfaces in projective spaces, as well as the positive parts of toric, cluster
and ﬂag varieties.
In Section 6 we discuss a number of examples of generalized polytopes (i.e. polytope-
like positive geometries): the familiar projective polytopes, Grassmann polytopes [7], and
polytopes in partial ﬂag varieties and loop Grassmannians. The tree Amplituhedron is an
important special case of a Grassmann polytope; just as cyclic polytopes are an important
special class of polytopes in projective space. We study in detail the simplest Grassmann
polytope that is not an Amplituhedron, and determine its canonical form by triangulation.
We also discuss loop and ﬂag polytopes, which generalize the all-loop-order Amplituhedron.
In Section 7 we take up the all-important question of determining the canonical form
associated with positive geometries. It is fair to say that no “obviously morally correct”
way of ﬁnding the canonical form for general Amplituhedra has yet emerged; instead several
interesting strategies have been found to be useful. We will review some of these ideas and
present a number of new ways of determining the form in various special cases. We ﬁrst
discuss the most direct and brute-force construction of the form following from a detailed
understanding of its poles and zeros along the lines of [8]. Next we illustrate the two general
ideas of “triangulation” and “push-forward” in action. We give several examples of tri-
angulating more complicated positive geometries with generalized simplices and summing
the canonical form for the simplices to determine the canonical form of the whole space.
We also give examples of morphisms from simplices into positive geometries. Typically
the morphisms involve solving coupled polynomial equation with many solutions, and the
push-forward of the form instructs us to sum over these solutions. Even for the familiar case
of polytopes in projective space, this gives a beautiful new representation of the canonical
form, which is formulated most naturally in the setting of toric varieties. Indeed, there
is a striking parallel between the polytope canonical form and the Duistermaat-Heckman
measure of a toric variety. We also give two simple examples of the push-forward map
from a simplex into the Amplituhedron. We ﬁnally introduce a new set of ideas for deter-
mining the canonical form associated with integral representations. These are inspired by
the Grassmannian contour integral formula for scattering amplitudes, as well as the (still
conjectural) notion of integration over a “dual Amplituhedron”. In addition to giving new
representations of forms for polytopes, we will obtain new representations for classes of Am-
plituhedron forms as contour integrals over the Grassmannian (for “ N M HV amplitudes”
in physics language), as well as dual-Amplituhedron-like integrals over a “Wilson-loop” to
determine the canonical forms for all tree Amplituhedra with m = 2.
The Amplituhedron involves a number of independent notions of positivity. It gener-
alizes the notion of an “interior” in the Grassmannian, but also has a notion of convexity,
associated with demanding “positive external data”. Thus the Amplituhedron generalizes
the notion of the interior of convex polygons, while the interior of non-convex polygons also
– 4 –

<!-- page 8 -->

qualify as positive geometries by our deﬁnitions. In Section 9 we deﬁne what extra features
a positive geometry should have to give a good generalization of “convexity”, which we will
call “positive convexity”. Brieﬂy the requirement is that the canonical form should have
no poles and no zeros inside the positive geometry. This is a rather miraculous (and largely
numerically veriﬁed) feature of the canonical form for Amplituhedra with evenm [8], which
is very likely “positively convex”, while the simplest new example of a Grassmann polytope
is not.
Furthermore, it is likely that our notion of positive geometry needs to be extended in
an interesting way. Returning to the simple examples of Figure 1, it may appear odd that
the interior of a circle is not a positive geometry while any convex polygon is one, given
that we can approximate a circle arbitrarily well as a polygon with the number of vertices
going to inﬁnity. The resolution of this little puzzle is that while the canonical form for a
polygon with any ﬁxed number of sides is a rational function with logarithmic singularities,
in the inﬁnite limit it is not a rational function–the poles condense to give a function with
branch cuts instead. The notion of positive geometry we have described in this paper is
likely the special case of a “rational” positive geometry, which needs to be extended in
some way to cover cases where the canonical form is not rational. This is discussed in more
detail in Section 10.
Our investigations in this paper are clearly only scratching the surface of what appears
to be a deep and rich set of ideas, and in Section 11 we provide an outlook on immediate
avenues for further exploration.
2 Positive geometries
2.1 Positive geometries and their canonical forms
We let PN denote N-dimensional complex projective space with the usual projection map
CN+1\{ 0}→ PN, and we let PN(R) denote the image of RN+1\{ 0} in PN.
Let X be a complex projective algebraic variety , which is the solution set in PN of a
ﬁnite set of homogeneous polynomial equations. We will assume that the polynomials have
real coeﬃcients. We then denote by X(R) the real part of X, which is the solution set in
PN(R) of the same set of equations.
A semialgebraic set in PN(R) is a ﬁnite union of subsets, each of which is cut out
by ﬁnitely many homogeneous real polynomial equations {x∈ PN(R)| p(x) = 0} and
homogeneous real polynomial inequalities {x∈ PN(R)| q(x) > 0}. To make sense of the
inequality q(x) > 0 , we ﬁrst ﬁnd solutions in RN+1\{ 0}, and then take the image of the
solution set in PN(R).
We deﬁne a D-dimensional positive geometry to be a pair ( X, X≥0), where X is an
irreducible complex projective variety of complex dimension D and X≥0 ⊂ X(R) is a
nonempty oriented closed semialgebraic set of real dimension D satisfying some technical
assumptions discussed in Appendix A where the boundary components of X≥0 are deﬁned,
together with the following recursive axioms:
– 5 –

<!-- page 9 -->

• For D = 0: X is a single point and we must have X≥0 = X. We deﬁne the 0-form
Ω(X, X≥0) on X to be±1 depending on the orientation of X≥0.
• For D > 0: we must have
(P1) Every boundary component ( C, C≥0) of ( X, X≥0) is a positive geometry of di-
mension D−1.
(P2) There exists a unique nonzero rational D-form Ω(X, X≥0) on X constrained by
the residue relation ResCΩ(X, X≥0) = Ω(C, C≥0) along every boundary compo-
nent C, and no singularities elsewhere.
See Appendix A.3 for the deﬁnition of the residue operator Res. In particular, all
leading residues (i.e. Res applied D times on various boundary components) of Ω( X, X≥0)
must be±1. We refer to X as the embedding space and D as the dimension of the positive
geometry. The form Ω( X, X≥0) is called the canonical form of the positive geometry
(X, X≥0). As a shorthand, we will often write X≥0 to denote a positive geometry (X, X≥0),
and write Ω( X≥0) for the canonical form. We note however that X usually contains
inﬁnitely many positive geometries, so the notation X≥0 is slightly misleading. Sometimes
we distinguish the interior X>0 of X≥0 from X≥0 itself, in which case we call X≥0 the
nonnegative part and X>0 the positive part. We will also refer to the codimension d
boundary components of a positive geometry ( X, X≥0), which are the positive geometries
obtained by recursively taking boundary components d times.
We stress that the existence of the canonical form is a highly non-trivial phenomenon.
The ﬁrst four geometries in Figure 1 are all positive geometries.
2.2 Pseudo-positive geometries
A slightly more general variant of positive geometries will be useful for some of our argu-
ments. We deﬁne a D-dimensional pseudo-positive geometry to be a pair ( X, X≥0) of the
same type as a positive geometry, but now X≥0 is allowed to be empty, and the recursive
axioms are:
• For D = 0: X is a single point. If X≥0 = X, we deﬁne the 0-form Ω( X, X≥0) on X
to be±1 depending on the orientation of X≥0. If X≥0 =∅, we set Ω( X, X≥0) = 0.
• For D > 0: if X≥0 is empty, we set Ω(X, X≥0) = 0. Otherwise, we must have:
(P1*) Every boundary component ( C, C≥0) of (X, X≥0) is a pseudo-positive geometry
of dimension D−1.
(P2*) There exists a unique rational D-form Ω( X, X≥0) on X constrained by the
residue relation ResCΩ(X, X≥0) = Ω(C, C≥0) along every boundary component
C and no singularities elsewhere.
We use the same nomenclature for X, X≥0, Ω as in the case of positive geometries. The key
diﬀerences are that we allow X≥0 =∅, and we allow Ω( X, X≥0) = 0. Note that there are
pseudo-positive geometries with Ω( X, X≥0)̸= 0 that are not positive geometries. When
– 6 –

<!-- page 10 -->

Ω(X, X≥0) = 0, we declare that X≥0 is a null geometry. A basic example of a null geometry
is the disk of Figure 1e.
2.3 Reversing orientation, disjoint unions and direct products
We indicate the simplest ways that one can form new positive geometries from old ones.
First, if ( X, X≥0) is a positive geometry (resp. pseudo-positive geometry), then so is
(X, X−
≥0), where X−
≥0 denotes the same space X≥0 with reversed orientation. Naturally, its
boundary components C−
i also acquire the reversed orientation, and we have Ω(X, X≥0) =
−Ω(X, X−
≥0).
Second, suppose ( X, X1
≥0) and ( X, X2
≥0) are pseudo-positive geometries, and suppose
that they are disjoint: X1
≥0∩ X2
≥0 =∅. Then the disjoint union ( X, X1
≥0∪ X2
≥0) is itself a
pseudo-positive geometry, and we have Ω( X1
≥0∪ X2
≥0) = Ω(X1
≥0) + Ω(X2
≥0). This is easily
proven by an induction on dimension. The boundary components of X1
≥0∩ X2
≥0 are either
boundary components of one of the two original geometries, or a disjoint union of such
boundary components. For example, a closed interval inP1(R) is a one-dimensional positive
geometry (see Section 2.4), and thus any disjoint union of intervals is again a positive
geometry. This is a special case of the notion of a triangulation of positive geometries
explored in Section 3.
Third, suppose ( X, X≥0) and ( Y, Y≥0) are positive geometries (resp. pseudo-positive
geometries). Then the direct product X× Y is naturally an irreducible projective variety
via the Segre embedding (see [9, I.Ex.2.14]), and X≥0× Y≥0⊂ X× Y acquires a natural
orientation. We have that ( Z, Z≥0) := ( X× Y, X≥0× Y≥0) is again a positive geometry
(resp. pseudo-positive geometry). The boundary components of ( Z, Z≥0) are of the form
(C× Y, C≥0× Y≥0) or ( X× D, X≥0× D≥0), where ( C, C≥0) and ( D, D≥0) are boundary
components of ( X, X≥0) and ( Y, Y≥0) respectively. The canonical form is Ω( Z, Z≥0) =
Ω(X, X≥0)∧ Ω(Y, Y≥0).
2.4 One-dimensional positive geometries
If ( X, X≥0) is a zero-dimensional positive geometry, then both X and X≥0 are points,
and we have Ω( X, X≥0) =±1. If ( X, X≥0) is a pesudo-positive geometry instead, then in
addition we are allowed to have X≥0 =∅ and Ω(X, X≥0) = 0.
Suppose that (X, X≥0) is a one-dimensional pseudo-positive geometry. A genus g pro-
jective smooth curve has g independent holomorphic diﬀerentials. Since we have assumed
that X is projective and normal but with no nonzero holomorphic forms (see Appendix A),
X must have genus 0 and is thus isomorphic to the projective line P1. Thus X≥0 is a
closed subset of P1(R)∼= S1. If X≥0 = P1(R) or X =∅ then Ω( X≥0) = 0 and X≥0 is a
pseudo-positive geometry but not a positive geometry. Otherwise, X≥0 is a union of closed
intervals, and any union of closed intervals is a positive geometry. A generic closed interval
is given by the following:
Example 2.1. We deﬁne the closed interval (or line segment) [a, b]⊂ P1(R) to be the set of
points{(1, x)| x∈ [a, b]}⊂ P1(R), where a < b . Then the canonical form is given by
Ω([a, b]) = dx
x− a− dx
x− b = (b− a)
(b− x)(x− a) dx. (2.1)
– 7 –

<!-- page 11 -->

where x is the coordinate on the chart (1 , x)∈ P1, and the segment is oriented along the
increasing direction of x. The canonical form of a disjoint union of line segments is the
sum of the canonical forms of those line segments.
3 Triangulations of positive geometries
3.1 Triangulations of pseudo-positive geometries
Let X be an irreducible projective variety, and X≥0⊂ X be a closed semialgebraic subset
of the type considered in Appendix A.1. Let ( X, Xi,≥0) for i = 1, . . . , tbe a ﬁnite collection
of pseudo-positive geometries all of which live in X. For brevity, we will write Xi,≥0 for
(X, Xi,≥0) in this section. We say that the collection {Xi,≥0} triangulates X≥0 if the
following properties hold:
• Each Xi,>0 is contained in X>0 and the orientations agree.
• The interiors Xi,>0 of Xi,≥0 are mutually disjoint.
• The union of all Xi,≥0 gives X≥0.
Naively, a triangulation of X≥0 is a collection of pseudo-positive geometries that tiles X≥0.
The purpose of this section is to establish the following crucial property of the canonical
form:
If{Xi,≥0} triangulates X≥0 then X≥0 is a pseudo-positive geometry and
Ω(X≥0) = ∑t
i=1 Ω(Xi,≥0). (3.1)
Note that even if all the {Xi,≥0} are positive geometries, it may be the case that X≥0 is
not a positive geometry. A simple example is a unit disk triangulated by two half disks
(see the discussion below Example 5.2).
If all the positive geometries involved are polytopes, our notion of triangulation reduces
to the usual notion of polytopal subdivision. If furthermore {Xi,≥0} are all simplices, then
we recover the usual notion of a triangulation of a polytope.
Note that the word “triangulation” does not imply that the geometries Xi,≥0 are
“triangular” or “simplicial” in any sense.
3.2 Signed triangulations
We now deﬁne three signed variations of the notion of triangulation. We loosely call any
of these notions “signed triangulations”.
We say that a collection{Xi,≥0} interior triangulates the empty set if for every point
x∈ ⋃
i Xi,≥0 that does not lie in any of the boundary components C of the Xi,≥0 we have
#{i| x∈ Xi,>0 and Xi,>0 is positively oriented at x}
=#{i| x∈ Xi,>0 and Xi,>0 is negatively oriented at x} (3.2)
where we arbitrarily make a choice of orientation of X(R) near x. Since all the Xi,>0 are
open subsets of X(R), it suﬃces to check the (3.2) for a dense subset of ⋃
i Xi,≥0− ⋃C,
– 8 –

<!-- page 12 -->

where ⋃C denotes the (ﬁnite) union of the boundary components. If {X1,≥0, . . . , Xt,≥0}
interior triangulates the empty set, we may also say that {X2,≥0, . . . , Xt,≥0} interior tri-
angulate X−
1,≥0. Thus an interior triangulation {X1,≥0, . . . , Xt,≥0} of X≥0 is a (genuine)
triangulation exactly when a generic point x∈ X≥0 is contained in exactly one of the Xi,≥0.
We now deﬁne the notion of boundary triangulation, which is inductive on the dimen-
sion. Suppose X has dimension D. Then we say that {Xi,≥0} is a boundary triangulation
of the empty set if:
• For D = 0, we have ∑t
i=1 Ω(Xi,≥0) = 0.
• For D > 0, suppose C is an irreducible subvariety of X of dimension D−1. Let
(C, Ci,≥0) be the boundary component of ( X, Xi,≥0) along C, where we set Ci,≥0 =∅
if such a boundary component does not exist. We require that for every C the
collection{Ci,≥0} form a boundary triangulation of the empty set.
As before, if{X1,≥0, . . . , Xt,≥0} boundary triangulates the empty set, we may also say that
{X2,≥0, . . . , Xt,≥0} boundary triangulates X−
1,≥0.
We ﬁnally deﬁne the notion of canonical form triangulation: we say that {Xi,≥0} is a
canonical form triangulation of the empty set if ∑t
i=1 Ω(Xi,≥0) = 0. Again, we may also
say that{X2,≥0, . . . , Xt,≥0} canonical form triangulates X−
1,≥0.
We now make the following claim, whose proof is given in Appendix B:
interior triangulation =⇒ boundary triangulation ⇐⇒ canonical form triangulation
(3.3)
Note that the reverse of the ﬁrst implication in (3.3) does not hold: (P1, P1(R)) is a null
geometry that boundary triangulates the empty set, but it does not interior triangulate
the empty set.
We also make the observation that if{Xi,≥0} boundary triangulates the empty set, and
all the Xi,≥0 except X1,≥0 are known to be pseudo-positive geometries, then we may con-
clude that X1,≥0 is a pseudo-positive geometry with Ω( X1,≥0) =− ∑t
i=2 Ω(Xi,≥0). (Here,
it suﬃces to know that X1,≥0, and recursively all its boundaries, are closed semialgebraic
sets of the type discussed in Appendix A.1.)
We note that (3.1) follows from (3.3). If {Xi,≥0} triangulate X≥0, we also have that
{Xi,≥0} interior triangulate X≥0. Unless we explicitly refer to a signed triangulation, the
word triangulation refers to (3.1). Finally, to summarize (3.1) and (3.3) in words, we say
that:
The canonical form is triangulation independent. (3.4)
We will return to this remark at multiple points in this paper.
3.3 The Grothendieck group of pseudo-positive geometries in X
We deﬁne theGrothendieck group of pseudo-positive geometries inX, denotedP(X), which
is the free abelian group generated by all the pseudo-positive geometries in X, modded out
– 9 –

<!-- page 13 -->

Figure 2: A triangle X≥0 triangulated by three smaller triangles Xi,≥0 for i = 1, 2, 3. The
vertices along the vertical mid-line are denoted P, Q and R.
by elements of the form
t∑
i=1
Xi,≥0 (3.5)
whenever the collection{Xi,≥0} boundary triangulates (or equivalently by (3.3), canonical
form triangulates) the empty set. Note that in P(X), we have X≥0 =−X−
≥0. Also by
(3.3), X≥0 = ∑
i Xi,≥0 if Xi,≥0 forms an interior triangulation of X≥0.
We may thus extend Ω to an additive homomorphism from P(X) to the space of
meromorphic top forms on X via:
Ω
( t∑
i=1
Xi,≥0
)
:=
t∑
i=1
Ω(Xi,≥0) (3.6)
Note that this homomorphism is injective, precisely because boundary triangulations and
canonical form triangulations are equivalent.
3.4 Physical versus spurious poles
In this subsection, we use “signed triangulation” to refer to any of the three notions in
Section 3.2. Let {Xi,≥0} be a signed triangulation of X≥0. The boundary components of
Xi,≥0 that are also a subset of boundary components of X≥0 are called physical boundaries;
otherwise they are called spurious boundaries . Poles of Ω( X, Xi,≥0) at physical (resp.
spurious) boundaries are called physical (resp. spurious) poles . We sometimes refer to the
triangulation independence of the canonical form (3.1) as cancellation of spurious poles ,
since spurious poles do not appear in the sum ∑
i Ω(X, Xi).
We now give an example which illustrates a subtle point regarding cancellation of
spurious poles. It may be tempting to think that spurious poles cancel in pairs along
spurious boundaries, but this is false in general. Rather, the correct intuition is that:
– 10 –

<!-- page 14 -->

Spurious poles cancel among collections of boundary components that boundary
triangulate the empty set.
Consider a triangle X≥0 triangulated by three smaller pieces Xi,≥0 for i = 1 , 2, 3 as in
Figure 2, but instead of adding all three terms in (3.1), we only add the i = 1 , 2 terms.
Since the triangles 1 and 2 have adjacent boundaries along line P Q, it may be tempting to
think that Ω(X, X1,≥0)+Ω( X, X2,≥0) has no pole there. This is, however, false because the
boundary components of 1 and 2 along line P R forms a signed triangulation of the segment
QR, which has a non-zero canonical form, so in particular Ω( X, X1,≥0) + Ω(X, X2,≥0) has
a non-zero residue along that line. However, had all three terms been included, then the
residue would be zero, since the boundary components of the three pieces along P R form
a signed triangulation of the empty set.
4 Morphisms of positive geometries
The canonical forms of diﬀerent pseudo-positive geometries can be related by certain maps
between them. We begin by deﬁning the push-forward (often also called the trace map)
for diﬀerential forms, see [10, II(b)]. Consider a surjective meromorphic map φ : M→ N
between complex manifolds of the same dimension. Let ω be a meromorphic top form on
M, b a point in N, and V an open subset containing b. If the map φ is of degree deg φ, then
the pre-image φ−1(V ) is the union of disconnected open subsets Ui for i = 1 , . . . ,deg φ,
with ai∈ Ui and φ(ai) = b. We deﬁne the push-forward as a meromorphic top form on N
in the following way:
φ∗(ω)(b) :=
∑
i
ψ∗
i (ω(ai)) (4.1)
where ψi := φ|−1
Ui : V → Ui.
Let ( X, X≥0) and ( Y, Y≥0) be two pseudo-positive geometries of dimension D. A
morphism Φ : ( X, X≥0) → (Y, Y≥0) consists of a rational (that is, meromorphic) map
Φ : X→ Y with the property that the restriction Φ |X>0 : X>0→ Y>0 is an orientation-
preserving diﬀeomorphism. A morphism where ( X, X≥0) = ( PD, ∆D) is also called a
rational parametrization. If in addition, Φ : X→ Y is an isomorphism of varieties, then
we call Φ : ( X, X≥0) → (Y, Y≥0) an isomorphism of pseudo-positive geometries. Two
pseudo-positive geometries are isomorphic if an isomorphism exists between them.
Note that if Φ : (X, X≥0)→ (Y, Y≥0) and Ψ : (Y, Y≥0)→ (Z, Z≥0) are morphisms, then
so is Π = Ψ◦ Φ. Pushforwards are functorial, that is, we have the equality Π∗ = Ψ∗◦ Φ∗.
Therefore, pseudo-positive geometries with morphisms form a category.
Finally, we state an important heuristic:
Heuristic 4.1. Given a morphism Φ : (X, X≥0)→ (Y, Y≥0) of pseudo-positive geometries,
we have
Φ∗(Ω(X, X≥0)) = Ω(Y, Y≥0) (4.2)
where Φ∗ is deﬁned by (4.1).
– 11 –

<!-- page 15 -->

We say that:
The push-forward preserves the canonical form. (4.3)
We do not prove Heuristic 4.1 in complete generality, but we will prove it in a number
of non-trivial examples (see Section 7.3). For now we simply sketch an argument using
some notation from Appendix A.
The idea is to use induction on dimension and the fact that “push-forward commutes
with taking residue”, formulated precisely in Proposition H.1. Let ( C, C≥0) be a boundary
component of ( X, X≥0). In general, the rational map Φ may not be deﬁned as a rational
map on C, but let us assume that (perhaps after a blowup of Φ [9, I.4], replacing ( X, X≥0)
by another pseudo-positive geometry) this is the case, and in addition that Φ is well-
deﬁned on all of C≥0. In this case, by continuity C≥0 will be mapped to the boundary
∂Y≥0. Since C is irreducible, and C≥0 is Zariski-dense in C, we see that Φ either collapses
the dimension of C (and thus C will not contribute to the poles of Φ ∗(Ω(X, X≥0))), or it
maps C surjectively onto one of the boundary components D of Y . In the latter case, we
assume that C>0 is mapped diﬀeomorphically to D>0, so ( C, C≥0)→ (D, D≥0) is again a
morphism of pseudo-positive geometries. The key calculation is then
ResDΦ∗(Ω(X, X≥0)) = Φ∗(ResCΩ(X, X≥0)) = Φ∗(Ω(C, C≥0)) = Ω(D, D≥0)
where the ﬁrst equality is by Proposition H.1 and the third equality is by the inductive
assumption. Thus Φ ∗(Ω(X, X≥0)) satisﬁes the recursive deﬁnition and must be equal to
Ω(Y, Y≥0).
5 Generalized simplices
Let (X, X≥0) be a positive geometry. We say that (X, X≥0) is a generalized simplex or that
it is simplex-like if the canonical form Ω( X, X≥0) has no zeros on X. The residues of a
meromorphic top form with no zeros is again a meromorphic top form with no zeros, so all
the boundary components of ( X, X≥0) are again simplex-like. While simplex-like positive
geometries are simpler than general positive geometries, there is already a rich zoo of such
objects.
Let us ﬁrst note that if (X, X≥0) is simplex-like, then Ω(X, X≥0) is uniquely determined
up to a scalar simply by its poles (without any condition on the residues). Indeed, suppose
Ω1 and Ω2 are two rational top forms on X with the same simple poles, both of which have
no zeros. Then the ratio Ω 1/Ω2 is a holomorphic function on X, and since X is assumed to
be projective and irreducible, this ratio must be a constant. This makes the determination
of the canonical form of a generalized simplex signiﬁcantly simpler than in general.
5.1 The standard simplex
The prototypical example of a generalized simplex is the positive geometry (Pm, ∆m), where
∆m := Pm
≥0 is the set of points in Pm(R) representable by nonnegative coordinates, which
– 12 –

<!-- page 16 -->

can be thought of as a projective simplex (see Section 5.2) whose vertices are the standard
basis vectors. We will refer to ∆m as the standard simplex. The canonical form is given by
Ω(∆m) =
m∏
i=1
dαi
αi
=
m∏
i=1
d log αi (5.1)
for points (α0, α1, . . . , αm)∈ Pm with α0 = 1. Here we can identify the interior of ∆m with
Rm
>0. Note that the pole corresponding to the facet at α0→ 0 has “disappeared” due to the
“gauge choice” (i.e. choice of chart) α0 = 1, which can be cured by changing the gauge. As
we will see in many examples, boundary components do not necessarily appear manifestly
as poles in every chart, and diﬀerent choices of chart can make manifest diﬀerent sets of
boundary components.
A gauge-invariant way of writing the same form is the following (see Appendix C):
Ω(∆m) = 1
m!
⟨α dmα⟩
α0··· αm
(5.2)
There are ( m+1) codimension 1 boundary components (i.e. facets of the simplex) corre-
sponding to the limits αi→ 0 for i = 0, . . . , m.
We say that a positive geometry ( X, X≥0) of dimension m is ∆-like if there exists a
degree one morphism Φ : ( Pm, ∆m)→ (X, X≥0). The projective coordinates on ∆ m are
called ∆−like coordinates of X≥0.
We point out that ∆-like positive geometries are not necessarily simplex-like. Examples
include BCFW cells discussed in Section 7.2.3. For now, we will content ourselves by giving
an example of how a new zeros can develop under pushforwards.
Example 5.1. Consider the rational top-form on P2, given by ω = 1
(x + 1)(y + 1)dxdy
in the chart {(1, x, y)} ⊂P2. The form ω has three poles (along x = 1, y = 1, and
the line at inﬁnity), and no zeros. Consider the rational map Φ : P2 → P2 given by
(1, x, y)↦→ (1, x, y/x) =: (1 , u, v). The map Φ has degree one, and using dy = udv + vdu
we compute that Φ∗ω = u
(u + 1)(uv + 1)dudv. So a new zero along u = 0 has appeared.
5.2 Projective simplices
A projective m-simplex (Pm, ∆) is a positive geometry in Pm cut out by exactly m+1 linear
inequalities. We will use Y ∈ Pm to denote a point in projective space with homogeneous
components YI indexed by I = 0, 1, . . . , m. A linear inequality is of the form YI WI≥ 0
for some vector W ∈ Rm+1 with components WI, and the repeated index I is implicitly
summed as usual. We deﬁne Y· W := YI WI. The vector W is also called a dual vector.
The projective simplex is therefore of the form
∆ ={Y ∈ Pm(R)| Y· Wi≥ 0 for i = 1, . . . , m+1} (5.3)
where the inequality is evaluated for Y in Euclidean space before mapping to projective
space. Here the Wi’s are projective dual vectors corresponding to the facets of the simplex.
Every boundary of a projective simplex is again a projective simplex, so it is easy to see
– 13 –

<!-- page 17 -->

that projective simplices satisfy the axioms of a positive geometry. For notational purposes,
we may sometimes write YI = (1, x, y, . . .) or YI = (x0, x1, . . . , xm) or something similar.
We now give formulae for the canonical form Ω(∆) in terms of both the vertices and
the facets of ∆. Let Zi∈ Rm+1 denote the vertices for i = 1, . . . , m+1, which carry upper
indices like ZI
i . We will allow the indices i to be represented mod m+1. We have
Ω(∆) = sm⟨Z1Z2··· Zm+1⟩m⟨Y dmY⟩
m!⟨Y Z1··· Zm⟩⟨ Y Z2··· Zm+1⟩···⟨ Y Zm+1··· Zm−1⟩ . (5.4)
where the angle brackets ⟨···⟩ denote the determinant of column vectors ··· , which is
SL(m+1)-invariant, and sm = −1 for m = 1 , 5, 9, . . ., and sm = +1 otherwise. See
Appendix C for the notation ⟨Y dmY⟩. Recall also from Appendix C that the quantity
Ω(A) := Ω(A)/⟨Y dmY⟩ (5.5)
is called the canonical rational function.
Now suppose the facet Wi is adjacent to vertices Zi+1, . . . , Zi+m, then Wi· Zj = 0 for
j = i+1, . . . , i+m. It follows that
WiI = (−1)(i−1)(m−i)ϵII 1···ImZI1
i+1··· ZIm
i+m (5.6)
where the sign is chosen so that Y · Wi > 0 for Y ∈ Int(A). See Section 6.1.3 for the
reasoning behind the sign choice.
We can thus rewrite the canonical form in W space as follows:
Ω(∆) = ⟨W1W2··· Wm+1⟩⟨ Y dmY⟩
m!(Y· W1)(Y· W2)··· (Y· Wm+1) . (5.7)
A few comments on notation: We will often write i for Zi inside an angle bracket, so for
example⟨i0i1··· im⟩ :=⟨Zi0Zi1··· Zim⟩ and⟨Y i1··· im⟩ :=⟨Y Zi1··· Zim⟩. Furthermore,
the square bracket [1, 2, . . . , m+1] is deﬁned to be the coeﬃcient of⟨Y dmY⟩ in (5.4). Thus,
[1, 2, . . . , m+1] = Ω(∆) (5.8)
Note that the square bracket is antisymmetric in exchange of any pair of indices. These
conventions are used only in Z space.
The simplest simplices are one-dimensional line segments P1(R) discussed in Exam-
ple 2.1. We can think of a segment [ a, b]∈ P1(R) as a simplex with vertices
ZI
1 = (1, a), Z I
2 = (1, b) (5.9)
where a < b .
In Section 6.1, we provide an extensive discussion on convex projective polytopes as
positive geometries, which can be triangulated by projective simplices.
– 14 –

<!-- page 18 -->

5.3 Generalized simplices on the projective plane
Suppose ( P2,A) is a positive geometry embedded in the projective plane. We now argue
thatA can only have linear and quadratic boundary components. Let ( C, C≥0) be one of
the boundary components of A. Then C is an irreducible projective plane curve. By our
assumption (see Appendix A) that C is normal, we must have that C⊂ P2 is a smooth
plane curve of degree d. The genus of a smooth degree d plane curve is equal to
g = (d− 1)(d− 2)
2 . (5.10)
According to the argument in Section 2.4, for ( C, C≥0) to be a positive geometry (Axiom
(P1)), we must have C ∼= P1. Therefore g = 0, which gives d = 1 or d = 2. Thus all
boundaries of the positive geometry A are linear or quadratic. In Section 5.3.1, we will
relax the requirement of normality and give an example of a “degenerate” positive geometry
in P2. We leave detailed investigation of non-normal positive geometries for future work.
Example 5.2. Consider a region S(a)∈ P2(R) bounded by one linear function q(x, y) and
one quadratic function f(x, y), where q = y− a≥ 0 for some constant −1 < a < 1, and
f = 1− x2− y2≥ 0. This is a “segment” of the unit disk. A picture for a = 1/10 is given
in Figure 1c.
We claim thatS(a) is a positive geometry with the following canonical form
Ω(S(a)) = 2
√
1− a2dxdy
(1− x2− y2)(y− a) (5.11)
Note that for the special case of a = 0, we get the canonical form for the “northern
half disk”.
Ω(S(0)) = 2dxdy
(1− x2− y2)y (5.12)
We now check that the form for general a has the correct residues on both boundaries.
On the ﬂat boundary we have
Resy=aΩ(S(a)) = 2
√
1− a2dx
1− a2− x2 = 2
√
1− a2dx
(
√
1− a2− x)(x +
√
1− a2)
(5.13)
Recall from Section 2.4 that this is simply the canonical form on the line segment x∈
[−
√
1− a2,
√
1− a2], with positive orientation since the boundary component inherits the
counter-clockwise orientation from the interior.
The residue on the arc is more subtle. We ﬁrst rewrite our form as follows:
Ω(S(a)) =
(√
1− a2dy
x(y− a)
)
d f
f (5.14)
which is shown by applying d f=−2(xdx + ydy). The residue along the arc is therefore
Resf=0Ω(S(a)) =
√
1− a2dy
x(y− a) (5.15)
– 15 –

<!-- page 19 -->

Substituting x =
√
1− y2 for the right-half of the arc gives residue +1 at the boundary
y = a, and substituting x =−
√
1− y2 for the left-half of the arc gives residue −1.
We give an alternative calculation of these residues. Let us parametrize ( x, y) by a
parameter t as follows.
(x, y) =
((t + t−1)
2 , (t− t−1)
2i
)
(5.16)
which of course satisﬁes the arc constraint f(x, y) = 0 for all t.
Rewriting the form on the arc in terms of t gives us
Resf=0Ω(S(a)) = 2
√
1− a2dt
t2− 2iat− 1 = (t+− t−)dt
(t− t+)(t− t−) (5.17)
where t± = ia±
√
1− a2 are the two roots of the quadratic expression in the denominator
satisfying
t+ + t− = 2ia, t +t− =−1 (5.18)
The corresponding roots ( x±, y±) are
(x±, y±) = (±
√
1− a2, a) (5.19)
which of course correspond to the boundary points of the arc.
The residues at t± and hence ( x±, y±) are±1, as expected.
By substituting a =−1 in Example 5.2 we ﬁnd that the unit disk D2 :=S(−1) has
vanishing canonical form, or equivalently, is a null geometry. Alternatively, one can derive
this by triangulating (see Section 3) the unit disk into the northern half disk and the
southern half disk, whose canonical forms must add up to Ω( D2). A quick computation
shows that the canonical forms of the two half disks are negatives of each other, so they sum
to zero. A third argument goes as follows: the only pole of Ω( D2), if any, appears along
the unit circle, which has a vanishing canonical form since it has no boundary components.
So in fact Ω(D2) has no poles, and must therefore vanish by the non-existence of nonzero
holomorphic top forms on the projective plane. More generally, a pseudo-positive geometry
is a null geometry if and only if all its boundary components are null geometries.
However, not all conic sections are null geometries. Hyperbolas are notable excep-
tions. From our point of view, the distinction between hyperbolas and circles as positive
geometries is that the former intersects a line at inﬁnity. So a hyperbola has two boundary
components, while a circle only has one. We show this as a special case of the next example.
Example 5.3. Let us consider a generic region in P2(R) bounded by one quadratic and
one linear polynomial. Let us denote the linear polynomial by q = Y · W ≥ 0 with
YI = (1, x, y)∈ P2(R) and the quadratic polynomial by f = Y Y· Q := YI YJ QIJ for some
real symmetric bilinear form QIJ . We denote our region as U(Q, W).
The canonical form is given by
Ω(U(Q, W)) =
√QQW W⟨Y dY dY⟩
(Y Y· Q)(Y· W ) (5.20)
– 16 –

<!-- page 20 -->

where QQW W :=− 1
2 ϵIJK ϵI′J′K′
QII′QJJ′WKWK′ and ϵIJK is the Levi-Civita symbol with
ϵ012 = 1, and ⟨···⟩ denotes the determinant. The appearance of √QQW W ensures that
the result is invariant under rescaling QIJ and WI independently, which is necessary. It
also ensures the correct overall normalization as we will show in examples.
It will prove useful to look at this example by putting the line W at inﬁnity WI =
(1, 0, 0) and setting YI = (1 , x, y), with Y Y · Q = y2− (x− a)(x− b) for a̸= b, which
describes a hyperbola. The canonical form becomes
Ω(U(Q, W)) = 2dxdy
y2− (x− a)(x− b) (5.21)
Note that taking the residue on the quadric gives us the 1-form on y2− (x− a)(x− b) = 0:
ResQΩ(U(Q, W)) = dx/y = 2dy/((x− a) + (x− b)) (5.22)
Suppose a̸= b, then this form is smooth as y→ 0 where x→ a or x→ b, which is evident
in the second expression above. The only singularities of this 1-form are on the line W ,
which can be seen by reparametrizing the projective space as ( z, w, 1)∼ (1, x, y) so that
z = 1/y, w = x/y, which gives the 1-form on 1 − (w− az)(w− bz) = 0:
ResQΩ(U(Q, W)) = dw− dz
z = [(w− az)(−1 + bz) + (w− bz)(−1 + az)]dz
z((w− az) + (w− bz)) (5.23)
Evidently, there are only two poles ( z, w) = (0 ,±1), which of course are the intersection
points of the quadric Q with the line W . The other “pole” in (5.23) is not a real singularity
since the residue vanishes.
Note however that as the two roots collide a→ b, the quadric degenerates to the
product of two lines (y + x− a)(y− x + a) and we get a third singularity at the intersection
of the two lines ( x, y) = (a, 0).
Note also another degenerate limit here, where the line W is taken to be tangent to
the quadric Q. We can take the form in this case to be ( dxdy)/(y2− x). Taking the residue
on the parabola gives us the 1-form dy, that has a double-pole at inﬁnity, which violates
our assumptions. This corresponds to the two intersection points of the line W with Q
colliding to make W tangent to Q. In fact, we can get rid of the line W all together and
ﬁnd that the parabolic boundary is completely smooth and hence only a null geometry.
Moreover, we can consider the form ( dxdy)/(x2 + y2− 1), i.e. associated with the
interior of a circle. But for the same reason as for the parabola, the circle is actually a null
geometry. Despite this, it is of course possible by analytic continuation of the coeﬃcients
of a general quadric to go from a circle to a hyperbola which is a positive geometry.
Now let us return to the simpler example of the segment U(Q, W) :=S(a), where
QIJ =


1 0 0
0−1 0
0 0 −1

 , W I = (−a, 0, 1) (5.24)
Substituting these into the canonical form we ﬁnd
QQW W = (1− a2) > 0, Y Y · Q = 1− x2− y2, Y · W = a− y, (5.25)
– 17 –

<!-- page 21 -->

-1.0 -0.5 0.0 0.5 1.0
-1.0
-0.5
0.0
0.5
1.0
x
y
(a) Curve: y2 − x(x − 1/2)(x + 1) = 0
/Minus1.0 /Minus0.5 0.0 0.5 1.0
/Minus1.0
/Minus0.5
0.0
0.5
1.0
x
y (b) Boundary: y2 − x2(x + 1) = 0
Figure 3: (a) A non-degenerate vs. (b) a degenerate elliptic curve. The former does not
provide a valid embedding space for a positive geometry, while the shaded “tear-drop” is
a valid (non-normal) positive geometry.
and therefore
Ω(U(Q, W)) = Ω(S(a)) (5.26)
as expected.
5.3.1 An example of a non-normal geometry
We would now like to give an example of a non-normal positive geometry. Consider the
geometryU(C)⊂ P2(R) deﬁned by a cubic polynomial Y Y Y · C≥ 0, where Y Y Y · C :=
CIJK YI YJ YK for some real symmetric tensor CIJK . The canonical form must have the
following form:
Ω(U(C)) = C0⟨Y dY dY⟩
Y Y Y· C (5.27)
where C0 is a constant needed to ensure that all leading residues are ±1. Of course, C0
must scale linearly as CIJK and must be dependent on the Aronhold invariants for cubic
forms. For our purposes we will work out C0 only in speciﬁc examples.
Let us consider a completely generic cubic, which by an appropriate change of variables
can always be written as Y Y Y· C = y2− (x− a)(x− b)(x− c) for constants a, b, c. If the
three constants are distinct, then there is no positive geometry associated with this case
because the 1-form obtained by taking a residue on the cubic is dx/y which is the standard
holomorphic one-form associated with a non-degenerate elliptic curve. We can also observe
directly that there are no singularities as x→ a, b, c, and that as we go to inﬁnity, we can
set y→ 1/t3, x→ 1/t2 with t→ 0, and dx/y→− 2dt is smooth. The existence of such a
form makes the canonical form non-unique, and hence ill-deﬁned. By extension, no positive
geometry can have the non-denegerate cubic as a boundary component either.
– 18 –

<!-- page 22 -->

However, if the cubic degenerates by having two of the roots of the cubic polynomial
in x collide, then we do get a beautiful (non-normal) positive geometry, one which has only
one zero-dimensional boundary. Without loss of generality let us put the double-root at
the origin and consider the cubic y2− x2(x + a2). Taking the residue on the cubic, we can
parametrize y2− x2(x + a2) = 0 as y = t(t2− a2), x = (t2− a2), then dx/y = dt/(t2− a2)
has logarithmic singularities at t =±a. Note that these two points correspond to the same
point y = x = 0 on the cubic! But the boundary is oriented, so we encounter the same
logarithmic singularity point from one side and then the other as we go around. We can
cover the whole interior of the “teardrop” shape for this singular cubic by taking
x = u(t2− a2), y = ut(t2− a2) (5.28)
which, for u∈ (0, 1) and t∈ (−a, a) maps 1-1 to the teardrop interior, dutifully reﬂected
in the form dxdy
y2− x2(x + a2) = dt
(a− t)(t + a)
du
u(1− u) (5.29)
Note that if we further take a→ 0, we lose the positive geometry as we get a form with a
double-pole, much as our example with the parabola in Example 5.3.
5.4 Generalized simplices in higher-dimensional projective spaces
Let us now consider generalized simplices (Pm,A) for higher-dimensional projective spaces.
Let (C, C≥0) be a boundary component of A, which is an irreducible normal hypersurface
in Pm. For (C, C≥0) to be a positive geometry, C must have no nonzero holomorphic forms.
Equivalently, the geometric genus of C must be 0. This is the case if and only if C has
degree less than or equal to m. Thus in P3, the boundaries of a positive geometry are
linear, quadratic, or cubic hypersurfaces.
It is easy to generalize Example 5.2 to simplex-like positive geometries in Pm(R): take
a positive geometry bounded by ( m− 1) hyperplanes Wi and a quadric Q, which has
canonical form
Ω(A) = C0⟨Y dmY⟩
(Y· W1)··· (Y· Wm−1)(Y Y· Q) . (5.30)
for some constant C0. Note that the ( m− 1) planes intersect generically on a line, that
in turn intersects the quadric at two points, so as in our two-dimensional example this
positive geometry has two zero-dimensional boundaries.
Let us consider another generalized simplex, this time in P3(R). We take a three-
dimensional region A ⊂P3(R) bounded by a cubic surface and a plane. If we take a
generic cubic surface C and generic plane W , then their intersection would be a generic
cubic curve in W , which as discussed in Section 5.3 cannot contain a (normal) positive
geometry.
On the other hand, we can make a special choice of cubic surface A that gives a
positive geometry. A pretty example is provided by the “Cayley cubic” (see Figure 4). If
YI = (x0, x1, x2, x3) are coordinates on P3, let the cubic C be deﬁned by
C· Y Y Y := x0x1x2 + x1x2x3 + x2x3x0 + x3x0x1 = 0 (5.31)
– 19 –

<!-- page 23 -->

Figure 4: The Cayley cubic curve. The plane separating the translucent and solid parts
of the surface is given by x0 = 0.
This cubic has four singular points at X0 = (1, 0, 0, 0), . . . , X3 = (0, 0, 0, 1). Note that
C gives a singular surface, but it still satisﬁes the normality criterion of a positive geometry.
Let us choose three of the singular points, say X1, X2, X3, and let W be the hyperplane
passing through these three points; we consider the form
Ω(A) = C0
⟨Y d3Y⟩
(Y Y Y· C)⟨Y X1X2X3⟩ (5.32)
where C0 is a constant. A natural choice of variables turns this into a “dlog” form. Consider
xi = syi, for i = 1, 2, 3; x0 =− y1y2y3
y1y2 + y2y3 + y3y1
(5.33)
Then if we group the three y’s as coordinates of P2 ={y = (y1, y2, y3)}, we have
Ω(A) = ⟨yd2y⟩
2y1y2y3
ds
(s− 1) (5.34)
This is the canonical form of the positive geometry given by the bounded component of
the region cut out by Y Y Y· C≥ 0 and⟨X1X2X3Y⟩≥ 0.
We can generalize this construction to Pm(R), with Y = (x0,··· , xm) and a degree m
hypersurface
Qm· Ym =
m∑
i=0
x0··· ˆxi··· xm,
where Qm· Ym := QmI1...ImYI1··· YIm and the singular points are X0 = (1, 0,··· , 0), . . . ,
Xm = (0,··· , 0, 1). Then if we choose m of these points and a linear factor corresponding
to the hyperplane going through them,
Ω(A) = C0
⟨Y dmY⟩
(Ym· Qm)⟨Y X1··· Xm⟩ (5.35)
is the canonical form associated with the bounded component of the positive geometry cut
out by Ym· Qm≥ 0,⟨X1··· XmY⟩≥ 0, for some constant C0.
– 20 –

<!-- page 24 -->

5.5 Grassmannians
In this section we brieﬂy review the positroid stratiﬁcation of the positive Grassmannian,
and argue that each cell of the stratiﬁcation is a simplex-like positive geometry.
5.5.1 Grassmannians and positroid varieties
Let G(k, n) denote the Grassmannian of k-dimensional linear subspaces of Cn. We recall
the positroid stratiﬁcation of the Grassmannian. Each point in G(k, n) is represented by
a k× n complex matrix C = (C1, C2, . . . , Cn) of full rank, where Ci∈ Ck denote column
vectors. Given C∈ G(k, n) we deﬁne a function f : Z→ Z by the condition that
Ci∈ span(Ci+1, Ci+2, . . . , Cf(i)) (5.36)
and f(i) is the minimal index satisfying this property. In particular, if Ci = 0, then
f(i) = i. Here, the indices are taken mod n. The function f is called an aﬃne permutation,
or “decorated permutation”, or sometimes just “permutation” [3, 5, 11]. Classifying points
of G(k, n) according to the aﬃne permutation f gives the positroid stratiﬁcation
G(k, n) =
⨆
f
˚Πf . (5.37)
where, for every aﬃne permutation f, the set ˚Πf consists of those C matrices satisfy-
ing (5.36) for every integer i. We let the positroid variety Πf ⊂ G(k, n) be the closure
of ˚Πf. Then Π f is an irreducible, normal, complex projective variety [11]. If k = 1 then
G(k, n)∼= Pn−1 and the stratiﬁcation (5.37) decomposes Pn−1 into coordinate hyperspaces.
5.5.2 Positive Grassmannians and positroid cells
Let G(k, n)(R) denote the real Grassmannian. Each point in G(k, n) is represented by
a k× n complex matrix of full rank. The (totally) nonnegative Grassmannian G≥0(k, n)
(resp. (totally) positive Grassmannian G>0(k, n)) consists of those points C∈ G(k, n)(R)
all of whose k× k minors, called Pl¨ ucker coordinates, are nonnegative (resp. positive) [5].
The intersections
Πf,>0 := G≥0∩ ˚Πf , Πf,≥0 := G≥0∩ Πf (5.38)
are loosely called (open and closed) positroid cells.
For any permutation f, we have
(Πf , Πf,≥0) is a positive geometry. (5.39)
The boundary components of (Π f , Πf,≥0) are certain other positroid cells (Π g, Πg,≥0) of
one lower dimension. The canonical form Ω( f) := Ω(Πf , Πf,≥0) was studied in [3, 11]. We
remark that Ω( f) has no zeros, so (Π f , Πf,≥0) is simplex-like.
The canonical form Ω( G≥0(k, n)) := Ω( G(k, n), G≥0(k, n)) of the positive Grassman-
nian was worked out and discussed in [3]:
Ω(G≥0(k, n)) :=
∏k
s=1
⟨
Cdn−kCs
⟩
((n−k)!)k ∏n
i=1(i, i+1, . . . , i+k−1) (5.40)
– 21 –

<!-- page 25 -->

where C := (C1, . . . , Ck)T is a k× n matrix representing a point in G(k, n), and the paren-
theses (i1, i2, . . . , ik) denotes the k× k minor of C corresponding to columns i1, i2, . . . , ik
in that order. We also divide by the “gauge group” GL( k) since the matrix representa-
tion of the Grassmannian is redundant. The canonical forms Ω( f) on Πf are obtained by
iteratively taking residues of Ω( G≥0(k, n)).
The Grassmannian G(k, n) has the structure of a cluster variety [12], as discussed in
Section 5.7. The cluster coordinates of G(k, n) can be constructed using plabic graphs or
on-shell diagrams. Given a sequence of cluster coordinates (c0, c1, . . . , ck(n−k))∈ Pk(n−k)
for the Grassmannian G(k, n), the positive Grassmannian is precisely the subset of points
representable by positive coordinates. It follows that G≥(k, n) is ∆-like with the degree-one
cluster coordinate morphism Φ : ( Pk(n−k), ∆k(n−k))→ (G(k, n), G≥0(k, n)). Note of course
that a diﬀerent degree-one morphism exists for each choice of cluster.
According to Heuristic 4.1, we expect that the canonical form on the positive Grass-
mannian is simply the push-forward of Ω(∆ k(n−k)). That is,
Ω(G≥0(k, n)) =±Φ∗
( ⟨
c dk(n−k)c
⟩
(k(n−k))! ∏k(n−k)
I=0 cI
)
(5.41)
where the overall sign depends on the ordering of the cluster coordinates. Equation (5.41)
is worked out in [7]. It follows in particular that the right hand side of (5.41) is independent
of the choice of cluster.
5.6 Toric varieties and their positive parts
In this section we show that positive parts of projectively normal toric varieties are examples
of positive geometries.
5.6.1 Projective toric varieties
Let z = (z1, z2, . . . , zn)∈ (Zm+1)n be a collection of integer vectors in Zm+1. We assume
that the set is graded, so:
There exists a∈ Qm+1 so that a· zi = 1 for all i. (5.42)
We deﬁne a (possibly not normal) projective toric variety X(z)⊂ Pn−1 as
X(z) ={(Xz1, Xz2, . . . , Xzn)| X∈ (C∗)m+1}⊂ Pn−1. (5.43)
where
Xzi := Xz0i
0 Xz1i
1 ··· Xzm,i
m (5.44)
Equivalently, X(z) is the closure of the image of the monomial map θz
θz : X = (X0, . . . , Xm)↦−→(Xz1, . . . , Xzn)∈ Pn−1. (5.45)
We shall assume that z spans Zm+1 so that dim X(z) = m. The intersection of
X(z) with {(C1, C2, . . . , Cn)| Ci∈ C∗}⊂ Pn−1 is a dense complex torus T ∼= (C∗)m in
– 22 –

<!-- page 26 -->

X(z). Deﬁne the nonnegative part X(z)≥0 of X(z) to be the intersection of X(z) with
∆n−1 ={(C1, C2, . . . , Cn)| Ci∈ R≥0}⊂ Pn−1(R). Similarly deﬁne X(z)>0. Equivalently,
X(z)>0 is simply the image of Rm+1
>0 under the monomial map ( C∗)m+1→ Pn−1. It is
known that X(z)≥0 is diﬀeomorphic to the polytope A(z) := Conv( z), see [13, 14]. We
establish a variant of this result in Appendix E. Note that we do not need to assume that
the zi are vertices ofA(z); some of the points zi may lie in the interior.
Our main claim is that
(X(z), X(z)≥0) is a positive geometry (5.46)
whenever X(z) is projectively normal (which implies normality). It holds if and only if we
have the following equality of lattice points in Zm+1
Cone(z)∩ spanZ(z) = spanZ≥0(z). (5.47)
If the equality (5.47) does not hold, we can enlarge z by including additional lattice points
in Cone(z)∩ spanZ(z) until it does.
The torus T acts on X(z) and the torus orbits are in bijection with the faces F of
the polytopeA(z). For each such face F , we denote by XF the corresponding torus orbit
closure; then XF is again a projective toric variety, given by using the points zi that belong
to the face F . If X(z) is projectively normal, then all the XF are as well.
5.6.2 The canonical form of a toric variety
The variety X(z) has a distinguished rational top form Ω X(z) of top degree. The rational
form ΩX(z) is uniquely deﬁned by specifying its restriction to the torus
ΩX(z)|T := ΩT :=
m∏
i=1
dxi
xi
,
where xi are the natural coordinates on T , and ΩT is the natural holomorphic non-vanishing
top form on T . In Appendix G, we show that when X(z) is projectively normal, the
canonical form Ω X(z) has a simple pole along each facet toric variety XF and no other
poles, and furthermore, for each facet F the residue ResXF ΩX(z) is equal to the canonical
form ΩXF of the facet.
This property of ΩX(z) establishes (5.46), apart from the uniqueness part of Axiom (P2)
which is equivalent to the statement that X(z) has no nonzero holomorphic forms. This is
well known: when X(z) is a smooth toric variety, this follows from the fact that smooth
projective rational varieties V have no nonzero holomorphic forms, or equivalently, have
geometric genus dimH0(V, ωV ) equal to 0. Normal toric varieties have rational singularities
so inherit this property from a smooth toric resolution. We have thus established (5.46),
and the canonical form Ω( X(z), X(z)≥0) is ΩX(z).
We remark that ΩX(z) has no zeros, and thus (X(z), X(z)≥0) is a simplex-like positive
geometry.
– 23 –

<!-- page 27 -->

Example 5.4. Take n = 4 and m = 2, with
z1 = (1, 0, 0), z 2 = (1, 1, 0), z 3 = (1, 1, 1), z 4 = (1, 0, 1).
The polytope A(z) is a square. The toric variety X(z) is the closure in P3 of the set of
points{(x, xy, xyz, xz)| x, y, z∈ C∗}, or equivalently of {(1, y, yz, z)| y, z∈ C∗}. This
closure is the quadric surface C1C3− C2C4 = 0. In fact, X(z) is isomorphic to the P1× P1,
embedded inside P3 via the Segre embedding.
The nonnegative part X(z)≥0 is the closure of the set of points {(1, y, yz, z)| y, z∈
R>0}, and is diﬀeomorphic to a square. There are four boundaries, given by Ci = 0 for
i = 1, 2, 3, 4, corresponding to y→ 0,∞ and z→ 0,∞. For example, when z→ 0 we have
the boundary component D ={(1, y, 0, 0)| y∈ C∗}⊂ P3, which is isomorphic to P1. In
these coordinates, the canonical form is given by
Ω(X(z), X(z)≥0) = ΩX(z) = dy
y
dz
z .
The residue Res z=0ΩX(z) is equal to dy/y, which is the canonical form of the boundary
component D∼= P1 above.
The condition (5.42) that z is graded implies that θz : (C∗)m+1→ T⊂ X(z) factors
as
(C∗)m+1−→(C∗)m+1/C∗ ˜θz
−→ T, (5.48)
where the quotient S = (C∗)m+1/C∗ arises from the action of t∈ C∗ given by
t· (X1, . . . , Xm+1) = (t˜a1X1, . . . , t˜am+1Xm+1) (5.49)
where ˜a∈ Zm+1 is a scalar multiple of a∈ Qm+1 that is integral. For example, if zi = (1, z′
i)
for z′
i∈ Zm as in Section 7.3.3, then a = (1 , 0, . . . ,0) and S can be identiﬁed with the
subtorus{(1, X1, X2, . . . , Xm)}⊂ (C∗)m+1. The map ˜θz : S→ T is surjective, but may
not be injective. By Example 7.8, we have
˜θz
∗(ΩS) = ΩT . (5.50)
5.7 Cluster varieties and their positive parts
We speculate that reasonable cluster algebras give examples of positive geometries. Let A
be a cluster algebra over C (of geometric type) and let ˚X = Spec(A) be the corresponding
aﬃne cluster variety [15]; thus the ring of regular functions on ˚X is equal to A. We will
assume that ˚X is a smooth complex manifold, see e.g. [16, 17] for some discussion of this.
The generators of A as a ring are grouped into clusters (x1, x2, . . . , xn), where n =
dim ˚X. Each cluster corresponds to a subtorus T∼= (C∗)n with an embedding ιT : T ↪→ ˚X.
Diﬀerent clusters are related by mutation:
xix′
i = M + M′, (5.51)
– 24 –

<!-- page 28 -->

swapping the coordinate xi for x′
i, where M, M′ are monomials in the xj, j ̸= i. It is
clear from (5.51) that if ( x1, . . . , xi, . . . , xn) are all positive real numbers, then so are
(x1, . . . , x′
i, . . . , xn). We thus deﬁne the positive part of ˚X to be ˚X>0 := ιT (Rn
>0).
Furthermore, we deﬁne the canonical form Ω ˚X := ∏n
i=1 dxi/xi. By (5.51), we have
xidx′
i + x′
idxi = dM + dM′ (5.52)
so wedging both sides with ∏
j̸=i dxj/xj, we deduce that the canonical form Ω ˚X does not
depend on the choice of cluster. In fact, under some mild assumptions, Ω ˚X extends to a
holomorphic top-form on ˚X.
We speculate that there is a compactiﬁcation X of ˚X such that
(X, X≥0 := ˚X>0) is a positive geometry with canonical form Ω( X, X≥0) = Ω ˚X . (5.53)
Furthermore, we expect that all boundary components are again compactiﬁcations
of cluster varieties. We also expect that the compactiﬁcation can be chosen so that the
canonical form has no zeros.
5.8 Flag varieties and total positivity
Let G be a reductive complex algebraic group, and let P⊂ G be a parabolic subgroup. The
quotient G/P is known as a generalized ﬂag variety. If G = GL(n), and P = B⊂ GL(n)
is the subgroup of upper triangular matrices, then G/B is the usual ﬂag manifold. If
G = GL(n) and
P =
{(
A B
0 C
)}
⊂ GL(n) (5.54)
with block form where A, B, C are respectively k× k, k× (n− k), and ( n− k)× (n− k),
then G/P∼= G(k, n) is the Grassmannian of k-planes in n-space.
In [6], the totally nonnegative part (G/P )≥0⊂ G/P (R) of G/P was deﬁned, assuming
that G(R) is split over the real numbers. We sketch the deﬁnition in the case that G =
GL(n). An element g∈ GL(n) is called totally positive if all of its minors (of any size) are
positive. Denoting the totally positive part of GL( n) by GL(n)>0, we then deﬁne
(GL(n)/P )≥0 := GL(n)>0· e,
where GL( n)>0· e denotes the orbit of GL( n)>0 acting on a basepoint e∈ G/P , which
is the point in G/P represented by the identity matrix. In the case that GL( n)/P is the
Grassmannian G(k, n), we have (G/P )≥0 = G(k, n)≥0, though this is not entirely obvious!
In [18] it was shown that there is a stratiﬁcation G/P = ⋃˚Πw
u such that each of the
intersections ˚Πw
u∩ (G/P )≥0 is homeomorphic to Rd
>0 for some d. The closures Π w
u = ˚Πwu
are known as projected Richardson varieties, and in the special case G/P∼= G(k, n), they
reduce to the positroid varieties of Section 5.5.1 [11, 19].
The statement
(G/P, (G/P )≥0) is a positive geometry (5.55)
– 25 –

<!-- page 29 -->

was essentially established in [19], but in somewhat diﬀerent language. Namely, it was
proved in [19] that for each stratum Π w
u (with G/P itself being one such stratum), there
is a meromorphic form Ω w
u with simple poles along the boundary strata {Πw′
u′} such that
ResΠw′
u′
Ωw
u = α· Ωw′
u′ for some scalar α. By identifying Ω w
u with the push-forward of the
dlog-form under the identiﬁcation Rd
>0∼= ˚Πw
u∩ (G/P )≥0, we expect all the scalars α can
be computed to be equal to 1. Note that this also shows that (Π w
u , Πw
u∩ (G/P )≥0) is itself
a positive geometry.
We remark that it is strongly expected that ˚Πw
u (and in particular the open stratum
inside G/P ) is a cluster variety [20]. Thus (5.55) is a special case of (5.53). For example,
the cluster structure of G(k, n) is established in [12].
6 Generalized polytopes
In this section we investigate the much richer class of generalized polytopes, or polytope-like
geometries, which are positive geometries whose canonical form may have zeros.
6.1 Projective polytopes
The fundamental example is a convex polytope embedded in projective space. Most of
our notation was already established back in Section 5.2. In Appendix D, we recall basic
terminology for polytopes and explain the relation between projective polytopes and cones
in a real vector space.
6.1.1 Projective and Euclidean polytopes
Let Z1, Z2, . . . , Zn∈ Rm+1, and denote by Z the n× (m + 1) matrix whose rows are given
by the Zi. Deﬁne A :=A(Z) :=A(Z1, Z2, . . . , Zn)⊂ Pm(R) to be the convex hull
A = Conv(Z) = Conv(Z1, . . . , Zn) :=
{ n∑
i=1
CiZi∈ Pm(R)| Ci≥ 0, i = 1, . . . , n
}
. (6.1)
We make the assumption that Z1, . . . , Zn are all vertices of A. In (6.1), the vector∑n
i=1 CiZi ∈ Rm+1 is thought of as a point in the projective space Pm(R). The poly-
topeA is well-deﬁned if and only if ∑n
i=1 CiZi is never equal to 0 unless Ci = 0 for all
i. A basic result, known as “Gordan’s theorem” [21], states that this is equivalent to the
condition:
There exists a (dual) vector X∈ Rm+1 such that Zi· X > 0 for i = 1, 2, . . . , n. (6.2)
The polytopeA is called a convex projective polytope.
Every projective polytope ( Pm,A) is a positive geometry. This follows from the fact
that every polytope A can be triangulated (see Section 3) by projective simplices. By
Section 5.2, we know that every simplex is a positive geometry, so by the arguments in
Section 3 we conclude that ( Pm,A) is a positive geometry. The canonical form Ω( A) of
a projective polytope will be discussed in further detail from multiple points of view in
Section 7.
– 26 –

<!-- page 30 -->

It is clear that the polytopeA is unchanged if each Zi is replaced by a positive multiple
of itself. This gives an action of the little group Rn
>0 on Z that ﬁxes A. To visualize a
polytope, it is often convenient to work with Euclidean polytopes instead of projective
polytopes. To do so, we use the little group to “gauge ﬁx” the ﬁrst component of Z to be
equal to 1 (if possible), so that Z = (1 , Z′) where Z′∈ Rm. The polytope A⊂ Pm can
then be identiﬁed with the set
{ n∑
i=1
CiZ′
i⊂ Rm| Ci≥ 0, i = 1, . . . , n and C1 + C2 +··· + Cn = 1
}
(6.3)
inside Euclidean space Rm. The Ci variables in this instance can be thought of as center-
of-mass weights. Points in projective space for which the ﬁrst component is zero lie on the
(m−1)-plane at inﬁnity.
The points Z1, . . . , Zn can be collected into a n× (m + 1) matrix Z, which can be
thought of as a linear map Z : Rn → Rm+1 or a rational map Z : Pn−1 → Pm. The
polytope A is then the image Z(∆n−1) of the standard ( n− 1)-dimensional simplex in
Pn−1(R).
6.1.2 Cyclic polytopes
We call the point conﬁguration Z1, Z2, . . . , Zn positive if n≥ m + 1, and all the ( m + 1)×
(m + 1) ordered minors of the matrix Z are strictly positive. Positive Z always satisfy
condition (6.2). In this case, the polytope A is known as a cyclic polytope. For notational
convenience, we identify Zi+n := Zi, so the vertex index is represented mod n.
For even m, the facets of the cyclic polytope are
Conv(Zi1−1, Zi1, . . . , Zim/2−1, Zim/2) (6.4)
for 1≤ i1−1 < i1 < i2−1 < i2 <··· < im/2−1 < im/2≤ n+1.
For odd m, the facets are
Conv(Z1, Zi1−1, Zi1, . . . , Zi(m−1)/2−1, Zi(m−1)/2) (6.5)
for 2≤ i1−1 < i1 < i2−1 < i2 <··· < i(m−1)/2−1 < i(m−1)/2≤ n and
Conv(Zi1−1, Zi1, . . . , Zi(m−1)/2−1, Zi(m−1)/2, Zn) (6.6)
for 1≤ i1−1 < i1 < i2−1 < i2 <··· < i(m−1)/2−1 < i(m−1)/2≤ n−1.
This description of the facets is commonly known as Gale’s evenness criterion [21].
An important example for the physics of scattering amplitudes in planar N = 4 super
Yang-Mills theory is the m = 4 cyclic polytope which has boundaries:
Conv(Zi−1, Zi, Zj−1, Zj) (6.7)
for 1≤ i−1 < i < j−1 < j≤ n+1. The physical applications are explained in Section 6.6.
– 27 –

<!-- page 31 -->

6.1.3 Dual polytopes
Let (Pm,A) be a convex polytope and let Y ∈ Pm(R) be a point away from any boundary
component. We now deﬁne the dual of A at Y , denotedA∗
Y , which is a convex polytope
in the linear dual of Pm (also denoted Pm). For the moment let us “de-projectivize” Y so
that Y ∈ Rm+1.
Recall that each facet of A is given by the zero-set (along ∂A) of some dual vector
W∈ Rm+1. Before going to projective space, we pick the overall sign ofW so that W·Y > 0
for our Y . We say that the facets are oriented relative to Y . Now assume that the facets
ofA are given by W1, . . . , Wr. Then we deﬁne:
A∗
Y := Conv(W1, . . . , Wr) :=



r∑
j=1
CjWj∈ Pm| Cj≥ 0, j = 1, . . . , r


 (6.8)
Not that the (relative) signs of the Wj’s are crucial, hence so is the position of Y relative
to the facets.
In the special case where Y ∈ Int(A), we letA∗ :=A∗
Y and refer to this simply as the
dual ofA. An equivalent deﬁnition of the dual of A is:
A∗ ={W∈ Pm| W· Y ≥ 0 for all Y ∈A} . (6.9)
A priori, the inequality W· Y ≥ 0 may not make sense when W and Y are projective. As
in (6.8), we give it precise meaning by working ﬁrst in Rm+1, and then taking the images
in Pm (see also Appendix D).
For generic Y , we also wish to assign an orientation to A∗
Y as follows. Suppose we
orient the facets W1, . . . , Wr relative to the interior ofA. Let s denote the number of terms
Wj· Y that are negative. Then we orient A∗
Y based on the parity of s. In particular, the
dual for Y ∈ Int(A) is positively oriented.
It should be obvious that ( Pm,A∗
Y ) is a positive geometry for each Y .
An important observation about the dual polytopeA∗
Y is that it has “opposite” combi-
natorics toA. In other words, vertices of A correspond to the facets ofA∗
Y and vice versa.
Since we assumed thatA has n vertices Z1, Z2, . . . , Zn, the dual polytope A∗
Y has n facets
corresponding to{W| W· Zi = 0} for i = 1, 2, . . . , n. Suppose a facet of A is adjacent to
vertices Zi1, . . . , Zim, then the dual vertex W satisﬁes W· Zi1 = . . . = W· Zim = 0 so that
WI = ϵII 1...ImZI1
i1 . . . ZIm
im (6.10)
where we have ordered the vertices so that Y· W > 0. This is a straightforward general-
ization of (5.6). Sometimes we will also write
W = (i1 . . . im) (6.11)
to denote the same quantity. Applying this to Section 6.1.2 gives us all the vertices of the
polytope dual to a cyclic polytope.
– 28 –

<!-- page 32 -->

We now state an important fact about dual polytopes. Given a signed triangulation
A = ∑
iAi of a convex polytopeA by other convex polytopesAi (see Sections 3 and 3.3),
and a point Y not along any boundary component, we have
A =
∑
i
Ai ⇒ A ∗
Y =
∑
i
A∗
iY (6.12)
In words, we say that
Dualization of polytopes “commutes” with triangulation. (6.13)
This is a crucial geometric phenomenon to which we will return. While we do not provide
a direct geometric proof, we will argue its equivalence to the triangulation independence of
the canonical form and the existence of a volume interpretion for the form in Section 7.4.1.
6.2 Generalized polytopes on the projective plane
Let us now discuss a class of positive geometries in P2 which includes Examples 5.2 and
5.3. Let C⊂ R2 be a closed curve that is piecewise linear or quadratic. Thus C is the
union of curves C1, C2, . . . , Cr where each Ci is either a line segment, or a closed piece of
a conic. We assume that C has no self-intersections, and let U⊂ R2 be the closed region
enclosed by C. We will further assume that U is a convex set. Deﬁne the degree d(U) ofU
to be the sum of the degrees of the Ci. We now argue that if d≥ 3,
(P2,U) is a positive geometry. (6.14)
We will proceed by induction on d = d(U). For the base case d = 3, there are two
possibilities: (a) U is a triangle, or (b) U is a convex region enclosed by a line and a
conic. For case (a), Ω(U) was discussed in Section 5.2. For case (b), Ω( U) was studied in
Example 5.3. In both cases, ( P2,U) is a positive geometry.
Now suppose that d(U) = d≥ 4 and that one of the Ci is a conic. Let L be the line
segment joining the endpoints of Ci. By convexity, L lies completely within U, and thus
decomposesU into the union U =U1∪U 2 of two regions where U1 has Ci and L as its
“sides”, while U2 satisﬁes the same conditions as U, but has more linear sides. In other
words,U is triangulated byU1,2, and by the discussion in Section 3, U is a pseudo-positive
geometry with Ω(U) = Ω(U1) + Ω(U2). In addition, we argue that U must be a positive
geometry, since all its boundary components (line segments on the projective line) are
positive geometries.
If none of the Ci is a conic, then U is a convex polygon in R2. We can slice oﬀ a
triangle and repeat the same argument.
Let us explicitly work out a simple example deﬁned by two linear boundaries and one
quadratic: a “pizza” slice.
Example 6.1. Consider a “pizza” shaped geometry; that is, a sector T (θ1, θ2) of the unit
circle between polar angles θ1, θ2, which is bounded by two linear equationsq1 =−x sin θ1+
y cos θ1≥ 0 and q2 = x sin θ2− y cos θ2≥ 0, and an arc f = 1− x2− y2≥ 0. Let us assume
– 29 –

<!-- page 33 -->

for simplicity of visualization that 0 ≤ θ1 < θ 2≤ π. See Figure 1d for a picture for the
case (θ1, θ2) = (π/6, 5π/6).
The canonical form is given by
Ω(T (θ1, θ2)) = [sin(θ2− θ1) + (−x sin θ1 + y cos θ1) + (x sin θ2− y cos θ2)]
(1− x2− y2)(−x sin θ1 + y cos θ1)(x sin θ2− y cos θ2) dxdy (6.15)
Let us take the residue along the linear boundary q1 = 0 via the limit x→ y cot θ1, and
conﬁrm that the result is the canonical form on the corresponding boundary component.
We get
Resq1=0Ω(T (θ1, θ2)) = (sin θ1)
(sin θ1− y)y dy (6.16)
which is the canonical form on the line segment y∈ [0, sin θ1] with positive orientation.
The upper bound y < sin θ1 is simply the vertical height of the boundary q1 = 0.
Similarly, the residue at q2 = 0 is given by
Resq2=0Ω(T (θ1, θ2)) =− (sin θ2)
(sin θ2− y)y dy (6.17)
which is the canonical form on the line segment y∈ [0, sin θ2], again with negative orienta-
tion.
The residue along the arc can be computed in a similar manner as for the segment of
the disk in Example 5.2, so we leave this as an exercise for the reader.
For θ1 = 0 , θ2 = π, we are reduced to the northern half disk from Example 5.2, so
T (0, π) =S(0). A quick substitution shows that the canonical forms match as well.
6.3 A naive positive part of partial ﬂag varieties
In this section, let us consider a partial ﬂag variety Fl(n; k) with k := (k1 < k2 <··· < kr)
where
Fl(n; k) :={V = (V1⊂ V2⊂···⊂ Vr⊂ Cn)| dim Vi = ki} (6.18)
is the space of ﬂags, whose components are linear subspaces of speciﬁed dimensions k1 <
k2 <··· < kr. Compared to Section 5.8, we have Fl( n; k) = GL(n)/P for an appropriate
choice of parabolic subgroup P .
In Section 5.8, we deﬁned the totally nonnegative part Fl( n; k)≥0. We now deﬁne the
naive nonnegative part Fl(n; k) ˜≥0 of Fl(n; k) to be the locus of V where Vi∈ G≥0(ki, n) for
all i. The ˜≥0 is to remind us that Fl( n; k) ˜≥0 may diﬀer from the totally nonnegative part
Fl(n; k)≥0. We speculate that
(Fl(n; k), Fl(n; k) ˜≥0) is a positive geometry. (6.19)
The naive nonnegative part Fl(n; k) ˜≥0 has the following symmetry property that the totally
nonnegative part Fl(n; k)≥0 lacks: if all the ki have the same parity, then the cyclic group
Z/nZ acts on Fl( n; k) ˜≥0. To see this, we represent points of Fl( n; k) ˜≥0 by kr× n full-rank
– 30 –

<!-- page 34 -->

matrices C so that Vi is the span of the ﬁrst ki rows. If C1, C2, . . . , Cn denote the n columns
of C, then the cyclic group acts by sendingC to the C′ with columns±Cn, C1, C2, . . . , Cn−1,
where the sign is + if the ki are odd, and− otherwise.
Unlike Fl(n; k)≥0, the naive nonnegative part Fl( n; k) ˜≥0 is in general a polytope-like
positive geometry: the canonical forms will have zeros. The case Fl( n; 1, 3) ˜≥0 is studied in
some detail in [22], and we will discuss its canonical form in Section 7.2.5.
6.4 L-loop Grassmannians
We now deﬁne theL-loop Grassmannian G(k, n; k), where k := (k1, . . . , kL) is a sequence of
positive integers. A point V in the L-loop Grassmannian G(k, n; k) is a collection of linear
subspaces VS ⊂ Cn indexed by S, where S :={s1, . . . , sl} is any subset of {1, 2, . . . , L}
for which kS := ks1+ . . .+ksL≤ n−k. Moreover, we require that dim VS = k + kS, and
VS⊂ VS′ whenever S⊂ S′. For simplicity we sometimes write Vi = V{i}, Vij = V{i,j}, and
so on and so forth. In particular, V∅⊂ Vs for any one-element set S ={s}.
We say that a point V ∈ G(k, n; k) is “generic” if Vi∩ Vj = V∅ for any i̸= j. For
such points, we have VS = span(Vs1, Vs2, . . . , Vsℓ) for any S ={s1, s2, . . . , sℓ}, so that V is
determined completely by V1, V2, . . . , VL. The space G(k, n; k) is naturally a subvariety of
a product of Grassmannians, and in particular it is a projective variety.
If L = 0, then the 0-loop Grassmannian reduces to the usual Grassmannian G(k, n).
If L = 1, the 1-loop Grassmannian reduces to the partial ﬂag variety Fl( n; k, k + k1). We
may refer to the 0-loop Grassmannian as the tree Grassmannian. The distinction between
“trees” and “loops” comes from the terminology of scattering amplitudes. We caution
that “loop Grassmannian” commonly refers to another inﬁnite dimensional space in the
mathematical literature, which is also called the aﬃne Grassmannian.
We now deﬁne the positive partG>0(k, n; k) of G(k, n; k). Consider the set of (k+K)×
n matrices M(k + K, n), where K := k1 + . . .+ kL. We will denote each matrix as follows:
P :=


C
D1
. . .
DL

 (6.20)
where C has k rows, and Di has ki rows for i = 1, . . . , L. We say that P is positive if for
each S ={s1, s2, . . . , sℓ} the matrix formed by taking the rows of C, Ds1, Ds2, . . . , Dsℓ is
positive, that is, has positive ( k + kS)× (k + kS) minors. Each positive matrix P gives
a point V ∈ G(k, n; k), where VS is the span of the rows of C, Ds1, Ds2, . . . , Dsℓ. Two
points P1,2 are equivalent if they map to the same point V . Each equivalence class deﬁnes
a point on the (strictly) positive part G>0(k, n; k). The nonnegative part G≥0(k, n; k) is
the closure of G>0(k, n; k) in G(k, n; k)(R).
There exists a subgroupG(k; k) of GL(k + K) acting on the left whose orbits in M(k +
K, n) are equivalence classes of matrices P deﬁning the same point V . Elements ofG(k; k)
allow row operations within each of C, or the Di, and also allows adding rows of C to each
Di.
– 31 –

<!-- page 35 -->

We caution that not every point V ∈ G(k, n; k) is representable by a matrix P . For
example, for G(0, 3; 1, 1), the P matrix is a 2×3 matrix. Consider a point on the boundary
where the two rows of P are scalar multiples of each other, then V1 = V2 and additional
information is required to specify the 2-plane V1,2. So there are even points in the boundary
of G≥0(k, n; k) that cannot be represented by P .
Let us focus our attention on theL-loop Grassmannian G(k, n; ℓL) where lL := (l, . . . , l)
with l appearing L times. The case l = 2 is the case of primary physical interest. TheL-loop
Grassmannian G(k, n; lL) has an action of the symmetric group SL on the set{1, 2, . . . , L}
with L elements. For a permutation σ∈ SL, we have σ(V )S = Vσ(S). In addition, when l
is even, the action of SL on G(k, n; lL) preserves the positive part: permuting the blocks
Di of the matrix P preserves the positivity conditions.
The L-loop Grassmannian G(k, n; k) is still very poorly understood in full generality.
For instance, a complete stratiﬁcation extending the positroid stratiﬁcation of the positive
Grassmannian is still unknown. The existence of the canonical form is also unknown.
Nonetheless, we have identiﬁed the canonical form for some L = 1 cases, which we discuss
in Section 7.2.5, and some L = 2 cases.
The proven existence of some L = 1 canonical forms is highly non-trivial. We therefore
speculate that
(G(k, n; k), G≥0(k, n; k)) is a positive geometry . (6.21)
Note that for even ℓ, the speculative positive geometry G(k, n; ℓL) should have an action of
SL: the symmetric group acts on the boundary components, and furthermore the canonical
form will be invariant under SL.
We may also denote a generic point in the loop Grassmannian as
Y = (Y, Y1, . . . , YL) (6.22)
where VS = span{Y, Ys1, . . . , Ysl} for any S. Or, for k = 2L we may use notation like
(Y, (AB)1, . . . ,(AB)L) or (Y, AB, CD, EF, . . .), which are common in the physics literature.
Example 6.2. Consider the space G(0, 4; 22) which is isomorphic to the “double Grassman-
nian” ( G(2, 4)× G(2, 4)), and has an action of the symmetric group S2. Let ( C1, C2)∈
G(2, 4)2 denote a point in the space, with both C1 and C2 thought of as 2 × 4 matrices
modded out by GL(2) from the left. The interior of the positive geometry is given by the
following points in matrix form:
(G(2, 4)2)>0 :={(C1, C2) : C1, C2∈ G>0(2, 4) and det
(
C1
C2
)
> 0} (6.23)
In other words, both C1, C2 are in the positive Grassmannian, and their combined 4 ×
4 matrix (i.e. the two rows of C1 stacked on top of the two rows of C2) has positive
determinant.
We can parametrize the interior with eight variables as follows:
(
C1
C2
)
=


1 x1 0−w1
0 y1 1 z1
1 x2 0−w2
0 y2 1 z2

 (6.24)
– 32 –

<!-- page 36 -->

The conditions C1, C2∈ G>0(2, 4) impose that all eight variables be positive, while the
ﬁnal condition requires
det
(
C1
C2
)
=−(x1− x2)(z1− z2)− (y1− y2)(w1− w2) > 0 (6.25)
The canonical form can be computed by a triangulation argument given in [23]:
Ω((G(2, 4)2)≥0) = dx1dy1dz1dw1dx2dy2dz2dw2(x1z2+x2z1+y1w2+y2w1)
x1x2y1y2z1z2w1w2[(x1−x2)(z1−z2)+(y1−y2)(w1−w2)] (6.26)
The 9 poles appearing in the denominator account for the boundaries deﬁned by the 9
inequalities. Note that the form is symmetric under exchanging 1 ↔ 2, as expected from
the action of S2.
Let us illustrate the simple method by which this result is obtained by looking at a
smaller example: a 4-dimensional boundary. Let us go to the boundary where y1,2 = w1,2 =
0. The geometry is then simply given by
x1,2 > 0, z1,2 > 0, (x1− x2)(z1− z2) < 0 (6.27)
But this can clearly be triangulated (see Section 3) in two pieces. We either have z1 >
z2 > 0 and x1 < x 2, or vice-versa. We can trivially triangulate z1 > z 2 > 0 by saying
z2 = a, z1 = a + b with a > 0, b > 0 and so the form is da db/ab = dz2dz1/z2(z1− z2). Thus
the full form is
dx1dx2dz2dz2×
( 1
z2(z1− z2)
1
x1(x2− x1) + 1
z1(z2− z1)
1
x2(x1− x2)
)
(6.28)
= dx1dx2dz1dz2(x2z1 + x1z2)
x1x2z1z2(x2− x1)(z1− z2) . (6.29)
which of course can be obtained from (6.26) by taking residues at the corresponding bound-
aries.
6.5 Grassmann, loop and ﬂag polytopes
Let us begin by reviewing the construction of Grassmann polytopes [7], which will motivate
the construction of ﬂag polytopes and loop polytopes.
Let Z1, Z2, . . . , Zn∈ Rk+m be a collection of vertices. The linear map Z : Rn→ Rk+m
induces a rational map Z : G(k, n)→ G(k, k + m) in the obvious way. If the map Z is
well-deﬁned on G≥0(k, n), we deﬁne the image
Z(G≥0(k, n)) ={C· Z| C∈ G≥0(k, n)}, or more generally Z(Πf,≥0) (6.30)
to be a Grassmann polytope. Note that we allow Z(Πf,≥0) in the deﬁnition because we
want faces of Grassmann polytopes to also be Grassmann polytopes.
In [7], it is shown that the following condition
There exists a ( k+m)×k real matrix M so that Z·M has positive k×k minors. (6.31)
– 33 –

<!-- page 37 -->

implies that Z(G≥0(k, n)) is well-deﬁned. When k = 1, (6.31) reduces to (6.2). In [7], (6.2)
was used to deﬁne Grassmann polytopes but recently Galashin has announced that there
exist images Z(G≥0(k, n)) that do not satisfy (6.31). See [7, 24] for a discussion of(6.31)
and other related criteria.
We now deﬁne ﬂag polytopes and loop polytopes generalizing Grassmann polytopes,
and give a condition similar to (6.31). We may sometimes refer to Grassmann polytopes
also as tree Grassmann polytopes and loop polytopes as loop Grassmann polytopes.
Let Z be a full rank n×(k+m) real matrix thought of as a linear map Z : Rn→ Rk+m.
Set
X := Fl(n; k) and d := kr = max
i
(ki)
for the former and assume that k+m≥ d, and
X := G(k, n; k) and d := max{dim VS| dim VS≤ k+m}
for the latter. In the ﬁrst case, we have a rational map Z : Fl(k; n)→ Fl(k; k + m) sending
Vi to Z(Vi) for i = 1, . . . , r. In the second case we have a rational map Z : G(k, n; k)→
G(k, k + m; k) sending VS to Z(VS). We then deﬁne the ﬂag polytope, or loop polytope to
be the image Z(X≥0), whenever the map Z is well-deﬁned on X≥0 (here X≥0 refers to the
naive nonnegative part Fl(n; k) ˜≥0 in the case X = Fl(n; k)). In the case of X = G(k, n; 0),
this reduces to the deﬁnition of a Grassmann polytope. We speculate that
Z(X≥0) is a positive geometry, (6.32)
where the ambient complex variety is taken to be the Zariski closure of Z(X≥0).
We now introduce the condition
There exists a ( k+m)×d real matrix M such that Z·M has positive d×d minors.(6.33)
generalizing (6.31). We claim that
Under (6.33), the image Z(X≥0) is well-deﬁned in both cases. (6.34)
Note that any positive Z satisﬁes (6.33) [7, Lemma 15.6].
Let us now prove (6.34). In [7], it is shown that Z(G≥0(d, n)) is well-deﬁned if Z
satisﬁes (6.33). We shall show that (6.33) implies the same statement for all 1 ≤ d′≤ d.
This will show that Z(Vs) in the Fl( k) case (resp. Z(VS) in the G(k, n; lL) case) is well-
deﬁned for V ∈ X≥0, proving (6.34).
We think of Z as a point in G(k + m, n). The condition (6.33) is equivalent to the
condition that there exists U ∈ G>0(d, n) such that U ⊂ Z, i.e. Z contains a totally
positive subspace of dimension d. In [7, Lemma 15.6], it is shown that if U∈ G>0(d, n)
then it contains U′∈ G>0(d′, n) for all d′≤ d. It follows that (6.33) implies the same
condition for all values d′≤ d, completing the proof.
– 34 –

<!-- page 38 -->

6.6 Amplituhedra and scattering amplitudes
Following the discussion in Section 6.5, let us further suppose that Z is positive: all the
ordered ( k + m)× (k + m) minors are positive. In other words, the rows of Z form the
vertices of a cyclic polytope. Then the Grassmann polytope
A(k, n, m) := Z(G≥0(k, n)) (6.35)
is known as the tree Amplituhedron [4, 23]. For instance, the tree Amplituhedron for k = 1
is a cyclic polytope in Pm(R).
Now consider the loop Grassmannian G(k, n; lL) . The corresponding L-loop Grass-
mann polytope is called the L-loop Amplituhedron [4, 23]:
A(k, n, m; lL) := Z(G≥0(k, n; lL)) (6.36)
We also refer to this space as the Amplituhedron at L-loops or simply the Amplituhedron
whenever the loop level L is understood. In particular, the 0-loop Amplituhedron is the
tree Amplituhedron. The following special case of (6.32) is at the heart of the connection
between scattering amplitudes and our work.
Conjecture 6.3. Grassmann polytopes (both trees and loops), particularly Amplituhedra,
are positive geometries.
It follows from the Tarski-Seidenberg theorem (see Appendix J) that tree and loop
Grassmann polytopes are all semialgebraic sets. In other words, they are given as a ﬁnite
union of sets that can be “cut out” by polynomial equations in the Pl¨ ucker coordinates
and polynomial inequalities in the Pl¨ ucker coordinates. While the Tarski-Seidenberg the-
orem guarantees that our geometries are semi-algebraic, it does not provide us with the
homogeneous inequalities needed to “cut out” the geometries. Identifying such inequalities
is an outstanding problem, progress on which will be reported in [25]. However, this still
does not prove the existence of the canonical form.
The m = 4, l = 2 Amplituhedron is the most interesting case for physics, because it
appears to provide a complete geometric formulation of all the planar scattering amplitudes
inN = 4 super Yang-Mills. More precisely,
the n-particle NkMHV tree amplitude = Ω( A(k, n, 4)) (6.37)
the integrand of the n-particle NkMHV L-loop amplitude = Ω( A(k, n, 4; 2L))(6.38)
We will often denote the physical Amplituhedron simply asA(k, n; L), and the physical tree
Amplituhedron more simply as A(k, n). Historically, the scattering amplitudes were ﬁrst
computed using techniques from quantum ﬁeld theory, and were subsequently recognized
as top-degree meromorphic forms with simple poles on the boundary of the Amplituhedron
and unit leading residues, thus providing the original motivation for the study of canonical
forms. The existence of the scattering amplitudes provides strong evidence for the existence
of canonical forms on Amplituhedra.
– 35 –

<!-- page 39 -->

7 Canonical forms
The main purpose of this section is to establish a list of methods and strategies for com-
puting the canonical form of positive geometries. A summary of the main methods is given
as follows:
• Direct construction from poles and zeros: We propose an ansatz for the canon-
ical form as a rational function and impose appropriate constraints from poles and
zeros.
• Triangulations: We triangulate a generalized polytope by generalized simplices and
sum the canonical form of each piece.
• Push-forwards: We ﬁnd morphisms from simpler positive geometries to more com-
plicated ones, and apply the push-forward via Heuristic 4.1.
• Integral representations: We ﬁnd expressions for the canonical form as a volume
integral over a “dual” geometry, or as a contour integral over a related geometry.
7.1 Direct construction from poles and zeros
Consider a positive geometry ( X, X≥0) of dimension m for which there exists a degree-one
morphism Φ : ( Pm,A)→ (X, X≥0) for some positive geometry A in projective space. By
Heuristic 4.1, it suﬃces to compute the canonical form on A before pushing forward the
result onto X≥0 via Φ. Since the map is of degree one, the push-forward is usually trivial.
SupposeA is deﬁned by homogeneous polynomial inequalities qi(Y )≥ 0 indexed by i
for Y ∈ Pm. Then an ansatz for the canonical form is the following:
Ω(A) = q(Y )⟨Y dmY⟩∏
i qi(Y ) (7.1)
for some homogeneous polynomial q(Y ) in the numerator which must satisfy:
deg q =
∑
i
deg qi− m− 1 (7.2)
so that the form is invariant under local GL(1) action Y → α(Y )Y . The method of
undetermined numerator is the idea that the numerator can be solved by imposing residue
constraints. Note that this method operates under the assumption that a solution to the
numerator exists, which in most cases is a non-trivial fact.
We illustrate the idea with a few simple examples below.
Example 7.1. Consider the quadrilateralA :=A(Z1, Z2, Z3, Z4) in P2(R) with facets given
by the four inequalities q1 = x≥ 0, q 2 = 2y− x≥ 0, q 3 = 3− x− y≥ 0, q 4 = 2− y≥ 0.
The picture is given in Figure 1b, and the vertices are
ZI
1 = (1, 0, 0), Z I
2 = (1, 2, 1), Z I
3 = (1, 1, 2), Z I
4 = (1, 0, 2) (7.3)
with (1, x, y)∈ P2(R) as usual.
– 36 –

<!-- page 40 -->

We will derive the canonical form with the following ansatz.
Ω(A) = (A + Bx + Cy)dxdy
x(2y− x)(3− x− y)(2− y) (7.4)
for undetermined coeﬃcients A, B, C. Note that the numerator must be linear by (7.2).
There are six (4 choose 2) double residues. Those corresponding to vertices of the
quadrilateral must have residue ±1 (the sign is chosen based on orientation), while those
corresponding to two opposite edges must have residue zero. We list these requirements as
follows, where we denote Resji := Resqj=0Resqi=0:
Res12 = A
12 = +1 (7.5)
Res23 = A + 2B + C
6 = +1 (7.6)
Res34 = A + B + 2C
3 = +1 (7.7)
Res41 = A + 2C
4 = +1 (7.8)
Res13 = A + 3C
6 = 0 (7.9)
Res24 =− A + 4B + 2C
12 = 0 (7.10)
By inspection, the only solution is ( A, B, C) = (12,−1,−4). It follows that
Ω(A) = (12− x− 4y)dxdy
x(2y− x)(3− x− y)(2− y) (7.11)
We observe that since there are many more equations than undetermined coeﬃcients, the
existence of a solution is non-obvious.
This method becomes complicated and intractable pretty fast. However, in the case
of cyclic polytopes, a general solution was identiﬁed in [8] which we review below.
7.1.1 Cyclic polytopes
We now apply the numerator method to the cyclic polytope geometry, described in [8].
Let us illustrate how it works for the case of a quadrilateral A :=A(Z1, Z2, Z3, Z4). We
know that the form must have poles when ⟨Y 12⟩,⟨Y 23⟩,⟨Y 34⟩,⟨Y 41⟩→ 0; together with
weights this tells us that
Ω(A) = LI YI
2!⟨Y 12⟩⟨Y 23⟩⟨Y 34⟩⟨Y 41⟩ (7.12)
for some LI. We must also require that the codimension 2 singularities of this form only
occur at the corners of the quadrilateral. But for generic L, this will not be the case;
writing (ij) for the line⟨Y ij⟩ = 0, we will also have singularities at the intersection of the
lines (12) and (34), and also at the intersection of (23) , (14). The numerator must put a
– 37 –

<!-- page 41 -->

zero on these conﬁgurations, and thus we have that L must be the line that passes through
(12)∩ (34) as well as (23)∩ (41):
LI = ϵIJK ((12)∩ (34))J((23)∩ (14))K (7.13)
If we expand out (ab)∩ (cd) := Za⟨bcd⟩− Zb⟨acd⟩ =−Zc⟨abd⟩ + Zd⟨abc⟩, we can reproduce
the expressions for this area in terms of triangulations.
Note that we can interpret the form as the area of the dual quadrilateral bounded by the
edges Z1, Z2, Z3, Z4 and hence the vertices W1 = (12), W2 = (23), W3 = (34), W4 = (41).
See (6.11) for the notation. By going to the aﬃne space with Y at inﬁnity as Y = (1, 0, 0),
Wi = (1, W′
i), we ﬁnd the familiar expression for the area of a quadrilateral with the vertices
W′
1, W′
2, W′
3, W′
4,
(W′
3− W′
1)× (W′
4− W′
2). (7.14)
where the× denotes the Euclidean cross product.
We can continue in this way to determine the form for any polygon. For instance for
a pentagonA, we have the general form
Ω(A) = LIJ YI YJ
2!⟨Y 12⟩⟨Y 23⟩⟨Y 34⟩⟨Y 45⟩⟨Y 51⟩ (7.15)
but now the numerator must put a zero on all the 5 bad singularities where (12) , (34)
intersect, (23) , (45) intersect and so on. Thus LIJ must be the unique conic that passes
through all these ﬁve points. If we let BI
i = [(i, i+1)∩ (i+2, i+3)]I be the bad points, then
LIJ = ϵ(I1J1)···(I5J5)(IJ )(B1B1)(I1J1)··· (B5B5)(I5J5) (7.16)
where ϵ(I1J1)(I2J2)···(I6J6) is the unique tensor that is symmetric in each of the ( IJ )’s but
antisymmetric when swapping ( IiJi)↔ (IjJj).
This construction for the numerator generalizes for all n-gons. Just from the poles
Ω(A) takes the form
Ω(A) = NI1···In−3YI1··· YIn−3
⟨Y 12⟩···⟨ Y n1⟩ (7.17)
Now there are N = n(n− 1)/2− n = ( n2− 3n)/2 “bad” intersections Ba,b of non-
adjacent lines, BI
a,b = [(a, a+1)∩(b, b+1)]I. But there is a unique (up to scale) numerator
that puts a zero on these bad intersections:
LI1···In−3 = ϵ(I (1)
1 ···I (1)
n−3)(I (2)
1 ···I (2)
n−3)···(I (N )
1 ···I (N )
n−3)(I1···In−3)
N∏
S=1
BI (S)
1
S ··· B
I (S)
n−3
S (7.18)
where we have re-labeled the intersections as BS for S = 1, . . . , N. Note that in order for
the ϵ tensor to exist, it is crucial that N+1 is the dimension of rank n−3 symmetrc tensors
on R3.
It is interesting that the polygon lies entirely inside the zero-set deﬁned by the numer-
ator: the “bad” singularities are “outside” the good ones.
– 38 –

<!-- page 42 -->

For higher-dimensional polytopes the story is much more interesting as described in
[8]. Here we content ourselves with presenting one of the examples which illustrates the
novelties that arise.
Consider the m = 3 cyclic polytope for n = 5, with vertices Z1, . . . , Z5. The boundaries
of the cyclic polytope in m = 3 dimensional projective space are of the form (1 , i, i + 1)
and (n, j, j + 1), which here are simply (123) , (134), (145), (125), (235), (345).
NIJ YI YJ
⟨Y 123⟩⟨Y 134⟩⟨Y 145⟩⟨Y 125⟩⟨Y 235⟩⟨Y 345⟩ (7.19)
The numerator corresponds to a quadric in P3 which has 4 × 5/2 = 10 degrees of
freedom, and so can be speciﬁed in principle by vanishing on 9 points.
Naively, however, much more is required of the numerator than vanishing on points.
The only edges of this polytope correspond to the lines ( i, j), but there are six pairs of the
above faces that do not intersect on lines ( i, j); we ﬁnd spurious residues at L1 = (123)∩
(145), L2 = (123)∩ (345), L3 = (134)∩ (125), L4 = (134)∩ (235), L5 = (145)∩ (235), L6 =
(125)∩ (345). So the numerator must vanish on these lines; the quadric must contain the
six lines Li. Also the zero-dimensional boundaries must simply correspond to the Zi, while
there are six possible intersections of the denominator planes that are not of this form,
so the numerator must clearly vanish on these six points X1,...,6 as well. Of course these
6 “bad points” all lie on the “bad lines”, so if the numerator kills the bad lines the bad
points are also killed.
But there is a further constraint that was absent for the case of the polygon. In the
polygon story, the form Ω was guaranteed to have sensible logarithmic singularities and
we only had to kill the ones in the wrong spots, but even this is not guaranteed for cyclic
polytopes. Upon taking two residues, for generic numerators we can encounter double (and
higher) poles. Suppose we approach the point Y → Z1, by ﬁrst moving Y to the line (13)
which is the intersection of the planes (123), (134). If we put Y = Z1 + yZ3, then two of the
remaining poles are⟨Y 145⟩ =−y⟨1345⟩ and⟨Y 125⟩ = y⟨1235⟩, and so we get a double-pole
y2. In order to avoid this and have sensible logarithmic singularities, the numerator must
vanish linearly as Y → Z1; the same is needed as Y → Z3 and Y → Z5. Thus in addition
to vanishing on the six lines Li, the numerator must also vanish at Y → Z1, Z3, Z5.
It is not a-priori obvious that this can be done; however quite beautifully the geometry
is such that the 6 lines Li break up into two sets, which mutually intersect on the 9 points
Xi and Z1,3,5, with three intersection points lying on each line. The numerator can thus
be speciﬁed by vanishing on these points, which guarantees that it vanishes as needed on
the lines.
More intricate versions of the same phenomenon happens for more general cyclic poly-
topes: unlike for polygons, apart from simply killing “bad points” the zero-set of the numer-
ator must “kiss” the positive geometry at codimension 2 and lower surfaces, to guarantee
getting logarithmic singularities. The form for m = 4 cyclic polytopes were constructed in
this way. We have thus seen what this most brute-force, direct approach to determining
the canonical form by understanding zeros and poles entails. The method can be powerful
– 39 –

<!-- page 43 -->

in cases where the geometry is completely understood, though as we have seen this can be
somewhat involved even for polytopes.
7.1.2 Generalized polytopes on the projective plane
Let us return to the study of positive geometries A in P2, in view of the current discussion
of canonical forms. In Sections 5.3 and 6.2 we explained that under the assumptions of
Appendix A, the boundary components are smooth curves and are thus either linear or
quadratic.
Let us suppose that we allow the boundary components to be singular curvesp(Y ) = 0,
as in Section 5.3.1, and furthermore we now allow p(Y ) to be of arbitrary degree d, and
have r double-points. For a degree d curve with r double-points, the genus is given by
(d−1)(d−2)/2−r. Now recall that curves of non-zero genus admit non-trivial holomorphic
top forms, which leads to non-unique canonical forms, thus violating our assumptions
in Section 2. We therefore require the curve to have (( d− 1)(d− 2)/2) double-points
and hence genus zero. This means that p(Y ) = 0 can be rationally parametrized as
YI = YI(t), or equivalently, that the normalization of the curve P (Y ) = 0 is isomorphic
to P1. In practice, it is easy to reverse-engineer the polynomial deﬁning the curve of
interest from a rational parametrization. Working with co-ordinate Y = (1, x, y), a rational
parametrization is of the form x(t) = Px(t)/Q(t), y(t) = Py(t)/Q(t). Then, the resultant
p(x, y) = R(Px(t)−xQ(t); Py(t)−yQ(t)) gives us the polynomial deﬁning the parametrized
curve. For instance taking x(t) = (t(t2 + 1))/(1 + t4), y(t) = (t(t2− 1))/(1 + t4) yields the
quartic “lemniscate” curve p(x, y) = 4((x2+y2)2−(x2−y2)), which has three double-points;
one at x = y = 0 and two at inﬁnity.
As for the canonical form, the numerator (see Section 7.1) must be chosen to kill
all the undesired residues. Recall that for a d-gon, the numerator has to put zeros on
d(d− 1)/2− d = (d2− 3d)/2 points, and that there is a unique degree ( d− 3) polynomial
that passes through those points, which determines the numerator uniquely up to overall
scale. It is interesting to consider an example which is the opposite extreme of a polygon.
Consider an irreducible degree d polynomial, with ( d− 1)(d− 2)/2 = ( d2− 3d)/2 + 1
singular points. To get a positive geometry, we can kill the residues on all but one of these
singular points, leaving just a single zero-dimensional boundary just as in our teardrop
cubic example of Section 5.3.1. These are the same number ( d2− 3d)/2 of points we want
to kill as in the polygon example, and once again there is a unique degree ( d− 3) curve
that passes through those points.
An example is provided by the “ampersand” geometry (see Figure 5) associated with
the quartic curve P (x, y) = ( y2− x2)(x− 1)(2x− 3)− 4(x2 + y2− 2x)2, which has three
singular points at (0 , 0), (1, 1), (1,−1). If we choose the numerator to be the line that kills
e.g. the points (0 , 0) and (1 ,−1), then we get a positive geometry corresponding to the
“teardrop” in the upper quadrant.
Two more examples: consider a region bounded by two quadrics Q1 and Q2. The
numerator of the form is Y · L for some line L. Now two generic quadrics intersect at
four points P1, P2, P3, P4. Mirroring the determination of the form for the case of the
quadrilateral, we can choose the line L appearing in the numerator to kill two of Pi’s, and
– 40 –

<!-- page 44 -->

-0.5 0.0 0.5 1.0 1.5 2.0
-1.0
-0.5
0.0
0.5
1.0
x
y
Figure 5 : An “ampersand” curve with boundary given by a quartic polynomial. The
shaded “teardrop” is a positive geometry.
this will give us the canonical form associated with the geometry (Q1,2·Y Y )≥ 0. Similarly,
consider a positive geometry deﬁned by a singular cubic C and a line W . Again we have
a numerator of the form Y· L. The line W intersects the cubic in three points P1, P2, P3.
If we pick the the line L to pass through one of the Pi as well as the singular point of
the cubic, we get the canonical form associated with the geometry. These constructions
can be extended to higher dimensions, where (as with the cyclic polytope example) we will
generically encounter numerators whose zeros touch the positive geometry on co-dimension
two (and lower dimensional) boundaries.
7.2 Triangulations
Recall from Section 3 that if a positive geometry is triangulated by a collection of other
positive geometries, its canonical form is given by the sum of the canonical forms of the
collection. We now apply this method to compute the canonical form of various generalized
polytopes.
7.2.1 Projective polytopes
LetA :=A(Z1, . . . , Zn) be a convex projective polytope. The canonical form Ω(A) can be
obtained from a triangulation ofA (see Section 3 and Appendix D). Let ∆ 1, ∆2, . . . ,∆r be
a triangulation ofA into simplices. For simplicity let us assume that the simplex interiors
are mutually non-overlapping.
The canonical form Ω(A) is given by
Ω(A) =
∑
i
Ω(∆i) (7.20)
– 41 –

<!-- page 45 -->

The fact that the simplicial canonical forms add is dependent on the assumption that the
orientation of the interior of ∆ i agrees with that of A for each i. More generally, for any
polytopal subdivision ofA into polytopesAi (i.e. a “triangulation” by polytopes), we have
Ω(A) =
∑
i
Ω(Ai). (7.21)
We begin with the simplest case: line segments in P1(R).
Example 7.2. Consider a triangulation of the segment [a, b] from Example 2.1 by a sequence
of successively connected segments:
[a, b] =
r⋃
i=1
[ci−1, ci] (7.22)
where a = c0 < c1 < . . . < cr = b. It is straightforward to check that
Ω([a, b]) = (b− a)dx
(b− x)(x− a) =
r∑
i=1
(ci− ci−1)dx
(ci− x)(x− ci−1) =
r∑
i=1
Ω([ci−1, ci]) (7.23)
More generally, for the positive geometry A = ⋃
i[ai, bi]⊂ P1 which is triangulated by
ﬁnitely many line segments with mutually disjoint interiors, the canonical form is:
Ω
(⋃
i
[ai, bi]
)
=
∑
i
Ω([ai, bi]) (7.24)
Example 7.3. SupposeA is a convex projective polytope, and Z∗ is a point in its interior,
thenA is triangulated by
A =
⋃
facets
Conv(Z∗, Zi1, Zi2, . . . , Zim) (7.25)
where we take the union over all choice of indicesi1, . . . , im for which Conv(Zi1, Zi2 . . . , Zim)
is a facet of the polytope, and we avoid repeated permutations of the same set of indices.
For each facet, we order the indices so thatZ∗, Zi1, . . . , Zim is positively oriented. It follows
that
Ω(A) =
∑
facets
[∗, i1, . . . , im] (7.26)
Recalling the facets of cyclic polytopes from Section 6.1.2, we have the following corol-
laries.
Example 7.4. The canonical rational function of a cyclic polytope A for even m can be
obtained as follows.
Ω(A) =
∑
1≤i1−1<i1<···<im/2−1<im/2≤n+1
[∗, i1−1, i1, . . . , im/2−1, im/2] (7.27)
For arbitrary Z∗, this is called a CSW triangulation. For Z∗ = Zi for some i, this is called
a BCFW triangulation.
– 42 –

<!-- page 46 -->

Example 7.5. The canonical rational function of a cyclic polytope A for odd m can be
obtained as follows.
Ω(A) =
∑
2≤i1−1<i1<···<i(m−1)/2−1<i(m−1)/2≤n
−[∗, 1, i1−1, i1, . . . , i(m−1)/2−1, i(m−1)/2](7.28)
+
∑
1≤i1−1<i1<···<i(m−1)/2−1<i(m−1)/2≤n−1
[∗, i1−1, i1, . . . , i(m−1)/2−1, i(m−1)/2, n](7.29)
for any Z∗. If we set Z∗ = Z1 or Zn, then we get
Ω(A) =
∑
2≤i1−1<i1<···<i(m−1)/2−1<i(m−1)/2≤n−1
[1, i1−1, i1, . . . , i(m−1)/2−1, i(m−1)/2, n](7.30)
7.2.2 Generalized polytopes on the projective plane
In this section we verify that the canonical form for the “pizza slice” geometry from Ex-
ample 6.1 can be obtained by triangulation.
Example 7.6. Recall the “pizza slice” geometryT (θ1, θ2) from Example 6.1. For simplicity,
we will assume reﬂection symmetry about the y-axis and letT (θ) :=T (θ, π− θ) for some
0≤ θ < π/ 2. Denote the vertices of the geometry by ZI
i ∈ P1(R) for i = 1, 2, 3, where
ZI
1 = (1, 0, 0), Z I
2 = (1, cos θ, sin θ), Z I
3 = (1,− cos θ, sin θ) (7.31)
The pizza slice is clearly the union of a segment of the disk (see Example 5.2) and a
triangle (see Section 5.2).
T (θ) =S(sin θ)∪A (Z1, Z2, Z3) (7.32)
It follows that
Ω(T (θ)) = Ω(S(sin θ)) + Ω(A(Z1, Z2, Z3)) (7.33)
= (2 cosθ)dxdy
(1−x2−y2)(y− sin θ) + (2 sin2 θ cos θ)dxdy
(sin θ−y)(−x sin θ+y cos θ)(x sin θ+y cos θ)(7.34)
= 2 cosθ(y + sin θ)dxdy
(1− x2− y2)(−x sin θ+y cos θ)(x sin θ+y cos θ) (7.35)
which is equivalent to (6.15) for θ1 = θ and θ2 = π− θ, with y− sin θ = 0 as a spurious
pole.
7.2.3 Amplituhedra and BCFW recursion
Motivated by physical principles of quantum ﬁeld theory, a recursion relation was discovered
for the canonical form of the physical Amplituhedron called BCFW recursion [26, 27]. This
is a rich subject on its own. While a full explanation of the recursion relation is beyond
the scope of this paper, we present a sketch of the idea here.
LetA be the amplituhedron deﬁned in (6.36). We begin by introducing an extra
parameter z by making the shift Zn→ Zn + zZn−1, which gives Ω(A)→ Ω(A(z)). The
principle of locality suggests that the canonical form can only develop simple poles in z
– 43 –

<!-- page 47 -->

(including possibly a simple pole at inﬁnity), which can be seen by studying the structure
of Feynman propagators. It follows that
Ω(A) =
∮
C
dz
z Ω(A(z)) (7.36)
where the contour C is a small counter-clockwise loop around the origin. Applying Cauchy’s
theorem by expanding the loop to inﬁnity gives
Ω(A) =−
∑
i
Resz→zi
Ω(A(z))
z + Ω(A(∞)) (7.37)
where zi denotes all the poles. The residue at inﬁnity is simply the Amplituhedron with
Zn removed.
The residues at zi, however, are more involved. Based on extensive sample computa-
tions, we make the following observations assuming D = dim(A):
• There exists a ∆-like positive geometry Ci in the loop Grassmannian G(k, n; 2L) of
dimension D.
• There exists a subset Ai ofA also of dimension D, called a BCFW cell.
• The map under Z :Ci→A i is a degree-one morphism. Since Ci is ∆-like, hence so is
Ai.
• Given ∆−like coordinates (1 , αi1, . . . , αiD)∈ PD(R) onCi, the residue at zi is given
by the push-forward:
−Resz→zi
Ω(A(z))
z = Z∗


D∏
j=1
dαij
αij

 = Ω(Ai) (7.38)
At L = 0, each set Ci is a positroid cell of the positive Grassmannian and Ai is the
image under Z. For L > 0 some generalization of this statement is expected to hold.
The precise construction of Ci is explained in [28]. While the map is never explicitly
mentioned in the reference, its geometric structure is explained in terms of momentum
twistor diagrams, which are loop extensions of Postnikov’s plabic graphs [5]. In particular,
the ∆-like coordinates can be read oﬀ from labels appearing on the graph, while the
diagrams at any k, n, L can be constructed from diagrams of lower k, n or L, hence the
recursive nature of BCFW.
We point out that while BCFW cells are ∆-like, they are not necessarily simplex-like.
Namely, their canonical forms may have zeros.
From (7.38) and the discussion in Section 3, it follows that the BCFW cells form a
boundary triangulation of the Amplituhedron:
Ω(A) =
∑
i
Ω(Ai) (7.39)
– 44 –

<!-- page 48 -->

Furthermore, it appears based on extensive numerical checks that the BCFW cells
have mutually disjoint interiors. So they triangulate the Amplituhedron in the ﬁrst sense
deﬁned in Section 3. We point out that if our assumptions on BCFW cells hold, then the
Amplituhedron must be a positive geometry.
Historically, BCFW recursion was ﬁrst discovered in the context of quantum ﬁeld
theory as an application of Cauchy’s theorem on the deformation parameter z. See [26].
The poles at zi correspond to Feynman propagators going on shell (i.e. locality), while
the residues at zi were constructed via the principle of unitarity in terms of amplitudes (or
loop integrands) of lower k, n or L with modiﬁcations on the particle momenta.
Since most positive geometries are not directly connected to ﬁeld theory scattering
amplitudes, we do not expect BCFW recursion to extend to all cases. Nonetheless, it is
conceivable that the canonical form can be reconstructed by an application of Cauchy’s
theorem to a clever shift in the boundary components. A solution to this problem would
allow us, in principle, to construct the canonical form of arbitrarily complicated positive
geometries from simpler ones.
7.2.4 The tree Amplituhedron for m = 1, 2
There is by now a rather complete understanding of the tree Amplituhedron with m = 1, 2,
for any k and n. The following results will be presented in detail elsewhere [25]. (For m = 1,
see also [29].) Here we will simply present (without proof) some simple triangulations of
these Amplituhedra, and give their associated canonical forms. We let A :=A(k, n, m)
whenever k, n, m are understood.
In the m = 1 Amplituhedron, YI
s is a k-plane in ( k+1) dimensions with s = 1, . . . , k
indexing a basis for the plane and I = 0, . . . , k indexing the vector components in ( k+1)
dimensions. We will triangulate by images of k−dimensional cells of G>0(k, n); in other
words for each cell we will look at the imageYI
s = ∑n
i=1 Csi(α1, . . . , αk)ZI
i , where α1, . . . , αk
are positive ∆−like co-ordinates for that cell. For every collection of k integers{i1, . . . , ik}
with 1≤ i1 < i2 <··· < ik≤ n− 1, there is a cell where
C{i1,...,ik}
sa =



1 a = is
αs a = is + 1
0 otherwise



(7.40)
with the positive variables αs≥ 0. In other words in this cell we have YI
s = ZI
is + αsZI
is+1.
Geometrically, in this cell the k-plane Y intersects the cyclic polytope of external
data in the k 1-dimensional edges ( Zi1, Zi1+1), . . . ,(Zik Zik+1). The claim that these cells
triangulate the m = 1 Amplituhedron is then equivalent to the statement that this Ampli-
tuhedron is the set of all k-planes which intersect the cyclic polytope in precisely k of its
1-dimensional consecutive edges (i.e. an edge between two consecutive vertices).
The motivation for this triangulation will be given (together with associated new char-
acterizations of the Amplituhedron itself) in [25]. For now we can at least show that these
cells are non-overlapping in Y space, by noting that in this cell, the following sequence of
minors
{⟨Y 1⟩,⟨Y 2⟩,··· ,⟨Y n⟩} (7.41)
– 45 –

<!-- page 49 -->

have precisely k sign ﬂips, with the ﬂips occurring at the locations (is, is+1) for s = 1, . . . , k.
Since the sign patterns are diﬀerent in diﬀerent cells, we can see that the cells are non-
overlapping; the fact that they triangulate the Amplituhedron is more interesting and will
be explained at greater length in [25].
The k-form associated with this cell is
Ω{i1,...,ik} = Z∗
( k∏
s=1
d log αs
)
=
k∏
s=1
dlog
(⟨Y, is+1⟩
⟨Y is⟩
)
(7.42)
and the full form is
Ω(A) =
∑
1≤i1<···<ik≤n−1
Ω{i1,...,ik} (7.43)
It is easy to further simplify this expression since the sums collapse telescopically. For
instance for k = 1 we have
∑
1≤i1≤n−1
dlog
(⟨Y, i1+1⟩
⟨Y i1⟩
)
= dlog
(⟨Y n⟩
⟨Y 1⟩
)
(7.44)
Note the cancellation of spurious poles in the sum leading nicely to the ﬁnal result. The
same telescopic cancellation occurs for general k, and for even k we are left with the ﬁnal
form
Ω(A) = dk×(k+1)Y
Vol GL(k)
∑
2≤j1−1<j1<···
<jk/2−1<jk/2≤n
[1, j1−1, j1, . . . , jk/2−1, jk/2] (7.45)
while for odd k we are left with
Ω(A) = dk×(k+1)Y
Vol GL(k)
∑
2≤j1−1<j1<···
<j(k−1)/2−1<j(k−1)/2≤n−1
[1, j1−1, j1, . . . , j(k−1)/2−1, j(k−1)/2, n] (7.46)
where the brackets denote
[j0, j1, . . . , jk] := ⟨j0 . . . jk⟩
⟨Y j0⟩···⟨ Y jk⟩ (7.47)
for any indices j0, . . . , jk. The brackets satisfy
k∏
s=1
d log
( ⟨Y js⟩
⟨Y js−1⟩
)
= dk×(k+1)Y
Vol GL(k)[j0, j1, . . . , jk] (7.48)
Note that each bracket can be interpreted as a simplex volume in Pk(R) whose vertices
are the Zj0, . . . , Zjk, with Y the hyperplane at inﬁnity. Note also that the combinatorial
structure of the triangulation is identical to triangulation of cyclic polytopes discussed in
Section 7.2.1. Indeed, when ⟨Y i⟩ > 0 for each i, the canonical rational function can be
interpreted as the volume of the convex cyclic polytope with vertices Z. However, these
conditions do not hold for Y on the interior of the Amplituhedron, since Y must pass
– 46 –

<!-- page 50 -->

through the interior of the cyclic polytope as it intersects k 1-dimensional consecutive
edges.
Starting with k = 2, this is not a positively convex geometry (see Section 9): the form
has zeros (and poles) on the interior of the Amplituhedron. We can see this easily for e.g.
k = 2, n = 4. We have a single term with a pole at ⟨Y 2⟩→ 0, so it is indeed a boundary
component, but it is trivial to see that ⟨Y 2⟩ can take either sign in the Amplituhedron, so
the form has poles and zeros on the interior.
We now consider the case m = 2, and triangulate the Amplituhedron with the image
of a collection of 2 × k dimensional cells of G>0(k, n). That is, for each cell we look at
the image YI
s = ∑n
i=1 Csi(α1, β1, . . . , αk, βk)ZI
i . Similar to m = 1, the cells are indexed by
{i1, . . . , ik} with 2≤ i1 < i2 <··· < ik≤ (n− 1). Now the C matrices are given by
C{i1,...,ik}
si =



(−1)s−1 i = 1
αs i = is
βs i = is + 1
0 otherwise



(7.49)
In other words, in this cell we have YI
s = (−1)s−1ZI
1 + αsZI
is + βsZI
is+1. As for m = 1, it
is easy to see that images of these cells are non-overlapping in Y space for essentially the
identical reason; in this cell it is easy to check that the sequence of minors
{⟨Y 12⟩,⟨Y 13⟩, . . . ,⟨Y 1n⟩} (7.50)
again has precisely k sign ﬂips, that occur at the locations ( is, is + 1) for s = 1, . . . , k.
The 2k-form associated with this cell is
Ω{i1,···,ik} = Z∗
( k∏
s=1
d log αs d log βs
)
=
k∏
s=1
dlog
( ⟨Y 1is⟩
⟨Y is, is + 1⟩
)
dlog
(⟨Y 1, is + 1⟩
⟨Y is, is + 1⟩
)
= dk(k+2)Y
Vol GL(k)[1, i1, i1+1; . . .; 1, ik, ik+1] (7.51)
where
[p1, q1, r1; . . .; pk, qk, rk] :=
[⟨
(Yk−1)s1p1q1r1
⟩
···
⟨
(Yk−1)sk pkqkrk
⟩
ϵs1···sk
]k
2k⟨Y p1q1⟩⟨ Y q1r1⟩⟨ Y p1r1⟩···⟨ Y pkqk⟩⟨ Y qkrk⟩⟨ Y pkrk⟩(7.52)
for any indices ps, qs, rs with s = 1, . . . , k and
(Yk−1)s := Ys1∧···∧ Ysk−1ϵss1···sk−1 (7.53)
As usual the full form arises from summing over the form for each piece of the trian-
gulation
Ω(A) =
∑
2≤i1<···ik≤n−1
Ω{i1,···,ik} (7.54)
– 47 –

<!-- page 51 -->

In particular, for k = 2, we have
Ω(A(2, 2, n)) =
⟨
Y d2Y1
⟩ ⟨
Y d2Y2
⟩
× (7.55)
∑
2≤i<j≤n−1
det
(
⟨Y1, i−1, i, i+1⟩⟨ Y1, j−1, j, j+1⟩
⟨Y2, i−1, i, i+1⟩⟨ Y2, j−1, j, j+1⟩
)2
22⟨Y 1i⟩⟨ Y 1, i+1⟩⟨ Y i, i+1⟩⟨ Y 1j⟩⟨ Y 1, j+1⟩⟨ Y j, j+1⟩
This is called the Kermit representation, and the summands [1 , i, i+1; 1, j, j+1] are
called Kermit terms . These are important for 1-loop MHV scattering amplitudes whose
physical AmplituhedronA(0, n; L=1) is isomorphic to the Amplituhedron A(2, n,2).
Returning to general k, of course the form also has spurious poles that cancel between
the terms, though unlike the case of m = 1 it cannot be trivially summed into a simple
expression with only physical poles. However there is an entirely diﬀerent representation
of the form, not obviously related to the triangulation of the Amplituhedron, which is
(almost) free of all spurious poles. This takes the form
Ω(A) = dk(k+2)Y
Vol GL(k)× (7.56)
∑
1≤i1<i2<···<ik≤n
⟨
(
Yk−1)s1
i1−1, i1, i1+1⟩···⟨
(
Yk−1)sk
ik−1, ik, ik+1⟩ϵs1···sk⟨Xi1··· ik⟩
⟨Y X⟩ ∏k
s=1⟨Y is, is+1⟩
Note the presence of a reference XIJ in this expression, playing an analagous role to a
“triangulation point” in a triangulation of a polygon into triangles [ X, i, i+1]. The ﬁnal
expression is however X-independent. Note also that apart from the ⟨Y X⟩ pole, all the
poles in this expression are physical.
This second “local” representation of the form Ω( A) allows us to exhibit something
that looks miraculous from the trianguation expression: Ω(A) is positive when Y is inside
the Amplituhedron, and so the m = 2 Amplituhedron is indeed a positively convex geome-
try (see Section 9)! Indeed, if we choose X judiciously to be e.g. XIJ = (ZlZl+1)IJ for some
l, then trivially all the factors in the denominator are positive. Also, ⟨XZi1··· Zik⟩ > 0
trivially due to the positivity of the Z data. The positivity of the ﬁrst factor in the nu-
merator is not obvious; however, it follows immediately from somewhat magical positivity
properties of the following “determinants of minors”. For instance for k = 2 the claim is
that as long as the Z data is positive,
det
(
⟨a, i− 1, i, i + 1⟩⟨ a, j− 1, j, j + 1⟩
⟨b, i− 1, i, i + 1⟩⟨ b, j− 1, j, j + 1⟩
)
> 0 (7.57)
for any a < b and i < j . Similarly for k = 3,
det


⟨a, b, i− 1, i, i + 1⟩⟨ a, b, j− 1, j, j + 1⟩⟨ a, b, k− 1, k, k + 1⟩
⟨a, c, i− 1, i, i + 1⟩⟨ a, c, j− 1, j, j + 1⟩⟨ a, c, k− 1, k, k + 1⟩
⟨b, c, i− 1, i, i + 1⟩⟨ b, c, j− 1, j, j + 1⟩⟨ b, c, k− 1, k, k + 1⟩

 > 0 (7.58)
– 48 –

<!-- page 52 -->

for any a < b < c ; i < j < k , with the obvious generalization holding for higher k. These
identities hold quite non-trivially as a consequence of the positivity of the Z data.
The existence of this second representation of the canonical form, and especially the
way it makes the positivity of the form manifest, is quite striking. The same phenomenon
occurs for k = 1 and any m–the canonical forms are always positive inside the polytope,
even though the determination of the form obtained by triangulating the polytope does
not make this manifest. For polytopes, this property is made manifest by the much more
satisfying representation of the form as the volume integral over the dual polytope. The
fact that the same properties hold for the Amplituhedron (at least for even m) suggests
that we should think of the “local” expression (7.56) for the form we have seen for m = 2
as associated with the “triangulation” of a “dual Amplituhedron”. We will have more to
say about dual positive Grassmannians and Amplituhedra in [30].
7.2.5 A 1-loop Grassmannian
We now consider the special case of the 1-loop positive GrassmannianG>0(1, n; 2) with k =
1 and L = 1, which is directly relevant for thephysical 1-loop AmplituhedronA(1, n; L=1).
The space G(1, n; 2) is the (3n− 7)-dimensional space consisting of 3× n matrices
P =
(
C
D
)
(7.59)
where the last two rows form the D matrix and the ﬁrst row forms the C matrix. The P
matrix has positive 3×3 minors while C has positive components. Alternatively, G(1, n; 2)
is the space of partial ﬂags {(V, W )| 0⊂ V ⊂ W ⊂ Cn} of subspaces where dim V = 1
and dim W = 3. The nonnegative part G≥0(1, n; 2) is given by those matrices P where the
row spaces of C and P are in the totally nonnegative Grassmannian.
There is an action of T+ = Rn
>0 on G≥0(1, n; 2). The quotient space G≥0(1, n; 2)/T+
can be identiﬁed with the space of n points (P1, . . . , Pn) in P2(R) in convex position (with
a ﬁxed distinguished line at inﬁnity L∞ with dual coordinates Q∞ = (1, 0, 0)), considered
modulo aﬃne transformations. The Pi are of course just the columns of P . For the
precise deﬁnition we refer the reader to [22], although we warn the reader that the positive
geometry is denoted G+(1, n; 1) in the reference. Using the geometry of such convex n-
gons, a collection of simplex-like cells ˜Πf,≥0⊂ G≥0(1, n; 2) are constructed in analogy to
the positroid cells Π f,≥0 of Section 6.5, where now f varies over a diﬀerent set of aﬃne
permutations. Note that some of the cells ˜Πf,≥0 are special cases of the totally positive
cells (Πw
u )≥0 of Rietsch and Lusztig described in Section 5.8, but some are not.
We sketch how ˜Πf,≥0 can be shown to be a positive geometry. First, associated to each
˜Πf,≥0 is a class of momentum-twistor diagrams Df [22, 28]. The edges of any such diagram
Df can be labeled to give a (degree-one) rational parametrization Rd
>0∼= ˜Πf,>0, and the
canonical form Ω( ˜Πf,≥0) is given by ∏
i dαi/αi where αi are the edge labels. Diﬀerent
diagrams for the same cell provide diﬀerent parametrizations. Each boundary component
C≥0 of ˜Πf,≥0 can be obtained by removing one of the edges of some momentum-twistor
diagram Df for ˜Πf,≥0, although some boundaries may be visible to only a proper subset
of diagrams. This shows that the residues of Ω( ˜Πf,≥0) give the forms Ω( C≥0).
– 49 –

<!-- page 53 -->

1 = X2X3 = 2
3
4
5
X1 5 1
2
3 = X1
4
X2 X3
4 = X2X3 = 5
1
2
3
X1
Figure 6: Spaces of pentagons (with vertices labeled 1 , 2, 3, 4, 5 for P1, P2, P3, P4, P5) that
correspond to the cells Π {1,2,5}, Π{2,3,5}, Π{3,4,5} respectively. In the leftmost picture, the
dashed line indicates that the edges 15 and 23 intersect on the side of 12 containing the
pentagon interior as shown. Each pentagon is inscribed in a “big” triangle with vertices
denoted X1, X2, X3. If we label the solid edge between i, i+1 as i, then the cell Π {a,b,c}
corresponds to the big triangle with (extended) edges a, b, c. Finally, note that a generic
pentagon in the plane belongs to exactly one of these three classes.
Unlike the nonnegative Grassmannian G≥0(k, n), there are
(n
3
)
(instead of just one!)
simplex-like top cells in G(1, n; 2), denoted Π{a,b,c} where{a, b, c}⊂{ 1, 2, . . . , n} is a 3-
element subset. As an example, with n = 5, the cells Π{1,2,5}, Π{2,3,5}, Π{3,4,5} correspond
to the diagrams shown in Figure 6.
A parametrization-independent formula for Ω(Π{a,b,c}) is given in [22]:
Ω(Π{a,b,c}) = d3n−7P∏n
i=1(i, i + 1, i + 2){X1, X2, X3} (7.60)
where the parentheses are deﬁned by (i, j, k) := det(Pi, Pj, Pk) for any (cyclically extended)
indices i, j, k, and {X1, X2, X3} is the area of the triangle with vertices X1, X2, X3 (see
dotted triangle in the polygon picture above),
{X1, X2, X3} = (X1, X2, X3)
[X1][X2][X3] (7.61)
where [X] denotes the component of X along C (i.e. Q∞· X), and the measure is deﬁned
by
d3n−7P =
⟨
Cdn−1C
⟩ ⟨
CDdn−3D1
⟩ ⟨
CDdn−3D2
⟩
(7.62)
with D1, D2 denoting the two rows of D.
Again, unlike the usual nonnegative Grassmannian, the 1-loop nonnegative Grassman-
nian G≥0(1, n; 2) is itself a polytope-like positive geometry. Indeed, it is shown in [22] that
G≥0(1, n; 2) can be triangulated by a collection of the top cells Π {a,b,c}. Namely, given a
usual triangulation ({a, b, c},{d, e, f}, . . .) of the n-gon (necessarily with n− 2 pieces), the
collection Π{a,b,c}, Π{d,e,f}, . . . gives a triangulation of G≥0(1, n; 2), and we have
Ω(G≥0(1, n; 2)) = Ω(Π{a,b,c}) + Ω(Π{d,e,f}) +··· . (7.63)
– 50 –

<!-- page 54 -->

Thus for example, we have
Ω(G≥0(1, 5; 2)) = Ω(Π{1,2,5}) + Ω(Π{2,3,5}) + Ω(Π{3,4,5}) (7.64)
Remarkably, the right hand side sums to the area of the pentagon with vertices P1, . . . , P5,
which be be seen pictorially.
More generally, a triangulation independent formula for Ω(G≥0(1, n; 2)) is given in [22]:
Ω(G≥0(1, n; 2)) = d3n−7P∏n
i=1(i, i + 1, i + 2)M(P ). (7.65)
whereM(P ) is the area of the n-gon with vertices P1, . . . , Pn. A simple formula for this
area is
M(P ) =
n−1∑
i=2
(1, i, i+1)
[1][i][i+1] (7.66)
Note that M(P ) is positive in G>0(1, n; 2), so that Ω( G≥0(1, n; 2)) is positively oriented
on G>0(1, n; 2). Thus G≥0(1, n; 2) is a positively convex geometry in the sense of Section
9.
7.2.6 An example of a Grassmann polytope
We now consider an example of a Grassmann polytope for k > 1 that is combinatorially
diﬀerent to the Amplituhedron. We set k = 2, n = 5, and m = 2. We take Z to be a
5× 4 matrix such that ⟨1234⟩ < 0 but ⟨1235⟩,⟨1245⟩,⟨1345⟩,⟨2345⟩ > 0. Explicitly, we
may gauge ﬁx
Z =


a−b c d
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1


where a, b, c, d > 0. The matrix
M =


1 0
0 1
−α β
−δ γ


with 0 < α, β, γ, δ ≪ 1, chosen to satisfy α/β < δ/γ < a/b shows that Z satisﬁes the
condition (6.31). Let A = Z(G≥0(2, 5)) denote the Grassmann polytope. Then for Y ∈A ,
the global inequalities⟨Y 14⟩≤ 0,⟨Y 15⟩≥ 0, and⟨Y 45⟩≥ 0 hold: for example, expanding
Y = C· Z, we get
⟨Y 14⟩ = (23)⟨2314⟩ + (25)⟨2514⟩ + (35)⟨3514⟩ = (23)⟨1234⟩− (25)⟨1245⟩− (35)⟨1345⟩≤ 0
where ( ab) denotes the minor of C ∈ G≥0(2, 5) at columns a, b. In contrast the tree
AmplituhedronA(2, 5, 2) where⟨1234⟩ > 0 satisﬁes⟨Y i, i+1⟩≥ 0 for all i.
– 51 –

<!-- page 55 -->

Our methods are not able to rigorously prove it, but a triangulation of this Grassmann
polytope appears to be given by the images under Z of the four 4-dimensional positroid
cells
[2][3][4][5] : (∗1) = 0, [1][2][3][5] : (∗4) = 0,
[1][2][3][4] : (∗5) = 0, [12][34][5] : (12) = (34) = 0 (7.67)
or of the two 4-dimensional positroid cells
[1][3][4][5] : (2∗) = 0, [1][23][45] : (23) = (45) = 0. (7.68)
Here, the notation [12][34][5] denotes the C matrices where columns C1 and C2 (resp. C3
and C4) are parallel, but C5 is linearly independent; this cell is cut out by the two equations
(12) = (34) = 0. Similarly, [2][3][4][5] denotes the C matrices where C1 = 0 and the other
columns have no relations; this cell is cut out by (12) = (13) = (14) = (15) = 0.
Thus the canonical rational function is given by
Ω(A) = [2, 3, 4; 2, 4, 5] + [1, 2, 3; 1, 3, 5] (7.69)
−[1, 2, 3; 1, 3, 4] + [5, 1, 2; 5, 3, 4] (7.70)
where the terms correspond respectively to the cells in the triangulation (7.67), and the
brackets are Kermit terms (see below (7.55)).
Alternatively, the canonical rational function can be given by two terms based on the
second triangulation (7.68):
Ω(A) = [1, 3, 4; 1, 4, 5] + [1, 2, 3; 1, 4, 5] (7.71)
This gives a remarkable algebraic equality between the two Kermit representations above,
which of course results from the phenomenon of triangulation independence of the form.
Note that the Kermit triangulation of the AmplituhedronA(2, 5, 2) diﬀers from (7.67)
and (7.68) by the cell C = [1][2][3][4], whose canonical form is given by the Kermit term
[1, 2, 3; 1, 3, 4]. The intuition for this is as follows. Starting with a positive Z matrix, we
may continuously vary the entries so that ⟨1234⟩ changes from positive to negative, but
all other maximal minors remain positive. At the moment when ⟨1234⟩ = 0, the image
of the cell C in G(2, 4) is no longer four-dimensional, but is three-dimensional, i.e., it
collapses. Changing ⟨1234⟩ from positive to negative thus changes whether C is used in a
triangulation. An analogous situation for a quadrilateral is illustrated in Figure 7.
Finally, despite not having proven the triangulations (7.67) and (7.68), our conﬁdence
in our claim comes from the fact that the resulting canonical form agrees numerically with
the iϵ contour representation discussed in Section 7.4.6.
7.3 Push-forwards
Recall from Heuristic 4.1 that for any morphism Φ : ( X, X≥0)→ (Y, Y≥0), we expect the
push-forward to preserve the canonical form:
Φ∗(Ω(X, X≥0)) = Ω(Y, Y≥0) (7.72)
– 52 –

<!-- page 56 -->

1
2 3
4 1
2
3
4 1
2
3
4
Figure 7: Changing ⟨123⟩ from > 0, to 0, then to < 0. The triangulation [124] + [234] is
changed to [213] + [124] + [234].
This procedure is useful for computing the canonical form of the image when the canonical
form of the domain is already known. However, ﬁnding morphisms of degree > 1 is a
diﬃcult challenge. We demonstrate a few non-trivial examples in this section.
7.3.1 Projective simplices
In this section we consider morphisms Φ : ( Pm, ∆)→ (X, X≥0) from projective simplices
to positive geometries X≥0. In most cases we will assume that ∆ = ∆ m is the standard
simplex, since they are isomorphic.
We begin with morphisms Φ : (Pm, ∆m)→ (X, X≥0) of degree one, in which case X≥0
is ∆−like (as deﬁned in Section 5.1), and its canonical form is given by:
Ω(X, X≥0) = Φ∗
( m∏
i=1
dαi
αi
)
(7.73)
where (1, α1, . . . , αm)∈ Pm. The simplest ∆-like positive geometry is a projective simplex:
Example 7.7. A projective simplex ∆⊂ Pm(R) is isomorphic to the standard simplex ∆ m
by the following map Φ : ( Pm, ∆m)→ (Pm, ∆):
Φ(α) =
m∑
i=0
αiZi+1 (7.74)
where Zi∈ Pm(R) are the vertices of ∆ for i = 1, . . . , m+1. As a matter of convention, the
projective variables and the vertices are indexed slightly diﬀerently. Note that the positive
part ∆m (i.e. αi > 0 for each i) is mapped diﬀeomorphically onto the interior of ∆.
The canonical form on ∆ is therefore
Ω(∆) = Φ∗
( m∏
i=1
dαi
αi
)
(7.75)
where we have made the “gauge choice” α0 = 1 as usual. Alternatively, pulling back the
form (5.4) onto ∆m gives the form on α-space.
The image of the hyperplane {αi = 0}⊂ Pm intersects ∆ along the facet opposite the
vertex Zi+1. Taking the residue of Ω(∆ m) along αi = 0 before pushing forward gives the
canonical form of that facet. We note that the pole for localizing on the facet opposite Z1
is hidden, as explained in Section 5.1.
– 53 –

<!-- page 57 -->

We now consider higher degree morphisms Φ : ( Pm, ∆m)→ (X, X≥0). Let us assume
for the moment that X = Pm. We now provide a general analytic argument for why the
push-forward should have no poles on X>0. The behavior of the push-forward near the
boundary of X≥0 is more subtle and will be discussed subsequently on a case-by-case basis.
Suppose the map is given by α↦→ Φ(α) and let β0 be a point in X>0. Furthermore,
assume if possible that the push-forward has a singularity atβ0. It follows that the Jacobian
J(α) of Φ(α) must vanish at some point α0 for which Φ(α0) = β0. Let β = Φ(α) which we
expand near the critical point.
β = Φ(α0) + λ
∑
i
ϵi
∂Φ(α0)
∂αi
+ 1
2 λ2 ∑
i,j
ϵiϵj
∂2Φ(α0)
∂αi∂αj
+ O(λ3) (7.76)
where we have set α = α0 + λϵ with λ a small parameter and ϵ a constant vector. Since
the Jacobian vanishes at α0, a generic point β in a small neighborhood of β0 cannot be
approximated by the linear term. However, unless the quadratic term degenerates, β can
be approximated quadratically by choosing ϵ so that the ﬁrst variation vanishes. Namely,
∑
a
ϵi
∂Φ(α0)
∂αi
= 0 (7.77)
It follows that the variation is even in λ, so there are two roots λ± (corresponding to
points α±, respectively) that approximate β, with λ+ =−λ−. Since the Jacobian is clearly
linear in λ for small variations near α0, therefore J(α+) = −J(α−) + O(λ2
−). Since the
push-forward is a sum of 1 /J(α)∼ 1/λ over all the roots, the roots corresponding to α±
therefore cancel in the limit β→ β0, and there is no pole.
We now show a few examples of higher degree push-forwards, beginning with self-
morphisms of the standard simplex.
Example 7.8. Let Φ : (Pm, ∆m)→ (Pm, ∆m) be a morphism of the standard simplex with
itself, deﬁned by
Φ(1, α1, . . . , αm) = (1 , β1, ..., βm) (7.78)
βj =
m∏
i=1
αaij
i (7.79)
where aij is an invertible integer matrix. We assume the determinant is positive so that
the map is orientation preserving. While this map is a self-diﬀeomorphism of Int(∆ m), it
is not necessarily one-to-one on Pm. The push-forward gives
Φ∗
( m∏
i=1
dαi
αi
)
=
∑
roots
dmβ
∂(β1...βm)
∂(α1...αm)
∏m
i=1 αi
= deg(Φ)
det(aij)
m∏
j=1
dβj
βj
(7.80)
where deg(Φ) is the number of roots, and we have substituted the Jacobian:
∂(β1 . . . βm)
∂(α1 . . . αm) = det(aij)
∏m
j=1 βj
∏m
i=1 αi
(7.81)
– 54 –

<!-- page 58 -->

It is easy to see that the degree of Φ must be | det(aij)|: after an integral change of basis,
the matrix (aij) can be put into Smith normal form, that is, made diagonal. For a diagonal
matrix (aij) it is clear that the degree of Φ is simply the product of diagonal entries. Thus
(7.80) veriﬁes Heuristic 4.1 in this case.
By contrast, we note that the pull-back along Φ gives Φ ∗(Ω(∆m)) = det( aij)Ω(∆m),
which does not preserve leading residues.
The next few examples explore the push-forward in one dimension. They are all
applications of Cauchy’s theorem in disguise.
Example 7.9. A simple non-trivial example is a quadratic push-forward Φ : ∆1→ ∆1 given
by Φ(1, α) = (1, aα2 +2 bα) for some real constants a > 0; b≥ 0. The assumptions suﬃce to
make Φ a self-morphism of ∆ 1. Setting (1 , β) = Φ(1, α) we get two roots α± from solving
a quadratic equation. The push-forward is therefore
Φ∗(d log α) =
∑
±
d log (α±) =
∑
±
d log
(
−b±
√
b2 + aβ
a
)
(7.82)
Since we are summing over roots, a standard Galois theory argument implies that the
result should be rational. Indeed, the square-root disappears, and direct computation
gives Φ∗(d log α) = d log β.
We can also do the sum without directly solving the quadratic equation. The result
should only depend on the sum and product of the roots x±, since the result must be a
rational function.
Φ∗(d log α) =
∑
±
dβ
α±
(
dβ
dα
)
±
=
∑
±
1
2α±(aα± + b) (7.83)
Substituting α±(aα± + b) = β− bα±, which comes from the original equation, we get
f∗(d log α) =
∑
±
1
2(β− bα±) = 2β− b(α+ + α−)
2(β2− bβ(α+ + α−) + b2α+α−) (7.84)
We now use the identities α+ + α− =−2b/a and α+α− =−β/a, which give the desired
result Φ∗(d log α) = d log β.
Example 7.10. We now go ahead and tackle the same example for a polynomial of arbitrary
degree. Suppose Φ is a self-morphism of ∆1 given by β = f(α) = αn+an−1αn−1+. . .+a1α.
We ﬁrst deﬁne the holomorphic function
g(α) = 1
α(f(α)− β) (7.85)
which has no pole at inﬁnity since f(α) is at least of degree one. The sum over all the
residues of the function is therefore zero by Cauchy’s theorem. It follows that
− 1
β +
∑
i
1
αif′(αi) = 0 (7.86)
– 55 –

<!-- page 59 -->

where we sum over all the roots αi of f(α) = β. Therefore,
Φ∗(d log α) =
∑
i
dβ
αif′(αi) = d log β (7.87)
Finally, we consider a simple but instructive push-forward of inﬁnite degree.
Example 7.11. Consider the map Φ : ( P1, [−π/2, π/2])→ (P1, [−1, 1]) between two closed
line segments given by:
Φ(1, θ) = (1, sin θ) (7.88)
While this map is not rational, we can nevertheless verify Heuristic 4.1 for Φ by explicit
computation. For any point (1, sin θ) in the image, there are inﬁnitely many roots of (7.88)
given by θn := θ + 2πn and θ′
n :=−θ + π(2n + 1) for n∈ Z. It is easy to show that both
sets of roots contribute the same amount to the push-forward, so we will just sum over θn
twice:
Φ∗
( πdθ
(π/2− θ)(θ + π/2)
)
= 2
∑
n∈Z
πdx
(π/2− θn)(θn + π/2) cosθn
= 2 dx
cos2 θ (7.89)
= 2dx
(1− x)(x + 1) (7.90)
which of course is the canonical form of [ −1, 1]. The inﬁnite sum can be computed by an
application of Cauchy’s theorem.
We note here that our deﬁnition (4.1) of the push-forward only allows ﬁnite degree maps
while Φ is of inﬁnite degree. Nonetheless, it appears that Heuristic 4.1 still holds when
the push-forward is an absolutely convergent series like (7.89). We stress that some push-
forwards give conditionally convergent series, such as the morphism ( P1, ∆1)→ (P1, [0, 1])
given by (1 , x)→ (1, e−x), in which case the push-forward is ill-deﬁned since there is no
canonical order in which to sum the roots.
7.3.2 Algebraic moment map and an algebraic analogue of the
Duistermaat-Heckman measure
Recall from Section 5.6 that toric varieties X(z) are positive geometries. We now show
how the canonical form of a polytope A = Conv(Z) can be obtained as the push-forward
of the canonical form of a toric variety, establishing an instance of Heuristic 4.1.
Associated to the torus action of T on X(z) is a moment map µ : X(z)→ Pm(R)
X(z)∋ (C1 :··· : Cn)↦−→
n∑
i=1
|Ci|2zi (7.91)
which is an important object in symplectic geometry. The image µ(X(z)) is the polytope
A(z)∈ Pm with vertices z1, . . . , zn.
Now, let us suppose we have a polytope A = Conv(Z) with vertices Z1, . . . , Zn such
that Z and z have the same “shape”. Namely, we insist that the determinants
⟨Zi0··· Zim⟩ and⟨zi0··· zim⟩ have the same sign (7.92)
– 56 –

<!-- page 60 -->

for all 1≤ i0, i1, . . . , im≤ n. Here, two real numbers have the same sign if they are both
positive, both negative or both zero. In other words, we ask that the vector conﬁgurations
Z and z have the same oriented matroid (see Appendix I). We caution that the integer
matrix z may not exist if Z is not “realizable over the rationals”.
Some basic terminology concerning oriented matroids is recalled in Appendix I. We
then have the (rational) linear map Z : X(z)→ Pm
X(z)∋ (C1 :··· : Cn)↦−→
n∑
i=1
CiZi. (7.93)
When Z = z, this map is called the algebraic moment map [13, 14]. Note that the moment
map has image in a real projective space but the algebraic moment map has image in a
complex projective space. We shall show in Section E that the image Z(X(z)≥0) of the
nonnegative part is the polytope A.
Suppose Y ∈ Pm. Then the inverse image of Y under the map Z is a linear slice
LY⊂ Pn−1 of dimension n−1− m. For a typical Y , the slice LY intersects X(z) in ﬁnitely
many points and we have the elegant equality
#|LY∩ X(z)| = m!· volume ofA(z). (7.94)
Here the volume of A(z) is taken with respect to the lattice generated by the vectors
z1, . . . , zn, so that the unit cube in this lattice has volume 1. In geometric language, (7.94)
states that the degree of X(z) is equal to m! times the volume of A(z).
When X(z) is a smooth complex projective variety, it is also a symplectic manifold.
In this case it has a real 2 m-form ω (not meromorphic!), called its symplectic volume. The
Duistermaat-Heckman measure is the push-forward µ∗ω on Pm(R), where ω is thought of
as a measure on X(z). Identifying A(z) with a polytope inside Rm, a basic result states
that µ∗ω is equal to the standard Lebesgue measure inside the polytope A(z), and is zero
outside.
We may replace the moment map µ by the linear map Z, and the symplectic volume
ω by our canonical holomorphic form Ω( X(z)≥0) from Section 5.6. The crucial result is
the following.
Theorem 7.12. Assume that z and Z have the same oriented matroids and that z is
graded. Then Z∗(Ω(X(z)≥0)) = Ω(A) is the canonical form of the polytope A = Conv(Z).
We remark that the graded condition (5.42) is a mild condition: since Z satisﬁes the
condition (6.2), it follows from Proposition I.1 that z does as well. Thus the vectors zi can
be scaled by positive integers until the set {z1, . . . , zn} is graded (5.42).
Note that in Theorem 7.12 we do not need to assume that X(z) is projectively normal.
Theorem 7.12 is proved in Appendix H. We sketch the main idea. Both (X(z), X(z)≥0)
and (Pm,A) are positive geometries. The condition that z and Z have the same oriented
matroid implies that the polytopes A(z) and A have the same combinatorial structure.
Thus the axioms (P1) and (P2) for the two positive geometries have the same recursive
structure. We prove the equality Z∗(Ω(X(z)≥0)) = Ω(A) by induction, assuming that the
– 57 –

<!-- page 61 -->

equality is already known for all the facets of A. At the heart of the inductive step is the
fact that taking push-forwards and taking residues of meromorphic forms are commuting
operations.
7.3.3 Projective polytopes from Newton polytopes
In this section we discuss morphisms from ( Pm, ∆m) to convex polytopes ( Pm,A) and
their push-forwards. Our main results here overlap with results from our discussion on
toric varieties in Section 7.3.2. However, our intention here is to provide a self-contained
discussion. Our focus here is also more geometric in nature, emphasizing the fact that any
such morphism restricts to a diﬀeomorphism Int(∆ m)→ Int(A).
Now let A⊂ Pm be a convex polytope in projective space with vertices Zi for i =
1, . . . , n. Let z1, z2, . . . , zn∈ Zm+1 be an integer matrix with the same oriented matroid as
Z1, . . . , Zn, that is, satisfying (7.92).
For simplicity we now assume that zi = (1, z′
i) = (1 , z′
1i, z′
2i, . . . , z′
mi) (see Section 5.6
for how to relax this condition).
Let us deﬁne a rational map Φ : ( Pm, ∆m)→ (Pm,A) given by:
Φ(X) =
∑
i
Ci(X)Zi (7.95)
Ci(X) := Xzi := Xz′
1i
1 Xz′
2i
2 ··· X
z′
m,i
m (7.96)
where (1, X)∈ Pm. This is called the Newton polytope map and the polytope with integer
vertices zi is called the Newton polytope.
We make two major claims in this section. The ﬁrst is the following:
Claim 1: The map Φ is a morphism provided that (7.92) holds. (7.97)
That is, it restricts to a diﬀeomorphism on Int(∆m)→ Int(A).
This is a non-trivial fact for which we provide two proofs in Appendix E. At the heart
of Claim (7.97) is that the Jacobian of Φ is uniformly positive on Int(∆ m):
J(Φ) =
∑
1≤i0<···<im≤n
Ci0··· Cim⟨zi0··· zim⟩⟨ Zi0··· Zim⟩ (7.98)
where J(Φ) denotes the Jacobian of Φ with respect to ui := log( Xi), which is clearly
positive provided that zi and Zi have the same oriented matroid (see (7.92)). While this
is only a necessary condition for Claim (7.97), it is nevertheless the key to proving it. We
provide a graphical example of the diﬀeomorphism for the pentagon in Figure 8.
This establishes the way to our second claim, which is an instance of Heuristic 4.1:
Claim 2: The canonical form of the polytope is given by the push-forward:
Ω(A) = Φ∗
( dmX∏m
a=1 Xa
)
(7.99)
Equation (7.99) follows from Theorem 7.12. To see this, note that in (5.50), we have
ΩS = ∏m
i=1 dXi/Xi and ΩT = ΩX(z) as meromorphic forms. Thus (7.99) follows from (5.50)
– 58 –

<!-- page 62 -->

0 1 2
0
1
2
z1
z2
-1.0 -0.5 0.0 0.5 1.0
-1.0
-0.5
0.0
0.5
1.0
Y 1
Y 2
Figure 8 : A Newton pentagon (left) with vertices z′ = ((0 , 0), (1, 0), (2, 1), (1, 2), (0, 1))
and the image of the corresponding diﬀeomorphism Φ( X) (right). The dark lines in the
interior of the pentagon (right) denote lines of constantX1 or X2. While the two pentagons
are not identical as sets, they do have the same oriented matroid.
and Theorem 7.12. We provide an alternative analytic argument avoiding toric varieties in
Section 7.3.4 by directing manipulating the sum-over-roots procedure in the push-forward
computation.
For computational purposes, a more convenient way to express the (canonical rational
function of the) push-forward is the following integral formula:
Ω(A)(Y ) =
∫ dmX∏m
a=1 Xa
δm(Y ; Φ(X)) (7.100)
where for any two points Y, Y′ in projective space Pm, the integral
δm(Y, Y′) = 1
m!
∫ dρ
ρ δm+1(Y− ρY′) (7.101)
is the delta function with weights (−m−1, 0). Here the sum over pre-images appearing in
the push-forward is equivalent to the sum over solutions to the constraints imposed by the
delta functions. The relevant Jacobian factors are taken care of by the delta functions as
well. We treat the delta functions formally as an “analytic” object without taking absolute
values in the Jacobian factor, and we sum over all complex roots.
In most cases numerical methods are needed to compute the push-forward, which we
have done extensively as veriﬁcation of Claim (7.99). However, here we show a simple case
where the push-forward can be done by hand.
Example 7.13. Let us consider a quadrilateral A on the projective plane. By a convenient
gauge-ﬁxing, we will take the external data and Y to be of the form
Z =


1 0 0
0 1 0
0 0 1
a−1 b

 , Y = (y, 1, x) (7.102)
– 59 –

<!-- page 63 -->

We can trivially compute the canonical rational function by e.g. triangulation as
[123] + [134], and ﬁnding
Ω(A) = (ab + ax + by)
xy(a + y)(b + x) dxdy (7.103)
and we will now reproduce this result from the Newton polytope map (7.95), with the
Newton polytope being the square with vertices (1, 0), (1, 1), (0, 1), (0, 0), respectively. Thus
our map is
Y = Φ(X) = X1Z1 + X1X2Z2 + X2Z3 + Z4 =
( X1 + a
X1X2− 1 , 1, X2 + b
X1X2− 1
)
(7.104)
which are projective equalities. We must solve the equations
(X1X2− 1)y = X1 + a, (X1X2− 1)x = X2 + b (7.105)
We then have
d2X
X1X2
= dxdy× (X1X2− 1)2
X1X2(xX1 + yX2− 1) (7.106)
It therefore suﬃces to show that
∑
roots
(X1X2− 1)2
X1X2(xX1 + yX2− 1) = (ab + ax + by)
xy(a + y)(b + x) (7.107)
If we deﬁne ρ = ( X1X2− 1), then we have X1 = ρy− a, X2 = ρx− b and so ( ρ + 1) =
(ρy− a)(ρx− b). So ρ satisﬁes the quadratic equation
ρ2− (1 + ax + by)
xy ρ + ab− 1
xy = 0 (7.108)
which has two roots ρ±. Note that
xX1 + yX2− 1 = x(ρy− a) + y(ρx− b)− 1 = 2xy
(
ρ− 1
2
(1 + ax + by)
xy
)
(7.109)
Comparing with the quadratic equation for ρ, we can identify the term corresponding to
the sum of the roots ( ρ+ + ρ−), giving:
(xX1 + yX2− 1)± =±xy(ρ+− ρ−) (7.110)
Thus, the sum over roots becomes
1
xy(ρ+− ρ−)×
( ρ2
+
(ρ+y− a)(ρ+x− b)− ρ2
−
(ρ−y− a)(ρ−x− b)
)
= 1
xy
ab(ρ+ + ρ−)− ρ+ρ−(by + ax)
(ρ+ρ−y2− a(ρ+ + ρ−)y + a2)(ρ+ρ−x2− b(ρ+ + ρ−)x + b2) (7.111)
And reading oﬀ
ρ+ρ− = ab− 1
xy , ρ + + ρ− = 1 + ax + by
xy (7.112)
from the quadratic equation we ﬁnally ﬁnd that (7.111) equals
ab + ax + by
xy(a + y)(b + x) (7.113)
as expected.
– 60 –

<!-- page 64 -->

7.3.4 Recursive properties of the Newton polytope map
We now derive the push-forward identity (7.99) for the Newton polytope by explicitly
manipulating the push-forward computation and applying induction on dimension. In
fact, we will derive a more general version for lower dimensional polytopes in Pm(R). The
statement is the following:
Consider the variety H⊂ Pm deﬁned by linear equations Y· H1, . . . , Y· Hs = 0 for
some dual vectors H1, . . . , Hs∈ Pm(R) with Y ∈ Pm. Let A denote a convex polytope in
H(R) of dimension D = m−s with vertices Z1, . . . , Zn. Let Φ : ( PD, ∆D)→ (H,A) be a
morphism deﬁned by a Newton polytope with vertices zi = (1, z′
i)∈ RD+1. Furthermore,
we assume that A and the Newton polytope have the same oriented matroid. Namely,
there exist constant vectors K1, . . . , Ks∈ Pm(R) such that
⟨K1··· KsZi0··· ZiD⟩ and⟨zi0··· ziD⟩ have the same sign (7.114)
for any set of indices 1 ≤ i0, . . . , iD≤ n.
The D = 0 case is trivial. Now assume D > 0. Let B denote a facet of A with
vertices Zj1, . . . , Zjp, and let B denote the corresponding facet of the Newton polytope.
We now argue that there exists a change of variables (X1, . . . , XD)→ (U1, . . . , UD) given by
Xb = ∏D
a=1 Uaαab for some invertible integer matrix αab that has the following properties:
(Note that we deﬁne Φ′(U) := Φ(ψ(U)) with X := ψ(U))
• The map U→ X is a self-morphism of ∆D which may be of degree > 1. In particular,
it is a self-diﬀeomorphism of Int(∆ D).
• The restriction of Φ′ to UD = 0 is a Newton polytope map ∆D−1→B whose Newton
polytope has the same shape as B.
We construct the change of variables as follows. Let us begin by considering the matrix
formed by column vectors ( zj1, . . . , zjD , zj) where the ﬁrst D columns are vertices of B,
while zj is any vertex of the Newton polytope away from the facet. Let α := (αab) be the
inverse of the matrix, which has only rational components. Finally, let us rescale the rows
of αab (indexed by a) by positive integers so that all its components are integral. This
provides the change of variables X→ U.
Let us redeﬁne zi for every i to be the vertex of the Newton polytope with respect to
U, which again has the same oriented matroid as A. In particular, the matrix of column
vectors ( zj1, . . . , zjD , zj) is identity. Since every vertex of B is a linear combination of
zj1, . . . , zjD, it must therefore have zero as its last component. Furthermore, since every
other vertex of the Newton polytope is a linear combination of zj1, . . . , zjD , zj with positive
coeﬃcient in zj, its last component must be positive. Geometrically, this means that the
UD = 0 limit is mapped to the facet B by Φ′.
Now, let Ψ : ∆D−1→B denote the map Φ′ restricted to UD = 0, and let wj1, . . . , wjp∈
RD denote the vertices of the Newton polytope of Ψ, which are equivalently the vectors
zj1, . . . , zjp, respectively, with the last component removed. It is straightforward to check
that the Newton polytope of Ψ has the same oriented matroid as B, so our induction
hypothesis can be applied to Ψ.
– 61 –

<!-- page 65 -->

We now argue that the push-forward by Φ ′ has a pole at the boundary B with the
expected residue Ω(B). Let Y = Φ′(U). The main strategy is to observe that the roots
(U1, . . . , UD−1) are independent of UD nearB.
Indeed, at Y ∈B (i.e. UD = 0), the map becomes
Y = Cj1Zj1 +··· + CjpZjp (7.115)
which gives us a collection of roots ( U1, . . . , UD−1) independent of UD. It follows therefore
from the induction hypothesis that
∑
roots (U1,...,UD−1)
dD−1U
U1··· UD−1
= Ψ∗
( dD−1U
U1··· UD−1
)
= Ω(B) (7.116)
Moreover, the roots UD are given by the equation
⟨K1 . . . KsY j1 . . . jD⟩∼ Uq
DF (U1, . . . , UD−1) (7.117)
for some function F independent of UD and some exponent q. Hence,
∑
roots UD
dUD
UD
= d log⟨K1 . . . KsY j1 . . . jD⟩ +··· (7.118)
where the··· denotes term proportional to dU1, . . . , dUD−1.
It follows that in the limit Y →B , we have
∑
roots
dDU
U1··· UD
=

 ∑
roots (U1,...,UD−1)
dD−1U
U1··· UD−1



 ∑
roots UD
dUD
UD

 +··· (7.119)
= Ψ∗
( dD−1U
U1··· UD−1
)
d log⟨K1 . . . KsY j1 . . . jD⟩ +··· (7.120)
= Ω(B) d log⟨K1 . . . KsY j1 . . . jD⟩ +··· (7.121)
where··· denotes terms smooth in the limit, and we have applied (7.118) and (7.116).
This of course is the expected pole and residue.
Furthermore, by the discussion in Section 7.3.1, we ﬁnd that there are no poles on the
interior ofA.
Finally, we can re-express our result as a push-forward from X-space by the following:
Φ∗
( dDX
X1··· XD
)
= Φ′
∗
( dDU
U1··· UD
)
(7.122)
since Φ′
∗ = Φ∗◦ ψ∗, and ψ∗ pushes the standard simplex form on U to the same form on
X (see (7.8)).
– 62 –

<!-- page 66 -->

7.3.5 Newton polytopes from constraints
We now provide an alternative way of thinking about equation (7.100) as constraints on C
space. Most of the notation in this section is borrowed from Section 7.4.6.
The map X→ Ci(X) parametrizes a subset of the projective space C∈ Pn−1. This
subset can be equivalently “cut out” using constraints on the Ci variables.
n∏
i=1
Cwpi
i = 1 (7.123)
with one constraint for each value of p = 1 , ..., n−m−1, where wpi is a constant integer
matrix to be determined. For the constraint to be well-deﬁned projectively, we must have∑
i wpi = 0 for each p.
Substituting the parametrization Ci(X) = ∏m
a=0 Xzai
a , we ﬁnd that
n∑
i=1
zaiwpi = 0 (7.124)
for each a, p.
We can now replace the push-forward formula (7.100) by an integral over all Ci with
imposed constraints.
Ω(A) = 1
m!
∫ dnC∏n
j=1 Cj


n−m−1∏
p=1
δ
(
1−
n∏
i=1
Cwpi
i
)
 δm+1
(
Y−
n∑
i=1
CiZi
)
(7.125)
Note that each delta function in the square brackets imposes one constraint, and in
the absence of constraints we arrive at the familiar cyclic measure on C space.
It is evident that explicitly summing over the roots of these polynomial equations
will become prohibitively more diﬃcult for large n. But of course there is a standard
approach to summing rational functions of roots of polynomial equations, making use of the
global residue theorem [31] which we review in Appendix F. This method has been applied
ubiquitously in the literature on scattering amplitudes, from the earliest understanding of
the relations between leading singularities and the connection between the twistor-string
and Grassmannian formalisms [1, 32, 33], to the recent application to scattering equations
[34–37]. Appropriately taking care of some minor subtleties, the global residue theorem also
works for our problem, naturally connecting the Newton polytope formula to triangulations
of the polytope.
We now provide explicit computations for the quadrilateral and the pentagon with
constraints.
Example 7.14. For m = 2, n = 4, there is only one constraint given by
wp := w1p = (Q1,−Q2, Q3,−Q4) (7.126)
for some integers Qi > 0, i = 1, 2, 3, 4. The positivity of the Qi variables is imposed by the
positivity of the Newton polytope.
– 63 –

<!-- page 67 -->

Now recall that delta functions can be identiﬁed with residues in the following manner:
∫
dz δ (z)f(z) = Resz→0
(1
z f(z)
)
= f(0) (7.127)
We will therefore think of the delta function constraints appearing in the square brackets
Eq. (7.125) as residues, and apply the global residue theorem F.1.
We have
Ω(A) = 1
2
∫ d4C
C1C2C3C4
[
CQ2
2 CQ4
4
CQ2
2 CQ4
4 − CQ1
1 CQ3
3
]
δ3
(
Y−
4∑
i=1
CiZi
)
(7.128)
Here we have underlined the pole corresponding to the constraint. The reader should
imagine that the three remaining constraints (i.e. Y = C· Z) also appear as poles, but for
notational convenience we will simply write them as delta functions. For higher n, we will
have additional constraints, and hence additional underlined polynomials.
Now (7.128) instructs us to sum over all global residues where the four constraints
vanish, which in general is very hard to compute by explicit summation. However, the
global residue theorem vastly simpliﬁes the problem. Note that there are eight poles in
our integral (i.e. four constraints plus the four cyclic factors Ci). In order to apply the
theorem, we will need to group the poles into four groups. Let us group the cyclic factors
with the underlined constraint, and each of the delta function constraints forms its own
group. It follows therefore that
Ω(A) =−1
2
4∑
i=1
∫ d4C
C1 . . . Ci . . . C4
[
CQ2
2 CQ4
4
CQ2
2 CQ4
4 − CQ1
1 CQ3
3
]
δ3
(
Y−
4∑
i=1
CiZi
)
(7.129)
This gives us four residues corresponding to Ci→ 0 for each i. Now the positivitiy of
Qi > 0 comes into play. Clearly, the C2, C4→ 0 residues vanish due to the appearance
of CQ2
2 CQ4
4 in the numerator. However, for the C1, C3→ 0 residues, the square bracket
becomes unity, and the result is equivalent to Res(1), Res(3), respectively, as deﬁned in
Eq. 7.232. It follows that
Ω(A) = Res(1) + Res(3) = [234] + [124] (7.130)
Alternatively, we could have assumed Qi < 0 for each i. This would have given us another
triangulation:
Ω(A) = Res(2) + Res(4) = [134] + [123] (7.131)
We note that our technique can be applied to convex cyclic Newton polytopes for any
m, provided that n = m+2. The constraint matrix is given by a sequence with alternating
signs.
wp = (Q1,−Q2, Q3,−Q4, ...,(−1)m+1Qm+2) (7.132)
– 64 –

<!-- page 68 -->

where the constants Qi are either all positive or all negative. If Qi > 0, then the canonical
rational function becomes
Ω(A) =
∑
i odd
Res(i) (7.133)
And for Qi < 0, we get
Ω(A) =
∑
i even
Res(i) (7.134)
Example 7.15. Let us move on to the n = 5, m = 2 pentagonA with the Newton polytope
having vertices (0, 0), (1, 0), (2, 1), (1, 2), (0, 1). Then the Newton polytope formula becomes
Ω(A) =
∫
dC1dC2dC3dC4dC5
1
C1C2C5
C2
1
C2
1 C3− C2
2 C5
C2
1
C2
1 C4− C2C2
5
δ3(Y− C· Z) (7.135)
Now on the support of the delta function we have a two-dimensional integral, and the
underline tells us to sum over all the roots of the two polynomials with C1̸= 0.
In order to use the global residue theorem for our pentagon problem, we group the
denominator factors into ﬁve groups, given by the three delta function constraints and
f1, f2:
f1 = C2C5(C2
1 C3− C2
2 C5), f 2 = (C2
1 C4− C2C2
5), g = C3
1 (7.136)
where g is the numerator.
The roots of f1 = 0, f2 = 0 certainly include the “complicated” solutions of the Newton
polytope problem, where C1̸= 0, and at these the residues are well-deﬁned. The only
subtlety is that we have other roots, where ( C2, C1) = (0, 0), and where ( C5, C1) = (0, 0).
These zeros are quite degenerate; the Jacobian factor vanishes and the residue is not directly
well-deﬁned.
We can deal with this by slightly deforming the functions; we will take instead
f1 = C2C5((C2
1− ϵ2
3)C3− C2
2 C5), f 2 = ((C2
1− ϵ2
4)C4− C2C2
5), g = C3
1 (7.137)
where we will imagine that both ϵ3, ϵ4 are eventually sent to zero. The singular zeros we
previously found, with ( C2, C1) = (0, 0) and with ( C5, C1) = (0, 0) will now be split into a
number of non-degenerate solutions, and we will be able to use the global residue theorem.
Let us see where these deformed zeros are located. For f1 = 0, we can set either
C2 = 0, C5 = 0 or ( C2
1− ϵ2
3)C3− C2
2 C5 = 0. The ﬁrst two cases are of course trivial; the
roots and corresponding residues, as we take ϵ3, ϵ4→ 0, are
C2 = 0, C 4 = 0, Res = [135] (7.138)
C5 = 0, C 4 = 0, Res = [123] (7.139)
C2 = 0, C 1 =±ϵ4,
∑
±
Res = ϵ2
4
ϵ2
4− ϵ2
3
[345] (7.140)
C5 = 0, C 1 =±ϵ4,
∑
±
Res = ϵ2
4
ϵ2
4− ϵ2
3
[234] (7.141)
– 65 –

<!-- page 69 -->

Note interestingly that the residues for the last two cases depend on the ratio ϵ3/ϵ4 even
as ϵ3,4→ 0. We next have to look at the solutions to
(C2
1− ϵ2
3)C3− C2
2 C5 = 0, (C2
1− ϵ2
4)C4− C2C2
5 = 0 (7.142)
We are interested in the solutions where C1 is close to zero; which here means that either
C1 is close to ϵ3 or C1 is close to ϵ4. More formally, we can set ϵ3,4 = ϵE3,4 and ask what
the solutions look like as ϵ→ 0 with E3,4 ﬁxed. It is then easy to see that if C2
1→ ϵ2
3, we
must have that C5 is non-zero and C2→ (ϵ2
3− ϵ2
4)C4/C2
5, while if C2
1→ ϵ2
4, we must have
that C2 is non-zero and C5→ (ϵ2
4− ϵ2
3)C3/C2
2. It is trivial to compute the residues in these
cases, and we ﬁnd
C1→± ϵ3, C 2→ (ϵ2
3− ϵ2
4)C4/C2
5 ,
∑
±
Res = ϵ2
3
ϵ2
4− ϵ2
3
[345] (7.143)
C1→± ϵ4, C 5→ (ϵ2
4− ϵ2
3)C3/C2
2 ,
∑
±
Res = ϵ2
4
ϵ2
3− ϵ2
4
[234] (7.144)
By the global residue theorem, the sum over all these residues gives us Ω (A), so we ﬁnd
Ω(A) = [123] + [135] + [345]
( ϵ2
4
ϵ2
4− ϵ2
3
− ϵ2
3
ϵ2
4− ϵ2
3
)
+ [234]
( ϵ2
4
ϵ2
4− ϵ2
3
− ϵ2
4
ϵ2
4− ϵ2
3
)
(7.145)
= [123] + [135] + [345] (7.146)
which is a standard triangulation of the pentagon.
It would be interesting to carry out the analog of this analysis for the general Newton
polytope expression associated with the canonical form of any polytope. The same resolu-
tion of the the singular roots will clearly be needed, and it will be interesting to see how
and which natural class of triangulations of the polytope emerges in this way.
7.3.6 Generalized polytopes on the projective plane
We now consider push-forwards onto generalized polytopes on the projective plane, partic-
ularly the pizza slice.
Example 7.16. We construct the canonical form of the pizza slice T (θ1, θ2) from Example
6.1 via push-forward. Let z1 = tan( θ1/2) and z2 = tan( θ2/2). Consider the morphism
Φ : (P1× P1, [z1, z2]× [0,∞])→T (θ1, θ2) given by:
(1, x, y) = Φ(z, t) :=
(
1, 1− z2
(1 + z2) , 2z
(1 + z2)
)
+ tZ∗ (7.147)
=
(
1, 1− z2
(1 + z2)(1 + t) , 2z
(1 + z2)(1 + t)
)
(7.148)
where z, t are coordinates on the two P1’s, and ZI
∗ := (1, 0, 0) is the “tip” of the pizza. Note
that the equations are projective. As z varies in [ z1, z2], the point ( 1−z2
(1+z2) , 2z
(1+z2)) sweeps
out the circular arc (cos( θ), sin(θ)) where θ varies from θ1 to θ2. The variable t acts like a
radial coordinate that goes from 0 (the unit arc) to ∞ (the tip).
– 66 –

<!-- page 70 -->

For a generic point (x, y) there are two roots in Φ−1(1, x, y), say (z, t) and (−1/z,−t−
2). We compute
Φ∗
( (z2− z1)
(z2− z)(z− z1) dz 1
t dt
)
(7.149)
= (1 + t)3
2
((1 + z2)(z2− z1)
(z2− z)(z− z1)
1
t− (1 + z2)(z2− z1)
(zz2 + 1)(1 + zz1)
1
(t + 2)
)
dxdy (7.150)
We have the two identities
1
2
(1 + z2)(z2− z1)
(z2− z)(z− z1) = sin(θ2− θ1) + sin(θ− θ1) + sin(θ2− θ)
2 sin(θ− θ1) sin(θ2− θ) (7.151)
−1
2
(1 + z2)(z2− z1)
(zz2 + 1)(1 + zz1) = sin(θ2− θ1)− sin(θ− θ1)− sin(θ2− θ)
2 sin(θ− θ1) sin(θ2− θ) (7.152)
which are related by a shift θ→ θ + π. Substituting into (7.150) and using 1 − x2− y2 =
t(2 + t)/(1 + t)2 gives
[sin(θ2− θ1) + (−x sin θ1 + y cos θ1) + (x sin θ2− y cos θ2)]
(1− x2− y2)(−x sin θ1 + y cos θ1)(x sin θ2− y cos θ2) dxdy (7.153)
which of course is the canonical form Ω( T (θ1, θ2)). Note that sine summation formulas
were used to get the denominator factors.
The push-forward calculation can also be done with more intuitive angular coordinates,
using an inﬁnite degree map similar to Example 7.11. We take the map Ψ : (P1×P1, [θ1, θ2]×
[0,∞])→T (θ1, θ2) given by:
(1, x, y) = Ψ(1, θ, t) := (1, cos θ, sin θ) + tZ∗ =
(
1, cos θ
1 + t , sin θ
1 + t
)
(7.154)
The variable θ acts as an angular coordinate between θ1 and θ2. For any point ( x, y) =
(cos θ, sin θ)/(1+t), there are two sets of roots given by:
(θn, tn) = ( θ + 2πn, t) (7.155)
(θ′
n, t′
n) = ( θ + π(2n + 1),−t−2) (7.156)
where n∈ Z. Summing over all roots in the push-forward gives
Ψ∗
( (θ2− θ1)dθ
(θ2− θ)(θ− θ1)
dt
t
)
= (1 + t)3
t
∑
n∈Z
(θ2− θ1)
(θ2− θn)(θn− θ1) dxdy (7.157)
+(1 + t)3
t + 2
∑
n∈Z
(θ2− θ1)
(θ2− θ′n)(θ′n− θ1) dxdy (7.158)
Ignoring the rational t factors, the summations give:
∑
n∈Z
(θ2− θ1)
(θ2− θn)(θn− θ1) = sin(θ2− θ1) + sin(θ− θ1) + sin(θ2− θ)
2 sin(θ− θ1) sin(θ2− θ) (7.159)
∑
n∈Z
(θ2− θ1)
(θ2− θ′n)(θ′n− θ1) = sin(θ2− θ1)− sin(θ− θ1)− sin(θ2− θ)
2 sin(θ− θ1) sin(θ2− θ) (7.160)
– 67 –

<!-- page 71 -->

which are exactly (7.151) and (7.152). Thus we again obtain (7.153) as the canonical form
of the pizza slice. The summation identities (7.159) and (7.160) can also be interpreted
as the push-forward summation for the inﬁnite degree map φ : θ↦→ z = tan(θ/2), and we
have Ψ = Φ◦ (φ× id), where id : t↦→ t is the identity map on the t coordinate.
7.3.7 Amplituhedra
In this section, we conjecture that the Amplituhedron form (i.e. the canonical form of the
Amplituhedron) can be formulated as a push-forward from the standard simplex. While
this is nothing more than a direct application of our favorite Heuristic 4.1, we wish to
emphasize the important open problem of constructing morphisms needed for the push-
forward. In this section, we let A :=A(k, n, m; lL).
Conjecture 7.17. Given a morphism Φ : ∆D→A (k, n, m; lL) from positive coordinates
to the Amplituhedron, the Amplituhedron form is given by the push-forward
Ω(A(k, n, m; lL)) = Φ∗
( D∏
a=1
dXa
Xa
)
(7.161)
where D is the dimension of the Amplituhedron.
Before providing explicit examples, we reformulate our conjecture in terms of the
canonical rational function Ω(A)(Y) of the Amplituhedron (see (6.22) for the notation Y),
which was ﬁrst mentioned in 5.5 for the k = 1 Amplituhedron, and extended to the loop
Amplituhedron in Appendix C. We will also refer to Ω (A) as the amplitude, motivated
by the physical interpretation discussed in Sec 7.3.7. Keep in mind, of course, that the
physical interpretation only exists for the physical Amplituhedron, and for L > 0 the
canonical rational function is strictly speaking the L-loop integrand of the amplitude.
Conjecture 7.18. Given a morphism Φ : ∆D→A (k, n, m; lL) from positive coordinates
to the Amplituhedron, the amplitude is given by:
Ω(A)(Y) =
∫ dDX∏D
a=1 Xa
δD(Y; Φ(X)) (7.162)
for any pointY∈A . For computational purposes,Y and Φ(X) are represented as matrices
modded out by a left group action, as discussed below (6.20).
The delta function δD(Y,Y′) is the unique (up to an overall normalization) delta func-
tion on G(k, k+m; lL) that is invariant under the group actionG(k; k) (deﬁned below 6.20)
onY′, and scales inversely as the measure (C.10) under the same group action on Y. The
inverted scaling ensures that the canonical form is locally invariant under the action.
Example 7.19. For k = 1 and m = 4, the physical tree AmplituhedronA is a convex cyclic
polytope with vertices Zi∈ P4(R). Morphisms Φ : ( P4, ∆4)→ (P4,A) are given by convex
cyclic Newton polytopes from (7.95), and the amplitude is given by:
Ω(A)(Y ) =
∫ d4X
X1X2X3X4
δ4(Y ; Φ(X)) (7.163)
where Y ∈ P4 and the delta function is given in (7.101) with m = 4.
– 68 –

<!-- page 72 -->

We now provide some examples for k = 2 , m = 2 , l = 2 , L = 0. While we do not
have a complete construction of such morphisms for all n, we did ﬁnd a few non-trivial
examples for small n. We stress that the existence of such morphisms is an absolutely
remarkable fact. We also speculate that a complete understanding of morphisms to the
tree Amplituhedron may provide insight on extending toric varieties to the Grassmannian,
as morphisms to the polytope were given by projective toric varieties.
Let us begin by clarifying the push-forward computation, which for the present case is
given by:
Ω(A) =
∫ d4X
X1X2X3X4
δ4(Y ; Φ(X)) (7.164)
where
δ4(Y ; Y′) = 1
4
∫ d2×2ρ
(det ρ)2 δ2×4(Y− ρ· Y′) (7.165)
is the delta function that imposes the constraint Y = Y′ for any pair of 2 × 4 matrices
Y, Y′, where the tilde indicates that the two sides are only equivalent up to an overall GL(2)
transformation. The ρ is a 2× 2 matrix that acts as a GL(2) transformation on Y′ from
the left, and the d2×2ρ/(det ρ)2 measure is GL(2) invariant in ρ both from the left and the
right. We see therefore that the delta function has GL(2) weights ( −4, 0) in ( Y, Y′), as
expected.
Example 7.20. Consider the Amplituhedron for ( k, m, n, l, L) = (2, 2, 4, 2, 0), which is sim-
ply
A ={C· Z∈ G(2, 4)| C∈ G≥0(2, 4)} (7.166)
where Z is a 4×4 matrix with positive determinant. Since Z is non-singular,A is isomorphic
to G≥0(2, 4). A (degree-one) morphism from ( P4, ∆4) to the Amplituhedron is therefore:
C(X) =
(
1 X1 0−X4
0 X2 1 X3
)
(7.167)
Φ(X) = C(X)· Z (7.168)
sending the interior Int(∆ 4) (where Xi > 0 for i = 1, 2, 3, 4) to the interior of the Ampli-
tuhedron.
Substituting into (7.164) gives:
Ω(A) = 1
4
⟨1234⟩2
⟨Y 12⟩⟨ Y 23⟩⟨ Y 34⟩⟨ Y 14⟩ (7.169)
Example 7.21. We now move on to the ﬁrst non-trivial example beyond the polytope.
Consider the same case as Example 7.20 but now with n = 5. The Amplituhedron is
A ={C· Z∈ G(2, 4)| C∈ G≥0(2, 5)} (7.170)
– 69 –

<!-- page 73 -->

with all the maximal ordered minors of Z positive. The interior of this Amplituhedron
has no obvious diﬀeomorphisms with the interior Int(∆ 4) of the 4-simplex. But we have
managed to stumble across a few lucky guesses, such as the following:
C(X) =
(
1 X1 X1X2 X2 0
0 X1X3 X1X2(X3+X3X4) X2(X3+X3X4+X4) 1
)
(7.171)
Φ(X) = C(X)· Z (7.172)
for X1, X2, X3, X4 > 0. We have veriﬁed numerically that the push-forward given by (7.171)
gives the correct 5-point 1-loop integrand. A careful analytic argument can be provided to
prove that the restriction Int(∆ 4) ∼−→Int(A) is indeed a diﬀeomorphism.
Example 7.22. We also provide an example for n = 6. The setup is the same as Example
7.21, with the C(X) matrix given by
C(X) =
(
X3
1 X2
2 X3+X2
1 X2
2 X3 X5
1 X2
2 X3X2
4 X3
1 X3X2
4 X1 0
−X4
1 X2
2 −X1X3 0 X2
1 X3X2
4 1+X2
1 X2
4 X5
1 X2
2 X2
4
)
(7.173)
The push-forward was veriﬁed numerically. We challenge the reader to prove that this map
restricts to a diﬀeomorphism Int(∆ 4) ∼−→Int(A).
7.4 Integral representations
We now present integral representations (e.g. volume integrals, contour integrals) of various
canonical forms.
7.4.1 Dual polytopes
Consider a convex polytope ( Pm,A) and a point Y not along any boundary component.
We argue that the canonical rational function Ω(A) at Y is given by the volume of the dual
polytopeA∗
Y (deﬁned in Section 6.1.3) under a Y -dependent measure. More precisely,
Ω(A)(Y ) = Vol (A∗
Y ) := 1
m!
∫
W∈A∗
Y
⟨W dmW⟩
(Y· W )m+1 (7.174)
In order for this integral to be well-deﬁned on projective space, the integrand must be
invariant underlocalGL(1) transformations W→ W′ = α(W )W , which we proved in (C.5).
Moreover, observe that by construction of A∗
Y , we have Y· W > 0 for every point W ∈
Int(A∗
Y ), which is important for the integral to converge. However, the overall sign of the
integral is dependent on the orientation of the dual. We say therefore that the volume is
signed.
Now let us prove this claim for simplices by explicit computation:
Example 7.23. Let Y ∈ Int(∆) for some simplex. The volume of the dual simplex ∆ ∗
Y
with vertices W1, . . . , Wm+1 (so that Y · Wi > 0 for each i) can be computed using a
Feynman parameter technique. Since the form is locally GL(1) invariant, we can gauge ﬁx
– 70 –

<!-- page 74 -->

the integration to W = W1 + α1W2 +··· + αmWm+1 and integrate over αi > 0. This gives
Vol (∆∗
Y ) =
∫ dmα⟨W1··· Wm+1⟩
((Y· W1) + α1(Y· W2) +··· + αm(Y· Wm+1))m+1 (7.175)
= ⟨W1··· Wm+1⟩
m!(Y· W1)··· (Y· Wm+1) (7.176)
agreeing with (5.7).
Note that the result is independent of the sign of the vertices Wi. If, for instance, we
move Y outside ∆ so that Y· W1 < 0 but Y· Wi > 0 for every i̸= 1, then we would have
needed to use−W1 in the integration, but the result would still have the same form.
We now argue that the formula holds for an arbitrary convex polytope based on three
observations:
• “Dualization of polytopes commutes with triangulation” (6.13). This means that
A =
∑
i
Ai ⇒ A ∗
Y =
∑
i
A∗
iY (7.177)
For triangulation by simplices, this formula is known as Filliman duality [38].
• The signed nature of the volume is crucial, because it implies triangulation indepen-
dence. This means that
A∗
Y =
∑
i
A∗
iY ⇒ Vol (A∗
Y ) =
∑
i
Vol (A∗
iY ) (7.178)
• The canonical rational function is triangulation independent (Section 3):
A =
∑
i
Ai ⇒ Ω(A) =
∑
i
Ω(Ai) (7.179)
Combining these three statements for a signed triangulation by simplicesAi = ∆i, it
follows that
Vol (A∗
Y ) =
∑
i
Vol (∆∗
iY ) =
∑
i
Ω(∆i) = Ω(A) (7.180)
which is the desired claim.
We have not given a proof of the ﬁrst observation (7.177). In Section 7.4.2 we will
give an independent proof of the volume formula (7.174). Then by the second and third
assumptions, we ﬁnd that Vol (A∗
Y ) = ∑
i Vol (A∗
iY ) for every Y , which implies thatA∗
Y =∑
iA∗
i , thus deriving (7.177). Alternatively, we can also say that the the volume formula
combined with the ﬁrst two assumptions implies the triangulation independence of the
canonical rational function.
We now wish to comment on the distinction between “physical” poles and “spurious”
poles (see Section 3.4) in the context of the volume formula, ﬁrst pointed out by Andrew
– 71 –

<!-- page 75 -->

Hodges as an interpretation of spurious poles appearing in BCFW recursion of NMHV tree
amplitudes [2].
Given a triangulation of A by polytopesAi with mutually non-overlapping interiors,
spurious poles appear along boundary components of the triangulating pieces that do not
belong to the boundary components of A. From the dual point of view, the duals A∗
iY
form an overlapping triangulation of A∗
Y , and a spurious pole corresponds to a subset
of volume terms Vol (A∗
iY ) going to inﬁnity individually, but whose sum remains ﬁnite.
Geometrically, the signed volumes overlap and cancel. More details are given in [2].
However, suppose instead that Y ∈ Int(A) and the duals A∗
iY have non-overlapping
interiors, then Vol (A∗
iY )≤ Vol (A∗
Y ). It follows that all the volume terms are ﬁnite on
Int(A), and there are no spurious poles. Of course, the sum is independent of X since the
integral is surface-independent. This is called a local triangulation. An example of a local
triangulation of cyclic polytopes in P4(R) is given in [39].
On a ﬁnal note, we argue that these simplicial volumes are identical to Feynman
parameters [40] appearing in the computation of loop scattering amplitudes. A general
Feynman parameter formula takes the following form.
1∏m
i=0 Ai
= m!
∫
x∈Im+1
dm+1x δ(1− ∑m
i=0 xi)
(∑m
i=0 xiAi)m+1 (7.181)
where Im+1 is the unit cube given by 0 < xi < 1 for all i. Integrating over 0 < x 0 < 1
yields
1∏m
i=0 Ai
= m!
∫
x∈Im
0<∑m
i=1xi<1
dmx 1
(A0 + ∑m
i=1 xi(Ai− A0))m+1 (7.182)
Now change variables xi→ αi so that
xi = αi
1 + ∑m
j=1 αi
(7.183)
and αi > 0 for all i is the equivalent region of integration. The Jacobian for the change of
measure is
dmx = dmα
(1 + ∑m
i=1 αi)m+1 (7.184)
Putting everything together, we get
1
m!
1∏m
i=0 Ai
=
∫
αi>0
dmα 1
(A0 + ∑m
i=1 αiAi)m+1 (7.185)
We see that the right hand side is very reminiscent of the volume formula (7.174) for a
(dual) simplex. The lesson here is that loop integrals can be reinterpreted as polytope
volumes, and Feynman parameters are coordinates on the interior of the polytope over
which we integrate.
– 72 –

<!-- page 76 -->

7.4.2 Laplace transforms
For a convex projective polytope A⊂ Pm(R), we let ¯A⊂ Rm+1 be the cone over A, so
that ¯A :={Y ∈ Rm+1| Y ∈A} . Similarly, one has the cone of the dual ¯A∗
Y ⊂ Rm+1 in
the dual vector space. For simplicity, we will only consider the dual for which Y ∈ Int(A),
in which caseA∗ :=A∗
Y .
We argue that the canonical rational function at any point Y ∈ Int(A) is given by a
Laplace transform over the cone of the dual:
Ω( ¯A)(Y ) = 1
m!
(∫
W∈ ¯A∗
Y
e−W·Y dm+1W
)
. (7.186)
Such integral formulae have been considered in [42]. Extensions to the Grassmannian are
discussed in [41]
We now show the equivalence of (7.186) with the dual volume (7.174). We begin with
the Laplace transform, and change variables by writing W = ρˆW so that ˆW is a unit vector
and ρ > 0 is the Euclidean norm of W . It follows that
dm+1W = 1
m! ρmdρ
⣨
ˆW dmˆW
⟩
(7.187)
The Laplace transform rational function becomes
Ω(A) = 1
m!
∫
ρ>0,ˆW∈A∗
e−ρˆW·Y ρmdρ
m!
⣨
ˆW dmˆW
⟩
= 1
m!
∫
ˆW∈A∗
⣨
ˆW dmˆW
⟩
(ˆW· Y )m+1
. (7.188)
This result is identical to (7.174) but “gauge-ﬁxed” so that W = ˆW has unit norm. Re-
moving the gauge choice and rewriting ˆW as W recovers (7.174).
In principle, this completes the argument, but let us do a few important examples.
Example 7.24. Suppose ∆ is a simplex, so ∆ ∗ is also a simplex, generated by facets
W1, . . . , Wm+1∈ Rm+1. Then setting W = α0W1 +··· αmWm+1, we compute
Ω( ¯∆)(Y ) = 1
m!
(∫
W∈ ¯A∗
e−W·Y dm+1W
)
(7.189)
= 1
m!⟨W1W2··· Wm+1⟩
(∫
Rm+1
>0
e−(α0(W1·Y )+α1(W2·Y )+···+αm(Wm+1·Y ))dm+1α
)
(7.190)
= ⟨W1W2··· Wm+1⟩
m!(Y· W1)(Y· W2)··· (Y· Wm+1) , (7.191)
in agreement with (5.7).
We recognize the result simply as the volume Vol (∆∗) (note the implicit dependence
on Y ). For a general convex polytope A, we may triangulate its dual A∗ = ∑
i ∆∗
i by
(dual) simplices. Then the cone of the dual is also triangulated by the cones ∆i
∗
of the
dual simplices. For simplicity let us assume that these dual cones are non-overlapping
– 73 –

<!-- page 77 -->

except possibly at mutual boundaries. We can therefore triangulate the Laplace transform
integration and obtain:
Ω(A)(Y ) =
∑
i
Vol (∆∗
i ) (7.192)
which of course is equivalent to Vol (A∗) as expected.
Let us now try a sample computation for a non-simplex polytope.
Example 7.25. LetA⊂ P2 be the polytope with vertices:
{(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1,−1)}
Then the dual cone is
¯A∗ ={W = (W0, W1, W2)∈ R3
≥0| W0 + W1≥ W2}. (7.193)
We compute
Ω(A) = 1
2!
∫
W∈ ¯A∗
e−W·Y dm+1W (7.194)
= 1
2!
∫ ∞
0
e−W0Y 0
∫ ∞
0
e−W1Y 1
∫ W0+W1
0
e−W2Y 2
dW2dW1dW0 (7.195)
= 1
2!
Y 0 + Y 1 + Y 2
(Y 0 + Y 2)(Y 1 + Y 2)Y 0Y 1 . (7.196)
To verify our calculation, we observe that
1
2!
Y 0 + Y 1 + Y 2
(Y 0 + Y 2)(Y 1 + Y 2)Y 0Y 1 = 1
2!
( 1
Y 0Y 1Y 2− 1
(Y 0 + Y 2)(Y 1 + Y 2)Y 2
)
(7.197)
corresponding to the triangulation A = ∆ 1∪ ∆2 where ∆ 1 has three vertices given by
{(1, 0, 0), (0, 1, 0), (0, 0, 1)} and ∆2 has vertices{(1, 0, 0), (1, 1,−1), (0, 1, 0)}.
Let us now argue that the Laplace transform makes manifest all the poles and residues
of the canonical form, and thus satisﬁes the recursive properties of the form. Suppose
{Y ∈ ∂A| W0· Y = 0} deﬁnes one of the facets of the polytope A, which we denote byB,
and hence W0 is one of the vertices ofA∗. We now show that (7.186) has a ﬁrst order pole
along the hyperplane W0· Y = 0 and identify its residue. Consider the expansion
W = αW0 + ¯W (7.198)
where α is a scalar and ¯W ∈ γ(W0), where γ(W0) denotes the union of all the facets
of the cone ¯A∗ not adjacent to W0. It is straightforward to prove that every point W
in the interior of the integration region ¯A∗ has a unique expression in the form (7.198)
with ( α, ¯W )∈ R>0× γ(W0). Furthermore, some simple algebra shows that dm+1W =
dα
⟨
W0dm ¯W
⟩
/m!. It follows that
Ω(A) = 1
m!
∫ ∞
0
dα e−α(W0·Y )
∫
¯W∈γ(W0)
e− ¯W·Y
⟨
W0dm ¯W
⟩
m! (7.199)
– 74 –

<!-- page 78 -->

The α > 0 integral can be trivially computed to reveal the ﬁrst order pole.
Ω(A) = 1
m!
1
(W0· Y )
∫
¯W∈γ(W0)
e− ¯W·Y
⟨
W0dm ¯W
⟩
m! (7.200)
If we now take a residue at (W0·Y )→ 0, we see that the remaining integral is invariant
under local shifts ¯W→ ¯W + β( ¯W )W0 along the direction of W0, where β( ¯W ) is a scalar
dependent on ¯W . So the integral is performed within the quotient space Pm/W0, which of
course is just the dual of the co-dimension one variety {Y | Y· W0 = 0} containingB. We
say that the integral has been projected through W0.
We can change the region of integration to ¯B∗ which we deﬁne to be the cone over the
union of all the facets of A∗ adjacent to W0. The change is possible because the surface
γ(W0)∪ ¯B∗ is closed under the projection. The choice of notation ¯B∗ suggests that the
region can be interpreted as the cone of the dual of B. Indeed, the facets of A∗ adjacent
to W0 correspond to the vertices of B.
It follows that
lim
(W0·Y )→0
Ω(A)(W0· Y ) = 1
m!
(∫
¯W∈B∗
e
¯W·Y dm ¯W
)
(7.201)
where dm ¯W is deﬁned to be the measure
⟨
W0dm ¯W
⟩
/m! on Pm/W0. We can interpret the
residue as a Laplace transform for B, as expected from the recursive nature of the residue.
7.4.3 Dual Amplituhedra
As argued in Section 3, a signed triangulation of a positive geometry A = ∑
iAi implies
Ω(A) = ∑
i Ω(Ai). This was argued based on the observation that spurious poles cancel
among the triangulating terms, thus leaving only the physical poles.
In our discussion of the dual polytope in Section 7.4.1, we argued that the volume
formulation of the canonical rational function (under certain assumptions) provides an
alternative understanding of triangulation independence. We therefore wish to extend these
assumptions to the Amplituhedron and conjecture a volume interpretation of the canonical
rational function. We restrict our conjecture to even m, since the volume formula implies
positive convexity (see Section 9), which in most cases does not hold for odd m.
LetA denote an Amplituhedron, and let X denote the irreducible variety in which it
is embedded. We conjecture the following:
Conjecture 7.26. 1. For each Y∈ X not on a boundary component of A, there exists
an irreducible variety X∗
Y, called the dual variety at Y, with a bijection (X,B) ∼−→
(X∗
Y ,B∗
Y) that maps positive geometries in X to positive geometries in X∗
Y. In par-
ticular, there exists a dual AmplituhedronA∗
Y for eachY.
2. Let B1,2 be positive geometries in X. Then B1⊂B 2 if and only if B∗
2Y⊂B∗
1Y.
3. Given a triangulation of B in X, we have
B =
∑
i
Bi ⇒ B ∗
Y =
∑
i
B∗
iY . (7.202)
– 75 –

<!-- page 79 -->

4. There exists a Y-dependent measure dVol on X∗
Y(R) so that:
Ω(B)(Y) = Vol (B∗
Y) :=
∫
B∗
Y
dVol (7.203)
Following the reasoning outlined around (7.180), we arrive at the desired conclusion:
A =
∑
i
Ai ⇒ A ∗
Y =
∑
i
A∗
iY ⇒ (7.204)
Vol (A∗
Y) =
∑
i
Vol (A∗
iY) ⇒ Ω(A) =
∑
i
Ω(Ai) (7.205)
In words, we say that the triangulation independence of the dual volume explains the trian-
gulation independence of the form. This provides an alternative argument to cancellation
of spurious poles.
7.4.4 Dual Grassmannian volumes
We now discuss a ﬁrst attempt at constructing a dual of the (tree) Amplituhedron which
extends the dual polytope construction in Section 7.4.1, but does not necessarily follow the
format of Section 7.4.3.
Let us begin by thinking about projective space ( k = 1 and any m) and the most
obvious form associated with the space of points (Y, W ) where Y ∈ Pm(R) and W∈ Pm(R)
is in the dual:
dVolk=1,m(Y, W ) := dm+1Y
Vol GL(1)
dm+1W
Vol GL(1)
1
(Y· W )m+1 (7.206)
Completely equivalently but slightly more naturally, we can think of the WI as being m-
planes WI1···Im in ( m+1) dimensions (Note that our dimension counting is Euclidean.),
with dVolk=1,m taking essentially the same form:
dVolk=1,m(Y, W ) = d1×(m+1)Y
Vol GL(1)
dm×(m+1)W
Vol GL(m)
1
⟨Y W⟩m+1 (7.207)
Thus we are taking the full ( m+1)-dimensional space and looking at the space of 1-planes
Y and m-planes W in it, with the only natural form possible on ( Y, W ) space.
Now letA be a convex polytope in Y space as usual. We would like to integrate the
form dVolk=1,m over some natural region in W space. An obvious way of motivating the
integration region for W is to ensure the form never has singularities when Y is in the
polytope’s interior. Since we can put Y = ∑n
i=1 CiZi with Ci > 0, we have ⟨Y W⟩ =∑n
i=1 Ci⟨iW⟩, so it is natural to say that the region in W space is deﬁned by ⟨iW⟩ > 0.
Indeed, since we know the vertices of the polytope are Zi, and these are the facets of the
dual polytope, this gives us the deﬁniton of the dual polytope in the space of hyper-planes.
And as we have indeed seen, this leads correctly to the canonical form associated with the
polytope:
Ω(A)(Y ) =
∫
⟨iW⟩≥0
dVolk=1,m(Y, W ) (7.208)
– 76 –

<!-- page 80 -->

where for simplicity we have absorbed any combinatorial factor into the measure.
All of this has an obvious extension to the Amplituhedron for general k, and even m
where we expect the geometry to be positively convex (see Section 9). In the full ( k + m)-
dimensional space where Zi lives, we consider k-planes Y and m−planes W , and the form
on (Y, W ) space:
dVolk,m(Y, W ) = dk×(m+k)Y
Vol GL(k)
dm×(m+k)W
Vol GL(m)
1
⟨Y W⟩m+k (7.209)
We conjecture that for Y ∈ Int(A), the canonical form Ω(A) is given by an integral
over a “dual Amplituhedron” in exactly the same way. As with the polytope example, we
want to ensure this form has no singularities whenY is in the Amplituhedron, and the most
obvious way of ensuring this is to deﬁne the dual Amplituhedron region by⟨i1··· ikW⟩≥ 0,
for 1≤ 11 <··· , < ik≤ n. Thus it is natural to conjecture
Ω(A)(Y ) =
∫
⟨i1···ikW⟩≥0
dVolk,m(Y, W ) (incorrect for k > 1) (7.210)
Where, again, the measure is appropriately normalized. This conjecture turns out to be
incorrect for k > 1, but let us do a simple example so we can discuss the subtleties.
Consider the ﬁrst non-trivial case where m = 2 , k = 2 , n = 4, so Y and W each
corresponds to a 2-plane in 4 dimensions. We can put the Z matrix to be identity. Then
the inequalities deﬁning the dual Amplituhedron are ⟨W 12⟩≥ 0,⟨W 23⟩≥ 0,⟨W 34⟩≥
0,⟨W 14⟩≥ 0,⟨W 13⟩≥ 0,⟨W 24⟩≥ 0. Note crucially that ⟨W 13⟩,⟨W 24⟩ are both positive
(in the interior), whereas for Y in the Amplituhedron interior, ⟨Y 13⟩,⟨Y 24⟩ are both
negative. This region in W space can be parametrized by WIJ = (W1W2)IJ with
W =
(
1−α1 0 α4
0 α2 −1 α3
)
(7.211)
where α1,2,3,4 > 0. We can also conveniently put YIJ = (Y1Y2)IJ in the Amplituhedron by
setting
Y =
(
1 β1 0−β4
0 β2 1 β3
)
(7.212)
for β1,2,3,4 > 0. Then⟨Y W⟩ = (α2+β2)(α4+β4)+( α1+β1)(α3+β3) and we must integrate
∫
α∈R4
>0
d4α 3
((α2 + β2)(α4 + β4) + (α1 + β1)(α3 + β3))4 (7.213)
The integrals can be performed easily, leading to
1
4
[
− 1
β1β2β3β4
+ 1
β2
1β2
3
log
(
1 + β1β3
β2β4
)
+ 1
β2
4β2
2
log
(
1 + β4β2
β1β3
)]
(7.214)
which can be written more invariantly as
− ⟨1234⟩2
4⟨Y 12⟩⟨Y 23⟩⟨Y 34⟩⟨Y 14⟩ + (7.215)
⟨1234⟩2
4⟨Y 23⟩2⟨Y 14⟩2 log
(
1 +⟨Y 23⟩⟨Y 14⟩
⟨Y 12⟩⟨Y 34⟩
)
+ ⟨1234⟩2
4⟨Y 12⟩2⟨Y 34⟩2 log
(
1 +⟨Y 12⟩⟨Y 34⟩
⟨Y 23⟩⟨Y 14⟩
)
– 77 –

<!-- page 81 -->

Here we encounter a surprise. The ﬁrst term looks like the expected canonical form
associated with the k = 2, m = 2, n = 4 Amplituhedron, but with the wrong sign. And we
have extra logarithmic corrections, so the form is not rational! In fact it is easy to check
that this form has the interesting property of having none of the usual poles expected of
the canonical form! For instance we expect poles when ⟨Y 12⟩→ 0; but in this limit, the
pole from the ﬁrst rational term precisely cancels what we get from expanding the logs.
However it is certainly amusing that the expected canonical form can be identiﬁed (even if
with the wrong sign!) as the “rational part” of this expression. We plan to return to these
questions in [30].
7.4.5 Wilson loops and surfaces
Continuing our search for the “dual Amplituhedron”, let us now consider another approach.
We wish to construct a simple “dual integral” formula (not necessarily a volume) yielding
the canonical rational function for the m = 2 tree Amplituhedron.
Let us begin by describing why the problem is challenging, returning to the k = 1
polygon example for m = 2. Here we have a polygon whose vertices are ZI
i , and the
Amplituhedron (a polygon) is just the convex hull of these vertices. Now for any k, the
co-dimension one boundaries of the m = 2 Amplituhedron are WIJ
i := (ZiZi+1)IJ , which
are 2-planes in (2 + k) dimensions. Here the product ZiZi+1 is a wedge product, so WIJ
i
is alternating, and projectively can be thought of as points in ∧2R4 ∼= R6 or P5 when
projectivized. Loosely speaking, we would like the dual Amplituhedron to be the “convex
hull of the WIJ
i ”. But there is a basic diﬃculty: while we can add vectors (i.e. 1-planes)
together to get other vectors, we cannot in general add k−planes to get other k−planes. In
the special case where k = 1, the WIJ
i = ϵIJK WiK are dual to points WiK, and so can be
added. Note of course that the WiK are just vertices of the dual polytope. But for general
k, if a natural notion of the “dual” Amplituhedron is to exist along these lines we must
learn how to deal with adding k-planes together.
We will defer a discussion of general strategies for doing this to [30], here we will discuss
one approach that can be carried to completion for the special case of m = 2. We begin
by noting that while we cannot add arbitrary 2-planes WIJ
a to get other 2-planes, adding
two consecutive W ’s does yield a 2-plane; to wit:
αWIJ
i−1 + βWIJ
i = [Zi(−αZi−1 + βZi+1)]IJ (7.216)
For α, β > 0, this gives us a line from Wi−1 to Wi within the Grassmannian. Thus there
is a natural“polygon” P in G(2, 2 + k) with the vertices WIJ
i joined consecutively by line
segments as above. Here we have not speciﬁed an interior for the polygon, only its edges.
In fact, since the embedding space G(2, 2+k) has dimension greater than 2 for k > 1, the
polygon does not necessarily have a unique interior. We return to this important point
shortly.
Since our canonical form has rank 2 × k, it is natural to expect the “dual integral”
representation to be an integral over a 2 × k dimensional space. Given this canonical
one-dimensional boundary in G(2, 2 +k), a simple possibility presents itself. Consider any
– 78 –

<!-- page 82 -->

(a) The standard measure on the Grassmannian
G(k, k+m) is formed by connecting the arrows on
the left with those on the right in the most natural
way. Namely, for each blue node, the k outgoing
arrows should be connected with each of the k
orange nodes.
(b) The measure for ( d ˜W W d ˜W )I1···I2k−2. The index contractions
are deﬁned graphically. In particular, we note that WIJ should
have 2 upstairs indices and hence 2 outgoing arrows, while d ˜WI1...Ik
should have k incoming arrows.
(c) Index contraction for the numerator of
ωk(W1, . . . , Wk; Y ). For each orange node, the
k outgoing arrows should be connected with each of
the k purple nodes.
Figure 9: Diagrams representing tensor contractions. Each node denotes a tensor, with
each outgoing arrow denoting an upstairs index of the tensor, and each incoming arrow
denoting a downstairs index.
– 79 –

<!-- page 83 -->

2-dimensional surface whose boundary is the one-dimensional polygon P . Now consider
any k of these surfaces Σ s for s = 1 ,··· , k, which may be distinct. Then we would like
to consider a k-fold integral over the space Σ := Σ 1×···× Σk. This gives us a 2 × k
dimensional integral as desired but appears to depend on the choice of Σ s for each s; our
only hope is that the forms are closed (in each of thek components independently) and thus
the integral depends only on the (canonical) polygon P and not on the particular surface
spanning it. As we will see, the structure of this form is essentially ﬁxed by demanding
that it is consistently deﬁned on the Grassmannian, and it will indeed turn out to be closed
in each component independently.
Let us ﬁrst recall what ﬁxes the structure of forms on the Grassmannian (see also
the discussion in Appendix C). Consider ﬁrst the Grassmannian G(k, k+m) associated
with a matrix YI
s with s = 1 , . . . , k and I = 1 ,··· , k+m. We can think of Y in a more
GL(k) invariant way as a k−fold antisymmetric tensor YI1···Ik = ϵs1···sk YI1
s1··· YIk
sk . It is
also natural to consider the m-plane ˜YJ1···Jm = ϵI1···IkJ1···JmYI1···Ik. The Pl¨ ucker relations
satisﬁed by Y are then contained in the simple statement YK
s YKJ2···Jm = 0.
It will be convenient to introduce a graphical notation for the GL( k+m) indices here.
Each node represents a tensor; and for each tensor, an upstairs index is denoted by an
arrow outgoing from the node and a downstairs index by an incoming one. Then YI1···Ik is
a node with k outgoing arrows and ˜YI1...Im is a node with m incoming ones, as shown by
the orange nodes in Figure 9.
Now as discussed in Appendix C, in order for a diﬀerential form to be well-deﬁned on
the Grassmannian, it must be invariant underlocalGL(k) transformations, YI
s → Lt
s(Y )YI
t .
We repeat the argument here from a graphical point of view. Since dY → L((L−1dL)Y +
dY ) under this transformation, we must have that the measure is unchanged if we replace
any single factor of dY I
s with any YI
t . This ﬁxes the standard measure factor ⟨Y dmY⟩ in
projective space up to scale. Generalizing to the Grassmannian, we are looking for a k× m
form. It is natural to consider the GL( k) invariant k-form (dkY )I1···Ik, deﬁned as minors of
the matrix of dY ’s, or (dkY )I1···Ik := ϵs1···sk dY I1
s1··· dY Ik
sk . For local GL(k) invariance, every
leg of (dkY ) must be contracted with some ˜Y , so that the replacement dY I
s → YI
t vanishes
by Pl¨ ucker. Thus there is a natural k× m form on the Grassmannian, whose diagram is
a complete graph connecting m factors of ( dkY ) on one side, and k factors of ˜Y on the
other side, as in Figure 9a. It is easy to see that in the standard gauge-ﬁxing by GL( k)
where a k× k block of the matrix representation of G(k, k+m) is set to the identity, this
form is simply the wedge product of the remaining variables. Any top-form on G(k, k+m)
is expressible as this universal factor multiplied by a GL(k) co-variant function of the Y ’s
with weight−(k+m). While the contraction described here is diﬀerent from the one given
in (C.8), they are equivalent, which can be shown by gauge ﬁxing.
We now use the same ideas to determine the structure of the 2 k-form on Σ. Let us
start with the case k = 2. We are looking for a 4-form that is the product of two 2-forms,
on the space of WIJ
1 and WIJ
2 . Here the subscripts 1 , 2 index the integration variables, not
the vertices Wi; the distinction should be clear form context. By the same logic as above,
we will build the form out of the building blocks ( d ˜W W d ˜W )IJ (see Figure 9b), which are
invariant under local GL(2). We then ﬁnd a form with appropriate weights under both the
– 80 –

<!-- page 84 -->

Ws and Y rescaling, given by
ωk=2(W1, W2; Y ) =
(
d ˜W1W1d ˜W1
)
IJ
(
d ˜W2W2d ˜W2
)
KL
YIK YJL
( ˜W1· Y )3( ˜W2· Y )3 (7.217)
We then claim that the canonical rational function for the m = 2, k = 2 Amplituhedron
can be expressed as
Ω(A(2, 2, n))(Y ) =
∫
Σ1×Σ2
ωk=2(W1, W2; Y ) (7.218)
For general k we will have k factors of ( W· Y )3 in the denominator, thus to have the
correct weight−(2 +k) in minors of Y , we have to have 2k− 2 factors of Y upstairs. Now
the objects (d ˜WsWsd ˜Wi)I1···I2k−2 each have 2k−2 incoming arrows (as in Figure 9b), while
every YI1···Ik has k outgoing arrows. We can thus express ωk(W1,··· , Wk; Y ) graphically
as the complete graph linking the k factors of (d ˜W W d ˜W ) on one side and the (2 k− 2) Y ’s
on the other, as shown in Figure 9c. We then claim that
Ω(A(k, 2, n))(Y ) =
∫
Σ
ω(W1, . . . , Wk; Y ) (7.219)
These expressions indeed reproduce the correct canonical rational function for the
m = 2 Amplituhedron for all k. Let us illustrate how this works for the case of k = 2.
A straightforward computation shows that the form ωk=2(W1, W2; Y ) is closed in W1, W2
independently; indeed it is closed even if the WIJ are not constrained by the Pl¨ ucker
relations, and can be thought of as being general points in P5. Thus the result of the
integral is independent of the surface Σ, provided that ∂Σs = P for each s. We will thus
construct each surface Σ s by triangulating it like the interior of a polygon. We begin
by picking an arbitrary reference point XIJ , and taking the triangle in P5 with vertices
X, Wi−1, Wi, which we denote by [X, Wi−1, Wi]. It follows that the union∪n
i=1[X, Wi−1, Wi]
forms a surface with boundary P , so we will take it to be our deﬁnition of Σ s for each s.
Suppose we integrate over the triangle pair ( W1, W2)∈ [X, Wi−1, Wi]× [X, Wj−1, Wj].
We can parametrize the triangle pair by
W1 = X + α1Zi−1Zi + β1ZiZi+1 (7.220)
W2 = X + α2Zj−1Zj + β2ZjZj+1 (7.221)
where α1,2 > 0; β1,2 > 0.
The only non-trivial part of the computation is working out the numerator index
contraction in (7.217). After a series of index gymnastics, we get for each i, j:
ωk=2 = 1
2
(N1(i, j) +N2(i, j))d2αd2β
(⟨Y X⟩ + α1⟨Y i−1, i⟩ + β1⟨Y i, i+1⟩)3 (⟨Y X⟩ + α1⟨Y j−j, j⟩ + β1⟨Y j, j+1⟩)3
(7.222)
where
N1(i, j) :=⟨Y X⟩⟨ Xij⟩⟨ Y (i−1, i, i+1)∩ (j−1, j, j+1)⟩ (7.223)
N2(i, j) :=−⟨ Y (i−1, i, i+1)∩ (Xj)⟩⟨ Y (j−1, j, j+1)∩ (Xi)⟩ (7.224)
– 81 –

<!-- page 85 -->

where⟨Y (abc)∩ (def)⟩ :=⟨Y1abc⟩⟨ Y2def⟩− (Y1↔ Y2) for any vectors a, b, c, d, e, f.
Integrating over α1,2 > 0; β1,2 > 0 and summing over all i, j gives us
∫
Σ
ωk=2 = 1
8
n∑
i,j=1
N1(i, j) +N2(i, j)
⟨Y X⟩2⟨Y i−1, i⟩⟨ Y i, i+1⟩⟨ Y j−1, j⟩⟨ Y j, j+1⟩
(7.225)
This is one of several local expressions for the canonical rational function Ω (A(2, 2, n)).
That is, there are no spurious singularities, except at ⟨Y X⟩→ 0. Interestingly, if we keep
only one of the numerator terms N1,N2, then the result would still sum to (half) the
correct answer. Perhaps some clever manipulation of the integration measure would make
this manifest. If we only keep the ﬁrst numerator, then we recover the local form given
in (7.56).
It is possible, through a clever choice of the surface Σ, to recover the Kermit represen-
tation (7.55) of the canonical rational function. While the equivalence between the Kermit
representation and the local form appears non-trivial as an algebraic statement, it follows
easily from the surface-independence of the integral.
This computation can be extended easily to higher k. Furthermore, since the surfaces
Σ1, . . . ,Σk are independent, it is possible to have picked a diﬀerent X for each surface,
giving a local form with arbitrary reference points X1, . . . , Xk.
7.4.6 Projective space contours part I
We now turn to a new topic. We show that the rational canonical form of convex projective
polytopes (and possibly more general positive geometries) can be represented as a contour
integral over a related projective space.
Recall for convex projective polytopesA that the n× (m + 1)-matrix Z can be consid-
ered a linear map Pn−1→ Pm, sending the standard simplex ∆n−1 to the polytopeA. Let-
ting (Cj)n
j=1 denote the coordinates on Pn−1, we have the equationY = Z(C) = ∑n
j=1 CjZj
describing the image Y ∈ Pm of a point C∈ Pn−1 under the map.
We begin with the simplex canonical form on (Cj)n
j=1∈ Cn constrained on the support
of the expression Y = ∑n
j=1 CjZj:
∫ dnC∏n
j=1 Cj
δm+1

Y−
n∑
j=1
CjZj

 . (7.226)
Typically, the delta function on projective space δm(Y, Z(C)) is reduced from rank m+1
to m by integrating over a GL(1) factor like ρ in (7.101). Instead, we have absorbed the
dρ/ρ measure into the canonical form on C-space, thus giving a rank- n measure on Cn.
We now describe a contour in the C-space such that the above integral gives the
canonical rational function Ω (A). A naive integral over all C∈ Rn is obviously ill-deﬁned
due to the 1 /Cj singularities. However, with some inspiration from Feynman, we can
integrate slightly away from the real line Cj → cj = Cj + iϵj for some small constants
ϵj > 0, with cj∈ R being the contour. We will assume that ∑n
j=1 ϵjZj = ϵY for some
ϵ > 0, and let ¯Y := (1 + iϵ)Y . After completing the contour integral, we can take the
– 82 –

<!-- page 86 -->

limit ϵ→ 0 to recover ¯Y → Y . This is reminiscent of the epsilons appearing in the loop
integration of amplitudes. Finally, we assume that the Zj vertices form a real convex
polytope and ¯Y is a positive linear combination of the Zj’s. Note that ¯Y is real and Y is
now slightly imaginary due to the iϵ shift.
We claim, in the ϵj→ 0 limit,
Ω(A)(Y ) = 1
(2πi)n−m−1m!
∫ dnc∏n
j=1(cj− iϵj) δm+1

 ¯Y−
n∑
j=1
cjZj

 (7.227)
with integration over cj∈ R for each j. The overall constants have been inserted to achieve
the correct normalization.
Before proving this identity in full generality, we give a few examples.
Example 7.27. The simplest example occurs for n = m+1 whereA is just a simplex in m
dimensions. In that case, there is no contour, and we can immediately set ϵj→ 0 for each
j and thus ϵ→ 0. We get
Ω(A)(Y ) = 1
m!
∫ dm+1c∏m+1
j=1 cj
δm+1

Y−
m+1∑
j=1
cjZj

 (7.228)
We can uniquely solve for each cj on the support of the delta function, which gives
cj = (−1)j−1
⣨
Y 12··· ˆj··· (m+1)
⟩
⟨12··· (m+1)⟩ (7.229)
where the “hat” denotes omission, and the Jacobian of the delta function is⟨12··· (m+1)⟩.
It follows that (see (5.8))
Ω(A)(Y ) = [1, 2, . . . , m+1] (7.230)
which is the familiar canonical rational function for a simplex.
More generally, suppose we integrate over a contour in the original C space that picks
up a set of poles at Cj→ 0 for all j except j = j0, . . . , jm, which we assume to be arranged
in ascending order. Then the residue is given by
1
m!
∫ 
∏
j∈J
ResCj=0

 dnC∏n
j=1 Cj
δ

Y−
n∑
j=1
CjZj

 = [j0, j1, j2, . . . , jm] (7.231)
where J = {1, 2, . . . , n}−{ j0, j1, j2, . . . , jm}. Suppose the indices contained in J are
k1, . . . , kn−m−1 in increasing order, then we will denote the residue collectively as Res( J)
or Res(k1, k2, . . . , kn−m−1). So
Res(J) := Res(k1, . . . , kn−m−1) := [j1, j2, . . . , jm] (7.232)
We note that the result may come with a negative sign if the contour is negatively oriented.
The Res operator, however, assumes a positive orientation. This formula will be very
convenient for the subsequent examples.
– 83 –

<!-- page 87 -->

We now move on to higher n examples for the polygon (i.e. m = 2).
Example 7.28. We now perform the contour integral explicitly at n = 4 points for the
m = 2 quadrilateral. There are four integrals over ci constrained by three delta functions.
We will integrate out c1,2,3 to get rid of the delta functions with a Jacobian factor ⟨123⟩3,
which gives us
1
2!(2πi)
∫
c4∈R
dc4/⟨123⟩3
(c1− iϵ1)(c2− iϵ2)(c3− iϵ3)(c4− iϵ4) (7.233)
where c1, c2, and c3 depend on c4 through the three equations ¯Y = Z(c).
In the large c4 limit, all three dependent variables scale like O(c4), so the integrand
scales like O(c−4
4 ) which has no pole at inﬁnity. We can now integrate over c4 by applying
Cauchy’s theorem. The key is to ﬁrst work out the location of the four poles relative to
the real line.
We begin with the constraints
¯Y = c1Z1 + c2Z2 + c3Z3 + c4Z4 (7.234)
which can be re-expressed in terms of three scalar equations by contracting with Z2Z3,
Z3Z1, and Z1Z2, respectively.
c4⟨234⟩ =
⟨ ¯Y 23
⟩
− c1⟨123⟩ (7.235)
c4⟨134⟩ =−
⟨ ¯Y 31
⟩
+ c2⟨123⟩ (7.236)
c4⟨124⟩ =
⟨ ¯Y 12
⟩
− c3⟨123⟩ (7.237)
We have written the equation so that each bracket is positive, provided thatZi is cyclically
convex and Y is inside the polygon. Both positivity conditions are crucial, because they
prescribe the location of the poles.
Now, for any index i = 1, 2, 3, 4, we let the “pole at i” refer to the pole at ci→ iϵi.
From the constraints, we ﬁnd that poles 1 and 3 both provide a negative imaginary part
to c4, so they are below the real line, while poles at 2 and 4 are above the real line (see
Figure 10). Since there is no pole at inﬁnity, the integral can be performed by closing the
contour below to pick up poles 1 , 3, or closing the contour above to pick up poles 2 , 4. The
former gives us
Ω(A) = Res(1) + Res(3) = [2, 3, 4] + [1, 2, 4] (7.238)
while the latter gives
Ω(A) = Res(2) + Res(4) = [1, 3, 4] + [1, 2, 3] (7.239)
Of course, these are two equivalent triangulations of the quadrilateral. We see therefore
that the iϵ contour beautifully explains the triangulation independence of the canonical
rational function as a consequence of Cauchy’s theorem.
– 84 –

<!-- page 88 -->

Figure 10: The locations of the four poles for the quadrilateral iϵ contour, with c1, c2 and
c3 dependent on c4 through ¯Y = c· Z. A pole is colored red if a counterclockwise contour
picks up the residue with a plus sign (e.g. +Res(2) , +Res(4)), while a pole is colored blue if
a counterclockwise contour picks up the residue with a minus sign (e.g.−Res(1),−Res(3)).
Of course, the signs are reversed if the contour is clockwise.
Example 7.29. We now compute the contour for a pentagon, where new subtleties emerge.
We begin as before by integrating over c1, c2 and c3 to get rid of the delta functions. We
then re-express the delta function constraints as three scalar equations.
c4⟨234⟩ + c5⟨235⟩ =
⟨ ¯Y 23
⟩
− c1⟨123⟩ (7.240)
c4⟨134⟩ + c5⟨135⟩ =−
⟨ ¯Y 31
⟩
+ c2⟨123⟩ (7.241)
c4⟨124⟩ + c5⟨125⟩ =
⟨ ¯Y 12
⟩
− c3⟨123⟩ (7.242)
We now integrate over c4 ∈ R. The locations of the poles are the same as before (see
Figure 10), and we are free to choose how we close the contour. For sake of example,
let us close the contour above so we pick up poles 2 and 4. We now analyze both poles
individually.
The pole at 4 induces c4→ iϵ4. Our constraints therefore become:
c5⟨235⟩ =
⟨ ¯Y 23
⟩
− c1⟨123⟩− iϵ4⟨234⟩ (7.243)
c5⟨135⟩ =−
⟨ ¯Y 31
⟩
+ c2⟨123⟩− iϵ4⟨134⟩ (7.244)
c5⟨125⟩ =
⟨ ¯Y 12
⟩
− c3⟨123⟩− iϵ4⟨124⟩ (7.245)
There are now four poles left for c5, corresponding to 1,2,3 and 5. The poles at 1 and 3
are clearly below the real line, as evident in the equations above, while the the pole at 5
is obviously above (see Figure 11). The pole at 2, however, is more subtle and deserves
closer attention. In the limit c2→ iϵ2, we ﬁnd from the second equation above that
c5⟨135⟩ =−
⟨ ¯Y 31
⟩
+ iq (7.246)
– 85 –

<!-- page 89 -->

Figure 11: The pole locations of c5 under c4→ iϵ4 (left) and c2→ iϵ2 (right). Note that
in both graphs the position of the 24 pole relative to the real line diﬀers depending on the
sign of q. See the caption under Figure 10 for explanations of the pole coloring.
where q = ϵ2⟨123⟩− ϵ4⟨134⟩. If q > 0, then the pole at 2 is above the real line, and if
q < 0, then the pole is below. So the relative size of the ϵj parameters makes a diﬀerence
to the computation. However, as we now show, the ﬁnal result is unaﬀected by the sign of
q. Suppose q > 0, then we can close the c5 contour above and pick up the following poles
Res(45) + Res(24) = [123] + [135] (7.247)
Alternatively, we can close below and pick up
Res(34) + Res(14) = [125] + [235] (7.248)
The two results, of course, are identical since there is no pole at inﬁnity. So the pole at
4 produces the following result regardless of how the c5 contour is closed, provided that
q > 0.
c4→ iϵ4 ; q > 0 ∼ Ω(Z1, Z2, Z3, Z5) (7.249)
If q < 0, then Res(24) migrates below the real line, in which case closing the contour above
would give
Res(45) = [123] (7.250)
and closing below would give
Res(34) + Res(14)− Res(24) = [125] + [235]− [135] (7.251)
which of course are equivalent. The minus sign in front of Res(24) appears due to the
orientation of the contour. In summary,
c4→ iϵ4 ; q < 0 ∼ Ω(Z1, Z2, Z3) (7.252)
Now let us move on to the pole of c4 at 2 which induces c2→ iϵ2. Again, there are
four poles left for c5, this time corresponding to 1,3,4,5. After re-arranging the constraints
– 86 –

<!-- page 90 -->

using Schouten identities, we ﬁnd
c5⟨123⟩⟨ 345⟩ =
⟨ ¯Y 34
⟩
⟨123⟩−⟨ 123⟩ (c1⟨134⟩ + iϵ⟨234⟩) (7.253)
c4⟨145⟩⟨ 123⟩ =−
⟨ ¯Y 41
⟩
⟨123⟩ +⟨123⟩ (iϵ2⟨124⟩ + c3⟨134⟩) (7.254)
c5⟨135⟩ =
⟨ ¯Y 13
⟩
+ iϵ2⟨123⟩− c4⟨134⟩ (7.255)
Evidently, the poles at 3 and 5 are above the real line, while the pole at 1 is below (see
Figure 11). The pole at 4, however, is above if q > 0 and below if q < 0.
For q > 0, closing the c5 contour above gives
Res(23)− Res(24) + Res(25) = [145]− [135] + [134] (7.256)
while closing below gives
Res(12) = [345] (7.257)
which are equivalent, so
c2→ iϵ2 ; q > 0 ∼ Ω(Z3, Z4, Z5) (7.258)
For q < 0, closing the contour above gives
Res(23) + Res(25) = [145] + [134] (7.259)
while closing below gives
Res(12) + Res(24) = [345] + [135] (7.260)
which are again equivalent, so
c2→ iϵ2 ; q > 0 ∼ Ω(Z1, Z3, Z4, Z5) (7.261)
We now sum over the c4→ iϵ4 and c2→ iϵ2 contributions. For q > 0, we get
Ω(A) = Ω(Z1, Z2, Z3, Z5) + Ω(Z3, Z4, Z5) (7.262)
and for q < 0, we get
Ω(A) = Ω(Z1, Z2, Z3) + Ω(Z1, Z3, Z4, Z5) (7.263)
Both results are of course correct. Again, we see triangulation independence as a result of
Cauchy’s theorem, but with additional subtleties involving the sign of q. Furthermore, we
could have closed thec4 contour below instead and achieved a diﬀerent set of triangulations.
We now argue for all m > 0 and all n≥ m+1 that the iϵ contour integral (7.227) is
equivalent to the dual volume formula (7.174). Let S denote the right hand side of (7.227).
We begin by writing the delta function in terms of its Fourier transform with dual variable
W∈ Rm+1.
δm+1

 ¯Y−
n∑
j=1
cjZj

 = 1
(2π)m+1
∫
dm+1W ei(−W· ¯Y +∑n
j=1cjW·Zj) (7.264)
– 87 –

<!-- page 91 -->

Then we integrate over each cj using the following identity:
∫
R
dcj
cj− iϵj
eicjW·Zj = (2πi) θ(W· Zj) (7.265)
where θ(x) is the Heaviside step function. It follows that
S = im+1
m!
∫
dm+1W e−iW· ¯Y
n∏
j=1
θ(W· Zj) (7.266)
We also change variables to radial coordinates ρ :=|W| and ˆW := W/|W| with|W|
denoting the Euclidean norm of W . We have W = ρ ˆW so that the measure now becomes
dm+1W = ρmdρ
⣨
ˆW dm ˆW
⟩
/m!, where
⣨
ˆW dm ˆW
⟩
is the pull back of ⟨W dmW⟩ to the
sphere ˆW∈ Sm.
Now recall the Fourier transform identity:
1
m!
∫
R
dx xmθ(x)e−ixy = (−i)m+1
(y− iϵ′)m+1 (7.267)
for some small ϵ′ > 0 which we take to zero in the end. The integral over ρ > 0 therefore
becomes:
1
m!
∫ ∞
0
dρ ρme−iρ ˆW· ¯Y = (−i)m+1
( ˆW· ¯Y− iϵ′)m+1 = (−i)m+1
( ˆW· Y )m+1 (7.268)
where we set ϵ′→ 0 on the right.
It follows that
S = 1
m!
∫
ˆW∈Sm
⣨
ˆW dm ˆW
⟩ 1
( ˆW· ¯Y )m+1
n∏
j=1
θ( ˆW· Zj) (7.269)
= 1
m!
∫
A∗
⟨W dmW⟩ 1
(W· ¯Y )m+1 (7.270)
which is the volume formula (7.174) for Ω (A) in the limit ¯Y → Y . In the last step, we
used that fact that the inequalities W· Zj > 0 imposed by the step functions carve out
the interior of the dual polytope A∗⊂ Pm. Furthermore, on the last line we removed the
“gauge” choice ˆW∈ Sm, since the resulting integral is gauge invariant under GL(1) action.
We stress that it is absolutely crucial for ¯Y to be on the polytope’s interior. Otherwise,
the denominator factor W· ¯Y can vanish and cause divergent behavior. From the contour
point of view, as shown in examples above, the position of ¯Y aﬀects the location of poles
relative to the contour.
7.4.7 Projective space contours part II
We now consider an alternative contour integral that is in essence identical to the previous,
but represented in a very diﬀerent way. The result is the following
Ω(A)(Y ) = 1
(2π)n−m−1m!
∫ dnB∏n
j=1(C0
j− iBj) δm+1


n∑
j=1
BjZj

 (7.271)
= 1
(2π)n−m−1m!
∫
B∈K
dn−m−1B∏n
j=1(C0
j− iBj) (7.272)
– 88 –

<!-- page 92 -->

for any point C0 = (C0
1 , C0
2 , . . . , C0
n)∈ Rn such that Y = ∑n
j=1 C0
j Zj and C0
j > 0. In the
second equation, K⊂ Rn denotes the ( n−m−1) dimensional kernel of the map Z : Rn→
Rm+1. The measure on K is deﬁned as
dn−m−1B :=
∫
dnB δm+1


n∑
j=1
BjZj

 = dBk1··· dBkn−m−1
⟨j0··· jm⟩ (7.273)
for any partition{j0, . . . , jm}∪{ k1, . . . , kn−m−1} of the index set{1, . . . , n}. On the right,
it is understood that B· Z = 0.
We now argue that (7.271) is equivalent to (7.227). An immediate consequence is that
this contour integral is independent of the choice of C0.
We begin with the iϵ contour (7.227), ﬁx a choice c0 satisfying ¯Y = c0· Z, and change
integration variables cj→ bj = c0
j− cj.
Ω(A)(Y ) = 1
(2πi)n−m−1m!
∫ dnb∏n
j=1(c0
j− bj− iϵj) δm+1


n∑
j=1
bjZj

 (7.274)
For each bj, there is a pole at bj = c0
j− iϵj which lives in the fourth quadrant on the
complex plane of bj. Since we are currently integrating over the real line, it is possible
to do a clockwise Wick rotation bj→ Bj =−ibj to integrate over the imaginary line (i.e.
Bj∈ R) without picking up any of the poles. It follows that
Ω(A)(Y ) = 1
(2π)n−m−1m!
∫ dnB∏n
j=1(c0
j− iBj− iϵj) δm+1


n∑
j=1
BjZj

 (7.275)
We can now set ϵj→ 0 as it no longer aﬀects the contour of integration. In this limit,
we recover c0
i → C0
i and ¯Y → Y , giving Y = C0· Z and hence the desired result. The
formula (7.271) was ﬁrst established in [43, Theorem 5.5].
Let us work out one example.
Example 7.30. LetA⊂ P2 have vertices{(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1,−1)}, as in Exam-
ple 7.25. The kernel is K ={(x, x,−x,−x) : x∈ R}⊂ R4. For Y = (Y 0, Y 1, Y 2) we pick
C0 = (Y 0− a, Y 1− a, Y 2 + a, a) for some a∈ R, with the assumption that all entries are
positive. Thus
Ω(A)(Y ) = 1
(2π)2!
∫ ∞
−∞
dx
(Y 0− a− ix)(Y 1− a− ix)(Y 2 + a + ix)(a + ix) (7.276)
= 1
2!
( 1
Y 0Y 1Y 2− 1
(Y 0 + Y 2)(Y 1 + Y 2)Y 2
)
(7.277)
where we have chosen to close the contour by picking the poles x = ia and x = i(Y 2 + a)
with positive imaginary part. This is independent of a, as expected, and agrees with
(7.197).
– 89 –

<!-- page 93 -->

It is interesting to contrast these contour representations with the Newton polytope
push-forward formula discussed in Section 7.3.3. For the former, the combinatorial struc-
ture of the convex polytope is automatically “discovered” by the contour integration with-
out prior knowledge. For the latter, the combinatorial structure must be reﬂected in the
choice of the Newton polytope, which may not be possible for polytopes whose combinato-
rial structure cannot be realized with integral coordinates (e.g. non-rational polytopes [44]).
7.4.8 Grassmannian contours
The generalization of the iϵ contour formulation to the Amplituhedron for k > 1 is an
outstanding problem. We now give a sketch of what such a generalization may look like at
tree level, if it exists.
We conjecture that the canonical rational function of the tree Amplituhedron, denoted
A(k, n, m; L=0), is given by a contour integral of the following form:
Ω(A) = 1
(2πi)k(n−m−k)(m!)k
∫
Γ
dk×nC∏n
i=1 Ci,i+1,...,i+k−1
δk×(k+m) (Y− C· Z) (7.278)
where the delta functions impose the usual Y = C· Z constraint while the measure over
C is the usual cyclic Grassmannian measure on G≥0(k, n). The integral is performed over
some contour Γ which we have left undeﬁned.
For n = m+k, there is no contour and we trivially get the expected result. For n =
m+k+1, we have naively guessed a contour that appears to work according to numerical
computations. The idea is to simply change variables C → c so that for every Pl¨ ucker
coordinate we have ci1,...,ik = Ci1,...,ik + iϵi1,...ik for a small constant ϵi1,...,ik > 0. We
will assume that ∑
1≤i1<···<ik≤n ϵi1...ik Zi1∧ . . .∧ Zik = ϵY for some ϵ > 0 and deﬁne
¯Y := (1 + iϵ)Y (We are re-scaling Pl¨ ucker coordinates here, not components of the matrix
representation.) so we can re-express Y = C· Z as ¯Y = c· Z as we did for the polytope.
Again, we assume that ¯Y is real and Y is slightly complex.
We then integrate over the real part of c.
Ω(A)(Y ) = 1
(2πi)k(m!)k
∫
Γ
dk×(m+k+1)c∏m+k+1
i=1 [ci,i+1,...,i+k−1−iϵi,i+1,...,i+k−1]
×
δk×(k+m) (¯Y− c· Z
)
(7.279)
After integrating over the delta function constraints, there are eﬀectively only k integrals
left to do. Conveniently, the poles appearing in the cyclic measure are linear in each
integration variable, and can therefore be integrated by applying Cauchy’s theorem.
One obvious attempt for generalizing beyond n > m +k+1 is to impose the exact same
iϵ deformation. However, after having integrated over the delta functions, the cyclic minors
are at least of quadratic order in the integration variables, thus making the integral very
challenging to perform (and possibly ill-deﬁned in the small ϵ limit). It is therefore still a
challenge to extend the contour integral picture to the Amplituhedron.
Despite the diﬃculty of extending the iϵ contour, our optimism stems from the well-
known observation that the canonical rational function of the physical Amplituhedron is
– 90 –

<!-- page 94 -->

given by a sum of global residues (see Appendix F) of the Grassmannian measure con-
strained on Y = C· Z. This was seen in the study of scattering amplitudes. See for
instance [1] and references therein. It is therefore reasonable to speculate that a choice of
contour would pick up the correct collection of poles whose global residues sum to the ex-
pected result, and that diﬀerent collections of residues that sum to the same result appear
as diﬀerent deformations of the same contour.
We expect these constructions to continue for the L-loop Amplituhedron. Namely, we
expect that the canonical rational function of the L-loop AmplituhedronA(k, n, m; lL) to
be given by a sum over global residues of the canonical form of the L-loop Grassmannian
G(k, k+m; lL) constrained by Y = Z(C) forC∈ G(k, k+m; lL) andY∈A (k, n, m; lL). A
non-trivial example for the 1-loop physical Amplituhedron A(1, 6; L=1) is given in [22].
The complete solution to this proposal is still unknown since the canonical form of the
loop Grassmannians are mostly unknown.
8 Integration of canonical forms
8.1 Canonical integrals
In this section we provide a brief outline of an important topic: integration of canonical
forms.
Consider a positive geometry ( X, X1,≥0) with canonical form Ω( X, X1,≥0). Naively,
integration of the form over X(R) or X1,≥0 is divergent due to the logarithmic singulari-
ties. However, consider another positive geometry ( X, X2,≥0) which does not intersect the
boundary components of X1,≥0 except possibly at isolated points. We can therefore deﬁne
the integral of the canonical form of X1,≥0 over X2,≥0:
ωX2,≥0(X1,≥0) =
∫
X2,≥0
Ω(X, X1,≥0) (8.1)
We will refer to such integrals as canonical integrals.
In particular, if X1,≥0 is positively convex, and X2,≥0⊂ X1,≥0, and X2,>0 is oriented
in the same way as X1,>0 where they intersect, then the integral is positive.
We observe that ω is triangulation independent in both arguments. Namely, given a
triangulation X2,≥0 = ∑
i Yi,≥0, we have
ωX2,≥0(X1,≥0) =
∑
i
ωYi,≥0(X1,≥0) (8.2)
A similar summation formula holds for a triangulation of X1,≥0.
The simplest example is the familiar polylogarithm functions, which can be reproduced
as canonical integrals.
Example 8.1. Let 0 < z < 1. Consider the standard simplex ( Pm, ∆m) and the simplex
(Pm, ∆m(z)) with vertices
(1, 0, 0, 0, . . . ,0, 1), (1, z, 0, 0, . . . ,0, 1), (1, z, z, 0, . . . , 0, 1), . . . ,(1, z, z, z, . . . , z,1), (8.3)
(1, z, z, z, . . . , z, 1−z) (8.4)
– 91 –

<!-- page 95 -->

where the ﬁrst row consists of m vectors containing 0,1,2,. . . , m−1 components of z,
respectively, and the second row consists of an extra point. We will refer to ∆ m(z) as the
polylogarithmic simplex of order m.
Alternatively, the simplex ∆ m(z) can be constructed recursively in m by beginning
with ∆1(z) which is simply the line segment x∈ [1− z, 1] with (1, x)∈ P1(R), and observe
that
∆m(z) =
⋃
t∈[0,z]
{t}× ∆m−1(t) (8.5)
where{t}× ∆m−1(t) denotes all the points (1 , t, x)∈ Pm(R) with (1 , x)∈ ∆m−1(t).
We argue by induction on m≥ 1 that the integral of the canonical form of ∆ m over
∆m(z) is precisely the polylogarithm Li m(z). That is,
Lim(z) =
∫
∆m(z)
Ω(∆m) (8.6)
Indeed, for m = 1, we have
∫
∆1(z)
Ω(∆1) :=
∫ 1
1−z
dt
t =− log(1− z) = Li1(z) (8.7)
Now suppose m > 1. Given the recursive construction (8.5), it is straightforward to show
that
∫
∆m(z)
Ω(∆m) =
∫ z
0
dt
t
∫
∆m−1(t)
Ω(∆m−1) (8.8)
This is the same recursion satisﬁed by the polylogarithms:
Lim(z) =
∫ z
0
dt
t Lim−1(t) (8.9)
which completes our argument.
8.2 Duality of canonical integrals and the Aomoto form
Now consider the special case of convex polytopes in projective space. We wish to discuss
an important duality of canonical integrals.
Consider convex polytopes A1,A2 in Pm(R) satisfying A2⊂A 1. It follows that the
dual polytopes (see Section 6.1.3) satisfy A∗
1 ⊂ A∗
2. While the polytope pair provides
a canonical integral ωA2(A1), the dual polytope pair provides a dual canonical integral
ωA∗
1(A∗
2). We claim that these two integrals are identical:
ωA2(A1) = ωA∗
1(A∗
2) (8.10)
This is the duality of canonical integrals, which can be derived easily by recalling the dual
volume formulation of the canonical rational function in Section 7.4.1, and arguing that
– 92 –

<!-- page 96 -->

both the canonical integral and its dual can be expressed by the same double integral as
follows:
ωA2(A1) = ωA∗
1(A∗
2) = 1
m!
∫
Y∈A2
∫
W∈A∗
1
⟨Y dmY⟩⟨ W dmW⟩
(Y· W )m+1 (8.11)
where we let Y ∈ Pm(R) and let W denote vectors in the dual projective space.
The double integral appearing on the right is said to be in Aomoto form , and was
used to express polylogarithmic functions as an integral over a pair of simplices [45]. For
extensions to polytopes, see [46].
Furthermore, we expect the duality of canonical integrals to hold for positive geome-
tries in projective space with non-linear boundaries. However, in such case, the canonical
rational function must be deﬁned by the volume of the dual region, which for a general
positive geometry can be obtained by approximating it by polytopes and taking the limit
of their duals. The details are discussed in Section 10, where it is emphasized that this
formulation of the canonical rational function does not necessarily match the deﬁnition in
Section 2 except for polytopes.
9 Positively convex geometries
Let (X, X≥0) be a positive geometry. The canonical form Ω( X, X≥0) may have zeros, and
the zero set may intersect X>0. Furthermore, in some cases the set of poles of Ω( X, X≥0)
may also intersect X>0. If neither the poles nor the zeros intersect X>0, then the form
Ω(X, X≥0) must be uniformly oriented on each connected component of the interior. In
this case, our sign conventions for Res (see (A.3)) and orientation inheritance by boundary
components (see Section A.1) ensures that Ω( X, X≥0) is positively oriented on the interior
relative to the orientation of X>0, which can be proven easily by induction on dimension.
In this case, we say that the canonical form is positively oriented, or simply positive.
As we shall explain below, the positivity of the canonical form has some relation to
the usual notion of convexity of the underlying positive geometry. We deﬁne a positive
geometry (X, X≥0) to be positively convex if its canonical form Ω( X, X≥0) is positive. We
remark that if (X, X≥0) and (Y, Y≥0) are positively convex geometries then so are (X, X−
≥0)
and (X× Y, X≥0× Y≥0). Also, boundary components of positively convex geometries are
again positively convex.
Consider ( P2,A) where A is a convex quadrilateral. As shown in Section 7.1.1, the
canonical form Ω(A) has four linear poles, and one linear zero. The poles are the four
sides ofA, and the zero is the line L that passes through the two intersection points of the
opposite sides. It is an elementary exercise to check that L never intersectsA. Thus the
convex quadrilateralA is a positively convex geometry. Indeed, we have:
Every convex projective polytope ( Pm,A) is a positively convex geometry. (9.1)
This follows immediately from either (7.174) or (7.186) which give positive integral formulae
for Ω(A)(Y ) for Y ∈ Int(A).
– 93 –

<!-- page 97 -->

Figure 12: A non-convex quadrilateral. The black dashed lines denote the two boundary
components that pass through the geometry’s interior. The red dashed line L is where the
canonical form vanishes. The form is negative inside the small triangle bounded completely
by dashed lines.
On the other hand, suppose instead that A′ is a nonconvex quadrilateral, as shown in
Figure 12. Again Ω( A′) has four linear poles and one linear zero. However, in this case,
the line L passes through the interior ofA′, and indeed two of the poles also pass through
the interior. Thus A′ is not a positively convex geometry. Nevertheless, note that near
most points of the boundary of A′, the form Ω(A′) is positively oriented. For a general
positively convex geometry, the form is always positively oriented in a neighborhood of
every 0-dimensional boundary component.
On the other hand, not every positive geometry (even connected ones) in P2 that is
convex in the usual sense is also positively convex. For example, consider the following
semialgebraic subset of P2(R):
A :={triangle with vertices (0 , 10), (−1, 0), (1, 0)}∪
{southern half disk with center (0 , 0) and radius 1}
Since both the triangle and the southern half disk are positive geometries, by Section 3,
A is itself a positive geometry. One of the poles of Ω( A) is along the boundary C =
{x2 + y2− 1 = 0}, and this pole passes through the triangle. It is then clear that Ω( A) is
not positive everywhere in the interior of A. Indeed, the other poles of Ω( A) are the two
non-horizontal sides S1, S2 of the triangle, and the numerator of Ω( A) is the line L that
passes through the intersection points P1, P2 of S1, S2 with C above the horizontal axis.
Thus Ω(A) is negative exactly within the region bounded by C and L.
Let us now discuss some other examples of positively convex geometries. Recall from
Section 2.4 that a positive geometry in dimension one is a disjoint union of intervals, say
A = ⋃r
i=1[ai, bi] where a1 < b1 < a2 < b2 <··· < ar < br. The canonical form is
Ω(A) =
∑
i
( 1
x− ai
− 1
x− bi
)
dx.
– 94 –

<!-- page 98 -->

Given x0∈ (aj, bj), the positivity of Ω(A) is equivalent to the inequality
∑
i
( 1
x0− ai
− 1
x0− bi
)
=
( 1
x0− aj
− 1
x0− bj−1
)
+
( 1
x0− aj−1
− 1
x0− bj−2
)
+··· + 1
x0− a1
+
(
− 1
x0− bj
+ 1
x0− aj+1
)
+
(
− 1
x0− bj+1
+ 1
x0− aj+2
)
+···− 1
x0− br
> 0
where each bracketed term is positive.
We do not know of a simplex-like positive geometry that is not positively convex.
Indeed all the the positive geometries in Section 5 are positively convex. For the simplices
and generalized simplices in projective spaces that we construct this can be seen directly
from the canonical form. Alternatively, it is easy to see that the boundaries never intersect
the positive part. For the positive parts of Grassmannians, toric varieties, ﬂag varieties
and cluster varieties, one may argue as follows. For each such positive geometry ( X, X≥0)
of dimension D, there is a complex torus T = (C∗)D⊂ X such that the positive part X>0
can be identiﬁed with the positive part RD
>0⊂ (C∗)D, and furthermore the canonical form
Ω(X≥0) can be identiﬁed with the standard holomorphic and non-vanishing form ΩT on T .
If x1, . . . , xD are coordinates on T , then ΩT = ∏
i d log xi. Since Ω( X≥0) is holomorphic
and non-vanishing on X>0, it follows that ( X, X≥0) is positively convex. Note that for
toric varieties, there is a unique choice of torus T , while for Grassmannians, ﬂag varieties,
and cluster varieties, there are many choices for the torus T .
Finally, we make the following conjecture:
Conjecture 9.1. The Amplituhedron A(k, n, m; 2L) is a positively convex geometry for
even m.
The cases m = 1, 2 (for L = 0) are discussed in Section 7.2.4. Conjecture 9.1 would
follow immediately from the existence of a dual Amplituhedron (see Section 7.4.3). Note
that the simple example of a Grassmann polytope in Section 7.2.6 is not positively convex,
a fact which we numerically veriﬁed.
As we remarked in Section 7.2.5, the k = 1, L = 1 positive loop Grassmannian
G>0(1, n; 2) is also positively convex.
10 Beyond “rational” positive geometries
We now consider some simple observations suggesting that our notion of positive geometry
should likely be thought of as a rational type of more general positive geometries. As we
stressed in the introduction, with our current deﬁnitions the disk is not a proper positive
geometry; it does not have zero-dimensional boundaries and its associated canonical form
vanishes. But of course we should be able to think of the disk as a polygon in the limit
of an inﬁnite number of vertices. In fact, let us consider more generally the limit of the
polygon form as the polygon boundary is taken to approximate a conic QIJ YI YJ = 0.
Without doing any computations, it is easy to guess the structure of the answer. In the
– 95 –

<!-- page 99 -->

smooth limit, the form should only have singularities when Y sits on the conic, i.e. when
Y Y· Q→ 0. But then by projective weights, the form must look like
Ω′(A) = C0×⟨Y dY dY⟩(det Q)3/4
(Y Y· Q)3/2 (10.1)
for some constant C0. Here we added an apostrophe since Ω ′(A) is not the canonical from
deﬁned in Section 2. We will shortly calculate the form and determine that the constant is
C0 = π. Note that the disappearance of the “zero-dimensional boundaries” in the limit is
associated with another novelty: the form is not rational, but has branch-cut singularities.
This clearly indicates that the notion of positive geometry we are working with needs to
be extended in some way; what we have been seeing are the “rational parts” of the forms,
which indeed vanishes for the circle, but there is a more general structure for the forms
associated with more interesting analytic structures.
Let us now compute the form for the region bounded by a conic, which without loss
of generality we can take to be the unit disk D2. We can take the external data to have
the form
Z(θ) =


1
cos θ
sin θ

 (10.2)
for 0≤ θ < 2π.
Let us ﬁrst do the computation in the most obvious way using approximation by
triangulation. Consider a polygonAN with vertices Z(θi) where θi = iδθ for i = 0, . . . , N−1
and δθ := 2 π/N. Let Z∗ be an arbitrary vertex not on the circle. Then the canonical
rational function for the polygon can be triangulated by
Ω(AN) =
N−1∑
i=0
[Z∗, Z(θi), Z(θi+1)] (10.3)
where the i’s are labeled mod N.
Now consider the canonical form for one of these triangles with corners Z∗, Z(θ), Z(θ +
δθ) for some small δθ:
1
2
⟨Z∗Z(θ)Z(θ + δθ)⟩2
⟨Y Z∗Z(θ)⟩⟨Y Z∗Z(θ + δθ)⟩⟨Y Z(θ)Z(θ + δθ)⟩ = 1
2 δθ ⟨Z∗Z(θ) ˙Z(θ)⟩2
⟨Y Z(θ) ˙Z(θ)⟩⟨Y Z∗Z(θ)⟩2 + O(δθ2)
(10.4)
where the dot denotes diﬀerentiation in θ.
Thus, in the limit of large N, (10.3) becomes:
Ω′(D2) = lim
N→∞
Ω(AN) = 1
2
∫ 2π
0
dθ ⟨Z∗Z ˙Z⟩2
⟨Y Z∗Z⟩2⟨Y Z ˙Z⟩
(10.5)
Note that very nicely this expression is invariant under any co-ordinate change in θ.
This tells us that the result only depends on the shape of the circle, not on the particular
– 96 –

<!-- page 100 -->

way in which it is approximated by a polygon. (Of course this is trivially expected from
the expression of the form as the area of the dual polygon which approximates the dual
conic, and we will perform the computation in that way momentarily).
Let us put Z∗ = (1, 0, 0) and Y = (1, x, y). We are left with
Ω′(D2) = 1
2
∫ 2π
0
dθ 1
(1− x cos θ− y sin θ)(y cos θ− x sin θ)2 (10.6)
Note that for real (x, y), the factor (y cos θ−x sin θ) inevitably has a zero on the integration
contour. This is easy to understand: the factor⟨Y Z∗Z⟩ inevitably has a zero when Y, Z∗, Z
are collinear, which for any Y on the disk’s interior must occur for some Z on the circle.
Of course since the ﬁnal form is independent of Z∗, this singularity is spurious. In order
to conveniently deal with this, we will give y a small imaginary part; by a rotation we can
put the real part of y to zero, so y =−iϵ. If we further put z = eiθ, we are left with a
contour integral around the origin
Ω′(D2) =−i
∮
dz 4z2
(xz2− 2z + x)(x(z2− 1)− ϵ(1 + z2))2 (10.7)
This integral can be trivially performed by residues. The poles associated with the second
factor in the denominator are both pushed away from the circle, assuming that Y lies in
the circle (so|x| < 1). Note that the product of the roots of the ﬁrst factor is 1, so one of
the poles of the ﬁrst factor is inside the circle and the other is outside. There is thus only
a single pole inside the circle, and we obtain
Ω′(D2) = π
(1− x2− y2)3/2 (10.8)
where we have put the y component back in.
We can of course also obtain the same result as a volume integral (7.174) over the dual
of the unit diskD2∗ which is the unit disk in the dual space. Again, by putting Y = (1, x,0)
for|x| < 1, and the integration variable W = (1, r cos θ, r sin θ), this gives us the integral:
Vol (D2∗) =
∫ 2π
0
∫ 1
0
rdrdθ
(1 + rxcosθ)3 = π
(1− x2)3/2 (10.9)
which can be performed by ﬁrst integrating over r, then doing the angular integral by
residues via z = eiθ. We can re-express this in projective terms to precisely get
Ω′(D2) = π (det Q)3/4
(Y Y· Q)3/2 (10.10)
as anticipated.
Let us next look at an obvious extension to the “pizza slice” geometry T (θ1, θ2) from
Example 6.1. Note that the the integrand is exactly the same as in our original triangulation
above, but we will instead be integrating over the arc A(θ1, θ2) from z1 = eiθ1 to z2 = eiθ2,
representing the intersetion of the pizza slice boundary with the circle. The reference Z∗ is
still the same. We will not need the regulator so we will put ϵ→ 0. Now, the integrand is
I(z) := 1
x3
4iz2
(z− r+)(z− r−)(z2− 1)2 , with r± = 1±
√
1− x2
x (10.11)
– 97 –

<!-- page 101 -->

Note that it has non-vanishing residues at z = r±, but the residues at z =±1 vanish.
Instead we have double-poles at z =±1. It is therefore natural to split this integrand
into two parts: one part that only has simple poles with the correct residues at z = r±,
and another piece that does not have any simple poles at all, that matches the rest of the
singularities. Thus we can write
I = Ilog + Irational (10.12)
with
Ilog := i
2(1− x2)3/2
( 1
z− r+
− 1
z− r−
)
, I rational :=− i
x2(1− x2)
(x + 2z + xz2)
(1− z2)2
(10.13)
The term Ilog(z) has logarithmic singularities and (naturally) integrates to give a logarithm,
and we get
i
2(1− x2)3/2 log
((z2− r+)(z1− r−)
(z1− r+)(z2− r−)
)
(10.14)
We can express this more elegantly in projective terms as
Ωlog(T (θ1, θ2)) = i(det Q)3/4
2(Y Y· Q)3/2× log[L+, L−, P1, P2] (10.15)
Here L± are the corners of the pizza slice on the conic Q, and P1,2 are the two points
on the conic that are on the tangent lines passing through Y . (Note that when Y is outside
the conic these tangent points are real, while when Y is inside the conic they are complex).
We can think of these as four points on the P1 deﬁned by the conic itself, and [ a, b, c, d] is
the cross-ratio of these four points on the conic.
Now let us look at Irational(z); since by construction it has vanishing residues, it must
be expressible as the derivative of a rational function; indeedIrational = −i
x2(1−x2) ∂z
(
(1+xz)
(1−z2)
)
.
Hence this term integrates to a rational function of Y , which of course reproduces our usual
canonical form associated with the pizza-slice geometry, written in projective terms as
Ωrational(T (θ1, θ2)) = Y· L
(Y Y· Q)(X· W1)(X· W2) (10.16)
where L is the line that kills the two “bad” singularities as we have seen a number of times
in our earlier discussion, and W1,2 deﬁne the two linear boundaries of the pizza.
We can draw a few conclusions from these simple computations. To repeat, by the
deﬁnitions of this paper, the circle should be assigned a vanishing canonical form, and
this is intuitively reasonable, since it does not have any zero-dimensional boundaries so
we cannot have an associated form with logarithmic singularities on all boundaries. But
clearly the circle is a limiting case of a series of positive geometries, and the limit evades
this logic in a nice way: the form simply is not rational, but has a branch cut singularity.
Moving on to the pizza slice, our deﬁnitions do call this a positive geometry and give it an
associated rational form, but (as with the circle) we clearly would not get the same result
as we would from the continuous limit of a polygon. Here we observed that the pizza slice
– 98 –

<!-- page 102 -->

form naturally splits into two pieces: a “rational” part, which precisely matches the form
naturally associated with the positive geometry in our sense, plus a new “transcendental”
piece.
The integrals associated with the circle and pizza slices were simple enough to tempt
us into direct computations, but the way in which the results split into rational and tran-
scendental pieces was somewhat mysterious. Is this split canonical? And why did the
“rational part” of this computation magically reproduce our usual deﬁnition of the (ratio-
nal) canonical form?
We will answer these questions by doing the computation again, more conceptually,
not just for the case of a circle but for any positive geometryA bounded by a parametrized
curve and two lines emanating from a point Z∗. Suppose we have some polynomially
parametrized curve Z(t), where t is some reparametrization of θ. We will then consider
the integral
Ω(A) =
∫ t2
t1
dtF (t), with F (t) = ⟨Z∗Z ˙Z⟩2
2⟨Y Z ˙Z⟩⟨Y Z∗Z⟩2 (10.17)
Let us ﬁrst examine the singularities of a general function
F (t) = R(t)
Q(t)P (t)2 (10.18)
where R(t), Q(t), P(t) are generic polynomials. We will assume that the degrees are such
that F decays at least as fast as t−2 at large t. Let qi be the roots of Q(t), and pα be the
roots of P (t). Clearly, F (t) has double-poles as t→ pα. Looking at the singular pieces as
t→ pα we have
F (t→ pα) = sα
(t− pα)2 + rα
t− pα
+··· (10.19)
with
sα = R(pα)
Q(pα) ˙P (pα)2 , r α = sα
( ˙R
R(pα)−
˙Q
Q(pα)−
¨P
˙P
(pα)
)
(10.20)
Similarly we have simple poles for F (t) as t→ qi,
F (t→ qi) = ri
t− qi
+··· , with ri = R(qi)
˙Q(qi)P (qi)2 (10.21)
Thus it is natural to express F (t) as a sum of two pieces,Fdp(t) with only double-poles,
and Fsp(t) with only simple poles,
F (t) = Fdp(t) + Fsp(t) (10.22)
where
Fdp(t) =
∑
α
sα
(t− pα)2 , F sp =
∑
α
rα
t− pα
+
∑
i
ri
t− qi
(10.23)
When we integrate F (t), this decomposition canonically divides the result into a “ra-
tional” and “logarithmic” part just as we saw in our pizza-slice example:
∫ t2
t1
dtF (t) = Ωrational(A) + Ωlog(A) (10.24)
– 99 –

<!-- page 103 -->

where
Ωrational(A) :=
∑
α
sα
( 1
t1− pα
− 1
t2− pα
)
Ωlog(A) :=
∑
α
rαlog
(t2− pα
t1− pα
)
+
∑
i
rilog
(t2− qi
t1− qi
)
(10.25)
Let us now specialize to the particular case of our F (t), and look ﬁrst at the rational
part. We ﬁnd
Ωrational(A) =
∑
pα
⟨Z∗Z ˙Z⟩2
2⟨Y Z ˙Z⟩⟨Y Z∗ ˙Z⟩2
( 1
t1− pα
− 1
t2− pα
)
(10.26)
where the pα are roots of⟨Y Z∗Z(t)⟩ = 0. Remarkably, we can recognize this sum over roots
as a push-forward onto A! Note ﬁrst that since ⟨Y Z∗Z⟩ = 0, we can write Y = Z∗ + uZ
for some scalar u, and thus
Ωrational(A) =
∑
pα
1
2⟨Z∗Z ˙Z⟩
1
u2
( 1
t1− pα
− 1
t2− pα
)
(10.27)
Now, clearly, the map
(t, u)→ Φ(t, u) := Z∗ + uZ(t) (10.28)
is a morphism from [ t1, t2]× [0,∞]⊂ P(R)2 toA. The canonical form on ( t, u) space is
Ω([t1, t2]× [0,∞]) = dt
( 1
t− t2
− 1
t− t1
)
× du
u (10.29)
Since⟨Y dY dY⟩ = 2ududt⟨Z∗Z ˙Z⟩, the push-forward by Φ gives us that
Φ∗ (Ω([t1, t2]× [0,∞])) =⟨Y dY dY⟩
∑
pα
1
2⟨Z∗Z ˙Z⟩
1
u2
( 1
t1− pα
− 1
t2− pα
)
(10.30)
which we immediately recognize as Ω rational(A). Hence, by Heuristic 4.1:
Ω(A) = Ωrational(A) (10.31)
Let us next look at the logarithmic part of the integral. Here too there is a small
surprise: the residues rα as t→ pα vanish:
rα = sα
(
2⟨Z∗Z ¨Z⟩
⟨Z∗Z ˙Z⟩
−⟨Y Z ¨Z⟩
⟨Y Z ˙Z⟩
−⟨Y Z∗ ¨Z⟩
⟨Y Z∗ ˙Z⟩
)
= 0, when⟨Y Z∗Z⟩ = 0 (10.32)
which can easily be seen by putting Y = Z∗ + uZ. The logarithmic term then simply
becomes
Ωlog(A) =
∑
qi
⟨Z∗Z ˙Z⟩2
2⟨Y Z ¨Z⟩⟨Y Z∗Z⟩2 log
(t2− qi
t1− qi
)
(10.33)
– 100 –

<!-- page 104 -->

where qi are the roots of ⟨Y Z(t) ˙Z(t)⟩ = 0. Note that since ( Z(t) ˙Z(t)) is the line tangent
to the parametrized curve at t, the roots of ⟨Y Z ˙Z⟩ = 0 are exactly the points on the
curve whose tangents pass through Y . Also note that the prefactors of the logarithms
are in general algebraic functions of the variables deﬁning the parametrized curve of the
geometry.
These observations clearly suggest that while the notion of “positive geometry” we
have introduced in this paper is perfectly well-deﬁned and interesting in its own right, it
should be generalized in an appropriate way to cover the case of possibly transcendental
canonical forms for a more complete picture.
11 Outlook
We have initiated a systematic investigation of (pseudo-)positive geometries and their as-
sociated canonical forms. These concepts arose in the context of the connection between
scattering amplitudes and the positive Grassmannian/Amplituhedron, but as we have seen
they are also natural mathematical ideas worthy of study in their own right. Even our
preliminary investigations have exposed many new venues of exploration.
At the most basic level, we would like a complete understanding of positive geometries
in projective spaces, Grassmannians, and toric, cluster and ﬂag varieties. A complete
classiﬁcation in projective space seems within reach. In this case, amongst other things we
need to demand that the boundary components have geometric genus zero, and that the
boundary components of the boundary components have geometric genus zero, and so on.
Perhaps most pressingly we would like to prove that the Amplituhedron itself is a
positive geometry! A proof of this fact seems within reach using familiar facts about the
Amplituhedron. There is ﬁrst a purely geometrical problem of showing that the Ampli-
tuhedron can be triangulated by images of “cells” of the positive loop Grassmannian under
the Amplituhedron map Z. With this in hand, we simply need to prove that the images of
these cells are themselves positive geometries. At this moment, “cells” refers to positroid
cells at tree level; at loop level, we suspect that a generalization exists, which we showed
for k = 1, L = 1, m = 2.
We have also deﬁned the notion of a “positively convex” geometry, where the canonical
form has no zeros or poles on the interior. As we have stressed, this is a highly non-trivial
property of the canonical form for Amplituhedra of even m, which is not manifest term-
by-term in the computation of the form using triangulations (e.g. BCFW). Finding more
examples of positively convex geometries in more general settings should shed more light on
these fascinating spaces. It would be particularly interesting to classify positively convex
geometries in the context of general Grassmann polytopes; these are likely to exist given
that cyclic polytopes are a special case of general convex polytopes.
The most important question is to give a natural and intrinsic way of deﬁning the
canonical form. Two directions here seem particularly promising–Is there a generalization
of the Newton-polytope “push-forward” method from polytopes to general positive geome-
tries? The examples we have for m = 2 Amplituhedra are encouraging but we do not yet
have a general picture. Similarly, does the “volume of dual polytope” or “contour integral
– 101 –

<!-- page 105 -->

over auxiliary geometry” ideas extend beyond polytopes to general positive geometries?
We again gave analogs of these constructions for some Amplituhedra but do not under-
stand the general structure. It would again be particularly interesting to look for such a
description for general Grassmann polytopes.
Finally, we have a number of indications suggesting that our notion of positive geom-
etry should be thought of as a special case of “rational” positive geometry, which must be
extended in some way to cases where the canonical form is not rational. We encountered
transcendental forms in two places–in looking at the most obvious “dual Grassmannian
integral” representation for the very simplest Amplituhedron forms, and in the “continu-
ous” limit of polygons. There are also other settings where such an extension seems called
for–for instance, there exist deformations of the positive Grassmannian/Amplituhedron
representation of scattering amplitudes to continuous helicities for the external particles,
that are natural from the point of view of integrable systems [47], which modify scattering
forms away from being rational. Demanding the existence of rational canonical forms on
positive geometries, with logarithmic singularities recursively deﬁned by matching lower-
degree canonical forms on lower dimensional boundaries, has led us to the simultaneously
rigid and rich set of objects we have studied in this paper. So, what replaces this criterion
for forms which are not rational? Finding the natural home in which to answer this ques-
tion, and identifying the associated generalization beyond rational positive geometries, is
a fascinating goal for future work.
Acknowledgments
We would like to thank Michel Brion, Livia Ferro, Peter Goddard, Song He, Nils Kanning,
Allen Knutson, Tomasz Lukowski, Alexander Postnikov, David Speyer, Hugh Thomas,
Jaroslav Trnka, Lauren Williams and Ellis Yuan for stimulating discussions. NA-H was
supported by the DOE under grant DOE DE-SC0009988. YB was supported by NSERC
PGS D and Department of Physics, Princeton University. TL was supported by NSF grant
DMS-1464693 and a Simons Fellowship.
A Assumptions on positive geometries
In this section we discuss several technical assumptions needed for positive geometries. We
will let ( X, X≥0) denote an arbitrary positive geometry throughout.
A.1 Assumptions on X≥0 and deﬁnition of boundary components
Let X>0 be the interior of the subspace X≥0⊂ X(R). Then X>0 is also a semialgebraic
set. We assume that X>0 is an open oriented real submanifold of X(R) of dimension D,
and that X≥0 is the closure of X>0. In particular, X(R) must be a dimension D real
algebraic variety. If X>0 has multiple connected components, one may have many choices
of orientations.
– 102 –

<!-- page 106 -->

Let ∂X≥0 := X≥0\ X>0. Let ∂X = ∂X≥0 denote the Zariski closure in X, deﬁned to
be
∂X ={x∈ X| p(x) = 0 if p(y) = 0 for all y∈ ∂X≥0} (A.1)
where p denotes a homogeneous polynomial. In other words, if a polynomial vanishes on
∂X≥0, then it also vanishes on ∂X, and ∂X is the largest set with this property. The set
∂X is a closed algebraic subset of X. We let C1, C2, . . . , Cr denote the codimension one
(that is, dimension D−1) irreducible components of ∂X. Deﬁne Ci,≥0 to be the closure of
the interior of Ci∩ ∂X≥0 as a subset of the real algebraic variety Ci(R).
The boundary components of (X, X≥0) are (Ci, Ci,≥0) for i = 1, 2, . . . , r. It is clear that
Ci,≥0 is a semialgebraic set. Axiom (P1) requires that Ci,≥0 has dimension D−1.
We now deﬁne an orientation on Ci,≥0. Let U ⊂ RD−1× R be an open set so that
(x, z)∈ U∩ (RD−1× R≥0) is a local chart for X≥0 with z = 0 mapped to the boundary.
We assume that Euclidean charts are oriented in the standard way.
• For D = 1: If the chart is orientation preserving, then we assign +1 orientation to
the point Ci,≥0; otherwise, we assign−1.
• For D > 1: We can always choose a chart that is orientation preserving. The bound-
ary therefore inherits locally the standard orientation of the ﬁrst D−1 components.
We remark that “reversing the orientation ofX>0” maps positive geometries to positive
geometries.
A.2 Assumptions on X
We must impose geometric conditions on the complex variety X for Axiom (P2) to make
sense. For the applications we have in mind, X may be singular. We will usually make the
assumption that X is a normal variety, so in particular the singular locus is of codimension
two or more. A rational D-form ω on X is deﬁned to be a rational D-form on the smooth
locus X◦⊂ X. If C⊂ X is a codimension one subvariety, then X◦∩ C is open and dense
in C, so the residue ResCΩ (see Appendix A.3) makes sense as a rational ( D− 1)-form on
C.
Axiom (P2) guarantees the following additional property: X must not have nonzero
holomorphic D-forms, for otherwise there is no possibility for Ω(X, X≥0) to be unique. If X
satisﬁes this property, then the uniqueness assumption in Axiom (P2) is immediate: If two
forms Ω 1(X, X≥0) and Ω 2(X, X≥0) satisfy the stated condition then their diﬀerence will
have no residues and is thus a holomorphicD-form on X, which must vanish everywhere. In
practice, X is typically also a rational variety: X has an (Zariski) open subset isomorphic
to an open subset of aﬃne space.
While we will implicitly assume that X is a normal variety throughout this work, there
do exist examples where X is non-normal but deserves to be called a positive geometry.
Indeed, some of the conjectural positive geometries in this work may require loosening
some of our technical assumptions. We discuss some explicit examples in Sections 5.3.1
and 7.1.2.
– 103 –

<!-- page 107 -->

A.3 The residue operator
The residue operator Res is deﬁned in the following way. Let ω be a meromorphic form on
X. Suppose C is an irreducible subvariety of X and z is a holomorphic coordinate whose
zero set z = 0 locally parametrizes C. Let us denote the other holomorphic coordinates
collectively as u. Then a simple pole of ω at C is a singularity of the form
ω(u, z) = ω′(u)∧ dz
z +··· (A.2)
where the··· denotes terms smooth in the small z limit, and ω′(u) is a non-zero meromor-
phic form deﬁned locally on the boundary component. We deﬁne
ResCω := ω′ (locally) (A.3)
If there is no such simple pole, then we deﬁne the residue to be zero.
B Near-equivalence of three notions of signed triangulation
We prove (3.3) by induction on D = dim X. The implications (3.3) clearly hold when
D = 0. Suppose now D > 0. Let{Xi,≥0} be an interior triangulation of the empty set. Let
C⊂ X be an irreducible subvariety of codimension one. Let ( C, Ci,≥0) be the boundary
component of ( X, Xi,≥0) along C, where we set Ci,≥0 =∅ if such a boundary component
does not exist. We claim that {Ci,≥0} is an interior triangulation of the empty set. Let
y∈ ⋃
i Ci,≥0, and assume that y does not lie on the boundary of any of the {Ci,≥0}. A
dense subset of such points (in C(R)) will in addition not lie on any of the boundary
components C′̸= C of any of the {Xi,≥0}, and we assume y is chosen to lie in this dense
subset. By assumption, (3.2) holds for all points x∈ U\ C, where U is an open ball in
X(R) containing y. By shrinking U if necessary, we may assume that U∩ C is an open
disk, and we ﬁx orientations of both U and U∩ C. The submanifold U∩ C divides U into
U + and U−, which can be labeled so that
{i| y∈ Ci,>0 and Ci,>0 is positively oriented at y}
={i| U +⊂ Xi,>0 and Xi,>0 is positively oriented on U +}
∪{i| U−⊂ Xi,>0 and Xi,>0 is negatively oriented on U−}
and
{i| y∈ Ci,>0 and Ci,>0 is negatively oriented at y}
={i| U−⊂ Xi,>0 and Xi,>0 is positively oriented on U−}
∪{i| U +⊂ Xi,>0 and Xi,>0 is negatively oriented on U +}.
We are making use of the assumptions on the local behavior of boundary components from
Appendix A.1. The equality
{i| y∈ Ci,>0 and Ci,>0 is positively oriented at y}
={i| y∈ Ci,>0 and Ci,>0 is negatively oriented at y}
– 104 –

<!-- page 108 -->

then follows from (3.2) applied to points in U + and points in U− respectively. It follows
that{Ci,≥0} is an interior triangulation of the empty set. By the inductive hypothesis we
have that{Ci,≥0} is a boundary triangulation of the empty set. Since this holds for all C,
we conclude that{Xi,≥0} is a boundary triangulation of the empty set.
Let Ω = ∑t
i=1 Ω(Xi,≥0). Suppose ﬁrst that {Xi,≥0} is a boundary triangulation of the
empty set. Let C be an irreducible subvariety of X of codimension one. Taking the residue
of Ω at C, we obtain
ResCΩ =
t∑
i=1
ResCΩ(Xi,≥0) =
t∑
i=1
Ω(Ci,≥0). (B.1)
By the inductive hypothesis we have ∑t
i=1 Ω(Ci,≥0) = 0, so we conclude that all residues
of Ω are 0, and thus Ω = 0 and {Xi,≥0} is a canonical form triangulation of the empty
set. Conversely, suppose that {Xi,≥0} is a canonical form triangulation of the empty set.
Then Ω = 0, so Res CΩ = 0 for any irreducible subvariety C ⊂ X of codimension one.
Thus{Ci,≥0} form a canonical form triangulation of the empty set, and by the inductive
hypothesis they also form a boundary triangulation of the empty set. We conclude that
{Xi,≥0} is a boundary triangulation of the empty set.
This completes the proof of (3.3).
C Rational diﬀerential forms on projective spaces and Grassmannians
C.1 Forms on projective spaces
Let η be a rational m-form on Cm+1, which we write as
η =
m∑
I=0
fI(Y )dY 0∧···∧ ˆdY I∧···∧ dY m (C.1)
where ˆdY I denotes omission. Here fI(Y ) is a rational function. Then η is the pullback of
a rational m-form on Pm if and only if
(1) η is homogeneous of degree 0, that is, fI(Y ) is homogeneous of degree −m, and
(2) ⟨η,E⟩ = 0, where E = ∑m
I=0 YI ∂I is the radial vector ﬁeld, also called the Euler
vector ﬁeld.
If we explicitly solve (2), then we learn that
η = m!· g(Y )
m∑
I=0
(−1)I YI dY 0∧···∧ ˆdY I∧···∧ dY m (C.2)
for some rational function g(Y ) of degree−m−1. We have the elegant formula
m∑
I=0
(−1)I YI dY 0∧··· ˆdY I···∧ dY m = 1
m!⟨Y dmY⟩. (C.3)
– 105 –

<!-- page 109 -->

Thus an arbitrary form on Pm can be written as
η = g(Y )ω (C.4)
for some function g(Y ) of degree−m−1, where we have deﬁned ω :=⟨Y dmY⟩
The factor ω is called the standard measureon projective space, and if η is the canonical
form of some pseudo-positive geometry ( Pm,A), then g(Y ) is called the canonical rational
function of (Pm,A) and is usually denoted Ω (A).
An alternative but equivalent description of a form η on projective space is that η
must be invariant under local GL(1) action on Y . That is, for any scalar α(Y ) possibly
dependent on Y , the form must be invariant under Y → Y′ = α(Y )Y . The word “local”
refers to the dependence of α on Y . In contrast, if α(Y ) is constant, then it would be called
a global transformation.
We argue that the factor ω is locally covariant. That is, it scales by some power of
α(Y ), and the exponent of the scaling is its GL(1) weight. Indeed, dY′ = Y dα + αdY ,
hence
⟨
Y′dmY′⟩
= αm+1⟨Y dmY⟩ (C.5)
where contraction with Y′ annihilates the dα term.
It follows that η is locally invariant under GL(1) (i.e. covariant with weight 0). Local
invariance is needed for η to be well-deﬁned on projective space.
Now suppose that θ is a rational (m+1)-form on Cm+1 which is homogeneous of degree
0. To obtain a form on projective space from θ, we deﬁne η =⟨θ,E⟩. It is not hard to see
that η is a m-form that satisﬁes (1), (2) from above. Indeed, since YI and dY I have degree
1, the vector ﬁeld ∂I has degree−1, so that η is homogeneous of degree 0. Part (2) follows
immediately from the fact that diﬀerential forms are alternating functions of vector ﬁelds,
or from the calculation that
⟨dY 0∧···∧ dY m,E⟩ =
m∑
I=0
(−1)I YI dY 0∧··· ˆdY I···∧ dY m = 1
m!⟨Y dmY⟩. (C.6)
Thus we can canonically pass between ( m+1)-forms, homogeneous of degree 0, on Cm+1
and m-forms on Pm by replacing dm+1Y by⟨Y dmY⟩/m!. An alternative way of thinking
of contracting against E is to divide by the measure of GL(1) = C∗. In other words, we
have the equality
dm+1Y
Vol GL(1) = ω (C.7)
C.2 Forms on Grassmannians
We now extend our discussion to the Grassmannian G(k, k+m).
Let M(k, k+m) denote the space of k× (k+m) matrices. For Y ∈ M(k, k+m), we
write Y1, Y2, . . . , Yk for the rows of Y , and YI
s for the component at row s and column I.
– 106 –

<!-- page 110 -->

We have an action of GL(k) on M(k, k+m) with quotient G(k, k+m). For s, t = 1, 2, . . . , k
deﬁne a vector ﬁeld
Est =
k+m∑
I=1
YI
s
∂
∂Y I
t
.
This is the inﬁnitesimal vector ﬁeld corresponding to the action of exp(test)∈ GL(k), where
est is the 0 , 1-matrix with a 1 in row s and column t.
A km-form η = η(Y ) on M(k, k+m) is the pullback of a form on G(k, k+m) if it
satisﬁes the two conditions
(1) It invariant under GL( k). That is, for any g∈ GL(k), we have g∗η = η.
(2) We have⟨η,Est⟩ = 0 for any s, t.
Condition (1) is equivalent to the condition that LEstη = 0 for any s, t, whereL denotes
the Lie-derivative. By Cartan’s formula, we have LEstη =⟨dη,Est⟩ + d(⟨η,Est⟩). By (2),
this is equivalent to the condition
⟨dη,Est⟩ = 0.
Let dk×(k+m)Y denote the natural top form on M(k, k+m). If we contract dk×(k+m)Y
against all the vector ﬁelds Est, we get up to a scalar the km-form
ω :=⟨Y1Y2··· YkdmY1⟩⟨Y1Y2··· YkdmY2⟩···⟨ Y1Y2··· YkdmYk⟩. (C.8)
While this form makes the GL( k+m) symmetry manifest, the GL( k) symmetry is hidden.
Nonetheless, both are guaranteed by our derivation. An alternative representation of the
measure making both manifest is given in Section 7.4.5.
An alternative way to think of this form is as
dk×(k+m)Y
Vol GL(k) = ω
As for projective space, we argue that ω is locally covariant under GL(k) action. Con-
sider an action of the form Y → L(Y )Y , where L(Y )∈ GL(k) acts on the rows of Y . The
diﬀerential of Y transforms as dY → L(L−1dL Y + dY ). Thus, in order to achieve local
covariance, ω must vanish whenever any dY I
s is replaced by any YI′
s′ , which is evidently the
case. It follows therefore that η is also locally invariant under GL( k), which is necessary
for η to be well-deﬁned on the Grassmannian.
Furthermore, it is easy to see directly that ⟨ω,Est⟩ = 0 holds: to compute ⟨ω,Est⟩, we
replace the t-th factor⟨Y1Y2··· YkdmYt⟩ by⟨Y1Y2··· YkYsdm−1Yt⟩, which is clearly 0.
Finally, any form η on G(k, k+m) can be written in the form
η = g(Y )ω (C.9)
for some function g(Y ) of degree −m−k in the Pl¨ ucker coordinates ofY . Similar to case
for the projective space, ω is called the standard measure on the Grassmannian; and if η
is the canonical form for some positive geometry ( G(k, k+m),A), then g(Y ) is called the
canonical rational function ofA and is usually denoted Ω (A).
– 107 –

<!-- page 111 -->

C.3 Forms on L-loop Grassmannians
The preceding discussion can be generalized toL-loop Grassmannians. Rather than ﬂeshing
out all the details, we simply write down the equivalent of the standard measure ω. The
canonical rational function is deﬁned in a similar fashion. For our purposes, the main
positive geometry of interest in the L-loop Grassmannian is the L-loop AmplituhedronA,
whose canonincal rational function Ω (A) is also called the amplitude.
LetY = ( Y, Y1, . . . , YL)∈ G(k, k + m; k) (see (6.22)). The standard measure ω on
G(k, k + m; k) is given by:
ω =
k∏
s=1
⟨Y dmYs⟩·
L∏
i=1
ki∏
s=1
⣨
Y Yidm−kiYis
⟩
(C.10)
where Ys denotes the rows of Y for s = 1 , . . . k, and Yis denotes the rows of Yi for s =
1, . . . , ki and i = 1, . . . , L.
We leave it to the reader to argue that the standard measure is locally covariant under
the groupG(k; k) deﬁned in Section 6.4.
D Cones and projective polytopes
Let V = Rm+1. A subset C⊂ V is called a convex cone if it is closed under addition and
scalar multiplication by R≥0. Thus a convex cone always contains the 0-vector. We say
that a cone C is pointed if it does not contain a line. Alternatively, C is pointed if whenever
vectors v and−v both lie in C then we have v = 0.
A polyhedral cone is the nonnegative real span
Cone(Z) := spanR≥0(Z1, Z2, . . . , Zn) =
{∑
i
aiZi| ai∈ R≥0
}
(D.1)
of ﬁnitely many vectors Z1, . . . , Zn. A rational polyhedral cone C is one such that the
generators Zi can be chosen to have integer coordinates. The dimension dim C of C is
equal to the dimension of the vector space that C spans.
From now on, let C be a pointed polyhedral cone. We will often assume that the
vectors Zi are not redundant, that is, none of them can be removed while still spanning
C. In this case, we call the Zi the generators, or edges, of C. The interior of the cone
C = Cone(Z) is then given by
Int(C) = spanR>0(Z1, Z2, . . . , Zn) =
{∑
i
aiZi| ai∈ R>0
}
(D.2)
A face F of C is the intersection F = C∩ H with a linear hyperplane H⊂ V such that
C lies completely on one side of H. Thus if H is given by v· α = 0 for some α∈ Rm+1,
then we must have C· α≥ 0 or C· α≤ 0. Every face of C is itself a rational pointed
polyhedral cone with generators given by those Zi that lie on H. Every face F′ of F is
itself a face of C. A face F is called a facet of C if dim F = dim C− 1. The 0-vector is the
unique face of C of dimension 0. We do not allow C to be a face of itself.
– 108 –

<!-- page 112 -->

A cone C is called simplicial if it has dim C generators. A triangulation of a polyhedral
cone C is a collection C1, C2, . . . , Cr of simplicial cones, all with the same dimension as C,
such that
1. We have C = ⋃
i Ci.
2. The intersection F = Ci∩ Cj of any two cones is a face of both cones Ci and Cj.
We sometimes, but not always, require the generators of Ci to be a subset of the generators
of C.
A projective polytope is the image A = Conv( Z) of a pointed polyhedral cone C =
Cone(Z) (after removing the origin) in projective space Pm. The faces (resp. facets) of A
are deﬁned to be the images of the faces (resp. facets) of C. The dimension of a face of A
is one less than the corresponding face of C. By deﬁnition, the empty face is a face of A.
The interior Int(A) is the image in Pm of the interior of the cone C.
Projective polytopes are the basic objects that we consider in Section 6.1. In some
cases we will use inequalities to deﬁne projective polytopes, and it may not be clear that
these inequalities are well-deﬁned on projective space. However, these inequalities are well-
deﬁned when lifted to cones and Rm+1. Finally, we remark that in Section 6.1, a projective
polytopeA usually refers to a polytope with an orientation, giving the interior of A the
structure of an oriented manifold. This orientation is always suppressed in the notation.
Facets F of a projective polytope A acquire a natural orientation from the orientation of
A.
A triangulation of a projective polytope is simply the image of a triangulation of the
corresponding cone.
E Monomial parametrizations of polytopes
We shall use the language of oriented matroids, reviewed in Appendix I.
To simplify the notation, we set r = m+1 in this section. It is convenient to work with
cones instead of polytopes. Let z1, . . . , zn∈ Rr and Z1, . . . , Zn∈ Rr be vectors spanning
Rr, and assume that the cone C = Cone(Z) spanned by Zi is pointed. Assume that z and
Z deﬁne the same oriented matroid M, that is,
⟨zi1··· zir⟩ and⟨Zi1··· Zir⟩ have the same sign. (E.1)
Let a· b denote the standard inner product of vectors a, b∈ Rr. Consider the map φ :
Rr→ Rr given by
φ(u) =
n∑
i=1
ezi·uZi. (E.2)
Theorem E.1. The map φ is a diﬀeomorphism of Rr onto the interior of the cone Cone(Z)
spanned by Z1, Z2, . . . , Zn.
– 109 –

<!-- page 113 -->

Before proving Theorem E.1, we ﬁrst deduce a number of corollaries. Suppose that
the zi are integer vectors. Let ˜Φ : (C∗)r→ Cr be the rational map given by
˜Φ(X) =
n∑
i=1
XziZi. (E.3)
Corollary E.2. The restriction of ˜Φ to Rr
>0 is a diﬀeomorphism of Rr
>0 with Int(C)⊂
Rr⊂ Cr.
Proof. The map ˜Φ|Rr
>0 is the composition of the map φ with the map ( x1, . . . , xr) ↦→
(log x1, . . . ,log xr).
The set of vectors z ={z1, z2, . . . , zn} is called graded if there exists a vector a∈ Qr
such that a· zi = 1 for all i. If zi = (1, z′
i) where z′
i∈ Zr−1, then clearly z is graded. Now
deﬁne a rational map Φ : ( C∗)r→ Pr−1 by
Φ(X) =
n∑
i=1
XziZi. (E.4)
Corollary E.3. The restriction of Φ to Rr−1
>0 is a diﬀeomorphism of Rr−1
>0 with Int(A)⊂
Pr−1.
Proof. Since the set z is graded, we can change coordinates so thatzi = (a, z′
i) for z′
i∈ Zr−1.
By replacing Xr with Xa
r , we may assume that a = 1, so that zi = (1, z′
i).
Use coordinates ( t, X, t) on C× Cr−1∼= Cr. Consider the map ˜Φ : Cr→ Cr given by
˜Φ(t, X) =
n∑
i=1
t1Xz′
i Zi = t
( n∑
i=1
Xz′
iZi
)
. (E.5)
Now restrict ˜Φ to Rr
>0 and apply Corollary E.2. For any t∈ R>0, the image of ˜Φ(t, X) in
Pr−1 is equal to Φ( X). Fixing t = 1, we obtain the claimed diﬀeomorphism.
We now provide two distinct proofs of E.1.
First proof of Theorem E.1. The basic structure of our argument is similar to that in [13,
p.84–85], but the details are signiﬁcantly more complicated.
The case r = 1 is straightforward. We assume that r > 1, and inductively that the
result for r− 1 is known.
Let us show that the map φ is a local isomorphism. We compute the Jacobian of the
map. This is given by the determinant of the r× r matrix
A(u) =
n∑
i=1
e⟨zi,u⟩zT
i Zi (E.6)
where zT
i is the transpose of zi. For a ﬁxed value of u∈ Rr, the vectors ez1·uz1, ez2·uz2,
. . . , ezn·uzn have the same oriented matroid M. By the Cauchy-Binet identity the deter-
minant J(u) = det(A(u)) is a sum of the products⟨ez1·uzi1··· ezn·uzir⟩⟨Zi1··· Zir⟩, over all
– 110 –

<!-- page 114 -->

1≤ i1 < i 2 <··· < ir≤ n. By our assumption (E.1), we obtain J(u) > 0. Thus φ is a
local diﬀeomorphism.
Let us next show that φ is one-to-one. It is enough to show that φ is one-to-one when
restricted to any line L ={at + b| t∈ R} in Rr. We have
φ(at + b) =
n∑
i=1
etzi·a+zi·bZi =
n∑
i=1
βietzi·aZi, (E.7)
where βi = e⟨zi,b⟩∈ R>0. The signs of the vector ( z1· a, z2· a, . . . , zn· a) is a signed cov-
ector of the oriented matroid M(z). It follows that there is a vector A∈ Rr so that
(Z1· A, Z2· A, . . . , Zn· A) has the same signs (see Proposition I.1). The one-variable func-
tion f(t) := φ(at + b)· A = ∑n
i=1 βietzi·aZi· A has positive derivative, and is thus injective.
It follows that φ itself is one-to-one.
Let us show that the image of φ contains points arbitrarily close to any point on a
facet of C. Let F be a facet of C, and after renaming let Z1, Z2, . . . , Zs be the Zi lying
in this facet. Since Z and z have the same oriented matroid, we see that z1, z2, . . . , zs are
exactly the zi lying on a facet of Cone( z). Thus there exists a∈ Rr such that z1· a =
z2· a =··· = zs· a = 0 and zi· a < 0 for i > s .
Let H = Rr−1⊂ Rr be a linear hyperplane not containing a. Thus H maps isomor-
phically onto the quotient Rr/R.a. Then for any b∈ H, we have that
φ(at + b) =
s∑
i=1
ezi·bZi +
n∑
j=s+1
βjetzj·aZj. (E.8)
We have limt→∞ φ(at+b) = ∑s
i=1 ezi·bZi, and since Z1, . . . , Zs span a pointed cone in Rr−1,
by the inductive hypothesis we know that the map φ′ : H→ F given by
φF (b) =
s∑
i=1
ezi·bZi (E.9)
is a diﬀeomorphism onto the interior of F . It follows that the image of φ contains points
arbitrarily close to any point on a facet of C.
We now argue that for each p0∈ Int(F ), the image of φ contains Bp0∩Int(C), for some
open ball Bp0 centered at p0. Let b0 = φ−1
F (p0)∈ H. There exists a neighborhood U of b0,
two positive real numbers δ > α > 0, and a vector Z∗∈ span(Zs+1, . . . , Zn) such that for
any ray I = [t0,∞)⊂ R with t0 suﬃciently large, we have that for t∈ I and b∈ U,
|φ(at + b)− (φF (b) + e−αtZ∗)| < e−δt0. (E.10)
Here, α = minj≥s+1(−zj· a), and Z∗ = ∑
j|α=−zj·a βjZj.
Let η : (Int(F ) + R>0Z∗)→ R× H be the map η(p + γZ∗) = (−(log γ)/α, φ−1
F (p)).
The composition φ′ = η◦ φ thus sends I× U to R× H. If φ′(t, b) = ( s, c), then (E.10)
implies that |t− s| < C · t0 and|b− c| < e−δt0, for some constant C. Furthermore, the
injectivity of φ implies the injectivity of φ′. Applying the following claim to appropriate
– 111 –

<!-- page 115 -->

closed (topological) balls inside I× U, we see that the image of φ′ contains [t′,∞)× U′ for
some t′ > t and U′⊂ U a neighborhood containing b0.
Claim. Suppose ¯Br⊂ Rr is a closed ball and f : ¯Br→ Rr is an injective continuous
function, smooth when restricted to either Sr−1 or Br. Then f(Sr−1) separates Rr into
two components, and f(Br) is a homemorphism onto the bounded component.
Proof of claim. The ﬁrst claim is the Jordan–Brouwer separation theorem. By the invari-
ance of domain theorem, f|Br maps Br homeomorphically to an open subset of Rr. It is
clear that the boundary of f(Br) is equal to f(Sr−1). Thus f(Br) must equal the bounded
component of Rr\ f(Sr−1).
We have thus shown that the image of φ contains a neighborhood of every point in
Int(F ) (intersected with Int( C)).
Finally, we show that φ is surjective onto the interior Int( C). Let Zi be an edge of C.
We shall show a weak form of convexity:
Claim. The image of φ intersected with any line parallel to Zi is either connected or
empty.
Proof of claim. Consider a linear projection π : Rr→ Rr−1 with kernel equal to the span of
Zi, where Zi is one of the edges of C. The images π(Z1), . . . , π(Zi−1), π(Zi+1), . . . , π(Zn)∈
Rr−1 has oriented matroidM/i, the contraction of M by i. Since Zi is an edge of C, we
have that π(C) is a pointed cone.
Let κ : Rr→ R be the map κ(u) = zi· u. Let H = ker κ be the kernel of κ. For t∈ R,
consider the function gt : H∼= Rr−1→ Rr−1 given by
gt(h) = π◦ φ(h + tzi) =
∑
j̸=i
ezj·(h+tzi)π(Zi) =
∑
j̸=i
ez′
j·h(αiπ(Zi)) (E.11)
where αi = ezj·(tzi) > 0, and z′
j∈ Rr−1∼= Rr/R.zi are the images of zj under the natural
quotient map. But the oriented matroid of z′
1, . . . , z′
i−1, z′
i+1, . . . , z′
n is equal toM/i as well,
so by the same result for r− 1 we deduce that gt maps Rr−1 bijectively onto the interior
of π(C).
For a pointp∈ Int(π(C)), the restriction of κ to (π◦φ)−1(p) is therefore a bijection, and
we deduce that (π◦ φ)−1(p) is diﬀeomorphic to R. As a consequence, for any p∈ Rr−1, the
set π((π◦ φ)−1(p)) is either connected or empty. Let S = Image(φ). Then π((π◦ φ)−1(p))
is the intersection of S with a line parallel to Zi. Varying p, we obtain the claim.
For an edge Zi of C and a point q∈ Rr, let Li(q) ={q+tZi| t∈ R} be the line through
q parallel to Zi. Let q be in the image of φ. We now show that (q−C)∩Int(C)⊂ Image(φ).
Consider the line Li(q). Let us ﬁrst suppose that L intersects C at a point p∈ Int(F ) in
the interior of a facet F . Since Image( φ) contains all points in some neighborhood of p,
and Image( φ)∩ L is connected, we see that q + tZi∈ Image(φ) for t < 0. Now suppose
that L intersects C in the interior of a face F′. First suppose F′ has one dimension less
than that of a facet. Since Image( φ) contains an open neighborhood of q, we can ﬁnd some
edge Zj of C and some ϵ such that q + ϵZj and q− ϵZj both lie in Image( φ), but now
Li(q + ϵZj) and Li(q− ϵZj) both intersect C in the interior of facets. By an induction
– 112 –

<!-- page 116 -->

on the codimension of the face F′, we obtain that ( q− C)∩ Int(C)⊂ Image(φ), for any
q∈ Image(φ).
Since Cone(z) is pointed, there exists a vector u∈ Rr such that zi· u > 0 for all i. It
follows that for any M > 0, there exists a point q∈ Image(φ) such that q = ∑s
i=1 αiZi
where αi > M for all i. It follows that Image( φ) = Int(C).
Second proof of Theorem E.1. We will prove Corollary E.2, which is equivalent. Let ˜Φ>0
denote the restriction ˜Φ|Rr
>0 : Rr
>0→ Int(C). Note that the basic ideas behind this theorem
were ﬁrst presented in the proof of Khovanskii’s theorem [48].
Let Y ∈ Int(C). We need to argue that the system of equations Y = ˜Φ>0 consists of
exactly one positive root (i.e. a root for which each component is positive).
The idea is to apply induction on the number of vertices n, starting at n = r which
is essentially trivial. For higher n, we smoothly deform the polytope to a lower vertex
polytope, and argue that the positive roots do not bifurcate throughout the deformation.
The result therefore follows from the induction hypothesis.
For convenience, let us deﬁne the function Ψ( X) := ∑n
i=1(Ci(X)− C0i)Zi, where
Y = ∑n
i=1 C0iZi for some constants C0i > 0. It therefore suﬃces to show that the system
of equations Ψ( X) = 0 contains exactly one positive root.
We ﬁrst observe that by setting any one of the variables Xa to zero, we necessarily
land on a boundary component of the polytope. It follows that no real solution X exists
that intersects ∂Rr
>0. We will use this fact later on.
For n = r, the ZI
i matrix is invertible, so it suﬃces to show that the systemCi(X) = C0i
for i = 1, . . . , n has exactly one positive root. Taking the log of both sides, we ﬁnd
r∑
a=1
zai log Xa = log C0i (E.12)
This is a linear system of equations with invertible matrix zai, and therefore has a unique
solution. Positivity of the solution is clear.
For n > r , let us introduce a new variable t and consider the system of equations
Ψ(t; X) = t(C1(X)− C01)Z1 +
n∑
i=2
(Ci(X)− C∗
0i)Zi (E.13)
We want to show that Ψ( t; X) = 0 has exactly one positive root at t = 1. At t = 0, the
induction hypothesis gives us exactly one positive root. Also, as we argued earlier, this
system does not have roots in ∂Rr
>0 (i.e. As t evolves from 0 to 1, roots will not move
through the boundary of the positive region.) Therefore it suﬃces to show that the system
does not bifurcate in the positive region as t evolves. Indeed, the toric Jacobian (i.e. the
Jacobian with respect to u) is non-vanishing.
J(t; u) = det
aI
(
Xa
∂ΨI(t; X)
∂Xa
)
= det
( n∑
i=1
C′
izT
i Zi
)
(E.14)
=
∑
1≤i1<...<ir≤n
C′
i1 . . . C′
ir⟨zi1 . . . zir⟩⟨ Zi1 . . . Zir⟩ (E.15)
– 113 –

<!-- page 117 -->

where C′
1 = tC1 and C′
i = Ci for i > 1. This Jacobian computation was essentially done in
the ﬁrst proof, but now with an extra factor of t.
It follows that the system does not bifurcate as t evolves from 0 to 1, which completes
our argument.
F The global residue theorem
We provide a very brief review of the global residue theorem (or GRT) [31], which is an
extension of Cauchy’s theorem to multiple variables. Applications of the GRT in amplitude
physics is discussed extensively in [1]. We remind the reader of the statement and provide
an intuitive reason it should be true that diﬀers from standard approaches to its proof,
which also naturally connects to the “push-forward” formula for canonical forms.
Let z ∈ Cn denote complex variables, and let g(z) and fa(z) for a = 1 , ..., n be
polynomials. Consider the roots of the system of equations
{fa(z) = 0} (F.1)
which we assume to be a ﬁnite set of isolated points zi. Furthermore, let us deﬁne the
holomorphic top form
ω := g(z)dnz∏n
a=1 fa(z) (F.2)
We deﬁne the global residue of ω at zi to be
Resziω = g(zi)
det
(
∂fa
∂zb
)
(zi)
(F.3)
where the determinant is applied on the matrix indexed by ( a, b).
The global residue theorem states the following:
Theorem F.1. (global residue theorem) The sum of all the global residues of ω vanishes
provided that (∑n
a=1 deg fa)− deg g > n . Namely,
∑
i
Resziω = 0 (F.4)
For n = 1, this is simply the statement that the sum of all residues of a holomorphic
function on the complex plane is zero, provided that there is no pole at inﬁnity.
Very often, there may be many (irreducible) polynomial factors F1, ..., FN for N≥ n
that appear in the denominator of ω:
ω = g(z)dnz∏N
A=1 FA(z)
(F.5)
In that case, we can group the the polynomials into n index subsets S1, ..., Sn that form
a partition of the index set {1, ..., N}, then let fa = ∏
A∈Sa FA(z) and apply the theorem.
The global residue theorem thereby involves summing over all the roots of any system of
– 114 –

<!-- page 118 -->

n polynomials FA1 = ... = FAn = 0 for which Aa∈ Sa for every a = 1, ..., n. It is easy to
show that the global residue at any root zi of n such polynomials looks like
Resziω = g(zi)(
det
(
∂FAa
∂zb
)∏
A̸∈{A1,...,An} FA
)
(zi)
(F.6)
The intuition behind the theorem is as follows. Let us denote by σ(ω) the sum over
all the global residues. Since σ(ω) is symmetric in the roots of the system of polynomial
equations, it must therefore be a rational function of the coeﬃcients of the polynomials
g(z) and fa(z), by a standard argument in Galois theory.
Furthermore, by applying the “pole cancellation” argument surrounding (7.76), it fol-
lows that σ(ω) has no poles anywhere. Indeed, the poles, if they exist, must appear when
the Jacobian of fa vanishes at a root zi. But similar to our argument surrounding (7.76),
the roots bifurcate in the neighborhood of zi, and the pairwise contribution cancel at lead-
ing order, thus giving no pole at the root zi. The σ(ω) must therefore be polynomial in the
coeﬃcients.
Now suppose we introduce an extra parameter t alongside the existing parameters zi so
that each polynomial fa and g becomes homogeneous, and we do so without changing the
degree of the polynomials (i.e. the highest order term in each polynomial is unaﬀected).
Now we imaging taking t→∞ in σ(ω). As t becomes large, the roots zi also become large
like O(t). Each global residue (F.3) must therefore scale like O(t−(∑
a degfa−degg−n)). It
follows that
σ(ω)∼ O(t−(∑
a degfa−degg−n)) (F.7)
which by assumption is a strictly negative power. It follows that σ(ω) must vanish, which
completes our argument.
G The canonical form of a toric variety
We follow the notation in [13]. Fix a lattice N∼= Zm and its dual lattice M = N∨. Let
σ be a pointed rational polyhedral cone in the vector space NQ∼= N⊗Z Q. Thus σ is the
cone generated by elements in N, and σ does not contain any line in NQ. The dual cone
σ∨⊂ MQ is given by
σ∨ ={u∈ MQ|⟨ u, v⟩≥ 0 for all v∈ σ}. (G.1)
For example, if σ ={0}, then σ∨ = MQ. The cone σ∨ is pointed if and only if σ is
d-dimensional.
The semigroup Sσ is the set σ∨∩ M, endowed with the multiplication inherited from
M. The semigroup algebra C[Sσ] is the commutative ring generated by symbols χu for
u∈ Sσ, and multiplication given by χu·χu′
= χu+u′
. The element χ0 is the identity element
of C[Sσ]. By deﬁnition, the spectrum Spec( C[Sσ]) is a (normal) aﬃne toric variety Aσ.
A fan ∆ in N is a ﬁnite set of pointed rational polyhedral cones σ in NQ such that
– 115 –

<!-- page 119 -->

1. Each face of a cone in ∆ is also in ∆;
2. The intersection of two cones in ∆ is a face of each.
By gluing the aﬃne toric varieties {Aσ | σ∈ ∆}, one obtains the normal toric variety
X(∆) associated to the fan ∆.
The toric variety X(∆) contains a dense algebraic torus:
T = (C∗)m = Spec(C[x±1
1 , . . . , x±1
m ])
We deﬁne a rational top-degree form Ω ∆ on X(∆) as the push-forward of the canonical
form
ΩT = dx1
x1
∧···∧ dxm
xm
(G.2)
on T . If we change coordinates on T , the canonical form Ω ∆ will change by±1. To ﬁx a
choice of sign, we ﬁx an orientation on MQ. If σ∨ is a full-dimensional cone in MQ and
τ∨⊂ σ∨ is a face of σ∨, then the orientation on MQ naturally induces an orientation on
the linear span span( τ∨).
The toric divisors Di of X∆ are indexed by the edges or one-dimensional cones τi of the
fan ∆ ([13, Section 3.3]). The divisor Di is the toric variety X(∆′) where ∆′∈ NQ/span(τi)
is the image of the fan ∆.
Proposition G.1. The canonical form Ω∆ has a simple pole along each toric divisor and
no other poles. The residue ResDΩ∆ along a toric divisor is equal to the canonical form of
the divisor D.
Proof. The toric variety X(∆) is the union of the dense torus T ⊂ X(∆) and its toric
divisors. Since Ω ∆|T = ΩT has no poles in T , the only poles are along the toric divisors.
Let the toric divisor D correspond to the edge τ of ∆. The rational forms Ω ∆ and
ResDΩ∆ are determined by their restriction to any open subset (for example, the dense
torus). We may thus replace X(∆) by an open aﬃne toric subvariety that contains a dense
subset of D. So we can and will assume that ∆ consists of the two cones {0} and τ, so
X(∆) = Aτ. After a change of basis of N, we may assume that τ = span(em) is the span
of the last basis vector. Thus Aτ∼= (C∗)m−1× C and D∼= (C∗)m−1×{ 0}⊂ Aτ. We have
Resxm=0
(dx1
x1
∧···∧ dxm
xm
)
= dx1
x1
∧···∧ dxm−1
xm−1
= ΩD (G.3)
the canonical form of the toric divisor D.
H Canonical form of a polytope via toric varieties
The aim of this section is to prove Theorem 7.12.
We shall use the following result roughly stating that taking residues and pushing
forward commute.
– 116 –

<!-- page 120 -->

Proposition H.1 ([51, Proposition 2.5]) . Suppose that f : M → N is a proper and
surjective map of complex manifolds of the same dimension. Let η be a meromorphic form
with only ﬁrst order poles on a smooth hypersurface V . Suppose that f(V ) is a smooth
hypersurface in N. Then f∗η has ﬁrst order poles on f(V ) and
Resf(V )f∗η = f∗ResV η. (H.1)
Let X′ := X(z) and let Ω′ := π∗(ΩX′). We shall check that Ω ′ satisﬁes the recursive
deﬁning property of the canonical form Ω( A). The statement is trivial when m = 0. We
proceed by induction on m.
Let g : X→ X′ be a toric resolution of singularities. Thus X is a smooth complete
toric variety, and the map g has the following properties:
1. The map g restricts to an isomorphism g : T∼= T′ from the dense torus T⊂ X to
the dense torus T′⊂ X′.
2. We have g∗(ΩX) = ωX′ and g−1(ΩX′) = ΩX.
3. The boundary divisor X\ T = ⋃D⊂ X is a normal crossings divisor.
4. For every torus orbit closure V of X, the image g(V ) is a torus orbit closure of X′.
Thus if D⊂ X is an irreducible toric divisor, then either dim g(D) < dim D, or
g(D) = D′, where D′ is some toric divisor of X.
The rational map π : Pn−1→ Pm has indeterminacy locus ker( Z)⊂ Pn−1 consisting
of lines in Rn sent to 0 by the linear map Z : Rn→ Rm+1. Let ˜π = π◦ g : X→ Pm. Then
π has indeterminacy locus L ={x∈ X| g(x)∈ ker(Z)}. By elimination of indeterminacy ,
there exists a sequence of blowups fi : Xi→ Xi−1 along smooth centers Ci−1⊂ Xi−1, for
i = 1, 2, . . . , r, satisfying:
1. X0 = X,
2. the composition hi := f1◦ f2◦···◦ fi : Xi→ X0 restricts to an isomorphism over
X\ L,
3. there is a regular map πr : Xr→ Pm such that πr = π◦ hr as rational maps.
All the varieties Xi are smooth, and the maps fi are all proper and birational. The
map πr is proper and surjective.
Let ∂X denote the toric boundary of X. It is the union of the toric divisors of X. We
shall make the technical assumption that
the union of the exceptional divisor of hi with h−1
i (∂X)
is a simple normal crossings divisor.
(H.2)
See [49, p.142, Main Theorem II].
The rational form ΩX has simple poles along each irreducible toric divisor D⊂ X (see
Appendix 5.6). We now investigate the poles of h∗
r(ΩX).
Claim. The rational form h∗
r(ΩX) has simple poles along the strict transforms ˜D :=
h−1r (D∩ U) of each irreducible toric divisor D, and no other poles.
– 117 –

<!-- page 121 -->

Proof of Claim. We shall prove the statement for the form h∗
i (ΩX) on Xi, proceeding by
induction on i.
The indeterminacy locus L⊂ X is closed. We ﬁrst check that L does not contain any
torus ﬁxed point of X. It is enough to show that π : X′→ Pm is deﬁned at the torus ﬁxed
points of X′. This is clear: a torus ﬁxed point of X′ is sent by π to the point Zk∈ Pm,
where span R≥0(Zk) is an edge of the cone Cone( Z). (Since z is graded, we must have
zk̸= 0, and thus Zk̸= 0 as well.)
Let U = X\L. Then for each irreducible toric divisor of D, we have that U∩D is open
and dense in D; since ΩX has a simple pole along D, it is clear that the strict transform
h∗
i (ΩX) has a simple pole along the strict transform ˜D.
Let Ej⊂ Xj denote the (irreducible) exceptional divisor of the map fj : Xj→ Xj−1.
We denote by ˜Ej ⊂ Xi the strict transform of Ej under fj+1◦···◦ fi. Since hi is an
isomorphism away from ⋃
j≤i ˜Ej, it suﬃces to show that h∗
r(ΩX) has no pole along each
˜Ej. Since the pullback of a holomorphic form is holomorphic, we are reduced to showing
that h∗
i (ΩX) has no pole along Ei.
We now consider the blowup of Xi−1 along the smooth center Ci−1. Suppose Ci−1 lies
in the divisors ˜D1, ˜D2, . . . , ˜Dt of Xi−1 (and not in any of the other ˜Dj). By our assumption
(H.2), the ˜Dj have normal crossings, so the intersection R = ˜D1∩ ˜D2∩···∩ ˜Dt has
codimension t. The intersection U∩ (D1∩···∩ Dt) is dense in ( D1∩···∩ Dt) (since
torus ﬁxed points of X do not lie in L). Since hi−1(Ci−1)∩ U =∅, we have that Ci−1 has
codimension at least one in R.
Thus codim( Ci−1) = t + s where s≥ 1. Let p∈ Ci−1. In a neighborhood V of p in
Xi−1, we may ﬁnd local coordinates x1, x2, . . . , xt, xt+1, . . . , xt+s, y1, y2, . . . , yℓ, so that Ci−1
is cut out by the ideal generated by x1, x2, . . . , xt+s, and ˜Dj is cut out by xj for 1, 2, . . . , t.
We may thus write (using the inductive hypothesis)
h∗
i−1(ΩX) = q
x1x2··· xt
dx1∧···∧ dxt+s∧ dy1∧···∧ dyℓ (H.3)
where q is a meromorphic function whose poles do not pass through p.
The blowup B of V along Ci−1∩V has local coordinates w1, . . . , wt+s−1, xt+s, y1, . . . , yℓ,
where xi = wixt+s for i = 1, 2, . . . , t+ s− 1. The exceptional divisor is given by xt+s = 0
in these coordinates. The pullback of h∗
i−1(ΩX) to B is given by
q
w1w2··· wtxt
t+s
d(w1xt+s)∧ d(w2xt+s)∧···∧ d(wt+s−1xt+s)∧ dxt+s∧ dy1∧···∧ dyℓ
(H.4)
= xs−1
t+s q
w1w2··· wt
dw1∧ dw2∧···∧ dwt+s−1∧ dxt+s∧ dy1∧···∧ dyℓ. (H.5)
Since s− 1≥ 0, the blowup B has no pole (but sometimes a zero) along the exceptional
divisor. This completes the proof of the claim.
Let Di be an irreducible toric divisor of X and ˜Di⊂ Xr its strict transform. Suppose
that g(Di) is a divisor in X′. Then π(Di) is the linear subspace of Pm spanned by some
– 118 –

<!-- page 122 -->

face F of the polytopeA. Apply Proposition H.1 with the choice f = πr and with M, N, V
being appropriate open subsets of Xr, Pm, and ˜Di respectively. We compute
Resπ(Di) Ω′ = Resπr( ˜Di)(πr)∗(h−1
r (ΩX))
= (πr)∗Res ˜Di
(h−1
r (ΩX)) by Proposition H.1,
= ˜π∗ResDiΩX hr is an isomorphism over a dense subset of Di,
= ˜π∗ΩDi by Proposition G.1,
= π∗Ωg(Di)
= Ω(F ) by the induction hypothesis.
We have used the fact that hr restricts to an isomorphism over a dense subset of Di.
Now, if Di is such that codim g(Di)≥ 2, then ˜Di clearly cannot contribute to poles
of Ω′ = (πr)∗(h−1
r (ΩX)). The claim above states that the only poles of h−1
r (ωX) are along
the ˜Di, so we conclude that the only poles of Ω′ are along linear subspaces spanned by the
faces ofA. We conclude that Ω′ = Ω(A).
I Oriented matroids
A basic reference for oriented matroids is [50]. Let v1, v2, . . . , vn∈ Rk be a collection of
vectors. The oriented matroidM =M(v) keeps track of the (positive) linear dependencies
between this set of vectors. If α∈ R, we let sign( α) = + , 0,− depending on whether
α > 0, α = 0, or α < 0.
Chirotope. The chirotope ofM is given by the function χ :{1, 2, . . . , n}k →{ +, 0,−}
speciﬁed by
χ(i1, i2, . . . , ik) := sign⟨vi1vi2··· vik⟩. (I.1)
Signed vectors. Deﬁne the space of linear dependencies D(v)⊂ Rn by
D(v) :={(a1, a2, . . . , an)∈ Rn|
n∑
i=1
aivi = 0}. (I.2)
The set of signed vectors of the oriented matroidM is the set sign( D(v)).
Signed covectors. Deﬁne the space of value vectors V (v)⊂ Rn by
V (v) :={(c· v1, . . . , c· vn)∈ Rn| c∈ Rk}. (I.3)
The set of signed covectors of the oriented matroidM is the set sign( V (v)).
Proposition I.1. Any one of (a) the chirotope, (b) the signed vectors, and (c) the signed
covectors, of an oriented matroid M determines the other two.
Given the oriented matroidM =M(v) and an index i∈{ 1, 2, . . . , n}, we can consider
the deletionM\i, which is the oriented matroid associated to v1, v2, . . . , ˆvi, . . . , vn. We also
have the contractionM/i which is the oriented matroid associated to ¯v1, ¯v2, . . . , ˆvi, . . . ,¯vn,
where ¯vj is the projection of vj∈ V to a linear hyperplane H⊂ V which does not containvi.
A basic result is that M\i andM/i depend only onM and not on the vectors v1, . . . , vn.
– 119 –

<!-- page 123 -->

J The Tarski-Seidenberg theorem
A semialgebraic subset of Rn is a ﬁnite union of sets that are cut out by ﬁnitely many
polynomial equations p(x) = 0 and ﬁnitely many polynomial inequalities q(x) > 0. Let
π : Rn → Rn−1 be the projection map that forgets the last coordinate. The Tarski-
Seidenberg theorem states that if S ⊂ Rn is a semialgebraic set, then so is π(S). We
now explain why this implies that the Amplituhedron, and more generally, any Grassmann
polytope is semialgebraic.
Let f : Rn→ Rm be a rational map. That is
f(x) =
(p1(x)
q1(x) , p2(x)
q2(x) , . . . , pm(x)
qm(x)
)
for polynomials pi, qi in n variables. Suppose S ⊂ Rn is a semialgebraic set such that
f is well deﬁned on S (so qi(x) is non-zero everywhere in S). We show that f(S) is
semialgebraic. Write (x, y) for a typical point in Rn× Rm. Deﬁne ΓS ={(x, y)}⊂ Rn× Rm
by the m polynomial equations
y1q1(x)− p1(x) = 0, . . . , ymqm(x)− pm(x) = 0
and the condition that x∈ S. It is clear that ΓS is semialgebraic, since the condition x∈ S
is semialgebraic. Also f(S) is equal to πm(ΓS) where πm : Rn× Rm→ Rm is the projection
to the last m factors. Thus applying the Tarski-Seidenberg theorem n times, we conclude
that f(S) is semialgebraic.
Now suppose S ⊂ Pn is semialgebraic. Thus S is a ﬁnite union of sets that are
cut out by ﬁnitely many homogeneous polynomial equations p(x) = 0 and ﬁnitely many
homogeneous polynomial inequalities q(x) > 0. Note that to make sense of the inequalities,
we ﬁrst deﬁne a semialgebraic cone in Rn+1, then we project down to Pn. Cover Pn with
n + 1 charts U0, . . . , Un each isomorphic to Rn. Then S∩ Ui is semialgebraic in Rn. Now
let g : Pn→ Pm be a rational map, and suppose g is well-deﬁned on S. Thus
g(x) = (p0(x), . . . , pm(x))
for homogeneous polynomials pi in n + 1 variables all of the same degree. Cover Pm with
charts V0, . . . , Vm, so for example V0 = (1, y1, y2, . . . , ym). Then for any i = 0, 1, . . . , n and
any j = 0, 1, . . . , m, the rational function g restricts to a rational function fij : Ui→ Vj. For
example f00(x) = ( p′
1(x)/p′
0(x), . . . , p′
m(x)/p′
0(x)) where p′(x1, . . . , xn) = p(1, x1, . . . , xn).
By the above argument, fij(Ui∩ S) is semialgebraic in Vj. Since the deﬁnition of semial-
gebraic allows ﬁnite unions, we deduce that g(S) is semialgebraic in Pm.
Now let G≥0(k, n)⊂ G(k, n) be the nonnegative Grassmannian. Embed G(k, n) inside
Pd where d =
(n
k
)
− 1. By deﬁnition G≥0(k, n) is a semialgebraic set inside Pd. Let
Z : Rn→ Rk+m be a linear map, which we assume to be of full rank. This induces a map
ZG : G(k, n)→ G(k, k + m), and also a map ZP : Pd→ Pc, where c =
(k+m
k
)
− 1. The map
ZP is in fact linear, with coeﬃcients given by minors of the matrix Z. In particular, ZP is
a rational map in the above sense, and thus ZP(G≥0(k, n)) is a semialgebraic set.
– 120 –

<!-- page 124 -->

References
[1] Arkani-Hamed, N., Cachazo, F., Cheung, C., & Kaplan, J. (2010). A duality for the S
matrix. Journal of High Energy Physics, 2010(3), 1-70.
[2] Hodges, A. Eliminating spurious poles from gauge-theoretic amplitudes. J. High Energ.
Phys. (2013) 2013: 135. doi:10.1007/JHEP05(2013)135
[3] Arkani-Hamed, N., Bourjaily, J. L., Cachazo, F., Goncharov, A. B., Postnikov, A., & Trnka,
J. (2016). Grassmannian Geometry of Scattering Amplitudes. Cambridge University Press.
[4] Arkani-Hamed, N., & Trnka, J. (2014). The amplituhedron. Journal of High Energy Physics,
2014(10), 1-33.
[5] Postnikov, A. (2006). Total positivity, Grassmannians, and networks. arXiv preprint
math/0609764.
[6] Lusztig, G. (1994). Total positivity in reductive groups. In Lie theory and geometry (pp.
531-568). Birkh¨ auser Boston.
[7] Lam, T. (2015). Totally nonnegative Grassmannian and Grassmann polytopes. arXiv
preprint arXiv:1506.00603.
[8] Arkani-Hamed, N., Hodges, A. & Trnka. Positive amplitudes in the amplituhedron. J. J.
High Energ. Phys. (2015) 2015: 30. doi:10.1007/JHEP08(2015)030
[9] Hartshorne, R. (2013). Algebraic geometry (Vol. 52). Springer Science & Business Media.
[10] Griﬃths, P. A. (1976). Variations on a theorem of Abel. Inventiones mathematicae, 35(1),
321-390.
[11] Knutson, A., Lam, T., & Speyer, D. E. (2013). Positroid varieties: juggling and geometry.
Compositio Mathematica, 149(10), 1710-1752.
[12] Scott, J. S. (2006). Grassmannians and cluster algebras. Proceedings of the London
Mathematical Society, 92(2), 345-380.
[13] Fulton, W. (1993). Introduction to toric varieties (No. 131). Princeton University Press.
[14] Sottile, F. (2002). Toric ideals, real toric varieties, and the algebraic moment map. arXiv
preprint math/0212044.
[15] Fomin, S., & Zelevinsky, A. (2002). Cluster algebras I: foundations. Journal of the American
Mathematical Society, 15(2), 497-529.
[16] Muller, G. (2013). Locally acyclic cluster algebras. Advances in Mathematics, 233(1),
207-247.
[17] Lam, T., & Speyer, D. E. (2016). Cohomology of cluster varieties. I. Locally acyclic case.
arXiv preprint arXiv:1604.06843.
[18] Rietsch, K. (1999). An algebraic cell decomposition of the nonnegative part of a ﬂag variety.
Journal of algebra, 213(1), 144-154.
[19] Knutson, A., Lam, T., & Speyer, D. E. (2014). Projections of Richardson varieties. Journal
f¨ ur die reine und angewandte Mathematik (Crelles Journal), 2014(687), 133-157.
[20] Leclerc, B. (2016). Cluster structures on strata of ﬂag varieties. Advances in Mathematics,
300, 190-228.
[21] Ziegler, G. M. (2012). Lectures on polytopes (Vol. 152). Springer Science & Business Media.
– 121 –

<!-- page 125 -->

[22] Bai, Y., He, S., & Lam, T. The amplituhedron from the one-loop Grassmannian measure. J.
High Energ. Phys. (2016) 2016: 112. doi:10.1007/JHEP01(2016)112
[23] Arkani-Hamed, N., & Trnka, J. Into the amplituhedron. J. High Energ. Phys. (2014) 2014:
182. doi:10.1007/JHEP12(2014)182
[24] Karp, S. N. (2017). Sign variation, the Grassmannian, and total positivity. Journal of
Combinatorial Theory, Series A, 145, 308-339.
[25] Arkani-Hamed, N., Thomas, H., & Trnka, J. In preparation.
[26] Britto, R., Cachazo, F., & Feng, B. (2005). New recursion relations for tree amplitudes of
gluons. Nuclear physics B, 715(1), 499-522.
[27] Arkani-Hamed, N., Bourjaily, J., Cachazo, F., Caron-Huot, S., & Trnka, J. (2011). The
all-loop integrand for scattering amplitudes in planar sym. Journal of High Energy Physics,
2011(1), 1-46.
[28] Bai, Y., & He, S. The amplituhedron from momentum twistor diagrams. J. High Energ.
Phys. (2015) 2015: 65. doi:10.1007/JHEP02(2015)065
[29] Karp, S. N., & Williams, L. K. (2016). The m= 1 amplituhedron and cyclic hyperplane
arrangements. arXiv preprint arXiv:1608.08288
[30] Arkani-Hamed, N., Bai, Y., & Lam, T. In preparation.
[31] Griﬃths, P., & Harris, J. (2014). Principles of algebraic geometry. John Wiley & Sons.
[32] Arkani-Hamed, N., Bourjaily, J., Cachazo, F., & Trnka, J. (2011). Local spacetime physics
from the Grassmannian. Journal of High Energy Physics, 2011(1), 1-20.
[33] Arkani-Hamed, N., Bourjaily, J., Cachazo, F., & Trnka, J. (2011). Uniﬁcation of residues and
Grassmannian dualities. Journal of High Energy Physics, 2011(1), 1-45.
[34] Cachazo, F., He, S., & Yuan, E. Y. Scattering in three dimensions from rational maps. J.
High Energ. Phys. (2013) 2013: 141. doi:10.1007/JHEP10(2013)141
[35] Cachazo, F., He, S., & Yuan, E. Y. (2014). Scattering equations and Kawai-Lewellen-Tye
orthogonality. Physical Review D, 90(6), 065001.
[36] Cachazo, F., He, S., & Yuan, E. Y. (2014). Scattering of massless particles in arbitrary
dimensions. Physical review letters, 113(17), 171601.
[37] Cachazo, F., He, S., & Yuan, E. Y. Scattering of massless particles: scalars, gluons and
gravitons. J. High Energ. Phys. (2014) 2014: 33. doi:10.1007/JHEP07(2014)033
[38] Filliman, P. (1992). The volume of duals and sections of polytopes. Mathematika, 39(1),
67-80.
[39] Arkani-Hamed, N., Bourjaily, J., Cachazo, F., Hodges, A., & Trnka, J. (2012). A note on
polytopes for scattering amplitudes. Journal of High Energy Physics, 2012(4), 1-22.
[40] Peskin, M. E., Schroeder, D. V., & Martinec, E. (1995). An introduction to quantum ﬁeld
theory. Avalon Publishing.
[41] Ferro, L., Lukowski, T., Orta, A. et al. Towards the amplituhedron volume. J. High Energ.
Phys. (2016) 2016: 14. doi:10.1007/JHEP03(2016)014
[42] Brion, M., & Vergne, M. (1999, September). Arrangement of hyperplanes. I: Rational
functions and Jeﬀrey-Kirwan residue. Annales Scientiﬁques de l '´Ecole Normale Sup´ erieure
(Vol. 32, No. 5, pp. 715-741).
– 122 –

<!-- page 126 -->

[43] Batyrev, V. V., & Tschinkel, Y. (1998). Manin’s conjecture for toric varieties. Journal of
Algebraic Geometry, 7(1), 15-54.
[44] Ziegler, G. M. (2008). Nonrational conﬁgurations, polytopes, and surfaces. The
Mathematical Intelligencer, 30(3), 36-42.
[45] Aomoto, K. (1982). Addition theorem of Abel type for hyper-logarithms. Nagoya
Mathematical Journal, 88, 55-71.
[46] Arkani-Hamed, N., & Yuan, E. In preparation.
[47] Ferro, L., Lukowski, T., Meneghelli, C. et al. Spectral parameters for scattering amplitudes
inN =4 super Yang-Mills theory. J. High Energ. Phys. (2014) 2014: 94.
doi:10.1007/JHEP01(2014)094
[48] Khovanskiˇi, A. G. (1991). Fewnomials (Vol. 88). American Mathematical Society.
[49] Hironaka, H. (1964). Resolution of Singularities of an Algebraic Variety Over a Field of
Characteristic Zero: I. Annals of Mathematics, 79(1), second series, 109-203.
doi:10.2307/1970486
[50] Bj¨ orner, A., Las Vergnas, M., Sturmfels, B., White, N., & Ziegler, G. (1999). Oriented
matroids. Encyclopedia of Mathematics and Its Applications. (No. 46). Cambridge
University Press.
[51] Khesin, B., & Rosly, A. (2001). Polar homology and holomorphic bundles. Philosophical
Transactions of the Royal Society of London A: Mathematical, Physical and Engineering
Sciences, 359(1784), 1413-1427.
– 123 –