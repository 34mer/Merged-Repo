Prepared for submission to JHEP

## **Surface Gauge Invariance, Soft Limits and the** **Transmutation of Gluons into Scalars**


**Jeffrey** **V.** **Backus,** **Carolina** **Figueiredo**


_Jadwin_ _Hall,_ _Princeton_ _University,_ _Princeton,_ _NJ_ _08540,_ _USA_


_E-mail:_ `[jvabackus@princeton.edu](mailto:jvabackus@princeton.edu)`, `[cfigueiredo@princeton.edu](mailto:cfigueiredo@princeton.edu)`


Abstract: Over the past year, the “scalar-scaffolding” formalism has revealed a number of

new features of gluon amplitudes. In this paper, we leverage these developments to study

two distinct but related questions, linked by the scaffolding statement of gauge invariance.

We start by revisiting the soft expansion of gluon amplitudes. The scaffolding picture al
lows for a precise definition of the soft limit and a canonical way to expand the amplitude.

At tree-level, this reproduces the classic Weinberg soft theorem, and at one-loop, using

surface kinematics, we derive an extension of this theorem valid at the level of the loop

integrand. We then switch gears and describe a new relationship between gluon and scalar

amplitudes. The expression of surface gauge invariance naturally suggests a certain differ
ential operator acting on individual external gluons. Remarkably, we find that, both for

the tree-level amplitude and the surface one-loop integrand, repeated applications of this
operator _transmutes_ gluon amplitudes/integrands into those of Tr( _ϕ_ [3] ) scalars. This is an
interesting counterpart to the _δ_ -shift connection that lifts “stringy” Tr( _ϕ_ [3] ) amplitudes to

those of gluons.


### **Contents**

**1** **Introduction** **2**


**2** **A** **Review** **of** **Scalar-Scaffolded** **Gluons** **5**

2.1 How to scalar-scaffold gluons . . . . . . . . . . . . . . . . . . . . . . . . . . 6

2.2 Examples at three- and four-points . . . . . . . . . . . . . . . . . . . . . . . 9

2.3 Surface kinematics and the one-loop gluon integrand . . . . . . . . . . . . . 11

2.4 One-loop one- and two- point surface integrands . . . . . . . . . . . . . . . . 14

### I Soft Limits at Tree-Level and One-Loop 16


**3** **Defining** **the** **Soft** **Limit** **at** **Tree-Level** **17**

3.1 Setting up the soft expansion . . . . . . . . . . . . . . . . . . . . . . . . . . 20


**4** **The** **Leading** **Soft** **Theorem** **at** **Tree-Level** **22**

4.1 Gauge-invariantifying the soft expansion . . . . . . . . . . . . . . . . . . . . 24


**5** **The** **One-Loop** **Leading** **Soft** **Theorem** **for** **the** **Surface** **Integrand** **25**

5.1 Defining the soft expansion in surface kinematics . . . . . . . . . . . . . . . 25

5.2 The leading soft theorem for the one-loop integrand . . . . . . . . . . . . . . 28

### II Transmutation of Gluons into Scalars 30


**6** **Polarization** **Choice** **for** _We_ **32**


**7** _We_ **as** **a** **Split** **Configuration** **34**
7.1 One split . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

7.2 Consecutive splits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
7.3 Shifted stringy integrals and Tr( _ϕ_ [3] ) at low energies . . . . . . . . . . . . . . 44


**8** **Polarization** **Configuration** **for** **Consecutive** **Splits** **46**

8.1 Four-point example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48


**9** **Transmutation** **at** **One-Loop** **51**


**10** **Outlook** **53**


**A** **Higher** **Orders** **in** **the** **Tree-Level** **Soft** **Expansion** **54**


**B** **Higher** **Orders** **in** **the** **One-Loop** **Soft** **Expansion** **59**


**Bibliography** **61**


                   - 1                   

**1** **Introduction**


In the past year, a new approach has been proposed for studying scattering amplitudes of
massless colored particles, from Tr( _ϕ_ [3] ) theory to pions and gluons [1–3]. This picture not

only makes the standard features of amplitudes manifest - such as factorization on poles

- but also brings to light previously-hidden properties of these objects [2, 4–14].

In this formulation, gluon amplitudes are recast using different kinematic variables,

which come from thinking of each external gluon as being produced by a pair of scalars 
the gluons are _scalar-scaffolded_ [1]. In this way, the gluon amplitude is written exclusively

in terms of dot products of the scalar momenta. This simple change of kinematic variables

turns out to have important consequences, in particular allowing us to write the gluon

amplitude in a canonical way, completely free of gauge redundancies [1]. In addition, at loop

level, this formulation naturally suggests an extension of kinematics - _surface_ _kinematics_

- that lets us write down well-defined gluon integrands that correctly match all cuts and

are also gauge invariant, before loop integration [15].

Given this progress, it is natural to ask how we can recast well-known features of gluon

amplitudes in this new language, as well as if we can uncover any new properties that are

exposed by this formalism. We will pursue both of these goals in this paper, which is divided

into two parts, linked by the scalar-scaffolding description of gauge invariance. In Part I,

we use scalar-scaffolding to define an on-shell soft limit and study the soft expansion of

gluon amplitudes both at tree-level and one-loop. In Part II, we explain how the expression

of gauge invariance suggests the introduction of simple differential operators acting on indi
vidual external gluons. These operators turn out to have a surprising property: successively

applying them to all but two gluons converts Yang-Mills (YM) amplitudes to amplitudes
for Tr( _ϕ_ [3] ) theory, both at tree-level and one-loop.


**Part** **I:** **Soft** **Limits** **at** **Tree-level** **and** **One-loop**


The study of soft limits in particle scattering is an ancient subject that has revealed many

deep aspects of fundamental physics, starting from Weinberg’s pioneering analysis of the

consistency conditions on theories of massless particles with spin [16, 17].

More recently, soft limits have been understood as part of a much larger narrative in the

modern revival of our understanding of scattering amplitudes. From the on-shell perspec
tive, soft limits are intimately connected with the physics of factorization. For example, in

color-ordered YM amplitudes, a gluon goes soft by becoming collinear with its two adjacent

gluons. Factorization near poles has played a major role in recursive methods to compute

amplitudes [18, 19], and similarly, some advantage has been obtained from behavior of am
plitudes under soft limits [20–26]. In another vein, leading and subleading soft limits can

be interpreted as the appearance of asymptotic symmetries on the celestial sphere [27–31].

Subleading and higher orders in the soft expansion have also been extensively studied in

the literature (at tree-level and beyond) for their own sake; see _e.g._ Refs. [32–37].


                   - 2                   

We start by studying the soft expansion for scalar-scaffolded gluons at tree-level. The

upshot of scalar-scaffolding is that the gluon amplitude has a completely _locked_ form, free

of gauge redundancies. This means that it has a completely well-defined Laurent expansion

in the kinematic variables, and therefore takes a similarly well-defined Laurent expansion

around soft limits. In addition, since the polarizations and momenta of the gluons are

traded for the momenta of 2 _n_ scalars, we can implement the soft expansion directly at

the level of the momentum invariants of the 2 _n_ scalars, allowing us to take the soft limit

while manifesting momentum conservation. Undertaking this limit, we derive leading and

subleading soft terms in this language and understand why there are no universal soft terms

at higher orders in the expansion. For the leading contribution, we find a simple result that

matches Weinberg’s soft theorem:


          - _X_ 2 _n−_ 3 _,_ 2 _n_ _X_ 3 _,_ 2 _n_          _A_ [Gluon] _n_ _→_ + _−_ 1 _× A_ [Gluon] _n−_ 1 _[,]_
_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1


where _Xi,j_ = ( _pi_ + _pi_ +1 + _· · · pj−_ 1) [2] are the planar Mandelstam invariants for the momenta
of the 2 _n_ scalars that scaffold the _n_ gluons.

In Sec. 5, we extend this study to the one-loop YM integrand defined in terms of

_surface_ _kinematics_ [15, 38, 39]. Here, since this extension of kinematics gives the integrand

a well-defined notion of gauge invariance as well as factorization on cuts prior to loop

integration, we may expect to find a statement similar to the one found for the tree-level

answer. Indeed, in the context of NLSM amplitudes [40], we have seen that this particular

kinematic extension can be used to define a pion integrand that makes manifest the Adler

zero directly at the level of the loop integrand (rather than post-loop integration) as well

as admits predictions for its behavior under multi-soft limits [5]. Therefore, it is natural to

ask what this extension gives in the context of the YM integrand soft expansion.

Quite remarkably, we find that, at leading order in the soft expansion, we obtain

precisely the same soft Weinberg term as in the tree-level case plus corrections:




  - _X_ 2 _n,_ 3  _In_ = + _[X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n]_ _−_ 1 _In−_ 1( _s,_ 2 _,_ 3 _, · · ·_ _,_ 2 _n −_ 2) _|S_
_X_ 2 _n−_ 1 _,_ 3 _X_ 2 _n−_ 3 _,_ 1



(1.1)

+ _O_ ( _δ_ [0] ) _._



_∂In−_ 1

_∂Xs,_ 2



+ _[X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n][ −]_ _[X]_ [2] _[n][−]_ [2] _[,]_ [2] _[n]_
���� _S_ _X_ 2 _n−_ 3 _,_ 1



_∂In−_ 1
_∂X_ 2 _n−_ 2 _,s_



���� _S_



+ _Xs,s_




- _X_ 2 _n,_ 3 _−_ _X_ 2 _n,_ 2
_X_ 2 _n−_ 1 _,_ 3



The correction terms are proportional to the tadpole variables _Xi,i_ and therefore translate
into scaleless contributions that vanish upon loop integration. It would be interesting to

understand how this correction interacts with the IR divergences that appear post-loop

integration, a topic we leave to future work.

It is not especially surprising to be able to translate known statements about the soft

expansion into scalar-scaffolding language at tree-level. It is somewhat more remarkable

that the extension of kinematics which makes the one-loop integrand well-defined also plays

nicely with the soft expansion, yielding the expected Weinberg term plus the simple cor
rection factors described above.


                   - 3                   

**Part** **II:** **Transmutation** **of** **Gluons** **into** **Scalars**


As emphasized in Part I, one striking aspect of the scalar-scaffolding formalism is the

fact that it eliminates gauge redundancies, turning gauge invariance and linearity in each

polarization vector into unified statements on the form of the amplitude [1]. In addition to

its utility in defining a soft expansion, this representation of the amplitude suggests that
we study a simple operator _W_ 2 _i_ that acts on the _i_ [th] external gluon:



_W_ 2 _i_ =



2 _i−_ 2



_j_ =2 _i_ +2



_∂_
_._
_∂X_ 2 _i,j_



It turns out that applying this operator to the _n_ -point amplitude produces a much
simpler object, closely related to an amplitude where gluons _i_ _−_ 1 _, i,_ and _i_ +1 are converted
into Tr( _ϕ_ [3] ) scalars. In Sec. 6, we explain that the action of this operator is equivalent to a

special choice for the polarization of gluon _i_ . Additionally, if we act with this operator on
( _n −_ 2) of the gluons, we find that all _n_ gluons have been converted into scalars - transforming the original, pure YM amplitude into a Tr( _ϕ_ [3] ) amplitude! This is a very surprising

fact, but, as we explain in Sec. 7, one is naturally led to discover it by consecutively apply
ing particular types of “split factorizations” [5] that implement the action of this operator
_W_ 2 _i_ .
To understand the action of these operators from splits, we need to define the scalar
scaffolded gluon amplitude via its surface integral formulation [1]. Doing so makes it

straightforward to find other surface integrals that compactly represent the action of any
number of _We_ ’s on the amplitude. Interestingly, after applying ( _n −_ 2) _We_ ’s, we do _not_
land on the surface integral for Tr( _ϕ_ [3] ) amplitudes; acting with the _We_ ’s on all but gluons
_i, j_, we instead find






  _∝_

_Sn_




- _dy_
_y_




 - 1

_u_ _[α]_ _i,j_ _[′][X][i,j]_   - _,_
( _i,j_ ) _∈Sn_ ( _k,m_ ) _∈SL_ _[u][k,m][ ×]_ [ �] ( _k,m_ ) _∈SR_ _[u][k,m]_



_i_ + 1





which is the surface integral for Tr( _ϕ_ [3] ) under the kinematic shift _Xi,j_ _→_ _Xi,j −_ 1 _/α_ _[′]_, if ( _i, j_ )
is a curve in _SL_ or in _SR_ (including boundary curves ( _i_ + 1 _, j_ ) and ( _i, j_ + 1)). Nonetheless,
in Sec. 7.3, we show that this class of shifted integrals indeed yields Tr( _ϕ_ [3] ) amplitudes at
low energies! It is amusing that, while some simple kinematic shifts take us from Tr( _ϕ_ [3] )
to pion and gluon amplitudes, others return us to Tr( _ϕ_ [3] ) at low energies, while of course
differing in the UV and at higher orders in the _α_ _[′]_ expansion.

In summary, to understand the features of these operators, we are forced to go back to

the definition of gluon amplitudes via surface integrals. It was in this context that scalarscaffolded gluon amplitudes were discovered as a simple shift of the Tr( _ϕ_ [3] ) amplitudes.
Now, we are finding an “opposite” connection - by applying ( _n −_ 2) _We_ ’s, we can start
from the surface integral for gluons and land on one that gives Tr( _ϕ_ [3] ) at low energies!


                   - 4                   

To conclude Part II, we explain how these operators have a natural extension to the

scalar-scaffolding formulation of loop integrands. We find that, by defining the one-loop

integrand using _surface_ _kinematics_ in the obvious way, the tree-level story beautifully ex
tends to the YM surface integrand: acting with _n_ of these loop operators turns the gluon
integrand to the Tr( _ϕ_ [3] ) one! It is natural to conjecture that this statement can be similarly

proven directly at the level of surface integrals using splits [5], but we leave this discussion

for future work.


**2** **A** **Review** **of** **Scalar-Scaffolded** **Gluons**


In order to make our presentation in this paper self-contained, in this section we give a

review of the main aspects of the scalar-scaffolding formalism, as well as some examples

of what gluon tree-level amplitudes and one-loop integrands look like when recast in this

language.

For the purposes of this paper, the most important aspect of this formalism is that

it allows us to define the kinematics for gluon scattering amplitudes in a canonical way,
encoding both on-shell gluon momenta _qi_ _[µ]_ [with] _[q]_ _i_ [2] [=] [0][,] [and] [transverse] [polarizations] _[ϵ][µ]_ _i_
with _ϵi · qi_ = 0. As a result, in this representation the amplitude has a _unique_ form. This
is to be contrasted with standard expressions for gluon amplitudes using momenta and

polarization vectors. Here, the expressions are always ambiguous. For instance, we can
use momentum conservation to express one of the momenta _qi_ _[µ]_ [in] [terms] [of] [the] [sum] [of] [all]
the rest, so that any occurrence of _qi · qj_ can be replaced with _−_ [�] _k_ = _i,j_ _[q][k]_ _[·][ q][j]_ [.] [Similarly,]
_qi_ _· ϵj_ can be replaced with _−_ [�] _k_ = _i,j_ _[q][k]_ _[·][ ϵ][j]_ [.] [Of] [course] [these] [ambiguities] [can] [be] [resolved]
by deciding to solve for _e.g._ _qn_ _[µ]_ [in] [terms] [of] [all] [the] [rest,] [but] [this] [is] [unnatural,] [breaking] [the]
cyclic symmetry of the problem. Scalar-scaffolding gives an invariant way to express the

amplitudes without breaking any of the symmetries, by giving a physical picture for the

production of the momenta and polarizations of the external gluons from pairs of scalars.

The linearity of gluon amplitudes in polarization vectors, as well as the on-shell gauge
invariance under _ϵµ_ _→_ _ϵµ_ + _αqµ_, are reflected in a natural way in the scaffolding picture.
These conditions force the amplitude to be written in a particular form - the launching

point to the discovery of important features about the amplitude in Part I and Part II.

In Sec. 2.1, we review how the kinematic invariants of gluon amplitudes can be recast

as momentum dot products of the scalars that scaffold the gluons. At tree-level, this allows
us to write the gluon amplitude in terms of planar Mandelstam variables _Xi,j_, each of which
is naturally associated to a curve on a disk with marked points on the boundary. We review
how the statements of gauge invariance and multi-linearity in the polarizations _ϵ_ _[µ]_ _i_ [translate]
into these _X_ ’s, as well as give the expression for the factorization on a given cut at _Xi,j_ = 0.
In Sec. 2.2, we flash some explicit examples of the three- and four-point gluon amplitudes

written in this language.

In Sec. 2.3, we give a review of the scalar-scaffolded gluon one-loop integrand formulated

in terms of _surface_ _kinematics_ . As explained in Ref. [15], this kinematic extension — which

comes from identifying kinematic variables with labelings of curves on the punctured disk —

will allow us to write down an object endowed with a generalized notion of gauge invariance


                   - 5                   

and well-defined cuts directly at the level of the integrand. These features will play a crucial

role in Part I and Part II when we generalize the results found at tree-level to one-loop.


**2.1** **How** **to** **scalar-scaffold** **gluons**


As prefaced in Sec. 1, we want to think of the gluons in a YM amplitude (or integrand) as

being _scalar-scaffolded_ ; that is, we think of each external gluon as being produced by two

massless colored scalars [1]. Concretely, let’s say we have an external gluon with momentum
_q_ 1 _[µ]_ [in] [an] [amplitude.] [As] [shown] [in] [Eq.] [(][2.1][),] [we] [quite] [literally] [“scaffold”] [the] [gluon] [with] [two]
scalars with momenta _p_ _[µ]_ 1 [and] _[ p]_ 2 _[µ]_ [.] [Since the scalars couple to the gluon via minimal coupling,]
we are then able to encode the polarization vector _ϵ_ _[µ]_ 1 [and] [on-shell] [gluon] [momentum] _[q]_ 1 _[µ]_ [in]
terms of the scalar momenta _p_ _[µ]_ 1 [and] _[p][µ]_ 2 [in] [the] [following] [way:]





_q_ 1 _[µ]_ _[∝]_ _[g]_ YM _[p][µ]_ 2 _⇒_




_q_ 1 _[µ]_ [=] _[ p]_ 1 _[µ]_ [+] _[ p]_ 2 _[µ][,]_

(2.1)
_ϵ_ _[µ]_ 1 [=] _[ p]_ 2 _[µ]_ _[−]_ _[α]_ [1][(] _[p]_ [1][ +] _[ p]_ [2][)] _[µ][,]_



where _α_ 1 is a gauge-dependent parameter that should drop out of the final amplitude.
Of course, in addition to the fact that the scalar momenta are on-shell, we also need the
gluon momentum to be on-shell. That is, we must require ( _p_ 1 + _p_ 2) [2] = 0, from which we
automatically find that _ϵ_ 1 _· q_ 1 = 0. This means that, via scalar-scaffolding, we always get
gluon amplitudes with null polarizations; however, this is enough since we can write any

polarization as a linear combination of null ones. In this way, we can represent an _n_ -point
gluon amplitude in terms of the momenta of 2 _n_ scalars satisfying ( _p_ 2 _i−_ 1 + _p_ 2 _i_ ) [2] = 0 for
_i_ = 1 _,_ 2 _, . . ., n_ .

Thus, the kinematic variables on which the _n_ -point gluon amplitude depends are the

_same_ as those of the 2 _n_ -point scalar amplitude, minus those lost due to the gluon on-shell

conditions.

To keep track of these scalar invariants, it is useful to introduce the so-called _momentum_

_polygon_ . An example for the case of five gluons (so ten scalars) is given in Fig. 1. To

construct the momentum polygon, we draw the momentum of each scaffolded scalar tipto-toe according to the standard ordering 1 _,_ 2 _, . . .,_ 2 _n −_ 1 _,_ 2 _n_, obtaining a closed 2 _n_ -gon

that manifests momentum conservation. By construction, the vector associated with the

chord from vertex _i_ to vertex _j_ in the 2 _n_ -gon is equal to the sum of the momenta of the
enclosed scalars _p_ _[µ]_ _i_ [+] _[ p]_ _i_ _[µ]_ +1 [+] _[ · · ·]_ [ +] _[ p]_ _j_ _[µ]_ _−_ 1 [.] [In] [this] [way,] [the] _[length]_ _[squared]_ [of] [these] [chords] [may]
be identified with the set of planar Mandelstam invariants, which are exactly the variables

that appear in the poles of planar diagrams:


_Xi,j_ = ( _pi_ + _pi_ +1 + _. . ._ + _pj−_ 1) [2] _._ (2.2)


Let’s now do a counting exercise. For the 2 _n_ -gon, there are 2 _n_ (2 _n_ _−_ 3) _/_ 2 chords,

matching the number of independent Mandelstam invariants appearing in a 2 _n_ -point scalar


                   - 6                   

**Figure** **1** : (Left) The momentum polygon for ten scalars (in black), drawn inside the disk
with marked points on the boundary (in dashed). The scaffolding chords/ curves on the
disk (in blue) are labeled by _Xi,i_ +2 for odd _i_ . (Right) In blue, we highlight the five-point
gluon momentum polygon with edges _qi_ _[µ]_ [, inscribed inside the scalar polygon.] [After putting]
the gluons on-shell by taking the scaffolding curves to zero, we are left with the five-point
gluon amplitude (in center).


amplitude. [1] But, in order to describe gluon kinematics we must further set the so-called
_scaffolding_ _chords_ _X_ 2 _i−_ 1 _,_ 2 _i_ +1 = ( _p_ 2 _i−_ 1 + _p_ 2 _i_ ) [2] = 0. This brings us down to 2 _n_ (2 _n −_ 3) _/_ 2 _−_
_n_ independent _X_ ’s, which is precisely the number of degrees of freedom of the _n_ -point

gluon amplitude. Therefore, the scalar variables (with the scaffolding conditions) furnish

basis of kinematic space for tree-level gluon amplitudes, where momentum conservation

is _automatically_ enforced from the fact that the _X_ ’s are chords of a _closed_ momentum

polygon.

We can equivalently think of the momentum polygon as inscribed in a disk with marked

points on the boundary (depicted in dashed gray on the _l.h.s._ of Fig. 1), where each bound
ary component is assigned the momentum of the respective edge of the momentum polygon.
In this picture, the kinematic invariants _Xi,j_ are now identified with _curves_ on the surface
(the disk), and we can read off the momentum in a given curve by _homology_, _i.e._, by de
forming the curve to a collection of boundary curves and adding their momenta. So, from

this point of view, this space of curves also defines a basis for the kinematic invariants of
the gluon amplitude, once we again go on the scaffolding locus _X_ 2 _i−_ 1 _,_ 2 _i_ +1 = 0. As we will
see momentarily, defining the basis of kinematic invariants in this way will turn out to be

especially crucial for the one-loop integrand.

The scaffolding curves  - marked in blue in Fig. 1  - form an inscribed _n_ -gon, cor
responding to the actual _gluon_ momentum _n_ -gon, where each edge is associated with a
gluon momentum _qi_ _[µ]_ [.] [All] [of] [the] [chords/] [curves] [living] [purely] [inside] [this] [smaller] _[n]_ [-gon] [are]
identified with invariants containing sums of gluon momenta. These are precisely the _Xi,j_ ’s
where both _i_ and _j_ are _odd_, and they are the variables allowed to appear as poles in the


1This is under the assumption that _d_, the dimensionality of spacetime, is sufficiently large, so that we
can ignore Gram determinant constraints. We will assume this throughout the paper unless said otherwise.


                   - 7                   

gluon amplitude. The remaining chords (where one of _i, j_ is even) encode information related to the polarizations, in the form of the dot products _qk · ϵm_ and _ϵk · ϵm_ . The explicit
correspondence depends on the gauge parameter _αi_, but one can easily read it off using the
map (2.1).

To summarize, we can use the scalar-scaffolding representation to write the gluon _n_  point amplitude _An_ ( _qi_ _· qj, ϵi_ _· qj, ϵi_ _· ϵj_ ) purely in terms of the kinematics of 2 _n_ scalars
_An_ ( _Xi,j_ ). [2] It is then natural to ask how well-known aspects of amplitudes translate into
this language. For our present purposes, we will need to understand (1) what the statement

of gauge invariance is in terms of the _X_ ’s, and (2) what the spin-sum gluing rule looks like

when we localize on a particular pole.

As explained in Ref. [1], in scalar variables the statement of gauge invariance comes
together with linearity in the polarization of the _i_ [th] gluon. Due to these two requirements,
we find that the amplitude _An_ must be linear in each _X_ 2 _i,j_, and that this linearity must be
such that the full amplitude can be written in the forms [1]




- _An_ (1 _,_ 2 _, . . .,_ 2 _n_ ) = [�] _j_ = _{_ 2 _i,_ 2 _i±_ 1 _}_ [(] _[X]_ [2] _[i,j]_ _[−]_ _[X]_ [2] _[i][−]_ [1] _[,j]_ [)] _[Q]_ [2] _[i,j][,]_



_._ (2.3)
_∂X_ 2 _i,j_



_An_ (1 _,_ 2 _, . . .,_ 2 _n_ ) = [�] _j_ = _{_ 2 _i,_ 2 _i±_ 1 _}_ [(] _[X]_ [2] _[i,j]_ _[−]_ _[X]_ [2] _[i][−]_ [1] _[,j]_ [)] _[Q]_ [2] _[i,j][,]_

with _Q_ 2 _i,j_ = _[∂][A][n]_
_An_ (1 _,_ 2 _, . . .,_ 2 _n_ ) = [�] _j_ = _{_ 2 _i,_ 2 _i±_ 1 _}_ [(] _[X]_ [2] _[i,j]_ _[−]_ _[X]_ [2] _[i]_ [+1] _[,j]_ [)] _[Q]_ [2] _[i,j][,]_ _∂X_ 2



These forms make manifest both invariance under a gauge transformation in the _i_ [th] gluon,
_An_ ( _ϵ_ _[µ]_ _i_ _[→]_ _[ϵ]_ _i_ _[µ]_ [+] _[ αq]_ _i_ _[µ]_ [) =] _[ A][n]_ [(] _[ϵ]_ _i_ _[µ]_ [)][,] [as] [well] [as] [linearity] [in] [the] [respective] [polarization,] _[A][n]_ [(] _[βϵ][µ]_ _i_ [) =]
_βAn_ ( _ϵ_ _[µ]_ _i_ [)][.] [We] [therefore] [see] [that] [these] [two] [statements] [—] [distinct] [in] [the] [ordinary] [gluon]
language - are naturally unified in the scalar-scaffolding language. In particular, if we

subtract the two representations in Eq. (2.3), we find the following identity that the ampli
tude must satisfy

     
_[∂][A][n]_



( _X_ 2 _i_ +1 _,j_ _−_ _X_ 2 _i−_ 1 _,j_ ) _[∂][A][n]_

_∂X_ 2

_j_



= 0 _,_ (2.4)
_∂X_ 2 _i,j_



which is the scaffolding representation of gauge invariance. In Sec. 2.3, we explain how

these statements extend to the surface one-loop [15].

It is likewise straightforward to translate the polarization sum appearing in gluon fac
torization channels into scalar language. As demonstrated in Ref. [1], the residue on a gluon
propagator _Xi,j_ = 0 (with _i_ and _j_ both odd) can be written in terms of the _X_ ’s as follows:




 
( _Xk,m −_ _Xk,j_ _−_ _Xm,i_ ) _[∂][A][L]_

_∂Xk,x_

_k∈L,_ _m∈R_


 
( _Xk,m −_ _Xk,i −_ _Xm,j_ ) _[∂][A][L]_

_∂Xk,x_

_k∈L,_ _m∈R_




  Res [=]
_Xi,j_ =0 _[A][n]_



_∂AR_

_[∂][A][L]_ _×_ _,_

_∂Xk,xL_ _∂Xm,xR_



(2.5)




 =



_∂AR_

_[∂][A][L]_ _×_

_∂Xk,xL_ _∂Xm,xR_



where we can move from the first line to the second line by using the constraint (2.4)
in both _xL_ and _xR_ . In the above formula, we have _L_ = _{i_ + 1 _, i_ + 2 _, · · ·_ _, j_ _−_ 1 _}_ and
_R_ = _{j_ + 1 _, j_ + 2 _, · · ·_ _, i −_ 1 _}_, and _AL_ and _AR_ are the two lower-point gluon amplitudes we


2For the remainder of this paper, we will denote the normal-ordered 2 _n_ -point scalar-scaffolded gluon
amplitude as _An_ (1 _,_ 2 _, . . .,_ 2 _n_ ), where we always implicitly assume that we are on the support of _X_ 2 _i−_ 1 _,_ 2 _i_ +1 =
0.


                   - 8                   

**Figure** **2** : (Top) Tree-level factorization at _Xi,j_ = 0 into two lower-point tree amplitudes,
_AL_ and _AR_ . (Bottom) Tree-loop factorization of the integrand at _Xi,j_ = 0 into a lowerpoint tree amplitude _AL_ and a lower-point one-loop integrand, _IR_ .


obtain when the propagator _Xi,j_ goes on-shell. This factorization is depicted geometrically
on the _l.h.s._ of Fig. 2, where we see that these lower-point amplitudes depend on the indices
to the left (right) of chord _Xi,j_ as well as on a new index associated with the summed-over
polarization of the intermediate gluon. So, the kinematic dependence of these amplitudes
are given by _AL_ _≡AL_ ( _i, i_ + 1 _, · · ·_ _, j −_ 1 _, j, xL_ ) and _AR_ _≡AR_ ( _i, xR, j, j_ + 1 _, · · ·_ _, i −_ 1).


**2.2** **Examples** **at** **three-** **and** **four-points**


We now present some simple examples of what YM amplitudes look like when cast in terms
of the scalar-scaffolded variables _Xi,j_ . Let’s start with the simplest case of the three-point
gluon interaction. Applying the mapping (2.1) to each one of the three gluons, we obtain


_A_ 3(1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6) = _X_ 1 _,_ 4 _X_ 2 _,_ 6 + _X_ 3 _,_ 6 _X_ 2 _,_ 4 + _X_ 2 _,_ 5 _X_ 4 _,_ 6 _−_ _X_ 2 _,_ 5 _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 4 _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 4 _X_ 2 _,_ 5 _._ (2.6)


Using this expression, we can demonstrate gauge invariance and linearity in gluon 1 by
checking that dependence in the _X_ 2 _,j_ goes as in Eq. (2.3), with _i_ = 1. Indeed, using
Eq. (2.3), we can make gauge invariance and linearity in gluon 1 manifest by writing _A_ 3 as


                   - 9                   

follows:
_A_ 3 = ( _X_ 2 _,_ 4 _−_ _X_ 1 _,_ 4) _X_ 3 _,_ 6 + _X_ 2 _,_ 5( _X_ 4 _,_ 6 _−_ _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 4) + _X_ 2 _,_ 6 _X_ 1 _,_ 4
(2.7)
= _X_ 2 _,_ 4 _X_ 3 _,_ 6 + _X_ 2 _,_ 5( _X_ 4 _,_ 6 _−_ _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 4) + ( _X_ 2 _,_ 6 _−_ _X_ 3 _,_ 6) _X_ 1 _,_ 4 _,_


since we set the chords _X_ 1 _,_ 5 = _X_ 1 _,_ 6 = 0 and _X_ 3 _,_ 4 = _X_ 3 _,_ 5 = 0. Of course, we can also write
_A_ 3 in a form that makes gauge invariance in gluon 2 or gluon 3 manifest; in these cases,
we would examine linearity in _X_ 4 _,j_ or _X_ 6 _,j_, respectively.
As for the four-point YM amplitude, using the fact that it has a unique form in scalar
scaffolded variables, it is meaningful to decompose it in a Laurent expansion as



_A_ 4(1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _,_ 7 _,_ 8) = _[R]_ [1] _[,]_ [5]




[3] _[,]_ [7]

+ _C_ [(4)] _,_ (2.8)
_X_ 3 _,_ 7




_[R]_ [1] _[,]_ [5] + _[R]_ [3] _[,]_ [7]

_X_ 1 _,_ 5 _X_ 3 _,_ 7



where _R_ 1 _,_ 5 and _R_ 3 _,_ 7 are the residues of _A_ 4 at _X_ 1 _,_ 5 = 0 and _X_ 3 _,_ 7 = 0, respectively, and _C_ [(4)]

the pure contact part. To be explicit, here _R_ 1 _,_ 5 is independent of _X_ 1 _,_ 5 and _R_ 3 _,_ 7 is independent of _X_ 3 _,_ 7. It is worth stressing this basic point again: the amplitudes have a completely
canonical Laurent expansion in the _X_ variables, but individual terms in the expansion (like

the ones shown in the above equation) are not gauge invariant. Gauge invariance is then an

interesting statement that relates different terms in the Laurent expansion to each other.
We can write the residues in terms of _Xi,j_ ’s as follows:


_R_ 1 _,_ 5 = _−_ _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 7 _−_ _X_ 1 _,_ 4 _X_ 5 _,_ 8 _X_ 2 _,_ 7 + _X_ 1 _,_ 4 _X_ 6 _,_ 8 _X_ 2 _,_ 7 + _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 2 _,_ 8 + _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 3 _,_ 7

_−_ _X_ 1 _,_ 6 _X_ 2 _,_ 4 _X_ 3 _,_ 7 + _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 7 _−_ _X_ 1 _,_ 4 _X_ 1 _,_ 6 _X_ 3 _,_ 8 + _X_ 1 _,_ 6 _X_ 2 _,_ 4 _X_ 3 _,_ 8 _−_ _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 3 _,_ 8

_−_ _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 4 _,_ 7 + _X_ 1 _,_ 6 _X_ 2 _,_ 5 _X_ 4 _,_ 8 _−_ _X_ 1 _,_ 6 _X_ 2 _,_ 4 _X_ 5 _,_ 8 + _X_ 1 _,_ 4 _X_ 2 _,_ 6 _X_ 5 _,_ 8 _−_ _X_ 1 _,_ 4 _X_ 3 _,_ 6 _X_ 5 _,_ 8
+ _X_ 2 _,_ 4 _X_ 3 _,_ 6 _X_ 5 _,_ 8 _−_ _X_ 2 _,_ 5 _X_ 3 _,_ 6 _X_ 5 _,_ 8 + _X_ 1 _,_ 4 _X_ 3 _,_ 7 _X_ 5 _,_ 8 _−_ _X_ 2 _,_ 4 _X_ 3 _,_ 7 _X_ 5 _,_ 8 + _X_ 2 _,_ 5 _X_ 3 _,_ 7 _X_ 5 _,_ 8
+ _X_ 2 _,_ 5 _X_ 4 _,_ 6 _X_ 5 _,_ 8 _−_ _X_ 2 _,_ 5 _X_ 4 _,_ 7 _X_ 5 _,_ 8 _−_ _X_ 1 _,_ 4 _X_ 2 _,_ 5 _X_ 6 _,_ 8 _−_ _X_ 1 _,_ 4 _X_ 3 _,_ 7 _X_ 6 _,_ 8 + _X_ 2 _,_ 4 _X_ 3 _,_ 7 _X_ 6 _,_ 8

