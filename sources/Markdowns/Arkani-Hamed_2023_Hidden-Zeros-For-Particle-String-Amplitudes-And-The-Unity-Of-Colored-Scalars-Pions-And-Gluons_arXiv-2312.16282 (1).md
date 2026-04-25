Prepared for submission to JHEP

## **Hidden zeros for particle/string amplitudes and the** **unity of colored scalars, pions and gluons**


**Nima** **Arkani-Hamed,** _[a]_ **Qu** **Cao** **(** **`曹趣`** **),** _[b,c]_ **Jin** **Dong** **(** **`董晋`** **),** _[b,d]_ **Carolina** **Figueiredo,** _[e]_

**Song** **He** **(** **`何颂`** **)** _[b,f,g]_

_aSchool_ _of_ _Natural_ _Sciences,_ _Institute_ _for_ _Advanced_ _Study,_ _Princeton,_ _NJ,_ _08540,_ _USA_

_bCAS_ _Key_ _Laboratory_ _of_ _Theoretical_ _Physics,_ _Institute_ _of_ _Theoretical_ _Physics,_ _Chinese_ _Academy_
_of_ _Sciences,_ _Beijing_ _100190,_ _China_
_cZhejiang_ _Institute_ _of_ _Modern_ _Physics,_ _Department_ _of_ _Physics,_ _Zhejiang_ _University,_ _Hangzhou,_
_310027,_ _China_
_dSchool_ _of_ _Physical_ _Sciences,_ _University_ _of_ _Chinese_ _Academy_ _of_ _Sciences,_ _No.19A_ _Yuquan_ _Road,_
_Beijing_ _100049,_ _China_
_eJadwin_ _Hall,_ _Princeton_ _University,_ _Princeton,_ _NJ_ _08540,_ _USA_
_f_ _School_ _of_ _Fundamental_ _Physics_ _and_ _Mathematical_ _Sciences,_ _Hangzhou_ _Institute_ _for_ _Advanced_
_Study_ _&_ _ICTP-AP,_ _UCAS,_ _Hangzhou_ _310024,_ _China_
_gPeng_ _Huanwu_ _Center_ _for_ _Fundamental_ _Theory,_ _Hefei,_ _Anhui_ _230026,_ _P._ _R._ _China_

_E-mail:_ `[arkani@ias.edu](mailto:arkani@ias.edu)`, `[qucao@zju.edu.cn](mailto:qucao@zju.edu.cn)`, `[dongjin@itp.ac.cn](mailto:dongjin@itp.ac.cn)`,
`[cfigueiredo@princeton.edu](mailto:cfigueiredo@princeton.edu)`, `[songhe@itp.ac.cn](mailto:songhe@itp.ac.cn)`


Abstract: Recent years have seen the emergence of a new understanding of scattering
amplitudes in the simplest theory of colored scalar particles–the Tr( _ϕ_ [3] ) theory–based on
combinatorial and geometric ideas in the kinematic space of scattering data. In this paper
we report a surprise: far from the toy model it appears to be, the “stringy” Tr( _ϕ_ [3] ) amplitudes
secretly _contains_ the scattering amplitudes for pions, as well as non-supersymmetric gluons,
in any number of dimensions. The amplitudes for the different theories are given by one
and the same function, related by a simple shift of the kinematics. This discovery was
spurred by another fundamental observation: the tree-level Tr( _ϕ_ [3] ) field theory amplitudes
have a hidden pattern of zeros when a special set of non-planar Mandelstam invariants
is set to zero. These zeros are not manifest in Feynman diagrams but are made obvious
by the connection of these amplitudes to the new understanding of associahedra arising
from “causal diamonds” in kinematic space. Furthermore, near these zeros, the amplitudes
simplify, by factoring into a non-trivial product of smaller amplitudes. Remarkably the
amplitudes for pions and gluons are observed to _also_ vanish in the same kinematical locus.
These properties for Tr( _ϕ_ [3] ) amplitudes hold and further generalize to the “stringy” Tr( _ϕ_ [3] )
amplitudes. The “kinematic causal diamond” picture suggests a unique shift of the kinematic
data that preserves the zeros, and this shift is precisely the one that unifies colored scalars,
pions, and gluons into a single object. We will focus in this paper on explaining the hidden
zeros and factorization properties and the connection between all the colored theories,
working for simplicity at tree level. Subsequent works will describe this new formulation
for the Non-linear Sigma Model and non-supersymmetric Yang-Mills theory, at all loop
orders.


**Contents**


**1** **From** **Toy** **Models** **to** **The** **Real** **World** **Via** **Numerators** **and** **Zeros** **1**


**2** **Tr** ( _ϕ_ [3] ) **Theory** **and** **the** **Associahedron** **4**
2.1 The kinematic mesh 5
2.2 The ABHY associahedron 8
2.3 The Minkowski summands and the mesh 9


**3** **Zeros** **and** **Factorizations** **of** **Tr** ( _ϕ_ [3] ) **Tree** **Amplitudes** **10**
3.1 Zeros and factorizations   - two simple examples 10
3.2 Zeros and factorizations   - general statement 14


**4** **The** **Non-linear** **Sigma** **Model** **17**
4.1 Zeros and the soft limit 18
4.2 Factorizations 18


**5** **Yang-Mills** **Theory** **21**


**6** **Stringy** **Tr** ( _ϕ_ [3] ) **22**
6.1 Zeros of Tr( _ϕ_ [3] ) string amplitudes 25
6.2 Factorization around the zeros 26


**7** **Stringy** _δ_ **eformation** **32**
7.1 Uniqueness of kinematical shift 34
7.2 Realization of the shift on momenta 35
7.3 4-point amplitudes 35
7.4 _α_ _[′]_ _δ_ _∈_ (0 _,_ 1) and the Non-linear Sigma Model 37
7.5 _α_ _[′]_ _δ_ = 1 and scaffolded gluons 41


**8** **Outlook** **48**


**Bibliography** **51**


**1** **From** **Toy** **Models** **to** **The** **Real** **World** **Via** **Numerators** **and** **Zeros**


Over the last few decades, a rich combinatorial and geometric structure underlying scattering amplitudes has been revealed. These descriptions have been most successful in the
context of theories, such as planar _N_ = 4 super-Yang-Mills (SYM) [1] and the Tr( _ϕ_ [3] )
theory for colored scalars [2–4], for which the amplitudes are relatively simple. Speaking
most invariantly, these are theories for which the amplitudes can be entirely determined


1


by their long-distance singularities, for instance, their factorization properties on massless
poles at tree level. Loosely speaking, the combinatorics and geometry provide an alternate
understanding of the rich and intricate pattern of **denominators** of the amplitude, which
turn out to non-trivially determine the entire amplitude as well.
But as we turn towards describing much more interesting and physically relevant theories, such as the non-supersymmetric gauge interactions of the Standard Model, we must
incorporate a qualitatively new feature present in the amplitudes. At the most basic and
concrete level, there are **numerator** factors associated with the more interesting interactions vertices of the realistic Lagrangians. Of course even _N_ = 4 SYM has such vertices, so
the more precise and invariant statement is that more interesting and realistic theories have
new “poles at infinity”, not associated simply with massless factorizations, which must be
incorporated in any new combinatorial/geometric formulation of this physics. Such poles
are absent in planar _N_ = 4 SYM (as one consequence of the famous hidden “dual conformal
invariance” of the theory [5]), as well as in Tr( _ϕ_ [3] ) theory (a consequence of a cousin hidden
“projective invariance” of the amplitudes [2]). Poles at infinity are naturally associated with
non-trivial numerator factors, whose presence and purpose in life must be exposed in the
next phase of the adventure of connecting combinatorial geometry to the real world.
The most obvious place to search for new structure associated with numerators is to
understand whether these give rise to interesting patterns of **zeros** of the amplitude - so
this is where we start. We will begin by studying the simplest theory of colored scalars,
Tr( _ϕ_ [3] ) theory, which has been much studied recently from the new perspectives of tropical
geometry, _u_ -variables and surfacehedra [3, 4, 6, 7]. This may appear to be an odd starting
point since the Tr( _ϕ_ [3] ) theory is precisely the most “overly simple” theory with **no** numerator
factors in its amplitude! And yet as we will see, even this seemingly boring theory _does_ have
a surprising and rich pattern of amplitude zeroes, and what is more, this pattern extends
to much more interesting and realistic theories of pions and gluons, revealing a striking
hidden unity between these three theories, which as we will show are in a precise sense
“contained” in each other. It is well-known that the traditional double copy relations [8–13]
(see also the recent reviews [14–16] and the references therein) have established a broad web
of interconnected theories. However, our results offer a new prescription for understanding
the relationships between these theories.
The presence of these hidden zeroes, at least for the Tr( _ϕ_ [3] ) theory, is not at all manifest
in the diagrammatic expansion for the amplitude, but _is_ made obvious by the understanding
of the Tr( _ϕ_ [3] ) amplitudes as the so-called “canonical form” of the so-called ABHY associahedron polytope, which we review in section 2. The zeros are connected with the fact that
ABHY associahedron is built out of simpler lower-dimensional objects - it is a Minkowski
sum of simplices. As we will see in section 3, by turning off a sufficient number of such
building blocks the polytope collapses and the amplitude vanishes. This geometric picture
also tells us that in the last step before the polytope collapses, it takes the form of a “sandwich”, with an interval separating opposite facets of the associahedron. This implies that
the amplitude factorizes into lower point amplitudes, in a completely predictable fashion. It
is fascinating to discover a new sort of factorization of amplitudes, which has nothing to do
with the usual factorization on poles, but instead characterizes the behavior of amplitudes


2


as we approach the hidden zeros.
Of course the behavior of amplitudes near poles is perhaps the best studied aspect of
the physics of particle scattering. By stark contrast, the kinematic locus where amplitudes
vanish has hardly been explored, and a clear interpretation of our zeros in familiar physical
terms is still lacking. Indeed both the zeros and factorization near zeros are properties of the
whole amplitude, not features manifest from the Feynman diagram perspective; they are
instead made manifest by the alternative geometric description of the amplitudes provided
by the associahedron.
Amazingly, we will find that exactly the same patterns of zeros and an avatar of the
factorization near zeros generalizes to all interesting theories of colored particles: the Nonlinear Sigma Model (NLSM) for pions, as well as gluons in Yang-Mills theory (YM). In
sections 4 and 5, we explain how this generalization works. The universality of these zeros
seen in other colored theories is especially surprising given that no obvious associahedron-ic
formulation for these theories is known.
However, as we will see, there _is_ a beautiful reason for the universality of these zeros,
which turn out to be deeply related to a surprising relation between these colored theories
revealed upon understanding a unified “stringy” descriptions of all these amplitudes. These
stringy generalizations have all the zeros and factorization patterns of the field theory
amplitudes and in fact generalize them to infinite new families of zero/factorization patterns.
They also allow us to see that amplitudes for colored scalars, pions, and gluons are all
given by a single function, expanded about different points in the kinematic space. This
remarkable connection between Tr( _ϕ_ [3] ) scalars, pions, and gluons will be explored at length
in sections 6 and 7. This single function is originally known as the _n_ -point Koba-Nielsen
string amplitudes [17], thus the zeros and factorization properties of all these theories at
tree level ultimately come from (bosonic) string theory.
Our goal in this paper is to explain the hidden zero/factorization patterns in the simplest possible setting and use this to motivate the new descriptions for amplitudes of pions
and gluons arising from a simple kinematic shift of the Tr( _ϕ_ [3] ) theory. To keep the discussion
as simple as possible, for the story of zeros and factorization we will focus on tree-level amplitudes; this will already be enough to suggest the kinematic shift relating all the colored
theories, that naturally generalizes to all loop orders. With this impetus as a starting point,
we will take up a detailed description of both the Non-linear Sigma Model and Yang-Mills
amplitudes from this point of view in upcoming works [18, 19].


**Note** **added:** After the first version appeared on arXiv, we were notified that some zeros of
the dual resonant amplitudes have also been studied in the early days of string theory [20].
Using the monodromy relations, it has been shown that the tachyon amplitudes vanish
under the same kinematic condition we found for stringy Tr( _ϕ_ [3] ) here. In addition, more
zero conditions that involve multiparticle Mandlestam variables are considered, as well as
the obvious extensions of the zeros of amplitudes for excited states, where the conditions
depend solely on Mandelstam variables and not on Lorentz products containing polarization
vectors, which differs from the results presented here.


3


**Figure** **1** : 6-point momentum polygon.


**2** **Tr** ( _ϕ_ [3] ) **Theory** **and** **the** **Associahedron**


In this section we will review the associahedron construction presented in [2], and explain
in detail the pattern of zeros and factorizations for Tr( _ϕ_ [3] ) theory that is made obvious by
this construction. Henceforth we will focus on tree-level amplitudes. However, since there
is an analogous Minkowski sum picture for polytopes describing loop integrands [3, 21], we
expect these observations to generalize at loop level.
The theory we are interested in is a theory of colored massless scalars interacting via a
cubic interaction, described by the following Lagrangian:


_L_ Tr( _ϕ_ 3) = Tr( _∂ϕ_ ) [2] + _g_ Tr( _ϕ_ [3] ) _,_ (2.1)



where _ϕ_ is an _N_ _× N_ matrix.
Since this is a scalar theory, the amplitude is exclusively a function of the Lorentz
invariant dot products of momenta: _pi · pj_ . There are _[n]_ [(] _[n][−]_ [1)] of these invariants, however



invariant dot products of momenta: _pi · pj_ . There are 2 of these invariants, however

momentum conservation gives us _n_ relations between them via [�] _j_ _[p][i]_ _[·][ p][j]_ [=] _[−][p]_ [2] _i_ [=] [0][,] [so]



we have _[n]_ [(] _[n][−]_ [1)]



we have _−_ _n_ independent invariants [1] . But there is no canonical way of imposing

2
the momentum conservation constraints, and no cyclically invariant choice of the _pi_ _· pj_
that form a basis. This is perhaps not a surprise, since there is nothing invariantly special
about dot products between pairs of momenta; many different linear combinations of these
objects can also be considered, so it is no surprise that a canonical basis for the invariants
does not exist ab initio; a better basis should reflect the exigencies of the physics we are
trying to describe.
Indeed, there is a much nicer basis for the kinematic invariants that is directly tailored
to our physical problem. Let us consider a fixed color ordering, which we can take to be
without loss of generality (1 _,_ 2 _, · · ·_ _, n_ ). We can keep track of the momenta of the particles



1Note that our discussion holds for general arbitrarily large spacetime dimension _D_ ; in any fixed spacetime dimension there are further “gram determinant” constraints on the dot products _pi_ _· pj_ for _n_ _>_ _D_
particles.


4


in a familiar way by drawing each _p_ _[µ]_ _i_ [as] [an] [edge] [of] [the] [“momentum] [polygon”] [(see] [figure] [1]
for the 6-point momentum polygon). We use the color ordering to order the momenta in the
polygon one after the other in the same way, ( _p_ _[µ]_ 1 _[, p][µ]_ 2 _[,][ · · ·]_ _[, p][µ]_ _n_ [)][.] [The] [fact] [that] [the] [polygon]
closes reflects momentum conservation [�] _i_ _[p]_ _i_ _[µ]_ [=] [0][.] [The] [vertices] [of] [this] [polygon] [can] [be]
associated with points _x_ _[µ]_ _i_ [so] [that] _[p][µ]_ _i_ [= (] _[x]_ _i_ _[µ]_ +1 _[−]_ _[x]_ _i_ _[µ]_ [)][,] [which] [makes] [momentum] [conservation]
manifest.
Now consider any chord in this polygon connecting the vertices ( _i, j_ ), and consider the
squared _Xi,j_ = ( _xi_ _−_ _xj_ ) [2] . The _Xij_ are naturally associated with the propagators that
appear in Feynman diagrams for this color ordering:


_Xi,j_ = ( _pi_ + _· · ·_ + _pj−_ 1) [2] _._ (2.2)


The tree amplitude is exclusively a function of these variables _A_ [Tr] _n_ [(] _[ϕ]_ [3][)] _≡A_ [Tr] _n_ [(] _[ϕ]_ [3][)] ( _{Xi,j}_ ).
Note that _Xi,i_ +1 = _p_ [2] _i_ [=] [0] [is] [not] [a] [dynamical] [variable,] [but] [all] [the] [rest] [of] [the] _[X][i,j]_ [are]
independent, and there are exactly _[n]_ [(] _[n]_ 2 _[−]_ [1)] _−_ _n_ of them. Hence the _Xi,j_ ’s give a complete

basis for all the kinematic invariants. This basis is much nicer than the one provided by
dot products: the _Xi,j_ are what appears directly in the amplitudes, the basis respects
the cyclic symmetry of the amplitudes, and all the momentum conservation conditions
are automatically taken into account: specifying an unconstrained set of _Xi,j_ fixes the
kinematical data for our scattering process.
Since the _Xi,j_ are a basis, we can express all the other kinematic invariants in terms of
them, including the dot product we began with. If we define


_ci,j_ = _−_ 2 _pi · pj,_ (2.3)


the relation is simply


_ci,j_ = _Xi,j_ + _Xi_ +1 _,j_ +1 _−_ _Xi,j_ +1 _−_ _Xi_ +1 _,j._ (2.4)


**2.1** **The** **kinematic** **mesh**


One particularly nice way of encoding the kinematic data of the scattering process is using
the **kinematic** **mesh** [22]. As we will see, the mesh is not only useful for organizing
the momentum invariants but will also be crucial for understanding the features of the
amplitude we will be studying throughout this paper.
The guiding principle used to build the mesh is equation (2.4). We associate each _Xi,j_
in (2.4) to the vertex of a square rotated by a 45 _[◦]_ angle (see figure 2 on the left), and the
corresponding _ci,j_ to the square. By placing these squares together we form a square grid
tilted 45 _[◦]_, that in the boundaries contains _Xi,i_ +1 = _p_ [2] _i_ [= 0][,] [since] [we] [are] [assuming] [massless]
particles. In figure 2, we present the mesh for the case of a 6-point process. We can see that
all the planar variables, _Xi,j_, are associated with grid points. Meanwhile the _non-planar_
dot product of momenta–which are the _ci,j_ with _i, j_ non-adjacent indices– correspond to
the square tiles. The mesh extends for infinitely long but reflects the cyclic symmetry of the
problem by an interesting “Mobius” symmetry, where we identify _Xi,j_ = _Xj,i_ and _ci,j_ = _cj,i_ .


5


relation satisfied by the four _X_ ’s in the vertices of the causal diamond is exactly that of
(2.4), where on the l.h.s. instead of _ci,j_, we have the sum of all the _ci,j_ ’s inside the causal
diamond under consideration (see figure 2 on the right).
We have already seen that the _Xi,j_ ’s form a basis for all kinematic invariants. However,
one can also build a basis in which we trade some of the planar variables for non-planar ones.
In particular, we are interested in the case where we get a basis including the planar variables
_Xi_ _[⋆]_ _,j_ _[⋆]_ of a particular triangulation, _T_ together with a set of non-planar Mandelstams,
_ci_ _[⋆]_ _,j_ _[⋆]_ . One way to find such a basis is by considering a minimal subregion of the mesh that
includes all the planar variables, once and only once. All such subregions are in one-to-one
correspondence with a triangulation of the _n_ -gon, such that the basis we are interested in
is formed by the _Xi,j_ ’s of this triangulation and the _ci,j_ ’s inside this region. To obtain this
subregion we do the following: start by picking a triangulation, _T_, of the _n_ -gon which is
determining the set of _n_ _−_ 3 chords, _Xi,j_ entering in the basis, with ( _i, j_ ) _∈T_ . Now consider
the “rotated triangulation”, formed by chords _Xi−_ 1 _,j−_ 1 with ( _i, j_ ) _∈T_ . Then consider the
region of the mesh that does **not** contain the meshes _ci−_ 1 _,j−_ 1 with ( _ij_ ) _∈T_ . Since the mesh
is infinite this will still be an infinite set of connected or disconnected regions, from which
we further extract a finite subset that contains all the planar Mandelstams, once and only
once - this is the desired subregion. The respective kinematic basis we are interested in is
constructed from the non-planar _ci,j_ ’s inside the subregion together with _n−_ 3 _Xi,j_ ’s in the
starting triangulation, _T_ .
In figure 3 we present the regions of the mesh corresponding to the three different types


6


**Figure** **3** : Triangulations and corresponding mesh subregions for 6-point kinematics.


of triangulation of the 6-point problem. All remaining triangulations correspond to cyclic
shifts of the ones presented, and these cyclic shifts only translate the region in the mesh
vertically, without altering its shape.
We denote the triangulations like the one on the left of figure 3 by **ray-like** triangulations. The kinematic basis associated with this region is _{X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, X_ 1 _,_ 5 _, c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, c_ 1 _,_ 5 _, c_ 2 _,_ 4 _,_
_c_ 2 _,_ 5 _, c_ 3 _,_ 5 _}_ . Such triangulations always lead to simple connected triangular regions in the
mesh. As we will see, this choice of basis makes most of the interesting features manifest


7


and therefore will be the preferred choice of kinematic basis henceforth.
Now that we have properly defined and organized the kinematical data that the amplitude depends on, let us proceed to study the associahedron and understand how it is
defined in kinematic space.


**2.2** **The** **ABHY** **associahedron**


As defined in [2], the ABHY associahedron associated with an _n_ -point amplitude is an
( _n −_ 3)–dimensional polytope. Its embedding in kinematic space goes as follows:


1. Define the region in kinematic space for which all the planar variables are **positive**  ∆+ = _{Xi,j_ _>_ 0 _}_, for all _i < j_ _∈{_ 1 _, . . ., n}_ .


2. Pick a subregion of the mesh determining a basis of _n −_ 3 planar variables, _X_ [˜] _i,j_, and
( _n −_ 2)( _n −_ 3) _/_ 2 non-planar, _c_ ˜ _i,j_, and solve for all the _Xi,j_ ’s in terms of this basis.


3. Impose that all _c_ ˜ _i,j_ _>_ 0, so that, in this new basis, ∆+ defines a set of _n_ ( _n −_ 3) _/_ 2
inequalities in an ( _n −_ 3)–dimensional space spanned by the _X_ [˜] _i,j_ . The convex-hull of
these inequalities is the ABHY associahedron.


From the previous procedure, we see that there are different ways of embedding this
polytope in kinematic space, each of them corresponding to a different choice of basis. These
different choices give rise to different realizations of the polytope, however, any statement
about the amplitude should be realization-independent.
Let us now see what the polytope looks like for a few simple examples.


**2.2.1** **4-point**


At 4-point we only have two different planar variables, _X_ 1 _,_ 3 and _X_ 2 _,_ 4, corresponding, respectively, to the Madelstams _s_ and _t_ . These are related to the non-planar variable, _c_ 1 _,_ 3 = _−u_,
in the following way:


_X_ 1 _,_ 3 + _X_ 2 _,_ 4 = _c_ 1 _,_ 3 _._ (2.5)


So picking the basis _{X_ 1 _,_ 3 _, c_ 1 _,_ 3 _}_, the ABHY associahedron is:


_{X_ 1 _,_ 3 _>_ 0 _∧_ _X_ 2 _,_ 4 _>_ 0 _⇔_ _X_ 1 _,_ 3 _< c_ 1 _,_ 3 _} ⇔_ 0 _< X_ 1 _,_ 3 _< c_ 1 _,_ 3 _,_ (2.6)


which is simply a line segment - a one-dimensional simplex. This is still a very small
example, so to understand how it works in a less trivial case it is worth going to 5 points.


**2.2.2** **5-point**


At 5-point, there are five different planar variables. However, there is only one possible
type of triangulation - the ray-like triangulation. Let us pick the basis corresponding
to the analogous of the 6-point ray-like triangulation discussed in the previous section,


8


**Figure** **4** : 5-point ABHY associahedron and respective Minkowski summands.



_i.e._ _{X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, c_ 2 _,_ 4 _}_ . Then the associahedron is defined in ( _X_ 1 _,_ 3 _, X_ 1 _,_ 4) space as
follows:

 _X_ 1 _,_ 3 _>_ 0



 _X_ 1 _,_ 4 _>_ 0





_X_ 1 _,_ 3 _>_ 0


_X_ 1 _,_ 4 _>_ 0



_X_ 2 _,_ 4 _>_ 0 _⇔_ _c_ 1 _,_ 3 _−_ _X_ 1 _,_ 3 + _X_ 1 _,_ 4 _>_ 0



_,_ (2.7)














_X_ 2 _,_ 5 _>_ 0 _⇔_ _c_ 1 _,_ 3 + _c_ 1 _,_ 4 _−_ _X_ 1 _,_ 3 _>_ 0

_X_ 3 _,_ 5 _>_ 0 _⇔_ _c_ 1 _,_ 4 + _c_ 2 _,_ 4 _−_ _X_ 1 _,_ 4 _>_ 0



which is exactly given by the pentagon presented in figure 4 (left). In section 1 we mentioned
that the ABHY associahedron is given by the Minkowski sum of simplices, which is fulcral
for the understanding of the zeros of the amplitude. At 4-point, the polytope is the onedimensional simplex, however, at 5-point this decomposition is not so obvious. Let us now
understand the decomposition of the polytope into its Minkowski summands.


**2.3** **The** **Minkowski** **summands** **and** **the** **mesh**


It turns out that each Minkowski summand is naturally associated with a mesh, _ci,j_ . Let
us start by analyzing the 5-point example. The set of inequalities in (2.7) carves out a
pentagon in ( _X_ 1 _,_ 3 _, X_ 1 _,_ 4) space, in which each edge corresponds to an inequality _Xi,j_ _>_ 0,
and thus is uniquely associated to that planar Mandelstam (see figure 4, left). In addition,
we see that the location of the edges of the pentagon is set by the values of the non-planar
variables _{c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, c_ 2 _,_ 4 _}_ . Therefore we can study what happens when we set some of these
non-planar variables to zero (see figure 4):


  - _c_ 1 _,_ 3 = _c_ 1 _,_ 4 = 0: The pentagon collapses to a horizontal line segment, _i.e._ a onedimensional simplex. This is then the Minkowski summand corresponding to mesh
