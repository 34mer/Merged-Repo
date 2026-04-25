MPP-2024-265

# Cosmohedra

#### Nima Arkani-Hamed [1], Carolina Figueiredo [2], and Francisco Vaz˜ao [3]


1
School of Natural Sciences, Institute for Advanced Study, Princeton, NJ 08540
2Department of Physics, Princeton University, Princeton, NJ 08540
3Max-Planck-Institut f¨ur Physik, Werner-Heisenberg-Institut, Boltzmannstr, 8, 85748 Garching,
Germany

#### December 31, 2024


**Abstract**


It has been a long-standing challenge to find a geometric object underlying the cosmological wavefunction for Tr( _ϕ_ [3] ) theory, generalizing associahedra and surfacehedra for scattering
amplitudes. In this note, we describe a new class of polytopes – “cosmohedra” – that provide
a natural solution to this problem. The faces of associahedra capture the combinatorics of
non-overlapping chords of the momentum polygon, reflecting all partial factorizations of amplitudes. Cosmohedra are far richer  - instead of non-overlapping chords, their faces capture
the “russian doll” structure of non-overlapping subpolygons that determine the wavefunction. We show that cosmohedra are intimately related to associahedra, obtained by “blowing
up” faces of the associahedron in a simple way. We give a full combinatorial description of
cosmohedron faces and their factorization properties, and provide an explicit realization in
terms of facet inequalities that further “shave” the facet inequalities of the associahedron.
We also discuss a novel way for computing the wavefunction from cosmohedron geometry
that extends the usual connection with polytope canonical forms. We illustrate cosmohedra with examples at tree-level and one loop; the close connection to surfacehedra suggests
the generalization to all loop orders. Moving beyond the wavefunction, we briefly describe
“cosmological correlahedra” for full correlators, which are one higher-dimensional polytopes,
interpolating between associahedra and cosmohedra on opposite facets in an extra direction
associated with the total energy. We speculate on how the existence of cosmohedra might
suggest a “stringy” formulation for the cosmological wavefunction/correlators, generalizing
the way in which the Minkowski sum decomposition of associahedra naturally extend particle
to string amplitudes.


1


### **Contents**

**1** **Amplitudes/Wavefunction,** **Associahedra/Cosmohedra** **2**


**2** **Russian** **dolls,** **subpolygons** **and** **flat** **space** Ψ **4**


**3** **Graph** **associahedra** **9**


**4** **Combinatorial** **cosmohedra** **12**


**5** **“Cosmologizing”** **the** **Feynman** **fan** **16**


**6** **Cosmic** **realizations** **19**


**7** **Permuto-cosmohedra** **22**


**8** **Wavefunction** **from** **geometry** **23**


**9** **Loop** **cosmohedra** **25**


**10** **Cosmological** **correlahedra** **32**


**11** **Outlook** **36**


**A** **Lightning** **review** **of** **the** **perturbative** **expansion** **of** Ψ **38**


**B** **Lightning** **review** **of** **the** **ABHY** **associahedron** **42**


**C** **Graph** **associahedra** **from** **cosmohedra** **44**

### **1 Amplitudes/Wavefunction, Associahedra/Cosmohedra**


Over the last two decades, many remarkable combinatorial structures underlying flat-space scattering amplitudes have been discovered. At first such structures were identified for simpler toy
model theories such as _N_ = 4 super Yang-Mills [1–4], as well as for a simple theory of colored
scalars [5–8] – Tr( _ϕ_ [3] ) theory – but, over the past few years, these have been extended to real world
theories [9–12].
There are many reasons to expect similar structures to underlie the cosmological wavefunction
of the universe, not least because it has long been appreciated that flat-space scattering amplitudes
are contained on the “total energy singularity” of the cosmological wavefunction [13–17]. Much
of the effort in looking for such structures has focused on a simple toy model of conformally
coupled scalars with general polynomial interactions in a general FRW cosmology [18–42]. The
cosmological wavefunction in these examples is simply related to the flat-space wavefunction. In
turn, for any single graph _G_, the flat-space wavefunction was recognized as being determined by
the canonical form of a “cosmological polytope” determined by _G_, in parallel with the way in
which amplitudes are determined by positive geometries [18].
However, all the magic in amplitudes is seen not one graph at a time, but in the sum over all
graphs. This is true not only in gauge theories and gravity, but even in the simplest toy model
of colored scalars, the Tr( _ϕ_ [3] ) theory. At tree-level, the amplitudes for this theory were associated


2


Figure 1: Associahedron (left) and cosmohedron (right) at 6-points


with the canonical form of a famous polytope - the associahedron. More recently, this theory
has been given a new formulation at all loop orders, using ideas related to counting problems
attached to curves on surfaces [6, 7]; one aspect of this story is an extension of associahedra at
tree-level to “surfacehedra” at all loop orders. And very surprisingly, this seeming “toy model”
secretly contains realistic theories – the amplitudes for pions and gluons can be obtained from the
“stringy” Tr( _ϕ_ [3] ) amplitudes by a simple kinematic shift [9–11,43,44].
It is thus obviously important to look for a combinatorial/geometric structure for cosmology,
not one graph at a time, but naturally combining all diagrams together into a single object. Indeed,
the discovery of the associahedron for Tr( _ϕ_ [3] ) theory, already at tree-level, suggested the search for
the “cosmohedron” that would compute the flat-space wavefunction for Tr( _ϕ_ [3] ) theory. The most
obvious thought is to try and “glue together” cosmological polytopes for the different diagrams
into the cosmohedron, but efforts in this direction were not successful. And while there have been
many other significant developments exposing the mathematical structures underlying cosmological observables - from generalizations of the cosmological polytope for computing correlators to
the discovery of “kinematic flow” differential equations directly describing FRW correlators [21,22]

- the basic question of “what object combines all diagrams together in cosmology?” has remained
open for many years.
In this note, we present a solution to this problem. We will describe “cosmohedra”, which are
polytopes that entirely capture the combinatorial structure of the wavefunction of Tr( _ϕ_ [3] ) theory,
in exact parallel with the associahedron for amplitudes. Indeed, as we will see, cosmohedra are
very closely connected to associahedra, and can be obtained from associahedra by “blowing up”
the faces on associahedra in a natural way. We will work for simplicity mostly at tree-level, but
will give some explicit examples at one-loop, but the way in which cosmohedra are connected to
the amplitude geometries obviously extends to all loop orders, and we will explicitly describe some
examples at one-loop.
We also briefly describe “cosmological correlahedra”, which capture all contributions not just
for the wavefunction, but for the full correlator. This object is a one-higher dimensional polytope
sandwiched between an associahedron on a “top” facet and a cosmohedron on the “bottom” facet.
While cosmohedra are very rich objects, their description, both combinatorially as well as how
they are cut out by inequalities, are strikingly simple. At tree-level, for the _n_ -pt wavefunction
we consider a _n_ -gon. The faces of the cosmohedron are associated with collections, _P_, of non

3


overlapping sub-polygons, which satisfy the rule that if any subpolygon _p_ in _P_ contains another
subpolygon of _P_ inside it, then all of _p_ must be covered by subpolygons in _P_ . The cosmohedron
captures all such collections in its face structure, where _P_ _[′]_ is a face of _P_ if _P_ _⊂_ _P_ _[′]_, that is if _P_ _[′]_

is a refinement of _P_ . This mirrors the combinatorial definition of the associahedron, where faces
are labeled by collections of non-overlapping chords, _C_, instead of non-overlapping sub-polygons.
The inequality definition of the cosmohedron can also be given in one line. We begin with the
inequalities cutting out the associahedron: for every chord _I_ _≡_ ( _i, j_ ) of the _n_ -gon, we associate a
variable _XI_ . The _X_ ’s are constrained by the ABHY conditions [5]; there is a realization of the associahedron for choice of triangulation, but one especially simple set is determined by _Xi,j_ + _Xi_ +1 _,j_ +1 _−_
_Xi,j_ +1 _−_ _Xi_ +1 _,j_ = _ci,j_, where _ci,j_ ’s are the set _{c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, · · ·_ _, c_ 1 _,n−_ 1 _, c_ 2 _,_ 4 _, c_ 2 _,_ 5 _, · · ·_ _, c_ 2 _,n−_ 1 _, · · · c_ 3 _,_ 5 _,_

_· · ·_ _, cn−_ 3 _,n−_ 1 _}_ . Under this constraint, the associahedron is cut out by the equations _XI_ _≥_ 0
for all _I_ . The cosmohedra are then obtained by further “shaving” the associahedron, by imposing
an additional set of inequalities. There is a facet of the cosmohedron for every partial triangulation, or what is the same, every collection of non-overlapping chords, _C_ . The inequalities defining
the cosmohedron are then simply [�] _I⊂C_ _[X][I]_ _[≥]_ [�] _[δ][P]_ [,] [where] [the] [sum] [is] [over] [all] [the] [subpolygons]

defined by _C_, and _δP_ are positive constants that are taken to be much smaller than the _ci,j_ ’s. The
_δP_ must satisfy the crucial inequalities _δP_ + _δP ′_ _≤_ _δP_ _∪P ′_ + _δP_ _∩P ′_, (with _δ_ full = 0 for the full polygon
is defined to be zero). This is all that is needed to define and study cosmohedra at tree-level.
Everything else that follows in this note consists only of motivation, exposition and examples.
Our aim in this note is to define and explore the most basic properties of cosmohedra. We
have tried to make the presentation largely self-contained, without assuming previous knowledge
of the physics of the cosmological wavefunction or the combinatorial geometry of amplitudes.
We give a lightning introduction to these two topics in appendices A and B. Cosmohedra also
feature a new geometry associated to a single diagram –“graph associahedra” - different from
the cosmological polytopes of [18], whose properties and relation with cosmological polytopes we
describe in greater detail in appendix C. As we will see, there are many physical and mathematical
novelties associated with cosmohedra and cosmological correlahedra, and a great deal remains to
be understood about these objects both physically and mathematically. We believe the existence
of these remarkable objects is a clear indication of a new world of ideas extending combinatorial
geometries to cosmology, and we hope this note will help stimulate further developments.

### 2 Russian dolls, subpolygons and flat space Ψ


In this note, we will be studying the wavefunction for a theory of colored scalars interacting via a
cubic interaction with the following action:




   _S_ [ _ϕ_ ] = _d_ _[d]_ _xdη_ [1]



Tr _ϕ_ [3] _,_ (1)
3




[1]

2 [Tr (] _[∂ϕ]_ [)][2] _[ −]_ _[λ]_ [3] 3 [(] _[η]_ [)]



where the background spacetime is flat, but we allow for general time-dependent couplings _λ_ 3( _η_ ).
In particular, for _λ_ 3( _η_ ) = _λ_ 3 _a_ ( _η_ ) _[−]_ [(] _[d][−]_ [1)] _[/]_ [2+2] we can do a Weyl rescaling to obtain the action of
conformally coupled scalars in an FRW cosmology with scale factor _a_ ( _η_ ) [18, 27, 45]. In the rest
of the note, we will focus on the flatspace case _λ_ 3( _η_ ) = _const._ since, as explained in 2.1 and in
greater detail in appendix A, starting with the flatspace answer we can obtain the cosmological
one via a simple integral transform.
After performing the path integral that defines Ψ, we can write it as follows:


4


Figure 2: (Left) Triangulation of the _[⃗]_ _k_ 6-gon and the respective dual cubic diagram. (Right)
Russian doll on the momentum 6-gon and respective tubing. Associated with each Russian doll,
_R_, a factor of 1 over the product of the perimeters of the subpolygons entering in _R_ . Any russian
doll always contains the full polygon whose perimeter is the sum of the _|_ _[⃗]_ _ki|_ which we call the total
energy _Et_ .




 - [�]
_i_ _[⃗k][i]_



_,_ (2)



Ψ = exp



��


_n≥_ 2



_n_


 




_d_ _[d]_ _ki_ Ψ _n_ [ _[⃗]_ _ki_ ] _δ_ _[d]_ [ ��]

_i_ =1



where Ψ _n_ [ _[⃗]_ _ki_ ] are called the _wavefunction_ _coefficients_ that capture the contributions to the path
integral with _n_ field insertions at the boundary _η_ = 0. The Ψ _n_ [ _[⃗]_ _ki_ ]’s admit a perturbative expansion
in _λ_ 3 that we review in appendix A. As it was first shown in [18], for a particular ordering of the
external states, stripping out the color-factor Tr( _ϕ_ 1 _ϕ_ 2 _· · · ϕn_ ), we can write Ψ _n_ [ _[⃗]_ _ki_ ] as a sum over
all the diagrams compatible with the ordering. From each diagram, we consider all the possible
collections of compatible subgraphs - _tubings_ (see figure 2 middle bottom, for an example of a
tubing of 6-point tree diagram)– and from each tubing get a factor of the product of one over the
energies entering each subgraph. So we can write





 

subgraph, _s∈t_



��




  Ψ _n_ =


diagrams, _D_





 

tubings _t_ of _D_



1
_Eb_



_._ (3)



To compare the wavefunction with the amplitude, it is useful to recast the tubing picture in terms
of subpolygons living inside the spatial-momentum polygon. Since we have spatial momentum
conservation, [�] _i_ _[n]_ =1 _[⃗k][i]_ [=] [0,] [we] [can] [draw] [the] [momentum] _[⃗k][i]_ [tip] [to] [toe,] [according] [to] [the] [ordering]
in study, and from it, we obtain a closed polygon - the spatial momentum _n_ -gon. Now we can
specify a tree-level diagram by looking at a given _triangulation_ of the _n_ -gon – _i.e._ a way of dividing
the _n_ -gon into triangles using internal chords of the _n_ -gon (see figure 2, left, for an example for
_n_ = 6).
So in this language, a graph is associated with a triangulation of the momentum _n_ -gon, which
determines a set of triangles, and quite nicely, a tubing is then a maximal collection of nonoverlapping subpolygons [1] - which we call a _Russian_ _doll_ - containing the set of triangles deter

1where non-overlapping means that their edges don’t cross, but they can be, however, fully contained inside
each other.


5


mined by the triangulation (see figure 2 right). Note that this means that for a given graph, any
tubing of the graph will always contain the tubes enclosing the vertices – the triangles – as well as
a big tube which encloses the full graph - the full momentum polygon. For each subgraph in the
tubing, we get a factor of the sum of the energies, _Ei_ = _|_ _[⃗]_ _ki|_, entering the subgraph. At the level of
the momentum _n_ -gon/Russian doll this corresponds precisely to the perimeter of the subpolygon
associated with the corresponding subgraph - _Pi,...,j_ is the perimeter of subpolygon with vertices
_{i, . . ., j}_, (figure 2,right).
Thus, we have our most basic expression for the wavefunction, given as a sum over maximal
sets **P** of non-overlapping sub-polygons:




 Ψ =


**P**






_P_ _⊂_ **P**



1
_._ (4)
_PP_



Since every **P** includes the triangles of a triangulation, we can also write this as a sum over all
diagrams/triangulations _T_, together with a sum over all the “russian dolls” associated with the
diagram _RT_, as




 Ψ =


_T_






_RT_






_P_ _⊂RT_



1
_._ (5)
_PP_



This formulation makes manifest the extra complexity of the wavefunction as compared with the
amplitude (which we get back to in section 2.2) - while for the amplitude we get a simple sum
over cubic diagrams/triangulations, and we get a single factor for each, in the wavefunction we
have an extra sum over all the russian dolls compatible with the triangulation. So we have that,
manifestly, while Tr( _ϕ_ [3] ) amplitudes, _An_, are about maximal collections of _non-overlapping chords_,
that define full triangulations of the _n_ -gon, the wavefunction, Ψ _n_ is about maximal collections of
_non-overlapping_ _subpolygons_, that define full russian dolls on the _n_ -gon.
Nonetheless, when we go on the residue of the total energy, _Et_ = 0, the wavefunction highly
simplifies and gives us precisely the flatspace amplitude:


Res _n_ = _An._ (6)
_Et_ =0 [Ψ][tree]


So far we have given more emphasis to the tree-level case, but all of the above discussion extends to
all loops. Already at tree-level, we can replace the momentum _n_ -gon by a disk with _n_ marked points
on the boundary (following the appropriate color-ordering), and where each boundary component
is assigned a momentum _[⃗]_ _ki_ . The subpolygons were then defined by collections of boundary edges
and internal chords, whose perimeter was just the sum of the length of each of these. In the
disk case, the subpolygons correspond to subsurfaces bounded by boundary components as well
as internal curves going from marked points to marked points. We can determine the perimeter of
the subsurfaces as the sum of the absolute values of the curves/boundary components bounding
the subsurface, where the momentum associated to a given curve is read by _homology_ . But as with
the story of “surface kinematics” [46] for amplitudes on surfaces, it is fruitful to think of more
general kinematic variables associated with the curve on the surface (in general, up to _homotopy_ ),
instead of relating it to a set of momenta. In the context of the wavefunction at tree-level, this
means that we can think of the perimeters of each subpolygon as independent variables.
At _n_ -points one-loop, the surface we get is instead a punctured disk with _n_ -marked points.
In this case, to provide a basis of homology on top of assigning momentum to the boundary
components of the disk, we also have to give momentum to one of the curves starting in a boundary
marked point and ending on the puncture – this corresponds to the spatial _loop_ _momentum_ . Once


6


we have done this, we can again read off the momentum of any curve, _[⃗]_ _kC_, on the surface by
homology. Finally, just like at tree-level, we can list all possible cubic graphs by considering all
the possible triangulations of the punctured disk, and the wavefunction is then given as a sum over
all russian dolls - which are now maximal collections of non-overlapping subsurfaces - where to
each subsurface we get a factor of its perimeters - the sum of _|_ _[⃗]_ _kC|_ for each curve _C_ bounding the
subsurface. The same picture holds at all orders in the topological expansion, where for each order
we have a different surface. And again, we will consider more general kinematic variables for the
wavefunction as being labelled by subsurfaces of the surface bounded by curves up to homotopy,
which can be specialized to the perimeters when written in terms of momenta determined by
homology. Most of this note will focus on the tree-level wavefunction, but in section 9 we explain
how our results extend to loop-level.
Finally, there is an obvious recursive expression for the wavefunction [21], trivially generalizing
the recursive expression as a sum over cuts for single graphs given in [18]. We can phrase this at
any loop order in terms of the perimeters _PS_ for any surface _S_, as



Ψ _S_ = _P_ [1] _S_





Ψ _S/C_ (7)

curves _C_



where we sum over all curves _C_, and _S/C_ is the simpler surface obtained by cutting _S_ along _C_ .
Before proceeding, let’s review how we can connect this formulation of the flat-space wavefunction to the wavefunction of more general FRW cosmologies described in the beginning of this
section.

#### 2.1 Flat Space → Cosmological Wavefunction


As explained in appendix A, for the case where the cubic coupling has some general timedependence _λ_ 3( _η_ ), it is useful to analyze each Fourier mode, _λ_ 3( _ε_ ), separately. In which case,
for each cubic vertex, _λ_ 3( _ε_ ) produces a shift in the energies entering the vertex by _ε_ . So, for a
general graph, we have that the energies associated to each cubic vertex are shifted by the energies
_εi_ associated to the couplings. This can be rephrased in terms of the perimeters of subpolygons as
follows: the perimeters associated to the triangles, _ti_ entering the triangulation are shifted by the
respective energy, _Pti_ _→Pti_ + _εi_, and for a generic subpolygon, _P_, we have _PP_ _→PP_ + [�] _ti⊂P_ _[ε][i]_ [.]

Therefore, having obtained the wavefunction for a single graph, _G_, it is easy to obtain the
corresponding cosmological wavefunction, in the following way












    - _∞_
Ψ [Cosm] _G_ =

_−∞_





 


_dεi λ_ 3( _εi_ )

triangles _ti_





  _PP_ _→PP_ + _εi_


_ti⊂P_



Ψ [Flat] _G_



_,_ (8)



where we associate a shift _εi_ with all the ( _n_ _−_ 2) triangles _ti_ in the triangulation, and shift
every perimeter _PP_ of a sub-polygon _P_ by the sum of the _εi_ for all the triangles _ti_ contained
in _P_, as described earlier. The precise form of _λ_ 3( _ε_ ) depends on the time-dependence that we
are interested in studying, but already here we see that the combinatorics associated to the flatspace wavefunction coefficients port literally to those of the cosmological wavefunction, with the
difference that for the latter we need to further perform this shift and integral.
We can now describe the same procedure for the full wavefunction, given by the sum over all
graphs. The obvious challenge is that the shifts _εi_ seem to be different from graph-to-graph, and
this doesn’t give us a universal ( _n −_ 2) dimensional “ _ε_ integrand” we simply integrate to get the
cosmological wavefunction.


7


Fortunately, there is a beautiful solution to this problem, which also arose in labeling general
interactions for colored Lagrangians in [8]. Let us choose a base triangulation that defines our
surface, and label the triangles in this base triangulation as ( _t_ 1 _, · · ·_ _, tN_ ). Then, as explained in [8],
_every_ _other_ _triangle_ on the surface is canonically associated with _one_ of these _ti_ . In a similar way,
any subpolygon _P_ is associated with a collection of triangles, _Ti_, that triangulate it, that can
ultimately map it to a collection of triangles in the base triangulation. Therefore, having made a
choice of base triangulation, we can unambiguously associate a _εi_ shift to every subpolygon, and
we find




  Ψ [Flat]



_λi_

_Ti⊂P_








    - _∞_
Ψ [Cosm] =

_−∞_





 


_dεiλ_ 3( _εi_ )

triangles _ti_







_PP_ _→PP_ + 


(9)



where here we can choose any triangulation of the subpolygon _P_ we like, as the sum [�] _Ti⊂P_ _[λ][i]_ [will]

be the same for all of them. This map will be explained in more detail in [47].

#### **2.2 Complexity of the wavefunction vs. amplitude**


Finally, it is interesting to compare and contrast the “size” of the amplitude compared with
the wavefunction, as this is a qualitative feature of the objects that is very clearly reflected in
the geometries we will be discussing. The number of diagrams for amplitudes _An_ are famously
given by the Catalan numbers, and satisfy an obvious recursion. The number of terms for the
wavefunction Ψ _n_ satisfy a very similar recursion relation, straightforwardly derived from the sum
over cuts recursive formula. The recursion relations for _An_ and Ψ _n_ are very similar,