_−_ _X_ 2 _,_ 5 _X_ 3 _,_ 7 _X_ 6 _,_ 8 + _X_ 2 _,_ 5 _X_ 4 _,_ 7 _X_ 6 _,_ 8 _,_


_R_ 3 _,_ 7 = _−_ _X_ 1 _,_ 4 _X_ 2 _,_ 7 _X_ 3 _,_ 6 + _X_ 1 _,_ 5 _X_ 2 _,_ 7 _X_ 3 _,_ 6 + _X_ 1 _,_ 4 _X_ 2 _,_ 8 _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 5 _X_ 2 _,_ 8 _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 4 _X_ 3 _,_ 8 _X_ 3 _,_ 6
+ _X_ 1 _,_ 5 _X_ 3 _,_ 8 _X_ 3 _,_ 6 + _X_ 2 _,_ 4 _X_ 3 _,_ 8 _X_ 3 _,_ 6 _−_ _X_ 2 _,_ 5 _X_ 3 _,_ 8 _X_ 3 _,_ 6 _−_ _X_ 2 _,_ 8 _X_ 4 _,_ 7 _X_ 3 _,_ 6 + _X_ 2 _,_ 7 _X_ 4 _,_ 8 _X_ 3 _,_ 6

_−_ _X_ 2 _,_ 7 _X_ 5 _,_ 8 _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 5 _X_ 2 _,_ 7 _X_ 4 _,_ 6 + _X_ 1 _,_ 5 _X_ 2 _,_ 8 _X_ 4 _,_ 6 _−_ _X_ 1 _,_ 5 _X_ 3 _,_ 8 _X_ 4 _,_ 6 + _X_ 2 _,_ 5 _X_ 3 _,_ 8 _X_ 4 _,_ 6

_−_ _X_ 2 _,_ 7 _X_ 3 _,_ 8 _X_ 4 _,_ 6 + _X_ 1 _,_ 5 _X_ 2 _,_ 7 _X_ 4 _,_ 7 _−_ _X_ 1 _,_ 6 _X_ 2 _,_ 7 _X_ 4 _,_ 7 _−_ _X_ 1 _,_ 5 _X_ 2 _,_ 8 _X_ 4 _,_ 7 + _X_ 1 _,_ 6 _X_ 2 _,_ 8 _X_ 4 _,_ 7
+ _X_ 1 _,_ 5 _X_ 3 _,_ 8 _X_ 4 _,_ 7 _−_ _X_ 1 _,_ 6 _X_ 3 _,_ 8 _X_ 4 _,_ 7 _−_ _X_ 2 _,_ 5 _X_ 3 _,_ 8 _X_ 4 _,_ 7 + _X_ 2 _,_ 6 _X_ 3 _,_ 8 _X_ 4 _,_ 7 + _X_ 2 _,_ 7 _X_ 4 _,_ 6 _X_ 5 _,_ 8

_−_ _X_ 2 _,_ 7 _X_ 4 _,_ 7 _X_ 5 _,_ 8 + _X_ 2 _,_ 7 _X_ 4 _,_ 7 _X_ 6 _,_ 8 _._
(2.9)


                   - 10                   

The contact part is given by


_C_ [(4)] = _−_ _X_ 1 _,_ 5 _X_ 2 _,_ 7 + _X_ 1 _,_ 4 _X_ 2 _,_ 7 + _X_ 1 _,_ 6 _X_ 2 _,_ 7 + _X_ 5 _,_ 8 _X_ 2 _,_ 7 _−_ _X_ 6 _,_ 8 _X_ 2 _,_ 7 _−_ _X_ 1 _,_ 4 _X_ 2 _,_ 8 + _X_ 1 _,_ 5 _X_ 2 _,_ 8

_−_ _X_ 1 _,_ 6 _X_ 2 _,_ 8 + _X_ 1 _,_ 4 _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 5 _X_ 3 _,_ 6 _−_ _X_ 2 _,_ 4 _X_ 3 _,_ 6 + _X_ 2 _,_ 5 _X_ 3 _,_ 6 _−_ _X_ 1 _,_ 4 _X_ 3 _,_ 7 + _X_ 1 _,_ 5 _X_ 3 _,_ 7

_−_ _X_ 1 _,_ 6 _X_ 3 _,_ 7 + _X_ 2 _,_ 4 _X_ 3 _,_ 7 _−_ _X_ 2 _,_ 5 _X_ 3 _,_ 7 + _X_ 1 _,_ 4 _X_ 3 _,_ 8 _−_ _X_ 1 _,_ 5 _X_ 3 _,_ 8 + _X_ 1 _,_ 6 _X_ 3 _,_ 8 _−_ _X_ 2 _,_ 4 _X_ 3 _,_ 8
+ _X_ 2 _,_ 5 _X_ 3 _,_ 8 + _X_ 1 _,_ 5 _X_ 4 _,_ 6 _−_ _X_ 2 _,_ 5 _X_ 4 _,_ 6 + _X_ 2 _,_ 8 _X_ 4 _,_ 6 _−_ _X_ 1 _,_ 5 _X_ 4 _,_ 7 + _X_ 1 _,_ 6 _X_ 4 _,_ 7 + _X_ 2 _,_ 5 _X_ 4 _,_ 7

_−_ _X_ 2 _,_ 6 _X_ 4 _,_ 8 + _X_ 3 _,_ 6 _X_ 5 _,_ 8 _−_ _X_ 3 _,_ 7 _X_ 5 _,_ 8 _−_ _X_ 4 _,_ 6 _X_ 5 _,_ 8 + _X_ 4 _,_ 7 _X_ 5 _,_ 8 + _X_ 2 _,_ 4 _X_ 6 _,_ 8 + _X_ 3 _,_ 7 _X_ 6 _,_ 8

_−_ _X_ 4 _,_ 7 _X_ 6 _,_ 8 _._
(2.10)


**2.3** **Surface** **kinematics** **and** **the** **one-loop** **gluon** **integrand**


Just as at tree-level, we can think of the gluons entering into a one-loop process as scalar
scaffolded, such that their momenta and polarizations are given in terms of the momenta

of the scalars by (2.1). Similarly, we can draw the scalar momentum polygon and inscribe

it in a disk with marked points on the boundary, assigning boundary components of the

disk to the momenta of the edges of the polygon just as in Fig. 1. But now, at one-loop,

the disk is a punctured disk.

At tree-level, we saw that the space of curves on the disk was in one-to-one correspondence with the basis of kinematic invariants for the 2 _n_ -point scalar problem; _Xi,j_ was
naturally associated to the curve going from _i_ to _j_, where we could read off its momen
tum by _homology_ . However, at one-loop, due to the presence of the puncture, the space of

curves now includes not only curves going from _i_ to _j_, but also those ending on the puncture
_Xi,p_, where _p_ stands for the puncture index. These chords are precisely those kinematic
invariants that should include the loop-momentum _l_ _[µ]_ .

This means that, in order to be able to assign momentum to all the curves of the
punctured disk, we have to associate momentum _l_ _[µ]_ to one of the curves ending on the
puncture; see the _l.h.s._ of Fig. 3. [3] Having done this, the situation is just like that at tree
level, where the space of curves of the punctured disk (up to homology) is in one-to-one

correspondence with the space of scalar integrand invariants. By further going to the locus
where the scaffolding curves _X_ 2 _i−_ 1 _,_ 2 _i_ +1 = 0, we define a basis for the invariants of the gluon
integrand for general spacetime dimension _d_ (large enough such that there are no Gram

determinant constraints).

The presence of the puncture introduces a novelty at loop-level not seen for trees:

there are an infinite number of curves one can draw on the punctured disk up to homotopy,

corresponding to the curves that self-intersect while going around the puncture (see the

_r.h.s._ of Fig. 3). However, since the puncture carries no momentum, these curves are all

_homologous_ to each other, so that up to homology we still have a finite number of curves. For

example, in Fig. 3, we draw three homotopically distinct curves which are all assigned the
same momentum: the once-self-intersecting curve _X_ 2 [(1)] _,_ 6 [,] [as] [well] [as] _[X]_ [2] _[,]_ [6] [and] _[X]_ [6] _[,]_ [2][,] [which] [do]
not self-intersect by go from 2 to 6 in different ways around the puncture. In particular, this


3This is in addition to giving to each boundary curve an external gluon momentum, just as we did at
tree-level.


                   - 11                   

**Figure** **3** : (Left) To define a basis of homology at one-loop, one has to further assign a
momentum _l_ _[µ]_ to one of the curves ending on the puncture. Doing this, we can then read
off the momenta of the remaining curves; for example, with _X_ 9 _,p_ = _l_ [2], we find by homology
that _X_ 7 _,p_ has momentum ( _p_ 7 + _p_ 8 + _l_ ) [2] . (Right) In red, we show examples of curves that
are homologous to each other and therefore are assigned the same momentum in standard
kinematics. In surface kinematics, we have instead _X_ 2 [(1)] _,_ 6 [=] _[ X]_ [2] _[,]_ [6] [and] _[X]_ [2] _[,]_ [6] [=] _[ X]_ [6] _[,]_ [2][.] [In] [green,]
we have drawn curves that are assigned zero momentum in standard kinematics, but which
are given a non-zero labeling in surface kinematics.


means that curves which are homologous to boundary curves are assigned zero momentum

by the on-shell condition. On the _r.h.s._ of Fig. 3, we present examples of such curves in
green. First, we have curve _X_ 9 _,_ 7, which is homologous to the scaffolding curve _X_ 7 _,_ 9 = 0. We
also show curve _X_ 9 _,_ 9 (homologous to nothing) and _X_ 8 [(1)] _,_ 9 [(homologous] [to] [a] [scalar] [boundary]
curve). The curves _Xi,i_ are dual to the propagators that appear in diagrams with tadpoles
at one-loop [1, 15]. Of course, when we define the physical integrand, we usually remove

these by-hand, since they give rise to scaleless integrals that vanish upon loop integration.
Similarly, curves like _X_ 9 _,_ 7 are dual to the propagators of diagrams with external gluon
bubbles, which we also remove from the integrand for the same reason; see Ref. [15] for

more details.

Therefore, just like at tree-level, we can recast the gluon one-loop integrand using scalar
variables _Xi,j_ that are naturally associated to the curves (up to homology) of the punctured
disk. However, by doing this we will still run into the standard problems regarding gluon

integrands: as just discussed, we will have to remove the contributions coming from tadpoles

and external bubble diagrams (since these give 1 _/_ 0 divergences). This leads to a non-gauge
invariant object, whose cuts don’t match gluing of lower-order amplitudes.

It was proposed in Ref. [15] that these problems can be ameliorated by considering

an integrand defined under a generalization of kinematics - _surface_ _kinematics_ . In this

formalism, one really assigns a kinematic variable to _each_ curve on the surface: instead
of identifying curves up to homology, we let curves _Xi,j_ and _Xj,i_ be different, but we
still identify _Xi,j_ [(] _[q]_ [)] [=] _[X][i,j]_ [(for] _[q]_ [the] [self-intersection] [number)] [for] [all] [curves] [other] [than] [the]

boundary curves. For these curves, we crucially keep _Xi,i_ [(1)] +1 [not] [equal] [to] [zero] [while] [still]
identifying with it all higher-self-intersecting curves. Thus, all the curves in green in Fig. 3


                   - 12                   

have their own kinematic variable, other than _X_ 2 [(1)] _,_ 6 [which] [is] [set] [to] [be] [equal] [to] _[X]_ [2] _[,]_ [6][.]
The _n_ -point YM integrand defined under surface kinematics  - which we will call the
_surface_ _integrand_ _In_ _≡In_ (1 _,_ 2 _, . . .,_ 2 _n_ ) - is naturally produced as the low-energy limit of
a surface integral [1, 15]. For most of this paper, the details of the surface integrals behind

tree and loop gluon amplitudes are irrelevant, and we will review the important aspects as

they occur in the rest of paper. For now, what is important is to discuss the remarkable

features of this object — namely how it manifests gauge invariance by generalizing Eq. (2.3)
and has a well-defined spin-sum gluing rule for the cuts as in Eq. (2.5). [4]


According to Ref. [15], gauge invariance and multi-linearity in gluon _i_ means that we

can write the surface integrand as



_∂Xj,_ 2 _i_







_In_ = 

_j_ =2 _i_


 =


_j_ =2 _i_




( _X_ 2 _i,j_ _−_ _X_ 2 _i−_ 1 _,j_ ) _[∂][I][n]_




_[∂][I][n]_ + ( _Xj,_ 2 _i −_ _Xj,_ 2 _i−_ 1) _[∂][I][n]_

_∂X_ 2 _i,j_ _∂Xj,_ 2



(2.11)




       - _∂In_ _∂In_
+ _X_ 2 _i−_ 2 _,_ 2 _i−_ 1 _×_ +
_∂X_ 2 _i−_ 2 _,_ 2 _i_ _∂X_ 2 _i−_ 2 _,_ 2 _i−_ 1



����2 _i→_ 2 _i−_ 1




( _X_ 2 _i,j_ _−_ _X_ 2 _i_ +1 _,j_ ) _[∂][I][n]_



_∂Xj,_ 2 _i_




_[∂][I][n]_ + ( _Xj,_ 2 _i −_ _Xj,_ 2 _i_ +1) _[∂][I][n]_

_∂X_ 2 _i,j_ _∂Xj,_ 2










_,_




       - _∂In_ _∂In_
+ _X_ 2 _i_ +1 _,_ 2 _i_ +2 _×_ +
_∂X_ 2 _i,_ 2 _i_ +2 _∂X_ 2 _i_ +1 _,_ 2 _i_ +2



����2 _i→_ 2 _i_ +1



where _j_ runs over all indices including the puncture. (Of course, when _j_ = _p_ we only get a
single factor inside the brackets since _X_ 2 _i,p_ = _Xp,_ 2 _i_ .) This statement is very similar to the
one found at tree-level (2.3), differing only by a correction term proportional to boundary
curves _Xi,i_ +1 _≡_ _Xi,i_ [(1)] +1 [.] [Likewise,] [at] [one-loop] [the] [identity] [(][2.4][)] [generalizes] [nicely] [to] [the]
statement




- _∂In_
+
_∂X_ 2 _i−_ 2 _,_ 2 _i_



_∂Xj,_ 2 _i_






_j_ =2 _i_




( _X_ 2 _i_ +1 _,j_ _−_ _X_ 2 _i−_ 1 _,j_ ) _[∂][I][n]_




_[∂][I][n]_ + ( _Xj,_ 2 _i_ +1 _−_ _Xj,_ 2 _i−_ 1) _[∂][I][n]_

_∂X_ 2 _i,j_ _∂Xj,_




+ _X_ 2 _i−_ 2 _,_ 2 _i−_ 1




- _∂In_ _∂In_
+
_∂X_ 2 _i,_ 2 _i_ +2 _∂X_ 2 _i_ +1 _,_ 2 _i_ +2



����2 _i→_ 2 _i_ +1




= 0 _,_



_∂In_
+
_∂X_ 2 _i−_ 2 _,_ 2 _i−_ 1



����2 _i→_ 2 _i−_ 1





_−_ _X_ 2 _i_ +1 _,_ 2 _i_ +2



(2.12)

which once more is the same as Eq. (2.4) up to some correction terms proportional to curves
_Xi,i_ +1.
Finally, on a cut of the integrand through a tree-level propagator (a “tree-loop cut”),


4Maybe the most remarkable feature of the surface integrand is that it has a well-defined _loop-cut_ which
matches the gluing of a tree-level object [15]. However, in the context of this paper, we will only need the
information about tree-loop type cuts.


                   - 13                   

the residue _Ri,j_ _≡_ Res _Xi,j_ =0 _In_ is given by [15]




  _Ri,j_ =


_k∈L,m∈R_


  +


_k∈L_



�� - _∂AL_
_Xk,m −_ _Xk,jθ_ [ˆ] _k,j−_ 1 _−_ _Xi,m_
_∂Xk,xL_



_∂IR_
_∂XxR,m_




 -  - _∂AL_
+ _Xm,k −_ _Xk,jθ_ [ˆ] _k,j−_ 1 _−_ _Xm,iθ_ [ˆ] _m,i−_ 1
_∂Xk,xL_



_∂IR_
_∂Xm,xR_







(2.13)



�� - _∂AL_
_Xk,p −_ _Xi,p −_ _Xk,jθ_ [ˆ] _k,j−_ 1
_∂Xk,xL_



_∂IR_
_∂XxR,p_








 - _∂AL_
+ _Xi−_ 1 _,i_

_k∈L_ _∂Xk,xL_



_∂IR_
_∂Xi−_ 1 _,i_



_,_
���� _xR→i_



where we are assuming the puncture is on the right of curve _Xi,j_ (see Fig. 2), and have
_θ_ ˆ _i,k_ = 1 _−_ _δi,k_, _L_ = _{i_ + 1 _, i_ + 2 _, . . ., j −_ 1 _}_, and _R_ = _{j, j_ + 1 _, . . ., i −_ 1 _, i}_ .


**2.4** **One-loop** **one-** **and** **two-** **point** **surface** **integrands**


To finish this section, we provide some explicit examples of one-loop surface integrands for

_n_ = 1 and _n_ = 2.

The one-point gluon integrand is simply given by the tadpole diagram. In surface

kinematics, this object has the following form:




_[X]_ [1] _[,]_ [2]

_−_ [(1 + ∆)(] _[X]_ [2] _[,p][ −]_ _[X]_ [1] _[,p]_ [)]
_X_ 1 _,p_ _X_ 1 _,p_



_I_ 1 = [2] _[X]_ [1] _[,]_ [2]



_,_ (2.14)
_X_ 1 _,p_



where ∆= 1 _−_ _d_ encodes the integrand’s dependence on the spacetime dimensionality _d_ .
Note that there is manifest dependence on the boundary curve _X_ 1 _,_ 2; once we set it to zero,
we are left with the standard scaleless tadpole integrand that integrates to zero. In addition,

one can easily check that it satisfies the surface gauge-invariance (2.11).


                   - 14                   

For a slightly more interesting example, at _n_ = 2 we have the following surface integrand



_I_ 2 = _[X]_ [2] _[,p]_ [∆]




[2] _[,p]_ [∆]

_−_ _[X]_ [3] _[,p]_ [∆]
_X_ 1 _,p_ _X_ 1 _,p_




[3] _[,p]_ [∆]

+ _[X]_ [4] _[,p]_ [∆]
_X_ 1 _,p_ _X_ 1 _,p_




[4] _[,p]_ [∆]

_−_ _[X]_ [2] _[,p][X]_ [4] _[,p]_ [∆]
_X_ 1 _,p_ _X_ 1 _,pX_ 3 _,p_




[2] _[,p][X]_ [4] _[,p]_ [∆]

+ _[X]_ [4] _[,p]_ [∆]
_X_ 1 _,pX_ 3 _,p_ _X_ 3 _,p_




[4] _[,p]_ [∆]

+ _[X]_ [3] _[,p][X]_ [1] _[,]_ [2][∆]
_X_ 3 _,p_ _X_ 1 _,pX_ 1 _,_ 1




[3] _[,p][X]_ [1] _[,]_ [2][∆]

_−_ _[X]_ [4] _[,p][X]_ [1] _[,]_ [2][∆]
_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,pX_ 1 _,_ 1




[4] _[,p][X]_ [1] _[,]_ [2][∆]

+ _[X]_ [1] _[,]_ [2] _[X]_ [1] _[,]_ [4][∆]
_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,pX_ 1 _,_ 1



_X_ 1 _,pX_ 1 _,_ 1




[2] _[,p][X]_ [1] _[,]_ [4][∆]

+ _[X]_ [3] _[,p][X]_ [1] _[,]_ [4][∆]
_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,pX_ 1 _,_ 1

[1] _[,p][X]_ [3] _[,]_ [4][∆]

_−_ _[X]_ [2] _[,p][X]_ [3] _[,]_ [4][∆]
_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,pX_ 3 _,_ 3




[2] _[,]_ [4][∆]

_−_ _[X]_ [2] _[,]_ [4][∆]
_X_ 1 _,p_ _X_ 3 _,p_

[1] _[,p]_ [∆]

+ _[X]_ [2] _[,p]_ [∆]
_X_ 3 _,p_ _X_ 3 _,p_




[2] _[,]_ [4][∆]

_−_ _[X]_ [3] _[,p][X]_ [2] _[,]_ [4][∆]
_X_ 3 _,p_ _X_ 1 _,pX_ 1 _,_ 1

[2] _[,p]_ [∆]

_−_ _[X]_ [4] _[,p][X]_ [2] _[,]_ [3][∆]
_X_ 3 _,p_ _X_ 3 _,pX_ 3 _,_ 3




[3] _[,p][X]_ [2] _[,]_ [4][∆]

+ _[X]_ [2] _[,]_ [4][∆]
_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,_ 1




[4] _[,p][X]_ [2] _[,]_ [3][∆]

+ _[X]_ [1] _[,p][X]_ [2] _[,]_ [3][∆]
_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,pX_ 3 _,_ 3




[2] _[,]_ [4][∆]

+ _[X]_ [2] _[,]_ [3] _[X]_ [3] _[,]_ [4][∆]
_X_ 1 _,_ 1 _X_ 3 _,pX_ 3 _,_ 3




[1] _[,p][X]_ [2] _[,]_ [3][∆]

_−_ _[X]_ [1] _[,p][X]_ [2] _[,]_ [4][∆]
_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,pX_ 3 _,_ 3



_X_ 3 _,pX_ 3 _,_ 3




_−_ _[X]_ [2] _[,p][X]_ [1] _[,]_ [4][∆]



+ _[X]_ [1] _[,p][X]_ [3] _[,]_ [4][∆]




[3] _[,p][X]_ [1] _[,]_ [4][∆]

_−_ _[X]_ [2] _[,]_ [4][∆]
_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,p_

[2] _[,p][X]_ [3] _[,]_ [4][∆]

_−_ _[X]_ [1] _[,p]_ [∆]
_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,p_



_X_ 3 _,pX_ 3 _,_ 3



+ _[X]_ [2] _[,]_ [4][∆]




_[X]_ [2] _[,p]_ _−_ _[X]_ [3] _[,p]_

_X_ 1 _,p_ _X_ 1 _,p_




[2] _[,]_ [4][∆]

+ _[X]_ [2] _[,p]_
_X_ 3 _,_ 3 _X_ 1 _,p_




_[X]_ [3] _[,p]_ + _[X]_ [4] _[,p]_

_X_ 1 _,p_ _X_ 1 _,p_




_[X]_ [4] _[,p]_ _−_ _[X]_ [2] _[,p][X]_ [4] _[,p]_

_X_ 1 _,p_ _X_ 1 _,pX_ 3 _,p_




_[X]_ [2] _[,p][X]_ [4] _[,p]_ + _[X]_ [4] _[,p]_

_X_ 1 _,pX_ 3 _,p_ _X_ 3 _,p_




_[X]_ [4] _[,p]_ + _[X]_ [3] _[,p][X]_ [1] _[,]_ [2]

_X_ 3 _,p_ _X_ 1 _,pX_ 1 _,_ 1




_[X]_ [3] _[,p][X]_ [1] _[,]_ [2] _−_ _[X]_ [4] _[,p][X]_ [1] _[,]_ [2]

_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,pX_ 1 _,_ 1




_[X]_ [4] _[,p][X]_ [1] _[,]_ [2] + [3] _[X]_ [1] _[,]_ [2] _[X]_ [1] _[,]_ [4]

_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,pX_ 1 _,_ 1



_X_ 1 _,pX_ 1 _,_ 1




_[X]_ [2] _[,p][X]_ [1] _[,]_ [4] + _[X]_ [3] _[,p][X]_ [1] _[,]_ [4]

_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,pX_ 1 _,_ 1




_[X]_ [1] _[,]_ [1] _[X]_ [2] _[,]_ [3] + _[X]_ [1] _[,]_ [4] _[X]_ [2] _[,]_ [3]

_X_ 1 _,pX_ 3 _,p_ _X_ 1 _,pX_ 3 _,p_




_[X]_ [1] _[,]_ [4] _[X]_ [2] _[,]_ [3] + _[X]_ [1] _[,]_ [1] _[X]_ [2] _[,]_ [4]

_X_ 1 _,pX_ 3 _,p_ _X_ 1 _,pX_ 3 _,p_




_[X]_ [1] _[,]_ [1] _[X]_ [2] _[,]_ [4] _−_ [2] _[X]_ [2] _[,]_ [4]

_X_ 1 _,pX_ 3 _,p_ _X_ 1 _,p_




_[X]_ [2] _[,]_ [4]

_−_ [2] _[X]_ [2] _[,]_ [4]
_X_ 1 _,p_ _X_ 3 _,p_



_X_ 3 _,p_




_−_ _[X]_ [2] _[,p][X]_ [1] _[,]_ [4]




_[X]_ [3] _[,p][X]_ [1] _[,]_ [4] _−_ _[X]_ [1] _[,]_ [1] _[X]_ [2] _[,]_ [3]

_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,pX_ 3 _,p_




_−_ _[X]_ [3] _[,p][X]_ [2] _[,]_ [4]




_[X]_ [3] _[,p][X]_ [2] _[,]_ [4] + _[X]_ [2] _[,]_ [4]

_X_ 1 _,pX_ 1 _,_ 1 _X_ 1 _,_ 1




_[X]_ [2] _[,]_ [4] + _[X]_ [1] _[,]_ [1] _[X]_ [3] _[,]_ [3]

_X_ 1 _,_ 1 _X_ 1 _,pX_ 3 _,p_




_[X]_ [1] _[,]_ [1] _[X]_ [3] _[,]_ [3] _−_ _[X]_ [1] _[,]_ [2] _[X]_ [3] _[,]_ [3]

_X_ 1 _,pX_ 3 _,p_ _X_ 1 _,pX_ 3 _,p_




_[X]_ [1] _[,]_ [2] _[X]_ [3] _[,]_ [3] _−_ _[X]_ [1] _[,]_ [4] _[X]_ [3] _[,]_ [3]

_X_ 1 _,pX_ 3 _,p_ _X_ 1 _,pX_ 3 _,p_




_[X]_ [1] _[,]_ [4] _[X]_ [3] _[,]_ [3] + _[X]_ [2] _[,]_ [4] _[X]_ [3] _[,]_ [3]

_X_ 1 _,pX_ 3 _,p_ _X_ 1 _,pX_ 3 _,p_




_[X]_ [2] _[,]_ [4] _[X]_ [3] _[,]_ [3] _−_ _[X]_ [1] _[,]_ [1] _[X]_ [3] _[,]_ [4]

_X_ 1 _,pX_ 3 _,p_ _X_ 1 _,pX_ 3 _,p_



_X_ 1 _,pX_ 3 _,p_



+ _[X]_ [1] _[,]_ [2] _[X]_ [3] _[,]_ [4]




[3] _[X]_ [2] _[,]_ [3] _[X]_ [3] _[,]_ [4] + _[X]_ [1] _[,p][X]_ [3] _[,]_ [4]

_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,pX_ 3 _,_ 3




_[X]_ [1] _[,]_ [2] _[X]_ [3] _[,]_ [4] + [3] _[X]_ [2] _[,]_ [3] _[X]_ [3] _[,]_ [4]

_X_ 1 _,pX_ 3 _,p_ _X_ 3 _,pX_ 3 _,_ 3




_[X]_ [1] _[,p][X]_ [3] _[,]_ [4] _−_ _[X]_ [2] _[,p][X]_ [3] _[,]_ [4]

_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,pX_ 3 _,_ 3




_[X]_ [2] _[,p][X]_ [3] _[,]_ [4] _−_ _[X]_ [1] _[,p]_

_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,p_




_[X]_ [1] _[,p]_ + _[X]_ [2] _[,p]_

_X_ 3 _,p_ _X_ 3 _,p_




_[X]_ [2] _[,p]_ _−_ _[X]_ [4] _[,p][X]_ [2] _[,]_ [3]

_X_ 3 _,p_ _X_ 3 _,pX_ 3 _,_ 3




_[X]_ [4] _[,p][X]_ [2] _[,]_ [3] + _[X]_ [1] _[,p][X]_ [2] _[,]_ [3]

_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,pX_ 3 _,_ 3



_X_ 3 _,pX_ 3 _,_ 3




_[X]_ [1] _[,p][X]_ [2] _[,]_ [4] + _[X]_ [2] _[,]_ [4]

_X_ 3 _,pX_ 3 _,_ 3 _X_ 3 _,_ 3




_−_ _[X]_ [1] _[,p][X]_ [2] _[,]_ [4]




_−_ 1 _−_ ∆ _,_
_X_ 3 _,_ 3



(2.15)
where, in addition to the boundary curves _Xi,i_ +1 = _Xi,i_ [(1)] +1 [,] [we] [now] [see] [the] [tadpole] [singu-]
larities _X_ 1 _,_ 1 = 0 and _X_ 3 _,_ 3 = 0.


                   - 15                   

### **Part I: Soft Limits at Tree-Level and One-Loop**

We now proceed to the study of the soft expansion of tree-level YM amplitudes and of

the one-loop integrand, both defined via scalar-scaffolding. As we will see, working in the

scalar-scaffolded representation makes it especially easy both to rigorously define the soft

limit and transparently understand how the soft expansion follows from factorization and

gauge invariance.

Before we actually take the soft limit, we must carefully define it. The most naive way
of defining a soft limit in (say) the _n_ [th] particle is simply to take the momentum _qn_ _[µ]_ _[→]_ [0][.]
But this is not precise enough: for instance, if we do this by rescaling _qn_ _[µ]_ _[→]_ _[εq]_ _n_ _[µ]_ [and]
sending _ε_ _→_ 0, momentum is not conserved for any _ε_ = 1. So, instead, we must give a
parametrization of _n_ -point kinematics _qi_ _[µ]_ [(] _[ε]_ [)] _[, ϵ]_ _i_ _[µ]_ [(] _[ε]_ [)][ which starts with the] _[ n]_ [-point kinematics]
at _ε_ = 1 and ends with the ( _n−_ 1)-point kinematics at _ε_ = 0, ensuring that both momentum
conservation [�] _i_ _[q]_ _i_ _[µ]_ [=] [0] [and] [the] [on-shell] [conditions] _[q]_ _i_ [2] [=] [0][,] _[ϵ][i]_ _[·][ q][i]_ [=] [0] [are] [true] [for] [all] _[ε]_ [.]
We will see in this Part I that the scalar-scaffolding picture suggests a simple and natural

way of doing this, by directly deforming the momentum polygon. As we emphasized in our

discussion of kinematics, working with _X_ variables trivializes momentum conservation, and

maintaining the on-shell conditions only forces that the _X_ ’s for boundary and scaffolding

are kept at zero.

As also emphasized in the previous section, the scalar-scaffolded representation of the

gluon amplitude has a completely _locked_ form, free of gauge redundancies while retaining

cyclic invariance; instead, gauge invariance is reflected in the form of the amplitude given

in Eq. (2.3) at tree-level and in Eq. (2.11) at one-loop. This allows us to canonically define

our soft limit as a Laurent expansion in a set of “soft factors.”

We will start at tree-level, reproducing the leading Weinberg soft factor as a conse
quence of factorization (the gluing rule of Eq. (2.5)) together with gauge invariance. We

then use the fact that the amplitude satisfies the gauge-invariance identity (2.4) to deter
mine the subleading term in the expansion as well as put certain constraints (in the form

of sum rules) on all higher order terms. (We describe these derivations in more detail in

App. A.)

We then turn to looking at the soft expansion of the one-loop integrand. As we have

mentioned, ordinary loop integrands for gluons are not in general well-defined, due to the

1 _/_ 0 divergences associated with tadpoles and external bubbles. Even if these are manually

removed in some way, the integrands are no longer gauge invariant and do not factorize

correctly on cuts. Thus, we do not expect any nice behavior in the soft limit for integrands,

only for amplitudes post-loop integration. But, as we reviewed in the previous section,

the one-loop surface integrand offers us hope, as it _does_ satisfy the two properties crucial

to obtaining our results at tree-level: (surface) gauge invariance and factorization. By

generalizing the soft expansion at tree-level to surface kinematics at one-loop, we find

that, at leading order, the surface integrand yields precisely the Weinberg soft term plus a

correction which manifestly vanishes upon integration. This is a remarkable fact: while the


                   - 16                   

Weinberg soft theorem is known to be all-loop-orders exact, it is surface kinematics that

gives us the kinematical structure necessary to promote this statement to loop integrand

level! We also discuss higher-order terms in the one-loop soft expansion in App. B.


**3** **Defining** **the** **Soft** **Limit** **at** **Tree-Level**


As referenced in the preamble, here we will explicitly define a (minimal) soft limit in scalar

variables which we will use to expand the YM amplitude and one-loop integrand. However,

before doing this, let’s first analyze this question in the standard language of polarization
vectors and gluon momenta, where the on-shell conditions ( _qi_ [2] [=] [0] [and] _[ϵ][i][ ·][ q][i]_ [=] [0][)] [are] [not]
made manifest.

To do this, consider the _n_ -point gluon momentum polygon _before_ scaffolding, where

each edge corresponds to the momentum of an external gluon. Label the vertices by dual
coordinates _x_ _[µ]_ _i_ [,] [such] [that] [each] [gluon] [momentum] [is] [given] [by] _[q]_ _i_ _[µ]_ [=] [(] _[x][i]_ [+1] _[−]_ _[x][i]_ [)] _[µ]_ [.] [In] [this]
geometric picture, we can naively take the _n_ [th] gluon soft in infinitely many ways: all
we must do is map this _n_ -point polygon to _any_ ( _n_ _−_ 1)-point polygon, where our only
requirement is that _x_ _[µ]_ 1 [and] _[x][µ]_ _n_ [must] [move] [together] [to] [a] [common] [vertex] _[x][µ]_ _s_ [of] [the] [smaller]
polygon so that _x_ _[µ]_ 1 _[−]_ _[x]_ _n_ _[µ]_ [=] _[ q]_ _n_ _[µ]_ _[→]_ [0][.] [Minimally, however, we can achieve this limit by leaving]
all _x_ _[µ]_ _i_ [for] _[ i][ ̸]_ [= 1] _[, n]_ [ fixed and only moving] _[ x]_ 1 _[µ]_ [and] _[ x]_ _n_ _[µ]_ [together to] _[ x]_ _s_ _[µ]_ [.] [Defined as a deformation]
on the closed momentum polygon, this limit guarantees momentum conservation holds at

all times, but we will still need to enforce the on-shell conditions.
In the simplest incarnation, we have that _x_ _[µ]_ 1 [and] _[x][µ]_ _n_ [follow] [a] [straight] [line] [until] _[x][µ]_ _s_ [,]
giving us:



