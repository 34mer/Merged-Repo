Prepared for submission to JHEP

## **Scattering Forms and the Positive Geometry of** **Kinematics, Color and the Worldsheet**


**Nima** **Arkani-Hamed,** _[a]_ **Yuntao** **Bai,** _[b]_ **Song** **He,** _[c,d]_ **Gongwang** **Yan** _[e,c]_


_aSchool_ _of_ _Natural_ _Sciences,_ _Institute_ _for_ _Advanced_ _Study,_ _Princeton,_ _NJ,_ _08540,_ _USA_

_bDepartment_ _of_ _Physics,_ _Princeton_ _University,_ _Princeton,_ _NJ,_ _08544,_ _USA_

_cCAS_ _Key_ _Laboratory_ _of_ _Theoretical_ _Physics,_ _Institute_ _of_ _Theoretical_ _Physics,_ _Chinese_ _Academy_
_of_ _Sciences,_ _Beijing,_ _100190,_ _China_

_dUniversity_ _of_ _Chinese_ _Academy_ _of_ _Sciences,_ _No.19A_ _Yuquan_ _Road,_ _Beijing_ _100049,_ _China_

_eInstitute_ _for_ _Advanced_ _Study,_ _Tsinghua_ _University,_ _Beijing,_ _100084,_ _China_

_E-mail:_ `[arkani@ias.edu](mailto:arkani@ias.edu)`, `[ytbai@princeton.edu](mailto:ytbai@princeton.edu)`, `[songhe@itp.ac.cn](mailto:songhe@itp.ac.cn)`,

```
 ygw17@mails.tsinghua.edu.cn

```

Abstract: The search for a theory of the S-Matrix over the past five decades has revealed surprising geometric structures underlying scattering amplitudes ranging from the
string worldsheet to the amplituhedron, but these are all geometries in auxiliary spaces as
opposed to the kinematical space where amplitudes actually live. Motivated by recent advances providing a reformulation of the amplituhedron and planar _N_ = 4 SYM amplitudes
directly in kinematic space, we propose a novel geometric understanding of amplitudes in
more general theories. The key idea is to think of amplitudes not as functions, but rather
as differential forms on kinematic space. We explore the resulting picture for a wide range
of massless theories in general spacetime dimensions. For the bi-adjoint _φ_ [3] scalar theory,
we establish a direct connection between its “scattering form” and a classic polytope—the
associahedron—known to mathematicians since the 1960’s. We find an associahedron living
naturally in kinematic space, and the tree level amplitude is simply the “canonical form”
associated with this “positive geometry”. Fundamental physical properties such as locality and unitarity, as well as novel “soft” limits, are fully determined by the combinatorial
geometry of this polytope. Furthermore, the moduli space for the open string worldsheet
has also long been recognized as an associahedron. We show that the scattering equations
act as a diffeomorphism between the interior of this old “worldsheet associahedron” and the
new “kinematic associahedron”, providing a geometric interpretation and simple conceptual
derivation of the bi-adjoint CHY formula. We also find “scattering forms” on kinematic
space for Yang-Mills theory and the Non-linear Sigma Model, which are dual to the fully
color-dressed amplitudes despite having no explicit color factors. This is possible due to a
remarkable fact—“Color is Kinematics”— whereby kinematic wedge products in the scattering forms satisfy the same Jacobi relations as color factors. Finally, all our scattering
forms are well-defined on the projectivized kinematic space, a property which can be seen
to provide a geometric origin for color-kinematics duality.


**Contents**


**1** **Introduction** **1**


**2** **The** **Planar** **Scattering** **Form** **on** **Kinematic** **Space** **7**
2.1 Kinematic Space 7
2.2 Planar Kinematic Variables 8
2.3 The Planar Scattering Form 9


**3** **The** **Kinematic** **Associahedron** **11**
3.1 The Associahedron from Planar Cubic Diagrams 11
3.2 The Kinematic Associahedron 13
3.3 Bi-adjoint _φ_ [3] Amplitudes 15
3.4 All Ordering Pairs of Bi-adjoint _φ_ [3] Amplitudes 18
3.5 The Associahedron is the Amplituhedron for Bi-adjoint _φ_ [3] Theory 23


**4** **Factorization** **and** **“Soft”** **Limit** **24**
4.1 Factorization 24
4.2 “Soft” Limit 26


**5** **Triangulations** **and** **Recursion** **Relations** **27**
5.1 The Dual Associahedron and Its Volume as the Bi-adjoint Amplitude 28
5.2 Feynman Diagrams as a Triangulation of the Dual Associahedron Volume 29
5.3 More Triangulations of the Dual Associahedron 31
5.4 Direct Triangulations of the Kinematic Associahedron 31
5.5 Recursion Relations for Bi-adjoint _φ_ [3] Amplitudes 33


**6** **The** **Worldsheet** **Associahedron** **35**
6.1 Associahedron from the Open String Moduli Space 36
6.2 Scattering Equations as a Diffeomorphism Between Associahedra 40


**7** **“Big** **Kinematic”** **Space** **and** **Scattering** **Forms** **44**
7.1 The Big Kinematic Space 45
7.2 Scattering Forms and Projectivity 47


**8** **Color** **is** **Kinematics** **50**
8.1 Duality Between Color and Form 51
8.2 Trace Decomposition as Pullback of Scattering Forms 53


**9** **Scattering** **Forms** **for** **Gluons** **and** **Pions** **56**
9.1 Gauge Invariance, Adler Zero, and Uniqueness of YM and NLSM Forms 56
9.2 YM and NLSM from the Worldsheet 57
9.3 Extended Positive Geometry for Gluons and Pions? 59


                   - i                    

**10** **Summary** **and** **Outlook** **59**


**A** **A** **Quick** **Review** **of** **Positive** **Geometries** **and** **Canonical** **Forms** **65**
A.1 Definitions 65
A.2 Triangulations 66
A.3 Pushforwards 66
A.4 Projective Polytopes and Dual Polytopes 67
A.5 Simple Polytopes 70
A.6 Recursion Relations 70


**B** **Vertex** **Coordinates** **of** **the** **Kinematic** **Associahedron** **72**


**C** **BCJ** **Relations** **and** **Dual-basis** **Expansion** **from** **Projectivity** **72**


**1** **Introduction**


Scattering amplitudes are arguably the most basic observables in fundamental physics.
Apart from their prominent role in the experimental exploration of the high energy frontier,
scattering amplitudes also have a privileged theoretical status as the only known observable
of quantum gravity in asymptotically flat space-time. As such it is natural to ask the
“holographic” questions we have become accustomed to asking (and beautifully answering)
in AdS spaces for two decades: given that the observables are anchored to the boundaries
at infinity, is there also a “theory at infinity” that directly computes the S-Matrix without
invoking a local picture of evolution in the interior of the spacetime?
Of course this question is famously harder in flat space than it is in AdS space. The
(exceedingly well-known) reason for this is the fundamental difference in the nature of the
boundaries of the two spaces. The boundary of AdS is an ordinary flat space with completely
standard notions of “time” and “locality”, thus we have perfectly natural candidates for what
a “theory on the boundary” could be—just a local quantum field theory. We do not have
these luxuries in asymptotically flat space. We can certainly think of the “asymptotics”
concretely in any of a myriad of ways by specifying the asymptotic on-shell particle momenta
in the scattering process. But whether this is done with Mandelstam invariants, or spinorhelicity variables, or twistors, or using the celestial sphere at infinity, in no case is there
an obvious notion of “locality” and/or “time” in these spaces, and we are left with the
fundamental mystery of what principles a putative “theory of the S-Matrix” should be
based on.
Indeed, the absence of a good answer to this question was the fundamental flaw that
doomed the 1960’s S-Matrix program. Many S-Matrix theorists hoped to find some sort
of first-principle “derivation” of fundamental analyticity properties encoding unitarity and
causality in the S-Matrix, and in this way to find the principles for a theory of the S-Matrix.


                   - 1                   

But to this day we do not know precisely what these “analyticity properties encoding causality” should be, even in perturbation theory, and so it is not surprising that this “systematic”
approach to the subject hit a dead end not long after it began.
Keenly wary of this history, and despite the same focus on the S-Matrix as a fundamental observable, much of the modern explosion in our understanding of scattering
amplitudes has adopted a fundamentally different and more intellectually adventurous philosophy towards the subject. Instead of hoping to slavishly _derive_ the needed properties of
the S-Matrix _from_ the principles of unitarity and causality, there is now a different strategy: to look for fundamentally new principles and new laws, very likely associated with
new mathematical structures, that produce the S-Matrix as the answer to entirely different
kinds of natural questions, and to only later discover space-time and quantum mechanics, embodied in unitarity and (Lorentz-invariant) causality, as derived consequences rather
than foundational principles.
The past fifty years have seen the emergence of a few fascinating geometric structures
underlying scattering amplitudes in unexpected ways, encouraging this point of view. The
first and still in many ways most remarkable example is perturbative string theory [1, 2],
which computes scattering amplitudes by an auxiliary computation of correlation functions
in the worldsheet CFT. At the most fundamental level there is a basic geometric object—the
moduli space of marked points on Riemann surfaces [3]—which has a “factorizing” boundary
structure. This is the primitive origin of the _factorization_ of scattering amplitudes, which
is needed for unitarity and locality in perturbation theory. More recently, we have seen a
new interpretation of the same worldsheet structure first in the context of “twistor string
theory” [4], and much more generally in the program of “scattering equations” [5, 6], which
directly computes the amplitudes for massless particles using a worldsheet but with no
stringy excitations [7, 8].
Over the past five years, we have also seen an apparently quite different set of mathematical ideas [9–11] underlying scattering amplitudes in planar maximally supersymmetric
gauge theory—the amplituhedron [12]. This structure is more alien and unfamiliar than the
worldsheet, but its core mathematical ideas are even simpler, of a fundamentally combinatorial nature involving nothing more than grade-school algebra in its construction. Moreover,
the amplituhedron as a _positive geometry_ [13] again produces a “factorizing” boundary structure that gives rise to locality and unitarity in a geometric way and makes manifest the
hidden infinite-dimensional Yangian symmetry of the theory.
While the existence of these magical structures is strong encouragement for the existence of a master theory for the S-Matrix, all these ideas have a disquieting feature in
common. In all cases, the new geometric structures are _not_ _seen_ _directly_ _in_ _the_ _space_ _where_
_the scattering amplitudes naturally live, but in some auxiliary spaces_ . These auxiliary spaces
are where all the action is, be it the worldsheet or the generalized Grassmannian spaces of
the amplituhedron. We are therefore _still_ left to wonder: what sort of questions do we have
to ask, directly in the space of “scattering kinematics”, to generate local, unitary dynamics?
Clearly we should not be writing down Lagrangians and computing path integrals, but what
should we do instead? What mathematical structures breathe scattering-physics-life into
the “on-shell kinematic space”? And is there any avatar of the geometric structures of the


                   - 2                   

**Figure** **1** : The one-dimensional associahedron (red line segment) as the intersection of the
positive region and the subspace _s_ + _t_ = _c_ where _c >_ 0 is a constant.


worldsheet, or amplituhedra, in this kinematic space?
Recent advances in giving a more intrinsic definition of the amplituhedron [14] suggest
the beginning of an answer to this question. A key observation is that, instead of thinking
about scattering amplitudes merely as _functions_ on kinematic space, they are to be thought
of more fundamentally as _differential_ _forms_ on kinematic space. In the context of the amplituhedron and planar _N_ = 4 SYM, kinematic space is simply the space of momentum
twistors _Zi_ for the particles _i_ = 1 _, . . ., n_ [10]. And on this space the differential form has a
natural purpose in life—it literally “bosonizes” the super-amplitude by treating the on-shell
Grassmann variables _ηi_ for the _i_ [th] particle as the momentum twistor differential _ηi_ _→_ _dZi_ .
This seemingly innocuous move has dramatic geometric consequences: given a differential
form, we can compute residues around singularities, and by now this is well known to reveal
the underlying _positive_ _geometry_ . Indeed, [14] provides a novel description of the amplituhedron _purely_ _in_ _the_ _standard_ _momentum_ _twistor_ _kinematic_ _space_, whereby the geometry
arises as the intersection of a top-dimensional “positive region” in the kinematic space with
a certain family of lower-dimensional subspaces with further “positivity” properties. The
scattering form is defined everywhere in kinematic space, and is completely specified by
its behavior when “pulled back” to the subspace on which the amplituhedron is revealed,
whereby it becomes the _canonical form_ [13] with logarithmic singularities on the boundaries
of this positive geometry.
In this paper, we will see a virtually identical structure emerge remarkably in a setting
very far removed from special theories with maximal supersymmetry in the planar limit.
We will consider a wide variety of theories of massless particles in a general number of
dimensions, beginning with one of the simplest possible scalar field theories—a theory
of _bi-adjoint_ _scalars_ with cubic interactions [15]. The words connecting amplitudes to
positive geometry are identical, but the cast of characters—the kinematic space, the precise
definitions of the top-dimensional “positive region” and the “family of subspaces”—differ
in important ways. Happily all the objects involved are simpler and more familiar—the
kinematic space is simply the space of Mandelstam invariants, the positive region is imposed
by inequalities that demand positivity of physical poles, and the subspaces are cut out by
linear equations in kinematic space—so that the resulting positive geometries are ordinary


                   - 3                   

_s_ 1234



_s_ 15







_s_ 12







_s_ 45


**Figure** **2** : Pictures for _n_ =5 (left) and _n_ =6 (right) associahedra, where we have labeled
every facet by the corresponding vanishing planar variable.



polytopes (as opposed to the generalization of polytopes into the Grassmannian seen in
the amplituhedron). When the dust settles, what emerges is the famous and beautiful
_associahedron_ polytope [16, 17]. In fact, the “kinematic associahedron” we have discovered
is in a precise sense the “amplituhedron” for the bi-adjoint _φ_ [3] theory.
By way of a broad-brush invitation to the rest of the paper, let us illustrate the key
ideas in some simple examples. Consider an amplitude for massless scalar particles whose
Feynman diagram expansion is simply given by the sum over planar cubic tree graphs.
For _n_ =4 particles, the amplitude would simply be [1] [+] [1] [.] [However,] [we] [consider] [instead] [a]



one-form Ω [(1)] _n_ =4 [given] [by]



Ω [(1)] _n_ =4 [=] _[ds]_



_s_ _[−]_ _[dt]_ _t_




[1] [1]

_s_ [+] _t_




[However,] [we] [consider] [instead] [a]
_t_ [.]



(1.1)
_t_



The structure of the form is of course very natural; we are simply replacing “1/propagator”
with _d_ log of the propagator. The relative minus sign is more intriguing and is demanded
by an interesting requirement—the differential form must be well-defined, not only on the
two-dimensional ( _s, t_ ) space, but also on the projectivized version of the space; in other
words, the form must be invariant under _local_ GL(1) transformations ( _s, t_ ) _→_ Λ( _s, t_ )( _s, t_ );
or said another way, it must only depend on the ratio ( _s/t_ ). Indeed, the minus sign allows
us to rewrite the form as _d_ log( _s/t_ ) which is manifestly projective. At _n_ points, we have an
( _n−_ 3)-form obtained by wedging together the _d_ log of propagators for every planar cubic
graph, and summing over all graphs with relative signs fixed by projectivity.
Returning to four points, we have a one-form defined on the two-dimensional ( _s, t_ )
space. But how can we extract the “actual amplitude” 1 [1] [this] [form,] [and] [how]
_s_ [+] _t_ [from]

is it related to any sort of positive geometry? Both questions are answered at once by
identifying some natural regions in kinematic space. First, if the poles of the amplitude are
to correspond to boundaries of a geometry, it is clear that we should impose a positivity
constraint on all the planar poles, which at four points are simply the conditions that
_s, t_ _≥_ 0. This brings us to the upper quadrant of the ( _s, t_ ) plane. But this alone can


                   - 4                   

1
2


scattering equations
6 _−−−−−−−−−−−→_

3 as a diffeomorphism


5 4


**Figure** **3** : The scattering equations provide a diffeomorphism from the worldsheet associahedron to the kinematic associahedron.


not correspond to the positive geometry we are seeking—for one thing, the space is twodimensional while our scattering form is a one-form! This suggests that in addition to
imposing these positivity constraints, we should _also_ identify a one-dimensional subspace
on which to pull back our form. Again it is trivial to identify a natural subspace in our
four-particle example: we simply impose that _s_ + _t_ = _c_, where _c >_ 0 is a positive constant.
Note that the intersection of this line with the positive region _s, t_ _>_ 0 is a line segment
with two boundaries at _s_ = 0 and _t_ = 0, which is a one-dimensional positive geometry
(See Figure 1). Furthermore, quite beautifully, pulling back our scattering one-form to this
one-dimensional subspace accomplishes two things: (1) this pulled-back form is also the
canonical form of the positive geometry of the interval; (2) given that _−u_ = _s_ + _t_ = _c_,
we have _ds_ + _dt_ = 0 on the line, and so the pullback of the form can be written as _e.g._
_ds/s −_ _dt/t_ = _ds_ (1 _/s_ + 1 _/t_ ), whereby factoring out the top form _ds_ on the line segment
leaves us with the amplitude!
This geometry generalizes to all _n_ in a simple way. The full kinematic space of Mandelstam invariants is _n_ ( _n −_ 3) _/_ 2-dimensional. A nice basis for this space is provided by all
planar propagators _sa,a_ +1 _,...,b−_ 1, and there is a natural “positive region” in which all these
variables are forced to be positive. There is also a natural ( _n−_ 3)-dimensional subspace that
is cut out by the equations _−sij_ = _cij_ for all non-adjacent _i, j_ excluding the index _n_, where
the _cij_ _>_ 0 are positive constants. These equalities pick out an ( _n −_ 3)-dimensional hyperplane in kinematic space whose intersection with the positive region is the associahedron
polytope. A picture of _n_ =5 _,_ 6 associahedra can be seen in Figure 2. As we saw for four
points, when the scattering form is pulled back to this subspace, it is revealed to be the
canonical form with logarithmic singularities on all the boundaries of this associahedron!
The computation of scattering amplitudes then reduces to triangulating the associahedron. Quite nicely one natural choice of triangulation directly reproduces the Feynman
diagram expansion, but other triangulations are of course also possible. As a concrete example, for _n_ =5 the Feynman diagrams express the amplitude as the sum over 5 cyclically
rotated terms:
1 1 1 1 1
+ + + + (1.2)
_s_ 12 _s_ 123 _s_ 23 _s_ 234 _s_ 34 _s_ 345 _s_ 45 _s_ 451 _s_ 51 _s_ 512

But there is another triangulation of the _n_ =5 associahedron that yields a surprising 3-term


                   - 5                   

1



2 3 4


_f_ _[a]_ [1] _[a]_ [2] _[b]_ _f_ _[ba]_ [3] _[c]_ _f_ _[ca]_ [4] _[a]_ [5]
5


_f_ _[a]_ [1] _[a]_ [2] _[b]_ _f_ _[ba]_ [3] _[c]_ _f_ _[ca]_ [4] _[a]_ [5] _↔_



1



2 3 4


_s_ 12 _s_ 45
5


d _s_ 12 _∧_ d _s_ 45



**Figure** **4** : An example of the duality between color factors and differential forms



expression:
_s_ 12 + _s_ 234 + _[s]_ [12][ +] _[ s]_ [234]
_s_ 12 _s_ 34 _s_ 234 _s_ 12 _s_ 234 _s_ 23



(1.3)
_s_ 12 _s_ 23 _s_ 123




_[s]_ [12][ +] _[ s]_ [234] + _[s]_ [12] _[ −]_ _[s]_ [123][ +] _[ s]_ [23]

_s_ 12 _s_ 234 _s_ 23 _s_ 12 _s_ 23 _s_ 123



which can not be obtained by any recombination of the Feynman diagram terms. Indeed,
we will see that the form enjoys a symmetry that is destroyed by individual terms in the
Feynman diagram triangulation and restored only in the full sum. In contrast, this new
representation comes from a simple triangulation that keeps this symmetry manifest, much
as “BCFW triangulations” of the amplituhedron [10, 11] make manifest the dual conformal/Yangian symmetries of planar _N_ = 4 SYM that are not seen in the usual Feynman
diagram expansion.
Beyond these parallels to the story of the amplituhedron, the picture of scattering forms
on kinematic space appears to have a fundamental role to play in the physics of scattering
amplitudes in more general settings. For instance, string theorists have long known of an
important associahedron, associated with the open string worldsheet; this raises a natural
question: Is there a natural diffeomorphism from the (old) worldsheet associahedron to the
(new) kinematic space associahedron? The answer is yes, and the map is precisely provided
by the scattering equations! This correspondence gives a one-line conceptual proof of the
CHY formulas for bi-adjoint amplitudes [15] as a “pushforward” from the worldsheet “ParkeTaylor form” to the kinematic space scattering form.
The scattering forms also give a strikingly simple and direct connection between kinematics and color! This is seen at two levels. First, we can define very general scattering
forms as a sum over all possible cubic graphs _g_ in a “big kinematic space”, with each graph
given by the wedge of the _d_ log of all its propagator factors weighted with “kinematic coefficients” _N_ ( _g_ ). The first important observation is that the projectivity of the form on
this big kinematic space forces the kinematic coefficients _N_ ( _g_ ) to satisfy the same Jacobi
relations as color factors; in other words, projectivity of the scattering form provides a deep
geometric origin for and interpretation of the BCJ _color-kinematics_ _duality_ [18, 19]
But there is a second, more startling connection to color made apparent by the scattering forms—“Color is Kinematics”. More precisely, as a simple consequence of momentum
conservation and on-shell conditions, the wedge product of the _d_ (propagator) factors associated with any cubic graph satisfies exactly the same algebraic identities as the color factors
associated with the same graph, as indicated in Figure 4 for a _n_ = 5 example. This “Color
is Kinematics” connection allows us to speak of the scattering forms for Yang-Mills theory
and the Non-linear Sigma Model in a fascinating new way. Instead of thinking about partial
amplitudes, or of objects dressed with color factors, we deal with fully permutation invari

                   - 6                   

ant differential forms on kinematic space with no color factors in sight! The usual colored
amplitudes can be obtained from these forms by replacing the wedges of the _d_ of propagators with color factors in a completely unambiguous way. These forms are furthermore
rigid, god-given objects, entirely fixed (at least at tree level) simply by standard dimensional power-counting, gauge-invariance (for YM) or the Adler zero (for the NLSM) [20],
and the requirement of projectivity. And of course, these forms are again obtained as
the “pushforward” via the scattering equations from the familiar differential forms on the
worldsheet [15, 21], in parallel to the bi-adjoint theory.
We now proceed to describe all the ideas sketched above in much more detail before
concluding with remarks on avenues for further work in this direction.


**2** **The** **Planar** **Scattering** **Form** **on** **Kinematic** **Space**


We introduce the _planar_ _scattering_ _form_, which is a _differential_ _form_ on the space of kinematic variables that encodes information about on-shell tree-level scattering amplitudes of
the bi-adjoint scalar. We emphasize the importance of “upgrading” amplitudes to forms,
which reveals deep and unexpected connections between physics and geometry that are not
seen in the Feynman diagram expansion, leading amongst other things to novel (and in some
cases more compact) representations of the amplitudes. We also find connections to scattering equations and color-kinematics duality as discussed in Sections 6 and 8, respectively.
We generalize to Yang-Mills and Non-linear Sigma Model in Section 9.


**2.1** **Kinematic** **Space**


We begin by defining the kinematic space _Kn_ for _n_ massless momenta _pi_ for _i_ = 1 _, . . ., n_ as
the space spanned by linearly independent Mandelstam variables in spacetime dimension
_D_ _≥_ _n−_ 1:
_sij_ := ( _pi_ + _pj_ ) [2] = 2 _pi · pj_ (2.1)


For _D_ _<_ _n−_ 1 there are further constraints on Mandelstam variables—Gram determinant
conditions—so the number of independent variables is lower. Due to the massless on-shell
conditions and momentum conservation, we have _n_ linearly independent constraints


_n_

     
_sij_ = 0 for _i_ = 1 _,_ 2 _, . . ., n_ (2.2)

_j_ =1; _j_ = _i_


The dimensionality of kinematic space is therefore




   - _n_
dim _Kn_ =
2





_−_ _n_ = _[n]_ [(] _[n][−]_ [3)] (2.3)

2





_−_ _n_ = _[n]_ [(] _[n][−]_ [3)]



More generally, for any set of particle labels _I_ _⊂{_ 1 _, . . ., n}_, we define the Mandelstam
variable



�2
=  


_sij_ (2.4)

_i,j∈I_ ; _i<j_



_sI_ :=



��

_pi_

_i∈I_



��




- 7 

1







2



7







7





3



6



5









5



**Figure** **5** : Correspondence between a 3-diagonal partial triangulation and a triple cut.
Note that the vertices are numbered on the left while the edges/particles are numbered on
the right.


It follows from momentum conservation that _sI_ = _sI_ ¯, where _I_ [¯] is the complement of _I_ . For
mutually disjoint index sets _I_ 1 _, . . ., Id_, we define _sI_ 1 _···Id_ := _sI_ 1 _∪···∪Id_ . We also define, for any
pair of index sets _I, J_ :






  = _sij_ (2.5)

_i∈I,j∈J_









 [�] _pj_

_j∈J_



_sI|J_ := 2



��

_pi_

_i∈I_




_·_



**2.2** **Planar** **Kinematic** **Variables**


We now focus on kinematic variables that are particularly useful for cyclically ordered
particles. For the _standard_ _ordering_ (1 _,_ 2 _, . . ., n_ ), we define _planar_ _variables_ with manifest
cyclic symmetry:
_Xi,j_ := _si,i_ +1 _,...,j−_ 1 (2.6)


for any pair of indices 1 _≤_ _i_ _<_ _j_ _≤_ _n_ . Note that _Xi,i_ +1 and _X_ 1 _,n_ vanish. Given a convex
_n_ -gon with cyclically ordered vertices, the variable _Xi,j_ can be visualized as the diagonal
between vertices _i_ and _j_, as in Figure 5 (left).
The Mandelstam variables in particular can be expanded in terms of these variables,
by the easily verified identity:


_sij_ = _Xi,j_ +1 + _Xi_ +1 _,j_ _−_ _Xi,j_ _−_ _Xi_ +1 _,j_ +1 (2.7)


It follows that the non-vanishing planar variables form a spanning set of kinematic space.
However, they also form a basis, since there are exactly dim _Kn_ = _n_ ( _n−_ 3) _/_ 2 of them. It is
rather curious that the number of planar variables is precisely the dimension of kinematic
space. Examples of the basis include _{s_ := _X_ 1 _,_ 3 _, t_ := _X_ 2 _,_ 4 _}_ for _n_ =4 particles and _{s_ 12 =
_X_ 1 _,_ 3 _, s_ 23 = _X_ 2 _,_ 4 _, s_ 34 = _X_ 3 _,_ 5 _,_ _s_ 123 = _X_ 1 _,_ 4 _, s_ 234 = _X_ 2 _,_ 5 _}_ for _n_ =5.


                   - 8                   

|2|Col2|2|
|---|---|---|
|graph _g_<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>_Xi,j_ =_ X_1_,_4|graph _g_<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>_Xi,j_ =_ X_1_,_4|2<br>3|
||7|5|


|2|Col2|2|
|---|---|---|
|graph _g′_<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>_Xi′,j′_<br>=_ X_2_,_6|graph _g′_<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>_Xi′,j′_<br>=_ X_2_,_6|2<br>3|
||7|5|



**Figure** **6** : Two planar graphs related by a mutation given by an exchange of channel
_Xi,j_ _→_ _Xi′,j′_ in a four point subgraph


More generally, for an ordering _α_ := ( _α_ (1) _, . . ., α_ ( _n_ )) of the external particles, we define
_α-planar_ _variables_
_Xα_ ( _i_ ) _,α_ ( _j_ ) := _sα_ ( _i_ ) _,α_ ( _i_ +1) _,...,α_ ( _j−_ 1) (2.8)


for any pair _i_ _<_ _j_ modulo _n_ . As before, _Xα_ ( _i_ ) _,α_ ( _i_ +1) and _Xα_ (1) _,α_ ( _n_ ) vanish, and the nonvanishing variables form a basis of kinematic space. Also, each variable can be visualized
as a diagonal of a convex _n_ -gon whose vertices are cyclically ordered by _α_ .


**2.3** **The** **Planar** **Scattering** **Form**


We now move on to our main task of defining the _planar_ _scattering_ _form_ . Let _g_ denote a
(tree) cubic graph with propagators _Xia,ja_ for _a_ = 1 _, . . ., n−_ 3. For each ordering of these
propagators, we assign a value sign( _g_ ) _∈{±_ 1 _}_ to the graph with the property that swapping
two propagators flips the sign. Then, we assign to the graph a _d_ log form:



sign( _g_ )



_n−_ 3


_d_ log _Xia,ja_ (2.9)

_a_ =1



where the sign( _g_ ) is evaluated on the ordering in which the propagators appear in the wedge
product. There are of course two sign choices for each graph.
Finally, we introduce the _planar_ _scattering_ _form_ of rank ( _n−_ 3):




  Ω [(] _n_ _[n][−]_ [3)] := sign( _g_ )

planar _g_



_n−_ 3


_d_ log _Xia,ja_ (2.10)

_a_ =1



where we sum over a _d_ log form for every planar cubic graph _g_ . Note that a particle ordering
is implicitly assumed by the construction, so we also denote the form as Ω [(] _[n][−]_ [3)] [1 _, . . ., n_ ]
when we wish to emphasize the ordering. For _n_ =3, we define Ω [(0)] _n_ =3 [:=] _[ ±]_ [1][.]
Since there are two sign choices for each graph, this amounts to many different scattering forms. However, there is a natural choice (unique up to overall sign) obtained by


                   - 9                   

making the following requirement:


The planar scattering form is _projective_ .



In other words, we require the form to be invariant under _local_ GL(1) transformations
_Xi,j_ _→_ Λ( _X_ ) _Xi,j_ for any index pair ( _i, j_ ), or equivalently _sI_ _→_ Λ( _s_ ) _sI_ for any index set _I_ .
This fixes the scattering form up to an overall sign which we ignore.
Moreover, this gives a simple _sign-flip_ _rule_ which we now describe. We say that two
planar graphs _g, g_ _[′]_ are related by a _mutation_ if one can be obtained from the other by
an exchange of channel in a four-point sub-graph (See Figure 6). Let _Xi,j, Xi′,j′_ denote
the mutated propagators, respectively, and let _Xib,jb_ for _b_ = 1 _, . . ., n−_ 4 denote the shared
propagators. Under a local GL(1) transformation, the Λ-dependence of the scattering form
becomes:

             - _n−_ 4              
�sign( _g_ ) + sign( _g_ _[′]_ )� _d_ log Λ _∧_           - _d_ log _Xi_ _,j_ + _· · ·_ (2.11)




- _n−_ 4

 






_d_ log _Xib,jb_

_b_ =1



+ _· · ·_ (2.11)