_n−_ 1


( _k −_ 1)Ψ _k_ Ψ _n_ +2 _−k._ (10)

_k_ =3



_An_ =



_n−_ 1


_AkAn_ +2 _−k,_ Ψ _n_ =

_k_ =3



The extra factor of ( _k −_ 1) for the Ψ _n_ recursion makes a dramatic difference in the asymptotics.
While _An_ grows exponentially at large _n_ as _An_ _→_ 4 _[n]_, Ψ _n_ _→_ _n_ ! grows factorially. Meanwhile, the
number of poles in the amplitude is given by the total number of internal chords for the amplitude,
which scales as _n_ [2], while the number of poles of the wavefunction is given by the total number
of subpolygons, which scales like 2 _[n]_ . Thus, the associahedron is an object with polynomially
many facets, and exponentially many vertices, while the object encoding the combinatorics for the
wavefunction – the cosmohedron – will be an object with exponentially many facets and factorially
many vertices.
More precisely, we have the asymptotics for the number of vertices


4 _[n]_
#Vertices(Assoc) _n_ _→_ #Vertices(Cosmo) _n_ _→_ _cn_ [4] _n_ ! (11)

_n_ [3] _[/]_ [2] ~~_[√]_~~ _π_ _[,]_


where _c_ = 0 _._ 05 _· · ·_ is a constant. Meanwhile, the number of facets of the associahedron is _n_ ( _n −_
3) _/_ 2, while as we will see the total number of facets of the cosmohedron is equal to the total
number of all (not just complete) triangulations of the _n_ -gon, and we have



_c_ _√_

#Facets(Assoc) _n_ _→_ _[n]_ [2] #Facets(Cosmo) _n_ _→_

2 _[,]_ _n_ [3] _[/]_ [2] [(3 +]


where _c_ = 0 _._ 04 _· · ·_ is a constant.


8



8) _[n]_ (12)


### **3 Graph associahedra**

Before proceeding to the full wavefunction, we are going to start by looking at the contributions
from each graph separately, and understand how to encode the combinatorics of the different russian dolls we obtain. A geometric description of the contribution of each graph for the wavefunction
was first proposed through the so-called “cosmological polytopes” in [18]. In this section, we will
discuss a different geometry that captures the combinatorics of a given graph, that naturally arises
when we think of the kinematic variables as naturally associated with perimeters of subpolygons
(and assume these are independent). In appendix C, we explain how graph associahedra are
related to cosmological polytopes.
For any triangulation _T_, we start by producing an associated dual graph _GT_, placing a node in
the middle of the face of every triangle, and connecting nodes if the corresponding triangles share
an edge. The russian dolls associated with this graph are “tubings” of the graph. As highlighted
earlier, each russian doll term will include the total energy/the perimeter of the full _n_ -gon - the
biggest “tube” containing the entire graph - as well as the perimeters of each triangle in the
triangulation - the small tubes encircling each node in the graph. It is thus not necessary to keep
track of these tubes, as they are in common to all tubings. Each term in the russian doll sum is
then associated with a maximal collection of non-overlapping tubes, where we do not include the
total tube or the small tubes encircling each node.
This leads us to define the “graph associahedron”, _AG_, associated with any graph to be a
polytope whose face structure reflects these tubings: the facets of the _AG_ are individual tubes,
the vertices are complete tubings, and faces of general dimension are partial tubings _τ_ with the
obvious notion of inclusion: if _τ_ _[′]_ _⊂_ _τ_, the faces for _τ_ _[′]_ belongs to that of _τ_ . When the graph
comes from the triangulation of a _n_ -gon, the graph associahedron _AG_ is ( _n −_ 4) _−_ dimensional. It
is non-trivial that such a polytope exists, and we will shortly give an explicit description of it in
the course of defining the cosmohedron, but we can illustrate with some simple examples.
We note that our definition of the graph associahedron is different from the one standard in
the mathematical literature [48,49], which also captures the combinatorics of tubings but with a
different set of rules than ours. We nonetheless give them the same name because “our” graph
associahedron for a graph _G_ turns out to be exactly the same as the usual graph associahedron
for a different graph _G_ [˜] . Beginning with our triangulation, instead of putting nodes in the interior
of each triangle, nodes are placed in the middle of each internal edge of a triangle, and two nodes
are connected if the corresponding edges meet at a vertex. The “standard” graph associahedron
for _G_ [˜] turns out to be the same as “our” graph associahedron for _G_ .
Before proceeding to examples, we would like to point out that graph associahedra have a
simple, beautiful factorization property on their facets. Consider any single tube T of a graph _G_,
then we have
Facet _T_ ( _AG_ ) = _AT_ _× AG/T_ _,_ (13)


where _G/T_ is the graph obtained by shrinking all of _T_ to a single point.

#### **3.1 5-points example**


At 5-points, let’s start by fixing the triangulation to be that containing chords _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ (all
the remaining triangulations are simply given by cyclic rotations of this one). In this case, we can
factor out from all the russian dolls a factor of 1 _/_ ( _EtP_ 1 _,_ 2 _,_ 3 _P_ 1 _,_ 3 _,_ 4 _P_ 1 _,_ 4 _,_ 5), and after doing this we get


9


Figure 3: 5(left) and 6(right) point graph associahedron. When drawing the graph we omit the
external legs to make manifest that for the purpose of the combinatorics of tubings what matters
is the topology of the graph with just the internal edges.


that the contribution to Ψ [(5)] coming from this graph is simply:




_,_



1
Ψ [(5)] _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ [=]
_Et P_ 1 _,_ 2 _,_ 3 _P_ 1 _,_ 3 _,_ 4 _P_ 1 _,_ 4 _,_ 5




- 1 1
+
_P_ 1 _,_ 2 _,_ 3 _,_ 4 _P_ 1 _,_ 3 _,_ 4 _,_ 5



which means we only have two terms. Therefore, we can associate each term with the boundary
of a one-dimensional line-segment (see figure 3, left). Each vertex of the line segment is then
associated with a tube which encloses either the left and middle sites, or the right and middle
sites.

#### **3.2 6-points examples**


At 6-points, there are now different types of triangulation to consider. Let’s start with the simplest
analog of what we had at 5-points, _i.e._ the triangulation containing chords _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ .
In this case, we have 5 different terms which we can write as:



1
Ψ [(6)] _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ [=]
_Et P_ 1 _,_ 2 _,_ 3 _P_ 1 _,_ 3 _,_ 4 _P_ 1 _,_ 4 _,_ 5 _P_ 1 _,_ 5 _,_ 6




- 1 1
+
_P_ 1 _,_ 2 _,_ 3 _,_ 4 _P_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _P_ 1 _,_ 2 _,_ 3 _,_ 4 _P_ 1 _,_ 4 _,_ 5 _,_ 6



1 1 1
+ + +
_P_ 1 _,_ 4 _,_ 5 _,_ 6 _P_ 1 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _P_ 1 _,_ 3 _,_ 4 _,_ 5 _P_ 1 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _P_ 1 _,_ 3 _,_ 4 _,_ 5 _P_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5



(14)




so we see there are five different subpolygons entering inside the brackets - _P_ 1 _,_ 2 _,_ 3 _,_ 4 _, P_ 1 _,_ 3 _,_ 4 _,_ 5 _, P_ 1 _,_ 4 _,_ 5 _,_ 6
squares and _P_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _, P_ 1 _,_ 3 _,_ 4 _,_ 5 _,_ 6 pentagons – each of which can be associated to an edge of a pentagon,
such that each of the five vertices where two edges meet gives one of the terms inside brackets in
(14) (see figure 3, center).
So we have that the graph associahedron for Ψ [(6)] _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ [is a pentagon.] [Obviously, the same]
is true for all the six triangulations that are cyclic rotations of _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ . In addition,
it is easy to check that the same is true for the 6 triangulations obtained by cyclic rotations of
triangulations _{_ (1 _,_ 3) _,_ (3 _,_ 5) _,_ (1 _,_ 5) _}_ and _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (4 _,_ 6) _}_, _i.e._ that for all these triangulations
once we factor out _Et_ and the perimeters of the triangles in the triangulation, the rest of the


10


Figure 4: (Left) 7-point graph associahedra for triangulations from the cyclic classes
_{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (4 _,_ 6) _,_ (1 _,_ 6) _},_ _{_ (1 _,_ 3) _,_ (3 _,_ 5) _,_ (1 _,_ 5) _,_ (1 _,_ 6) _}_ . (Right) 7-point graph associahedra for
triangulations from the cyclic classes _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _,_ (1 _,_ 6) _},_ _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _,_ (5 _,_ 7) _},_
_{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (4 _,_ 7) _,_ (5 _,_ 7) _},_ _{_ (1 _,_ 3) _,_ (3 _,_ 7) _,_ (3 _,_ 6) _,_ (4 _,_ 6) _}_ .


wavefunction has precisely 5 terms that can be associated to vertices of a pentagon in exactly the
same way we did for the case of Ψ [(6)] _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ [.] [This] [is] [ultimately] [because] [the] [associated] [dual]
graph for these triangulations where we omit the external legs is also a chain (see figure 3, middle).
However, if instead we consider triangulation _{_ (1 _,_ 3) _,_ (3 _,_ 5) _,_ (1 _,_ 5) _}_ (or _{_ (2 _,_ 4) _,_ (4 _,_ 6) _,_ (2 _,_ 6) _}_ ) we
have that after we factor out the common part, we are still left with six terms:



1
Ψ [(6)] _{_ (1 _,_ 3) _,_ (3 _,_ 5) _,_ (1 _,_ 5) _}_ [=]
_Et P_ 1 _,_ 2 _,_ 3 _P_ 3 _,_ 4 _,_ 5 _P_ 1 _,_ 5 _,_ 6 _P_ 1 _,_ 3 _,_ 5




- 1 1 1
+ +
_P_ 1 _,_ 2 _,_ 3 _,_ 5 _P_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _P_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _P_ 1 _,_ 3 _,_ 4 _,_ 5 _P_ 1 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _P_ 1 _,_ 3 _,_ 4 _,_ 5



1 1 1
+ + +
_P_ 1 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _P_ 1 _,_ 3 _,_ 5 _,_ 6 _P_ 1 _,_ 3 _,_ 5 _,_ 6 _P_ 1 _,_ 2 _,_ 3 _,_ 5 _,_ 6 _P_ 1 _,_ 2 _,_ 3 _,_ 5 _,_ 6 _P_ 1 _,_ 2 _,_ 3 _,_ 5




_,_



(15)
therefore, for this type of triangulation the graph associahedron is given by a hexagon, where
each edge is associated with one of the six subpolygons appearing inside brackets and each vertex
associated to one of the terms in (15) (see figure 3, right). Indeed, in this case, the dual graph
(after removing the external legs) has a star topology which is different from that of the chain
that we found for the remaining triangulations of the hexagon.

#### **3.3 7-points examples**


At 7-points, there are a total of 42 triangulations. These amount to 6 different cyclic classes of
triangulations. From these 6 cyclic classes (represented by one of its triangulations), there are
four,


_{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _,_ (1 _,_ 6) _},_ _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _,_ (5 _,_ 7) _},_

_{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (4 _,_ 7) _,_ (5 _,_ 7) _},_ _{_ (1 _,_ 3) _,_ (3 _,_ 7) _,_ (3 _,_ 6) _,_ (4 _,_ 6) _},_


which produce the graph topology corresponding to a chain with four nodes, for which the graph
associahedron we can see in the right of figure 4. If we pick Ψ [(7)] _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _,_ (1 _,_ 6) _}_ [,] [the] [wavefunction]


11


coefficient for this graph will have 14 terms. Two of these terms are represented in figure 4 (two
highlighted vertices), after factorizing _Et_ and the perimeters of the triangles, they are:


1 1
_,_ _,_
_P_ 134567 _P_ 1345 _P_ 1567 _P_ 134567 _P_ 13456 _P_ 1345


where the first term corresponds to the tubing at the top of the figure, and the second term
corresponds to the tubing in the middle. The triangulations coming from cyclic rotations produce
the same graph associahedron, as well as all the other triangulations in the remaining 3 cyclic
classes. Since now the facets of the associahedron are two-dimensional, it is easier to illustrate
the factorization properties of the facets. For example, the facets associated to the pentagon
subpolygons (the green tubes in figure 4) are squares, since they are the product of a segment–
the graph associahedron of three-site chain–with another segment, seeing that when we shrink
the green tubes to a node, we obtain three site chains. All the other facets in figure 4 (right)
are pentagons. Considering they always result from the factorization of the five-site chain into
a four-site chain, whose graph associahedron is a pentagon, and a two-site chain whose graph
associahedron is a point.
The other two cyclic classes,


_{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (4 _,_ 6) _,_ (1 _,_ 6) _},_ _{_ (1 _,_ 3) _,_ (3 _,_ 5) _,_ (1 _,_ 5) _,_ (1 _,_ 6) _},_


produce the graph topology we see at the left in figure 4. The graph associahedron in this case
has 18 vertices, which match the number of terms in the wavefunction coefficient associated with
these type of triangulations.

### **4 Combinatorial cosmohedra**


So far, we have understood how to encode the combinatorics of russian dolls graph-by-graph – via
the graph associahedron. Now we want to understand how to put the information of all graphs
together to find an object that captures the combinatorics of the full wavefunction.
From the amplitudes side, we already know of an object that precisely captures the combinatorics of triangulations of _n_ -gons – the associahedron, Assoc _n_ . The Assoc _n_ is a ( _n_ _−_ 3)-dimensional
polytope whose faces are labelled by collections of non-overlapping chords of the _n_ -gon, such that
the vertices label all possible triangulations of the _n_ -gon. Combinatorially, the associahedron is
defined as follows: Let us consider a set of non-overlapping chords _C_ of the polygon, which defines
a partial triangulation. We say that _C_ _[′]_ is a refinement of _C_ if as sets, we have _C_ _⊂_ _C_ _[′]_ . Then the
associahedron is a polytope that has faces for each _C_ such that


_C_ _[′]_ is a face of _C_ if _C_ _⊂_ _C_ _[′]_ _._ (16)


Note, by convention, the interior of the associahedron is the empty set, and the co-dimension one
facets, ( _n −_ 4)-dimensional, are associated with single chords. We review the associahedron in
more detail in appendix B, as well as the relevant embedding of the polytope in kinematic space,
usually called the ABHY associahedron [5].
Now, the goal is to understand how we can use the structure of the associahedron  - that
captures all the diagrams in a single object – to get an object that puts all the graph associahedra
together therefore describing the combinatorics of russian dolls for all the cubic graphs - the
cosmohedron.


12


Figure 5: (Left) Associahedron (pentagon) and cosmohedron (decagon) at 5-points. (Right) 5point cosmohedron with respective labelling of facets in terms of relevant sub-polygons.


We noted the interesting feature that the graph associahedron for the triangulation of a _n−_ gon
is ( _n_ _−_ 4) dimensional. This is precisely the dimension of a _facet_ of a ( _n_ _−_ 3) dimensional polytope.
This suggests a natural strategy for discovering the cosmohedron. We begin with the _n_ -pt associahedron, which is ( _n_ _−_ 3) dimensional. Each of its vertices corresponds to a complete triangulation,
and for the cosmohedron, we would like to associate a ( _n −_ 4) dimensional graph associahedron
with each of these. Thus, we should take the associahedron and “blow up” each of its vertices into
a full ( _n −_ 4) dimensional facet, with the shape of its corresponding graph associahedron.
It is easy to implement this idea for _n_ = 5: in this case the associahedron is a pentagon and
we simply “blow up” each vertex of the _n_ = 5 pentagon, into the graph associahedron which is
a one-dimensional interval. By doing this, we get a decagon, whose vertices are now labeled by
russian dolls for the _n_ = 5 wavefunction, as shown in figure 5.
Note that while previously for the case of the _n_ = 5 associahedron we had that the edges
were partial triangulations, now for the cosmohedron we have that the edges are partial and full
triangulations. Each such partial/full triangulation contains a set of sub-polygons, and the Russian
dolls obtained at a given vertex contain the sub-polygons entering the union of those appearing
on the edges that meet on the respective vertex.
The picture is much more interesting for _n_ = 6. Here, as we saw earlier, 12 of the 14 triangulations have graphs that are four-site chains, whose graph associahedron are pentagons. The
two triangulations _{_ (1 _,_ 3) _,_ (3 _,_ 5) _,_ (1 _,_ 5) _}, {_ (2 _,_ 4) _,_ (4 _,_ 6) _,_ (2 _,_ 6) _}_ instead have hexagons as their graph
associahedra. Obviously, in order to “blow up” these vertices into pentagons and hexagons, we
will have to introduce many new faces as well, and it is not a priori obvious that the resulting
object will reproduce the combinatorics the cosmohedron is meant to capture. But it does! This
“blow up” of the six-point associahedron to the cosmohedron is shown in figure 1.
Let’s now define the cosmohedron combinatorial for general _n_ . We saw that faces of the
associahedron were associated with collections of non-overlapping chords following face structure
defined by (57). The story for the cosmohedron turns out to be very similar. Instead of collections
of non-overlapping chords _C_, we consider collections of non-overlapping sub-polygons _P_ . Here, as
usual, two sub-polygons are non-overlapping if none of their chords cross; one can be contained
in another, or they can be disjoint. There is one more “russian doll” condition we impose on the
collection _P_ . If _X, Y_ are sub-polygons in _P_ with _Y_ contained in _X_, then there must be other


13


Figure 6: Cosmo6 with labelling of different codimension facets in terms of relevant subpolygons


sub-polygons inside _X_ so that _X_ is fully covered by sub-polygons.
Having defined our subsets _P_, the defining property of the cosmohedron is exactly as it was
for the associahedron. The cosmohedron has faces for all _P_, such that


_P_ _[′]_ is a face of _P_ if _P_ _⊂_ _P_ _[′]_ _._ (17)


The interior of the cosmohedron can be thought as associated with _P_ = (1 _,_ 2 _, · · ·_ _, n_ ) the full
polygon. The co-dimension-1 facets of the cosmohedron are associated with _P_ _[′]_ that correspond
to the sub-polygons in any partial triangulation of the _n_ -gon. This combinatorial rule for the
labelling of the faces is illustrated in figure 6 for _n_ = 6 example.

#### **4.1 Faces and Factorization**


One of the most fundamental properties of associahedra is that faces of associahedra are given by
products of lower associahedron – reflecting the feature of tree-level amplitudes that factorize into
lower point amplitudes when we go near a pole. We now describe the analog of this phenomenon
for the cosmohedron.
Let us first discuss facets of the cosmohedron. These are associated with a collection of nonoverlapping chords _C_ that give a partial triangulation of the _n_ -gon. Given _C_, we have a collection
of sub-polygons _{PC}_ . We also get a dual graph _GC_, obtained by putting a vertex in the middle
of every sub-polygon and connecting vertices when the corresponding sub-polygons share an edge.
Then, we have
Facet _C_ [Cosmo _n_ ] =              - Cosmo _Pi_ _× AGC_ _._ (18)

_Pi⊂PC_


14


Figure 7: (Left) Set of facets corresponding to partial triangulations with a single chord that by
themselves contain _all_ vertices of the cosmohedron. (Right) Set of facets corresponding to full
triangulations that also touch _all_ vertices.


Since our 6-point cosmohedron is three-dimensional, it provides a good illustration of facet factorization. The red facets in figure 1 correspond to full triangulations. Thus, the facets will be
exactly the graph associahedron of the corresponding graph, since all subpolygons are triangles.
The green facets will correspond to partial triangulations with two cords, for this example the
subpolygons involved will always be a square and two triangles. This means we can insert three
nodes in each of the subpolygons, and the only graph we can form is the three-site chain. Then,
the facets will always be squares since the cosmohedron associated with the 4-point wavefunction
is a line interval, and so is the graph associahedron of the three-site chain. Finally, we have the
blue facets, which correspond to a partial triangulation with one cord. There are two types of
blue facets, the one where the cord splits the hexagon into a pentagon and a triangle, and the
one where the cord splits the hexagon into two squares. For both types, the dual graph is the
two-site chain, whose graph associahedron is a point. For the first type (darker blue), we get the
factorization of the 5-point cosmohedron and the 3-point (which is a point), thus these facets will
be decagons, which corresponds to the 5-point cosmohedron. The second type (lighter blue) will
be the result of the factorization into two 4-point cosmohedra, which are segments, resulting in
square facets.

#### **4.2 The geometry of recursive factorization**


In section 2, we explained how there are two equivalent representations of the wavefunction one as a sum over diagrams and their respective russian dolls (5), the other via the recursive
representation in terms of cuts given in (7).
We would now like to point out how the geometry of the cosmohedron makes both representations of the wavefunction completely obvious. Let’s do this by looking at the three-dimensional
cosmohedron (see figure 7). Recall that every term in the russian doll expansion of the wavefunction is associated with a vertex of the cosmohedron.
Now, the point is that there are a number of natural ways of attaching any vertex of the cosmohedron uniquely to some facet of the cosmohedron. We can consider the “maximal” facets of
the cosmohedron that correspond to complete triangulations T, and associate a vertex correspond

15


15

















13





13



35







Figure 8: (Left) ”Cosmologizing” the _n_ = 6 associahedron fan to obtain the Cosmo6 fan. In
light blue, we highlight the cone corresponding to the non-simple vertex. (Right) Labelling of the
four-facets meeting at the non-simple vertex, as well as the two possible “blow up”s into simple
vertices. In both cases, we create a new edge (marked in red) that is already labelled by a full
russian doll.


ing to a given russian doll with its corresponding triangulation. In this way, the collection of all
vertices can be organized into first collecting all the facets associated with triangulations _T_, and
then looking at the vertices of each facet, as given in (5). This is obviously the first representation
or what we called the russian doll picture. But there is another interesting way of associating
vertices with facets: every vertex can also be naturally attached to one of the “minimal” facets of
the cosmohedron corresponding to a single chord. The corresponding facet is just the product of
cosmohedra for the left and right factors on the cut. Hence, we can run through all the vertices
by summing over all these facets, and then take the vertices on them. This way of collecting the
vertices gives us the recursive computation of the wavefunction in terms of the sum over cuts, as
in (7). The russian doll and cut-recursive picture of the polytope are shown in figure 7. Of course,
we can uniquely associate vertices to facets in other ways interpolating between the two extremes
we have discussed, corresponding to different ways of running the recursive sum over cuts, but
deciding to represent some of the lower wavefunction factors directly as a sum over russian dolls.

