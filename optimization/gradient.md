# Gradient

## Directional Derivative

Before getting into directional derivatives, let's see how the partial derivatives, gradient and total derivative fall into together.&#x20;

For this, we consider a function $$f: \mathbf R^2 \rightarrow \mathbf R$$ , which is basically a scalar function we multivariate input.&#x20;

$$
f(x,y)
$$

### Partial Derivative

Partial derivative is change in function when changing only of the variable, keeping the other fixes, and assuming that the other variable is independed of the first

So we will have two partial derivatives for this - $$\frac{\partial f}{\partial x}$$

$$
\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}
$$

### Gradient

Gradient is basically the vector representation of the partial derivatives.&#x20;

Gradient of a function at point $$p$$, basically gives the direction and the rate of fastest increase.&#x20;

The gradient is represented as $$\nabla f$$. Where

$$
\nabla f = \frac{\partial f}{\partial x} \mathbf i +  \frac{\partial f}{\partial y} \mathbf j
$$

Mostly Gradient is represented at column vector i.e

$$
\nabla f = [\frac{\partial f}{\partial x} ,\frac{\partial f}{\partial y}]^T
$$

Gradient is the change in the input. <mark style="color:orange;">(Make this more clear),</mark> [<mark style="color:orange;">https://en.wikipedia.org/wiki/Gradient#Relationship\_with\_derivative</mark>](https://en.wikipedia.org/wiki/Gradient#Relationship\_with\_derivative)

Imagine a 3D graph, which is like hills and valleys. $$x$$and $$y$$ are two dimension and $$f(x,y)$$ determines the hieght of graph at $$x,y$$. Now imagine a ball at any point on the surface of the graph. Now the if let the ball roll, the $$- \nabla f$$basically gives you the direction of where the ball would roll towards.&#x20;



### Derivative

Derivative is&#x20;



### Directional Derivative

{% embed url="https://youtu.be/N_ZRcLheNv0" %}
