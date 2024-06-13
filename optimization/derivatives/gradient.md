# Gradient

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

Imagine a 3D graph, which is like hills and valleys. $$x$$and $$y$$ are two dimension and $$f(x,y)$$ determines the hieght of graph at $$x,y$$. Now imagine a ball at any point on the surface of the graph. Now the if let the ball roll, the $$- \nabla f$$basically gives you the direction of where the ball would roll towards.&#x20;

{% embed url="https://youtu.be/QQPz3eXXgQI" %}

### Relationship between Gradient and Derivative

Gradient is the change in the input. <mark style="color:orange;">(Make this more clear),</mark> [<mark style="color:orange;">https://en.wikipedia.org/wiki/Gradient#Relationship\_with\_derivative</mark>](https://en.wikipedia.org/wiki/Gradient#Relationship\_with\_derivative)

### &#x20;Graident and Trangent Plane

<figure><img src="../../.gitbook/assets/image (169).png" alt=""><figcaption></figcaption></figure>

Tangent plant is the plane passing through the point and both partial derivatives of the function $$f(x,y)$$

Basically both the tangent lines lies in the tangent plane. And two lines passing through a plane are enough to get a unique plane equation.&#x20;
