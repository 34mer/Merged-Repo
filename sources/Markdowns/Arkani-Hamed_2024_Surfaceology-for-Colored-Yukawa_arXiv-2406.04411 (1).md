Prepared for submission to JHEP

##### **Surfaceology for Colored Yukawa Theory**


**Shounak** **De,** _[a,]_ **Andrzej** **Pokraka,** _[a,]_ **Marcos** **Skowronek,** _[a,]_ **Marcus** **Spradlin,** _[a,b,c,]_

**Anastasia** **Volovich** _[a,b,]_


_aDepartment_ _of_ _Physics,_ _Brown_ _University,_ _Providence,_ _RI_ _02912,_ _USA_

_bDepartment_ _of_ _Physics,_ _Harvard_ _University,_ _Cambridge,_ _MA_ _02138,_ _USA_

_cBrown_ _Theoretical_ _Physics_ _Center,_ _Brown_ _University,_ _Providence,_ _RI_ _02912,_ _USA_


_E-mail:_ `shounak` `[de@brown.edu](mailto:shounak_de@brown.edu)`, `andrzej` `[pokraka@brown.edu](mailto:andrzej_pokraka@brown.edu)`,
`marcos` ~~`s`~~ `kowronek` ~~`s`~~ `antos@brown.edu`, `marcus` `[spradlin@brown.edu](mailto:marcus_spradlin@brown.edu)`,

```
 anastasia v olovich@brown.edu

```

Abstract: Arkani-Hamed and collaborators have recently shown that scattering amplitudes

for colored theories can be expressed as integrals over combinatorial objects simply con
structed from surfaces decorated by kinematic data. In this paper we extend the curve inte
gral formalism to theories with colored fermionic matter and present a compact formula for

the all-loop, all-genus, all-multiplicity amplitude integrand of a colored Yukawa theory. The

curve integral formalism makes certain properties of the amplitudes manifest and repackages

non-trivial numerators into a single combinatorial object. We also present an efficient formula
for _L_ -loop integrated amplitudes in terms of a sum over 2 _[L]_ combinatorial determinants.


**Contents**


**1** **Introduction** **1**


**2** **Surfaceology** **review** **2**


**3** **Fermionic** **curve** **integrals** **for** **colored** **Yukawa** **theory** **5**

3.1 Colored Yukawa theory 5

3.2 General features of the theory 6

3.3 The combinatorial amplitude for colored Yukawa theory 10


**4** **Examplitudes** **14**

4.1 Trees 14

4.1.1 Five-point 15

4.1.2 Six-point 17

4.2 One-loop 19

4.2.1 Planar two-point 20

4.2.2 Planar four-point 23

4.2.3 Non-planar three-point 25

4.3 Planar two-loop two-point 27


**5** **Outlook** **32**


**1** **Introduction**


Recently Arkani-Hamed and collaborators [1–3] have reformulated scattering amplitudes for

colored theories in terms of fundamentally geometric/combinatorial objects called curve inte
grals. Remarkably, in a theory of matrix-valued scalars, the color-ordered partial amplitude

at any loop order and multiplicity is computed via a global Schwinger integral that is the

tropicalization of certain _stringy_ integrals. These objects provide a unified description for all

Feynman diagrams of any given topology, as well as a canonical definition of loop integrands.

The curve integral perspective has facilitated a host of novel results: hidden zeroes [4, 5],
new factorization relations [6, 7], gluons from scalars [8], the relationship between Tr(Φ [3] ) and

non-linear sigma model amplitudes [9, 10], and related work [11–14].

In this paper, we extend the curve integral formalism to theories with fermionic matter;

an essential step towards realizing the amplitudes of more general quantum field theories in

terms of purely combinatorial/geometric building blocks. Specifically, we study a colored

Yukawa theory and derive compact tropical expressions for _L_ -loop _n_ -point amplitudes both


                   - 1                    

before and after loop integration. Our formulae do not make reference to a sum over Feynman

diagrams and only depend on the combinatorics of curves associated to distinguished ribbon
graphs or fatgraphs. In particular, our post loop-integration formula is a 2 _[L]_ -term sum over

tropical determinants that encode the tensor structure of the theory. Despite avoiding the
need to sum over a large number of Feynman diagrams, our formulae have an inherent 2 _[L]_


growth in complexity stemming from the fact that each internal puncture in the surface can

be assigned different species (in this case, two).

The paper is organized as follows. Section 2 reviews the essential aspects of the curve

integral formalism, highlighting the essential steps to compute the relevant geometric objects.

Section 3 defines the Lagrangian for our colored Yukawa theory and explains how the color

ordering of the interaction vertex places constraints on the theory. In subsection 3.3, we

present the main result of this work: a curve integral formula for colored Yukawa amplitudes.

Section 4 provides pedagogical examples at tree and loop level demonstrating the practical

application of our formulae. Section 5 concludes with potential directions for future research.


**2** **Surfaceology** **review**


In this section, we review the basic aspects of the curve integral formalism, outlining the nec
essary steps to compute the “curvy” objects that enter our formulae for scattering amplitudes

in colored Yukawa theory. For more insight into the physical and mathematical significance

of these elements, we refer to the original works and their extensions [1–3, 5, 6, 8–10].

In the curve integral formalism, the kinematic data of color-ordered partial amplitudes

is described by the set of all possible curves on a representative fatgraph Γ for the amplitude

in question. It is also often convenient to work with the associated surface Σ where the

fatgraph Γ corresponds to a specific triangulation of Σ via graph duality (see figure 1). Given

a fatgraph Γ, its propagators can be interpreted as roads along which certain paths or _curves_
are drawn. Each road is assigned a variable _ye_, and a curve _C_ is described by a _word_ which
records the series of roads and left/right turns at a vertex that the curve _C_ makes on the

fatgraph
_C_ = _yiRyjLyk . . . ._ (2.1)


On the surface, the endpoints of a path can either be an external or an internal puncture. In

the latter case, this is depicted on the fatgraph as spiraling indefinitely around a loop. Due

to an over-counting associated with the direction of the spiral, we choose to work exclusively

with curves that spiral _counterclockwise_ (if one chooses to work with the clockwise convention,

some formulae must be modified).

From these curves, we generate the kinematic data of color-ordered partial amplitudes.
The momentum associated with each curve _PC_ _[µ]_ [is] [given] [by] [the] [prescription]


_PC_ _[µ]_ [=] _[ P][ µ]_ start [+]          - _P_ incoming _[µ]_ from the left _[.]_ (2.2)

right turns


                   - 2                    

3


5







4





**Figure** **1** : Surface triangulation (right) corresponding to a certain fatgraph (left). Both are

related by graph duality.


In other words, each time the path takes a right turn, we add the incoming momentum from
the left road of the vertex. We also introduce the _g_ -vector associated to each curve, _⃗gC_ _∈_ R _[E]_,
where _E_ is the number of roads in the fatgraph. In order to compute it, it is useful to represent

the left/right turns in the path as going up/down along a _mountainscape_


yl



ym (2.3)

###### **·**



_C_ = _yiRyjLykLylRym . . ._ _←→_



yi yk


###### **··**

yj


Then, the components of the corresponding _g_ -vector are