where we have only written the terms involving the _d_ log of all shared propagators of _g_ and
_g_ _[′]_ . Here sign( _g_ _[′]_ ) is evaluated on the same propagator ordering as sign( _g_ ) but with _Xi,j_
replaced by _Xi′,j′_ . The form is projective if the Λ-dependence disappears, _i.e._ when we
have
sign( _g_ ) = _−_ sign( _g_ _[′]_ ) (2.12)


for each mutation.
The sign flip rule has several immediate consequences. For instance, it ensures that the
form is cyclically invariant up to a sign:


_i →_ _i_ +1 _⇒_ Ω [(] _n_ _[n][−]_ [3)] _→_ ( _−_ 1) _[n][−]_ [3] Ω [(] _n_ _[n][−]_ [3)] (2.13)


since it takes ( _n−_ 3) mutations (mod 2) to achieve the cyclic shift. The sign flip rule
also ensures that the form factorizes correctly. Indeed, it suffices to consider the channel
_X_ 1 _,m_ _→_ 0 for any _m_ = 3 _, . . ., n−_ 1 for which


_X_ 1 _,m→_ 0
Ω [(] _[n][−]_ [3)] (1 _,_ 2 _, . . ., n_ ) _−−−−−→_ Ω [(] _[m][−]_ [3)] (1 _,_ 2 _, . . ., m−_ 1 _, I_ ) _∧_ _[dX]_ [1] _[,m]_ _∧_ Ω [(] _[n][−][m][−]_ [1)] ( _I_ _[−]_ _, m, . . ., n_ ) _,_

_X_ 1 _,m_

(2.14)
where _pI_ = _−_ [�] _[m]_ _i_ =1 _[−]_ [1] _[p][i]_ [is] [the] [on-shell] [internal] [particle.] [General] [channels] [can] [be] [obtained]
via cyclic shift.
Projectivity is equivalent to the natural statement that the form only depends on _ratios_
of Mandelstam variables, as we can explicitly see in some simple examples for _n_ =4 _,_ 5:




(2.15)



Ω [(1)] (1 _,_ 2 _,_ 3 _,_ 4) = _d_ log _s −_ _d_ log _t_ = _[ds]_




    - _s_
_t_ [=] _[ d]_ [ log] _t_



_s_ _[−]_ _[dt]_ _t_




   
- _X_ 1 _,_ 3
= _d_ log
_X_ 2 _,_ 4




- 10 

Ω [(2)] (1 _,_ 2 _,_ 3 _,_ 4 _,_ 5) = _d_ log _X_ 1 _,_ 4 _∧_ _d_ log _X_ 1 _,_ 3 + _d_ log _X_ 1 _,_ 3 _∧_ _d_ log _X_ 3 _,_ 5 + _d_ log _X_ 3 _,_ 5 _∧_ _d_ log _X_ 2 _,_ 5
+ _d_ log _X_ 2 _,_ 5 _∧_ _d_ log _X_ 2 _,_ 4 + _d_ log _X_ 2 _,_ 4 _∧_ _d_ log _X_ 1 _,_ 4




_[X]_ [1] _[,]_ [3] _∧_ _d_ log _[X]_ [1] _[,]_ [3]

_X_ 2 _,_ 4 _X_ 1 _,_ 4




_[X]_ [1] _[,]_ [3] _∧_ _d_ log _[X]_ [3] _[,]_ [5]

_X_ 2 _,_ 5 _X_ 2 _,_ 4



(2.16)
_X_ 2 _,_ 4



= _d_ log _[X]_ [1] _[,]_ [3]




_[X]_ [1] _[,]_ [3] + _d_ log _[X]_ [1] _[,]_ [3]

_X_ 1 _,_ 4 _X_ 2 _,_ 5



where we have written on the last expression for each example the form in terms of ratios
of _X_ ’s only. For _n_ =6, the form is given by summing over 14 planar graphs which can be
expressed as ratios in the following way:




_[X]_ [2] _[,]_ [4] _∧_ _d_ log _[X]_ [1] _[,]_ [4]

_X_ 1 _,_ 3 _X_ 4 _,_ 6

_[X]_ [2] _[,]_ [6] _∧_ _d_ log _[X]_ [2] _[,]_ [5]

_X_ 1 _,_ 5 _X_ 3 _,_ 5




_[X]_ [1] _[,]_ [5] + _d_ log _[X]_ [2] _[,]_ [6]

_X_ 4 _,_ 6 _X_ 1 _,_ 3

_[X]_ [2] _[,]_ [4] _−_ _d_ log _[X]_ [2] _[,]_ [4]

_X_ 3 _,_ 5 _X_ 1 _,_ 3




_[X]_ [2] _[,]_ [6] _∧_ _d_ log _[X]_ [3] _[,]_ [6]

_X_ 1 _,_ 3 _X_ 1 _,_ 3

_[X]_ [2] _[,]_ [4] _∧_ _d_ log _[X]_ [4] _[,]_ [6]

_X_ 1 _,_ 3 _X_ 3 _,_ 5




_[X]_ [3] _[,]_ [6] _∧_ _d_ log _[X]_ [4] _[,]_ [6]

_X_ 1 _,_ 3 _X_ 3 _,_ 5

_[X]_ [4] _[,]_ [6] _∧_ _d_ log _[X]_ [2] _[,]_ [6]

_X_ 3 _,_ 5 _X_ 1 _,_ 5



_._
_X_ 1 _,_ 5



Ω [(3)] _n_ =6 [=] _d_ log _[X]_ [2] _[,]_ [4]



_X_ 3 _,_ 5




_−_ _d_ log _[X]_ [2] _[,]_ [6]




_[X]_ [1] _[,]_ [4] _∧_ _d_ log _[X]_ [1] _[,]_ [5]

_X_ 4 _,_ 6 _X_ 4 _,_ 6

_[X]_ [2] _[,]_ [5] _∧_ _d_ log _[X]_ [2] _[,]_ [4]

_X_ 3 _,_ 5 _X_ 3 _,_ 5



Finally, for a general ordering _α_ of the external particles, we define the scattering
form Ω [(] _[n][−]_ [3)] [ _α_ ] by making index replacements _i_ _→_ _α_ ( _i_ ) on Ω [(] _n_ _[n][−]_ [3)], which is equivalent to
replacing Eq. (2.10) with a sum over _α_ -planar graphs. Recall that a cubic graph is called
_α-planar_ if it is planar when external legs are ordered by _α_ ; alternatively, we say that the
graph is _compatible_ with the order. Furthermore, the form is projective.
We emphasize that projectivity is a rather remarkable property of the scattering form
which is not true for each Feynman diagram separately. Indeed, no proper subset of Feynman diagrams provides a projective form—only the sum over all the diagrams (satisfying
the sign flip rule) is projective. This foreshadows something we will see much more explicitly later on in connection to the positive geometry of the associahedron: the Feynman
diagram expansion provides just one type of triangulation of the geometry, which introduces a spurious “pole at infinity” that cancels only in the sum over all terms. But other
triangulations that are manifestly projective term-by-term are also possible, and often lead
to even shorter expressions.


**3** **The** **Kinematic** **Associahedron**


We introduce the _associahedron_ polytope [16, 17, 22] and discuss its connection to the
bi-adjoint scalar theory. We begin by reviewing the combinatorial structure of the associahedron before providing a novel construction of the associahedron in kinematic space. We
then argue that the tree level amplitude is a geometric invariant of the kinematic associahedron called its _canonical_ _form_ as review in Appendix A, thus establishing the associahedron
as the “amplituhedron” of the (tree) bi-adjoint theory.


**3.1** **The** **Associahedron** **from** **Planar** **Cubic** **Diagrams**


There exist many beautiful, combinatorial ways of constructing associahedra; an excellent
survey of the subject, together with comprehensive references to the literaure, is given
by [23]. In this section, we discuss one of the most fundamental descriptions of the associahedron which is also most closely related to scattering amplitudes. We begin by clarifying
some terminology regarding polytopes.


                   - 11                   

**Figure** **7** : Combinatorial structure of the _n_ =5 associahedron (left) and the _n_ =6 associahedron (right). For simplicity, only vertices are labeled for the latter.


A _boundary_ of a polytope refers to a boundary of any codimension. A _k_ -boundary is a
boundary of dimension _k_ . A _facet_ is a codimension 1 boundary. Given a convex _n_ -gon, a
_diagonal_ is a straight line between any two non-adjacent vertices. A _partial triangulation_ is a
collection of mutually non-crossing diagonals. A _full_ _triangulation_ or simply a _triangulation_
is a partial triangulation with maximal number of diagonals, namely ( _n−_ 3).
For any _n≥_ 3, consider a convex polytope of dimension ( _n−_ 3) with the following properties:


1. For every _d_ = 0 _,_ 1 _, . . ., n−_ 3, there exists a one-to-one correspondence between the
codimension _d_ boundaries and the _d_ -diagonal partial triangulations of a convex _n_   gon.


2. A codimension _d_ boundary _F_ 1 and a codimension _d_ + _k_ boundary _F_ 2 are adjacent if
and only if the partial triangulation of _F_ 2 can be obtained by addition of _k_ diagonals
to the partial triangulation of _F_ 1.


In particular, the triangulation with no diagonals corresponds to the polytope’s interior,
and:
The vertices correspond to the full triangulations. (3.1)


A classic result in combinatorics says that the number of full triangulations, and hence the
number of vertices of our polytope, is the Catalan number _Cn−_ 2 [24]. Any polytope _An_
satisfying these properties is an _associahedron_ . See Figure 7 for examples.
Before establishing a precise connection to scattering amplitudes, we make a few observations that provide some of the guiding principles. Let us order the edges of the _n_ -gon
cyclically with 1 _, . . ., n_, and recall that:


_d_ -diagonal partial triangulations of the _n_ -gon are in one-to-one correspondence


with _d_ -cuts on _n_ -particle planar cubic diagrams. (See Figure 5) (3.2)


                   - 12                   

The edges of the _n_ -gon correspond to external particles, while the diagonals correspond to
cuts.
Furthermore, the associahedron _factorizes_ _combinatorially_ . That is, consider a facet _F_
corresponding to some diagonal that subdivides the _n_ -gon into a _m_ -gon and a ( _n−m_ +2)gon (See Figure 15). The two lower polygons provide the combinatorial properties for two
lower associahedra _Am_ and _An−m_ +2, respectively, and the facet is combinatorially identical
to their direct product:
_F_ _[∼]_ = _Am × An−m_ +2 (3.3)


We show in Section 4.1 that this implies the factorization properties of amplitudes.
Finally, we observe that the associahedron is a _simple_ polytope, meaning that each
vertex is adjacent to precisely dim _An_ = ( _n−_ 3) facets. Indeed, given any associahedron
vertex and its corresponding triangulation, the adjacent facets correspond to the ( _n−_ 3)
diagonals.


**3.2** **The** **Kinematic** **Associahedron**


We now show that there is an associahedron naturally living in the kinematic space for _n_
particles. The construction depends on an ordering for the particles which we take to be
the standard ordering for simplicity.
We first define a region ∆ _n_ in kinematic space by imposing the inequalities


_Xi,j_ _≥_ 0 for all 1 _≤_ _i < j_ _≤_ _n_ (3.4)


Recall that _Xi,i_ +1 and _X_ 1 _n_ are trivially zero and therefore do not provide conditions. Since
the number of non-vanishing planar variables is exactly the dimension of kinematic space,
it follows that ∆ _n_ is a simplex with a facet at infinity. This leads to an obvious problem.
The associahedron _An_ should have dimension ( _n−_ 3), which for _n_ _>_ 3 is lower than the
kinematic space dimension. We resolve this by restricting to a ( _n−_ 3)-subspace _Hn_ _⊂Kn_
defined by a set of constants:


Let _cij_ := _Xi,j_ + _Xi_ +1 _,j_ +1 _−_ _Xi,j_ +1 _−_ _Xi_ +1 _,j_ be a _positive_ _constant_

for every pair of _non-adjacent_ indices 1 _≤_ _i < j_ _≤_ _n−_ 1 (3.5)


Note that we have deliberately omitted _n_ from the index range. Also, Eq. (2.7) implies the
following simple identity:
_cij_ = _−sij_ (3.6)


The condition Eq. (3.5) is therefore equivalent to requiring _sij_ to be a _negative_ _constant_ for
the same index range. Counting the number of constraints, we find the desired dimension:


dim _Hn_ = dim _Kn −_ [(] _[n][ −]_ [2)(] _[n][ −]_ [3)] = _n −_ 3 (3.7)

2


Finally, we let _An_ := _Hn_ _∩_ ∆ _n_ be a polytope. We claim that _An_ _is_ _an_ _associahedron_ _of_
_dimension_ ( _n−_ 3). See Figure 8 for examples. Recall from Section 3.1 that the associahedron


                   - 13                   

_X_ 2 _,_ 5



_X_ 1 _,_ 4







_X_ 1 _,_ 3







**Figure** **8** : Kinematic associahedra for _n_ =4 (top left), _n_ =5 (top right) and _n_ =6 (bottom).


factorizes combinatorially, meaning that each facet is combinatorially the direct product of
two lower associahedra as in Eq. (3.3). In Section 4.1, we show that the same property
holds for the kinematic polytope _An_, thereby implying our claim.
Here we highlight the key observation needed for showing factorization and hence the
associahedron structure. Note that the boundaries are enforced by the positivity conditions
_Xi,j_ _≥_ 0, so that we can reach any codimension 1 boundary by setting some particular
_Xi,j_ _→_ 0. But then, to reach a lower dimensional boundary, we cannot set _Xk,l_ _→_ 0 for any
diagonal ( _k, l_ ) that _crosses_ ( _i, j_ ) (See Figure 9). Indeed, if we begin with the basic identity
Eq. (3.5) with ( _i, j_ ) replaced by ( _a, b_ ) and sum _a, b_ over the range _i ≤_ _a < j_ and _k_ _≤_ _b < l_,
the sums telescope and we find




    _Xj,k_ + _Xi,l_ = _Xi,k_ + _Xj,l −_

_i≤a<j_
_k≤b<l_



_cab_ (3.8)



for any 1 _≤_ _i_ _<_ _j_ _<_ _k_ _<_ _l_ _≤_ _n_ . Now consider a situation like Figure 10 (top) where the


                   - 14                   

Not allowed!


**Figure** **9** : Planar variables _Xi,j_ corresponding to crossing diagonals cannot be simultaneously set to zero.


diagonals _Xi,k_ = 0 and _Xj,l_ = 0 cross, then




   _Xj,k_ + _Xi,l_ = _−_

_i≤a<j_
_k≤b<l_



_cab_ (3.9)



which is a contradiction since the left side is _nonnegative_ while the right side is _strictly_
_negative_ . Geometrically, this means that every boundary of _An_ is labeled by a set of noncrossing diagonals ( _i.e._ a partial triangulation), as expected for the associahedron.
Let us do some quick examples. For _n_ =4, the kinematic space with variables ( _s, t, u_ )
satisfies the constraint _s_ + _t_ + _u_ = 0 and is 2-dimensional. However, the kinematic associahedron is given by the line segment 0 _<_ _s_ _<_ _−u_ where _u_ _<_ 0 is a constant, as shown in
Figure 8 (top left). For _n_ =5, the kinematic space is 5-dimensional, but the subspace _Hn_ =5
is 2-dimensional defined by three constants _c_ 13 _, c_ 14 _, c_ 24. If we parameterize the subspace in
the basis ( _X_ 1 _,_ 3 _, X_ 1 _,_ 4), then the associahedron _An_ =5 is a pentagon with edges given by:


_X_ 1 _,_ 3 _≥_ 0 (3.10)

_X_ 3 _,_ 5 = _−X_ 1 _,_ 4 + _c_ 14 + _c_ 24 _≥_ 0 (3.11)

_X_ 2 _,_ 5 = _−X_ 1 _,_ 3 + _c_ 13 + _c_ 14 _≥_ 0 (3.12)

_X_ 2 _,_ 4 = _X_ 1 _,_ 4 _−_ _X_ 1 _,_ 3 + _c_ 13 _≥_ 0 (3.13)

_X_ 1 _,_ 4 _≥_ 0 (3.14)


where the edges are given in clockwise order (See Figure 8 (top right)). The _n_ =6 example
is given in Figure 8 (bottom).
The associahedron _An_ in kinematic space is only one step away from scattering amplitudes, as we now show.


**3.3** **Bi-adjoint** _φ_ [3] **Amplitudes**


We now show the connection between the kinematic associahedron _An_ and scattering amplitudes in bi-adjoint scalar theory. The discussion here applies to tree amplitudes with
a pair of standard ordering, which we denote by _mn_ . We generalize to arbitrary ordering
pairs _m_ [ _α|β_ ] in Section 3.4. This section relies on the concept of _positive_ _geometries_ and
_canonical_ _forms_, for which a quick review is given in Appendix A. For readers unfamiliar


                   - 15                   

with the subject, Appendices A.1, A.4 and A.5 suffice for the discussion in this section. A
much more detailed discussion is given in [13].
We make two claims in this section:


1. The pullback of the cyclic scattering form Ω [(] _n_ _[n][−]_ [3)] to the subspace _Hn_ is the canonical
form of the associahedron _An_ .


2. The canonical form of the associahedron _An_ determines the tree amplitude of the
bi-adjoint theory with identical ordering.


Recall that the associahedron is a simple polytope (See end of Section 3.1), and the
canonical form of a simple polytope (See Eq. (A.23)) is a sum over its vertices. For each
vertex _Z_, let _Xia,ja_ = 0 denote its adjacent facets for _a_ = 1 _, . . ., n−_ 3. Furthermore, for each
ordering of the facets, let sign( _Z_ ) _∈{±_ 1 _}_ denote its orientation relative to the inherited
orientation. The canonical form is therefore



Ω( _An_ ) = - sign( _Z_ )


vertex _Z_



_n−_ 3


_d_ log _Xia,ja_ (3.15)

_a_ =1



where sign( _Z_ ) is evaluated on the ordering of the facets in the wedge product. Since the
form is defined on the subspace _Hn_, it may be helpful to express the _Xi,j_ variables in terms
of a basis of ( _n−_ 3) variables like Eq. (5.4).
We argue that Eq. (3.15) is equivalently the pullback of the scattering form Eq. (2.10)
to the subspace _Hn_ . Since there is a one-to-one correspondence between vertices _Z_ and
planar cubic graphs _g_, it suffices to show that the pullback of the _g_ term is the _Z_ term.
This is true by inspection since _g_ and its corresponding _Z_ have the same propagators _Xia,ja_ .
The only subtlety is that the sign( _Z_ ) appearing in Eq. (3.15) is defined geometrically, while
the sign( _g_ ) appearing in Eq. (2.10) is defined by local GL(1) invariance. We now argue
equivalence of the two by showing that sign( _Z_ ) satisfies the sign flip rule.
Suppose _Z, Z_ _[′]_ are vertices whose triangulations are related by a mutation. While
mutations are defined as relations between planar cubic graphs (See Figure 6), they can
equivalently be interpreted from the triangulation point of view. Indeed, two triangulations
are related by a mutation if one can be obtained from the other by exchanging exactly one
diagonal. For example, the two triangulations of a quadrilateral are related by mutation.
For a generic triangulation of the _n_ -gon, every mutation can be obtained by identifying a
quadrilateral in the triangulation and exchanging its diagonal. In Figure 10 (top), we show
an example where a mutation is applied to the quadrilateral ( _i, j, k, l_ ) with the diagonal
( _i, k_ ) in _Z_ exchanged for the diagonal ( _j, l_ ) in _Z_ _[′]_ . Note that we have implicitly assumed
1 _≤_ _i_ _<_ _j_ _<_ _k_ _<_ _l_ _≤_ _n_ . Furthermore, taking the exterior derivative of the kinematic
identity Eq. (3.8) gives us


_dXj,k_ + _dXi,l_ = _dXi,k_ + _dXj,l ._ (3.16)


Note that the two propagators on the left appear in both diagrams, while the two propa

                   - 16                   

_k_



= _⇒_













_k_





= _⇒_





**Figure** **10** : Two triangulations related by a mutation _Xi,k_ _→_ _Xj,l_ (top) or equivalently
_sIJ_ _→_ _sJK_ (bottom).


gators on the right are related by mutation. It follows that



_n−_ 3


_dXia,ja_ = _−_

_a_ =1



_n−_ 3


_dXi′a,ja′_ (3.17)
_a_ =1



The crucial part is the minus sign, which implies the sign flip rule:


sign( _Z_ ) = _−_ sign( _Z_ _[′]_ ) (3.18)


We can therefore identify sign( _Z_ ) = sign( _g_ ). Furthermore, an important consequence of
(3.17) is that the following quantity is independent of _g_ on the pullback:



_d_ _[n][−]_ [3] _X_ := sign( _g_ )


Substituting into Eq. (3.15) gives



_n−_ 3


_dXia,ja_ (3.19)

_a_ =1





 _d_ _[n][−]_ [3] _X_ = _mnd_ _[n][−]_ [3] _X_ (3.20)



Ω( _An_ ) =





 [�]

planar _g_



1

- _n−_ 3
_a_ =1 _[X][i]_ _a_ _[,j]_ _a_



which gives the expected amplitude _mn_, thus completing the argument for our second claim.
For convenience we sometimes denote the item in parentheses as Ω( _An_ ), called the _canonical_


                   - 17                   

_rational_ _function_ . Thus,
Ω( _An_ ) = _mn_ (3.21)



Let us do a quick and informative example for _n_ =4. We use the usual Mandelstam
variables ( _s, t, u_ ) := ( _X_ 1 _,_ 3 _, X_ 2 _,_ 4 _, −X_ 1 _,_ 3 _−_ _X_ 2 _,_ 4 = _−c_ 13). Here _u_ is a negative constant, and
the associahedron is simply the line segment 0 _≤_ _s_ _≤−u_ in Figure 8 (top left), whose
canonical form is




    - 1 1
Ω( _An_ =4) =
_s_ _[−]_ _s_ + _u_




- - 1
_ds_ = [1]
_s_ [+] _t_



_t_




_ds_ (3.22)



which of course is also the desired amplitude up to the _ds_ factor. Now consider pulling back
the planar scattering form Eq. (2.15). Since _u_ is a constant on _Hn_ =4 and _s_ + _t_ + _u_ = 0,
hence _ds_ = _−dt_ on the pullback. It follows that



Ω [(1)] _n_ =4 _[|][H]_ _n_ =4 [=] - 1 [1]
_s_ [+] _t_




_ds_ (3.23)



which is equal to Eq. (3.22). We also demonstrate an example for _n_ = 5 where the associahedron is a pentagon as shown in Figure 8 (top right). We argue that the pullback of Eq. (2.16)
determines the 5-point amplitude by showing that the numerators have the expected sign on
the pullback, namely _dX_ 1 _,_ 4 _dX_ 1 _,_ 3 = _dX_ 1 _,_ 3 _dX_ 3 _,_ 5 = _dX_ 3 _,_ 5 _dX_ 2 _,_ 5 = _dX_ 2 _,_ 5 _dX_ 2 _,_ 4 = _dX_ 2 _,_ 4 _dX_ 1 _,_ 4.
For instance, the identity _X_ 3 _,_ 5 = _−X_ 1 _,_ 4 + _c_ 14 + _c_ 24 implies _∂_ ( _X_ 1 _,_ 4 _, X_ 1 _,_ 3) _/∂_ ( _X_ 1 _,_ 3 _, X_ 3 _,_ 5) = 1,
leading to the first equality. We leave the rest as an exercise for the reader. It follows that
the pullback determines the corresponding amplitude.




     - 1 1 1 1 1
Ω [(2)] _n_ =5 _[|][H]_ _n_ =5 [=] + + + +
_X_ 1 _,_ 3 _X_ 1 _,_ 4 _X_ 3 _,_ 5 _X_ 1 _,_ 3 _X_ 1 _,_ 4 _X_ 2 _,_ 4 _X_ 2 _,_ 5 _X_ 3 _,_ 5 _X_ 2 _,_ 4 _X_ 2 _,_ 5


Of course, this is also the canonical form of the pentagon.


**3.4** **All** **Ordering** **Pairs** **of** **Bi-adjoint** _φ_ [3] **Amplitudes**




_d_ [2] _X_ (3.24)



We now generalize our results to every ordering pair of the bi-adjoint theory. Given an
ordering pair _α, β_, the amplitude is given by the sum of all cubic diagrams _compatible_ with
both orderings, with an overall sign from the trace decomposition [15] that we postpone
to Section 8.2 and more specifically Eq. (8.26). Here we ignore the overall sign and simply
define _m_ [ _α|β_ ] to be the sum over the cubic graphs.
We first review a simple diagrammatic procedure [15] for obtaining all the graphs
appearing in _m_ [ _α|β_ ] as illustrated in Figure 11:


                   - 18                   

**Figure** **11** : Step-by-step procedure for obtaining the mutual cuts (3 [rd] picture) and the
mutual partial triangulation (4 [th] ) for ( _α, β_ ) = (12345678 _|_ 81267354). The first three pictures
are found in [15].


1. Draw _n_ points on the boundary of a disk ordered cyclically by _α_ .


2. Draw a closed path of line segments connecting the points in order _β_ . These line
segments enclose a set of polygons, forming a polygon decomposition.


3. The internal vertices of the decomposition correspond to cuts on cubic graphs called
_mutual_ _cuts_ .


4. The cuts correspond to diagonals of the _α_ -ordered _n_ -gon, forming a _mutual_ _partial_
_triangulation_ .


The cubic graphs compatible with both orderings are precisely those that admit all the
mutual cuts. Equivalently, they correspond to all triangulations of the _α_ -ordered _n_ -gon
containing the mutual partial triangulation. Conversely, given a graph of mutual cuts or
equivalently a mutual partial triangulation, we can reverse engineer the ordering _β_ up to
dihedral transformation as follows:


1. Color each vertex of the graph white or black like Figure 12 so that no two adjacent
vertices have the same color.


2. Draw a closed path that winds around white vertices clockwise and black vertices
counterclockwise.


3. The path gives the ordering _β_ up to cyclic shift. Changing the coloring corresponds
to a reflection.


The path gives the _β_ up to cyclic shift. Swapping the colors reverses the particle ordering.
It follows that _β_ can be obtained up to dihedral transformations.
We are now ready to construct the kinematic polytope for an arbitrary ordering pair.
We break the symmetry between the two orderings by using planar variables _Xα_ ( _i_ ) _,α_ ( _j_ )
discussed at the end of Section 2.2. In analogy with Eq. (3.4), we define a simplex ∆[ _α_ ] in
kinematic space by requiring that:


_Xα_ ( _i_ ) _,α_ ( _j_ ) _≥_ 0 for all 1 _≤_ _i < j_ _≤_ _n_ . (3.25)


                   - 19                   

5



**Figure** **12** : This mutual cut diagram gives rise to ( _α, β_ ) = (12345678 _,_ 81267354) by the
described rules.


Similar to before, _Xα_ ( _i_ ) _,α_ ( _i_ +1) and _Xα_ (1) _,α_ ( _n_ ) vanish and therefore do not provide conditions.
We can visualize the variable _Xα_ ( _i_ ) _,α_ ( _j_ ) as the diagonal ( _α_ ( _i_ ) _, α_ ( _j_ )) of a regular _n_ -gon whose
vertices are labeled by _α_ . Furthermore, we construct a ( _n−_ 3)-subspace _H_ [ _α|β_ ] of kinematic
space by making the following requirements:


1. For each diagonal ( _α_ ( _i_ ) _, α_ ( _j_ )) that crosses at least one diagonal in the mutual partial
triangulation, we require _bα_ ( _i_ ) _,α_ ( _j_ ) := _Xα_ ( _i_ ) _,α_ ( _j_ ) _>_ 0 to be a positive constant.


2. The mutual triangulation (assuming _d_ diagonals) subdivides the _n_ -gon into ( _d_ +1)
sub-polygons, and we impose the non-adjacent constant conditions Eq. (3.5) to each
sub-polygon.


For the last step, it is necessary to omit an edge from each sub-polygon when imposing
the non-adjacent constants. By convention, we omit edges corresponding to the diagonals
of the mutual triangulation as well as edge _n_ of the _n_ -gon so that no two sub-polygons
omit the same element. A moment’s thought reveals that there is only one way to do this.
Finally, we define the kinematic polytope _A_ [ _α|β_ ] := _H_ [ _α|β_ ] _∩_ ∆[ _α_ ]. In particular, for the
standard ordering _α_ = _β_ = (1 _, . . ., n_ ), we recover (∆[ _α_ ] _, H_ [ _α|β_ ] _, A_ [ _α|β_ ]) = (∆ _n, Hn, An_ ).
Let us get some intuition for the shape of the kinematic polytope. Clearly _A_ [ _α|α_ ] is
just the associahedron with boundaries relabeled by _α_ . For general _α, β_, we can think of
the mutual partial triangulation (with _d_ diagonals) as a partial triangulation corresponding
to some codimension _d_ boundary of the associahedron _A_ [ _α|α_ ]. Now imagine “zooming in”
on the boundary by pushing all non-adjacent boundaries to infinity. The non-adjacent
boundaries precisely correspond to partial triangulations of the _α_ -ordered _n_ -gon that cross
at least one diagonal of the mutual partial triangulation. This provides the correct intuition
for the “shape” of the kinematic polytope _A_ [ _α|β_ ]. Said in another way, the polytope _A_ [ _α|β_ ]
is again an associahedron but with incompatible boundaries pushed to infinity.
For _n_ =4, the three distinct kinematic polytopes are shown in Figure 13. For _n_ =5,
consider the case ( _α, β_ ) = (12345 _,_ 13245). The mutual partial triangulation consists of the
regular pentagon with the single diagonal (2 _,_ 4) (See Figure 14 (left)) with two compatible
cubic graphs corresponding to the channels ( _X_ 2 _,_ 4 _, X_ 2 _,_ 5) and ( _X_ 2 _,_ 4 _, X_ 1 _,_ 4). The constants are


                   - 20                   

(a) (1234)
_u <_ 0 const
_d_ log( _s/t_ )



(b) (1324)
_s >_ 0 const
_d_ log _t_



(c) (2134)
_t >_ 0 const
_d_ log _s_



**Figure** **13** : Three orderings for the _n_ =4 kinematic polytopes. We assume the same
_α_ = (1234) but different _β_ (displayed above). Furthermore, we present the constant and
canonical form for each geometry.


given by


_b_ 1 _,_ 3 := _X_ 1 _,_ 3 _>_ 0 (3.26)


_b_ 3 _,_ 5 := _X_ 3 _,_ 5 _>_ 0 (3.27)

_c_ 14 := _X_ 1 _,_ 4 + _X_ 2 _,_ 5 _−_ _X_ 2 _,_ 4 _>_ 0 (3.28)


and the inequalities are given by


_X_ 2 _,_ 4 _≥_ 0 (3.29)


_X_ 2 _,_ 5 _≥_ 0 (3.30)


_X_ 1 _,_ 4 _≥_ 0 (3.31)


