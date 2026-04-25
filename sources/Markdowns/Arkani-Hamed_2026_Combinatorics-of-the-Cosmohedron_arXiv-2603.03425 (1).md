## Combinatorics of the cosmohedron

Federico Ardila-Mantilla [∗] Nima Arkani-Hamed [†]


Carolina Figueiredo [‡] Francisco Vaz˜ao [§]


**Abstract**
The cosmohedron was recently proposed as a polytope underlying the cosmological
wavefunction for Tr(Φ [3] ) theory. Its faces were conjectured to be in bijection with
Matryoshkas, which are obtained from a subdivision of a polygon by sequentially
wrapping groups of polygons into larger polygons. In this paper, we prove the
correctness of this construction and elucidate its combinatorial structure. Cosmohedra
generalize to a wider class of _X_ in _Y_ polytopes, where we chisel a polytope from
the family _X_ at each vertex of a polytope _Y_ . We sketch a new application of
these chiseled polytopes to the physics of ultraviolet divergences in loop-integrated
Feynman amplitudes.

### **1 Introduction**


It has been a long-standing question in cosmology to find a geometric object that encodes
the cosmological wavefunction of Tr( _ϕ_ [3] ) theory. The combinatorics of this wavefunction
is governed by certain nesting subdivisions of a polygon that we call _Matryoshkas_ .


Arkani-Hamed, Figueiredo, and Vaz˜ao [AHFV25] proposed a construction of the _cosmohedron_
as a solution to this cosmological question. The goal of this article is to prove the
correctness of that subtle construction. Along the way we recover and discover numerous
physical, combinatorial, polyhedral, and enumerative properties of Matryoshkas and
cosmohedra, that we briefly outline in this introduction.


∗Queen Mary University of London and San Francisco State University; `f.ardila@qmul.ac.uk` .
†Institute for Advanced Study, Princeton; `arkani@ias.edu.`
‡Jadwin Hall, Princeton University; `cfigueiredo@princeton.edu` .
§Institute for Advanced Study, Princeton; `fvvazao@ias.edu` .


1


**1.1** **Combinatorial** **properties** **of** **the** **cosmohedron**


The combinatorial structure of the cosmological wavefunction of Tr( _ϕ_ [3] ) theory is described
by the _Matryoshkas_ of an ( _n_ + 2)-gon _n_ +2, so these are the objects we wish to model
geometrically in the cosmohedron. We� call them Matryoshkas because their nesting
structure is reminiscent of, though much richer than, that of the Matryoshka dolls created
by S. Malyutin and V. Zvyozdochkin in Russia in the 1890s.
One way of constructing a Matryoshka, “from the inside out,” is to choose a subdivision
of _n_ +2, and then repeatedly choosing a group of adjacent outermost polygons and
wrapping� them into a larger polygon engulfing them. Alternatively, “from the outside
in”, a Matryoshka is obtained recursively by choosing a subdivision of _n_ +2, and then
placing a Matryoshka inside each of its polygons. 

Figure 1: An octagonal Matryoshka _M_ and a maximal Matryoshka _M_ _[′]_ containing it.


Naturally, we can think of a Matryoshka as a set of polygons. This gives a partial
order on the set of Matryoshkas on _n_ +2 by _containment_ : we have _M_ _≤_ _M_ _[′]_ if every
polygon of _M_ is also in _M_ _[′]_ . Arkani-Hamed, Figueiredo, and Vaz˜ao introduced an ( _n −_ 1)-dimensional polytope
called the _cosmohedron_ to encode this combinatorial structure; see Definition 4.15. Our
main result is a proof of the following statement from [AHFV25].


**Theorem** **1.1.** _The_ _face_ _lattice_ _of_ _the_ ( _n −_ 1) _-cosmohedron_ _is_ _anti-isomorphic_ _to_ _the_
_poset_ _of_ _Matryoshkas_ _of_ _an_ ( _n_ + 2) _-gon._


**1.2** **Polyhedral** **properties** **of** **the** **cosmohedron**


The search for a cosmohedron that models the combinatorics of Matryoshkas is analogous,
and in fact closely related, to earlier constructions of polyhedra with a desired combinatorial
structure. An important motivating example is the _associahedron_, whose faces are in
bijection with the plane trees of a given size.
The cosmohedron is obtained from the associahedron through a careful chiseling
procedure: at each vertex _aT_ corresponding to the binary tree _T_, we chisel a copy of the
_bracket_ _associahedron_ Br _T_ . The chiselings at the different vertices interact with each


2


Arkani–Hamed, Figueiredo, and Vaz˜ao [AHFV25] proposed a construction of the
cosmohedron AFV _n−_ 1 as an ( _n−_ 1)-dimensional polytope in R [(] _[n]_ [+2)(] _[n][−]_ [1)] _[/]_ [2] ; see Definition
4.15. This embedding gives the polytope an elegant inequality description, but it does
not offer a direct path to prove its correctness, as we explain in Sections 1.4 and 6.
Our approach is to construct a different embedding Cosmo _n−_ 1 of the cosmohedron in
(a hyperplane in) R _[n]_ which is closer in spirit to the family of generalized permutahedra.
To do so, we begin by building its normal fan CosmoFan _n−_ 1 in R _[n]_ _/_ R, and proving that
it has the correct combinatorial structure of Matryoshkas; we do this in Definition 2.3
and Theorem 3.6. Next, we construct explicit coordinates for the vertices of Cosmo _n−_ 1,
and prove that its normal fan is CosmoFan _n−_ 1 in Theorem 4.11. Since we know the rays
of the fan, we can readily use them to compute the inequality description of Cosmo _n−_ 1
in Theorem 4.13. Finally, with inequality descriptions at hand for both of them, we
find a linear isomorphism between Cosmo _n−_ 1 in R _[n]_ and AFV _n−_ 1 in R [(] _[n]_ [+2)(] _[n][−]_ [1)] _[/]_ [2] in
Theorem 4.16. This proves the combinatorial structure of the cosmohedron AFV _n−_ 1 as
conjectured in [AHFV25].


**1.3** **Enumerative** **properties** **of** **the** **cosmohedron**


In Section 5 we turn to enumerative questions. The facets of the cosmohedron are
in bijection with the non-trivial subdivisions of _n_ +2, which are enumerated by the

              
3


Hipparchus–Schr¨oder numbers. This sequence is well understood, and is in fact one of
the earliest combinatorial sequences, dating to the second century BC; for an interesting
historical account, see [Sta99, Sta97].
The vertices correspond to the maximal Matryoshkas; we prove that they are enumerated
by sequence A177384 in the OEIS. We give a recursive formula for the sequence and a
simple polynomial differential equation for the power series:


**Theorem** **1.2.** _The_ _generating_ _function_ _M_ ( _x_ ) = _x_ [2] + 2 _x_ [3] + 10 _x_ [4] + 72 _x_ [5] + _· · ·_ _for_ _the_
_number_ _of_ _maximal_ _Matryoshkas_ _is_ _characterized_ _by_ _the_ _polynomial_ _differential_ _equation_


_M_ ( _x_ ) = _x_ [2] + _M_ ( _x_ ) _M_ _[′]_ ( _x_ ) _._


Thus Matryoshkal numbers form one of the simplest sequences in the notoriously difficult
family of _D-algebraic_ _power_ _series_ [Mel21]. For instance, we do not know how to prove
the asymptotic behavior of this sequence; see Conjecture 5.7.
We also give an intriguing description for the _f_ -vectors of cosmohedra: their generating
function equals its own compositional inverse up to a simple transformation. Consider
the _f_ -polynomials of the cosmohedral fans _fn_ ( _t_ ) as well as the simple transformation
_gn_ ( _t_ ) = ((1 + _t_ ) _fn_ ( _t_ ) _−_ 1) _/t_ . The coefficients of _gn_ ( _t_ ) are obtained by adding consecutive
coefficients of _fn_ ( _t_ ):


_f_ 1( _t_ ) = 1 _,_ _f_ 2( _t_ ) = 1 + 2 _t,_ _f_ 3( _t_ ) = 1 + 10 _t_ + 10 _t_ [2] _,_ _f_ 4( _t_ ) = 1 + 44 _t_ + 114 _t_ [2] + 72 _t_ [3] _, . . ._

_g_ 1( _t_ ) = 1 _,_ _g_ 2( _t_ ) = 3 + 2 _t,_ _g_ 3( _t_ ) = 11 + 20 _t_ + 10 _t_ [2] _,_ _g_ 4( _t_ ) = 45 + 158 _t_ + 186 _t_ [2] + 72 _t_ [3] _, . . ._


**Theorem** **1.3.** _The_ _f_ _-polynomials_ _of_ _cosmohedra_ _form_ _the_ _unique_ _sequence_ _{fn_ ( _t_ ) _}n≥_ 1
_such_ _that_ _the_ _power_ _series_ _in_ (R[ _t_ ])[ _x_ ]


_x −_ _f_ 1( _t_ ) _x_ [2] _−_ _f_ 2( _t_ ) _x_ [3] _−_ _f_ 3( _t_ ) _x_ [4] _−_ _. . ._

_x_ + _g_ 1( _t_ ) _x_ [2] + _g_ 2( _t_ ) _x_ [3] + _g_ 3( _t_ ) _x_ [3] + _. . ._


_are_ _compositional_ _inverses,_ _where_ _gn_ ( _t_ ) = ((1 + _t_ ) _fn_ ( _t_ ) _−_ 1) _/t_ _for_ _n ≥_ 1 _._


We also give a strikingly similar formula for the _f_ -vector of the correlatron.


**1.4** **Elusive** **qualities** **of** **the** **cosmohedron**


As mentioned above, Arkani–Hamed, Figueiredo, and Vaz˜ao’s cosmohedron AFV _n−_ 1 is
an ( _n_ _−_ 1)-dimensional polytope in R [(] _[n]_ [+2)(] _[n][−]_ [1)] _[/]_ [2], given by a combinatorially rich system
of inequalities; see Definition 4.15. How might one prove its combinatorial structure?
The standard methods don’t give a simple approach.
One might try to prove that AFV _n−_ 1 has the correct incidences between vertices
and facets. However, we did not have a formula for the vertices of AFV _n−_ 1 before; and
now that we do thanks to Proposition 4.8, we see they are rather intricate. Proving the
vertex-facet incidences would be a highly non-trivial matter.
To circumvent this issue, one might instead describe the normal fan of AFV _n−_ 1,
and prove the corresponding wall-crossing inequalities, as described for example in


4


[ACEP20, Lemma 2.10] or [CLS24, Theorems 6.1.5–6.1.7]. We know at the outset that
this computation would be much more cumbersome than usual, because the normal fan is
not simplicial. Furthermore, in this high dimensional embedding, the ( _n−_ 1)-dimensional
normal fan lives in a combinatorially intricate quotient of an [1]

2 [(] _[n]_ [+2)(] _[n][−]_ [1)–dimensional]
space, so the description of the normal fan is far from unique. These obstacles make this
computation very subtle as well.
These are the reasons why we proceeded by giving a different construction of the
cosmohedron Cosmo _n−_ 1 in R _[n]_, in the spirit of generalized permutahedra, and proved its
combinatorial structure. Then, as we somewhat optimistically hoped at the outset, the
polytopes Cosmo _n−_ 1 and AFV _n−_ 1 turned out to be linearly, and thus combinatorially
equivalent.
However, proving the correctness of Cosmo _n−_ 1 is still a delicate matter. Cosmohedra
are related to several polytopes in the mathematical literature, some of which are known
to be relevant in physical applications, and many of which are generalized permutahedra.
These include permutahedra [BS13, Sch13], associahedra [CSZ15, Lod04, Sta63, Tam54],
bracket associahedra [BCL [+] 22, LA22] (which are special cases of graph associahedra

[CD06, Dev09, Pos09]), permutoassociahedra [CL23, Kap93], and permutonestohedra

[Gai15], among others. There are numerous methods to prove the combinatorial structure
of such polytopes.
In Section 6 we explain that the cosmohedron Cosmo _n−_ 1 is more subtle than its
predecessors in several ways: it is not very symmetric, it is not simple, it depends very
delicately on the chiseling, we do not know how to express it as a deformation of an
easy polytope, we do not know how to express it as a Minkowski sum of easy polytopes,
and its faces factor combinatorially but not geometrically. For these reasons, proving its
combinatorial structure requires new ideas, as described above.


**1.5** **Cosmological** **properties** **of** **the** **cosmohedron**


Let us close this introduction by briefly explaining the physical origins of this project.
The content of this section is not essential to the mathematical understanding of this
paper, but it is essential to the discovery of these mathematical objects, and it gives rise
to many interesting new directions.
The past decade has seen the discovery of startling and deep new connections between
fundamental physics and new mathematical structures in combinatorics and geometry.
The story began with the most basic and fundamental physical processes in nature–the
collision and scattering of elementary particles. Because of quantum mechanics, the
outcome of any given scattering process is uncertain; only the probability for different
states can be predicted. Given an initial state _i_ and a final state _f_, the probability is
_|Ai,f_ _|_ [2] where _Ai,f_ is the _scattering amplitude_ . The textbook method for computing these
amplitudes is to sum over _Feynman_ _diagrams_ representing the different ways in which
the collision events can take place in space and time.
The connection to combinatorics and geometry can most easily and vividly be illustrated
in an especially useful toy model, the so-called _Tr(ϕ_ [3] _)_ theory, for “colored” scalar
particles represented by _N_ _× N_ square matrices. In the simplest limit (“tree-level”),


5


the amplitude turns into the sum over all planar trivalent (known in physics as _cubic_ )
tree diagrams, or what is the same, a sum over the triangulations of an _n_ -gon.
A priori to a physicist, there is no obvious combinatorics here: we simply have a
collection of diagrams that have to be collected and summed over, in no particular
order, to arrive at the final result. But a combinatorialist knows that there is something
very special about this particular collection of objects: the triangulations of an _n_ -gon
are captured by the vertices of a polytope, the associahedron.
This link turns out to be the tip of a large iceberg of much larger significance to
physics beyond “merely” the combinatorics of diagrams. A particular embedding of the
associahedron allows us to extract mathematical expressions for the scattering amplitude
from the geometry [AHBHY18a]. This particular embedding makes it natural to think
of the associahedron as a Minkowski sum of the simplest possible pieces - a collection
of simplices - and quite remarkably, this fact is intimately related to (and indeed lets
us naturally discover from the bottom-up) the generalization from particle scattering to
scattering processes in string theory. Over the past few years, these developments have
led to the discovery of a number of surprising connections between seemingly totally
different physical theories [AHCD [+] 24] and, almost as an incidental byproduct, have
provided new ways to simplify enormously complicated Feynman diagram calculations,
sometimes into a few lines.
The connection to physics also led to the discovery of new mathematical objects.
For instance, the associahedron captures all tree diagrams, but what about diagrams
that can be drawn on surfaces with arbitrary topology? The consistency of the physical
picture demands that geometric objects encoding such diagrams must exist, and they
have indeed been described in the physics literature [AHFS [+] 25].
This emerging connection between physics and combinatorics suggests a radical new
picture for the laws of physics, where the notion of particle evolution in spacetime is
not primary. Instead, the unifying combinatorial-geometric objects that control how all
spacetime processes are “glued together” play a more fundamental role. This dovetails
nicely with an expectation widely shared by most theoretical physicists that the notion of
spacetime cannot be fundamental but must eventually be supplanted by more elementary
and abstract ideas. The new connection to combinatorics suggests a concrete strategy
for pursuing this vision.
Nowhere is the need for a new picture of physics supplanting spacetime more urgent
than in cosmology. Amongst other things, the notion of time itself breaks down at the
big bang singularity, so the standard picture of time evolution must likely be abandoned.
Cosmology also offers us a rich set of physical observables to compute, and in principle
measure, that turn out to be interesting generalizations of scattering amplitudes. It
is widely believed that the very early history of the universe involved a period of
exponentially rapid expansion known as _inflation_, and that quantum fluctuations in
this early inflationary phase were blown up to enormous scales, even larger than our
observable universe, giving rise to all the “clumpiness” in matter and all the interesting
structures we see in the universe today. The details of these quantum fluctuations
are reflected in the statistics of the distribution of mass and energy in the universe


6


today and are known as _cosmological_ _correlation_ _functions_ . The cosmological correlators
produced during inflation are computed in much the same way as particle scattering
amplitudes, drawing diagrams for all possible ways the correlations could have been
produced. But there is an important difference: while for scattering processes a single
diagram represents a single elementary process, in cosmology, even a single diagram
has much more structure, precisely having to do with the different time-ordering of
“histories” a given diagram can represent.
If we return to the toy Tr( _ϕ_ [3] ) theory, to compute a cosmological correlator, a given
diagram must be further decorated by all the possible _bracketings_ of the graph, or
equivalently, what we will call the possible _Matryoshkas_ associated with the corresponding
triangulation. This arises in a very natural way when solving the Schr¨odinger equation
_H_ Ψ = _E_ Ψ to compute the wavefunction Ψ( _ϕ_ ) for _ϕ_, from which we determine probabilities
and correlation functions. The Schr¨odinger equation for Ψ( _ϕ_ ) = exp[ _ψ_ ( _ϕ_ )] can be solved
in perturbation theory. The exponential relating Ψ( _ϕ_ ) to _ψ_ ( _ϕ_ ) reflects the familiar
exponential relationship between all graphs and connected graphs. Every connected
cubic diagram with _n_ external legs, where the external legs carry spatial momentum _[⃗]_ _ki_,
makes a contribution to the coefficient of _ϕ_ ( _[⃗]_ _k_ 1) _· · · ϕ_ ( _[⃗]_ _kn_ ) in the Taylor expansion of _ψ_ ( _ϕ_ )
in powers of _ϕ_ . The contribution of a diagram to _ψ_ depends on “energies” entering each
subgraph – this is the total sum of the magnitude of the momenta entering the subgraph.
In Figure 3, these energies are given by perimeters of subpolygons.


Figure 3: The contribution of a tree graph (or equivalently a triangulation) to the
wavefunction is determined by the bracketings of the graph (or equivalently the
Matryoshkas of the triangulation). Here _ki,j_ denotes the length between vertices _i_ and _j_,
which corresponds to the length of the momenta flowing through the edges of the graph,
and _P_ stands for the perimeter of the subpolygons entering the Matryoshka.


Written in terms of _ψ_, the Schr¨odinger equation turns into a simple recursion relation:
the contribution from a given graph can be computed by first writing a factor of the
inverse of the sum over all energies on the vertices, and then summing over all the ways
of deleting an edge from the graph, and adding the energy of the edge to the vertices
it connects to in the smaller graph with the edge deleted. We can run this recursion


7


until there are no more edges to be cut, and every term encountered corresponds to a
bracketing of the graph – where to each bracket subgraph we associate the factor given by
the total energy entering that subgraph. Phrased in the language of the triangulations,
each bracket corresponds to a sub-polygon in the triangulation, to which we associate
a factor given by its inverse perimeter. The terms contributing to the wavefunction are
then associated with a maximal collection of nested sub-polygons in the triangulation,
corresponding to a Matryoshka; see Figure 3.
Given the close connection between scattering amplitudes and cosmological correlators,
physics suggested that some analog of the associahedron must exist, capturing not
the combinatorics of all triangulations, but the factorially larger combinatorics of all
possible Matryoshkas. This was the motivation leading to the discovery and definition
of cosmohedra, which are polytopes precisely realizing this picture.
Our main goal in this paper is to better understand the combinatorics and geometry
of cosmohedra, provide proofs of many of their claimed properties, and also describe
them in a way that makes more natural contact with similar objects that have recently
been studied in combinatorics.


**1.6** **Outlook:** _X_ **in** _Y_ **polytopes** **and** **related** **constructions** **in** **physics**


Apart from its intrinsic mathematical interest, our treatment makes it clear that cosmohedra
belong to a wider class of objects whose relevance to physics should extend far beyond
cosmology. We will see that cosmohedra generalize to what we can call _X_ _in Y_ polytopes,
where we begin with a polytope _Y_ and “chisel” it in a way controlled by a family _X_
of polytopes to get a new _chiseled_ _polytope_ . At the level of fans, the normal fan of a
(simple) polytope _Y_ is canonically refined using the normal fans of the polytopes in _X_ .
We expect these _X_ in _Y_ polytopes to be relevant to many settings in physics, where,
in addition to summing over all diagrams, we must keep track of various properties of
subgraphs in each diagram.
An especially important example of this arises in the context of scattering amplitudes
beyond “tree” level. In diagrams with loops, the internal momenta are not determined
uniquely and must be integrated over. This is associated with a rich pattern of possible
divergences when loop momenta become large (“ultraviolet”) or small (“infrared”).
For an individual Feynman diagram, these divergences are controlled by the Newton
polytopes of certain graph polynomials – the so-called _Symanzik polynomials_ –associated
with the graph. In [AHCD [+] 24], all Feynman diagrams are naturally realized as cones
glued together into a complete “Feynman fan”, but this raises a question posed in

[AHCD [+] 24]: can the combinatorics of the “Symanzik polytopes” associated with any
graph be encoded in some way inside the full Feynman fan that glues all diagrams
together? This is exactly what _X_ in _Y_ polytopes allows us to do. In the Appendix,
we sketch this construction in the first interesting case: the Symanzik _U_ -polynomials at
one-loop level in the Tr( _ϕ_ [3] ) theory.


8


### **2 Matryoshkas, bracketed trees, and the cosmohedral fan**

**2.1** **Matryoshkas**