_gC_ _[e]_ [= (# of] [peaks] [at] _[ e]_ [)] _[ −]_ [(# of] [valleys] [at] _[ e]_ [)] _[.]_ (2.4)


The collection of _g_ -vectors divides R _[E]_ into a spanning set of top-dimensional cones that

defines the _Feynman_ _fan_ . Since each top-dimensional cone of the Feynman fan corresponds

to a specific Feynman diagram, the propagators of a Feynman diagram are those associated

to the _g_ -vectors defining that cone.

In order to determine which curves are present in the different cones on the fan, we need
another object called the _tropical_ _headlight_ _function_ _αC_ ( _**t**_ ). These can be computed from
the associated 2 _×_ 2 curve matrices _MC_, which encode the information of each curve _C_ . We
obtain them by replacing the elements in the words with the associated matrices















_ye_ _→_




1 0
0 _ye_



_,_ _L →_




1 0

1 1



_,_ _R →_




1 1

0 1



_._ (2.5)




- 3 

Then, the corresponding headlight function _αC_ ( _**t**_ ) is given by


_αC_ ( _**t**_ ) = Trop[( _MC_ )11] + Trop[( _MC_ )22] _−_ Trop[( _MC_ )12] _−_ Trop[( _MC_ )21] _,_ (2.6)


where the tropicalization of a function _f_ ( _**y**_ ) is defined as the limit


_f_ ( _**y**_ ) _→_ exp �Trop( _f_ )( _**t**_ )� _,_ as _ye_ = exp _te,_ _te_ _→∞._ (2.7)


For computational purposes, this simply amounts to the replacement rule


_xy_ _→_ _tx_ + _ty,_ _x_ + _y_ _→_ max( _tx, ty_ ) _._ (2.8)


Importantly, the headlight functions _αC_ are piecewise linear in each cone on the Feynman
fan. Moreover, they only “light up” on the cones bounded by the corresponding vector _⃗gC_


_αC_ ( _⃗gD_ ) = _δC,D._ (2.9)


Another useful function that is directly related to the _αC_ ’s is the _tropical step function_ Θ _C_ ( _**t**_ ),
which is piecewise constant on each cone [3]



Θ _C_ = _⃗gC_ _· ∇αC_ =




1 in any cone that contains _C,_

(2.10)
0 otherwise _._



Starting from non-planar surfaces at one loop (or at two loops for planar ones), there are

sets of curves that can wind an arbitrary number of times around the punctures before ending.

These curves correspond to the same Feynman diagrams and therefore, it is necessary to mod

out by the Mapping Class Group (MCG) so that we do not over count [1]. This is achieved at
the level of the curve integral by inserting a tropical function _K_ called the _Mirzakhani_ _kernel_ .

In the examples considered in this paper, there is only one generator of the MCG, which
takes the form of a closed curve ∆ [1] . The curves that intersect ∆are divided into different
cosets under the MCG. For each coset _i_, we choose a curve representative _Ci_ [0] [and] [keep] [only]
the paths compatible with this set. Using this data, the Mirzakhani kernel is



_K_ = 

_i_



_αCi_ 0 (2.11)
_ρ_ _[,]_



where _ρ_ is the sum over the set _S_ of all curves not invariant under MCG


       _ρ_ = _αC._ (2.12)


_C∈S_


Since _K_ has support on a finite set of cones, we only need to compute a small number of
headlight functions, namely the ones compatible with the coset representatives _Ci_ [0][.]


1For a more general treatment of this process, please refer to [1].


                   - 4                    

## ✓

Φ Φ


**Figure** **2** : The Lagrangian (3.1) only allows for one ordering of the cubic vertex (left), while

the other one (right) cannot appear in the partial amplitudes.


**3** **Fermionic** **curve** **integrals** **for** **colored** **Yukawa** **theory**


This section starts with the Lagrangian for our colored Yukawa model and enumerates the

basic Feynman rules. Subsequently, we explain how the color-ordered partial amplitudes

are subject to stringent constraints that are made manifest in the surface picture. These

constraints greatly simplify the structure of the partial amplitudes. Lastly, we present a

formula for the loop integrands and their integrated partial amplitudes in our colored Yukawa

theory.


**3.1** **Colored** **Yukawa** **theory**


In this paper, we consider _N_ [2] massless colored Dirac fermions and scalars transforming in
the fundamental _×_ anti-fundamental representation of _SU_ ( _N_ ) minimally coupled via a cubic

Yukawa and a cubic scalar vertex. Explicitly, the Lagrangian is








                               
( _i_ Ψ [¯] _[Aa]_ _/∂AB_ Ψ _[Bb]_ ) _T_ _[a]_ _T_ _[b]_ _−_ [1] [¯Ψ] _[Aa]_ [Ψ] _[b]_ _A_ [Φ] _[c][T][ a][T][ b][T][ c]_ [+] _[λ]_ [Φ] _[a]_ [Φ] _[b]_ [Φ] _[c][T][ a][T][ b][T][ c]_

2 [(] _[∂][µ]_ [Φ] _[a][∂][µ]_ [Φ] _[b]_ [)] _[T][ a][T][ b]_ [+] _[g]_



_L_ = Tr



_,_



= _i_ Tr�¯Ψ _/∂_ Ψ� _−_ [1] - _∂µ_ Φ _∂_ _[µ]_ Φ� + _g_ Tr�¯ΨΨΦ� + _λ_ Tr�Φ [3][�] _._ (3.1)

2 [Tr]



Here, _A, B_ are Dirac indices, _T_ _[a]_ are the _SU_ ( _N_ ) generators, Φ _[i]_ _j_ [= Φ] _[a]_ [(] _[T][ a]_ [)] _j_ _[i]_ [, and Ψ] _[i]_ _j_ [= Ψ] _[a]_ [(] _[T][ a]_ [)] _j_ _[i]_
with _i, j_ = 1 _,_ 2 _, . . ., N_ . [2] The Feynman rules for the propagators and vertices are



∆ _[ab]_ _[i][p][/]_
ΨΨ [¯] [=]

[2]




_[δ][ab]_ _[,]_ _VY_ _[abc]_ = _ig_ Tr( _T_ _[a]_ _T_ _[b]_ _T_ _[c]_ ) _,_ _V_ Φ _[abc]_ [3] [=] _[ iλ]_ [Tr(] _[T][ a][T][ b][T][ c]_ [)] _[,]_ (3.2)
_p_ [2]




_[i][p][/]_ _[δ][ab]_ _[,]_ ∆ _[ab]_ Φ [=] _[−][i]_

_p_ [2] _p_ [2]



and we assume all the particles to be ingoing. In the following, we consider partial ordered

amplitudes and drop the dependence on the color indices _a, b, c_ . We also assume that the

Dirac fermions and gamma matrices are in arbitrary number of dimensions _D_ .

It is very important to note that the Yukawa interaction vertex has a definite color ordering. Consequently, the color indices must be contracted in the order dictated by Tr(ΨΨΦ) [¯] in

double-line diagrams (see figure 2). The diagrams that contribute to a partial amplitude are


2In what follows, we denote the trace over _SU_ ( _N_ ) color indices _a, b_ as Tr[ _. . ._ ] and the trace over Dirac

indices _A, B_ as tr[ _. . ._ ] _._


                   - 5                    

Ψ1



Ψ2







Ψ1


**Figure** **3** : The planar three-point topology (left) cannot be constructed with the vertex

ordering in the Lagrangian (3.1), but the same Feynman integral is obtained from the non
planar diagram (right).


then constrained such that at every interaction vertex, the outgoing fermion has to appear

immediately after the outgoing anti-fermion in clockwise order. In the language of curves,

this means that the fermionic charge flow always turns right at every vertex in the fatgraph.

Compared to a theory where both vertex orderings are allowed, only a subset of dia
grams is allowed for each partial amplitude of (3.1). However, we want to emphasize that all

Feynman integrals that can appear in ordinary (uncolored) Yukawa theory are present in at
least one partial amplitude. [3] To illustrate this, consider the one-loop three-point amplitude
_A_ [one-loop] 3 (Ψ [¯] 1 _,_ Ψ2 _,_ Φ3). It is straightforward to see that it is impossible to draw the fatgraph
corresponding to the planar triangle topology involving two fermionic propagators, but the

associated Feynman integral can nevertheless be obtained from the double trace, non-planar
amplitude _A_ [one-loop] 3 (Ψ [¯] 1 _,_ Ψ2 _|_ Φ3) (see figure 3). Far from being a downside, the fact that the
vertex ordering severely constrains the partial amplitudes facilitates compact combinatorial

formulas for the amplitudes. As argued in the following section, both the distribution of the

different curves in each of the fermionic trace factors and their ordering within them are com
pletely fixed by the cubic vertex orientation. Each cone or Feynman diagram is thus solely

characterized by the set of curves that light up on the corresponding region of the Feynman

fan.


**3.2** **General** **features** **of** **the** **theory**


This section presents various interesting features of the partial amplitudes in the colored

Yukawa theory with Lagrangian (3.1).


3In other words, this formulation (3.1) is consistent with uncolored Yukawa theory, i.e., if we substituted for
the _SU_ ( _N_ ) generators _T_ _[a]_ _→_ ~~_√_~~ 1 [we] [would] [recover] [the] [amplitudes] [in] [conventional] [Yukawa] [theory] [without]

_N_ [1][,]
color indices. Note that one has to keep partial ordered amplitudes that would normally vanish from traceless
ness of the _SU_ ( _N_ ) generators.


                   - 6                    

**Fermions** **come** **in** **adjacent** **pairs.** The first property of our colored Yukawa theory we

want to highlight is that all external anti-fermions are immediately followed by an external

fermion in the color ordering. Moreover, the fermion traces always connect anti-fermion _i_ to

fermion _i_ + 1. Both of the above facts are a consequence of the single vertex orientation in

(3.1): if anti-fermion _i_ was instead followed by a scalar _i_ + 1, then the fermion line starting

from _i_ would have a scalar leg emerging from the left. This vertex would have a clockwise
assignment of ΨΦΨ, [¯] which doesn’t respect the ordering dictated by the Lagrangian.


**External fermion traces.** From the surface point of view, curves appear in a given external

fermion trace if and only if one of its endpoints connects to the fermion at the end of the trace.
Explicitly, if particles _i_ and _i_ + 1 are Ψ [¯] and Ψ respectively, all curves _Ci_ +1 _,j_ must correspond
to a fermionic particle. This also implies that _j_ must be an external anti-fermion, a scalar

or an internal puncture in the surface. Meanwhile, cones involving curves that connect two

fermion particles do not contribute to the amplitude. Moreover, two external punctures which

are not fermions are always connected by scalar curves.

These claims follow directly from the duality between surface triangulations and Feynman

diagrams. Using the first feature of our theory, we know that a Ψ puncture in the surface

corresponds to a region between two external adjacent fermionic legs in a Feynman diagram,

which are connected by a charged line.


Therefore, every internal propagator separating this region from any other one must be part of

this line, and thus of fermionic nature. Moreover, if an internal fermion propagator separated

two Ψ regions, then it would be part of two different charge flows, which is obviously not

possible.


**Internal** **fermion** **traces.** In addition to fermionic trace factors connecting two external

particles, Feynman diagrams can also contain fermion lines that form closed loops. Such

fermion trace lines are constrained to circle _one_ _and_ _only_ _one_ internal puncture in the surface

due to the orientation of the Yukawa vertex. Since the Feynman rules for these fermion loops

involve a Dirac trace of the propagator momenta, the tropical integrand for the amplitude

factorizes into separate internal traces where each curve is connected to the same internal
puncture _C_ 0 _a,j_ . This is again a consequence of the vertex ordering, which forces the fermionic
charge flow to stay confined to a single loop. We already know that the puncture _j_ in _C_ 0 _a,j_
cannot be an external fermion Ψ (such curves are always part of external charge flows), so _j_
must be an external anti-fermion Ψ, [¯] external scalar Φ or another internal puncture.

Even so, these curves are not guaranteed to be fermionic. Since the Lagrangian includes

a cubic scalar interaction, it is clear that for every Feynman diagram that contains a closed

fermion loop we must include an analogous graph where all the propagators participating in


                   - 7                    

Ψ2


1





Φ5



3


2


1 6



Φ5











5



4



6


**Figure** **4** : On the left, the internal puncture is fixed to be fermionic. Therefore, all curves

connected to it are charged and form a closed fermion line. On the right, the puncture is

scalar. Therefore, the curves connected to it are not necessarily charged.


the closed fermion loop are replaced by scalar propagators. In other words, each internal punc
ture can behave both as a fermion and a scalar. In the former case, all the curves connected

to the puncture carry fermionic charge. This is easily seen with the triangulation/diagram

duality, since the fermionic loop propagators separate the internal puncture region from the

other ones. This leads to the appearance of a closed Dirac trace in the corresponding Feynman

diagrams. Moreover, the contribution of this charge assignment vanishes on the cones with

curves where the internal puncture is connected to another fermion, since the two endpoints

would be Ψ particles.

On the other hand, when the internal puncture is not fixed to be a fermion, the curves

connected to this puncture are considered fermionic if and only if they are connected to

another Ψ puncture. Otherwise, they are considered scalar. This leads to Feynman diagrams

where the propagators in the loop are either part of a different fermion trace (for example, an

open line connecting two external legs) or scalar. The different scenarios described above are

illustrated in figure 4, where the external legs of the Feynman diagrams have been assigned

to punctures in the surface by moving counter-clockwise.
All in all, when writing down the numerator, we have to sum over all the possible 2 _[L]_


charge assignments for the set of internal punctures, where _L_ is the number of closed loops

in the amplitude.

Lastly, since the surface is invariant under permutations of the internal punctures, we
always order the punctures such that 0 _a_ comes before 0 _b_ if _a < b_ .


                   - 8                    

b


##### C



a





c



Ψi+1



b



d


e


##### C



i+1,k a c - · ·


Ψi+1



i+1,k a c - · ·



**Figure** **5** : The mountainscapes for two curves starting at fermion _i_ + 1 start differing at the

turn after _c_ . In the trace within the partial amplitude, the one that turns right (upper) will

appear before the one that turns left (lower).


**Universal** **fermion** **flow** **order.** Interestingly, it turns out that the order in which the

different curves appear inside each fermion trace is consistent across all cones in the Feynman

fan, and is fully fixed by their mountainscape.
To see this, consider the case of an external fermion line connecting Ψ [¯] _i_ and Ψ _i_ +1, as well
as two of its curves _Ci_ +1 _,j_ and _Ci_ +1 _,k_ . Since they have a common starting point at _i_ + 1, the
two mountainscapes associated with the curves will have an initial part in common and differ

after some specific turn (see figure 5). In particular, the momenta associated to the curve that
turns right first always appears before the other one in the chain of _/P C_ in a spinor product
_v_ ¯( _pi_ ) _· · ·_ _/P Ci_ +1 _,j · · ·_ _/P Ci_ +1 _,k · · · u_ ( _pi_ +1). Indeed, turning right first in the fatgraph means that
the curve connects to a puncture in the surface that appears later in clockwise order. Using

the graph duality, this means that the region corresponding to that puncture in the Feynman
diagram is closer to the antifermion (Ψ) [¯] leg, and thus will appear first in the trace factor.

For internal fermion loops, the argument is the same except that we need to choose a

starting curve for the closed loop in order to compare curves. The need for such a choice

arises from the cyclic symmetry of the trace (in the curve language, this reflects that curves

connecting to internal punctures spiral forever around it without a definite endpoint).


**Complete** **set** **of** **Feynman** **integrals** **for** **Yukawa.** As discussed above, the seemingly

innocent choice of only including one ordering for the cubic vertex in the Lagrangian has

constrained the form of the partial amplitudes in a remarkable manner. If we had included

the complementary direction of the charge flow, we would have to consider all the possible

permutations of the curves appearing in each Feynman diagram, spoiling their distribution

and ordering within the different fermion lines.

However, despite the fact that only a restricted class of Feynman diagrams contribute to

a partial amplitude, this model still generates the full set of Feynman integrals that appear


                   - 9                    

in the “complete” ordinary Yukawa theory.

Indeed, the independence of the interaction vertex on momenta means that any missing

contribution to the partial amplitude is identical to the one corresponding to some other color

ordering (see figure 3). Thus, we recover the uncolored theory (up to factors of _N_ ) by setting
all _SU_ ( _N_ ) generators to identity _T_ _[a]_ _→_ 1.

In the next subsection, we use these features to write down a complete yet compact

expression for the partial amplitude in colored Yukawa theory.


**3.3** **The** **combinatorial** **amplitude** **for** **colored** **Yukawa** **theory**


Any _n_ -point, _L_ -loop partial amplitude in colored Yukawa theory can be expressed as a sum
over Feynman diagrams, each of them consisting of a product of propagators _p_ [2] _i_ [in] [the] [de-]
nominator, weighed by a numerator factor _N_ and integrated over the undetermined loop
momenta _la_ . The numerator _N_ is a product over open (closed) spinor products of the form
_v_ ¯( _pi_ ) _· · · /pj · · · u_ ( _pk_ ) (tr - _· · · /pi · · ·_ �) coming from the internal fermionic propagators in (3.2).
Additionally, a prefactor of _ig_ or _iλ_ is added for each vertex in the diagram



��
( _ig_ ) _[V]_ [Ψ] ( _iλ_ ) _[V]_ [Φ]

Γ _a_



d _[D]_ _la_ _N_ Γ
_._ (3.3)
_iπ_ _[D/]_ [2] - _i∈_ Γ _[p]_ _i_ [2]



_A_ [(] _[n]_ [)] = 


_a_



Meanwhile, the curve formalism of [1, 2] formulates the partial amplitudes of colored TrΦ [3]

theory as an integral over a _E_ = ( _n−_ 3+3 _L_ +2 _g_ )-dimensional vector space called the Feynman

fan




- d _[E]_ _**t**_ _S_ ( _**t**_ ) =
MCG _[e][−][S]_ [(] _**[t]**_ [)] _[,]_



_αC_ ( _**t**_ ) _PC_ [2] _[,]_ (3.4)
_C_



��
_A_ =


_a_



d _[D]_ _la_
_iπ_ _[D/]_ [2]



where _C_ are the curves that one can draw on the base fatgraph, the _αC_ are the headlight
functions that select the set of curves that appear in each cone and we need to mod out by

the action of the Mapping Class Group (MCG) to avoid summing over equivalent Feynman

diagrams.

The extension of the curve integral to a fermionic theory like our Yukawa model requires
including a numerator factor _N_ into the surface integrand in a way that doesn’t explicitly
sum over Feynman diagrams. In other words, we need to express _N_ as a tropical function

solely referencing the set of curves _C_ one can draw in the fatgraph that characterizes the

amplitude. This is surprisingly straightforward to do thanks to the stringent constraints that

result from fixing the cubic vertex orientation. Firstly, we need to divide the numerator into
a sum over all 2 _[L]_ possible charge assignments (fermion or scalar) for the internal punctures
in the surface. We denote each configuration by the set of punctures _O_ = _{_ 0 _a_ _∈_ Ψ _}_ (1 _<_
_a < L_ ) chosen to be fermionic. For example, at two-loops, we have the following possibilities:
conf(Ψ0) = _{_ ∅ _, {_ 01 _}, {_ 02 _}, {_ 01 _,_ 02 _}}_ .
If ( _PC_ [(] _[k]_ _ij_ [)][)] _[µ]_ [denotes] [the] [momentum] [associated] [to] [the] [curve] [connecting] [endpoints] _[i, j]_ [in]
the fatgraph (with _k_ being an abstract index to differentiate between the distinct curves that


                   - 10                    

share the same endpoints), then the expression for the numerator factor _N_ that appears in

the loop integrand is given by















_N_ ( _**t**_ ) = ( _−i_ ) _[E]_ ( _iλ_ ) _[V][ −]_ _[N]_ 2 [Ψ] ( _ig_ )



_N_ Ψ

2



 [�]



_PF i_ ( _**t**_ )
_i_ =Ψ [¯]







 _,_ (3.5)






 

_O∈_ conf(Ψ0)



¯Θ _[O]_ ΨΨ [(] _**[t]**_ [)] 


_P_ tr _a_ ( _**t**_ )

_a∈O_



where



�( _k_ )



_/P_ ( _k_ )
_Ci_ +1 _,j_ [(] _**[t]**_ [)]








_PF i∈_ Ψext( _**t**_ ) = _v_ ¯( _pi_ ) _P_















 _j_ =Ψ [¯] _,_ Φ _,_ 0 _•_



 _[u]_ [(] _[p][i]_ [+1][)] _[,]_



�( _k_ )



(3.6)



_/P_ ( _k_ )
_C_ 0 _a,j_ [(] _**[t]**_ [)]










_P_ tr _a_ ( _**t**_ ) = _−_ tr _P_












 _j_ =Ψ [¯] _,_ Φ _,_ 0 _b_

_b>a_









 _,_



are path ordered products of tropical functions _/P C_ ( _**t**_ ) corresponding to external fermion lines
and internal closed fermion traces. [4] Here, _N_ Ψ is the number of external fermionic particles,
and _V_ = _n_ +2 _L_ +2 _g_ _−_ 2 is the total number of vertices for an _n_ -point amplitude with _L_ closed
loops. Note the factor of _−_ 1 in the second line of (3.6) corresponding to the sign associated

to closed fermionic loops.
The product inside the first brackets goes over all Ψ [¯] _i_ Ψ _i_ +1 pairs that form an external
fermion line, while the product inside the second brackets goes over all fermionic internal
punctures 0 _a_ _∈O_ for each configuration. To avoid counting cones that include curves connecting two fermions (which are not allowed by the vertex ordering), we include a function


        ¯Θ _[O]_ ΨΨ [(] _**[t]**_ [) =] (1 _−_ Θ _Cij_ ) _,_ (3.7)

_i,j_ =Ψ


where the external fermions and fermionic punctures in _O_ are included in the product above.

The tropical slashed momenta are defined as



_/P C_ ( _**t**_ ) =




- _−_ _[g]_



(3.8)
1 otherwise _._



in any cone that contains _C,_
_λ_ _[/P][ C]_



Explicitly, one can write this in terms of the tropical step functions introduced in [3]



_/P C_ ( _**t**_ ) = _−_ _[g]_




_[g]_ - _−_ _[g]_

_λ_ _[/P][ C]_ [Θ] _[C]_ [(] _**[t]**_ [) +][ 1][¯Θ] _[C]_ [(] _**[t]**_ [) =][ 1][ +] _λ_




    
_[−]_ [1] Θ _C_ ( _**t**_ ) _._ (3.9)
_λ_ _[/P][ C]_



4We use the following shorthand for the product over curves



�( _k_ )


_j_ = Ψ [¯] _,_ Φ _,_ 0 _b_
_b>a_



= 
_j_ = Ψ [¯] _,_ Φ _,_ 0 _b_
_b>a_




- _,_


_k_







where ( _k_ ) distinguishes distinct curves that share the same endpoints.


                   - 11                    

The factor of _g/λ_ is introduced at the level of the propagators to guarantee the correct

coupling constant scaling on each cone in the Feynman fan. Masses can be incorporated into
the tropical _/P_ -function


_/P C_ ( _**t**_ ) _→_ _/P C_ ( _**t**_ ) + Θ _C_ ( _**t**_ ) _mC,_ (3.10)


where _mC_ _→_ _m_ Ψ if _C_ is a fermionic curve and _m_ Φ otherwise. However, the presence of
an extra term without a gamma matrix makes it hard to find a loop-integrated tropical

formulation of the amplitudes. For this reason, we set all masses to zero in this work.

Both here and in the loop-integrated amplitude, it is important to orient the curve appearing in the momenta _PC_ _[µ]_ [such] [that] [the] [endpoint] [corresponding] [to] [the] [Ψ] [particle] [is] [at]
the beginning. This way, the momentum and charge flows have the same direction, as dictated by the Feynman rules. Finally, the path-ordering operator _P_ arranges the curves inside

each trace factor according to the criteria presented in section 3.2. We stress again that

the ordering of the curves is a completely mechanical procedure that can be done simply by

comparing the paths that each of them follows in the base fatgraph (more specifically, from

their mountainscapes, see figure 5).

Equation (3.5) provides the numerator factor that, once introduced into the loop inte
grand of (3.4), accounts for the fermionic propagators of colored Yukawa theory. We can go

a step further and ask if it’s possible to completely integrate out the loop momenta without

spoiling the curvy formulation of the amplitude. That is, find a tropical formula that only

depends on the _t_ variables spanning the Feynman fan (and external data).

Remarkably, once the numerator is separated according to the different charge configu
rations for the internal punctures, the loop-integrated expression for the amplitude takes a
compact form for each charge assignment _O_ . Explicitly, the result of the integral is the usual

scalar exponential involving the graph Symanzik polynomials, times a numerator prefactor
where the Lorentz tensor dependence is packaged into a determinant of a _|C_ Ψ _| × |C_ Ψ _|_ matrix,
where _|C_ Ψ _|_ is the number of fermionic curves in the assignment (external plus internal)



_A_ = ( _−i_ ) _[E]_ ( _iλ_ ) _[V][ −]_ _[N]_ 2 [Ψ] ( _ig_ )



_N_ Ψ

2






_U_ 0 _[−Z]_ (3.11)

_[.]_
_U_ _[D/]_ [2]



0

_U_ _[−Z]_











_F_ 0

_U_

 _[e]_




 - d _[E]_ _**t**_
_×_
MCG







 [�] _P_ Γ _i_

_i_ =Ψ [¯]



��

_P_ tr [(Γ)] _a_
_a∈O_










 

_O∈_ conf(Ψ0)



¯Θ _[O]_ ΨΨ [(] _**[t]**_ [)]



det Ω _O_



Here, we suppress the dependence on _**t**_ in the integrand above so that it fits on one line. We
also introduce the following shorthands for the gamma matrix versions of _PF_ and _P_ tr



�( _k_ )






_[,]_
 _[u]_ [(] _[p][i]_ [+1][)]



_P_ Γ _i∈_ Ψext( _**t**_ ) = _v_ ¯( _pi_ ) _P_













[ _γi_ [(] +1 _[k]_ [)] _,j_ [(] _**[t]**_ [)]] _[µ][C]_
_j_ =Ψ [¯] _,_ Φ _,_ 0 _•_











�( _k_ )



(3.12)




[ _γ_ 0 [(] _[k]_ _a_ [)] _,j_ [(] _**[t]**_ [)]] _[µ][C]_










 _,_



_P_ tr [(Γ)] _a_ [(] _**[t]**_ [) =] _[ −]_ [tr]



 _P_










 _j_ =Ψ [¯] _,_ Φ _,_ 0 _b_

_b>a_


 - 12 







where the tropical gamma matrices are




[ _γC_ ( _**t**_ )] _[µ][C]_ = _−_ _[g]_




    
_[−]_ [1] Θ _C_ ( _**t**_ ) _._ (3.13)
_λ_ _[γ][µ][C]_




_[g]_ - _−_ _[g]_

_λ_ _[γ][µ][C]_ [Θ] _[C]_ [(] _**[t]**_ [) +][ 1][¯Θ] _[C]_ [(] _**[t]**_ [) =][ 1][ +] _λ_



In other words, [ _γC_ ( _**t**_ )] _[µ][C]_ is a Dirac matrix in the cones where the curve _C_ lights up, and the
identity matrix in every other case. We also define a special determinant that produces the

loop-integrated tensor structures



(det Ω _O_ )( _**t**_ ) _._ (3.14)

����� _ωC_ =0







(det Ω _O_ )( _**t**_ ) =



��


_C_ =Ψ



_∂_
_∂ωC_



A more precise definition of Ωwill be given below.
The functions _U,_ _F_ 0 and _Z_ are the usual graph Symanzik polynomials, which can be
defined in terms of the external kinematics and the headlight functions _αC_ ( _**t**_ ) of each curve.
Considering that the momentum associated to a certain curve _C_ can be decomposed as a

loop-dependent and a non-loop-dependent part



_PC_ _[µ]_ [=] _[ K]_ _C_ _[µ]_ [+]


the Symanzik polynomials are given by



_L_


_lC_ _[a]_ _[l]_ _a_ _[µ][,]_ _lC_ _[a]_ _[∈]_ [Z] _[,]_ (3.15)
_a_ =1



_U_ = det Λ _,_ _F_ 0 = _J_ _[T]_ [ ˜] Λ _J,_ _Z_ = 


_KC_ [2] _[α][C][,]_
_C_



_lC_ _[a]_ _[l]_ _C_ _[b]_ _[α][C][,]_ _J_ _[a,µ]_ =  _C_ _C_




 Λ _[ab]_ =



(3.16)
_lC_ _[a]_ _[K]_ _C_ _[µ]_ _[α][C][,]_
_C_



where Λ [˜] = (det Λ)Λ _[−]_ [1] is the adjugate matrix of Λ. Finally, the numerator structure of the
amplitude is encoded in the _|C_ Ψ _| × |C_ Ψ _|_ matrix Ω, which has the following entries




   -   -   - (3.17)
4 [1] _[ω][C][ω]_ _C_ [ ˜] _lC_ _[a]_ ˜ [(Λ] _[−]_ [1][)] _[ab][l]_ _C_ _[b]_ _η_ _[µ][C]_ _[µ]_ [ ˜] _C_ _,_ _C_ = _C._ [˜]



Ω _CC_ ˜ =









   -    -    -    - ��

 _ωC_ ¯Θ _C_ ( _**t**_ ) + Θ _C_ ( _**t**_ ) _KC_ _[µ][C]_ _−_ [�] _C_ _[′]_ _lC_ _[a]_ _[′]_ [(Λ] _[−]_ [1][)] _[ab][l]_ _C_ _[b]_ _αC′_ ( _**t**_ ) _KC_ _[µ][C][′]_ _,_ _C_ = _C,_ [˜]

       -       -       -       
Θ _C_ ( _**t**_ )Θ _C_ ˜( _**t**_ ) 1 _−_ 4 [1] _[ω][C][ω]_ _C_ [ ˜] _l_ _[a]_ ˜ [(Λ] _[−]_ [1][)] _[ab][l]_ _C_ _[b]_ _η_ _[µ][C]_ _[µ]_ [ ˜] _C_ _,_ _C_ = _C._ [˜]




      Θ _C_ ( _**t**_ )Θ _C_ ˜( _**t**_ ) 1 _−_ 4 [1]



The curves _C,_ _C_ [˜] that enter the matrix are the ones that have a fermionic puncture (either
an external leg or an internal puncture of _O_ for a specific configuration), oriented such that
the Ψ endpoint is at the beginning of the path. The _ωC_ are auxiliary variables associated
with each fermionic curve, which are used to extract the multi-linear term of the determinant
(3.11) by acting with the differential operator [�] _C_ _[∂][ω]_ _C_ [.] [Notice that, for curves joining external]
punctures, _lC_ _[a]_ [= 0] [and] [the] [matrix] [elements] [reduce] [simply] [to] _[K]_ _C_ _[µ]_ [=] _[ P][ µ]_ _C_ [or] _[ω][C]_ [.]
In the following sections, we exemplify how to use this formula to compute partial am
plitudes at several orders in the loop momenta and the ’t Hooft expansion, illustrating the

origin of each term in the expressions (3.5) and (3.11) along the way.


                   - 13                    

**4** **Examplitudes**


Having presented the generic tropical expressions for the numerator factor _N_ and the corresponding partial amplitude _A_ for the theory of colored scalars and fermions at hand, we

now explicitly demonstrate its utility with several examples at both tree and loop level, in

increasing order of complexity.


**4.1** **Trees**


We begin by furnishing certain tree-level examples in our colored Yukawa theory (3.1), showcasing the utility of our tropical numerator formula _N_ ( _**t**_ ) given by (3.5) and highlighting the

several features of the theory (as elucidated in section 3.2) it encapsulates.



2 3 4



n−1



1



**Figure** **6** : The _n_ -point tree-level comb graph.



For computing tree-level partial amplitudes, we choose the _n_ -point comb graph as our

distinguished fatgraph Γ, as shown in figure 6. Such a choice for Γ with end points 1 and

_n_, and with the (clockwise) ordering 123 _. . . n_ allows us to list all the possible curves at tree
level. For each pair of external lines _i, j_, there is a unique curve _Cij_ that connects them. The
paths of such curves and their associated momenta are given by


_Cij_ = _iLyi−_ 1 _RyiRyi_ +1 _. . . Ryj−_ 2 _Lj_ _PCij_ = _pi_ + _pi_ +1 + _· · ·_ + _pj−_ 1 _≡_ _pi,i_ +1 _,...,j−_ 1 _,_


_C_ 1 _j_ = 1 _Ry_ 1 _Ry_ 2 _. . . Ryj−_ 2 _Lj_ _PC_ 1 _j_ = _p_ 1 _,...,j−_ 1 _,_ (4.1)


_Cin_ = _iLyi−_ 1 _RyiRyi_ +1 _. . . Ryn−_ 3 _Rn_ _PCin_ = _pi,...,n−_ 1 _,_


where 1 _<_ _i_ _<_ _j_ _−_ 1 and _j_ _<_ _n_ . Using the curve matrices presented in section 2, one can

compute the associated headlight functions, which are given as


_αij_ ( _**t**_ ) = _f_ [˜] _j−_ 2 _,i_ + _f_ [˜] _j−_ 3 _,i−_ 1 _−_ _f_ [˜] _j−_ 3 _,i −_ _f_ [˜] _j−_ 2 _,i−_ 1 _,_

_α_ 1 _j_ ( _**t**_ ) = _−tj−_ 2 + _f_ [˜] _j−_ 2 _,_ 1 _−_ _f_ [˜] _j−_ 3 _,_ 1 _,_

_αin_ ( _**t**_ ) = _f_ [˜] _n−_ 3 _,i−_ 1 _−_ _f_ [˜] _n−_ 3 _,i_ _,_ (4.2)


with the tropical functions _f_ [˜] _ij_ defined by a reversed ordering compared to the tropical functions _fij_ given in [2] (because our comb graph in figure 6 has the opposite orientation to their
choice):
_f_ ˜ _ij_ ( _**t**_ ) = max(0 _, tj, tj_ + _tj−_ 1 _, . . ., tj_ + _tj−_ 1 + _· · ·_ + _ti_ ) _._ (4.3)


                   - 14                    

Equipped with these definitions, the _n_ -point tree-level partial amplitude with _N_ Ψ _/_ 2
fermion pairs is

               _A_ = d _[n][−]_ [3] _**t**_ _N_ ( _**t**_ ) _e_ _[−][S]_ [(] _**[t]**_ [)] _,_ (4.4)


where the tropical numerator formula (3.5) simplifies drastically to yield



 _._ (4.5)
















_N_ ( _**t**_ ) = ( _−i_ ) _[n][−]_ [3] ( _iλ_ ) _[n][−]_ [2] _[−]_ _[N]_ 2 [Ψ] ( _ig_ )



_N_ Ψ

2





 [�] _v_ ¯( _pi_ ) _P_

_i_ =Ψ [¯]



_/P i_ +1 _,j_ ( _**t**_ )
_j_ =Ψ [¯] _,_ Φ








 _[u]_ [(] _[p][i]_ [+1][)]







The various symbols in the above expression retain their definitions as introduced in section
3.3. [5]


**4.1.1** **Five-point**


Let us now utilize the five-point example as the simplest playground to explore some of

the general features of the colored Yukawa theory at action and to verify that the tropical

numerator formula (4.5) explicitly reproduces the expected Feynman diagrams (cones) of the

fan.
Let us consider the external charge configuration _A_ (Ψ1 _,_ Φ2 _,_ Φ3 _,_ Φ4 _,_ Ψ [¯] 5) involving a single
fermion/anti-fermion pair and three scalars with the indicated cyclic ordering. Now, according
to one of the claims presented in section 3.2, curves _C_ 13 _, C_ 14 should strictly correspond to a
fermionic particle and appear in external fermion traces. Let us see why this should be the

case in our example from a surface perspective. All curves on our base fatgraph Γ have a

fixed charge, which is determined analogously to the momentum assignment procedure:


       _QC_ = _q_ start + _q_ incoming from the left _._ (4.6)


right turns


Imposing charge conversation and the correct ordering at every vertex implies that we are left
with triangles with an ordered set of charges _{−_ 1 _,_ 0 _,_ +1 _}_ . Based on this observation, we see
that curves _C_ 13 _, C_ 14 must strictly be fermionic for this external charge assignment, as shown
in the surface triangulation in figure 7.

Another related claim is that two external marked points which are not fermions are

always connected by scalar curves. Thus, for the arrangement of species we are considering,
curves _C_ 24 _, C_ 25 _, C_ 35 should be scalars. This is another consequence of imposing charge conservation at each vertex - there will also exist triangulations containing uncharged triangles
(i.e., made of only scalar (dotted) curves) corresponding to the Tr�Φ [3][�] vertex in the theory,

an example of which is given in figure 8. For the sake of completion, we present the other

three surface triangulations that contribute to the partial amplitude under study in figure 9.


5We have removed the index _k_ from the tropical momenta, as every curve is uniquely determined by its

endpoints at tree-level.


                   - 15                    

3









Ψ `1`





**Figure** **7** : Triangulation (blue) of the charged disk with fermionic (solid) internal curves

leading to charge conservation at every vertex/triangle and the corresponding dual graph

(red).



4









Ψ `1`





**Figure 8** : Triangulation (blue) of the charged disk with scalar (dotted) internal curves leading

to charge conservation at every vertex/triangle and the corresponding dual graph (red).















Ψ `1` Ψ `1`







Ψ `1`



**Figure** **9** : The remaining surface triangulations contributing to the five-point partial amplitude _A_ (Ψ1 _,_ Φ2 _,_ Φ3 _,_ Φ4 _,_ Ψ [¯] 5).


                   - 16                    

While we have provided a bit of intuition for some of the claims presented in section 3.2

through this example, such features are inherently baked into the tropical numerator formula

(4.5) - it identifies all the fermionic/scalar curves for a given external charge assignment

and churns out the associated fermion trace. For the example at hand, the expression for the

tropical numerator is given by


_N_ ( _**t**_ ) = _igλ_ [2][ �] _v_ ¯( _p_ 5) _P{/P C_ 13( _**t**_ ) _/P C_ 14( _**t**_ ) _}u_ ( _p_ 1)� = _igλ_ [2][ �] _v_ ¯( _p_ 5) _/P C_ 14( _**t**_ ) _/P C_ 13( _**t**_ ) _u_ ( _p_ 1)� _,_ (4.7)


where we have used the universal fermion flow feature to order the curves _C_ 14 _> C_ 13, which
can be read off from the paths using (4.1). Using the relation for the tropical momenta (3.8),

the above expression for the tropical numerator generates the appropriate external fermionic

traces corresponding to the triangulations depicted above in figures 7-9:


_N_ �� _C_ 13 _,C_ 14 [=] _[ ig]_ [3][[¯] _[v]_ [(] _[p]_ [5][)] _[/p]_ 123 _[/p]_ 12 _[u]_ [(] _[p]_ [1][)]] _[,]_ _N_ �� _C_ 13 _,C_ 35 [=] _[ −][ig]_ [2] _[λ]_ [[¯] _[v]_ [(] _[p]_ [5][)] _[/p]_ 12 _[u]_ [(] _[p]_ [1][)]] _[,]_

_N_ �� _C_ 24 _,C_ 25 [=] _[ igλ]_ [2][[¯] _[v]_ [(] _[p]_ [5][)][1] _[u]_ [(] _[p]_ [1][)]] _[,]_ _N_ �� _C_ 14 _,C_ 24 [=] _[ −][ig]_ [2] _[λ]_ [[¯] _[v]_ [(] _[p]_ [5][)] _[/p]_ 123 _[u]_ [(] _[p]_ [1][)]] _[,]_

_N_ �� _C_ 25 _,C_ 35 [=] _[ igλ]_ [2][[¯] _[v]_ [(] _[p]_ [5][)][1] _[u]_ [(] _[p]_ [1][)]] _[ .]_ (4.8)


Constructing the _g_ -vectors and the headlight functions _αC_ for the curves in our example using
(4.2), we can explicitly check that our tropical expressions for the integrand and consequently

the partial amplitude indeed reproduce the five Feynman diagrams in our fan, as shown

in figure 10. Explicitly, after carrying out the integration in curve space we arrive at the

following result for the partial amplitude












          _A_ (Ψ1 _,_ Φ2 _,_ Φ3 _,_ Φ4 _,_ Ψ [¯] 5) = d [2] _**t**_ _N_ ( _**t**_ ) exp




_−_ - _αC_ ( _**t**_ ) _PC_ [2]

_C_




[[¯] _[v]_ [(] _[p]_ [5][)] _[p][/]_ [123] _[p][/]_ [12] _[u]_ [(] _[p]_ [1][)]]
= _ig_ [3]



5) _p/_ 12 _u_ ( _p_ 1)] + _igλ_ [2][ [¯] _[v]_ [(] _[p]_ [5][)] _[u]_ [(] _[p]_ [1][)]]

