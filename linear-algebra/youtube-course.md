# Youtube Course

## Linear Subspace

* Element zero has to be part of the subspace
* Linear combination (multiplication by scalar, addition of two elements) of any two elements belonging to the subspace also needs to belong to the subspace.

## Spanning

To span a complete $$n$$dim space, we need atleast $$n$$ independent vectors of $$n$$ dimension. For example, to span complete $$\mathbb{R}^n$$, you need atleast $$n$$independent $$x$$st $$x \in \mathbb{R}^n$$.&#x20;

## Determining number of linear dependences&#x20;

Let's say you have K vectors each of $$x_i$$ $$\in \mathbb{R}^n$$, such that K > n. But you use maximum have n vectors to span the whole $$\mathbb{R}^n$$such that there are no linearly dependent vectors. Hence when you have K vectors, some of them have to be linearly dependent on others. Hence there will be exactly, K-n linear dependences among the K vectors.&#x20;

## Linear Combination are vectors!

Say you have three vectors, $$\vec{a},\vec{b},\vec{c}$$ st $$\vec{a}+\vec{b} +\vec{c}=\vec{0}$$, in this there is a linear combiantion. But that linear combination is actually a vector, $$\vec{0}$$vector. So you can treat each linear dependence equation as actually a vector.&#x20;

## Null space

The span formed by the vectors which are the coefficients of vectors whose linear combination is zero.

{% embed url="https://youtu.be/LlyiyoMcLJY?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv" %}

i.e null space of given k vectors is basically the span of vectors made up by coefficients of linear dependence equations in those k vectors. One linear dependence given eq'n give one vector, hence if there are m dependent eq'n among those k vectors, the Null space will be span of those m vectors.&#x20;

**Essentially null space of a given k vectors is space of vectors which will always give zero when those k vectors are linearly expressed with coefficients of the vector. i.e let** $$A$$ **be a matrix formed by stack** $$k$$**vectors as column of the Matrix** $$A$$**. Then null space is the space such that any vector** $$x$$ **belonging to null space gives:** $$Ax=0$$**. ie Null space is space of all vectors** $$x$$ **such that** $$Ax=0$$ **where** $$A$$**is matrix formed by k vectors.  Note that if the K vectors are linearly independent, then there won't be any non-trivial** $$x$$ **possible in that case, hence Null space will be just zero vector.**&#x20;

**You can also see Null space as defining the relatoinship among the columns of the matrix. Null space defines are complete relations among the columns. i.e defines the linear dependence of columns.**&#x20;

\


## Spanning Set

Set of vectors that can express any other vector from the same vector space as a linear combination.  There would be some minimum number of vectors needed in the spanning set in order to express the all vectors possible in their vector space. For ex: if you have one 2D vector, you can only express other vectors that lie in the same line as the one vector in the space. But if you would have 2 2D vectors which are not colinear then you can span all the vectors in the plane using their linear combination. That spanning set with a minimum number of vectors (those vectors would have to be linearly independent) would be called the basis.&#x20;

## &#x20;Dimension of vector space

The minimum of vectors needed in the spanning set in order to express all the vectors in that vector space (of course the vectors will have to be linearly independent) is called the dimension of that vector space.&#x20;

## Basis

A spanning set with the minimum number of vectors to express all other vectors in the space is called Basis. A Basis can express all vectors as linear combinations and do so uniquely. The number of vectors in the basis is the dimension of that vector space.&#x20;

## Way to Look at Linear system of Eq'ns

{% embed url="https://youtu.be/3YcMNeNNImY?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv" %}

## Null space vs Column Space

{% embed url="https://youtu.be/39h6IviFU9c?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv" %}

**Null Space:** Analysiszing null space of given vectors, helps us to know the dependence between the vectors, i.e if vectors are linear dependent or independent.&#x20;

**Columns Space:** Column space is the span of the given vectors, it helps us analyse the span of vectors.&#x20;

Null space helps as tell if there are infnitely many solutions of the eq'n of unique, and Column space can help tell if are unique solutions or none at all.&#x20;

