# Matrix Decomposition

## Eigen Decomposition

An eigenvector of a **square matrix** $$\matrix A$$is a vector $$\boldsymbol v$$, such that multiplying it by  $$\matrix A$$only change its scale.

$$
A\boldsymbol v = \lambda\boldsymbol v
$$

The scalar $$\lambda$$which is scaling factor is called eigenvalue. 

$$
\matrix A = V\text{diag}(\lambda)V^T
$$

There is something called left eigenvector which can be found as: $$\boldsymbol v^T A = \lambda\boldsymbol v^T$$.

The eigendecomposition of a real symmetric matrix can also be used to optimize quadratic expressions of the form  $$f(\boldsymbol x) = \boldsymbol x^T \matrix A\boldsymbol x$$subject to $$|| x ||_2 = 1$$. Whenever x is equal to an eigenvector of A, f takes on the value of the corresponding eigenvalue. The maximum value of f within the constraint region is the maximum eigenvalue and its minimum value within the constraint region is the minimum eigenvalue.

**NOTE: Eigen Value Decomposition is only defined for square matrix.**

Some properties of eigendecomposition.

* A matrix is singular if and only if any of the eigenvalues are zero.
* A matrix whose eigenvalues are all positive is called **positive definite.**
* A matrix whose eigenvalues are all positive or zero is called **positive semdefinite.**

## Singular Value Decomposition

SVD is more general in nature than eigenvalue decomposition. It's more informative than eigendecomposition.

$$
\matrix A = UDV^T
$$

if $$A$$is $$m\times n$$, then $$U$$is $$m\times m$$, $$D$$is diagonal matrix of $$m\times n$$, $$V$$is matrix of $$n\times n$$.

Both $$U$$and $$V$$are orthogonal matrices. Note that $$D$$is not necessarily square. The diagonal values are **singular values of matrix** $$A$$. The columns of U are known as the left-singular vectors. The columns of V are known as as the right-singular vectors.