_p_ [2] 12 _[p]_ [2] 512 _p_ [2] 23 _[p]_ [2] 234




_[p][/]_ [123] _[p][/]_ [12] _[u]_ [(] _[p]_ [1][)]] _−_ _ig_ [2] _λ_ [¯ _v_ ( _p_ 5) _p/_ 12 _u_ ( _p_ 1)]

_p_ [2] 12 _[p]_ [2] 123 _p_ [2] 12 _[p]_ [2] 512



_p_ [2] 23 _[p]_ [2] 234




_−_ _ig_ [2] _λ_ [¯ _v_ ( _p_ 5) _p/_ 123 _u_ ( _p_ 1)]



_._ (4.9)
_p_ [2] 51 _[p]_ [2] 512



) _p/_ 123 _u_ ( _p_ 1)] + _igλ_ [2][ [¯] _[v]_ [(] _[p]_ [5][)] _[u]_ [(] _[p]_ [1][)]]

_p_ [2] 23 _[p]_ [2] 123 _p_ [2] 51 _[p]_ [2] 512



Thus, we see that our tropical formula contains all the correct contributions for this five-point

tree-level partial amplitude in colored Yukawa theory as a single integral over the parameter

space of the Feynman fan.


**4.1.2** **Six-point**


We now turn towards demonstrating a six-point tree example involving three fermionic pairs,
specifically considering the partial amplitude _A_ (Ψ [¯] 1 _,_ Ψ2 _,_ Ψ [¯] 3 _,_ Ψ4 _,_ Ψ [¯] 5 _,_ Ψ6). Due to the single ordering of the Yukawa interaction vertex, the number of diagrams/triangulations contributing

