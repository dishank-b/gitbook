# Eigen Value Decomposition

Solution of the below equation gives the eigenvalues and eigenvectors.

$$
Ax = \lambda x
$$



**Eigenvectors are basically the vectors which only scale under the transformation** $$A$$**where the scale is given by** $$\lambda$$**.**&#x20;

Let $$A$$be matrix of dimension $$n \times n$$. And let it have all the real eigenvalues and eigenvectors i.e $$n$$eigenvalues and eigenvectors. Then we will following equations.&#x20;

$$
Ax_i = \lambda_i x_i  \forall i
$$

Basically we get $$n$$ equations with $$x_i$$being eigenvectors, now we should we able to represent all the $$n$$individual equations using one matrix equation. You can see that all the equations can be combined as&#x20;

$$
A[x_1, x_2, ..., x_n] = [\lambda_1 x_1, \lambda_2 x_2, .... \lambda_n x_n] \\
 = [x_1, x_2, ..., x_n] \text{diag}(\lambda_1, \lambda_2, ...,  \lambda_n)
$$

where $$[x_1, x_2, ..., x_n]$$is essentially a matrix with vector $$x_1, x_2, ..., x_n$$as its columns.&#x20;

Let's represent $$[x_1, x_2, ..., x_n]$$as $$V$$i.e $$V = [x_1, x_2, ..., x_n]$$. Then we can write&#x20;

$$
AV = V\text{diag}(\lambda_1, \lambda_2, \lambda_n) \\
A = V\text{diag}(\lambda_1, \lambda_2, ...,  \lambda_n)V^{-1}
$$

Where $$V$$is the matrix made by eigenvectors as columns of $$V$$and $${diag}(\lambda_1,  \lambda_2, ..., \lambda_n)$$is the diagonal matrix with eigenvalues as diagonal elements.&#x20;

**This is eigenvalue decomposition.**&#x20;

### **Real-Symmetric Matrix**

Now if the matrix $$A$$is real-symmetric matrix, the eigenvectors are actually orthogonal. Then we represent the decomposition as&#x20;

$$
A = Q\Lambda Q^T
$$

Where $$Q$$is an orthogonal matrix formed by orthogonal eigenvectors.&#x20;

### Use of Eigenvalues

* Matrix is singular if and only if any of it's eigenvalues are zero.&#x20;
* If $$A$$is real-symmetrix then solution of $$f(x)= x^T Ax$$ subject to $$||x||_2 = 1$$. Here is $$x$$is an eigenvector then $$f(x)$$is corresponding eigenvalue. The minimum and maximum value of $$f(x)$$is simply minimum and maximum eigenvalue.&#x20;
* If all eigenvalues are positive then the matrix is positive-definite. Similary about positive-semidefinite, etc.&#x20;
* $$A^2 = AA=X\Lambda X^{-1}X\Lambda X^{-1} = X\Lambda^2 X^{-1}$$

{% embed url="https://youtu.be/HWnCv4iHCDc" %}

{% embed url="https://youtu.be/PFDu9oVAE-g" %}
