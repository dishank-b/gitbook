---
description: Chapter about Linear Algebra
---

# Linear Algebra

Linear algebra is a very beautiful part of mathematics. Where we discuss about vector spaces and their properties. Where we discuss about different characteristics of linear systems and how to solve them. 

One important think about Linear algebra is to able to draw parallel between geometry and arithmetic/algebra. Ability to understand both component on their own and yet able to draw parallel between the two is true understanding for the topic. 

## Linearity

See the following equation:

$$
\hat y = w^Tx+b
$$

See, in the above equation, the mapping from parameters $$w$$to predictions $$y$$ is linear function, but the mapping from features $$x$$to predictions $$y$$is affine function. In other words, $$\hat y$$is linear function/transformation of $$w$$ whereas affine function/transformation with $$x$$.

## Linear Combination

## The Moore-Penrose Pseudoinverse

Let's say we want to solve, $$Ax=y$$, then solution of this is given as say $$x=\boldsymbol{\matrix B}y$$. 

If $$A$$is invertible then we simply have $$B=A^{-1}$$. But what if $$A$$is not invertible, ie. the system of equation have no roots or have more than one roots.

Depending on the structure of the problem, it may not be possible to design a unique mapping from A to B . If A is taller than it is wide, then it is possible for this equation to have no solution. If A is wider than it is tall, then there could be multiple possible solutions.

The Moore-Penrose pseudoinverse allows us to make some headway in these cases. The pseudoinverse of A is defined as a matrix 

$$
A + = \lim_{\alpha\rightarrow0} (A^T A + α I )^{−1} A^T
$$

  Practical algorithms for computing the pseudoinverse are not based on this definition, but rather the formula 

$$
A^+ = V D^+ U^T
$$

where U, D and V are the singular value decomposition of A, and the pseudoinverse $$D^ +$$ of a diagonal matrix D is obtained by taking the reciprocal of its non-zero elements then taking the transpose of the resulting matrix. 

When A has more columns than rows, then solving a linear equation using the pseudoinverse provides one of the many possible solutions. Specifically, it provides the solution $$x = A^ + y$$ with minimal Euclidean norm $$|| x ||_2$$ among all possible solutions. 

When A has more rows than columns, it is possible for there to be no solution. In this case, using the pseudoinverse gives us the $$x$$ for which$$ Ax$$ is as close as possible to y in terms of Euclidean norm $$|| Ax − y ||_2$$ .