to the partial amplitude is severely limited. As we shall see, there are only four contributing

diagrams, a fact that is exactly reproduced by our tropical numerator formula (4.5). More
over, following the discussion of the previous example, one should convince themselves that
curves _C_ 14 _, C_ 25 _, C_ 36 will be _fermionic_, as they involve only a single external fermion marked


                   - 17                    

#### g35






#### g13















**Figure** **10** : The tree-level Feynman fan for _A_ (Ψ1 _,_ Φ2 _,_ Φ3 _,_ Φ4 _,_ Ψ [¯] 5) in colored Yukawa theory.


point. Meanwhile, curves _C_ 13 _, C_ 15 _, C_ 35 will be _scalar_, as they connect external marked points
which are not fermions. [6] The tropical numerator formula for this example is given by


_N_ ( _**t**_ ) = _iλg_ [3][ �] _v_ ¯( _p_ 1) _/P C_ 25( _**t**_ ) _u_ ( _p_ 2)�� _v_ ¯( _p_ 3) _/P C_ 41( _**t**_ ) _u_ ( _p_ 4)�� _v_ ¯( _p_ 5) _/P C_ 63( _**t**_ ) _u_ ( _p_ 6)� _._ (4.10)


One can easily check that the above formula correctly reproduces the external trace factors

appearing in the contributing cones depicted in figure 11


_N_ �� _C_ 13 _,C_ 14 _,C_ 15 [=] _[ −][ig]_ [4][[¯] _[v]_ [(] _[p]_ [1][)][1] _[u]_ [(] _[p]_ [2][)][¯] _[v]_ [(] _[p]_ [3][)] _[/p]_ 456 _[u]_ [(] _[p]_ [4][)][¯] _[v]_ [(] _[p]_ [5][)][1] _[u]_ [(] _[p]_ [6][)]] _[,]_

