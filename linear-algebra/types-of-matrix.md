# Positive (Semi)Definite Matrices

## Symmetric Matrix

When the matrix entries are the same across the diagonal.&#x20;

![](<../.gitbook/assets/image (165) (1) (1).png>)

$$
A = A^T
$$

## Positive Definite or Positive Semi-definite

It's defined for symmetric matrix $$M$$.

An $$n\times n$$ symmetric real matrix $$M$$ is said to be positive-definite  if $$x^TMx > 0$$for all non-zero $$\mathbf {x}$$in $$\mathbb {R} ^{n}$$.  Formally

**Positive Semi-Definite**

An $$n\times n$$ symmetric real matrix $$M$$ is said to be positive-definite  if $$x^TMX \geq 0$$ for all non-zero $$\mathbf {x}$$in $$\mathbb {R} ^{n}$$. &#x20;

What does positive definite mean?&#x20;

It's similar to saying for example in one dimensional that $$kx^2$$should be positive $$\forall x$$which means $$k>0$$. In a similar manner, for higher dimensions, to get the higher dimensional parabola always positive we need a positive definite matrix.&#x20;

* **All the eigenvalues of a positive definite matrix are positive.**&#x20;
* **A matrix is positive definite if it’s symmetric and all its eigenvalues are positive.**

The determinant of a positive definite matrix is always positive, so a positive definite matrix is always [nonsingular](https://mathworld.wolfram.com/NonsingularMatrix.html).

{% embed url="https://towardsdatascience.com/what-is-a-positive-definite-matrix-181e24085abd" %}

{% embed url="https://medium.com/sho-jp/linear-algebra-101-part-8-positive-definite-matrix-4b0b5acb7e9a" %}

{% embed url="https://gregorygundersen.com/blog/2022/02/27/positive-definite/" %}
Very comprehensive study of PSD Matrices. Relating it to dot product, quadratic programming, and visualization.&#x20;
{% endembed %}

#### Why does PSD matrices have to be symmetric?

{% embed url="https://math.stackexchange.com/questions/1964039/why-do-positive-definite-matrices-have-to-be-symmetric" %}

#### PSD from the lens of dot-product

Let's see

We can consider $$x^TAx$$ as dot product $$(x^T)Ax$$. Now PSD means $$(x^T)(Ax) \geq 0$$ which means $$x^T$$ and $$Ax$$ are parallel. Hence, it means that $$A$$ is a transformation that keeps $$Ax$$ parallel to $$x$$.&#x20;

#### Full Rank Matrix

In [linear algebra](https://en.wikipedia.org/wiki/Linear\_algebra), the **rank** of a [matrix](https://en.wikipedia.org/wiki/Matrix\_\(mathematics\)) A is the [dimension](https://en.wikipedia.org/wiki/Dimension\_\(vector\_space\)) of the [vector space](https://en.wikipedia.org/wiki/Vector\_space) generated (or [spanned](https://en.wikipedia.org/wiki/Linear\_span)) by its columns.This corresponds to the maximal number of [linearly independent](https://en.wikipedia.org/wiki/Linearly\_independent) columns of A. This, in turn, is identical to the dimension of the vector space spanned by its rows. Rank is thus a measure of the "[nondegenerateness](https://en.wikipedia.org/wiki/Degenerate\_form)" of the [system of linear equations](https://en.wikipedia.org/wiki/System\_of\_linear\_equations) and [linear transformation](https://en.wikipedia.org/wiki/Linear\_transformation) encoded by A.

A matrix is said to have **full rank** if its rank equals the largest possible for a matrix of the same dimensions, which is the lesser of the number of rows and columns.&#x20;
