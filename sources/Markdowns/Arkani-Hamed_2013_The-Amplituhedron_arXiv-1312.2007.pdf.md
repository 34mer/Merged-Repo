Preprint typeset in JHEP style - PAPER VERSION CALT-68-2872

# **The Amplituhedron**


**Nima** **Arkani-Hamed** _[a]_ **and** **Jaroslav** **Trnka** _[b]_


_a_ _School_ _of_ _Natural_ _Sciences,_ _Institute_ _for_ _Advanced_ _Study,_ _Princeton,_ _NJ_ _08540,_ _USA_

_b_ _California_ _Institute_ _of_ _Technology,_ _Pasadena,_ _CA_ _91125,_ _USA_


Abstract: Perturbative scattering amplitudes in gauge theories have remarkable
simplicity and hidden infinite dimensional symmetries that are completely obscured
in the conventional formulation of field theory using Feynman diagrams. This suggests the existence of a new understanding for scattering amplitudes where locality
and unitarity do not play a central role but are derived consequences from a different starting point. In this note we provide such an understanding for _N_ = 4 SYM
scattering amplitudes in the planar limit, which we identify as “the volume” of a
new mathematical object–the Amplituhedron–generalizing the positive Grassmannian. Locality and unitarity emerge hand-in-hand from positive geometry.


#### **Contents**

**1.** **Scattering** **Without** **Space-Time** **2**


**2.** **Triangles** _→_ **Positive** **Grassmannian** **5**


**3.** **Polygons** **(Tree)** **Amplituhedron** _n,k_ ( _Z_ ) **6**
_→_ _A_


**4.** **Why** **Positivity?** **8**


**5.** **Cell** **Decomposition** **10**


**6.** **“Volume”** **as** **Canonical** **Form** **12**


**7.** **The** **Superamplitude** **13**


**8.** **Hiding** **Particles** **Loop** **Positivity** **in** _G_ +( _k, n_ ; _L_ ) **15**
_→_


**9.** **The** **Amplituhedron** _n,k,L_ ( _Z_ ) **17**
_A_


**10.** **The** **Loop** **Amplitude** **Form** **18**


**11.** **Locality** **and** **Unitarity** **from** **Positivity** **21**


**12.** **Four** **Particles** **at** **All** **Loops** **23**


**13.** **Master** **Amplituhedron** **26**


**14.** **Outlook** **28**


                 - 1                  

#### **1. Scattering Without Space-Time**

Scattering amplitudes in gauge theories are amongst the most fundamental observables in physics. The textbook approach to computing these amplitudes in perturbation theory, using Feynman diagrams, makes locality and unitarity as manifest
as possible, at the expense of introducing large amounts of gauge redundancy into
our description of the physics, leading to an explosion of apparent complexity for
the computation of amplitudes for all but the very simplest processes. Over the last
quarter-century it has become clear that this complexity is a defect of the Feynman diagram approach to this physics, and is not present in the final amplitudes
themselves, which are astonishingly simpler than indicated from the diagrammatic
expansion [1–7].

This has been best understood for maximally supersymmetric gauge theories in
the planar limit. Planar _N_ = 4 SYM has been used as a toy model for real physics in
many guises, but as toy models go, its application to scattering amplitudes is closer
to the real world than any other. For instance the leading tree approximation to
scattering amplitudes is identical to ordinary gluon scattering, and the most complicated part of loop amplitudes, involving virtual gluons, is also the same in _N_ = 4
SYM as in the real world.
Planar _N_ = 4 SYM amplitudes turn out to be especially simple and beautiful, enjoying the hidden symmetry of dual superconformal invariance [8, 9], associated with a dual interpretation of scattering amplitudes as a supersymmetric Wilson
loop [10–12]. Dual superconformal symmetry combines with the ordinary conformal
symmetry to generate an infinite dimension “Yangian” symmetry [13]. Feynman diagrams conceal this marvelous structure precisely as a consequence of making locality
and unitarity manifest. For instance, the Yangian symmetry is obscured in either
one of the standard physical descriptions either as a“scattering amplitude” in one
space-time or a “Wilson-loop” in its dual.

This suggests that there must be a different formulation of the physics, where
locality and unitarity do not play a central role, but emerge as derived features from
a different starting point. A program to find a reformulation along these lines was
initiated in [14,15], and in the context of a planar _N_ = 4 SYM was pursued in [16–18],
leading to a new physical and mathematical understanding of scattering amplitudes

[19]. This picture builds on BCFW recursion relations for tree [6, 7] and loop [18,
20] amplitudes, and represents the amplitude as a sum over basic building blocks,
which can be physically described as arising from gluing together the elementary
three-particle amplitudes to build more complicated on-shell processes. These “onshell diagrams” (which are essentially the same as the “twistor diagrams” of [16,21,
22]) are remarkably connected with “cells” of a beautiful new structure in algebraic
geometry, that has been studied by mathematicians over the past number of years,
known as the positive Grassmannian [19, 23]. The on-shell building blocks can not


                 - 2                  

be associated with local space-time processes. Instead, they enjoy all the symmetries
of the theory, as made manifest by their connection with the Grassmannian–indeed,
the infinite dimensional Yangian symmetry is easily seen to follow from “positive”
diffeomorphisms [19].
While these developments give a complete understanding for the on-shell building
blocks of the amplitude, they do not go further to explain _why_ the building blocks
have to be combined in a particular way to determine the full amplitude itself. Indeed,
the particular combination of on-shell diagrams is dictated by _imposing_ that the final
result is local and unitary–locality and unitarity specify the singularity structure of
the amplitude, and this information is _used_ to determine the full integrand. This is
unsatisfying, since we want to see locality and unitarity emerge from more primitive
ideas, not merely use them to obtain the amplitude.
An important clue [17,19,24] pointing towards a deeper understanding is that the
on-shell representation of scattering amplitudes is not unique: the recursion relations
can be solved in many different ways, and so the final amplitude can be expressed as
a sum of on-shell processes in different ways as well. The on-shell diagrams satisfy
remarkable identities–now most easily understood from their association with cells
of the positive Grassmannian–that can be used to establish these equivalences. This
observation led Hodges [24] to a remarkable observation for the simplest case of
“NMHV” tree amplitudes, further developed in [25]: the amplitude can be thought
of as the volume of a certain polytope in momentum twistor space. However there
was no a priori understanding of the origin of this polytope, and the picture resisted
a direct generalization to more general trees or to loop amplitudes. Nonetheless, the
polytope idea motivated a continuing search for a geometric representation of the
amplitude as “the volume” of “some canonical region” in “some space”, somehow
related to the positive Grassmannian, with different “triangulations” of the space
corresponding to different natural decompositions of the amplitude into building
blocks.
In this note we finally realize this picture. We will introduce a new mathematical
object whose “volume” directly computes the scattering amplitude. We call this
object the “Amplituhedron”, to denote its connection both to scattering amplitudes
and positive geometry. The amplituhedron can be given a self-contained definition in
a few lines as done below in section 9. We will motivate its definition from elementary
considerations, and show how scattering amplitudes are extracted from it.
Everything flows from generalizing the notion of the “inside of a triangle in a
plane”. The first obvious generalization is to the inside of a simplex in projective
space, which further extends to the positive Grassmannian. The second generalization is to move from triangles to convex polygons, and then extend this into the
Grassmannian. This gives us the amplituhedron for tree amplitudes, generalizing
the positive Grassmannian by extending the notion of positivity to include external
kinematical data. The full amplituhedron at all loop order further generalizes the


                 - 3                  

notion of positivity in a way motivated by the natural idea of “hiding particles”.

Another familiar notion associated with triangles and polygons is their area. This
is more naturally described in a projective way by a canonical 2-form with logarithmic singularities on the boundaries of the polygon. This form also generalizes to the
full amplituhedron, and determines the (integrand of) the scattering amplitude. The
geometry of the amplituhedron is completely bosonic, so the extraction of the superamplitude from this canonical form involves a novel treatment of supersymmetry,
directly motivated by the Grassmannian structure.

The connection between the amplituhedron and scattering amplitudes is a conjecture which has passed a large number of non-trivial checks, including an understanding of how locality and unitarity arise as consequences of positivity. Our purpose in
this note is to motivate and give the complete definition of the amplituhedron and
its connection to the superamplitude in planar _N_ = 4 SYM. The discussion will be
otherwise telegraphic and few details or examples will be given. In two accompanying notes [26,27], we will initiate a systematic exploration of various aspects of the
associated geometry and physics. A much more thorough exposition of these ideas,
together with many examples worked out in detail, will be presented in [28].


**Notation**


The external data for massless _n_ particle scattering amplitudes (for an excellent
review see [29]) are labeled as _λa,_ _λ_ [˜] _a,_ ˜ _ηa_ for _a_ = 1 _, . . ., n_ . Here _λa,_ _λ_ [˜] _a_ are the
spinor-helicity variables, determining _|_ null _⟩_ momenta _p_ _[A]_ _a_ _[A]_ [˙] = _λ_ _[A]_ _a_ _[λ]_ [˜] _[A]_ _a_ [˙] [.] [The] _[η]_ [˜] _[a]_ [are] [(four)]
grassmann variables for on-shell superspace. The component of the color-stripped
superamplitude with weight 4( _k_ + 2) in the _η_ ˜’s is _Mn,k_ . We can write



_Mn,k_ ( _λa,_ _λ_ [˜] _a,_ ˜ _ηa_ ) = _[δ]_ [4][(][�]



_a_ _[λ][a][λ]_ [˜] _[a]_ [)] _[δ]_ [8][(][�]




_[λ][a]_ [)] _[δ]_ [(]

_[λ][a]_ _a_ _[λ][a][η]_ [˜] _[a]_ [)]

_n,k_ ( _za, ηa_ ) (1.1)
12 _. . ._ _n_ 1 _× M_
_⟨_ _⟩_ _⟨_ _⟩_




                       _λa_
where ( _za, ηa_ ) are the (super) “momentum-twistor” variables [24], with _za_ =
_µa_





.



The _za, ηa_ are unconstrained, and determine the _λa,_ _λ_ [˜] _a_ as



˜ ~~[1]~~ _[ a][⟩][µ][a]_ [+][1][ +] _[ ⟨][a]_ [+][1] _[ a]_ ~~[1]~~ _[⟩][µ][a]_ [ +] _[ ⟨][a a]_ [+][1] _[⟩][µ][a]_ ~~[1]~~
_λa_ =

_[⟨][a]_ _a_ ~~1~~ _a_ _a a_ +1



_,_
_⟨a_ ~~1~~ _a⟩⟨a a_ +1 _⟩_




~~[1]~~ _[ a][⟩][η][a]_ [+][1][ +] _[ ⟨][a]_ [+][1] _[ a]_ ~~[1]~~ _[⟩][η][a]_ [ +] _[ ⟨][a a]_ [+][1] _[⟩][η][a]_ ~~[1]~~
_η_ ˜ _a_ =

_[⟨][a]_ _a_ ~~1~~ _a_ _a a_ +1



(1.2)
_⟨a_ ~~1~~ _a⟩⟨a a_ +1 _⟩_



where throughout this paper, the angle brackets _⟨. . . ⟩_ denotes totally antisymmetric
contraction with an _ϵ_ tensor. _n,k_ is cyclically invariant. It is also invariant under
_M_
the little group action ( _za, ηa_ ) _ta_ ( _za, ηa_ ), so ( _za, ηa_ ) can be taken to live in P [3] _[|]_ [4] .
_→_
At loop level, there is a well-defined notion of “the integrand” for scattering
amplitudes, which at _L_ loops is a 4 _L_ form. The loop integration variables are points in


                 - 4                  

the (dual) spacetime _x_ _[µ]_ _i_ [, which in turn can be associated with] _[ L]_ [ lines in momentum-]
twistor space that we denote as ( _i_ ) for _i_ = 1 _,_ _, L_ . The 4 _L_ form is [30–32]
_L_ _· · ·_


( _za, ηa_ ; ( _i_ )) (1.3)
_M_ _L_