Finally we plot this region in the basis ( _X_ 2 _,_ 4 _, X_ 2 _,_ 5) as shown in Figure 14 where the first two
inequalities simply give the positive quadrant while the last inequality gives the diagonal
boundary _X_ 1 _,_ 4 = _c_ 14 _−_ _X_ 2 _,_ 5 + _X_ 2 _,_ 4 _≥_ 0.
Having constructed the kinematic polytope _A_ [ _α|β_ ], we now discuss its connection to
bi-adjoint tree amplitude _m_ [ _α|β_ ] (omitting the overall sign). We make the following two
claims in analogy to the two claims made near the beginning of Section 3.3:


1. The pullback of the cyclic scattering form Ω [(] _[n][−]_ [3)] [ _α_ ] to the subspace _H_ [ _α|β_ ] is the
canonical form of the kinematic polytope _A_ [ _α|β_ ]. That is,


Ω [(] _[n][−]_ [3)] [ _α_ ] _|H_ [ _α|β_ ] = Ω( _A_ [ _α|β_ ]) (3.32)


2. The canonical form of the kinematic polytope _A_ [ _α|β_ ] determines the amplitude _m_ [ _α|β_ ].
That is,
Ω( _A_ [ _α|β_ ]) = _m_ [ _α|β_ ] (3.33)


The derivation is not substantially different than what we have seen before, so we simply


                   - 21                   

2



3





_X_ 2 _,_ 4







_X_ 2 _,_ 5


**Figure** **14** : The mutual partial triangulation for ( _α, β_ ) = (12345 _,_ 13245) (left) and its
kinematic polytope (right). The faded area corresponds to the boundary at infinity. The
two vertices correspond to the two cubic graphs compatible with both orderings.


highlight a few subtleties. For the first claim, recall that the scattering form is a sum over
all _α_ -planar graphs:




  Ω [(] _[n][−]_ [3)] [ _α_ ] = sign( _g_ )


_α_ -planar _g_



_n−_ 3


_d_ log _Xα_ ( _ia_ ) _,α_ ( _ja_ ) (3.34)
_a_ =1



We claim that on the pullback to the subspace _H_ [ _α|β_ ], the numerator is identical and
non-zero for every ( _α, β_ )-planar graph _g_ and zero otherwise:



sign( _g_ )



_n−_ 3


_dXα_ ( _ia_ ) _,α_ ( _ja_ ) =
_a_ =1




_d_ _[n][−]_ [3] _X_ if _g_ is _β_ -planar

(3.35)
0 otherwise



The pullback therefore sums all the _β_ -planar diagrams and destroys all other diagrams,
thus giving the desired amplitude _m_ [ _α|β_ ]:





 _d_ _[n][−]_ [3] _X_ = _m_ [ _α|β_ ] _d_ _[n][−]_ [3] _X_ (3.36)



Ω [(] _[n][−]_ [3)] [ _α_ ] _|H_ [ _α|β_ ] =






 


( _α,β_ )-planar _g_



1

- _n−_ 3
_a_ =1 _[X][α]_ [(] _[i]_ _a_ [)] _[,α]_ [(] _[j]_ _a_ [)]



As before, it can be shown that this is also the canonical form of the kinematic polytope
_A_ [ _α|β_ ]. The canonical forms for the _n_ =4 examples are given in Figure 13. The canonical
form for the _n_ =5 example in Figure 14 is


Ω( _A_ [12345 _|_ 13245]) = _d_ log _X_ 2 _,_ 5 _d_ log _X_ 2 _,_ 4 + _d_ log _X_ 2 _,_ 4 _d_ log _X_ 1 _,_ 4




 - 1 1
= +
_X_ 2 _,_ 5 _X_ 2 _,_ 4 _X_ 2 _,_ 4 _X_ 1 _,_ 4




_d_ [2] _X_ (3.37)



where we used the fact that _dX_ 2 _,_ 5 _dX_ 2 _,_ 4 = _dX_ 2 _,_ 4 _dX_ 1 _,_ 4 on the pullback, which follows from


                   - 22                   

the identity _X_ 1 _,_ 4 = _c_ 14 _−_ _X_ 2 _,_ 5 + _X_ 2 _,_ 4.


**3.5** **The** **Associahedron** **is** **the** **Amplituhedron** **for** **Bi-adjoint** _φ_ [3] **Theory**


Let us summarize the story so far for the bi-adjoint _φ_ [3] theory. We have an obvious kinematic
space _Kn_ parametrized by the _Xi,j_ which is _n_ ( _n −_ 3) _/_ 2-dimensional. We also have a scattering form Ω [(] _n_ _[n][−]_ [3)] of rank ( _n−_ 3) defined on this space, which for _n >_ 3 is of lower than top
rank. This scattering form is fully determined by its association with a positive geometry
living in the kinematic space defined in the following way. First, there is a top-dimensional
“positive region” in the kinematic space given by _Xi,j_ _≥_ 0 whose boundaries are associated
with all the poles of the planar graphs. Next, there is a family of ( _n−_ 3)-dimensional linear
subspaces defined by _Xi,j_ + _Xi_ +1 _,j_ +1 _−_ _Xi,j_ +1 _−_ _Xi_ +1 _,j_ = _cij_ . With appropriate positivity constraints on the constants _cij_ _>_ 0, this subspace intersects the “positive region” in
a positive geometry—the kinematic associahedron _An_ . Furthermore, the scattering form
Ω [(] _n_ _[n][−]_ [3)] on the full kinematic space is fully determined by the property of pulling back to
the canonical form of the associahedron on this family of subspaces. Hence, the physics
of on-shell tree-level bi-adjoint _φ_ [3] amplitudes are completely determined by the positive
geometry not in any auxiliary space but directly in kinematic space.
Furthermore, there is a striking similarity between this description of bi-adjoint _φ_ [3]

scattering amplitudes and the description of planar _N_ = 4 super Yang-Mills (SYM) with the
amplituhedron as the positive geometry [14]. Indeed the general structure is identical. There
is once again a kinematic space, which for planar _N_ = 4 SYM is given by the momentumtwistor variables _Zi_ _∈_ P [3] (R) for _i_ = 1 _, . . ., n_, and a differential form Ω [(4] _n_ _[k]_ [)] of rank 4 _× k_
(for N _[k]_ MHV) on kinematic space that is fully determined by its association with a positive
geometry. We again begin with a “positive region” in the kinematic space which enforces
positivity of all the poles of planar graphs via _⟨ZiZi_ +1 _ZjZj_ +1 _⟩≥_ 0; however, also required
is a set of topological “winding number” conditions enforced by a particular “binary code” of
sign-flip patterns for the momentum-twistor data. This is a top-dimensional subspace of the
full kinematic space. There is also a canonical 4 _× k_ dimensional subspace of the kinematic
space, corresponding to an affine translation of a given set of external data _Z∗_ in the
direction of a fixed _k_ -plane ∆ in _n_ dimensions; this subspace is thus specified by a (4+ _k_ ) _×n_
matrix _Z_ := ( _Z∗,_ ∆) _[T]_ . Provided the condition that all ordered (4+ _k_ ) _×_ (4+ _k_ ) minors of
_Z_ are positive, this subspace intersects the “positive region” in a positive geometry—the
(tree) amplituhedron. The form Ω [(4] _n_ _[k]_ [)] on the full space is fully determined by the property
of pulling back to the canonical form of the amplituhedron found on this family of subspaces.
Once again this connection between scattering forms and positive geometry is seen directly
in ordinary momentum-twistor space, without any reference to the auxiliary Grassmannian
spaces where amplituhedra were originally defined to live.
The nature of the relationship between “kinematic space”, “positive region”, “positive
family of subspaces” and “scattering form” is literally identical in the two stories. We say
therefore that “the associahedron is the amplituhedron for bi-adjoint _φ_ [3] theory”.
Of course there are some clear differences as well. Most notably, the scattering form
Ω [(4] _n_ _[k]_ [)] is directly the super-amplitude with the differentials _dZi_ _[I]_ [interpreted] [as] [Grassmann]
variables _ηi_ _[I]_ [, whereas for the bi-adjoint] _[ φ]_ [3] [theory we have forms on the space of Mandelstam]


                   - 23                   

variables with no supersymmetric interpretation. While the planar _N_ = 4 scattering forms
are unifying different helicities into a single natural object, what are the forms in Mandelstam space doing? As we have already seen in the bi-adjoint example, and with more to
come in later sections, these forms are instead _geometrizing_ _color_ _factors_, as established in
Section 8.


**4** **Factorization** **and** **“Soft”** **Limit**


We now derive two important properties of amplitudes by exploiting geometric properties
of the associahedron:


1. The amplitude factorizes on physical poles.


2. The amplitude vanishes in a “soft” limit.


We emphasize that both properties follow from geometric arguments. While amplitude
factorization is familiar, here it emerges from the “geometry factorization” of the associahedron; and the vanishing in the “soft limit” is a property of the amplitude that is made
more manifest by the geometry than Feynman diagrams.


**4.1** **Factorization**


Recall from Section 3.1 that the associahedron factorizes combinatorially, _i.e._ each facet is
combinatorially identical to a product of two lower associahedra (See Eq. (3.3)). We now
demonstrate this explicitly for the kinematic polytope _An_, thus giving a simple derivation
of the fact that _An_ is indeed an associahedron. While Eq. (3.3) is a purely combinatorial
statement, we go further in this section and find explicit geometric constructions for the
two lower associahedra. We therefore say that _An_ _factorizes_ _geometrically_ . Furthermore,
we argue that _geometrical_ _factorization_ of _An_ directly implies _amplitude_ _factorization_, so
that locality and unitarity of the amplitude are _emergent_ _properties_ of the geometry.
We rewrite the kinematic associahedron _An_ as _A_ (1 _,_ 2 _, . . .,_ ¯ _n_ ) to emphasize the particle
labels and their ordering; we put a bar over index _n_ to emphasize that the subspace _Hn_
is defined with non-adjacent indices omitting _n_ (See Eq. (3.5)). We make the following
observations:


1. _Geometric_ _factorization_ : The facet _Xi,j_ = 0 is equivalent to a product polytope


_An|Xi,j_ =0 = _[∼]_ _AL × AR_ (4.1)


where


_AL_ := _A_ ( _i, i_ +1 _, . . ., j−_ 1 _,_ _I_ [¯] )

_AR_ := _A_ (1 _, . . ., i−_ 1 _, I, j, j_ +1 _, . . .,_ ¯ _n_ ) (4.2)


and _I_ denotes the intermediate particle. The cut can be visualized as the diagonal
( _i, j_ ) on the convex _n_ -gon (See Figure 15).


                   - 24                   

2. _Amplitude_ _factorization_ : The residue of the canonical form along the facet _Xi,j_ = 0
factors:
Res _Xi,j_ =0Ω( _An_ ) = Ω( _AL_ ) _∧_ Ω( _AR_ ) (4.3)


This implies factorization of the amplitude.


We first construct the “left associahedron” _AL_ and the “right associahedron” _AR_ by Eq. (4.2)
as _independent_ associahedra living in _independent_ kinematic spaces. The indices appearing
in the construction are nothing more than well-chosen labels at this point. To emphasize
this, we use independent planar variables for _AL_ and _AR_ :


_AL_ : _La,b_ for _i ≤_ _a < b < j_ (4.4)

_AR_ : _Ra,b_ for 1 _≤_ _a < b < n_ except _i ≤_ _a < b < j_ (4.5)


The index ranges can be visualized as Figure 15 where the “left” planar variables _La,b_
correspond to diagonals of the “left” subpolygon, and likewise for the “right”. Furthermore,
the two associahedra come with positive non-adjacent constants _lab_, _rab_, respectively. For
_lab_ the indices consist of all non-adjacent pairs _a, b_ in the range _i ≤_ _a < b < j_ . For _rab_ they
consist of all non-adjacent pairs _a, b_ in the range (1 _, . . ., i−_ 1 _, I, j, j_ +1 _, . . ., n−_ 1).
We now argue that there exists a one-to-one correspondence:


_AL × AR_ = _[∼]_ _An|Xi,j_ =0 (4.6)


We begin by picking a kinematic basis for _AL_ consisting of _La,b_ variables corresponding
to some triangulation of the left subpolygon in Figure 15, and similarly for the _Ra,b_ variables. The two triangulations combine to form a partial triangulation of the _n_ -gon with the
diagonal ( _i, j_ ) omitted. Each diagonal corresponds to a planar variable, thus providing a
basis for the subspace _Hn|Xi,j_ =0. Furthermore, we assume that the non-adjacent constants
match so that _cab_ = _lab_ for all _lab_ . As for _rab_, we assume that _cab_ = _rab_ for all _rab_ where
_a, b ̸_ = _I_ . Furthermore, _raI_ = [�] _k∈I_ _[c][ak]_ [for] [all] _[r][aI]_ [.]
We then write down the most obvious map _AL × AR_ _→_ _Hn|Xi,j_ =0 given by:


_Xa,b_ = _La,b_ for all left basis variables _La,b_ (4.7)

_Xa,b_ = _Ra,b_ for all right basis variables _Ra,b_ (4.8)


Since the _Xa,b_ variables in the image form a basis for _An|Xi,j_ =0, this completely defines
the map. We observe that _Xa,b_ = _La,b_ holds not just for left basis variables, but for all
left variables _La,b_ . The idea is to rewrite _La,b_ in terms of basis variables and non-adjacent
constants. Since the same formula holds for _Xa,b_, and the constants match by assumption,
therefore the desired result must follow. Similarly, _Xa,b_ = _Ra,b_ holds for all right variables
_Ra,b_ .
Now we argue that the image of the embedding lies in the facet _An|Xi,j_ =0, which
requires showing that all planar propagators _Xa,b_ are positive under the embedding except
for _Xi,j_ = 0. This is trivially true for propagators whose diagonals do not cross ( _i, j_ ),
since either _Xa,b_ = _La,b_ or _Xa,b_ = _Ra,b_ . Now consider a crossing diagonal ( _k, l_ ) satisfying


                   - 25                   

**Figure** **15** : The diagonal (4 _,_ 7) subdivides the 8-gon into a 4-gon (on the “left”) and a
6-gon (on the “right”), suggesting that the facet _X_ 4 _,_ 7 = 0 of the associahedron _An_ =8 is
combinatorially identical to _An_ =4 _× An_ =6.


1 _≤_ _i_ _<_ _k_ _<_ _j_ _<_ _l_ _≤_ _n_ . Applying Eq. (3.8) with indices _j, k_ swapped and setting _Xi,j_ = 0
gives

        _Xk,l_ = _Xk,j_ + _Xi,l_ + _cab_ (4.9)

_i≤a<k_
_j≤b<l_


Since _Xk,j_ is a diagonal of the left subpolygon and _Xi,l_ is a diagonal of the right, they
are both positive. It follows that the right hand side is term-by-term positive, hence our
crossing term _Xk,l_ must also be positive, as claimed. We emphasize that _Xk,l_ is actually
strictly positive, implying that it cannot be cut. This is important because cutting crossing
propagators simultaneously would violate the planar graph structure of the associahedron.
Finally, it is easy to see that this is a one-to-one map, thus completing our argument for
the first assertion Eq. (4.1).
As an example, consider the _n_ =6 kinematic associahedron shown in Figure 8 (bottom).
Let us consider the facet _X_ 2 _,_ 5 = 0 which by geometric factorization is a product of 4-point
associahedra ( _i.e._ a product of line segments) and must therefore be a quadrilateral. This
agrees with Figure 8 (bottom) by inspection. The same is true for the facets _X_ 1 _,_ 4 = 0 and
_X_ 3 _,_ 6 = 0. In contrast, the facet _X_ 3 _,_ 5 = 0 is given by the product of a point with a pentagon,
and is therefore also a pentagon. The same holds for the remaining 5 facets.
The second assertion Eq. (4.3) follows immediately from the first:


Res _Xi,j_ =0Ω( _An_ ) = Ω( _An|Xi,j_ =0) = Ω( _AL × AR_ ) = Ω( _AL_ ) _∧_ Ω( _AR_ ) (4.10)


where the first equality follows from the residue property Eq. (A.1), the second from the
first assertion Eq. (4.1) and the third from the product property Eq. (A.2). This provides
a geometric explanation for the factorization of the amplitude first discussed in Eq. (2.14).


**4.2** **“Soft”** **Limit**


The associahedron geometry suggests a natural “soft limit” where the polytope is “squashed”
to a lower dimensional one, whereby the amplitude obviously vanishes.
Consider the associahedron _An_ which lives in the subspace _Hn_ defined by non-adjacent
constants _cij_ . Let us consider the “soft” limit where the non-adjacent constants _c_ 1 _i_ _→_ 0 go


                   - 26                   

to zero for _i_ = 3 _, . . ., n−_ 1. It follows from kinematic constraints that



_n−_ 1


_c_ 1 _i_ _→_ 0 (4.11)

_i_ =3



_X_ 1 _,_ 3 + _X_ 2 _,n_ = _s_ 12 + _s_ 1 _n_ = _−_



_n−_ 1


_s_ 1 _i_ =

_i_ =3



But since both terms on the left are nonnegative _X_ 1 _,_ 3 _, X_ 2 _,n_ _≥_ 0 inside the associahedron, the
limit “squashes” the geometry to a lower dimension where _X_ 1 _,_ 3 = _X_ 2 _,n_ = 0. The canonical
form must therefore vanish everywhere on _Hn_, implying that the amplitude is identically
zero. Note that if we restrict kinematic variables to the interior of the associahedron, then
_p_ 1 _· pi_ _→_ 0 for every _i_, yielding the true soft limit _p_ 1 _→_ 0. A similar argument can be given
to show that the canonical form vanishes in the “soft” limit where _ci,n−_ 1 _→_ 0 for every
_i_ = 1 _, . . ., n−_ 3. And by cyclic symmetry, the amplitude must vanish under every “soft”
limit given by _sij_ _→_ 0 for some fixed index _i_ and every index _j_ = _i−_ 1 _, i_ +1.
Furthermore, given any triangulation of the associahedron _An_ of the kind discussed in
Section 5.4, every piece of the triangulation is squashed by the “soft” limit. It follows that
the canonical form of each piece must vanish individually.
The fact that the amplitude _mn_ vanishes in this limit is rather non-trivial from a
physical point of view. While the geometric argument we provided is straightforward, there
does not appear to be any obvious physical reason for it. It is another feature of the
amplitude made obvious by the associahedron geometry.
As an example, the _n_ =5 amplitude Eq. (3.24) vanishes in the limit _c_ 13 _, c_ 14 _→_ 0, which
can be seen by substituting the equivalent limits _X_ 1 _,_ 3 _→_ _X_ 1 _,_ 4 _−X_ 2 _,_ 4 and _X_ 2 _,_ 5 _→_ _X_ 2 _,_ 4 _−X_ 1 _,_ 4
directly into the amplitude Eq. (3.24).


**5** **Triangulations** **and** **Recursion** **Relations**


Since the scattering forms pull back to the canonical form on our associahedra, it is natural
to expect that concrete expressions for the scattering amplitudes correspond to natural
triangulations of the associahedron. This connection between triangulations of a positive
geometry and various physical representations of amplitudes has been vigorously explored
in the context of the positive Grassmannian/amplituhedron, with various triangulations of
spaces and their duals corresponding to BCFW and “local” forms for scattering amplitudes.
In the present case of study for bi-adjoint _φ_ [3] theories, we encounter a lovely surprise: one of
the canonical triangulations of the associahedron literally reproduced the Feynman diagram
expansion! Ironically this representation also introduces spurious poles (at infinity!) that
only cancel in the full sum over all diagrams; also, other properties of the amplitude, such
as the vanishing in the “soft” limit discussed in Section 4.2, are also not manifest term-byterm in this triangulation. We also explore a number of other natural triangulations of the
geometry that make manifest the features hidden by the Feynman diagram triangulation.
Quite surprisingly, some triangulations lead to even more compact expressions for these
familiar and already very simple amplitudes! Finally, we introduce a novel recursion relation
for amplitudes based on the factorization properties discussed in Section 4.1.


                   - 27                   

**5.1** **The** **Dual** **Associahedron** **and** **Its** **Volume** **as** **the** **Bi-adjoint** **Amplitude**


Recall that every convex polytope _A_ has a _dual_ _polytope_ _A_ _[∗]_ which we review in Appendix A.4 where some notation is established. An important fact also explained in Appendix A.4 says that the canonical form of any polytope _A_ is determined by the volume of
its dual _A_ _[∗]_ :
Ω( _A_ ) = Vol( _A_ _[∗]_ ) (5.1)


This identity has many implications for both physics and geometry. We refer the reader
to [13] for a more thorough discussion.
Applying Eq. (5.1) to our discussion implies that the canonical form of the associahehdron _An_ is determined by the volume of the _dual_ _associahedron_ _A_ _[∗]_ _n_ [:]


Ω( _An_ ) = Vol( _A_ _[∗]_ _n_ [)] (5.2)


But in the same way, the canonical form is determined by the amplitude _mn_ via Eq. (3.21),
thus suggesting that the amplitude is the volume of the dual:


_mn_ = Vol( _A_ _[∗]_ _n_ [)] (5.3)


This leads to yet another geometric interpretation of the bi-adjoint amplitude. For the
remainder of this section, we describe the construction of the dual associahedron in more
detail, and provide the example for _n_ =5.
Following the discussion in Appendix A.4, we embed the subspace _Hn_ in projective
space P _[n][−]_ [3] (R), and we choose a basis _Xi′_ 1 _[,j]_ 1 _[′]_ _[, . . ., X][i]_ _n_ _[′]_ _−_ 3 _[,j]_ _n_ _[′]_ _−_ 3 [of] [Mandelstam] [variables] [to]
denote coordinates on the subspace:


_Y_ = (1 _, Xi′_ 1 _[,j]_ 1 _[′]_ _[, . . ., X][i]_ _n_ _[′]_ _−_ 3 _[,j]_ _n_ _[′]_ _−_ 3 [)] _[ ∈]_ [P] _[n][−]_ [3][(][R][)] (5.4)


Here we have introduced a zeroth component “1” since the coordinates are embedded projectively. Any other basis can be obtained via a _GL_ ( _n−_ 2) transformation.
Furthermore, we denote the facets of the associahedron in projective coordinates. Recall
that every facet of _An_ is of the form _Xi,j_ = 0. We rewrite this in the form _Wi,j_ _· Y_ = 0 for
some dual vector _Wi,j_ . For example, consider _n_ = 5 in the basis _Y_ = (1 _, X_ 1 _,_ 3 _, X_ 1 _,_ 4). Then


_Y_ _· W_ 2 _,_ 5 = _X_ 2 _,_ 5 = _c_ 13 + _c_ 14 _−_ _X_ 1 _,_ 3 = ( _c_ 13 + _c_ 14 _, −_ 1 _,_ 0) _· Y_ (5.5)


which implies that _W_ 2 _,_ 5 = ( _c_ 13 + _c_ 14 _, −_ 1 _,_ 0). More generally, the components of any _Wi,j_ can
be read off from the expansion of _Xi,j_ in terms of basis variables _Xi′a,ja′_ and non-adjacent
constants. Here we present all the dual vectors for the _n_ = 5 pentagon in Figure 8 (top


                   - 28                   

right):



**Figure** **16** : Two triangulations of the dual associahedron _A_ _[∗]_ _n_ =5


_W_ 1 _,_ 3 = (0 _,_ 1 _,_ 0)


_W_ 3 _,_ 5 = ( _c_ 14 + _c_ 24 _,_ 0 _, −_ 1)

_W_ 2 _,_ 5 = ( _c_ 13 + _c_ 14 _, −_ 1 _,_ 0)

_W_ 2 _,_ 4 = ( _c_ 13 _, −_ 1 _,_ 1)


_W_ 1 _,_ 4 = (0 _,_ 0 _,_ 1) (5.6)









Once the coordinates for the dual vectors _Wi,j_ are computed, they can be thought of as
_vertices_ of the dual associahedron _A_ _[∗]_ _n_ [in] [the] [dual] [projective] [space.] For _n_ =5, the dual
associahedron is a pentagon whose vertices are Eq. (5.6) (See Figure 16).


**5.2** **Feynman** **Diagrams** **as** **a** **Triangulation** **of** **the** **Dual** **Associahedron** **Volume**


We now compute the volume of _A_ _[∗]_ by triangulation and summing over the volume of each
piece. We make use of the fact that _A_ _[∗]_ _n_ [is] [a] _[simplicial]_ [polytope,] [meaning] [that] [each] [facet] [is]
a simplex. This is equivalent to _An_ being a simple polytope. In this case the dual is easily
triangulated by the following method:


1. Take a reference point _W∗_ on the interior of the dual polytope.


2. For each facet of the dual, take the convex hull of the facet with _W∗_ which gives a
simplex.


3. The union of all such simplices forms a triangulation of the dual.


Let _Z_ denote a _facet_ of the dual _A_ _[∗]_ _n_ [.] Then _Z_ is adjacent to some vertices _Wi_ 1 _,j_ 1 _, . . .,_
_Win−_ 3 _,jn−_ 3 corresponding to propagators _Xi_ 1 _,j_ 1 _, . . ., Xin−_ 3 _,jn−_ 3, respectively. By taking the
convex hull of the facet _Z_ with _W∗_, and taking the union over all facets, we get a triangulation of the dual associahedron whose volume is the sum over the volume of each simplex.


                   - 29                   

Recalling the formula for the volume of a simplex Eq. (A.20), we find


     Vol( _A_ _[∗]_ _n_ [)] [=] Vol( _W∗, Wi_ 1 _,j_ 1 _, . . ., Win−_ 3 _,jn−_ 3)

vertex _Z_



= 

vertex _Z_



sign( _Z_ ) - _W∗Wi_ 1 _,j_ 1 _· · · Win−_ 3 _,jn−_ 3�

( _Y_ _· W∗_ ) [�] _a_ _[n]_ =1 _[−]_ [3][(] _[Y]_ _[·][ W][i]_ _a_ _[,j]_ _a_ [)]



(5.7)



where sign( _Z_ ) is the orientation of the adjacent vertices _Wi_ 1 _,j_ 1 _, . . ., Win−_ 3 _,jn−_ 3 (in that order)
relative to the inherited orientation. Note that the antisymmetry of sign( _Z_ ) is compensated
by the antisymmetry of the determinant _⟨· · · ⟩_ in the numerator, and the sum is independent
of the choice of reference point _W∗_ . Furthermore, the sign( _Z_ ) here is equivalent to the
sign( _Z_ ) appearing in Eq. (3.15) where _Z_ denotes the corresponding _vertex_ of _An_ . In fact,
we now argue that for an appropriate choice of reference point _W∗_, the Feynman diagram
expansion Eq. (3.20) is term-by-term equivalent to the expression Eq. (5.7), where each _Z_
is associated with its corresponding planar cubic graph _g_ .
With the benefit of hindsight, we set the reference point to _W∗_ = (1 _,_ 0 _. . .,_ 0), which is
particularly convenient because the numerators in Eq. (5.7) are now equivalent for all _Z_ .
Indeed, since _Xia,ja_ = _Y_ _· Wia,ja_, we have


    - _W∗Wi_ 1 _,i_ 1 _· · · Win−_ 3 _,jn−_ 3� = _[∂]_ [(] _[X][i]_ [1] _[,j]_ [1] _[, . . ., X][i][n][−]_ [3] _[,j][n][−]_ [3][)] (5.8)

_∂_ ( _Xi′_ 1 _[,j]_ 1 _[′]_ _[, . . ., X][i]_ _n_ _[′]_ _−_ 3 _[,j]_ _n_ _[′]_ _−_ 3 [)] [=][ sign][(] _[Z]_ [)] _[/]_ [sign][(] _[Z][′]_ [)]


where the primed variables form the basis we chose back in Eq. (5.4), and the second equality
follows from Eq. (3.17). This shows that all the numerators in Eq. (5.7) are equivalent to
sign( _Z_ _[′]_ ), which we set to one. Finally, substituting ( _Y_ _· W∗_ ) = 1 and ( _Y_ _· Wia,ja_ ) = _Xia,ja_
into Eq. (5.7) and replacing _Z_ by _g_ gives



Vol( _A_ _[∗]_ _n_ [) =] 
planar _g_



1
(5.9)

- _n−_ 3
_a_ =1 _[X][i]_ _a_ _[,j]_ _a_



which is precisely the Feynman diagram expansion Eq. (3.20) for the amplitude. It follows
that the amplitude is the volume of the dual associahedron


Vol( _A_ _[∗]_ _n_ [) =][ Ω(] _[A][n]_ [) =] _[ m][n]_ (5.10)


of which the Feynman diagram expansion is a particular triangulation.
We point out that the Feynman diagram expansion introduces a spurious vertex _W∗_,
which term-by-term gives rise to a pole at infinity that cancels in the sum. From the point
of view of the original associahedron, this corresponds to a “signed” triangulation of _An_
with overlapping simplices, whereby every simplex consists of all the facets that meet at
a vertex together with the boundary at infinity. The presence of bad poles at infinity in
individual Feynman diagrams that only cancel in the sum over all diagrams bears striking
resemblance to the behavior of Feynman diagrams under BCFW shifts in gauge theories
and gravity. There too, individual Feynman diagrams have poles at infinity, even though


                   - 30                   

the final amplitude does not, and this surprising vanishing at infinity is critically related
to the magical properties of amplitudes in these theories. Indeed, the absence of poles
at infinity in Yang-Mills theory finds a deeper explanation in terms of the symmetry of
dual conformal invariance. It is thus particularly amusing to see an analog of this hidden
symmetry even for something as innocent-seeming as bi-adjoint _φ_ [3] theory! Furthermore, the
scattering form in the full kinematic space is projectively invariant, a symmetry invisible
in individual diagrams. And the pullback of the forms to the associahedron subspaces
are _also_ projectively invariant, with no pole at infinity. In Yang-Mills theories, we have
discovered representations (such as those based on BCFW recursion relations) that make
the dual conformal symmetry manifest term-by-term, and these were much later seen to
be associated with triangulations of the amplituhedron. Similarly, we now turn to other
natural triangulations of the associahedron which do not introduce new vertices and thus
have no spurious poles at infinity, thus making manifest term-by-term the analogous feature
of bi-adjoint _φ_ [3] amplitudes that is hidden in Feynman diagrams.


**5.3** **More** **Triangulations** **of** **the** **Dual** **Associahedron**


Returning to Eq. (5.7), a different choice of _W∗_ would have led to alternative triangulations,
and hence novel formulas for the amplitude. For instance, for _n_ =5, we can take the limit
_W∗_ _→_ _W_ 13. This kills two volume terms and gives a three-term triangulation as shown in
Figure 16 (right):



_mn_ =5 = _[X]_ [1] _[,]_ [3][ +] _[ X]_ [2] _[,]_ [5]




_[X]_ [1] _[,]_ [3][ +] _[ X]_ [2] _[,]_ [5] + _[X]_ [1] _[,]_ [3] _[ −]_ _[X]_ [1] _[,]_ [4][ +] _[ X]_ [2] _[,]_ [4]

_X_ 1 _,_ 3 _X_ 2 _,_ 5 _X_ 2 _,_ 4 _X_ 1 _,_ 3 _X_ 2 _,_ 4 _X_ 1 _,_ 4




_[X]_ [1] _[,]_ [3][ +] _[ X]_ [2] _[,]_ [5] + _[X]_ [1] _[,]_ [3][ +] _[ X]_ [2] _[,]_ [5]

