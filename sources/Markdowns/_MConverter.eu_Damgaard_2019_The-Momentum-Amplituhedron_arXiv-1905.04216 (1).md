LMU-ASC 21/19

Prepared for submission to JHEP

The Momentum Amplituhedron

David Damgaard,1 Livia Ferro,1,2 Tomasz Lukowski,2 and Matteo Parisi3

1Arnold–Sommerfeld–Center for Theoretical Physics, 

Ludwig–Maximilians–Universität, 

Theresienstraße 37, 80333 München, Germany

2School of Physics, Astronomy and Mathematics, 

University of Hertfordshire, 

Hatfield, Hertfordshire, AL10 9AB, United Kingdom

3Mathematical Institute, University of Oxford, 

Andrew Wiles Building, Radcliffe Observatory Quarter, 

Woodstock Road, Oxford, OX2 6GG, U.K. 

E-mail: d.damgaard@lmu.de, livia.ferro@lmu.de, t.lukowski@herts.ac.uk, 

parisi@maths.ox.ac.uk

Abstract: In this paper we define a new object, the momentum amplituhedron, which is the long sought-after positive geometry for tree-level scattering amplitudes in N = 4 super Yang-Mills theory in spinor helicity space. Inspired by the construction of the ordinary amplituhedron, we introduce bosonized spinor helicity variables to represent our external kinematical data, and restrict them to a particular positive region. The momentum amplituhedron Mn,k is then the image of the positive Grassmannian via a map determined by such kinematics. The scattering amplitudes are extracted from the canonical form with logarithmic arXiv:1905.04216v1 \[hep-th\] 10 May 2019

singularities on the boundaries of this geometry. 

Contents

1

Introduction

1

2

The Definition

3

2.1

The Ordinary Amplituhedron

3

2.2

The Momentum Amplituhedron

5

2.3

Momentum Amplituhedron Volume Form

9

3

Examples

11

3.1

MHV/MHV Amplitudes

11

3.2

NMHV6 Amplitude

13

4

Conclusions and Outlook

17

5

Acknowledgments

18

A Orthogonal complements

18

B Proof of the relation \(Xpq\) = hY pqi

20

C Momentum Conservation

20

D Positive Mandelstam variables for k = 2

21

1

Introduction

In the past decade a new, geometric picture has emerged for scattering amplitudes in planar N = 4 super Yang-Mills \(SYM\) theory. It originated from the observation that the tree-level amplitudes and loop-level integrands of n-point amplitudes for all helicity sectors can be computed using integrals over the Grassmannian space \[1, 2\]. In such formulation, amplitudes can be extracted from a Grassmannian integral over a suitable contour which selects a particular sum of residues. Building upon this idea, novel studies revealed the interrelation between the rich combinatorial structure of positive Grassmannians and the physical properties of amplitudes \[3\]. From this point of view, the aforementioned residues are associated with positroid cells, which are particular subvarieties inside the positive Grassmannian. The proper combination of cells is selected by using the Britto-Cachazo-Feng-Witten \(BCFW\) recursion relations \[4, 5\]. However, the cells contributing to a particular amplitude are seem-ingly not related to each other inside the positive Grassmannian. Nevertheless, via a map

– 1 –

defined by a positive matrix of bosonized momentum twistor variables, they assemble in a convex-like object. The image of the positive Grassmannian through such map is a geometric space, the amplituhedron \[6\], and the union of the cell images provides a particular triangulation. The amplituhedron became eventually the first example of a vast family of the so-called positive geometries \[7\], which nowadays provide a geometric description for various quantities in theoretical physics: see, for instance, the kinematic associahedron \[8\], the cosmological polytope \[9\], and positive geometries in CFT \[10, 11\]. 

Nevertheless, despite the name, the amplituhedron is more naturally suited to describe the dual Wilson loop rather than the amplitude itself, being defined in the momentum twistor space. In particular, the employment of these variables restricts the possible generalization of this geometry to scattering amplitudes in other models, since it is based on the Amplitude/Wilson loop duality which is present only in planar N = 4 SYM. Therefore it limits the possibility of finding positive geometries for scattering amplitudes in less supersymmetric models and beyond the planar sector. It is then desirable to find a geometric description directly in the ordinary twistor space or, even better, in the spinor helicity space \(λi, ˜

λi\). The

first attempt in this direction was made in \[12\], where it was suggested that the amplituhedron in momentum space should be the image of the twistor-string worldsheet \[13\] through the Roiban-Spradlin-Volovich \(RSV\) equations \[14\]. In particular, it was conjectured that the space should have proper sign flips for both λi and ˜

λi, as well as the additional assumption

that the planar Mandelstam variables should be positive. In this paper we will show that a suitable positive geometry with such characteristics exists and provides the proper expressions for the amplitude when written in the non-chiral superspace \(λi, ˜

λi, ηi, ˜

ηi\). In order to

achieve our goal, we will first introduce its bosonized version: \(Λi, ˜

Λi\). By assuming that the

external kinematic data Λ and ˜

Λ satisfy particular positivity conditions, we will reproduce the sign flips postulated in \[12\]. Additionally, further constraints entangling Λ and ˜

Λ will

enforce positivity of Mandelstam variables. Then, we will define the momentum amplituhedron as the image of the positive Grassmannian through a map determined by this positive external data. We will show that such space is indeed a positive geometry, whose canonical logarithmic differential form encodes scattering amplitudes in spinor helicity variables. 

The paper is structured as follows. We start in section 2 by reviewing the formulation of the original amplituhedron in the bosonized momentum twistor space. We proceed by defining the momentum amplituhedron, i.e. the positive geometry in the bozonized spinor helicity variables. Afterwards, we show how to find the logarithmic differential form on the momentum amplituhedron and how to extract the scattering amplitudes from it. Section 3

consists of examples which show in detail how to use the construction from section 2. We end the paper with Conclusions and Outlook, and a few Appendices containing more technical details of our construction. 

– 2 –

2

The Definition

2.1

The Ordinary Amplituhedron

We start by recalling the construction of the amplituhedron in momentum twistor space. In the past few years there has been a lot of progress on different descriptions of the amplituhedron \[7, 15\]. We will focus here on two of them, which will be relevant for our construction of the momentum amplituhedron: the original definition introduced in \[6\] and the description based on the sign flips presented in \[15\]. The first states that the amplituhedron A\(m=4\) n,k0

can be described on the space of bosonized supertwistors ZA, A = 1, . . . , 4 \+ k0, which speci

ify the kinematic data for the n-particle Nk0 MHV amplitude. The components of bosonized supertwistors include the bosonic part of the momentum supertwistors \(λa, ˜

µ ˙a\), a, ˙a = 1, 2, 

i

i

and the bosonized version of the fermionic components ξα = φα

, α = 1, . . . k0, where φα

i

RχR

i

R

are auxiliary Grassmann-odd parameters and R = 1, . . . , 4 is the R-symmetry index. As already explored in the literature, there exists a straightforward generalization of bosonized variables beyond the case relevant for physics, m = 4, and in the following we will allow any values for the label m. We start by demanding that the matrix of bosonized variables Z = \(ZA\) ∈ M

i

\+\(m \+ k0, n\) is positive, i.e. all its ordered maximal minors are positive. Then the amplituhedron A\(m\)

n,k0 is defined as the image of the map

ΦZ : G\+\(k0, n\) → G\(k0, k0 \+ m\) , 

\(2.1\)

given by

Y A

∈

α = cαiZ A

i

G\(k0, k0 \+ m\) , 

C = \(cαi\) ∈ G\+\(k0, n\) . 

\(2.2\)

Here, G\+\(k0, n\) is the positive Grassmannian, i.e. the space of all positive matrices modulo GL\(k0\) transformations. For each amplituhedron A\(m\)

n,k0 , one can define a \(k0 · m\)-dimensional

\(m\)

differential form Ωn,k0, called the volume form, which has logarithmic singularities on all boundaries \(of all dimensions\) of the amplituhedron space A\(m\) n,k0 . In particular, the volume