_,_ (3.1)











_x_ _[µ]_ 1 [(] _[ε]_ [) =] _[ x]_ _s_ _[µ]_ _[−]_ _[ε]_ [ (] _[x][µ]_ _s_ _[−]_ _[x]_ 1 _[µ]_ [)]

_v_ 1 _[µ]_
_x_ _[µ]_ _n_ [(] _[ε]_ [) =] _[ x]_ _s_ _[µ]_ _[−]_ _[ε]_ [ (] _[x][µ]_ _s_ _[−]_ _[x]_ _n_ _[µ]_ [)]



_x_ _[µ]_ 2














_vn_ _[µ]_



_x_ _[µ]_ 1



where _v_ 1 _[µ]_ [and] _[v]_ _n_ _[µ]_ [are] [the] [vectors] [connecting] _[x][µ]_ 1 [and] _[x][µ]_ _n_ [to] _[x][µ]_ _s_ [,] [respectively,] [which] [satisfy]
_vn_ _[µ]_ [=] _[ v]_ 1 _[µ]_ [+] _[ q]_ _n_ _[µ]_ [.] [The] [soft] [limit] [itself] [corresponds] [to] [changing] [the] [parameter] _[ε]_ [smoothly] [from]
1 to 0. Note that, since we are only deforming _x_ _[µ]_ 1 [and] _[x][µ]_ _n_ [,] [we] [only] [affect] [the] [momenta]
of the two gluons adjacent to the soft gluon, _q_ 1 _[µ]_ [and] _[q]_ _n_ _[µ]_ _−_ 1 [.] [This] [means] [that] [our] [minimal]
mapping trivially keeps all gluons 2 through _n −_ 2 on-shell at all times. We therefore only
need to worry about what happens with gluons 1, _n_, and _n −_ 1.
Starting with gluon _n_, under this path the momentum _qn_ _[µ]_ [(] _[ε]_ [)] [is] [simply] [given] [by]


_qn_ _[µ]_ [(] _[ε]_ [) = (] _[x]_ [1] _[−]_ _[x][n]_ [)] _[µ]_ [(] _[ε]_ [) =] _[ ε]_ [(] _[x]_ [1] _[−]_ _[x][n]_ [)] _[µ]_ [=] _[ εq]_ _n_ _[µ][,]_ (3.2)


                   - 17                   

so gluon _n_ remains on-shell during the limit. For gluon 1, we have that


_q_ 1 _[µ]_ [(] _[ε]_ [) = (] _[x]_ [2] _[ −]_ _[x][s]_ [)] _[µ]_ [ +] _[ ε]_ [(] _[x]_ _s_ _[µ]_ _[−]_ _[x]_ 1 _[µ]_ [) =] _[ q]_ 1 _[µ]_ [+ (] _[ε][ −]_ [1)] _[v]_ 1 _[µ][.]_ (3.3)


As such, keeping _q_ 1 [2][(] _[ε]_ [) = 0][ for any] _[ ε]_ [ requires us to constrain] _[ v]_ 1 _[µ]_ [with] _[ v]_ 1 [2] [= 0][ and] _[ v]_ [1] _[ ·][ q]_ [1] [= 0][.]
Further ensuring that _ϵ_ 1 _· q_ 1( _ε_ ) = 0, we also need _v_ 1 _· ϵ_ 1 = 0.
For gluon _n −_ 1, we analogously find


_qn_ _[µ]_ _−_ 1 [(] _[ε]_ [) = (] _[x][s][ −]_ _[x][n][−]_ [1][)] _[µ]_ [ +] _[ ε]_ [(] _[x][n][ −]_ _[x][s]_ [)] _[µ]_ [=] _[ q]_ _n_ _[µ]_ _−_ 1 [+ (1] _[ −]_ _[ε]_ [)] _[v]_ _n_ _[µ][,]_ (3.4)


so asking for _qn_ [2] _−_ 1 [(] _[ε]_ [) = 0] [similarly] [implies] [that] _[v]_ _n_ [2] [= 0] [and] _[v][n]_ _[·][ q][n][−]_ [1] [= 0][.] [Finally,] [imposing]
_ϵn−_ 1 _·_ _qn−_ 1( _ε_ ) = 0 gives the condition that _ϵn−_ 1 _·_ _vn_ = 0. Therefore, in order to keep
everyone on-shell while changing only the momenta of the adjacent gluons, we must impose
the following constraints on _v_ 1 _[µ]_ [and] _[v]_ _n_ _[µ]_ [:]


Gluon 1 : _v_ 1 [2] [= 0] _[,]_ _q_ 1 _· v_ 1 = 0 _,_ _ϵ_ 1 _· v_ 1 = 0 _,_

(3.5)
Gluon _n −_ 1 : _vn_ [2] [= 0] _[,]_ _qn−_ 1 _· vn_ = 0 _,_ _ϵn−_ 1 _· vn_ = 0 _._


Note that these constraints are gauge invariant, as required.
Since, _e.g._, _vn_ _[µ]_ [can] [be] [written] [as] [a] [function] [of] _[v]_ 1 _[µ]_ [through] [the] [equality] _[v]_ _n_ _[µ]_ [=] _[v]_ 1 _[µ]_ [+] _[ q]_ _n_ _[µ]_ [,]
Eq. (3.5) constitutes a total of six constraints on the vector _v_ 1 _[µ]_ [.] [As] [such,] [there] [certainly]
exists a solution for _x_ _[µ]_ _s_ [in] [six] [dimensions] [or] [higher.] [But,] [given] [our] [universe,] [it] [is] [natural]
to ask if there is a way to realize this limit in _d_ = 4. To explore this question, it is best to

work in spinor-helicity variables, where we will represent the momenta of gluons 1, _n_ and
_n −_ 1 as


( _q_ 1) _α,_ ˙ _α_ = _λ_ 1 _,αλ_ [˜] 1 _,_ ˙ _α,_ ( _qn_ ) _α,_ ˙ _α_ = _λn,αλ_ [˜] _n,α_ ˙ _,_ ( _qn−_ 1) _α,_ ˙ _α_ = _λn−_ 1 _,αλ_ [˜] _n−_ 1 _,_ ˙ _α,_ (3.6)


and their polarizations as




_[i,α][µ]_ [˜] _[i,][α]_ [ ˙]

_,_ ( _ϵ_ [+] _i_ [)] _[α,]_ [ ˙] _[α]_ [=] _[µ][i,α][λ]_ [˜] _[i,][α]_ [ ˙]

[ _λ_ [˜] _iµ_ ˜ _i_ ] _⟨λiµi⟩_



( _ϵ_ _[−]_ _i_ [)] _[α,]_ [ ˙] _[α]_ [=] _[λ][i,α][µ]_ [˜] _[i,][α]_ [ ˙]



(3.7)
_⟨λiµi⟩_ _[,]_



with _µi,_ ˜ _µi_ reference spinors. Since _v_ 1 _[µ]_ [and] _[v]_ _n_ _[µ]_ [are] [also] [null] [vectors] [by] [the] [conditions] [in]
Eq. (3.5), we can similarly write them as spinors:


( _v_ 1) _α,_ ˙ _α_ = _λ_ _[v]_ _α_ [1] _[λ]_ [˜] _[v]_ _α_ ˙ [1] _[,]_ ( _vn_ ) _α,_ ˙ _α_ = _λ_ _[v]_ _α_ _[n][λ]_ [˜] _[v]_ _α_ ˙ _[n][.]_ (3.8)


Then, the condition _vn_ _[µ]_ [=] _[v]_ 1 _[µ]_ [+] _[ q]_ _n_ _[µ]_ [nicely] [turns] [into] [the] [standard] [three-point] [kinematics]
constraint, which means that we have either


_λ_ _[v]_ [1] _∝_ _λ_ _[v][n]_ _∝_ _λn,_ or _λ_ ˜ _[v]_ 1 _∝_ _λ_ ˜ _[v][n]_ _∝_ _λ_ ˜ _n._ (3.9)


Let’s now consider the situation where both gluons 1 and _n −_ 1 have positive helicity, and


                   - 18                   

choose the _λ_ ’s to be parallel. Then, we can satisfy the conditions in Eq. (3.5) by picking


_v_ 1 _∝_ _λnλ_ [˜] 1 _,_ _vn_ _∝_ _λnλ_ [˜] _n−_ 1 _._ (3.10)


However, if we had instead chosen the _λ_ [˜] ’s to be parallel, it is easy to conclude that there is

no solution: we would need to pick the forbidden values of the reference spinors to satisfy

all the conditions.
In contrast, if we take gluons 1 and _n −_ 1 to both have negative helicity, then we find
there is _no_ solution if we choose the _λ_ ’s to be parallel, but there is a solution for _λ_ [˜] ’s parallel

given by
_v_ 1 _∝_ _λ_ 1 _λ_ [˜] _n,_ _vn_ _∝_ _λn−_ 1 _λ_ [˜] _n._ (3.11)


Finally, there is unsurprisingly no solution when the helicities of gluons 1 and _n −_ 1 are

opposite. Therefore, we conclude that the soft limit as defined above is realizable in _d_ = 4
as long as gluons 1 and _n −_ 1 have the _same_ helicity.

So, having carefully defined our limit in the standard gluon-amplitude language, let us
understand how this particular limit translates into the scalar variables _Xi,j_ introduced in
the previous section. For now, we’ll do this for the case at tree-level, and we will explain

how it generalizes to the one-loop surface integrand in Sec. 5.1. We start by placing the
gluon momentum polygon inside the 2 _n_ -point scalar polygon, where we map _x_ _[µ]_ _i_ _[→]_ _[x]_ 2 _[µ]_ _i−_ 1 [.]
Since, by definition, we are only moving _x_ _[µ]_ 1 [and] _[x][µ]_ 2 _n−_ 1 [during] [the] [soft] [limit,] [the] [only]
chords that change are _X_ 1 _,j_ and _Xj,_ 2 _n−_ 1. They evolve as


_X_ 1 _,j_ ( _ε_ ) = [ _xj_ _−_ _x_ 1( _ε_ )] [2] = [( _xj_ _−_ _xs_ ) + _ε_ ( _xs −_ _x_ 1)] [2] = _Xs,j_ + _ε_ ( _X_ 1 _,j_ _−_ _Xj,s_ ) _,_

_Xj,_ 2 _n−_ 1( _ε_ ) = [ _xj_ _−_ _x_ 2 _n−_ 1( _ε_ )] [2] = [( _xj_ _−_ _xs_ ) + _ε_ ( _xs −_ _x_ 2 _n−_ 1)] [2] = _Xs,j_ + _ε_ ( _Xj,_ 2 _n−_ 1 _−_ _Xj,s_ ) _,_
(3.12)
where _Xs,j_ are the chords on the final polygon we obtain after colliding points _x_ _[µ]_ 1 [and] _[ x]_ 2 _[µ]_ _n−_ 1
together to _x_ _[µ]_ _s_ [.] [To] [ensure] [the] [gluons] [remain] [on-shell] [throughout] [the] [soft] [limit] [we] [must]
have: _X_ 1 _,_ 3( _ε_ ) = _X_ 2 _n−_ 1 _,_ 2 _n−_ 3( _ε_ ) = 0 and _X_ 1 _,_ 2( _ε_ ) = _X_ 2 _n−_ 1 _,_ 2 _n−_ 2( _ε_ ) = 0. This constrains _xs_ to
be null separated from (1 _,_ 2 _,_ 3) as well as (2 _n −_ 3 _,_ 2 _n −_ 2 _,_ 2 _n −_ 1), which is exactly what we

found in (3.5). In scalar variables, we see from the above that the objects controlling the

perturbative soft expansion are


_δj_ [(1)] = _ε_ ( _X_ 1 _,j_ _−_ _Xs,j_ ) _,_ _δj_ [(2] _[n][−]_ [1)] = _ε_ ( _Xj,_ 2 _n−_ 1 _−_ _Xs,j_ ) _,_ (3.13)


which we will refer to as our “soft factors.” Note that the _δj_ [(1)] are non-vanishing only for

_j_ = 4 _,_ 5 _, . . .,_ 2 _n −_ 2 and the _δj_ [(2] _[n][−]_ [1)] for _j_ = 2 _,_ 3 _, . . .,_ 2 _n −_ 4. Therefore, we _define_ the soft

expansion of the scalar-scaffolded YM amplitude _An_ as a Laurent expansion in _δj_ [(1)] _[, δ]_ _j_ [(2] _[n][−]_ [1)] .
We stress that, given that the _X_ ’s provide a basis for the full gluon kinematic space,

it is not necessary to refer directly to the momentum polygon picture to define soft lim
its. _Any_ motion in _X_ space that leaves the scaffolding _X_ ’s untouched (at zero) and where
_X_ 1 _,j, X_ 2 _n−_ 1 _,j_ are identified (at the end) _defines_ a consistent soft limit. Of course, as discussed above, in any fixed spacetime dimension the _X_ ’s are _not_ in general all independent,


                   - 19                   

and therefore soft maps in _X_ space might not be reachable given the dimension constraints.
We can also understand that any soft map in _X_ space which does not touch _X_ 2 _,k_ and
_X_ 2 _n−_ 2 _,k_ also leaves the polarizations of the adjacent gluons unchanged, since we are free to
pick _ϵ_ _[µ]_ 1 [=] _[ p]_ 2 _[µ]_ [= (] _[x]_ [3] _[ −]_ _[x]_ [2][)] _[µ]_ [and] _[ϵ][µ]_ _n−_ 1 [=] _[ p]_ 2 _[µ]_ _n−_ 3 [= (] _[x]_ [2] _[n][−]_ [2] _[ −]_ _[x]_ [2] _[n][−]_ [3][)] _[µ]_ [.]
In some important cases, these soft factors are not actually differences in _X_ variables
but rather equivalent to a single _X_ . In particular, since _Xs,_ 2 _n−_ 3 = _Xs,_ 3 = 0 and _Xs,_ 2 =
_Xs,_ 2 _n−_ 2 = 0, we have during the soft limit that



_X_ 2 _,_ 2 _n−_ 1( _ε_ ) = _δ_ 2 [(2] _[n][−]_ [1)] _,_

_X_ 3 _,_ 2 _n−_ 1( _ε_ ) = _δ_ 3 [(2] _[n][−]_ [1)] _,_



_X_ 1 _,_ 2 _n−_ 2( _ε_ ) = _δ_ 2 [(1)] _n−_ 2 _[,]_

(3.14)
_X_ 1 _,_ 2 _n−_ 3( _ε_ ) = _δ_ 2 [(1)] _n−_ 3 _[.]_



The tree-level YM amplitude has poles when _X_ 1 _,_ 2 _n−_ 3 _, X_ 3 _,_ 2 _n−_ 1 _→_ 0, which correspond to
gluon _n_ becoming collinear with the neighboring gluons 1 and _n −_ 1, respectively. This

means - just as with the famous leading Weinberg pole - the leading order term in the

soft expansion will localize on these two factorization channels.


**3.1** **Setting** **up** **the** **soft** **expansion**



Having defined the soft limit in scalar-scaffolded variables, let’s now look a bit closer at the
structure of the amplitude _An_ . As we just explained, the only two soft factors which appear
as poles in _An_ are _δ_ 3 [(2] _[n][−]_ [1)] = _X_ 3 _,_ 2 _n−_ 1( _ε_ ) and _δ_ 2 [(1)] _n−_ 3 [=] _[ X]_ [1] _[,]_ [2] _[n][−]_ [3][(] _[ε]_ [)][.] [Therefore,] [to] [perform] [the]
soft expansion, we will start by explicitly writing out the dependence on these two poles as

follows:
_An_ = _[R]_ [1] _[,]_ [2] _[n][−]_ [3] + _[R]_ [3] _[,]_ [2] _[n][−]_ [1] + _R,_ (3.15)




_[R]_ [1] _[,]_ [2] _[n][−]_ [3] + _[R]_ [3] _[,]_ [2] _[n][−]_ [1]

_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1



+ _R,_ (3.15)
_X_ 3 _,_ 2 _n−_ 1



where _R_ 1 _,_ 2 _n−_ 3 and _R_ 3 _,_ 2 _n−_ 1 are the residues of _An_ at _X_ 1 _,_ 2 _n−_ 3 = 0 and _X_ 3 _,_ 2 _n−_ 1 = 0, respectively, and _R_ is everything else, which does _not_ have poles in either _X_ 1 _,_ 2 _n−_ 3 or _X_ 3 _,_ 2 _n−_ 1.
Note that, even though _R_ 1 _,_ 2 _n−_ 3 and _R_ 3 _,_ 2 _n−_ 1 are only gauge invariant on the support of
_X_ 1 _,_ 2 _n−_ 3 = 0 and _X_ 3 _,_ 2 _n−_ 1 = 0, respectively, since the amplitude has a locked form, decomposing it in this way is completely canonical.
In the next subsection, we use the explicit form of the residues, _R_ 1 _,_ 2 _n−_ 3 and _R_ 3 _,_ 2 _n−_ 1, as
given in Eq. (2.5), to obtain the leading Weinberg soft theorem, which is of order _O_ ( _δ_ _[−]_ [1] ).

But let us start with some remarks on how higher order terms in the soft expansion can also

be derived (in the case of the subleading) and constrained (in the case of sub-subleading and

higher) by using gauge invariance in gluon _n_ . We will leave most of the technical aspects of

this discussion for App. A, but we show here the main result which constrains higher order

terms in the soft expansion.
Starting at _O_ ( _δ_ [0] ), _R_ plays a role in the soft expansion of _An_ . And, unlike for the
residues _R_ 1 _,_ 2 _n−_ 3 and _R_ 3 _,_ 2 _n−_ 1, which are known to all soft orders (and written out in App. A),
we seem to have no formula to control its soft expansion. However, knowing that _An_ must


                   - 20                   

be gauge invariant in the _n_ [th] gluon means we must be able to write _An_ as

 - _j_ [(] _[X][j,]_ [2] _[n]_ _[−]_ _[X]_ [1] _[,j]_ [)] _[∂][X]_ _j,_ 2 _n_ _[R]_ [1] _[,]_ [2] _[n][−]_ [3] - _j_ [(] _[X][j,]_ [2] _[n]_ _[−]_ _[X]_ [1] _[,j]_ [)] _[∂][X]_ _j,_ 2 _n_ _[R]_ [3] _[,]_ [2] _[n][−]_ [1] 


( _Xj,_ 2 _n −_ _X_ 1 _,j_ ) _Cj,_

_j_



+
_X_ 1 _,_ 2 _n−_ 3




- _j_ [(] _[X][j,]_ [2] _[n]_ _[−]_ _[X]_ [1] _[,j]_ [)] _[∂][X]_ _j,_ 2 _n_ _[R]_ [3] _[,]_ [2] _[n][−]_ [1]



_j,_ 2 _n_        
+
_X_ 3 _,_ 2 _n−_ 1



(3.16)
where _j_ = 2 _,_ 3 _, . . .,_ 2 _n −_ 2 (here and everywhere else in this subsection) and the _Cj_ are
defined by



_X_ 3 _,_ 2 _n−_ 1



_∂_
_Cj_ =
_∂Xj,_ 2 _n_




_An −_ _[R]_ [1] _[,]_ [2] _[n][−]_ [3]




_[R]_ [1] _[,]_ [2] _[n][−]_ [3] _−_ _[R]_ [3] _[,]_ [2] _[n][−]_ [1]

_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1




_,_ (3.17)



where we use the fact that gauge invariance in _n_ implies linearity in all _Xj,_ 2 _n_ .
Now, since _R_ 3 _,_ 2 _n−_ 1 is gauge invariant in the _n_ [th] gluon (on the locus of _X_ 3 _,_ 2 _n−_ 1 = 0),
we can write _R_ 3 _,_ 2 _n−_ 1 as [�] _j_ [(] _[X][j,]_ [2] _[n][ −]_ _[X]_ [1] _[,j]_ [)] _[∂][X]_ _j,_ 2 _n_ _[R]_ [3] _[,]_ [2] _[n][−]_ [1][.] [So,] [the] [term] [in] [the] [numerator] [of]
_X_ 3 _,_ 2 _n−_ 1 in Eq. (3.16) is precisely _R_ 3 _,_ 2 _n−_ 1. Similarly, we can write _R_ 1 _,_ 2 _n−_ 3, on the locus of
_X_ 1 _,_ 2 _n−_ 3 = 0, as [�] _j_ [(] _[X][j,]_ [2] _[n][ −]_ _[X]_ [1] _[,j]_ [)] _[∂][X]_ _j,_ 2 _n_ _[R]_ [1] _[,]_ [2] _[n][−]_ [3][.] [However, in this case we have to correct for]
the fact that the term in the numerator of _X_ 1 _,_ 2 _n−_ 3 in Eq. (3.16) does _not_ have _X_ 1 _,_ 2 _n−_ 3 = 0.
Therefore, the numerator of _X_ 1 _,_ 2 _n−_ 3 comes out to _R_ 1 _,_ 2 _n−_ 3 _−_ _X_ 1 _,_ 2 _n−_ 3 _∂X_ 2 _n−_ 3 _,_ 2 _nR_ 1 _,_ 2 _n−_ 3. Our
amplitude then takes the form




_[R]_ [1] _[,]_ [2] _[n][−]_ [3] + _[R]_ [3] _[,]_ [2] _[n][−]_ [1]

_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1



( _Xj,_ 2 _n −_ _X_ 1 _,j_ ) _Cj_ _−_ _[∂R]_ [1] _[,]_ [2] _[n][−]_ [3]

_∂X_ 2 _n−_ 3 _,_ 2

_j_



_An_ = _[R]_ [1] _[,]_ [2] _[n][−]_ [3]




[3] _[,]_ [2] _[n][−]_ [1]    
+
_X_ 3 _,_ 2 _n−_ 1



_._ (3.18)
_∂X_ 2 _n−_ 3 _,_ 2 _n_



But, recall that gauge invariance and linearity in the polarization of the _n_ [th] gluon means

that we can also write the amplitude in the form of the first line in Eq. (2.3). Using the

exact same line of reasoning as above, this gives that



_An_ = _[R]_ [1] _[,]_ [2] _[n][−]_ [3]




[3] _[,]_ [2] _[n][−]_ [1]    
+
_X_ 3 _,_ 2 _n−_ 1




_[R]_ [1] _[,]_ [2] _[n][−]_ [3] + _[R]_ [3] _[,]_ [2] _[n][−]_ [1]

_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1



( _Xj,_ 2 _n −_ _Xj,_ 2 _n−_ 1) _Cj_ _−_ _[∂R]_ [3] _[,]_ [2] _[n][−]_ [1]

_∂X_ 3 _,_ 2 _n_

_j_



_._ (3.19)
_∂X_ 3 _,_ 2 _n_



Therefore, if we _subtract_ Eq. (3.18) and Eq. (3.19), we obtain



( _Xj,_ 2 _n−_ 1 _−_ _X_ 1 _,j_ ) _Cj_ = _−_ _[∂R]_ [3] _[,]_ [2] _[n][−]_ [1]

_∂X_ 3 _,_ 2 _n_

_j_








[3] _[,]_ [2] _[n][−]_ [1]

+ _[∂R]_ [1] _[,]_ [2] _[n][−]_ [3]
_∂X_ 3 _,_ 2 _n_ _∂X_ 2 _n−_ 3 _,_ 2



_._ (3.20)
_∂X_ 2 _n−_ 3 _,_ 2 _n_



Note that, so far, this equation is exact; however, if we apply the soft limit to Eq. (3.20),
we can replace ( _Xj,_ 2 _n−_ 1 _−_ _X_ 1 _,j_ ) = ( _δj_ [(2] _[n][−]_ [1)] _−_ _δj_ [(1)][)][,] [and] [then] [we] [find]




  _δj_ [(2] _[n][−]_ [1)] _Cj_ _−_
_j_ _j_




[3] _[,]_ [2] _[n][−]_ [1]

+ _[∂R]_ [1] _[,]_ [2] _[n][−]_ [3]
_∂X_ 3 _,_ 2 _n_ _∂X_ 2 _n−_ 3 _,_ 2







_δj_ [(1)] _[C][j]_ [=] _[ −]_ _[∂R]_ [3] _[,]_ [2] _[n][−]_ [1]

_∂X_ 3 _,_ 2 _n_

_j_



_._ (3.21)
_∂X_ 2 _n−_ 3 _,_ 2 _n_



Taylor-expanding the _Cj_ in soft factors gives us




  _Cj_ = _Cj_ [(0)] +

_k_




- _δk_ [(1)] _[C][j,][{]_ [(] _[k]_ [;1)] _[}]_ [ +] _[ δ]_ _k_ [(2] _[n][−]_ [1)] _Cj,{_ ( _k_ ;2 _n−_ 1) _}_ + _· · ·_ _,_ (3.22)



where _Cj,{_ ( _k_ 1 _,...,km_ ;1) _,_ ( _l_ 1 _,...,lr_ ;2 _n−_ 1) _}_ = ( _∂X_ 1 _,k_ 1 _· · · ∂X_ 1 _,km_ )( _∂Xl_ 1 _,_ 2 _n−_ 1 _· · · ∂Xlr,_ 2 _n−_ 1) _Cj_ . Plugging


                   - 21                   

this into Eq. (3.21), we see that the leading _Cj_ [(0)] are fully determined by matching to the
soft expansion of the _r.h.s._ . As such, it is possible - using just factorization and gauge
invariance - to derive the subleading term in the soft expansion of _An_ .
However, clearly such a strategy will not work for higher order terms in the expansion.

Indeed, already at the next order, on the _l.h.s._ we find:






_j,k_




- _δj_ [(2] _[n][−]_ [1)] _δk_ [(2] _[n][−]_ [1)] _Cj,{_ ( _k_ ;2 _n−_ 1) _} −_ _δj_ [(1)] _[δ]_ _k_ [(1)] _[C][j,][{]_ [(] _[k]_ [;1)] _[}]_ [ +] _[ δ]_ _j_ [(1)] _[δ]_ _k_ [(2] _[n][−]_ [1)] ( _Ck,{_ ( _j_ ;1) _} −_ _Ck,{_ ( _j_ ;2 _n−_ 1) _}_ ) _._



(3.23)

Matching with _r.h.s._, we are thus only able to determine the totally symmetric part of
the tensors _Cj,{_ ( _k_ ;2 _n−_ 1) _}_ and _Cj,{_ ( _k_ ;1) _}_, as well as the full linear combination ( _−Ck,{_ ( _j_ ;1) _} −_
_Cj,{_ ( _k_ ;2 _n−_ 1) _}_ ). Now, clearly this doesn’t entirely fix these matrices: in particular, if we shift
them as _Ck,{_ ( _j_ ;1) _}_ _→_ _Ck,{_ ( _j_ ;1) _}_ + _Ak,j_ and _Cj,{_ ( _k_ ;2 _n−_ 1) _}_ _→_ _Cj,{_ ( _k_ ;2 _n−_ 1) _}_ + _Ak,j_ with _Ak,j_ skewsymmetric, then _Ak,j_ just drops out from Eq. (3.21). We therefore see that - using just
gauge invariance in the _n_ [th] gluon — we can only determine the soft expansion up to _O_ ( _δ_ [0] ),
corresponding to the leading and first subleading terms. [5] However, despite this restriction,
we should pause to appreciate the remarkable fact that we can say _anything_ about the _Cj_ .
Since gauge invariance gave us the constraint (3.20), such a statement would be _impossible_

to make if we were dealing with, say, scalars and not gluons. So, it is clear that gauge

invariance plays a critical role in the structure and universality of the soft expansion.


**4** **The** **Leading** **Soft** **Theorem** **at** **Tree-Level**


Let us now derive the leading order term in the soft expansion of _An_ . Starting with _R_ 1 _,_ 2 _n−_ 3,
we use Eq. (2.5) to write




  
( _Xj,J_ _−_ _X_ 1 _,j_ _−_ _X_ 2 _n−_ 3 _,J_ ) _[∂M][L]_

_∂Xj,x_

_j∈L,_ _J∈{_ 2 _n−_ 2 _,_ 2 _n−_ 1 _,_ 2 _n}_




   _R_ 1 _,_ 2 _n−_ 3 =




_[∂M][L]_ _×_ _[∂M][R]_

_∂Xj,xL_ _∂XJ,x_



_,_ (4.1)
_∂XJ,xR_



where _L_ = _{_ 2 _,_ 3 _, . . .,_ 2 _n−_ 4 _}_, _ML_ = _An−_ 1(1 _,_ 2 _, . . .,_ 2 _n−_ 4 _,_ 2 _n−_ 3 _, xL_ ) and _MR_ = _A_ 3(1 _, xR,_ 2 _n−_
3 _,_ 2 _n −_ 2 _,_ 2 _n −_ 1 _,_ 2 _n_ ), which is simply a three-point gluon amplitude. We can therefore use
the explicit form of _MR_ given in Eq. (2.6) to write out the derivatives _∂XJ,xR_ _MR_ appearing
in Eq. (4.1). We’ll do exactly this in detail in App. A; for now, since we only care about

the leading order contribution, we can note that the only derivative that contributes is for
_J_ = 2 _n −_ 2, _∂X_ 2 _n−_ 2 _,xR_ _MR_ = _X_ 2 _n−_ 3 _,_ 2 _n_ . So, we find



_R_ 1 _,_ 2 _n−_ 3 = _X_ 2 _n−_ 3 _,_ 2 _n ×_



2 _n−_ 4

- _∂ML_

( _Xj,_ 2 _n−_ 2 _−_ _Xs,j_ )
_∂Xj,_ 2 _n−_ 2
_j_ =2


_ML_ (1 _,_ 2 _,...,_ 2 _n−_ 2)



+ _O_ ( _δ_ ) _,_ (4.2)



5Such a result is unsurprising given recent work in Ref. [41] demonstrating the non-existence of universal
soft terms past sub-leading order.


                   - 22                   

where we have replaced _xL_ _→_ 2 _n −_ 2. Now, using the gauge-invariance statement in gluon
_n −_ 1, we can recognize the sum above to be exactly the amplitude _ML_ . Further noting
that, at leading order in _δj_ [(1)][,] _[M][L]_ [(1] _[,]_ [ 2] _[, . . .,]_ [ 2] _[n][ −]_ [2)] _[ →A][n][−]_ [1][(] _[s,]_ [ 2] _[,]_ [ 3] _[, . . .,]_ [ 2] _[n][ −]_ [2)] _[ ≡A][n][−]_ [1][,] [we]
find
_R_ 1 _,_ 2 _n−_ 3 = _X_ 2 _n−_ 3 _,_ 2 _n × An−_ 1 + _O_ ( _δ_ ) _._ (4.3)


In other words, at leading order, the spin sum coming from a cut on an intermediate gluon

precisely turns into the gauge-invariance statement, which allows us to recover just the

lower-point amplitude!
Repeating this analysis for _R_ 3 _,_ 2 _n−_ 1, where now the two lower-point amplitudes are
_ML_ = _A_ 3(1 _,_ 2 _,_ 3 _, xL,_ 2 _n −_ 1 _,_ 2 _n_ ) and _MR_ = _An−_ 1(2 _n −_ 1 _, xR,_ 3 _,_ 4 _, . . .,_ 2 _n −_ 2), the residue
formula tell us that




 
( _Xj,J_ _−_ _Xj,_ 2 _n−_ 1 _−_ _X_ 3 _,J_ ) _[∂M][L]_

_∂XJ,x_

_j∈R,_ _J∈{_ 2 _,_ 1 _,_ 2 _n}_




   _R_ 3 _,_ 2 _n−_ 1 =




_[∂M][L]_ _×_ _[∂M][R]_

_∂XJ,xL_ _∂Xj,x_



_,_ (4.4)
_∂Xj,xR_



with _R_ = _{_ 4 _,_ 5 _, . . .,_ 2 _n −_ 2 _}_ . Using again the explicit form of the three-point amplitude
_ML_, the only term that contributes at _O_ ( _δ_ [0] ) in the _J_ -sum (see App. A for details) comes
from _J_ = 2. We find



( _X_ 2 _,j_ _−_ _Xj,_ 2 _n−_ 1) _[∂M][R]_

_∂Xj,_

_j_




   _R_ 3 _,_ 2 _n−_ 1 = _X_ 3 _,_ 2 _n ×_



+ _O_ ( _δ_ ) _,_
(4.5)
_∂Xj,_ 2



where we have relabeled _xR_ = 2. Now, just as for the previous residue, the sum over _j_
above is precisely equal to _MR_ due to gauge invariance in gluon 2. Further expanding
_MR_ (2 _n −_ 1 _,_ 2 _,_ 3 _, . . .,_ 2 _n −_ 2) in powers of _δj_ [(2] _[n][−]_ [1)] = _Xj,_ 2 _n−_ 1 _−_ _Xj,s_ gives us


_R_ 3 _,_ 2 _n−_ 1 = _X_ 3 _,_ 2 _n × An−_ 1 + _O_ ( _δ_ ) _,_ (4.6)


where, unsurprisingly, we see the appearance of precisely the same ( _n −_ 1)-point amplitude

as in Eq. (4.3).

Therefore, at leading order in soft expansion we find




  - _X_ 2 _n−_ 3 _,_ 2 _n_ _X_ 3 _,_ 2 _n_
_An_ _→_ +
_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1




_An−_ 1( _s,_ 2 _,_ 3 _,_ 4 _, · · ·_ _,_ 2 _n −_ 2) + _O_ ( _δ_ [0] ) _._ (4.7)



As we emphasized earlier, when written in terms of the scalar _Xi,j_ variables, the gluon
amplitude has a completely unique form. Thus, the soft expansion is well-defined. However,

the leading order term (as well as the subleading term discussed in App. A) given above is
_not_ completely gauge invariant: while trivially gauge invariant in gluons 1 through _n −_ 1
(due to _An−_ 1), we’ll show in the next section that it is only gauge invariant in the _n_ [th]

gluon up to a subleading correction. This is not a problem: we will describe a simple

operation which allows us to “gauge-invariantify” the leading soft term. This reflects a

general fact of our soft expansion in scalar-scaffolded variables, that follows from the more

general statement about the Laurent expansion of the amplitude we have already alluded to,


                   - 23                   

independent of soft limits. While the terms in the soft expansion are canonical, the terms

are not individually gauge-invariant. Instead gauge invariance relates different terms in the

Laurent expansion to each other, allowing us ‘ “gauge-invariantify", determining parts of

the higher order terms in the expansion in terms of the lower-order ones.


**4.1** **Gauge-invariantifying** **the** **soft** **expansion**



Looking back to the Weinberg soft pole [17], we can easily translate it into the _X_ ’s and

compare with what we’ve derived in the previous section:

      - _ϵn · q_ 1      -      - _X_ 3 _,_ 2 _n_      
= 2 + _[X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n]_ _−_ 1 _._ (4.8)