_N_ �� _C_ 13 _,C_ 35 _,C_ 36 [=] _[ −][ig]_ [4][[¯] _[v]_ [(] _[p]_ [1][)][1] _[u]_ [(] _[p]_ [2][)][¯] _[v]_ [(] _[p]_ [3][)][1] _[u]_ [(] _[p]_ [4][)][¯] _[v]_ [(] _[p]_ [5][)] _[/p]_ 612 _[u]_ [(] _[p]_ [6][)]] _[,]_

_N_ �� _C_ 15 _,C_ 25 _,C_ 35 [=] _[ −][ig]_ [4][[¯] _[v]_ [(] _[p]_ [1][)] _[/p]_ 234 _[u]_ [(] _[p]_ [2][)][¯] _[v]_ [(] _[p]_ [3][)][1] _[u]_ [(] _[p]_ [4][)][¯] _[v]_ [(] _[p]_ [5][)][1] _[u]_ [(] _[p]_ [6][)]] _[,]_

_N_ �� _C_ 13 _,C_ 15 _,C_ 35 [=] _[ ig]_ [3] _[λ]_ [[¯] _[v]_ [(] _[p]_ [1][)][1] _[u]_ [(] _[p]_ [2][)][¯] _[v]_ [(] _[p]_ [3][)][1] _[u]_ [(] _[p]_ [4][)][¯] _[v]_ [(] _[p]_ [5][)][1] _[u]_ [(] _[p]_ [6][)]] _[.]_ (4.11)


Having worked out five-point and six-point examples explicitly to demonstrate that the trop
ical numerator formula generates the desired Feynman diagrams at tree level, it is clear that

one can proceed in an analogous manner to work out partial amplitudes at any multiplicity.


6The remaining curves, namely _C_ 24 _, C_ 26 _, C_ 46, connect fermion marked points; consequently they do not
contribute to the tropical formula and don’t appear in valid triangulations for this amplitude.


                   - 18                    

Ψ `4`





Ψ `4`













Ψ `1` Ψ `1`





Ψ `4`





**Figure** **11** : Surface triangulations of the charged disk with six marked points contributing
to the partial amplitude _A_ (Ψ [¯] 1 _,_ Ψ2 _,_ Ψ [¯] 3 _,_ Ψ4 _,_ Ψ [¯] 5 _,_ Ψ6).


**4.2** **One-loop**


In this section, we describe how the general formulas (3.5) and (3.11) simplify at one-loop,

which we illustrate in sections 4.2.1 and 4.2.2 with the planar two- and four-point amplitudes.

Lastly, in section 4.2.3, we compute the non-planar three-point amplitude.

At one loop, the curve integral formula for the amplitude simplifies to


              -              - d _[D]_ _ℓ_
_A_ = d _[E]_ _**t**_ _[N]_ [(] _**[t]**_ [)] _[e][−][S]_ [(] _**[t]**_ [)] _[,]_ (4.12)
_iπ_ _[D/]_ [2]


where, for the numerator factor, there are two charge configurations corresponding to whether
the internal puncture is a scalar ( _O_ = ∅) or a fermion ( _O_ = _{_ 0 _}_ )



 _._ (4.13)









- _/P_ [(] 0 _[k]_ _,j_ [)]

_j_ =Ψ [¯] _,_ Φ



















_N_ ( _**t**_ ) = ( _−i_ ) _[E]_ ( _iλ_ ) _[V][ −]_ _[N]_ 2 [Ψ] ( _ig_ )



_N_ Ψ

2





 [�] _PF i_

_i_ =Ψ [¯]



¯Θ [∅] ΨΨ _[−]_ [¯Θ] ΨΨ [0] [tr]











 _P_



�( _k_ )











Note that there is no MCG at planar one loop, and we have dropped the dependence on _**t**_ in

the integrand. After performing the loop-momentum integration, one arrives at an expression


                   - 19                    

```
1 2

```




**Figure** **12** : Base fatgraph for the two-point amplitude.


with two contributions: one for diagrams with an internal fermion trace and one without:







0

_U_ _[−Z]_





 [�] _P_ Γ _i_

_i_ =Ψ [¯]



_F_ 0

 -  - _e_ _U_
 ¯Θ [∅] ΨΨ [det Ω][∅] _[−]_ [¯Θ] ΨΨ [0] _[P]_ [tr][(Γ)] 0 det Ω0




_[.]_
_U_ _[D/]_ [2]



_A_ = ( _−i_ ) _[E]_ ( _iλ_ ) _[V][ −]_ _[N]_ 2 [Ψ] ( _ig_ )



_N_ Ψ 
2 d _[E]_ _**t**_



(4.14)


**4.2.1** **Planar** **two-point**


We choose the wheel topology for the base fatgraph for the planar one-loop two-point ampli
tude (see figure 12). There are a total of four non-boundary curves on this fatgraph:


_C_ 10 = 1 _Ry_ 2( _Ly_ 1 _Ly_ 2) _[∞]_ _,_ _C_ 20 = 2 _Ry_ 1( _Ly_ 2 _Ly_ 1) _[∞]_ _,_

(4.15)
_C_ 11 = 1 _Ly_ 1 _Ry_ 2 _L_ 1 _,_ _C_ 22 = 2 _Ly_ 2 _Ry_ 1 _L_ 2 _._


The momentum associated to each curve is


_PC_ 10 = _ℓ,_ _PC_ 20 = _ℓ_ _−_ _p_ 1 _,_ _PC_ 11 = _p_ 12 = 0 _,_ _PC_ 22 = _p_ 12 = 0 _._ (4.16)


With this, we have all the pieces needed to use (4.13) for various choices of external particles.


**Example:** **two** **fermions.** For 1 = Ψ [¯] and 2 = Ψ, the one-loop integrand becomes


_N_ ( _**t**_ ) = _λg_     - _v_ ¯( _p_ 1) _/P C_ 20( _**t**_ ) _u_ ( _p_ 2)��¯Θ22( _**t**_ ) _−_ ¯Θ0ΨΨ [(] _**[t]**_ [) tr]     - _/P C_ 01( _**t**_ )�� _,_ (4.17)

where Θ [¯] [∅] ΨΨ [=] [¯Θ][22][.] [Note] [that] [the] [path] [ordering] [is] [not] [necessary] [in] [this] [example] [because] [one]
never encounters more than one _/P C_ in a fermion line. To verify that this integrand produces
the expected Feynman integrals, we pull it back to the cones in the Feynman fan (see figure

13). On the Feynman cones, the integrand becomes



_N_ ( _**t**_ ) _|_ tad = _g_ (¯ _v_ ( _p_ 1) _u_ ( _p_ 2)) - _λ −_ _g_ tr - _/ℓ_ �� =


_N_ ( _**t**_ ) _|_ tad _′_ = 0 _,_


                  - 20                   


(4.18)



+



_,_


```
2

```











|Col1|2|Col3|Col4|
|---|---|---|---|
|||||
|||||
||C11|||


|Col1|Col2|2|Col4|
|---|---|---|---|
|||C22|C22|
|||||
|||||


```
     1 1 1

```

**Figure** **13** : Triangulations of the two-point wheel surface in blue. Each triangulation is a

cone in the Feynman fan. The dual (Feynman) graph associated to each triangulation is

shown in red: a bubble and two tadpoles. The non-boundary curves have also been labeled.



where the above equalities hold at the level of the loop-momentum numerators. We have
used the fact that Θ [¯] [0] ΨΨ [vanishes] [on] [the] [bubble] [cone] [while] [both] [¯Θ][∅] ΨΨ [and] [¯Θ][0] ΨΨ [vanish] [on] [the]
last tadpole cone in figure 13.

Either working directly from the Feynman diagrams or (4.13), the loop-integrated bubble

with numerator evaluates to

   - d _[D]_ _ℓ_   -   - _α_ 1 _e_ _[F]_ [bub] _[/][U]_ [bub]
_iπ_ _[D/]_ [2] d _[E]_ _**t**_ _N_ ( _**t**_ ) _e_ _[−][S]_ ���� = _g_ [2] _v_ ¯( _p_ 1) _/p_ 1 _u_ ( _p_ 2) d [2] _α_ _α_ 1 + _α_ 2 _[D/]_ [2] _,_ (4.19)




- - _α_ 1
d _[E]_ _**t**_ _N_ ( _**t**_ ) _e_ _[−][S]_ ����bub = _g_ [2] _v_ ¯( _p_ 1) _/p_ 1 _u_ ( _p_ 2) d [2] _α_ _α_ 1 + _α_ 2



_e_ _[F]_ [bub] _[/][U]_ [bub]



_,_ (4.19)
_U_ bub _[D/]_ [2]



where _α_ 1 = _αC_ 10 _|_ bub, _α_ 2 = _αC_ 20 _|_ bub, _U_ bub = _α_ 1 + _α_ 2 and _F_ bub = _−α_ 1 _α_ 2 _p_ [2] 1 [.] Next, we
illustrate how to get the above loop-integrated expression directly from the combinatorial

formula (4.14).
When the internal puncture is fermionic, _O_ = _{_ 0 _}_, there is one fermionic curve: _C_ 01 ( _C_ 20
is not allowed because it connects two fermions). In this case, Ω0 is the 1 _×_ 1 matrix







(Ω0) _C_ 01 _C_ 01 = _ωC_ 01



�¯Θ _C_ 01( _**t**_ ) + Θ _C_ 01( _**t**_ ) _αC_ 20( _**t**_ _U_ ) _KCµC_ 2001



_,_ (4.20)



Here, only _KC_ _[µ]_ 20 [=] _[−][p]_ [1] [is] [non-vanishing] [(] _[K]_ _C_ _[µ]_ 01 [=] _[K]_ _C_ _[µ]_ 11 [=] _[K]_ _C_ _[µ]_ 22 [=] [0).] [Moreover,] [note] [that]
in (3.17), the sum over _C_ _[′]_ includes _all_ curves, not just the fermionic ones. For the charge
configuration _O_ = ∅, the only fermionic curve is _C_ 20 and Ω∅ is also a 1 _×_ 1 matrix







(Ω∅) _C_ 20 _C_ 20 = _ωC_ 20



�¯Θ _C_ 20( _**t**_ ) + Θ _C_ 20( _**t**_ ) _αC_ 01( _**t**_ _U_ ) _KCµC_ 2020



_._ (4.21)



Specifying (4.14) to our example, one finds that only the charge configuration _O_ = ∅

contributes on the bubble cone; thus



_F_ 0

       -        -        - _U_
_A|_ bub = _−_ ( _iλ_ )( _ig_ ) d _[E]_ _**t**_ _v_ ¯( _p_ 1)[ _γC_ 20( _**t**_ )] _[µ][C]_ [20] _u_ ( _p_ 2) det Ω∅( _**t**_ ) _[e]_



0

_U_ _[−Z]_



_,_
����bub



_U_ _[D/]_ [2]




       - _α_ 1
= _g_ [2] _v_ ¯( _p_ 1) _/p_ 1 _u_ ( _p_ 2) d [2] _α_ _α_ 1 + _α_ 2


            - 21             


_e_ _[F]_ [bub] _[/][U]_ [bub]

_,_ (4.22)
_U_ bub _[D/]_ [2]


where

_F_ 0




_[−][α]_ [1] _[α]_ [2] = _[F]_ [bub]

_α_ 1 + _α_ 2 _U_ bub



_,_ (4.23)
_U_ bub



0 _α_ 2 _p_ [2] 1

= _−_ _α_ 2 _p_ [2] 1 [=] _[−][α]_ [1] _[α]_ [2]
_U_ _[−Z]_ ����bub _α_ 1 + _α_ 2 _α_ 1 + _α_



and




[ _γC_ 20( _**t**_ )] _[µ][C]_ [20] det Ω [∅] ( _**t**_ ) _α_ 1 _KCµC_ 2020 = _[α]_ [1] _[/K][C]_ [20] = _−_ _α_ 1 _p/_ 1 _._ (4.24)
���bub [=] _[ γ][µ][C]_ [20] _U_ bub _U_ bub _U_ bub



Comparing to (4.19), we find agreement.


**Example:** **two** **scalars.** The other possible two-point integrand corresponds to 1 = Φ

and 2 = Φ:


_N_ ( _**t**_ ) = _λ_ [2][ �] 1 _−_ tr        - _/P C_ 01( _**t**_ ) _/P C_ 02( _**t**_ )�� _,_ (4.25)

where Θ _[O]_ ΨΨ [= 1] _[∀]_ _**[t]**_ _[ ∈]_ [R][2] [since] [there] [are] [no] [external] [fermions.] [Again,] [the] [path] [ordering] [does]
not matter in this example because the trace is cyclic invariant. Pulling back the integrand

to the Feynman cones, we find the usual sum over Feynman diagrams with



_N_ ( _**t**_ ) _|_ tad =


_N_ ( _**t**_ ) _|_ tad _′_ =



Φ1 Φ2


Φ1 Φ2



+


+



Φ1 Φ2


_,_


_,_


Φ1 Φ2



(4.26)



where the above equalities hold at the level of the numerator of the momentum space inte
grand.

