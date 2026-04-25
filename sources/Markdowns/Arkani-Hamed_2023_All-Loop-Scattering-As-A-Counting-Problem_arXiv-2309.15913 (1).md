Prepared for submission to JHEP

## **All Loop Scattering as a Counting Problem**


**N.** **Arkani-Hamed,** _[a]_ **H.** **Frost,** _[b]_ **G.** **Salvatori,** _[c]_ **P-G.** **Plamondon** _[d]_ **H.** **Thomas** _[e]_


_aSchool_ _of_ _Natural_ _Sciences,_ _Institute_ _for_ _Advanced_ _Study,_ _Princeton,_ _NJ,_ _08540,_ _USA_

_bMathematical_ _Institute,_ _Andrew_ _Wiles_ _Building,_ _Woodstock_ _Rd,_ _Oxford,_ _UK_

_cMax-Plank-Instit¨ut_ _fur_ _Physik,_ _Werner-Heisenberg-Institut,_ _D-80805_ _M¨unchen,_ _Germany_

_dLaboratoire_ _de_ _Math´ematiques_ _de_ _Versailles,_ _UVSQ,_ _CNRS,_ _Universit´e_ _Paris-Saclay,_ _IUF,_ _France_

_eLaCIM,_ _D´epartement_ _de_ _Math´ematiques,_ _Universit´e_ _du_ _Qu´ebec_ _`a_ _Montr´eal,_ _Montr´eal,_ _QC,_ _Canada_


_E-mail:_ `[arkani@ias.edu](mailto:arkani@ias.edu)`, `[frost@maths.ox.ac.uk](mailto:frost@maths.ox.ac.uk)`, `[giulios@mpp.mpg.de](mailto:giulios@mpp.mpg.de)`,
`[pierre-guy.plamondon@uvsq.fr](mailto:pierre-guy.plamondon@uvsq.fr)`, `[thomas.hugh](mailto:thomas.hugh_r@uqam.ca)` ~~`r`~~ `@uqam.ca`


Abstract: This is the first in a series of papers presenting a new understanding of scattering

amplitudes based on fundamentally combinatorial ideas in the kinematic space of the scat
tering data. We study the simplest theory of colored scalar particles with cubic interactions,

at all loop orders and to all orders in the topological ’t Hooft expansion. We find a novel

formula for loop-integrated amplitudes, with no trace of the conventional sum over Feynman

diagrams, but instead determined by a beautifully simple counting problem attached to any

order of the topological expansion. These results represent a significant step forward in the

decade-long quest to formulate the fundamental physics of the real world in a radically new

language, where the rules of spacetime and quantum mechanics, as reflected in the principles

of locality and unitarity, are seen to emerge from deeper mathematical structures.


**Contents**


**1** **Introduction** **and** **Summary** **2**

1.1 Kinematic space 6

1.2 The First Miracle: Discovering Feynman diagrams 8

1.3 An infinity of diagrams and the spectre of Gravity 10

1.4 The Amplitudes 12

1.5 The Second Miracle: The Counting Problem 14

1.6 Back to the Amplitude! 17


**2** **The** **partial** **amplitude** **expansion** **18**


**3** **Momenta** **and** **curves** **20**

3.1 Mountainscapes 20

3.2 Intersections 21

3.3 Momentum Assignments 23

3.3.1 Aside on Homology 25

3.4 Spirals 26


**4** **The** **Feynman** **Fan** **26**

4.1 Example: tree level at 5-points 27

4.2 The Fan 28

4.3 The Mapping Class Group 28

4.3.1 Aside on automorphisms 29

4.4 Example: the non-planar 1-loop propagator 30

4.5 The Delta plane 31

4.6 Example: the planar 1-loop propagator 32


**5** **A** **Counting** **Problem** **For** **Curves** **33**

5.1 Curve Matrices 34

5.2 Headlight Functions 36

5.3 Example: tree level at 5-points 37

5.4 Example: the non-planar 1-loop propagator 38

5.5 Spirals 39

5.6 Example: the planar 1-loop propagator 40

5.7 Example: the genus one 2-loop vacuum 41


**6** **Integrand** **Curve** **Integrals** **42**

6.1 Example: the tree level 5-point amplitude 43

6.2 Example: the planar 1-loop propagator 44

6.3 Example: the planar 1-loop 3-point amplitude 45


                   - i                    

6.4 Note on factorization 46


**7** **Amplitude** **Curve** **Integrals** **47**

7.1 Example: the planar 1-loop propagator 48

7.2 Example: the non-planar 1-loop propagator 49

7.3 Example: The non-planar 3-point amplitude 50

7.4 Example: genus-one 2-loop amplitudes 51


**8** **Modding** **Out** **by** **the** **Mapping** **Class** **Group** **51**

8.1 Warm up 52

8.2 A Tropical Mirzakhani kernel 53

8.3 Example: the non-planar 1-loop propagator 53

8.4 General Tropical Mirzakhani Kernels 55

8.5 The General Iterative Method 55

8.6 Example: the genus one 2-loop vacuum amplitude 57


**9** **Examplitudes** **58**

9.1 The non-planar 1-loop 3-point amplitude 58

9.2 The genus one 2-loop vacuum amplitude 60

9.3 The planar 2-loop tadpole 62

9.4 The planar 3-loop vacuum amplitude 64


**10** **A** **First** **Look** **at** **Recursion** **67**


**11** **Outlook** **68**


**A** **Deriving** **the** **Curve** **Integral** **Formula** **70**


**B** **Factorization** **in** **detail** **71**

B.1 MCG invariant curve 72

B.2 MCG non-invariant curve 72


**C** **The** **Surface** **Symanzik** **polynomials** **73**

C.1 The first surface Symanzik 74

C.2 The second surface Symanzik 75


**D** **The** **Recursion** **Formula** **76**


**E** **Recursion** **Examples** **77**

E.1 The 3-point non-planar 1-loop amplitude 77

E.2 The 2-loop vacuum at genus one 78

E.3 A comment on the 1-loop planar amplitudes 79


                   - 1                    

**F** **Details** **for** **the** **non-planar** **1-loop** **propagator** **79**


**1** **Introduction** **and** **Summary**


Scattering amplitudes are perhaps the most basic and important observables in fundamental

physics. The data of a scattering process—the on-shell momenta and spins of the particles—

are specified at asymptotic infinity in Minkowski space. The conventional textbook formalism

for computing amplitudes “integrates in” auxiliary structures that are not present in the

final amplitude, including the bulk spacetime in which particle trajectories are imagined to

live, and the Hilbert space in which the continuous bulk time evolution of the wavefunction

takes place. These auxiliary structures are reflected in the usual formalism for computing

amplitudes, using Feynman diagrams, which manifests the rules of spacetime (locality) and

quantum mechanics (unitarity). As has been increasingly appreciated over the past three

decades, this comes at a heavy cost—the introduction of huge redundancies in the description

of physics, from field redefinitions to gauge and diffeomorphism redundancies, leading to

enormous complexities in the computations, that conceal a stunning hidden simplicity and

seemingly miraculous mathematical structures revealed only in the final result [1–7].

This suggests that we should find a radically different formulation for the physics of

scattering amplitudes. The amplitudes should be the answer to entirely new mathematical

questions that make no reference to bulk spacetimes and Hilbert space, but derive locality

and unitarity from something more fundamental. A number of concrete examples of this have

already been found in special cases. The discovery of deep and simple new structures in com
binatorics and geometry has led to new definitions of certain scattering amplitudes, without

reference to spacetime or quantum mechanics. Notably, the amplituhedron determines the

scattering amplitudes in planar N =4 SYM, and associahedra and cluster polytopes determine

colored scalar amplitudes at tree-level and one-loop [8–11].

Up to now, these results have been limited in how much of the perturbative expansion

they describe—at all loop orders for maximally supersymmetric theories, but only in the

planar limit, and only through to one loop for non-supersymmetric theories. Furthermore,

the connection between combinatorial geometry and scattering amplitudes at loop level has

only been made through the integrand (pre-loop integration) of the amplitudes, and not the

amplitudes themselves. Both of these limitations must be transcended to understand all

aspects of particle scattering in the real world.

This article is the first in a series reporting on what we believe is major new progress

towards this goal. These ideas set the foundation for a number of other interrelated threads

and results that will appear in various groups of papers. So we take this opportunity to give

a birds-eye view of the nature of these developments and the new concepts that are driving

this progress.


                   - 2                    

Our departure point is a new formulation of a simple theory,—colored scalar particles with

cubic interactions,—at all loop orders and to all orders in the topological ’t Hooft expansion,

in the form of what we call a _curve integral_ . This approach has no hint of a sum over Feynman

diagrams anywhere in sight and is instead associated with a simple counting problem defined

at any order in the topological expansion. This counting problem defines a remarkable set
of variables, _uC_, associated with every curve, _C_, on a surface. The _u_ -variables non-trivially
define _binary_ _geometries_ [12] by dint of satisfying the remarkable non-linear equations [13]


       _uC_ + _u_ _[n]_ _D_ [(] _[C,D]_ [)] = 1 _,_ (1.1)

_D_


where _n_ ( _C, D_ ) is the intersection number of the curves _C, D_ . In the _positive_ _region_, where all
the _uC_ are non-negative, the _u_ -equations force all the _uC_ to lie between 0 and 1: 0 _≤_ _uC_ _≤_ 1.
Of mathematical interest, this positive region is a natural and invariant compactification of

_Teichm¨uller_ _space_ . This algebraic presentation of Teichm¨uller space is a counterpart to the

famous synthetic compactification of Teichm¨uller spaces and surface-type cluster varieties
given by Fock-Goncharov [14, 15]. The new compactifications defined by the _uC_ variables are
immediately relevant for physics, and lead to the new _curve_ _integral_ formulation of all-loop

amplitudes presented in this article.

The curve integral does more than reformulate the perturbative series in a new way. It

also exposes basic new structures in field theory. For instance, a striking consequence of our

formulation is that amplitudes for large _n_ particles at _L_ -loops effectively factorise into a tree

and a loop computation. The full large _n_ amplitudes can be reconstructed from computations

of _n_ -point tree amplitudes and low-point _L_ -loop amplitudes. Moreover, our curve integral

formulas make manifest that amplitudes satisfy a natural family of differential equations in

kinematic space. The solutions of these equations give novel and efficient recursion relations

for all-loop amplitudes.

This article focuses on colored scalar amplitudes. However, the results here have exten
sions to other theories. New curve integral formulations have been discovered for theories of

colored scalar particles with arbitrary local interactions, as well as for the amplitudes of pions

and non-supersymmetric Yang-Mills theories. These formulas reveal striking inter-relations

between these theories, together with surprising hidden properties of their amplitudes that

are made manifest by the curve integral formalism.

Our results also have implications for the understanding of strings and UV completion.

The counting problem at the heart of this paper not only defines QFT amplitudes, it also
defines amplitudes for bosonic strings, via the _u_ -variables, _uC_, mentioned above. This gives a
combinatorial formulation of string amplitudes that makes no reference to worldsheet CFTs

and vertex operators. This new approach to string amplitudes differs from the conventional

theory in a very fundamental way. The _u_ -variables, which are derived from a simple counting

problem, have a beautiful and direct connection to the geometry of two-dimensional surfaces.

But this connection is via the _hyperbolic_ _geometry_ of Teichm¨uller space, and _not_ via the

conventional picture of Riemann surfaces with a complex structure. The new string formulas


                   - 3                    

are not just an exercise in passing between the complex and the hyperbolic pictures for

Teichm¨uller space. We find that we can reproduce bosonic strings at loop level, but other

choices are just as consistent, at least insofar as the field theory limit is concerned. This

allows us to deform string amplitudes into a larger, but still highly constrained, space of

interesting objects. This runs counter to the lore that string theory is an inviolable structure

that cannot be modified without completely breaking it. Our larger class of string amplitudes

transcends the usual strictures on spacetime dimension, as well as the famous instabilities of

non-supersymmetric strings. Moreover, our new combinatorial-geometric point of view also
makes it easier to recover particle amplitudes from strings in the _α_ _[′]_ _→_ 0 limit. By contrast,

recovering field theory from conventional string theory involves vastly (technically, infinitely!)

more baggage than is needed [16].

There are several other related developments, including the discovery of a remarkable

class of polytopes, _surfacehedra_, whose facet structure captures, mathematically, the intricate

boundary structure of Teichm¨uller space, and, physically, the intricate combinatorics of am
plitude singularities at all loop orders, and whose _canonical_ _form_ determines (an appropriate

notion of the) loop integrand at all orders in the topological expansion.

The results of all these parallel threads of investigation will be presented in various groups

of papers. We end this preview of coming attractions by explaining a quite different sort of

motivation for our works that will be taken up in near-future work. The counting problem

that lies at the heart of this paper has an entirely elementary definition. But the central

importance of this counting problem will doubtless seem mysterious at first sight. It finds its

most fundamental origin in remarkably simple but deep ideas from the “quiver representation

theory” [17, 18] of (triangulated) surfaces. Arrows between the nodes of a quiver can be

associated with maps between vector spaces attached to the nodes. Choosing compatible

linear maps between the nodes defines a _quiver_ _representation_ . In this context, our counting

problem is equivalent to counting the _sub-representations_ of these quiver representations.

This perspective illuminates the mathematical structure underlying all of our formulas. But

these ideas also hint at a fascinating prospect. The amplitudes we study are associated with

the class of surface-type quivers, which are dual to triangulated surfaces. Nothing in our

formulas forces this restriction on us: we are free to consider a much wider array of quivers.

_All_ of these quivers can be associated with amplitude-like functions. This vast new class

of functions enjoys an intricate (amplitude-like) structure of “factorisations” onto simpler

functions. This amounts to a dramatic generalisation of the notion of an “amplitude”, and

in a precise sense also generalises the rules of spacetime and quantum mechanics to a deeper,

more elementary, but more abstract setting.

Having outlined this road map, we return to the central business of this first paper. We
will study the simplest theory of _N_ [2] colored particles with any mass _m_, grouped into an
_N_ _× N_ matrix Φ _[I]_ _J_ [with] _[I, J]_ [= 1] _[,][ · · ·]_ _[, N]_ [.] [The] [Lagrangian,] [with] [minimal] [cubic] [coupling,] [is]


_L_ = Tr( _∂_ Φ) [2] + _m_ [2] Tr(Φ [2] ) + _g_ Tr(Φ [3] ) _,_ (1.2)


in any number _D_ of spacetime dimensions. This theory is a simpler cousin of all theories


                   - 4                    

of colored particles, including Yang-Mills theories, since the singularities of these amplitudes

are the same for all such theories, only the _numerators_ differ from theory to theory. The

singularities of amplitudes are associated with some of the most fundamental aspects of

their conventional interpretation in terms of spacetime processes respecting unitarity. So

understanding the amplitudes for this simple theory is an important step towards attacking

much more general theories.

We will show that _all_ amplitudes in this theory, for any number _n_ of external particles, and

to all orders in the genus (or 1 _/N_ ) expansion [19], are naturally associated with a strikingly

simple counting problem. This counting problem is what allows us to give _curve_ _integral_

formulas for the amplitudes at all orders. The curve integral makes it easy to perform the

loop integrations and presents the amplitude as a single object.

As an example, consider the single-trace amplitude for _n_ -point scattering at 1-loop. Let
the particles have momenta _p_ _[µ]_ _i_ [,] _[i]_ [=] [1] _[, ..., n]_ [.] [The] [curve] [integral] [for] [this] [amplitude] [(pre-loop]
integration) is




- 
_αi_ ( _l_ + _p_ 1 + _· · ·_ + _pi_ ) [2] _−_

_i_ =1 _i,j_



_αi,j_ ( _pi_ + _· · ·_ + _pj−_ 1) [2]

_i,j_




    -     _A_ [1] _n_ _[−]_ [loop] = _d_ _[D]_ _l_


     _i_ _[t][i][≥]_ [0]










_d_ _[n]_ _t_ exp






 _−_



_n_




(1.3)

where


_αi,j_ = _fi,j_ + _fi_ +1 _,j_ +1 _−_ _fi,j_ +1 _−_ _fi_ +1 _,j,_ (1.4)


_αi_ = _αi,i_ + _n,_


_fi,j_ = max(0 _, tj, tj_ + _tj−_ 1 _, · · ·_ _, tj_ + _tj−_ 1 + _· · · ti_ +2) _._ (1.5)


The propagators that arise in the 1-loop Feynman diagrams are either loop propagators, with
momenta ( _l_ + _p_ 1 + _· · ·_ + _pi_ ), or tree-like propagators, with momenta ( _pi_ + _pi_ +1 + _· · ·_ + _pj−_ 1). The
exponential in (1.3) looks like a conventional Schwinger parametrisation integral, except that

_all_ the propagators that arise at 1-loop are included in the exponent. Instead of Schwinger
parameters, we have _headlight_ _functions_ : _αi_ (for the loop propagators) and _αi,j_ (for the tree
propagators). The headlight functions are piecewise linear functions of the _ti_ variables. The
magic is that (1.3) is a _single_ integral over an _n_ -dimensional vector space. Unlike conventional

Schwinger parametrisation, which is done one Feynman diagram at a time, our formulas

make no reference to Feynman diagrams. Amazingly, the exponent in (1.3) breaks _t_ -space

into different cones where the exponent is linear. Each of these cones can be identified

with a particular Feynman diagram, and the integral in that cone reproduces a Schwinger

parameterisation for that diagram. This miracle is a consequence of the properties of the
headlight functions _αi_ ( _t_ ) and _αi,j_ ( _t_ ). These special functions arise from a simple counting
problem associated with the corresponding propagator.

As in conventional Schwinger parametrisation, the dependence on the loop momentum
variable, _l_ _[µ]_, in the curve integral, (1.3), is Gaussian. We can perform the loop integration to


                   - 5                    

**Figure** **1** : Fat graphs at tree-level, 1-loop single trace, 1-loop double trace, and 2-loop single

trace, respectively.


find the a second curve integral for the amplitude (post loop integration),




     _A_ [1] _n_ _[−]_ [loop] =


   _i_ _[t][i][≥]_ [0]



_D_

 - 2 _π_  - 2
_d_ _[n]_ _t_ _e_ _[−]_ _[F]_ _U_ _._ (1.6)
_U_



In this formula, the polynomials _U_ and _F_ are given by






_αi,j pi.pj_

_i,j_




   _αi,_ _F_ =

_i_ _i,j_



 _m_ [2][ �]




  _αi_ + 2

_i_ _i,j_



_U_ = 


_αiαj_ ( _pi_ + _· · · pj−_ 1) [2] _−_

_i,j_






 _U._ (1.7)



These polynomials are analogs of the familiar Symanzik polynomials, but whereas the Symanzik

polynomials appear in individual Feynman integrals, this one curve integral above computes

the whole amplitude.

These 1-loop curve integrals generalise to all orders in perturbation theory, at any loop

order and genus. In the rest of this introductory section we give a birds-eye view of the key

formulas and results.


**1.1** **Kinematic** **space**


To begin with, we have to define the _kinematic_ _space_ where all the action will take place.

In our theory, each Feynman diagram is what is called a ‘double-line notation diagram’,

‘ribbon graph’ or ‘fatgraph’ in the literature; we will call them fatgraphs in what follows.

Examples of fatgraphs are shown in Figure 1. Order by order, in the ’t Hooft expansion,

these Feynman diagrams get organised into partial amplitudes, labeled by their shared _color_

_structure_ . Conventionally, when we do a ’t Hooft expansion, we think of these fat graphs as

‘living on’ or ‘being drawn on’ a surface with some genus and number of boundary components.

We will think of them in a different way: a _single_ fat graph itself _defines_ a surface. In fact,

we will use a single fat graph to define all the data we need to compute an amplitude!

Take some fatgraph, Γ, at any order in the ’t Hooft expansion. Suppose that it has _n_

external lines and _E_ internal edges. Then this fat graph has loop order, _L_, with


_E_ = _n_ + 3( _L −_ 1) _._ (1.8)


Let the external lines have momenta _p_ 1 _, . . ., pn_, and introduce _L_ loop variables, _ℓ_ 1 _, . . ., ℓL_ .
Then, by imposing momentum conservation at each vertex of Γ, we can find a consistent


                   - 6                    

**Figure** **2** : A tree fat graph with momenta assigned to all edges.


assignment of momenta to all edges of the fat graph in the usual way: if each edge, _e_, gets a
momentum _p_ _[µ]_ _e_ [,] [then] [whenever] [three] [edges,] _[e]_ 1 _[, e]_ 2 _[, e]_ 3 [,] [meet] [at] [a] [vertex,] [we] [have]


_p_ _[µ]_ _e_ 1 [+] _[ p]_ _e_ _[µ]_ 2 [+] _[ p]_ _e_ _[µ]_ 3 [= 0] _[.]_ (1.9)


For example, Figure 2 is an assignment of momenta to the edges of a tree graph.

The amplitude itself depends on momenta only through Lorentz invariant combinations.

So we want to define a collection of Lorentz invariant kinematic variables. Consider a curve,

_C_, drawn on the fatgraph Γ that starts at an external line, passes through the graph and
exits at another external line. For example, the curve in Figure 3 starts at _p_ 2, and exits at _p_ 5.
Every such curve can be assigned a unique momentum. It is given by the momentum of the

first edge plus the sum of all momenta on the graph entering the curve ‘from the left’. For
example, in Figure 3, the curve starts with momentum _p_ 2, and then takes two right turns. At
the first right turn, momentum _p_ 3 enters from the left. At the second right turn, momentum
_p_ 4 enters from the left. The total momentum of the curve is then given by


_p_ _[µ]_ _C_ [=] _[ p]_ 2 _[µ]_ [+] _[ p]_ 3 _[µ]_ [+] _[ p]_ 4 _[µ][.]_ (1.10)


Notice that if we had gone in the opposite direction (starting at _p_ 5), we would have got


_−p_ _[µ]_ _C_ [=] _[ p]_ 5 _[µ]_ [+] _[ p]_ 1 _[µ][.]_ (1.11)


But by total momentum conservation ( _p_ 1 + _. . ._ + _pn_ = 0), it does not matter which direction
we take.

For a general curve, _C_, on any fatgraph, this rule can be written as:


_PC_ _[µ]_ [=] _[ p]_ start _[µ]_ [+]            - _p_ _[µ]_ from left _[.]_ (1.12)

right turns


This rule assigns to every curve _C_ on our fatgraph Γ some momentum, _PC_ _[µ]_ [.] [Each] _[P][ µ]_ _C_ [is] [a]
linear combination of external momenta, _pi_, and loop variables, _ℓa_ . Each curve, _C_, then also
defines a Lorentz invariant kinematic variable


_XC_ = _PC_ [2] [+] _[ m]_ [2] _[.]_ (1.13)


                   - 7                    

**Figure** **3** : Every curve, _C_, drawn on the fat graph inherits a momentum, _PC_ _[µ]_ [,] [from] [the]
momenta assigned to the fat graph itself.


The collection of variables _XC_, for _all_ curves _C_ on the fatgraph, defines a complete set of
kinematic variables in our kinematic space. Modulo a small detail about how to deal with

internal color loops, this completes the description of our kinematic space.

It is significant in our story that we can use the momenta of a _single_ fat graph (or
Feynman diagram) to define a complete set of kinematic variables _XC_ . As we will see in more
detail in Section 6, this basic idea ends up solving the long-standing problem of defining a

good notion of loop integrand beyond the planar limit!


**1.2** **The** **First** **Miracle:** **Discovering** **Feynman** **diagrams**


We now look for a question whose answer produces scattering amplitudes. We just saw how we

can define all our kinematics using a single fatgraph. So with this starting point, what would

make us consider _all_ possible Feynman diagrams (i.e. all spacetime processes)? And why

should these be added together with equal weights (as demanded by quantum mechanics)?

Amazingly, the answer to both of these fundamental questions is found right under our noses,

once we think about how to systematically describe all the curves on our fatgraph.

How can we describe a curve on our fat graph without drawing it? We can do this by

labeling all the edges, or “roads”, on the fatgraph. Any curve passes through a series of these

roads. Moreover, at each vertex, we demand that the curve must turn either left or right:

we do not allow our curves to do a ‘U turn’. It follows that a curve is fully described by the

order of the roads and turns it takes as it passes through the graph. For example, the curve

in Figure 4 enters through edge ‘1’, takes a left turn, goes down ‘ _x_ ’, takes a left turn, goes

down ‘ _y_ ’, takes a right turn, and then exits via ‘4’.

We can represent this information graphically as a _mountainscape_, where left turns are

represented by upward slopes, and right turns are represented by downward slopes. The

mountainscape for the curve in Figure 4 is shown in the Figure.

Once again, let our fatgraph have _E_ internal edges. To every curve _C_, we will associate
a vector **g** _C_ in _curve_ _space_ . As a basis for this vector space, take _E_ vectors **e** _i_, associated to
each internal edge. Then **g** _C_ can be read off from the mountainscape for _C_ using the following


                   - 8                    

**Figure** **4** : Describing a curve on a fatgraph (left) using a mountainscape diagram (right).


**Figure** **5** : The five (non boundary) curves that we can draw on a 5-point tree fatgraph.



rule:

      **g** _X_ =



**e** v _._ (1.14)

valleys v




- 
**e** p _−_

peaks p



For example, the curve in Figure 4 has a peak at ‘ _y_ ’ and no valleys. So the _g_ -vector for this

curve is
**g** _C_ = **e** _y._ (1.15)


Now consider _every_ curve that we can draw on the fatgraph in Figure 4. There are 10

possible curves. 5 of these are ‘boundaries’, and their g-vectors end up vanishing (because

their mountainscapes have no peaks or valleys). The remaining 5 curves are drawn in Figure
5. If we label the external lines, each curve can be given a name _Cij_ ( _i, j_ = 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5), where
_Cij_ is the curve connecting _i_ and _j_ . Their g-vectors are


**g** 13 = **e** _x,_ **g** 14 = **e** _y,_ **g** 24 = _−_ **e** _x_ + **e** _y,_ **g** 25 = _−_ **e** _x,_ **g** 35 = _−_ **e** _y._ (1.16)


If we draw these five g-vectors, we get Figure 6. This has revealed a wonderful surprise! Our

g-vectors have divided curve space into five regions or _cones_ . These cones are spanned by the

g-vectors for the following pairs of curves:


( _C_ 13 _, C_ 14) _,_ ( _C_ 14 _, C_ 24) _,_ ( _C_ 24 _, C_ 25) _,_ ( _C_ 25 _, C_ 35) _,_ and ( _C_ 35 _, C_ 13) _._ (1.17)


These pairs of curves precisely correspond to _all_ the five Feynman diagrams of the 5-point

tree amplitude!

This is a general phenomenon. The collection of g-vectors for all the curves _C_ on a

fatgraph is called _the_ _g-vector_ _fan_ [20–22], or _the_ _Feynman_ _fan_, associated to that fatgraph.
Each top-dimensional cone of the fan is spanned by an _E−_ tuple of curves, _Ca_ 1 _, · · ·_ _, CaE_,


                   - 9                    

**Figure** **6** : The collection of **g** -vectors for the fat graph in Figure 4 cuts the 2-dimensional

vector space into five regions.


and these _E−_ tuples of curves are precisely the propagators of Feynman diagrams. Moreover,

the cones are non-overlapping, and together they densely cover the entire vector space! The

g-vector fan is telling us that all the Feynman diagrams for the amplitude are combined in

curve space.

Even better, each of the cones in the g-vector fan have the same size. It is natural to
measure the size of a cone, bounded by some g-vectors **g** 1 _, · · ·_ _,_ **g** _E_, using the determinant of
these vectors: _⟨_ **g** 1 _· · ·_ **g** _E⟩_ . Remarkably, the cones of the g-vector fan all satisfy: _⟨_ **g** 1 _· · ·_ **g** _E⟩_ =
_±_ 1.

To summarise, starting with a _single_ fatgraph at any order in perturbation theory, simply

recording the data of the curves on the fatgraph, via their g-vectors, brings _all_ the Feynman

diagrams to life. Furthermore, we see why they are all naturally combined together into one

object, since they collectively cover the entire curve space! This represents a very vivid and

direct sense in which the most basic aspects of spacetime processes and the sum-over-histories

of quantum mechanics arise as the answer to an incredibly simple combinatorial question.


**1.3** **An** **infinity** **of** **diagrams** **and** **the** **spectre** **of** **Gravity**


An important novelty appears with the first non-planar amplitudes. Consider the double
trace one-loop amplitude at 2-points. A fatgraph for this amplitude is given in Figure 7.

There are now infinitely many curves that we can draw on this fat graph: they differ from

one another only in how many times they wind around the graph.

The g-vector fan for this infinity of curves is shown in Figure 8. These g-vectors break

curve space up into infinitely many cones. Each of these cones is bounded by a pair of
g-vectors, _gCm_ and _gCm_ +1, where _Cm_ and _Cm_ +1 are two curves that differ by exactly one


                   - 10                    

**Figure** **7** : A double-trace 1-loop fat graph, which has infinitely many possible curves.


**Figure** **8** : The g-vector fan for the 2-point double-trace 1-loop fat graph, which has infinitely

many regions.


_winding_ . If we use our rule for the momenta of curves, (1.12), the momenta of these curves

are
_PC_ _[µ]_ _m_ [=] _[ mk][µ]_ [ +] _[ ℓ][µ][,]_ [and] _[P][ µ]_ _Cm_ +1 [= (] _[m]_ [ + 1)] _[k][µ]_ [ +] _[ ℓ][µ][.]_ (1.18)


So the momenta associated to each cone are related to each other by a translation in the loop
variable, _ℓ_ _[µ]_ _�→_ _ℓ_ _[µ]_ + _k_ _[µ]_ . It follows that _every_ cone in Figure 8 corresponds to a copy of the

_same_ Feynman diagram.

What has gone wrong? The g-vector fan is telling us to include infinitely many copies

of one Feynman diagram. This is a consequence of the _mapping_ _class_ _group_ of the fat graph

in Figure 7. The mapping class group of this fatgraph acts by increasing the winding of

curves drawn on the fatgraph. In fact, this infinity of windings is the heart of the well-known

difficulty in defining a loop integrand for non-planar amplitudes. Fortunately, as we will see,

it is easy to _mod_ _out_ by the action of the mapping class group, which we will do using what

we call the _Mirzakhani_ _trick_ [23]. Getting rid of these infinities using the Mirzakhani trick is

the final ingredient we need in order to define amplitudes directly from the combinatorics of


                   - 11                    

a single fatgraph.

As an aside, note that the infinite collection of cones in Figure 8 does not quite cover the
entire vector space! The g-vectors asymptotically approach the direction ( _−_ 1 _,_ 1), but never
reach it. This is the beginning of fascinating story: it turns out that the vector ( _−_ 1 _,_ 1) is the

g-vector for the _closed_ curve that loops once around the fat graph. Nothing in our story asks

us to consider these closed curves, but the g-vector fan forces them on us. Physically, these

new closed curves are associated with the appearance of a new _uncoloured_ particle, _σ_ . These

missing parts of the fan are then seen to have a life of their own: they tell us about a theory
with uncoloured self-interactions, _σ_ [3], that is minimally coupled to our colored particle by an

interaction _σ_ Tr (Φ). The appearance of _σ_ is a scalar avatar of how the graviton is forced on

us in string theory even if we begin only with open strings. From our perspective, however,

this has absolutely nothing to do with the worldsheet of string theory; it emerges directly

from the combinatorics defined by a fatgraph.


**1.4** **The** **Amplitudes**


The g-vector fan gives a beautiful unified picture of all Feynman diagrams living in an _E_ 
dimensional vector space, _curve_ _space_ . This result suggests a natural formula for the full

amplitude in the form of an integral over curve space. To find this formula, we need one extra
ingredient. For every curve, _C_, we will define a piecewise-linear _headlight_ _function_, _αC_ ( **t** ).
We will define the headlight function _αC_ so that it “lights up” curve space in the direction
**g** _C_, and vanishes in all other g-vector directions:


_αC_ ( **g** _D_ ) = _δC,D_ (1.19)


This definition means that _αC_ vanishes everywhere, except in those cones that involve **g** _C_ .
Moreover, _αC_ is _linear_ inside any given cone of the Feynman fan.
Using linear algebra, we can give an explicit expression for _αC_ in any cone where it is
non-vanishing. Suppose that the g-vectors of such a cone are ( **g** _C,_ **g** _D_ 1 _, · · ·_ _,_ **g** _DE−_ 1). The
unique linear function of **t** which evaluates to 1 on **g** _C_ and 0 on all the other g-vectors is


_[· · ·]_ **[ g]** _[D][E][−]_ [1] _[⟩]_
_αC_ = _[⟨]_ **[t g]** _[D]_ [1] (1.20)

_⟨_ **g** _C_ **g** _D_ 1 _· · ·_ **g** _DE−_ 1 _⟩_ _[.]_


In what follows, imagine that we already know these functions, _αC_ ( **t** ).
We now define an _action_, _S_, given by a sum over all curves on a fatgraph:


_S_ ( **t** ) =         - _αC_ ( **t** ) _XC,_ with _XC_ = _PC_ [2] [+] _[ m]_ [2] _[.]_ (1.21)

_C_


Recall that _PC_ _[µ]_ [is the momentum we associate to a curve] _[ C]_ [.] [If we restrict] _[ S]_ [(] **[t]** [) to a single cone,]
bounded by some g-vectors, **g** _C_ 1 _, . . .,_ **g** _CE_, then the only _α_ ’s that are non-zero in this cone
are precisely _αC_ 1 _, . . ., αCE_ . Moreover, _S_ ( **t** ) is linear in this cone. It is natural to parametrise
the region inside this cone by **t** = _ρ_ 1 **g** _C_ 1 + _· · · ρE_ **g** _CE_, with _ρi_ _≥_ 0 positive. Then we can


                   - 12                    

integrate exp( _−S_ ) in this cone. The result is identical to the result of a standard Schwinger

parametrisation for a single Feynman diagram:



_E_



_i_ =1




 
_d_ _[E]_ _t e_ _[−][S]_ =

cone



_∞_


_d_ _[E]_ _ρ |⟨gC_ 1 _· · · gCE_ _⟩|_

0



_E_


_e_ _[−][ρ][i][X][Ci]_ =

_i_ =1



1
_PC_ [2] _i_ [+] _[ m]_ [2] _[.]_ (1.22)



The factor _|⟨gX_ 1 _· · · gXE_ _⟩|_ is the Jacobian of the change of variables from ( _t_ 1 _, · · ·_ _, tE_ ) to
( _ρ_ 1 _, · · ·_ _, ρE_ ). As we have remarked, the cones are _unimodular_ and these Jacobian factors are
all equal to 1!

In order to get the full amplitude, all we have to do now is integrate exp( _S_ ) over the

whole vector space, instead of restricting it to just a single cone. However, to account for the

infinity resulting from the _mapping_ _class_ _group_, we also need to factor out this MCG action

in our integral, which we denote by writing the measure as


_d_ _[E]_ _t_
(1.23)
MCG _[.]_


Before doing the loop integrations, the full amplitude is then given by a _curve_ _integral_ :












 
_−_ _αX_ ( **t** )( _p_ [2] _X_ [+] _[ m]_ [2][)]

_X_




  _A_ = _d_ _[D]_ _ℓ_ 1 _· · · d_ _[D]_ _ℓL_




- _d_ _[E]_ _t_
MCG [exp]



_._ (1.24)



The dependence on loop momenta in this formula is Gaussian. When we integrate the loop

momenta, we find the final amplitude is given by a curve integral




  - _d_ _[E]_ _t_
_A_ =
MCG




- _πL_

_U_ ( _α_ )




- _[D]_ 2 - _F_ ( _α_ ) exp _._ (1.25)
_U_ ( _α_ )



_U_ ( _α_ ) and _F_ ( _α_ ) are homogeneous polynomials in the headlight functions. They are analogous

to Symanzik polynomials, but are not associated with any particular Feynman diagram. We
give simple formulas for _A_ and _F_ in Section 7.

The key to using these curve integral formulas lies in how we mod out by the MCG. One

way of doing this would be to find a _fundamental_ _domain_ in **t** -space that would single out

one copy of each Feynman diagram. However, in practice this is no easier than enumerating

Feynman diagrams. Instead, we will use an elegant way of modding out that we call _the_

_Mirzakhani_ _trick_, which is analogous to the Fadeev-Popov trick familiar from field theory. As

we will see, any MCG invariant function, _f_, can be integrated as,

             - _d_ _[E]_ _t_              
[=] _d_ _[E]_ _t K_ ( _α_ ) _f,_ (1.26)
MCG _[f]_


where the _Mirzakhani_ _kernel_ _K_ ( _α_ ) is a simple rational function of the _αC_ ’s. [1] We will describe
several formulas for these kernels. In all cases, _K_ has support on a finite region of the fan, so


1The restriction on the integration region [�] _i_ _[t][i]_ _[≥]_ [0] [in] [equation] [(][1.6][)] [for] [1-loop] [amplitudes] [can] [be] [thought]

of as the smallest example of a Mirzakhani kernel. In this formula, we are modding out by a discrete _Z_ 2
symmetry, described more in Section 4.5.


                   - 13                    

(a) (b) (c)


**Figure** **9** : Three mountainscapes.


that only a small number of the _αC_ ’s is ever needed to compute the amplitude. We will also
show how some of our methods for producing _K_ give new systematic recursive methods for

computing amplitudes.


**1.5** **The** **Second** **Miracle:** **The** **Counting** **Problem**


We have given a formula, (1.25), for partial amplitudes at any order in the ‘t Hooft expansion
of our theory. However, the meat of this formula is in the headlight functions, _αC_ . The
problem is that headlight functions are, naively, hard to compute!

The issue can already been seen at tree level. For _n_ -points at tree level, the number
of possible curves, _C_, is _∼_ _n_ [2], whereas the number of Feynman diagrams (or cones) grows
exponentially as _∼_ 4 _[n]_ . Each _αC_ restricts to a different linear function on each of the _∼_ 4 _[n]_

cones. So we would expect that it takes an exponentially-growing amount to work to compute
all of the _αC_,—about as much work as it would take us to just enumerate all the Feynman
diagrams to begin with! So, is there an easier way to compute _αC_ ?
This is where a second miracle occurs. It turns out that headlight functions can be

computed efficiently by matrix multiplication. In fact, the calculation is completely _local_ _to_

_the_ _curve_, in the sense that we only need to know the path taken by _C_, and nothing else

about the fatgraph it lives in. There are always many fewer curves than there are Feynman
diagrams. This means that the amount of work to compute the _αC_ ’s should grow slower than
the amount of work it takes to enumerate all Feynman diagrams.
This way of computing _αC_ is based on a simple combinatorial problem. For a curve, _C_,
draw its _mountainscape_ . We are going to record all the ways in which we can pick a subset

of letters of _C_, subject to a special rule: if we pick a letter _y_, we also have to pick any letters

_downhill_ of _y_ . We will then define an _F_ _polynomial_ for the curve, _F_ ( _C_ ), which records the

valid subsets.

For example, for the mountainscape in Figure 9(a), we get


_F_ = 1 + _a_ + _c_ + _ac_ + _abc._ (1.27)


This is because we can choose the following subsets: no-one (“1”); just _a_ ; just _c_ ; _a_ and _c_

together; or finally we can pick _b_, but if we do, we must also pick _a_ and _c_, which are both

downhill of _b_ . In Figure 9(b), we get


_F_ = 1 + _b_ + _ab_ + _bc_ + _abc,_ (1.28)


                   - 14                    

because in this example we can choose: no-one; just _b_ ; we can pick _a_, but if we do we must

also pick _b_ ; we can pick _c_, but we must then also pick _b_ ; and finally we can can pick both _a_

and _c_, but then we must also pick _b_ . Finally, we leave Figure 9(c) as an exercise. The result

is

_F_ = 1 + _a_ + _d_ + _ad_ + _ab_ + _abd_ + _abcd._ (1.29)


In general, there is a fast method for computing _F_ ( _C_ ) by reading the mountainscape for

_C_ from left to right. Say the leftmost letter is _Y_, and call the next letter _y_ . Then write
_F_ ( _C_ ) = _F_ no + _F_ yes, where we group the terms in _F_ ( _C_ ) according to whether they include _Y_
( _F_ yes) or not ( _F_ no). Similarly write _f_ no _, f_ yes for what we would get starting instead from _y_ .
Suppose that in our mountainscape we move “up” from _Y_ to _y_ . Then if we do not pick _Y_,

then we cannot pick _y_ either, since if we choose _y_ we must choose _Y_ . On the other hand if

we do choose _Y_, we can either pick or not pick _y_ . Thus, in this case, we have


_F_ no = _f_ no _,_ _F_ yes = _Y_ ( _f_ no + _f_ yes) _._ (1.30)


Similarly if, in our mountainscape, we move down from _Y_ to _y_, we find that


_F_ no = _f_ no + _f_ yes _,_ _F_ yes = _Y f_ yes _._ (1.31)



In matrix form, we find that

         _F_ no
_F_ yes


where _ML_ and _MR_ are the matrices











= _ML,R_ ( _Y_ )




_f_ no
_f_ yes



_,_ (1.32)












1 1

0 _Y_



_._ (1.33)



_ML_ ( _Y_ ) =




1 0

_Y_ _Y_



_,_ _MR_ ( _Y_ ) =



Now suppose that the curve _C_ is given explicitly by the following series of edges and

turns:
( _y_ 1 _,_ turn1 _, y_ 2 _,_ turn2 _, · · ·_ _, ym−_ 1 _,_ turn _m−_ 1 _, ym_ ) _,_ (1.34)



where turn _i_ is either a left or right turn, immediately following _yi_ . Given (1.32), we find

          -          -          -          _F_ no 1

= _M_ _,_

_F_ yes _ym_











= _M_




1
_ym_



_,_ (1.35)



where
_M_ ( _C_ ) = _M_ turn1( _y_ 1) _M_ turn2( _y_ 2) _· · · M_ turn _m−_ 1( _ym−_ 1) _._ (1.36)


So our counting problem is easily solved simply by multiplying a series of 2 _×_ 2 matrices

(equation 1.33) associated with the left and right turns taken by the curve _C_ .


                   - 15                    

Suppose that the initial edge of _C_, _y_ 1, and the final edge, _ym_, are external lines of the
fatgraph. It is natural to write _F_ ( _C_ ) as a sum over four terms:


_F_ ( _C_ ) = _F_ no _,_ no + _F_ no _,_ yes + _F_ yes _,_ no + _F_ yes _,_ yes _,_ (1.37)


where we group terms in _F_ ( _C_ ) according to whether they do or do not include the first and
last edges: _y_ 1 and/or _ym_ . Indeed, these terms are also the entries of the matrix _M_ ( _C_ ),







_M_ ( _C_ ) =




_F_ no _,_ no _F_ no _,_ yes
_F_ yes _,_ no _F_ yes _,_ yes



_,_ (1.38)



if we now set _ym_ = 1. In fact, we will also set _y_ = 1 for every external line of the fatgraph,
and will reserve _y_ -variables for internal edges of the fatgraph.
Notice that det _ML_ ( _y_ ) = det _MR_ ( _y_ ) = _y_, so that



det _M_ ( _C_ ) =



_m−_ 1


_yi._ (1.39)

_i_ =2



In other words, we have the identity


          _F_ no _,_ no _F_ yes _,_ yes = _F_ no _,_ yes _F_ yes _,_ no + _yi._ (1.40)


_i_


Motivated in part by this identity, we will define _u_ -variables for every curve,



_uC_ = _[F]_ [(] _[C]_ [)][no] _[,]_ [yes] _[ F]_ [(] _[C]_ [)][yes] _[,]_ [no]



_._ (1.41)
_M_ ( _C_ )11 _M_ ( _C_ )22




_[F]_ [(] _[C]_ [)][no] _[,]_ [yes] _[ F]_ [(] _[C]_ [)][yes] _[,]_ [no] = _[M]_ [(] _[C]_ [)][12] _[M]_ [(] _[C]_ [)][21]

_F_ ( _C_ )no _,_ no _F_ ( _C_ )yes _,_ yes _M_ ( _C_ )11 _M_ ( _C_ )22



These _uC_ variables are most interesting to us in the region _yi_ _≥_ 0. Equation (1.40) implies
that 0 _≤_ _uC_ _≤_ 1 in this region. They vastly generalise the _u_ -variables defined and studied in

[24, 25].

We now define the headlight functions. We define them to capture the asymptotic be
haviour of the _u_ -variables when thought of as functions of the **y** variables. We define


_αC_ = _−_ Trop _uC._ (1.42)


where Trop _uC_ is the so-called _tropicalization_ of _uC_ .
The idea of tropicalization is to look at how functions behave asymptotically in **y** -space.
To see how this works, parameterise the _yi_ _≥_ 0 region by writing _yi_ = exp _ti_, where the _ti_ are
real variables. Then, as the _ti_ become large, Trop _uC_ is defined such that


_uC_ ( **t** ) _→_ exp (Trop _uC_ ) _._ (1.43)


For example, consider a simple polynomial, _P_ ( _y_ 1 _, y_ 2) = 1 + _y_ 2 + _y_ 1 _y_ 2 = 1 + _e_ _[t]_ [2] + _e_ _[t]_ [1][+] _[t]_ [2] . As
we go to infinity in **t** = ( _t_ 1 _, t_ 2) in different directions, different monomials in _P_ will dominate.
In fact, we can write, as we go to infinity in **t**,


_P_ _→_ exp max(0 _, t_ 2 _, t_ 1 + _t_ 2) _,_ (1.44)


                   - 16                    

and so Trop ( _P_ ) = max(0 _, t_ 2 _, t_ 1 + _t_ 2). If we have a product of polynomials, _F_ = [�] _a_ _[P][ c]_ _a_ _[a]_ [, then]
as we go to infinity in **t** we have _F_ _→_ _e_ [Trop(F)], where Trop _F_ = _ca_ Trop ( _Pa_ ).

[�]
Returning to headlight functions, our definition can also be written as


_αC_ = Trop ( _M_ ( _C_ )11) + Trop ( _M_ ( _C_ )22) _−_ Trop ( _M_ ( _C_ )12) _−_ Trop ( _M_ ( _C_ )21) _._ (1.45)


For example, consider again the _n_ = 5 tree amplitude. Take the curve _C_ from Figure 4
(left). This curve has path (1 _, L, x, R, y, R,_ 4). So it has a matrix (with _y_ 23 _, y_ 15 _≡_ 1)







_M_ ( _C_ ) = _ML_ (1) _MR_ ( _x_ ) _MR_ ( _y_ ) =


Using this matrix, we find that its _u_ -variable is




1 1 + _y_

1 1 + _y_ + _xy_



_._ (1.46)



1 + _y_
_uC_ = (1.47)
1 + _y_ + _xy_ _[,]_


and so its headlight function is


_αC_ = max(0 _, ty, tx_ + _ty_ ) _−_ max(0 _, ty_ ) _._ (1.48)


Amazingly, this function satisfies the key property of the headlight functions: _αC_ vanishes on
every g-vector, except for its own g-vector, **g** _C_ = (1 _,_ 0).


**1.6** **Back** **to** **the** **Amplitude!**


We have now formulated how to compute all-order amplitudes in TrΦ [3] theory as a counting

problem. The final expression for the integrated amplitude at any order of the topological
expansion associated with a surface _S_ is given as




  -   - _πL_
_A_ = _d_ _[E]_ _t K_ ( _α_ )

_U_ ( _α_ )




- _[D]_ 2 - _F_ ( _α_ )
exp
_U_ ( _α_ )




_,_ (1.49)



where _F_ ( _α_ ) _, U_ ( _α_ ) are homogeneous polynomials in the _αC_ ’s, _K_ ( _α_ ) is the Mirzakhani kernel
that mods out by the mapping-class-group, and crucially, each _αC_ is determined entirely
by the path of its curve, using a simple counting problem on the curve. The presence of
_K_ ensures that only a finite number of _αC_ ’s ever appear in our computations, which makes
the formula easy to apply. There is no trace of the idea of ‘summing over all spacetime

processes’ in this formula. Instead, small combinatorial problems attached to the curves on

a fatgraph, treated completely independently of each other, magically combine to produce

local and unitary physics, pulled out of the platonic thin air of combinatorial geometry.

Our goal in the rest of this paper is to describe these ideas systematically. Our focus in

here will exclusively be on simply presenting the formulas for the amplitudes. This presenta
tion will be fully self-contained, so that the interested reader will be fully equipped to find the
curve integrals for the Tr _ϕ_ [3] theory at any order in the topological expansion. The methods


                   - 17                    

can be applied at any order in the topological expansion, but there are a number of novelties

that need to be digested. We illustrate these subtleties one at a time, as we progress from

tree level examples through to one and two loops, after which no new phenomena occur. We

begin at tree-level to illustrate the basic ideas. At one-loop single-trace, we show how to deal

with _spiralling_ curves. Then, as we have seen above, double-trace amplitudes at 1-loop expose

the first example of the infinities associated with the mapping class group. Finally, we study

the leading 1 _/N_ correction to single-trace at 2-loops—the genus one amplitude—to show how

to deal with a non-abelian mapping class group. This non-abelian example illustrates the

generality and usefulness of the Mirzakhani trick.

In all cases discussed in this paper we will use use the smallest example amplitudes

possible to illustrate the new conceptual points as they arise. The next paper in this series

will give a similarly detailed set of formulae for amplitudes for any number of particles, _n_ . In

this sense this first pair of papers can be thought of as a “user guide” for the formalism. A

systematic accounting of the conceptual framework underlying these formulae, together with

an exposition of the panoply of related developments, will be given in the later papers of this

series.


**2** **The** **partial** **amplitude** **expansion**


Consider a single massive scalar field with two indices in the fundamental and anti-fundamental
representations of SU( _N_ ), _ϕ_ = _ϕ_ _[I]_ _J_ _[t][I]_ _[t][J]_ [,] [and] [with] [a] [single] [cubic] [interaction,]


_Lint_ = _g_ Tr                 - _ϕ_ [3][�] = _g ϕ_ _[J]_ _I_ _[ϕ]_ _J_ _[K][ϕ]_ _K_ _[I]_ _[.]_ (2.1)


The trace of the identity is Tr(1) = _δI_ _[I]_ [=] _[N]_ [.] [The] [propagator] [for] [the] [field] _[ϕ]_ [can] [be] [drawn]
as a double line and the Feynman diagrams are _fatgraphs_ with cubic vertices. The Feynman
rules follow from (2.1). To compute the _n_ point amplitude, _An_, fix _n_ external particles with
momenta _ki_ _[µ]_ [and] [colour] [polarisations] _[t][IJ]_ _i_ [.] [A] [fatgraph] [Γ] [with] _[V]_ [cubic] [vertices] [contributes] [to]
the amplitude as


( _ig_ ) _[V]_ _C_ Γ Val(Γ) _,_ (2.2)


where _C_ Γ is the tensorial contraction of the polarisations _t_ _[IJ]_ _i_ according to Γ. The kinematical
part is given by an integral of the form



_L_

    
  Val(Γ) =




- 
_d_ _[D]_ _ℓi_

_i_ =1 edges



edges _e_



1
_Pe_ [2] + _m_ [2] _[,]_ (2.3)



for some assignment of loop momenta to the graph. Each momentum _Pe_ _[µ]_ [is] [linear] [in] [the]
external momenta _ki_ _[µ]_ [and] [in] [the] [loop] [momentum] [variables] _[ℓ][µ]_ _i_ [.] [To] [find] _[P]_ _e_ _[ µ]_ [,] [the] [edges] [of] [Γ]
need to be oriented, so that momentum conservation can be imposed at each cubic vertex.
The colour factors _C_ Γ organise the amplitude _An_ into partial amplitudes. This is because
_C_ Γ depends only on the topology of Γ regarded as a surface, and forgets about the graph.


                   - 18                    

**Figure** **10** : Feynman graphs Γ and the surfaces _S_ (Γ) that label their colour factors.


Write _S_ (Γ) for the surface obtained from the fatgraph Γ by ‘forgetting’ the graph. Two
fatgraphs Γ1 _,_ Γ2 share the same colour factor, _C_ Σ, if they correspond to the same marked
surface, Σ = _S_ (Γ1) = _S_ (Γ2). The amplitude can therefore be expressed as



_C_ Σ _A_ Σ _,_ (2.4)



_An_ =



_∞_





- 
( _ig_ ) _[n][−]_ [2+2] _[L]_

_L_ =0 Σ s _._ t



Σ s _._ t _._
_h_ +2 _g_ = _L_ +1



where we sum over marked bordered surfaces Σ having _n_ marked points on the boundary. At

loop order _L_, this second sum is over all surfaces Σ with _h_ boundary components and genus

_g_, subject to the Euler characteristic constraint: _h_ + 2 _g_ = _L_ + 1. The partial amplitudes

appearing in (2.4) are




 _A_ Σ = Val(Γ) _._ (2.5)


Γ
_S_ (Γ)=Σ



Examples of some ribbon graphs Γ and their corresponding surfaces are shown in Figure 10.
Our aim is to evaluate _A_ Σ. It is conventional to compute Val(Γ) using _Schwinger_ _param-_
_eters_ . Schwinger parameters are introduced via the identity


1                - _∞_
_P_ [2] + _m_ [2] [=] 0 _dα e_ _[−][α]_ [(] _[P]_ [ 2][+] _[m]_ [2][)] _._ (2.6)

The integration in _ℓ_ _[µ]_ _i_ [loop] [variables] [then] [becomes] [a] [Gaussian] [integral,] [and] [the] [result] [can] [be]
written as



Γ

_−_ _m_ [2][ �]
_U_ Γ



_αi_

_i_



_,_ (2.7)



_D_

- 2
exp




_F_ Γ








    Val(Γ) =


_αi≥_ 0




  - 2 _π_
_d_ _[E]_ _α_
_U_ Γ




- 19 

where _U_ Γ and _F_ Γ are the Symanzik polynomials of Γ. The Symanzik polynomials depend on
Γ regarded as a graph (i.e. forgetting that it is a surface). The first Symanzik polynomial is

given by



_U_ Γ = 

_T_





_αe,_ (2.8)

_e̸∈T_



where the sum is over all spanning trees, _T_, of Γ. The second Symanzik polynomial is given
by a sum over all spanning 2-forests, ( _T_ 1 _, T_ 2), which cut Γ into two tree graphs:






  _Pe_

_e̸∈T_ 1 _∪T_ 2



2













_F_ Γ = _−_ 

( _T_ 1 _,T_ 2)






  _αe_

_e̸∈T_ 1 _∪T_ 2



_,_ (2.9)



where _Pe_ _[µ]_ [is] [the] [momentum] [of] [the] [edge] _[e]_ [.] [It] [can] [be] [shown] [that] _[F]_ Γ [depends] [only] [on] [the]
external momenta, and not on the loop momentum variables.
The partial amplitudes _A_ Σ are given by sums over integrals of this form, as in (2.5). But
it is the purpose of this paper to show how _A_ Σ can be written more compactly as a _single_
Symanzik-like integral. It does not work to naively sum the integrands of Val(Γ) for different

Feynman diagrams Γ. One problem is that there is no conventional way to relate the loop

momentum variables for different Feynman graphs. We will see how this is solved by basic

facts from surface geometry. Moreover, a simple counting problem associated to surfaces will

allow us to define tropical functions we call _headlight_ _functions_ . These simple functions allow

us to evaluate the full partial amplitude without enumerating the Feynman diagrams.


**3** **Momenta** **and** **curves**


Curves on fatgraphs are the key building block for our formulation of amplitudes. In this

section we show how a fatgraph can be used to assign momenta to its curves. This momen
tum assignment solves the problem of finding a consistent choice of momentum variables for

all Feynman diagrams contributing to an amplitude. This generalizes the _dual_ _momentum_

_variables_ that can be used for planar amplitudes.


**3.1** **Mountainscapes**


A _curve_ is a path on the fatgraph that enters from an external line, passes through the

fatgraph without self-intersections, and exits on an external line. It is sometimes useful to

separately consider _closed_ _curves_, which are paths on the fatgraph that form a closed loop.

Curves are important because they define _triangulations_ of fatgraphs. A triangulation is

a maximal collection of pairwise non-intersecting curves. The key point is that each triangulation of Γ corresponds, by graph duality, to some fatgraph Γ _[′]_ . These fatgraphs Γ _[′]_ all have
the same colour factor and so contribute, as Feynman diagrams, to the same amplitude. [2] The


2There is also a duality between triangulations of a fatgraph Γ, and triangulations of the surface _S_ (Γ).

Defining this requires some care and is not needed for the results here.


                   - 20                    

**Figure** **11** : A triangulation of a fatgraph is a maximal set of curves that cuts the fatgraph

into cubic vertices.


methods in this paper can be used to automatically find all the triangulations of Γ without

having to list them, using only the data of the curves on Γ.

A curve _C_ on Γ is completely specified by reading off the order in which _C_ passes through

the edges of Γ. It is also helpful to record the _left_ _and_ _right_ _turns_ made by the curve. We

present this information using _mountainscape_ _diagrams_ . The vertices of a mountainscape are

labelled by the edges of Γ. Each left turn made by _C_ is recorded with a left arrow (and a

step up), while each right turn is written with a right arrow (and a step down):


_j_ _i_



_i_



_k_



_Turn_ _left_ _from_ _i_ _to_ _j._ _Turn_ _right_ _from_ _i_ _to_ _k._


For example, the curve in Figure 12(a) passes through the edges 1 _, x, w, z, y, w,_ 4. Its

mountainscape is shown in Figure 12(b). If we traverse _C_ in the opposite direction we

obtain the left-right reflection of this mountainscape. We regard these as being the _same_

mountainscape. For brevity, it is convenient to write mountainscapes as a _word_, writing ‘L’

for a left turn, and ‘R’ for a right turn. The mountainscape in Figure 12(b) is given by the

word

_C_ = 1 _LxRwRzRyLwL_ 4 _._ (3.1)


**3.2** **Intersections**


Mountainscape diagrams encode the intersections of curves. In fact, it is not necessary to

know the whole fatgraph in order to determine if two curves intersect: their mountainscapes

alone have all the data needed.

For example, consider Figure 13. The two curves in Figure 13(a) are


_C_ = _x_ 2 _RyLx_ 4 and _C_ _[′]_ = _x_ 1 _LyRx_ 3 _._ (3.2)


                   - 21                    

**Figure** **12** : A curve on a fatgraph (left) and its mountainscape diagram (right).


**Figure** **13** : A pair of intersecting curves (left), and a pair of non-intersecting curves (right).


These two mountainscapes _overlap_ on the edge _y_, which they share in common. For _C_, _y_ is
a _peak_, whereas for _C_ _[′]_, _y_ is a _valley_ . This is equivalent to the information that _C_ and _C_ _[′]_


_intersect_ at _y_ . By contrast, the two curves in Figure 13(b) are


_C_ = _x_ 1 _LyLx_ 4 and _C_ _[′]_ = _x_ 2 _RyRx_ 3 _._ (3.3)


These curves also overlap on the edge _y_ . But _y_ does not appear in these curves as a peak or
valley. This is equivalent to the information that _C_ and _C_ _[′]_ do not intersect.
In general, if two curves _C_ and _C_ _[′]_ intersect, their paths must overlap near the intersection.
So suppose that _C_ and _C_ _[′]_ share some sub-path, _W_, in common. Then _C_ and _C_ _[′]_ _intersect_
_along_ _W_ only if _W_ is a peak for one and a valley for the other. In other words, _C_ and _C_ _[′]_


intersect at _W_ if they have the form


_C_ = _W_ 1 _RWLW_ 2 and _C_ _[′]_ = _W_ 3 _LWRW_ 4 _,_ (3.4)


or


_C_ = _W_ 1 _LWRW_ 2 and _C_ _[′]_ = _W_ 3 _RWLW_ 4 _,_ (3.5)


                   - 22                    

**Figure** **14** : The two special triangulations of a fatgraph, _T_ and _T_ [˜], are defined by curves with

exactly one peak (left) and curves with exactly one valley (right).


for some sub-paths _W_ 1 _, W_ 2 _, W_ 3 _, W_ 4. The left/right turns are very important. If the two
curves have the form, say,


_C_ = _W_ 1 _RWRW_ 2 and _C_ _[′]_ = _W_ 3 _LWLW_ 4 _,_ (3.6)


then they _do_ _not_ _intersect_ at _W_ .

Using this general rule, we can find triangulations of fatgraphs using only the data of the

curves.
For every fatgraph Γ, there are two special triangulations. Suppose that Γ has edges _ei_,
_i_ = 1 _, . . ., E_ . Let _Ci_ be the curve that, starting from _ei_, turns right in both directions away
from _ei_ . Then


_Ci_ = _· · · LeLe_ _[′]_ _LeiRe_ _[′′]_ _Re_ _[′′′]_ _R · · ·_ _._ (3.7)


_Ci_ has exactly one peak, which is at _ei_ . The intersection rule, (3.4), shows that no pair of
such curves _Ci, Cj_ ( _i ̸_ = _j_ ) intersect. So the _Ci_ give _E_ nonintersecting curves, and these form
a triangulation, _T_ . We can also consider the curves


_C_ ˜ _i_ = _· · · ReRe_ _[′]_ _ReiLe_ _[′′]_ _Le_ _[′′′]_ _L · · ·_ _,_ (3.8)


that turn left going in both directions away from _ei_ . These _C_ [˜] _i_ each have exactly one valley,
at _ei_, and so they are mutually nonintersecting. Together, they give another triangulation of
the fatgraph, _T_ [˜] . An example of these special triangulations is given in Figure 14.


**3.3** **Momentum** **Assignments**


The edges of a fatgraph Γ are naturally decorated with momenta, induced by the _external_
_momenta_ of the graph. Let Γ have _n_ external momenta _p_ _[µ]_ 1 _[, . . ., p]_ _n_ _[µ]_ [,] [directed] _[into]_ [the] [graph]
(say). By imposing momentum conservation at each cubic vertex, we obtain a momentum _p_ _[µ]_ _e_
for every edge. If Γ has loops (i.e. _E_ _> n −_ 3), then there is a freedom in the definition of the
_p_ _[µ]_ _e_ [that] [we] [parametrise] [by] [some] _[L]_ _[loop]_ _[momentum]_ _[variables]_ [,] _[ℓ][µ]_ 1 _[, . . ., ℓ][µ]_ _L_ [.] [This] [is] [the] [standard]
rule for assigning momenta to a fatgraph, Γ.


                   - 23                    

(a) (b)


**Figure** **15** : (a) Reversing a curve reverses its momentum assignment. (b) The momenta of

three curves that cut out a cubic vertex satisfy momentum conservation.


To go further, we now introduce a way to also assign a momentum to every _curve_ on Γ.
For a curve with an orientation, _[−→]_ _C_, will assign a momentum _P−→_ _[µ]_ [This momentum assignment]
_C_ [.]

should satisfy two basic rules. If _[←−]_ _C_ is the curve with reversed orientation (Figure 15a), then


_P←_ _[µ]_ _−_ _−→_ (3.9)
_C_ [=] _[ −][P][ µ]_ _C_ _[.]_

And if three curves, _[−→]_ _C_ 1 _,_ _[−→]_ _C_ 2 _,_ _[−→]_ _C_ 3, cut out a cubic vertex (Figure 15a), then we impose momentum conservation at that vertex:


_P−→_ _[µ]_ _−→_ _−→_ (3.10)
_C_ 1 [+] _[ P][ µ]_ _C_ 2 [+] _[ P][ µ]_ _C_ 3 [= 0] _[.]_


The solution to satisfying both (3.9) and (3.10) is very simple, if we start with the
momenta _p_ _[µ]_ _e_ [assigned] [to] [the] [edges] [of] [Γ.] [Suppose] _[−→]_ _C_ enters Γ via the external line _i_ . Then
assign this curve
_P−→C_ _[µ]_ [=] _[ p]_ _i_ _[µ]_ [+]                      - _p_ _[µ]_ left _[,]_ (3.11)

right turns

where _p_ _[µ]_ left [is] [the] [momentum] [of] [the] [edge] [incident] [on] _[C]_ [from] [the] [left,] [at] [the] [vertex] [where] _[−→]_ _C_
makes a right turn. The momentum assignment, (3.11), can easily be checked to satisfy (3.9)

and (3.10).

For example, take the fatgraph in Figure 16. The assignment of momenta to the edges
of the graph is shown in the Figure. The curve _C_ 0 in Figure 16 enters the graph with
momentum _p_ _[µ]_ . Then it turns left, traverses an edge, and then turns right. At the right turn,
the momentum incident on the curve from the left is _−p −_ _ℓ_ _[µ]_ . So the momentum assignment

of this curve is
_P−→_ _[µ]_ (3.12)
_C_ 0 [=] _[ −][ℓ][µ][.]_

The curve _C_ 1 in Figure 16 has two right turns. At its first right turn, it gains momentum _p_ _[µ]_ .
At its second right turn, it gains momentum _−p_ _[µ]_ _−_ _ℓ_ _[µ]_ . So the momentum assignment of this

curve is
_P−→_ _[µ]_ (3.13)
_C_ 1 [=] _[ p][µ][ −]_ _[ℓ][µ][.]_


                   - 24                    

**Figure 16** : An assignment of momenta to the edges of a fatgraph (left) induces as assignment

of momenta to curves on the fatgraph (right).


For _any_ triangulation, _T_, the above rules assign a momentum to every curve in the

triangulation. By construction, these momenta satisfy momentum conservation at each of

the cubic vertices cut out by _T_ . The upshot of this is that we can _re-use_ the same loop
momentum variables, _ℓ_ 1 _, ..., ℓL_, when assigning momenta to _any_ triangulation of Γ. This
simple idea makes it possible to do the loop integrations for all diagrams at once, instead of

one Feynman diagram at a time, which is a key step towards our formulas for amplitudes.

This idea also makes it possible to compute well-defined _loop_ _integrands_, even beyond the

planar limit.


**3.3.1** **Aside** **on** **Homology**


There is a more formal way to understand the assignment of momenta to curves: these
momentum assignments are an avatar of the homology of the fatgraph. Let _H_ 1(Γ _,_ Γ _∞_ ) be
the homology of Γ (regarded as a surface) relative to the _ends_ of the external edges of the
fatgraph, Γ _∞_ . An oriented curve _[−→]_ _C_ represents a class [ _[−→]_ _C_ ] _∈_ _H_ 1(Γ _,_ Γ0), and

[ _[−→]_ _C_ ] + [ _[←−]_ _C_ ] = 0 (3.14)


in homology. Moreover, if three curves cut out a cubic vertex, their classes satisfy

[ _[−→]_ _C_ 1] + [ _[−→]_ _C_ 2] + [ _[−→]_ _C_ 3] = 0 (3.15)


in homology. This means that a momentum assignment to curves satisfying (3.9) and (3.10)

defines a linear map


_P_ : _H_ 1(Γ _,_ Γ _∞_ ) _→_ R [1] _[,D][−]_ [1] _,_ (3.16)


from _H_ 1(Γ _,_ Γ _∞_ ) to Minkowski space.


                   - 25                    

**Figure** **17** : The momenta incident on a closed loop in a fatgraph sum to zero. This ensures

that the assignment of momentum to a spiral curve is well defined.


**3.4** **Spirals**


The colour factor _C_ Γ is a product of trace factors tr( _t_ 1 _...tk_ ) formed from the colour polarisations _ti_ _[J]_ _I_ [.] [If] [Γ] [has] [a] [closed] [colour] [loop,] [this] [boundary] [contributes] [tr(1)] [=] _[N]_ [to] [the]
colour factor. For such a fatgraph, there are curves that infinitely spiral around this closed

loop. These spiral curves can be treated just the same as all the other curves. In fact, the

momentum assignment for spiral curves follows again from the same rule above, (3.11).
Suppose that Γ has a closed colour loop, _β_ . Suppose that there are some _m_ _≥_ 1 edges

incident on the loop, as in Figure 17. By momentum conservation, the momenta of these
edges, _p_ 1 _, . . ., pm_, must sum up to zero: [�] _i_ _[m]_ =1 _[p][i]_ [= 0.] [This] [ensures] [that] [(][3.11][)] [assigns] [a] [well-]
defined momentum to a curve that spirals around this boundary, because the contributions
from the _p_ _[µ]_ _i_ [vanish] [after] [every] [complete] [revolution.]


**4** **The** **Feynman** **Fan**


For a fatgraph Γ with _E_ edges ( _e_ 1 _, . . ., eE_ ), consider the _E_ -dimensional vector space, _V_,
generated by some vectors, **e** 1 _, . . .,_ **e** _E_ . To every curve _C_ on the fatgraph, we can assign a
_g-vector_, **g** _C_ _∈_ _V_ . These simple integer vectors contain all the key information about the
curves on Γ. Moreover, the _g_ -vectors define a _fan_ in _V_ that we can use to rediscover the

Feynman diagram expansion for the amplitude.

To define the _g_ -vector of a curve, _C_, consider the _peaks_ and _valleys_ of its mountainscape.
_C_ has a _peak_ _at_ _ei_ if it contains


_· · · LeiR · · ·_ _._ (4.1)


                   - 26                    

**Figure** **18** : The five curves on the _n_ = 5 tree fatgraph.


_C_ has a _valley_ _at_ _i_ if it contains


_· · · ReiL · · ·_ _._ (4.2)


Let _a_ _[i]_ _C_ [be] [the] [number] [of] [times] [that] _[C]_ [has] [a] [peak] [at] _[e][i]_ [,] [and] [let] _[b][i]_ _C_ [be] [the] [number] [of] [times]
that _C_ has a valley at _ei_ . This information about the peaks and valleys is recorded by the
_g-vector_ _of_ _C_,



**g** _C_ _≡_



_E_


_gC_ _[i]_ **[e]** _[i][,]_ where _gC_ _[i]_ [=] _[ a]_ _C_ _[i]_ _[−]_ _[b]_ _C_ _[i]_ _[.]_ (4.3)
_i_ =1



Each curve has a distinct _g_ -vector. The converse is even more surprising: a curve is completely

specified by its _g_ -vector.
For example, consider the curve, _Ci_, in the triangulation _T_ Γ, which has only one peak,
at _ei_ . The _g_ -vector for _Ci_ is then


**g** _Ci_ = **e** _i._ (4.4)


So the _g_ -vectors of this triangulation _T_ Γ span the positive orthant of _V_ .


**4.1** **Example:** **tree** **level** **at** **5-points**


Take the comb graph Γ, with edges labelled by variables _x_ and _y_, as in Figure 18. The five

curves on Γ are


_C_ 13 = 1 _LxR_ 3 _,_ _C_ 14 = 1 _LxLyR_ 4 _,_ _C_ 24 = 2 _RxLyR_ 4 _,_ (4.5)


_C_ 25 = 2 _RxLyL_ 5 _,_ _C_ 35 = 3 _RyL_ 5 _._ (4.6)


Counting the peaks and valleys of these mountainscapes gives











**g** 13 =




- 1

0



_,_ **g** 14 =




0

1



_,_ **g** 24 =





_−_ 1

1



_,_ **g** 25 =




- 
_−_ 1

0



_,_ **g** 35 =




- 0

_−_ 1



_._ (4.7)



These _g_ -vectors are shown in Figure 19. They define a _fan_ in the 2-dimensional vector space.
The top-dimensional cones of this fan are spanned by pairs of _g_ -vectors, such as **g** 14 and **g** 24,
whose corresponding curves define triangulations.


                   - 27                    

**Figure** **19** : The Feynman fan for _n_ = 5 tree level.


**4.2** **The** **Fan**


The _g_ -vectors of all the curves on Γ together define an integer fan F _⊂_ _V_ . To define a fan,

we must specify all of its _cones_ . We adopt the rule that two or more _g_ -vectors span a cone in

F if and only if their curves do not intersect. The main properties of F are:


1. It is a polyhedral fan that is dense _V_ . [3]


2. Its top dimensional cones are in 1:1 correspondence with triangulations.


3. The _g_ -vectors of each top-dimensional cone span a parallelepiped of unit volume.


Since the top-dimensional cones of F correspond to triangulations, and hence to Feynman

diagrams, we call F the _Feynman_ _fan_, or sometimes, the _g-vector_ _fan_ .
The property that F is _polyhedral_ _and_ _dense_ means that every rational vector **g** _∈_ _V_ is

contained in _some_ cone in the fan. This implies that every such **g** can be _uniquely_ written as

a positive linear combination of _g_ -vectors. In Section 5, we solve the problem of how to do

this expansion explicitly.


**4.3** **The** **Mapping** **Class** **Group**


The Feynman fan of a fat graph Γ inherits from Γ an action of a discrete, finitely generated

group called the _mapping_ _class_ _group_, MCG. The MCG of a fatgraph, Γ, is the group of

homeomorphisms of Γ, up to isotopy, that restrict to the identity on its boundaries. The

action of MCG on the fatgraph can be studied by considering its action on curves. Since


3A fan is _polyhedral_ if the intersection of any two cones is itself, if nonempty, a cone in the fan, and the

faces of each cone are cones in the fan. A fan is _dense_ if any integer vector is contained in some cone of the

fan. In general, irrational vectors are not always contained in our fans, but this will not play any role in this

paper.


                   - 28                    

**Figure** **20** : Triangulations (left) that are related to each other by the action of of the MCG.

These triangulations are all dual to the same Feynman diagram (right).


we only ever consider curves up to homotopy, a group element _γ_ _∈_ MCG induces a map on

curves
_γ_ : _C_ _�→_ _γC._ (4.8)


Since MCG acts via homeomorphisms, it does not affect curve intersections and non-intersections.
If _C_ and _C_ _[′]_ are two non-intersecting curves, then _γC_ and _γC_ _[′]_ are likewise non-intersecting.
Similarly, if _C, C_ _[′]_ intersect, so do _γC_ and _γC_ _[′]_ . This means that if some curves, _C_ 1 _, . . ., CE_,
form a triangulation, so do their images under MCG. Moreover, if the triangulation _{C_ 1 _, . . ., CE}_
is dual to a fatgraph Γ _[′]_, then each image _{γC_ 1 _, . . ., γCE}_ is _also_ dual to the same fatgraph,
Γ _[′]_ .

For example, take the 2-point non-planar fatgraph Γ in Figure 20. The MCG acts on Γ

by _Dehn_ _twists_ that increase the number of times a curve winds around the fatgraph. All

triangulations of Γ are related to each other by the MCG and they are all dual to the same

fatgraph (right in Figure 20).

In general, if Γ has loop number _L_, then MCG has a presentation with _L_ generators [15].

These can be identified with Dehn twists around annuli in the fatgraph.

The MCG action on curves induces a piecewise linear action on the vector space, _V_,


_γ_ : **g** _C_ _�→_ **g** _γC._ (4.9)


It follows from the above properties of the MCG action on curves that the action of MCG

on _V_ leaves the fan F invariant (if we forget the labels of the rays). Furthermore, two top
dimensional cones of the fan correspond to the same Feynman diagram if and only if they are

related by the MCG action.


**4.3.1** **Aside** **on** **automorphisms**


There is another discrete group that acts on the Feynman fan: the group of graph automor
phisms, Aut(Γ). The elements of Aut(Γ) are permutations of the labels of the edges of Γ. A

permutation is an _automorphism_ if it leaves the list of fat vertices of Γ unchanged (including

the vertex orientations). Each fat vertex can be described by a triple of edge labels with a

cyclic orientation, ( _ijk_ ).
Aut(Γ) has a linear action on _V_ given by permuting the basis vectors **e** 1 _, . . .,_ **e** _E_ . The
action of Aut(Γ) leaves the fan invariant (again if we forget the labels of the rays).


                   - 29                    

**Figure** **21** : A fatgraph with _|_ Aut(Γ) _|_ = 3. Cyclic permutations of the edges leave it un
changed.


**Figure** **22** : The infinite family of curves, _Cn_, for the non-planar one loop propagator.


An example of a fatgraph with nontrivial automorphisms is Figure 21. In this example,

cyclic permutations of the 3 edges preserve the fatgraph. Most fatgraphs that we will consider

have trivial automorphism groups, and so the action of Aut(Γ) will not play a big role in this

paper.


**4.4** **Example:** **the** **non-planar** **1-loop** **propagator**


Take the 1-loop fatgraph Γ in Figure 22, with edges labeled by variables _x_ and _y_ . Some of
the curves on Γ, _Cn_, are shown in the Figure. These curves are related to each other by the
action of MCG, which is generated by a Dehn twist, _γ_ . With the labelling in Figure 22, the

action of _γ_ is
_γ_ : _Cn_ _�→_ _Cn_ +1 _._ (4.10)


There are infinitely many such curves on the fatgraph.

The paths of the curves on Γ are


_Cn_ = 1 _L_ ( _xLyR_ ) _[n]_ _xR_ 2 for _n ≥_ 0 _,_ (4.11)

_Cn_ = 1 _Ry_ ( _RxLy_ ) [1+] _[n]_ _L_ 2 for _n <_ 0 _,_ (4.12)


∆= _xLyR,_ (4.13)


where ∆is the closed loop. Note that the curves _Cn_ differ from one another by multiples of
the closed path ∆. In this way, we can see the MCG directly in terms of the mountainscapes

of the curves.


                   - 30                    

**Figure** **23** : The Feynman fan for the non-planar 1-loop propagator.


Counting peaks and valleys in the mountainscapes, the _g_ -vectors for these curves are:









for _n ≥_ 0 _,_ (4.14)


for _n <_ 0 _,_ (4.15)



**g** _n_ =


**g** _n_ =


**g** ∆ =




_−n_ + 1

_n_


_n_ + 1
_−n −_ 2




- 
_−_ 1

1



_._ (4.16)



These _g_ -vectors define the fan in Figure 19. There are infinitely many rays of this fan. The

action of MCG on curves lifts to a piecewise linear action on the fan, generated by the action

of the Dehn twist _γ_ . _γ_ acts on the fan as


**g** _n_ +1 = **g** _n_ + **g** ∆ _,_ for _n ≥_ 0 _,_ (4.17)


**g** 0 = **g** _−_ 1 + (1 _,_ 1) _,_ (4.18)

**g** _n_ +1 = **g** _n −_ **g** ∆ _,_ for _n < −_ 1 _._ (4.19)


This is (trivially) an isomorphism of the fan.


**4.5** **The** **Delta** **plane**


A _closed_ _curve_ is a curve Γ that forms a loop. For a closed curve ∆, consider the series of left
and right turns that it makes. We can record this series of turns as a _cyclic_ _word_, like _W_ ∆ =
( _RRLRL_ ). Whenever _RL_ appears in _W_ ∆ it corresponds to a _valley_ in the mountainscape,
which happens where the curve switches from turning right to turning left. Likewise, _LR_


                   - 31                    

**Figure** **24** : Curves on the bubble fatgraph.


corresponds to a _peak_ . If the cyclic word _WC_ has _n_ occurrences of ‘ _RL_ ’, it must also have
exactly _n_ occurrences of ‘ _LR_ ’. For example, the cyclic word


( _RRLRLLLRRLL_ ) _,_ (4.20)


switches from right-to-left 3 times, and from left-to-right 3 times.

In other words, the mountainscape for a closed curve has exactly as many peaks as
valleys. It follows that the _g_ -vector, **g** ∆, for any closed curve ∆is normal to the vector
**n** = (1 _,_ 1 _,_ 1 _, ...,_ 1) _[T]_ . We call the plane normal to **n** the ∆ _plane_ : _V_ ∆ _⊂_ _V_ .
For example, in the previous subsection, the closed curve ∆had _g_ -vector **g** ∆ = ( _−_ 1 _,_ 1),
which is normal to the vector (1 _,_ 1).

Finally, note that a closed curve that makes _only_ right-turns (resp. left-turns) corresponds

to a path around a loop boundary of Γ. These curves have no peaks and no valleys. So these

loop boundaries are assigned zero _g_ -vector. They are also assigned zero momentum (by the

reasoning in Section 3.4).


**4.6** **Example:** **the** **planar** **1-loop** **propagator**


Take the 1-loop bubble diagram, Γ, with edges _x_ and _y_, and external edges 1 and 2, as in
Figure 24. Consider the four curves, _C_ 1 _, C_ 2 _, S_ 1 _, S_ 2, shown in the Figure. These have paths


_C_ 1 = 1 _RxLyR_ 1 (4.21)


_C_ 2 = 2 _RyLxR_ 2 (4.22)


_S_ 1 = 1 _RxLyLxLyL · · ·_ (4.23)


_S_ 2 = 2 _RyLxLyLxL · · ·_ _._ (4.24)


                   - 32                    

**Figure** **25** : The Feynman Fan for the 1-loop planar propagator.


The curves _S_ 1 _, S_ 2 end in anticlockwise spirals around the closed loop boundary. There are
also two curves, _S_ 1 _[′]_ [and] _[S]_ 2 _[′]_ [,] [which] [spiral] _[clockwise]_ [into] [the] [puncture:]


_S_ 1 _[′]_ [= 1] _[LyRxRyR][ · · ·]_ (4.25)

_S_ 2 _[′]_ [= 2] _[LxRyRxR][ · · ·]_ _[.]_ (4.26)


Counting peaks and valleys, the _g_ -vectors of these curves are
















- 0

1



_,_ **g** _C_ 2 =




1

_−_ 1



_,_ **g** _S_ 1 =




0

_−_ 1



_,_ **g** _S_ 2 =




- 
_−_ 1

0



_._ (4.27)




- 1

0



_,_ **g** _S_ 2 _′_ [=]



**g** _C_ 1 =





_−_ 1

1



_,_ **g** _S_ 1 _′_ [=]



These _g_ -vectors give the fan in Figure 25. Notice that the _g_ -vectors of the curves _C_ 1 _, C_ 2 lie
on the Delta plane: _x_ + _y_ = 0.

Including the anticlockwise spirals would lead to us counting every Feynman diagram
twice. This is because the triangulation with _C_ 1 _, S_ 1 is dual to the same diagram as the
triangulation by _C_ 1 _, S_ 1 _[′]_ [,] [and] [so] [on.] [To] [prevent] [overcounting,] [it] [makes] [sense] [to] [restrict] [to] [the]
part of the fan that involves only _C_ 1 _, S_ 1 _, S_ 2, and _C_ 2. This part of the fan is precisely the half
space, _x_ + _y_ _≤_ 0, cut out by the Delta plane.


**5** **A** **Counting** **Problem** **For** **Curves**


There is a natural counting problem associated to mountainscapes, and this counting problem

plays the central role in our amplitude computations.

For a mountainscape, _C_, the idea is to form subsets of _C_ by _filling_ _up_ the mountain
scape from the bottom. A subset is valid if it includes everything _downhill_ of itself in the

mountainscape.

For example, consider the curve in Figure 26,


_C_ = 1 _R_ 2 _L_ 3 _._ (5.1)


                   - 33                    

**Figure** **26** : Two examples of mountainscapes and their sub-mountainscapes.


The valid subsets of _C_, shown in the Figure, are 2 _,_ 1 _R_ 2 _,_ 2 _L_ 3, and 1 _R_ 2 _L_ 3. In other words, if 3

is in the subset, then 2 must also be included, because it is downhill of (left of) 3. Likewise,

if 1 is in the subset, then 2 must also be included, because 2 is downhill of (right of) 3.

This information can be summarised using a generating function or _F_ _-polynomial_ . Introduce variables _yi_, _i_ = 1 _, . . ., E_, labelled by the edges of Γ. Then the _F_ -polynomial of a curve
_C_ is




  _FC_ = 1 +

_C_ _[′]_ _⊂C_





_yi,_ (5.2)
_i∈C_ _[′]_



where the sum is over all valid (non-empty) subsets of _C_, including _C_ itself.

In the example, (5.1), we have four valid subsets, and the _F_ -polynomial is


_FC_ = 1 + _y_ 2 + _y_ 1 _y_ 2 + _y_ 2 _y_ 3 + _y_ 1 _y_ 2 _y_ 3 _._ (5.3)


**5.1** **Curve** **Matrices**


Consider a curve _C_ that starts at any edge _ei_ and ends at any edge _ej_ . It is natural to
decompose its _F_ -polynomial as a sum of four terms,


_FC_ = _F−−_ + _F−_ + + _F_ + _−_ + _F_ ++ _,_ (5.4)


where: _F−−_ counts subsets that exclude the first and last edges; _F−_ + counts subsets that
exclude the first edge and include the last edge; and so on.
Now consider what happens if we _extend_ _C_ along one extra edge. Let _C_ _[′]_ extend _C_ by

adding a left turn before _i_ :
_C_ _[′]_ = _ekLC,_ (5.5)


                   - 34                    

for some edge _ek_ . The _F_ -polynomial of _C_ _[′]_ can be deduced using (5.4). Terms that involve _yi_
_must_ contain _yk_, since _ek_ is _downhill_ of _ei_ in the curve. So


_FC′_ = (1 + _yk_ ) _F−−_ + (1 + _yk_ ) _F−_ + + _ykF_ + _−_ + _ykF_ ++ _._ (5.6)


Similarly, if _C_ _[′′]_ is obtained from _C_ by adding a right turn before _ei_, then _C_ _[′′]_ = _elRC_, for
some edge _el_, and we find that the new _F_ -polynomial is


_FC′′_ = _F−−_ + _F−_ + + (1 + _yl_ ) _F_ + _−_ + (1 + _yl_ ) _F_ ++ _._ (5.7)


This equation follows because any term not containing _yi cannot_ contain _yl_, since _ei_ is _downhill_
of _el_ in the curve.
Equations (5.6) and (5.7) can be used to compute the _F_ -polynomial for any curve. It

simple to do implement this is by defining a _curve_ _matrix_, whose entries are given by the

decomposition, (5.4):





_._ (5.8)



_MC_ =




_F−−_ _F−_ +
_F_ + _−_ _F_ ++



The curve matrix _MC′_ is obtained from the curve matrix _MC_ via the matrix version of (5.6):







_MC′_ =




1 0
_yk_ _yk_



_MC._ (5.9)



The matrix multiplying _MC_ in this equation represents what happens when _C_ is extended by
adding a left turn at the start. Similarly, the matrix version of (5.7) is




1 1
0 _yl_







_MC′′_ =



_MC,_ (5.10)



which represents what happens when _C_ is adding a right turn at the start.

It can be convenient to decompose the new matrices appearing in (5.9) and (5.10) as a

product,

        -        -        - ��        -        -        -        - ��        1 0 1 0 1 0 1 1 1 0 1 1

= _,_ = _._ (5.11)

_yk_ _yk_ 0 _yk_ 1 1 0 _yl_ 0 _yl_ 0 1


Then, for any curve, _C_, we can compute its curve matrix, _MC_, directly from the word
specifying the curve. To do this, we just replace each turn and edge with the associated

matrix:







��
1 0

1 1











��
1 1

0 1







=




1 0
0 _yk_



_,_




1 1
0 _yl_



=




1 0
0 _yl_



_._ (5.11)















_L →_




1 0

1 1



_,_ _R →_




1 1

0 1



_,_ _ei_ _→_




1 0
0 _yi_



_._ (5.12)



Every curve matrix _MC_ is then a product of these simple matrices.
For example, for the curve _C_ = 1 _R_ 2 _L_ 3 considered above, its matrix is



��
1 0
0 _y_ 2



��
1 0

1 1



�� 1 0
0 _y_ 3



_MC_ =




1 0
0 _y_ 1



��
1 1

0 1



=




- 1 + _y_ 2 _y_ 2 _y_ 3
_y_ 1 _y_ 2 _y_ 1 _y_ 2 _y_ 3



_._ (5.13)




- 35 

**Figure** **27** : Getting a new fatgraph.


The sum of the entries of this curve matrix recovers the curve’s _F_ -polynomial, (5.3).

Curve matrices neatly factorise. If several curves all begin with the same word, _W_, their
words can be written as _Ci_ = _WCi_ _[′]_ [.] [Their] [matrices] [are] [then] _[M][C]_ _i_ [=] _[M][W][ M]_ _Ci_ _[′]_ [,] [so] [that] [we]
only have to compute _MW_ once to determine all the _MCi_ . Moreover, if we add extra legs to
a fatgraph Γ, to form a larger fatgraph, Γ _[′]_, the matrices _MC_ for the larger fatgraph can be
obtained directly from the matrices for the smaller fatgraph. In practice, this is very useful,

and allows us to exploit the methods in this paper to compute all- _n_ formulas for amplitudes.

[26]


**5.2** **Headlight** **Functions**


It follows from the definition of _MC_, as a product of the matrices in (5.13), that


         det _MC_ = _ye._ (5.14)


_e∈C_


Expanding the determinant, this gives


            - _ye_

1 = _[F][−]_ [+] _[F]_ [+] _[−]_ + _._ (5.15)

_F−−F_ ++ _F−−F_ ++


Motivated in part by this identity, define the _u-variable_ of a curve _C_ as the ratio


_uC_ = _[F][−]_ [+] _[F]_ [+] _[−]_ _._ (5.16)

_F−−F_ ++


These _u_ -variables vastly generalise those studied in [24, 25], and (5.15) is a generalisation of

the _u-equations_ studied there.

The _headlight_ _function_ of a curve _C_ is the _tropicalization_ of the _u_ -variable,


_αC_ = _−_ Trop _uC._ (5.17)


For a polynomial _F_ ( _y_ ), its tropicalization captures the behaviour of _F_ at large values of _yi_ .
Parametrise the _yi_ as _yi_ = exp _ti_ . Then, in the large _t_ limit,


_F_ ( _y_ ) _→_ exp Trop _F_ ( _t_ ) _._ (5.18)


                   - 36                    

For example, if _F_ ( _y_ ) = 1+ _y_ 1 + _y_ 1 _y_ 2, then Trop _F_ ( _t_ ) = max(0 _, t_ 1 _, t_ 1 + _t_ 2). In practice, Trop _F_
is obtained from _F_ by replacing multiplication with addition, and replacing sums with taking

the maximum.
In terms of the matrix _MC_, the headlight function is


_αC_ = Trop _MC_ [1] _[,]_ [1] + Trop _MC_ [2] _[,]_ [2] _−_ Trop _MC_ [1] _[,]_ [2] _−_ Trop _MC_ [2] _[,]_ [1] _[.]_ (5.19)


Headlight functions satisfy the following remarkable property:



_αC_ ( **g** _D_ ) =




1 if _C_ = _D_
(5.20)
0 otherwise.



This implies that headlight functions can be used to express any vector **g** _∈_ _V_ as a positive

linear combination of the generators of a cone of the Feynman fan, by writing


       **g** = _αC_ ( **g** ) **g** _C._ (5.21)


_C_


This expansion has a geometrical interpretation. Any integer vector **g** _∈_ _V_ corresponds to

some curve (or set of curves), _L_, possibly with self-intersections. Any intersections in _L_ can

be uncrossed on Γ using the _skein_ _relations_ . Repeatedly applying skein relations, _L_ can be
decomposed on the surface into a unique set of non-self-intersecting curves, and _αC_ ( _g_ ) is the
number of times the curve _C_ appears in this decomposition.


**5.3** **Example:** **tree** **level** **at** **5-points**


The curves for the 5-points tree level amplitude were given in Section 4.1. Their curve

matrices, using the replacements (5.13), are



_C_ 13 = _LxR_ _−→_ _M_ 13 =


_C_ 14 = _LxLyR_ _−→_ _M_ 14 =


_C_ 24 = _RxLyR_ _−→_ _M_ 24 =


_C_ 25 = _RxLyL_ _−→_ _M_ 25 =


_C_ 35 = _RyL_ _−→_ _M_ 35 =


              - 37              



- 1 1

1 1 + _x_



_,_ (5.22)




1 1

1 + _x_ 1 + _x_ + _xy_


1 + _x_ 1 + _x_ + _xy_

_x_ _x_ (1 + _y_ )









_,_ (5.23)


_,_ (5.24)




1 + _x_ + _xy_ _xy_

_x_ + _xy_ _xy_







_,_ (5.25)




1 + _y_ _y_

_y_ _y_







_._ (5.26)


**Figure** **28** : The Schwinger parameter _α_ 24 on the Feynman fan.


Given these matrices, the headlight functions are


_α_ 13 = max(0 _, x_ ) _,_ (5.27)


_α_ 14 = _−_ max(0 _, x_ ) + max(0 _, x, x_ + _y_ ) _,_ (5.28)


_α_ 24 = _−_ max(0 _, x, x_ + _y_ ) + max(0 _, x_ ) + max(0 _, y_ ) _,_ (5.29)


_α_ 25 = _−x −_ max(0 _, y_ ) + max(0 _, x, x_ + _y_ ) _,_ (5.30)


_α_ 35 = _−y_ + max(0 _, y_ ) _._ (5.31)


It can be verified that _αij_ ( **g** _C_ ) = 1 if _C_ = _Cij_, and that otherwise _αij_ ( **g** _C_ ) = 0. For example,
the values taken by _α_ 24 are shown in Figure 28.


**5.4** **Example:** **the** **non-planar** **1-loop** **propagator**


The mountainscapes for the non-planar 1-loop propagator are given in Section 4.4. Using

these, we can compute the headlight functions, and find:


_αn_ = _fn −_ 2 _fn−_ 1 + _fn−_ 2 _,_ _n ≥_ 0 _,_ (5.32)

_αn_ = _gn −_ 2 _gn_ +1 + _gn_ +2 _,_ _n <_ 0 _._ (5.33)


where the tropical functions _fn_ and _gn_ are given by


_fn_ = max(0 _,_ ( _n_ + 1) _x,_ ( _n_ + 1) _x_ + _ny_ ) _,_ for _n ≥_ 0 _,_ (5.34)


_gn_ = max(0 _, −_ ( _n_ + 1) _x, −_ ( _n_ + 1) _x −_ _ny_ ) _,_ for _n ≤−_ 1 _,_ (5.35)


with the following special cases:


_f−_ 2 = 0 _,_ _f−_ 1 = 0 _,_ _g_ 1 = _−_ 2 _x −_ _y,_ _g_ 0 = _−x._ (5.36)


                   - 38                    

A full derivation of these functions using the matrix method is given in Appendix F.
It is easy to verify that these _αn_ satisfy the key property:



_αn_ ( **g** _m_ ) =


For example, take _n, m ≥_ 0. Then we find




1 if _n_ = _m_
(5.37)
0 otherwise.



so that



_fn_ ( **g** _m_ ) = max(0 _,_ 1 + _n −_ _m_ ) _,_ (5.38)


_αn_ ( **g** _m_ ) = max(0 _,_ 1 + _n −_ _m_ ) + max(0 _, −_ 1 + _n −_ _m_ ) _−_ 2 max(0 _, n −_ _m_ ) _._ (5.39)



This agrees with (5.37).


**5.5** **Spirals**


Suppose _C_ is a curve that ends in a spiral around a loop boundary of Γ. If 1 _,_ 2 _, ..., m_ are the

edges around that boundary, _C_ has the form


_C_ = _W_ 1 _L_ 2 _L...LmL_ 1 _L_ 2 _L...,_ (5.40)


for some subpath _W_ . We can compute the transfer matrix for the infinite tail at the right

end of _C_ . The path for one loop around the boundary is


∆:= 1 _L_ 2 _L...LmL,_ (5.41)


and the matrix for this path is



_M_ ∆ =




- 1 0
_F∗_ _y∗_



_,_ (5.42)



where



_y∗_ =



_m_


_yi,_ and _F∗_ = _y_ 1 + _y_ 1 _y_ 2 + _..._ + _y_ 1 _y_ 2 _...ym._ (5.43)

_i_ =1



Now consider the powers, _M_ ∆ _[n]_ [,]


_M_ ∆ _[n]_ [=]


If the path _W_ has matrix




1 0
_F∗_ (1 + _y∗_ + _· · ·_ + _y∗_ _[n][−]_ [1] ) _y∗_ _[n]_







_._ (5.44)



_MW_ =




- _a_ _b_

_,_ (5.45)

_c_ _d_




- 39 

then the path _W_ ∆ _[n]_ has _u_ -variable


_∗_ )
_uW_ ∆ _n_ = _[b]_ [(] _[c]_ [ +] _[ dF][∗]_ [(1 +] _[ y][∗]_ [+] _[ · · ·]_ [ +] _[ y][n][−]_ [1] (5.46)
_d_ ( _a_ + _bF∗_ (1 + _y∗_ + _· · ·_ + _y∗_ _[n][−]_ [1] )


and in the _n →∞_ limit this tends to (assuming _y∗_ _<_ 1 for convergence)


_uW_ ∆ _∞_ = lim [=] _[b]_ [(] _[c]_ [(1] _[ −]_ _[y][∗]_ [) +] _[ dF][∗]_ [)] (5.47)
_n→∞_ _[u][W]_ [∆] _[n]_ _d_ ( _a_ (1 _−_ _y∗_ ) + _bF∗_ ) _[,]_


which is the _u_ -variable for the full spiraling curve. Instead of computing this limit, it is
convenient to instead compute this _u_ -variable by multiplying the matrix _MW_ with the matrix







_M_ �∆ =




1 _−_ _y∗_ 0
_F∗_ 1



_._ (5.48)



Note that _M_ [�] ∆ is _not_ the _n_ _→∞_ limit of _M_ ∆. We can use this matrix, (5.48), when
computing the matrix for any curve that ends in a spiral: the spiraling part can be replaced
by _M_ [�] ∆ directly. Similarly, suppose a curve _begins_ with a spiral around the closed path
∆= _RmR · · · R_ 2 _R_ 1. Then this infinite spiral contributes a factor of _M_ [�] ∆ _[T]_ [to] [the] [beginning] [of]
the matrix product, with _y∗_ and _F∗_ given as before.


**5.6** **Example:** **the** **planar** **1-loop** **propagator**


We can put these formulas to work for the planar 1-loop propagator. The curves for this

amplitude are given in Section 4.6. Evaluating the curve matrices gives:











_MC_ 1 =


_MS_ 1 =




1 + _x_ 1 + _x_ + _xy_

_x_ _x_ + _xy_




- 1 + _x_ 1

_x_ (1 + _y_ ) 1



_,_ _MC_ 2 =




1 + _y_ 1 + _y_ + _xy_

_y_ _y_ + _xy_



_,_ (5.49)



_,_ _MS_ 2 =




- 1 + _y_ 1

_y_ (1 + _x_ ) 1



_._ (5.50)



The headlight functions are


_αC_ 1 = max(0 _, x_ ) + max(0 _, y_ ) _−_ max(0 _, x, x_ + _y_ ) _,_ (5.51)

_αC_ 2 = max(0 _, x_ ) + max(0 _, y_ ) _−_ max(0 _, y, x_ + _y_ ) _,_ (5.52)

_αS_ 1 = _−x −_ max(0 _, y_ ) + max(0 _, x_ ) _,_ (5.53)

_αS_ 2 = _−y −_ max(0 _, x_ ) + max(0 _, y_ ) _._ (5.54)


Once again, using the _g_ -vectors from Section 4.6, we verify that these functions satisfy



_αC_ ( **g** _D_ ) =




1 if _C_ = _D_
(5.55)
0 otherwise.


- 40 

**Figure** **29** : The 2-loop vacuum graph with genus one.


**5.7** **Example:** **the** **genus** **one** **2-loop** **vacuum**


We now introduce a more complicated example: the 2-loop vacuum amplitude at genus one.

A fatgraph for this amplitude, Γ, is given in Figure 29. The colour factor of this graph has

only one factor, tr(1), because Γ only has one boundary. In fact, the curves on Γ must all

begin and end in spirals around this one boundary. Using Figure 29 we can identify the curves

which have precisely _one_ _valley_ in their mountainscape: i.e. which only have one switch from

turning right to turning left. These three curves are


_C_ 1 _/_ 0 = ( _RwRzRx_ ) _[∞]_ _R_ ( _wLxLzL_ ) _[∞]_ _,_ (5.56)

_C_ 0 _/_ 1 = ( _RxRwRz_ ) _[∞]_ _R_ ( _xLzLwL_ ) _[∞]_ _,_ (5.57)

_C_ 1 _/_ 1 = ( _RzRxRw_ ) _[∞]_ _R_ ( _zLwLxL_ ) _[∞]_ _._ (5.58)


These curves are non-intersecting and form a triangulation. The surface associated to Γ is

the torus with one puncture, and the labels we assign to these curves are inspired by drawing
the curves on the torus, pictured as a quotient of a Z [2] lattice.
Besides _C_ 1 _/_ 1, we find that the only other curve compatible with both _C_ 1 _/_ 0 and _C_ 0 _/_ 1 is


_C−_ 1 _/_ 1 = ( _RxRwRz_ ) _[∞]_ _RxLzR_ ( _xLzLwL_ ) _[∞]_ _._ (5.59)


This curve has a peak at _z_, but no peaks at either _x_ or _w_ (which is what would result in an
intersection with _C_ 1 _/_ 0 or _C_ 0 _/_ 1).
As we will see later, the four curves _C_ 1 _/_ 0 _, C_ 0 _/_ 1 _, C_ 1 _/_ 1 _, C−_ 1 _/_ 1 are all we need to compute


                   - 41                    

the 2-loop vacuum genus one amplitude. Evaluating these curves’ matrices gives







_M_ 1 _/_ 0 =


_M_ 0 _/_ 1 =


_M_ 1 _/_ 1 =


_M−_ 1 _/_ 1 =




_w_ (1 + _x_ + _xz_ ) [2] + (1 _−_ _xzw_ ) [2] 1 + _x_ + _xz_

_w_ (1 + _x_ + _xz_ ) 1


_x_ (1 + _z_ + _zw_ ) [2] + (1 _−_ _xzw_ ) [2] 1 + _z_ + _zw_

_x_ (1 + _z_ + _zw_ ) 1




(1 + _x_ + _xz_ ) [2] + _z_ ( _x_ + _xz_ + _xzw_ ) [2] 1 + _x_ + 2 _xz_ + _xz_ [2] + _xz_ [2] _w_
_x_ (1 + _x_ + 2 _xz_ + _xz_ [2] + _xz_ [2] _w_ ) _x_ (1 + _z_ )







_,_ (5.60)


_,_ (5.61)




- _z_ (1 + _w_ + _wx_ ) [2] + (1 _−_ _xzw_ ) [2] 1 + _w_ + _wx_

_z_ (1 + _w_ + _wx_ ) 1



_,_ (5.62)







_._ (5.63)



Because we restrict to anti-clockwise spiraling curves, all the _g_ -vectors lie in the half-plane
_x_ + _z_ + _w_ _≤_ 0. Restricting to this half-plane, the headlight functions are given by


_α_ 1 _/_ 0 = max(0 _, −w −_ 2 max(0 _, x, x_ + _z_ )) _,_ (5.64)

_α_ 0 _/_ 1 = max(0 _, −x −_ 2 max(0 _, z, z_ + _w_ )) _,_ (5.65)

_α_ 1 _/_ 1 = max(0 _, −z −_ 2 max(0 _, w, w_ + _x_ )) _,_ (5.66)


and


_α−_ 1 _/_ 1 = max(0 _, z_ ) + max (2 max(0 _, x, x_ + _z_ ) _, z_ + 2 _x_ + 2 max(0 _, z, z_ + _w_ )) (5.67)


_−_ max(0 _, x, x_ + _z, x_ + 2 _z, x_ + 2 _z_ + _w_ ) _._ (5.68)


We again verify that these _αC_ are 1 on their corresponding _g_ -vectors.


**6** **Integrand** **Curve** **Integrals**


We want to compute the partial amplitudes of our theory. For some fatgraph Γ, let _A_ be the
amplitude that multiplies the colour factor _c_ Γ.
The momentum assignment rule in Section 3.3 defines one set of loop momentum variables

for all propagators contributing to the amplitude, even beyond planar diagrams. This means
that _A_ can be obtained as the integral of a single _loop_ _integrand_ _I_ :



_L_

  - [�]
_A_ = - _d_ _[D]_ _ℓi_


_i_ =1







_I._ (6.1)



However, beyond planar diagrams, there is a price to pay for introducing our momentum
assignment. For any triangulation by curves, _C_ 1 _, C_ 2 _, ..., CE_, we associate the product of
propagators


1
_,_ (6.2)
_XC_ 1 _XC_ 2 _. . . XCE_


                   - 42                    

where _XC_ is given by the momentum assignment rule. If we sum over every such term, (6.2),
for all triangulations of Γ, we obtain some rational function _I∞_ . But the loop integral of
_I∞_ is not well defined if Γ has a nontrivial mapping class group, MCG. This is because two
triangulations related by the MCG action integrate to the _same_ Feynman diagram. So the
loop integral of _I∞_ contains, in general, infinitely many copies of each Feynman integral.
Fortunately, we can compute integrands _I_ for the amplitude by ‘dividing by the volume
of MCG’. As a function, _I_ is not uniquely defined. But all choices for _I_ integrate to the same

amplitude.
We will compute integrands _I_ using the headlight functions, _αC_ . The formula takes the
form of a _curve_ _integral_,


                - _d_ _[E]_ _t_
_I_ = (6.3)
MCG _[e][−][S]_ [(] **[t]** [)] _[.]_


Here, _E_ is the number of edges of the fatgraph Γ. We call it a _curve_ _integral_ because the

integral is over the _E_ -dimensional vector space, _V_, whose integral points correspond to curves

(or collections of curves) on Γ. As discussed in Section 4.2, the mapping class group MCG

has a piecewise linear action on _V_, and we mod out by this action in the integral. We call

_S_ ( _t_ ) the _curve_ _action_ . It is given by a sum


       _S_ ( **t** ) = _αC_ ( **t** ) _XC,_ (6.4)


_C_


where we sum over all curves, _C_, on the fatgraph. [4] For a general derivation of this curve

integral formula, see Appendix A. In this section, we show how to practically use (6.3) to

compute some simple amplitudes.

In fact, (6.3) also makes the loop integrals easy to do. This leads to a direct curve integral
formula for the amplitude _A_, which we study in Section 7.
Later, in Section 10, we also show that the integrands _I_ can be computed recursively,

starting from the curve integral formula, (6.3). This result generalises the standard _forward_

_limit_ method for 1-loop amplitudes to _all_ orders in the perturbation series.


**6.1** **Example:** **the** **tree** **level** **5-point** **amplitude**


Curve integrals give new and simple amplitude formulas, even at tree level. Take the same

fatgraph studied in Sections 4.1, 5.3 and 6.1. The kinematic variables for the curves on this
graph are ( _i < j −_ 1)
_Xij_ = ( _ki_ + _..._ + _kj−_ 1) [2] + _m_ [2] _._ (6.5)


Then the amplitude, given by (6.1), is


                   _A_ (12345) = _dy_ 1 _dy_ 2 _Z,_ (6.6)


4We exclude _closed_ _curves_ from this sum. Including the closed curves corresponds to coupling our colored

field to an uncolored scalar particle. For simplicity, we delay the discussion of uncolored amplitudes


                   - 43                    

where


_−_ log _Z_ = _α_ 13 _X_ 13 + _α_ 14 _X_ 14 + _α_ 24 _X_ 24 + _α_ 25 _X_ 25 + _α_ 35 _X_ 35 _._ (6.7)


Using the formulas for _αij_ from Section 5.3, _Z_ can be further simplified to


log _Z_ = _X_ 25 _x_ + _X_ 35 _y_ + _s_ 13 _f_ 13 + _s_ 14 _f_ 14 + _s_ 24 _f_ 24 _,_ (6.8)


where _sij_ = 2 _ki · kj_ and the _fij_ are the simple functions


_f_ 13 = max(0 _, x_ ) _,_ _f_ 14 = max(0 _, x, x_ + _y_ ) _,_ _f_ 24 = max(0 _, y_ ) _._ (6.9)


The 5-point amplitude is then


          _A_ (12345) = _dy_ 1 _dy_ 2 exp ( _X_ 25 _x_ + _X_ 35 _y_ + _s_ 13 _f_ 13 + _s_ 14 _f_ 14 + _s_ 24 _f_ 24) _._ (6.10)


It is already interesting to note that the formula for the amplitude has been written in terms
of the simple functions _f_ 13 _, f_ 14 _, f_ 24 _, y_ 1 _, y_ 2, and the Mandelstam invariants _sij_ . These _sij_ are
automatically summed together by the formula to form the appropriate poles of the tree level

amplitude.


**6.2** **Example:** **the** **planar** **1-loop** **propagator**


Consider again the 1-loop planar propagator (Sections 4.6 and 5.6). The amplitude is




  -   _A_ = _d_ _[D]_ _ℓ_


_x_ + _y≤_ 0



_dxdyZ,_ (6.11)



where


_−_ log _Z_ = _αC_ 1 _XC_ 1 + _αC_ 2 _XC_ 2 + _αS_ 1 _XS_ 1 + _αS_ 2 _XS_ 2 _._ (6.12)


We can assign the momenta of the curves to be


_PC_ 1 = 0 _,_ _PS_ 1 = _ℓ,_ _PS_ 2 = _ℓ_ + _k,_ _PC_ 2 = 0 _._ (6.13)


Substituting these momenta (with _k_ [2] + _m_ [2] = 0) into the integrand gives


_−_ log _Z_ = _ℓ_ [2] ( _αS_ 1 + _αS_ 2) + 2 _ℓ_ _· kαS_ 2 + _m_ [2] ( _αC_ 1 + _αC_ 2 + _αS_ 1) _._ (6.14)


At this point, we can either integrate over _x_ + _y_ _≤_ 0, or do the loop integral. Doing the loop

integral first is a Gaussian integral, which gives



_k_ [2] _αS_ 1 _α_ + _S_ [2] 2 _αS_ 2 _−_ _m_ [2] ( _αC_ 1 + _αC_ 2 + _αS_ 1)



_._ (6.15)







_D_

- 2
exp








   _A_ =


_x_ + _y≤_ 0




  - _π_
_dxdy_
_αS_ 1 + _αS_ 2




- 44 

This resembles the Symanzik formula for a single Feynman integral, but instead includes

contributions from all three Feynman diagrams for this amplitude. Finally, substituting the

headlight functions gives



_D_

- 2 - [(] _[y]_ [ + max(0] _[, x]_ [)] _[ −]_ [max(0] _[, y]_ [))][2] exp _m_ [2] _−_ _m_ [2] _|x|_ _._ (6.16)

_x_ + _y_




   _A_ =


_x_ + _y≤_ 0




  - _−π_
_dxdy_
_x_ + _y_



It is not immediately obvious that this reproduces the Feynman integrals for this am
plitude. But note that, for example, restricting the domain of the integral to the negative

orthant gives



_D_

- 2 - - _y_ 2 ��
exp _m_ [2] _._ (6.17)

_x_ + _y_ [+] _[ x]_




 

_x,y≤_ 0




  - _−π_
_dxdy_
_x_ + _y_



After writing
_y_ [2]



(6.18)
_x_ + _y_ [+ (] _[x]_ [ +] _[ y]_ [)] _[,]_



_y_

_x_ + _y_ [+] _[ x]_ [ =] _[ −]_ _x_ + _[xy]_



this recovers the Feynman integral for the bubble graph. By extending the integral to the
full region, _x_ + _y_ _≤_ 0, we recover not just this bubble integral, but the full amplitude!


**6.3** **Example:** **the** **planar** **1-loop** **3-point** **amplitude**


For a more complicated planar example, consider the 1-loop planar 3-point amplitude, with
the fatgraph Γ, in Figure 30. There are nine curves on this graph: three curves _Ci,i_ +2,
connecting external lines _i, i_ + 2; three curves _Ci,i_, which loop around and come back to
external line _i_ ; and three curves _Ci,_ 0 that start from the external line _i_ and end in a spiral
around the closed loop.
In the planar sector, a convenient way to assign momenta is to use _dual_ _variables_ . Let _zi_ _[µ]_
( _i_ = 1 _,_ 2 _,_ 3) be dual variables for the external lines, and _z_ 0 be the dual variable for the closed
loop. Then curves from external lines _i_ to _j_ have


_Xi,j_ = ( _zj_ _−_ _zi_ ) [2] + _m_ [2] _,_ (6.19)


whereas a curve from _i_ that ends in a spiral around the loop has


_Xi,_ 0 = ( _zi −_ _z_ 0) [2] + _m_ [2] _._ (6.20)


If the external momenta are _p_ 1 _, p_ 2 _, p_ 3, then we can take _z_ 1 = 0 _, z_ 2 = _p_ 1 _, z_ 3 = _p_ 1 + _p_ 2. The
closed loop variable, _z_ 0, can be used as a loop momentum variable.
The 3-point one-loop planar amplitude is then




  _A_ = _d_ _[D]_ _z_ 0







_d_ **t** _Z,_ (6.21)




 - _ti≥_ 0


- 45 

**Figure** **30** : A fatgraph for the 3-point 1-loop planar amplitude.


where (taking cyclic indices mod 3)



3


_αi,iXi,i_ +

_i_ =1



3


_αi,_ 0 _Xi,_ 0 _._ (6.22)

_i_ =1




_−_ log _Z_ =



3


_αi,i_ +2 _Xi,i_ +2 +

_i_ =1



The headlight functions for these curves are


_αi,_ 0 = _ti_ + _gi_ +1 _−_ _gi,_ (6.23)

_αi,i_ +2 = _gi −_ _fi −_ _fi_ +1 _,_ (6.24)

_αi,i_ = _fi_ +1 + _hi −_ _gi −_ _gi_ +1 _,_ (6.25)


where


_fi_ = max(0 _, ti_ ) _,_ (6.26)


_gi_ = max(0 _, ti, ti_ + _ti_ +1) _,_ (6.27)


_hi_ = max(0 _, ti, ti_ + _ti_ +1 _, ti_ + _ti_ +1 + _ti_ +2) _._ (6.28)


**6.4** **Note** **on** **factorization**


The integrands defined by curve integrals factorise in the correct way. Take again the curve

integral


                 - _d_ _[E]_ _t_
_I_ = (6.29)
MCG _[Z.]_


In Appendix B, we show that the residue at _XC_ = 0 is given by


                   - _dE−_ 1 _t_
Res _XC_ =0 _I_ = _[Z][′][,]_ (6.30)
MCG _[′]_


                   - 46                    

which is now the curve integral for the fatgraph Γ _C_, obtained by cutting Γ along _C_ . In this
formula, MCG _[′]_ is the MCG of Γ _C_, and the momentum _PC_ _[µ]_ [of] [the] [curve] _[C]_ [is] [put] [on] [shell.] [In]
the fatgraph Γ _C_, the curve _C_ gives two new boundaries, which are assigned momenta _±PC_ _[µ]_ [.]
For example, before loop integration, the non-planar 1-loop fatgraph Γ has loop integrand



_∞_


_αnXn_
_n_ = _−∞_







_._ (6.31)




  _I_ = _dxdy_ exp





_−_



Here, the momenta of the curves are _Pn_ _[µ]_ [=] _[ℓ][µ]_ [+] _[nk][µ]_ [.] Consider the _X_ 0 = 0 pole. The
parameter _α_ 0 vanishes outside _x_ _≥_ 0. In this region, the only non-vanishing parameters are
_α_ 1 and _α−_ 1. The residue at _X_ 0 = 0 is then


               Res _X_ 0=0 _I_ = _dy_ exp           - _−α_ 1 _[′]_ _[X]_ [1] _[−]_ _[α]_ _−_ _[′]_ 1 _[X][−]_ [1]           - _,_ (6.32)


where the restriction to _x_ = 0 gives _α_ 1 _[′]_ [= max(0] _[, y]_ [) and] _[ α]_ _−_ _[′]_ 1 [=] _[ y][−]_ [max(0] _[, y]_ [).] [This is the] _[ n]_ [ = 4]
tree level amplitude, with external momenta are _k, ℓ, −k, −ℓ_, and _ℓ_ _[µ]_ . The two propagators
are _X_ 1 = ( _k_ + _ℓ_ ) [2] + _m_ [2] and _X−_ 1 = ( _k −_ _ℓ_ ) [2] + _m_ [2] .


**7** **Amplitude** **Curve** **Integrals**


Following the previous section, the curve integral formula for the full amplitude is




  - _d_ _[E]_ **t**
_A_ =
MCG



��� _d_ _[D]_ _ℓa_ exp( _−S_ ( **t** )) _._ (7.1)



The loop integration variables, _ℓa_, appear quadratically in the curve action _S_ ( **t** ). So, if we
perform the loop integral _before_ performing the curve integral over the _ti_, it is a Gaussian
integral. The result is a curve integral




  - _d_ _[E]_ **t**
_A_ =
MCG




- _πL_

_U_




- _[D]_ 2 - exp _−_ _[F]_ [0] _,_ (7.2)

_U_ _[−Z]_



where _U, F_ 0 and _Z_ are homogeneous polynomials in the _αC_ ’s that we call _surface_ _Symanzik_
_polynomials_ .

The curve integral (7.2) resembles the Schwinger form of a single Feynman integral, but

it integrates to the full amplitude. Once again, it is important to mod out by the action of

the mapping class group, to ensure that the integral does not overcount Feynman diagrams.
We now summarise how to compute the surface Symanzik polynomials, _U, F_ 0 _, Z_ . Suppose
that a choice of loop momentum variables, _ℓ_ _[µ]_ _a_ [,] [has] [been] [fixed.] [The] [momentum] [assigned] [to] [a]
curve _C_ is of the form
_PC_ _[µ]_ [=] _[ K]_ _C_ _[µ]_ [+]              - _h_ _[a]_ _C_ _[ℓ][µ]_ _a_ _[,]_ (7.3)

for some integers _h_ _[a]_ _C_ [.] [These] _[h][a]_ _C_ [geometrically] [can] [be] [understood] [in] [terms] [of] [intersections]
between _C_ and a basis of _L_ closed curves on the fatgraph. Using the _h_ _[a]_ _C_ [intersection numbers,]
define an _L × L_ matrix

       _A_ _[ab]_ = _h_ _[a]_ _C_ _[h][b]_ _C_ _[α][C][,]_ (7.4)

_C_


                   - 47                    

and a _L_ -dimensional vector (with momentum index _µ_ )


       _B_ _[a,µ]_ = _h_ _[a]_ _C_ _[α][C][K]_ _C_ _[µ]_ _[.]_ (7.5)

_C_


The then surface Symanzik polynomials are



_U_ = det _A,_ _FU_ 0 [=] _[ B]_ _µ_ _[a]_ - _A_ _[−]_ [1][�]



_ab_ _[B][b,µ][,]_ _Z_ = - _αC_ - _KC_ [2] [+] _[ m]_ [2][�] _._ (7.6)

_C_



_Z_ =    _ab_ _[B][b,µ][,]_



These arise in the usual way by performing the Gaussian integral, as discussed in detail in

Appendix C.

In fact, the surface Symanzik polynomials have simple expressions when expanded as a
sum of monomials. For a set of curves, _S_ = _{C_ 1 _, ..., CL}_, write _αS_ for the corresponding
monomial



_αS_ =



_L_


_αCi._ (7.7)
_i_ =1



The determinant, det _A_, can be expanded to give


_U_ =              

_S_ cuts Σ
to disk



_αS,_ (7.8)



where we sum over all sets _S_ whose curves cut Γ down to a tree fatgraph. In other words, _U_

is the sum over all _maximal_ _cuts_ of the graph Γ. Moreover, using the Laplace expansion of
the matrix inverse, _F_ 0 can be expanded to find



�2
_,_ (7.9)



_F_ 0 = 
_S_ _[′]_ cuts Σ
to 2 disks



_αS′_



��

_KC_ _[µ]_
_C∈S_ _[′]_



where the sum in this formula is now over sets _S_ _[′]_ of _L_ + 1 curves that factorise Γ into two

disjoint tree graphs. Each monomial in the sum is multiplied by the total momentum flowing

through the factorisation channel.

A complete derivation of (7.8) and (7.9) is given in Appendix C.


**7.1** **Example:** **the** **planar** **1-loop** **propagator**


We return to the planar 1-loop propagator (Sections 4.6, 5.6, 6.2). Of the four curves
_C_ 1 _, C_ 2 _, S_ 1 _, S_ 2, only _S_ 1 and _S_ 2 carry loop momentum and cut Γ open to a tree. The first
surface Symanzik polynomial is therefore


_U_ = _αS_ 1 + _αS_ 2 _._ (7.10)


The _B_ -vector is
_B_ _[µ]_ = _αS_ 2 _k_ _[µ]_ _,_ (7.11)


                   - 48                    

so that the second surface Symanzik polynomial is


_F_ 0 = _αS_ [2] 2 _[k]_ [2] _[.]_ (7.12)


Finally,
_Z_ = _m_ [2] ( _αS_ 1 + _αC_ 1 + _αC_ 2) _._ (7.13)


The amplitude is then given by the curve integral




   _A_ =


_x_ + _y≥_ 0



_D_

_dxdy_ - _αS_ 1 + _π_ _αS_ 2 - 2 exp - _αSα_ 1 _S_ +2 _k α_ [2] _S_ 2 _−_ _m_ [2] ( _αS_ 1 + _αC_ 1 + _αC_ 2)� _._ (7.14)



This again recovers the formula (6.15), which we obtained by direct integration in the previous

section.


**7.2** **Example:** **the** **non-planar** **1-loop** **propagator**


We return to the non-planar 1-loop propagator (Sections 4.4 and 5.4). The momentum of the
curve _Cn_ is


_Pn_ _[µ]_ [=] _[ ℓ][µ]_ [ +] _[ np][µ][.]_ (7.15)


Every curve _Cn_ cuts Γ to a tree graph with 4 external legs. So the first Symanzik polynomials
is



_U_ =



_∞_


_αn,_ (7.16)
_n_ = _−∞_



where _αn_ is the headlight function for _Cn_ . Every pair of distinct curves _Cn, Cm_ cuts Γ into
two trees, and so



_F_ 0 =



_∞_

 
_nmαnαmp_ [2] _._ (7.17)
_n,m_ = _−∞_



Finally,


The amplitude is then



_Z_ =



_∞_


_αn_ ( _m_ [2] + _n_ [2] _p_ [2] ) _._ (7.18)
_n_ = _−∞_




  - _dxdy_
_A_ =
MCG




- _π_
_U_



_D_  -  
- 2 exp _−_ _[F]_ [0] _._ (7.19)

_U_ _[−Z]_




- 49 

The MCG acts on the fan in this case as **g** _n_ _�→_ **g** _n_ +1. A fundamental domain for this action
is clearly the positive orthant, spanned by **g** 0 _,_ **g** 1. In this orthant, the surface Symanzik
polynomials are


_U_ = _x_ + _y,_ (7.20)

_F_ 0 = _y_ [2] _p_ [2] _,_ (7.21)

_Z_ = _xm_ [2] _._ (7.22)


So we find




- _D/_ 2 - - ��
exp _m_ [2] _−_ _[y]_ [2] _,_ (7.23)

_x_ + _y_ _[−]_ _[x]_




   _A_ =


_x,y≥_ 0




  - _π_
_dxdy_
_x_ + _y_



where we have put _p_ _[µ]_ on shell, _p_ [2] + _m_ [2] = 0. Or, equivalently,




- _D/_ 2 - _[xy]_ exp _−p_ [2] _._ (7.24)

_x_ + _y_ _[−]_ _[m]_ [2][(] _[x]_ [ +] _[ y]_ [)]




   _A_ =


_x,y≥_ 0




  - _π_
_dxdy_
_x_ + _y_



**7.3** **Example:** **The** **non-planar** **3-point** **amplitude**


Even at 1-loop, it is not always easy to identify the fundamental domain of the MCG. To see

the problem, consider the non-planar one-loop 3-point amplitude. Let the first trace factor
have external particle _p_ _[µ]_ 1 [,] [and] [the] [second] [trace] [factor] [have] _[p][µ]_ 2 [and] _[p][µ]_ 3 [.] The curves, _Cij_ _[n]_ [,]
connecting a pair of distinct start and end points, _i, j_, are labelled by the number of times,
_n_, they loop around the graph. The curves _C_ 22 and _C_ 33 begin and end at the same edge, and
are invariant under the MCG. Then, for a specific choice of loop momentum variable, we find

the momentum assignments


_P_ 12 _[n]_ [=] _[ np]_ 1 _[µ][,]_ _P_ 13 _[n]_ [=] _[ np]_ 1 _[µ]_ _[−]_ _[p]_ 2 _[µ][,]_ _P_ 22 = 0 _,_ _P_ 33 = 0 _._ (7.25)


We can readily give the curve integral formula for the amplitude,




  - _dxdydz_
_A_ =
MCG




- _π_
_U_



_D_ - 
- 2 exp _−_ _[F]_ [0] _,_ (7.26)

_U_ _[−Z]_



where the surface Symanzik polynomials are



_α_ 22 + _α_ 33 +







_U_ =



_∞_ 

_α_ 13 _[n]_ [+] _[ α]_ 12 _[n]_ _[,]_ _F_ 0 = _B_ _[µ]_ _B_ _[µ]_ _,_ _Z_ = _m_ [2]
_n_ = _−∞_



_∞_




_∞_


_α_ 12 _[n]_
_n_ = _−∞_



_._ (7.27)



In the formula for _F_ 0, the _B_ -vector is



_B_ _[µ]_ =



_∞_


_np_ _[µ]_ 1 _[α]_ 12 _[n]_ [+ (] _[np]_ 1 _[µ]_ _[−]_ _[p]_ 2 _[µ]_ [)] _[α]_ 13 _[n]_ _[.]_ (7.28)
_n_ = _−∞_


    - 50     

However, at this point we confront the problem of quotienting by MCG. The MCG is

generated by


**g** 12 _[n]_ _[�→]_ **[g]** 12 _[n]_ [+1] _[,]_ **[g]** 13 _[n]_ _[�→]_ **[g]** 13 _[n]_ [+1] _[,]_ (7.29)


and it leaves **g** 22 and **g** 33 invariant. Naively, we might want to quotient by the MCG by
restricting the integral to the region spanned by: **g** 12 [0] _[,]_ **[ g]** 13 [0] _[,]_ **[ g]** [22] _[,]_ **[ g]** [33][.] [However,] [this] [region] [is]
too small. It does not include any full cones of the Feynman fan. We could also try restricting
the integral to the region spanned by: **g** 12 [0] _[,]_ **[ g]** 13 [0] _[,]_ **[ g]** 12 [1] _[,]_ **[ g]** 13 [1] _[,]_ **[ g]** [22] _[,]_ **[ g]** [33][.] [But] [this] [region] [is] [too] [large!]
The amplitude has _three_ Feynman diagrams, but this region contains _four_ cones, so it counts

one of the diagrams twice.

As this example shows, it is already a delicate problem to explicitly specify a fundamental

domain for the MCG action.


**7.4** **Example:** **genus-one** **2-loop** **amplitudes**



The problem of modding by MCG becomes even more acute for non-planar amplitudes. The

genus one 2-loop vacuum amplitude, considered in Section 5.7, is computed by a 3-dimensional
curve integral. But the MCG action in this case is an action of SL2Z. The action on _g_ -vectors
is of the form







**g** _p/q_ _�→_ **g** ( _ap_ + _bq_ ) _/_ ( _cp_ + _dq_ ) _,_ for




_a_ _b_

_c_ _d_



_∈_ SL2Z _._ (7.30)



For the vacuum amplitude, a simple example of a fundamental region is the region spanned
by **g** 1 _/_ 0 _,_ **g** 0 _/_ 1 _,_ and **g** 1 _/_ 1. However, for the _n_ -point genus one 2-loop amplitude, identifying a
fundamental region of this SL2Z-action becomes very difficult.
In the next section, we present a simple method to compute the integrals in our formulas,

for any MCG action.


**8** **Modding** **Out** **by** **the** **Mapping** **Class** **Group**


Our formulas for amplitudes and integrands take the form of integrals over R _[E]_ modulo the

action of the Mapping Class Group, MCG,


                 - _d_ _[E]_ _t_
_A_ = (8.1)
MCG _[f]_ [(] _[t]_ [)] _[,]_


for some MCG-invariant function, _f_ ( _t_ ). One way to evaluate this integral is to find a fun
damental domain for the MCG action. But it is tricky to identify such a region in general.
Instead, it is convenient to mod out by the MCG action by defining a kernel, _K_, such that


                _A_ = _d_ _[E]_ _t K_ ( _t_ ) _f_ ( _t_ ) _._ (8.2)


In this section, we find kernels, _K_, that can be used at all orders in perturbation theory, for

all Mapping Class Groups.


                   - 51                    

**8.1** **Warm** **up**


Consider the problem of evaluating an integral modulo a group action on its domain. For
example, suppose _f_ ( _x_ ) is invariant under the group of translations, _T_, generated by _x �→_ _x_ + _a_,

for some constant, _a_ . We want to evaluate an integral




  _I_ =


R _/T_



_dxf_ ( _x_ ) _._ (8.3)



One way to do this is to restrict to a fundamental domain of _T_ :


_a_

                 


_I_ =



_dxf_ ( _x_ ) _._ (8.4)

0



But we can alternatively find a kernel _K_ ( _x_ ) such that


_∞_

                


_I_ =



_dx K_ ( _x_ ) _f_ ( _x_ ) _._ (8.5)

_−∞_



One way to find such a kernel is to take a function _g_ ( _x_ ) with finite support around 0, say.

Then we can write



1 =




- _∞_
_n_ = _−∞_ _[g]_ [(] _[x][ −]_ _[na]_ [)]

- _∞_ (8.6)
_n_ = _−∞_ _[g]_ [(] _[x][ −]_ _[na]_ [)] _[,]_



provided that [�] _n_ _[∞]_ = _−∞_ _[g]_ [(] _[x][ −]_ _[na]_ [)] [is] [nowhere] [vanishing.] [Inserting] [this] [into] [(][8.3][),]




       _I_ =


R _/T_


So that we can use



_dx_



_∞_

- _∞n_ = _−∞_ _[g]_ [(] _[x][ −]_ _[na]_ [)] - _g_ ( _x_ )

- _∞_ _dx_ - _∞_ (8.7)
_n_ = _−∞_ _[g]_ [(] _[x][ −]_ _[na]_ [)] _[f]_ [(] _[x]_ [) =] _n_ = _−∞_ _[g]_ [(] _[x][ −]_ _[na]_ [)] _[f]_ [(] _[x]_ [)] _[.]_

_−∞_


_g_ ( _x_ )
_K_ ( _x_ ) =   - _∞_ (8.8)
_n_ = _−∞_ _[g]_ [(] _[x][ −]_ _[na]_ [)]



as a kernel to quotient out by the translation group. For example, suppose that we take
_g_ ( _x_ ) = Θ( _x_ + _a_ )Θ( _−x_ + _a_ ), where Θ( _x_ ) is the Heaviside function. Inserting this into (8.7)

gives



_a_




_I_ =





_dx_ [1]

2

_−a_



(8.9)
2 _[f]_ [(] _[x]_ [)] _[.]_



The domain of this integral contains two copies of a fundamental domain for _T_, but this is
compensated for by the 1 _/_ 2 coming from _K_ ( _x_ ) to give the correct answer.


                   - 52                    

**8.2** **A** **Tropical** **Mirzakhani** **kernel**


The headlight functions, _αC_, give a very natural solution to the problem of defining an
integration kernel, _K_ .
Consider the case when MCG has _one_ _generator_ . Let _S_ be the set of curves which are

_not_ invariant under MCG. The sum of their headlight functions,


       _ρ_ = _αC,_ (8.10)


_C∈S_


is itself a MCG-invariant function. Moreover, _ρ_ does not vanish on any top-dimensional cone
(because no diagram can be formed without using at least one propagator from _S_ ). So we

can consider inserting the function


1 = _[ρ]_ (8.11)

_ρ_


into our integrals.
The set _S_ is the disjoint union of cosets under the MCG action, by the Orbit-Stabilizer

theorem. When MCG has a single generator, these cosets are easy to describe. MCG does
not alter the endpoints of curves. So if _Cij_ _∈S_ is a curve connecting external lines _i_ and _j_,
the orbit of _Cij_ is a coset of _S_ . By the Orbit-Stabalizer theorem, these cosets are disjoint. So
_ρ_ can be resumed as




 _ρ_ =


_i,j_





_αγCij_ _._ (8.12)
_γ∈_ MCG



Given this, we can mod out by the MCG action by defining



_K_ = 

_i,j_



_αCij_ (8.13)

_ρ_ _[,]_



where we choose a distinguished representative, _Cij_, for each coset. We call (8.13) a _tropical_
_Mirzakhani_ _kernel_, because it is a tropical version of the kernel introduced by Mirzakhani to
compute Weil-Petersson volumes [23]. Each headlight function, _αCij_, is non-vanishing in a
convex region _VCij_ that is spanned by all the cones in the fan that contain **g** _Cij_ . These regions
_over-count_ the diagrams, but this over-counting is corrected by the kernel, _K_ .


**8.3** **Example:** **the** **non-planar** **1-loop** **propagator**


As a sanity check, let us repeat the calculation of the non-planar 1-loop propagator from

Section 7.2, but now using the tropical Mirzakhani kernel. The MCG has one generator, and
no curves are MCG-invariant. So take the set _S_ to be the set of all curves, _Cn_, and write



_∞_

 
_ρ_ = _αn._ (8.14)

_n_ = _−∞_


  - 53  

Choose _C_ 0, say, as the coset representative (all other curves are in the orbit of _C_ 0). Then the
tropical Mirzakhani kernel, (8.13), is
_K_ = _[α]_ [0] (8.15)

_ρ_ _[.]_


Using this kernel, we find a pre-loop-integration integrand,



_∞_


_αiXi_

_i_ = _−∞_







_._ (8.16)




  _I_ = _dxdy K_ ( _x, y_ ) exp





_−_



The headlight functions for this example were given in (5.33). In particular, _α_ 0 = max(0 _, x_ ),
which is vanishing outside of the region _x_ _≥_ 0. In this region, the only other non-vanishing

headlight functions are


_α−_ 1 = max(0 _, y_ ) and _α_ 1 = _−y_ + max(0 _, y_ ) _._ (8.17)


The formula is therefore




  _I_ =


_x≥_ 0



_x_
_dxdy_ (8.18)
_x_ + _|y|_ [exp (] _[−][α][−]_ [1] _[X][−]_ [1] _[ −]_ _[α]_ [0] _[X]_ [0] _[ −]_ _[α]_ [1] _[X]_ [1][)] _[ .]_



We can now perform the loop integral. Recall that _Xn_ = ( _ℓ_ + _nk_ ) [2] + _m_ [2] . Using this, the
exponent, _Z_, in (8.18) is


_−_ log _Z_ = _ρ ℓ_ [2] + 2 _ℓ_ _· k_ ( _α_ 1 _−_ _α−_ 1) + _m_ [2] _α_ 0 _._ (8.19)


The Gaussian integral gives



_D_

- 2 - _|y|_ [2] exp _k_ [2] _._ (8.20)

_x_ + _|y|_ _[−]_ _[m]_ [2] _[x]_




  _A_ =


_x≥_ 0



_x_
_dxdy_
_x_ + _|y|_




- _π_
_x_ + _|y|_



This doesn’t immediately look like the Feynman integral for the 1-loop bubble. However,

writing


2 _x_ _[x][ −]_ _[y]_ (8.21)
_x_ + _y_ [= 1 +] _x_ + _y_ _[,]_


we find



_D_

- 2 - _y_ [2] exp _k_ [2] _._ (8.22)

_x_ + _y_ _[−]_ _[m]_ [2] _[x]_




   _A_ =


_x,y≥_ 0




  - _π_
_dxdy_
_x_ + _y_



since the integrand over _x, y_ _≥_ 0 is even under _x ↔_ _y_, whereas _x −_ _y_ is odd. This is still not

exactly the same as the conventional integral. To recover the conventional form, note that

the exponent can be rewritten as


_xy_

_−_ _[y]_ [2] (8.23)

_x_ + _y_ _[−]_ _[x]_ [ =] _x_ + _y_ _[−]_ [(] _[x]_ [ +] _[ y]_ [)] _[.]_


                   - 54                    

**8.4** **General** **Tropical** **Mirzakhani** **Kernels**


Tropical Mirzakhani kernels can be defined to _any_ mapping class group, with more than one

generator. Fix some fatgraph Γ, with mapping class group MCG.

A conceptually simple way to define a kernel is to consider the set of _L_ -tuples of curves

that cut Γ to a tree graph. These define the _first_ _Symanzik_ _polynomial_,



_U_ = 

_S_
cuts to tree



_αS,_ (8.24)



which can also be computed as a determinant of a matrix (Section 7). This function does not

vanish on top-dimensional cones of the Feynman fan, since every diagram contains a subset

of propagators that cut Γ to a tree. We can therefore insert

1 = _[U]_ (8.25)

_U_


into our integrals. Under the MCG action, the set of _L_ -tuples appearing in _U_ is partitioned

into cosets. Each coset represents an MCG-inequivalent way of cutting Γ down to a tree. By

choosing a representative _L_ -tuple for each such loop cut, we arrive at a kernel



_K_ = 

distinct loop cuts



_αS_

(8.26)
_U_ _[.]_



Our integrals can then be computed as a sum over maximal cuts:



_A_ = - _d_ _[E]_ _y_ [=] MCG _[I]_

distinct loop cuts




_d_ _[E]_ _y_ _[α][S]_ (8.27)

_U_ _[I][.]_



The disadvantage of this formula is that it can be difficult to systematically identify a set of

MCG-inequivalent maximal cuts.


**8.5** **The** **General** **Iterative** **Method**


A more systematic way to quotient out by MCG is to break the MCG-action one generator

at a time. This iterative method has the advantage of being completely algorithmic.

To apply the method, pick a trace-factor of Γ, _β_, which has some external particles,
1 _, ..., m_ . Let _Sβ_ be the set of curves that have at least one endpoint in _β_, excluding any
curves that are MCG-invariant, and write


       _ρβ_ = _αC._ (8.28)

_C∈Sβ_


_ρβ_ is MCG-invariant. This is because the MCG action does not alter the endpoints of a
curve. The set _Sβ_ therefore has a coset decomposition. For each MCG orbit in _Sβ_, pick a
representative curve, so that




 
_αγCi,_ (8.29)
_γ∈_ MCG(Σ)


- 55 


_ρβ_ =



_k_



_i_ =1


for some _k_ = _|Sβ/_ MCG(Σ) _|_ coset representatives _C_ 1 _, ..., Ck_ . We give more details about how
to pick a set of coset representatives below.
Every top-dimensional cone is generated by at least _one_ curve from the set _Sβ_, because
otherwise that cone would not correspond to a complete triangulation of Γ. This means that
_ρβ_ is non-vanishing everywhere, except on some lower-dimensional cones. Away from this
vanishing locus, we can write

1 = _[ρ][β]_ _._ (8.30)

_ρβ_


Given this, we define a tropical Mirzakhani kernel



_Kβ_ =



_k_



_i_ =1



_αCi_ _._ (8.31)

_ρβ_



This has the effect of breaking the MCG symmetry of the integrand, and reducing us to

evaluating simpler integrals. In particular, we have




  - _d_ _[E]_ _t_
_A_ = [=]
MCG _[I]_



_k_



_i_ =1




- _d_ _[E]_ _t_ _αCi_ _I,_ (8.32)
Stab( _Ci_ ) _ρβ_



where Stab( _Ci_ ) _≤_ MCG is the _stablizer_ _subgroup_ for _Ci_ . The factor

_αCi_ (8.33)

_ρβ_


is _itself_ invariant under Stab( _Ci_ ). So the integrals,


               - _d_ _[E]_ _t_ _αCi_ (8.34)
Stab( _Ci_ ) _ρ_ _[I][,]_


can themselves be evaluated by finding a Mirzkhani kernel for the new group, Stab( _Ci_ ). This
iterative method ultimately yields an integral with no group action,


               - _d_ _[E]_ _y_               _A_ = [=] _d_ _[n]_ _y K I,_ (8.35)
MCG _[I]_


where _K_ is a sum of products of kernels of the form (8.33).

To complete the description of the iterative method, we describe how to choose coset
representatives from the set _Sβ_ . The curves in this set break into two subsets, as in Figure
31:


1. Curves _C_ whose endpoints lie in two distinct trace factors. These curves cut Γ to a
fatgraph Γ _C_ which has one fewer trace factors.


2. Curves _C_ with both endpoints in the same trace factor. These curves cut Γ to a fatgraph
Γ _C_ with one lower genus.


                   - 56                    

**Figure** **31** : The two types of curves that are not invariant under the MCG, drawn here on

the surface _S_ (Γ) associated to a fatgraph: curves connecting distinct trace factors (right),

and topologically nontrivial curves that begin and end on the same trace factor (left).


Both of these subsets have decompositions into cosets specified by the endpoints of the curves.
So, for every pair of particles, _i, j_ (with _i_ in trace factor _β_ ), pick _any_ curve _Cij_ [0] [connecting]
them. These can be taken as coset representatives. The caveat is that, if _i, j_ are both in trace
factor _β_, we must choose a curve _Cij_ [0] [which] [is] [not] [MCG-invariant.] [An] [MCG-invariant] [curve]
generates a trivial coset. The first step to break the MCG is then to insert the kernel






_i∈β_






_j_



_αij_ [0]
_._ (8.36)

_Sβ_ _[α][C]_



For amplitudes involving a large number of external particles, this iterative method
naively requires a lot of work (growing like _n_ _[L]_ with the number of particles, _n_ ). However,

this apparent complexity goes away completely if we choose an appropriate fatgraph, Γ, for

our calculation. We use this to obtain simple formulas for amplitudes at all- _n_ in a separate

paper, [26]. But for now we will focus on low-point amplitudes, to illustrate the method in

its simplest form.


**8.6** **Example:** **the** **genus** **one** **2-loop** **vacuum** **amplitude**


As an example, we briefly describe what happens for the genus one 2-loop vacuum amplitude
(Sections 5.7 and 7.4). The MCG is now SL2Z. In this case, there is only _one_ coset to
consider, since every curve is related to every other by



**g** _p/q_ _�→_ **g** ( _ap_ + _bq_ ) _/_ ( _cp_ + _dq_ ) _,_ for




- _a_ _b_

_c_ _d_



_∈_ SL2Z _._ (8.37)



For the first step of the iteration, we can take any curve, say _C_ 1 _/_ 0, as a coset representative.
The kernel for the first step is
_α_ 1 _/_ 0
_K_ 1 _/_ 0 =            - _._ (8.38)
_C_ _[α][C]_


                   - 57                    

The subgroup that leaves _C_ 1 _/_ 0 invariant is




  
: _n ∈_ Z



_<_ SL2Z _._ (8.39)



Stab _C_ 1 _/_ 0 =



�� 1 _n_

0 1



The curves compatible with _C_ 1 _/_ 0 form a single coset for the action of this subgroup. So, for
the second step, we can choose just one of them, _C_ 0 _/_ 1, say, as a coset representative. The
kernel for the second step is
_α_ 0 _/_ 1
_K_ 0 _/_ 1 =            - (8.40)

_[,]_
_C_ _[′][ α][C][′]_

where we sum only over curves, _C_ _[′]_, that are non-intersecting with _C_ 1 _/_ 0. The final kernel is
simply
_α_ 1 _/_ 0 _α_ 0 _/_ 1
_K_ = _,_ (8.41)
_α_ 1 _/_ 0 + _α_ 0 _/_ 1 + _α_ 1 _/_ 1 + _α−_ 1 _/_ 1 _α_ 0 _/_ 1 + _α_ 1 _/_ 1 + _α−_ 1 _/_ 1


where the simplification arises because _C_ 1 _/_ 1 and _C−_ 1 _/_ 1 are the only curves compatible with
both _C_ 1 _/_ 0 and _C_ 0 _/_ 1.


**9** **Examplitudes**


We now show how to use the tropical Mirzakhani kernels to evaluate curve integrals. We give

detailed low-dimensional examples of amplitudes up to 3 loops.


**9.1** **The** **non-planar** **1-loop** **3-point** **amplitude**


The formula for the 1-loop non-planar 3-point amplitude was given in Section 7.3. However,

we did not show how to quotient by the MCG. Using the tropical Mirzakhani kernel, we now

find the formula




  -   - _π_
_A_ = _d_ [3] _t K_
_U_



_D_ - 
- 2 _F_ 0
exp _,_ (9.1)
_U_ _[−Z]_



where the Mirzakhani kernel is



12 [+] _[ α]_ 13 [0]
_K_ = _[α]_ [0] _,_ (9.2)
_ρ_



with _ρ_ the sum over all _αC_ (except for those curves which are invariant under the MCG,
namely _C_ 22, _C_ 33). The surface Symanzik polynomials are, as before,



_α_ 22 + _α_ 33 +







_U_ =



_∞_ 
- _α_ 13 _[n]_ [+] _[ α]_ 12 _[n]_ _[,]_ _F_ 0 = _BµB_ _[µ]_ _,_ _Z_ = _m_ [2]

_n_ = _−∞_



_∞_




_∞_


_α_ 12 _[n]_
_n_ = _−∞_



_._ (9.3)



In the formula for _F_ 0, the _B_ -vector is



_B_ _[µ]_ =



_∞_


_np_ _[µ]_ 1 _[α]_ 12 _[n]_ [+ (] _[np]_ 1 _[µ]_ _[−]_ _[p]_ 2 _[µ]_ [)] _[α]_ 13 _[n]_ _[.]_ (9.4)
_n_ = _−∞_


    - 58     

Let us first see why (9.2) is a Mirzakhani kernel. The MCG has one generator. It leaves
_C_ 22 and _C_ 33 invariant, but acts non-trivially on the set _{C_ 12 _[n]_ _[, C]_ 13 _[n]_ _[}]_ [of] [all] [curves] [that] [connect]
the first trace factor to the second trace factor. _ρ_ is the sum of _αC_ for all these curves,



_ρ_ =



_∞_


( _α_ 12 _[n]_ [+] _[ α]_ 13 _[n]_ [)] _[ .]_ (9.5)
_n_ = _−∞_



This set has two MCG cosets, labelled by the start and end points of the curves. We can
take _C_ 12 [0] [and] _[C]_ 13 [0] [as] [the] [two] [coset] [representatives.] _[C]_ 12 [0] [,] [for] [instance,] [represents] [the] [coset] [of]
all curves that begin at 1 and end at 2. (Recall Section 8.)
Naively, it looks as if (9.1) involves infinitely many _αC_, which it would be laborious to
compute. However, the Mirzakhani kernel ensures that only a few _αC_ are needed. To see how
this works, consider, say, the first term in the kernel,

_K_ 12 = _[α]_ 12 [0] (9.6)
_ρ_ _[.]_


In the region where _α_ 12 [0] [= 0,] [all] [other] _[α][C]_ [are] [vanishing,] [except] [for:]


_α_ 12 _[−]_ [1] _[,]_ _[α]_ 12 [1] _[,]_ _[α]_ 13 [0] _[,]_ _[α]_ 13 [1] _[,]_ _[α]_ [22] _[.]_ (9.7)


So in this region, _U_ and _B_ _[µ]_ simplify to


_U_ = _α_ 12 [0] [+] _[ α]_ 12 [1] [+] _[ α]_ 12 _[−]_ [1] [+] _[ α]_ 13 [0] [+] _[ α]_ 13 [1] _[,]_ (9.8)

_B_ _[µ]_ = _−k_ 1 _[µ][α]_ 12 _[−]_ [1] _[−]_ _[k]_ 2 _[µ][α]_ 13 [0] [+ (] _[k]_ 1 _[µ]_ _[−]_ _[k]_ 2 _[µ]_ [)] _[α]_ 13 [1] _[.]_ (9.9)


When we compute these _α_ ’s, using the matrix method, we find that they become simple
functions in the region _x_ _>_ 0, where _α_ 12 [0] [is] [non-zero.] In this region, we have _α_ 12 [0] [=] _[x]_ [.]
Moreover, the remaining 5 headlight functions become


_α_ 13 [1] [=] _[ −]_ [max(0] _[, y]_ [) + max(0] _[, y, y]_ [ +] _[ z]_ [)] _[,]_ _α_ 13 [0] [= max(0] _[, y]_ [)] _[,]_ (9.10)

_α_ 12 [1] [=] _[ −][y][ −]_ [max(0] _[, z]_ [) + max(0] _[, y, y]_ [ +] _[ z]_ [)] _[,]_ _α_ 12 _[−]_ [1] [=] _[ −][z]_ [ + max(0] _[, z]_ [)] _[,]_ (9.11)

_α_ 22 = _−_ max(0 _, y, y_ + _z_ ) + max(0 _, y_ ) + max(0 _, z_ ) _._ (9.12)


These are precisely the headlight functions for the 5-point tree amplitude! We could have
anticipated this, because cutting Γ along _C_ 12 [0] [yields a 5-point tree graph.] [Using these tree-like]
headlight functions, we can compute the contribution of _K_ 12 to the curve integral, (9.1). The
contribution from the second term in the Mirzakhani kernel is similar.
In this example, we find that we only need to know the headlight functions _αC_ for _tree_
_level_ amplitudes, in order to compute the full 1-loop amplitude! In fact, we can prove that
this happens _in_ _general_ . Suppose a monomial, _αS_ (for some set of _L_ curves _S_ ), appears in
the numerator of the kernel _K_ . In the region where _αS_ = 0, all remaining _αC_ ’s simplify to
become headlight functions for the tree-fatgraph obtained by cutting Γ along all the curves

in _S_ . This general phenomenon is computationally very useful, and we study it in greater

detail elsewhere.


                   - 59                    

**9.2** **The** **genus** **one** **2-loop** **vacuum** **amplitude**


We have already mentioned the 2-loop genus one vacuum computation in Sections 5.7 and

7.4. We now have all the tools to compute it properly. The result is the following simple

integral




- _[D]_ 2
exp ( _−Z_ ) _,_ (9.13)




  _A_ =


_R_




   - _π_ 2
_dxdydz K_

_U_



where the kernel is (as given in Section 8.6)


_α_ 1 _/_ 0
_K_ =
_α_ 1 _/_ 0 + _α_ 0 _/_ 1 + _α_ 1 _/_ 1 + _α−_ 1 _/_ 1


and now with surface Symanzik polynomials



_α_ 0 _/_ 1
_,_ (9.14)
_α_ 0 _/_ 1 + _α_ 1 _/_ 1 + _α−_ 1 _/_ 1



_U_ = det _A,_ (9.15)

_Z_ = _m_ [2] ( _α_ 1 _/_ 0 + _α_ 0 _/_ 1 + _α_ 1 _/_ 1 + _α−_ 1 _/_ 1) _._ (9.16)


Note that the region, _R_, where _α_ 1 _/_ 0 _α_ 0 _/_ 1 = 0 is, in the coordinates of Section 5.7, given by
_w, x_ _≤_ 0 and _x_ + 2 _z_ _≤_ 0. The curve integral is restricted by the Mirzakhani kernel to this

region.

To see how this curve integral comes about, we need to understand how to assign momenta

to the curves. The easiest way to assign momenta is to use the homology of curves on the
torus, Section 3.3.1. Assign the A-cycle momentum _ℓ_ 1 and the B-cycle momentum _ℓ_ 2. The
curve _Cp/q_ wraps the A-cycle _q_ times and the _B_ -cycle _p_ times, and so it has momentum
_pℓ_ 1 + _qℓ_ 2 giving
_Xp/q_ = ( _pℓ_ 1 + _qℓ_ 2) [2] + _m_ [2] _._ (9.17)


With this momentum assignment, the matrix _A_, which records the dependence on chosen

basis of loops, is







_A_ _[ab]_ =




_α_ 1 _,_ 0 + _α_ 1 _,_ 1 + _α−_ 1 _,_ 1 _α_ 1 _,_ 1 _−_ _α−_ 1 _,_ 1
_α_ 1 _,_ 1 _−_ _α−_ 1 _,_ 1 _α_ 0 _,_ 1 + _α_ 1 _,_ 1 + _α−_ 1 _,_ 1



_._ (9.18)



Moreover, the momentum assigned to the curves has no non-loop part, so that


_Z_ = _m_ [2][ �] _αC,_ (9.19)


_C_


which restricts to (9.16) in the region _R_ .

We now evaluate the amplitude. Once again, we will be aided by a striking simplification

of the headlight parameters. The headlight parameters were given in Section 5.7. But in the
region _R_, _α_ 1 _/_ 1 and _α−_ 1 _/_ 1 simplify to become tree-like headlight functions:


_α_ 1 _/_ 1 = max(0 _, −z_ ) and _α−_ 1 _/_ 1 = max(0 _, z_ ) _._ (9.20)


                   - 60                    

This corresponds to the fact that cutting Γ along _C_ 1 _/_ 0 and _C_ 0 _/_ 1 gives a 4-point tree graph.
Moreover, in this region,


_α_ 1 _/_ 0 = _−w,_ and _α_ 0 _/_ 1 = _−x −_ 2 max(0 _, z_ ) _,_ (9.21)


and so


_α_ 1 _/_ 0 + _α_ 0 _/_ 1 + _α_ 1 _/_ 1 + _α−_ 1 _/_ 1 = _−w −_ _x −_ _z_ (9.22)

_α_ 0 _/_ 1 + _α_ 1 _/_ 1 + _α−_ 1 _/_ 1 = _−x −_ _z._ (9.23)


Moreover, _U_ and _Z_ become


_U_ = det _A_ = _wx_ + _zw −_ ( _x_ + 2 max(0 _, z_ )) _|z|,_ and _Z_ = _−m_ [2] ( _w_ + _x_ + _z_ ) _._ (9.24)


So the vacuum amplitude is




- _[D]_ 2
exp   - _m_ [2] ( _w_ + _x_ + _z_ )� _._ (9.25)




  _A_ =


_R_



_dwdxdz_ _[w]_ [(] _[x]_ [ + 2 max(0] _[, z]_ [))]

( _w_ + _x_ + _z_ )( _x_ + _z_ )




- _π_ 2

_U_



It is not obvious that this is the correct answer. In the conventional calculation, the

amplitude receives just a single contribution: the vacuum sunset Feynman diagram. Our

formula resembles, but is not the same, as the Schwinger parameterisation for this diagram.
To see that they are equivalent, note that _R_ can be divided into two regions: one where _z_ _≥_ 0
and another where _z_ _≤_ 0. By a simple change of variables, the integral over either one of

these regions can be written as




- _[D]_ 2
exp   - _−m_ [2] ( _a_ + _b_ + _c_ )� _._ (9.26)




   _I_ =


_a,b,c≥_ 0



_ab_
_dadbdc_
( _a_ + _b_ + _c_ )( _b_ + _c_ )




- _π_ [2]


_ab_ + _bc_ + _ca_



However, summing over the 6 possible permutations of _a, b, c_, note that


_ab_

[of] _[a, b, c]_ [) =] _[ a]_ [ +] _[ b]_ [ +] _[ c.]_ (9.27)
_b_ + _c_ [+ (permutations]


It follows that _I_ is 1 _/_ 6 times the sunset integral with the usual parameterisation. Integrating

over all of _R_, we then recover that




- _[D]_ 2
exp   - _−m_ [2] ( _x_ + _y_ + _|z|_ )� _._ (9.28)




   - _π_ [2]
_dxdydz_

_xy_ + _y|z|_ + _|z|x_



_A_ = [1]

3




 

_x,y,z≥_ 0



This is 1 _/_ 3 times the vacuum sunset integral. The factor of 1 _/_ 3 corresponds to the fact that
the fatgraph has _|_ Aut(Γ) _|_ = 3.


                   - 61                    

**Figure** **32** : A planar 2-loop tadpole graph.


**9.3** **The** **planar** **2-loop** **tadpole**


We can compute the planar 2-loop tadpole amplitude using the fatgraph Γ in Figure 32.

The curves on this fatgraph can be labelled by their endings. We have two loop boundaries,
labelled 2 _,_ 3 in the Figure. The curves are then _C_ 23 _, C_ 22 _, C_ 33 _, C_ 12 _[n]_ _[, C]_ 13 _[n]_ [,] [where] _[n]_ [indexes] [how]
many times the curves _C_ 12 _[n]_ _[, C]_ 13 _[n]_ [loop] [around] [before] [beginning] [their] [spiral.] [As] [usual,] [we] [will]
only need a small number of these curves to compute the amplitude.
Because Γ is planar, we can introduce dual variables _z_ 1 _[µ][, z]_ 2 _[µ][, z]_ 3 _[µ]_ [to] [parametrise] [the] [mo-]
menta of the curves. The propagator factors are then


_X_ 12 _[n]_ [= (] _[z]_ [2] _[−]_ _[z]_ [1][)][2][ +] _[ m]_ [2] _[,]_ _X_ 13 _[n]_ [= (] _[z]_ [3] _[−]_ _[z]_ [1][)][2][ +] _[ m]_ [2] _[,]_ _X_ 23 = ( _z_ 3 _−_ _z_ 2) [2] + _m_ [2] _._ (9.29)


It is convenient to take _z_ 3 _−_ _z_ 1 and _z_ 2 _−_ _z_ 1 as our loop momentum variables.
The curve integral for the amplitude is then




  -   - _π_ 2
_A_ = _d_ [4] _t K_

_U_




- _[D]_ 2
exp( _−Z_ ) _,_ (9.30)


        


where




         _U_ = det _A,_ and _Z_ = _m_ [2]



( _α_ 12 _[n]_ [+] _[ α]_ 13 _[n]_ [)]
_n_



_._ (9.31)




   _α_ 23 + _α_ 22 + _α_ 33 +



Moreover, using the momenta assignments from the dual variables, (9.29), _A_ is the 2 _×_ 2

matrix







_A_ =




_α_ 23 + [�] _n_ [1] = _−_ 1 _[α]_ 12 _[n]_ _α_ 23
_α_ 23 _α_ 23 + [�] _n_ [1] = _−_ 1 _[α]_ 13 _[n]_



_._ (9.32)



_U_ is the determinant of _A_, and each monomial in this determinant corresponds to a pair
of curves that cut Γ to a 5-point tree graph. Using the fact that _αCαD_ = 0 if _C, D_ intersect,
we find



_U_ =



_∞_




_n_ = _−∞_




- _α_ 23 _α_ 12 _[n]_ [+] _[ α]_ [23] _[α]_ 13 _[n]_ [+] _[ α]_ 12 _[n]_ _[α]_ 13 _[n]_ [+] _[ α]_ 12 _[n]_ _[α]_ 13 _[n]_ [+1] - _._ (9.33)


     - 62      

**Figure** **33** : A maximal cut of the planar 2-loop tadpole graph. The curve _C_ 12 [0] [cuts] [Γ] [to] [a]
3-point 1-loop graph, and the curve _C_ 23 cuts this further to a 5-point tree graph.


Here, we have chosen a convention for the index _n_ such that _C_ 12 _[n]_ _[, C]_ 13 _[n]_ [+1] are compatible, but
_C_ 12 _[n]_ _[, C]_ 13 _[n][−]_ [1] intersect. The MCG has one generator, which acts on the index _n_ . So it is clear
that the monomials in _U_ can be decomposed into four cosets (corresponding to the four terms

in the sum). We therefore get a Mirzakhani kernel (of the type discussed in Section 8.4)


_K_ = _[U]_ [0] (9.34)

_U_ _[,]_


with
_U_ 0 = _α_ 23 _α_ 12 [0] [+] _[ α]_ [23] _[α]_ 13 [0] [+] _[ α]_ 12 [0] _[α]_ 13 [0] [+] _[ α]_ 12 [0] _[α]_ 13 [1] _[.]_ (9.35)


In the region where _U_ 0 = 0, only 12 _αC_ ’s are non-vanishing. In fact, each monomial in _U_ 0
defines a maximal cut of Γ, which cuts Γ to a 5-point tree graph. See Figure 33. _A_ is the

sum of four terms,


_A_ = _AC_ 23 _,C_ 120 [+] _[ A][C]_ [23] _[,C]_ 13 [0] [+] _[ A][C]_ 12 [0] _[,C]_ 13 [0] [+] _[ A][C]_ 12 [0] _[,C]_ 13 [1] _[,]_ (9.36)


each corresponding to a different maximal cut of the fatgraph.
For instance, _AC_ 23 _,C_ 120 [is] [given] [by] [the] [curve] [integral] [over] [the] [region] _[α]_ [23] _[α]_ 12 [0] [=] [0.] [In] [this]
region, only 5 other _αC_ ’s are non-vanishing. The curves correspond to the five curves on the
5-point tree graph obtained by cutting along _C_ 23 _, C_ 12 [0] [.] [The 5 curves compatible with] _[ C]_ [23] _[, C]_ 12 [0]
are
_C_ 12 [1] _[,]_ _[C]_ 12 _[−]_ [1] _[,]_ _[C]_ 13 [0] _[,]_ _[C]_ 13 [1] _[,]_ _[C]_ [22] _[.]_ (9.37)


In this region, the headlight functions simplify, so that, similar to the previous examples, the

curve integral only sees the headlight functions of the 5-point tree-level problem. Explicitly,
in coordinates, we can take (in this region) _α_ 23 = _w,_ _α_ 12 [0] [=] _[x]_ [,] [and] [the] [remaining] [headlight]


                   - 63                    

**Figure** **34** : Three loop.


functions take the form of tree-level headlight functions (see Figure 33):


_α_ 13 [1] [=] _[ f]_ [2] _[−]_ _[f]_ [1] _[−]_ _[z,]_ _α_ 13 [0] [=] _[ f]_ [1] _[−]_ _[y,]_ (9.38)

_α_ 22 = _f_ 2 _−_ _f_ 3 _,_ _α_ 12 [1] [=] _[ f]_ [3] _[,]_ (9.39)

_α_ 12 _[−]_ [1] [=] _[ f]_ [1][ +] _[ f]_ [3] _[ −]_ _[f]_ [2] _[.]_ (9.40)


where
_f_ 1 = max(0 _, y_ ) _,_ _f_ 2 = max(0 _, z, y_ + _z_ ) _,_ _f_ 3 = max(0 _, z_ ) _._ (9.41)


So, in this region, the _A_ matrix restricts to







_A_ _[′]_ =




_w_ + _f_ 1 _−_ _f_ 2 + 2 _f_ 3 _w_
_w_ _w_ + _f_ 2 _−_ _y −_ _z_



_,_ (9.42)



and _Z_ restricts to
_Z_ _[′]_ = _m_ [2] ( _w_ + _x −_ _y −_ _z_ + _f_ 1 + _f_ 2 + _f_ 3) _._ (9.43)


The contribution of this term to the amplitude is then




- _[D]_ 2
exp( _−Z_ _[′]_ ) _._ (9.44)




     _AC_ 23 _,C_ 120 [=]

_w,x≥_ 0



_wx_
_dwdxdydz_
det _A_ _[′]_




- _π_ [2]

det _A_ _[′]_



The other 3 cuts are similarly computed.


**9.4** **The** **planar** **3-loop** **vacuum** **amplitude**


We now consider a 3-loop example. The 3-loop vacuum amplitude can be computed using

the 3-loop fatgraph, Γ, in Figure 34. The curves on Γ all begin and end in a spiral. There are

four loop boundaries, labelled _a_ = 1 _,_ 2 _,_ 3 _,_ 4 in the Figure, that the curves can spiral around.
Let _Cab_ _[δ]_ [be] [the] [curves] [that] [begin] [spiralling] [around] _[a]_ [,] [and] [end] [spiralling] [around] _[b]_ [.] [There] [are]


                   - 64                    

infinitely many such curves, all related by the action of the MCG. In fact, the MCG action
in this case is quite complicated: it is an action of the braid group _B_ 3. However, using a
tropical Mirzakhani kernel, we can still compute the amplitude.

The momentum assignment to the curves is easy to describe, because Γ is a planar graph.
Introduce dual momentum variables, _za_ _[µ]_ [, associated to the four boundaries,] _[ a]_ [ = 1] _[,]_ [ 2] _[,]_ [ 3] _[,]_ [ 4.] [Then]
the propagator for _Cab_ _[δ]_ [is] [just]
_Xab_ = ( _zb_ _[µ]_ _[−]_ _[z]_ _a_ _[µ]_ [)][2][ +] _[ m]_ [2] _[.]_ (9.45)


We can choose any three _za_ to be our loop momentum variables.
Our formula for the amplitude is then




  -   - _π_ 3
_A_ = _d_ [6] _t K_

_U_




- _[D]_ 2
exp( _−Z_ ) _,_ (9.46)



where the surface Symanzik polynomials are


_U_ = det _[′]_ _A,_ [˜] _Z_ = _m_ [2][ �] _αab_ _[δ]_ _[.]_ (9.47)


Here, we take a slightly different approach to presenting _U_, adapted to the planar case, by
using a reduced determinant, det _[′]_, which excludes a row and column. The 4 _×_ 4 matrix _A_ [˜] is
(for _a ̸_ = _b_ )



_A_ ˜ _ab_ = 


_αab_ _[δ]_ _[,]_ _A_ ˜ _aa_ = _−_  _δ_ _c_ = _a_




- _A_ ˜ _ac._ (9.48)


_c_ = _a_



By the matrix-tree theorem, the reduced determinant, det _[′]_ _A_ [˜], turns into a sum over all maxi
mal cuts of the fatgraph Γ. In this case, a maximal cut is given by any three non-intersecting
curves, _{Cab_ _[δ]_ _[, C]_ _cd_ _[δ][′]_ _[, C]_ _ef_ _[δ][′′][}]_ [,] [such] [that] [the] [pairs,—] _[ab]_ [,] _[cd]_ [,] _[ef]_ [,—span] [a] [tree] [on] [the] [set] _[{]_ [1] _[,]_ [ 2] _[,]_ [ 3] _[,]_ [ 4] _[}]_ [.]
So det _[′]_ _A_ [˜] indeed recovers the definition of _U_ as the sum over maximal cuts of the fatgraph.

Explicitly, it takes the form

      -       _U_ = _α_ _[δ]_ _[α][δ][′]_ _[α][δ][′′]_ (9.49)







_δ,δ_ _[′]_ _,δ_ _[′′]_





_αab_ _[δ]_ _[α]_ _cd_ _[δ][′]_ _[α]_ _ef_ _[δ][′′]_ (9.49)
trees



We can now use this formula for _U_ to define a Mirzakhani kernel, _K_ . This set of triples
appearing in _U_ can be decomposed as a sum of cosets under the MCG. The MCG-action leaves

the starts and ends of each curve unchanged. So we find that there are 16 MCG-inequivalent
maximal cuts of Γ, corresponding to the 4 [2] distinct labelled trees in the set _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ . For

each such labelled tree, we choose a coset representative.


_αab_ [0] _[α]_ _cd_ [0] _[α]_ _ef_ [0] _[,]_ (9.50)


where the pairs _ab, cd, ef_ define the tree, and _Cab_ [0] _[, C]_ _cd_ [0] _[, C]_ _ef_ [0] [is some choice of 3 non-intersecting]
curves. Let _U_ 0 be the sum of monomials for these 16 coset representatives. It has the form



_U_ [0] = 


_α_ 14 _α_ 24 _α_ 34 _._ (9.51)

4 perms




 - 
_α_ 12 _α_ 23 _α_ 34 +

12 perms 4




- 65 

Then
_K_ = _[U]_ [0] (9.52)

_U_


is our Mirzakhani kernel.

An exercise in the intersection rules for mountainscapes shows that the following 6 curves

are sufficient to build each of the 16 maximal cuts:


_C_ 14 [0] [= (] _[xRyR]_ [)] _[∞][x]_ [(] _[LvLwLuLx]_ [)] _[∞][,]_ (9.53)

_C_ 24 [0] [= (] _[uRyRvRzR]_ [)] _[∞][u]_ [(] _[LxLvLwLu]_ [)] _[∞][,]_ (9.54)

_C_ 34 [0] [= (] _[wRzR]_ [)] _[∞][w]_ [(] _[LuLxLvLw]_ [)] _[∞][,]_ (9.55)

_C_ 12 [0] [= (] _[yRxR]_ [)] _[∞][y]_ [(] _[LuLzLvLy]_ [)] _[∞][,]_ (9.56)

_C_ 23 [0] [= (] _[zRuRyRvR]_ [)] _[∞][z]_ [(] _[LwLz]_ [)] _[∞][,]_ (9.57)

_C_ 13 [0] [= (] _[RyRx]_ [)] _[∞][LvR]_ [(] _[zLwL]_ [)] _[∞][.]_ (9.58)


This is because all of these curves are pairwise compatible. Using these curves, we can define
a restricted matrix (for _a ̸_ = _b_ )


_A_ ˜ [0] _ab_ [=] _[ α]_ _ab_ [0] _[,]_ _A_ ˜ [0] _aa_ [=] _[ −]_          - _A_ ˜ [0] _ac_ (9.59)

_c_ = _a_


so that, by the matrix-tree theorem, _U_ [0] = det _[′]_ _A_ [˜][0] . Our Mirzakhani kernel is then


_[A]_ [˜][0]
_K_ = [det] _[′]_ _._ (9.60)

det _[′]_ _A_ [˜]


For each of the 16 monomials in _U_ [0] we get a contribution to _A_ . For instance, take the

monomial
_α_ 12 [0] _[α]_ 23 [0] _[α]_ 34 [0] _[,]_ (9.61)


corresponding to the tree 1 _−_ 2 _−_ 3 _−_ 4. The associated contribution to _A_ only involves _αC_
for curves _C_ compatible with this maximal cut. This maximal cut gives a tree fatgraph, with
colour ordering (123432). [5] So this contribution to the amplitude involves only the 9 headlight

functions for this 6-point tree fatgraph.
Finally, note that by permutation symmetry (with respect to the dual variables _za_ ), we
only really need to evaluate two of the maximal cuts in our formula, say:


_α_ 12 [0] _[α]_ 23 [0] _[α]_ 34 [0] and _α_ 14 [0] _[α]_ 24 [0] _[α]_ 34 [0] _[.]_ (9.62)


Then
_A_ = 12 _A_ 12 _,_ 23 _,_ 34 + 4 _A_ 14 _,_ 24 _,_ 34 _,_ (9.63)


where each of _A_ 12 _,_ 23 _,_ 34 and _A_ 14 _,_ 24 _,_ 34 can be computed knowing only the headlight functions
for a 6-point tree graph.


5Cutting a curve that ends in a spiral around a loop boundary creates a new external line on that boundary.


                   - 66                    

**10** **A** **First** **Look** **at** **Recursion**


The tropical Mirzakhani kernels dramatically simplify the task of evaluating our amplitudes.

Using these kernels, our formulas for amplitudes at _L_ loops end up expressed in terms of
the headlight functions, _αC_, that we have already computed for lower loop level amplitudes.
In this section, we show an alternative way to apply the Mirzakhani kernels to compute
amplitudes, by using them to define a powerful recursion relation for the integrands, _I_ .

Fix a fatgraph Γ. Its associated (pre-loop-integration) integrand is given by the curve

integral








  - _d_ _[n]_ _t_
_I_ = _Z_ = exp
MCG _[Z,]_





_−_ - _αCXC_


_C_



_._ (10.1)



To evaluate the curve integral, we introduce a tropical Mirzakhani kernel, as above. Take, for
example, some trace factor _β_ . The non-separating curves with endpoints on Γ form a set _Sβ_,
and which can be partitioned into MCG orbits with some coset representatives _C_ 1 _, . . ., Ck_ .
Each of these curves, _Ci_, cuts Γ to a fat graph Γ _Ci_ with a smaller number of loops. The
Mirzakhani kernel _Kβ_ then gives



_I_ =



_k_



_i_ =1




- _d_ _[n]_ _t_ _αCi_ (10.2)
MCG _ρ_ _[Z.]_



Introducing an auxiliary parameter, _ξ_, the 1 _/ρ_ can be incorporated into the exponential using



1
_ρ_ [=]



_∞_


_dξ e_ _[−][ρξ]_ _._ (10.3)

0



Equation (10.2) then implies the following recursion formula:



_I_ =



_∞_


_dξ_

0



_k_



_i_ =1




_−_ 1

_[I]_ [Γ] _[Ci]_ [(] _[X]_ _C_ _[′]_ [)] _[,]_ (10.4)
( _XCi_ + _ξ_ ) [2]



where the new dual variables _XC_ _[′]_ [appearing] [in] [the] [integrand] _[I]_ [Γ] _Ci_ [(] _[X]_ _C_ _[′]_ [)] [are] [given] [by]



_XC_ _[′]_ [=]




_XC_ + _ξ_ if _C_ _∈Sβ_
(10.5)
_XC_ else.



This formula, (10.4), is a completely recursive way to obtain the rational functions _I_ to all

orders in the perturbation series. A detailed derivation of (10.4) is given in Appendix D.

For example, consider again the 1-loop non-planar propagator computed in Section 7.2.
The curves on Γ are _S_ = _{Cn}_ as before, and their associated dual variables are


_Xn_ = ( _ℓ_ + _nk_ ) [2] _._ (10.6)


                   - 67                    

The MCG has just one generator, and so we will only need to apply the global forward limit
once. Taking _C_ 0 as our coset representative, (10.4) gives



_I_ Γ =



_∞_

- _−_ 1

_dξ_ _[I]_ [Γ] _[C]_ [0] [(] _[X]_ [1][ +] _[ ξ, X][−]_ [1][ +] _[ ξ]_ [)] _[,]_ (10.7)
( _X_ 0 + _ξ_ ) [2]
0



where Γ _C_ 0 is the 4-point tree graph obtained by cutting Γ along _C_ 0. The curves _C_ 1 and _C−_ 1
become the two possible propagators of Γ _C_ 0: on Γ, _C_ 1 and _C−_ 1 are the only two curves that
do not intersect _C_ 0. So we have,



_I_ Γ = _−_



_∞_

- - 1 1 1 1

_dξ_
( _X_ 0 + _ξ_ ) [2] _X_ 1 + _ξ_ [+] ( _X_ 0 + _ξ_ ) [2] _X−_ 1 + _ξ_
0




_._ (10.8)



Evaluating the _ξ_ integral gives the following formula for the integrand:


1 1
_I_ Γ = (10.9)
_X_ 0( _X_ 1 _−_ _X_ 0) [+] _X_ 0( _X−_ 1 _−_ _X_ 0) _[.]_


Here we see the appearance of _linearised_ _propagators_, of the form 1 _/_ ( _XC_ _−_ _XCi_ ). Such
linearised propagators have arisen in previous studies of forward limit [27–32]. In the full sum,

these linearised propagators sum to give back the ordinary loop integrand after identifications

made using shifts of the loop momenta. In our current example, the loop momentum shift
_ℓ_ _�→_ _ℓ_ + _k_ shifts the dual variables by _Xn_ _�→_ _Xn_ +1. Applying this shift to the second term in
(10.9) gives


1 1 1
_I_ Γ _[′]_ [=] _._ (10.10)
_X_ 0( _X_ 1 _−_ _X_ 0) [+] _X_ 1( _X_ 0 _−_ _X_ 1) [=] _X_ 0 _X_ 1


For higher loop integrands, we can use multiple iterations of (10.4) to write _I_ as a sum over

some tree amplitudes, with various shifts in the kinematic variables.
Note that the recursion, (10.4), continues to hold even when the _XC_ variables are not
all distinct. For example, if all _XC_ are set equal to a constant, _XC_ = _X_, then _I_ Γ = _C_ Γ _/X_ _[E]_,
where _C_ Γ is the number of Feynman diagrams contributing to the amplitude. In this case,
(10.4) can be used to recursively compute the number of diagrams. Moreover, the recursion

(10.4) also holds when there are higher poles in the integrand, arising from diagrams like

bubbles. We give a more complete analysis of these recursions elsewhere.


**11** **Outlook**


The new representation of all-loop amplitudes we have studied in this paper has implications

far beyond our understanding of scalar amplitudes, and has consequences for the understand
ing of particle and string scattering generally. We highlight a number of directions that are

especially primed for immediate development.


                   - 68                    

The magic of the _curve integral_ formulas is that integrals over an _O_ ( _n_ ) dimensional space,
of an action built from _O_ ( _n_ [2] ) piecewise linear functions, automatically reproduces the full
amplitudes, which are conventionally sums over _O_ (4 _[n]_ ) Feynman diagrams. The novelty of

this formalism over conventional field theory must therefore become most manifest in the
limit _n_ _→∞_ of a large number of particles. In examples, we have found evidence that

the external kinematical data can be chosen so that the large- _n_ limits the curve integrals

are smooth, leading to formulas for amplitudes in the large- _n_ limit in terms of _tropical_ _path_

_integrals_ . Studying this limit might lead to a new understanding of the emergence of strings

from colored particles at strong coupling. At strong coupling, the scattering for a small

number of particles is exponentially small, and the amplitude is instead dominated by the

emission of a huge number of particles, approximating field configurations that should more

continuously connect to a string worldsheet picture.

Even at finite _n_ the curve integral formalism offers radically new methods to compute

amplitudes. For instance, it allows to evaluate amplitudes numerically by direct integration,

thus avoiding the generation of Feynman diagrams altogether. The geometric properties of

the fan suggest a new search for an optimal numerical integration strategy, uplifting recent

breakthroughs in the numerical evaluation of Feynman integrals in parametric form to entire

amplitudes [33, 34].

A second frontier ripe for immediate investigation is an understanding of gravity and
gravity-like amplitudes. Just as the tr _ϕ_ [3] theory is a model for general colored amplitudes,
a scalar model for gravity is given by an uncolored scalar _σ_ with cubic self-interaction _σ_ [3] .

In special cases, it is now standard to think of uncolored and colored theories as related by
double-copy or ‘gravity = gauge [2] ’ formulas [35]. The stringy origin of these formulas, the

KLT relations, is deeply connected to thinking about the string worldsheet in a fundamentally

_complex_ fashion as a Riemann surface with a complex structure. But there are many reasons

why our formulation of uncolored amplitudes will involve a very different sort of treatment. As

we alluded to in the introduction, the existence of _σ_ is forced on us in the most elementary way

by the structure of the Feynman fan, which has lower-dimensional ‘holes’ that are beautifully

completed by adding in new vectors corresponding to _σ_ particles. This does not remotely
have the flavor of ‘gravity = gauge [2] ’. Moreover, as alluded to in the introduction, the _u_ 
variables central to our story are deeply connected to the string wordsheet (and Teichm¨uller

space), but via _hyperbolic_ _geometry_ and _not_ through the conventional picture of Riemann

surfaces with complex structure. All of this dovetails nicely with the many observations, in

examples of gravity amplitudes, that there is vastly more structure to gravity amplitudes
than is suggested by the ‘gravity=gauge [2] ’ slogan. The striking way in which _σ_ is forced on

us in our story is a new departure point for uncovering more of this hidden structure.

Finally, our results here strongly suggest that there is way to describe fundamental par
ticle physics in the real world from a more elementary starting point, with spacetime and

quantum mechanics appearing as emergent principles. We believe that we have taken a ma
jor new step in this direction with the results we have begun to introduce in this paper. A

number of major challenges remain before we can reach this goal. The first is to understand


                   - 69                    

how fermions arise from this new perspective, which has so far only been applied to bosonic

scattering. For Standard Model physics, describing chiral fermions will be especially inter
esting and important. Another challenge is that the key structures in our formulas stem

from a fatgraph, which is most immediately connected to the adjoint representation of _U_ ( _N_ )

gauge theories. But the quantum numbers of the Standard Model are more interesting. For

instance, in the _SO_ (10) grand unified theory, the matter lives in ten fundamentals (higgses)

together with three **16** ’s for the fermions. How might the amplitudes for matter in these

representations emerge from elementary combinatorial foundations?


**Acknowledgments**


We especially thank Song He and Thomas Lam for countless stimulating conversations on the topics
of this paper over many years. We also thank Sebastian Mizera and Hofie Hannesdottir for many
discussions, and Song He, Carolina Figueiredo, Daniel Longenecker, Qu Cao and Jin Dong for ongoing
interactions related to the material of this paper over the past year. NAH is supported by the DOE
under grant DE-SC0009988; further crucial contributions to his work were made possible by the Carl
B. Feinberg cross-disciplinary program in innovation at the IAS. NAH also expresses sincere thanks
to HF, PGP, GS and HT for restraining themselves from strangling him during the completion of
this work. PGP is supported by ANR grant CHARMS (ANR-19-CE40-0017) and by the Institut
Universitaire de France (IUF). PGP worked on this project while participating in _Representation_
_Theory:_ _Combinatorial_ _Aspects_ _and_ _Applications_ at the Centre for Advanced Study, Oslo. HF is
supported by Merton College, Oxford. During this project HF received additional support from ERC
grant GALOP (ID: 724638). During this project GS was supported by Brown University, Providence,
the Perimeter Institute, Waterloo, and the Institute for Advanced Study, Princeton. GS was also
funded by the European Union’s Horizon 2020 research and innovation programs _Novel_ _structures_ _in_
_scattering_ _amplitudes_ (No. 725110) of Johannes Henn. GS thanks the groups of C. Anastasiou and
N. Beisert at ETH Zurich for hospitality during the worst phase of the COVID-19 pandemic. HT was
supported by NSERC Discovery Grant RGPIN-2022-03960 and the Canada Research Chairs program,
grant number CRC-2021-00120.


**A** **Deriving** **the** **Curve** **Integral** **Formula**


To see why (6.3) is correct, let us write the amplitude explicitly. Write


_XC_ = _PC_ [2] [+] _[ m]_ [2] (A.1)


for the propagator factor associated to curve _C_ (with momentum _PC_ _[µ]_ [).] [Fix] [some] [fatgraph] [Γ] [with]
some color factor _C_ Γ. The associated partial amplitude can be expressed with just one overall loop
integration as






_C_



_L_

  _A_ = - _d_ _[D]_ _ℓi_


_i_ =1



��


Γ _[′]_







1
_XC_



_,_ (A.2)



where sum over exactly one of every fatgraph Γ _[′]_ that has color factor _C_ Γ _[′]_ = _C_ Γ. The integrand in this
formula can be written as an integral over _curve space_, _V_ . To do this, recall that every top dimensional


                   - 70                    

cone of the Feynman fan corresponds to some triangulation of Γ. Any vector **g** _∈_ _V_ Γ can be expanded
as a sum of the generators of the cone that it is in using


**g** =                 - _αC_ ( **g** ) **g** _C,_ (A.3)


_C_


where _αC_ are the headlight functions and **g** _C_ are the _g_ -vectors of the curves, _C_ . Consider the function
on _V_ given by







_Z_ = exp





_−_ - _αC_ ( **t** ) _XC_


_C_



_,_ (A.4)



where the sum in the exponent is over all open curves _C_ . Let _T_ be a triangulation corresponding to
some top-dimensional cone, with curves _C_ 1 _, ..., CE_ . Restricting _Z_ to this cone gives



_E_

- _αCi_ ( **t** ) _XCi_


_i_ =1







_,_ (A.5)



_Z|_ cone = exp





_−_



_E_




which follows from (A.3). Moreover, the generators of this top dimensional cone span a parallelopiped
of unit volume, so there exist corresponding coordinates _y_ 1 _[′]_ _[, ..., y]_ _E_ _[′]_ [such] [that] _[d][E][y]_ [=] _[d][E][y][′]_ [and] [so] [that]
any vector in this cone can be written as



**g** =



_E_

- _yi_ _[′]_ **[g]** _[C]_ _i_ _[.]_ (A.6)


_i_ =1



The integral of _Z_ over this cone is then



_E_



_i_ =1



1
_._ (A.7)
_XC_





=




 - 
_d_ _[E]_ _yZ_ =

cone _≥_ 0







_d_ _[E]_ _y_ _[′]_ exp




- _E_

 - _−yi_ _[′][X][C]_ _i_


_i_ =1



_≥_ 0



It follows from this that the partial amplitude (A.2) can be written as a curve integral over curve
space:




  - _d_ _[E]_ **t**
_A_ =
MCG



_L_


 - _d_ _[D]_ _ℓi Z._ (A.8)


_i_ =1



In this formula, we integrate over curve space modulo the action of the mapping class group. This
ensures that we count each fatgraph Γ only once. We explain how to compute these curve integrals,
with non-trivial MCG actions, in Section 8.


**B** **Factorization** **in** **detail**


In the text, the factorization of the curve integral formula for integrands _I_ is stated in (6.30). This
formula gives the residue of the pole 1 _/XC_ . To derive the formula, there are two possible cases to
consider: either _C_ is MCG-invariant, or not.


                   - 71                    

**B.1** **MCG** **invariant** **curve**


Suppose _C_ is MCG-invariant. The _XC_ pole arises from the part of the integral over the region of
curve space where _αC_ _>_ 0. Since Stab( _C_ ) = MCG(Γ), the MCG action has a well-defined restriction
to this region and we have a well-defined curve integral




   _I_ _[′]_ =


_αC_ _>_ 0



_d_ _[E]_ _t_
(B.1)
MCG _[Z.]_



To compute _I_ _[′]_, take a triangulation containing _C_, with curves _C, D_ 1 _, ..., DE−_ 1. Take coordinates
adapted to this cone:



**g** = _tC_ **g** _C_ +



_n−_ 1

- _t_ _[′]_ _i_ **[g]** _[D]_ _i_ _[.]_ (B.2)


_i_ =1



By the unit volume property, the integration measure is


_d_ _[E]_ _t_ = _dtCd_ _[E][−]_ [1] _t_ _[′]_ _._ (B.3)


In these coordinates, the restriction of _Z_ to this region is






 _,_ (B.4)



_Z|tC_ _>_ 0 = _e_ _[−][t][C]_ _[X][C]_ exp





 _−_ - _αDXD_

_D|C_



where the sum is over _D_ that do not intersect _C_ . For these curves, _αD_ ( **g** + **g** _C_ ) = _αD_ ( **g** ), so that the
only _tC_ -dependence is in the exp( _−tCXC_ ) factor. Write _αD_ _[′]_ [=] _[α][D][|][t]_ _C_ [=0][,] [for] [the] [headlight] [functions]
restricted to _tC_ = 0. _αD_ _[′]_ [is] [the] [headlight] [function] [of] _[D]_ [considered] [as] [a] [curve] [on] [the] [cut] [fatgraph] [Γ] _[C]_ [.]
The _tC_ integral gives



1
_I_ _[′]_ =
_XC_




- _dE−_ 1 _t′_

(B.5)
MCG _[Z][C][,]_



where






 _._ (B.6)



_ZC_ = exp





 _−_ - _αD_ _[′]_ _[X][D]_

_D|C_



The full curve integral _I_ is _I_ = _I_ _[′]_ + _. . .,_ where the _. . ._ has no _XC_ pole. So


                    - _dE−_ 1 _t′_
Res _XC_ =0 _I_ = MCG _[Z][C][,]_ (B.7)


where, on the RHS, _PC_ _[µ]_ [is] [put] [on] [shell] [(] _[X][C]_ _[→]_ [0).]


**B.2** **MCG** **non-invariant** **curve**


If Stab( _C_ ) _<_ MCG, we can use a Mirzakhani kernel to evaluate the 1 _/XC_ pole. We choose _C_ as one
of the coset representatives, so that the Mirzakhani kernel is

_K_ = _[α][C]_ (B.8)

_ρ_ [+] _[ . . . .]_


                   - 72                    

Then

             - _d_ _[E]_ _t_              - _d_ _[E]_ _t_ _αC_

[=] (B.9)
MCG _[Z]_ Stab _C_ _ρ_ _[Z]_ [ +] _[ . . .,]_


where the _. . ._ are all terms without a 1 _/XC_ pole. To guarantee that _XC_ only appears in the first term,
we can choose the other coset representatives _C_ 1 _, ..., CL−_ 1 so that all of these are curves that intersect
_C_ . We can put the 1 _/ρ_ in the numerator, by introducing an auxiliary integration variable _ξ_ :




- _d_ _[E]_ _t_

[=]
MCG _[Z]_



_∞_

- - _d_ _[E]_ _t_

_dξ_ (B.10)
Stab( _C_ ) _[α][C][e][−][ξρ][Z]_ [ +] _[ . . . .]_
0



Changing variables as before, and integrating over _tC_ gives




- _d_ _[E]_ _t_

[=]
MCG _[Z]_



_∞_

- _−_ 1

_dξ_
( _XC_ + _ξ_ ) [2]
0




- _d_ _[E][−]_ [1] _t_ _[′]_

(B.11)
Stab( _C_ ) _[Z]_ _[′]_ [ +] _[ . . .,]_



where _Z_ _[′]_ is obtained from _Z_ by shifting _XD_ _�→_ _XD_ + _ξ_ for all _D_ in the Mirzakhani set. Finally,
integrating over _ξ_, and using



_m_



_i_ =1






_j_ = _i_



1
_Xi_ + _ξ_ [=]



_m_



_i_ =1



1
_Xi_ + _ξ_



1
_,_ (B.12)
_Xj_ _−_ _Xi_



we find

            - _d_ _[E]_ _t_ 1

_[→]_
MCG _[Z]_ _XC_




- _d_ _[E][−]_ [1] _t_ _[′]_

[+] _[ . . .,]_ (B.13)
Stab( _C_ ) _[Z][C]_



where _−_ log _ZC_ is the curve action given by summing over all curves, _D_, compatible with _C_ :


_−_ log _ZC_ =            - _αDXD._ (B.14)


_D_


Note that this calculation does not apply if the integrand has higher poles in _XC_, such as if _XC_
is a bubble propagator for a planar diagram.


**C** **The** **Surface** **Symanzik** **polynomials**



Fixing an assignment of momenta to the curves gives explicit formulas for the all the propagator
factors



_L_

- _h_ _[a]_ _C_ _[ℓ][µ]_ _a_

_a_ =1



2




_XC_ =





_KC_ _[µ]_ [+]



+ _m_ [2] _,_ (C.1)



in terms of one set of loop momentum variables _ℓ_ _[µ]_ _a_ [.] [In] [terms] [of] [these] [loop] [variables,] [the] [curve] [action,]



becomes




_−_ log _Z_ =   - _αCXC,_ (C.2)


_C_


_−_ log _Z_ = _−ℓ_ _[µ]_ _a_ _[A][ab][ℓ][µ]_ _b_ _[−]_ [2] _[B]_ _µ_ _[a][ℓ][µ]_ _a_ _[−Z][,]_ (C.3)


      - 73      

where _A, B, Z_ are all linear functions in the generalised Schwinger parameters:


_A_ _[ab]_ =            - _h_ _[a]_ _C_ _[h][b]_ _C_ _[α][C]_ (C.4)


_C_

_Bµ_ _[a]_ [=]              - _h_ _[a]_ _C_ _[α][C][K][C µ]_ (C.5)

_C_

_Z_ =             - _αC_ ( _KC_ [2] [+] _[ m]_ [2][)] (C.6)

_C_


Performing the Gaussian integral over the _ℓa_ variables, in _D_ dimensions, gives




  - _d_ _[E]_ **t**
_A_ =
MCG




- _πL_


det _A_




- _[D]_ 2
exp  - _−B_ _[T]_ _A_ _[−]_ [1] _B −Z_  - _._ (C.7)



So we identify the surface Symanzik polynomials:

_U_ = det _A,_ and _F_ 0 (C.8)

_U_ [=] _[ B][T][ A][−]_ [1] _[B.]_


These are the formulas used in the main text. In this appendix, we consider the explicit expansions
of _U_ and _F_ 0 in monomials.


**C.1** **The** **first** **surface** **Symanzik**


Since _X_ _[ij]_ is linear in the parameters _αC_, the determinant det _X_ is homogeneous of degree _L_ . For a
set of curves _S_ = _{C_ 1 _, ..., CL}_, let us find the coefficient in det _A_ of the monomial


_αS_ =                  - _αCi._ (C.9)


By the definition of the determinant, this coefficient is


det _A_ = _. . ._ + _αS_ (det _h|S_ ) [2] + _. . ._ _,_ (C.10)


where


det _h|S_ = _ϵi_ 1 _...iLh_ _[i]_ _C_ [1] 1 _[...h]_ _C_ _[i][L]_ _L_ _[.]_ (C.11)


Note that the ordering of the curves _C_ 1 _, ..., CL_ does not matter, because this determinant only enters
the formula for det _A_ as a square.
We now make two observations. Firstly, det _h|S_ is only non-zero if the curves in _S_ cut Γ to a
tree graph. Secondly, for any conventional choice of loop variables (defined below), the determinants
det _h|S_ are all either 0 or _±_ 1. So the result is that _U_ is given by



_U_ = 

_S_ cuts Γ
to tree



_αS._ (C.12)



For the first statement, consider _L_ = 1. Then all curves have momenta of the form


_PC_ = _h_ [1] _C_ _[ℓ]_ [1] [+] _[ K]_ _C_ _[µ]_ _[.]_ (C.13)


If _h_ [1] _C_ [=] [0,] [cutting] [Σ] [along] _[C]_ [breaks] [it] [into] [two] [parts:] [one] [part] [with] _[L]_ [=] [1,] [and] [a] [second] [part] [with]
_L_ = 0 (i.e. a disk). Whereas, if _h_ [1] _C_ [=] [0,] [cutting] [Γ] [along] _[C]_ [cuts] [the] [loop] [open,] [giving] [a] [new] [surface]
with _L_ = 0 (i.e. a disk). So at 1-loop the first Symanzik polynomial is



_U_ = 

_C_ cuts Γ
to tree



_αC_ - _h_ [1] _C_ �2 _._ (C.14)




- 74 

For _L_ _>_ 1, the determinant det _h|S_ is nonzero if and only if the linear transformation (in _H_ 1(Γ _, ∂_ Γ)
from [ _L_ 1] _, ...,_ [ _LL_ ] to [ _C_ 1] _, ...,_ [ _CL_ ] is invertible. By induction from the _L_ = 1 case, this means that the
curves in _S_ cut Γ to a disk. So



_U_ = 

_S_ cuts Γ
to tree



_αS_ (det _h|S_ ) [2] _._ (C.15)



Secondly, it turns out that (det _h|S_ ) [2] is either 0 or 1. We sketch how to prove this by fixing any
genus _g_ fatgraph with _h_ trace-factor components. The loop order of such a fatgraph is


_L_ = 2 _g_ + _h −_ 1 _._ (C.16)


A natural basis of loop-carrying curves can be given by picking some 2 _g_ curves _Ai, Bi_ wrapping the
_A, B_ -cycles of the graph, and _h −_ 1 curves _Ci_ connecting the _h_ trace factors. These give a set, _S_, of _L_
cures that cut Γ to a tree, so (det _h|S_ ) [2] =1. Moreover, we can choose our momentum assignment such
that
_PAi_ = _ℓ_ 2 _i−_ 1 _,_ _PBi_ = _ℓ_ 2 _i,_ _PCi_ = _ℓ_ 2 _g_ + _i._ (C.17)


Now consider the momenta of Dehn twists of these curves. For instance, taking one of the _Ci_, a Dehn
twist _γ_ around one of its trace-factors gives a new curve


_PγCi_ = _PCi_ _± k_ tf _,_ (C.18)



where _k_ tf is the total momentum of the trace factor. Moreover, any product of Dehn twists acting on
a pair of A,B-cycles acts on their momenta as SL2Z:

                 - _ℓ_ 2 _i−_ 1� _�→_ _X_                 - _ℓ_ 2 _i−_ 1� _,_ (C.19)
_ℓ_ 2 _i_ _ℓ_ 2 _i_




- _�→_ _X_ - _ℓ_ 2 _i−_ 1
_ℓ_ 2 _i_




_,_ (C.19)



for some _X_ _∈_ SL2Z. In this way, we find that the momenta of any set, _S_ _[′]_, that cuts Γ to a tree, is
obtained from the momenta of _S_ via translations by non-loop momenta, and SL2Z transformations.
Both of which leave the determinant unchanged:


(det _h|S′_ ) [2] = (det _h|S_ ) [2] = 1 _._ (C.20)


**C.2** **The** **second** **surface** **Symanzik**


The second surface Symanzik polynomial is


_F_ 0

(C.21)
_U_ [=] _[ B][T][ A][−]_ [1] _[B.]_


The Laplace formula evaluates the inverse as


                   - _A_ _[−]_ [1][�] _[ij]_ = [(] _[−]_ [1)] _[i]_ [+] _[j]_ (C.22)

det _A_ _[|][A][|][ij][,]_


where _|A|_ _[ij]_ is the _i, j_ minor. Since _U_ = det _A_,



_F_ 0 = 2 



- _αCαDKC_ _· KD_ 

_C,D_ _i,j_



( _−_ 1) _[i]_ [+] _[j]_ _h_ _[i]_ _C_ _[h][j]_ _D_ _[|][A][|][ij][.]_ (C.23)
_i,j_




- 75 

As above, again write _S_ = _{C_ 1 _, ..., CL}_ for a set of _L_ curves and _αS_ for the associated monomial. The
minors of _A_ are



_|A|ij_ = 

_S_






_C∈S_



_αS_ _|hS|_ _[i]_ _C_ _[|][h][S][|][j]_ _C_ _[,]_ (C.24)
_αC_



where _|hS|_ _[i]_ _C_ [is the (] _[i, C]_ [) minor of the matrix] _[ h][|][S]_ [= [] _[h][i]_ _C_ 1 _[|][...][|][h]_ _C_ _[i]_ _L_ [].] [By the definition of the determinant,]


_L_
�( _−_ 1) _[i]_ _h_ _[i]_ _D_ _[|][h][S][|][i]_ _C_ [= det] _[ h][S]_ _C→D_ _[,]_ (C.25)

_i_ =1


where _SC→D_ is the set obtained from _S_ by replacing _C_ with _D_ . Substituting (C.24) into (C.23), and
using the identity (C.25), gives (after reordering the summations)



�2



_F_ 0 = 2 
_S_ _[′]_
_|S_ _[′]_ _|_ = _L_ +1



_αS_ _′_



��


_C∈S_ _[′]_



�det _hS′\C_ - _KC_ _[µ]_



_,_ (C.26)



where the sum is restricted to sets of _L_ +1 curves _S_ _[′]_ such that _any_ _L_ subset of _S_ _[′]_ gives a nonvanishing
determinant det _hS′\C_ .
We make three observations to simplify this formula.
First, by the previous section, any _L_ -subset of _S_ _[′]_ that has nonvanishing determinant cuts Γ to a
tree graph. It follows that the sum in this formula is over sets _S_ _[′]_ that _factorize_ Γ into two trees!
Secondly, by the previous subsection, since each of the sets _S_ _[′]_ _\C_ cuts Γ to a tree, the determinants
are all
det _hS′\C_ = _±_ 1 _._ (C.27)

In fact, finally, note that both the vectors _h_ _[i]_ _C_ [and] [the] [momenta] _[K]_ _C_ _[µ]_ [are] [defined] [with] [respect] [to]
an orientation of _C_ . For any subset _S_ _[′]_, these orientations can be chosen so that all the determinants
det _hS′\C_ are positive (say). For this choice,


det _hS′\C_ = 1 _._ (C.28)


Combining these three observations, the final formula for _F_ 0 is



�2



_F_ 0 = 
_S_ _[′]_ cuts Γ
to 2 trees



_αS′_



��

_KC_ _[µ]_
_C∈S_ _[′]_



_,_ (C.29)



for an allowed choice of orientations of the momenta _KC_ .


**D** **The** **Recursion** **Formula**


For a fatgraph Γ, the curve integral for integrands is


                   - _d_ _[E]_ _t_
_I_ = (D.1)
MCG _[Z,]_


with


_−_ log _Z_ =            - _αCXC._ (D.2)


_C_


                   - 76                    

For some trace factor _β_ of Γ, we have the set of curves _S_ that have one or two endpoints in _β_ . Under
the MCG, this set has some, say _k_, coset representatives, _Ci_ ( _i_ = 1 _, . . ., k_ ). Then




  - _d_ _[E]_ _t_
_I_ = [=]
MCG _[Z]_



_k_



_i_ =1




- _d_ _[E]_ _t_ _αCi_ (D.3)
Stab( _Ci_ ) _ρ_ _[Z,]_




- _d_ _[E]_ _t_ _αCi_
Stab( _Ci_ ) _ρ_



where



_ρ_ = - _αC._ (D.4)


_C∈S_



Introducing an auxiliary parameter, _ξ_, we re-write this as



_∞_

- - _d_ _[E]_ _t_

_dξ_ (D.5)
MCG _[α][C][i][Z]_ [(] _[ξ]_ [)] _[.]_
0



_I_ =



_k_



_i_ =1



where the new integrand is




- _αC_ ( _XC_ + _ξ_ ) + 

_C∈S_ _D̸∈S_




_−_ log _Z_ ( _ξ_ ) = 


_αDXD._ (D.6)

_D̸∈S_



Integrating over the _αCi_ direction in each term curve integral gives



_∞_

- _−_ 1

_dξ_
( _XCi_ + _ξ_ ) [2]
0



_I_ =



_k_



_i_ =1




- _d_ _[n][−]_ [1] _t_ _[′]_

(D.7)
Stab( _Ci_ ) _[Z]_ _[′]_ [(] _[ξ]_ [)] _[,]_



where




 - _αC_ _[′]_ [(] _[X][C]_ [+] _[ ξ]_ [) +] 
_C∈S,C_ = _Ci_ _D̸∈S_




_−_ log _Z_ _[′]_ ( _ξ_ ) = 



- _αD_ _[′]_ _[X][D][,]_ (D.8)

_D̸∈S_



and _αC_ _[′]_ [are] [the] [headlight] [functions] [obtained] [after] [integrating] [out] [the] **[g]** _[C]_ _i_ [direction.] [These] [are] [the]
headlight functions for the fatgraph Γ _Ci_ obtained by cutting along _Ci_ .
Note that we can evaluate the _ξ_ integral using identities such as



_m_



_i_ =1



1
_Xi_ + _t_ [=]



_m_



_i_ =1



1
_Xi_ + _t_






_j_ = _i_



1
_._ (D.9)
_Xj_ _−_ _Xi_



When all the _XC_ propagator factors are distinct (i.e. there are no higher poles), we can perform the
integral to find




- _d_ _[n][−]_ [1] _t_ _[′]_

(D.10)
Stab( _Ci_ ) _[Z]_ _[′]_ [(] _[−][X][C][i]_ [)] _[,]_



_I_ =



_k_



_i_ =1



1
_XCi_



**E** **Recursion** **Examples**


**E.1** **The** **3-point** **non-planar** **1-loop** **amplitude**


Take Γ to be the 3-point non-planar 1-loop diagram considered in Section 9.1. The curves are
_C_ 12 _[n]_ _[, C]_ 13 _[n]_ _[, C]_ [22] _[, C]_ [33][.] [For] [the] [Mirzakhani] [method,] [we] [have] [two] [cosets,] [with] [representatives] _[C]_ 12 [0] _[, C]_ 13 [0] [.]
Cutting Γ along _C_ 12 [0] [gives] [a] [5-point] [tree] [fatgraph] [Γ] _C_ 12 [0] [.] [The] [curves] [compatible] [with] _[C]_ 12 [0] [are]


_C_ 12 [1] _[, C]_ 13 [0] _[, C]_ 12 _[−]_ [1] _[, C]_ 13 _[−]_ [1] _[, C]_ [22] _[.]_ (E.1)


                   - 77                    

The global forward limit then computes _I_ Γ as


1
_I_ Γ = _X_ 12 [0] _I_ Γ _C_ 120 [(] _[X]_ 12 [1] _[−]_ _[X]_ 12 [0] _[, X]_ 13 [0] _[−]_ _[X]_ 12 [0] _[, X]_ 12 _[−]_ [1] _[−]_ _[X]_ 12 [0] _[, X]_ 13 _[−]_ [1] _[−]_ _[X]_ 12 [0] _[, X]_ [22][) + (2] _[ ↔]_ [3)] _[.]_ (E.2)


But the 5-point tree amplitude is



_I_ ( _X_ 1 _, X_ 2 _, X_ 3 _, X_ 4 _, X_ 5) =



5



_i_ =1



1
_._ (E.3)
_XiXi_ +1



So the integrand is


1 1 1
_I_ Γ =
_X_ 12 [0] [(] _[X]_ 12 [1] _[−]_ _[X]_ 12 [0] [)(] _[X]_ 13 [0] _[−]_ _[X]_ 12 [0] [) +] _X_ 12 [0] [(] _[X]_ 13 [0] _[−]_ _[X]_ 12 [0] [)(] _[X]_ 12 _[−]_ [1] _[−]_ _[X]_ 12 [0] [) +] _X_ 12 [0] [(] _[X]_ 12 _[−]_ [1] _[−]_ _[X]_ 12 [0] [)(] _[X]_ 13 _[−]_ [1] _[−]_ _[X]_ 12 [0] [)]

1 1
+ + (E.4)
_X_ 12 [0] [(] _[X]_ 13 _[−]_ [1] _[−]_ _[X]_ 12 [0] [)] _[X]_ [22] _X_ 12 [0] _[X]_ [22][(] _[X]_ 12 [1] _[−]_ _[X]_ 12 [0] [)] [+ (2] _[ ↔]_ [3)] _[.]_


The momenta are explicitly


_P_ 12 _[n]_ [=] _[ ℓ]_ [+] _[ nk]_ [1] _[,]_ _P_ 13 _[n]_ [=] _[ ℓ]_ [+] _[ k]_ [2] [+] _[ nk]_ [1] _[,]_ _P_ 22 = _k_ 1 _,_ _P_ 33 = _k_ 1 + _k_ 2 _._ (E.5)


**E.2** **The** **2-loop** **vacuum** **at** **genus** **one**


The 2-loop genus 1 vacuum amplitude has already been computed in Section 9.2. Take again Γ to be
the 2-loop genus one vacuum diagram. The curves of Γ are _Cp/q_, with momentum


_Pp/q_ = _pℓ_ + _qℓ_ _[′]_ _._ (E.6)


Every curve _Cp/q_ is in the same MCG-orbit. Pick, say, _C_ 0 _/_ 1 as the coset representative. The curves
compatible with _C_ 0 _/_ 1 are _C_ 1 _/n_ for _n_ _∈_ Z. Cutting Γ along _C_ 0 _/_ 1 gives a 1-loop non-planar diagram
Γ _C_ 0 _/_ 1, and the curves _C_ 1 _/n_ can be identified with the curves we called ‘ _Cn_ ’ in the previous example.
Applying the global forward limit once gives


1
_I_ Γ = _X_ 0 _/_ 1 _I_ Γ _C_ 0 _/_ 1 ( _X_ 1 _/n −_ _X_ 0 _/_ 1) _._ (E.7)


However, we have already computed the 1-loop non-planar integrand, and found, up to loop-momentum
shifts, that it is given by


1
_I_ Γ _C_ 0 _/_ 1 ( _Xn_ ) = _X_ 0 _X_ 1 _._ (E.8)


Using this result in (E.7) gives


1
_I_ Γ = (E.9)
_X_ 0 _/_ 1( _X_ 1 _/_ 0 _−_ _X_ 0 _/_ 1)( _X_ 1 _/_ 1 _−_ _X_ 0 _/_ 1) _[.]_


Loop re-definitions of _ℓ_ and _ℓ_ _[′]_ can be used to cyclically permute the labels 0 _/_ 1 _,_ 1 _/_ 0 _,_ 1 _/_ 1. Summing
over the possible three cyclic permutations (and dividing by 3) gives


1

_I_ Γ = [1] _._ (E.10)

3 _X_ 0 _/_ 1 _X_ 1 _/_ 0 _X_ 1 _/_ 1


The 1 _/_ 3 factor is expected because _|_ Aut(Γ) _|_ = 3. We therefore recover 1 _/_ 3 of the Feynman integral
of the sunrise vacuum diagram.


                   - 78                    

**E.3** **A** **comment** **on** **the** **1-loop** **planar** **amplitudes**


Our formula for the 1-loop planar amplitudes can be computed directly, without topological recursion.
The global Schwinger formula gives a well defined loop integrand for these amplitudes, without linearized propagators. However, we can arrive at a forward-limit-like formula for the 1-loop integrand
by inserting the ‘trivial’ Mirzakhani kernel



1 =



_n_



_i_ =1



_α_ 0 _i_

- _n_ (E.11)
_i_ = _j_ _[α]_ [0] _[j]_



into the curve integral. Here, _α_ 0 _i_ is the headlight function of _C_ 0 _i_, the curve from _i_ to the internal loop
boundary, 0. Equation (E.11) then allows us to write the 1-loop planar n-point amplitude as a sum
of _n_ disk amplitudes, with linearized propagators. Evaluating the integral, using the recursion (10.4),
the integrand is




_−_ 1
_A_ (12 _....i_ 0 _i....n_ ) _,_ (E.12)
_X_ 0 _i_ ����� _X_ 0 _j_ _�→X_ 0 _j_ _−X_ 0 _i_



_I_ 1loop(1 _, ..., n_ ) =



_n_



_i_ =1



where _A_ (12 _...n_ ) are the tree-level partial amplitudes, but now with linearized propagators.


**F** **Details** **for** **the** **non-planar** **1-loop** **propagator**


The matrix for the curves _Cn_ with _n ≥_ 0 is


_Mn_ = _LDx_ ( _LDyRDx_ ) _[n]_ _R._ (F.1)


Taking the transpose, we see that _Mn_ _[T]_ [=] _[ M][n]_ [.] [In] [particular,]


�1 1                     _M_ 0 = _._ (F.2)
1 1 + _x_



Given _M_ 0, we can compute _Mn_ using


�0 _−xy_
_Mn_ +1 = _MnB_ +1 _,_ where _B_ +1 = _R_ _[−]_ [1] _LDyRDxR_ =
1 1 + _x_ + _xy_


It follows that we can write




_._ (F.3)



_Mn_ = - _Fn−_ 2 _Fn−_ 1
_Fn−_ 1 _Fn_




_,_ (F.4)



where


_Fn_ +2 = (1 + _x_ + _xy_ ) _Fn_ +1 _−_ _xyFn,_ (F.5)


with initial conditions _F−_ 2 = 1 _, F−_ 1 = 1. The first few examples are


_F_ 0 = 1 + _x,_ (F.6)

_F_ 1 = 1 + 2 _x_ + _x_ [2] + _x_ [2] _y,_ (F.7)

_F_ 2 = 1 + 3 _x_ + 3 _x_ [2] + _x_ [3] + 2 _x_ [2] _y_ + 2 _x_ [3] _y_ + _x_ [3] _y_ [2] _._ (F.8)


                   - 79                    

Similarly, the matrix for the curves _Cn_ with _n <_ 0 is given by


_Mn_ = _RDy_ ( _RDxLDy_ ) _[−][n][−]_ [1] _L,_ _n <_ 0 _._ (F.9)


These matrices are again symmetric, and



�1 + _y_ _y_
_M−_ 1 =
_y_ _y_




_._ (F.10)



We can evaluate _Mn_ using


�1 + _x_ + _xy_ _xy_
_Mn−_ 1 = _MnB−_ 1 _,_ where _B−_ 1 = _L_ _[−]_ [1] _RDxLDyL_ = _−_ 1 0


This implies that _Mn_ ( _n <_ 0) has the form,




_._ (F.11)



_Mn_ =           - _Gn_ _xyGn_ +1
_xyGn_ +1 ( _xy_ ) [2] _Gn_ +2


where the polynomials _Gn_ are determined by the recursion




_,_ (F.12)



_Gn_ = (1 + _x_ + _xy_ ) _Gn_ +1 _−_ _xyGn_ +2 _,_ (F.13)


with initial condition _G_ 1 = 1 _/_ ( _x_ [2] _y_ ) and _G_ 0 = 1 _/x_ . The first few polynomials are


_G−_ 1 = 1 + _y,_ (F.14)

_G−_ 2 = 1 + _x_ + 2 _xy_ + _xy_ [2] _,_ (F.15)

_G−_ 3 = (1 + _x_ + _xy_ ) [2] + _x_ [2] _y_ (1 + _y_ ) [2] _._ (F.16)


We now need to compute the tropicalizations of the polynomials _Fn_ ( _n_ _≥−_ 2) and _Gn_ ( _n_ _≤_ 1).
Write


_fn_ = Trop _Fn,_ and _gn_ = Trop _Gn._ (F.17)


Then, for _n ≥_ 0, we find


_fn_ = max(0 _,_ ( _n_ + 1) _x,_ ( _n_ + 1) _x_ + _ny_ ) _,_ (F.18)


which follows by induction using that


_fn_ +2 = max(max(0 _, x, x_ + _y_ ) + _fn_ +1 _,_ max(0 _, x_ + _y_ ) + _fn_ ) _._ (F.19)


Similarly, for _n ≤−_ 1,


_gn_ = max(0 _, −_ ( _n_ + 1) _x, −_ ( _n_ + 1) _x −_ _ny_ ) _._ (F.20)


We also have that


_f−_ 2 = 0 _,_ _f−_ 1 = 0 _,_ _g_ 1 = _−_ 2 _x −_ _y,_ _g_ 0 = _−x._ (F.21)


The headlight functions are


_αn_ = _−fn_ + 2 _fn−_ 1 _−_ _fn−_ 2 _,_ _n ≥_ 0 _,_ (F.22)

_αn_ = _−gn_ + 2 _gn_ +1 _−_ _gn_ +2 _,_ _n <_ 0 _._ (F.23)


                   - 80                    

**References**


[1] Stephen J. Parke and T. R. Taylor. An Amplitude for _n_ Gluon Scattering. _Phys._ _Rev._ _Lett._,
56:2459, 1986.


[2] Zvi Bern, Lance Dixon, David C. Dunbar, and David A. Kosower. One-loop _n_ -point gauge
theory amplitudes, unitarity and collinear limits. _Nuclear_ _Physics_ _B_, 425(1-2):217–260, aug
1994.


[3] Zvi Bern, Lance Dixon, David C. Dunbar, and David A. Kosower. Fusing gauge theory tree
amplitudes into loop amplitudes. _Nuclear_ _Physics_ _B_, 435(1-2):59–101, feb 1995.


[4] Edward Witten. Perturbative gauge theory as a string theory in twistor space. _Communications_
_in_ _Mathematical_ _Physics_, 252(1-3):189–258, oct 2004.


[5] Freddy Cachazo, Peter Svrcek, and Edward Witten. MHV vertices and tree amplitudes in gauge
theory. _Journal_ _of_ _High_ _Energy_ _Physics_, 2004(09):006–006, sep 2004.


[6] Ruth Britto, Freddy Cachazo, and Bo Feng. New recursion relations for tree amplitudes of
gluons. _Nuclear_ _Physics_ _B_, 715(1-2):499–522, may 2005.


[7] Ruth Britto, Freddy Cachazo, Bo Feng, and Edward Witten. Direct proof of the tree-level
scattering amplitude recursion relation in yang-mills theory. _Physical_ _Review_ _Letters_, 94(18),
may 2005.


[8] Nima Arkani-Hamed and Jaroslav Trnka. The amplituhedron. _Journal_ _of_ _High_ _Energy_ _Physics_,
2014(10), oct 2014.


[9] Nima Arkani-Hamed, Yuntao Bai, Song He, and Gongwang Yan. Scattering Forms and the
Positive Geometry of Kinematics, Color and the Worldsheet. _arXiv:1711.09102_ _[hep-th]_, 2017.


[10] Giulio Salvatori. 1-loop amplitudes from the halohedron. _Journal_ _of_ _High_ _Energy_ _Physics_,
2019(12), dec 2019.


[11] Nima Arkani-Hamed, Song He, Giulio Salvatori, and Hugh Thomas. Causal Diamonds, Cluster
Polytopes and Scattering Amplitudes. _arXiv:1912.12948_ _[hep-th]_, January 2020.


[12] Nima Arkani-Hamed, Song He, and Thomas Lam. Stringy canonical forms. _JHEP_, 02:069, 2021.


[13] Nima Arkani-Hamed, Hadleigh Frost, Giulio Salvatori, Pierre-Guy Plamondon, and Hugh
Thomas. The curvy world of curves. in preparation.


[14] V. V. Fock and A. B. Goncharov. Moduli spaces of local systems and higher Teichm¨uller theory.
_arXiv_ _Mathematics_ _e-prints_, page math/0311149, November 2003.


[15] Robert C Penner. _Decorated_ _Teichm¨uller_ _theory_, volume 1. European Mathematical Society,
2012.


[16] Nima Arkani-Hamed, Hadleigh Frost, Giulio Salvatori, Pierre-Guy Plamondon, and Hugh
Thomas. The combinatorical string. in preparation.


[17] Harm Derksen and Jerzy Weyman. _An_ _Introduction_ _to_ _Quiver_ _Representations_ . American
Mathematical Soc., November 2017.


[18] N. Haupt. Euler characteristics of quiver Grassmannians and Ringel-Hall algebras of string
algebras. _Algebr_ _Represent_ _Theor_, 15:755–793, 2012.


[19] ’t Hooft, G. A planar diagram theory for strong interactions. _Nuclear_ _Physics_ _:_ _B_, 72, 1974.


                   - 81                    

[20] V. V. Fock and A. B. Goncharov. Dual Teichm¨uller and lamination spaces. _arXiv_ _Mathematics_
_e-prints_, page math/0510312, October 2005.


[21] Sergey Fomin and Andrei Zelevinsky. Cluster algebras IV: Coefficients. _Compos._ _Math._,
143(1):112–164, 2007.


[22] Sergey Fomin and Dylan Thurston. Cluster algebras and triangulated surfaces part II: Lambda
lengths. _Memoirs_ _of_ _the_ _American_ _Mathematical_ _Society_, 255(1223):0–0, sep 2018.


[23] M. Mirzakhani. Simple geodesics and Weil-Petersson volumes of moduli spaces of bordered
Riemann surfaces. _Invent._ _math._, 167:179–222, 2007.


[24] Francis C. S. Brown. Multiple zeta values and periods of moduli spaces M0 _,n_ . _Annales_
_scientifiques_ _de_ _l’Ecole_ _[´]_ _Normale_ _Sup´erieure,_ _Serie_ _4_, 42(3):371–489, 2009.


[25] Nima Arkani-Hamed, Song He, and Thomas Lam. Cluster configuration spaces of finite type.
_Symmetry,_ _Integrability_ _and_ _Geometry:_ _Methods_ _and_ _Applications_, oct 2021.


[26] Nima Arkani-Hamed, Hadleigh Frost, Giulio Salvatori, Pierre-Guy Plamondon, and Hugh
Thomas. All n paper. in preparation.


[27] Song He and Ellis Ye Yuan. One-loop scattering equations and amplitudes from forward limit.
_Physical_ _Review_ _D_, 92(10), nov 2015.


[28] Johannes Agerskov, N. E. J. Bjerrum-Bohr, Humberto Gomez, and Cristhiam Lopez-Arcos.
One-loop yang-mills integrands from scattering equations. _Physical_ _Review_ _D_, 102(4), aug 2020.


[29] Franziska Porkert and Oliver Schlotterer. One-loop amplitudes in einstein-yang-mills from
forward limits. _Journal_ _of_ _High_ _Energy_ _Physics_, 2023(2), feb 2023.


[30] Y. Geyer and R. Monteiro. Gluons and gravitons at one loop from ambitwistor strings. _J._ _High_
_Energ._ _Phys._, 2018:68, 2018.


[31] Yvonne Geyer and Ricardo Monteiro. Two-loop scattering amplitudes from ambitwistor strings:
from genus two to the nodal riemann sphere. _Journal_ _of_ _High_ _Energy_ _Physics_, 2018(11), nov
2018.


[32] Y. Geyer, R. Monteiro, and R. Stark-Much˜ao. Two-loop scattering amplitudes: double-forward
limit and colour-kinematics duality. _J._ _High_ _Energ._ _Phys._, 2019:49, 2019.


[33] Michael Borinsky. Tropical Monte Carlo quadrature for Feynman integrals. _Annales_ _de_
_l’Institut_ _Henri_ _Poincar´e_ _D_, jan 2023.


[34] Michael Borinsky, Henrik J. Munch, and Felix Tellander. Tropical Feynman integration in the
Minkowski regime. _Computer_ _Physics_ _Communications_, 292:108874, nov 2023.


[35] Zvi Bern, John Joseph M. Carrasco, and Henrik Johansson. Perturbative Quantum Gravity as a
Double Copy of Gauge Theory. _Phys._ _Rev._ _Lett._, 105:061602, 2010.


                   - 82                    