We can specify the line by giving two points 1( _i_ ) _,_ 2( _i_ ) on it, which we can collect as
_L_ _L_
_γ_ ( _i_ ) for _γ_ = 1 _,_ 2. can also be thought of as a 2 plane in 4 dimensions. In previous
_L_ _L_
work, we have often referred to the two points on the line 1 _,_ 2 as “ _AB_ ”, and we
_L_ _L_
will use this notation here as well.
Dual superconformal symmetry says that _n,k_ is invariant under the _SL_ (4 4)
_M_ _|_
symmetry acting on ( _za, ηa_ ) as (super)linear transformations. The full symmetry of
the theory is the Yangian of _SL_ (4 _|_ 4).

#### 2. Triangles → Positive Grassmannian


To begin with, let us start with the simplest and most familiar geometric object of
all, a triangle in two dimensions. Thinking projectively, the vertices are _Z_ 1 _[I][, Z]_ 2 _[I][, Z]_ 3 _[I]_
where _I_ = 1 _, . . .,_ 3. The interior of the triangle is a collection of points of the form


_Y_ _[I]_ = _c_ 1 _Z_ 1 _[I]_ [+] _[ c]_ [2] _[Z]_ 2 _[I]_ [+] _[ c]_ [3] _[Z]_ 3 _[I]_ (2.1)


where we span over all _ca_ with


_ca_ _>_ 0 (2.2)


More precisely, the interior of a triangle is associated with a triplet ( _c_ 1 _, c_ 2 _, c_ 3) _/GL_ (1),
with all ratios _ca/cb_ _>_ 0, so that the _ca_ are either all positive or all negative, but
here and in the generalizations that follow, we will abbreviate this by calling them


transformations, grouped into a _k × n_ matrix











 _/GL_ ( _k_ ) (2.3)



_C_ =



 _c_ 1 _. . ._ _cn_



Projective space is the special case of _G_ (1 _, n_ ). The notion of positivity giving us
the “inside of a simplex” in projective space can be generalized to the Grassmannian.
The only possible _GL_ ( _k_ ) invariant notion of positivity for the matrix _C_ requires us to
fix a particular ordering of the columns, and demand that all minors in this ordering
are positive:


_⟨ca_ 1 _. . . cak⟩_ _>_ 0 for _a_ 1 _< · · · < ak_ (2.4)

We can also talk about the very closely related space of positive matrices _M_ +( _k, n_ ),
which are just _k × n_ matrices with all positive ordered minors. The only difference
with the positive Grassmannian is that in _M_ +( _k, n_ ) we are not moding out by _GL_ ( _k_ ).
Note that while both _M_ +( _k, n_ ) and _G_ +( _k, n_ ) are defined with a given ordering
for the columns of the matrices, they have a natural cyclic structure. Indeed, if
( _c_ 1 _, . . ., cn_ ) give a positive matrix, then positivity is preserved under the (twisted)
cyclic action _c_ 1 _c_ 2 _, . . ., cn_ ( 1) _[k][−]_ [1] _c_ 1.
_→_ _→_ _−_

#### 3. Polygons (Tree) Amplituhedron n,k ( Z ) _→ A_

Another natural generalization of a triangle is to a more general polygon with _n_
vertices _Z_ 1 _[I][, . . ., Z]_ _n_ _[I]_ [.] [Once] [again] [we] [would] [like] [to] [discuss] [the] [interior] [of] [this] [region.]
However in general this is not canonically defined–if the points _Za_ are distributed
randomly, they don’t obviously enclose a region where all the _Za_ are all vertices. Only
if the _Za_ form a _convex_ polygon do we have a canonical “interior” to talk about:


_×_


Having arranged for this, the interior of the polygon is given by points of the form


_Y_ _[I]_ = _c_ 1 _Z_ 1 _[I]_ [+] _[ c]_ [2] _[Z]_ 2 _[I]_ [+] _[ . . . c][n][Z]_ _n_ _[I]_ with _ca_ _>_ 0 (3.2)


Note that this can be thought of as an interesting pairing of two different positive
spaces. We have


( _c_ 1 _, . . ., cn_ ) _G_ +(1 _, n_ ) _,_ ( _Z_ 1 _, . . ., Zn_ ) _M_ +(3 _, n_ ) (3.3)
_⊂_ _⊂_


If we jam them together to produce


_Y_ _[I]_ = _caZa_ _[I]_ (3.4)


for fixed _Za_, ranging over all _ca_ gives us all the points on the inside of the polygon,
living in _G_ (1 _,_ 3).

This object has a natural generalization to higher projective spaces; we can
consider _n_ points _Za_ _[I]_ [in] _[G]_ [(1] _[,]_ [ 1 +] _[ m]_ [),] [with] _[I]_ [= 1] _[, . . .,]_ [ 1 +] _[ m]_ [,] [which] [are] [positive]


_⟨Za_ 1 _. . . Za_ 1+ _m⟩_ _>_ 0 (3.5)


Then, the analog of the “inside of the polygon” are points of the form


_Y_ _[I]_ = _caZa_ _[I][,]_ with _ca_ _>_ 0 (3.6)


This space is very closely related to the “cyclic polytope” [33], which is the convex
hull of _n_ ordered points on the moment curve in P _[m]_, _Za_ = (1 _, ta, t_ [2] _a_ _[, . . ., t][m]_ _a_ [),] [with]
_t_ 1 _<_ _t_ 2 _<_ _tn_ . From our point of view, forcing the points to lie on the moment
_· · ·_
curve is overly restrictive; this is just one way of ensuring the positivity of the _Za_ .
We can further generalize this structure into the Grassmannian. We take positive
external data as ( _k_ + _m_ ) dimensional vectors _Za_ _[I]_ [for] _[ I]_ [= 1] _[, . . ., k]_ [ +] _[m]_ [.] [It is natural to]
restrict _n_ ( _k_ + _m_ ), so that the external _Za_ fill out the entire ( _k_ + _m_ ) dimensional
_≥_
space. Consider the space of _k_ -planes in this ( _k_ + _m_ ) dimensional space, _Y_ _⊂_
_G_ ( _k, k_ + _m_ ), with co-ordinates


_Yα_ _[I][,]_ _[α]_ [ = 1] _[, . . . k,]_ _[I]_ [= 1] _[, . . ., k]_ [ +] _[ m]_ (3.7)


We then consider a subspace of _G_ ( _k, k_ + _m_ ) determined by taking all possible “positive” linear combinations of the external data,


_Y_ = _C · Z_ (3.8)


or more explicitly


_Yα_ _[I]_ [=] _[ C][αa][Z]_ _a_ _[I]_ (3.9)


                 - 7                  

where


_Cαa_ _G_ +( _k, n_ ) _, Za_ _[I]_ (3.10)
_⊂_ _[⊂]_ _[M]_ [+][(] _[k]_ [ +] _[ m, n]_ [)]

It is trivial to see that this space is cyclically invariant if _m_ is even: under the
twisted cyclic symmetry, _Zn_ ( 1) _[k]_ [+] _[m][−]_ [1] _Z_ 1 and _cn_ ( 1) _[k][−]_ [1] _c_ 1, and the product
_→_ _−_ _→_ _−_
is invariant for even _m_ .
We call this space the generalized tree amplituhedron _n,k,m_ ( _Z_ ). The polygon is
_A_
the simplest case with _k_ = 1 _, m_ = 2. Another special case is _n_ = ( _k_ + _m_ ), where we
can use _GL_ ( _k_ + _m_ ) transformations to set the external data to the identity matrix
_Za_ _[I]_ [=] _[δ]_ _a_ _[I]_ [.] In this case _Ak_ + _m,k,m_ is identical to the usual positive Grassmannian
_G_ +( _k, k_ + _m_ ).
The case of immediate relevance to physics is _m_ = 4, and we will refer to this as
the tree amplituhedron _n,k_ ( _Z_ ). The tree amplituhedron lives in a 4 _k_ dimensional
_A_
space and is not trivially visualizable. For _k_ = 1, it is a polytope, with inequalities
determined by linear equations, while for _k_ _>_ 1, it is not a polytope and is more
“curvy”. Just to have a picture, below we sketch a 3-dimensional face of the 4
dimensional amplituhedron for _n_ = 8, which turns out to be the space _Y_ = _c_ 1 _Z_ 1 +
_. . . c_ 7 _Z_ 7 for _Za_ positive external data in P [3] :

#### **4. Why Positivity?**


We have motivated the structure of the amplituhedron by mimicking the geometric
idea of the “inside” of a convex polygon. However there is a simpler and deeper
origin of the need for positivity. We can attempt to define _Y_ = _C ·_ _Z_ with no positive
restrictions on _C_ or _Z_ . But in general, this will not be projectively meaningful, and
this expression won’t allow us to define a region in _G_ ( _k, k_ + _m_ ). The reason is that
for _n > k_ + _m_, there is always some linear combination of the _Za_ which sum to zero!
We have to take care to avoid this happening, and in order to avoid “0” on the left
hand side, we obviously need positivity properties on both the _Z_ ’s and the _C_ ’s.


                 - 8                  

It is simple and instructive to see why positivity ensures that the _Y_ = _C_ _· Z_
map is projectively well-defined. We will see this as a by-product of locating the
co-dimension one boundaries of the generalized tree amplituhedron. Let us illustrate

_⟨_ _⟩→_


compute


We can see why there is some hope for the positivity of this sum, since the _ca_ _>_ 0,
and also ordered minors of the _Z_ _[′]_ _s_ are positive. It is however obvious that if _i, j_ are
not consecutive, some of the terms in this sum will be positive, but some (where _a_ is
stuck between _i, j_ ) will be negative. But precisely when _i, j_ are consecutive, we get
a manifestly positive sum:


      _Y ZiZi_ +1 = _ca_ _ZaZiZi_ +1 _>_ 0 (4.2)
_⟨_ _⟩_ _⟨_ _⟩_

_a_


Since _ZaZiZi_ +1 _>_ 0 for _a_ = _i, i_ +1, this is manifestly positive. Thus the boundaries
_⟨_ _⟩_ _̸_
are lines ( _ZiZi_ +1) as expected.
This also tells us that the map _Y_ = _C_ _· Z_ is projectively well-defined. There
is no way to get _Y_ _→_ 0, since this would make the left hand side identically zero,
which is impossible without making all the _ca_ vanish, which is not permitted as we
we mod out by _GL_ (1) on the _ca_ .


                 - 9                  

We can extend this logic to higher _k, m_ . Let’s look at the case _m_ = 4 already for
_k_ = 1. We can investigate whether the plane ( _ZiZjZkZl_ ) is a boundary by computing

      _Y ZiZjZkZl_ = _ca_ _ZaZiZjZkZl_ (4.3)
_⟨_ _⟩_ _⟨_ _⟩_

_a_


Again, this is not in general positive. Only for ( _i, j, k, l_ ) of the form ( _i, i_ +1 _, j, j_ +1),
we have

      _Y ZiZi_ +1 _ZjZj_ +1 = _ca_ _ZaZiZi_ +1 _ZjZj_ +1 _>_ 0 (4.4)
_⟨_ _⟩_ _⟨_ _⟩_

_a_


For general even the _m_, the boundaries are when _Y_ is on the plane
( _ZiZi_ +1 _. . . Zim/_ 2 _−_ 1 _Zim/_ 2). This again shows that the _Y_ = _C_ _Z_ is projectively well
_·_
defined. The result extends trivially to general _k_, provided the positivity of _C_ is
respected. For _m_ = 4 the boundaries are again when the _k_ -plane ( _Y_ 1 _Yk_ ) is on
_· · ·_
( _ZiZi_ +1 _ZjZj_ +1), as follows from

     _⟨Y_ 1 _. . . YkZiZi_ +1 _ZjZj_ +1 _⟩_ = _⟨ca_ 1 _. . . cak⟩⟨Za_ 1 _. . . ZakZiZi_ +1 _ZjZj_ +1 _⟩_ _>_ 0 (4.5)

_a_ 1 _<···<ak_


