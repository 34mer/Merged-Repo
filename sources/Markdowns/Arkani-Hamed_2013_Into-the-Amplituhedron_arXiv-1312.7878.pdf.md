Preprint typeset in JHEP style - PAPER VERSION CALT-68-2873

# **Into the Amplituhedron**


**Nima** **Arkani-Hamed** _[a]_ **and** **Jaroslav** **Trnka** _[b]_


_a_ _School_ _of_ _Natural_ _Sciences,_ _Institute_ _for_ _Advanced_ _Study,_ _Princeton,_ _NJ_ _08540,_ _USA_

_b_ _California_ _Institute_ _of_ _Technology,_ _Pasadena,_ _CA_ _91125,_ _USA_


Abstract: We initiate an exploration of the physics and geometry of the amplituhedron, starting with the simplest case of the integrand for four-particle scattering in
planar _N_ = 4 SYM. We show how the textbook structure of the unitarity double-cut
follows from the positive geometry. We also use the geometry to expose the behavior
of the multicollinear limit, providing a direct motivation for studying the logarithm
of the amplitude. In addition to computing the two and three-loop integrands, we
explore various lower-dimensional faces of the amplituhedron, thereby computing
non-trivial cuts of the integrand to all loop orders.


### **Contents**

**1.** **Geometry** **and** **Physics** **of** **the** **Amplituhedron** **2**


**2.** **One** **Loop** **Geometry** **5**


**3.** **Warmup** **Exercises** **7**


**4.** **Two** **Loops** **11**


**5.** **Generalities** **on** **Cuts** **13**


**6.** **Unitarity** **from** **Positivity** **15**


**7.** **Three** **Loops** **18**


**8.** **Multi-Collinear** **Region** **19**


**9.** **Log** **of** **the** **Amplitude** **20**


**10.** **Some** **Faces** **of** **the** **Amplituhedron** **25**


**11.** **Four** **Particle** **Outlook** **30**


                 - 1                  

### **1. Geometry and Physics of the Amplituhedron**

In [1], we introduced a new geometric object–the Amplituhedron–underlying the
physics of scattering amplitudes for _N_ = 4 SYM in the planar limit. At tree level,
the amplituhedron is a natural generalization of “the inside of a convex polygon”.
Loops arise by extending the geometry to incorporate the idea of “hiding particles”
in the only natural way possible.
The amplituhedron _An,k,L_ for _n_ -particle N _[k]_ MHV amplitudes at _L_ loops, lives in
_G_ ( _k, k_ + 4; _L_ ), which is the space of _k_ -planes _Y_ in _k_ + 4 dimensions, together with
_L_ 2-planes _L_ 1 _, · · ·_ _, LL_ in the 4 dimensional complement of _Y_ . The external data
are given by a collection of _n_ ( _k_ + 4) dimensional vectors _Za_ _[I]_ [.] [Here] _[a]_ [ = 1] _[,][ · · ·][ n]_ [,] [and]
_I_ = 1 _, · · ·_ _,_ ( _k_ + 4). This data is taken to be “positive”, in the sense that all the
ordered ( _k_ + 4) _×_ ( _k_ + 4) determinants _⟨Za_ 1 _· · · Zak_ +4 _⟩_ _>_ 0 for _a_ 1 _<_ _· · ·_ _<_ _ak_ +4. The
subspace of _An,k,L_ of _G_ ( _k, k_ + 4; _L_ ) is determined by a “positive” linear combination
of the (positive) external data. The _k_ -plane is _Yα_ _[I]_ [,] [and] [the] [2-planes] [are] _[L][I]_ _γ_ ( _i_ ) [,] [where]
_γ_ = 1 _,_ 2 and _i_ = 1 _, . . ., L_ . The amplituhedron is the space of all _Y, L_ ( _i_ ) of the form


_Yα_ _[I]_ [=] _[ C][αa][Z]_ _a_ _[I][,]_ _L_ _[I]_ _γ_ ( _i_ ) [=] _[ D][γa]_ [(] _[i]_ [)] _[Z]_ _a_ _[I]_ (1.1)


where the _Cαa_ specifies a _k_ -plane in _n_ -dimensions, and the _Dγa_ ( _i_ ) are _L_ 2-planes
living in the ( _n −_ _k_ ) dimensional complement of _C_, with the positivity property that
for any 0 _≤_ _l ≤_ _L_, all the ordered maximal minors of the ( _k_ + 2 _l_ ) _× n_ matrix













_D_ ( _i_ 1)

.
.
.
_D_ ( _il_ )







 (1.2)





_C_


are positive.
There is a canonical rational form Ω _n,k_ ; _L_ associated with _An,k_ ; _L_, with the property
of having logarithmic singularities on all the lower-dimensional boundaries of _An,k_ ; _L_ .
The loop integrand form for the super-amplitude is naturally extracted from Ω _n,k_ ; _L_

[1].

The amplituhedron can be defined in a few lines, as we have just done. But the
resulting geometry is incredibly rich and intricate–as it must be, to generate all the
structure found in planar _N_ = 4 SYM scattering amplitudes to all loop orders! For
instance, the singularity structure of the amplitude is reflected in the geometry of
the various boundaries of the amplituhedron; studying this geometry in some of the
simplest cases allows us to see the emergence of locality and unitarity from positive
geometry.
Even just the tree amplituhedron generalizes the positive Grassmannian _G_ +( _k, n_ )

[2]. A complete understanding of _G_ +( _k, n_ ) revealed many surprising connections to


                 - 2                  

other structures, from the fundamentally combinatorial backbone of affine permutations, to cluster algebras, to the physical connection with on-shell processes [2–4]. It
is natural to expect the full amplituhedron _An,k,L_ to have a much richer structure. A
complete understanding of the full geometry of the amplituhedron, at the same level
as our understanding of the positive Grassmannian, will likely involve further physical and mathematical ideas. Our goal in this note is to begin laying the groundwork
for this exploration, by looking at various simple aspects of amplituhedron geometry
in the simplest non-trivial case of clear physical interest.
While the tree amplituhedron generalizes the positive Grassmannian in a direct
way, extending the notion of positivity to external data, the extension of positivity
associated with “hiding particles” which gives rise to loops is more novel and interesting. The very simplest case of four-particle scattering has _k_ = 0 _, n_ = 4. Here,
we don’t have the additional structure of Grassmann components for the external
data [1], the external data are just the ordinary bosonic momentum-twistor [5] variables _Z_ 1 _[I][, Z]_ 2 _[I][, Z]_ 3 _[I][, Z]_ 4 _[I]_ [,] [for] _[I]_ [=] [1] _[,][ · · ·]_ _[,]_ [ 4.] [Furthermore,] [the] [constraint] [of] [positivity] [for]
external data is trivial in this case; indeed using a _GL_ (4) transformation we can
set the 4 _×_ 4 matrix ( _Z_ 1 _, · · ·_ _, Z_ 4) to identity. The loop variables are just lines in
momentum-twistor space (or better, two-planes in four-dimensions), which correspond to points in the (dual) space-time. Having set the _Z_ matrix to the identity,
each 2 _×_ 4 matrix for the lines _L_ _[I]_ _γ_ ( _a_ ) [is] [simply] [identified] [with] [the] _[D]_ [matrices] _[D]_ [(] _[i]_ [)][.]
The amplituhedron positivity constraints are that the all the ordered minors of
each _D_ ( _i_ ) matrix are positive


(12) _i,_ (13) _i,_ (14) _i,_ (23) _i,_ (24) _i,_ (34) _i_ _>_ 0 (1.3)


We also have mutual positivity, that the 4 _×_ 4 determinant _⟨D_ ( _i_ ) _D_ ( _j_ ) _⟩_ _>_ 0, which
tells us that


(12) _i_ (34) _j_ + (23) _i_ (14) _j_ + (34) _i_ (12) _j_ + (14) _i_ (23) _j_ _−_ (13) _i_ (24) _j_ _−_ (24) _i_ (13) _j_ _>_ 0 (1.4)


We can also express these conditions in a convenient gauge, where




  - 1 _xi_ 0 _−wi_
_D_ ( _i_ ) =
0 _yi_ 1 _zi_




(1.5)



Then the positivity of each _D_ ( _i_ ) simply tells us that


_xi, yi, zi, wi_ _>_ 0 (1.6)


while the mutual positivity conditions become


( _xi −_ _xj_ )( _zi −_ _zj_ ) + ( _yi −_ _yj_ )( _wi −_ _wj_ ) _<_ 0 (1.7)


In this note we study various aspects of the geometry defined by these inequalities, as well as the corresponding canonical form Ω, which directly gives us the loop


                 - 3                  

integrand for four-particle scattering. Of course the four-particle amplitude has been
an object of intensive study for many years [6–10], with loop integrand now available
through seven loops. But our approach will be fundamentally different from previous
works. We will not begin by drawing planar diagrams made out of “boxes”, we will
make no mention of recursion relations, we will not make ansatze for the integrand
which are checked against cuts, and we will make no mention of physical constraints
from exponentiation of infrared divergences etc. Instead, we will discover all the
known general properties of the loop integrand, and many other properties besides,
directly by studying the positive geometry of the amplituhedron.


We will start with a lightning review of the one-loop geometry, which is just
that of _G_ +(2 _,_ 4), mostly to define some notation and nomenclature. We then do
some warm-up exercises for associating canonical forms Ωwith spaces specified by
particularly simple inequalities, which will come in handy in later sections. The
first non-trivial case with mutual positivity is obviously two loops, and we show how
to triangulate the space and extract the loop integrand, matching the well-known
result given as a sum of two double-boxes. Interestingly, while our triangulation of
the two-loop amplituhedron is manifestly “positive”, the sum of double-boxes is not,
with each term having singularities outside the amplituhedron that only cancel in
the sum.


We then make some general observation on the structure of certain cuts of the
amplitude, which correspond to various boundaries of the amplituhedron. In particular, the textbook understanding of unitarity as following from the break-up of
the loop integrand into two parts sewed together on the “unitarity cut” follows in a
beautiful way from positive geometry. These general results and some further explicit
triangulations also allow us to determine the three-loop integrand. We move on to
exploring another natural set of cuts that take the amplitude into the multi-collinear
region. This exposes a fascinating property of cuts of the multi-loop integrand: the
residues depend not only on the final cut geometry, but also on the path taken to
reach that geometry. Studying the combinatorics of this path dependence naturally
motivates looking at the logarithm of the amplitude, and explains why the log has
such good IR behavior.


From our new perspective, the determination of the integrand to all loop orders
requires a complete understanding of the full amplituhedron geometry. We have not
yet achieved this yet, but we believe that a systematic approach to this problem is
possible. As a prelude, we give a survey of some of the lower-dimensional “faces” of
amplituhedron. We can explicitly triangulate these faces and find their corresponding
canonical forms, which give us cuts of the full integrand. This already gives us highly
non-trivial all-loop order information about the integrand, in many cases not readily
available from any other approach.


                 - 4                  

### **2. One Loop Geometry**

At one loop we have a single line _L_ 1 _L_ 2, which we often also called “( _AB_ )”. The
geometry is given by the positive Grassmannian _G_ +(2 _,_ 4). The external data form a
polygon in P [3] with vertices _Z_ 1, _Z_ 2, _Z_ 3, _Z_ 4 and edges _Z_ 1 _Z_ 2, _Z_ 2 _Z_ 3, _Z_ 3 _Z_ 4, _Z_ 1 _Z_ 4.


The line _AB_ = _L_ 1 _L_ 2 is parametrized as


where _γ_ = 1 _,_ 2 and _a, I_ = 1 _, . . .,_ 4. The matrix _D_ represents a cell of positive
Grassmannian _G_ +(2 _,_ 4), in the generic case it is a top cell. In one particularly
convenient gauge-fixing we can write




  - 1 _x_ 0 _−w_
_D_ =
0 _y_ 1 _z_




(2.2)



where _x, y, z, w_ _>_ 0. This gauge-fixing of the _D_ matrix covers all boundaries by
sending variables _x, y, z, w_ to zero or infinity.
The form with logarithmic singularities on the boundaries of the space is trivially



Ω= _[dx]_



_dw_