_X_ 1 _,_ 3 _X_ 3 _,_ 5 _X_ 2 _,_ 5 _X_ 1 _,_ 3 _X_ 2 _,_ 5 _X_ 2 _,_



_X_ 1 _,_ 3 _X_ 2 _,_ 4 _X_ 1 _,_ 4



(5.11)



Note that we have re-written the non-adjacent constants _cij_ in terms of planar variables
via Eq. (3.5). The sum of these three volumes gives the volume of the dual associahedron,
and hence the amplitude. Furthermore, since no spurious vertices are introduced, the result
makes manifest term-by-term the absence of poles at infinity. This contrasts the Feynman
diagram expansion where spurious poles appear term-by-term. Finally, this method of
setting _W∗_ to one of the vertices can be repeated for arbitrary _n_, and in general produces
fewer terms than with Feynman diagrams.


**5.4** **Direct** **Triangulations** **of** **the** **Kinematic** **Associahedron**


Recall that canonical forms are _triangulation_ _independent_, hence the canonical form of a
polytope can be obtained by triangulation and summation over the canonical form of each
piece. A brief review is given in Appendix A.2. We now exploit this property to compute
the canonical form of the associahedron, thus establishing another method for computing
amplitudes.
We wish to compute the _n_ =5 amplitude for which the associahedron is a pentagon.
We choose the basis _Y_ = (1 _, X_ 13 _, X_ 14), and triangulate the associahedron as the union of
three triangles _ABC_, _ACD_ and _ADE_ (See Figure 17). It follows that


Ω( _An_ =5) = Ω( _ABC_ ) + Ω( _ACD_ ) + Ω( _ADE_ ) (5.12)


                   - 31                   

_X_ 1 _,_ 3


_A_



_X_ 1 _,_ 4 _E_



_X_ 1 _,_ 4





_X_ 2 _,_ 5


_D_





**Figure** **17** : A triangulation of the associahedron _An_ =5


Note that the triangles must be oriented in the same way as the associahedron (clockwise
in this case). Getting the wrong orientation would cause a sign error. The boundaries of
the triangles are given by _W_ _· Y_ = 0 for:


_WAB_ = (0 _,_ 1 _,_ 0) _WBC_ = ( _c_ 14 + _c_ 24 _,_ 0 _, −_ 1)

_WCD_ = ( _c_ 13 + _c_ 14 _, −_ 1 _,_ 0) _WDE_ = ( _c_ 13 _, −_ 1 _,_ 1) _WAE_ = (0 _,_ 0 _,_ 1)

_WAC_ = (0 _, −c_ 14 _−_ _c_ 24 _, c_ 13 + _c_ 14) _WAD_ = (0 _, −c_ 14 _, c_ 13 + _c_ 14) (5.13)


Recalling the canonical form for a simplex Eq. (A.21), we get


Ω( _ABC_ ) = [(] _[X]_ [1] _[,]_ [3][ +] _[ X]_ [2] _[,]_ [5][)(] _[X]_ [1] _[,]_ [4][ +] _[ X]_ [3] _[,]_ [5][)] _[d]_ [2] _[X]_

_X_ 1 _,_ 3 _X_ 3 _,_ 5( _X_ 1 _,_ 4 _X_ 2 _,_ 5 _−_ _X_ 1 _,_ 3 _X_ 3 _,_ 5)

( _X_ 1 _,_ 3 + _X_ 2 _,_ 5) [2] ( _X_ 2 _,_ 4 _−_ _X_ 2 _,_ 5 + _X_ 3 _,_ 5) _d_ [2] _X_
Ω( _ACD_ ) =
_X_ 2 _,_ 5( _−X_ 1 _,_ 4 _X_ 2 _,_ 5 _−_ _X_ 1 _,_ 3 _X_ 2 _,_ 4 + _X_ 1 _,_ 3 _X_ 2 _,_ 5)( _X_ 1 _,_ 4 _X_ 2 _,_ 5 _−_ _X_ 1 _,_ 3 _X_ 3 _,_ 5)

Ω( _ADE_ ) = [(] _[X]_ [1] _[,]_ [3] _[ −]_ _[X]_ [1] _[,]_ [4][ +] _[ X]_ [2] _[,]_ [4][)(] _[−][X]_ [2] _[,]_ [4][ +] _[ X]_ [1] _[,]_ [4][ +] _[ X]_ [2] _[,]_ [5][)] _[d]_ [2] _[X]_

_X_ 1 _,_ 4 _X_ 2 _,_ 4( _−X_ 1 _,_ 4 _X_ 2 _,_ 5 _−_ _X_ 1 _,_ 3 _X_ 2 _,_ 4 + _X_ 1 _,_ 3 _X_ 2 _,_ 5)


Ω( _An_ =5) = Ω( _ABC_ ) + Ω( _ACD_ ) + Ω( _ADE_ )


where again we have rewritten the non-adjacent constants _cij_ in terms of planar variables
via Eq. (3.5). The sum of these three quantities determines the amplitude. This expansion
is fundamentally different in character from the Feynman diagram expansion due to the
appearance of (non-linear) spurious poles that occur in the presence of spurious boundaries
_AC_ and _AD_ .
This approach can be extended to all _n_ provided that a triangulation is known. Two
important properties of the bi-adjoint amplitude, which are obscured by individual Feynman
diagrams, become manifest in this triangulation. First, unlike that for each Feynman
diagram, the form for each piece of the triangulation is projective, which means it only
depends on the ratio of _X_ variables. Moreover, geometrically it is obvious that the vanishing


                   - 32                   

“soft” limit also works term-by-term, which is certainly not the case for each Feynman
diagram.


**5.5** **Recursion** **Relations** **for** **Bi-adjoint** _φ_ [3] **Amplitudes**


We propose a simple recursion relation for computing the amplitude Ω( _An_ ) as a form.
Our derivation applies the recursion relations from Appendix A.6 and the factorization
properties from Section 4.1. The result is reminiscent of _BCFW_ _triangulation_ for the amplituhedron [12, 25]. While it is not obvious from the field theory point of view, the recursion
follows naturally from the geometric picture.
We begin by picking a kinematic basis


_Y_ = (1 _, Xi_ 1 _,j_ 1 _, . . ., Xin−_ 3 _,jn−_ 3) (5.14)


For simplicity let _Z∗_ = (1 _,_ 0 _, . . .,_ 0) denote the reference point appearing in Eq. (A.25).
Furthermore, for any facet given by _Xi,j_ = _Wi,j_ _· Y_ = 0 corresponding to some dual vector
_Wi,j_, we let
_Xi,j_ [0] [:=] _[ W][i,j]_ _[·][ Z][∗]_ _Xi,j_ _[′]_ [:=] _[ W][i,j]_ _[·][ Y]_ _[−]_ _[W][i,j]_ _[·][ Z][∗]_ (5.15)


Equivalently, we can expand the propagator _Xi,j_ by


_Xi,j_ = _Xi,j_ [0] [+] _[ X]_ _i,j_ _[′]_ (5.16)


where _Xi,j_ [0] [is] [a] [linear] [combination] [of] [non-adjacent] [constants] [while] _[X]_ _i,j_ _[′]_ [is] [a] [linear] [combi-]
nation of the basis variables. This expansion is basis-dependent, but unique for each basis.
Furthermore, the deformation Eq. (A.25) _Y_ _→_ _Y_ [ˆ] is given by



_Y_ ˆ = _Y_ _−_ - _Wi,j_ _· Y_
_Wi,j_ _· Z∗_




_Z∗_ (5.17)







=


=




- _Xi,j_ _[′]_
_−Xi,j_ [0] _, Xi_ 1 _,j_ 1 _, . . ., Xin−_ 3 _,jn−_ 3





1 _,_




- _−Xi,j_ [0]
_Xi,j_ _[′]_



_Xi_ 1 _,j_ 1 _, . . .,_



(5.18)


(5.19)
















- _−Xi,j_ [0]
_Xi,j_ _[′]_



_Xin−_ 3 _,jn−_ 3



where in the last step we rescaled the vector by an overall factor to put it in the same form as
Eq. (5.14), which is possible since the vector is projective. This gives us the deformations
_X_ ˆ _ia,ja_ = - _−Xi,j_ [0] _[/X]_ _i,j_ _[′]_ - _Xia,jb_ for every basis variable. We caution the reader that this
deformation is only applied on the basis variables, not on all kinematic variables _Xk,l_ . The
non-adjacent constants are invariant under the deformation _c_ ˆ _kl_ = _ckl_, and the deformation
for any other kinematic variable can be obtained by expanding it in terms of basis variables
and non-adjacent constants. In particular, the deformation for _Xi,j_ vanishes:







_X_ ˆ _i,j_ = _X_ ˆ _i,j_ _[′]_ [+] _[X]_ [ˆ] _i,j_ [0] [=]




- _−Xi,j_ [0]
_Xi,j_ _[′]_



_Xi,j_ _[′]_ [+] _[ X]_ _i,j_ [0] [= 0] (5.20)




- 33 

which is expected since the deformation is a projection onto the cut.
From Eq. (A.31) we propose that the canonical form of the associahedron can be
obtained from the canonical form of each facet:


Ω( _An_ ) =             - _Di,j_ Ω( [ˆ] _Fi,j_ ) (5.21)

facet _Fi,j_


where _Fi,j_ denotes the facet along _Xi,j_ = 0, and we sum over all facets. The hat operator
denotes a pullback via the deformation _Xkl_ _→_ _X_ [ˆ] _kl_, and the _Di,j_ operator denotes the
“numerator replacement” rule (See Eq. (A.26)):





_d_ _[n][−]_ [3] _X_ (5.22)




- _Xd_ _[n][−]_ [4] _X_ - _→_




- _Xi,j_ [0]
_Xi,j_



where _X_ denotes the vector _Y_ with the initial component chopped off, and the angle brackets
denote the determinant - _Xd_ _[n][−]_ [4] _X_ - := det( _X, dX, . . ., dX_ ). Finally, recall from Section 4.1
that each _Fi,j_ factorizes into a product of lower associahedra like _Fi,j_ = _[∼]_ _AL ×AR_ . It follows
that

      -      -      Ω( _An_ ) = _Di,j_ ˆΩ( _AL_ ) _∧_ ˆΩ( _AR_ ) (5.23)


facet _Fi,j_


This provides a recursion relation for the amplitude because Ω( _AL_ ) and Ω( _AR_ ) are determined by lower point amplitudes. The existence of such a recursion for bi-adjoint amplitudes is not expected from the usual field-theory point of view, but here we have seen that
it follows directly from the geometry.
We now do an example for _n_ =5 (See Figure 17). We pick the basis _Y_ = (1 _, X_ 1 _,_ 3 _, X_ 1 _,_ 4),
and we consider the contribution from the facet _X_ 2 _,_ 5 = _c_ 13 + _c_ 14 _−_ _X_ 1 _,_ 3 which implies
_X_ 2 [0] _,_ 5 [=] _[ c]_ [13][ +] _[ c]_ [14] [and] _[X]_ 2 _[′]_ _,_ 5 [=] _[ −][X]_ [1] _[,]_ [3][.] [The] [deformations] [are] [given] [by]


_X_ ˆ1 _,_ 3 = _c_ 13 + _c_ 14 (5.24)

_X_ ˆ1 _,_ 4 = _[c]_ [13][ +] _[ c]_ [14] _X_ 1 _,_ 4 (5.25)

_X_ 1 _,_ 3

_X_ ˆ3 _,_ 5 = _−_ _[c]_ [13][ +] _[ c]_ [14] _X_ 1 _,_ 4 + _c_ 14 + _c_ 24 (5.26)

_X_ 1 _,_ 3

_X_ ˆ2 _,_ 5 = 0 (5.27)

_X_ ˆ2 _,_ 4 = _[c]_ [13][ +] _[ c]_ [14] _X_ 1 _,_ 4 _−_ _c_ 1 _,_ 4 (5.28)

_X_ 1 _,_ 3


And the required numerator replacement is given by




   - _c_ 13 + _c_ 14    _⟨XdX⟩→_ _d_ [2] _X_ (5.29)
_X_ 2 _,_ 5


     - 34     

On the cut _X_ 2 _,_ 5 = 0, the associahedron factorizes into the product _AL × AR_ given by


_AL_ = _A_ (2 _,_ 3 _,_ 4 _,_ _I_ [¯] ) (5.30)

_AR_ = _A_ (1 _, I,_ [¯] 5) (5.31)


where _I_ is the intermediate particle. See the discussion around Eq. (4.2) for more details.
Recalling the 4- and 3-point amplitudes, we have


Ω( _AL_ ) = _d_ log _X_ 2 _,_ 4 _−_ _d_ log _X_ 3 _,_ 5 (5.32)

Ω( _AR_ ) = 1 (5.33)


Then the pullback Ω( [ˆ] _AL_ ) _∧_ Ω( [ˆ] _AR_ ) gives


_d_ log _X_ [ˆ] 2 _,_ 4 _−_ _d_ log _X_ [ˆ] 3 _,_ 5 (5.34)

( _c_ 13 + _c_ 14) _c_ 24 _⟨XdX⟩_
=
( _c_ 14 _X_ 1 _,_ 3 _−_ _c_ 13 _X_ 1 _,_ 4 _−_ _c_ 14 _X_ 1 _,_ 4)( _c_ 14 _X_ 1 _,_ 3 + _c_ 24 _X_ 1 _,_ 3 _−_ _c_ 13 _X_ 1 _,_ 4 _−_ _c_ 14 _X_ 1 _,_ 4)


Applying the numerator replacement Eq. (5.29) and rewriting the non-adjacent variables
in terms of planar variables via Eq. (3.5) gives


( _X_ 1 _,_ 3 + _X_ 2 _,_ 5) [2] ( _X_ 2 _,_ 4 _−_ _X_ 2 _,_ 5 + _X_ 3 _,_ 5) _d_ [2] _X_
(5.35)
_X_ 2 _,_ 5( _−X_ 1 _,_ 4 _X_ 2 _,_ 5 _−_ _X_ 1 _,_ 3 _X_ 2 _,_ 4 + _X_ 1 _,_ 3 _X_ 2 _,_ 5)( _X_ 1 _,_ 4 _X_ 2 _,_ 5 _−_ _X_ 1 _,_ 3 _X_ 3 _,_ 5)


But this is precisely the Ω( _ACD_ ) term appearing in Eq. (5.12), which is the canonical form
of the triangle _ACD_ in Figure 17. This confirms the discussion in Appendix A.6 where we
expected to find the canonical form of the triangle given by the convex hull of _Z∗_ = _A_ and
the facet _CD_, which is precisely _ACD_ .
Similarly, the contribution from _X_ 3 _,_ 5 and _X_ 2 _,_ 4 give Ω( _ABC_ ) and Ω( _ADE_ ), respectively.
The contributions from the remaining cuts _X_ 1 _,_ 3 and _X_ 1 _,_ 4 vanish because they intersect the
reference point _Z∗_ and hence the geometry is degenerate. It follows that the recursion
provides a triangulation of the associahedron with reference point _Z∗_ = (1 _,_ 0 _,_ 0) identical
to Eq. (5.12).
More generally, given a choice of basis and reference point _Z∗_, the recursion gives
a triangulation of the associahedron with a reference point. Again, we emphasize that
this “BCFW-like” representation of bi-adjoint amplitudes is very different from Feynman
diagrams, and it is not obvious how to derive it from a field-theory argument.


**6** **The** **Worldsheet** **Associahedron**


We have seen that scattering amplitudes are better thought of as differential forms on
the space of kinematic variables that pullback to the canonical forms of associahedra in
kinematic space. This is a deeply satisfying connection. After all, the associahedron is
perhaps the most fundamental and primitive object whose boundary structure embodies
“factorization” as a combinatorial and geometric property.


                   - 35                   

Furthermore, string theorists have long known of the fundamental role of the associahedron for the open string. After all, the boundary structure of the open string moduli
space—the moduli space of _n_ ordered points on the boundary of a disk—also famously
“factorizes” in the same way. In fact, it is well-known that the Deligne-Mumford compactification [3, 26] of this space has precisely the same boundary structure as the associahedron.
The implications of this “worldsheet associahedron” for aspects of stringy physics have also
been explored in _e.g._ [27, 28].
Moreover, from general considerations of positive geometries we know that there should
also be a “worldsheet canonical form” associated with this worldsheet associahedron, which
turns out to be the famous “worldsheet Parke-Taylor form” [29] (for related discussions see
_e.g._ [28, 30]), an object whose importance has been highlighted in Nair’s observation [31]
and Witten’s twistor string [4], and especially in the story of scattering equations and the
CHY formulas for scattering amplitudes [5, 6, 15, 32].
But how is the worldsheet associahedron related to the kinematic associahedron? This
simple question has a striking answer: The scattering equations act as a _diffeomorphism_
from the worldsheet associahedron to the kinematic associahedron! From general grounds,
it follows that the kinematic scattering form is the pushforward of the worldsheet ParkeTaylor form under the scattering equation map. This gives a beautiful raison d’etre to the
scattering equations, and a quick geometric derivation of the bi-adjoint CHY formulas. We
now explain these ideas in more detail.


**6.1** **Associahedron** **from** **the** **Open** **String** **Moduli** **Space**


Recall that the moduli space of genus zero _M_ 0 _,n_ is the space of configurations of _n_ distinct
punctures on the Riemann sphere CP [1] modulo SL(2 _,_ C). The real part _M_ 0 _,n_ (R) is the
_open-string_ _moduli_ _space_ consisting of all distinct points _σi_ ( _i_ = 1 _, . . ., n_ ) on the real line
(and infinity) modulo SL(2 _,_ R). While there are _n_ ! ways of ordering the _σi_ variables, any
pair of orderings related by dihedral transformation are SL(2 _,_ R) equivalent. It follows that
the real part is tiled by ( _n−_ 1)! _/_ 2 distinct regions given by inequivalent orderings of the _σi_
variables [26]. The region given by the standard ordering is called the _positive_ _part_ of the
open string moduli space or more simply the _positive_ _moduli_ _space_


_M_ [+] 0 _,n_ [:=] _[ {][σ]_ [1] _[< σ]_ [2] _[<][ · · ·][ < σ][n][}][/]_ [SL(2] _[,]_ [ R][)] (6.1)


where the SL(2 _,_ R) redundancy can be “gauge fixed” in the standard way by setting fixing
three variables ( _σ_ 1 _, σn−_ 1 _, σn_ ) = (0 _,_ 1 _, ∞_ ) in which case _M_ [+] 0 _,n_ [=] _[ {]_ [0] _[ < σ]_ [2] _[<][ · · ·][ < σ][n][−]_ [2] _[<]_ [ 1] _[}]_ [.]
Sometimes we also denote the space by _M_ [+] 0 _,n_ [(1] _[,]_ [ 2] _[, . . ., n]_ [)] [to] [emphasize] [the] [ordering.] [Fur-]
thermore, recall that _M_ [+] 0 _,n_ [can] [also] [be] [constructed] [as] [the] [(strictly)] [positive] [Grassmannian]
G _>_ 0(2 _, n_ ) modded out by the torus action R _[n]_ _>_ 0 [.] [More] [precisely,] [we] [consider] [the] [set] [of] [all]
2 _× n_ matrices ( _C_ 1 _, . . ., Cn_ ) with positive Plücker coordinates ( _ab_ ) := det( _Ca, Cb_ ) _>_ 0 for
1 _≤_ _a < b ≤_ _n_, modded out by GL(2) action and column rescaling.
In analogy to what we did for the kinematic polytope, we make two claims for the
positive moduli space:


                   - 36                   

_σ_ 3







**Figure** **18** : A blowup of the _n_ =5 worldsheet associahedron showing all boundaries.


1. The (compactified) positive moduli space is an associahedron which we call the _world-_
_sheet_ _associahedron_ .


2. The canonical form of the worldsheet associahedron is the Parke-Taylor form,



_n_



_a_ =1



_d_ [2] _Ca_ (6.2)
( _a a_ +1)



1
_ωn_ [WS] := vol [SL(2)]



_n_



_a_ =1



_dσa_ 1
=
_σa −_ _σa_ +1 vol [SL(2) _×_ GL(1) _[n]_ ]



where in the last expression we rewrote the form in Plücker coordinates.


More precisely, the process of compactification provides the positive moduli space _M_ [+] 0 _,n_
with boundaries of all codimensions, and here we present a natural compactification called
the _u-space_ _compactification_ that produces the boundary structure of the associahedron.
Of course, the associahedron structure of the positive moduli space is well-known [3, 26],
but the discussion we present here is instructive for later sections.
The compactification is very subtle in _σi_ variables because our naive gauge choice fails
to make all boundaries manifest. Nonetheless, all the boundaries can be visualized via a
“blowup” procedure. Consider the case _n_ =5 where only three of the five boundaries are
manifest in the standard gauge as shown in Figure 18. The two “hidden” boundaries can
be recovered by introducing a blowup at the vertices ( _σ_ 2 _, σ_ 3) = (0 _,_ 0) and (1 _,_ 1) as shown
in Figure 18. A similar procedure applies for all _n_ . We will come back to this picture when
we discuss the canonical form, but now we provide an explicit compactification that makes
manifest all the boundaries.
We introduce the variables _ui,j_ for 1 _≤_ _i_ _<_ _j−_ 1 _<_ _n_ which are constrained to the
region 0 _≤_ _ui,j_ _≤_ 1. The _ui,j_ is analogous to the planar kinematic variable _Xi,j_ introduced
in Eq. (2.6), and can therefore be visualized as the diagonal ( _i, j_ ) of a convex _n_ -gon with
cyclically ordered labels like Figure 5 (left). There are of course _n_ ( _n−_ 3) _/_ 2 of these variables.
Furthermore, we impose the _non-crossing_ _identity_


        _ui,j_ = 1 _−_ _uk,l_ (6.3)


( _k,l_ ) _∈_ ( _i,j_ ) _[c]_


for each diagonal ( _i, j_ ), where ( _i, j_ ) _[c]_ denotes the set of all diagonals that cross ( _i, j_ ). Only
( _n−_ 2)( _n−_ 3) _/_ 2 of these _n_ ( _n−_ 3) _/_ 2 constraints are independent, so the space is of dimension
( _n−_ 3).


                   - 37                   

Let us consider some examples. For _n_ =4 we have two variables with one constraint


_u_ 1 _,_ 3 = 1 _−_ _u_ 2 _,_ 4 (6.4)


For _n_ =5 we have five variables satisfying the constraint


_u_ 1 _,_ 3 = 1 _−_ _u_ 2 _,_ 4 _u_ 2 _,_ 5 _,_ (6.5)


and four others related by cyclic shift; but only three constraints are independent, thus giving a 2-dimensional surface shown in Figure 19. For _n_ =6, there are two types of constraints
corresponding to two types of diagonals of the hexagon. Here we present the constraints
for the diagonals (1 _,_ 3) and (1 _,_ 4), and the rest are related via cyclic shift.


_u_ 1 _,_ 3 = 1 _−_ _u_ 2 _,_ 4 _u_ 2 _,_ 5 _u_ 2 _,_ 6 _u_ 1 _,_ 4 = 1 _−_ _u_ 2 _,_ 5 _u_ 2 _,_ 6 _u_ 3 _,_ 5 _u_ 3 _,_ 6 _,_ (6.6)


This gives 6 + 3 = 9 constraints, but only six are independent.
The _u_ -space provides an explicit compactification of the positive moduli space. To see
this, we begin by constructing a map from the positive moduli space _M_ [+] 0 _,n_ [to] [the] [interior]
of _u_ -space via the following cross ratio formula:



_ui,j_ = [(] _[σ][i][ −]_ _[σ][j][−]_ [1][)(] _[σ][i][−]_ [1] _[ −]_ _[σ][j]_ [)]



(6.7)
( _i j_ )( _i−_ 1 _j−_ 1)




[(] _[σ][i][ −]_ _[σ][j][−]_ [1][)(] _[σ][i][−]_ [1] _[ −]_ _[σ][j]_ [)] [(] _[i j][−]_ [1)(] _[i][−]_ [1] _[ j]_ [)]

( _σi −_ _σj_ )( _σi−_ 1 _−_ _σj−_ 1) [=] ( _i j_ )( _i−_ 1 _j−_ 1)



which has already been studied extensively in the original dual resonance model ( _c.f._ [33]
and more recently in [34]). The map provides a diffeomorphism between the positive moduli
space and the _u_ -space interior. Taking the closure in _u_ -space thereby provides the required
~~+~~
compactification. Henceforth we denote _u_ -space by _M_ 0 _,n_ [.]

~~+~~
We now argue that the compactification _M_ 0 _,n_ [is] [an] [associahedron.] [We] [begin] [by] [show-]
ing that there are exactly _n_ ( _n−_ 3) _/_ 2 codimension 1 boundaries given individually by _ui,j_ = 0
for every diagonal ( _i, j_ ). We then show that every codimension 1 boundary “factors” like
Eq. (3.3), from which the desired conclusion follows.
Clearly the boundaries of the space are given by _ui,j_ = 0 or 1. However, if _ui,j_ = 1
then by the non-crossing identity Eq. (6.3) we must have _uk,l_ = 0 for at least one diagonal
( _k, l_ ) _∈_ ( _i, j_ ) _[c]_ . It therefore suffices to only consider _ui,j_ = 0. We claim that every boundary
_ui,j_ = 0 “factors” geometrically into a product of lower-dimensional worldsheets:


~~+~~ ~~+~~ ~~+~~
_∂_ ( _i,j_ ) _M_ 0 _,n_ _[∼]_ [=] _[ M]_ 0 _,nL_ _[× M]_ 0 _,nR_ (6.8)


where


~~+~~ ~~+~~
_M_ 0 _,nL_ [:=] _[M]_ 0 _,nL_ [(] _[i, . . ., j][−]_ [1] _[, I]_ [)] (6.9)

~~+~~ ~~+~~
_M_ 0 _,nR_ [:=] _[M]_ 0 _,nR_ [(1] _[, . . ., i][−]_ [1] _[, I, j, . . ., n]_ [)] (6.10)


with _I_ denoting an auxiliary label and ( _nL, nR_ ) = ( _j−i_ +1 _, n_ + _i−j_ +1). Similar to the
geometric factorization of the kinematic polytope discussed in Section 4.1, we visualize the


                   - 38                   

_u_ 1 _,_ 3



**Figure** **19** : The worldsheet associahedron for _n_ =5 presented in a coordinate chart where
all boundaries are manifest. We caution the reader that some coordinate charts do not
make manifest all the boundaries.


geometric factorization of the compactification as the diagonal ( _i, j_ ) that subdivides the
convex _n_ -gon into a “left” subpolygon and a “right” subpolygon as shown in Figure 15.
Furthermore, note that Eq. (6.8) immediately implies that the boundary is of dimension
( _n_ _−_ 4) and hence codimension 1. From the _σ_ -space point of view, the limit _ui,j_ = 0
corresponds to the usual degeneration where the _σa_ for all _a_ = _i, . . ., j−_ 1 pinch together
on the left subpolygon, and similarly the _σa_ for all _a_ = _j, . . ., n,_ 1 _, . . ., i−_ 1 pinch together
on the right subpolygon.
To derive Eq. (6.8), let _L, R_ denote the set of diagonals of the left and right subpolygons,
respectively. Then in the limit _ui,j_ = 0, we get _uk,l_ = 1 for every diagonal ( _k, l_ ) that crosses
( _i, j_ ). It follows that the constraints Eq. (6.3) split into two independent sets of constraints,
one for each subpolygon:



_up,q_

( _p,q_ ) _∈_ ( _k,l_ ) _[c]_ _∩L_



Left:


Right:









[= 1] _[ −]_      _[u][k,l]_




[= 1] _[ −]_      _[u][k,l]_













_up,q_

( _p,q_ ) _∈_ ( _k,l_ ) _[c]_ _∩R_



( _k, l_ ) _∈_ _L_
������


( _k, l_ ) _∈_ _R_
������



(6.11)







(6.12)










~~+~~ ~~+~~
These provide precisely the constraints for the left and right factors _M_ 0 _,nL_ [and] _[M]_ 0 _,nR_ [,]

~~+~~
thereby implying Eq. (6.8). We conclude therefore that the compactified space _M_ 0 _,n_ [is] [an]
associahedron. As an example, the _n_ =5 worldsheet associahedron is shown in Figure 19.
We now compute the canonical form. Since the worldsheet associahedron has the same
boundary structure as the kinematic associahedron, therefore its canonical form should take
on a similar form as Eq. (3.15). Indeed, let us work in the standard gauge ( _σ_ 1 _, σn−_ 1 _, σn_ ) =
(0 _,_ 1 _, ∞_ ) where the moduli space interior is the simplex 0 _< σ_ 2 _< σ_ 3 _< · · · < σn−_ 2 _<_ 1. We
now blow up the boundaries of the simplex to form an associahedron polytope, in the manner
discussed earlier. We assume that our blowup is small of order _ϵ_, with boundaries given
by _Bi,j_ ( _ϵ_ ; _σ_ ) _≥_ 0 corresponding to the diagonals ( _i, j_ ) of the _n_ -gon. The exact expression


                   - 39                   

for _Bi,j_ is not unique; however, since the boundary ( _i, j_ ) corresponds to the limit where
_σi, σi_ +1 _, . . ., σj−_ 1 pinch, it is thereby necessary that lim _ϵ→_ 0 _Bi,j_ ( _ϵ, σ_ ) = _σi,j−_ 1. Now, we
compute the canonical form by substituting _Xi,j_ _→_ _Bi,j_ into Eq. (3.15), then removing the
blowup by taking the limit _ϵ →_ 0:




 - ~~+~~ Ω _M_ 0 _,n_ = lim
_ϵ→_ 0





sign( _g_ )

planar _g_



_n−_ 3


_d_ log _Bia,ja_ ( _ϵ_ ; _σ_ ) (6.13)

_a_ =1




 = sign( _g_ )


planar _g_



_n−_ 3


_d_ log _σia,ja−_ 1 (6.14)

_a_ =1



where we sum over all planar cubic graphs _g_, and for every _g_ the ( _ia, ja_ ) for _a_ = 1 _, . . ., n−_ 3
are the diagonals of the corresponding triangulation. The sign( _g_ ) is defined by the sign flip
rule Eq. (2.12) as before. We caution the reader that the naive substitution _Xi,j_ _→_ _ui,j_
is incorrect; since the _ui,j_ variables are constrained by non-linear equations ( _i.e._ the noncrossing identities Eq. (6.3)), hence there is no known dual polytope with boundaries _ui,j_ _≥_ 0
whose volume takes the form Eq. (3.15).
Furthermore, since the _ϵ →_ 0 limit reduces to a simplex, the canonical form must also
reduce to the form for that simplex, which we recognize as the Parke-Taylor form Eq. (6.2):


          - ~~+~~           - _d_ _[n][−]_ [3] _σ_
Ω _M_ 0 _,n_ = _−_ _σ_ 2( _σ_ 2 _−σ_ 3) _· · ·_ ( _σn−_ 2 _−_ 1) (6.15)