\(m=4\)

form Ωn,k0

encodes the Nk0 MHV tree-level amplitude in N = 4 SYM. The geometric space A\(m\)

\(m\)

n,k0 together with the form Ωn,k0 describe a positive geometry, as defined in \[7\]. Throughout \(m\)

the years, various methods to find the volume form Ωn,k0 have been proposed \[7, 16–18\]. One can, for example, triangulate the amplituhedron A\(m\)

n,k0 by e.g. finding a collection of positroid

cells T = \{∆σ\} of dimension k0 · m in G\+\(k0, n\) such that the images of these cells through the function ΦZ do not overlap and cover the amplituhedron. To each positroid cell one can associate a canonical form ωσ with logarithmic singularities on all its boundaries, see \[3\]. The \(m\)

volume form Ωn,k0 is found by evaluating the push-forward of the canonical forms ωσ via the function ΦZ and then summing over all positroid cells in the triangulation \(m\)

X

Ω

\(Φ

n,k0 =

Z \)∗ ωσ . 

\(2.3\)

∆σ∈T

– 3 –

The result of the push-forward is a logarithmic differential form on G\(k0, k0 \+ m\) which can be written as

\(m\)

X

Ω

d

\(Y, Z\) , 

\(2.4\)

n,k0 =

Y log ασ

1 \(Y, Z \) ∧ dY log ασ

2 \(Y, Z \) ∧ . . . ∧ dY log ασ

k0m

∆σ∈T

where ασ\(Y, Z\) are the canonical positive coordinates parametrizing the cell ∆

i

σ . The explicit

expressions for various values of parameters \(n, m, k0\) can be found e. g. in \[7\]. 

\(m\)

An alternative way to find the volume form is to introduce a volume function Ωn,k0 defined by

k0

\(m\)

Y

\(m\)

Ω

hY

n,k0 =

1 . . . Yk0 dmYαi Ωn,k0 , 

\(2.5\)

α=1

where Qk0

hY

α=1

1 . . . Yk0 dmYαi is the standard measure on the Grassmannian G\(k0, k0 \+ m\). 

The volume function can also be obtained by evaluating the integral over the space of k × n matrices

k0

Z

\(m\)

dk0·ncαi

Y

X

Ω

δm\+k0 \(Y A −

c

n,k0 =

α

αiZ A

i \) , 

\(2.6\)

γ \(12 . . . k0\)\(23 . . . k0 \+ 1\) . . . \(n1 . . . k0 − 1\) α=1

i

over a suitable contour γ. The integrand is a meromorphic function of c and the integral reduces to a sum of residues, specified by the contour γ. 

\(m\)

The original construction of the amplituhedron defines the volume form Ωn,k0 as differential form on an auxiliary Grassmannian space G\(k0, k0 \+ m\) parametrized by Y . However, as pointed out in \[15\], the form \(2.4\) can be also thought of as a differential form on the purely bosonic part of the momentum supertwistors, za, a = 1, . . . , m. It can be accomplished by i

replacing the differential with respect to Y by the differential with respect to the kinematic data Z: dY log → dZlog, and at the same time by fixing Y = Y ∗, where Y ∗ is a reference k0-plane in k0 \+ m dimensions. This new differential form is a logarithmic differential form on the space of configurations of za, satisfying particular sign-flip or topological conditions \[15\]. 

i

Let us now recall the proper sign-flip conditions in the m = 2 case, which will be relevant for us in the following. For m = 2, we consider a configuration of two-dimensional vectors za, i

a = 1, 2, and define the brackets hijiz := z1z2 − z2z1. The amplituhedron A\(m=2\) i

j

i

j

n,k0

space is

defined as a subspace of the configuration space \{zi\}i=1,...,n satisfying the following conditions: hii \+ 1iz > 0 and the sequence \{h12iz, h13iz, . . . , h1niz\} has exactly k0 sign flips. 

\(2.7\)

Although the sign-flip characterization of the amplituhedron does not refer either to any auxiliary space or the quite peculiar bosonization described above, it is not an easy task to find the volume form directly from this definition. Therefore, we often refer back to the original construction of the amplituhedron in the bosonized space. 

– 4 –

2.2

The Momentum Amplituhedron

In order to define an amplituhedron directly in the spinor helicity space we will follow a reverse path compared to the one described in the previous section. Our starting point will be the conjecture in \[12\] suggesting that we should consider a positive geometry described by proper sign-flips in the spinor helicity space, together with positivity of the Mandelstam variables formed out of consecutive momenta. Let us start by taking a configuration space of n spinor-helicity variables parametrized by \{λa, ˜

λ ˙a\}, a, ˙a = 1, 2, and define the brackets

hiji

˜

˜

λ := λ1λ2 − λ2λ1 and \[ij\]

:= ˜

λ1λ2 − ˜

λ2λ1. Let us also define planar Mandelstam variables

i

j

i

j

˜

λ

i

j

i

j

X

si,i\+1,...,i\+p =

hj1j2iλ\[j1j2\]˜ . 

\(2.8\)

λ

i≤j1<j2≤i\+p

This relation is understood modulo n. Then the conjecture of \[12\] states that the positive region would be defined by the following conditions:

• Positive planar Mandelstam variables: si,i\+1,...,i\+p > 0 for i = 1, . . . , n, p = 1, . . . , n − 3. 

• Correct sign flips: let the list \{h12iλ, h13iλ, . . . , h1niλ\} have N sign flips and the list

\{\[12\]˜, \[13\] , . . . , \[1n\] \} have ˜

N sign flips, then we require one of the two possibilities: λ

˜

λ

˜

λ

\(N, ˜

N \) = \(k − 2, k\) or \(N, ˜

N \) = \(n − k, n − k − 2\). 

In this paper we define the space of bosonized spinor helicity variables and a related positive geometry, which we call the momentum amplituhedron Mn,k. This will encode the Nk−2MHV

n-particle tree-level amplitudes in N = 4 SYM1. By demanding certain positivity conditions on the bosonized variables, we will recover proper sign flips for λ and ˜

λ. With additional

assumptions, we will also guarantee that the planar Mandelstam variables are positive. 

As described in details in \[12\], any n-particle Nk−2MHV scattering amplitude in planar N = 4 SYM can be written as a differential form in spinor helicity space. The starting point is the non-chiral superspace which is parametrized by spinor helicity variables, \{λa, ˜

λ ˙a\}, 

a, ˙a = 1, 2, together with the Grassmann odd parameters \{ηr, ˜

η ˙r\}, r, ˙r = 1, 2. Then the

amplitude is a function on n copies of this superspace with coordinates \{λi, ηi|˜

λi, ˜

ηi\}. Let us

remark that in this space the supercharges take the form: n

n

X

X

˜

q ˙ar =

˜

λ ˙aiηri , 

qar =

λai ˜

η ˙ri . 

\(2.9\)

i=1

i=1

Moreover, there is a natural way to associate the R-symmetry indices \(r, ˙r\) with the spinor indices \(a, ˙a\) and write any function on the superspace as a differential form on its bosonic part. It amounts to the replacement

ηa → dλa , 

˜

η ˙a → d˜

λ ˙a . 

\(2.10\)

1Notice that k = k0 \+ 2, where k0 was defined in the previous section. 

– 5 –

The degree of this differential form in \(dλ, d˜

λ\) is then \(2\(n − k\), 2k\), respectively. This is a

similar situation to the one which we have encountered for the momentum twistors, where the amplitude can be thought of as a differential form of degree 4k0 = 4\(k − 2\) on the bosonic part of the momentum twistor superspace. Equivalently, it was possible to introduce a bosonized momentum twistor space by introducing auxiliary Grassmann-odd parameters. We will now repeat this construction for the spinor helicity variables. 

Let us introduce 2\(n − k\) auxiliary Grassmann-odd parameters φα

a , α = 1, . . . , n − k and

2k auxiliary Grassmann-odd parameters ˜

φ ˙α, ˙

α = 1, . . . , k. We define bosonized spinor helicity

˙a

variables as