_y_ _w_



_dy_

_x_ _y_



_dz_

_w_ _z_



(2.3)
_z_



The boundaries occur when one of the variables approaches 0 or _∞_ . We can easily
translate this expression back to momentum twistor space by solving two linear
equations:
_ZA_ = _Z_ 1 + _xZ_ 2 _−_ _wZ_ 4 _,_ _ZB_ = _yZ_ 2 + _Z_ 3 + _zZ_ 4 (2.4)


which gives

Ω= _[⟨][AB d]_ [2] _[Z][A][⟩⟨][AB d]_ [2] _[Z][B][⟩⟨]_ [1234] _[⟩]_ [2] (2.5)

_⟨AB_ 12 _⟩⟨AB_ 23 _⟩⟨AB_ 34 _⟩⟨AB_ 14 _⟩_


We now describe the boundaries of this space in detail–these are nothing but all
the cells of _G_ +(2 _,_ 4), which have also been described at length in e.g. [4]. We describe
them in detail here since the same geometry will arise repeatedly in the context of cuts
of the multiloop amplitudes. At the level of the form they correspond to logarithmic
singularities. In giving co-ordinates for the boundaries, we will freely use different


                 - 5                  

gauge-fixings as convenient for any given case, with all parameters positive. They
will always be trivially related to boundaries of (2.2).
The first boundaries occur when line _AB_ intersects one of the lines _Z_ 1 _Z_ 2, _Z_ 2 _Z_ 3,
_Z_ 3 _Z_ 4 or _Z_ 1 _Z_ 4. In the gauge-fixing (2.2) this sets one of the variables to _x, y, z, w_ to
0. In particular,


_⟨AB_ 12 _⟩_ = _w,_ _⟨AB_ 23 _⟩_ = _z,_ _⟨AB_ 34 _⟩_ = _y,_ _⟨AB_ 14 _⟩_ = _x_ (2.6)


where we suppressed _⟨_ 1234 _⟩_ . For cutting _Z_ 1 _Z_ 2, _⟨AB_ 12 _⟩_ = _w_ = 0 we get




- 1 _x_ 0 0
0 _y_ 1 _z_










- 1 _x_ 0 0
0 0 1 _z_











0 _y_ 1 0








                 - 6                  

_−α_ _−_ 1 0 0










- 0 1 0 0







four constraints.




        - 1 0 0 0
0 0 1 0



0 1 0 0







Let us start with a trivial example; suppose we have


_a < x < b_ (3.1)


It’s obvious that the form is 1 1 [but] [lets] [reproduce] [this] [in] [a] [heavy-handed]
_x−a_ _[−]_ _x−b_ [,]
way, from the viewpoint using “positive co-ordinates”. In this case, we can write

_α_
_x_ = _a_ + ( _b −_ _a_ ) (3.2)
1 + _α_


                 - 7                  

Note that for _∞_ _>_ _α_ _>_ 0, we cover the entire range of _a_ _<_ _x_ _<_ _b_ . The canonical
form is just _[dα]_ [which] [can] [be] [re-written] [in] [the] [original] [co-ordinates] [as]

_α_ [,]


_dα_ _dx_ _dx_ ( _a −_ _b_ ) _dx_

(3.3)
_α_ [=] _x −_ _a_ _[−]_ _x −_ _b_ [=] ( _x −_ _a_ )( _x −_ _b_ )


Next, consider 0 _< x_ 1 _< x_ 2. Once again, we can use positive variables


_x_ 1 = _α_ 1 _,_ _x_ 2 = _α_ 1 + _α_ 2 (3.4)


and the form is quite trivially



_dα_ 1

_α_ 1



_dα_ 2 _dx_ 1 _dx_ 2

= (3.5)
_α_ 2 _x_ 1( _x_ 2 _−_ _x_ 1)



We will henceforth skip the step of parametrization with positive variables, and also
omit the measure factor in presenting results.
Next consider 0 _< x_ 1 _< x_ 2 _< a_, the form is

    - 1 1 �� 1 1    - _a_

_−_ _−_ = (3.6)
_x_ 1 _x_ 1 _−_ _a_ _x_ 2 _−_ _x_ 1 _x_ 2 _−_ _a_ _x_ 1( _x_ 2 _−_ _x_ 1)( _a −_ _x_ 1)



�� 1 1

_−_
_x_ 2 _−_ _x_ 1 _x_ 2 _−_ _a_




- _a_
= (3.6)
_x_ 1( _x_ 2 _−_ _x_ 1)( _a −_ _x_ 1)



This extends trivially to e.g. 0 _< x_ 1 _< x_ 2 _< a < x_ 3 _< x_ 4 _< b_, for which the form is


_ab_
(3.7)
_x_ 1( _x_ 2 _−_ _x_ 1)( _a −_ _x_ 2)( _x_ 3 _−_ _a_ )( _x_ 4 _−_ _x_ 3)( _b −_ _x_ 4)


We will find it convenient to use a notation to represent these forms. Consider a
chain of inequalities of the form 0 _<_ _X_ 1 _<_ _X_ 2 _· · ·_ _<_ _XN_ . Some of the _X_ ’s are
the variables our form depends on, and some are constants like _a, b_ in our previous
examples. We will represent the constants by underlining the corresponding _X_ ’s.
In this notation, the form accompanying our two examples above are denoted as

[ _x_ 1 _, x_ 2 _, a_ ] and [ _x_ 1 _, x_ 2 _, a, x_ 3 _, x_ 4 _, b_ ]. As yet another example,




       - 1 1

[ _x_ 1 _, a, b, x_ 2 _, x_ 3 _, c, x_ 4] = _−_
_x_ 1 _x_ 1 _−_ _a_



�� 1 1
_x_ 2 _−_ _b_ _[−]_ _x_ 2 _−_ _c_



�� 1 1

_−_
_x_ 3 _−_ _x_ 2 _x_ 3 _−_ _c_



�� 1
_x_ 4 _−_ _c_

(3.8)







Next, suppose we have _xi, y_ with _y_ _> xi_ for all _i_ . Then, if the _x_ _[′]_ _s_ are ordered so
that _x_ 1 _< · · ·_ _, < xn_, we have _y_ _> xn_, and the form is




[ _x_ 1 _, · · ·_ _, xn, y_ ] = [1]

_x_ 1



1 1

_· · ·_
_x_ 2 _−_ _x_ 1 _xn −_ _xn−_ 1



1
(3.9)
_y −_ _xn_



Then we simply sum over all the permutations

     
[ _xσ_ 1 _, · · ·_ _, xσn, y_ ] (3.10)

_σ_


                 - 8                  

Note that individual terms in this sum have spurious poles ( _xi −_ _xj_ ), which cancel
in the sum. Indeed, in this simple case, it is trivial to do the sum explicitly, and find


_y_ _[n][−]_ [1]

(3.11)
( _y −_ _x_ 1)( _y −_ _x_ 2) _· · ·_ ( _y −_ _xn_ ) _x_ 1 _· · · xn_


Extremely naively, we may have expected the product in the denominator, but why
is there is a numerator factor? The reason is that otherwise, the form would not have
only logarithmic singularities! For instance, the residues on _x_ 1 _, · · ·_ _, xn_ _→_ 0 would
give 1 _/y_ _[n]_ ; it is the numerator that makes this 1 _/y_ . We can extend this to _yI_ _>_ _xi_
for a collection of _m_ _y_ ’s. This means that the smallest _y_ is larger than the largest _x_ .
Thus the form is

    
[ _xσ_ 1 _, · · ·_ _, xσn, yp_ 1 _· · ·_ _, ypm_ ] (3.12)
_σ,p_


Again the spurious poles cancel in the sum, but the forms are more interesting. In
the simplest new case where _n_ = 3 _, m_ = 2 the form is

_x_ 1 _x_ 2 _x_ 3 _y_ 1 + _x_ 1 _x_ 2 _x_ 3 _y_ 2 _−_ _x_ 1 _x_ 2 _y_ 1 _y_ 2 _−_ _x_ 1 _x_ 3 _y_ 1 _y_ 2 _−_ _x_ 2 _x_ 3 _y_ 1 _y_ 2 + _y_ 1 [2] _[y]_ 2 [2] (3.13)
_x_ 1 _x_ 2 _x_ 3( _y_ 1 _−_ _x_ 1)( _y_ 1 _−_ _x_ 2)( _y_ 1 _−_ _x_ 3)( _y_ 2 _−_ _x_ 1)( _y_ 2 _−_ _x_ 2)( _y_ 3 _−_ _x_ 3)


Let us now consider the inequality _x, y_ _>_ 0 and also _x_ + _y_ _<_ 1, or _x_ + _y_ _>_ 1.
The first case is just the inside of a triangle, while the second case is a quadrilateral:


Obviously the form in the first case _x_ + _y_ _<_ 1 is

_−_ 1
(3.14)
_xy_ ( _x_ + _y −_ 1)


For the second case, the region can be broken into two pieces in obvious ways. For
instance, if _x_ _>_ _a_, there is no further restriction on _y_, while if _x_ _<_ 1, we must have
_y_ _>_ 1 _−_ _x_


                 - 9                  

The form is then
1 1 1 1 _x_ + _y_
(3.15)
_x −_ 1 _y_ [+] _x_ (1 _−_ _x_ ) _y_ + _x −_ 1 [=] _xy_ ( _x_ + _y −_ 1)


This form could have also been derived without any triangulation. The denominator reflects all the inequalities as it should. However, with a random numerator,
we would have non-vanishing residue at the origin _x_ = _y_ = 0, which is clearly not in
the space. The numerator kills that residue, and the resulting form has logarithmic
singularities on the boundary of our space. We could have also arrived at this form
in another way. We know the form for _x_ + _y_ _<_ 1. Since the form with no restriction
(other than positivity) on _x, y_ is just 1 _/_ ( _xy_ ), we conclude that the form for _x_ + _y_ _>_ 1
is
1 _−a_ _x_ + _y_
(3.16)
_xy_ _[−]_ _xy_ ( _x_ + _y −_ 1) [=] _xy_ ( _x_ + _y −_ 1)


As a final example, let us consider _x, y, a_ 1 _, b_ 1 _, a_ 2 _, b_ 2 _>_ 0, together with the two
constraints
_x_ _x_
+ _[y]_ _>_ 1 _,_ + _[y]_ _>_ 1 (3.17)
_a_ 1 _b_ 1 _a_ 2 _b_ 2

We will find the form by triangulating the space in two different ways. In the first
triangulation, begin by ordering _a_ 1 _<_ _a_ 2 without loss of generality; the final form
will be obtained by symmetrizing 1 _↔_ 2. The shape of the allowed region _x, y_ space
depends on whether _b_ 1 _< b_ 2 or _b_ 1 _> b_ 2:


If _b_ 1 _< b_ 2, then the space is essentially the same as the quadrilateral we just studied.
The associated form obtained by breaking it up into the two regions _x_ _>_ _a_ 2, and
0 _< x < a_ 2, is given by




_[y]_ _>_ 1 _,_ _x_ + _[y]_

_b_ 1 _a_ 2 _b_




_>_ 1 (3.17)
_b_ 2








[1] 1

_y_ [+ [] _[x, ][a]_ [2][]] _y_ + _[b]_ [2] _[x]_




[2] _[x]_

_a_ 2 _[−]_ _[b]_ [2]








[ _a_ 1 _, a_ 2][ _b_ 1 _, b_ 2]




[ _a_ 2 _, x_ ] [1]



(3.18)



If _b_ 1 _> b_ 2, we have a pentagonal shape. We can break this up into three regions,
where _x > a_ 2, _a_ 2 _> x > a_ 12 and _a_ 12 _> x >_ 0. Here _a_ 12 = _[a]_ _a_ [1] 2 _[a]_ _b_ [2] 1 [(] _−_ _[b]_ [1] _a_ _[−]_ 1 _[b]_ _b_ [2] 2 [)] [.] [The] [associated]

form is








[1] 1

_y_ [+ ][[] _[a]_ [12] _[, x, ][a]_ [2][]] _y_ + _[b]_ [2] _[x]_



1 1

[2] _[x]_ + [ _x, a_ 12] _y_ + _[b]_ [1] _[x]_

