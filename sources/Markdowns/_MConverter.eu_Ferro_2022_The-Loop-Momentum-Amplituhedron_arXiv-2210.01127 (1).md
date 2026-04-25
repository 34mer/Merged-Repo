Prepared for submission to JHEP

The Loop Momentum Amplituhedron

Livia Ferro and Tomasz Lukowski, 

Department of Physics, Astronomy and Mathematics, 

University of Hertfordshire, 

Hatfield, Hertfordshire, AL10 9AB, United Kingdom

E-mail: l.ferro@herts.ac.uk, t.lukowski@herts.ac.uk

Abstract: In this paper we focus on scattering amplitudes in maximally supersymmetric Yang-Mills theory and define a long sought-after geometry, the loop momentum amplituhedron, which we conjecture to encode tree and \(the integrands of\) loop amplitudes in spinor helicity variables. Motivated by the structure of amplitude singularities, we define an extended positive space, which enhances the Grassmannian space featuring at tree level, and a map which associates to each of its points tree-level kinematic variables and loop momenta. 

The image of this map is the loop momentum amplituhedron. Importantly, our formulation provides a global definition of the loop momenta. We conjecture that for all multiplicities and helicity sectors, there exists a canonical logarithmic differential form defined on this space, and provide its explicit form in a few examples. 

arXiv:2210.01127v1 \[hep-th\] 3 Oct 2022

Contents

1

Introduction

1

2

Amplituhedra

3

2.1

The Momentum Amplituhedron Revisited

3

2.2

The Amplituhedron

5

2.3

Boundaries of Amplituhedra

6

3

The Loop Momentum Amplituhedron

7

4

Examples

10

5

Conclusions and Outlook

13

6

Acknowledgements

14

A Kinematic Variables

14

1

Introduction

In recent years we have seen tremendous advances in new geometric formulations of observ-ables in Quantum Field Theories, known nowadays under the name of positive geometries

\[1\]. These are defined recursively as regions with boundaries of all codimensions, where each boundary is again a positive geometry. Importantly, they are equipped with a unique differential form with logarithmic singularities along all boundaries – the canonical form – which, for physically relevant positive geometries, is a physical quantity. A striking feature of these geometries is that from their definition, by imposing only positivity constraints on some external data, they encode physical properties, such as locality and unitarity, in their boundary structure. 

In this paper we focus on positive geometries for scattering amplitudes in N “ 4 super Yang-Mills \(sYM\) theory, i.e. amplituhedra – see \[2, 3\] for extensive reviews. Two geometries have been defined in this theory: the amplituhedron \[4\] and the momentum amplituhedron

\[5\]. The amplituhedron, which has been the prime example of a positive geometry, is defined in momentum twistor space and is relevant for tree- and loop-level expectation values of Wilson loops, i.e. scattering amplitudes with the maximally-helicity-violating \(MHV\) part factored out. Importantly, since ordering is crucial in the definition of momentum twistors, the amplituhedron encodes only the planar sector of N “ 4 sYM. The momentum amplituhedron is instead formulated in the non-chiral spinor helicity space and therefore provides a natural

– 1 –

language to extend the positive geometry construction to the non-planar sector. However, until now, it was defined only for amplitudes at tree level. The natural question arises whether there exists a positive geometry formulated in the non-chiral spinor helicity space which also produces the amplitude integrands at loop level. In this paper we provide an affirmative answer to this question and formulate the long sought-after geometry for loop amplitudes in spinor helicity space – the loop momentum amplituhedron. 

Finding the loop momentum amplituhedron has been a long-standing and important goal since the inception of the tree-level geometry. 

One of the main obstacles that had

been hindering this construction was to find a proper, global definition of the off-shell loop momentum in the spinor helicity space. Indeed, while in the dual space, where momentum twistors are defined, the loop momentum is uniquely determined up to a global shift, in the Feynman approach in momentum space we can redefine it independently for each Feynman diagram. The final answer, after performing Feynman integrals, does not depend on these redefinitions, however, the integrand itself changes significantly. In particular, this leads to introducing unphysical singularities that should not arise in the geometric approach. In this paper we resolve this problem by providing a global definition of the loop momenta that serve as parameters in the map defining the loop momentum amplituhedron. To construct this map, we emphasize an important fact about the singularity structures of scattering amplitudes and expectation values of Wilson loops. While at tree level their singularities differ, at loop level there is a one-to-one correspondence between the singularities of integrands for these quantities. Then, since amplituhedra encode physical singularities in the structure of their boundaries, this statement is valid for the boundaries of the geometries: while at tree level the amplituhedron and momentum amplituhedron boundaries are different, at loop level they can be mapped to each other in a simple way. Led by this observation, we draw inspiration from the loop amplituhedron and find its counterpart in spinor helicity variables. For this purpose, we use the relation between momentum twistors and spinor helicity variables, which first appeared in the Grassmannian formulations of scattering amplitudes in these two spaces \[6\]. 