which also shows that _Y_ is always a full rank _k_ -plane in _k_ + 4 dimensions.
The emergence of boundaries on the plane ( _ZiZi_ +1 _ZjZj_ +1) is a simple and striking consequence of positivity. We will shortly understand that the location of these
boundaries are the “positive origin” of locality from the geometry of the amplituhedron.

#### **5. Cell Decomposition**


The tree amplituhedron can be thought of as the image of the top-cell of the the
positive Grassmannian _G_ +( _k, n_ ) under the map _Y_ = _C_ _Z_ . Since dim _G_ ( _k, k_ + _m_ ) =
_·_
_mk_ _≤_ dim _G_ ( _k, n_ ) = _k_ ( _n −_ _k_ ) for _n_ _≥_ _k_ + _m_, this is in general a highly redundant
map. We can already see this in the simplest case of the polygon, which lives in
2 dimensions, while the _ca_ span an ( _n_ 1) dimensional space. The non-redundant
_−_
maps into _G_ ( _k, k_ + _m_ ) can only come from the _m_ _k_ dimensional “cells” of _G_ +( _k, n_ ).
_×_
For the polygon, these are the cells we can label as ( _i, j, k_ ), where all but ( _ci, cj, ck_ )
are non-vanishing. The image of these cells in the _Y_ -space are of course just the
triangles with vertices at _Zi, Zj, Zk_, which lie inside the polygon.
The union of all these triangles covers the inside of the polygon. However, we can
also cover the inside of the polyon more nicely with non-overlapping triangles, giving
a triangulation. Said in a heavy-handed way, we find a collection of 2 dimensional
cells of _G_ +(1 _, n_ ), so that their images in _Y_ space are non-overlapping except on
boundaries, and collectively cover the entire polygon. Of course these collections


                 - 10                  

which we can write as

     
(1 _i i_ +1) (5.1)

_i_


Sticking with _k_ = 1 but moving to _m_ = 4, the four-dimensional cells of _G_ +(1 _, n_ )
are labeled by five non-vanishing _c_ ’s ( _ci, cj, ck, cl, cm_ ). While it is harder to visualize,
one can easily show algebraically that the above simple triangulation of the polygon
generalizes to

     
(1 _i i_ +1 _j j_ +1) (5.2)

_i<j_


This expression is immediately recognizable to physicists familiar with scattering
amplitudes in _N_ = 4 SYM. If the ( _i, j, k, l, m_ ) are interpreted as “R-invariants”, this
expression is one of the canonical BCFW representations of the _k_ = 1 “NMHV” tree
amplitudes. In the positive Grassmannian representation for amplitudes [17,19], Rinvariants are precisely associated with the corresponding four-dimensional cells of
_G_ (1 _, n_ ).
For general _k_, _m_ any _m_ _k_ dimensional cell of _G_ +( _k, n_ ) maps under _Y_ = _C_ _Z_ into
_×_ _·_
some region or cell in _G_ ( _k, k_ + _m_ ). Said more explicitly, consider an _m×k_ dimensional
cell Γ of the _G_ +( _k, n_ ), with “positive co-ordinates” _C_ [Γ] ( _α_ 1 [Γ] _[, . . ., α]_ _m_ [Γ] _×k_ [)] [[19].] [Putting]
_Y_ = _C_ ( _α_ ) _·Z_ and scanning over all positive _α_ ’s, this carves out a region in _G_ ( _k, k_ + _m_ )
which is a corresponding cell Γ of the tree amplituhedron. A cell decomposition is a
collection _T_ of non-overlapping cells Γ which cover the entire amplituhedron.
The case of immediate relevance for physics is _m_ = 4. For any _k_, the BCFW
decomposition of tree amplitudes gives us a collection of 4 _×k_ dimensional cells of the
positive Grassmannian. We have performed extensive checks for high _k_ and _n_, that
for positive external _Z_, under _Y_ = _C ·_ _Z_ these cells are beautifully mapped into nonoverlapping regions of _G_ ( _k, k_ + 4) that together cover the entire tree amplituhedron.
As we have stressed, other than the desire to make the final result local and unitary,
we did not previously have a rational for thinking about this particular collection


                 - 11                  

of cells of _G_ +( _k, n_ ). Now we know what natural question this collection of cells are
answering: taken together they “cellulate” the tree amplituhedron. We will shortly
see how to directly associate the amplitude itself directly with the geometry of the
amplituhedron.

#### **6. “Volume” as Canonical Form**


Before discussing how to determine the (super)amplitude from the geometry, let us
define the notion of a “volume” associated with the amplituhedron. As should by
now be expected, we will merely generalize a simple existing idea from the world of
triangles and polygons.
The usual notion of “area” has units and is obviously not projectively meaningful.
However there is a closely related idea that is. For the triangle, we can consider a
rational 2-form in _Y_ -space, which has logarithmic singularities on the boundaries of
the triangle. This is naturally associated with positive co-ordinates for the triangle,
if we expand _Y_ = _Z_ 3 + _α_ 1 _Z_ 1 + _α_ 2 _Z_ 2, then the form is



Ω123 = _[dα]_ [1]

_α_ 1



_dα_ 2

(6.1)
_α_ 2



which can be re-written more invariantly as



Ω123 =

_[⟨]_ _Y_ _[Y dY dY]_ 12 _Y_ 23 _[ ⟩⟨]_ [123] _Y_ 31 _[⟩]_ [2]



(6.2)
_⟨Y_ 12 _⟩⟨Y_ 23 _⟩⟨Y_ 31 _⟩_



We can extend this to a form Ω _P_ for the convex polygon _P_ . The defining property
of Ω _P_ is that



Ω _P_ has logarithmic singularities on all the boundaries of _P_ .



Ω _P_ can be obtained by first triangulating the polygon in some way, then summing
the elementary two-form for each triangle, for instance as




 Ω _P_ =



Ω1 _i i_ +1 _._ (6.3)
_i_



Each term in this sum has singularities corresponding to _Y_ hitting the boundaries of
the corresponding triangle. Most of these singularities, associated with the internal
edges of the triangulation, are spurious, and cancel in the sum. Of course the full
form Ω _P_ is independent of the particular triangulation.
This form is closely related to an area, not directly of the polygon _P_, but its
dual _P_ [˜], which is also a convex polygon [25]. If we dualize so that points are mapped
to lines and lines to points, then a point _Y_ _inside P_ is mapped to a line _Y_ _outside_ _P_ [˜] .
If we write Ω _P_ = _Y d_ [2] _Y_ _V_ ( _Y_ ), then _V_ ( _Y_ ) is the area of _P_ [˜] living in the euclidean
_⟨_ _⟩_
space defined by _Y_ as the line at infinity.
This form can be generalized to the tree amplituhedron in an obvious way. We
define a rational form Ω _n,k_ ( _Y_ ; _Z_ ) with the property that


                 - 12                  

Ω _n,k_ ( _Y_ ; _Z_ ) has logarithmic singularities on all the boundaries of _n,k_ ( _Z_ ).
_A_


Just as for the polygon, one concrete way of computing Ωis to give a cell decomposition of the amplituhedron. For any cell Γ associated with positive co-ordinate
( _α_ 1 [Γ] _[, . . ., α]_ 4 [Γ] _k_ [), there is an associated form with logarithmic singularities on the bound-]
aries of the cell



Ω [Γ] _n,k_ [(] _[Y]_ [ ;] _[ Z]_ [) =]



�4 _k_


_i_ =1



_dαi_ [Γ] (6.4)
_αi_ [Γ]



For instance, consider 4 dimensional cells for _k_ = 1, associated with cells in _G_ +(1 _, n_ )
which are vanishing for all but columns _a_ 1 _, . . ., a_ 5, with positive co-ordinates
( _αa_ 1 _, . . ., αa_ 4 _, αa_ 5 = 1). Its image in _Y_ space is simply


_Y_ = _αa_ 1 _Za_ 1 + _. . . αa_ 4 _Za_ 4 + _Za_ 5 (6.5)


and the form is



_a_ 1

_. . ._ _[dα][a]_ [4]
_αa_ 1 _αa_ 4



1 2 3 4 5 (6.6)

_Y Za_ 1 _Za_ 2 _Za_ 3 _Za_ 4 _. . ._ _Y Za_ 5 _Za_ 1 _Za_ 2 _Za_ 3
_⟨_ _⟩_ _⟨_ _⟩_



_dαa_ 1




_[a]_ [4] = _⟨Y d_ [4] _Y ⟩⟨Za_ 1 _Za_ 2 _Za_ 3 _Za_ 4 _Za_ 5 _⟩_ [4]

_αa_ 4 _Y Za_ 1 _Za_ 2 _Za_ 3 _Za_ 4 _. . ._ _Y Za_ 5 _Za_ 1 _Za_



Now, given a collection of cells _T_ that cover the full amplituhedron, Ω _n,k_ ( _Y_ ; _Z_ ) is
given by

      Ω _n,k_ ( _Y_ ; _Z_ ) = Ω [Γ] _n,k_ [(] _[Y]_ [ ;] _[ Z]_ [)] (6.7)

Γ _⊂T_


As with the polygon, the form is independent of the particular cell decomposition.
Note that the definition of the amplituhedron itself crucially depends on the
positivity of the external data _Z_, and this geometry in turn determines the form Ω.
However, once this form is in hand, it can be analytically continued to any (complex!)
_Y_ and _Z_ .

#### **7. The Superamplitude**



We have already defined central objects in our story: the tree amplituhedron, together with the associated form Ωthat is loosely speaking its “volume”. The tree
super-amplitude _n,k_ can be directly extracted from Ω _n,k_ ( _Z_ ). To see how, note that
_M_
we we can always use a _GL_ (4 + _k_ ) transformation to send _Y_ _Y_ 0 as
_→_







_Y_ 0 =




04 _×k_
1 _k×k_



(7.1)



We can think of the 4 dimensional space complementary to _Y_ 0, acted on by an
unbroken _GL_ (4) symmetry, as the usual P [3] of momentum-twistor space. Accordingly,


                 - 13                  

we identify the top four components of the _Za_ with the usual bosonic momentumtwistor variables _za_ :



_za_

1
_∗_
...

_k_
_∗_








 (7.2)




_Za_ =













We still have to decide how to interpret the remaining _k_ entries of _Za_ . Clearly, if they
are normal bosonic variables, we have an infinite number of extra degrees of freedom.
It is therefore natural to try and make the remaining components infinitesimal, by
saying that some _N_ + 1’st power of them vanishes. This is equivalent to saying that
each entry can be written as



_za_
_φ_ _[A]_ 1

_[·][ η]_ [1] _[A]_
...
_φ_ _[A]_ _k_

_[·][ η][Ak]_








 (7.3)




_Za_ =













where _φ_ 1 _,...,k_ and _ηa_ are Grassmann parameters, and _A_ = 1 _, . . .,_ .
_N_
Now there is a unique way to extract the amplitude. We simply localize the form
Ω _n,k_ ( _Y_ ; _Z_ ) to _Y_ 0, and integrate over the _φ_ ’s:




           _Mn,k_ ( _za, ηa_ ) = _d_ _[N]_ _φ_ 1 _. . . d_ _[N]_ _φk_


Here _δ_ [4] _[k]_ ( _Y_ ; _Y_ 0) is a projective _δ_ function




Ω _n,k_ ( _Y_ ; _Z_ ) _δ_ [4] _[k]_ ( _Y_ ; _Y_ 0) (7.4)




           _δ_ [4] _[k]_ ( _Y_ ; _Y_ 0) = _d_ _[k][×][k]_ _ρ_ _[β]_ _α_ [det(] _[ρ]_ [)][4] _[ δ][k][×]_ [(] _[k]_ [+4)][(] _[Y]_ _α_ _[I]_ _[−]_ _[ρ]_ _α_ _[β][Y]_ 0 _[I]_ _β_ [)] (7.5)


Note that there is really no integral to perform in the second step; the delta functions
fully fix _Y_ . Any form on _G_ ( _k, k_ + 4) is of the form


