---
description: Gradients, Jacobians, etc in Matrix algebra
---

# Matrix Calculus

## Gradient

$$f: \mathcal{R}^d \rightarrow \mathcal{R}$$ where $$f$$ is some function.

$$
\hat y = f(\mathbf w)
$$

Here $$\mathbf w \in \mathcal{R}^d$$, now for some reason we have want the derivative of $$f$$ wrt to each elements of $$\mathbf w$$, that will be called gradient. Represented as follows:

$$
\nabla_\mathbf w f(\mathbf w) = [\frac{\partial f}{\partial w_1}, \dots, \frac{\partial f}{\partial w_d}]^T
$$

The $$\text{grad}$$ $$\nabla_\mathbf w f(\mathbf w)$$is supposed to be also a horizontal vector of same dimension as $$\mathbf w$$.

* **Note that the** $$f(\mathbf w)$$ is scalar values function but $$\nabla_\mathbf w f(\mathbf w)$$ is actually a vector values function.&#x20;
* The gradients are perpendicular to the contour lines of the curve $$f$$.
* The gradient of $$f$$points in the direction of the steepest ascent. Why? Think using directional derivatives.&#x20;

### Gradient in Matrix, Vector forms

Let's say that $$f( \mathbf w) = \mathbf w\cdot \mathbf x = \mathbf w^T\mathbf x = \mathbf x^T \mathbf w$$ which is simply a linear function. Here x is some input vector of dimension same as . Then we have&#x20;

$$
\nabla_{\mathbf w} f(\mathbf w) = \nabla_\mathbf w (\mathbf w^T \mathbf x) = \mathbf x
$$

## Jacobian

Now let $$f: \mathcal{R}^n \rightarrow \mathcal{R}^m$$. In this case we would have a jacobian $$J$$

$$
J = \begin{bmatrix}
\frac{\partial \mathbf f}{\partial x_1} & \dots & \frac{\partial \mathbf f}{\partial x_n}\\
\end{bmatrix} \\
= \begin{bmatrix}
\nabla^T f_1\\
\dots\\
\nabla^T f_m\\
\end{bmatrix} \\
= \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \dots & \frac{\partial  f_1}{\partial x_n}\\
\vdots & \dots & \vdots\\
\frac{\partial f_m}{\partial x_1} & \dots & \frac{\partial  f_m}{\partial x_n}\\
\end{bmatrix}
$$

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption><p>Dimension of reulting Jacobian shape based on function and input shape</p></figcaption></figure>

{% hint style="info" %}
Note: Jacobian and Gradient are transpose of each other. So, if you try to calculate derivative of single value function with respect to a vector using Jacobian, it would be a row vector. So to get a gradient you have transpose it.&#x20;
{% endhint %}

## Chain Rule

### Vector

Let $$\mathbf{f, g}$$ be two vector valued function and $$x$$ be a scalar. Then

$$
\nabla_x \mathbf f = \frac{\partial  \mathbf {f(g(}x))}{\partial x} = \frac{\partial \mathbf f}{\partial \mathbf g}\frac{\partial \mathbf g}{\partial x}
$$

Now if there are multiple paramteres i.e. it's a vector $$\mathbf x$$. Then it's&#x20;

$$
\nabla_{\mathbf x} \mathbf f = \frac{\partial  \mathbf {f(g(x))}}{\partial \mathbf x} = \frac{\partial \mathbf f}{\partial \mathbf g}\frac{\partial \mathbf g}{\partial \mathbf x}
$$

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption><p>Full Jacobian Calculation</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption><p>Chain Rule for different dimension of variables.</p></figcaption></figure>

## Resources

{% embed url="https://explained.ai/matrix-calculus/" %}

{% embed url="https://souryadey.github.io/teaching/material/Matrix_Calculus.pdf" %}

{% embed url="https://atmos.washington.edu/~dennis/MatrixCalculus.pdf" %}

{% embed url="http://dsp.ucsd.edu/~kreutz/PEI-05%20Support%20Files/ECE275A_Viewgraphs_5.pdf" %}