Consider a convex ( _n_ +2)-gon _P_ . A _subdivision_ _S_ is a set of sub-polygons whose union is
_P_ and whose interiors are pairwise disjoint. A subdivision _S_ can be naturally identified
with the corresponding set _C_ of non-crossing diagonals of _P_ . We say _S_ _refines_ _S_ _[′]_, and
write _S_ _≥S_ _[′]_, if the following three equivalent conditions hold: every polygon in _S_ is
contained in a polygon in _S_ _[′]_, every polygon in _S_ _[′]_ is a union of polygons in _S_, and the
corresponding sets of chords satisfy _C_ _⊇C_ _[′]_ .
A _Matryoshka_ or _Russian_ _doll_ _M_ is a set of sub-polygons of _P_ such that for any
non-minimal polygon _X_ in _M_, the maximal subpolygons ( _M<X_ )max of _X_ that are in
the Matryoshka _M_ subdivide _X_ . In particular, the set _M_ min of minimal polygons in _M_
form the _underlying_ _subdivision_ of _M_ . We say _M_ _refines_ _M_ _[′]_, and write _M_ _≥_ _M_ _[′]_, if the
sets of polygons satisfy _M_ _⊇_ _M_ _[′]_ .
For example, Figure 4 shows two maximal Matryoshkas _M_ 1 and _M_ 2 on a hexagon.
Removing a quadrilateral from _M_ 1 gives a Matryoshka smaller than it. Removing a
single triangle from _M_ 1 does not give a non-Matryoshka, because the corresponding
quadrilateral is not subdivided by its maximal subpolygons.


Figure 4: Two maximal Matryoshkas _M_ 1 and _M_ 2 on a hexagon.


Recursively, a Matryoshka is either:

_•_ _M_ = _{P_ _}_, the full polygon, or

_•_ _M_ = _S ∪_ [�] _S∈S_ _[M][S]_ [:] [a] [subdivision] _[S]_ [of] _[P]_ [and] [a] [Matryoshka] _[M][S]_ [on] [each] [part] _[S]_ [of] _[S]_ [.]


**Definition 2.1.** _The_ poset of Matryoshkas Mat _n−_ 1 _is the partially ordered set of Matryoshkas_
_on_ _the_ ( _n_ + 2) _-gon_ _ordered_ _by_ _containment,_ _with_ _an_ _additional_ _maximum_ _element_ 1 _._

[�]


**2.2** **The** **cosmohedral** **fan** **in** **terms** **of** **Matryoshkas**


Let us give the vertices of our ( _n_ +2)-gon _P_ = _n_ +2 the labels 0 _,_ 1 _, . . ., n_ +1 counterclockwise,
with the edge _e_ joining 0 and _n_ + 1 placed horizontally � at the top.
Consider a triangulation (or subdivision) _S_ of _P_ .

Triangle (or polygon) labels. We have a canonical labeling of the _n_ triangles of _S_ with the
vertex labels 1 _, . . ., n_ : We give the label _v_ to the first triangle of _S_ that one encounters


9


on a straight path from vertex _v_ to edge _e_ . (In a subdivision, a _k_ -gon gets _k −_ 2 such
labels.)

Diagonal labels. Each diagonal of _S_ separates two triangles labeled _v_ and _w_ (or polygons
labeled _V_ and _W_ ), with triangle _v_ between triangle _w_ and edge _e_ ; we give that diagonal
the label _vw_ _[⊥]_ (or _V W_ _[⊥]_ ).


Now consider a Matryoshka _M_ of _P_, with underlying triangulation (or subdivision) _S_ .
Polygon labels. Each diagonal _vw_ _[⊥]_ is contained inside a unique smallest polygon of
_M_, which we denote _M_ ( _vw_ _[⊥]_ ). When _M_ is maximal, this is a bijection between the
diagonals of _S_ and the�non-minimal polygons of _M_ .
Containment poset. The diagonals _vw_ _[⊥]_ are the elements of the _containment_ _poset_ _τ_
of _M_, whose order relations are given by containment of the corresponding polygons:
_ij_ _[⊥]_ _≥_ _kl_ _[⊥]_ if _M_ ( _ij_ _[⊥]_ ) _⊇_ _M_ ( _kl_ _[⊥]_ ). This poset is a tree, which is binary if _M_ is maximal.
Matryoshkal �cone. To the�Matryoshka _M_ we assign the cone

cone( _M_ ) = _{x ∈_ R _[n]_ : _xi −_ _xj_ _≥_ _xk −_ _xl_ _≥_ 0 when    - _M_ ( _ij_ _[⊥]_ ) _⊇_    - _M_ ( _kl_ _[⊥]_ ) _}_ (1)

naturally associated to the containment poset.


Figure 5: The Matryoshka _M_ 1 and its containment poset _τ_ 1.


**Example** **2.2.** _In_ _the_ _Matryoshka_ _M_ 1 _of_ _Figure_ _5_ _we_ _have_ (21 _[⊥]_ ) _⊂_ (32 _[⊥]_ ) _and_
(34 _[⊥]_ ) _⊂_ (32 _[⊥]_ ) _,_ _so_ cone( _M_ ) = _{x ∈_ R [4] : _x_ 3 _−_ _x_ 2 _≥{x_ 2 _−_ _x_ 1 _, x�_ 3 _−_ _x_ 4 _} ≥�_ 0 _}._

_�_ _�_

**Definition** **2.3.** _The_ cosmohedral fan _is_


CosmoFan _n−_ 1 = _{_ cone( _M_ ) : _M_ _is_ _a_ _Matryoshka_ _of_ _the_ ( _n_ + 2) _-gon}._


We will prove in Section 3 that this is indeed a fan, and that it has the desired
combinatorial structure:


**Theorem 2.4.** _The cosmohedral fan is a complete fan in_ R _[n]_ _._ _The map M_ _�→_ cone( _M_ ) _is_
_an_ _order-preserving_ _bijection_ _between_ _the_ _poset_ Mat _n−_ 1 _of_ _Matryoshkas_ _of_ _an_ ( _n_ +2) _-gon_
_and_ _the_ _face_ _lattice_ _L_ (CosmoFan _n−_ 1) _of_ _the_ _cosmohedral_ _fan._


10


**2.3** **Bracketed** **trees** **and** **the** **cosmohedral** **fan**


Let us give a different combinatorial description of Matryoshkas, which gives rise to a
description of the cosmohedral fan in terms of _bracketed_ _trees_ .


**2.3.1** **Preliminaries:** **plane** **trees,** **triangulations,** **and** **the** **associahedral** **fan.**


A _plane_ _tree_ is a rooted tree where the children of each node are linearly ordered from
left to right. The plane trees on _n_ +1 leaves form a poset Tree _n−_ 1 where _T_ _≤_ _T_ _[′]_ if _T_ can
be obtained from _T_ _[′]_ by contracting edges. We include an additional maximum element
�1 that makes this poset into a lattice.
The coatoms of this poset are the _binary_ _trees_, which have _n_ internal nodes and _n_ +1
leaves. It is sometimes convenient to erase the leaves of a binary tree, obtaining a plane
tree with _n_ vertices.
If _S_ is a subdivision of _n_ +2, then the _dual_ _graph_ _T_ ( _S_ ) has a vertex for each polygon
of _S_ and an edge between each pair of polygons that share an edge. � This is a tree rooted
at the polygon adjacent to the top edge _e_ . Figure 9 shows the binary trees dual to the
subdivisions of Matryoshkas _M_ 1 and _M_ 2.
If _S_ is a triangulation then _T_ ( _S_ ) is a binary tree, and this is a bijection between
the triangulations of _n_ +2 and the trees in Tree _n−_ 1; the number of such objects is the
Catalan number _Cn_ =� _n_ +11 �2 _nn_ �.
The internal vertices of a plane tree _T_ with _n_ + 1 leaves are naturally labeled with
sets that form a partition of [ _n_ ]: we give the gaps between the leaves the labels 1 _,_ 2 _, . . ., n_
from left to right, and label each internal node of _T_ with the gap(s) that are visible from
it. We regard _T_ as the Hasse diagram of a pre-poset on [ _n_ ] whose root is the maximum
element, and define


cone( _T_ ) = _{x ∈_ R _[n]_ _/_ R **1** : _xi_ _≥_ _xj_ for each _i ≥_ _j_ in _T_ int _}_


where **1** = (1 _, . . .,_ 1). In particular _xi_ = _xj_ in cone( _T_ ) whenever _i_ and _j_ label the same
vertex of _T_ .


**Definition** **2.5.** _The_ associahedral fan _is_


AssocFan _n−_ 1 = _{_ cone( _T_ ) : _T_ _is_ _a_ _plane_ _tree_ _on_ _n_ + 1 _leaves}._


Figure 6 shows the associahedral fan AssocFan3.


**Theorem 2.6.** _[Lod04] The associahedral fan_ AssocFan _n−_ 1 _is a complete fan in_ R _[n]_ _._ _The_
_map_ _T_ _�→_ cone( _T_ ) _is_ _an_ _order-preserving_ _bijection_ _between_ _the_ _poset_ Tree _n−_ 1 _of_ _plane_
_trees_ _with_ _n_ + 1 _leaves_ _and_ _the_ _face_ _lattice_ _L_ (AssocFan _n−_ 1) _of_ _the_ _associahedral_ _fan._


11


Figure 6: The three-dimensional associahedral fan.


**2.3.2** **Preliminaries:** **graph** **bracketings** **and** **bracket** **associahedral** **fans.**


Let _H_ = ( _V, E_ ) be a connected graph. A _bracket_ of _H_ is a connected subgraph of _H_
with at least one edge. We identify it with its set of edges. A _bracketing_ of _H_ is a
collection _B_ of brackets such that any two brackets are either nested (one is contained
in the other) or disjoint (they have no edges or vertices in common). We require every
bracketing to contain the full graph _H_ .
The _poset of bracketings_ Br( _H_ ) is the set of bracketings of _H_ ordered by containment,
with an additional maximum element 1.

[�]
In a bracketing _B_, each edge _e_ is contained in a unique smallest bracket of _B_, which
we denote bracket _B_ ( _e_ ) or simply bracket( _e_ ). This defines a pre-poset tree( _B_ ) on the edge
set _E_, where _e ≥B_ _f_ if _e_ is _outermore_ than _f_ in the sense that bracket( _e_ ) _⊇_ bracket( _f_ );
or equivalently, every bracket containing _e_ also contains _f_ . Because every bracket is
contained in a unique smallest bracket, the poset tree( _B_ ) is a tree rooted at a unique
maximal element. We obtain a cone


cone _H_ ( _B_ ) = _{y_ _∈_ R _[E]_ [(] _[H]_ [)] : _ye_ _≥_ _yf_ for each _e ≥B_ _f_ _}._


Its dimension is _|B|_ .


**Definition** **2.7.** _The_ bracket associahedral fan _of_ _a_ _graph_ _H_ _is_


BrAssocFan( _H_ ) = _{_ cone _H_ ( _B_ ) : _B_ _is_ _a_ _bracketing_ _of_ _H}_


Figure 7 illustrates the bracket associahedral fan of a path of length 4 with edges
_e, f, g_ . The fan is three-dimensional, with all cones containing the line _ye_ = _yf_ = _yg_, so
we display a 2-dimensional slice.


**Theorem** **2.8.** _[AHFV25,_ _CD06]_ _The_ _bracket_ _associahedral_ _fan_ BrAssocFan( _H_ ) _is_ _a_
_complete fan in_ R _[E]_ [(] _[H]_ [)] _._ _The map B_ _�→_ cone _H_ ( _B_ ) _is an order-preserving bijection between_


12


_the_ _poset_ _of_ _bracketings_ Br( _H_ ) _and_ _the_ _face_ _lattice_ _L_ (BrAssocFan( _H_ )) _of_ _the_ _bracket_
_associahedral_ _fan._


Figure 7: The bracket associahedral fan of a path.


Bracket associahedral fans and graph associahedral fans. The _line_ _graph_ _L_ ( _H_ ) of _H_ =
( _V, E_ ) is the graph of edge adjacencies of _H_ : it has a vertex for each edge _e_ of _H_, and
the vertices corresponding to edges _e, f_ are connected in _L_ ( _H_ ) if _e_ and _f_ share a vertex
in _H_ . The bracketings of _H_ are in order-preserving bijection with the tubings of _L_ ( _H_ )
in the sense of [CD06], so


_{_ bracket associahedral fans _}_ ⊊ _{_ graph associahedral fans _}._


Figure 8: Bracketings of _H_ correspond to tubings of _L_ ( _H_ ).


The graph associahedral fan of the claw _K_ 1 _,_ 3  - studied and depicted in [ARW06,
Figure 3] in its manifestation as the Dynkin diagram _D_ 4 - is a three-dimensional fan
with 10 rays, corresponding to the 10 tubes of the graph. The reader may verify that
this is the only graph on four vertices that has 10 tubes. Since the claw is not a line
graph, this is not a bracket associahedral fan. It is then natural to ask:


Which graph associahedral fans are bracket associahedral fans?


13


**2.3.3** **The** **cosmohedral** **fan** **in** **terms** **of** **bracketed** **trees.**


A _bracketed_ _tree_ ( _T, B_ ) consists of a plane tree _T_ and a bracketing _B_ of _T_ . Let us define
the cone of a bracketed tree ( _T, B_ ) with _n_ + 1 leaves to be


cone( _T, B_ ) = _{x ∈_ R _[n]_ : _xi −_ _xj_ _≥_ _xk −_ _xl_ _≥_ 0 when bracket _B_ ( _ij_ ) _⊇_ bracket _B_ ( _kl_ ) _}._


Note that the inequalities of cone( _T, B_ ) correspond to the order relations of the tree
poset tree( _B_ ), as illustrated in Figure 9.
The goal of this section is to show that the cones of the bracketed trees on _n_ + 1
leaves are precisely the cones of the cosmohedral fan CosmoFan _n−_ 1. We begin with a
technical lemma.


**Lemma** **2.9.** _For_ _any_ _bracketed_ _tree_ ( _T, B_ ) _we_ _have_


cone( _T, B_ ) _⊆_ cone( _T_ ) _,_ dim cone( _T, B_ ) = dim cone( _T_ ) = _|V_ ( _T_ ) _int|_ + 1 _._


_Proof._ The inclusion and the formula for dim cone( _T_ ) are clear from the definitions. To
prove that cone( _T, B_ ) has the same dimension, we first claim that for _x_ _∈_ cone( _T, B_ )
we have that _xi_ = _xj_ if _i_ and _j_ label the same vertex of _T_ . To see this, note that for an
offspring _k_ we have bracket _B_ ( _ik_ ) = bracket _B_ ( _jk_ ) so _xi −_ _xk_ = _xj −_ _xk_ (or analogously for
the parent _k_, if they do not have offspring). Setting these equalities aside, the remaining
inequalities of cone( _T, B_ ) are given by the acyclic poset tree( _B_ ), so they imply no further
equalities.


Figure 9: Two Matryoshkas, their corresponding bracketed trees, and their cones.


**The** **bijection** **with** **Matryoshkas.** For a Matryoshka _M_, let _S_ = _M_ min be the set of
inclusion-minimal polygons in _M_, which form the underlying subdivision of _M_ .


14


1. The _rooted_ _planar_ _tree_ _TM_ of _M_ is the dual graph of _S_, rooted at the top polygon
containing edge _e_ .


2. Each non-minimal polygon _P_ in _M_ is a disjoint union of minimal polygons in _M_ min,
whose dual graph is a bracket of the tree _TM_, denoted bracket( _P_ ). The _bracketing_
_BM_ of _M_ is _BM_ = _{_ bracket( _P_ ) : _P_ _∈_ _Mnot min}_ .


**Lemma** **2.10.** _The_ _map_ _M_ _�→_ ( _TM_ _, BM_ ) _is_ _a_ _bijection_ _between_ _the_ _Matryoshkas_ _on_ _an_
( _n_ + 2) _-gon_ _and_ _the_ _bracketed_ _trees_ BrTree _n−_ 1 _with_ _n_ + 1 _leaves._


_Proof._ The Matryoshka condition on _M_ implies that _BM_ is indeed a bracketing of _TM_ .
Conversely, for any pair ( _T, B_ ), the plane tree _T_ is dual to a subdivision _S_ of the
( _n_ + 2)-gon, and each bracket in _B_ is dual to a polygon _P_ that is the union of polygons
in _S_ . The bracketing condition on _B_ implies that these polygons form a Matryoshka.


**Lemma** **2.11.** _Under the bijection of Lemma 2.10,_ _the cone of the Matryoshka M_ _equals_
_the_ _cone_ _of_ _the_ _bracketed_ _tree_ ( _TM_ _, BM_ ) _:_


cone( _M_ ) = cone( _TM_ _, BM_ ) _._


_Proof._ This follows readily from the definitions.


**Corollary** **2.12.** _We_ _have_


CosmoFan _n−_ 1 = _{_ cone( _T, B_ ) : ( _T, B_ ) _is_ _a_ _bracketed_ _tree_ _with_ _n_ + 1 _leaves}._


**The** **poset** **of** **bracketed** **trees.** Consider a graph _G_ and a bracketing _B_ . If _β_ is a bracket
of _B_, the _deletion_ is the bracketing _B −_ _β_ is a bracketing of _G_ . If _µ_ is a minimal bracket
of _B_, the _contraction_ is the bracketing _B/µ_ := _{β_ _−_ _µ_ : _β_ _∈_ _B, β_ = _µ}_ of the tree
_T/µ_ where edge _µ_ is contracted - so the edge is deleted and its vertices are identified;
see Figure 10. If _E_ is a downset in (the tree pre-poset of) _B_, we can define _B/E_ by
successively contracting the brackets in _E_ in a non-decreasing order.


Figure 10: A contraction of a bracketing.


The _poset_ _of_ _bracketed_ _plane_ _trees_ with _n_ + 1 leaves, denoted BrTree _n−_ 1, is defined
by deletion and contraction as follows. Locally, we have a cover relation ( _T, B_ ) ⋖ ( _T_ _[′]_ _, B_ _[′]_ )
if either:
(i) _T_ = _T_ _[′]_ and _B_ = _B_ _[′]_ _−_ _β_ _[′]_ for a bracket _β_ _[′]_ of _B_ _[′]_, or
(ii) _T_ = _T_ _[′]_ _/µ_ _[′]_ and _B_ = _B_ _[′]_ _/µ_ _[′]_ for a minimal bracket _µ_ _[′]_ of _B_ _[′]_ .
Globally, we have a poset relation ( _T, B_ ) _≤_ ( _T_ _[′]_ _, B_ _[′]_ ) if _T_ = _T_ _[′]_ _/E_ for a set of edges _E_
that is a downset of the tree poset of _B_ _[′]_, and _B_ _⊆_ _B_ _[′]_ _/E_ . We augment this poset with
a maximum element 1.

[�]


15


**Proposition 2.13.** _The bijection M_ _�→_ ( _TM_ _, BM_ ) _of Lemma 2.10, is a poset isomorphism_
_between_ _the_ _lattice_ _of_ _Matryoshkas_ Mat _n_ +2 _and_ _the_ _poset_ _of_ _bracketed_ _trees_ BrTree _n−_ 1 _._


_Proof._ In a cover relation _M_ ⋖ _M_ _[′]_ of Matryoshkas, _M_ is obtained from _M_ _[′]_ by either:
(i) removing a non-minimal polygon _P_, which corresponds to leaving _TM_ = _TM_ _′_ fixed
and making _BM_ = _BM_ _′_ _−_ bracket( _P_ ), or
z (ii) removing the minimal polygons _P_ 1 _, . . ., Pk_ that subdivided a next-to-minimal
polygon _P_ in _M_ _[′]_, so _P_ becomes minimal in _M_ ; this corresponds to contracting the
minimal bracket( _P_ ) to get ( _TM_ _, BM_ ) = ( _TM_ _′/_ bracket( _P_ ) _, BM_ _′/_ bracket( _P_ )).
This proves the poset isomorphism.

### **3 Proof of correctness of the cosmohedral fan**


**3.1** **Positive** **bracket** **associahedral** **fans**


The _positive_ _bracket_ _associahedral_ _fan_ of a graph _H_ is the intersection


BrAssocFan _≥_ 0( _H_ ) = BrAssocFan( _H_ ) _∩_ R _[E]_ _≥_ 0 [(] _[H]_ [)]


of the bracket associahedral fan with the positive orthant, with the inherited polyhedral
structure.


Figure 11: The positive bracket associahedral fan of a path.


**Example** **3.1.** _Figure_ _11_ _illustrates_ _the_ _positive_ _bracket_ _associahedral_ _fan_ _of_ _a_ _path_ _of_
_length_ _4_ _with_ _edges_ _e, f, g;_ _it_ _is_ _the_ _intersection_ _of_ _Figure_ _7_ _–_ _which_ _we_ _should_ _recall_
_is_ _three-dimensional_ _–_ _with_ _the_ _positive_ _orthant._ _The_ _maximal_ _cones_ _are_ _in_ _bijection_
_with_ _those_ _of_ _Figure_ _7,_ _but_ _there_ _are_ _new_ _lower-dimensional_ _cones,_ _corresponding_ _to_ _the_


16


_bracketings B_ _of the contractions G of the path._ _We label a few of the faces with a picture_
_of_ _the_ pre-bracketing ( _G, B_ ) _,_ _and_ _with_ _the_ _list_ _B_ _of_ _brackets,_ _which_ _is_ _enough_ _to_ _recover_
_G._ _We_ _now_ _prove_ _this_ _description_ _holds_ _in_ _general._


A _pre-bracketing_ is a bracketing of a contraction of _H_ ; that is, a pair ( _G, B_ ) consisting
of a contraction _G_ of _H_ and a bracketing _B_ of _G_ . When _H_ is fixed, we simply write _B_
instead of ( _G, B_ ), since _G_ is determined automatically as the maximum bracket in _B_ .
The _poset_ _of_ _pre-bracketings_ PreBr( _H_ ) is again defined by deletion and contraction:
_B_ ⋖ _B_ _[′]_ if _B_ is obtained from _B_ _[′]_ by either (i) removing a bracket or (ii) contracting a
minimal bracket.
We define the _positive_ _cone_ _of_ _a_ _pre-bracketing_ _B_ of _H_ to be


