Prepared for submission to JHEP

# **All Loop Scattering for All Multiplicity**


**N.** **Arkani-Hamed,** _[a]_ **H.** **Frost,** _[b]_ **G.** **Salvatori,** _[c]_ **P-G.** **Plamondon** _[d]_ **H.** **Thomas** _[e]_


_aSchool_ _of_ _Natural_ _Sciences,_ _Institute_ _for_ _Advanced_ _Study,_ _Princeton,_ _NJ,_ _08540,_ _USA_

_bMathematical_ _Institute,_ _Andrew_ _Wiles_ _Building,_ _Woodstock_ _Rd,_ _Oxford,_ _UK_

_cMax-Plank-Instit¨ut_ _fur_ _Physik,_ _Werner-Heisenberg-Institut,_ _D-80805_ _M¨unchen,_ _Germany_

_dLaboratoire_ _de_ _Math´ematiques_ _de_ _Versailles,_ _UVSQ,_ _CNRS,_ _Universit´e_ _Paris-Saclay,_ _IUF,_

_France_

_eLaCIM,_ _D´epartement_ _de_ _Math´ematiques,_ _Universit´e_ _du_ _Qu´ebec_ _`a_ _Montr´eal,_ _Montr´eal,_ _QC,_

_Canada_
_E-mail:_ `[arkani@ias.edu](mailto:arkani@ias.edu)`, `[frost@maths.ox.ac.uk](mailto:frost@maths.ox.ac.uk)`, `[giulios@mpp.mpg.de](mailto:giulios@mpp.mpg.de)`,
`[pierre-guy.plamondon@uvsq.fr](mailto:pierre-guy.plamondon@uvsq.fr)`, `[thomas.hugh](mailto:thomas.hugh_r@uqam.ca)` ~~`r`~~ `@uqam.ca`


Abstract: This is part of a series of papers describing the new curve integral formalism for scattering amplitudes of the colored scalar tr _ϕ_ [3] theory. We show that the curve
integral manifests a very surprising fact about these amplitudes: the dependence on
the number of particles, _n_, and the loop order, _L_, is effectively decoupled. We derive
the curve integrals at tree-level for all _n_ . We then show that, for higher loop-order,
it suffices to study the curve integrals for _L_ -loop tadpole-like amplitudes, which have
just one particle per color trace-factor. By combining these tadpole-like formulas with
the the tree-level result, we find formulas for the all _n_ amplitudes at _L_ loops. We illustrate this result by giving explicit curve integrals for all the amplitudes in the theory,
including the non-planar amplitudes, through to two loops, for all _n_ .


### **Contents**

**1** **Introduction** **and** **Summary** **2**


**2** **Review** **4**


**3** **Tree-level** **Amplitudes** **7**


**4** **The** **Planar** **1-loop** **Amplitudes** **11**


**5** **The** **Telescopic** **Property** **14**


**6** **Decoupling** **Trees** **and** **Loops** **15**


**7** **Planar** **One-Loop** **Amplitudes** **Revisited** **17**


**8** **The** **Non-planar** **One-loop** **Amplitudes** **19**


**9** **Prefactors** **for** **All-multiplicity** **26**


**10** **Summary** **of** **Tree-Loop** **factorization** **30**


**11** **The** **Planar** **2-Loop** **Amplitudes** **31**


**12** **The** **2-Loop** **Triple-trace** **Amplitudes** **36**


**13** **The** **2-Loop** **Amplitudes** **at** **Genus** **One** **41**


**14** **The** **2-Loop** **Double-trace** **Amplitudes** **46**


**15** **Outlook** **49**


**A** **Curve** **Glossary** **52**


                  - 1                  

### **1 Introduction and Summary**

This is the second in a series of papers laying out a new point of view on scattering
amplitudes—the _curve_ _integral_ formalism—which is based on combinatorial structures
in the space of scattering data. [1] The curve integral exposes a number of hidden
features of amplitudes. In this paper we describe a striking example of one such hidden
structure. Ordinarily, the complexity of scattering amplitudes is thought to grow both
with increasing the number of particles _n_, and also with increasing loop order _L_ . The
case of amplitudes at both large _n_ and large _L_ is thought to be vastly more complicated
still. In this paper we will see that this expectation is misleading. First, we find that
the tree-level calculation for all _n_ is simplified by the curve integral formula. Second,
we find that the curve integral naturally decouples the dependence of amplitudes on _n_
and _L_ . The calculation of an _L_ -loop amplitude for small _n_ is all that is required to find
a closed formula for all _n_ .
The _n_ -point tree amplitude in tr _ϕ_ [3] theory is conventionally given by a sum of
diagrams. There are



1
_Cn−_ 2 =
_n −_ 1



�2 _n −_ 4�

(1.1)

_n −_ 2



such diagrams, and this number grows exponentially as _∼_ 4 _[n]_ _/_ ( _[√]_ _πn_ [3] _[/]_ [2] ) for large _n_ .
By contrast, the curve integral formula gives the amplitude as an integral over an
( _n −_ 3)-dimensional space,



_A_ [tree] _n_ =



_∞_


_d_ _[n][−]_ [3] _t Z._ (1.2)

0



The integrand, _Z_, is given by computing _n_ ( _n −_ 3) _/_ 2 simple _headlight_ _functions_, _αij_,
each with no more than _O_ ( _n_ ) terms:


log _Z_ = _−_           - _αij_ �( _pi_ + _· · ·_ + _pj−_ 1) [2] + _m_ [2][�] _._ (1.3)


1 _≤i<j−_ 1


This simple function is all that is needed to obtain _A_ [tree] _n_ [,] [which] [is] [naively] [a] [sum] [over]
exponentially many Feynman diagrams. We give explicit formulas for _αij_ valid at all
_n_ .
We can give closed formulas for the headlight functions _αij_ because they follow
from an inductive calculation using two-by-two matrices. These _curve_ _matrices_, _MC_ [tree],
have simple polynomial entries. The curve matrices for the _n_ -point amplitude are
sufficient to determine the matrices for the ( _n_ + 1)-point amplitude inductively, by
matrix multiplication. This immediately leads to closed formulas for these matrices for
all _n_ .


                  - 2                  

The simplification of the curve integral at tree level becomes even more striking at
loop level. We first study the very simplest _tadpole-like_ loop amplitudes, which have
just one particle in every color trace-factor. These _tadpole_ _amplitudes_ are determined
by a basic set of 2 _×_ 2 curve matrices, _MC_ [tadpole] . The surprise is that, having computed
both the tadpole matrices _MC_ [tadpole] and the tree matrices _MC_ [tree], we find that this is
everything needed to compute the curve integral for amplitudes at _any_ _n_, for fixed _L_ .
In other words, deriving the curve integral for an amplitude _An,L_ is only as difficult as
finding the curve integral for an _L_ -loop tadpole.
Moreover, the dependence on _n_ and _L_ is completely factorized in the curve integrals.
For any _n_ and _L_, the curve integral amplitude formula takes the form




   -    - _πL_
_An,L_ = _d_ _[E]_ _t_ _K_ _U_




- _[D]_ 2 - _×_ exp _−_ _[F]_ [0] _,_ (1.4)

_U_ _[−Z]_



where _E_ = _n_ + 3 _L −_ 3. In this formula, the first factor in the integrand,




 - _πL_
_K_

_U_




- _[D]_ 2
(1.5)



does not depend on _n_ . It can be computed once and for all for a tadpole-like graph.
The dependence on _n_ enters only via the exponential, whose exponent is a sum of terms
which grow only polynomially with _n_ .
The simplicity of these factorized formulas is illustrated by Table 1, which shows
the number of curve matrices _MC_ required in order to compute, first, the _n_ -independent
prefactor, and, second, the exponent of the exponential.
For example, this factorization can be seen in the 1-loop planar amplitudes. In
appropriate coordinates, the curve integrals for these amplitudes are



0




_∞_




_D_

- 2 - exp _−_ [1] _F_ 0 _−Z_ _._ (1.6)

_t_ 0



_A_ 1-loop =



_dt_ 0 _dt_ 1 _· · · dtn−_ 1

_−∞_ _−∞_




- _π_
_t_ 0



The 1-loop planar tadpole has only two propagators, and defines two associated curve
matrices, _MC_ [tadpole] . Just one of these matrices is required to compute the _n_ -independent
pre-factor, which in this case is

_D_

            - _π_            - 2

_._ (1.7)

_t_ 0


Whereas, both of the two tadpole curve matrices are needed to compute the exponent.
Given these two tadpole curve matrices, and the tree-level matrices _MC_ [tree], both _F_ 0 and
_Z_ can be computed directly.


                  - 3                  

Order # of Matrices for the prefactor Total # of Matrices

1-loop Planar 1 2
1-loop Double-trace 3 5
2-loop Planar 9 17
2-loop Genus-one 9 10
2-loop Double-trace 14 23
2-loop Triple-trace 24 33


**Table** **1** : The minimal number of curve matrices needed to derive the curve integral
for all-multiplicity amplitudes (right column), and the number of matrices needed to
derive just the pre-factor (middle column).


Needless to say, this Tree-Loop factorization is not at all manifest in the conventional diagrammatic approach to perturbation theory. Moreover, this factorization of
the tree- and loop-like parts of the calculation plays a practical role when computing
the amplitudes. In this paper, we illustrate this by giving concrete, all- _n_ formulas for
all amplitudes in the tr _ϕ_ [3] theory through to two loops: tree-level, 1-loop planar, 1-loop
double-trace, two-loop planar, two-loop triple trace, and the genus-one single-trace
two-loop corrections. We focus on the practical methods for determining the curve
integral formulas, while explaining the Tree-Loop factorization along the way. The
mathematical and conceptual foundations for the results will be described in greater
detail elsewhere.

### **2 Review**


In [1] we gave a formula for amplitudes in a coloured cubic scalar theory at any order
in perturbation theory. Each partial amplitude can be computed, in _D_ spacetime
dimensions, using a _curve_ _integral_ of the form








  -   - _d_ _[E]_ _t_
_A_ = _d_ _[D]_ _ℓ_
MCG [exp]





_−_ - _αC_ ( _t_ ) _XC_


_C_



_._ (2.1)



with _E_ = _n −_ 3 + 2 _L_ + 2 _g_, if _A_ is a partial amplitude with _L_ loops and genus _g_ . This
formula resembles a standard Feynman integral with Schwinger parameters. However,
here the Feynman parameters are replaced by piecewise linear functions, _αC_, of the _E_
integration variables _ti_ . Instead of integrating one Feynman diagram at a time, this
formula computes the full amplitude.


                  - 4                  

Using the curve integral formula, we can integrate over the loop variables, _ℓa_, once
and for all (rather than separately for each diagram). The result is (in some _D_ = 2 _d_ _−_ _ϵ_
dimension)




  - _d_ _[E]_ _t_
_A_ =
MCG




- _πL_

_U_




- _[D]_ 2 - exp _−_ _[F]_ [0] _,_ (2.2)

_U_ _[−Z]_



where _U, F_ 0 _, Z_ are homogeneous polynomials in the _αC_ .
Equations (2.1) and (2.2) are formulas for the full amplitude, automatically summing over all Feynman diagrams. However, counter-intuitively, the starting point for
these formulas is to choose a distinguished Feynman diagram, Γ. The Feynman diagrams for the theory are cubic fatgraphs. The main point in [1] is that a single given
fatgraph, Γ, contains all the information we need to compute the sum over _all_ diagrams.
The variables _ti_ are each assigned to each of the _E_ edges of the diagram Γ. The propagator factors, _XC_, correspond to paths, _C_, along the diagram Γ. And the functions
_αC_ ( _t_ ) are computed directly from the data of the path _C_, which can be described as
series of left and right turns on Γ.
To be concrete, consider some curve, _C_, with path


_C_ = _e_ 0 _Le_ 1 _Re_ 2 _· · ·_ _._ (2.3)


In other words, _C_ enters via external edge _e_ 0, takes a left turn, goes down edge _e_ 1,
takes a right turn, and so on. To find _αC_, we first replace each turn and edge with a
matrix:



�1 0
_e �→_
0 _ye_




- �1 0
_,_ _L �→_
1 1




- �1 1
_,_ _R �→_
0 1




_._ (2.4)



In this way, each curve defines a matrix, given by the product of these matrices:



�1 0��1 0
_MC_ =
1 1 0 _y_ 1



��1 1��1 0
0 1 0 _y_ 2





_· · ·_ _._ (2.5)



Note that external edges have _ye_ = 1. Each entry of _MC_ is a polynomial in the variables
_ye_ . Given _MC_, the _headlight_ _function_ is


_αC_ = _−_ Trop _MC_ [12] _[−]_ [Trop] _[M]_ [ 21] _C_ [+ Trop] _[M]_ [ 11] _C_ [+ Trop] _[M]_ [ 22] _C_ _[,]_ (2.6)


where Trop denotes the _tropicalization_ of a polynomial. Note that if the curve _C_ ends
in an infinite spiral around a closed loop path, ∆= _e_ 1 _Le_ 2 _L · · · emL_, this infinite path
is replaced by the matrix


            - 1 _−_ _y_ 1 _y_ 2 _· · · ym_ 0�
_M_ �∆ = _._ (2.7)
_y_ 1 + _y_ 1 _y_ 2 + _. . ._ + _y_ 1 _y_ 2 _· · · ym_ 1


                  - 5                  

(See Section 5.5 of [1] for more details.)
The distinguished fatgraph, Γ, also defines a consistent momentum assignment
to every curve, _C_ . We again read this directly from the fatgraph. Momenta, _p_ _[µ]_ _e_ [,]
are assigned to the edges of Γ in the usual way. If Γ has _L_ loops, the momenta are
parameterized by a choice of _L_ loop momentum variables _ℓ_ _[µ]_ _a_ [.][1] [Then] [a] [curve,] _[C]_ [,] [that]
enters via edge _e_ 1, say, is assigned momentum

_PC_ _[µ]_ [=] _[ p]_ _e_ _[µ]_ 1 [+]             - _p_ _[µ]_ left _[,]_ (2.8)

right turn


where, at each right turn, we add the momentum incident on the vertex from the left.
Given this momentum assignment, each _PC_ _[µ]_ [can] [be] [written] [as] [a] [sum] [of] [a] [loop-]
dependent and non-loop-dependent part,



_PC_ _[µ]_ [=] _[ K]_ _C_ _[µ]_ [+]



_L_


_ℓ_ _[a]_ _C_ _[ℓ][µ]_ _a_ _[,]_ (2.9)

_a_ =1



for some integers _ℓ_ _[a]_ _C_ [.] [In terms of this momentum assignment, the polynomials] _[ U][,][ F]_ [0] _[,][ Z]_
are given by

_U_ = det Λ _,_ _F_ 0 = _J_ _[T]_ [ ˜] Λ _J,_ _Z_ = �( _KC_ [2] [+] _[ m]_ [2][)] _[α][C][,]_ (2.10)

_C_


where the _L × L_ matrix Λ and vector _B_ are given by




 Λ _[ab]_ =



_ℓ_ _[a]_ _C_ _[ℓ][b]_ _C_ _[α][C][,]_ _J_ _[a,µ]_ =  
_C_ _C_



_ℓ_ _[a]_ _C_ _[K]_ _C_ _[µ][α][C][.]_ (2.11)

_C_



We write Λ = (det Λ) Λ [˜] _[−]_ [1] for the adjugate of Λ. For practical purposes, it is convenient
to leave _U_ and _F_ 0 expressed in terms of Λ _[ab]_ and _J_ _[a]_ . However, these polynomials also
have a beautiful combinatorial definition. Expanding the determinant, _U_ becomes a
sum of monomials, each corresponding to a cut of the diagram Γ that reduces it to a
tree graph. _U_ is then the sum over all such _maximal_ _cuts_ . Moreover, the monomial
terms of _F_ 0 correspond to _factorizing_ cuts of Γ into two trees.
The amplitude formulas, (2.1) and (2.2), still look a little formal because the integral requires us to mod out by the Mapping Class Group, MCG. MCG is a discrete
finitely generated group of symmetries of the fatgraph, Γ. Rather than finding a fundamental domain for this group action (which is tricky in general), we can evaluate
the integrals by introducing an integration kernel. The final formula for the amplitude
then reads,




  -   - _πL_
_A_ = _d_ _[E]_ _t K_

_U_




- _D/_ 2 - exp _−_ _[F]_ [0] _,_ (2.12)

_U_ _[−Z]_



1This is equivalent to choosing a labeled basis of the first homology of the graph.


                 - 6                 

for some kernel _K_ ( _t_ ), that we call the Mirzakhani kernel. [2] General methods for finding
a kernel are given in [1]. In this article, we will see that the computation of _K_ can be
simplified further. Amazingly, both _U_ and _K_ (and also the matrix Λ) are independent
of the number of external particles, _n_ . The number of external particles, and their
momenta, only enter the formula through the exponent in the formula, which is linear
in the momentum invariants.

### **3 Tree-level Amplitudes**


The curve integral formula for amplitudes is already interesting at tree level. Naively,
a tree-level _n_ -point amplitude is a sum over _∼_ 4 _[n]_ different Feynman diagrams. By
contrast, the tree-level curve integral is an integral over _n−_ 3 dimensions of an integrand
formed by _∼_ _n_ [2] headlight functions, _αC_, each of which can be computed by multiplying
_∼_ _n_ matrices. The resulting formula for the tree level amplitude is


                  _A_ tree(123 _...n_ ) = _d_ _[n][−]_ [3] _t Z,_ (3.1)


where


_−_ log _Z_ =          - _αCXC._ (3.2)


_C_


This sum is over all _n_ ( _n−_ 3) _/_ 2 possible propagators, _Cij_ . If _ki_ _[µ]_ [are the external momenta,]
the propagator variables, _XC_, are given by


_Xij_ = _Pij_ [2] [+] _[ m]_ [2] _[,]_ (3.3)


where _Pij_ = _ki_ + _. . ._ + _kj−_ 1 is the momentum of the _Cij_ propagator. We stress again
that computing _Z_ is much easier than enumerating Feynman diagrams.
In fact, this section finds a simple all- _n_ expression for _Z_ . The headlight functions,
_αC_, depend on our choice of distinguished fatgraph, Γ. If we choose Γ to be the comb
graph, as in Figure 1, then we obtain particularly simple formulas for the _αC_ . This
leads to the following compact all- _n_ formula for the amplitude,



_j_ = _n−_ 3


_fijcij_

1 _≤i≤j_








       _A_ tree(123 _...n_ ) = _d_ _[n][−]_ [3] _t_ exp




- _n−_ 3

 
_tiXi_ +1 _,n −_

_i_ =1



_._ (3.4)



2 _K_ is a tropical version of the kernel introduced by Mirzakhani to compute Weil-Petterson volumes,

[2] and which has been applied to physical calculations in, e.g. [3].


                  - 7                  

**Figure** **1** : The _n_ -point tree-level comb graph.


Here we write _fij_ for the tropical functions


_fij_ ( **t** ) = max _{_ 0 _, ti, ti_ + _ti_ +1 _, ..., ti_ + _ti_ +1 + _..._ + _tj},_ (3.5)


and _cij_ are the Mandelstam-like kinematic variables,


_cij_ = _Xi,j_ +3 + _Xi_ +1 _,j_ +2 _−_ _Xi,j_ +2 _−_ _Xi_ +1 _,j_ +3 _._ (3.6)


Not only is (3.4) an all- _n_ formula for the tree amplitude, it also contains the ingredients
we need to compute amplitudes for all- _n_ at higher orders in perturbation theory. Because of this, we will derive (3.4) in detail in this section. The formulas in this section
will be used repeatedly in subsequent calculations in this paper.


**3.1** **Tree-level** **Headlight** **Functions**


Take Γ to be the comb graph with end points labelled 1 and _n_, and with the ordering
1234 _...n_ . For each _i, j_, there is a unique curve, _Cij_, that connects external line _i_ to
external line _j_ . The paths of these curves are


_Cij_ = _Rei−_ 1 _LeiLei_ +1 _...Lej−_ 2 _R,_ (3.7)


_C_ 1 _j_ = _Le_ 1 _Le_ 2 _...Lej−_ 2 _R,_ (3.8)


_Cin_ = _Rei−_ 1 _LeiLei_ +1 _...Len−_ 3 _L._ (3.9)


where 1 _< i < j −_ 1 and _j_ _< n_ . Using the replacements (2.4), we find that these curves
have curve matrices




   - _Fi−_ 1 _,j−_ 3 _Fi−_ 1 _,j−_ 2
_Mij_ =
_yi−_ 1 _Fi,j−_ 3 _yi−_ 1 _Fi,j−_ 2




_,_ (3.10)




   - 1 1
_M_ 1 _j_ =
_F_ 1 _,j−_ 3 _F_ 1 _,j−_ 2




- - _Fi−_ 1 _,n−_ 3 _yi−_ 1 _,n−_ 3
_,_ _Min_ =
_yi−_ 1 _Fi,n−_ 3 _yi−_ 1 _,n−_ 3


  - 8   



_,_ (3.11)


where _yi,j_ = _yiyi_ +1 _. . . yj_ and the _Fij_ are the polynomials [3]


_Fij_ = 1 + _yi_ + _yiyi_ +1 + _..._ + _yiyi_ +1 _...yj,_ (3.12)


These matrices will be used throughout our calculations in this paper.
Write _fij_ = Trop _Fij_ for the tropicalization of the F-polynomials, (3.12). It follows
from (3.10) that the headlight functions are


_αij_ ( **t** ) = _fi−_ 1 _,j−_ 3 + _fi,j−_ 2 _−_ _fi−_ 1 _,j−_ 2 _−_ _fi,j−_ 3 (3.13)

_α_ 1 _j_ ( **t** ) = _f_ 1 _,j−_ 2 _−_ _f_ 1 _,j−_ 3 _,_ (3.14)

_αin_ ( **t** ) = _−ti−_ 1 + _fi−_ 1 _,n−_ 3 _−_ _fi,n−_ 3 _,_ (3.15)


with the tropical functions _fij_ given by


_fij_ ( **t** ) = max _{_ 0 _, ti, ti_ + _ti_ +1 _, ..., ti_ + _ti_ +1 + _..._ + _tj}._ (3.16)


**3.2** **The** **All-multiplicity** **Amplitude**


To obtain the amplitude, we first consider the assignment of momenta to curves. Using
the momentum assignment rule, (2.8), the momentum of the curve _Cij_ is (with _i < j−_ 1)


_Pij_ = _pi_ + _pi_ +1 + _..._ + _pj−_ 1 _,_ (3.17)


where _p_ _[µ]_ _a_ [are] [the] [external] [momenta.] [Because] [Γ] [is] [planar,] [we] [can] [alternatively] [assign]
these momenta using _dual_ _momentum_ _variables_, _za_ _[µ]_ [,] [so] [that]


_Pij_ _[µ]_ [=] _[ z]_ _j_ _[µ]_ _[−]_ _[z]_ _i_ _[µ][,]_ (3.18)


where, say, _zi_ = _p_ 1 + _· · ·_ + _pi−_ 1. In either case, the propagator factors are



2




_Xij_ = _m_ [2] +




- _j−_ 1

 
_pa_

_a_ = _i_



_,_ with _Xii_ +1 = 0 _,_ _X_ 1 _n_ = 0 _._ (3.19)



With these momentum assignments understood, the amplitude is


                _An_ = _d_ _[n][−]_ [3] _t Z,_ (3.20)


where




_−_ log _Z_ =



_n_

 
_αijXij._ (3.21)

1 _≤i<j−_ 1



3The polynomials _Fij_ ( _y_ ) are the _F-polynomials_ associated to this A-type cluster algebra.


                 - 9                 

The _αij_ ( _t_ ) are given by (3.13–3.15).
An alternative form of log _Z_ is obtained by expanding the _αij_ ( _t_ ). This gives



_j_ = _n_

 
( _fi,j−_ 2 + _fi−_ 1 _,j−_ 3 _−_ _fi−_ 1 _,j−_ 2 _−_ _fi,j−_ 3) _Xij,_ (3.22)

1 _≤i<j−_ 1




_−_ log _Z_ = _−_



_n−_ 3


_tiXi_ +1 _,n_ +

_i_ =1



where, in the second sum, we set _fkl_ _≡_ 0 if _k_ = 0, or _l_ = _n −_ 2. The second sum can
be rewritten to find



_j_ = _n−_ 3


_fijcij,_ (3.23)

1 _≤i≤j_



log _Z_ =



_n−_ 3


_tiXi_ +1 _,n_ +

_i_ =1



where the Mandelstam-like variables _cij_ are


_cij_ = _Xi,j_ +3 + _Xi_ +1 _,j_ +2 _−_ _Xij_ +2 _−_ _Xi_ +1 _,j_ +3 _._ (3.24)


Evaluating these using (3.19), we find



_cij_ =








_si,j_ +3 _−_ _m_ [2] _j_ = _i_
_s_ 1 _n−_ 3 _−_ _m_ [2] ( _i, j_ ) = (1 _, n −_ 3) (3.25)
_si,j_ +3 otherwise _,_







where the _sij_ = ( _ki_ + _kj_ ) [2] are the Mandelstam variables.


**3.3** **Grafting** **Trees**


Throughout must of this paper, we will join comb tree graphs to other, higher-loop
fatgraphs. By convention, we will take a _n_ + 1-point comb graph, Γ, and join its
( _n_ + 1)st leg to an external leg of some other graph, Γ _[′]_ . The result is a larger graph
Γ _⊔_ Γ _[′]_ . Consider a curve, _C_, that enters the graph through external line _i_ of Γ, and
then proceeds into Γ _[′]_ . It has a path


_C_ = _Rei−_ 1 _LeiL · · · Len−_ 1 _D,_ (3.26)


for some path _D_ . Now that _en−_ 1 is an internal edge of the larger graph Γ _⊔_ Γ _[′]_, it is
assigned its own variable, _yn−_ 1. The curve matrix _MC_ then factors into a product




_MD._ (3.27)



_MC_ = _Mi,n_ +1



�1 0
0 _yn−_ 1



Given this, it is convenient to define the matrix




_,_ (3.28)



_Wi_ = _Mi,n_ +1



�1 0
0 _yn−_ 1




- 10 

**Figure** **2** : An _n_ -point 1-loop planar graph.


so that _MC_ = _WiMD_ . For _i >_ 1 we have




   - _Fi−_ 1 _,n−_ 2 _yi−_ 1 _,n−_ 1
_Wi_ =
_yi−_ 1 _Fi,n−_ 2 _yi−_ 1 _,n−_ 1




_,_ (3.29)



and for _i_ = 1 we have




   - 1 0
_W_ 1 =
_F_ 1 _,n−_ 2 _y_ 1 _,n−_ 1




_._ (3.30)



When multiple tree graphs Γ [1] _, . . .,_ Γ _[h]_ are joined to different trace-factors of a graph
Γ, it is helpful to record the trace-factor by adding an additional index and writing _Wi_ _[A]_
(for _A_ = 1 _, . . ., h_ ) for the tree-level matrix starting from _i_ in Γ _[A]_ .

### **4 The Planar 1-loop Amplitudes**


Curve integrals allow us to compute the 1-loop planar amplitudes for all multiplicity.
In this section, we illustrate the curve integral method by deriving an all- _n_ formula
using the _wheel_ diagram. Later, in Section 7, we revisit this amplitude with new tools,
that allow us to disentangle the loop-like and tree-like parts of this formula.


**4.1** **1-Loop** **Headlight** **Functions**


Take Γ to be the 1-loop _wheel_ _diagram_, in Figure 2, with _n_ external legs labeled
1 _,_ 2 _, ..., n_, cyclically. This fatgraph has finitely many curves. There are _n_ ( _n_ + 1) _/_ 2
curves connecting external legs, that we call _Cij_ with 1 _≤_ _i ≤_ _n_ and _i < j_ (cyclically).
There are also _n_ spiraling curves _Ci_ 0 that start at an external leg, _i_, and end in a spiral
around Γ’s internal boundary.


                  - 11                  

Examining Γ, in Figure 2, the curves _Cij_ ( _i ≤_ _j_ ) and _Ci_ 0 have paths


_Cij_ = _ReiLei_ +1 _L · · · Lej−_ 1 _R,_ (4.1)

_Ci_ 0 = _R_ ( _eiLei_ +1 _· · · Lei−_ 1 _L_ ) _[∞]_ _._ (4.2)


Substituting the matrices in equation (2.4), these paths determine the curve matrices
of these curves [4]




   - _Fi,j−_ 1 _Fij_
_Mij_ =
_yiFi_ +1 _,j−_ 1 _yiFi_ +1 _,j_




- - _Fi,i−_ 2 1�
_,_ _Mi_ 0 = _,_ (4.3)
_yiFi_ +1 _,i−_ 1 1



where


_Fij_ = 1 + _yi_ + _yiyi_ +1 + _. . ._ + _yiyi_ +1 _...yj._ (4.4)


These curve matrices define headlight functions. Write


Trop _Fij_ = _fij_ = max(0 _, ti, ti_ + _ti_ +1 _, ..., ti_ + _ti_ +1 + _..._ + _tj_ ) _,_ (4.5)


for the tropicalization of the _F_ -polynomials, where the indices are understood cyclically
(mod _n_ ). Then (in the region [�] _i_ _[n]_ =1 _[t][i]_ _[<]_ [ 0)]


_αij_ = _fi,j−_ 1 + _fi_ +1 _,j_ _−_ _fij_ _−_ _fi_ +1 _,j−_ 1 (4.6)

_αi_ 0 = _−ti −_ _fi_ +1 _,i−_ 1 + _fi,i−_ 2 _._ (4.7)


Note that the _αi_ 0 satisfy the identity



_n_


_αi_ 0 = _−_

_i_ =1



_n_


_ti._ (4.8)

_i_ =1



This identity will be useful for simplifying the formula for the amplitude.


**4.2** **The** **Loop** **Integrand**


Since Γ is a planar diagram, it is convenient to use _dual_ _momentum_ _variables_ to record
momentum assignments. With dual variables _x_ _[µ]_ _i_ [(] _[i]_ [=] [0] _[,]_ [ 1] _[, . . ., n]_ [),] [the] [propagator]
factors are
_Xij_ = ( _xj_ _−_ _xi_ ) [2] + _m_ [2] _._ (4.9)

If _p_ _[µ]_ _i_ [(] _[i]_ [ = 1] _[, . . ., n]_ [)] [are] [the] [external] [momenta,] [take]


_x_ _[µ]_ _i_ [=] _[ p]_ 1 _[µ]_ [+] _[ . . .]_ [ +] _[ p]_ _i_ _[µ]_ _−_ 1 _[.]_ (4.10)


4For the infinitely spiraling path the limit has to be defined carefully and _Mi_ 0 is defined by replacing
the infinite spiral with the matrix _M_ [�] ∆ given by equation (2.7).


                  - 12                  

It is convenient to use _x_ _[µ]_ 0 [as] [the] [loop] [momentum] [variable.]
With these momentum assignments, the integrand (pre-loop integration) is given
by the curve integral




     _I_ 1 _−_ loop =


   - _ti≤_ 0



_d_ _[n]_ _t Z,_ (4.11)



where



_n_


_Xi_ 0 _αi_ 0 _._ (4.12)

_i_ =1




_−_ log _Z_ =



cyclic


_Xijαij_ +

_i<j_



A more explicit formula for _Z_ follows from substituting the expressions for the
headlight functions. This gives



_n_


_fi,i−_ 2( _Xi−_ 1 _,_ 0 _−_ _Xi,_ 0) +

_i_ =1



cyclic


_fijcij,_ (4.13)

_i≤j_



log _Z_ =



_n_


_tiXi,_ 0 +

_i_ =1



where _cij_ = _Xij_ + _Xi−_ 1 _,j_ +1 _−_ _Xi,j_ +1 _−_ _Xi−_ 1 _,j_ .


**4.3** **The** **All-multiplicity** **Amplitude**


The integrand, _I_, depends on the loop momentum variable _x_ _[µ]_ 0 [.] [But] [the] [integral] [over]
_x_ _[µ]_ 0 [is] [Gaussian.] [Performing] [this] [integration] [in] _[D]_ [=] [2] _[d][ −]_ _[ϵ]_ [dimensions] [gives] [the] [curve]
integral formula for the amplitude,




     _A_ 1-loop =


   _i_ _[t][i][≤]_ [0]




  - _π_
_d_ _[n]_ **t**
_U_



_D_ - 
- 2
exp _−_ _[F]_ [0] _,_ (4.14)

_U_ _[−Z]_



where _U, F_ 0 _, Z_ are the _surface_ _Symanzik_ _polynomials_ for Γ. In terms of the headlight
functions,



_n_


_αi_ 0 _αj_ 0 _zi · zj,_ (4.15)

_i,j_ =1



_U_ =



_n_


_αi_ 0 _,_ _F_ 0 =

_i_ =1



_n_


_αi_ 0( _zi_ [2] [+] _[ m]_ [2][)] _[.]_ (4.16)
_i_ =1



_Z_ =



cyclic


_αijXij_ +

_i<j−_ 1



We find even more explicit formulas for _U, F_ 0 by substituting the formulas for the
headlight functions. This gives:



_n_


_titjzi · zj_ + _fi,i−_ 2 _fj,j−_ 2 _pi · pj._ (4.17)

_i,j_ =1


 - 13 


_U_ = _−_



_n_


_ti,_ _F_ 0 =

_i_ =1


### **5 The Telescopic Property**

The computations of the headlight functions, _αC_, are not very sensitive to the number of external particles, _n_ . This is because the transfer matrices, _MC_, are computed
multiplicatively. This is related to a fundamental _telescopic_ _property_ of the headlight
functions, which we explain in this section. The telescopic property leads to simplifications of the curve integral formulas.
Consider a path, _C_, that has not yet reached an external line of some fatgraph, Γ.
The path has an associated curve matrix,


                  - _a_ _b_                  _MC_ = _,_ (5.1)
_c_ _d_


for some _a, b, c, d_, which are polynomials for the _y_ -variables. The associated headlight
function for this matrix is


_αC_ = Trop( _a_ ) + Trop( _d_ ) _−_ Trop( _b_ ) _−_ Trop( _c_ ) _._ (5.2)


Suppose that _C_ ends just before traversing an edge, _e∗_, with variable _y∗_ . Then _C_
can be extended in one of two ways, as in Figure 3. It can traverse _e∗_ and turn left, to
get a longer path: _Ce∗L_ . Or it can turn right instead: _Ce∗R_ . The associated transfer
matrices are




    - _a_ + _by∗_ _by∗_
_MCy∗L_ = _c_ + _dy∗_ _dy∗_




- - _a_ _a_ + _by∗_
_,_ _MCy∗R_ = _c_ _c_ + _dy∗_




_._ (5.3)



If we stop here to compute the new headlight functions of these paths, we find


_αCe∗L_ = Trop( _b_ ) + Trop( _c_ + _dy∗_ ) _−_ Trop( _d_ ) _−_ Trop( _a_ + _by∗_ ) (5.4)

_αCe∗R_ = Trop( _a_ + _by∗_ ) + Trop( _c_ ) _−_ Trop( _a_ ) _−_ Trop( _c_ + _dy∗_ ) _._ (5.5)


But note that the sum of these two functions is equal to _αC_, corresponding to the
matrix _MC_ :
_αCe∗L_ + _αCe∗R_ = _αC._ (5.6)


In other words, the sum _αCe∗L_ + _αCe∗R_ can be computed without finding _MCy∗L_ and
_MCy∗R_ separately. It is only necessary to compute the matrix _MC_ .
This relation can be telescopically nested to compute larger sums of headlight
functions. Suppose Γ can be decomposed into a join of two graphs, Γ = Γ [1] _⊔_ Γ [2], where
Γ [1] is a tree graph. And suppose that _C_ is a path in Γ with an endpoint at the join of
the two graphs. We can sum over all ways to extend _C_ to an external line of the tree


                  - 14                  

**Figure** **3** : An incomplete curve can be extended in one of two ways: to the left, or to
the right.


graph Γ [1] . If Γ [1] has _k_ external lines (excluding the join), we obtain _k_ curves _C_ 1 _, ..., Ck_ .
Then applying (5.6) gives
_k_

      
_αCk_ = _αC._ (5.7)

_i_ =1


Similarly, if _C_ is a path in Γ with _both_ of its endpoints at the join of the two graphs,
we can sum over all ways to extend _C_ to a complete path. Suppose _Cij_ is the curve
obtained by extending _C_ to have endpoints _i_ and _j_ in Γ0 (with, say, _i ≤_ _j_ ). Then



_k_



_i_ =1
_i≤j_



_αCij_ = _αC._ (5.8)



In other words, the telescopic property dramatically simplifies any sum over headlight
functions _αC_ for a class of curves, _C_, that differ only by their endpoint on a tree
subgraph.

### **6 Decoupling Trees and Loops**


One drastic consequence of the telescopic property is that the curve integral integrands
_factorize_ into the product of a loop-like factor, which is independent of _n_, and a second
_n_ -dependent factor which contains the kinematics.
To make this factorization manifest, we define a class of _Tree-Loop_ _graphs_ . We say
that an _L_ -loop fatgraph is a _tadpole_ _graph_ if it has exactly one particle per trace-factor.
This generalises the usual notion of a tadpole (i.e. a graph with just one external leg).
A Tree-Loop graph is then formed by joining tree graphs to the legs of a tadpole graph.
For example, Figure 4 is a Tree-Loop graph formed by joining a 1-loop tadpole and an
( _n_ + 1)-point tree graph.


                  - 15                  

**Figure** **4** : A Tree-Loop fatgraph for the planar 1-loop amplitudes.


Take some _L_ -loop tadpole fatgraph, Γ _ℓ_, with _h_ external legs (one for each tracefactor). Then, for some comb tree graphs Γ _[A]_ ( _A_ = 1 _, . . ., h_ ) we can form a Tree-Loop
graph



Γ = Γ _ℓ_ _⊔_



_h_


Γ _A,_ (6.1)

_A_ =1



where Γ _[A]_ is joined to leg _A_ of Γ _ℓ_ . Now consider the curves on this Tree-Loop graph, Γ.
A curve that connects particle _i_ on trace-factor _A_ to particle _j_ on trace-factor _B_ can
be decomposed into three parts:


_C_ = _Ci_ _[A][C][AB][C]_ _j_ _[B][,]_ (6.2)


where _Ci_ _[A]_ [and] _[C]_ _j_ _[B]_ [are] [paths] [in] [the] [tree] [graphs,] [and] _[C][AB]_ [is] [a] [path] [in] [the] [tadpole,] [Γ] _[ℓ]_ [.]
The curve matrix for _C_ is then the product


_MC_ = _Wi_ _[A][M][C]_ _AB_          - _Wj_ _[B]_          - _T_ _,_ (6.3)


where the _Wi_ _[A]_ [are the tree-level matrices we have already computed for all] _[ n]_ [ in Section]
3.3. In other words, to find the curve matrices for Γ, it suffices to compute only the
the matrices _MCAB_ for the curves on the tadpole graph, Γ _ℓ_ .
Note that the momentum assignments also become easier to compute. For the
curve _C_ = _Ci_ _[A][C][AB][C]_ _j_ _[B]_ [,] [the] [momentum] [can] [be] [written] [as] [a] [sum]


_PC_ = _PCAB_ + _zj_ _[B]_ _[−]_ _[z]_ _i_ _[A][,]_ (6.4)


where _PCAB_ is the momentum of _CAB_ on the tadpole graph, Γ _ℓ_ . Here, _zi_ _[A]_ is the
momentum
_zi_ _[A]_ [=] _[ p][i]_ [+1] [+] _[ · · ·]_ [ +] _[ p][n]_ _A_ (6.5)


formed by summing momenta on trace-factor _A_ . _nA_ is the number of particles incident
on trace-factor _A_, and the particles are ordered (12 _· · · nA_ ) by convention. So the


                  - 16                  

momenta of curves on Γ follow from the momentum assignments for the tadpole graph,
Γ _ℓ_ .
The upshot is that _n_ -point amplitudes at _L_ loops with _h_ trace-factors, can be
computed by studying an _h_ -point _L_ -loop fatgraph.

### **7 Planar One-Loop Amplitudes Revisited**


In Section 4 we computed the planar one-loop amplitudes. We now revisit these amplitudes, by deriving them from a study of the 1-loop planar tadpole.
The 1-loop planar tadpole graph, Γ _ℓ_, is shown in Figure 5. The tadpole has two
curves: a single loop, _P_, and a spiral, _S_ . We discard the clockwise spiral. [5] The paths
of these curves are
_P_ = _RxR,_ and _S_ = _R_ ( _xL_ ) _[∞]_ _._ (7.1)


So the two curve matrices are



�1 1 + _x_
_P_ =
0 _x_


The headlight functions are




- �1 1�
_,_ and _S_ = _._ (7.2)
_x_ 1



_αP_ = _tx −_ max(0 _, tx_ ) _,_ _αS_ = _−tx._ (7.3)


Note that _P_ has zero momentum, whereas _S_ has momentum _x_ _[µ]_ 0 [,] [if] _[x][µ]_ 0 [is] [the] [loop]
momentum variable running through the one edge of the graph.
As an aside, consider evaluating the tadpole amplitude. The curve integral formula
for the loop integrand gives



0

 
_dtx e_ _[t][x][ℓ]_ [2] _._ (7.4)

_−∞_



_I_ tadpole =



0

 
_dtx_ exp   - _−αP_ _m_ [2] _−_ _αS_ ( _m_ [2] + _ℓ_ [2] )� =

_−∞_



After integrating out the loop momentum, the curve integral for the amplitude is



_D_

- 2
_,_ (7.5)



_A_ tadpole =



0

 
_dtx_

_−∞_




- _π_
_−tx_



as expected.


5In general, only one helicity of spirals enter into the formulas for amplitudes. As explained in [1],
including both spirals leads to overcounting of Feynman diagrams.


                  - 17                  

**Figure** **5** : The Planar One-loop tadpole (left), and its two curves: _S_ and _P_ .


To compute the _n_ -point amplitude, join a comb tree graph Γ [1] to the one leg of the
tadpole. The result is the _Tree-Loop_ graph, Γ, in Figure 4. The curves on Γ can be
written in Tree-Loop factorised form. In addition to the curves on Γ [1], _Cij_ (with _i < j_ ),
that do not intersect the tadpole, the other curves are (with _i ≤_ _j_ )


_Cji_ = _Wi_ [1] _[P]_             - _Wj_ [1]             - _T_ _,_ _Ci_ 0 = _Wi_ [1] _[S,]_ (7.6)


where _Wi_ [1] [is] [the] [curve] [that] [connects] [edge] _[i]_ [on] [the] [tree,] [to] [the] [edge] [that] [joins] [Γ][1] [to]
the the tadpole. ( ) _[T]_ denotes word reversal. Note that _MCT_ is given by the matrix
transpose, _MC_ _[T]_ [.] [The] [curve] [matrices] [for] [these] [paths] [are] [given] [in] [Section] [3.3][.]
Using (7.2), the curve matrix for _Ci_ 0, for example, is




      - 1 0
_Mi_ 0 = _Wi_ [1] _[S]_ [=]
_F_ 1 _,n−_ 2 _y_ 1 _,n−_ 1



��1 1� - 1 0

=

_x_ 1 _F_ 1 _,n−_ 2 + _xy_ 1 _,n−_ 1 _F_ 1 _,n−_ 2 + _y_ 1 _,n−_ 1




_,_ (7.7)



so that the headlight function for this curve is


_αi_ 0 = max(0 _,_ _t_ 1 _,_ _. . ._ _,_ _t_ 1 + _· · ·_ + _tn−_ 1) (7.8)

_−_ max(0 _,_ _t_ 1 _,_ _. . ._ _,_ _t_ 1 + _· · ·_ + _tn−_ 2 _,_ _t_ 1 + _· · ·_ + _tn−_ 1 + _tx_ ) _,_


where _tx_ is the tropical variable for _x_ . The other headlight functions can be similarly
computed.
Substituting the headlight functions into our curve integral formula gives a new
formula for the planar one-loop amplitudes. In fact, an interesting simplification arises.
Recall that _U_ is given by



_U_ =



_n_


_αi_ 0 _._ (7.9)

_i_ =1



Applying the telescopic property, this simplifies to


_U_ = _αS_ = _−tx._ (7.10)


                  - 18                  

The amplitude then takes the form


            -             - _π_
_A_ 1-loop = _d_ _[n]_ **t** _−tx_

_tx<_ 0



_D_

- 2 - _F_ 0 exp _−Z_ _,_ (7.11)
_tx_



where **t** = ( _t_ 1 _, . . ., tn−_ 1 _, tx_ ). In this integral, the first factor,


_D_

           - _π_            - 2

_,_ (7.12)

_−tx_


is independent of _n_, and is precisely what is obtained when we evaluate the (divergent)
tadpole amplitude.
This is a first sign that Tree-Loop factorization simplifies the final amplitude formulas. As we will see in the following sections, Tree-Loop factorization becomes even
more useful at higher orders in the perturbation series.

### **8 The Non-planar One-loop Amplitudes**


As a more complicated example, consider the one-loop double-trace amplitudes, for any
number of particles, _n_ = _n_ 1 + _n_ 2. The all-multiplicity case follows from an analysis of
the 1-loop double-trace tadpole graph. The final formula we obtain for the amplitude
takes the form (with _E_ = _n_ 1 + _n_ 2)




    
       - _π_
_An_ 1 _,n_ 2 = _d_ _[E]_ _t K_ _U_



_D_ - 
- 2
exp _−_ _[F]_ [0] _._ (8.1)

_U_ _[−Z]_



Here, _U_ and _K_ have simple formulas that follow from studying the tadpole graph.
Whereas _F_ 0 and _Z_ have all- _n_ formulas involving the kinematics, that we derive by
adding trees to the tadpole fatgraph. The number of terms in _F_ 0 and _Z_ grows polynomially with _n_ .


**8.1** **The** **Tadpole**


The tadpole fatgraph, Γ _ℓ_, is given in Figure 6. It has two trace-factors, each with one
particle, labelled 1 and 2. There are two curves on Γ _ℓ_ that begin and end at the same
point, and carry zero momentum:


_C_ 11 = _Le_ 1 _Le_ 2 _L,_ _C_ 22 = _Le_ 1 _Le_ 2 _L._ (8.2)


There are also curves that connect 1 and 2. For example, reading off from the fatgraph,
the first few of these curves are


_C_ 12 _[−]_ [1] [=] _[ Re]_ [2] _[L,]_ _C_ 12 [0] [=] _[ Le]_ [1] _[R,]_ _C_ 12 [1] [=] _[ Le]_ [1][(] _[Le]_ [2] _[Re]_ [1][)] _[R.]_ (8.3)


                  - 19                  

**Figure** **6** : The non-planar one-loop tadpole-like graph (left), and examples of curves
on the graph (right).


These three curves differ from each other by Dehn twists around the closed path


∆= _Le_ 2 _Re_ 1 _._ (8.4)


Dehn twists around ∆generate the MCG for this diagram.
Let _p_ _[µ]_ 1 [=] _[−][p][µ]_ [and] _[p][µ]_ 2 [=] _[p][µ]_ [be] [the] [momentum] [assigned] [to] [the] [external] [legs.] [Then]
the momentum associated to ∆is


_P_ ∆ = _−p_ _[µ]_ _._ (8.5)


Assign a momentum routing to the internal edges of the fatgraph ( _e_ 1 and _e_ 2) by setting,
say, _pe_ 2 = _ℓ_ _−_ _p_, and _pe_ 1 = _ℓ_ _−_ 2 _p_ . Then the three curves have momenta


_P_ 12 _[−]_ [1] [=] _[ ℓ]_ _[−]_ _[p,]_ _P_ 12 [0] [=] _[ ℓ,]_ _P_ 12 [1] [=] _[ ℓ]_ [+] _[ p.]_ (8.6)


**8.2** **Aside** **on** **the** **Role** **of** **the** **Mirzakhani** **Kernel**


Γ _ℓ_ is sufficiently simple that it is a feasible exercise to write down paths for _all_ curves
on the fatgraph. The complete set of curves can be labelled as


_C_ 11 _,_ _C_ 22 _,_ _C_ 12 _[w]_ _[,]_ (8.7)


for _w_ _∈_ Z. Here, _C_ 12 _[w]_ [+1] is obtained from _C_ 12 _[w]_ [by] [inserting] [a] [twist] [around] [the] [closed]
curve ∆. The curves _C_ 12 _[−]_ [1] _[, C]_ 12 [0] _[, C]_ 12 [1] [are as above.] [Moreover, the momentum assignments]
in (8.6) generalise to


_P_ 12 _[m]_ [=] _[ ℓ]_ [+] _[ mp,]_ _P_ 11 = 0 _,_ _P_ 22 = 0 _._ (8.8)


With these momentum assignments, the tadpole amplitude can be given by the curve
integral




    - _d_ [2] _t_
_A_ tadpole =
MCG




- _π_
_U_



_D_ - 
- 2
exp _−_ _[F]_ [0] _,_ (8.9)

_U_ _[−Z]_




- 20 

where it is still necessary to quotient by the action of MCG. In this formula, the surface
Symanzik polynomials are formally given as infinite sums:



_U_ =



_∞_

- _α_ 12 _[w]_ _[,]_ _F_ 0 = _J_ _[µ]_ _Jµ,_ (8.10)

_w_ = _−∞_



_Z_ = _m_ [2] ( _α_ 11 + _α_ 22) +



_∞_


( _m_ [2] + _w_ [2] _p_ [2] ) _α_ 12 _[w]_ _[,]_ (8.11)
_w_ = _−∞_



where



_∞_
_J_ _[µ]_ = _p_ _[µ]_ - _w α_ 12 _[w]_ _[.]_ (8.12)

_w_ = _−∞_



In practice, these infinite expressions are not useful for computations. This emphasizes the important role played by the _Mirzakhani_ _kernel_, _K_ . The integral becomes




    
       - _π_
_A_ tadpole = _d_ [2] _t K_ _U_



_D_  -  
- 2
exp _−_ _[F]_ [0] _._ (8.13)

_U_ _[−Z]_



In the region where _K_ = 0, most headlight functions, _αC_, are vanishing. In general,
only finitely many headlight functions contribute to this formula. So _U, F_ 0 and _Z_ are
all given instead by _finite_ _sums_ . And it is only necessary to find the paths for a finite
number of curves in order to use the formula.


**8.3** **MCG** **and** **Mirzakhani** **Kernel**


The MCG is generated by Dehn twists around the closed curve ∆. Write _γ_ ∆ for the
action of this Dehn twist on curves. ∆does not intersect _C_ 11 or _C_ 22, so these curves
are MCG invariant. Whereas ∆intersects any curve, _C_ 12, connecting 1 and 2. So these
curves are acted on by _γ_ ∆.
The curves _C_ 12 form a single coset under the action of _γ_ ∆. Take _C_ 12 [0] [as] [a] [coset]
representative. Then a Mirzakhani kernel is given by

_K_ = _[α]_ 12 [0] (8.14)
_ρ_ _[,]_


where _ρ_ is the sum

      _ρ_ = _αC_ 12 (8.15)


_C_ 12


over all curves connecting 1 and 2.
However, here a simplification arises. Draw _C_ 12 [0] [on the fatgraph Γ] _[ℓ]_ [.] [There are only]
_four_ curves that do not intersect _C_ 12 [0] [.] [These] [are]


_C_ 11 _,_ _C_ 22 _,_ _C_ 12 _[−]_ [1] _[,]_ _C_ 12 [1] _[,]_ (8.16)


                  - 21                  

whose paths are given above (see (8.2) and (8.3)). So the Mirzakhani kernel is in fact


_K_ = _α_ 12 [0] _._ (8.17)
_α_ 12 _[−]_ [1] [+] _[ α]_ 12 [0] [+] _[ α]_ 12 [1]


Moreover, the surface Symanzik polynomials for the tadpole, which were given as
formal expressions in Section 8.2, also simplify in the region where _K_ is non-vanishing.
They become (if _p_ _[µ]_ is on-shell, say)


_U_ = _α_ 12 _[−]_ [1] [+] _[ α]_ 12 [0] [+] _[ α]_ 12 [1] _[,]_ _F_ 0 = _p_ [2] ( _α_ 12 [1] _[−]_ _[α]_ 12 _[−]_ [1][)][2] (8.18)

_Z_ = _m_ [2] ( _α_ 11 + _α_ 22 + _α_ 12 [0] [)] _[.]_ (8.19)


In summary, the pre-factor appearing in the tadpole amplitude formula,




 - _π_
_K_
_U_



_D_

- 2
_,_ (8.20)



can be computed using the paths for 3 curves. While the whole integrand for the
integral can be computed using the paths for a set, _S_ of 5 curves. The curve matrices
for these five curves is given in Appendix A.1.
As a final remark, using the Appendix, the headlight functions for the five curves
are


_α_ 12 _[−]_ [1] [= max(0] _[, t]_ [2][)] _[ −]_ _[t]_ [2] _[,]_ _α_ 12 [0] [= max(0] _[, t]_ [1][)] _[,]_ (8.21)

_α_ 12 [1] [= max(0] _[,]_ [ 2] _[t]_ [1] _[,]_ [ 2] _[t]_ [1] [+] _[ t]_ [2][)] _[ −]_ [2 max(0] _[, t]_ [1][)] _[,]_ (8.22)

_α_ 11 = _α_ 22 = _t_ 1 + _t_ 2 _−_ max(0 _, t_ 1 _, t_ 1 + _t_ 2) _._ (8.23)


Restricting to the region _t_ 1 _>_ 0, where _K ̸_ = 0, they simplify to the headlight functions
become


_α_ 12 _[−]_ [1] [= max(0] _[, t]_ [2][)] _[ −]_ _[t]_ [2] _[,]_ _α_ 12 [0] [=] _[ t]_ [1] _[,]_ (8.24)

_α_ 12 [1] [= max(0] _[, t]_ [2][)] _[,]_ _α_ 11 = _t_ 2 _−_ max(0 _, t_ 2) _._ (8.25)


So, in fact, _K_ and _U_ take especially simple forms in coordinates:


_K_ = _t_ 1 _U_ = _t_ 1 + _|t_ 2 _|._ (8.26)
_t_ 1 + _|t_ 2 _|_ _[,]_


We will see below that these formulas continue to hold for the all-multiplicity formula.


                  - 22                  

**Figure** **7** : The Tree-Loop graph for the 1-loop non-planar amplitude.


**8.4** **The** **Tree-Loop** **Fatgraph**


To compute the _n_ -point amplitude, consider joining the two ends of the tadpole Γ _ℓ_ to
two comb tree graphs, Γ [1] and Γ [2], with _n_ 1 and _n_ 2 particles respectively. The result is
the Tree-Loop graph for the problem, Γ, as in Figure 7. In this section, we see how to
find the curves on Γ and their momenta explicitly.
The curves on Γ can be obtained from the curves on Γ _ℓ_ . For example, the curve
_C_ 12 [0] [can] [be] [extended] [to] [a] [path]

_Cij_ [0] [=] _[ W]_ [ 1] _i_ _[C]_ 12 [0]                  - _Wj_ [2]                  - _T_ _,_ (8.27)


that connects particle _i_ on trace-factor 1 and particle _j_ on trace-factor 2. Here, _Wi_ _[A]_ [is]
the path through the tree Γ _A_ from particle _i_ to the edge joining the tree to Γ _ℓ_, and ( ) _[T]_

denotes path-reversal. Similarly, a curve that begins and ends on a single trace-factor,
_A_, (with _A_ = 1 or 2) has a path of the form (with _i < j_ )


_Cij_ = _Wij_ _[A][,]_ or _Cji_ = _Wi_ _[A][C][AA]_           - _Wj_ _[A]_           - _T_ _,_ (8.28)


where _Wij_ _[A]_ [is] [the] [curve] [connecting] [particles] _[i, j]_ [in] [Γ] _[A]_ [that] [does] [not] [pass] [through] [Γ] _[ℓ]_ [.]
The momenta of curves on Γ also follow from the momentum assignment to curves
on the tadpole, Γ _ℓ_ . Let _p_ [1] _i_ [and] _[ p]_ _j_ [2] [(] _[i]_ [ = 1] _[, . . ., n]_ [1][,] _[ j]_ [= 1] _[, . . ., n]_ [2][) be the external momenta.]
By momentum conservation,



_n_ 1


_p_ [1] _i_ [=] _[ p][µ][,]_
_i_ =1



_n_ 2


_p_ [2] _j_ [=] _[ −][p][µ][.]_ (8.29)
_j_ =1



Then the momentum of _Cij_ [0] [,] [for] [example,] [is] [given] [by]


_Pij_ [0] [=] _[ ℓ]_ [+] _[ z]_ _j_ [2] _[−]_ _[z]_ _i_ [1] _[,]_ (8.30)


                  - 23                  

where recall that the curve _P_ 12 [0] [on] [the] [tadpole] [has] [momentum] _[ℓ]_ [.] [Here,]


_zi_ _[A]_ [=] _[ p]_ _i_ _[A]_ +1 [+] _[ · · ·]_ [ +] _[ p]_ _n_ _[A]_ _A_ (8.31)


are the dual-like variables on each trace-factor. (The general rule was given as equation
(6.4).) Similarly, the curves in (8.28) have momenta (with _A_ = 1 or 2)


_Pij_ _[A]_ [=] _[ p]_ _i_ _[A]_ +1 [+] _[ · · ·]_ [ +] _[ p]_ _j_ _[A][,]_ _Pji_ _[A]_ [=] _[ z]_ _j_ _[A]_ _[−]_ _[z]_ _i_ _[A][.]_ (8.32)


**8.5** **The** **All-multiplicity** **Amplitude**


We now use the Tree-Loop graph, Γ, to find the curve integral for the all-multiplicity
amplitude. We find that the end result is not that much more complicated than the
tadpole case. This is true in general, for reasons explained further in Section 9.
The MCG action on Γ is induced by the MCG on the tadpole, Γ _ℓ_ . It is generated
by the Dehn twist _γ_ ∆, which acts non-trivially only on the curves _Cij_ _[w]_ [,]


_Cij_ _[w]_ [=] _[ C]_ _i_ [1] _[C]_ 12 _[w]_ _[C]_ _j_ [2] _[,]_ (8.33)


that connect trace-factor 1 and trace-factor 2. Here, _C_ 12 _[w]_ [are] [the] [curves] [connecting] [1]
and 2 on the tadpole. _γ_ ∆ does not alter the tree-parts of the curve. So this set of curves
is decomposed into cosets: one coset for every pair _i, j_ of particles. Take _Cij_ [0] [as] [coset]
representatives. Then a Mirzakhani kernel is



_n_ 2



_j_ =1



_K_ =



_n_ 1



_i_ =1



_αij_ [0]
(8.34)
_ρ_ _[,]_



where _ρ_ is the sum

      _ρ_ = _αij_ _[w]_ (8.35)

_Cij_ _[w]_



over all such curves.
However, the telescopic property dramatically simplifies this expression. In particular,
_n_ 1 _n_ 2

     -      - [0] [0]



_n_ 2




_i_ =1





_αij_ [0] [=] _[ α]_ [0] _[,]_ (8.36)
_j_ =1



where _α_ [0] is the headlight function of the curve _C_ 12 [0] [on] [the] [tadpole] [graph.] [Likewise,] _[ρ]_
simplifies to
_ρ_ = _α_ _[−]_ [1] + _α_ [0] + _α_ [1] _,_ (8.37)


                  - 24                  

where we recall (from Section 8.3) that these are the only terms that contribute in the
region _α_ [0] = 0. So the all-multiplicity Mirzakhani kernel is


_α_ [0]
_K_ = (8.38)

_α_ _[−]_ [1] + _α_ [0] + _α_ [1] _[,]_


which is identical to the _K_ found for the tadpole.
In the region _α_ [0] = 0, _αC_ vanishes unless _C_ is a curve that does not intersect the
curve _C_ 12 [0] [on] [the] [fatgraph.] [In] [other] [words,] [the] [only] [curves] [we] [need] [to] [consider] [are]
those constructed from the special set of five curves


_C_ 11 _,_ _C_ 22 _,_ _C_ 12 _[−]_ [1] _[,]_ _C_ 12 [0] _[C]_ 12 [1] _[,]_ (8.39)


considered in Section 8.3. _U_ is a sum over all curves that carry a loop momentum.
These are the curves joining trace-factor 1 and trace-factor 2. So



_n_ 2


_αij_ _[w]_ [=] _[ α][−]_ [1][ +] _[ α]_ [0][ +] _[ α]_ [1] _[,]_ (8.40)
_j_ =1



_n_ 1



_i_ =1



_U_ =



1



_w_ = _−_ 1



which has again been simplified using the telescopic relation. Note that this _U_ is
identical to the one obtained for the tadpole case
Using the coordinate expressions for _K_ and _U_, equation (8.26), the all-multiplicity
amplitude is then given by



_D_

- 2 - _F_ 0 exp _−_ _._ (8.41)
_t_ 1 + _|t_ 2 _|_ _[−Z]_



_An_ 1 _,n_ 2 = - _d_ _[E]_ _t_ _t_ 1 + _t_ 1 _|t_ 2 _|_

_t_ 1 _>_ 0




- _π_
_t_ 1 + _|t_ 2 _|_



The remaining surface Symanzik polynomials are given by finite sums of curves. In
particular, _F_ 0 = _J_ _[µ]_ _Jµ_ where





_αij_ _[m]_ [(] _[z]_ _j_ [2] _[−]_ _[z]_ _i_ [1] [+] _[ wp]_ [)] _[.]_ (8.42)
_i,j_



_J_ _[µ]_ =



1



_w_ = _−_ 1



And _Z_ is a sum over the finite set of all curves that do not intersect _C_ 12 [0] [:]




- _αij_ _[w]_ �( _zj_ [2] _[−]_ _[z]_ _i_ [1] [+] _[ wp]_ [)][2][ +] _[ m]_ [2][�] _._ (8.43)

_i,j_



1



_w_ = _−_ 1



_Z_ = 

_A_ =1 _,_ 2




- _αij_ _[A]_ �� _Pij_ _[A]_ �2 + _m_ 2 [�] +


_i_ = _j_




- 25 

**8.6** **Comment** **on** **Evaluating** **the** **Curve** **Integral**


The curve integral formula for the amplitude, (8.41), has two parts. There is the
pre-factor




 - _π_
_K_
_U_



_D_

- 2
_,_ (8.44)



and the exponential part,

            -            -            _d_ _[E][−]_ [2] _t_ exp _−_ _[F]_ [0] _,_ (8.45)

_U_ _[−Z]_


which contains the kinematics. To evaluate the pre-factor, it was only necessary to
know the curve matrices for 3 curves on the tadpole graph. (These matrices are given
in appendix A.1.)
To evaluate the kinematic part, it was necessary to use the set of five curves on the
tadpole graph that are non-intersecting with _C_ 12 [0] [:]


_C_ 11 _,_ _C_ 22 _,_ _C_ 12 _[−]_ [1] _[,]_ _C_ 12 [0] _[,]_ _C_ 12 [1] _[.]_ (8.46)


Out of these five curves, we can build the relevant set of curves on Γ:


_Cij_ [1] _[,]_ _[C]_ _kl_ [2] _[,]_ _[C]_ _ik_ _[−]_ [1] _[,]_ _[C]_ _ik_ [0] _[,]_ _[C]_ _ik_ [1] _[,]_ (8.47)


for _i, j_ = 1 _, . . ., n_ 1, _k, l_ = 1 _, . . ., n_ 2 and _i ≤_ _j_, _k_ _≤_ _l_ . There are


3 _n_ 1 _n_ 2 + _n_ 1( _n_ 1 _−_ 2) + _n_ 2( _n_ 2 _−_ 2) (8.48)


such curves. The curve matrices for all these curves follow from taking products of the
five tadpole curve matrices (for the curves (8.46)), as well as the tree matrices


_Wij_ [1] _[,]_ _[W]_ [ 2] _kl_ _[,]_ _[W]_ [ 1] _i_ _[,]_ _[W]_ [ 2] _k_ _[,]_ (8.49)


which were computed in Section 3.3. There are

1 [1] (8.50)
2 _[n]_ [1][(] _[n]_ [1] _[ −]_ [1) +] 2 _[n]_ [2][(] _[n]_ [2] _[ −]_ [1)]


such matrices. So both the number of terms in the exponent of (8.45), and the number
of matrices needed to compute them, grow polynomially in _n_ 1 _, n_ 2.

### **9 Prefactors for All-multiplicity**


For the 1-loop double-trace amplitudes studied in Section 8, both the Mirzakhani kernel,
_K_, and the surface Symanzik polynomial, _U_, did not depend on the number of particles.
In this section, we explain that this _always_ happens, at all orders in perturbation theory,
when using a Tree-Loop graph.


                  - 26                  

**Figure** **8** : Turning a fatgraph into a surface.


**Figure** **9** : The two types of cosets that arise when forming the Mirzakhani kernel:
curves that lower the genus (left), and curves that decrease the number of trace-factors
(right).


**9.1** **Mirzakhani** **Kernels**


Consider any Tree-Loop graph, Γ, with _h_ trace-factors labelled _A_ = 1 _,_ 2 _, . . ., h_ . It can
be a useful book-keeping device when constructing the Mirzakhani kernel to also draw
the surface, _S_, obtained by fattening Γ. Examples of surfaces obtained from fatgraph
are in Figure 8. A path _C_ on Γ lifts to a curve on _S_, and one can draw _C_ on _S_ without
knowing its exact path.
There are two types of curves that arise when constructing the Mirzakhani kernel,
as shown in Figure 9. Starting from a fixed trace-factor, _A_, we consider the set of
curves, _SA_, that contain: all non-separating curves [6] that return to trace-factor _A_ ; and
all curves that connecting trace-factor _A_ to a second trace-factor _B_ ( _B_ = _A_ ).


6A non-separating curve is one that does not divide the surface into two regions.


                  - 27                  

The first step in constructing the Mirzakhani kernel is to consider the coset decomposition of the set of curves _SA_ under the MCG action. The set can be written as the
disjoint union
_SA_ = _SAA ⊔_             - _SAB,_ (9.1)


_B_ = _A_


where _SAB_ are the curves connecting distinct trace-factors, _A_ and _B_, and _SAA_ are the
set of non-separating curves that begin and end on trace-factor _A_ .
Any curve in the set _SAB_ can be written in the factorized form


_C_ = _Wi_ _[A][C][AB]_           - _Wj_ _[B]_           - _T_ _,_ (9.2)


for some external lines _i_ and _j_, and some curve _CAB_ connecting the two trace-factors
on the tadpole sub-graph, Γ _ℓ_ . The set _SAB_ decomposes into cosets, corresponding to
each possible choice of start and end points, _i_ and _j_ . Fix some choice of curve _CAB_ [0]
connecting the two trace-factors on the tadpole sub-graph, Γ _ℓ_ . Then the curves


_Cij_ [0] [=] _[ W][ A]_ _i_ _[C]_ _AB_ [0]                 - _Wj_ _[B]_                 - _T_ _,_ (9.3)


for each _i_ and _j_ can be taken as coset representatives. In building a Mirzakhani kernel,
we sum over each of these cosets, to obtain the following terms:



_nB_



_j_ =1



_KAB_ =



_nA_



_i_ =1



_αij_ [0]
(9.4)
_ρ_ _[.]_



where _nA_ and _nB_ are the number of particles on each trace-factor, and


      _ρ_ = _αC._ (9.5)


_C∈S_


The telescopic property gives a large simplification of the terms _KAB_ . The property
implies that

     
_αCij_ 0 [=] _[ α][C]_ _AB_ [0] _[.]_ (9.6)
_i,j_


So the terms in _KAB_ simplify to become

_KAB_ = _[α]_ _AB_ [0] (9.7)
_ρ_ _[.]_



Moreover, the telescopic property also simplifies the denominator, _ρ_, which can now be
written as



_ρ_ =



_h_




_B_ =1





_αCAB_ _,_ (9.8)

_CAB_




- 28 

where the second sum is over curves _CAB_ on the tadpole graph that connect _A_ and _B_ .
It follows that _KAB_ only depends on tadpole graph curves.
The analysis of the set _SAA_ of non-separating curves is similar. After applying the
telescopic property, the sum over cosets of this set gives


_KAA_ = _[α]_ _AA_ [0] (9.9)
_ρ_ _[,]_



for some choice of non-separating curve _CAA_ [0] [on] [the] [tadpole] [graph.] [The] [Mirzakhani]
kernel for the set _S_ is therefore



_K_ =



_h_




_B_ =1



_αAB_ [0] (9.10)
_ρ_ _[,]_



and this is precisely a Mirzakhani kernel for the tadpole graph, Γ _ℓ_ .
Inductively applying this result, to obtain a Mirzakhani kernel for the full MCG,
we can conclude that: _A_ _Mirzakhani_ _kernel_ _for_ _a_ _Tree-Loop_ _graph_ Γ _is_ _given_ _by_ _the_
_Mirzakhani_ _kernel_ _K_ _of_ _its_ _tadpole_ _sub-graph,_ Γ _ℓ._


**9.2** **The** **Surface** **Symanzik** **Polynomial**


The surface Symanzik function _U_ for a Tree-Loop fatgraph Γ also does not depend
on _n_ . This is because the loop momentum _ℓC_ carried by a curve, _C_ = _Ci_ _[A][C][AB][C]_ _j_ _[B]_ [,] [is]
just the loop momentum carried by the tadpole part of its path, _CAB_ . Similarly, the
loop momentum _ℓC_ carried by _C_ = _Ci_ _[A][C][AA][C]_ _j_ _[A]_ [is] [the] [loop] [momentum] [carried] [by] [the]
subpath _CAA_ . The entries of the Λ matrix can therefore be written as






_CAB_



Λ _[ab]_ =



_h_



_A,B_ =1





_ℓ_ _[a]_ _CAB_ _[ℓ]_ _C_ _[b]_ _AB_ _[α][C]_ _iABj_ _[,]_ (9.11)
_i,j_



where _CiABj_ = _Ci_ _[A][C][AB][C]_ _j_ _[B]_ [.] [By] [the] [telescopic] [property,]

     
_αCiABj_ = _αCAB_ _._ (9.12)

_i,j_


So it follows that the matrix entry Λ _[ab]_ for the Tree-Loop graph Γ is equal to the matrix
entry for the tadpole subgraph Γ _ℓ_ :



_C_
on Γ _ℓ_



Λ _[ab]_ =



_h_



_A,B_ =1




- 
_ℓ_ _[a]_ _CAB_ _[ℓ]_ _C_ _[b]_ _AB_ _[α][C]_ _AB_ [=]
_CAB_ _C_







_ℓ_ _[a]_ _C_ _[ℓ][b]_ _C_ _[α][C][.]_ (9.13)



We can conclude that: the surface Symanzik function for a Tree-Loop graph is equal
to the surface Symanzik _U_ of its tadpole sub-graph, Γ _ℓ_ .


                  - 29                  

### **10 Summary of Tree-Loop factorization**

In this section we summarize how Tree-Loop fatgraphs, and the general results in Sections 6 and 9, can be used in practice to compute amplitudes at arbitrary multiplicity.
In the subsequent sections, we then apply this method to all 2-loop amplitudes.
Let Γ be any Tree-Loop graph with _h_ trace-factors and _L_ loops. Let Γ _ℓ_ be its
tadpole subgraph. As a first step, we can compute a Mirzakhani kernel, _K_, for the
tadpole graph by analysing the MCG action on Γ _ℓ_ .
Given this _K_, recall that _K_ restricts the domain of integration. We can restrict
our attention to the finite set of curves, _S_, on Γ _ℓ_, that have non-vanishing headlight
functions on this domain. Using this set of curves, we can compute the surface Symanzik
polynomial
_U_ = det Λ _,_ (10.1)


where Λ is the _L × L_ Λ-matrix of the tadpole graph. This is computed by working out
the momentum assignments, _PC_, to the curves _C_ _∈S_ . Each momentum takes the form



_PC_ _[µ]_ [=] _[ K]_ _C_ _[µ]_ [+]



_L_


_ℓ_ _[a]_ _C_ _[ℓ][µ]_ _a_ _[,]_ (10.2)

_a_ =1



for some choice of loop momentum variables _ℓ_ _[µ]_ _a_ [.] [Then] [the] [Λ-matrix] [is]


      Λ _[ab]_ = _ℓ_ _[a]_ _C_ _[ℓ][b]_ _C_ _[α][C][,]_ (10.3)

_C∈S_


which is always a finite sum.
After these preliminaries, we have almost all the data needed to write down the
curve integral for all-multiplicity. The final result takes the form




   -   - _πL_
_A_ Γ = _d_ **t** _K_ _U_




- _D/_ 2 - exp _−_ _[F]_ [0] _,_ (10.4)

_U_ _[−Z]_



where _K_ and _U_ have already been computed.
The remaining two functions, _F_ 0 and _Z_ are given by sums over the finitely many
curves on Γ that can be produced by extending the curves _S_ to the full graph. In
particular,
_F_ 0 = _Jµ_ Λ [˜] _J_ _[µ]_ _,_ (10.5)


where Λ [˜] = det(Λ)Λ _[−]_ [1] denotes the adjugate of the Λ-matrix, and _J_ _[µ]_ is an _L_ -vector
given by
_J_ _[a,µ]_ =      -      - _ℓ_ _[a]_ _[α][C]_      - _K_ _[µ]_ [+] _[ z][B]_ _[−]_ _[z][A]_      - _._ (10.6)







_ℓ_ _[a]_ _C_ _[α][C]_ - _KC_ _[µ]_ _AB_ [+] _[ z]_ _j_ _[B]_ _[−]_ _[z]_ _i_ _[A]_ - _._ (10.6)



_CAB∈S_



_C_ = _Wi_ _[A][C][AB][W][ B]_ _j_


    - 30     

**Figure** **10** : The 2-loop planar tadpole.


The sum is over all curves _C_ = _Wi_ _[A][C][AB][W][ B]_ _j_ [that can be arrived at by extending a curve]
_CAB_ in the set _S_ to a curve on the full graph Γ. Likewise, _Z_ is given by a similar sum



_Z_ = 

_CAB∈S_




 

_C_ = _Wi_ _[A][C][AB][W][ B]_ _j_




- �2 _KC_ _[µ]_ _AB_ [+] _[ z]_ _j_ _[B]_ _[−]_ _[z]_ _i_ _[A]_ _αC_ +

_C_
tree



_KC_ [2] _[α][C][.]_ (10.7)



We also include in this sum curves _C_ = _Wij_ _[A]_ [which] [are] [entirely] [in] [the] [tree-part] [of] [the]
tree-loop graph. If we have already computed the momentum assignments, _PC_, for the
tadpole graph curves in _S_, these sums are easy to evaluate. In particular, the headlight
function _αC_, for a curve _C_ = _Wi_ _[A][C][AB][W][ B]_ _j_ [,] [is] [given] [by] [computing] [the] [curve] [matrix]


_MC_ = _Wi_ _[A]_ _[M][AB]_          - _Wj_ _[B]_          - _T_ _._ (10.8)


The _Wi_ _[A]_ [matrices] [have] [been] [computed] [for] [all-multiplicity] [in] [Section] [3.3][.]
In summary, to find the all-multiplicity formula for the amplitude, it suffices to
first study the tadpole graph. For the tadpole graph, one first derives a kernel, _K_, and
the corresponding finite set of curves, _S_, that are compatible with _K_ . For each of these
curves, _C_ _∈S_, one computes the corresponding curve matrix, _MC_, and momentum,
_PC_ = _ℓC_ + _KC_ . These data depend only on the tadpole subgraph Γ _ℓ_, and they suffice
to compute the all-multiplicity formula. The dependence on the particle data in _A_
enters only through the vector _J_ _[µ]_ and the function _Z_ . But the computation of these
functions explained above does not depend on the topology of the graph Γ _ℓ_ .

### **11 The Planar 2-Loop Amplitudes**


This section uses the Tree-Loop method described in Section 10 to compute the planar 2-loop amplitudes. Most of the computation is concerned with the planar 2-loop
tadpole, and then the all-multiplicity result is derived at the end.


                  - 31                  

**Figure** **11** : The closed curve, ∆, on the 2-loop planar tadpole graph.


**Figure** **12** : The surface picture obtained by fattening the tadpole graph, with two
MCG cosets: curves _C_ 0 _a_ that end in a spiral around _a_ (left) and curves _C_ 0 _b_ that end
in a spiral around _b_ (right).


**11.1** **MCG** **and** **Mirzakhani** **Kernel**


A 2-loop planar tadpole fatgraph, Γ _ℓ_, is given in Figure 10. The graph is planar, with
two closed loops we label _a_ and _b_ . There is one nontrivial closed curve on Γ _ℓ_, ∆, shown
in Figure 11. This closed curve has (anti-clockwise) path


∆= _zRyRzRwRxRwL._ (11.1)


Dehn twists around ∆, _γ_ ∆, generate the MCG of the graph.
To find a Mirzakhani kernel, consider how Dehn twists around ∆act on the set of
curves with one endpoint on the trace-factor. (To produce the Mirzakhani kernel, we
ignore curves that factorize Γ _ℓ_ into two graphs.) Using the surface diagram, Figure 12,
obtained by fattening Γ _ℓ_ to a surface, it is easy to identify that there are two cosets
under MCG: the curves _C_ 0 _a_ that end in a spiral around _a_, and the curves _C_ 0 _b_ that end
in a spiral around _b_ .
Exploring possible paths on the fatgraph, Γ _ℓ_, we identify two possible coset repre

                  - 32                  

sentatives,


_C_ 0 [0] _a_ [=] _[ LwR]_ [(] _[xL]_ [)] _[∞][,]_ and _C_ 0 [0] _b_ [=] _[ RzR]_ [(] _[yL]_ [)] _[∞][.]_ (11.2)


These are the shortest paths connecting 0 to a spiral around _a_ or _b_ . Other paths can
be obtained by acting with Dehn twists _γ_ ∆. Acting once with _γ_ ∆ gives paths


_C_ 0 [1] _a_ [=] _[ RzRyRzRwR]_ [(] _[xL]_ [)] _[∞][,]_ _C_ 0 [1] _b_ [=] _[ R]_ [∆] _[zR]_ [(] _[yL]_ [)] _[∞][.]_ (11.3)


Whereas acting with _γ_ ∆ (or twisting ‘clockwise’ around ∆) gives paths


_C_ 0 _[−]_ _a_ [1] [=] _[ LwLxLwLzLyLzRwR]_ [(] _[xL]_ [)] _[∞][,]_ _C_ 0 _[−]_ _b_ [1] [=] _[ LwLxLwLzR]_ [(] _[yL]_ [)] _[∞][.]_ (11.4)


The Mirzakhani kernel is then


0 _a_ 0 _b_
_K_ = _[α]_ [0] _[α]_ [0] (11.5)
_ρ_ [+] _ρ_ _[,]_



where _ρ_ is a sum over all curves of the form _C_ 0 _a_ or _C_ 0 _b_ that are compatible with either
_C_ 0 [0] _a_ [or] _[C]_ 0 [0] _b_ [.] [We] [write]

     -      _ρ_ = _αC_ + _αC_ _,_ (11.6)




- 
_αC_ 0 _a_ +
_C_ 0 _a∈S_ _C_ 0 _b_



_αC_ 0 _b,_ (11.6)
_C_ 0 _b∈S_



where _S_ be the set of _all_ curves on Γ _ℓ_ which are compatible with either _C_ 0 [0] _a_ [or] _[C]_ 0 [0] _b_ [.]
We find that there are 17 curves in _S_ . All of these curves and their paths are listed
in Appendix A.2.


**11.2** **Tadpole** **Curves** **and** **Momenta**


The tadpole fatgraph is planar, so the momentum assignments can be solved using dual
momentum variables: _x_ _[µ]_ 0 _[, x][µ]_ _a_ _[, x][µ]_ _b_ [.] [Curves] [that] [begin] [at] [the] [external] [line,] [0,] [and] [end] [in]
a spiral, _a_ or _b_, have propagators


_X_ 0 _a_ = ( _xa −_ _x_ 0) [2] + _m_ [2] _,_ _X_ 0 _b_ = ( _xb −_ _x_ 0) [2] + _m_ [2] _._ (11.7)


Likewise curves that begin spiraling around _a_ and end spiraling around _b_ have propagator
_Xab_ = ( _xa −_ _xb_ ) [2] + _m_ [2] _._ (11.8)


Finally, any curve that begins and ends at 0 has zero momentum. It is convenient to
set _x_ 0 = 0 and use _xa_ and _xb_ as loop momentum variables.
The Λ-matrix is constructed from the headlight functions _αC_ for curves _C_ that
carry loop momentum. But from this momentum assignment, it follows that the only
curves that carry loop momentum, _xa_ and _xb_, are the curves _C_ 0 _a, C_ 0 _b_, that have one


                  - 33                  

**Figure** **13** : The Tree-Loop fatgraph for the 2-loop planar amplitudes.


spiral, and any curve, _Cab_, that spirals around _a_ and spirals around _b_ . In fact, there
is just one curve _Cab_ . In the set of curves _S_, listed in Appendix A.2, we see that of a
total of 17 curves, only 9 of them carry loop momentum and appear in Λ.
Using (11.7) and (11.8), the Λ-matrix is




              - _αab_ + _α_ 0 _a_ _−αab_
Λ =
_−αab_ _αab_ + _α_ 0 _b_


Here, _α_ 0 _a, α_ 0 _b_ is a convenient notation for the sums




_._ (11.9)




 _α_ 0 _a_ =




- 
_αC_ 0 _a,_ _α_ 0 _b_ =
_C_ 0 _a∈S_ _C_ 0 _b_



_αC_ 0 _b._ (11.10)
_C_ 0 _b∈S_



The surface Symanzik polynomial, _U_, is given by _U_ = det Λ. Expanding the determinant as a sum of monomials gives


_U_ = _αabα_ 0 _a_ + _αabα_ 0 _b_ + _α_ 0 _aα_ 0 _b._ (11.11)


In summary, _K_ and _U_ can be computed from the headlight functions for a set
of 9 curves, whose paths are listed in Appendix A.2. In addition to these, _S_ has
an additional 8 curves which do not carry loop momentum. These 8 curves do not
contribute to computing _K_, _U_, _F_ 0, but are needed in what follows to compute when
computing _Z_ .


**11.3** **The** **Tree-Loop** **Fatgraph**


To find the all- _n_ amplitude, attach a tree graph Γ [0] to the external leg of the tadpole,
to obtain the Tree-Loop graph, Γ, in Figure 13.


                  - 34                  

Since Γ is still planar, the momenta of curves can still be assigned using dual
momentum variables, _x_ _[µ]_ _i_ [(for] _[ i]_ [ = 1] _[, . . ., n, a, b]_ [).] [If the external momenta are] _[ p][µ]_ _i_ [, we can]
take
_x_ _[µ]_ _i_ [=] _[ p]_ 1 _[µ]_ [+] _[ · · ·]_ [ +] _[ p]_ _i_ _[µ]_ _−_ 1 _[.]_ (11.12)


The propagator of a curve that connects line _i_ to line _j_ is then


_Xij_ = ( _xj_ _−_ _xi_ ) [2] + _m_ [2] _._ (11.13)


The propagators for a curve that begins at line _i_ and ends in a spiral ( _a_ or _b_ ) are


_Xia_ = ( _xa −_ _xi_ ) [2] + _m_ [2] _,_ _Xib_ = ( _xb −_ _xi_ ) [2] + _m_ [2] _._ (11.14)


We again take _xa, xb_ as loop momentum variables.
To compute _F_ 0 and _Z_, we need to enumerate the curves on Γ. But these are
obtained directly from the curves on the tadpole graph, Γ _ℓ_, by adding tree paths in all
possible ways. All the work was in enumerating the curves on Γ _ℓ_ . We find that the
complete list of loop-carrying curves on Γ is


_Cia_ = _WiC_ 0 _a,_ _Cib_ = _WiC_ 0 _b,_ _Cab_ (11.15)


for all curves _C_ 0 _a, C_ 0 _b_ _∈S_ on the tadpole fatgraph. In addition, we have curves that
do not carry loop momentum, (with _i ≤_ _j_ )


_Cij_ = _WiC_ 00 _Wj_ _[T]_ _[,]_ _Cij_ = _Wij,_ _Cji_ = _WiCB Wj_ _[T]_ _[,]_ (11.16)


for all tadpole curves _C_ 00 _∈S_, and where _CB_ is the boundary curve on the tadpole
fatgraph.
The paths for all the tadpole curves in _S_ are given in Appendix A.2 and can be
used to find the curve matrices _MC_ for all of these curves by taking matrix products.


**11.4** **The** **All-multiplicity** **Amplitude**


The resulting curve integral for the amplitude is (with _E_ = _n_ + 2)




   -   - _π_ 2
_An_ = _d_ _[E]_ _t K_ _U_




- _[D]_ 2 - exp _−_ _[F]_ [0] _,_ (11.17)

_U_ _[−Z]_



where _U, K_ are given by the tadpole calculation, equations (11.11) and (11.5). It
remains to find _F_ 0 and _Z_ .
The formulas for _F_ 0 and _Z_ then follow from the momentum assignments to these
curves. _F_ 0 is given by
_F_ 0 = _J_ _[T]_ [ ˜] Λ _J,_ (11.18)


                  - 35                  

where the vector _J_ follows from the momentum assignments, (11.14), and is given by














 _._ (11.19)



_αCia_
_Cia∈S_


_αCib_
_Cib∈S_



_J_ _[µ]_ =



_n_


_zi_ _[µ]_

_i_ =1







˜Λ is the matrix adjugate of the matrix, Λ, computed for the tadpole, (11.9). The
adjugate is




  - _αab_ + _α_ 0 _b_ _αab_
˜Λ =
_αab_ _αab_ + [�] _k_ _[α]_ 0 _[k]_ _a_




_._ (11.20)



Finally, _Z_ is a sum over all curves on Γ that can be obtained by from the set _S_,


_Z_ =          - _αC_ ( _KC_ [2] [+] _[ m]_ [2][)] _[,]_ (11.21)

_C_

where _KC_ _[µ]_ [is the part of the momentum of] _[ C]_ [that does not depend on] _[ z]_ _a_ _[µ][, z]_ _b_ _[µ]_ [.] [Explicitly,]
this is









  _αij_ + _αji_ + _αWiC_ 00 _W Tj_

_C_ 00 _∈S_



_Z_ =



_n_


_Xij_

_i<j_



_αCib_
_Cib∈S_







��




  _αCia_ +
_Cia∈S_ _Cib_



+



_n_


( _zi_ [2] [+] _[ m]_ [2][)]
_i_ =1



_._ (11.22)


### **12 The 2-Loop Triple-trace Amplitudes**

In the previous example, the MCG had only one generator, just as in the 1-loop doubletrace amplitudes. The triple-trace amplitudes are first example with a more interesting
MCG. The MCG in this case is still abelian, but has three generators.


**12.1** **MCG** **and** **Mirzakhani** **Kernel**


A triple-trace 2-loop tadpole fatgraph, Γ _ℓ_, is given in Figure 14. There are three
nontrivial closed curves on Γ _ℓ_, shown in Figure 15. These closed curves have the paths:


∆0 = _wRy_ 2 _Ry_ 2 _RwRzRx_ 2 _Rx_ 2 _RzL,_ (12.1)


∆1 = _x_ 1 _Rx_ 2 _L,_ ∆2 = _y_ 1 _Ly_ 2 _R._ (12.2)


Each of these closed curves surrounds one of the three trace-factors. Dehn twists
around each of these ∆ _i_, _γ_ ∆ _i_, generate the MCG. The ∆ _i_ curves in Figure 15 are nonintersecting. It follows that the Dehn twists around the ∆ _i_ commute, and the MCG is
isomorphic to Z [3] .


                  - 36                  

**Figure** **14** : A 2-loop triple-trace tadpole graph.


To find a Mirzakhani kernel, consider one trace-factor at a time. A curve, _CAB_,
connecting trace-factors _A_ and _B_, intersects ∆ _A_ and ∆ _B_, and is acted on by Dehn
twists around these two curves. Consider the curves with one endpoint on trace-factor
0. From the surface diagram, Figure 16, these curves decompose into two cosets: the
curves _C_ 01 connecting 0 and 1, and the curves _C_ 02 connecting 0 and 2.
Exploring paths on the fatgraph, Γ _ℓ_, we identify two possible coset representatives:


_C_ 01 [00] [=] _[ LzLx]_ [2] _[R,]_ _C_ 02 [00] [=] _[ RwRy]_ [2] _[L.]_ (12.3)


These are the shortest paths in the two cosets. Other paths in these cosets can be
obtained by acting with the Dehn twists: _γ_ ∆0 _, γ_ ∆1 _, γ_ ∆2. Write


      -      _ρ_ = _αC_ 01 + _αC_ 02 (12.4)


for the sum over curves with a single endpoint on trace-factor 0.
The stabilizer of _C_ 01 [00] [is] [generated] [by] _[γ]_ [∆] 2 [.] [To] [mod] [out] [by] [the] [stabilizer,] [consider]
the set of curves connecting 1 and 2. From the surface diagram, Figure 16, it can be
seen that these curves form two cosets. Looking for curves compatible with _C_ 01 [00][,] [we]
find


_C_ 12 [01] [=] _[ Rx]_ [1] _[LzLwLy]_ [1] _[R,]_ _C_ 12 [11] [=] _[ Lx]_ [2] _[RzLwLy]_ [1] _[R,]_ (12.5)


which can be taken as coset representatives. Note that _C_ 12 [10] [is] [obtained] [from] _[C]_ 12 [00] [by]
acting with _γ_ ∆1.
Likewise, the stabilizer of _C_ 02 [00] [is] [generated] [by] _[γ]_ [∆] 1 [.] [To] [mod] [out] [by] [this] [stabilizer,]
again consider the curves connecting 1 and 2. From the surface diagram, Figure 16,
it can be seen that these curves form two cosets. Looking for curves compatible with
_C_ 02 [00][,] [we] [find]


_C_ 12 [00] [=] _[ Rx]_ [1] _[LzLwRy]_ [2] _[L,]_ _C_ 12 [01] [=] _[ Lx]_ [1] _[LzLwLy]_ [1] _[R,]_ (12.6)


                  - 37                  

**Figure** **15** : The three nontrivial closed curves, ∆0 _,_ ∆1 _,_ ∆2, on the 2-loop triple-trace
tadpole graph.


which can be taken as coset representatives.
A Mirzakhani is then


_K_ = _[α]_ 01 [00] _[α]_ 12 [01] + _[α]_ 01 [00] _[α]_ 12 [11] + _[α]_ 02 [00] _[α]_ 12 [00] + _[α]_ 02 [00] _[α]_ 12 [01] _,_ (12.7)
_ρρ_ _[′]_ _ρρ_ _[′]_ _ρρ_ _[′]_ _ρρ_ _[′]_


where _ρ_ _[′]_ is a sum

      _ρ_ _[′]_ = _αC_ 12 (12.8)


over curves connecting 1 and 2. Only finitely many curves appear in _ρ_ and _ρ_ _[′]_ . Namely,
only curves compatible with one of the pairs of curves appearing in the numerators of
_K_ .
Let _S_ be the set of _all_ curves on Γ _ℓ_ which are compatible with one of the pairs of
curves appearing in the numerators of _K_ .
We find that there are 33 curves in _S_ . 24 of these are curves that carry loop
momentum, and so appear in _U_, _K_ and _F_ 0. Whereas 9 of these are curves do not carry
loop momentum and only contribute to _Z_ . All 33 of these curves and their paths are
listed in Appendix A.4.


**12.2** **Tadpole** **Curves** **and** **Momenta**


The momentum assignment rule shows that the closed curves have momenta


_P_ ∆0 = _p_ 0 _,_ _P_ ∆1 = _p_ 1 _,_ _P_ ∆2 = _p_ 2 _._ (12.9)


                  - 38                  

**Figure** **16** : The surface obtained by fattening the tadpole fatgraph, and the four
MCG-inequivalent cuts of the surface that give the Mirzakhani kernel.


A momentum routing can be chosen such that


_P_ 01 [00] [=] _[ ℓ]_ [1] _[,]_ _P_ 02 [00] [=] _[ ℓ]_ [2] _[,]_ _P_ 12 [00] [=] _[ ℓ]_ [1] [+] _[ ℓ]_ [2] _[,]_ (12.10)


for some loop momentum variables _ℓ_ 1 _, ℓ_ 2. Acting with the MCG, we obtain all other
curves. A Dehn twist by ∆ _i_ acting on _Cij_ adds _±pi_ to its momentum. So:


_P_ 01 _[ab]_ [=] _[ ℓ]_ [1] [+] _[ ap]_ [0] [+] _[ bp]_ [1] _[,]_ (12.11)

_P_ 02 _[ab]_ [=] _[ ℓ]_ [2] [+] _[ ap]_ [0] [+] _[ bp]_ [2] _[,]_ (12.12)

_P_ 12 _[ab]_ [=] _[ ℓ]_ [1] [+] _[ ℓ]_ [2] [+] _[ ap]_ [1] [+] _[ bp]_ [2] _[.]_ (12.13)


Finally, the curves that begin and end at the same trace-factor are homologous to
the boundaries of the fatgraph. This means that the momentum of such a curve _CAA_
( _A_ = 0 _,_ 1 _,_ 2) is a linear combination of the boundary momenta: _p_ 0 _, p_ 1 _, p_ 2.
The Λ-matrix is constructed from _αC_ for curves _C_ that carry loop momentum.
The only curves carrying loop momenta are those curves connecting two distinct tracefactors. Given (12.10), the Λ-matrix is




  - _α_ 01 + _α_ 12 _α_ 12
Λ =
_α_ 12 _α_ 02 + _α_ 12




_,_ (12.14)



where

       _αAB_ = _αCAB_ (12.15)

_CAB∈S_

is the sum over those curves _CAB_ _∈S_, connecting trace-factors _A_ and _B_, that are
compatible with the Mirzakhani kernel, _K_ . The surface Symanzik polynomial _U_ is
given by
_U_ = det Λ = _α_ 01 _α_ 02 + _α_ 01 _α_ 12 + _α_ 02 _α_ 12 _._ (12.16)


                  - 39                  

**12.3** **The** **All-multiplicity** **Amplitudes**


To find the all-multiplicity amplitudes, attach tree comb graphs Γ [0] _,_ Γ [1] _,_ Γ [2] to Γ _ℓ_, to
obtain the Tree-Loop graph, Γ. Let the number of external particles on each tracefactor be _n_ 0 _, n_ 1 _, n_ 2, respectively, with _n_ = _n_ 0 + _n_ 1 + _n_ 2. From a curve _CAB_ on Γ _ℓ_, we
obtain curves of the form
_CiABj_ = _Wi_ _[A][C][AB]_               - _Wj_ _[B]_               - _T_ (12.17)


connecting particle _i_ on trace-factor _A_ to particle _j_ on trace-factor _B_ . The momentum
assigned to such a curve is (see Section 10)


_PCiABj_ = _PCAB_ + _zj_ _[B]_ _[−]_ _[z]_ _i_ _[A][.]_ (12.18)


And the headlight function _αC_ is obtained by multiplying the matrix _MCAB_ with the
tree matrices _Wi_ _[A]_ [and] - _Wj_ _[B]_ - _T_ .
The curve integral for the amplitude is then (with _E_ = _n_ )




     -     - _π_ 2
_An_ 1 _,n_ 2 _,n_ 3 = _d_ _[E]_ _t K_ _U_




- _[D]_ 2 - exp _−_ _[F]_ [0] _._ (12.19)

_U_ _[−Z]_



Here, _K_ and _U_ are given as above by the tadpole calculation (equations (12.7) and
(12.16)).
The formulas for _F_ 0 and _Z_ follow from the momentum assignments. For a curve
_CiABj_ connecting trace-factors _A_ and _B_, write


_PC_ = _KC_ + _ℓCAB_ _,_ (12.20)


where _ℓCAB_ is the part depending on the loop momentum variables. From (12.10),


_ℓC_ 01 = _ℓ_ 1 _,_ _ℓC_ 02 = _ℓ_ 2 _,_ _ℓC_ 12 = _ℓ_ 1 + _ℓ_ 2 _._ (12.21)


It follows that J is




 

_C_ 01 _∈S_
_C_ = _Wi_ [0] _[C]_ [01][(] _[W]_ [ 1] _j_ [)] _T_

 

_C_ 02 _∈S_
_C_ = _Wi_ [0] _[C]_ [02][(] _[W]_ [ 2] _j_ [)] _T_




  _KC αC_ +

_C_ 12 _∈S_
_C_ = _Wi_ [1] _[C]_ [12][(] _[W]_ [ 2] _j_ [)] _T_

  _KC αC_ +

_C_ 12 _∈S_
_C_ = _Wi_ [1] _[C]_ [12][(] _[W]_ [ 2] _j_ [)] _T_






_,_ (12.22)





_J_ =









_KC αC_


_KC αC._



Then _F_ 0 is, as usual _F_ 0 = _J_ _[T]_ [ ˜] Λ _J_, where the adjugate matrix of Λ is




  - _α_ 02 + _α_ 12 _−α_ 12
˜Λ =
_−α_ 12 _α_ 01 + _α_ 12


     - 40     



_._ (12.23)


**Figure** **17** : The 2-loop genus-one tadpole fatgraph.



Finally,
_Z_ =         

_CAB∈S_





(( _KC_ ) [2] + _m_ [2] ) _αC,_ (12.24)

_C_



where the second sum is over curves _C_ = _Wi_ _[A][C][AB]_ - _Wj_ _[B]_ - _T_ formed by extending _CAB_ to
a curve on Γ.
As in the previous examples, evaluating the curve integral for _An_ 1 _,n_ 2 _,n_ 3 is simplified
by using the form of the Mirzakhani kernel _K_, which has four terms. So the amplitude
is a sum of four curve integrals. For example, the monomial _α_ 01 [00] _[α]_ 02 [00] [appears] [in] _[K]_ [.]
Restricting to the region _α_ 01 [00] _[α]_ 02 [00][, the curve integral simplifies.] [Cutting Γ] _[ℓ]_ [along] _[ C]_ 01 [00] _[, C]_ 02 [00]
gives a 7-point tree graph, which has 14 possible curves. So this contribution to _An_ 1 _,n_ 2 _,n_ 3
can be computed using 14 matrices, valid for all multiplicities.

### **13 The 2-Loop Amplitudes at Genus One**


The first non-planar contribution to the single trace amplitude at two loops is given by
genus one diagrams. These give a first example of a non-abelian Mapping Class Group,
which is isomorphic in this case to SL2Z _×_ Z.


**13.1** **MCG** **and** **Mirzakhani** **Kernel**


The genus-one tadpole fatgraph, Γ _ℓ_, is given in Figure 17. There are three non-trivial
closed curves on Γ _ℓ_ . These closed curves are shown in Figure 18 and they have paths:


∆ _A_ = _y_ 1 _Ry_ 2 _Ly_ 3 _R,_ ∆ _B_ = _y_ 1 _Ry_ 2 _Ry_ 4 _L,_ (13.1)


∆0 = _y_ 1 _Ry_ 2 _Ry_ 4 _Ry_ 3 _Ry_ 2 _Ly_ 1 _Ry_ 4 _Ry_ 3 _R._ (13.2)


                  - 41                  

**Figure 18** : The three closed curves, ∆0 _,_ ∆1 _,_ ∆2, on the 2-loop genus-one tadpole graph.
Dehn twists around these curves generate a Z _×_ SL2Z Mapping Class Group.


∆0 is the closed curve surrounding the trace-factor of the fatgraph. ∆ _A_ and ∆ _B_ are
homologous to the A- and B- cycles of the torus (if Γ _ℓ_ is drawn embedded on the torus).
Dehn twists _γ_ ∆ around these closed curves generate MCG. ∆0 does not intersect
either of ∆ _A_ or ∆ _B_, so _γ_ ∆0 commutes with the other two Dehn twists. Whereas ∆ _A_
and ∆ _B_ intersect, so that Dehn twists around these closed curves do _not_ commute.
Since ∆ _A_ and ∆ _B_ are the A- and B- cycles of the torus, these Dehn twists generate
the MCG of the torus, which gives an SL2Z subgroup of the full MCG. The MCG is
therefore isomorphic to Z _×_ SL2Z.
All open curves on Γ _ℓ_ begin and end on the external line, 0. Furthermore, all curves
are equivalent up to MCG and therefore belong to the same coset.
Exploring curves on the fatgraph, we find a short path


_C_ 1 = _Ly_ 2 _Ry_ 4 _Ly_ 1 _L_ (13.3)


which can be taken as coset representatives for the unique MCG coset. Note that _C_ 1
intersects ∆ _A_ and ∆0, but _not_ ∆ _B_ . So the stabilizer of this curve is the Z subgroup
generated by _γ_ ∆ _B_ . Write

      _ρ_ = _αC_ (13.4)


for the sum over all curves _C_ that are compatible with _C_ 1. Then

_KA_ = _[α]_ [1] (13.5)

_ρ_


is a Mirzakhani kernel that partially mods out by MCG, but does not mod out by the
stabilizer generated by _γ_ ∆ _B_ .
Cutting the surface along _C_ 1 gives an annulus with two marked points on one
boundary, and one marked point on the other. ∆ _B_ is the closed loop on the annulus
and generates the MCG of the annulus, which is a Z subgroup of the full MCG. So the


                  - 42                  

**Figure** **19** : The four MCG-inequivalent pairs of curves that cut the torus to a disk.
Each pair of curves corresponds to a distinct term in the Mirzakhani kernel, _K_ .


curves compatible with _C_ 1 decompose into two cosets under this Z subgroup: depending
on their endpoints on the cut surface.
To mod out by the stabilizer, we need to find curves that intersect ∆ _B_ and are
compatible with _C_ 1. We find, for example, the paths


_C_ 2 = _Ly_ 2 _Ly_ 3 _Ry_ 1 _L,_ _C_ 3 = _Ry_ 1 _Ry_ 4 _Ry_ 3 _Ry_ 1 _Ry_ 2 _Ry_ 4 _Ly_ 1 _L._ (13.6)


These are both compatible with _C_ 1, intersect ∆ _B_, but are not related to each other by
_γ_ ∆ _B_ (on the cut surface, the annulus, they connect distinct pairs of endpoints). So we
can take _C_ 2 and _C_ 3 as our two coset representatives.
Write

       _ρB_ = _αC_ (13.7)


for the sum over all curves, _C_, which are compatible with _C_ 1 and which intersect ∆ _B_ .
Then the final Mirzakhani kernel for the full MCG is




[1] _α_ 2 + _α_ 3

_ρ_ _ρB_



_K_ = _[α]_ [1]



_._ (13.8)
_ρB_



The two terms in _K_ correspond to the two MCG-inequivalent cuts shown in Figure 19.
Let _S_ be the set of all curves which are compatible with one of the two pairs of
curves appearing in the numerators of _K_ . There are 10 curves in _S_ . Of these, 9 curves
carry loop momentum, and contribute to the computation of _K_ and _U_ . Only 1 curve
in the set does not carry loop momentum: the curve _C_ 00 that follows the boundary of
Γ _ℓ_, and carries zero momentum:


_C_ 00 = _Ly_ 2 _Ly_ 3 _Ly_ 4 _Ly_ 2 _Ly_ 1 _Ly_ 3 _Ly_ 4 _Ly_ 1 _L._ (13.9)


The paths for all 10 of the curves in _S_ are listed in Appendix A.5.


                  - 43                  

**13.2** **Momentum** **Assignments**


By momentum conservation, the external momentum entering the tadpole graph is zero.
Assign a momentum routing to the graph by assigning edge 4 the loop momentum
variable _ℓ_ _[µ]_ 1 [,] [and] [edge] [3] [the] [loop] [momentum] [variable] _[ℓ][µ]_ 2 [.] [Then] [the] [momenta] [of] [the]
closed curves are
_P_ ∆0 = 0 _,_ _P_ ∆ _A_ = _ℓ_ 1 _,_ _P_ ∆ _B_ = _ℓ_ 2 _._ (13.10)


Moreover this momentum routing induces a momentum assignment to all open curves.
For example, using the momentum assignment rule,


_PC_ 1 = _ℓ_ 2 _,_ _PC_ 2 = _ℓ_ 1 _,_ _PC_ 3 = _ℓ_ 1 _._ (13.11)


Another way to understand this momentum assignment is that, on the surface (Figure
19), the curve _C_ 1 (red in the figure) is homologous to ∆ _B_ (ignoring the boundary tracefactor), and so has the same momentum as ∆ _B_ . Likewise, the curves _C_ 2 and _C_ 3 (blue
in the figure) are homologous to ∆ _A_ . [7]

Now consider any curve _C_ in the set _S_ . The momentum assigned to _C_ is necessarily
a linear combination of _ℓ_ 1 and _ℓ_ 2. It is convenient to write


_C_ = _C_ _[p/q]_ [;] _[w]_ (13.12)


for any such curve _C_ with momentum


_PCp/q_ ; _w_ = _pℓ_ 1 + _qℓ_ 2 _._ (13.13)


Here, _w_ is an arbitrary index that distinguishes distinct curves that carry the same
loop momentum. For example, we can write _C_ 1 = _C_ [0] _[/]_ [1;0], _C_ 2 = _C_ [1] _[/]_ [0;0], _C_ 3 = _C_ [1] _[/]_ [0;1] .
The Λ-matrix follows from the momentum assignments, (13.13). It is given by




 _p_ [2] _αC_


_C_ = _C_ _[p/q]_ [;] _[w]_
_C∈S_

  _pq αC_


_C_ = _C_ _[p/q]_ [;] _[w]_
_C∈S_




 

_C_ = _C_ _[p/q]_ [;] _[w]_
_C∈S_

 

_C_ = _C_ _[p/q]_ [;] _[w]_
_C∈S_






_,_ (13.14)




Λ =









_pq αC_


_q_ [2] _αC_



These sums exclude the one curve, _C_ 00, that does not carry loop momentum. The
surface Symanzik polynomial _U_ is then the determinant, _U_ = det Λ.


7As explained in [1], the momenta assigned to curves, _PC_ _[µ]_ [,] [satisfy] [the] [same] [additive] [relations] [as]
the classes of curves in homology.


                  - 44                  

As an aside, note that this determinant can be expanded as the sum over pairs
_C, D_ of curves in _S_ :



2
_αC αD._ (13.15)



����




  det Λ =


_C_ = _C_ _[p/q]_ [;] _[w]_

_D_ = _C_ _[r/s]_ [;] _[w][′]_



_p_ _r_
���� _q_ _s_



It can be checked that the determinant factors appearing in this sum, ( _ps −_ _qr_ ) [2], are
equal to 1 if and only if the two curves _C_ and _D_ cut Γ _ℓ_ to a tree. Otherwise the
determinant factor is zero. So _U_ is precisely a sum over maximal cuts of Γ _ℓ_ that can
be formed from the set _S_ :
_U_ =            - _αCαD._ (13.16)


_C,D∈S_
max. cut


**13.3** **The** **All-multiplicity** **Amplitudes**


To find the all-mulitplicity genus-one amplitudes, attach a tree comb graph, Γ [0], to the
external leg of Γ _ℓ_, to obtain a Tree-Loop graph, Γ. Let Γ have _n_ external legs. From
any curve _C_ _[p/q]_ [;] _[w]_ _∈S_ on Γ _ℓ_, we can obtain a curve


_Cij_ _[p/q]_ [;] _[w]_ = _WiC_ _[p/q]_ [;] _[w]_ ( _Wj_ ) _[T]_ _,_ (13.17)


connecting particles _i_ and _j_, and such a curve has momentum (see Section 10)


_Pij_ _[p/q]_ [;] _[w]_ = _PCp/q_ ; _w_ + _zj_ _−_ _zi._ (13.18)


The headlight functions for these curves are obtained by matrix multiplication from the
_n_ tree-level matrices _Wi_ ( _i_ = 1 _, . . ., n_ ) and the 10 matrices _MC_ for the curves _C_ _[p/q]_ [;] _[w]_ in
_S_ .
Note that there are also a set of curves that do not carry loop momentum and have
tree-like propagators. These are (for _i < j −_ 1)


_Cij_ = _Wij,_ (13.19)


with momentum _Pij_ = _pi_ + _· · ·_ + _pj−_ 1, and also (for _i ≤_ _j_ )


_Cji_ = _WiCB_ ( _Wj_ ) _[T]_ _,_ (13.20)


with momentum _Pji_ = _pi_ +1 + _· · ·_ + _pj_ .
The curve integral for the amplitude is then (with _E_ = _n_ + 2)




   -   - _π_ 2
_An_ = _d_ _[E]_ _t K_ _U_




- _[D]_ 2 - exp _−_ _[F]_ [0] _._ (13.21)

_U_ _[−Z]_




- 45 

**Figure** **20** : A tadpole graph for the 2-loop double-trace amplitudes.



Here, _K_ (equation (13.8)) and _U_ (equation (13.14)) are computed using the 13 curves
_C_ _[p/q]_ [;] _[w]_ in _S_ .
The formulas for _F_ 0 and _Z_ follow from the momentum assignments. The vector
_J_ _[µ]_ is
















 

_C_ _[p/q]_ [;] _[w]_ _∈S_
_C_ = _WiC_ _[p/q]_ [;] _[w]_ _Wj_ _[T]_

 

_C_ _[p/q]_ [;] _[w]_ _∈S_
_C_ = _WiC_ _[p/q]_ [;] _[w]_ _Wj_ _[T]_



_p αC zij_ _[µ]_


_q αC zij_ _[µ]_



_J_ _[µ]_ =







_,_ (13.22)



where _zij_ _[µ]_ [=] _[ z]_ _j_ _[µ]_ _[−]_ _[z]_ _i_ _[µ]_ [.] [Then] _[F]_ [0] [=] _[ J][ T]_ [ ˜Λ] _[J]_ [,] [where] [˜Λ] [is] [the] [the] [adjugate] [of] [the] [Λ-matrix]
(equation (13.14)). Finally,



_Z_ = 

_C∈S_
_D_ = _WiCWj_ _[T]_




- _zij_ [2] [+] _[ m]_ [2][�] _αD_ +



_j_ = _n_



_i_ =1
_i<j−_ 1




- _zji_ [2] [+] _[ m]_ [2][�] _αCij_ _._ (13.23)


### **14 The 2-Loop Double-trace Amplitudes**

To complete our list of 2-loop amplitude formulas, we give here a curve integral formula
for the 2-loop double-trace amplitudes. The analysis is very similar to the computations
in the foregoing sections.


**14.1** **MCG** **and** **Mirzakhani**


The double-trace tadpole fatgraph, Γ _ℓ_, is given in Figure 20. The MCG is generated
by Dehn twists around the closed curves, ∆1 and ∆2, that surround trace-factor 1 and
trace-factor 2 of Γ _ℓ_, respectively. ∆1 and ∆2 are non-intersecting, and so these two
Dehn twists commute, and the MCG is isomorphic to the free abelian group Z [2] .


                  - 46                  

**Figure** **21** : The surface obtained by fattening the double-trace 2-loop fatgraph is a
sphere with one puncture and two trace-factors. There are five MCG-inequivalent cuts
of this surface to a disk, which appear in the Mirzakhani kernel, _K_ . Note that the first
two (and the last two) cuts are MCG-inequivalent due to the different order in which
the curves are incident at the trace-factors.


Using the surface diagram, Figure 21, one can identify the MCG cosets. In fact,
there are five MCG-inequivalent cuts of the surface to a disk (shown in the figure).
Exploring paths on the tadpole fatgraph, Γ _ℓ_, we find that the following five pairs of
curves can be taken as representatives for the five cuts:


( _C_ 1 [0] _,_ 0 _[, C]_ 1 [1] _,_ _[,]_ 2 [0][)] _[,]_ ( _C_ 1 [0] _,_ 0 _[, C]_ 1 [0] _,_ _[,]_ 2 [0][)] _[,]_ ( _C_ 1 [0] _,_ 0 _[, C]_ 2 [0] _,_ 0 [)] _[,]_ ( _C_ 2 [0] _,_ 0 _[, C]_ 1 [0] _,_ _[,]_ 2 [0][)] _[,]_ ( _C_ 2 [0] _,_ 0 _[, C]_ 1 [0] _,_ _[,]_ 2 [1][)] _[,]_ (14.1)


where the explicit paths for the 5 curves appearing here are given in Figure 22. The
paths for these curves are also listed in Appendix A.3. We have chosen to label curves
as _CAB_ _[w]_ [, where] _[ A]_ [ and] _[ B]_ [(] _[A, B]_ [= 0] _[,]_ [ 1] _[,]_ [ 2) are trace-factors that the curve begins and ends]
on. _A_ = 0 is the trace-factor with no particles. _w_ is some decoration to distinguish
distinct curves with the same endpoints.
Let _S_ be the finite set of curves compatible with at least one of the five cuts in
equation (14.1). All curves in this set and their paths are listed in Appendix A.3. There
are 23 curves in total, of which 14 curves connect distinct trace-factors. Consider the
sum, _U_, over all possible cuts that can be formed from the set of curves _S_ :


_U_ = _α_ 01 _α_ 12 + _α_ 01 _α_ 02 + _α_ 02 _α_ 12 _,_ (14.2)


where _αAB_ is a sum over curves in _S_ connecting trace-factors _A_ and _B_,


      _αAB_ = _αCAB_ _._ (14.3)

_CAB∈S_


Then a Mirzakhani kernel is given by


10 _[α]_ 12 [10] [+] _[ α]_ 10 [0] _[α]_ 12 [00] [+] _[ α]_ 10 [0] _[α]_ 20 [0] [+] _[ α]_ 20 [0] _[α]_ 12 [00] [+] _[ α]_ 20 [0] _[α]_ 12 [01]
_K_ = _[α]_ [0] _._ (14.4)
_U_


                  - 47                  

**Figure** **22** : The five curves on Γ _ℓ_ which we use to construct all five MCG-inequivalent
cuts.


**14.2** **The** **All-multiplicity** **Amplitudes**


To assign momenta to the curves in the set _S_, choose a routing of momenta on Γ _ℓ_
(Figure 20) such that edge _x_ 1 has momentum _ℓ_ _[µ]_ 1 [and] [edge] _[x]_ [2] [has] [momentum] _[ℓ][µ]_ 2 [,] [for]
some loop momentum variables, _ℓ_ 1 _, ℓ_ 2. Let _p_ 1 = _p_ and _p_ 2 = _−p_ be the momenta of the
two trace-factors. Then the momentum assignment rule gives, for example,


_PC_ 010 [=] _[ ℓ]_ [1] _[,]_ _PC_ 020 [=] _[ ℓ]_ [2] _[.]_ (14.5)


The only curves that carry a loop momentum are those connecting distinct trace-factors.
In Appendix A.3, these curves are labelled such that their momenta are given by


_PC_ 12 _[w]_ 1 _[,w]_ 2 = _ℓ_ 1 _−_ _ℓ_ 2 + ( _w_ 1 _−_ _w_ 2 _−_ 1) _p,_ (14.6)

_PC_ 01 _[w]_ [=] _[ ℓ]_ [1][ +] _[ wp,]_ (14.7)

_PC_ 02 _[w]_ [=] _[ ℓ]_ [2] _[ −]_ _[wp.]_ (14.8)


In the notation of the summary, Section 10, these curves have momentum


_PC_ _[µ]_ [=] _[ K]_ _C_ _[µ]_ [+] _[ ℓ]_ _C_ [1] _[ℓ]_ 1 _[µ]_ [+] _[ ℓ]_ _C_ [2] _[ℓ]_ 1 _[µ][,]_ (14.9)


where _ℓC_ 12 = (1 _, −_ 1), _ℓC_ 01 = (1 _,_ 0) and _ℓC_ 02 = (0 _,_ 1).
The all-multiplicity amplitude is then given by




  -   - _π_ 2
_A_ = _d_ _[E]_ _t K_

_U_




- _[D]_ 2 - exp _−_ _[F]_ [0] _,_ (14.10)

_U_ _[−Z]_



where _K_ is given by (14.4), _U_ is given by (14.2). _F_ 0 and _Z_ are given by the formulas
in Section 10, with the momenta assignments as above.


                  - 48                  

### **15 Outlook**

This paper opens a systematic investigation of all-loop scattering amplitudes in the tr _ϕ_ [3]

theory at all _n_ . We have seen that certain especially simple fatgraph representatives
for the curve integral formalism manifest a remarkable decoupling of _n_ and _L_, and we
illustrated this at all _n_ for all amplitudes in the theory through to two loops.
In practice, the computations described in this paper are best done using a computer. The curve integral formalism is based on simple combinatorial rules, which are
very amenable to implement in code. This will play an important role in applications of
these formulas beyond two-loops. One possible application of these computer methods
could lie in the numerical evaluation of amplitudes. Tropical methods have recently
proved useful for the evaluation of individual Feynman integrals. [4, 5]
The key result that underlies all the formulas in this paper is the existence of an
explicit positive parametrization for Teichm¨uller spaces, which is most closely related
to the point of view of [6]. This parametrization is given by the definition of the socalled _u_ -variables as rational functions in positive _y_ -variables. [1]. However, to arrive at
formulas for amplitudes, we have to take the tropicalization of this parametrization. [8]

Tropical moduli spaces have a rich topological structure, which is an active area of
research. [9] It remains to be seen what importance these topological facts about tropical
moduli spaces have for the new formulas in this paper, which compute amplitudes as
integrals over tropical moduli spaces.
We close by discussing in greater detail some particularly interesting physics questions to explore using the results in this paper.


**15.1** **Large** _n_ **limits**


Perhaps the most striking fact about the curve integral formulas is that an integral over
a _∼_ _n_ dimensional space, built out of _∼_ _n_ [2] simple _headlight_ _functions_, each with no
more than _∼_ _n_ terms, magically produces the amplitude: which is naively the sum over
_∼_ 4 _[n]_ Feynman diagrams. This suggests that the curve integral can be used to define
a sensible large _n_ limit of amplitudes. Large _n_ limits have been studied for certain
special cases, [10, 11] and processes with multi-state emission of many particles may
be important in phenomenomology.
Clearly, the external kinematics should be chosen carefully for the large _n_ limit to
be well-defined. For instance, we can pick a smooth curve _C_ in some _D_ dimensional


8The headlight functions, _αC_ ( _t_ ), are defined as the tropicalization of the _u_ -variables, _uC_ ( _y_ ).
9Tropical moduli spaces are central to recent calculations of previously unknown Betti numbers
in the cohomology of _Mg,n_, and in calculations of the cohomology of the Kontsevich graph complex,
relevant to certain problems in number theory. [7–9]


                  - 49                  

space, and at any _n_, define our canonical momentum polygons by picking a collection
of ordered points on _C_ ; the density of points increases as _n_ _→∞_, and one should
expect the final amplitude to just be a function of _C_ itself. Another option is to think
of the _Xij_ as evaluating some smooth function _X_ ( _u, v_ ) on the “kinematic spacetime”
on the discrete lattice associated with the _n_ point problem. We can begin with the
simplest situation where _X_ ( _u, v_ ) = _X_ 0 = _Xij_ is just a constant. In this case, working for
simplicity at tree-level, the sum over all diagrams is simply the total number of diagrams
weighted by 1 _/X_ 0 _[n][−]_ [3] . Since the total number of diagrams scales as 4 _[n]_, we have that at
large _n_ the amplitude scales as _Mn_ _∼_ (4 _/X_ 0) _[n]_ . Thus lim _n→∞_ (1 _/n_ )log _Mn_ _→_ log(4 _/X_ 0)
has a good large _n_ behavior, reminiscent of the large _N_ behavior in the ’t Hooft limit,
where the action is enhanced by an overall power of _N_ . It is then natural to understand
lim _n→∞_ (1 _/n_ )log _Mn_ ( _X_ ) for smooth perturbations _X_ ( _u, v_ ) = _X_ 0 + _δX_ ( _u, v_ ). In both
these scenarios for taking the large _n_ limit of kinematics, we expect that curve integral
representation will also have a “smooth” limit; with the integral of a piecewise linear
action on an ( _n −_ 3) dimensional space asymptoting to a sort one-dimensional path
integral with an action given by an integral over tropical functionals, and one can hope
that critical points of this unusual “tropical action” will determine the leading behavior
of the amplitude in this limit.


**15.2** **Large** _L_ **limits**


In this paper we have focused on understanding the large _n_ limit of amplitudes. This
was made possible by choosing a particularly simple reference triangulation. This
suggests a similar strategy for understanding large _L_ limits as well. For instance in the
planar limit, we can work with an especially simple fat graph for a tadpole at _L_ -loops,
consisting of a string of _L_ bubbles. The enumeration of all the relevant curves that
survive on the support on the Mirzakhani kernel, together with the computation of
the corresponding matrices, can be carried out recursively in a straightforward way. It
would be interesting to examine the behavior of the amplitudes at large _L_ in the ’t
Hooft limit.
In a similar vein, we can simply count all planar vacuum diagrams; this is tantamount to simply setting all the _X_ variables to one, with no loop integrations. Diagram
counting is the same thing as studying the tr _ϕ_ [3] _matrix_ _model_ . This subject is usually
studied using the techniques of random matrix theory, with the the famous and rich
connections to two dimensional quantum gravity and string theory revealed in doublescaling limits. [3, 12, 13] These methods are however tailored to matrix integrals and
do not straightforwardly generalize to field theory and non-trivial loop integrals. With
a judicious choice of representative fat graphs for general vacuum diagrams, the curve
integral formalism yields a different way of counting diagrams. This should not recover


                  - 50                  

the results from the matrix model literature, but suggests a path to generalize those
results to higher dimensions and to compute subleading terms in 1 _/L_ .


**15.3** **Renormalization**


One of the most important aspects of fundamental physics that has not yet been properly understood from the on-shell amplitude perspective is the exponentiation of UV
divergences and the Wilsonian renormalization group. The reason appears obvious:
the Wilsonian viewpoint is maximally off-shell, integrating out models of local quantum fields. Moreover, already when studying individual Feynman integrals, it can be
intricate to identify and remove those divergences which need to be canceled. In this
vein, tropical methods have recently proved useful. [14, 15]
The curve integral formalism offers a fresh perspective on this physics and is expected to manifest renormalization and renormalizability in a new way. Here again,
the UV divergences depend on _n_ and _L_ in a way which suggests treating _n_ and _L_
independently, involving separate physics. The logarithmic UV divergences at _n_ points
should be associated with specific _n_ -dependent factors, reflecting the fact they can be
reabsorbed into a redefinition of coupling constants. Whereas, the _L_ -dependence must
reflect the summation of leading and subleading UV log-divergences associated with
the RG. It is plausible that the exponentiation of UV divergences is naturally reflected
in the recursive structure of the fan itself.
A hint of how renormalization is encoded in the curve integral picture can be seen
for the 1-loop planar amplitudes discussed in Sections 4 and 7. In _D_ = 2 _d −_ _ϵ_ dimensions, these amplitudes have 1 _/ϵ_ UV divergences. The divergences are conventionally
removed by redefinition of the propagators or vertices in the Lagrangian, with the exact correction required depending on the dimension. But the divergences can also be
removed directly inside the curve integral, which has the form (after loop integration)




   _A_ =


  - _ti≤_ 0



_d_ _[n]_ _t F,_ (15.1)



for some _F_ ( _t_ ). Every cone in the integration region of this curve integral corresponds
to some fatgraph _σ_ . The integral over a cone will give a UV divergence if (and only if)
_σ_ contains a divergent subgraph, _γ_ . By Euler’s relation, if _γ_ has loop order _Lγ_ and _nγ_
external lines, then the superficial divergence of _γ_ is


_dγ_ = _nγ_ + 3( _Lγ_ _−_ 1) _−_ [1] (15.2)

2 _[LD,]_


                  - 51                  

and it gives a divergence if _dγ_ _<_ 0. We can remove these divergences from the curve
integral by defining tropical functions, _RD_ ( _y_ ), such that


_RD|σ_ = �0 if a subgraph of _σ_ has _dγ_ _<_ 0 (15.3)
1 else


Then define a _regularized_ _amplitude_ by




    _A_ [reg] 1-loop [=]


   - _ti≤_ 0



_d_ _[n]_ _t RD F._ (15.4)



The exact form of _RD_ depends on the dimension, _D_ .
For instance, in _D_ = 2+ _ϵ_ dimensions, the divergent subgraphs are 1-loop tadpoles,
which have _dγ_ = _−ϵ/_ 2 _<_ 0. In this case, one option for _RD_ turns out to be











_R_ 2 = max




 0 _,_ 1 _−_ _gii_ _[a]_ _[∂][t]_ _a_ _[α][C]_ _ii_ [(] _[t]_ [)]


_i_



_,_ (15.5)



where the sum is over all _tadpole_ _propagator_ curves, _Cii_, and **g** _ii_ is the _g_ -vector of _Cii_ .
Similar functions can be defined for higher dimensions.
It will be fascinating to find generalizations of this to all loops, such that UV divergences are governed by tropical functions on the Feynman fan, to better understand
renormalization and renormalizability from an on-shell perspective.

### **Acknowledgments**


NAH is supported by the DOE under grant DE-SC0009988; further support was made possible

by the Carl B. Feinberg cross-disciplinary program in innovation at the IAS. PGP is supported

by ANR grant CHARMS (ANR-19-CE40-0017) and by the Institut Universitaire de France

(IUF). HF is supported by Merton College, Oxford, and received additional support from

ERC grant GALOP (ID: 724638). GS is supported by the European Union’s Horizon 2020

research and innovation programs _Novel_ _structures_ _in_ _scattering_ _amplitudes_ (No. 725110) of

Johannes Henn. HT is supported by NSERC Discovery Grant RGPIN-2022-03960 and the

Canada Research Chairs program, grant number CRC-2021-00120.

### **A Curve Glossary**


For reference, and as a proof of principle, we record here all the curve paths needed to compute

every amplitude up to 2-loops. In practice, these lists are most easily obtained by computer.


                  - 52                  

**A.1** **1-loop** **Non-planar** **2-point**


The Mirzakhani kernel in Section 8 takes the form

_K_ = _[α]_ 12 [0] (A.1)
_ρ_ _[.]_


So the set of curves, _S_, contributing to the curve integral for the amplitude are those which
are compatible with _C_ 12 [0] [.] [There] [are] [five] [such] [curves] [on] [the] [tadpole] [graph.]
One way to enumerate these curves is to cut the tadpole graph along _C_ 12 [0] [,] [to] [produce]
a 5-point tree graph. The five curves we need are then the five curves on three 5-point tree

graph.
Of the 5 curves in _S_, 3 of them carry loop momentum and are given by


_C_ 12 _[−]_ [1] [= 1] _[Re]_ [2] _[L]_ [2] _[,]_ (A.2)

_C_ 12 [0] [= 1] _[Le]_ [1] _[R]_ [2] _[,]_ (A.3)

_C_ 12 [1] [= 1] _[Le]_ [1] _[Le]_ [2] _[Re]_ [1] _[R]_ [2] _[.]_ (A.4)


In addition to these, there are the two curves that follow the boundaries of the fatgraph, and
which contribute to _Z_ . These boundary curves have paths


_C_ 11 = 1 _Le_ 1 _Le_ 2 _L_ 1 _,_ (A.5)


_C_ 22 = 2 _Le_ 1 _Le_ 2 _L_ 2 _._ (A.6)


Note that it is straightforward to use these paths to obtain the curve matrices for these

five curves by matrix multiplication. One finds







_M_ 11 = _M_ 22 =


_M_ 12 _[−]_ [1] [=]


_M_ 12 [0] [=]


_M_ 12 [1] [=]




1 0
1 + _y_ 1 + _y_ 1 _y_ 2 _y_ 1 _y_ 2




1 1 + _y_ 1
1 + _y_ 1 1 + 2 _y_ 1 + _y_ 1 [2] [+] _[ y]_ 1 [2] _[y]_ [2]




- 1 + _y_ 2 _y_ 2
_y_ 2 _y_ 2




1 1
1 1 + _y_ 1











(A.7)


(A.8)


(A.9)


(A.10)



For the rest of this Appendix, we record only the paths of the curves.


                  - 53                  

**A.2** **2-loop** **Planar** **Tadpole**


The following is the finite set _S_ of 16 non-boundary curves compatible with the Mirzakhani
kernel _K_ in Section 11:


0 _LwR_ ( _xL_ ) _[∞]_

0 _RzR_ ( _yL_ ) _[∞]_


0 _LwLxLwR_ 0


0 _RzLyLzL_ 0


0 _RzRyRzL_ 0

( _Rx_ ) _[∞]_ _LwLzR_ ( _yL_ ) _[∞]_

( _Ry_ ) _[∞]_ _LzRwR_ ( _xL_ ) _[∞]_

0 _LwLxLwLzR_ ( _yL_ ) _[∞]_

0 _RzRyRzRwR_ ( _xL_ ) _[∞]_

( _Ry_ ) _[∞]_ _LzRwRxRwR_ 0

( _Rx_ ) _[∞]_ _LwLzLyLzRwR_ ( _xL_ ) _[∞]_

( _Ry_ ) _[∞]_ _LzRwLxLwLzR_ ( _yL_ ) _[∞]_

0 _LwLxLwLzLyLzRwR_ ( _xL_ ) _[∞]_

0 _RzRyRzRwRxRwLzR_ ( _yL_ ) _[∞]_


0 _LwLxLwLzLyLzRwRxRwR_ 0


0 _RzRyRzRwLxLwLzLyLzL_ 0


The momentum of a curve _CAB_ ( _A, B_ = 0 _, a, b_ ) connecting trace-factors _A_ and _B_ is given in
dual variables by _x_ _[µ]_ _B_ _[−]_ _[x]_ _A_ _[µ]_ [.] _[x][µ]_ _a_ [and] _[x][µ]_ _b_ [are] [the] [loop] [momentum] [variables.] [So] [it] [follows] [that,]
of these 16 curves, 9 of them carry loop momentum and so contribute to _K_, _U_ and _F_ 0. The
remaining 7 contribute only to _Z_ .
In addition, the tadpole graph has one boundary curve, _C_ 00, which contributes to _Z_, and
has the path


_C_ 00 = 0 _RzRyRzRwRxRwR_ 0


                  - 54                  

**A.3** **2-loop** **Double** **Trace**


The following is the finite set _S_ of 21 non-boundary curves compatible with the Mirzakhani
kernel _K_ in Section 14:


_C_ 12 [01] [=] _[ Ly]_ [2] _[Rx]_ [1] _[L]_

_C_ 12 [10] [=] _[ Ly]_ [1] _[Rx]_ [2] _[L]_

_C_ 12 [00] [=] _[ Rx]_ [2] _[RzLx]_ [1] _[L]_

_C_ 12 [11] [=] _[ Ly]_ [1] _[LzRy]_ [2] _[R]_

_C_ 11 [0] [=] _[ Ly]_ [1] _[Rx]_ [2] _[Ry]_ [2] _[Rx]_ [1] _[L]_

_C_ 22 [0] [=] _[ Ly]_ [2] _[Rx]_ [1] _[Ry]_ [1] _[Rx]_ [2] _[L]_

_C_ 10 [0] [=] _[ R]_ [(] _[x]_ [1] _[Ly]_ [2] _[Lx]_ [2] _[Ly]_ [1] _[L]_ [)] _[∞]_

_C_ 20 [0] [=] _[ R]_ [(] _[x]_ [2] _[Ly]_ [1] _[Lx]_ [1] _[Ly]_ [2] _[L]_ [)] _[∞]_

_C_ 11 _[−]_ [1] _[/]_ [2] = _Ly_ 1 _Rx_ 2 _Ry_ 2 _LzRy_ 1 _R_

_C_ 11 [1] _[/]_ [2] [=] _[ Rx]_ [1] _[Ly]_ [2] _[Lx]_ [2] _[RzLx]_ [1] _[L]_

_C_ 22 _[−]_ [1] _[/]_ [2] = _Ly_ 2 _Rx_ 1 _Ry_ 1 _LzRy_ 2 _R_

_C_ 22 [1] _[/]_ [2] [=] _[ Rx]_ [2] _[Ly]_ [1] _[Lx]_ [1] _[RzLx]_ [2] _[L]_

_C_ 12 [1] _[−]_ [1] = _Ly_ 1 _Rx_ 2 _Ry_ 2 _LzLx_ 2 _L_

_C_ 12 _[−]_ [11] = _Ly_ 2 _Rx_ 1 _Ry_ 1 _LzLx_ 1 _L_

_C_ 12 _[−]_ [10] = _Rx_ 1 _RzRy_ 1 _Lx_ 1 _RzLx_ 2 _L_

_C_ 12 [0] _[−]_ [1] = _Rx_ 2 _RzRy_ 2 _Lx_ 2 _RzLx_ 1 _L_

_C_ 10 _[−]_ [1] [=] _[ Ly]_ [1] _[LzR]_ [(] _[y]_ [2] _[Lx]_ [2] _[Ly]_ [1] _[Lx]_ [1] _[L]_ [)] _[∞]_

_C_ 10 [1] [=] _[ Rx]_ [1] _[RzR]_ [(] _[y]_ [1] _[Lx]_ [1] _[Ly]_ [2] _[Lx]_ [2] _[L]_ [)] _[∞]_

_C_ 20 _[−]_ [1] [=] _[ Ly]_ [2] _[LzR]_ [(] _[y]_ [1] _[Lx]_ [1] _[Ly]_ [2] _[Lx]_ [2] _[L]_ [)] _[∞]_

_C_ 20 [1] [=] _[ Rx]_ [2] _[RzR]_ [(] _[y]_ [2] _[Lx]_ [2] _[Ly]_ [1] _[Lx]_ [1] _[L]_ [)] _[∞]_

_C_ 00 = ( _Rx_ 2 _Ry_ 2 _Rx_ 1 _Ry_ 1) _[∞]_ _LzR_ ( _y_ 2 _Lx_ 2 _Ly_ 1 _Lx_ 1 _L_ ) _[∞]_


The only curves that carry loop momentum are those curves _CAB_ connecting distinct tracefactors, _A_ and _B_ .

It follows that, of these 21 curves, 14 of them carry loop momentum and so contribute
to _K_, _U_ and _F_ 0. The remaining 7 contribute only to _Z_ .
In addition, the tadpole graph has two boundary curves, which contribute to _Z_, and have

paths


_C_ 11 = 1 _Rx_ 1 _RzRy_ 1 _R_ 1


_C_ 22 = 2 _Rx_ 2 _RzRy_ 2 _R_ 2


                  - 55                  

**A.4** **2-loop** **Triple** **Trace**


The following is the finite set _S_ of 30 non-boundary curves compatible with the Mirzakhani
kernel _K_ in Section 12:


0 _LzLx_ 2 _R_ 1


1 _Rx_ 1 _LzR_ 0


2 _Ly_ 1 _RwL_ 0


2 _Ry_ 2 _LwL_ 0


0 _LzLx_ 2 _Lx_ 1 _Rx_ 2 _R_ 1


1 _Rx_ 1 _LzLwLy_ 1 _R_ 2


2 _Ly_ 1 _RwRzLx_ 2 _R_ 1


2 _Ry_ 2 _LwRzLx_ 2 _R_ 1


2 _Ry_ 2 _LwRzRx_ 1 _L_ 1


2 _Ry_ 2 _Ry_ 1 _Ly_ 2 _LwL_ 0


0 _LzLx_ 2 _Lx_ 1 _LzLwLy_ 1 _R_ 2


0 _LzLx_ 2 _Lx_ 1 _LzLwRy_ 2 _L_ 2


1 _Lx_ 2 _RzLwLy_ 1 _Ly_ 2 _LwL_ 0


1 _Lx_ 2 _RzLwLy_ 1 _Ly_ 2 _Ry_ 1 _R_ 2


1 _Rx_ 1 _LzLwLy_ 1 _Ly_ 2 _LwL_ 0


1 _Rx_ 1 _LzLwLy_ 1 _Ly_ 2 _Ry_ 1 _R_ 2


1 _Rx_ 1 _Rx_ 2 _Lx_ 1 _LzLwLy_ 1 _R_ 2


1 _Rx_ 1 _Rx_ 2 _Lx_ 1 _LzLwRy_ 2 _L_ 2


0 _LzLx_ 2 _Lx_ 1 _LzLwLy_ 1 _Ly_ 2 _Ry_ 1 _R_ 2


1 _Lx_ 2 _RzLwLy_ 1 _Ly_ 2 _LwRzLx_ 2 _R_ 1


1 _Rx_ 1 _LzLwLy_ 1 _Ly_ 2 _LwRzLx_ 2 _R_ 1


1 _Rx_ 1 _LzLwLy_ 1 _Ly_ 2 _LwRzRx_ 1 _L_ 1


1 _Rx_ 1 _Rx_ 2 _Lx_ 1 _LzLwLy_ 1 _Ly_ 2 _LwL_ 0


2 _Ly_ 1 _RwRzLx_ 2 _Lx_ 1 _LzLwLy_ 1 _R_ 2


2 _Ry_ 2 _LwRzLx_ 2 _Lx_ 1 _LzLwLy_ 1 _R_ 2


2 _Ry_ 2 _LwRzLx_ 2 _Lx_ 1 _LzLwRy_ 2 _L_ 2


0 _LzLx_ 2 _Lx_ 1 _LzLwLy_ 1 _Ly_ 2 _LwRzLx_ 2 _R_ 1


0 _LzLx_ 2 _Lx_ 1 _LzLwLy_ 1 _Ly_ 2 _LwRzRx_ 1 _L_ 1


2 _Ly_ 1 _RwRzLx_ 2 _Lx_ 1 _LzLwLy_ 1 _Ly_ 2 _LwL_ 0


2 _Ry_ 2 _LwRzLx_ 2 _Lx_ 1 _LzLwLy_ 1 _Ly_ 2 _LwL_ 0


                  - 56                  

The only curves that carry loop momentum are those curves _CAB_ connecting distinct tracefactors, _A_ and _B_ .

It follows that, of these 30 curves, 24 of them carry loop momentum and so contribute
to _K_, _U_ and _F_ 0. The remaining 6 contribute only to _Z_ .
In addition, the tadpole graph has three boundary curves, which contribute to _Z_, and

have paths


_C_ 11 = 1 _Rx_ 1 _Rx_ 2 _R_ 1


_C_ 22 = 2 _Ry_ 2 _Ry_ 1 _R_ 2


_C_ 00 = 0 _RwRy_ 2 _Ry_ 1 _RwRzRx_ 1 _Rx_ 2 _RzR_ 0


**A.5** **2-loop** **Genus** **One** **Tadpole**


The following is the finite set _S_ of 9 non-boundary curves compatible with the Mirzakhani
kernel _K_ in Section 13:


_C_ 1 = _C_ [0] _[/]_ [1;0] = 0 _Ly_ 2 _Ry_ 4 _Ly_ 1 _L_ 0

_C_ 2 = _C_ [1] _[/]_ [0;0] = 0 _Ly_ 2 _Ly_ 3 _Ry_ 1 _L_ 0

_C_ 3 = _C_ [1] _[/]_ [0;1] = 0 _Ry_ 1 _Ry_ 4 _Ry_ 3 _Ry_ 1 _Ry_ 2 _Ry_ 4 _Ly_ 1 _L_ 0

_C_ 4 = _C_ [1] _[/]_ [1;0] = 0 _Ry_ 1 _Ry_ 4 _Ry_ 3 _Ry_ 1 _L_ 0

_C_ 5 = _C_ [1] _[/]_ [1;1] = 0 _Ly_ 2 _Ly_ 3 _Ly_ 4 _Ly_ 2 _R_ 0

_C_ 6 = _C_ _[−]_ [1] _[/]_ [1;0] = 0 _Ly_ 2 _Ly_ 3 _Ry_ 1 _Ry_ 2 _Ry_ 4 _Ly_ 1 _L_ 0

_C_ 7 = _C_ [0] _[/]_ [1;1] = 0 _Ly_ 2 _Ly_ 3 _Ry_ 1 _Ry_ 2 _Ry_ 4 _Ry_ 3 _Ry_ 2 _R_ 0

_C_ 8 = _C_ [0] _[/]_ [1;2] = 0 _Ry_ 1 _Ry_ 4 _Ry_ 3 _Ry_ 1 _Ry_ 2 _Ry_ 4 _Ry_ 3 _Ly_ 4 _Ly_ 1 _L_ 0

_C_ 9 = _C_ _[−]_ [1] _[/]_ [1;1] = 0 _Ry_ 1 _Ry_ 4 _Ry_ 3 _Ry_ 1 _Ry_ 2 _Ry_ 4 _Ly_ 1 _Ry_ 2 _Ry_ 4 _Ly_ 1 _L_ 0


All 9 of these curves carry loop momentum and so contribute to _K_, _U_ and _F_ 0.
In addition, the tadpole graph has one boundary curve, which contributes to _Z_, and has

path


_C_ 00 = 0 _Ry_ 1 _Ry_ 4 _Ry_ 3 _Ry_ 1 _Ry_ 2 _Ry_ 4 _Ry_ 3 _Ry_ 2 _R_ 0 _._

### **References**


[1] N. Arkani-Hamed, H. Frost, G. Salvatori, P-G. Plamondon, and H. Thomas. All loop

scattering as a counting problem, 2023.


[2] M. Mirzakhani. Simple geodesics and Weil-Petersson volumes of moduli spaces of

bordered Riemann surfaces. _Invent._ _math._, 167:179–222, 2007.


                  - 57                  

[3] Phil Saad, Stephen H. Shenker, and Douglas Stanford. JT gravity as a matrix integral.

3 2019.


[4] Michael Borinsky. Tropical Monte Carlo quadrature for Feynman integrals. _Annales_ _de_

_l’Institut_ _Henri_ _Poincar´e_ _D_, jan 2023.


[5] Michael Borinsky, Henrik J. Munch, and Felix Tellander. Tropical Feynman integration

in the Minkowski regime. _Computer_ _Physics_ _Communications_, 292:108874, nov 2023.


[6] V. V. Fock and A. B. Goncharov. Moduli spaces of local systems and higher

Teichm¨uller theory. _arXiv_ _Mathematics_ _e-prints_, page math/0311149, November 2003.


[7] Francis Brown. Invariant Differential Forms on Complexes of Graphs and Feynman

Integrals. _SIGMA_, 17:103, 2021.


[8] Michael Borinsky and Karen Vogtmann. The euler characteristic of out (f n).

_Commentarii_ _Mathematici_ _Helvetici_, 95(4), 2020.


[9] Jørgen Ellegaard Andersen, Ga¨etan Borot, S´everin Charbonnier, Alessandro

Giacchetto, Danilo Lewa´nski, and Campbell Wheeler. On the kontsevich geometry of

the combinatorial teichm¨uller space, 2021.


[10] M. B. Voloshin. Multiparticle amplitudes at zero energy and momentum in scalar

theory. _Nucl._ _Phys._ _B_, 383:233–248, 1992.


[11] Michael R. Douglas and Stephen H. Shenker. Strings in Less Than One-Dimension.

_Nucl._ _Phys._ _B_, 335:635, 1990.


[12] David J. Gross and Alexander A. Migdal. Nonperturbative Solution of the Ising Model

on a Random Surface. _Phys._ _Rev._ _Lett._, 64:717, 1990.


[13] David J. Gross and Alexander A. Migdal. Nonperturbative Two-Dimensional Quantum

Gravity. _Phys._ _Rev._ _Lett._, 64:127, 1990.


[14] Nima Arkani-Hamed, Aaron Hillman, and Sebastian Mizera. Feynman polytopes and

the tropical geometry of uv and ir divergences. _Phys._ _Rev._ _D_, 105:125013, Jun 2022.


[15] Aaron Hillman. A subtraction scheme for feynman integrals, 2023.


                  - 58                  