Since there are no external fermions, Ω∅ = 1. When the puncture is fermionic there are
two internal fermionic curves: _C_ 01 and _C_ 02. Therefore,

(Ω0) _C_ 01 _C_ 01 _|_ bub = _−ωC_ 01 _α_ 2 _UK_ bub _CµC_ 0201 _,_



(Ω0) _C_ 02 _C_ 02 _|_ bub = _ωC_ 02 _α_ 1 _UK_ bub _CµC_ 0202 _,_



(4.27)




_[ω][C]_ [02] _η_ _[µ][C]_ [01] _[µ][C]_ [02]

4 _U_ bub



(Ω0) _C_ 01 _C_ 02 _|_ bub = 1 _−_ _[ω][C]_ [01] _[ω][C]_ [02]



_._
_U_ bub



On the bubble cone, the amplitude becomes











 _[e][F]_ [bub] _[/][U]_ [bub]



_._ (4.28)
_U_ bub _[D/]_ [2]








             
_[g]_ [2] _U_ bub tr[ _γ_ _[µ]_ _γµ_ ] _−_ 2 _α_ 1 _α_ 2 tr _[p]_ _/_ 1 _[p]_ _/_ 1

_λ_ [2] 2 _U_ [2]



2 _U_ bub [2]




     _A|_ bub = _λ_ [2] d _[E]_ _**t**_



1 _−_ _[g]_ [2]




- 22 

`2` y2 `3`



y1



y3


```
1

```


y4


ℓ


```
4

```


**Figure** **14** : The one-loop four-point base fatgraph.


Here, the first term is clearly recognizable as the Tr(Φ [3] ) bubble while the second term is the

bubble with a fermion trace.


**4.2.2** **Planar** **four-point**


The four-point wheel fatgraph (figure 14) has a total of 35 triangulation or cones. Due to

the large number of cones, we only present a check of our tropical formula for the box and

triangle cones shown in figure 15. Furthermore, we will only consider the amplitude with two
fermions and two scalars: _A_ (Ψ [¯] 1 _,_ Ψ2 _,_ Φ3 _,_ Φ4).
To determine the integrand numerator, only the words for the non-boundary curves
connected to the puncture or the fermion Ψ2 are needed:


_C_ 10 = 1 _R_ ( _y_ 4 _Ly_ 3 _Ly_ 2 _Ly_ 1 _L_ ) _[∞]_ _,_ _C_ 20 = 2 _R_ ( _y_ 1 _Ly_ 4 _Ly_ 3 _Ly_ 2 _L_ ) _[∞]_ _,_



_C_ 30 = 3 _R_ ( _y_ 2 _Ly_ 1 _Ly_ 4 _Ly_ 3 _L_ ) _[∞]_ _,_ _C_ 40 = 4 _R_ ( _y_ 3 _Ly_ 2 _Ly_ 1 _Ly_ 4 _L_ ) _[∞]_ _,_

_C_ 24 [cc] [= 2] _[Ry]_ [1] _[Ly]_ [4] _[R]_ [4] _[,]_ _C_ 24 = 2 _Ly_ 2 _Ry_ 3 _Ly_ 4 _,_

_C_ 21 = 2 _Ly_ 2 _Ry_ 3 _Ry_ 4 _L_ 1 _,_ _C_ 23 [cc] [= 2] _[Ry]_ [1] _[Ly]_ [4] _[Ly]_ [3] _[R]_ [3] _[ .]_



(4.29)



Here, the superscript “cc” on a curve _Cij_ [cc] [indicates] [that] [the] [curve] [travels] [from] [starting] [point]
_i_ to endpoint _j_ in a counterclockwise manner (i.e. passing the puncture from the right). This

is the first instance of the superscript ( _k_ ) in the formulae (3.6) and (3.12). The momenta

associated to each curve are


_PC_ 10 = _ℓ,_ _PC_ 20 = _ℓ_ _−_ _p_ 1 _,_ _PC_ 30 = _ℓ_ _−_ _p_ 12 _,_ _PC_ 40 = _ℓ_ + _p_ 4 _,_ (4.30)

_PC_ 24 [cc] [=] _[ −][p]_ [23] _[,]_ _PC_ 24 = _p_ 23 _,_ _PC_ 23 [cc] [=] _[ p]_ [2] _[,]_ _PC_ 21 = _p_ 234 _._


With this we have enough data to evaluate the tropical integrand


                            _N_ ( _**t**_ ) = _gλ_ [3] [�] _v_ ¯( _p_ 1) _/P C_ 24cc [(] _**[t]**_ [)] _[/P][ C]_ 23 [cc] [(] _**[t]**_ [)] _[/P][ C]_ [20][(] _**[t]**_ [)] _[/P][ C]_ [21][(] _**[t]**_ [)] _[/P][ C]_ [24][(] _**[t]**_ [)] _[u]_ [(] _[p]_ [2][)]

(4.31)
_×_ �¯Θ∅ΨΨ [(] _**[t]**_ [)] _[ −]_ [¯Θ] ΨΨ [0] [(] _**[t]**_ [) tr]        - _/P C_ 03( _**t**_ ) _/P C_ 04( _**t**_ ) _/P C_ 01( _**t**_ )�� _._


Unlike the two-point example, the path ordering is important in this case. Examination of
the words (4.29) reveals that _C_ 24 [cc][,] _[C]_ 23 [cc] [and] _[C]_ [20] [turn] [right] [immediately,] [while] _[C]_ [24] [and] _[C]_ [21]
turn left first. Thus, _C_ 24 and _C_ 21 appear at the end of the fermion line. Furthermore, since


                   - 23                    

```
3

```

```
3

```

```
3

```

```
2

```

```
2

```

```
2

```

```
4

```

```
4

```

```
4

```

```
1

```

```
1

```

```
1

```

```
3

```

```
3

```

```
2

```

```
2

```

```
4

```

```
4

```

```
1

```

```
1

```


**Figure** **15** : Some of the Feynman cones at one-loop and four points. The curves that

triangulate the dual surface are depicted in blue and the corresponding Feynman graphs in

red.


_C_ 21 turns right before _C_ 24 it must come first: _• < C_ 21 _< C_ 24. While _C_ 24 [cc][,] _[C]_ 23 [cc] [and] _[C]_ [20] [share]
the same first right turn, _C_ 20 does not turn right again which means that it must appear after
_C_ 24 [cc] [and] _[C]_ 23 [cc][:] _[•][ < C]_ [20] _[< C]_ [21] _[< C]_ [24][.] [Comparing] [the] [final] [two] [curves] [fixes] [the] [ordering] [of] [the]
curves in the external fermion line to be


_C_ 24 [cc] _[< C]_ 23 [cc] _[< C]_ [20] _[< C]_ [21] _[< C]_ [24] _[.]_ (4.32)


The ordering of the curves in the internal fermion trace is determined by the same rule but

differs somewhat due to the fact there is no natural starting point for the closed fermion
trace. Picking _y_ 1 as the starting road and expanding the words for the curves appearing in
the fermion trace gives


_C_ 01 = ( _Ry_ 1 _Ry_ 2 _Ry_ 3 _Ry_ 4) _[∞]_ _Ry_ 1 _Ry_ 2 _Ry_ 3 _Ry_ 4 _L_ 1 _,_



_C_ 03 = ( _Ry_ 3 _Ry_ 4 _Ry_ 1 _Ry_ 2) _[∞]_ _Ry_ 3 _Ry_ 4 _Ry_ 1 _Ry_ 2 _L_ 3 _,_

_C_ 04 = ( _Ry_ 4 _Ry_ 1 _Ry_ 2 _Ry_ 3) _[∞]_ _Ry_ 4 _Ry_ 1 _Ry_ 2 _Ry_ 3 _L_ 4 _,_



(4.33)



where we see that _C_ 01 turns right first followed by _C_ 04 and then _C_ 03. Thus, the curves in the
closed fermion loop are ordered according to _C_ 01 _< C_ 04 _< C_ 03.
It is easy to verify that the numerator (4.31) evaluates to the expected Feynman inte
grands. For illustrative purposes, we show the evaluation of this numerator on the box and


                   - 24                    

second triangle cone of figure 15


_N_ ( _**t**_ ) _|_ box = _−λ_ [2] _g_ [2][ �] _v_ ¯( _p_ 1) _/P C_ 20 _u_ ( _p_ 2)� =



Ψ2


Ψ `¯` 1



Φ3


Φ4



_,_ (4.34)




        
                    -                    - [�]

_N_ ( _**t**_ ) _|_ tri2 = _λ_ [3] _g_ _v_ ¯( _p_ 1) _u_ ( _p_ 2) 1 + _[g]_ [3] [tr] _/P C_ 01 _/P C_ 04 _/P C_ 03 _,_

_λ_ [3]



Ψ2 Φ3



Ψ2 Φ3



_,_ (4.35)



=



+



Ψ `¯` 1



Φ4



Ψ `¯` 1



Φ4



where the above equalities are at the level of the momentum space numerator of the integrand

rather than the full integral.

Lastly, for completeness, we provide the relevant matrix elements of Ωon the box and

second triangle cones:







(Ω∅) _C_ 20 _C_ 20 _|_ box = _ωC_ 02


(Ω0) _C_ 0 _iC_ 0 _i|_ tri2 = _ωC_ 0 _i_




- _KCµC_ 2020 _−_ _α_ 1 _KCµC_ 1010 + _α_ 2 _KCµC_ 2020 _U_ +box _α_ 3 _KCµC_ 3030 + _α_ 4 _KCµC_ 4040




- _µC_ 0 _i_ _α_ 1 _KCµC_ 010 _i_ [+] _[ α]_ [3] _[K]_ _CµC_ 030 _i_ [+] _[ α]_ [4] _[K]_ _CµC_ 040 _i_

_KC_ 0 _i_ _−_ _U_ tri2



_,_ (4.36)







_,_ (4.37)



_η_ _[µ][C]_ [0] _[i]_ _[µ][C]_ [0] _[j]_
(Ω0) _C_ 0 _iC_ 0 _j_ _|_ tri2 = 1 _−_ _ωC_ 0 _iωC_ 0 _j_ 4 _,_ (4.38)



where _i, j_ = 1 _,_ 3 _,_ 4, _U_ box = _α_ 1 + _α_ 2 + _α_ 3 + _α_ 4, _U_ tri2 = _α_ 1 + _α_ 3 + _α_ 4. Other matrix elements
either vanish or are simply equal to the variable _ωC_ in these cones. Note that, in general, one
needs to account for the fact that _ℓC_ 0 _i_ = _−ℓCi_ 0. We also remind the reader that _KC_ 10 = 0,
_KC_ 20 = _−p_ 2, _KC_ 30 = _−p_ 12 and _KC_ 40 = _p_ 4.


**4.2.3** **Non-planar** **three-point**


In this section we check how our formalism works for a non-planar example: _A_ (Ψ [¯] 1 _,_ Ψ2 _|_ Φ3).
Here the vertical bar indicates that the two fermionic particles belong to a separate color

trace than the scalar. For the base fatgraph we choose the topology depicted in figure 16.

There are four types of non-boundary curves that can be drawn on this fatgraph: the ones

connecting leg 1 to leg 3, the ones connecting leg 2 to leg 3, and the ones connecting legs 1
and 2 to themselves. From those, we need to discard the curves of the form _C_ 22, since those
would give rise to Feynman diagrams with the wrong vertex ordering (there cannot be curves

with two fermions Ψ as endpoints).


                   - 25                    

**Figure** **16** : Choice of base fatgraph for the non-planar three-point amplitude.


Moreover, it is easy to see that we can draw an infinite number of distinct curves _C_ 13 _, C_ 23,
by circling around the loop an arbitrary number of times before exiting on leg 3. This leads to

an overcounting of Feynman diagrams, which is a manifestation of the action of the _Mapping_

_Class_ _Group_ (MCG) [1]. In order to arrive at the correct expression for the amplitude, we

need to mod out by the action of this group. This is done with the help of the Mirzakhani
kernel _K_, which restricts the integration to the fundamental domain of the Feynman fan.

In order to compute it, we start by identifying the single non-trivial closed curve that

generates the MCG on the surface in figure 16:


∆= _y_ 1 _Ly_ 2 _Ry_ 3 _R ._ (4.39)


Since ∆only intersects curves of the form _C_ 13 and _C_ 23, those are the only ones that are not
invariant under the action of the corresponding Dehn twists _γ_ ∆. Thus, we need to choose one
representative for each coset, which we choose to be


_C_ 13 [0] [= 1] _[Ly]_ [1] _[R]_ [3] _[,]_ _C_ 23 [0] [= 2] _[Ry]_ [2] _[L]_ [3] _[ .]_ (4.40)


Acting on these with Dehn twists _γ_ ∆ generates different curves, for example


_C_ 13 [1] _[≡]_ _[γ]_ [∆][(] _[C]_ 13 [0] [) = 1] _[Ly]_ [1] _[Ly]_ [2] _[Ry]_ [3] _[Ry]_ [1] _[R]_ [3] _[,]_ _C_ 23 [1] _[≡]_ _[γ]_ [∆][(] _[C]_ 23 [0] [) = 2] _[Ly]_ [3] _[Ry]_ [1] _[R]_ [3] _[.]_ (4.41)