### **5 “Cosmologizing” the Feynman fan**


We now want to explain how we can systematically obtain the Cosmo _n_ from the _n_ -point associahedron, and to do this it is useful to start by looking at the respective dual fans.
There is a very simple picture for the fan of the cosmohedron, beginning with the fan of the
associahedron. The _g_ -vectors for all the curves ( _i, j_ ) of the associahedron divide the ( _n_ _−_ 3)dimensional _g_ -vector space into cones, each of which corresponds to a triangulation/diagram.
The cosmohedron “cosmologizes” these cones by further subdividing them into smaller cones in a
natural way.
Let us consider the example of the cone of the 6-point associahedron bounded by the curves
_{_ (1 _,_ 3) _,_ (1 _,_ 5) _,_ (3 _,_ 5) _}_ . Since we only care about the direction of the rays, we can represent this
cone projectively by a two-dimensional triangle with ( _g_ 1 _,_ 3 _, g_ 3 _,_ 5 _, g_ 1 _,_ 5) as its vertices (see figure 8,
left only blue vertices). Now, to “cosmologize” this cone, we begin by adding rays corresponding
to all possible subset sums of the rays _{_ (1 _,_ 3) _,_ (3 _,_ 5) _,_ (1 _,_ 5) _}_ bounding the parent cone. Thus, we
have the original rays _g_ 1 _,_ 3 _, g_ 3 _,_ 5 _, g_ 1 _,_ 5 together with _g_ 1 _,_ 3 + _g_ 3 _,_ 5 _, g_ 3 _,_ 5 + _g_ 1 _,_ 5 _, g_ 1 _,_ 3 + _g_ 3 _,_ 5 (in green) and
_g_ 1 _,_ 3 + _g_ 3 _,_ 5 + _g_ 1 _,_ 5 (in red). These add midpoints and the barycenter of the two-dimensional triangle,


16


24





24













Figure 9: (Left) Fan of the 6-point associahedron. (Right) Fan of the 6-point cosmohedron that
can be obtained by “cosmologizing” the associahedron one.


corresponding to the original cone. Now, we build new cones in the obvious way, by joining the
vertices and midpoints of the triangle with the barycenter, as shown in figure 8. In this way,
we produce many new cones, that correspond to the russian doll vertices of the cosmohedron.
Note that the central ray ( _g_ 1 _,_ 3 _, g_ 3 _,_ 5 _, g_ 1 _,_ 5) is bounded by six cones. The corresponding facet of the
cosmohedron is a hexagon, which is the correct graph associahedron for the graph associated with
this triangulation.
The situation is more interesting if we start with a different triangulation of the associahedron,
say bounded by _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_, where the graph associahedron is a pentagon rather than a
hexagon. We again begin with the parent rays and add all the subset sums associated with them,
giving us again the vertices ( _g_ 1 _,_ 3 _, g_ 1 _,_ 4 _, g_ 1 _,_ 5), midpoints ( _g_ 1 _,_ 3+ _g_ 1 _,_ 4 _, g_ 1 _,_ 3+ _g_ 1 _,_ 5 _, g_ 1 _,_ 4+ _g_ 1 _,_ 5) and barycenter
_g_ 1 _,_ 3 + _g_ 1 _,_ 4 + _g_ 1 _,_ 5 (see figure 8, middle). This time to produce the cones, we connect all these points
to the barycenter, _except_ we don’t include an edge connecting _g_ 1 _,_ 4 to _g_ 1 _,_ 3 + _g_ 1 _,_ 4 + _g_ 1 _,_ 5, as highlighted
in figure 8. This means that we have a cone bounded by four rays ( _g_ 1 _,_ 3 + _g_ 1 _,_ 4 _, g_ 1 _,_ 4 _, g_ 1 _,_ 4 + _g_ 1 _,_ 5 _, g_ 1 _,_ 3 +
_g_ 1 _,_ 4 + _g_ 1 _,_ 5), so the corresponding vertex of the cosmohedron belongs to four facets (as illustrated on
the right of figure 8), reflecting the fact we have already mentioned, that the cosmohedron is _not_
a simple polytope. Note also that there are five cones touching the ray at the center, so that the
facet of the cosmohedron associated with triangulation _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ is a pentagon, which
is correctly the graph associahedron of the corresponding diagram.
The combinatorics for the full fans of the six-point associahedron and cosmohedron are shown
in figure 9. The fan is three-dimensional, and the figure shows all the cones of the fan, except
for the cone in the back. For the associahedron (left of figure 9), we see the familiar nine rays
corresponding to the facets, and 14 cones corresponding to the vertices of the associahedron. We
have shaded the five cones meeting at a ray corresponding to the pentagonal faces (dark blue) and
the four cones meeting at a ray corresponding to the square faces of the associahedron (light blue);
for the pentagon, the fifth cone is located on the back triangle and is not shaded to avoid clutter.
For the cosmohedron (right of figure 9), we add the midpoints on all edges and barycenters, and
connect them with edges as shown in the picture. We have highlighted the collection of cones that
give the decagon (dark blue), hexagon (dark pink), pentagon (light pink) and square (light blue
and green) facets of the cosmohedron. Only eight of the ten cones of the decagon are visible in
the picture, the remaining two are on the back triangle of the fan and are again not shaded in the


17


picture to avoid clutter.
In summary, we can obtain the cosmohedron fan by starting with the associahedron fan as
follows: look at a cone of the associahedron fan, which is defined by a collection of g-vectors _gC_,
each associated to a chord _C_ entering the triangulation _T_ dual to the cone, take all possible subsets
_S_ = ( _C_ 1 _, C_ 2 _, · · ·_ _, Ck_ ) with all _Ci_ _∈_ _T_, of any length _k_ = 1 _,_ 2 _, · · ·_ _, n −_ 3, and to each such subset
add a ray:

       _gS_ = _gC._ (19)


_C ∈S_


This defines all the rays of the cosmohedron fan, and therefore the facets of the cosmohedron.
Collections of these rays give us cones that specify the vertices of the cosmohedron. But these
cones are not always simplices - cosmohedra are not simple polytopes.

#### **5.1 Cosmohedra are not simple polytopes**


As we have highlighted earlier, and seen in the _n_ = 6 example, cosmohedra are _not_ simple
polytopes. This is to be contrasted with the associahedron which indeed is a simple polytope (as
we can see from its fan construction as well as in figure 1 for the _n_ = 6 case).
As we will explain now, this feature turns out to be extremely crucial to have an object that
reproduces the combinatorial feature of russian dolls (as described in (17)), and therefore that
encodes the information of the wavefunction.
Let’s say instead we “blow-up” all the non-simple vertices to obtain a simple polytope. For
simplicity let’s look at the case of _n_ = 6, which is the first case this happens, and look at the
non-simple vertex associated with cone _{g_ 1 _,_ 4 _, g_ 1 _,_ 3 + _g_ 1 _,_ 4 _, g_ 1 _,_ 4 + _g_ 1 _,_ 5 _, g_ 1 _,_ 3 + _g_ 1 _,_ 4 + _g_ 1 _,_ 5 _}_ highlighted
in figure 8. In these vertices, the four faces meet - _{_ (1 _,_ 4) _}_, _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_, _{_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ and
_{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ - and the union of their respective subpolygons forms the russian doll containing triangles _{_ (1 _,_ 2 _,_ 3) _,_ (1 _,_ 3 _,_ 4) _,_ (1 _,_ 4 _,_ 5) _,_ (1 _,_ 5 _,_ 6) _}_ and the two squares _{_ (1 _,_ 2 _,_ 3 _,_ 4) _,_ (1 _,_ 4 _,_ 5 _,_ 6) _}_ . Now
there are two ways in which we can blow up this vertex, one way is by adding an edge connecting
rays _g_ 1 _,_ 4 and _g_ 1 _,_ 3 + _g_ 1 _,_ 4 + _g_ 1 _,_ 5 - the object we obtain in this case corresponds to the full barycentric
subdivision of the associahedron, which we will later on denote by _Permuto-cosmohedron_ ; another
way is by adding an edge connecting rays _g_ 1 _,_ 3 + _g_ 1 _,_ 4 and _g_ 1 _,_ 4 + _g_ 1 _,_ 5. At the level of the polytope,
the first type of blow up would lead to the object on the top right of figure 8 while the second one
leads to the one on the bottom right of figure 8.
However, note that in both cases, the object we obtain after the “blow-up” does _not_ encode the
combinatorics of russian dolls correctly. This is because if we look at the new edge (represented
in red in figure 8), it is labelled by the union of the subpolygons of the facets that meet along it,
which in both cases means that it is already labelled by the full russian doll associated with the
original non-simple vertex.
This is an important difference between the cosmohedron and the associahedron. We will now
proceed to discuss the realization of the geometry that precisely reproduces the combinatorics of
the cosmohedron. As we will see, this embedding starts from the kinematic embedding of the
associahedron as in [5] and adds some extra inequalities that precisely shave off this polytope
exactly in the way that produces the correct polytope with non-simple vertices.


18


### **6 Cosmic realizations**

Let’s now discuss the embedding of the cosmohedron in kinematic space. In appendix B, we
described how to carve out the associahedron in the space of planar propagators _Xi,j_ via a set
of inequalities. For the case of the cosmohedron, in addition to the inequalities cutting out the
associahedron, we have an additional set of inequalities that further “shave off” the different
codimension faces of the associahedron.
Recall that for the Cosmo _n_, we have a facet associated with every partial triangulation, given
by a set of non-overlapping chords _C_ . Therefore, for each _C_ we have an inequality of the form

       
_Xc_ _≥_ _ϵC,_ (20)

_c∈C_


where we take
_ϵC_ _≪_ _ci,j,_ (21)


for any ( _i, j_ ), where _ci,j_ are the non-planar Mandelstam that enter the embedding of the associahedron, defining the position of the different facets (see appendix B). With this constraint, we
have that these new inequalities are only “shaving off” faces of the associahedron.
The _ϵC_ must satisfy certain relations and hierarchies for these new inequalities to correctly cut
out the cosmohedron from the underlying associahedron, all of which relate _ϵ_ ’s with the sets _C, C_ _[′]_

to those of the union ( _C ∪_ _C_ _[′]_ ) and the intersection ( _C ∩_ _C_ _[′]_ ). We must have _inequalities_


_ϵC_ + _ϵC′_ _< ϵC∪C′_ + _ϵC∩C′,_ (22)


when _C ∩_ _C_ _[′]_ is empty or is entirely to the left or right of _C, C_ _[′]_, and _equalities_


_ϵC_ + _ϵC′_ = _ϵC∪C′_ + _ϵC∩C′,_ (23)


otherwise. The equalities (23) force the existence of non-simple vertices. Since the facets containing
a given vertex have at most ( _n −_ 3) _Xi,j_ variables in their respective facet inequalities (20), then
any non-simple vertex is obtained by requiring that more than ( _n −_ 3) facet inequalities to be
saturated. This imposes an equality of the type of equation (23).
It is possible to further simplify conditions (23) and (22). The equalities are guaranteed if we
express _ϵC_ as a sum over variables _δP_ attached to every subpolygon of the partial triangulation
given by _C_ . In other words, we take

       _ϵC_ = _δP_ _._ (24)


_P_ of _C_


In turn, the inequalities for the _ϵC_ are guaranteed by very similar inequalities for the _δP_ :


_δP_ + _δP ′_ _< δP_ _∩P ′_ + _δP_ _∪P ′_ (25)


In this expression, we must further ensure that the _δ_ for the full polygon, _δ_ (12 _···n_ ), is set to zero.
It is simple to parametrize _δP_ ’s that satisfy these constraints. For instance, any convex function
of the number of edges (# _P_ ) of _P_, that vanishes when # _P_ = _n_, will satisfy these inequalities. A
simple choice is
_δP_ = _δ_ ( _n −_ # _P_ ) [2] _._ (26)


Here _δ_ is a uniform small factor that we can make as small as we like to ensure that _δP_ and hence
_ϵC_ ’s are all much smaller than the _ci,j_ cutting out the underlying associahedron (21).


19


Figure 10: Realizations of cosmohedra. (Left) Embedding of Cosmo6 with pentagonal facets highlighted in pink and hexagonal ones highlighted in yellow. (Right) Embedding of the Cosmo [1-loop] 3 .
The purple facets correspond to partial triangulations, and the pink and yellow facets correspond
to full triangulations.


This then defines the embedding of the cosmohedron, which automatically also defines an
embedding for the graph associahedra - which we introduced in section 3, to encode the combinatorics of russian dolls graph by graph. To explicitly read off the embedding, all we need to do
is to go on a facet corresponding to the full triangulation that is dual to the graph we want to
consider. In appendix C.1, we give the resulting set of the inequalities that directly carve out the
graph associahedron.
We will now give an example of what the set of equalities/inequalities are for the case of the
Cosmo6.

#### **6.1 6-point example**


For the 6-point cosmohedron, we have 44 different _ϵC_, and we can form 105 sets _{ϵC, ϵC′, ϵC∪C′, ϵC∩C′}._
From these, 12 will be equalities [2], for example:


_ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ + _ϵ{_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ = _ϵ{_ (1 _,_ 4) _}_ + _ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _} ._ (27)


Note that in this case we have _C_ = _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_, _C_ _[′]_ = _{_ (1 _,_ 4) _,_ (1 _,_ 5) _}_, and _C_ _∩_ _C_ _[′]_ = _{_ (1 _,_ 4) _}_ .
So we have that (1 _,_ 4) divides the hexagon into two smaller squares and _C_ fills one of the squares
(the one to the left of _C ∩_ _C_ _[′]_ ) while _C_ _[′]_ fills the other (the one to the right of _C ∩_ _C_ _[′]_ ). Therefore,
we have that _C_ is to the left of _C_ _∩_ _C_ _[′]_ and _C_ _[′]_ is to the right of _C_ _∩_ _C_ _[′]_, and therefore we must
have an equality.
This equality follows from saturating the four facet inequalities:


_X_ (1 _,_ 4) _≥_ _ϵ{_ (1 _,_ 4) _},_ _X_ (1 _,_ 3) + _X_ (1 _,_ 4) + _X_ (1 _,_ 5) _≥_ _ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _},_
(28)
_X_ (1 _,_ 3) + _X_ (1 _,_ 4) _≥_ _ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _},_ _X_ (1 _,_ 4) + _X_ (1 _,_ 5) _≥_ _ϵ{_ (1 _,_ 4) _,_ (1 _,_ 5) _},_


2There is one for each triangulation whose graph associahedron is a pentagon, as in all such cases we have a
non-simple vertex.


20


thus ensuring the existence of the vertex touched by the four facets (which is precisely the one
highlighted in figure 8). From figure 1, it is clear there are 12 such vertices in total, which in the
embedding come from the 12 equalities. The remaining 93 sets will form inequalities, for example:


_ϵ{_ (1 _,_ 3) _}_ + _ϵ{_ (1 _,_ 4) _}_ _< ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _},_
(29)
_ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ + _ϵ{_ (1 _,_ 3) _,_ (1 _,_ 5) _}_ _< ϵ{_ (1 _,_ 3) _}_ + _ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _} ._


In the first case, we have that _C_ _∩_ _C_ _[′]_ = ∅, and therefore we have an inequality. In the second
case, we have that both _C_ and _C_ _[′]_ are to the right of _C ∪_ _C_ _[′]_ and so we also have an inequality.
Finding _ϵC_ which satisfy all 105 relations will ensure that the facet inequalities (20) define the
cosmohedron for the 6-point wavefunction. Finding such a solution is simpler if we impose the
map (24). For example,


_ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ = _δ_ (1 _,_ 2 _,_ 3) + _δ_ (1 _,_ 3 _,_ 4) + _δ_ (1 _,_ 4 _,_ 5 _,_ 6) _,_ _ϵ{_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ = _δ_ (1 _,_ 2 _,_ 3 _,_ 4) + _δ_ (1 _,_ 4 _,_ 5) + _δ_ (1 _,_ 5 _,_ 6) _,_
(30)
_ϵ{_ (1 _,_ 4) _}_ = _δ_ (1 _,_ 2 _,_ 3 _,_ 4) + _δ_ (1 _,_ 4 _,_ 5 _,_ 6) _,_ _ϵ{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ = _δ_ (1 _,_ 2 _,_ 3) + _δ_ (1 _,_ 3 _,_ 4) + _δ_ (1 _,_ 4 _,_ 5) + _δ_ (1 _,_ 5 _,_ 6) _,_


which immediately satisfies (27), as all _δP_ in the first line match the ones in the second line. This
mapping will take (29) to,


_δ_ (1 _,_ 3 _,_ 4 _,_ 5 _,_ 6) + _δ_ (1 _,_ 2 _,_ 3 _,_ 4) _< δ_ (1 _,_ 3 _,_ 4) + _δ_ (1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6) _,_
_δ_ (1 _,_ 4 _,_ 5 _,_ 6) + _δ_ (1 _,_ 4 _,_ 5 _,_ 6) _< δ_ (1 _,_ 3 _,_ 4 _,_ 5 _,_ 6) + _δ_ (1 _,_ 4 _,_ 5) _,_


which are precisely of the form (25). This mapping imposed on all 105 relations will satisfy all
12 equalities and will make several of the 93 inequalities linearly dependent on each other. Thus,
we will have only 57 inequalities of the form (25), which will be satisfied if we parametrize the _δP_
with the convex function (26),
_δP_ = _δ_ (6 _−_ # _P_ ) [2] _._


Therefore, imposing the mapping (24) in the facet inequalities (20), with the parametrization
(26), defines the 6-point cosmohedron. A picture of the embedded object is presented on the right
of figure 10.

#### **6.2 Higher-point examples**


Beyond 6-points, the cosmohedron will be 4-dimensional, or higher. Its complexity increases
rapidly, as it is shown by the counting of vertices and facets in eqs. (11) and (12). Nevertheless,
the construction of these polytopes follows exactly the same procedure, and below we list the
different _F_ -vectors ( _i.e._ the numbers of the different codimension faces) of the cosmohedra up to
9-points:

|codim-1|codim-2|codim-3|codim-4|codim-5|
|---|---|---|---|---|
|2|—|—|—|—|
|10|10|—|—|—|
|44|114|72|—|—|
|196|952|1400|644|—|
|902|7116|18040|18528|6704|



9-points 4278 50550 194616 332664 262728 78408


where codim stands for the codimension of the faces.
As a comparison, we can list the _F_ -vector for the associahedron of the respective amplitudes:


21


|codim-1|codim-2|codim-3|codim-4|codim-5|
|---|---|---|---|---|
|2|—|—|—|—|
|5|5|—|—|—|
|9|21|14|—|—|
|14|56|84|42|—|
|20|120|300|330|132|


9-points 27 225 825 1485 1287 429


As a quick check, one can add all the entries of the _F_ -vector for one of the _n_ -points associahedron above, and confirm that will match the number of codimension-1 faces ( _i.e._ facets) in
the corresponding cosmohedron. We know this is the case because the cosmohedron is obtained
by “shaving” each face of the associahedron, and the facets of the cosmohedron are associated to
partial/full triangulations (which is precisely the information encoded by the different codim faces
of the associahedron).

### **7 Permuto-cosmohedra**


In the previous section, we described the set of inequalities that carve out the cosmohedron,
together with the set of constraints on _ϵC_ required to produce the correct polytope. As we saw, in
addition to the inequalities (22), we also had equalities, which ultimately imply that the polytope
we have is not _simple_ . We now want to explain a systematic way to blow up the polytope into
another polytope which is simple - the permuto-cosmohedron [3] - which will be the object from
which we can ultimately extract the wavefunction (as we explain in the next section).
Let’s go back to the fan definition of the polytope. As explained previously, we can go from
the associahedron fan to the cosmohedron fan by adding rays corresponding to all possible subsets of chords entering on a given triangulation - corresponding therefore to all possible partial
triangulations. However, not all rays are connected to each other, which is why the cosmohedron
is not simple.
We have already explored in detail the non-simple vertex at 6-points where facets _{_ (1 _,_ 4) _}_,
_{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_, _{_ (1 _,_ 4) _,_ (1 _,_ 5) _}_, _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ meet in section 5.1. In particular, we explained
how the two different “blow-up” led to objects that did not consistently describe the combinatorics
of russian dolls.
However, let’s now go back to the blow up in which we produce an edge between facets _{_ (1 _,_ 4) _}_
and _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ - this corresponds to the full _barycentric_ _subdivision_ of the associahedron
fan into a permutohedron fan, leading to what we called the _permuto-cosmohedron_ . For this new
object, we can think of each vertex as labeling the ways in which we can get a full triangulation by
listing chords in a particular order. In particular, for two vertices produced in the blow up, these
correspond to cases in which we start with (1 _,_ 4) and then we have two possible ways to continue
to the full triangulation:


_{_ (1 _,_ 4) _} →{_ (1 _,_ 4) _,_ (1 _,_ 3) _} →{_ (1 _,_ 4) _,_ (1 _,_ 3) _,_ (1 _,_ 5) _},_
(31)
_{_ (1 _,_ 4) _} →{_ (1 _,_ 4) _,_ (1 _,_ 5) _} →{_ (1 _,_ 4) _,_ (1 _,_ 3) _,_ (1 _,_ 5) _},_


each of which corresponds to one of the vertices we obtain after _simplifying_ the non-simple vertex
of the original cosmohedron.


3This object already appeared earlier when we explained the “blow-up” of the non-simple vertex for the _n_ = 6
case.


22


Figure 11: Examples of 1 _/XC_ for different faces of _n_ = 5 and _n_ = 8 cosmohedron.


The permuto-cosmohedron is then a simple polytope whose vertices label all the possible orderings of building full triangulations out of partial triangulations. For general _n_, the fan definition
of the permuto-cosmohedron is simply given by the full barycentric subdivision of the respective
Assoc _n_ fan. This object has manifestly more vertices than the cosmohedron and therefore is not
precisely tailored to the wavefunction. Nonetheless, as we will see momentarily, this permutuhedral
blow-up will provide us a natural way of extracting the full wavefunction from the geometry.
Before proceeding to the extraction of the wavefunction let’s discuss the embedding of the
permuto-cosmohedron. For the cosmohedron we saw that for each facet associated with a given
collection of chords, _C_, we have an inequality of the form of (20), where the _ϵC_ ’s satisfy both
equalities (23) and inequalities (22). To produce the full permuto-cosmohedron all we need to do
is turn the _equalities_ (23) into inequalities, with the same sign, _i.e._ we have that for _any_ collection
of chords _C_ and _C_ _[′]_ :
_ϵC_ + _ϵC′_ _< ϵC∪C′_ + _ϵC∩C′,_ (32)


this then turns all the non-simple vertices into simple ones and gives us precisely the blow-up
corresponding to the permuto-cosmohedron.

### **8 Wavefunction from geometry**


Let’s now discuss how to extract the wavefunction from the geometry. We will start by defining the
canonical form of the graph associahedron for a single graph, and then proceed to the generalization
that gives us the full wavefunction from the cosmohedron.
The connection between the wavefunction and geometry for single graphs is by now the familiar
one. For a single diagram/ _n−_ pt triangulation, with ( _n −_ 3) chords, we have a ( _n −_ 4)-dimensional
graph associahedron. The graph associahedron is simple, hence one computation of the canonical
form of the graph associahedron is given by summing over all vertices – corresponding to complete
tubings/russian dolls - and multiplying by 1 _/P_ ’s for all the tubes corresponding to the facets
meeting at the vertex. This gives us a term with ( _n −_ 4) poles. Of course, _every_ tubing associated
with the diagram has the _E_ total tube surrounding the entire graph, as well as the small circles
encircling every vertex - corresponding to the triangles entering the triangulation dual to the
graph. Hence, we have



Ψ _G_ = _P_ 1tot _×_ 
_v⊂G_



1
_Pv_ _×_ Ω( _AG_ ) _,_ (33)



where _P_ tot is the perimeter of the full _n_ -gon corresponding to _Et_, and _Pv_ the perimeter of each
triangle entering the underlying triangulation.


23


The extraction of the wavefunction for the sum over all diagrams is much more interesting.
Let’s consider the simple polytope we get by blowing-up the cosmohedron as described in the
previous section - the permuto-cosmohedron. Each facet of this polytope is associated a partial
triangulation given by a collection of non-overlapping chords _C_ . Let _nC_ be the number of nontriangle subpolygons entering in the partial triangulation defined by _C_, then we define



1
_≡_ [1]
_XC_ _nC_




 

_P,P_ _[′]_ meeting on edge



1
_PP_ _P_ _[′]_ _P ′_ _[,]_ (34)



where we consider the products of the perimeters of the subpolygons entering in _C_ that share an
edge, and sum over them (see figure 11). So this means that to each facet, instead of associating a
single singularity (like we do to extract the amplitude from the associahedron), we associate _pairs_
_of_ _singularities_ . It is clear that we could not associate a single singularity to each facet simply
because the dimensionality of the Cosmo _n_ does not match the number of singularities on Ψ _n_ . This
new feature reflects that even the way we extract the wavefunction from the canonical form of
cosmohedra requires a generalization from what is done in the amplitudes case.
We now look at the canonical form for the permutohedron, associating _XC_ (34)). Since the
permuto-cosmohedron is simple, the canonical form is the sum over all vertices weighted by the
product of all 1 [for] [the] [facets] [that] [meet] [on] [the] [vertex.] [While] [this] [manifestly] [has] [only] [simple]
_XC_ [’s]
poles in terms of 1 [it] [will] [clearly] [have] [terms] [with] [simple] [poles] [as] [well] [as] [double] [and] [higher]
_XC_ [,]
poles when written in terms of the 1 [But] [the] [claim] [is] [that] [the] [wavefunction] [is] [given] [by] [the]
_PP_ [.]
part of the canonical form with only simple poles:

Ψ = _E_ [1] _t_ _×_ Ω( _XC_ ) _|_ single poles in _P_ P _._ (35)

#### **8.1 5-point example**


At five points the cosmohedron is simple, therefore it coincides with the permuto-cosmohedron.
Then, we can directly compute the poles of each facet, _XC_, according to (34). Let’s consider the
facet labelled by the cords _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_, the singularity pairs we associate to it are (see figure
11):
1 1 1
= + _._
_X{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ _P_ 123 _P_ 134 _P_ 134 _P_ 145


Similarly, we can compute the singularity pairs of the facets that meet facet _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ - those
are _{_ (1 _,_ 3) _}_, and _{_ (1 _,_ 4) _}_ - for which we have:


1 1 1 1
= _,_ = _._
_X{_ (1 _,_ 3) _}_ _P_ 123 _P_ 1345 _X{_ (1 _,_ 4) _}_ _P_ 1234 _P_ 145


We can now compute the contributions of each of these two vertices to the wavefunction:


1 1 1
= + _,_
_X{_ (1 _,_ 3) _,_ (1 _,_ 4) _}X{_ (1 _,_ 3) _}_ _P_ 123 [2] _[P]_ [134] _[P]_ [1345] _P_ 123 _P_ 134 _P_ 145 _P_ 1345

1 1 1
= + _._
_X{_ (1 _,_ 3) _,_ (1 _,_ 4) _}X{_ (1 _,_ 4) _}_ _P_ 123 _P_ 134 _P_ 145 _P_ 1234 _P_ 134 _P_ 145 [2] _[P]_ [1234]


According to (35), in the first line above, we send the first term to zero, and in the second line
we send the second term to zero. So we are left with precisely the russian dolls contributing to


24


each vertex (see figure 5). When we sum these two terms, they add up to the wavefunction of the
graph corresponding to the triangulation _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ . By computing the contributions from the
remaining vertices of the decagon, we obtain the full wavefunction at 5-points.

#### **8.2 6-point example**


Let us now see how the prescription in (35) gives us the correct contribution in the blown up
vertices at 6-points. Let us use our running example of the vertices in (31) as an example (see
top right of figure 8). For the first line in (31), which corresponds to one vertex of the permutocosmohedron, the pairs of singularities are:



1        - 1
=
_X{_ (1 _,_ 4) _}X{_ (1 _,_ 3) _,_ (1 _,_ 4) _}X{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ 2 _P_ 1234 _P_ 1456



�� 1 1
+
_P_ 123 _P_ 134 _P_ 134 _P_ 1456




_×_




 - 1 1 1
_×_ + +
_P_ 123 _P_ 134 _P_ 134 _P_ 145 _P_ 145 _P_ 156




_,_



where the [1] [the] [first] [factor] [comes] [from] [the] [fact] [that] [the] [facet] _[{]_ [(1] _[,]_ [ 4)] _[}]_ [has] [two] [non-triangle]

2 [in]
subpolygons, two squares, thus _nC_ = 2 in (34). As for the second line in (31), the other vertex
coming from the blow up, the contribution will be:



1        - 1
=
_X{_ (1 _,_ 4) _}X{_ (1 _,_ 4) _,_ (1 _,_ 5) _}X{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ 2 _P_ 1234 _P_ 1456



�� 1 1
+
_P_ 1234 _P_ 145 _P_ 145 _P_ 156




_×_




 - 1 1 1
_×_ + +
_P_ 123 _P_ 134 _P_ 134 _P_ 145 _P_ 145 _P_ 156




_._



After sending all double poles (or higher) to zero, one can check that the added contribution
of the two vertices above is:




 - 1
2
2 _P_ 123 _P_ 134 _P_ 145 _P_ 156 _P_ 1234 _P_ 1456




_,_



which is precisely the russian doll term associated with the original non-simple vertex in the
cosmohedron (see figure 8). The remaining non-simple vertices follow the same blow up into two
vertices, and all other vertices are simple. Following the same prescription as in the examples
above, one can compute the 6-point wavefunction from the permuto-cosmohedron.

### **9 Loop cosmohedra**


The associahedron picture for Tr( _ϕ_ [3] ) amplitudes at tree-level was extended to one-loop polytopes [50,51], and then to all loop orders in the curve-integral formalism [6,7]. Indeed, the picture
of curves on surfaces most naturally gives us the “Feynman fan”, with every curve _X_ on the
surface associated with a g-vector _gX_ . Beautifully, maximal collections of non-overlapping curves
form cones that tile all of g-vector space. This fan is the setting for the “global Schwinger parameterization” of the curve integral formalism; a related but distinct fact is that this fan can also be
thought of as the normal fan of polytopes - “surfacehedra” - that capture the combinatorics of
surfaces and all their cuts in their facet structure.


25


Figure 12: (Left) Cosmohedron 2-point 1-loop, edges are labelled by partial triangulations with a
single curve (where we have two types of curves ending in the puncture, marked in red and blue),
and vertices correspond to full triangulations. We can read off the russian doll at each vertex by
taking the union of the subsurfaces entering on each edge. (Right) Cosmohedron 3-point 1-loop.
Highlighted in blue and green we have facets labeled by a single curve (squares, decagons and
dodecagons); in gray facets labeled by two curves (squares); and in red and yellow faces labelled
by full triangulations (pentagons and hexagons) – corresponding to the graph-associahedra for the
loop graphs.


Thus, we should expect cosmohedra to exist at loop-level as well, generalizing surfacehedra in
the same way they generalized associahedra at tree-level. Of course these objects do exist, and in
this section we will give a telegraphic account of loop-level cosmohedra, assuming some familiarity
with the curves-on-surfaces picture for amplitudes of [6,10]. We will return to give more leisurely,
self-contained and systematic exposition of these objects in future work.
To begin with, the combinatorial definition of loop level cosmohedra is exactly the same as
what we have seen at tree-level, where instead of collections of “sub-polygons” _P_ we consider more
generally collection of subsurfaces. We give simple examples of 2- and 3-dimensional cosmohedra
associated with the _n_ = 2 _,_ 3 at 1-loop, corresponding to the once-punctured disk with marked
points on the boundary, in figure 12. Note that, as familiar for amplitudes, it is natural to include
two kinds of “loop” curves corresponding to the two kinds of “spiraling” loop variables around the
puncture.
From the examples presented, we can also observe how the factorization (18) holds at looplevel. Let us consider figure 12 (right), the red and yellow facets correspond to graph associahedra
directly, since they are full triangulations. Then the green facets are dodecagons since they correspond to the product of a 3-point tree level cosmohedron, which is a point, a two-point loop
level cosmohedron, which is a dodecagon, and a graph associahedron corresponding to the two-site
chain, which is a point. The dark blue facets are decagons, since they correspond to the product of
a 5-point tree level cosmohedron (a decagon), and the graph associahedron of a tadpole (a point).
Then, the light blue facets are squares, since they correspond to the product of a 4-point tree-level
cosmohedron, which is an interval, a one-point one-loop cosmohedron, which is also an interval,
and the graph associahedron of the two-site chain (which is a point).
Now, the most obvious picture for generalizing the cosmohedron to all loops therefore proceeds
by generalizing the picture of “cosmologizing” the Feynman fan. These proceeds precisely in the


26


Figure 13: (Left) Graph associahedron for the triangle graph. (Right) Graph associahedron for
the box graph.


same way as for the tree-level cosmohedron. We subdivide every cone in _g_ -vector space into smaller
cones, by considering all possible sums of the _g_ -vectors in a given cone. This yields the fan for the
loop cosmohedron, which allows us to write the facet inequalities:

       
_Xc_ _≥_ _ϵC,_

chords _c_ in _C_


where _C_ is a given partial triangulation of the punctured disk. For the loop case, the propagator
variable _Xi,j_ differs from _Xj,i_, since the chord can go around the loop in two different ways [4] . We
will also have propagators attached to tadpoles, _Xi,i_ . As well as the propagators in the loop, _Xi,p_
and _X_ [˜] _i,p_ (where _p_ is labelling the puncture).
The constants in the facet inequalities, _ϵC_, obey the same equalities and inequalities as in tree
level, (23) and (22), respectively. Also at loop level, the equalities are automatically satisfied if
we map each _ϵC_ to the sum of the sub-surfaces in the correspondent partial triangulation,


       _ϵC_ = _δP_ _,_


_P_ of _C_


And the inequalities in the _ϵ_ are all automatically satisfied if we satisfy the inequalities:


        _δP_ + _δP ′_ _< δP_ _∪P ′_ + _δP_ ˜ _,_ (36)

_P_ ˜ _∈{P_ _∩P ′}_


where the sum over _δP_ ˜ is reflecting the fact that at loop level the intersection of two sub-surfaces
can be given by two or more disjoint surfaces.

#### **9.1 Graph associahedra at loop-level**


At loop level, the graph associahedron is obtained exactly the same way as for tree-level. For each
triangulation, we associate a node to each subsurface, and connect the nodes between subsurfaces


4Even though when we assign momentum to these curves in the standard way, _i.e._ by homology, they both have
the same momentum.


27


that share an edge, building the dual graph, _GT_ . Then the graph associahedron, _AG_, is the
polytope whose facets correspond to the different tubes of the graph (not including the tubes that
enclose single vertices nor the tube that encloses the full graph), and the vertices correspond to
complete tubings. The factorization property, defined by eq.(13), holds at loop level. Let’s now
give some simple examples at one-loop.


**Three-point** **triangle** **diagram** The graph associahedron of the triangle diagram is a hexagon
(see figure 13, left), precisely matching the six russian dolls one can find in the graph. The triangle
graph is dual to the triangulation of the punctured disk containing curves _{_ ( _p,_ 1) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _}_ .
The facets in figure 13 (left) either correspond to blue tubes or to red tubes, both are segments.
The red tube corresponds to the product of the graph associahedron of the two site chain,
which is a point, with the graph associahedron of the bubble (obtained by shrinking the red tube
to a node), which is a segment.
The blue tube corresponds to the product of the graph associahedron of the three-site chain,
which is a segment, which the graph associahedron of the tadpole (obtained by shrinking the blue
tubes to a node), which is a point.
All the terms will correspond to the product of a blue tube with a red tube, which is clear by
the facet intersections in figure 13 (left), and respective labeling (which are the nesting of the red
tube in the blue tube). One such term, after factoring out the total energy and the triangles, is:


1
_,_
_P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ ( _p,_ 1) _,_ ( _p,_ 3)


the remaining 5 terms are just variations of this one, as one can see by the labels of figure 13 (left).


**Four-point** **box** **diagram** The graph associahedron for the four-point box diagram has 20
vertices, 32 edges and 14 facets, as can be seen in the right of figure 13. This corresponds to the
triangulation _{_ ( _p,_ 1) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _,_ ( _p,_ 4) _}_ of the punctured disk. The graph associahedron will have
three types of facets, the tubes with two sites (red tubes in figure 13) will be hexagons, the tubes
with three sites (green tubes in figure 13) will be squares, the tubes with four sites (blue tubes in
figure 13) will be pentagons.
The red tubes will correspond to the product graph associahedron of the two-site chain (subgraph inside the red tube), which is a point, with the graph associahedron of the triangle diagram
(obtained after shrinking any red tube in the box), which we can see from the left of figure 13,
that is a hexagon.
The green tubes will correspond to the product of the graph associahedron of the three-site
chain, which is an interval, with the graph associahedron of the bubble (obtained by shrinking any
green tube in the box diagram in the right of figure 13), which is also a segment. The product is
a square.
Finally, the blue tubes will correspond to the product of the graph associahedron of the four-site
chain, which is a pentagon (as can be verified in the left of figure 3), with the graph associahedron
of the tadpole, which is a point.
In total, the polytope has 20 vertices, precisely matching the number of russian dolls in the
graph. There will be 16 terms which correspond to a tubing which has a blue, a green and a red
tube. One such term, after factoring out the total energy and the triangles, is:


1
_,_
_P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 4) _,_ (4 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 4) _,_ ( _p,_ 1) _,_ ( _p,_ 4) _P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ ( _p,_ 1) _,_ ( _p,_ 3)


28


and one can consider 16 similar tubings. In the polytope of figure 13, one can identify these terms
by finding the vertices that are intersections of facets labeled by a blue tube, a green tube and a
red tube. The other 4 terms correspond to the product of a blue tube with two red tubes, one
such example is:


1
_._
_P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 4) _,_ (4 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ ( _p,_ 1) _,_ ( _p,_ 3) _P_ (3 _,_ 4) _,_ (4 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 1)


Again one can count four vertices in figure 13 which are the intersection of two facets labeled
by a red tube and one facet labeled by a blue tube.

#### **9.2 One-loop cosmohedra realization**


As described earlier, the embedding of the loop cosmohedra is done exactly in the same way as in
the tree-level case. We now proceed to give some explicit examples.


**Two-points** The one-loop two-points associahedron is a hexagon, thus the corresponding cosmohedron will be a dodecagon. The Feynman fan is given by the g-vectors:


_g_ 1 _,_ 1 _,_ _g_ 2 _,_ 2 _,_ _gp,_ 1 _,_ _gp,_ 2 _,_ _gp,_ ˜ 1 _,_ _gp,_ ˜ 2 _,_


and we “cosmologize” it by adding the following linear combinations of g-vectors:


_g_ 1 _,_ 1 + _gp,_ 1 _,_ _g_ 2 _,_ 2 + _gp,_ 2 _,_ _gp,_ 1 + _gp,_ 2 _,_


as well as the other three rays with _gp,i_ _→_ _gp,i_ ˜ . Now that we have the form of our facet inequalities,
we only need to parametrize the _ϵ_ constants which will “shave off” the underlying loop associahedron polytope. The _ϵ_ will have to satisfy 6 inequalities in order to yield the correct polytope and
since in this case the polytope is two-dimensional, and thus simple, there are no equalities to be
imposed on the _ϵ_ -space,


_ϵ{_ (1 _,_ 1) _}_ + _ϵ{_ ( _p,_ 1) _}_ _< ϵ{_ (1 _,_ 1) _,_ ( _p,_ 1) _},_ _ϵ{_ ( _p,_ 1) _}_ + _ϵ{_ ( _p,_ 2) _}_ _< ϵ{_ ( _p,_ 1) _,_ ( _p,_ 2) _},_


and the remaining for are obtained by the mappings _p_ _→_ _p_ ˜ and/or 1 _→_ 2. These inequalities
transform into intersections and unions of sub-surfaces when using the mapping (24):


_δ{_ (1 _,_ 1) _}_ + _δ{_ (1 _,_ 2) _,_ (2 _,_ 1) _,_ ( _p,_ 1) _}_ _< δ{_ (1 _,_ 1) _,_ ( _p,_ 1) _},_
_δ{_ (1 _,_ 2) _,_ (2 _,_ 1) _,_ ( _p,_ 1) _}_ + _δ{_ (1 _,_ 2) _,_ (2 _,_ 1) _,_ ( _p,_ 2) _}_ _< δ{_ (1 _,_ 2) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _}_ + _δ{_ (2 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _},_


respectively. Here, the _δP_ are labelled by the cords that bound the sub-surface. The second
inequality is an example of the case where the intersection of the surfaces on the left-hand side is
given by multiple disjoint sub-surfaces.


**Three-points** At three-points the cosmohedron is three-dimensional, it has 108 vertices, 168
edges and 62 facets. This means we will have 62 _ϵC_, which will form 138 inequalities, and 12
equalities. One such equality is:


_ϵ{_ (1 _,_ 1) _,_ (1 _,_ 3) _}_ + _ϵ{_ (1 _,_ 1) _,_ ( _p,_ 1) _}_ = _ϵ{_ (1 _,_ 1) _}_ + _ϵ{_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ ( _p,_ 1) _},_


29


and the other 11 equalities are variations of this one. On the other hand, two examples of inequalities are:


_ϵ{_ (1 _,_ 1) _}_ + _ϵ{_ (1 _,_ 3) _}_ _< ϵ{_ (1 _,_ 1) _,_ (1 _,_ 3) _},_
_ϵ{_ ( _p,_ 1) _,_ ( _p,_ 2) _}_ + _ϵ{_ ( _p,_ 1) _,_ ( _p,_ 3) _}_ _< ϵ{_ ( _p,_ 1) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _}_ + _ϵ{_ ( _p,_ 1) _},_


which have the corresponding form in terms of overlaps of sub-surfaces:


_δ{_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _}_ + _δ{_ (1 _,_ 3) _,_ (3 _,_ 1) _}_ _< δ{_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ (3 _,_ 1) _},_
_δ{_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ ( _p,_ 1) _,_ ( _p,_ 3) _}_ + _δ{_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _}_ _< δ{_ (2 _,_ 3) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _}_ + _δ{_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ ( _p,_ 1) _},_


where the union in the first line is the total energy sub-surface, which we set to zero. This
example also provides a good illustration of the factorization of the facets at one-loop. The facets
labelled by the cords _{_ (2 _,_ 1) _}_, _{_ (3 _,_ 2) _}_ or _{_ (1 _,_ 3) _}_ will be dodecagons, since they constitute the
factorization into the one-loop two-points cosmohedron, the tree level three-point cosmohedron
and the two-site chain graph associahedron, which are a dodecagon, and two points, respectively.
Thus, the cosmohedron will have three dodecagon facets. Then, the facets labelled by the cords
_{_ ( _p,_ 1) _}_, _{_ ( _p,_ 2) _}_ or _{_ ( _p,_ 3) _}_, (as well as the facets with _p_ _→_ _p_ ˜) will be decagons, since here the
facet factorizes into one sub-surface with five boundaries and no puncture, thus it will be the
cosmohedron of the five point wavefunction, which is a decagon, and the graph associahedron of
the one site graph, which is a point. The cosmohedron will have 6 decagon facets. Finally, the
facets labelled by the cords _{_ (1 _,_ 1) _}_, _{_ (2 _,_ 2) _}_ or _{_ (3 _,_ 3) _}_ will be squares. Since they represent the
factorization of the facet into a square and the one-loop one-point sub-surface, and the graph
associated to it is the two-site chain. Thus, the facet is the product of two segments and a point,
which is a square. Following this factorization properties, one can find the remaining facets of the
cosmohedron.

#### **9.3 Extracting the loop wavefunction from geometry**


Extracting the wavefunction from the cosmohedron at loop level is very similar to tree level. One
starts by constructing the permuto-cosmohedron, which follows from turning the equalities into
inequalities, and then constructing the canonical form for the polytope and extracting the part
with only simple poles.
Firstly, we will discuss how to build the permuto-cosmohedron at loop level. We have seen
in the beginning of this section that the structure of the equalities and inequalities is exactly
the same. And each equality corresponds to a non-simple vertex in the cosmohedron. Then, to
“simplify” these vertices one turns the equalities into inequalities in the same way as we did at
tree level:
_ϵC_ + _ϵC′_ = _ϵC∪C′_ + _ϵC∩C′_ _→_ _ϵC_ + _ϵC′_ _< ϵC∪C′_ + _ϵC∩C′ ._


Finding a parametrization of the _ϵ_ satisfying all inequalities, will ensure we obtain the permutocosmohedron at loop level.
To extract the full wavefunction, the pairs of singularities we associate to each facet have
to be slightly reformulated, relative to the tree level case. If we consider a given facet and the
corresponding partial triangulation, labeled by the set of cords _C_, and _nC_ being the number of
sub-surfaces with more than three bounding edges in the partial triangulation, then we still define,



1
_≡_ [1]
_XC_ _nC_





 

_P,P_ _[′]_ meeting on edge


30



1
_PP_ _P_ _[′]_ _P ′_







_._ (37)


However, when in the set _C_ there is only one chord connecting the inner puncture to the disk
boundary, ( _p, i_ ), then the partial triangulation will have a sub-surface with two edges which go
around this chord - say _{_ ( _i, p_ ) _,_ ( _p, i_ ) _}_ - like we see for the subsurfaces in red and blue in the (left)
top russian doll depicted in figure 12. In these cases we have to associate a triangle sub-surface
to the chord, ( _p, i_ ), which we will define to be _PP_ _≡T_ ( _p,i_ ). And this sub-surface borders only
with the sub-surface which goes around the cord ( _p, i_ ). The wavefunction is defined from the
permuto-cosmohedron in the same way as at tree-level, except in the end, after selecting the single
poles in the canonical form, we set all _T_ ( _p,i_ ) _→_ 1. Therefore, we can write,




  - 1
Ψ = _Et_ _×_ Ω( _XC_ ) _|_ single poles in _P_ P



_._ (38)
����� _T_ ( _p,i_ ) _→_ 1



**One-loop** **two-point** **wavefunction** The cosmohedron for the one-loop two-point wavefunction is simple, therefore is equivalent to the permutahedral “blow-up”. The cosmohedron is a
dodecagon, and here we will discuss explicitly how to compute the contributions from three vertices, since the remaining ones are some variation of these. First, let us consider the vertex which
results from the intersection of the facets _{_ ( _p,_ 1) _}_ and _{_ ( _p,_ 1) _,_ ( _p,_ 2) _}_ . Then according to the above
discussion we can write:


1 1 1 1
= _,_ = _._
_X{_ ( _p,_ 1) _}_ _P_ (1 _,_ 2) _,_ (2 _,_ 1) _,_ ( _p,_ 1) _T_ ( _p,_ 1) _X{_ ( _p,_ 1) _,_ ( _p,_ 2) _}_ _P_ (1 _,_ 2) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _P_ (2 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 2)


Therefore, the contribution from this vertex is:


1
_,_
_EtP_ (1 _,_ 2) _,_ (2 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 2) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _P_ (2 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 2)


where we have set the value of _T_ ( _p,_ 1) to one at the end. Then, we can compute the contribution of
the vertex which is the intersection of the facet _{_ ( _p,_ 1) _}_ and _{_ (1 _,_ 1) _,_ ( _p,_ 1) _}_,


1 1 1 1 1
= _,_ = + _,_
_X{_ ( _p,_ 1) _}_ _P_ (1 _,_ 2) _,_ (2 _,_ 1) _,_ ( _p,_ 1) _T_ ( _p,_ 1) _X{_ (1 _,_ 1) _,_ ( _p,_ 1) _}_ _P_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _T_ ( _p,_ 1)


which in the end will lead to the contribution,


1
_,_
_EtP_ (1 _,_ 2) _,_ (2 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 2) _,_ (2 _,_ 1) _,_ (1 _,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1)


keep in mind that we dropped the terms with _T_ ( [2] _p,_ 1) [,] [just] [like] [for] [any] [other] [sub-surface,] [and] [only]
in the end we set _T_ ( _p,_ 1) _→_ 1. And finally, we can compute the contribution from the vertex at the
intersection of the facets _{_ (1 _,_ 1) _}_ and _{_ (1 _,_ 1) _,_ ( _p,_ 1) _}_,


1 1 1 1 1
= _,_ = + _,_
_X{_ (1 _,_ 1) _}_ _P_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 1) _P_ (1 _,_ 1) _X{_ (1 _,_ 1) _,_ ( _p,_ 1) _}_ _P_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _T_ ( _p,_ 1)


and its contribution to the wavefunction is:


1
_._
_EtP_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 1) _P_ (1 _,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1)


31


**One-loop** **three-point** **wavefunction** Now we will proceed with the three-point one-loop example. Here we will compute one contribution from a non-simple vertex and one of the terms
in the triangle diagram, since these are the vertices that best illustrate the differences with
the tree-level computations. Let us start with the non-simple vertex, where the facets _{_ (1 _,_ 1) _}_,
_{_ (1 _,_ 1) _,_ (1 _,_ 3) _}_, _{_ (1 _,_ 1) _,_ ( _p,_ 1) _}_, and _{_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ ( _p,_ 1) _}_ meet. The permutahedral “blow-up” splits
it into two vertices, one of which, is the intersection of the facets _{_ (1 _,_ 1) _}_, _{_ (1 _,_ 1) _,_ (1 _,_ 3) _}_, and
_{_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ ( _p,_ 1) _}_, and another _{_ (1 _,_ 1) _}_, _{_ (1 _,_ 1) _,_ ( _p,_ 1) _}_, and _{_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ ( _p,_ 1) _}_ . For the first
vertex, we can write,


1 1 1 1 1
= _,_ = + _,_
_X{_ (1 _,_ 1) _}_ _P_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _P_ (1 _,_ 1) _X{_ (1 _,_ 1) _,_ (1 _,_ 3) _}_ _P_ (1 _,_ 2) _,_ (1 _,_ 3) _,_ (2 _,_ 3) _P_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ (3 _,_ 1) _P_ (1 _,_ 1) _P_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ (3 _,_ 1)

1 1 1 1
= + + _,_
_X{_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ ( _p,_ 1) _}_ _P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (1 _,_ 3) _P_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ (3 _,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ (3 _,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _T_ ( _p,_ 1)


for the second vertex the partial triangulation with two cords will differ, it is,


1 1 1
= + _._
_X{_ (1 _,_ 1) _,_ ( _p,_ 1) _}_ _P_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _T_ ( _p,_ 1)


Naturally, both vertices will give the same contribution, which is,


1
_._
2 _EtP_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _P_ (1 _,_ 1) _P_ (1 _,_ 1) _,_ ( _p,_ 1) _P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (1 _,_ 3) _P_ (1 _,_ 1) _,_ (1 _,_ 3) _,_ (3 _,_ 1)


Since they are two, the one-half will cancel. Finally, we will look at the vertex at the intersection
of the facets, _{_ ( _p,_ 1) _}_, _{_ ( _p,_ 1) _,_ ( _p,_ 2) _}_, and _{_ ( _p,_ 1) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _}_ . This is one of the 6 vertices in the
facet of the cosmohedron which corresponds to the triangle diagram. For this vertex, we can write,


1 1 1 1
= _,_ = _,_
_X{_ ( _p,_ 1) _}_ _P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ ( _p,_ 1) _T_ ( _p,_ 1) _X{_ ( _p,_ 1) _,_ ( _p,_ 2) _}_ _P_ (1 _,_ 2) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _P_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 2)

1 1 1 1
= + + _._
_X{_ ( _p,_ 1) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _}_ _P_ (1 _,_ 2) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _P_ (2 _,_ 3) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _P_ (2 _,_ 3) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _P_ (3 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 3) _P_ (1 _,_ 2) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _P_ (3 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 3)


This leads to the contribution, for this vertex,


1
_,_
_EtP_ (1 _,_ 2) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _P_ (2 _,_ 3) _,_ ( _p,_ 2) _,_ ( _p,_ 3) _P_ (3 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 3) _P_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ ( _p,_ 1) _,_ ( _p,_ 2) _P_ (1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ ( _p,_ 1)


which we can check to be one of the tubings of the triangle diagram.

### **10 Cosmological correlahedra**


Having found a geometry underlying the wavefunction for Tr( _ϕ_ [3] ) theory, it is natural to go a step
further, and ask whether there is any geometry not just for the wavefunction, but directly for the
physical observable, the correlator. Taking a step back to put this question into context, while the
discoveries of geometries underlying amplitudes and wavefunctions have been remarkable, it is still
unsatisfying that what we are supposed to physically _do_ with these objects - namely, mod-square
them to get probabilities, expectation values and correlation functions - is left untouched. The


32


Figure 14: (Left) Fan of the cosmological correlahedron for _n_ = 4. In dashed, we represent the
underlying associahedron fan. (Right) 4-points cosmological correlahedron.


burning question is simple - given that there are autonomous combinatorial/geometric structures
underlying amplitudes and wavefunctions, what sort of cousin of these objects makes it natural
to discover the Born rule, and ultimately the physical observables?
In this section, we will sketch an answer to this question by briefly introducing “cosmological
correlahedra” capturing all the contributions to the correlator in Tr( _ϕ_ [3] ) theory. As we will see,
they naturally combine both associahedra and cosmohedra in a single higher-dimensional polytope.
Let’s begin with a quick reminder on how to compute flat-space correlators in the language of
polygons. In addition to subpolygons, we simply also include the chords _ki,j_ = _|_ _[⃗]_ _ki,j|_ in the story. A
term in the correlator is determined by first giving a (possibly empty) collection of non-overlapping
chords, _C_, with which we associate a factor of [�] ( _i,j_ ) _∈C_ [(1] _[/k][i,j]_ [).] [This collection of chords divides the]

polygon into subpolygons ( _P_ compatible with _C_ ), and we further multiply by the wavefunction
of each of the subpolygons. We then sum over all choices for the initial set of non-overlapping
chords. So we can write:



1 _×_ - Ψ _P,_ (39)
_ki,j_

_P_ compatible _C_




  Corr _n_ = Φ _n_ +


_C̸_ = _∅_






( _i,j_ ) _∈C_



where here we manifestly separated the case in which the collection of chords is empty, that just
gives us the full wavefunction. The combinatorics of the full correlator is then clearly a hybrid
between those of amplitudes (non-crossing chords) and the wavefunction (non-overlapping subpolygons).
Now, it is natural to expect any geometry for the full correlator to live in one higher dimension
than the associahedron/cosmohedron. The reason is that while all the terms in the wavefunction
have an _Et_ singularity, which is not explicitly included as a facet in the cosmohedron, this is
not the case for the full correlator - some terms have _Et_ singularities (those coming from Ψ _n_ in
(39)) and others don’t (the remaining terms in (39)). Thus, it stands to reason to think about an
object in one higher dimension, roughly corresponding to _Et_, with a “bottom” facet associated
with _Et_, which looks like the cosmohedron. If this object is to include the combinatorics of nonoverlapping chords, then we know that these objects alone, with no reference to sub-polygons
at all, are captured by the associahedron. So it is reasonable to expect that the “cosmological
correlahedron” we are looking for should be a sort of sandwich in an extra dimension, with the


33


cosmohedron at the “bottom”, and an associahedron maximally far away, at the “top” of the new
direction.
This can also be nicely motivated by trying to guess what the fan of this higher-dimensional
object might look like. Let us consider the simplest possible case of _n_ = 4. The fan for the
associahedron has the two usual rays for g-vectors (1 _,_ 3) _,_ (2 _,_ 4), pointing in opposite directions
in one dimension. But we will introduce two new rays, “ _B_ ” and “ _T_ ” (for “bottom” and “top”)
pointing in opposite directions in a second direction. We know we want to have facets of the
correlator polytope corresponding to two different kinds of single chords: one where the single
chord is associated with subpolygons (like we saw earlier for the wavefunction), and another
where it is associated simply with the _|_ _[⃗]_ _k|_ in the correlator. We will thus record images of the rays
(1 _,_ 3) _,_ (2 _,_ 4) on the bottom and top, by defining


(1 _,_ 3) _B_ = (1 _,_ 3) + _B,_ (2 _,_ 4) _B_ = (2 _,_ 4) + _B,_
(40)
(1 _,_ 3) _T_ = (1 _,_ 3) + _T,_ (2 _,_ 4) _T_ = (2 _,_ 4) + _T._


This gives us the six rays _T,_ (1 _,_ 3) _T_ _,_ (1 _,_ 3) _B, B,_ (2 _,_ 4) _B,_ (2 _,_ 4) _T_, which is naturally associated with
the hexagon shown in figure 14. We see that this hexagon has an interval at the top and one
at the bottom, naturally associated with the _n_ = 4 associahedron and cosmohedron respectively.
Note that the top facet only has vertices of the associahedron, and does not by itself correspond
to any terms in the correlator. But the remaining four vertices (highlighted in black in figure 14)
are naturally associated with all the terms in the correlator.
Let’s move on to the next example at _n_ = 5, where we will see almost all the relevant structure
for general _n_ . We again start from the rays of the associahedron, which we can label with the
chords (1 _,_ 3) _,_ (1 _,_ 4) _,_ (2 _,_ 4) _,_ (2 _,_ 5) _,_ (2 _,_ 6), now living in two dimensions, and add _B, T_ pointing in
opposite directions in an extra third direction. We then produce the rays ( _i, j_ ) _B_ = ( _i, j_ ) + _B_ and
( _i, j_ ) _T_ = ( _i, j_ ) + _T_ as before. But on the bottom, we continue to produce the rest of the rays
for the cosmohedron as we have described before, by producing the sums of the bottom rays. To
produce the cones, we begin by connecting all the bottom rays to _B_ and all the top rays to _T_ .
Next, we connect all the bottom rays amongst each other as for the cosmohedron, while all the top
rays are connected to each other as they are for the associahedron. Finally, the top and bottom
and connected by a very simple rule: an ( _i, j_ ) _T_ is connected to every bottom ray that contains
( _i, j_ ). The fan for the _n_ = 5 is three-dimensional but as usual we can draw a projective picture
of it two-dimensionally, and this is drawn in figure 15 (left); a combinatorial representation of the
wavefunction is shown in the top of figure 19 (at the end of the note). Again, we see that the “top”
facet is the associahedron, and the “bottom” facet is a cosmohedron. All the faces in between
are labelled by mixtures of the “top” chords - which we can think of as the _|_ _[⃗]_ _k|_ chords in the
wavefunction, and “bottom” chords - which give us nested subpolygons. Apart from the vertices
on the top associahedron facet (marked in blue), the rest of the vertices precisely correspond to
all the terms in the correlator (marked in black).
The cosmological correlahedron has a natural combinatorial definition for all _n_ . Faces are
labelled by _{C, P_ _}_, where _C_ is a collection of non-overlapping chords as for associahedra, and _P_
is a collection of non-overlapping subpolygons satisfying the russian doll rule as for cosmohedra,
except that we now include the “full perimeter” as subpolygons, and we have two full perimeters
labelled by _T_, _B_ . There are two special faces, the “top” facet where _{C_ = empty _, P_ = _P_ full _,_ top _}_
and the “bottom” facet where _{C_ = empty _, P_ = _P_ full _,_ bottom _}_ . No subpolygons, nor _P_ full _,_ bottom are
allowed to occur in the list with _P_ full _,_ top. Then, the cosmological correlahedron generalizes the


34


Figure 15: (Left) Projection of the _n_ = 5 cosmological correlahedron fan. In dashed we represent
the underlying associahedron fan with rays (3 _,_ 5), (1 _,_ 3), (1 _,_ 4) and (2 _,_ 4) marked in gray, with
the added dimension corresponding to _Et_ . Shaded in red we highlight the pentagonal facet which
is touching the base Cosmo5, and in blue the hexagonal facet which is touching the top Assoc5.
(Right) 3-dimensional projection of the Corr6 fan, coming from the underlying 3-dimensional
associahedron cone containing rays (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5). In green, we highlight a square pyramid
corresponding to a non-simple vertex of Corr6.


notion of compatibility for associahedra and cosmohedra in the obvious way:


_{C_ _[′]_ _, P_ _[′]_ _}_ is a face of _{C, P_ _}_ if _C_ _⊂_ _C_ _[′]_ and _P_ _⊂_ _P_ _[′]_ _._ (41)


At _n_ = 6 the fan is four-dimensional, but we can draw a relevant piece of it three-dimensionally,
as done in figure 15 (right). The rays are produced and connected to form cones in exactly the way
we described above: starting with the rays of the associahedron ( _i, j_ ), producing ( _i, j_ ) _B_ = ( _i, j_ )+ _B_
and ( _i, j_ ) _T_ = ( _i, j_ )+ _T_, producing the rest of the rays of the cosmohedron from the bottom rays, and
connecting all the bottom rays as for cosmohedra, the top rays are connected as for associahedra,
and every top ( _i, j_ ) _T_ ray to every bottom rays that contains ( _i, j_ ). Again remarkably, the cones
are non-overlapping, and apart from the purely top ones giving all the triangulations of the _n_ -gon,
the rest of the cones are associated with every term in the correlator.
As for cosmohedra, starting with _n_ = 6 we encounter the phenomenon of non-simple vertices for
the cosmological correlahedron. In the figure, the five rays (1 _,_ 4) _T_ together with (1 _,_ 4) _B,_ (1 _,_ 3) _B_ +
(1 _,_ 4) _B,_ (1 _,_ 5) _B_ + (1 _,_ 4) _B,_ (1 _,_ 3) _B_ + (1 _,_ 4) _B_ + (1 _,_ 5) _B_ form a square-pyramid, associated with a single
term in the correlator.
The picture for the fan of the cosmological correlahedron can clearly be extended to loops, and
an example of a three-dimensional polytope for the 1-loop bubble is shown in the bottom of figure
19 (at the end of the note).
It is also natural to cut out the cosmological correlahedron by inequalities, extending those of
associahedra and cosmohedra in the obvious way, involving “shaving parameters” _ϵT,B_ for both
the top and bottom rays. We have checked that the polytopes produced in this way have exactly
the correct combinatorics for _n_ = 6, and that they have the correct number of vertices to account
for the correlator up to _n_ = 8. In figure 16 we show the embedding of the _n_ = 5 cosmological


35


Figure 16: (Left) Embedding of the Corr5. (Right) Embedding of the (1 _,_ 4) _T_ facet of Corr6.


correlahedron as well as the embedding of the facet (1 _,_ 4) _T_ of the _n_ = 6 one. For general _n_,
we expect an interesting relation between _ϵT,B_ to produce the correct combinatorics. We leave
an exploration of this question, as well as the systematics of extracting the correlator from the
geometry, to future work.

### **11 Outlook**



This note has concerned itself simply with introducing the cosmohedra and explaining some of
the most basic physics and mathematics associated with them. As with amplituhedra and associahedra, it is remarkable to find mathematical structures that autonomously “know about” and
“discover” the wavefunction. For the associahedron itself, the magic is in the basic ABHY [5,50]
“ _X_ + _X_ _−_ _X_ _−_ _X_ = _c,_ _X_ _≥_ 0” equations that cut it out via inequalities. These equations can
be motivated and interpreted in various ways, from arising as a sort of “wave equation” in kinematic space to capturing the data of curves on surfaces in the simplest possible way. None of
these make any reference to the collection of all Feynman diagrams, and yet they give rise to an
object that unifies and discovers all diagrams. As we have seen in proceeding to cosmohedra,
we must include a further set of equations associated with partial triangulations, [�] _c⊂C_ _[X][c]_ _[≥]_ _[ϵ][C]_ [.]



we must include a further set of equations associated with partial triangulations, [�] _c⊂C_ _[X][c]_ _[≥]_ _[ϵ][C]_ [.]

The new magic is clearly in the conditions _ϵC_ + _ϵC′_ _≤_ _ϵC∪C′_ + _ϵC∩C′_, which must sometimes be
imposed as inequalities and sometimes as equalities depending on _C, C_ _[′]_ . Such conditions are
ubiquitous in the study of various polytopes associated with graphs, where they are known as
“submodularity conditions”. In our context, when the inequalities are strictly satisfied we get the
“permuto-cosmohedron” cousin of the cosmohedron. But the “perfect” object with the correct
combinatorics needs the more subtle combination of equalities and inequalities, that as we described are captured by putting _ϵC_ = [�] _P_ _[δ][P]_ [,] [summing] [over] [all] [subpolygons] [in] _[C]_ [,] [where] [the] _[δ][P]_



scribed are captured by putting _ϵC_ = [�] _P_ _[δ][P]_ [,] [summing] [over] [all] [subpolygons] [in] _[C]_ [,] [where] [the] _[δ][P]_

satisfy the strict submodularity condition _δP_ + _δP ′_ _< δP_ _∪P ′_ + _δP_ _∩P ′_ . Again, all of these expressions
treat the chords in _C_ democratically; there is no hint of any sort of russian doll structure expected
for the wavefunction. Nonetheless, they emerge, as a consequence of this extremely simple yet
obviously deep combinatorics and geometry.
There are many open questions surrounding simply understanding these objects better. Chief
amongst them is a deeper understanding of precisely how the geometry determines the wavefunction - we have given a novel prescription for extracting the wavefunction from the canonical



36


form of the cosmohedron - involving replacing the poles associated with facets with products of
pairs of poles, and keeping only terms with simple poles in the resulting expression. What is the
deeper origin and meaning of this prescription? Is there a different idea that directly gives us the
wavefunction, with multiple poles automatically removed? And is there a bigger geometry that
associates individual poles - not pairs of them - with facets, so that the usual notion of canonical
form would give the wavefunction?
On this last point, it is worth contrasting our story with that of cosmological polytopes [18],
which for single graphs _do_ give a geometry with a facet associated to every pole of the wavefunction. For single graphs, cosmohedra instead tell us to work with a different geometry - graph
associahedra - and these objects are already somewhat more interesting: a common set of poles
corresponding to the total energy and the individual internal triangles are factored out, and the
geometry only knows about the remaining non-trivial poles that differ between the russian dolls.
Consequently, even something as basic as the emergence of the amplitude as _Et_ _→_ 0 is understood
differently: in the cosmological polytope we simply go to the total energy facet and discover (at
tree-level) a simplex, which gives the amplitude. Meanwhile, as explained in detail in appendix C,
as _Et_ _→_ 0 many of the faces of the graph associahedra shrink, so the resulting objects simplifies
dramatically to a product of simplices.
Now, the cosmohedron unifies all the graph associahedra for the different diagrams into a
single object. This single object does not have a single facet for every possible singularity of the
wavefunction, but for (canonical) pairs of them. If it were possible to realize the old idea of gluing
all cosmological polytopes together into a bigger object, then we might have a facet for every
singularity. There is still no concrete idea for how to make this work, and certainly the way the
cosmohedron accomplishes this - using the geometry of the underlying associahedron as the way
to generate and combine all the diagrams - does not mesh with cosmological polytopes simply
because the dimension of associahedra and cosmological polytopes are so different. At any rate,
the unusual prescription we have found for extracting the wavefunction from the canonical form of
the cosmohedron geometry may come to be seen as either a feature or a bug, and deserves further
exploration.
In addition to better understanding cosmohedra, there are also a huge number of bigger questions left open by our investigations, and we close by highlighting two of them that seem especially
interesting and urgent. We have focused on the cosmohedron geometry associated with the “energy integrand” for the cosmological wavefunction, but recent work on “kinematic flow” [22, 29]
has shown that the full integrated objects satisfy differential equations, which for single graphs
have a natural interpretation associated with the growth of graph tubings. There are similar interpretations for the full integrated amplitude, in terms of growing subpolygons. These tubings
and subpolygons have additional decorations relative to what we have seen there, corresponding to
giving two different colorings (corresponding to _±_ signs of energies) for internal chords. It would
be fascinating to understand whether there is an extension of the cosmohedron that captures this
combinatorics.
In another direction, recall that in a precise sense, the associahedron gives us a direct path
for discovering strings starting from particle amplitudes. The deep clue to the “strings” hiding
in plain sight underlying “particles” is that, while the associahedron is primitively cut out by a
simple set of inequalities, the particular structure of these inequalities also allows us to think about
the associahedron as being built out of a Minkowski sum of simple pieces. The summands of these
Minkowski sums can be thought of Newton polytopes for certain polynomials, and this in turn
immediately generalizes particle to string amplitudes [52]. Of course history did not proceed in this
way – the Koba-Nielsen formula was written down long before the connection to the associahedron


37


was discovered. But with cosmology, we have a new opportunity. At present, there is no useful
perturbative worldsheet picture for cosmological observables (or AdS boundary correlators, which
our model of conformally coupled scalars is equally well suited to describe). But we have now
discovered a combinatorial/geometric object unifying all diagrams for cosmology. What is the
analog or extension of the Minkowski sum picture, F-polynomials, and _u_ variables in our new
setting? And what sort of “stringy” generalization of the particle wavefunctions might it describe?

### **Acknowledgements**


We thank Federico Ardilla, Paolo Benincasa, Nick Early, Pavel Galashin, Austin Joyce, Thomas
Lam, Hayden Lee, Alex Postnikov and Hugh Thomas for discussions and comments. The work
of N.A.H. is supported by the DOE (Grant No. DE-SC0009988), by the Simons Collaboration on
Celestial Holography, by the ERC universe+ synergy grant, and further support was made possible
by the Carl B. Feinberg cross-disciplinary program in innovation at the IAS. C.F. is supported by
FCT/Portugal (Grant No. 2023.01221.BD). F.V. research is funded by the European Union (ERC,
UNIVERSE PLUS, 101118787). We would also like to thank the developers of `polymake` [53].

### A Lightning review of the perturbative expansion of Ψ


In this appendix, we review the perturbative formulation of the wavefunction. The theory we
study here is a theory of colored massless scalars interacting via a cubic interaction with the
following action given in (1).
The wavefunction is then defined via the path integral as follows


                  Ψ[ _ϕ_ ( _⃗x_ )] = _D_ [ _φ_ ] _e_ _[i][S]_ [[] _[φ]_ []] _,_ (42)


where we integrate over all field configurations that satisfy the boundary condition at asymptotic
future _φ_ ( _⃗x, η_ = 0) = _ϕ_ ( _⃗x_ ), as well as the Bunch-Davies vacuum/ _iϵ_ prescription in the past [54],
_i.e._ _φ_ ( _⃗x, η_ = _−∞_ (1 _−_ _iϵ_ )) = 0. Since we have spatial momentum conservation, it is useful to go
to Fourier space, _[⃗]_ _k_, where the solution of the free equations of motion satisfying the boundary
conditions is given by:
_φ⃗k_ = _ϕ⃗ke_ _[iE][k][η]_ _,_ (43)

with _Ek_ = _|_ _[⃗]_ _k|_, so that we can read the 3-point interaction in momentum space to be:




- 0

_dηλ_ 3( _η_ ) _ϕ⃗k_ 1 _ϕ⃗k_ 2 _ϕ⃗k_ 3 _e_ _[i]_ [(] _[E][k]_ [1] [+] _[E][k]_ [2] [+] _[E][k]_ [3] [)] _[η]_ _δ_ _[d]_ ( _[⃗]_ _k_ 1 + _[⃗]_ _k_ 2 + _[⃗]_ _k_ 3) _,_ (44)
_−∞_



1

3





 
_d_ _[d]_ _ki_

_i_ =1 _,_ 2 _,_ 3



to perform the _η_ integral it is useful to Fourier represent _λ_ 3 and analyze each mode separately:




- 0

_dηλ_ 3( _ε_ ) _ϕ⃗k_ 1 _ϕ⃗k_ 2 _ϕ⃗k_ 3 _e_ _[i]_ [(] _[E][k]_ [1] [+] _[E][k]_ [2] [+] _[E][k]_ [3] [+] _[ε]_ [)] _[η]_ _δ_ _[d]_ ( _[⃗]_ _k_ 1 + _[⃗]_ _k_ 2 + _[⃗]_ _k_ 3)
_−∞_



1

3




- 
  _dε_ _d_ _[d]_ _ki_


_i_ =1 _,_ 2 _,_ 3



(45)
_,_



= _−_ _[i]_

3




- - - 1
_dε_ _i_ =1 _,_ 2 _,_ 3 _d_ _[d]_ _ki ϕ⃗k_ 1 _ϕ⃗k_ 2 _ϕ⃗k_ 3 _δ_ _[d]_ ( _[⃗]_ _k_ 1 + _[⃗]_ _k_ 2 + _[⃗]_ _k_ 3) _λ_ 3( _ϵ_ ) _Ek_ 1 + _Ek_ 2 + _Ek_ 3 + _ε_

                       - ��                        Ψ [(3)]


38


from where we can read off the bulk-to-boundary propagator _GB,∂_ ( _Ek, η_ ) = _e_ _[iE][k][η]_ as well as the
three-point wavefunction coefficient Ψ [(3)] . Here we have left _λ_ 3( _η_ ) outside Ψ [(3)] to highlight the
connection of this example to the case where the couplings are simply constants: if _λ_ 3( _η_ ) _≡_ _λ_ 3,
then we would have gotten Ψ [(3)] = 1 _/_ ( _Ek_ 1 + _Ek_ 2 + _Ek_ 3), so we can get the time-dependent case by
shifting the sum of the energies entering the 3-point vertex by _ε_ and integrating it against some
kernel, _λ_ 3( _ε_ ), which depends on the precise time dependence of the problem we want to study.
For this reason, from now on we will focus on the simpler case _λ_ 3( _η_ ) _≡_ _λ_ 3 and later come back to
the way to transform back into the most general time-dependent case.
By expanding around the free solution, _φ⃗k_ = _ϕ⃗ke_ _[iE][k][η]_ + _δφ⃗k_, we can perform the path integral
in _δφ⃗k_ . The bulk-to-bulk propagator coming from _δφk_ reads



1
_GB,B_ ( _Ek_ ; _η_ 1 _, η_ 2) =
2 _Ek_




- _e_ _[iE][k]_ [(] _[η]_ [1] _[−][η]_ [2][)] _θ_ ( _η_ 1 _−_ _η_ 2) + _e_ _[iE][k]_ [(] _[η]_ [2] _[−][η]_ [1][)] _θ_ ( _η_ 2 _−_ _η_ 1) _−_ _e_ _[iE][k]_ [(] _[η]_ [2][+] _[η]_ [1][)][�] _,_ (46)



where the first two terms are the standard Feynman propagator and the last one ensures _δφ_ _→_ 0
as _η_ 1 _,_ 2 _→_ 0.
The wavefunction can be decomposed in the wavefunction coefficients, Ψ _n_, as follows:




 - [�]
_i_ _[⃗k][i]_



_,_ (47)



_n_


 




_d_ _[d]_ _ki_ Ψ _n_ [ _[⃗]_ _ki_ ] _δ_ _[d]_ [ ��]

_i_ =1



Ψ = exp



��


_n≥_ 2



1

_n_ !



each Ψ _n_ can be represented via a diagrammatic expansion in momentum space, and these are the
object of study throughout the note.
For example at 4-points, fixing the color ordering of the external _ϕ_ ’s to be Ψ [(4)] ( _ϕ ⃗k_ 1 _, ϕ ⃗k_ 2 _, ϕ ⃗k_ 3 _, ϕ ⃗k_ 4),
we have contributions from two diagrams:




     - 0
_s_ -channel:




[�] _GB,∂_ ( _Ei, η_ ) 

_i_ =1 _,_ 2 _j_ =3 _,_



_dηdη_ _[′]_ [�]
_−∞_





_GB,∂_ ( _Ej, η_ _[′]_ ) _GB,B_ ( _E_ 1 _,_ 2; _η, η_ _[′]_ ) _,_

_j_ =3 _,_ 4




     - 0
_t_ -channel:




[�] _GB,∂_ ( _Ei, η_ ) 

_i_ =1 _,_ 4 _j_ =2 _,_



_dηdη_ _[′]_ [�]
_−∞_



(48)


_GB,∂_ ( _Ej, η_ _[′]_ ) _GB,B_ ( _E_ 2 _,_ 3; _η, η_ _[′]_ ) _,_

_j_ =2 _,_ 3



where _E_ 1 _,_ 2 = _|_ _[⃗]_ _k_ 1 + _[⃗]_ _k_ 2 _|_ = _|_ _[⃗]_ _k_ 3 + _[⃗]_ _k_ 4 _|_ and _E_ 2 _,_ 3 = _|_ _[⃗]_ _k_ 2 + _[⃗]_ _k_ 3 _|_ = _|_ _[⃗]_ _k_ 1 + _[⃗]_ _k_ 4 _|_ . Now, from each channel, since
each _GB,B_ has three terms, we would naively expect to get three terms. However, remarkably
these terms nicely cancel to give a single contribution from each channel:


1
_s_ -channel:
( _E_ 1 + _E_ 2 + _E_ 1 _,_ 2)( _E_ 3 + _E_ 4 + _E_ 1 _,_ 2)( _E_ 1 + _E_ 2 + _E_ 3 + _E_ 4) _[,]_

(49)
1
_t_ -channel:
( _E_ 2 + _E_ 3 + _E_ 2 _,_ 3)( _E_ 1 + _E_ 4 + _E_ 2 _,_ 3)( _E_ 1 + _E_ 2 + _E_ 3 + _E_ 4) _[.]_


A remarkable feature of the wavefunction is that it _contains_ the amplitude in the total energy,
_Et_, pole, _i.e._ when we extract the residue at _Et_ = [�] _i_ _[n]_ =1 _[E][i]_ [=] [0] [we] [should] [obtain] [the] [scattering]
amplitude. We can already observe this feature for this simple 4-point example, by noting that
when we have _E_ 1 + _E_ 2 + _E_ 3 + _E_ 4 = 0, we have 4-momentum conservation and in particular
( _E_ 1 + _E_ 2 + _E_ 1 _,_ 2)( _E_ 3 + _E_ 4 + _E_ 1 _,_ 2) = ( _E_ 1 + _E_ 2 + _E_ 1 _,_ 2)( _−E_ 1 _−_ _E_ 2 + _E_ 1 _,_ 2) = ( _p_ 1 + _p_ 2) [2] = _s_, where _p_ _[µ]_ _i_
stands for the 4-momentum; and similarly for the _t_ -channel contribution.
In addition, we can see that the contribution we get from each diagram corresponds is a product
of three factors: the first two correspond to the sum of the energies entering each vertex, and the


39


Figure 17: Tubings at 4 and 5 points


last one, to the sum of the energies entering the full diagram _Et_ (energies entering the tubes
depicted on the left of figure 17).
Similarly, if we do the same exercise at 5-points for the diagram depicted in figure 17 (right),
we get two terms (instead of the naive nine terms from the two _GB,B_ ):


1
_Et_ ( _E_ 1 + _E_ 2 + _E_ 1 _,_ 2)( _E_ 1 _,_ 2 + _E_ 3 + _E_ 4 _,_ 5)( _E_ 4 _,_ 5 + _E_ 4 + _E_ 5)( _E_ 1 + _E_ 2 + _E_ 3 + _E_ 4 _,_ 5)

(50)
1
+
_Et_ ( _E_ 1 + _E_ 2 + _E_ 1 _,_ 2)( _E_ 1 _,_ 2 + _E_ 3 + _E_ 4 _,_ 5)( _E_ 4 _,_ 5 + _E_ 4 + _E_ 5)( _E_ 1 _,_ 2 + _E_ 3 + _E_ 4 + _E_ 5) _[,]_


where once more we get the factors corresponding to the sums of the energies entering each
vertex, the total energy _Et_, and now a new factor corresponding to the energy entering a subgraph
( _E_ 1 + _E_ 2 + _E_ 3 + _E_ 4 _,_ 5) in the first one and ( _E_ 1 _,_ 2 + _E_ 3 + _E_ 4 + _E_ 5). Each contribution is then naturally
associated with a _tubing_ of the 5-point graph we are studying - this is a maximal collection of
subgraphs inside a graph (see right of figure 17).
For example, at 5-points the diagram considered above corresponds to the triangulation of
the pentagon containing chords (1 _,_ 3) and (1 _,_ 4). Now, let’s look back at the first term in (50),
and notice that each term appearing can be associated to a perimeter of a subpolygon inside this
momentum 5-gon (as explained in section 2):


_P_ 1 _,_ 2 _,_ 3 = _E_ 1 + _E_ 2 + _E_ 1 _,_ 2 = _|_ _[⃗]_ _k_ 1 _|_ + _|_ _[⃗]_ _k_ 2 _|_ + _|_ _[⃗]_ _k_ 1 + _[⃗]_ _k_ 2 _|,_

_P_ 1 _,_ 3 _,_ 4 = _E_ 1 _,_ 2 + _E_ 3 + _E_ 4 _,_ 5 = _|_ _[⃗]_ _k_ 1 + _[⃗]_ _k_ 2 _|_ + _|_ _[⃗]_ _k_ 3 _|_ + _|_ _[⃗]_ _k_ 4 + _[⃗]_ _k_ 5 _|,_



_P_ 1 _,_ 4 _,_ 5 = _E_ 4 + _E_ 5 + _E_ 4 _,_ 5 = _|_ _[⃗]_ _k_ 4 _|_ + _|_ _[⃗]_ _k_ 5 _|_ + _|_ _[⃗]_ _k_ 4 + _[⃗]_ _k_ 5 _|,_

_P_ 1 _,_ 2 _,_ 3 _,_ 4 = _E_ 1 + _E_ 2 + _E_ 3 + _E_ 4 _,_ 5 = _|_ _[⃗]_ _k_ 1 _|_ + _|_ _[⃗]_ _k_ 2 _|_ + _|_ _[⃗]_ _k_ 3 _|_ + _|_ _[⃗]_ _k_ 4 + _[⃗]_ _k_ 5 _|,_

_P_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 = _E_ 1 + _E_ 2 + _E_ 3 + _E_ 4 + _E_ 5 = _|_ _[⃗]_ _k_ 1 _|_ + _|_ _[⃗]_ _k_ 2 _|_ + _|_ _[⃗]_ _k_ 3 _|_ + _|_ _[⃗]_ _k_ 4 _|_ + _|_ _[⃗]_ _k_ 5 _|,_



(51)



where _Pi,...,j_ is the perimeter of subpolygon with vertices _{i, . . ., j}_ . So we have that each blob
entering the tubing is mapped to a subpolygon on the momentum _n_ -gon and a complete tubing
corresponds to a maximal collection of nested non-overlapping subpolygons, which we call a russian
doll.


40


The full wavefunction will be given purely in russian doll terms, that is, it will be a sum of terms
where each term is one collection of non-overlapping subpolygons (tubes). This is also known as
the _old-fashioned_ _perturbation_ _theory_ (OFPT) representation [18,27,28] of the wavefunction. To
understand this representation, let’s consider the time integral representation of a given graph
contributing to Ψ:







���



_e_ _[i]_ [(]  - _iv_ _∈Ev_ _[′]_ _[E][i]_ _v_ [)] _[η][v]_ ���

_v∈V_ _e∈E_



_G_ ( _Eke_ ; _ηe, ηe′_ )

_e∈E_




  - 0
_ψG_ =

_−∞_ (1 _−iϵ_ )



��

_dηv_

_v∈V_



_,_ (52)



where _V_ is the set of vertices in the graph, _E_ is the set of internal edges of the graph, _Ev_ _[′]_ [is] [the] [set]
of external states attached to the vertex _v_ (and _Eiv_ are the respective moduli of the momenta),
and _Eke_ is the momentum flowing in the edge _e_ . We now consider the action of the operator:


       ∆= _−i_ _∂ηv,_

_v∈V_


on the integrand of (52). We can start by applying integration-by-parts. The total derivative
vanishes, since the bulk-to-bulk propagators vanish at the upper boundary (see (46) when sending
_η_ 1 or _η_ 2 to zero), and on the other hand the _iϵ_ prescription (Bunch-Davies condition) ensures the
integrand vanishes in the lower boundary. Then we consider the action of ∆separately in the
external propagators, and in the product of bulk-to-bulk propagators, _G_ ( _ye_ ; _ηe, ηe′_ ). It is clear
that,





_Eiv_
_iv∈Ev_ _[′]_




       
  _e_ _[i]_ [(] _iv_ _∈Ev_ _[′]_ _[E][i]_ _v_ [)] _[η][v]_

_v∈V_











       
�� _e_ _[i]_ [(] - _iv_ _∈Ev_ _[′]_ _[E][i]_ _v_ [)] _[η][v]_


_v∈V_



_,_





 [�]

_v∈V_







∆




       
�� _e_ _[i]_ [(] - _iv_ _∈Ev_ _[′]_ _[E][i]_ _v_ [)] _[η][v]_


_v∈V_



=



where the quantity in parentheses is the total energy of _ψG_ . Then the action of ∆on the bulkto-bulk propagators is essentially only the action on the boundary term, since when acting on the
time-ordered terms, these vanish. This is true because ∆is the time-translation operator, and the
time-ordered terms are time translation invariant. Practically, one can simply see that by acting
with _∂η_ 1 + _∂η_ 2 on the time ordered terms in (46), that the derivatives of the exponentials in _η_ 1 and
_η_ 2 will cancel each other. Therefore, we can say that:



















_G_ ( _Eke_ ; _ηe, ηe′_ )

_e∈E/{e_ ˜ _}_







 [�] _e_ _[iE][k][e]_ [˜][(] _[η][e]_ [˜][+] _[η][e]_ [˜] _[′]_ [)]

_e_ ˜ _∈E_



 [�]



∆



��



_G_ ( _ye_ ; _ηe, ηe′_ )

_e∈E_



= _−_



 _._



Putting everything together, the exponentials in the expression above will be just like bulk-toboundary propagators. Then, we can write,




   _Et ψG_ ( _E_ 1 _, ..., En_ ) =



_ψG_ ˜( _E_ 1 _, ..., En, Eke, Eke_ ) _._ (53)
_e∈E_ Loop




- 
_ψGL_ ( _ELe_ ; _Eke_ ) _ψGR_ ( _ERe_ ; _Eke_ ) +
_e∈E_ Tree _e∈E_



Where in the first term we are summing over every edge that is not in a loop (the set _E_ Tree), and
_GL_ and _GR_ correspond to the subgraphs to the left and right of the edge _e_ . _ELe_ are the external
states of the left subgraph, and similarly for the right subgraph. Additionally, both _GL_ and _GR_
also have an external state with the momentum of the edge _e_ in _G_ . In the second term, we are
˜
summing over the remaining edges, which are part of a loop (the set _E_ Loop). _G_ stands for the
graph obtained by cutting the edge _e_ in the graph _G_ . It will have all the _n_ external states plus two


41


more, both with momentum of the edge _e_ . Equation (53), when applied recursively, allows us to
construct the OFPT representation of the wavefunction. In [28], the authors showed that there is
one triangulation of the dual of the cosmological polytope which yields the OFPT representation.
From (53), we have that in the sum on the right-hand side, each term will be a product of
singularities corresponding to tubes (equivalently, subpolygons) that do not overlap, either are
fully inside one another, or are disjoint. Applying this formula recursively, we can see that this
property will hold in the expansion of the different terms. Therefore, it becomes clear that we can
write the wavefunction as a sum of russian dolls.

### **B Lightning review of the ABHY associahedron**


The associahedron, Assoc _n_, is a polytope that encodes the combinatorics of triangulations of _n_ gons. Concretely, Assoc _n_ is an ( _n −_ 3)-dimensional simple polytope whose faces are associated to
partial/full triangulations of the _n−_ gon, or what is the same, collections of non-overlapping chords
of the _n_ -gon. The codimension-1 faces are associated to partial triangulations with a single chord,
codimension 2 faces with those with two chords, and so on until we reach the vertices, which are
labelled by ( _n −_ 3) non-overlapping chords specifying a full triangulation.
If we denote a collection of non-overlapping chords by _C_, then the associahedron is the polytope
whose face structure reflects the combinatorics of compatible chords, which can be stated as the
fundamental property that:


_C_ _[′]_ is a face of _C_ if _C_ _⊂C_ _[′]_ .


One simple way of constructing the associahedron combinatorially is via _mutations_ . This is
if we start on a given vertex of the associahedron, corresponding to a full triangulation of the
_n_ -gon, we can generate the vertices that are connected to it by performing mutations: given the
collection of chords in a triangulation, each chord is then a diagonal of a square defined by the
boundary edges and the remaining chords on the triangulation. A mutation flips one of the chords
to the other diagonal of the square in which it is contained. Since a triangulation contains _n −_ 3
chords, starting at a given vertex we can mutate in _n −_ 3 different ways, which means that at any
vertex of our polytope ( _n −_ 3) edges meet, which tells us the polytope is _simple_ . Following this
procedure, we can generate the full polytope, and we further conclude that any two vertices are
connected via an edge if and only if their triangulations are related by a mutation.
For example, suppose we do this exercise for _n_ = 4. In that case, there are only two triangulations and the geometry is one-dimensional - the Assoc4 is a line interval with two vertices, one
at each boundary of the interval, labeling the two possible triangulations. In this case it is trivial,
but indeed we see a mutation relates the two triangulations.
At _n_ = 5, we should find a two-dimensional geometry, which ends up being a pentagon as
depicted in the left of figure 3. We see that each edge is associated with partial triangulations
with a single chord, and the vertices are labeling all the possible 5 triangulations of the pentagon.
Similarly, for _n_ = 6, the Assoc6 is a three-dimensional polytope, with 9 codimension one facets

- one associated to each chord of the hexagon – 21 codimension-2 facets – associated to collections
of two non-overlapping chords - and finally 14 vertices, each labeling one triangulation of the
hexagon (see figure 1, left).
One remarkable property of the associahedron is the factorization structure associated with its
boundaries - the boundaries of associahedra are given by products of lower-point associahedra.
This feature stands as the geometric avatar of factorization of tree-level scalar amplitudes into


42


products of lower-point amplitudes. For example, if we look at the 5-point associahedron (figure
5, left) then we see that each boundary - the edges - are naturally associated with a partial
triangle with a single chord which divides the pentagon into a square and a triangle. Indeed, the
boundary is then given by the product of the lower-point associahedron associated to the smaller
polygons appearing in the partial triangulation. In this case, the 3-point associahedron is a point
and the 4-point is the line segment described above, so we get simply a line interval. Similarly,
at 6-points, we see that the polytope has 6 pentagonal facets and 3 square facets. The first six,
correspond to partial triangulations including a single chord ( _i, i_ + 2) which divides the hexagon
into a pentagon and a triangle, therefore we expect to get Assoc5 _×_ Assoc3, which is indeed what
we have since these facets are pentagons. As for the square facets, these correspond to partial
triangulations with a single chord of the type ( _i, i_ +3) which divides the hexagon into two squares,
and therefore we get that these facets are Assoc4 _×_ Assoc4, which is precisely a square.
We stress that is not at all obvious a priori that the combinatorics of partial triangulations
can be captured by a polytope. It’s existence, and it’s factorization properties on facets are most
naturally understood from a particular realization in terms of a simple set of inequalities we will
review in a moment.
Now that we have understood how the combinatorial information associated to cubic tree
graphs is organized in this polytope, and in particular how its boundary structure encodes the
basic factorization features of amplitudes, let’s see how we can connect these physical observables
to this geometry.
In a theory of colored scalars interacting via cubic interactions  - Tr( _ϕ_ [3] ) theory  - we can write
the amplitudes perturbatively over sums of cubic diagrams. Namely at leading order, once we
fix an ordering for the external particles, say _e.g._ the standard ordering (1 _,_ 2 _, · · ·_ _, n −_ 1 _, n_ ), we
get contributions from all the possible tree-level planar Feynman diagrams - which are precisely
dual to triangulations of the _n_ -gon. In particular, if we associate to each edge of the _n_ -gon a
momentum of the particle in the scattering process, _p_ _[µ]_ 1 _[, p][µ]_ 2 _[,][ · · ·]_ _[, p][µ]_ _n_ [,] [then] [given] [a] [triangulation] [we]
have that the length [2] of the chords entering in the triangulation precisely give us the momentum
square flowing through the propagators in the dual cubic graph. Let’s denote the (length) [2] of a
chord going from vertex _i_ to vertex _j_ by _Xi,j_ then we have:


_Xi,j_ = ( _pi_ + _pi_ +1 + _· · ·_ + _pj−_ 1) [2] _,_ (54)


where we have _Xi,j_ = _Xj,i_ and _Xi,i_ +1 = 0 since we are considering our particles to be massless and
therefore we have _p_ [2] _i_ [=] [0.] [Therefore,] [we] [can] [write] [Tr(] _[ϕ]_ [3][)] [amplitudes] [at] [tree-level] [as] [a] [sum] [over]
all possible cubic Feynman diagrams - all possible triangulations of the _n_ -gon - where for each
diagram we have a factor of one over the product of the _Xi,j_ corresponding to the chords entering
in the triangulation:



_An_ ( _Xi,j_ ) = 

triang. _T_






_Xi,j_ _∈T_



1
_._ (55)
_Xi,j_



This way of writing the amplitude makes manifest that it is a function exclusively of the _Xi,j_ ’s
which are usually called the planar variables - as they correspond to the invariants associated to
momentum flowing through propagators of planar tree diagrams. Note, however, that the planar
variables are _not_ all the possible Lorentz invariants dot product of momentum one can consider,
for example we also have the dot products _pi_ _· pj_ with _i_ and _j_ non-adjacent. In particular, at
_n_ -points we have _n_ chosen 2 dot products of momenta, but due to momentum conservation only
_n_ ( _n −_ 3) _/_ 2 of these are actually independent. Quite nicely _n_ ( _n −_ 3) _/_ 2, is precisely the number of
_Xi,j_ we have for an _n_ -gon, and therefore we have that the planar variables form a _basis of kinematic_


43


_space_, where momentum conservation is automatically implemented by the fact that they lived in
a _closed_ momentum polygon.
This means that the non-planar variables  - corresponding to dot products of non-adjacent
particles - can be written in terms of the planar ones. Let us call the non-planar invariants by
_ci,j_ = _−_ 2 _pi · pj_ with _i, j_ not adjacent. Then we have:


_ci,j_ = _Xi,j_ + _Xi_ +1 _,j_ +1 _−_ _Xi,j_ +1 _−_ _Xi_ +1 _,j._ (56)


Now that we have defined the kinematic space the amplitude lives in as well as given a precise
definition of the amplitude in this space (55), we can proceed to understand how to connect this
object to the geometry of the associahedron. The first step is to embed the associahedron in
kinematic space — where the amplitude is defined — this is we want to define a set of inequalities
in _Xi,j_ space that carve out this polytope. This embedding was introduced in [5] and we will
summarize it here. As explained above, each facet of this geometry is associated with a partial
triangulation with a single chord, and therefore is naturally associated with a given _Xi,j_ . Therefore,
to each facet we associate the inequality:


_Xi,j_ _≥_ 0 _._ (57)


So we have that all _X_ ’s are positive inside the polytope and vanish in the respective facets.
However, as explained earlier the Assoc _n_ is an _n−_ 3-dimensional object, and the current inequalities
naively define a cone in an _n_ ( _n −_ 3) _/_ 2 dimensional space. So in order to bring it to the correct dimension we intersect this cone with the “ABHY” plane defined as follows: Pick a triangulation say
_{X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, · · ·_ _, X_ 1 _,n−_ 1 _}_ and consider the kinematic basis containing the _X_ ’s in the triangulation as
well as the collection of non-planar variables _C_ = _{c_ 1 _,_ 3 _, c_ 1 _,_ 4 _, · · ·_ _, c_ 1 _,n−_ 1 _, c_ 2 _,_ 4 _, c_ 2 _,_ 5 _, · · ·_ _, c_ 2 _,n−_ 1 _, · · · c_ 3 _,_ 5 _,_

_· · ·_ _, cn−_ 3 _,n−_ 1 _}_ which contains exactly _n_ ( _n −_ 3) _/_ 2 _−_ ( _n −_ 3) _c_ ’s. Then since this forms a basis we
can write all _X_ ’s in terms of the _X_ ’s in the chosen triangulation and the _ci,j_ ’s in this collection. If
we fix the non-planar variables in _C_ to be _positive_ then (57) defines an _n_ _−_ 3 dimensional geometry
in the space spanned by _X_ 1 _,_ 3 _, X_ 1 _,_ 4 _, · · ·_ _, X_ 1 _,n−_ 1 which is precisely the associahedron.
Given this embedding, the amplitude is given by the canonical form of this polytope. There
are various motivations for the ABHY inequalities, from a “causal diamond” picture [50] in kinematic space to recording the data of curves on surfaces [6]. It is striking that none of these refer
to summing over all diagrams. The connection with the usual Feynman diagrams arises from a
particular way of computing the canonical form of the associahedron. Indeed for any simple polytope, there is a natural triangulation, taking the inverse product of the facet inequalities meeting
at each vertex and summing over all vertices, corresponding to an especially obvious triangulation
of the _dual_ polytope. Since each vertex of the associahedron corresponds to a complete triangulation, this expression for the canonical form of a simple polytope turns into the Feynman diagram
expansion.

### **C Graph associahedra from cosmohedra**


The early connection between positive geometry and the cosmological wavefunction for a single
graph was through cosmological polytopes [18]. In the context of cosmohedra, we have instead seen
that the geometry of single graphs are instead given by graph associahedra. We have already given
a combinatorial description of these graph associahedra as part of the build-up to motivating the
cosmohedron itself. In this appendix, we will describe how to cut out the graph associahedra by


44


inequalities, simply by specializing the cosmohedron to its graph-associahedron facets. Amongst
other things, this will allow us to describe the simple relationship between graph associahedra and
cosmological polytopes.
Note that unlike for the full cosmohedra  - where the relationship between the wavefunction
and the canonical form of the geometry is the interesting “non-linear” one described in the text

- for single graphs the story is entirely straightforward. We can associate a dual graph _G_ with
a Feynman diagram/triangulation _T_ in the usual way. We associate energy variables _xv_ with the
vertices and _ye_ with the edges; as we will see, we can think of the graph associahedron as living
in _y_ space. After factoring out the total energy _Et_, and individual triangle perimeters _tv_, the
wavefunction for _G_ is simply given by the canonical form of the graph associahedron, _AG_ :



Ψ _G_ = [1]

_Et_






_v_



1
_tv_ Ω _AG_ ( _y_ ; _tv, Et_ ) _,_ (58)



whereas we will see, _Et, tv_ appear as parameters cutting out the graph associahedron in _y_ space.
The graph associahedra (and certain degenerations we will describe when writing all perimeters
in terms of standard ( _xv, ye_ ) energy variables) also give a novel understanding of the emergence
of the amplitude on the scattering facet at tree-level, and also explain some remarkable features
of wavefunction residues that had resisted a transparent understanding to date.

#### **C.1 Inequalities for the graph associahedron**



The graph associahedra are particular facets of cosmohedra, corresponding to complete triangulations _T_ of the _n_ -gon. For a given _T_, we can associate a dual graph _G_ in the usual way. This facet
of the cosmohedron is associated with the inequality _XI_ _≥_ [�] _δTi_, where _XI_ are all the chords

[�]
in the triangulation and _δTi_ are associated with each triangle of the triangulation (as given in (20)
and (24)). By going on this facet, we are saturating this to the equality

      -       



 _XI_ =

_I_ _i_



_δTi._ (59)

_i_



In terms of the dual graph _G_, we can think of _δTi_ as associated with a small circle surrounding
the _i_ -th vertex of _G_ .
Obviously, the other facets of the cosmohedron that meet the one associated with _T_ must
correspond to partial triangulations that are coarsenings of _T_ . These will become facets of the
graph associahedron for _T_, so the inequalities cutting out the graph associahedron are all of the
form [�] _J_ _[X][J]_ _[≥]_ [�] _[δ][p]_ [,] [with] _[J]_ [depending] [on] [the] [partial] [triangulation] [we’re] [considering.] [We] [can]



form [�] _J_ _[X][J]_ _[≥]_ [�] _[δ][p]_ [,] [with] _[J]_ [depending] [on] [the] [partial] [triangulation] [we’re] [considering.] [We] [can]

denote these inequalities easily in the language of the tubes. The partial triangulation gives a
collection of non-overlapping sub-polygons _p_, which can be denoted on _G_ by a collection of nonoverlapping tubes we will also label by _p_ .
Then, [�] _J_ _[X][J]_ [is the sum over all the edges of] _[ G]_ [ that are cut by the tubes.] [Clearly, the smallest]



Then, [�] _J_ _[X][J]_ [is the sum over all the edges of] _[ G]_ [ that are cut by the tubes.] [Clearly, the smallest]

tubes, which encircle a single vertex, corresponding to triangle sub-polygons, are special. We can
label our partial triangulation by specifying a collection of larger (not triangle) tubes, _P_, and
having done this, understanding that the vertices not encircled by tubes, are encircled with small
ones. The inequalities are then

      -      -      



 - - 
_Xe_ _≥_ _δP_ + _δt,_ (60)

_e_ not in _P_



45


where the sum is over the edges _e_ that are not contained in the interior of any big tube in _P_, and
_t_ are the tubes encircling the single vertices not encircled by the set of big tubes _P_ .
But it is now trivial to see that the inequalities associated with more than one of these larger
tube are all redundant, following from those for single tubes. Consider the simple example of the
triangulation _{_ (1 _,_ 3) _,_ (1 _,_ 4) _,_ (1 _,_ 5) _}_ for _n_ = 6. We are working on the support of


_X_ 1 _,_ 3 + _X_ 1 _,_ 4 + _X_ 1 _,_ 5 = _δ_ 1 _,_ 2 _,_ 3 + _δ_ 1 _,_ 3 _,_ 4 + _δ_ 1 _,_ 4 _,_ 5 _._ (61)


The partial triangulations _{_ (1 _,_ 3) _,_ (1 _,_ 4) _}_ is associated with a single tube – corresponding to square
(1 _,_ 4 _,_ 5 _,_ 6)–, as is that for (14 _,_ 15), and the inequalities are


_X_ 1 _,_ 3 + _X_ 1 _,_ 4 _≥_ _δ_ 1 _,_ 2 _,_ 3 + _δ_ 1 _,_ 3 _,_ 4 + _δ_ 1 _,_ 4 _,_ 5 _,_ 6 _,_ _X_ 1 _,_ 4 + _X_ 1 _,_ 5 _≥_ _δ_ 1 _,_ 2 _,_ 3 _,_ 4 + _δ_ 1 _,_ 4 _,_ 5 + _δ_ 1 _,_ 5 _,_ 6 _._ (62)


But adding these inequalities and using (61) we have that


_X_ 1 _,_ 3 + _X_ 1 _,_ 4 + _X_ 1 _,_ 4 + _X_ 1 _,_ 5 _≥_ _δ_ 1 _,_ 2 _,_ 3 + _δ_ 1 _,_ 3 _,_ 4 + _δ_ 1 _,_ 4 _,_ 5 _,_ 6 + _δ_ 1 _,_ 2 _,_ 3 _,_ 4 + _δ_ 1 _,_ 4 _,_ 5 + _δ_ 1 _,_ 5 _,_ 6
(63)
_⇒_ _X_ 1 _,_ 4 _≥_ _δ_ 1 _,_ 2 _,_ 3 _,_ 4 + _δ_ 1 _,_ 4 _,_ 5 _,_ 6 _,_



which is the two-tube inequality associated with the partial triangulation _{_ (1 _,_ 4) _}_ . This obviously
extends to any number of tubes: on the support of [�] _J_ _[X][J]_ [=] [�] _i_ _[δ][T]_ _i_ [,] [the] [sum] [of] [the] [inequalities]



_J_ _[X][J]_ [=] [�]



extends to any number of tubes: on the support of [�] _J_ _[X][J]_ [=] [�] _i_ _[δ][T]_ _i_ [,] [the] [sum] [of] [the] [inequalities]

for single tubes implies the inequality for multi-tubes, and so these are redundant.
We can naturally define the variables for the graph without referring to the underlying triangulation. Thus, we associate variables _Xe_ with the edges of _G_, and constants _δP_ with single tubes
_P_ . The graph associahedron is then cut out by the inequalities:

      -      



 - 
_Xe_ _≥_ _δP_ +

_e_ not in _P_ _v_ not in



_δv,_ (64)

_v_ not in _P_



where _δv_ is associated to the small encircling of vertex _v_ . The _δP_ satisfy our ubiquitous inequalities


_δP_ + _δP ′_ _< δP_ _∪P ′_ + _δP_ _∩P ′_ (65)


where, as for the full cosmohedron, _δ_ all = 0.
It is amusing that the graph associahedron for linear chains are simply associahedra; in this
case, all the myriad properties of Tr( _ϕ_ [3] ) amplitudes following from the connection with the associahedron are inherited by the wavefunction for these single graphs. Indeed, the Minkowski sum
decomposition and corresponding stringy integrals exist for all graph associahedra, so cousins of
full _stringy_ Tr( _ϕ_ [3] ) amplitudes exist, associated with single graphs for the wavefunction! This gives
an interesting entry-point into possible stringy formulations for cosmological wavefunctions we
leave to future work.

#### **C.2 Relation to cosmological polytopes**


We now discuss the connection between graph associahedra and the cosmological polytope. As a
natural entry into the discussion, we note again that the natural variables we are using to describe
the wavefunction are _perimeters_, thought of as independent variables. This is an extension of
the usual kinematic variables, in the general spirit of the extensions of kinematics for amplitudes
given by curves on surfaces [46]. For a single graph, this is equivalent to working with independent
variables _p_ associated to every tube. But to compare with the standard wavefunction and with


46


cosmological polytopes, we work with the standard energy variables. As it is well-known for a
single graph, these are conventionally denoted by variables _xv_ for the sum of the energies entering
each vertex and _ye_ for the energy of each internal edge of _G_ . Of course, the _x, y_ variables determine
the _p_ associated with every tube, via



_Pp_ = 



- 
_xv_ +

_v_ in _p_ _e_ entering



_ye,_ (66)

_e_ entering _p_



the sum over the energies of the vertices contained inside _p_ together with the external edges
entering _p_ - the familiar energy pole associated with the tube _p_ . Note that this enforces certain
equalities between the _Pp_ ’s:
_Pp_ + _Pp′_ = _Pp∪p′_ + _Pp∩p′._ (67)


In fact, it is easy to see that we can work backwards  - imposing these natural equalities on
the perimeters _Pp_ implies that they can be expressed in terms of _xv, ye_ variables associated with
the graph.
Let us now discuss the cosmological polytope for a graph with _V_ vertices and _E_ edges. It is
usually described as a projective polytope in _E_ + _V_ _−_ 1 dimensions; of course this is equivalently
thought of as a cone over this polytope in _E_ + _V_ dimensions. This cone is cut out by the simple
inequalities, for every tube _p_



_Pp_ _≥_ 0 _,_ or 



- 
_xv_ +

_v_ in _p_ _e_ entering



_ye_ _≥_ 0 _._ (68)

_e_ entering _p_



Now, in the story of the graph associahedron, we are factoring out the total-energy singularity,
as well as those associated with the small tubes encircling each vertex. Thus, it is natural to expect
that the relationship with the graph associahedron and the cosmological polytope is revealed when
we slice the cosmological polytope on the plane

     -     



    _xv_ = _Et,_ _xv_ +

_v_ _e_



_ye_ = _tv,_ (69)

_e_ connected to _v_



where we hold _Et, tv_ _>_ 0 as constants.
Indeed, as we now see, this slice of the cosmological polytope is very closely related to the
graph associahedron. For instance, for the simplest cases of the 2-dimensional graph associahedra,
corresponding to the 4-site chain and star graphs (shown in figure 3, right), this slice of the
cosmological polytope gives us precisely the familiar pentagon and hexagon. But more generally,
it is obvious that this sliced cosmological polytope cannot be precisely the same as the graph
associahedron - the graph associahedron knows about the general perimeters, not about the
specialization associated with working with _x_ ’s and _y_ ’s.
There is a beautiful resolution of this discrepancy. The sliced cosmological polytope is obtained
by a _degeneration_ of the graph associahedron, when the _δP_ occurring in the inequalities cutting
out the graph associahedron saturate most of the inequalities they satisfy. Indeed, we have that

  - _δP_ + _δP ′_ _< δP_ _∪P ′_ + _δP_ _∩P ′,_ if _P_ _∩_ _P_ _[′]_ is a single vertex or _P_ _∪_ _P_ _[′]_ is everything _,_
(70)
_δP_ + _δP ′_ = _δP_ _∪P ′_ + _δP_ _∩P ′,_ otherwise _._


Imposing these equalities has the effect of shrinking some of the faces of the graph associahedra

- the graph associahedra are all simple polytopes, but the sliced cosmological polytopes are not.


47


For instance, for the case of the 5 site chain where the graph associahedron is the usual threedimensional associahedron (see figure 4, right), while the sliced cosmological polytope still has 9
faces, but only has 12 vertices and 19 edges instead of the usual 14 vertices and 21 edges; two
of the edges of the usual associahedron are then contracted to a point in the sliced cosmological
polytope.
It is straightforward to establish the connection between the sliced cosmological polytope and
this degeneration of the graph associahedron. We simply take the graph, and solve for the _xv_
variables by setting all the perimeters associated with the small tubes encircling the vertices to
_tv_ . We are left only with _ye_ variables. These satisfy a single equality (from the _Et_ equation in
(69)), and the rest of the inequalities coming from (68). Then the inequality for any large tube _P_
becomes

      -      



- 
(2 _ye_ ) _≥_

_e_ not in _P_ _v_ not in



_tv −_ _Et._ (71)

_v_ not in _P_



If we identify 2 _ye_ _≡_ _Xe_, these are just the inequalities for cutting out the graph associahedron
(64), but with a special choice for the RHS of the inequality. Comparing with the RHS of the _P_
inequality for the graph associahedron _δP_ + [�] _v_ not in _P_ _[δ][v]_ [we] [have] [that]


       _δP_ = ( _tv −_ _δv_ ) _−_ _Et._ (72)


_v_ not in _P_



Further matching [�]



_e_ [2] _[y][e]_ [=] [�]



_v_ _[t][v]_ _[−]_ _[E][t]_ [(from] [(69))] [with] [�]



_e_ _[X][e]_ [=] [�]



Further matching [�] _e_ [2] _[y][e]_ [=] [�] _v_ _[t][v]_ _[−]_ _[E][t]_ [(from] [(69))] [with] [�] _e_ _[X][e]_ [=] [�] _v_ _[δ][v]_ [(from] [the] [facet] [defined]

by the graph associahedron in the cosmohedron (59)) lets us identify

      


( _tv −_ _δv_ ) = _Et._ (73)

_v_



It is then very easy to see that the choice for _δP_ in (72) satisfies the inequalities and equalities
given for the degenerated graph associahedron we defined above (70).

#### C.3 Et and all-vertex singularities


It is a beautiful fact that the residue on the _Et_ _→_ 0 pole of the wavefunction gives the scattering
amplitude. It is important to emphasize that this fact crucially depends on using the usual
kinematics for the wavefunction, and does not arise when treating the perimeters as independent
variables. Indeed, in the russian doll picture, _every_ term has an _Et_ pole! So there is no special
simplification to the wavefunction when _Et_ _→_ 0; for instance, at large _n_ there are still the same
number of factorially many terms as there are for the full wavefunction. And yet, when we express
all the perimeters in terms of ( _xv, ye_ )’s, there is a vast simplification – the amplitude appearing as
the residue on the pole is a single term!
This is clearly an important phenomenon, and it is interesting to understand it thoroughly. Of
course the time-integral representation for the wavefunction makes this fact rather obvious, but
this representation has many other defects, amongst other things being riddled with spurious 1 _/ye_
poles that only cancel in the full sum. The russian doll picture only has physical poles term-byterm, but as we have just said, does not make the appearance of the amplitude on the _Et_ _→_ 0
pole manifest.
The cosmological polytope gives us a very satisfying understanding of what happens as _Et_ _→_ 0.
Starting from the defining representation as a convex hull of points, it is easy to see that (at treelevel) there are very few vertices lying on the scattering facet where _Et_ _→_ 0, and that this facet


48


is in fact a simplex; since the canonical form of a simplex is trivially given by the product of its
facet inequalities this makes the emergence of the amplitude obvious.
Instead, _Et_ does not appear as a facet of the graph associahedron, nor of its degenerated cousin
enforcing working with ( _xv, ye_ ) variables; _Et_ has been “factored out” and only affects the polytope
through its role in defining the inequalities. It is therefore interesting to understand how the
scattering amplitude arises in this language.
There is yet another striking feature of the wavefunction for single graphs, which has been
observed since the earliest literature on the subject, but which has resisted a simple understanding.
Namely, if we take the residue of the wavefunction in all the vertex variables, the result is extremely
simple, given by the product [�] _e_ 21 _ye_ [.] [The] [residue] [for] [individual] [terms] [in] [the] [russian] [doll] [sum] [are]

in general much more complicated, but the full sum simplifies dramatically.
The degenerated graph associahedra beautifully explain both the appearance of the amplitude
as _Et_ _→_ 0 as well as the simplicity of the total vertex residue, in a uniform way. It is easy
to see that in both cases, the relevant limit ends up greatly simplifying the degenerated graph
associahedron. When the vertex residues are taken, the degenerated graph associahedron turns
into a simplex. Instead as _Et_ _→_ 0, the graph associahedron degenerates to a product of simplices,
such that the full canonical form is again a single term. In both cases, when the canonical form is
multiplied by the appropriate prefactors factored out in Ψ _G_, we get precisely the correct result.



**Total** **Vertex** **Residue** Let’s first see what happens on the total-vertex residue. This is taking
the residue on all _tv_ _→_ 0 in Ψ _G_, that leaves us with the canonical form for the degenerated
graph associahedron when all the _tv_ _→_ 0. Using that [�] _e_ [(2] _[y][e]_ [)] [=] [�] _[t][v]_ _[−]_ _[E][t]_ [(from] [(69)),] [we] [can]



graph associahedron when all the _tv_ _→_ 0. Using that [�] _e_ [(2] _[y][e]_ [)] [=] [�] _[t][v]_ _[−]_ _[E][t]_ [(from] [(69)),] [we] [can]

equivalently write the inequalities for any tube _P_ (71) as

    -     - _tv→_ 0     



- _tv→_ 0 
_tv_ _−−−→_

_v_ in _P_ _e_ in _P_




- 
(2 _ye_ ) _≤_

_e_ in _P_ _v_ in _P_



(2 _ye_ ) _≤_ 0 _,_ (74)

_e_ in _P_



which greatly simplify when setting all _tv_ _→_ 0. Now we always have tubes _P_ enclosing a single edge
_e_, and for these the inequality is simply (2 _ye_ ) _≤_ 0. But these then imply all the other inequalities!
Thus, as the _tv_ _→_ 0, the degenerated graph associahedron, _A_ [˜] _G_, turns into the simplex cut out by
(2 _ye_ ) _≤_ 0, with (2 _ye_ ) = _−Et_ . The canonical form of this simplex is precisely:

[�]



_e_




  Ω _A_ ˜ _G_ [=] _[ E][t][ ×]_

_e_



1
_⇒_ Ψ _G_ = [1]
2 _ye_ _E_



_×_ Ω _A_ ˜ _G_ [=]  _Et_



1
_,_ (75)
2 _ye_



so when we multiply by the prefactor in Ψ _G_ we get precisely the simple residue we are looking to
explain.


_Et_ **residue** The emergence of the amplitude on the _Et_ _→_ 0 facet is more interesting. The first
observation is simple: when we set _Et_ _→_ 0, only the inequalities for a small subset of tubes are
relevant, as they imply all the remaining. Given any tree-graph, for a given edge _e_, there are
two special tubes, the “left” and “right” tubes, _Le, Re_, which cross the edge and encircle all the
vertices to one or other part of the full tree graph. Note that some of these _L, R_, which correspond
to circling just one vertex at the very end of the graph, are part of the circlings that have been
factored out, and are not facets of the polytope - corresponding to triangles in the subpolygon
picture. These are obviously important for the emergence of the amplitude - on the support of
_Et_ = 0, the Lorentz-invariant propagator is simply the product _LeRe_ . It is very easy to see that in
general, any tube _P_ is given as a positive sum over _L/R_ tubes, minus some multiple of _Et_ . Thus,


49


when _Et_ = 0, any other tube is a positive sum of ( _L, R_ )’s, and hence all the other inequalities
((68), for _P_ not a _L, R_ type tube) are redundant.
But there are still many ( _L, R_ )’s, and it is not trivially obvious that the degenerated graph
associahedron has gotten much “simpler” as _Et_ _→_ 0. But it has! Indeed, we will now see that the
canonical form of the degenerated graph associahedron as _Et_ _→_ 0, _A_ _[E]_ _G_ _[t]_ [,] [is]




   Ω _AEtG_ [=] 



 
internal _v_ _[t][v]_




internal _[L]_ [ �]



(76)
internal _[R,]_



where internal _v_ stands for every vertex in the graph that is connected to more than one internal
edge, and internal _L/R_ stand for the _L, R_ tubings that enclose more than a single vertex. The
numerator of this form kills the factors of 1 _/t_ int factored out in front on Ψ, for all the _tv_ associated
to internal vertices, while the denominator combines with the 1 _/t_ ext factors, so that for each
internal edge we get a factor _LeRe_, which precisely turns in to the Lorentz-invariant dot product
of the 4-momentum flowing through that edge, to giving us the amplitude.
It remains to establish this simple expression for the canonical form. The canonical form for
any polytope is given by the product of all the poles corresponding to the polytope facets, with a
numerator factor _N_, which enforces the fact that the form only has unit residues on the vertices of
the polytope. For a simplex, this numerator factor is just a constant, depending on the constants
occurring in the inequalities cutting out the facets of the polytope. For a general complicated
polytope, the numerator is a complicated function. But for products of simplices, the numerator
is similarly just a constant. We will now see that the residue of the form on all possible vertices
of the degenerated associahedron is so simple that we can determine the residue to be precisely
the one shown above, showing both that the polytope has turned into a product of simplices and
giving us the amplitude as desired.
We will begin by representing any _Le, Re_ tube by placing an arrow on the edge _e_, pointing left
or right, respectively (see figure 18, top left). Note for the case of an edge touching an outside
vertex of the graph, we don’t include the arrow pointing towards the vertex, since these are the
small tubes that have been factored out.
We would like to compute the residues when we set ( _E_ _−_ 1) of the _L/R_ tubes to zero. It is useful
to represent this choice of ( _E −_ 1) tubes by putting ( _E −_ 1) arrows on the graph. It is then easy
to see that any “arrowing” of the graph that avoids having vertices with all incoming arrows gives
a non-zero residue. For the cases where some vertices have all incoming arrows, it is impossible to
find a solution for the _y_ ’s, and so the residue vanishes. For the “legal” configurations, the ( _E −_ 1)
equalities fully localize the _y_ ’s, and it is easy to read off the value of _ye_ for any edge _e_ touching
vertices _v, v_ _[′]_ . If _e_ does not have any arrows, then _ye_ = _tv_ + _t_ _[′]_ _v_ [.] [If] [there] [is] [an] [arrow] [pointing] [from]
_v_ to _v_ _[′]_, then 2 _ye_ = _tv_ . Finally, if there are two arrows pointing in opposite directions on _e_, then
_ye_ = 0. This allows us to compute the value of any _other L/R_ tube (that is not among the ones we
took residues on to begin with) in a simple way. Take this _L/R_ tube, and represent it by drawing
one more _E_ ’th arrow on the graph, along the edge associated to the _L/R_ tube. Then the vertex
the arrow points to, call it _v∗_, will now have all incoming arrows (see figure 18, left bottom, where
we have added a red/green extra arrow). The value of this _L/R_ tube (associated to this _E_ th
arrow), on the support of the residue solution defined by the first ( _E −_ 1) tubes, is simply given
by _tv∗_ !


50


3


t2+t4


t2



1



2



t2+t4






|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
||ET||ET|
|||||


|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||



Figure 18: Left top: an example of an “arrowing” of a tree-graph with ( _E −_ 1) arrows. The graph
has seven edges, and we have placed six arrows on the edges, with no arrow pointing towards a
boundary vertex. Left bottom: if we place any seventh arrow on the graph, there is a unique
vertex with all incoming arrows. Examples are highlighted for adding the red arrow with the
circled red with all incoming arrows, and the same with green arrow and circled vertex. Right:
the (degenerated) graph associahedron for the Mercedes-Benz graph is a hexagon. But when
_Et_ _→_ 0, it further degenerates into a triangle; this is the mechanism for the emergence of the
amplitude on the _Et_ _→_ 0 pole.



In this way we see that remarkably,

 






  
_R_  = _t_ internal _,_ (77)



all internal




 


all _L_ not in the
( _E −_ 1) residue



_L_











 


all _R_ not in the
( _E −_ 1) residue



and this is completely independent of which ( _E_ _−_ 1) set we pick. Thus, simply choosing this
product for the numerator correctly normalizes the canonical form, leading to the correct final
result to get the amplitude as the residue when _Et_ _→_ 0.
In figure 18 (right), we show what happens when we send _Et_ _→_ 0 for the case of the graph
associahedron of the star graph at 6-points in the (2 _y_ 1) _,_ (2 _y_ 2) plane - the hexagon becomes a
triangle. The canonical form for this triangle is



_t_ 4 1
Ω _[E]_ triangle _[t]_ [=] _⇒_ Ψ _[E]_ triangle _[t]_ [=] _×_ Ω _[E]_ triangle _[t]_ [=]
_R_ 1 _R_ 2 _R_ 3 _L_ 1 _L_ 2 _L_ 3 _t_ 4



3



_i_ =1



1
(78)
_LiRi_



where _R_ 1 = _x_ 2 + _x_ 3 + _y_ 1 _,_ 4, _R_ 2 = _x_ 1 + _x_ 3 + _y_ 2 _,_ 4, _R_ 3 = _x_ 1 + _x_ 2 + _y_ 3 _,_ 4 and _L_ 1 = _x_ 1 + _y_ 1 _,_ 4, _L_ 2 = _x_ 2 + _y_ 2 _,_ 4,
_R_ 3 = _x_ 3 + _y_ 3 _,_ 4 (where, since _Et_ = 0, we have _x_ 1 + _x_ 2 + _x_ 3 = 0). The factor of _t_ 4 in the numerator
is there for unit leading singularities. This _t_ 4 in the numerator cancels the 1 _/t_ 4 factored in front
for the wavefunction, leaving us with the amplitude.

### **References**


[1] Nima Arkani-Hamed and Jaroslav Trnka. The Amplituhedron. _JHEP_, 10:030, 2014.


51


[2] Nima Arkani-Hamed, Jacob L. Bourjaily, Freddy Cachazo, Alexander B. Goncharov, Alexander Postnikov, and Jaroslav Trnka. _Grassmannian_ _Geometry_ _of_ _Scattering_ _Amplitudes_ . Cambridge University Press, 4 2016.


[3] Nima Arkani-Hamed, Freddy Cachazo, Clifford Cheung, and Jared Kaplan. A Duality For
The S Matrix. _JHEP_, 03:020, 2010.


[4] Edward Witten. Perturbative gauge theory as a string theory in twistor space. _Commun._
_Math._ _Phys._, 252:189–258, 2004.


[5] Nima Arkani-Hamed, Yuntao Bai, Song He, and Gongwang Yan. Scattering Forms and the
Positive Geometry of Kinematics, Color and the Worldsheet. _JHEP_, 05:096, 2018.


[6] N. Arkani-Hamed, H. Frost, G. Salvatori, P-G. Plamondon, and H. Thomas. All Loop Scattering As A Counting Problem. 9 2023.


[7] N. Arkani-Hamed, H. Frost, G. Salvatori, P-G. Plamondon, and H. Thomas. All Loop Scattering For All Multiplicity. 11 2023.


[8] Nima Arkani-Hamed, Carolina Figueiredo, Hadleigh Frost, and Giulio Salvatori. Tropical
Amplitudes For Colored Lagrangians. 2 2024.


[9] Nima Arkani-Hamed, Qu Cao, Jin Dong, Carolina Figueiredo, and Song He. Hidden zeros
for particle/string amplitudes and the unity of colored scalars, pions and gluons. 12 2023.


[10] Nima Arkani-Hamed, Qu Cao, Jin Dong, Carolina Figueiredo, and Song He. Scalar-Scaffolded
Gluons and the Combinatorial Origins of Yang-Mills Theory. 12 2023.


[11] Nima Arkani-Hamed, Qu Cao, Jin Dong, Carolina Figueiredo, and Song He. NLSM _⊂_ Tr( _ϕ_ [3] ).
1 2024.


[12] Freddy Cachazo, Song He, and Ellis Ye Yuan. Scattering of Massless Particles in Arbitrary
Dimensions. _Phys._ _Rev._ _Lett._, 113(17):171601, 2014.


[13] Nima Arkani-Hamed and Juan Maldacena. Cosmological Collider Physics. 3 2015.


[14] Juan M. Maldacena and Guilherme L. Pimentel. On graviton non-Gaussianities during inflation. _JHEP_, 09:045, 2011.


[15] Suvrat Raju. New Recursion Relations and a Flat Space Limit for AdS/CFT Correlators.
_Phys._ _Rev._ _D_, 85:126009, 2012.


[16] Paolo Benincasa. From the flat-space S-matrix to the Wavefunction of the Universe. 11 2018.


[17] Nima Arkani-Hamed and Paolo Benincasa. On the Emergence of Lorentz Invariance and
Unitarity from the Scattering Facet of Cosmological Polytopes. 11 2018.


[18] Nima Arkani-Hamed, Paolo Benincasa, and Alexander Postnikov. Cosmological Polytopes
and the Wavefunction of the Universe. 9 2017.


[19] Dionysios Anninos, Tarek Anous, Daniel Z. Freedman, and George Konstantinidis. Late-time
Structure of the Bunch-Davies De Sitter Wavefunction. _JCAP_, 11:048, 2015.


52


[20] Nima Arkani-Hamed, Daniel Baumann, Hayden Lee, and Guilherme L. Pimentel. The Cosmological Bootstrap: Inflationary Correlators from Symmetries and Singularities. _JHEP_,
04:105, 2020.


[21] Nima Arkani-Hamed, Daniel Baumann, Aaron Hillman, Austin Joyce, Hayden Lee, and Guilherme L. Pimentel. Differential Equations for Cosmological Correlators. 12 2023.


[22] Nima Arkani-Hamed, Daniel Baumann, Aaron Hillman, Austin Joyce, Hayden Lee, and Guilherme L. Pimentel. Kinematic Flow and the Emergence of Time. 12 2023.


[23] Aaron Hillman. Symbol Recursion for the dS Wave Function. 12 2019.


[24] Paolo Benincasa and Gabriele Dian. The Geometry of Cosmological Correlators. 1 2024.


[25] Paolo Benincasa and Francisco Vaz˜ao. The Asymptotic Structure of Cosmological Integrals.
2 2024.


[26] Harry Goodhew, Sadra Jazayeri, and Enrico Pajer. The Cosmological Optical Theorem.
_JCAP_, 04:021, 2021.


[27] Paolo Benincasa. Amplitudes meet Cosmology: A (Scalar) Primer. 3 2022.


[28] Paolo Benincasa and William J. Torres Bobadilla. Physical representations for scattering
amplitudes and the wavefunction of the universe. _SciPost_ _Phys._, 12(6):192, 2022.


[29] Daniel Baumann, Harry Goodhew, and Hayden Lee. Kinematic Flow for Cosmological Loop
Integrands. 10 2024.


[30] Paolo Benincasa and Francisco Vaz˜ao. Cosmological Infrared Subtractions & Infrared-Safe
Computables. 5 2024.


[31] Scott Melville and Enrico Pajer. Cosmological Cutting Rules. _JHEP_, 05:249, 2021.


[32] Sadra Jazayeri, Enrico Pajer, and David Stefanyszyn. From locality and unitarity to cosmological correlators. _JHEP_, 10:065, 2021.


[33] Harry Goodhew, Sadra Jazayeri, Mang Hei Gordon Lee, and Enrico Pajer. Cutting cosmological correlators. _JCAP_, 08:003, 2021.


[34] Paolo Benincasa, Giacomo Brunello, Manoj K. Mandal, Pierpaolo Mastrolia, and Francisco
Vaz˜ao. On one-loop corrections to the Bunch-Davies wavefunction of the universe. 8 2024.


[35] Shounak De and Andrzej Pokraka. A physical basis for cosmological correlators from cuts.
11 2024.


[36] Scott Melville and Guilherme L. Pimentel. A de Sitter S-matrix from amputated cosmological
correlators. _JHEP_, 08:211, 2024.


[37] Chandramouli Chowdhury, Arthur Lipstein, Jiajie Mei, Ivo Sachs, and Pierre Vanhove. The
Subtle Simplicity of Cosmological Correlators. 12 2023.


[38] Till Heckelbacher, Ivo Sachs, Evgeny Skvortsov, and Pierre Vanhove. Analytical evaluation
of cosmological correlation functions. _JHEP_, 08:139, 2022.


53


[39] Santiago Agui Salcedo and Scott Melville. The cosmological tree theorem. _JHEP_, 12:076,
2023.


[40] David Meltzer. The inflationary wavefunction from analyticity and factorization. _JCAP_,
12(12):018, 2021.


[41] Noah Bittermann and Austin Joyce. Soft limits of the wavefunction in exceptional scalar
theories. _JHEP_, 03:092, 2023.


[42] Sebasti´an C´espedes, Anne-Christine Davis, and Scott Melville. On the time evolution of
cosmological correlators. _JHEP_, 02:012, 2021.


[43] Nima Arkani-Hamed and Carolina Figueiredo. Circles and Triangles, the NLSM and Tr(Φ [3] ).
3 2024.


[44] Qu Cao, Jin Dong, Song He, Canxin Shi, and Fanky Zhu. On universal splittings of tree-level
particle and string scattering amplitudes. _JHEP_, 09:049, 2024.


[45] Paolo Benincasa. Cosmological Polytopes and the Wavefuncton of the Universe for Light
States. 9 2019.


[46] Nima Arkani-Hamed, Qu Cao, Jin Dong, Carolina Figueiredo, and Song He. Surface Kinematics and ”The” Yang-Mills Integrand. 8 2024.


[47] N. Arkani-Hamed, C. Figueiredo, and F. Vaz˜ao. to appear. 2025.


[48] Alexander Postnikov. Permutohedra, associahedra, and beyond, 2005.


[49] Alexander Postnikov, Victor Reiner, and Lauren Williams. Faces of generalized permutohedra,
2007.


[50] Nima Arkani-Hamed, Song He, Giulio Salvatori, and Hugh Thomas. Causal diamonds, cluster
polytopes and scattering amplitudes. _JHEP_, 11:049, 2022.


[51] Nima Arkani-Hamed, Song He, Thomas Lam, and Hugh Thomas. Binary geometries, generalized particles and strings, and cluster algebras. _Phys._ _Rev._ _D_, 107(6):066015, 2023.


[52] Nima Arkani-Hamed, Song He, and Thomas Lam. Stringy canonical forms. _JHEP_, 02:069,
2021.


[53] Ewgenij Gawrilow and Michael Joswig. _polymake:_ _a_ _Framework_ _for_ _Analyzing_ _Convex_ _Poly-_
_topes_ . 2000.


[54] T. S. Bunch and P. C. W. Davies. Quantum Field Theory in de Sitter Space: Renormalization
by Point Splitting. _Proc._ _Roy._ _Soc._ _Lond._ _A_, 360:117–134, 1978.


54


##### Corr5 :

Top Front Facet:


Bottom/Back Facet:


(1,3)T : Hexagon



Assoc5


Cosmo5



(1,3)B+(3,5)B: Pentagon

(1,3)B: Square

##### Corr21-loop :



Top Front Facet:


Bottom/Back Facet:


(1,p)T : Hexagon



Assoc21-loop


Cosmo21-loop



(1,p)B+(2,p)B: Pentagon

(1,p)B: Square


Figure 19: The top figure shows the combinatorial structure of the three-dimensional _n_ = 5
cosmological correlahedron, looked at from above. We see the top pentagon facet as the _n_ = 5
associahedron, and the bottom decagon as the _n_ = 5 cosmohedron. A number of other facets,
edges and vertices are labelled by collections ( _C, P_ ) of non-overlapping chords and subpolygons.
There are 30 vertices. The top 5 vertices (marked in blue) all correspond to triangulations of the
associahedron, the rest of the vertices are all the terms in the correlator. The bottom figure shows
exactly the same for the _n_ = 2, 1-loop correlator. As for the amplitude polytopes, there are two
kinds of “loop” variable, touching the puncture. The top facet is the hexagon familiar from the
amplitude. The bottom is the dodecagon for the cosmohedron. The vertices not on the top facet
all correspond to the terms in the correlator.


55


