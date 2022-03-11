# QR Decomposition

For any real square matrix $$A$$we have

$$
A = QR
$$

Where $$Q$$is an orthogonal matrix and $$R$$is an upper trianguler matrix.&#x20;

* Used to solve linear least square problems.&#x20;

### Orthogonal Matrices

Remember that the orthogonal matrix preserves lengths and angles in linear space. This means that multiplying a vector by an orthogonal matrix will preserve lengths and angles between vectors.&#x20;

### Upper Triangular Matrices

What does the upper triangular matrix mean? So let's say if we have an upper triangular matrix $$R$$.

$$
XR = Y
$$

$$Y$$ columns are linear combinations of columns of $$X$$in proportion decided by values in matrix $$R$$. Since $$R$$ is an upper triangular matrix, it means that any column of $$Y$$is linear combination of only columns on or before that column in $$X$$i.e column $$i$$ of $$Y$$is combinations of columns $$1:i$$ of $$X$$.&#x20;

### Derivation of QR factorization

![](../../.gitbook/assets/PXL\_20220310\_215544665.jpg) ![](../../.gitbook/assets/PXL\_20220310\_215554120.jpg)

The process described in the pictures above is called **Gram-Schimdt Orthogonalizatoin procedure.**&#x20;

So basically **QR** decomposition captures the gram-schimdt orthogonailzation. it decomposed the matrix $$A$$as to how to get multiply an orthogonal matrix $$Q$$by an upper triangular matrix $$R$$.&#x20;

### Solving Linear Square Solution&#x20;

{% embed url="https://youtu.be/7KP6TO5JXYY" %}

{% embed url="https://youtu.be/hBOruhKIItE" %}