_a_ 2 _[−]_ _[b]_ [2] _a_ 1




[1] _[x]_

_a_ 1 _[−]_ _[b]_ [1]








[ _a_ 1 _, a_ 2][ _b_ 2 _, b_ 1]




[ _a_ 2 _, x_ ] [1]



(3.19)




- 10 

Summing these forms and symmetrizing in 1 _↔_ 2, all the spurious poles cancel
and we find for the final form




_[x]_ _[y]_

_a_ 1 [+] _b_



( _[x]_




_[y]_ _[x]_

_b_ 1 [)(] _a_



_b_ 2 [)]



(3.20)

_[y]_

_b_ 2 _[−]_ [1)]




_[x]_ _[y]_

_a_ 1 [+] _b_ 1




_[x]_ _[y]_

_a_ 2 [+] _b_ 2




_[x]_ _[y]_

_y_ 2 [+] _b_



_xya_ 1 _b_ 1 _a_ 2 _b_ 2( _[x]_




_[y]_ _[x]_

_b_ 1 _[−]_ [1)(] _y_



Note that we could also have arrived at this result in another simpler way, by
thinking of the constraints in ( _a_ 1 _, b_ 1) and ( _a_ 2 _, b_ 2) spaces separately. For fixed _x, y_, if
we redefine _Ai_ = _x/ai_ and _Bi_ = _y/bi_, we just have _A_ 1 + _B_ 1 _>_ 1 _, A_ 2 + _B_ 2 _>_ 1. We
then get for the form


1 _A_ 1 + _B_ 1 ( _A_ 2 + _B_ 2)
(3.21)
_xy_ _[×]_ _A_ 1 _B_ 1( _A_ 1 + _B_ 1 _−_ 1) _[×]_ _A_ 2 _B_ 2( _A_ 2 + _B_ 2 _−_ 1)


which, including the trivial Jacobian factors from the change of variables, reduces
immediately to our above result obtained using triangulation.

### **4. Two Loops**


We now move on to studying the inequalities defining the amplituhedron for fourparticle scattering, starting at two-loops, where we just have a single mutual positivity condition to deal with, simply


( _x_ 1 _−_ _x_ 2)( _z_ 1 _−_ _z_ 2) + ( _y_ 1 _−_ _y_ 2)( _w_ 1 _−_ _w_ 2) _<_ 0 (4.1)


Without loss of generality we can take _x_ 1 _< x_ 2. Then we have


_z_ 1 _−_ _z_ 2 _>_ [(] _[y]_ [1] _[ −]_ _[y]_ [2][)(] _[w]_ [1] _[ −]_ _[w]_ [2][)] (4.2)

_x_ 2 _−_ _x_ 1


If either _y_ 1 _>_ _y_ 2 _, w_ 1 _>_ _w_ 2 or _y_ 1 _<_ _y_ 2 _, w_ 1 _<_ _w_ 2, we have ( _y_ 1 _−_ _y_ 2)( _w_ 1 _−_ _w_ 2) _>_ 0; the
form is then




[ _x_ 1 _, x_ 2] [1]

_z_ 2



_z_ 1 _−_ _z_ 2 _−_ [(] _[y]_ [1] _[−][y]_ [2][)(] _[w]_ [1] _[−][w]_ [2][)]



1




[2][)(] _[w]_ [1] _[−][w]_ [2][)] ([ _y_ 1 _, y_ 2][ _w_ 1 _, w_ 2] + [ _y_ 2 _, y_ 1][ _w_ 2 _, w_ 1]) (4.3)

_x_ 2 _−x_ 1



But if _y_ 1 _< y_ 2 _, w_ 1 _> w_ 2 or _y_ 1 _> y_ 2 _, w_ 1 _< w_ 2, we have


_z_ 2 _−_ _z_ 1 _< −_ [(] _[y]_ [1] _[ −]_ _[y]_ [2][)(] _[w]_ [1] _[ −]_ _[w]_ [2][)] (4.4)

_x_ 2 _−_ _x_ 1


Then the form is



_x_ 2 _−x_ 1







1
_x_ 1



1
_x_ 2 _−_ _x_ 1



1
_z_ 1




1 1