cone _H_ ( _B_ ) _≥_ 0 = _{y_ _∈_ R _[E]_ [(] _[H]_ [)] : _ye_ _≥_ _yf_ _≥_ 0 for each _e ≥B_ _f,_ _ye_ = 0 for each _e_ contracted _}._


**Proposition** **3.2.** _For_ _any_ _graph_ _H,_ _the_ _map_ _B_ _�→_ cone _H_ ( _B_ ) _≥_ 0 _is_ _an_ _order-preserving_
_bijection_ _between_ _the_ _poset_ PreBr( _H_ ) _of_ _pre-bracketings_ _of_ _H_ _and_ _the_ _face_ _lattice_
_L_ (BrAssocFan _≥_ 0( _H_ )) _of_ _the_ _positive_ _bracket_ _associahedral_ _fan_ _of_ _H._


_Proof._ A face of the positive bracket associahedral fan is obtained by intersecting a face
cone _H_ ( _B_ ) of BrAssocFan( _H_ ) for a bracketing _B_ with a face R _[E]_ _≥_ 0 [of] [R] _[E]_ _≥_ 0 [(] _[H]_ [)] for a subset
_E_ _⊆_ _E_ ( _H_ ). Imposing the equations _yf_ = 0 for _f_ _∈/_ _E_ on cone _H_ ( _B_ ) also implies _yf_ _′_ = 0
for any _f_ _[′]_ _<B_ _f_ ; so if we let _F_ be the downset of (the tree poset of) _B_ generated by
_F_ = _E_ ( _H_ ) _−_ _E_, then
cone _H_ ( _B_ ) _∩_ R _[E]_ _≥_ 0 [= cone] _[H]_ [(] _[B/F]_ [)] _[≥]_ [0] _[.]_ (2)


Every pre-bracketing of _H_ arises in this way, proving the description of the cones of
BrAssoc _≥_ 0( _H_ ).
Now, for a pre-bracketing _B_ of _H_, a facet of cone _H_ ( _B_ ) _≥_ 0 is obtained by either (i)
setting _ye_ = _yf_ for _e_ ⋗ _f_ in tree( _B_ ), which has the effect of deleting the bracket of _f_,
or (ii) setting _yf_ = 0 for a minimal _f_ in tree( _B_ ), which has the effect of contracting the
bracket of _f_ . The poset isomorphism follows.


**3.2** **The** **cosmohedral** **fan** **and** **positive** **bracket** **associahedral** **fans**


Now we describe the cosmohedral fan in terms of positive bracket associahedral fans.


**Lemma** **3.3.** _Let_ _T_ _be_ _a_ _plane_ _rooted_ _tree_ _with_ _n_ + 1 _leaves,_ _whose_ _internal_ _vertices_ _are_
_canonically_ _labelled_ _by_ [ _n_ ] _._ _Label_ _each_ _edge_ _in_ _the_ _order_ _ij_ _where_ _i_ _is_ _closer_ _to_ _the_ _root_
_than_ _j._ _We_ _have_ _inverse_ _maps:_


_∼_ = _∼_ =
_fT_ : R _[E]_ [(] _[T]_ [)] _−→_ R _[n]_ _/_ R **1** _fT_ _[−]_ [1] : R _[n]_ _/_ R **1** _−→_ R _[E]_ [(] _[T]_ [)]


   _eij_ _�−→_ _ek_ + R ( _xv_ ) _v∈V_ ( _T_ ) + R **1** _�−→_ ( _xi −_ _xj_ ) _ij∈E_ ( _T_ ) _._

_k∈_ ( _T_ _−ij_ ) _i_


_where_ ( _T −ij_ ) _i_ _and_ ( _T −ij_ ) _j_ _are the connected components of the forest T −ij_ _containing_
_i_ _and_ _j_ _respectively._ _Furthermore,_


17


_∼_ =
_1._ _the_ _map_ _fT_ : R _[E]_ [(] _[T]_ [)] _−→_ R _[n]_ _/_ R **1** _is_ _an_ _isomorphism_ _of_ _vector_ _spaces,_


_∼_ =
_2._ _the_ _restriction_ _fT_ : R _[E]_ _≥_ 0 [(] _[T]_ [)] _−→_ cone( _T_ ) _is_ _an_ _isomorphism_ _of_ _cones,_ _and_


_∼_ =
_3._ _the_ _restriction_ _fT_ : cone _T_ ( _B_ ) _≥_ 0 _−→_ cone( _T, B_ ) _is_ _an_ _isomorphism_ _of_ _cones_ _for_ _any_
_bracketing_ _B_ _of_ _tree_ _T_ _._


_∼_ =
_4._ _the_ _restriction_ _fT_ : cone _T_ ( _B_ ) _≥_ 0 _−→_ cone( _T_ ( _B_ ) _, B_ ) _is_ _an_ _isomorphism_ _of_ _cones_ _for_
_any_ _pre-bracketing_ _B_ _of_ _tree_ _T_ _,_ _where_ _T_ ( _B_ ) _≤_ _T_ _is_ _the_ _tree_ _supporting_ _B._


_Proof._ First, we check that these maps are indeed inverse to each other. For each basis
vector _eij_ corresponding to edge _ij_ of _T_, the vector _fT_ ( _eij_ ) has coordinates equal to 1
on component ( _T_ _−_ _ij_ ) _i_ and 0 on component ( _T_ _−_ _ij_ ) _j_ . Therefore _fT_ _[−]_ [1][(] _[f][T]_ [ (] _[e][ij]_ [))] [is] [only]
non-zero on the edge _ij_ - whose vertices lie in different components - where it equals 1.
Thus _fT_ _[−]_ [1][(] _[f][T]_ [ (] _[e][ij]_ [))] [=] _[e][ij]_ [indeed.] [Since] [both] [spaces] [are] [(] _[n][ −]_ [1)-dimensional,] [this] [means]
_fT_ is an isomorphism and _fT_ _[−]_ [1] is its inverse, proving 1.
To show 2, notice that _y_ = _fT_ _[−]_ [1][(] _[x]_ [)] [is] [nonnegative] [if] [and] [only] [if] _[x]_ [satisfies] [the]
inequalities of cone( _T_ ). For 3., observe that _y_ satisfies the additional inequalities _yij_ _≥_
_ykl_ _≥_ 0 of cone _T_ ( _B_ ) _≥_ 0 if and only if _x_ satisfies the inequalities _xi −_ _xj_ _≥_ _xk −_ _xl_ _≥_ 0 of
cone( _T, B_ ) for _ij_ _≥B_ _kl_ . For 4. notice that _y_ satisfies _yij_ = 0 for each contracted edge
_ij_ if and only if _x_ satisfies _xi_ = _xj_ when _i_ and _j_ label the same vertex in _T_ ( _B_ ); these
are precisely the equalities that hold in cone( _T_ ( _B_ ) _, B_ ), as we explained in the proof of
Lemma 2.9.


**Example** **3.4.** _Consider_ _the_ _Matryoshka_ _M_ 1 _and_ _its_ _corresponding_ _tree_ _T_ 1 _with_ _edges_
_e_ = 21 _, f_ = 32 _, g_ = 34 _,_ _and_ _bracketing_ _B_ 1 = _{e, efg, g},_ _as_ _shown_ _in_ _Figure_ _9._ _Then_

cone _T_ 1( _B_ 1) _≥_ 0 = _{y_ _∈_ R _[efg]_ : _yf_ _≥{ye, yg} ≥_ 0 _} ⊂_ R _[E]_ [(] _[T]_ [)] _,_


_and_ _its_ _image_ _under_ _the_ _map_ _fT_ 1 _is_

cone( _T_ 1 _, B_ 1) = _{x ∈_ R [4] _/_ R **1** : _x_ 3 _−_ _x_ 2 _≥{x_ 2 _−_ _x_ 1 _, x_ 3 _−_ _x_ 4 _} ≥_ 0 _} ⊂_ R _[n]_ _/_ R **1**


_as_ _illustrated_ _in_ _Figure_ _12._


For the moment, we only know CosmoFan _n−_ 1 to be the set of Matryoshkal cones.
Our next goal is to show that it is indeed a polyhedral fan, with the correct combinatorial
structure. We begin with a simple technical lemma.


**Corollary** **3.5.** _We_ _have_


        CosmoFan _n−_ 1 = _fT_ (BrAssocFan _≥_ 0( _T_ ))


_T_


_where_ _the_ _union_ _is_ _over_ _all_ _binary_ _trees_ _T_ _with_ _n_ + 1 _leaves._


_Proof._ Any cone of CosmoFan _n−_ 1 is of the form cone( _M_ ) = cone( _T, B_ ) for a bracketed
tree ( _T, B_ ). If we choose any binary _T_ [+] _≥_ _T_, then _B_ is a pre-bracketing of _T_ [+], and
Lemma 3.3.4 shows that this cone is in _fT_ +(BrAssocFan _≥_ 0( _T_ [+] )).


Notice in particular that the union above is not disjoint.


18


Figure 12: The linear map _fT_ 1 embeds the four-sided cone _T_ 1( _B_ 1) _≥_ 0 of BrAssocFan _≥_ 0( _T_ 1)
in Figure 11 into the cone( _T_ 1) of Assoc _n−_ 1 in Figure 6. The result is the cone
_fT_ 1(cone _T_ 1( _B_ 1) _≥_ 0) = cone( _T_ 1 _, B_ 1) of Cosmo _n−_ 1.


**3.3** **The** **cosmohedral** **fan** **is** **a** **complete** **fan**


**Theorem** **3.6.** _The_ _cosmohedral_ _fan_ CosmoFan _n−_ 1 _is_ _a_ _complete_ _fan_ _in_ R _[n]_ _/_ R **1** _._ _The_
_map_ _M_ _�→_ cone( _M_ ) _is_ _an_ _order-preserving_ _bijection_ _between_ _the_ _Matryoshkas_ _of_ _an_
( _n_ + 2) _-gon_ _and_ _the_ _faces_ _of_ CosmoFan _n−_ 1 _._


_Proof._ To prove that the cones intersect properly, let us first analyze how a Matryoshkal
cone( _T_ 1 _, B_ 1), which sits in an associahedral cone( _T_ 1) of the same dimension, intersects
a smaller associahedral cone( _T_ ) _⊆_ cone( _T_ 1). Consider any maximal _T_ [+] _≥_ _T_ 1. Then _B_ 1
is a pre-bracketing of _T_ [+] and we have


cone( _T_ 1 _, B_ 1) _∩_ cone( _T_ ) = _fT_ +(cone _T_ +( _B_ 1) _≥_ 0) _∩_ _fT_ +(R _[E]_ _≥_ 0 [(] _[T]_ [)] )

= _fT_ +(cone _T_ +( _B_ 1) _≥_ 0 _∩_ R _[E]_ _≥_ 0 [(] _[T]_ [)] )

= _fT_ +(cone _T_ +( _B_ 1 _/F_ ) _≥_ 0) for _F_ = _E_ ( _T_ [+] ) _−_ _E_ ( _T_ ) _,_ by (2)

= cone( _T_ 1 _[′][, B]_ 1 _[′]_ [)] for _B_ 1 _[′]_ [=] _[ B]_ [1] _[/F]_


where _T_ 1 _[′]_ [=] _[ T]_ [ +] _[/F]_ [=] _[ T/]_ [(] _[F]_ _[−]_ _[F]_ [)] _[ ≤]_ _[T]_ [is] [the] [tree] [supporting] _[B]_ 1 _[′]_ [.]
For example, in the top row of Figure 13 we compute cone( _M_ 1) _∩_ cone( _T_ ) for the
Matryoshka _M_ 1 = ( _T_ 1 _, B_ 1) of Figure 9 and the tree _T_ of the shown subdivision. Here
_T_ [+] = _T_ 1, _F_ = _E_ ( _T_ [+] ) _−_ _E_ ( _T_ ) = _{_ 21 _}_, and the downset in _τ_ 1 is _F_ = _F_ = _{_ 21 _}_ . Thus
we obtain ( _T_ 1 _[′][, B]_ 1 _[′]_ [)] [by] [contracting] [edge] [21] [from] [(] _[T]_ [1] _[, B]_ [1][).] [The] [resulting] [inequalities] [are]
_x_ 3 _−_ _x_ 21 _≥_ _x_ 3 _−_ _x_ 4 _≥_ 0, where _x_ 21 denotes the common value of _x_ 2 = _x_ 1. In the second
row we compute cone( _M_ 2) _∩_ cone( _T_ ) similarly.
Now consider two Matryoshkas _M_ 1 = ( _T_ 1 _, B_ 1) and _M_ 2 = ( _T_ 2 _, B_ 2). Their cones


19


Figure 13: The intersection of the two Matryoshkal cones _M_ 1 and _M_ 2 described in
Figure 9. We begin by computing _T_ = _T_ 1 _∧_ _T_ 2 and use it to find _T_ 1 _[′][, T]_ 2 _[ ′]_ [and the inherited]
bracketings _B_ 1 _[′]_ [and] _[B]_ 2 _[′]_ [.] [From] [there] [we] [find] _[B][′]_ [=] _[ B]_ 1 _[′]_ _[∧]_ _[B]_ 2 _[′]_ [.] [Then] _[M]_ _[′]_ [is] [the] [Matryoshka]
of _T_ _[′]_ and _B_ _[′]_ .


intersect inside cone( _T_ 1) _∩_ cone( _T_ 2) = cone( _T_ ) where _T_ = _T_ 1 _∧_ _T_ 2 in Tree _n−_ 1. Then


cone( _M_ 1) _∩_ cone( _M_ 2) = (cone( _T_ 1 _, B_ 1) _∩_ cone( _T_ )) _∩_ (cone( _T_ 2 _, B_ 2) _∩_ cone( _T_ ))

= cone( _T_ 1 _[′][, B]_ 1 _[′]_ [)] _[ ∩]_ [cone(] _[T][ ′]_ 2 _[, B]_ 2 _[′]_ [)] [where] _[T][ ′]_ 1 _[, T]_ 2 _[ ′]_ _[≤]_ _[T]_

= _fT_ +(cone _T_ +( _B_ 1 _[′]_ [)] _[≥]_ [0] _[∩]_ [cone] _T_ [+][(] _[B]_ 2 _[′]_ [)] _[≥]_ [0][)] for any maximal _T_ [+] _≥_ _T_

= _fT_ +(cone _T_ +( _B_ _[′]_ ) _≥_ 0) for _B_ _[′]_ = _B_ 1 _[′]_ _[∧]_ _[B]_ 2 _[′]_ [,] [by] [Proposition] [3.2]

= cone( _M_ _[′]_ ) for the Matryoshka _M_ _[′]_ of ( _T_ _[′]_ _, B_ _[′]_ )


where _T_ _[′]_ _≤_ _T_ [+] is the tree supporting _B_ _[′]_ = _B_ 1 _[′]_ _[∧]_ _[B]_ 2 _[′]_ [.]
In the third row of Figure 13 we compute cone( _M_ 1) _∩_ cone( _M_ 2) for the Matryoshkas of
Figure 9, noticing that the tree we had considered is _T_ = _T_ 1 _∧T_ 2. Considering _B_ 1 _[′]_ [and] _[ B]_ 2 _[′]_
as pre-bracketings of any maximal tree _T_ [+] _≥_ _T_ we compute their meet _B_ _[′]_ = _B_ 1 _[′]_ _[∧][B]_ 2 _[′]_ [and]
obtain from it the tree _T_ _[′]_ and the inequalities of the intersection, _x_ 3 _−_ _x_ 12 = _x_ 3 _−_ _x_ 4 _≥_ 0;
that is, the ray _x_ 3 _≥_ _x_ 124 in R [4] _/_ R.
To prove that the fan is complete, we begin with the fact that the maximal tree
cones cone( _T_ ) of the associahedral fan cover R _[n]_ _/_ R **1** . Now, for each _T_, the cones
cone _T_ ( _B_ ) _≥_ 0 of the pre-bracketing fan cover the positive orthant R _[E]_ _≥_ 0 [(] _[T]_ [)], so their images

_fT_ (cone _T_ ( _B_ ) _≥_ 0) = cone( _T_ ( _B_ ) _, B_ ) cover _fT_ (R _[E]_ _≥_ 0 [(] _[T]_ [)] ) = cone( _T_ ).
Finally, let us prove the poset isomorphism, keeping in mind that we already showed
that Mat _n_ +2 = _[∼]_ BrTree _n_ +1. Clearly _M_ 1 _⊆_ _M_ 2 implies cone( _M_ 1) _⊆_ cone( _M_ 2). Assume
that cone( _M_ 1) = cone( _T_ 1 _, B_ 1) _⊆_ cone( _T_ 2 _, B_ 2) = cone( _M_ 2). Let _T_ be a maximal tree
such that cone( _T_ ) contains these cones; _B_ 1 and _B_ 2 are pre-bracketings of _T_ . Then
_fT_ (cone _T_ ( _B_ 1) _≥_ 0) = cone( _T_ 1 _, B_ 1) = cone( _T_ 2 _, B_ 2) _⊆_ _fT_ (cone _T_ ( _B_ 2) _≥_ 0) by Lemma 3.3 so
cone _T_ ( _B_ 1) _≥_ 0 _⊆_ cone _T_ ( _B_ 2) _≥_ 0 which means that _B_ 1 _≤_ _B_ 2 in PreBr( _T_ ) by Proposition
3.2. Therefore ( _T_ 1 _, B_ 1) _⊆_ ( _T_ 2 _, B_ 2) in BrTree _n−_ 1, which means that _M_ 1 _≤_ _M_ 2 in Mat _n−_ 1
by Proposition 2.13.


20


### **4 The cosmohedron**

In this section, we define the cosmohedron Cosmo _n−_ 1(a _,_ b) and prove that its normal fan
is the cosmohedral fan CosmoFan _n−_ 1.
To set conventions, let _e_ 1 _, . . ., en_ be the standard basis of R _[n]_ . Let us write _i_ _<<_ _j_,
when integers _i < j_ are not consecutive, that is, _|j −_ _i| >_ 1. We note that the set of pairs
( _i, j_ ) with 0 _≤_ _i << j_ _≤_ _n_ +1 is in bijection with the set diag [+] ( _n_ +2) = diag( _n_ +2) _∪{e}_
of diagonals augmented with the base edge _e_ . - 

**4.1** **Preliminaries:** **Associahedra** **and** **bracket** **associahedra**


**Loday’s** **associahedron.** Given a sequence of positive numbers a = ( _aij_ )0 _≤i<<j≤n_ +1, the
_Loday_ _associahedron_ is


    Loday _n−_ 1(a) = _aij_ ∆( _i,j_ ) (3)

0 _≤i<<j≤n_ +1




  = _{x ∈_ R _[n]_ :



_aij,_

0 _≤i<<j≤n_ +1




- 
_xi_ =

1 _≤i≤n_ 0 _≤i<<j_




- 
_xi_ _≥_

_r≤i≤s_ _r−_ 1 _≤i<<j_







_aij_ for 1 _≤_ _r_ _≤_ _s ≤_ _n.}_ (4)

_r−_ 1 _≤i<<j≤s_ +1



where ∆( _i,j_ ) = ∆[ _i_ +1 _,j−_ 1] = conv( _ei_ +1 _, . . ., ej−_ 1) is a face of the standard simplex in R _[n]_,
and _P_ + _Q_ = _{p_ + _q_ : _p ∈_ _P, q_ _∈_ _Q}_ denotes Minkowski sum of polytopes. [1]


**Theorem** **4.1.** _[AA23,_ _Pos09]_ _The_ _normal_ _fan_ _of_ _the_ _associahedron_ Loday _n−_ 1(a) _is_ _the_
_associahedral_ _fan_ AssocFan _n−_ 1 _._


Let _S_ be a triangulation of _n_ +2 corresponding to the binary tree _T_ . It will be
useful to express the vertex _aT_ of� Loday’s associahedron in terms of _S_ . To do so, say
that diagonal _ij_ _transversally_ _crosses_ the triangle labeled _v_ with vertices _u_ _<_ _v_ _<_ _w_ if
it intersects edges _uv_ and _vw_, not at _v_ . This is equivalent to _u ≤_ _i < v_ _< j_ _≤_ _w_ . When
this is the case we write _ij_ _→_ _v_ . We invite the reader to check that each diagonal of the
polygon crosses exactly one triangle of the triangulation _S_ transversally.


**Lemma 4.2.** _[Lod04, Pos09] The vertex aS_ _of_ Loday _n−_ 1(a) _corresponding to a triangulation_
_S_ _of_ _n_ +2 _has_ _coordinates_

       
_�_ ( _aS_ ) _v_ = _aij_


_ij→v_ _in_ _S_


_summing over the extended diagonals ij_ _∈_ diag [+] ( _n_ +2) _that cross triangle v transversally._

_�_

_Proof._ The vertex _aT_ of Loday _n−_ 1(a) corresponding to a binary tree _T_ has coordinates


     ( _aT_ ) _v_ = _ai−_ 1 _,j_ +1 for _v_ _∈_ [ _n_ ]

_i∨j_ = _v_ in _T_


1It is more customary to choose _α_ = ( _αij_ )1 _≤i≤j≤n_ and write [�] _i≤j_ _[α][ij]_ [∆][[] _[i,j]_ []] [for Loday’s associahedron;]

we use _ai−_ 1 _,j_ +1 = _αij_ instead.


21


where _i ∨_ _j_ is the lowest common ancestor of _i_ and _j_ ; this is implicit in [Lod04, Pos09]
see for example [AA23, Figure 6]. The second statement then follows readily from the
bijection.


**Devadoss’s** **bracket** **associahedron** . For a graph _H_, let b : Brackets( _H_ ) _→_ Z be any
function that is _concave_ in the sense that _b_ ( _β_ 1) + _b_ ( _β_ 2) _> b_ ( _β_ 1 _∩_ _β_ 2) + _b_ ( _β_ 1 _∪_ _β_ 2) for any
intersecting brackets _β_ 1 and _β_ 2. For example, _b_ ( _β_ ) can be any concave function of the
number of edges _|β|_ = _k_ ; that is, _b_ ( _k_ ) _>_ [1]