\! 

λa

ΛA

i

i =

, 

A = \(a, α\) = 1, . . . , n − k \+ 2 , 

\(2.11\)

φα ·

a

ηa

i



˜

\! 

˜ ˙

λ ˙a

ΛA

i

i =

˜

, 

˙

A = \( ˙a, ˙

α\) = 1, . . . , k \+ 2 . 

\(2.12\)

φ ˙α · ˜

η ˙a

˙a

i

In the next step we define a positive region on the space of bosonized spinor helicity variables. 

We introduce the matrices





Λ = ΛA ΛA . . . ΛA

∈ M \(n − k \+ 2, n\), 

˜

Λ =

˜ ˙

A ˜ ˙

A

˙

A

∈ M \(k \+ 2, n\) , \(2.13\)

1

2

n

Λ

Λ

. . . ˜

Λ

1

2

n

and refer to the pair \(Λ, ˜

Λ\) as the kinematic data. These matrices describe linear subspaces of dimension n − k \+ 2 and k \+ 2, respectively, inside an n-dimensional space. We denote their orthogonal complements as Λ⊥ ∈ M \(k − 2, n\) and ˜

Λ⊥ ∈ M \(n − k − 2, n\). The orthogonal

complements are defined up to a GL-transformation, corresponding to a change of basis of the corresponding subspaces. Additionally, we define two types of brackets on the space of bosonized variables. On the space of Λ’s we define

h

A

i

n−k\+2

1i2 . . . in−k\+2i = A

ΛA1 ΛA2 . . . Λ

. 

\(2.14\)

1A2...An−k\+2

i1

i2

in−k\+2

Similarly for the space of ˜

Λ’s we have

˙

˙

˙

A

\[i

˜ A1 ˜ A2

k\+2

1i2 . . . ik\+2\] = ˙

Λ

Λ

. . . ˜

Λ

. 

\(2.15\)

A

˙

1A2... ˙

Ak\+2

i1

i2

ik\+2

Until now there is manifest symmetry between Λ and ˜

Λ: if we exchange Λ ↔ ˜

Λ together

with exchanging k ↔ n−k, the space looks the same. This corresponds to the parity invariance of N = 4 SYM. In the following we will, however, need to break this symmetry by choosing one of two possible descriptions. These two choices correspond to the two possibilities available in the conjecture for the sign-flip condition. In order to define the positive region, we restrict

– 6 –

the allowed external data to be positive in the following sense: \(

\)

matrix ˜

Λ positive

. 

\(2.16\)

matrix Λ⊥ positive

Alternatively, we could assume that the matrices ˜

Λ⊥ and Λ are positive and proceed in an

analogous way. We emphasize that the fact that the matrix Λ⊥ is positive does not imply that the matrix Λ is positive. On the contrary, using the discussion from the Appendix A, 

one can notice that the matrix encoding the orthogonal complement of a positive matrix will have both positive and negative minors. 

Having defined the positive region we are ready to adapt the map \(2.1\) to the bosonized spinor helicity space. We define the momentum amplituhedron Mn,k as the image of the positive Grassmannian G\+\(k, n\) through the map

Φ

: G

\(Λ, ˜

Λ\)

\+\(k, n\) → G\(k, k \+ 2\) × G\(n − k, n − k \+ 2\) , 

\(2.17\)

which to each element of the positive Grassmannian C = \{c ˙αi\} ∈ G\+\(k, n\) associates a pair of Grassmannian elements \( ˜

Y , Y \) ∈ G\(k, k \+ 2\) × G\(n − k, n − k \+ 2\) in the following way

˜ ˙

˙

Y A

˜ A

˙

α = c ˙

αi Λi , 

Y A

α = c⊥

αi ΛA

i , 

\(2.18\)

where C⊥ = \{c⊥ \} is the orthogonal complement of C. One can show that Y has rank \(n − k\), αi

therefore it is an element of G\(n − k, n − k \+ 2\) and the map Φ

is well defined. After

\(Λ, ˜

Λ\)

imposing additional assumptions on Λ and ˜

Λ, which will guarantee positive planar Mandel-

stam variables, we claim that the momentum amplituhedron Mn,k is a positive geometry and its volume form encodes the n-particle Nk−2MHV tree-level scattering amplitude in N = 4

SYM. 

In order to confirm this claim, we start by checking that the momentum amplituhedron has the expected dimension, namely 2n − 4, and that we find the correct pattern of sign flips. 

Let us first observe that the dimension of G\(k, k \+ 2\) × G\(n − k, n − k \+ 2\) is 2n dim\(G\(k, k \+ 2\)\) \+ dim\(G\(n − k, n − k \+ 2\)\) = 2k \+ 2\(n − k\) = 2n . 

\(2.19\)

We notice, however, that the image of the positive Grassmannian G\+\(k, n\) through the map Φ

is lower dimensional. Indeed, the momentum amplituhedron lives in the following \(Λ, ˜

Λ\)

co-dimension four surface inside G\(k, k \+ 2\) × G\(n − k, n − k \+ 2\): n

X 

a 

˙

a

P a ˙a =

Y ⊥ · Λ

˜

Y ⊥ · ˜

Λ

= 0 . 

\(2.20\)

i

i

i=1

For a proof of this statement see Appendix C. We defined here the orthogonal complements Y ⊥ ∈ G\(2, n − k \+ 2\) and ˜

Y ⊥ ∈ G\(2, k \+ 2\). One can think about the condition \(2.20\)

– 7 –

as being equivalent to the momentum conservation but written directly in the momentum amplituhedron space. Indeed, if we project through a fixed Y and ˜

Y , as we will see later, 

then we find



a



˙

a

Y ⊥ · Λ

→ λa

˜

→ ˜

i , 

Y ⊥ · ˜

Λ

λ ˙ai , 

\(2.21\)

i

i

and the condition \(2.20\) reduces to the usual momentum conservation. 

Equation \(2.20\)

implies that the image of the positive Grassmannian G\+\(k, n\) through the map Φ

is a

\(Λ, ˜

Λ\)

co-dimension four surface inside the space G\(k, k \+ 2\) × G\(n − k, n − k \+ 2\) and therefore has the correct dimension 2n − 4. 

The second check we would like to perform is to confirm that this geometry satisfies the correct sign flip conditions, postulated in \[12\]. Let us first remind the reader that one can reduce the geometry in the bosonized space to the purely bosonic part by projecting the kinematic configuration in the direction of a fixed Y , see \[15\]. In the context of the momentum amplituhedron, the projection results in the reduction:

hY iji → hijiλ , 

\[ ˜

Y ij\] → \[ij\]˜ . 

\(2.22\)

λ

Therefore, we are interested in the following sequences of brackets:

\{hY 12i, hY 13i, . . . , hY 1ni\} , 

\(2.23\)

and

\{\[ ˜

Y 12\], \[ ˜

Y 13\], . . . , \[ ˜

Y 1n\]\} . 

\(2.24\)

We want to show that the number of sign flips equals k − 2 in the sequence \(2.23\) and k in the sequence \(2.24\). This corresponds to the condition \(N, ˜

N \) = \(k − 2, k\) in the conjecture

in \[12\]. It is easy to see that the number of sign flips in the sequence \(2.24\) is k since the formula in \(2.18\) for ˜

Y is the definition of the ordinary amplituhedron \[6\] with m = 2 and k = k0. It was shown in \[15\] that in this case the number of sign flips equals k. The sequence

\(2.23\) requires further attention. Let us define X ∈ G\(k − 2, k\) by

¯

¯

XA

A

˙

α = \(Λ⊥\)i c ˙

αi , 

¯

A = 1, . . . , k − 2 , ˙

α = 1, . . . , k . 

\(2.25\)

We emphasize that both matrices Λ⊥ and C in \(2.25\) are positive. Therefore \(2.25\) is similar to the definition of the ordinary amplituhedron with m = 2 and k → k − 2, with the role of the matrices C and Λ⊥ exchanged. It implies that the number of sign flips in the sequence