_−_
_z_ 2 _z_ _z_ [(] _[y]_ [1]



_z_ 2 _−_ _z_ 1 + [(] _[y]_ [1] _[−][y]_ [2][)(] _[w]_ [1] _[−][w]_ [2][)]



([ _y_ 1 _, y_ 2][ _w_ 2 _, w_ 1] + [ _y_ 2 _, y_ 1][ _w_ 1 _, w_ 2])


(4.5)




- 11 

Finally, we just have to swap 1 _↔_ 2. The sum of these terms is then


_x_ 1 _z_ 2 + _x_ 2 _z_ 1 + _y_ 1 _w_ 2 + _y_ 2 _w_ 1
(4.6)
_x_ 1 _x_ 2 _y_ 1 _y_ 2 _z_ 1 _z_ 2 _w_ 1 _w_ 2[( _x_ 1 _−_ _x_ 2)( _z_ 1 _−_ _z_ 2) + ( _y_ 1 _−_ _y_ 2)( _w_ 1 _−_ _w_ 2)]


We can expand it as a sum of four terms by canceling terms in numerator and
denominator,

  - 1   _x_ 2 _y_ 1 _y_ 2 _z_ 1 _w_ 1 _w_ 2[( _x_ 1 _−_ _x_ 2)( _z_ 1 _−_ _z_ 2) + ( _y_ 1 _−_ _y_ 2)( _w_ 1 _−_ _w_ 2)] [+ 1] _[ ↔]_ [2]

  - 1   + (4.7)
_x_ 1 _x_ 2 _y_ 2 _z_ 1 _z_ 2 _w_ 1[( _x_ 1 _−_ _x_ 2)( _z_ 1 _−_ _z_ 2) + ( _y_ 1 _−_ _y_ 2)( _w_ 1 _−_ _w_ 2)] [+ 1] _[ ↔]_ [2]



We can solve for all variables in terms of momentum twistors, finding








+ symmetrization



(4.8)



_⟨_ 1234 _⟩_ [3]


_⟨AB_ 12 _⟩⟨AB_ 23 _⟩⟨AB_ 34 _⟩⟨ABCD⟩_



_⟨CD_ 34 _⟩⟨CD_ 14 _⟩⟨CD_ 12 _⟩_



_⟨_ 1234 _⟩_ [3]
+

_⟨AB_ 23 _⟩⟨AB_ 34 _⟩⟨AB_ 14 _⟩⟨ABCD⟩_
_⟨CD_ 14 _⟩⟨CD_ 12 _⟩⟨CD_ 23 _⟩_



where by symmetrization we mean adding another two terms where we swap ( _AB_ ) _↔_
( _CD_ ). The expression (4.8) is the integrand for two double boxes


terms instead of two.

we double cut one loop variable so that _D_ (1) passes through the point 1, while _D_ (2)
passes through the point 3. The _D_ matrices on this cut have the form




  - 1 0 0 0
_D_ (1) =
0 _y_ 1 _z_




- - 1 _x_ 0 _−w_
_,_ _D_ (2) =
0 0 1 0


 - 12  



(4.9)


But note that the mutual positivity condition between _D_ (1) and _D_ (3) is automatically
satisfied,
_⟨D_ (1) _D_ (2) _⟩_ = _xz_ + _yw_ _>_ 0 (4.10)


Because of this, we conclude that taking a further residue where ( _AB_ )1( _AB_ )2 is cut
must vanish, since there is no way to set this to zero without further setting one of
_x, z_, and _y, w_, to zero.

on this 5-cut, but the residue cancels in the sum


By contrast, obviously each term in our triangulation is compatible with all positivity
conditions. This mirrors familiar features of the BCFW expansion for tree amplitudes: they correspond to triangulations that are “inside” the amplituhedron and
manifestly consistent with positivity properties (and therefore also the symmetries
of the theory), at the expense of manifest locality.

### **5. Generalities on Cuts**


Before starting our more detailed exploration of multiloop amplitudes, let us make
some general observations about cuts of the integrand.


**Reconstruction** **from** **Single** **Cuts**


We are familiar with reconstructing the integrand from BCFW shifts of the external
data [11]. For instance, if we shift _Z_ 1 _→_ _Z_ [ˆ] 1 = _Z_ 1 + _αZ_ 4, the integrand at _α_ = 0
is (the negative of) the residues of the single cuts where _⟨_ ( _AB_ ) _i_ 12 [ˆ] _⟩→_ 0. This is
trivially reflected from positivity. We can divide the _wi_ space into the pieces where
_w_ 1 is smallest, _w_ 2 is smallest and so on. Suppose _w_ 1 is smallest; then we can set
_wi_ = _w_ 1 + _w_ ˆ _i_ . The remaining positivity conditions are then exactly the same as the


                 - 13                  

same as the computation of the single cut where _w_ 1 _→_ 0. And we have to sum over
the single cuts for setting each of the _wi_ _→_ 0.
Obviously, we can extend this to all the variables ( _x, y, z, w_ ). We can always take
sum _xix, yiy_ _, ziz_ _, wiw_ to be smallest, and sum over all possible _ix, iy, iz, iw_ . Then, we
can compute the integrand directly by summing over all these 4-cuts. This naturally
corresponds to using a residue theorem using an extended BCFW deformation under
which _Z_ 1 _→_ _Z_ [ˆ] 1 = _Z_ 1 + _αZ_ 4 + _βZ_ 2 _,_ _Z_ 3 _→_ _Z_ [ˆ] 3 = _Z_ 3 + _γZ_ 2 + _ρZ_ 4.


**Emergent** **Planarity** **and** **Leading** **Singularities**


Let us now consider the opposite extreme, and look at the zero-dimensional faces of
the amplituhedron. Here, each _D_ ( _i_ ) is taken to be one of the zero dimensional cells of
_G_ (2 _,_ 4), where the columns _i, j_ can be set to the identity and the remaining entries
are zero. From the mutual positivity of equation (4.1), we learn something very
simple right away: the configuration will satisfy positivity in all cases except one: we
can’t have the (13) cells and (24) cells at the same time. It is trivial to see that this
fact extends to all _n_ MHV amplitudes at all loop orders. If all the _ABi_ = ( _ab_ ) _i_ are
drawn as chords on a disk, then a configuration with lines that don’t cross is allowed,
but a configuration with lines that cross violates positivity and must have vanishing
residue. Examples of allowed and non-allowed configurations are shown below:


The fact that our form can ultimately be expressed as a sum over planar local
integrands is not obviously built into the geometry, but of course does emerge from
it. We see this planarity very vividly in the above structure of leading singularities–
clearly planar diagrams can only give us leading singularities of the allowed type,
while all other objects can give us the illegal “crossing” configurations. Indeed there
are many meaningful local integrands, compatible with the cyclic structure on external data, which can nonetheless not be considered as “planar”. A simple example
is the square of one-loop amplitude, whose integrand can be written in momentum
twistor space as


_⟨_ 1234 _⟩_ [4]

(5.1)
_⟨AB_ 12 _⟩⟨AB_ 23 _⟩⟨AB_ 34 _⟩⟨AB_ 14 _⟩⟨CD_ 12 _⟩⟨CD_ 23 _⟩⟨CD_ 34 _⟩⟨CD_ 14 _⟩_


                 - 14                  

This integrand has an obvious leading singularity where e.g. _AB_ = 13 and _CD_ =
24, which cross in index space. This is a “not allowed” leading singularity that is
incompatible with positivity. Thus, we see that the planar structure of the integrand
is not a trivial consequence of cyclically ordered external data, but actually emerges
from the positive geometry of the amplituhedron. Note that “planarity” is not an
obvious invariant property of the full integrand, but is only a natural statement about
a particular expansion of the integrand in terms of (local) Feynman diagrams. It is
thus perhaps not surprising that planarity should be one of many derived properties
of the integrand from the amplituhedron point of view.

### **6. Unitarity from Positivity**


In much of the recent work on scattering amplitudes in planar _N_ = 4 SYM, the
unitarity of loop amplitudes has been directly associated with correctly matching
the single cut of the loop integrand [11], determined by the the forward limit [12]
of the lower-loop amplitude. However there is an even simpler manifestation of
unitarity, familiar from the textbooks, in the double-cut (or “unitarity cut”) of the
integrand, which is given by sewing together two lower loop integrand.


This is easy to translate to momentum-twistor language. Starting with the _L_ -loop
integrand, we take one loop variable, ( _AB_ ) _L_, to cut (12) and (34). The corresponding
_D_ matrix is then of the form




  - 1 _x_ 0 0
_DL_ =
0 0 _y_ 1




(6.1)



If we compute the residue of the integrand on this configuration, unitarity tells us
that the result must be



_y_ _[Z]_ [4] _[, Z]_ [4]



_dy_

_x_ _y_




 - _M_ 4 _[L]_ [1][(] _[Z]_ [1] _[−][xZ]_ [2] _[, Z]_ [2] _[, Z]_ [3] _[, Z]_ [4] _[−][yZ]_ [3][)] _[M][ L]_ 4 [2]

_L_ 1+ _L_ 2= _L−_ 1







_dx_




 _y_ _[×]_




_Z_ 1 _, Z_ 2 _−_ [1]




[1]

_x_ _[Z]_ [1] _[, Z]_ [3] _[ −]_ _y_ [1]



(6.2)
We will now see that this result follows in a simple and beautiful way from the
positive geometry of the amplituhedron.
On the unitarity cut, the positivity conditions are the usual ones for the ( _L −_ 1)
loop variables. For _DL_ we just have that _x, y_ _>_ 0. The mutual positivity between


                 - 15                  

_DL_ and the remaining _Di_ just tells us that


(23) _i_ + _xy_ (14) _i −_ _x_ (13) _i −_ _y_ (24) _i_ _>_ 0 (6.3)


This condition also tells us that


[(13) _−_ _y_ (14)][(24) _−_ _x_ (14)] = (13)(24) _−_ _x_ (13)(14) _−_ _y_ (14)(24) + _xy_ (14) [2] (6.4)


= (12)(34) + (14)[(23) + _xy_ (14) _−_ _x_ (13) _−_ _y_ (24)] _>_ (12)(34) _>_ 0


where in the second line we used (13)(24) = (12)(34) + (23)(14). Now, obviously we
can divide the space of each _Di_ into ones where (13) _i_ _−_ (14) _i_ _>_ 0, and (13) _i_ _−y_ (14) _i_ _<_
0, similarly (24) _i −_ _x_ (14) _i_ _>_ 0 or (24) _i −_ _x_ (14) _i_ _<_ 0. However, if the product of these
two factors is negative it is impossible to satisfy equation (6.3). Thus, for each _i_, we
have _either_ that
(13) _−_ _y_ (14) _>_ 0 and (24) _−_ _x_ (14) _>_ 0 (6.5)


or
(13) _−_ _y_ (14) _>_ 0 _,_ and (24) _−_ _x_ (14) _>_ 0 (6.6)


Let us say that _L_ 1 of the lines _Da_ satisfy the first inequality and the remaining
_L_ 2 = _L −_ 1 _−_ _L_ 1 lines _DA_ satisfy the second inequality. Explicitly, in the first case
the region is represented by positivity conditions


(12) _a_ _>_ 0 _,_ (13) _a −_ _y_ (14) _a_ _>_ 0 _,_ (14) _a_ _>_ 0 _,_ (23) _a_ _>_ 0 _,_ (24) _a −_ _x_ (14) _a_ _>_ 0 _,_ (34) _a_ _>_ 0


(23) _a_ + _xy_ (14) _a −_ _x_ (13) _a −_ _y_ (24) _a_ _>_ 0 (6.7)


Let us define shifted columns


( [ˆ] 3) _a_ = (3) _a −_ _y_ (4) _a,_ ( [ˆ] 2) _a_ = (2) _a −_ _x_ (1) _a_ (6.8)


Thus the set of positivity conditions become


(1 [ˆ] 2) _a_ _>_ 0 _,_ (1 [ˆ] 3) _a_ _>_ 0 _,_ (14) _a_ _>_ 0 _,_ ( [ˆ] 2 [ˆ] 3) _a_ _>_ 0 _,_ ( [ˆ] 24) _a_ _>_ 0 _,_ ( [ˆ] 34) _a_ _>_ 0 (6.9)


In the second region we have


(12) _A_ _>_ 0 _, y_ (14) _A −_ (13) _A_ _>_ 0 _,_ (14) _A_ _>_ 0 _,_ (23) _A_ _>_ 0 _, x_ (14) _A −_ (24) _A_ _>_ 0 _,_ (34) _A_ _>_ 0


(23) _A_ + _xy_ (14) _A −_ _x_ (13) _A −_ _y_ (24) _A_ _>_ 0 (6.10)


Let us define shifts



( [ˆ] 1) _A_ = (1) _A −_ [1]




[1] ( [ˆ] 4) _A_ = (4) _A −_ [1]

_x_ [(2)] _[A][,]_ _y_



(6.11)
_y_ [(3)] _[A]_



Then the set of positivity conditions become


( [ˆ] 12) _A_ _>_ 0 _,_ ( [ˆ] 13) _A_ _>_ 0 _,_ ( [ˆ] 1 [ˆ] 4) _A_ _>_ 0 _,_ (23) _A_ _>_ 0 _,_ (2 [ˆ] 4) _A_ _>_ 0 _,_ (3 [ˆ] 4) _A_ _>_ 0 (6.12)


                 - 16                  

Now, we come to the positivity conditions internal to the _Da_ ’s, internal to the
_DA_ ’s, and also the ones between _Da_ and _DA_ ’s. Actually quite strikingly, the _Da_ ’s
and _DA_ ’s are automatically mutually positive! We look at


(12) _a_ (34) _A_ + (23) _a_ (14) _A_ + (34) _a_ (12) _A_ + (14) _a_ (23) _A −_ (13) _a_ (24) _A −_ (24) _a_ (13) _A_ (6.13)


Rewriting this in terms of the natural shifted variables



(2) _a_ = ( [ˆ] 2) _a_ + _x_ (1) _a,_ (3) _a_ = ( [ˆ] 3) _a_ + _y_ (4) _a_ (1) _A_ = ( [ˆ] 1) _A_ + [1]




[1] (4) _A_ = ( [ˆ] 4) _A_ + [1]

_x_ [(2)] _[A][,]_ _y_



_y_ [(3)] _[A]_



(6.14)
and plugging into (6.13) we find




                    - 1
(1 [ˆ] 2) _a_ (3 [ˆ] 4) _A_ + [(2 [ˆ][ˆ] 3) _a_ + _xy_ (14) _a_ + _y_ ( [ˆ] 24) _a_ + _x_ (1 [ˆ] 3) _a_ ] [1]
_xy_ [(23)] _[A]_ [ + (ˆ1ˆ4)] _[A]_ [ +] _x_



_y_ [(ˆ13)] _[A]_




[1] [1]

_x_ [(2ˆ4)] _[A]_ [ +] _y_








                  + ( [ˆ] 34) _a_ ( [ˆ] 12) _A_ + (14) _a_ (23) _A −_ [(1 [ˆ] 3) _a_ + _y_ (14) _a_ ] (2 [ˆ] 4) _A_ + [1]

_y_ [(23)] _[A]_




                  + ( [ˆ] 34) _a_ ( [ˆ] 12) _A_ + (14) _a_ (23) _A −_ [(1 [ˆ] 3) _a_ + _y_ (14) _a_ ] (2 [ˆ] 4) _A_ + [1]




- 
_−_ [( [ˆ] 24) _a_ + _x_ (14) _a_ ] ( [ˆ] 13) _A_ + [1]

_x_ [(23)] _[A]_




- 
_−_ [( [ˆ] 24) _a_ + _x_ (14) _a_ ] ( [ˆ] 13) _A_ + [1]







= (1 [ˆ] 2) _a_ (3 [ˆ] 4) _A_ + (34) [ˆ] _a_ ( [ˆ] 12) _A_ + [1]

_y_ [[(ˆ2ˆ3)] _[a]_ [ +] _[ x]_ [(1ˆ3)] _[a]_ [](ˆ13)] _[A]_ [ +] _[ x]_ [[(1ˆ3)] _[a]_ [ +] _[ y]_ [(14)] _[a]_ [](ˆ1ˆ4)] _[A]_



+ [( [ˆ] 2 [ˆ] 3) _a_ + _y_ ( [ˆ] 24) _i_ ](14) _A_ + [1]




[1] [1]

_x_ [[(ˆ2ˆ3)] _[a]_ [ +] _[ y]_ [(ˆ24)] _[i]_ [](2ˆ4)] _[A]_ [ +]




_[>]_ [ 0] (6.15)
_xy_ [(ˆ2ˆ3)] _[a]_ [(23)] _[A]_



The positivity here is quite non-trivial; the expression many terms with plus and
minus signs that cancel each other, leaving only pluses.
The mutual positivity internally for the _Da_ ’s (or the _DA_ ’s) are exactly the same
for the shifted and unshifted columns, since the (4 _×_ 4) determinants are unchanged
in shifting a column by a multiple of another. These can be easily translated in shifts
of external twistors. Under _Aγ_ = _Dγa · Za_, we have for the first shift


_A_ = _D · Z_ = (1) _Z_ 1 + (2) [ˆ] _Z_ 2 + (3) [ˆ] _Z_ 3 + (4) _Z_ 4
= (1) _Z_ 1 + (2) _Z_ 2 _−_ _x_ (1) _Z_ 2 + (3) _Z_ 3 _−_ _y_ (4) _Z_ 3 + (4) _Z_ 4

= (1) _Z_ [ˆ] 1 + (2) _Z_ 2 + (3) _Z_ 3 + (4) _Z_ [ˆ] 4 (6.16)


Thus, the form for the _L_ 1 lines is


_M_ 4 _[L]_ [1][(] _[Z]_ [1] _[−]_ _[xZ]_ [2] _[, Z]_ [2] _[, Z]_ [3] _[, Z]_ [4] _[−]_ _[yZ]_ [3][)] (6.17)


and analogously the form for the _L_ 2 lines is



_y_ _[Z]_ [4] _[, Z]_ [4]




(6.18)



_M_ 4 _[L]_ [2]




_Z_ 1 _, Z_ 2 _−_ [1]




[1]

_x_ _[Z]_ [1] _[, Z]_ [3] _[ −]_ _y_ [1]



Thus, we conclude that the unitarity cut is



_y_ _[Z]_ [4] _[, Z]_ [4]



_dx_



_dy_

_x_ _y_




 _y_ _[×]_




_[×]_ - _M_ 4 _[L]_ [1][(] _[Z]_ [1] _[−][xZ]_ [2] _[, Z]_ [2] _[, Z]_ [3] _[, Z]_ [4] _[−][yZ]_ [3][)] _[M][ L]_ 4 [2]

_L_ 1+ _L_ 2= _L−_ 1








_Z_ 1 _, Z_ 2 _−_ [1]




[1]

_x_ _[Z]_ [1] _[, Z]_ [3] _[ −]_ _y_ [1]



(6.19)
precisely as needed to enforce unitarity.


                 - 17                  

### **7. Three Loops**

Having established these general results, let us turn to the three-loop amplitude.
Recall from our general discussion that it suffices to look at various cuts of the
amplitude, coming from taking _xσ_ 1 _, yσ_ 2 _, zσ_ 3 _, wσ_ 4 to be smallest. For the case of three
loops, at least one pair of _σ_ 1 _, σ_ 2 _, σ_ 3 _, σ_ 4 will correspond to the same loop, thus, to
compute the full three-loop integrand, it suffices to compute the cut of the integrand
where one loop is double-cut. We have already verified that the unitarity double-cut
is correctly reproduced at any loop order. It thus suffices to compute the remaining
double cuts, which we call the “corner cuts”: where the line passes through one of
the points _Zi_, or its parity conjugate, where the line lies in the plane ( _Zi−_ 1 _ZiZi_ +1).
Since these are parity conjugate, it is enough to compute one of them, which we take
to be the cut where the line corresponding to the third loop passes through point 4.
It will be convenient to use a different gauge-fixing for the third loop




  - _a_ 1 _b_ 0
_D_ (3) =
0 0 0 1




(7.1)



If we further rescale the variables for the remaining loop variables as _wi_ _→_ _wi/b, yi_ _→_
_byi_ ; _zi_ _→_ _zi/a, xi_ _→_ _axi_, the remaining positivity conditions become


_xi_ + _yi_ _>_ 1 _,_ ( _x_ 1 _−_ _x_ 2)( _z_ 1 _−_ _z_ 2) + ( _y_ 1 _−_ _y_ 2)( _w_ 1 _−_ _w_ 2) _<_ 0 (7.2)


We can assume that _x_ 1 _< x_ 2, so that just as for two-loops we have then sum at the
end over 1 _↔_ 2. Let us also define



_x_ 2 _−x_ 1








[2][)(] _[w]_ [1] _[−][w]_ [2][)] _,_ _Z−_ = _z_ [1] 1