2 [(] _[b]_ [(] _[k][ −]_ [1) +] _[ b]_ [(] _[k]_ [ + 1)).]


**Definition** **4.3.** _The_ Devadoss bracket associahedron _of_ _a_ _graph_ _H_ _is_


      BrAssoc _H_ (b) = _{y_ _∈_ R _[E]_ [(] _[H]_ [)] : _ye_ = _b_ ( _H_ ) _,_


_e∈E_ ( _H_ )


      
_ye_ _≤_ _b_ ( _β_ ) _for_ _all_ _brackets_ _β_ _of_ _H}._ (5)

_e∈β_


**Theorem 4.4.** _[Dev09, PPP23] The normal fan of the bracket associahedron_ BrAssoc _H_ b
_is_ _the_ _bracket_ _associahedral_ _fan_ _of_ _H._


We remark that Devadoss [Dev09] works with the sequence _b_ ( _β_ ) = _−_ 3 _[|][β][|−]_ [2]  - see
Lemma 5.2 - but in fact Theorem 4.4 holds precisely for concave sequences. To see
this, we use Padrol, Pilaud, and Poullot’s description [PPP23, Corollary 2.12] of the
deformation cone of graph associahedral fans, and in particular bracket associahedral
fans. This cone is given by the equality _b_ ( _G_ ) = 0 and inequalities _b_ ( _β −_ _e_ ) + _b_ ( _β −_ _e_ _[′]_ ) _<_
_b_ ( _β_ ) + _b_ ( _β −_ _e −_ _e_ _[′]_ ) for any bracket _β_ and any non-disconnecting edges _e, e_ _[′]_ of _β_ . This
is equivalent to the concavity condition above. [2]


**Lemma** **4.5.** _Let_ b : Brackets( _H_ ) _→_ R _be_ _concave._ _The_ _vertex_ _bB_ _of_ BrAssoc _H_ (b)
_associated_ _to_ _a_ _maximal_ _bracketing_ _B_ _of_ _H_ _is_ _given_ _by_


      ( _bB_ ) _e_ = _b_ (bracket( _e_ )) _−_ _b_ (bracket( _f_ )) _for_ _e ∈_ _E_ ( _H_ ) _,_ (6)


_f_ ⋖ _e_


_summing_ _over_ _the_ _edges_ _f_ _that_ _e_ _covers_ _in_ tree( _B_ ) _._


In a maximal bracketing, each bracket contains one or two maximal sub-brackets, so
the expression above has at most three terms.


_Proof._ For each maximal bracketing _B_, we can compute the entries of vertex _bB_ recursively
by ( _bB_ ) _e_ = _b_ ( _e_ ) for any edge _e_ that is a bracket, and [�] _e∈β_ [(] _[b][B]_ [)] _[e]_ [=] _[ b]_ [(] _[β]_ [) for every bracket] _[ β]_
of _B_ . In the tree of _B_, this says _b_ (bracket( _e_ )) = [�] _f_ _≤e_ [(] _[b][B]_ [)] _[e]_ [.] [Adding a minimum element]
�0 with _b_ (�0) = _bB_ (�0) = 0, and applying M¨obius inversion in the poset tree( _B_ ) _∪_ �0, we get
( _bB_ ) _e_ = [�] _f_ _≤e_ _[µ]_ [(] _[f, e]_ [)] _[ b]_ [(bracket(] _[f]_ [))] [Since] [the] [interval] [[] _[f, e]_ []] [is] [a] [path,] _[µ]_ [(] _[f, e]_ [)] [equals] [1] [if]
_f_ = _e_, it equals _−_ 1 if _f_ ⋖ _e_, and it is 0 otherwise; so (6) does indeed describe Devadoss’s
bracket associahedron.


2Padrol, Pilaud, and Poullot require _b_ ( _G_ ) = 0, but we can remove this condition by a suitable
translation. For general graphs, some care is required when _β −_ _e −_ _e_ _[′]_ is disconnected, but this does not
happen for trees.


22


Slightly differently, we will work with the _extended_ _set_ _of_ _brackets_ Brackets [+] ( _H_ ) =
Brackets( _H_ ) _∪_ _V_ ( _H_ ), including also a _small_ _bracket_ around each individual vertex.
Consider any concave function b : Brackets [+] ( _T_ ) _→_ Z; in the concavity condition, if
_β_ 1 _∩_ _β_ 2 is an edge-less graph on vertices _v_ 1 _, . . ., vk_, we set _b_ ( _β_ 1 _∩_ _β_ 2) = _b_ ( _v_ 1)+ _· · ·_ + _β_ ( _vk_ ).
The function b induces a concave function b _[−]_ : Brackets( _H_ ) _→_ Z defined by


       _b_ _[−]_ ( _β_ ) = _b_ ( _β_ ) _−_ _b_ ( _v_ ) _,_ (7)


_v∈V_ ( _β_ )


whose bracket associahedron we now describe. A bracketing _B_ of _H_ now gives an
_extended_ tree [+] ( _B_ ) that also includes the small brackets.


**Lemma** **4.6.** _Let_ b : Brackets [+] ( _H_ ) _→_ R _be_ _concave_ _and_ b _[−]_ : Brackets( _H_ ) _→_ R _be_ _given_
_by_ (7) _._ _The_ _vertex_ _bB_ _of_ BrAssoc _H_ (b _[−]_ ) _associated_ _to_ _a_ _maximal_ _bracketing_ _B_ _of_ _H_ _is_
_given_ _by_

      ( _bB_ ) _e_ = _b_ (bracket( _e_ )) _−_ _b_ (bracket( _f_ )) _for_ _e ∈_ _E_ ( _H_ ) _._ (8)


_f_ ⋖ _e_


_summing_ _over_ _the_ _edges_ _f_ _that_ _e_ _covers_ _in_ _the_ _extended_ tree [+] ( _B_ ) _._


_Proof._ This follows by applying Lemma 4.5 to b _[−]_ .


**4.2** **The** **cosmohedron**


In this section we construct a _cosmohedron_ : a polytope Cosmo _n−_ 1(a _,_ b) whose normal
fan is the cosmohedral fan CosmoFan _n−_ 1. We first give two vertex descriptions of
Cosmo _n−_ 1(a _,_ b) and use them to prove that it has the correct normal fan. We then
use the normal fan to compute the inequality description of Cosmo _n−_ 1(a _,_ b). Finally,
we use those inequalities to prove that Cosmo _n−_ 1(a _,_ b) is linearly isomorphic to the
cosmohedron proposed by Arkani-Hamed, Figueiredo, and Vaz˜ao [AHFV25]. This gives
a proof of the correctness of their construction.
Recall that diag [+] ( _n_ +2) = diag( _n_ +2) _∪_ _e_ is the set of diagonals of the ( _n_ + 2)-gon
augmented with the base� _e_ . We say a function� b = ( _b_ ( _P_ ) : _P_ is a subpolygon of _n_ +2) _∈_

R [(] _[n]_ _≥_ [+2] 3 [)] is _concave_ if _b_ ( _P_ 1)+ _b_ ( _P_ 2) _> b_ ( _P_ 1 _∩_ _P_ 2)+ _b_ ( _P_ 1 _∪_ _P_ 2) whenever the intersection and�
union are also subpolygons. An example is a concave function of the number of vertices
of the polygon.



Throughout this section, we fix:

_•_ an arbitrary positive vector a = ( _aij_ : _ij_ _∈_ diag [+] ( _n_ +2)) _∈_ R [diag][+][(][�] _[n]_ [+2][)] _[∼]_ = R [(] _[n]_ [+1] 2 [)],

_•_ a concave vector b = ( _b_ ( _P_ ) : _P_ is a subpolygon of� ) _∈_ R [(] _[n]_ _≥_ [+2] 3 [)],




_•_ a concave vector b = ( _b_ ( _P_ ) : _P_ is a subpolygon of _n_ +2) _∈_ R [(] _[n]_ _≥_ [+2] 3 [)],

_m_