\{\(X12\), \(X13\), . . . , \(X1n\)\} , 

\(2.26\)

equals k − 2, where we defined

\(Xij\) = ˙α

X1 ....Xk−2 c

1... ˙

αk

˙

α

˙

α

1

˙

αk−2

k−1,i c ˙

αk,j . 

\(2.27\)

– 8 –

Moreover, one can show that

\(Xij\) = hY iji , 

\(2.28\)

see Appendix B. This implies that the number of sign flips in \(2.23\) is k − 2, as required. 

2.3

Momentum Amplituhedron Volume Form

Having defined the space Mn,k, we want to find its volume form, i.e. the differential form with logarithmic singularities on all boundaries of Mn,k. We start by classifying possible boundaries of the momentum amplituhedron. There are three different types of boundaries: two of them are similar to the ones we have encountered already for the amplituhedron A\(m=2\): n,k

hY i i \+ 1i = 0 , 

\[ ˜

Y i i \+ 1\] = 0 . 

\(2.29\)

These can be related to all possible collinear limits of the amplitude. In addition, there is also a new type of boundary which depends on both Λ and ˜

Λ. These are defined by

Si,i\+1...,i\+p = 0 , 

p = 2, . . . , n − 4 , 

\(2.30\)

where Si,i\+1...,i\+p is the uplift of the planar Mandelstam variables \(2.8\) to the amplituhedron space defined as

X

Si,i\+1...,i\+p =

hY j1j2i\[ ˜

Y j1j2\] . 

\(2.31\)

i≤j1<j2≤i\+p

Notice that Si,i\+1...,i\+p reduces to the ordinary Mandelstam variables si,i\+1...,i\+p we defined in \(2.8\) when projected through fixed Y and ˜

Y . The boundaries \(2.30\) correspond to all possible non-trivial factorizations of the amplitude. Notice that the case when a two-particle Mandelstam variable vanishes splits into two boundaries of the momentum amplituhedron of the type \(2.29\) and are not included in \(2.30\). 

We look now for a differential form Ωn,k with logarithmic singularities on all boundaries of the form \(2.29\) and \(2.30\) and which is finite inside Mn,k. To do this we first triangulate the space Mn,k with each triangle being an image through the map Φ

of a \(2n−4\)-dimensional

\(Λ, ˜

Λ\)

cell of the positive Grassmannian G\+\(k, n\). The proper combination of cells can be found using the positroid MathematicaTM package \[19\]2. The logarithmic differential form on Mn,k is the sum over such cells of push-forwards of canonical differential form for each cell. As for the ordinary amplituhedron A\(m\), the explicit answer is a sum of rational functions where n,k

the denominators can contain spurious singularities, corresponding to spurious boundaries in a given triangulation. These singularities disappear in the complete sum and the only divergences of Ωn,k correspond to the external boundaries \(2.29\) and \(2.30\). The final check we need to perform in order to obtain a positive geometry is to confirm that there are no singularities of Ωn,k inside Mn,k. It is clear for the boundaries \(2.29\) because it is easy to 2To find a possible triangulation of Mn,k one needs to use the function treeContour\[n,k\]. 

– 9 –

show that for all points inside the amplituhedron hY i i \+ 1i > 0 , 

\[ ˜

Y i i \+ 1\] > 0 . 

\(2.32\)

The situation is more complicated for the singularities where Si,i\+1,...,i\+p vanish. As we will see when studying examples in the following section, the positivity conditions which we spelled out in the previous section – ˜

Λ positive and Λ⊥ positive – are not enough to

guarantee that Si,i\+1,...,i\+p > 0 for all points inside the amplituhedron Mn,k. At the moment it is unclear in full generality what are the necessary and sufficient conditions to enforce positive Mandelstam variables. Nevertheless, we have found instances for which all planar Mandelstams are positive for all points in Mn,k, proving that the set of configurations for which the momentum amplituhedron is a positive geometry is non-empty. Let us take for example the following parametrization of the kinematic data:

¯

¯

˙

˙

\(Λ⊥\)A

A−1

A

A−1

i = i

, 

˜

Λi = i

. 

\(2.33\)

This choice of positive matrices corresponds to considering the vertices of the polytopes defined by the matrices Λ⊥ and ˜

Λ to lie on the moment curve. We have explicitly checked that for all points inside the momentum amplituhedron Mn,k, for n ≤ 10 and any k, and with the kinematic data specified by \(2.33\), all planar Mandelstam variables are positive: Si,i\+1...,i\+p > 0 , 

p = 1, . . . , n − 3 . 

\(2.34\)

We will study examples in more detail in the following section. We will notice that the space of allowed kinematic configurations is rather large and, in particular, for MHV and MHV

amplitudes all kinematic configurations provide positive geometry. 

We conclude this section by two remarks. First, we describe how to obtain the amplitude Atree from the volume form Ω

n,k

n,k . Let us recall that the momentum amplituhedron Mn,k is \(2n − 4\)-dimensional and therefore the degree of Ωn,k is \(2n − 4\). There are various ways one can write Ωn,k, related to each other by momentum conservation. In order to make it invariant we use the fact that 1 = δ4\(P \)d4P . This allows us to define the volume function Ωn,k in the following way:

n−k

k

Y

Y

Ωn,k ∧ d4P δ4\(P \) =

hY1 . . . Yn−kd2Yαi

\[ ˜

Y1 . . . ˜

Ykd2 ˜

Y ˙α\] δ4\(P \) Ωn,k . 

\(2.35\)

α=1

˙

α=1

Indeed, the form Ωn,k ∧ d4P is top-dimensional and therefore can be written in terms of the measure on G\(k, k \+ 2\) × G\(n − k, n − k \+ 2\) multiplied by a function. Then, the procedure to extract the amplitude from the volume form Ωn,k is similar to the ordinary amplituhedron, 

– 10 –

i.e. we localize the Y and ˜

Y on reference subspaces3



\! 



\! 

**0**

**0**2×k

Y ∗ =

2×\(n−k\)

, 

˜

Y ∗ =

, 

\(2.36\)

**1**\(n−k\)×\(n−k\)

**1**k×k

obtaining

Z

Z

Atree

n,k

= δ4\(p\)

dφ1a . . . dφn−k

a

d ˜

φ1˙a . . . d ˜

φk˙a Ωn,k\(Y ∗, ˜

Y ∗, Λ, ˜

Λ\) , 

\(2.37\)

where δ4\(p\) comes from the localization of δ4\(P \) on Y ∗, ˜

Y ∗. In the following section we will

show how extracting the amplitude works in practice in a few examples. 

Finally, in analogy with the ordinary amplituhedron, we can introduce an integral representation of the volume function Ωn,k as an integral over a matrix space n−k

k

Z

d\(n−k\)·\(n−k\)g Z

Y

Y

˙

˙

δ4\(P \) Ω

A

˜ A

n,k =

ωn,k

δ\(n−k\+2\)\(Y A−gβ

δ\(k\+2\)\( ˜

Y − c ˙αi Λ

\(detg\)n−k

α

α \(c⊥\)βi ΛA

i \)

˙

α

i \) , 

α=1

˙

α=1

\(2.38\)

where we additionally need to integrate over the matrix g corresponding to a GL\(n − k\)-

transformation encoding the ambiguity of defining an orthogonal complement. The integra-tion measure ωn,k is the canonical measure on the space of k · n matrices: dk·nc ˙αi

ωn,k =

, 

\(2.39\)

\(12 . . . k\)\(23 . . . k \+ 1\) . . . \(n1 . . . k − 1\)

where the brackets in the denominator are minors of the matrix C

\(i1i2 . . . ik\) = ˙α

c

c

. . . c

. 

\(2.40\)

1 ˙

α2... ˙

αk

˙

α1i1 ˙

α2i2

˙

αkik

3

Examples

3.1

MHV/MHV Amplitudes

We now move to study examples of momentum amplituhedra, starting with MHV and MHV