This allows us to define the loop momentum amplituhedron. By enhancing the Grassmannian space G\`pk, nq present at tree level with L two-planes and requiring additional positivity constraints, we find that the L-loop momentum amplituhedron is the image of a map which associates to every point of this extended positive space the tree-level variables pλ, ˜

λq and the

loop momentàp for p “ 1, . . . , L. 

This paper is organized as follows. In section 2 we review the basic facts about amplituhedra. In particular, we start by recalling, and afterwards refining, the definition of the momentum amplituhedron at tree level. After a review of the amplituhedron, we present the motivation for our definition of momentum amplituhedron at loop level. Section 3 is the main part of the paper and contains the definition of the loop momentum amplituhedron. We then present a few examples in section 4, before closing with conclusions and outlook. Appendix

A collects the definitions of all variables used throughout the paper. 

– 2 –

2

Amplituhedra

In this section we provide a brief review of the definitions of the momentum amplituhedron Mn,k at tree level and the amplituhedron An,k1,L at tree and loop level. This will set the stage for our new definition of the momentum amplituhedron at loop level that we introduce in the subsequent section. 

2.1

The Momentum Amplituhedron Revisited

Let us start by recalling the original definition of the \(tree\) momentum amplituhedron introduced in \[5\]. First, we consider the Grassmannian Gpk, nq, which is the space of all k ˆ n matrices modulo GLpkq row transformations, and the positive Grassmannian G\`pk, nq, which is the subset of Gpk, nq consisting of all positive matrices, i.e. matrices with all maximal ordered minors positive. We also introduce a pair of fixed matrices pΛ, ˜

Λq and demands that

˜

Λ P M\`pk \` 2, nq is a positive matrix and Λ P M\`,τ pn ´ k \` 2, nq is a twisted positive matrix, i.e. a matrix whose orthogonal complement is a positive matrix. Then, the momentum amplituhedron Mn,k “ ΦΛ,˜ΛpG\`pk, nqq, for 2 ď k ď n ´ 2, is defined as the image of the positive Grassmannian G\`pk, nq through a linear map Φ

specified by the two fixed matrices Λ and

Λ, ˜

Λ

˜

Λ:

Φ

: G

Λ, ˜

Λ

\`pk, nq Ñ Gpk, k \` 2q ˆ Gpn ´ k, n ´ k \` 2q . 

\(2.1\)

Explicitly, we have for pY, ˜

Y q P Gpk, k \` 2q ˆ Gpn ´ k, n ´ k \` 2q and C “ pc 9αiq P G\`pk, nq that

ÿ

9

ÿ

9

Y A

A

˜ A

α “

pcKqαiΛA

i , 

˜

Y

c Λ

9

α “

9

αi

i , 

\(2.2\)

i

i

where pcKqαi for α “ 1, . . . , k and i “ 1, . . . , n are the elements of the orthogonal complement CK of the matrix C. 

The linear map Φ

can be further composed with a projection

Λ, ˜

Λ

P

: G

Λ, ˜

Λ

pk, k \` 2q ˆ Gpn ´ k, n ´ k \` 2q Ñ Gp2, nq ˆ Gp2, nq , 

\(2.3\)

to extract the familiar spinor helicity variables

ÿ

ÿ

9

λa

a

˜ A

i “

pY KqA ΛA

i , 

˜

λ 9ai “

p ˜

Y Kq 9a Λ

9

A

i . 

\(2.4\)

A

9

A

The image Mn,k :“ pPΛ,˜Λ ˝ ΦΛ,˜ΛqpG\`pk, nqq of the positive Grassmannian through the composition of these maps is then a region defined directly in spinor helicity space. 

As

shown in \[5\], definition \(2.2\) implies that for any point pλ, ˜

λq P Mn,k the spinor brackets

xiì 1y :“ λ1λ2

λ1

˜

λ2

˜

λ1

i

j ´ λ2

i

j ą 0 and riì 1s :“ ˜

λ1i j ´ ˜λ2i j ą 0 are positive. Moreover, for

particular choices of matrices Λ and ˜

Λ also all planar Mandelstam variables si,ì1,...,ìj ą 0

are positive, ensuring that the boundary structure of Mn,k reflects the correct singularity structure of the tree-level amplitudes in planar N “ 4 sYM. Additionally, the following sign

– 3 –

flip patterns are satisfied by the spinor brackets: tx12y, x13y, . . . , x1nyu has k ´ 2 sign flips , 

\(2.5\)

tr12s, r13s, . . . , r1nsu has k sign flips . 

\(2.6\)

Before moving on to the definition of the amplituhedron, we want to make an important comment regarding the properties of Mn,k that has not been previously spelled out in the literature but will be crucial in the following. Notice that the definitions \(2.2\) and \(2.4\)

trivially imply that for any point pλ, ˜

λq P Mn,k we have

ÿ

ÿ

λa

˜

i pcKqαi “ 0 , 

λ 9aic 9αi “ 0 , 

\(2.7\)

i

i

and therefore1 ˜

λ ¨ C “ 0 and λ Ă C. Let us make the latter statement more precise. To this extent, we will use the observation made in \[5\] that allows to rewrite the λ part of \(2.2\) and

\(2.4\) in an alternative way. Let us modify the previous definition and define a map φΛK,˜Λ

labelled by two positive matrices ΛK P M\`pk ´ 2, nq and ˜

Λ P M\`pk \` 2, nq:

φ

: G

ΛK, ˜

Λ

\`pk, nq Ñ Gp2, nq ˆ Gp2, nq , 

\(2.8\)

that will generalize the compositions of functions in our original definition. To every element in the positive Grassmannian G\`pk, nq it associates a pair of matrices pλ, ˜

λq:

ÿ

ÿ

9

λa

a

˜ A

i “

pXKqαcαi , 

˜

λ 9ai “

p ˜

Y Kq 9a Λ

9

A

i , 

\(2.9\)

α

9

A

where X ¯a

ř

\`

α “

ΛK˘¯a c

i

i

αi P Gpk ´ 2, kq. 

Then Mn,k “ φΛK,˜ΛpG\`pk, nqq. The equivalence

between this definition and the one in \(2.4\) descends from the fact that for all i, j we have xijy “ xY ijy “ pXijqC , where the last equality was proven in \[5\] . Importantly, the variables X that we introduced allow one to construct a GLpkq matrix

˜

¸

XK2,k

G “

, 

\(2.10\)

0k´2,2 1k´2,k´2

such that

˜

¸

λ

GC “

, 

\(2.11\)

c

where c P M pk ´ 2, nq. Therefore, for any element C P G\`pk, nq and for the corresponding image point pλpCq, ˜

λpCqq P Mn,k, it is always possible to find a representative for C such that the first two rows of the matrix C are the λs. 

1These relations between λ, ˜

λ and C were the starting point of the development of the Grassmannian approach to scattering amplitudes in \[7\]. Here, instead they rather result from the definition of the momentum amplituhedron. 

– 4 –

The final comment in this section is related to the fact that points in the positive Grassmannian space G\`pk, nq featuring in the definition of the momentum amplituhedron have a well-known relation to the points in the positive Grassmannian space G\`pk1, nq “ G\`pk´2, nq in the definition of the amplituhedron \[6\]. Provided λ P Gp2, nq, and using relation \(2.11\), one can define the matrix

č “ Qc , 

\(2.12\)

where

xi ´ 1 iyδi

Q

\`1,j \` xi ì 1yδi´1,j \` xì 1 i ´ 1yδi,j

ij “

. 

\(2.13\)

xi ´ 1 iyxi ì 1y

Importantly, we checked in various examples that if λ is inside the momentum amplituhedron Mn,k, then č P G\`pk ´ 2, nq is a positive matrix, and we conjecture this holds for all n and k. 

2.2

The Amplituhedron

Similar to the momentum amplituhedron, the L-loop amplituhedron An,k1,L can be defined \[8\]

as the image of a particular space, generalizing the positive Grassmannian, through a linear map

Φ

L

L

Z : G\`pk1, nq ˆ Gp2, nq

Ñ Gpk1, k1 \` 4q ˆ Gp2, k1 \` 4q , 

\(2.14\)

where k1 “ k ´ 2 and Z P M\`pk1 \` 4, nq is a positive matrix. The map ΦZ assigns to every point C “ pcαiq P G\`pk1, nq and a collection of points Dl “ pdl,γiq P Gp2, nq the values n

n

I

ÿ

ÿ

pYZ qα “

cαi ZIi , 

LIl,γ “

dl,γi ZIi , 

\(2.15\)

i“1

i“1

with l “ 1, . . . , L enumerating the loops and γ “ A, B. The domain G\`pk1, nq ˆ Gp2, nqL of ΦZ is defined as all points pC, D1, . . . , DLq P Gpk1, nq ˆ Gp2, nq ˆ . . . ˆ Gp2, nq such that all matrices

¨

˛

Dl1

˜

¸

˚

. ‹

´

¯

D

. 

l

˚

. ‹

C , 

1

, 

. . . 

˚

‹ , 

\(2.16\)

C

˚D ‹

˝

lL ‚

C

are positive for li “ 1, . . . , L. Then the loop amplituhedron is defined as A

L

n,k1,L “ ΦZ pG\`pk1, nq ˆ Gp2, nq q . 

\(2.17\)

As for the momentum amplituhedron, we can compose ΦZ with a projection P

L

L

Z : Gpk1, k1 \` 4q ˆ Gp2, k1 \` 4q

Ñ Gp4, nq ˆ Gp2, 4q , 

\(2.18\)

– 5 –

and define the bosonic part of the momentum twistors za as i

ÿ

za

a

i “

pY K

Z qI Z I

i . 

\(2.19\)

I

The momentum twistor line parametrizing the loop momenta is specified by a pair of points pABql where

ÿ

za

aLI

l,γ “

pY K

Z qI

l,γ . 

\(2.20\)

I

This allows us to define the loop amplituhedron directly in the momentum twistor space A

L

n,k1,L “ pPZ ˝ ΦZ qpG\`pk1, nq ˆ Gp2, nq q . 

\(2.21\)

For completeness, we recall an important property of An,k1,L that follows from the definitions of the maps ΦZ and PZ: given a point pzi, pABq1, . . . , pABqLq P An,k1,L, the brackets of momentum twistors xi ì 1 j j \` 1y ą 0 are positive, where xijkly “ IJKLzI zJ zKzL. Simi-i

j

k

l

larly, for brackets involving loop variables we have xpABql i ì 1y ą 0 and xpABqapABqby ą 0. 

Moreover, points in the loop amplituhedron are known to have the following sign flip patterns txpABqa12y, xpABqa13y, . . . , xpABqa1nyu has pk1 \` 2q sign flips for each loop , tx1234y, x1235y, . . . , x123nyu has k1 sign flips . 

\(2.22\)

2.3

Boundaries of Amplituhedra

The amplituhedra we reviewed in the previous sections are conjectured2 to define positive geometries3 \[1\] and therefore can be equipped with canonical differential forms that encode physical quantities. 

For the tree momentum amplituhedron, the canonical form encodes the tree-level scattering amplitudes in planar N “ 4 sYM, written in the non-chiral spinor helicity superspace. On the other hand, the loop amplituhedron canonical form provides the loop integrand in the same theory but written in the momentum twistor space instead. 

Importantly, in the latter case the tree-level MHV factor is removed. This last statement has significant implications for the singularity structure of the canonical form of the amplituhedron, and therefore for the boundary structure of the amplituhedron itself. In particular, at tree level, the codimension one boundaries of the momentum amplituhedron Mn,k are given by the collinear limits, xi ì 1y “ 0 , ri ì 1s “ 0, and the factorization limits si,ì1...,ìp “ 0 , with p “ 2, . . . , n ´ 4. On the other hand, for the amplituhedron the facets are given by the points satisfying xi ì 1 j j \` 1y “ 0. When j “ ì 2, the boundary xi ì 1 ì 2 ì 3y “ 0 translates into the boundary riì 1s “ 0 of the tree momentum amplituhedron. When j ą ì 2, the boundary corresponds to a factorization channel and one can map it to the boundary of the momentum amplituhedron where one of the planar Mandelstam 2There is no general proof of this fact, but in all cases where the explicit answer has been found, one can check that it is indeed true. 

3To be more precise they are weighted positive geometries as advocated in \[9\]. 

– 6 –

variables vanishes. However, since the MHV amplitude is factored out for the amplituhedron, there is no boundary of the amplituhedron that would correspond to xi ì 1y “ 0. Therefore, the boundary structure of the tree momentum amplituhedron is very different from the boundary structure of the tree amplituhedron. This has the important implication that there is no simple map relating the points in the two amplituhedra. However, there exists a direct translation of all singularities of loop-level integrands from momentum twistors to spinor helicity space:

ÿ

2

xABi ì 1y “ 0

ÐÑ

p\` \`

pjq “ 0 , 

\(2.23\)

j

2

xpABq1pABq2y “ 0

ÐÑ

p\`1 ´ \`2q “ 0 , 

\(2.24\)

wherèl is a particular choice of off-shell loop momenta that we will discuss in detail in the following. Equipped with this observation, we provide in the next section the definition of the loop momentum amplituhedron. 

3

The Loop Momentum Amplituhedron

We want to extend the definition of momentum amplituhedron from the previous section to include loops. As we argued before, since there is a one-to-one correspondence between singularities of loop-level integrands written in terms of momentum twistors and in the momentum space \(after we translate between kinematic variables\), we will adapt the construction of the loop amplituhedron from section 2.2 into spinor helicity variables. To start, let us recall that in the momentum twistor space each loop momentum is encoded as a line pABql that can be defined by specifying two momentum twistors zl,A and zl,B, up to a GLp2q transformation. To simplify our notation, we will drop the loop index l in the remaining part of this section, and discuss a single loop variable. In the amplituhedron construction, after we use the projections

\(2.19\) and \(2.20\), the line is parametrised in terms of the external momentum twistors as ÿ

za

γ “

dγizai , 

γ “ A, B . 

\(3.1\)

i

Moreover, momentum twistors can be written in terms of the spinor helicity variables λ and dual space coordinates xi as

˜

¸

˜

¸

λ

λ

z

i

i

i “

“

, 

i “ 1, . . . , n , 

\(3.2\)

˜

µi

xiλi

and similarly for the loop momentum twistors in terms of a single dual space coordinate x:

˜

¸

˜

¸

λ

λ

z

γ

γ

γ “

“

, 

γ “ A, B . 

\(3.3\)

˜

µγ

xλγ

– 7 –

Combining the expansion \(3.1\) with \(3.3\), we immediately get an expansion of λA and λB in terms of the external particles:

ÿ

λα

γ “

dγiλα

i , 

γ “ A, B . 

\(3.4\)

i

Since D “ pdγiq P Gp2, nq, then there is a natural GLp2q transformation between λA and λB. 

One of the most important insights from this simple calculation is that, if we want to translate the momentum twistors loop variables to spinor helicity space, we should look for a parametrisation of the loop momenta that renders manifest this GLp2q transformation. In the following, we will use the following parametrisation of off-shell momentum, written in terms of spinor helicity variables

\` “ λ ˜

˜

AλÀ λB λB , 

\(3.5\)

where, in order for \` to be GLp2q-invariant, ˜

λA, ˜

λB need to transform as

˜

¸

˜

¸

´

¯

´

¯

˜

λ1A

˜

λA

λ1 λ1

λ

, 

\(3.6\)

A

B

“

A λB

¨ G , 

˜

“ G´1 ¨

λ1B

˜

λB

for G P GLp2q. 

In the next step, we want to derive the expansion of ˜

λA and ˜

λB in terms of external

particles by considering the remaining part of the condition \(3.1\). First, let us introduce

˜

ÿ

λ

˜

γ “

γδλδ , 

γ “ A, B . 

\(3.7\)

δ“A,B

Taking the last two entries in the expansion \(3.1\), we have that ÿ

˜

µγ “

dγi ˜

µi

\(3.8\)

i

with ˜

µi “ xiλi and ˜

µγ “ xγλγ. A simple calculation results in

˜

i´1

¸

ÿ

ÿ

ÿ

ÿ

xλA “

dAixiλi “

dAi

x1 ´

pj

λi “ x1λA ´

dAixjiy˜

λj . 

\(3.9\)

i

i

j“1

jăi

As the last step, we need to identify the loop momentum \` with the dual coordinate x. 

There are various choices that we could make which would result in different loop momentum amplituhedron geometries. 

Importantly, the canonical forms on these geometries can be related to each other by the change of variables between these choices. Motivated by the explicit form of the relation \(3.9\), we settled for the following relation

\` “ x ´ x

˜

˜

˜

˜

1 “ λAλÀ λB λB “ λAλB ´ λB λA . 

\(3.10\)

– 8 –

This allows us to find the explicit expansion of ˜

λγ in terms of the external particles

˜

ÿ

xijy

λ

˜

γ “

dγi

λj . 

\(3.11\)

xABy

jăi

Using \(3.10\), we find the loop momentum written in terms of external spinor helicity variables, as well as of elements of the matrix D:

˜

¸ ˜

¸

˜

¸ ˜

¸

ÿ

ÿ

xijy

ÿ

ÿ

xijy

\` “

d

˜

˜

Aiλi

dBi

λj

´

dBiλi

dAi

λj

. 

\(3.12\)

xABy

xABy

i

jăi

i

jăi

Importantly, this formula provides a global definition of loop momentum. 

We are now ready to define the loop momentum amplituhedron. To this effect, we extend the map from section 2.1 to include also loop momenta. We define

˜

φ

: G

pΛK, ˜

Λq

\`pk, nq ˆ Gp2, nqL Ñ Gp2, nq ˆ Gp2, nq ˆ GLp2qL

C

Dl

ÞÑ

λ

˜

λ

\`l

where ΛK P M\`pk ´ 2, nq, ˜

Λ P M\`pk \` 2, nq and we will define the product ˆ shortly. The map ˜

φ

associates to every point C P G

pΛK, ˜

Λq

\`pk, nq and a collection of points Dl P Gp2, nq, 

the tree-level variables pλ, ˜

λq given by \(2.4\) and the loop momentàl given by \(3.10\). To complete our definition, we need to explain what we mean by the ˆ product present in the domain of ˜

φ

. We have already introduced in \(2.13\) the matrix Qpλq that relates the pΛK, ˜

Λq

Grassmannian points in the definition of the tree amplituhedron to the Grassmannian points in the definition of the tree momentum amplituhedron. In particular, we conjectured that for pλ, ˜

λq P Mn,k and C P G\`pk, nq, if we can define č “ Q ¨ c then č P G\`pk ´ 2, nq. The product îs defined by additional positivity conditions relating the matrix č with the loop-level matrices Dl. We define G\`pk, nq ˆ Gp2, nqL as the set of all points C P G\`pk, nq and Dl P Gp2, nq for l “ 1, . . . L such that all matrices

¨

˛

Dl1

˜

¸

˚

. ‹

´ ¯

D

. 

l

˚

. ‹

č , 

1

, 

. . . 

˚

‹ , 

\(3.13\)

č

˚D ‹

˝

lL ‚

č

are positive for all li “ 1, . . . , L. 

The loop momentum amplituhedron Mn,k,L is then defined as the image M

\`

L˘

n,k,L “ ˜

φ

G

. 

\(3.14\)

pΛK, ˜

Λq

\`pk, nq ˆ Gp2, nq

This is the main result of our paper. 

We conclude this section by having a preliminary look at the boundary structure of the

– 9 –

loop momentum amplituhedron. First, it is clear from our construction that Mn,k,L has boundaries when the tree-level invariants vanish, reflecting the facet structure of the tree momentum amplituhedron. In particular, it has boundaries that correspond to factorisations when the planar Mandelstam variables vanish si,ì1,...,ìp “ 0. It also has boundaries coming from collinear limits of two types4 when xiì 1y “ 0 or riì 1s “ 0. These are supplemented by the codimension-one boundaries of two types coming from loop level:

˜

¸

•

D

ř

r

p\`r \`

p

j

j q2 “ 0 corresponding to a sufficient number of minors of the matrix č

vanishing for some r “ 1, . . . , L; 

¨

˛

Dr1

• p\`

˚

‹

r

´ \` q2 “ 0 corresponding to a sufficient number of minors of the matrix D

1

r2

r

˝

2 ‚

č

vanishing for some r1 ‰ r2. 

Finding the complete stratification of boundaries of Mn,k,L remains an open and interesting problem that we plan to address in the future. 

4

Examples

In this section we present a few examples of the loop momentum amplituhedron and the related amplitudes. 

Let us start with the simplest case, the MHV amplitudes. Since in this case we have k1 “ k ´ 2 “ 0, then the matrix č in \(3.13\) is an empty matrix and there is no positivity condition mixing C and the loop matrices Dl. This means that each matrix Dl P G\`p2, nq is positive on its own, and there are additional mutual positivity conditions between Ds as in

\(3.13\). Therefore, the geometry in this case is simply the product of the tree-level geometry and the loop geometry. This immediately implies that the canonical form Ωn,2,L for the loop momentum amplituhedron Mn,2,L is the wedge product of the canonical form for the tree momentum amplituhedron Mn,2,0 times the 4L-form coming from the loop geometry: Ωn,2,L “ Ωn,2,0 ^ ˜

Ωn,2,L , 

\(4.1\)

where ˜

Ωn,2,L is a 4L-form coming purely from the loop geometry. Since we know from \[5\] the exact form of the tree-level canonical form, we just need to find the canonical form of the loop geometry. 

Because of the factorisation of the tree and loop geometries we described above, it is possible for a direct translation of the loop canonical forms from the loop amplituhedron

\[4\]. In particular, the one-loop amplituhedron An,0,1 is the union of images of the so-called 4It is possible that these boundaries are not facets of the loop momentum amplituhedron but instead they are lower dimensional, as for example in the 4-point case. 

– 10 –

kermits \[4, 10\] with associated matrices:

˜

¸

1 0 . . . ˚

K

i ˚ . . . 0 0 . . . 

i,j :

, 

\(4.2\)

1 0 . . . 0 0 . . . ˚j ˚ . . . 

through the map PZ ˝ ΦZ. Then, we conjecture that also the one-loop momentum amplituhedron Mn,2,1 is the union of the images of the kermits

ď

M

˜

n,2,1 “

φ

pC, K

pΛK, ˜

Λq

i,j q . 

\(4.3\)

iăj

The canonical form ωn,0,1 of An,0,1 is known and reads

ÿ

ωn,0,1 “

ωK

, 

\(4.4\)

i,j

1ăiăjăn

where

xAB1iy

xABiì 1y

xABjj \` 1y

xABj \` 11y

ωK

“ dlog

^ dlog

^ dlog

^ dlog

. 

\(4.5\)

i,j

xAB1ì 1y

xAB1ì 1y

xAB1jy

xAB1jy

We claim that the canonical form for the one-loop momentum amplituhedron is ÿ

Ωn,2,1 “ Ωn,2,0 ^

ΩK

, 

\(4.6\)

i,j

iăj

where

ři

řj

p\` ´ \`˚

p\` ´

paq2

p\` ´ \`˚

1 jq2

p\` ´

paq2

Ω

1 iq2

a“1

a“1

K

“ dlog

^ dlog

^ dlog

^ dlog

, 

i,j

p\` ´ \`˚

1 i

p\` ´ \`˚

p\` ´ \`˚

p\` ´ \`˚

\`1q2

1 ì1q2

1 j\`1q2

1 j\`1q2

\(4.7\)

and we have defined

˜

j´1

i

¸

1

´1

ÿ

ÿ

\`˚ij “

λi

xljy˜

λl ´ λj

xliy˜

λl

. 

\(4.8\)

xijy

l“1

l“1

Moving on beyond one loop, general triangulations of the loop amplituhedron can be obtained from the BCFW recursion relation \[10\] together with the on-shell diagram parametrisation proposed in \[11\]. We conjecture that for MHV amplitudes, the images of the same BCFW matrices will triangulate the loop momentum amplituhedron and loop amplituhedron. To support our claim, we provide the simplest example beyond one loop: two-loop four-point amplitude. In this case, there are 16 BCFW terms \[11\] and we have performed extensive numerical checks that given a set of positive data and a point inside the loop momentum amplituhedron, it lies in one and only one of the images of the 16 cells corresponding to these BCFW terms. Then we can translate the known canonical forms to spinor helicity

– 11 –

*p* 1

*p*

*x*

2

2

*ℓ* 1 \+ *p* 1

*p*

*ℓ* 1

*x*

*ℓ* 1 \+ *p* 1 \+ *p* 2

1

*x*

*p*

*AB*

2

2

*ℓ* 1 \+ *p* 1

*ℓ* 2 \+ *p* 1

*ℓ*

*x*

1 − *ℓ* 2

1

*x* 3

*ℓ*

*ℓ*

1 − *ℓ* 2

2 \+ *p* 1 \+ *p* 2

*x* 1

*x*

*x*

*AB*

*xCD*

*x* 3

*ℓ*

*CD*

*ℓ*

2

2 \+ *p* 1 \+ *p* 2

*ℓ* 1

*ℓ* 2 − *p* 4

*ℓ* 1 − *p* 4

*ℓ* 2 − *p* 4

*x*

*p*

*x* 4

*p*

*p* 4

4

*p* 3

4

3

Figure 1. The two diagrams corresponding to the two terms in \(4.9\). The remaining two terms have identical diagrams with xAB and xCD exchanged. 

space and sum them together. Ultimately, we get the well-known formula

" 

˜

s2t d4\`1d4\`2

Ω4,2,2 “

\`21p\`1 \` p1q2p\`1 ´ p4q2p\`1 ´ \`2q2p\`2 \` p1q2p\`2 \` p1 \` p2q2p\`2 ´ p4q2

st2 d4\`

\*

1d4\`2

\`

\` p\`1 Ø \`2q ,\(4.9\)

\`21p\`1 \` p1q2p\`1 \` p1 \` p2q2p\`1 ´ \`2q2\`22p\`2 \` p1 \` p2q2p\`2 ´ p4q2

where as defined before we havè1 “ xAB ´ x1 and \`2 “ xCD ´ x1. Each term in this expansion corresponds to the expression associated to a standard Feynman diagram, see fig. 

4. Since for MHV amplitudes the parametrization of the BCFW cells is known at any loop

\[11\], then it is in principle possible to extend our calculation beyond four points and beyond two loops to find canonical differential forms for the loop momentum amplituhedron Mn,2,L. 

We conclude this section by having a first look at examples beyond the MHV sector. 

In this case, the geometry is not the product of the tree-level and loop geometries anymore. 

Indeed, the matrix č is not empty, and therefore there are positivity conditions mixing the matrices č and Dl. For instance, for next-to-MHV \(NMHV\) amplitudes at one loop, we require that the 3 ˆ n matrix C is positive \(that implies that the 1 ˆ n matrix č is positive\), and the 3 ˆ n matrix obtained by stacking a single D matrix on top of the č is positive. Let us consider the 5-point case. One would naively think to be able to use the BCFW triangulations of the loop amplituhedron given in \[4, 12\], where one can find three BCFW terms with their parametrisations of pD, čq matrices. Then, one considers points in the domain of the loop momentum amplituhedron map C ˆ D corresponding to points in these BCFW cells, namely points for which č “ Qc. Since Q has rank n ´ 2 and is therefore not an invertible matrix, 

– 12 –

this is however not possible5. Therefore, it is a non-trivial task to find triangulations of the loop momentum amplituhedron using the known results about the loop amplituhedron, and the problem of triangulating Mn,k,L for k ą 2 remains the most urgent unresolved question. 

The fact that the triangulations of amplituhedron and momentum amplituhedron cannot be easily matched also means that the geometry of the loop momentum amplituhedron beyond MHV level is much richer in structure and deserves further study. 

5

Conclusions and Outlook

In this paper we presented the geometry for scattering amplitudes in N “ 4 sYM at tree and loop level in spinor helicity space, i.e. the loop momentum amplituhedron. Taking inspiration from the singularity structure of amplitudes and expectation values of Wilson loops, we used the known construction of the loop amplituhedron and adapted it to spinor helicity space. 

Importantly, while all facets of the loop part of the amplituhedron are mapped to facets of the momentum amplituhedron at loop level, the complete boundary stratification of the two geometries is different, due to the differences at tree level. 

There are many natural questions which arise from this work. The most pressing direction is to investigate how to triangulate the loop momentum amplituhedron geometry. Unlike for the MHV loop momentum amplituhedron, where the triangulation can be directly obtained from the triangulations of the loop amplituhedron, for higher helicity sectors it is not possible anymore due to the mixing of tree and loop geometries. As for the momentum twistor space, the most natural starting point would be the BCFW recursion relation solved in terms of on-shell diagrams, which should provide parametrisations for the tree-level matrix C and the loop-level matrices Dp. 

An equally pressing question is the boundary structure of the loop momentum amplituhedron. The full stratification at tree level was found in \[15\] and it possesses very natural physical properties, with all boundaries labelled by Grassmannian forests that physically correspond to all possible factorisations and soft and collinear limits of tree amplitudes. We expect that also at loop level one will be able to introduce a natural, physically motivated labelling for all boundaries of the loop momentum amplituhedron. As the starting point, one can expand the methods implemented in the Mathematica package amplituhedronBoundaries \[16\] that have been crucial at tree level. This would provide us with a classification of all singularities of amplitude integrands at any loop order. 

Another interesting question is the extension of our construction to the loop level of the orthogonal momentum amplituhedron, i.e. the positive geometry for tree-level amplitudes in ABJM theory \[17, 18\], that is defined in terms of the positive orthogonal Grassmannian

\[19\]. For four-point ABJM amplitudes a geometry encoding all-loop amplitude integrands has already been suggested in \[20\]. This has been done by projecting the N “ 4 sYM loop 5It differs at tree level where one can construct a map from positroid cells of G\`pk ´ 2, nq to positroid cells Gk,n, the so-called T-duality map \[13, 14\]. The T-duality map however acts on whole positroid cells and not on their points, as is required at loop level. 

– 13 –

amplituhedron to three dimensions. Then, a natural question is if this result, combined with our definition of the loop momentum amplituhedron, allows for generating the all-loop orthogonal momentum amplituhedron also for other multiplicities. 

Furthermore, it has been recently showed that the so-called “negative geometries” \[21\]

provide a geometric definition of an infrared finite quantity interpreted as the expectation value of the Wilson loop with a single Lagrangian insertion, at least for four points. Following the same logic, it would be interesting to study whether one can retrieve infrared finite information about integrated amplitudes also from the loop momentum amplituhedron. 

Finally, since the loop momentum amplituhedron is defined in spinor helicity space, it should allow for generalisations to the non-planar sector of N “ 4 sYM, which would result in a geometry for non-planar loop integrands. A strong suggestion that such geometry should exist come from the fact that also the non-planar loop amplitude integrands have logarithmic singularities and can be converted to logarithmic differential forms \[22\]. One of the main difficulties of moving to non-planar amplitudes had been the absence of a global definition of the loop momentum. However, since our construction provides such a global definition by defining the loop momentum as a parameter of the map ˜

φ

, a natural conjecture would

pΛK, ˜

Λq

be to find non-planar contributions by modifying the domain of the map ˜

φ. This conjecture

is reinforced by the fact that non-planar on-shell diagrams \[23–25\], which represent cuts of non-planar loop amplitudes, are connected to parts of Grassmannian spaces different from the positive one. Therefore, they can provide a useful hint on finding a non-planar momentum amplituhedron. 

6

Acknowledgements

We would like to thank A. Lipstein and J. Trnka for useful discussions. This work was partially funded by the Deutsche Forschungsgemeinschaft \(DFG, German Research Foundation\) – Projektnummern 404358295 and 404362017. This research was partially supported by the Munich Institute for Astro-, Particle and BioPhysics \(MIAPbP\) which is funded by the Deutsche Forschungsgemeinschaft \(DFG, German Research Foundation\) under Germany’s Excellence Strategy – EXC-2094 – 390783311. 

A

Kinematic Variables

In this appendix we collect the variables used in N “ 4 sYM which are mentioned in the paper. 

Spinor helicity variables. 

In a massless theory in four dimensions with p2i “ 0 for all particles, one can write each momentum as

pa 9a

i

“ λair

λ 9ai , 

\(A.1\)

in terms of two spinor variables λ and r

λ. In N “ 4 SYM, we can consider

– 14 –

• the chiral superspace pλα, ˜λ 9α|ηAq: ηA are Grassmann-odd variables transforming in the fundamental representation of the SU p4q R-symmetry, 

• the non-chiral superspace pλα, ηa|˜λ 9α, ˜η9aq: ηa, η 9a are two sets of Grassmann-odd variables r

both transforming in the fundamental representations of SU p2q. One can think of η 9a r

as Fourier conjugate variables to η3,4. 

Dual superspace. 

Starting from the on-shell chiral superspace, one can define a dual superspace with coordinates px, θq with

xa 9a

i

´ xa 9a

i´1 “ λa

i´1r

λ 9ai´1 , 

θaA

i

´ θaA

i´1 “ λa

i´1ηA

i´1

i “ 1, . . . , n . 

\(A.2\)

This is the space where the n-sided null polygon Wilson loop dual to the n-point amplitude is formulated. 

Momentum twistor variables. 

The \(super\) momentum twistors are defined from the dual

superspace

Zi “ pzai|χA

i q “ pλia, ˜

µ 9ai|χA

i q ” pλia, xa 9aλia|θaA

i

λiaq . 

\(A.3\)

The momentum twistors are unconstrained and they determine r λ, η via, 

xi ´ 1 iyp˜

µ|χqì1 \` xì 1 i ´ 1yp˜

µ|χqì xi ì 1yp˜

µ|χqi´1

pr

λ|ηqi “

, 

\(A.4\)

xi ´ 1 iyxi ì 1y

and we also have

xi ´ 1 i k ´ 1 ky

x2

2

ij :“ pxi ´ xj q

“

, 

\(A.5\)

xi ´ 1 iyxk ´ 1 ky

where xijkly “ IJKLzI zJ zKzL. Finally, in momentum twistor variables, the loop integral is i

j

k

l

an integral over the space of lines pABq. This can be rewritten as an integral over a pair of points A and B, modulo the GLp2q redundancies labeling their positions on the line: d4zAd4zB

d4\` “

. 

\(A.6\)

volpGLp2qq

References

\[1\] N. Arkani-Hamed, Y. Bai and T. Lam, “Positive Geometries and Canonical Forms”, 

JHEP 1711, 039 \(2017\), arxiv:1703.04541. 

\[2\] L. Ferro and T. Lukowski, “Amplituhedra, and beyond”, J. Phys. A 54, 033001 \(2021\), 

arxiv:2007.04342. 

\[3\] E. Herrmann and J. Trnka, “The SAGEX Review on Scattering Amplitudes, Chapter 7: Positive Geometry of Scattering Amplitudes”, arxiv:2203.13018. 

\[4\] N. Arkani-Hamed and J. Trnka, “The Amplituhedron”, JHEP 1410, 030 \(2014\), 

arxiv:1312.2007. 

– 15 –

\[5\] D. Damgaard, L. Ferro, T. Lukowski and M. Parisi, “The Momentum Amplituhedron”, 

JHEP 1908, 042 \(2019\), arxiv:1905.04216. 

\[6\] N. Arkani-Hamed, F. Cachazo and C. Cheung, “The Grassmannian Origin Of Dual Superconformal Invariance”, JHEP 1003, 036 \(2010\), arxiv:0909.0483. 

\[7\] N. Arkani-Hamed, F. Cachazo, C. Cheung and J. Kaplan, “A Duality For The S Matrix”, 

JHEP 1003, 020 \(2010\), arxiv:0907.5418. 

\[8\] N. Arkani-Hamed, H. Thomas and J. Trnka, “Unwinding the Amplituhedron in Binary”, 

JHEP 1801, 016 \(2018\), arxiv:1704.05069. 

\[9\] G. Dian, P. Heslop and A. Stewart, “Internal boundaries of the loop amplituhedron”, 

arxiv:2207.12464. 

\[10\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, S. Caron-Huot and J. Trnka, “The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM”, JHEP 1101, 041 \(2011\), 

arxiv:1008.2958. 

\[11\] Y. Bai and S. He, “The Amplituhedron from Momentum Twistor Diagrams”, 

JHEP 1502, 065 \(2015\), arxiv:1408.2459. 

\[12\] Y. Bai, S. He and T. Lam, “The Amplituhedron and the One-loop Grassmannian Measure”, 

JHEP 1601, 112 \(2016\), arxiv:1510.03553. 

\[13\] T. Lukowski, M. Parisi and L. K. Williams, “The positive tropical Grassmannian, the hypersimplex, and the m=2 amplituhedron”, arxiv:2002.06164. 

\[14\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. B. Goncharov, A. Postnikov and J. Trnka, 

“Grassmannian Geometry of Scattering Amplitudes”, Cambridge University Press \(2016\). 

\[15\] L. Ferro, T. Lukowski and R. Moerman, “From momentum amplituhedron boundaries to amplitude singularities and back”, JHEP 2007, 201 \(2020\), arxiv:2003.13704. 

\[16\] T. Lukowski and R. Moerman, “Boundaries of the amplituhedron with amplituhedronBoundaries”, Comput. Phys. Commun. 259, 107653 \(2021\), arxiv:2002.07146. 

\[17\] Y.-t. Huang, R. Kojima, C. Wen and S.-Q. Zhang, “The orthogonal momentum amplituhedron and ABJM amplitudes”, JHEP 2201, 141 \(2022\), arxiv:2111.03037. 

\[18\] S. He, C.-K. Kuo and Y.-Q. Zhang, “The momentum amplituhedron of SYM and ABJM from twistor-string maps”, JHEP 2202, 148 \(2022\), arxiv:2111.02576. 

\[19\] Y.-T. Huang and C. Wen, “ABJM amplitudes and the positive orthogonal grassmannian”, 

JHEP 1402, 104 \(2014\), arxiv:1309.3252. 

\[20\] S. He, C.-K. Kuo, Z. Li and Y.-Q. Zhang, “All-loop ABJM amplitudes from projected, bipartite amplituhedron”, arxiv:2204.08297. 

\[21\] N. Arkani-Hamed, J. Henn and J. Trnka, “Nonperturbative negative geometries: amplitudes at strong coupling and the amplituhedron”, JHEP 2203, 108 \(2022\), arxiv:2112.06956. 

\[22\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo and J. Trnka, “Singularity Structure of Maximally Supersymmetric Scattering Amplitudes”, Phys. Rev. Lett. 113, 261603 \(2014\), arxiv:1410.0354. 

\[23\] N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. Postnikov and J. Trnka, “On-Shell Structures of MHV Amplitudes Beyond the Planar Limit”, JHEP 1506, 179 \(2015\), arxiv:1412.8475. 

– 16 –

\[24\] J. L. Bourjaily, S. Franco, D. Galloni and C. Wen, “Stratifying On-Shell Cluster Varieties: the Geometry of Non-Planar On-Shell Diagrams”, JHEP 1610, 003 \(2016\), arxiv:1607.01781. 

\[25\] S. Paranjape, J. Trnka and M. Zheng, “Non-planar BCFW Grassmannian Geometries”, 

arxiv:2208.02262. 

– 17 –


# Document Outline

+ 1 Introduction 
+ 2 Amplituhedra  
	+ 2.1 The Momentum Amplituhedron Revisited 
	+ 2.2 The Amplituhedron 
	+ 2.3 Boundaries of Amplituhedra 

+ 3 The Loop Momentum Amplituhedron 
+ 4 Examples 
+ 5 Conclusions and Outlook 
+ 6 Acknowledgements 
+ A Kinematic Variables