{% embed url="https://youtu.be/gik1altzSU0?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv" %}

can easily see that: $$\text{dim}(R)+\text{dim}(N) =$$num of columns. Where R is columns space and N is null space.&#x20;

## Solving Systems of Eqn's: Related to gaussian elimination

The point of gaussian elimination is to find the relations among the given vectors easier to parse or more evident. It helps to know the span of vectors, or see if the vectors are linearly independed/dependent. Or to check if some vector is indeed in the span of given vectors, etc.&#x20;

## Matrix Multiplication

### Column Perspective (What we kind of been looking at until now)

Let's consider matrix multiplication of the form  $$Ax$$. Where $$A$$is some dimension matrix and $$x$$is vector, now you can the multiplication basically gives as a vector which is in column space of $$A$$, specifically linear combination of columns of $$A$$ where the coeffcients of combination is given by $$x.$$ $$Ax$$ can be seens as $$x$$ doing something to the $$A$$matrix to get some output vector, $$x$$deciedes the proportion of columns of A in which they are combined to get the new vector.&#x20;

Now let's talk about the matrix of the form $$AX$$, where both $$A, X$$ are matrices, now you can see the matrix multiplication as many $$Ax_i$$ where each $$x_i$$ is column of matrix $$X$$. Hence all the columns of resultant matrix are essentially some combination of columns of matrix $$A$$, where the proportion/coefficient of combination is decided by the columns of matrix $$X$$.

### Row perspective

Resultant matrix can be seen as linear combination of rows of right hand side matrix where coefficients are given by row by left hand side matrix. &#x20;

## Matrix Inverse

* only two matric whose multiplication is commutative are $$A$$ and $$A^{-1}$$. & vice versa i.e if multiplication of matrices is commutative, then they have to be each other inverse.
* A matrix is only invertible if it's columns are linearly independent i.e rows are linearly independent. \
  [https://youtu.be/fNpPrRNq8DU?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv](https://youtu.be/fNpPrRNq8DU?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv)

You can find matrix inverse by using gaussian elimination. &#x20;

## Transpose and Symmetric Matrices

Columns becomes rows when tranposed. When transposing, it might become useful to use the row perspectinve.&#x20;

* &#x20;Can be used to describe the symmetric metrices i.e $$A = A^T$$.
* $$AA^T$$is always a symmetric matrix. Can be easily seen that $$A^T$$, just have interchnages rows and columns and hence the multipliationn for the resultant becomes symmetric.&#x20;

## x^TAy

Properties of $$x^TAy$$.

{% embed url="https://youtu.be/YBABbb9TPEE?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv" %}

## A=LU Decomposition

{% embed url="https://youtu.be/HS7RadfcoFk?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv" %}

You see as solving $$A=LU$$, as trying to find $$L^{-1}$$such that applying it on left hand side of $$A$$ i.e doing row operations to $$A$$ will get your matrix $$U$$. &#x20;

SImilar you can see it as, as trying to find $$U^{-1}$$such that applying it on right hand side of $$A$$ i.e doing columns operations to $$A$$ will get your matrix $$L$$.

## Determinant

The determinant is essentially a way to find out if the columns of the matrix, ie the spanning vectors of the column space are linearly dependent or not. If the determinant of the matrix is zero, it essentially means that the columns are linearly dependent.&#x20;

It is also a way of telling if the systems of eqns will have infinitely many solutions or be unique, if they have infinitely many solutions that means that determinant is zero.&#x20;

* Matrix with determinant zero is called singular matrix.
* Determinant of upper or lower triangular matrix is given by multiplication of diagonal entries of the matrix.&#x20;
* [https://youtu.be/OIEEt8SuQYk?list=PLlXfTHzgMRULWJYthculb2QWEiZOkwTSU](https://youtu.be/OIEEt8SuQYk?list=PLlXfTHzgMRULWJYthculb2QWEiZOkwTSU)

There is a geometrical analogous of determinant as well. The determinant in 2D gives area of paralellogram given by the columns of matrix and in 3D gives volume. &#x20;

&#x20;&#x20;