amplitudes. Already in this case the volume function takes a new and interesting form. The dimension of the momentum amplituhedron Mn,2 is the same as the dimension of the positive Grassmannian G\+\(2, n\) and therefore there is no need to triangulate the amplituhedron, it is enough to take the image of the Grassmannian top-dimensional positroid cell. It is an easy task to find all boundaries of the momentum amplituhedron Mn,2: they are all of the form hY ii \+ 1i = 0 for i = 1, . . . , n. The volume form we find in this section will make these boundaries manifest. One can also show that, for all points inside the momentum amplituhedron Mn,2, \[ ˜

Y ii \+ 1\] > 0 for all i = 1, . . . , n, as well as Si,i\+1...,i\+p > 0 for all i = 1, . . . , n and p = 1, . . . , n − 3, see appendix D. 

3This choice of Y ∗, ˜

Y ∗ is compatible with the embedding of λ, ˜

λ in Λ, ˜

Λ as in \(2.11\), \(2.12\). 

– 11 –

Let us start by considering the simplest case, i.e. the four-point MHV amplitude. We parametrize the top cell of G\+\(2, 4\) using the positive parameters αj:



\! 

1 α

C =

2 0 −α3

. 

\(3.1\)

0 α1 1 α4

There are various ways to find α’s from equations \(2.18\). A particular choice results in α’s depending only on Y and Λ:

hY 12i

hY 23i

hY 34i

hY 14i

α1 =

, α

, α

, α

. 

\(3.2\)

h

2 =

3 =

4 =

Y 13i

hY 13i

hY 13i

hY 13i

The push-forward of the Grassmannian top form through \(2.17\) is therefore: 4

^

hY 12i

hY 23i

hY 34i

hY 14i

Ω4,2 =

dlogαj = dlog

∧ dlog

∧ dlog

∧ dlog

\(3.3\)

hY 13i

hY 13i

hY 13i

hY 13i

j=1

h1234i2

=

hY d2Y

h

1ihY d2Y2i . 

\(3.4\)

Y 12ihY 23ihY 34ihY 41i

If instead we solve equations \(2.18\) only in terms of ˜

Y we find the following representation

for the volume form

\[1234\]2

Ω4,2 =

\[ ˜

Y d2 ˜

Y1\]\[ ˜

Y d2 ˜

Y2\] . 

\(3.5\)

\[ ˜

Y 12\]\[ ˜

Y 23\]\[ ˜

Y 34\]\[ ˜

Y 41\]

It is easy to check that \(3.3\) and \(3.5\) are related to each other by momentum conservation

\(2.20\). Independently of the chosen representation for the volume form, the volume function can be evaluated using \(2.35\) and gives the following manifestly parity symmetric answer: h1234i2\[1234\]2

Ω4,2 =

, 

\(3.6\)

hY 12ihY 23i\[ ˜

Y 12\]\[ ˜

Y 23\]

unique up to momentum conservation. Finally, we can extract the amplitude Atree using 4,2

\(2.37\) to get

δ4\(q\)δ4\(˜

q\)

Atree

4,2

= δ4\(p\)

, 

\(3.7\)

h12iλh23iλ\[12\]˜\[23\]

λ

˜

λ

where q, ˜

q are defined in \(2.9\). This formula agrees with the result found in \[12\]. 

This calculation can be easily generalized to any MHV amplitude. A particular repre-

– 12 –

sentation for the volume form reads

n−1 





^

hY i, i \+ 1i

hY 1, i \+ 1i

Ωn,2 =

dlog

∧ dlog

\(3.8\)

hY 1, i \+ 1i

hY 12i

i=2

h1 . . . ni2

=

hY d2Y

h

1ihY d2Y2i . . . hY d2Yn−2i . 

\(3.9\)

Y 12ihY 23i . . . hY 1ni

This result agrees with the one we get for the ordinary amplituhedron A\(2\)

. Let us notice

n,n−2

that, when Ωn,k is written explicitly as a logarithmic form \(3.8\), it can be easily compared with results in \[12\]: it is sufficient to project through a fixed Y , which results in removing all Y -dependence, and to consider the differentials to act on λ. Finally, the volume function for MHVn amplitudes is



\!2

h1 . . . ni2

P \[12ij\]hY iji

i<j

Ωn,2 =

. 

\(3.10\)

\[ ˜

Y 12\]2hY 12ihY 23i . . . hY 1ni

The results for MHV amplitudes are the parity conjugate of the previous formulæ. In particular, as for the MHV case, we do not need to triangulate the momentum amplituhedron Mn,n−2 since its dimension is already 2n − 4. The boundaries of Mn,n−2 are easily found and all take the form \[ ˜

Y ii \+ 1\] = 0 for i = 1, . . . , n. Moreover, for all points inside Mn,n−2 we find hY ii \+ 1i > 0 for i = 1, . . . , n and Si,i\+1,...,i\+p > 0 for i = 1, . . . , n and p = 1, . . . , n − 3. 

3.2

NMHV6 Amplitude

As a next step, we consider the first example where we need to triangulate the momentum amplituhedron in order to find the volume form. The positive Grassmannian G\+\(3, 6\) is nine-dimensional, while the momentum amplituhedron M6,3 is eight-dimensional and therefore the image of the positive Grassmannian through the map Φ

cannot be injective. In order to

\(Λ, ˜

Λ\)

find the volume form Ω6,3 we need to therefore focus on codimension-one cells in G\+\(3, 6\). 

There are two possible combinations of eight-dimensional cells whose images triangulate M6,3: T1 = \{\(123\) = 0, \(345\) = 0, \(561\) = 0\} , 

T2 = \{\(234\) = 0, \(456\) = 0, \(612\) = 0\} , \(3.11\)

where by \(ijk\) = 0 we denote the cell in G\+\(3, 6\) for which the minor \(ijk\) vanishes. The volume form can then be written as follows

\(612\)

\(234\)

\(456\)

\(123\)

\(345\)

\(561\)

Ω6,3 = Ω

\+ Ω

\+ Ω

= Ω

\+ Ω

\+ Ω

, 

\(3.12\)

6,3

6,3

6,3

6,3

6,3

6,3

\(ijk\)

where Ω

is the pushforward of the logarithmic differential form on the cell \(ijk\) = 0. 

6,3

\(123\)

In the following we focus on Ω

, the other terms can be found by cyclic shifts. We

6,3

parametrize the cell for which \(123\) = 0 using canonical coordinates and solve the relations

– 13 –

\(2.18\) to find

hY 12i

hY 23i

\[ ˜

Y ˆ

34\]

\[ ˜

Y 64\]

α1 =

, α

, α

, α

\(3.13\)

h

2 =

3 =

4 =

Y 13i

hY 13i

\[ ˜

Y ˆ

1ˆ

3\]

\[ ˜

Y ˆ

1ˆ

3\]

\[ ˜

Y 6ˆ

1\]

\[ ˜

Y 4ˆ

1\]

\[ ˜

Y 45\]

\[ ˜

Y 56\]

α5 =

, α6 =

, α7 =

, α8 =

, 

\(3.14\)

\[ ˜

Y ˆ

1ˆ

3\]

\[ ˜

Y ˆ

1ˆ

3\]

\[ ˜

Y 64\]

\[ ˜

Y 64\]

where we have denoted the following shifted variables

ˆ

h

h

˜

Y 23i

ˆ

Y 12i

Λ

˜

˜

˜

1 = ˜

Λ1 \+

Λ

Λ

Λ

h

2 , 

3 = ˜

Λ3 \+

2 . 

\(3.15\)

Y 13i

hY 13i

One can notice that the canonical variables are just an uplift of the formula found in \[12\]4. 

The push-forward is computed as

8

\(123\)

^

Ω

=

dlogα

6,3

i , 

\(3.16\)

i=1

which, using \(2.35\), leads to the following explicit form for the volume function \(123\)

\(hY 12i\[12456\] \+ hY 13i\[13456\] \+ hY 23i\[23456\]\)2 \(\[ ˜

Y 45\]h12345i \+ \[ ˜

Y 46\]h12346i \+ \[ ˜

Y 56\]h12356i\)2

Ω

=

. 