_c_ 2 _,_ 4.


9


  - _c_ 1 _,_ 3 = _c_ 2 _,_ 4 = 0: The pentagon collapses to triangle, _i.e._ a two-dimensional simplex.
This is then the Minkowski summand corresponding to mesh _c_ 1 _,_ 4.


  - _c_ 1 _,_ 4 = _c_ 2 _,_ 4 = 0: The pentagon collapses to a horizontal line segment, again a onedimensional simplex. This is then the Minkowski summand corresponding to mesh
_c_ 1 _,_ 3.


So Minkowski summing these three simplices associated with the three different nonplanar variables, builds back the full pentagon. The fact that each Minkowski summand is
associated with a non-planar variable, we can keep track of Minkowski summands using the
mesh, just like it is shown in figure 4 (right), where we present only the subregion of the mesh
corresponding to the basis choice being used. We see that the lower-dimensional dimensional
simplices are on the meshes on the left while the top-dimensional one is associated with
the right-most corner. This pattern will persist at _n_ -point as long as we are dealing with
a basis associated with a ray-light triangulation: the meshes on the left-boundary will
correspond to one-dimensional simplices and, as we move towards the right, the dimension
of the simplices increases until it becomes top-dimensional in the right-most corner.
This is a good point to highlight that, had we chosen a different basis, the pentagon
would look different: it would be embedded in a different space, ( _X_ [˜] _i_ 1 _,j_ 1 _,_ _X_ [˜] _i_ 2 _,j_ 2), and the
non-planar variables involved would be different. In particular, at higher points, different
types of basis triangulation lead to different Minkowski summands.


**3** **Zeros** **and** **Factorizations** **of** **Tr** ( _ϕ_ [3] ) **Tree** **Amplitudes**


**3.1** **Zeros** **and** **factorizations** **–** **two** **simple** **examples**


Now that we have understood how the ABHY associahedron is defined in terms of its
Minkowski summands, let us proceed to the study of the zeros of the amplitude. To do this
we will start by studying in detail two simple examples: the 5-point and 6-point amplitudes.


**3.1.1** **5-point** **amplitude**


At 5-point, the amplitude is given by the sum of five different Feynman diagrams, corresponding to the five possible triangulations of the pentagon:


1 1 1 1 1
_A_ 5 = + + + + _._ (3.1)
_X_ 1 _,_ 3 _X_ 1 _,_ 4 _X_ 2 _,_ 4 _X_ 2 _,_ 5 _X_ 1 _,_ 3 _X_ 3 _,_ 5 _X_ 1 _,_ 4 _X_ 2 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 5


So to determine the kinematic locus where the amplitude vanishes, we can reduce (3.1)
to a common denominator and ask for the numerator to vanish. By doing this we get a
cubic equation that obscures any possible simple zeros of the amplitude.
However, we can recast the question about the zeros locus of the amplitude in polytopal
language. As it is explained in [2], the amplitude is the canonical form of the ABHY
associahedron, and therefore if we are able to make the polytope collapse one in dimension,
the amplitude will vanish.
Looking back at the 5-point associahedron presented in figure 4, we see that by setting
_c_ 1 _,_ 3 = _c_ 1 _,_ 4 = 0 or _c_ 1 _,_ 4 = _c_ 2 _,_ 4 = 0, the pentagon collapses into a line segment, which then


10


**Figure** **5** : 5-point factorization near zeros.


means that the amplitude vanishes in this limit! Note that the same is no longer true for
the case _c_ 1 _,_ 3 = _c_ 2 _,_ 4 = 0, since in this limit we still get a top-dimensional object, and thus
the amplitude does not vanish.
Now by the cyclic invariance of the 5-point amplitude, any cyclic images of these conditions also make the amplitude vanish. Therefore, we get the simple family of zeros: pick an
_i ∈{_ 1 _, . . .,_ 5 _}_, the amplitude vanishes in the locus _ci,j_ = 0, for all _j_ (non-adjacent to _i_ ). Even
though the realization of the associahedron associated to the basis _{X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, c_ 2 _,_ 4 _}_
does **not** make manifest all these zeros, for each zero we can always find a realization in
which it is manifest, as we will show in section 3.2.
Even though this example is still relatively simple it illustrates how the Minkowski sum
picture of the associahedron justifies the presence of this simple class of zeros: Knowing
that the non-planar variables are associated with individual summands that build up the
full polytope then, by turning off enough of them, we can make the polytope collapse in
dimension, and thus make the amplitude vanish.
Let us now focus on the zero _c_ 1 _,_ 3 = _c_ 1 _,_ 4 = 0, and understand what happens in the
penultimate step before the polytope collapses, _i.e._ when we **only** set _c_ 1 _,_ 3 = 0, or _c_ 1 _,_ 4 = 0.
In the latter case, _c_ 1 _,_ 4 = 0, the two remaining Minkowski summands are two intervals, and
so the polytope reduces to a square/rectangle (see figure 5, bottom). In particular, starting
with the full pentagon, we can see that by setting _c_ 1 _,_ 4 = 0, we lose the edge associated with
_X_ 2 _,_ 4. One way to explain this fact is that since:


_X_ 1 _,_ 4 + _X_ 2 _,_ 5 _−_ _X_ 2 _,_ 4 = _c_ 1 _,_ 4 _−−−−→c_ 1 _,_ 4=0 _X_ 2 _,_ 4 = _X_ 1 _,_ 4 + _X_ 2 _,_ 5 _._ (3.2)


So the condition _X_ 2 _,_ 4 _>_ 0, becomes redundant, since it is automatically satisfied for
_X_ 1 _,_ 4 _>_ 0 and _X_ 2 _,_ 5 _>_ 0, and thus the corresponding facet disappears. Therefore, in this


11


limit, the amplitude only depends on _{X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, X_ 2 _,_ 5 _, X_ 3 _,_ 5 _}_ . In addition, from section
2.2.1, we know that the 4-point ABHY associahedron is simply a line segment, so the fact
that the geometry reduces to a product of two line segments hints that in this limit the
amplitude turns into a product of two 4-point amplitudes. Indeed, by starting with the
5-point amplitude and imposing _c_ 1 _,_ 4 = 0, we obtain:



_A_ 5( _X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, X_ 2 _,_ 4 _, X_ 2 _,_ 5 _, X_ 3 _,_ 5) _−−−−→c_ 1 _,_ 4=0 - 1 + 1
_X_ 1 _,_ 3 _X_ 2 _,_ 5




- - 1 1
_×_ +
_X_ 1 _,_ 4 _X_ 3 _,_ 5




_,_ (3.3)



which is indeed the product of two 4-point amplitudes with some interesting kinematics,
_A_ 4( _X_ 1 _,_ 3 _, X_ 2 _,_ 5) and _A_ 4( _X_ 1 _,_ 4 _, X_ 3 _,_ 5). Let us now try to understand how we can read off this
behavior from the kinematic mesh. We are currently exploiting the behavior near the zero
associated with setting _c_ 1 _,_ 3 = _c_ 1 _,_ 4 = 0, which corresponds to a 45 _[◦]_ titled rectangle in the
bottom of the triangular mesh. The remaining part of the mesh, is exactly that of a 4-point
problem. By setting only _c_ 1 _,_ 4 to zero, one of the 4-point factors we get exactly corresponds
to this 4-point amplitude, with the kinematics entering the bottom diagonal depending on
which _ci,j_ we don’t set to zero. Before understanding the kinematic dependence, let us look
at the other 4-point factor. This term is associated with the _X_ ’s at the bottom and the
top of the causal diamond associated with the zero. Using the _c_ -equation for the full causal
diamond between _X_ 1 _,_ 3 and _X_ 2 _,_ 5, we have that _c_ 1 _,_ 3 = _X_ 1 _,_ 3 + _X_ 2 _,_ 5, and so we can rewrite
(3.3) as:



_c_ 1 _,_ 4=0 _c_ 1 _,_ 3                     - 1 1
_A_ 5( _X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, X_ 2 _,_ 4 _, X_ 2 _,_ 5 _, X_ 3 _,_ 5) _−−−−→_ _×_ +
_X_ 1 _,_ 3 _X_ 2 _,_ 5 _X_ 1 _,_ 4 _X_ 3 _,_ 5




_,_ (3.4)



so this factor is there to make manifest that the amplitude vanishes if we further set _c_ 1 _,_ 3 = 0.
As we will see, for a generic _n_ -point amplitude factorization, we always have such a factor
that exactly ties to the zero we are exploiting.
Let us now understand the kinematic dependence of the lower 4-point amplitude. Say
that, instead, we had set _c_ 1 _,_ 3 = 0. In this limit, the pentagon reduces to a trapezoid (see
figure 5, top), as we lose the edge corresponding to _X_ 1 _,_ 4. Similarly to the previous case, in
this limit, the amplitude factorizes into a product of two 4-point amplitudes as follows:



_A_ 5( _X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, X_ 2 _,_ 4 _, X_ 2 _,_ 5 _, X_ 3 _,_ 5) _−−−−→c_ 1 _,_ 3=0 - 1 + 1
_X_ 1 _,_ 3 _X_ 2 _,_ 5




- - 1 1
_×_ +
_X_ 2 _,_ 4 _X_ 3 _,_ 5







_c_ 1 _,_ 4   - 1 1
= _×_ +
_X_ 1 _,_ 3 _X_ 2 _,_ 5 _X_ 2 _,_ 4 _X_ 3 _,_ 5



(3.5)

_,_



so the first factor remains the same, since we are still probing the same zero, while the
second factor is now _A_ 4( _X_ 2 _,_ 4 _, X_ 3 _,_ 5). So the lower point amplitude no longer depends on
_X_ 1 _,_ 4, as this edge of the polytope is now lost, and instead depends on _X_ 2 _,_ 4 which survives
in this limit.
In summary, we understand that by turning on different _ci,j_ inside the zero causal diamond the factorization pattern does **not** change, however, the kinematic variables entering


12


the lower point amplitudes **do** change. This is because by turning on different _ci,j_ the
facets of the polytope that survive in the limit are different, or, in other words, the set
of inequalities _Xi,j_ _>_ 0 that become redundant depends on the _ci,j_ that we turn on. We
will explain the general pattern in which the kinematics are inherited in the lower point
amplitudes in section 3.2.
The discussion in this section is summarized pictorially in figure 5.


**3.1.2** **6-point** **amplitude**


The six-particle amplitude is a sum of 14 terms, corresponding to the Feynman diagrams
in three cyclic classes:


   - 1 1   - 1 1
_A_ 6 = + + cyclic + + _._ (3.6)
_X_ 1 _,_ 3 _X_ 1 _,_ 4 _X_ 1 _,_ 5 _X_ 1 _,_ 3 _X_ 3 _,_ 6 _X_ 4 _,_ 6 _X_ 1 _,_ 3 _X_ 3 _,_ 5 _X_ 1 _,_ 5 _X_ 2 _,_ 4 _X_ 4 _,_ 6 _X_ 2 _,_ 6


Let us now see how the zeros and factorizations work, where we see the most generic
behavior seen for all _n_, with cyclically inequivalent classes for patterns of zeros.
We begin with the full ABHY associahedron, shown in the left panel of figure 6. For
some orientation, note that the facets lying on the co-ordinate planes _X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, X_ 1 _,_ 5 _→_ 0
are the pentagons ( _X_ 1 _,_ 3 _→_ 0 and _X_ 1 _,_ 5 _→_ 0) and the square ( _X_ 1 _,_ 4 _→_ 0) as expected from
the associated _A_ 5 _× A_ 3 and _A_ 4 _× A_ 4 factorizations. Note that we also have facets parallel
to these, on the opposite side of the polytope. For instance, the facet parallel to the _X_ 1 _,_ 3
plane corresponds to _X_ 2 _,_ 6 _→_ 0. This is obvious from the mesh picture since we have
_X_ 2 _,_ 6 = _C_ _−_ _X_ 1 _,_ 3 where _C_ = _c_ 1 _,_ 3 + _c_ 1 _,_ 4 + _c_ 1 _,_ 5; this is the top corner of the maximal causal
with _X_ 1 _,_ 3 on the bottom. In the same way the facet parallel to _X_ 1 _,_ 4 is _X_ 3 _,_ 6 and the one
parallel to _X_ 1 _,_ 5 is _X_ 4 _,_ 6. This is a general feature of the ABHY associahedron: there are
pairs of facets parallel to the coordinate planes that “look the same”, corresponding to the
poles associated with the bottom and top boundaries of the mesh picture. Let us begin
with the analog of what we saw already at 5 points, the “skinny rectangle” zero. If we set
_c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, c_ 1 _,_ 5 _→_ 0, then the three-dimensional associahedron collapses in the _X_ 1 _,_ 3 direction
down to a two-dimensional pentagon. We can see this visually in figure 6 (a more detailed
figure 17 appears at the end of the paper), where we have represented the penultimate
step in shutting off _c_ ’s, where _c_ 1 _,_ 3 _, c_ 1 _,_ 5 _→_ 0 but _c_ 1 _,_ 4 is still turned on. At this point, we
have a “sandwich”, with the _X_ 1 _,_ 3 facet and its parallel cousin _X_ 2 _,_ 6 facet, separated by an
interval. When we further shut off _c_ 1 _,_ 4 the interval shrinks to zero and we are left with the
pentagon, showing that the amplitude vanishes in this limit. We can also look at shutting
off _c_ 1 _,_ 4 _, c_ 1 _,_ 5 _, c_ 2 _,_ 4 _, c_ 2 _,_ 5 where the associahedron collapses to a square. This is also shown
in figure 6, where we have again shown the penultimate step where we have turned _c_ 2 _,_ 4
back on. We again have a “sandwich” with _X_ 1 _,_ 4 and opposite _X_ 3 _,_ 6 facets, separated by
an interval. The interval shrinks to zero when _c_ 2 _,_ 4 _→_ 0; the associahedron collapses to a
square and the amplitude vanishes. Just as at five points, in the penultimate step before


13


**Figure** **6** : 6-point factorization near zeros.


the associahedron collapses, the amplitude factorizes, as we can see explicitly:




_,_



_A_ 6 _−−−−−−−−→c_ 1 _,_ 3=0 _,c_ 1 _,_ 5=0 - 1 + 1
_X_ 1 _,_ 3 _X_ 2 _,_ 6

_A_ 6 _−−−−−−−−−−−−−→c_ 1 _,_ 4=0 _,c_ 1 _,_ 5=0 _,c_ 2 _,_ 5=0 - 1 + 1
_X_ 1 _,_ 4 _X_ 3 _,_ 6




- - 1 1 1 1 1
_×_ + + + +
_X_ 2 _,_ 4 _X_ 1 _,_ 5 _X_ 1 _,_ 5 _X_ 3 _,_ 5 _X_ 3 _,_ 5 _X_ 3 _,_ 6 _X_ 3 _,_ 6 _X_ 4 _,_ 6 _X_ 4 _,_ 6 _X_ 2 _,_ 4




- - 1 1
_×_ +
_X_ 1 _,_ 3 _X_ 2 _,_ 6




- - 1 1
_×_ +
_X_ 1 _,_ 5 _X_ 4 _,_ 6




_._ (3.7)



In the top line, we see the factor (1 _/X_ 1 _,_ 3 +1 _/X_ 2 _,_ 6), which vanishes when we further set
_c_ 1 _,_ 4 _→_ 0, since _X_ 1 _,_ 3 + _X_ 2 _,_ 6 = _c_ 1 _,_ 3 + _c_ 1 _,_ 4 + _c_ 1 _,_ 5 _→_ 0 when we set _c_ 1 _,_ 4 _→_ 0. It multiplies a fiveparticle amplitude, but with some interestingly redefined kinematic variables. If we look
at the picture of the associahedron in this limit, the two bounding facets of the “sandwich”
are precisely _X_ 1 _,_ 3 and _X_ 2 _,_ 6, while the facets keeping _X_ 1 _,_ 3 _, X_ 2 _,_ 6 can be read off going around
the pentagons as _X_ 2 _,_ 4 _, X_ 1 _,_ 5 _, X_ 3 _,_ 5 _, X_ 3 _,_ 6 _, X_ 4 _,_ 6, which precisely defines the kinematics for an
effective five-particle amplitude given in the second factor. The same story holds for the
“big square” zero/factorization. The first factor (1 _/X_ 1 _,_ 4 + 1 _/X_ 3 _,_ 6) vanishes when _c_ 2 _,_ 4 _→_ 0
since _X_ 1 _,_ 3 + _X_ 2 _,_ 6 = _c_ 1 _,_ 4 + _c_ 1 _,_ 5 + _c_ 2 _,_ 4 + _c_ 2 _,_ 5 _→_ 0. At finite _c_ 2 _,_ 4 the facets in between the _X_ 1 _,_ 4
and _X_ 3 _,_ 6 facets are _X_ 1 _,_ 3 _, X_ 1 _,_ 5 _, X_ 2 _,_ 6 _, X_ 4 _,_ 6. This is exactly the direct product of two effective
4-point problems with variables ( _X_ 1 _,_ 3 _, X_ 2 _,_ 6) and ( _X_ 4 _,_ 6 _, X_ 1 _,_ 5), which appear in the 4-point
amplitude factors.
In figure 7, we summarize the patterns of zeros found for the 5-point and 6-point
amplitudes using the kinematic mesh. We can see that all the zeros patterns are causal
diamonds that extend to the boundaries of the mesh picture.


**3.2** **Zeros** **and** **factorizations** **–** **general** **statement**


We now present the general statement about the zeros and factorization of _n_ -point tree-level
Tr( _ϕ_ [3] ) amplitudes. As we will see the motivation and proof of these statements follow easily


14


**Figure** **8** : Zeros (left) and Factorizations with associated kinematic shifts (right).


from simple properties of the associahedron. In later sections, we will give a different proof,
beginning from the stringy integral representation of these amplitudes, that will generalize
the statements beyond the field theory limit to full string amplitudes.


15


**Zeros** Consider an _n_ -point tree-level amplitude in Tr( _ϕ_ [3] ) theory. Draw the corresponding
_n_ -point kinematic mesh. Pick a point in the mesh, _i.e._ a planar variable _XB_, and consider
the causal diamond anchored in this variable: follow the two light rays starting at _XB_, let
them bounce in the boundaries of the mesh, and meet again in some other point, _XT_ . This
encloses a region - a causal diamond. Setting all the _ci,j_ inside this causal diamond to zero
will make the amplitude vanish (see figure 8).


**Factorizations** Let us consider turning back on one of the _c_ ’s inside the zero causal
diamond, _c⋆_ = 0. Then the amplitude factorizes into the product of lower point amplitudes
in the following way (see figure 8):




    - 1
_An_ ( _c⋆_ = 0) = + [1]
_X_ B _X_ T




_× A_ [down] _× A_ [up] _._ (3.8)



Now the kinematic dependence of _A_ [down] and _A_ [up] can be read off from the kinematic
mesh, and is summarized in figure 8. The question is what are the kinematic variables that
enter in the upper/lower part of the down/up amplitudes. These are precisely those of the
facets of the associahedron that are not lost in this kinematic limit.
Let us start by looking at _A_ [down] . We see that for any _X_ lying beneath the _c⋆_, we
can build a rectangle with _X_ on the left vertex, _Xi,i_ +1 = 0 in the boundary on the right
vertex, _XB_ on the bottom vertex, and _X_ [˜] on the top vertex, where _X_ [˜] lives on the upper
boundary of the mesh. In this limit all the _ci,j_ inside this rectangle are **zero**, and so using
the _c_ -equation we can write:
_X_ = _XB_ + _X._ [˜] (3.9)


Just like we saw in the 5-point example, this then means that the inequality _X_ _>_
0 becomes redundant, and so the facet of the polytope associated with _X_ disappears.
Consequently, the variable that survives and enters the lower point amplitude is _X_ [˜] . Exactly
in the same way all the _X_ ’s above _c⋆_ for _A_ [up], disappear and instead the _X_ [˜] from the bottom
boundary of the mesh are the ones that enter _A_ [up] .
Finally, for all the _X_ ’s lying above _c⋆_ in _A_ [down], if we try to build the same rectangle,
now it will include _c⋆_ = 0, and the argument does not hold anymore. However, we can now
build a rectangle connecting _X_ to _X_ [˜], _X_ T and a _Xi,i_ +1 in the left boundary of the mesh.
Inside this rectangle all the _ci,j_ = 0, and so we get:


_X_ ˜ = _X_ T + _X,_ (3.10)


which tells us that for this region the facets associated with _X_ [˜] disappear and the ones with
_X_ survive. Exactly the same argument tells us that the _X_ ’s beneath _c⋆_ for _A_ [up] survive in
this limit and thus appear in _A_ [up] .
By now it should be clear that both the zeros and the factorization are properties of
the amplitudes of Tr( _ϕ_ [3] ) theory that are fundamentally hidden in the Feynman diagram
formulation of these objects. It is instead the underlying geometry that gives us access to
them and even suggests looking for them in the first place.


16


As we will see shortly, these properties extend immediately to full string amplitudes.
Before getting to that, we will first go through an even more magical fact - that these
generalize to the Non-linear Sigma Model and Yang-Mills theory. This generalization is
surprising because there is no known geometrical formulation for these theories. Ultimately,
the reason for the emergence of these properties will be manifest when we see that these
theories are secretly simple deformations of each other. These deformations are defined at
the level of stringy formulations of the amplitudes that we go over in section 7.


**4** **The** **Non-linear** **Sigma** **Model**


We were motivated to look for and predict zeros of the Tr( _ϕ_ [3] ) amplitude from the Minkowski
sum picture of the associahedron. But in the end, the zeros are associated with a simple
locus in the space of non-planar Mandelstam invariants. As such it is natural to wonder whether other colored theories, which have the same notion of color-ordering and
planarity/non-planarity, may also have such zeros. Clearly random theories will not have
these zeros, for instance, the amplitude for Tr( _ϕ_ [4] ) is simply a constant at four points and
does not have our zero. But this is not an especially “nice” theory. Perhaps the most natural theory to examine is the Non-linear Sigma Model for pions, which already does have
famous Adler zeros associated with soft limits. Of course on the surface the Tr( _ϕ_ [3] ) theory
and the NLSM could not appear more different: Tr( _ϕ_ [3] ) theory has no derivatives in its
interactions, and has non-vanishing amplitudes for all multiplicity; by contrast, pions are
derivatively coupled and only have non-vanishing amplitudes for an even number of particles! Nonetheless, in this section we will see experimentally that the NLSM amplitudes
have zeros in precisely the same locus of kinematics we uncovered for the Tr( _ϕ_ [3] ) theory.
The scattering of massless pions can be described by the U( _N_ ) Non-Linear Sigma
Model, and we record the Lagrangian in Cayley parametrization ( _c.f._ [23]):


1           -           _L_ NLSM = _∂µ_ U _[†]_ _∂_ _[µ]_ U _,_ with U = (I + _λ_ Φ)(I _−_ _λ_ Φ) _[−]_ [1] _,_ (4.1)

[Tr]
8 _λ_ [2]


where Φ = _ϕI_ _T_ _[I]_, with _T_ _[I]_ the generators of _U_ ( _N_ ) flavor group and _λ_ is the coupling constant. It is straightforward to derive color-ordered Feynman rules, _e.g._ for Tr(1 _,_ 2 _, · · ·_ _, n_ ),
and the vertex with two derivatives for any even multiplicity 2 _m_ is given by



2 _m_


_pa · pa_ +2 _r_ +1 _._ (4.2)

_a_ =1



_V_ 2 _m_ = _−_ _[λ]_ [2] _[m][−]_ [2]

2



_m−_ 1



_r_ =0



NLSM tree amplitudes have been studied in _e.g._ [13, 24]. It is well known that odd-point
NLSM amplitudes vanish and even-point amplitudes have the Adler zero [25], _i.e._ _A_ [NLSM] 2 _n_ _∼_
_O_ ( _τ_ ) when any external momentum becomes soft, _p_ _[µ]_ _i_ [=] _[τ]_ [ ˆ] _[p][µ]_ _i_ [with] _[τ]_ _[→]_ [0][.] [Hereafter,] [we]
will absorb the coupling constant _λ_ by defining: _A_ [NLSM] 2 _n_ _≡_ _λ_ [2] _[−][n]_ _A_ [NLSM] 2 _n_, therefore, _e.g._ the
4-point amplitude reads _A_ [NLSM] 4 = _X_ 1 _,_ 3 + _X_ 2 _,_ 4. And the 6-point result is

_A_ [NLSM] 6 = [(] _[X]_ [1] _[,]_ [3][ +] _[ X]_ [2] _[,]_ _X_ [4][)(] 1 _,_ _[X]_ 4 [1] _[,]_ [5][ +] _[ X]_ [4] _[,]_ [6][)] _−_ _X_ 1 _,_ 3 _−_ _X_ 2 _,_ 4 + (cyclic _, i →_ _i_ + 2) _._ (4.3)


17


**4.1** **Zeros** **and** **the** **soft** **limit**


Surprisingly, all the zeros that we described for Tr( _ϕ_ [3] ) theory are also zeros of NLSM
tree-level amplitudes. So starting with a mesh describing 2 _n_ -kinematics, by picking any
causal diamond like the one in figure 8 and setting all the _ci,j_ ’s inside it to zero, the NLSM
amplitude vanishes.
As explained previously, depending on the _X_ B we pick to build the zero causal diamond,
the shape of the diamond, and in particular, the codimension of the zero changes. The
**smallest** codimension zeros are the **skinny** **rectangle** ones, where we pick an index _i_, and
set all _ci,j_ = 0, for all the _j_ not adjacent to _i_ . It is well known that pion amplitudes have
the Adler zero, _i.e._ vanish when one particle is soft. Note however that the zero we are
presenting is **not** **a** **soft** **limit**, instead it is stronger, in the sense that the fact that the
amplitude vanishes in this zero implies that it has the Adler zero.
Let us look concretely at the 4-point amplitude. In this case, the zero would be _c_ 1 _,_ 3 = 0,
and so _p_ 1 _· p_ 3 = 0, which, however does **not** require any particle to be soft. Indeed we have
that the 4-point pion amplitude is:


_A_ [NLSM] 4 = _X_ 1 _,_ 3 + _X_ 2 _,_ 4 = _c_ 1 _,_ 3 _−−−−→Ac_ 1 _,_ 3=0 [NLSM] 4 = 0 _,_ (4.4)


and so vanishes as expected. Of course, for this zero to imply the Adler zero, it is crucial
that the amplitude does not have poles when _p_ _[µ]_ _i_ _[→]_ [0][,] [which] [is] [true] [for] [the] [NLSM] [since]
we always have even-point interactions. The same is not true for Tr( _ϕ_ [3] ) theory, and this is
why the zero in this context does not imply the vanishing in the soft limit.
At last, it is worth highlighting that, despite the fact that the skinny rectangle zero is
somehow related to the Adler zero, the same is not true for the other codimension zeros that
we predict from the mesh picture. Just like in the Tr( _ϕ_ [3] ) case, there is no clear physical
explanation for the presence of these general families of zeros that are there for colored
scalars and pions.


**4.2** **Factorizations**


Let us now understand how the statement about factorization near zeros generalizes to
pions. For pion scattering, we always start with a 2 _n_ kinematical mesh and, for a particular
codimension zero, _i.e._ a particular zero causal diamond, we can ask what happens if we turn
on one of the _c_ ’s inside the zero causal diamond, _c⋆_ = 0. It turns out, that if the lower
point amplitudes, _A_ [down] and _A_ [up], are both **even** -point amplitudes then the factorization
holds exactly in the same way we described for Tr( _ϕ_ [3] ):




      - 1
_A_ [NLSM] 2 _n_ ( _c⋆_ = 0) = _X_ B + _X_ [1] T




_× A_ [down,NLSM] _× A_ [up,NLSM] _,_ (4.5)



where the kinematic dependence of _A_ [down,NLSM] and _A_ [up,NLSM] are determined exactly in
the way we explained for Tr( _ϕ_ [3] ) (according to figure 8).
However, when the factorization pattern produces **odd** -point amplitudes we have something new. As we know there are no odd-point amplitudes for pions, so instead the ampli

18


**Figure** **9** : Factorization into mixed theory amplitudes, NLSM+ _ϕ_ [3] .


tudes that enter in (4.5) are amplitudes in the mixed theory of pions and scalars [26]:


_A_ [NLSM] 2 _n_ ( _c⋆_ = 0) = ( _X_ B + _X_ T) _× A_ [down,NLSM+] _[ϕ]_ [3] _× A_ [up,NLSM+] _[ϕ]_ [3] _._ (4.6)


In addition, we see that the prefactor involving _X_ B and _X_ T also changed: instead of
the 4-point scalar amplitude, we have the 4-point NLSM amplitude. This change is due to
the fact that mixed amplitudes have different units than NLSM amplitudes. But note that
the prefactor is still such that makes manifest that the amplitude vanishes if we further set
_c⋆_ = 0.
Now the kinematic dependence of _A_ [down,NLSM+] _[ϕ]_ [3] and _A_ [up,NLSM+] _[ϕ]_ [3] are once more determined by the kinematic shifts described for Tr( _ϕ_ [3] ), however, we still need to specify
the configuration of _π_ ’s and _ϕ_ ’s entering these amplitudes. It turns out that this depends
on the choice of _c⋆_ that is set to non-zero, but it will always be the case that for a 2 _n−_ 1
amplitude, we will always have 3 _ϕ_ ’s and 2 _n−_ 4 _π_ ’s.
To describe the rule let us start by considering a 6-point pion amplitude and consider
the factorization that leads to a 5-point amplitude, corresponding to turning on a _ci,j_
inside a skinny rectangle (see figure 9, left). The skinny rectangle can either be on the
top of the mesh or at the bottom. Let us start by looking at the case in which it is on
the top, like the one highlighted in blue in figure 9. Then by turning on the top _c_, we get
the amplitude in which the three _ϕ_ ’s are the last three particles, at five points this then
means we have two _π_ ’s and three _ϕ_ ’s. For a general 2 _n −_ 1 mixed amplitude, we would
have 2 _n −_ 4 _π_ ’s followed by 3 _ϕ_ ’s. Now as we go down the skinny rectangle turning on
different _ci,j_, the pattern is that the first _ϕ_ next to the _π_ ’s starts moving past them, once
at a time. Since there are 2 _n −_ 3 meshes in the skinny rectangle, once we reach the point
to turn on the _ci,j_ corresponding to the right-most mesh, the _ϕ_ has now passed the full
string of _π_ ’s so that we have _A_ [NLSM+] _[ϕ]_ [3] ( _ϕ, π, π, ϕ, ϕ_ ), at 5-point case (figure 9, left), and
_A_ [NLSM+] _[ϕ]_ [3] ( _ϕ, π, . . ., π, ϕ, ϕ_ ), for the general 2 _n −_ 1 mixed amplitude.
Let us now continue by looking at the bottom skinny rectangle. Starting from the


19


right-most mesh we have _A_ [NLSM+] _[ϕ]_ [3] ( _ϕ, π, . . ., π, ϕ, ϕ_ ), and going down is going to make the
_ϕ_ to the right of the string of _π_ ’s move through them, just like in the previous case. So
that when we reach the left-most bottom mesh, we get _A_ [NLSM+] _[ϕ]_ [3] ( _ϕ, ϕ, π, . . ., π, ϕ_ ).
The way this generalizes for the factorization involving a general codimension zero is
summarized in figure 9 (right). By picking some _c⋆_ = 0 inside a given causal diamond, the _ϕ_,
_π_ configuration in _A_ [down,NLSM+] 2 _n−_ 1 _[ϕ]_ [3] and _A_ [up,NLSM+] 2 _m−_ 1 _[ϕ]_ [3] is exactly the same as the ones we would
have obtained considering a factorization from a skinny rectangle in a 2 _n_, 2 _m_ problem,
respectively, where the _c⋆_ occupies the same relative position in these lower problems, as it
does in the bigger one (see figure 9, right).


**4.2.1** **Examples**


Let us now see this factorization in action for the case of the 6-point pion amplitude.
We start by looking at the factorization associated with the square causal diamond,
for which the lower point amplitudes are 4-point amplitudes, and thus should be NLSM
amplitudes. Consider the zero associated with setting _{c_ 1 _,_ 4 _, c_ 2 _,_ 4 _, c_ 1 _,_ 5 _, c_ 2 _,_ 5 _}_ to zero, and let
us look at the factorization we get by turning on _c_ 2 _,_ 4. From the kinematic shifts, we expect
_X_ 3 _,_ 5 and _X_ 2 _,_ 4 to be fixed, and so the bottom 4-point amplitude will be a function of ( _X_ 1 _,_ 3,
_X_ 2 _,_ 6, _c_ 1 _,_ 3), while the top 4-point will depend on ( _X_ 1 _,_ 5, _X_ 4 _,_ 6, _c_ 3 _,_ 5). In this kinematic limit,
the amplitude becomes:



_c_ 1 _,_ 3 _c_ 2 _,_ 4 _c_ 3 _,_ 5                 - 1 1
_A_ 6( _c_ 1 _,_ 4 = _c_ 1 _,_ 5 = _c_ 2 _,_ 5 = 0) = +
_X_ 1 _,_ 4( _X_ 1 _,_ 4 _−_ _c_ 2 _,_ 4) [=] _X_ 1 _,_ 4 _X_ 3 _,_ 6





_· c_ 1 _,_ 3 _· c_ 3 _,_ 5




 - 1 1
= +
_X_ 1 _,_ 4 _X_ 3 _,_ 6





_·_ ( _X_ 1 _,_ 3 + _X_ 2 _,_ 6)

  - ��  
_A_ [down,NLSM] 4




_·_ ( _X_ 1 _,_ 5 + _X_ 4 _,_ 6)

 - �� 


(4.7)
_,_



_A_ [up,NLSM] 4



which follows exactly the form predicted in (4.5).
Let us now consider the factorization into the 5-point mixed amplitude. The skinny
rectangle we will consider will be the usual one containing _{c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, c_ 1 _,_ 5 _}_ :


  - Turn on _c_ 1 _,_ 5:


According to the kinematic shifts, we should get a 5-point amplitude depending on
( _X_ 2 _,_ 4, _X_ 2 _,_ 5, _X_ 3 _,_ 5, _X_ 3 _,_ 6, _X_ 4 _,_ 6, _c_ 2 _,_ 4, _c_ 2 _,_ 5, _c_ 3 _,_ 5). In this limit, the amplitude becomes:


           - _c_ 3 _,_ 5            _A_ 6( _c_ 1 _,_ 3 = _c_ 1 _,_ 4 = 0) = _c_ 1 _,_ 5 _·_ + _[c]_ [2] _[,]_ [4] + 1
_X_ 3 _,_ 6 _X_ 2 _,_ 5




     - _X_ 3 _,_ 5 + _X_ 4 _,_ 6      = ( _X_ 1 _,_ 3 + _X_ 2 _,_ 6) _·_ + _[X]_ [2] _[,]_ [4][ +] _[ X]_ [3] _[,]_ [5] _−_ 1
_X_ 3 _,_ 6 _X_ 2 _,_ 5



(4.8)
_._




- �� 
_A_ [NLSM+] 5 _[ϕ]_ [3] ( _ϕ,π,π,ϕ,ϕ_ )




- Turn on _c_ 1 _,_ 4:



20


According to the kinematic shifts, we should get a 5-point amplitude depending on
( _X_ 2 _,_ 4, _X_ 1 _,_ 5, _X_ 3 _,_ 5, _X_ 3 _,_ 6, _X_ 4 _,_ 6, _c_ 2 _,_ 4, _c_ 2 _,_ 5, _c_ 3 _,_ 5). In this limit, the amplitude becomes:



_A_ 6( _c_ 1 _,_ 3 = _c_ 1 _,_ 5 = 0) = _c_ 1 _,_ 4 _·_ _[c]_ [3] _[,]_ [5]

_X_ 3 _,_ 6

           - _X_ 3 _,_ 5 + _X_ 4 _,_ 6            = ( _X_ 1 _,_ 3 + _X_ 2 _,_ 6) _·_ _−_ 1
_X_ 3 _,_ 6



_._ (4.9)




                          - ��                          
_A_ [NLSM+] 5 _[ϕ]_ [3] ( _ϕ,π,ϕ,π,ϕ_ )


- Turn on _c_ 1 _,_ 3:


According to the kinematic shifts, we should get a 5-point amplitude depending on
( _X_ 1 _,_ 4, _X_ 1 _,_ 5, _X_ 3 _,_ 5, _X_ 3 _,_ 6, _X_ 4 _,_ 6, _c_ 2 _,_ 4, _c_ 2 _,_ 5, _c_ 3 _,_ 5). In this limit, the amplitude becomes:




        - _c_ 3 _,_ 5
_A_ 6( _c_ 1 _,_ 4 = _c_ 1 _,_ 5 = 0) = _c_ 1 _,_ 3 _·_ + _[c]_ [3] _[,]_ [5][ +] _[ c]_ [2] _[,]_ [5]
_X_ 3 _,_ 6 _X_ 1 _,_ 4








     - _X_ 3 _,_ 5 + _X_ 4 _,_ 6      = ( _X_ 1 _,_ 3 + _X_ 2 _,_ 6) _·_ + _[X]_ [4] _[,]_ [6][ +] _[ X]_ [1] _[,]_ [5] _−_ 1
_X_ 3 _,_ 6 _X_ 1 _,_ 4



(4.10)
_._




- �� 
_A_ [NLSM+] 5 _[ϕ]_ [3] ( _ϕ,ϕ,π,π,ϕ_ )



**5** **Yang-Mills** **Theory**


Finally, let us look at the last and most important colored theory: pure Yang-Mills theory.
In this case, we are describing massless spin 1 particles and therefore the amplitudes have
a crucial new ingredient: the **polarizations** of the gluons, _ϵi_ . So we have that _A_ [YM] _≡_
_A_ [YM] ( _pi · pj, ϵi · pj, ϵi · ϵj_ ).
Due to this new feature, the statement about the zeros requires a generalization to
involve a statement about polarization vectors as well. The most natural extension is as
follows:


**Gluon** **Zeros** Consider an _n_ -point tree-level amplitude in YM theory. Draw the corresponding _n_ -point kinematic mesh. Draw a causal diamond just like the one described for
Tr( _ϕ_ [3] ). Setting all the _ci,j_ inside this causal diamond to zero as well as all _ϵi_ _· pj_, _ϵj_ _· pi_
and _ϵi_ _· ϵj_ will make the amplitude vanish. Note that setting _ϵi_ _· ϵj_ = 0 is not a gaugeinvariant statement, unless we also have _ϵi · pj_ = _ϵj_ _· pi_ = 0. Therefore the zero condition
is well-defined and physically meaningful.
For example, if we set not only _c_ 1 _,_ 3 = _−_ 2 _p_ 1 _·_ _p_ 3 = 0 but also _ϵ_ 1 _·_ _ϵ_ 3 = _ϵ_ 1 _·_ _p_ 3 = _ϵ_ 3 _·_ _p_ 1 = 0,
the 4-gluon amplitude vanishes. Similarly, we can have 4( _n−_ 3) zero conditions associated
with “skinny rectangle” and other causal diamonds such as the 16 conditions with ( _i, j_ ) =
(1 _,_ 4) _,_ (1 _,_ 5) _,_ (2 _,_ 4) _,_ (2 _,_ 5) which makes the 6-gluon amplitude vanishes.
Now the question about factorization is more subtle. In particular there is only one
inner product that we can turn back on that does not mess the gauge invariance of the
other conditions: setting _ci,j_ = 0 makes _ϵ · p_ = 0 meaningless, _ϵi · pj_ = 0 makes _ϵi · ϵj_ = 0


21


meaningless. So the only well-defined thing to do is set _ϵi ·_ _ϵj_ = 0. Still doing so it is unclear
the meaning of the factor multiplying _ϵi · ϵj_ obtained in this limit.
For this reason, at this stage, we do not have any generalization of the factorizations
found for the previous theories. Such a generalization will only appear once we find a
formulation of Yang-Mills theory that connects it to the other colored theories. Of course,
while the connection between Tr( _ϕ_ [3] ) and the NLSM is surprising, at least these are both
theories of scalars, so it is even more surprising to connect Tr( _ϕ_ [3] ) with Yang-Mills–for
instance where do the polarization vectors come from? As we will see in section 7, this new
description of the _n_ gluon amplitudes will actually begin with a theory of 2 _n_ colored scalars,
which will arise from a shift of the stringy Tr( _ϕ_ [3] ) amplitudes for 2 _n_ scalars. Factorizing on
poles where _n_ pairs of these scalars fuse to produce gluons then gives us general _n_ -gluon
amplitudes. This formulation will make the zeros and factorizations present in this theory
manifest.


**6** **Stringy** **Tr** ( _ϕ_ [3] )


In this section, we generalize the zeros and factorizations of Tr( _ϕ_ [3] ) tree amplitude to the
corresponding string amplitude: the so-called stringy integrals for ABHY associahedron [6],
which also represents a tree-level example of the so-called “binary geometry” [7]. These
string amplitudes are in fact _n_ -point generalizations [17] of the Veneziano amplitude [27],
known as dual resonance model in the early days of string theory (see [28] for a review), and
more recently they arise as a natural basis for _n_ -gluon tree amplitudes in type-I superstring
theory (see [29, 30]). The _n_ -point amplitude is given by an integral over the moduli-space
of real points _z_ 1 _, . . ., zn_ on the boundary of the disk:




        _In_ [Tr(] _[ϕ]_ [3][)] (1 _,_ 2 _, ..., n_ ) =

_D_ (1 _...n_ )



d _z_ 1 _. . ._ d _zn_ 1
vol SL(2 _,_ R) _z_ 1 _,_ 2 _z_ 2 _,_ 3 _. . . zn,_ 1

      - ��       PT(1 _,_ 2 _,···,n_ )




 _×_ _zi,j_ [2] _[α][′][p][i][·][p][j]_

_i<j_


  - ��   Koba-Nielsen factor



_,_ (6.1)



where the SL(2 _,_ R) redundancy allows one to fix three punctures and the integration domain
is the positive part of the real moduli space, _M_ [+] 0 _,n_ [,] [or] _[z]_ [1] _[<]_ _[z]_ [2] _[<]_ _[· · ·]_ _[<]_ _[z][n]_ [(with] [3] [of]
them fixed); here _zi,j_ := _zj_ _−_ _zi_ _>_ 0 for _i_ _<_ _j_, and the integrand is given by the ParkeTaylor factor, PT(1 _,_ 2 _, · · ·_ _, n_ ) times the universal Koba-Nielsen factor (we have omitted the
overall prefactor _α_ _[′][ n][−]_ [3] ). The low energy limit, where _α_ _[′]_ _Xi,j_ _≪_ 1, yields the Tr( _ϕ_ [3] ) tree
amplitudes, and low-energy, _α_ _[′]_ -expansion of these integrals have been extensively studied
in the literature (the so-called _Z_ -theory [31, 32]).
To translate this to stringy integrals for binary geometries, we introduce _u_ variables
(one for each chord ( _i, j_ )), which are SL(2,R) invariant cross-ratios defined as follows:


_ui,j_ = _[z][i][−]_ [1] _[,j][z][i,j][−]_ [1] _._ (6.2)

_zi,jzi−_ 1 _,j−_ 1


In terms of _u_ ’s, the Koba-Nielsen factor becomes [�] _i,j_ _[u]_ _i,j_ _[α][′][X][i,j]_ with planar variables _Xi,j_ =
( _pi_ + _pi_ +1 + _..._ + _pj−_ 1) [2] (with _Xi,i_ +1 = 0). Note that there are _n_ ( _n−_ 3) _/_ 2 _u_ variables, which


22


satisfy _u_ equations [2, 22] (see earlier works _e.g._ [17, 33]):


       _ui,j_ + _uk,l_ = 1 _,_ (6.3)


( _k,l_ ) cross ( _i,j_ )


such that for any _ui,j_ _→_ 0, all incompatible _uk,l_ _→_ 1 (the chord ( _k, l_ ) intersects with ( _i, j_ )),
hence the name “binary geometry". The ordering of _zi_ is equivalent to requiring all _u_ variables to be positive (which implies that 0 _< ui,j_ _<_ 1), thus we have the ( _n−_ 3)-dimensional
positive binary geometry, _Un_ [+] _[∼M]_ 0 [+] _,n_ [,] [which] [has] [the] [shape] [of] [a] [(curvy)] [associahedron] [[][7][].]
As shown in [2], the Parke-Taylor factor PT(1 _,_ 2 _, · · ·_ _, n_ ) with the measure is nothing but
the canonical form of this space, which we denote as Ω( _Un_ [+][)][,] [thus] [we] [have]




        _In_ [Tr(] _[ϕ]_ [3][)] (1 _,_ 2 _, ..., n_ ) =




[�]

_ui,j_ _[α][′][X][i,j]_ _._ (6.4)
_i<j_



Ω  - _Un_ [+]  - [�]
_Un_ [+]



To be more explicit, one can choose any _positive_ _parametrization_ of _Un_ [+][,] [and] [a] [conve-]
nient one inspired by first fix the SL(2 _,_ R) by choosing a gauge fixing _e.g._ _z_ 1 = 0 _, zn−_ 1 =
1 _, zn_ = _∞_ ) and change the remaining _z_ variables to the positive _y_ variables as


_y_ 1 _,_ 3 _· · · y_ 1 _,n−_ 1 _y_ 1 _,_ 4 _· · · y_ 1 _,n−_ 1
_z_ 2 = _,_ _z_ 3 _−z_ 2 = _,_
1 + _y_ 1 _,n−_ 1 + _· · ·_ + _y_ 1 _,n−_ 1 _y_ 1 _,n−_ 2 _· · · y_ 1 _,_ 3 1 + _y_ 1 _,n−_ 1 + _· · ·_ + _y_ 1 _,n−_ 1 _y_ 1 _,n−_ 2 _· · · y_ 1 _,_ 3

1

_· · ·_ _,_ 1 _−_ _zn−_ 2 = _._
1 + _y_ 1 _,n−_ 1 + _· · ·_ + _y_ 1 _,n−_ 1 _y_ 1 _,n−_ 2 _· · · y_ 1 _,_ 3

(6.5)
After the variable transformation, the integral becomes




        _In_ [Tr(] _[ϕ]_ [3][)] (1 _,_ 2 _, ..., n_ ) =

R _[n][−]_ [3]

_>_ 0



_n−_ 1



_i_ =3



d _y_ 1 _,i_




 
_Fi,j_ ( _y_ ) _[−][α][′][c][i,j]_ _,_ (6.6)

1 _≤i,j<n_



_y_ 1 _,i_ 
_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_



where the **F-polynomials** for our **ray-like** **triangulation**, _Fi,j_ ( _y_ ), are defined below
in (6.9), the exponents _ci,j_ are the non-planar variables (without _ci,n_ ) satisfying (2.4).
More generally for any initial triangulation, the _n_ -point tree-level amplitude can be
written as




    _In_ [Tr(] _[ϕ]_ [3][)] =

R _[n][−]_ [3]

_>_ 0



_n−_ 3



_I_ =1



d _yI_

_yI_




       

_ua,b_ _[α][′][X][a,b]_ ( _y_ ) =
( _a,b_ )



R _[n][−]_ [3]

_>_ 0





_Fi,j_ ( _y_ ) _[−][α][′][c][i,j]_ _,_ (6.7)

_i,j_







d _yI_



_n−_ 3



_I_ =1



_I_  
_yI_ _yI_ _[α][′][X][I]_



where _{yI_ _>_ 0 _}_ for _I_ = 1 _, · · ·_ _, n−_ 3 specify a triangulation of the _n_ -gon, which provides a
positive parametrization of _Un_ [+] [(thus] [the] [Parke-Taylor] [form] [becomes] [Ω(] _[U]_ _n_ [+][) =][ �] _I_ _[d]_ [ log] _[ y][I]_ [;]
for each curve/chord, ( _a, b_ ), the _u_ -variable _ua,b_ is a nice rational function of _yI_, which are
discussed in detail in [3], and the Koba-Nielsen factor becomes [�] _I_ _[y]_ _I_ _[α][′][X][I]_ times the product of
( _n−_ 2)( _n−_ 3)

2 _Fi,j_ ( _y_ ), which are F polynomials of _yI_ ’s for this triangulation [3], with exponents
_−α_ _[′]_ _ci,j_ .
Of course (6.7) is just the tree-level/disk instance of stringy integrals associated with
general surfaces _S_, which correspond to “stringy” Tr( _ϕ_ [3] ) amplitudes in the genus expansion


23


**Figure** **10** : F-polynomials for ray-like triangulations, at 5 and 6 points.


(details can again be found in [3]):




    _IS_ [Tr(] _[ϕ]_ [3][)] =

R _[d]_

_>_ 0



_d_



_I_ =1



d _yI_

_yI_




_u_ Γ( _y_ ) _[α][′][X]_ [Γ] _,_ (6.8)



where given the triangulation of the surface _S_, we have **positive** **coordinates** _yI_ for
_I_ = 1 _,_ 2 _, · · ·_ _, d_ and for **every** curve on _S_ denoted by Γ we have a _u_ **-variable** _u_ Γ( _y_ ), which
is a rational function of _yI_, and the kinematic variable _X_ Γ as its exponent.
In section 2 we concluded that by setting a collection of _ci,j_ = 0, the field theory Tr( _ϕ_ [3] )
amplitude vanishes, and that by turning **one** _c⋆_ back on, the amplitude factorizes into three
pieces, corresponding to lower point amplitudes. Both these properties heavily relied on
the Minkowski sum picture for the ABHY associahedron encoding these amplitudes. This
picture emerges from (6.7) (for any triangulation) in the _α_ _[′]_ _→_ 0 limit [6]. In this section,
we study how the field-theory statements generalize to the stringy Tr( _ϕ_ [3] ) integral (6.7).
Already in the field theory case, we concluded that we could access **all** zeros and
factorizations by choosing the realization of the ABHY associahedron determined by **ray-**
**like** triangulations (which produced a triangular region in the kinematic mesh). The same
is true for string amplitudes and so we will be mostly considering positive parametrizations
_{yI_ _}_ of (6.7) corresponding to **ray-like** triangulations [6]. In this case, the _F_ -polynomials
have a simple recursive structure, say at _n_ -point with triangulation _{y_ 1 _,_ 3 _, y_ 1 _,_ 4 _, · · ·_ _, y_ 1 _,n−_ 1 _}_ :


_Fi,j_ = 1 + _y_ 1 _,j_ + _y_ 1 _,jy_ 1 _,j−_ 1 + _· · ·_ + _y_ 1 _,j . . . y_ 1 _,i_ +2 _._ (6.9)


Since each _Fi,j_ is automatically associated with the non-planar Mandelstam, _ci,j_, it is
useful to organize them in the mesh picture. In figure 10 we present the 5-point and 6-point


24


kinematic mesh obtained when considering, respectively, triangulations _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ and
_{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_, as well as the corresponding _F_ -polynomials.
Choosing a ray-like triangulation, the kinematic variables appearing in (6.7) once written in terms of _Fi,j_ are: _XI_ and _ci,j_ with ( _i_ + 1 _, j_ + 1) = _I_ . This forms a kinematic
basis naturally associated with the corresponding triangular region of the kinematic mesh.
For example, at 6-point, for triangulation _{y_ 1 _,_ 3 _, y_ 1 _,_ 4 _, y_ 1 _,_ 5 _}_ we have _{X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, X_ 1 _,_ 5 _}_ and
_{c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, c_ 1 _,_ 5 _, c_ 2 _,_ 4 _, c_ 2 _,_ 5 _, c_ 3 _,_ 5 _}_ .
It is well known that string amplitudes have poles when _Xa,b_ equals some non-positive
integer (with _Xa,b_ = 0 corresponding to the pole of field-theory amplitudes) [6]. However,
like in the field-theory case, the kinematical locus where they vanish has not been studied
as extensively. Let us now understand how the field theory zeroes identified in section 2
generalize to the string amplitudes.


**6.1** **Zeros** **of** **Tr** ( _ϕ_ [3] ) **string** **amplitudes**


We begin with the simplest case, the 4-point amplitude. Considering the triangulation of
the square containing chord (1 _,_ 3), we get the following string amplitude:



_,_
Γ[ _α_ _[′]_ _c_ 1 _,_ 3]




    _I_ 4 [Tr(] _[ϕ]_ [3][)] =



d _y_ 1 _,_ 3




_[α][′]_ [(] _[c]_ [1] _[,]_ [3] _[ −]_ _[X]_ [1] _[,]_ [3][)]]

= [Γ[] _[α][′][X]_ [1] _[,]_ [3][]Γ[] _[α][′][X]_ [2] _[,]_ [4][]]
Γ[ _α_ _[′]_ _c_ 1 _,_ 3] Γ[ _α_ _[′]_ _c_ 1 _,_ 3]



R _>_ 0



_y_ 1 _,_ 3

_y_ 1 _,_ 3 _y_ 1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3] (1+ _y_ 1 _,_ 3) _[−][α][′][c]_ [13] = [Γ[] _[α][′][X]_ [1] _[,]_ [3][]Γ[] Γ[ _α_ _[α][′][′]_ _c_ [(] _[c]_ 1 _,_ [1] 3 _[,]_ [3] ] _[ −]_ _[X]_ [1] _[,]_ [3][)]]



