---
description: Gradients, Jacobians, etc in Matrix algebra
---

# Matrix Calculus

## Gradient

$$f: \mathcal{R}^d \rightarrow \mathcal{R}$$ where $$f$$ is some function.

$$
\hat y = f(\omega)
$$

Here $$\omega \in \mathcal{R}^d$$, now for some reason we have want the derivative of $$f$$ wrt to each elements of $$\omega$$, that will be called gradient. Represented as follows:

$$
\nabla_\omega f(w) = [\frac{\partial f}{\partial \omega_1}, \dots, \frac{\partial f}{\partial \omega_d}]^T
$$

The $$\text{grad}$$ $$\nabla_\omega f(w)$$is supposed to be also a vector of same dimension as $$\omega$$.

* **Note that the** $$f(\omega)$$ is scalar values function but $$\nabla_\omega f(w)$$ is actually a vector values function.&#x20;
* The gradients are perpendicular to the contour lines of the curve $$f$$.
*   The gradient of $$f$$points in the direction of the steepest ascent. Why? Think using directional derivatives.&#x20;



#### Gradient in Matrix, Vector forms

Let's say that $$f(\omega) = \omega^Tx$$, which is simply a linear function. Here x is some input vector of dimension same as . Then we have&#x20;

$$
\nabla_\omega f(w) = \nabla_\omega (\omega^Tx) = x
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



## Resources

{% embed url="https://explained.ai/matrix-calculus/" %}

{% embed url="http://dsp.ucsd.edu/~kreutz/PEI-05%20Support%20Files/ECE275A_Viewgraphs_5.pdf" %}

{% embed url="https://atmos.washington.edu/~dennis/MatrixCalculus.pdf" %}
