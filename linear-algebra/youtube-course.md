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

&#x20;