_•_ a small constant 0 _< ε <_ [where] _[m]_ [ = min] _[ a]_ [and] - _[M]_ [= max] _[ |][b]_ [(]




_•_ a small constant 0 _< ε <_ 24 _mM_ [where] _[m]_ [ = min] _[ a][ij]_ [and] _[M]_ [= max] _[ |][b]_ [(] _[P]_ [)] _[|]_ [.]
The cosmohedron Cosmo _n−_ 1(a _,_ b) is constructed from those choices.



23


**4.2.1** **Vertex** **description**


For a rooted plane tree _T_ let



_f_ _[T]_ : R _[E]_ [(] _[T]_ [)] _−→_ R _[V]_ 0 [ (] _[T]_ [)]
_eij_ _�−→_ _ei −_ _ej_


be the isomorphism between R _[E]_ [(] _[T]_ [)] and R _[V]_ 0 [ (] _[T]_ [)] := _{x_ _∈_ R _[V]_ [ (] _[T]_ [)] : [�] _v_ _[x][v]_ [=] [0] _[}]_ [dual] [to]

the isomorphism _fT_ of Lemma 3.3. Also, our chosen vector b _∈_ R [(] _[n]_ _≥_ [+2] 3 [)] induces a map
b : Brackets [+] ( _T_ ) _→_ R, since the extended brackets of _T_ correspond to the polygons in
the triangulation of _M_ . In turn this induces a map b _[−]_ : Brackets( _T_ ) _→_ R by (7).


**Definition** **4.7.** _For_ _a_ _maximal_ _Matryoshka_ _M_ _with_ _bracketed_ _tree_ ( _T, B_ ) _we_ _define_


_cM_ := _aT_ + _ε f_ _[T]_ ( _bB_ )


_where_ _aT_ _is_ _the_ _vertex_ _of_ Loday _n−_ 1(a) _corresponding_ _to_ _the_ _plane_ _tree_ _T_ _and_ _bB_ _is_ _the_
_vertex_ _of_ BrAssoc _T_ (b _[−]_ ) _corresponding_ _to_ _its_ _bracketing_ _B._ _The_ cosmohedron _is_


Cosmo _n−_ 1(a _,_ b) := conv( _cM_ : _M_ _is_ _a_ _maximal_ _Matryoshka_ _on_ _the_ ( _n_ + 2) _-gon_ ) _⊂_ R _[n]_ _._


Before we prove the correctness of this construction, let us give an explicit formula
for the vertex _cM_ directly in terms of the Matryoshka _M_ .



**Proposition** **4.8.** _Let_ _M_ _be_ _a_ _maximal_ _Matryoshka_ _on_ _n_ +2 _._ _For_ _each_ _v_ _∈_ [ _n_ ] _define_

_�_




- 
_aij_ =

_ij→v_ _u≤_








  ( _aM_ ) _v_ =



_u≤i<v_



_aij_

_v<j≤w_



_summing over the diagonals ij_ _that cross triangle v (with vertices uvw) of the triangulation_
_of_ _M_ _transversally._
_For_ _each_ _polygon_ _of_ _the_ _Matryoshka_ _M_ _that_ _is_ _subdivided_ _into_ _maximal_ _subpolygons_
_Q_ _and_ _R_ _in_ _M_ _,_ _let_
_bM_ ( _P_ ) = _b_ ( _P_ ) _−_ _b_ ( _Q_ ) _−_ _b_ ( _R_ ) _._


_For_ _each_ _v_ _∈_ [ _n_ ] _,_ _where_ _triangle_ _v_ _has_ _edges_ _uv_ _(opposite_ _to_ _vertex_ _v),_ _lv,_ _and_ _rv,_ _define_


( _bM_ ) _v_ = _bM_ ( _P_ ( _lv_ )) + _bM_ ( _P_ ( _rv_ )) _−_ _bM_ ( _P_ ( _uv_ ))


_where_ _P_ ( _e_ ) _is_ _the_ _minimal_ _polygon_ _in_ _M_ _containing_ _diagonal_ _e;_ _when_ _e_ _is_ _an_ _edge_ _of_
_n_ +2 _,_ _we_ _set_ _bM_ ( _P_ ( _e_ )) = 0 _._ _Then_ _the_ _vertex_ _cM_ _of_ _a_ _Matryoshka_ _M_ _has_ _coordinates_

_�_

( _cM_ ) _v_ = ( _aM_ ) _v_ + _ε_ ( _bM_ ) _v_ _for_ _v_ _∈_ [ _n_ ] _._


_Proof._ This follows readily from Lemmas 4.2 and 4.5 and Definition 4.7.


24


**Remark** **4.9.** _Our_ _preferred_ _choice_ _of_ a _and_ b _will_ _be_



_aij_ = 1 _for_ _all_ _i, j,_ _b_ ( _P_ ) =


_This_ _choice_ _simplifies_ _computations:_ _we_ _have_




0 _if_ _|P_ _| ≤_ 4
3 _[|][P]_ _[|−]_ [5] _if_ _|P_ _| ≥_ 5 _._



( _aM_ ) _v_ = _|lv| · |rv|_


_where_ _|f_ _|_ _is_ _the_ _number_ _of_ _edges_ _of_ _n_ +2 _that_ _are_ _on_ _the_ _side_ _of_ _f_ _opposite_ _to_ _e._ _Also,_
_bM_ ( _P_ ) = 0 _for_ _all_ _triangles_ _and_ _quadrilaterals�_ _P_ _._


**Example** **4.10.** _Let_ _us_ _compute_ _the_ _vertex_ _cM_ 2 _for_ _the_ _Matryoshka_ _M_ 2 _of_ _Figure_ _4._
_We_ _have_ _aM_ 2 = (1 _·_ 2 _,_ 1 _·_ 1 _,_ 3 _·_ 2 _,_ 1 _·_ 1) = (2 _,_ 1 _,_ 6 _,_ 1) _The_ _non-zero_ _coordinates_ _of_ _bM_ 2
_are_ _bM_ 2( _hexagon_ ) = 3 _−_ 1 _−_ 0 = 2 _and_ _bM_ 2( _pentagon_ ) = 1 _−_ 0 _−_ 0 = 1 _._ _Therefore_
_bM_ 2 = (0 + 0 _−_ 1 _,_ 0 + 0 _−_ 0 _,_ 1 + 2 _−_ 0 _,_ 0 + 0 _−_ 2) = ( _−_ 1 _,_ 0 _,_ 3 _, −_ 2) _and_


_cM_ 2 = (2 _,_ 1 _,_ 6 _,_ 1) + _ε_ ( _−_ 1 _,_ 0 _,_ 3 _,_ 2) _._


**4.2.2** **The** **cosmohedron:** **proof** **of** **correctness**


**Theorem** **4.11.** _The_ _normal_ _fan_ _of_ _the_ _cosmohedron_ Cosmo _n−_ 1(a _,_ b) _is_ _the_ _cosmohedral_
_fan_ CosmoFan _n−_ 1 _._


_Proof._ Let _NP_ ( _v_ ) := _{w_ _∈_ _V_ _[∗]_ : _w_ ( _v_ ) _≥_ _w_ ( _p_ ) for all _p_ _∈_ _P_ _}_ denote the normal cone of
vertex _v_ in polytope _P_ _⊂_ _V_ . Since the cosmohedron lives on a hyperplane with constant
coordinate sum, its dual space is R _[n]_ _/_ R **1** . We need to prove that


_N_ Cosmo _n−_ 1(a _,_ b)( _cM_ ) = cone( _M_ )


for all maximal Matryoshkas _M_ . Since both the left-hand sides and the right-hand sides
subdivide R _[n]_ _/_ R **1** with no interior overlap as _M_ ranges over the maximal Matryoshkas,
it suffices to prove the inclusion _⊆_ for all _M_ .
Let _M_ be a maximal Matryoshka with bracketed tree ( _T, B_ ), and take _w_ _∈N_ Cosmo _n−_ 1( _cM_ ).
To prove that _w_ _∈_ cone( _M_ ), we proceed in two steps.

Step 1. Consider a covering relation _M_ ( _ij_ _[⊥]_ ) ⋗ _M_ ( _kl_ _[⊥]_ ) in _M_ . We need to show that
_w_ satisfies the corresponding inequality� _wi −_ _wj_ _≥_ - _wk −_ _wl_ for cone( _M_ ).
Edge _kl_ _[⊥]_ creates a subdivision _M_ ( _kl_ _[⊥]_ ) = _P_ 1 _∪P_ 2 and edge _ij_ _[⊥]_ creates a subdivision
_M_ ( _ij_ _[⊥]_ ) = _M_ ( _kl_ _[⊥]_ ) _∪_ _P_ 3. Consider the Matryoshka � _M_ _[′]_ obtained by removing _M_ ( _kl_ _[⊥]_ )
and� adding �a new polygon around _P_ 2 and _P_ 3. The bracketed tree of _M_ _[′]_ is ( _T, B_ _[′]_ ) for the same tree _T_ and a different bracketing. The
containment trees _τ_ = tree( _B_ ) and _τ_ _[′]_ = tree( _B_ _[′]_ ) differ by a simple mutation, as shown
in Figure 14. Since Devadoss’s bracket associahedron is a generalized permutahedron, its


25


Figure 14: A swap of a non-minimal polygon in a Matryoshka, and the corresponding
effect on the polygon containment tree _τ_ .


adjacent vertices _bB_ and _bB′_ satisfy _bB −_ _b_ _[′]_ _B_ [=] _[ L]_ [(] _[e][ij][ −]_ _[e][kl]_ [) for some] _[ L >]_ [ 0[AA23, Pos09].]
Now _w_ _∈N_ Cosmo _n−_ 1( _cM_ ) gives _w_ ( _cM_ ) _≥_ _w_ ( _cM_ _′_ ), so


_w_ ( _aT_ + _ε f_ _[T]_ ( _bB_ )) _≥_ _w_ ( _aT_ + _ε f_ _[T]_ ( _bB′_ ))

_wf_ _[T]_ ( _L_ ( _eij_ _−_ _ekl_ )) _≥_ 0

_w_ (( _ei −_ _ej_ ) _−_ ( _ek −_ _el_ )) _≥_ 0


as desired.

Step 2. Consider a polygon _M_ ( _kl_ _[⊥]_ ) that does not contain a smaller _M_ ( _k_ _[′]_ _l_ _[′⊥]_ ); it must
be a quadrilateral split into two triangles � _k_ and _l_ . Consider the Matryoshka � _M_ _[′]_ obtained
by flipping those two triangles in the quadrilateral.


Figure 15: A flip of the triangulation in a Matryoshka, and the corresponding effect on
the tree _T_ of the triangulation.


The tree _T_ _[′]_ of (the triangulation of) _M_ _[′]_ is obtained from _T_ by a simple edge mutation,
as shown in Figure 15. Since Loday’s associahedron is a generalized permutahedron, its


26


adjacent vertices _aT_ and _aT ′_ satisfy _aT_ _−_ _a_ _[′]_ _T_ [=] _[ L]_ [(] _[e][i][ −]_ _[e][j]_ [)] [for] [some] _[L >]_ [ 0] [[AA23,] [Pos09].]
The bracketings _B_ and _B_ _[′]_ both contain bracket _ij_, so they contain the same set of
polygons, and give isomorphic posets _τ_ = tree( _B_ ) _[∼]_ = tree( _B_ _[′]_ ) = _τ_ _[′]_ . This means that
_bB_ = _bB′_ up to the resulting reordering of the edges ( _hi, ij, jk_ ) _�→_ ( _hj, ji, ik_ ). Therefore
if we write _H_ = ( _bB_ ) _hi, I_ = ( _bB_ ) _ij, J_ = ( _bB_ ) _jk_,

_f_ _[T]_ ( _bB_ ) _−_ _f_ _[T][ ′]_ ( _bB′_ ) = ( _H_ ( _eh −_ _ei_ ) + _I_ ( _ei −_ _ej_ ) + _J_ ( _ej_ _−_ _ek_ ))

_−_ ( _H_ ( _eh −_ _ej_ ) + _I_ ( _ej_ _−_ _ei_ ) + _J_ ( _ei −_ _ek_ ))

= ( _−H_ + 2 _I_ _−_ _J_ )( _ei −_ _ej_ ) _._


Now since _w_ _∈N_ Cosmo _n−_ 1( _cM_ ), we have _w_ ( _cM_ ) _≥_ _w_ ( _cM_ _′_ ), so


         -          _w_ ( _aT_ _−_ _aT ′_ ) + _ε_ ( _f_ _[T]_ _−_ _f_ _[T][ ′]_ )( _bB_ ) _≥_ 0


_w_ (( _L_ + 2 _ε_ ( _−H_ + 2 _I_ _−_ _J_ ))( _ei −_ _ej_ ) _≥_ 0

_w_ ( _ei −_ _ej_ ) _≥_ 0


as desired. In the last step we are observing that each entry of ( _bB_ ) is at most 3 _M_ because
the formula in Lemma 4.5 contains at most three terms, so _|_ 2 _ε_ ( _−H_ + 2 _I −_ _J_ ) _| <_ 24 _Mε_,
whereas each edge _aT −aT ′_ of Loday _n−_ 1(a) is a sum of edges of its Minkowski summands,
so its length _L_ is at least _m_ .


**Remark** **4.12.** _In_ _Step_ _2_ _of_ _the_ _proof_ _above,_ _it_ _is_ _essential_ _that_ _bB_ _and_ _bB′_ _are_ _equal_ _up_
_to_ _the_ _natural_ _reordering_ _of_ _their_ _coordinates._ _This_ _is_ _a_ _subtle_ _requirement,_ _because_ _bB_
_and_ _bB′_ _are_ _vertices_ _of_ _different_ _bracket_ _associahedra_ BrAssoc _T_ _and_ BrAssoc _T ′._ _The_ _key_
_property of Devadoss’s realization of bracket associahedra that makes this work is that the_
_coordinates_ _of_ _a_ _vertex_ _bB_ _only_ _depend_ _on_ _the_ _poset_ _τ_ = tree( _B_ ) _of_ _the_ _bracketing,_ _and_
_in_ _the_ _above_ _situation_ _we_ _have_ _τ_ = tree( _B_ ) = tree( _B_ _[′]_ ) = _τ_ _[′]_ _._ _We_ _note_ _that_ _Postnikov’s_
_realization_ _[Pos09]_ _of_ _bracket_ _associahedra_ _does_ _**not**_ _have_ _this_ _property,_ _so_ _we_ _cannot_ _use_
_it_ _to_ _realize_ _the_ _cosmohedron_ _in_ _this_ _manner._


**4.2.3** **Inequality** **description.**


For a chord _C_ and a vertex _i_ or diagonal _ij_ of _n_ +2, let us write _C_ _≻_ _i_ if the chord _C_
is strictly above vertex _i_ and _C_ _⪰_ _ij_ if the chord� _C_ is weakly above diagonal _ij_, with
respect to the base edge _e_ at the top.
For a subdivision _S_ of _n_ +2 (or equivalently a non-crossing set of chords _C_ ), we define
some parameters of _S_ and � _C_ in a few equivalent ways. Each description is sufficient, but
it can be useful at times to have all of them available. Let the _depth_ of a vertex _i_ or a
diagonal _ij_ of _n_ +2 be

    - _dS_ ( _i_ ) = # of chords _C_ of _C_ with _C_ _≻_ _i_

= distance from vertex _i_ to the root in tree( _S_ )


= depth of vertex _i_ in tree□( _S_ ) _,_ and


_dS_ ( _ij_ ) = # of chords _C_ of _C_ with _C_ _⪰_ _ij_

= depth of cell _ij_ in tree□( _S_ ) _._


27


where tree□( _S_ ) is the canonical embedding of the tree of _S_ in a square grid, and the
depth of a vertex or a cell in tree□( _S_ ) is the number of non-root vertices of the tree
whose southwest/southeast shadow contains it; see Figure 16.


Figure 16: A subdivision _S_, its corresponding tree, its grid embedding with the
corresponding cell depths, and the corresponding cosmohedral facet.



**Theorem** **4.13.** _The_ _cosmohedron_ Cosmo _n−_ 1(a _,_ b) _⊂_ R _[n]_ _is_ _described_ _by_ _the_ _irredundant_
_system_ _of_ _inequalities_

  -   



- 
_xi_ =
1 _≤i≤n_ _ij∈_ diag(



_b_ ( _P_ ) _for_ _any_ _subdivision_ _S._

_P_ _∈S_




- 
_dS_ ( _i_ ) _xi_ _≥_
1 _≤i≤n_ _ij∈_ diag(







_aij,_

_ij∈_ diag( _n_ +2)


 
_�_




 - 
_dS_ ( _ij_ ) _aij_ _−_ _ε_
_ij∈_ diag( _n_ +2) _P_ _∈S_

_�_



_Proof._ The lineality space of CosmoFan _n−_ 1 is R(1 _, . . .,_ 1), so the only equality satisfied
by Cosmo _n−_ 1(a _,_ b) is the given one.
The irredundant inequalities of Cosmo _n−_ 1(a _,_ b) correspond to the rays of CosmoFan _n−_ 1,
which are in bijection with the minimal non-trivial Matryoshkas by Theorem 3.6. These
are the subdivisions _S_ of _n_ +2 - with no nesting - obtained from the non-crossing sets
of chords _C_ . By (1), the ray� R _≥_ 0( _ρS_ ) = cone( _S_ ) is given by the inequalities _xv −_ _xw_ _≥_ 0,
and hence ( _ρS_ ) _v −_ ( _ρS_ ) _w_ = 1, for all chords _vw_ _[⊥]_ of _S_ . Therefore _ρS_ = ( _dS_ (1) _, . . ., dS_ ( _n_ )).

   Notice that _ρS_ = _ρ{C}_ and _ρ{C}_ = _ei_ +1 + _· · ·_ + _ej−_ 1 for _C_ = _ij_ .



_ρ{C}_ and _ρ{C}_ = _ei_ +1 + _· · ·_ + _ej−_ 1 for _C_ = _ij_ .
_C∈C_



28


To determine the extreme value of ( _ρS, x_ ) for _x_ _∈_ Cosmo _n−_ 1(a _,_ b), we need to
compute ( _ρS, cM_ ) for any maximal Matryoshka _M_ = ( _T, B_ ) that refines _S_ ; see Figure
17. A chord _C_ gets a label _vw_ _[⊥]_ for a pair of adjacent triangles _v, w_ in the triangulation
_T_, and the definition in Lemma 3.3 gives _fT_ ( _evw_ ) = _ρ{C}_ + R **1** ; this is also a ray of the
associahedral fan AssocFan _n−_ 1. Therefore




  ( _ρC, cM_ ) =


_C∈C_




- _ρC,_ _aT_ + _ε f_ _[T]_ ( _bB_ )� by Definition 4.7,




 =




- 
( _ρC, aT_ ) + _ε_
_C∈C_ _C_ = _vw_




 
( _fT_ ( _evw_ ) _, f_ _[T]_ ( _bB_ ))
_C_ = _vw_ _[⊥]_ _∈C_



The first sum comes from the Loday associahedron; using (4) we obtain

    -    -    -    



- 
( _ρC, aT_ ) =
_C∈C_ _C_




 - 
_aij_ =

_ij_ : _ij⪯C_ _ij_







_dC_ ( _ij_ ) _aij_

_ij_



_C_



Since _fT_ and _f_ _[T]_ are dual, the second sum equals


         







- 
( _bB_ ) _vw_ =

_vw_ _[⊥]_ _∈C_ _vw_ _[⊥]_







_vw_ _[⊥]_ _∈C_




   _b_ (bracket _B_ ( _vw_ )) _−_ _b_ (bracket _B_ ( _tu_ ))

_tu_ ⋖ _Bvw_



using Lemma 4.6 for the vertices of the bracket associahedron. Here _tu_ ⋖ _B_ _vw_ means
that _vw_ is covers _tu_ in the extended tree [+] ( _B_ ) of the bracketing _B_ .
Now, every diagonal _d_ of the triangulation _T_ that is not in _C_ is inside a polygon
_P_ _∈S_, so bracket _B_ ( _d_ ) _⊂_ _P_ cannot contain any chord in _C_ . It follows that _C_ is an upper
ideal of tree [+] ( _B_ ), and that the brackets of the maximal non-elements of _C_ are precisely
the polygons in _S_ . Also, tree( _B_ ) has a unique maximal element _V W_ = tree( _B_ ) _max_ .
Therefore

  -  



- 
( _bB_ ) _vw_ = _b_ (bracket _B_ ( _V W_ )) _−_

_vw_ _[⊥]_ _∈C_ _tu∈_ (tree( _B_ )



_b_ (bracket _B_ ( _tu_ ))

_tu∈_ (tree( _B_ ) _−C_ )max




  = _b_ ( ) _−_ _b_ ( _P_ )


_P_ _∈S_

  



  = _b_ ( ) _−_


_P_ _∈S_

  
 = _−_ _b_ ( _P_ )


_P_ _∈S_




 = _−_



using that _b_ (�) = 0 . The desired result follows.

**Example** **4.14.** _Figure_ _17_ _shows_ _a_ _Matryoshka_ _M_ _that_ _refines_ _the_ _subdivision_ _S_ _of_
_Figure 16, so vertex cM_ _is on the facet that maximizes ρC._ _In the computation of_ ( _ρC, cM_ )
_above,_ _the_ _left_ _sum_ _is_ _simply_ _the_ _dot_ _product_ _of_ _the_ _cell_ _labels_ _of_ tree□( _S_ ) _and_ a _._ _Writing_
_b_ ( _·_ ) = _b_ (bracket _B_ ( _·_ )) _for_ _legibility,_ _the_ _right_ _sum_ _is_


[ _b_ (42)) _−_ _b_ (23) _−_ _b_ (45)] + [ _b_ (23) _−_ _b_ (3) _−_ _b_ (21)] + [ _b_ (45) _−_ _b_ (56) _−_ _b_ (4)]


= 0 _−_ _b_ (3) _−_ _b_ (21) _−_ _b_ (56) _−_ _b_ (4)


= _−b_ 0124 _−_ _b_ 234 _−_ _b_ 047 _−_ _b_ 4567


29


Figure 17: A vertex on the facet given by Figure 16.


**4.2.4** **Isomorphism** **with** **the** **Arkani–Hamed-Figueiredo-Vaz˜ao** **cosmohedron.**



In _kinematic_ _space_ one assigns a real number to each diagonal of _n_ +2:

[diag(] _[∼]_ [(] _[n]_ [+2)(] _[n][−]_ [1)]                   - _[/]_ [2]

_[n]_ [+2][)]



R [diag(][�] _[n]_ [+2][)] = _{_ ( _Xij_ ) _ij∈_ diag( _n_ +2) _}_ _[∼]_ = R [(] _[n]_ [+2)(] _[n][−]_ [1)] _[/]_ [2]

to the base edge _e_ = 0 _, n_   - + 1.



We assign _X_ 0 _,n_ +1 = 0 to the base edge _e_ = 0 _, n_ + 1.
Let us fix:

_•_ an arbitrary assignment A = ( _Aij_ : 0 _≤_ _i_ _<<_ _j_ _≤_ _n_ ) of  - _n_ 2� positive numbers to
the diagonals of _n_ +2 that do not involve _n_ + 1, and

_•_ a small convex� vector B = ( _B_ ( _P_ ) : _P_ is a subpolygon of _n_ +2).
Note that the vector b of the previous section was concave, and� _B_ is convex.
Arkani-Hamed, Bai, He, and Yan [AHBHY18b] defined the _associahedron_ [3] ABHY _n−_ 1(A)
to be the ( _n −_ 1)-dimensional polytope



_{X_ _∈_ R [diag(][�] _[n]_ [+2][)] : _Xr,s_ + _Xr_ +1 _,s_ +1 _−_ _Xr,s_ +1 _−_ _Xr_ +1 _,s_ = _Ars_ for 0 _≤_ _r_ _≪_ _s ≤_ _n_

_Xr,s_ _≥_ 0 for 0 _≤_ _r_ _≪_ _s ≤_ _n_ + 1 _, }_ (9)



where _X_ 0 _,n_ +1 = _Xr,r_ +1 := 0 for 0 _≤_ _r_ _≤_ _n_, and again, _r_ _≪_ _s_ means that _s −_ _r_ _≥_ 2.
Arkani-Hamed, Figueiredo, and Vaz˜ao [AHFV25] defined the following polytope, and
conjectured that its face structure matches the combinatorics of Matryoshkas.


**Definition** **4.15.** _The_ cosmohedron AFV _n−_ 1(A _,_ B) _is_ _the_ ( _n −_ 1) _-dimensional_ _polytope_



_{X_ _∈_ R [diag(] _[�][n]_ [+2][)] : _Xr,s_ _≥_ 0 _for_ 0 _≤_ _r_ _≪_ _s ≤_ _n_ + 1 _,_



_Xr,s_ + _Xr_ +1 _,s_ +1 _−_ _Xr,s_ +1 _−_ _Xr_ +1 _,s_ = _Ars_ _for_ 0 _≤_ _r_ _≪_ _s ≤_ _n,_

- 



- 
_XC_ _≥_

_C∈C_ _P_ _∈S_ (



_B_ ( _P_ ) : _for_ _non-crossing_ _C_ _⊂_ diag( _n_ +2) _}_ (10)
_P_ _∈S_ ( _C_ ) _�_



_where_ _S_ ( _C_ ) _is_ _the_ _set_ _of_ _polygons_ _in_ _the_ _subdivision_ _of_ _n_ +2 _induced_ _by_ _C._

3In [AHBHY18b] this is denoted _An_ +2. We use the subscript _�n −_ 1 to match the root system _An−_ 1
and the dimension of the polytope.


30


      **Theorem** **4.16.** _The_ _map_ _Xr,s_ =




- 
_xi −_
_r<i<s_ _r≤i<<j_



_aij_ _gives_ _linear_ _isomorphisms_

_r≤i<<j≤s_



_1._ _between_ _the_ _associahedra_ Loday _n−_ 1(a) _and_ ABHY _n−_ 1(A) _,_ _and_


_2._ _between_ _the_ _cosmohedra_ Cosmo _n−_ 1(a _,_ b) _and_ AFV _n−_ 1(A _,_ B) _,_


_where Aij_ = _ai,j_ +1 _for each diagonal ij_ _∈_ diag( _n_ +2) _and B_ ( _P_ ) = _−ε b_ ( _P_ ) _for sufficiently_
_small_ _ε >_ 0 _._ _�_


Before proving this, we note that a has size  - _n_ +1� whereas A has size  - _n_ �; this
2 2
is because the _n_ entries _ai−_ 1 _,i_ +1 do not enter the definition of AFV _n−_ 1(A _,_ B). These
entries are the coefficients of the points ∆ _{i}_ = _ei_ in the Minkowski sum of Loday _n−_ 1(a),
so they only cause a translation of the polytope.


_Proof_ _of_ _Theorem_ _4.16._ 1. A vector _x_ _∈_ R _[n]_ determines a vector _X_ in kinematic space
that satisfies the linearly independent equations


_Xr,s_ + _Xr_ +1 _,s_ +1 _−_ _Xr,s_ +1 _−_ _Xr_ +1 _,s_ = _ar,s_ +1 = _Ar,s_ for 0 _≤_ _r_ _<< s ≤_ _n._


as one readily verifies. These - _n_ - equations restrict _X_ to a vector space of dimension
2
( _n_ +2)( _n−_ 1) _/_ 2 _−_ - _n_ - = _n−_ 1, which is precisely the dimension of the associahedron. The
2
inequalities _Xr−_ 1 _,s_ +1 _≥_ 0 are restatements of the defining inequalities of Loday _n−_ 1(a) as
written in (4), proving the desired isomorphism. See also [Ear24].
2. It remains to translate the inequalities of the cosmohedron Cosmo _n−_ 1(a _,_ b):

   -    -    



 - 
_dC_ ( _ij_ ) _aij_ _−_ _ε_
_ij∈_ diag( _n_ +2) _P_ _∈S_

  



- 
_dC_ ( _i_ ) _xi_ _≥_
1 _≤i≤n_ _ij∈_ diag(



_b_ ( _P_ )

_P_ _∈S_



for any subdivision _S_ with chords _C_ . We rewrite this as











_d{C}_ ( _ij_ ) _aij_

_ij∈_ diag( _n_ +2)

  




 _≥_ 
_C∈C_




  _−_ _ε_ _b_ ( _P_ ) _._

_P_ _∈S_






_C∈C_





 [�] _d{C}_ ( _i_ ) _xi_

1 _≤i≤n_




 



Now notice that _d{C}_ ( _i_ ) is 1 if _C_ _≻_ _i_ and 0 otherwise, and _d{C}_ ( _ij_ ) is 1 if _C_ _⪰_ _ij_ and 0
otherwise, so

    -     _XC_ = _d{C}_ ( _i_ ) _xi −_ _d{C}_ ( _ij_ ) _aij._




- 
_d{C}_ ( _i_ ) _xi −_
1 _≤i≤n_ _ij∈_ diag(



_d{C}_ ( _ij_ ) _aij._

_ij∈_ diag( _n_ +2)

  


Thus the inequalities of Cosmo _n−_ 1(a _,_ b) in _x_ -space are equivalent to the inequalities of
AFV _n−_ 1(A _,_ B) in _X_ -space. We note that B is concave if and only if b is concave, and B
is made sufficiently small - as [AHFV25] requires - by making _ε_ sufficiently small.



In particular, this proves one of our main results: the correctness of Arkani-Hamed,
Figueiredo, and Vaz˜ao’s construction.


**Corollary 4.17.** _The face poset of Arkani-Hamed, Figueiredo, and Vaz˜ao’s cosmohedron_
AFV _n−_ 1 _is_ _anti-isomorphic_ _to_ _the_ _poset_ _of_ _Matryoshkas_ _of_ _an_ ( _n_ + 2) _-gon._


31


It also lets us determine precisely what their requirement of a “small enough” _B_
means. Theorem 4.11 proves that Cosmo _n−_ 1(a _,_ b) is a cosmohedron for 0 _<_ _ε_ _<_
(min _aij_ ) _/_ 24(max _b_ ( _P_ )); it would be interesting to trace the proof carefully and find
the optimal constant.

### **5 Face structure and enumeration**


**The dimension of a face.** Recall that _M_ not min is the number of polygons in a Matryoshka
_M_ that are not inclusion-minimal.


**Lemma** **5.1.** _The_ _cone_ _of_ _a_ _Matryoshka_ _M_ _in_ _the_ _cosmohedral_ _fan_ _has_ _dimension_


dim cone( _M_ ) = _|Mnot_ _min|_ + 1 _._


_Proof._ If ( _T, B_ ) is the bracketed tree corresponding to _M_ from Lemma 2.10, we have
cone( _M_ ) = cone( _T, B_ ) = _fT_ (cone _T_ ( _B_ ) _≥_ 0) and its dimension equals the dimension of
cone _T_ ( _B_ ), which is the number of brackets in _B_ . This equals the number of non-minimal
polygons of the Matryoshka _M_ .


**Faces** **of** **the** **cosmohedron** **factor** **combinatorially,** **but** **not** **geometrically.** The faces of
the cosmohedron have an interesting factorization property that is subtler and weaker
than the analogous property for bracket associahedra.


Bracket associahedra [4] have the property that any facet factors canonically as a
Cartesian product of two bracket associahedra, as we now describe. Let _H_ be a graph,
_β_ be a bracket of _H_, and _H/β_ the contraction of _β_ in _H_, whose edges are in bijection
with _E_ ( _H_ ) _−_ _E_ ( _β_ ). Also let _b|β_ ( _β_ _[′]_ ) = _b_ ( _β_ _[′]_ ) for each bracket _β_ _[′]_ of _β_ and _b/β_ ( _β_ _[′′]_ ) =
_b_ ( _β ∪_ _β_ _[′′]_ ) _−_ _b_ ( _β_ ) for each bracket _β_ _[′′]_ of _H/β_ . Note that if _b_ is concave on Brackets( _H_ ),
then _b|β_ and _b/β_ are concave on Brackets( _β_ ) and Brackets( _H/β_ ), respectively.


**Lemma** **5.2.** _[AA23]_ _For_ _any_ _graph_ _H_ _and_ _any_ _bracket_ _β_ _of_ _H,_ _the_ _eβ-maximal_ _facet_
_of_ BrAssoc _H_ (b) _is_ _linearly_ _isomorphic_ _to_ _the_ _product_ _of_ _bracket_ _associahedra_


(BrAssoc _H_ (b)) _β_ = BrAssoc _[∼]_ _β_ (b _|β_ ) _×_ BrAssoc _H/β_ (b _/β_ ) _⊂_ R _[E]_ [(] _[β]_ [)] _×_ R _[E]_ [(] _[H/β]_ [)]


Facets, and hence faces, of cosmohedra have an analogous factorization property   but it is significantly weaker. The first statement below was observed in [AHFV25], but
it holds an unexpected surprise.


**Proposition** **5.3.** _Let_ _S_ _be_ _a_ _subdivision_ _of_ _the_ ( _n_ + 2) _−_ _gon_ _into_ _polygons_ _P_ 1 _, . . ., Pk_
_where_ _Pi_ _is_ _an_ ( _ni_ + 2) _-gon._ _Let_ _T_ ( _S_ ) _be_ _its_ _dual_ _graph,_ _which_ _is_ _a_ _tree._ _Then_ _the_ _facet_
_of_ Cosmo _n_ _corresponding_ _to_ _S_ _is_ _**combinatorially**_ _isomorphic_ _to_ _the_ _product_


(Cosmo _n_ ) _S_ = _[∼][comb]_ BrAssoc _T_ ( _S_ ) _×_ (Cosmo _n_ 1) _× · · · ×_ (Cosmo _nk_ ) _._


_However,_ _this_ _factorization_ _**does**_ _**not**_ _**hold**_ _**geometrically**_ _._


4and, more broadly, generalized permutahedra [AA23, Edm70]


32


_Proof._ The face poset of _L_ (Cosmo _n_ ) is the opposite of the poset _Mn_ of Matryoshkas
of the ( _n_ + 2)-gon. The interval [ [�] 0 _,_ (Cosmo _n_ ) _S_ ] corresponds to the subposet ( _Mn_ ) _≥S_ of
Matryoshkas refining _S_ . Such a Matryoshka is obtained by making _k_ + 1 independent
choices:
(i) refining each of the _k_ polygons _Pi_ internally with its own Matryoshka   - the ways
of doing this are in order-reversing bijection with the faces of Cosmo _ni_ - and
(ii) refining _S_ externally with compatible polygons that are unions of the _Pi_ s   - the
ways of doing this are in order-reversing bijection with the bracketings of _T_ ( _S_ ).
These independent choices are compatible with the order relations of the posets, giving
the desired result.


The above isomorphism is not, in general, a linear isomorphism of polyhedra. We can
already see this in the cosmohedron Cosmo3. Consider the subdivision of a hexagon by
a long and a short diagonal, as illustrated in Figure 18. Proposition 5.3 predicts that this
facet is combinatorially isomorphic to the product _T_ ( _P_ 2) _×_ Cosmo2 _×_ Cosmo1 _×_ Cosmo1 =
_| × | × · × ·_ which is a quadrilateral. We claim that this face is a trapezoid; we can see
this in Figure 2, but let us verify it algebraically. We use Proposition 4.8 to compute:


_cM_ 1 = (1 _,_ 2 _,_ 6 _,_ 1) + _ε_ (0 _, −_ 3 _,_ 3 _,_ 0) _cN_ 1 = (2 _,_ 1 _,_ 6 _,_ 1) + _ε_ ( _−_ 3 _,_ 0 _,_ 3 _,_ 0)

_cM_ 2 = (2 _,_ 1 _,_ 6 _,_ 1) + _ε_ ( _−_ 1 _,_ 0 _,_ 3 _, −_ 2) _cN_ 2 = (1 _,_ 2 _,_ 6 _,_ 1) + _ε_ (0 _, −_ 1 _,_ 3 _, −_ 2)


and notice that the opposite sides


_cM_ 1 _−_ _cN_ 1 = (1 _−_ 3 _ε_ )( _e_ 2 _−_ _e_ 1) _,_ _cM_ 2 _−_ _cN_ 2 = (1 _−_ _ε_ )( _e_ 1 _−_ _e_ 2) _,_


are parallel but not equal. Since it is not a parallelogram, this quadrilateral face cannot
be expressed as a Cartesian product of two edges.


Figure 18: A trapezoidal face of the cosmohedron.


33


**5.1** **Enumeration**


Having understood the combinatorial structure of the cosmohedron, we are now ready
to enumerate its faces. We also compute the face numbers of the _correlatron_ of [FV26],
which are closely related in an elegant and surprising way.


**5.2** **Counting** **the** **faces** **of** **the** **cosmohedron**


Our next goal is to compute the number of faces of the cosmohedron in each dimension.
We list these numbers in Table 1 for _n ≥_ 6.

|cosmohedron|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|0<br>1<br>2<br>3<br>4<br>5<br>6|1<br>1<br>1<br>1<br>1<br>1<br>1|2<br>10<br>44<br>196<br>902<br>4278|10<br>114<br>952<br>7116<br>50550|72<br>1400<br>18040<br>194616|644<br>18528<br>332664|6704<br>262728|78408|



Table 1: The number of _d_ -codimensional faces of the _n_ th cosmohedron on _n_ + 2 points.


It is useful to organize them in the _f_ -polynomial _fn_ ( _t_ ) = _f_ AssocFan _n−_ 1( _t_ ) and the
modified _f_ -polynomial _gn_ ( _t_ ) = [(1+ _t_ ) _fn_ ( _t_ ) _−_ 1] _/t_, whose coefficients are the consecutive
pair sums of the coefficients of _fn_ ( _t_ ):


_f_ 1( _t_ ) = 1 _,_ _f_ 2( _t_ ) = 1 + 2 _t,_ _f_ 3( _t_ ) = 1 + 10 _t_ + 10 _t_ [2] _,_ _f_ 4( _t_ ) = 1 + 44 _t_ + 114 _t_ [2] + 72 _t_ [3] _, . . ._

_g_ 1( _t_ ) = 1 _,_ _g_ 2( _t_ ) = 3 + 2 _t,_ _g_ 3( _t_ ) = 11 + 20 _t_ + 10 _t_ [2] _,_ _g_ 4( _t_ ) = 45 + 148 _t_ + 186 _t_ [2] + 72 _t_ [3] _, . . . ._


**Theorem** **5.4.** _The_ _f_ _-polynomials_ _of_ _the_ _cosmohedral_ _fans_ _form_ _the_ _unique_ _sequence_
_{fn_ ( _t_ ) _}n≥_ 1 _of_ _polynomials_ _such_ _that_ _the_ _power_ _series_ _in_ (R[ _t_ ])[ _x_ ]


_x −_ _f_ 1( _t_ ) _x_ [2] _−_ _f_ 2( _t_ ) _x_ [3] _−_ _f_ 3( _t_ ) _x_ [4] _−_ _. . ._

_x_ + _g_ 1( _t_ ) _x_ [2] + _g_ 2( _t_ ) _x_ [3] + _g_ 3( _t_ ) _x_ [3] + _. . ._


_are_ _compositional_ _inverses,_ _where_ _gn_ ( _t_ ) = [(1 + _t_ ) _fn_ ( _t_ ) _−_ 1] _/t._ _Equivalently,_ _the_ _power_
_series_ _At_ ( _x_ ) = _x −_ _f_ 1( _t_ ) _x_ [2] _−_ _f_ 2( _t_ ) _x_ [3] + _. . ._ _satisfies_



_At_




- (2 _t_ + 1) _x −_ (2 _t_ + 2) _x_ 2



_x −_ (2 _t_ + 2) _x_ 2 
_−_ 1 + [1]
_t_ (1 _−_ _x_ ) _t_



_t_




- _At_ ( _x_ ) = _x._



_Proof._ Every face _F_ of the cosmohedral fan is contained in a unique minimal face of the
associahedral fan _A_ ( _F_ ). If _F_ corresponds to a Matryoshka _M_ on an ( _n_ + 2)-gon then
_A_ ( _F_ ) corresponds to the subdivision _Mmax_ given by the maximal polygons _P_ 1 _, . . ., Pk_
of _M_ . If _Pi_ is an ( _ni_ + 2)-gon then _n_ = _n_ 1 + _· · ·_ + _nk_ .


34


Conversely, consider a face _A_ of the associahedral fan, corresponding to a non-trivial
subdivision _S_ of the ( _n_ + 2)-gon into an ( _ni_ + 2)-gon _Pi_ for 1 _≤_ _i_ _≤_ _k_ . The faces _F_ of
the cosmohedron such that _A_ ( _F_ ) = _A_ correspond to the Matryoshkas with _Mmax_ = _S_ ;
these are obtained by choosing arbitrary Matryoshkas _M_ 1 _, . . ., Mk_ on _P_ 1 _, . . ., Pk_, that
is, faces _F_ 1 _, . . ., Fk_ on the corresponding cosmohedral fans. Furthermore, we have



_k_


dim _Fi._

_i_ =1



dim _F_ = 1 + _|M_ not min _|_ = 1 +



_k_


( _|_ ( _Mi_ )not min _|_ + 1) = 1 +

_i_ =1



so the _f_ -numbers of the cosmohedron Cosmo _n−_ 1 are given by the recurrence




 - 
_t_ [codim] _[ F]_ = 1 + _t_

_F_ _≤_ Cosmo _n−_ 1 _A_ ⪇Assoc




  _fn_ ( _t_ ) =



_fn_ 1( _t_ ) _· · · fnk_ ( _t_ ) _._ (11)
_A_ ⪇Assoc _n−_ 1



Adding the full face Assoc _n−_ 1 to both sides, we obtain


       _gn_ ( _t_ ) = _fA_ ( _t_ ) (12)

_A≤_ Assoc _n−_ 1


using the notation of [AA23]: if _x_ 1 _, x_ 2 _, . . .,_ is a sequence and a face _A_ of the associahedron
Assoc _n−_ 1 is combinatorially a product of associahedra Assoc _n_ 1 _−_ 1 _× · · ·_ Assoc _nk−_ 1, then
we write _xA_ = _xn_ 1 _· · · xnk_ .
Arriving at (12) is a pleasant d´ej`a vu: the associahedral version of Lagrange inversion
obtained in [AA23, Theorem 2.4.3] tells us that this recurrence is precisely equivalent
to the assertion that _x_ _−_ _f_ 1( _t_ ) _x_ [2] _−_ _f_ 2( _t_ ) _x_ [3] _−_ _. . ._ and _x_ + _g_ 1( _t_ ) _x_ [2] + _g_ 2( _t_ ) _x_ [3] + _. . ._ are
compositional inverses.
The second formulation follows from the first by a straightforward computation.


A pleasant feature of this proof is that Aguiar and Ardila discovered the associahedral
version of Lagrange inversion in [AA23, Theorem 2.4.3] within the Hopf-algebraic structure
of Loday’s associahedra, specifically. Is it coincidental that this is the same associahedron
we constructed? Might there be a deeper underlying algebraic explanation? Cosmohedra
feature an operadic structure that is the subject of an upcoming paper.


**Corollary** **5.5.** _The_ _f_ _-polynomials_ _of_ _the_ _cosmohedral_ _fans_ _are_ _given_ _by_ _the_ _recurrence_
_f_ 1( _t_ ) = 1 _and_




_· · ·_ _for_ _n ≥_ 2 _._
_a_ 2!




[(] _[t]_ [)] _[a]_ [1] _f_ 2( _t_ ) _[a]_ [2]

_a_ 1! _a_ 2!




   _fn_ ( _t_ ) = 1 + _t_

1 _[a]_ [1] 2 _[a]_ [2] _···⊢n_



( _n_ + _a_ 1 + _a_ 2 + _· · ·_ )!



1 + _a_ 2 + _· · ·_ )!

_·_ _[f]_ [1][(] _[t]_ [)] _[a]_ [1]
( _n_ + 1)! _a_ 1!



_summing over the non-trivial partitions of n as a sum n_ = _a_ 1 _·_ 1+ _a_ 2 _·_ 2+ _· · ·_ + _an−_ 1 _·_ ( _n−_ 1) _._


_Proof._ This is a reformulation of the recurrence formula (11), taking into account that
the number of subdivisions of an ( _n_ + 2)-gon into _a_ 2 triangles, _a_ 3 quadrilaterals, etc. is
( _n_ + _a_ 1 + _a_ 2 + _· · ·_ )! _/_ ( _n_ + 1)! _a_ 1! _a_ 2! _· · ·_ [Sta99, Theorem 5.3.10].


35


**5.3** **Asymptotic** **growth**


**Facets.** The facets of the cosmohedron Cosmo _n−_ 1 are in bijection with the non-trivial
subdivisions of an ( _n_ +2)-gon, or equivalently the non-trivial parenthesizations of a string
of _n_ + 1 letters. Their number, listed in column 1 of Table 1, is one less than the _n_ -th
_Hipparchus–Schr¨oder_ _number_ . This is one of the oldest known combinatorial quantities,
studied by astronomer and mathematician Hipparchus in the second century B.C.; for a
fascinating historical account, see [Sta99, Sta97]. These numbers are sequence A001003
in the Online Encyclopedia of Integer Sequences; their generating function is



_x_ + _x_ [2] + 3 _x_ [3] + 11 _x_ [4] + 45 _x_ [5] + 197 _x_ [6] + _· · ·_ = [1]

4




- ~~�~~ 1 + _x −_ 1 _−_ 6 _x_ + _x_ [2]



_√_
The asymptotic growth of the sequence is controlled by 3+ 8, the inverse of the smallest

root of 1 _−_ 6 _x_ + _x_ [2] . More precisely [Knu97], the number _rn_ of rays grows like



_√_
18 _−_ 4) _/π ·_ (3 +



8) _[n]_ _· n_ _[−]_ [3] _[/]_ [2] _._



_rn_ _∼_ [1]

4




- ~~_√_~~
(



**Vertices.** The vertices of the cosmohedron Cosmo _n−_ 1 are in bijection with the maximal
Matryoshkas on an ( _n_ + 2)-gon. The following lemma is stated in [AHFV25] with a
minor typo; we include a proof.


**Lemma** **5.6.** _The_ _number_ _mn_ _of_ _maximal_ _Matryoshkas_ _on_ _an_ ( _n_ + 2) _-gon_ _is_ _given_ _by_
_the_ _recurrence_ _relation_



_m_ 1 = 1 _,_ _mn_ =



_n−_ 1


( _k_ + 1) _mkmn−k_ _for_ _n ≥_ 2 _._

_k_ =1



_The_ _formal_ _power_ _series_ _M_ ( _x_ ) = [�] _n≥_ 2 _[m][n][−]_ [1] _[x][n]_ [=] _[ x]_ [2][ + 2] _[x]_ [3][ + 10] _[x]_ [4][ + 72] _[x]_ [5][ +] _[ · · ·]_ _[is]_ _[given]_
_by_ _the_ _differential_ _equation_

_x_ [2]
_M_ _[′]_ ( _x_ ) = 1 _−_

_M_ ( _x_ ) _[.]_


_Proof._ Fix an edge _e_ of the ( _n_ + 2)-gon. A maximal Matryoshka is obtained by splitting
an ( _n_ +2)-gon into a ( _k_ +2)-gon that contains _e_ and an ( _n−k_ +2)-gon, and then putting a
maximal Matryoshka in each one of them. There are _k_ +1 possible positions for the outer
( _k_ + 2)-gon that contains _e_, and _mk_ and _mn−k_ choices for the two inner Matryoshkas,
respectively. The differential equation follows by a straightforward computation.


In particular, this means that _M_ ( _x_ ) is a _D_ -algebraic series; that is, its derivatives
satisfy a polynomial equation with coefficients in C[ _x_ ]; in fact, one of the simplest such
equations: _M_ ( _x_ ) = _x_ [2] + _M_ ( _x_ ) _M_ _[′]_ ( _x_ ). Compare this with the algebraic power series
for Catalan numbers, which satisfies one of the simplest algebraic equations _C_ ( _x_ ) =
1 + _xC_ ( _x_ ) [2] .
Melczer [Mel21] writes that “ _D-algebraic_ _series_ _seem_ _to_ _be_ _on_ _the_ _border_ _between_
_decidability and undecidability, perhaps tipped to the side of undecidability._ _[...]_ _Compared_


36


_to_ _D-finite_ _functions,_ _not_ _much_ _is_ _known_ _about_ _D-algebraic_ _asymptotics,_ _and_ _in_ _general_
_not_ _much_ _can_ _be_ _said._ ”. Since _M_ ( _x_ ) is one of the simplest _D_ -algebraic series, the
following conjecture of Kotesovic, based on numerical evidence, is an interesting challenge.


**Conjecture** **5.7.** _[KI14]_ _The_ _number_ _of_ _Matryoshkas_ _grows_ _asymptotically_ _like_


_mn_ _∼_ _c · n_ ! _· n_ [4]


_for_ _c_ = 0 _._ 005428 _. . .._


**All** **faces.** A more ambitious goal would be to find the asymptotics for the total number
of faces, or even the limit distribution of the normalized _f_ -vector. We do not know how
to do this.


**5.4** **Counting** **the** **faces** **of** **the** **correlatron**


Another object that naturally arises in physics, and that is intimately related to the
cosmohedron, is the _correlatron_ introduced by Figueiredo and Vaz˜ao in [FV26]. This
polytope captures the combinatorics of the correlator, a physical observable that can
be computed from the wavefunction. The combinatorial structure of this object is
described by the interacting combinatorics of chords (the combinatorics of associahedra)
and subpolygons (the combinatorics of cosmohedra).


Figure 19: The three-dimensional correlatron.


The correlatron is an unbounded _n_ -dimensional polyhedron, with faces of two kinds:
1. The bounded faces of the correlatron are labelled by the compatible pairs ( _C, M_ ),
consisting of a set _C_ of non-crossing chords and a Matryoshka _M_ on an ( _n_ +2)-gon. Here
_C_ and _M_ are _compatible_ if no chord in _C_ intersects a polygon in _M_ ; or equivalently, if _C_


37


is a subset of the diagonals in the underlying subdivision _M_ max of _M_ . The bounded face
inclusions of the correlatron are given by the reverse inclusion of chords and Matryoshkas:


_{C_ _[′]_ _, M_ _[′]_ _}_ is a face of _{C, M_ _}_ in the correlatron if and only if _C_ _⊆C_ _[′]_ and _M_ _≤_ _M_ _[′]_ _._


2. The unbounded faces are labeled by chords _C_, which we underline to distinguish
them easily from the earlier faces. An unbounded face _C_ is contained in _C_ _[′]_ if and only if
_C_ _⊆C_ _[′]_ . An unbounded face _C_ also contains the bounded faces ( _C_ _[′]_ _, M_ _[′]_ ) such that _C_ _⊆C_ _[′]_ .
Note in particular that the correlatron has a bottom cosmohedral facet Cosmo _n−_ 1
corresponding to the pairs of the form ( _∅, M_ ). Its unbounded directions look like a cone
over Assoc _n−_ 1. Since the unbounded faces of the correlatron are enumerated by the
well-known _f_ -vector of the associahedron, we focus on enumerating the bounded part.

|correlatron|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|0<br>1<br>2<br>3<br>4<br>5<br>6|0<br>0<br>0<br>0<br>0<br>0<br>0|1<br>3<br>11<br>45<br>197<br>903|4<br>35<br>251<br>1694<br>11158|25<br>405<br>4592<br>44932|200<br>4984<br>80036|1890<br>65606|20248|



Table 2: The number of _d_ -codimensional faces of the _n_ th bounded correlatron.


**Theorem** **5.8.** _The_ _reverse_ _f_ _-polynomials_ _of_ _the_ _bounded_ _correlatrons_ _h_ 1( _t_ ) = _t, h_ 2( _t_ ) =
3 _t_ +4 _t_ [2] _, h_ 3( _t_ ) = 11 _t_ +35 _t_ [2] +25 _t_ [3] _, . . . form the unique sequence {hn_ ( _t_ ) _}n≥_ 1 _of polynonmials_
_such_ _that_ _the_ _power_ _series_ _in_ (R[ _t_ ])[ _x_ ]


_x_ + _h_ 1( _t_ ) _x_ [2] + _h_ 2( _t_ ) _x_ [3] + _h_ 3( _t_ ) _x_ [4] + _. . ._

_x −_ _tg_ 1( _t_ ) _x_ [2] _−_ _tg_ 2( _t_ ) _x_ [3] _−_ _tg_ 3( _t_ ) _x_ [3] + _. . ._



_are compositional inverses, where gn_ ( _t_ ) = [(1+ _t_ ) _fn_ ( _t_ ) _−_ 1] _/t and fn_ _is the f_ _-polynomial of_
_the nth cosmohedral fan._ _Equivalently, the power series Ht_ ( _x_ ) = _x_ + _h_ 1( _t_ ) _x_ [2] + _h_ 2( _t_ ) _x_ [3] + _. . ._
_satisfies_



_Ht_




- ( _t_ + 1) _x_ 2 _−_ _tx_ + ( _t_ + 1) _At_ ( _x_ ) = _x_
1 _−_ _x_



_where_ _At_ ( _x_ ) _is_ _the_ _generating_ _function_ _for_ _the_ _f_ _-vectors_ _of_ _cosmohedra_ _in_ _Theorem_ _5.4._


_Proof._ Every face _F_ of the truncated correlatron corresponds to a pair ( _C, M_ ) where
_M_ is non-trivial. Let _C_ create a subdivision into polygons _P_ 1 _, . . ., Pk_, and let _A_ ( _F_ ) be
the corresponding face of the associahedal fan corresponding to the set of chords _C_ . A
Matryoshka _M_ compatible with _C_ restricts to Matryoshkas _M_ 1 _, . . ., Mk_ on _P_ 1 _, . . ., Pk_ .
One can almost recover _M_ from the _Mi_ s: the only additional information is whether
_M_ contains the polygon _Pi_ (in which case we let _εi_ = 1) or it does not (in which case


38


_εi_ = 0). We note that if _Mi_ is the trivial Matryoshka on _Pi_, then _εi_ = 1 necessarily; if
_Mi_ is non-trivial, then _εi_ can be chosen freely. Finally notice that



_k_


( _εi −_ 1)

_i_ =1



_k_

- _|_ ( _Pi_ )non-min _|_ +


_i_ =1



Therefore



codim _F_ = _|C|_ + _|M_ non-min _|_ = _k_ +


   _hn_ ( _t_ ) = _t_ [codim] _[ F]_


_F_ _≤_ BdCorrela _n_




  =


_A≤_ Assoc _n_
_S_ ( _A_ )= _{P_ 1 _,...,Pk}_




 _t_ _[k]_


_M_ 1 _,...,Mk_
_ε_ 1 _,...,εk_




- _k_ 
 
_t_ _[|]_ [(] _[P][i]_ [)][non-min] _[|]_ [+] _[ε][i][−]_ [1]

_i_ =1




      
 
_t_ _[|]_ [(] _[P][i]_ [)][non-min] _[|]_ 1 + [1]

_t_

_Mi_ = _{Pi}_



_k_

 - 
_t_ _[|C|]_

_A≤_ Assoc _n_ _i_ =1


_k_

 - 
_t_ _[|C|]_

_A≤_ Assoc _n_ _i_ =1







_t_




 =




 1 +




- []






_i_ =1




 =




- 1 + ( _fPi_ ( _t_ ) _−_ 1) 1 + [1]



��



_i_ =1




- 1 + ( _fPi_ ( _t_ ) _−_ 1) 1 + [1] _t_




 = _t_


_A≤_ Assoc _n_



_k_


((1 + _t_ ) _fPi_ ( _t_ ) _−_ 1)
_i_ =1




 = _tgA_ ( _t_ ) _,_

_A≤_ Assoc _n_



again using the notation of [AA23]. The associahedral version of Lagrange inversion

[AA23, Theorem 2.4.3] then tells us that _x −_ _tg_ 1( _t_ ) _x_ [2] _−_ _tg_ 2( _t_ ) _x_ [3] _−_ _tg_ 3( _t_ ) _x_ [4] + _. . ._ and
_x_ + _h_ 1( _t_ ) _x_ [2] + _h_ 2( _t_ ) _x_ [3] + _h_ 3( _t_ ) _x_ [3] + _. . ._ are compositional inverses.
The second formulation follows from a straightforward computation.


Note the remarkable similarity between the formulas in Theorems 5.4 and 5.8 for
the _f_ -vectors of the cosmohedron and bounded correlatron. Is this an indication of
something deeper?

### **6 Elusive qualities of the cosmohedron**


The cosmohedron is related to several beautiful polytopes in the literature, either through
direct connections or indirect analogies. These include the permutahedron [BS13, Sch13],
the associahedron [Lod04, Sta63], graph associahedra [CD06], the nested permutahedron

[CL22], the permutoassociahedron [CL23], and the permutonestohedron [Gai15], among
others.
However, there are numerous ways in which the combinatorial structure of the
cosmohedron is more subtle than its predecessors. In turn, this makes it significantly


39


harder to prove the correctness of this construction. In this section, we discuss some of
the intricacies that arise - and that remain in future polytopes of interest.


**The cosmohedron is not very symmetric.** The permutahedron, the nested permutahedron,
the permuto-associahedron, and the permutonestohedron are symmetric under the natural
action of _Sn_ onto R _[n]_ . This allows us to express them as the convex hull of the _Sn_ -orbit
of a point, or of a carefully placed permutahedron or associahedron, respectively. The
cosmohedron only has a natural action of the dihedral group.
The cosmohedron is made of an associahedron’s worth of different bracket associahedra.
It requires much greater care to choose a suitable realization of each bracket associahedron
that are compatible with each other, and then place each one of them at the correct
position, in order to make sure that they glue correctly into a well-behaved global
polytope. This is a subtle matter.


**The** **cosmohedron** **is** **not** **simplicial.** This is not a surprise; none of the polytopes on
the above list are simplicial. Proposition 5.3 shows that the only simplicial faces of the
cosmohedron are the vertices and edges.


**The cosmohedron is not simple.** This is more surprising, because all the other polytopes
in the list above are simple. The only simple vertices of the cosmohedron are those whose
Matryoshka is nested linearly. To see this, let _M_ = ( _T, B_ ) be a maximal Matryoshka.
The facets of cone( _M_ ) correspond to the facets of cone _T_ ( _B_ ) _≥_ 0. These in turn correspond
to the _n −_ 2 facets of cone _T_ ( _B_ ) (which is simplicial), and the facets of the form _ye_ _≥_ 0
for a minimal bracket in _B_, which is an edge in _B_, and corresponds to a quadrilateral
in _M_ . Therefore


(number of facets of cone( _M_ )) = _n −_ 2 + (number of quadrilaterals in _M_ ) _._


This can be any number between _n −_ 1 and _⌊_ 3 _n/_ 2 _⌋−_ 2. It equals _n −_ 1 precisely if _M_
has exactly one quadrilateral, which happens precisely when _M_ is linearly nested.
Why is this a challenge? The fact that polytopes like (bracket) associahedra are
simple allows for a flexible construction. One can start with an easy polytope (in these
cases a simplex), and then create new facets one at a time by making cuts that are “not
too deep”, so that the facets meet transversally. The required care only involves depth
inequalities; see [Lod04, Dev09, PPP23].
We **do** construct the cosmohedron through a chiseling of faces of the associahedron,
but we have to be much more careful now: the chiseling has to line up perfectly to create
the required non-transversal crossings. The required care now involves many equalities
as well as inequalities. In AFV _n−_ 1, these equalities manifest in the fact that the linear
forms [�] _C∈C_ _[X][C]_ [satisfy many linear relations between them.] [In Cosmo] _[n][−]_ [1][, they manifest]
in the many requirements _bB_ = _bB′_ in Remark 4.12.


**The** **cosmohedron** **depends** **delicately** **on** **the** **chiseling.** To further illustrate the point
above, recall that in our construction of the cosmohedron, we chiseled a Devadoss
bracket associahedron at each vertex of the associahedron. This choice is important. For


40


instance, despite their usefulness in other settings, the Postnikov bracket associahedra
do not produce the cosmohedron upon chiseling.


**We** **don’t** **know** **the** **cosmohedron** **to** **be** **a** **deformation** **of** **an** **easy** **polytope.** The
_deformations of the permutahedron_, also known as _generalized permutahedra_ or _polymatroids_,
are obtained from the permutahedron by moving facets without pushing them past
vertices. They are characterized by having the same edge directions as the permutahedron,
namely _ei −_ _ej_ for _i ̸_ = _j_ [ACEP20, Prop. 2.6], [Pos09].
Generalizing this setup, Castillo and Liu [CL22] defined the _nested_ _permutahedron_
Perm( _α, β_ ) by placing an ( _n−_ 1)-permutahedron at each corner of the _n_ -permutahedron.
They studied its deformations, and showed that Kapranov’s _permutoassociahedron_ [Kap93]

- which has an ( _n −_ 1)-associahedron at each vertex of the _n_ -permutahedron, can be
obtained as a deformation of Perm( _α, β_ ).
The cosmohedron would seem to fit in the same framework; our proof of Theorem 3.6
even shows that the cosmohedron has the same edge directions as Perm( _α, β_ ), namely
_ei −_ _ej_ and _ei −_ _ej_ + _ek −_ _el_ for distinct _i, j, k, l_ . This makes it natural to wonder: Is our
cosmohedron a deformation of the nested permutahedron? **It** **is** **not.**
Dually, we claim that our cosmohedral fan is not a coarsening of the nested braid
fan Br [2] _n_ [of] [Castillo] [and] [Liu] [[CL22].] [The] _[n]_ [!] _[ ·]_ [ (] _[n][ −]_ [1)!] [facets] [of] [Br][2] _n_ [correspond] [to] [the]
choices of an order _σ_ _∈_ _Sn_ of the coordinates of _x_ _∈_ R _[n]_ and an order _τ_ _∈_ _Sn−_ 1 of their
consecutive differences. For example, the set of points _x ∈_ R [4] with
_x_ 3 _> x_ 1 _> x_ 4 _> x_ 2 and _x_ 3 _−_ _x_ 1 _> x_ 1 _−_ _x_ 4 _> x_ 4 _−_ _x_ 2 _>_ 0
is a maximal open cone of Br [2] 4 [.] [Such a point must satisfy two inequalities] _[ x]_ [3] _[−][x]_ [4] _[> x]_ [3] _[−][x]_ [1]
and _x_ 1 _−_ _x_ 2 _>_ 0 of the Matryoshkal cone( _M_ 2) of Figure 9, but it may or may not satisfy
the third inequality _x_ 3 _−_ _x_ 1 _>_ _x_ 1 _−_ _x_ 2. Therefore, this maximal cone of Br [2] 4 [intersects]
cone( _M_ 2) full-dimensionally, but is not contained in it. This proves our claim.
Why is this a challenge? Generalized permutahedra are in bijection with submodular
functions on the subsets of [ _n_ ]. Thus to construct them, it is sufficient to choose the
correct submodular function, and to use the theory of polymatroids and generalized
permutahedra to prove the correct combinatorial structure; see [AA23, Pos09].
We do not know an analog to the permutahedron for this setting. It would be
very interesting to find a nice polytope such that (i) it can be deformed to obtain the
cosmohedron, (ii) its deformation cone can be nicely described combinatorially, and (iii)
the face structure of its deformations is combinatorially well-behaved.


**We** **don’t** **know** **the** **cosmohedron** **to** **be** **a** **Minkowski** **sum** **of** **easy** **polytopes.** The
permutahedron, Loday’s associahedron, and Postnikov’s graph and bracket associahedra
can all be expressed as Minkowski sums of faces of the standard simplex. This gives a
simple proof that their face structure– the common refinement of the easy face structures
of the summands - is correct. For details, see [Pos09].
We do not know how to do this in our setting. It would be interesting to find
a realization of the cosmohedron that can be decomposed easily and usefully into a
Minkowski sum.


41


**The** **faces** **of** **the** **cosmohedron** **only** **factor** **combinatorially.** As discussed in Lemma
5.2, faces of a generalized permutahedra factor into smaller generalized permutahedra

[AA23, Edm70]. For permutahedra, associahedra, and graph associahedra, any facet of a
polytope in these families is a product of smaller polytopes in the same family. This gives
an inductive strategy to prove their combinatorial structure, introduced for associahedra
in [MSS02]. One simply needs to guarantee that the facets are placed correctly; again,
because these polytopes are simple, this step only requires verifying the appropriate
depth inequalities. Once the facets are laid out correctly, thanks to their factorization,
the rest of the face structure can be proved recursively.
In our realization of the cosmohedron, each one of the facets is **combinatorially, but**
**not** **geometrically** a product of cosmohedra and a bracket associahedron. Therefore,
its combinatorial structure cannot be proved using this inductive strategy. It would
be interesting to find a realization of the cosmohedron where the face factorization of
Proposition 5.3 holds geometrically.


**Outlook:** **chiseled** **polytopes.** In an upcoming paper, we present a general family of _X_
_in_ _Y_ polytopes that contains all of the polytopes above, and numerous other polytopes
of interest, old and new. Our proof strategy for the combinatorial structure of the
cosmohedron is very well suited to this general setting. In the Appendix, we provide
some physical motivation for this general construction, by sketching a new motivating
example: we introduce the _one-loop_ _U_ _-polytope_, which captures the combinatorics of all
one-loop cubic (trivalent) graphs, as well as the Feynman polytope for the Symanzik
_U_ -polynomial of each graph, all in one polytope.

### **7 Acknowledgements**


The work of Federico Ardila–Mantilla was supported by the National Science Foundation
(Grant DMS 2154279) in the United States, a Wolfson Fellowship of The Royal Society
in the United Kingdom, and the Friends of the Institute for Advanced Study Fund
at the IAS. The work of Nima Arkani-Hamed was supported by the DOE (Grant
No. DE-SC0009988), the Simons Collaboration on Celestial Holography, the European
Union (ERC, UNIVERSE PLUS, 101118787), and the Carl B. Feinberg cross-disciplinary
program in innovation at the IAS. The work of Carolina Figueiredo was supported by
FCT/Portugal (Grant No. 2023.01221.BD). The work of Francisco Vaz˜ao was supported
by the Jonathan M. Nelson Center for Collaborative Research. Views and opinions
expressed are those of the author(s) only and do not necessarily reflect those of the
European Union or the European Research Council Executive Agency. Neither the
European Union nor the granting authority can be held responsible for them.

### A Appendix: X in Y polytopes


The main focus of this paper has been to explore and prove the mathematical properties
of cosmohedra, which encode the cosmological wavefunction of Tr( _ϕ_ [3] ) theory. We use


42


this appendix to discuss how the principles that guided the construction of cosmohedra
are of much broader relevance.


**A.1** **The** **cosmohedron** **as** **a** **guiding** **example** **for** _X_ **in** _Y_ **polytopes**


As we have learned by now, cosmohedra encode geometrically the combinatorics of
maximal Matryoshkas of an _n_ -gon. One way to organize all such Matryoshkas is by
dividing them into classes labeled by the underlying collection of triangles - _i.e._ the
underlying triangulation. This is what naturally occurs in physics. To write down
the cosmological wavefunction, we start by listing all possible cubic (trivalent) graphs,
which correspond to all possible triangulations. Then, for each cubic graph, we consider
all possible ways of finding maximal collections of nested subgraphs, which give the
possible maximal Matryoshkas compatible with the respective underlying triangulation.
The cosmohedron is then the object that puts both combinatorial problems together. In
particular, to find the cosmohedron we first needed to find two other polytopes:


Y. The underlying polytope whose vertices label all possible triangulations/diagrams

   - which at tree-level is simply the associahedron;


_X_ . A class of polytopes, one associated to each triangulation, whose vertices label all
possible Matryoshkas compatible with the respective triangulation – which is done
by the bracket associahedon _XT_ for each triangulation _T_ .


Once we have these two objects under control, we “blow up” each vertex _vT_ of _Y_
into the respective _X_ polytope _XT_, via the chiseling procedure described earlier. At the
level of the normal fans, we subdivide each cone of the fan of _Y_ using the corresponding
normal fan in the family _X_ .
Therefore, for any given combinatorial problem, where on top of listing all possible
diagrams ( _Y_ ), we also want to keep track of some further information _XG_ of **each**
diagram _G_ ( _X_ ). Once we find the polytopes for _X_ and _Y_ separately, we can seek to
define the polytope that captures the full combinatorics ( _X_ in _Y_ ) by the procedure
described above.
As it turns out, such situations are ubiquitous in physics, and not just in the
mathematical settings discussed in Section 6. In this appendix, we will discuss a
particular example, simply to illustrate how this construction generalizes to other contexts.


**A.2** **The** _U_ **-polytope** **for** **one-loop-integrated** **amplitudes**


At loop-level, the amplitudes are expressed as a sum of _Feynman_ _integrals_, which often
diverge at the boundaries of the integration domain. Thus, it is important to record the
asymptotic behavior of the integrands. The most transparent way to do this is by using
the projective representation of Feynman integrals in terms of _Schwinger_ _parameters_ _αe_

- one for each edge of the Feynman diagram _G_ - where they take the following form:




    _IG_ = Γ( _d_ )

RP _[E][−]_ [1]

_>_ 0




- _e∈G_ _[dα][e]_ 1

_._

GL(1) _UG_ _[D/]_ [2] _[−][d]_ _FG_ _[d]_


43


Here _d_ = _E_ _−_ _LD/_ 2 is the _superficial_ _degree_ _of_ _divergence_ of a graph _G_ with _E_ edges
and genus _L_ (number of independent loops) in spacetime dimension _D_, and _UG_ and _FG_
are the first and second _Symanzik_ _polynomials_ of _G_ :



_UG_ = 

_T_ tree of _G_




- 
_αe,_ _FG_ =

_e/∈T_ _T_ 2-tree







_T_ 2-tree of _G_





_αe._

_e/∈T_



The sum in _UG_ is over all spanning trees of _G_, and the sum in _FG_ is over all spanning
_2-trees_ _T_ 1 _⊔_ _T_ 2, where _T_ 1 and _T_ 2 are two vertex-disjoint trees that span all vertices of _G_ .
To correctly describe the divergences of _IG_, one needs to characterize the asymptotic
behavior of _UG_ and _FG_ .
Therefore, at one-loop level, we are looking for an object that captures not only
all possible cubic (trivalent) one-loop graphs _G_ (collected in a polytope _Y_ ), but also
the possible leading monomials in _UG_ and _FG_ for each graph _G_ (collected in a family
of polytopes _X_ ). As it turns out, the polytopes Y and _X_ polytopes are known in the
physics and mathematics literature [AH, AHHM22, BR25, Edm70]. We will show how
to combine them together into a single chiseled polytope. This answers a question posed
in [AHFS [+] 25].
In this Appendix, we illustrate the essential ideas behind the construction in a simple
but already interesting case: the asymptotic behaviors of the _U_ -polynomials in the
one-loop setting. In an upcoming paper, we will treat the general setting of higher
loops, and consider both Symanzik polynomials _F_ and _U_ .


**A.2.1** **The** _Y_ **polytope:** **the** **one-loop** **associahedron**


The _one-loop_ _associahedron_ is a polytope designed to parameterize the triangulations
of a polygon _n_ [with] [one] [puncture.] [Consider] [an] _[n]_ [-gon] [with] [vertices] [cyclically] [labeled]
1 _,_ 2 _, . . ., n_ and a puncture labeled _O_ . We consider curves of two kinds:


1. _chords_ _xi,j_ that go from _i_ to _j_ while keeping the puncture _O_ to the right, for
1 _≤_ _i, j_ _≤_ _n_ . (Note that we have _diagonals_ _xi,j_ = _xj.i_ for each _i ̸_ = _j_, and _tadpoles_
_xi,i_ for each _i_ .)


2. _spokes_ _yk_ and ˜ _yk_ that spiral from _k_ into the puncture clockwise and counterclockwise,
respectively. (For simplicity, we draw straight lines from _k_ to _O_ tagged in blue and
red, respectively.)


We are interested in the triangulations of _n_ [using] [these] [curves.] [Notice] [that] [every]
triangulation uses exactly _n_ curves, and contains at least one spoke _yk_ or _y_ ˜ _k_ . Also, notice
that a clockwise and a counterclockwise spiral always intersect, so every triangulation is
monochromatic. The left panels of Figures 20 and 21 show the 6 triangulations (and six
coarser subdivisions) for _n_ = 2, and the 10 blue triangulations for _n_ = 3, respectively
The _loop_ _associahedron_ was first introduced in [AH]; it is a variant of the cluster
polytopes in [AHHST22] that includes the _tadpole_ curves, _xi,i_ . For the punctured
_n_ -gon, we get an _n_ -dimensional simplicial polytope whose vertices correspond to the
triangulations of _n_ [.] [Its] [faces] [correspond] [to] [the] [partial] [triangulations] [or] [subdivisions]


44


of _n_ [,] [and] [the] [containment] [relations] [of] [the] [faces] [match] [the] [reverse] [inclusion] [relations]
of the sets of curves. The left panels of Figures 22 and 23 respectively illustrate the
one-loop associahedra for 2 [and] 3 [.]


**A.2.2** **The** _X_ **polytopes:** **Feynman** **polytopes**


The asymptotic behavior of the Symanzik polynomials _UG_ and _FG_ is fully characterized
by their Newton polytopes in R _[E]_ [(] _[G]_ [)] :


_UG_ = Newt( _UG_ ) _,_ _FG_ = Newt( _FG_ )


called _Feynman_ _polytopes_ and studied in [AHHM22].
Since _UG_ and _FG_ are squarefree, _UG_ and _FG_ are 0-1 polytopes. The exponents of _UG_
(resp. _FG_ ) are the complements of the spanning trees (resp. 2-trees) of graph _G_, which
are the bases of the matroid _M_ ( _G_ ) (resp. the truncation matroid Tr _M_ ( _G_ )). It follows
that
_UG_ = _PM_ ( _G_ ) _⊥,_ _FG_ = _P_ (Tr _M_ ( _G_ )) _⊥_


where _PM_ denotes the matroid (basis) polytope of _M_ and _[⊥]_ denotes matroid duality.
In this appendix, for clarity and simplicity, we focus on the first Symanzik polynomials
in the one-loop setting. When _G_ only has one cycle, the polynomial _UG_ is simply the sum
of all variables _αe_ associated to the edges _e_ of that cycle, and the Feynman polytope is just
the standard simplex on those edges. We summarize this by writing that _UG_ = ∆Cycle( _G_ )
in the one-loop setting. Note that, unlike in the setting of cosmohedra, this polytope is
usually low-dimensional.


**A.2.3** **Towards** **a** **general** **construction:** _X_ **in** _Y_ **fans** **in** **dimensions** **2** **and** **3**


To motivate the general construction, let us first carry it out in detail in dimensions 2 and
3, beginning at the level of fans. The fan of the one-loop associahedron has a ray for each
curve of _n_ [,] [and] [a] [face] [cone(] _[C]_ [)] [for] [each] [collection] [of] _[C]_ _[⊂]_ [Curves(] _n_ [)] [of] [compatible]
curves, or equivalently, each subdivision of _n_ [.] [We] [need] [to] [subdivide] [the] [cones] [of] [this]
fan to keep track of the dominant terms of the corresponding _U_ -polynomials.



**Example** **A.1.** _For_ _n_ = 2 _there_ _are_ _three_ _blue_ _and_ _three_ _red_ _triangulations_ _of_ 2 _[.]_ _[Their]_
_cones_ _naturally_ _fit_ _into_ _a_ _complete_ _fan_ _in_ _the_ _plane_ _shown_ _in_ _the_ _left_ _panel_ _of_ _Figure_
_20._ _The_ _only_ _diagrams_ _with_ _a_ _non-trivial_ _U_ _polynomial_ _are_ _the_ _ones_ _with_ _two_ _spokes,_
_corresponding to the positive and negative quadrants of the fan._ _The dual diagram of these_
_triangulations_ _is_ _the_ _bubble_ _diagram_ _with_ _two_ _parallel_ _edges_ _α_ 1 _and_ _α_ 2 _;_ _its_ _U-polynomial_



_is_ _simply:_ _U_






= _α_ 1 + _α_ 2 _,._



_We_ _wish_ _to_ _divide_ _each_ _such_ _cone_ _into_ _two_ _subcones,_ _depending_ _on_ _which_ _term_ _of_
_U_ _dominates:_ _α_ 1 _or_ _α_ 2 _._ _We_ _can_ _easily_ _do_ _this_ _by_ _subdividing_ _them_ _in_ _half,_ _adding_ _the_
_rays_ _g_ 1 _,_ 2 = _g_ 1 + _g_ 2 _and_ _g_ ˜1 _,_ 2 = _g_ ˜1 + ˜ _g_ 2 _respectively._ _Here_ _gi_ _are_ _the_ _usual_ _g_ -vectors _for_
_the_ _spokes_ _curves,_ _which_ _are_ _the_ _rays_ _of_ _the_ _loop_ _associahedral_ _fan._ _This_ _subdivision_ _is_
_shown_ _in_ _the_ _right_ _panel_ _of_ _Figure_ _20._


45


Figure 20: (a) Fan of the two-dimensional one-loop associahedron. (b) Refinement of a
cone in the fan to encode the dominating terms of the _U_ -polynomial.


**Example** **A.2.** _For_ _n_ = 3 _there_ _are_ _10_ _blue_ _(and_ _10_ _red)_ _triangulations_ _of_ _the_ _punctured_
_disk_ _with_ _three_ _marked_ _points_ _on_ _the_ _boundary_ 3 _[.]_ _[They]_ _[label]_ _[the]_ _[maximal]_ _[cones]_ _[of]_ _[the]_
_fan_ _shown_ _on_ _the_ _left_ _of_ _Figure_ _21;_ _this_ _is_ _the_ _blue_ _half_ _of_ _the_ _one-loop_ _associahedral_ _fan._
_The_ _red_ _half_ _is_ _isomorphic,_ _and_ _is_ _glued_ _to_ _this_ _one_ _along_ _the_ _boundary_ _in_ _the_ _opposite_
_orientation._ _Together_ _they_ _form_ _a_ _complete_ _three-dimensional_ _fan._



21



21

























32



13











Figure 21: (a) Half-fan of the three-dimensional one-loop associahedron. (b) Half-fan of
the three-dimensional one-loop _U_ -polytope.


_Again,_ _for_ _each_ _triangulation_ _C_ _with_ _two_ _spokes_ _yi_ _and_ _yj,_ _we_ _introduce_ _a_ _new_ _ray_
_gij_ = _gi_ + _gj_ _that_ _subdivides_ _the_ _corresponding_ _cone_ _in_ _half._ _But_ _now_ _there_ _is_ _also_ _a_
_triangulation_ _with_ _three_ _spokes_ _y_ 1 _, y_ 2 _, y_ 3 _,_ _with_ _U_ _polynomial_ _α_ 1 + _α_ 2 + _α_ 3 _._ _We_ _subdivide_
_its_ _face_ cone( _g_ 1 _, g_ 2 _, g_ 3) _by_ _introducing_ _four_ _new_ _rays_ _g_ 1 _,_ 2 = _g_ 1 + _g_ 2 _,_ _g_ 2 _,_ 3 = _g_ 2 + _g_ 3 _,_ _g_ 1 _,_ 3 =
_g_ 1 + _g_ 3 _,_ _and_ _that_ _span_ _three_ _full-dimensional_ _subcones:_ cone1 = cone( _g_ 1 _, g_ 1 _,_ 2 _, g_ 1 _,_ 3 _, g_ 1 _,_ 2 _,_ 3) _,_


46


cone2 = cone( _g_ 2 _, g_ 1 _,_ 2 _, g_ 2 _,_ 3 _, g_ 1 _,_ 2 _,_ 3) _, and_ cone3 = cone( _g_ 3 _, g_ 1 _,_ 3 _, g_ 2 _,_ 3 _, g_ 1 _,_ 2 _,_ 3) _._ _This is illustrated_
_on_ _the_ _right_ _side_ _of_ _Figure_ _21._ _Already_ _in_ _this_ _example,_ _we_ _see_ _that_ _the_ _fan_ _is_ _not_
_simplicial,_ _and_ _therefore_ _the_ _U-polytope_ _will_ _not_ _be_ _simple._


**A.2.4** **The** **normal** **fan** **of** **the** _U_ **-polytope**


Now we are ready to describe the general construction of the _U_ -fan.


**Fan** **of** **the** **one-loop** **associahedron.** The fan of the one-loop associahedron [AH] has a
ray for each curve of _n_ [,] [and] [a] [face] [cone(] _[C]_ [)] [for] [each] [collection] [of] [compatible] [curves,]
_C_ _⊂_ Curves( _n_ [),] [or equivalently,] [each subdivision of] _n_ [.] [This is a simplicial fan whose]
cones are ordered by reverse inclusion:


cone( _C_ ) _⊆_ cone( _C_ _[′]_ ) if and only if _C_ _⊆C_ _[′]_ _._



**Fan** **of** **the** _U_ **polytope.** Now consider a facet cone( _C_ ) of the one-loop associahedron,
corresponding to a triangulation _C_ of _n_ [.] [In the polytope, we wish to replace the vertex]
_vC_ with a simplex ∆Spokes( _C_ ), since the spokes of _C_ correspond to the edges in the unique
loop of the cubic diagram dual to _C_ . Therefore we need to subdivide the simplicial
face cone( _C_ ) into _|_ Spokes( _C_ ) _|_ maximal cones. If cone( _C_ ) is regular then the _s_ -th cone
cone( _C, s_ ) consists of the points in cone( _C_ ) whose closest spoke-ray is _gs_ . If it is not, we
linearly transform it into a regular cone, and use that subdivision. Explicitly, we obtain
new rays

      -      _gS_ = _gs,_ _g_ ˜ _S_ = _g_ ˜ _s_




- 
_gs,_ _g_ ˜ _S_ =

_s∈S_ _s∈S_



_g_ ˜ _s_

_s∈S_



for each subset _S_ _⊆_ [ _n_ ] and more generally, a new cone


cone( _C, S_ ) = cone( _{gij_ : _xij_ _∈_ Chords( _C_ ) _} ∪{gT_ : _S_ _⊆_ _T_ _⊆_ Spokes( _C_ ) _}_ )


for each non-crossing set of curves _C_ and each non-empty subset _∅̸_ = _S_ _⊆_ Spokes( _C_ ) where we allow the exception _S_ = _∅_ for the sets _C_ with no spokes.
Note that cone( _C, S_ ) is a _|_ Chords( _C_ ) _|_ -fold cone over a ( _|_ Spokes( _C_ ) _| −|S|_ )–cube. We
have
cone( _C, S_ ) _⊆_ cone( _C_ _[′]_ _, S_ _[′]_ ) if and only if _C_ _⊆C_ _[′]_ and _S_ _⊇S_ _[′]_ _,_


The blue and red fans glue along the “equatorial complex” of (necessarily lower-dimensional)
faces cone( _C, ∅_ ) such that _C_ has no spokes.


**A.2.5** **The** _U_ **-polytope**


We now construct a geometric realization of the _U_ -polytope, given by the appropriate
chiseling procedure that creates, at each vertex of the underlying _Y_ -polytope, the respective
_X_ -polytope. We understood above how to subdivide the normal fan of the loop associahedron
to get the normal fan of the _U_ -polytope - and therefore we have its new facet normals
_gS_ and _g_ ˜ _S_ for _S_ _⊆_ [ _n_ ] . However, as we saw for the cosmohedron, it is a subtle matter to


47


determine how deeply we need to chisel in each direction to obtain the correct polytope.
This is controlled by the constants _ϵS_ and _ϵ_ ˜ _S_ .appearing in the new facet inequalities
_gS_ _· x ≥_ _ϵS_ and _g_ ˜ _S_ _· x ≥_ _ϵ_ ˜ _S_ .
Given a vector c of positive parameters _crs_, _cr_ and _c_ ˜ _r_ for 1 _≤_ _r, s_ _≤_ _n_, the _one-loop_
_associahedron_ _L_ 1(c) defined in [AH, BR25] is the _n_ -dimensional polytope



_L_ 1(c) =





( _x, y,_ ˜ _y_ ) _∈_ R [Curves(] _n_ +2 [)] : [ _xr,s_ _≥_ 0 _,_ _yr_ _≥_ 0 _,_ _y_ ˜ _r_ _≥_ 0 ] _,_


 _xr,r_ + _xr_ +1 _,r_ +1 _−_ _xr_ +1 _,r −_ _yr −_ _y_ ˜ _r−_ 1 = _cr_ +1 _,r,_







(13)




_xr,s_ +1 + _xr−_ 1 _,s −_ _xr,s −_ _xr−_ 1 _,s−_ 1 = _crs_ for _r_ = _{s_ + 1 _, s},_











_yr_ + ˜ _yr −_ _xr_ +1 _,r_ +1 = _cr_ +1 _._


where we set to 0 any variables that are undefined because their subscripts are outside
of the prescribed ranges. In this equation, we are writing vectors in R [Curves(] _n_ +2 [)] in the

form ( _x, y,_ ˜ _y_ ) _∈_ R [Chords(] _n_ +2 [)] _×_ R [Spokes(] _n_ +2 [)] _×_ RSpokes(� _n_ +2 [)] where _x_ = ( _xr,s_ )1 _≤r,s≤n_,
_y_ = ( _yr_ )1 _≤r≤n_, and _y_ ˜ = (˜ _yr_ )1 _≤r≤n_ .
To construct our _U_ -polytope, we need to introduce new facet inequalities of the form:

   -    



- 
_yk_ _≥_ _ϵS,_

_k∈S_ _k∈S_



_y_ ˜ _k_ _≥_ _ϵ_ ˜ _S_ for _∅̸_ = _S_ _⊆_ [ _n_ ] (14)

_k∈S_



for the possible subsets of spokes. A first condition on the _ϵ_ s is that they should be small
enough in relation to the _c_ s that the chiseling will not remove any faces of _L_ 1(c). The
parameters must also satisfy the equalities


_ϵS_ 1 + _ϵS_ 2 = _ϵS_ 1 _∪S_ 2 + _ϵS_ 1 _∩S_ 2 for any subsets _S_ 1 _, S_ 2 with _S_ 1 _∩S_ 2 = _∅_ (15)


since the corresponding rays of the normal fan satisfy _gS_ 1 + _gS_ 2 = _gS_ 1 _∪S_ 2 + _gS_ 1 _∩S_ 2, and
they lie in the same cone cone([ _n_ ] _, {ys}_ ) of the fan for any _s ∈S_ 1 _∩S_ 2. In addition, the
_ϵ_ s must satisfy the _wall-crossing_ _inequalities_


_ϵi,j_ _> ϵi_ + _ϵj_ for _i ̸_ = _j_ (16)


since the corresponding rays satisfy _gi,j_ = _gi_ + _gj_, and cone( _gi, gi,j_ ) and cone( _gj, gi,j_ ) are
distinct cones in the fan. The analogous conditions hold for the ˜ _ϵ_ ’s. One may verify that
these are all the necessary and sufficient conditions to obtain the desired _U_ -polytope.
The solutions to the system of equations (15) are of the form


_ϵ{s_ 1 _,...,sk}_ = _ϵs_ 1 + _· · ·_ + _ϵsk_ + ( _k −_ 1) _ϵ_ (17)


for any choice of _ϵ_ 1 _, . . ., ϵn, ϵ_, and the inequalities (16) are satisfied when _ϵ_ _>_ 0. The
same analysis holds for the _ϵ_ ˜’s. Thus a particularly simple choice of parameters that
cuts out a _U_ -polytope is
_ϵS_ = ˜ _ϵS_ = ( _|S| −_ 1) _ϵ ._ (18)


48


Figure 22: (a) _Y_ : Two-dimensional one-loop associahedron. (b) _X_ in _Y_ :
Two-dimensional one-loop _U_ -polytope.


for small _ϵ >_ 0. Summarizing, the _U_ -polytope is



_U_ (c) = _{_ ( _x, y,_ ˜ _y_ ) _∈_ _L_ 1(c) : 



- 
_yk_ _≥_ ( _|S| −_ 1) _ϵ,_

_k∈S_ _k∈S_



_y_ ˜ _k_ _≥_ ( _|S| −_ 1) _ϵ_ for _∅̸_ = _S_ _⊆_ [ _n_ ] _}_

_k∈S_



**Example** **A.3.** _For_ _n_ = 2 _,_ _the_ _one-loop_ _associahedron_ _is_ _the_ _intersection_ _of_ _the_ _subspace_


_y_ 1 + ˜ _y_ 1 _−_ _x_ 2 _,_ 2 = _c_ 2 _,_ _y_ 2 + ˜ _y_ 2 _−_ _x_ 1 _,_ 1 = _c_ 1 _,_

_x_ 1 _,_ 1 + _x_ 2 _,_ 2 _−_ _y_ 2 _−_ _y_ ˜1 = _c_ 1 _,_ 2 _,_ _x_ 1 _,_ 1 + _x_ 2 _,_ 2 _−_ _y_ 1 _−_ _y_ ˜2 = _c_ 2 _,_ 1 _,_ (19)


_with_ _the_ _positive_ _orthant_ _x_ 1 _,_ 1 _≥_ 0 _,_ _x_ 2 _,_ 2 _≥_ 0 _,_ _y_ 1 _≥_ 0 _,_ _y_ 2 _≥_ 0 _._ _To_ _obtain_ _the_ _U-polytope,_
_we_ _impose_ _the_ _stronger_ _inequalities_


_x_ 1 _,_ 1 _≥_ 0 _,_ _x_ 2 _,_ 2 _≥_ 0 _,_ _y_ 1 _≥_ _ϵ_ 1 _,_ _y_ 2 _≥_ _ϵ_ 2 _,_ _y_ 1 + _y_ 2 _≥_ _ϵ_ 1 + _ϵ_ 2 + _ϵ ._ (20)


_for_ _any_ _ϵ_ 1 _, ϵ_ 2 _, ϵ_ _>_ 0 _and_ _the_ _analogous_ _inequalities_ _for_ _y_ ˜ _for_ _any_ _ϵ_ ˜1 _,_ ˜ _ϵ_ 2 _,_ ˜ _ϵ_ _with_ _ϵ,_ ˜ _ϵ_ _>_ 0 _._
_Using_ _the_ _parameterization_ _ϵ_ 1 = _ϵ_ 2 = 0 _(and_ _similarly_ _for_ _ϵ_ ˜ _)_ _and_ _ϵ_ = _ϵ_ ˜ _we_ _obtain_ _the_
_correct_ _embedding_ _as_ _shown_ _on_ _the_ _right_ _of_ _Figure_ _22._


49


Figure 23: (a) Y: Three-dimensional one-loop associahedron. (b) _X_ in _Y_ : Three
dimensional one-loop _U_ -polytope.


_Similarly,_ _for_ _n_ = 3 _,_ _we_ _intersect_ _the_ _subspace_


_y_ 1 + ˜ _y_ 1 _−_ _x_ 2 _,_ 2 = _c_ 2 _,_ _y_ 2 + ˜ _y_ 2 _−_ _x_ 3 _,_ 3 = _c_ 3 _,_ _y_ 3 + ˜ _y_ 3 _−_ _x_ 1 _,_ 1 = _c_ 1 _,_

_x_ 1 _,_ 1 + _x_ 2 _,_ 2 + _x_ 2 _,_ 1 _−_ _y_ 1 _−_ _y_ ˜3 = _c_ 2 _,_ 1 _,_ _x_ 2 _,_ 2 + _x_ 3 _,_ 3 + _x_ 3 _,_ 2 _−_ _y_ 2 _−_ _y_ ˜1 = _c_ 3 _,_ 2
_x_ 3 _,_ 3 + _x_ 1 _,_ 1 + _x_ 1 _,_ 3 _−_ _y_ 3 _−_ _y_ ˜2 = _c_ 1 _,_ 3 _,_ _x_ 1 _,_ 3 + _x_ 2 _,_ 1 _−_ _x_ 1 _,_ 1 = _c_ 2 _,_ 3 _,_

_x_ 2 _,_ 1 + _x_ 3 _,_ 2 _−_ _x_ 2 _,_ 2 = _c_ 3 _,_ 1 _,_ _x_ 3 _,_ 2 + _x_ 1 _,_ 3 _−_ _x_ 3 _,_ 3 = _c_ 1 _,_ 2 _,_ (21)


_with_ _the_ _inequalities_


_xi,i_ _≥_ 0 _,_ _x_ 2 _,_ 1 _≥_ 0 _,_ _x_ 3 _,_ 2 _≥_ 0 _,_ _x_ 1 _,_ 3 _≥_ 0 _,_

_yi_ _≥_ _ϵi,_ _yi_ + _yj_ _≥_ _ϵi_ + _ϵj_ + _ϵ,_ _y_ 1 + _y_ 2 + _y_ 3 _≥_ _ϵ_ 1 + _ϵ_ 2 + _ϵ_ 3 + 2 _ϵ_ (22)


_for_ _ϵ_ 1 _, ϵ_ 2 _, ϵ_ 3 _, ϵ >_ 0 _,_ _and_ _analogous_ _inequalities_ _for_ _the_ _y_ ˜ _s._
_With_ _ϵi_ = ˜ _ϵi_ = 0 _and_ _ϵ_ = ˜ _ϵ_ = 1 _,_ _we_ _produce_ _the_ _correct_ _embedding_ _seen_ _in_ _Figure_ _23._

### **References**


[AA23] Marcelo Aguiar and Federico Ardila. _Hopf_ _monoids_ _and_ _generalized_
_permutahedra_, volume 289. American Mathematical Society, 2023.


[ACEP20] Federico Ardila, Federico Castillo, Christopher Eur, and Alexander
Postnikov. Coxeter submodular functions and deformations of Coxeter
permutahedra. _Advances_ _in_ _Mathematics_, 365:107039, 2020.


[AH] Nima Arkani-Hamed. All-Loop Scattering as a Counting Problem.
Amplitudes 2022 Talk.


50


[AHBHY18a] Nima Arkani-Hamed, Yuntao Bai, Song He, and Gongwang Yan.
Scattering Forms and the Positive Geometry of Kinematics, Color and
the Worldsheet. _JHEP_, 05:096, 2018.


[AHBHY18b] Nima Arkani-Hamed, Yuntao Bai, Song He, and Gongwang Yan.
Scattering forms and the positive geometry of kinematics, color and the
worldsheet. _Journal_ _of_ _High_ _Energy_ _Physics_, 2018(5):1–78, 2018.


[AHCD [+] 24] Nima Arkani-Hamed, Qu Cao, Jin Dong, Carolina Figueiredo, and Song
He. Hidden zeros for particle/string amplitudes and the unity of colored
scalars, pions and gluons. _JHEP_, 10:231, 2024.


[AHFS [+] 25] N. Arkani-Hamed, H. Frost, G. Salvatori, P-G. Plamondon, and
H. Thomas. All loop scattering as a counting problem. _JHEP_, 08:194,
2025.


[AHFV25] Nima Arkani-Hamed, Carolina Figueiredo, and Francisco Vaz˜ao.
Cosmohedra. _JHEP_, 11:029, 2025.


[AHHM22] Nima Arkani-Hamed, Aaron Hillman, and Sebastian Mizera. Feynman
polytopes and the tropical geometry of UV and IR divergences. _Phys._
_Rev._ _D_, 105(12):125013, 2022.


[AHHST22] Nima Arkani-Hamed, Song He, Giulio Salvatori, and Hugh Thomas.
Causal diamonds, cluster polytopes and scattering amplitudes. _JHEP_,
11:049, 2022.


[ARW06] Federico Ardila, Victor Reiner, and Lauren Williams. Bergman complexes,
coxeter arrangements, and graph associahedra. _S´eminaire Lotharingien de_
_Combinatoire_, 54:B54Aj, 2006.


[BCL [+] 22] Luciana Basualdo Bonatto, Safia Chettih, Abigail Linton, Sophie Raynor,
Marcy Robertson, and Nathalie Wahl. An infinity operad of normalized
cacti. _Topology_ _and_ _its_ _Applications_, 316:108107, 2022.


[BR25] Jeffrey V. Backus and Laurentiu Rodina. Emergence of Unitarity and
Locality from Hidden Zeros at One-Loop Order. _Phys._ _Rev._ _Lett._,
135(13):131601, 2025.


[BS13] Alicia Boole Stott. _Geometrical_ _deduction_ _of_ _semiregular_ _from_ _regular_
_polytopes_ _and_ _space_ _fillings_, volume 11. J. M¨uller, 1913.


[CD06] Michael Carr and Satyan L Devadoss. Coxeter complexes and
graph-associahedra. _Topology_ _and_ _its_ _Applications_, 153(12):2155–2168,
2006.


[CL22] Federico Castillo and Fu Liu. Deformation cones of nested braid fans.
_International_ _Mathematics_ _Research_ _Notices_, 2022(3):1973–2026, 2022.


51


[CL23] Federico Castillo and Fu Liu. The permuto-associahedron revisited.
_European_ _Journal_ _of_ _Combinatorics_, 110:103706, 2023.


[CLS24] David A Cox, John B Little, and Henry K Schenck. _Toric_ _varieties_,
volume 124. American Mathematical Society, 2024.


[CSZ15] Cesar Ceballos, Francisco Santos, and G¨unter M Ziegler. Many
non-equivalent realizations of the associahedron. _Combinatorica_,
35(5):513–551, 2015.


[Dev09] Satyan L Devadoss. A realization of graph associahedra. _Discrete_
_Mathematics_, 309(1):271–276, 2009.


[Ear24] Nick Early. Generalized permutohedra in the kinematic space. _Journal_ _of_
_High_ _Energy_ _Physics_, 2024(6):1–24, 2024.


[Edm70] Jack Edmonds. Submodular functions, matroids, and certain polyhedra.
In _Combinatorial_ _Structures_ _and_ _their_ _Applications_ _(Proc._ _Calgary_
_Internat._ _Conf.,_ _Calgary,_ _Alta.,_ _1969)_, pages 69–87. Springer, 1970.


[FV26] Carolina Figueiredo and Francisco Vaz˜ao. Correlator polytopes. _Phys._
_Rev._ _D_, 113(2):025005, 2026.


[Gai15] Giovanni Gaiffi. Permutonestohedra. _Journal of Algebraic Combinatorics_,
41(1):125–155, 2015.


[Kap93] Mikhail M Kapranov. The permutoassociahedron, mac lane’s coherence
theorem and asymptotic zones for the kz equation. _Journal_ _of_ _Pure_ _and_
_Applied_ _Algebra_, 85(2):119–142, 1993.


[KI14] Vaclav Kotesovic and OEIS Foundation Inc. Entry E177384, The on-line
encyclopedia of integer sequences, 2014.


[Knu97] Donald E Knuth. _The_ _Art_ _of_ _Computer_ _Programming:_ _Fundamental_
_Algorithms,_ _Volume_ _1_ . Addison-Wesley Professional, 1997.


[LA22] Guillaume Laplante-Anfossi. The diagonal of the operahedra. _Advances_
_in_ _Mathematics_, 405:108494, 2022.


[Lod04] Jean-Louis Loday. Realization of the stasheff polytope. _Archiv_ _der_
_Mathematik_, 83(3):267–278, 2004.


[Mel21] Stephen Melczer. _An_ _Invitation_ _to_ _Analytic_ _Combinatorics_ . Springer,
2021.


[MSS02] Martin Markl, Steve Shnider, and Jim Stasheff. Operads in algebra,
topology and physics. _Mathematical_ _surveys_ _and_ _monographs_, 96, 2002.


52


[Pos09] Alexander Postnikov. Permutohedra, associahedra, and beyond.
_International_ _Mathematics_ _Research_ _Notices_, 2009(6):1026–1106, 2009.


[PPP23] Arnau Padrol, Vincent Pilaud, and Germain Poullot. Deformation
cones of graph associahedra and nestohedra. _European_ _Journal_ _of_
_Combinatorics_, 107:103594, 2023.


[Sch13] Pieter Hendrik Schoute. _Analytical_ _treatment_ _of_ _the_ _polytopes_ _regularly_
_derived_ _from_ _the_ _regular_ _polytopes_, volume 11. J. M¨uller, 1913.


[Sta63] James Dillon Stasheff. Homotopy associativity of h-spaces. ii.
_Transactions_ _of_ _the_ _American_ _Mathematical_ _Society_, 108(2):293–312,
1963.


[Sta97] Richard P Stanley. Hipparchus, plutarch, schr¨oder, and hough. _The_
_American_ _Mathematical_ _Monthly_, 104(4):344–350, 1997.


[Sta99] Richard P Stanley. Enumerative combinatorics volume 2. _Cambridge_
_studies_ _in_ _advanced_ _mathematics_, 1999.


[Tam54] Dov Tamari. Mono¨ıdes pr´eordonn´es et chaˆınes de malcev. _Bulletin_ _de_ _la_
_Soci´et´e_ _math´ematique_ _de_ _France_, 82:53–96, 1954.


53