(6.10)
which is exactly the Beta function B( _α_ _[′]_ _X_ 1 _,_ 3 _, α_ _[′]_ _X_ 2 _,_ 4). In the field-theory limit ( _α_ _[′]_ _→_ 0),

we get _I_ 4 [Tr(] _[ϕ]_ [3][)] _→_ _c_ 1 _,_ 3 _/_ ( _α_ _[′]_ _X_ 1 _,_ 3 _X_ 2 _,_ 4), which vanishes for _c_ 1 _,_ 3 = 0, as discussed previously.
However, from the Beta function (6.10), we see that, in addition to this zero, the full string
amplitude vanishes whenever _α_ _[′]_ _c_ 1 _,_ 3 is a **non-positive** **integer** .
From the integral representation, by setting _α_ _[′]_ _c_ 1 _,_ 3 = _−n_, with _n ∈_ N0 we get:



d _y_ 1 _,_ 3

R _>_ 0 _y_ 1 _,_ 3 _y_ 1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3][+] _[k]_


 - �� =0



R _>_ 0



d _y_ 1 _,_ 3



= 0 _._ (6.11)



_I_ 4 [Tr(] _[ϕ]_ [3][)] _→_



_n_



_k_ =0




- _n_

_k_



��



The integrals appearing in the sum are divergent, however, they all vanish by analytic
continuation. The integral of the form - _dy_ _[y][α][′][X]_ [bears] [resemblance] [to] [the] [concept] [of] [a]



continuation. The integral of the form �R _>_ 0 _dyy_ _[y][α][′][X]_ [bears] [resemblance] [to] [the] [concept] [of] [a]

**scaleless** **integral** within the context of Feynman integrals. The parameter _α_ _[′]_ serves as a
regulator factor, causing the integral to vanish. Specifically, we have:



_dy_
R _>_ 0 _y_



_._ (6.12)
���� _y_ = _∞_



_dy_

[=] _[ −]_ _[y][α][′][X]_
_y_ _[y][α][′][X]_ _α_ _[′]_ _X_



_α_ _[′]_ _X_



_dy_ - _∞_

[+]
_y_ _[y][α][′][X]_



1






R _>_ 0



_dy_ - 1

[=]
_y_ _[y][α][′][X]_



_dy_



_dy_



_dy_



+ _[y][α][′][X]_
���� _y_ =0 _α_ _[′]_ _X_



0



In the first part of the integral, _α_ _[′]_ is analytically continued to _α_ _[′]_ _X_ _>_ 0, while in the
second part of the integral, _α_ _[′]_ is analytically continued to _α_ _[′]_ _X_ _<_ 0. As a result, both
sides of the integral evaluate to zero. As we will see shortly the vanishing of this class of
one-dimensional integrals will be behind the general patterns of zeros we will describe in
string amplitudes.


25


Without loss of generality, let us choose the initial ray-triangulation to be _y_ 1 _,i_ for
_i_ = 3 _, · · ·_ _, n −_ 1, then, from (6.9), all the _F_ -polynomials depending on _y_ 1 _,i_ are those _Fab_
with 1 _≤_ _a_ _≤_ _i_ _−_ 2 _, i_ _≤_ _b_ _≤_ _n_ _−_ 1. Looking at the mesh, this is saying that all the
F-polynomials that depend on _y_ 1 _,j_ are contained **inside** **the** **causal** **diamond** **anchored**
**at** _X_ 1 _,j_ (see figure 10). So by setting all the _ca,b_ = _−na,b_, with _na,b_ _∈_ N0, inside this causal
diamond, the stringy integral vanishes because the integration in _y_ 1 _,i_ reduces to (6.11):



_×_ �R _>_ 0 d _yy_ 11 _,i,i_ _y_ 1 _α,i_ _[′]_ _X_ 1 _,i_ + _ka_ 1 _,b_ 1 + _···_ + _kaN,bN_


- �� =0



= 0 _,_



_In_ [Tr(] _[ϕ]_ [3][)] _→_




                
 
(remaining integrals) _×_

_ka_ 1 _,b_ 1 _,...,kaN,bN_ =0



_na_ 1 _,b_ 1 _,...,naN,bN_

 


d _y_ 1 _,i_



R _>_ 0



(6.13)
where _N_ corresponds to the number of _c_ ’s inside the causal diamond considered. Note that
the integral in _y_ 1 _,i_ can also be considered as the 4-pt integral but setting _c_ to zero, which
therefore vanishes.



**Zeros** In field theory, we concluded that the zero locus corresponded to setting the _c_ ’s
inside some causal diamond anchored in _X_ B to zero. For string amplitudes the zero locus
is now given by setting the same collection of _c_ ’s but to any non-positive integer, _i.e._ for
the mesh corresponding to triangulation (1 _,_ 3) _, . . .,_ (1 _, n −_ 1), if we want the zero to come
from the integration in _y_ 1 _,i_ :


_α_ _[′]_ _cab_ = _−na,b,_ for 1 _≤_ _a ≤_ _i −_ 2 _,_ _i ≤_ _b ≤_ _n −_ 1 _,_ and _na,b_ _∈_ N0 _._ (6.14)


Since each zero causal diamond is uniquely determined by the _X_ B it is anchored on,
the total number of zeros for the Tr( _ϕ_ [3] ) field theory amplitude is _[n]_ [(] _[n][−]_ [3)], which is equal to

2
the number of _Xi,j_ ’s, and so the number of poles.
Next, we will study factorization near such zeros. Exactly like in the field theory case,
we do this by relaxing one condition: so we set all but one _ca,b_ inside the causal diamond
to non-positive integers.


**6.2** **Factorization** **around** **the** **zeros**


For simplicity, let us begin by understanding what happens when we set all the _ca,b_ inside
the causal diamond to **zero**, but for one of them _c⋆_ = 0. In this case, the amplitude
factorizes into three pieces, just like in the field theory case. If instead, we allow the _c_ ’s
to be negative integers, then we get a sum of factorized terms, with interesting kinematic
shifts, as we will see shortly. We have already understood the reason for factorization in the
field theory limit from the perspective of the Minkowski-sum picture for the associahedron.
We will now see a related but different derivation for factorization whose fundamental origin
lies in certain separation properties of the _F_ -polynomials appearing in the stringy integral.
This will generalize our observations about factorization to the full stringy amplitude [2] .


2While we will not dwell on this point, our previous derivation centered on Minkowski sums and the one
we present now are closely connected, since the Minkowski summands are nothing other than the Newton
polytopes of the _F_ -polynomials.


26


**6.2.1** **Examples:** _n_ = 5 _,_ 6


We begin by studying our two simple examples of _n_ = 5 _,_ 6 string amplitudes. This will
expose the basic mechanism for factorization arising from special properties of the _F_ polynomials, which motivate simple variable changes on the _y_ variables, giving rise both to
factorization of the amplitude as well as precisely the same interesting kinematic shifts we
encountered in our field-theoretical analysis.
At _n_ = 5, the stringy integral reads:



4



_i_ =3




    - _∞_
_I_ 5 [Tr(] _[ϕ]_ [3][)] =

0




    - _∞_
_I_ 5 [Tr(] _[ϕ]_ [3][)] =



_y_ 1 _,i_ 
_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_



d _y_ 1 _,i_





_Fi,j_ ( **y** ) _[−][α][′][c][i,j]_

_i<j_




 - _∞_
=



d _y_ 1 _,_ 4

_y_ 1 _,_ 4 _y_ 1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3] _y_ 1 _[α]_ _,_ _[′]_ 4 _[X]_ [1] _[,]_ [4] (1 + _y_ 1 _,_ 3) _[−][α][′][c]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 4) _[−][α][′][c]_ [2] _[,]_ [4] (1 + _y_ 1 _,_ 4 + _y_ 1 _,_ 3 _y_ 1 _,_ 4) _[−][α][′][c]_ [1] _[,]_ [4] _._



0



d _y_ 1 _,_ 3

_y_ 1 _,_ 3



(6.15)
Let us consider the zero associated with the skinny rectangle, _{c_ 1 _,_ 3 _, c_ 1 _,_ 4 _}_ . Setting
_c_ 1 _,_ 3 = _c_ 1 _,_ 4 = 0 the integral becomes:



�� _∞_
_I_ 5 [Tr(] _[ϕ]_ [3][)] _→_

0



d _y_ 1 _,_ 3

_y_ 1 _,_ 3 _y_ 1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3]



d _y_ 1 _,_ 3



�� _∞_


0



d _y_ 1 _,_ 4

_y_ 1 _,_ 4 _y_ 1 _[α]_ _,_ _[′]_ 4 _[X]_ [1] _[,]_ [4] (1 + _y_ 1 _,_ 4) _[−][α][′][c]_ [2] _[,]_ [4] = 0 _._ (6.16)



Now letting _c_ 1 _,_ 4 = 0, the answer factorizes as follows:




    - _∞_
_I_ 5 [Tr(] _[ϕ]_ [3][)] _→_

0

    - _∞_
=



d _y_ 1 _,_ 3

_y_ 1 _,_ 3 _y_ 1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3]



_y_ 1 _,_ 4 - _y_ 1 _,_ 3 _y_ 1 _,_ 4

_y_ 1 _,_ 4 _y_ 1 _[α]_ _,_ _[′]_ 4 _[X]_ [1] _[,]_ [4] (1 + _y_ 1 _,_ 4) _[−][α][′]_ [(] _[c]_ [2] _[,]_ [4][+] _[c]_ [1] _[,]_ [4][)] 1 + (1 + _y_ 1 _,_ 4)



d _y_ 1 _,_ 3

_y_ 1 _,_ 3 _y_ 1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3]



d _y_ 1 _,_ 4

_y_ 1 _,_ 4 _y_ 1 _[α]_ _,_ _[′]_ 4 _[X]_ [1] _[,]_ [4] (1 + _y_ 1 _,_ 4) _[−][α][′][c]_ [2] _[,]_ [4] (1 + _y_ 1 _,_ 4 + _y_ 1 _,_ 3 _y_ 1 _,_ 4) _[−][α][′][c]_ [1] _[,]_ [4]



d _y_ 1 _,_ 4




- _−α′c_ 1 _,_ 4
_._




- _∞_


0

- _∞_



0



0



d _y_ 1 _,_ 4 - _y_ 1 _,_ 3 _y_ 1 _,_ 4

_y_ 1 _,_ 4 _y_ 1 _[α]_ _,_ _[′]_ 4 _[X]_ [1] _[,]_ [4] (1 + _y_ 1 _,_ 4) _[−][α][′]_ [(] _[c]_ [2] _[,]_ [4][+] _[c]_ [1] _[,]_ [4][)] 1 + (1 + _y_ 1 _,_ 4)



(6.17)
Now changing variables to _y_ ˜1 _,_ 3 = _y_ 1 _,_ 3 _y_ 1 _,_ 4 _/_ (1 + _y_ 1 _,_ 4), we get:



d _y_ 1 _,_ 4

_y_ 1 _,_ 4 _y_ 1 _[α]_ _,_ _[′]_ 4 [(] _[X]_ [1] _[,]_ [4] _[−][X]_ [1] _[,]_ [3][)] (1 + _y_ 1 _,_ 4) _[−][α][′]_ [(] _[c]_ [2] _[,]_ [4][+] _[c]_ [1] _[,]_ [4] _[−][X]_ [1] _[,]_ [3][)]




    - _∞_
_I_ 5 [Tr(] _[ϕ]_ [3][)] _→_

0



_y_ 1 _,_ 3 - _∞_

_y_ ˜1 _,_ 3 _y_ ˜1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3] (1 + ˜ _y_ 1 _,_ 3) _[−][α][′][c]_ [1] _[,]_ [4] 0



d˜ _y_ 1 _,_ 3



0



= _I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,_ 3 _, α_ _[′]_ ( _c_ 1 _,_ 4 _−_ _X_ 1 _,_ 3)) _× I_ 4 [up] _[,]_ [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ ( _X_ 1 _,_ 4 _−_ _X_ 1 _,_ 3) _, α_ _[′]_ ( _c_ 2 _,_ 4 + _c_ 1 _,_ 4 _−_ _X_ 1 _,_ 4))

= _I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,_ 3 _, α_ _[′]_ _X_ 2 _,_ 5) _× I_ 4 [up] _[,]_ [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 2 _,_ 4 _, α_ _[′]_ _X_ 3 _,_ 5) _._
(6.18)
We see clearly a direct stringy generalization of the factorization we saw in the field
theory limit. We have the 4-point amplitude pre-factor, now as a full stringy amplitude
_I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,_ 3 _, α_ _[′]_ _X_ 2 _,_ 5), that vanishes when we further set _c_ 1 _,_ 4 _→_ 0. Then we have a product
of smaller stringy amplitudes, a (trivial) 3-point “down” amplitude and the “up” amplitude
_I_ 4 [up] _[,]_ [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 2 _,_ 4 _, α_ _[′]_ _X_ 3 _,_ 5), whose (interestingly redefined) kinematic variables _X_ 2 _,_ 4 _, X_ 3 _,_ 5 precisely agree the same way as our previous analysis as summarized in figure 5. The mechanism for factorization is easy to see as a consequence of a “separation property” of _F_ polynomials. After setting _c_ 1 _,_ 3 _→_ 0, all the non-trivial dependence on _y_ 1 _,_ 3 is in the _F_ polynomial (1 + _y_ 1 _,_ 4 + _y_ 1 _,_ 4 _y_ 1 _,_ 3) = ( _A_ + _y_ 1 _,_ 3 _B_ ) with _A_ = (1 + _y_ 1 _,_ 4) and _B_ = _y_ 1 _,_ 4 and quite
nicely, both _A, B_ are polynomials that appear in smaller amplitudes. We can manifest


27


the factorization by the change of variables _y_ 1 _,_ 3 _B/A_ = _y_ ˜1 _,_ 3, and this is what induces the
interesting kinematic redefinitions in the smaller amplitude factors.
At 6-point, choosing once more the triangulation _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ for _n_ = 6, the
stringy integral is given by:



5



_i_ =3


5



_i_ =3




    - _∞_
_I_ 6 [Tr(] _[ϕ]_ [3][)] =

0




    - _∞_
_I_ 6 [Tr(] _[ϕ]_ [3][)] =



_y_ 1 _,i_ 
_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_



d _y_ 1 _,i_





_Fi,j_ ( **y** ) _[−][α][′][c][i,j]_

_i<j_




 - _∞_
=

0



d _y_ 1 _,i_

_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_ (1 + _y_ 1 _,_ 3) _[−][α][′][c]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 4) _[−][α][′][c]_ [2] _[,]_ [4] (1 + _y_ 1 _,_ 5) _[−][α][′][c]_ [3] _[,]_ [5]



_×_ (1 + _y_ 1 _,_ 4(1 + _y_ 1 _,_ 3)) _[−][α][′][c]_ [1] _[,]_ [4] (1 + _y_ 1 _,_ 5(1 + _y_ 1 _,_ 4)) _[−][α][′][c]_ [2] _[,]_ [5] (1 + _y_ 1 _,_ 5(1 + _y_ 1 _,_ 4(1 + _y_ 1 _,_ 3))) _[−][α][′][c]_ [1] _[,]_ [5] _._
(6.19)
At 6-point we have our two kinds of zeros, the “skinny rectangle” and “big square”
patterns. The near-zero factorizations for the skinny rectangles exactly mirror what we
have already seen at 5 points so we will look at the square pattern, where setting _c_ 14 =
_c_ 24 = _c_ 15 = _c_ 25 = 0 makes the amplitude vanish.



5



_i_ =3




    - _∞_
_I_ 6 [Tr(] _[ϕ]_ [3][)] _→_

0




    - _∞_
_I_ 6 [Tr(] _[ϕ]_ [3][)] _→_



d _y_ 1 _,i_

_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_ (1 + _y_ 1 _,_ 3) _[−][α][′][c]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 5) _[−][α][′][c]_ [3] _[,]_ [5]




 - _∞_
=

0



d _y_ 1 _,_ 4

_y_ 1 _,_ 4 _y_ 1 _[α]_ _,_ _[′]_ 4 _[X]_ [1] _[,]_ [4]



(6.20)











d _y_ 1 _,i_



_i_ =4



_y_ 1 _,i_ �� _∞_

_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_ (1 + _y_ 1 _,_ 3) _[−][α][′][c]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 5) _[−][α][′][c]_ [3] _[,]_ [5] 0



0




                          - ��                          =0

= 0 _._



By turning on _c_ 1 _,_ 5, we expect the stringy integral to factorize into two 4-point amplitudes (up and down) and the 4-point prefactor:



5



_i_ =3


5





    - _∞_
_I_ 6 [Tr(] _[ϕ]_ [3][)] _→_

0




    - _∞_
_I_ 6 [Tr(] _[ϕ]_ [3][)] _→_



d _y_ 1 _,i_

_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_ (1 + _y_ 1 _,_ 3) _[−][α][′][c]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 5) _[−][α][′][c]_ [3] _[,]_ [5] (1 + _y_ 1 _,_ 5 + _y_ 1 _,_ 4 _y_ 1 _,_ 5 + _y_ 1 _,_ 3 _y_ 1 _,_ 4 _y_ 1 _,_ 5) _[−][α][′][c]_ [1] _[,]_ [5]




 - _∞_
=

0




- _−α′c_ 1 _,_ 5
_._



d _y_ 1 _,i_



_i_ =3



_y_ 1 _,i_ 
_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_ (1 + _y_ 1 _,_ 3) _[−][α][′][c]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 5) _[−][α][′]_ [(] _[c]_ [3] _[,]_ [5][+] _[c]_ [1] _[,]_ [5][)] 1 + [(1 +] (1 + _[ y]_ [1] _[,]_ [3] _y_ [)] _[y]_ 1 _,_ [1] 5 _[,]_ [4] ) _[y]_ [1] _[,]_ [5]



(1 + _y_ 1 _,_ 5)



(6.21)
So changing variables to _y_ ˜1 _,_ 4 = (1 + _y_ 1 _,_ 3) _y_ 1 _,_ 4 _y_ 1 _,_ 5 _/_ (1 + _y_ 1 _,_ 5), we get:




    - _∞_
_I_ 6 [Tr(] _[ϕ]_ [3][)] _→_

0



0



_y_ 1 _,_ 3 - _∞_

_y_ 1 _,_ 3 _y_ 1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 3) _[−][α][′]_ [(] _[c]_ [1] _[,]_ [3][+] _[X]_ [1] _[,]_ [4][)] _×_ 0



d˜ _y_ 1 _,_ 4

_y_ ˜1 _,_ 4 _y_ ˜1 _[α]_ _,_ _[′]_ 4 _[X]_ [1] _[,]_ [4] (1 + ˜ _y_ 1 _,_ 4) _[−][α][′][c]_ [1] _[,]_ [5]



d _y_ 1 _,_ 3




 - _∞_
_×_

0



d _y_ 1 _,_ 5

_y_ 1 _,_ 5 _y_ 1 _[α]_ _,_ _[′]_ 5 [(] _[X]_ [1] _[,]_ [5] _[−][X]_ [1] _[,]_ [4][)] (1 + _y_ 1 _,_ 5) _[−][α][′]_ [(] _[c]_ [3] _[,]_ [5][+] _[c]_ [1] _[,]_ [5] _[−][X]_ [1] _[,]_ [4][)]



= _I_ 4 [down] _[,]_ [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,_ 3 _, α_ _[′]_ ( _c_ 1 _,_ 3 + _X_ 1 _,_ 4 _−_ _X_ 1 _,_ 3)) _× I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,_ 4 _, α_ _[′]_ ( _c_ 1 _,_ 5 _−_ _X_ 1 _,_ 4))

_× I_ 4 [up] _[,]_ [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ ( _X_ 1 _,_ 5 _−_ _X_ 1 _,_ 4) _, α_ _[′]_ ( _c_ 3 _,_ 5 + _c_ 1 _,_ 5 _−_ _X_ 1 _,_ 5))

= _I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,_ 4 _, α_ _[′]_ _X_ 3 _,_ 6) _× I_ 4 [down] _[,]_ [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,_ 3 _, α_ _[′]_ _X_ 2 _,_ 4) _× I_ 4 [up] _[,]_ [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 3 _,_ 5 _, α_ _[′]_ _X_ 4 _,_ 6) _._
(6.22)


28


As in the 5-point example the mechanism for factorization is a separation property of
the _F_ polynomials. Having set _c_ 1 _,_ 4 _, c_ 2 _,_ 4 _, c_ 2 _,_ 5 _→_ 0, the only non-trivial dependence on _y_ 1 _,_ 4 is
in the _F_ -polynomial 1 + _y_ 1 _,_ 5 + _y_ 1 _,_ 4 _y_ 1 _,_ 5 + _y_ 1 _,_ 3 _y_ 1 _,_ 4 _y_ 1 _,_ 5 = _A_ + _y_ 1 _,_ 4 _B_, where _A_ = (1 + _y_ 1 _,_ 5) _, B_ =
_y_ 1 _,_ 5(1 + _y_ 1 _,_ 3). Again nicely _A, B_ are (up to monomial factors) _F_ -polynomials for smaller
amplitudes. We then make the change of variable to _By_ 1 _,_ 4 _/A_ = _y_ ˜1 _,_ 4, and this induces the
interesting kinematic shifts for the “up” and “down” four-point amplitudes.


**6.2.2** **General** **Proof**


The general proof of factorization works in exactly the same way as we just saw in our
examples; apart from decoration with indices, the steps are exactly the same as we saw
above. We consider the zero associated with maximal causal diamond anchored to _X_ 1 _,i_,
and consider turning back on _c⋆_ = _ck,m_ = 0. Then stringy integral factorizes as follows:



_i−_ 1

    _In_ [Tr(] _[ϕ]_ [3][)] _→_ 

_l_ =3



_j_ = _i_ 1 _≤a<b−_ 1 _≤i−_ 1 (6.23)

 
_Fe,f_ ( **y** ) _[−][α][′][c][e,f]_ _._

_i−_ 1 _≤e<f_ _−_ 1 _<n−_ 1



d _y_ 1 _,l_




 
_Fa,b_ ( **y** ) _[−][α][′][c][a,b]_

1 _≤a<b−_ 1 _≤i−_ 1



_y_ 1 _,l_

_y_ 1 _,l_ _y_ 1 _[α]_ _,l_ _[′][X]_ [1] _[,l]_



_n−_ 1


 


_j_ = _i_



d _y_ 1 _,j_



_y_ 1 _,j_ 
_y_ 1 _,j_ _y_ 1 _[α]_ _,j_ _[′][X]_ [1] _[,j]_



_× Fk,m_ ( **y** ) _[−][α][′][c][k,m]_ _×_ 


As in our examples, the key point is that the only _F_ _−_ polynomial depending on _y_ 1 _,i_
is _Fk,m_ ( **y** ) = 1 + _y_ 1 _,m_ + _· · ·_ + _y_ 1 _,m · · · y_ 1 _,k_ +2 _≡_ _A_ + _y_ 1 _,iB_, with _A_ = _Fi−_ 1 _,m_ and _B_ =
_Fk,i−_ 1 - _mp_ = _i_ +1 _[y]_ [1] _[,p]_ [,] [which] [suggests] [the] [variable] [change] _[By]_ [1] _[,i][/A]_ [ =] _[y]_ [˜][1] _[,i]_ [.] [Following] [our] [noses]
this will give the factorization for the amplitude into smaller string amplitudes, with the
same kinematical redefinition encountered in the field theory limit. Working everything out
explicitly, we easily perform the integral over _y_ 1 _,i_ :


     - d _y_ 1 _,i_      - d _y_ 1 _,i_
_y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_ _Fk,m_ ( **y** ) _[−][α][′][c][k,m]_ = _y_ 1 _,i_ _y_ 1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_ ( _A_ + _y_ 1 _,iB_ ) _[−][α][′][c][k,m]_




           - d˜ _y_ 1 _,i_
= _A_ _[−][α][′][c][k,m]_ [+] _[α][′][X]_ [1] _[,i]_ _B_ _[−][α][′][X]_ [1] _[,i]_ _y_ ˜1 _,i_ _y_ ˜1 _[α]_ _,i_ _[′][X]_ [1] _[,i]_ (1 + ˜ _y_ 1 _,i_ ) _[−][α][′][c][k,m]_