While Eq. (6.13) and Eq. (6.15) look very different, their equivalence is guaranteed by the
geometric argument provided. In fact, the former can be thought of as a triangulation (with
overlapping pieces that “cancel”) of the latter.
Finally, we present Eq. (6.13) in a SL(2) invariant way:



Ω - _M_ ~~+~~ 0 _,n_ - = - sign( _g_ )


planar _g_



_n−_ 3

- _d_ log - _σia,ja−_ 1 _σ_ 1 _,n_ _σn−_ 1 _,n_

_a_ =1 _σ_ 1 _,n−_ 1 _σia,n_ _σja−_ 1 _,n_




(6.16)



**6.2** **Scattering** **Equations** **as** **a** **Diffeomorphism** **Between** **Associahedra**


We have now seen two associahedra: the kinematic associahedron _An_ in kinematic space
~~+~~
_Kn_ and the worldsheet associahedron _M_ 0 _,n_ [in moduli space] _[ M]_ [0] _[,n]_ [.] [Furthermore, recall that]
the scattering equations [5] relate points in moduli space to points in kinematic space. It is
therefore natural to expect that the same equations should relate the two associahedra. We
begin by reinterpreting the scattering equations as a map from moduli space to kinematic
space, giving the _scattering_ _equation_ _map_ . We then make the striking observation that the
scattering equation map acts as a _diffeomorphim_ between the two associahedra.


scattering equations
_M_ 0 _,n_ _−−−−−−−−−−−−→_ _Kn_ (6.17)
as a map


~~+~~ scattering equations
_M_ 0 _,n_ _−−−−−−−−−−−−→_ _An_ (6.18)
as a diffeomorphism


                   - 40                   

This has immediate consequences for amplitudes, including a novel derivation of the CHY
formula for bi-adjoint scalars and much more. But before jumping ahead, let us establish
the map.
Recall that the scattering equations [5] read



_Ei_ :=



_n_



_j_ =1; _j_ = _i_



_sij_
= 0 for _i_ = 1 _, . . ., n_ (6.19)
_σi,j_



where _σi,j_ := _σi −_ _σj_, and only ( _n−_ 3) equations are independent due to SL(2) redundancy.
It is convenient to first send _σn_ _→∞_ so that by adding all _E_ 1 _, E_ 2 _, ..., Ec_ together we find




  _sc,c_ +1 = _−_


1 _≤i≤c_
_c_ +1 _≤j≤n−_ 1
( _i,j_ )=( _c,c_ +1)



_sij_
_σc,c_ +1 _._ (6.20)
_σi,j_



for the range 1 _≤_ _c_ _≤_ _n−_ 2. Combining variables _sc,c_ +1 that have adjacent indices and
variables _sij_ that have non-adjacent indices ( _i.e._ _j−i_ _>_ 1) gives us a formula for every
planar variable _Xa,b_ :



_sij_
_σa,b−_ 1 _,_ (6.21)
_σi,j_




  _Xa,b_ = _−_


1 _≤i<a_
_a<j<b_



_sij_    _σa,j_ _−_
_σi,j_

_a≤i<b_
_b≤j<n_



_sij_     _σi,b−_ 1 _−_
_σi,j_

1 _≤i<a_
_b≤j<n_



whereby every index pair _i, j_ on the right hand side is non-adjacent with _i, j_ = _n_ . This
provides a remarkable rewriting of the scattering equations because every Mandelstam
variable on the right is a constant _sij_ = _−cij_ . Substituting the constants and recovering
the SL(2) invariance by rewriting the _σ_ variables as cross-ratios of Plücker coordinates gives



( _i n_ )( _j n_ )( _a b−_ 1)

[(6.22)]
( _i j_ )( _a n_ )( _b−_ 1 _n_ ) _[c][ij][ .]_




 _Xa,b_ =


1 _≤i<a_
_a<j<b_



( _a j_ )( _i n_ ) ( _i j_ )( _a n_ ) _[c][ij]_ [ +]

_a≤i<b−_ 1
_b≤j<n_



( _j n_ )( _i b−_ 1) ( _i j_ )( _b−_ 1 _n_ ) _[c][ij]_ [ +]

1 _≤i<a_
_b≤j<n_



Since the right hand side consists only of constants and _σ_ variables, this provides a map
_σ_ _→_ _X_ from moduli space to kinematic space (more specifically to the subspace _Hn_ when
the _σi_ variables are real), thus providing the _scattering_ _equation_ _map_ that we are after.
Let us look at the map more closely. First and foremost, every point _Xa,b_ on the
image is manifestly positive when the _σi_ variables are ordered since the constants _cij_ _>_ 0
~~+~~
are positive. It follows that Eq. (6.22) maps the worldsheet associahedron _M_ 0 _,n_ [into] [the]
kinematic associahedron _An_ .
Moreover, every boundary of the worldsheet associahedron (of any codimension) is
mapped to the corresponding boundary of the kinematic associahedron. Indeed, consider
a codimension 1 boundary _ua,b_ _→_ 0. In this limit, the variables _σa, . . ., σb−_ 1 all pinch to
a point so that _σi,j_ _→_ 0 for all _a_ _≤_ _i_ _<_ _j_ _<_ _b_ . By direct inspection of Eq. (6.22) we
find that _Xa,b_ _→_ 0 in this limit. It follows therefore that every boundary _ua,b_ = 0 of
the worldsheet associahedron is mapped to the corresponding boundary _Xa,b_ = 0 of the


                   - 41                   

= _⇒_



_X_ 1 _,_ 3







**Figure** **20** : Graphical evidence demonstrating that for _n_ =5, the interior of the worldsheet
associahedron is mapped diffeomorphically to the interior of the kinematic associahedron
by the scattering equation map. Each contour line denotes a locus where one of _σ_ 2 _, σ_ 3 is
constant.


kinematic associahedron. An extended statement holds for boundaries of all codimensions.
We say therefore that the scattering equation map preserves the associahedron boundary
structure. Furthermore, this suggests that every point on the kinematic associahedron is
reached by the map.
Finally, we make a numerical observation. For every point on the interior of the kinematic polytope, exactly one of the ( _n−_ 3)! solutions of the scattering equations lies on the
interior of the worldsheet associahedron. In other words, provided that planar propagators
_sa···b−_ 1 _>_ 0 are positive and the non-adjacent constants _sij_ _<_ 0 are negative, then there
exists exactly one real ordered solution _σ_ 1 _< · · · < σn_ . We have checked this thoroughly up
to _n_ =10 for a substantial amount of data. Note that our kinematic inequalities are different
from the ones introduced in [35] where all solutions are _real_ .
We conjecture therefore that the scattering equation map is a _diffeomorphism_ from the
worldsheet associahedron to the kinematic associahedron. For _n_ =5, the scattering equation
map is given by


_X_ 1 _,_ 3 = _[σ]_ [2] ( _c_ 13 + _σ_ 3 _c_ 14) (6.23)

_σ_ 3

1
_X_ 1 _,_ 4 = (( _σ_ 3 _−_ _σ_ 2) _c_ 24 + _σ_ 3(1 _−_ _σ_ 2) _c_ 14) (6.24)
1 _−_ _σ_ 2


In Figure 20, we present graphical evidence showing that these equations provide a diffeomorphism.
Diffeomorphisms play an important role in the theory of positive geometries and canonical forms. Recall from Appendix A.3 and more specifically Eq. (A.7) that provided a diffeomorphism _φ_ : _A_ _→B_ between two positive geometries, the map pushes the canonical


                   - 42                   

form of one to the other:


diffeomorphism _φ_
_A_ _−−−−−−−−−−→_ _B_ (6.25)


pushforward by _φ_
Ω( _A_ ) _−−−−−−−−−−−→_ Ω( _B_ ) (6.26)


Applying this to our scenario, we find that the scattering equation map pushes the canonical
form of the worldsheet associahedron to that of the kinematic associahedron.


~~+~~ scattering equations
_M_ 0 _,n_ _−−−−−−−−−−−−→_ _An_ (6.27)
as diffeomorphism


         - ~~+~~          - pushforward by
Ω _M_ 0 _,n_ _−−−−−−−−−−−−→_ Ω( _An_ ) (6.28)
scattering equations


But Eq. (6.15) and Eq. (3.20) imply


pushforward by
_ωn_ [WS] _−−−−−−−−−−−−→_ _mnd_ _[n][−]_ [3] _X_ (6.29)
scattering equations


It follows that the amplitude _mn_ can be obtained by pushing forward the Parke-Taylor form
via the scattering equations. Recalling the definition of the pushforward from Eq. (A.5),
we obtain the amplitude form by taking the Parke-Taylor form, substituting all roots of the
scattering equations and summing over all roots.


     
_ωn_ [WS] = _mnd_ _[n][−]_ [3] _X_ (6.30)

sol _. σ_


For a general ordering pair _α, β_, this generalizes to the following statement




     
_ωn_ [WS] [ _α_ ] = _m_ [ _α|β_ ] _d_ _[n][−]_ [3] _X_ (6.31)

sol _. σ_


where _ωn_ [WS] [ _α_ ] denotes the Parke-Taylor form for the ordering _α_, and the scattering equations
~~+~~
are reinterpreted as a map _M_ 0 _,n_ _→Kn_ that restricts to a diffeomorphism _M_ 0 _,n_ [[] _[α]_ []] _[→]_

~~+~~
_A_ [ _α|β_ ], where _M_ 0 _,n_ [[] _[α]_ []][ denotes the (compactified)] _[ α]_ [-ordered part of the open string moduli]
space.
We caution the reader that the pullback of the right hand side in Eq. (6.30) does _not_
produce the left hand side. Indeed, pulling back a canonical form does not necessarily
produce another canonical form. For instance, pulling back _d_ log _y_ via _y_ = _x_ [2] gives 2 _d_ log _x_,
which does not even have unit residue.
We observe that Eq. (6.31) is reminiscent of the CHY formula for the bi-adjoint scalar.
Indeed they are equivalent, as we now show. We begin by rewriting our pushforward in
delta function form:




   _mn_ = _ωn_ ( _σ_ )




- _n−_ 3

 


_δ_ ( _Xia,ja_ _−_ _φa_ ( _σ_ ))

_a_ =1







(6.32)



where the variables _Xia,ja_ form a planar basis (corresponding to the diagonals of a triangulation), and _Xia,ja_ = _φa_ ( _σ_ ) is the scattering equation map Eq. (6.22). It is necessary


                   - 43                   

that the basis variables appear with unit Jacobian in the delta functions, because _mn_ is
obtained from Ω( _An_ ) by stripping away [�] _a_ _[n]_ =1 _[−]_ [3] _[ds][I]_ _a_ [.] [In] [other] [words,] [the] [delta] [functions]
must be normalized in the basis in which _mn_ is obtained from Ω( _An_ ).
Now we claim that Eq. (6.32) is equivalent to the corresponding CHY formula:




- _′_

_δ_


_a_






 (6.33)




     _mn,_ CHY := _ωn_ [WS] [ _σ_ ]





1
 - _n_
_a_ =1 [(] _[σ][a][ −]_ _[σ][a]_ [+1][)]












 [�]


_b_ = _a_



_sab_
_σa −_ _σb_



Here we have deliberately isolated the Parke-Taylor form and grouped the other ParkeTaylor factor with the delta function. With a little bit of work, it can be shown that the
square bracket expressions in Eq. (6.33) and Eq. (6.32) are equivalent. Thus, the second
Parke-Taylor factor acts as a Jacobian factor for pushing forward onto the subspace _Hn_ .
More generally, a delta function dressed with an _α_ -ordered Parke-Taylor factor provides the
pushforward onto the subspace _H_ [ _α_ ] defined in Eq. (8.22) or equivalently _H_ [ _α|α_ ] defined
in Section 3.4. It follows that
_mn_ = _mn,_ CHY (6.34)


We have thus provided a novel derivation of the CHY formula for the bi-adjoint scalar.
This derivation is purely geometric, and does not rely on the usual arguments involving
factorization.
Finally, we make a brief comment about all ordering pairs. In Section 3.4, we obtained
the partial amplitude _m_ [ _α|β_ ] from the pullback of the planar scattering form Ω [(] _[n][−]_ [3)] [ _α_ ]
to the subspace _H_ [ _α|β_ ]. However, around Eq. (8.26) we argue that the same amplitude
can also be obtained by pulling back the same form to a different subspace _H_ [ _β_ ]. Hence,
the amplitude can be expressed as the integral of the _α_ -ordered Parke-Taylor form over
the delta function dressed with _β_ -ordered Parke-Taylor factor, which is precisely the CHY
formula. It follows that
_m_ [ _α|β_ ] = _m_ CHY[ _α|β_ ] (6.35)


for every ordering pair.


**7** **“Big** **Kinematic”** **Space** **and** **Scattering** **Forms**


So far we have considered scattering forms for amplitudes where there is some natural
notion of an ordering, and with it, an associahedron geometry where an ordering is also important. In this section, we lay the groundwork for discussing scattering forms and positive
geometries in much more general theories with no notion of ordering at all. Remarkably,
this will be associated with a new “projective” understanding of color-kinematics relations,
and as we will see in Section 8, even a geometrization of color itself!
In order to do this, we retrace our steps to the beginning, and think of kinematic space
in a more fundamental way. Most treatments of the space of independent Mandelstam
invariants simply posit that the natural variables are the _sij_ subject to the constraint

- _i_ _[s][ij]_ [=] [0][.] Already in the case where we had a natural ordering, we found that this
was not useful, and that a better set of independent variables—the planar variables _Xa,b_ 

                   - 44                   

was needed to expose the connection between physics and geometry. But why was this
important? And how can we generalize to situations where we do not have an ordering?
A key realization is that there was never anything canonical about choosing _sij_ as
co-ordinates for kinematic space—apart from being constrained, they are just a particular
random collection of momentum dot products. On the other hand, something physical
was gained by working with _Xi,j_ variables: the kinematic space is described by _physical_
_propagators_ _associated_ _with_ _cubic_ _graphs_ that directly encode all possible singularities of a
local theory.
This motivates a new way of thinking about the kinematic space where the fundamental
variables are _all_ collections of possible propagators associated with cubic graphs. Of course
as we will see this is a highly redundant set, and these objects satisfy certain relations.
Nonetheless, we find an especially simple way of characterizing this space that makes the
fundamental link between kinematics and color transparent.
We begin by constructing a higher dimensional _big_ _kinematic_ _space_ _Kn_ _[∗]_ [before] [reducing]
to the usual kinematic space _Kn_ of Mandelstam variables which we henceforth refer to
as _small_ _kinematic_ _space_ . We find that the big space is important in its own right with
connections to Jacobi relations. Furthermore, in Section 7.2, we discuss a large class of
_scattering_ _forms_ beyond the planar scattering form of Section 2.3, some of which have
polytope interpretations and some have additional symmetries like permutation invariance.


**7.1** **The** **Big** **Kinematic** **Space**


We begin by constructing the _big_ _kinematic_ _space_ _Kn_ _[∗]_ [.] [Consider] [a] [set] [of] [abstract] [variables]
_SI_ indexed by all subsets _I_ _⊂{_ 1 _,_ 2 _, . . ., n}_ subject to two conditions,


  - _SI_ = _SI_ ¯ where _I_ [¯] is the complement of _I_


  - _SI_ = 0 for _|I|_ = 0 _,_ 1 _, n−_ 1 _, n_


For example, _Kn_ _[∗]_ =4 [is] [a] [3-dimensional] [space] [spanned] [by] [the] [variables]


_{S_ 12 = _S_ 34 _,_ _S_ 13 = _S_ 24 _,_ _S_ 14 = _S_ 23 _}_ (7.1)


while _Kn_ _[∗]_ =5 [is a 10-dimensional space spanned by] _[S][ij]_ [’s,] [and] _[ K]_ _n_ _[∗]_ =6 [is a 25-dimensional space]
spanned by 15 _Sij_ ’s and 10 _Sijk_ ’s. The dimension for general _n_ is given by


dim _Kn_ _[∗]_ [= 2] _[n][−]_ [1] _[−][n][−]_ [1] (7.2)


which for _n_ _>_ 3 is higher than the dimension _n_ ( _n−_ 3) _/_ 2 of the small kinematic space
_Kn_ . Nonetheless, the latter can be recovered by imposing a _7-term_ _identity_ which we now
describe.
For every partition of _n_ particles into four subsets


_I_ 1 _⊔_ _I_ 2 _⊔_ _I_ 3 _⊔_ _I_ 4 = _{_ 1 _,_ 2 _, · · ·_ _, n}_ (7.3)


                   - 45                   

_gs_ _gt_ _gu_


**Figure** **21** : A four set partition _I_ 1 _⊔_ _I_ 2 _⊔_ _I_ 3 _⊔_ _I_ 4 of the external labels and the three corresponding channels. The three graphs _gs, gt, gu_ are identical except for a 4-point subgraph.


we impose the following identity consisting of 7 terms (See Figure 21):


_SI_ 1 _I_ 2 + _SI_ 2 _I_ 3 + _SI_ 1 _I_ 3 = _SI_ 1 + _SI_ 2 + _SI_ 3 + _SI_ 4 (7.4)


where _SIJ_ := _SI∪J_ . We can visualize this identity as a triplet of cubic graphs which are
identical except for a four point subgraph, with the propagators on the left corresponding
to the three channels of the subgraph, and the propagators on the right corresponding to
the four legs of the subgraph. See Figure 21 for an illustration. Moreover, recall that while
Eq. (7.4) is usually presented as a derived property of 4-point kinematics, here we take a
different point of view whereby the small kinematic space _Kn_ is constructed by requiring
Eq. (7.4) as an “axiomatic identity” from which the usual kinematic identities follow:




 _SI_ = _Sij_ for all _I_ ;


_i<j_ ; _i,j∈I_



_n_


_Sij_ = 0 for all _i_ (7.5)

_j_ =1; _j_ = _i_



We derive the first identity by induction on _m_ = _|I|_, which is trivial for _m_ _≤_ 2. Now
assume that the assertion has been proven for _m_ _<_ _k_, and _|I|_ = _k_ for some index set _I_ .
We first isolate two elements _a, b_ _∈_ _I_ and define _K_ := _I\{a, b}_ . Applying Eq. (7.4) to the
partition _I_ [¯] _⊔_ _K ⊔{a} ⊔{b}_ gives


_Sab_ + _SaK_ + _SbK_ = _SK_ + _SI_ ¯ (7.6)


where we used _Sa_ = _Sb_ = 0. It follows that


         _SI_ = _SI_ ¯ = _Sab_ + _SaK_ + _SbK_ _−_ _SK_ = _Sij_ (7.7)

_i<j_ ; _i,j∈I_


where for the last equality we applied the induction hypothesis to each of the four terms
on the left hand side. This completes the derivation.


                   - 46                   

For the second identity in Eq. (7.5), we apply the first identity to _I_ [¯] for _I_ := _{i}_ which
gives

     
_Sab_ = _SI_ ¯ = _SI_ = 0 (7.8)
_a<b_ ; _a,b_ = _i_


Applying the first identity again to the full index set gives


      
_Sab_ = 0 (7.9)

_a<b_


Subtracting Eq. (7.8) from Eq. (7.9) gives the desired result.
It follows therefore that the 7-term identity reduces the big kinematic space _Kn_ _[∗]_ [to]
the small kinematic space _Kn_, in which case the abstract variables can be identified with
Mandelstam variables:
_SI_ = _sI_ for each _I_ (7.10)


For some purposes, we find it useful to study geometries and differential forms directly in
the big kinematic space prior to imposing the 7-term identity.


**7.2** **Scattering** **Forms** **and** **Projectivity**


We introduce _scattering_ _forms_ as a generalization of the planar scattering forms from Section 2.3 to _all_ cubic graphs. We then explore the implications of _projectivity_ in this general
framework and discover _Jacobi_ _identities_ for kinematic numerators as a direct consequence.
Before defining the scattering forms, we establish the properties of cubic graphs from
the point of view of the big space. Recall that a cubic graph _g_ consists of ( _n−_ 3) Mandelstam
variables _sIa_ corresponding to the propagators of the graph. Then the corresponding big
_SIa_ variables form a mutually compatible set, whereby any pair of variables _SI_ and _SJ_ are
said to be _compatible_ if the index sets are either disjoint _I ∩_ _J_ = _∅_ or one is contained in the
other. Furthermore, we define an _ordered_ _cubic_ _graph_ as a pair ( _g|α_ ) consisting of a cubic
graph _g_ and an ordering _α_ for the external legs, assuming that _g_ is compatible with _α_ .
For every ordered cubic graph ( _g|α_ ) with propagators _SIa_, we define a _d_ log form



Ω [(] _[n][−]_ [3)] ( _g|α_ ) := sign( _g|α_ )



_n−_ 3


_d_ log _SIa_ (7.11)

_a_ =1



where sign( _g|αg_ ) _∈{±_ 1 _}_ depends not only on the ordered graph but also on the ordering of
the propagators so that swapping two propagators changes the sign. The antisymmetry of
the sign is of course compensated by the antisymmetry of the wedge product. Furthermore,
we impose relations between the sign of different ordered cubic graphs via a _sign_ _flip_ _rule_ .
Recall that two graphs _g, g_ _[′]_ with the same ordering _α_ are related by a _mutation_ if one can
be obtained from the other by an exchange of channel in a 4-point subgraph like Figure 6.
We assume that planarity in the ordering _α_ is preserved by the mutation, so that only one
mutation is possible in every 4-point subgraph of any cubic graph. Furthermore, we say
that two orderings _α, α_ _[′]_ for the same graph _g_ are related by a _vertex_ _flip_ if ( _g|α_ _[′]_ ) can be
obtained from ( _g|α_ ) by exchanging two legs of a vertex (See Figure 22). Finally, we define


                   - 47                   

5


4


3


2


1



6


7



3


2


1


5


4



6


7



**Figure** **22** : A vertex flip at the red vertex


the sign flip rule by requiring a sign change for every mutation and every vertex flip.


Mutation: sign( _g|α_ ) = _−_ sign( _g_ _[′]_ _|α_ ) (7.12)

Vertex flip: sign( _g|α_ ) = _−_ sign( _g|α_ _[′]_ ) (7.13)


For a generic pair of ordered graphs ( _g|α_ ) _,_ ( _g|β_ ) related by a sequence of sign flips, let
flip( _α, β_ ) denote the number of flips involved (modulo 2) so that


sign( _g|α_ ) = ( _−_ 1) [flip(] _[α,β]_ [)] sign( _g|β_ ) (7.14)


If we restrict _α_ to the standard ordering, then the vertex flip is irrelevant and we reduce
to the sign flip rule for the planar scattering form Eq. (2.12). More generally, we require
the sign rule under vertex flip for any quantity _Q_ ( _g|α_ ) labeled by ordered cubic graphs.
It follows that a product like _Q_ ( _g|α_ ) _Q_ _[′]_ ( _g|α_ ) of two such quantities is independent of the
ordering and can therefore be written in a condensed form _Q_ ( _g_ ) _Q_ _[′]_ ( _g_ ).
We now define the _scattering_ _form_ for _n_ particles as a rank ( _n−_ 3) form on _Kn_ _[∗]_ [of] [the]
following form

      Ω [(] _[n][−]_ [3)] [ _N_ ] = _N_ ( _g|αg_ )Ω [(] _[n][−]_ [3)] ( _g|αg_ ) (7.15)


cubic _g_


where we sum over all cubic graphs _g_, and to every cubic graph we assign an ordering _αg_
and a kinematic numerator _N_ ( _g|αg_ ) which we assume to be independent of big _S_ variables.
However, since every term is independent of the ordering _αg_, we can condense our notation
as follows:

       Ω [(] _[n][−]_ [3)] [ _N_ ] = _N_ ( _g_ )Ω [(] _[n][−]_ [3)] ( _g_ ) (7.16)


cubic _g_


Furthermore, we consider _projective_ _scattering_ _forms_, which are scattering forms that
are invariant under _local_ GL(1) _transformations_ _SI_ _→_ Λ( _S_ ) _SI_ . This imposes constraints
on the kinematic numerators which we now explain. Consider a triplet of cubic graphs
_gs, gt, gu_ like Figure 21. Under the transformation, the Λ-dependence of the scattering form
becomes







( _N_ ( _gs|I_ 1 _I_ 2 _I_ 3 _I_ 4)+ _N_ ( _gt|I_ 1 _I_ 4 _I_ 2 _I_ 3)+ _N_ ( _gu|I_ 1 _I_ 3 _I_ 4 _I_ 2)) _d_ log Λ _∧_


                 - 48                  



- _n−_ 4

 
_d_ log _SJb_

_b_ =1



+ _· · ·_ (7.17)


where the _SJb_ denote the ( _n−_ 4) propagators shared by the triplet, and the _· · ·_ denotes
similar expressions for all other triplets. Now, since the non-vanishing propagators are
independent in the big kinematic space, therefore the Λ-dependence vanishes precisely if
the coefficient of every triplet vanishes. This gives us (2 _n−_ 5)!!( _n−_ 3) _/_ 3 identities (not all
independent), one for each triplet, of the following form:


_N_ ( _gs|I_ 1 _I_ 2 _I_ 3 _I_ 4)+ _N_ ( _gt|I_ 1 _I_ 4 _I_ 2 _I_ 3)+ _N_ ( _gu|I_ 1 _I_ 3 _I_ 4 _I_ 2) = 0 (7.18)


Note that we have explicitly written out the ordering for each graph which is important for
making sure that the three terms add. We refer to Eq. (7.18) as a _Jacobi_ _identity_ due to its
similarity to the Jacobi identity for structure constants of Lie groups. It follows that the
scattering form is projective if and only if its numerators satisfy Jacobi identities.
We make a few comments before providing examples. Note that Eq. (7.18) is derived
without imposing the 7-term identity Eq. (7.4). This is crucial, as imposing the identity
would reduce us to the small kinematic space _Kn_ where the set of all propagators no longer
forms a basis (although the set of all _planar_ propagators does), in which case we cannot
require the coefficient of every triplet in Eq. (7.17) to vanish. Furthermore, the GL(1)
transformation does not act on the kinematic numerators, which may depend on usual
kinematic quantities like ( _pi_ _· pj_ ), ( _ϵi_ _· pj_ ) and ( _ϵi_ _· ϵj_ ) that we assume to be independent
of big _S_ variables. Nonetheless, we can define a similar local GL(1) transformation acting
directly on the small space via _pi_ _→_ ~~�~~ Λ( _p_ ) _pi_ . It is straightforward then to show that GL(1)
invariance in the big space directly implies GL(1) _covariance_ in the small space, meaning
Ω[ _N_ ] [(] _[n][−]_ [3)] ( _s_ ) _→_ Λ _[D/]_ [2] Ω [(] _[n][−]_ [3)] [ _N_ ]( _s_ ) where _D_ is the mass dimension of the numerators.
Let us consider some examples of projective scattering forms. The simplest case is the

_α-planar_ _scattering_ _form_




  Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [ _α_ ] = sign( _g|α_ )

_α_ -planar _g_



_n−_ 3


_d_ log _SIa_ (7.19)

_a_ =1



where we sum over all cubic graphs _g_ compatible with the ordering _α_ . For the standard
ordering this reduces to Eq. (2.10) in the small kinematic space. In this case, the kinematic
numerator _N_ ( _g|α_ ) vanishes for any graph incompatible with _α_, and is _±_ 1 otherwise. More
specifically, for every triplet, either none of the three graphs is compatible, or exactly two
are. For instance, if the first two of the triplet _gs, gt, gu_ are compatible, then


_N_ ( _gs|I_ 1 _I_ 2 _I_ 3 _I_ 4) = _±_ 1 _N_ ( _gt|I_ 1 _I_ 4 _I_ 2 _I_ 3) = _∓_ 1 _N_ ( _gu|I_ 1 _I_ 3 _I_ 4 _I_ 2) = 0 (7.20)


One way to generalize the planar scattering form without introducing any additional
structures such as spin or color is to drop the planarity requirement and consider all projective scattering forms whose numerators are 0 _, ±_ 1. This provides a large class of scattering
forms called _d_ log scattering forms of which the planar case is only one. Furthermore, as the
planar form is closely tied to the geometry of the associahedron, many of these other forms
are also closely tied to polytopes of their own such as the permutohedron. We provide more


                   - 49                   

1



2 3 4


_f_ _[a]_ [1] _[a]_ [2] _[b]_ _f_ _[ba]_ [3] _[c]_ _f_ _[ca]_ [4] _[a]_ [5]
5


_f_ _[a]_ [1] _[a]_ [2] _[b]_ _f_ _[ba]_ [3] _[c]_ _f_ _[ca]_ [4] _[a]_ [5] _↔_



1



2 3 4


_s_ 12 _s_ 45
5


d _s_ 12 _∧_ d _s_ 45



**Figure** **23** : An example of the duality between color factors and differential forms


details on this topic in the Outlook.
Furthermore, we point out that while planar forms have cyclic symmetry, it is also
possible to construct projective forms with _permutation_ _symmetry_ . As will be discussed
in the next section, such scattering forms can be obtained from _color-dressed_ _amplitudes_
that are permutation invariant, via an important connection between differential forms and
color. These include scattering forms for theories like Yang-Mills and Non-linear Sigma
Model, which we discuss in more detail in Section 9.
Last but not least, we state an important property for any projective scattering form.
Since planar scattering forms are projective, it follows that every linear combination of
them is also projective:


       Ω [(] _[n][−]_ [3)] [ _C_ ] = _C_ ( _α_ )Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [ _α_ ] (7.21)

_α∈Sn/Zn_


where the _C_ ( _α_ ) coefficients are independent of big _S_ variables. Remarkably, the converse is
also true, _i.e._ every projective scattering form is a linear combination of planar scattering
forms. We give a detailed derivation in Appendix C, and the upshot is that any projective
scattering form can be expanded in terms of a basis of ( _n−_ 2)! planar forms,


     Ω [(] _[n][−]_ [3)] [ _C_ _[′]_ ] = _C_ _[′]_ ( _π_ ) Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [1 _, π_ (2) _, . . ., π_ ( _n−_ 1) _, n_ ] _._ (7.22)

_π∈Sn−_ 2


**8** **Color** **is** **Kinematics**


In the last section we have seen a striking relationship between _projective_ _scattering_ _forms_
in the big kinematic space, and the _color-kinematics_ connection for numerator factors. But
this is just half of the story. In this section we see another related but distinct relationship
between color and kinematics. Indeed we have become accustomed to speaking of “colorkinematics duality”, but this relationship is even more basic from the scattering form point
of view so that in a precise sense, “Color is Kinematics!” Temporarily ignoring the correct
assignment of signs, the basic observation is extremely simple: any scattering form involves
a sum over cubic graphs in kinematic space, and these all have a factor that is the wedge
product of all the _ds_ ’s associated with the propagators. But quite beautifully, as a consequence of the 7-term identity Eq. (7.4), these wedge-product factors associated with any
cubic graph satisfy exactly the same Jacobi identities as the color factors associated with
the same graphs! This leads naturally to a duality between color factors and differential
forms, as suggested by Figure 23. We will see that this “Color is Kinematics” relation goes


                   - 50                   