Ω= _⟨Y_ 1 _. . . Ykd_ [4] _Y_ 1 _⟩_ _. . . ⟨Y_ 1 _. . . Ykd_ [4] _Yk⟩× ωn,k_ ( _Y_ ; _Z_ ) (7.6)


and our expression just says that

              _Mn,k_ ( _za, ηa_ ) = _d_ _[N]_ _φ_ 1 _. . . d_ _[N]_ _φkωn,k_ ( _Y_ 0; _Za_ ) (7.7)

Note that we can define this operation for any _N_, however, only for _N_ = 4 does
_n,k_ further have weight zero under the rescaling ( _za, ηa_ ).
_M_
This connection between the form and the super-amplitude also allows us to
directly exhibit the relation between our super-amplitude expressions and the Grassmannian formulae of [17,19]. Consider the form in _Y_ -space associated with a given


                 - 14                  

4 _k_ dimensional cell Γ of _G_ +( _k, n_ ). Then, if _Cαa_ [Γ] [(] _[α]_ [1] _[, . . ., α]_ [4] _[k]_ [) are positive co-ordinates]
1 _dα_ [Γ] 4 _k_
for the cell, and Ω [Γ] = _[dα]_ [Γ] [the] [associated] [form] [in] _[Y]_ [space,] [then] [it] [is] [easy]
_α_ [Γ] 1 _[. . .]_ _α_ [Γ] 4 _k_ [is]
to show that

   -    -    _d_ [4] _φ_ 1 _. . . d_ [4] _φk_ Ω [Γ] _δ_ [4] _[k]_ ( _Y_ ; _Y_ 0) = _dα_ 1Γ _. . ._ _[dα]_ 4 [Γ] _k_ _δ_ [4] _[k][|]_ [4] _[k]_ ( _Cαa_ ( _z_ ) _a_ ) (7.8)

_α_ 1 [Γ] _α_ 4 [Γ] _k_ _Z_


where _a_ = ( _za_ _ηa_ ) are the super momentum-twistor variabes. This is precisely the
_Z_ _|_
formula for computing on-shell diagrams (in momentum-twistor space) as described
in [17,19,34]. Thus, while the amplituhedron geometry and the associated form Ωare
purely bosonic, we have extracted from them super-amplitudes which are manifestly
supersymmetric. Indeed, the connection to the Grassmannian shows much more–the
superamplitude obtained for each cell is manifestly Yangian invariant [19].

#### 8. Hiding Particles Loop Positivity in G +( k, n ; L ) _→_


The direct generalization of “convex polygons” into the Grassmannian _G_ ( _k, k_ + 4)
has given us the tree amplituhedron. We will now ask a simple question: can we
“hide particles” in a natural way? This will lead to an extended notion of positivity
giving us loop amplitudes.

It is trivial to imagine what we might mean by hiding a single particle, but as
we will see momentarily, the idea of hiding particles is only natural if we hide _pairs_
of _adjacent_ particles. To pick a concrete example, suppose we have some positive
matrix _C_ with columns we’ll label ( _A_ 1 _, B_ 1 _,_ 1 _,_ 2 _, . . ., m, A_ 2 _, B_ 2 _, m_ + 1 _, . . . n_ ). We can
always gauge-fix the _A_ 1 _, B_ 1 and _A_ 2 _, B_ 2 columns so that the matrix takes the form



















_A_ 1 _B_ 1 1 2 _. . ._ _m_ _A_ 2 _B_ 2 _m_ + 1 _. . ._ _n_
1 0 _∗_ _∗_ _. . ._ _∗_ 0 0 _∗_ _. . ._ _∗_
0 1 _∗_ _∗_ _. . ._ _∗_ 0 0 _∗_ _. . ._ _∗_
0 0 _∗_ _∗_ _. . ._ _∗_ 1 0 _∗_ _. . ._ _∗_
0 0 _∗_ _∗_ _. . ._ _∗_ 0 1 _∗_ _. . ._ _∗_
0 0 _∗_ _∗_ _. . ._ _∗_ 0 0 _∗_ _. . ._ _∗_
... ... ... ... ... ... ... ... ... ... ...
0 0 _∗_ _∗_ _. . ._ _∗_ 0 0 _∗_ _. . ._ _∗_



















We would now like to “hide” the particles _A_ 1 _, B_ 1 _, A_ 2 _, B_ 2. We do this simply by
chopping out the corresponding columns. The remaining matrix can be grouped into
the form
 



_D_ (1)

 _D_ (2)

_C_



~~~~
 (8.1)




- 15 

But the “hidden” particles leave an echo in the positivity properties of this matrix.
The positivity of the minors involving all of ( _A_ 1 _, B_ 1 _, A_ 2 _, B_ 2), ( _A_ 2 _, B_ 2) and ( _A_ 1 _, B_ 1)
individually, as well those not involving _A_ 1 _, B_ 1 _, A_ 2 _, B_ 2 at all enforce that the ordered
maximal minors of the following matrices






~~~~
 (8.2)












- _C_ _,_




_D_ (1)

_C_



_,_




_D_ (2)

_C_



_,_





_D_ (1)

 _D_ (2)

_C_



are all positive.
We can now see why particles are most naturally hidden in pairs. If we had
instead hidden single particles as _A_ 1 _, A_ 2 _, A_ 3 _, . . ._ in separate columns, the remaining
minors would be positive or negative depending on the orderings of _A_ 1 _, A_ 2 _, A_ 3 _, . . ._,
which is additional structure over and above the cyclic ordering of the external data.
In order to avoid this arbitrariness, we should hide particles in even numbers, with
pairs the minimal case. In order to ensure that only minors involving the pairs
( _AiBi_ ) are taken into account, we mod out by the _GL_ (2) action rotating the ( _Ai, Bi_ )
columns into each other.
This “hidden particle” picture has thus motivated an extended notion of positivity associated with the Grassmannian. We are used to considering a _k_ -plane in _n_
dimensions _C_, with all ordered minors positive. But we can also imagine a collection
of _L_ 2-planes _D_ ( _i_ ) in the ( _n_ _k_ ) dimensional complement of _C_, schematically
_−_


We call this space _G_ ( _k, n_ ; _L_ ), and we will denote the collection of ( _D_ ( _i_ ) _, C_ ) as .
_C_

_D_ ( _i_ ).

way.


                 - 16                  

Extending the map _Y_ = _C.Z_ in the obvious way to include the _D_ ’s leads us to
define the full amplituhedron.

#### 9. The Amplituhedron n,k,L ( Z ) _A_

We can now give the full definition of the amplituhedron _n,k,L_ ( _Z_ ). First, the ex_A_
ternal data for _n_ _≥_ _k_ + 4 particles is given by the vectors _Za_ _[I]_ [living] [in] [a] [(4 +] _[ k]_ [)]
dimensional space; where _a_ = 1 _, . . ., n_ and _I_ = 1 _, . . .,_ 4 + _k_ . The data is positive


_⟨Za_ 1 _. . . Za_ 4+ _k⟩_ _>_ 0 for _a_ 1 _< · · · < a_ 4+ _k_ (9.1)


The amplituhedron lives in _G_ ( _k, k_ + 4; _L_ ): the space of _k_ planes _Y_ in ( _k_ + 4) dimensions, together with _L_ 2-planes ( _i_ ) in the 4 dimensional complement of _Y_,
_L_
schematically


We will denote the collection of ( ( _i_ ) _, Y_ ) as .
_L_ _Y_
The amplituhedron _n,k,L_ ( _Z_ ) is the subspace of _G_ ( _k, k_ + 4; _L_ ) consisting of all
_A_
_Y_ ’s which are a positive linear combination of the external data,

_Y_ = _C · Z_ (9.2)

More explicitly in components, the _k_ -plane is _Yα_ _[I]_ [,] [and] [the] [2-planes] [are] _[L]_ _γ_ _[I]_ ( _i_ ) [,] [where]
_γ_ = 1 _,_ 2 and _i_ = 1 _, . . ., L_ . The amplituhedron is the space of all _Y,_ ( _i_ ) of the form
_L_

_Yα_ _[I]_ [=] _[ C][αa][Z]_ _a_ _[I][,]_ _[L]_ _γ_ _[I]_ ( _i_ ) [=] _[ D][γa]_ [(] _[i]_ [)] _[Z]_ _a_ _[I]_ (9.3)


where as in the previous section the _Cαa_ specifies a _k_ -plane in _n_ -dimensions, and the
_Dγa_ ( _i_ ) are _L_ 2-planes living in the ( _n_ _k_ ) dimensional complement of _C_, with the
_−_
positivity property that for any 0 _≤_ _l ≤_ _L_, all the ordered ( _k_ + 2 _l_ ) _×_ ( _k_ + 2 _l_ ) minors
of the ( _k_ + 2 _l_ ) _× n_ matrix
 














_D_ ( _i_ 1)

.
.
.
_D_ ( _il_ )



~~~~

~~~~ (9.4)




_C_


- 17 

are positive.
The notion of cells, cell decomposition and canonical form can be extended to
the full amplituhedron. A cell Γ is associated with a set of positive co-ordinates _α_ [Γ] =
( _α_ 1 [Γ] _[, . . ., α]_ 4( [Γ] _k_ + _L_ ) [), rational in the] _[ C]_ [, such that for] _[ α]_ [’s positive,] _[ C]_ [(] _[α]_ [) = (] _[D]_ [(] _[i]_ [)][(] _[α]_ [)] _[, C]_ [(] _[α]_ [))]
is in _G_ +( _k, n_ ; _L_ ). A cell decomposition is a collection _T_ of non-intersecting cells Γ
whose images under _Y_ = _C_ _· Z_ cover the entire amplituhedron. The rational form
Ω _n,k,L_ ( ; _Z_ ) is defined by having the property that
_Y_


Ω _n,k,L_ ( _Y_ ; _Z_ ) has logarithmic singularities on all the boundaries of _n,k,L_ ( _Z_ )
_A_


A concrete formula follows from a cell decomposition as




  Ω _n,k,L_ ( ; _Z_ ) =
_Y_

Γ _⊂T_



4(� _k_ + _L_ )


_i_ =1



_dαi_ [Γ] (9.5)
_αi_ [Γ]



Of course any cell decomposition gives the same form Ω _n,k,L_ .

#### **10. The Loop Amplitude Form**