6,3

S123hY 12ihY 23i\[ ˜

Y 45\]\[ ˜

Y 56\]hY 1|5 \+ 6|4 ˜

Y \]hY 3|4 \+ 5|6 ˜

Y \]

\(3.17\)

After using our procedure \(2.37\) for extracting the amplitude, we find that the expression

\(3.17\) reduces to the formula found in \[12\]. While for the denominator it can be easily seen, the numerator requires a more careful analysis. The reader can convince oneself that the first bracket in the numerator will reduce to the “d6˜

λ” part:

\(hY 12i\[12456\] \+ hY 13i\[13456\] \+ hY 23i\[23456\]\)2 → δ4\(q\)\(˜

η4\[56\]˜ \+ ˜

η

\+ ˜

η

\)2 , \(3.18\)

λ

5\[64\]˜

λ

6\[45\]˜

λ

while the second bracket corresponds to the part proportional to “d6λ”: 2

\[ ˜

Y 45\]h12345i \+ \[ ˜

Y 46\]h12346i \+ \[ ˜

Y 56\]h12356i

→ δ4\(˜

q\) \(η1h23iλ \+ η2h31iλ \+ η3h12iλ\)2 . 

\(3.19\)

Finally, we can write the complete volume form Ω6,3 by using \(3.16\) and shifting labels: \(123\)

\(345\)

\(561\)

\(123\)

\(123\)

\(123\)

Ω





6,3 = Ω

\+ Ω

\+ Ω

= Ω

\+ Ω

\+ Ω

, 

\(3.20\)

6,3

6,3

6,3

6,3

6,3



6,3

i→i\+2

i→i\+4

and similarly for the volume function. One can check that the spurious divergencies, appearing \(123\)

as poles of the type hY i|j \+ k|l ˜

Y \] in Ω

, cancel in the sum and the form Ω

6,3

6,3 diverges

4The attentive reader will notice that we have a discrepancy of signs w.r.t. \[12\]. In our formulæ they are such that the canonical coordinates are all positive for positive data. 

– 14 –

logarithmically on the 15 boundaries of the momentum amplituhedron M6,3: hY ii \+ 1i = 0 , i = 1, . . . , 6 , 

\[ ˜

Y ii \+ 1\] = 0 , i = 1, . . . , 6 , 

Si,i\+1,i\+2 = 0 , i = 1, 2, 3 . 

\(3.21\)

Moreover, it is also easy to verify that for all points inside M6,3 one has hY ii \+ 1i > 0

and \[ ˜

Y ii \+ 1\] > 0. This immediately implies that the two-particle Mandelstam variables are positive. It is however not true for the three-particle Mandelstam variables. Let us focus first on

S123 = hY 12i\[ ˜

Y 12\] \+ hY 13i\[ ˜

Y 13\] \+ hY 23i\[ ˜

Y 23\] . 

\(3.22\)

It is clear that the first and last term in this expansion are explicitly positive, however the middle term has no definite sign. Using \(2.18\) we can further expand the Mandelstam variable to get



S123 = \(123\)

h1i⊥\(145\)\[12345\] \+ \(146\)\[12346\] \+ \(156\)\[12356\] \+ \(456\)\[23456\]

\+ h2i⊥\(245\)\[12345\] \+ \(246\)\[12346\] \+ \(256\)\[12356\] − \(456\)\[13456\]



\+ h3i⊥\(345\)\[12345\] \+ \(346\)\[12346\] \+ \(356\)\[12356\] \+ \(456\)\[12456\]



\+\(456\)

h4i⊥\(124\)\[12456\] \+ \(234\)\[23456\] \+ \(134\)\[13456\] \+ \(123\)\[12356\]

\+ h5i⊥\(125\)\[12456\] \+ \(235\)\[23456\] \+ \(135\)\[13456\] − \(123\)\[12346\]



\+ h6i⊥\(126\)\[12456\] \+ \(236\)\[23456\] \+ \(136\)\[13456\] \+ \(123\)\[12345\] , \(3.23\) where we have organized the expansion to have all brackets explicitly positive. Then, the manifestly negative terms present in the expansion can in principle dominate over the positive terms making the Mandelstam variable negative. Let us first remark that a careful numerical analysis shows that S123 is negative only in a very small subregion of M6,3 for generic positive data. Moreover, when the kinematic data is taken to be on the moment curve \(2.33\), S123

is positive. We can now state a sufficient condition for S123 to be positive for points inside M6,3: we impose the constraints on the kinematics

h1i⊥ ˇ

\[1\] − h2i⊥ ˇ

\[2\] \+ h3i⊥ ˇ

\[3\] \+ h4i⊥ ˇ

\[4\] − h5i⊥ ˇ

\[5\] \+ h6i⊥ ˇ

\[6\] > 0 , 

\(3.24\)

where with \[ˇi\] we denote the five-bracket with the index i omitted. By studying the remaining independent three-particle Mandelstam variables, i.e. S234 and S345, we find the same type of relations \(3.24\) with the signs cyclically shifted by, respectively, one and two positions. For all kinematic data satisfying these three conditions, the momentum amplituhedron M6,3 is a positive geometry. At the moment it is unclear what is the geometric interpretation of these inequalities. 

– 15 –

Factorization properties. One important property of the amplitudes is that they factorize into products of smaller amplitudes when planar Mandelstam variables vanish. This is reflected in the amplituhedron geometry in the fact that, when we approach one of its boundaries, then the volume form factorizes. In the ordinary amplituhedron, the statement is even more general: the geometry itself factorizes as a cartesian product of two positive geometries. For the momentum amplituhedron the situation is slightly more involved and the factorization properties rather come from the amalgamation of on-shell diagrams inside the positive Grassmannian \[3\]. To perform the amalgamation we need to start with two planes CL ∈ G\(kL, nL\) and CR ∈ G\(kR, nR\), where nL,R denote the number of particles in the left and right diagram, respectively, and kL,R is their respective helicity. Then we take their direct product, which brings us to ˆ

C ∈ G\(kL \+ kR, nL \+ nR\), and subsequently we project the product to C ∈ G\(kL \+ kR − 1, nL \+ nR − 2\). As a result, the C-matrix describing the cell where the factorization takes place is composed of the two overlapping C-matrices corresponding to the left and the right amplitude. 

To illustrate how the amalgamation works in the context of the momentum amplituhedron, we study it in details for n = 6 and k = 3. We encounter three different types of amalgamations, depending on which boundary we approach. Let us start by taking S123 → 0. This boundary is parametrized by a seven-dimensional positroid cell for which \(123\) = \(456\) = 0. 

This cell can be written in terms of positive coordinates as





1 α5 \+ α7 α5α6

0

0

0

C





6,3|

=

0

1

α

. 

\(3.25\)

S

6

α2 \+ α4 α2α3 0

123=0





0

0

0

1

α3 α1

This matrix can be regarded as coming from the amalgamation of two positive matrices corresponding to four-point MHV amplitudes. We can indeed recognize that the two matrices inside the \(2 × 4\) boxes are positive and both correspond to M4,2. 

The second type of boundaries we consider is \[ ˜

Y ii \+ 1\] → 0. Let us focus on \[ ˜

Y 56\] → 0. 

We expect this limit to describe the case when particles 5 and 6 become collinear, and the amplitude Atree reduces to Atree. It is indeed reflected in the form of the matrix defining this 6,3

5,2

boundary. We can see it by studying the seven-dimensional cell parametrizing the boundary

\[ ˜

Y 56\] → 0:





1 α3 \+ α5 \+ α7 \(α3 \+ α5\)α6 α3α4 0 0

C





6,3|

=

0

1

α

, 

\(3.26\)

\[ ˜

Y 56\]=0

6

α4 α2 0





0

0

0

0

1 α1

where one can recognize the positive matrix defining M5,2 in the upper left corner. Notice that the value of k reduces in this limit. Finally, we consider the limit hY ii \+ 1i → 0 which should correspond to a collinear limit with k preserved. Indeed, the boundary with hY 56i = 0