_q_ 1 _· q_ _[−]_ _[ϵ]_ _q_ _[n]_ _n_ _[ ·]_ _·_ _[ q]_ _q_ _[n]_ _X_ 3 _,_ 2 _n−_ 1 _X_ 1 _,_ 2 _n−_ 3



_qn · q_




- - _X_ 3 _,_ 2 _n_
= 2 + _[X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n]_
_X_ 3 _,_ 2 _n−_ 1 _X_ 1 _,_ 2 _n−_ 3




    
[2] _[n][−]_ [3] _[,]_ [2] _[n]_

_−_ 1 _._ (4.8)
_X_ 1 _,_ 2 _n−_ 3



Up to a multiplicative factor, this agrees with what we found at _O_ ( _δ_ _[−]_ [1] ), but curiously

it also includes a term subleading in the soft limit. This reflects a nice fact about the

Weinberg soft term: it is _exactly_ gauge invariant in the soft gluon, even away from the
soft limit. In _X_ language, while the terms with poles are gauge invariant up to _O_ ( _δ_ _[−]_ [1] ),
they are not fully gauge invariant in gluon _n_ simply because the variation of _e.g._ _X_ 3 _,_ 2 _n_
is proportional to _X_ 3 _,_ 2 _n−_ 1. But beautifully, the extra _−_ 1 term makes the expression fully
gauge-invariant in 2 _n_ .
So, a simple question is whether there is any operation we can do to each order _O_ ( _δ_ _[k]_ )
in our expansion to make it gauge invariant in the _n_ [th] polarization on its own. To pursue

this, let us the define an operator


      _G_ ( _e,o_ ) [ _F_ ] = ( _Xj,e −_ _Xj,o_ ) _∂Xj,eF_ _−_ _F,_ (4.9)

_j_


where _j_ ranges over all indices other than _e_ and _o_, for _e_ an even index and _o_ an odd index.

The function _F_ is gauge invariant in index _e_ if and only if it satisfies


_G_ ( _e,e_ +1) [ _F_ ] = 0 _,_ and _G_ ( _e,e−_ 1) [ _F_ ] = 0 _._ (4.10)


Furthermore, if we have a function _F_ that, while _not_ gauge invariant in index _e_, satisfies
_G_ ( _e,e_ +1) [ _F_ ] = _G_ ( _e,e−_ 1) [ _F_ ] = 0, then we can gauge-invariantify it by considering a new
function
_F_ _[G][e]_ = _F_ + _G_ ( _e,e_ +1) [ _F_ ] _._ (4.11)


One can check that _F_ _[G][e]_ is, by construction, gauge invariant in _e_ . Of course, by performing
this operation, we generically interfere with gauge invariance in some other indices _e_ _[′]_ . Let’s

now turn back to the leading term we obtained in our soft expansion, and ask whether we

can gauge-invariantify it. It is simple to show that


_G_ 2 _n,_ 1       - _S_ _[−]_ [1][�] = _−An−_ 1 _,_ and _G_ 2 _n,_ 2 _n−_ 1       - _S_ _[−]_ [1][�] = _−An−_ 1 _,_ (4.12)


                   - 24                   

so, upon gauge-invariantifying, we find


            - _X_ 2 _n−_ 3 _,_ 2 _n_ _X_ 3 _,_ 2 _n_             _S_ _[−]_ [1] _[,][G]_ [2] _[n]_ = _S_ _[−]_ [1] _−An−_ 1 = + _−_ 1 _× An−_ 1 _._ (4.13)
_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1


This leading soft factor - now gauge invariant in _all_ gluons - agrees precisely with the

standard Weinberg soft factor!

In App. A, we explain how higher terms in the soft expansion also satisfy the condition
_G_ ( _e,e_ +1) [ _F_ ] = _G_ ( _e,e−_ 1) [ _F_ ] _̸_ = 0, and thus can be gauge-invariantified using exactly this simple
procedure.


**5** **The** **One-Loop** **Leading** **Soft** **Theorem** **for** **the** **Surface** **Integrand**


We now proceed to discussing how to extend the soft expansion at tree-level to the one-loop

surface integrand. We start in Sec. 5.1 by generalizing the tree-level soft limit to surface

kinematics at one-loop. Then, in Sec. 5.2, we use the gauge invariance statement (2.11) as

well as the factorization rule (2.13) to show that, at leading order in the soft expansion, the

surface integrand obeys its own leading soft term, a simple generalization of that found at

tree-level.


**5.1** **Defining** **the** **soft** **expansion** **in** **surface** **kinematics**


In the tree-level case, we started by deriving the soft limit in momentum space, and then
we translated it into the scalar variables _Xi,j_ . In the end, we obtained a map defined purely
on the curves of the disk, corresponding to the choice where we make points _x_ _[µ]_ 1 [and] _[x][µ]_ 2 _n−_ 1
collide into a final point _x_ _[µ]_ _s_ [as] [in] [Eq.] [(][5.1][).] [Thought] [of] [as] [a] [map] [directly] [on] [the] [curves]
living on the surface, it is then trivial to extend this map to the punctured disk:



_X_ 1 _,j_ ( _ε_ ) = _Xs,j_ + _ε_ ( _X_ 1 _,j_ _−_ _Xs,j_ ) _,_


_Xj,_ 1( _ε_ ) = _Xj,s_ + _ε_ ( _Xj,_ 1 _−_ _Xj,s_ ) _,_



_X_ 2 _n−_ 1 _,k_ ( _ε_ ) = _Xs,k_ + _ε_ ( _X_ 2 _n−_ 1 _,k −_ _Xs,k_ ) _,_

(5.1)
_Xk,_ 2 _n−_ 1( _ε_ ) = _Xk,s_ + _ε_ ( _Xk,_ 2 _n−_ 1 _−_ _Xk,s_ ) _,_



for _j, k_ _∈{_ 2 _,_ 3 _, . . .,_ 2 _n −_ 2 _, p,_ 2 _n}_, where we impose that the scaffolding chords _X_ 1 _,_ 3 and
_X_ 2 _n−_ 3 _,_ 2 _n−_ 1 remain zero at all times by setting _Xs,_ 3 = _X_ 2 _n−_ 3 _,s_ = 0. For curves that touch
only points 1 and 2 _n −_ 1, we additionally find


_X_ 1 _,_ 1( _ε_ ) = _Xs,s_ + _ε_ ( _X_ 1 _,_ 1 _−_ _Xs,s_ ) _,_ _X_ 2 _n−_ 1 _,_ 2 _n−_ 1( _ε_ ) = _Xs,s_ + _ε_ ( _X_ 2 _n−_ 1 _,_ 2 _n−_ 1 _−_ _Xs,s_ ) _,_

(5.2)
_X_ 1 _,_ 2 _n−_ 1( _ε_ ) = _Xs,s_ + _ε_ ( _X_ 1 _,_ 2 _n−_ 1 _−_ _Xs,s_ ) _._


In the above, we have made manifest the difference between curves _Xi,j_ and _Xj,i_, since, in
surface kinematics, these variables are not identified.

However, there is now a slight subtlety at one-loop, as it turns out that surface kinemat
ics forces an inconsistent mapping of certain curves (boundary curves) from the 2 _n_ -point
punctured disk onto the (2 _n −_ 1)-point one. We illustrate this in Fig. 4. In particular,
consider curve _X_ 1 _,_ 2, which is associated with the self-intersecting curve shown on the left
of Fig. 4. In the soft limit, this curve gets mapped into the self-intersecting boundary curve


                   - 25                   

**Figure** **4** : (Top) The self-intersecting boundary curve, _X_ 1 _,_ 2, under the soft limit is mapped
into the boundary self-intersecting boundary curve _Xs,_ 2. (Bottom) Mapping of the non-self
intersecting curve _X_ 2 _n−_ 1 _,_ 2 and its self-intersecting version, _X_ 2 [(1)] _n−_ 1 _,_ 2 [, under the soft limit.] [As]

we can see, _X_ 2 _n−_ 1 _,_ 2 is mapped to an honest boundary curve, which is zero, while _X_ 2 [(1)] _n−_ 1 _,_ 2
is mapped into the boundary curve _Xs,_ 2. Therefore, the only consistent way of defining the
soft limit is mapping _Xs,_ 2 = 0.


_Xs,_ 2. Of course, curve _X_ 2 _n−_ 1 _,_ 2 should also map to _Xs,_ 2. However, on the surface there
are two distinct curves labeled by _X_ 2 _n−_ 1 _,_ 2 - the one that self-intersects _X_ 2 [(1)] _n−_ 1 _,_ 2 [,] [repre-]
sented in blue on the right of Fig. 4, and the one which does not _X_ 2 _n−_ 1 _,_ 2, represented in
green. In the soft limit, _X_ 2 [(1)] _n−_ 1 _,_ 2 [maps] [into] [the] [self-intersecting] [boundary] [curve] _[X][s,]_ [2][,] [and]
the non-self-intersecting curve _X_ 2 _n−_ 1 _,_ 2 maps into a genuine boundary curve that therefore
should go to zero in the soft limit. However, in surface kinematics, we _don’t_ distinguish
between _X_ 2 [(1)] _n−_ 1 _,_ 2 [from] _[X]_ [2] _[n][−]_ [1] _[,]_ [2][,] [and] [thus] [the] [only] [consistent] [thing] [to] [do] [is] [say] [that] [these]
three curves (including _X_ 1 _,_ 2) get mapped to zero; this means that, in the soft limit, we
must enforce _Xs,_ 2 = 0. A similar story holds for curves _X_ 2 _n−_ 2 _,_ 2 _n−_ 1 and _X_ 2 _n−_ 2 _,_ 1, and can
be resolved in the same way by setting _X_ 2 _n−_ 2 _,s_ = 0. By defining the limit like this, the
lower-point integrand we land on after taking the soft limit is the one where the boundary
curves _Xs,_ 2 and _X_ 2 _n−_ 2 _,s_ have been set to zero.
Keeping this in mind, we will organize the one-loop soft limit as a Laurent expansion
in soft factors _δ_ 1 _,j_ = _ε_ ( _X_ 1 _,j_ _−_ _Xs,j_ ) and _δ_ 2 _n−_ 1 _,j_ = _ε_ ( _X_ 2 _n−_ 1 _,j_ _−_ _Xs,j_ ), with the analogous
for _δj,_ 1 _, δj,_ 2 _n−_ 1. As discussed, we need to set _Xs,_ 2 = _X_ 2 _n−_ 2 _,s_ = 0 and _Xs,_ 3 = _X_ 2 _n−_ 3 _,s_ = 0.


                   - 26                   

Therefore, the _X_ kinematical variables that vanish in the soft limit are given by



_X_ 2 _n−_ 3 _,_ 1( _ε_ ) = _δ_ 2 _n−_ 3 _,_ 1 _,_


_X_ 1 _,_ 2( _ε_ ) = _δ_ 1 _,_ 2 _,_


_X_ 2 _n−_ 2 _,_ 1( _ε_ ) = _δ_ 2 _n−_ 2 _,_ 1 _,_



_X_ 2 _n−_ 1 _,_ 3( _ε_ ) = _δ_ 2 _n−_ 1 _,_ 3 _,_


_X_ 2 _n−_ 2 _,_ 2 _n−_ 1( _ε_ ) = _δ_ 2 _n−_ 2 _,_ 2 _n−_ 1 _,_


_X_ 2 _n−_ 1 _,_ 2( _ε_ ) = _δ_ 2 _n−_ 1 _,_ 2 _._



(5.3)



Note that, if we were dealing with standard momentum space variables, we would also
have to take _X_ 1 _,_ 2 _n−_ 3 _→_ 0 and _X_ 3 _,_ 2 _n−_ 1 _→_ 0 in the soft limit by momentum conservation,
since these are connected to propagators _X_ 2 _n−_ 3 _,_ 1 and _X_ 3 _,_ 2 _n−_ 1 respectively by a bubble
diagram. However, in surface kinematics, the limit we get _only_ sends _X_ 2 _n−_ 3 _,_ 1 and _X_ 2 _n−_ 1 _,_ 3 to
zero. Therefore, in the soft limit, the answer will localize solely onto these two factorization

channels, just like we saw at tree-level. So, once again it is convenient to decompose the
surface loop integrand _In_ as




_[R]_ [2] _[n][−]_ [3] _[,]_ [1] + _[R]_ [2] _[n][−]_ [1] _[,]_ [3]

_X_ 2 _n−_ 3 _,_ 1 _X_ 2 _n−_ 1 _,_ 3



_In_ = _[R]_ [2] _[n][−]_ [3] _[,]_ [1]



+ _R,_ (5.4)
_X_ 2 _n−_ 1 _,_ 3



where _R_ 2 _n−_ 3 _,_ 1 and _R_ 2 _n−_ 1 _,_ 3 are the residues of _In_ at _X_ 2 _n−_ 3 _,_ 1 = 0 and _X_ 2 _n−_ 1 _,_ 3 = 0, respectively, and _R_ is everything else. Like at tree-level, _R_ manifestly starts at _O_ ( _δ_ [0] ) in the soft
expansion, since it has poles in neither _X_ 2 _n−_ 3 _,_ 1 nor _X_ 2 _n−_ 1 _,_ 3.
To derive the leading contribution to the soft limit, we again use the explicit expressions
for _R_ 2 _n−_ 3 _,_ 1 and _R_ 2 _n−_ 1 _,_ 3, given by the formula (2.13). We leave this for the next section
and App. B, and for now just discuss the generalization of the gauge-invariance constraint

(3.20) to one-loop-order.
As we see from Eq. (2.11) the one-loop gauge invariance statement for _In_ is very
similar to the tree-level case, up to corrections proportional to boundary curves. Therefore,

proceeding exactly in the same way as in the tree-level case, we find that gauge invariance

in 2 _n_ implies that we can write the integrand as



_In_ = _[R]_ [2] _[n][−]_ [3] _[,]_ [1]




[2] _[n][−]_ [1] _[,]_ [3]    
+
_X_ 2 _n−_ 1 _,_ 3




_[R]_ [2] _[n][−]_ [3] _[,]_ [1] + _[R]_ [2] _[n][−]_ [1] _[,]_ [3]

_X_ 2 _n−_ 3 _,_ 1 _X_ 2 _n−_ 1 _,_ 3




    _C_ 2 _n,j_ ( _X_ 2 _n,j_ _−_ _X_ 1 _,j_ ) +

_j_ _j_



_Cj,_ 2 _n_ ( _Xj,_ 2 _n −_ _Xj,_ 1)

_j_



+ _X_ 1 _,_ 2




- _∂R_
_C_ 2 _n,_ 2 +
_∂X_ 1 _,_ 2 ����2 _n→_ 1





_−_ _[∂R]_ [2] _[n][−]_ [3] _[,]_ [1] _,_

_∂X_ 2 _n−_ 3 _,_ 2 _n_



and, by interchanging 1 _↔_ 2 _n −_ 1, as



_In_ = _[R]_ [2] _[n][−]_ [3] _[,]_ [1]




_[R]_ [2] _[n][−]_ [3] _[,]_ [1] + _[R]_ [2] _[n][−]_ [1] _[,]_ [3]

_X_ 2 _n−_ 3 _,_ 1 _X_ 2 _n−_ 1 _,_ 3




[2] _[n][−]_ [1] _[,]_ [3]    
+
_X_ 2 _n−_ 1 _,_ 3




    _C_ 2 _n,j_ ( _X_ 2 _n,j_ _−_ _X_ 2 _n−_ 1 _,j_ ) +

_j_ _j_



_Cj,_ 2 _n_ ( _Xj,_ 2 _n −_ _Xj,_ 2 _n−_ 1)

_j_



(5.5)


(5.6)



����2 _n→_ 2 _n−_ 1





_−_ _[∂R]_ [2] _[n][−]_ [1] _[,]_ [3] _,_

_∂X_ 2 _n,_ 3



+ _X_ 2 _n−_ 2 _,_ 2 _n−_ 1




- _∂R_
_C_ 2 _n−_ 2 _,_ 2 _n_ +
_∂X_ 2 _n−_ 2 _,_ 2 _n−_ 1



where, just like in the tree-level case, the _C_ ’s are completely well defined by



_X_ 2 _n−_ 1 _,_ 3



_∂_
_C_ 2 _n,j_ =
_∂X_ 2 _n,j_




_In −_ _[R]_ [2] _[n][−]_ [3] _[,]_ [1]




_[R]_ [2] _[n][−]_ [3] _[,]_ [1] _−_ _[R]_ [2] _[n][−]_ [1] _[,]_ [3]

_X_ 2 _n−_ 3 _,_ 1 _X_ 2 _n−_ 1 _,_ 3




_,_ (5.7)




- 27 

and similarly for _Cj,_ 2 _n_ . Therefore, subtracting Eqns. (5.5) and (5.6), the one-loop generalization of Eq. (3.20) is



(5.8)



����2 _n→_ 1








    _C_ 2 _n,j_ ( _X_ 2 _n−_ 1 _,j_ _−_ _X_ 1 _,j_ ) +

_j_ _j_



_Cj,_ 2 _n_ ( _Xj,_ 2 _n−_ 1 _−_ _Xj,_ 1) + _X_ 1 _,_ 2

_j_








- _∂R_
_C_ 2 _n,_ 2 +
_∂X_ 1 _,_ 2



_._
_∂X_ 2 _n−_ 3 _,_ 2 _n_



����2 _n→_ 2 _n−_ 1




= _−_ _[∂R]_ [2] _[n][−]_ [1] _[,]_ [3]




[2] _[n][−]_ [1] _[,]_ [3]

+ _[∂R]_ [2] _[n][−]_ [3] _[,]_ [1]
_∂X_ 2 _n,_ 3 _∂X_ 2 _n−_ 3 _,_ 2




_−_ _X_ 2 _n−_ 2 _,_ 2 _n−_ 1




- _∂R_
_C_ 2 _n−_ 2 _,_ 2 _n_ +
_∂X_ 2 _n−_ 2 _,_ 2 _n−_ 1



Due to its similarity to Eq. (2.5), one might expect that we can once again extract the

leading order behavior of the _C_ ’s from the above constraint. Unfortunately, this naive

strategy will not work here. This is because, if we expand the _l.h.s._ of the above equation
in soft factors, we now find a term _Xs,s_ ( _C_ 2 _n−_ 1 _,_ 2 _n_ _−_ _C_ 2 _n,_ 1) starting at _O_ ( _δ_ [0] ), due to the
fact _X_ 2 _n−_ 1 _,_ 1 = 0 on the scaffolding residue. Since _Xs,s_ is _not_ a soft factor, we cannot
exactly match terms at _O_ ( _δ_ ) as we did at tree-level. We leave to future investigations the

question of whether there is some other way to extract the leading _C_ ’s out of Eq. (5.8), or

if additional inputs are needed.
In App. B, we give some explicit formulae for the residues _R_ 2 _n−_ 3 _,_ 1 and _R_ 2 _n−_ 1 _,_ 3 that
are needed to derive the one-loop soft expansion, particularly the leading term we explore

next.


**5.2** **The** **leading** **soft** **theorem** **for** **the** **one-loop** **integrand**


To derive the leading soft theorem at one-loop, we want to extract the leading order of
_R_ 2 _n−_ 3 _,_ 1 and _R_ 2 _n−_ 1 _,_ 3. Let’s start by looking at _R_ 2 _n−_ 1 _,_ 3. We can write it explicitly by
using the gluing rule (2.13), where, in this case, _AL_ = _A_ 3(3 _, xL,_ 2 _n −_ 1 _,_ 2 _n,_ 1 _,_ 2) and _IR_ =
_In−_ 1(3 _,_ 4 _, · · ·_ 2 _n −_ 2 _,_ 2 _n −_ 1 _, xR_ ). In App. B, proceeding just as we did at tree-level, we
present the different terms in the _j_ -sum over _∂Xj,xL_ _AL_ . There, we derive the following
leading order term in the expansion of _R_ 2 _n−_ 1 _,_ 3:



_∂In−_ 1
_R_ 2 _n−_ 1 _,_ 3 = _X_ 2 _n,_ 3 _× In−_ 1( _s,_ 2 _,_ 3 _, . . .,_ 2 _n −_ 2) _|S_ + ( _X_ 2 _n,_ 3 _−_ _X_ 2 _n,_ 2) _Xs,s_

_∂Xs,_ 2



+ _O_ ( _δ_ ) _,_ (5.9)
���� _S_



where “ _|S_ ” means we are setting the boundary curves _Xs,_ 2 _, X_ 2 _n−_ 2 _,s_ to zero. Doing the same
thing for _R_ 2 _n−_ 3 _,_ 1, we analogously find



_∂In−_ 1
_R_ 2 _n−_ 3 _,_ 1 = _X_ 2 _n−_ 3 _,_ 2 _n×In−_ 1( _s,_ 2 _,_ 3 _, . . .,_ 2 _n−_ 2) _|S_ +( _X_ 2 _n−_ 3 _,_ 2 _n−X_ 2 _n−_ 2 _,_ 2 _n_ ) _Xs,s_
_∂X_ 2 _n−_ 2 _,s_



+ _O_ ( _δ_ ) _._
���� _S_



(5.10)
So, in both cases, we see the appearance of the lower-point gluon integrand _In−_ 1 that we
obtain by collapsing _x_ _[µ]_ 1 [and] _[x][µ]_ 2 _n−_ 1 [into] [the] [point] _[x][µ]_ _s_ [.] [In] [fact,] [as] [we] [show] [in] [App.] [B][,] [it] [is]
surface gauge invariance that let’s us recognize the lower-point integrand at leading order

in the spin-sum formula — exactly mirroring the situation at tree-level! With both of these


                   - 28                   

expressions in-hand, we can write the one-loop integrand soft factor as




  - _X_ 2 _n,_ 3
_In_ = + _[X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n]_
_X_ 2 _n−_ 1 _,_ 3 _X_ 2 _n−_ 3 _,_ 1




_In−_ 1( _s,_ 2 _,_ 3 _, · · ·_ _,_ 2 _n −_ 2) _|S_



_∂In−_ 1
_∂X_ 2 _n−_ 2 _,s_ ���� _S_



(5.11)

+ _O_ ( _δ_ [0] ) _._



_∂In−_ 1

_∂Xs,_ 2



+ _[X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n][ −]_ _[X]_ [2] _[n][−]_ [2] _[,]_ [2] _[n]_
���� _S_ _X_ 2 _n−_ 3 _,_ 1



+ _Xs,s_




- _X_ 2 _n,_ 3 _−_ _X_ 2 _n,_ 2
_X_ 2 _n−_ 1 _,_ 3



All told, the integrand has precisely the same behavior as at tree-level, up to correction
terms proportional to _Xs,s_ . Nonetheless, when we go to physical kinematics, we should set
_Xs,s_ = 0. To consider this limit, we separate the term in the bracket into two categories:
those that have _Xs,s_ in the denominator, and those that do not. Terms in the latter
case vanish, while, in the former case, the _Xs,s_ ’s cancel, and so they survive when we set
_Xs,s_ _→_ 0. However, these correspond precisely to scaleless terms that therefore vanish
after loop-integration. So, as required, only the Weinberg term plays a physical role. It is

remarkable that, within surface kinematics, the leading term is not only a property of the

one-loop amplitude but of the one-loop integrand!

Just like at tree-level, we can easily gauge-invariantify the part that survives post-loop
integration to exactly match it with the leading Weinberg term:




  - _X_ 2 _n,_ 3  _In_ = + _[X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n]_ _−_ 1 _In−_ 1( _s,_ 2 _,_ 3 _, · · ·_ _,_ 2 _n −_ 2) _|S_
_X_ 2 _n−_ 1 _,_ 3 _X_ 2 _n−_ 3 _,_ 1



_∂In−_ 1
_∂X_ 2 _n−_ 2 _,s_ ���� _S_



(5.12)

+ _O_ ( _δ_ [0] ) _,_



_∂In−_ 1

_∂Xs,_ 2



+ _[X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n][ −]_ _[X]_ [2] _[n][−]_ [2] _[,]_ [2] _[n]_
���� _S_ _X_ 2 _n−_ 3 _,_ 1



+ _Xs,s_




- _X_ 2 _n,_ 3 _−_ _X_ 2 _n,_ 2
_X_ 2 _n−_ 1 _,_ 3



Quite beautifully, we have found that the canonical Yang-Mills loop integrand   - cru
cially defined using surface kinematics including tadpoles and external bubbles - also

enjoys a canonical behavior in the soft limit.


                   - 29                   

### **Part II: Transmutation of Gluons into Scalars**

We now switch to exploring a different topic— one which naturally arises from the fact that

gauge redundancies enforce a locked form for the scalar-scaffolded representation of gluon

amplitudes. As we reviewed in Sec. 2, gauge invariance and linearity in the polarization of
the _i_ [th] gluon restrict the form of _An_ to


    - _An_ (1 _,_ 2 _, . . .,_ 2 _n_ ) = [�] _j /∈{_ 2 _i,_ 2 _i±_ 1 _}_ [(] _[X]_ [2] _[i,j]_ _[−]_ _[X]_ [2] _[i][−]_ [1] _[,j]_ [)] _[∂][X]_ 2 _i,j_ _[A][n][,]_

(5.13)
_An_ (1 _,_ 2 _, . . .,_ 2 _n_ ) = [�] _j /∈{_ 2 _i,_ 2 _i±_ 1 _}_ [(] _[X]_ [2] _[i,j]_ _[−]_ _[X]_ [2] _[i]_ [+1] _[,j]_ [)] _[∂][X]_ 2 _i,j_ _[A][n][.]_


Staring at these expressions immediately suggests a simple kinematic locus, where we set


_X_ 2 _i,j_ _→_ 1 + _X_ 2 _i_ +1 _,j_ + _αi_ ( _X_ 2 _i−_ 1 _,j_ _−_ _X_ 2 _i_ +1 _,j_ ) _,_ for all _j_ _∈{/_ 2 _i,_ 2 _i ±_ 1 _}._ (5.14)


Here, the freedom in _αi_ is associated with gauge redundancy, and the 1 could be replaced
by any constant _c_, which would simply rescale the final answer. Note also that since the _X_ ’s
have units of _p_ [2], in making this choice we are working in units where this (dimensionful) _c_

is set to 1.

Since this limit changes only _X_ variables dependent on the index 2 _i_, it corresponds to
some particular choice of polarization _ϵi_ . We will explicitly define this configuration in the
following section. However, in scalar-scaffolded variables, one can simply use the forms in

Eq. (5.13) to see that this choice reduces the amplitude to



_An_ ( _X_ 2 _i,j_ _→_ 1 + _X_ 2 _i_ +1 _,j_ + _αi_ ( _X_ 2 _i−_ 1 _,j_ _−_ _X_ 2 _i_ +1 _,j_ )) =      

_j_


which is then equivalent to acting on _An_ with the operator



_∂An_
_,_ (5.15)
_∂X_ 2 _i,j_



_W_ 2 _i_ [ _F_ ] = 

_j /∈{_ 2 _i,_ 2 _i±_ 1 _}_



_∂_
_F._ (5.16)
_∂X_ 2 _i,j_



Note that this operator - a quite natural object within the scalar-scaffolded picture eliminates dependence on the index 2 _i_ (and therefore on the polarization _ϵi_ ) in the simplest
and most symmetric way possible. This fact alone suggests that, by acting with _W_ 2 _i_, we
might somehow be transmuting the _i_ [th] gluon into a scalar.

This is the idea we will explore systematically both at tree-level and one-loop here in

Part II. But before launching into this analysis, we can see that our results in Part I already
hint that the object we land on after applying _W_ 2 _i_ has intriguing structure suggestive of
some kind of “scalarization.” When we performed the soft expansion, we found it useful
to decompose _An_ in terms of the two collinear residues, _R_ 1 _,_ 2 _n−_ 3 and _R_ 3 _,_ 2 _n−_ 1, plus a part
without these poles. The latter could further be written in terms of the _Cj_ and a derivative
of one of the residues, as shown in Eq. (3.18) and, equivalently, in Eq. (3.19). Using the


                   - 30                   

explicit formulae for _R_ 1 _,_ 2 _n−_ 3 and _R_ 3 _,_ 2 _n−_ 1 given in App. A, it is trivial to check that



_∂X_ 2 _n−_ 3 _,_ 2 _n_



_W_ 2 _n_




- _R_ 1 _,_ 2 _n−_ 3
+ _[R]_ [3] _[,]_ [2] _[n][−]_ [1]
_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1




_[R]_ [3] _[,]_ [2] _[n][−]_ [1] + [�] _j_ [2] =2 _[n][−]_ [2][(] _[X][j,]_ [2] _[n][ −]_ _[X]_ [1] _[,j]_ [)] _[C][j]_ _[−]_ _[∂R]_ [1] _[,]_ [2] _[n][−]_ [3]

_X_ 3 _,_ 2 _n−_ 1 _∂X_ 2 _n−_ 3 _,_ 2 _n_




=



2 _n −_ 3 _,_ 2 _n −_ 2)

+ _[A][n][−]_ [1][(2] _[n][ −]_ [1] _[,]_ [ 2] _[,]_ [ 3] _[, . . .,]_ [ 2] _[n][ −]_ [2)]
_X_ 1 _,_ 2 _n−_ 3 _X_ 3 _,_ 2 _n−_ 1



_An−_ 1(1 _, . . .,_ 2 _n −_ 3 _,_ 2 _n −_ 2)



+ [�] _j_ [2] =2 _[n][−]_ [2] _[C][j][.]_
_X_ 3 _,_ 2 _n−_ 1



(5.17)

That is, the residues turn into precisely lower-point gluon amplitudes, defanged of the
standard spin-sum we get when we glue three-point and ( _n −_ 1)-point gluon amplitudes.
In App. A, we also show that the sum of _Cj_ given above obeys simple sum rules as an
expansion in soft factors. What’s more, for the special cases of _αi_ = 0 or _αi_ = 1, we can
recognize the kinematic locus (5.15) as that of one of the simplest “split” patterns - _skinny_

_rectangles_ - discussed in Refs. [2, 5]. These splits are true not only at the level of the field

theoretic amplitude but also at full stringy level, where they are most natural.

We now undertake a more systematic treatment, starting by rephrasing the kinematical
locus (5.15) in terms of constraints on the scalar _pi_ _· pj_, and ultimately translating these
into constraints on the dot products of the polarization and momenta of the gluons. We

then study gluon amplitudes using _surface_ _integrals_ [1], which we briefly review here to set

notation and explain our basic strategy. As proposed in [1, 2], the tree-level surface integral
associated to the disk with _n_ marked points on the boundary _Sn_ is given by [42, 43]:




      - + _∞_
_A_ [Tr(] _Sn_ _[ϕ]_ [3][)] [ _Xi,j_ ] =




 
_u_ _[X]_ _i,j_ _[i,j]_ [[] _[{][y][P][ }]_ []] _[,]_ (5.18)
( _i,j_ ) _∈Sn_




  Ω _yP_
0



where Ω _yP_ = [�] _P_ _∈T_ _[dy][P][ /y][P]_ [for] _[T]_ [some] [triangulation] [of] _[S][n]_ [,] [and] [we] [have] [taken] [the] [string]
scale _α_ _[′]_ _→_ 1. This integral is usually called the “stringy” Tr( _ϕ_ [3] ) integral as it yields treelevel Tr( _ϕ_ [3] ) amplitudes at low energies. The _ui,j_ ’s are the so-called _u_ -variables, where _ui,j_
is associated with the curve from marked point _i_ to marked point _j_ ; [6] they are functions of
the _positive_ _coordinates_, _yP_, such that for any value of _yP_ _∈_ [0 _,_ + _∞_ ), we have _ui,j_ _∈_ [0 _,_ 1],
for any ( _i, j_ ).

The _u_ -variables satisfy a set of non-linear equations — the _u_ -equations [42, 44] — which

at tree-level are simply

       _ui,j_ + _uk,m_ = 1 _._ (5.19)


( _k,m_ ) crossing ( _i,j_ )


Remarkably, although there are as many equations as _u_ -variables, the space of solutions

to these equations is quite non-trivial. Namely, at tree-level, these equations define an
( _n −_ 3)-dimensional space, which we can parametrize using the _yP_ ’s.
We then obtain the string amplitude for scalar-scaffolded gluons by a two-step procedure. We first perform the _δ_ -shift in Eq. (5.18), where we shift _Xi,j_ with + _δ_ if ( _i, j_ ) are


6In terms of the standard worldsheet coordinates, _zi,j_ = _zj_ _−zi_, the _ui,j_ are simply the SL(2 _,_ R)-invariant
cross-ratios, _ui,j_ = _zi,j−_ 1 _zi−_ 1 _,j/_ ( _zi,jzi−_ 1 _,j−_ 1) _._


                   - 31                   

both even, and _−δ_ if they are both odd, to obtain




     - + _∞_
_AS_ 2 _n_ [ _Xi,j_ _[δ]_ [] =]




 
_u_ _[X]_ _i,j_ _[i,j]_ [[] _[{][y][P][ }]_ []] _[ ×]_
( _i,j_ ) _∈S_ 2 _n_







��
( _i,j_ ) even _[u][i,j]_

 ( _i,j_ ) odd _[u][i,j]_




  Ω _yP_
0



_,_ (5.20)



where we have further set _δ_ = 1. At low energies, this integral describes the scattering of

the 2 _n_ scalars scaffolding the gluons. To finally obtain the gluon amplitude, we must further
put the gluons on-shell, which is done by taking the _scaffolding_ _residues_ on Eq. (5.20) [7]




         
_A_ [Gluon] _S_ 2 _n_ [ _Xi,j_ ] = _X_ Res1 _,_ 3=0 _X_ Res3 _,_ 5=0




- ��

_· · ·_ Res _._ (5.21)
_X_ 1 _,_ 2 _n−_ 1=0 _[A][S]_ [2] _[n]_ [[] _[X][i,j]_ []]



Having defined gluon amplitudes via surface integrals, we then study what happens
when we apply a single _We_ as well as collections of _We_ ’s. As we will see, the fact that the
surface integrals underlying gluon amplitudes satisfy “split” factorizations - together with

the machinery of surfaceology - allows us to cleanly describe the action of arbitrary sets
of _We_ ’s at the level of the surface integral. Most interestingly, we show that after applying
( _n −_ 2) _We_ ’s, the surface integral gives _Xe_ 1 _,e_ 2 (for the two indices missing out of the _We_ )
times a shifted integral— which, at field-theory level, magically conspires to give us the
Tr( _ϕ_ [3] ) amplitude. So, by applying ( _n −_ 2) _We_ ’s to the amplitude, we succeed in turning
all the _n_ gluons into scalars! We then conclude by describing the natural generalization of

this operator to one-loop surface kinematics. There, we’ll see that, by acting now with all
_n_ of them, we also can turn the one-loop YM integrand into the one-loop Tr( _ϕ_ [3] ) integrand.


**6** **Polarization** **Choice** **for** _We_


