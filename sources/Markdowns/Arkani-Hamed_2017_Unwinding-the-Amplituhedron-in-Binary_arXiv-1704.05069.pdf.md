Prepared for submission to JHEP

##### **Unwinding the Amplituhedron in Binary**


**Nima** **Arkani-Hamed,** [1] **Hugh** **Thomas,** [2] **Jaroslav** **Trnka** [3]


1 _School_ _of_ _Natural_ _Sciences,_ _Institute_ _for_ _Advanced_ _Study,_ _Princeton,_ _NJ_ _08540,_ _USA_

2 _LaCIM, D´epartement de Math´ematiques,_ _Universit´e du Qu´ebec `a Montr´eal,_ _Montr´eal,_ _QC, Canada_

3 _Center_ _for_ _Quantum_ _Mathematics_ _and_ _Physics_ _(QMAP),_
_Department_ _of_ _Physics,_ _University_ _of_ _California,_ _Davis,_ _CA_ _95616,_ _USA_


_E-mail:_ `arkani@ias.edu,` `[hugh.ross.thomas@gmail.com,](mailto:arkani@ias.edu, hugh.ross.thomas@gmail.com, trnka@ucdavis.edu)` `trnka@ucdavis.edu`


Abstract: We present new, fundamentally combinatorial and topological characterizations
of the amplituhedron. Upon projecting external data through the amplituhedron, the resulting configuration of points has a specified (and maximal) generalized “winding number”.
Equivalently, the amplituhedron can be fully described in binary: canonical projections of
the geometry down to one dimension have a specified (and maximal) number of “sign flips”
of the projected data. The locality and unitarity of scattering amplitudes are easily derived
as elementary consequences of this binary code. Minimal winding defines a natural “dual”
of the amplituhedron. This picture gives us an avatar of the amplituhedron purely in the
configuration space of points in vector space (momentum-twistor space in the physics), a new
interpretation of the canonical amplituhedron form, and a direct bosonic understanding of
the scattering super-amplitude in planar _N_ = 4 SYM as a differential form on the space of
physical kinematical data.


**Contents**


**1** **The** **Amplituhedron** **2**


**2** **Projecting** **Through** _Y_ **3**


**3** **Winding** **8**


**4** **Crossings** **11**


**5** **The** **Amplituhedron** **As** **Binary** **Code** **13**


**6** **Factorization** **19**


**7** **Triangulations** **from** **Sign** **Flips** **22**


**8** **Loops** **25**


**9** **The** **Amplituhedron** **in** **Twistor** **Space** **28**


**10** **(Super)-Amplitudes** **As** **Differential** **Forms** **on** **Twistor** **Space** **30**


**11** **Parity** **33**


**12** **Different** **winding** **sectors,** _M × M_ **and** **Correlation** **Functions** **35**


**13** **A** **“Dual”** **of** **the** **Amplituhedron** **37**


**14** **Cutting** **Out** **The** **Amplituhedron** **With** **Inequalities** **38**


**15** **Open** **Problems** **and** **Outlook** **40**


                   - 1                    

**1** **The** **Amplituhedron**


Recent years have revealed a fascinating and unexpected connection between the basic physics
of particle scattering amplitudes and new mathematical structures in “positive geometry” [1–
4]. In the context of _N_ = 4 super-Yang-Mills theory in the planar limit, the Amplituhedron

[5] provides an autonomous definition of scattering amplitudes in purely geometric terms,
with no reference to quantum-mechanical evolution in space-time. The principles of locality
and unitarity are moved from their primary position in the usual formulation of quantum
field theory, to derivative notions emerging hand-in-hand from the positive geometry. This
physics and mathematics has been explored from a variety of perspectives in the past few
years (see e.g. [6–16]), and a systematic mathematical exploration of the notion of “positive
geometries” has recently been initiated in [17].
The amplituhedron is a simple generalization of the notion of plane polygons into the
Grassmannian. Thinking projectively, the vertices of a convex _n_ -polygon can be represented
as 3-vectors _Za_ _[I]_ [for] _[a]_ [ = 1] _[,][ · · ·]_ _[, n]_ [and] _[I]_ [= 1] _[,][ · · ·]_ _[,]_ [ 3.] [The] [convexity] [is] [reflected] [by] [positivity] [of]
minors [ _a_ _b_ _c_ ] _>_ 0 for _a_ _<_ _b_ _<_ _c_ . Then the interior of the polygon can be thought of as
_Z_ _Z_ _Z_
all the points _Y_ _[I]_ which are in the convex hull of the _Za_ _[I]_ [,] [i.e.] [all] _[Y]_ _[I]_ [of] [the] [form] _[Y]_ _[I]_ [=] _[c][a][Z]_ _a_ _[I]_
with _ca_ _>_ 0. The (tree) amplituhedron _m,k,n_ lives in the space of _k_ -planes _Y_ in ( _k_ + _m_ )
_A_
dimensions. We have external data _Za_ _[I]_ [,] [for] _[I]_ [=] [1] _[,][ · · ·]_ _[,]_ [ (] _[k]_ [ +] _[ m]_ [).] [We] [think] [of] _[Y]_ [as] [being] [the]
span of _k_ vectors _Yα_ _[I]_ [for] _[α]_ [ = 1] _[,][ · · ·][ k]_ [.] [We] [then] [consider] [all] [the] _[Y]_ _α_ _[I]_ [of] [the] [form]


_Yα_ _[I]_ [=] _[ C][αa][Z]_ _a_ _[I]_ (1.1)


where the fixed external data _a_ is “positive” in the sense of the “positive Grassmannian”,
_Z_
and we vary over _Cαa_ that are also positive in the same sense:


[ _a_ 1 _ak_ + _m_ ] _>_ 0 for _a_ 1 _<_ _< ak_ + _m,_ [ _Ca_ 1 _Cak_ ] _>_ 0 for _a_ 1 _<_ _< ak_ (1.2)
_Z_ _· · · Z_ _· · ·_ _· · ·_ _· · ·_

and the simple idea of “hiding particles” gives a natural extension of this geometry to the
“all-loop” amplituhedron. This definition needs an ordering (1 _,_ 2 _, · · ·_ _, n_ ) for the external
data, but the notion of positivity allows for a “twisted” cyclic symmetry. If the minors of _Cαa_
are positive, so are the minors of a new matrix where _Cα_ 1 _Cα_ 2, _Cα_ 2 _Cα_ 3 _,_ _, Cαn_
_→_ _→_ _· · ·_ _→_
( 1) _[k][−]_ [1] _Cα_ 1. The same is true for the _a_ . Note that if _m_ is even, ( 1) _[k][−]_ [1] ( 1) _[k]_ [+] _[m][−]_ [1] = 1

_−_ _Z_ _−_ _×_ _−_
and so the amplituhedron itself is invariant under an untwisted cyclic symmetry, while for _m_
odd the ordering is reflected in the amplituhedron geometry as well.
(We break slightly with earlier notation in the literature where the external data is
referred to as non-caligraphic _Za_ _[I]_ [since we are reserving] _[ Z]_ _a_ _[I]_ [for something else we will introduce]
shortly, and which will make a more ubiquitous appearance in this paper: the data we get
after projecting the _a_ through _Y_ . Also, strong emphasis on positivity associated with
_Z_
the the positivity of the _Cαa_ matrix, which played a starring role in the story of on-shell
diagrams, and was already “demoted” to playing an equal role with the positivity of external
_a_ data in the first description of the amplituhedron, is essentially entirely absent in our new
_Z_


                   - 2                    

picture. Therefore, no familiarity with the non-trivial aspects of the positive Grassmannian
is assumed in what follows. The few “positive properties” we will use will be introduced in a
self-contained way as needed).
Note that this description of the amplituhedron is highly redundant. This is clear already
for the polygon, since the space of the coefficients _ca_ is (projectively) ( _n_ 1) dimensional,
_−_
while the space of _Y_ ’s in the polygon is obviously only 2-dimensional. More generally the
space of the _Cαa_ is _k_ ( _n_ _k_ ) dimensional which (since _n_ ( _k_ + _m_ )) is always larger than _k_ _m_

_−_ _≥_ _×_
which is the dimensionality of the tree amplituhedron. Concretely, this means that if we are
given some _Y_, we can’t easily check whether or not it is in the amplituhedron. We would like
a different description of the amplituhedron, one which can be used to directly check whether
or not a given _Y_ is in the amplituhedron.
This is what we will do in this paper. We will give a radically different, more invariant and intrinsic definition of the amplituhedron, which is essentially entirely combinatorial/topological in nature. While we do not yet have a complete proof of the equivalence of
this new definition with the usual one, we have checked the equivalence numerically in a large
number of examples, and will also provide proofs in a number of special cases. This new
picture opens up new avenues of investigation into the structure of the amplituhedron, and
also suggests a striking new picture of scattering super-amplitudes in _N_ = 4 SYM, _directly_
as certain differential forms on the (momentum-twistor) space of external kinematical data.
We will briefly touch on a number of these points, deferring more detailed investigations to
future work.


**2** **Projecting** **Through** _Y_


We have posed a concrete question which motivates the search for a new definition of the
amplituhedron: given some _Y_, how can we check whether it is inside the amplituhedron? Now
for general convex polytopes, there is a standard answer to this question. Indeed, polytopes
can be defined in two different ways. The first is “vertex-centered”: given a collection of
points _Za_ _[I]_ [,] [the] [polytope] [is] [defined] [as] [the] [convex] [hull] [of] [these] [points.] [This] [is] [the] [“] _[Y]_ [=] _[ c][a][Z][a]_ [”]
description, which we directly generalize with the conventional definition of the amplituhedron. But there is also a second, “face-centered” description of the polytope. Here we cut out
the polytope by a collection of inequalities associated with the facets _I,i_ of the polytope,
_W_
i.e. by imposing the inequalities [ _Y_ _i_ ] 0.
_W_ _≥_
Can we extend this simple picture to the amplituhedron? We certainly know all the
co-dimension one boundaries of the amplituhedron. For instance for _m_ = 2, this corresponds
to [ _Y ii_ + 1] _→_ 0; for _m_ = 4, [ _Y ii_ + 1 _jj_ + 1] _→_ 0 etc. (Note that here, and sometimes in
what follows, when it will not cause confusion, we write _i_ for _i_ .) So it is natural to ask, for
_Z_
instance for _m_ = 2: is the amplituhedron characterized by [ _Y ii_ + 1] _≥_ 0?
The answer is easily seen to be “no”. The obstruction is a familiar one from the usual story
of the positive Grassmannian, and can be seen in the first non-trivial case of _k_ = 2 _, m_ = 2 _, n_ =
4 where the amplituhedron corresponds to the simplest positive Grassmannian _G_ +(2 _,_ 4). The


                   - 3                    

inequalities associated with the codimension one boundaries are [ _Y_ 12] _,_ [ _Y_ 23] _,_ [ _Y_ 34] _,_ [ _Y_ 14]
all _>_ 0. But then the Plucker relations tell us that


[ _Y_ 13] [ _Y_ 24] = [ _Y_ 12] [ _Y_ 34] + [ _Y_ 23] [ _Y_ 14] (2.1)


The right hand side is positive when the boundary inequalities are satisfied, but this doesn’t
fix the signs of [ _Y_ 13] _,_ [ _Y_ 24], which can be either both positive or both negative. The amplituhedron demands the choice where [ _Y_ 13] _,_ [ _Y_ 24] _<_ 0, so we see that, unlike for polygons,
the boundary inequalities are insufficient to define the space.
Let us start by defining the elementary notion of “projection”, which we will use repeatedly in the rest of this paper. Given an _N_ -dimensional vector space _**V**_, there is an obvious
notion of projection through some fixed vector _∗_ to get an ( _N_ 1) dimensional vector space.
_V_ _−_
The vectors in the new space are just the equivalence classes [ ] = + _α_ _∗_ _**V**_ . Alge_V_ _{V_ _V_ _| V_ _∈_ _}_
braically, we can always do a _GL_ ( _N_ ) transformation to put _∗_ in the form _∗_ = (0 _,_ _,_ 0 _,_ 1).
_V_ _V_ _· · ·_
A vector is then of the form = ( _V_ 1 _,_ _VN_ _−_ 1 _, ξ_ ), and we can associate the projected ( _N_ 1)
_V_ _V_ _· · ·_ _−_
dimensional vector [ ] with _V_ = ( _V_ 1 _,_ _, VN_ _−_ 1). Note that those _GL_ ( _N_ ) transformations
_V_ _· · ·_
that leave _∗_ invariant simply act as _GL_ ( _N_ 1) transformations on the projected vectors _V_ .






















To repeat the general construction, we can always do a _GL_ ( _k_ + _m_ ) transformation to put the
_k_ ( _k_ + _m_ ) matrix _Y_ in the form _Y_ = ( **0** _k×m_ **1** _k×k_ ). Then the _a_ = ( _Za_ _ξa_ ). The _GL_ ( _k_ + _m_ )
_×_ _|_ _Z_ _|_
transformations that leave _Y_ invariant act as _GL_ ( _m_ ) transformation on the _Za_ . There is also
an obvious relationship between the antisymmetric brackets in ( _k_ + _m_ ) and _m_ dimensions.
Representing _Y_ as the span of _k_ vectors _Yα_ =1 _,···,k_,


_Za_ 1 _Zam_ = [ ( _Y_ 1 _Yk_ ) _a_ 1 _am_ ] [ _Y_ _a_ 1 _am_ ] (2.2)
_⟨_ _· · ·_ _⟩_ _· · ·_ _Z_ _· · · Z_ _≡_ _Z_ _· · · Z_

We will spend the rest of this section examining what these projections look like for the

















We can easily repeat this exercise for general _k_ . For the minimal value of _n_ = _k_ + 2, the
signs of all of the [ _Y ab_ ] are fixed, and we show the pictures for _k_ = 1 _, · · ·_ _,_ 4 below:


                   - 5                    

_k_ =1 _,_ w =1 _k_ =2 _,_ w =1 _k_ =3 _,_ w =2 _k_ =4 _,_ w =2
_hY n_ 1 _i_ _>_ 0 _hY n_ 1 _i_ _<_ 0 _hY n_ 1 _i_ _>_ 0 _hY n_ 1 _i_ _<_ 0


Using the fact that we are in the _n_ = _k_ + 2 case, where the signs of all [ _Y ab_ ] are
fixed, we see that _Y_ being in the amplituhedron is characterized by the winding number of
the path (12) _,_ (23) _, · · ·_ _,_ ( _n_ 1). The necessary winding is _w_ = ( _k_ + 1) _/_ 2 when _k_ is odd, and
_w_ = ( _k/_ 2) when _k_ is even. Note that these two cases are simply distinguished by ( _−_ 1) _[k][−]_ [1]

factors associated with the twisted cyclic symmetry, which tells us that _⟨n_ 1 _⟩_ = [ _Y n_ 1] _>_ 0
for _k_ odd and _⟨n_ 1 _⟩_ = [ _Y n_ 1] _<_ 0 for _k_ even. As we will argue, this picture works for all _n_ :
_Y_ is in the amplituhedron if and only if _⟨ii_ + 1 _⟩_ _>_ 0, and the path (12) _,_ (23) _, · · ·_ _,_ ( _n_ 1) has
winding number _w_ = 2
_⌊_ _[k]_ [+1] _[⌋]_ [.]

What happens for _m_ = 1? Here the only obvious co-dimension one boundary inequalities
correspond to ( _−_ 1) _[k]_ [ _Y_ 1] _>_ 0 _,_ [ _Y n_ ] _>_ 0, which can’t cut out the amplituhedron (for one
thing they can’t even distinguish between different _k_ ’s!). But let us follow the same logic as
for _m_ = 2, and ask what the picture looks like after we project through _Y_ . Here the final
space is even simpler—it is only 1-dimensional! Clearly we can’t be talking about the notion
of “winding number” as we did for _m_ = 2, but we can do something even more primitive:
we can look at the number of times the path (12) _,_ (23) _, · · ·_ _,_ ( _n −_ 1 _n_ ) jumps over _Y_ (again
mapped to the origin), or, equivalently, we can count the number of sign flips in the sequence
_{⟨_ 1 _⟩, · · ·_ _, ⟨n⟩}_ . Looking again at the case of minimal _n_ = ( _k_ + 1) reveals the pattern we are
looking for:

###### 1 Y 2 1 3 Y 2 1 3 Y 4 2 k =1, 1 flip k =2, 2 flips k =3, 3 flips


Again this extends for general _n_ : _Y_ is in the _m_ = 1 amplituhedron if the sequence
_{⟨_ 1 _⟩, · · ·_ _, ⟨n⟩}_ = _{_ [ _Y_ 1] _, · · ·_ _,_ [ _Y n_ ] _}_ has exactly _k_ sign flips.


                   - 6                    

It is interesting to note that a natural relationship between the “winding” and “flip”
pictures. Consider an _m_ = 2 configuration. Then, if we project through e.g. the point _Z_ 1,
to go down to one dimension, the resulting configuration of the projected _Z_ 2 _,_ _, Zn_ has the
_· · ·_
sign flip pattern compatible with the _m_ = 1 amplituhedron, i.e. it has precisely _k_ sign flips.












##### k =2 flips 0 flips





Indeed, projecting down to one dimension from two dimension gives us a way to characterize the points in the amplituhedron without explicitly assuming that we are on the right
side of the boundaries! We can instead simply demand that we get the correct sign flip pattern upon projecting through _each_ of the vertices _Za_, (and as always appropriately including
the factors of ( _−_ 1) _[k][−]_ [1] for the twisted cyclic symmetry). In the righthand figure below, _Y_
is in the amplituhedron, which can be verified either because it is on the right side of the
boundaries and has the correct winding, or because in each of the projected one-dimensional
pictures, the number of flips equals _k_ . In the lefthand figure, _Y_ is not in the amplituhedron,
which can be verified either by observing that it is on the wrong side of the (34) boundary,
or that the number of sign-flips in the projected one-dimensional pictures is not always equal
to _k_ .


                   - 7                    

2



4



4



2

_−_ 1

_−_ 3


_Y_

_−_ 4


3
1

_−_ 2




_−_ 3


1




_−_ 1

3


_Y_ _−_ 4


_−_ 2



4 2 _Y_ 3


_−_ 3 _−_ 1 _Y_ _−_ 2



4 2 _Y_ 3


_−_ 1 _Y_ _−_ 2 _−_ 3


**3** **Winding**


###### 2 2 1 1


###### 2 2 2 2



Having motivated our approach to characterizing the amplituhedron with simple examples,
we now give a more systematic account starting with the case of even _m_, where we will use
a generalized notion of “winding number”. Let us first precisely define what we mean by
winding number (again for even _m_ ); since this is a general topological notion we will do this
for a completely generic configuration of _Za_ .
Start with _m_ = 2. We can count the winding number by asking whether or not a vector
pointed in some direction _Z∗_ will intersect the interior of a given boundary ( _ii_ + 1). This
means that some positive multiple of _Z∗_ should be expressible as a _positive_ linear combination
of _Zi_ and _Zi_ +1, i.e. that we should be able to express


_x∗Z∗_ = _xiZi_ + _xi_ +1 _Zi_ +1 with _x∗, xi, xi_ +1 _>_ 0 (3.1)


This tells us that a vector in the direction _Z∗_ intersects the boundary ( _ii_ + 1) if and only
_⟨Z∗Zi⟩_
if _⟨ZiZi_ +1 _⟩_ _[<]_ [ 0] _[,]_ _[⟨]_ _⟨_ _[Z]_ _Z_ _[∗]_ _iZ_ _[Z]_ _i_ _[i]_ +1 [+1] _⟩_ _[⟩]_ _[>]_ [ 0.] [This] [leads] [us] [to] [define]



_⟨Z_ _[∗]_ _iZi_ _[i]_ +1 [+1] _⟩_ _[>]_ [ 0.] [This] [leads] [us] [to] [define]



_wi_ ( _Z∗_ ) =




+1 if sgn _{⟨ZiZi_ +1 _⟩, ⟨Z∗Zi⟩, ⟨Z∗Zi_ +1 _⟩}_ = _{_ + _, −,_ + _}_ or _{−,_ + _, −}_ (3.2)
0 otherwise




- 8 

_i_ +1




#### _Y_






|Col1|i|Col3|
|---|---|---|
||+_Z_<br>+_Zi_||
||_⇤i−_1<br>+_Z_|_⇤i−_1<br>+_Z_|



_i−_ 1





Then we define the total winding number to sum all the boundaries that are hit in this
way, with a factor of +1 when they are oriented as _⟨ii_ + 1 _⟩_ _>_ 0, and ( _−_ 1) when _⟨ii_ + 1 _⟩_ _<_ 0:




  _wm_ =2 =



sgn( _ZiZi_ +1 ) _wi_ ( _Z∗_ ) (3.3)
_⟨_ _⟩_ _×_
_i_



Note that in our applications, where we demand that _⟨ii_ + 1 _⟩_ _>_ 0 with the twisted cyclic
symmetry, we only pick up a minus sign for the boundaries ( _n_ 1), and only when _k_ is even.
The total winding number does not depend on _Z∗_ . This is both intuitively obvious and
easy to prove. As we change _Z∗_ smoothly, the _wi_ will not change till the line pointing in the
direction of _Z∗_ is hitting the boundary of some interval ( _ii_ +1). Let’s follow what happens as
we start with some boundary ( _ii_ +1) that is hit—where we can expand _x∗Z∗_ = _xiZi_ + _xi_ +1 _Zi_ +1
with _x∗, xi, xi_ +1 _>_ 0, and move _xi_ +1 to be very slightly positive, then zero, then slightly
negative. Right on the boundary where _xi_ +1 0, _Z∗_ is obviously also on the boundary of
_→_
the different interval ( _i −_ 1 _i_ ), so it is natural to ask about whether or this interval is also hit.
For small _xi_ +1,
_i_ 1 _i_
_⟨∗_ _−_ _⟩_ _[−][x][i]_ _,_ _⟨∗_ _⟩_ _[−][x][i]_ [+1] _[⟨][ii]_ [ + 1] _[⟩]_ _._ (3.4)

[=] [=]



_⟨∗i −_ 1 _⟩_

_i_ 1 _i_ _[−]_ _x_ _[x]_ _∗_ _[i]_
_⟨_ _−_ _⟩_ [=]



_i_

_[x][i]_ _,_ _⟨∗_ _⟩_

_x∗_ _i_ 1 _i_ _[−][x]_ _x_ _[i]_ _∗_ [+1] _i_ _[⟨][ii]_ [ + 1] 1 _i_ _[⟩]_
_⟨_ _−_ _⟩_ [=] _⟨_ _−_ _⟩_



_._ (3.4)
_x∗_ _i_ 1 _i_
_⟨_ _−_ _⟩_



Thus if the signs of _ii_ + 1 and _i_ 1 _i_ are the same, then when _xi_ +1 is slightly positive
_⟨_ _⟩_ _⟨_ _−_ _⟩_
we intersect ( _ii_ + 1) but not ( _i_ 1 _i_ ), and when we pass through to _xi_ +1 slightly negative
_−_
we no longer intersect ( _ii_ + 1) but _do_ intersect ( _i −_ 1 _i_ ). Thus _wi_ + _wi−_ 1 = 1 for both signs
of _xi_ +1 and the total winding number doesn’t change. On the other hand when the signs of
_i_ 1 _i_ and _ii_ + 1 are opposite, then when _xi_ +1 is slightly positive _both_ intervals are hit,
_⟨_ _−_ _⟩_ _⟨_ _⟩_
while when _xi_ +1 crosses to be slightly negative _neither_ of the intervals is hit. Thus the sum
of the contributions to the winding from ( _i_ 1 _i_ ) and ( _ii_ + 1) are zero for both signs of _xi_ +1
_−_
and again the total winding number doesn’t change.




- 9 

We can immediately extend to _m_ = 4. Now, projecting through _Y_ produces points _Za_
in a four-dimensional vector space. In four dimensions, it is not meaningful to talk about
the winding of a curve around the origin. The obvious generalization is to ask about the
winding of some topological 3-sphere around the origin instead. There is a 3-sphere naturally
present in the story: the piecewise linear sphere formed from the simplices ( _ii_ + 1 _jj_ + 1).
To understand this winding very concretely, we ask whether a vector in the direction _Z∗_
intersects a given boundary ( _ii_ + 1 _jj_ + 1), which demands that


_x∗Z∗_ = _xiZi_ + _xi_ +1 _Zi_ +1 + _xjZj_ + _xj_ +1 _Zj_ +1 with _x∗, xi, xi_ +1 _, xj, xj_ +1 _>_ 0 (3.5)



This tells us that a vector in the direction _Z∗_ intersects the boundary ( _ii_ + 1 _jj_ + 1) if and
_⟨Z∗ZiZi_ +1 _Zj_ _⟩_ _⟨Z∗ZiZj_ _Zj_ +1 _⟩_
only if _⟨ZiZi_ +1 _Zj_ _Zj_ +1 _⟩_ _[<]_ [0] _[,]_ _[⟨]_ _⟨_ _[Z]_ _Z_ _[∗]_ _iZ_ _[Z]_ _i_ _[i]_ +1 _[Z][i]_ _Z_ [+1] _j_ _Z_ _[Z]_ _j_ _[j]_ +1 [+1] _⟩_ _[⟩]_ _[>]_ [0] _[,]_ _⟨ZiZi_ +1 _Zj_ _Zj_ +1 _⟩_ _[<]_ [0] _[,]_ _[⟨]_ _⟨_ _[Z]_ _Z_ _[∗]_ _iZ_ _[Z]_ _i_ _[i]_ +1 [+1] _Z_ _[Z]_ _j_ _[j]_ _Z_ _[Z]_ _j_ _[j]_ +1 [+1] _⟩_ _[⟩]_ _[>]_ [0.] [Again]



_⟨Z∗ZiZj_ _Zj_ +1 _⟩_

_[⟨]_ _⟨_ _[Z]_ _Z_ _[∗]_ _iZ_ _[Z]_ _i_ _[i]_ +1 _[Z][i]_ _Z_ [+1] _j_ _Z_ _[Z]_ _j_ _[j]_ +1 [+1] _⟩_ _[⟩]_ _[>]_ [0] _[,]_ _⟨ZiZi_ +1 _Zj_ _Zj_ +1 _⟩_ _[<]_ [0] _[,]_ _[⟨]_ _⟨_ _[Z]_ _Z_ _[∗]_ _iZ_ _[Z]_ _i_ _[i]_ +1 [+1] _Z_ _[Z]_ _j_ _[j]_ _Z_ _[Z]_ _j_ _[j]_ +1 [+1] _⟩_ _[⟩]_



only if _⟨ZiZ∗_ _i_ +1 _i_ _Zi_ +1 _j_ _Zj_ +1 _j_ _⟩_ _[<]_ [0] _[,]_ _⟨Z_ _[∗]_ _iZi_ _[i]_ +1 _[i]_ _Z_ [+1] _j_ _Zj_ _[j]_ +1 [+1] _⟩_ _[>]_ [0] _[,]_ _⟨ZiZ∗_ _i_ +1 _i_ _Zj_ _j_ _Zj_ +1 _j_ +1 _⟩_ _[<]_ [0] _[,]_ _⟨Z_ _[∗]_ _iZi_ _[i]_ +1 [+1] _Zj_ _[j]_ _Zj_ _[j]_ +1 [+1] _⟩_ _[>]_ [0.] [Again]

this leads us to define



+1 _,_ if sgn _ZiZi_ +1 _ZjZj_ +1 _,_
_{⟨_ _⟩_
_Z∗ZiZi_ +1 _Zj_ _,_ _Z∗ZiZi_ +1 _Zj_ +1 _,_ _Z∗ZiZjZj_ +1 _,_ _Z∗Zi_ +1 _ZjZj_ +1
_⟨_ _⟩_ _⟨_ _⟩_ _⟨_ _⟩_ _⟨_ _⟩}_
= _{_ + _, −,_ + _, −,_ + _}_ or _{−,_ + _, −,_ + _, −}_
0 otherwise



_wi,j_ ( _Z∗_ ) =

















(3.6)



and we define the total winding number to sum over all the boundaries hit in this way,
sign-weighted by the orientation of the boundary in the same way as above:

     _wm_ =4 = sgn( _ZiZi_ +1 _ZjZj_ +1 ) _wi,j_ ( _Z∗_ ) (3.7)

_⟨_ _⟩_ _×_
_i,j_


Once again this total winding number is independent of _Z∗_ ; the argument is exactly the
same as we saw above for _m_ = 2. As we smoothly change _Z∗_, we only have to worry about
the situations where a point in the direction of _Z∗_ lies in some two-dimensional boundary of


                   - 10                    

the three-dimensional cell ( _ii_ + 1 _jj_ + 1); i.e. when _x∗Z∗_ = _xiZi_ + _xi_ +1 _Zi_ +1 + _xjZj_ +1. This
boundary is also shared by one other cell ( _ii_ + 1 _j −_ 1 _j_ ), and depending on the relative signs
of _⟨ii_ + 1 _jj_ + 1 _⟩_ and _⟨ii_ + 1 _j_ _−_ 1 _j⟩_, either we pass from hitting one boundary to the other
as _Z∗_ is smoothly changed with the net contribution to the winding equalling one, or we go
from hitting both to missing both with the net contribution being zero.
This definition of winding generalizes in the obvious way for any even _m_, by counting the
number of times a line in the direction _Z∗_ hits the the boundaries ( _i_ 1 _i_ 1 + 1 _· · · im/_ 2 _im/_ 2 + 1).
What winding numbers define the amplituhedron? For _m_ = 2, the winding numbers for
_k_ = 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 are 1 _,_ 1 _,_ 2 _,_ 2 _,_ 3 _,_ 3, and in general are given by _wm_ =2 _,k_ = 2 . For _m_ = 4,
_⌊_ [(] _[k]_ [+1)] _⌋_

we have windings 1 _,_ 1 _,_ 3 _,_ 3 _,_ 6 _,_ 6, in general







_wm_ =4 _,k_ =






2

_⌊_ _[k]_ [+3] _[⌋]_

2



For general even _m_, the winding number is given by







(3.8)


(3.9)



_w_ ( _m, k_ ) =






2

_⌊_ _[k]_ [+] _m_ _[m][−]_ [1] _⌋_

2



We have a simple proof of this fact for the positive Grassmannian case of _n_ = ( _k_ + _m_ ),
and it is empirically correct in all other examples we have checked. It is also interesting to
note that _wm,k_ is the _maximum_ winding possible, so the amplituhedron maximizes winding;
we will not prove these statements here, instead giving a simple proof of analogous statements
about sign flip patterns in section 5.


**4** **Crossings**


We have seen that for even _m_, the correct topological notion characterizing the amplituhedron
is that of “winding”. Already for _m_ = 1, we have seen that the correct notion was that
of counting “crossings”, the number of times the origin _Y_ was crossed in traversals from
1 _→_ 2 _→· · ·_ _→_ _n_ ; this is determined by looking at the number of sign flips in the sequence
_{_ [ _Y_ 1] _, · · ·_ _,_ [ _Y n_ ] _}_ . How can we generalize this to general odd _m_ ?
In fact the topological notions for odd _m_ and even ( _m_ + 1) are closely related to each
other. Let’s consider _m_ = 1 _, m_ = 2. In both cases, we look at the collection of simplices
( _ii_ +1). Looking at the number of sign flips simply counts how many of these intervals contain
the origin (the image of _Y_ ). In other words, for any interval ( _ii_ + 1), we define _ci_ = +1 if
sgn _i_ _,_ _i_ + 1 = + or + and _ci_ = 0 otherwise; if _ci_ = 1 the interval ( _ii_ + 1) contains
_{⟨_ _⟩_ _⟨_ _⟩}_ _{−_ _}_ _{_ _−}_
(or “crosses”) the origin.
We can extend this idea to any odd _m_ . For _m_ = 3, we look at the exactly the same
collection of simplices ( _ii_ + 1 _jj_ + 1) we consider for defining winding for _m_ = 4. Now these
3-dimensional simplices are space-filling in _m_ = 3 dimensions, and we can ask how many of


                   - 11                    

them contain the origin. We are then led to define



+1 _,_ if sgn _Zi_ +1 _ZjZj_ +1 _,_ _ZiZjZj_ +1 _,_ _ZiZi_ +1 _Zj_ +1 _,_ _ZiZi_ +1 _Zj_
_{⟨_ _⟩_ _⟨_ _⟩_ _⟨_ _⟩_ _⟨_ _⟩}_
= _{_ + _, −,_ + _, −}_ or _{−,_ + _, −,_ + _}_ (4.1)
0 otherwise



_ci,j_ =













The objects _ci, ci,j_ are analogous to the _wi, wi,j_ defined to compute winding numbers. In
the winding case, we had to sum over _all_ the boundaries in order to get an object independent
of _Z∗_ . For odd _m_, however, the story is a little different. Already for _m_ = 1 we saw that it
was natural to sum over all the boundaries _except_ the boundary ( _n_ 1); this already gave us
the characterization of the amplituhedron in terms of _k_ sign flips. Of course there would have
been no harm in including the ( _n_ 1) boundary–we would simply add one to the “crossing” for
odd _k_ –but it is more natural not to include the ( _n_ 1) boundary. We will follow this pattern
for general odd _m_ ; we define the crossings to be




 _cm_ =1 =




- 
_ci,_ _cm_ =3 =

_i_ = _n_ _i<j,j_ =



_ci,j,_ etc _._ (4.2)

_i<j,j_ = _n_



It is straightforward to compute the number of crossings for _m_ = 3 by looking at the case
of the positive Grassmannian; we find for _k_ = 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _, · · ·_ the crossings 1 _,_ 2 _,_ 4 _,_ 6 _,_ 9 _,_ 12.
In general for even _k_ we have _ck_ = _k_ ( _k_ + 2) _/_ 4, while for odd _k_ we have _ck_ = (( _k_ + 1) _/_ 2) [2],
which can be unified in the expression _ck_ = (( _k_ + 1) _/_ 2) [2] .
_⌊_ _⌋_
There is a simple picture relating “crossing” and “winding” number that gives us an
expression for _ck,m_ for odd _m_ and odd _k_ . First, most naively the crossing number for some
_k, m_ should naively be double the winding number for _k, m_ +1. The reason is that if we start
from _m_ + 1 dimensions and project through some direction _Z∗_, all the boundaries containing
the origin will be the ones that were intersected either in the direction + _Z∗_ or _Z∗_ . We can

_−_
be more precise by thinking about about passing from _m_ + 1 to _m_ dimensions by quotienting
through _Z_ 1 + _ϵZn_ . Again each winding “hit” contributes 2 to the crossing number, however,
we have to correct for the fact that we ignore the “1 _n_ ” facets when counting the crossing
number. But these facets are exactly telling us about what we get for the winding number if
we go down into the ( _m_ 1) amplituhedron after quotienting by _Z_ 1 and _Zn_ . Thus for odd _k_,
_−_
we expect







_ck,m_ = 2 _wk,m_ +1 _wk,m−_ 1 = [2] _[k]_ [ +] _[ m][ −]_ [1]
_−_ _m_ + 1




_k_ + _m−_ 2



2
_m−_ 1

2



(odd _k_ ) (4.3)



On the other hand, for even _m_ we don’t get any correction from the ( _n_ 1) boundaries, and we
find - 



_k_ + _m−_ 1







_ck,m_ = 2 _wk,m_ +1 = 2



2
_m_ +1

2



(even _k_ ) (4.4)



We have numerically checked the validitiy of these expression up to _m_ = 7 for large values of
_k_ . And again, analogous to the statement of maximal winding for even _m_, we have observed
that this crossing number is maximized by the amplituhedron.


                   - 12                    

**5** **The** **Amplituhedron** **As** **Binary** **Code**


The “winding/crossing” description we have given captures a “global”, topological property
of the _Za_ data characterizing the amplituhedron. We will now see that this information can
even more efficiently be captured in a different way. The key idea is to _further_ project through
some of the external data points, in the only natural way possible, to get down to 1 dimension.
It is very easy to see that if we start with some point in a higher _m_ amplituhedron, projecting
down to _m_ = 1 keeps us in the amplituhedron. But remarkably the opposite is also true:
the higher _m_ amplituhedron is _fully_ _determined_ by the requirement that _all_ possible “positive
projections” down to one dimension land us in the _m_ = 1 amplituhedron!
Let’s begin with the _m_ = 1 amplituhedron. The claim is that we are in the _m_ = 1
amplituhedron if and only if the sequence


_{⟨_ 1 _⟩, ⟨_ 2 _⟩, · · ·_ _, ⟨n⟩}_ has precisely _k_ sign flips (5.1)


This is equivalent to the characterization of the _m_ = 1 amplituhedron recently given in [15].
Let’s now look at _m_ = 2. Note that if we project the external data through 1,
_Z_ _Z_
the rest of the projected ’s are also positive; this is because 1 _a_ 1 _ak_ + _m−_ 1 _>_ 0 for
_Z_ _⟨Z_ _Z_ _· · · Z_ _⟩_
_a_ 1 _<_ _<_ _ak_ + _m−_ 1. Then it is natural to ask that the projected _Y_ should be in the _m_ = 1

_· · ·_
amplituhedron with external data ( 2;1 _,_ _,_ _n_ ;1) obtained by projecting through 1. We
_Z_ _· · ·_ _Z_ _Z_
can phrase this purely as a statement about the _m_ = 2 dimensional data _Za_, since projecting
through 1 followed by a projection through _Y_ is simply the same as starting from _m_ = 2
_Z_
dimensions and projecting through _Z_ 1 to get to a one-dimensional space; thus it is natural
to ask for the _m_ = 2 dimensional configuration of the vectors to have the property that
when projected through _Z_ 1 we land a configuration in the _m_ = 1 amplituhedron. Now by
the twisted cyclic symmetry, we can cycle any one of the ’s to the “ 1”. Thus, we should
_Z_ _Z_
demand that _no_ _matter_ _which_ _Za_ we project through, we end up in _m_ = 1 amplituhedron.
Now, we claim that these give us necessary and sufficient conditions for _Y_ to be in the _m_ = 2
amplituhedron! Said more explicitly, we claim that _Y_ is the _m_ = 2 amplituhedron if and
only if all the following sequences (where _Z_ [ˆ] _i_ ( 1) _[k][−]_ [1] _Zi_ accounts for the twisted cyclic
_≡_ _−_
symmetry):
 
 12 _,_ 1 _n_ 
 _⟨_ _⟩_ _· · · ⟨_ _⟩_ 
 [ˆ] 











_⟨n_ [ˆ] 1 _⟩· · · ⟨n_ ( [�] _n −_ 1) _⟩_



_⟨_ 12 _⟩, · · · ⟨_ 1 _n⟩_
_⟨_ 23 _⟩· · · ⟨_ 2 _n⟩⟨_ 2 [ˆ] 1 _⟩_
...



have precisely _k_ sign flips (5.2)



















Note as usual that in terms of the underlying ( _k_ + 2) dimensional data, this is putting
constraints on _Y_ since _ab_ = [ _Y_ _a_ _b_ ] .
_⟨_ _⟩_ _Z_ _Z_
This statement is primary, but we can quickly derive some consequences of it that will
lead to a much more efficient check of whether _Y_ is in the _m_ = 2 amplituhedron. We first
observe that the sign-flip conditions trivially reproduce the correct signs of the obvious codimension one boundaries of the amplituhedron. For _m_ = 1, the obvious boundaries are


                   - 13                    

( _−_ 1) _[k]_ _⟨_ 1 _⟩_ _>_ 0 _, ⟨n⟩_ _>_ 0. But this is automatically a consequence of the sequence _{⟨_ 1 _⟩, · · ·_ _, ⟨n⟩}_
having _k_ sign flips. Now let’s look at _m_ = 2; we will show that the sign flip pattern forces


_⟨ii_ + 1 _⟩_ _>_ 0 (5.3)


Let’s start with the sequence
_{⟨_ 12 _⟩, · · ·_ _, ⟨_ 1 _n⟩}_ (5.4)

Without loss of generality we can set _⟨_ 12 _⟩_ _>_ 0. Suppose that _k_ is even; this tells us that _⟨_ 12 _⟩_
and _⟨_ 1 _n⟩_ are both positive. But now look at the next sequence

_{⟨_ 23 _⟩, · · ·_ _,_ ( _−_ 1) _[−]_ [(] _[k][−]_ [1)] _⟨_ 21 _⟩}_ (5.5)

For _k_ even this says that _⟨_ 23 _⟩_ has the same sign as _−⟨_ 21 _⟩_ = _⟨_ 12 _⟩_ and is hence positive.
Continuing in this way we find that all of _⟨_ 12 _⟩, ⟨_ 23 _⟩, ⟨_ ( _n_ _−_ 1) _n⟩_ and _⟨_ 1 _n⟩_ are all positive.
The same argument works for _k_ odd. Thus, we see that the sign flip constraint forces the
boundaries _ii_ + 1 _>_ 0 (where as always _Zn_ +1 = ( 1) _[k][−]_ [1] _Z_ 1).
_⟨_ _⟩_ _−_
Having established this, we now show that so long as _⟨ii_ + 1 _⟩_ _>_ 0, it suffices to check the
sign flip pattern for only _one_ of projections down to _m_ = 1! In other words, we claim that


_Y_ is in the _m_ = 2 amplituhedron iff
(5.6)

[ _Y ii_ + 1] _>_ 0 _,_ and the sequence _{_ [ _Y_ 12] _, · · ·_ [ _Y_ 1 _n_ ] _}_ has precisely _k_ sign flips _._

We now show that all the sign flip patterns follow from just the one beginning with _⟨_ 12 _⟩_
as long as we have _⟨ii_ + 1 _⟩_ _>_ 0. Let’s start by showing that if _{⟨_ 12 _⟩, · · · ⟨_ 1 _n⟩}_ has _k_ sign flips,
so does _{⟨_ 23 _⟩, · · ·_ _,_ ( _−_ 1) [(] _[k][−]_ [1)] _⟨_ 21 _⟩}_ .
Let us draw these two sequences one on top of the other, shifted in the natural way:


12 13 1 _n_
_⟨_ _⟩⟨_ _⟩· · ·_ _⟨_ _⟩_ (5.7)
_⟨_ 23 _⟩· · ·_ _⟨_ 2 _n⟩⟨_ 2 [ˆ] 1 _⟩_

and let’s put in what we already know about the signs:


+ 13 ( 1) _[k][−]_ [1]
_⟨_ _⟩· · ·_ _−_ (5.8)

+ _· · ·_ _⟨_ 2 _n⟩_ ( _−_ 1) _[k][−]_ [1]



which is clearly compatible with the bottom sequence having _k_ sign flips. Now, since we know
what the ends of the sequences look like, let’s examine a block of signs in the middle,

           -           1 _i_ 1 _i_ + 1
_⟨_ _⟩⟨_ _⟩_ (5.9)
_⟨_ 2 _i⟩⟨_ 2 _i_ + 1 _⟩_


The pattern of these signs cannot be arbitrary. Indeed by the Plucker relation


_⟨_ 1 _i⟩⟨_ 2 _i_ + 1 _⟩−⟨_ 1 _i_ + 1 _⟩⟨_ 2 _i⟩_ = _⟨ii_ + 1 _⟩⟨_ 12 _⟩_ _>_ 0 (5.10)


                   - 14                    






(5.9)


where we have used that _⟨_ 12 _⟩_, _⟨ii_ + 1 _⟩_ _>_ 0. Thus while in principle we have 2 [4] = 16 possible
sign patterns in the block, the 4 combinations where _⟨_ 1 _i⟩⟨_ 2 _i_ + 1 _⟩_ _<_ 0 and _⟨_ 1 _i_ + 1 _⟩⟨_ 2 _i⟩_ _>_ 0
cannot occur. The allowed patterns can then be classified as

      -       -       -       _a_ _a_ _a_ _a_

“don’t change” _,_ _−_ “flip both”

_b_ _b_ _b_ _b_











“don’t change” _,_




_a_ _−a_
_b_ _−b_



“flip both”



and

_a_ _−a_
_a_ _a_











“flip top when same as bottom ” _,_




_a_ _a_
_−a_ _a_



“flip bottom when opposite to top”



It is now trivial to see that the number of sign flips in the two sequences must be the same.
Obviously the “don’t change” and “flip both” change the number of flips equally. The crucial
point is related to the second set of allowed possibilities. These tell us that if somewhere we
have a flip in the top row but not the bottom one, then while we can have any number of
flips of both rows thereafter, the _next_ time there is a flip in one row but not another, it must
be that the flip occurs in the second row and not the first! This is because the first row can
only flip when it has the same parity as the second, while the second can flip only when it
has the opposite parity to the first.
We can extend this analysis to any higher _m_ . Let us illustrate with the case _m_ = 4.
First, if we project the external data through any ( _b_ _b_ +1), the remaining data will still
_Z_ _Z_ _Z_
be positive. So, we claim that _Y_ is the the _m_ = 4 amplituhedron if and only if, for all such
projections, the projected _Y_ is in the _m_ = 2 amplituhedron; and as we have seen this in
turn can be checked by projecting through any _Za_ and demanding we end up in the _m_ = 1
amplituhedron. Thus, more explicitly the claim is that _Y_ is in the _m_ = 4 amplituhedron iff
the sequences (for all _i ̸_ = _a, b, b_ + 1),

_{_ [ _Y abb_ + 1 _i_ ] _}_ have precisely _k_ sign flips (5.11)

for all _a, b_ . As for _m_ = 2, we can see that this immediately implies that _Y_ is on the right side
of the boundaries, i.e.

[ _Y ii_ + 1 _jj_ + 1] _>_ 0 (5.12)


so that the physics of locality follows from the pattern of sign flips! This follows trivially
since we already saw that _⟨ii_ + 1 _⟩_ _>_ 0 follows from the sign flip pattern for _m_ = 2, so if we
projected through some ( _ZjZj_ +1) we have _ii_ + 1 _jj_ + 1 _>_ 0; since we assume the flip pattern
_⟨_ _⟩_
must work for all _j_ the result follows. And just as for _m_ = 2, we will now show that this
further implies that we only have to check the sign flip pattern for a single sequence, that is


_Y_ is in the _m_ = 4 amplituhedron iff

[ _Y ii_ + 1 _jj_ + 1] _>_ 0 _,_ and the sequence _{_ [ _Y_ 1234] _, · · ·_ [ _Y_ 123 _n_ ] _}_ has precisely _k_ sign flips
(5.13)
The proof is easy. First, the number of sign flips for the sequences _{⟨_ 1 _jj_ + 1 _i⟩}_, _{⟨_ 2 _jj_ + 1 _i⟩}_,
3 _jj_ + 1 _i_ _,_ are the obviously the same, since projecting through ( _ZjZj_ +1) we just land
_{⟨_ _⟩}_ _· · ·_


                   - 15                    

on the _m_ = 2 problem for which we’ve already established this result. Very slightly more
non-trivially we need to show that the number of sign flips for the sequences _{⟨_ 1 _j_ _−_ 1 _ji⟩}_
and _{⟨_ 1 _jj_ + 1 _i⟩}_ are the same. But we can easily do this in two steps. First, let’s look at
the sequences _{⟨_ 123 _i⟩}_ and _{⟨_ 234 _i⟩}_ . Since these have (23) in common, projecting through
( _Z_ 2 _Z_ 3) lands us on _m_ = 2 where again we know the number of flips are equal. But then from
the fact that the number of flips of _{⟨_ 1 _jj_ + 1 _i⟩}_ and _{⟨_ 2 _jj_ + 1 _i⟩}_ are the same, we see that
the number of flips of _{⟨_ 123 _i⟩}_ and _⟨_ 134 _i⟩}_ are the same. Continuing in this way we see that
the number of flips of _{⟨abb_ + 1 _i⟩}_ is independent of _a, b_ so long as _⟨ii_ + 1 _jj_ + 1 _⟩_ _>_ 0, thus it
suffices to only check the sequence _{⟨_ 123 _i⟩}_ .
For general _m, k, n_, the flip definition of the amplituhedron is then simply the space of
_Y_ ’s for which



( 1) _[k]_ 1( _i_ 1 _i_ 1 + 1) ( _i m−_ 1

_−_ _⟨_ _· · ·_ 2



2 _[−]_ [1] +1 [)] _[⟩][,][ ⟨]_ [(] _[i]_ [1] _[i]_ [1][ + 1)] _[ · · ·]_ [ (] _[i][ m]_ 2 _[−]_ [1]



2 _[−]_ [1] +1 [)] _[n][⟩]_ _[>]_ [ 0] [for] _[m]_ [odd]



(5.14)




_−_ 1 _[m][−]_ [1]

2 _[i]_ 2



2 _[i][ m]_ 2



( _i_ 1 _i_ 1 + 1) ( _i_ _[m]_ 2
_⟨_ _· · ·_



_⟨_ ( _i_ 1 _i_ 1 + 1) _· · ·_ ( _i_ _[m]_ 2 _[i][ m]_ 2 [+1][)] _[⟩]_ _[>]_ [ 0] [for] _[m]_ [even]

_{⟨_ 12 _· · ·_ ( _m −_ 1) _m⟩, · · ·_ _, ⟨_ 12 _· · ·_ ( _m −_ 1) _n⟩}_ has _k_ sign flips




_[−]_ [1] _[m][−]_ [1]

2 _[i]_ 2



**5.1** **General** **Positive** **Projections** **and** **Relations** **Between** **Amplituhedra**


Our “binary code” characterization of the amplituhedron generalizes to a deeper statement
that relates amplituhedra with different values of _m_ . To begin with, let us define a “positive
projection” _m→m′_ to be some ( _m_ _m_ _[′]_ ) plane, such that projecting the _a_ data through
_P_ _−_ _Z_
_m→m′_ leaves the data positive, that is
_P_

[ _m→m′_ _a_ 1 _ak_ + _m′_ ] _>_ 0 for _a_ 1 _<_ _< ak_ + _m′_ (5.15)
_P_ _Z_ _· · · Z_ _· · ·_

Now, it is rather trivial to see, directly from the _Y_ = _C_ _·_ _Z_ picture, that if _Y_ is in the
amplituhedron for ( _m, k_ ), then projecting everything through _P_, the projected _Y_ is the ( _k, m_ _[′]_ )
amplituhedron associated with the projected _a_ data. But much more non-trivially, we have
_Z_
an _only_ _if_ statement: _Y_ is in the amplituhedron if, and only if, for _all_ positive projections
_m→m′_, the projected _Y_ is the ( _k, m_ _[′]_ ) amplituhedron in the projected space.
_P_
The “binary code” characterization specializes this fact for _m_ = 1. We also make a
somewhat degenerate choice for the positive projections, making use of the fact that if we
project through any _b,_ _b_ +1, the remaining data is clearly positive. (This is a slightly
_Z_ _Z_
degenerate choice since _b,_ _b_ +1 are projected to the origin). Doing this successively lets
_Z_ _Z_
us project down to either _m_ = 2 or _m_ = 1; further projecting through _Z_ 1 also preserves
positivity and lets us get from _m_ = 2 to _m_ = 1.


**5.2** **The** **Positive** **Grassmannian** **From** **Flips**


The case _k_ = 0 is interesting. Here the _Z_ data is simply in the positive Grassmannian of
_G_ +( _m, n_ ), and we don’t have any _Y_ so that the _Za_ = _a_ . It is then interesting to see that
_Z_
our sign flip constraints give a different characterization of the positivity of the _Z_ ’s. This is
trivial for _m_ = 1; here we say that the sequence _{⟨_ 1 _⟩, ⟨_ 2 _⟩, · · ·_ _, ⟨n⟩}_ has _k_ = 0 sign flips, which
just says that all the entries of the 1 _× n_ _Z_ matrix are positive. We see in general that for


                   - 16                    

_k_ = 0 we are declaring that certain minors have _k_ = 0 sign flips, and thus must all have the
same sign. Let’s now look at _m_ = 2. Here our criterion is simply that _⟨ii_ + 1 _⟩_ _>_ 0, and that
_{⟨_ 12 _⟩, · · · ⟨_ 1 _n⟩}_ have zero sign flips; since _⟨_ 12 _⟩_ _>_ 0 this just tells us that that the rest of the
_⟨_ 1 _i⟩_ are positive; so for _m_ = 2 our conditions say that we should have

_⟨ii_ + 1 _⟩_ _>_ 0 _,_ and _⟨_ 13 _⟩, · · · ⟨_ 1( _n −_ 1) _⟩_ _>_ 0 (5.16)

While this doesn’t _manifestly_ force all the ordered minors of _Z_ to be positive, this subset of
minors is very well-known to the a “cluster” of _G_ +(2 _, n_ ); that is, forcing these minors to be
positive automatically forces all the rest of the ordered minors to also be positive (on the
support of the Plucker relations).
(We note paranthetically that here we are taking the “twisted” cyclic symmetry for
granted, but if we back up a step we can actually see its necessity from the sign flip point of
view. Suppose we didn’t have the twisted cyclic symmetry, but we ask that all the sequences
_{⟨_ 12 _⟩, · · · ⟨_ 1 _n⟩}, {⟨_ 23 _⟩, · · ·_ _, ⟨_ 21 _⟩}_ etc. all have _k_ = 0 sign flips. Then we quickly run into a
contradiction already for _m_ = 2 _, n_ = 4: from _{⟨_ 12 _⟩, ⟨_ 13 _⟩, ⟨_ 14 _⟩}_ we would have to say that
all these minors are (say) positive, then from _{⟨_ 23 _⟩, ⟨_ 24 _⟩, ⟨_ 21 _⟩}_, since the last sign is negative
we would have to say that _⟨_ 23 _⟩, ⟨_ 24 _⟩_ are negative, but then finally from _{⟨_ 34 _⟩, ⟨_ 31 _⟩, ⟨_ 32 _⟩}_ we
have a contradiction since _⟨_ 32 _⟩_ is forced to be positive while _⟨_ 31 _⟩_ is forced to be negative. So
the twisted cyclic symmetry is necessary to get the same number of sign flips through any
projections).
The story works the same way for any _m_ . Our constraint of _k_ = 0 sign flips forces a
certain set of minors to be positive. For _m_ odd we have that



1( _i_ 1 _i_ 1 + 1) ( _i_ _m−_ 1
_⟨_ _· · ·_ 2



2 _[−]_ [1] +1 [)] _[⟩][,][ ⟨]_ [(] _[i]_ [1] _[i]_ [1][ + 1)] _[ · · ·]_ [ (] _[i][ m]_ 2 _[−]_ [1]



2 _[−]_ [1] +1 [)] _[n][⟩][,]_




_−_ 1 _[m][−]_ [1]

2 _[i]_ 2




_[−]_ [1]

2 _[i][ m]_ 2 _[−]_ [1]



2 2 2 2 (5.17)

and _{⟨_ 12 _· · ·_ ( _m −_ 1) _m⟩, · · · ⟨_ 12 _· · ·_ ( _m −_ 1) _n⟩}_ are all _>_ 0



While for _m_ even these are



( _i_ 1 _i_ 1 + 1) ( _i_ _[m]_ 2
_⟨_ _· · ·_




[are] [all] _[>]_ [ 0] [(5.18)]
2 [+1][)] _[⟩]_ _[>]_ [ 0 and] _[ {⟨]_ [12] _[ · · ·]_ [ (] _[m][ −]_ [1)] _[m][⟩][,][ · · · ⟨]_ [12] _[ · · ·]_ [ (] _[m][ −]_ [1)] _[n][⟩}]_




_[m]_
2 _[i]_ 2



Quite beautifully, the positivity of these minors suffice to force the positivity of all the other
minors of _G_ ( _m, n_ ). Thus our sign flip criterion successfully (and non-trivially) works for the
most trivial case of _k_ = 0.
The case where _n_ = ( _k_ + _m_ ) works in exactly the same way. The external _Z_ data can be
set to the identity matrix _Za_ _[I]_ [=] _[δ]_ _a_ _[I]_ [.] [Let’s] [denote] [the] [minors] [of] [the] _[k][ ×]_ [ (] _[k]_ [ +] _[ m]_ [)] [dimensional]
_Y_ matrix as ( _a_ 1 _ak_ ). Consider any object of the type [ _Y b_ 1 _bm_ ] ; it is obviously given
_· · ·_ _· · ·_
(up to sign) by the minor ( _a_ 1 _ak_ ), ( _a_ 1 _an−m_ = _k_ ) = ( _b_ 1 _,_ _, bm_ ) are the conjugate indices
_· · ·_ _· · ·_ _· · ·_
to the ( _b_ 1 _,_ _, bm_ ). Now, since the sequence [ _Y_ 12 ( _m_ 1) _m_ ] _,_ _,_ [ _Y_ 12 ( _m_ 1) _n_ ]
_· · ·_ _{_ _· · ·_ _−_ _· · ·_ _· · ·_ _−_ _}_
has length _n −_ ( _m −_ 1) = _k_ + 1, for this sequence to have _k_ sign flips it must switch signs
in every slot, and thus we have sign constraints on the minors of _Y_ ; of course the boundary
constraints also fix signs of the _Y_ minors. For instamce, for _m_ = 2 _, k_ = 2 _, n_ = 4 we have that


[ _Y_ 12] _,_ [ _Y_ 23] _,_ [ _Y_ 34] _,_ [ _Y_ 14] _>_ 0 _→_ (34) _,_ (14) _,_ (12) _,_ (23) _>_ 0

sgn _{_ [ _Y_ 12] _,_ [ _Y_ 13] _,_ [ _Y_ 14] _}_ = _{_ + _, −,_ + _}_ _→_ (24) _>_ 0 (5.19)


                   - 17                    

and of course the positivity of (12) _,_ (23) _,_ (34) _,_ (14) together with (24) _>_ 0 also implies (13) _>_ 0
and so _Y_ is in the positive Grassmannian _G_ +(2 _,_ 4). Conversely, obviously if _Y_ is in _G_ +(2 _,_ 4)
it will have the correct sign flips. For general _k, m_ with _n_ = ( _k_ + _m_ ), we force positivity on
the ordered minors that are the “conjugates” to the ones we described above for _k_ = 0, and
again there are enough minors to guarantee all the minors are positive.


**5.3** **The** **Amplituhedron** **Maxmizes** **Flips**


We pause to note that, so long as the external _Z_ data is positive, the _maximum_ number of
flips for our sequences is also given by _k_, in other words, the sequence


_{_ [ _Y_ 12 _· · ·_ ( _m −_ 1) _m_ ] _, · · ·_ _,_ [ _Y_ 12 _· · ·_ ( _m −_ 1) _n_ ] _}_ has _at_ _most_ _k_ sign flips (5.20)


The proof uses the same simple observations exploited in the previous subsection. Suppose
that there are at least ( _k_ + 1) sign flips in the sequence, and that they occur at the slots
_j_ 1 _, j_ 2 _,_ _, jk, jk_ +1, i.e. that we have sgn([ _Y_ 123 ( _m_ 1) _jα_ +1] ) = sgn([ _Y_ 123 ( _m_
_· · ·_ _· · ·_ _−_ _−_ _· · ·_ _−_
1) _jα_ ] ). Then, 1 _,_ _,_ ( _m−_ 1) _,_ _j_ 1 _,_ _,_ _jk_ +1 are ( _m_ 1)+( _k_ +1) = ( _k_ + _m_ ) vectors that give
_Z_ _· · ·_ _Z_ _Z_ _· · ·_ _Z_ _−_
a basis for the space, so we can expand _jk_ +1 as a linear combination of them; the positivity
_Z_
of the _Z_ ’s fixes the signs in the expansion as described in section 6:

_Zjk_ +1+1 = + _Zjk_ +1 _−Zjk_ + _· · ·_ + ( _−_ 1) _[k]_ ( _Zj_ 1 _−Zm−_ 1 + _· · ·_ ( _−_ 1) _[m][−]_ [1] _Z_ 1) (5.21)


But then we can compute that [ _Y_ 12 ( _m_ 1) _Zjk_ +1] = +[ _Y_ 12 ( _m_ 1) _Zjk_ ] [ _Y_ 12 ( _m_
_· · ·_ _−_ _· · ·_ _−_ _−_ _· · ·_ _−_
1) _Zjk−_ 1] + ( 1) _[k]_ [ _Y_ 12 ( _m_ 1) _j_ 1] ; every term on the right-hand side has the same

_· · ·_ _−_ _· · ·_ _−_
sign as the first term, and so [ _Y_ 12 ( _m_ 1) _jk_ +1 + 1] can’t have the opposite sign as
_· · ·_ _−_

[ _Y_ 12 ( _m_ 1) _jk_ +1], contradicting a sign flip at _jk_ +1! Thus, a completely equivalent way
_· · ·_ _−_
of characterizing the amplituhedron is simply to say that _Y_ is in the amplituhedron if and
only if under any projection to _m_ = 1 dimensions we have the maximum possible number of
_k_ sign flips.


**5.4** _Y_ = _C · Z_ _→_ **Correct** **Flips**

We’d like to now show that for for _Y_ = _C_ _· Z_ with _C_ in the positive Grassmannian, we
have the correct sign-flip pattern. First we show that if we’ve already shown some _C_ gives
_Y_ = _C ·Z_ with the correct flips, then we can always add zero columns to _C_ without changing
the conclusions. The argument is trivial for even _m_, since we can always use the cyclic
symmetry to put the zero column at the very end. But then we are merely adding a last

[ _Y_ 1 _· · ·_ ( _m −_ 1)( _n_ + 1)] to our sequence, and since we already have the maximum number
_k_ of flips we can’t have any more. In this way, by adding a zero column at the end and
then cyclically shifting, we can add zeroes in any columns we like without changing the total
number of sign flips. Since we’ve already proven than _Y_ = _C_ _· Z_ for the _n_ = ( _k_ + _m_ ) case,
for _n >_ ( _k_ + _m_ ), we have also established the right flip pattern for the image of those _k × n_
dimensional cells of _G_ +( _k, n_ ) which correspond to positive matrices in a ( _k_ + _m_ ) subset of


                   - 18                    

the _n_ columns. But we would like to show that for _any_ positive matrix _Cαa_, the projection
through _Y_ = _C · Z_ gives the right sign flip pattern.
Here we make use of a simple but non-trivial fact about positive matrices, which tells
us how to systematically build more complicated positive matrices from simpler ones. Any
_K_ _× N_ matrix in the positive Grassmannian, including generic points in the interior (or the
“top cell”), can be constructed starting from some zero-dimensional cell (corresponding to
the ( _K ×_ _N_ ) matrix being set to the identity in some ( _K ×_ _K_ ) block and vanishing elsewhere),
and recursively shifting the columns of the matrix by positive multiples of its immediately
neighboring (non-vanishing) columns.
Thus, we can make any positive matrix _C_, by beginning with zero dimensional cells where
the _C_ matrix is the identity in some _k × k_ block, and then repeatedly shifting a given column
of _C_ by positive multiples of its neighbors. But note that under _Cαa_ _Cαa_ + _xa_ +1 _Cαa_ +1,
_→_
the effect on _Y_ is the same as if we shifted _a_ _a_ + _xa_ +1 _a_ +1; since this preserves the
_Z_ _→Z_ _Z_
positivity of the _Z_, again the (maximized) number of flips can not be altered. In this way
we can work our way up from _C_ ’s corresponding to zero-dimesional cells of _G_ +( _k, n_ ) to any
point in _G_ +( _k, n_ ).
The only subtlety in this argument is that at the starting point, where _C_ is a zerodimensional cell fixed to the identity matrix in columns ( _i_ 1 _,_ _, ik_ ), _Y_ = ( _i_ 1 _ik_ ) is also
_· · ·_ _Z_ _· · · Z_
on a zero-dimensional boundary of the amplituhedron, and many of the brackets [ _Y_ 12 _· · ·_ ( _m−_
1) _i_ ] vanish and so there is ambiguity in how to assign the signs and decide whether the starting
flip pattern in correct. But there is a very easy fix to this problem. We simply choose _C_ to
be in the positive Grassmannian associated only with columns ( _i_ 1 _,_ _, ik_ ) and any _m_ other
_· · ·_
columns, with tiny values for positive co-ordinates chosen so that _C_ is very close to the zerodimensional cell which is the identity in ( _i_ 1 _,_ _, ik_ ). Since we have already established that
_· · ·_
we get the correct sign-flip pattern for this case, we have done what was needed—find a slight
deformation that has the correct sign flip pattern. Starting from this point, we do exactly the
shifts of columns of _C_ by adjacent columns that takes _C_ to a generic point in _G_ +( _k, n_ ) and
the argument follows as before; the number of flips is preserved in every step and we etablish
the claimed result.


**6** **Factorization**


One of the central features of amplituhedron geometry is the way in which the co-dimension
one boundaries of the amplituhedron are closely related to amplituhedra with lower _k_ and
_n_ . This is expected to be a feature of amplituhedra for all _m_ . In the particular case of
_m_ = 4 we expect to see the the amplituhedron with some _k, n_ “factorize” into two lowerpoint amplituhedra ( _kL, nL_ ) and ( _kR, nR_ ) with _nL_ + _nR_ = _n_ + 2 and _kL_ + _kR_ = _k −_ 1. We
can see an avatar of factorization in “ _C_ _· Z_ ” description of the amplituhedron, in the form
of the _C_ -matrices on co-dimension one boundaries of the space. For instance when _m_ = 4,
on the co-dimension-one boundaries where [ _Y ii_ + 1 _jj_ + 1] 0, we can write _Y_ = _yf_ _y_ where
_→_
_yf_ is a point in the span of ( _i,_ _i_ +1 _,_ _j,_ _j_ +1) and _y_ is a ( _k_ 1) plane. This implies that
_Z_ _Z_ _Z_ _Z_ _−_


                   - 19                    

the _C_ matrix should have a representation where the top row is non-zero only in the entires
( _ii_ + 1 _jj_ + 1). But then, remarkably, positivity forces _C_ to “factorize” in the form


# 0 B B @


## _CL_
# CCA



_i_ _i_ +1 _j_ _j_ +1
## _⇤ ⇤ ⇤ ⇤_


# 1


## _CR_


## _CR_



where the blocks _CL_ and _CR_ are individually positive. This is strongly suggestive of factorization for the amplituhedron geometry itself. Let us examine this geometry more precisely. Given the point _yf_ in _Y_ which is in the span of ( _i,_ _i_ +1 _,_ _j,_ _j_ +1), we can expand
_Z_ _Z_ _Z_ _Z_
_yf_ = ( _αiZi_ + _αi_ +1 _Zi_ +1) + ( _αjZj_ + _αj_ +1 _Zj_ +1) _≡_ _Ii_ + _Ij_ . Then if we project through _yf_, the
geometry should consist of “left” and “right” amplituhedron, where the external data of the
“left” are (the projections through _yf_ of) _Ii,_ _j_ +1 _,_ _,_ _i_ and the “right” amplituhedron has
_Z_ _· · ·_ _Z_
external data _i_ +1 _,_ _,_ _j, Ij_ . (It is easy to see that this projected data is positive). While
_Z_ _· · ·_ _Z_
this fact is strongly suggested by the “factorization” of the _C_ -matrix, it is not easy to prove
from the _C_ picture; for instance it is not obvious that the different ( _kL, nL_ ); ( _kR, nR_ ) splits
_·Z_
are all non-overlapping in _Y_ space. As we will now see, the factorization structure of the amplituhedron boundary follows simply and provably from our point of view, as an elementary
consequence of the “binary code” of sign-flip patterns.
Let’s start with _m_ = 2. The factorization picture we expect is the following. The
boundaries are at [ _Y ii_ + 1] _→_ 0; without loss of generality we will consider the boundary
where [ _Y_ 12] _→_ 0. We can set _Y_ = _yf_ _y_ where _yf_ = ( _Z_ 1 + _xZ_ 2) with _x >_ 0, and _y_ is a ( _k −_ 1)
plane. If we project through _yf_, the resulting projected data ( 2 _,f_ _,_ _n,f_ ) is still positive.
_Z_ _· · ·_ _Z_
The “factorization” statement is then that _y_ is in the _k −_ 1 amplituhedron. Said in terms of
sign flips, this means that as we take [ _Y_ 12] _→_ 0, the sequence _{_ [ _Y_ 23] _,_ [ _Y_ 24] _, · · ·_ _,_ [ _Y_ 2 _n_ ] _}_
has ( _k −_ 1) flips.
The heart of the matter will be to show that if [ _Y_ 12] _→_ 0, then necessarily [ _Y_ 13] _<_ 0.
Let us assume for this for the moment and show how our desired result follows from it. Let’s
write again _Y_ = ( _Z_ 1 + _xZ_ 2) _y_, then if [ _Y_ 13] _<_ 0 we have that _x_ [ 2 _y_ 13] _<_ 0, but we also know
that [ _Y_ 23] _>_ 0 which means that [ 1 _y_ 23] _>_ 0; thus we must have _x >_ 0. Now we are interested
in the sign pattern of the sequence _{_ sgn([ _Y_ 2 _i_ ] ) _}_ = _{_ sgn([ 1 _y_ 2 _i_ ] ) _}_ . But this can clearly related
to the sign pattern of the sequence _{_ sgn([ _Y_ 1 _i_ ] ) _}_ = _{_ sgn( _x_ [ 2 _y_ 1 _i_ ] ) _}_ = _−{_ sgn([ _Y_ 2 _i_ ] _}_ . Thus,
the number of sign flips of the sequence _{_ [ _Y_ 23] _, · · ·_ _,_ [ _Y_ 2 _n_ ] _}_ is the same as counting the
number of sign flips of _{_ [ _Y_ 13] _, · · ·_ [ _Y_ 1 _n}_ .
Now we know that the sequence _{_ [ _Y_ 12] _,_ [ _Y_ 13] _, · · ·_ _,_ [ _Y_ 1 _n_ ] _}_ has _k_ sign flips; even though


                   - 20                    

on the boundary we have [ _Y_ 12] _→_ 0, it was approached from [ _Y_ 12] _>_ 0. Furthermore since

[ _Y_ 13] _<_ 0, we started this sequence with a single flip. Therefore, the rest of the sequence
_{_ [ _Y_ 13] _, · · ·_ [ _Y_ 1 _n_ ] _}_ must have ( _k −_ 1) flips, as desired.
So we now simply have to prove that as [ _Y_ 12] _→_ 0, we must have [ _Y_ 13] _<_ 0. The proof
will importantly use both the fact that the sequence _{_ [ _Y_ 1 _i_ ] _}_ has _k_ sign flips, as well as sign
patterns associated with the positivity of the _Z_ data.
Suppose to the contrary that [ _Y_ 13] _>_ 0. Then we must have _k_ places to the right of 3
where where the sign flips occurred, let’s call then _b_ 1 _,_ _, bk_ ; in other words we must have
_· · ·_
the signs

       -        
[ _Y_ 12] [ _Y_ 13] [ _Y_ 1 _b_ 1] [ _Y_ 1 _b_ 2] _· · ·_ [ _Y_ 1 _bk_ ] (6.1)
0 [+] + _−_ + _· · ·_ ( _−_ 1) _[k]_

We will now expand _b_ 1 in terms of the basis of 1 _,_ 2 _,_ 3 _,_ _b_ 2 _,_ _,_ _bk_, and here the positiv_Z_ _Z_ _Z_ _Z_ _Z_ _· · ·_ _Z_
ity of the _Z_ data will be important, since it implies a fixed pattern of signs in this expansion.
Indeed let us consider more generally _n_ vectors _a_ in _K_ dimensions, with all ordered
_Z_
minors positive. Let us consider ( _K_ + 1) of these vectors. Then we can expand any one
of them in a basis of the other _K_ ; the positivity of the ordered minors implies certain sign
patterns on the coefficients of this expansion. For instance consider _K_ = 4 and any five
_a_ 1 _,_ _,_ _a_ 5 for _a_ 1 _< a_ 2 _<_ _< a_ 5. Then, we can for instance expand _a_ 1 in a basis of the
_Z_ _· · ·_ _Z_ _· · ·_ _Z_
rest:

_a_ 1 = [[] _[a]_ [1] _[a]_ [3] _[a]_ [4] _[a]_ [5][]] _[Z][a]_ [2] _[−]_ [[] _[a]_ [1] _[a]_ [2] _[a]_ [4] _[a]_ [5][]] _[Z][a]_ [3] [+ [] _[a]_ [1] _[a]_ [2] _[a]_ [3] _[a]_ [5][]] _[Z][a]_ [4] _[−]_ [[] _[a]_ [1] _[a]_ [2] _[a]_ [3] _[a]_ [4][]] _[Z][a]_ [5]
_Z_ [ _a_ 2 _a_ 3 _a_ 4 _a_ 5]

= + _a_ 2 _a_ 3 + _a_ 4 _a_ 5 (6.2)
_Z_ _−Z_ _Z_ _−Z_


where in the second expression we are only keeping track of the signs of the coefficients. More
generally, for positive _Z_ and any ordered _a_ 1 _<_ _<_ _aK_ +1, any given _Zal_ can be expanded

_· · ·_
in terms of the others, starting with + signs for its immediate neighbors to the left and right
and alternating signs both to the left and to the right:


[+] _[ · · ·]_
_al_ = [+] _[Z][a][l]_ [+1] _[−Z][a][l]_ [+2] (6.3)
_Z_ + _al−_ 1 _al−_ 2 +
_Z_ _−Z_ _· · ·_

Applying this general fact to our case of interest we have simply


+ 3 2 + 1
_b_ 1 = _Z_ _−Z_ _Z_ (6.4)
_Z_ + _b_ 2 _b_ 3 + + ( 1) _[k]_ _bk_
_Z_ _−Z_ _· · ·_ _−_ _Z_

But using this expansion we can compute


[ _Y_ 1 _b_ 1] = [ _Y_ 13] _−_ [ _Y_ 12] + [ _Y_ 1 _b_ 2] _−_ [ _Y_ 1 _b_ 3] + _· · ·_ + ( _−_ 1) _[k]_ [ _Y_ 1 _bk_ ] (6.5)
= (+) + (0) + (+) + (+) + _· · ·_ + (+) _>_ 0


which contradicts [ _Y_ 1 _b_ 1] _<_ 0. Thus we can’t have [ _Y_ 13] _>_ 0, and must have [ _Y_ 13] _<_ 0.


                   - 21                    






(6.1)


Let us now move on to the more interesting case _m_ = 4. Suppose we are sitting on the
boundary where [ _Y_ 12 _jj_ + 1] _→_ 0. By projecting through either (12) or ( _jj_ + 1) to get to
_m_ = 2, we can conclude that _Y_ = ( _Z_ 1 + _xZ_ 2 + _xjZj_ + _xj_ +1 _Zj_ +1) _y_ where _y_ is a ( _k −_ 1) plane
and _x_ _>_ 0, with _xj, xj_ +1 having the same sign. Also, from what we’ve just learned about
_m_ = 2, projecting through ( _jj_ + 1) we can conclude that the sequence


_{_ [ _Y_ 23 _jj_ +1] _,_ [ _Y_ 24 _jj_ +1] _, · · ·_ _,_ [ _Y_ 2( _j −_ 1) _jj_ +1] ; [ _Y_ 2( _j_ +2) _jj_ +1] _, · · ·_ _,_ [ _Y_ 2 _njj_ +1] _}_ (6.6)

has ( _k −_ 1) sign flips. But from the facts that [ _Y_ 12 _j −_ 1 _j_ ] _>_ 0 _,_ [ _Y_ 12 _jj_ + 1] _>_ 0, we conclude
that _xj_ +1[ _y_ 12 _j_ 1 _jj_ +1] _>_ 0 and _xj_ [ _y_ 12 _jj_ +1 _j_ +2] _>_ 0; since _xj, xj_ +1 have the same sign we

_−_
conclude that [ _y_ 12 _j −_ 1 _jj_ + 1] and [ _y_ 12 _jj_ + 1 _j_ + 2] have the same sign. But this means that

[ _Y_ 2( _j_ _−_ 1) _jj_ +1] = ( _−_ 1) _[k][−]_ [1] [ _y_ 12( _j_ _−_ 1) _jj_ +1] and [ _Y_ 2( _j_ +2) _jj_ +1] = ( _−_ 1) _[k][−]_ [1] [ _y_ 12 _jj_ +1 _j_ +2]
have the same sign. Given the above sequence has ( _k −_ 1) sign flips and since we have seen
that [ _Y_ 2( _j_ _−_ 1) _jj_ + 1] ; [ _Y_ 2( _j_ + 2) _jj_ + 1] have the same sign, there is no sign flip at those
slots, so we conclude that


_{_ [ _Y_ 23 _jj_ + 1] _, · · ·_ _,_ [ _Y_ 2( _j −_ 1) _jj_ + 1] _}_ has _kR_ sign flips [=] _[ k][ −]_ [1] (6.7)

[ _Y_ 2( _j_ + 2) _jj_ + 1] _,_ _,_ [ _Y_ 2 _njj_ + 1] has _kL_ sign flips _[,]_ [ with] _[ k][L]_ [ +] _[ k][R]_
_{_ _· · ·_ _}_


Now note that since ( _jj_ +1) = ( _jIj_ ), the first sign sequence above is precisely what we would
look at to check membership in the _kL_ amplituhedron with external data 2 _,_ _,_ _j,_ _Ij_ .
_Z_ _· · ·_ _Z_ _Z_
Note also that [ _Y_ 12( _j_ +1) _i_ ] = _xj_ [ _jy_ 12 _j_ +1 _i_ ] = _xj_ [ _Y_ 2 _ijj_ +1] . Thus the number of sign flips
_−_
of the second sequence is exactly the same as the sequence _{_ [ _Y_ 12( _j_ +1)( _j_ +2) _, · · ·_ _,_ [ _Y_ 12( _j_ +
1) _n_ ] _}_ ; since 12 = 1 _I_ 1, this precisely checks membership in the _kL_ amplituhedron with external
data ( 1 _,_ _I_ 1 _,_ ( _j_ +1) _,_ _,_ _n_ ).
_Z_ _Z_ _Z_ _· · ·_ _Z_
Strictly speaking, this argument tells us that every point on the boundary of the amplituhedron belongs to the factorized product of the lower amplituhedra, but the possibility is
left open that the amplituhedron boundary is only a subset of the sum of the product of lower
amplituhedra and does not fully cover it. However, since we have shown that all _Y_ = _C_ _· Z_
do have the right flip count, we know that all the image of all the _C_ matrices of the factorized
form will have the correct flip counts on both the left and right, and we are done.


**7** **Triangulations** **from** **Sign** **Flips**


For _m_ = 1 and _m_ = 2, keeping track of the sign flip pattern give us a natural triangulation
of the amplituhedron. Let’s consider first _m_ = 1, where _Y_ is a _k_ -plane in ( _k_ + 1) dimensions.
Start with the easiest case _k_ = 1. Since we know _{_ [ _Y_ 1] _, · · ·_ _,_ [ _Y n_ ] _}_ has one sign flip, let’s focus
on the place this flip takes place; there is some _j_ for which [ _Y j_ ] _<_ 0 but [ _Y_ ( _j_ +1) _>_ 0. The full
_m_ = 1 _, k_ = 1 amplituhedron is then covered for the collection of these regions for all _m_ . Now,
with _k_ = 1 we can always expand _Y_ in some basis _A,_ _B_ as _Y_ as _Y_ = _A_ + _xB_ _B_ ; in order to
_Z_ _Z_ _Z_ _Z_
describe the _m_ = 1 “cell” where the sign flip occurs in the _j_ ’th slot, it is clearly convenient to
choose _A_ = _j_ and _B_ = _j_ +1. Then we see that [ _Y j_ ] = _x_ [ _jj_ + 1] _,_ [ _Y j_ + 1] = [ _jj_ + 1] .
_Z_ _Z_ _Z_ _Z_ _−_


                   - 22                    

Thus to match the sign pattern in this cell we must have _x_ _>_ 0; and conversely, every
_Y_ of this form with _x_ _>_ 0 will belong to this cell. We can proceed in the same way to
_k_ = 2. Here we can characterize Z the sign flips completely by specifying the two slots in the
flips took place; so there is some _j_ 1 and _j_ 2 for which [ _Y j_ 1] _>_ 0 _,_ [ _Y_ ( _j_ 1 + 1)] _<_ 0 _,_ [ _Y j_ 2] _<_
0 _,_ [ _Y_ ( _j_ 2 + 1)] _>_ 0. Again we can conveniently expand _Y_ = ( _Zj_ 1 + _x_ 1 _Zj_ 1+1)( _Zj_ 2 + _x_ 2 _Zj_ 2+1).
Now [ _Y_ ( _j_ 1 + 1)] _<_ 0 tells us that [ _j_ 1 _j_ 1+1( _j_ 2 + _x_ 2 _j_ +2)] _>_ 0, so then the positivity
_Z_ _Z_ _Z_ _Z_
of [ _Y j_ 1] = _x_ 1[ _j_ 1 _j_ 1+1( _j_ 2 + _x_ 2 _j_ 2+1)] tells us we must have _x_ 1 _>_ 0. Similarly _x_ 2 _>_ 0.
_Z_ _Z_ _Z_ _Z_
And again conversely, every _Y_ of the form with _x_ 1 _, x_ 2 _>_ 0 will belong to this “cell” of the
_m_ = 1 _, k_ = 2 amplituhedron. In general then, we find that


The region in the _m_ = 1 amplituhedron where [ _Y_ 1] [ _Y n_ ] flips in slots _j_ 1 _,_ _jk_
_{_ _· · ·_ _}_ _· · ·_
is covered by
_Y_ = ( _j_ 1 + _x_ 1 _j_ 1+1)( _j_ 2 + _x_ 2 _j_ 2+1) ( _jk_ + _xk_ _jk_ +1) with _xk_ 0
_Z_ _Z_ _Z_ _Z_ _· · ·_ _Z_ _Z_ _≥_
(7.1)
We can trivially relate this to the “ _Y_ = _C.Z_ ” description of the amplituhedron; we can think
of _Y_ as the span of the _k_ points of _Yα_ with _Yα_ = _Zjα_ + _xαZjα_ +1. Then we can also recognize
this as _Yα_ = _Cαa_ _a_, where
_Z_  



1 _a_ = _iα_
_xα_ _a_ = _iα_ + 1
0 otherwise









_Cαa_ _[{][i]_ [1] _[,][···][,i][k][}]_ =













(7.2)





with the positive variables _α_ 0. Note that the ordered minors of this _C_ -matrix are all
_Z_ _≥_
positive.
The _k_ form associated with this cell is




- _k_ 
_d_ log [ _Y Ziα_ +1]
_α_ =1 [ _Y_ _iα_ ]
_Z_




(7.3)



Ω _[{][i]_ [1] _[,][···][,i][k][}]_ =




- _k_

_d_ log _xα_ =

_α_ =1




- _k_



and the full form is

       Ω= Ω _[{][i]_ [1] _[,][···][,i][k][}]_ (7.4)


1 _≤i_ 1 _<···ik≤_ ( _n−_ 1)



The _m_ = 2 amplituhedron can be triangulated in precisely the same way. The only difference is that we have to mark the slots ( _j_ 1 _,_ _, jk_ ) where the sequence [ _Y_ 12] _,_ _,_ [ _Y_ 1 _n_ ] has
_· · ·_ _{_ _· · ·_ _}_
its sign flips. Now _Y_ is a _k_ -plane in ( _k_ +2) dimensions, and we can parametrize any _k_ -plane as
_Y_ = (+ _Z_ 1 + _x_ 1 _Zj_ 1 + _y_ 1 _Zj_ 1+1)( _−Z_ 1 + _x_ 2 _Zj_ 2 + _y_ 2 _Zj_ 2+1)(+ _Z_ 1 + _x_ 3 _Zj_ 3 + _y_ 3 _Zj_ 3+1) _· · ·_ (( _−_ 1) _[k]_ _Z_ 1 +
_xk_ _jk_ + _yk_ _jk_ +1); here the alternating signs in front of 1 are chosen for convenience. Then
_Z_ _Z_ _Z_
just as for _m_ = 1, the pattern of signs forced by flips at _j_ 1 _,_ _, jk_ forces all the _xα, yα_ 0,
_· · ·_ _≥_
and conversely any _Y_ of this form has flips in these slots. We can think of these “cells” in
the _Y_ = _C · Z_ language as _Yα_ = ( _−_ 1) [(] _[α][−]_ [1)] _Z_ 1 + _xαZjα_ + _yαZjα_ +1, giving us a _C_ matrix of the
form  



( _−_ 1) _[α][−]_ [1] _a_ = 1
_xα_ _a_ = _jα_
_yα_ _a_ = _jα_ + 1
0 otherwise

















_Cαa_ _[{][j]_ [1] _[,][···][,j][k][}]_ =

















(7.5)




- 23 

with manifestly positive minors.
We can also see this triangulation very naturally from the winding picture. Let us
characterize the winding pattern by looking at the boundaries that are hit when we choose
_∗_ to point in the two directions _∗_ = 1, and _∗_ = + 1; equivalently we are looking at
_Z_ _Z_ _−Z_ _Z_ _Z_
which boundaries are intersected by the full line joining 1 and the origin. For _k_ = 1, since
_Z_
we have winding number 1 the line in the direction 1 must intersect a single boundary
_−Z_
( _i_ 1 _i_ 1 + 1). The direction + _Z_ 1 is degenerate since both ( _n_ 1) are (12) are hit; a small variation
means only one of the two is hit. So it is useful to characterize a cell just by the ( _i_ 1 _i_ 1 + 1)
boundary hit in the direction 1. Next let’s look at _k_ = 2. The winding number here is
_−Z_
again 1, and the direction 1 again hits some ( _i_ 1 _i_ 1 + 1). But now in the direction + 1,
_−Z_ _Z_
we find that a small variation will either cause the line to hit both of ( _n_ 1) _,_ (12) or miss both
of them. Thus winding number 1 means that in the direction + 1 some other boundary
_Z_
( _i_ 2 _i_ 2 + 1) is hit. Then for _k_ = 3 with winding number 2, in direction _−Z_ 1 we must hit two
boundaries ( _i_ 1 _i_ 1 +1) _,_ ( _i_ 2 _i_ 2 +1), while in (a small deformation of) the direction + 1 we hit one
_Z_
of ( _n_ 1) _,_ (12), and thus one more boundary ( _i_ 3 _i_ 3 + 1) is hit. This pattern obviously continues
for all _k_ : the line joining _Z_ 1 to the origin intersects _k_ boundaries ( _i_ 1 _i_ 1 + 1) _, · · ·_ _,_ ( _ikik_ + 1).
This picture corresponds precisely to what we would see by projecting through 1, and the
_Z_




















- 24 

The 2 _k_ form associated with this cell is




  Ω _[{][i]_ [1] _[,][···][,i][k][}]_ =



_d_ log _xα_ _d_ log _yα_ (7.6)

_α_




  _d_ log [ _Y Z_ 1 _Ziα_ ]
_α_ [ _Y_ _iα_ _iα_ +1]
_Z_ _Z_




- - _d_ log [ _Y Z_ 1 _Ziα_ +1] ]

[ _Y_ _iα_ _iα_ +1
_Z_ _Z_




 =



d _[k]_ [(] _[k]_ [+2)] _Y_
=
Vol(GL( _k_ ))



�[ - _Y_ _[k][−]_ [1][�] _[α]_ [1] _Z_ 1 _Zi_ 1 _Zi_ 1+1 ~~�~~ ] [ - _Y_ _[k][−]_ [1][�] _[α]_ [2] _Z_ 1 _Zi_ 2 _Zi_ 2+1] _· · ·_ [ �( _Y_ _[k][−]_ [1][�] _[α][k]_ _Z_ 1 _Zik_ _Zik_ +1] _ϵα_ 1 _···αk_ - _k_
_α_ [[] _[ Y][ Z]_ [1] _[Z][i]_ _α_ [] [] _[ Y][ Z]_ [1] _[Z][i]_ _α_ [+1][] [] _[ Y][ Z][i]_ _α_ _[Z][i]_ _α_ [+1][]]



As usual the full form arise from summing over the form for each piece of the triangulation




       Ω= Ω _[{][i]_ [1] _[,][···][,i][k][}]_ (7.7)


1 _≤i_ 1 _<···ik≤_ ( _n−_ 1)


This form also has spurious poles that cancel between the terms.
This most direct connection between sign patterns and triangulations of the amplituhedron is restricted to the simplest _m_ = 1 _,_ 2 amplituhedra. Starting with _m_ = 3 _,_ 4, there isn’t a
simple relation between the image of a particular cell of _G_ +( _k, n_ ), and any one sign pattern.


**8** **Loops**


We now move on to loops, beginning with a quick review of the usual definition of the
loop-level amplituhedron. We fix _m_ = 4; at _L_ loops, we have ( _k_ + 2)-planes ( _Y AB_ ) _i_ for
_i_ = 1 _, · · ·_ _, L_, all of which intersect on a common _k_ -plane _Y_ . We can describe any of the
planes ( _Y AB_ ) _i_ as the span of _Y_ together with a 2-plane ( _AB_ ); together with a redundancy
that allows us to translate ( _AB_ ) in any direction of _Y_ . If we denote ( _AB_ ) _i_ by ( _A_ 1 _A_ 2) _i_, the
_L_ -loop amplituhedron is defined to be all the _Yα_ _[I]_ [and] _[A][I]_ _σ_ ; _i_ [of] [the] [form]


_Yα_ _[I]_ [=] _[ C][αa][Z]_ _a_ _[I]_ _[,]_ _[A][σ,i]_ [=] _[ D]_ _σa_ [(] _[i]_ [)] _[Z]_ _a_ _[I]_ (8.1)

where we have new (2 _× n_ ) matrices _Dσ,a_ [(] _[i]_ [)] [which] [are] [defined] [up] [to] [translations] [by] [the] _[C]_ _αa_ [.]
Together with _Cαa_, these satisfy an extended positivity constraint of the “loop-positive Grassmannian”, which say that, for any collection of 0 _≤_ _l_ _≤_ _L_ of the _D_ ’s, _D_ [(] _[i]_ [1][)] _, · · ·_ _, D_ [(] _[i][l]_ [)], the
ordered minors of the matrix  










(8.2)













_D_ [(] _[i]_ [1][)]
...
_D_ [(] _[i][l]_ [)]



_C_


are all positive.
Let us turn to extending our topological characterization of the the amplituhedron to
loop level. When we project through _Y_, _Y AB_ projects down to a 2-plane we can call ( _AB_ ).
It is then natural to conjecture the following: projecting through ( _Y AB_ ) the 2-dimensional


                   - 25                    

data should correspond to the _m_ = 2 _,_ ( _k_ + 2) amplituhedron, while projecting through _Y_ we
should end up in the _m_ = 4 _, k_ amplituhedron as usual. As before, we can phrase this in terms
of projections down to the _m_ = 1 amplituhedron, which tells us that for fixed _a_, _b_,


_{_ [( _Y AB_ ) _ai_ ] _}_ has ( _k_ + 2) sign flips for all _a,_ _{_ [ _Y abb_ + 1 _i_ ] _}_ has _k_ sign flips for all _a, b_ (8.3)


Again as before, this has the effect of requiring that [( _Y AB_ ) _ii_ +1] _>_ 0 _,_ [ _Y ii_ +1 _jj_ +1] _>_ 0, and if
we assume these conditions, then it suffices to check the sign flip pattern only through one set
of projections. This leads to the most efficient characterization of the 1-loop amplituhedron
as those ( _Y AB_ ), _Y_ for which


[( _Y AB_ ) _ii_ + 1] _>_ 0 _,_ [ _Y ii_ + 1 _jj_ + 1] _>_ 0 (8.4)

_{_ [( _Y AB_ )12] _, · · ·_ _,_ [( _Y AB_ )1 _n_ ] _}_ has ( _k_ + 2) sign flips (8.5)

_{_ [ _Y_ 1234] _, · · ·_ _,_ [ _Y_ 123 _n_ ] _}_ has _k_ sign flips (8.6)


When there is more than one loop, we have several ( _k_ + 2)-planes ( _Y AB_ ) _γ_, with the _k_ -plane
_Y_ common to all of them. The conditions are exactly the same as the above for each loop
separately. But it is also natural to demand after projecting through any of the ( _AB_ ) _γ_ to
get to a 2-dimensional space, that further projecting through ( _AB_ ) _ρ_ should land us in the
“ _m_ = 0 amplituhedron”, which is just the condition that [ _Y_ ( _AB_ ) _γ_ ( _AB_ ) _ρ_ ] _>_ 0.
Note that this definition gives us an extremely simple picture for the loop amplituhedron.
At one loop, we simply have that the amplituhedron is the intersection of the _m_ = 2 _,_ ( _k_ + 2)
and the _m_ = 4 _, k_ “tree” amplituhedra! That is, ( _Y AB, Y_ ) is in the 1-loop amplituhedron, if
the ( _k_ +2) plane ( _Y AB_ ) is in the _m_ = 2 amplituhedron, with the _k_ -plane _Y_ inside ( _Y AB_ ) is in
the _m_ = 4 amplituhedron. And for any number of loops we have the further intersection with
the “ _m_ = 0” amplituhedron. None of this is obvious from the “( _C, D_ )” picture of the loop
amplituhedron, and this even suggests new approaches to triangulating the amplituhedron.
Consider for example the case of _k_ = 1 _, L_ = 1 _, n_ = 5. In the new picture, we simply
have ( _Y AB_ ) in the _m_ = 2 _, n_ = 5 _, k_ = 3 amplituhedron where it is just the _G_ +(3 _,_ 5) positive
Grassmannian. Now this plane slices through the tree amplituhedron (just the polytope given
by the convex hull of the external data for _k_ = 1). Projectively ( _Y AB_ ) is a plane and the
intersection with this polytope is just a pentagon on this plane. And the point _Y_ on ( _Y AB_ )
is forced to lie inside this pentagon! Note this also suggests a different way of expressing the
loop integrand/amplituhedron form than the usual one coming from BCFW triangulation.
Traditionally for this case we would write the form as “4-form _×_ 4-form”: one 4-form (for
the _Y_ dependence corresponding to the “R-invariant”), multiplied by another 4-form for the
loop ( _AB_ ). In the new picture, it is more naturally expressed as “6 form _×_ 2 form”, where
the 6-form is the canonical form for ( _Y AB_ ) in the _m_ = 2 amplituhedron, and the “2-form”
is the one for _Y_ on ( _Y AB_ ) inside the aforementioned pentagon.
As another example, let us look at the case of _k_ = 0 _, n_ = 5 _, L_ = 2. In the old definition,
we look at two (2 5) “ _D_ ” matrices _D_ 1 _,_ 2. We first have to demand that both _D_ 1 _,_ 2 are
_×_
positive (which means that _AB_ 1 and _AB_ 2 are in the usual 1-loop (same as _m_ = 2 tree)


                   - 26                    

amplituhedron), together with the requirement that all the ordered (4 _×_ 4) minors of the
(4 5) matrix stacking ( _D_ 1 _, D_ 2), are positive. This certaily implies that ( _AB_ )1( _AB_ )2 _>_ 0,
_×_ _⟨_ _⟩_
but seems to demand even more. However, our new claim is that, once ( _AB_ )1 _,_ ( _AB_ )2 are in
the 1-loop amplituhedron, then demanding ( _AB_ )1( _AB_ )2 _>_ 0 is enough to enforce being in
the 2-loop amplituhedron.
It is straightforward to check this picture by computing the full 2-loop amplitude, but in
order to illustate the methods in a simpler non-trivial example, let us compute a “cut” of the
2-loop _n_ = 5 amplitude where _⟨AB_ 12 _⟩→_ 0, and _⟨CD_ 34 _⟩_ = 0 _, ⟨CD_ 45 _⟩_ = 0. For simplicity
we use positive data where _Z_ 5 = _−Z_ 4 + _Z_ 3 _−_ _Z_ 2 + _Z_ 1 and also normalize _⟨Z_ 1 _Z_ 2 _Z_ 3 _Z_ 4 _⟩_ = 1.
Given the 3-term triangulation of the 1-loop amplituhedron, it is easy to see that on this cut
_CD_ only belongs to a single cell, and can be put in the form _C_ = _Z_ 3 + _uZ_ 4 _, D_ = _Z_ 4 + _vZ_ 5
with _u, v_ _>_ 0. There are two one-loop cells which cover _⟨AB_ 12 _⟩_ = 0; so just demanding that
( _CD_ ) _,_ ( _AB_ ) are in the 1-loop amplituhedra tells us we can parametrize







_C_ = _Z_ 3 + _uZ_ 4 _, D_ = _Z_ 4 + _vZ_ 5 _, A_ = _Z_ 1 + _xZ_ 2 _, B_ =




_Z_ 3 + _yZ_ 2 + _zZ_ 4
_−Z_ 1 + _αZ_ 4 + _βZ_ 5



; _u, v, x, y, z, α, β_ _>_ 0



(8.7)
Now in each of these cells, we have the additional condition that _⟨ABCD⟩_ _>_ 0. For instance
in the first cell, we have



_⟨ABCD⟩_ = (1 + _v_ ) _y_ + _uv_ (1 + _x_ + _y_ ) _−_ _v_ (1 + _x_ ) _z_ _>_ 0 (8.8)


and thus we have the inequalities


_x, y, u, v_ _>_ 0 _,_ 0 _< z_ _<_ [(1 +] _[ v]_ [)] _[y]_ [ +] _[ uv]_ [(1 +] _[ x]_ [ +] _[ y]_ [)] (8.9)

_v_ (1 + _x_ )


and the corresponding form is







Ω [(1)] = _[dx]_




_[dx]_ _dy_

_x_ _y_



_dy_ _du_

_y_ _u_



_dv_
_u_ _v_



_v_ _[dz]_



_z_ _v_ (1+ _x_ )
_−_ [(1+] _[v]_ [)] _[y]_ [+] _[uv]_ [(1+] _[x]_ [+] _[y]_ [)]



 [1]




[1] 1

_z_ _[−]_ _z −_ [(1+] _[v]_ [)] _[y]_ _v_ [+]



_v_ (1+ _x_ )






 (8.10)



Exactly the same exercise for the second cell gives us the inequalities


_x, β, u, v_ _>_ 0 _,_ 0 _< α <_ _[x]_ [(1 +] _[ v]_ [ +] _[ v]_ [) +] _[ β]_ [(1 +] _[ x]_ [)] (8.11)

_v_ (1 + _x_ )



and the form







Ω [(2)] = _[dx]_



_dβ_
_x_ _β_



_du_
_β_ _u_



_dv_
_u_ _v_



_v_ _[dα]_



_α_ _v_ (1+ _x_ )
_−_ _[x]_ [(1+] _[v]_ [+] _[v]_ [)+] _[β]_ [(1+] _[x]_ [)]



 [1]




[1] 1

_α_ _[−]_ _α −_ _[x]_ [(1+] _[v]_ _v_



_v_ (1+ _x_ )






 (8.12)



Now we simply add the two forms. Of course since we have used different variables to
parametrize _B_ in the two cells, we have to make the co-ordinate change between them. We can
always expand _B_ as either _B_ = _Z_ 3+ _yZ_ 2+ _zZ_ 4 or as _B_ = _−Z_ 1+ _αZ_ 4+ _βZ_ 5 (of course in general


                   - 27                    

with no sign restriction on _y, z, α, β_ ). Mathcing ( _AB_ ) in these two co-ordinates gives us the
relationship between the parameters as _α_ = _−x/_ (1+ _x_ + _y_ ) _, β_ = _x_ (1+ _z_ ) _/_ (1+ _x_ + _y_ ). Inserting
this into the expression for Ω [(2)] and adding Ω [(1)] gives an expression for Ω= Ω [(1)] + Ω [(2)] :


Ω= _dxdydzdudv_ _[uv]_ [(1 +] _[ x]_ [ +] _[ y]_ [)(1 +] _[ x]_ [ +] _[ y]_ [ +] _[ z]_ [ +] _[ xz]_ [) +] _[ y]_ [(1 +] _[ x]_ [ +] _[ y]_ [ +] _[ v]_ [(1 +] _[ x]_ [ +] _[ y]_ [) +] _[ z]_ [(1 +] _[ x]_ [)]

_uvxy_ (1 + _x_ + _y_ ) _z_ (1 + _z_ )((1 + _v_ ) _y_ + _uv_ (1 + _x_ + _y_ ) _−_ _v_ (1 + _x_ ) _z_ )
(8.13)
This expression precisely (and highly non-trivially) matches the corresponding cut of the
2-loop amplitude.
Our new description of the full amplituhedron for both trees and loops now has a satisfyingly strong resonance with three central aspects of scattering amplitude physics. The
“ _m_ = 0” part of the geometry is about understanding the geometry of mutual positivity
between loops ( _AB_ ) _γ_ ( _AB_ ) _ρ_ _>_ 0; this is present even for the simplest case of _k_ = 0 _, n_ = 4,
_⟨_ _⟩_
and is associated with the physics of the universal IR divergences and the cusp-anomalous
dimension. The “ _m_ = 4” part of course has to do with the physics of tree amplitudes. Finally
the “ _m_ = 2” part is the physics of the leading quantum corrections.


**9** **The** **Amplituhedron** **in** **Twistor** **Space**


As we have remarked, it is striking that our new picture of the amplituhedron makes reference
only to what the configuration of _Z_ ’s looks like after projecting the ( _k_ + _m_ )-dimensional _Z_ data
through _Y_ . For the case of relevance to scattering amplitudes with _m_ = 4, this means that
everything can be described as a property of the configuration of bosonic momentum-twistor
data! This is pleasing, since from a physical point of view, while the _m_ = 4-dimensional
momentum-twistors have a manifest importance as specifying the external kinematical data,
the introduction of the extra _k_ components of the _Z_ ’s, and the _k_ -plane _Y_, is more mysterious, related to a “bosonization” of the supersymmetry. This structure is needed since the
canonical amplituhedron form lives in _Y_ space, and the super-amplitude is extracted from it

[5]. But given that our new definition of the amplitude seems to make reference only to the
_m_ -dimensional space, it would be very pleasing if the geometry of the amplituhedron as well
as the superamplitude could be directly associated with the _m_ -dimensional space, without
ever referring to _Y_ or the underlying ( _m_ + _k_ ) dimensional _Z_ data.
This is very easy to do. We are working with the configuration space _M_ ( _m, n_ ) of _n_
vectors _Za_ in _m_ dimensions. Let us define the subspace of ( _m, n_ ) where the configuration
_M_
has the correct “winding” or “flip” pattern we have discussed earlier appropriate to some _k_
as _W_ ( _k, m, n_ ) _⊂M_ ( _m, n_ ). Now, the space _M_ ( _m, n_ ) is _m × n_ dimensional, and the subset
_W_ ( _k, m, n_ ) is clearly a top-dimensional subspace and is also _m_ _×_ _n_ dimensional. On the other
hand, the amplituhedron is _k × m_ dimensional and has lower dimension. We would thus like
to identify subspaces in _M_ ( _m, n_ ) that can be obtained from some fixed ( _m_ + _k_ ) dimensional
data _a_ by projecting though some _k_ -plane _Y_ .
_Z_
But this is both natural and trivial. Suppose we begin with some fixed set of vectors
_Z∗a_ that give us a point in ( _m, n_ ). We can think of this as giving as a fixed _m_ -plane _Z∗_
_M_


                   - 28                    

in _n_ dimensions. Now, let us consider the affine subspace which are linear translates of this
_m_ -plane, by translating in directions lying in some fixed _k_ -plane ∆in _n_ dimensions.

















In equations, we look at the space of all _Za_ _[i]_ [that] [can] [be] [obtained] [starting] [from] _[Z]_ _∗_ _[i]_ _a_ [and]
translating in the direction of ∆ _[α]_ _a_ [,] [i.e.] [all] _[Z]_ _a_ _[i]_ [of] [the] [form]

_Za_ _[i]_ [=] _[ Z]_ _∗_ _[i]_ _a_ [+] _[ y]_ _α_ _[i]_ [∆] _[α]_ _a_ (9.1)



(Here _i_ = 1 _, · · ·_ _, m_ is the vector index on the _m−_ dimensional space).
Note that such a subspace is specified by giving a ( _k_ + _m_ ) _× n_ matrix of data,







_Za_ _[I]_ [=]




_Z∗_ _[i]_ _a_
∆ _[α]_ _a_



(9.2)



which is what we think of as “fixed external data” in the usual amplituhedron story. Here the
index _I_ runs from _I_ = 1 _, · · ·_ _,_ ( _k_ + _m_ ); we can think of the first _m_ components as corresponding
to the _i_ indices and the last _k_ components as corresponding to the _α_ indices. Furthermore, the
_Za_ above are precisely what we get by projecting the ( _k_ + _m_ )-dimensional _a_ data through
_Z_
the _k_ -plane _Yα_ _[I]_ [in] [(] _[k]_ [ +] _[ m]_ [)] [dimensions,] [where]

_Yα_ _[I]_ [=] _[i]_ = _yα_ _[i]_ _[,]_ _[Y]_ _α_ _[I]_ [=] _[β]_ = _δα_ _[β]_ (9.3)
_−_

Thus from the _m_ -dimensional point of view, specifying ( _k_ + _m_ )-dimensional data is actually picking out a particular translation of the subspace of _M_ ( _m, n_ ) from a _k × m_ space
of possible translations. We can refer to this translation of _M_ ( _m, n_ ) as the affine subspace
_Y_ [ _Z_ ].
For any of these affine subspaces, we can look at the part of the subspace which is compatible with the correct winding/flip pattern, and gives us the _m_ -dimensional characterization
of the amplituhedron _m,k,n_ [ ]:
_A_ _Z_

_m,k,n_ [ ] = [ ] [ _m, k, n_ ] (9.4)
_A_ _Z_ _Y_ _Z_ _∩W_


                   - 29                    

In this picture, there is one last vestige of the ( _k_ + _m_ ) dimensional picture–we must
demand that this affine subspace be “positive” in the sense that all the ordered minors of the
_Z_ matrix are positive. It is interesting to ask the extent to which we can remove even this
restriction. To begin with we can ask the following obvious question. Suppose we have some
_m_ -dimensional configuration of _Z_ ’s satisfying the right winding condition. Is it guaranteed
that we can think of having obtained this data by projecting _positive_ ( _k_ + _m_ )-dimensional
data through some _k_ -plane _Y_ ? Said more prosaically: given some ( _m_ _n_ ) matrix of _Za_ ’s
_Z_ _×_
that satisfies the winding/flip criteria, can we always add _k_ more rows so that the resulting
( _k_ + _m_ ) _× n_ matrix is positive?
While we do not have a general proof of this statement, we suspect that the answer is
likely “yes”. A sketch of an approach to a proof might be the following, setting _m_ = 2 for
simplicity. We’d like to show that whatever _m_ = 2 dimensional data we have with correct
winding, we can uplift it to positive ( _k_ + 2) dimensional data. Now, if we have two different
collections of _Zi_ with the same orientation for the windings for both curves, then we should
be able to smoothly deform one configuration into the other. If the orientations of each
segment ( _ii_ + 1) are also the same, then it seems plausible that such a deformation can be
generated by a combination of elementary moves on the vertices _Zi_ : rescaling _Zi_ by a positive
constant, or moving _Zi_ in the direction of either of its neighbors; i.e. a series of operations
of the form _Zi_ _→_ _xiZi_ + _xi−_ 1 _Zi−_ 1 + _xi_ +1 _Zi_ +1. But these moves on the projected _Zi_ follows
under projection from exactly the same operation on the _Z_ ’s in the ( _k_ +2)-dimensional space
_Zi_ _→_ _xiZi_ + _xi−_ 1 _Zi−_ 1 + _xi_ +1 _Zi_ +1, and this operation preserves the positivity of the _Z_ data.
Finally this picture clearly extends to all loop orders. For the case _m_ = 4 of relevance
to scattering amplitudes, aside from the _Za_ we also have _L_ planes ( _AB_ ) _α_ which are 2-planes
in 4-dimensions. We can define _W_ ( _m_ = 4 _, k, n_ ; _L_ ) _⊂M_ ( _m_ = 4 _, k, n_ ) _×_ ( _AB_ ) _[L]_ as that subset
that has the correct winding properties at loop level. Then, the loop-level amplituhedron is


                 _m_ =4 _,k,n_ [ ] = [ ] ( _AB_ ) _[L]_ [�] [ _m_ = 4 _, k, n_ ; _L_ ] (9.5)
_A_ _Z_ _Y_ _Z_ _×_ _∩W_


**10** **(Super)-Amplitudes** **As** **Differential** **Forms** **on** **Twistor** **Space**


Having seen the _m_ -dimensional image of the amplituhedron without any reference to _Y_,
let us go further and discuss how to think about the canonical form and the scattering
(super)-amplitude in an intrinsically _m_ -dimensional way—as we will see the super-amplitude
is _literally_ a degree _m × k_ differential form on the configuration space _M_ ( _m, n_ ) of the _m_ dimensional _Za_ ’s. Before showing how this works in generality, let’s start with a simple
example familiar from the simplest scattering amplitudes with _m_ = 4 _, k_ = 1, which are built
out of the well-known “ _R_ -invariants”. Let’s first describe the _R_ -invariant in standard terms,
as a super-amplitude, which we can write as

(12345) = _[δ]_ [4][ (] _[⟨]_ [1234] _[⟩][η]_ [5][ + cyclic)] (10.1)

_⟨_ 1234 _⟩· · · ⟨_ 5123 _⟩_


                   - 30                    

Now in the language of the amplituhedron, we instead talk about a 4-form with logarithmic
singularities on _Y_ space, that is



Ω( _Y,_ _a_ ) = _dY_ log [[] _[ Y]_ [ 1234]]
_Z_ [ _Y_ 5123]




[[] _[ Y]_ [ 1234]]

[ _Y_ 5123] [ _Y_ 5123]

_[· · ·][ d][Y]_ [ log] [[] _[ Y]_ [ 4512]]




[[] _[ Y]_ [ 4512]] [ _Y d_ [4] _Y_ ] [ 12345] [4]

[ _Y_ 5123] [=] [ _Y_ 1234] [ _Y_



(10.2)

[ _Y_ 1234] _· · ·_ [ _Y_ 5123]



Here the subscript on _dY_ is to remind us that we are to take the external data as fixed,
with the differentials acting on _Y_ . Starting from this form there is a simple prescription for
extracting the superamplitude, but we will present a more direct and striking connection.
Note that of course all the brackets occurring as arguments of the dlog’s above contain _Y_ ;
thus we can interpret them all as 4-brackets on the space of momentum-twistors obtained
when projecting through _Y_ . It is then very natural to look at a 4-form, not on _Y_ space, but
on momentum-twistor space, as



Ω( _Za_ ) = _dZ_ log _[⟨]_ [1234] _[⟩]_




_[⟨]_ [1234] _[⟩]_

_⟨_ 5123 _⟩_ _[· · ·][ d][Z]_ [log] _[⟨]_ _⟨_ 5123 [4512] _[⟩]_ _⟩_



(10.3)
_⟨_ 5123 _⟩_



Now, one can directly verify that this form can be re-written as

Ω( _Za_ ) = _[δ]_ [4][ (] _[⟨]_ [1234] _[⟩][dZ]_ [5][ + cyclic)] (10.4)

_⟨_ 1234 _⟩· · · ⟨_ 5123 _⟩_

Note that remarkably, this is precisely the _R_ -invariant, if the (anti-commuting) super-variables
_ηa_ _[I]_ [are] [replaced] [by] [the] [differentials] _[η]_ _a_ _[I]_ _[→]_ _[dZ]_ _a_ _[I]_ [!] [We] [will] [shortly] [understand] [why] [this] [happens]
on general grounds, but let us first make some general comments.
Suppose we have some _m×k_ form on the Grassmannian, and let us consider the pull-back
of this form to some _m×k_ dimensional subspace of _G_ ( _k_ + _m, n_ ). We can describe this by some
_Cαa_ ( _x_ 1 _,_ _, xm×k_ ). Now, consider those _k_ -planes that are constrained by being orthogonal
_· · ·_
to some _m_ -plane, _Z_ ; this will generically intersect the subspace in points; concretely we are
just saying that the equations


_Cαa_ ( _xi_ ) _Za_ _[I]_ [= 0] _[,]_ [has] [solutions] _[x][i]_ [=] _[ x][i]_ [(] _[Z][a]_ [)] (10.5)



We would like to push forward any form from the Grassmannian onto _Za_ space, in other
words we would like to re-write the measure _dx_ 1 _dxm×k_ in terms of the wedge products of
_· · ·_
_m_ _k_ of the _dZa_ ’s. The result is simple; we will show that
_×_




       _dx_ 1 _· · · dxm×k_ = _dy_ 1 _· · · dym×k δ_ _[m][×][k]_ [ _Cαa_ ( _y_ ) _Za_ ] _δ_ _[m][×][k]_ [ _CαadZa_ ]




 = _dy_ 1 _· · · dym×k δ_ _[m][×][k][|][m][×][k]_ [ _Cαa_ ( _y_ ) **Z** _a_ ] with _ηa_ _[I]_ _[→]_ _[dZ]_ _a_ _[I]_ (10.6)



The proof is easy. Let’s start with taking the differential of _CαaZa_ _[I]_ [= 0,] [to] [find]


_∂Cαa_

_Za_ _[I]_ _[dx][i]_ [=] _[ −][C][αa]_ [(] _[x]_ [)] _[dZ]_ _a_ _[I]_ (10.7)
_∂xi_


                   - 31                    

Taking the _m × k_ power of both sides we find



det _{αI,i}_




_∂Cαa_ ( _x_ )
_∂xi_ _Za_ _[I]_




_dx_ 1 _dxm×k_ = _δ_ _[m][×][k]_ ( _CαadZa_ ) (10.8)
_· · ·_



so that




       _dx_ 1 _dxm×k_ = det _{αI,i}_
_· · ·_




_∂Cαa_ ( _x_ )
_∂xi_ _Za_ _[I]_



�� _−_ 1
_δ_ _[m][×][k]_ ( _Cαa_ ( _x_ ) _dZa_ )
_×_




 = _dy_ 1 _· · · dym×k δ_ _[m][×][k]_ [ _Cαa_ ( _y_ ) _Za_ ] _δ_ _[m][×][k]_ [ _CαadZa_ ] (10.9)



as desired.
Thinking of the canonical amplituhedron forms instead as _m_ _×_ _k_ forms on the _m_   dimensional space of _Za_ data exposes some remarkable relationships between forms that are
not evident from the conventional _Y_ -space picture. Let us return to the _m_ = 2 amplituhedron
for which we gave a triangulation and determined the form in section 7. We can re-interpret
these� as forms on the space of 2-dimensional vectors _Za_ . For _k_ = 1, from the triangulation
_i_ [(1] _[ii]_ [ + 1)] [of] [the] [polygon] [we] [have]




  Ω _k_ =1 _,m_ =2 =


_i_



( _Z_ 1 _Zi_ _dZi_ +1 _Z_ 1 _Zi_ +1 _dZi_ + _ZiZi_ +1 _dZ_ 1) [2]
_⟨_ _⟩_ _−⟨_ _⟩_ _⟨_ _⟩_ (10.10)

_Z_ 1 _Zi_ _Z_ 1 _Zi_ +1 _ZiZi_ +1
_⟨_ _⟩⟨_ _⟩⟨_ _⟩_



But there is now a beautifully simple expression for the 2 _× k_ form for any _k_, we have

Ω _[k]_ _k_ =1 _,m_ =2
Ω _k,m_ =2 = (10.11)

_k_ !


This understanding of the scattering amplitude as a differential form obviously extends
to loop level as well. In addition to the external twistor data _Za_, we also have _L_ 2-planes
( _AB_ ) _α_, and we have a 4 ( _k_ + _L_ ) form on _Za,_ ( _AB_ ) _α_ space. Note that in this setting “the
_×_ _{_ _}_
loop integrand” is just one component of the 4( _k_ + _L_ ) form. For instance, even the simplest
_n_ = 4 1-loop amplitude corresponds to the 4-form



_d_ log _[⟨][AB]_ [12] _[⟩]_




_[⟨][AB]_ [12] _[⟩]_

_⟨AB_ 13 _⟩_ _[· · ·][ d]_ [log] _[⟨]_ _⟨_ _[AB]_ _AB_ [14] 13 _[⟩]_ _⟩_



= (10.12)
_⟨AB_ 13 _⟩_



_⟨ABd_ [2] _A⟩⟨ABd_ [2] _B⟩⟨_ 1234 _⟩_ [2]




[2] _A_ _ABd_ [2] _B_ 1234
_⟩⟨_ _⟩⟨_ _⟩_ [2] + +

_AB_ 12 _AB_ 14 _· · ·_ _[⟨][AB]_ [12] _[⟩]_ [2] _[⟨][ABdZ]_ _AB_ 12 [3] _[dZ]_ [3] _[⟩⟨][ABdZ]_ _AB_ 14 [4] _[dZ]_ [4] _[⟩]_ [+] _[ · · ·]_
_⟨_ _⟩· · · ⟨_ _⟩_ _⟨_ _⟩· · · ⟨_ _⟩_



(10.13)
_⟨AB_ 12 _⟩· · · ⟨AB_ 14 _⟩_



The first terms, where all 4 _d_ ’s hit ( _AB_ ), is the familiar 1-loop integrand; then we have terms
with a mixture of _d_ ’s hitting the ( _AB_ ) and the _Za_, and the last term, where the _d_ ’s hit only
the _Za_ .
Our new picture of scattering amplitudes as differential forms is very satisfying. The
“super”-part of superamplitudes has always presented an obstruction between linking properties of the integrand on the one hand, and the final integrated amplitudes on the other.
In particular, recent years has seen a fascinating emergence of cluster algebra structure in


                   - 32                    

the polylogarithms found in _N_ = 4 SYM amplitudes—the arguments of the polylogs are
expressed as cross-ratios of momentum twistor data [18] naturally associated with cluster
algebras [19, 20] for the external kinematical data in _M_ (4 _, n_ ). This has long cried out for a
link with the positive Grassmannian/amplituhedron structure at the level of the integrand,
but the “ _η_ ”’s in superamplitudes obscure this connection. The bosonization of the integrand
afforded by the amplituhedron improves the situation, but leaves us with external data that
is (4 + _k_ ) dimensional while obviously the cluster structure in integrated results only knows
about 4-dimensional momentum twistor data. But finally with the new picture of amplitudes
as forms, integrand and amplitudes are on a fully equal footing, depending on the same variables. As we have seen, however, the “positive geometry” associated with external data in the
4-dimensional space is not merely “positivity”, but involves further combinatorial/topological
“winding/flip” criteria. It will be fascinating to understand how these may be reflected in
the transcendental functions appearing after loop integration.


**11** **Parity**


Parity is a fundamental symmetry of scattering amplitudes which is conventionally completely obscured in momentum-twistor space. The bosonic action of the symmetry is easy to
see: given momentum twistors _Za_ _[I]_ [,] [we] [have] [the] [parity] [conjugates] _[W][aI]_ [which] [are] [the] [planes]
( _Za−_ 1 _ZaZa_ +1); with an additional factor of ( 1) for _a_ = 1 and _a_ = _n_ . Now, for the full

_−_
scattering amplitudes labeled by ( _n,_ [�] _k_ ), parity interchanges [�] _k_ _↔_ ( _n_ [�] _−_ _k_ ); but in terms of _k_
this is the rather more peculiar looking interchange of _k_ _↔_ ( _n −_ _k −_ 4), which presumably
reflects a symmetry _k_ _↔_ ( _n_ _−_ _k_ _−_ _m_ ) for general _m_ . As we will now see, our “winding” picture
gives a beautifully simple understanding of these symmetries.
The are in fact two different Z2 symmetries that in concert give us the physical parity.
The first one is extremely simple but already shows strikingly why a _k_ _↔_ ( _n−m−k_ ) symmetry
should be expected. Suppose we simply change _Za_ ( 1) _[a]_ _Za_ i.e. we flip the sign of ever
_→_ _−_
other _Z_ . Now consider (e.g. for _m_ = 2) the sequence _{⟨_ 12 _⟩, ⟨_ 13 _⟩, · · · ⟨_ 1 _n⟩}_ . Note that the
number of possible positions of sign-flips of this sequence is ( _n_ _−_ 2), and is ( _n_ _−_ _m_ ) for general
_m_ . Now, obviously if two consecutive signs agree before this transformation, they will disagree
afterwards, and vice-versa. So this changes the number of sign flips from _k_ _→_ ( _n −_ _m −_ _k_ )!
This is a rather trivial Z2 which knows nothing about the _Wa_ . There is a more non-trivial
fact featuring the _Wa_ : if the _Z_ ’s are in the amplituhedron, i.e. that _ii_ +1 _jj_ +1 _>_ 0 and the
_⟨_ _⟩_
sequence _{⟨_ 1234 _⟩, · · ·_ _, ⟨_ 123 _n⟩}_ has _k_ sign flips, then the _W_ ’s are _also_ in the amplituhedron
with the same value of _k_ !
First note that as long as _ZiZi_ +1 _ZjZj_ +1 _>_ 0, then also _WiWi_ +1 _WjWj_ +1 _>_ 0, since
_⟨_ _⟩_ _⟨_ _⟩_


_WiWi_ +1 _WjWj_ +1 = _ZiZi_ +1 _ZjZj_ +1 _Zi−_ 1 _ZiZi_ +1 _Zi_ +2 _Zj−_ 1 _ZjZj_ +1 _Zj_ +2 (11.1)
_⟨_ _⟩_ _⟨_ _⟩⟨_ _⟩⟨_ _⟩_


Note that for this conclusion we don’t have to assume that all the minors of these _Z_ ’s are
positive (which they aren’t!), only that the minors of the form _⟨aa_ + 1 _bb_ + 1 _⟩_ _>_ 0.


                   - 33                    

Now, we only have to show that the sequence _W_ 1 _W_ 2 _W_ 3 _W_ 4 _,_ _W_ 1 _W_ 2 _W_ 3 _W_ 5 _,_ _W_ 1 _W_ 2 _W_ 3 _Wn_
_{⟨_ _⟩_ _⟨_ _⟩_ _· · · ⟨_ _⟩}_
has _k_ sign flips. A short computation of these four brackets turns this into the pretty statement that the sequence


_{⟨_ 1(234) _⟩, ⟨_ 1(345) _⟩, · · ·_ _, ⟨_ 1( _n −_ 2 _n −_ 1 _n_ ) _⟩}_ has _k_ sign flips (11.2)


This statement is easy to prove. Let us consider the following sequences of minors



_⟨_ 1234 _⟩⟨_ 1235 _⟩⟨_ 1236 _⟩· · ·_ _⟨_ 123 _n⟩_
_⟨_ 1234 _⟩⟨_ 1345 _⟩⟨_ 1346 _⟩· · ·_ _⟨_ 134 _n⟩_
_⟨_ 1234 _⟩⟨_ 1345 _⟩⟨_ 1456 _⟩· · ·_ _⟨_ 145 _n⟩_
... ... ... ...

_· · ·_
_⟨_ 1234 _⟩⟨_ 1345 _⟩⟨_ 1456 _⟩· · ·_ _⟨_ 1( _n −_ 2 _n −_ 1 _n_ ) _⟩_



(11.3)



The first row is our usual sequence _{⟨_ 123 _i⟩}_, which has _k_ sign flips. The second row has the
same first entry as the first row, and thereafter is of the form _⟨_ 134 _i⟩_ . The third row has the
same first two entries as the second row, and is thereafter of the form _⟨_ 145 _i⟩_, and so on. Now
it is easy to see that the number of sign flips of the _i_ ’th and ( _i_ + 1)’st rows must be the same.
The first parts of the two rows coincide; thereafter the argument is exactly the same as what
we used to show that the number of sign flips for the _m_ = 2 amplituhedron is independent of
the point we project through, namely, that by Plucker, we know that either there are no sign
flips in successive slots, or both flip, or if the top row flips, the next slot where a flip occurs
just in one row, it must occur in the bottom row. Since we know that all the last entries are
of the form _⟨ii_ + 11 _n⟩_ and thus have a fixed sign, this means that the number of sign flips
must be equal. In this way we work our way from the top to bottom rows, and conclude that
the sequence _{⟨_ 1(234) _⟩, ⟨_ 1(345) _⟩, · · ·_ _, ⟨_ 1( _n −_ 2 _n −_ 1 _n_ ) _⟩_ has _k_ sign flips, as desired.
The statement of parity at loop level is more interesting. Let’s work at one-loop to begin
with. We know that when we project through _AB_, the sequence _⟨AB_ 12 _⟩, ⟨AB_ 13 _⟩, · · ·_ _, ⟨AB_ 1 _n⟩_
should have _k_ + 2 sign flips. Now, we would like to see what happens when we dualize the _Zi_
to _Wi_ ; our claim is that loop-level parity is the statement that the sequence


_ABW_ 1 _W_ 2 _,_ _ABW_ 1 _W_ 3 _,_ _ABW_ 1 _Wn_ has _k_ sign flips (11.4)
_{⟨_ _⟩_ _⟨_ _⟩· · ·_ _⟨_ _⟩}_


In general, we can expand


_ABW_ 1 _Wj_ = _ABn_ 1 2 _j_ 1 _jj_ + 1 _ABn_ 2 1 _j_ 1 _jj_ + 1 + _AB_ 12 _nj_ 1 _jj_ + 1 _._ (11.5)
_⟨_ _⟩_ _⟨_ _⟩⟨_ _−_ _⟩−⟨_ _⟩⟨_ _−_ _⟩_ _⟨_ _⟩⟨_ _−_ _⟩_


If we want to write this back with _Y_ ’s, we have to add a _Y_ to both sets of brackets,

[ _Y ABn_ 1] [ _Y_ 2 _j_ _−_ 1 _jj_ + 1] _−_ [ _Y ABn_ 2] [ _Y_ 1 _j_ _−_ 1 _jj_ + 1] + [ _Y AB_ 12] [ _Y nj_ _−_ 1 _jj_ + 1] . The
claim is that this sequence should have _k_ sign flips. For _k_ = 0, this is the statement that all
_ABW_ 1 _Wi_ are positive, a statement we will say more about in section 14. We don’t have a
_⟨_ _⟩_
proof for general _k_, though we have checked these statements numerically for a large range
of _k, n, L_ .


                   - 34                    

**12** **Different** **winding** **sectors,** _M × M_ **and** **Correlation** **Functions**

Given that the amplituhedron has maximal winding, it is natural to ask whether there is
any meaning to sectors with different winding/flip patterns. Let us start again with the
case of _m_ = 2, _k_ = 2. The amplituhedron corresponds to winding number 1, but is there
some meaning to the sector where we still have [ _Y ii_ + 1] _>_ 0 but where we have winding
number 0? The interpretation of the _m_ = 2 amplitudes as the 1-loop integrand for the MHV
amplitudes suggests an obvious candidate. We know that by parity we can replace _Za_ with
_Wa_ = ( _Za−_ 1 _ZaZa_ +1); doing this takes us from the integrand for MHV amplitudes to that
for MHV amplitudes. So it is natural to conjecture that the canonical form associated with
winding 0 sector corresponds to the MHV 1-loop integrand. We have verified empirically that
this is correct, by identifying the MHV integrand with the canonical form with logarithmic
singularities on the minimally winding space. The forms are of course different, for instance
for _n_ = 5 we have


MHV = (12.1)
_M_ _[⟨][AB]_ [(512)] _[ ∩]_ [(234)] _AB_ _[⟩⟨]_ [3451] 12 _[⟩−⟨]_ _AB_ _[AB]_ 23 [51] _AB_ _[⟩⟨]_ [1234] 34 _AB_ _[⟩⟨]_ [2345] 45 _[⟩−⟨]_ _AB_ 51 _[AB]_ [34] _[⟩⟨]_ [4512] _[⟩⟨]_ [5123] _[⟩]_

_⟨_ _⟩⟨_ _⟩⟨_ _⟩⟨_ _⟩⟨_ _⟩_

while

~~_M_~~ MHV = _[⟨][AB]_ [13] _[⟩⟨]_ [2345] _[⟩⟨]_ [4512] _AB_ 12 _[⟩−⟨]_ _AB_ _[AB]_ 23 [51] _[⟩⟨]_ _AB_ [1234] 34 _[⟩⟨]_ _AB_ [2345] 45 _[⟩−⟨]_ _AB_ _[AB]_ 51 [34] _[⟩⟨]_ [4512] _[⟩⟨]_ [5123] _[⟩]_ (12.2)

_⟨_ _⟩⟨_ _⟩⟨_ _⟩⟨_ _⟩⟨_ _⟩_

It is interesting to note a feature of the geometry also reflected in the forms. The winding
number 1 and 0 regions are _almost_ disjoint, in the sense that they don’t touch on co-dimension
one boundaries. Only when we go to higher-dimensional boundaries that correspond to
collinear regions do the two regions touch. This is reflected in the forms: while both forms
have the same “physical poles”, the forms are different, and the residues on the co-dimension
one boundaries are also different. But upon taking enough residues and going to high enough
co-dimension boundaries, the forms match when the shared boundaries match.
We can continue in this way to discuss any number of loops, still with _k_ = 0. When
projecting through each ( _AB_ ) _i_, we either get winding number 0 or 1. If we define the all-loop
integrand for MHV and MHV amplitudes to be _M_, written in a loop expansion as

_M_ = 1 + _g_ [2] _M_ 1 + _g_ [4] _M_ 2 + _· · ·_ _,_ _M_ = 1 + _g_ [2] _M_ 1 + _g_ [4] _M_ 2 + _· · ·_ (12.3)

then


_MM_ = 1 + _g_ [2] ( _M_ 1 + _M_ 1) + _g_ [4] ( _M_ 2 + _M_ 2 + _M_ 1 _M_ 1 + _M_ 1 _M_ 1) + _· · ·_ (12.4)

At each loop order, we are adding over all the possible winding numbers, and thus _M × M_
is naturally decomposing the space defined simply by the boundary inequalities


( _AB_ ) _jii_ + 1 _>_ 0 _,_ ( _AB_ ) _i_ ( _AB_ ) _j_ _>_ 0 (12.5)
_⟨_ _⟩_ _⟨_ _⟩_

into the pieces with different winding numbers. It is interesting to note that at 1-loop there
is a well-defined form with logarithmic singuarties on these boundaries. Interestingly, it does


                   - 35                    

not correspond to the parity even _sum_ of the MHV and MHV integrands,but to the parity
odd difference between them, which vanishes for _n_ = 4 but is non-vanishing for higher _n_ .
It is interesting that this space defined by the “obvious physical boundaries” inequalities
has a nice physical interpretation. Indeed we began our investigations in this paper by noting
that the space we get simply from imposing the obvious physics boundaries


[ _Y ii_ + 1 _jj_ + 1] _>_ 0 _,_ [ _Y_ ( _AB_ ) _αii_ + 1] _>_ 0 _,_ [ _Y_ ( _AB_ ) _α_ ( _AB_ ) _β_ ] _>_ 0 (12.6)


does not give us the amplituhedron, but it may find a natural meaning related to the “square”
of the amplitude, and simplified even further, to correlation functions. Indeed recent years
have seen a beautiful connection between amplitudes and the light-like limit of stress-tensor
correlators in = 4 SYM. For MHV amplitudes, it is natural to think of the lines ( _ZiZi_ +1)
_N_
and the loops ( _AB_ ) on the same footing; we can indeed think of a collection of lines 1 _,···,n_ + _L_ .
_L_
Going to the light-like limit simply picks _n_ of these lines _i_ out and asks _a_ to intersect _a_ +1
_L_ _L_ _L_
cyclically. The correlation function itself is however a fully permutation invariant function of
all the _i_ . It is therefore tempting to associate the geometry _i_ _j_ _>_ 0 with the correlation
_L_ _⟨L_ _L_ _⟩_
function. For general _k_, we can do the same thing; we consider some number of ( _k_ +2)-planes
in ( _k_ + 4) dimensions ( _Y_ _i_ ) for _i_ = 1 _,_ _,_ ( _n_ + _L_ ), which overlap on _Y_, in such a way the
_L_ _· · ·_
planes are “mutually positive”

[ _Y_ _i_ _j_ ] _>_ 0 (12.7)
_L_ _L_

This is a perfectly well-defined space, but the crucial question is, how can we associate
a form with this geometry to reproduce the correlation functions? An inspection of the
correlators themselves shows that they do not have logarithmic singularities—upon taking
residues we encounter double-poles that ruin the logarithmic property. It would be fascinating
to nonetheless find _some_ way of associating a form with this space. One obvious strategy is
simply to ask the form to become logarithmic in the lightlike limit, where we know that the
geometry does decompose into different winding sectors with well-defined forms associated
with the square of the amplitude _M_ [2] . But it would be much more satisfying if this could be
done more intrinsically; see [21] for some interesting attempts along these lines. Obviously
any such picture must contain all the intricate information associated with the topology of
the amplituhedron.
There are a number of other interesting objects closely related to the amplitudes and the
amplituhedron canonical form. For instance we saw that for _m_ = 2, the canonical form for
any _k_ is the _k_ ’th power of the form for _k_ = 1; while this doesn’t hold true for _m_ = 4, we have
nonetheless observed this “ _k_ ’th power form” is interesting, for instance it non-trivially has
only simple poles. Even more interestingly, at loop level we have the natural “ratio function”
which is the ratio _n,k,L/_ _n,k_ =0 _,L_ . Might any of these objects be associated with different
_M_ _M_
winding sectors?


                   - 36                    

**13** **A** **“Dual”** **of** **the** **Amplituhedron**



Continuing in the vein of exploring the significance of different winding/flip sectors, it is
natural to ask about a natural counterpart to the amplituhedron: what space do we define
if, in projecting through some _k_ _[′]_ -plane, the resulting data has “minimal” winding? It is in
particular natural to ask this for projecting through _k_ _[′]_ = _m_ -dimensional planes _Y_ [˜] in ( _k_ + _m_ )
dimensions; the dimensionality of _Y_ [�] space is _m × k_, the same as the amplituhedron. Now,
“minimal flips” has a meaning; as we saw in our discussion of the _k_ = 0 amplituhedron, the
positive Grassmannian itself gives us configurations of “zero flips” via projection down to one
dimension. So, it is natural to define the subspace of _m_ -planes in ( _k_ + _m_ ) dimensions which
satisfy
_Y_ _a_ 1 _ak_ _>_ 0 for _a_ 1 _<_ _< ak_ (13.1)
_⟨_ [�] _Z_ _· · · Z_ _⟩_ _· · ·_

A related motivation for defining this space is simply the following. We may have extremely
naively thought that starting with positive ( _k_ + _m_ )-dimensional data and projecting through
_Y_ in the amplituhedron would have left us with positive data. As we have seen this is wrong,
but it is natural to ask what planes _Y_ [�] do have such a property. Note that in the language of
section 5.1, the _Y_ [�] are “positive projections” _m→m′_ =0 down to _m_ _[′]_ = 0. The space of _Y_ [�] ’s of
_P_
this form is not empty, easy examples are afforded by looking at a matrix of positive _a_ data
_Z_
that has the form of the “moment curve”
 


























1 _· · ·_ 1
_x_ 1 _xn_

_· · ·_
_x_ [2] 1 _x_ [2] _n_

_· · ·_
... ... ...
_x_ _[k]_ 1 [+] _[m][−]_ [1] _x_ _[k]_ _n_ [+] _[m][−]_ [1]

_· · ·_



with _x_ 1 _<_ _< xn_ (13.2)
_· · ·_



All the ordered minors of this matrix are given by Vandermonde determinants and are positive
for _x_ 1 _<_ _<_ _xn_ . But if we take _Y_ [�] to be an _m_ plane given by the bottom _m_ rows of this

_· · ·_ _−_
matrix, then projecting through _Y_ [�] will give us _k_ dimensional data that simply corresponds
to the top _k_ rows of the matrix which are still positive.
Note that the space of _Y_ [˜] ’s defined in this way has the property that

_⟨Y_ [�] _· Y ⟩_ _>_ 0 for all _Y_ in the amplituhedron (13.3)

For the special case of _k_ = 1 for any _m_, the _Y_ [˜] ’s are _m_ -planes in _m_ + 1 dimensions, which
are points in the dual **P** _[m]_ . Then the inequalities


_Y_ _Za_ _>_ 0 (13.4)
_⟨_ [�] _·_ _⟩_

are the equations defining a polytope in the dual **P** _[m]_, whose facets are the _Za_ . So for _k_ = 1,
this space can be identified with the dual of the (cyclic) polytope coming from the external
data. The obvious extension to general _k_ gives one natural working definition for a dual of
the amplituhedron, as described in [10, 17].


                   - 37                    

This definition can naturally be extended to loops when _m_ = 4. At one-loop, we have

- _Y_ which is a four-plane in (4 + _k_ ) dimensions; but we also have a 2-plane _y_ ˜ inside _Y_ ; again
this space of 4-planes _Y_ [�] with a 2-plane _y_ ˜ inside it has the same dimensionality as the 1-loop
amplituhedron for _m_ = 4. Requiring minimal winding when projecting through _Y_ [˜] and _y_ ˜
requires
_Y_ _a_ 1 _ak_ _>_ 0 _,_ _y_ ˜ _a_ 1 _ak_ +2 _>_ 0 (13.5)
_⟨_ [�] _Z_ _· · · Z_ _⟩_ _⟨_ _Z_ _· · · Z_ _⟩_

At _L_ -loop order, we have _L_ 2-planes _y_ ˜ _i_ ; in addition to the above constraints, we must also
have that _y_ ˜ _iy_ ˜ _j_ _>_ 0, where _abcd_ represents contraction with the antisymmetric tensor
_⟨⟨_ _⟩⟩_ _⟨⟨_ _⟩⟩_
on the 4-dimensional space defined by the 4-plane _Y_ [�] . Said in the (4 + _k_ )-dimensional terms,
this says
_ϵ_ _[I]_ [1] _[···][I]_ [4] _[J]_ [1] _[···][J][k]_ (˜ _yi_ ) _I_ 1 _I_ 2(˜ _yj_ ) _I_ 3 _I_ 4 = _ρϵ_ _[I]_ [1] _[···][I]_ [4] _[J]_ [1] _[···][J][k]_ [ �] _YI_ 1 _I_ 2 _I_ 3 _I_ 4 _,_ with _ρ >_ 0 (13.6)


The space we have described certainly gives us _a_ natural geometric “dual” of the amplituhedron. As described in [10, 17], there are further motivations to find a dual amplituhedron;
by analogy with the well-understood case of _k_ = 1, we can hope for a direct and intrinsic
definition of the canonical form with logarithmic singularities on the amplituhedron expressed
as an integral over the dual geometry. As already described in [17] for the simplest case of
_G_ +(2 _,_ 4), a direct extension of the analogy with _k_ = 1 already involves novel features not seen
for polytopes. It will be interesting to see if the definition of the dual amplituhedron we have
given will nonetheless end up playing an important role in determining the canonical form
for both tree and loops.


**14** **Cutting** **Out** **The** **Amplituhedron** **With** **Inequalities**


We began by asking whether there was a way of defining the amplituhedron analagous to the
inequalities that cut out a polytope but immediately saw the obvious boundary inequalities
are not enough. We have seen that this conditions must be supplemented by topological ones
to determine the amplituhedron. Here we describe an alternative description which describes
the amplituhedron purely by cutting it out with inequalities; we content ourselves with a brief
description of these inequalities here, leaving a more complete investigation of this subject to
future work.
As we have seen, the “winding” picture becomes natural when projecting through _Y_ –we
are focusing on the information that is contained in all the direction _not_ spanned by the
_k_ -plane _Y_ . Amusingly, the picture of inequalities is defined precisely in the opposite way, by
looking at an interesting configuration of points _inside Y_ . Let us start with _m_ = 2. We would
like to identify points in the _k_ -plane _Y_, which lives in ( _k_ + 2) dimensions. Just by dimension
counting, a 3-plane in ( _k_ + 2) dimensions will intersect _Y_ in a point. But what natural 3planes can we consider? Given the cyclic structure inherent in the set-up, it is natural to
consider the 3-planes ( _a−_ 1 _a_ _a_ +1), multiplied by some appropriate factors of ( 1) _[k][−]_ [1] for
_Z_ _Z_ _Z_ _−_
_a_ = 1 _, n_ . These 3-planes intersect _Y_ in points that we will call _Va_ . Then, we claim that _Y_


                   - 38                    

is in the amplituhedron if and only if [ _Y ii_ + 1] _>_ 0, and also that the configuration of _n_,
_k_ -dimensional vectors _Va_ is in the positive Grassmannian _G_ +( _k, n_ )!
Checking that _Y_ = _C_ _· Z_ satisfies this condition is interesting. These inequalities are
satisfied due to somewhat magical positivity properties of the following “determinants of
minors”. For instance for _k_ = 2 the claim is that as long as the _Z_ data is positive,



det




[ _a_ _i−_ 1 _i_ _i_ +1] [ _a_ _j−_ 1 _j_ _j_ +1]
_Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_
����� [ _b_ _i−_ 1 _i_ _i_ +1] [ _b_ _j−_ 1 _j_ _j_ +1]
_Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_




_>_ 0 (14.1)
�����



for any _a_ _<_ _b_ and _i_ _<_ _j_ . This inequality follows non-trivially as a consequence of the
positivity of the _Z_ data; indeed it is a consequence of a more general interesting statement.
Let’s consider any _α_ 1 _<_ _α_ 2 _<_ _α_ 3, and _β_ 1 _<_ _β_ 2 _<_ _β_ 3 with _αi_ _βi_ . Now, consider the set of
_≤_
all indices _{_ 1 _,_ 2 _, · · ·_ _, n}_ - _{α_ 1 + 1 _, · · ·_ _, α_ 3 _−_ 1 _}_ - _{β_ 1 + 1 _, · · ·_ _, β_ 3 _−_ 1 _}_, and choose any _a < b_ in
this set. Then the claim is that




_>_ 0 (14.2)
�����



det




[ _aα_ 1 _α_ 2 _α_ 3] [ _bβ_ 1 _β_ 2 _β_ 3]
����� [ _aβ_ 1 _β_ 2 _β_ 3] [ _bα_ 1 _α_ 2 _α_ 3]



These statement can be proven recursively, starting from _Z_ ’s that correspond to 0-dimensional
cells of the external data positive Grassmannian where they are easily verified, and building
up to a general configuration of _Z_ ’s by shifting adjacent columns; it is easy to show that the
shifts push all such determinants to be positive.
Similarly for _k_ = 3, the analog of this statement is that for any _a < b < c_, _i < j_ _< k_, we
have




[ _a_ _b_ _i−_ 1 _i_ _i_ +1] [ _a_ _b_ _j−_ 1 _j_ _j_ +1] [ _a_ _b_ _k−_ 1 _k_ _k_ +1]
_Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_

[ _a_ _c_ _i−_ 1 _i_ _i_ +1] [ _a_ _c_ _j−_ 1 _j_ _j_ +1] [ _a_ _c_ _k−_ 1 _k_ _k_ +1]
_Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_

[ _b_ _c_ _i−_ 1 _i_ _i_ +1] [ _b_ _c_ _j−_ 1 _j_ _j_ +1] [ _b_ _c_ _k−_ 1 _k_ _k_ +1]
_Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_ _Z_




_>_ 0 (14.3)
�������



det



�������



This follows from a more general statement where ( _i−_ 1 _, i, i_ +1) _,_ ( _j_ _−_ 1 _, j, j_ +1) _,_ ( _k_ _−_ 1 _, k, k_ +1)
are replaced by any _α_ 1 _< α_ 2 _< α_ 3; _β_ 1 _< β_ 2 _< β_ 3; _γ_ 1 _< γ_ 2 _< γ_ 3 with _αi_ _≤_ _βi_ _≤_ _γi_, and _a, b, c_ are
chosen from the set 1 _,_ _, n_ _α_ 1 +1 _,_ _, α_ 3 1 _β_ 1 +1 _,_ _, β_ 3 1 _γ_ 1 +1 _,_ _, γ_ 3 1
_{_ _· · ·_ _}−{_ _· · ·_ _−_ _}−{_ _· · ·_ _−_ _}−{_ _· · ·_ _−_ _}_
with _a < b < c_ . The obvious generalization of these statements holds for higher _k_ .
The extension of the inequalities cutting out the tree amplituhedron to any _m_ is straightforward. For instance for _m_ = 4, we consider the 5-planes ( _a−_ 2 _a−_ 1 _a_ _a_ +1 _a_ +2), again
_Z_ _Z_ _Z_ _Z_ _Z_
multiplied by appropriate factors of ( _−_ 1) _[k][−]_ [1] for indices that wrap past _n_ . These 5-planes
intersect the _k_ -plane _Y_ in points _Ua_ . Once again, we conjecture that _Y_ is in the amplituhedron if and only if the obvious boundaries [ _Y ii_ + 1 _jj_ + 1] _>_ 0, and the configuration of
_k_ -dimensional vectors _Ua_ is in _G_ +( _k, n_ ). The extension to the all-loop amplituhedron then
follows. We have [ _Y ii_ + 1 _jj_ + 1] _>_ 0 _,_ [( _Y AB_ ) _αii_ + 1] _>_ 0 _,_ [ _Y_ ( _AB_ ) _α_ ( _AB_ ) _β_ ] _>_ 0. We also
demand that the 3-planes ( _a−_ 1 _a_ _a_ +1) intersect the ( _k_ + 2)-planes ( _Y AB_ ) _α_ in points _Va_ _[α]_
_Z_ _Z_ _Z_
which are belong to _G_ +( _k_ + 2 _, n_ ), and the 5-planes ( _a−_ 2 _Za−_ 1 _a_ _a_ +1 _a_ +2) intersect _Y_ in
_Z_ _Z_ _Z_ _Z_
points _Ua_ which belong to _G_ +( _k, n_ ).


                   - 39                    

**15** **Open** **Problems** **and** **Outlook**


We have presented an essentially combinatorial/topological characterization of the amplituhedron. It is remarkable that the rich, intricate geometry of the amplituhedron, and associated
with it, all the non-trivial physics of planar _N_ = 4 SYM scattering amplitudes, can ultimately
determined by nothing more than specifying a simple pattern of + and _−_ sign flips.
A great deal remains to be understood both about the mathematics and physics associated
with this new picture. Most pressingly, we would like to fully establish the equivalence of our
new formulation of the amplituhedron with the usual one; all that remains to be shown is that
satisfying correct winding or flip patterns implies that _Y_ can be written in the “ _Y_ = _C_ _· Z_ ”
form. At an even more basic level, we would like to have a proof of the equivalence between
“sign-flip” and “winding/crossing number” pictures.
We have largely focused on describing points on the interior of the amplituhedron, but it
is desirable to find an characterization of all the boundaries of the amplituhedron along the
same lines. On boundaries of the amplituhedron, many of the brackets involving _Y_ vanish
and, for instance, the “sign flip” criterion becomes ill-defined. We can of course ask if there
are perturbations to _Y_ that change “0”’s into + _[′]_ _s_ and _−_ ’s to get the right pattern of sign
flips, but is there a more efficient combinatorial check of whether degenerate configurations
of _Y_ ’s are in fact legal boundaries of the amplituhedron?
For the simplest _m_ = 1 and _m_ = 2 amplituhedra, we saw that an exhaustive account of the
sign flip/winding patterns directly led to triangulations of the spaces and the determination
of their associated canonical forms. This picture does not trivially extend to higher _m_, but
is there any topological interpretation of the known triangulations of _m_ = 4 amplituhedra,
and if not, are there new triangulations that are more natural from the “winding/flip” point
of view?
Do the sectors with different winding numbers have role to play in the physics? We
have seen that the space defined purely by the obvious physical inequalities, even further
generalized to simply mutual positivity between the 2-planes defining loops, seems to be
related to _M_ _×_ _M_ and correlation functions; but what is the invariant property of the
canonical form generalizing the notion of “logarithmic singularities” which can determine
correlators from the geometry?
Finally, the _m_ dimensional image of the amplituhedron made possible by our new picture
seems important from a number of points of view. In one obvious direction, we can finally
treat the geometry of “the integrand” and “the amplitude” on exactly the same footing (see
also [22]). This should be especially useful in the context of the powerful new methods
being developed, using the amplituhedron together with Landau equations, to constrain (and
perhaps determine) the “symbol” of multiloop MHV amplitudes in _N_ = 4 SYM [19, 20, 23].
The winding/flip picture of the amplituhedron should reduce this program to perfectly welldefined geometry problems, not just for MHV amplitudes but for amplitudes with all _n, k, L_ .
It is also exciting to have a new picture of the integrand of scattering amplitudes, which
depending _solely_ on the physical (momentum-twistor) data determining the momenta of the


                   - 40                    

particles. We have seen that 4 _×k_ forms on this kinematical space, which have logarithmic singularities on regions with correct winding numbers, determine the maximally supersymmetric
amplitudes. It would be fascinating to extend this picture to the other examples of amplitudes
which are known to be connected to positive geometry—for instance in ordinary momentum
space (or ordinary twistor space) for _N_ = 4 SYM, where “winding” should plausibly make
contact with twistor-strings [24], and ABJM theory [25, 26].
But more ambitiously, the notion of combining all helicity information together in one
object as a _differential_ _form_, rather than exploiting polarization vectors, or using the “ _η_ ”’s
of supersymmetric theories, and fixing this form by singularities determined by topological
properties, is a simple and powerful idea that begs for generalization. Since everything now
depends only on the momenta of external particles, our geometric, topological and combinatorial imaginations are no longer necessarily shackled to toy worlds with conformal invariance
and supersymmetry, and we can hope to describe scattering amplitudes closer to the real
world in this language. As some first steps in this direction, we are naturally led to ask: what
happens when we have additional data, like lines at infinity that break conformal invariance;
are there new notions of “winding” associated with these structures? And it is peculiar to
restrict our attention to 4 _× k_ forms only, are there natural forms of all degrees, which would
certainly be associated with less (or non)supersymmetric theories?


**Acknowledgements**


We would like to thank Yuntao Bai, Song He, Thomas Lam, Steve Karp and Lauren Williams
for useful discussions. The work of NAH is supported by the DOE under grant DOE DESC0009988. The work of HT is supported by NSERC and the Canada Research Chairs
program. We gratefully recognize the hospitality of the Fields Institute, where some of this
work was carried out.


**References**


[1] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. B. Goncharov, A. Postnikov and J. Trnka,
_Cambridge_ _University_ _Press_, arXiv:1212.5605 [hep-th].


[2] G. Lusztig, Representation Theory **2** (1998) 70–78.


[3] G. Lusztig, Lie Theory and Geometry, In Honor of B. Kostant, vol. 123 of Prog. in Math.,
pp. 531–569. Birkhauser, Boston, 1994.


[4] A. Postnikov, arXiv:math/0609764.


[5] N. Arkani-Hamed and J. Trnka, JHEP **1410**, 30 (2014) [arXiv:1312.2007 [hep-th]].


[6] N. Arkani-Hamed and J. Trnka, JHEP **1412**, 182 (2014) [arXiv:1312.7878 [hep-th]].


[7] S. Franco, D. Galloni, A. Mariotti and J. Trnka, JHEP **1503**, 128 (2015) [arXiv:1408.3410

[hep-th]].


[8] Y. Bai and S. He, JHEP **1502**, 065 (2015) [arXiv:1408.2459 [hep-th]].


                   - 41                    

[9] T. Lam, Commun. Math. Phys. **343**, no. 3, 1025 (2016) [arXiv:1408.5531 [math.AG]].


[10] N. Arkani-Hamed, A. Hodges and J. Trnka, JHEP **1508**, 030 (2015) [arXiv:1412.8478 [hep-th]].


[11] L. Ferro, T. Lukowski, A. Orta and M. Parisi, JHEP **1603**, 014 (2016) [arXiv:1512.04954

[hep-th]].


[12] D. Galloni, arXiv:1601.02639 [hep-th].


[13] L. Ferro, T. Lukowski, A. Orta and M. Parisi, arXiv:1612.04378 [hep-th].


[14] L. Ferro, T. Lukowski, A. Orta and M. Parisi, arXiv:1612.06276 [hep-th].


[15] S. N. Karp and L. K. Williams, arXiv:1608.08288 [math.CO].


[16] Y. Bai, S. He and T. Lam, JHEP **1601**, 112 (2016) doi:10.1007/JHEP01(2016)112

[arXiv:1510.03553 [hep-th]].


[17] N. Arkani-Hamed, Y. Bai and T. Lam, arXiv:1703.04541 [hep-th].


[18] A. Hodges, JHEP **1305**, 135 (2013) [arXiv:0905.1473 [hep-th]].


[19] A. B. Goncharov, M. Spradlin, C. Vergu and A. Volovich, Phys. Rev. Lett. **105**, 151605 (2010)

[arXiv:1006.5703 [hep-th]].


[20] J. Golden, A. B. Goncharov, M. Spradlin, C. Vergu and A. Volovich, JHEP **1401**, 091 (2014)

[arXiv:1305.1617 [hep-th]].


[21] B. Eden, P. Heslop and L. Mason, arXiv:1701.00453 [hep-th].


[22] L. J. Dixon, M. von Hippel, A. J. McLeod and J. Trnka, JHEP **1702**, 112 (2017)

[arXiv:1611.08325 [hep-th]].


[23] T. Dennen, I. Prlina, M. Spradlin, S. Stanojevic and A. Volovich, arXiv:1612.02708 [hep-th].


[24] E. Witten, Commun. Math. Phys. **252**, 189 (2004), hep-th/0312171.


[25] O. Aharony, O. Bergman, D. L. Jafferis and J. Maldacena, JHEP **0810**, 091 (2008)

[arXiv:0806.1218 [hep-th]].


[26] Y. Huang, C. Wen, JHEP (2014) 2014: 104. arXiv:1309.3252 [hep-th].


                   - 42                   