(6.24)



= _A_ _[−][α][′][c][k,m]_ [+] _[α][′][X]_ [1] _[,i]_ _B_ _[−][α][′][X]_ [1] _[,i]_ _× I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,i, α_ _[′]_ ( _ck,m −_ _X_ 1 _,i_ ))

              - ��               


_,_



_I_ 4 [Tr(] _[ϕ]_ [3)] ( _α_ _[′]_ _X_ B _,α_ _[′]_ _X_ T)



where in the second line we used our change variables _y_ ˜1 _,i_ = _By_ 1 _,i/A_, which reduces the
integral to the 4-point stringy integral. This 4-point factor is exactly analogous to the one
we saw in the factorization of the field theory amplitudes, (1 _/X_ B +1 _/X_ T), except that now
we get indeed the full 4-point string amplitude. Exactly in the same way as in the field
theory, this factor makes manifest that if we further set _ck,m_ to a non-positive integer the


29


whole amplitude vanishes. Plugging this result back into (6.23),



_i−_ 1


 

_l_ =3



d _y_ 1 _,l_



_n−_ 1

          
 -  
_Fab_ ( **y** ) _[−][α][′][c][ab]_

1 _≤a<b−_ 1 _≤i−_ 1 _j_ = _i_




 
_Fe,f_ ( **y** ) _[−][α][′][c][e,f]_

_i−_ 1 _≤e<f_ _−_ 1 _<n−_ 1



_y_ 1 _,l_ 
_y_ 1 _,l_ _y_ 1 _[α]_ _,l_ _[′][X]_ [1] _[,l]_



_j_ = _i_ +1



d _y_ 1 _,j_



_y_ 1 _,j_ 
_y_ 1 _,j_ _y_ 1 _[α]_ _,j_ _[′][X]_ [1] _[,j]_



_× A_ _[−][α][′][c][k,m]_ [+] _[α][′][X]_ [1] _[,i]_ _B_ _[−][α][′][X]_ [1] _[,i]_ _× I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,i, α_ _[′]_ ( _ck,m −_ _X_ 1 _,i_ ))



_i−_ 1

 
 =


_l_ =3



d _y_ 1 _,l_



_n−_ 1

          
 - _Fa,b_ ( **y** ) _[−][α][′][c]_ _a,b_ _[′]_  

1 _≤a<b−_ 1 _≤i−_ 1 _j_ = _i_




 - _Fe,f_ ( **y** ) _[−][α][′][c]_ _e,f_ _[′]_


_i−_ 1 _≤e<f_ _−_ 1 _<n−_ 1



_y_ 1 _,l_ 
_y_ 1 _,l_ _y_ 1 _[α]_ _,l_ _[′][X]_ [1] _[,l]_



_j_ = _i_ +1



d _y_ 1 _,j_



_yy_ 11 _,j,j_ _y_ 1 _α,j_ _[′]_ _X_ 1 _[′]_ _,j_ 


_× I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,i, α_ _[′]_ ( _ck,m −_ _X_ 1 _,i_ ))

_≡Ii_ [down] _[,]_ [Tr(] _[ϕ]_ [3][)] _× In_ [up] _−_ _[,]_ _i_ [Tr(] +2 _[ϕ]_ [3][)] _× I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,i, α_ _[′]_ ( _ck,m −_ _X_ 1 _,i_ )) _,_
(6.25)
where in the third line we replace _A_ ( _⃗y_ ) and _B_ ( _⃗y_ ), and define the shifted exponents _c_ _[′]_ and
_X_ _[′]_ . We have that: _c_ _[′]_ _a,b_ [=] _[c][a,b]_ [except] [for] _[c][′]_ _k,i−_ 1 [=] _[c][k,i][−]_ [1][ +] _[ X]_ [1] _[,i]_ [,] [while] _[c][′]_ _e,f_ [=] _[c][e,f]_ [except] [for]
_c_ _[′]_ _i−_ 1 _,m_ [=] _[ c][i][−]_ [1] _[,m]_ [ +] _[ c][k,m][ −]_ _[X]_ [1] _[,i]_ [.] [Finally] [we] [also] [have] _[X]_ 1 _[′]_ _,j_ [=] _[ X]_ [1] _[,j][ −]_ _[X]_ [1] _[,i]_ [,] [for] _[j]_ [=] _[ i]_ [ + 1] _[, . . ., m]_ [.]
As we will see shortly, these shifts are exactly such that the up and down amplitudes depend
on exactly the same kinematics as the respective up and down amplitudes in the field theory
case, _i.e._ the lower point string amplitudes appearing in the factorization also follow the
kinematic shifts summarized in figure 8.
Looking at the kinematic mesh, _Ii_ [down] _[,]_ [Tr(] _[ϕ]_ [3][)] denotes the string amplitude corresponding

to the down triangular mesh, which is _Ii_ [Tr(] _[ϕ]_ [3][)] (1 _, . . ., i_ _−_ 1 _, I_ ) with _pI_ = _−_ [�] _[i]_ _j_ _[−]_ =1 [1] _[p][j]_ [,] [but now]
with shifted kinematic invariants:



_i−_ 1

      _Ii_ [down] _[,]_ [Tr(] _[ϕ]_ [3][)] = 
_l_ =3



d _y_ 1 _,l_




 - _Fa,b_ ( **y** ) _[−][α][′][c]_ _a,b_ _[′]_


1 _≤a<b−_ 1 _≤i−_ 1



_y_ 1 _,l_ 
_y_ 1 _,l_ _y_ 1 _[α]_ _,l_ _[′][X]_ [1] _[,l]_



= _Ii_ [Tr(] _[ϕ]_ [3][)] (1 _, . . ., i −_ 1 _, I_ ) _,_
���� _Xl,i→Xl,i_ + _X_ 1 _,i_ = _Xl,n,_ for _l_ =2 _,...,k._



(6.26)



where the shifted rules for the kinematic invariant are shifting the _Xl,i_ to _Xl,i_ + _X_ 1 _,i_, which
is equal to _Xl,n_ since the zero conditions, for _l_ = 2 _, . . ., k_ . These shifted rules are equivalent
to the definition of _c_ _[′]_ _a,b_ [.]

In turn, _In_ [up] _−_ _[,]_ _i_ [Tr(] +2 _[ϕ]_ [3][)] denotes as the string amplitude corresponding to the upper trian
gular mesh, which is _In_ [Tr(] _−i_ _[ϕ]_ +2 [3][)][(] _[i, . . ., n, J]_ [)] [with] _[p][J]_ [=] _[−]_ [�] _[n]_ _j_ = _i_ _[p][j]_ [,] [but] [with] [shifted] [kinematic]
invariant:



_n−_ 1

     _In_ [up] _−_ _[,]_ _i_ [Tr(] +2 _[ϕ]_ [3][)] = 
_j_ = _i_ +1


_n−_ 1

     
   =


_j_ = _i_ +1



d _y_ 1 _,j_




 - _Fe,f_ ( **y** ) _[−][α][′][c]_ _e,f_ _[′]_


_i−_ 1 _≤e<f_ _−_ 1 _<n−_ 1



_yy_ 11 _,j,j_ _y_ 1 _α,j_ _[′]_ _X_ 1 _[′]_ _,j_ 


d _yi−_ 1 _,j_




 - _Fe,f_ ( **y** ) _[−][α][′][c]_ _e,f_ _[′]_


_i−_ 1 _≤e<f_ _−_ 1 _<n−_ 1



_yyi−i−_ 11 _,j,j_ _yiα−_ _[′]_ _X_ 1 _,ji_ _[′]_ _−_ 1 _,j_ 


(6.27)



= _In_ [Tr(] _−i_ _[ϕ]_ +2 [3][)][(] _[i, . . ., n, J]_ [)] _[|][X]_ _i−_ 1 _,j_ _[→][X]_ _i−_ 1 _,j_ _[−][X]_ _i−_ 1 _,n_ [=] _[X]_ 1 _,j_ _[,]_ [for] _[j]_ [=] _[m]_ [+1] _[,...,n][−]_ [1] _[.][,]_


30


where in the second line, we change the integration variables _y_ 1 _,j_ to _yi−_ 1 _,j_ . The kinematic
shifts send _Xi−_ 1 _,j_ to _Xi−_ 1 _,j_ _−_ _Xi−_ 1 _,n_, which is equal to _X_ 1 _,j_ since the zero conditions, for
_j_ = _m_ + 1 _, . . ., n −_ 1. This shifted rules are equivalent to the definition of _c_ _[′]_ _e,f_ [and] _[X]_ 1 _[′]_ _,j_ [.]
In summary, by picking a zero causal diamond, _cab_ = 0 _,_ for 1 _≤_ _a ≤_ _i_ _−_ 2 _, i ≤_ _b ≤_ _n_ _−_ 1,
and letting _ck,m_ = 0, the stringy integral for Tr( _ϕ_ [3] ) factorizes into lower point amplitudes
according to:


_In_ [Tr(] _[ϕ]_ [3][)] _→Ii_ [down] _[,]_ [Tr(] _[ϕ]_ [3][)] _× In_ [up] _−_ _[,]_ _i_ [Tr(] +2 _[ϕ]_ [3][)] _× I_ 4 [Tr(] _[ϕ]_ [3][)] ( _α_ _[′]_ _X_ 1 _,i, α_ _[′]_ ( _ckm −_ _X_ 1 _,i_ )) _._ (6.28)


The shifted rules for up and down amplitudes are exactly those presented in figure 8,
and can be summarized as follows:


_Xl,i_ _→_ _Xl,i_ + _X_ 1 _,i_ = _Xl,n,_ for _l_ = 2 _, . . ., k._ (6.29)

_Xi−_ 1 _,j_ _→_ _Xi−_ 1 _,j_ _−_ _Xi−_ 1 _,n_ = _X_ 1 _,j,_ for _j_ = _m_ + 1 _, . . ., n −_ 1 _._ (6.30)


**6.2.3** **Factorization** **for** **general** **negative** **integers**


We have seen that when all the mesh constants but one in a maximal causal diamond are set
to zero, the amplitude simplifies by factoring to a product of smaller amplitudes with nontrivially modified kinematics. Just as the statement about zeros extends to the full string
amplitude when the mesh constants are set more generally either to zero or negative integers,
the near-zero factorizations also generalize to this case. We will see that instead of simply
factoring into a product of smaller amplitudes, we get an interesting sum over products of
smaller amplitudes with redefined kinematics. To see how this works let us consider as an
example a skinny rectangle factorization where we set _c_ 1 _,_ 3 = _−n_ 1 _,_ 3 _, c_ 1 _,_ 5 = _−n_ 1 _,_ 5 but we
turn on _c_ 1 _,_ 4. The stringy integral becomes




  - _∞_
_I_ 6 =

0



d _y_ 1 _,_ 3 d _y_ 1 _,_ 4 d _y_ 1 _,_ 5

_y_ 1 _[X]_ _,_ 3 [1] _[,]_ [3] _[y]_ 1 _[X]_ _,_ 4 [1] _[,]_ [4] _[y]_ 1 _[X]_ _,_ 5 [1] _[,]_ [5] _×_ (1 + _y_ 1 _,_ 3) _[n]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 5(1 + _y_ 1 _,_ 4(1 + _y_ 1 _,_ 3))) _[n]_ [1] _[,]_ [5] _×_
_y_ 1 _,_ 3 _y_ 1 _,_ 4 _y_ 1 _,_ 5



(1 + _y_ 1 _,_ 4(1 + _y_ 1 _,_ 3)) _[−][c]_ [1] _[,]_ [4] (1 + _y_ 1 _,_ 4) _[−][c]_ [2] _[,]_ [4] (1 + _y_ 1 _,_ 5(1 + _y_ 1 _,_ 4)) _[−][c]_ [2] _[,]_ [5] (1 + _y_ 1 _,_ 5) _[−][c]_ [3] _[,]_ [5] _._


Relative to our usual expressions when mesh constants are set to zero, we have the
extra factor on the first line, (1 + _y_ 1 _,_ 3) _[n]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 5(1 + _y_ 1 _,_ 4(1 + _y_ 1 _,_ 3))) _[n]_ [1] _[,]_ [5] . The important
fact is that for _n_ 1 _,_ 3 _, n_ 1 _,_ 5 positive integers, this factor is a _finite_ _polynomial_ in _y_ 1 _,_ 3 _, y_ 1 _,_ 4 _, y_ 1 _,_ 5,
we have


       (1+ _y_ 1 _,_ 3) _[n]_ [1] _[,]_ [3] (1+ _y_ 1 _,_ 5(1+ _y_ 1 _,_ 4(1+ _y_ 1 _,_ 3))) _[n]_ [1] _[,]_ [5] = _Ck_ 1 _,_ 3 _,k_ 1 _,_ 4 _,k_ 1 _,_ 5( _n_ 1 _,_ 3 _, n_ 1 _,_ 5) _y_ 1 _[k]_ _,_ [1] 3 _[,]_ [3] _[y]_ 1 _[k]_ _,_ [1] 4 _[,]_ [4] _[y]_ 1 _[k]_ _,_ [1] 5 _[,]_ [5] _[,]_

_k_ 1 _,_ 3 _,k_ 1 _,_ 4 _,k_ 1 _,_ 5

(6.31)
where _Ck_ 1 _,_ 3 _,k_ 1 _,_ 4 _,k_ 1 _,_ 5( _n_ 1 _,_ 3 _, n_ 1 _,_ 5) are constants arising simply from performing the multinomial expansions of each term; while these can be trivially computed the detailed expressions are not important for us. But at this point, the expression is precisely the
one we encountered previously when the mesh constants were set to zero, except as a
weighted sum with weights _Ck_ 1 _,_ 3 _,k_ 1 _,_ 4 _,k_ 1 _,_ 5 of the previous amplitudes with kinematics shifted
as _X_ 1 _,_ 3 _→_ _X_ 1 _,_ 3 + _k_ 1 _,_ 3 _,_ _X_ 1 _,_ 4 _→_ _X_ 1 _,_ 4 + _k_ 1 _,_ 4 _,_ _X_ 1 _,_ 5 _→_ _X_ 1 _,_ 5 + _k_ 1 _,_ 5.


31


For instance if we set _n_ 1 _,_ 3 = 1 _, n_ 1 _,_ 5 = 1, we have (1+ _y_ 1 _,_ 3) [1] (1+ _y_ 1 _,_ 5(1+ _y_ 1 _,_ 4(1+ _y_ 1 _,_ 3))) [1] =
1+ _y_ 1 _,_ 3 + _y_ 1 _,_ 5 + _y_ 1 _,_ 3 _y_ 1 _,_ 5 + _y_ 1 _,_ 4 _y_ 1 _,_ 5 +2 _y_ 1 _,_ 3 _y_ 1 _,_ 4 _y_ 1 _,_ 5 + _y_ 1 [2] _,_ 3 _[y]_ [1] _[,]_ [4] _[y]_ [1] _[,]_ [5][.] [Now recall that for factorization]
when mesh constants are set to zero, we have the factorization _I_ 6 _→_ _F_ 4( _X_ ) _F_ 5( _X_ ) where
_F_ 4( _X_ ) = Γ[ _X_ 1 _,_ 3]Γ[ _X_ 2 _,_ 6] _/_ Γ[ _X_ 1 _,_ 3 + _X_ 2 _,_ 6] and _F_ 5( _X_ ) = _I_ 5( _X_ 2 _,_ 4 _, X_ 2 _,_ 5 _→_ _X_ 1 _,_ 5 _, X_ 3 _,_ 5 _, X_ 3 _,_ 6 _, X_ 4 _,_ 6).
Then at _n_ 1 _,_ 3 = _n_ 1 _,_ 5 = 1 we instead have the factorization


_I_ 6 _→_ ( _F_ 4 _F_ 5) + ( _F_ 4 _F_ 5) ( _X_ 1 _,_ 3 _→_ _X_ 1 _,_ 3 + 1)

+ ( _F_ 4 _F_ 5) ( _X_ 1 _,_ 5 _→_ _X_ 1 _,_ 5 + 1) + ( _F_ 4 _F_ 5) ( _X_ 1 _,_ 3 _→_ _X_ 1 _,_ 3 + 1 _, X_ 1 _,_ 5 _→_ _X_ 1 _,_ 5 + 1)

+ ( _F_ 4 _F_ 5) ( _X_ 1 _,_ 4 _→_ _X_ 1 _,_ 4 + 1 _, X_ 1 _,_ 5 _→_ _X_ 1 _,_ 5 + 1)

+ 2 ( _F_ 4 _F_ 5) ( _X_ 1 _,_ 3 _→_ _X_ 1 _,_ 3 + 1 _, X_ 1 _,_ 4 _→_ _X_ 1 _,_ 4 + 1 _, X_ 1 _,_ 5 _→_ _X_ 1 _,_ 5 + 1)

+ ( _F_ 4 _F_ 5) ( _X_ 1 _,_ 3 _→_ _X_ 1 _,_ 3 + 2 _, X_ 1 _,_ 4 _→_ _X_ 1 _,_ 4 + 1 _, X_ 1 _,_ 5 _→_ _X_ 1 _,_ 5 + 1) _._ (6.32)


The story for near-zero factorizations when mesh constants are set to general negative
integers is the same. We always get a factor which is a polynomial _P_ in all the _y_ ’s associated
with the _F_ polynomials raised to integer powers, which we can simply expand to get a big
polynomial in the _y_ ’s. This then gives us a factorization of exactly the same form as
with vanishing mesh constants, but as a sum over shifted kinematics determined by the
polynomial _P_ .


**7** **Stringy** _δ_ **eformation**


In this section, we propose a class of “universal” stringy models as a one-parameter deformation of the tree-level stringy Tr( _ϕ_ [3] ) amplitude for an even number 2 _n_ of particles, which
will be the basis of our unification of Tr( _ϕ_ [3] ), pion and gluon amplitudes.
This deformation amounts to inserting a factor ( [�] _ue,e/_ _uo,o_ ) _[α][′][δ]_ in the string integral

[�]
(6.7), where we take the product of all _ua,b_ with _a, b_ both being even, over the product of
_ua,b_ both being odd, and _δ_ is the deformation parameter:




- _α′δ_
_,_ (7.1)




   _I_ 2 _[δ]_ _n_ [=]

R [2] _[n][−]_ [3]

_>_ 0



2 _n−_ 3



_I_ =1



d _yI_

_yI_





_u_ _[α]_ _a,b_ _[′][X][a,b]_
( _a,b_ )



��
( _e,e_ ) _[u][e,e]_

 ( _o,o_ ) _[u][o,o]_



expanding this ratio, we see that this factor is simply **shifting** the kinematics, _Xa,b_, of the
un-deformed, stringy Tr( _ϕ_ [3] ) amplitude:


_I_ 2 _[δ]_ _n_ [=] _[ I]_ 2 [Tr] _n_ [(] _[ϕ]_ [3][)] [ _α_ _[′]_ _Xe,e_ _→_ _α_ _[′]_ ( _Xe,e_ + _δ_ ) _, α_ _[′]_ _Xo,o_ _→_ _α_ _[′]_ ( _Xo,o −_ _δ_ )] _._ (7.2)


In addition, we claim that for different values of _α_ _[′]_ _δ_ we get different colored theories:


1. _α_ _[′]_ _δ_ = 0: In this case, we get back the usual stringy Tr( _ϕ_ [3] ) integral, so at low energies,
we get the field theory amplitudes of the Tr( _ϕ_ [3] ) Lagrangian:


_L_ Tr( _ϕ_ 3) = Tr ( _∂ϕ_ ) [2] + _g_ Tr( _ϕ_ [3] ) _._ (7.3)


32


2. _α_ _[′]_ _δ_ _∈_ (0 _,_ 1): In this case we claim that, at low energies, we get field theory amplitudes
of the U(N) Non-linear Sigma Model ( _c.f._ [23]) :


1           -           _L_ NLSM = _∂µ_ U _[†]_ _∂_ _[µ]_ U _,_ with U = (I + _λ_ Φ)(I _−_ _λ_ Φ) _[−]_ [1] _._ (7.4)

[Tr]
8 _λ_ [2]


3. _α_ _[′]_ _δ_ = 1: In this case, we claim that, at low energies, we get Yang-Mills theory (YM).
In fact, it is not simply YM, but instead gluons and adjoint scalars (YMS) (these
YMS amplitudes have been studied in _e.g._ [13]), with the following Lagrangian:










_I_ = _J_



YM

[1] _[−]_ _[g]_ [2]

2 _[D][µ][ϕ][I]_ _[D][µ][ϕ][I]_ 4



4





- _ϕ_ _[I]_ _, ϕ_ _[J]_ [�][2]  _._ (7.5)



_L_ YMS = _−_ Tr



 [1]




[1] [+] [1]

4 _[F][ µν][F][µν]_ 2



In the rest of this section, we will study in detail how this deformation works. However,
for a more complete explanation of each shift see [18, 19].
There are multiple ways to motivate why this new factor is the correct deformation [18,
19]. Notwithstanding, in the context of this note, what interests us the most is to understand
how it explains the fact that the zeros and factorizations are present for these three colored
theories. Indeed it turns out that this is the **only** kinematic shift that one can do on the
_Xi,j_ _[′]_ _[s]_ [that] [preserves] [the] _[c][′]_ _i,j_ _[s]_ [!] [We] [will] [prove] [this] [shortly] [but] [let] [us] [start] [by] [understanding]
why this is the case and how it implies the generalization of the zeros/factorizations for any
value of the deformation.
From equation (2.4), establishing the relation between the non-planar variables to the
planar ones, we can easily see that by shifting _Xe,e_ _→_ _Xe,e_ + _δ_ and _Xo,o_ _→_ _Xo,o_ _−_ _δ_,
while keeping _Xo,e_ unchanged, the shift exactly cancels in (2.4) thus preserving all _ci,j_ ’s.
This means that independent of the underlying triangulation we choose, _T_, to parametrize
_ui,j_ [ _yT_ ], the _c_ ’s appearing in the exponents of the _F_ -polynomials in the string integral
remain unchanged. Therefore the result of this shift can only change the exponents of _yi_ .
Note that our derivation in sections 6.1 and 6.2 of the zeros/factorizations of the stringy
integral is **independent** of these exponents of _yi_ . Therefore, the fact that the _c_ _[′]_ _i,j_ _[s]_ [remain]
unchanged under this shift implies that the zeros and factorizations are also true for _In_ _[δ]_ [!]
We stress that the existence of zeros and factorizations for both field theory and string
theory amplitudes is made obvious from the associahedron and the stringy _δ_ eformation we
describe in this section. We expect that with these statements in hand, it should be possible
to prove them from different starting points as well. For instance we have understood how
the zeros and factorization of Tr _ϕ_ [3], NLSM, and YMS field-theory amplitudes can be proven
starting from their CHY formulas [11–13], though the formalism doesn’t make these facts
obvious. We find it more natural and satisfying that these hidden properties of both string
and field-theory amplitudes, together with the startling unity of all these colored theories,
are manifested via stringy _δ_ eformation.


33


**Figure** **11** : The _c_ -preserving shift for 6-point stringy integral.


**7.1** **Uniqueness** **of** **kinematical** **shift**


The striking fact is not only that this shift exactly preserves the non-planar variables, but
it actually is the **unique** shift that does so.
To prove this, we start by noticing that in order to preserve all _ci,j_ of a ray-like triangulation, it suffices to specify shifts of the planar variables _Xa,b_ in the triangulation. This
is because we can solve for all the remaining _X_ variables in terms of the _ci,j_ ’s and _Xa,b_ .
While any shifts of _n−_ 3 initial _Xa,b_ preserve _ci,j_ appearing for this triangulation, asking
for the shift to preserve **all** the _ci,j_, so that we have **all** the zeros and factorizations is
much more constraining. Let us choose a specific triangulation, say the ray-like one with
(1 _,_ 3) _,_ (1 _,_ 4) _, · · ·_ _,_ (1 _, n−_ 1), and specify the initial shifts as


_X_ 1 _,i_ _→_ _X_ 1 _,i_ + _δ_ 1 _,i,_ for _i_ = 3 _,_ 4 _, · · ·_ _, n−_ 1 _._ (7.6)


In order to preserve _ci,j_ of this triangulation (with 1 _≤_ _i_ _<_ _j_ _<_ _n_ ) we must shift _Xa,b_
according to the solution of (2.4); in particular, we find the following shifts for _Xi,n_ (the
variables in the opposite edge of the triangular region):


_Xi,n_ _→_ _Xi,n −_ _δ_ 1 _,i_ +1 _,_ for _i_ = 2 _,_ 3 _, · · ·_ _, n−_ 2 _._ (7.7)


In other words, _X_ 2 _,n_ must be shifted by the same amount but in the opposite direction
as _X_ 1 _,_ 3, same for _X_ 3 _,n_ and _X_ 1 _,_ 4, and so on. Now how can we preserve the remaining _ci,n_ for
_i_ = 2 _,_ 3 _, · · ·_ _, n−_ 2? Note _c_ 2 _,n_ = _X_ 2 _,n_ + _X_ 1 _,_ 3 _−_ _X_ 3 _,n_ and the shifts of _X_ 2 _,n_ and _X_ 1 _,_ 3 cancel on
the RHS, thus to preserve _c_ 2 _,n_ we must have the shift of _X_ 3 _,n_ vanishes, _δ_ 1 _,_ 4 = 0. To preserve
_c_ 3 _,n_ = _X_ 3 _,n_ + _X_ 1 _,_ 4 _−_ _X_ 1 _,_ 3 _−_ _X_ 4 _,n_, we must have _δ_ 1 _,_ 5 = _δ_ 1 _,_ 3. Similarly we find _δ_ 1 _,_ 6 = 0,


34


