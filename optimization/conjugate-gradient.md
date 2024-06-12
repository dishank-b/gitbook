# Conjugate Gradient

The conjugate gradient method is often implemented as an [iterative algorithm](https://en.wikipedia.org/wiki/Iterative\_method), applicable to [sparse](https://en.wikipedia.org/wiki/Sparse\_matrix) systems that are too large to be handled by a direct implementation or other direct methods such as the [Cholesky decomposition](https://en.wikipedia.org/wiki/Cholesky\_decomposition).

**NOTE: This method only works, when matrix A is positive definite.**&#x20;

Used to solve the linear system of equations denoted by&#x20;

$$
Ax = b
$$

Where $$A$$ is PSD matrix i.e $$x^TAx \geq 0$$ and $$n \times n.$$&#x20;

Two non-zero **vectors** $$u, v$$ **are conjugate wrt matrix** $$A$$, if&#x20;

$$
u^TAv=0
$$

**Geometrically, what this means is that the matrix** $$A$$ **transforms** $$v$$**, such that the transfomed vector** $$v$$**is orthogonal to vector** $$u$$**.**&#x20;

### Direct Method

The direct method depends upon the condition of conjugancy, find the a basis $$P = {p_1, p_2, \dots p_n}$$ in $$\mathbb{R}^n$$. such that each of paris of $$p_i, p_j$$ are conjugate, ie $$p_i^TAp_j=0$$.&#x20;

Now we write the $$x$$ as combination of spanning vectors, ie $$x = \sum_i \alpha_i p_i$$. Now we have&#x20;

$$
Ax = b \\
\sum_i \alpha_i Ap_i =b
$$

Now the trick is to multiply that equation by $$p_k$$, then left hand side will be zero for all $$k \neq i$$.&#x20;

$$
\sum_i \alpha_i p_k^TAp_i =p_k^Tb
$$

$$\forall k$$ $$k\neq i$$, the terms will be zero. leaving only term with $$i=k$$, then we will get&#x20;

$$
\alpha_k = \frac{p_k^Tb}{p_k^TAp_k}
$$

repeat this for $$k=i \quad \forall i$$, to get all $$\alpha_i$$.&#x20;

Hence the algorithm consists to steps:

* Having the basis comprising of conjugate vectors wrt matrix $$A$$.&#x20;
* Finding  $$\alpha_i \quad \forall i$$.



{% hint style="info" %}
Why do n mutually conjugate vectors form a basis for R^n?&#x20;

Ans: [https://home.cc.umanitoba.ca/\~lovetrij/cECE7670/2005/Slides/slides4.pdf](https://home.cc.umanitoba.ca/\~lovetrij/cECE7670/2005/Slides/slides4.pdf)
{% endhint %}



### Iterative Method

Another kind of really different way to see this is from the perspective of optimization on gradient descent, this where the "gradient descent" comes from in "conjugate gradient descent". The way to look at solving $$Ax=b$$, is to see it as minization of following problem

$$
f(x) = \frac{1}{2}x^TAx - bx
$$

Now to minimize $$f(x)$$, we need $$f'(x)=0$$. Hence

$$
f'(x) =0 := Ax-b = 0
$$

Which is exactly the equation we want to solve. And since $$f''(x)=A$$and since $$A$$ is PSD, can be sure sure that solution is minima and not a maxima.&#x20;

#### Orthogonal gradient descents

Generally to minimize the f(x), we can use gradient descent. Start with initial $$x$$, and move into the direction of gradient descents to iterate to new $$x$$.&#x20;

Conjugate gradient descent is different in the way that in conjugate gradient descent, the gradients updates are conjugate to each other or orthogonal to each other wrt matrix $$A$$. To do this, we use [Gram-Schmidt orthonormalization](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt\_process). Basically we subtract any components of previous gradient directions from the current gradient direction which we get from gradient descent direction.&#x20;

### Properties of CGD

* The matrix $$A$$need to be PSD.&#x20;
* For a system of n variables. The CGD should converge in n iterations.&#x20;

##

{% embed url="https://www.math.purdue.edu/~eremenko/dvi/lect4.9.pdf" %}





&#x20;