As just explained, from gauge invariance and multi-linearity we know that the action of _We_
is equivalent to fixing the _X_ ’s to the kinematical locus given in Eq. (5.15). For simplicity

of notation, let us take _e_ = 2 _n_ . We now want to translate this locus from scalar-scaffolded

language into standard gluon amplitude language, where it will correspond to conditions
on dot products involving _ϵ_ _[µ]_ _n_ [.]
Using the scalar-scaffolding map, we can write:


_∂_ _∂_
_A_ _[µ]_ _n_ [=] _An_ = _−_ _An,_ (6.1)
_∂ϵn,µ_ _∂x_ 2 _n,µ_



where _x_ _[µ]_ 2 _n_ [is] [the] [coordinate] [associated] [with] [vertex] [2] _[n]_ [in] [the] [scalar] [momentum] [polygon,]
and the minus sign is just a convention. But, since the scalar-scaffolded amplitude depends
on the chords _Xi,j_ = ( _xi_ _−_ _xj_ ) [2], it is useful to recast this derivative in terms of _X_ ’s as
follows:



_A_ _[µ]_ _n_ [=]



2 _n−_ 2





- _−_ 2 - _x_ _[µ]_ 2 _n_ _[−]_ _[x]_ _j_ _[µ]_ - _∂An_ _._ (6.2)

_∂Xj,_ 2 _n_
_j_ =2



7The result of this residue matches the standard open bosonic string gluon amplitude, where the gluon
polarization and momenta are scalar-scaffolded [1, 45].


                   - 32                   

So, a polarization _ϵn,µ −_ _αnqn,µ_ (with its gauge-dependence made explicit) that corresponds to the action of _W_ 2 _n_ is simply one that satisfies


2 [ _ϵn,µ −_ _αnqn,µ_ ] ( _x_ _[µ]_ 2 _n_ _[−]_ _[x]_ _j_ _[µ]_ [) =] _[ −]_ [1] _[,]_ for all _j_ _∈{_ 2 _, . . .,_ 2 _n −_ 2 _}._ (6.3)


Recall from Eq. (2.1) that we can write the polarization and momentum of gluon _i_ in terms
of scalar momenta as _ϵi,µ −_ _αiqi,µ_ = _p_ _[µ]_ 2 _i_ _[−]_ _[α][i]_ [(] _[p]_ [2] _[i][−]_ [1][ +] _[ p]_ [2] _[i]_ [)] _[µ]_ [and] _[q]_ _i_ _[µ]_ [=] [(] _[p]_ [2] _[i][−]_ [1][ +] _[ p]_ [2] _[i]_ [)] _[µ]_ [.] [Using]
this correspondence, we know that


_ϵ_ _[µ]_ _n_ _[−]_ _[α][n][q]_ _n_ _[µ]_ [=] _[ p]_ 2 _[µ]_ _n_ _[−]_ _[α][n]_ [(] _[p]_ 2 _[µ]_ _n_ [+] _[ p]_ 2 _[µ]_ _n−_ 1 [) = (] _[x]_ [1] _[ −]_ _[x]_ [2] _[n]_ [)] _[µ][ −]_ _[α][n]_ [(] _[x]_ [1] _[ −]_ _[x]_ [2] _[n][−]_ [1][)] _[µ][.]_ (6.4)


As a check, plugging this into Eq. (6.3) gives


_−Xj,_ 2 _n_ + _X_ 1 _,j_ + _αn_ ( _Xj,_ 2 _n−_ 1 _−_ _X_ 1 _,j_ ) = _−_ 1 _⇔_ _Xj,_ 2 _n_ = 1 + _X_ 1 _,j_ + _αn_ ( _Xj,_ 2 _n−_ 1 _−_ _X_ 1 _,j_ ) _,_ (6.5)


which is precisely the kinematical locus given in Eq. (5.15) for 2 _i_ = 2 _n_ .

Now, purely in terms of scalar momenta, the conditions in Eq. (6.3) are equivalent to


2[ _p_ 2 _n −_ _αn_ ( _p_ 2 _n_ + _p_ 2 _n−_ 1)] _· p_ 1 = 1 _,_

(6.6)
2[ _p_ 2 _n −_ _αn_ ( _p_ 2 _n_ + _p_ 2 _n−_ 1)] _· p_ 2 _n−_ 2 = _−_ 1 _,_


and

[ _p_ 2 _n −_ _αn_ ( _p_ 2 _n_ + _p_ 2 _n−_ 1)] _· pj_ = 0 _,_ for all _j_ _∈{_ 2 _, . . .,_ 2 _n −_ 3 _}._ (6.7)


We can then trivially translate these constraints into conditions on the dot products of _ϵ_ _[µ]_ _n_
to obtain



_q_ 1 _· ϵn_ = 1 _/_ 2 _,_


_qj_ _· ϵn_ = 0 _,_


_qn−_ 1 _· ϵn_ = _−_ 1 _/_ 2 _,_



_ϵ_ 1 _· ϵn_ = _−α_ 1 _/_ 2 _,_


_ϵj_ _· ϵn_ = 0 _,_


_ϵn−_ 1 _· ϵn_ = _−_ (1 _−_ _αn−_ 1) _/_ 2 _,_



with _j_ _∈{_ 2 _, . . ., n −_ 2 _},_ (6.8)



where the factor of 1 _/_ 2 is a normalization convention. So, we find that the only non-zero
dot products with _ϵ_ _[µ]_ _n_ [are those involving the two adjacent gluons,] [1][ and] _[ n]_ _[−]_ [1][,] [and that the]
precise value of these dot products is _gauge dependent_ - encoded in their explicit dependence
in _α_ 1 and _αn−_ 1. This means we have a full gauge orbit worth of polarization configurations
corresponding to the action of _W_ 2 _n_ . As suggested by this result, and as we show in Sec. 7.2,
_W_ 2 _n_ [ _An_ ] satisfies gauge invariance (2.3) in all but gluons 1 and _n −_ 1, a fact which will
become important when we study successive applications of this operator.

We can simplify the conditions in Eqs. (6.6) and (6.7) by selecting the special gauge
choices _αn_ = 0 _,_ 1:


_αn_ = 0 : 2 _p_ 2 _n · p_ 1 = _−_ 2 _p_ 2 _n−_ 2 _· p_ 2 _n_ = 1 _,_ 2 _p_ 2 _n · pj_ = 0 _,_

(6.9)
_αn_ = 1 : 2 _p_ 2 _n−_ 1 _· p_ 1 = _−_ 2 _p_ 2 _n−_ 2 _· p_ 2 _n−_ 1 = _−_ 1 _,_ 2 _p_ 2 _n−_ 1 _· pj_ = 0 _,_


with _j_ _∈{_ 2 _, . . .,_ 2 _n_ _−_ 3 _}_ . Though obviously not gauge invariant, these constraints are


                   - 33                   

exactly those from which we obtain a simple type of _split_ _factorization_ [2, 5], which we

explore in the next section.

In Ref. [46], the authors define a transmutation operator


_Ti,j,k_ = _∂qi·ϵj_ _−_ _∂qk·ϵj_ _,_ (6.10)


which acts on the gluon amplitude decreasing the spin of particle _j_ and inserting it between
particles _i_ and _k_ within a color trace structure. Of course, like we did with _We_, we can also
interpret this operator as a polarization configuration for gluon _j_ . In particular, if we take
_i_ = 1, _j_ = _n_ and _k_ = _n_ _−_ 1, then acting with _T_ 1 _,n,n−_ 1 corresponds to choosing a polarization
_ϵ_ _[µ]_ _n_ [such] [that:]



_q_ 1 _· ϵn_ = 1 _,_

_qn−_ 1 _· ϵn_ = _−_ 1 _,_



_qj_ _· ϵn_ = 0 _,_ with _j_ _∈{_ 2 _, . . ., n −_ 2 _},_

(6.11)
_ϵk · ϵn_ = 0 _,_ with _k_ _∈{_ 1 _, . . ., n −_ 1 _},_



which, up to a multiplicative factor, matches what we found in Eq. (6.8), for the particular
gauge choice of _α_ 1 = 0 and _αn−_ 1 = 1!
In addition, in Ref. [46], the authors show that acting with _Ti,j,k_ in _n −_ 2 adjacent
gluons together with the action of _Tl,m_ = _∂ϵl·ϵm_ on the remaining two, _i.e._, acting with



_T_ [ _{a_ 1 _, a_ 2 _, . . ., an}_ ] = _Ta_ 1 _,an_



_n−_ 1

- _Tai−_ 1 _,ai,an,_ (6.12)


_i_ =2



where _{a_ 1 _, a_ 2 _, . . ., an}_ = _α_ is an ordered set of labels, turns the _n_ -point gluon amplitude
with color-ordering _α_ into a pure Tr( _ϕ_ [3] ) amplitude with the same color-ordering. [8] This
then suggests that, by acting consecutively with ( _n −_ 2) _We_ operators, we should also be
very close to turning the gluon amplitude into a Tr( _ϕ_ [3] ) one. As we explain in the next

section, this is exactly the case.

However, to flesh this out, we first need to have some control on the objects we obtain after acting with _We_ . We will achieve this via the special gauge choices _αn_ = 0 _,_ 1, which allow
us to recast the action of _We_ as a split factorization, using the constraints given in Eq. (6.9).
Splits hold at the level of the surface integral that defines scalar-scaffolded gluon amplitudes

at low energies. As we will see, working directly at string-level will give us a natural way of
explaining what happens when we apply _W_ consecutively on the different gluons. Then, in

Sec. 8, we translate the results from splits back to standard polarization/momentum space
and compare the action of our operators with that of _T_ [ _a_ 1 _, a_ 2 _, · · ·_ _, an_ ] from Eq. (6.12).


**7** _We_ **as** **a** **Split** **Configuration**


We will now discuss the two split factorizations that land us on the kinematical loci corresponding to _αn_ = 0 and _αn_ = 1 in Eq. (5.15), from which we derive a concrete expression

- in the form of a surface integral - for _W_ 2 _n_ [ _An_ ]. Throughout this section, we will deal


8If, instead, we acted with Eq. (6.12) on a gluon amplitude with ordering _β_ = _α_, the resulting amplitude
would be a doubly color-ordered amplitude of bi-adjoint scalar theory.


                   - 34                   

**Figure** **5** : (Left) Two surfaces _S_ [(1)] (in blue) and _S_ 0 [(2)] (in red) associated with the split
relevant for the gauge choice _αn_ = 0. (Right) Surfaces _S_ [(1)] (in blue) and _S_ 1 [(2)] (in red)
entering the split for the gauge choice _αn_ = 1.


mostly with the surface integral defining 2 _n_ -point scalar scattering _AS_, and we will take
the scaffolding residues as necessary.
Looking back at the original unshifted Tr( _ϕ_ [3] ) surface integral (5.18), it was pointed

out in Ref. [5] that simple features of _u_ -variables allow us to derive kinematic loci where

the integral “splits” into the product of two integrals associated to subsurfaces that overlap

on a triangle. To derive these loci - also referred to as “split kinematics” - we map each
curve _Xi,j_ on the original surface _S_ 2 _n_ into the sum of its images in the subsurfaces _S_ [(1)]

(with kinematics _zi,j_ ) and _S_ [(2)] (with kinematics _xi,j_ ). Now, by going on split kinematics,
the _δ_ -shifted surface integral in Eq. (5.20) reduces to a _product_ of shifted surface integrals
associated to _S_ 1 and _S_ 2:


Split
_AS_ 2 _n_ [ _Xi,j_ _[δ]_ []] _−−−→AS_ (1)[ _zi,j_ _[δ]_ []] _[ × A]_ _S_ [(2)][[] _[x]_ _i,j_ _[δ]_ []] _[,]_ (7.1)


where the _δ_ subscript is included to remind us that the kinematics on both sides will be
shifted. While the _Xi,j_ are shifted with the standard _δ_ = _±_ 1, the shifts for _xi,j_ and _zi,j_ are
determined via the split map, as we explain in more detail in the next section.


**7.1** **One** **split**


In order to describe the action of _We_, the relevant split factorizations are of the simplest
type, in which we take _S_ [(1)] to be a disk with 4 marked points and _S_ [(2)] a disk with 2 _n −_ 1
marked points. Concretely, for the gauge choice corresponding to _αn_ = 0, we want the split
where _S_ [(1)] = (1 _,_ 2 _,_ 2 _n −_ 1 _,_ 2 _n_ ) and _S_ 0 [(2)] = (2 _,_ 3 _, . . .,_ 2 _n −_ 1 _,_ 2 _n_ ), while, for _αn_ = 1, we want
the same _S_ [(1)] but with _S_ 1 [(2)] = (1 _,_ 2 _, . . .,_ 2 _n −_ 2 _,_ 2 _n −_ 1) (see Fig. 5). Working out the split


                   - 35                   

kinematic configurations associated to these choices, we find



Split _αn_ = 0 :


_X_ 1 _,_ 2 _n−_ 1 = _z_ 1 _,_ 2 _n−_ 1 _,_


_X_ 2 _,_ 2 _n_ = _z_ 2 _,_ 2 _n,_

_X_ 1 _,j_ = _xj,_ 2 _n,_ for _j_ _∈S_ 0 [(2)] _\ {_ 2 _n −_ 1 _},_

_Xi,j_ = _xi,j,_ for ( _i, j_ ) _∈S_ 0 [(2)] _\ {_ 2 _n},_

_Xj,_ 2 _n_ = _z_ 2 _,_ 2 _n_ + _xj,_ 2 _n_


_↓_


_Xj,_ 2 _n_ = _X_ 2 _,_ 2 _n_ + _X_ 1 _,j_



Split _αn_ = 1 :


_X_ 1 _,_ 2 _n−_ 1 = _z_ 1 _,_ 2 _n−_ 1 _,_


_X_ 2 _n−_ 2 _,_ 2 _n_ = _z_ 2 _,_ 2 _n,_

_Xj,_ 2 _n−_ 1 = _xj,_ 2 _n−_ 1 _,_ for _j_ _∈S_ 1 [(2)] _\ {_ 1 _},_

_Xi,j_ = _xi,j,_ for ( _i, j_ ) _∈S_ 1 [(2)] _\ {_ 2 _n −_ 1 _},_

_Xj,_ 2 _n_ = _z_ 2 _,_ 2 _n_ + _xj,_ 2 _n−_ 1


_↓_


_Xj,_ 2 _n_ = _X_ 2 _n−_ 2 _,_ 2 _n_ + _Xj,_ 2 _n−_ 1 _,_



(7.2)



for _j_ = 2 _,_ 3 _, . . .,_ 2 _n −_ 2. If we further set _z_ 2 _,_ 2 _n_ = 1 in both splits, we are left with precisely
the kinematic conditions listed in Eq. (6.9), for the respective gauge-choices.

Let’s now see what happens at the level of the surface integral on the support of these
two split configurations. Starting with the _αn_ = 1 case, we know that the surface integral
will factorize as
Split
_AS_ 2 _n_ ( _Xi,j_ _[δ]_ [)] _−−−→αn_ =1 _[A]_ [4][[] _[z]_ 1 _[δ]_ _,_ 2 _n−_ 1 _[, z]_ 2 _[δ]_ _,_ 2 _n_ []] _[ × A]_ _S_ 1 [(2)][[] _[x]_ _i,j_ _[δ]_ []] _[.]_ (7.3)


Using the split map (7.2), we derive that _z_ 1 _[δ]_ _,_ 2 _n−_ 1 [=] _[X]_ 1 _[δ]_ _,_ 2 _n−_ 1 _[⇒]_ _[z]_ 1 _[δ]_ _,_ 2 _n−_ 1 [=] _[z]_ [1] _[,]_ [2] _[n][−]_ [1] _[ −]_ [1][,] [and]

similarly, _z_ 2 _[δ]_ _,_ 2 _n_ [=] _[ X]_ 2 _[δ]_ _n−_ 2 _,_ 2 _n_ _[⇒]_ _[z]_ 2 _[δ]_ _,_ 2 _n_ [=] _[ z]_ [2] _[,]_ [2] _[n]_ [ +1][;] [as for the kinematics] _[ x][δ]_ _i,j_ [of the surface] _[ S]_ 1 [(2)][,]
they have exactly the same shift as their respective _Xi,j_ . Therefore, we find that



_u_ 2 _,_ 2 _n_
_y_ _[u]_ 1 _[z]_ [1] _,_ 2 _[,]_ [2] _n_ _[n]_ _−_ _[−]_ 1 [1] _[u][z]_ 2 [2] _,_ 2 _[,]_ [2] _n_ _[n]_
_S_ [(1)][ Ω][(1)] _u_ 1 _,_ 2 _n−_ 1




- - _ue,e_

 - _uo,o_



(7.4)

_[,]_ [2] _[n][−]_ [1] _[ −]_ [1)Γ(] _[z]_ [2] _[,]_ [2] _[n]_ [ + 1)]

_,_
Γ( _z_ 1 _,_ 2 _n−_ 1 + _z_ 2 _,_ 2 _n_ )




- _×_



Split
_AS_ 2 _n_ _−−−→αn_ =1





  Ω [(2)] _y_ _u_ _[x]_ _i,j_ _[i,j]_
_S_ 1 [(2)]



= _AS_ 1(2) [[] _[x][i,j]_ [=] _[ X][i,j]_ []] _[ ×]_ [Γ(] _[z]_ [1] Γ( _[,]_ [2] _[n]_ _z_ _[−]_ 1 [1] _,_ 2 _[ −]_ _n−_ [1)Γ(] 1 + _z_ _[z]_ 2 [2] _,_ _[,]_ 2 [2] _n_ _[n]_ ) [ + 1)]



which, upon taking a scaffolding residue at _X_ 1 _,_ 2 _n−_ 1 = _z_ 1 _,_ 2 _n−_ 1 = 0 (turning the _n_ [th] gluon
on-shell), gives us


Split
Res _−−−→_
_X_ 1 _,_ 2 _n−_ 1=0 _[A][S]_ [2] _[n]_ _αn_ =1 _[−][z]_ [2] _[,]_ [2] _[n][ × A][S]_ 1 [(2)][[] _[X][i,j]_ []]



_⇔_ 



_−_ _X_ 2 _n−_ 1 _,j_ ) _∂X_ 2 _n,j_ _AS_ 2 _n_ = _−z_ 2 _,_ 2 _nAS_ 2 _n−_ 1(1 _,_ 2 _, . . .,_ 2 _n −_ 1)


_z_ 2 _,_ 2 _n_



(7.5)



( _X_ 2 _n,j_ _−_ _X_ 2 _n−_ 1 _,j_ )

_j_ _z_



_⇔_ _W_ 2 _n_ [ _AS_ 2 _n_ ] = _−AS_ 2 _n−_ 1(1 _,_ 2 _, . . .,_ 2 _n −_ 1) _,_


where we have used the fact that after taking scaffolding residue in _X_ 1 _,_ 2 _n−_ 1 recover the
statement of gauge invariance and linearity in the polarization vector of the _n_ [th] gluon.
_S_ 2 _n−_ 1 _≡S_ 1 [(2)] stands for surface we are left with - a disk with (2 _n −_ 1) marked points on


                   - 36                   

the boundary. By following the same procedure for the _αn_ = 0 split, we find




- - _u_ 2 _,_ 2 _n_
_×_ _y_ _[u][z]_ 1 [1] _,_ 2 _[,]_ [2] _n_ _[n]_ _−_ _[−]_ 1 [1] _[u][z]_ 2 [2] _,_ 2 _[,]_ [2] _n_ _[n]_

_S_ [(1)][ Ω][(1)] _u_ 1 _,_ 2 _n−_ 1



(7.6)




- [�]
_e_ =2 _n_ _[u][e,e]_

 - _uo,ou_ 2 _n,o_



Split
_AS_ 2 _n_ _−−−→αn_ =0





  Ω [(2)] _y_ _u_ _[x]_ _i,j_ _[i,j]_
_S_ 0 [(2)]



= _AS_ 0(2) [[] _[x][j,]_ [2] _[n]_ [=] _[ X]_ [1] _[,j][, x][i,j]_ [=] _[ X][i,j]_ []] _[ ×]_ [Γ(] _[z]_ [1] Γ( _[,]_ [2] _[n]_ _z_ _[−]_ 1 [1] _,_ 2 _[ −]_ _n−_ [1)Γ(] 1 + _z_ _[z]_ 2 [2] _,_ _[,]_ 2 [2] _n_ _[n]_ ) [ + 1)] _,_



where, as previously noted, _S_ 0 [(2)] = (2 _,_ 3 _, . . .,_ 2 _n −_ 1 _,_ 2 _n_ ). However, because we have _xj,_ 2 _n_ =
_X_ 1 _,j_ from split kinematics, the particular surface integral _AS_ 0(2) given above is equivalent

to _AS_ 1(2) [ _Xi,j_ ] _≡AS_ 2 _n−_ 1 [ _Xi,j_ ], _i.e._, the same integral appearing in the last line of Eq. (7.4).
And so, by taking the scaffolding residue on _X_ 1 _,_ 2 _n−_ 1 = _z_ 1 _,_ 2 _n−_ 1 = 0, we find


Split
_X_ 1 _,_ Res2 _n−_ 1=0 _[A][S]_ [2] _[n]_ _−−−→αn_ =0 _[−A][S]_ [2] _[n][−]_ [1][[] _[X][i,j]_ []] _⇔_ _W_ 2 _n_ [ _AS_ 2 _n_ ] = _−AS_ 2 _n−_ 1(1 _,_ 2 _, . . .,_ 2 _n −_ 1) _,_ (7.7)


which precisely agrees with the result from the previous split. Of course, this was expected,
since on the support of _X_ 1 _,_ 2 _n−_ 1 = 0, the two split configurations are gauge-equivalent.
So, in summary, we find that when we act with the operator _W_ 2 _i_ on the full 2 _n_   point scalar-scaffolded string amplitude _AS_ 2 _n_, we are left with the surface integral with the
appropriate even/odd _δ_ -shifts for a surface _without_ point 2 _i_ :




      _W_ 2 _i_ [ _AS_ 2 _n_ ] = _−_




 - - - _ue,e_

_u_ _[X]_ _i,j_ _[i,j]_ _×_    - _uo,o_
( _i,j_ ) _∈S_ 2 _n−_ 1




    Ω _y_
_S_ 2 _n−_ 1= _S_ 2 _n\{_ 2 _i}_




_,_ (7.8)



where _S_ 2 _n−_ 1 is the disk (1 _,_ 2 _, . . .,_ 2 _i −_ 1 _,_ 2 _i_ + 1 _, . . .,_ 2 _n_ ). Of course, by taking the rest of the
scaffolding residues _X_ 1 _,_ 3 = _X_ 3 _,_ 5 = _· · ·_ = _X_ 2 _i−_ 3 _,_ 2 _i−_ 1 = _X_ 2 _i_ +1 _,_ 2 _i_ +3 = _· · ·_ = _X_ 2 _n−_ 1 _,_ 1 = 0 on
Eq. (7.8), we can extract the action of _W_ 2 _i_ on the full string gluon amplitude.


**7.2** **Consecutive** **splits**


Having understood the result of applying a single _We_, we can now ask what happens if we
act with another _We′_ on the integral (7.8). In particular, we want to understand if we can
still describe this new polarization configuration as associated to the same splits identified

above, but now applied to a different gluon.

As we will see now, since the integral in Eq. (7.8) has an _odd_ number of points, the
ratio of _ue,e/uo,o_ turns out to not simplify in the same way as it does when the integral is
_even_ . As a result, the gauge invariance statement (5.13) for the gluons adjacent to 2 _i_ are

modified. Nonetheless, we find that for any gluon there is always at least one split pattern
that correctly gives the action of _W_ . Of course, we are free to define the action of _W_ via a

particular split choice (or in other words a convenient gauge), and since the final answer is

gauge invariant, it won’t depend on this choice.

Let’s see what happens explicitly with a simple example for _n_ = 4 (2 _n_ = 8); it will

be clear that the result generalizes to all _n_ . Looking at Eq. (7.8), we see that, after acting
with _W_ 8 on _AS_ 2 _n_ (and taking a scaffolding residue on _X_ 1 _,_ 2 _n−_ 1 = 0), the surface integral


                   - 37                   

associated to _S_ 7 becomes


_W_ 8









3


2





4 5 



_S_ 8


1 8













6


7





_._ (7.9)



Now, we want to apply the operator _W_ 2, associated with gluon 1, to the integral
associated with _AS_ 7, as defined in Eq. (7.9). To do this, let’s look at the split configuration
that would give us the action of _W_ 2. Just like in the _W_ 8 case, we should have naively two
options - _α_ 1 = 0 and _α_ 1 = 1 - where the first one imposes the locus _X_ 2 _,j_ = 1 + _X_ 3 _,j_ and
the second one imposes _X_ 2 _,j_ = 1 + _X_ 1 _,j_ . Let’s start by looking at the first case, for which
we have the following split:



_xi,j_



_X_ 2 _,_ 4 = _z_ 2 _,_ 4 _,_


_X_ 1 _,_ 3 = _z_ 1 _,_ 3 _,_



6


7














Gluon 1:


( _α_ 1 = 0)



3


2



_Xi,j_ = _xi,j,_ ( _i, j_ ) _∈S_ [(2)] _\ {_ 2 _},_



_⇒_















_X_ 3 _,j_ = _x_ 2 _,j,_ _j_ = 1



(7.10)





_X_ 2 _,j_ = _x_ 2 _,j_ + _z_ 2 _,_ 4 _._


|1|Col2|
|---|---|
|1<br>||



We can check whether this split is compatible with the _δ_ -shift by reading off the shifts on
the _xi,j_ and _zi,j_ . From the first two equalities we have _z_ 2 _[δ]_ _,_ 4 [=] _[X]_ 2 _[δ]_ _,_ 4 _[⇒]_ _[z]_ 2 _[δ]_ _,_ 4 [=] _[z]_ [2] _[,]_ [4][ + 1][,] [and]
similarly, _z_ 1 _[δ]_ _,_ 3 [=] _[z]_ [1] _[,]_ [3] _[ −]_ [1][.] [From] [the] [third] [equality] [we] [find] _[x][δ]_ 2 _,j_ [=] _[x]_ [2] _[,j]_ _[−]_ [1] [if] _[j]_ [is] [odd,] [and]
_x_ _[δ]_ 2 _,j_ [=] _[ x]_ [2] _[,j]_ [otherwise.] [Finally,] [for] [the] [split] [to] [be] [compatible] [with] [the] _[δ]_ [-shift,] [we] [must] [have]
that the last equation can be consistently shifted: on the _l.h.s._, we see that _X_ 2 _,j_ is shifted
with +1 if _j_ is even, and not shifted otherwise. This precisely agrees with the shift we
obtain for the _r.h.s._, which we just derived for _z_ 2 _,_ 4 and _x_ 2 _,j_ . Therefore, applying this split
and taking the scaffolding residue on _X_ 1 _,_ 3 = _z_ 1 _,_ 3 = 0 yields:




 
_u_ _[X]_ _i,j_ _[i,j]_
( _i,j_ ) _∈S_ [(2)]



Res _−−−→_ Split1
_X_ 1 _,_ 3=0 _[W]_ [8][ [] _[A][S]_ [8][]] _α_ 1=0








    Ω
_S_ [(2)] =(1 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _,_ 7)




- - _ue,e_

 - _uo,o_







(7.11)

_._




        _⇔W_ 2 [ _W_ 8 [ _AS_ 8]] =




 
_u_ _[X]_ _i,j_ _[i,j]_
( _i,j_ ) _∈S_ 2 _n\{_ 2 _,_ 8 _}_




- - _ue,e_

 - _uo,o_




   Ω
_S_ 2 _n\{_ 2 _,_ 8 _}_



Before proceeding, let’s see what we would have obtained if we had instead considered the


                   - 38                   

split corresponding to _α_ 1 = 1, given by:


_xi,j_



_X_ 2 _,_ 7 _→_ _z_ 2 _,_ 4 _,_


_X_ 1 _,_ 3 _→_ _z_ 1 _,_ 3 _,_



6


7














Gluon 1:


( _α_ 1 = 1)



3


2



_Xi,j_ _→_ _xi,j,_ ( _i, j_ ) _∈S_ [(2)] _\ {_ 1 _}_



_⇒_















_X_ 1 _,j_ _→_ _x_ 1 _,j,_ _j_ = 3



(7.12)





_X_ 2 _,j_ _→_ _x_ 1 _,j_ + _z_ 2 _,_ 4 _._


|1|Col2|
|---|---|
|1<br>||



Reading off the resulting _δ_ -shifts, we obtain _z_ 2 _[δ]_ _,_ 4 [=] _[ z]_ [2] _[,]_ [4][,] _[ z]_ 1 _[δ]_ _,_ 3 [=] _[ z]_ [1] _[,]_ [3] _[−]_ [1][,] _[ x]_ 1 _[δ]_ _,j_ [=] _[ X]_ 1 _[δ]_ _,j_ [.] [However,]
given these shifts, the final equality is not consistently shifted: while on the _l.h.s._ we have
that _X_ 2 _,j_ is shifted by +1 when _j_ is even, and not shifted otherwise, on the _r.h.s._ for even
_j_ we obtain no shift and a shift of _−_ 1 for odd _j_ . Therefore this split kinematics is _not_

compatible with the _δ_ -shift, and this split doesn’t hold.
However, there is a simple way to fix this. Let us define _X_ [ˆ] 2 _,_ 7 = _X_ 2 _,_ 7 _−_ 1. If we write
the integral (7.8) (for 2 _i_ = 8) in terms of _X_ [ˆ] 2 _,_ 7, we find that _X_ [ˆ] 2 _,_ 7 will be shifted with +1
(since _X_ 2 _,_ 7 has no shift). By doing this and applying the same split (7.12), by construction
we find that it is compatible with the “new” _δ_ -shift, but now this shift happens in the locus


_X_ ˆ2 _,_ 7 = 1 _⇔_ _X_ 2 _,_ 7 = 2 _,_ _X_ 2 _,j_ = 1 + _X_ 1 _,j,_ for _j_ = 7 _._ (7.13)


This is simply reflecting the fact that the gauge invariance statement for 2, when making
manifest the dependence in ( _X_ 2 _,j −_ _X_ 1 _,j_ ), is different than the standard one for the integral
defining _W_ 8[ _AS_ 8] _≡AW_ 8. In particular, from Eq. (7.13), we have





( _X_ 2 _,j_ _−_ _X_ 1 _,j_ ) _[∂][A][W]_ [8]

_∂X_ 2 _,j_

_j_ =7



_AW_ 8 = 



_[∂][A][W]_ [8] + ( _X_ 2 _,_ 7 _−_ 1) _[∂][A][W]_ [8]

_∂X_ 2 _,j_ _∂X_ 2 _,_ 7



_._ (7.14)
_∂X_ 2 _,_ 7



However, since there were no problems with the initial split corresponding to the locus
_X_ 2 _,j_ _→_ 1 + _X_ 3 _,j_, we still have



( _X_ 2 _,j_ _−_ _X_ 3 _,j_ ) _[∂][A][W]_ [8]

_∂X_ 2 _,j_

_j_



_AW_ 8 = 


_._ (7.15)
_∂X_ 2 _,j_



Therefore, subtracting Eq. (7.15) and Eq. (7.14), we obtain the following identity





( _X_ 3 _,j_ _−_ _X_ 1 _,j_ ) _[∂][A][W]_ [8]

_∂X_ 2 _,j_

_j_ =7








_[∂][A][W]_ [8] + ( _X_ 3 _,_ 7 _−_ 1) _[∂][A][W]_ [8]

_∂X_ 2 _,j_ _∂X_ 2 _,_ 7



= 0 _,_ (7.16)
_∂X_ 2 _,_ 7



and, using this, we can describe the gauge orbit corresponding to the polarization choice of
_W_ 2 on _AW_ 8 as


_X_ 2 _,_ 7 = 1 + _X_ 3 _,_ 7 + _α_ 1(1 _−_ _X_ 3 _,_ 7) _,_ _X_ 2 _,j_ = 1 + _X_ 3 _,j_ + _α_ 1( _X_ 1 _,j −_ _X_ 3 _,j_ ) _,_ for _j_ = _{_ 7 _,_ 8 _}._ (7.17)


                   - 39                   

For _α_ 1 = 1, this polarization choice is of the same form as what we found for _W_ 8, but in
general it is different.

Looking back at the split mappings, it is simple to understand that this modification

in the gauge-invariant statement comes from the fact that the non-scaffolding chord inside
the four-point subsurface, which should be shifted with +1, gets mapped into an _Xe,o_ in
the big surface, which is not shifted. This only happens because after acting with _W_,

the surface we are dealing has one fewer point and hence has two consecutive odd indices.

Therefore, it is straightforward that the only “gluons” that will have modifications in their

gauge-invariance statements are those adjacent to the ones that have already been acted
on with _We_ (where the _e_ ’s are no longer part of the surface).
In particular, in the four-point example we are considering, this means that the gauge
invariance statement for gluon 2 after acting with _W_ 8 should be unaffected, but the one
for gluon 3 should have a modification. Indeed, if we repeat the exercise we just did for
gluon 1, but now considering the relevant splits for gluons 2 and 3 (giving the action of _W_ 4
and _W_ 6, respectively), we find the following. For gluon 2, both gauge choices _α_ 2 = 0 and
_α_ 2 = 1 lead to a split map consistent with the _δ_ -shift, reflecting standard gauge invariance
for gluon 2. As for gluon 3, we find that the split corresponding to _α_ 3 = 1, which is given
by the mapping _X_ 6 _,j_ = 1 + _X_ 5 _,j_, is compatible with the _δ_ -shift, but the same is not true
for the case _α_ 3 = 0, which gives the mapping _X_ 6 _,j_ = 1 + _X_ 7 _,j_, precisely as we expected.
Concretely, we find that the gauge invariance statements in 6 are





( _X_ 6 _,j_ _−_ _Xj,_ 7) _[∂][A][W]_ [8]

_∂X_ 6 _,j_

_j_ =1



_AW_ 8 = 



_[∂][A][W]_ [8] + ( _X_ 1 _,_ 6 _−_ 1) _[∂][A][W]_ [8]

_∂X_ 6 _,j_ _∂X_ 1 _,_ 6



_∂X_ 1 _,_ 6



( _X_ 6 _,j_ _−_ _Xj,_ 5) _[∂][A][W]_ [8]

_∂X_ 6 _,j_

_j_



_,_ (7.18)




 =



_∂X_ 6 _,j_



which is completely analogous to what we found for gluon 1. Note that the direction in