_δ_ 1 _,_ 7 = _δ_ 1 _,_ 5 and so on. Thus the only _c_ -preserving shifts correspond to _δ_ 1 _,e_ = 0 and all _δ_ 1 _,o_
equal. However, for odd _n_ we further conclude that _δ_ 1 _,o_ = 0 as well, and only for even _n_ we
can have non-vanishing and equal _δ_ 1 _,o_, which we call _−δ_ . This leads to _δXe,e_ = _−δXo,o_ = _δ_,
and _δXo,e_ = 0, which are the only possible _c_ -preserving shifts!


**7.2** **Realization** **of** **the** **shift** **on** **momenta**


We have expressed our shift directly in terms of its action on our basis of invariants _Xi,j_,
but we can of course also describe it explicitly in terms of a shift on the momenta directly.
It is actually slightly more convenient to describe the shift in terms of the vertices _x_ _[µ]_ _i_ [of]
the momentum polygon, from which the shift on the momenta _p_ _[µ]_ _i_ [=] [(] _[x][µ]_ _i_ +1 _[−]_ _[x]_ _i_ _[µ]_ [)] [can] [be]
inferred. To realize the shift for an 2 _n_ particle process, we imagine adding 2 _n_ dimensions
of spacetime, orthogonal to the ones the original momentum polygon lives in, which are
grouped into _n_ pairs of different timelike and spacelike directions _t_ _[µ]_ _a_ _[, s][µ]_ _a_ [for] _[a]_ [=] [1] _[,][ · · ·]_ _[, n]_ [.]
So we have _sa · xj_ = _ta · xj_ = 0 for all _a, j_, and also _ta · tb,_ _ta · sb,_ _sa · tb,_ _sa · sb_ = 0 for _a ̸_ = _b_ .
Finally we normalize _t_ [2] _a_ [=] 2 _[δ]_ _[, s]_ _a_ [2] [=] _[ −]_ 2 _[δ]_ [.] [Then] [we] [can] [define] [the] [shift]



2 _[δ]_ _[, s]_ _a_ [2] [=] _[ −]_ 2 _[δ]_




_[δ]_ [Then] [we] [can] [define] [the] [shift]

2 [.]



sending



_x_ _[µ]_ 2 _k_ _[→]_ _[x]_ 2 _[µ]_ _k_ [+] _[ t]_ _k_ _[µ][,]_ _[x][µ]_ 2 _k_ +1 _[→]_ _[x]_ 2 _[µ]_ _k_ +1 [+] _[ s]_ _k_ _[µ][,]_ (7.8)


_X_ 2 _k,_ 2 _l_ = ( _x_ 2 _k −_ _x_ 2 _l_ ) [2] _→_ ( _x_ 2 _k −_ _x_ 2 _l_ + _tk −_ _tl_ ) [2] = _X_ 2 _k,_ 2 _l_ + _δ,_



_X_ 2 _k_ +1 _,_ 2 _l_ +1 = ( _x_ 2 _k_ +1 _−_ _x_ 2 _l_ +1) [2] _→_ ( _x_ 2 _k_ +1 _−_ _x_ 2 _l_ +1 + _sk −_ _sl_ ) [2] = _X_ 2 _k_ +1 _,_ 2 _l_ +1 _−_ _δ,_

_X_ 2 _k,_ 2 _l_ +1 = ( _x_ 2 _k −_ _x_ 2 _l_ +1) [2] _→_ ( _x_ 2 _k −_ _x_ 2 _l_ +1 + _tk −_ _sl_ ) [2] = _X_ 2 _k,_ 2 _l_ +1 _,_ (7.9)


which is just our kinematic shift.


**7.3** **4-point** **amplitudes**


In order to gain more intuition for the physics of our shifts, it is useful to study the shifted
four-particle amplitude in some detail. Recall that with our shifts we have


_I_ 4 _[δ]_ [=] [Γ[] _[α][′]_ [(] _[X]_ [1] _[,]_ [3] _[ −]_ _[δ]_ [)]Γ[] _[α][′]_ [(] _[X]_ [2] _[,]_ [4][ +] _[ δ]_ [)]] _._ (7.10)

Γ[ _α_ _[′]_ ( _X_ 1 _,_ 3 + _X_ 2 _,_ 4)]


Of course for _δ_ = 0, the low-energy amplitude is 1 1 [the] [massless] [Tr][(] _[ϕ]_ [3][)]
_α_ _[′]_ _X_ 1 _,_ 3 [+] _α_ _[′]_ _X_ 2 _,_ 4 [of]
theory. We can get an idea of the massive spectrum of states in the UV completion by
looking at the residue on the first massive pole at e.g. _α_ _[′]_ _X_ 1 _,_ 3 = _−_ 1. This residue is
(1 _−_ _α_ _[′]_ _X_ 2 _,_ 4), and using the familiar translation from _s, t_ variables to center-of-mass energies
and angles, _t_ = (cos _θ −_ 1) _s/_ 2, the residue at _α_ _[′]_ _X_ 1 _,_ 3 = _α_ _[′]_ _s_ = _−_ 1 becomes [(cos] 2 _[θ]_ [+1)] . The

angular dependence on cos _θ_ allows to read off that at this mass level we have the exchange
of a particle of spin 0 and one of spin 1. Let us now turn on _δ_ and see what happens as
we vary _α_ _[′]_ _δ_ from very small values near 0, to intermediate fractional values, and then near
_α_ _[′]_ _δ_ _→_ 1 (see figure 12). At very low-energies for _α_ _[′]_ _X_ 1 _,_ 3 _, α_ _[′]_ _X_ 2 _,_ 4 _≪_ 1, we have


_I_ 4 _[δ]_ _[→]_ _[α][′]_ [ �] Γ[ _−α_ _[′]_ _δ_ ]Γ[+ _α_ _[′]_ _δ_ ]� _×_ ( _X_ 1 _,_ 3 + _X_ 2 _,_ 4) _,_ (7.11)


35


**Figure** **12** : UV completion for different values of _α_ _[′]_ _δ_ .



giving us the amplitude for NLSM with _λ_ [2] = _α_ _[′]_ Γ[ _−α_ _[′]_ _δ_ ]Γ[+ _α_ _[′]_ _δ_ ]. We can again get an idea
of the spectrum of massive states, by looking at the first massive level; this is actually a
shifted version of the massless pole we had at _δ_ = 0; the residue at _X_ 1 _,_ 3 = _δ_ is simply
1! Thus we learn that at the first massive level where _X_ 1 _,_ 3 = _δ_, we are exchanging a
massive spin-0 particle. If _α_ _[′]_ _δ_ _≪_ 1, there is a separation of scales between this state and
the rest of the string states. At very low energies where _X_ _≪_ _δ_, we have the amplitude for
pions. At _X_ 1 _,_ 3 = _δ_ we encounter an extra massive spin-0 particle. The amplitudes in the
intermediate region _δ_ _≪_ _X_ 1 _,_ 3 _, X_ 2 _,_ 4 _≪_ _α_ [1] _[′]_ [is] [simply] [that] [of] [the] [Tr][(] _[ϕ]_ [3][)] [theory,] [which] [softens]

the UV power-law growth of the low-energy NLSM amplitudes into falling 1 _/X_ behavior.
And ultimately for energies above the string scale _α_ _[′]_ _X_ 1 _,_ 3 _, α_ _[′]_ _X_ 2 _,_ 4 _≫_ 1 we see the tower of
stringy excitations and the softest UV behavior characteristic of string theory.
When _α_ _[′]_ _δ_ is no longer small, but say near _∼_ 1 _/_ 2, there is no separation between the
first massive scalar and the rest of the string states, and so we get a purely stringy UV
completion with no intermediate Tr( _ϕ_ [3] ) regime.
The situation becomes more interesting as we approach _α_ _[′]_ _δ_ _→_ 1. Let us put _α_ _[′]_ _δ_ = 1 _−ϵ_ .
Then we have a light state _X_ 1 _,_ 3 = _−ϵ_ . The residue on this pole is Γ[ _α_ _[′]_ _X_ 2 _,_ 4 +1 _−_ _ϵ_ ] _/_ Γ[ _X_ 2 _,_ 4 _−_
_ϵ_ ] = ( _X_ 2 _,_ 4 _−_ _ϵ_ ). Again translating to energies and angles, we see that at this small mass we
are exchanging both a spin-0 and a spin-1 particle. Thus, for _α_ _[′]_ _δ_ very close to 1, we see
pion amplitude at low energies, but encounter, instead of a massive spin-0 particle as we
did for _α_ _[′]_ _δ_ close to 0, a massive spin-1 particle (and a scalar), once again softening the UV
behavior of the low-energy theory. This is familiar physics from real-world QCD, where the
_ρ_ meson plays the dominant role in the unitarization of pion scattering.
This makes it clear what we must expect at _α_ _[′]_ _δ_ _→_ 1. The light massive spin-1 particle
becomes massless in this limit, and the only consistent theory we could be describing is
Yang-Mills theory! Of course we have an amplitude for external scalars, and so we are



36


describing colored scalars coupled to gluons. Exactly at _α_ _[′]_ _δ_ = 1, the amplitude is

_I_ 4 _[δ]_ [=1] = [Γ[] _[α][′]_ Γ[ _[X]_ [1] _α_ _[,]_ [3] _[′]_ ( _[ −]_ _X_ 1 [1]Γ[] _,_ 3 + _[α]_ _X_ _[′][X]_ 2 _,_ [2] 4 _[,]_ [4] )] [ + 1]] _._ (7.12)


Note that these shifts keep a massless gluon pole at _X_ 1 _,_ 3 = 0, but remove it at _X_ 2 _,_ 4 = 0.
Thus we must interpret this amplitude as that of two **different** colored scalars _A, B_, in the
configuration 1 _[A]_ 2 _[A]_ 3 _[B]_ 4 _[B]_, so that the _X_ 1 _,_ 3 channel gluon exchange is allowed by the _X_ 2 _,_ 4
channel exchange is forbidden. This interpretation is easily confirmed by looking at the
low-energy limit, where the amplitude becomes _X_ 2 _,_ 4 _/X_ 1 _,_ 3 + 1, precisely corresponding to
_X_ 1 _,_ 3 channel gluon exchange for 1 _[A]_ 2 _[A]_ 3 _[B]_ 4 _[B]_ scattering plus the four-vertex contact diagram.
As we will now see, this story generalizes for all shifted 2 _n_ particle amplitudes. For
_δ_ = 0 we have the amplitudes for Tr( _ϕ_ [3] ) theory at low energies. Instead for general
fractional _δ_, the low-energy amplitudes are those of NLSM. When _α_ _[′]_ _δ_ is small, the NLSM
amplitudes are first UV softened into those of Tr( _ϕ_ [3] ) at energies above _∼_ _δ_, before being
further UV softened into string amplitudes above the scale 1 _/α_ _[′]_ . For _α_ _[′]_ _δ_ of order one, the
UV softening of the low-energy NLSM amplitudes is purely stringy. But as _α_ _[′]_ _δ_ increases
further and approaches one, colored massive spin-1 particles descend from the string states,
and at _α_ _[′]_ _δ_ = 1, we are describing the amplitudes for pairs of _n_ distinct colored scalars,
ordered as _M_ 1 _,···,n_ (1 _[A]_ [1] 2 _[A]_ [1] 3 _[A]_ [2] 4 _[A]_ [2] _· · ·_ (2 _n −_ 1) _[A][n]_ (2 _n_ ) _[A][n]_ ). As we will discuss further below
and explore at much greater length in [19], these amplitudes give us, inter-alia, direct
access to _n_ -gluon amplitudes, by factorizing 2 _n_ -scalar amplitudes on gluon poles where
( _p_ 2 _k−_ 1 + _p_ 2 _k_ ) [2] _→_ 0.


**7.4** _α_ _[′]_ _δ_ _∈_ (0 _,_ 1) **and** **the** **Non-linear** **Sigma** **Model**


For _α_ _[′]_ _δ_ non-integer we claim that




   _I_ 2 _[δ]_ _n_ [=]

R [2] _[n][−]_ [3]

_>_ 0



2 _n−_ 3



_I_ =1



d _yI_

_yI_




- 
_ue,e_ _[α][′]_ [(] _[X][e,e]_ [+] _[δ]_ [)] _×_