– 16 –

corresponds to the following seven-dimensional cell in the positive Grassmannian:





1 α5 \+ α7

α5α6

0

0

0

C





6,3|

=

0

1

α

. 

\(3.27\)

hY 56i=0

3 \+ α6 α3α4

0

0





0

0

1

α4 α2 α1

The highlighted part corresponds to the positive 3 × 5 matrix present in the definition of M5,3, as expected. 

Comments on positive Mandelstam variables. We finish by commenting on the sufficient conditions for the kinematic data which guarantee positivity for all planar Mandelstam variables. We will study the case k = 3 in details. Let us introduce the following combination of brackets relevant in this case:

Pi

= hi

1i2i3,j1j2j3

1i⊥\[i2i3j1j2j3\] − hi2i⊥\[i1i3j1j2j3\] \+ hi3i⊥\[i1i2j1j2j3\] . 

\(3.28\)

We checked that, for any n and k = 3, the conditions guaranteeing positivity for all Mandelstam variables Si,i\+1,...,i\+p read:

Pi

\+ P

> 0

i

1i2i3,j1j2j3

j1j2j3,i1i2i3

1i2i3 ∈ Ii,p, 

j1j2j3 ∈ ¯

Ii,p , 

\(3.29\)

where we defined Ii,p := \{i, i \+ 1, ..., i \+ p\}. In particular we see that the relations \(3.24\) which we found in the previous section to have S123 > 0 can be written as P123,456 \+ P456,123 > 0 . 

\(3.30\)

After a preliminary study of the Mandelstam variables for higher k we have observed that a similar set of relations should be valid also in that case. However, it is unclear to us at the moment what will be the general form of such relations, whether they also provide necessary conditions and what is their geometric interpretation. 

4

Conclusions and Outlook

In this paper we have introduced a novel geometric object, the momentum amplituhedron Mn,k, which computes tree-level scattering amplitudes in N = 4 SYM directly in momentum space. To accomplish this, we have defined bosonized spinor helicity variables \(Λi, ˜

Λi\), for

which we imposed specific positivity conditions, i.e. we demanded the matrices Λ⊥ and ˜

Λ

to be positive. The image of the positive Grassmannian G\+\(k, n\) through this positive data defines a positive geometry if additional constraints on kinematics are imposed. Then, the volume form on the momentum amplituhedron Mn,k encodes the tree-level amplitude Atree. 

n,k

Additionally, we showed that the positive kinematics, when projected to the spinor helicity space, satisfies the conjecture formulated in \[12\]; in particular, it obeys the sign-flip conditions postulated there. 

– 17 –

As already mentioned, in the cases of MHV and MHV all planar Mandelstam variables are positive. In order for this to be true in other helicity sectors, and to guarantee the momentum amplituhedron to be a positive geometry, the positive region of the \(Λ, ˜

Λ\)-space needs to be

restricted further. The nature of such additional constraints on the kinematical data remains however unclear to us. Nevertheless, we checked algebraically up to a large number of particles n that the restricted space is not empty. Extensive numerical tests showed that it is actually rather large. Providing necessary and sufficient conditions for positivity of planar Mandelstam variables is an open problem and is left for future work. 

Our paper opens various interesting avenues of investigation. The first question is whether a generalization of our construction to loop amplitudes is possible. There exists a natural extension of tree-level differential forms to loop integrands, as suggested in \[12\]. Bosonizing those formulæ in a similar fashion as for tree level would therefore be a step worth pursuing. 

Then the underlying positive geometry should bear similarities with the ordinary loop-level amplituhedron. Perhaps the most fascinating question is whether we can extend our construction to other theories. For instance, our work could shed light on positive geometries in twistor theories in higher dimensions \[20, 21\]. Moreover, the momentum amplituhedron is formulated directly in spinor helicity variables, which are universal variables for massless theories in four dimensions \(and beyond\). This opens the pathway for investigating positive geometries for non-planar, less- or non-supersymmetric theories. For instance, in \[8\] the differential forms for Yang-Mills and non-linear sigma model were found. These forms do not have logarithmic singularities, which would indicate that there is no underlying positive geometry. However, already for N = 4 SYM one needs to factorize δ4\(q\) to get a logarithmic form on the spinor helicity space, see \[12\]. Nevertheless, this problem disappears when we consider the forms on the momentum amplituhedron, as we showed in this paper. We anticipate that similar, but more complicated, behaviour might be possible for less- or non-supersymmetric theories. 

5

Acknowledgments

This work was partially funded by the Deutsche Forschungsgemeinschaft \(DFG, German Research Foundation\) – Projektnummern 404358295 and 404362017. M. P. would like to thank “Fondazione A. Della Riccia” for financial support. 

A

Orthogonal complements

In this appendix we set the conventions for orthogonal complements we use in the main body. 

Let us consider a matrix





b11 b12 . . . b1n

b



21 b22 . . . b2n

B = 





. 

. 

\(A.1\)

. 

.. .. 

.. 



. 

. 

. 

. 





bk1 bk2 . . . bkn

– 18 –

It describes a k-plane B in an n-dimensional space. We can therefore define its orthogonal complement B⊥: an \(n − k\)-plane in n dimensions. Such plane can be parametrized by an \(n − k\) × n matrix





b⊥

b⊥

. . . 

b⊥

11

12

1n



b⊥

b⊥

. . . 

b⊥



21

22

2n

B⊥ = 





. 

. 

\(A.2\)

. 

.. 

. . 

.. 



. 

. 

. 

. 







b⊥

b⊥

. . . b⊥

n−k 1

n−k 2

n−k n

Matrices related by a GL\(n − k\) transformation acting on rows of B⊥ define the same plane B⊥, with a different choice of basis. The maximal minors of matrices B and B⊥ are related to each other

\(i1, . . . , in−k\)⊥

B = g i

\(j

1,...,in−k ,j1,...,jk

1, . . . , jk\)B , 

\(A.3\)

where \{i1, . . . , in−k, j1, . . . , jk\} = \{1, . . . , n\} and g is a scalar, independent of the minors we consider. In our considerations we will fix a particular basis of the orthogonal complement, which will fix the value for g. We motivate it by considering B to be an element of the Grassmannian G\(k, n\). We choose a patch in the Grassmannian such that B = \(**1**k×k|b\) , 

\(A.4\)

and the basis of its orthogonal complement to be

B⊥ = −bT |**1**



\(n−k\)×\(n−k\)

. 

\(A.5\)

It is easy to check, by taking \{j1, . . . , jk\} = \{1, . . . , k\}, that in this case g = \(−1\)k\(n−k\) . 

\(A.6\)

It is important to notice that the relation \(A.3\) is not an involution. In the most general case \(j1, . . . , jk\)B = ˜

g j

\(i

1,...,jk ,i1,...,in−k

1, . . . , in−k\)⊥

B . 

\(A.7\)

For this to agree with \(A.3\) we need to fix

˜

g = \(−1\)k\(n−k\)g = 1 . 

\(A.8\)

In order to be consistent, we need to therefore indicate which matrices from the main body of the paper we treat as B and which ones as B⊥. The rule we adopt is that the positive matrices will all play the role of B. This implies the following relations between brackets we

– 19 –

introduced in the main text:

\(j1, . . . , jk\) = j

\(i

1,...,jk ,i1,...,in−k

1, . . . , in−k\)⊥ , 

\(A.9\)

hj1, . . . , jk−2i⊥ = j

hi

1,...,jk−2,i1,...,in−k\+2

1, . . . , in−k\+2i , 

\(A.10\)

\[j1, . . . , jk\+2\] = j

\[i

1,...,jk\+2,i1,...,in−k−2

1, . . . , in−k−2\]⊥ , 

\(A.11\)

where the round, angle and square brackets above are the minors of the positive matrices C, Λ⊥ and ˜

Λ, respectively. 

B

Proof of the relation \(Xpq\) = hY pqi

With the conventions for orthogonal complements from the previous appendix, we are able to prove the formula \(2.28\):

X

\(X p q\) =

