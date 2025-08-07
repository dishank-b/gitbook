# Conjugate Gradient

## Background

The conjugate gradient method is often implemented as an [iterative algorithm](https://en.wikipedia.org/wiki/Iterative_method), applicable to [sparse](https://en.wikipedia.org/wiki/Sparse_matrix) systems that are too large to be handled by a direct implementation or other direct methods such as the [Cholesky decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition).

Iterative methods like CG are suited for use with sparse matrices. If $$A$$ is dense, your best course of action is probably to factor and solve the equation by backsubstitution. The time spent factoring a dense  is roughly equivalent to the time spent solving the system iteratively; and once  is factored, the system can be backsolved quickly for multiple values of  $$b$$. Compare this dense matrix with a sparse matrix of larger size that fills the same amount of memory. The triangular factors of a sparse $$A$$ usually have many more nonzero elements than$$A$$ itself. Factoring may be impossible due to limited memory, and will be time-consuming as well; even the backsolving step may be slower than iterative solution. On the other hand, most iterative methods are memory-efficient and run quickly with sparse matrices.

**NOTE: This method only works, when matrix A is positive definite.**&#x20;

## Problem Setting

Used to solve the linear system of equations denoted by&#x20;

$$
Ax = b
$$

Where $$A$$ is PSD matrix i.e $$x^TAx \geq 0$$ and $$n \times n.$$&#x20;

Another kind of really different way to see this is from the perspective of optimization on gradient descent, this where the "gradient descent" comes from in "conjugate gradient descent". The way to look at solving $$Ax=b$$, is to see it as minization of following problem

$$
f(x) = \frac{1}{2}x^TAx - bx
$$

Now to minimize $$f(x)$$, we need $$f'(x)=0$$. Hence

$$
f'(x) =0 := Ax-b = 0
$$

Which is exactly the equation we want to solve. And since $$f''(x)=A$$and since $$A$$ is PSD, can be sure sure that solution is minima and not a maxima.&#x20;

## Steepest Gradient Descent

Let's first start talking with a version of gradient descent that's called Steepest Descent.

So, in steepest descent we take multiple steps to reach the optimal value. Many of those steps might be in the same direction. Because at each point, we are just going in the direction perpendicular to level sets. What this means, is that we are searching in the span defined by gradients at each point. Something like below

<figure><img src="../.gitbook/assets/image (171).png" alt="" width="375"><figcaption><p>Now this, a lot of steps are in the same direction, but all the gradients are perpendicular to each other.</p></figcaption></figure>

In GD, search is spanned by the gradient vectors and these gradient vectors are orthogonal to each other.

You solve it using iterative methods as follows:

$$
x_{t+1} = x_t - \alpha_t f'(x)
$$

Now, how steepest descent is different from general gradient descent is, that here we try to find an optimal value for step size $$\alpha_t$$.  We find that by using

$$
\alpha_T^\star = \arg\min_{\alpha_t} f(x_t-\alpha_t g_t)
$$

which we find by following

$$
\frac{\partial f(x_t-\alpha_t g_t)}{\partial \alpha_t} = 0 \\
\alpha_t^\star = \frac{g_t^Tg_t}{g_t^TAg_t}
$$

From above equations we also get the following

$$
f'(x_t-\alpha_tg_t) g_t = 0\\
g_{t+1}^Tg_t = 0
$$

i.e gradients are orthogonal to each other at each step.&#x20;

## Conjugate Gradient Descent

In CG, we search in the space defined by direction vectors such that we don't take steps in the same direction, i.e in each iteration, we are exploring in new direction. So for example, finding a point in $$n$$dim space would take only n steps.&#x20;

So you iteratively find different directions, such that they are conjugate orthogonal (<mark style="color:red;">why they need to be conjugate orthogonal?</mark>) to each other and search in those directions.&#x20;

If you think about it, since it's n-dimensional space, you can express each vector as a combination of  $$n$$ independent vectors that spans that $$n$$ dim space, so, let's say you start from $$x_0$$, now you should be able to find $$n$$ components ($$\alpha$$), in which proportion you combine the $$n$$ vectors to get the solution.&#x20;

So basically you find the $$n$$ eigen vectors in the space of optimization, in each step you find one direction and take exactly that much step in that direction that's needed to reach the solution in that direction.  i.e **At each step you are finding the one correct component of the total vector.**&#x20;

<mark style="color:red;">**Key question: How do we find those directions?**</mark>

What this basically means is that each step direction will be orthogonal to each other, but not in euclidean space but in the optimization space.&#x20;

<figure><img src="../.gitbook/assets/image (172).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (173).png" alt="" width="220"><figcaption><p>A comparison of the convergence of <a href="https://en.wikipedia.org/wiki/Gradient_descent">gradient descent</a> with optimal step size (in green) and conjugate vector (in red) for minimizing a quadratic function associated with a given linear system. Conjugate gradient, assuming exact arithmetic, converges in at most <em>n</em> steps, where <em>n</em> is the size of the matrix of the system (here <em>n</em> = 2).</p></figcaption></figure>

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

Ans: [https://home.cc.umanitoba.ca/\~lovetrij/cECE7670/2005/Slides/slides4.pdf](https://home.cc.umanitoba.ca/~lovetrij/cECE7670/2005/Slides/slides4.pdf)
{% endhint %}



### Iterative Method

#### Orthogonal gradient descents

Generally to minimize the f(x), we can use gradient descent. Start with initial $$x$$, and move into the direction of gradient descents to iterate to new $$x$$.&#x20;

Conjugate gradient descent is different in the way that in conjugate gradient descent, the gradients updates are conjugate to each other or orthogonal to each other wrt matrix $$A$$. To do this, we use [Gram-Schmidt orthonormalization](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process). Basically we subtract any components of previous gradient directions from the current gradient direction which we get from gradient descent direction.&#x20;

### Properties of CGD

* The matrix $$A$$ need to be PSD.&#x20;
* For a system of n variables. The CGD should converge in n iterations.&#x20;

## &#x20;Resources

{% embed url="https://discuss.pytorch.org/t/efficient-o-n-hessian-vector-product-with-pearlmutter-trick/59037" %}

{% embed url="https://gregorygundersen.com/blog/2022/03/20/conjugate-gradient-descent/" %}

{% embed url="https://iclr-blogposts.github.io/2024/blog/bench-hvp/" %}

{% embed url="https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf" %}