( _e,e_ ) ( _o,o_





_uo,e_ _[α][′][X][o,e]_ _,_ (7.13)

( _o,e_ )








- 
_uo,o_ _[α][′]_ [(] _[X][o,o][−][δ]_ [)] _×_

( _o,o_ ) ( _o,e_



yields NLSM tree-level amplitudes at low energies, _i.e._ in the _α_ _[′]_ _→_ 0 limit, thus explaining
all the mysterious zeros and factorizations observed for these amplitudes.
To show that this is the case let us understand the consequences of this shift. For
_δ_ = 0, the fact that the string amplitude has poles associated with massless resonances for
_Xi,j_ _→_ 0, is because _u_ _[α]_ _i,j_ _[′][X][i,j]_ _→_ 1, and thus the integral develops a singularity in one of
the integration boundaries. This is particularly easy to see for the _Xi,j_ _∈T_ : in this case,
the integral becomes singular for _Xi,j_ = 0 because it diverges near _yi,j_ = 0 as we see in
(6.7). For _δ_ = 0, we lose the poles corresponding to _Xe,e, Xo,o_ =0, since the divergences of
the integral are still regulated by _δ_ . Note that poles corresponding to _Xe,e, Xo,o_ chords are
associated with propagators enclosing **odd-point** interactions. Therefore, at leading order
in the low energy expansion, we only have poles when _Xo,e_ = 0, which are precisely the
propagators appearing in diagrams built only out of even-point interactions. This is exactly
the pole structure that we expect for NLSM amplitudes, and thus the first hint that we are
going in the correct direction.


37


Now provided we have the correct pole structure, _i.e._ we don’t have any poles for
_Xe,e, Xo,o_ =0, then the fact that the amplitude vanishes in the skinny-rectangle type zero
(which it does because the undeformed amplitude does) implies that this amplitude has
vanishing soft limit, _i.e._ it has the **Adler** **zero** . This is exactly what we concluded before
just for the case of field theory NLSM, that our zero **implies** the Adler zero for these
amplitudes.
Finally, just from _u_ -equations, we have that on the _Xo,e_ _→_ 0, the amplitude (7.13)
factorizes into the product of the respective lower-point amplitudes. At tree-level, the Adler
zero together with factorization ensure that the low energy limit corresponds to NLSM
amplitude [24, 34]. Alternatively, we could make the same conclusion via the uniqueness
theorem [35, 36] even without the knowledge of factorization.
For this note, this is enough since we are interested in understanding the zeros and
factorizations of tree-level amplitudes. However, as it is explained in [18] this shift also
allows us to obtain NLSM loop-level amplitudes.
This way we have proved that (7.13) defines a new completion of the NLSM amplitudes.
Different stringy completions of the NLSM have been proposed [32, 37], but none make the
zeros and factorizations manifest. In both cases, the stringy completion is **manifestly**
cyclic, as opposed to our stringy completion, which is manifestly not cyclically symmetric
but in which the leading order at low energies restores the cyclic symmetry expected for
NLSM amplitudes.
We thus see that the UV completion provided by this stringy formulation is not a
familiar one. To understand this better let us look directly at what happens in the fieldtheory limit.


**7.4.1** **NLSM** **from** **field** **theory** **Tr** ( _ϕ_ [3] )


To extract the field theory limit, let us assume that we also have _α_ _[′]_ _δ_ _≪_ 1. Therefore we
obtain:




   _I_ 2 _[δ]_ _n_ [=]

R [2] _[n][−]_ [3]

_>_ 0



2 _n−_ 3



_I_ =1



d _yI_

_yI_




- 
_u_ _[α]_ _e,e_ _[′]_ [(] _[X][e,e]_ [+] _[δ]_ [)] _×_

( _e,e_ ) ( _o,o_



(7.14)





_uo,e_ _[α][′][X][o,e]_

( _o,e_ )








- 
_uo,o_ _[α][′]_ [(] _[X][o,o][−][δ]_ [)] _×_

( _o,o_ ) ( _o,e_



_→A_ 2 [Tr] _n_ [(] _[ϕ]_ [3][)] ( _Xe,e_ _→_ _Xe,e_ + _δ, Xo,o_ _→_ _Xo,o −_ _δ_ ) _,_


where _A_ 2 [Tr] _n_ [(] _[ϕ]_ [3][)] stands for the field theory amplitude in Tr( _ϕ_ [3] ) theory. Finally to get the real
low energy behavior we need to further expand in _X_ _≪_ _δ_ or, equivalently, _δ_ _→∞_ . From
our previous argument, we have that the leading non-vanishing order in this expansion is
the NLSM amplitude.
This means that we can get the NLSM amplitude directly from the Tr( _ϕ_ [3] ) field theory
amplitude:


_A_ [NLSM] 2 _n_ = lim 2 _n_ ( _Xe,e_ _→_ _Xe,e_ + _δ, Xo,o_ _→_ _Xo,o −_ _δ_ ) _,_ (7.15)
_δ→∞_ _[δ]_ [2] _[n][−]_ [2] _[A]_ [Tr][(] _[ϕ]_ [3][)]


where the prefactor _δ_ [2] _[n][−]_ [2] is there ensure the correct units.


38


So we have that the UV completion provided by this stringy integral is one in which the
NLSM is given as the low energy limit of a theory of colored massive scalars. These scalars
can be regular scalars with mass [2] = _δ_ or tachyons with mass [2] = _−δ_ . This is certainly an
unfamiliar UV completion of the NLSM. Apart from the unusual presence of positive and
negative mass [2] particles with precisely equal magnitudes, the UV amplitude is not cyclically
invariant, while the NLSM amplitudes certainly are. Indeed the full UV amplitude does
have a cyclic symmetry under _i →_ _i_ +1 but only if we also flip the sign _δ_ _→−δ_ . This implies
that in the 1 _/δ_ expansion, all terms with even powers of _δ_ will be cyclically invariant while
those with odd powers of _δ_ will pick up a minus sign under cyclic shift. Quite beautifully,
for the shifted 2 _n_ particle amplitude, after the naively leading powers of 1 _/δ_ all cancel, we
are left with an amplitude that begins with an even power 1 _/δ_ [2(] _[n][−]_ [1)] and hence is cyclically
invariant as desired. A simple Lagrangian that generates the shifted Tr( _ϕ_ [3] ) amplitudes and
explains the non-cyclic nature of the UV completion will be presented in [18].


**4-point** Let us now look at the 4-point amplitude. Starting from the Tr( _ϕ_ [3] ) and performing the shift we get:


1 1
_A_ [Tr] 4 [(] _[ϕ]_ [3][)] ( _X_ 1 _,_ 3 _→_ _X_ 1 _,_ 3 _−_ _δ, X_ 2 _,_ 4 _→_ _X_ 2 _,_ 4 + _δ_ ) = _X_ 1 _,_ 3 _−_ _δ_ [+] _X_ 2 _,_ 4 + _δ_ _[,]_ (7.16)


now expanding in _δ_ _≫_ 1 yields:



_δ→∞_
_A_ [Tr] 4 [(] _[ϕ]_ [3][)] ( _X_ 1 _,_ 3 _−_ _δ, X_ 2 _,_ 4 + _δ_ ) _−−−→_ [1]




[(] _[X]_ [1] _[,]_ [3][ +] _[ X]_ [2] _[,]_ [4][)]
_δ_ [2]

  - ��  _A_ [NLSM] 4




[1]

_δ_ [(1] _[ −]_ [1)] _[ −]_ _δ_ [1]



+ _O_ (1 _/δ_ [3] ) _,_ (7.17)



where indeed the first order cancels and the leading non-vanishing order gives the pion
amplitude. Already in this small 4-point problem, we can appreciate how important it is
that the mass of _Xe,e_ is minus that of the mass of _Xo,o_ . If this was not the case the leading
order would be non-vanishing and we would **not** get the NLSM, instead, it would be closer
to _ϕ_ [4] theory.


**6-point** At 6-point it is convenient to start by writing the Tr( _ϕ_ [3] ) amplitude in a way that
makes manifest the _X_ o,e poles, as follows:



�� 1 1
+
_X_ 4 _,_ 6 _X_ 1 _,_ 5




+ (cyclic _, i →_ _i_ + 2)



_A_ [Tr] 6 [(] _[ϕ]_ [3][)] ( _X_ _→_ _X_ _± δ_ ) = [1]



_X_ 1 _,_ 4




- 1 1
+
_X_ 1 _,_ 3 _X_ 2 _,_ 4



(7.18)
1 1
+ + _._
_X_ 1 _,_ 3 _X_ 3 _,_ 5 _X_ 1 _,_ 5 _X_ 2 _,_ 4 _X_ 4 _,_ 6 _X_ 2 _,_ 6



39


Performing the shift on the 6-point Tr( _ϕ_ [3] ) amplitude yields:



�� 1 1
_X_ 4 _,_ 6 + _δ_ [+] _X_ 1 _,_ 5 _−_ _δ_




+ (cyclic _, i →_ _i_ + 2)



_A_ [Tr] 6 [(] _[ϕ]_ [3][)] ( _X_ _→_ _X_ _± δ_ ) = _X_ [1] 1 _,_ 4




- 1 1
_X_ 1 _,_ 3 _−_ _δ_ [+] _X_ 2 _,_ 4 + _δ_



1 1
+
( _X_ 1 _,_ 3 _−_ _δ_ )( _X_ 3 _,_ 5 _−_ _δ_ )( _X_ 1 _,_ 5 _−_ _δ_ ) [+] ( _X_ 2 _,_ 4 + _δ_ )( _X_ 4 _,_ 6 + _δ_ )( _X_ 2 _,_ 6 + _δ_ ) _[,]_

(7.19)
gathering and expanding in _δ_ _≫_ 1 we get:



_δ→∞_
_A_ [Tr] 6 [(] _[ϕ]_ [3][)] ( _X_ _→_ _X_ _± δ_ ) _−−−→−_ _δ_ [1][4]





_−_ [(] _[X]_ [1] _[,]_ [3][ +] _[ X]_ [2] _[,]_ [4][)(] _[X]_ [1] _[,]_ [5][ +] _[ X]_ [4] _[,]_ [6][)] + (cyclic _, i →_ _i_ + 2)

_X_ 1 _,_ 4



+ _X_ 1 _,_ 3 + _X_ 3 _,_ 5 + _X_ 1 _,_ 5 + _X_ 2 _,_ 4 + _X_ 4 _,_ 6 + _X_ 2 _,_ 6) + _O_ (1 _/δ_ [5] ) _,_
(7.20)
which we can identify with the 6-point NLSM amplitude, _A_ [NLSM] 6 .


**7.4.2** **Factorizations** **near** **zeros**


The identifications of NLSM amplitudes with those of Tr( _ϕ_ [3] ) theory with the simple shifted
kinematics _Xee_ _→_ _Xee_ + _δ, Xoo_ _→_ _Xoo_ _−_ _δ, Xeo_ _→_ _Xeo_ allows to also very simply understand the pattern of factorization near zeroes we had observed experimentally in section 4.
Precisely because these shifts are _c_ -preserving, at the level of the Tr( _ϕ_ [3] ) amplitudes, the
factorization patterns are precisely the same before and after the shifts.
To begin with, we consider the near-zero factorizations for 2 _n_ particle amplitudes into
“even points _×_ even points”, even when taking into account the necessary kinematic shifts,
we still end up with the same _δ_ shifts for the _Xee, Xoo, Xeo_ for each of the lower point amplitudes. This proves that the “even _×_ even” near-zero factorizations for NLSM amplitudes
simply factor into the product of NLSM amplitudes, just as we saw in section 4.
The case of near-zero factorization to “odd _×_ odd” amplitudes is somewhat more interesting, since as we observed experimentally in section 4, we encounter the mixed amplitudes
for cubic scalars _ϕ_ and pions _π_ . We can now easily understand the reason for this, as well
as the interesting rule for “who is a _ϕ_ and who is a “ _π_ ” we delineated in section 4. As an
example let us consider the _n_ = 6 factorization associated the upper skinny rectangle in
figure 9, where we turn on _c_ 2. Let us focus on the 5-point factor, with the appropriate
kinematic replacements. For clarity, we will denote the kinematics of the _n_ = 5 problem by _Y_ variables _Yij_ . So all the _Yij_ = _Xij_ except of course _Y_ 15 = 0, and we have the
kinematic replacement _Y_ 25 = _X_ 26. We can now perform the _δ_ shift on all the variables:
_Y_ 1 _,_ 3 _→_ _Y_ 1 _,_ 3 _−δ, Y_ 1 _,_ 4 _→_ _Y_ 1 _,_ 4 _, Y_ 2 _,_ 4 _→_ _Y_ 2 _,_ 4 + _δ, Y_ 2 _,_ 5 = _X_ 2 _,_ 6 _→_ _X_ 2 _,_ 6 + _δ_ = _Y_ 2 _,_ 5 + _δ, Y_ 3 _,_ 5 _→_ _Y_ 3 _,_ 5 _−δ_ .
We denote the effect of this on the 5-point mesh by attaching a “+/-” to each variable as
denoted in figure 16 presented at the end of the paper.
We can now see that the shifts in the _n_ = 5 mesh do _not_ preserve all the _c_ ’s. Nonetheless,
some of the _c_ ’s are preserved, as represented in the shaded meshes in the figure. This
picture enables us to see that this _n_ = 5 factor does _not_ have all of our zeros; not all
the skinny rectangles remain unshifted. However, some of the zeros do survive: the ones
naturally associated with soft limits for particles 1 _,_ 3 _,_ 5 are still clearly present in the picture.
Now for particles 1 _,_ 3, we can see that the collinear poles ( _p_ 1 + _p_ 2) [2] = _Y_ 1 _,_ 3 _→_ _Y_ 1 _,_ 3 _−_ _δ_,


40


( _p_ 5 + _p_ 1) [2] = _Y_ 2 _,_ 5 _→_ _Y_ 2 _,_ 5 + _δ_ are shifted, so these massless poles are absent, and hence
the skinny rectangle zero implied an Adler zero when particle 1 becomes soft. The same
holds for particle 3. However, for particle 5, we have that collinear pole ( _p_ 4 + _p_ 5) [2] = _Y_ 1 _,_ 4
is unshifted, and hence the skinny rectangle zero does not imply a soft zero for particle
5. It is easy to see that factorization of the Tr( _ϕ_ [3] ) amplitude after the shifts implies that
the remaining particles must be interpreted as scalars with a Tr( _ϕ_ [3] ) coupling. So we have
learned that the 5-pt factor in the near zero factorization associated with turning on _c_ 2 gives
us a mixed amplitude _A_ [NLSM+] _[ϕ]_ [3] ( _π, ϕ, π, ϕ, ϕ_ ) [26]. This argument extends to the general
pattern of “odd _×_ odd” factorizations of NLSM amplitudes explained in section 4.


**7.5** _α_ _[′]_ _δ_ = 1 **and** **scaffolded** **gluons**


Now let us explore what happens when the deformation becomes one in string units, _i.e._
_α_ _[′]_ _δ_ = 1. Then the stringy integral becomes:




   _I_ 2 _[δ]_ _n_ [=]

R [2] _[n][−]_ [3]

_>_ 0



2 _n−_ 3



_I_ =1



d _yI_

_yI_





_ua,b_ _[α][′][X][a,b]_
( _a,b_ )




( _e,e_ ) _[u][e,e]_
_,_ (7.21)

( _o,o_ ) _[u][o,o]_



as explained in 7.3, at low energies, we expect to get a theory of colored scalars and gluons,
just like that given by Lagrangian (7.5).
At tree-level, we can see that (7.21) is what we get in the bosonic string amplitude,
describing the scattering of 2 _n_ gluons, by choosing a particular kinematic configuration.
This connection will make clear the origin of the scalars.


**7.5.1** **Bosonic** **string** **connection**


The open bosonic string amplitude for 2 _n_ gauge bosons with polarizations _ϵi_ is given by:



_α_ _[′]_ _ϵi · pj_

_zi,j_




[�] 2 _[ϵ][i][ ·][ ϵ][j]_

_i_ = _j_ _zi,j_ [2]







������multi-linear in _ϵi_




        - d [2] _[n]_ _zi_
_A_ [tree] _n_ (1 _,_ 2 _, . . .,_ 2 _n_ ) =
SL(2,R)







 [�] _zi,j_ [2] _[α][′][p][i][·][p][j]_

_i<j_










_√_






 exp



 [�]




_−_
_zi,j_ [2]



_,_



(7.22)
where _zi,j_ = _zi_ _−_ _zj_ are the usual worldsheet coordinates ( _c.f._ [38]). Let us now assume
that the space is sufficiently high-dimensional, with _D_ [˜] dimensions, so that we can achieve
the following kinematical configuration:



_pi · ϵj_ = 0 _,_ _∀_ ( _i, j_ ) _∈_ (1 _, ...,_ 2 _n_ ) _,_



_ϵi · ϵj_ =




1 if ( _i, j_ ) _∈{_ (1 _,_ 2); (3 _,_ 4); (5 _,_ 6); _..._ ; (2 _n −_ 1 _,_ 2 _n_ ) _},_


0 otherwise _._



(7.23)



This kinematic configuration can be easily achieved by considering the momentum to
live in the first _D_ dimensions (the ones corresponding to the usual dimensionality of space),
and the polarizations to live in the extra dimensions. With this kinematical choice, all
the polarizations are fixed, and the remaining degrees of freedom are the 2 _n D_ -dimensional
momenta – exactly that of a 2 _n_ -scalar problem. The bosonic string integral (7.22) simplifies
enormously and we get the following single term:


41


**Figure** **13** : Two scalar - one gluon interaction



(7.23) kinematics            - d [2] _[n]_ _zi_
_A_ 2 _n_ (1 _,_ 2 _, ...,_ 2 _n_ ) _−−−−−−−−−−→_
SL(2,R)




- 1

_i<j_ _zi,j_ [2] _[α][′][p][i][·][p][j]_ _z_ 1 [2] _,_ 2 _[z]_ 3 [2] _,_ 4 _[z]_ 5 [2] _,_ 6 _[...z]_ 2 [2] _n−_ 1 _,_ 2 _n_




 - d [2] _[n]_ _zi_ 1
=
SL(2,R) _z_ 1 _,_ 2 _z_ 2 _,_ 3 _z_ 3 _,_ 4 _. . . z_ 2 _n,_ 1





_zi,j_ [2] _[α][′][p][i][·][p][j]_
_i<j_



_z_ 2 _,_ 3 _z_ 4 _,_ 5 _z_ 6 _,_ 7 _. . . z_ 2 _n,_ 1 (7.24)
_z_ 1 _,_ 2 _z_ 3 _,_ 4 _z_ 5 _,_ 6 _. . . z_ 2 _n−_ 1 _,_ 2 _n_




          - ��           Stringy Tr( _ϕ_ [3] )


Now the _u_ -variables are defined in terms of the worldsheet coordinates, as the following
SL(2 _,_ R)-invariant cross-ratios:
_ui,j_ = _[z][i,j][−]_ [1] _[ z][i][−]_ [1] _[,j]_ _._ (7.25)

_zi,j zi−_ 1 _,j−_ 1


Using this definition, one can see that the extra ratio in the integrand is exactly equal
��  to ( _e,e_ ) _[u][e,e][/]_ [ �] ( _o,o_ ) _[u][o,o]_, giving us back (7.21).
Therefore, we now understand that the scalars scattering in (7.21) are secretly gluons in
higher dimensions. Moreover, we see that they only interact with their immediate neighbors,
since only _ϵ_ 2 _i_ _·ϵ_ 2 _i−_ 1 are non-zero – which can be interpreted as there being _n_ different species
of such scalars that do not mix. Finally, the original cubic gluon interaction gives rise to a
cubic interaction between a pair of scalars, (2 _i,_ 2 _i −_ 1), and a gluon with the corresponding
Feynman rule (see figure 13).
Therefore, starting from the 2 _n_ -scalar scattering, to access the _n_ -point gluon amplitude,
we need to take _n_ residues, that put the gluons on-shell, _i.e._ take residues corresponding to
_X_ 1 _,_ 3 = _X_ 3 _,_ 5 = _· · ·_ = _X_ 1 _,_ 2 _n−_ 1 = 0. So from this perspective, we think of each gluon in the
scattering process as coming from a pair of scalars - the gluons are scaffolded by scalars.
This allows us to talk about spin-1 particles in a purely scalar way, which ultimately allows
the connection to the simple theory of colored scalars that we started with. See figure 14 for
the case where, starting with a 10-point scalar, we can access the 5-point gluon amplitude,
after taking the scaffolding residue. Such 2 _n_ -scalar bosonic string amplitudes as well as
YMS amplitudes [13] in the field-theory limit, were studied in [39, 40].
As we explain in [19], the momentum and polarization of the gluons can be determined
in terms of the momentum of the external scalars:

         _qi_ _[µ]_ = ( _p_ 2 _i_ + _p_ 2 _i−_ 1) _[µ]_ _[,]_ (7.26)

_ϵ_ _[µ]_ _i_ _∝_ ( _p_ 2 _i −_ _p_ 2 _i−_ 1) _[µ]_


42


**Figure** **14** : From 10-point scalar amplitude to 5-point gluon amplitude after taking the
scaffolding residue.


where the momentum of the gluon can be read off directly by momentum conservation and
the polarization through the vertex Feynman rule in figure 13. In this scalar language,
gauge invariance and linearity in the polarizations have their own avatar that is explained
in detail in [19].


**7.5.2** **Scaffolding** **residue**


In order to extract the gluon amplitude we need to take the residues _X_ 2 _i_ +1 _,_ 2 _i−_ 1 = 0. To
easily access this residue it is useful to pick a positive parametrization _{yT }_ corresponding
to a triangulation **including** chords _X_ 2 _i_ +1 _,_ 2 _i−_ 1. This way the singularity associated with
_X_ 2 _i_ +1 _,_ 2 _i−_ 1 = 0 comes from the divergence of the integral near _y_ 2 _i_ +1 _,_ 2 _i−_ 1 = 0, and the residue
of the amplitude turns into the residue of the integrand at _y_ 2 _i_ +1 _,_ 2 _i−_ 1 = 0.

��                   As it is explained in [19], for such a triangulation, the factor ( _e,e_ ) _[u][e,e][/]_ [ �] ( _o,o_ ) _[u][o,o]_

simplifies to:

     ( _e,e_ ) _[u][e,e]_ 1 1
_−→_ _×_ _,_ (7.27)
�( _o,o_ ) _[u][o,o]_ _y_ 1 _,_ 3 _y_ 3 _,_ 5 _. . . y_ 1 _,_ 2 _n−_ 1 �( _k,m_ ) _∈T_ _[′][ y][k,m]_


where _T_ _[′]_ stands for the triangulation of the inner _n_ -gon, with vertices _{_ 1 _,_ 3 _,_ 5 _, . . .,_ 2 _n −_ 1 _}_,
corresponding to the gluon amplitude. And thus the 2 _n_ -scalar amplitude becomes:




   _I_ 2 _[δ]_ _n_ [=]

R [2] _[n][−]_ [3]

_>_ 0



_n_



_i_ =1



d _y_ 2 _i−_ 1 _,_ 2 _i_ +1

_y_ 2 [2] _i−_ 1 _,_ 2 _i_ +1






_I∈T_ _[′]_





_ua,b_ _[α][′][X][a,b]_
( _a,b_ )



d _yI_

_yI_ [2]



_,_ (7.28)




                 - ��                 Ω2 _n_


which is exactly the stringy Tr( _ϕ_ [3] ) integral where instead of a dlog form, we have d _y/y_ [2] .
So n-point gluon amplitude is then given by the low energy of:


     
              -              -              -              - �� [�]

_In_ [gluon] = Res _y_ 1 _,_ 3=0 Res _y_ 3 _,_ 5=0 _. . ._ Res _y_ 1 _,_ 2 _n−_ 1=0 (Ω2 _n_ ) _. . ._ _._ (7.29)

R _[n]_ _>_ _[−]_ 0 [3] ��� _X_ 2 _i−_ 1 _,_ 2 _i_ +1=0


43


**7.5.3** **Zeros**



The stringy 2 _n_ -scalar has all the same zeros and factorizations as stringy Tr( _ϕ_ [3] ) theory,
but in order to understand the zeros/factorizations for gluon amplitudes, we need to study
which of these survive after the scaffolding residue.
As pointed out previously, to access the scaffolding residue it is useful to pick the
underlying triangulation to contain _{X_ 2 _i−_ 1 _,_ 2 _i_ +1 _}_ . To talk about the zeros we will pick the
underlying triangulation to be as close as possible to the usual ray-like one by choosing the
triangulation of the _n_ -gon to be ray-like. Still, the fact that we have chords _{X_ 2 _i−_ 1 _,_ 2 _i_ +1 _}_
means that the _ci,j_ appearing in the stringy integral are not exactly those of the usual
triangle (see figure 18 at the end of the paper).
We are now going to study the zeros of the gluon amplitude for the case of 10 scalars _→_
5 gluons. This example is big enough to illustrate the non-trivial features and understand
how it generalizes to higher points. At 10 points, let us consider the triangulation of the
10-gon: _{X_ 1 _,_ 3 _, X_ 3 _,_ 5 _, X_ 5 _,_ 7 _, X_ 7 _,_ 9 _, X_ 1 _,_ 9 _, X_ 1 _,_ 5 _, X_ 1 _,_ 7 _}_, _i.e._ we have the scaffolding chords and a
ray-like triangulation for the inner pentagon. For this choice of triangulation, the resulting
region of the mesh is represented in figure 18 as the shaded region. We see that there are
only 3 meshes from the usual triangle that are now missing and instead are replaced by 3
meshes on the top.
In figure 18 we represent the _F_ -polynomials entering the string integral inside the mesh,
_ci,j_, corresponding to their exponents. We further mark with red dots the scaffolding poles,
_Xi,j_, that we need to take the residue on to localize on the gluon problem. The claim is
that effectively, to read off the zeros/factorizations, we should think of the gluon mesh as
being the one highlighted in red, as this is the one in which each mesh point is associated
with one of the _X_ odd _,_ odd entering the gluon amplitude. In this case, we should have a 5point mesh, so we see that each usual square in a scalar mesh gets replaced with 4 squares,
in the gluon mesh. In this new picture, to get a zero we need to see exactly the same
patterns of meshes to zero, of course, now each individual mesh gets subdivided into four
smaller meshes. Thus at 5-point, our usually expected codimension-2 zeros are mapped to
codimension 2 _×_ 4 = 8 zeros. This is exactly the codimension we obtained when we phrase
them in terms of _pi · pj, ϵi · pj, ϵj · pi, ϵi · ϵj_ . It is worth noting that this is **not** a zero of the
full 2 _n_ -scalar problem, but instead a zero only after taking the scaffolding residue to land
on the _n_ -gluon amplitude.
Looking back at figure 18, one zero would correspond to setting _ci,_ 7 = _ci,_ 8 = 0 for
_i ∈{_ 1 _, . . .,_ 4 _}_, or, in the full stringy case, to a negative integer. The reason why the answer
vanishes in this limit is because, after the scaffolding residue, it reduces to a sum of integrals
of the form:

      - _∞_



d _y_ 1 _,_ 7



0



1 _,_ 7

_y_ 1 _,_ 7 _y_ 1 _[X]_ _,_ 7 [1] _[,]_ [7][+] _[n]_ _×_ (remaining integrations) _,_ with _n ∈_ N0 _,_ (7.30)



and so, for the usual reason, we get zero from the integration in _y_ 1 _,_ 7. It is easy to understand
why this happens. Note that all the _Fi,j_ inside the zero causal diamond depend on _y_ 1 _,_ 7,
however, there are still other _F_ -polynomials, **outside** this causal diamond, depending on


44


_y_ 1 _,_ 7, such as _Fi,_ 9 for _i_ _∈{_ 1 _, . . .,_ 5 _}_ . But in all these cases _y_ 1 _,_ 7 always appears multiplied
by some _yi,j_ associated with a scaffolding variable. Therefore, after taking the scaffolding
residue, this dependence will either vanish since we are evaluating at _y_ scaff = 0, or shift
_y_ 1 _[X]_ _,_ 7 [1] _[,]_ [7][.] [In either case,] [we will have the form (][7.30][) after the scaffolding residue.] [Instead,] [the]
_F_ -polynomials that are inside the zero causal diamond are those in which the dependence
on _y_ 1 _,_ 7 is of the form: 1 + _y_ 1 _,_ 7 + _. . ._ which are unaffected by the scaffolding residue and
thus would not lead to (7.30).
Another possible zero is obtained by setting _c_ 1 _,j_ = _c_ 2 _,j_ = 0 for _j_ _∈{_ 5 _, . . .,_ 8 _}_, or, in the
full stringy case, to a negative integer. In this case, the claim is that, after the scaffolding
residue, the amplitude reduces to sums of integrals of the form of (7.30) but where _y_ 1 _,_ 7 and
_X_ 1 _,_ 7 get replaced for _y_ 1 _,_ 5 and _X_ 1 _,_ 5, and thus the zero comes from the integration in _y_ 1 _,_ 5.
As for the case in _y_ 1 _,_ 7, all _F_ -polynomials depending on _y_ 1 _,_ 5 **outside** this causal diamond
are such that _y_ 1 _,_ 5 always appears multiplied by some _y_ 2 _i−_ 1 _,_ 2 _i_ +1. Whereas, for all the _F_ polynomials inside the zero causal diamond, the dependence in _y_ 1 _,_ 5 is either of the form
1+ _y_ 1 _,_ 5 + _. . ._, or _y_ 1 _,_ 5 appears multiplying one of the remaining _y_ ’s of the inner _n_ -gon, which
in the 5-pt case is only _y_ 1 _,_ 7. The presence of these last terms would also not lead to (7.30),
and thus why these need to be inside the zero causal diamond.
We can translate the locus of zeros we have just phrased in terms of vanishing _c_ ’s in
the more familiar language of dot products between polarization vectors and momenta. For
instance consider our first set of zeros, where _ci,_ 7 = _ci,_ 8 = 0 for _i_ = 1 _, · · ·_ _,_ 4. So e.g. for _i_ =
1 _,_ 2 we have the four constraints _p_ 1 _·p_ 7 _, p_ 1 _·p_ 8 _, p_ 2 _·p_ 7 _, p_ 2 _·p_ 8 = 0. Taking linear combinations of
these relations is equivalent to the four statements ( _p_ 1 _±p_ 2) _·_ ( _p_ 7 _±p_ 8) = 0, and given the map
between polarization vectors and momenta where e.g. _qj_ = _p_ 2 _j−_ 1 + _p_ 2 _j, ϵj_ = ( _p_ 2 _j_ _−_ _p_ 2 _j−_ 1),
this turns into the statements that _q_ 1 _· q_ 4 = 0 _, q_ 1 _· ϵ_ 4 = 0 _, ϵ_ 1 _· q_ 4 = 0 _, ϵ_ 1 _· ϵ_ 4 = 0. This
generalizes in the obvious way: every “big” mesh ( _i, j_ )is divided into four “small” meshes
that are set to zero, and this is equivalent to the statements _qi·qj_ = _qi·ϵj_ = _ϵi·qj_ = _ϵi·ϵj_ = 0,
just as we observed experimentally in section 5.
For a general 2 _n_ -scalar to _n_ -gluon amplitude, by drawing the effective gluon mesh
(represented in red for the 5-point gluon problem in 18) the zero causal diamonds are
exactly those identified in the usual scalar mesh, where now a square gets replaced by a set
of 4 squares. Let us say the zero for one such causal diamond comes from the integration
in _yI_ of the internal _n_ -gon, then the claim is that all the _F_ -polynomials lying inside this
causal diamond contain all the _F_ -polynomials in which _yI_ does **not** appear multiplying one
of the scaffolding _y_ ’s.


**7.5.4** **Factorizations**


Once more, since the 2 _n_ -scalar amplitude is just a _c_ -preserving deformation of stringy
Tr( _ϕ_ [3] ), all the factorizations of the latter are also true for the former. So, to understand
which factorizations of the 2 _n_ -scalar turn into gluon factorizations, we need to study which
ones survive after the scaffolding residue. The idea is then to find the factorizations in
which the scaffolding variables appear in lower point amplitudes so that the residue is nonvanishing. There are two different such cases - either the lower point amplitudes are both
odd points or even points.


45


**Figure** **15** : Factorization of the 10-point scalars and the scaffolded 5-point gluons.


To explain the different possible factorization patterns we can find we will be studying
the 10-point scalar problem, as this example is big enough to include all the subtleties we
find for general 2 _n_ scalars.
Let us consider the even-point factorizations of the 10-point scalar amplitude. For evenpoint factorizations, as long as we ensure that all the scaffolding variables appear on the
lower problems, then we have two 2 _n_ -scalar lower point amplitudes. In addition, since for
even-point factorizations the _X_ B and _X_ T associated with the causal diamond we’re probing
are both _X_ o,e, the prefactor is the usual 4-point amplitude of Tr( _ϕ_ [3] ) theory:

_A_ _[α]_ 2 _n_ _[′][δ]_ [=1] ( _c⋆_ = 0) _→_ [Γ(] Γ( _[α]_ _α_ _[′][′][X]_ ( _X_ [B] B [)Γ(] + _[α]_ _X_ _[′][X]_ T [T] )) [)] _[× A]_ 2 _[α]_ _n_ _[′][δ]_ 1 [=1] _[,]_ [up] _× A_ 2 _[α]_ _n_ _[′][δ]_ 2 [=1] _[,]_ [down] _,_ (7.31)


where _c⋆_ is the mesh we are turning on inside the zero causal diamond, and 2 _n_ 1 and 2 _n_ 2
are the lower even-point amplitudes, such that _n_ 1 + _n_ 2 = _n_ + 1.
Let us go back to the 10-point example. In this case, there are two possible ways of
factorizing into even-point amplitudes, presented in figure 15 (center and right mesh). Let
us start by looking at the right case corresponding to a square - in this case, the lower
point amplitudes are:


_A_ 10( _c⋆_ = 0) _→_ [Γ(] _[α][′][X]_ [1] _[,]_ [6][)Γ(] _[α][′][X]_ [5] _[,]_ [10][)] 6 _× A_ [up] 6 _[.]_ (7.32)

Γ( _α_ _[′]_ ( _X_ 1 _,_ 6 + _X_ 5 _,_ 10)) _[× A]_ [down]


Let us focus on those factorizations that can also be accessed in the field theory limit for
gluons, by considering setting all the _c_ ’s inside the square to zero but for one _c⋆_ inside this


46


square to be not zero. Asking for all the scaffolding variables to appear in the appropriately
kinematic shifted lower amplitudes forces two columns of the square vanish, and therefore
the _c_ ’s we can choose to turn on are exactly those inside the gluon mesh (see figure 15,
right). Now note that while in the “up” amplitude taking the scaffolding residue in the
original problem, corresponds to taking three residues on this 6-point amplitude and thus
exactly producing a **3-point gluon** amplitude, the same is not true for the down amplitude.
In the 6-point amplitude at the bottom, we are only taking residues in two variables, _X_ 1 _,_ 3
and _X_ 3 _,_ 5, not an _X_ 1 _,_ 5. Therefore we are only producing two gluons and the remaining pair
of scalars is left untouched, and so after taking the scaffolding residue, the down amplitude
is that of **two** **gluons** **+** **two** **scalars** . Of course, if we further take a residue in _X_ 1 _,_ 5, then
we further turn the down amplitude into a 3pt gluon amplitude, and this becomes a pure
gluon factorization. The last piece we need to understand is the prefactor, which in the
field theory limit becomes:




     - 1 1
_A_ 10( _c⋆_ = 0) _→_ +
_X_ 1 _,_ 6 _X_ 5 _,_ 10




_× A_ [down] 6 _× A_ [up] 6 _[,]_ (7.33)



so taking the scaffolding residue in each term to turn the scalar amplitudes into gluon
amplitudes will not affect the prefactor. This seems then to say that in the end we are left
with an answer that has poles when _X_ o,e _→_ 0, which is incompatible with the fact that
after scaffolding residue we should be left with only poles of _X_ o,o _→_ 0, corresponding to
chords of the gluon problem. However, note that, crucially, since we are also setting the
rectangles, _ci,_ 6 = _ci,_ 9 = 0 with _i_ = 1 _, . . .,_ 4, we have that _X_ 1 _,_ 6 = _X_ 1 _,_ 7 and _X_ 5 _,_ 10 = _X_ 5 _,_ 9,
allowing us to conclude that after taking the scaffolding residue we get:



_A_ [gluons] 5 ( _c⋆_ = 0) _→_ - _X_ 11 _,_ 7 + _X_ 15 _,_ 9 - _× A_ [down,] 4 [gluons] [+] _[ϕ]_ _× A_ [up,] 3 [gluons] _,_ (7.34)



where this is now an honest factorization of the 5-point gluon amplitude.
Another possible zero causal diamond that leads to even lower point amplitudes is the
one represented in the central mesh of figure 15, where the lower point amplitudes are now
4-point and 8-point. Once more, asking for the scaffolding variables to be present in the
lower point problems, forces us to set _ci,_ 4 = _ci,_ 9 = 0 for _i_ = 1 _,_ 2, and thus the _ci,j_ we choose
to turn on lives inside the effective gluon mesh. So the factorization pattern is now in the
field theory limit:




     - 1 1
_A_ 10( _c⋆_ = 0) _→_ +
_X_ 1 _,_ 4 _X_ 3 _,_ 10




_× A_ [down] 4 _× A_ [up] 8 _[.]_ (7.35)



As opposed to the 6 _×_ 6 factorization, in this case, by taking the scaffolding residue both
the 4-point and the 8-point scalar amplitudes turn into pure gluon amplitudes, and similarly,
the prefactors change appropriately so that we get an honest 5-point gluon factorization:



_A_ [gluon] 5 ( _c⋆_ = 0) _→_ - _X_ 11 _,_ 5 + _X_ 13 _,_ 9 - _× A_ [down,] 2 [gluons] _× A_ [up,] 4 [gluons] _._ (7.36)


47


Finally, let us look at the case of an odd-point factorization. At 10-point, one example
of this is by considering the skinny rectangle (figure 15, left). In this case, the down
amplitude is a 3-point amplitude which is trivial, and the up amplitude is 9-point. Asking
for the scaffolding variables to be present in the lower point problems, forces _c_ 1 _,_ 9 = 0, and
by turning on any of the remaining _c_ ’s inside the skinny rectangle we obtain:




      - _∞_
_A_ 10( _c⋆_ = 0) _→_

0



d _y_ 1 _,_ 3

_y_ 1 [2] _,_ 3 _y_ 1 _[α]_ _,_ _[′]_ 3 _[X]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 3) _[−][α][′][c][⋆]_



_×A_ [up] 9 _[,]_ (7.37)




                 - ��                 _A_ _[α]_ 4 _[′][δ]_ [=1]


so we see that in this case the 4-point pre-factor becomes the 4-point 2 _n_ -scalar amplitude,
while for the lower point amplitude, it’s just the 9-point amplitude with the extra _u_ e,e _/u_ o,o.
So in the low energy limit, and further taking the scaffolding residue we get:


_A_ 10( _c⋆_ = 0) _−−−−→_ _[α][′][X][≪]_ [1] _[X]_ [2] _[,]_ [10] _× A_ [up] 9 [;] _A_ [gluon] 5 ( _c⋆_ = 0) _→_ _X_ 2 _,_ 10 _× A_ [up,scaffolded] 9 _._ (7.38)

_X_ 1 _,_ 3


Similarly to what we saw in the NLSM, we predict that lower odd-point amplitudes
generated in these factorizations could be some mixed amplitudes of gluons and scalars.
Regardless this is certainly another honest factorization of the gluon 5-point amplitude.
The other reason to expect the lower-point object to be a mixed theory amplitude is exactly
because the skinny rectangle is closely connected to soft limits, exactly the case in which it
was first observed the appearance of these extended theory amplitudes.


**8** **Outlook**


There are many obvious avenues for exploration following from the observations in this
paper, so instead of attempting an exhaustive accounting of all of them, we will highlight
a few that seem especially ripe for immediate development.
Already at tree-level, it is interesting to ask whether the pattern of zeros suffices to
completely determine the amplitude. For both the Tr( _ϕ_ [3] ) theory and the NLSM, there is
an obvious ansatz to make for the _n_ -particle tree amplitude. Combining all the poles into a
common denominator, we can assume that the numerator is a polynomial of correct units
for each theory, and add the further crucial assumption that this numerator is at most
linear in each _Xij_ variable; this last requirement enforces good behavior in the Regge limit.
This still leaves an enormous number of free parameters in the ansatz, but we can further
impose our hidden zeroes. Quite remarkably we have found that experimentally for Tr( _ϕ_ [3] )
amplitudes with _n_ = 5 _,_ 6 _,_ 7 points and for NLSM amplitudes with _n_ = 6 _,_ 8, imposing the
zeros in this way does fully fix the amplitude! For _n_ -point Tr( _ϕ_ [3] ) amplitude, the number
of parameters is _[n]_ [(] _[n][−]_ [3)] choose ( _n−_ 3), and there are 51 and 6700 parameters for _n_ = 6 _,_ 8

2
ansatz of NLSM amplitude respectively. Indeed imposing the simplest (cyclic class of)
“skinny rectangle” zeros is enough to fully determine the amplitude in all these cases. It
would be fascinating to prove this fact in general since this provides an entirely new way to
uniquely determine scattering amplitudes, complementary to the traditional picture relying


48


on poles and factorization. It would also be very interesting to ask how does the string
amplitude is constrained by the zeros. It has been demonstrated in [41] that by combining
the monodromy relations and the behaviour under the (generalised) Britto-Cachazo-FengWitten shifts [42], the zeros [20] of the residues of amplitudes at the kinematic poles are
suffcient to dertermine certain string amplitudes.
Our focus on the numerator structure of the amplitude dovetails with an approach to
determining the canonical form of positive geometries [43], first seen in the context of the
amplituhedron for _N_ = 4 SYM, by looking at pattern of zeros for the numerator demanded
by killing illegal singularities/enforcing the “dlog form” structure [44]. In this setting, the
variety associated with the vanishing of the numerator is called the “adjoint” of the positive
geometry. This set of zeros is more closely associated with familiar facts about singularities
of amplitudes, while our new zeros reflect something entirely different, the collapsing of the
geometry as kinematics are varied. It would be interesting to study the analog of these
“collapsing geometry” zeros for the amplituhedron, to begin with even for the simplest case
of the best-understood _m_ = 2 amplituhedron.
It is interesting to phrase the existence of our pattern of zeros in an algebraic-geometric
language. If we combine all the diagrams into a common denominator consisting of the
product of all the _Xi,j_, the amplitude is _A_ = _N_ ( _X_ ) _/D_ ( _X_ ), where the numerator _N_ ( _X_ ) is
a degree [(] _[n][−]_ [2)(] 2 _[n][−]_ [3)] polynomial in the _Xi,j_ . The complete locus of zeros of the amplitude

is then a complicated variety in the _X_ space defined by _N_ ( _X_ ) = 0. From this perspective,
the hidden zeros tell us something striking about this complicated variety: it contains a
large number of _linear_ _subspaces_ of various dimensionalities. This is certainly not a generic
property for high-dimensional varieties! It would be fascinating if this “numerator variety”
had further special properties. A speculative but intriguing thought is that this variety
should be in some sense “maximally nice”. For instance one might hope that the variety
is “determinantal”, with _N_ ( _X_ ) expressible as the determinant of a predictable matrix, in a
way that would make all our hidden zeros manifest.
In this paper, we have focused on zeroes and factorization at tree level, where at least
for the Tr( _ϕ_ [3] ) theory the amplitude is given by the canonical form for the associahedron.
We now know that the integrand for the Tr( _ϕ_ [3] ) theory at 1-loop is also given by the
canonical form of a cousin of the associahedron, also naturally presented as a Minkowski
sum of simplices [22, 45]. Thus we expect a similar locus in kinematic space where the
one-loop integrand has zero/factorization patterns, which would be interesting to flesh
out. Of course this locus will in general involve sending kinematic variables involving the
loop momenta to zero, and so don’t immediately imply zeros for integrated amplitudes.
It would be interesting to see if any trace of these zeros survives post-loop integration.
Beyond one loop and to all orders in the topological expansion, there are various notions of
a loop integrand naturally associated with surfaces, with the simplest “infinite integrand”
reflecting the action of the mapping class group and the concomitant infinite repetition
of Feynman diagrams/triangulations of the surface. This infinite integrand is also the
canonical form of associated polytopes–“surfacehedra”–having infinitely many facets with
a fractal structure [21]. Surfacehedra are also Minkowski sums, so at least the infinite
integrand should also have patterns of zeros and factorization, though the implications of


49


this fact both for naturally finite integrands obtained by truncating the surfacehedra or
modding out by the mapping class group must be properly understood.
The phenomenon of factorization near zeros is clearly striking, and it would be fascinating to understand if and how it generalizes. We have seen an especially simple geometric
understanding of this factorization, by understanding how the associahedron degenerates
as Minkowski summands are shut off, so that at the penultimate step before it collapses
entirely to lower dimensions, it simplifies drastically to what we described in the introduction as the “sandwich”, with an interval separating two opposite facets. It is natural to
wonder whether there are other predictable patterns for the degenerating associahedron
as we turn on further _c_ ’s, that might also have interpretations in terms of factorization.
We are aware of one such pattern: if instead of turning on a single _ci∗,j∗_ in our maximal
causal diamond, we turn on an entire strip i.e. _ci∗,k_ for all _k_ inside the diamond, then the
amplitude _also_ factorizes. This is an interpretation in our mesh picture of the “3-splits” for
Tr( _ϕ_ [3] ) amplitudes discovered in [46]. It would be interesting to try and interpret this in the
language of the associahedron and examine how it might extend to full string amplitudes.
More generally it would be interesting to classify the general set of factorization properties
for string amplitudes associated with shutting off various patterns of _c_ ’s.
In another vein, it is interesting that starting purely from the NLSM, we are naturally
led to discover the mixed _π/ϕ_ amplitudes from the near-zero factorizations. The particular
mixed amplitudes we discover in this way are clearly only a tiny subset of all possible mixed
amplitudes–for instance, they all contain only three _ϕ_ ’s. In [18] we will show how general
NLSM + _ϕ_ [3] amplitudes can be obtained by a simple set of kinematic shifts of the Tr( _ϕ_ [3] )
amplitudes. Of course, the mixed amplitudes do not have all of our zeros, and so the shifts
are not the _c_ -preserving shifts featured in this paper.
Nonetheless, this general phenomenon of kinematic shifts generating non-trivial theories
from simple ones is a fascinating one, and it would be interesting to see how far it extends.
One especially simple example is worth mentioning as an interesting contrast to the shift
we have highlighted in this paper. Suppose we shift the _g_ Tr( _ϕ_ [3] ) amplitudes by _Xe,e_ ; _o,o_ _→_
_Xe,e_ ; _o,o_ + _δ, Xe,o_ _→_ _Xe,o_, i.e. no _±δ_ difference. This still removes all the massless poles
_Xee, Xoo_ and leaves us only with poles associated with even-particle scattering amplitudes.
It is trivial to see that the low-energy amplitudes for _X_ _≪_ _δ_ with the deformation are
nothing but that of _λ_ Tr( _ϕ_ [4] ) theory with quartic coupling _λ_ = _g_ [2] _/δ_, augmented with a
further tower of higher-dimension operators. It is striking that this seemingly minor but
unusual change–the sign difference between even-even and odd-odd shifts–makes all the
difference in the world in going from generating the relatively boring Tr( _ϕ_ [4] ) theory to the
much richer and more intricate amplitudes for pions and gluons!
As another amusing example, suppose we take the _g_ Tr( _ϕ_ [3] ) theory but this time shift
_all_ 1 _/X_ _→_ 1 _/X_ + _κ_ . Clearly, the new functions we obtain in this way will still factorize
onto themselves on the massless poles, and so still define a consistent set of amplitudes.
But for which theory? We can actually determine a Lagrangian for the amplitudes of
this theory in a very simple way. At any _n_, there is the part of the amplitude with no
poles at all–purely a contact interaction. At _n_ points, this is given by simply replacing
every propagator by _κ_ ; since there are Catalan _n−_ 3 many diagrams at _n_ points, this contact


50


interaction is _Cn−_ 3 _κ_ _[n][−]_ [3] _g_ _[n][−]_ [2] . Hence we can identify an interesting non-linear Lagrangian
we can call the “Catalan Lagrangian” that gives rise to the amplitudes associated with
this shift: _L_ [Catalan] = [�] _n_ _[∞]_ =3 _[C][n][−]_ [3] _[g][n][−]_ [2] _[κ][n][−]_ [3][Tr(] _[ϕ][n]_ [)] [=] _[g]_ [Tr] �( _[√]_ 1 _−_ 4 _gκϕ −_ 1) _/_ (2 _κ_ )�. This is
again an interesting cousin of the more interesting and surprising linear shift in our paper,
which starts from the polynomial Tr( _ϕ_ [3] ) theory and generates the amplitudes for the nonpolynomial Lagrangian describing pion scattering. It would be interesting to map out the
space of these possible deformations more systematically.
Finally, it is clearly interesting to study the widest class of theories connected by sharing
hidden zeros and factorization. The most obvious place to begin is to simply consider our
shifted theories with general values for _δ_ . As we have explained for generic fractional _δ_, the
low-energy amplitudes are always those of the NLSM. But for _α_ _[′]_ _δ_ being integers, something
more interesting happens. As we have seen for _α_ _[′]_ _δ_ = 1 we have a theory of massless gluons
interacting with the “scaffolding” of the external scalars. It is easy to see that for e.g.
_α_ _[′]_ _δ_ = 2, while the leading interactions at low-energies are those of gluons coupled to the
scaffolding scalars, there are _also_ interactions that must be interpreted as arising from a
theory of massless colored particles of spin 2. In general for _α_ _[′]_ _δ_ = _J_, at least kinematically
we are describing gluons coupled to a tower of massless colored particles of spin up to _J_ .
Of course there are famous theorems [47] about the impossibility of consistent theories for
massless colored particles of high spin, so at first blush these theories for _J_ _>_ 1 should be
discredited on physical grounds. But the way they naturally connect to Tr( _ϕ_ [3] ), NLSM, and
Yang-Mills, simply via further continuing the _δ_ deformation, suggests these theories may
somehow have a purpose in life, perhaps especially in the limit as _δ_ _→∞_, where an infinite
tower of higher-spin colored particles become massless.


**Acknowledgments**


It is our pleasure to thank Alfredo Guevara, Daniel Longenecker, Giulio Salvatori, Yichao
Tang, Jaroslav Trnka, Ellis Ye Yuan, Yaoqi Zhang for inspiring discussions. The work of
N.A.H. is supported by the DOE (Grant No. DE-SC0009988), by the Simons Collaboration
on Celestial Holography, and further support was made possible by the Carl B. Feinberg
cross-disciplinary program in innovation at the IAS. The work of Q.C. is supported by the
National Natural Science Foundation of China under Grant No. 123B2075. The work of
C.F. is supported by FCT/Portugal (Grant No. 2023.01221.BD). The work of S.H. has
been supported by the National Natural Science Foundation of China under Grant No.
12225510, 11935013, 12047503, 12247103, and by the New Cornerstone Science Foundation
through the XPLORER PRIZE.


**Bibliography**


[1] N. Arkani-Hamed and J. Trnka, _The_ _Amplituhedron_, _JHEP_ **10** (2014) 030,

[ `[arXiv:1312.2007](http://arxiv.org/abs/1312.2007)` ].


[2] N. Arkani-Hamed, Y. Bai, S. He, and G. Yan, _Scattering_ _Forms_ _and_ _the_ _Positive_ _Geometry_
_of_ _Kinematics,_ _Color_ _and_ _the_ _Worldsheet_, _JHEP_ **05** (2018) 096, [ `[arXiv:1711.09102](http://arxiv.org/abs/1711.09102)` ].


51


[3] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _All_ _Loop_
_Scattering_ _as_ _a_ _Counting_ _Problem_, `[arXiv:2309.15913](http://arxiv.org/abs/2309.15913)` .


[4] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _All_ _Loop_
_Scattering_ _For_ _All_ _Multiplicity_, `[arXiv:2311.09284](http://arxiv.org/abs/2311.09284)` .


[5] J. M. Drummond, J. Henn, V. A. Smirnov, and E. Sokatchev, _Magic_ _identities_ _for_ _conformal_
_four-point_ _integrals_, _JHEP_ **01** (2007) 064, [ `[hep-th/0607160](http://arxiv.org/abs/hep-th/0607160)` ].


[6] N. Arkani-Hamed, S. He, and T. Lam, _Stringy_ _canonical_ _forms_, _JHEP_ **02** (2021) 069,

[ `[arXiv:1912.08707](http://arxiv.org/abs/1912.08707)` ].


[7] N. Arkani-Hamed, S. He, T. Lam, and H. Thomas, _Binary_ _geometries,_ _generalized_ _particles_
_and_ _strings,_ _and_ _cluster_ _algebras_, _Phys._ _Rev._ _D_ **107** (2023), no. 6 066015,

[ `[arXiv:1912.11764](http://arxiv.org/abs/1912.11764)` ].


[8] Z. Bern, J. J. M. Carrasco, and H. Johansson, _New_ _Relations_ _for_ _Gauge-Theory_ _Amplitudes_,
_Phys._ _Rev._ _D_ **78** (2008) 085011, [ `[arXiv:0805.3993](http://arxiv.org/abs/0805.3993)` ].


[9] Z. Bern, J. J. M. Carrasco, and H. Johansson, _Perturbative_ _Quantum_ _Gravity_ _as_ _a_ _Double_
_Copy_ _of_ _Gauge_ _Theory_, _Phys._ _Rev._ _Lett._ **105** (2010) 061602, [ `[arXiv:1004.0476](http://arxiv.org/abs/1004.0476)` ].


[10] F. Cachazo, S. He, and E. Y. Yuan, _Scattering_ _equations_ _and_ _Kawai-Lewellen-Tye_
_orthogonality_, _Phys._ _Rev._ _D_ **90** (2014), no. 6 065001, [ `[arXiv:1306.6575](http://arxiv.org/abs/1306.6575)` ].


[11] F. Cachazo, S. He, and E. Y. Yuan, _Scattering_ _of_ _Massless_ _Particles_ _in_ _Arbitrary_
_Dimensions_, _Phys._ _Rev._ _Lett._ **113** (2014), no. 17 171601, [ `[arXiv:1307.2199](http://arxiv.org/abs/1307.2199)` ].


[12] F. Cachazo, S. He, and E. Y. Yuan, _Scattering_ _of_ _Massless_ _Particles:_ _Scalars,_ _Gluons_ _and_
_Gravitons_, _JHEP_ **07** (2014) 033, [ `[arXiv:1309.0885](http://arxiv.org/abs/1309.0885)` ].


[13] F. Cachazo, S. He, and E. Y. Yuan, _Scattering_ _Equations_ _and_ _Matrices:_ _From_ _Einstein_ _To_
_Yang-Mills,_ _DBI_ _and_ _NLSM_, _JHEP_ **07** (2015) 149, [ `[arXiv:1412.3479](http://arxiv.org/abs/1412.3479)` ].


[14] Z. Bern, J. J. Carrasco, M. Chiodaroli, H. Johansson, and R. Roiban, _The_ _Duality_ _Between_
_Color_ _and_ _Kinematics_ _and_ _its_ _Applications_, `[arXiv:1909.01358](http://arxiv.org/abs/1909.01358)` .


[15] Z. Bern, J. J. Carrasco, M. Chiodaroli, H. Johansson, and R. Roiban, _The_ _SAGEX_ _review_ _on_
_scattering_ _amplitudes_ _Chapter_ _2:_ _An_ _invitation_ _to_ _color-kinematics_ _duality_ _and_ _the_ _double_
_copy_, _J._ _Phys._ _A_ **55** (2022), no. 44 443003, [ `[arXiv:2203.13013](http://arxiv.org/abs/2203.13013)` ].


[16] T. Adamo, J. J. M. Carrasco, M. Carrillo-González, M. Chiodaroli, H. Elvang, H. Johansson,
D. O’Connell, R. Roiban, and O. Schlotterer, _Snowmass_ _White_ _Paper:_ _the_ _Double_ _Copy_ _and_
_its_ _Applications_, in _Snowmass_ _2021_, 4, 2022. `[arXiv:2204.06547](http://arxiv.org/abs/2204.06547)` .


[17] Z. Koba and H. B. Nielsen, _Reaction_ _amplitude_ _for_ _n_ _mesons:_ _A_ _Generalization_ _of_ _the_
_Veneziano-Bardakci-Ruegg-Virasora_ _model_, _Nucl._ _Phys._ _B_ **10** (1969) 633–655.


[18] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _NLSM_ _⊂_ _Tr_ ( _ϕ_ [3] ),

`[arXiv:2401.05483](http://arxiv.org/abs/2401.05483)` .


[19] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Scalar-Scaffolded_ _Gluons_ _and_
_the_ _Combinatorial_ _Origins_ _of_ _Yang-Mills_ _Theory_, `[arXiv:2401.00041](http://arxiv.org/abs/2401.00041)` .


[20] A. D’Adda, S. Sciuto, R. D’Auria, and F. Gliozzi, _Zeros_ _of_ _dual_ _resonant_ _amplitudes_, _Nuovo_
_Cim._ _A_ **5** (1971) 421–432.


[21] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _Surfacehedra,_
_to_ _appear_, .


52


[22] N. Arkani-Hamed, S. He, G. Salvatori, and H. Thomas, _Causal_ _diamonds,_ _cluster_ _polytopes_
_and_ _scattering_ _amplitudes_, _JHEP_ **11** (2022) 049, [ `[arXiv:1912.12948](http://arxiv.org/abs/1912.12948)` ].


[23] K. Kampf, J. Novotny, and J. Trnka, _Tree-level_ _Amplitudes_ _in_ _the_ _Nonlinear_ _Sigma_ _Model_,
_JHEP_ **05** (2013) 032, [ `[arXiv:1304.3048](http://arxiv.org/abs/1304.3048)` ].


[24] C. Cheung, K. Kampf, J. Novotny, and J. Trnka, _Effective_ _Field_ _Theories_ _from_ _Soft_ _Limits_ _of_
_Scattering_ _Amplitudes_, _Phys._ _Rev._ _Lett._ **114** (2015), no. 22 221602, [ `[arXiv:1412.4095](http://arxiv.org/abs/1412.4095)` ].


[25] S. L. Adler, _Consistency_ _conditions_ _on_ _the_ _strong_ _interactions_ _implied_ _by_ _a_ _partially_
_conserved_ _axial_ _vector_ _current_, _Phys._ _Rev._ **137** (1965) B1022–B1033.


[26] F. Cachazo, P. Cha, and S. Mizera, _Extensions_ _of_ _Theories_ _from_ _Soft_ _Limits_, _JHEP_ **06**
(2016) 170, [ `[arXiv:1604.03893](http://arxiv.org/abs/1604.03893)` ].


[27] G. Veneziano, _Construction_ _of_ _a_ _crossing_ _-_ _symmetric,_ _Regge_ _behaved_ _amplitude_ _for_ _linearly_
_rising_ _trajectories_, _Nuovo_ _Cim._ _A_ **57** (1968) 190–197.


[28] P. Di Vecchia, _The_ _Birth_ _of_ _string_ _theory_, _Lect._ _Notes_ _Phys._ **737** (2008) 59–118,

[ `[arXiv:0704.0101](http://arxiv.org/abs/0704.0101)` ].


[29] C. R. Mafra, O. Schlotterer, and S. Stieberger, _Complete_ _N-Point_ _Superstring_ _Disk_
_Amplitude_ _II._ _Amplitude_ _and_ _Hypergeometric_ _Function_ _Structure_, _Nucl._ _Phys._ _B_ **873** (2013)
461–513, [ `[arXiv:1106.2646](http://arxiv.org/abs/1106.2646)` ].


[30] J. Broedel, O. Schlotterer, and S. Stieberger, _Polylogarithms,_ _Multiple_ _Zeta_ _Values_ _and_
_Superstring_ _Amplitudes_, _Fortsch._ _Phys._ **61** (2013) 812–870, [ `[arXiv:1304.7267](http://arxiv.org/abs/1304.7267)` ].


[31] C. R. Mafra and O. Schlotterer, _Non-abelian_ _Z-theory:_ _Berends-Giele_ _recursion_ _for_ _the_
_α_ _[′]_ _-expansion_ _of_ _disk_ _integrals_, _JHEP_ **01** (2017) 031, [ `[arXiv:1609.07078](http://arxiv.org/abs/1609.07078)` ].


[32] J. J. M. Carrasco, C. R. Mafra, and O. Schlotterer, _Abelian_ _Z-theory:_ _NLSM_ _amplitudes_ _and_
_α’-corrections_ _from_ _the_ _open_ _string_, _JHEP_ **06** (2017) 093, [ `[arXiv:1608.02569](http://arxiv.org/abs/1608.02569)` ].


[33] F. C. S. Brown, _Multiple_ _zeta_ _values_ _and_ _periods_ _of_ _moduli_ _spaces_ _M_ _0_ _,n_ _(_ _R_ _)_, _Annales_ _Sci._
_Ecole_ _Norm._ _Sup._ **42** (2009) 371, [ `[math/0606419](http://arxiv.org/abs/math/0606419)` ].


[34] C. Cheung, K. Kampf, J. Novotny, C.-H. Shen, and J. Trnka, _On-Shell_ _Recursion_ _Relations_
_for_ _Effective_ _Field_ _Theories_, _Phys._ _Rev._ _Lett._ **116** (2016), no. 4 041601, [ `[arXiv:1509.03309](http://arxiv.org/abs/1509.03309)` ].


[35] N. Arkani-Hamed, L. Rodina, and J. Trnka, _Locality_ _and_ _Unitarity_ _of_ _Scattering_ _Amplitudes_
_from_ _Singularities_ _and_ _Gauge_ _Invariance_, _Phys._ _Rev._ _Lett._ **120** (2018), no. 23 231602,

[ `[arXiv:1612.02797](http://arxiv.org/abs/1612.02797)` ].


[36] L. Rodina, _Uniqueness_ _from_ _gauge_ _invariance_ _and_ _the_ _Adler_ _zero_, _JHEP_ **09** (2019) 084,

[ `[arXiv:1612.06342](http://arxiv.org/abs/1612.06342)` ].


[37] M. Bianchi, D. Consoli, and P. Di Vecchia, _On_ _the_ _N-pion_ _extension_ _of_ _the_ _Lovelace-Shapiro_
_model_, _JHEP_ **03** (2021) 119, [ `[arXiv:2002.05419](http://arxiv.org/abs/2002.05419)` ].


[38] M. B. Green, J. H. Schwarz, and E. Witten, _SUPERSTRING_ _THEORY._ _VOL._ _1:_
_INTRODUCTION_ . Cambridge Monographs on Mathematical Physics. 7, 1988.


[39] S. He, F. Teng, and Y. Zhang, _String_ _amplitudes_ _from_ _field-theory_ _amplitudes_ _and_ _vice_ _versa_,
_Phys._ _Rev._ _Lett._ **122** (2019), no. 21 211603, [ `[arXiv:1812.03369](http://arxiv.org/abs/1812.03369)` ].


[40] S. He, F. Teng, and Y. Zhang, _String_ _Correlators:_ _Recursive_ _Expansion,_ _Integration-by-Parts_
_and_ _Scattering_ _Equations_, _JHEP_ **09** (2019) 085, [ `[arXiv:1907.06041](http://arxiv.org/abs/1907.06041)` ].


53


[41] R. H. Boels and T. Hansen, _String_ _theory_ _in_ _target_ _space_, _JHEP_ **06** (2014) 054,

[ `[arXiv:1402.6356](http://arxiv.org/abs/1402.6356)` ].


[42] R. Britto, F. Cachazo, B. Feng, and E. Witten, _Direct_ _proof_ _of_ _tree-level_ _recursion_ _relation_ _in_
_Yang-Mills_ _theory_, _Phys._ _Rev._ _Lett._ **94** (2005) 181602, [ `[hep-th/0501052](http://arxiv.org/abs/hep-th/0501052)` ].


[43] N. Arkani-Hamed, Y. Bai, and T. Lam, _Positive_ _Geometries_ _and_ _Canonical_ _Forms_, _JHEP_ **11**
(2017) 039, [ `[arXiv:1703.04541](http://arxiv.org/abs/1703.04541)` ].


[44] N. Arkani-Hamed, A. Hodges, and J. Trnka, _Positive_ _Amplitudes_ _In_ _The_ _Amplituhedron_,
_JHEP_ **08** (2015) 030, [ `[arXiv:1412.8478](http://arxiv.org/abs/1412.8478)` ].


[45] G. Salvatori, _1-loop_ _Amplitudes_ _from_ _the_ _Halohedron_, _JHEP_ **12** (2019) 074,

[ `[arXiv:1806.01842](http://arxiv.org/abs/1806.01842)` ].


[46] F. Cachazo, N. Early, and B. Giménez Umbert, _Smoothly_ _splitting_ _amplitudes_ _and_
_semi-locality_, _JHEP_ **08** (2022) 252, [ `[arXiv:2112.14191](http://arxiv.org/abs/2112.14191)` ].


[47] S. Weinberg and E. Witten, _Limits_ _on_ _Massless_ _Particles_, _Phys._ _Lett._ _B_ **96** (1980) 59–62.


54


of 6-point NLSM.


55


57