We can extract the 4 _L_ -form for the loop integrand from Ω _n,k,L_ in the obvious way.
The 2-planes ( _i_ ), being in the complement of _Y_ 0, can be taken to be non-vanishing
_L_
in the first 4 entries _L_ ( _[I]_ _i_ ) [=] [(] _[L]_ [(] _[i]_ [)2] _[×]_ [4] _[|]_ [0][2] _[×][k]_ [).] [Each] _[L][γ]_ [(] _[i]_ [)] [gives] [us] [a] [line] [(] _[L][γ]_ [=1] _[L][γ]_ [=2][)][(] _[i]_ [)]
(which we have also been calling ( _AB_ )( _i_ )) in P [3] . These are the momentum-twistor
representation of the loop integration variables. The analog of equation (7.4) for the
loop integrand form is




         _Mn,k_ ( _za, ηa_ ; _L_ ( _γ_ ( _i_ )) = _d_ [4] _φ_ 1 _. . . d_ [4] _φk_




Ω _n,k,L_ ( _Y,_ _γ_ ( _i_ ); _Z_ ) _δ_ [4] _[k]_ ( _Y_ ; _Y_ 0) (10.1)
_L_



Any form on _G_ ( _k, k_ + 4 _k_ ; _L_ ) can be written as



Ω= _Y d_ [4] _Y_ 1 _. . ._ _Y d_ [4] _Yk_
_⟨_ _⟩_ _⟨_ _⟩_




- _L_

_Y_ 1( _i_ ) 2( _i_ ) _d_ [2] 1( _i_ ) _Y_ 1( _i_ ) 2( _i_ ) _d_ [2] 2( _i_ ) _ωn,k,L_ ( _Y,_ ( _i_ ))( _Z_ )
_⟨_ _L_ _L_ _L_ _⟩⟨_ _L_ _L_ _L_ _⟩×_ _L_
_i_ =1



(10.2)
where we denoted _Y_ = _Y_ 1 _. . . Yk_ . So we have for the integrand of the all-loop amplitude




        _Mn,k_ ( _za, ηa, Lγ_ ( _i_ )) = _d_ [4] _φ_ 1 _. . . d_ [4] _φk_




- _L_

1( _i_ ) 2( _i_ ) _d_ [2] 1( _i_ ) 1( _i_ ) 2( _i_ ) _d_ [2] 2( _i_ ) _ωn,k_ ( _Y_ 0 _,_ _γ_ ( _i_ ); _Za_ )
_⟨L_ _L_ _L_ _⟩⟨L_ _L_ _L_ _⟩_ _L_
_i_ =1



(10.3)


Already the simplest case _k_ = 0 of the amplituhedron is interesting at loop level. At
1-loop, we have a 2-plane in 4 dimensions _AB_, and the _D_ matrix is just restricted to


                 - 18                  

be in _G_ +(2 _, n_ ). It is easy to see that the 4 dimensional cells of _G_ +(2 _, n_ ) are labeled
by a pair of triples [ _a, b, c_ ; _x, y, z_ ], where the top row of the matrix is non-zero in the
columns ( _a, b, c_ ) and the bottom in columns ( _x, y, z_ ). A simple collection of these


     
[1 _i i_ +1; 1 _j j_ +1] (10.4)

_i<j_


beautifully covers the amplituhedron in this case. The map into _G_ (2 _,_ 4) for each cell
is


_A_ = _Z_ 1 + _αiZi_ + _αi_ +1 _Zi_ +1 _,_ _B_ = _−Z_ 1 + _αjZj_ + _αj_ +1 _Zj_ +1 (10.5)


and so the form associated with the cell is



_dαi_

_αi_



_dαi_ +1

_αi_ +1



_αj_
_αj_



_dαj_ +1



_j_ +1 _ABd_ [2] _A_ _ABd_ [2] _B_ _AB_ (1 _i i_ +1) (1 _j j_ +1)

= _⟨_ _⟩⟨_ _⟩⟨_ _∩_ _⟩_ [2]
_αj_ +1 _AB_ 1 _i_ _AB_ 1 _i_ +1 _AB i i_ +1 _AB_ 1 _j_ _AB_ 1 _j_ +1



_⟨AB_ 1 _i⟩⟨AB_ 1 _i_ +1 _⟩⟨AB i i_ +1 _⟩⟨AB_ 1 _j⟩⟨AB_ 1 _j_ +1 _⟩⟨AB j j_ +1 _⟩_
(10.6)



The form Ωgives exactly the “Kermit” expansion for the MHV integrand given
in [18], now obtained without any reference to tree amplitudes, forward limits or
recursion relations.

In this simple case, direct triangulation of the space is straightforward. But we
could also have worked backwards, starting with the BCFW formula, and recognizing
how each term in the “Kermit” expansion is associated with positive co-ordinates for
some cell of the amplituhedron. We could then observe that, remarkably, these cells
are non-overlapping, and together cover the full amplituhedron.

In order to illustrate more of the structure of the loop amplituhedron, including
the interplay between the “ _C_ ” and “ _D_ ” matrices, let us consider the 1-loop _k_ = 1
amplitude for _n_ = 6. There are 16 terms in the BCFW recursion, which can all
be mapped back to their _Y, AB_ space form, and in turn associated with positive
co-ordinates in the amplituhedron. For instance, one of BCFW terms is


_⟨Y AB_ 13 _⟩⟨Y AB_ (561) _∩_ (2345) _⟩_ [4] _⟨Y AB_ (123) _∩_ ( _Y_ 456) _⟩_ [2]

_⟨Y_ 2345 _⟩⟨Y AB_ (561) _∩_ ( _Y_ 345) _⟩⟨Y AB_ (561) _∩_ ( _Y_ 234) _⟩⟨Y AB_ (561) _∩_ ( _Y_ 235) _⟩⟨Y AB_ 56 _⟩_
_⟨Y AB_ (561) _∩_ ( _Y_ 45(23) _∩_ ( _Y AB_ 1)) _⟩⟨Y AB_ 12 _⟩⟨Y AB_ 23 _⟩⟨Y AB_ 13 _⟩⟨Y AB_ 15 _⟩⟨Y AB_ 16 _⟩_


While it may not be immediately apparently, this is nothing but the “dlog” canonical
form associated with the following positive co-ordinates for the ( _D, C_ ) matrix












_D_

_C_







=





1 _x_ _y_ 0 0 0

 _−w_ 0 0 0 _−_ 1 _−z_
_w_ _xt_ 1 _t_ 2 + _t_ 1 _y_ _t_ 3 1 + _t_ 4 _z_


    - 19    

This exercise can be repeated with all 16 BCFW terms. The corresponding ( _D, C_ )
matrices are

- �� ��
0 0 1 _x_ _y_ 0 0 0 1 _x_ _y_ 0 0 0 1 0 _x_ + _t_ 3 _y_ _yt_ 4
0 _−t_ 1 _−t_ 2 _−_ _w_ 0 _zt_ 3 _zt_ 4 0 0 _−w_ 0 _z_ + _t_ 3 _t_ 4 0 _−t_ 1 _w_ _−z_ _−_ _t_ 2 _w_ 0 _t_ 3 _t_ 4
1 _t_ 1 _t_ 2 0 _t_ 3 _t_ 4 1 _t_ 1 _t_ 2 0 _t_ 3 _t_ 4 1 _t_ 1 _t_ 2 0 _t_ 3 _t_ 4



��
0 0 1 _x_ _y_ 0
0 0 _−w_ 0 _z_ + _t_ 3 _t_ 4
1 _t_ 1 _t_ 2 0 _t_ 3 _t_ 4



��
0 0 1 0 _x_ + _t_ 3 _y_ _yt_ 4
0 _−t_ 1 _w_ _−z_ _−_ _t_ 2 _w_ 0 _t_ 3 _t_ 4
1 _t_ 1 _t_ 2 0 _t_ 3 _t_ 4








0 0 _t_ 1 _t_ 2 + _x_ + _yw_ _y_ 0
0 0 0 _wz_ _z_ + _t_ 3 _t_ 4
1 0 _t_ 1 _t_ 2 _t_ 3 _t_ 4



��

_−_ 1 0 0 _x_ _y_ 0
_w_ 0 0 0 1 _z_
_t_ 1 _t_ 2 _t_ 3 _t_ 4 + _x_ _y_ 0



��
1 0 _−x_ _−w_ 0 0

_−_ 1 0 0 _−y_ _−z_ 0
1 + _t_ 1 _t_ 2 _t_ 3 + _xt_ 4 _y_ + _wt_ 4 _z_ 0








1 _x_ _y_ 0 0 0
_−w_ 0 0 0 _−_ 1 _−z_
_w_ _xt_ 1 _t_ 2 + _t_ 1 _y_ _t_ 3 1 + _t_ 4 _z_


_−_ 1 0 0 _x_ _y_ 0
_w_ 0 0 0 1 _z_
_t_ 1 + _w_ 0 _t_ 2 _t_ 3 + _xt_ 4 1 + _t_ 4 _y_ _z_



��
0 _t_ 2 _t_ 3 + _x_ + _yw_ _y_ 0 0
0 0 _zw_ _t_ 4 + _z_ 1 0
_t_ 1 _t_ 2 _t_ 3 _t_ 4 1 0



��

_−_ 1 0 _x_ _y_ 0 0
_w_ 0 0 0 1 _z_
_w_ + _t_ 1 _t_ 2 _t_ 3 + _xt_ 4 _yt_ 4 1 _z_







��
_x_ 1 _y_ 0 0 0
0 _w_ _z_ + _wy_ + _t_ 1 _t_ 2 0 0
1 0 _t_ 1 _t_ 2 _t_ 3 _t_ 4



��

_−_ 1 0 0 _x_ _y_ 0
_w_ 0 0 0 1 _z_
_w_ + _t_ 1 _t_ 2 _t_ 3 _t_ 4 _x_ 1 + _t_ 4 _y_ _z_








0 _x_ 1 _w_ 0 0
_−z_ _−y_ 0 0 _−_ 1 0
_z_ (1 + _t_ 1) _y_ _t_ 2 _wt_ 2 + _t_ 3 1 + _t_ 1 + _t_ 4 0



��

_−_ 1 0 _−x_ _−y_ 0 0
_w_ 0 0 0 1 _z_
_w_ 0 _xt_ 1 _t_ 2 + _yt_ 1 1 + _t_ 3 + _t_ 4 _z_ (1 + _t_ 4)









_−_ 1 _−x_ _−y_ 0 0 0
_w_ 0 0 0 1 _z_
_w_ 0 _t_ 1 _t_ 2 1 + _t_ 3 + _t_ 4 _z_ (1 + _t_ 4)



��

_−_ 1 _−x_ _−y_ 0 0 0
_w_ 0 0 0 1 _z_
_w_ _t_ 1 _x_ _t_ 2 + _yt_ 1 0 1 + _t_ 3 + _t_ 4 _z_ (1 + _t_ 4)







One can easily check that for all variables positive, the bottom row of these matrices
is positive, and all the ordered 3 _×_ 3 minors are also positive. For any cell, we can
range over all the positive variables, which under the _Y_ = _C_ _· Z_ gives an image of
the cell in ( _Y, AB_ ) space. Remarkably, we find that these cells are non-overlapping,
and cover the entire space. This can be checked directly in a simple way. We begin
by fixing positive external data ( _Z_ 1 _,_ _, Z_ 6). We then choose any positive matrix
_· · ·_
_C_ at random, which gives an associated point _Y_ inside the amplituhedron. We can
ask whether or not this point is contained in one of the cells, by seeing whether _Y_
can be reproduced with positive values for all eight variables of the cell. Doing this
we find that every point in the amplituhedron is contained in just one of these cells
(except of course for points on the common boundaries of different cells). The cells
taken together therefore give a cellulation of the amplituhedron.
Note that the form shown above, associated with a BCFW term, has some
physical poles (like _⟨Y AB_ 12 _⟩_ ), but also many unphysical poles. The unphysical
poles are associated with boundaries of the cell that are “inside” the amplituhedron,
and not boundaries of the amplituhedron themselves. These boundaries are spurious,
and so are the corresponding poles, which cancel in the sum over all BCFW terms.
We have checked in many other examples, for higher _k_ and also at higher loops,
that ( _a_ ) BCFW terms can be expressed as canonical forms associated with cells of
the amplituhedron and ( _b_ ) these collection of cells do cover the amplituhedron.
It is satisfying to have a definition of the loop amplituhedron that lives directly
in the space relevant for loop amplitudes. This is in contrast with the approach to
computing the loop integrand using recursion relations, which ultimately traces back
to higher _k_ and _n_ tree amplitudes. Consider the simple case of the 2-loop 4-particle
amplitude. We are after a form in the space of two 2-planes ( _AB_ )1 _,_ ( _AB_ )2 in four
dimensions. The BCFW approach begins with the _k_ = 2 _, n_ = 8 tree amplitudes,


                 - 20                  

and arrives at the form we are interested in after taking two “forward limits”. But
the amplituhedron lives directly in the ( _AB_ )1 _,_ ( _AB_ )2 space, and we can find a cell
decomposition for it directly, yielding the form without having to refer to any tree
amplitudes.


We have understood how to directly “cellulate” the amplituhedron in a number
of other examples, and strongly suspect that there will be a general understanding for
how to do this. The BCFW decomposition of tree amplitudes seems to be associated
with particularly nice, canonical cellulations of the tree amplituhedron. Loop level
BCFW also gives a cell decomposition. The “direct” cellulations we have found
in many cases are however simpler, without an obvious connection to the BCFW
expansion.


Locality and unitarity are encoded in the positive geometry of the amplituhedron

_ZiZi_ +1 _ZjZj_ +1 0; in the loop-level integrand, we can also have poles of the
_⟨_ _⟩→_
form _AB i i_ +1 0, and _AB_ ( _i_ ) _AB_ ( _j_ ) 0. Unitarity is reflected in what happens
_⟨_ _⟩→_ _⟨_ _⟩→_
as poles are approached, schematically we have [19]


Given the connection between the form Ω _n,k,L_ and the amplitude, it is obvious
that the first (co-dimension one) poles of the amplitude are associated with the codimension one “faces” of the amplituhedron. For trees, we have already seen that, remarkably, positivity forces these faces to be precisely where _⟨Y_ 1 _. . . YkZiZi_ +1 _ZjZj_ +1 _⟩→_
0, exactly as needed for locality. The analog statement for the full loop amplituhedron also obviously includes _Y_ 1 _YkAB i i_ +1 0.
_⟨_ _· · ·_ _⟩→_

The factorization properties of the amplitude also follow directly as a consequence of positivity. For instance, let us consider the boundary of the tree amplituhedron where the _k_ plane ( _Y_ 1 _. . . Yk_ ) is on the plane ( _ZiZi_ +1 _ZjZj_ +1). We can
e.g. assume that _Y_ 1 is a linear combination of ( _Zi, Zi_ +1 _, Zj, Zj_ +1), and thus that the
top row of the _C_ matrix is only non-zero in these columns. But then, positivity


                 - 21                  

remarkably forces the _C_ matrix to “factorize” in the form














 _k↑R_
_↓_



_i_ _i_ + 1 _j_ _j_ + 1



_↑_
_kL_
_↓_







for all possible _kL, kR_ such that _kL_ + _kR_ = _k_ 1. This factorized form of the _C_

_−_
matrix in turn implies that on this boundary, the amplituhedron does “split” into
lower-dimensional amplituhedra in exactly the way required for the factorization of
the amplitude.
We can similarly understand the single-cut of the loop integrand. Consider for
concreteness the simplest case of the _n_ particle one-loop MHV amplitude. On the
boundary where _⟨AB n_ 1 _⟩→_ 0, the _D_ matrix has the form



2 _. . ._ _n_

- [1]
1 0 _. . ._ _xn_

_−_
_y_ 1 _y_ 2 _. . ._ _yn_







The connection of this _D_ matrix to the forward limit [35] of the NMHV tree
amplitude is simple. In the language of [18], the forward limit in momentum-twistor
space is represented as


we start with the tree NMHV amplitude, associated with the positive 1 _× n_ matrix

( _yA yB y_ 1 _y_ 2 _. . ._ _yn_ ) (11.1)


and first we “add” particle _n_ + 1 between _n_ and _A_, which adds three degrees of
freedom _xn, xA, α_



_B_ 1 2 _. . ._ _n_ _n_ + 1

- _[A]_
_xA_ _αxA_ 0 0 _. . ._ _xn_ 1

_−_ _−_
_yA_ _yB_ + _αyA_ _y_ 1 _y_ 2 _. . ._ _yn_ 0


         - 22         





and we finally “merge” _n_ + 1 _,_ 1, which means shifting column 1 as _c_ 1 _c_ 1 _cn_ +1
_→_ _−_
and removing column ( _n_ + 1). This gives us the matrix



_B_ 1 2 _. . ._ _n_

- _[A]_
_xA_ _αxA_ 1 0 _. . ._ _xn_

_−_
_yA_ _yB_ + _αyA_ _y_ 1 _y_ 2 _. . ._ _yn_







note that the the _A, B_ columns have precisely four degrees of freedom _xA, α, yA, yB_
which we can remove by _GL_ (2) acting on the _A, B_ columns. Chopping off _A, B_ we
are then left precisely with the _D_ matrix on the single cut. This shows that the
single cut of the loop integrand is the forward limit of the tree amplitude, exactly as
required by unitarity.

#### **12. Four Particles at All Loops**



Let us briefly describe the simplest example illustrating the novelties of positivity at
loop level, for four-particle scattering at _L_ loops. We can parametrize each _D_ ( _i_ ) as




  1 _xi_ 0 _wi_
_D_ ( _i_ ) = _−_
0 _yi_ 1 _zi_





(12.1)



In this simple case the positivity constraints are just that all the 2 2 minors of _D_ ( _i_ )
_×_
and the 4 4 minors
_×_     -     






det




_D_ ( _i_ )
_D_ ( _j_ )



(12.2)



are positive. This translates to


_xi, yi, zi, wi_ _>_ 0 _,_ ( _xi_ _xj_ )( _zi_ _zj_ ) + ( _yi_ _yj_ )( _wi_ _wj_ ) _<_ 0 (12.3)
_−_ _−_ _−_ _−_

We can rephrase this problem in a simple, purely geometrical way by defining two
dimensional vectors _⃗ai_ = ( _xi, yi_ ) _,_ _[⃗]_ _bi_ = ( _zi, wi_ ). The points are in the upper quadrant
of the plane. The mutual positivity condition is just ( _⃗ai_ _⃗aj_ ) ( _[⃗]_ _bi_ _bj_ ) _<_ 0. Geomet_−_ _·_ _−_ _[⃗]_
rically this just means that the _⃗a,_ _[⃗]_ _b_ must be arranged so that for every pair _i, j_, the
line directed from _⃗ai_ _⃗aj_ is pointed in the opposite direction as the one directed
_→_
from _[⃗]_ _bi_ _bj_ . An example of an allowed configuration of such points for _L_ = 3 is
_→_ _[⃗]_


                 - 23                  

Finding a cell decomposition of this 4 _L_ dimensional space directly gives us the integrand for the four-particle amplitude at _L_ -loops.
Now, we know that the final form can be expressed as a sum over local, planar
diagrams. This makes it all the more remarkable that no-where in the definition
of our geometry problem do we reference to diagrams of any sort, planar or not!
Nonetheless, this property is one of many that emerges from positivity.
As we will describe at greater length in [26], it is easy to find a cell decomposition for the full space “manually” at low-loop orders. We suspect there is a more
systematic approach to understanding the geometry that might crack the problem
at all loop order. As an interesting warmup to the full problem, we can investigate
lower-dimensional “faces” of the four-particle amplituhedron. Cellulations of these
faces corresponds to computing certain cuts of the integrand, at all loop orders. We
will discuss many of these faces and cuts systematically in [26]. Here we will content
ourselves by presenting some especially simple but not completely trivial examples.
Let us start by considering an extremely simple boundary of the space, where all
the _wi_ 0. This corresponds to having all the lines intersect ( _Z_ 1 _Z_ 2). The positivity
_→_
conditions then simply become


( _xi_ _xj_ )( _zi_ _zj_ ) _<_ 0 (12.4)
_−_ _−_


which is trivial to triangulate. Whatever configuration of _x_ ’s we have are ordered in
some way, say _x_ 1 _<_ _< xL_ . Then we must have _z_ 1 _>_ _> zL_ . The _yi_ just have to
_· · ·_ _· · ·_
be positive. The associated form is then trivially (we omit the measure [�] _i_ _[dx][i][dz][i][dy][i]_ [):]



1
_. . ._ [1]
_y_ 1 _yL_



1
_x_ 1



1 1
_. . ._
_x_ 2 _x_ 1 _xL_ _xL−_ 1
_−_ _−_



1
_zL_



1 1
_. . ._ + perm _._ (12.5)
_zL−_ 1 _zL_ _z_ 1 _z_ 2
_−_ _−_



Now, this cut is particularly simple to understand from the point of view of the
familiar “local” expansions of the integrand–there is only only local diagram that
can possibly contribute to this cut: the “ladder” diagram. The corresponding cut is
precisely what we have above from positivity.


We can continue along these lines to explore faces of the amplituhedron which
determine cuts to all loop orders that are difficult (if not impossible) to derive in
any other way. For instance, suppose that some of the lines intersect ( _Z_ 1 _Z_ 2), so
that the _wi_ 0 for _i_ = 1 _, . . ., L_ 1 and others intersects ( _Z_ 3 _Z_ 4), so that _yI_ 0


for _I_ = _L_ 1 + 1 _, . . ., L_ . To pick a concrete interesting example, let choose _L_ 2

_−_
lines to intersect (12) and 2 lines to intersect (34). We can further specialize the
geometry and take more cuts by making the _L_ ’th line pass through the point 3 – this
corresponds to sending _zL_ 0. Let us also take the ( _L_ 1)’st line to pass through
_→_ _−_
the point 4 - this corresponds to sending _zL−_ 1 _, wL−_ 1 with _wL−_ 1 _/zL−_ 1 _WL−_ 1
_→∞_ _≡_
fixed.
We can again label the _xi_ ; _xI_ so they are in increasing order; then the positivity
conditions become


_x_ 1 _<_ _< xL−_ 2 _, z_ 1 _>_ _> zL−_ 2; _xL−_ 1 _< xL_ (12.6)
_· · ·_ _· · ·_

and


_WL−_ 1 _yi_ _>_ ( _xL−_ 1 _xi_ ) _,_ _wLyi_ _> zi_ ( _xi_ _xL_ ) (12.7)
_−_ _−_

This space is also trivial to triangulate, but the corresponding form is more interesting. The ordering for the _z_ ’s is associated with the form


1
_z_ ~~_L_~~ ~~2~~ ( _z_ ~~_L_~~ ~~3~~ _z_ ~~_L_~~ ~~2~~ )( _z_ ~~_L_~~ ~~4~~ _z_ ~~_L_~~ 3) _. . ._ ( _z_ 1 _z_ 2)
_−_ _−_ _−_

The interesting part of the space involves _xi, yi_ . Note that if _xi_ _<_ _xL−_ 1, the second
inequality on _yi_ is trivially satisfied for positive _yi_, and the only constraint on _yi_ is
just _yi_ _>_ ( _xL−_ 1 _xi_ ) _/WL−_ 1. If _xL−_ 1 _<_ _xi_ _<_ _xL_, then both inequalities are satisfied
_−_
and we just have _yi_ _>_ 0. Finally if _xi_ _>_ _xL_, the first inequality is trivially satisfied
and we just have _yi_ _> zi_ ( _xi_ _xL_ ) _/wL_ . Thus, given any ordering for all the _x_ _[′]_ _s_, there
_−_
is an associated set of inequalities on the _y_ ’s, and the corresponding form in _x, y_
space is trivially obtained. For instance, consider the case _L_ = 5, and an ordering
for the _x_ ’s where _x_ 1 _< x_ 4 _< x_ 2 _< x_ 5 _< x_ 3. The corresponding form in ( _x, y_ ) space is
just



1 1
_x_ 1( _x_ 4 _x_ 1)( _x_ 2 _x_ 4)( _x_ 5 _x_ 2)( _x_ 3 _x_ 5) _y_ 1 ( _x_ 4 _x_ 1) _/W_ 4
_−_ _−_ _−_ _−_ _−_ _−_



1
_y_ 2



1
_y_ 3 _z_ 3( _x_ 3 _x_ 5) _/w_ 5
_−_ _−_
(12.8)



By summing over all the possible orderings _x_ ’s, we get the final form. For general
_L_, we can simply express the result (again omitting the measure) as a sum over
permutations _σ_ :



_L_ - _−_ 2


_l_ =1




   1
( _zl_ _zl_ +1) _×_

_σ_ ; _σ_ 1 _<···<σL−_ 2

_−_



_σ_ ; _σ_ 1 _<···<σL−_ 2; _σL−_ 1 _<σL_



1
(12.9)
( _xσl−_ 1 _−_ _xσl−−_ 11 [)]




- _L_


_l_ =1



1
_wLWL−_ 1



( _yi_ ( _xL−_ 1 _xi_ ) _/WL−_ 1) _[−]_ [1] _σi_ _< σL−_ 1
_−_ _−_
_yi_ _[−]_ [1] _σL−_ 1 _< σi_ _< σL_
( _yi_ ( _xi_ _xL_ ) _zi/wL_ ) _[−]_ [1] _σL_ _< σi_
_−_ _−_


  - 25  


















_×_



_L_ - _−_ 2


_i_ =1


which cancel in the sum. This result can be checked against the cuts of the corresponding amplitudes that are available in “local form”. The diagrams that contribute
are of the type


but now there are non-trivial numerator factors that don’t trivially follow from the
structure of propagators. The full integrand is available through to seven loops in
the literature [36–40]. The inspection of the available local expansions on this cut
does not indicate an obvious all-loop generalization, nor does it betray any hint that
that the final result can be expressed in the one-line form given above. For instance
just at 5 loops, the local form of the cut is given as a sum over diagrams,


with intricate numerator factors. If all terms are combined with a common denominator of all physical propagators, the numerator has 347 terms. Needless to say, the
complicated expression obtained in this way perfectly matches the amplituhedron


We have defined the amplituhedron _n,k,L_ separately for every _n, k_ and loop order _L_ .
_A_
However, a trivial feature of the geometry is that _n,k,L_ is contained in the “faces”
_A_
of _n′,k′,L′_, for _n_ _[′]_ _>_ _n, k_ _[′]_ _>_ _k, L_ _[′]_ _>_ _L_ . The objects needed to compute scattering
_A_
amplitudes for any number of particles to all loop orders are thus contained in a
“master amplituhedron” with _n, k, L →∞_ .


                 - 26                  

In this vein it may also be worth considering natural mathematical generalizations of the amplituhedron. We have already seen that the generalized tree amplituhedron _n,k,m_ lives in _G_ ( _k, k_ + _m_ ) and can be defined for any even _m_ . It is obvious
_A_
that the amplituhedron with _m_ = 4, of relevance to physics, is contained amongst
the faces of the object defined for higher _m_ .
If we consider general even _m_, we can also generalize the notion of “hiding particles” in an obvious way: adjacent particles can be hidden in even numbers. This leads
us to a bigger space in which to embed the generalized loop amplituhedron. Instead of
just considering _G_ ( _k, k_ +4; _L_ ) of ( _k−_ planes) _Y_ together with _L_ (2 _−_ planes) in _m_ = 4
dimensional complement of _Y_, we can consider a space _G_ ( _k, k_ + _m_ ; _L_ 2 _, L_ 4 _, . . ., Lm−_ 2),
of _k_ -planes _Y_ in ( _k_ + _m_ ) dimensions, together with _L_ 2 (2-planes), _L_ 4 (4-planes),
_. . . Lm−_ 2 (( _m_ 2)-planes) in the _m_ dimensional complement of _Y_, schematically:
_−_


Once again we have _Y_ = _C · Z_, with the obvious extension of the loop positivity conditions on to _G_ ( _k, n_ ; _L_ 2 _, L_ 4 _, . . ., Lm−_ 2). We can call this space _n,k_ ; _m,L_ 2 _,...,Lm−_ 2( _Z_ ).
_C_ _A_
The _m_ = 4 amplituhedron is again just a particular face of this object. It would
be interesting to see whether this larger space has any interesting role to play in
understanding the _m_ = 4 geometry relevant to physics.


                 - 27                  

#### **14. Outlook**

This paper has concerned itself with perturbative scattering amplitudes in gauge theories. However the deeper motivations for studying this physics, articulated in [14,15]
have to do with some fundamental challenges of quantum gravity. We have long
known that quantum mechanics and gravity together make it impossible to have local observables. Quantum mechanics forces us to divide the world in two pieces–an
infinite measuring apparatus and a finite system being observed. However for any
observations made in a finite region of space-time, gravity makes it impossible to
make the apparatus arbitarily large, since it also becomes heavier, and collapses the
observation region into a black hole. In some cases like asymptotically AdS or flat
spaces, we still have precise quantum mechanical observables, that can be measured
by infinitely large apparatuses pushed to the boundaries of space-time: boundary
correlators for AdS space and the S-matrix for flat space. The fact that no precise
observables can be associated with the inside of the space-time strongly suggests that
there should be a way of computing these boundary observables without any reference to the interior space-time at all. For asymptotically AdS spaces, gauge-gravity
duality [41] gives us a wonderful description of the boundary correlators of this kind,
and gives a first working example of emergent space and gravity. However, this
duality is still an equivalence between ordinary physical systems described in standard physical language, with time running from infinite past to infinite future. This
makes the duality inapplicable to our universe for cosmological questions. Heading
back to the early universe, an understanding of emergent time is likely necessary to
make sense of the big-bang singularity. More disturbingly, even at late times, due
to the accelerated expansion of our universe, we only have access to a finite number
of degrees of freedom, and thus the division of the world into “infinite” and “finite”
systems, required by quantum mechanics to talk about precise observables, seems
to be impossible [42]. This perhaps indicates the need for an extension of quantum
mechanics to deal with subtle cosmological questions.

Understanding emergent space-time or possible cosmological extensions of quantum mechanics will obviously be a tall order. The most obvious avenue for progress
is directly attacking the quantum-gravitational questions where the relevant issues
must be confronted. But there is another strategy that takes some inspiration from
the similarly radical step taken in the transition from classical to quantum mechanics, where classical determinism was lost. There is a powerful clue to the coming
of quantum mechanics hidden in the structure of classical mechanics itself. While
Newton’s laws are manifestly deterministic, there is a completely different formulation of classical mechanics–in terms of the principle of least action–which is not
manifestly deterministic. The existence of these very different starting points leading
to the same physics was somewhat mysterious to classical physicists, but today we
know why the least action formulation exists: the world is quantum-mechanical and


                 - 28                  

not deterministic, and for this reason, the classical limit of quantum mechanics can’t
immediately land on Newton’s laws, but must match to some formulation of classical physics where determinism is not a central but derived notion. The least action
principle formulation is thus much closer to quantum mechanics than Newton’s laws,
and gives a better jumping off point for making the transition to quantum mechanics
as a natural deformation, via the path integral.
We may be in a similar situation today. If there is a more fundamental description of physics where space-time and perhaps even the usual formulation of
quantum mechanics don’t appear, then even in the limit where non-perturbative
gravitational effects can be neglected and the physics reduces to perfectly local and
unitary quantum field theory, this description is unlikely to directly reproduce the
usual formulation of field theory, but must rather match on to some new formulation
of the physics where locality and unitarity are derived notions. Finding such reformulations of standard physics might then better prepare us for the transition to the
deeper underlying theory.
In this paper, we have taken a baby first step in this direction, along the lines of
the program put forward in [14,15] and pursued in [17–19]. We have given a formulation for planar _N_ = 4 SYM scattering amplitudes with no reference to space-time or
Hilbert space, no Hamiltonians, Lagrangians or gauge redundancies, no path integrals
or Feynman diagrams, no mention of “cuts”, “factorization channels”, or recursion
relations. We have instead presented a new geometric question, to which the scattering amplitudes are the answer. It is remarkable that such a simple picture, merely
moving from “triangles” to “polygons”, suitably generalized to the Grassmannian,
and with an extended notion of positivity reflecting “hiding” particles, leads us to
the amplituhedron _n,kL_, whose “volume” gives us the scattering amplitudes for a
_A_
non-trivial interacting quantum field theory in four dimensions. It is also fascinating
that while in the usual formulation of field theory, locality and unitarity are in tension with each other, necessitating the introduction of the familiar redundancies to
accommodate both, in the new picture they emerge together from positive geometry.
A great deal remains to be done both to establish and more fully understand
our conjecture. The usual positive Grassmannian has a very rich cell structure. The
task of understanding all possible ways to make ordered _k_ _× k_ minors of a _k_ _× n_
matrix positive seems daunting at first, but the key is to realize that the “big”
Grassmannian can be obtained by gluing together (“amalgamating” [43]) “little”
_G_ (1 _,_ 3)’s and _G_ (2 _,_ 3)’s, building up larger positive matrices from smaller ones [19].
Remarkably, this extremely natural mathematical operation translates directly to the
physical picture of building on-shell diagrams from gluing together elementary threeparticle amplitudes. This story of [19] is most naturally formulated in the original
twistor space or momentum space, while the amplituhedron picture is formulated
in momentum-twistor space. At tree-level, there is a direct connection between the
cells of _G_ ( _k, n_ ) that cellulate the amplituhedron, and those of _G_ ( _k_ + 2 _, n_ ), which


                 - 29                  

give the corresponding on-shell diagram interpretation of the cell [19]. In this way,
the natural operation of decomposing the amplituhedron into pieces is ultimately
turned into a vivid on-shell scattering picture in the original space-time. Moving to
loops, we don’t have an analogous understanding of all possible cells of the extended
positive space _G_ +( _k, n_ ; _L_ )–we don’t yet know how to systematically find positive coordinates, how to think about boundaries and so on, though certainly the on-shell
representation of the loop integrand as “non-reduced” diagrams in _G_ ( _k_ + 2 _, n_ ) [19]
gives hope that the necessary understanding can be reached. Having control of the
cells and positive co-ordinates for _G_ +( _k, n_ ; _L_ ) will very likely be necessary to properly
understand the cellulation _n,k_ ; _L_ . It would also clearly be very illuminating to find
_A_
an analog of the amplituhedron, built around positive external data in the original
twistor variables.This might also shed light on the connection between these ideas
and Witten’s twistor-string theory [4,44], along the lines of [45–48].
While cell decompositions of the amplituhedron are geometrically interesting in
their own right, from the point of view of physics, we need them only as a steppingstone to determining the form Ω _n,k,L_ . This form was motivated by the idea of the
area of a (dual) polygon. For polygons, we have another definition of “area”, as
an integral, and this gives us a completely invariant definition for Ωfree of the
need for any triangulation. We do not yet have an analog of the notion of “dual
amplituhedron”, and also no integral representation for Ω _n,k,L_ . However in [27], we
will give strong circumstantial evidence that such such an expression should exist.
On a related note, while we have a simple geometric picture for the loop integrand
at any fixed loop order, we still don’t have a non-perturbative question to which the
full amplitude (rather than just the fixed-order loop integrand) is the answer.
Note that the form Ω _n,k,L_ is given directly by construction as a sum of “dlog”
pieces. This is a highly non-trivial property of the integrand, made manifest (albeit
less directly) in the on-shell diagram representation of the amplitude [19] (see also

[49,50]). Optimistically, the great simplicity of this form should allow a new picture
for carrying out the integrations and arriving at the final amplitudes. The crucial role
that positive external data played in our story suggests that this positive structure
must be reflected in the final amplitude in an important way. The striking appearance
of “cluster variables” for external data in [51] is an example of this.
We also hope that with a complete geometric picture for the integrand of the
amplitude in hand, we are now positioned to make direct contact with the explosion of progress in using ideas from integrability to determine the amplitude directly [52–55]. A particularly promising place to start forging this connection is with
the four-particle amplitude at all loop orders. As we noted, the positive geometry
problem in this case is especially simple, while the coefficient of the log [2] infrared divergence of the (log of the) amplitude gives the cusp anomalous dimension, famously
determined using integrability techniques in [56–58]. Another natural question is
how the introduction of the spectral parameter in on-shell diagrams given in [59,60]


                 - 30                  

can be realized at the level of the amplituhedron.
On-shell diagrams in _N_ = 4 SYM and the positive Grassmannian have a close
analog with on-shell diagrams in ABJM theory and the positive null Grassmannian [61], so it is natural to expect an analog of the amplituhedron for ABJM as
well. Should we expect any of the ideas in this paper to extend to other field theories, with less or no supersymmetry, and beyond the planar limit? As explained
in [19], the connection between on-shell diagrams and the Grassmannian is valid
for any theory in four dimensions, reflecting only the building-up of more complicated on-shell processes from gluing together the basic three-particle amplitudes.
The connection with the positive Grassmannian in particular is universal for any
planar theory: only the measure on the Grassmannian determining the on-shell form
differs from theory to theory. Furthermore, on-shell BCFW representations of scattering amplitudes are also widely available–at loop level for planar gauge theories,
and at the very least for gravitational tree amplitudes (where there has been much
recent progress from other points of view [62–67]). As already mentioned, one of the
crucial clues leading to the amplituhedron was the myriad of different BCFW representation of tree amplitudes, with equivalences guaranteed by remarkable rational
function identities relating BCFW terms. We have finally come to understand these
representations and identities as simple reflections of amplituhedron geometry. As
we move beyond planar _N_ = 4 SYM, we encounter even _more_ identities with this
character, such as the BCJ relations [68,69]. Indeed even sticking to planar _N_ = 4
SYM, such identities, of a fundamentally non-planar origin, give rise to remarkable
relations between amplitudes with different cyclic orderings of the external data. It
is hard to believe that these on-shell objects and the identities they satisfy only
have a geometric “triangulation” interpretation in the planar case, while the even
richer structure beyond the planar limit have no geometric interpretation at all. This
provides a strong impetus to search for a geometry underlying more general theories.
Planar _N_ = 4 SYM amplitudes are Yangian invariant, a fact that is invisible
in the conventional field-theoretic description in terms of amplitudes in one space
or Wilson loops in the dual space. We have become accustomed to such striking
facts in string theory, which has a rich spectrum of _U_ dualities, that are impossible
to make manifest simultaneously in conventional string perturbation theory. Indeed
the Yangian symmetry of planar _N_ = 4 SYM is just fermionic _T_ -duality [70]. The
amplituhedron has now given us a new description of planar _N_ = 4 SYM amplitudes
which does not have a usual space-time/quantum mechanical description, but _does_
make all the symmetries manifest. This is not a “duality” in the usual sense, since
we are not identifying an equivalence between existing theories with familiar physical interpretations. We are seeing something rather different: new mathematical
structures for representing the physics without reference to standard physical ideas,
but with all symmetries manifest. Might there be an analogous story for superstring
scattering amplitudes?


                 - 31                  

### **Acknowledgements**

We thank Zvi Bern, Jake Bourjaily, Freddy Cachazo, Simon Caron-Huot, Clifford
Cheung, Pierre Deligne, Lance Dixon, James Drummond, Sasha Goncharov, Song He,
Johannes Henn, Andrew Hodges, Yu-tin Huang, Jared Kaplan, Gregory Korchemsky,
David Kosower, Bob MacPherson, Juan Maldacena, Lionel Mason, David McGady,
Jan Plefka, Alex Postnikov, Amit Sever, Dave Skinner, Mark Spradlin, Matthias
Staudacher, Hugh Thomas, Pedro Vieira, Anastasia Volovich, Lauren Williams and
Edward Witten for valuable discussions. Our research in this area over the past many
years owes an enormous debt of gratitude to Edward Witten, Andrew Hodges, and
especially Freddy Cachazo and Jake Bourjaily, without whom this work would not
have been possible. N. A.-H. is supported by the Department of Energy under grant
number DE-FG02-91ER40654. J.T. is supported in part by the David and Ellen Lee
Postdoctoral Scholarship and by DOE grant DE-FG03-92-ER40701 and also by NSF
grant PHY-0756966.

#### **References**


[1] S. J. Parke and T. R. Taylor, Phys. Rev. Lett. **56**, 2459 (1986).


[2] Z. Bern, L. J. Dixon, D. C. Dunbar and D. A. Kosower, Nucl. Phys. B **425**, 217
(1994) [hep-ph/9403226].


[3] Z. Bern, L. J. Dixon, D. C. Dunbar and D. A. Kosower, Nucl. Phys. B **435**, 59
(1995) [hep-ph/9409265].


[4] E. Witten, Commun. Math. Phys. **252**, 189 (2004) [hep-th/0312171].


[5] F. Cachazo, P. Svrcek and E. Witten, JHEP **0409**, 006 (2004) [hep-th/0403047].


[6] R. Britto, F. Cachazo and B. Feng, Nucl. Phys. B **715**, 499 (2005) [hep-th/0412308].


[7] R. Britto, F. Cachazo, B. Feng and E. Witten, Phys. Rev. Lett. **94**, 181602 (2005)

[hep-th/0501052].


[8] L. F. Alday and J. M. Maldacena, JHEP **0706**, 064 (2007) [arXiv:0705.0303

[hep-th]].


[9] J. M. Drummond, J. Henn, V. A. Smirnov and E. Sokatchev, JHEP **0701**, 064
(2007) [hep-th/0607160].


[10] S. Caron-Huot, JHEP **1107**, 058 (2011) [arXiv:1010.1167 [hep-th]].


[11] L. J. Mason and D. Skinner, JHEP **1012**, 018 (2010) [arXiv:1009.2225 [hep-th]].


[12] L. F. Alday, B. Eden, G. P. Korchemsky, J. Maldacena and E. Sokatchev, JHEP
**1109**, 123 (2011) [arXiv:1007.3243 [hep-th]].


                 - 32                  

[13] J. M. Drummond, J. M. Henn and J. Plefka, JHEP **0905**, 046 (2009)

[arXiv:0902.2987 [hep-th]].


[14] N. Arkani-Hamed and J. Kaplan, JHEP **0804**, 076 (2008) [arXiv:0801.2385 [hep-th]].


[15] N. Arkani-Hamed, F. Cachazo and J. Kaplan, JHEP **1009**, 016 (2010)

[arXiv:0808.1446 [hep-th]].


[16] N. Arkani-Hamed, F. Cachazo, C. Cheung and J. Kaplan, JHEP **1003**, 110 (2010)

[arXiv:0903.2110 [hep-th]].


[17] N. Arkani-Hamed, F. Cachazo, C. Cheung and J. Kaplan, JHEP **1003**, 020 (2010)

[arXiv:0907.5418 [hep-th]].


[18] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, S. Caron-Huot and J. Trnka, JHEP
**1101**, 041 (2011) [arXiv:1008.2958 [hep-th]].


[19] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. B. Goncharov, A. Postnikov and
J. Trnka, arXiv:1212.5605 [hep-th].


[20] R. H. Boels, JHEP **1011**, 113 (2010) [arXiv:1008.3101 [hep-th]].


[21] A. P. Hodges and S. Huggett, Surveys High Energ. Phys. **1**, 333 (1980).


[22] A. P. Hodges, hep-th/0503060.


[23] A. Postnikov, arXiv:math/0609764.


[24] A. Hodges, JHEP **1305**, 135 (2013) [arXiv:0905.1473 [hep-th]].


[25] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. Hodges and J. Trnka, JHEP **1204**,
081 (2012) [arXiv:1012.6030 [hep-th]].


[26] N. Arkani-Hamed and J. Trnka, “Into the Amplituhedron”, to appear.


[27] N. Arkani-Hamed, A. Hodges and J. Trnka, “Three Views of the Amplituhedron”, to
appear.


[28] N. Arkani-Hamed and J. Trnka, “Scattering Amplitudes from Positive Geometry”, in
preparation.


[29] H. Elvang and Y. -t. Huang, arXiv:1308.1697 [hep-th].


[30] A. Hodges, JHEP **1308**, 051 (2013) [arXiv:1004.3323 [hep-th]].


[31] L. Mason and D. Skinner, J. Phys. A **44**, 135401 (2011) [arXiv:1004.3498 [hep-th]].


[32] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo and J. Trnka, JHEP **1206**, 125 (2012)

[arXiv:1012.6032 [hep-th]].


[33] http://en.wikipedia.org/wiki/Cyclic ~~p~~ olytope


                 - 33                  

[34] L. J. Mason and D. Skinner, JHEP **0911**, 045 (2009) [arXiv:0909.0250 [hep-th]].


[35] S. Caron-Huot, JHEP **1105**, 080 (2011) [arXiv:1007.3224 [hep-ph]].


[36] Z. Bern, M. Czakon, L. J. Dixon, D. A. Kosower and V. A. Smirnov, Phys. Rev. D
**75**, 085010 (2007) [hep-th/0610248].


[37] Z. Bern, L. J. Dixon and V. A. Smirnov, Phys. Rev. D **72**, 085001 (2005)

[hep-th/0505205].


[38] Z. Bern, J. J. M. Carrasco, H. Johansson and D. A. Kosower, Phys. Rev. D **76**,
125020 (2007) [arXiv:0705.1864 [hep-th]].


[39] J. L. Bourjaily, A. DiRe, A. Shaikh, M. Spradlin and A. Volovich, JHEP **1203**, 032
(2012) [arXiv:1112.6432 [hep-th]].


[40] B. Eden, P. Heslop, G. P. Korchemsky and E. Sokatchev, Nucl. Phys. B **862**, 450
(2012) [arXiv:1201.5329 [hep-th]].


[41] J. M. Maldacena, [hep-th/9711200].


[42] E. Witten, hep-th/0106109.


[43] V. V. Fock and A. B. Goncharov, Ann. Sci. L’Ecole Norm. Sup. (2009),
arXiv:math.AG/0311245.


[44] R. Roiban, M. Spradlin and A. Volovich, Phys. Rev. Lett. **94**, 102002 (2005)

[hep-th/0412265].


[45] L. Dolan and P. Goddard, JHEP **0912**, 032 (2009) [arXiv:0909.0499 [hep-th]].


[46] D. Nandan, A. Volovich and C. Wen, JHEP **1007**, 061 (2010) [arXiv:0912.3705

[hep-th]].


[47] N. Arkani-Hamed, J. Bourjaily, F. Cachazo and J. Trnka, JHEP **1101**, 049 (2011)

[arXiv:0912.4912 [hep-th]].


[48] J. L. Bourjaily, J. Trnka, A. Volovich and C. Wen, JHEP **1101**, 038 (2011)

[arXiv:1006.1899 [hep-th]].


[49] A. E. Lipstein and L. Mason, JHEP **1305**, 106 (2013) [arXiv:1212.6228 [hep-th]].


[50] A. E. Lipstein and L. Mason, arXiv:1307.1443 [hep-th].


[51] J. Golden, A. B. Goncharov, M. Spradlin, C. Vergu and A. Volovich,
arXiv:1305.1617 [hep-th].


[52] S. Caron-Huot and S. He, JHEP **1207**, 174 (2012) [arXiv:1112.1060 [hep-th]].


[53] B. Basso, A. Sever and P. Vieira, Phys. Rev. Lett. **111**, 091602 (2013)

[arXiv:1303.1396 [hep-th]].


                 - 34                  

[54] B. Basso, A. Sever and P. Vieira, arXiv:1306.2058 [hep-th].


[55] L. J. Dixon, J. M. Drummond, M. von Hippel and J. Pennington, arXiv:1308.2276

[hep-th].


[56] N. Beisert and M. Staudacher, Nucl. Phys. B **670**, 439 (2003) [hep-th/0307042].


[57] N. Beisert, B. Eden and M. Staudacher, J. Stat. Mech. **0701**, P01021 (2007)

[hep-th/0610251].


[58] B. Eden and M. Staudacher, J. Stat. Mech. **0611**, P11014 (2006) [hep-th/0603157].


[59] L. Ferro, T. Lukowski, C. Meneghelli, J. Plefka and M. Staudacher, arXiv:1308.3494

[hep-th].


[60] L. Ferro, T. Lukowski, C. Meneghelli, J. Plefka and M. Staudacher, Phys. Rev. Lett.
**110**, no. 12, 121602 (2013) [arXiv:1212.0850 [hep-th]].


[61] Y. -t. Huang and C. Wen, arXiv:1309.3252 [hep-th].


[62] A. Hodges, arXiv:1204.1930 [hep-th].


[63] F. Cachazo and Y. Geyer, arXiv:1206.6511 [hep-th].


[64] F. Cachazo and D. Skinner, Phys. Rev. Lett. **110**, 161301 (2013) [arXiv:1207.0741

[hep-th]].


[65] D. Skinner, arXiv:1301.0868 [hep-th].


[66] F. Cachazo, S. He and E. Y. Yuan, arXiv:1307.2199 [hep-th].


[67] F. Cachazo, S. He and E. Y. Yuan, arXiv:1309.0885 [hep-th].


[68] Z. Bern, J. J. M. Carrasco and H. Johansson, Phys. Rev. D **78**, 085011 (2008)

[arXiv:0805.3993 [hep-ph]].


[69] Z. Bern, J. J. M. Carrasco and H. Johansson, [arXiv:1004.0476 [hep-th]].


[70] N. Berkovits and J. Maldacena, JHEP **0809**, 062 (2008) [arXiv:0807.3196 [hep-th]].


                 - 35                  