\(i1 . . . ik−2 p q\)hi1 . . . ik−2i⊥ =

\(B.1\)

i1<...<ik−2

X

=

i

\(j

1...ik−2 p q j1...jn−k

1 . . . jn−k\)⊥i1...ik−2 j1...jn−k p qhj1 . . . jn−k p qi \(B.2\)

j1<...<jn−k

X

=

\(j1 . . . jn−k\)⊥hj1 . . . jn−k p qi = hY p qi . 

\(B.3\)

j1<...<jn−k

C

Momentum Conservation

In this appendix we show that the momentum amplituhedron lives in the co-dimension four surface defined by the conditions:

n

X 

a 

˙

a

Y ⊥ · Λ

˜

Y ⊥ · ˜

Λ

= 0 , 

a, ˙a = 1, 2 . 

\(C.1\)

i

i

i=1

Let us start by observing that

0 = Y ⊥ · Y = Y ⊥ · Λ · C⊥ . 

\(C.2\)

Therefore the 2-dimensional subspace Y ⊥ · Λ is contained in the k-dimensional subspace \(C⊥\)⊥ = C. Analogously, we can deduce that ˜

Y ⊥ · ˜

Λ ⊆ C⊥. Then, the two subspaces Y ⊥ · Λ

and ˜

Y ⊥ · ˜

Λ are themselves orthogonal, as encoded in formula \(C.1\). 

– 20 –

D

Positive Mandelstam variables for k = 2

We would like to prove that, for all MHV momentum amplituhedra, every planar Mandelstam variable is positive, namely:

X

SI =

hY j1j2i\[ ˜

Y j1j2\] > 0, 

I = \{i, i \+ 1, ..., i \+ p\} . 

\(D.1\)

j1,j2∈I

First, let us observe that, for k = 2:

hY j1j2i = hi⊥\(j1j2\) , 

\(D.2\)

where hi⊥ = h1 . . . ni is positive. Then we can rewrite: X

SI = h1...ni

\(j1j2\)\(ab\)\[abj1j2\] . 

\(D.3\)

j1<j2∈I,a<b

There are only two cases for which the bracket \[abj1j2\] is negative: a < j1 < b < j2 or j1 < a < j2 < b. In particular, we observe that if a, b 6∈ I then \[abj1j2\] > 0. For b ∈ I and a < j1 < b < j2, together with the term

\(j1j2\)\(ab\)\[abj1j2\] < 0 , 

\(D.4\)

in the sum there are two additional terms proportional to \[abj1j2\]: \(bj2\)\(aj1\)\[aj1bj2\] \+ \(j1b\)\(aj2\)\[aj2j1b\] , 

\(D.5\)

both positive. Using Schouten identity, the three terms together add up to zero: \(j1j2\)\(ab\)\[abj1j2\] \+ \(bj2\)\(aj1\)\[aj1bj2\] \+ \(j1b\)\(aj2\)\[aj2j1b\] = 0 . 

\(D.6\)

Analogously, for the case j1 < a < j2 < b, together with the term \(j1j2\)\(ab\)\[abj1j2\] < 0 , 

\(D.7\)

we have also two positive terms

\(aj2\)\(j1b\)\[j1baj2\] \+ \(j1a\)\(j2b\)\[j2bj1a\] . 

\(D.8\)

Again, using Schouten identity, the three terms together add up to zero. We therefore conclude that all negative terms are cancelled and the Mandelstam variables are positive. 

– 21 –

References

\[1\] N. Arkani-Hamed, F. Cachazo, C. Cheung, and J. Kaplan, A Duality For The S Matrix, JHEP

1003 \(2010\) 020, \[arXiv:0907.5418\]. 

\[2\] L. J. Mason and D. Skinner, Dual Superconformal Invariance, Momentum Twistors and Grassmannians, JHEP 11 \(2009\) 045, \[arXiv:0909.0250\]. 

\[3\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. B. Goncharov, A. Postnikov, and J. Trnka, Grassmannian Geometry of Scattering Amplitudes. Cambridge University Press, 2016. 

\[4\] R. Britto, F. Cachazo, and B. Feng, New recursion relations for tree amplitudes of gluons, Nucl. 

Phys. B715 \(2005\) 499–522, \[hep-th/0412308\]. 

\[5\] R. Britto, F. Cachazo, B. Feng, and E. Witten, Direct proof of tree-level recursion relation in Yang-Mills theory, Phys. Rev. Lett. 94 \(2005\) 181602, \[hep-th/0501052\]. 

\[6\] N. Arkani-Hamed and J. Trnka, The Amplituhedron, JHEP 1410 \(2014\) 30, \[arXiv:1312.2007\]. 

\[7\] N. Arkani-Hamed, Y. Bai, and T. Lam, Positive Geometries and Canonical Forms, JHEP 11

\(2017\) 039, \[arXiv:1703.0454\]. 

\[8\] N. Arkani-Hamed, Y. Bai, S. He, and G. Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet, JHEP 05 \(2018\) 096, \[arXiv:1711.0910\]. 

\[9\] N. Arkani-Hamed, P. Benincasa, and A. Postnikov, Cosmological Polytopes and the Wavefunction of the Universe, arXiv:1709.0281. 

\[10\] B. Eden, P. Heslop, and L. Mason, The Correlahedron, JHEP 09 \(2017\) 156, 

\[arXiv:1701.0045\]. 

\[11\] N. Arkani-Hamed, Y.-T. Huang, and S.-H. Shao, On the Positive Geometry of Conformal Field Theory, arXiv:1812.0773. 

\[12\] S. He and C. Zhang, Notes on Scattering Amplitudes as Differential Forms, JHEP 10 \(2018\) 054, \[arXiv:1807.1105\]. 

\[13\] E. Witten, Perturbative gauge theory as a string theory in twistor space, Commun. Math. Phys. 

252 \(2004\) 189–258, \[hep-th/0312171\]. 

\[14\] R. Roiban, M. Spradlin, and A. Volovich, On the tree level S matrix of Yang-Mills theory, Phys. 

Rev. D70 \(2004\) 026009, \[hep-th/0403190\]. 

\[15\] N. Arkani-Hamed, H. Thomas, and J. Trnka, Unwinding the Amplituhedron in Binary, JHEP

01 \(2018\) 016, \[arXiv:1704.0506\]. 

\[16\] N. Arkani-Hamed, A. Hodges, and J. Trnka, Positive Amplitudes In The Amplituhedron, JHEP

08 \(2015\) 030, \[arXiv:1412.8478\]. 

\[17\] L. Ferro, T. Lukowski, A. Orta, and M. Parisi, Towards the Amplituhedron Volume, JHEP 03

\(2016\) 014, \[arXiv:1512.0495\]. 

\[18\] L. Ferro, T. Lukowski, and M. Parisi, Amplituhedron meets Jeffrey Kirwan residue, J. Phys. 

A52 \(2019\), no. 4 045201, \[arXiv:1805.0130\]. 

\[19\] J. L. Bourjaily, Positroids, Plabic Graphs, and Scattering Amplitudes in Mathematica, 

arXiv:1212.6974. 

– 22 –

\[20\] Y. Geyer and L. Mason, Polarized Scattering Equations for 6D Superamplitudes, Phys. Rev. 

Lett. 122 \(2019\), no. 10 101601, \[arXiv:1812.0554\]. 

\[21\] Y. Geyer and L. Mason, The M-theory S-matrix, arXiv:1901.0013. 

– 23 –


# Document Outline

+ 1 Introduction 
+ 2 The Definition  
	+ 2.1 The Ordinary Amplituhedron 
	+ 2.2 The Momentum Amplituhedron 
	+ 2.3 Momentum Amplituhedron Volume Form 

+ 3 Examples  
	+ 3.1 MHV/MHV Amplitudes 
	+ 3.2 Amplitude 

+ 4 Conclusions and Outlook 
+ 5 Acknowledgments 
+ A Orthogonal complements 
+ B Proof of the relation  
+ C Momentum Conservation 
+ D Positive Mandelstam variables for k=2