even deeper, with the _trace_ _decomposition_ of color factors directly equivalent to _subspace_
_pullbacks_ of the form. This connection allows us to geometrize color, and makes it possible
to speak of colored theories, such as Yang-Mills theories and the Non-linear sigma model,
purely in terms of scattering forms which can be freely exchanged for explicit color factors.


**8.1** **Duality** **Between** **Color** **and** **Form**


We establish the _duality_ _between_ _color_ _factors_ _and_ _differential_ _forms_ _on_ _kinematic_ _space_ _Kn_
by showing that the latter satisfy _Jacobi_ _relations_ similar to the usual Jacobi relations for
structure constants. This leads naturally to a _duality_ _between_ _color-dressed_ _amplitudes_ _and_
_scattering_ _forms_ .
We begin by reviewing the algebra of color. Given an ordered graph we define a
color factor _C_ ( _g|α_ ) by first drawing _g_ as a planar graph whose external legs are ordered
clockwise by _α_ (See Figure 23 (left)). Then, for each internal and external line we assign
an index, and for each vertex _v_ we assign a structure constant _f_ _[a][v][b][v][c][v]_, where the indices
_av, bv, cv_ correspond to the three adjacent lines in clockwise order. Finally, we obtain the
color factor by multiplying the structure constants and contracting repeated indices (which
occur along internal lines). Hence,


        _C_ ( _g|α_ ) = _f_ _[a][v][b][v][c][v]_ (8.1)


_v_


where index contraction is implicitly assumed. The antisymmetry of the structure constants
implies the vertex flip sign rule Eq. (8.2) while the usual Jacobi identities for the structure
constants imply Jacobi identities for the color factors Eq. (8.3) for any triple like Figure 21:


_C_ ( _g|α_ ) = ( _−_ 1) [flip(] _[α,β]_ [)] _C_ ( _g|β_ ) (8.2)


_C_ ( _gs|I_ 1 _I_ 2 _I_ 3 _I_ 4)+ _C_ ( _gt|I_ 1 _I_ 4 _I_ 2 _I_ 3)+ _C_ ( _gu|I_ 1 _I_ 3 _I_ 4 _I_ 2) = 0 (8.3)


We now argue that a similar set of identities hold for differential forms on the kinematic
space _Kn_ . For every ordered graph ( _g|α_ ) with propagators _sIa_ for _a_ = 1 _, . . ., n−_ 3, we define
the ( _n−_ 3)-form



_W_ ( _g|α_ ) = sign( _g|α_ )



_n−_ 3


_dsIa_ (8.4)

_a_ =1



We claim that the form satisfies the vertex flip sign rule Eq. (8.5) and the Jacobi identity
Eq. (8.6) in perfect analogy with color factors.


_W_ ( _g|α_ ) = ( _−_ 1) [flip(] _[α][|][β]_ [)] _W_ ( _g|β_ ) (8.5)


_W_ ( _gs|I_ 1 _I_ 2 _I_ 3 _I_ 4)+ _W_ ( _gt|I_ 1 _I_ 4 _I_ 2 _I_ 3)+ _W_ ( _gu|I_ 1 _I_ 3 _I_ 4 _I_ 2) = 0 (8.6)


The former follows from the sign( _g|α_ ) factor in Eq. (8.4). The latter follows from applying
the 7-term identity Eq. (7.4) to the triplet _gs, gt, gu_ from Figure 21:


_dsI_ 1 _I_ 2 + _dsI_ 2 _I_ 3 + _dsI_ 1 _I_ 3 = _dsI_ 1 + _dsI_ 2 + _dsI_ 3 + _dsI_ 4 (8.7)


                   - 51                   

Note that on the left the propagators correspond to the three channels of the triplet, while
on the right the propagators correspond to the legs of the 4-point subgraph. Moreover, let
_sJb_ for _b_ = 1 _, . . ., n−_ 4 denote the propagators shared by the triplet. It follows that



( _dsI_ 1 _I_ 2 + _dsI_ 2 _I_ 3 + _dsI_ 1 _I_ 3) _∧_



_n−_ 4


_dsJb_ = 0 (8.8)

_b_ =1



where every term on the right hand side has vanished. In particular, external legs vanish
by on-shell condition while internal legs vanish since they already appear in the product
_∧_ _[n]_ _b_ =1 _[−]_ [4] _[ds][J]_ _b_ [.] [The] [result] [is] [precisely] [the] [sought] [after] [Jacobi] [relation.]
This implies a _duality_ _between_ _color_ _factors_ _and_ _differential_ _forms_ _on_ _kinematic_ _space_
_Kn_ :
_C_ ( _g|α_ ) _↔_ _W_ ( _g|α_ ) (8.9)


Hence “Color is Kinematics”. We emphasize that the 7-term identity is absolutely crucial
for this property to hold, thus providing one of the motivations for constructing kinematic
space _Kn_ by the 7-term identity directly.
We provide some examples for low _n_ . For _n_ =4, there are three color factors dual to
1-forms:


_Cs_ = _f_ _[a]_ [1] _[a]_ [2] _[b]_ _f_ _[ba]_ [3] _[a]_ [4] _↔_ _ds_

_Ct_ = _f_ _[a]_ [1] _[a]_ [4] _[b]_ _f_ _[ba]_ [2] _[a]_ [3] _↔_ _dt_

_Cu_ = _f_ _[a]_ [1] _[a]_ [3] _[b]_ _f_ _[ba]_ [4] _[a]_ [2] _↔_ _du_



For _n_ =5, color factors are dual to 2-forms. Here we provide one example as illustrated in
Figure 23.
Furthermore, the duality Eq. (8.9) leads naturally to a _duality_ _between_ _color-dressed_
_amplitudes_ _and_ _scattering_ _forms_ . Consider a colored-dressed amplitude **M** _n_ [ _N_ ] with kinematic numerators _N_ :

      -      - 1
**M** _n_ [ _N_ ] = _N_ ( _g|αg_ ) _C_ ( _g|αg_ ) (8.10)




- 
_N_ ( _g|αg_ ) _C_ ( _g|αg_ )

cubic _g_ _I∈g_



_I∈g_



1
(8.10)
_sI_



where we sum over all cubic graphs _g_, and _sI_ for _I_ _∈_ _g_ denote the propagators in the graph.
We now map this amplitude to a form on kinematic space by applying Eq. (8.9) to each
color factor individually, giving




  Ω [(] _[n][−]_ [3)] [ _N_ ] =




- 
_N_ ( _g|αg_ ) _W_ ( _g|αg_ )

cubic _g_ _I∈g_



_I∈g_



1
(8.11)
_sI_



which we recognize as a scattering form Eq. (7.15) with _SI_ _→_ _sI_ . Likewise, we can return
to the amplitude Eq. (8.10) by applying Eq. (8.9) backwards. Thus, the duality Eq. (8.9)
implies the duality Eq. (8.12)


**M** _n_ [ _N_ ] _↔_ Ω [(] _[n][−]_ [3)] [ _N_ ] (8.12)


                   - 52                   

We henceforth refer to both dualities as _color-form_ duality. Note that for any permutationinvariant color-dressed amplitude, Eq. (8.12) gives a scattering form that is nicely permutation invariant. Furthermore, we comment on the role of projectivity. Recall that the
numerators _N_ ( _g_ ) satisfy Jacobi relations provided that the scattering form Ω [(] _[n][−]_ [3)] [ _N_ ]( _s_ )
is derived from a projective form in the big kinematic space. The dual amplitude **M** _n_ [ _N_ ]
therefore admits an expansion with _N_ ( _g_ ) as _BCJ_ _numerators_, first proposed by Bern, Carrasco and Johansson in [18].
For the special case of bi-adjoint scalar with double color group SU( _N_ ) _×_ SU( _N_ ). The
scattering form is obtained by simply choosing _N_ ( _g_ ) = _C_ ( _g_ ) for every graph _g_ :




  Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] = _C_ ( _g|αg_ ) sign( _g|αg_ )

cubic _g_



_n−_ 3


_d_ log _sIa_ (8.13)

_a_ =1



which is both permutation invariant and projective. The corresponding double color-dressed
amplitude is given by




  **M** _φ_ 3 _,n_ =


cubic _g_



_C_ ( _g_ ) _C_ [˜] ( _g_ )
(8.14)

_I∈g_ _[s][I]_



**8.2** **Trace** **Decomposition** **as** **Pullback** **of** **Scattering** **Forms**


We explore color-form duality further by examining _partial_ _amplitudes_ and their interpretation from the differential form point of view. We find that _trace_ _decomposition_ _of_ _color-_
_dressed_ _amplitudes_ _are_ _dual_ _to_ _pullbacks_ _of_ _the_ _scattering_ _form_ to appropriate subspaces of
dimension ( _n−_ 3).
Recall that for the color groups U( _N_ ) and SU( _N_ ), the color factors can be decomposed
as traces from which partial amplitudes are obtained. More precisely, we have


     _C_ ( _g|α_ ) = ( _−_ 1) [flip(] _[α,β]_ [)] Tr( _β_ (1) _, . . ., β_ ( _n_ )) (8.15)


_β∈O_ ( _g_ ) _/Zn_


where _O_ ( _g_ ) _/Zn_ denotes all 2 _[n][−]_ [2] orderings compatible with the graph _g_ modulo cyclic transformations. In other words, out of all ( _n−_ 1)! distinct trace terms, the color factor _C_ ( _g|α_ )
is expanded precisely in terms of those traces whose ordering is compatible with the graph.
Substituting Eq. (8.15) into Eq. (8.10) for every graph _g_ gives us the trace decomposition for the amplitude:


     **M** _n_ [ _N_ ] = Tr( _β_ (1) _, . . ., β_ ( _n_ )) _Mn_ [ _N_ ; _β_ ] (8.16)


_β∈Sn/Zn_


where the _partial_ _amplitude_ _Mn_ [ _N_ ; _β_ ] is given by a sum over _β_ -planar graphs:




   _Mn_ [ _N_ ; _β_ ] =




 - 
_N_ ( _g|β_ )

_β−_ planar _g_ _I∈g_



_I∈g_



1
(8.17)
_sI_




- 53 

As an example, for _n_ =4, the color factors decompose as


_Cs_ =Tr(1234) _−_ Tr(2134) _−_ Tr(1243) + Tr(2143) (8.18)


_Ct_ =Tr(1423) _−_ Tr(4123) _−_ Tr(1432) + Tr(4132) (8.19)


_Cu_ =Tr(1342) _−_ Tr(3142) _−_ Tr(1324) + Tr(3124) (8.20)


where both the _s_ and _t_ channels contribute to the ordering _β_ = (1234), thus giving



_M_ 4[ _N_ ; 1234] = _[N]_ [(] _[s][|]_ [1234)]



(8.21)
_t_




[1234)] + _[N]_ [(] _[t][|]_ [1234)]

_s_ _t_



We now argue that the partial amplitude Eq. (8.17) can be obtained by pulling back
the scattering form Eq. (8.11) to an ( _n−_ 3)-dimensional subspace _H_ [ _β_ ] which we define by
imposing ( _n−_ 2)( _n−_ 3) _/_ 2 independent conditions:


_H_ [ _β_ ] :=      - _sβ_ ( _i_ ) _β_ ( _j_ ) is constant _|_ 1 _≤_ _i < j−_ 1 _≤_ _n−_ 2� (8.22)


This coincides with the subspace _Hn_ define in Eq. (3.5) if _β_ is the standard ordering and
the constants _sβ_ ( _i_ ) _β_ ( _j_ ) are negative. Now for any graph _g_ compatible with _β_, we define the
pullback
_dV_ [ _β_ ] := _W_ ( _g|β_ ) _|H_ [ _β_ ] (8.23)


which is independent of the graph as shown around Eq. (3.19) for the standard ordering.
More generally, for a pair of orderings _α, β_, we have



_W_ ( _g|α_ ) _|H_ [ _β_ ] =



�( _−_ 1) [flips(] _[α,β]_ [)] _dV_ [ _β_ ] if _g_ is compatible with _β_

(8.24)
0 otherwise



where the first line follows immediately from the definition Eq. (8.23), while the second line
requires a proof for which we provide a sketch. Our strategy is to argue by induction on
the number of particles, beginning with _n_ =4 which can be verified directly. For higher _n_,
suppose _g_ is a cubic graph that is compatible with _α_ but not with _β_, and for simplicity let
us assume that _β_ is the standard ordering. We observe that the graph must consist of at
least one propagator of the form _sij_ where _i < j_ and _i, j_ = _n_ . If _i, j_ are non-adjacent, then
_dsij_ = 0 on the pullback, and we are done. Otherwise, the propagator must be _si,i_ +1, giving
_W_ ( _g_ ) = _dsi,i_ +1 _∧_ _W_ _[′]_ ( _g_ ) for some form _W_ _[′]_ ( _g_ ). Since factors of _dsi,i_ +1 within _W_ _[′]_ ( _g_ ) do not
contribute, we can therefore think of _W_ _[′]_ ( _g_ ) as the form for a reduced graph _g_ _[′]_ obtained
from _g_ by collapsing particles _i_ and _i_ +1 into a single particle. But _W_ _[′]_ ( _g_ ) vanishes by
induction, thus completing the argument. One subtlety of the last step is that the particle
( _i, i_ + 1) is generically off-shell with mass-squared given by _si,i_ +1, which appears to violate
the induction hypothesis. But since factors of _dsi,i_ +1 are effectively zero, the induction still
holds. It follows that the pullback of the scattering form Ω [(] _[n][−]_ [3)] [ _N_ ] to the subspace _H_ [ _β_ ]


                   - 54                   

_π_ (2) _π_ (3) _π_ ( _n −_ 1)


1 _n_


**Figure** **24** : Multi-peripheral graph with respect to 1 and _n_ for the ordering _π_ _∈_ _Sn−_ 2


gives the partial amplitude _Mn_ [ _N_ ; _β_ ]:










 _dV_ [ _β_ ] = _Mn_ [ _N_ ; _β_ ] _dV_ [ _β_ ] (8.25)



Ω [(] _[n][−]_ [3)] [ _N_ ] _|H_ [ _β_ ] =




 




 - 
_N_ ( _g|β_ )

_β_ -planar _g_ _I∈g_



_I∈g_



1
_sI_



Applying this to the planar scattering form Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [ _α_ ] for the bi-adjoint scalar gives us
the double partial amplitude _m_ [ _α|β_ ]:


Ω _φ_ 3[ _α_ ] _|H_ [ _β_ ] = ( _−_ 1) [flip(] _[α,β]_ [)] _m_ [ _α|β_ ] _dV_ [ _β_ ] (8.26)


This is very different from Eq. (3.32) where the same amplitude was obtained by pulling back
to a different subspace _H_ [ _α|β_ ]. The advantage of the latter is that it provides a geometric
interpretation for the amplitude (form) as the canonical form of a positive geometry as
in Eq. (3.33). The former, however, can be applied to trace decompose any colored tree
amplitude.
Finally, we discuss the role of some well-known amplitude relations. Recall the decomposition a la Del Duca, Dixon and Maltoni (DDM) [36] given in Eq. (8.27), where _gπ_
denotes the multi-peripheral graph with respect to 1 and _n_ for the ordering _π_ _∈_ _Sn−_ 2 as
shown in Figure 24.


     **M** _n_ [ _N_ ] = _C_ ( _gπ|π_ ) _Mn_ [ _N_ ; 1 _, π_ (2) _, . . ., π_ ( _n−_ 1) _, n_ ] (8.27)

_π∈Sn−_ 2


It follows that the color-dressed amplitude can be expanded in terms of only ( _n−_ 2)! partial
amplitudes of the form given in Eq. (8.27), which is more efficient than the ( _n−_ 1)!-term
expansion of the standard trace decomposition. This also follows from the Kleiss-Kuijf
(KK) [37] relations. Furthermore, applying the color-form duality to Eq. (8.27) gives an
analogous identity for the scattering form


     Ω [(] _[n][−]_ [3)] [ _N_ ] = _W_ ( _gπ|π_ ) _Mn_ [ _N_ ; 1 _, π_ (2) _, . . ., π_ ( _n−_ 1) _, n_ ] (8.28)

_π∈Sn−_ 2


Note that the expansion is unique both for the color-dressed amplitude and for the form,
since the multi-peripheral graphs _gπ_ form a basis. Furthermore, we find that Bern-CarrascoJohansson (BCJ) relations [18] follow from requiring the scattering form to be projective,
as shown in Appendix C.
Last but not least, as we have discussed around Eq. (7.22), every projective form can
be expanded in a basis of ( _n−_ 1)! planar scattering forms labeled by the orderings _π_ _∈_ _Sn−_ 2,


                   - 55                   

and now we can spell out the coefficients. As shown in Appendix C, the coefficient for the
_π_ term is nothing but the kinematic numerator _N_ ( _gπ|π_ ):


     Ω [(] _[n][−]_ [3)] [ _N_ ] = _N_ ( _gπ|π_ ) Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] (1 _, π_ (2) _, · · ·_ _, π_ ( _n−_ 1) _, n_ ) _._ (8.29)

_π∈Sn−_ 2


Note that Eq. (8.28) and Eq. (8.29) are complementary to each other. By the color-form
duality, the latter is equivalent to the well-known _dual-basis_ _expansion_ [38] of the colordressed amplitude:


     **M** _n_ [ _N_ ] = _N_ ( _gπ|π_ ) _Mn_ _[φ]_ [3][[1] _[, π]_ [(2)] _[, . . ., π]_ [(] _[n][−]_ [1)] _[, n]_ []] (8.30)

_π∈Sn−_ 2


**9** **Scattering** **Forms** **for** **Gluons** **and** **Pions**


There are two prime examples of permutation invariant forms on kinematic space: the
scattering forms associated with the scattering of gluons in Yang-Mills theory, and of pions
in the Non-linear Sigma Model. Let us stress again the central novelty of this claim: there is
a differential form on the kinematic space, with coefficients that depend on either momenta
and polarization vectors (for Yang-Mills) or Mandelstam variables (for the NLSM), which
are fully permutation invariant with no _f_ _[abc]_ factors anywhere in sight. Nonetheless, the
geometrization of color discussed in the previous sections tells us that these forms contain
all the information about color-dressed amplitudes.
In fact more is true: the scattering forms for gluons and pions are remarkably rigid
objects. For gluons, we find that there is a _unique_ differential form with the usual minimal
power-counting in momenta that is both gauge invariant and projectively invariant. In
particular, the permutation invariance need not be stipulated but is derived. Similarly, the
form for pions is the unique form where the requirement of gauge invariance for each leg
is replaced with that of the Adler zero in the soft limit. Such “uniqueness theorems” have
recently been established in [20], for partial amplitudes from which the uniqueness of the
full scattering form follows, provided the crucial extra requirement of projectivity. We also
show that these forms have a natural pushforward origin from the worldsheet.


**9.1** **Gauge** **Invariance,** **Adler** **Zero,** **and** **Uniqueness** **of** **YM** **and** **NLSM** **Forms**


We establish general conditions under which scattering forms for gluons and (two-derivativecouple, massless) pions are unique. Consider general scattering forms Ω [(] gluon _[n][−]_ [3)] [and][ Ω] pion [(] _[n][−]_ [3)] for
pure gluons and pure pions, respectively. For the gluons, we require the kinematic numerators to consist of contractions in momenta _p_ _[µ]_ _i_ [and] [polarizations] _[ϵ][µ]_ _i_ [with] [each] [polarization]
appearing exactly once; moreover we require the expected power counting, which suggests
in particular that there can be no more than ( _n−_ 2) contractions like ( _ϵi · pj_ ) in any term;
finally, we require gauge invariance ( _i.e._ invariance under the shift _ϵ_ _[µ]_ _i_ _[→]_ _[ϵ]_ _i_ _[µ]_ [+] _[ αp]_ _i_ _[µ]_ [).] [For] [the]
pions, we require the numerators to be polynomials of Mandelstam variables with the right
power counting ( _i.e._ with degree ( _n−_ 2) in Mandelstams), and the Adler zero condition ( _i.e_ .


                   - 56                   

vanishing under every soft limit _p_ _[µ]_ _i_ _[→]_ [0][).] [Finally,] [we] [assume] [that] [the] [forms] [are] [projective.]
We claim that in both cases, the scattering form is unique up to an overall constant.
To derive these two claims, we decompose the scattering forms a la DDM Eq. (8.28),
and denote the partial amplitudes for the ordering _π_ _∈_ _Sn−_ 2 as _Mn_ [gluon] ( _π_ ) and _Mn_ [pion] ( _π_ ),
respectively, which are given by Eq. (8.17) with appropriate numerators. Given the linearindependence of the _W_ ( _gπ|π_ ) factors, it is clear that each gluon partial amplitude inherits
gauge invariance from Ω [(] gluon _[n][−]_ [3)] [while] [each] [pion] [partial] [amplitude] [inherits] [Adler] [zero] [from]

Ω [(] pion _[n][−]_ [3)][.] [However,] [the] [main] [result] [of] [[][20][]] [states] [that] [any] [expression] [satisfying] [the] [assump-]

tions of _Mn_ [gluon] ( _π_ ) must be the Yang-Mills partial amplitude _Mn_ [YM] ( _π_ ) up to a constant,
and similarly any expression satisfying the assumptions of _Mn_ [pion] ( _π_ ) must be the Non-linear
Sigma Model partial amplitude _Mn_ [NLSM] ( _π_ ). Hence, there exist constants _απ, απ_ _[′]_ [for] [every]
_π_ so that
_Mn_ [gluon] ( _π_ ) = _απMn_ [YM] ( _π_ ) _Mn_ [pion] ( _π_ ) = _απ_ _[′]_ _[M]_ _n_ [NLSM] ( _π_ ) (9.1)


Finally, recall that the partial amplitudes satisfy BCJ relations due to projectivity of the
form. It follows that the constants _α_ := _απ_ are identical for all _π_ and likewise for _α_ _[′]_ := _απ_ _[′]_
so that the scattering forms are unique up to a constant:


Ω [(] gluon _[n][−]_ [3)] [=] _[ α]_ [Ω][(] YM _[n][−]_ [3)] Ω [(] pion _[n][−]_ [3)] = _α_ _[′]_ Ω [(] NLSM _[n][−]_ [3)] (9.2)


Note that projectivity plays a crucial role without which we could have put arbitrary
constants on the right hand side of Eq. (8.28), thus leading to a ( _n−_ 2)!-parameter family
of solutions. Furthermore, permutation symmetry, unitarity and factorization all emerge as
natural consequences of gauge invariance/Adler’s zero and projectivity (and some technical
constraints on the numerators), even though none was assumed.
For all _n_, these forms can be obtained from the color-dressed amplitude by directly
applying the relation Eq. (8.9), thus establishing their existence. Here we give explicit
examples for _n_ =4. The NLSM form reads:




       - _s_
Ω [(1)] NLSM [=] _[ s t d]_ [ log]
_t_




= _t d s −_ _s d t_ (9.3)



which also equals ( _u dt −_ _t du_ ) = ( _s du −_ _u ds_ ) and is thus permutation invariant up to a
sign. We can express the YM form as a combination of two _φ_ [3] forms:




      - _s_
Ω [(1)] YM [=] _[ N][s][ d]_ [ log]
_t_




- - _u_
+ _Nu d_ log
_t_




(9.4)



where _Ns, Nu_ are BCJ numerators for the _s_ and _u_ channels (see _e.g._ [39]).


**9.2** **YM** **and** **NLSM** **from** **the** **Worldsheet**


We now discuss the worldsheet origin of projective scattering forms with YM and NLSM as
the primary examples. First we show that every projective scattering form Ω [(] _[n][−]_ [3)] [ _N_ ] on _Kn_
can be obtained as the pushforward of an equivalence class of forms _ωn_ [ _N_ ] on the moduli
space _M_ 0 _,n_ . In particular, the planar scattering form Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [ _α_ ] is obtained by pushing
forward the Parke-Taylor form _ωn_ [WS] [ _α_ ].


                   - 57                   

Recall that given any form _ωn_ ( _σ_ ) on moduli space, its pushforward is given by substituting and summing over all solutions of the scattering equations


       _ω_ ( _σ_ ) _→_ _ωn_ ( _σ_ ) (9.5)


sol _. σ_


Note that two forms _ωn_ and _ωn_ _[′]_ [are] [pushed] [to] [the] [same] [forward] [if] [and] [only] [if] [they] [are]
equivalent on the support of the scattering equations. We therefore “equate” moduli space
forms _ωn_ ( _σ_ ) _, ωn_ _[′]_ [(] _[σ]_ [)][ that are equivalent on the support of the scattering equations for which]




- 
_ωn_ ( _σ_ ) =

sol _. σ_ sol _. σ_




    _ωn_ ( _σ_ ) _≃_ _ωn_ _[′]_ [(] _[σ]_ [)] = _⇒_





_ωn_ _[′]_ [(] _[σ]_ [)] (9.6)

sol _. σ_