which the modification happens is the one touching the (1 _,_ 7) edge, in this case associated
with the differences ( _X_ 6 _,j_ _−_ _X_ 7 _,j_ ).
In summary, having applied any number of _We_, the gauge-invariance statements for
the gluons adjacent to the even indices that have been removed will be modified, in one of
the directions. We now proceed to studying what happens when we act with ( _n −_ 2) _We_ ’s.
To do this, we make use of the fact described above - that, at each step, there always is
a “good direction” for which the polarization configuration giving the action of _We_ is the
standard one, _i.e. Xe,j_ _→_ 1+ _Xe±_ 1 _,j_ . Using this fact, in Sec. 8, we give a simple description
of the polarization choice corresponding to acting with multiple _We_ ’s. Of course, since the
gluon amplitude is gauge invariant, any polarization configuration related to the one found
in this simple way will also correspond to applying the same set of _We_ .
Let’s for now stick to the two simple examples at four-points, where we have acted with
_W_ 4 or _W_ 6 on _AW_ 8, and give explicit expressions of the integrals we get in both cases. From
the action of _W_ 4, which we can induce by applying either one of the splits and taking the


                   - 40                   

residue on _X_ 3 _,_ 5 = 0, we obtain











3



 2



3




  _≡_

_S_ 6




- _dy_
_y_




_._




 
_u_ _[X]_ _i,j_ _[i,j]_
( _i,j_ ) _∈S_ 6



6



6




- _u_ 2 _,_ 6
_u_ 1 _,_ 3 _u_ 1 _,_ 5 _u_ 3 _,_ 7 _u_ 5 _,_ 7



_W_ 4



 2







(7.19)
On the other hand, applying the “good” split to define _W_ 6 and applying the scaffolidng
residue _X_ 5 _,_ 7 = 0, we find











3



 2



3




_._




 
_u_ _[X]_ _i,j_ _[i,j]_
( _i,j_ ) _∈S_ 6



6




- _u_ 2 _,_ 4
_u_ 1 _,_ 3 _u_ 1 _,_ 5 _u_ 3 _,_ 5 _u_ 3 _,_ 7



_W_ 6



 2








  _≡_

_S_ 6




- _dy_
_y_


|4 5|Col2|5|Col4|
|---|---|---|---|
|_S_6<br>7<br>1<br><br>|_S_6<br>7<br>1<br><br>|||
|_S_6<br>7<br>1<br><br>|||7|



(7.20)
Now, since the original four-point YM amplitude has units of _X_ [2], after acting twice
with _W_ operators, the resulting units are _X_ [0] . Therefore, we want to extract the piece with
units _X_ [0] from the low-energy expansion of Eqs. (7.19) and (7.20). Since we further know

that the final answer should be linear in indices (2 _,_ 6) and (2 _,_ 4), respectively, it can only be

of the form _X/X_ . In addition, since there can at most be a single _X_ in the numerator, this
linearity statement implies that, in the case where we acted with _W_ 4 (7.19), the numerator
is _X_ 2 _,_ 6, and, for the case of _W_ 6, the _X_ in the numerator must be _X_ 2 _,_ 4.
Let’s start with Eq. (7.19) and extract the scaffolding residue corresponding to _X_ 1 _,_ 3 = 0.
Since we only care about the piece proportional to _X_ 2 _,_ 6, we can write



_dy_ 1 _,_ 5

_y_ 1 _,_ 5




 - 1

_u_ _[X]_ _i,j_ _[i,j]_ _u_ 1 _,_ 3 _u_ 1 _,_ 5 _u_ 3 _,_ 7 _u_ 5 _,_ 7 _×_ _[∂]_ [log(] _∂y_ 1 _[u]_ _,_ 3 [2] _[,]_ [6][)]
( _i,j_ ) _∈{_ 1 _,_ 3 _,_ 4 _,_ 5 _,_ 7 _}_



_∂y_ 1 _,_ 3



���� _y_ 1 _,_ 3=0



Res [=] _[X]_ [2] _[,]_ [6]
_X_ 1 _,_ 3=0 _[A][S]_ [6]




- _∞_


0



_dy_ 5 _,_ 7

_y_ 5 _,_ 7







+ (independent of _X_ 2 _,_ 6) _._


where from the _u_ -equation for _u_ 2 _,_ 6 we have that _∂y_ 1 _,_ 3 log( _u_ 2 _,_ 6) _|y_ 1 _,_ 3 = _u_ 1 _,_ 3 _u_ 1 _,_ 5 _u_ 3 _,_ 7 _u_ 5 _,_ 7, precisely canceling all the denominator factors in the integral. So, by further taking the
scaffolding residue in _X_ 5 _,_ 7, we are left with




   - _∞_
_X_ 2 _,_ 6 _×_

0



_dy_ 1 _,_ 5 low energies - 1 1

_u_ _[X]_ 1 _,_ 5 [1] _[,]_ [5] _[u]_ 3 _[X]_ _,_ 7 [3] _[,]_ [7] _−−−−−−−→_ _X_ 2 _,_ 6 _×_ +
_y_ 1 _,_ 5 _X≪_ 1 _X_ 1 _,_ 5 _X_ 3 _,_ 7







+ _O_ ( _X_ ) _,_ (7.21)



_A_ [Tr] 4 [(] _[ϕ]_ [3)] (1 _,_ 3 _,_ 5 _,_ 7)


where we find the appearance of the Tr( _ϕ_ [3] ) amplitude for the gluon inner-gon! Of course,
we can make the _X_ 2 _,_ 6 factor disappear trivially by acting with either _W_ 2 or _W_ 6.
So we find that, by acting consecutively with _We_ on all the gluons but one, we turn
the gluon amplitude into a purely Tr( _ϕ_ [3] ) amplitude! If instead we only acted with all _We_ ’s
but two, we get the Tr( _ϕ_ [3] ) amplitude multiplied by a single _X_ that ensures linearity in the

remaining two gluons.


                   - 41                   

We will prove this result for the general _n_ -point gluon amplitude in the next section.

But, before doing that, let’s look at what would have happened in the case described by
Eq. (7.20), where instead of acting with _W_ 8 and _W_ 4, we acted with _W_ 8 and _W_ 6. In this
case, keeping the part proportional to _X_ 2 _,_ 4 in the _X_ 1 _,_ 3 residue, we obtain




 - 1

_u_ _[X]_ _i,j_ _[i,j]_ _u_ 1 _,_ 3 _u_ 1 _,_ 5 _u_ 3 _,_ 5 _u_ 3 _,_ 7 _×_ _[∂]_ [log(] _∂y_ 1 _[u]_ _,_ 3 [2] _[,]_ [4][)]
( _i,j_ ) _∈{_ 1 _,_ 3 _,_ 4 _,_ 5 _,_ 7 _}_



_∂y_ 1 _,_ 3



���� _y_ 1 _,_ 3=0



_dy_ 1 _,_ 5

_y_ 1 _,_ 5



Res [=] _[X]_ [2] _[,]_ [4]
_X_ 1 _,_ 3=0 _[A][S]_ [6]




- _∞_


0



_dy_ 3 _,_ 5

_y_ 3 _,_ 5







+ (independent of _X_ 2 _,_ 4) _._



But now, we have that _∂y_ 1 _,_ 3 log( _u_ 2 _,_ 4) _|y_ 1 _,_ 3 = _u_ 1 _,_ 3 _u_ 3 _,_ 7 _u_ 3 _,_ 5, which cancels all the _u_ ’s in the
denominator except for _u_ 1 _,_ 5. Therefore, after taking the scaffolding residue on _X_ 5 _,_ 7, we
derive




   - _∞_
_X_ 2 _,_ 4 _×_



_dy_ 1 _,_ 5 1

_u_ _[X]_ 1 _,_ 5 [1] _[,]_ [5] _[u][X]_ 3 _,_ 7 [3] _[,]_ [7] _×_ = _X_ 2 _,_ 4 _×_ [Γ(] _[X]_ [1] _[,]_ [5] _[ −]_ [1)Γ(] _[X]_ [3] _[,]_ [7][)]
_y_ 1 _,_ 5 _u_ 1 _,_ 5 Γ( _X_ 1 _,_ 5 + _X_ 3 _,_ 7 _−_ 1)



Γ( _X_ 1 _,_ 5 + _X_ 3 _,_ 7 _−_ 1)



_dy_ 1 _,_ 5



_._ (7.22)



0



_→A_ 4 [Tr][(] _[ϕ]_ [3)] (1 _,_ 3 _,_ 5 _,_ 7)+ _O_ ( _X_ )


So, in this case we don’t get exactly the surface Tr( _ϕ_ [3] ) integral (5.18) - instead, we have
an extra factor of 1 _/u_ 1 _,_ 5. Even so, in this case it is trivial to see that the leading low-energy
part of this integral is _still_ the four-point Tr( _ϕ_ [3] ) amplitude. And, once again, if we act
with _W_ 4 or _W_ 2 on this object are left with the purely scalar amplitude just like before. In
general, after applying ( _n −_ 2) _W_ ’s, we will find integrals like this one, that are not flat-out
the standard “surface” Tr( _ϕ_ [3] ) integrals shown in Eq. (5.18). But, we will show that, for this
new class of integrals, the leading order in the low-energy expansion is still Tr( _ϕ_ [3] ) theory.

We explain this now.
At higher points, the strategy is clear: we start by applying the ( _n −_ 2) splits that give
us the action of ( _n −_ 2) _We_ operators, for all _e_ except _e_ 1 _, e_ 2 (see the _l.h.s._ of Fig. 6). From
this, we obtain the _δ_ -shifted integral associated to surface where all even indices except
_e_ 1 _, e_ 2 have been deleted from the original surface (first equation on the _r.h.s._ of Fig. 6).
Then, when we extract the scaffolding residue associated with _e_ 1 ( _Xi_ 1 _,j_ 1 = 0, as depicted
in Fig. 6), we want to collect the piece proportional to _Xe_ 1 _,e_ 2 in order to ensure linearity
in polarizations _e_ 1 and _e_ 2. Again, the term proportional to _Xe_ 1 _,e_ 2 brings to the integrand
a factor of _∂yi_ 1 _,j_ 1 log( _ue_ 1 _,e_ 2) _|yi_ 1 _,j_ 1 =0, which we can compute using the _u_ -equation for _ue_ 1 _,e_ 2;
the result is _∂yi_ 1 _,j_ 1 log( _ue_ 1 _,e_ 2) _|yi_ 1 _,j_ 1 =0 = _−_ [�] _i∈I,j∈J_ _[u][i,j]_ [,] [where] _[I]_ [is] [the] [set] [of] _[odd]_ [indices]
between _i_ 1 and _i_ 2 (including _i_ 1 and _i_ 2), and _J_ is that between _j_ 1 and _j_ 2 (including _j_ 1 and
_j_ 2), since these are all the curves that cross ( _e_ 1 _, e_ 2). This leaves us with the integral in the
second line in Fig. 6. There, we see a factor of one over the product of _u_ ’s corresponding

to curves that start and end in _I_, and the same for _J_ - these are represented in blue on
the _l.h.s._ of Fig. 6. Finally, extracting the last residue in _Xi_ 2 _,j_ 2, we obtain the bottom line
in Fig. 6, which is now a surface integral defined over the inner _odd_ n-gon that we get after

taking all scaffolding residue.
So, in summary, after applying ( _n −_ 2) consecutive splits, the result is simply a prefactor of _Xe_ 1 _,e_ 2 times a particular surface integral over the disk with _n_ -marked points on
the boundary. All of the points on the disk are labeled by odd indices, corresponding to the


                   - 42                   

_Sn_




- _dyo,o_
_yo,o_



_u_ _[X]_ _X_  - _ui,ju_  - _e_ 1 _,eu_ 2
_X_




 - _ui,j_ - _ui,i⋆_ - _uj,j⋆_

_i∈I,j∈J_




- _dyo,o_
_yo,o_











_dyi_ 2 _,j_ 2

_yi_ 2 _,j_ 2






- _dyi_ 1 _,j_ 1
_yi_ 1 _,j_ 1


Res
� _Xi_ 1 _,j_ 1 =0


= _Xe_ 1 _,e_ 2


Res
� _Xi_ 2 _,j_ 2 =0


= _Xe_ 1 _,e_ 2



1
_u_ _[X]_ _X_  - _ui,i_ _[∗]_
_X_




 - _ui,i_ _[∗]_ 
_i,i_ _[∗]_ _∈I_ _j,j_ _[∗]_ _∈_




 - _uj,j_ _[⋆]_ [+] _[ · · ·]_

_j,j_ _[∗]_ _∈J_






- _dyi_ 2 _,j_ 2
_yi_ 2 _,j_ 2




- _dyo,o_
_yo,o_













1
_u_ _[X]_ _X_  - _ui,i_ _[⋆]_
_X_


|Col1|Col2|Col3|i2<br>e2<br>j2|Col5|Col6|
|---|---|---|---|---|---|
|_S_2_n_||||||
|_S_2_n_||_S_2_n_|_S_2_n_|||
|_S_2_n_||_S_2_n_|_S_2_n_|||
|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1|
|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1|1<br>_e_1<br>_j_1||
|1<br>_e_1<br>_j_1||||||




 - _ui,i_ _[⋆]_ 
_i,i_ _[∗]_ _∈I_ _j,j_ _[∗]_




 - _uj,j_ _[⋆]_

_j,j_ _[∗]_ _∈J_







**Figure** **6** : (Left) In red, we draw the leftover surface obtained after acting with _We_ on all
even indices apart from _e_ 1 and _e_ 2. The set of indices between _i_ 1 and _i_ 2 we call _I_, and those
between _j_ 1 and _j_ 2 we call _J_ . The curves in blue are the curves starting and ending in either
_I_ or _J_ . (Right) On the first line is the surface integral associated to the red surface. After
taking the two remaining scaffolding residue in _Xi_ 1 _,j_ 1 and _Xi_ 2 _,j_ 2, we find the surface Tr( _ϕ_ [3] )
integral with an extra factor of one over the product of the _u_ ’s associated with the curves
highlighted in blue on the left.


inner _n_ -gon, and, in addition to the standard logarithmic form and Koba-Nielsen factor,

we have a factor of one over the product of all the _u_ ’s living in the two smaller subsurfaces
determined by the chords ( _i_ 1 _, i_ 2) and ( _j_ 1 _, j_ 2):






     _≡_ _Xe_ 1 _,e_ 2 _×_

_Sn_




- _dy_
_y_




 - 1

( _i,j_ ) _∈Sn_ _u_ _[X]_ _i,j_ _[i,j]_ �( _i,j_ ) _∈SL_ _[u][i,j]_ _[×]_ [ �] ( _i,j_ ) _∈SR_ _[u][i,j]_ _,_ (7.23)







where _SL_ and _SR_ include curves ( _i_ 1 _, i_ 2) and ( _j_ 1 _, j_ 2), respectively. If instead we took _e_ 2 =
_e_ 1 + 2 (this is _i_ 1 = _i_ 2), we obtain the extremal case where _SL_ disappears, and instead we
get the following integral:


_k_ 3




 - 1

_u_ _[X]_ _i,j_ _[i,j]_   - _,_ (7.24)
( _i,j_ ) _∈Sn_ ( _i,j_ ) _∈SR_ _[u][i,j]_



_k_ 2




        _SR_ _≡_ _Xe_ 1 _,e_ 2 _×_

_Sn_




- _dy_
_y_



_k_ 1


where again _SR_ includes curve ( _k_ 1 _, k_ 3).
So, in both cases, the integral we obtain is not _precisely_ the “surface” Tr( _ϕ_ [3] ) integral


                   - 43                   

- it is instead one where certain kinematics _Xi,j_ are shifted by _−_ 1. Yet, as we will now
demonstrate, all of these integrals remarkably give the _n_ -point Tr( _ϕ_ [3] ) amplitude at leading
order in the low-energy expansion! With this result, we find that, by acting with ( _n −_ 2)
_We_ ’s on the _n_ -point gluon amplitude (2 _n_ scalars), we produce the corresponding _n_ -point
Tr( _ϕ_ [3] ) amplitude, multiplied by the factor _Xe_ 1 _,e_ 2 for the two even indices left out of the set
of _We_ . If we further act with either _We_ 1 or _We_ 2, we kill the _Xe_ 1 _,e_ 2 pre-factor, and we are
left with the pure scalar amplitude - succeeding in converting _all_ the external gluons into

colored scalars!


**7.3** **Shifted** **stringy** **integrals** **and** **Tr(** _ϕ_ [3] **)** **at** **low** **energies**


Let’s now prove that the integrals found in Eqs. (7.23) and (7.24) indeed give Tr( _ϕ_ [3] ) am
plitudes at low energies. To do this, we want to show that the residue in any full triangu
lation/cubic diagram is equal to 1 (at leading order). We will demonstrate this recursively,

by taking one residue at a time in the triangulation chords, and understanding how the

result of each residue always lands us on integrals of the form of Eqs. (7.23) and (7.24).

We begin by looking at integrals of the form of Eq. (7.23). Pick a triangulation of the
surface _Sn_ . There are then two possibilities:


1. the triangulation contains a chord ( _k, m_ ) crossing both curves ( _i_ 1 _, i_ 2) and ( _j_ 1 _, j_ 2) (the
boundaries of _SL/SR_ );


2. the triangulation contains either chord ( _i_ 1 _, j_ 2) or ( _i_ 2 _, j_ 1).


Let’s start by looking at case 1. In this scenario, since the exponent of curve ( _k, m_ ) is _not_
shifted, when we take the residue at _Xk,m_ _→_ 0 we simply find the product of the two lower
surface integrals that result from cutting _Sn_ along ( _k, m_ ):







Res _Xk,m_ =0
_−−−−−−−→_





_×_



_,_ (7.25)







_k_















where in both cases we have precisely a kinematic shift of the same type of that of the

original surface, _i.e._ :

   -   



[ �] 1

_u_ _[X]_ _i,j_ _[i,j]_  _S_ [(1)] _SL_ [(1)] _[u][i,j]_




  _SL_ [(2)] _[u][i,j]_



_S_ [(1)][ Ω][(1)][ �]




  _SL_ [(1)] _[u][i,j]_




    _×_
_SR_ [(1)] _[u][i,j]_



_S_ [(2)][ Ω][(2)][ �]




[ �] 1

_u_ _[X]_ _i,j_ _[i,j]_  _S_ [(2)] _SL_ [(2)] _[u][i,j]_



_._
_SR_ [(2)] _[u][i,j]_



Here, we have lost the contribution coming from all the _ui,j_ associated to curves that cross
( _k, m_ ) because these go to one when _uk,m_ _→_ 0.
Now, let’s consider case 2, and say our triangulation contains curve ( _i_ 2 _, j_ 1). Then, once
more, since _Xi_ 2 _,j_ 1 is not shifted, extracting the residue at _Xi_ 2 _,j_ 1 = 0 simply gives us the


                   - 44                   

product of the two lower surface integrals:


Res _Xi_ 2 _,j_ 1 =0
_−−−−−−−→_ _j_ 1



_i_ 1


_i_ 2



_SR_ [(1)] _×_ _[i]_ 2



_j_ 2


_j_ 1



_SR_ [(2)] _,_ (7.26)



where now we see the appearance of two integrals of the extremal type given in Eq. (7.24).

Let us analyze what happens when we take a residue in this extremal case, where there

is only a factor of products of _u_ ’s associated with a single subsurface. Take the integral
given in Eq. (7.24) as an example. Whatever the triangulation we are considering for _Sn_
is, it either contains a chord _crossing_ ( _k_ 1 _, k_ 3), or it _contains_ chord ( _k_ 1 _, k_ 3). In the first
case, just like previously, it is trivial to check that under the residue of a curve that crosses
( _k_ 1 _, k_ 3) (say ( _k_ 2 _, m_ ) for some _m_ _∈{k_ 3 + 1 _, k_ 3 + 2 _, · · ·_ _, k_ 1 _−_ 1 _}_ ) the integral factorizes into
the product of two lower integrals of the same type as the original one, _i.e._ both associated

to a similar extremal case (7.24).
If instead the triangulation contains the chord ( _k_ 1 _, k_ 3), it is not so clear whether the
residue on _Xk_ 1 _,k_ 3 = 0 will still land us on an integral of the form of Eqs. (7.23) and (7.24),
since _Xk_ 1 _,k_ 3 gets shifted. Let’s now compute this residue explicitly. To simplify the notation,
we will take (without loss of generality) _k_ 1 = 1 _, k_ 2 = 2 _, k_ 3 = 3. We start by defining the
object that we are computing via the shift of the standard “stringy” Tr( _ϕ_ [3] ) integral as

follows



_ASn_ ( _X_ [ˆ] 1 _,_ 3 _,_ _X_ [ˆ] _i,j_ ) _,_ where _X_ [ˆ] 1 _,_ 3 = _X_ 1 _,_ 3 _−_ 1 _,_ and _X_ [ˆ] _i,j_ =




_Xi,j_ _−_ 1 _,_ if _i, j_ = 2 _,_

(7.27)
_Xi,j,_ otherwise.



Now, due to the kinematic shift, taking the residue at _X_ 1 _,_ 3 = 0 corresponds to extracting
the first residue of the unshifted amplitude at _X_ [ˆ] 1 _,_ 3 = _−_ 1. To compute this residue, we can
use the formula given in Ref. [47]:



Res _ASn_ ( _X_ [ˆ] 1 _,_ 3 _,_ _X_ [ˆ] _i,j_ ) =
_X_ ˆ1 _,_ 3= _−_ 1



_n−_ 1
�( _−c_ ˆ1 _,j_ ) _× ASR_ - _X_ ˆ1 _,m_ _→_ _X_ ˆ1 _,m_ + Θ( _j −_ _m_ )� _,_ (7.28)

_j_ =3



where _c_ ˆ1 _,j_ = _X_ [ˆ] 1 _,j_ + _X_ [ˆ] 2 _,j_ +1 _−_ _X_ [ˆ] 2 _,j_ _−_ _X_ [ˆ] 1 _,j_ +1, and Θ( _j −_ _m_ ) = 1, if _j_ _≥_ _m_, and 0 otherwise.
But crucially, we only want to keep the piece that has units of _X_ [0] from this residue, which
comes from the shifts in _X_ [ˆ] . In particular, the shifts in _X_ [ˆ], imply that some of the _c_ ˆ1 _,j_ are
also shifted by negative integers. It is easy to check that the _only_ _c_ ˆ1 _,j_ that gets shifted is
that of _j_ = _n −_ 1, for which we have _c_ ˆ1 _,n−_ 1 = _c_ 1 _,n−_ 1 _−_ 1. Therefore, the piece of order _X_ [0]

of this residue is simply


_X_ ˆ1Res _,_ 3= _−_ 1 _ASn_ ( _X_ [ˆ] 1 _,_ 3 _,_ _X_ [ˆ] _i,j_ ) = _ASR_      - _X_ ˆ1 _,m_ _→_ _X_ ˆ1 _,m_ + 1� + _O_ ( _X_ ) _._ (7.29)


                   - 45                   

So, we obtain the lower-point amplitude associated to the subsurface bounded by (1 _,_ 3),
but where now the kinematics _X_ [ˆ] 1 _,m_ _→_ _X_ [ˆ] 1 _,m_ + 1 — in terms of the original _X_ ’s, this means
that _X_ 1 _,m_ is _unshifted_ ! Therefore, we have that the residue in _X_ 1 _,_ 3 is again an integral of
the form of Eq. (7.24), where now _SR_ is bounded by curve (3 _, n_ ).
So, putting everything together, by computing the residue in _Xk_ 1 _,k_ 3 = 0 on Eq. (7.24),
we get



_k_ 3








[ �] 1

_u_ _[X]_ _i,j_ _[i,j]_  _S_ [(1)] _SR_ [(1)]



_._ (7.30)
_SR_ [(1)] _[u][i,j]_



= _k_ 1


_k_ 1 _−_ 1




     _SR_ [(1)] _≡_



_S_ [(1)][ Ω][(1)][ �]







Res
_Xk_ 1 _,k_ 3 =0









_k_ 2



In all the residues, we obtain a recursive result that always lands us on integrals of the

form of either Eq. (7.23) or Eq. (7.24). This means that we will eventually hit a situation

where one of the lower-point problems is in the form of the previously-considered example
at four-points. Since there we proved we get the Tr( _ϕ_ [3] )amplitude at low energies, we have

finished the proof.

This proof is largely pictorial and conceptual, but it is amusing to note its extensive use

of much of the basic technology of _u_ -variables and surfaceology. The final object we land

on - an (integer) kinematically-shifted stringy integral which nonetheless also reduces to
Tr( _ϕ_ [3] ) at low energies - is especially interesting. This suggests that the world of integer

kinematically-shifted integrals is even richer than we have realized so far.


**8** **Polarization** **Configuration** **for** **Consecutive** **Splits**


Having understood that, after applying ( _n −_ 2) _We_ on the _n_ -point gluon amplitude, we get
the _n_ -point Tr( _ϕ_ [3] ) amplitude (times _Xe_ 1 _,e_ 2), we now turn to discussing the polarization
configuration corresponding to this limit.

To do this we use the simple split kinematic configurations that define the action of
_We_ at each step, starting from the gluon amplitude all the way down to Tr( _ϕ_ [3] ). Note that,
in this way of describing the kinematical locus, the order in which we apply the different
_We_ will now be important. This is simply because, after applying a given _We_, index _e_
disappears, and so the map for the next operator will be with respect to the kinematics

that do not depend on _e_ . However, this ordering is just a practicality that makes it especially
straightforward to derive a particular polarization configuration for the action of these _We_ ’s.
After obtaining one such configuration, gauge invariance of the gluon amplitude tells us that
any gauge-equivalent configuration will similarly describe the action of the _We_ ’s.
Let’s consider a set of ( _n −_ 2) operators that includes all the even indices in _I_ 2 _n_ =
_{_ 1 _,_ 2 _,_ 3 _, · · ·_ _,_ 2 _n −_ 1 _,_ 2 _n}_ except for _e_ 1 and _e_ 2, and let’s for the moment assume that _e_ 1 and
_e_ 2 are not adjacent to each other (which would correspond to case Eq. (7.23)). So we have


                   - 46                   

two subsets of even indices adjacent to each other:


_EL_ = _{e_ _[L]_ 1 _[, e]_ 2 _[L][,][ · · ·]_ _[, e][L]_ _nL_ _[}][,]_ _ER_ = _{e_ _[R]_ 1 _[, e]_ 2 _[R][,][ · · ·]_ _[, e][R]_ _nR_ _[}][,]_ (8.1)


with _EL_ being the subset to the left of chord _Xe_ 1 _,e_ 2, and _ER_ that to the right of _Xe_ 1 _,e_ 2,
with _nR_ + _nL_ = _n −_ 2. One possible ordering in applying these operators is to start from
the one closest to _e_ 1 in _ER_ and end with the one closest to _e_ 2, and then proceed with the
one closest to _e_ 2 in _EL_ and end with the one closest to _e_ 1. In this way, we are going around
the disk counter-clock wise - once more, this is just one possibility. Doing it in this way,

since we are going counter-clockwise, it is simpler to consider the kinematic configuration
corresponding to _Xe,j_ _→_ _Xe−_ 1 _,j_ + 1 [9] . This yields:


_ER_ : _XeR_ 1 _[,j]_ [= 1 +] _[ X][e][R]_ 1 _[−]_ [1] _[,j][,]_ [for] _[j]_ _[∈]_ _[I]_ [2] _[n][,]_

_XeR_ 2 _[,j]_ [= 1 +] _[ X][e][R]_ 2 _[−]_ [1] _[,j][,]_ [for] _[j]_ _[∈]_ _[I]_ [2] _[n][ \ {][e][R]_ 1 _[}][,]_

...

_XeRnR_ _[,j]_ [= 1 +] _[ X][e][R]_ _nR_ _[−]_ [1] _[,j][,]_ [for] _[j]_ _[∈]_ _[I]_ [2] _[n][ \ {][e][R]_ 1 _[, e]_ 2 _[R][,][ · · ·]_ _[, e][R]_ _nR−_ 1 _[}][,]_


(8.2)


_EL_ : _XeL_ 1 _[,j]_ [= 1 +] _[ X][e][L]_ 1 _[−]_ [1] _[,j][,]_ [for] _[j]_ _[∈]_ _[I]_ [2] _[n][ \][ E][R][,]_

_XeL_ 2 _[,j]_ [= 1 +] _[ X][e][L]_ 2 _[−]_ [1] _[,j][,]_ [for] _[j]_ _[∈]_ _[I]_ [2] _[n][ \ {][E][R][ ∪]_ _[e][L]_ 1 _[}][,]_

...

_XeLnL_ _[,j]_ [= 1 +] _[ X][e][L]_ _nL_ _[−]_ [1] _[,j][,]_ [for] _[j]_ _[∈]_ _[I]_ [2] _[n][ \ {][E][R][ ∪]_ _[e][L]_ 1 _[, e]_ 2 _[L][,][ · · ·]_ _[, e][L]_ _nL−_ 1 _[}][.]_


This configuration defines one representative in the gauge orbit that gives the action of _We_
with _e ∈_ _ER ∪_ _EL_ . Due to gauge invariance, we can reach all the remaining configurations
by performing the standard gauge transformations _X_ 2 _i,j_ _→_ _X_ 2 _i,j_ + _αi_ ( _X_ 2 _i_ +1 _,j_ _−_ _X_ 2 _i−_ 1 _,j_ ),
for any even index 2 _i_ ; as the gluon amplitude is invariant under these, they will all lead to
the same final result. Similarly, if instead we put _e_ 1 and _e_ 2 next to each other, we would
only have a single subset _ER_ (where _nR_ = _n −_ 2), but the polarization configuration above
would still hold.

We can easily translate Eq. (8.2) into collections of non-adjacent dot products of scalar
momenta _pi · pj_ being set to zero (just like we saw for the action of a single _We_ in Sec. 6).
Using this we can translate condition (8.2) into a statement directly on the dots products
involving the polarizations of the ( _n −_ 2) gluons in _EL_ and _ER_ . We will now do explicitly
this in the four-point example, and use it to compare our operator with the one proposed

in Ref. [46].


9Strictly speaking, we don’t need to make this choice for the first ones we apply in either set, as for
these both gauge invariance statements are unaltered.


                   - 47                   

**8.1** **Four-point** **example**


Let us now go back to the four-point example studied in Sec. 7.2, and read off the polarization configuration corresponding to the action of 2 _W_ ’s. In particular, we’ll consider
_W_ 4[ _W_ 8[ _A_ 4]], which corresponds to case described in Eq. (7.19), and _W_ 6[ _W_ 8[ _A_ 4]], which
corresponds to that of Eq. (7.20).
In both cases, we apply _W_ 8 first, and so we can pick either split factorization, as
for the first one there are no subtleties. Without loss of generality, let’s choose the one
corresponding the map _X_ 8 _,j_ = 1 + _X_ 1 _,j_, which is equivalent to the following locus in terms
of the scalar dot products _pi · pj_ :


2 _p_ 8 _· p_ 1 = 1 _,_ 2 _p_ 8 _· p_ 6 = _−_ 1 _,_ 2 _p_ 8 _· pj_ = 0 _,_ for _j_ _∈{_ 2 _,_ 3 _,_ 4 _,_ 5 _},_ (8.3)


where of course we always have _p_ 8 _· p_ 7 = 0 since this is the same as asking for _q_ 4 [2] [=] [0][.]
Picking _ϵ_ _[µ]_ 4 [=] _[ p]_ 8 _[µ]_ [(which] [is] [consistent] [with] _[α]_ [4] [=] [0][),] [but] [letting] [the] [remaining] [polarizations]
be generic, _i.e._ _ϵ_ _[µ]_ _i_ [=] _[ p]_ 2 _[µ]_ _i_ _[−]_ _[α][i]_ [(] _[p]_ [2] _[i]_ [ +] _[ p]_ [2] _[i][−]_ [1][)] _[µ]_ [,] [we] [obtain]



_ϵ_ 4 _· ϵ_ 1 = _−α_ 1 _/_ 2 _,_

_ϵ_ 4 _· ϵ_ 2 = 0 _,_

_ϵ_ 4 _· ϵ_ 3 = _−_ (1 _−_ _α_ 3) _/_ 2 _,_



_ϵ_ 4 _· q_ 1 = 1 _/_ 2 _,_

_ϵ_ 4 _· q_ 2 = 0 _,_

_ϵ_ 4 _· q_ 3 = _−_ 1 _/_ 2 _._



(8.4)



This is precisely the four-point analog of the locus derived in Eq. (6.8), for the 2 _n_ case.
Now let’s consider the case in which we further act with _W_ 4. In this scenario, we are
allowed to choose either split mapping, as both gauge invariance statements are unaffected
for gluon 2. Let’s say we pick the map _X_ 4 _,j_ = 1 + _X_ 5 _,j_, which at the level of the scalar dot
products corresponds to


2 _p_ 4 _· p_ 5 = 1 _,_ 2 _p_ 4 _· p_ 2 = _−_ 1 _,_ 2 _p_ 4 _· pj_ = 0 _,_ for _j_ _∈{_ 1 _,_ 6 _},_

(8.5)
2 _p_ 4 _·_ ( _p_ 7 + _p_ 8) = 0 _⇔_ 2 _p_ 4 _· p_ 7 = 0 _,_


where in the last constraint we have used the fact that _p_ 4 _· p_ 8 = 0 from the action of _W_ 8.
Therefore, picking _ϵ_ _[µ]_ 2 [=] _[ p]_ 4 _[µ]_ [,] [these] [turn] [into]



_ϵ_ 2 _· ϵ_ 1 = _−_ (1 _−_ _α_ 1) _/_ 2 _,_

_ϵ_ 2 _· ϵ_ 3 = _−α_ 3 _/_ 2 _,_

( _ϵ_ 2 _· ϵ_ 4 = 0) _,_



_ϵ_ 2 _· q_ 1 = _−_ 1 _/_ 2 _,_

_ϵ_ 2 _· q_ 3 = 1 _/_ 2 _,_

_ϵ_ 2 _· q_ 4 = 0 _,_



(8.6)



where we put the constraint _ϵ_ 2 _· ϵ_ 4 = 0 in parenthesis since it was imposed by the action
of _W_ 8, and by the time we act with _W_ 4 the answer no longer depends on _ϵ_ _[µ]_ 4 [.] [Therefore,]
the kinematical locus describing _W_ 4[ _W_ 8[ _A_ 4]] is given by Eq. (8.6), as well as any gaugeequivalent configurations. In this locus, we therefore obtain




       - 1 1
_W_ 4[ _W_ 8[ _A_ 4]] = _X_ 2 _,_ 6 _×_ +
_X_ 1 _,_ 5 _X_ 3 _,_ 7




= _X_ 2 _,_ 6 _× A_ [Tr] 4 [(] _[ϕ]_ [3][)] ( _X_ 1 _,_ 5 _, X_ 3 _,_ 7) _._ (8.7)




- 48 

If, instead of acting with _W_ 4, we had acted with _W_ 6, we would have had to be careful to
use the correct split mapping, which in this case is _X_ 6 _,j_ = 1 _−_ _X_ 5 _,j_ . Translating this into
the scalar dot products yields