The Mirzakhani kernel is then given by


13 [+] _[ α]_ 23 [0]
_K_ = _[α]_ [0] _,_ (4.42)
_ρ_


where _ρ_ is a sum over all curves _C_ 13 _, C_ 23 that are contained in the set _S_ of paths compatible
with our coset representatives:




 _ρ_ =




- 
_αC_ 13 +
_C_ 13 _∈S_ _C_ 23



_αC_ 23 _._ (4.43)
_C_ 23 _∈S_



We find there are 7 curves that are compatible on the support of this Mirzakhani kernel: _C_ 13 _[n]_ [,]
_C_ 23 _[n]_ [,] [and] _[C]_ [11] [with] _[n]_ _[∈{−]_ [1] _[,]_ [ 0] _[,]_ [ +1] _[}]_ [.] [Out] [of] [these,] [only] _[C]_ 23 _[n]_ [are] [fermionic] [and] [appear] [inside]
the external fermion trace connecting particles 1 and 2 (there are no closed fermion loops, as

there are no internal punctures in the surface).


                   - 26                    

```
1 2

```






**Figure** **17** : Feynman diagrams appearing for the non-planar three-point amplitude.


Explicitly, the tropical numerator becomes


_N_ = _λ_ [2] _g_ Θ [¯] _C_ 22( _**t**_ )¯ _v_ ( _p_ 1) _/P C_ 23 _−_ 1 [(] _**[t]**_ [)] _[/P][ C]_ 23 [0] [(] _**[t]**_ [)] _[/P][ C]_ 23 [1] [(] _**[t]**_ [)] _[u]_ [(] _[p]_ [2][)] _[ .]_ (4.44)


We can go one step further and integrate out the loop momentum. Since there are no potential

closed fermion loops, there is only one possible tropical tensor structure in the numerator,
which is given by the 3 _×_ 3 matrix with entries described in (3.17):



_,_







��



_KC_ _[µ][n]_ 23 _n_ _[−]_ [1]



_U_





_αC_ 23 _KC_ _[µ][n]_ 23
_C_ 23 _∈S_




- [��]



(Ω∅) _nn_ = _ωn_




¯Θ _C_ 23 _n_ [(] _**[t]**_ [)+Θ] _[C]_ 23 _[n]_ [(] _**[t]**_ [)]




   _αC_ 13 _KC_ _[µ][n]_ 13 [+]
_C_ 13 _∈S_ _C_ 23








   
_[n][ω][m]_

_η_ _[µ][n][µ][m]_
4 _U_



_,_ (4.45)



(Ω∅) _nm_ = Θ _C_ 23 _[n]_ [(] _**[t]**_ [)Θ] _[C]_ 23 _[m]_ [(] _**[t]**_ [)]



1 _−_ _[ω][n][ω][m]_



where _m_ = _n_ . Above, we have condensed the notation by using the indices _n, m_ to indicate
the instance of the curve _C_ 23 _[n]_ [,] [since] [those] [are] [the] [only] [ones] [that] [appear] [in] [the] [open] [fermion]
line. As we saw in the other one-loop examples, the first Symanzik polynomial takes the

simple form

      -      _U_ = _αC_ + _αC_ (4.46)




- 
_αC_ 13+
_C_ 13 _∈S_ _C_ 23 _∈S_



_αC_ 23 _._ (4.46)
_C_ 23 _∈S_



Expanding the determinant of the matrix Ω∅ and taking the coefficient of the monomial
_ω−_ 1 _ω_ 0 _ω_ 1 yields all the possible tensor contractions after loop integration. Integrating over
the Feynman fan by substituting the explicit expressions for the headlight and step functions
_αC,_ Θ _C_, we find the sum over all possible Feynman diagrams: the three different topologies
are depicted in figure 17.


**4.3** **Planar** **two-loop** **two-point**


In this section we present our final example: the two-loop two-point planar amplitude.

We start by choosing the base fatgraph of figure 18. This choice is especially useful since

one can recycle previous quantities via tree-loop factorization [2]. For example, all of the nec
essary surfaceology calculations (headlight functions, Symanzik polynomials, etc.) for higher

point two-loop surfaces share the same loop contributions from the tadpole subdiagrams. It


                   - 27                    

```
            1 2

```

**Figure** **18** : Choice of base fatgraph for the planar two-loop two-point amplitude. This

fatgraph is obtained by gluing one of the legs of a three-point tree with a two-loop tadpole

fatgraph and is particularly convenient for enumerating the curves.


is also easy to adapt the tree-level part by adding more external legs to the comb fatgraph of

section 4.1.

For this surface there are three main types of curves: the ones that start at an external

leg and end in a spiral around one of the loops, the ones that start and end at an external leg,

and the ones that start and end spiraling. Taking into account that particle 2 is a fermion

Ψ, we ignore every curve that connects leg 2 to itself since they lead to Feynman diagrams

with the wrong vertex ordering.

Like in section 4.2.3, we also need to quotient out by the action of the mapping class

group for surfaces with two punctures. Indeed, the tadpole subdiagram can be traversed by

one non-trivial closed curve ∆that loops around both internal punctures


∆= _ybRxbRybRyaRxaRyaL ._ (4.47)


Since ∆intersects the curves that start at an external leg and end spiraling, this subset

transforms non-trivially under the action of the MCG. All other curves are invariant under

the MCG action since these curves do not intersect ∆.
In other words, there are four MCG cosets, represented by curves of the form _C_ 10 _a_, _C_ 20 _a_,
_C_ 10 _b_ and _C_ 20 _b_ . To mod out by the action of the group, we need to identify one representative
curve for each coset. We choose the shortest paths ending on a counterclockwise spiral

_C_ 10 [0] _a_ [= 1] _[RzLy][a][R]_ [(] _[x][a][L]_ [)] _[∞]_ _[,]_ _C_ 20 [0] _a_ [= 2] _[LzLy][a][R]_ [(] _[x][a][L]_ [)] _[∞]_ _[,]_

(4.48)
_C_ 10 [0] _b_ [= 1] _[RzRy][b][R]_ [(] _[x][b][L]_ [)] _[∞]_ _[,]_ _C_ 20 [0] _b_ [= 2] _[LzRy][b][R]_ [(] _[x][b][L]_ [)] _[∞]_ _[.]_

Acting with Dehn twists _γ_ ∆ on these curves generates all curves not invariant under the
MCG. For example

_C_ 10 [1] _a_ _[≡]_ _[γ]_ [∆][(] _[C]_ [10] _a_ [) = 1] _[RzRy][b][Rx][b][Ry][b][Ry][a][R]_ [(] _[x][a][L]_ [)] _[∞]_ _[.]_ (4.49)


The Mirzakhani kernel is then the tropical function that quotients out the MCG by selecting

only the curves compatible with our representatives:

10 _a_ [+] _[ α]_ 20 [0] _a_ [+] _[ α]_ 10 [0] _b_ [+] _[ α]_ 20 [0] _b_
_K_ = _[α]_ [0] _._ (4.50)
_ρ_


                   - 28                    

Here, _ρ_ is the sum over all curves that intersect ∆and are compatible with _C_ 1 [0] _a_ [,] _[C]_ 2 [0] _a_ [,] _[C]_ 1 [0] _b_ [and]
_C_ 2 [0] _b_ [(as] [before,] [we] [call] [the] [set] [of] [all] [such] [curves] _[S]_ [):]



_αC_ 20 _b_ _._ (4.51)
_C_ 20 _b_ _∈S_




- 
_αC_ 10 _a_ +
_C_ 10 _a_ _∈S_ _C_ 20 _a_




- 
_αC_ 10 _b_ +
_C_ 10 _b_ _∈S_ _C_ 20 _b_




 _ρ_ =




- 
_αC_ 20 _a_ +
_C_ 20 _a_ _∈S_ _C_ 10



In total, _S_ contains 24 curves compatible with the Mirzakhani kernel that respect the Yukawa

vertex ordering.

Since this amplitude is planar and the internal punctures in a surface don’t carry any

momentum, the kinematic assignments of the curves take a simple form, and are invariant

under the action of the MCG. In particular, we choose the loop parametrization


_PC_ _[µ]_ 10 _a_ [=] _[ l][a][,]_ _[P]_ _C_ _[ µ]_ 20 _a_ [=] _[ l][a][ −]_ _[p,]_ _[P]_ _C_ _[ µ]_ 10 _b_ [=] _[ l][b][,]_ _[P]_ _C_ _[ µ]_ 20 _b_ [=] _[ l][b][ −]_ _[p,]_ (4.52)


where we are referring to arbitrary curves with the indicated endpoints.

For the loop-integrated form of the tropical numerator, we make use of the matrix Λ that

enters in the expression for the Symanzik polynomials (3.16). To determine it, we use the

telescopic property of the headlight functions [2], according to which the expression for the

_α_ ’s of the tadpole subgraph is simply given by the sum over all possible ways to extend them

into the tree diagram. Therefore, we find







Λ =




_α_ 0 _a_ 0 _b_ + _α_ 10 _a_ + _α_ 20 _a_ _−α_ 0 _a_ 0 _b_
_−α_ 0 _a_ 0 _b_ _α_ 0 _a_ 0 _b_ + _α_ 10 _b_ + _α_ 20 _b_



_,_ (4.53)



where

     _αi_ 0 _a_ =



_αCi_ 0 _b_ _,_ _i_ = 1 _,_ 2 _._ (4.54)
_Ci_ 0 _b_ _∈S_




- 
_αCi_ 0 _a_ _,_ _αi_ 0 _b_ =
_Ci_ 0 _a_ _∈S_ _Ci_ 0



As seen in previous examples, one advantage of our formulation for the Yukawa numerator is

that all the tropical objects, such as the headlight functions, do not depend on the species for

the external particles that characterize a specific amplitude. Thus, we can reuse these results

for amplitudes containing different particle species.
Let’s start with the case where the two external legs are fermionic, _A_ (Ψ [¯] 1 _,_ Ψ2). The
charge assignments for each curve are also (partially) fixed thanks to the constraints from
our Yukawa vertex ordering. For instance, curves of the form _C_ 2 _j_ ( _j_ = 1 _, a, b_ ) are always
fermionic and only appear as part of the external fermion line _v_ ¯( _p_ 1) _· · · u_ ( _p_ 2), while curves
connecting leg 1 to itself are scalar. On the other hand, the species of the curves that end on a

spiral and start at either leg 1 or the other spiral depends on the specific charge configuration

that is assigned to the internal punctures. For example, curves that begin/end at a spiral
around a fermionic puncture always appear inside internal Dirac traces tr[ _· · · γ · · ·_ ] as part of

the closed fermion loop.

With this, we can insert the tropical functions into the general formula (3.5) to obtain an

expression for the curve integral numerator of the two-loop two-point amplitude. Localizing

to the different cones in the Feynman fan, we find the expected Feynman diagrams (there are


                   - 29                    

**Figure** **19** : Kite topology for the planar two-loop two-point fermion amplitude.


a total of 52) of our colored Yukawa theory. For example, the cone corresponding to the kite

topology (see figure 19) evaluates to


_N_ ��kite [=] _[ −][ig]_ [3] _[λ][v]_ [¯][(] _[p]_ [1][)] _[/P][ C]_ 20 [0] _b_ _[/P][ C]_ 20 [0] _a_ _[u]_ [(] _[p]_ [2][) + MCG] [perm.] _[,]_ (4.55)


where the rest of the terms arise from considering spiral curves related by the MCG. Each

of these MCG-equivalent curves evaluates to the same expression once the physical value for
the curve momenta _PC_ is substituted. This overcounting is compensated by the Mirzakhani
kernel.

Let’s also explicitly write the loop-integrated expression for this Feynman diagram by

evaluating our formula (3.11) on the respective cones. By inserting the expression for Λ

into the matrix (3.17) and evaluating on particular cones, we obtain the tensor structure

that arises after integrating out the loop momenta in terms of the curve integral variables.

However, it is also important to note that specific Feynman diagrams are associated to only
one of the 2 _[L]_ (in this case, four) possible charge assignments for the internal punctures.
For the kite diagram, both punctures _a_ and _b_ are scalar ( _O_ = ∅), which is reflected by

the fact that there are no closed fermion lines. Localizing to its cone, we see that the curves
that don’t appear reduce to trivial factors of _ωC_ on the diagonal of the tensor matrix, while
the non-trivial minor is given by







(Ω∅) _aa_ _→ω_ 20 _a_



_KC_ _[µ][a]_ 20 _a_ _[−]_ _U_ [1]



_U_





 - _α_ 10 [0] _b_ [+] _[ α]_ 20 [0] _b_ [+] _[ α]_ [0] _a_ [0] _b_ �� _α_ 10 [0] _a_ _[K]_ _C_ _[µ][a]_ 10 _a_ [+] _[ α]_ 20 [0] _a_ _[K]_ _C_ _[µ][a]_ 20 _a_ 