We now wish to classify all forms on moduli space that pushforward to projective
scattering forms. Recall from Appendix C that every projective form can be expanded in
a basis of ( _n−_ 2)! planar scattering forms with coefficients given by kinematic numerators
for multi-peripheral graphs:


     Ω [(] _[n][−]_ [3] [ _N_ ] = _N_ ( _gπ|π_ )Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [1 _, π_ (2) _, . . ., π_ ( _n−_ 1) _, n_ ] (9.7)

_π∈Sn−_ 2


which can obviously be obtained by pushing forward the following form on moduli space:


      _ωn_ [ _N_ ] = _N_ ( _gπ|π_ ) _ωφ_ [WS][3] [(] _[π]_ [)] (9.8)

_π∈Sn−_ 2


In this way, we can construct a worldsheet form that gives _any_ projective form as a linear
combination of Parke-Taylor forms with different orderings.
Two important worldsheet forms are the YM and NLSM forms, which are determined
by the corresponding CHY half-integrand. More precisely, we claim that



Ω [(] YM _[n][−]_ [3)] = 



- 
_dµn_ Pf _[′]_ Ψ _n_ Ω [(] NLSM _[n][−]_ [3)] [=]
sol _._ _σ_ sol _._





_dµn_ det _[′]_ _An_ (9.9)

sol _._ _σ_



where _dµn_ := _d_ _[n]_ _σ/_ vol [SL(2)] and Pf _[′]_ Ψ _n_ and det _[′]_ _An_ are the reduced Pfaffian and determinant (both permutation invariant), respectively, as defined in [6].


[Pf] _[|]_ [Ψ] _[n][|]_ _i,j_ _[i,j]_ det _|An|_ _[i,j]_ _i,j_
Pf _[′]_ Ψ _n_ := ( _−_ 1) _[i]_ [+] _[j]_ det _[′]_ _An_ := for any 1 _≤_ _i < j_ _≤_ _n_ (9.10)
_σi,j_ _σi,j_ [2]


Here Ψ _n_ ( _σ, ϵ, p_ ) is the 2 _n ×_ 2 _n_ matrix built from polarizations and momenta







Ψ _n_ :=




_A_ _−C_ _[T]_


_C_ _B_


- 58 


(9.11)


where _Aa,b, Ba,b, Ca,b_ are _n × n_ block matrices given by:



_σaa,bb_ _a ̸_ = _b_



_pa·pb_



_ϵa·ϵb_








0 _a_ = _b_



_ϵσaa,b·ϵb_ _a ̸_ = _b_



_Aa,b_ :=


_Ca,b_ :=








 _−_ [�] _c_ = _a_ _[C][a,c]_ _a_ = _b_



_a,b_ _Ba,b_ :=

0 _a_ = _b_



(9.12)











_ϵσaa,b·pb_ _a ̸_ = _b_



_ϵa·pb_



An important property of these worldsheet forms is that, on the support of scattering
equations, Pf _[′]_ Ψ _n_ is manifestly gauge invariant [6] and det _[′]_ _An_ has the Adler zero [21]:


Pf _[′]_ Ψ _n_ ( _ϵ_ _[µ]_ _i_ _[→]_ _[ϵ]_ _i_ _[µ]_ [+] _[ αp]_ _i_ _[µ]_ [) = Pf] _[′]_ [Ψ] _[n]_ [(] _[ϵ]_ _i_ _[µ]_ [)] lim [= 0] (9.13)
_p_ _[µ]_ _i_ _[→]_ [0][ det] _[ ′][A][n]_


The uniqueness of the YM and NLSM forms under the conditions discussed above implies
that there is a unique equivalence class of worldsheet forms for each theory, which by (9.13)
must be given by Pf _[′]_ Ψ _n_ and det _[′]_ _An_, respectively. Finally, it is well known that both Pf _[′]_ Ψ _n_
and det _[′]_ _An_ can be expanded in terms of Parke-Taylor forms with coefficients given by BCJ
numerators [15], which reaffirms the result already found in Eq. (9.8). For example, the
_n_ =4 forms are

det _[′]_ _A_ 4 _dµ_ 4 = _[s]_ [2] _[dµ]_ [4] _→_ _s t_     - _ωφ_ [WS][3] [(1234) +] _[ ω]_ _φ_ [WS][3] [(1324)]     - = _s t ωφ_ [WS][3] [(1423)]

_σ_ 12 [2] _[σ]_ 34 [2]

Pf _[′]_ Ψ4 _dµ_ 4 _→_ _Ns_ _ωφ_ [WS][3] [(1234)] _[ −]_ _[N][u]_ _[ω]_ _φ_ [WS][3] [(1324)]


**9.3** **Extended** **Positive** **Geometry** **for** **Gluons** **and** **Pions?**


It is clear that the gluon and pion scattering forms are fundamental objects, with a canonical
purpose in life directly in kinematic space as well as on the worldsheet. What we are still
missing is the complete connection of these scattering forms with positive geometries. The
obstacle is the most obvious one: while the forms are dictated by god-given properties of
gauge-invariance/Adler zero and projective invariance, they are not _canonical_ _forms_ which
must have not only logarithmic singularities but also unit leading residues. This may be
taken as an invitation to _e.g._ further “geometrize” the polarization vectors—something we
have already seen as a critical part of the amplituhedron story in four dimensions—or there
may be other ways to more naturally tie the “prefactors” in both YM and the NLSM to
the underlying (associahedron) geometry universally associated with the poles of (planar)
cubic graphs.


**10** **Summary** **and** **Outlook**


Let us quickly recap the main ideas we have discussed in this paper.


  - Scattering amplitudes are better thought of as “scattering forms”—differential forms
on kinematic space.


                   - 59                   

  - The kinematic associahedron is the analog of the amplituhedron for bi-adjoint _φ_ [3]

theory at tree level, and the tree amplitude is the canonical form of this associahedron.


  - The associahedron geometry makes manifest properties of bi-adjoint _φ_ [3] amplitudes
such as factorization and “soft” limit. It also provides new representations of the
amplitudes from triangulations of the geometry, with the Feynman diagram expansion
being one particular triangulation.


  - The tree-level open string moduli space is an associahedron, and scattering equations provide a diffeomorphism between the worldsheet and kinematic associahedra.
Furthermore, the pushforward of the Parke-Taylor form—the canonical form of the
worldsheet associahedron—gives the tree scattering form for the bi-adjoint scalar theory.


  - “Color is Kinematics”: the differential forms for cubic graphs satisfy Jacobi relations
identical to color factors, thus a color-dressed amplitude is dual to a scattering form
and partial amplitudes are obtained as pullbacks of the form to appropriate subspaces.


  - It is natural to study scattering forms in the big kinematic space, and for a form
to be projectively well defined, kinematic numerators must satisfy the same Jacobi
identities as color factors.


  - Two primary examples are the scattering forms for Yang-Mills and the Non-Linear
Sigma Model. These forms are uniquely fixed by standard power-counting, gauge
invariance/Adler zero conditions, and projectivity.


There are many obvious unanswered questions and open avenues of investigation suggested by our results. For instance: Is there a complete geometrization of scattering forms
for YM and the NLSM that brings the polarization vectors into the geometry? This question is of course also relevant to the search for geometries connected to gravity amplitudes.
While we do not have any natural scattering forms due to the absence of color, the amplitudes can be obtained using the double-copy construction a la BCJ [18, 19]. More precisely,
for a double copy of the form _L⊗R_ between theories _L_ and _R_, the amplitude for the product
theory can be obtained directly from either Ω [(] _L_ _[n][−]_ [3)] for the _L_ theory or Ω [(] _R_ _[n][−]_ [3)] for the _R_
theory by replacing the wedge products _W_ ( _g_ ) with appropriate kinematic numerators:




  **M** _[L]_ _n_ _[⊗][R]_ =

cubic _g_



_NL_ ( _g_ ) _NR_ ( _g_ )

 - = Ω [(] _L_ _[n][−]_ [3)] _|W_ ( _g_ ) _→NR_ ( _g_ ) = Ω [(] _R_ _[n][−]_ [3)] _|W_ ( _g_ ) _→NL_ ( _g_ ) _,_ (10.1)
_I∈g_ _[s][I]_



For example, we obtain gravity from the product YM _⊗_ YM, Born-Infeld theory from the
product YM _⊗_ NLSM and the so-called special Galileon theory from NLSM _⊗_ NLSM [21].
Along this line, it is very tempting to connect our worldsheet picture for the open string
to the ambitwistor string [8, 40–42], and related worldsheet methods using scattering equations [43, 44] which are exclusively for the closed string. Furthermore, could we understand
the double-copy construction, and possible geometries for gravity amplitudes in a way simi

                   - 60                   

lar to the Kawai-Lewellen-Tye relations connecting open- and closed-string amplitudes [45]
(See [46, 47] for related ideas)?
We have seen the YM scattering form as pushforward of the Pfaffian form on the
worldsheet, which is unique gauge invariant under the assumptions provided. What is even
more remarkable is that the full-fledged _open_ _string_ _amplitude_ can be obtained by directly
integrating the Pfaffian on the worldsheet associahedron (with Koba-Nielsen factor [33] as
a natural regulator for logarithmic divergences)! While this can be shown by string theory
calculation ( _c.f._ [34]), there must be deep conceptual reasons why the gauge-invariant
object for gluon scattering in YM theory completely dictates the infinite series of higherdimensional corrections from superstrings! It would be highly desirable to understand this
fact better and to see in general how integrals and pushforwards of worldsheet forms are
related to each other [29].
Let us end with a few suggestions for immediate avenues of progress which are more
continuously connected to the themes introduced in this paper.


**General** _d_ log **Projective** **Forms:** **Permutohedra** **and** **Beyond** Recall that a scattering form Eq. (10.2) is called _d_ log _scattering_ _form_ if it is projective and every kinematic
numerator is either 0 or _±_ 1. A classification of all such forms is then equivalent to solving
the Jacobi relations (7.18) provided _N_ ( _g|αg_ ) _∈{_ 0 _, ±_ 1 _}_ .


      Ω [(] _d_ _[n]_ log _[−]_ [3)][(] _[S]_ [) =] _N_ ( _g_ ) Ω [(] _[n][−]_ [3)] ( _g_ )( _S_ ) (10.2)

cubic _g_


While we do not have a complete classification, we can discuss some general properties.
To every _d_ log scattering form, we assign a connected graph Υ consisting of a vertex for
every cubic graph _g_ whose numerator _N_ ( _g_ ) is non-zero, with a line between any two vertices related by mutation. Furthermore, projectivity is satisfied precisely if every vertex is
adjacent to exactly ( _n−_ 3) lines ( _i.e._ the graph is “simple”), and a sign flip occurs between
any two vertices related by mutation. In particular, walking along any closed path in the
graph Υ should return us back to the same sign. Note that this does not imply that the
path must be of even length, since the sign at the initial vertex depends on its propagators
which may have been reordered by the sequence of mutations.
The simplest example of of _d_ log scattering forms is of course the planar scattering form
Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [ _α_ ] whose connected graph Υ is given by the skeleton of the _α_ -ordered associahedron,
also known as the Tamari lattice [48]. In fact, for every _n_, the Tamari lattice provides the
smallest number of vertices possible. However, the Tamari lattice is only the beginning of
a large class of examples. For _n_ =4, there is only one possible topology for the graph ( _i.e._ a
line segment). For _n_ =5, we have seen possible topologies are pentagon, hexagon, octagon
and nonagon.
For all _n_, a large class of possible connected graphs are given by the skeleton of the
“Cayley polytopes” discussed in [49] whose _d_ log scattering forms were obtained by pushing
forward Cayley functions (expressed as a form on moduli space) via the scattering equations.
The Cayley polytopes are polytopes constructed directly in kinematic space, of which the


                   - 61                   

kinematic associahedron is one example. Furthermore, much of our associahedron discussion
generalizes word-for-word to the Cayley polytopes, a summary of which is provided below.


  - The Cayley polytope (whose skeleton is the connected graph Υ) is constructed directly
in kinematic space _Kn_ by intersecting a ( _n−_ 3)-dimensional subspace with the positive
region defined by setting _sI_ _≥_ 0 for every propagator appearing in the cubic graphs.


  - The pullback of the _d_ log scattering form to the subspace gives the canonical form of
the Cayley polytope.


  - The scattering form can be obtained as the pushforward of a form on moduli space
_M_ 0 _,n_ .


Here we present the construction for one example: _permutohedron_ _Pn_ [50], which is
the Cayley polytope with largest number of vertices for any _n_, where each of the ( _n−_ 2)!
vertices corresponding to a multi-peripheral cubic graph with respect to 1 and _n_ as shown
in Figure 24.
We begin by defining the top-dimensional “positive region” where all possible poles of
the multi-peripheral graphs are positive:


_s_ 1 _a_ 1 _···am_ for _m_ = 1 _, . . ., n−_ 3 and 2 _≤_ _a_ 1 _< · · · < am_ _≤_ _n−_ 1 (10.3)


where every cut corresponds one of the (2 _[n][−]_ [2] _−_ 2) facets of the permutohedron. Furthermore,
the subspace is given by the following ( _n−_ 2)( _n−_ 3) _/_ 2 conditions:


_sij_ is a negative constant for 2 _≤_ _i < j_ _≤_ _n−_ 1 _,_ (10.4)


which are the analog of non-adjacent constants for the associahedron case. One can prove
that the intersection of the positive region with the subspace gives the permutohedron by
showing geometric factorization on all possible boundaries. Note that _Pn_ =4 is a line segment;
and _Pn_ =5 is a hexagon while _Pn_ =6 is a truncated octahedron, as shown in Figure (25).
Similar to that for associahedron, the (projective) scattering form for _Pn_ is given by




  Ω [(] _P_ _[n]_ _n_ _[−]_ [3)] = sgn( _π_ )

_π∈Sn−_ 2



_n−_ 2


_d_ log _s_ 1 _π_ (2) _···π_ ( _a_ ) (10.5)

_a_ =2



where sgn( _π_ ) is the signum of permutation _π_ . Furthermore, the pullback of the scattering
form to the subspace (denoted _Qn_ ) gives the canonical form of the permutohedron:





 _d_ _[n][−]_ [3] _s_ (10.6)



Ω [(] _P_ _[n]_ _n_ _[−]_ [3)] _|Qn_ =





 [�]

_π∈Sn−_ 2



1

- _n−_ 2
_a_ =1 _[s]_ [1] _[π]_ [(2)] _[···][π]_ [(] _[a]_ [)]



Finally, the scattering form can be obtained as a pushforward of the following form on
moduli space:

      _ωPn_ := sgn( _π_ ) _ωn_ [WS] ( _π_ ) (10.7)

_π∈Sn−_ 2


                   - 62                   

2 3 4


1 5


3 2 4


1 5



2 4 3


3 4 2


1 5



4 2 3


1 5


4 3 2


1 5



































**Figure** **25** : Permutohedra for _n_ =5 (top) and _n_ =6 (bottom)


as suggested by Eq. (9.8).
The discussion provided above can be generalized to all Cayley polytpes studied in [49].
which belong in the much larger class of _generalized_ _permutohedra_ studied by Postnikov [51,
52]. In on-going discussions with Postnikov we have learned that our construction for
these polytopes are equivalent to his under a natural change of variables. It is likely that
a corresponding _d_ log scattering form exists for generalized permutohedra. Moreover, for
recent studies of worldsheet forms that are relevant to our construction, see [53, 54].


**Massive** **Scalar** **Amplitudes,** **Non-logarithmic** **Forms** While we have ostensibly focused on amplitudes for massless particles, for the bi-adjoint _φ_ [3] theory in particular it is
clear that there is no obstruction to dealing with the scattering of massive particles. One


                   - 63                   

interesting point about doing this is the following: we know that we can generate _e.g._ _φ_ [4]

couplings from a cubic theory once massive particles are integrated out. Now, suppose we
started with a _φ_ [4] theory; there are already small subtleties on how to geometrize the scattering form in this case related to the fact that the form simply does not have logarithmic
singularities, and have singularities at infinity. The addiction to “forms with logarithmic
singularities” is perhaps the central obstacle to seeing connections to positive geometries.
But if we generate the quartic coupling by integrating out massive scalars in a cubic theory,
the full theory _does_ have logarithmic singularities, and so we can “sneak up” on the hard
problem of dealing with non-logarithmic singularities by regulating them as logarithmic
ones which are then sent to infinity. Furthermore, the scattering forms for the NLSM have
non-trivial residues on all the poles as well as poles at infinity; it would again be fascinating
to find a purely geometrical characterization of these residues.


**Loops** Furthermore, we can immediately start to explore scattering forms and possible
positive geometries associated with the loop integrand for _e.g._ the bi-adjoint scalar theory.
We can attempt to mimic the steps needed to “upgrade” the amplitude to a differential
form at loop level. An early and obvious source of annoyance is what to do about bubble
topologies, since naively including them would give double and higher poles, thus ruining
the logarithmic singularities of the form. It is perhaps reasonable to then sum over all
diagrams excluding these bubbles. At four points and one loop, this leaves us with a sum
over five _d_ log forms. Can these forms be made to be projective, and is there a positive
geometry in the extended kinematic space of loop and Mandelstam variables attached to
the loop scattering forms?
Going beyond the bi-adjoint scalar case, one can consider scattering forms for loop
integrands in gauge theories and more general theories with color. In particular, it should
be straightforward to write down forms for one-loop maximally supersymmetric Yang-Mills
amplitudes in general dimensions, since there is no contribution from bubbles. Similarly we
expect these forms for loop integrands to have a worldsheet origin that may be related to
scattering equations and ambitwistor strings at loop level [40, 55–63].


**Scattering** **Forms,** **Amplituhedron** **and** **Twistor** **Strings** **in** **Four** **Dimensions** We
have now seen _two_ notions of scattering forms. In the story of the amplituhedron the forms
play the role of combining different helicity amplitudes (as does the super-amplitude) into
a single object, while in this paper the differential forms are tied to the geometrization
of color. How are these pictures related to each other? There must be a connection,
not only for moral reasons, but for more pragmatic and technical ones. We know that
the scattering equations and the CHY formula for gluon amplitudes transition smoothly
in four-dimensional spacetime to the Roiban-Spradlin-Volovich (RSV) equations and the
twistor-string formulas for _N_ = 4 SYM scattering amplitudes [64]. The latter is deeply
connected to the geometry of the positive Grassmannian and the amplituhedron, while
we have exposed the connection of the former to the worldsheet associahedron. Making
progress on these particular questions will undoubtedly need some conceptually new ideas.
On the other hand, first steps have been taken in identifying scattering forms for
(tree-level) super-amplitudes in _N_ = 4 SYM and the “amplituhedron” in ordinary, four

                   - 64                   

dimensional momentum space; these are (2 _n−_ 4)-forms Ω [(2] _n_ _[n][−]_ [4)] encoding all helicity amplitudes in the space of _{λa,_ _λ_ [˜] _a_ _|_ _a_ = 1 _,_ 2 _, · · ·_ _, n}_ subject to momentum conservation, and the
(2 _n−_ 4)-dimensional “amplituhedron” lives in a “positive region” in the space with correct
“winding numbers” [29, 65]. In close analogy with our associahedron story, there is strong
evidence that the four-dimensional scattering equations (RSV) provide a diffeomorphism
from _G>_ 0(2 _, n_ ) (the twistor-string worldsheet) to the “amplituhedron” in momentum space;
its canonical form, or the pullback of Ω [(2] _n_ _[n][−]_ [4)] to the subspace where it lives, is then given
by the pushforward of the cyclic form of _G>_ 0(2 _, n_ ) [29, 65]. We leave the study of these
exciting questions for future investigations.


**Acknowledgments**


We would like to thank Freddy Cachazo, Nick Early, Yvonne Geyer, Peter Goddard, Steven
Karp, Thomas Lam, Alex Postnikov, Oliver Schlotterer, Hugh Thomas, Lauren Williams,
Ellis Yuan and Yong Zhang for stimulating discussions. SH would also like to thank Nima
Arkani-Hamed and the Institute for Advanced Study for their hospitality. GY would also
like to thank the Department of Physics at Tsinghua University for four great years of
undergraduate education. We would also like to thank the anonymous referee for helpful
comments. The work of NAH is supported by the DOE under grant DOE DESC0009988.
YB is supported by the Department of Physics, Princeton University and a NSERC postgraduate scholarship. SH’s research is supported in part by the Thousand Young Talents
program and the Key Research Program of Frontier Sciences of CAS.


**A** **A** **Quick** **Review** **of** **Positive** **Geometries** **and** **Canonical** **Forms**


In this section, we provide a quick review of _positive_ _geometries_ and _canonical_ _forms_, which
were introduced in [13] by two of the authors of the present paper and Thomas Lam.


**A.1** **Definitions**


Loosely speaking, a positive geometry _A_ is a _real, oriented,_ _closed geometry_ with boundaries
of all codimensions. In particular, each boundary of a positive geometry is again a positive
geometry. For instance, polytopes are positive geometries with linear boundaries. More
generally, a positive geometry can have curved boundaries defined by polynomials of higher
order. A more rigorous definition of positive geometry was introduced in [13] as a semialgebraic variety with some topological assumptions.
The crucial point is that every positive geometry has a _unique_ differential form Ω( _A_ )
defined on its ambient space called its canonical form, satisfying the following properties:


1. It is meromorphic, with simple poles precisely along the boundaries of the geometry.


2. For any hyper-surface _H_ containing a boundary _B_ of _A_, the residue along _H_ is given
by
Res _H_ Ω( _A_ ) = Ω( _B_ ) (A.1)


                   - 65                   

3. If _A_ is a point, then Ω( _A_ ) = _±_ 1 depending on the orientation.


Assuming that the ambient space does not admit any non-zero holomorphic top forms,
the canonical form is unique for each positive geometry. For this reason, the positive
geometry is usually embedded in (real) projective space P _[N]_ (R) rather than (real) Euclidean
space R _[N]_ where holomorphic top forms exist in abundance. But since R _[N]_ can be embedded
in P _[N]_ (R) via _x_ _→_ (1 _, x_ ), it is convenient to visualize projective space as Euclidean space
with a hyperplane at infinity.
One trivial property of canonical forms is that for any pair of positive geometries _A_
and _B_, we have
Ω( _A × B_ ) = Ω( _A_ ) _∧_ Ω( _B_ ) (A.2)


In addition, canonical forms have two important properties which we now discuss: _triangu-_
_lation_ and _pushforward_ .


**A.2** **Triangulations**


Given a _subdivision_ of a positive geometry _A_ by finitely many pieces _Aa_, the canonical form
satisfies
Ω( _A_ ) =               - Ω( _Aa_ ) (A.3)


_a_


We often refer to a subdivision as a _triangulation_ even if the pieces _Aa_ are not simplices.
Since the right hand side is independent of the choice of triangulation, we say that:


The canonical form is _triangulation_ _independent_ . (A.4)


The intuition behind Eq. (A.3) is that the _spurious_ _poles_ appearing on the right hand side
cancel while the _physical_ _poles_ are identical on both sides. This is not as obvious as it
may seem. Naively it is tempting to think that spurious poles cancel in pairs along the
boundary between any two adjacent pieces of the triangulation, but this is generically false
as multiple pieces may be needed to cancel a spurious pole. See Section 3 of [13] for a
careful derivation.


**A.3** **Pushforwards**


Consider a map _φ_ : _A_ _→B_ between positive geometries of the same dimension. Given a
form _ω_ on the ambient space of _A_, we can _push_ it to a form _η_ on the ambient space of _B_
via the map _φ_ :

_φ_                   _ω_ ( _a_ ) _−→_ _η_ ( _b_ ) := _ω_ ( _a_ ) (A.5)


roots _a_


where for any _b_ _∈B_ we sum over all _complex_ roots _a_ of _b_ = _φ_ ( _a_ ), where _φ_ is analytically
continued. This is called a _pushforward_, also denoted by


_φ∗_ ( _ω_ ) := _η_ (A.6)


Suppose, furthermore, that _φ_ is a _diffeomorphism_ between the interior of the two positive geometries, but possibly _finitely-many-to-one_ when analytically continued. We claim


                   - 66                   

that the map pushes the canonical form of the domain to the canonical form of the image:


_φ_
Ω( _A_ ) _−→_ Ω( _B_ ) (A.7)


We therefore say that:


The pushforward preserves canonical forms. (A.8)


This claim has been proven in certain examples where the boundary structures of _A_ and _B_
are well understood [13]. However, it remains an outstanding challenge to prove it in the
most general case. Some ideas for doing so is discussed in Section 4 of [13], which involves
a “blowup” procedure.
For computational purposes, the pushforward can be expressed in a more useful way.
Let _ai_ denote coordinates on _A_ and _bi_ coordinates on _B_ for _i_ = 1 _, . . ., D_ . Also let


_ω_ := _f_ ( _a_ ) _d_ _[D]_ _a_ _η_ := _g_ ( _b_ ) _d_ _[D]_ _b_ (A.9)


denote the top forms. Then


               _g_ ( _b_ ) = _d_ _[D]_ _af_ ( _a_ ) _δ_ _[D]_ ( _b −_ _φ_ ( _a_ )) (A.10)


where the integral sign is simply an instruction to sum over all roots on the support of the
delta function. This is the _delta_ _function_ _expression_ of the pushforward. It is important
that the _bi_ variables appear with unit Jacobian in the delta functions.
Before ending this section, we generalize the pushforward to the case where dim _B_ _≥_
dim _A_ . Consider a set of scalar equations Φ _i_ ( _a, b_ ) = 0 with _a ∈A_ and _b ∈B_ . Here Φ acts as
an _implicit_ _function_ between the positive geometries, rather than a direct map. We assume
that there are dim _A_ independent equations, and that for any _b ∈B_, there are _finitely_ many
complex roots _a ∈A_ . Now, given a form _ω_ on the ambient space of _A_, we can push it to a
form _η_ on the ambient space of _B_ via Φ:


Φ               _ω_ ( _a_ ) _−→_ _η_ ( _b_ ) := _ω_ ( _a_ ) (A.11)


roots _a_


As before, we can denote the pushforward as:


Φ _∗_ ( _ω_ ) := _η_ (A.12)


If dim _A_ = dim _B_ and Φ _i_ ( _a, b_ ) = _bi −_ _φi_ ( _a_ ), then we recover (A.8).


**A.4** **Projective** **Polytopes** **and** **Dual** **Polytopes**


We discuss the properties of _convex_ _polytopes_ _as_ _positive_ _geometries_ . While polytopes are
most easily visualized in Euclidean space R _[m]_, for the present discussion it is more convenient
to embed the polytope in projective space P _[m]_ (R) via _x_ _→_ (1 _, x_ ). Let _Y_ = (1 _, x_ ) denote
a point in projective space with components _Y_ _[A]_ indexed by _A_ = 0 _, . . ., m_ . Furthermore,


                   - 67                   

let _W_ denote points in the _dual_ _space_ with components _WA_, and we define the contraction
_Y_ _· W_ := _Y_ _[A]_ _WA_ where the repeated index _A_ is implicitly summed.
Now consider a convex polytope _A_ with vertices _Zi_ = (1 _, Zi_ _[′]_ [)][.] [Then] [the] [interior] [of] _[A]_
is given by all positive linear combinations of the vertices in projective space:







_A_ =



��

_CiZi_ _|_ _Ci_ _>_ 0

_i_



(A.13)



Note of course that the coefficients generically form a redundant representation of the
interior. Furthermore, the polytope can be cut out by linear equations of the form _Y ·Wj_ _≥_ 0
for some collection of dual vectors _Wj_ . The facets of the polytope are therefore given by
_Y_ _· Wj_ = 0.
Furthermore, we construct the _dual_ _polytope_ _A_ _[∗]_ as the convex polytope in the _dual_
_projective_ _space_ whose vertices are given by the dual vectors _Wj_ . It follows that the interior
of _A_ _[∗]_ is the set of all positive linear combinations of the dual vectors:



_A_ _[∗]_ =















(A.14)









_CjWj_ _|_ _Cj_ _>_ 0

_j_



It can be shown that _A_ _[∗]_ is precisely the set of all points _W_ cut out by the inequalities
_W_ _· Zi_ _≥_ 0, implying that the facets of the dual polytope are given by _W_ _· Zi_ = 0. This
leads us to an important fact about the duality of polytopes:


The facets of _A_ are dual to the vertices of _A_ _[∗]_, and vice versa. (A.15)


More generally, we have:


1. The codim- _d_ boundaries of _A_ correspond to the ( _d−_ 1)-boundaries of the dual _A_ _[∗]_ .


2. Any two boundaries of _A_ differing by one dimension are adjacent precisely if
their duals are adjacent.


It follows that the dual of every simple polytope is simplicial, and vice versa. Recall that a
polytope of dimension _m_ is called _simple_ if every vertex is adjacent to exactly _m_ facets (or
equivalently _m_ edges); and a polytope is called _simplicial_ if every facet is a simplex. We
leave the derivation as an exercise for the reader.
Having established the dual polytope _A_ _[∗]_, we find a direct connection to the canonical
form of the original polytope _A_ —the canonical form is determined by the volume of the
dual. For any _Y_ on the interior of _A_, we define a _Y_ -dependent measure on the dual space:


_⟨Wd_ _[m]_ _W_ _⟩_
_d_ Vol := (A.16)
( _Y_ _· W_ ) _[m]_ [+1]


where the angle brackets denote the determinant _⟨Wd_ _[m]_ _W_ _⟩_ := det ( _W, dW, . . ., dW_ ). The


                   - 68                   

( _Y_ -dependent) volume of the dual _A_ _[∗]_ is therefore


                  Vol( _A_ _[∗]_ ) := (A.17)

_W_ _∈A_ _[∗]_ _[d]_ [Vol]


Then, as shown in Section 7 of [13], the canonical form of the polytope _A_ is determined by
the volume of the dual polytope _A_ _[∗]_ :


Ω( _A_ ) = Vol( _A_ _[∗]_ ) _⟨Y d_ _[m]_ _Y ⟩_ _/m_ ! (A.18)


which we also write as
Ω( _A_ ) = Vol( _A_ _[∗]_ ) (A.19)


where Ω( _A_ ) is called the _canonical_ _rational_ _function_ and is the coefficient of the universal
factor _⟨Y d_ _[m]_ _Y ⟩_ _/m_ ! appearing in the canonical form Ω( _A_ ). For convenience, the canonical
rational function defined here is normalized differently from the one defined in the original
reference [13]. In particular, the volume of a dual simplex ∆ _[∗]_ with vertices _W_ 1 _, . . ., Wm_ +1
is given by

Vol(∆ _[∗]_ ) = _[⟨]_              - _[W]_ _mj_ =1 [1] +1 _[ · · ·]_ [(] _[Y][ W][·][m][ W]_ [+1] _[j]_ [)] _[⟩]_ (A.20)


which can be computed by integrating Eq. (A.16) over all _Y_ = _C_ 1 _W_ 1 + _· · ·_ + _CmWm_ + _Wm_ +1
parameterized by _C_ 1 _, . . ., Cm_ _>_ 0. In order for the integral to converge, it suffices to put
_Y_ inside the simplex by requiring _Y_ _· Wj_ _>_ 0 for every _j_ . The canonical form is therefore



_⟨W_ 1 _· · · Wm_ +1 _⟩_
Ω(∆) = _⟨Y d_ _[m]_ _Y ⟩_ =
_m_ ! [�] _j_ _[m]_ =1 [+1][(] _[Y]_ _[·][ W][j]_ [)]



_m_

- - _Y_ _· Wj_

_d_ log
_Y_ _· Wm_ +1
_j_ =1




(A.21)



where the equivalence of the last two expressions can be seen by applying a GL( _m_ +1)
transformation to fix the _Wj_ ’s to the identity matrix. The last expression is antisymmetric
in the _Wj_ ’s for all _j_ even though the appearance of _Wm_ +1 appears to break this symmetry.
Alternatively, the canonical form can be expressed in terms of the vertices _Z_ 1 _, . . ., Zm_ +1 of
the simplex as follows:


_⟨Z_ 1 _· · · Zm_ +1 _⟩_ _[m]_
Ω(∆) = _⟨Y d_ _[m]_ _Y ⟩_ (A.22)

              -               _m_ ! [�] _i_ _[m]_ =1 [=1] _Y Z_ 1 _· · ·_ _Z_ [ˆ] _i · · · Zm_ +1


where the hat denotes omission. This formula can be derived by substituting ( _Wj_ ) _A_ =
_ϵAA_ 1 _···AmZj_ _[A]_ +1 [1] _[Z]_ _j_ _[A]_ +2 [2] _[· · ·][ Z]_ _j_ _[A]_ + _[m]_ _m_ [into] [Eq.] [(][A.21][),] [whereby] [the] [facet] _[Y]_ _[·][ W][j]_ [=] [0] [is] [assumed] [to]
be adjacent to the vertices _Zj_ +1 _, . . ., Zj_ + _m_ . Note that the index on the vertices are labeled
modulo ( _m_ +1). More generally, the volume of a dual _polytope_ _A_ _[∗]_ can be obtained by
triangulation into simplices and summing over the volume of each simplex.
We summarize the key points as follows:


1. Every convex polytope _A_ has a _dual_ _polytope_ _A_ _[∗]_ .


2. The canonical form of the polytope Ω( _A_ ) is determined by the volume of the dual


                   - 69                   

polytope Vol( _A_ _[∗]_ ).


**A.5** **Simple** **Polytopes**


We now compute the canonical form of simple polytopes for which a simple formula exists.
Let _A_ denote a convex simple polytope of dimension _m_ . We claim that the canonical form
can be expressed as a sum over all vertices:



Ω( _A_ ) = - sign( _Z_ )


vertex _Z_



_m_


_d_ log ( _Y_ _· Wa_ ) (A.23)

_a_ =1



where for every vertex _Z_ the dual vectors _Wa_ correspond to the _m_ adjacent facets. Furthermore, the sign( _Z_ ) _∈{±_ 1 _}_ denotes the orientation of the facets _W_ 1 _, . . ., Wn−_ 3, which
of course is antisymmetric. It is important that the polytope be simple, for otherwise the
expression would be ill-defined.
We derive Eq. (A.23) by induction on dimension _m_ . For _m_ = 0, _A_ is an isolated point
and the canonical form is simply _±_ 1 depending on its orientation. Now suppose _m >_ 0, and
our claim has been proven for all dimensions less than _m_ . It suffices to argue that (A.23) has
the correct first order poles and residues, since the canonical form is uniquely defined by such
properties. Clearly, it has poles on the facets of the polytope, as required. Furthermore,
for any facet _F_ given by _Y_ _· W_ = 0, the residue of Eq. (A.23) along _Y_ _· W_ = 0 is





sign( _Z_ _[′]_ )
_Z_ _[′]_



_m−_ 1


_d_ log( _Y_ _· Wa_ ) (A.24)

_a_ =1



where we sum over all vertices _Z_ _[′]_ adjacent to the facet _F_ . But by the induction hypothesis
this is the required canonical form Ω( _F_ ), thus completing the derivation.


**A.6** **Recursion** **Relations**


We argue that the canonical form of a convex polytope _A_ of dimension _m_ can be obtained
from the canonical forms of its facets. This provides a recursion relation for the canonical
forms of polytopes. Combined with the factorization properties of the kinematic associahedron as discussed in Section 4.1, this provides recursion relations for the amplitude as
shown in Section 5.5.
However, there is an obvious difficulty. The canonical form of a facet is only defined
on the hyperplane containing that facet, while the canonical form of _A_ is defined on the
whole space. We resolve this issue by pulling back the facet canonical form via a projection
map. For each facet _F_ of _A_, let _WF_ _· Y_ = 0 denote the hyperplane containing _F_ for some
dual vector _WF_ . We pick a reference point _Z∗_ on the interior of _A_, and we establish a
deformation _Y_ _→_ _Y_ [ˆ] given by

_[·][ W][F]_ [ )]
_Y_ ˆ = _Y_ _−_ [(] _[Y]_ (A.25)

( _WF_ _· Z_ _[∗]_ ) _[Z][∗]_

which can be visualized by drawing the straight line crossing _Y_ and _Z∗_, and recognizing _Y_ [ˆ]
as the intersection between the line with the hyperplane _Y_ _·_ _W_ = 0. Hence, the deformation


                   - 70                   

projects points onto the hyperplane along the direction of the reference point. We can
therefore pullback the canonical form Ω( _F_ ) of the facet, thus giving us a form on the whole
space which we denote by Ω( [ˆ] _F_ ).
We now argue that the canonical form Ω( _A_ ) can be obtained from the Ω( [ˆ] _F_ ) forms by
employing a little “trick”, which instructs us to factor out the universal factor - _∗Y d_ _[m][−]_ [1] _Y_ 
from Ω( [ˆ] _F_ ) and replace it by a different form:


             - _∗Y d_ _[m][−]_ [1] _Y_             - _→_ [(] _[Z][∗]_ _[·][ W]_ [)] (A.26)

( _Y_ _· W_ ) _[⟨][Y d][m][Y][ ⟩]_ _[/m]_


We denote this “replacement procedure” as an operator _DW_ giving Ω( [ˆ] _F_ ) _→_ _DW_ Ω( [ˆ] _F_ ).
While this is not a differential operator, it increases the rank of the form by one.
The _DW_ operator may seem unfamiliar, but it has a simple geometric interpretation.
For any facet _F_, the _DW_ Ω( [ˆ] _F_ ) is nothing more than the canonical form of the polytope
given by the convex hull of _F_ with _Z∗_ which we denote by _A_ ( _Z∗, F_ ):


_DW_ Ω( [ˆ] _F_ ) = Ω( _A_ ( _Z∗, F_ )) (A.27)


We show this in the case where _F_ is a simplex with vertices _Z_ 1 _, . . ., Zm_ whose canonical
form (See Eq. (A.22)) is given by


_⟨XZ_ 1 _· · · Zm⟩_ _[m][−]_ [1] [�] _XY d_ _[m][−]_ [1] _Y_            Ω( _F_ ) = (A.28)

                -                 ( _m−_ 1)! [�] _a_ _[m]_ =1 _Y XZ_ 1 _· · ·_ _Z_ [ˆ] _a · · · Zm_


where the hat denotes omission and _X_ is an arbitrary vector for which _W ·_ _X_ = 0. Also, the
point _Y_ is restricted to the hyperplane where the facet lives. It can be shown that Ω( _F_ ) is
independent of _X_ . The pull back via the deformation _Y_ _→_ _Y_ [ˆ] is therefore


_⟨Z∗Z_ 1 _· · · Zm⟩_ _[m][−]_ [1] [�] _Z∗Y d_ _[m][−]_ [1] _Y_              ˆΩ( _F_ ) = (A.29)

                -                 ( _m−_ 1)! [�] _a_ _[m]_ =1 _Y Z∗Z_ 1 _· · ·_ _Z_ [ˆ] _a · · · Zm_


which is most easily obtained by setting _X_ = _Z∗_ in Eq. (A.28) and realizing that the
deformation term in _Y_ [ˆ] is absorbed in the brackets by the _Z∗_ so that _Y_ [ˆ] can be replaced by
_Y_ wherever it appears. Applying the replacement operator _DW_ then gives


_⟨Z∗Z_ 1 _· · · Zm⟩_ _[m]_ _⟨Y d_ _[m]_ _Y ⟩_
_DW_ Ω( [ˆ] _F_ ) =     -     - (A.30)

_m_ ! _⟨Y Z_ 1 _· · · Zm⟩_ [�] _[m]_ _a_ =1 _Y Z∗Z_ 1 _· · ·_ _Z_ [ˆ] _a · · · Zm_


where we have substituted _WA_ = _ϵAA_ 1 _···AmZ_ 1 _[A]_ [1] _· · · Zm_ _[A][m]_ because the hyperplane _Y_ _· W_ = 0
is spanned by the vertices _Z_ 1 _, . . ., Zm_ . But in light of Eq. (A.22), we find that Eq. (A.30)
is precisely the canonical form of _A_ ( _Z∗, F_ ) as claimed. For the more general case where _F_
is a generic polytope, we derive Eq. (A.27) by triangulating _F_ in terms of simplices and
applying the preceding argument to each simplex.


                   - 71                   

Finally, we propose that the canonical form _A_ is given by


Ω( _A_ ) =              - _DW_ Ω( [ˆ] _F_ ) (A.31)

facet _F_


which follows directly from the fact that _A_ is triangulated by the polytopes _A_ ( _Z∗, F_ ).


**B** **Vertex** **Coordinates** **of** **the** **Kinematic** **Associahedron**


We now provide a recursive algorithm for deriving the vertices of the associahedron _An_ .
Consider a vertex _Z_ 0 corresponding to a triangulation of the _n_ -gon. Our goal is to work
out all planar components _Xi,j_ of _Z_ 0 in terms of the non-adjacent constants _ckl_ . Our
strategy is to compute the components one planar basis ( _i.e._ a basis of planar variables
given by the diagonals of any triangulation) at a time by starting with the _Z_ 0 basis where
all components vanish, and applying a sequence of mutations. Since every planar basis
can be reached by such a sequence, this establishes a recursive procedure for computing all
planar components. It suffices then to discuss how the components are related by mutation.
Consider a mutation _Z_ _→_ _Z_ _[′]_ like the one shown in Figure 10 (top) where _Xi,k_ mutates to
_Xj,l_ . From Eq. (3.8) we find




    _Xj,l_ = _Xj,k_ + _Xi,l −_ _Xi,k_ +

_i≤a<j_
_k≤b<l_



_cab_ (B.1)



which computes _Xj,l_ from the basis of _Z_, thus completing the algorithm.
Here we present the vertex coordinates for the kinematic associahedron _An_ =5 from
Figure 8 (top right) in the basis _Y_ = (1 _, X_ 13 _, X_ 14):


_ZA_ = (1 _,_ 0 _,_ 0) (B.2)

_ZB_ = (1 _,_ 0 _, c_ 14 + _c_ 24) (B.3)

_ZC_ = (1 _, c_ 13 + _c_ 14 _, c_ 14 + _c_ 24) (B.4)

_ZD_ = (1 _, c_ 13 + _c_ 14 _, c_ 14) (B.5)

_ZE_ = (1 _, c_ 13 _,_ 0) (B.6)


(B.7)


**C** **BCJ** **Relations** **and** **Dual-basis** **Expansion** **from** **Projectivity**


We argue that the requirement of _projectivity_ has two important consequences for scattering
forms.


  - The partial amplitudes satisfy BCJ relations.


  - Every projective scattering form can be written as a linear combination of planar
scattering forms Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [ _α_ ] like Eq. (8.29).


                   - 72                   

We derive the first claim by directly applying a local GL(1) transformation _sI_ _→_ Λ _sI_
to the DDM form Eq. (8.28). Invariance under the transformation implies



_n−_ 2

 
_dz_ ( _π, j_ ) = 0 (C.1)

_j_ =2; _j_ = _i_





sgn( _π_ ) _Mn_ ( _π_ )
_π∈Sn−_ 2



_n−_ 2
�( _−_ 1) _[i]_ _z_ ( _π, i_ )


_i_ =2



where sgn( _π_ ) is the signum of the permutation and


_Mn_ ( _π_ ) := _Mn_ (1 _, π_ (2) _, . . ., π_ ( _n−_ 1) _, n_ ) (C.2)

_z_ ( _π, i_ ) := _s_ 1 _,π_ ( _i_ ) + _sπ_ (2) _,π_ ( _i_ ) + _· · ·_ + _sπ_ ( _i−_ 1) _,π_ ( _i_ ) (C.3)


Furthermore, we pull back to a subspace where


_{dsij_ = 0 for 1 _≤_ _i < j−_ 1 _< n−_ 1 _} ∩{dsn−_ 2 _,n−_ 1 = 0 _}_ (C.4)


We find that the only permutations _π_ that contribute are _πi_ for _k_ = 2 _, . . ., n−_ 1. For
2 _≤_ _k_ _≤_ _n−_ 2 we have


_πk_ = (1 _,_ 2 _, . . ., k−_ 1 _, n−_ 1 _, k, k_ +1 _, . . ., n−_ 2 _, n_ ) (C.5)


and for _k_ = _n−_ 1 we have _πn−_ 1 = (1 _,_ 2 _, . . ., n_ ). Moreover, for 2 _≤_ _k_ _≤_ _n−_ 2 only the _i_ = _k_
term in Eq. (C.1) contributes, giving



_dz_ ( _πk, j_ )

_j_ =2; _j_ = _k_








(C.6)





_Mn_ ( _πk_ ) _z_ ( _πk, k_ )








_n−_ 2

 
 [(] _[−]_ [1)] _[n][−]_ [1] _j_ =2; _j_



where we applied sgn( _πk_ ) = ( _−_ 1) _[n][−][k][−]_ [1] . For _k_ = _n−_ 1, however, all values of _i_ contribute
in Eq. (C.1), giving



_dz_ ( _πn−_ 1 _, j_ )

_j_ =2; _j_ = _i_








(C.7)






- []








_Mn_ ( _πn−_ 1)




_−_



_n−_ 2




_z_ ( _πn−_ 1 _, i_ )

_i_ =2



_n−_ 2

 
 [(] _[−]_ [1)] _[i][−]_ [1] _j_ =2; _j_



We leave it as an exercise for the reader to show that the expressions in curly braces
appearing in Eq. (C.6) and Eq. (C.7) are identical on the pullback. Furthermore, the
square bracket expression in Eq. (C.7) is equivalently


[ _· · ·_ ] = _z_ ( _πn−_ 1 _, n−_ 1) (C.8)


which follows from the kinematic identity [�] 1 _≤i<j≤n_ _[s][ij]_ [= 0][.] [Finally,] [combining] [the] [contri-]
butions for all _k_ gives
_n−_ 1

     
_Mn_ ( _πk_ ) _z_ ( _πk, k_ ) = 0 (C.9)

_k_ =2


                   - 73                   

Or equivalently


_n−_ 1

 
( _s_ 1 _,n−_ 1+ _s_ 2 _,n−_ 1+ _· · ·_ + _sk−_ 1 _,n−_ 1) _Mn_ (1 _, . . ., k−_ 1 _, n−_ 1 _, k, . . ., n−_ 2 _, n_ ) = 0 (C.10)

_k_ =2


which we recognize as one of the fundamental BCJ relations. By pulling back to other
subspaces, we can derive all BCJ relations. It follows that partial amplitudes of projective
scattering forms satisfy BCJ relations.
We now move on to derive the second claim. Recall that the Jacobi identities impose linear relations for the kinematic numerators, leaving a basis of ( _n−_ 2)! independent elements.
In particular, every numerator can be expanded in a basis of numerators corresponding to
all multi-peripheral graphs with respect to 1 and _n_ (See Figure 24):


_N_ ( _π_ ) := _N_ ( _gπ|_ 1 _, π_ (2) _, . . ., π_ ( _n−_ 1) _, n_ ) for _π_ _∈_ _Sn−_ 2 (C.11)


Thus, every numerator has an expansion of the form


      _N_ ( _g|αg_ ) = _M_ ( _g|αg_ ; _π_ ) _N_ ( _π_ ) (C.12)

_π∈Sn−_ 2


for some coefficients _M_ ( _g|α_ ; _π_ ) _∈{_ 0 _, ±_ 1 _}_ . By the color-kinematics duality, the color factors
must then obey the same expansion:


      _C_ ( _g|αg_ ) = _M_ ( _g|αg_ ; _π_ ) _C_ ( _π_ ) (C.13)

_π∈Sn−_ 2


where
_C_ ( _π_ ) := _C_ ( _gπ|_ 1 _, π_ (2) _, . . ., π_ ( _n−_ 1) _, n_ ) for _π_ _∈_ _Sn−_ 2 (C.14)


Substituting this into the (color-dressed) bi-adjoint scattering form Eq. (8.13) and extracting the coefficient of _C_ ( _π_ ) ( _i.e._ the only term contributing to the ordering _π_ in the standard
trace decomposition) gives the following expansion for the planar scattering form:


      Ω _φ_ [(] _[n]_ [3] _[−]_ [3)] [ _π_ ] = _M_ ( _g|αg_ ; _π_ )Ω [(] _[n][−]_ [3)] ( _g|αg_ ) (C.15)

cubic _g_


It follows that for an arbitrary (projective) scattering form, we have


     Ω [(] _[n][−]_ [3)] [ _N_ ] = _N_ ( _g|αg_ )Ω [(] _[n][−]_ [3)] ( _g|αg_ ) (C.16)


cubic _g_



= 

cubic _g_





_N_ ( _π_ ) _M_ ( _g|αg_ ; _π_ )Ω [(] _[n][−]_ [3)] ( _g|αg_ ) (C.17)
_π∈Sn−_ 2




 = _N_ ( _π_ )Ω [(] _φ_ _[n]_ [3] _[−]_ [3)] [ _π_ ] (C.18)

_π∈Sn−_ 2



which is a linear combination of planar scattering forms, as promised.


                   - 74                   

**References**


[1] M. B. Green, J. H. Schwarz, and E. Witten, _Superstring_ _Theory_ _Vol._ _1,_ _2_ . 1987.


[2] J. Polchinski, _String_ _Theory_ _Vol._ _1_ _and_ _2_ . Cambridge university press, 1998.


[3] P. Deligne and D. Mumford, “The irreducibility of the space of curves of given genus,”

_Publications_ _Mathématiques_ _de_ _l’Institut_ _des_ _[Hautes](http://dx.doi.org/10.1007/BF02684599)_ _Études_ _Scientifiques_ **36** no. 1, (Jan,
1969) [75–109.](http://dx.doi.org/10.1007/BF02684599) `[https://doi.org/10.1007/BF02684599](https://doi.org/10.1007/BF02684599)` .


[4] E. Witten, “Perturbative gauge theory as a string theory in twistor space,” _[Commun.](http://dx.doi.org/10.1007/s00220-004-1187-3)_ _Math._
_Phys._ **252** [(2004)](http://dx.doi.org/10.1007/s00220-004-1187-3) 189–258, `[arXiv:hep-th/0312171](http://arxiv.org/abs/hep-th/0312171)` `[hep-th]` .


[5] F. Cachazo, S. He, and E. Y. Yuan, “Scattering equations and Kawai-Lewellen-Tye
orthogonality,” _Phys._ _Rev._ **D90** [no.](http://dx.doi.org/10.1103/PhysRevD.90.065001) 6, (2014) 065001, `[arXiv:1306.6575](http://arxiv.org/abs/1306.6575)` `[hep-th]` .


[6] F. Cachazo, S. He, and E. Y. Yuan, “Scattering of Massless Particles in Arbitrary
Dimensions,” _Phys._ _Rev._ _Lett._ **113** no. 17, (2014) 171601, `[arXiv:1307.2199](http://arxiv.org/abs/1307.2199)` `[hep-th]` .


[7] N. Berkovits, “Infinite Tension Limit of the Pure Spinor Superstring,” _JHEP_ **03** [(2014)](http://dx.doi.org/10.1007/JHEP03(2014)017) 017,

`[arXiv:1311.4156](http://arxiv.org/abs/1311.4156)` `[hep-th]` .


[8] L. Mason and D. Skinner, “Ambitwistor strings and the scattering equations,” _JHEP_ **[07](http://dx.doi.org/10.1007/JHEP07(2014)048)**
[(2014)](http://dx.doi.org/10.1007/JHEP07(2014)048) 048, `[arXiv:1311.2564](http://arxiv.org/abs/1311.2564)` `[hep-th]` .


[9] N. Arkani-Hamed, F. Cachazo, C. Cheung, and J. Kaplan, “A Duality For The S Matrix,”

_JHEP_ **03** [(2010)](http://dx.doi.org/10.1007/JHEP03(2010)020) 020, `[arXiv:0907.5418](http://arxiv.org/abs/0907.5418)` `[hep-th]` .


[10] A. Hodges, “Eliminating spurious poles from gauge-theoretic amplitudes,” _JHEP_ **[05](http://dx.doi.org/10.1007/JHEP05(2013)135)** (2013)
[135,](http://dx.doi.org/10.1007/JHEP05(2013)135) `[arXiv:0905.1473](http://arxiv.org/abs/0905.1473)` `[hep-th]` .


[11] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. B. Goncharov, A. Postnikov, and J. Trnka,
_Grassmannian_ _Geometry_ _of_ _Scattering_ _Amplitudes_ . Cambridge University Press, 2016.
`[arXiv:1212.5605](http://arxiv.org/abs/1212.5605)` `[hep-th]` .


[12] N. Arkani-Hamed and J. Trnka, “The Amplituhedron,” _JHEP_ **10** [(2014)](http://dx.doi.org/10.1007/JHEP10(2014)030) 030,

`[arXiv:1312.2007](http://arxiv.org/abs/1312.2007)` `[hep-th]` .


[13] N. Arkani-Hamed, Y. Bai, and T. Lam, “Positive Geometries and Canonical Forms,” _[JHEP](http://dx.doi.org/10.1007/JHEP11(2017)039)_
**11** [(2017)](http://dx.doi.org/10.1007/JHEP11(2017)039) 039, `[arXiv:1703.04541](http://arxiv.org/abs/1703.04541)` `[hep-th]` .


[14] N. Arkani-Hamed, H. Thomas, and J. Trnka, “Unwinding the Amplituhedron in Binary,”

`[arXiv:1704.05069](http://arxiv.org/abs/1704.05069)` `[hep-th]` .


[15] F. Cachazo, S. He, and E. Y. Yuan, “Scattering of Massless Particles: Scalars, Gluons and
Gravitons,” _JHEP_ **07** [(2014)](http://dx.doi.org/10.1007/JHEP07(2014)033) 033, `[arXiv:1309.0885](http://arxiv.org/abs/1309.0885)` `[hep-th]` .


[16] J. D. Stasheff, “Homotopy Associativity of H-Spaces. I,” _Transactions_ _of_ _the_ _American_
_Mathematical_ _Society_ **108** no. 2, (1963) 275–292. `[http://www.jstor.org/stable/1993608](http://www.jstor.org/stable/1993608)` .


[17] J. D. Stasheff, “Homotopy Associativity of H-Spaces. II,” _Transactions_ _of_ _the_ _American_
_Mathematical_ _Society_ **108** no. 2, (1963) 293–312. `[http://www.jstor.org/stable/1993609](http://www.jstor.org/stable/1993609)` .


[18] Z. Bern, J. J. M. Carrasco, and H. Johansson, “New Relations for Gauge-Theory
Amplitudes,” _Phys._ _Rev._ **[D78](http://dx.doi.org/10.1103/PhysRevD.78.085011)** (2008) 085011, `[arXiv:0805.3993](http://arxiv.org/abs/0805.3993)` `[hep-ph]` .


[19] Z. Bern, J. J. M. Carrasco, and H. Johansson, “Perturbative Quantum Gravity as a Double
Copy of Gauge Theory,” _Phys._ _Rev._ _Lett._ **[105](http://dx.doi.org/10.1103/PhysRevLett.105.061602)** (2010) 061602, `[arXiv:1004.0476](http://arxiv.org/abs/1004.0476)` `[hep-th]` .


[20] N. Arkani-Hamed, L. Rodina, and J. Trnka, “Locality and Unitarity from Singularities and
Gauge Invariance,” `[arXiv:1612.02797](http://arxiv.org/abs/1612.02797)` `[hep-th]` .


                   - 75                   

[21] F. Cachazo, S. He, and E. Y. Yuan, “Scattering Equations and Matrices: From Einstein To
Yang-Mills, DBI and NLSM,” _JHEP_ **07** [(2015)](http://dx.doi.org/10.1007/JHEP07(2015)149) 149, `[arXiv:1412.3479](http://arxiv.org/abs/1412.3479)` `[hep-th]` .


[22] D. Tamari, “Monoides préordonnés et chaînes de Malcev,” _Bulletin_ _de_ _la_ _[Société](http://dx.doi.org/10.24033/bsmf.1446)_
_mathématique_ _de_ _[France](http://dx.doi.org/10.24033/bsmf.1446)_ (Jan., 1954) .


[23] G. M. Ziegler, _Lectures_ _on_ _polytopes_ _(Graduate_ _Texts_ _in_ _Mathematics,_ _Vol._ _152)_ .
Springer-Verlag, 1995.


[24] “Wikipedia: Catalan number.” `[https://en.wikipedia.org/wiki/Catalan_number](https://en.wikipedia.org/wiki/Catalan_number)` .


[25] Y. Bai and S. He, “The Amplituhedron from Momentum Twistor Diagrams,” _JHEP_ **[02](http://dx.doi.org/10.1007/JHEP02(2015)065)**
[(2015)](http://dx.doi.org/10.1007/JHEP02(2015)065) 065, `[arXiv:1408.2459](http://arxiv.org/abs/1408.2459)` `[hep-th]` .


[26] S. L. Devadoss, “Tessellations of Moduli Spaces and the Mosaic Operad,” _ArXiv_ _Mathematics_
_e-prints_ (July, 1998), `[math/9807010](http://arxiv.org/abs/math/9807010)` .


[27] A. J. Hanson and J.-P. Sha, “A contour integral representation for the dual five-point
function and a symmetry of the genus-4 surface in R**6,” _J._ _Phys._ **A39** [(2006)](http://dx.doi.org/10.1088/0305-4470/39/10/017) 2509–2537.


[28] S. Mizera, “Combinatorics and Topology of Kawai-Lewellen-Tye Relations,” _JHEP_ **[08](http://dx.doi.org/10.1007/JHEP08(2017)097)** (2017)
[097,](http://dx.doi.org/10.1007/JHEP08(2017)097) `[arXiv:1706.08527](http://arxiv.org/abs/1706.08527)` `[hep-th]` .


[29] N. Arkani-Hamed, “Amplitudes and Correlators as Canonical Forms; Worldsheets as Positive
Geometries.”
`[http://www.strings2017.org/wp-content/uploads/2017/06/1000_nimastring.pdf](http://www.strings2017.org/wp-content/uploads/2017/06/1000_nimastring.pdf)` .


[30] L. de la Cruz, A. Kniss, and S. Weinzierl, “Properties of scattering forms and their relation
to associahedra,” `[arXiv:1711.07942](http://arxiv.org/abs/1711.07942)` `[hep-th]` .


[31] V. P. Nair, “A Current Algebra for Some Gauge Theory Amplitudes,” _Phys._ _Lett._ **B214**
(1988) [215–218.](http://dx.doi.org/10.1016/0370-2693(88)91471-2)


[32] F. Cachazo, S. He, and E. Y. Yuan, “Scattering in Three Dimensions from Rational Maps,”

_JHEP_ **10** [(2013)](http://dx.doi.org/10.1007/JHEP10(2013)141) 141, `[arXiv:1306.2962](http://arxiv.org/abs/1306.2962)` `[hep-th]` .


[33] Z. Koba and H. B. Nielsen, “Manifestly crossing invariant parametrization of n meson
amplitude,” _Nucl._ _Phys._ **[B12](http://dx.doi.org/10.1016/0550-3213(69)90071-6)** (1969) 517–536.


[34] C. R. Mafra, O. Schlotterer, and S. Stieberger, “Complete N-Point Superstring Disk
Amplitude II. Amplitude and Hypergeometric Function Structure,” _Nucl._ _Phys._ **[B873](http://dx.doi.org/10.1016/j.nuclphysb.2013.04.022)** (2013)
[461–513,](http://dx.doi.org/10.1016/j.nuclphysb.2013.04.022) `[arXiv:1106.2646](http://arxiv.org/abs/1106.2646)` `[hep-th]` .


[35] F. Cachazo, S. Mizera, and G. Zhang, “Scattering Equations: Real Solutions and Particles on
a Line,” _JHEP_ **03** [(2017)](http://dx.doi.org/10.1007/JHEP03(2017)151) 151, `[arXiv:1609.00008](http://arxiv.org/abs/1609.00008)` `[hep-th]` .


[36] V. Del Duca, L. J. Dixon, and F. Maltoni, “New color decompositions for gauge amplitudes
at tree and loop level,” _Nucl._ _Phys._ **[B571](http://dx.doi.org/10.1016/S0550-3213(99)00809-3)** (2000) 51–70, `[arXiv:hep-ph/9910563](http://arxiv.org/abs/hep-ph/9910563)` `[hep-ph]` .


[37] R. Kleiss and H. Kuijf, “Multi - Gluon Cross-sections and Five Jet Production at Hadron
Colliders,” _Nucl._ _Phys._ **[B312](http://dx.doi.org/10.1016/0550-3213(89)90574-9)** (1989) 616–644.


[38] Z. Bern and T. Dennen, “A Color Dual Form for Gauge-Theory Amplitudes,” _Phys._ _[Rev.](http://dx.doi.org/10.1103/PhysRevLett.107.081601)_
_Lett._ **107** [(2011)](http://dx.doi.org/10.1103/PhysRevLett.107.081601) 081601, `[arXiv:1103.0312](http://arxiv.org/abs/1103.0312)` `[hep-th]` .


[39] C. R. Mafra, O. Schlotterer, and S. Stieberger, “Explicit BCJ Numerators from Pure
Spinors,” _JHEP_ **07** [(2011)](http://dx.doi.org/10.1007/JHEP07(2011)092) 092, `[arXiv:1104.5224](http://arxiv.org/abs/1104.5224)` `[hep-th]` .


[40] T. Adamo, E. Casali, and D. Skinner, “Ambitwistor strings and the scattering equations at
one loop,” _JHEP_ **04** [(2014)](http://dx.doi.org/10.1007/JHEP04(2014)104) 104, `[arXiv:1312.3828](http://arxiv.org/abs/1312.3828)` `[hep-th]` .


                   - 76                   

[41] K. Ohmori, “Worldsheet Geometries of Ambitwistor String,” _JHEP_ **06** [(2015)](http://dx.doi.org/10.1007/JHEP06(2015)075) 075,

`[arXiv:1504.02675](http://arxiv.org/abs/1504.02675)` `[hep-th]` .


[42] E. Casali, Y. Geyer, L. Mason, R. Monteiro, and K. A. Roehrig, “New Ambitwistor String
Theories,” _JHEP_ **11** [(2015)](http://dx.doi.org/10.1007/JHEP11(2015)038) 038, `[arXiv:1506.08771](http://arxiv.org/abs/1506.08771)` `[hep-th]` .


[43] E. Casali and P. Tourkine, “On the null origin of the ambitwistor string,” _JHEP_ **11** (2016)
[036,](http://dx.doi.org/10.1007/JHEP11(2016)036) `[arXiv:1606.05636](http://arxiv.org/abs/1606.05636)` `[hep-th]` .


[44] W. Siegel, “Amplitudes for left-handed strings,” `[arXiv:1512.02569](http://arxiv.org/abs/1512.02569)` `[hep-th]` .


[45] H. Kawai, D. C. Lewellen, and S. H. H. Tye, “A Relation Between Tree Amplitudes of Closed
and Open Strings,” _Nucl._ _Phys._ **[B269](http://dx.doi.org/10.1016/0550-3213(86)90362-7)** (1986) 1–23.


[46] Y.-t. Huang, W. Siegel, and E. Y. Yuan, “Factorization of Chiral String Amplitudes,” _[JHEP](http://dx.doi.org/10.1007/JHEP09(2016)101)_
**09** [(2016)](http://dx.doi.org/10.1007/JHEP09(2016)101) 101, `[arXiv:1603.02588](http://arxiv.org/abs/1603.02588)` `[hep-th]` .


[47] S. Mizera, “Scattering Amplitudes from Intersection Theory,” `[arXiv:1711.00469](http://arxiv.org/abs/1711.00469)` `[hep-th]` .


[48] D. Tamari, “The algebra of bracketings and their enumeration,” _Nieuw_ _Arch._ _Wisk_ **3** no. 10,
(1962) 131–146.


[49] X. Gao, S. He, and Y. Zhang, “Labelled tree graphs, Feynman diagrams and disk integrals,”

`[arXiv:1708.08701](http://arxiv.org/abs/1708.08701)` `[hep-th]` .


[50] “Wikipedia: Permutohedron.” `[https://en.wikipedia.org/wiki/Permutohedron](https://en.wikipedia.org/wiki/Permutohedron)` .


[51] A. Postnikov, “Permutohedra, associahedra, and beyond,” _ArXiv_ _Mathematics_ _e-prints_ (July,
2005), `[math/0507163](http://arxiv.org/abs/math/0507163)` .


[52] A. Postnikov, V. Reiner, and L. Williams, “Faces of Generalized Permutohedra,” _ArXiv_
_Mathematics_ _e-prints_ (Sept., 2006), `[math/0609184](http://arxiv.org/abs/math/0609184)` .


[53] N. Early, “Generalized Permutohedra, Scattering Amplitudes, and a Cubic Three-Fold,”

`[arXiv:1709.03686](http://arxiv.org/abs/1709.03686)` `[math.CO]` .


[54] F. Cachazo, “Combinatorial Factorization,” `[arXiv:1710.04558](http://arxiv.org/abs/1710.04558)` `[hep-th]` .


[55] E. Casali and P. Tourkine, “Infrared behaviour of the one-loop scattering equations and
supergravity integrands,” _JHEP_ **04** [(2015)](http://dx.doi.org/10.1007/JHEP04(2015)013) 013, `[arXiv:1412.3787](http://arxiv.org/abs/1412.3787)` `[hep-th]` .


[56] Y. Geyer, L. Mason, R. Monteiro, and P. Tourkine, “Loop Integrands for Scattering
Amplitudes from the Riemann Sphere,” _Phys._ _Rev._ _Lett._ **115** no. 12, (2015) 121603,
`[arXiv:1507.00321](http://arxiv.org/abs/1507.00321)` `[hep-th]` .


[57] S. He and E. Y. Yuan, “One-loop Scattering Equations and Amplitudes from Forward
Limit,” _Phys._ _Rev._ **D92** [no.](http://dx.doi.org/10.1103/PhysRevD.92.105004) 10, (2015) 105004, `[arXiv:1508.06027](http://arxiv.org/abs/1508.06027)` `[hep-th]` .


[58] Y. Geyer, L. Mason, R. Monteiro, and P. Tourkine, “One-loop amplitudes on the Riemann
sphere,” _JHEP_ **03** [(2016)](http://dx.doi.org/10.1007/JHEP03(2016)114) 114, `[arXiv:1511.06315](http://arxiv.org/abs/1511.06315)` `[hep-th]` .


[59] F. Cachazo, S. He, and E. Y. Yuan, “One-Loop Corrections from Higher Dimensional Tree
Amplitudes,” _JHEP_ **08** [(2016)](http://dx.doi.org/10.1007/JHEP08(2016)008) 008, `[arXiv:1512.05001](http://arxiv.org/abs/1512.05001)` `[hep-th]` .


[60] Y. Geyer, L. Mason, R. Monteiro, and P. Tourkine, “Two-Loop Scattering Amplitudes from
the Riemann Sphere,” _Phys._ _Rev._ **D94** [no.](http://dx.doi.org/10.1103/PhysRevD.94.125029) 12, (2016) 125029, `[arXiv:1607.08887](http://arxiv.org/abs/1607.08887)` `[hep-th]` .


[61] S. He and O. Schlotterer, “New Relations for Gauge-Theory and Gravity Amplitudes at Loop
Level,” _Phys._ _Rev._ _Lett._ **118** no. 16, (2017) 161601, `[arXiv:1612.00417](http://arxiv.org/abs/1612.00417)` `[hep-th]` .


                   - 77                   

[62] S. He, O. Schlotterer, and Y. Zhang, “New BCJ representations for one-loop amplitudes in
gauge theories and gravity,” `[arXiv:1706.00640](http://arxiv.org/abs/1706.00640)` `[hep-th]` .


[63] H. Gomez, S. Mizera, and G. Zhang, “CHY Loop Integrands from Holomorphic Forms,”

_JHEP_ **03** [(2017)](http://dx.doi.org/10.1007/JHEP03(2017)092) 092, `[arXiv:1612.06854](http://arxiv.org/abs/1612.06854)` `[hep-th]` .


[64] R. Roiban, M. Spradlin, and A. Volovich, “On the tree level S matrix of Yang-Mills theory,”

_Phys._ _Rev._ **[D70](http://dx.doi.org/10.1103/PhysRevD.70.026009)** (2004) 026009, `[arXiv:hep-th/0403190](http://arxiv.org/abs/hep-th/0403190)` `[hep-th]` .


[65] S. He, “Scattering amplitudes as differential forms.”

`[http://online.kitp.ucsb.edu/online/scamp_c17/he/](http://online.kitp.ucsb.edu/online/scamp_c17/he/)` .


                   - 78                   

