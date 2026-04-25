Prepared for submission to JHEP

## **Scalar-Scaffolded Gluons and the Combinatorial** **Origins of Yang-Mills Theory**


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


Abstract: We present a new formulation for Yang-Mills scattering amplitudes in any

number of dimensions and at any loop order, based on the same combinatorial and binarygeometric ideas in kinematic space recently used to give an all-order description of Tr _ϕ_ [3]


theory. We propose that in a precise sense the amplitudes for a suitably “stringy” form of

these two theories are identical, up to a simple shift of kinematic variables. This connec
tion is made possible by describing the amplitudes for _n_ gluons via a “scalar scaffolding”,

arising from the scattering of 2 _n_ colored scalars coming in _n_ distinct pairs of flavors fusing

to produce the gluons. Fundamental properties of the “ _u_ -variables”, describing the “binary

geometry” for surfaces appearing in the topological expansion, magically guarantee that
the kinematically shifted Tr _ϕ_ [3] amplitudes satisfy the physical properties needed to be

interpreted as scaffolded gluons. These include multilinearity, gauge invariance, and fac
torization on tree- and loop- level gluon cuts. Our “stringy” scaffolded gluon amplitudes

coincide with amplitudes in the bosonic string for extra-dimensional gluon polarizations

at tree-level, but differ (and are simpler) at loop-level. We provide many checks on our

proposal, including matching non-trivial leading singularities through two loops. The sim
ple counting problem underlying the _u_ variables autonomously “knows” about everything

needed to convert colored scalar to gluon amplitudes, exposing a striking “discovery” of

Yang-Mills amplitudes from elementary combinatorial ideas in kinematic space.


**Contents**


**1** **Introduction** **and** **Summary** **1**


**2** **Review** **of** **Surfaceology** **7**
2.1 The Tr _ϕ_ [3] theory 8

2.2 Defining the surface 9

2.3 Kinematical data and curves on the surface 10

2.4 From curves on the fat graph to words 13

2.5 From words to _u_ -variables 14

2.6 Summary of _u_ facts 16

2.7 “Stringy” amplitudes 19


**3** **Scalar-Scaffolded** **Gluons** **24**

3.1 From 2 _n_ scalars to _n_ gluons 25

3.2 Polarizations and momenta of the gluons 26

3.3 Unified form of gauge invariance and multi-linearity 28

3.4 Dictionary: From scalar to gluon kinematics 31

3.5 3-point gluon amplitude in scalar language 32


**4** **Tree-level** **Gluon** **Amplitudes** **33**

4.1 Connection to the bosonic string 33

4.2 The scaffolding residue 35
4.3 Scaffolding residue ⇒ Gauge invariant and multi-linear amplitude 38
4.4 Tree-level factorization 40

4.5 Computing scaffolding residues for general _n_ 44

4.6 Consistency check: From 4 _n_ -scalars to 2 _n_ -scalars 48

4.7 Examples 50

4.8 Further comments 53


**5** **Loop-level** **Gluon** **Amplitudes** **55**

5.1 Loop scaffolding form 55

5.2 Surface Kinematics 57

5.3 Surface gauge invariance 59

5.4 Examples: one-loop 1- and 2-gluon integrands 61

5.5 A well-defined Yang-Mills integrand 64


**6** **Leading** **Singularities** **64**

6.1 Linearized _u_ ’s 65

6.2 Tree level 67

6.3 Loop level 70


                   - i                   

**7** **Integrand** **Cuts:** **Tree-loop** **cut** **and** **loop-cut** **73**

7.1 Tree-loop Cut 73

7.2 Loop-Cut 76

7.3 Gluing in Momentum Space 78

7.4 Surface kinematics and the loop-cut 81

7.5 Loop-cut matching with Tree-gluing 82


**8** **Outlook** **84**


**A** **Scaffolding** **residues** **using** **worldsheet** **variables** **of** **bosonic** **string** **87**


**B** **Complete** **results** **for** 1 **-loop** 4 **-point** **box** **leading** **singularity** **87**


**C** **Factorization** **for** **derivatives** **of** _u_ **variables** **89**


**D** **Matching** **of** **the** **loop-cut** **with** **gluing** **of** **tree** **in** **the** **forward** **limit** **91**

D.1 Matching of the _D_ -dependent part 91

D.2 Matching of variables of tree triangulation 92

D.3 Matching of loop variables 93
D.4 Matching of curves _X_ 1 _,j_ 97
D.5 Matching the tadpole part 98

D.6 Difference between loop-cut and tree-gluing as a total derivative 99


**1** **Introduction** **and** **Summary**


Scattering amplitudes are the “boundary observables” in flat space. The observations of

the asymptotic states are made at infinity, while the interior of the spacetime serves as

an auxiliary arena allowing us to incrementally build up the final amplitude in terms of

interactions at and propagation between spacetime points. But given that the observable

is anchored at infinity, it is natural to take the holographic point of view and ask: is there a

way of calculating scattering amplitudes that jettisons the interior of the spacetime entirely,

formulated purely in the kinematic space describing the scattering amplitude?

Tackling this question has turned out to involve ideas very far from the much more

familiar (and so far more successful) instantiations of holography in Anti-de-Sitter space .

The reason is simple: the “kinematic space” that labels boundary correlation functions in

AdS space is simply all the points in the one lower-dimensional spacetime on the bound
ary, with a conventional notion of locality, time, and quantum mechanical evolution. By

contrast, the kinematic space labelling scattering processes has none of this familiar struc
ture: for _n_ particle scattering we have the space of _n_ on-shell momenta, without any of the

familiar properties of the arenas in which physics is usually described.

But over the past decade, it has become apparent that in a number of cases, there

is just enough structure in this seemingly barren kinematic space to discover entirely new


1


**Figure** **1** : Binary behaviour of _u_ -variables and factorizations.


mathematical questions to which the scattering amplitudes, with all their richness and com
plexity, are the answer. The emerging picture is that kinematic space contains elementary

but deep combinatorial structures that in turn specify a tower of related mathematical ob
jects above them, ultimately giving a completely autonomous definition of amplitudes. In

this way, the usual foundational principles of locality and unitarity can be seen as derivative

notions, ultimately arising from this fundamentally combinatorial rubric.

The first example of this sort of structure was seen with the discovery of the amplituhedron for N = 4 SYM in the planar limit [1]. The integrand for the planar amplitude, at any
loop order, is given as the “canonical form” [2] of a certain region in the kinematic space

of momentum(-twistor) data [3], entirely specified by topological winding number and pos
itivity properties [4]. There is no mention of diagrams, locality, or unitarity anywhere in

sight, instead in this example, these very simple but rather alien and more abstract com
binatorial and geometric concepts bring the physics of spacetime and quantum mechanics

to life, along the way manifesting the hidden infinite Yangian symmetry enjoyed by the
scattering amplitudes. However, the very special nature of planar N = 4 SYM–its maximal
supersymmetry and integrability–might be thought of as a dissuasion from the thought

that such structures generalize to more realistic theories, instead perhaps being an artifact

of studying the most special toy model we know of.

In the past few years, however, morally similar but technically quite different structures

have been seen in a completely different setting, for the simplest theory of colored scalars
with cubic self-interactions–the Tr _ϕ_ [3] theory–at all loop orders and to all orders in the

topological ’t Hooft expansion [5, 6] [7, 8]. This “curve-integral” formalism features a simple

counting problem defined at any order in the topological expansion, which defines a set of
variables, _uC_, defined for all propagators/ curves _C_ on a surface, satisfying the remarkable
non-linear equations _uC_ +∏ _D uD_ [#int][(] _[C,D]_ [)] = 1. These equations define a “binary geometry” [9,
10]: if we set _u_ C ≥ 0 they also force 0 ≤ _u_ C ≤ 1, and as we approach a boundary where _u_ C → 0
all the “incompatible” curves D that cross C have _u_ D → 1. The amplitudes are defined

by A = ∫ _ω_ ∏ _C uPCX_ [2] [,] [where] _[ω]_ [is] [a] [simple] [canonical] [form] [with] [logarithmic] [singularities] [on]


2


the boundaries where _uC_ → 0, and _PC_ _[µ]_ [is] [the] [momentum] [associated] [with] _[C]_ [.] [The] [binary]
character of the _u_ C variables tells us that the “curve integral” for A deserves to be called
an “amplitude”, by guaranteeing the correct patterns of factorization near singularities as

in figure 1 at tree-level. The curve integral can give us both “stringy” amplitudes, or, via

“tropicalization”, directly amplitudes in the field theory limit. There is no trace of the idea

of “summing over all spacetime processes’ in these formulas. Instead, the simple counting

problem attached to curves on surfaces magically converts combinatorial geometry into

local and unitary physics in this model.
But in the same way that N = 4 SYM theory seems “too special” to offer a hope for
connecting combinatorial geometry to real-world physics, the Tr _ϕ_ [3] theory might seem too
simple. While the singularities/poles/“denominators” of Tr _ϕ_ [3] are universal and shared

by all theories of colored particles, real-world amplitudes for e.g. colored gluons differ

in a crucial way, in their numerator structure. However, so far the connection between

amplitudes and geometry has centered on long-distance singularities captured only by

the “denominators”, which are simple poles associated in many settings with the sim
plest “logarithmic” singularities. This is reflected in the ubiquity of “canonical forms

with dlog singularities on boundaries of positive geometries” in this world of ideas. In
teresting numerators are instead associated with new singularities at infinite momentum,

not captured by “dlog” singularities. This basic fact has been a thorn in the side of the

“amplitudes=combinatorial geometry” program for over a decade, going back to “poles at

infinity” seen in non-supersymmetric BCFW shifts, and non-dlog forms in the Grassman
nian required to describe leading singularities in non-supersymmetric gauge theory [11].

Clearly the realistic non-supersymmetric Yang-Mills theory demands a move away from

such “dlog forms”, but in what setting, and how? Until very recently, there was no plan

of attack to make progress on this fundamental mystery.

But in [12] we reported a wonderful surprise that has transformed the situation. Far
from the toy model it appears to be, the “stringy” Tr _ϕ_ [3] amplitudes secretly _contains_ the

scattering amplitudes for pions [13], as well as non-supersymmetric gluons, in any number

of dimensions. The amplitudes for the different theories are given by one and the same

function, related by a simple shift of the kinematics. Working at tree-level, the stringy Tr
_ϕ_ [3] amplitude is given as



A [Tr] _[ϕ]_ [3] = ∫



∞




_[i]_

_yi_ [∏] _i,j_ _ui,j_ _[α]_ [′] _[X][i,j]_ _,_ (1.1)



∏ _[dy][i]_
0 _y_



where _Xi,j_ = ( _pi_ + _pi_ +1 +⋯+ _pj_ −1) [2] are the natural planar variables occurring as poles in the
amplitude. This same function remarkably determines Yang-Mills amplitudes by a simple

kinematical shift:


A [gluons] ( _X_ ) = A [Tr] _[ϕ]_ [3] ( _Xe,e_ → _Xe,e_ + 1/ _α_ [′] _,Xo,o_ → _Xo,o_   - 1/ _α_ [′] _,Xe,o_ → _Xe,o_ ) _,_ (1.2)

where _Xe,e,Xo,o,Xe,o_ refer to _Xi,j_ where the pair of indices ( _i,j_ ) are both even, both odd,
or one of each respectively.

To be more precise, this kinematical shift gives us the amplitude for what we call

“scaffolded gluons”: an amplitude for 2 _n_ colored scalars coming in _n_ pairs of distinct


3


**Figure** **2** : From colored scalars to scalar-scaffolded gluons.


flavors. As we will explain in detail, completely general amplitudes for _n_ gluons, with

arbitrary choices of (null) polarizations, are captured by these “scaffolded” amplitudes the

“scaffolding residues” are taken, corresponding to factorizing this amplitude on the channel

where the pairs of same-species scalar fuse into gluons. This will turn out to be a simple

and powerful picture both for presenting gluon amplitudes in an entirely canonical way

free of the familiar annoying redundancies, as well as seeing their hidden relationships with

other theories.
Our kinematic shift can equivalently be described by multiplying the Tr _ϕ_ [3] integrand
by a factor (∏ _u_ [+] _e,e_ [1] _[u]_ [−] _o,o_ [1] [)][.] [This] [factor] [has] [a] [beautiful] [interpretation] [directly] [in] [terms] [of] [the]
_y_ variables, if we choose a particularly natural triangulation for our 2 _n_ -gon surface. We

simply choose any triangulation/fat graph we like for the “inner” _n_ -gon, and turn it into a

“scaffolding triangulation” by splitting each of the _n_ external legs in two, just as suggested
from the scalar scaffolding picture. Quite beautifully, this product (∏ _u_ [+] _e,e_ [1] _[u]_ [−] _o,o_ [1] [)] [=] [∏] _i_ _[y]_ _i_ [−][1][.]
This means that the entire effect of the kinematical shift for the 2 _n_ scalar problem is to
replace the dlog-form measure ∏ _dyi_ / _yi_ →∏ _dyi_ / _yi_ [2] [(see] [figure] [2][)!] [Note] [this] [is] [no] [longer] [a]
dlog form, as had long been anticipated was necessary for non-supersymmetric Yang-Mills

theory.

As shown in [12] and discussed at further length in this paper, at tree level this kine
matic shift precisely matches gluon amplitudes in the bosonic string, choosing the momenta

to lie in _d_ dimensions and pairs of polarizations to live in _n_ extra dimensions. In this paper

we will go much further, and propose that, appropriately interpreted, this expression gives

us a definition for the amplitudes of non-supersymmetric Yang-Mills theory at all loop

orders, in any number of spacetime dimensions. But where does this strange kinematic

shift come from? And why on earth should it have had anything to do with describing

gluon amplitudes?

We will see striking answers to these questions throughout this paper. Clearly generic

functions of _X_ ’s for a 2 _n_ problem can not be interpreted as amplitudes for scaffolded


4


gluons. Instead as we will see these functions must have a symmetry under certain linear
shifts of the _Xi,j_, guaranteeing both **gauge** **invariance** and **multilinearity** of the gluon
amplitudes they are describing. These properties emerge magically from the shifted integral
with the _dy_ / _y_ [2] measure, when the scaffolding residue to land on gluon amplitudes is taken.
We have already remarked that the fundamental “binary” property of the _u_ variables–that
when _u_ C → 0 the _u_ D → 1 for D intersecting C–is responsible for factorization and therefore
the right to call the curve integral an “amplitude” for the scalar Tr _ϕ_ [3] theory. Shifting
to the _dy_ / _y_ [2] form and taking the scaffolding residue ends up also probing the behavior of
the _u_ ’s in the first-order neighborhood of where they vanish, which takes us beyond the

most basic “binary” properties. Amazingly, fundamental identities relating _u_ variables of

the inner _n_ -gon and outer 2 _n_ -gon problems give exactly the needed first-order behavior to

force the integral to have the symmetries needed for gauge invariance and multilinearity!

This is already strong evidence that we must be describing gluons, but to clinch the case

we have to show consistent factorization on gluon poles, both for tree-like factorization, as

well the loop-level “single cut”. As we will see, once again properties of the _u_ variables that

follow transparently from their definition in terms of the counting problem, give precisely

the needed identities for these “tree-cut” and “loop-cut = forward limit” factorizations to

arise exactly as needed. All of these properties hold not just in the field theory limit but
also at finite _α_ [′] .

We find it fascinating that elementary but deep properties of the _u_ variables, ultimately

deriving from the simple counting problem associated with curves on surfaces that define

them [7, 8], contain exactly the magical properties needed to produce functions that can

be interpreted as scattering amplitudes for gluons enjoying gauge invariance. This mirrors

the famous “discovery of gluons” arising from M¨obius invariance of correlators for the

spin-one vertex operators in string theory. But in this new picture there is no worldsheet,

no conformal field theory living on it, and no vertex operators. Instead we have pure

combinatorics, with the magical ability to produce “gluon amplitudes” seemingly out of

thin air!

In the course of these explorations we will also see that merely asking for our new

integrals to have any kind of natural factorization properties on the poles, dictates how

to more precisely interpret the 2 _n_ scaffolded formula. At loop level the product over
curves C must include open curves with up to one self-intersection per loop. It must also
include a product over closed curves ∆with exponents _u_ [1] ∆ [−] _[D]_ where _D_ is the number of
spacetime dimensions, which is where the dependence on spacetime dimensionality, absent
in the Tr _ϕ_ [3] theory, makes an appearance for gluons. The need for including curves with

one self-intersection per loop is very interesting, and shows a pronounced difference with
what is expected of string theory at one-loop. For Tr _ϕ_ [3] theory it is already known that

matching (bosonic) string theory at loop-level from the curve-integral formalism [14] asks

us to consider the product over _all_ curves, including those with arbitrarily high intersection

numbers. It is fascinating that in order to have consistent factorization on massless gluon

poles–guaranteeing that we are describing Yang-Mills theory at low energies–we must make

the curve-integral “slightly more stringy” by including curves with a finite number of self
intersections. Of course, this is still vastly simpler than the infinite set of curves that string


5


theory demands even to describe the scalar Tr _ϕ_ [3] theory.

The consistent factorization of “loop-cut = forward limit” [15, 16] is especially non
trivial, where not only algebraic relations but total derivative identities are needed to

establish the correspondence; nonetheless, they all fall out naturally from the counting

problem formulae for the _u_ variables. As we will emphasize, this solves a long-standing

conceptual problem afflicting all attempts to date to make sense of the notion of “the Yang
Mills integrand” at loop-level for non-supersymmetric theories. The well-known problem

is again a very basic one. The Feynman diagrams have diagrams with “tadpoles” and
hence 1/0 propagators at the level of the integrand. But a general feature of the curveintegral formalism already for Tr _ϕ_ [3] theory allows us the flexibility to give any values we

like to the _X_ variables–in particular, nothing mandates that the variables corresponding

to tadpoles (or massless external bubbles) be set equal to zero. Leaving them free then lets

us work with completely well-defined integrands. Remarkably, it is precisely these well
defined integrands that satisfy the exact “loop-cut = forward limit” formula! So the surface

formalism _defines_ objects for us that naturally enjoy a “surface” notion of gauge-invariance,

and also factorize precisely onto themselves. Amongst other things, this opens the door

to finding all-loop recursion relations for pure Yang-Mills amplitudes in any number of

dimensions [17].
We believe that the remarkable link between Tr _ϕ_ [3] theory, pions, and gluons reported

in [12], extended to all loops in the present paper and [13] represents a major step forward

in the adventure of describing real-world scattering processes in the radically new language

of combinatorial geometry. Our goal in this paper is to initiate an exploration of the new

world of physical and mathematical ideas involved in this “combinatorial discovery” of

pure Yang-Mills theory, and present the most basic checks on our proposal, leaving many

interesting and important questions for future work.

We will begin in section 2 with a review of “surfaceology” and the curve integral

formalism. This is intended as a crash-course introduction to all the formulas needed

to understand the surface picture for kinematic space, a user manual for computing _u_

variables and using them to construct stringy amplitudes, and a compendium of important

facts about _u_ variables we will use throughout this paper. This short section is meant as a

self-contained summary of the facts we will need from the curve-integral formalism, whose

origin and conceptual underpinning are presented in a different series of papers beginning

with [7, 8]; the review of _u_ variables will borrow results to appear in [18]. We next move

on in section 3 to describing the picture of scalar-scaffolded gluons, establishing the simple

dictionary between gluon and scalar variables, and understanding how the basic gluonic

kinematic facts of on-shell gauge-invariance and linear dependence on polarization-vectors

are given a unified description in scalar terms. We discuss gluon amplitudes at tree level in

section 4, beginning by showing how our proposal precisely matches gluon amplitudes in

the open bosonic string, with an appropriate choice of extra-dimensional polarizations. We

will see how the unified statements of gauge-invariance and multilinearity arise from simple

properties of the _u_ variables. The same properties also imply consistent factorization of the

amplitude on massless gluon poles. We present an explicit _n_ -point formula for scaffolding

residues, and see how the interpretation of the scalar-scaffolded amplitudes as those of


6


extra-dimensional polarization gluons is naturally discovered in our language. We also

give simple examples of three- and four-point string/particle amplitudes. We move on to

present our proposal at loop-level in section 5, where a number of essential new ingredients

first make an appearance, and the difference with standard string amplitudes becomes

stark. This includes the need for keeping minimally self-intersecting curves as well as

closed curves encoding the dependence on the number of spacetime dimensions we have

alluded to above. Finally, we present a series of checks we have performed on our proposal.

In section 6, we compute leading singularities corresponding to gluing together on-shell

three-gluon amplitudes for arbitrary graphs: in our picture this turns into a simple residue

computation in the _y_ variables, and we present non-trivial examples through two loops, and

we find perfect matching with the gluing computation includes both the Yang-Mills and
_F_ [3] three-particle amplitudes. Of course this computation of leading singularities using

residues in _y_ variables bears no resemblance at all to the direct gluing of three-particle

amplitudes, and is also much more efficient. We then proceed to our most fundamental

and important check in section 7, showing how the single one loop-cut magically matches

the tree-forward limit, at full “stringy” level, following from many further fundamental

properties of _u_ variables hardwired into their combinatorial definition. We finally end

with an outlook on obvious avenues for future exploration immediately following from the

developments we discuss in this paper.


**2** **Review** **of** **Surfaceology**


A recent series of papers [7] has introduced the curve integral formalism for describing both
“stringy” Tr _ϕ_ [3] amplitudes, as well as the closely related “tropical” representation of these

amplitudes in the field theory limit, at all orders in the ‘t Hooft topological expansion. The

kinematic space for the amplitude at any order in the topological expansion is associated
with a surface S, which is specified by providing a triangulation or what is the same, a
single “fat graph” F, whose vertices are associated with triangles of the triangulation,
glued to each other as dictated by the edges. All the kinematic variables at this order in

the topological expansion are naturally associated with curves that can be drawn on the
surface or equivalently, paths that can be drawn on F. This space of curves on S specifies
the kinematic arena for Tr _ϕ_ [3] amplitudes. The heart of the curve integral formalism lies in
the existence of a remarkable set of “ _u_ C-variables” attached to any curve C on surface S.
As already mentioned in the introduction, these variables non-trivially satisfy the beautiful

equations
_u_ C + ∏ _u_ [# int] D [(C] _[,]_ [D)] = 1 _._ (2.1)
D


These equations define a variety whose dimensionality is given by the number of internal
edges of F, or more fancily, the dimensionality of the Teichmuller space of S. There are
a variety of ways of presenting the solution space of these equations. One uses ideas from
the hyperbolic geometry of S. A more surprising and deeper presentation is fundamentally combinatorial, expressing _u_ C’s as the solution to a certain extremely simple counting


7


problem associated with the curve C as drawn on the fat-graph F, giving _u_ C( _yi_ ) as a ratio
of polynomials in variables _yi_ associated with all the internal edges of F.
The _u_ variables are the stars of the Tr _ϕ_ [3] show in [7], playing many crucial roles.
They manifest a “binary” property, where asking _u_ C ≥ 0 also forces 0 ≤ _u_ C ≤ 1. This also
implies that if some _u_ C → 0, all the _u_ D → 1 for the curves D that cross C. Mathematically,
this gives us a completely algebraic characterization of all possible degenerations of the
surface. Said in more fancy (but not more contentful) language, the _u_ C variables give a
new, practical, algebraic, and “global” definition of the compactification of the Teichmuller
space of S. This is extremely useful: all the usual ways of choosing coordinates for the
surface are “local”; as such they make some degenerations/singularities easy to see, but

others are always more complicated, needing a detailed analysis and manual “blow-ups”

as the boundaries of the co-ordinate chart are approached. But the _u_ variables do all the

blowups for us, once and for all.

This “binary” property also has a crucial physical interpretation. If we consider a

product of the form ∏ _X uPXX_ [2] [, then as any particular] _[ u][X]_ [∗] [→] [0, the product factorizes exactly]
to the same product on the smaller surface we get by cutting the big surface along _X_ [∗] . This
precisely reflects the factorization of scattering amplitudes when the propagator _PX_ [2] [∗] [→] [0]
goes on-shell. This is what allows the curve integral formulas for both the “stringy” and
field-theoretic Tr _ϕ_ [3] theory to be interpreted as “amplitudes” for these models.
Amazingly, the _u_ / _y_ variables turn out to have a number of further properties, well
beyond the “binary” property manifested in the _u_ equations, that allow simple kinematic
shifts to transmute the seemingly “dull” amplitudes of Tr _ϕ_ [3] theory into the amplitudes of

gluons. The central goal of this paper is to show how this magic happens.

But our goal in this section is to provide a self-contained introduction to all aspects of

“surfaceology” needed for the reader to follow all of our arguments, without needing to have

previously read the series of papers associated with [7, 8]. As such our purpose is to simply

present the logical connection between various important concepts, and provide recipes for

concrete computations, without explaining where the concepts and formulas come from.

The reader interested in these conceptual underpinning as well as many concrete examples

of full amplitudes computed using the curve integral formalism is encouraged to consult

[7, 8]. Our review of the properties of the _u_ / _y_ variables borrows from the complete account
that will be given in [18].


**2.1** **The** **Tr** _ϕ_ [3] **theory**

Let _ϕ_ be an _N_ × _N_ matrix, the Lagrangian of the theory is:


L = Tr ( _∂ϕ_ ) [2] + _g_ Tr _ϕ_ [3] _._ (2.2)


so _ϕ_ is a massless field that interacts through cubic interactions with the coupling constant
_g_ [1] . We use the double line notation to keep track of the color indices in the interactions.


1It is trivial to add a mass term, but to keep things as simple as possible with our ultimate aim of
describing gluons in mind, we will stick with the massless Tr _ϕ_ [3] theory.


8


**Figure** **3** : Triangulation of the disk with 5 marked points on the boundary and corre
sponding dual fat graph.


Since this is a scalar theory, the data of a scattering process in this theory is simply the
momentum of the particles, _pi_ . As for the amplitude, since it has to be a Lorentz-invariant
function, it will only be a function of the **Mandelstam** **invariants** : _pi_ ⋅ _pj_ .
As we will explain in the next sections, the surface provides a very useful way of

organizing the kinematic data of the problem. In addition, we can use it to read off the

building blocks of string amplitudes - the **u-variables** .


**2.2** **Defining** **the** **surface**


The first step consists of defining the surface. By doing so, we specify both the scattering

process and the order in the topological expansion we are considering.

A surface is defined as a collection of triangles together with a rule on how to glue the

edges of the triangles together. So, one way of defining it is by providing a diagram, as it

uniquely determines a triangulation via duality.

For the most part in this paper, the surfaces we will be considering are disks with _n_

marked points on the boundary, and _l_ punctures – corresponding to single-trace amplitudes

of _n_ particles at _l_ loop order in the planar limit–though of course all surfaces corresponding

to all orders in the ‘t Hooft topological expansion can be chosen.


**2.2.1** **Tree-level**


At tree level let us consider the case of a 5-pt amplitude, which corresponds to a disk with
5 marked points on the boundary. Taking into account the diagram with propagators _X_ 1 _,_ 3
and _X_ 1 _,_ 4, we obtain the triangulation presented in Figure 3 (left).
The color graph, or ribbon graph, can be obtained from the Feynman diagram by

fattening the edges of the graph and assigning arrows that keep track of the contraction of

the color indices. However for our purposes, we only need the color graph without the color

indices - we call it the **fat** **graph**, as shown in figure 3 (right). The fat graph is then dual

to a triangulation of the surface and thus uniquely defines the surface. In fact, one can

explicitly go from the fat graph to the surface: for example, in the 5-point case presented


9


**Figure** **4** : Box triangulation of the punctured disk with 4 marked points on the boundary

and corresponding dual fat graph.


in figure 3, we can recover the disk with marked points on the boundary by shrinking the

shaded regions to points.


**2.2.2** **Loop-level**


Let us now consider a loop example, a 1-loop amplitude at 4 points. The corresponding

surface is now a disk with a puncture and four marked points on the boundary, for which
we choose a box triangulation. We denote the four chords of this triangulation by _Yi_,
(instead of _X_ ) because they end on the puncture. (see Figure 4 for triangulation (left)

and corresponding fat graph (right)). Similarly, by shrinking the shaded regions of the fat

graph, we can recover the punctured disk with 4 marked points on the boundary.


**2.3** **Kinematical** **data** **and** **curves** **on** **the** **surface**


Next, we need to understand how the kinematics, the data of the scattering problem is

encoded in the surface.

The mapping can be summarized as follows:


**Kinematical** **Data** **Surface**
Propagators ������������→ Chords/Curves, [ _X_ C]
Feynman Diagrams ������������→ Triangulations { _Xi_ 1 _,j_ 1 _,...,Xin_ −3 _,jn_ −3}


The scalar amplitudes we are considering are purely functions of the propagators, so,

according to the mapping, all the data of the problem is encoded on the curves we can

draw on the surface. Of course, naively, there seems to be an infinite number of curves one

can draw on a surface, so we need to understand which ones we need to consider.


10


**Figure** **5** : Determining momentum of curve _X_ 2 _,_ 5.


The answer is: we consider all curves that are not homologous to each other. Now we

need to say how to consistently assign momenta to these curves.


**2.3.1** **Tree-level**


At tree level, we start by assigning momentum to the boundary curves of the disk, corre
sponding to the momentum of the external particles. Now the planar variables associated
with the boundary curves are _Xi,i_ +1 = _p_ [2] _i_ [,] [so] [for] [boundary] [curves,] [we] [have:] _[X][i,i]_ [+][1] [=][ 0,] [for]
massless particles.

Now, at tree-level, we can read off the momentum assigned to a non-boundary curve,
_Xi,j_, by deforming it into the boundary, where it can be seen as the union of the boundary
curves from _i_ to _i_ + 1,..., _j_ - 1 to _j_ . So then the momentum of this curve is just the sum
of the momentum of these boundary curves, and thus we get _Xi,j_ = ( _pi_ + _..._ + _pj_ −1) [2], as we
expect for the planar propagators.

Alternatively, we can read off the momentum of a curve by using the fat graph. Let’s
go back to our 5-point example and consider the curve _X_ 2 _,_ 5, which on the surface side is
connecting the marked points 2 and 5. In order to draw this curve on the fat graph, we

first need to slightly rotate the ends of this curve **clock-wise** (see figure 5 (left)), this new

curve goes by the name of a **lamination** . Laminations start and end in the boundaries

of the disk, instead of marked points. These boundaries correspond to the edges of the

fat graph, and this is why laminations are the objects that are naturally defined in the fat

graph. From now on we will refer to the edges of the fat graph as **roads**, since, as opposed

to 1-dimensional edges of graphs, the roads of the fat graph are crucially 2-dimensional.
Therefore, the momentum of the boundaries of the disk, _p_ _[µ]_ _i_ [,] [determines] [the] [momentum]
associated with the external roads of the fat graph.

Thus to each curve on the surface, there is a unique lamination which is also defined

in the fat graph. The distinction between a curve and a lamination will not be important

for most of the matters we will encounter, so we will refer to curves and laminations

interchangeably, and highlight the situations in which the difference is important.


11


**Figure** **6** : Determining momentum of curve _Y_ 1.


So as a lamination, we can draw curve _X_ 2 _,_ 5 on the fat graph as shown in figure 5 (right).
To read off the momentum, we follow the curve and start by writing down the momentum
of the road in which the curve enters the graph - so for _X_ 2 _,_ 5, we would write down _p_ _[µ]_ 2 [.]
Now each time the curve reaches an intersection and turns **right**, we add the momentum
of the road coming from the **left** - so for _X_ 2 _,_ 5, it turns right in the first intersection, so we
add _p_ _[µ]_ 3 [,] [and] [right] [in] [the] [second] [intersection,] [so] [we] [also] [add] _[ p][µ]_ 4 [.] [If,] [instead,] [the] [curve] [turns]
left at an intersection, we don’t add anything. In the end, the momentum of the curve
is simply the sum of momentum obtained squared - so for _X_ 2 _,_ 5 we get ( _p_ 2 + _p_ 3 + _p_ 4) [2], as
expected.


**2.3.2** **Loop-level**


At loop level, we also start by assigning momentum to the boundary curves. However,

because of the presence of the puncture, we can now draw curves that are **not homologous**

to any boundary, for example, any curve going from a boundary-marked point to the

puncture. Therefore we need to assign a momentum to one of such curves - this is exactly
the loop momentum _l_ _[µ]_ (see figure 6, left).

As opposed to the case of tree-level, at loop-level we now have a genuine infinite family

of curves that are not homologous to each other. One way of seeing all such curves is to

consider a curve starting and ending in some boundary-marked points. At tree-level, all

such curves are unique, but in the presence of the puncture we can consider curves that

start and end in the same points but that wind around the puncture _n_ times and thus

self-intersecting _n_ times. In addition, another curve we can draw in the punctured disk

is a **closed** curve. This closed curve is homologous to the full boundary and so has zero

momentum. In any case, we will associate a variable, ∆, to this curve and it will turn out

to play an important role later.


12


**Figure** **7** : From curve to word: curve _X_ 2 _,_ 5.


Just like in the tree-level case, we can read off the momentum of any curve using the

fat graph. To do so we go from the curve to the lamination - note that for curves that

end in the puncture, the corresponding laminations spiral **counter-clockwise** around the

puncture an infinite number of times (see figure 6). Then we follow exactly the same rule
as in the tree-level case: so for _Y_ 1, we start by writing down _p_ _[µ]_ 1 [,] [then] [it] [turns] [right] [in] [the]
first intersection, so we add the momentum coming from the left which in this case is _l_ _[µ]_,

the loop momentum. Finally, it spirals around forever, and keeps turning left while doing

so, which means we don’t have to add any more momentum. Therefore we are left with
_Y_ 1 = ( _p_ 1 + _l_ ) [2] .
Having defined the mapping between the surface variables and the kinematic invariants,

we now have to understand what operation we need to do on the surface that gives us the

amplitude in terms of these variables.


**2.4** **From** **curves** **on** **the** **fat** **graph** **to** **words**


In this step, we want to find a way of encoding the information about the curves on the

surface of some new objects. These objects should be such that using them one is fully

able to reconstruct the surface as well as the curve in question.

To do this we use the fat graph defining the surface, and start by labelling its **roads**

according to the sides they touch (see figure 7 (left)).

Making use of this labelling, we can record the path of a given curve along the fat

graph by keeping track of the roads it goes through as well as whether it turns right or

left each time it reaches an intersection. So let’s establish the rule that for each left-turn

we go up, while for each right turn, we go down. By following this rule we build up a

mountainscape uniquely associated with the curve we follow, we call this object the **word** .

As an example, let’s consider a 5-point process at tree-level. Let’s pick the fat graph
with propagators _X_ 1 _,_ 3 and _X_ 1 _,_ 4, and look at the curve from 2 to 5 (see figure 7 (left)).
Following the curve, we see it enters the graph in road 23, then it turns **left** to 13, then

**right** to 14, and finally **right** to 45. Following the rule described in the previous paragraph,
we get the word for curve _X_ 2 _,_ 5 (see figure 7 (right)).


13


The words are the most basic objects defined on the surface that encode all the kine
matic data. The last step is to understand what manipulation we need to do on these

words to obtain the amplitude. This involves building the **u-variables** .


**2.5** **From** **words** **to** _u_ **-variables**


At tree-level, the _u_ -variables are well-studied objects in the literature, appearing already in

the earliest days of the dual resonance model in the work of Koba and Nielsen [19], in the

work of Francis Brown on the study of _ζ_ values from stringy integrals [20], and directly in

the context of binary geometries in [9]. One of the central discoveries of the curve integral

formalism [7] is the generalization of _u_ -variables to all surfaces. There are a number of ways

of doing this, either framed in the language of hyperbolic geometry, or more abstractly,

in terms of a simple counting problems associated with the words attached to curves on

surfaces. This counting problem approach is both the more elementary and deeper one, and

was summarized in [7]. A more systematic exposition of all the different ways of thinking

about _u_ variables from both the counting problem and hyperbolic geometry viewpoints,

aimed at physicists, will be given in [14, 18].
To each curve, C, on the surface we can associate a u-variable, _u_ C, that satisfies the
**u-equation** :
_u_ C + ∏ _u_ D [#int][(C] _[,]_ [D)] = 1 _,_ (2.3)
D

where the product is taken over all other curves D and #int(C _,_ D) the intersection number
between the two curves. For positive _u_ ’s, we see that all _u_ ’s are bounded by 1. In addition,
from equation (2.3), when _u_ C goes to zero, all the _u_ D, for the curves D that intersect C,
have to go to one. This **binary** behavior is crucial to ensure that amplitudes build out of

the _u_ ’s satisfy **factorization** near poles.

The _u_ -equations form a non-linear set of equations that make it obvious that the _u_  
variables are not independent of each other. So it is useful to find a good parametrization

of the space of solutions of the _u_ -equations. This is a non-trivial problem for which the

surface gives a very nice answer.

As we explained in 2.2, in order to define the surface one has to provide a fat graph,

dual to a triangulation of the surface. Of course, there are multiple fat graphs that describe
the same surface, in particular for an _n_ -point tree, there are Catalan _n_ −2 such possibilities.
Each choice of fat graph corresponds to a **positive** **parametrization** of the u-variables

that automatically satisfies the u-equations.

To obtain this parametrization we start by assigning variables to the internal roads of
the fat graph – the ones corresponding to the propagators, _yi_ . Now the _u_ ’s will be functions
of the _yi_ ’s, in particular, will be ratios of polynomials in the _yi_ ’s. To get these functions
we define two matrices:


_[y][i]_ [0]
_ML_ ( _yi_ ) = [ _[y][i]_ ; _MR_ ( _yi_ ) = [ _[y][i]_ (2.4)
0 1 []] 1 1 []] _[,]_


where _L_ and _R_ stand for left and right. To build the u-variable from some word, _WC_ of
some curve _C_, all we need to do is multiply these matrices in the order the curve tells


14


us to, _i.e._ each time it turns left/right at some road _yi_ we multiply by _ML_ ( _yi_ )/ _MR_ ( _yi_ ),
respectively. Any non-boundary curve starts in some boundary road and then turns left

or right into some internal road, since there is no _y_ associated with the starting boundary
road, the first matrix appearing _ML_ or _MR_ should be evaluated at 1. By the end of this,
we have a 2×2 matrix, whose entries are polynomials in the _y_ s, _mi,j_ ( _y_ ). The u-variable for
the curve is simply:
_uC_ = _[m]_ [1] _[,]_ [2][ ⋅] _[m]_ [2] _[,]_ [1] _._ (2.5)

_m_ 1 _,_ 1 ~~⋅~~ _m_ 2 _,_ 2


Let’s go through an example to see how the rule works in practice. Consider the 5-pt

tree level amplitude, so the disk with 5 punctures, and let’s get the u-variable for curve
_X_ 2 _,_ 5 (figure 7). In this case, the sequence of _L_ / _R_ matrices is:


[1] [0] [0] [1]
_ML_ (1) _MR_ ( _y_ 1 _,_ 3) _MR_ ( _y_ 1 _,_ 4) = [ [1] (2.6)
0 1 [][] _[y]_ [1] 1 _[,]_ [3] 1 [][] _[y]_ [1] 1 _[,]_ [4] 1 [] = [][1][ +] _[ y]_ [1] 1 _[,]_ + [4][ +] _y_ _[ y]_ 1 _,_ [1] 4 _[,]_ [3] _[y]_ [1] _[,]_ [4] 1 []] _[.]_


Hence from (2.5), we have:

1 + _y_ 1 _,_ 4
_u_ 2 _,_ 5 = _._ (2.7)
1 ~~+~~ _y_ 1 _,_ 4 ~~+~~ _y_ 1 _,_ 3 _y_ 1 _,_ 4


The _u_ variables for the “spiraling curves” into punctures are interesting. Let us denote
the chords in the triangulation hitting the puncture read counterclockwise as _y_ 1 [(] _[p]_ [)] _[,y]_ 2 [(] _[p]_ [)] _[,]_ [⋯] _[,y]_ _r_ [(] _[p]_ [)] .
Then any word corresponding to a spiraling curve will end with the infinite repeating up
ward sequence:



⋰

      - _y_ 1 [(] _[p]_ [)]
_yr_ [(] _[p]_ [)]
⋰

  - _y_ 2 [(] _[p]_ [)]
⋰ _y_ 1 [(] _[p]_ [)]



(2.8)



So at the end of the word, we encounter the matrix _M_ spiral = _ML_ ( _y_ 1 [(] _[p]_ [)][)] _[M][L]_ [(] _[y]_ 2 [(] _[p]_ [)][)⋯] _[M][L]_ [(] _[y]_ _r_ [(] _[p]_ [)] ),
which is raised to the _N_ ’th power with _N_ sent to infinity. Now it is easy to see that


_[N]_ _[N]_ [−][1]
spiral _[F]_ [spiral][(][1][ +] _[ Y]_ [spiral][ + ⋯+] _[ Y]_ spiral [)]
_M_ spiral _[N]_ [= (] _[ Y]_ ) _,_ (2.9)
0 1


where
_Y_ spiral = ( _y_ 1 [(] _[p]_ [)][⋯] _[y]_ _r_ [(] _[p]_ [)] ) _,_ _F_ spiral = _y_ 1 [(] _[p]_ [)] + _y_ 1 [(] _[p]_ [)] _[y]_ 2 [(] _[p]_ [)] + ⋯+ _y_ 1 [(] _[p]_ [)][⋯] _[y]_ _r_ [(] _[p]_ [)] _._ (2.10)

Not that in order for the geometric series to converge, we must have _Y_ spiral < 1 ⇔

∏ _i yi_ [(] _[p]_ [)] < 1. This is a restriction we must impose on the _yi_ [(] _[p]_ [)] above and beyond their
positivity.


15


If we call the matrix product for the part of the word before we begin spiraling as


_[b]_
_M_ before = ( _[a]_ (2.11)
_c_ _d_ [)] _[,]_

then if we take the _u_ variable for the matrix _M_ before _M_ spiral _[N]_ [and] [take] _[N]_ [→∞] [we] [find]

_u_ spiral = _[c]_ [(] _[aF]_ [spiral][ +] _[ b]_ [(][1][ −] _[Y]_ [spiral][))] (2.12)

_a_ ~~(~~ _cF_ spiral ~~+~~ _d_ ~~(~~ 1 ~~−~~ _Y_ spiral ~~))~~ _[.]_


**2.5.1** **u-variable** **for** **closed** **curve**


The rules described above allow us to obtain the _u_ variables for all curves defined on the

surface. We will also have occasion to define _u_ variables for closed curves around the

punctures, ∆, for which we put:


_u_ ∆ _I_ = (1 −∏ _yi_ [(] _[p][I]_ [)] ) _,_ (2.13)
_i_


where ∆ _I_ stands for the closed curve around puncture _I_, and _yi_ [(] _[p][I]_ [)] are the _y_ ’s present in the
underlying triangulation that go from one boundary point, _i_, and end in the puncture, _I_ .

For example, let’s consider again the punctured disk with 4 marked points on the boundary

- the 4-point one-loop amplitude. Choosing the box triangulation of figure 4, means we
have four chords going from the boundary to the puncture, _Y_ 1 _,Y_ 2 _,Y_ 3 and _Y_ 4. So in this
case, the u-variable for the closed curve is:

_u_ ∆ = (1 − _y_ 1 [(] _[p]_ [)] _[y]_ 2 [(] _[p]_ [)] _[y]_ 3 [(] _[p]_ [)] _[y]_ 4 [(] _[p]_ [)][)] _[.]_ (2.14)

Note this _u_ ∆ → 0 precisely when the product _Y_ spiral we encountered for spiraling _u_
variables hits the boundary _Y_ spiral → 1 we just saw above. So it is natural to have _u_ ∆
detect this boundary.

Using the relation between the _y_ and _u_ variables we will review just below, it is easy

to see that this definition is independent of the choice of triangulation; we have that
∏ _i yi_ [(] _[p]_ [)] = ∏ _Y_ _uY_ where the _Y_ denote all the curves spiraling at the puncture.


**2.6** **Summary** **of** _u_ **facts**


Here present a summary of a few facts about the _u_ variables that will be useful through
out the rest of the paper. These results are all borrowed from [18] where a systematic
understanding of these and many other properties of _u_ / _y_ variables will be given.


**2.6.1** _u_ **’s** **of** **sub-surfaces**

Suppose we have a surface S, and a subsurface _s_ contained inside it. (We can concretely
define a subsurface _s_ simply by giving its fat-graph as a subgraph of the parent fat-graph
for S). It is natural to wonder whether we can build out of the _u_ variables _u_ [(S)] for curves
C

C variables on the big surface S, a set of objects _u_ [(] _c_ _[s]_ [)] that satisfy the _u_ equations labelled
by curves _c_ on the smaller surface _s_ . This question has a beautiful and natural answer: we


16


**Figure** **8** : Smaller 4-point inside bigger surface.


can build _u_ variables for the small surface out of simple monomials in the _u_ variables for

the big one. Given a curve _c_ in _s_, we simply consider _all_ ways of extending _c_ into curves
on the big surface, C _c_ . Then we have

_u_ [(] _c_ _[s]_ [)] = ∏ _u_ [(S)] C _c_ _[.]_ (2.15)
all curves C _c,_ extending _c_ into S


**2.6.2** **Generalized** _u_ **-equations**


We have just seen that the _u_ variables for smaller surfaces _s_ can be expressed as monomials
in the _u_ variables of the big surface S. Thus the _u_ equations for the smaller surface _s_ turn
into new equations when these are expressed as monomials in the original surface S–these
are the _generalized_ _u_ _equations_ . For instance for the disk at tree-level, we can consider

the subsurface given by a 4-point fatgraph bounded by regions _i,a,j,b_ as in figure 8. The
curve ( _i,j_ ) in this 4-point subsurface extends to the bigger tree into all the curves ( _x,y_ )
with _x_ in the set between ( _i,a_ - 1) and _y_ in the set between ( _j,b_ - 1). Then we have
_u_ [(] _i,j_ [4][)] [= ∏] _[x]_ [⊂(] _[i,a]_ [−][1][)] _[,y]_ [⊂(] _[j,b]_ [−][1][)] _[ u][x,y]_ [.] [Similarly] [the] [curve] [(] _[a,b]_ [)] [in] [the] [subsurface] [extends] [to] [all] [the]

( _w,z_ ) with _w_ between ( _a,j_ - 1) and _z_ between ( _b,i_ - 1), so _u_ [(] _a,b_ [4][)] [= ∏] _[w]_ [⊂(] _[a,j]_ [−][1][)] _[,z]_ [⊂(] _[b,i]_ [−][1][)] _[ u][w,z]_ [.]
Then from the trivial 4-point _u_ equations we get a non-trivial expression for sums of

monomials in the parent _u_ ’s:

_u_ [(] _i,j_ [4][)] [+] _[ u]_ _a,b_ [(][4][)] [=][ 1][ →] ∏ _ux,y_ + ∏ _uw,z_ = 1 _._ (2.16)
_x_ ⊂( _i,a_ −1) _,y_ ⊂( _j,b_ −1) _w_ ⊂( _a,j_ −1) _,z_ ⊂( _b,i_ −1)


All the extended _u_ equations at tree-level can be summarized by a simple picture: we
divide all the indices going around the disk into four consecutive sets ( _A,B,C,D_ ). Then
the extended equations are _UA,C_ + _UB,D_ = 1, where _UA,C_ is the product of all the _ui,j_ with
_i_ in _A_ and _j_ in _C_, and _UB,D_ is the product of all _uk,l_ with _k_ in _B_ and _l_ in _D_ . The special
case where _A_ is the single _i_ and _C_ is the single _j_, with _B,D_ filling out the complementary


17


**Figure** **9** : _PX_ for different words.


indices, gives us the standard _u_ equation for _ui,j_ . As an example of a new generalized
_u_ equations for _n_ = 6 we can take _A_ = (1 _,_ 2) _,B_ = (3) _,C_ = (4) _,D_ = (5 _,_ 6), then we have
_u_ 1 _,_ 4 _u_ 2 _,_ 4 + _u_ 3 _,_ 5 _u_ 3 _,_ 6 = 1.


**2.6.3** _y_ **’s** **and** _u_ **’s**


We now explain how to express the product of all the _y_ ’s in terms of _u_ ’s, for any given

triangulation of the surface.

We can write each _y_ as a product of _u_ ’s in the following way:


_yi_ = ∏ _ugXX_ [(] _[i]_ [)] _[,]_ (2.17)
_X_


where _g_ [(] _[i]_ [)] [for] [the] _[i]_ [-th] [component] [of] [the] **[g-vector]** [corresponding] [to] [curve] _[X]_ [.] [We]
_X_ [stands]
can get _gX_ by looking at the corresponding word describing the curve. This word is a
mountainscape with some roads appearing as peaks, P, and others as valleys, V. These
peaks and valleys are always roads associated with the propagators of the underlying trian
gulation/ internal edges of the underlying fat-graph. To each such internal road we assign
a vector, _g_ ⃗ _i_, then the _g_ -vector of some curve, _X_, can be written as a linear combination of
_g_ ⃗ _i_ as follows:
_g_ ⃗ _X_ = −∑ _g_ ⃗ _I_ + ∑ _g_ ⃗ _J_ _._ (2.18)
_I_ ∈P _J_ ∈V

Therefore we have that _gX_ [(] _[i]_ [)] will either be ±1 depending on whether _i_ appears as a
valley or a peak in the word for _X_ . Ultimately, the product of all the _y_ ’s is simply:

∏ _yi_ = ∏ _u_ _[p]_ _X_ _[X]_ _[,]_ _pX_ ≡∑ _gX_ [(] _[i]_ [)] _[.]_ (2.19)
_i_ _X_ _i_


18


From (2.18), we have that _pX_ = # (valleys)  - # (peaks), appearing in the word for
curve _X_ . It turns out that _pX_ is completely determined by what the word looks like at
the boundaries since the net number of right/left turns in the middle must even out (see

figure 9).In summary, we have:



∏ _yI_ = ∏ _u_ _[P]_ _X_ _[X]_ _[,]_ with _pX_ =
_I_ _X_



⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩



+1 _,_ if _X_ turns _R_ at the start and _L_ at the end,

−1 _,_ if _X_ turns _L_ at the start and _R_ at the end,



0 _,_ otherwise.



(2.20)



**2.7** **“Stringy”** **amplitudes**


Now we want to explain how we can use the variables defined from the surface, such as the

curves and respective _u_ -variables, to build string amplitudes.


**2.7.1** **Tree-level**


String amplitudes are given as integrals over possible configurations of the string world
sheet. An _n_ -point string tree-level amplitude corresponds to an integral over the modulispace of real points _z_ 1 _,...,zn_ on the boundary of the disk [19, 21]:



d _z_ 1 _..._ d _zn_
A [tree,tachyon] _n_ (1 _,_ 2 _,...,n_ ) = ∫



_z_ 1 _..._ d _zn_

[∏] ( _ij_ ) [2] _[α]_ [′] _[k][i]_ [⋅] _[k][j]_
SL ~~(~~ 2 _,_ R ~~)~~ [×] _i_ < _j_



_,_ (2.21)




 - **�����������������** **�����������������**
Koba-Nielsen factor



with _z_ 1 < _z_ 2 < ⋅⋅⋅< _zn_, so that ( _ij_ ) = _zj_ - _zi_ - 0 for _i_ < _j_, _ki_ are the particle momenta and
_α_ [′] is the string constant. The worldsheet SL(2 _,_ R) invariance demands that _α_ [′] _ki_ [2] [= −][1] [and]
so the external states are tachyons with _m_ [2] = −( _α_ [′] ) [−][1] . [2] .
It turns out that the _zi_ ’s also define a parametrization of the solution to the _u_ equations
in which each _u_ variable is an SL(2,R) invariant cross-ratios of the ( _ij_ )’s defined as follows:

_ui,j_ = [(] _[i]_ [−][1] _[,j]_ [)(] _[i,j]_ [−][1][)] (2.22)

~~(~~ _i,j_ ~~)(~~ _i_ ~~−~~ 1 _,j_ ~~−~~ 1 ~~)~~ _[.]_


We can now express the integrand in terms of _u_ ’s, finding [5, 9, 10]:

d _[n]_ _zi_ /SL(2,R)
A [tree,tachyon] _n_ (1 _,_ 2 _,...,n_ ) = ∫ ~~(~~ 12 ~~)(~~ 23 ~~)(~~ 34 ~~)~~ _..._ ~~(~~ _n_ 1 ~~)~~ [∏] _i_ < _j_ _ui,j_ _[α]_ [′][(] _[x][i,j]_ [−][1][)] _,_ (2.23)

where the _xi,j_ = ( _ki_ + _..._ + _kj_ −1) [2] are the planar-variables made from the external tachyon
momenta. We will find it convenient to instead interpret this expression not as scattering
amplitudes for tachyons but for massless external scalars with momenta _pi_ with _p_ [2] _i_ [=] [0,]
simply by identifying the planar kinematic invariants for the massless problem _Xi,j_ = ( _pi_ +
⋯+ _pj_ −1) [2] with those of the tachyons _xi,j_ via _Xi,j_ = _xi,j_ - 1. Thus we study finally

d _[n]_ _zi_ /SL(2,R)
A [tree] _n_ (1 _,_ 2 _,...,n_ ) = ∫ ~~(~~ 12 ~~)(~~ 23 ~~)(~~ 34 ~~)~~ _..._ ~~(~~ _n_ 1 ~~)~~ [∏] _i_ < _j_ _u_ _[α]_ _i,j_ [′] _[X][i,j]_ _,_ (2.24)


2 2 2
We use the mostly-plus signature so that _k_ = − _m_ .


19


This is useful for talking about a “low-energy field theory limit”, something which doesn’t

make sense for tachyons whose mass is set by the string scale, but does make sense for
the massless _Xi,j_ kinematics (where we also set _Xi,i_ +1 = 0). Indeed the low-energy limit of
these “Parke-Taylor” or “ _Z_ -theory” amplitudes [22–24], where _α_ [′] _Xi,j_ ≪ 1, are just those
of massless Tr _ϕ_ [3] theory (2.2). For this reason we will refer to this as the bosonic string
Tr _ϕ_ [3] amplitude in the rest of this paper.
We can easily convert between the _zi_ and _yi_ variables that have both been used to give
parametrizations of the same _ui,j_ variables. Doing this we find that the “Parke-Taylor”
measure written in terms of the _zi_ variables simplifies to a “dlog form” in the _yi_, and the
string integral takes it’s simplest form as:



A [tree] _n_ (1 _,_ 2 _,...,n_ ) = ∫



∞



∏
0 _i_



d _yi_

_u_ _[α]_ [′] _[X][C]_ _,_ (2.25)
_yi_ [∏] _C_ _C_



where the product is taken over all the curves _C_ on the disk with _n_ -marked points on the
boundary, and _uC_ are the corresponding _u_ -variables parametrized by the _yi_ .


**2.7.2** **Loop-level**


The _n_ -point 1-loop amplitude in terms of surface variables is given exactly by (2.25) but

where the product is taken over all the curves of the punctured disk with _n_ marked points

on the boundary. As pointed out before, at 1-loop, there are now an infinite number

of curves coming from curves that self-intersect infinitely often. So we can rewrite this

product as follows:



A [1-loop] _n_ (1 _,_ 2 _,...,n_ ) = ∫



∞



∏
0 _i_



d _yi_

_u_ _[α]_ _C_ [′] _[X][C]_ × ∏ _u_ _[α]_ _C_ [′][′] _[X][C]_ [′] × _u_ [∆] ∆ _[,]_ (2.26)
_yi_ [∏] _C_ _C_ [′] ∈ S.I.



where the first product includes a finite number of terms corresponding to curves that never

self-intersect. The second product is an infinite product over all the self-intersecting curves

with different numbers of self-intersections. At last, we have the closed curve contribution,

∆.

A precise matching between this form of the amplitude and the conventional presenta
tion of tachyon bosonic string amplitudes through 1-loop will appear in [14]. But as stressed

in [7], at loop-level there are more options for “stringy” presentations of amplitudes at least

so long as we are primarily interested in matching the correct field theoretic low energy

limit. In particular, the contributions from the self-intersecting and closed curves are ir
relevant to the field theory or “tropical” limit of the amplitudes; indeed these curves don’t
even occur dually as propagators in any Tr _ϕ_ [3] diagrams. This means that if we are only

interested in the field theory limit, we can effectively use a truncated integrand where we

only keep the first product over non-self-intersecting curves. We emphasize again that this

truncated object is **not** the full string amplitude at loop level, rather it is a simpler but
still “stringy” object that correctly gives Tr _ϕ_ [3] amplitudes at low-energies.


**2.7.3** **Higher** **loops**


Beyond single-trace amplitudes at one loop, an important novelty appears with the first

non-planar amplitudes. For instance in the double-trace one-loop amplitudes, we have


20


infinitely many curves that we can draw on this fat graph: they differ from one another

only in how many times they wind around the graph. This is a consequence of the _mapping_

_class_ _group_ of the surface, which acts by increasing the winding of curves. In fact, this

infinity of windings is the heart of the well-known difficulty in defining a loop integrand

for non-planar amplitudes. Fortunately as described explicitly in [7, 8], it is easy to _mod_

_out_ by the action of the mapping class group, using the “ _Mirzakhani_ _trick_ ” [25]. This

is a version of the familiar Fadeev-Popov idea for modding out by gauge redundancies in
the path integral, and is accomplished by inserting a “ _Mirzakhani_ _Kernel_ ” _K_ ( _u_ ) into the
integration over the _y_ variables. We will not display these factors explicitly in the rest of

this paper, and they will not be relevant for the explicit two-loop computations we will

perform for leading singularities.


**2.7.4** **Integration** **Contour**

The stringy Tr _ϕ_ [3] integral is defined naively on the integration contour where 0 < _yi_ < ∞.
But this form only converges when the _Xi,j_ - 0; continuing to the physically interesting
region where we see resonances and the amplitude has poles, where _Xi,j_ < 0, is carried out
by analytic continuation.

This is a frustrating state of affairs. For four-point, the explicit expression in terms
of the Beta function (Γ( _X_ 1 _,_ 3)Γ( _X_ 2 _,_ 4))/Γ( _X_ 1 _,_ 3 + _X_ 2 _,_ 4) gives us the analytic continuation
and allows us to compute the amplitude everywhere, but for general _n_ -point scattering no

analytic formula is known and so the analytic continuation is not handed to us.

More conceptually, we would like to find the correct integration contour on which to
define this integral. The contour should agree with the naive one for 0 < _yi_ < ∞ when the
integral is convergent, but give us the correct analytic continuation everywhere.

This is essentially the subject of defining the _iϵ_ prescription for string amplitudes, and

a prescription for this contour was given by Witten in [26]. This prescription is essentially

“local” in character, describing a deformation of the contour in the neighborhood of all

possible singularities of the amplitude, ultimately associated with all the possible degener
ations of the surface equivalent to Feynman diagrams, and so involves a local analysis of

the integration domain with an amount of work that grows exponentially with the number

of particles.

Now we know that one of the purposes in life of the _u_ variables and their _y_ parametriza
tion is to explicitly “blow up” all possible degenerations of the surface, and thereby generate

these exponentially many degenerations from objects that are described only by at most
_O_ ( _n_ [2] ) variables. As will be described in much greater length [27], for this reason, the _u,y_
formalism is ideally suited to define the _iϵ_ contour in a one-shot “global” way. In practice,

this gives us a concrete contour prescription that can be written down once and for all, for

all _n_, on which all the integrals in our paper are convergent returning well-defined ampli
tudes. We defer a detailed discussion of this contour to [27], contenting ourselves here only

with illustrating how things work in the simplest case of four-particle scattering. Setting
_u_ 1 _,_ 3 = _y_ 1 _,_ 3/(1 + _y_ 1 _,_ 3) and _u_ 2 _,_ 4 = 1/(1 + _y_ 1 _,_ 3), we have one of the classic forms of the beta


21


function integral



_y_ 1 _,_ 3

_y_ 1 _[X]_ _,_ 3 [1] _[,]_ [3][(][1][ +] _[ y]_ [1] _[,]_ [3][)][−(] _[X]_ [1] _[,]_ [3][+] _[X]_ [2] _[,]_ [4][)] _[.]_ (2.27)
_y_ 1 _,_ 3



d _y_ 1 _,_ 3
0 _y_



A4 = ∫



∞



To define the analytic continuation we imagine giving _X_ 1 _,_ 3 _,X_ 2 _,_ 4 small imaginary parts,
i.e. setting _X_ 1 _,_ 3 → _X_ 1 [∗] _,_ 3 [+] _[ iϵ]_ [1] _[,]_ [3] [and] _[X]_ [2] _[,]_ [4][ →] _[X]_ 2 [∗] _,_ 4 [+] _[ iϵ]_ [2] _[,]_ [4] [where] _[X]_ 1 [∗] _,_ 3 _[,X]_ 2 [∗] _,_ 4 [are] [real.] [It] [is] [useful]
to change from the _y_ variables to the effective Schwinger parameter _y_ 1 _,_ 3 = _e_ [−] _[t]_ [1] _[,]_ [3] . The naive
contour 0 < _y_ 1 _,_ 3 < ∞ is then given by an integration over the entire real _t_ 1 _,_ 3 axis. It is
important that the contour goes to _t_ 1 _,_ 3 →+∞ to capture the pole in the amplitude as
_X_ 1 _,_ 3 → 0, and similarly that it goes to _t_ 1 _,_ 3 →−∞ to capture the pole in _X_ 2 _,_ 4. These are of
course also the degenerations where _u_ 1 _,_ 3 → 0 and _u_ 2 _,_ 4 → 0, respectively.
Now, the _iϵ_ contour is very natural in this Schwinger parameterization language. After

we proceed on the real axis for a little while, we tilt the contour up till it’s nearly vertical
in the complex _t_ 1 _,_ 3 plane for Re( _t_ 1 _,_ 3) > 0, but with a small tilt towards the right so it does
reach Re( _t_ 1 _,_ 3) →∞. Similarly, we tilt it down in the complex plane for Re( _t_ 1 _,_ 3) < 0. In
other words for some _t_ 1 _,_ 3 > _t_ [⋆] 1 _,_ 3 [,] [our] [contour] [can] [be] [parametrized] [as] _[t]_ [1] _[,]_ [3][(] _[ρ]_ [) =] _[ t]_ [∗] 1 _,_ 3 [+] _[ ρ]_ [(] _[i]_ [ +] _[ δ]_ [)]
with 0 < _ρ_ < ∞, for small _δ_ . The contour for negative values of Re( _t_ 1 _,_ 3) can be defined in a
similar way. This contour is a smooth deformation of the original one, but now gives us a

well-defined integral, provided _δ_ is chosen to be small enough. For instance on the right, as
_ρ_ becomes large, the integrand scales as exp[( _X_ 1 [∗] _,_ 3 [+] _[ iϵ]_ [1] _[,]_ [3][)(] _[ρ]_ [(] _[i]_ [ +] _[ δ]_ [))]][.] [The] [real] [part] [of] [the]
argument of the exponential is ( _X_ 1 [∗] _,_ 3 _[δ]_ [ −] _[ϵ]_ [1] _[,]_ [3][)] _[ρ]_ [.] [So] [no] [matter] [how] [negative] _[X]_ 1 [∗] _,_ 3 [becomes,]
we can make _δ_ small enough for the - _ϵ_ 1 _,_ 3 term to suppress the integrand as _ρ_ →∞. The
same thing holds for the left side of the contour. We can readily check that numerically

integrating along this contour gives us the correct result. Note that this natural contour
in _t_ 1 _,_ 3 translates in a pretty contour in _u_ 1 _,_ 3 = _e_ [−] _[t]_ [1] _[,]_ [3] /(1 + _e_ [−] _[t]_ [1] _[,]_ [3] ). The usual contour has _u_ 1 _,_ 3
covering the entire real line 0 < _u_ 1 _,_ 3 < 1. The new contour instead spirals around _u_ 1 _,_ 3 = 0 _,_ 1,
exactly as in Witten’s prescription [26]. The original and deformed contours in both _t_ 1 _,_ 3
and _u_ 1 _,_ 3 are shown in figure 10.
This example is too simple to illustrate the real power of the _u,y_ variables in defining

the _iϵ_ contour, which we will explain in more detail in [27]. But briefly, the point is that

essentially the same contour, only with some care taken in where the “turns” into the
complex plane are taken, can be chosen for each _yi_ independently. The magic of the _u,y_
variables then correctly implements the needed shifts to make the integrals convergent
in all degenerate limits, for precisely the same reason that the _ui,j_ ’s “blow up” all the
singularities as _ui,j_ → 0 and the _yi,j_ furnish a positive parametrization of the _ui,j_ . For
the purposes of this paper, this is enough to concretely specify a contour on which our

scaffolded gluon amplitudes can be concretely evaluated.


**2.7.5** **Low** **Energy** **Limit**

The _u_ / _y_ variable formalism makes it especially easy to take the low-energy limit _α_ [′] _Xi,j_ ≪ 1
of the stringy Tr _ϕ_ [3] integrals and extract the field theory limit of the amplitudes. The
reason is simply that the singularities in the _dy_ / _y_ measure are logarithmic, regulated by
the _u_ _[X]_ _X_ [factors.]


22


**Figure** **10** : _iϵ_ contour for the 4-point amplitude.


Putting _yi_ = _e_ [−] _[t][i]_, the naive integration runs over all real _ti_, and for _X_ → 0 we have
divergences at infinity in _t_ space. Thus for _α_ [′] _X_ ≪ 1 the integral is dominated by ∣ _t_ [⃗] ∣→
∞. In this limit, the _u_ variables simplify. Each _u_ is a ratio of polynomials in the _y_,
and the polynomials in turn simplify. In different cones in _t_ [⃗] space, corresponding to a
triangulation/diagram T when a collection of compatible _u_ variables all vanish together,
exactly because the incompatible _u_ ’s → 1, the integral in _t_ space becomes nothing than the
Schwinger parametrization for T and the integral is dominated by ∏X⊂T (1/ _X_ ) which is
just the contribution to the amplitude from the diagram T .
This shows that the field-theory limit of the stringy integrals matches the correct sum

over diagrams. The fact that we have an analytic representation of _u_ variables actually gives

us much more: an integral expression for the amplitude directly in the field-theory limit,

as an integral over a single object, just as the full stringy integral, but now interpreted

as giving a “global Schwinger parametrization” for the sum over all diagrams at once.
Returning to examining the stringy integrand as ∣ _t_ [⃗] ∣→∞, in different cones, one monomial
in the polynomials defining the _u_ ’s will dominate over others, and so _uX_ → exp _[α][X]_ [(] _[t]_ [)], where
_αX_ is a **piece-wise** **linear** function of the _ti_ that is called the “tropicalization” of _uX_,
which serves as the global Schwinger parameter for _X_ . This variable was also called the

“headlight function” in [7], to emphasize that it “lights up” in all the cones in _t_ space

compatible with the chord _X_ . Replacing the full stringy integrand by this “tropicalized”

version gives the correct field-theory limit. This gives a much more striking representation

of the amplitude without any reference to sum over diagrams.
As an example at 5-points, consider the polynomial (1 + _y_ 1 _,_ 4 + _y_ 1 _,_ 4 _y_ 1 _,_ 3) appearing in


23


the expression for the _u_ variables. Seeing _y_ 1 _,_ 3 = _e_ [−] _[t]_ [1] _[,]_ [3] _,y_ 1 _,_ 4 = _e_ [−] _[t]_ [1] _[,]_ [4], then as ∣ _t_ [⃗] ∣→∞ we have


∣ _t_ [⃗] ∣→∞
(1 + _e_ [−] _[t]_ [14] + _e_ [−] _[t]_ [14] _e_ [−] _[t]_ [13] ) ���→ _e_ [max][(][0] _[,]_ [−] _[t]_ [14] _[,]_ [−] _[t]_ [14][−] _[t]_ [13][)] _,_ (2.28)


and similarly for the other polynomials. In this way we can read off the _αX_, for instance



_u_ 2 _,_ 4 = [1][ +] _[ e]_ [−] _[t]_ [1] _[,]_ [4][ +] _[ e]_ [−] _[t]_ [1] _[,]_ [4] _[e]_ [−] _[t]_ [1] _[,]_ [3]

~~(~~ 1 ~~+~~ _e_ [−] _[t]_ [1] _[,]_ [3] ~~)(~~ 1 ~~+~~ _e_ [−] _[t]_ [1] _[,]_ [4] ~~)~~



∣ _t_ [⃗] ∣→∞
���→ _e_ _[α]_ [2] _[,]_ [4][(] _[t]_ [13] _[,t]_ [1] _[,]_ [4][)] _,_ (2.29)



where
_α_ 2 _,_ 4( _t_ [⃗] ) = max(0 _,_     - _t_ 1 _,_ 4 _,_     - _t_ 1 _,_ 4 − _t_ 1 _,_ 3) − max(0 _,_     - _t_ 1 _,_ 3) − max(0 _,_     - _t_ 1 _,_ 4) _,_ (2.30)


is the piece-wise linear global Schwinger parameter or “headlight function” associated with
the curve (2 _,_ 4). In this way the full 5-point tree amplitude can be written as a single
“tropical” integral,



A5[ _Xi,j_ ] = ∫



+∞



(2.31)
−∞ [d] _[t]_ [1] _[,]_ [3][ d] _[t]_ [1] _[,]_ [4] _[ e]_ [∑] _[i,j][ X][i,j]_ _[α][i,j]_ [(] _[t]_ [)] _[.]_



Furthermore, at loop-level, as familiar from Schwinger parametrization, the loop in
tegrations can be performed as Gaussian integrals, so we are left with a global Schwinger

parametrization of the sum of all loop diagrams at any given order in the topological

expansion.


**3** **Scalar-Scaffolded** **Gluons**


In this paper, we are unveiling a hidden direct connection between the seemingly “boring”
Tr _ϕ_ [3] theory and the much more exciting physics of gluon scattering amplitudes in Yang
Mills theory. Obviously the first order of business in making this connection is to answer

the simplest possible question: how can the basic kinematics for these theories possibly be

the same? After all, gluons have spin described by polarization vectors, which are obviously
missing in Tr _ϕ_ [3] theory. So how can gluons and scalars possibly be related?

This has been a constant source of tension in attempting to connect the world of

polytopes and curves on surfaces to real-world scattering amplitudes. The purely scalar
_Xi,j_ variable description of kinematics played a crucial role from the very outset of the
ABHY associahedron story, but there was seemingly no natural way to manually “add

polarization vectors” to include gluons. For one thing, due to gauge-redundancy, there was

no invariant way of doing this. And besides, adding any source of redundancy ran very
much counter to the spirit of the _Xi,j_, one of whose virtues was in giving a non-redundant
description of the momentum kinematics!

In this section we will describe an extremely simple but beautiful resolution to this basic

problem. We will describe _n_ gluon amplitudes in a purely scalar language using kinematic

_X_ variables, by imagining that we are scattering 2 _n_ colored scalars. There is always a pole
of the amplitude where the scalars (1 _,_ 2) fuse into an on-shell gluon1, scalars (3 _,_ 4) fuse to


24


**Figure** **11** : Three particle amplitude between two colored scalars and a gluon.


gluon2, and so on. The residue on this pole then gives us the _n_ −gluon amplitude [3] . For
obvious reasons, we will refer to this as “the scaffolding residue”.
We will show explicitly how to describe gluon scattering amplitudes for any [4] polar
izations in this scalar language. We will also discuss the constraints on functions of the
2 _n_ -gon _Xij_ variables, that allow us to interpret scaffolding residues as gluon amplitude,
satisfying both the constraints of on-shell gauge-invariance and multilinearity in the polar
ization vectors. Despite the fact that these two properties are physically very different, we

will see that they are both naturally unified in a single pretty mathematical statement.

We remark that the “scaffolding” method is a very general one, and can be used to

describe particles of any mass and spin, since we can always imagine producing the spinning

particles with a pair of scalars. We can for instance also “scaffold” gravitons, only the

scaffolded avatar of the gauge-invariance/multilinearity conditions will change. Similarly

we can scaffold massive string states, with some extra care to be taken to disentangle mass

degeneracy in the string spectrum.

But while the basic strategy is essentially trivial, the scaffolding picture allows us to

talk about seemingly very different amplitudes in the same kinematical language. It is this

ability that allows us to bring the highly non-trivial relations between the amplitudes for

very different theories to light.


**3.1** **From** 2 _n_ **scalars** **to** _n_ **gluons**

The scalars we consider interact with gluons via the unique three-point coupling: _g_ YM( _p_ 2 −
_p_ 1) _[µ]_, as depicted in figure 11. If we start with a 2 _n_ -scalar scattering process and take _n_
residues to make all the gluons (produced by adjacent scalars) on-shell, we land on the

_n_ -gluon amplitude.

Explicitly, to get the _n_ -point gluon amplitude we take residues on the simple poles
corresponding to _X_ 1 _,_ 3 = _X_ 3 _,_ 5 = _X_ 5 _,_ 7 = _..._ = _X_ 2 _n_ −1 _,_ 1 = 0, or equivalently, in terms of the


3 2
Note that in order for the massless residue on ( _pi_ + _pi_ +1) → 0 to _only_ be given by factorization on the
gluon pole, we further have to assume that there are no cubic interactions between these scalars. This can
be trivially arranged with the _Z_ 2 symmetry flipping the sign of every scalar. It also automatically occurs
from one of the natural origins for these scalars from higher-dimensional gluons
4 2
Strictly speaking we will describe _null_ polarization vectors _ϵ_ = 0. Of course, these provide a basis for

all possible polarizations.


25


momentum, ( _p_ 1 + _p_ 2) [2] = ( _p_ 3 + _p_ 4) [2] = ( _p_ 5 + _p_ 6) [2] = _..._ = ( _p_ 2 _n_ −1 + _p_ 2 _n_ ) [2] = 0, which is exactly
the condition to have the intermediate particles, in this case the gluons, on-shell. This

procedure is illustrated in figure 12 for the case of a 5-point gluon amplitude.

At tree-level, making the external gluons on the shell is enough to ensure that all

the internal particles are gluons as well. For this reason, by taking this residue we are

automatically left with the **tree-level** **pure** **gluon** **amplitude** . From this point onward,

we will denote this residue that takes us from the scalar 2 _n_ -gon to the gluon _n_ -gon, as the

**scaffolding** **residue**, for purely pictorial reasons inspired by figure 12.

However, exactly because we are still starting from a scalar scattering, all the gluon

information in the n-point amplitude left after taking the scaffolding residue is now encoded

in scalar language, and so all the explicit dependence on polarizations characteristic of gluon

amplitudes is less manifest. So we need to understand how we can extract this information

from the starting scalar process.

For the rest of this section, we will explain how the information about the gluons is
encoded in the _Xi,j_ ’s as well as understand how the properties of gluon amplitudes such as
gauge invariance and multilinearity in each polarization are manifest in what we get from

the scaffolding residue of the 2 _n_ -scalar amplitude.


**3.1.1** **Counting** **number** **of** **degrees** **of** **freedom**


As a sanity check, let’s start by checking that after taking the 2 _n_ scaffolding residue the

number of degrees of freedom left in the scalar problem, matches that of an n-point gluon
problem. Originally, for the scattering of these 2 _n_ -scalars, we have a total of 2 _n_ (2 _n_ - 3)/2
independent planar Mandelstams, _Xi,j_ . After taking the scaffolding residue, we fix _n_ of
these variables to zero, so we have 2 _n_ (2 _n_ - 3)/2 − _n_ = 2 _n_ (2 _n_ - 4)/2 degrees of freedom
left. For an n-point gluon problem, we have _n_ ( _n_ - 3)/2 independent planar Mandelstams,
_n_ ( _n_ - 1)/2 possible _ϵi_ ⋅ _ϵj_, and _n_ ( _n_ - 1) − _n_ = _n_ ( _n_ - 2) = _n_ (2 _n_ - 2)/2 different _ϵi_ ⋅ _pj_ . So
summing these three: (4 _n_ [2] −8 _n_ )/2 = 2 _n_ (2 _n_ −4)/2, which agrees with the scaffolding residue,
as expected.

Let’s now proceed and see in detail how to extract the gluon amplitude from the

2 _n_ -scalar amplitude, via this residue.


**3.2** **Polarizations** **and** **momenta** **of** **the** **gluons**


Let’s now understand how the polarizations and momentum of the gluons are encoded in
the planar variables _Xi,j_ of the scaffolding scalars. To do so, we focus on a single gluon of
the full process, see figure 13. By momentum conservation, we can read off directly that
the momentum of the incoming gluon is going to be _qi_ _[µ]_ [= (] _[p]_ [2] _[i]_ [−][1] [+] _[p]_ [2] _[i]_ [)] _[µ]_ [, which satisfies] _[ q]_ _i_ [2] [=][ 0]
on the scaffolding residue. So we have _q_ 1 _[µ]_ [= (] _[p]_ [1][ +] _[ p]_ [2][)] _[µ]_ [.] [By] [convention,] [we] [will] [always] [use]
_q_ to denote the momentum of the gluons and _p_ the momentum of the scaffolding scalars.
As for the polarization vector, _ϵi_, of course it isn’t uniquely fixed but can be shifted by
gauge transformations, whose geometric interpretation we will give in a moment. But one
symmetrical choice for _ϵi_ is the one familiar from the Feynman rule for the 3-point vertex
between the scalars and the gluon, which gives us _ϵ_ _[µ]_ _i_ [∝(] _[p]_ [2] _[i]_ [ −] _[p]_ [2] _[i]_ [−][1][)] _[µ]_ [.] [On] [the] [scaffolding]
residue, it satisfies _ϵi_ ⋅ _pi_ = 0, as necessary for on-shell gluons. It also satisfies _ϵ_ [2] _i_ [=] [0,] [so]


26


**Figure** **12** : Scaffolding residue from 10-scalar amplitude to 5-gluon.


**Figure** **13** : Polarization and momentum of scaffolded gluon.


we are describing generalized “circular polarizations”; this is not a restriction since these

furnish a basis for all possible polarization states.

To better understand the geometrical meaning of the polarizations, it is useful to label
the edges of the momentum polygon by vectors _Xi_ _[µ]_ [,] [such] [that] _[p][µ]_ _i_ [= (] _[X][i]_ [+][1][ −] _[X][i]_ [)] _[µ]_ [.] [In] [terms]
of these variables we have:

_ϵ_ _[µ]_ 1 [∝(] _[X]_ [3][ −] _[X]_ [2][)] _[µ]_ [ −(] _[X]_ [2][ −] _[X]_ [1][)] _[µ]_ [ ∝] _[X]_ 2 _[µ]_ [−] [(] _[X]_ [3][ +] _[ X]_ [1][)] _[µ]_ _._ (3.1)

2


So we can see that the information about the polarizations is also included in the

momentum polygon: they correspond to the vectors going from the midpoint of the triangle

to the extra edge in the scaffolding (see figure 14). Picking this particular representation of

the polarization vectors gives a misleading significance to the midpoint, however, as we will


27


**Figure** **14** : Polarizations of scaffolded gluons.


see, invariance under gauge transformations tells us precisely that the polarization vector

can be attached anywhere on this edge.


**3.3** **Unified** **form** **of** **gauge** **invariance** **and** **multi-linearity**


We now want to see what the statements about gauge invariance and multi-linearity translate to in the scalar degrees of freedom, _Xi,j_ . Let’s start with **gauge** **invariance** . To avoid
cumbersome indices, we will study gauge invariance for gluon 1, but all translate to the
_i_ th gluon by replacing 1 by 2 _i_ - 1, 2 by 2 _i_, etc.
Invariance under gauge transformations tells us:

_ϵ_ _[µ]_ 1 [→] _[ϵ]_ 1 _[µ]_ [+] _[ αq]_ 1 _[µ]_ ⇒ _δ_ A = 0 ∀ _α,_ (3.2)


which can be phrased in terms of the momentum of the 2n-scalars as


( _p_ 2 − _p_ 1) _[µ]_ →( _p_ 2 − _p_ 1) _[µ]_ + _α_ ( _p_ 1 + _p_ 2) _[µ]_ ⇒ _δ_ A = 0 ∀ _α._ (3.3)


Now we want to understand what this shift means in terms of the _Xi,j_ since these are
the variables the amplitude depends on. To do this, let’s express the gauge transformations
in terms of the variables _Xi_ _[µ]_ [:]



( _X_ 2 − _[X]_ [1][ +] _[ X]_ [3]




_[ X]_ [3] _µ_

) + _α_ ( _X_ 3 − _X_ 1) _[µ]_ _,_ (3.4)
2




_[ X]_ [3] _µ_

) →( _X_ 2 − _[X]_ [1][ +] _[ X]_ [3]
2 2



which is equivalent to simply shifting _X_ 2 _[µ]_ [as] [follows:]

_X_ 2 _[µ]_ [→] _[X]_ 2 _[µ]_ [+] _[ α]_ [(] _[X]_ [3][ −] _[X]_ [1][)] _[µ][.]_ (3.5)


Geometrically, gauge invariance is then equivalent to the statement that we are allowed
to move the base point of the polarization of gluon _i_ along _X_ 2 _[µ]_ _i_ −1 _,_ 2 _i_ +1 [,] [see] [figure] [15][.]


28


**Figure** **15** : Gauge Transformations.


Indeed, while we have emphasized a “top-down” picture of the scalar scaffolding, start
ing with the idea of using pairs of colored scalars to fuse into gluons, we can also very nicely

motivate the scaffolding idea from the bottom-up. So let’s start from the beginning just
with the data for _n_ gluons–their momenta _pi_ and polarization vectors _ϵi_ . We can use the _pi_
to draw the momentum polygon as usual. But it is also natural to record the information
about the polarization vectors simply by placing the end of the vector _ϵi_ somewhere on
the edge _pi_ of the momentum polygon. This immediately defines our 2 _n_ -gon, on the locus
where _X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,_ ⋯= 0 reflecting _p_ [2] _i_ [=][ 0.] [Since] [there] [is] [no] [invariant] [place] [on] [the] [edge] _[p][i]_ [to]
place _ϵi_, it is natural to demand that any question we ask of this 2 _n_ -gon should be invariant
under shifting where we place the endpoint of _ϵi_, and of course very nicely shifting this
endpoint is precisely gauge-invariance _ϵ_ _[µ]_ _i_ [→] _[ϵ]_ _i_ _[µ]_ [+] _[αp]_ _i_ _[µ]_ [.] [As an aside, the on-shell field-strength]
_fi_ _[µν]_ = _p_ _[µ]_ _i_ _[ϵ]_ _i_ _[ν]_ [−] _[p]_ _i_ _[ν][ϵ]_ _i_ _[µ]_ [has] [an] [obvious] [and] [pretty] [geometric] [interpretation] [as] [well–it] [is] [simply]
the antisymmetric tensor determined by the plane formed, ( _X_ 2 _i_ −1 _,X_ 2 _i,X_ 2 _i_ +1).
Ultimately this transformation will produce a shift in the planar variables involving
_X_ 2 _[µ]_ [which] [can] [be] [derived] [as] [follows:]



( _X_ 2 _[µ]_ [−] _[X]_ _j_ _[µ]_ [) →(] _[X]_ 2 _[µ]_ [−] _[X]_ _j_ _[µ]_ [) +] _[ α]_ [(] _[X]_ 3 _[µ]_ [−] _[X]_ 1 _[µ]_ [)]



⇒( _X_ 2 _[µ]_ [−] _[X]_ _j_ _[µ]_ [)(] _[X]_ [2] _[µ]_ [ −] _[X][jµ]_ [) →(] _[X]_ 2 _[µ]_ [−] _[X]_ _j_ _[µ]_ [)(] _[X]_ [2] _[µ]_ [ −] _[X][jµ]_ [) +] _[ α]_ [(] _[X]_ 3 _[µ]_ [−] _[X]_ 1 _[µ]_ [)(] _[X]_ [2] _[µ]_ [ −] _[X][jµ]_ [)]



(3.6)



⇒ _X_ 2 _,j_ → _X_ 2 _,j_ + _α_ ( _X_ 3 _,j_ - _X_ 1 _,j_ ) _._



So we can state gauge invariance in gluon _i_ th as

A[ _X_ 2 _i,j_ → _X_ 2 _i,j_     - _α_ ( _X_ 2 _i_ +1 _,j_     - _X_ 2 _i_ −1 _,j_ )] −A[ _X_ 2 _i,j_ ] = 0 _._ (3.7)


29


In addition, we know the amplitude, _A_ 2 _n_, should be **multi-linear** in each polarization:

_ϵ_ _[µ]_ _i_ [→] _[ϵ]_ _i_ _[µ]_ [+] _[ βϵ]_ _i_ _[µ]_ ⇒ _δ_ A = _β_ A _._ (3.8)


Again, let’s see what this translates to in scalar language for gluon 1. Rewriting this
in terms of _Xi_ _[µ]_ [yields]



( _X_ 2 − _[X]_ [1][ +] _[ X]_ [3]




_[ X]_ [3] _µ_

) + _β_ ( _X_ 2 − _[X]_ [1][ +] _[ X]_ [3]
2 2




_[ X]_ [3] _µ_

) →( _X_ 2 − _[X]_ [1][ +] _[ X]_ [3]
2 2




_[ X]_ [3] _µ_

) _,_ (3.9)
2



which is equivalent to

2 [−] _[X]_ 1 _[µ]_ [)] 2 [−] _[X]_ 3 _[µ]_ [)]
_X_ 2 _[µ]_ [→] _[X]_ 2 _[µ]_ [+] _[β]_ [(] _[X]_ _[µ]_ + _[β]_ [(] _[X]_ _[µ]_ _._ (3.10)
2 2


Proceeding as we did in (3.6), we get that the _X_ 2 _,j_ transform as



_X_ 2 _,j_ → _X_ 2 _,j_ + _[β]_ [(] _[X]_ [2] _[,j]_ [ −] _[X]_ [1] _[,j]_ [)]




[ −] _[X]_ [1] _[,j]_ [)]

+ _[β]_ [(] _[X]_ [2] _[,j]_ [ −] _[X]_ [3] _[,j]_ [)]
2 2



_,_ (3.11)
2



and so linearity in polarization _i_ th can be restated as:




_[β]_ _[β]_

2 [(] _[X]_ [2] _[i,j]_ [ −] _[X]_ [2] _[i]_ [−][1] _[,j]_ [) +] 2



A[ _X_ 2 _i,j_ → _X_ 2 _i,j_ + _[β]_




_[β]_ [(3.12)]

2 [(] _[X]_ [2] _[i,j]_ [ −] _[X]_ [2] _[i]_ [+][1] _[,j]_ [)] −A[] _[X]_ [2] _[i,j]_ [] =] _[ β]_ [A[] _[X]_ [2] _[i,j]_ []] _[.]_



Combining **gauge** **invariance** and **multi-linearity** for gluon 1, we get:




[ −] _[X]_ [1] _[,j]_ [)]

+ _[β]_ [(] _[X]_ [2] _[,j]_ [ −] _[X]_ [3] _[,j]_ [)]
2 2



A[ _X_ 2 _,j_ → _X_ 2 _,j_ + _[β]_ [(] _[X]_ [2] _[,j]_ [ −] _[X]_ [1] _[,j]_ [)]




_[X]_ [3] _[,j]_

+ _α_ ( _X_ 3 _,j_    - _X_ 1 _,j_ )] −A[ _X_ 2 _,j_ ] = _β_ A[ _X_ 2 _,j_ ]
2



⇔ A[ _X_ 2 _,j_ → _X_ 2 _,j_ + ( _[β]_




_[β]_

2 [+] _[ α]_ [)(] _[X]_ [2] _[,j]_ [ −] _[X]_ [1] _[,j]_ [) + (] _[β]_ 2




_[β]_

2 [−] _[α]_ [)(] _[X]_ [2] _[,j]_ [ −] _[X]_ [3] _[,j]_ [)] −A[] _[X]_ [2] _[,j]_ [] =] _[ β]_ [A[] _[X]_ [2] _[,j]_ []] _[.]_



(3.13)
Picking _α_ = ± _β_ /2, we get:



A[ _X_ 2 _,j_ → _X_ 2 _,j_ + _β_ ( _X_ 2 _,j_ - _X_ 1 _,j_ )] −A[ _X_ 2 _,j_ ] = _β_ A[ _X_ 2 _,j_ ] _,_

A[ _X_ 2 _,j_ → _X_ 2 _,j_ + _β_ ( _X_ 2 _,j_ - _X_ 3 _,j_ )] −A[ _X_ 2 _,j_ ] = _β_ A[ _X_ 2 _,j_ ] _._ (3.14)



This is then the unified form of the statements for both multilinearity and gauge
invariance: we have a rescaling symmetry under shifting _X_ 2 _,j_ by either of its neighbors
_X_ 1 _,j_ or _X_ 3 _,j_ . The shift by _X_ 1 _,j_ tells us that the amplitude must be expressible as

A = ∑ ( _X_ 2 _,j_         - _X_ 1 _,j_ ) × Q2 _,j,_
_j_ ≠{1 _,_ 2 _,_ 3}

A = ∑ ( _X_ 2 _,j_         - _X_ 3 _,j_ ) × Q [˜] 2 _,j,_ (3.15)
_j_ ≠{1 _,_ 2 _,_ 3}

where Q2 _,j,_ Q [˜] 2 _,j_ some function of the kinematics, _Xi,j_, but **independent** of _X_ 2 _,j_ . This
tells us they are equal:
Q2 _,j_ = Q [˜] 2 _,j_ = _∂X_ 2 _,j_ A _._ (3.16)


30


In summary, translating this property for a general gluon _i_, we conclude that the

amplitude **must** be of the form:

A [gluon] _n_ = ∑ ( _X_ 2 _i,j_      - _X_ 2 _i_ −1 _,j_ ) × Q2 _i,j_
_j_ ≠{2 _i_ −1 _,_ 2 _i,_ 2 _i_ +1}

_,_ (3.17)
= ∑ ( _X_ 2 _i,j_            - _X_ 2 _i_ +1 _,j_ ) × Q2 _i,j._
_j_ ≠{2 _i_ −1 _,_ 2 _i,_ 2 _i_ +1}

where Q2 _i,j_ is function of the remaining kinematics, **independent** of _X_ 2 _i,j_ . As pointed out
before and is made clear in this section, gluon amplitudes expressed in terms of the scalar

data have a **unique** form, that makes gauge invariance manifest, without introducing any

redundancies in the representation.


**3.4** **Dictionary:** **From** **scalar** **to** **gluon** **kinematics**


In this section we present a systematic way of mapping from the scalar kinematic invariants
of the scaffolding 2 _n_ -gon into the momenta, _qi_, and polarizations, _ϵi_, of the gluons we obtain
after extracting the scaffolding residue.
Note that all the _Xi,j_ with _i_ and _j_ **odd**, _Xo,o_, correspond to chords living inside the
_n_ -gon, and thus are the planar variables of the _n_ gluon problem:

_X_ 2 _i_ −1 _,_ 2 _j_ −1 = ( _qi_ + _qi_ +1 + ⋅⋅⋅+ _qj_ −1) [2] ≡ _Xi,j_ [g] _[,]_ (3.18)

where _X_ 2 _i_ −1 _,_ 2 _i_ +1 = ( _p_ 2 _i_ −1+ _p_ 2 _i_ ) [2] = _qi_ [2] [=][ 0 on the scaffolding residue.] [As usual, these] _[ n]_ [(] _[n]_ [−][3][)/][2]
planar variables are related to the same number of linearly independent Mandelstam vari
ables of _n_ gluons via

  - 2 _qi_ ⋅ _qj_ = _Xi,j_ [g] [+] _[ X]_ _i_ [g] +1 _,j_ +1 [−] _[X]_ _i,j_ [g] +1 [−] _[X]_ _i_ [g] +1 _,j_ [⇔]

(3.19)

  - 2( _p_ 2 _i_ −1 + _p_ 2 _i_ ) ⋅( _p_ 2 _j_ −1 + _p_ 2 _j_ ) = _X_ 2 _i_ −1 _,_ 2 _j_ −1 + _X_ 2 _i_ +1 _,_ 2 _j_ +1 − _X_ 2 _i_ −1 _,_ 2 _j_ +1 − _X_ 2 _i_ +1 _,_ 2 _j_ −1 _._


Let’s now work out the relations between the remaining planar variables: _Xe,e_ and
_Xe,o_, and the gluon data, _i.e._ (linearly independent) products of the form _ϵi_ ⋅ _ϵj_, _ϵi_ ⋅ _qj_ . In
the previous section, we saw that the polarization of each gluon could be associated with

a vector starting at the midpoint of the edge of the gluon _n_ -gon and ending on the vertex

of the scalar 2 _n_ -gon. However, gauge invariance tells us that the polarization vector does

**not** have to lie at the midpoint, and can lie in any point along the gluon edge, allowing us

to write:
_ϵi_ = (1 − _α_ ) _p_ 2 _i_                       - _αp_ 2 _i_ −1 _,_ (3.20)

for an arbitrary parameter _α_ . Recall that _qi_ _[µ]_ [= (] _[p]_ [2] _[i]_ [ +] _[ p]_ [2] _[i]_ [−][1][)] _[µ]_ [,] [thus] _[ϵ]_ [2] _i_ [=] _[ ϵ][i]_ [ ⋅] _[q][i]_ [ =][ 0] [exactly] [on]
the scaffolding residue. The choice of midpoint corresponds to _α_ = 1/2, but let us keep _α_
generic. Both the momentum and polarization of the _i_ th gluon can be expressed in terms

of the vertices of the 2 _n_ -gon as

_ϵ_ _[µ]_ _i_ [∝(][1][ −] _[α]_ [)(] _[X]_ [2] _[i]_ [+][1][ −] _[X]_ [2] _[i]_ [)] _[µ]_ [ −] _[α]_ [(] _[X]_ [2] _[i]_ [ −] _[X]_ [2] _[i]_ [−][1][)] _[µ][,]_ (3.21)

_qi_ _[µ]_ [∝(] _[X]_ [2] _[i]_ [+][1][ −] _[X]_ [2] _[i]_ [)] _[µ]_ [ + (] _[X]_ [2] _[i]_ [ −] _[X]_ [2] _[i]_ [−][1][)] _[µ]_ [ = (] _[X]_ [2] _[i]_ [+][1][ −] _[X]_ [2] _[i]_ [−][1][)] _[µ][ .]_ (3.22)


31


Note that _qi_ _[µ]_ [only depends on “odd” vertices] _[ X]_ [1] _[,X]_ [3] _[,]_ [⋯] _[,X]_ [2] _[n]_ [−][1][, thus] _[ ϵ][i]_ [ ⋅] _[q][j]_ [must depend]
on _Xk,l_ with at least one of _k,l_ being odd. This means that the only dependence on _Xe,e_
is through _ϵi_ ⋅ _ϵj_ - this will be important shortly. The remaining Lorentz products can be
expressed in terms of _X_ ’s as follows: Using (3.21) and (3.22) we can write the remaining

gluon kinematics as

2 _ϵi_ ⋅ _ϵj_ =(1 − _α_ )(−(1 − _α_ ) _X_ 2 _i_ +1 _,_ 2 _j_ +1 − _αX_ 2 _i_ −1 _,_ 2 _j_ +1 − _αX_ 2 _i_ +1 _,_ 2 _j_ −1 + _X_ 2 _i,_ 2 _j_ +1 + _X_ 2 _i_ +1 _,_ 2 _j_ )

(3.23)

    - _α_ [2] _X_ 2 _i_ −1 _,_ 2 _j_ −1 + _αX_ 2 _i,_ 2 _j_ −1 + _αX_ 2 _i_ −1 _,_ 2 _j_    - _X_ 2 _i,_ 2 _j,_

2 _ϵi_ ⋅ _qj_ =(1 − _α_ ) _X_ 2 _i_ +1 _,_ 2 _j_ −1 −(1 − _α_ ) _X_ 2 _i_ +1 _,_ 2 _j_ +1 + _αX_ 2 _i_ −1 _,_ 2 _j_ −1 − _αX_ 2 _i_ −1 _,_ 2 _j_ +1
(3.24)
+ _X_ 2 _i,_ 2 _j_ +1 − _X_ 2 _i,_ 2 _j_ −1 _,_

with _X_ 1 _,_ 3 = _X_ 3 _,_ 5 = _..._ = _X_ 2 _n_ −1 _,_ 1 = 0 and _Xi,i_ = _Xi,i_ +1 = 0. Again by plugging in _α_ = 2 [1] [we]

recover the special midpoint choice above. If, instead, we choose _α_ = 0 or 1 both equations
simplify, _e.g._, for _α_ = 1 we have

2 _ϵi_ ⋅ _ϵj_ = _X_ 2 _i,_ 2 _j_ −1 + _X_ 2 _i_ −1 _,_ 2 _j_       - _X_ 2 _i_ −1 _,_ 2 _j_ −1 − _X_ 2 _i,_ 2 _j_ = − _c_ 2 _i_ −1 _,_ 2 _j_ −1 _,_ (3.25)

2 _ϵi_ ⋅ _qj_ = _X_ 2 _i,_ 2 _j_ +1 − _X_ 2 _i,_ 2 _j_ −1 + _X_ 2 _i_ −1 _,_ 2 _j_ −1 − _X_ 2 _i_ −1 _,_ 2 _j_ +1 _._


Note that if and only if an expression of Lorentz products is **gauge** **invariant** and

**multilinear** in all _ϵ_ ’s, the corresponding expression in _X_ ’s becomes independent of the
parameter _α_ . On the other hand, by solving (3.23) and (3.24) we can express all _Xe,e_ and
_Xe,o_ in terms of a basis of Lorentz products, and vice-versa.


**3.5** **3-point** **gluon** **amplitude** **in** **scalar** **language**


To finish this section, we want to provide an example of a gluon amplitude written in this
scalar language. So will consider the 3−point gluon amplitude that is extracted from a
6−point scalar process.
Using (3.23) and (3.24) for _n_ = 3, _e.g._ with _α_ = 1 we have

2 _ϵ_ 1 ⋅ _ϵ_ 2 = _X_ 1 _,_ 4 − _X_ 2 _,_ 4 _,_ 2 _ϵ_ 2 ⋅ _ϵ_ 3 = _X_ 3 _,_ 6 − _X_ 4 _,_ 6 _,_ 2 _ϵ_ 3 ⋅ _ϵ_ 1 = _X_ 2 _,_ 5 − _X_ 2 _,_ 6 _,_

(3.26)
2 _ϵ_ 1 ⋅ _q_ 2 = _X_ 2 _,_ 5 _,_ 2 _ϵ_ 2 ⋅ _q_ 3 = _X_ 1 _,_ 4 _,_ 2 _ϵ_ 3 ⋅ _q_ 1 = _X_ 3 _,_ 6 _._


At 3-points we have two different types of interactions: the Yang-Mills (YM) vertex,
A [YM] 3, and the _F_ [3] vertex, A _[F]_ 3 [ 3][.] [Using] [(][3.26][),] [we] [can] [write] [A][YM] 3 in terms of _X_ ’s as

_A_ [YM] 3 (1 _,_ 2 _,_ 3) = −( _X_ 2 _,_ 5 − _X_ 2 _,_ 6) _X_ 1 _,_ 4 −( _X_ 3 _,_ 6 − _X_ 4 _,_ 6) _X_ 2 _,_ 5 −( _X_ 1 _,_ 4 − _X_ 2 _,_ 4) _X_ 3 _,_ 6 _,_ (3.27)


which become nicely


_A_ [YM] 3 (1 _,_ 2 _,_ 3) = −4( _ϵ_ 1 ⋅ _ϵ_ 3 _ϵ_ 2 ⋅ _q_ 3 + _ϵ_ 2 ⋅ _ϵ_ 3 _ϵ_ 1 ⋅ _q_ 2 + _ϵ_ 1 ⋅ _ϵ_ 2 _ϵ_ 3 ⋅ _q_ 1) _._ (3.28)

Similarly, for the 3-point _F_ [3] amplitude,   - _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 6, we find

_A_ _[F]_ 3 [ 3][(][1] _[,]_ [2] _[,]_ [3][) = −][8] _[ ϵ]_ [1] [⋅] _[q]_ [2] _[ϵ]_ [2] [⋅] _[q]_ [3] _[ϵ]_ [3] [⋅] _[q]_ [1] _[.]_ (3.29)


32


**4** **Tree-level** **Gluon** **Amplitudes**


Having learned how to describe the kinematics of gluon scattering amplitudes in a scalar

language–thinking of each gluon as being “scaffolded” by a pair of colored scalars–we now

turn to dynamics, and make our proposal for gluon scattering amplitudes.

We start at tree-level, and define a stringy integral representation of scaffolded gluon
amplitudes as a very simple deformation of the stringy Tr _ϕ_ [3] as [12]:



A2 _n_ (1 _,_ 2 _,...,_ 2 _n_ )[ _Xi,j_ ] = ∫



∞




_[u][i,j]_
( [∏][(] _[i,j]_ [)∈][even] ) _,_ (4.1)

∏( _i,j_ )∈odd _ui,j_



∏
0 C∈T



d _y_ C



_y_ C

_y_ C [∏] _i_ < _j_ _u_ _[α]_ _ij_ [′] _[X][i,j]_




- **�������������������������** - **�������������������������** Integrand of (2.24)



where _y_ C corresponds to the positive parametrization associated with triangulation T of the
disk with 2 _n_ marked points in the boundary. Note that this deformation simply amounts to
shifting the kinematics entering the stringy Tr _ϕ_ [3] : _Xo,o_ → _Xo,o_ −1/ _α_ [′] and _Xe,e_ → _Xe,e_ +1/ _α_ [′] .
In the rest of this section, we will explain _why_ (4.1) describes the scaffolded gluons.

At tree-level, we can “cheat” to be assured that we are describing gluons, by showing that

this proposal precisely matches the amplitude for gluons in the open bosonic string, and

we will begin by doing this.

We will then proceed to see why these expressions deserve to be called “gluon ampli
tudes” more intrinsically, by showing that the amplitudes defined in this way satisfy all

the physical properties expected of gluons: on-shell gauge invariance, linearity in polar
izations, as well as consistent factorization on massless gluon poles. These will all follow

from simple but fundamental facts about the _u_ variables summarized in our discussion of

“surfaceology”. This more intrinsic understanding of the amplitudes directly in _u_ variable

language will be crucial in the extension of our proposal to loop-level we undertake in the

next section, where (welcome!) stark differences with string loop amplitudes appear and

we can no longer “cheat” by borrowing the (in)consistency of the bosonic string.


**4.1** **Connection** **to** **the** **bosonic** **string**


At tree-level, gluon amplitudes in the bosonic string are given as a worldsheet integral [28]:




~~[′]~~ _ϵi_ ⋅ _pj_ ⎞

~~(~~ _ij_ ~~)~~ ⎠



d _[n]_ _zi_ ⎛
A [tree] _n_ (1 _,_ 2 _,...,n_ ) = ∫ SL(2,R ~~)~~ ⎝ [∏] _i,j_ ( _ij_ ) [2] _[α]_ [′] _[p][i]_ [⋅] _[p][j]_ [⎞] ⎠ [exp] [⎛] ⎝ [∑] _i_ ≠ _j_ 2 _[ϵ]_ ~~(~~ _[i]_ _ij_ [ ⋅] ~~)~~ _[ϵ]_ [2] _[j]_ [−]



~~√~~



_α_ ~~[′]~~ _ϵi_ ⋅ _pj_



_,_
�����������multi-linear in _ϵi_



(4.2)
where _ϵi_ are the polarizations and _pi_ the respective momentum, and ( _ij_ ) = _zi_ - _zj_ . Since
we are describing the scattering of gluons, in addition to the Koba-Nielsen factor [19], we

also have a part encoding the information about the polarizations of the gluons, which

is compactly represented in the exponential. Since gluon amplitudes are **linear** in each

polarization, we are meant to keep only the term in the expansion of the exponential which

is multilinear in all the polarizations.

This integral representation of the bosonic string amplitudes is fairly compact, however,

it is less interesting for practical purposes such as computing the amplitudes. As it is usually


33


the case for stringy integrals, the integrals in (4.2) do not converge and so if one wants to

evaluate it for some physical kinematics, one has to first resort to analytic continuation to

properly define it (we come back to this in section 4.8.)

In addition, expanding the exponential we can see that to each term proportional to
_ϵi_ ⋅ _ϵj_ we get a factor of ( _ij_ ) [2] in the denominator. The presence of such terms tells us that
the integral has double poles when ( _ij_ ) → 0. Of course, such double poles are not physical
and can be eliminated using integration by parts (IBPs).

Even forgetting about the convergence issues, one key difference between the (4.2) and

the tachyon integral, (2.21), is that in the first, (4.2), we have a sum of different stringy
integrals, each multiplied by a factor of _pi_ ⋅ _ϵj_, _ϵi_ ⋅ _ϵj_, while in the latter, (2.21), there is
a single integral that generates everything. So a natural question is whether there is a

different starting point, that still describes gluons, but in which the amplitude, like in

the scalar case, is represented as single term integral - this can be achieved exactly by

**scaffolding** **the** **gluons** **in** **a** **scalar** **problem** .

To reach the 2 _n_ -scalar problem, define these scalars as the remaining degrees of freedom

after fixing some configuration for the polarizations:

Concretely, we consider the scattering to happen in a sufficiently high-dimensional
space, with _D_ [˜] dimensions, so that we can achieve the following kinematical configuration:



_pi_ ⋅ _ϵj_ = 0 _,_ ∀( _i,j_ ) ∈(1 _,...,_ 2 _n_ ) _,_



_ϵi_ ⋅ _ϵj_ =
⎧⎪⎪⎨⎪⎪⎩



1 if ( _i,j_ ) ∈{(1 _,_ 2); (3 _,_ 4); (5 _,_ 6); _..._ ; (2 _n_ - 1 _,_ 2 _n_ )} _,_



(4.3)



0 otherwise _._



This kinematics can be achieved by demanding that the momentum, _pi_ live in the first
_D_ dimensions of spacetime, and the polarizations live in the extra dimensions, of this big
dimensional, _D_ [˜] spacetime:



∣
_p_ ∣ _[µ]_ _i_
0

0
⋮
0

0



⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟
⎠



0
⋮
0

0
⋮
1
⋮
0



⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟
⎠



_pi_ =



⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜
⎝



_D_


Extra

dims.



; _ϵ_ 2 _j_ /2 _j_ −1 =



⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜
⎝



_D_


← _j_ th



_._ (4.4)



By making this kinematical choice, we fixed all the polarizations, and all the data left

in the problem are the momenta. Therefore we are left only with scalar degrees of freedom,
whose kinematics is described by the Mandelstam invariants, _pi_ ⋅ _pj_ living in _D_ spacetime
dimensions - these are exactly 2 _n_ **scaffolding** **scalars** .

Plugging this kinematical choice in the bosonic string integral (4.2), most of the terms


34


in the exponential vanish, and the big sum collapses into a single term:


2n-scalar d [2] _[n]_ _zi_ 1
A2 _n_ (1 _,_ 2 _,...,_ 2 _n_ ) �����→∫ SL(2,R ~~)~~ _i,j_ ∈(1∏ _,_ 2 _,...,_ 2 _n_ )( _ij_ ) [2] _[α]_ [′] _[p][i]_ [⋅] _[p][j]_ ~~(~~ 12 ~~)~~ [2] ~~(~~ 34 ~~)~~ [2] ~~(~~ 56 ~~)~~ [2] _..._ ~~(~~ 2 _n_ ~~−~~ 1 _,_ 2 _n_ ~~)~~ [2] _[.]_

(4.5)
Recalling the definition of the _u_ variables in terms of ( _ij_ ) (2.22), we can rewrite (4.5)
in terms of _u_ ’s as follows:



d _[n]_ _zi_ /SL(2,R) (23)(45)(67) _..._ (2 _n,_ 1)
A2 _n_ (1 _,_ 2 _,...,_ 2 _n_ )[ _Xi,j_ ] = ∫ ~~(~~ 12 ~~)(~~ 23 ~~)(~~ 34 ~~)~~ _..._ ~~(~~ 2 _n,_ 1 ~~)~~ [∏] _i,j_ _u_ _[α]_ _ij_ [′] _[X][i,j]_ ~~(~~ 12 ~~)(~~ 34 ~~)(~~ 56 ~~)~~ _..._ ~~(~~ 2 _n_ ~~−~~ 1 _,_ 2 _n_ ~~)~~



d _[n]_ _zi_ /SL(2,R)
= ∫ ~~(~~ 12 ~~)(~~ 23 ~~)(~~ 34 ~~)~~ _..._ ~~(~~ 2 _n,_ 1 ~~)~~ [∏] _i,j_ _u_ _[α]_ _ij_ [′] _[X][i,j]_

  - **������������������������������������������������������** **������������������������������������������������������**
Integrand of (2.24)



( [∏][(] _[i,j]_ [)∈][even] _[u][i,j]_




[(] _[i,j]_ [)∈][even] _[i,j]_

) _._
∏( _i,j_ )∈odd _ui,j_



(4.6)

This is exactly the form of equation (4.1)   - the integrand of (2.24), times the extra
multiplicative factor of the ratio of the product of all the _ui,j_ for _i_ and _j_ even and the
product of all the _ui,j_ for _i_ and _j_ odd.
So, from this perspective, we learn that the external scaffolding scalars we are scattering

are secretly **gluons** **in** **higher** **dimensions**, where we are expanding around a kinematic

point where the gluons effectively become colored scalars. Exactly because of the gluon

3 -point interaction, we have that these colored scalars interact with gluons through a

cubic vertex whose Feynman rule is, once again, the expected one in figure 11. Note that,
however, since we picked _ϵi_ ⋅ _ϵj_ = 0, except for ( _i,j_ ) = (2 _k_ - 1 _,_ 2 _k_ ), this cubic interaction
is only present between **adjacent** pairs of scalars, (2 _k_ - 1 _,_ 2 _k_ ). This means that for a
2 _n_ -scalar process we have _n_ -different species, { _A_ 1 _,A_ 2 _,...,An_ }, of these colored scalars
and the scattering process we are describing is (1 _[A]_ [1] _,_ 2 _[A]_ [1] _,_ 3 _[A]_ [2] _,_ 4 _[A]_ [2] _,_ ⋯ _,_ (2 _n_ - 1) _[A][n]_ _,_ (2 _n_ ) _[A][n]_ ).
Such 2 _n_ -scalar bosonic string amplitudes were also studied in [29, 30], where a systematic

IBP algorithm was developed and the field-theory limit produces 2 _n_ -scalar amplitudes of

Yang-Mills-scalar theory [31] naturally given in CHY formulas [32, 33].

Therefore, to extract the gluon amplitude from (4.1) all we need to do is compute
the scaffolding residue: _X_ 2 _k_ −1 _,_ 2 _k_ +1 → 0. In this kinematical locus, each pair of adjacent
scalars, (2 _k_ - 1 _,_ 2 _k_ ), produces an on-shell gluon, uncovering the n-point gluon amplitude.
Of course, the answer will be in terms of the scalar Mandelstam invariants, _Xi,j_, and so to
recover the usual expression for the amplitude in terms of polarizations we can use directly

the dictionary presented in section 3.4.


**4.2** **The** **scaffolding** **residue**


Let us now proceed and see in detail how to extract the scaffolding residue from the 2n
scalar amplitude (4.1). Following the procedure laid out in section 2, each a positive
parametrization, _ui,j_ [ _y_ ], is associated with a triangulation of the disk with 2 _n_ marked
points on the boundary, T . As pointed out before, the final answer is **independent** of
this choice, but it is simpler to access the singularities of a particular diagram by choosing

the parametrization associated with its dual triangulation. Therefore, since we want to


35


**Figure** **16** : Scaffolding triangulation: including all the _X_ 2 _i_ −1 _,_ 2 _i_ +1 propagators.


access the residue _X_ 2 _i_ −1 _,_ 2 _i_ +1 → 0, it is helpful to choose a triangulation that includes the
scaffolding chords - we call such triangulations as **scaffolding** **triangulation** (see figure

16).


**4.2.1** **The** 2 _n_ **-scalar** **form** **in** **the** **scaffolding** **triangulation**


For such a choice of triangulation, the ratio of _ui,j_ in the 2n-scalar form (4.1) reduces to
something very simple. Recall from section 2.6.3, that the product of all the _y_ C can be
written in terms of _u_ ’s as described in eq. (2.20).

Now something especially nice happens in the case of a scaffolding triangulation: by
drawing the curves on the fat graph we can see that all the _Xe,e_ will be such that _PXe,e_ = −1
and _Xo,o_ will be such that _PXo,o_ = +1, while all the remaining will be zero [5] . Therefore, as
long as we are working in the scaffolding triangulation we have:


_[u][i,j]_
∏ _y_ C = ∏ _ys_ ∏ _yi_ = ( [∏][(] _[i,j]_ [)∈][odd] ) _,_ (4.7)
C _s_ _i_ ∏( _i,j_ )∈even _ui,j_

where _ys_ stands for the y’s corresponding to propagators in the scaffolding, _X_ 2 _k_ −1 _,_ 2 _k_ +1,
while _yi_ are those associated with propagators of the internal gluon problem, _Xo,o_ .
Therefore picking a positive parametrization of the stringy integral corresponding to
a scaffolding triangulation, T _s_, (4.6) reduces to:



d _yi_ 1

_yi_ [∏] _i,j_ _u_ _[X]_ _ij_ _[i,j]_ [ _ys,yi_ ] ( ∏ _s ys_ ∏ _i yi_ )



A2 _n_ (1 _,_ 2 _,...,_ 2 _n_ )[ _Xi,j_ ] = ∫



∞



∏
0 _s_

∞

∏
0 _s_



d _ys_

× ∏
_ys_ _i_



d _ys_ ∏

_ys_ [2] _i_



d _ys_



(4.8)
_,_



= ∫



∞



d _yi_



d _yi_

_yi_ [2] ∏ _i,j_ _u_ _[X]_ _ij_ _[i,j]_ [ _ys,yi_ ]




- **������������������������������������������������** **�����������������������������������������������** ��
Ω2 _n_



5Note that this is **independent** of the internal details of the triangulation, and so it is true for any

surface, which means it holds both tree-level as well as loop-level


36


where we have set _α_ [′] = 1. Note that this is exactly the scalar integral (2.24), but where
instead of having a dlog( _y_ ) = d _y_ / _y_ form, we have d _y_ / _y_ [2] . We call this non-dlog form that
we are integrating the 2n-scalar form, Ω2 _n_ .


**4.2.2** **Extracting** **the** **residue**


Since we have picked the scaffolding chords to be part of the triangulation, we can factor out of the Koba-Nielsen factor a piece that looks like the ∏ _s ys_ _[X][s]_ [,] [with] _[X][s]_ [denoting]
the scaffolding chords, _X_ 2 _k_ −1 _,_ 2 _k_ +1. Therefore the integral over the scaffolding _ys_ reduces
schematically to:



∏
0 _s_



d _ys_



d _ys_

_ys_ _[X][s]_ × F [ _ys,yi,Xi,j_ ] _,_ (4.9)
_ys_ [2]



∫



∞



where F represents some function of the remaining variables which is regular and non-zero
when the _ys_ and _Xs_ go to zero.
Looking at the integral we can see that if we set one of the scaffolding variables _Xsi_
to zero, then the integral over _ysi_ is divergent for _ysi_ near 0. Therefore, for _Xsi_ → 0, the
integral is dominated by the region _ysi_ near 0. Focusing on this region, we can rewrite F
using the appropriate Taylor expansion:



_yys_ [2] _sii_ _ysXi_ _si_ ⎛⎝ [F [] _[y][s][i]_ [=][ 0] _[,y][s][,y][i][,X][i,j]_ [] +] _[ y][s][i]_ dF [ _ys_ d _,yysii,Xi,j_ ]



_s,yi,Xi,j_ ]

∣ + _..._ [⎞]
d _ysi_ _ysi_ =0 ⎠ _[,]_



_ϵ_ d _ysi_

0 _y_ [2]



_ϵ_



∏
0 _s_ ≠ _si_



d _ys_



d _ys_

_ys_ _[X][s]_ × ∫
_ys_ [2]



∫



∞



(4.10)
where the integration in _ysi_ is from 0 to _ϵ_, and _ϵ_ is some number arbitrarily close to zero,
but non-zero.

One can now perform the integral, term by term in the expansion, using analytic

continuation:



_y_ _[ϵ][A]_

_y_ _[y][A]_ [ =] _A_



_ϵ_ d _y_


0 _y_



(4.11)
_A_ _[,]_



∫



_ϵ_



which gives:




_[s][,y][i][,X][i,j]_ []]

∣ + _..._ [⎞]
d _ysi_ _ysi_ =0 ⎠ _[.]_



_ϵ_ _[X][si]_ [1] [=][ 0] _[,y][s][,y][i][,X][i,j]_ [] +] _[ϵ][X][si]_

_Xsi_ ~~−~~ 1 [F [] _[y][s][i]_ _Xsi_




_[X][si]_ ⋅ [d][F [] _[y][s][,y][i][,X][i,j]_ []]

_Xsi_ d _ysi_



∏
0 _s_ ≠ _si_



d _ys_ _ϵ_ _[X][si]_ [−][1]

_ys_ _[X][s]_ × [⎛]
_ys_ [2] ⎝ _Xsi_ ~~−~~



d _ys_



∫



∞



(4.12)
From here we can read off directly the residue on _Xsi_ = 0 to be



∏
0 _s_ ≠ _si_



_s,yi,Xi,j_ ∣

d _ysi_ _ysi_ =0



Res _Xsi_ =0(A2 _n_ (1 _,_ 2 _,...,_ 2 _n_ )) = ∫



∞



⎞
⎠



∏
0 _i_



d _yi_



_i_ ∫

_yi_ [2]



d _ys_ dF [ _ys,yi,Xi,j_ ]

_ys_ _[X][s]_ × [⎛]
_ys_ [2] ⎝ d _ysi_



d _ys_



∞



= ∫



∞



Res _ysi_ =0 (Ω2 _n_ ) _._
0



(4.13)
Repeating this procedure for all the scaffolding variables _ys_, we obtain:



0 Res _ys_ 1 =0 (Res _ys_ 2 =0 ( _..._ (Res _ysn_ =0Ω2 _n_ ) _..._ )) _,_ (4.14)



A [gluon] _n_ = ∫



∞



and we conclude that this consecutive residue is simply given by the part of F [ _ys,yi,Xi,j_ ]
which is **linear** **in** **all** **the** **scaffolding** _y_ ’s, { _ys_ 1 _,_ ... _,ysn_ }.


37


**4.3** **Scaffolding** **residue** ⇒ **Gauge** **invariant** **and** **multi-linear** **amplitude**



Let’s now understand how the scaffolding residue of the 2n-scalar amplitude, automatically

gives something of the form of (3.17), _i.e._ an object which is automatically gauge-invariant

and multilinear in the corresponding polarizations. Without loss of generality, let us focus

on what happens after taking the residue corresponding to putting gluon 1 on-shell, _i.e._
_X_ 1 _,_ 3 → 0, which is given by the residue of Ω2 _n_ at _y_ 1 _,_ 3 = 0:



_._
������������ _y_ 1 _,_ 3=0



d _yi_ ∑

_yi_ [2] ( _IJ_ )



⎛ _∂_ log( _uIJ_ )
⎝ _[X][I,J]_ _∂y_ 1 _,_ 3



( _uIJ_ )

_∂y_ 1 _,_ 3 (∏ _km_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ] [⎞] ⎠



Res _y_ 1 _,_ 3=0Ω2 _n_ (1 _,_ 2 _,...,_ 2 _n_ )[ _Xi,j_ ] = ∏
_s_ ≠(1 _,_ 3)



d _ys_ ∏

_ys_ [2] _i_



(4.15)
However, not all the _ui,j_ depend on _y_ 1 _,_ 3. In fact, only the _u_ ’s corresponding to curves
that go through road 13, can depend on _y_ 1 _,_ 3. Therefore the only curves for which this
derivative is non-zero are curves _X_ 1 _,j_ and _X_ 2 _,j_ (see figure 17):



_._
������������ _y_ 1 _,_ 3=0



d _yi_ ∑

_yi_ [2] _J_



⎛ _∂_ log( _u_ 1 _J_ )
⎝ _[X]_ [1] _[,J]_ _∂y_ 1 _,_ 3 (∏ _km_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ]



Res _y_ 1 _,_ 3=0Ω2 _n_ [ _Xi,j_ ] = ∏
_s_ ≠(1 _,_ 3)



d _ys_ ∏

_ys_ [2] _i_



( _u_ 2 _J_ )

_∂y_ 1 _,_ 3 (∏ _km_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ] [⎞] ⎠



_∂_ log( _u_ 2 _J_ )
+ _X_ 2 _,J_



(4.16)
Now we claim that _∂y_ 1 _,_ 3 log( _u_ 1 _J_ ) = − _∂y_ 1 _,_ 3 log( _u_ 2 _J_ ). This follows immediately from one
of the fundamental facts about the _u_ variables we summarized in our surfaceology review.

We can consider the smaller surface obtained simply by cutting just before the forking into
(1 _,_ 2). Let’s consider the curve [1 _J_ ] on the smaller surface that starts on the road (13) and
exits at _J_ ; we use square brackets to remind us this is a curve on the smaller surface. This
manifestly does not depend on _y_ 1 _,_ 3 which is a boundary in the smaller surface. This curve
can be extended to a curve on the full surface in two ways, into (1 _J_ ) and (2 _J_ ). So we have
that _U_ [1 _,J_ ] = _u_ 1 _,J_ _u_ 2 _,J_ is independent of _y_ 1 _,_ 3 and hence _∂y_ 1 _,_ 3 _u_ 1 _,J_ = − _∂y_ 1 _,_ 3 _u_ 2 _,J_ as desired. We
can also see this very simply directly, from the matrix formula for the _u_ variables. Let’s
consider the words corresponding to curves _X_ 2 _,J_ and _X_ 1 _,J_ . From figure 17, we see that
these curves agree everywhere except for the last intersection, at the end of road 13. So

we can write their _u_ -variables as follows:




_[B]_ _[y]_ [1] _[,]_ [3] _[Ay]_ [1] _[,]_ [3][ +] _[ B]_
1 _J_ ∶ _M_ remaining × _ML_ ( _y_ 1 _,_ 3) = [ _[A]_
_C_ _D_ [] × [] _[y]_ [1] 0 _[,]_ [3] 1 [] = [] _C y_ _[Ay]_ [1] 1 _[,]_ _,_ [3] 3 _C y_ 1 _,_ 3 + _D_ []]



⇒ _u_ 1 _J_ = _[C]_ [ (] _[Ay]_ [1] _[,]_ [3][ +] _[ B]_ [)]



_A_ ~~(~~ _C y_ 1 _,_ 3 ~~+~~ _D_ ~~)~~ _[,]_




_[B]_ [0] _[B]_
2 _J_ ∶ _M_ remaining × _MR_ ( _y_ 1 _,_ 3) = [ _[A]_
_C_ _D_ [] × [] _[y]_ [1] 1 _[,]_ [3] 1 [] = [] _C y_ _[Ay]_ 1 [1] _,_ _[,]_ 3 [3] + [ +] _D_ _[ B]_ _D_ []]



(4.17)



⇒ _u_ 2 _J_ = _[B]_ [ (] _[C y]_ [1] _[,]_ [3][ +] _[ D]_ [)]



_D_ ~~(~~ _Ay_ 1 _,_ 3 ~~+~~ _B_ ~~)~~ _[,]_



where _A,B,C_ and _D_ are functions of the remaining _y_ ’s. Even without knowing the details
of the rest of the curves, we can check that the product _u_ 1 _,J_ _u_ 2 _,J_ does **not** depend on _y_ 1 _,_ 3.


38


**Figure** **17** : Curves _X_ 1 _,J_ and _X_ 2 _,J_ .


**Figure** **18** : Triangulation containing { _X_ 2 _i,_ 2 _i_ +2}.


Thus we have dlog _u_ 1 _J_ = − dlog _u_ 2 _J_ . This relation allows us to write the residue as:




_[u]_ [2] _[J]_

_∂y_ 1 _,_ 3 ( _km_ ∏)≠(2 _J_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ]



_,_



Res _y_ 1 _,_ 3=0Ω2 _n_ [ _Xi,j_ ] = ∑ ( _X_ 2 _,J_ - _X_ 1 _,J_ ) ∏
_J_ _s_ ≠(1 _,_ 3)



d _ys_



d _ys_ ∏

_ys_ [2] _i_



d _yi_

× _[∂]_ [log][(] _[u]_ [2] _[J]_ [)]
_yi_ [2] _∂y_ 1 _,_ 3



d _yi_




- **�������������������������������������������������������������������������������������** **�������������������������������������������������������������������������������������** Q2 _,J_



(4.18)

which is exactly of the form required by gauge-invariance and multi-linearity (3.6). Here
the product over ( _km_ ) excludes (2 _J_ ) since _u_ 2 _J_ ∣ _y_ 1 _,_ 3=0 = 1. From (3.6), we should also be
able to express this residue as a sum of terms proportional to ( _X_ 2 _,J_ - _X_ 3 _,J_ ). This is not
as obvious and, to prove that this is the case, it is useful to triangulate the surface in a
different way - using a triangulation containing _X_ 2 _i,_ 2 _i_ +2, with _i_ ∈{1 _,..,n_ } (see figure 18).
In this case, the _u_ ’s are functions of different _y_ ’s, that we denote by _y_ ˜. In this
parametrization, the residue corresponding to the original scaffolding residue, _i.e._ _X_ 1 _,_ 3 =
_X_ 3 _,_ 5 = _..._ = _X_ 1 _,_ 2 _n_ −1 = 0, is obtained by taking the residue of Ω2 _n_ at _y_ 2 _i,_ 2 _i_ +2 →∞. Now in this
new triangulation, by exactly the same argument presented for the original triangulation,


39


_∂y_ ˜ [(] 2 _[u]_ _,_ 4 [3] _[J]_ [)] = − _[∂]_ [log] _∂y_ ˜ [(] 2 _[u]_ _,_ 4 [2] _[J]_ [)]



we have that _[∂]_ [log][(] _[u]_ [3] _[J]_ [)]




[2] _[J]_, therefore we also have:

_∂y_ ˜2 _,_ 4




_[u]_ [2] _[J]_

_∂y_ ˜2 _,_ 4 ( _km_ ∏)≠(3 _J_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ˜]



_._



Res _y_ ˜2 _,_ 4=∞Ω2 _n_ [ _Xi,j_ ] = ∑ ( _X_ 2 _,J_ - _X_ 3 _,J_ ) ∏
_J_ _s_ ≠(2 _,_ 4)



d˜ _ys_



d˜ _ys_ ∏

_y_ ˜ _s_ [2] _i_



d˜ _yi_

× _[∂]_ [log][(] _[u]_ [2] _[J]_ [)]
_y_ ˜ _i_ [2] _∂y_ ˜2 _,_ 4



d˜ _yi_




- **�������������������������������������������������������������������������������������** **�������������������������������������������������������������������������������������** Q˜2 _,J_



(4.19)

Repeating the same argument, one can show that such a form holds for any triple of
indices (2 _i_ - 1 _,_ 2 _i,_ 2 _i_ + 1), and thus for each gluon in the problem. Just in the same way as
before, (after taking the remaining scaffolding residues) we have ∫ _Q_ [˜] 2 _,J_ = ∫ _Q_ 2 _,J_ = _∂X_ 2 _,J_ A _n_ .
Hence, we have proved that taking the scaffolding residue automatically gives us something

that is manifestly **gauge** **invariant** as well as **multi-linear** in all polarizations.


**4.4** **Tree-level** **factorization**


Our goal now is to understand what factorization looks like in this scalar language. As we

know, for the usual way we write the amplitudes directly in terms of the polarizations of
the gluons, when we extract the residue of the amplitude on a pole, _Xa,b_ = 0, we obtain
the gluing of the two lower point amplitudes, A _L_ and A _R_ :

Aglued = A _[µ]_ _L_ [(−] _[η][µ,ν]_ [ +] _[p][µ][q][ν]_ [ +] _[ p][ν][q][µ]_ )A _[ν]_ _R_ [= −A] _L_ _[µ]_ _[η][µ,ν]_ [A] _R_ _[ν]_ _[,]_ (4.20)

_p_ ~~⋅~~ _q_


where the term between brackets is doing the polarization sum for the intermediate gluon,
_I,I_ [′] we are producing. We define

A _[µ]_ _L_ [=] _[ ∂][ϵ][I,µ]_ [A] _[L]_ _,_ A _[ν]_ _R_ [=] _[ ∂][ϵ]_ _I_ [′] _,ν_ [A] _[R][,]_ (4.21)

and _pµ_ = _pI,µ_ = − _pI_ ′ _,µ_ and _q_ _[µ]_ is some reference vector for which _q_ ⋅ _p_ ≠ 0. Note that the final
answer does not depend on the arbitrary choice of _q_ _[µ]_ . In the second equality, we use the
fact that _ML_ _[µ]_ _[p][I,µ]_ [ =] _[ M]_ _R_ _[ν]_ _[p][I]_ [′] _[,ν]_ [=][ 0,] [as] [required] [by] [gauge] [invariance.]
We now want to phrase this rule for summing over polarizations (“gluing” rule) in terms
of the scalar variables of the scaffolded problem. To do so, we think of gluons, _I_ and _I_ [′] as

being scaffolded by a pair of scalars, such that in the momentum polygon this interaction
is associated with a triangle whose vertices are ( _a,b,x_ ) and ( _a,b,x_ [′] ), respectively (see
figure 19 ). Therefore, the polarizations of _I_ and _I_ [′] are, respectively, encoded in the
scalar variables, _Xx_ _[µ]_ [,] [and] _[X]_ _x_ _[ν]_ [′][.] [Now] [using] [our] [scalar] [definition] [of] [gauge-invariance] [and]
multi-linearity of A _L_ and A _L_ in gluons, _I_ and _I_ [′], respectively, we have:



⎞
⎠ _[,]_



A _[µ]_ _L_ [=] _[ ∂][X]_ _x_ _[µ]_ [A] _[L]_ [ =] _∂_
_∂Xx_ _[µ]_



⎛ ⎞
( _Xx,j_   - _Xb,j_ )Q _x,j_ ( _Xx_ _[µ]_ [−] _[X]_ _j_ _[µ]_ [)] _[∂]_ [A] _[L]_
⎝ [∑] _j_ ⎠ [=][ 2] [⎛] ⎝ [∑] _j_ _∂Xx,j_



_∂_
A _[ν]_ _R_ [=] _[ ∂][X]_ _x_ _[ν]_ [′] [A] _[R]_ [ =] _∂Xx_ _[ν]_ [′] (∑ _J_ ( _Xx_ ′ _,J_ - _Xa,J_ )Q _x_ ′ _,J_ ) = 2 (∑ _J_ ( _Xx_ _[ν]_ [′][ −] _[X]_ _J_ _[ν]_ [)] _∂X_ _[∂]_ [A] _x_ _[R]_ ′ _,J_ ) _._



(4.22)



Therefore contracting with the flat metric, we obtain:

Aglued = −4 ∑( _Xx_ _[µ]_ [−] _[X]_ _j_ _[µ]_ [)(] _[X][x]_ [′] _[,µ]_ [ −] _[X][J,µ]_ [)] _[∂]_ [A] _[L]_
_j,J_ _∂Xx,j_


40



_∂_ A _R_
_,_ (4.23)
_∂Xx_ ′ _,J_


**Figure** **19** : Tree-level factorization.


using a gauge transformation and a rescaling, we can choose _Xx_ _[µ]_ [=] _[ X]_ _b_ _[µ]_ [and] _[ X]_ _x_ _[ν]_ [′] [=] _[ X]_ _a_ _[ν]_ [which]
yields:
Aglued ∝∑( _Xb_ _[µ]_ [−] _[X]_ _j_ _[µ]_ [)(] _[X][a,µ]_ [ −] _[X][J,µ]_ [)] _[∂][X]_ _x,j_ [A] _[L][∂][X]_ _x_ [′] _,J_ [A] _[R]_
_j,J_

(4.24)
∝∑(− _Xb,J_        - _Xa,j_ + _Xj,J_ ) _∂Xx,j_ A _L∂Xx_ ′ _,J_ A _R._
_j,J_


To check factorization we want to extract the massless residues and interpret the

result in terms of lower point gluon amplitudes. Let’s study the residue corresponding to
having _Xa,b_ on-shell, so _Xa,b_ = 0. Choosing an appropriate scaffolding triangulation that
contains _Xa,b_, this residue is given by the coefficient multiplying _ya,b_ in the expansion of
∏ _u_ _[X]_ _X_ [.] [Similarly] [to] [what] [was] [argued] [in] [4.3][,] [the] [only] _[ u]_ [’s] [that] [depend] [on] _[y][a,b]_ [are] [those] [that]
correspond to curves that intersect _Xa,b_ as laminations, i.e. all the curves that go through
road _ab_ in the fat graph. There are three types of such curves: _Xj,J_, _Xa,J_ and _Xj,b_, with
_j_ ∈{ _a_ + 1 _,...,b_ - 1} and _J_ ∈{ _b_ + 1 _,...,a_ - 1}. So expanding the Koba-Nielsen factor up to
linear order in _ya,b_ yields:



_∂_ log( _uj,J_ )
∏ _u_ _[X]_ _X_ [=][ 1][ +] _[ y][a,b]_ ∑ _Xj,J_
_X_ _j,J_ _∂ya,b_
⎡⎢⎢⎢⎢⎣



( _uj,J_ ) _∂_ log( _uj,b_ )

+ ∑ _Xj,b_
_∂ya,b_ _j_ _∂ya,b_



( _uj,b_ ) _∂_ log( _ua,J_ )

+ ∑ _Xa,J_
_∂ya,b_ _J_ _∂ya,b_



⎤⎥⎥⎥⎥⎦



������������ _ya,b_ =0



_∂ya,b_



+ O( _ya,b_ [2] [)] _[.]_
(4.25)

Now we note that any triangulation containing road _ab_ will look schematically like

figure 20, and therefore, similarly to what we proved in 4.3, we have:

∏ _uj,J_ × _ua,J_ ≡U _ab,J_ [right] _[,]_ (4.26)
_j_

∏ _uj,J_ × _uj,b_ ≡U _j,ab_ [left] _[,]_ (4.27)
_J_

where U _ab,J_ [right] [and][ U] _j,ab_ [left] [are the] _[ u]_ [’s of the smaller surfaces on the right/left of] _[ ab]_ [ respectively,]


41


**Figure** **20** : Fat graph around road _ab_ .


and thus **do** **not** **depend** on _ya,b_ . Therefore we have:



_∂_ log( _ua,J_ )



_,_
_∂ya,b_



_ua,J_ = −∑

_∂ya,b_ _j_

( _uj,b_ ) = −∑

_∂ya,b_ _j_



_∂_ log( _uj,J_ )



_∂_ log( _uj,b_ )



_∂_ log( _uj,J_ )



(4.28)

( _uj,J_ )

_._
_∂ya,b_



Plugging these relations into (4.25), we get:

∏ _u_ _[X]_ _X_ [=][ 1][ +] _[ y][a,b]_ [∑] ( _Xj,J_  - _Xj,b_  - _Xa,J_ ) _[∂]_ [log][(] _[u][j,J]_ [)] ∣ + O( _ya,b_ [2] [)] _[.]_ (4.29)
_X_ _j,J_ _∂ya,b_ _ya,b_ =0


Finally, we can get _[∂]_ [log] _∂y_ [(] _a,b_ _[u][j,J]_ [)] ∣ using the _u_ -equations:

_ya,b_ =0

_uj,J_ + _ua,b_ ∏ _uXL_ ∏ _uXR_ ∏ _uX_ = 1 _,_ (4.30)
_XL_ ∈ _Lj_ _XR_ ∈ _RJ_ _X_ ∈I



where _RJ_ and _Lj_ stand for the set of curves that intersects _Xj,J_ but that live on the
right/left on _Xa,b_, respectively, and so do **not** intersect _Xa,b_ ; I stands for the set of curves
that are simultaneously incompatible with _Xa,b_ and _Xj,J_ . Since _ua,b_ = 0, when _ya,b_ = 0, we
have:
_∂_ log( _uj,J_ )

_[∂u][a,b]_



_uj,J_ ∣ = − _[∂u][a,b]_

_∂ya,b_ _ya,b_ =0 _∂ya,b_




_[∂u]_ _∂ya,b_ _[a,b]_ ∣ _ya,b_ =0 _X_ ∏ _L_ ∈ _Lj_ _u_ ˜ _XL_ _XR_ ∏∈ _RJ_ _u_ ˜ _XR,_ (4.31)



where _u_ ˜ _X_ = _uX_ ∣ _ya,b_ =0, are the _u_ ’s of the smaller right and left surfaces, obtained when cut
through curve _Xa,b_ . In addition, we don’t have any _uX_ for _X_ ∈I since these all go to 1
when _ua,b_ → 0.


42


We now need to compute _∂ya,bua,b_ ∣ _ya,b_ =0. It is easy to see that this expression nicely
factorizes in precisely the way needed to ensure factorization of the amplitude. Since ( _a,b_ )
is road present in our triangulation, the word for ( _a,b_ ) is a “ _V_ ”, with a series of right turns
ending on ( _a,b_ ) then a series of left turns thereafter, of the form _αRa_ 1⋯ _alRya,bLb_ 1 _L_ ⋯ _brLβ_
where _α,β_ are boundaries and the _a_ ’s and _b_ ’s denote the roads on the left and right of
( _a,b_ ). Then from the matrix product formula for _ua,b_ it is very easy to see that

_ua,b_ = _ya,bFLFR_ + _O_ ( _ya,b_ [2] [)] _[,]_ (4.32)


where

_FL_ = (1 + _al_ + _alal_ −1 + ⋯+ _alal_ −1⋯ _a_ 1) _, FR_ = (1 + _br_ + _brbr_ −1 + ⋯+ _brbr_ −1⋯ _b_ 1) _._ (4.33)

So we have that _∂ya,bua,b_ ∣ _ya,b_ =0 = _FLFR_ nicely factorizes. But each of these factors
_FL,FR_ is also directly interpreted as the coefficient of the leading term in _ya,b_ for ( _a,b_ )
curve on each of the obvious smaller _L,R_ surfaces. The reason is simply that on each of
the _L,R_ surfaces, the ( _a,b_ ) _[L,R]_ curves is still a road in the triangulation, the word is still a
_V_, but e.g. on the L surface, the word for ( _a,b_ ) _[L]_ immediately runs into a boundary after
turning left on ( _a,b_ ), similarly for ( _a,b_ ) _[R]_ . Thus _∂ya,bu_ _[L]_ _a,b_ [∣] _[y]_ _a,b_ [=][0] [=] _[F][L][,∂][y]_ _a,b_ _[u][R]_ _a,b_ [∣] _[y]_ _a,b_ [=][0] [=] _[F][R]_ [.]
Thus we have that
_∂ua,b_ _∂u_ _[L]_ _a,b_ _∂u_ _[R]_ _a,b_
∣ _ya,b_ =0 = ∣ _ya,b_ =0 × ∣ _ya,b_ =0 _._ (4.34)
_∂ya,b_ _∂ya,b_ _∂ya,b_

So then we have that the residue of the amplitude at _Xa,b_ = 0 is:



_∂u_ _[L]_ _a,b_
Res _Xa,b_ =0 A _n_ = −∑( _Xj,J_ - _Xj,b_ - _Xa,J_ ) ∣ _ya,b_ =0 ∏ _u_ ˜ _XL_
_j,J_ _∂ya,b_ _XL_ ∈L _j_

                 - **�������������������������������** �� **��������������������������������**                  _Q_ _[L]_ _j_



_∂u_ _[R]_ _a,b_
⋅ ∣ _ya,b_ =0 ∏ _u_ ˜ _XR_
_∂ya,b_ _XR_ ∈R _J_

 - **���������������������������������** - **����������������������������������**
_Q_ _[R]_ _J_



_._



(4.35)
But _Q_ _[L]_ _j_ [and] _[Q][R]_ _J_ [are] [precisely] [the] [objects] [that] [show] [up] [in] [the] [lower-point] [ampli-]
tudes when we take the scaffolding residue on _ya,b_ ! Consider two lower-point amplitudes:
A _L_ ( _a,a_ +1 _,...,b_ −1 _,b,x_ ) and A _R_ ( _b,b_ +1 _,...,a_ −1 _,a,x_ [′] ). As we saw in our discussion of gauge
invariance and multilinearity above, when we take the scaffolding residue as _Xa,b_ → 0 we
have A _L_ = ∑ _j_ ( _Xx,j_ - _Xb,j_ ) _∂ya,bux,j_ ∣ _ya,b_ =0 and similarly for A _R_ . But by precisely the same
steps above, by looking at the _u_ equation for _ux,j_ / _ux_ ′ _,J_ and differentiating with respect to
_ya,b_, we find that

Res _Xa,b_ =0 A _L_ ( _a,...,b,x_ ) =∑( _Xx,j_          - _Xb,j_ ) _Q_ _[L]_ _x,j_ _[,]_
_j_

(4.36)
Res _Xa,b_ =0 A _R_ ( _b,...,a,x_ [′] ) =∑( _Xx_ ′ _,J_         - _Xa,J_ ) _Q_ _[R]_ _x_ [′] _,J_ _[,]_
_J_

where the _Q_ _[L]_ _x,j_ _[,Q][R]_ _x_ [′] _,J_ [are] [precisely] [the] [factors] [that] [appeared] [in] [the] [residue] [of] [the] [full]
amplitude on the _Xa,b_ → 0 pole above, _i.e._ _Q_ _[L]_ _x,j_ [≡] _[Q]_ _j_ _[L]_ [and] _[Q][R]_ _x_ [′] _,J_ [≡] _[Q]_ _J_ _[R]_ [.] [Since] _[Q][L]_ _j_ [=] _[ ∂][X]_ _x,j_ [A] _[L]_
and similarly for _Q_ _[R]_ _J_ [,] [we] [finally] [have] [that]

Res _Xa,b_ =0 A _n_ = −∑( _Xj,J_        - _Xj,b_        - _Xa,J_ ) _∂Xx,j_ A _L∂Xx_ ′ _,J_ A _R,_ (4.37)
_j,J_

which is precisely the statement of factorization on the _Xa,b_ → 0 pole.


43


**4.5** **Computing** **scaffolding** **residues** **for** **general** _n_


In this section, we present explicit formulas for scaffolding residues for all _n_ . We will

see that the result becomes exactly the _n_ -gluon bosonic string amplitude written in our

new scalar language, whose integrand is a sum of products of surprisingly simple building

blocks we call _V_ ’s and _W_ ’s, corresponding to first- and second-derivatives with respect to

the scaffolding _y_ ’s. We will also see that the _V_ ’s and _W_ ’s can be expressed purely in terms

of products of _u_ variables of the inner _n_ -gon problem in a nice graphical way. Our purpose

here is to show how the bosonic string gluons amplitude naturally falls out of taking the

scaffolding residue in the world of _u_ and _y_ variables; in an appendix A we show how to see

this directly in terms of the conventional worldsheet _z_ variables.

Of course, the consistent factorization of the scaffolded bosonic string amplitude at

tree-level guarantees that taking the scaffolding residue will correctly land on the gluon

amplitude, but we are performing this computation here for two reasons. First, in order to

illustrate how the residues can be taken and subsequently interpreted directly in terms of

integrands involving the _u_ variables on the smaller _n_ -gon surface. We expect this exercise

will be useful for higher loops, where our picture for gluon amplitudes differs significantly

(and is much simpler) than the string amplitude. Second, the final expressions written in

terms of _X_ and _u_ variables have a very pretty direct combinatorial characterization, which

is not manifested in the conventional bosonic string gluon amplitudes written in terms of

polarization vectors and momenta.
We begin by considering a scaffolding triangulation, denoting by _yk_ ≡ _y_ 2 _k_ −1 _,_ 2 _k_ +1 for
_k_ ≤ _n_ to represent the _y_ ’s associated with the “outer” scaffolding propagators _X_ 2 _k_ −1 _,_ 2 _k_ +1,
and _yi_ with _n_ < _i_ ≤ 2 _n_ −3 for the ones corresponding to the “inner” propagators of the gluon
problem. For example, for _n_ = 4, we have denoted _y_ 1 = _y_ 1 _,_ 3 _,y_ 2 = _y_ 3 _,_ 5 _,y_ 3 = _y_ 5 _,_ 7 _,y_ 4 = _y_ 1 _,_ 7 and
_y_ 5 = _y_ 1 _,_ 5 or _y_ 5 = _y_ 3 _,_ 7.
As we’ve discussed already taking the scaffolding residue amounts to extracting the
coefficient of _y_ 1⋯ _yn_ of the factor ∏ _u_ _[α]_ [′] _[X]_, which is a function of _yn_ +1 _,_ ⋯ _,y_ 2 _n_ −3 and the _X_
variables in the exponents. As we have seen in sec. 4.3, only _u_ 1 _,j_ and _u_ 2 _,j_ depend on _y_ 1 since
these are the only two chords that pass the road 13; they differ only by taking different
turns after hitting (13) and the product _u_ 1 _,ju_ 2 _,j_ is independent of _y_ 1. Thus, the derivative
with respect to _y_ 1 brings down a factor


_V_ 1 ∶= _α_ [′] ∑( _X_ 2 _,j_           - _X_ 1 _,j_ ) _[∂u]_ [2] _[,j]_ ∣ _,_ (4.38)
_j_ _∂y_ 1 _y_ 1=0

where the sum is over _j_ = 1 _,_ ⋯ _,_ 2 _n_, but the terms with _j_ = 1 _,_ 2 _,_ 3 vanish ( _X_ 1 _,_ 3 = 0), and
we have used the fact that _u_ 2 _,j_ = 1 on the support of _y_ 1 = 0 and so we omit it in the
denominator.
Similarly only _u_ 2 _a_ −1 _,j_, _u_ 2 _a,j_ depend on _ya_ and their product is independent of it, thus
we define for _a_ = 1 _,_ 2 _,_ ⋯ _,n_


_Va_ ∶= _α_ [′] ∑( _X_ 2 _a,j_            - _X_ 2 _a_ −1 _,j_ ) _[∂u]_ [2] _[a,j]_ ∣ _,_ (4.39)
_j_ _∂ya_ _ya_ =0


44


and the simplest term of the residue contains the product of _n_ such factors _V_ 1 _V_ 2⋯ _Vn_, which
is at order _α_ [′] _[n]_ .
More complicated terms appear when the derivative with respect to _yb_ hits on _Va_ from
previous steps. However, the higher-than-second-order derivative with respect to _y_ 1 _,_ ⋯ _,yn_
of any _u_ variable must vanish, since any chord has exactly one entrance and exit. Moreover,
exactly four _u_ variables, namely _u_ 2 _a_ −1 _,_ 2 _b_ −1, _u_ 2 _a_ −1 _,_ 2 _b_, _u_ 2 _a,_ 2 _b_ −1 and _u_ 2 _a,_ 2 _b_ have non-vanishing
second derivatives with respect to _ya,yb_ . Thus, in the summation over _j_ of _∂Va_ / _∂yb_, only
two terms with _j_ = 2 _b_ and _j_ = 2 _b_ - 1 are non-vanishing:




_[∂V][a]_

∣ = ( _X_ 2 _a,_ 2 _b_    - _X_ 2 _a_ −1 _,_ 2 _b_ ) _[∂]_ [2] _[u]_ [2] _[a,]_ [2] _[b]_
_∂yb_ _yb_ =0 _∂ya∂yb_




_[∂V][a]_
_α_ [′]




[2] _[u]_ [2] _[a,]_ [2] _[b]_

+ _α_ [′] ( _X_ 2 _a,_ 2 _b_ −1 − _X_ 2 _a_ −1 _,_ 2 _b_ −1) _[∂]_ [2] _[u]_ [2] _[a,]_ [2] _[b]_ [−][1]
_∂ya∂yb_ _∂ya∂yb_



_,_ (4.40)
_∂ya∂yb_



where we have suppressed the conditions _ya_ = _yb_ = 0. Note that similarly for _∂Vb_ / _∂ya_ we
have only two terms with _j_ = 2 _a_ and 2 _a_ - 1 non-vanishing. An explicit computation shows
that these two derivatives are very nicely equal to each other, so we can write the result in

a more symmetric way and define



_∂_ [2] _u_ 2 _a,_ 2 _b_
_Wa,b_ ∶= _α_ [′] _c_ 2 _a_ −1 _,_ 2 _b_ −1



_u_ 2 _a,_ 2 _b_

∣ _,_ (4.41)
_∂ya∂yb_ _ya_ = _yb_ =0



where we have used _X_ 2 _a,_ 2 _b_ + _X_ 2 _a_ −1 _,_ 2 _b_ −1 − _X_ 2 _a_ −1 _,_ 2 _b_ - _X_ 2 _a,_ 2 _b_ −1 = _c_ 2 _a_ −1 _,_ 2 _b_ −1. Putting everything
together, we have a pretty formula for the scaffolding residue



_r_
∏ _Wia,ja_
_a_



_n_ −2 _r_ ⎞
∏ _Vkb_ _u_ _[α]_ _i,j_ [′] _[X][i,j]_ _,_ (4.42)
_b_ ⎠ ( [∏] _ij_ )



⎛⌊ _n_ /2⌋+1

∑ ∑

⎝ _r_ =0 { _i,j_ } _,_ { _k_ }



⎛
⎝



∫



2 _n_ −3
∏
_a_ = _n_ +1



_dya_

_ya_ [2]



where we have the _dy_ / _y_ [2] form for the remaining _n_ −3 variables within the _n_ -gon, and the _n_ point Koba-Nielsen factor ∏ _u_ _[X]_ ; inside the bracket, we have a summation over all partitions
of {1 _,_ 2 _,_ ⋯ _,n_ } into _r_ pairs { _ia,ja_ } and _n_ - 2 _r_ singlets _kb_, each given by the product of _W_ ’s
and _V_ ’s. For example, the _n_ = 3 case reads _V_ 1 _V_ 2 _V_ 3 + _W_ 1 _,_ 2 _V_ 3 + _W_ 2 _,_ 3 _V_ 1 + _W_ 1 _,_ 3 _V_ 2, and for _n_ = 4
we have
_V_ 1 _V_ 2 _V_ 3 _V_ 4 + ( _W_ 1 _,_ 2 _V_ 3 _V_ 4 + perm _._ ) + ( _W_ 1 _,_ 2 _W_ 3 _,_ 4 + perm _._ ) _,_ (4.43)

with 6 terms of the form _WV V_ and 3 terms of the form _WW_ . Note that in the _α_ [′] → 0 limit,
only some of these terms contribute to the lowest-order, or the pure Yang-Mills amplitude.
For example, for _n_ = 3 only _V W_ terms contribute and for _n_ = 4 only _WW_ and _WV V_ terms
contribute, while _V_ _[n]_ terms only contribute to amplitude with pure higher-dimensional
operators such as _F_ [3] and _F_ [4] .

We remark that we can already learn many interesting facts about bosonic string

gluon amplitudes and their field-theory limit (Yang-Mills plus higher-dimensional operators
starting with _F_ [3] ) from these expressions. For example, if we are interested in helicity
amplitudes in _D_ = 4, there is a prescription to directly translate _V_ and _W_ into spinorhelicity expressions, which lead to formulas for _n_ -gluon string and field-theory amplitudes

in spinor-helicity variables [34]. Soft theorems for gluons can be derived using (4.42) which

take the form of “double-soft theorems” for scaffolded scalars [35, 36]. We also discover

hidden properties of gluon amplitudes, for instance, the field-theory amplitudes admit an

interesting expansion associated with a sum over all facets of the associahedron [34].


45


**4.5.1** **Triangulation-independent** **formula**


One apparent drawback of our result (4.42) is that it seems to depend on the triangulation,
namely both the form _dy_ / _y_ [2] and those first and second derivatives in _V_ and _W_ depend on
the triangulation of the _n_ -gon. Here we will show that by absorbing some _y_ factors into _V_

and _W_ we can make both of them triangulation independent. Such a rewriting also makes

it manifest that the new _V_ and _W_ can be expressed in terms of products of _u_ ’s, which have

nice graphical interpretations.
To begin with, note that in the scaffolding triangulation, each _u_ 2 _a_ −1 _,_ 2 _a_ +1 is proportional
to _ya_, and we define
_u_ 2 _a_ −1 _,_ 2 _a_ +1 ≡ _yau_ ˆ2 _a_ −1 _,_ 2 _a_ +1 _,_ (4.44)


and it is crucial to use the _u_ -equations

_u_ 2 _a,j_ + _u_ 2 _a_ −1 _,_ 2 _a_ +1 ∏ _ui_ = 1 _,_ (4.45)
_i_ ∈ _Dj_

where subset _Dj_ includes the curves intersecting with (2 _a,j_ ) except (2 _a_ −1 _,_ 2 _a_ +1). In the
limit _ya_ → 0, we expand _u_ -equations (4.45) as

_u_ 2 _a,j_ ∣ _ya_ =0 = 1 _,_ (4.46)


as well as
_∂u_ 2 _a,j_

∣ = − _u_ ˆ2 _a_ −1 _,_ 2 _a_ +1 ∏ _ui_ ∣ _ya_ =0 _,_ (4.47)
_∂ya_ _ya_ =0 _i_ ∈ _Dj_


where we have expressed the first derivative in terms of _u_ ˆ and product of those _u_ ’s crossing (2 _a_ −1 _,_ 2 _a_ +1). Similarly from the _u_ -equation of _u_ 2 _a,_ 2 _b_, we can derive that the second
derivative is given by


_∂_ [2] _u_ 2 _a,_ 2 _b_

= − _u_ ˆ2 _a_ −1 _,_ 2 _a_ +1 _u_ ˆ2 _b_ −1 _,_ 2 _b_ +1 ∏ _ui_ ∣ _ya_ =0 _,yb_ =0 _,_ (4.48)
_∂ya∂yb_ _i_ ∈ _E_

where subset _E_ includes curves intersecting with (2 _a,_ 2 _b_ ) except for (2 _a_ −1 _,_ 2 _a_ +1) and
(2 _b_ −1 _,_ 2 _b_ +1).
Now it becomes obvious that for any term of the summation in (4.42), there is a
common factor ∏ _[n]_ _a_ =1 _[u]_ [ˆ][2] _[a]_ [−][1] _[,]_ [2] _[a]_ [+][1] [from] [the] _[u]_ [ˆ][’s] [in] [each] _[V]_ [and] _[W]_ [’s,] [which] [cancels] [the] [ratio]
(∏( _i,j_ )∈even _ui,j_ /(∏( _i,j_ )∈odd _ui,j_ ))∣ _ya_ =0 to give:



_n_ _[u][i,j]_
∏ _u_ ˆ2 _a_ −1 _,_ 2 _a_ +1 ( [∏][(] _[i,j]_ [)∈][even] )∣
_a_ =1 ∏( _i,j_ )∈odd _ui,j_



= ∏
_ya_ =0 _i,j_ ∈ _n_ −gon



1
_,_ (4.49)
_ui,j_



This gives us a triangulation-independent formula for the scaffolding residue, which
contains the invariant ( _n_ −3)-form _dy_ / _y_ and the Koba-Nielsen factor ∏ _u_ _[X]_ [−][1] :



_r_
∏ _Wi_ [′] _a,ja_
_a_


46



_n_ −2 _r_ ⎞
∏ _Vk_ [′] _b_ _ui,j_ _[α]_ [′] _[X][i,j]_ [−][1] _,_ (4.50)
_b_ ⎠ ( [∏] _ij_ )



⎛⌊ _n_ /2⌋+1

∑ ∑

⎝ _r_ =0 { _i,j_ } _,_ { _k_ }



∏
0 _a_



d _ya_

_ya_



∫



∞


**Figure** **21** : _V_ [′] and _W_ [′] in terms _u_ ’s for _n_ = 4.


where we have redefined _V_ and _W_ to be

_Va_ [′] [= −] _[α]_ [′][ ∑] ( _X_ 2 _a,j_  - _X_ 2 _a_ −1 _,j_ ) ∏ _ui_ ∣ _ya_ =0 _,_ _Wa,b_ [′] [= −] _[α]_ [′] _[c]_ [2] _[a]_ [−][1] _[,]_ [2] _[b]_ [−][1] [∏] _ui_ ∣ _ya_ =0 _,yb_ =0 _,_ (4.51)
_j_ _i_ ∈ _Dj_ _i_ ∈ _E_


which are written in terms of a product of _u_ ’s without referring to any specific triangulation.
The product of the _u_ ’s appearing in the definitions of _Va_ [′] [and] _[W]_ [ ′] _a,b_ [have] [a] [very] [simple]
graphical interpretation. For the coefficient of ( _X_ 2 _a,j_ - _X_ 2 _a_ −1 _,j_ ) in _Va_ [′] [we] [simply] [take] [the]
product over all the _u_ ’s in the inner _n_ -gon that intersects (2 _a,j_ ). For _Wa,b_ [′] [we] [similarly]
have the product over all the _u_ ’s of the inner _n_ -gon that intersect (2 _a,_ 2 _b_ ).
For example, the _n_ = 3 amplitude is given by _V_ 1 [′] _[V]_ 2 [′] _[V]_ 3 [′] [+] _[ V]_ 1 [′] _[W]_ [ ′] 2 _,_ 3 [+][ perm] _[.]_ [with]

_V_ 1 [′] [= −] _[α]_ [′] _[X]_ [2] _[,]_ [5] _[,]_ _W_ 1 [′] _,_ 2 [= −] _[α]_ [′] _[c]_ [1] _[,]_ [3] _[,]_ (4.52)

and cyclic images _e.g._ _V_ 2 = − _α_ [′] _X_ 1 _,_ 4. In this case, there is no integral left in (4.50) and we
reproduce the familiar result (4.64).
For _n_ = 4 case, we have the following _V_ [′] and _W_ [′], where the product of _u_ ’s are shown
in Fig. 21:

_V_ 1 [′] [= −] _[α]_ [′][(] _[u]_ [3] _[,]_ [7][(] _[X]_ [2] _[,]_ [5] [−] _[X]_ [1] _[,]_ [5][)+] _[u]_ [1] _[,]_ [5] _[X]_ [2] _[,]_ [7][)] _[,]_ _W_ 1 [′] _,_ 2 [= −] _[α]_ [′] _[c]_ [1] _[,]_ [3] _[u]_ [3] _[,]_ [7] _[,]_ _W_ 1 [′] _,_ 3 [= −] _[α]_ [′] _[c]_ [1] _[,]_ [5] _[u]_ [1] _[,]_ [5] _[u]_ [3] _[,]_ [7] _[,]_ [(4.53)]


47


**Figure** **22** : _V_ [′] and _W_ [′] in terms _u_ ’s for _n_ = 5.


as well as their cyclic images. Similar to (4.43), we have 3 + 6 + 1 terms of the form _W_ [′] _W_ [′],
_W_ [′] _V_ [′] _V_ [′] and _V_ [′] _V_ [′] _V_ [′] _V_ [′] respectively, and (4.50) becomes:



1 _,_ 2 _[W]_ [ ′] 3 _,_ 4 [+][ perms] _[.]_ [) + (] _[W]_ [ ′] 1 _,_ 2 _[V]_ 3 [′] _[V]_ 4 [′] [+][ perm] _[.]_ [) +] _[ V]_ 1 [′] _[V]_ 2 [′] _[V]_ 3 [′] _[V]_ 4 [′][)] _[u][α]_ 1 _,_ [′] 5 _[X]_ [1] _[,]_ [5][−][1] _u_ _[α]_ 3 _,_ [′] 7 _[X]_ [3] _[,]_ [7][−][1] _,_
_y_ [((] _[W]_ [ ′]



_dy_

0 _y_



∫



∞



(4.54)
where only one integration variable is left, which can be chosen as _y_ = _y_ 1 _,_ 5 or _y_ 3 _,_ 7 depending
on the inner triangulation. For the former we have _u_ 1 _,_ 5 = _y_ 1 _,_ 5/(1 + _y_ 1 _,_ 5) and _u_ 3 _,_ 7 = 1 - _u_ 1 _,_ 5 =
1/(1 + _y_ 1 _,_ 5), and the other way around for the latter.
Finally, we present these building blocks for _n_ = 5 amplitude which can be nicely
summarized in figure 22. All cyclically inequivalent ones are:

_V_ 1 [′] [= −] _[α]_ [′][(] _[u]_ [3] _[,]_ [7] _[u]_ [3] _[,]_ [9] [(] _[X]_ [2] _[,]_ [5] [−] _[X]_ [1] _[,]_ [5][) +] _[ u]_ [1] _[,]_ [5] _[u]_ [3] _[,]_ [9] _[u]_ [5] _[,]_ [9] [(] _[X]_ [2] _[,]_ [7] [−] _[X]_ [1] _[,]_ [7][) +] _[ u]_ [1] _[,]_ [5] _[u]_ [1] _[,]_ [7] _[X]_ [2] _[,]_ [9][)] _[,]_ (4.55)

_W_ 1 [′] _,_ 2 [= −] _[α]_ [′] _[c]_ [1] _[,]_ [3] _[u]_ [3] _[,]_ [7] _[u]_ [3] _[,]_ [9] _[,]_ _W_ 1 [′] _,_ 3 [= −] _[α]_ [′] _[c]_ [1] _[,]_ [5] _[u]_ [1] _[,]_ [5] _[u]_ [3] _[,]_ [7] _[u]_ [3] _[,]_ [9] _[u]_ [5] _[,]_ [9] _[.]_ (4.56)

The _n_ = 5 string amplitude is a two-fold integral as in (4.50), where in the summation we
have _V_ 1 [′][⋯] _[V]_ 5 [′][,] [10] [permutations] [of] _[V]_ 1 [′] _[V]_ 2 [′] _[V]_ 3 [′] _[W]_ [ ′] 4 _,_ 5 [,] [and] [15] [permutations] [of] _[V]_ 1 [′] _[W]_ [ ′] 2 _,_ 3 _[W]_ [ ′] 4 _,_ 5 [.]


**4.6** **Consistency** **check:** **From** **4** _n_ **-scalars** **to** **2** _n_ **-scalars**


Now that we have an explicit form for the gluon amplitude obtained after taking the

scaffolding residue, we can perform a nice consistency check. Suppose we did not know the

bosonic string answer, and so we did not know a priori that the scalars we are scattering

can be thought of as higher-dimensional polarizations of gluons. How could we discover

this fact inherently within our world?


48


One way of doing this is to start with a 4 _n_ -scalar string amplitude. In this case, taking

the scaffolding residue leads to a 2 _n_ -gluon string amplitude; if we then choose the special

polarizations in (4.3), the result must simplify dramatically to land on the 2 _n_ -scalar string

amplitude again!

We will now see that very nicely this is indeed the case. Let us consider the 4 _n_ -scalar
scattering labelled by {1 _,_ 1 [′] _,_ 2 _,_ 2 [′] _,...,_ 2 _n,_ 2 _n_ [′] }, which results in the 2 _n_ -gluon scattering by
taking the scaffolding residues { _X_ 1 _,_ 2 _,X_ 2 _,_ 3 _,...,X_ 2 _n,_ 1}. Recalling the dimensional reduction
that turns the gluons into the 2 _n_ -scalars, eq. (4.3), we see that this is equivalent to take
the derivative _∂ϵ_ 1⋅ _ϵ_ 2 _∂ϵ_ 3⋅ _ϵ_ 4 _...∂ϵ_ 2 _n_ −1⋅ _ϵ_ 2 _n_ on the conventional string correlator. On the other
hand, in the 4 _n_ -scalar kinematic configuration, we have:

_ϵ_ _[µ]_ _i_ [∝(][1][ −] _[α]_ [)(] _[X][i]_ [+][1][ −] _[X][i]_ [′][)] _[µ]_ [ −] _[α]_ [(] _[X][i]_ [′][ −] _[X][i]_ [)] _[µ][,]_ (4.57)

_qi_ _[µ]_ [∝(] _[X][i]_ [+][1][ −] _[X][i]_ [)] _[µ][ .]_ (4.58)


Importantly, as we have mentioned before, the dependence on _Xi_ [′] _,j_ [′] only appears in
_ϵi_ ⋅ _ϵj_ . Therefore, the above derivative on Lorentz product of _ϵ_ is equivalent to the following
derivative in our kinematic configuration:

_∂ϵ_ 1⋅ _ϵ_ 2 _∂ϵ_ 3⋅ _ϵ_ 4 _...∂ϵ_ 2 _n_ −1⋅ _ϵ_ 2 _n_ ∼(−2) _[n]_ _∂X_ 1′ _,_ 2′ _∂X_ 3′ _,_ 4′ _...∂X_ 2 _n_ −1′ _,_ 2 _n_ ′ _,_ (4.59)


where in the RHS we have included the normalization factor. Now recall the _X_ ’s dependence in the building blocks of our “stringy correlator”: _Vi_ [′] [depends] [on] _[X][i]_ [′] _[,j][,X][i,j]_ [for] [some]
_j_ (with no prime), _Wi,j_ [′] [depends] [on] _[c][i,j]_ [=] _[X][i,j]_ [+] _[ X][i]_ [′] _[,j]_ [′] [−] _[X][i]_ [′] _[,j]_ [−] _[X][i,j]_ [′][.] [Therefore,] [it] [is] [clear]
that the derivative (4.59) resulting on only one term:

_W_ 1 [′] _,_ 2 _[W]_ [ ′] 3 _,_ 4 _[...W]_ [ ′] 2 _n_ −1 _,_ 2 _n_ [→(−][1][)] _[n]_ [(−][2][)] _[n]_ [∏] ∏ _ui,j_
_i_ ∈even _j_ ≠ _i_ −1 _,i,i_ +1

(4.60)
= 2 _[n]_ ∏ _u_ [2] _i,j_ ∏ _uk,l,_
( _i,j_ )∈even _k_ ∈even _,l_ ∈odd


where all the indices in the subscript only involve labels with no prime. For example,
consider (4 _n_ = 12)-scalar to (2 _n_ = 6)-scalar, the one term that contributes to the derivative
reads(see Fig. 23):
_W_ 1 [′] _,_ 2 _[W]_ [ ′] 3 _,_ 4 _[W]_ [ ′] 5 _,_ 6 [→] [8] _[u]_ 2 [2] _,_ 4 _[u]_ [2] 2 _,_ 6 _[u]_ [2] 4 _,_ 6 _[u]_ [2] _[,]_ [5] _[u]_ [1] _[,]_ [4] _[u]_ [3] _[,]_ [6] _[,]_ (4.61)


49


where we have set _α_ [′] = 1. Recall in (4.50) we have an overall factor 1/(∏( _i,j_ ) _ui,j_ ), therefore the dimensional reduction transforms the 2 _n_ -scaffolding-gluon to the 2 _n_ -scalar correctly with the factor 2 _[n]_ ∏( _i,j_ )∈even _ui,j_ /∏( _i,j_ )∈odd _ui,j_, which in the above example reads
8( _u_ 2 _,_ 4 _u_ 2 _,_ 6 _u_ 4 _,_ 6)/( _u_ 1 _,_ 3 _u_ 1 _,_ 5 _u_ 3 _,_ 5) as expected.


**4.7** **Examples**


We end our tree-level discussion by presenting some explicit examples of how to use (4.1)

to extract gluon amplitudes. For simplicity, we will be focusing on the 3- and 4-point

amplitudes. In section 4.8, we make some comments on how to systematically extract the

field theory gluon amplitude at higher points.


**4.7.1** **3-point** **example**


To obtain the 3-point gluon interaction we start with the 6-scalar amplitude. Picking the
scaffolding triangulation { _X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,X_ 1 _,_ 5} we obtain



1 _,_ 3 d _y_ 3 _,_ 5 d _y_ 1 _,_ 5

_y_ 1 [2] _,_ 3 _[y]_ 3 [2] _,_ 5 _[y]_ 1 [2] _,_ 5 ∏ _i,j_ _u_ _[α]_ _ij_ [′] _[X][i,j]_ ( _[u]_ _u_ [2] 1 _[,]_ _,_ [4] 3 _[u]_ _u_ [2] 3 _[,]_ _,_ [6] 5 _[u]_ _u_ [4] 5 _[,]_ _,_ [6] 7



d _y_ 1 _,_ 3 d _y_ 3 _,_ 5 d _y_ 1 _,_ 5
0 _y_ [2] _[y]_ [2] _[y]_ [2]




_[u]_ [2] _[,]_ [4] _[u]_ [2] _[,]_ [6] _[u]_ [4] _[,]_ [6] ) _._ (4.62)

_u_ 1 _,_ 3 _u_ 3 _,_ 5 _u_ 5 _,_ 7



A6 = ∫



∞



Plugging in the explicit parametrization, _ui,j_ ( _y_ 1 _,_ 3 _,y_ 3 _,_ 5 _,y_ 1 _,_ 5), yields:



1 _,_ 3 d _y_ 3 _,_ 5 d _y_ 1 _,_ 5

_y_ 1 [2] _,_ 3 _[y]_ 3 [2] _,_ 5 _[y]_ 1 [2] _,_ 5 _y_ 1 _[α]_ _,_ [′] 3 _[X]_ [1] _[,]_ [3] _y_ 3 _[α]_ _,_ [′] 5 _[X]_ [3] _[,]_ [5] _y_ 1 _[α]_ _,_ [′] 5 _[X]_ [1] _[,]_ [5] (1 + _y_ 1 _,_ 3) [−] _[α]_ [′] _[c]_ [1] _[,]_ [4] (1 + _y_ 1 _,_ 5) [−] _[α]_ [′] _[c]_ [2] _[,]_ [5] (1 + _y_ 3 _,_ 5) [−] _[α]_ [′] _[c]_ [3] _[,]_ [6]



d _y_ 1 _,_ 3 d _y_ 3 _,_ 5 d _y_ 1 _,_ 5
0 _y_ [2] _[y]_ [2] _[y]_ [2]



A6 = ∫



∞



× (1 + _y_ 1 _,_ 3 + _y_ 1 _,_ 3 _y_ 3 _,_ 5) [−] _[α]_ [′] _[c]_ [1] _[,]_ [3] (1 + _y_ 1 _,_ 5 + _y_ 1 _,_ 5 _y_ 1 _,_ 3) [−] _[α]_ [′] _[c]_ [1] _[,]_ [5] (1 + _y_ 3 _,_ 5 + _y_ 3 _,_ 5 _y_ 1 _,_ 5) [−] _[α]_ [′] _[c]_ [3] _[,]_ [5] _._
(4.63)
As discussed in 4.2.2, taking the scaffolding residue amounts to setting _X_ 1 _,_ 3 = _X_ 3 _,_ 5 =
_X_ 1 _,_ 5 = 0, and collecting the piece of the integrand that is linear in _y_ 1 _,_ 3 _,y_ 3 _,_ 5 and _y_ 1 _,_ 5. In
this case, after taking this residue there are no integrations left and we get:



_A_ [gluon] 3 = _α_ [′][ 2] ( _c_ 1 _,_ 3 _c_ 1 _,_ 5 + _c_ 1 _,_ 3 _c_ 2 _,_ 5 + _c_ 1 _,_ 3 _c_ 3 _,_ 5 + _c_ 1 _,_ 4 _c_ 3 _,_ 5 + _c_ 1 _,_ 5 _c_ 3 _,_ 5 + _c_ 1 _,_ 5 _c_ 3 _,_ 6) +




- _α_ [′][ 3] ( _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 6)



(4.64)



= _α_ [′][ 2] (−( _X_ 2 _,_ 5 − _X_ 2 _,_ 6) _X_ 1 _,_ 4 −( _X_ 3 _,_ 6 − _X_ 4 _,_ 6) _X_ 2 _,_ 5 −( _X_ 1 _,_ 4 − _X_ 2 _,_ 4) _X_ 3 _,_ 6)




- _α_ [′][ 3] ( _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 6) _._



The leading piece in _α_ [′] is exactly the Yang-Mills amplitude, and we can check it
precisely matches (3.27). The sub-leading term corresponds to the _F_ [3] vertex, which has

higher units.

Before proceeding, let’s use this simple example to highlight two non-trivial features

of this scaffolded gluon amplitude: First, since we extract the answer via this scaffolding

residue, the amplitude can be written as a function of **solely** **non-planar** **variables**,
_ci,j_ = - _pi_ ⋅ _pj_, with _i_ and _j_ non-adjacent. This is a non-trivial general fact that will be
explored further in [34]. Second, as we have mentioned already, in this scalar language

the amplitude takes a unique form, there is no gauge-redundancy ambiguity in how it is

expressed.


50


**4.7.2** **4-point** **example:** **string** **and** **field-theory** **amplitudes**



For _n_ = 4, after taking the scaffolding residue we are left with one integration - which we
can trivially perform – so we now present explicitly the integrated 4-gluon string amplitude.

To do this, we use the result we get after taking the scaffolding residue in terms of _V_ ’s and

_W_ ’s presented in (4.54), but now we explicitly evaluate the last integration.

Let us define



_I_ ( _a,b_ ) ∶= [Γ][(] _[X]_ [1] _[,]_ [5][ +] _[ a]_ [)][Γ][(] _[X]_ [3] _[,]_ [7][ +] _[ b]_ [)]



(4.65)
Γ ~~(~~ _X_ 1 _,_ 5 ~~+~~ _X_ 3 _,_ 7 ~~+~~ _a_ ~~+~~ _b_ ~~)~~ _[,]_



with integer shifts _a,b_ . The first term reads



1 _,_ 5

_u_ _[X]_ 1 _,_ 5 [1] _[,]_ [5][−][1] _u_ _[X]_ 3 _,_ 7 [3] _[,]_ [7][−][1] _W_ 1 [′] _,_ 2 _[W]_ [ ′] 3 _,_ 4 [=] _[ c]_ [1] _[,]_ [3] _[c]_ [5] _[,]_ [7] _[I]_ [(][1] _[,]_ [−][1][)] _[.]_ (4.66)
_y_ 1 _,_ 5



_dy_ 1 _,_ 5
0 _y_



∫



∞



The second term, _i.e._ the integral of _W_ 2 [′] _,_ 3 _[W]_ [ ′] 1 _,_ 4 [is] [given] [by] [the] [cyclic] [rotation] [for] [the]
4-gon: _Xi,j_ → _Xi_ +2 _,j_ +2, which acts on _I_ ( _a,b_ ) as _I_ ( _a,b_ ) → _I_ ( _b,a_ ). The third term reads:



1 _,_ 5

_u_ _[X]_ 1 _,_ 5 [1] _[,]_ [5][−][1] _u_ _[X]_ 3 _,_ 7 [3] _[,]_ [7][−][1] _W_ 1 [′] _,_ 3 _[W]_ [ ′] 2 _,_ 4 [=] _[ c]_ [1] _[,]_ [3] _[c]_ [3] _[,]_ [7] _[I]_ [(][1] _[,]_ [1][)] _[.]_ (4.67)
_y_ 1 _,_ 5



_dy_ 1 _,_ 5
0 _y_



∫



∞



For combinations of the type _W_ [′] _V_ [′] _V_ [′], we have



1 _,_ 5

_y_ 1 _,_ 5 _u_ _[X]_ 1 _,_ 5 [1] _[,]_ [5][−][1] _u_ _[X]_ 3 _,_ 7 [3] _[,]_ [7][−][1] _W_ 1 [′] _,_ 2 _[V]_ 3 [′] _[V]_ 4 [′]



_dy_ 1 _,_ 5
0 _y_



∫



∞



_c_ 1 _,_ 3 _I_ (1 _,_ 0)
= (( _X_ 1 _,_ 5 − 1)( _X_ 1 _,_ 5 ( _X_ 3 _,_ 6 − _X_ 3 _,_ 7) + _X_ 1 _,_ 6 _X_ 3 _,_ 7)( _X_ 3 _,_ 7 − _X_ 3 _,_ 8)
~~(~~ _X_ 1 _,_ 5 ~~−~~ 1 ~~)~~ _X_ 1 _,_ 5



(4.68)



+ _X_ 3 _,_ 7 ( _X_ 3 _,_ 6 − _X_ 1 _,_ 6 ( _X_ 3 _,_ 7 + 1) + _X_ 1 _,_ 5 (− _X_ 3 _,_ 6 + _X_ 3 _,_ 7 + 1)) _X_ 5 _,_ 8) _,_



and three more terms with _W_ 2 [′] _,_ 3 _[V]_ 4 [′] _[V]_ 1 [′] _[,W]_ [ ′] 3 _,_ 4 _[V]_ 1 [′] _[V]_ 2 [′][,] [and] _[W]_ [ ′] 1 _,_ 4 _[V]_ 2 [′] _[V]_ 3 [′] [are] [obtained] [from] [cyclic]
rotations (proportional to _I_ 0 _,_ 1 _,I_ 1 _,_ 0 and _I_ 0 _,_ 1). Similarly, for _W_ 1 [′] _,_ 3 _[V]_ 2 [′] _[V]_ 4 [′] [we] [have]



1 _,_ 5

_y_ 1 _,_ 5 _u_ _[X]_ 1 _,_ 5 [1] _[,]_ [5][−][1] _u_ _[X]_ 3 _,_ 7 [3] _[,]_ [7][−][1] _W_ 1 [′] _,_ 3 _[V]_ 2 [′] _[V]_ 4 [′]



_dy_ 1 _,_ 5
0 _y_



∫



∞



= _[c]_ [1] _[,]_ [5] _[I]_ [(][1] _[,]_ [1][)]




[1] _[,]_ [1]

_[c]_ [1] _[,]_ [5] _[I]_ ( _X_ 1 _,_ 5 ( _X_ 3 _,_ 7 − _X_ 3 _,_ 8)(( _X_ 1 _,_ 4 − _X_ 1 _,_ 5 − 1) _X_ 3 _,_ 7 + ( _X_ 1 _,_ 5 + 1) _X_ 4 _,_ 7)

_X_ 1 _,_ 5 _X_ 3 _,_ 7



(4.69)




   - _X_ 3 _,_ 7 ( _X_ 1 _,_ 4 ( _X_ 3 _,_ 7 + 1) + _X_ 1 _,_ 5 ( _X_ 4 _,_ 7 − _X_ 3 _,_ 7)) _X_ 5 _,_ 8) _,_

and another term with _W_ 2 [′] _,_ 4 _[V]_ 1 [′] _[V]_ 3 [′] [by] [cyclic] [rotation.] The last case, the integral with
_V_ 1 [′] _[V]_ 2 [′] _[V]_ 3 [′] _[V]_ 4 [′][,] [is] [given] [by]

_P_ 0 _I_ (−1 _,_ 3) + _P_ 1 _I_ (0 _,_ 2) + _P_ 2 _I_ (1 _,_ 1) + _P_ 3 _I_ (2 _,_ 0) + _P_ 4 _I_ (3 _,_ −1) _,_ (4.70)

where we have degree-4 polynomials in _X_ ’s, _Pi_ with _i_ = 0 _,_ 1 _,_ ⋯ _,_ 4, as follows

_P_ 0 = _X_ 1 _,_ 4 _X_ 5 _,_ 8 ( _X_ 2 _,_ 5 − _X_ 1 _,_ 5)( _X_ 1 _,_ 6 − _X_ 1 _,_ 5) _,_ (4.71)

_P_ 1 = _X_ 1 _,_ 4 ( _X_ 1 _,_ 6 − _X_ 1 _,_ 5)( _X_ 2 _,_ 5 − _X_ 1 _,_ 5)( _X_ 3 _,_ 8 − _X_ 3 _,_ 7) + _X_ 1 _,_ 4 ( _X_ 1 _,_ 6 − _X_ 1 _,_ 5) _X_ 2 _,_ 7 _X_ 5 _,_ 8
(4.72)
+ _X_ 1 _,_ 4 ( _X_ 2 _,_ 5 − _X_ 1 _,_ 5) _X_ 3 _,_ 6 _X_ 5 _,_ 8 + ( _X_ 1 _,_ 6 − _X_ 1 _,_ 5)( _X_ 2 _,_ 5 − _X_ 1 _,_ 5)( _X_ 4 _,_ 7 − _X_ 3 _,_ 7) _X_ 5 _,_ 8 _,_


51


_P_ 2 = _X_ 1 _,_ 4 ( _X_ 1 _,_ 6 − _X_ 1 _,_ 5) _X_ 2 _,_ 7 ( _X_ 3 _,_ 8 − _X_ 3 _,_ 7) + _X_ 1 _,_ 4 ( _X_ 2 _,_ 5 − _X_ 1 _,_ 5) _X_ 3 _,_ 6 ( _X_ 3 _,_ 8 − _X_ 3 _,_ 7)

+ ( _X_ 1 _,_ 6 − _X_ 1 _,_ 5)( _X_ 2 _,_ 5 − _X_ 1 _,_ 5)( _X_ 4 _,_ 7 − _X_ 3 _,_ 7)( _X_ 3 _,_ 8 − _X_ 3 _,_ 7) + _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 6 _X_ 5 _,_ 8
+ ( _X_ 1 _,_ 6 − _X_ 1 _,_ 5) _X_ 2 _,_ 7 ( _X_ 4 _,_ 7 − _X_ 3 _,_ 7) _X_ 5 _,_ 8 + ( _X_ 2 _,_ 5 − _X_ 1 _,_ 5) _X_ 3 _,_ 6 ( _X_ 4 _,_ 7 − _X_ 3 _,_ 7) _X_ 5 _,_ 8 ;



(4.73)



and _P_ 3 and _P_ 4 are obtained from _P_ 1 and _P_ 0 by cyclic rotation, respectively. Adding these
contributions we obtain the explicit result of _n_ = 4 string amplitude.
Finally, we present the 4-point Yang-Mills amplitude, which is given by the _α_ [′] → 0
limit of the full stringy result. Just as we saw at 3-points case, we find that the result takes

a suggestive “c-expansion” form:




[({] _[c][i,j]_ [})]

+ _[N]_ [3] _[,]_ [7][({] _[c][i,j]_ [})]
_X_ 1 _,_ 5 _X_ 3 _,_ 7



_A_ [YM] 4 = _α_ [′][2] ( _[N]_ [1] _[,]_ [5][({] _[c][i,j]_ [})]




_[c][i,j]_

+ _c_ 1 _,_ 5 _c_ 3 _,_ 7) _,_ (4.74)
_X_ 3 _,_ 7



where we have two poles, _X_ 1 _,_ 5 and _X_ 3 _,_ 7, with numerators _N_ 1 _,_ 5 and _N_ 3 _,_ 7 = _N_ 1 _,_ 5∣ _i_ → _i_ +2, as
well as a “contact term” _c_ 1 _,_ 5 _c_ 3 _,_ 7. Both the contact term and these two numerators can
be expressed solely in terms of _ci,j_ ’s. This is not at all guaranteed a priori but reflects a
general phenomenon we will explore for all _n_ in forthcoming work [34]. The numerator
_N_ 1 _,_ 5 is given by:



_N_ 1 _,_ 5 = − _c_ 1 _,_ 5 _c_ [2] 3 _,_ 7 [−] _[c]_ [1] _[,]_ [3] _[c]_ [1] _[,]_ [5] _[c]_ [3] _[,]_ [7] [−] _[c]_ [1] _[,]_ [5] _[c]_ [1] _[,]_ [7] _[c]_ [3] _[,]_ [7] [−] _[c]_ [1] _[,]_ [3] _[c]_ [2] _[,]_ [5] _[c]_ [3] _[,]_ [7] [−] _[c]_ [1] _[,]_ [5] _[c]_ [2] _[,]_ [7] _[c]_ [3] _[,]_ [7] [−] _[c]_ [1] _[,]_ [3] _[c]_ [3] _[,]_ [5] _[c]_ [3] _[,]_ [7]

   - _c_ 1 _,_ 5 _c_ 3 _,_ 6 _c_ 3 _,_ 7 − _c_ 1 _,_ 5 _c_ 3 _,_ 8 _c_ 3 _,_ 7 − _c_ 1 _,_ 5 _c_ 4 _,_ 7 _c_ 3 _,_ 7 − _c_ 1 _,_ 3 _c_ 5 _,_ 7 _c_ 3 _,_ 7 − _c_ 1 _,_ 4 _c_ 5 _,_ 7 _c_ 3 _,_ 7 − _c_ 1 _,_ 5 _c_ 5 _,_ 7 _c_ 3 _,_ 7

   - _c_ 1 _,_ 3 _c_ 5 _,_ 8 _c_ 3 _,_ 7 − _c_ 1 _,_ 4 _c_ 5 _,_ 8 _c_ 3 _,_ 7 − _c_ 1 _,_ 7 _c_ 5 _,_ 8 _c_ 3 _,_ 7 − _c_ 1 _,_ 3 _c_ 1 _,_ 5 _c_ 1 _,_ 7 − _c_ 1 _,_ 3 _c_ 1 _,_ 7 _c_ 2 _,_ 5 − _c_ 1 _,_ 3 _c_ 1 _,_ 5 _c_ 2 _,_ 7

   - _c_ 1 _,_ 4 _c_ 1 _,_ 7 _c_ 3 _,_ 5 − _c_ 1 _,_ 5 _c_ 1 _,_ 7 _c_ 3 _,_ 5 − _c_ 1 _,_ 3 _c_ 2 _,_ 7 _c_ 3 _,_ 5 − _c_ 1 _,_ 4 _c_ 2 _,_ 7 _c_ 3 _,_ 5 − _c_ 1 _,_ 5 _c_ 2 _,_ 7 _c_ 3 _,_ 5 − _c_ 1 _,_ 5 _c_ 1 _,_ 7 _c_ 3 _,_ 6

   - _c_ 1 _,_ 5 _c_ 2 _,_ 7 _c_ 3 _,_ 8 − _c_ 1 _,_ 3 _c_ 1 _,_ 5 _c_ 4 _,_ 7 − _c_ 1 _,_ 3 _c_ 2 _,_ 5 _c_ 4 _,_ 7 − _c_ 1 _,_ 3 _c_ 3 _,_ 5 _c_ 4 _,_ 7 − _c_ 1 _,_ 4 _c_ 3 _,_ 5 _c_ 4 _,_ 7 − _c_ 1 _,_ 5 _c_ 3 _,_ 5 _c_ 4 _,_ 7

   - _c_ 1 _,_ 3 _c_ 1 _,_ 5 _c_ 5 _,_ 7 − _c_ 1 _,_ 3 _c_ 1 _,_ 6 _c_ 5 _,_ 7 − _c_ 1 _,_ 3 _c_ 1 _,_ 7 _c_ 5 _,_ 7 − _c_ 1 _,_ 3 _c_ 2 _,_ 5 _c_ 5 _,_ 7 − _c_ 1 _,_ 3 _c_ 2 _,_ 6 _c_ 5 _,_ 7 − _c_ 1 _,_ 3 _c_ 2 _,_ 7 _c_ 5 _,_ 7

   - _c_ 1 _,_ 5 _c_ 3 _,_ 5 _c_ 5 _,_ 7 − _c_ 1 _,_ 6 _c_ 3 _,_ 5 _c_ 5 _,_ 7 − _c_ 1 _,_ 7 _c_ 3 _,_ 5 _c_ 5 _,_ 7 − _c_ 1 _,_ 3 _c_ 3 _,_ 6 _c_ 5 _,_ 7 − _c_ 1 _,_ 4 _c_ 3 _,_ 6 _c_ 5 _,_ 7 − _c_ 1 _,_ 5 _c_ 3 _,_ 6 _c_ 5 _,_ 7

   - _c_ 1 _,_ 5 _c_ 3 _,_ 8 _c_ 5 _,_ 7 − _c_ 1 _,_ 6 _c_ 3 _,_ 8 _c_ 5 _,_ 7 − _c_ 1 _,_ 7 _c_ 3 _,_ 8 _c_ 5 _,_ 7 − _c_ 1 _,_ 3 _c_ 1 _,_ 7 _c_ 5 _,_ 8 − _c_ 1 _,_ 3 _c_ 2 _,_ 7 _c_ 5 _,_ 8 − _c_ 1 _,_ 7 _c_ 3 _,_ 5 _c_ 5 _,_ 8

   - _c_ 1 _,_ 5 _c_ 3 _,_ 5 _c_ 3 _,_ 7 − _c_ 1 _,_ 7 _c_ 5 _,_ 7 _c_ 3 _,_ 7 − _c_ 1 _,_ 3 _c_ 1 _,_ 7 _c_ 3 _,_ 5 − _c_ 1 _,_ 5 _c_ 1 _,_ 7 _c_ 3 _,_ 8 − _c_ 1 _,_ 5 _c_ 3 _,_ 8 _c_ 4 _,_ 7 − _c_ 1 _,_ 4 _c_ 3 _,_ 5 _c_ 5 _,_ 7

   - _c_ 1 _,_ 4 _c_ 3 _,_ 5 _c_ 3 _,_ 7 − _c_ 1 _,_ 6 _c_ 5 _,_ 7 _c_ 3 _,_ 7 − _c_ 1 _,_ 3 _c_ 2 _,_ 5 _c_ 2 _,_ 7 − _c_ 1 _,_ 5 _c_ 2 _,_ 7 _c_ 3 _,_ 6 − _c_ 1 _,_ 5 _c_ 3 _,_ 6 _c_ 4 _,_ 7 − _c_ 1 _,_ 3 _c_ 3 _,_ 5 _c_ 5 _,_ 7

   - _c_ 1 _,_ 7 _c_ 3 _,_ 6 _c_ 5 _,_ 7 − _c_ 1 _,_ 7 _c_ 3 _,_ 8 _c_ 5 _,_ 8 − _c_ 1 _,_ 6 _c_ 3 _,_ 6 _c_ 5 _,_ 7 − _c_ 1 _,_ 7 _c_ 3 _,_ 6 _c_ 5 _,_ 8 _._



(4.75)



This reduces to the “leading singularity” given in (6.9) upon sending _X_ 1 _,_ 5 → 0. It is
possible to simplify this formula somewhat by introducing the notation _cA,B_ = ∑ _k_ ∈ _A,l_ ∈ _B ck,l_,
so that e.g. _c_ 12 _,_ 34 = _c_ 1 _,_ 3 + _c_ 1 _,_ 4 + _c_ 2 _,_ 3 + _c_ 2 _,_ 4. Then we have

_N_ 1 _,_ 5 = − _c_ 3 _,_ 5678 ( _c_ 1 _,_ 67 _c_ 5 _,_ 7 + _c_ 1 _,_ 5 _c_ 12345 _,_ 7 + _c_ 1 _,_ 7 _c_ 5 _,_ 8) − _c_ 1 _,_ 4 ( _c_ 12345 _,_ 7 _c_ 3 _,_ 5 + _c_ 3 _,_ 67 _c_ 5 _,_ 7 + _c_ 3 _,_ 7 _c_ 5 _,_ 8)

    - _c_ 1 _,_ 3 ( _c_ 123 _,_ 5 _c_ 1234 _,_ 7 + _c_ 123 _,_ 567 _c_ 5 _,_ 7 + _c_ 123 _,_ 7 _c_ 5 _,_ 8) _._
(4.76)

Note that already the 4-point gluon amplitude looks more complicated than we are used

to from the familiar Parke-Taylor formulas in four dimensions. This reflects the basic fact

that _D_ -dimensional gluon amplitudes simply are richer than in four dimensions, and that

we are non-redundantly describing all possible gluon polarizations in a single expression.


52


**4.8** **Further** **comments**


**Simplicity** **of** **residue** **extraction** A fascinating general phenomenon has been encoun
tered repeatedly in “surfaceology” for amplitudes, which also appears in the context of the

computation of scaffolding residues we began with in this section that we would like to

highlight here.

After taking the scaffolding residue, we end up (as with the bosonic string gluon

expression) with a sum over exponentially many terms. What then is the point of beginning

with the “one-term” expression for the 2 _n_ scalar problem, if the final gluon expression looks

exponentially complicated in any case? Of course the scalar starting point is much more

compact and crucially allows us to see the deep connection between scalar, pions, and

gluons. But does it have a practical, computational advantage of any sort?

Naively the answer would seem to be “no”, but remarkably, while the analytic expres
sion for the residue indeed has exponentially many terms, the actual computation of the

residue can be done in polynomial time! This is a famous occurrence in various branches

of mathematics and physics. For instance, the analytic expression for the determinant of
an _n_ × _n_ matrix has _n_ ! terms but can be trivially computed in _n_ [3] time using Gaussian elimination. Similarly, if we look at the 10-th Newton polynomial of 10 [3] variables ∑ _xi_ 1⋯ _xi_ 10
where the _i_ ’s range from 1 _,_ ⋯ _,_ 10 [3], there are roughly 10 [30] terms in the sum, but for any
numerical values of the _xi_ we can get the answer in a nanosecond on a computer, simply
by looking at to the coefficient of _t_ [10] in the expansion of (1 + _tx_ 1)(1 + _tx_ 2)⋯(1 + _tx_ 1000).
The same thing occurs for the computation of our residue: the “one-term” starting

point from the 2 _n_ scalar problem allows us to compute a result naively needing expo
nentially many terms in polynomial time. As mentioned this is a special case of a gen
eral fact we have encountered repeatedly in the connection between amplitudes and the
combinatorial geometry of surfaces. At the most basic level, the _uX_ variables and their
tropicalizations to the “headlight functions” _αX_ generate the exponentially many cones
associated with Feynman diagrams from polynomially many expressions involving poly
nomially many terms. Extensions of the tropical formalism for computing amplitudes for

very general Lagrangians [37] see the same feature for generating numerator factors. It

would be fascinating to better understand the origins of this huge reduction in apparent

complexity for the sorts of polynomial expressions we encounter in scattering amplitudes.


**Integration** **Contour** **for** **Gluons** Our integral form for the 2 _n_ scalar scaffolded amplitude is given as an integral over positive _yi_ - 0, but of a form ∏ _i dyi_ / _yi_ [2] [with] [power-law]
singularities as _yi_ → 0. As such even in the field theory limit, where the _Xij_ close to zero,
the integral is not well defined on this naive contour and the result must be appropriately

analytically continued from the domain where the _X_ ’s are positive enough to make the integral converge. Given that these amplitudes arise from a simple kinematic shift of the Tr _ϕ_ [3],
this can be rephrased as the familiar fact discussed in our review of stringy Tr _ϕ_ [3] integrals,
that the integral form of the Koba-Nielsen formula only converges when the _Xi,j_ - 0, and
continuing to the physically interesting region where we see resonances and the amplitude
has poles, where _Xi,j_ < 0, is accomplished by analytic continuation. As discussed there and
at greater length in [27], the _u_ / _y_ variables make it easy to define an explicit contour on


53


which the integral converges for _any_ _Xi,j_ . For the purposes of this paper, this is enough to
concretely specify a contour on which our scaffolded gluon amplitudes can be concretely

evaluated.


**Field Theory Limit For Gluons** Extracting the field theory limit of our scalar-scaffolded
gluon amplitude is more challenging than for Tr _ϕ_ [3] theory. As we discussed earlier, the _dy_ / _y_
singularity makes it easy to extract the low-energy limit of the amplitudes for _α_ [′] _X_ ≪ 1,
localizing to logarithmic divergences as ∣log _y_ ∣→∞. This procedure does not work immediately for our scaffolded gluons, where the _dy_ / _y_ [2] form has power-law divergences and the
integral must be defined by analytic continuation, even at tree-level. In [34] will report

on an elementary and direct way of extracting the field theory limit, via a “cone-by-cone”

analysis of the singular behavior of the integrand. This will be analyzed systematically

at tree and loop level in [34], but we can illustrate with the simplest but still non-trivial

example of the four-point amplitude.

We begin by arbitrarily dividing the integral over _y_ into two regions, for _y_ between
(0,1) and (1 _,_ ∞). Then we have




[1] _[,]_ [3]

_y_ 1 _[X]_ _,_ 3 [1] _[,]_ [3][(][1][ +] _[ y]_ [1] _[,]_ [3][)][−] _[c]_ [1] _[,]_ [3] _[,]_ (4.77)
_y_ 1 [2] _,_ 3



) _[dy]_ [1] _[,]_ [3]
1 _y_ [2]



A [gluon] 4 = (∫



1

0 [+∫]



1



∞



where _c_ 1 _,_ 3 = _X_ 1 _,_ 3 + _X_ 2 _,_ 4 is a “mesh constant” in the language of [6, 12].
We will now extract the leading singular behavior from each piece in a standard way.
For _y_ ⊂(0 _,_ 1), we can expand



1 _,_ 3

_y_ 1 _[X]_ _,_ 3 [1] _[,]_ [3] [(][1][ + (−] _[c]_ [1] _[,]_ [3][)] _[y]_ [1] _[,]_ [3][ +] [(−] _[c]_ [1] _[,]_ [3][)(−] _[c]_ [1] _[,]_ [3][ −] [1][)]
_y_ 1 [2] _,_ 3 2



1 _dy_ 1 _,_ 3

0 _y_ [2]




_[c]_ [1] _[,]_ [3] [1]

_y_ 1 [2] _,_ 3 [+ ⋯) =]
2



∫



1




_[c]_ [1] _[,]_ [3] + [(−] _[c]_ [1] _[,]_ [3][)(−] _[c]_ [1] _[,]_ [3][ −] [1][)]

_X_ 1 _,_ 3 2




_[c]_ [1] _[,]_ [3] + ⋯ _,_

_X_ 1 _,_ 3



= 1
_X_ 1 _,_ 3 ~~−~~ 1 [−] _X_ _[c]_ [1] 1 _[,]_ _,_ [3]




_[c]_ [1] _[,]_ [3] [1]

+ ⋯= −1 + ⋯− _[c]_ [1] _[,]_ [3]
2 _X_ 1 _,_



(4.78)



where in the second line we have kept the leading terms at low energies, which here scale as
_X_ [0] as opposed to _X_ [−][1] we are familiar with for the Tr _ϕ_ [3] amplitude. Note that in performing
this integral we are assuming that _X_ 1 _,_ 3 > 1 for convergence, and indeed the leading singular
term 1/( _X_ 1 _,_ 3 − 1) has a pole at _X_ 1 _,_ 3 = 1, but we are then free to analytically continue and
expand in _X_ 1 _,_ 3 around zero. Doing this converts the naive power-law divergence we would
get from the d _y_ 1 _,_ 3/ _y_ 1 [2] _,_ 3 [behavior] [near] _[y]_ [1] _[,]_ [3][ →] [0,] [to] [simply] [the] [constant] [term] [−][1.] [Performing]
a similar analysis for _y_ 1 _,_ 3 ⊂(1 _,_ ∞), we find that the leading behavior simply gives us (+1):




_[c]_ [1] _[,]_ [3] [1] + ⋯

2 _y_ 1 [2] _,_ 3



1 _,_ 3

_y_ 1 _[X]_ _,_ 3 [1] _[,]_ [3][(][1][ +] _[ y]_ [1] _[,]_ [3][)][−] _[X]_ [1] _[,]_ [3][−] _[X]_ [2] _[,]_ [4] [=] ∫
_y_ 1 [2] _,_ 3



1 _,_ 3

( [1]
_y_ 1 [2] _,_ 3 _y_ 1



_dy_ 1 _,_ 3
1 _y_ [2]



_dy_ 1 _,_ 3
1 _y_ [2]



∞




[1] )

_y_ 1 _,_ 3



_X_ 2 _,_ 4
(1 + [−] _[c]_ [1] _[,]_ [3]




_[c]_ [1] _[,]_ [3] + [(−] _[c]_ [1] _[,]_ [3][)(−] _[c]_ [1] _[,]_ [3][ −] [1][)]

_y_ 1 _,_ 3 2 _y_ [2]



∫



∞



= 1 + ⋯ _._ (4.79)



This (+1) cancels the (−1) remnant from the naive power divergence in the first regions,
leaving us with
A [gluon] 4 → [−] _X_ _[c]_ 1 [1] _,_ _[,]_ 3 [3] _._ (4.80)


54


The cancellation of the “-1” and “1” pieces from the two regions reflects the ba
sic fact used repeatedly in the zeros analysis of [12] that the classic “scale-less integral”

∫0∞ _[dy]_ [/] _[y y][α]_ [ =][ 0.]
The same strategy works in general. It is more convenient to set the _yi_ = _e_ [−] _[t][i]_ and
work in _t_ space, which is divided into cones corresponding to the different degenerations

of the surface/diagrams. In each cone, there is a leading behavior at infinity, that can be

nicely controlled by understanding the “ _g_ -vector fan”, which we can factor out and then

expand around. The resulting functions of the kinematic variables _X_ can then in turn be
expanded about _X_ = 0, keeping the leading low-energy behavior.


**5** **Loop-level** **Gluon** **Amplitudes**


Having just learned how to describe tree-level gluon scattering amplitudes using scalar
scaffolding, we now turn to making our proposal for gluon amplitudes at loop level. At tree
level, we had the luxury of being able to easily compare with the corresponding expressions

in the bosonic string, but at loop-level we will be proceeding more adventurously.

At tree level, we understood that the simple kinematic shift  - which is equivalent
to inserting the magic monomials in _u_ ’s (∏ _ue,e_ /∏ _uo,o_ ), which is equal to the product
of all ∏ _i yi_ in the scaffolding triangulation - is responsible for transmuting the “boring”
amplitudes of Tr _ϕ_ [3] theory into ones that enjoy the gauge invariance, multilinearity and

factorization of gluon amplitudes.

But in fact, as mentioned in our review of surfaceology, this monomial has exactly the

same property for _any_ surface. This motivates an extension of our proposal to any surface

and hence all loop orders/orders in the ’t Hooft expansion.

Our goal in this section is to present this all-loop generalization, discussing a number of
novelties that arise along the way: we will see that the product over curves C must include
open curves with up to one self-intersection per loop, as well as a product over closed

curves ∆with exponents that introduce the dependence on the spacetime dimension, _D_ .

The treatment of self-intersecting curves marks a major difference from the conventional
bosonic string theory. For Tr _ϕ_ [3] theory matching (bosonic) string theory at loop-level from

the curve-integral formalism asks us to consider the product over _all_ curves [14], including

those with arbitrarily high intersection numbers. Meanwhile, if we want a “stringy” integral
that reduces to Tr _ϕ_ [3] at low energies it suffices to only keep non-self-intersecting curves,

which are the only ones dually interpretable as propagators in Feynman diagrams. It is

intriguing that in order to describe gluons we must make the curve integral “slightly more

stringy” by including curves with a finite number of self-intersections, but still distinct from

the infinite number of curves needed to describe the “real bosonic string” in this language.


**5.1** **Loop** **scaffolding** **form**


In the tree-level case, we derived the scaffolding form Ω2 _n_ starting from the bosonic string
2 _n_ gluon amplitude and choosing a kinematic configuration in which the gluons become

effectively scalars - 2 _n_ scalars. Following the same procedure at loop-level is much less

trivial, as bosonic string loop amplitudes are significantly more complicated.


55


Instead, we will follow a different strategy that once more relies on how the tree
level amplitudes are formulated in terms of the surface problem. As we saw in the previous

section, the resulting scaffolding form, in terms of _u_ ’s, was simply that of the bosonic string
Tr _ϕ_ [3] amplitude, times the factor corresponding to the ratio of _u_ ’s, (4.6). In particular,
choosing the scaffolding triangulation, we can simplify this to the bosonic string Tr _ϕ_ [3]

amplitude where instead of a logarithmic form in the _y_ ’s, we have a _dy_ / _y_ [2] form (4.8).
In order to generalize this scaffolding form to the loop level, we consider exactly the

same integrand but instead of being defined on the disk, it is now defined on the punctured

disk. So, at one-loop, for example, we start with (2.26) and replace the integration measure:



A [1-loop] 2 _n_ (1 _,_ 2 _,...,_ 2 _n_ ) = ∫



∞



∏
0 _i_



d _yi_

_yi_ [2] ∏ _C_ _uC_ _[α]_ [′] _[X][C]_ × _C_ [′] ∏∈ s.i. _u_ _[α]_ _C_ [′][′] _[X][C]_ [′] × _u_ [∆] ∆ _[.]_ (5.1)



This is our candidate for the loop surface integral. The version for higher loops is

exactly the same except that at higher loops there are more closed curves, so instead we
have a product over _u_ ∆ _i_ .
As pointed out previously, since there are an infinite number of self-intersecting curves,
this integrand contains an infinite number of terms. In the case of Tr _ϕ_ [3], we can truncate

this infinite product, since all self-intersection curves had no impact on the field-theory

limit: their _u_ variables can never go to zero since they occur in both terms of the _u_

equations, and hence they don’t affect the leading singularities that dominate the field

theory limit. We now want to understand how this generalizes to gluons, _i.e._ what is

the minimal set of curves we need to include in the integrand that gives us gluons at low

energies.

Another feature of gluon loop amplitudes is the dependence on the spacetime dimen
sion, _D_ . If tree amplitudes are written either in terms of dot products of momenta and

polarization vectors, or in our scalar scaffolding language, they are _D_ independent. How
ever, loop amplitudes/integrands are certainly _D_ dependent, mechanically arising from the
trace of the metric _η_ _[µν]_ _ηµν_ = _D_ . However, from (5.1) we do not see any explicit dependence
on _D_, so where is the spacetime dimension dependence coming from?


**5.1.1** ∆


At the outset of our discussion we mentioned that in order to describe gluons at loop level,

we have to consider closed curves that naturally live on the surface. In the planar limit,
these are closed curves surrounding punctures. These are not needed for “stringy” Tr _ϕ_ [3]


integrals, at least if we only want to match the low-energy field theory limit (they are

needed for the full bosonic string amplitude), but together with the self-intersecting curves

we will mention in a moment, they will be important to describe gluons.

By homology closed curves should have zero momentum, but we will give the corresponding _u_ ∆ variables an exponent ∆. We will see that to describe gluons in _D_ spacetime
dimensions at one loop we must take


∆ = 1 − _D._ (5.2)


56


Note again the importance of using the scalar scaffolding picture, which allows our descrip
tion of momentum kinematics to be dimension agnostic, and now allows us to introduce

the dependence on spacetime dimension _D_ as a continuous parameter we can choose at

will.

At general loop level we conjecture that the _D_ -dependence comes in purely through
the choice of the exponents for closed curves in the form ∆ = _n_ ∆ - _D_, where _n_ ∆ is an
integer. All the checks of our proposal from leading singularities we will discuss later are
consistent with _n_ ∆ = 1 just as at 1-loop.


**5.1.2** **Self-Intersecting** **Curves**


As we mentioned previously, in the case of Tr _ϕ_ [3] the contribution from self-intersecting

curves does not affect the low energy limit. For gluons, however, the minimal set of curves

we need includes curves that self-intersect at most once (around each puncture, in case we

are considering a higher loop process). Thus the proposal for the gluon loop integrand is:



_,_ (5.3)



A [m-loop] 2 _n_ (1 _,_ 2 _,...,_ 2 _n_ ) = ∫



∞



∏
0 _i_



d _yi_



d _yi_

_yi_ [2] ∏ _C_ _u_ _[α]_ _C_ [′] _[X][C]_ × _C_ [′] ∈ #∏s.i.=1 _u_ _[α]_ _C_ [′][′] _[X][C]_ [′] × _k_ ∈{1∏ _,...,m_ } _u_ [∆] ∆ _[k]_ _k_




- **���������������������������������������������������������������������������������������** - **���������������������������������������������������������������������������������������** 


Ω [m-loop] 2 _n_


where ∆ _k_ denotes the closed curve going around puncture _k_ .
Before proceeding, let’s highlight the following: at tree-level, the 2 _n_ -scaffolding form

was derived directly from the bosonic string answer, and thus the low energy limit had to

be gluons. For the loop integrand (5.1), this is **not** the case, so there is no guarantee a

priori that we are describing gluons, and in particular that (5.3) is the correct truncation.

One encouraging feature is that the object we get after taking the scaffolding residue

satisfies a notion of gauge-invariance/multi-linearity, just like in the tree-level case. We

will explore this notion in section 5.3.

Another check on this object is to compute the loop-leading singularities and check

that they agree with gluon-leading singularities. Some nontrivial examples of this matching

are presented in 6.3. These computations make manifest how the self-intersecting curves

are important at low energies.

However to prove the full consistency of this formulation what one has to do is show

that starting with (5.3) and going on the cut of the loop propagator, we land on the

tree-level answer (4.8) of the corresponding cut surface. This turns out to be quite non
trivial, but we present the full proof of this matching in section 7. As a byproduct, we will

understand why we need to keep all the curves up to self-intersection one.


**5.2** **Surface** **Kinematics**


Let us now explain how we can read off the _X_ C, _i.e._ the kinematic invariant _X_ associated
to a given curve C on the surface, appearing in the loop surface integral (5.3).
Just like at tree-level, for the non-self-intersecting curves, each curve C is dual to a
propagator entering in the 2 _n_ scalar amplitude, and, in particular, those that starts and


57


**Figure** **24** : On the left, we have the tadpole and external bubble triangulations of the

4-point gluon one-loop surface, where each curve is assigned a different variable _X_, even

when they are the same homology/have the same momentum. The scaffolding curves are

dashed while the gluon internal propagators are solid lines. On the right, we have some

examples of curves and the respective kinematic assignments defined by surface kinematics.


ends on an odd marked point/puncture are dual to gluon propagators (post-scaffolding

residue). Regardless, like we did at tree-level, we can read off the momentum flowing

through the corresponding propagator by _homology_, or equivalently by the left-right rule

presented in 2.

So we could certainly follow this procedure at loop-level as well. Doing so and assuming

the puncture carries no momenta, we would get that different curves on the surface are

assigned the same kinematic invariant _X_ . For example, already at one-loop, there are two
non-self-intersecting going from boundary marked points _i_ and _j_ : _Xi,j_, that goes through
the left of the puncture, and _Xj,i_ going through the right. If we read off the momentum
of these curves by homology we would have _Xi,j_ = _Xj,i_ . In particular, this would force
certain curves to be assigned zero kinematic invariant, such as _Xi_ +1 _,i_ = _Xi,i_ = 0, as well
as _Xj_ +2 _,j_ = 0 for _j_ odd, as these are homologous to the scaffolding curves that are set to
zero after the scaffolding residue. In particular, for _i_ odd, _Xi,i_ and _Xi_ +2 _,i_ are precisely
the curves that are dual to gluon tadpoles and external bubbles propagators, respectively,

which in momentum space are indeed assigned zero momentum (see figure 24, left).

However, the integrand that has all the canonical features of a gluon integrand, _i.e._

that is gauge-invariant and where all the cuts are given in terms of gluing of lower objects,

is naturally defined in terms of an extension of these kinematics - this is what we will call
_surface_ _kinematics_ . Instead of reading the _X_ C’s by homology, we assign a different variable
_X_ C to each _different_ curve on the surface, so in particular, already at one-loop we have
_Xi,j_ ≠ _Xj,i_ . However we assign the same variable to curves that differ by self-intersection,
_X_ C(0) = _X_ C(1) except for the case of the boundary curves _Xi,i_ +1 for which the only existing
curve has self-intersection one (see figure 24, right).

By reading off the kinematics in this way, the _n_ -point gluon one-loop integrand depends
on (2 _n_ ) [2] - 2 _n_ _Xi,j_ ’s [6], and 2 _n_ _Xi,p_ ≡ _Yi_, _i.e._ curves ending on the puncture. As we will


6
We have _Xi,i_ +2 = 0 for _i_ odd from the scaffolding residue, and no _Xa,a_ with _a_ even can appear in the
answer.


58


see momentarily, keeping _all_ these distinct kinematic variables is crucial to allow us to

correctly interpret all the cuts of the integrand, as well as provide a simple generalization

of gauge-invariance satisfied by this object. Let us now proceed to explaining how the

statement of tree-level gauge-invariance that we found earlier nicely generalizes to loop
level for integrands defined in terms of surface kinematics.


**5.3** **Surface** **gauge** **invariance**


It is well known that the notion of gauge invariance for loop integrands is afflicted with

difficulties associated with the presence of the tadpole (as well as massless external bub
ble) propagators. But we have already seen, at tree level, that simple properties of the
_u_ [′] _s_ directly hand us a certain linear expansion of the amplitude in terms of the scaffolding

kinematic variables, that automatically encodes gauge invariance and multilinearity. We

will now see how this extends to loop level, to determine the general form of “gluon am
plitudes” predicted by the binary geometry of the surface. As we will see these will give

a natural home for incorporating tadpoles/massless external bubbles with no ambiguities,

and we will use this to **define** what we mean by gauge invariance and multilinearity. To

avoid this mouthful of a phrase in what follows we will refer to this simply as “surface

gauge invariance”.
To do this let us focus on gluon 1, and look at the scaffolding residue, _y_ 1 _,_ 3 → 0.
Similarly to the tree-level example, the _u_ ’s that depend on _y_ 1 _,_ 3 are: _u_ 1 _,J_, _u_ 2 _,J_, _uJ,_ 1, _uJ,_ 2,
as well as the loop variables, _uY_ 1 and _uY_ 2.
Now for each curve _u_ [(] _[q]_ [)]
2 _,J_ [/] _[u]_ _J,_ [(] _[q]_ 2 [)] [(where q denotes the number of self-intersections, so] _[ q]_ [ =][ 0]
or 1), we have, just like at tree-level:



_∂_ log _u_ [(] 1 _[q]_ _,J_ [)] = − _∂_ log _u_ [(] 2 _[q]_ _,J_ [)] _,_ _∂_ log _u_ [(] _J,_ _[q]_ 1 [)] = − _∂_ log _u_ [(] _J,_ _[q]_ 2 [)] _,_ _∂_ log _uY_ 1
_∂y_ 1 _,_ 3 _∂y_ 1 _,_ 3 _∂y_ 1 _,_ 3 _∂y_ 1 _,_ 3 _∂y_ 1 _,_ 3



_._ (5.4)
_∂y_ 1 _,_ 3



log _uY_ 1

= − _[∂]_ [log] _[ u][Y]_ [2]
_∂y_ 1 _,_ 3 _∂y_ 1 _,_ 3



Note however that when _J_ = 2 _n_, _u_ [(] 2 [0] _n,_ [)] 1 [=] [0,] [as] [this] [in] [this] [case] [it] [is] [just] [a] [boundary]

curve, so the equality above only holds for _u_ [(] 2 [1] _n,_ [)] 2 [and] _[u]_ [(] 2 [1] _n,_ [)] 1 [.] [Bearing] [this] [in] [mind] [we] [get]
that after taking the scaffolding residue in _X_ 1 _,_ 3 we can write our answer as follows:


59


d _ys_



_y_ Res1 _,_ 3=0 [Ω] 2 [loop] _n_ [[] _[X][i,j]_ [] =∑] _J_ ( _X_ 2 _,J_ - _X_ 1 _,J_ ) _s_ ≠(∏1 _,_ 3)



d _ys_ d _yi_ _q_ =0 _,_ 1 2 _,J_

_s_ ≠(∏1 _,_ 3) _ys_ [2] ∏ _i_ _yi_ [2] × _∂y_ 1 _,_ 3 (∏ _km_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ]∣ _y_ 1 _,_ 3=0

- **�����������������������������������������������������������������������������������������������������** **�����������������������������������������������������������������������������������������������������** Q2 _,J_



d _ys_ ∏

_ys_ [2] _i_



d _yi_ × _∂_ log(∏ _q_ =0 _,_ 1 _u_ [(] 2 _[q]_ _,J_ [)][)]

_yi_ [2] _∂y_ 1 _,_ 3



d _yi_



d _ys_ d _yi_ _q_ =0 _,_ 1 _J,_ 2

_s_ ≠(∏1 _,_ 3) _ys_ [2] ∏ _i_ _yi_ [2] × _∂y_ 1 _,_ 3 (∏ _km_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ]∣ _y_ 1 _,_ 3=0

- **�����������������������������������������������������������������������������������������������������** **�����������������������������������������������������������������������������������������������������**
Q _J,_ 2



+ ∑ ( _XJ,_ 2 − _XJ,_ 1) ∏
_J_ _s_ ≠(1 _,_ 3)



d _ys_



_ys_ ∏

_ys_ [2] _i_



d _yi_ × _∂_ log(∏ _q_ =0 _,_ 1 _uJ,_ [(] _[q]_ 2 [)][)]

_yi_ [2] _∂y_ 1 _,_ 3



d _yi_



d _ys_ d _yi_ _[u][Y]_ [2]

_s_ ≠(∏1 _,_ 3) _ys_ [2] ∏ _i_ _yi_ [2] × _[∂]_ [log] _∂y_ 1 _,_ 3 (∏ _km_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ]∣ _y_ 1 _,_ 3=0

- **���������������������������������������������������������������������������������������** **���������������������������������������������������������������������������������������** Q0



+ ( _Y_ 2 − _Y_ 1) ∏
_s_ ≠(1 _,_ 3)



d _ys_



d _ys_ ∏

_ys_ [2] _i_



d _yi_

× _[∂]_ [log][(] _[u][Y]_ [2][)]
_yi_ [2] _∂y_ 1 _,_ 3



d _yi_



d _yi_



_,_



+ _X_ 2 _n,_ 1 × ∏
_s_ ≠(1 _,_ 3)



d _ys_ d _yi_ 2 _n,_ 2

_s_ ≠(∏1 _,_ 3) _ys_ [2] ∏ _i_ _yi_ [2] × _∂y_ 1 _,_ 3 (∏ _km_ ) _u_ _[X]_ _km_ _[k,m]_ [ _y_ ]∣ _y_ 1 _,_ 3=0

- **������������������������������������������������������������������������������������������** **������������������������������������������������������������������������������������������**



d _ys_



d _ys_ ∏

_ys_ [2] _i_



d _yi_ _∂_ log( _u_ 2 [(][0] _n,_ [)] 2 [)]

×
_yi_ [2] _∂y_ 1 _,_ 3



Q [(] 2 [0] _n,_ [)] 2

(5.5)
where _J_ ∈{1 _,_ 3 _,_ 4 _,_ ⋯ _,_ 2 _n_ }. Note that there is the correction term in the last line proportional
to _X_ 2 _n,_ 1 precisely because of the reason mentioned above.
Now just like at tree-level, we have the Q2 _,J_ = _∂X_ 2 _,J_ I _n_, Q _J,_ 2 = _∂XJ,_ 2I _n_ and Q0 = _∂Y_ 2I _n_,
where I _n_ stands for the object we get after taking the scaffolding residue, which at low
energies gives us the gluon loop-integrand. Similarly we would like to be able to express

the correction term, in terms of some operation on the integrand. To do this we start by
observing that taking a derivative on (5.5) with respect to _X_ 2 _n,_ 1 and observe that we can
isolate Q2 [(][0] _n,_ [)] 2 [by] [evaluating] [the] [result] [at] _[X]_ [2] _[,J]_ [→] _[X]_ [1] _[,J]_ [,] _[X][J,]_ [2][ →] _[X][J,]_ [1] [and] _[Y]_ [2][ →] _[Y]_ [1][:]



_∂_ Res _y_ 1 _,_ 3=0 Ω [loop] 2 _n_ [[] _[X][i,j]_ []]
∣ =[∑ ( _X_ 2 _,J_                - _X_ 1 _,J_ ) _[∂]_ [Q][2] _[,J]_
_∂X_ 2 _n,_ 1 2→1 _J_ _∂X_ 2 _n,_



_∂X_ 2 _n,_ 1



+( _Y_ 2 − _Y_ 1) _[∂]_ [Q][0]




_[∂]_ [Q][2] _[,J]_ + ∑ ( _XJ,_ 2 − _XJ,_ 1) _[∂]_ [Q] _[J,]_ [2]

_∂X_ 2 _n,_ 1 _J_ _∂X_ 2 _n,_ 1




[0]
+( _Y_ 2 − _Y_ 1) _[∂]_ + Q [(] 2 [0] _n,_ [)] 2 [−Q][2] _[n,]_ [2][]∣]

_∂X_ 2 _n,_ 1 2→1
= −Q2 [(][1] _n,_ [)] 2 [∣][2][→][1][ = −Q] 2 [(][1] _n,_ [)] 2 _[,]_



(5.6)



where we used Q2 _n,_ 2 = Q [(] 2 [1] _n,_ [)] 2 [+ Q] 2 [(][0] _n,_ [)] 2 [as] [well] [as] [that] [the] [Q][’s] [are] [independent] [of] _[X]_ [2] _[,J]_ _[,X][J,]_ [2]
and _Y_ 2. Therefore we have that:

_∂_ I _n_ _∂_ I _n_
Q [(] 2 [0] _n,_ [)] 2 [= Q][2] _[n,]_ [2][ −Q] 2 [(][1] _n,_ [)] 2 [=] + ∣ _._ (5.7)
_∂X_ 2 _n,_ 2 _∂X_ 2 _n,_ 1 2→1


In summary, the full gauge-invariance as well as multi-linearity of the integrand in

gluon one can be written as follows:


60


I _n_ = ∑ [( _X_ 2 _,j_ - _X_ 1 _,j_ ) _[∂]_ [I] _[n]_
_j_ ≠2 _∂X_ 2 _,j_




_[∂]_ [I] _[n]_ + ( _Xj,_ 2 − _Xj,_ 1) _[∂]_ [I] _[n]_

_∂X_ 2 _,j_ _∂Xj,_

_[∂]_ [I] _[n]_ + ( _Xj,_ 2 − _Xj,_ 3) _[∂]_ [I] _[n]_

_∂X_ 2 _,j_ _∂Xj,_




_[∂]_ [I] _[n]_ ] + _X_ 2 _n,_ 1 × [ _[∂]_ [I] _[n]_

_∂Xj,_ 2 _∂X_ 2




_[∂]_ [I] _[n]_ + _[∂]_ [I] _[n]_

_∂X_ 2 _,_ 4 _∂X_ 3 _,_



_∂_ I _n_

_[∂]_ [I] _[n]_ + ∣ ]

_∂X_ 2 _n,_ 2 _∂X_ 2 _n,_ 1 2→1



(5.8)

_[∂]_ [I] _[n]_ ∣ ] _._

_∂X_ 3 _,_ 4 2→3



= ∑ [( _X_ 2 _,j_ - _X_ 3 _,j_ ) _[∂]_ [I] _[n]_
_j_ ≠2 _∂X_ 2 _,j_




_[∂]_ [I] _[n]_ ] + _X_ 3 _,_ 4 × [ _[∂]_ [I] _[n]_

_∂Xj,_ 2 _∂X_ 2 _,_



where once again the same statement goes through for _X_ 2 _,J_ _,X_ 3 _,J_, just like at tree-level.


**5.4** **Examples:** **one-loop** 1 **-** **and** 2 **-gluon** **integrands**


In this section, we present simplest examples at one loop, namely 1-gluon and 2-gluon

integrands, which are obtained from scaffolding residues of (5.3) in the low energy limit

with 2 and 4 scalars, respectively. We will see explicitly how the surface kinematics and

surface gauge invariance work in these simple examples.


**5.4.1** 1 **-gluon** **integrand**


Let us begin with the 1-point integrand, and we choose the underlying triangulation to be
the tadpole triangulation for the gluon problem, _i.e._ { _X_ 1 _,_ 1 _,Y_ 1}, where _X_ 1 _,_ 1 is the scaffolding
chord and _Y_ 1 is the loop propagator of the gluon amplitude. Keeping only curves with selfintersection at most one as prescribed, we get that the stringy gluon integrand is:



_y_ 1 ⎛ 1

_y_ 1 [2] Res _y_ 1 _,_ 1=0 ⎝ _y_ 1 [2] _,_ 1 _i_ ∏=1 _,_ 2 _u_ _[X]_ _i,i_ _[i,i][u]_ _Y_ _[Y][i]_ _i_ [×] _[ u]_ ∆ [∆] ( _u_ [(] 1 [1] _,_ 2 [)][)] _[X]_ [1] _[,]_ [2][(] _[u]_ [(] 2 [1] _,_ 1 [)][)] _[X]_ [2] _[,]_ [1] _i_ [∏] =1 _,_ 2( _u_ [(] _i,i_ [1][)][)] _[X][i,i]_ [⎞] ⎠ _[,]_



d _y_ 1
0 _y_ [2]



A [gluon] 1 = ∫



∞



(5.9)

where we have used the algorithm of section 2.5 to obtain _u_ variables in this triangulation

as follows,



1 + _y_ 1 _,_ 1 + _y_ 1 _y_ 1 _,_ 1

_[y]_ [1] _[,]_ [1][(][1][ +] _[ y]_ [1][ +] _[ y]_ [1] _[y]_ [1] _[,]_ [1][)] _,_ _u_ 2 _,_ 2 = _,_

1 ~~+~~ _y_ 1 ~~+~~ _y_ 1 _,_ 1 ~~+~~ _y_ 1 _y_ 1 _,_ 1 1 ~~+~~ _y_ 1 _,_ 1 ~~+~~ _y_ 1 _y_ 1 _,_ 1 ~~+~~ _y_ 1 _y_ 1 [2] _,_ 1



_u_ 1 _,_ 1 = _[y]_ [1] _[,]_ [1][(][1][ +] _[ y]_ [1][ +] _[ y]_ [1] _[y]_ [1] _[,]_ [1][)]




[1][ (] _[y]_ [1] _[,]_ [1][ +][ 1][)]

_y_ 1 _y_ 1 _,_ 1 ~~+~~ 1 _[,]_ _uY_ 2 = _[y]_ _y_ [1] _[y]_ 1 _,_ [1] 1 _[,]_ [1] ~~+~~ [ +] 1 [ 1]



_uY_ 1 = _[y]_ [1][ (] _[y]_ [1] _[,]_ [1][ +][ 1][)]




[1] _[y]_ [1] _[,]_ [1] [ 1]

_u_ ∆ = 1 − _y_ 1 _,_
_y_ 1 _,_ 1 ~~+~~ 1 _[,]_



( _y_ 1 + 1)( _y_ 1 _,_ 1 + 1)( _y_ 1 _y_ 1 _,_ 1 + 1) ( _y_ 1 + 1)( _y_ 1 _,_ 1 + 1)( _y_ 1 _y_ 1 _,_ 1 + 1)
_u_ [(] 1 [1] _,_ 2 [)] [=] 2 _,_ 1 [=]
~~((~~ _y_ 1 ~~+~~ 1 ~~)~~ _y_ 1 _,_ 1 ~~+~~ 1 ~~)(~~ _y_ 1 ~~(~~ _y_ 1 _,_ 1 ~~+~~ 1 ~~) +~~ 1 ~~)~~ _[,u]_ [(][1][)] ~~((~~ _y_ 1 ~~+~~ 1 ~~)~~ _y_ 1 _,_ 1 ~~+~~ 1 ~~)(~~ _y_ 1 ~~(~~ _y_ 1 _,_ 1 ~~+~~ 1 ~~) +~~ 1 ~~)~~ _[,]_



(5.10)
where in the low-energy limit those _u_ [(] _i,i_ [1][)] [do] [not] [contribute] [to] [the] [gluon] [integrand,] [so] [we]
do not list them here. Then, we take the scaffolding residue on _y_ 1 _,_ 1 = 0 and set _X_ 1 _,_ 1 = 0 as
we have discussed in section 4.2.2, which gives the nice result:



d _y_ 1
0 _y_ [2]



A [gluon] 1 = ∫



∞



_y_ 1 [2]



⎛ [(][1][ −] _[y]_ [1][)][ ∆] _[y]_ 1 _[α]_ [′] _[Y]_ [1] ( _y_ 1 ( _X_ 1 _,_ 2 + _X_ 2 _,_ 1) + ( _y_ 1 − 1)( _y_ 1 + 1)( _Y_ 1 − _Y_ 2)) ⎞
⎝ [−] _[α]_ [′] _y_ 1 ~~+~~ 1 ⎠ _[.]_



(5.11)
We can now directly integrate over _y_ 1 and obtain the “stringy” integrand, but all we
need is the low-energy limit. It is straightforward to take _α_ [′] → 0 and obtain

A [gluon] 1 = − _[X]_ [1] _[,]_ [2][ +] _[ X]_ [2] _[,]_ [1][ + (] _Y_ [∆] 1 [+][ 1][)(] _[Y]_ [1][ −] _[Y]_ [2][)] _,_ (5.12)


which as expected involves the 1-point tadpole graph only.


61


**5.4.2** 2 **-gluon** **integrand**


Next we present the result for one-loop 2-gluon integrand, and we obtain it by starting

with a 4-scalar process described by (5.3), taking the scaffolding residue, reducing us to

the 2-point 1-loop stringy gluon integrand from which we ultimately extract the low-energy

limit to obtain the field theory integrand.

We choose the underlying triangulation to be the bubble triangulation for the gluon
problem, _i.e._ { _X_ 1 _,_ 3 _,X_ 3 _,_ 1 _,Y_ 1 _,Y_ 3}, where _X_ 1 _,_ 3 and _X_ 3 _,_ 1 are the scaffolding chords and _Y_ 1 _,Y_ 3
are the loop propagators of the gluon amplitude. Keeping only curves with self-intersection

at most one as prescribed, we get that the stringy gluon integrand is:



_y_ 1 d _y_ 3 ⎛ 1

_y_ 1 [2] _[y]_ 3 [2] Res _y_ 1 _,_ 3= _y_ 3 _,_ 1=0 ⎝ _y_ 1 [2] _,_ 3 _[y]_ 3 [2] _,_ 1 _u_ _[X]_ 2 _,_ 4 [2] _[,]_ [4] _[u][X]_ 4 _,_ 2 [4] _[,]_ [2] _i_ =1∏ _,...,_ 4 _u_ _[X]_ _i,i_ _[i,i][u]_ _i,i_ _[X][i,i]_ −1 [−][1] _[u]_ _Y_ _[Y][i]_ _i_ [×] _[ u]_ ∆ [∆]



A [gluon] 2 = ∫ d _y_ 1 d _y_ 3

[2] [2]



( _u_ [(] 2 [1] _,_ 4 [)][)] _[X]_ [2] _[,]_ [4][(] _[u]_ 4 [(][1] _,_ 2 [)][)] _[X]_ [4] _[,]_ [2] _i_ =1∏ _,...,_ 4( _u_ [(] _i,i_ [1][)][)] _[X][i,i]_ [(] _[u]_ _i,i_ [(][1][)] −1 [)] _[X][i,i]_ [−][1][(] _[u]_ _i_ [(] - [1] 1 [)] _,i_ [)] _[X][i]_ [−][1] _[,i]_ [⎞] ⎠ _[,]_



(5.13)



where we have set _X_ 1 _,_ 3 = _X_ 3 _,_ 1 = 0. Now since we picked the triangulation corresponding
to the bubble diagram for the gluon problem, containing chords { _Y_ 1 _,Y_ 3}, the singularity
corresponding to this diagram is located near _y_ 1 _,y_ 3 → 0. There are two other diagrams,
corresponding to the tadpole diagrams with chords, { _Y_ 1 _,X_ 1 _,_ 1} and { _Y_ 3 _,X_ 3 _,_ 3}, whose singularities are located in different boundaries of the integration domain. To extract the

field theory limit of (5.13), we proceed as outlined in section 4.8, fully explained in [34],

and extract the contribution to the integrand from each of these 3 regions. Summing them

gives the full low-energy integrand:



A [gluon] 2 = − _[X]_ [1] _[,]_ [2] _[X]_ [1] _[,]_ [4][ +] _[ X]_ [2] _[,]_ [1] _[X]_ [4] _[,]_ [1][ −(][∆] [+][ 1][)(] _[X]_ [2] _[,]_ [1] _[X]_ [1] _[,]_ [4][ −] _[Y]_ [2] _[X]_ [1] _[,]_ [4][ −] _[Y]_ [4] _[X]_ [2] _[,]_ [1][ +] _[ Y]_ [3][ (] _[X]_ [1] _[,]_ [4][ +] _[ X]_ [2] _[,]_ [1][ −] _[X]_ [2] _[,]_ [4][))]



_Y_ 1 _X_ 1 _,_ 1



+ _[X]_ [1] _[,]_ [2][ −] _[X]_ [2] _[,]_ [1][ +] _[ X]_ [4] _[,]_ [1][ −] _[X]_ [1] _[,]_ [4][ +][ 2] _[X]_ [2] _[,]_ [4][ −] _[X]_ [4] _[,]_ [2][ −(][∆] [+][ 1][)(] _[Y]_ [2][ −] _[Y]_ [3][ +] _[ Y]_ [4][ −] _[X]_ [2] _[,]_ [4][)]



_X_ 1 _,_ 1




_[X]_ [4] _[,]_ [2] [∆] [ 1] _[Y]_ [2] _[Y]_ [3] _[ Y]_ [4] _[X]_ [2] _[,]_ [4]

+ _[X]_ [2] _[,]_ [4]
_Y_ 1 _X_ 1 _,_ 1



+ _[Y]_ [2][ (] _[X]_ [1] _[,]_ [4][ −] _[X]_ [4] _[,]_ [1][ +] _[ X]_ [4] _[,]_ [3][ −] _[X]_ [3] _[,]_ [4][) +] _[ X]_ [1] _[,]_ [1][ (] _[X]_ [3] _[,]_ [2][ −] _[X]_ [4] _[,]_ [2][ +] _[ X]_ [4] _[,]_ [3][)]




[3] _[,]_ [4] _[ X]_ [1] _[,]_ [1] _[X]_ [3] _[,]_ [2] _[X]_ [4] _[,]_ [2] _[ X]_ [4] _[,]_ [3]

+ ( _i_ → _i_ + 2)
_Y_ 1 _Y_ 3




- _[X]_ [1] _[,]_ [4] _[X]_ [3] _[,]_ [2][ +] _[ X]_ [2] _[,]_ [1] _[X]_ [4] _[,]_ [3][ +] _[ X]_ [1] _[,]_ [1] _[X]_ [3] _[,]_ [3][ −(][∆] [+][ 1][)] _[Y]_ [2] _[Y]_ [4]




_[ X]_ [1] _[,]_ [1] _[X]_ [3] _[,]_ [3] [∆] [ 1] _[Y]_ [2] _[Y]_ [4]

+ (∆ + 1) _,_
_Y_ 1 _Y_ 3



(5.14)
where ( _i_ → _i_ + 2) denotes the cyclic permutation {1 _,_ 2 _,_ 3 _,_ 4} →{3 _,_ 4 _,_ 1 _,_ 2} for all preceding
terms, and the terms on the last line are manifestly invariant under ( _i_ → _i_ +2). This same
integrand can be obtained from a recursion relation we present in [17], which leverages our

understanding of the loop-cuts as well as good behvaior at infinity under a uniform shift

of the loop-variables.

We can as usual translate from our scalar description of the kinematics to standard

presentations depending on dot products of momenta and polarization vectors if we like.
The polarization vectors are still given by (3.21); we can make the gauge choice _α_ = 1 so
that
_ϵ_ _[µ]_ _i_ [∝−(] _[X]_ [2] _[i]_ [ −] _[X]_ [2] _[i]_ [−][1][)] _[µ][.]_ (5.15)


62


In addition, we have the freedom to choose the loop momentum so that _Y_ 1 = _l_ [2] . Then
the _X,Y_ variables are expressed in terms of the usual Lorentz invariants as

_Y_ 1 = _l_ [2] _,_ _Y_ 2 = _Y_ 1 − 2 _ϵ_ 1 ⋅ _l,_ _Y_ 3 = _l_ [2] + 2 _q_ 1 ⋅ _l,_ _Y_ 4 = _Y_ 3 − 2 _ϵ_ 2 ⋅ _l,_ _X_ 2 _,_ 4 = −2 _ϵ_ 1 ⋅ _ϵ_ 2 _._ (5.16)

Note that we do _not_ put _X_ 1 _,_ 1 _,X_ 3 _,_ 3 = 0 at the level of the integrand; we will make
further comments on this point in a moment. We obviously have similar expressions for

higher points and loops, once we specify some choice for polarizations and loop momenta.

Of course, the integrated result is independent of such choices, and post-integration we are

also free to put tadpoles to zero.


**5.4.3** **Gauge** **Invariance** **check**


In the previous section, we explained how this surface definition of the integrand gives us

a generalized notion of gauge invariance for the loop integrand. Now that we have derived

an explicit example of 1- and 2-gluon integrands, we can check that the form predicted in

(5.5) holds in these cases.

For (5.12), it is easy to check the surface gauge invariance (in gluon 1):

A [gluon] 1 = ( _X_ 2 _,_ 1)Q _X_ 2 _,_ 1 + ( _Y_ 2 − _Y_ 1)Q _Y_ 2 + ( _X_ 1 _,_ 2)Q _X_ 1 _,_ 2 _,_ (5.17)


1
where Q _X_ ∶= _[∂]_ [A] _∂X_ [gluon], and they read,



_Y_ [1] 1 _,_ Q _Y_ 2 = − [(][∆] _Y_ [+] 1 [ 1][)]



Q _X_ 2 _,_ 1 = Q _X_ 1 _,_ 2 = − [1]



_._ (5.18)
_Y_ 1



Similarly, we can write the 2-gluon integrand (5.14) in the form as prescribed in (5.5):

A [gluon] 2 = ∑ ( _X_ 2 _,j_ - _X_ 1 _,j_ )Q _X_ 2 _,j_ + ∑ ( _Xj,_ 2 − _Xj,_ 1)Q _Xj,_ 2 + _X_ 4 _,_ 2Q _X_ 4 _,_ 2 + _X_ 4 _,_ 1Q [′] _X_ 4 _,_ 1 _[,]_ [(5.19)]
_j_ =1 _,_ 3 _,_ 4 _,p_ _j_ =1 _,_ 3



2 2
where Q _X_ ∶= _[∂]_ [A] _∂X_ [gluon] except for the last boundary term Q [′] _X_ 4 _,_ 1 [∶=] _[∂]_ _∂X_ [A][gluon] 4 _,_ 1 [∣][2][→][1][,] [and] [they] [read]



Q _X_ 2 _,_ 1 = _[X]_ [3] _[,]_ [3][ −] _[X]_ [4] _[,]_ [3][ +] _[ Y]_ [4]




[1] + ( _D_  - 2) _[X]_ [1] _[,]_ [4][ +] _[ Y]_ [3][ −] _[Y]_ [4]

_Y_ 1 _Y_ 1 _X_ 1 _,_ 1




_[X]_ [4] _[,]_ [3] _[ Y]_ [4]  - _X_ 4 _,_ 1  - [1]

_Y_ 1 _Y_ 3 _Y_ 1 _X_ 1 _,_ 1 _Y_



_,_
_Y_ 1 _X_ 1 _,_ 1



Q _X_ 1 _,_ 2 = − _Y_ _[X]_ 1 _X_ [1] _[,]_ 1 [4]

Q _X_ 2 _,_ 3 = − _[X]_ [4] _[,]_ [3]



_Y_ 4

_[X]_ [1] _[,]_ [4]  - + [1]

_Y_ 1 _X_ 1 _,_ 1 _Y_ 1 _Y_ 3 _Y_

_Y_ 4

_[X]_ [4] _[,]_ [3]  - + [1]

_Y_ 3 _X_ 3 _,_ 3 _Y_ 1 _Y_ 3 _Y_



_,_
_Y_ 1




[1] + ( _D_  - 2) _[X]_ [4] _[,]_ [3][ +] _[ Y]_ [1][ −] _[Y]_ [4]

_Y_ 3 _Y_ 3 _X_ 3 _,_ 3



Q _X_ 3 _,_ 2 = _[X]_ [1] _[,]_ [1][ −] _Y_ _[X]_ 1 _Y_ [1] 3 _[,]_ [4][ +] _[ Y]_ [4]

Q _X_ 2 _,_ 4 = − _[X]_ [3] _[,]_ [3][ +] _Y_ _[ Y]_ 1 _Y_ [1] 3 [ −] [2] _[Y]_ [3]

Q _X_ 4 _,_ 2 = [−] _[X]_ [1] _[,]_ [1][ +][ 2] _[Y]_ [1][ −] _[Y]_ [3]



_,_
_Y_ 3




_[X]_ [1] _[,]_ [4] _[ Y]_ [4]  - _X_ 3 _,_ 4  - [1]

_Y_ 1 _Y_ 3 _Y_ 3 _X_ 3 _,_ 3 _Y_



(5.20)




_[ Y]_ [1][ −] [2] _[Y]_ [3]

+ ( _D_      - 2) [−] _[X]_ [1] _[,]_ [1][ +] _[ Y]_ [1][ −] _[Y]_ [3]
_Y_ 1 _Y_ 3 _Y_ 1 _X_ 1 _,_ 1



_,_
_Y_ 3 _X_ 3 _,_ 3



_,_
_Y_ 1 _X_ 1 _,_ 1




[ +][ 2] _[Y]_ [1][ −] _[Y]_ [3]

+ ( _D_       - 2) [−] _[X]_ [3] _[,]_ [3][ −] _[Y]_ [1][ +] _[ Y]_ [3]
_Y_ 1 _Y_ 3 _Y_ 3 _X_ 3 _,_ 3



Q _Y_ 2 = _[X]_ [1] _[,]_ [4][ −] _[X]_ [4] _[,]_ [1][ +] _[ X]_ [4] _[,]_ [3][ −] _[X]_ [3] _[,]_ [4]



_,_
_Y_ 3 _X_ 3 _,_ 3



_X_ 4 _,_ 3 _Y_ 4

_[X]_ [1] _[,]_ [4]  -  - + [1]

_Y_ 1 _X_ 1 _,_ 1 _Y_ 3 _X_ 3 _,_ 3 _Y_ 1 _Y_ 3 _Y_




[1] _[ X]_ [4] _[,]_ [3] _[X]_ [3] _[,]_ [4]

+ ( _D_         - 2)(− _[X]_ [1] _[,]_ [4]
_Y_ 1 _Y_ 3 _Y_ 1 _X_ 1




[1] + [1]

_Y_ 1 _Y_




[1] ) _,_

_Y_ 3



Q [′] _X_ 4 _,_ 1 [= −] [1] _._

_Y_ 3



63


**5.5** **A** **well-defined** **Yang-Mills** **integrand**


It is interesting to compare the integrand we have obtained in this way with the conventional

Yang-Mill bubble integrand. Here we run into the familiar difficulty that we do not have

a well-defined conventional Yang-Mills integrand, precisely due to the existence of the

tadpole/massless external bubble terms and the infamous “1/0” problem associated with

them, as well as massless external bubbles. We are usually instructed to throw out the

tadpoles/massless external bubbles, on the grounds that they are “scale-less integrals that

integrate to zero”, but clearly something nice about the integrand must be lost in doing

so, and indeed it now fails to be gauge invariant.

By contrast, the bubble integrand we have just produced is perfectly well defined. We
encounter the familiar 1/0 difficulties if we were to set the tadpole _X_ 1 _,_ 1 → 0, but nothing
forces us to do this, and at finite _X_ 1 _,_ 1 we have an object that is both well-defined and is
consistent with its own internal-to-the-world-of-surfaces notion of gauge invariance. If we
were to set _X_ 1 _,_ 1 → 0, we can only get singularities in terms with 1/ _X_ 1 _,_ 1 poles. These are
of course precisely tadpole factorizations, and therefore must obviously multiply scale-less

integrals that integrate to zero. So, we get to have our integrand cake and eat our amplitude

too: we have a well-defined integrand at finite values of tadpole/massless external bubble

variables, when these are set to zero as naively needed to match normal kinematics we

do encounter divergences which are however guaranteed to be proportional to objects that

integrate to zero.

We can also check that our integrand has the correct cuts to match field theory gluing.

The most straightforward check is the usual unitarity double-cut. But it also has the correct
single-cuts, which again needs a proper discussion of _X_ 1 _,_ 1 ≠ 0 for the “forward limit” term.
We will discuss at length in our discussion of the loop-cut/forward limit connection, even
at finite _α_ [′], in the penultimate section of this paper.

The elementary mechanism by which tadpoles/massless external bubbles are naturally

dealt with suggests a recursive procedure for computing integrands for Yang-Mills theory

[17] in any number of dimensions, in the planar limit where integrands are well-defined.

We have computed integrands determined by this recursion through a number of one- and

two-loop examples, which have passed all obvious consistency checks [17]. Optimistically

an all-loop recursion for non-supersymmetric Yang-Mills theory in the planar limit may be
at hand, as a counterpart to the very different recursion for planar N = 4 SYM [38].


**6** **Leading** **Singularities**


We have given an integral representation for scalar-scaffolded gluon scattering amplitudes.

In principle, with a correct contour prescription for integrating over the _y_ variables, we
have a “curve integral” representation for these amplitudes. Just as for Tr _ϕ_ [3] theory, at

loop level we can also integrate over the loop momenta as Gaussian integrals, to represent

the integrated amplitudes as an integral over _y_ space. We can also attempt to understand

the field theory limit directly, which as we have indicated a number of times, is more
interesting than the trivial tropicalization seen in Tr _ϕ_ [3] theory, due to the non-logarithmic
character of the _dy_ / _y_ [2] measure.


64


We will take up both these lines of investigation in future works, defining the contour

for the amplitude [27] as well as understanding a number of aspects of the field theory

limit [34]. In this section we will instead content ourselves with performing the most basic

but fundamental check that we are correctly describing gluon amplitudes at multi-loop

level: we will show that our curve integral form correctly produces the leading singularities

of gluon amplitudes in a number of non-trivial examples, from trees through to two loops.

Unlike the computation of the full amplitude/integrand, which needs care in defining

the contour in _y_ space, computing leading singularities is much simpler. We are interested

in computing a leading singularity corresponding to gluing together three-particle ampli
tudes according to any particular trivalent diagram. Now, if we choose the underlying

triangulation of the surface to be dual to the diagram of the leading singularity, it is easy
to see that the residue on the pole setting all the _X_ → 0 for the glued internal lines, is
computed simply by setting all these _X_ ’s to zero in the _y_ integrand and simply computing
the **residue** of the integrand around all the _y_ → 0. Since the form is a _dy_ / _y_ [2] form, this
residue ultimately gives us simply the part of the expansion of the product of the _u_ _[X]_ _X_ [for]
small _y_, that is linear in all the _y_ ’s, and so we need the expansion of each _uX_ around _y_ → 0
up to first order in all the _yi_ .
Note that leading singularities for the Tr _ϕ_ [3] theory are completely trivial–they are all
equal to 1, since all we are doing in that case is taking residues of the _dy_ / _y_ form at _y_ = 0
which sets the remaining _u_ → 1. This reflects the obvious fact that the Tr _ϕ_ [3] theory has only
poles and no numerators. The leading singularities are (essentially by definition!) a clean

probe of the “purely numerator” part of gluon amplitudes, and we see directly that this is
associated with the _dy_ / _y_ [2] form. This already also alerts us to the possibility that curves
with small self-intersection numbers can be important. Even though their _u_ ’s can never go

to zero, expanding around 1 they can have terms first-order in _y_ . It is intuitive that curves

with higher self-intersection will begin with higher powers of _y_ and so up to linear order we

will only need curves with low self-intersection number. Indeed in a moment we will prove

that curves with two or more self-intersections around a given puncture begin at quadratic

order or higher in some _y_ variable and hence never contribute to leading singularities. But

we also see that curves with up to one self-intersection around each loop puncture will

indeed be needed to correctly match leading singularities.


**6.1** **Linearized** _u_ **’s**


The computation of leading singularities needs an expansion for the _u_ ’s up to first order in
the _y_ ’s. Quite beautifully, there is a direct expression for _uX_ to first order in the _y_ ’s that we
can simply read off by looking at the pattern of intersections of the curve _X_ and the base

triangulation of the surface, which will greatly simplify our analysis. We are borrowing here

from [18] where this and more general results will be explained and derived. Let us start

by picking the underlying triangulation, corresponding to the leading singularity we are
interested in. Now consider some curve, _Xa,b_, not in the triangulation, and its respective
_u_ variable, _uXa,b_ (see figure 25).
Let’s denote by I _a,b_ the set of curves in the triangulation that _Xa,b_ intersects. Next,
we look at each marked point _a_ and _b_, and check whether there are triangulation chords


65


**Figure** **25** : Linearized _u_ ’s.


ending on these points. Let us say that this is the case for point _a_, and list these chords
together with chord _Xa,b_ and twist them clockwise to obtain the respective laminations.
Then let us list all these chords in clockwise order: { _Xp_ 1 _,...,Xa,b,Xp_ [⋆] _,...,Xpk_ } (see figure
25). We do the same for vertex _b_ and we get a set { _Xq_ 1 _,...,Xa,b,Xq_ [⋆] _,...,Xql_ }. Then the
linearized _ua,b_ is:



_u_ _[X]_ _a,b_ _[a,b]_ = 1 − _Xa,b_ ∏ _yC_ [Int][[{C] _[,X][a,b]_ [}]] −∏ _yC_ [Int][[{C] _[,X][a,b]_ [}]] ( _yp_ [⋆] + _yp_ [⋆] _yp_ [⋆] +1 [+ ⋅⋅⋅+] _[ y][p]_ [⋆] _[y][p]_ + [⋆] 1 _[...y][p][k]_ [)]
⎡⎢⎢⎢⎢⎣C∈I _a,b_ C∈I _a,b_



−∏ _yC_ [Int][[{C] _[,X][a,b]_ [}]] ( _yq_ [⋆] + _yq_ [⋆] _yq_ + [⋆] 1 [+ ⋅⋅⋅+] _[ y][q]_ [⋆] _[y][q]_ + [⋆] 1 _[...y][q][l]_ [)]
C∈I _a,b_



+ ∏ _yC_ [Int][[{C] _[,X][a,b]_ [}]] ( _yp_ [⋆] + _yp_ [⋆] _yp_ [⋆] +1 [+ ⋅⋅⋅+] _[ y][p]_ [⋆] _[y][p]_ + [⋆] 1 _[...y][p][k]_ [)(] _[y][q]_ [⋆] [+] _[ y][q]_ [⋆] _[y][q]_ + [⋆] 1 [+ ⋅⋅⋅+] _[ y][q]_ [⋆] _[y][q]_ + [⋆] 1 _[...y][q][l]_ [)]
C∈I _a,b_ ⎤⎥⎥⎥⎥⎦
+ O [2] ( _y_ ) _._
(6.1)

This makes manifest that any curve that intersects one of the triangulation chords

more than once will **not** contribute to the leading singularity, as it will be automatically

quadratic in that _y_ . Thus as alluded to above, any curve that self-intersects twice or more

going around any loop puncture will not contribute to leading singularities. But curves

with up to one self-intersection per puncture can (and will) be relevant.

Let us now give a specific example for the case of a loop-level amplitude. We consider

a 3-point 1-loop gluon amplitude, which is a 6-point 1-loop scalar amplitude. We are inter
ested in the leading singularity in which one of the legs has a bubble (see figure 26), which
corresponds to the triangulation of the punctured disk with chords { _X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,X_ 5 _,_ 1 _,Y_ 1 _,Y_ 5}.
Kinematically, _X_ 1 _,_ 5 = _X_ 5 _,_ 1 but they are different curves on the surface, as we can see in
figure 26. We want to find the linearized expression of _uY_ 3 in terms of { _y_ 1 _,_ 3 _,y_ 3 _,_ 5 _,y_ 5 _,_ 1 _,y_ 1 _,y_ 5}.
As a chord, _Y_ 3 only intersects _X_ 1 _,_ 5. However, as a lamination, on the side of marked point
3, it intersects _X_ 3 _,_ 5; while on the puncture end, it intersects first _Y_ 1 and then _Y_ 5. Strictly
speaking, as a lamination, _Y_ 3 intersects _Y_ 1 and _Y_ 5 an infinite number of times, but since we



66


**Figure** **26** : Bubble triangulation and curve for linearized _uY_ 3.


are only interested in the expansion up to linear order, we can truncate it at intersection
1. This means that the linearized _uY_ 3 is simply:

( _uY_ 3) _[Y]_ [3] = 1 − _Y_ 3 [ _y_ 1 _,_ 5 − _y_ 1 _,_ 5 _y_ 3 _,_ 5 − _y_ 1 _,_ 5 ( _y_ 1 + _y_ 1 _y_ 5) + _y_ 1 _,_ 5 _y_ 3 _,_ 5 ( _y_ 1 + _y_ 1 _y_ 5)] _._ (6.2)


**6.2** **Tree** **level**


Let us study tree-level leading singularities in detail. It suffices to present explicit examples

for 3- and 4-point cases, and the general rules for computing any tree-level leading singularities will become clear. The _n_ = 3 case is trivial in that after scaffolding no more residues
are needed thus the only leading singularity corresponds to the amplitudes obtained in 3.5.

However, we still go through it to illustrate how the same result can be obtained from the
linearized _u_ ’s discussed above. Recall that we simply take 2 _n_ = 6 integral and take scaffolding residues in { _X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,X_ 1 _,_ 5} which already forms a triangulation. The linearized
_u_ ’s we need are simply
_u_ _[X]_ 1 _,_ 4 [1] _[,]_ [4] = 1 − _X_ 1 _,_ 4( _y_ 3 _,_ 5 − _y_ 1 _,_ 3 _y_ 3 _,_ 5) _,_ (6.3)

_u_ _[X]_ 2 _,_ 4 [2] _[,]_ [4] = 1 − _X_ 2 _,_ 4 _y_ 1 _,_ 3 _y_ 3 _,_ 5 _,_ (6.4)


and their cyclic images _u_ 2 _,_ 5 _,u_ 3 _,_ 6, and _u_ 4 _,_ 6 _,u_ 2 _,_ 6 respectively. Note that for our purpose we
have sent _X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,X_ 1 _,_ 5 → 0 in these expressions. From here it is easy to read off the
terms that are linear in all _y_ ’s at the leading _α_ [′] order, which gives the 3-point Yang-Mills

amplitude or leading singularity:


_X_ 1 _,_ 4 _X_ 2 _,_ 6 − _X_ 1 _,_ 4 _X_ 2 _,_ 5 + cyclic _,_ (6.5)


and of course in agreement with (3.27). In addition, there is one more term that contributes
to the next order in _α_ [′], - _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 6, which is exactly the _F_ [3] amplitude or leading
singularity.

Moving on to 4 points and we consider the “ _s_ -channel” leading singularity given by
the triangulation { _X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,X_ 5 _,_ 7 _,X_ 1 _,_ 7 and _X_ 1 _,_ 5} (see first of figure 27). We need to take
residue in corresponding _y_ ’s, which corresponds to taking the coefficient of _y_ 1 _,_ 3 _y_ 3 _,_ 5 _y_ 5 _,_ 7 _y_ 1 _,_ 7


67


**Figure** **27** : Dual diagram and linearized _u_ ’s for 4-point leading singularity.


**Figure** **28** : Dual diagrams for 5- and 6-point leading singularities.


of ∏ _u_ _[X]_ . Again it is straightforward to obtain the linearized _u_ ’s from the rules above, for
example (see figure 27):
_u_ _[X]_ 1 _,_ 4 [1] _[,]_ [4] = 1 − _X_ 1 _,_ 4( _y_ 3 _,_ 5 − _y_ 1 _,_ 3 _y_ 3 _,_ 5) _,_ (6.6)

_u_ _[X]_ 1 _,_ 6 [1] _[,]_ [6] = 1 − _X_ 1 _,_ 6( _y_ 5 _,_ 7 − _y_ 1 _,_ 5 _y_ 5 _,_ 7 − _y_ 1 _,_ 3 _y_ 1 _,_ 5 _y_ 5 _,_ 7) _,_ (6.7)

_u_ _[X]_ 3 _,_ 7 [3] _[,]_ [7] = 1 − _X_ 3 _,_ 7 _y_ 1 _,_ 5(−1 + _y_ 1 _,_ 7)(−1 + _y_ 3 _,_ 5) _._ (6.8)


Now the leading singularity obtained from the coefficient above contains three different
orders, _α_ [′] _[k]_ for _k_ = 3 _,_ 4 _,_ 5, which correspond to gluing 2 three-point amplitudes with 0 _,_ 1 or
2 of them being _F_ [3] vertices, respectively. The leading pure YM contribution reads

_c_ 5 _,_ 8 ( _X_ 1 _,_ 4 ( _X_ 2 _,_ 7 − _X_ 2 _,_ 5) + _X_ 2 _,_ 5 _X_ 4 _,_ 7) − _c_ 1 _,_ 4 ( _c_ 5 _,_ 8 _X_ 3 _,_ 7 − _X_ 3 _,_ 6 _X_ 5 _,_ 8 + _X_ 1 _,_ 6 ( _X_ 5 _,_ 8 − _X_ 3 _,_ 8))

- _X_ 1 _,_ 4 _X_ 1 _,_ 6 ( _X_ 2 _,_ 8 − _X_ 5 _,_ 8) − _X_ 1 _,_ 4 _X_ 2 _,_ 6 _X_ 5 _,_ 8 + _X_ 2 _,_ 5 ( _X_ 1 _,_ 4 − _X_ 4 _,_ 6) _X_ 5 _,_ 8 + _X_ 1 _,_ 6 _X_ 2 _,_ 5 ( _X_ 1 _,_ 4 − _X_ 4 _,_ 8 + _X_ 5 _,_ 8) _,_
(6.9)

where we have kept the expression directly from the computation, which is written in terms
of both _c_ ’s and _X_ ’s. The sub-leading contribution with one _F_ [3] insertion reads

_X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 8 + _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 7 _X_ 5 _,_ 8 + _X_ 1 _,_ 6 _X_ 2 _,_ 4 _X_ 5 _,_ 8 _X_ 3 _,_ 7
(6.10)

  - _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 7 − _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 5 _,_ 8 − _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 5 _,_ 8 _X_ 3 _,_ 7 + ( _Xi,j_ → _Xi_ +4 _,j_ +4) _._

Finally, the pure _F_ [3] term is simply   - _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 7 _X_ 5 _,_ 8. Remarkably, the pure _F_ [3]

contribution contains only one term in both cases we have considered above. In fact, this
is true for any pure _F_ [3] leading singularity, or equivalently the highest _α_ [′] order, to all
loops! For now, let us discuss tree-level pure _F_ [3] leading singularities for any triangulation

to all _n_ . According to (6.1), each _X_ is multiplied with at least one _y_, thus the highest


68


**Figure** **29** : Gluing of 3-point amplitudes.


_α_ [′] order is given by a single term, namely the product of all _X_ ’s (with a minus sign) that
intersects only one of those initial _X_ ’s. For example, for _n_ = 5 with scaffolding triangulation
{ _X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,...,X_ 9 _,_ 1} and inner triangulation { _X_ 1 _,_ 5 _,X_ 1 _,_ 7} (see the first graph in figure 28),
the term with only _F_ [3] vertices is

LS _[F]_ 5; [ 3] _X_ 15= _X_ 17=0 [= −] _[X]_ [1] _[,]_ [4] _[X]_ [1] _[,]_ [6] _[X]_ [1] _[,]_ [8] _[X]_ [2] _[,]_ [5] _[X]_ [3] _[,]_ [7] _[X]_ [5] _[,]_ [9] _[X]_ [7] _[,]_ [10] _[.]_ (6.11)

For _n_ = 6 with inner triangulations _a_ = { _X_ 1 _,_ 5 _,X_ 1 _,_ 7 _,X_ 1 _,_ 9}, _b_ = { _X_ 3 _,_ 7 _,X_ 1 _,_ 7 _,X_ 1 _,_ 9} and
_c_ = { _X_ 1 _,_ 5 _,X_ 5 _,_ 9 _,X_ 1 _,_ 9} as presented in figure 28, the LS are

LS _[F]_ 6; [ 3] _a_ [= −] _[X]_ [1] _[,]_ [4] _[X]_ [1] _[,]_ [6] _[X]_ [1] _[,]_ [8] _[X]_ [1] _[,]_ [10] _[X]_ [2] _[,]_ [5] _[X]_ [3] _[,]_ [7] _[X]_ [5] _[,]_ [9] _[X]_ [7] _[,]_ [11] _[X]_ [9] _[,]_ [12] _[,]_



LS _[F]_ 6; [ 3] _b_ [= −] _[X]_ [1] _[,]_ [5] _[X]_ [1] _[,]_ [8] _[X]_ [1] _[,]_ [10] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [6] _[X]_ [3] _[,]_ [9] _[X]_ [4] _[,]_ [7] _[X]_ [7] _[,]_ [11] _[X]_ [9] _[,]_ [12] _[,]_

LS _[F]_ 6; [ 3] _c_ [= −] _[X]_ [1] _[,]_ [4] _[X]_ [1] _[,]_ [7] _[X]_ [1] _[,]_ [10] _[X]_ [2] _[,]_ [5] _[X]_ [3] _[,]_ [9] _[X]_ [5] _[,]_ [8] _[X]_ [5] _[,]_ [11] _[X]_ [6] _[,]_ [9] _[X]_ [9] _[,]_ [12] _[.]_



(6.12)



In general, the highest-order contribution of any _n_ -point LS is given by a product of
2 _n_ −3 _X_ ’s, which is consistent with the fact that it is obtained from gluing _n_ −2 _F_ [3] vertices.
For lower order terms, we replace _k_ = 1 _,_ 2 _,_ ⋯ _,n_ −2 of _F_ [3] vertices by three-point Yang-Mills
ones, which have mass dimension of _X_ [2] _[n]_ [−][3][−] _[k]_, thus for the lowest order, _i.e._ pure YM LS,
the mass dimension is the expected _X_ _[n]_ [−][1] ). Since YM 3-point amplitude has more terms
than _F_ [3], the number of terms grows for lower order terms.
Now it is a remarkable fact that any such (2 _n_ −3)-fold residue, computed by extracting
the coefficient of ∏ _y_ in the expansion, agrees with gluing _n_ −2 three-point amplitudes
(which is the sum of both the YM and _F_ [3] pieces) together! Of course, at tree-level this is

guaranteed by the fact that the formula is computing _n_ -gluon tree amplitude in the bosonic

string which must contain all such LS. However, even without such a direct relation with

bosonic string at loop level, as we will see shortly residues of loop-level stringy formulas

continue to give correct loop-level LS!

Already at tree-level, these residues are compared with the actual leading singulari
ties obtained from gluing three-point amplitudes using the factorization rule (4.35). For

example, the four-point LS is given by the gluing of two three-point amplitudes, which is

illustrated in figure 29.



4
LS [YM] _L_ (1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,a_ ) = ∑( _Xj,a_ - _Xj,_ 5) _Q_ _[L]_ _j_ [=] _[ g]_ [2] _[,a]_ [(−] _[X]_ [1] _[,]_ [4][) +] _[ g]_ [3] _[,a]_ [(] _[c]_ [1] _[,]_ [4][) +] _[ g]_ [4] _[,a]_ [(−] _[X]_ [2] _[,]_ [5][)] _[,]_
_j_ =2


8
LS [YM] _R_ [(] _[a,]_ [5] _[,]_ [6] _[,]_ [7] _[,]_ [8] _[,]_ [1][) =] ∑ ( _Xa,J_ - _X_ 1 _,J_ ) _Q_ _[R]_ _J_ [=] _[ g][a,]_ [6][(−] _[X]_ [5] _[,]_ [8][) +] _[ g][a,]_ [7][(] _[c]_ [5] _[,]_ [8][) +] _[ g][a,]_ [8][(−] _[X]_ [1] _[,]_ [6][)] _[,]_
_J_ =6


69



(6.13)


where LS _[Y M]_ _L_ / _R_ [denotes three-point YM amplitude/LS on the left/right side, and] _[ g][j,a]_ [ = (] _[X][j,a]_ [−]
_Xj,_ 5), _ga,J_ = ( _Xa,J_ - _X_ 1 _,J_ ). The gluing rule directly formulated in _X_ variables is given by
the factorization (4.35):

∑( _Xj,a_   - _Xj,_ 5) _Q_ _[L]_ _j_ [(] _[X][a,J]_ [−] _[X]_ [1] _[,J]_ [)] _[Q]_ _J_ _[R]_ [→−∑] ( _Xj,J_   - _Xj,_ 5 − _X_ 1 _,J_ ) _Q_ _[L]_ _j_ _[Q]_ _J_ _[R][,]_ (6.14)
_j,J_ _j,J_

which is equal to _gj,aga,J_ → _gj,J_ ≡( _Xj,_ 5 + _X_ 1 _,J_ - _Xj,J_ ).



LS [YM] 4 = LS [YM] _L_ (1 _,...,_ 5 _,a_ ) ⊗ LS [YM] _R_ [(] _[a,]_ [5] _[,...,]_ [1][)]

= _g_ 2 _,_ 6( _X_ 1 _,_ 4 _X_ 5 _,_ 8) + _g_ 3 _,_ 6(− _c_ 1 _,_ 4 _X_ 5 _,_ 8) + _g_ 4 _,_ 6( _X_ 2 _,_ 5 _X_ 5 _,_ 8)

+ _g_ 2 _,_ 7(− _X_ 1 _,_ 4 _c_ 5 _,_ 8) + _g_ 3 _,_ 7( _c_ 1 _,_ 4 _c_ 5 _,_ 8) + _g_ 4 _,_ 7(− _X_ 2 _,_ 5 _c_ 5 _,_ 8)

+ _g_ 2 _,_ 8( _X_ 1 _,_ 4 _X_ 1 _,_ 6) + _g_ 3 _,_ 8(− _c_ 1 _,_ 4 _X_ 1 _,_ 6) + _g_ 4 _,_ 8( _X_ 2 _,_ 5 _X_ 1 _,_ 6) _,_



(6.15)



where of course the gluing result LS [YM] 4 agrees with the residue (6.9), and ⊗ denotes the
gluing rule _gj,aga,J_ → _gj,J_ .
Recall the 3-point F [3] amplitude obtained in section 3.5 (for both L and R):


LS [F] _L_ [3][(][1] _[,]_ [2] _[,]_ [3] _[,]_ [4] _[,]_ [5] _[,a]_ [) =] _[ g]_ [3] _[,a][X]_ [1] _[,]_ [4] _[X]_ [2] _[,]_ [5] _[,]_

(6.16)
LS [F] _R_ [3][(] _[a,]_ [5] _[,]_ [6] _[,]_ [7] _[,]_ [8] _[,]_ [1][) =] _[ g][a,]_ [7] _[X]_ [1] _[,]_ [6] _[X]_ [5] _[,]_ [8] _[.]_


We can glue F [3] amplitude with YM amplitude to give the 4-point LS LS4 [YM][+][F][3], and
LS LS [F] 4 [3] with two _F_ [3] vertices:

LS [YM] 4 [+][F][3] = LS [F] _L_ [3][(][1] _[,...,]_ [5] _[,a]_ [) ⊗] [LS] _R_ [YM][(] _[a,]_ [5] _[,...,]_ [1][) +][ LS] _L_ [YM] (1 _,...,_ 5 _,a_ ) ⊗ LS [F] _R_ [3][(] _[a,]_ [5] _[,...,]_ [1][)]

= ( _g_ 2 _,_ 7(− _X_ 1 _,_ 4) + _g_ 3 _,_ 7( _c_ 1 _,_ 4) + _g_ 4 _,_ 7(− _X_ 2 _,_ 5)) _X_ 1 _,_ 6 _X_ 5 _,_ 8
+ ( _g_ 3 _,_ 6(− _X_ 5 _,_ 8) + _g_ 3 _,_ 7( _c_ 5 _,_ 8) + _g_ 3 _,_ 8(− _X_ 1 _,_ 6)) _X_ 1 _,_ 4 _X_ 2 _,_ 5 _,_


LS4 [F][3] [=][ LS] _L_ [F][3][(][1] _[,...,]_ [5] _[,a]_ [) ⊗] [LS] _R_ [F][3][(] _[a,]_ [5] _[,...,]_ [1][)]

= _g_ 3 _,_ 7 _X_ 1 _,_ 6 _X_ 5 _,_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 5 = − _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 7 _X_ 5 _,_ 8 _._
(6.17)
It is straightforward to see that the gluing of _F_ [3] vertices is particularly simple, always

giving one term for any _n_ and agrees with the residue discussed above.


**6.3** **Loop** **level**


Now we present examples at loop level. Starting with one-loop three-point triangle with
triangulation { _X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,X_ 5 _,_ 1 _,Y_ 1 _,Y_ 3 _,Y_ 5}, the linearized _u_ ’s are, for example, (see figure 30)

_u_ _[X]_ 2 _,_ 5 [2] _[,]_ [5] = 1 − _X_ 2 _,_ 5 _y_ 1 _,_ 3 _y_ 3(1 − _y_ 5 − _y_ 5 _y_ 1 _,_ 5) _,_ (6.18)

_u_ _[X]_ 5 _,_ 2 [5] _[,]_ [2] = 1 − _X_ 5 _,_ 2 _y_ 1 _,_ 3 _y_ 1(1 − _y_ 3 _,_ 5) _,_ (6.19)

( _uY_ 2) _[Y]_ [2] = 1 − _Y_ 2 _y_ 1 _,_ 3(1 − _y_ 1 − _y_ 1 _y_ 5 − _y_ 1 _y_ 3 _y_ 5) _._ (6.20)


70


**Figure** **30** : Dual diagram and linearized _u_ ’s for 1-loop triangle leading singularity.


**Figure** **31** : Dual diagram for 1-loop massless bubble and self-intersecting curve needed

for the leading singularity computation.


The remaining _u_ ’s that give non-vanishing contribution are cyclic of (6.18)-(6.20) and

the one corresponds to the closed curve:


( _u_ ∆) [∆] = 1 − ∆ _y_ 1 _y_ 3 _y_ 5 _._ (6.21)


Then we can directly obtain the result:


−2 _Y_ 6 _X_ 1 _,_ 4 _X_ 2 _,_ 5 − 2 _Y_ 2 _X_ 1 _,_ 4 _X_ 3 _,_ 6 − 2 _Y_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 6 + 2 _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 6 −(∆ + 1) _Y_ 2 _Y_ 4 _Y_ 6 _._ (6.22)


It is worth noting that the complete result for this case contains no contribution from
the _F_ [3] vertices. In fact, if we include the _u_ ’s corresponding to the curves { _X_ 3 _,_ 1 _,X_ 5 _,_ 3 _,X_ 1 _,_ 5}
(See right of figure 30), we can compute the _F_ [3] term _Y_ 2 _Y_ 4 _Y_ 6 _X_ 3 _,_ 1 _X_ 5 _,_ 3 _X_ 1 _,_ 5 but it vanishes
since we have set { _X_ 3 _,_ 1 _,X_ 5 _,_ 3 _,X_ 1 _,_ 5} → 0 (on-shell). Similarly, all the terms with at least
one _F_ [3] vertex vanish.

For the 3-point massless bubble, as depicted in figure 31 (left), it is crucial to include

the curve with a single self-intersection (see figure 31, right), whose corresponding linearized

_u_ reads:
( _u_ [S] 3 _,_ _[.]_ 6 [I] _[.]_ [)] _[X]_ [3] _[,]_ [6] [=][ 1][ −] _[X]_ [3] _[,]_ [6] _[y]_ [1] _[y]_ [3] _[y]_ [1] _[,]_ [3] _[y]_ [5] _[,]_ [1] _[.]_ (6.23)


Then one can compute the result which contains contributions with zero and one _F_ [3]


vertex to be


(1 + ∆) _Y_ 2 ( _Y_ 5 _X_ 1 _,_ 4 − _Y_ 6 _X_ 1 _,_ 4 − _Y_ 4 _X_ 3 _,_ 6 + _Y_ 5 _X_ 3 _,_ 6 − _Y_ 5 _X_ 4 _,_ 6 + _X_ 3 _,_ 6 _X_ 1 _,_ 4 + _Y_ 5 _X_ 3 _,_ 6 _X_ 1 _,_ 4) _._ (6.24)


Again curves with higher self-intersection are irrelevant as they begin at quadratic or

higher order and don’t contribute to the leading singularity.


71


**Figure** **32** : Dual diagrams of 2-loop 2- and 3-point leading singularities.


For the 4-point box, the result already contains 434 terms which we present in appendix B, however, the highest _α_ [′] order is again given by a single term:


_Y_ 2 _Y_ 4 _Y_ 6 _Y_ 8 _X_ 1 [2] _,_ 5 _[X]_ 3 [2] _,_ 7 _[.]_ (6.25)


In fact, using the rule we have previously introduced, we can obtain directly the contribution with only _F_ [3] vertices for the 5- and 6-point penta- and hexa-gon:

Pentagon ∶− _Y_ 2 _Y_ 4 _Y_ 6 _Y_ 8 _Y_ 10 _X_ 1 _,_ 5 _X_ 1 _,_ 7 _X_ 3 _,_ 7 _X_ 3 _,_ 9 _X_ 5 _,_ 9 _,_

(6.26)
Hexagon ∶ _Y_ 2 _Y_ 4 _Y_ 6 _Y_ 8 _Y_ 10 _Y_ 12 _X_ 1 _,_ 5 _X_ 1 _,_ 9 _X_ 3 _,_ 7 _X_ 3 _,_ 11 _X_ 5 _,_ 9 _X_ 7 _,_ 11 _._


It is straightforward to generalize the computation to one-loop higher points, and in

particular for _n_ -gon LS, one can check that the result agrees with those written in terms

of polarization and (external and loop) momenta [39].

Finally, let us present some examples for 2-loop 2- and 3-point. We attach the same
∆to all closed curves. For simplicity, we will focus on the leading _α_ [′] order. Now for the

gluing of two 1-loop 2-point bubble (first graph in figure 32), the result reads:

−(1 + ∆) [2] _Ya,_ 2 _Yb,_ 4 _Ya,b_ + ( _a_ ↔ _b_ ) _,_ (6.27)


where we have the second term since the integrand contains the contribution of the graph

from symmetrization of loop punctures _a,b_ . For the second graph in figure 32, the result is

2(1 + ∆) _X_ 2 _,_ 4 _Ya,_ [2] 1 _[,]_ (6.28)

where the factor of 2 comes from the symmetrization (1 ↔ 3 _,a_ ↔ _b_ ) of the graph. For
3-point, the third graph reads:

(1+∆) _Yb,_ 6 (−(1 + ∆) _Ya,_ 2 _Ya,_ 4 _Ya,b_ + 2( _X_ 1 _,_ 4 _X_ 2 _,_ 5 _Yb,_ 3 − _X_ 1 _,_ 4 _X_ 2 _,_ 5 _Ya,b_ - _X_ 1 _,_ 4 _Ya,_ 2 _Yb,_ 3 − _X_ 2 _,_ 5 _Ya,_ 4 _Yb,_ 3)) _,_
(6.29)

and the final graph is:

_Yb,_ 3(4 _X_ 1 _,_ 4 _X_ 2 _,_ 5 _Ya,_ 6 − 4 _X_ 1 _,_ 4 _Ya,_ 2 _Ya,_ 6 − 4 _X_ 2 _,_ 5 _Ya,_ 4 _Ya,_ 6 (6.30)

−(1 + ∆) _Yb,_ 6( _X_ 1 _,_ 4 _Ya,_ 2 + _X_ 2 _,_ 5 _Ya,_ 4 − _X_ 1 _,_ 4 _Yb,_ 2 + _X_ 1 _,_ 4 _Yb,_ 3 − _X_ 2 _,_ 4 _Yb,_ 3 + _X_ 2 _,_ 5 _Yb,_ 3 − _X_ 2 _,_ 5 _Yb,_ 4)) _._


It is important to include the curves that can self-intersect up to once around either of

the punctures. Of course the expression again matches what we get from explicit gluing.


72


**7** **Integrand** **Cuts:** **Tree-loop** **cut** **and** **loop-cut**


We finally turn to the most non-trivial checks on our proposal - the cuts of our integrand.
In this section, we will study both the tree-like cut, where we go on residue at _Xi,j_ = 0
( _i,j_ both odd), that we will call the tree-loop cut, and the loop-cut, given by the residue

of our curve integral at loop level, on a “single cut” setting a single loop propagator to
zero, _Yi_ = 0 (i odd). In the first case, this should match the gluing of a tree process with
a one-loop integrand, while in the second case, we should match the “forward limit” of an

amplitude with one loop lower. Now, in the later case, this match is usually fraught with

subtlety in non-supersymmetric theories, due to the fact that both single-cuts and forward

limits are naively infected with “1/0” divergences. But as we have hinted earlier, dealing

with surface kinematics gives us a way out of this impasse, allowing a non-trivial match

between “loop cut” and “forward limit” to be made.

In this section, we will start by deriving the gluing rules in momentum space, and

then proceed to explain the generalization of them to surface kinematics. The later part

is directly given to us by understanding the residues surface integral defining the surface

integrands at low-energies. We will focus on studying both cuts at one-loop.

We will start with the tree-loop cut where we will see that if we cut a tree-like propaga
tor the final answer matches the generalized gluing of a tree and a loop-integrand, defined

in terms of surface kinematics. Next, we will see that if we cut any loop propagator at one

loop, it matches the tree-level amplitude in the forward limit, with the cut loop adding

two color-adjacent particles, “glued” by summing over polarization states. This will hold
not only in the field theory limit but even at finite _α_ [′] .


**7.1** **Tree-loop** **Cut**


In this case, we are considering starting with a one-loop integrand, and cutting it via
a given propagator _Xa,b_ with _a_ < _b_ and _a,b_ both odd, so that the puncture is on the
right of the curve _Xa,b_ . In this limit, we expect to match the gluing of a tree amplitude,
A _L_ ( _a,a_ + 1 _,_ ⋯ _,b_ - 1 _,b,x_ ), and a loop-integrand on the right, I _R_ ( _b,b_ + 1 _,_ ⋯ _,a_ - 1 _,a,x_ [′] ). This
is precisely the type of factorization already studied at tree-level in section 4.4, with the

difference that now the lower point object on the right is a loop-integrand instead of a tree

amplitude.

Recall from 4.4, that in momentum space this cut was written as follows:

Aglued ∝∑(− _Xb,J_         - _Xa,j_ + _Xj,J_ ) _∂Xx,j_ A _L∂Xx_ ′ _,J_ A _R,_ (7.1)
_j,J_

where _j_ ranges over the indices entering A _L_ and _J_ those on A _R_ . Therefore the only
difference for the case in which A _R_ ≡I _R_ is that the sum over _J_ is now _J_ ∈{ _b_ + 1 _,b_ + 2 _,_ ⋯ _,a_ 1 _,p_ }, where _p_ is the puncture.
In addition, in this formula all the _X_ ’s entering correspond to momentum invariants

that, as explained previously, are read off by homology. This means that in this formula
we have _Xj,J_ = _XJ,j_, as well as the tadpole curves and external bubble that appear in the
sum, such as _Xa_ +1 _,a_ −1 and _Xa,a_, are set to zero.


73


So our goal now is to derive an extension of (7.1) that is defined for full surface

kinematics described in 5.2. To do this we start with the definition of the surface integrand
coming from the surface integral where we assign the kinematics to each curve _X_ C according
to 5.2, and study what happens on the residue at _Xa,b_ = 0.


**7.1.1** **Tree-loop** **cut** **from** **surface** **integral**

We know that taking the residue at _Xa,b_ = 0 of the full integrands, corresponds to taking
the residue of the form in the surface integral at _ya,b_ = 0, provided we picked an underlying
fatgraph containing propagator _Xa,b_ . So we want to extract the following residue


⎛ 1 ⎞
Res _ya,b_ =0 ⎝ _ya,b_ [2] C∈S∏ _u_ _[X]_ C [C] ⎠ _[,]_ (7.2)


where we are omitting the remaining integration _y_ ’s as well as the scaffolding residue,

required to get the gluon amplitude.
Now the _u_ -variables that have a non-zero derivative with respect to _ya,b_, and thus
contribute to this residue, correspond to those associated to curves that cross _Xa,b_ once or
intersect it as lamination. If we read off the kinematics _X_ C by homology, than these curves
are precisely those appearing in the prefactor in (7.1). However if we are keeping all the

curves, we should be more careful in understanding these residue.

Let’s start by listing all the curves that will contribute to the residue. Of course, as
before we have the contribution from curves from _j_ to _J_, where now we distinguish, _u_ [(] _[q]_ [)]
_j,J_
and _u_ [(] _[q]_ [)] [with] _[q]_ [labeling] [the] [self-intersection] [which] [can] [be] [either] [zero] [or] [one,] _[q]_ [ =][ 0] _[,]_ [1,] [and]
_J,j_ [,]

_j_ ∈ **L** = { _a_ + 1 _,_ ⋯ _,b_ - 1} and _J_ ∈ **R** = { _b_ + 1 _,_ ⋯ _,a_ - 1}. Now in addition to _u_ [(] _a,J_ _[q]_ [)] [and] _[u]_ [(] _J,a_ _[q]_ [)][,] [we]

have curves _u_ [(] _a,j_ [1][)] [as] [well] [as] _[u]_ [(] _j,a_ _[q]_ [)][.] [Similarly,] [we] [have] [curves] _[u]_ [(] _j,b_ _[q]_ [)] [and] _[u]_ _b,j_ [(] _[q]_ [)][,] [as] [well] [as] _[u]_ _b,a_ [(] _[q]_ [)][.]

Finally, we have also contribution coming from _u_ [(] _a,a_ _[q]_ [)][.]
Let’s now go through each of these separately and derive the contribution they give
on the residue, _Xa,b_ = 0. Starting with _u_ [(] _j,J_ _[q]_ [)] [and] _[u]_ [(] _J,j_ _[q]_ [)][,] [it] [is] [trivial] [to] [show] [(as] [shown] [in] [an]
appendix) that in the locus where _ya,b_ = 0 we have:



_∂_ log _u_ [(] _[q]_ [)] _∂_ log _u_ [(] _[q]_ [)]
_j,J_ _x_ [′] _,J_
∣ = _[∂]_ [log] _[ u][j,x]_ ∣ × ∣ _,_
_∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0



_∂_ log _u_ [(] _[q]_ [)] _∂_ log _u_ [(] _[q]_ [)]
_J,j_ ∣ = _[∂]_ [log] _[ u][j,x]_ ∣ × _J,x_ [′] ∣ _._
_∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0



(7.3)



Now inside the surface integral, these derivatives precisely allow us to interpret the
result on the residue in terms of the lower-objects as we can write them as _∂Xj,x_ A _L_ ×
_∂Xx_ ′ _,J_ I _R_ . Therefore the contribution to the residue coming from these curves is simply

_∂_ A _L_ _∂_ I _R_ _∂_ A _L_ _∂_ I _R_ _∂_ A _L_
∑ _Xj,J_ × + _XJ,j_ × × _[∂]_ [I] _[R]_ (7.4)
_j,J_ _∂Xj,x_ _∂Xx_ ′ _,J_ _∂Xj,x_ _∂XJ,x_ ′ [+] _[ Y][j]_ _∂Xj,x_ _∂Yx_ [′] _[,]_


74


where we have added explicitly the case in which _J_ = _p_ . Now the remaining curves that
cross _Xa,b_ are then: _u_ [(] _j,b_ [1][)] _[,u]_ _b,j_ [(] _[q]_ [)] [as] [well] [as] _[u]_ _j,a_ [(] _[q]_ [)] _[,u]_ _a,j_ [(][1][)][,] [for] [which] [we] [can] [similarly] [derive:]



_∂_ log _u_ [(][1][)]
_j,b_
∣ = _[∂]_ [log] _[ u][j,x]_
_∂ya,b_ _ya,b_ =0 _∂ya,b_

_∂_ log _u_ [(] _[q]_ [)]
_b,j_
∣ = _[∂]_ [log] _[ u][j,x]_
_∂ya,b_ _ya,b_ =0 _∂ya,b_




[log] _[ u][j,x]_ _∂_ log _ux_ [(][1][′] _,b_ [)] _∂_ A _L_

∣ × ∣ ⇒ _Xj,b_ × _[∂]_ [I] _[R]_
_∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂Xj,x_ _∂Xx_ ′

[log] _[ u][j,x]_ _∂_ log _u_ [(] _b,x_ _[q]_ [)][′] _∂_ A _L_

∣ × ∣ ⇒ _Xb,j_ × _[∂]_ [I] _[R]_
_∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂Xj,x_ _∂X_



_,_
_∂Xx_ ′ _,b_



_∂Xb,x_ ′ _[,]_



_∂_ log _u_ [(] _j,a_ _[q]_ [)] _∂_ log _u_ [(] _x_ _[q]_ [′] _,a_ [)] _∂_ A _L_ _∂_ I _R_
∣ = _[∂]_ [log] _[ u][j,x]_ ∣ × ∣ ⇒ _Xj,a_ × _,_
_∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂Xj,x_ _∂Xx_ [′] _,a_

_∂_ log _u_ [(] _a,j_ [1][)] _∂_ log _ua,x_ [(][1][)][′] _∂_ A _L_ _∂_ I _R_
∣ = _[∂]_ [log] _[ u][j,x]_ ∣ × ∣ ⇒ _Xa,j_ ×
_∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂Xj,x_ _∂Xa,x_ [′] _[,]_



(7.5)



for any _j_ ∈ **L** . Note that even though _ux_ [(][0][′] _,b_ [)] [(similarly] [for] _[u]_ [(] _a,x_ [0][)][′][)] [corresponds] [to] [a] [purely]

boundary curve _u_ [(] _x_ [1][′] _,b_ [)] [does] [not,] [and] [therefore] [by] [keeping] [curves] _[X][x]_ [′] _[,b]_ [non-zero] [in] [the] [inte-]
grand, we can once more interpret the result on the residue as a derivative of the lower-point

object. The contributions to the cut of each of these curves are presented on the right in

(7.5).
Now let’s proceed to study the curves that intersect _Xa,b_ as _laminations_, and as shown
in the appendix, in this case the derivative of the _u_ -variables still factorize but in a different

way.
To begin we have curves _u_ [(] _j,b_ [0][)] [for] [all] _[j]_ [∈] **[L]** [/{] _[b]_ [ −] [1][}][,] [from] [which] [we] [get:]



_∂_ log _u_ [(][0][)]
_j,b_
∣ = _[∂]_ [log] _[ u][j,x]_
_∂ya,b_ _ya,b_ =0 _∂ya,b_




[1] _[u][a,b]_

∣ _,_ (7.6)
_∂ya,b_ _ya,b_ =0




[log] _[ u][j,x]_ ∣ × − _[∂]_ [log][ (][1][ −] _[u][a,b]_ [)]

_∂ya,b_ _ya,b_ =0 _∂ya,b_



from which we get the following contribution to the cut



_∂_ A _L_

- _Xj,b_ × ∑ ( _[∂]_ [I] _[R]_
_∂Xj,x_ ⎡⎢⎢⎢⎢⎣ _J_ ∈ **R** ∪{ _a,b_ } _∂Xx_ ′



_∂_ I _R_

_[∂]_ [I] _[R]_ + _[∂]_ [I] _[R]_

_∂Xx_ ′ _,J_ _∂XJ,x_ ′ [) +] _∂Yx_ [′]



_∂Yx_ [′]



_,_ (7.7)
⎤⎥⎥⎥⎥⎦



for all _j_ ∈ **L** /{ _b_ - 1}. In addition, curves _u_ [(] _b,a_ _[q]_ [)][,] _[u][a,p]_ [,] _[u][a,p]_ [and] _[u]_ [(] _a,a_ _[q]_ [)] [also] [laminate] [the] [puncture]
giving us the following contributions on the cut:



_∂_ A _L_
_∂Xj,x_ × _∂Y_ _[∂]_ [I] _x_ _[R]_ [′] [−] _[X][a,a]_ [ ∑] _j_ ∈ **L**



_∂_ A _L_ _∂_ I _R_
_∂Xj,x_ × ( _∂X_ _[∂]_ [I] _x_ _[R]_ [′] _,a_ + _∂Xa,x_ [′] [)] _[,]_ [(7.8)]




- _Xb,a_ ∑
_j_ ∈ **L**



_∂_ A _L_
× _[∂]_ [I] _[R]_
_∂Xj,x_ _∂Xb,x_ ′ [−] _[Y][a]_ [ ∑] _j_ ∈ **L**



and finally we also have curves _u_ [(] _a,J_ _[q]_ [)] [for] [all] _[J]_ [∈] **[R]** [as] [well] [as] _[u]_ _J,a_ [(] _[q]_ [)] [for] _[J]_ [∈] **[R]** [/{] _[a]_ [ −] [1][}][,] [since] [for]

_J_ = _a_ - 1, we only have _u_ [(] _a_ [1] - [)] 1 _,a_ [since] _[u]_ _a_ [(][0] - [)] 1 _,a_ [is] [a] [boundary.] [We] [will] [see] [this] [last] [case] [is] [a] [bit]
more subtle, but for the remaining curves, just like before we get, in the residue



_∂_ A _L_ _∂_ I _R_
× (7.9)
_∂Xj,x_ _∂XJ,x_ ′ _[.]_



−∑ _Xa,J_ ∑
_J_ ∈ **R** _j_ ∈ **L**



_∂_ A _L_ _∂_ I _R_
×   - ∑ _XJ,a_ ∑
_∂Xj,x_ _∂Xx_ ′ _,J_ _J_ ∈ **R** /{ _a_ −1} _j_ ∈ **L**


75


Now let’s look at the contribution of curve _u_ [(] _a_ [1]  - [)] 1 _,a_ [,] [just] [like] [for] [the] [remaining] [curves]
laminating curves, the dlog also factorizes to give:

_∂_ log _u_ [(] _a_ [1]       - [)] 1 _,a_ _∂_ log _ua_ [(][1]       - [)] 1 _,x_ [′]
∣ = − _[∂]_ [log][ (][1][ −] _[u][a,b]_ [)] ∣ × ∣ _,_ (7.10)
_∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0 _∂ya,b_ _ya,b_ =0

and once inside the surface integral the first term will produce the −∑ _j_ ∈ **L** _∂_ A _L_ / _∂Xj,x_,
also obtained in the previous cases, however now the second term in the product is _not_
_∂_ I _R_ / _∂Xa_ −1 _,x_ [′] . This would only be true if we had the dlog of the product of _ua_ [(][0] - [)] 1 _,x_ [′] _[u]_ [(] _a_ [1] - [)] 1 _,x_ [′][,]
which both have the same exponent, _Xa_ −1 _,x_ [′] in the surface integral, this is:



⎤⎥⎥⎥⎥⎥⎦



⎞
⎟ ∏ _u_ _[X]_ [C]
C
⎠ C∈SI _R_



∣
_ya,b_ =0



(7.11)



_∂X∂a_ I− _R_ 1 _,x_ [′] [= ∫] SI _R_ _P_ ≠(∏ _a,b_ )

= Q [(] _a_ [0]    - [)] 1 [+ Q] _a_ [(][1]    - [)] 1



d _yP_

_y_ [2]
_P_



⎛
⎜
⎝

⎡⎢⎢⎢⎢⎢⎣



log _u_ [(][0][)] log _u_ [(][1][)]
_a_ −1 _,x_ [′] + _a_ −1 _,x_ [′]
_∂ya,b_ _∂ya,b_



and for the tree-loop cut, we only want the second term in the sum on the r.h.s. This

term in precisely the counterpart of the correction term we derived in the gauge-invariance

statement for the surface integrand in 5.3. So from equation (5.5), we have that

_∂_ I _R_
Q [(] _a_ [1]          - [)] 1 [= −] _∂Xa_ −1 _,a_ ∣ _x_ [′] → _a,_ (7.12)

and thus the contribution from curve _u_ [(] _a_ [1] - [)] 1 _,a_ [to] [the] [cut] [is:]



+ _Xa_ −1 _,a_ ∑
_j_ ∈ **L**



_∂_ A _L_ _∂_ I _R_
× ∣ _._ (7.13)
_∂Xj,x_ _∂Xa_ −1 _,a_ _x_ [′] → _a_



In summary, collecting all the different contributions derived above, we can write the

tree-loop cut as follows:



_L_
_X_ Res _a,b_ =0 [(][Ω] 2 [loop] _n_ [) =] _j_ ∈ _L,J_ ∑∈ _R_ [( _Xj,J_ - _Xj,bδ_ [ˆ] _j,b_ −1 − _Xa,J_ ) _∂X_ _[∂]_ [A] _j,x_ [S]



_∂_ I _R_ [S]
_∂Xx_ ′ _,J_



_L_
+( _XJ,j_ - _Xj,bδ_ [ˆ] _j,b_ −1 − _XJ,aδ_ [ˆ] _J,a_ −1) _[∂]_ [A][S]
_∂Xj,x_



_∂_ I _R_ [S]
_∂XJ,x_ ′ []]



(7.14)



_L_
+ ∑ [( _Xj,p_ - _Xa,p_ - _Xj,bδ_ [ˆ] _j,b_ −1) _[∂]_ [A][S]
_j_ ∈ _L_ _∂Xj,x_



_∂_ I _R_ [S]
]
_∂Xx_ [′] _,p_



+ ∑ _Xa_ −1 _,a_ _∂_ A [S] _L_
_j_ ∈ _L_ _∂Xj,x_



_∂_ I _R_ [S] ∣ _,_
_∂Xa_ −1 _,a_ _x_ [′] → _a_



with _δ_ [ˆ] _i,k_ = 1 − _δi,k_ .


**7.2** **Loop-Cut**


On the loop side, we will be considering a 2 _n_ -scalar 1-loop amplitude, from which we get

the _n_ -point 1-loop gluon amplitude. To define the corresponding surface, we will find it


76


**Figure** **33** : Tadpole Triangulation with _Y_ 1 and _X_ 1 _,_ 1 _,_ and loop cut.


**Figure** **34** : Tree triangulation and scaffolding residue.


convenient to pick a particular “tadpole” triangulation, whose fat-graph includes the loop
propagator _Y_ 1 as well as the tadpole propagator _X_ 1 _,_ 1 (see figure 33). Taking the loop cut
corresponds to extracting the residue when _Y_ 1 = 0, which is easy to do in this triangulation
since _Y_ 1 is one of the chords in the triangulation. The resulting tree-level result corresponds
to a (2 _n_ + 2)-point amplitude, with the two extra gluon legs glued. We call these extra
two legs 1 [′] and _p_ (see figure 33). Regardless of _Y_ 1 = 0 we still keep _X_ 1 _,_ 1 as the label of the
curve on the cut surface.
To do the matching, we consider the tree-level amplitude of 2 _n_ +4 scalars, where we label the particles as (1 _,_ 2 _,...,_ 2 _n,_ 1 [′] _,sR,p,sL_ ) so that the matching with the loop computation
becomes clearer. We make the gluons, 1 [′] and _p_, on-shell by taking the scaffolding residue,
_X_ 1 _,p_ = _X_ 1 [′] _,p_ = 0. Therefore we pick a triangulation to define the surface that contains
propagators { _X_ 1 _,p,X_ 1 _,p_ [′] _,X_ 1 _,_ 1 [′] }, the last propagator is chosen to replicate the triangulation
picked in the loop cut part (see figure 34). The corresponding fat graphs associated with

the 1-loop and tree-level triangulations are presented in figure 35.


77


**Figure** **35** : 1-loop fat graph (left) and tree-level fat graph (right).


**7.3** **Gluing** **in** **Momentum** **Space**


We will now describe the procedure for performing the polarization sum (“gluing”) for

the two gluons in the forward limit opened up by cutting a loop. This will be a bit

more interesting than the gluing we already encountered in our discussion of tree-level
factorization, where we took two separate gauge-invariant objects A _[µ]_ _L_ [(] _[p,]_ [⋯)] _[,]_ [A] _R_ _[ν]_ [(−] _[p,]_ [⋯)]
and performed the polarization sum over the intermediate particle which finally yielded
(thanks to the gauge-invariance of A _L,_ A _R_ ) the trivial gluing rule A _[µ]_ _L_ [A] _R_ _[ν]_ _[η][µν]_ [.] [Now] [instead]
here we wish to start with a single _n_ -point tree-level amplitude, and glue together two of

its adjacent legs, say 1 and _n_ . The polarization sum is:

Aglued = A _n_ _[µν]_ [(−] _[η][µ,ν]_ [+] _[p][µ][q][ν]_ [ +] _[ p][ν][q][µ]_ ) _,_ with A _[µν]_ _n_ [=] _[ ∂][ϵ]_ 1 _,µ_ _[∂][ϵ]_ _n,ν_ [A] _[n][.]_ (7.15)

_p_ ~~⋅~~ _q_


Now, there is a crucial difference with the tree-like gluing case. Gauge invariance does
**not** imply that A _[µν]_ _n_ _[p]_ _µ_ [vanishes,] [and] [in] [general] [for] [non-Abelian] [gauge] [theories] [we] [have]

A _[µν]_ _n_ _[p][µ]_ [≠] [0] _[.]_ (7.16)


This is famously related to the need to introduce ghost fields in the Lagrangian at loop

level. However all is not lost, gauge invariance still constrains the form of this object, since

we must have:
A _[µν]_ _n_ _[p][µ][p][ν]_ [=][ 0] ⇒ A _[µν]_ _n_ _[p][µ]_ [= N] _[ p][ν][,]_ (7.17)

where N is some function of the remaining kinematics and polarizations. Using this fact,
the result after gluing can be written as:

Aglued = A _n_ _[µν]_ [(−] _[η][µ,ν]_ [+] _[p][µ][q][ν]_ [ +] _[ p][ν][q][µ]_ ) = −A _[µν]_ _n_ _[η][µ,ν]_ [+][ 2][N] _[,]_ (7.18)

_p_ ~~⋅~~ _q_


where the _q_ _[µ]_ dependence dropped out again, as expected. Therefore, to perform the gluing
in the forward limit, we need to determine N .


78


Let us now rephrase some of these statements in scalar language using the _Xi,j_ ’s from
the scaffolded gluon amplitude. Again, let us say we start with an _n_ -point tree-level gluon

amplitude, so 2 _n_ scalar amplitude, and we want to glue gluons 1 and _n_ . Then the _X_ ’s
associated with the polarizations of these gluons are, respectively, _X_ 2 _[µ]_ [and] _[ X]_ 2 _[ν]_ _n_ [, so we have:]

_∂_ [2] A _n_
A _[µν]_ _n_ [=] _,_ (7.19)
_∂X_ 2 _[µ][∂X]_ 2 _[ν]_ _n_

where A _n_ stands for the amplitude obtained after taking the scaffolding residue in gluons
1 and _n_ . Now, gauge invariance and multi-linearity in particles 1 and _n_, we know we can

write:
A _n_ = ∑( _X_ 2 _,j_       - _X_ 1 _,j_ )Q [2] _j_ [= ∑] ( _X_ 2 _n,j_       - _X_ 1 _,j_ )Q [2] _j_ _[n][.]_ (7.20)
_j_ _j_

Now by linearity in the polarizations the Q [2] _j_ [cannot] [depend] [in] _[X]_ [2] _[,k]_ [for] [any] _[k]_ [,] [and]
similarly for Q [2] _j_ _[n]_ [.] [Therefore] [we] [can] [rewrite] [(][7.20][)] [as:]



A _n_ = ∑( _X_ 2 _,j_ - _X_ 1 _,j_ ) _[∂]_ [A] _[n]_
_j_ _∂X_ 2




_[∂]_ [A] _[n]_ = ∑( _X_ 2 _n,j_ - _X_ 1 _,j_ ) _[∂]_ [A] _[n]_

_∂X_ 2 _,j_ _j_ _∂X_ 2



_._ (7.21)
_∂X_ 2 _n,j_



Now plugging the second form of A _n_ into the derivative with respect to _X_ 2 _,j_, we get:

_∂_ [2] A _n_ _∂_ A _n_
A _n_ = ∑( _X_ 2 _,j_    - _X_ 1 _,j_ )( _X_ 2 _n,k_    - _X_ 1 _,k_ ) + _X_ 2 _,_ 2 _n_ _._ (7.22)
_j,k_ _∂X_ 2 _,j∂X_ 2 _n,k_ _∂X_ 2 _,_ 2 _n_

From this expression we can read off A _[µν]_ _n_ [:]

_∂_ [2] A _n_ _[∂]_ [A] _[n]_
A _[µν]_ _n_ [=][ 4] [∑] ( _X_ 2 _[µ]_ [−] _[X]_ _j_ _[µ]_ [)(] _[X]_ 2 _[ν]_ _n_ [−] _[X]_ _k_ _[ν]_ [)]     - 2 _η_ _[µν]_ _._ (7.23)
_j,k_ _∂X_ 2 _,j∂X_ 2 _n,k_ _∂X_ 2 _,_ 2 _n_

Now doing a gauge transformation and a rescaling in gluon 2 and 2 _n_, let us choose _X_ 2 _[µ]_ [=] _[ X]_ 1 _[µ]_
and _X_ 2 _[ν]_ _n_ [=] _[ X]_ 1 _[ν]_ [.] [So] [we] [get] [the] [following] [representation] [of] [A] _[µν]_ _n_ [:]

_∂_ [2] A _n_ _[∂]_ [A] _[n]_
A _[µν]_ _n_ [∝] [4] [∑] ( _X_ 1 _[µ]_ [−] _[X]_ _j_ _[µ]_ [)(] _[X]_ 1 _[ν]_ [−] _[X]_ _k_ _[ν]_ [)]     - 2 _η_ _[µν]_ _._ (7.24)
_j,k_ _∂X_ 2 _,j∂X_ 2 _n,k_ _∂X_ 2 _,_ 2 _n_

Now this is a particularly nice representation because it is such that N is zero:



_∂_ [2] A _n_ _[∂]_ [A] _[n]_
A _[µν]_ _n_ _[p][µ]_ [∝] 4 ∑( _X_ 1 _[µ]_ [−] _[X]_ _j_ _[µ]_ [)(] _[X]_ 1 _[ν]_ [−] _[X]_ _k_ _[ν]_ [)] - 2 _η_ _[µν]_
_j,k_ _∂X_ 2 _,j∂X_ 2 _n,k_ _∂X_ 2 _,_ 2
⎡⎢⎢⎢⎢⎣



_∂X_ 2 _,_ 2 _n_



( _X_ 3 − _X_ 1) _µ_
⎤⎥⎥⎥⎥⎦



_∂_ [2] A _n_
= 2 ∑( _X_ 3 _,j_ - _X_ 1 _,j_ )( _X_ 1 _[ν]_ [−] _[X]_ _k_ _[ν]_ [)] - 2( _X_ 3 _[ν]_ [−] _[X]_ 1 _[ν]_ [)] _[∂]_ [A] _[n]_
_j,k_ _∂X_ 2 _,j∂X_ 2 _n,k_ _∂X_ 2 _,_ 2



_∂X_ 2 _,_ 2 _n_



_∂_
= 2 ∑( _X_ 1 _[ν]_ [−] _[X]_ _k_ _[ν]_ [)]
_k_ _∂X_ 2 _n,k_



⎛
( _X_ 3 _,j_   - _X_ 1 _,j_ ) _[∂]_ [A] _[n]_
⎝ [∑] _j_ _∂X_ 2 _,j_



_∂X_ 2 _,j_



−2( _X_ 1 _[ν]_ [−] _[X]_ 3 _[ν]_ [)] _[∂]_ [A] _[n]_

_∂X_ 2 _,_ 2 _n_



(7.25)



+ 2( _X_ 1 _[ν]_ [−] _[X]_ 3 _[ν]_ [)] _[∂]_ [A] _[n]_



⎛ ⎞
( _X_ 3 _,j_   - _X_ 1 _,j_ ) _[∂]_ [A] _[n]_
⎝ [∑] _j_ _∂X_ 2 _,j_ ⎠

- **�������������������������������������** - **�������������������������������������** ��
=0



_∂X_ 2 _,_ 2 _n_
= 0 _,_



79


where the sum over _j_ vanishes because of gauge invariance. Therefore we found a representation of A _[µν]_ _n_ for which N = 0, and so in which the gluing becomes simply:



_∂_ [2] A _n_
Aglued ∝−A _n_ _[µν][η][µν]_ [∝] [2] [∑] ( _X_ 1 _[µ]_ [−] _[X]_ _j_ _[µ]_ [)(] _[X]_ [1] _[µ]_ [ −] _[X][kµ]_ [)] - _D_ _[∂]_ [A] _[n]_
_j,k_ _∂X_ 2 _,j∂X_ 2 _n,k_ _∂X_ 2 _,_ 2



_∂X_ 2 _,_ 2 _n_



(7.26)

_[∂]_ [A] _[n]_ _._

_∂X_ 2 _,_ 2 _n_



_∂_ [2] A _n_
= ∑( _X_ 1 _,j_ + _X_ 1 _,k_ - _Xj,k_ ) - _D_ _[∂]_ [A] _[n]_
_j,k_ _∂X_ 2 _,j∂X_ 2 _n,k_ _∂X_ 2 _,_ 2



This is finally our expression for gluing in the forward limit, written purely in terms

of _X_ variables.

Of course, this holds for gluing any gauge-invariant object in the forward limit, but

we now turn to the specific representations we give for _M_ in terms of integrals of forms of

_y_ variables, and translate this statement into a gluing rule for these forms. Let’s start by

defining the two forms we obtain by taking one scaffolding residue after the other:

Ω _s_ 1 _,_ 3 = Res _y_ 1 _,_ 3=0Ω [loop] 2 _n_ _[,]_ Ω _S_ = Res _y_ 1 _,_ 2 _n_ −1=0Ω _s_ 1 _,_ 3 _._ (7.27)


Then we have:

_∂_ A _n_ _∂_ Ω _S_
= ∫ = ∫ Res _y_ 1 _,_ 2 _n_ −1=0 ( _[∂]_ [Ω] _[s]_ [1] _[,]_ [3] )
_∂X_ 2 _,j_ _∂X_ 2 _,j_ _∂X_ 2 _,j_



⎛
= ∫ Res _y_ 1 _,_ 2 _n_ −1=0 ⎝ _s_ ≠( [∏] 1 _,_ 3)



d _ys_ ∏

_ys_ [2] _i_



d _yi_

× _[∂]_ [log][(] _[u]_ [2] _[,j]_ [)]
_yi_ [2] _∂y_ 1 _,_ 3



d _yi_




_[u]_ [2] _[,j]_

∏ _u_ _[X]_ _k,m_ _[k,m]_ [[] _[y]_ []∣]
_∂y_ 1 _,_ 3 ( _k,m_ )≠{(1 _,j_ ) _,_ (2 _,j_ )} _y_ 1 _,_ 3=0



⎞
⎠



_∂_ log( _u_ 2 _n,k_ )



_∂y_ 1 _,_ 2 _n_ −1



d _yi_

[∑( _X_ 2 _n,k_  - _X_ 2 _n_ −1 _,k_ ) _[∂]_ [log][(] _[u]_ [2] _[,j]_ [)]
_yi_ [2] _k_ _∂y_ 1 _,_ 3



d _yi_



= ∫ ∏
_s_ ≠{(1 _,_ 3) _,_
(1 _,_ 2 _n_ −1)}



d _ys_ ∏

_ys_ [2] _i_




[log][(] _[u]_ [2] _[,]_ [2] _[n]_ [)]
+ _[∂]_ [2] ] × ∏

_∂y_ 1 _,_ 3 _∂y_ 1 _,_ 2 _n_ −1 ( _k,m_ )≠{(1 _,j_ ) _,_ (2 _,j_ ) _,_
(1 _,k_ ) _,_ (2 _n_ −1 _,k_ )}



_∂y_ 1 _,_ 3



_u_ _[X][k,m]_ _,_
_k,m_ [[] _[y]_ []∣]
_y_ 1 _,_ 3= _y_ 1 _,_ 2 _n_ −1=0



(7.28)
which further taking a derivative on _X_ 2 _n,k_, gives



_∂_ [2] A _n_ = ∫ ∏
_∂X_ 2 _n,k∂X_ 2 _,j_ _s_ ≠{(1 _,_ 3) _,_
(1 _,_ 2 _n_ −1)}



d _ys_ ∏

_ys_ [2] _i_



d _yi_



d _yi_ ∏

_yi_ [2] ( _k,m_ )≠{(1 _,j_ ) _,_ (2 _,j_ ) _,_
(1 _,k_ ) _,_ (2 _n_ −1 _,k_ )}



_u_ _[X][k,m]_
_k,m_ [[] _[y]_ []]




- **����������������������������������������������������������������������������** - **����������������������������������������������������������������������������** (KN)˜



(7.29)



× ( _[∂]_ [log][(] _[u]_ [2] _[,j]_ [)]

_∂y_ 1 _,_ 3



_∂_ log( _u_ 2 _n,k_ )

)∣ _,_
_∂y_ 1 _,_ 2 _n_ −1 _y_ 1 _,_ 3= _y_ 1 _,_ 2 _n_ −1=0



so we can summarize the gluing rule as follows:

AGlued = ∫∑ ( _X_ 1 _,j_ + _X_ 1 _,k_  - _Xj,k_ ) _[∂]_ [log][ (] _[u]_ [2] _[,j]_ [)]
_j,k_ _∂y_ 1 _,_ 3


80



_∂_ log( _u_ 2 _n,k_ ) ˜ _∂_ Ω _S_

× (KN) − _D_ ⋅ _._ (7.30)
_∂y_ 1 _,_ 2 _n_ −1 _∂X_ 2 _,_ 2 _n_


We finally translate this result using the variables of the loop-cut we want to compute,

and find that the glued form is given by:



⎤⎥⎥⎥⎥⎥⎥⎥⎦������������������ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



_∂_ log _usR,k_

_∂y_ 1 [′] _,p_



⎡⎢⎢⎢⎢⎢⎢⎢⎣



∑
_j_ ∈{2 _,...,_ 1 [′] } _,_
_k_ ∈{1 _,...,_ 2 _n_ }



Ω [2] Glued _[n]_ [=∏]
_i_



d _yi_

_yi_ [2] ∏ _u_ _[X]_ _C_ _[C]_



( _Xp,j_ + _Xp,k_ - _Xj,k_ ) _[∂]_ [log] _[ u][s][L][,j]_

_∂y_ 1 _,p_



_∂_ Ω _S_

    - _D_ ⋅ _,_
_∂XsL,sR_

(7.31)
where _yi_ are now all remaining variables in the triangulation (other than the two scaffolding
ones we extracted the residue) and _C_ stands for the curves living in the smaller surface,
obtained after taking the scaffolding residue. Ω _S_ is now the form resulting from taking
both scaffolding residues that now correspond to _y_ 1 _,p_ = _y_ 1 [′] _,p_ = 0. As previously we can
express this object in terms of derivatives of the lower-point tree amplitude as follows:

Ω [Glued] 2 _n_ = ∑ ( _Xj,p_ + _Xk,p_      - _Xj,k_ ) _∂_ [2] A [S] _n_ +2      - _D_ _[∂]_ [A] _n_ [tree] +2 ; (7.32)
_j,k_ _∂Xj,sL∂Xk,sR_ _∂XsL,sR_

Now, in this formula we are assuming _Xj,k_ = _Xk,j_, since in the tree side these variables
are indeed the same. Now crucially the glued object is meant to match the result we get

from the cut of the one-loop integrand, which if we define in terms of surface kinematics
has _Xj,k_ ≠ _Xk,j_ . So just like in the tree-loop cut, we want to derive a generalization of
(7.32) which allow us to match with the object defined in terms of surface kinematics.


**7.4** **Surface** **kinematics** **and** **the** **loop-cut**


Manifestly in equation (7.31), the only part that is sensitive to surface kinematics is the
term _Xj,k_, as well as the index range for _j,k_ is correct. From the loop-cut side, we know
that all the curves _Xj,k_ entering must correspond to curves that intersect _Y_ 1. Let’s assume
_j_ < _k_, then _Xj,k_ is the curve that goes above the puncture, while _Xk,j_ goes below the
puncture. So the self-intersection one version of _Xj,k_ and the self-intersection zero of _Xk,j_
both cross _Y_ 1 and thus contribute to the loop-cut. So on the loop side, taking the residue
on _y_ 1 = 0 we get the contributions from these curves _u_ [(] _j,k_ [1][)] [and] _[u]_ [(] _k,j_ [0][)][.] [Just] [like] [we] [saw] [on] [the]
tree-loop cut, it’s simple to show that the derivatives of these _u_ -variables factorize nicely

into derivatives of _u_ ’s of the tree-problem as follows:



_∂_ log _u_ [(][1][)]
_j,k_
∣ = _[∂]_ [log] _[ u][j,s][R]_
_∂y_ 1 _y_ 1=0 _∂y_ 1 [′] _,p_

_∂_ log _u_ [(][0][)]
_k,j_
∣ = _[∂]_ [log] _[ u][k,s][R]_
_∂y_ 1 _y_ 1=0 _∂y_ 1 [′] _,p_




_[ u][j,s][L]_

∣
_∂y_ 1 _,p_ _y_ 1 _,p_ =0




[log] _[ u][j,s][R]_

∣ × _[∂]_ [log] _[ u][k,s][L]_
_∂y_ 1 [′] _,p_ _y_ 1′ _,p_ =0 _∂y_ 1 _,p_


[log] _[ u][k,s][R]_

∣ × _[∂]_ [log] _[ u][j,s][L]_
_∂y_ 1 [′] _,p_ _y_ 1′ _,p_ =0 _∂y_ 1 _,p_




_[ u][k,s][L]_ ∣ _,_

_∂y_ 1 _,p_ _y_ 1 _,p_ =0



(7.33)



81


So from here, we see that to follow surface kinematics (7.31) becomes



(7.34)



⎤⎥⎥⎥⎥⎦������������ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



∑ ( _Xp,j_ + _Xp,k_ - _Xj,k_ ) _[∂]_ [log] _[ u][j,s][R]_
_j,k_ _∂y_ 1 [′] _,p_
⎡⎢⎢⎢⎢⎣



_∂_ log _uk,sL_

_∂y_ 1 _,p_



Ω [2] Glued _[n]_ [=∏]
_i_



d _yi_

_yi_ [2] ∏ _u_ _[X]_ _C_ _[C]_



_∂_ Ω _S_

    - _D_ ⋅ _,_
_∂XsL,sR_

where now _j,k_ ∈(1 _,_ 2 _,_ ⋯ _,_ 2 _n,_ 1 [′] ), and in the end we set 1 [′] → 1, and we get _Xi,i,Xi_ +1 _,i,Xi,i_ +1 ≠
0. In terms of derivatives of the tree object we can write:

Ω [2] Glued _[n]_ [= ∑] [( _Xj,p_ + _Xk,p_ - _Xj,k_ ) _∂_ [2] A [S] _n_ +2 ]∣ - _D_ _[∂]_ [A] _n_ [S] +2 ; _j,k_ ∈(1 _,_ 2 _,_ ⋯ _,_ 2 _n,_ 1 [′] ) _._
_j,k_ _∂Xj,sR∂Xk,sL_ 1 [′] →1 _∂Xx_ [′] _,x_

(7.35)

Now that we have the glued object expressed in terms of the most general kinematics,
_Xi,j_ ≠ _Xj,i_, let’s proceed to show that the result we get from the residue of the surface loop
integrand matches this gluing.


**7.5** **Loop-cut** **matching** **with** **Tree-gluing**


To do this we start by rewriting the tree-level gluing on a way that facilitates the matching

of each term separately as follows:



⎡⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣




- ∑ _Xj,k_ _∂_ log _usL,k_
_j,k_ ∈{2 _,...,_ 2 _n_ } _∂y_ 1 _,p_



_j,k_ ∈{2 _,...,_ 2 _n_ } _∂y_ 1 _,p_ _∂y_ 1 [′] _,p_

- **������������������������������������������������������������** **�����������������������������������������������������������** ��
(††)



_∂_ log _usR,j_



_∂_ Ω _S_
Ω [2] Glued _[n]_ [= −] _[D]_ [⋅]

     - **��������������** _∂X_      - _s_ **���������������** _L,sR_
(†)



+ ∏
_i_



d _yi_

_yi_ [2] ∏ _u_ _[X]_ _C_ _[C]_



_∂y_ 1 _,p_



+ ∑ _Xp,j_ ⎛ _∂_ log _usL,j_
_j_ ∈{2 _,...,_ 2 _n_ } ⎝ _∂y_ 1 _,p_



∑ _Xp,j_ ⎛ _∂_ log _usL,j_ ∑ _∂_ log _usR,k_ + _[∂]_ [log] _[ u][s][R][,j]_ ∑ _∂_ log _usL,k_ ⎞
_j_ ∈{2 _,...,_ 2 _n_ } ⎝ _∂y_ 1 _,p_ _k_ ∈{1 _,...,_ 2 _n_ } _∂y_ 1 [′] _,p_ _∂y_ 1 [′] _,p_ _k_ ∈{2 _,...,_ 1 [′] } _∂y_ 1 _,p_ ⎠

- **�������������������������������������������������������������������������������������������������������������������������������������������������** **�������������������������������������������������������������������������������������������������������������������������������������������������**
(†††)



_∂_ log _usR,k_




_[ u][s][R][,j]_ ∑

_∂y_ 1 [′] _,p_ _k_ ∈{2 _,...,_ 1 [′] }



_usL,j_

∑
_∂y_ 1 _,p_ _k_ ∈{1 _,...,_ 2 _n_ }



_usR,k_

+ _[∂]_ [log] _[ u][s][R][,j]_
_∂y_ 1 [′] _,p_ _∂y_ 1 [′] _,p_



_∂_ log _usL,k_



_∂y_ 1 _,p_



_∂_ log _uk,sR_




- ∑ _X_ 1 _,k_ _∂_ log _u_ 1 _,sR_
_k_ ∈{2 _,...,_ 2 _n_ } _∂y_ 1 [′] _,p_



_∂_ log _uk,sL_



_uk,sL_

+ _Xk,_ 1′ _[∂]_ [log] _[ u][s][L][,]_ [1][′]
_∂y_ 1 _,p_ _∂y_ 1 _,p_



_k_ ∈{2 _,...,_ 2 _n_ } _∂y_ 1 [′] _,p_ _∂y_ 1 _,p_ _∂y_ 1 _,p_ _∂y_ 1 [′] _,p_

- **������������������������������������������������������������������������������������������������������������������** - **�������������������������������������������������������������������������������������������������������������������**
(††††)



_∂y_ 1 [′] _,p_



_∂y_ 1 _,p_




- _X_ 1 _,_ 1 [′] ( _[∂]_ [log] _[ u][s][L][,]_ [1][′]



_usR,_ 1

)
_∂y_ 1 [′] _,p_



_∂_ log _usR,_ 1



⎤⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦



_,_



�������������������������� _y_ 1 _,p_ = _y_ 1′ _,p_ =0



_∂y_ 1 _,p_




- **��������������������������������������������������** - **��������������������������������������������������** (†††††)



(7.36)
where we are setting _X_ 1 _,j_ = _X_ 1′ _,j_ . Our goal now is to show the different terms agree with
the loop cut result, up to a possible total derivative. Let’s look at what the loop-cut result

looks like before proceeding.


82


As explained before, in the loop integrand we include all the curves up to self-intersection
one. So by taking the residue on _Y_ 1, we are effectively taking the residue of the integrand
at _y_ 1 = 0, which leads to:



_,_
������������� _y_ 1 _,p_ = _y_ 1′ _,p_ =0



Res _y_ 1=0Ω [loop] 2 _n_ =∏
_i_



d _yi_



d _yi_

_yi_ [2] ∏ _u_ _[X]_ _C_ _[C]_



∑ _Yj_ _∂_ log _uYj_
⎡⎢⎢⎢⎢⎣ _j_ ∈{2 _,...,_ 2 _n_ } _∂y_ 1



_uYj_ + ∑ _Xj,k_ _∂_ log _u_ [(] _j,k_ [1][)] + _Xk,j_ _∂_ log _u_ [(] _k,j_ [0][)]

_∂y_ 1 _j_ ≤ _k_ _∂y_ 1 _∂y_ 1



_∂_ log _u_ [(] 1 [1] _,j_ [)] _∂_ log _u_ [(] _j,_ [0] 1 [)] _[u]_ _j,_ [(][1] 1 [)] _∂_ log _u_ [(] 1 [0] _,_ 1 [)] _[u]_ 1 [(][1] _,_ 1 [)]
+ ∑ _X_ 1 _,j_ + _Xj,_ 1 + _X_ 1 _,_ 1 - ∆
_j_ ∈{2 _,_ ⋯ _,_ 2 _n_ } _∂y_ 1 _∂y_ 1 _∂y_ 1 ⎤⎥⎥⎥⎥⎦



(7.37)
where once more we are keeping full surface kinematics. So, using ∆ = 1− _D_, we can rewrite
(7.37) as follows:



_∂_ log _u_ [(][1][)] _∂_ log _u_ [(][0][)]
_j,k_ _k,j_
∑ _Xj,k_ + _Xk,j_
_j_ ≤ _k_ _∂y_ 1 _∂y_ 1

 - **�������������������������������������������������������** **�������������������������������������������������������**

⎡⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣ (⋆⋆)



Res _y_ 1=0Ω [loop] 2 _n_ = _D_ ⋅∏
_i_



d _yi_



d _yi_

_yi_ [2] ∏ _u_ _[X]_ _C_ _[C]_



d _yi_

_yi_ [2] ∏ _u_ _[X]_ _C_ _[C]_



+ ∏
_i_




 - **�������������������������** - _i_ **�������������������������** ��
(⋆)



+ ∑ _Yj_ _∂_ log _uYj_
_j_ ∈{2 _,...,_ 2 _n_ } _∂y_ 1

 - **������������������������������** **������������������������������** (⋆⋆⋆)



_∂_ log _u_ [(] 1 [1] _,j_ [)] _∂_ log _u_ [(] _j,_ [0] 1 [)] _[u]_ _j,_ [(][1] 1 [)]
+ ∑ _X_ 1 _,j_ + _Xj,_ 1
_j_ ∈{2 _,_ ⋯ _,_ 2 _n_ } _∂y_ 1 _∂y_ 1

  - **�������������������������������������������������������������������������**  - **��������������������������������������������������������������������������**
(⋆⋆⋆⋆)



⎛
+ _X_ 1 _,_ 1 ⎜⎝



⎛ _∂_ log _u_ 1 _,_ 1 _∂_ log _u_ 1 [(][1] _,_ 1 [)] ⎞
_X_ 1 _,_ 1 ⎜ + ⎟
⎝ _∂y_ 1 _∂y_ 1 ⎠

- **����������������������������������������������** **����������������������������������������������** (⋆⋆⋆⋆⋆)



_u_ 1 _,_ 1 + _∂_ log _u_ 1 [(][1] _,_ 1 [)]

_∂y_ 1 _∂y_ 1



_∂_ log _u_ 1 _,_ 1



−1



_._



⎤⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦



������������������������������ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



(7.38)
From figures 33 and 34, it’s obvious that _Yj_ on the loop side maps to _Xp,j_ on the tree
glue side. In addition, the choice of triangulation for the loop/tree problems makes it clear
that ∏ _i_ d _yyi_ [2] _i_ [∏] _[u]_ _C_ _[X][C]_ is the same for both of them.

The approach we will follow is to analyze each term separately and understand whether

they match directly or differ by a total derivative. The matching works quite intricately,

and we devote the appendix D for more details, here we simply summarize the results.
Both (⋆) and (⋆⋆) can be shown to match (†) and (††), respectively. The same is
not true for the remaining three terms, however, the difference will be shown to be the

following rather non-trivial total derivative:



∏ _k_ ∈{1 _,...,m_ −1} _up,ku_ 1 [′] _,k_ ⎞

_u_ 1 _,p_ ∏ _j_ ∈{2 _,...,_ 2 _n_ } _u_ [2] _p,j_ ∏ _C_ _u_ _[X]_ _C_ _[C]_ ⎠ [∣] _y_ 1 _,p_ = _y_ 1′ _,p_ =0 _._ (7.39)




- _[∂]_

_∂yt_



⎛
⎝ [∏] _y_ [1] _i_ [2]



It is very pleasing that the total derivative is with respect to the only variable we could

possibly have “local” to the triangulation.


83


This establishes the consistency of our curve integral for scalar-scaffolded gluons, by

showing that the loop-cut and the tree-level gluing agree up to a total derivative. We stress

again that while this argument is strictly valid at 1-loop, its quite “local” character makes

it likely that it can be extended to any number of loops.


**8** **Outlook**


The first concrete example for reformulating the fundamental physics of scattering ampli
tudes in a new mathematical language, based on elementary but deep ideas in combinatorics

and geometry, arose ten years ago in the content of the positive Grassmannian [11] and
the amplituhedron [1] for planar N = 4 SYM. The past decade has seen a succession of
developments pushing away from this very special theory and closer to the physics of Yang
Mills theory in the real world [5, 7–9, 12, 13]. This program has been motivated by the

belief that more magic–not less!–should reveal itself as we move from toy models towards

describing the universe we actually live in.

We believe that with the results reported in this paper, we have entered a new phase

in this adventure, in which combinatorial geometry in kinematic space is finally seen to

directly describe major aspects of the world we see outside our windows. In one fell swoop,

we have freed ourselves from the shackles of supersymmetry and integrability and “dlog

forms”, along the way discovering a startling unity between non-supersymmetric gluons,

pions, and the simplest theory of colored scalars.

As such there are a huge number of avenues for exploration, both in better under
standing the conceptual origins and underpinnings of our proposal, as well as in seeking

to propel us ever closer to describing all aspects of real-world physics from this new point

of view. Instead of making a long list of these entirely obvious big questions, we close

by mentioning a small number of directions of exploration immediately following from the

developments here, which we hope to report on in the near future.

To begin with, we have left a number of important loose ends that need to be fully

understood to precisely define our proposal at all orders in the topological expansion. We

have emphasized that the dependence on dimensionality _D_ arises through the product of

the closed ∆curves wrapping around punctures, keeping one self-intersection per puncture.

This is a perfectly well-defined proposal for the planar diagrams contributing to single-trace

amplitudes, but starting with the torus corrections at two loops there are many kinds of

closed ∆curves that can contribute, and the precise statement about the choice of ∆’s

and exponents must be understood. Similarly, the precise statement about ∆’s for multi
trace amplitudes must be determined. We have checked that in the simplest case of 1-loop

annulus corrections to double-trace amplitudes, where there is a unique closed ∆curve
separating the two boundaries, the obvious choice of ∆with the same exponent (1 − _D_ )
correctly matches leading singularities, so we expect a consistent choice is possible at all

orders in the topological expansion. Also, our proof for the equality of the loop-cut and
forward limit was strictly only for the one-loop cut → tree-level forward limit. The character
of the argument was however very “local” on the surface, and we expect that it can be


84


extended to all orders– as supported by the successful checks of leading singularities at two

loops– but it is important to establish this definitively.

Perhaps the most pressing question is learning how to effectively extract the low-energy,

field-theory limit of the amplitudes from our stringy integrals. This is more challenging
than the analogous problem for the Tr _ϕ_ [3] theory, where the _dy_ / _y_ singularity makes it easy
to extract the low-energy limit of the amplitudes for _α_ [′] _X_ ≪ 1, localizing to logarithmic
divergences as ∣log _y_ ∣→∞. This can be easily computed by “tropicalizing” the _u_ variables,
giving a global Schwinger parametrization for the full amplitude directly in the field theory

limit. This procedure does not work straightforwardly for our scaffolded gluons, where
the _dy_ / _y_ [2] form has power-law divergences and the integral must be defined by analytic
continuation, even at tree-level. In [34] we will report on an elementary and direct way of

extracting the field theory limit, via a “cone-by-cone” analysis of the singular behavior of

the integrand. This will already expose a number of surprising facts about gluon ampli
tudes. For instance, it will allow us to establish what we call the “mesh expansion” for tree

amplitudes, in terms of interesting sums associated with _all_ facets of the ABHY associa
hedron. Extremes of this expansion can be described very efficiently either by closed-form

formulae at all multiplicity, or by novel “tropical” expressions. But we are still seeking

an efficient “tropical” representation of the _full_ gluon amplitudes, as a counterpart of the
existing “tropical” formulae for Tr _ϕ_ [3] theory at all orders in the topological expansion.

We have emphasized that our surface picture for gluons provides a solution to a long
standing difficulty of making sense of “nice” integrands for non-supersymmetric Yang-Mills

theories, by giving a natural way of treating the infamous “1/0” difficulties associated with

tadpoles and massless external bubbles [16]. Quite apart from its conceptual importance

especially at “stringy” level, the elementary mechanism by which tadpoles/massless ex
ternal bubbles are naturally dealt with suggests a recursive procedure for computing inte
grands for Yang-Mills theory [17] in any number of dimensions, in the planar limit where

integrands are well-defined. We have computed integrands determined by this recursion

through a number of one- and two-loop examples, which have passed all obvious consis
tency checks [17]. Optimistically an all-loop recursion for non-supersymmetric Yang-Mills

theory in the planar limit may be at hand, as a counterpart to the very different recursion
based on BCFW recursion for planar N = 4 SYM [38].
We have seen that the extremely simple and purely kinematical idea of thinking about

particles with spin in the “scalar-scaffolding” language allows highly non-trivial hidden

features of gluon amplitudes to be brought to light. As such it is clearly interesting to

study more general spinning amplitudes in this language. Clearly tree-level gravity ampli
tudes can be described in exactly the same 2 _n_ scalar scaffolding language, with an obvious

extension of the notions of multilinearity and gauge invariance. Their stringy integrands

are again a single term, arising as usual from the mod-square of the scalar-scaffolded gluon

integrand. Amplitudes for particles of any mass and spin, including the string resonances,

can also be kinematically described using scalar scaffolding. The surprise for gluons is that

the “dynamics” can be captured by a simple kinematic shift/monomial in the _u_ variables.
It would therefore be fascinating to look for an analog of our (∏ _ue,e_ /∏ _uo,o_ ) factor that
might describe the scattering of general string states.


85


Finally, while our new description for scalar-scaffolded gluons works in any number of
dimensions, we know amplitudes in _D_ = 4 spacetime dimensions are not only particularly
important, but should have extra simplicity reflected in the Abelian nature of the little

group and the natural decomposition of the amplitude into helicity sectors. In fact we ex
pect the behavior of the amplitude _near_ four dimensions to also be significant; for instance,

it has long been appreciated that the enigmatic “rational terms” in loop amplitudes are
determined by “ _ϵ_ / _ϵ_ ” effects in dimensional regularization, and hence are sensitive to the
behavior of the integrand close to four dimensions. There is a natural way to approach this
physics, parametrizing the _X_ kinematic data in _D_ = 4 using momentum twistor variables
and considering general perturbations _ϵδX_ as an expansion in _ϵ_ .

This also gives a new avenue for trying to understand the lingering mystery of having an

embarrassment of riches in describing the dynamics of gluons using combinatorial geometry.

In four dimensions and with maximal supersymmetry, we have the story of the positive

Grassmannian [11] and the amplituhedron [1], while now in general dimensions and with

no supersymmetry, we have the scalar-scaffolded gluons arising from the combinatorics of
surfaces. Obviously, in _D_ = 4 these two stories must be connected. Perhaps the closest
point where a technical connection can be made is at the level of leading singularities,

where we have two different formulations as the residues of a master differential form, in the

Grassmannian and the binary geometry of surfaces respectively. Of course, the two stories

also differ crucially at the very outset, by the way they describe the scattering kinematics.

In the positive Grassmannian and amplituhedron, the external data is labelled “one-particle

at a time”, by specifying momentum(-twistor) variables for each particle, while in the
scaffolding picture it is crucial that the data is specified in terms of variables _Xij_ encoding
Lorentz-invariants labelled by _pairs_ of points/particles. An understanding of the approach
to _D_ = 4 from the scalar-scaffolding story, encoding the kinematic data in momentumtwistor variables, should help bring the connection between these two fascinating worlds

closer to light.


**Acknowledgments**


It is our pleasure to thank Hadleigh Frost, Sebastian Mizera, Pierre-Guy Plamondon, Giulio

Salvatori, and Hugh Thomas for numerous inspiring discussions. The work of N.A.H. is

supported by the DOE (Grant No. DE-SC0009988), by the Simons Collaboration on

Celestial Holography, and further support was made possible by the Carl B. Feinberg

cross-disciplinary program in innovation at the IAS. The work of Q.C. is supported by

the National Natural Science Foundation of China under Grant No. 123B2075. The work

of C.F. is supported by FCT/Portugal (Grant No. 2023.01221.BD). The work of S.H.

has been supported by the National Natural Science Foundation of China under Grant No.

12225510, 11935013, 12047503, 12247103, and by the New Cornerstone Science Foundation

through the XPLORER PRIZE.


86


**A** **Scaffolding** **residues** **using** **worldsheet** **variables** **of** **bosonic** **string**


In sec. 4 we have given elegant and practical formulas for the _n_ -gluon amplitudes obtained

from scaffolding 2 _n_ -scalar amplitudes (which are special components of 2 _n_ -gluon ampli
tudes) in bosonic string theory; we have also shown a consistency check from 4 _n_ scalars to

2 _n_ gluons and then 2 _n_ scalars, which concludes the tree-level story.

However, we can also directly compute scaffolding residue of 2 _n_ -scalar amplitudes using

worldsheet variables, which gives again the _n_ -gluon correlator of bosonic-string integrand

as shown in (4.1). Our starting point is:



⟨∏ [2] _a_ _[n]_ =1 _[e][ip][a]_ [⋅] _[X]_ [(] _[z][a]_ [)][⟩]

_,_ (A.1)
_z_ 12 [2] _[z]_ 34 [2] ~~[⋯]~~ _[z]_ 2 [2] _n_ −1 _,_ 2 _n_



I(12)⋯(2 _n_ −12 _n_ ) = ∫ SL _d_ ~~(~~ [2] 2 _[n]_ _,z_ R ~~)~~



_z_ 12 [2] ∏ _[z]_ 34 [2] _i_ < _j_ ~~[⋯]~~ _z_ _[z]_ _i,j_ [2] 2 [2] _[p]_ _n_ _[i]_ - [⋅] _[p]_ 1 _[j]_ _,_ 2 _n_ = ∫ SL _d_ ~~(~~ [2] 2 _[n]_ _,z_ R ~~)~~



where we have rewritten the Koba-Nielsen factor in terms of the OPE of vertex operators.
It is important to make the special choice _ϵi_ = _p_ 2 _i_ −1 (recall _qi_ _[µ]_ [=] _[ p]_ 2 _[µ]_ _i_ −1 [+] _[p]_ 2 _[µ]_ _i_ [):] [as] [we] [have]
discussed one can check that _ϵa_ ⋅ _ϵb_ ∝ _c_ 2 _a_ −1 _,_ 2 _b_ −1 in _Wa,b_, and for a given _a_, the collection of
_ϵa_ ⋅ _qb_ for _b_ ≠ _a_ is equivalent to those _X_ 2 _a,j_ - _X_ 2 _a_ −1 _,j_ for all _j_ . Taking the scaffolding residues
corresponds to taking the residues at _zi,i_ +1 = 0 for odd _i_, in terms of the _z_ variables. The
residue _z_ 12 = 0 is given by taking the derivative of the vertex operator and setting _z_ 1 = _z_ 2:



2 _n_
_∂z_ 1 ⟨∏ _e_ _[ip][a]_ [⋅] _[X]_ [(] _[z][a]_ [)] ⟩∣
_a_ =1



2 _n_
= ⟨ _ip_ 1 ⋅ _∂z_ 2 _X_ ( _z_ 2) _e_ _[ip]_ [1] _[,]_ [2][⋅] _[X]_ [(] _[z]_ [2][)] ∏ _e_ _[ip][a]_ [⋅] _[X]_ [(] _[z][a]_ [)] ⟩ _._ (A.2)
_z_ 1= _z_ 2 _a_ =3



Remember the special choice _ϵa_ = _p_ 2 _a_ −1, and _qa_ = _p_ 2 _a_ −1 + _p_ 2 _a_ = _p_ 2 _a_ −1 _,_ 2 _a_, after scaffolding
the 2 _n_ -scalar correlator becomes the _n_ -gluon correlator


_n_ _n_
⟨∏ _ip_ 2 _a_ −1 ⋅ _∂z_ 2 _aX_ ( _z_ 2 _a_ ) _e_ _[ip]_ [2] _[a]_ [−][1] _[,]_ [2] _[a]_ [⋅] _[X]_ [(] _[z]_ [2] _[a]_ [)] ⟩= ⟨∏ _iϵa_ ⋅ _∂z_ 2 _aX_ ( _z_ 2 _a_ ) _e_ _[iq][a]_ [⋅] _[X]_ [(] _[z]_ [2] _[a]_ [)] ⟩ _,_ (A.3)
_a_ =1 _a_ =1

with the relabelling the worldsheet coordinates _z_ 2 _a_ → _za_ . Therefore, the 2 _n_ -scalar bosonic
string amplitude becomes the _n_ -gluon bosonic string amplitude by scaffolding:


_n_
scaffolding ∏ _[n]_ _a_ =1 _[dz][a]_
I(12)⋯(2 _n_ −12 _n_ ) �����→∫ vol SL ~~(~~ 2 _,_ R ~~)~~ [⟨] _a_ ∏=1 _iϵa_ ⋅ _∂zaX_ ( _za_ ) _e_ _[iq][a]_ [⋅] _[X]_ [(] _[z][a]_ [)] ⟩ _._ (A.4)


Having made connections with the more familiar worldsheet variables, we can also

repeat such a derivation for closed-string and conclude that the _n_ -graviton scattering am
plitudes of bosonic string is again given by scaffolding residue of 2 _n_ -scalar amplitudes,

which are “mod-square” closed-stringy integrals over “complex binary geometries” [10].

Obviously, such a “mod-square” 2 _n_ -scalar integral for closed-string is related to those for

open-string via Kawai-Lewellen-Tye (KLT) relations [40]. In the field-theory limit, they

become double copy relations [41] between gravity and gluon amplitudes, now written in

this scalar-scaffolding language.


**B** **Complete** **results** **for** 1 **-loop** 4 **-point** **box** **leading** **singularity**

We present the complete result of 1-loop 4-point box leading singularity (with _Y_ 1 = _Y_ 2 =
_Y_ 3 = _Y_ 4 = 0) which contains terms with mass dimension _X_ _[m]_ for _m_ = 4 _,_ 5 _,_ 6 _,_ 7 _,_ 8. These


87



_n_ _n_
⟨∏ _ip_ 2 _a_ −1 ⋅ _∂z_ 2 _aX_ ( _z_ 2 _a_ ) _e_ _[ip]_ [2] _[a]_ [−][1] _[,]_ [2] _[a]_ [⋅] _[X]_ [(] _[z]_ [2] _[a]_ [)] ⟩= ⟨∏ _iϵa_ ⋅ _∂z_ 2 _aX_ ( _z_ 2 _a_ ) _e_ _[iq][a]_ [⋅] _[X]_ [(] _[z]_ [2] _[a]_ [)] ⟩ _,_ (A.3)
_a_ =1 _a_ =1


terms correspond to the pure Yang-Mills leading singularity and those with 1 _,_ 2 _,_ 3 and 4
insertions of _F_ [3] vertices, respectively. The pure Yang-Mills leading singularity reads:




- [(][∆] [+][ 1][)]




[1] 3 _,_ 7 _[X]_ 1 [2] _,_ 5 [+] [1]

4 _[X]_ [2] 2




[ 1]

_Y_ 2 _Y_ 4 _Y_ 6 _Y_ 8 − 2 _Y_ 6 _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 5 + [1]
4 4




[1] 1 _,_ 5 [−] _[X]_ [2] _[,]_ [8] _[X]_ [3] _[,]_ [6] _[X]_ 1 [2] _,_ 5 [−] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5

2 _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [6] _[X]_ [2]



+ _X_ 2 _,_ 8 _X_ 3 _,_ 7 _X_ 1 [2] _,_ 5 [+] [1]




[1] 1 _,_ 5 [−] _[X]_ [1] _[,]_ [6] _[X]_ 3 [2] _,_ 7 _[X]_ [1] _[,]_ [5] [+][ 2] _[Y]_ [6] _[Y]_ [8] _[X]_ [2] _[,]_ [4] _[X]_ [1] _[,]_ [5] [−] _[Y]_ [4] _[Y]_ [8] _[X]_ [2] _[,]_ [6] _[X]_ [1] _[,]_ [5] [+][ 2] _[Y]_ [4] _[Y]_ [8] _[X]_ [2] _[,]_ [7] _[X]_ [1] _[,]_ [5]

2 _[X]_ [2] _[,]_ [8] _[X]_ [4] _[,]_ [6] _[X]_ [2]




- _Y_ 8 _X_ 2 _,_ 4 _X_ 3 _,_ 6 _X_ 1 _,_ 5 + _Y_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 6 _X_ 1 _,_ 5 − _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 6 _X_ 1 _,_ 5 − _Y_ 4 _X_ 2 _,_ 8 _X_ 3 _,_ 6 _X_ 1 _,_ 5 + _X_ 1 _,_ 4 _X_ 2 _,_ 8 _X_ 3 _,_ 6 _X_ 1 _,_ 5

- _Y_ 2 _Y_ 6 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + _Y_ 6 _X_ 2 _,_ 4 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + _Y_ 8 _X_ 2 _,_ 4 _X_ 3 _,_ 7 _X_ 1 _,_ 5 − _Y_ 4 _X_ 2 _,_ 6 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 _,_ 5
+ _X_ 1 _,_ 6 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 _,_ 5 − _X_ 1 _,_ 4 _X_ 2 _,_ 8 _X_ 3 _,_ 7 _X_ 1 _,_ 5 − _X_ 1 _,_ 6 _X_ 2 _,_ 8 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + _Y_ 4 _X_ 2 _,_ 6 _X_ 3 _,_ 8 _X_ 1 _,_ 5 − _X_ 2 _,_ 5 _X_ 3 _,_ 6 _X_ 3 _,_ 8 _X_ 1 _,_ 5



+ _X_ 1 _,_ 6 _X_ 3 _,_ 7 _X_ 3 _,_ 8 _X_ 1 _,_ 5 + _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 3 [2] _,_ 7 [−] _[X]_ [1] _[,]_ [6] _[X]_ [2] _[,]_ [4] _[X]_ 3 [2] _,_ 7 [+] [1]




[1] 3 _,_ 7 [+] _[ Y]_ [4] _[Y]_ [8] _[X]_ [1] _[,]_ [6] _[X]_ [2] _[,]_ [5] [−] [2] _[Y]_ [4] _[Y]_ [8] _[X]_ [1] _[,]_ [6] _[X]_ [2] _[,]_ [7]

2 _[X]_ [1] _[,]_ [6] _[X]_ [2] _[,]_ [5] _[X]_ [2]



+ _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 6 + _Y_ 4 _Y_ 8 _X_ 2 _,_ 7 _X_ 3 _,_ 6 − _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 6 + 2 _Y_ 4 _Y_ 8 _X_ 1 _,_ 6 _X_ 3 _,_ 7 − _Y_ 8 _X_ 1 _,_ 6 _X_ 2 _,_ 4 _X_ 3 _,_ 7

- _Y_ 6 _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 7 − _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 7 + _Y_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 7 − _Y_ 4 _Y_ 8 _X_ 2 _,_ 6 _X_ 3 _,_ 7 + _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 6 _X_ 3 _,_ 7

- _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 7 _X_ 3 _,_ 7 − _Y_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 8 _X_ 3 _,_ 7 + _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 8 _X_ 3 _,_ 7 + _Y_ 6 _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 8 − _Y_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 8



+ _X_ 1 _,_ 6 _X_ 2 _,_ 4 _X_ 3 _,_ 7 _X_ 3 _,_ 8 − _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 7 _X_ 3 _,_ 8 + [1]




[1] [1]

4 _[X]_ [1] _[,]_ [6] _[X]_ [2] _[,]_ [5] _[X]_ [3] _[,]_ [8] _[X]_ [4] _[,]_ [7][ +] 4



4 _[X]_ [1] _[,]_ [4] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [6] _[X]_ [5] _[,]_ [8]



+ (cyclic _,i_ → _i_ + 2 _,i_ + 4 _,i_ + 6) _,_
(B.1)
which, by setting ∆ = 1 − _D_, agrees with the well-known _D_ -dimensional result ( _c.f._ [39])
once we translate it to polarizations and momenta.
Those with 1 _,_ 2 and 3 insertions of _F_ [3] vertices are:



_Y_ 2 _X_ 3 [2] _,_ 7 _[X]_ 1 [2] _,_ 5 [−] [2] _[Y]_ [4] _[Y]_ [6] _[X]_ [2] _[,]_ [7] _[X]_ 1 [2] _,_ 5 [+][ 2] _[Y]_ [4] _[Y]_ [6] _[X]_ [2] _[,]_ [8] _[X]_ 1 [2] _,_ 5 [+] _[ Y]_ [4] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [6] _[X]_ 1 [2] _,_ 5 [−] _[Y]_ [4] _[X]_ [2] _[,]_ [8] _[X]_ [3] _[,]_ [6] _[X]_ 1 [2] _,_ 5 [+][ 2] _[Y]_ [4] _[Y]_ [6] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5

- _Y_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 [2] _,_ 5 [−] _[Y]_ [6] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5 [−] _[Y]_ [8] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5 [+] _[ Y]_ [4] _[X]_ [2] _[,]_ [8] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5 [+] _[ Y]_ [6] _[X]_ [2] _[,]_ [8] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5

- _Y_ 2 _X_ 1 _,_ 6 _X_ 3 [2] _,_ 7 _[X]_ [1] _[,]_ [5] [−] _[Y]_ [4] _[X]_ [1] _[,]_ [6] _[X]_ 3 [2] _,_ 7 _[X]_ [1] _[,]_ [5] [−] _[Y]_ [8] _[X]_ [1] _[,]_ [6] _[X]_ 3 [2] _,_ 7 _[X]_ [1] _[,]_ [5] [+][ 2] _[Y]_ [2] _[Y]_ [8] _[X]_ [1] _[,]_ [4] _[X]_ [3] _[,]_ [6] _[X]_ [1] _[,]_ [5] [+] _[ Y]_ [4] _[Y]_ [8] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [6] _[X]_ [1] _[,]_ [5]

- _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 6 _X_ 1 _,_ 5 − 2 _Y_ 2 _Y_ 8 _X_ 1 _,_ 4 _X_ 3 _,_ 7 _X_ 1 _,_ 5 − 2 _Y_ 2 _Y_ 8 _X_ 1 _,_ 6 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + 2 _Y_ 6 _Y_ 8 _X_ 2 _,_ 4 _X_ 3 _,_ 7 _X_ 1 _,_ 5

- _Y_ 4 _Y_ 8 _X_ 2 _,_ 6 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + _Y_ 6 _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + _Y_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 _,_ 5
+ _Y_ 8 _X_ 1 _,_ 6 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 _,_ 5 − _Y_ 6 _X_ 1 _,_ 4 _X_ 2 _,_ 8 _X_ 3 _,_ 7 _X_ 1 _,_ 5 − _Y_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 8 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + 2 _Y_ 4 _Y_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 8 _X_ 1 _,_ 5

- _Y_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 6 _X_ 3 _,_ 8 _X_ 1 _,_ 5 + _Y_ 2 _X_ 1 _,_ 6 _X_ 3 _,_ 7 _X_ 3 _,_ 8 _X_ 1 _,_ 5 + _Y_ 4 _X_ 1 _,_ 6 _X_ 3 _,_ 7 _X_ 3 _,_ 8 _X_ 1 _,_ 5 − 2 _Y_ 2 _Y_ 4 _X_ 1 _,_ 6 _X_ 3 [2] _,_ 7
+ _Y_ 8 _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 3 [2] _,_ 7 [−] _[Y]_ [8] _[X]_ [1] _[,]_ [6] _[X]_ [2] _[,]_ [4] _[X]_ 3 [2] _,_ 7 [+] _[ Y]_ [4] _[X]_ [1] _[,]_ [6] _[X]_ [2] _[,]_ [5] _[X]_ 3 [2] _,_ 7 [+][ 2] _[Y]_ [2] _[Y]_ [8] _[X]_ [1] _[,]_ [4] _[X]_ [1] _[,]_ [6] _[X]_ [3] _[,]_ [7] [+] _[ Y]_ [2] _[X]_ [1] _[,]_ [4] _[X]_ [1] _[,]_ [6] _[X]_ 3 [2] _,_ 7

- 2 _Y_ 6 _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 7 + _Y_ 4 _Y_ 8 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 7 − _Y_ 8 _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 7 _X_ 3 _,_ 7 − _Y_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 7 _X_ 3 _,_ 8
+ (cyclic _,i_ → _i_ + 2 _,i_ + 4 _,i_ + 6) ;
(B.2)


88


_Y_ 2 _Y_ 4 _X_ 3 [2] _,_ 7 _[X]_ 1 [2] _,_ 5 [+][ 2] _[Y]_ [2] _[Y]_ [4] _[Y]_ [6] _[Y]_ [8] _[X]_ 1 [2] _,_ 5 [−] [2] _[Y]_ [4] _[Y]_ [6] _[Y]_ [8] _[X]_ [2] _[,]_ [7] _[X]_ 1 [2] _,_ 5 [+] _[ Y]_ [2] _[Y]_ [4] _[Y]_ [6] _[Y]_ [8] _[X]_ [3] _[,]_ [7] _[X]_ [1] _[,]_ [5]
+ 2 _Y_ 2 _Y_ 4 _Y_ 6 _X_ 3 _,_ 7 _X_ 1 [2] _,_ 5 [+][ 2] _[Y]_ [2] _[Y]_ [4] _[Y]_ [8] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5 [−] _[Y]_ [4] _[Y]_ [6] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5 [−] _[Y]_ [4] _[Y]_ [8] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5
+ _Y_ 4 _Y_ 6 _X_ 2 _,_ 8 _X_ 3 _,_ 7 _X_ 1 [2] _,_ 5 [−] _[Y]_ [2] _[Y]_ [4] _[X]_ [1] _[,]_ [6] _[X]_ 3 [2] _,_ 7 _[X]_ [1] _[,]_ [5] [−] _[Y]_ [2] _[Y]_ [8] _[X]_ [1] _[,]_ [6] _[X]_ 3 [2] _,_ 7 _[X]_ [1] _[,]_ [5] [−] _[Y]_ [4] _[Y]_ [8] _[X]_ [1] _[,]_ [6] _[X]_ 3 [2] _,_ 7 _[X]_ [1] _[,]_ [5]

- 2 _Y_ 2 _Y_ 6 _Y_ 8 _X_ 1 _,_ 4 _X_ 3 _,_ 7 _X_ 1 _,_ 5 − 2 _Y_ 2 _Y_ 4 _Y_ 8 _X_ 1 _,_ 6 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + _Y_ 6 _Y_ 8 _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 _,_ 5
+ _Y_ 2 _Y_ 4 _X_ 1 _,_ 6 _X_ 3 _,_ 7 _X_ 3 _,_ 8 _X_ 1 _,_ 5 − 2 _Y_ 2 _Y_ 4 _Y_ 8 _X_ 1 _,_ 6 _X_ 3 [2] _,_ 7 [+] _[ Y]_ [2] _[Y]_ [8] _[X]_ [1] _[,]_ [4] _[X]_ [1] _[,]_ [6] _[X]_ 3 [2] _,_ 7 [−] _[Y]_ [6] _[Y]_ [8] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5



(B.3)




[1] 1 _,_ 5 [+] [1]

2 _[Y]_ [4] _[Y]_ [8] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [6] _[X]_ [2] 2



3 _,_ 7 _[X]_ 1 [2] _,_ 5
2 _[Y]_ [2] _[Y]_ [6] _[X]_ [2]



+ [1]




[1] 3 _,_ 7 [+] [1]

2 _[Y]_ [4] _[Y]_ [8] _[X]_ [1] _[,]_ [6] _[X]_ [2] _[,]_ [5] _[X]_ [2] 2



+ _Y_ 4 _Y_ 8 _X_ 1 _,_ 6 _X_ 2 _,_ 7 _X_ 3 _,_ 7 _X_ 1 _,_ 5 + (cyclic _,i_ → _i_ + 2 _,i_ + 4 _,i_ + 6) ;



_Y_ 2 _Y_ 4 _Y_ 6 _X_ 3 [2] _,_ 7 _[X]_ 1 [2] _,_ 5 [+][ 2] _[Y]_ [2] _[Y]_ [4] _[Y]_ [6] _[Y]_ [8] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5 [−] _[Y]_ [4] _[Y]_ [6] _[Y]_ [8] _[X]_ [2] _[,]_ [7] _[X]_ [3] _[,]_ [7] _[X]_ 1 [2] _,_ 5
(B.4)

      - _Y_ 2 _Y_ 4 _Y_ 8 _X_ 1 _,_ 6 _X_ 3 [2] _,_ 7 _[X]_ [1] _[,]_ [5] [+ (][cyclic] _[,i]_ [ →] _[i]_ [ +][ 2] _[,i]_ [ +][ 4] _[,i]_ [ +][ 6][)] _[.]_


Finally, the one term with 4 _F_ [3] vertices reads:


_Y_ 2 _Y_ 4 _Y_ 6 _Y_ 8 _X_ 1 [2] _,_ 5 _[X]_ 3 [2] _,_ 7 _[.]_ (B.5)


**C** **Factorization** **for** **derivatives** **of** _u_ **variables**



In this appendix, we show that the derivatives of _u_ variables encountered in computing

residues nicely factorize. The statement is true very generally. Suppose we are interested

in _u_ variables that depend on a given _y_ variable. Obviously the associated curve _C_ must

pass through the road associated with _y_ . We will focus on the cases where the curve passes
through the road _y_ once. The word for this curve is then of the form _A_ −Turn− _y_ −Turn [′] - _B_
where Turn, Turn [′] are either Left or Right turns into and out of _y_ respectively.

Let us begin by considering the case where the words _A,B_ are generic; by this we
mean that the 2 × 2 matrices for _A,B_ are non-zero in all their entries. Geometrically, this
corresponds to the case where the curve _C_ intersects _y_ once. The matrix associated with

_C_ is then of the form




_[b]_ _[b]_ [′]
_MC_ = ( _[a]_
_c_ _d_ [)] _[M][L]_ [/] _[R]_ [(] _[y]_ [)(] _[ a]_ _c_ [′][′] _d_ [′]




_[b]_

(C.1)
_c_ [′] _d_ [′][ )]



Let’s consider the case with _ML_ ( _y_ ), then


_C_ _[M]_ _C_ [2] _[,]_ [1]
_uC_ = _[M]_ [1] _[,]_ [2] = [(] _[ab]_ [′] _[y]_ [ +] _[ d]_ [′][(] _[b]_ [ +] _[ ay]_ [))(] _[a]_ [′] _[cy]_ [ +] _[ c]_ [′][(] _[d]_ [ +] _[ cy]_ [))] (C.2)
_M_ [1] _[,]_ [1] ~~(~~ _aa_ [′] _y_ ~~+~~ _c_ [′] ~~(~~ _b_ ~~+~~ _ay_ ~~))(~~ _b_ [′] _cy_ ~~+~~ _d_ [′] ~~(~~ _d_ ~~+~~ _cy_ ~~))~~
_C_ _[M]_ _C_ [2] _[,]_ [2]



and we can compute



_∂y_ log _uC_ ∣ _y_ =0 = −( _[ad]_ [ −] _[bc]_




[ −] _[bc]_ ) × ( _[a]_ [′] _[d]_ [′][ −] _[b]_ [′] _[c]_ [′]

_bd_ _c_ [′] _d_ [′]




_[b]_ _[c]_

) (C.3)
_c_ [′] _d_ [′]



This expression beautifully factorizes into a part that only depends on the part of the
words on either side of _y_ . [7] .


7
Note that since _C_ intersects _y_, _uC_ → 1 as _y_ → 0, so that _∂y_ log _uC_ is actually equal to _∂yuC_ ; we work
with _∂y_ log _uC_ simply because the logarithmic derivative is most natural for manipulations with the surface
integral.


89


This also means that we can interpret the two factors as _∂_ log _u_ ’s for curves on new

surfaces, which we get by cutting on _y_ and adding “scaffolding” to them. Consider a
curve _C_ left whose word is _AyLα_ where _α_ is a boundary. Since the matrix for this word is
exactly the same as the one we looked at above putting the right matrix to the identity,
we have that _∂y_ log _uC_ left∣ _y_ =0 = −( _ad_ - _bc_ )/( _bd_ ). Similarly, we can define the curve _C_ right
whose word is _βRyB_ where _β_ is a boundary. Then the matrix for this word is exactly the
same as for _C_ with the choice that the “left” matrix is given by _MR_ ( _α_ → 1), so that again
_∂y_ log _uC_ right∣ _y_ =0 = −( _a_ [′] _d_ [′] - _b_ [′] _c_ [′] )/( _c_ [′] _d_ [′] ).
Thus we have discovered that the _∂y_ log _uC_ ∣ _y_ =0 factorizes. We can write this explicitly
in terms of words as

_∂y_ log _u_ [ _XyZ_ ]∣ _y_ =0 = − _∂y_ log _u_ [ _XyLα_ ]∣ _y_ =0 × _∂y_ log _u_ [ _βRyZ_ ]∣ _y_ =0 (C.4)

where _X_ = _A_ and _Z_ = _LB_ . We can recognize this in terms of the left and right curves on
the two surfaces we get by cutting on _y_ and adding scaffolding as in the above:

_∂y_ log _uC_ ∣ _y_ =0 = _∂y_ log _uC_ left∣ _y_ =0 × _∂y_ log _uC_ right∣ _y_ =0 (C.5)


Exactly the same manipulations show precisely the same factorization with a right

turn at _y_ . Note that in defining the left and right curves, we decided to turn left at the
end for _C_ left and right at the beginning for _C_ right. Flipping the choice for each one gives
the same factorizing expression with an extra minus sign.

Note that in this argument, it was important that the left and right matrices _X,Z_

were generic, so that the _u_ variables for the left and right curves were well-defined. This

will not be the case if the left or right part of the curves correspond to pure boundaries,

that is, if _X_ has all right turns or _Z_ has all left turns. This corresponds to a case where

the curve _C_ does pass through _y_ but does not intersect _y_ as a curve; if we draw _y_ as a

chord, then we can say this is a case where the chord associated with _C_ doesn’t intersect

the chord for _y_, but the lamination for _C_ does intersect the chord for _y_ .
Let’s consider the case where the left part of the word for _C_ is of the form (AllRight)yLB.
The result will end up being exactly the same if _y_ is followed by a right turn instead. Now

a general all right matrix is of the form


[0]
_M_ allright = ( _[a]_ (C.6)
_b_ 1 [)]



and hence




[0] _[b]_ [′]
_MC_ = ( _[a]_ (C.7)
_c_ 1 [)] _[M][L]_ [(] _[y]_ [)(] _[ a]_ _c_ [′][′] _d_ [′][ )]



From here we can compute that the derivative of _u_ again factorizes [8] .

_∂yuC_ = − _c_ × [(] _[b]_ [′][ +] _[ d]_ [′][)(] _[a]_ [′] _[d]_ [′][ −] _[b]_ [′] _[c]_ [′][)] _._ (C.8)

~~(~~ _a_ [′] ~~+~~ _c_ [′] ~~)~~ _d_ [′][2]


8Note this expression does not coincide with what we’d get from our previous expressions simply putting

_c_ → 0, this is why we have to treat the case where the words are “all right” to the left of _y_ or “all left” to

the right of _y_ separately


90


Just as before we can interpret each factor in terms of curves on the cut surfaces that

are further scaffolded along the cut curve _y_ . In terms of words we have that

_∂yu_ [(AllRight) _yZ_ ]∣ _y_ =0 = _∂yu_ [(AllRight) _yLα_ ]∣ _y_ =0 × _∂yu_ [ _βLyZ_ ]∣ _y_ =0 (C.9)


Note that as in our previous example, we could also choose _βRZ_ above, at the cost of
an overall sign. We write it using _L_, since the curve with word ( _βLyZ_ ) intersect the
curve for _y_ which has word ( _βRy_ (AllLeft)), and hence it’s _∂yu_ [ _βLyZ_ ] can be replaced
by _∂u_ log _u_ [ _βLyZ_ ] at _y_ = 0. Meanwhile, the word for the first factor ((AllRight) _yLα_ ) is
just that for the curve _y_ itself on the left surface, so we have _u_ curve _y_ for that factor. It
is again useful to write all derivatives as logarithmic derivatives, but clearly _∂yu_ curvey =

- _∂y_ (1 − _u_ curve _y_ ) so _∂yu_ curvey∣ _y_ =0 = − _∂y_ log(1 − _u_ curvey)∣ _y_ =0 since _u_ curvey → 0 as _y_ → 0. Thus
expressed in terms of logarithmic derivatives we have that for curves _C_ with words of the
form ((AllRight) _yZ_ ), we have the factorization for the derivatives as

_∂yuC_ ∣ _y_ =0 = − _∂y_ log(1 − _u_ curve _y_ )∣ _y_ =0 × _∂y_ log _uC_ right∣ _y_ =0 (C.10)

where _C_ right has the word ( _βLyZ_ ).


**D** **Matching** **of** **the** **loop-cut** **with** **gluing** **of** **tree** **in** **the** **forward** **limit**


In this appendix, we show the highly non-trivial matching of the loop-cut and the gluing

of tree amplitude. We separate the matching of each term into different parts, and in the

end, we show the difference is actually a total derivative.


**D.1** **Matching** **of** **the** _D_ **-dependent** **part**

We will start by showing that (†)=(⋆), _i.e._ that the _D_ -dependent part of both answers
agree.
To do this, we look at the tree-level side and understand how we can write _∂XsL,sR_ A, in
terms of _u_ ’s. After taking the scaffolding residue on _sL_, we know we can write the answer
as:




_[u][s][L][,j]_

× ∏ _u_ _[X]_ _X_ [∣]
_∂y_ 1 _,p_ _X_ _y_ 1 _,p_ =0



Res _y_ 1 _,p_ =0A = ∏
_i_

= ∏
_i_



d _yi_

∑( _XsL,j_  - _Xp,j_ ) _[∂]_ [log][(] _[u][s][L][,j]_ [)]
_yi_ [2] _j_ _∂y_ 1 _,p_



d _yi_



d _yi_

∑( _XsL,j_  - _Xp,j_ ) _[∂u][s][L][,j]_
_yi_ [2] _j_ _∂y_ 1 _,p_



d _yi_



(D.1)

_[s][L][,j]_

× ∏ _u_ _[X]_ _X_ [∣] _,_
_∂y_ 1 _,p_ _X_ _y_ 1 _,p_ =0



where in the last line we used the fact that _usL,j_ → 1 when _y_ 1 _,p_ = 0, which follows directly
from the _u_ -equations. Therefore, the part proportional to _XsL,sR_ after taking the residue
in _y_ 1 [′] _,p_, is simply:



⎛ _∂_ [2] _usL,sR_ × ∏ _u_ _[X]_ _X_ [∣] + _..._ [⎞] (D.2)
⎝ _[X][s][L][,s][R]_ _∂y_ 1 [′] _,p∂y_ 1 _,p_ _X_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 ⎠ _[.]_


91



Res _y_ 1′ _,p_ =0 (Res _y_ 1 _,p_ =0A) = ∏
_i_



d _yi_

_yi_ [2]


Now using the word for curve _XsL,sR_, we can write _usL,sR_ in terms of _y_ 1 _,p_ and _y_ 1 [′] _,p_ :

_usL,sR_ = 1 ~~+~~ _y_ 11 [′] _,p_ + _y_ ~~+~~ _y_ 1 [′] 1 _,p_ [′] _,py_ 1 _,p_ ⇒ _∂y∂_ [2] 1 _u_ [′] _,ps∂yL,s_ 1 _R,p_ ∣ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 = −1 _._ (D.3)


Therefore we have:



_∂_ A

- _D_ ⋅ = _D_ ⋅∏
_∂XsL,sR_ _i_



d _yi_

∏ _u_ _[X]_ _X_ [∣] _,_ (D.4)
_yi_ [2] _X_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



d _yi_



which is exactly what we get on the loop-cut side. So indeed we have (†)=(⋆), and the
D-dependent parts agree without any need for total derivative identities.


**D.2** **Matching** **of** **variables** **of** **tree** **triangulation**

Let’s proceed to the matching of (††) with (⋆⋆), _i.e._ the parts proportional to _Xj,k_ . Let’s
start by looking at the loop-side. In this case, we have contributions from two curves, _Xk,j_,
_u_ [(] _k,j_ [0][)][,] [intersecting] _[Y]_ [1] [and] _[X][j,k]_ [that] [self-intersects] [once,] _[u]_ [(] _j,k_ [1][)][.] [Let’s] [now] [understand] [how] [we]
can write the derivatives _∂y_ 1 log _uk,j_ in terms of the _u_ ’s of the cut surface. Let’s start by
looking at _uk,j_, using the matrix method to get this _u_ -variable we have:


_[y]_ [0] _[b]_ _[dy]_ [ +] _[ b]_ [(] _[y]_ [ +] _[ xy]_ [1][)]
_kj_ ∶ _M_ 1 _MR_ ( _y_ 1) _M_ 2 = [ _[x]_
_z_ _w_ [][] _[y]_ 1 [1] 1 [][] _[a]_ _c_ _d_ [] = [] _cw_ _[ cy]_ [ +] + _[ a]_ _a_ [(] ( _[y]_ _w_ [ +] + _[ xy]_ _zy_ [1] 1 [)] ) _dw_ + _b_ ( _w_ + _zy_ 1) []] _[.]_



⇒ _uk,j_ [(][0][)] [=] [(] _[by]_ [ +] _[ dy]_ [ +] _[ bxy]_ [1][)(] _[aw]_ [ +] _[ cw]_ [ +] _[ ay]_ [1] _[z]_ [)]




_[ u][k,j]_ ∣ = [(] _[bc]_ [ −] _[ad]_ [)(] _[wx]_ [ −] _[yz]_ [)]

_∂y_ 1 _y_ 1=0 ~~(~~ _a_ ~~+~~ _c_ ~~)(~~ _b_ ~~+~~ _d_ ~~)~~ _wy_



~~(~~ _a_ ~~+~~ _c_ ~~)(~~ _b_ ~~+~~ _d_ ~~)~~ _wy_ _[,]_




_[by]_ _[ dy]_ _[ bxy]_ [1] _[aw]_ _[ cw]_ _[ ay]_ [1] _[z]_ ⇒ _[∂]_ [log] _[ u][k,j]_

~~(~~ _ay_ ~~+~~ _cy_ ~~+~~ _axy_ 1 ~~)(~~ _bw_ ~~+~~ _dw_ ~~+~~ _by_ 1 _z_ ~~)~~ _∂y_ 1



(D.5)
where _M_ 1 and _M_ 2 are the matrices corresponding to the word to the left/right of _y_ 1,
respectively. After cutting the loop surface, this curve breaks into two, one on the left and
one on the right, that we call _XL_ and _XR_ (see figure 36). Now we consider their extensions
into the scaffolded surface which turns them into curves that are defined on the tree-level
side (represented in dashed in figure 36). This way of extending _XR_ and _XL_ is exactly
such that the corresponding _u_ ’s are




_[y]_
_uXL_ = _uj,sL_ ∶ _M_ 1 _MR_ ( _yL_ ) = [ _w_ _[y]_ [ +] + _[ xy]_ _zy_ _[L]_ _L_ _w_ []]




[log] _[ u][X][L]_

∣ = − [(] _[wx]_ [ −] _[yz]_ [)]
_∂yL_ _yL_ =0 ~~(~~ _wy_ ~~)~~



⇒ _uXL_ = _[y]_ [(] _[w]_ [ +] _[ y][L][z]_ [)]



_._
~~(~~ _wy_ ~~)~~




_[y]_ _[w]_ _[ y][L][z]_ ⇒ _[∂]_ [log] _[ u][X][L]_

_w_ ~~(~~ _y_ ~~+~~ _xyL_ ~~)~~ _∂yL_



(D.6)




_[d]_ [ +] _[ b]_ [(][1][ +] _[ y][R]_ [)]
_uXR_ = _uk,sR_ ∶ _ML_ (1) _MR_ ( _yR_ ) _M_ 2 = [ _[c]_ [ +] _[ a]_ _a_ [(] + [1][ +] _c_ _[ y][R]_ [)] _b_ + _d_ ]



⇒ _uXR_ = [(] _[a]_ [ +] _[ c]_ [)(] _[b]_ [ +] _[ d]_ [ +] _[ by][R]_ [)]




_[ u][X][R]_ ( _bc_   - _ad_ )

∣ =
_∂yR_ _yR_ =0 ~~(~~ _a_ ~~+~~ _c_ ~~)(~~ _b_ ~~+~~ _d_ ~~)~~ _[.]_




_[a]_ _[ c]_ _[b]_ _[ d]_ _[ by][R]_

~~(~~ _b_ ~~+~~ _d_ ~~)(~~ _a_ ~~+~~ _c_ ~~+~~ _ayR_ ~~)~~ [⇒] _[∂]_ [log] _∂y_ _[ u]_ _R_ _[X][R]_



Therefore we have:



_∂_ log _uk,j_




_[ u][X][R]_

∣ × _[∂]_ [log] _[ u][X][L]_
_∂yR_ _yR_ =0 _∂yL_



_uk,j_ ∣ = − _[∂]_ [log] _[ u][X][R]_

_∂y_ 1 _y_ 1=0 _∂yR_




_[ u][X][L]_ ∣ _,_ (D.7)

_∂yL_ _yL_ =0



92


surface (dashed).


from figure 36, we can read off directly the extensions in the scaffolded problem, which

gives us exactly the tree-level result:



_∂_ log _uk,j_



_uk,j_ ∣ = − _[∂]_ [log] _[ u][s][L][,j]_

_∂y_ 1 _y_ 1=0 _∂y_ 1 _,p_



_∂_ log _usR,k_ _._ (D.8)

_∂y_ 1 [′] _,p_



_∂y_ 1 _,p_



Proceeding exactly in the same way for the self-intersecting curve, we find:



_∂_ log _u_ [(][1][)]
_j,k_ ∣ = − _[∂]_ [log] _[ u][s][L][,k]_
_∂y_ 1 _y_ 1=0 _∂y_ 1 _,p_


**D.3** **Matching** **of** **loop** **variables**



_∂_ log _usR,j_ _._ (D.9)

_∂y_ 1 [′] _,p_



We now want to relate (†††) with (⋆⋆⋆), _i.e._ the parts proportional to _Xp,j_ / _Yj_ in the tree
and loop answers, respectively. In this case, it turns out that these two factors will not

match at integrand level, but we will show that they differ by a total derivative.
Let’s start by looking at the tree-level glue term (†††), in particular to the piece
proportional to _Xp,J_ with _J_ ∈{2 _,...,_ 2 _n_ }:



+ _[∂]_ [log] _[ u][s][R][,J]_




_[s][R][,J]_ ∑

_∂y_ 1 [′] _,p_ _k_ ∈{2 _,...,_ 1 [′] }



⎞
⎟⎟⎟⎟⎟⎟⎟⎟
⎠

���������������������������� _y_ 1 _,p_ = _y_ 1′ _,p_ =0



_._



_∂_ log _usR,k_



_∂_ log _usL,k_



_Xp,J_



⎛
⎜⎜⎜⎜⎜⎜⎜⎜
⎝



_∂_ log _usL,J_



_∂y_ 1 _,p_ _k_ ∈{1 _,...,_ 2 _n_ } _∂y_ 1 [′] _,p_

- **��������������������������������������������������** - **���������������������������������������������������**
**(1)**



_sL,J_

∑
_∂y_ 1 _,p_ _k_ ∈{1 _,...,_ 2 _n_ }



_∂y_ 1 [′] _,p_ _k_ ∈{2 _,...,_ 1 [′] } _∂y_ 1 _,p_

- **�������������������������������������������������** - **��������������������������������������������������**
**(2)**



(D.10)



93


Let’s start by analyzing term **(1)** :



_._
����������� _y_ 1 _,p_ = _y_ 1′ _,p_ =0



_usL,J_ × _∂_ log (∏ _k_ ∈{1 _,...,_ 2 _n_ } _usR,k_ )

_∂y_ 1 _,p_ _∂y_ 1 [′] _,p_



_Xp,J_ _∂_ log _usL,J_ ∑

_∂y_ 1 _,p_ _k_ ∈{1 _,...,_ 2 _n_ }



_∂_ log _usR,k_



_usR,k_ ∣ = _Xp,J_ _∂_ log _usL,J_

_∂y_ 1 [′] _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 _∂y_ 1 _,p_



_∂y_ 1 [′] _,p_



(D.11)

Now inside the second logarithm we have the product of all the u-variables correspond
ing to curves that start somewhere on the tree part and eventually end in the following
path: from _t_ to 1 [′] _p_ and exit in road _p,sR_ . This means that this product is effectively the
_u_ -variable of the curve of the smaller surface obtained by cutting through road _t_, _UsR,t_, that
goes from road _p,sR_ to road _t_ . In particular, this means that this product is **independent**
of _yt_ . Now the _u_ -variable for this curve on this smaller surface is really simple:

1 _∂_ log (∏ _k_ ∈{1 _,...,_ 2 _n_ } _usR,k_ )
_k_ ∈{1∏ _,...,_ 2 _n_ } _usR,k_ ≡ _UsR,t_ = ~~(~~ 1 ~~+~~ _y_ 1 [′] _,p_ ~~)~~ ⇒ _∂y_ 1 [′] _,p_ ∣ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 = −1 _._ (D.12)


So we can rewrite (D.10) as follows:



_∂y_ 1 [′] _,p_ _k_ ∈{2 _,...,_ 1 [′] } _∂y_ 1 _,p_

- **�������������������������������������������������** - **��������������������������������������������������**
**(2)**



⎞
⎟⎟⎟⎟⎟⎟⎟⎟
⎠

���������������������������� _y_ 1 _,p_ = _y_ 1′ _,p_ =0



_._ (D.13)



_∂_ log _usL,k_



_Xp,J_



⎛


 - _[∂]_ [log] _[ u][s][L][,J]_

_∂y_ 1 _,p_

⎜⎜⎜⎜⎜⎜⎜⎜� **��������������** **��������������** ⎝ **(1)**



+ _[∂]_ [log] _[ u][s][R][,J]_




_[s][R][,J]_ ∑

_∂y_ 1 [′] _,p_ _k_ ∈{2 _,...,_ 1 [′] }



Before looking at term **(2)**, let’s look at what we have on the loop-side. From (7.38),
we have that the term in (⋆⋆⋆) proportional to _YJ_ is:


_YJ_ _∂_ log _uYJ_ ∣ _._ (D.14)

_∂y_ 1 _y_ 1=0


Since _YJ_ does not intersect _Y_ 1, we can’t use the _u_ -equations to compute this derivative.
Instead, we consider all curves that, just like _YJ_, enter the fat graph in _J,J_ + 1 and go until
road 1, and from there continue to anywhere. Let’s denote this set of curves by C. This
is of course an infinite family of curves since they can self-intersect infinitely often. Now,

exactly for the same reason as before, have that:


_∂y_ 1 ( _uYJ_ × ∏ _uX_ ) = 0 ⇒ _∂y_ 1 log _uYJ_ = − _∂y_ 1 ∑ log _uX_ _._ (D.15)
_X_ ∈C _X_ ∈C

Now since we want to evaluate the derivative at _y_ 1 = 0, the contribution coming from
_X_ ∈C that intersects _Y_ 1 more than once is zero. Therefore we have:


_∂y_ 1 log _uYJ_ ∣ = − _∂y_ 1 log ∏ _uJ,k_ ∣ _,_ (D.16)
_y_ 1=0 _k_ ∈{1 _,...,_ 2 _n_ } _y_ 1=0

where for _k_ ∈{1 _,...,J_ - 1} these correspond to curves that self-intersect once; while for
_k_ ∈{ _J,...,_ 2 _n_ } these are curves that do not intersect but still go around the loop (see


94


**Figure** **37** : Extending curve _YJ_     - curves that intersect _Y_ 1 only once.


figure 37, left). So this product of curves can be interpreted as a curve that starts on road
( _J,J_ + 1), goes around the loop once, and ends in _t_ (union of curve green and red). In
particular, after cutting the loop surface, this curve breaks into _XL_ and _XR_ (see figure
37, right). _XR_ is effectively a curve of the smaller surface that starts in the tadpole road.
Therefore, using the result from section D.2, we can write the derivative of the logarithm

as follows:



_uYJ_ _∂_ log _uXJ,_ 1

∣ =
_∂y_ 1 _y_ 1=0 _∂y_ 1




_[ u][X]_ [1] _[,t]_

∣ = _[∂]_ [log] _[ u][X][L]_
_∂y_ 1 _y_ 1=0 _∂y_ 1




_[ u][X][L]_

⋅ _[∂]_ [log] _[ u][X][R]_
_∂y_ 1 _∂y_ 1



_∂_ log _uYJ_



_uXJ,_ 1

⋅ _[∂]_ [log] _[ u][X]_ [1] _[,t]_
_∂y_ 1 _∂y_ 1




_[ u][X][R]_ ∣ _._ (D.17)

_∂y_ 1 _y_ 1=0



Once again, to relate to the tree-level variables, we consider the extension of curves
_XL_ and _XR_, to the scaffolded cut surface in the same way we did previously. While
_uX_ 1 _,t_ becomes _UsR,t_ giving a trivial contribution, as shown in (D.12), _uXJ,_ 1 becomes _usL,J_,
allowing us to write
_∂_ log _uYJ_

_[∂]_ [log] _[ u][s][L][,J]_



_uYJ_

∣ = − _[∂]_ [log] _[ u][s][L][,J]_
_∂y_ 1 _y_ 1=0 _∂y_ 1




_[ u][s][L][,J]_

∣ _,_ (D.18)
_∂y_ 1 _y_ 1=0



which precisely matches part of the tree-level contribution. So currently the difference
between the tree-gluing and the loop cut for (†††) is simply term **(2)** :



_Xp,J_ ⎛ _∂_ log _usR,J_ ∑
⎝ _∂y_ 1 [′] _,p_ _k_ ∈{2 _,...,_ 1 [′] }



_∂_ log _usL,k_

_∂y_ 1 _,p_



⎞
⎠ _._ (D.19)

������������ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



Let’s now try to use the _u_ -equations to simplify **(2)** . We start by once more turning

the sum into a product inside the logarithm:



_usR,J_ ⋅ _∂_ log ∏ _k_ ∈{2 _,...,_ 1′} _usL,k_

_∂y_ 1 [′] _,p_ _∂y_ 1 _,p_



_Xp,J_ _∂_ log _usR,J_



∈{2 _,...,_ 1′} _sL,k_

∣ _._ (D.20)
_∂y_ 1 _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



95


As opposed to **(1)**, this product of _u_ ’s **cannot** be identified as the _u_ of a smaller

surface. So instead, in order to simplify this result we use the extended _u_ -equations:


∏ _usL,k_ + _u_ 1 _,pu_ 1 _,sR_ = 1 _,_ (D.21)
_k_ ∈{2 _,...,_ 1 [′] }


which allows us to write:



_∂_ log ∏ _k_ ∈{2 _,...,_ 1′} _usL,k_




_[∂u]_ [1] _[,p]_ ∣ = − _[∂u]_ [1] _[,p]_

_∂y_ 1 _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 _∂y_ 1 _,p_



∈{2 _,...,_ 1′} _usL,k_

∣ = − _u_ 1 _,sR_ ⋅ _[∂u]_ [1] _[,p]_
_∂y_ 1 _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 _∂y_ 1 _,p_




_[∂u]_ [1] _[,p]_ ∣ _._ (D.22)

_∂y_ 1 _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



Finally to compute _∂y_ 1 _,pu_ 1 _,p_, we use (2.17) which allows us to write _y_ 1 _,p_ in terms of _u_ ’s
in the following way:



_u_ 1 _,p_ ∏ _k_ ∈{2 _,...,_ 2 _n_ } _up,k_
_y_ 1 _,p_ =




_[∂u]_ [1] _[,p]_ ∏ _up,k_ ∣ _,_ (D.23)

_∂y_ 1 _,p_ _k_ ∈{2 _,...,_ 2 _n_ } _y_ 1 _,p_ = _y_ 1′ _,p_ =0



_k_ ∈{2 _,...,_ 2 _n_ } _up,k_

⇒ 1 = _[∂u]_ [1] _[,p]_
_usL,sRusL,_ 1 [′] _∂y_ 1 _,p_



and so we can rewrite (D.20) as


_Xp,J_ _∂_ log _usR,J_ ⋅ 1 ∣ _._ (D.24)

_∂y_ 1 [′] _,p_ ∏ _k_ ∈{2 _,...,_ 2 _n_ } _up,k_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0


Using, once again, the _u_ -equations we can find an expression for _∂y_ 1′ _,p_ log _usR,J_ in terms
of the remaining _u_ variables as follows:



_usR,J_ + _u_ 1 [′] _,p_ ∏
_a_ ∈{1 _,...,J_ −1}
_b_ ∈{ _J_ +1 _,...,_ 1 [′] }



_ua,b_ × ∏ _up,k_ = 1
_k_ ∈{ _J_ +1 _,..._ 2 _n_ }



⇒ _[∂]_ [log] _[ u][s][R][,J]_




- **����������** _∂y_ 1 [′] _,p_ **����������**
=1




_[ u][s][R][,J]_ = − _[∂]_ [log] _[ u]_ [1][′] _[,p]_

_∂y_ 1 [′] _,p_ _∂y_ 1 [′] _,p_



× ∏
_a_ ∈{1 _,...,J_ −1}
_b_ ∈{ _J_ +1 _,...,_ 1 [′] }



(D.25)
_ua,b_ × ∏ _up,k,_
_k_ ∈{ _J_ +1 _,..._ 2 _n_ }



which we can further simplify with the help of the generalized _u_ -equations that tell us



∏ _ua,b_ = 1 - _up,J_ _usR,J_ ⇒ ∏
_a_ ∈{1 _,...,J_ −1} _a_ ∈{1 _,...,J_ −1}
_b_ ∈{ _J_ +1 _,...,_ 1 [′] } _b_ ∈{ _J_ +1 _,...,_ 1 [′] }



_ua,b_ ∣ = 1 - _up,J_ ∣ _._ (D.26)
_y_ 1 _,p_ = _y_ 1′ _,p_ =0 _y_ 1 _,p_ = _y_ 1′ _,p_ =0



In summary, we have that the tree-level contribution that is not present in the loop

side is:



_Xp,J_ ( [1][ −] _[u][p,J]_




_[u][p,J]_ 1

⋅ )∣ _._ (D.27)
_up,J_ ∏ _k_ ∈{2 _,...,J_ −1} _up,k_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



In subsection D.6, we show that the above difference between loop integrand and the

forward limit of the tree is actually a total derivative and thus vanishes after integration.


96


**Figure** **38** : Curves contributing to _X_ 1 _,j_ term.


**D.4** **Matching** **of** **curves** _X_ 1 _,j_

Now we want to see how (††††) matches (⋆⋆⋆⋆). Let’s start with the tree side. Since
_X_ 1 _,_ 2 = _X_ 1 [′] _,_ 2 _n_ = 0 we have that (††††) is :



∑ - _Xj,_ 1 [′] _[∂]_ [log] _[ u][s][L][,]_ [1][′]
_j_ ∈{2 _,...,_ 2 _n_ } _∂y_ 1 _,p_



_∂_ log _usR,j_



_∂_ log _usR,_ 1 ∣ _._

_∂y_ 1 [′] _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0




- **������������** _∂y_ 1 _,p_ **������������** =−1



log _usR,j_ ∣ - _X_ 1 _,j_ _∂_ log _usL,j_

_∂y_ 1 [′] _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 _∂y_ 1 _,p_



_∂y_ 1 _,p_



(D.28)

Now on the loop side, we have to consider the contributions of three different curves, see

figure 38. Let’s start by looking at the contribution coming from the two self-intersecting
curves. From the word for curve _X_ 1 _[S.I.]_ _,j_ [,] [we] [get] [the] [following] _[u]_ [-variable:]




[0] _[y][t]_ _[y]_ [1] _[b]_
_u_ [(] 1 [1] _,j_ [)] [∶] _M_ 1 _ML_ ( _yt_ ) _ML_ ( _y_ 1) _M_ 2 = [ _[x]_
_z_ 1 [][] _[y]_ 0 _[t]_ 1 [][] _[y]_ 0 [1] 1 [][] _[a]_ _c_ _d_ []]



_∂_ log _u_ [(] 1 [1] _,j_ [)]

[(] _[d]_ [ +] _[ by]_ [1][ +] _[ dy]_ [1][)(] _[c]_ [ +] _[ cy][t][z]_ [ +] _[ ay]_ [1] _[y][t][z]_ [ +] _[ cy]_ [1] _[y][t][z]_ [)] ∣ = [(] _[bc]_ [ −] _[ad]_ [)]

~~(~~ _c_ ~~+~~ _ay_ 1 ~~+~~ _cy_ 1 ~~)(~~ _d_ ~~+~~ _dytz_ ~~+~~ _by_ 1 _ytz_ ~~+~~ _dy_ 1 _ytz_ ~~)~~ [⇒] _∂y_ 1 _y_ 1=0 _cd_ ~~(~~ 1 ~~+~~ _ytz_



⇒ _u_ [(] 1 [1] _,j_ [)] [=] [(] _[d]_ [ +] _[ by]_ [1][ +] _[ dy]_ [1][)(] _[c]_ [ +] _[ cy][t][z]_ [ +] _[ ay]_ [1] _[y][t][z]_ [ +] _[ cy]_ [1] _[y][t][z]_ [)]



_cd_ ~~(~~ 1 ~~+~~ _ytz_ ~~)~~ _[.]_



(D.29)

Now proceeding like we did in section D.2, we can show that:



_∂_ log _u_ [(] 1 [1] _,j_ [)] ∣ = − _[∂]_ [log] _[ u][s][R][,]_ [1]
_∂y_ 1 _y_ 1=0 _∂y_ 1 [′] _,p_


Doing exactly the same thing for _Xj,_ _[S.I.]_ 1 we get:



_∂_ log _usL,j_ _._ (D.30)

_∂y_ 1 _,p_



_∂_ log _u_ [(] _j,_ [1] 1 [)]
∣ = _[∂]_ [log] _[ u][s][R][,j]_ _._ (D.31)
_∂y_ 1 _y_ 1=0 _∂y_ 1 [′] _,p_


97


This means that the contribution coming from the two self-intersecting curves perfectly

matches the tree-level gluing term. However, on the loop side, we still have a contribution
from the non-self-intersecting curve _Xj,_ 1 (see figure 38), for which the _u_ -variable is:




[0] [0] _[b]_ _axy_ 1 _bxy_ 1
_j_ 1 ∶ _M_ 1 _MR_ ( _y_ 1) _M_ 2 = [ _[x]_
_z_ 1 [][] _[y]_ 1 [1] 1 [][] _[a]_ _c_ _d_ [] = [] _c_ + _a_ (1 + _zy_ 1) _d_ + _b_ (1 + _zy_ 1) []]



⇒ _uj,_ 1 = _[b]_ [(] _[a]_ [ +] _[ c]_ [ +] _[ ay]_ [1] _[z]_ [)]




_[ u][j,]_ [1]

∣ = _[bz]_ [(] _[ad]_ [ −] _[bc]_ [)]
_∂y_ 1 _y_ 1=0 _a_ ~~(~~ _b_ ~~+~~ _d_ ~~)~~ [2]




_[b]_ _[a]_ _[ c]_ _[ ay]_ [1] _[z]_ ⇒ _[∂]_ [log] _[ u][j,]_ [1]

_a_ ~~(~~ _b_ ~~+~~ _d_ ~~+~~ _by_ 1 _z_ ~~)~~ _∂y_ 1




[(] _[ad]_ [ −] _[bc]_ [)] (D.32)

_[,]_
_a_ ~~(~~ _b_ ~~+~~ _d_ ~~)~~ [2]



which can be expressed in terms of the scaffolded-tree variables as follows:



_∂_ log _uj,_ 1



_uj,_ 1

∣ = − _z_ _[∂]_ [log] _[ u][s][R][,j]_
_∂y_ 1 _y_ 1=0 _∂y_ 1 [′] _,p_



_,_ (D.33)
_∂y_ 1 [′] _,p_



with _z_ being the _F_ -polynomial appearing in _M_ 1. So on the loop side, we have an extra
term:



∑ - _zX_ 1 _,j_ _∂_ log _usR,j_
_j_ =3 _,...,_ 2 _n_ −1 _∂y_ 1 [′] _,p_



_._ (D.34)
_∂y_ 1 [′] _,p_



Now, one can easily check that _z_ is exactly the _F_ -polynomial corresponding to the
curve that turns consistently right until _yt_, and thus has the following simple form:

_z_ = (1 + _yt_ (1 + _y_ 1 _,m_ (1 + _..._ ))) _._ (D.35)


Finally, we note that this _F_ -polynomial appears in the expression of _uY_ 1, allowing us
to write:
_z_ 1 [=] _u_ _[y]_ _Y_ [1] 1 ∣ _y_ 1=0 = _k_ ∈{2∏ _,...,_ 2 _n_ } _uYk_ ∣ _y_ 1=0 = _k_ ∈{2∏ _,...,_ 2 _n_ } _up,k_ ∣ _y_ 1=0 _,_ (D.36)


where we use (2.17) in the first equality. In summary, the extra term in the loop side is:



∑      - _X_ 1 _,j_ _∂_ log _usR,j_
_j_ =3 _,...,_ 2 _n_ −1 _∂y_ 1 [′] _,p_


**D.5** **Matching** **the** **tadpole** **part**



1
_._ (D.37)
∏ _k_ ∈{2 _,...,_ 2 _n_ } _up,k_



From the tree-level side (†††††), we have the following




- _X_ 1 _,_ 1 [′] _[∂]_ [log] _[ u][s][L][,]_ [1][′]

_∂y_ 1 _,p_



log _usR,_ 1

∣ = _X_ 1 _,_ 1 [′] _[∂]_ [log] _[ u][s][R][,]_ [1]
_∂y_ 1 [′] _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 _∂y_ 1 [′] _,p_



_∂_ log _usR,_ 1




_[ u][s][R][,]_ [1]

∣ _._ (D.38)
_∂y_ 1 [′] _,p_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



From the loop side, we have two contributions, one from the regular tadpole curve,

and one from the tadpole that self-intersects once. To obtain the contribution from the
latter we can use directly (D.31), setting _j_ = 1 to get:

_X_ 1 _,_ 1 _∂_ log _u_ [(] 1 [1] _,_ 1 [)] ∣ = _X_ 1 _,_ 1 _∂_ log _usR,_ 1 _,_ (D.39)
_∂y_ 1 _y_ 1=0 _∂y_ 1 [′] _,p_


which precisely matches the tree glue result. As for the contribution from the non-selfintersecting curve, proceeding exactly in the same way as we did for _Xj,_ 1, we get:




- _X_ 1 _,_ 1 _∂_ log _usR,_ 1



log _usR,_ 1 = − _X_ 1 _,_ 1 _∂_ log _usR,_ 1

_∂y_ 1 [′] _,p_ _∂y_ 1 [′] _,p_



_∂y_ 1 [′] _,p_



1
_._ (D.40)
∏ _k_ ∈{2 _,...,_ 2 _n_ } _up,k_



98


**D.6** **Difference** **between** **loop-cut** **and** **tree-gluing** **as** **a** **total** **derivative**


So in summary the difference between the loop cut and the tree-level glue is:



(D.41)



1
+ 1 [⎞] _u_ _[X]_ _C_ _[C]_
∏ _k_ ∈{2 _,...,_ 2 _n_ } _up,k_ ⎠ [∏] _C_



∏ [1]

_yi_ [2]



⎛
∑ ( _X_ 1 _,j_  - _Xp,j_ ) _[∂]_ [log] _[ u][s][R][,j]_
⎝ _j_ =1 _,...,_ 2 _n_ _∂y_ 1 [′] _,p_



_∂y_ 1 [′] _,p_



=∏ [1]

_yi_ [2]



⎛ 1 − _up,j_
⎝ [−] _j_ =1∑ _,...,_ 2 _n_ ( _X_ 1 _,j_ - _Xp,j_ ) ∏ _k_ ∈{2 _,...,j_ } _up,k_ + 1 [⎞] ⎠ [∏] _C_ _u_ _[X]_ _C_ _[C]_ _[.]_



The claim is that (D.41) is equal to the following total derivative:



_k_ ∈{1 _,...,m_ −1} _up,ku_ 1 [′] _,k_ ⎞

_up,_ 1 ∏ _j_ ∈{2 _,...,_ 2 _n_ } _u_ [2] _p,j_ ∏ _C_ _u_ _[X]_ _C_ _[C]_ ⎠



_,_ (D.42)
����������� _y_ 1 _,p_ = _y_ 1′ _,p_ =0




- _[∂]_

_∂yt_



⎛
⎝ [∏] _y_ [1] _i_ [2]



∏ _k_ ∈{1 _,...,m_ −1} _up,ku_ 1 [′] _,k_



where _m_ is the region indicated in figure 35.

Let’s now proceed to the proof this result. We start by using (2.17), _yi_ = ∏ _X_ _ugXX_ [(] _[i]_ [)][,] [to]
write _yt_ in terms of _u_ ’s as follows


_[u]_ [1][′] _[,k]_
_yt_ = ( [∏] _[k]_ [∈{][1] _[,...,m]_ [−][1][}] ) _,_ (D.43)

∏ _j_ ∈{ _m,...,_ 2 _n_ } _up,j_


and so we can simplify expression (D.42) by defining _Q_ as


_[u][p,k][u]_ [1][′] _[,k]_ _yt_ _yt_
_Q_ = [∏] _[k]_ [∈{][1] _[,...,m]_ [−][1][}] = = (D.44)

_up,_ 1 ∏ _j_ ∈{2 _,...,_ 2 _n_ } _u_ [2] _p,j_ ∏ _j_ ∈{2 _,...,_ 2 _n_ } _up,j_ 1 ~~−~~ _u_ 1 _,_ 1 [′] _[,]_


where we use the _u_ -equations in the last equality. Therefore the claim is equivalent to




_[ u][p,J]_

∣ = [1][ −] _[u][p,J]_
_∂yt_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0 _up,J_




- _Q_ _[∂]_ [log] _[ u][p,J]_




_[u][p,J]_ 1

⋅ ∣ _._ (D.45)
_up,J_ ∏ _k_ ∈{2 _,...,J_ −1} _up,k_ _y_ 1 _,p_ = _y_ 1′ _,p_ =0



It is sufficient to prove (D.45) under a specific triangulation since the integrated result is

triangulation-independent. For example, taking the scaffolding triangulation with a ray-like
triangulation inside the gluon _n_ -gon: { _X_ 1 _,p_ [′] _,X_ 1 _,p,X_ 1 _,_ 3 _,X_ 3 _,_ 5 _,...,X_ 2 _n_ −1 _,_ 1 [′] _,X_ 1 _,_ 1 [′] _,X_ 3 _,_ 1 [′] _,...,_
_X_ 2 _n_ −1 _,_ 1 [′] }, allow us to write _Q_ as



_Q_ = _[y][t]_ [(][1][ +] _[ y][t]_ [)]



_._ (D.46)
_up,_ 2



Then one can prove (D.45) indeed holds after some tedious algebra involving the 2 × 2
matrices defining the _u_ variables.


99


**References**


[1] N. Arkani-Hamed and J. Trnka, _The_ _Amplituhedron_, _JHEP_ **10** (2014) 030,

[ `[arXiv:1312.2007](http://arxiv.org/abs/1312.2007)` ].


[2] N. Arkani-Hamed, Y. Bai, and T. Lam, _Positive_ _Geometries_ _and_ _Canonical_ _Forms_, _JHEP_ **11**
(2017) 039, [ `[arXiv:1703.04541](http://arxiv.org/abs/1703.04541)` ].


[3] A. Hodges, _Eliminating_ _spurious_ _poles_ _from_ _gauge-theoretic_ _amplitudes_, _JHEP_ **05** (2013) 135,

[ `[arXiv:0905.1473](http://arxiv.org/abs/0905.1473)` ].


[4] N. Arkani-Hamed, H. Thomas, and J. Trnka, _Unwinding_ _the_ _Amplituhedron_ _in_ _Binary_, _JHEP_
**01** (2018) 016, [ `[arXiv:1704.05069](http://arxiv.org/abs/1704.05069)` ].


[5] N. Arkani-Hamed, Y. Bai, S. He, and G. Yan, _Scattering_ _Forms_ _and_ _the_ _Positive_ _Geometry_
_of_ _Kinematics,_ _Color_ _and_ _the_ _Worldsheet_, _JHEP_ **05** (2018) 096, [ `[arXiv:1711.09102](http://arxiv.org/abs/1711.09102)` ].


[6] N. Arkani-Hamed, S. He, G. Salvatori, and H. Thomas, _Causal_ _diamonds,_ _cluster_ _polytopes_
_and_ _scattering_ _amplitudes_, _JHEP_ **11** (2022) 049, [ `[arXiv:1912.12948](http://arxiv.org/abs/1912.12948)` ].


[7] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _All_ _Loop_
_Scattering_ _as_ _a_ _Counting_ _Problem_, `[arXiv:2309.15913](http://arxiv.org/abs/2309.15913)` .


[8] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _All_ _Loop_
_Scattering_ _For_ _All_ _Multiplicity_, `[arXiv:2311.09284](http://arxiv.org/abs/2311.09284)` .


[9] N. Arkani-Hamed, S. He, T. Lam, and H. Thomas, _Binary_ _geometries,_ _generalized_ _particles_
_and_ _strings,_ _and_ _cluster_ _algebras_, _Phys._ _Rev._ _D_ **107** (2023), no. 6 066015,

[ `[arXiv:1912.11764](http://arxiv.org/abs/1912.11764)` ].


[10] N. Arkani-Hamed, S. He, and T. Lam, _Stringy_ _canonical_ _forms_, _JHEP_ **02** (2021) 069,

[ `[arXiv:1912.08707](http://arxiv.org/abs/1912.08707)` ].


[11] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. B. Goncharov, A. Postnikov, and J. Trnka,
_Grassmannian_ _Geometry_ _of_ _Scattering_ _Amplitudes_ . Cambridge University Press, 4, 2016.


[12] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Hidden_ _zeros_ _for_
_particle/string_ _amplitudes_ _and_ _the_ _unity_ _of_ _colored_ _scalars,_ _pions_ _and_ _gluons_,
`[arXiv:2312.16282](http://arxiv.org/abs/2312.16282)` .

[13] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _NLSM_ ⊂ _Tr_ ( _ϕ_ [3] ),

`[arXiv:2401.05483](http://arxiv.org/abs/2401.05483)` .


[14] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _The_
_combinatorial_ _string,_ _to_ _appear_ .


[15] R. P. Feynman, _Quantum_ _theory_ _of_ _gravitation_, _Acta_ _Phys._ _Polon._ **24** (1963) 697–722.


[16] S. Caron-Huot, _Loops_ _and_ _trees_, _JHEP_ **05** (2011) 080, [ `[arXiv:1007.3224](http://arxiv.org/abs/1007.3224)` ].


[17] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Surface_ _Kinematics_ _and_
_“The”_ _Yang-Mills_ _Integrand,_ _to_ _appear_ .


[18] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _The_ _curvy_
_world_ _of_ _curves,_ _to_ _appear_ .


[19] Z. Koba and H. B. Nielsen, _Reaction_ _amplitude_ _for_ _n_ _mesons:_ _A_ _Generalization_ _of_ _the_
_Veneziano-Bardakci-Ruegg-Virasora_ _model_, _Nucl._ _Phys._ _B_ **10** (1969) 633–655.


[20] F. C. S. Brown, _Multiple_ _zeta_ _values_ _and_ _periods_ _of_ _moduli_ _spaces_ _M_ _0_ _,n_ _(_ _R_ _)_, _Annales_ _Sci._
_Ecole_ _Norm._ _Sup._ **42** (2009) 371, [ `[math/0606419](http://arxiv.org/abs/math/0606419)` ].


100


[21] G. Veneziano, _Construction_ _of_ _a_ _crossing_ _-_ _symmetric,_ _Regge_ _behaved_ _amplitude_ _for_ _linearly_
_rising_ _trajectories_, _Nuovo_ _Cim._ _A_ **57** (1968) 190–197.


[22] C. R. Mafra, O. Schlotterer, and S. Stieberger, _Complete_ _N-Point_ _Superstring_ _Disk_
_Amplitude_ _II._ _Amplitude_ _and_ _Hypergeometric_ _Function_ _Structure_, _Nucl._ _Phys._ _B_ **873** (2013)
461–513, [ `[arXiv:1106.2646](http://arxiv.org/abs/1106.2646)` ].


[23] C. R. Mafra and O. Schlotterer, _Non-abelian_ _Z-theory:_ _Berends-Giele_ _recursion_ _for_ _the_
_α_ [′] _-expansion_ _of_ _disk_ _integrals_, _JHEP_ **01** (2017) 031, [ `[arXiv:1609.07078](http://arxiv.org/abs/1609.07078)` ].


[24] J. J. M. Carrasco, C. R. Mafra, and O. Schlotterer, _Abelian_ _Z-theory:_ _NLSM_ _amplitudes_ _and_
_α’-corrections_ _from_ _the_ _open_ _string_, _JHEP_ **06** (2017) 093, [ `[arXiv:1608.02569](http://arxiv.org/abs/1608.02569)` ].


[25] M. Mirzakhani, _Simple_ _geodesics_ _and_ _Weil-Petersson_ _volumes_ _of_ _moduli_ _spaces_ _of_ _bordered_
_Riemann_ _surfaces_, _Invent._ _Math._ **167** (2006), no. 1 179–222.


[26] E. Witten, _The_ _Feynman_ _iϵ_ _in_ _String_ _Theory_, _JHEP_ **04** (2015) 055, [ `[arXiv:1307.5124](http://arxiv.org/abs/1307.5124)` ].


[27] N. Arkani-Hamed, C. Figueiredo, and G. N. Remmen, _Open_ _String_ _Amplitudes:_
_Singularities,_ _Asymptotics,_ _and_ _New_ _Representations_, `[arXiv:2412.20639](http://arxiv.org/abs/2412.20639)` .


[28] M. B. Green, J. H. Schwarz, and E. Witten, _Superstring_ _Theory:_ _Volume_ _1,_ _Introduction_ .
Cambridge university press, 1988.


[29] S. He, F. Teng, and Y. Zhang, _String_ _amplitudes_ _from_ _field-theory_ _amplitudes_ _and_ _vice_ _versa_,
_Phys._ _Rev._ _Lett._ **122** (2019), no. 21 211603, [ `[arXiv:1812.03369](http://arxiv.org/abs/1812.03369)` ].


[30] S. He, F. Teng, and Y. Zhang, _String_ _Correlators:_ _Recursive_ _Expansion,_ _Integration-by-Parts_
_and_ _Scattering_ _Equations_, _JHEP_ **09** (2019) 085, [ `[arXiv:1907.06041](http://arxiv.org/abs/1907.06041)` ].


[31] F. Cachazo, S. He, and E. Y. Yuan, _Scattering_ _Equations_ _and_ _Matrices:_ _From_ _Einstein_ _To_
_Yang-Mills,_ _DBI_ _and_ _NLSM_, _JHEP_ **07** (2015) 149, [ `[arXiv:1412.3479](http://arxiv.org/abs/1412.3479)` ].


[32] F. Cachazo, S. He, and E. Y. Yuan, _Scattering_ _of_ _Massless_ _Particles_ _in_ _Arbitrary_
_Dimensions_, _Phys._ _Rev._ _Lett._ **113** (2014), no. 17 171601, [ `[arXiv:1307.2199](http://arxiv.org/abs/1307.2199)` ].


[33] F. Cachazo, S. He, and E. Y. Yuan, _Scattering_ _of_ _Massless_ _Particles:_ _Scalars,_ _Gluons_ _and_
_Gravitons_, _JHEP_ **07** (2014) 033, [ `[arXiv:1309.0885](http://arxiv.org/abs/1309.0885)` ].


[34] _work_ _in_ _progress_ .


[35] N. Arkani-Hamed, F. Cachazo, and J. Kaplan, _What_ _is_ _the_ _Simplest_ _Quantum_ _Field_ _Theory?_,
_JHEP_ **09** (2010) 016, [ `[arXiv:0808.1446](http://arxiv.org/abs/0808.1446)` ].


[36] F. Cachazo, S. He, and E. Y. Yuan, _New_ _Double_ _Soft_ _Emission_ _Theorems_, _Phys._ _Rev._ _D_ **92**
(2015), no. 6 065030, [ `[arXiv:1503.04816](http://arxiv.org/abs/1503.04816)` ].


[37] N. Arkani-Hamed, C. Figueiredo, H. Frost, and G. Salvatori, _Tropical_ _Amplitudes_ _For_
_Colored_ _Lagrangians_, `[arXiv:2402.06719](http://arxiv.org/abs/2402.06719)` .


[38] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, S. Caron-Huot, and J. Trnka, _The_ _All-Loop_
_Integrand_ _For_ _Scattering_ _Amplitudes_ _in_ _Planar_ _N=4_ _SYM_, _JHEP_ **01** (2011) 041,

[ `[arXiv:1008.2958](http://arxiv.org/abs/1008.2958)` ].


[39] A. Edison, S. He, H. Johansson, O. Schlotterer, F. Teng, and Y. Zhang, _Perfecting_ _one-loop_
_BCJ_ _numerators_ _in_ _SYM_ _and_ _supergravity_, _JHEP_ **02** (2023) 164, [ `[arXiv:2211.00638](http://arxiv.org/abs/2211.00638)` ].


[40] H. Kawai, D. C. Lewellen, and S. H. H. Tye, _A_ _Relation_ _Between_ _Tree_ _Amplitudes_ _of_ _Closed_
_and_ _Open_ _Strings_, _Nucl._ _Phys._ _B_ **269** (1986) 1–23.


101


[41] Z. Bern, J. J. M. Carrasco, and H. Johansson, _New_ _Relations_ _for_ _Gauge-Theory_ _Amplitudes_,
_Phys._ _Rev._ _D_ **78** (2008) 085011, [ `[arXiv:0805.3993](http://arxiv.org/abs/0805.3993)` ].


102