��

_−_ - _α_ 10 [0] _b_ [+] _[ α]_ 20 [0] _b_ - _α_ 0 _a_ 0 _bKC_ _[µ][a]_ 0 _a_ 0 _b_ [+] _[ α]_ [0] _[a]_ [0] _b_ - _α_ 10 [0] _b_ _[K]_ _C_ _[µ][a]_ 10 _b_ [+] _[ α]_ 20 [0] _b_ _[K]_ _C_ _[µ][a]_ 20 _b_ 


_,_



(4.56)



(Ω∅) _bb→_ (Ω∅) _aa_ ��� _a↔b_ _[,]_ (Ω∅) _ab_ = (Ω∅) _ba_ _→_ 1 _−_ [1] 4



_α_ 0 _a_ 0 _b_

[1]

4 _[ω]_ [20] _[a][ω]_ [20] _[b]_ _U_



_a_ 0 _b_ _η_ _[µ][a][µ][b]_ _,_

_U_



where we have used the shorthand notation for the indices _a, b_ to correspond to the two curves
_C_ 20 [0] _a_ _[, C]_ 20 [0] _b_ [associated with fermionic propagators in (][4.55][).] [Computing the determinant of this]
matrix and extracting the multilinear coefficient in _ω_ 20 _aω_ 20 _b_, we obtain all the contributions
to the tensorial dependence of the numerator after integrating the loop momenta.
Next we treat the two-loop two-point scalar amplitude _A_ (Φ1 _,_ Φ2). As remarked earlier,
half of the work is already done since the expressions for the headlight functions and surface


                   - 30                    

**Figure** **20** : Kite topology for the planar two-loop two-point scalar amplitude.


Symanzik polynomials are the same for both _A_ (Ψ [¯] 1 _,_ Ψ2) and _A_ (Φ1 _,_ Φ2). However, the possible
charge assignments for the curves change. The curves of the form _C_ 12 _, C_ 11 _, C_ 22 are all scalar,
while the species of any curve that ends at a spiral is dictated by the charge assignments of the

internal punctures. In particular, this means that fermion lines are always closed, appearing

as Dirac traces of propagators involving a single loop.

For example, the tropical numerator evaluates to different versions of the kite diagram

depending on the charge of the punctures. In the case that the punctures _a_ and _b_ are chosen
to be fermionic and scalar, respectively ( _O_ = _{_ 0 _a}_ ), we find the diagram in figure 20 on the
kite cone. On this cone, the expression for the tropical numerator becomes


_N_ ��kite [=] _[ −][ig]_ [3] _[λ]_ [ tr]        - _/P C_ 10 _a /P C_ 0 _a_ 0 _b /P C_ 20 _a_        - _._ (4.57)


After loop integration, the tensor matrix for this charge assignment has a non-trivial 3 _×_ 3

minor (again, we will abuse notation and specify the indices of the matrix in terms of the

other endpoint of the curves in (4.57) that end spiraling around _a_ ) with entries







(Ω0 _a_ )11 _→_ _ω_ 10 _a_



_KC_ _[µ]_ [1] 0 _a_ 1 _[−]_ [1]



_U_





 - _α_ 10 [0] _b_ [+] _[α]_ 20 [0] _b_ [+] _[α]_ [0] _a_ [0] _b_ �� _α_ 10 [0] _a_ _[K]_ _C_ _[µ]_ [1] 0 _a_ 1 [+] _[α]_ 20 [0] _a_ _[K]_ _C_ _[µ]_ [1] 0 _a_ 2�



��
+� _α_ 10 [0] _b_ [+] _[α]_ 20 [0] _b_ - _α_ 0 _a_ 0 _bKC_ _[µ]_ [1] 0 _a_ 0 _b_ [+] _[α]_ [0] _[a]_ [0] _b_ - _α_ 10 [0] _b_ _[K]_ _C_ _[µ]_ [1] 0 _b_ 1 [+] _[α]_ 20 [0] _b_ _[K]_ _C_ _[µ]_ [1] 0 _b_ 2�



_,_







(Ω0 _a_ ) _bb_ _→_ _ω_ 0 _a_ 0 _b_



_KC_ _[µ][b]_ 0 _a_ 0 _b_ _[−]_ _U_ [1]



_U_





 - _α_ 10 [0] _b_ [+] _[α]_ 20 [0] _b_ �� _α_ 10 [0] _a_ _[K]_ _C_ _[µ][b]_ 0 _a_ 1 [+] _[α]_ 20 [0] _a_ _[K]_ _C_ _[µ][b]_ 0 _a_ 2�



��
+� _α_ 10 [0] _a_ [+] _[α]_ 20 [0] _a_ [+] _[α]_ 10 [0] _b_ [+] _[α]_ 20 [0] _b_ - _α_ 0 _a_ 0 _bKC_ _[µ][b]_ 0 _a_ 0 _b_ _[−]_ - _α_ 10 [0] _a_ [+] _[α]_ 20 [0] _a_ �� _α_ 10 [0] _b_ _[K]_ _C_ _[µ][b]_ 0 _b_ 1 [+] _[α]_ 20 [0] _b_ _[K]_ _C_ _[µ][b]_ 0 _b_ 2�



_,_



_α_ 10 _b_ + _α_ 20 _b_ + _α_ 0 _a_ 0 _b_

[1]

4 _[ω]_ [10] _[a][ω]_ [20] _[a]_ _U_



(Ω0 _a_ )12 = (Ω0 _a_ )21 _→_ 1 _−_ 4 [1]

(Ω0 _a_ )1 _b_ = (Ω0 _a_ ) _b_ 1 _→_ 1 + [1]



20 _b_ _η_ _[µ]_ [1] _[µ][b]_ _,_

_U_



20 _b_ 0 _a_ 0 _b_ _η_ _[µ]_ [1] _[µ]_ [2] _,_

_U_



_α_ 10 _b_ + _α_ 20 _b_

[1]

4 _[ω]_ [10] _[a][ω]_ [20] _[a]_ _U_



(Ω0 _a_ )22 _→_ (Ω0 _a_ )11 _|_ 1 _↔_ 2 _,_ (Ω0 _a_ )2 _b_ = (Ω0 _a_ ) _b_ 2 _→_ (Ω0 _a_ )1 _b|_ 1 _↔_ 2 _._ (4.58)


As in the fermion case, expanding the determinant and picking the multilinear term in
_ω_ 10 _aω_ 20 _aω_ 0 _a_ 0 _b_ yields all the possible pairwise tensor contractions that can appear after integrating the loop momenta.


                   - 31                    

**5** **Outlook**


This paper extends the curve integral formalism introduced in recent works [1–3] to quan
tum field theories of colored interacting fermions and scalars. By making use of constraints

apparent from the surface point of view, we find a compact expression for colored Yukawa

amplitudes as a single integral over a tropical numerator that makes no reference to Feynman

diagrams. Moreover, we can perform the loop integration and obtain expressions in terms

of special determinants. In addition to the explicit checks of equations (3.5) and (3.11) in
cluded in section 4, we have also performed various checks of our formula for (7-10)-point

tree amplitudes, planar 5- and 6-point one-loop amplitudes, non-planar 4-point amplitudes

and two-loop 4-point amplitudes.

While our work provides further evidence that a combinatorial formulation of (close to)

real-world scattering amplitudes is tangible, there are still numerous aspects of the curve

integral framework that need to be understood better. For example, it is essential to account

for massive fermions without breaking the nice combinatorial structure observed in (3.11) in

order to extend the curve integral formalism to more realistic theories. While the determinant

in the loop-integrated formula does not seem robust enough to capture the generalization

to non-zero fermion mass, its simple realization at the level of the loop integrand suggests

that a combinatorial formulation is feasible. Moreover, to describe quantum electrodynamics

or quantum chromodynamics, a curve integral formulation for amplitudes involving gauge

bosons (photons or gluons) coupled to fermions in the fundamental representation of _SU_ ( _N_ )

is necessary.

Another intriguing question is whether there exists a Feynman fan more naturally suited

to theories with fermions that does not require us to sum over different charge configurations

for the internal punctures. In other words, a division of the tropical space that spans the

complete set of Yukawa Feynman diagrams in a non-overlapping way. This would effectively
reduce the 2 _[L]_ -term sum into a tropical product.

Finally, it would be interesting to find a _stringy_ version of Yukawa amplitudes that
reduces to equations (3.5) and (3.11) in the low-energy limit _α_ _[′]_ _≪_ 1 along the lines of [5, 15].

With such a formula one could more easily test factorization in fermionic theories as well as

investigate the possibility of kinematic shifts analogous to the _δ_ -shifts that relate NLSM and
Yang-Mills amplitudes to their Tr(Φ [3] ) counterparts [6, 8, 9].


**Acknowledgements**


We are grateful to N. Arkani-Hamed, C. Figueiredo, H. Frost, and G. Salvatori for carefully

explaining many aspects of their work and to S. Paranjape and H. Thomas for related dis
cussions. This work was supported in part by the US Department of Energy under contract

DE-SC0010010 Task F (SD, MSp, AV), by Simons Investigator Award #376208 (AP, AV),

and by Bershadsky Distinguished Visiting Fellowships at Harvard (MSp, AV).


                   - 32                    

**References**


[1] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _All_ _Loop_
_Scattering_ _as_ _a_ _Counting_ _Problem_, `[2309.15913](http://arxiv.org/abs/2309.15913)` .


[2] N. Arkani-Hamed, H. Frost, G. Salvatori, P.-G. Plamondon, and H. Thomas, _All_ _Loop_
_Scattering_ _For_ _All_ _Multiplicity_, `[2311.09284](http://arxiv.org/abs/2311.09284)` .


[3] N. Arkani-Hamed, C. Figueiredo, H. Frost, and G. Salvatori, _Tropical_ _Amplitudes_ _For_ _Colored_
_Lagrangians_, `[2402.06719](http://arxiv.org/abs/2402.06719)` .


[4] C. Bartsch, T. V. Brown, K. Kampf, U. Oktem, S. Paranjape, and J. Trnka, _Hidden_ _Amplitude_
_Zeros_ _From_ _Double_ _Copy_, `[2403.10594](http://arxiv.org/abs/2403.10594)` .


[5] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Hidden_ _zeros_ _for_ _particle/string_
_amplitudes_ _and_ _the_ _unity_ _of_ _colored_ _scalars,_ _pions_ _and_ _gluons_, `[2312.16282](http://arxiv.org/abs/2312.16282)` .


[6] N. Arkani-Hamed and C. Figueiredo, _All-order_ _splits_ _and_ _multi-soft_ _limits_ _for_ _particle_ _and_
_string_ _amplitudes_, `[2405.09608](http://arxiv.org/abs/2405.09608)` .


[7] Q. Cao, J. Dong, S. He, and C. Shi, _A_ _universal_ _splitting_ _of_ _string_ _and_ _particle_ _scattering_
_amplitudes_, `[2403.08855](http://arxiv.org/abs/2403.08855)` .


[8] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _Scalar-Scaffolded_ _Gluons_ _and_ _the_
_Combinatorial_ _Origins_ _of_ _Yang-Mills_ _Theory_, `[2401.00041](http://arxiv.org/abs/2401.00041)` .


[9] N. Arkani-Hamed, Q. Cao, J. Dong, C. Figueiredo, and S. He, _NLSM_ _⊂_ _Tr_ ( _ϕ_ [3] ), `[2401.05483](http://arxiv.org/abs/2401.05483)` .


[10] N. Arkani-Hamed and C. Figueiredo, _Circles_ _and_ _Triangles,_ _the_ _NLSM_ _and_ _Tr(_ Φ [3] _)_,

`[2403.04826](http://arxiv.org/abs/2403.04826)` .


[11] A. Laddha and A. Suthar, _Positive_ _Geometries,_ _Corolla_ _Polynomial_ _and_ _Gauge_ _Theory_
_Amplitudes_, `[2405.10601](http://arxiv.org/abs/2405.10601)` .


[12] B. Gim´enez Umbert and K. Yeats, Φ _[p]_ _Amplitudes_ _from_ _the_ _Positive_ _Tropical_ _Grassmannian:_
_Triangulations_ _of_ _Extended_ _Diagrams_, `[2403.17051](http://arxiv.org/abs/2403.17051)` .


[13] J. Dong, X. Li, and F. Zhu, _Pions_ _from_ _higher-dimensional_ _gluons:_ _general_ _realizations_ _and_
_stringy_ _models_, `[2404.11648](http://arxiv.org/abs/2404.11648)` .


[14] Y. Li, D. Roest, and T. ter Veldhuis, _Hidden_ _Zeros_ _in_ _Scaffolded_ _General_ _Relativity_ _and_
_Exceptional_ _Field_ _Theories_, `[2403.12939](http://arxiv.org/abs/2403.12939)` .


[15] N. Arkani-Hamed, S. He, and T. Lam, _Stringy_ _canonical_ _forms_, _JHEP_ **02** (2021) 069,

[ `[1912.08707](http://arxiv.org/abs/1912.08707)` ].


                   - 33                    