2 _p_ 4 _· p_ 5 = 1 _,_ 2 _p_ 5 _·_ ( _p_ 7 + _p_ 8) = _−_ 1 _, ⇔_ 2 _p_ 5 _· p_ 7 = _−_ 1 _,_

(8.8)
2 _p_ 5 _· pj_ = 0 _,_ for _j_ _∈{_ 1 _,_ 2 _,_ 3 _},_


where we have used the fact that _p_ 5 _· p_ 8 = 0, from _W_ 8. Note that if we had chosen the
other split, which imposes similar conditions but now on the dot products involving _p_ 6, we
would have obtained 2 _p_ 6 _·_ ( _p_ 7 + _p_ 8) = 1. Since 2 _p_ 6 _· p_ 8 = _−_ 1 from _W_ 8, this would give us
2 _p_ 6 _· p_ 7 = 2, which precisely agrees with what we found in Sec. 7.2. In any case, let’s stick
to this simpler choice. We can easily translate it into conditions on _ϵ_ _[µ]_ 3 [by] [picking] _[α]_ [3] [=] [1][,]
for which _ϵ_ _[µ]_ 3 [=] _[ −][p]_ 5 _[µ]_ [.] [We] [thus] [find]



_ϵ_ 3 _· ϵ_ 1 = 0 _,_

_ϵ_ 3 _· ϵ_ 2 = _−_ (1 _−_ _α_ 2) _/_ 2 _,_

( _ϵ_ 3 _· ϵ_ 4 = 0) _,_



_ϵ_ 3 _· q_ 1 = 0 _,_

_ϵ_ 3 _· q_ 2 = _−_ 1 _/_ 2 _,_

_ϵ_ 3 _· q_ 4 = 1 _/_ 2 _,_



(8.9)



where, once again, we put the constraint _ϵ_ 3 _· ϵ_ 4 = 0 in parenthesis since it was already
imposed by _W_ 8 provided we set _α_ 3 = 1 in Eq. (8.10). To summarize, for _W_ 6[ _W_ 8[ _A_ 4]], we
derive the following locus



_ϵ_ 4 _· ϵ_ 1 = _−α_ 1 _/_ 2 _,_

_ϵ_ 4 _· ϵ_ 2 = 0 _,_

_ϵ_ 4 _· ϵ_ 3 = 0 _,_



_ϵ_ 4 _· q_ 1 = 1 _/_ 2 _,_

_ϵ_ 4 _· q_ 2 = 0 _,_

_ϵ_ 4 _· q_ 3 = _−_ 1 _/_ 2 _,_



_ϵ_ 3 _· ϵ_ 1 = 0 _,_

_ϵ_ 3 _· ϵ_ 2 = _−_ (1 _−_ _α_ 2) _/_ 2 _,_



_ϵ_ 3 _· q_ 1 = 0 _,_

_ϵ_ 3 _· q_ 2 = _−_ 1 _/_ 2 _,_

_ϵ_ 3 _· q_ 4 = 1 _/_ 2 _,_



(8.10)



which, at the level of the amplitude, gives us




       - 1 1       _W_ 6[ _W_ 8[ _A_ 4]] = _X_ 2 _,_ 4 _×_ _X_ 1 _,_ 5 + _X_ 3 _,_ 7 = _X_ 2 _,_ 4 _× A_ [Tr] 4 [(] _[ϕ]_ [3][)] ( _X_ 1 _,_ 5 _, X_ 3 _,_ 7) _._ (8.11)



**Comparison** **with** **transmutation** **operators** **from** **Ref.** **[46]** At this stage, it is natu
ral to go back to the operator introduced in Ref. [46] (also used in Ref. [41] to derive higher
order soft statements), and ask whether it matches any sequence of actions with the _We_
operators. According to Ref. [46], one should get the Tr( _ϕ_ [3] ) amplitude from the gluon one

by acting with



_T_ [ _a_ 1 _, a_ 2 _, · · ·_ _, an_ ] = _Ta_ 1 _,an_



_n−_ 1

- _Tai−_ 1 _,ai,an,_ (8.12)


_i_ =2



where _{a_ 1 _, a_ 2 _, · · ·_ _, an}_ is the ordered set of labels, and _Ti,j,k_ = _∂qi·ϵj_ _−∂qk·ϵj_ and _Tl,m_ = _∂ϵl·ϵm_ .
From its definition in Eq. (8.12), it is clear that this operator acts on ( _n −_ 2) gluons with
_Tai−_ 1 _,ai,an_, and then kills off the dependence on the remaining two polarizations with _Ta_ 1 _,an_ .
This seems very similar to our case, with the exception that in the operator _T_ [ _a_ 1 _, a_ 2 _, · · ·_ _, an_ ],
the last two polarizations are always associated with two adjacent gluons, _a_ 1 and _an_, while


                   - 49                   

in our case, depending on the set of _We_ ’s we choose to apply, the final two gluons can also
be separated from each other.

Nonetheless, to compare explicitly with Ref. [46], let us consider a case in which the

last two gluons (say gluons 1 and 2) are adjacent to each other at four-points. From our
perspective, this corresponds to applying _W_ 6 and _W_ 8, just like we described previously.
The closest limit to this in Ref. [46] would be to consider the ordered set in (8.12) to be
_{_ 2 _,_ 3 _,_ 4 _,_ 1 _}_, in which case we have


_T_ [ _{_ 2 _,_ 3 _,_ 4 _,_ 1 _}_ ] = _T_ 2 _,_ 1   - _Ti−_ 1 _,i,_ 1 = _∂ϵ_ 1 _·ϵ_ 2 ( _∂q_ 2 _·ϵ_ 3 _−_ _∂q_ 1 _·ϵ_ 3) ( _∂q_ 3 _·ϵ_ 4 _−_ _∂q_ 1 _·ϵ_ 4) _._ (8.13)

_i_ = _{_ 3 _,_ 4 _}_


So, starting with _T_ 3 _,_ 4 _,_ 1 = ( _∂q_ 3 _·ϵ_ 4 _−_ _∂q_ 1 _·ϵ_ 4), as explained in Sec. 6 this operator is picking
a polarization configuration for _ϵ_ _[µ]_ 4 [which] [agrees] [with] [what] [we] [get] [from] [acting] [with] _[W]_ [8][,]
provided we make the gauge choice _α_ 1 = 0 and _α_ 3 = 1; this is so that, in Eq. (8.10), we
ensure that all the dot products _ϵ_ 4 _· ϵi_ = 0. Note that it is convenient to have _α_ 3 = 1, since
this is also the gauge we pick to read off the kinematic locus giving _W_ 6 in Eq. (8.9).
Now, after acting with _W_ 6 and _W_ 8, from Eq. (8.11) we get a prefactor _X_ 2 _,_ 4 times the
four-point Tr( _ϕ_ [3] ) amplitude, and quite remarkably, for the gauge choice _α_ 1 = 0 _, α_ 3 = 1, we
find that _X_ 2 _,_ 4 = _ϵ_ 1 _· ϵ_ 2! This means that we can directly compare the action of _T_ 2 _,_ 3 _,_ 1 _T_ 3 _,_ 4 _,_ 1
with that of _W_ 6 _W_ 8. For this gauge choice, _W_ 8 is equivalent to _T_ 3 _,_ 4 _,_ 1, so let’s now look at
_W_ 6 and _T_ 2 _,_ 3 _,_ 1. From the definition of _T_ 2 _,_ 3 _,_ 1, we see that it is equivalent to the polarization
configuration
_ϵ_ 3 _· ϵi_ = 0 _,_ _ϵ_ 3 _· q_ 1 = _−_ 1 _,_ _ϵ_ 3 _· q_ 2 = 1 _,_ _ϵ_ 3 _· q_ 4 = 0 _._ (8.14)


Comparing with Eq. (8.9), by picking _α_ 2 = 1 we can have _ϵ_ 3 _·_ _ϵi_ = 0, but the conditions
on _ϵ_ 3 _· qi_ from _W_ 6 don’t match those of _T_ 2 _,_ 3 _,_ 1 - they are also not related by any gauge
transformation. Therefore, even though the two operators are closely related, already at

four-points they are not the same.

Another way one can conclude this is by looking at the action of the two operators

directly at the level of the string amplitudes. In Ref. [46], the authors claim that by

starting with the the _n_ -point tree-level gluon bosonic string amplitude [45]



(8.15)





_zi,j_ [2] _[q][i][·][q][j]_ exp
_i<j_
















������linear in all _ϵi_




        _A_ [YM] _n_ (1 _,_ 2 _, . . ., n_ ) =

_D_



d _[n]_ _zi_
SL(2,R)





2 _[ϵ][i][ ·][ ϵ][j]_
_i_ = _j_ _zi,j_ [2]




_[i][ ·][ ϵ][j]_

_−_ _[ϵ][i][ ·][ q][j]_
_zi,j_ [2] _zi,j_
















_zi,j_



with _D_ = _z_ 1 _<_ _z_ 2 _<_ _· · ·_ _<_ _zn_ and _zi,j_ = _zj_ _−_ _zi_, and acting on it with the operator in
Eq. (8.12), one obtains directly the stringy Tr( _ϕ_ [3] ) shown in Eq. (5.18). We can write the
latter integral in terms of the _zi,j_ ’s, reproducing the _Z_ -theory integral [48]





_zi,j_ [2] _[q][i][·][q][j]_ _._ (8.16)
_i<j_




         _A_ [Tr] _n_ [(] _[ϕ]_ [3][)] (1 _,_ 2 _, . . ., n_ ) =

_D_



d _[n]_ _zi_ 1
SL(2,R) _z_ 1 _,_ 2 _z_ 2 _,_ 3 _· · · zn,_ 1



Indeed, already at four-points, by going on the kinematic locus specified by _T_ 2 _,_ 3 _,_ 1 _T_ 3 _,_ 4 _,_ 1


                 - 50                 

we find


         _A_ [YM] _n_ (1 _,_ 2 _, . . ., n_ ) =

_D_


         =

_D_



d _[n]_ _zi_
SL(2,R)


d _[n]_ _zi_
SL(2,R)




- 2 _ϵ_ 1 _· ϵ_ 2

_zi,j_ [2] _[α][′][p][i][·][p][j]_ _z_ 1 _,_ 2 _z_ 2 _,_ 3 _z_ 3 _,_ 4 _z_ 4 _,_ 1 _,_
_i>j_








- 2 _ϵ_ 1 _· ϵ_ 2

_i>j_ _zi,j_ [2] _[α][′][p][i][·][p][j]_ _z_ 1 [2] _,_ 2




- - 1 1
_×_ _−_
_z_ 4 _,_ 1 _z_ 4 _,_ 3







1 _· ϵ_ 2 - 1 1

_×_ _−_
_z_ 1 [2] _,_ 2 _z_ 3 _,_ 1 _z_ 3 _,_ 2



(8.17)
which is precisely stringy Tr( _ϕ_ [3] ). If instead we apply the polarization configuration corresponding to _W_ 6 _W_ 8 (with _α_ 1 = 0 _, α_ 3 = 1 _, α_ 2 = 1) we arrive at




- 2 _ϵ_ 1 _· ϵ_ 2

_zi,j_ [2] _[α][′][p][i][·][p][j]_ _z_ 1 _,_ 2 _z_ 2 _,_ 3 _z_ 3 _,_ 4 _z_ 4 _,_ 1 _×_ _[z]_ _z_ [2] 4 _[,]_ _,_ [4] 3 _[z]_ _z_ [1] 1 _[,]_ _,_ [3] 2
_i>j_




- - 1 1
_×_ _−_
_z_ 4 _,_ 3 _z_ 4 _,_ 1







d _[n]_ _zi_
SL(2,R)


d _[n]_ _zi_
SL(2,R)




- 2 _ϵ_ 1 _· ϵ_ 2

_i>j_ _zi,j_ [2] _[α][′][p][i][·][p][j]_ _z_ 1 [2] _,_ 2



_A_ [YM] _n_ (1 _,_ 2 _, . . ., n_ ) = [1] 4







1 _· ϵ_ 2 - 1 1

_×_ _−_
_z_ 1 [2] _,_ 2 _z_ 3 _,_ 2 _z_ 3 _,_ 4



= [1]

4






_D_




_D_







_,_
_z_ 4 _,_ 3 _z_ 1 _,_ 2



(8.18)

which is manifestly different than Eq. (8.17). In addition, recalling that we can write the
_ui,j_ in terms of the _zi,j_ as _ui,j_ = _zi,j−_ 1 _zi−_ 1 _,j/_ ( _zi,jzi−_ 1 _,j−_ 1), we can recognize the extra factor
to be 1 _/u_ 1 _,_ 3, which precisely agrees with what we found at the level of the integral in
Eq. (8.17)!


**9** **Transmutation** **at** **One-Loop**


Having understood the action of _We_ on tree-level gluon amplitudes, it is natural to ask how
this extends to one-loop. Recall that, in Eq. (5.16), we took _We_ to be a sum of derivatives
of _An_ with respect to all _X_ variables depending on the index _e_ . In this way, the resulting
object was independent of _e_ . Thus, the simplest way to generalize to loop-level is to define
_We_ [(] _[l]_ [)] in exactly the same way:



_We_ [(] _[l]_ [)] = 

_j_ = _e_



_∂_  +
_∂Xe,j_

_j_ = _e_



_∂_ _∂_
+ _,_ (9.1)
_∂Xj,e_ _∂Xe,p_



where we are dealing with surface kinematics, and so _Xe,j_ = _Xj,e_ .
Using the explicit expressions for the residues _R_ 2 _n−_ 3 _,_ 1 and _R_ 2 _n−_ 1 _,_ 3, one can show that
we precisely recover the lower-point integrands by acting with this operator:



_We_ [(] _[l]_ [)][[] _[I][n]_ [] =] _[I][n][−]_ [1][(1] _[,]_ [ 2] _[, . . .,]_ [ 2] _[n][ −]_ [2)]




_[,]_ [ 2] _[, . . .,]_ [ 2] _[n][ −]_ [2)]

+ _[I][n][−]_ [1][(2] _[n][ −]_ [1] _[,]_ [ 2] _[, . . .,]_ [ 2] _[n][ −]_ [2)]
_X_ 2 _n−_ 3 _,_ 1 _X_ 2 _n−_ 1 _,_ 3



+ _· · ·_ _,_ (9.2)
_X_ 2 _n−_ 1 _,_ 3



where the ellipses contain the remaining terms with poles in neither _X_ 2 _n−_ 3 _,_ 1 nor _X_ 2 _n−_ 1 _,_ 3.
This formula is strikingly similar to that found in Eq. (5.17) for the tree-level case. As a
result, we may hope that, using our simple generalization _We_ [(] _[l]_ [)][,] [we] [can] [transmutate] [gluons]
into scalars not only at tree-level but also at loop-integrand-level.

Note that, in the first appearance of transmutation operators, the authors introduce
_Ti,j,k_ (which is equivalent to _We_ ) as an operator that _preserves_ tree-level gauge invari

                   - 51                   

ance [46]. Since gauge invariance only holds post-loop integration, it is hard to see how,

in the standard language, such an operator might also exist for the one-loop integrand.

However, once again working in surface kinematics, we find that the simplest, most natural
generalization of _We_ given in Eq. (9.1) precisely gives us what we want!
Let us start by consider the simplest case, the one-point integrand given in Eq. (2.14).
Applying to it the operator _W_ 2 [(] _[l]_ [)][,] [one] [can] [check] [simply] [that]



_∂I_ 1
_W_ 2 [(] _[l]_ [)][[] _[I]_ [1][] =] + _[∂][I]_ [1]
_∂X_ 1 _,_ 2 _∂X_ 2




_[∂][I]_ [1] = [1] _[ −]_ [∆]

_∂X_ 2 _,p_ _X_ 1 _,p_




_[∂][I]_ [1] + _[∂][I]_ [1]

_∂X_ 2 _,_ 1 _∂X_ 2



_._ (9.3)
_X_ 1 _,p_



As anticipated, this is exactly the one-point integrand in Tr( _ϕ_ [3] ) theory multiplied by 1 _−_ ∆=
_d_ . Note that, already in this simplest case, it is crucial to keep the boundary curves _X_ 1 _,_ 2
and _X_ 2 _,_ 1, as otherwise, we would not get the Tr( _ϕ_ [3] ) integrand. So, once more we see
clearly that surface kinematics plays a fundamental role in allowing us to extend tree-level

statements to loop integrands.
We can go one step further, and see what happens when we apply _W_ 2 [(] _[l]_ [)] and _W_ 4 [(] _[l]_ [)]
sequentially to the two-point integrand shown in Eq. (2.15). This gives us


_d_ _d_ _d_
_W_ 2 [(] _[l]_ [)][[] _[W]_ 4 [(] _[l]_ [)][[] _[I]_ [2][]] =] _[ W]_ 4 [(] _[l]_ [)][[] _[W]_ 2 [(] _[l]_ [)][[] _[I]_ [2][]] =] + + _,_ (9.4)
_X_ 1 _,pX_ 3 _,p_ _X_ 1 _,pX_ 1 _,_ 1 _X_ 3 _,pX_ 3 _,_ 3


where, again, we find the integrand for Tr( _ϕ_ [3] ) theory times _d_, the dimension of spacetime.

We have checked that this behavior continues up to five-points, and therefore we make the
conjecture that applying all _n_ _We_ [(] _[l]_ [)] operators to _In_ always returns the _n_ -point integrand
in Tr( _ϕ_ [3] ) theory multiplied by _d_ . We suspect that, with an argument similar to the one

presented at tree-level ( _i.e._, using splits of the one-loop surface integral), one should be

able to prove the result above, but we leave it to future work. For other instances of

transmutation at one-loop, see Refs. [49–51].

Finally, let us end by making some remarks on the generalization of transmutation

operators to higher loops. As it turns out, already at two-loops it is clear that the naive

extension doesn’t hold purely by a units argument. At _l_ -loops, the integrand has units of
_X_ [2] _[−]_ [2] _[l]_, and so at two-loops it has units of _X_ _[−]_ [2] . Already in the simplest case of _n_ = 1 _, l_ = 2,
the part of the integrand that has all the Tr( _ϕ_ [3] ) singularities has five _X_ ’s in the denominator
and three in the numerator. So, to hope to turn the gluon integrand into a Tr( _ϕ_ [3] ) one,

we would need to act with at least three differential operators. However, since we are at

one-point, we only have a single even index _e_ = 2. For this reason, it is not obvious how
or if any sort of transmutation holds for _l_ _≥_ 2. On the other hand, the form of the _We_
operators were suggested by gauge invariance, and the statement of gauge invariance at

higher loops has not yet been fully fleshed out. So, it is conceivable that understanding

this could offer a way out of the units dilemma.


                   - 52                   

**10** **Outlook**


The scalar-scaffolded formalism offers us a new window into the study of gluon amplitudes.

In this paper, we leveraged the advantages of this representation - the trivialization of

on-shell kinematics using scalar _X_ variables, a locked form for the amplitude, and the use

of surface kinematics to give a well-defined surface integrand at loop-level - to explore

two aspects of gluon amplitudes, tied together by their close relationship to the scaffolding

representation of surface gauge invariance.

In Part I, we used the scalar variables to give a precise kinematical definition for the

soft limit, as a well-defined Laurent expansion in a set of soft factors. At tree-level, we

derived universal leading and subleading terms in the soft expansion, which followed directly

from the combination of factorization on the collinear poles adjacent to the soft gluon and

the requirement of gauge invariance. A general feature of the scaffolding formalism is

that the terms in the amplitude Laurent expansion are well-defined but not individually

gauge invariant, so gauge invariance can link different terms in the expansion. This led us

to propose a simple “gauge-invariantifying” operation that produced gauge-invariant soft

terms at both leading and subleading levels. At one-loop, working in the expanded surface
kinematics basis gave us a clear way to generalize our tree-level soft limit and apply it to the

YM surface integrand. The use of surface kinematics makes it possible to define a canonical

Yang-Mills integrand, enjoying both gauge invariance as well as correct cuts. These two

properties led to well-defined soft factors at the level of the surface loop integrand. We

obtained a universal leading term in the one-loop soft expansion, which has the expected
Weinberg factor plus specific corrections proportional to the tadpole variable _Xs,s_ ; of course,
these corrections vanish upon loop integration. It is striking to find a well-defined soft term

at integrand level, whose existence is made possible only by the use of surface kinematics.
In Part II, we switched gears and investigated a differential operator _We_ acting on
external gluon labels, suggested naturally from the requirements of gauge invariance. After

taking some hints about its structure from the soft expansion in Part I, we demonstrated

that the action of this operator is equivalent to imposing some of the simplest “split” kine
matic configurations on the amplitude. Working at the level of the full surface integral,

we used these split kinematics to find the surface integral that results from applying any
number of _We_ operators. In particular, after applying ( _n −_ 2) of them in any order, we
obtained a class of “shifted” integrals, which remarkably reduce to Tr( _ϕ_ [3] ) amplitudes at low
energies! For a single operation, our _We_ turns out to correspond precisely to the insertion
operator _Ti,j,k_ discussed in Ref. [46], whereas, for multiple applications, differences appear.
We then showed that, using surface kinematics, the _We_ operator can be generalized to the
one-loop integrand. We conjectured (and verified up to _n_ = 5 points) that applying the
_We_ to all _n_ gluons of the YM integrand returns the Tr( _ϕ_ [3] ) integrand. We suspect that
this statement can be proven by an extension of our tree-level split kinematics argument to

loop-level.

We close by briefly discussing a set of possible next steps suggested by our investiga
tions.

When we defined the soft limit in Part I, we chose a certain “minimal” limit, where we


                   - 53                   

changed only the momenta of the soft gluon and its two adjacent gluons. We also ensured

that the on-shell conditions of all gluons remained true during the limit, while momentum

conservation was handled _ipso_ _facto_ by the dual variables of the momentum polygon. In

this limit, we derived a universal subleading soft theorem. It would be interesting to

investigate the relationship between this subleading soft theorem and the ones that have

been intensively studied in the literature on celestial holography over the past decade .

In particular, while our “minimal” soft limit can be realized for general polarizations in
high enough ( _d_ _≥_ 6) spacetime dimensions, it cannot be realized for all helicities in _d_ = 4

dimensions. It is obvious that a “less minimal” soft limit, where more _X_ ’s are varied, can

be defined in any number of dimensions, and it would be interesting to compute subleading

theorems for these extended soft limits.
As we discussed in Part II, the transmutation operator _We_ applied to the full surface
integral has a beautiful interpretation from the perspective of split kinematics: it returns

the surface integral for the surface with marked point _e_ removed (7.8). One might therefore
hope that _We_ [ _An_ ] has some interpretation as an “amplitude” itself, where one (or a few)
gluons are turned into scalars. Indeed, at field-theory level, we see from Eq. (5.17) that
_We_ [ _An_ ] factorizes on the poles _X_ 1 _,_ 2 _n−_ 3 and _X_ 3 _,_ 2 _n−_ 1 as on a scalar exchange, giving some
possible hints at its structure. Could there be some diagrammatic way to understand the

field theory limit of the surface integral (7.8)? Even if not an amplitude, is there a set of

rules that determines its structure in _X_ language?

It would be even more fascinating to find an algorithmic way to build YM theory from
Tr( _ϕ_ [3] ) theory directly at field-theory level, where one would hope to obtain a prescription
to “undo” each _We_ operation. Since transmutation also exists at one-loop, one could hope
to do this for both the tree amplitude and the one-loop integrand. Of course, to find

such a procedure for the integrand, we would likely first need to understand the proof of

transmutation at one-loop; in particular, is there a surface integral similar to Eq. (7.8) for
the punctured disk after applying _We_ [(] _[l]_ [)][?] [And] [finally,] [as] [noted] [in] [Sec.] [9][,] [it] [it] [natural] [to]
seek out a transmutation operator valid for more than one-loop - a challenge we can only

sensibly undertake after finding a systematic understanding of surface gauge invariance at

all loop orders.


**Acknowledgments**


The authors thank Nima Arkani-Hamed, Clifford Cheung, Jin Dong and Alfredo Guevara

for useful discussions. J.B. is supported by the NSF Graduate Research Fellowship under

Grant No. KB0013612. C.F. is supported by FCT - Fundacao para a Ciencia e Tecnologia,

I.P. (2023.01221.BD and DOI https://doi.org/10.54499/2023.01221.BD)


**A** **Higher** **Orders** **in** **the** **Tree-Level** **Soft** **Expansion**


In this Appendix, we will finish the discussion started in Sec. 3.1; namely, we will derive

the subleading term in the soft expansion and see what constraints we can place at sub
subleading and higher.


                   - 54                   

To do this, we will start with the residue in _X_ 1 _,_ 2 _n−_ 3, which, as discussed in the main
text, takes the form




  
( _Xj,J_ _−_ _X_ 1 _,j_ _−_ _X_ 2 _n−_ 3 _,J_ ) _[∂M][L]_

_∂Xj,x_

_j∈L,_ _J∈{_ 2 _n−_ 2 _,_ 2 _n−_ 1 _,_ 2 _n}_




   _R_ 1 _,_ 2 _n−_ 3 =




_[∂M][L]_ _×_ _[∂M][R]_

_∂Xj,xL_ _∂XJ,x_



_,_ (A.1)
_∂XJ,xR_



where _L_ = _{_ 2 _,_ 3 _, . . .,_ 2 _n−_ 4 _}_, _ML_ _≡_ _ML_ (1 _,_ 2 _, . . .,_ 2 _n−_ 4 _,_ 2 _n−_ 3 _, xL_ ), which is an ( _n−_ 1)-point
amplitude, and _MR_ _≡_ _MR_ (1 _, xR,_ 2 _n −_ 3 _,_ 2 _n −_ 2 _,_ 2 _n −_ 1 _,_ 2 _n_ ), which is a 3-point amplitude.
Using the explicit form of 3-point amplitude for _MR_, as given in Eq. (2.6), we can write
out each term in the _J_ -sum above as follows:


     - _∂ML_
_J_ = 2 _n −_ 2 : _X_ 2 _n−_ 3 _,_ 2 _n ×_ ( _Xj,_ 2 _n−_ 2 _−_ _X_ 1 _,j_ ) _,_

_∂Xj,_ 2 _n−_ 2
_j_



(A.2)




 ) _×_



_J_ = 2 _n −_ 1 : ( _X_ 2 _n−_ 2 _,_ 2 _n −_ _X_ 2 _n−_ 3 _,_ 2 _n −_ _X_ 1 _,_ 2 _n−_ 2


_δ_ 2 [(1)] _n−_ 2



_δj_ [(2] _[n][−]_ [1)] _−δj_ [(1)]



( _Xj,_ 2 _n−_ 1 _−_ _X_ 1 _,j_ )
_j_ [(2] _[n][−]_ [1)] [(1)]



_∂ML_
_,_
_∂Xj,_ 2 _n−_ 2



_∂ML_
_−X_ 2 _n−_ 3 _,_ 2 _n_ ) _,_
_∂Xj,_ 2 _n−_ 2



_J_ = 2 _n_ : _X_ 1 _,_ 2 _n−_ 2


_δ_ 2 [(1)] _n−_ 2



_×_ 


