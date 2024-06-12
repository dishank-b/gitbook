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

An $$n\times n$$ symmetric real matrix $$M$$ is said to be positive semi-definite  if $$x^TMX \geq 0$$ for all non-zero $$\mathbf {x}$$in $$\mathbb {R} ^{n}$$. &#x20;

**What does positive definite mean?**  It's similar to saying for example in one dimensional that $$kx^2$$should be positive $$\forall x$$which means $$k>0$$. Similarly, for higher dimensions, to get the higher dimensional parabola always positive we need a positive definite matrix.&#x20;

### PSD from the lens of dot-product

Let's see

We can consider $$x^TAx$$ as dot product $$(x^T)Ax$$. Now PSD means $$(x^T)(Ax) \geq 0$$ which means $$x^T$$ and $$Ax$$ form an acute angle between them i.e point in the same directoin. Hence, it means that $$A$$ is a transformation that keeps $$Ax$$ in the same direction as $$x$$.&#x20;

### Properties of PD or PSD matrices

**All the eigenvalues of a positive definite matrix are positive.  A matrix is positive definite if it’s symmetric and all its eigenvalues are positive.**

As established all the transformed vectors Ax are in same direction as x for positive dot product. Let's consider some eigen vector $$v_i$$with it's eigen value $$\lambda_i$$. Now we know that $$Av_i = \lambda_iv_i$$ , so for $$(v_i^T)(Av_i) \geq 0 \implies v_i^T\lambda_uv_i \geq 0 \implies \lambda_i ||v_i|| \geq 0 \implies \lambda_i \geq 0$$



**The determinant of a positive definite matrix is always positive, so a positive definite matrix is always** [**nonsingular**](https://mathworld.wolfram.com/NonsingularMatrix.html)**.**

$$
\text{det}(A) = \prod_{n=1}^N \lambda_n
$$

So if all the $$\lambda_n$$are positive, determinant will also be positive.&#x20;



**Decomposition**

If $$A$$ is **Positive semi-definite if and only if it can be decomposed as follows:**

$$
A = B^TB
$$

Also

$$
A = LL^T
$$

Where $$L$$ is a lower triangular matrix. And this is called Cholesky decomposition.&#x20;

## PSD Matrices defining Ellipsoid

Let's say we have $$Q(x) = x^TAx$$, be a positive definite form. Then the set

$$
\{x \in \mathbf R^n: Q(x)=c\}
$$

where $$c$$ is some constant. This set of points forms an ellipsoid.&#x20;

### Resrouces

{% embed url="https://gregorygundersen.com/blog/2022/02/27/positive-definite/" %}
Very comprehensive study of PSD Matrices. Relating it to dot product, quadratic programming, and visualization.&#x20;
{% endembed %}

{% embed url="https://towardsdatascience.com/what-is-a-positive-definite-matrix-181e24085abd" %}

{% embed url="https://medium.com/sho-jp/linear-algebra-101-part-8-positive-definite-matrix-4b0b5acb7e9a" %}

#### Why does PSD matrices have to be symmetric?

{% embed url="https://math.stackexchange.com/questions/1964039/why-do-positive-definite-matrices-have-to-be-symmetric" %}

### Full Rank Matrix

In [linear algebra](https://en.wikipedia.org/wiki/Linear\_algebra), the **rank** of a [matrix](https://en.wikipedia.org/wiki/Matrix\_\(mathematics\)) A is the [dimension](https://en.wikipedia.org/wiki/Dimension\_\(vector\_space\)) of the [vector space](https://en.wikipedia.org/wiki/Vector\_space) generated (or [spanned](https://en.wikipedia.org/wiki/Linear\_span)) by its columns.This corresponds to the maximal number of [linearly independent](https://en.wikipedia.org/wiki/Linearly\_independent) columns of A. This, in turn, is identical to the dimension of the vector space spanned by its rows. Rank is thus a measure of the "[nondegenerateness](https://en.wikipedia.org/wiki/Degenerate\_form)" of the [system of linear equations](https://en.wikipedia.org/wiki/System\_of\_linear\_equations) and [linear transformation](https://en.wikipedia.org/wiki/Linear\_transformation) encoded by A.

A matrix is said to have **full rank** if its rank equals the largest possible for a matrix of the same dimensions, which is the lesser of the number of rows and columns.&#x20;



## Resources

* Talks about multiple properties of PSD and also gives insight about Hessians of functions as they are PSD