_x_ 2 _−x_ 1



_Z_ + = [1]

_z_ 2



_z_ 1 _−_ _z_ 2 _−_ [(] _[y]_ [1] _[−][y]_ [2][)(] _[w]_ [1] _[−][w]_ [2][)]



1



_z_ 1



(7.3)




1 1

_−_
_z_ 2 _z_ _z_ [(] _[y]_



_z_ 2 _−_ _z_ 1 _−_ [(] _[y]_ [2] _[−][y]_ [1][)(] _[w]_ [1] _[−][w]_ [2][)]



Then, by dividing the space into pieces much as we did at 2-loops, we find that the
form is


[ _x_ 1 _, x_ 2 _,_ 1]([1 _−_ _x_ 1 _, y_ 1 _, y_ 2]([ _w_ 1 _, w_ 2] _Z_ + + [ _w_ 2 _, w_ 1] _Z−_ ) (7.4)

+ ([1 _−_ _x_ 2 _, y_ 2 _,_ 1 _−_ _x_ 1 _, y_ 1] + [1 _−_ _x_ 1 _, y_ 2 _, y_ 1])([ _w_ 2 _, w_ 1] _Z_ + + [ _w_ 1 _, w_ 2] _Z−_ ))

+ [ _x_ 1 _,_ 1 _, x_ 2]([1 _−_ _x_ 1 _, y_ 1 _, y_ 2]([ _w_ 1 _, w_ 2] _Z_ + + [ _w_ 2 _, w_ 1] _Z−_ )

+ ([ _y_ 2 _,_ 1 _−_ _x_ 1 _, y_ 1] + [1 _−_ _x_ 1 _, y_ 2 _, y_ 1])([ _w_ 2 _, w_ 1] _Z_ + + [ _w_ 1 _, w_ 2] _Z−_ ))


+ [1 _, x_ 1 _, x_ 2]([ _y_ 1 _, y_ 2]([ _w_ 1 _, w_ 2] _Z_ + + [ _w_ 2 _, w_ 1] _Z−_ ) + [ _y_ 2 _, y_ 1]([ _w_ 2 _, w_ 1] _Z_ + + [ _w_ 1 _, w_ 2] _Z−_ )


Adding 1 _↔_ 2, all spurious poles cancel and we obtain




- _w_ 2 _x_ 1 _x_ 2 _y_ 1 + _w_ 2 _x_ 2 _y_ 12 [+] _[ w]_ [1] _[x]_ [1] _[x]_ [2] _[y]_ [2] _[−]_ _[w]_ [1] _[y]_ [1] _[y]_ [2] _[−]_ _[w]_ [2] _[y]_ [1] _[y]_ [2] [+] _[ w]_ [2] _[x]_ [1] _[y]_ [1] _[y]_ [2] [+] _[ w]_ [1] _[x]_ [2] _[y]_ [1] _[y]_ [2]
+ _w_ 2 _y_ 1 [2] _[y]_ [2] [+] _[ w]_ [1] _[x]_ [1] _[y]_ 2 [2] [+] _[ w]_ [1] _[y]_ [1] _[y]_ 2 [2] _[−]_ _[x]_ [1] _[x]_ [2] _[z]_ [1] [+] _[ x]_ [1] _[x]_ [2] 2 _[z]_ [1] [+] _[ x]_ [2] 2 _[y]_ [1] _[z]_ [1] [+] _[ x]_ [1] _[x]_ [2] _[y]_ [2] _[z]_ [1]
+ _x_ 2 _y_ 1 _y_ 2 _z_ 1 _−_ _x_ 1 _x_ 2 _z_ 2 + _x_ [2] 1 _[x]_ [2] _[z]_ [2] [+] _[ x]_ [1] _[x]_ [2] _[y]_ [1] _[z]_ [2] [+] _[ x]_ [2] 1 _[y]_ [2] _[z]_ [2] [+] _[ x]_ [1] _[y]_ [1] _[y]_ [2] _[z]_ [2]







_abx_ 1 _x_ 2 _y_ 1 _y_ 2 _z_ 1 _z_ 2 _w_ 1 _w_ 2( _x_ 1 + _y_ 1 _−_ 1)( _x_ 2 + _y_ 2 _−_ 1)(( _x_ 2 _−_ _x_ 1)( _z_ 1 _−_ _z_ 2) + ( _y_ 2 _−_ _y_ 1)( _w_ 1 _−_ _w_ 2))
(7.5)


                 - 18                  

This matches what we get from the familiar local expansion, as a sum over ladders
and “tennis court” diagrams:

### **8. Multi-Collinear Region**


We have seen that a particular double cut of a single loop–the unitarity cut– is simply
expressed in terms of (shifted) lower-loop objects. It is thus natural to look at the
other two kinds of double cuts. Let us consider the cut where the _L_ _[th]_ line passes
through 2. It will be convenient to use a different gauge-fixing for this last line




  - 0 1 0 0
_D_ ( _L_ ) = _−α_ 0 1 _γ_




(8.1)



Then the mutual positivity conditions between _D_ ( _L_ ) and the other lines is simply


_αwi_ + _zi_ _> γ_ (8.2)


It is amusing that from the point of view of the lower-loop problem, we are simply
putting a simple additional restriction on the allowed region for _wi, zi_ .
Despite the apparent simplicity of this deformation of the _L −_ 1 loop problem,
unlike the unitarity cut, this double cut can’t be determined in terms of shifts of
lower-loop problems in a straightforward way. However, there is a further, triple cut,
which does have a very simple interpretation. Consider the limit where _β_ _→_ 0. This
is the collinear region, where the line passes through the point 2 while lying in the
plane (123) [13]. Note that the positivity condition is now automatically satisfied,
and so the cut is trivial:
_A_ [coll] _L_ _[.]_ = _[dα]_ _α_ _[×][ A][L][−]_ [1] (8.3)

In this discussion we assumed that all the lines but one are generic. We now
investigate what happens when _l_ lines are sent into the collinear region. The most


                 - 19                  

general way this can happen is to start with _L_ 12 lines cutting (12) and _L_ 23 lines
cutting (23). Let us gauge-fix in a convenient way, and write for the two sets of lines




  - _βi_ 1 0 0
_D_ ( _i_ ) = _−αi_ 0 1 _γi_




- - 0 1 _ρI_ 0
_D_ ( _I_ ) =
_αI_ 0 1 _γI_




(8.4)



In order to reach the collinear limit, we must send _βi, γi_ _→_ 0, and _ρI, δI_ _→_ 0.
We can send these to zero in different ways, but let us focus on one for definiteness,
the other cases can be treated similarly. For the lines cutting (12), we first take them
to pass through 2, and then move them into the collinear region where they lie in
(123); in other words, we first send _βi_ _→_ 0, and then _γi_ _→_ 0. Similarly for the lines
intersecting (23), we first send them to pass through 2, then to lie in (123), so that
we put the _ρI_ _→_ 0, then send _γI_ _→_ 0. Now, the positivity conditions between these
lines are just



( _βi −_ _βj_ )( _γi −_ _γj_ ) _>_ 0 _,_ ( _ρI_ _−_ _ρJ_ ) - _γI_ _−_ _[γ][J]_
_αI_ _αJ_





_>_ 0 _,_ ( _βi −_ _αIρI_ )( _γi −_ _γI_ ) _>_ 0


(8.5)



Collectively, these tell us something simple. Suppose we take the lines to pass
through 2 in some particular order, say by first taking _β_ 1 _→_ 0, then _β_ 2 _→_ 0, then
_ρ_ 1 _→_ 0, then _ρ_ 2 _→_ 0, then _β_ 3 _→_ 0 etc. Then, the cut vanishes unless the lines are
taken into the collinear limit in exactly the same order! In this case, the cut is just



_l_



_a_ =1



_dαa_ _× M_ _[L][−][l]_ (8.6)

_αa_


### **9. Log of the Amplitude**

Scattering amplitudes have well-known double-logarithmic infrared divergences, arising precisely from loop integration in the collinear region. At _L_ loops, we have a
log [2] _[L]_ divergence, which exponentiates in a well-known way; the logarithm of the
amplitude only has a log [2] divergence. This is a motivation for looking at the log
of the amplitude from a physical point of view. But as we have just seen, the loop
integrand form also has an extremely simple behavior in the multicollinear limit.
We will now see that this behavior, together with some very simple combinatorics,
already motivates looking at the logarithm of the amplitude directly at the level
of the integrand. While the amplitude itself has a non-vanishing residue when one
loop momentum is brought into the collinear region, we will see that the log of the
amplitude vanishes in the multicollinear region, unless _all L_ loop momenta are taken
into the collinear region. The residue depends in a non-trivial way on the specific
path taken into the collinear region. Furthermore, we will see that the log of the


                 - 20                  

amplitude naturally leads us to consider _all_ the natural “positive regions” we can
think of related to amplituhedron geometry.
Let us start by introducing a generating function combining together the amplitude at all loop order, otherwise known as the amplitude itself:


_M_ = 1 + _gM_ 1 + _g_ [2] _M_ 2 + _· · ·_ (9.1)


Now, consider for any function _f_, the expansion for _f_ ( _M_ ). Suppose that


_f_ (1 + _x_ ) = _x_ + _a_ 2 _x_ [2] + _a_ 3 _x_ [3] + _· · ·_ (9.2)


then


_f_ ( _M_ ) = ( _gM_ 1 + _g_ [2] _M_ 2 + _· · ·_ ) + _a_ 2( _g_ [2] _A_ [2] 1 [+ 2] _[g]_ [3] _[M]_ [1] _[M]_ [2] [+] _[ · · ·]_ [ ) +] _[ a]_ [3] _[g]_ [3] _[M]_ [3] [+] _[ · · ·]_

= _gM_ 1 + _g_ [2] ( _M_ 2 + _a_ 2 _M_ 1 [2][) +] _[ g]_ [3][(] _[M]_ [3] [+ 2] _[a]_ [2] _[M]_ [1] _[M]_ [2] [+] _[ a]_ [3] _[M]_ [ 3] 1 [) +] _[ · · ·]_ (9.3)


We’d now like to extract the permutation-invariant integrand from this expression at _L_ loops. For instance,


    _M_ 3 = _d_ [4] _x_ 1 _d_ [4] _x_ 2 _d_ [4] _x_ 3 _M_ 3( _x_ 1 _, x_ 2 _, x_ 3)


    _M_ 1 _M_ 2 = _d_ [4] _x_ 1 _d_ [4] _x_ 2 _d_ [4] _x_ 3 [( _M_ 1( _x_ 1) _M_ 2( _x_ 2 _, x_ 3) + _M_ 1( _x_ 2) _M_ 2( _x_ 1 _, x_ 3) + _M_ 1( _x_ 3) _M_ 2( _x_ 1 _, x_ 2)]


    _M_ 1 [3] [=] _d_ [4] _x_ 1 _d_ [4] _x_ 2 _d_ [4] _x_ 3 _M_ 1( _x_ 1) _M_ 1( _x_ 2) _M_ 1( _x_ 3) (9.4)


Actually, for the combinatorics, the “� _d_ [4] _x_ ” are irrelevant. Instead, we define a
generating function




  _M_ = 1 +




  _xi_ ( _i_ ) +

_i_ _i<j_




- 
_xixj_ ( _ij_ ) +

_i<j_ _i<j<k_



_xixjxk_ ( _ijk_ ) + _· · ·_ (9.5)

_i<j<k_



Here “(1)” stands for _M_ 1( _x_ 1), “(134)” stands for _M_ 3( _x_ 1 _, x_ 3 _, x_ 4) and so on. Then, the
integrand for _f_ ( _M_ ) at _L_ loops is just the coefficient of ( _x_ 1 _· · · xL_ ) in the expansion
of _f_ ( _A_ ), or put another way


_f_ ( _M_ ) _[L][−][loop]_ = _∂x_ 1 _···xLf_ ( _M_ ) _|x_ 1= _···_ = _xL_ =0 (9.6)


Obviously, if we are only interested in _L_ loops, we can truncate the _xi_ to just
_x_ 1 _, · · ·_ _, xL_ if we like. Thus, explicitly, for _L_ = 3, we have


_M_ = 1 + _x_ 1(1) + _x_ 2(2) + _x_ 3(3) + _x_ 1 _x_ 2(12) + _x_ 1 _x_ 3(13) + _x_ 2 _x_ 3(23) + _x_ 1 _x_ 2 _x_ 3(123)
(9.7)


and foreseeing our future interest, for _f_ ( _M_ ) = log( _M_ ), we have for the 3-loop log of
the amplitude


(log _M_ ) [3] _[−][loop]_ = (123) + 2(1)(2)(3) _−_ [(1)(23) + (2)(13) + (3)(12)] (9.8)


                 - 21                  

We would now like to compute the cut of _f_ ( _M_ ) in the multi-collinear limit.
Suppose _L_ lines are sent to pass through 2 in some order (1 _, · · ·_ _, L_ ). We already
know that the cut of the amplitude in the multi-collinear limit depends on the order
in which the lines are then sent to the collinear region–indeed for the amplitude
the cut vanishes unless the lines are sent to the collinear limit in the same order
(1 _, · · ·_ _, L_ ). This will not in general be true for _f_ ( _M_ ). Suppose that a set of _l_ lines
are moved into the collinear limit in some order _σ_ = _{σ_ 1 _, · · ·_ _, σl}_ . For instance for
_L_ = 3, we could take _σ_ = _{_ 2 _}_ or _σ_ = _{_ 13 _}_ or _σ_ = _{_ 231 _}_ . Then, it is easy to see that
the multi-collinear cut of _f_ ( _M_ ) can be computed as follows.
We first play the following game, to produce a new generating function _M_ _[σ]_ : (I)
if an ordered subset of _σ_ occurs out of order in the brackets of _M_, we drop that term.
(II) We then delete all the labels in _σ_ . Let’s illustrate this for _L_ = 3 with _σ_ = _{_ 31 _}_ .
The terms _x_ 1 _x_ 3(13) and _x_ 1 _x_ 2 _x_ 3(123) in _M_ are dropped, and the rest are kept. Then,
we drop the indices 3 _,_ 1, and are left with


_M_ _[{]_ [31] _[}]_ = 1 + _x_ 1 + _x_ 2(2) + _x_ 3 + _x_ 1 _x_ 2(2) + _x_ 2 _x_ 3(2) (9.9)


The multi-collinear cut of _f_ ( _M_ ) is easily seen to be just

    - _dαασσii_ _× ∂x_ 1 _,···xLf_ ( _M_ _[σ]_ ) _|x_ 1= _···_ = _xL_ =0 (9.10)


We are now ready to see why the logarithm of the amplitude is so natural from
a purely combinatorial point of view. Let us return to looking at _M_ _[{]_ [31] _[}]_ . Observe
that while _M_ is itself and irreducible polynomial, _M_ _[{]_ [31] _[}]_ factorizes as


_M_ _[{]_ [31] _[}]_ = [1 + _x_ 1 + _x_ 3][1 + _x_ 2(2)] (9.11)


Note that the second factor is just the _M_ polynomial made of the undeleted variables,
while the first factor is the generating function made of the variables with only terms
in correct order kept.
This is a general statement. For any _σ_, let _σ_ ¯ be the complementary set. Then







_M_ _[σ]_ =




 1 +




  _xσi_ +

_i_ _i<j_ ; _σi_



_xσixσj_ + _· · ·_

_i<j_ ; _σi<σj_





 _× M_ _[σ]_ [¯] (9.12)



To illustrate with a more non-trivial example, say for _L_ = 5 and _σ_ = _{_ 415 _}_, we have


_M_ _[{]_ [415] _[}]_ = (1 + _x_ 1 + _x_ 4 + _x_ 5 + _x_ 1 _x_ 5 + _x_ 4 _x_ 5) _×_ (1 + _x_ 2(2) + _x_ 3(3) + _x_ 2 _x_ 3(23)) (9.13)


Note that if _σ_ is anything other than the empty set, the factorization in nontrivial. Because of this factorization, it is natural to consider the log of the object.
Then, we see that for any string _σ_ of length 0 _< l < L_,


_∂x_ 1 _···xL_ log _M_ _[σ]_ = 0 (9.14)


                 - 22                  

We thus learned something remarkable: if we take the log of the amplitude,
then the cut taking any number _l_ _< L_ of the loop variables into the collinear region
vanishes! Only if all _L_ lines are taken into the collinear region together, can we get
something non-zero. This explains why the log of the amplitude only has a log [2]

divergence. We get a log [2] divergence from each loop momentum brought into this
collinear region. For the amplitude itself, we can bring all _L_ lines into the collinear
region one at a time, and thus we get the log [2] _[L]_ IR divergence. However for the log
of the amplitude, since all _L_ lines must be brought in the collinear region together
we just get a single overall log [2] divergence. (Note that had even this limit given us
no residue, the log would have have been completely IR divergence free!).

Very interestingly, the logarithm of the amplitude doesn’t have the property,
familiar for the amplitude itself, of having “unit leading singularities”. If all _L_ lines
are taken into the collinear region in an order _σ_ = ( _σ_ 1 _, · · ·_ _, σL_ ), then the residue is







_xixj_ + _· · ·_

_i<j_ ; _σi<σj_






 _|xi_ =0 (9.15)



_∂x_ 1 _···xL_ log




 1 +




 _xi_ +

_i_ _i<j_ ; _σi_



Note that unlike the amplitude itself, which is only non-vanishing for _σ_ =
(1 _,_ 2 _, · · ·_ _, n_ ), the log of the amplitude vanishes in this case, since

 




 1 +




 _xi_ +

_i_ _i<j_ ; _σi_



_xixj_ + _· · ·_

_i<j_ ; _σi<σj_



 = (1 + _x_ 1) _· · ·_ (1 + _xn_ ) (9.16)



maximally factorizes! In the other extreme, if _σ_ = ( _n, · · ·_ _,_ 1) is oppositely ordered
to (1 _, · · ·_ _, n_ ), then we have


_∂x_ 1 _···xL_ (1 + _x_ 1 + _· · · xL_ ) _|xi_ =0 = ( _L −_ 1)! (9.17)


In general, we can find residues ranging from 1 to ( _L −_ 1)!. For instance, at 4 loops,
we have the non-vanishing residues 1,2,3, 4 and 6, coming from the following paths:


1 : (2 _,_ 3 _,_ 4 _,_ 1)(2 _,_ 4 _,_ 1 _,_ 3)(3 _,_ 1 _,_ 4 _,_ 2)(4 _,_ 1 _,_ 2 _,_ 3) 2 : (2 _,_ 4 _,_ 3 _,_ 1)(3 _,_ 2 _,_ 4 _,_ 1)(4 _,_ 1 _,_ 3 _,_ 2)(4 _,_ 2 _,_ 1 _,_ 3)


3 : (3 _,_ 4 _,_ 1 _,_ 2) 4 : (3 _,_ 4 _,_ 2 _,_ 1)(4 _,_ 2 _,_ 3 _,_ 1)(4 _,_ 3 _,_ 1 _,_ 2) 6 : (4 _,_ 3 _,_ 2 _,_ 1) 0 : other (9.18)


The log of the amplitude has another fascinating feature, which we can see
already starting at 2-loops, where


log _M_ 2 = (12) _−_ (1)(2) (9.19)


Note that the 2-loop amplitude puts the positivity restriction _⟨D_ (1) _D_ (2) _⟩_ _>_ 0
on the lines, but “1 _−_ loop [2] ” part does not put any positivity restrictions on them.
Indeed, we can think of this as the sum over two regions, with _⟨D_ (1) _D_ (2) _⟩_ _>_ 0 and


                 - 23                  

_⟨D_ (1) _D_ (2) _⟩_ _<_ 0. Thus, the sum that gives the log is the form associated with the
region where _⟨D_ (1) _D_ (2) _⟩_ _<_ 0 ! The pattern continues at all higher loops. At 3-loops
we have three positivity conditions involving


_{⟨D_ (1) _D_ (2) _⟩, ⟨D_ (1) _D_ (3) _⟩, ⟨D_ (2) _D_ (3) _⟩}_ (9.20)


For the amplitude they are all positive, _M_ 3 = _{_ + + + _}_ while for the log of the
amplitude (9.8) we get a sum of terms


(log _M_ ) [3] _[−][loop]_ = _{_ + _−−} ⊕{−_ + _−} ⊕{−−_ + _} ⊕_ 2 _{−−−}_ (9.21)


At 4 loops we have 6 positivity conditions,


_{⟨D_ (1) _D_ (2) _⟩, ⟨D_ (1) _D_ (3) _⟩, ⟨D_ (1) _D_ (4) _⟩, ⟨D_ (2) _D_ (3) _⟩, ⟨D_ (2) _D_ (4) _⟩, ⟨D_ (3) _D_ (4) _⟩}_ (9.22)


For the amplitude we have _M_ 4 = _{_ + + + + ++ _}_ . The log is


(log _M_ ) [4] _[−][loop]_ = (1234) _−_ [(12)(34) + (13)(24) + (14)(23)]


+ [(12)(3)(4) + (13)(2)(4) + (14)(2)(3) + (23)(1)(4) + (24)(1)(3) + (34)(1)(2)]


+ 2 [(123)(4) + (124)(3) + (134)(2) + (234)(1)] _−_ 6 (1)(2)(3)(4) (9.23)


and can be decomposed into a sum of regions as


(log _M_ ) [4] _[−][loop]_ = _R_ 1 _⊕_ 2 _R_ 2 _⊕_ 3 _R_ 3 _⊕_ 4 _R_ 4 _⊕_ 6 _R_ 6 (9.24)


where


_R_ 1 = _{−−−_ + ++ _} ⊕{−−_ + + _−_ + _} ⊕{−−_ + + + _−} ⊕{−_ + _−−_ ++ _}_


_⊕{−_ + _−_ + + _−} ⊕{−_ + + _−−_ + _} ⊕{−_ + + _−_ + _−} ⊕{−_ + + + _−−}_


_⊕{_ + _−−−_ ++ _} ⊕{_ + _−−_ + _−_ + _} ⊕{_ + _−_ + _−−_ + _} ⊕{_ + _−_ + _−_ + _−}_


_⊕{_ + _−_ + + _−−} ⊕{_ + + _−−−_ + _} ⊕{_ + + _−−_ + _−} ⊕{_ + + _−_ + _−−}_


_R_ 2 = _{−−−−_ ++ _} ⊕{−−−_ + _−_ + _} ⊕{−−−_ + + _−} ⊕{−−_ + _−−_ + _}_


_⊕{−−_ + _−_ + _−} ⊕{−_ + _−−−_ + _} ⊕{−_ + _−_ + _−−} ⊕{−_ + + _−−−}_


_⊕{_ + _−−−_ + _−} ⊕{_ + _−−_ + _−−} ⊕{_ + _−_ + _−−−} ⊕{_ + + _−−−−}_


_R_ 3 = _{−−_ + + _−−} ⊕{−_ + _−−_ + _−} ⊕{_ + _−−−−_ + _}_


_R_ 4 = _{−−−−−_ + _} ⊕{−−−−_ + _−} ⊕{−−−_ + _−−} ⊕{−−_ + _−−−}_


_⊕{−_ + _−−−−} ⊕{_ + _−−−−−}_


_R_ 6 = _{−−−−−−}_


While the expansion of the logarithm itself includes terms with both plus and minus
signs, remarkably, in all cases we get a sum over regions, with all positive integer
coefficients, reflecting the allowed leading singularities for different orderings of approaching the collinear region.


                 - 24                  

### **10. Some Faces of the Amplituhedron**

In this section, we study a few classes of lower-dimensional faces of the amplituhedron, that are particularly easy to triangulate. The canonical form associated with
these faces computes corresponding cuts of the full integrand.


**Ladders** **and** **Next-to-Ladders**


Already in [1], we discussed a set of faces that are extremely easy to understand.
Let’s take all _L_ loops to cut the line (12), by sending all the _wi_ _→_ 0. The positivity
conditions just become ( _xi −_ _xj_ )( _zi −_ _zj_ ) _<_ 0. In whatever configuration of _x_ ’s we
have, they are ordered in some way, say _x_ 1 _<_ _· · ·_ _<_ _xL_, and this condition tells us
that the _z_ ’s are oppositely ordered _z_ 1 _>_ _· · ·_ _>_ _zL_ . The _yi_ just have to be positive.
The associated form is then trivially



1
_. . ._ [1]
_y_ 1 _yL_



1
_x_ 1



1 1
_. . ._
_x_ 2 _−_ _x_ 1 _xL −_ _xL−_ 1



1
_zL_



1 1
_. . ._ (10.1)
_zL−_ 1 _−_ _zL_ _z_ 1 _−_ _z_ 2



which corresponds to the unique “ladder” local diagrams that can contribute to this
cut; to see this propagator structure explicitly, we simply regroup the terms in the
product as 1 _/_ ( _y_ 1 _· · · yL_ ) multiplying


1 1 1
_×_ [1] (10.2)
_x_ 1 ( _x_ 2 _−_ _x_ 1)( _z_ 1 _−_ _z_ 2) _[× · · · ×]_ ( _xL −_ _xL−_ 1)( _zL−_ 1 _−_ _zL_ ) _[×]_ _zL_


We can move on to consider “next-to-ladder” cuts. Suppose for instance that
( _L_ _−_ 1) of the loop variables cutting (12), while the _L_ ’th loop cuts (34) so that
_yL_ _→_ 0. The positivity for the ( _L −_ 1) lines is simply _x_ 1 _<_ _x_ 2 _<_ _· · ·_ _<_ _xL−_ 1 and
_z_ 1 _> z_ 2 _> · · · > zL−_ 1 as above. The mutual positivity conditions are just that


_wLyi_ _>_ ( _xi −_ _xL_ )( _zi −_ _zL_ ) (10.3)


The canonical form is very easy to determine. We simply consider all the for _L_
orderings of the _x_ ’s for which _x_ 1 _< · · ·_ _, < xL−_ 1, i.e. the orderings [ _x_ 1 _, · · ·_ _, xL−_ 1 _, xL_ ],

[ _x_ 1 _, · · ·_ _, xL, xL−_ 1], _· · ·_, [ _xL, x_ 1 _, · · ·_ _, xL−_ 1]; similarly, we consider all the analogous
orderings of the _z_ ’s: [ _zL, zL−_ 1 _, · · ·_ _, z_ 1], [ _zL−_ 1 _, zL, · · ·_ _, z_ 1], _· · ·_, [ _zL−_ 1 _, · · ·_ _, z_ 1 _, zL_ ], Then
if in the ordering, either both _xk_ _>_ _xL_, _zk_ _>_ _zL_ or _xk_ _<_ _xL, zk_ _<_ _zL_, we have
_yk_ _>_ ( _xk −_ _xL_ )( _zk −_ _zL_ ) _/wL_, otherwise we just have _yk_ _>_ 0. The corresponding form
is


  
[ _xσ_ 1 _−_ 1 _[,][ · · ·]_ _[, x][σ]_ _L_ _[−]_ [1][][] _[z][ρ]_ 1 _[−]_ [1] _[,][ · · ·]_ _[, z][ρ][−]_ _L_ [1][]] (10.4)
_σ_ 1 _<···<σL−_ 1 _,ρ_ 1 _>···>ρL−_ 1




- [ _yk −_ _w_ 1 _L_ [(] _[x][k][ −]_ _[x][L]_ [)(] _[z][k][ −]_ _[z][L]_ [)]] _[−]_ [1] _[ σ][k]_ _[> σ][L][, ρ][k]_ _[> ρ][L]_ or _σk_ _< σL, ρk_ _< ρL_
_yk_ _[−]_ [1] otherwise


             - 25              






_×_



_L−_ 1



_k_ =1


This expression sums the cuts for local diagrams of the form


**Corner** **Cuts**


We can systematically approach the faces of the amplituhedron where every line
is one of the double-cut configurations. We already know what happens with the
unitarity double-cut on general grounds. So we are left with the “corner cuts”,
where any line either passes through _Zi_, or lies in the plane ( _Zi−_ 1 _ZiZi_ +1). We use
different convenient gauge fixings: for the case of lines passing through 1, and lines
in the plane (412), we use




    - 1 0 0 0
_D_ through 1 =
0 _y_ 1 _z_




- - _u_ 1 0 0
_,_ _D_ in (412) = _−v_ 0 0 1




(10.5)



Note that
_⟨D_ through 1 _D_ in (412) _⟩_ = _−_ 1 (10.6)



is negative, and so we immediately learn that it is impossible to have lines of both
types in one corner! We can either have a collection of lines passing through 1, _or_ a
collection of lines lying in the plane (412). Suppose we approach the configuration
where all the lines path through 1, by starting with all the lines intersecting (41),
and sending the lines into the corner in some order, first _w_ 1 _→_ 0 _, · · ·_ _,_ then _wL_ _>_ 0.
This orders _w_ 1 _<_ _· · ·_ _<_ _wL_ and so _y_ 1 _>_ _· · ·_ _>_ _yL_, thus the form on this final corner
cut is just [ _yL, · · ·_ _, y_ 1]. Note that we see again something we have observed already
a number of times: the form on the cut depends not just on the geometry of the
ultimate configuration of lines, but also on the path taken to that configuration.

We can easily determine completely general corner cuts where all the lines are
of one type or the other. For instance, suppose we start with _L_ 1 lines cutting (14),
and _L_ 2 lines cutting (12), and that we send these lines to pass through the corners
1 and 2 in some order. If we parametrize the matrices as

        - 1 0 0 0 �� 0 1 0 0         
(10.7)

0 _yi_ 1 _zi_ _−αI_ 0 _βI_ 1



�� 0 1 0 0
_−αI_ 0 _βI_ 1




(10.7)



then the positivity conditions are just _yL_ 1 _>_ _· · ·_ _>_ _y_ 1 _, βL_ 2 _>_ _· · ·_ _>_ _β_ 1, with the
mutual positivity condition _ziβI_ _>_ 1, which just means _zi_ _>_ 1 _/β_ 1 for all _i_ . Then the


                 - 26                  

form is trivially

   

_I_



_α_ 1 _I_ _×_ [ _yL_ 1 _, · · ·_ _, y_ 1][ _βL_ 2 _, · · ·_ _, β_ 1] 
_i_



1
(10.8)
_zi −_ _β_ 1 _[−]_ [1]



This result generalizes trivially to the case with _L_ 1 lines cutting (41), _L_ 2 lines
cutting (12), _L_ 3 lines cutting (23) and _L_ 4 lines cutting (34), then taken to pass
through 1 _,_ 2 _,_ 3 _,_ 4.


These results are very simple and arise from a single local term. Much more
interesting are the mixed corner cuts, where we have the two different types of lines
passing through different corners. One case is still extremely simple, where the two
different lines pass through consecutive corners. Suppose we have _L_ 1 lines passing
through 1, and _L_ 2 lines lying in (123). It is trivial to see that


_⟨D_ through 1 _D_ lying in (123) _⟩_ = (14)through 1(23)lying in(123) _>_ 0 (10.9)


and so the mutual positivity between these two sets is automatically satisfied. The
form is then just the product of the form for the _L_ 1 lines and the _L_ 2 lines separately.
The non-trivial case is when the corner cuts are different lines in opposite corners.
Suppose we have _L_ 1 lines cutting (41) that were then sent to pass through 1 in order
( _L_ 1 _, · · ·_ _,_ 1), and _L_ 3 lines cutting (23) that were made to pass through (234) in order
(1 _, · · ·_ _, L_ 3).


For notational convenience we’ll parametrize the _D_ matrices using different variable
names in this case:




    - 1 0 0 0
_D_ through 1 =
0 _xi_ 1 _yi_




- _,_ _D_ lying in(234) = - 0 1 _a−I_ 1 0
0 0 _b_ _[−]_ _I_ [1] 1


 - 27  



(10.10)


Then the positivity conditions are



_x_ 1 _< · · · < xL_ 1 _,_ _a_ 1 _< · · · < aL_ 3 _,_ and _[x][i]_




_[x][i]_ + _[y][i]_

_aI_ _bI_




_>_ 1 (10.11)
_bI_



It is quite straightforward to triangulate this space; let us work out the case
_L_ 3 = 2 explicitly. Here the geometry is very similar to the last of our warmup
exercises. Suppose first that _b_ 1 _< b_ 2. Then the inequalities are just _xi/a_ 2 + _yi/b_ 2 _>_ 1
together with the restriction _x_ 1 _<_ _· · ·_ _<_ _xL_ 1. We simply order the _xi_ relative to _a_ 2.
If _xi_ _>_ _a_ 2, then we just have _yi_ _>_ 0 and the form is 1 _/yi_, while if _xi_ _<_ _a_ 2, we have
_Yi,_ 2 _>_ 0 and the form is 1 _/Yi,_ 2. Here we have defined



_Yi,_ 1 = _yi_ + _[b]_ [1] _[x][i]_




[1] _[x][i]_ _−_ _b_ 1 _, Yi,_ 2 = _yi_ + _[b]_ [2] _[x][i]_

_a_ 1 _a_ 2




_−_ _b_ 2 _._ (10.12)
_a_ 2



Thus, for _b_ 1 _< b_ 2, the form is just







1 1
_a_ 1( _a_ 2 _−_ _a_ 1) _b_ 1( _b_ 2 _−_ _b_ 1)




    
[ _· · ·_ _, xm, a_ 2 _, xm_ +1 _· · ·_ ]

_m_ _k_



_k_







(10.13)




- _Yk,_ _[−]_ 2 [1] _[k]_ _[≤]_ _[m]_
_yk_ _[−]_ [1] _k_ _> m_



If instead _b_ 2 _<_ _b_ 1, then we have to break _x_ space up into the three regions
between 0 _, a_ 12 _, a_ 2 where _a_ 12 = _[a]_ _a_ [1] 2 _[a]_ _b_ [2] 1 [(] _−_ _[b]_ [1] _a_ _[−]_ 1 _[b]_ _b_ [2] 2 [)] [.] [We] [have] [to] [sum] [over] [all] [the] [orderings] [of]

the _x_ ’s relative to _a_ 12 _, a_ 2’; for all the _xi_ _> a_ 2, the form in _y_ space is just 1 _/yi_, for the
_xi_ in the range _a_ 2 _>_ _xi_ _>_ _a_ 12 the _y_ form is just 1 _/Yi,_ 2, while for _a_ 12 _>_ _xi_ _>_ 0 the _y_
form is 1 _/Yi,_ 1. Thus in this case the form is



_Yk,_ _[−]_ 1 [1] _[,]_ _[k]_ _[≤]_ _[m]_
_Yk,_ _[−]_ 2 [1] _[,]_ _[m < k]_ _[≤]_ _[l]_
_yk_ _[−]_ [1] _k_ _> l_













1 1
_a_ 1( _a_ 2 _−_ _a_ 1) _b_ 1( _b_ 2 _−_ _b_ 1)




- 
[ _· · ·_ _, xm, a_ 12 _, xm_ +1 _, · · ·_ _, xl, a_ 2 _, xl_ +1 _, · · ·_ ]

_m≤l_ _k_



_k_

















(10.14)

The full form is just the sum of these two pieces. While this result is completely
straightforward from triangulation, it gives rise to highly non-trival local expressions
even at comparatively low loop order. In the first really interesting case at 5 loops,
with _L_ 1 = 3 and _L_ 3 = 2, 19 local terms contribute to this cut, and when they are all
combined under a common denominator, the numerator has 325 terms.

There is another interesting feature of these cuts, that is not evident from any
traditional point of view but is obvious from the positive geometry. We have seen
that fixing the order in which the lines are brought to pass through 1, imposes the
constraint _x_ 1 _< · · · < xL_ 1. But, if we sum over all the different orderings, we simply
remove these ordering constraints! We then expect that the form simplifies greatly.
Indeed, if we stick with the case _L_ 3 = 2, then we just get several copies of the problem
_x/a_ 1 + _y/b_ 1 _>_ 1 _, x/a_ 2 + _y/b_ 2 _>_ 1, which we analyzed in our warmup section. Thus,
the sum over all the ways to start with _L_ 1 lines on (41) which are then sent through


                 - 28                  

1 (while sending _L_ 3 = 2 lines to lie in (234) in the usual fixed order), is






_i_



_yi_



1
_a_ 1( _a_ 2 _−_ _a_ 1)


**Internal** **Cuts**




1
_b_ 1( _b_ 2 _−_ _b_ 1)





[ _xi, a_ 2] [1]




[1] + [ _a_ 2 _, xi_ ] [1]

_Yi,_ 2 _yi_




(10.15)




[1] + [ _a_ 2 _, xi_ ] [1]

_Yi,_ 2 _yi_



1
+
_b_ 2( _b_ 1 _−_ _b_ 2)






_i_



_yi_




- [�]





[ _xi, a_ 12] [1]




[1] + [ _a_ 12 _, xi, a_ 2] [1]

_Yi,_ 1 _Yi,_



It is interesting that up to 4 loop order, every loop in the local expansion of the
amplitude touches the external lines, but this behavior is obviously not generic.
Starting at 5 loops, we have diagrams with purely internal loops, such as


are simply



_D_ (1) =






_,_








(10.16)



Note that the mutual positivity between _D_ (1) _D_ (3) and _D_ (2) _D_ (4) is automatic. The
geometry of the lines is


                 - 29                  

and so we can think of the lines as ( _AB_ )1 = [ˆ] 1 [ˆ] 2 _,_ ( _AB_ )2 = [ˆ] 2 [ˆ] 3 _,_ ( _AB_ )3 = [ˆ] 3 [ˆ] 4 _,_ ( _AB_ )4 = [ˆ] 1 [ˆ] 4,
where


ˆ1 = 1 + _σ_ (2 + _α_ (3 + _β_ 4)) _,_ ˆ2 = 2 + _α_ (3 + _β_ (4 _−_ _γ_ 1))
ˆ3 = 3 + _β_ (4 _−_ _γ_ (1 + _σ_ 2)) _,_ ˆ4 = 4 _−_ _γ_ (1 + _σ_ (2 + _α_ 3)) (10.17)



Now, it is easy to see that the remaining mutual positivity conditions between
_D_ (1) _, · · ·_ _, D_ (4) and the other _D_ ( _i_ ) are just satisfied by the lower-loop shifted amplitude; thus we conclude that on this cut the form is

_dα_ _dβ_ _dγ_ _dσ_



_dβ_

_α_ _β_



_dγ_

_β_ _γ_



_dσ_

_γ_ _σ_



(10.18)
_σ_ _[×][ M][ L][−]_ [4][(ˆ1] _[,]_ [ ˆ2] _[,]_ [ ˆ3] _[,]_ [ ˆ4)]


### **11. Four Particle Outlook**

We have only scratched the surface of the rich amplituhedron geometry controlling
four-particle scattering in planar _N_ = 4 SYM at all loop order. There is obviously
much more to be done just along the elementary lines of this note, minimally in
further continuing a systematic exploration of other facets of the geometry, corresponding to different classes of cuts of physical interest. But we close with a few
comments about some different avenues of exploration.
In this note we have approached the determination of the integrand for fourparticle scattering by directly “triangulating” the amplituhedron geometry. The _L−_
loop geometry is defined in a self-contained way, as a subspace living inside _L_ copies
of space-time realized as _G_ (2 _,_ 4). In particular, no-where do we need to refer to lowerloop, higher- _k_ amplitudes, as in necessary in the BCFW recursion approach [14] to
loop integrands [11]. Nonetheless, it is likely that some natural connection exists with
the full problem, and perhaps a broader view of the bigger amplituhedron geometry in
which the four-particle problem sits will be important for systematically determining
the all-loop integrand. Certainly, experience with the positive Grassmannian [2, 4]
strongly suggests that different faces can’t be properly understood in isolation.
As we have seen, the approach to computing the integrand by triangulating
the amplituhedron does not give us the familiar expansions that are manifestly local.
This is of course not surprising; however, what _is_ surprising is that some special local
expansions expose yet _another_ aspect of positivity, that we are not making apparent
in the triangulation approach. As also mentioned in [1], we are still clearly missing
a picture of the form Ωwhich is analogous to one available for convex polygons,
determined by a literal volume of the _dual_ polygon. We don’t yet have a notion of
a “dual amplituhedron”, but there is a powerful indication that such a formulation
must exist: the form Ωis itself positive, inside the amplituhedron! More specifically,
we can write the _L−_ loop integrand as



Ω _L_ ( _ABi_ ) =



_L_

- _⟨ABid_ [2] _Ai⟩⟨ABid_ [2] _Bi⟩ML_ ( _ABi_ ) (11.1)


_i_ =1


    - 30    

Then, we claim that when the ( _AB_ ) _i_ are taken to lie inside the amplituhedron,


_ML_ ( _ABi_ ) _>_ 0 (11.2)


We will return to exploring this fact at greater in length in [15]. We stress that this
property is _not_ manifest term-by-term in the amplituhedron triangulation expansion
of the integrand. Random forms of the local expansion also don’t make this remarkable property manifest term-by-term, but there are particularly nice forms of local
expansion that do make this manifest. As we will discuss in [15], we suspect that
this surprising positivity property of the integrand is pointing the way to a more
direct and intrinsic, triangulation-independent definition for the canonical form Ω
associated with the amplituhedron.
From a mathematical point of view, it is interesting that the study of amplitudes
leads to stratifications of various collections of objects in projective space. If we
consider a collection of _n_ vectors in _k_ dimensions, together with a cyclic structure on
this data, we are led to the beautiful stratification of the space given by the positive
Grassmannian. Even just with the the four-particle amplituhedron, we see something
new, not needing a cyclic structure on the objects: given a collection of _L_ 2-planes
in 4 dimensions, the positivity conditions are fully permutation invariant between
the _L_ lines. Just as with the positive Grassmannian, it is natural to expect the cell
structure of the amplituhedron to be determined in a fundamentally combinatorial
way. The fascinating path-dependence of the forms associated with the cuts, together
with the combinatorics that arise just in the simple discussion of the multi-collinear
limit, are perhaps indications of an underlying combinatorial structure.
The four-particle amplitude is a truly remarkable object. At the level of the
integrand, at multi-loop order it contains non-trivial information about all the more
complicated multi-particle amplitudes in the theory. At the level of the final integrated expression, we have a function that smoothly interpolates between a picture
of “interacting gluons” at weak coupling to “minimal area surface in AdS space” [16]
at strong coupling. We have explored a reformulation of this physics in terms of
a simple to define, yet rich and intricate geometry. We hope that this will lead us
a more direct understanding of how the picture of “gluons” and “strings” arise as
different limits of a single object. As a small step in this direction, it is encouraging
to find a natural understanding, intrinsic to the geometry, of the behavior of the
amplitude in the multi-collinear region, and an associated intrinsic-to-the-geometry
rationale for taking the log of the amplitude. Trying to more completely determine
the IR singular behavior of the integrand of the amplitude is an ideal laboratory to
connect our approach to the loop integrand with the final integrated expressions, and
especially to ideas related to integrability. Indeed the coefficient of the log [2] infrared
divergence of the log of the amplitude is given by the cusp anomalous dimension,
which was brilliantly determined using integrability in [17–19]. It is notable that
this approach makes crucial use of a spectral parameter, something which is absent


                 - 31                  

in our present discussion of the amplituhedron. Given the spectral deformation of
on-shell diagrams given in [20,21], it is natural to ask whether a similar deformation
can be found directly at the level of the amplituhedron.

### **Acknowledgements**


We thank Jake Bourjaily, Freddy Cachazo, Simon Caron-Huot, Johannes Henn, Andrew Hodges, Jan Plefka, Dave Skinner and Matthias Staudacher for stimulating
discussions. N. A.-H. is supported by the Department of Energy under grant number DE-FG02-91ER40654. J. T. is supported in part by the David and Ellen Lee
Postdoctoral Scholarship and by DOE grant DE-FG03-92-ER40701 and also by NSF
grant PHY-0756966.

### **References**


[1] N. Arkani-Hamed and J. Trnka, arXiv:1312.2007 [hep-th].


[2] A. Postnikov, arXiv:math/0609764.


[3] V. V. Fock and A. B. Goncharov, Ann. Sci. L’Ecole Norm. Sup. (2009),

arXiv:math.AG/0311245.


[4] N. Arkani-Hamed, F. Cachazo, C. Cheung and J. Kaplan, JHEP **1003**, 020 (2010)

[arXiv:0907.5418 [hep-th]]; N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo,

A. B. Goncharov, A. Postnikov and J. Trnka, arXiv:1212.5605 [hep-th].


[5] A. Hodges, JHEP **1305**, 135 (2013) [arXiv:0905.1473 [hep-th]].


[6] Z. Bern, M. Czakon, L. J. Dixon, D. A. Kosower and V. A. Smirnov, Phys. Rev. D

**75**, 085010 (2007) [hep-th/0610248].


[7] Z. Bern, L. J. Dixon and V. A. Smirnov, Phys. Rev. D **72**, 085001 (2005)

[hep-th/0505205].


[8] Z. Bern, J. J. M. Carrasco, H. Johansson and D. A. Kosower, Phys. Rev. D **76**,

125020 (2007) [arXiv:0705.1864 [hep-th]].


[9] J. L. Bourjaily, A. DiRe, A. Shaikh, M. Spradlin and A. Volovich, JHEP **1203**, 032

(2012) [arXiv:1112.6432 [hep-th]].


[10] B. Eden, P. Heslop, G. P. Korchemsky and E. Sokatchev, Nucl. Phys. B **862**, 450

(2012) [arXiv:1201.5329 [hep-th]].


[11] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, S. Caron-Huot and J. Trnka, JHEP

**1101**, 041 (2011) [arXiv:1008.2958 [hep-th]].


[12] S. Caron-Huot, JHEP **1105**, 080 (2011) [arXiv:1007.3224 [hep-ph]].


                 - 32                  

[13] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo and J. Trnka, JHEP **1206**, 125 (2012)

[arXiv:1012.6032 [hep-th]].


[14] R. Britto, F. Cachazo, B. Feng and E. Witten, Phys. Rev. Lett. **94**, 181602 (2005)

[hep-th/0501052].


[15] N. Arkani-Hamed, A. Hodges and J. Trnka, to appear.


[16] L. F. Alday and J. M. Maldacena, JHEP **0706**, 064 (2007) [arXiv:0705.0303

[hep-th]].


[17] N. Beisert and M. Staudacher, Nucl. Phys. B **670**, 439 (2003) [hep-th/0307042].


[18] N. Beisert, B. Eden and M. Staudacher, J. Stat. Mech. **0701**, P01021 (2007)

[hep-th/0610251].


[19] B. Eden and M. Staudacher, J. Stat. Mech. **0611**, P11014 (2006) [hep-th/0603157].


[20] L. Ferro, T. Lukowski, C. Meneghelli, J. Plefka and M. Staudacher, arXiv:1308.3494

[hep-th].


[21] L. Ferro, T. Lukowski, C. Meneghelli, J. Plefka and M. Staudacher, Phys. Rev. Lett.

**110**, no. 12, 121602 (2013) [arXiv:1212.0850 [hep-th]].


                 - 33                  