( _Xj,_ 2 _n −_ _X_ 1 _,j_
_j_ [(1)]



_δj_ [(1)] + _Xs,j_



where we have relabeled _xL_ = 2 _n_ _−_ 2, and under brackets we show the soft map for the _X_ ’s
on the prefactors.
Let us look at each of these contributions one-by-one. Using gauge invariance of _ML_
in gluon _n −_ 1, the _J_ = 2 _n −_ 2 contribution becomes





( _Xj,_ 2 _n−_ 2 _−_ _X_ 1 _,j_ ) _[∂M][L]_

_∂Xj,x_

_j∈L_




  _X_ 2 _n−_ 3 _,_ 2 _n ×_



= _X_ 2 _n−_ 3 _,_ 2 _n × ML_ (1 _,_ 2 _, . . .,_ 2 _n −_ 2) _._ (A.3)
_∂Xj,xL_



Of course, this is exactly the term that gave us half of the leading Weinberg term in the

main text. However, if we want to look at higher orders, we have to take into account that
_ML_ depends on the soft factors, via _X_ 1 _,j_ = _Xs,j_ + _δj_ [(1)][.] [Taylor] [expanding] _[M][L]_ [yields:]



_An−_ 1

+ [1]
_∂Xs,i_ 2



_ML_ (1 _,_ 2 _, . . .,_ 2 _n −_ 2) = _An−_ 1 +



2 _n−_ 4





- _∂An−_ 1

_δi_ [(1)] _∂Xs,i_
_i_ =4



2




- _∂_ [2] _An−_ 1

_δi_ [(1)] _δk_ [(1)] _∂Xs,i∂Xs,k_ + _· · ·_ _,_ (A.4)
_i,k_



with _An−_ 1 _≡An−_ 1( _s,_ 2 _,_ 3 _, · · ·_ _,_ 2 _n −_ 2). This then gives the all-order soft expansion of the
_J_ = 2 _n −_ 2 contribution. Quite nicely, the _J_ = 2 _n −_ 1 and _J_ = 2 _n_ terms are already
organized as expansions in soft factors, so all we must do is plug in the expansion of _ML_ .
In summary, using the residue formula together with the expansion of _ML_, we can derive
the all-order soft expansion of the pole in _X_ 1 _,_ 2 _n−_ 3. In particular, at subleading order _O_ ( _δ_ ),


                   - 55                   

we find:


_R_ 1 [(1)] _,_ 2 _n−_ 3 [:] _[ X]_ [2] _[n][−]_ [3] _[,]_ [2] _[n]_




- _∂An−_ 1

_δi_ [(1)] _∂Xi,s_
_i_ =4



2 _n−_ 4




+ ( _X_ 2 _n−_ 2 _,_ 2 _n −_ _X_ 2 _n−_ 3 _,_ 2 _n_ )
_∂Xi,s_



2 _n−_ 4






( _δj_ [(2] _[n][−]_ [1)] _−_ _δj_ [(1)][)] _[∂][A][n][−]_ [1]

_∂Xj,_ 2 _n−_

_j_ =2



_∂Xj,_ 2 _n−_ 2



_._
_∂Xj,_ 2 _n−_ 2



+ _δ_ 2 [(1)] _n−_ 2



2 _n−_ 4






( _Xj,_ 2 _n −_ _Xs,j_ _−_ _X_ 2 _n−_ 3 _,_ 2 _n_ ) _[∂][A][n][−]_ [1]

_∂Xj,_ 2 _n−_

_j_ =2



(A.5)
We can repeat this analysis for the other residue _R_ 3 _,_ 2 _n−_ 1, where now the two lower-point
amplitudes that enter the factorization formula




 
( _Xj,J_ _−_ _X_ 2 _n−_ 1 _,j_ _−_ _X_ 3 _,J_ ) _[∂A][L]_

_∂XJ,x_

_j∈R,_ _J∈{_ 2 _,_ 1 _,_ 2 _n}_




   _R_ 3 _,_ 2 _n−_ 1 =



_∂AR_

_[∂A][L]_ _×_ (A.6)

_∂XJ,xL_ _∂Xj,xR_



are _AL_ _≡_ _AL_ (1 _,_ 2 _,_ 3 _, xL,_ 2 _n −_ 1 _,_ 2 _n_ ), and _AR_ _≡_ _AR_ (2 _n −_ 1 _, xR,_ 3 _,_ 4 _, . . .,_ 2 _n −_ 2), which are,
respectively, a 3- and an ( _n −_ 1)-point amplitudes; and _R_ = _{_ 4 _,_ 5 _, . . .,_ 2 _n −_ 2 _}_ . Using again

the explicit form of the 3-point amplitude given in Eq. (2.6), the different terms in the

_J_ -sum take values



( _X_ 2 _,j_ _−_ _Xj,_ 2 _n−_ 1) _[∂A][R]_

_∂Xj,_

_j_




   _J_ = 2 : _X_ 3 _,_ 2 _n ×_



_,_
_∂Xj,_ 2



_∂AR_
_,_
_∂Xj,_ 2



(A.7)



_J_ = 1 : ( _X_ 2 _,_ 2 _n −_ _X_ 3 _,_ 2 _n −_ _X_ 2 _,_ 2 _n−_ 1

_δ_ 2 [(2] _[n][−]_ [1)]




 ) _×_



( _X_ 1 _,j_ _−_ _Xj,_ 2 _n−_ 1)
_j_ [(1)] [(2] _[n][−]_ [1)]



_δj_ [(1)] _−δj_ [(2] _[n][−]_ [1)]



_J_ = 2 _n_ : _X_ 2 _,_ 2 _n−_ 1


_δ_ 2 [(2] _[n][−]_ [1)]



_×_ 


( _Xj,_ 2 _n −_ _Xj,_ 2 _n−_ 1
_j_ [(2] _[n][−]_



_Xj,s_ + _δj_ [(2] _[n][−]_ [1)]



_−X_ 3 _,_ 2 _n_ ) _[∂A][R]_ _,_

_∂Xj,_ 2



where now we have relabeled _xR_ = 2. As before, we can use the gauge invariance of _AR_ to
rewrite the _J_ = 2 contribution as



( _X_ 2 _,j_ _−_ _Xj,_ 2 _n−_ 1) _[∂A][R]_

_∂Xj,_

_j_




 _X_ 3 _,_ 2 _n ×_



= _X_ 3 _,_ 2 _n × AR_ (2 _n −_ 1 _,_ 2 _, . . .,_ 2 _n −_ 2) _,_ (A.8)
_∂Xj,_ 2



where now _AR_ depends on the soft factors via _Xj,_ 2 _n−_ 1 = _Xj,s_ + _δj_ [(2] _[n][−]_ [1)] . Taylor expanding
_AR_ in the soft factors we obtain



+ _· · ·_ _._ (A.9)
_∂Xi,s_



_AR_ (2 _n −_ 1 _,_ 2 _, . . .,_ 2 _n −_ 2) = _An−_ 1 +



2 _n−_ 4





- _∂An−_ 1

_δi_ [(2] _[n][−]_ [1)] _∂Xi,s_
_i_ =4



Of course, as with _R_ 1 _,_ 2 _n−_ 3, this nails all orders in the soft expansion of _R_ 3 _,_ 2 _n−_ 1; in particular,


                   - 56                   

the term at subleading order takes the form



+ ( _X_ 2 _,_ 2 _n −_ _X_ 3 _,_ 2 _n_ )
_∂Xi,s_



(A.10)



_R_ 3 [(1)] _,_ 2 _n−_ 1 [:] _[ X]_ [3] _[,]_ [2] _[n]_



2 _n−_ 4





- _∂An−_ 1

_δi_ [(2] _[n][−]_ [1)] _∂Xi,s_
_i_ =4



2 _n−_ 2






( _δj_ [(1)] _−_ _δj_ [(2] _[n][−]_ [1)] ) _[∂]_ _∂X_ _[A][n]_ _j,_ _[−]_ 2 [1]
_j_ =4



_∂Xj,_ 2



_._
_∂Xj,_ 2



+ _δ_ 2 [(2] _[n][−]_ [1)]



2 _n−_ 2






( _Xj,_ 2 _n −_ _Xj,s −_ _X_ 3 _,_ 2 _n_ ) _[∂][A][n][−]_ [1]

_∂Xj,_ 2

_j_ =4



To fully understand the subleading term in the soft expansion of the amplitude, we also
need control over the soft expansion of _R_ in Eq. (3.15). As alluded to in the main text, we
can use the constraint coming from gauge invariance in the _n_ [th] gluon (3.20) to determine
the leading-order piece of _R_ .

Let us start by rewriting Eq. (3.21), but now making manifest the different terms on

the _l.h.s._ :




_[∂R]_ [1] _[,]_ [2] _[n][−]_ [3] _−_ _[∂R]_ [3] _[,]_ [2] _[n][−]_ [1]

_∂X_ 2 _n−_ 3 _,_ 2 _n_ _∂X_ 3 _,_ 2 _n_



_._ (A.11)
_∂X_ 3 _,_ 2 _n_



2 _n−_ 4






( _δj_ [(2] _[n][−]_ [1)] _−_ _δj_ [(1)][)] _[C][j]_ [=] _[∂R]_ [1] _[,]_ [2] _[n][−]_ [3]

_∂X_ 2 _n−_ 3 _,_ 2

_j_ =4



3


_δk_ [(2] _[n][−]_ [1)] _Ck −_
_k_ =2



2 _n−_ 2

 
_δk_ [(1)] _[C][k]_ [ +]
_k_ =2 _n−_ 3



2 _n−_ 2




Now, using Eqs. (A.2) and (A.7), we can easily extract the derivatives of _R_ 1 _,_ 2 _n−_ 3 and
_R_ 3 _,_ 2 _n−_ 1, and write the difference entering on the _r.h.s._ in terms of lower-point amplitudes
_ML_ (1 _,_ 2 _, . . .,_ 2 _n −_ 2) and _AR_ (2 _n −_ 1 _,_ 2 _, . . .,_ 2 _n −_ 2):



2 _n−_ 2

- _∂AR_

_δk_ [(1)] _∂X_ 2 _,k_
_k_ =2 _n−_ 3



_∂R_ 1 _,_ 2 _n−_ 3

_−_ _[∂R]_ [3] _[,]_ [2] _[n][−]_ [1] = _ML −_ _AR −_
_∂X_ 2 _n−_ 3 _,_ 2 _n_ _∂X_ 3 _,_ 2 _n_



3

- _∂ML_

_δk_ [(2] _[n][−]_ [1)] _∂Xk,_ 2 _n−_ 2 +
_k_ =2








_−_



2 _n−_ 4



_i_ =4




- - [�] _∂ML_
_δi_ [(2] _[n][−]_ [1)] _−_ _δi_ [(1)] _∂Xi,_ 2 _n−_ 2 + _∂X_ _[∂A]_ 2 _[R]_ _,i_



(A.12)



2 _n−_ 2



_j_ =4



_∂AR_
_._
_∂X_ 2 _,j_




_−_ _δ_ 2 [(1)] _n−_ 2



2 _n−_ 4



_j_ =2



_∂ML_
_∂Xj,_ 2 _n−_ 2 + _δ_ 2 [(2] _[n][−]_ [1)]



Expanding _ML_ and _AR_ in soft factors, we see that the difference ( _ML −_ _AR_ ) starts at linear
order as




_[n]_ [1]

+ _O_ ( _δ_ [2] ) _._ (A.13)
_∂Xi,s_



_ML −_ _AR_ =



2 _n−_ 4






( _δi_ [(1)] _−_ _δi_ [(2] _[n][−]_ [1)] ) _[∂]_ _∂X_ _[A][n]_ _i,s_ _[−]_ [1]
_i_ =4



So, plugging everything into Eq. (A.12), we can read off the leading _O_ ( _δ_ [0] ) part of each _Cj_ :



_Cj_ [(0)] = _−_ _[∂][A][n][−]_ [1]




_[A][n][−]_ [1] _∂An−_ 1

_−_ _−_ _[∂][A][n][−]_ [1]
_∂Xs,j_ _∂Xj,_ 2 _n−_ 2 _∂X_ 2 _,j_



_,_ _j_ = 4 _,_ 5 _, . . .,_ 2 _n −_ 4 _,_
_∂X_ 2 _,j_



_C_ 2 [(0)] _n−_ 3 [=] _[ −]_ _[∂][A][n][−]_ [1] _,_

_∂X_ 2 _,_ 2 _n−_ 3



_C_ 2 [(0)] =



2 _n−_ 3



_k_ =4



_∂An−_ 1

_,_
_∂X_ 2 _,k_



(A.14)



2 _n−_ 4



_j_ =3



_∂An−_ 1
_._
_∂Xj,_ 2 _n−_ 2



_C_ 3 [(0)] = _−_ _∂X_ _[∂][A]_ 3 _,_ _[n]_ 2 _[−]_ _n−_ [1] 2 _,_



_C_ 2 [(0)] _n−_ 2 [=]




- 57 

Finally, since at leading order in the soft factors we have _∂X_ 2 _n−_ 3 _,_ 2 _nR_ 1 _,_ 2 _n−_ 3 _, ∂X_ 3 _,_ 2 _nR_ 3 _,_ 2 _n−_ 1 _→_
_An−_ 1, we can use Eqs. (3.18) and (3.19) to write the first two terms in the soft expansion
as







_An_ _→_




_X_ 2 _n−_ 3 _,_ 2 _n_



2 _n−_ 3 _,_ 2 _n_

+ _[X]_ [3] _[,]_ [2] _[n]_
_δ_ 2 [(1)] _n−_ 3 _δ_ 3 [(2] _[n][−]_



_δ_ 3 [(2] _[n][−]_ [1)]



_R_ 1 [(1)] _,_ 2 _n−_ 3 _R_ 3 [(1)] _,_ 2 _n−_ 1
_−An−_ 1 + + +
_δ_ 2 [(1)] _n−_ 3 _δ_ 3 [(2] _[n][−]_ [1)]



2 _n−_ 2


( _Xj,_ 2 _n −_ _Xs,j_ ) _Cj_ [(0)]
_j_ =2



+ _O_ ( _δ_ ) _._



_An−_ 1



Leading, _S_ _[−]_ [1]



Sub-leading, _S_ [0]



Now, just like at leading order it is possible to gauge-invariantify the subleading term
in the _n_ [th] gluon. To do this, let us first note that, by gauge-invariantifying the leading
term, we have subsumed into it the subleading factor of _−An−_ 1. So, to continue with our
gauge-invariantifying, we will treat this factor as part of the leading term and focus our
attention only on _S_ ~~0~~ _≡S_ 0 + _An−_ 1.
~~0~~ ~~0~~ ~~0~~
Remarkably, we find that the subleading term _S_, also satisfies, _G_ 2 _n,_ 1[ _S_ ] = _G_ 2 _n,_ 2 _n−_ 1[ _S_ ],
concretely we have that



~~0~~ ~~0~~ _G_ 1 _,_ 2 _n−_ 3
_G_ 2 _n,_ 1[ _S_ ] = _G_ 2 _n,_ 2 _n−_ 1[ _S_ ] =



1 _,_ 2 _n−_ 3

+ _[G]_ [3] _[,]_ [2] _[n][−]_ [1]
_δ_ 2 [(1)] _n−_ 3 _δ_ 3 [(2] _[n][−]_ [1)]



+ _G_ 0 _,_ (A.15)
_δ_ 3 [(2] _[n][−]_ [1)]



where one can work out


_G_ 1 _,_ 2 _n−_ 3 = _−δ_ 2 [(1)] _n−_ 2



2 _n−_ 4

- _∂An−_ 1

_δj_ [(2] _[n][−]_ [1)] _∂Xj,_ 2 _n−_ 2 _,_
_j_ =2



_,_
_∂X_ 2 _,j_



(A.16)



_G_ 3 _,_ 2 _n−_ 1 = _−δ_ 2 [(2] _[n][−]_ [1)]



2 _n−_ 2





- _∂An−_ 1

_δj_ [(1)] _∂X_ 2 _,j_
_j_ =4



+
_∂X_ 2 _,j_



_G_ 0 =



2 _n−_ 2





- _∂An−_ 1

_δj_ [(1)] _∂X_ 2 _,j_
_j_ =4



2 _n−_ 4

- _∂An−_ 1

_δj_ [(2] _[n][−]_ [1)] _∂Xj,_ 2 _n−_ 2 _._
_j_ =2



0 ~~0~~
Since we find that _G_ 2 _n,_ 1[ _S_ ] = _G_ 2 _n,_ 2 _n−_ 1[ _S_ ], we can then use the same simple trick (4.11)
we used at leading order to gauge-invariantify the subleading soft term in gluon _n_, which
~~0~~ 0
is then simply _S_ + _G_ 2 _n,_ 1[ _S_ ].
Let us conclude this appendix with some remarks about what happens at higher orders
in the soft expansion. Of course, since we have formulae for the residues _R_ 1 _,_ 2 _n−_ 3 and
_R_ 3 _,_ 2 _n−_ 1 we can continue to write their soft expansions indefinitely. But, the only constraint
we have for the rest of the amplitude comes from Eq. (3.21), which can only be used to
write down the leading part of the _Cj_ in the soft expansion. However, we can ask if there
is _anything_ interesting that can be said about the behavior of the higher-order terms in the
_Cj_ expansion using just Eq. (3.21). Indeed, one can see a hint of some structure by noticing
that, if one sums the terms in Eq. (A.14), many terms cancel, and the result is



2 _n−_ 2


_Cj_ [(0)] =
_j_ =2



2 _n−_ 4



_j_ =4



_∂An−_ 1

_._ (A.17)
_∂Xj,s_




- 58 

It turns out that this behavior continues to all orders in the soft expansion. To state it
most succinctly, let us consider the soft limit where we take _x_ _[µ]_ _s_ [=] _[x][µ]_ 1 [.] [In] [this] [case,] [our]
two sets of soft factors _δj_ [(1)] _[, δ]_ _j_ [(2] _[n][−]_ [1)] become degenerate, and we thus only have one set
_δj_ = _Xj,_ 2 _n−_ 1 _−_ _X_ 1 _,j_ to deal with. Let us consider _C_ = [�] _j_ _[C][j]_ [as] [an] [expansion] [in] [these]
parameters:



_C_ = _C_ 0 +



2 _n−_ 2





- _Ciδi_ + [1]

2!

_i_ =2



2!



2 _n−_ 2

- _Ci,jδiδj_ + _· · ·_ _._ (A.18)


_i,j_ =2



One can then work out easily from Eq. (3.21) that the property in Eq. (A.17) continues to

all orders in the above expansion:



2 _n−_ 2





- _Ci_ = [1]

2

_i_ =2



_∂A_ [(1)] _n−_ 1
_,_
_∂X_ 1 _,j_



_C_ 0 =



2 _n−_ 4



_j_ =4


2 _n−_ 2




_∂A_ [(1)] _n−_ 1
_,_
_∂X_ 1 _,j_



2



2 _n−_ 4



_i,j_ =4



_∂A_ [(1)] _n−_ 1
_∂X_ 1 _,i_



_∂A_ [(1)] _n−_ 1
_∂X_ 1 _,j_



_∂A_ [(1)] _n−_ 1
_,_ _. . ._
_∂X_ 1 _,k_



(A.19)




- _Ci,j_ = [1]

3

_i,j_ =2



3



2 _n−_ 4



_i,j,k_ =4



_∂A_ [(1)] _n−_ 1
_∂X_ 1 _,i_



where _A_ [(1)] _n−_ 1 [=] _[ A][n][−]_ [1][(1] _[,]_ [ 2] _[, . . .,]_ [ 2] _[n]_ _[−]_ [2)][.] [The object] _[ C]_ [, though not appearing in the amplitude]
itself, is interesting in its own right, since it precisely agrees with the piece of _W_ 2 _n_ [ _An_ ] that
has no poles in _X_ 1 _,_ 2 _n−_ 3 and _X_ 3 _,_ 2 _n−_ 1. (See Eq. (5.17).) In the main text, we observed that
the numerators of those poles simply gave lower-point amplitudes under the action of _W_ 2 _n_,
and now, after a bit more work, we find that the remainder also behaves nicely — satisfying

the interesting sum rules described above.


**B** **Higher** **Orders** **in** **the** **One-Loop** **Soft** **Expansion**


In this Appendix, we discuss the specifics of the soft expansion of the one-loop integrand.
Let us begin by analyzing the residue in _X_ 2 _n−_ 1 _,_ 3. Using Eq. (2.13), this corresponds
to _i_ = 2 _n −_ 1, _j_ = 3, _L_ = _{_ 2 _n,_ 1 _,_ 2 _}_, and _R_ = _{_ 3 _,_ 4 _, . . .,_ 2 _n −_ 1 _}_ . In this case, we have that
_AL_ = _A_ 3(1 _,_ 2 _,_ 3 _, xL,_ 2 _n −_ 1 _,_ 2 _n_ ) and _IR_ = _In−_ 1(2 _n −_ 1 _, xR,_ 3 _,_ 4 _, . . .,_ 2 _n −_ 2). Just as we did
at tree-level, we will consider each contribution of the known three-point amplitude to the

gluing rule individually. Starting with _k_ = 1, we find that




_[∂][I][R]_ + ( _X_ 1 _,p −_ _X_ 2 _n−_ 1 _,p_ ) _[∂][I][R]_

_∂X_ 2 _,m_ _∂X_ 2



_k_ = 1 : [ _X_ 2 _n,_ 2 _−_ _X_ 2 _n,_ 3 _−_ _X_ 2 _n−_ 1 _,_ 2] _×_



��



( _X_ 1 _,m −_ _X_ 2 _n−_ 1 _,m_ ) _[∂][I][R]_

_∂X_ 2

_m∈R_



_∂X_ 2 _,p_









( _Xm,_ 1 _−_ _Xm,_ 2 _n−_ 1 _θ_ [ˆ] _m,_ 2 _n−_ 2) _[∂][I][R]_

_∂Xm,_

_m∈R_



����2 _→_ 2 _n−_ 1




 +



_∂IR_

_[∂][I][R]_ + _X_ 2 _n−_ 2 _,_ 2 _n−_ 1

_∂Xm,_ 2 _∂X_ 2 _n−_ 2 _,_ 2 _n−_ 1



_,_



(B.1)
where, like at tree-level, we have relabeled the dummy index _xR_ _→_ 2. Also, recall that _θ_ [ˆ] _a,b_
equals 1 if _a_ = _b_ and 0 otherwise. Expanding the prefactors of the above equation in soft


                   - 59                   

factors, and keeping in mind that _X_ 2 _n−_ 2 _,_ 2 _n−_ 1 _→_ _δ_ 2 _n−_ 2 _,_ 2 _n−_ 1 is itself a soft factor, we derive




_[∂][I][R]_ + ( _δ_ 1 _,p −_ _δ_ 2 _n−_ 1 _,p_ ) _[∂][I][R]_

_∂X_ 2 _,m_ _∂X_ 2



_k_ = 1 : [ _X_ 2 _n,_ 2 _−_ _X_ 2 _n,_ 3 _−_ _δ_ 2 _n−_ 1 _,_ 2] _×_



��



( _δ_ 1 _,m −_ _δ_ 2 _n−_ 1 _,m_ ) _[∂][I][R]_

_∂X_ 2

_m∈R_



_∂X_ 2 _,p_



_−Xs,s_ _∂IR_ + _∂X_ 2 _n−_ 1 _,_ 2





( _δm,_ 1 _−_ _δm,_ 2 _n−_ 1 _θ_ [ˆ] _m,_ 2 _n−_ 2) _[∂][I][R]_

_∂Xm,_

_m∈R_



_∂Xm,_ 2



_∂IR_
+ _δ_ 2 _n−_ 2 _,_ 2 _n−_ 1
_∂X_ 2 _n−_ 2 _,_ 2 _n−_ 1



����2 _→_ 2 _n−_ 1




_._



(B.2)
Now, the lower-point integrand _IR_ depends on the soft factors via _Xm,_ 2 _n−_ 1 = _Xm,s_ + _δm,_ 2 _n−_ 1
(and similarly for _X_ 2 _n−_ 1 _,m_ ) for _m ∈_ _R_ . So, expanding _IR_ in _δm,_ 2 _n−_ 1 and _δ_ 2 _n−_ 1 _,m_, we derive
the all-soft-order expansion of Eq. (B.1); at leading order _O_ ( _δ_ [0] ) in particular, we get



_∂In−_ 1
_k_ = 1 : ( _X_ 2 _n,_ 3 _−_ _X_ 2 _n,_ 2) _Xs,s_

_∂Xs,_ 2



+ _O_ ( _δ_ ) _,_ (B.3)
���� _S_



where _In−_ 1 _≡In−_ 1( _s,_ 2 _, . . .,_ 2 _n_ _−_ 2). The notation “ _|S_ ” instructs us to evaluate on the locus
of _Xs,_ 2 _, X_ 2 _n−_ 2 _,s_ = 0, as required by our definition of the soft limit. In this case, gauge
invariance in gluon 2 means that the derivative _∂Xs,_ 2 _In−_ 1 is independent of _Xs,_ 2, but we
still need to manually send _X_ 2 _n−_ 2 _,s_ _→_ 0 to ensure consistency of the limit.
As for _k_ = 2, we find



_∂Xm,_ 2







_k_ = 2 : _X_ 2 _n,_ 3 _×_



��


_m∈R_




( _X_ 2 _,m −_ _X_ 2 _n−_ 1 _,m_ ) _[∂][I][R]_




_[∂][I][R]_ + ( _Xm,_ 2 _−_ _Xm,_ 2 _n−_ 1 _θ_ [ˆ] _m,_ 2 _n−_ 2) _[∂][I][R]_

_∂X_ 2 _,m_ _∂Xm,_



_∂IR_

+( _X_ 2 _,p −_ _X_ 2 _n−_ 1 _,p_ ) _[∂][I][R]_ + _X_ 2 _n−_ 2 _,_ 2 _n−_ 1

_∂X_ 2 _,p_ _∂X_ 2 _n−_ 2 _,_ 2 _n−_ 1



����2 _→_ 2 _n−_ 1




_._



(B.4)
Quite nicely, just like at tree-level, the large sum inside the brackets simply becomes _IR_
due to the surface gauge invariance of _IR_ ! As such, the soft expansion of the _k_ = 2 term
comes exclusively from the Taylor expansion of _IR_, which at leading order yields


_X_ 2 _n,_ 3 _In−_ 1( _s,_ 2 _, . . .,_ 2 _n −_ 2) _|S_ + _O_ ( _δ_ ) _._ (B.5)


Finally, we examine the case of _j_ = 2 _n_ . Here, since _∂X_ 2 _n,xL_ _AL_ = _δ_ 2 _n−_ 1 _,_ 2, the entire term is
subleading in the soft expansion, and will thus not contribute to the leading theorem.
Now, we can undergo exactly the same procedure for the residue _R_ 2 _n−_ 3 _,_ 1, where we
take _i_ = 1, _j_ = 2 _n_ _−_ 3, _L_ = _{_ 1 _,_ 2 _, . . .,_ 2 _n_ _−_ 3 _}_, _R_ = _{_ 2 _n_ _−_ 2 _,_ 2 _n_ _−_ 1 _,_ 2 _n}_, _IL_ =
_In−_ 1(1 _,_ 2 _, . . .,_ 2 _n_ _−_ 3 _, xL_ ) and _AR_ = _A_ 3(1 _, xR,_ 2 _n_ _−_ 3 _,_ 2 _n_ _−_ 2 _,_ 2 _n_ _−_ 1 _,_ 2 _n_ ) in Eq. (2.13).
In this case, _m_ = 2 _n −_ 1 gives the analogous expression for Eq. (B.2), _m_ = 2 _n −_ 2 for

Eq. (B.4), and we again find something manifestly subleading for _m_ = 2 _n_ . So, by further
Taylor expanding _IL_ now in factors of _δ_ 1 _,k_ and _δk,_ 1, we can straightforwardly obtain the allsoft-order expansion of _R_ 2 _n−_ 3 _,_ 1. In doing so, we have also proved the leading soft theorem
(pre-gauge-invariantification), displayed in Eq. (5.12).


                   - 60                   

**Bibliography**


[1] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Scalar-Scaffolded_ _Gluons_ _and_
_the_ _Combinatorial_ _Origins_ _of_ _Yang-Mills_ _Theory_, `[arXiv:2401.00041](http://arxiv.org/abs/2401.00041)` .


[2] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Hidden_ _zeros_ _for_
_particle/string_ _amplitudes_ _and_ _the_ _unity_ _of_ _colored_ _scalars,_ _pions_ _and_ _gluons_,
`[arXiv:2312.16282](http://arxiv.org/abs/2312.16282)` .


[3] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Nonlinear_ _Sigma_ _model_
_amplitudes_ _to_ _all_ _loop_ _orders_ _are_ _contained_ _in_ _the_ _Tr(_ Φ _3)_ _theory_, _Phys._ _Rev._ _D_ **110** (2024),
no. 6 065018, [ `[arXiv:2401.05483](http://arxiv.org/abs/2401.05483)` ].


[4] F. Cachazo, N. Early, and B. G. Umbert, _Smoothly_ _splitting_ _amplitudes_ _and_ _semi-locality_,
_Journal_ _of_ _High_ _Energy_ _Physics_ **2022** (Aug., 2022).


[5] N. Arkani-Hamed and C. Figueiredo, _All-order_ _splits_ _and_ _multi-soft_ _limits_ _for_ _particle_ _and_
_string_ _amplitudes_, `[arXiv:2405.09608](http://arxiv.org/abs/2405.09608)` .


[6] Y. Zhang, _New_ _Factorizations_ _of_ _Yang-Mills_ _Amplitudes_, `[arXiv:2406.08969](http://arxiv.org/abs/2406.08969)` .


[7] Y. Zhang, _On_ _the_ _New_ _Factorizations_ _of_ _Yang-Mills_ _Amplitudes_, `[arXiv:2412.15198](http://arxiv.org/abs/2412.15198)` .


[8] K. Zhou, _Understanding_ _zeros_ _and_ _splittings_ _of_ _ordered_ _tree_ _amplitudes_ _via_ _Feynman_
_diagrams_, `[arXiv:2411.07944](http://arxiv.org/abs/2411.07944)` .


[9] Y. Li, T. Wang, T. Brauner, and D. Roest, _Diagrammatic_ _Derivation_ _of_ _Hidden_ _Zeros_ _and_
_Exact_ _Factorisation_ _of_ _Pion_ _Scattering_ _Amplitudes_, `[arXiv:2412.14858](http://arxiv.org/abs/2412.14858)` .


[10] C. Bartsch, T. V. Brown, K. Kampf, U. Oktem, S. Paranjape, and J. Trnka, _Hidden_
_Amplitude_ _Zeros_ _From_ _Double_ _Copy_, `[arXiv:2403.10594](http://arxiv.org/abs/2403.10594)` .


[11] L. Rodina, _Hidden_ _zeros_ _=_ _secret_ _ultraviolet_ _scaling,_ _and_ _a_ _new_ _path_ _to_ _uniqueness_,

`[arXiv:2406.04234](http://arxiv.org/abs/2406.04234)` .


[12] J. V. Backus and L. Rodina, _Emergence_ _of_ _Unitarity_ _and_ _Locality_ _from_ _Hidden_ _Zeros_ _at_
_One-Loop_, `[arXiv:2503.03805](http://arxiv.org/abs/2503.03805)` .


[13] C. R. T. Jones and S. Paranjape, _Smooth_ _Splitting_ _and_ _Zeros_ _from_ _On-Shell_ _Recursion_,

`[arXiv:2505.02520](http://arxiv.org/abs/2505.02520)` .


[14] B. Feng, L. Zhang, and K. Zhou, _Hidden_ _Zeros_ _and_ 2 _-split_ _via_ _BCFW_ _Recursion_ _Relation_,

`[arXiv:2504.14215](http://arxiv.org/abs/2504.14215)` .


[15] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Surface_ _Kinematics_ _and_ _”The”_
_Yang-Mills_ _Integrand_, `[arXiv:2408.11891](http://arxiv.org/abs/2408.11891)` .


[16] S. Weinberg, _Photons_ _and_ _gravitons_ _in_ _s-matrix_ _theory:_ _Derivation_ _of_ _charge_ _conservation_
_and_ _equality_ _of_ _gravitational_ _and_ _inertial_ _mass_, _Phys._ _Rev._ **135** (Aug, 1964) B1049–B1056.


[17] S. Weinberg, _Infrared_ _photons_ _and_ _gravitons_, _Phys._ _Rev._ **140** (Oct, 1965) B516–B524.


[18] R. Britto, F. Cachazo, B. Feng, and E. Witten, _Direct_ _proof_ _of_ _tree-level_ _recursion_ _relation_ _in_
_Yang-Mills_ _theory_, _Phys._ _Rev._ _Lett._ **94** (2005) 181602, [ `[hep-th/0501052](http://arxiv.org/abs/hep-th/0501052)` ].


[19] R. Britto, F. Cachazo, and B. Feng, _New_ _recursion_ _relations_ _for_ _tree_ _amplitudes_ _of_ _gluons_,
_Nucl._ _Phys._ _B_ **715** (2005) 499–522, [ `[hep-th/0412308](http://arxiv.org/abs/hep-th/0412308)` ].


[20] C. Cheung, K. Kampf, J. Novotny, and J. Trnka, _Effective_ _Field_ _Theories_ _from_ _Soft_ _Limits_ _of_
_Scattering_ _Amplitudes_, _Phys._ _Rev._ _Lett._ **114** (2015), no. 22 221602, [ `[arXiv:1412.4095](http://arxiv.org/abs/1412.4095)` ].


                   - 61                   

[21] C. Cheung, K. Kampf, J. Novotny, C.-H. Shen, and J. Trnka, _On-Shell_ _Recursion_ _Relations_
_for_ _Effective_ _Field_ _Theories_, _Phys._ _Rev._ _Lett._ **116** (2016), no. 4 041601, [ `[arXiv:1509.03309](http://arxiv.org/abs/1509.03309)` ].


[22] C. Cheung, K. Kampf, J. Novotny, C.-H. Shen, and J. Trnka, _A_ _Periodic_ _Table_ _of_ _Effective_
_Field_ _Theories_, _JHEP_ **02** (2017) 020, [ `[arXiv:1611.03137](http://arxiv.org/abs/1611.03137)` ].


[23] K. Zhou, _Tree_ _level_ _amplitudes_ _from_ _soft_ _theorems_, _JHEP_ **03** (2023) 021,

[ `[arXiv:2212.12892](http://arxiv.org/abs/2212.12892)` ].


[24] K. Zhou, _Constructing_ _tree_ _amplitudes_ _of_ _scalar_ _EFT_ _from_ _double_ _soft_ _theorem_, _JHEP_ **12**
(2024) 079, [ `[arXiv:2406.03784](http://arxiv.org/abs/2406.03784)` ].


[25] C. Hu and K. Zhou, _Recursive_ _construction_ _for_ _expansions_ _of_ _tree_ _Yang–Mills_ _amplitudes_
_from_ _soft_ _theorem_, _Eur._ _Phys._ _J._ _C_ **84** (2024), no. 3 221, [ `[arXiv:2311.03112](http://arxiv.org/abs/2311.03112)` ].


[26] F. Cachazo, P. Cha, and S. Mizera, _Extensions_ _of_ _Theories_ _from_ _Soft_ _Limits_, _JHEP_ **06**
(2016) 170, [ `[arXiv:1604.03893](http://arxiv.org/abs/1604.03893)` ].


[27] A. Strominger, _On_ _BMS_ _Invariance_ _of_ _Gravitational_ _Scattering_, _JHEP_ **07** (2014) 152,

[ `[arXiv:1312.2229](http://arxiv.org/abs/1312.2229)` ].


[28] A. Strominger, _Asymptotic_ _Symmetries_ _of_ _Yang-Mills_ _Theory_, _JHEP_ **07** (2014) 151,

[ `[arXiv:1308.0589](http://arxiv.org/abs/1308.0589)` ].


[29] A. Strominger, _Lectures_ _on_ _the_ _Infrared_ _Structure_ _of_ _Gravity_ _and_ _Gauge_ _Theory_ . 3, 2017.


[30] V. Lysov, S. Pasterski, and A. Strominger, _Low’s_ _Subleading_ _Soft_ _Theorem_ _as_ _a_ _Symmetry_ _of_
_QED_, _Phys._ _Rev._ _Lett._ **113** (2014), no. 11 111601, [ `[arXiv:1407.3814](http://arxiv.org/abs/1407.3814)` ].


[31] F. Cachazo and A. Strominger, _Evidence_ _for_ _a_ _New_ _Soft_ _Graviton_ _Theorem_,

`[arXiv:1404.4091](http://arxiv.org/abs/1404.4091)` .


[32] Z.-Z. Li, H.-H. Lin, and S.-Q. Zhang, _Infinite_ _Soft_ _Theorems_ _from_ _Gauge_ _Symmetry_, _Phys._
_Rev._ _D_ **98** (2018), no. 4 045004, [ `[arXiv:1802.03148](http://arxiv.org/abs/1802.03148)` ].


[33] A. Laddha and A. Sen, _Sub-subleading_ _Soft_ _Graviton_ _Theorem_ _in_ _Generic_ _Theories_ _of_
_Quantum_ _Gravity_, _JHEP_ **10** (2017) 065, [ `[arXiv:1706.00759](http://arxiv.org/abs/1706.00759)` ].


[34] A. Sen, _Subleading_ _Soft_ _Graviton_ _Theorem_ _for_ _Loop_ _Amplitudes_, _JHEP_ **11** (2017) 123,

[ `[arXiv:1703.00024](http://arxiv.org/abs/1703.00024)` ].


[35] Z. Bern, S. Davies, and J. Nohle, _On_ _Loop_ _Corrections_ _to_ _Subleading_ _Soft_ _Behavior_ _of_ _Gluons_
_and_ _Gravitons_, _Phys._ _Rev._ _D_ **90** (2014), no. 8 085015, [ `[arXiv:1405.1015](http://arxiv.org/abs/1405.1015)` ].


[36] T. Klose, T. McLoughlin, D. Nandan, J. Plefka, and G. Travaglini, _Double-Soft_ _Limits_ _of_
_Gluons_ _and_ _Gravitons_, _JHEP_ **07** (2015) 135, [ `[arXiv:1504.05558](http://arxiv.org/abs/1504.05558)` ].


[37] Y. Hamada and G. Shiu, _Infinite_ _Set_ _of_ _Soft_ _Theorems_ _in_ _Gauge-Gravity_ _Theories_ _as_
_Ward-Takahashi_ _Identities_, _Phys._ _Rev._ _Lett._ **120** (2018), no. 20 201601, [ `[arXiv:1801.05528](http://arxiv.org/abs/1801.05528)` ].


[38] G. Salvatori, _1-loop_ _Amplitudes_ _from_ _the_ _Halohedron_, _JHEP_ **12** (2019) 074,

[ `[arXiv:1806.01842](http://arxiv.org/abs/1806.01842)` ].


[39] N. Arkani-Hamed, S. He, G. Salvatori, and H. Thomas, _Causal_ _diamonds,_ _cluster_ _polytopes_
_and_ _scattering_ _amplitudes_, _JHEP_ **11** (2022) 049, [ `[arXiv:1912.12948](http://arxiv.org/abs/1912.12948)` ].


[40] N. Arkani-Hamed and C. Figueiredo, _Circles_ _and_ _Triangles,_ _the_ _NLSM_ _and_ _Tr(_ Φ [3] _)_,

`[arXiv:2403.04826](http://arxiv.org/abs/2403.04826)` .


[41] F.-S. Wei and K. Zhou, _On_ _soft_ _factors_ _and_ _transmutation_ _operators_, _JHEP_ **10** (2024) 102,

[ `[arXiv:2406.04622](http://arxiv.org/abs/2406.04622)` ].


                   - 62                   

[42] N. Arkani-Hamed, S. He, and T. Lam, _Stringy_ _canonical_ _forms_, _JHEP_ **02** (2021) 069,

[ `[arXiv:1912.08707](http://arxiv.org/abs/1912.08707)` ].


[43] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _All_ _Loop_
_Scattering_ _as_ _a_ _Counting_ _Problem_, `[arXiv:2309.15913](http://arxiv.org/abs/2309.15913)` .


[44] N. Arkani-Hamed, S. He, T. Lam, and H. Thomas, _Binary_ _geometries,_ _generalized_ _particles_
_and_ _strings,_ _and_ _cluster_ _algebras_, _Phys._ _Rev._ _D_ **107** (2023), no. 6 066015,

[ `[arXiv:1912.11764](http://arxiv.org/abs/1912.11764)` ].


[45] M. B. Green, J. H. Schwarz, and E. Witten, _SUPERSTRING_ _THEORY._ _VOL._ _1:_
_INTRODUCTION_ . Cambridge Monographs on Mathematical Physics. 7, 1988.


[46] C. Cheung, C.-H. Shen, and C. Wen, _Unifying_ _Relations_ _for_ _Scattering_ _Amplitudes_, _JHEP_ **02**
(2018) 095, [ `[arXiv:1705.03025](http://arxiv.org/abs/1705.03025)` ].


[47] N. Arkani-Hamed, C. Figueiredo, and G. N. Remmen, _Open_ _String_ _Amplitudes:_
_Singularities,_ _Asymptotics,_ _and_ _New_ _Representations_, `[arXiv:2412.20639](http://arxiv.org/abs/2412.20639)` .


[48] Y.-t. Huang, O. Schlotterer, and C. Wen, _Universality_ _in_ _string_ _interactions_, _JHEP_ **09**
(2016) 155, [ `[arXiv:1602.01674](http://arxiv.org/abs/1602.01674)` ].


[49] Y.-X. Tao and Q. Chen, _A_ _type_ _of_ _unifying_ _relation_ _in_ _(A)dS_ _spacetime_, _JHEP_ **02** (2023)
030, [ `[arXiv:2210.15411](http://arxiv.org/abs/2210.15411)` ].


[50] Q. Chen and Y.-X. Tao, _Differential_ _operators_ _and_ _unifying_ _relations_ _for_ _1-loop_ _Feynman_
_integrands_ _from_ _Berends-Giele_ _currents_, _JHEP_ **08** (2023) 038, [ `[arXiv:2301.08043](http://arxiv.org/abs/2301.08043)` ].


[51] Q. Cao, J. Dong, S. He, and F. Zhu, _One-loop_ _amplitudes_ _in_ _gauge_ _theories_, _Phys._ _Rev._ _D_
**111** (2025), no. 6 065015, [ `[arXiv:2412.19629](http://arxiv.org/abs/2412.19629)` ].


                   - 63                   

