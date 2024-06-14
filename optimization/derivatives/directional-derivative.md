# Directional Derivative

So in partial derivatives, you only consider the derivative when changing one of the variable while keeping others fixed. So in case of $$f(x,y)$$, we you find $$\frac{\partial f}{\partial x}$$, you are basically cutting the graph at fixed $$y$$, and now just changing. Similar of partial wrt $$y$$, you keep x constant.

But in multivariate functions, you can calculate the derivative in multiple directions and not just two. For example you can ask about the derivative in the direction \[1,2] ie if $$x$$changes 1 unit and $$y$$changes 2 unit.&#x20;

Imagine 3D graph, with $$z=f(x,y)$$, now here imagine vertical planes that cuts through the graph. $$\frac{\partial f}{\partial x}$$ is when you are cutting the graph with a plane at some $$y_0$$where plane is parallel to  $$x-z$$ plane. Similary for $$\frac{\partial f}{\partial y}$$. But there are multiple more vertical planes possible that goes cuts trough the graph.

**So the directional derivative allows for us to calculate the derivative in the direction of the plane that cuts the graph.**&#x20;

<figure><img src="../../.gitbook/assets/image (170).png" alt="" width="375"><figcaption></figcaption></figure>

### Directional Derivative as a limit

Directional Derivative is basically the rate of change in some particular direction. Basically, when you partial derivative, you measure the delta in output for delta in the input.&#x20;

Now, in case when the input is multidimensional, i.e it's a vector. You can measure the delta in output when the delta in the input in some particular direction and not just in $$x$$or $$y$$ direction.&#x20;

Hence mathematically, the direction derivative is:

$$
\frac{\partial f}{\partial \vec v} = \nabla_{\vec v}f(\vec a) = \lim_{h\to 0} \frac{f(\vec a+h\vec v)-f(\vec a)}{h}
$$

So basically this gives you the derivative along the direction $$\vec v$$. But not here that $$\vec v$$ just supposed to represent the direction and hence it's magnitude it's sort of irrelevant, but the derivative will change let's say if you have $$2\vec v$$.

### Directional Derivative as a Slope

{% embed url="https://youtu.be/4tdyIGIEtNU" %}





### Resources

{% embed url="https://youtu.be/4RBkIJPG6Yo" %}

{% embed url="https://youtu.be/GJODOGq7cAY" %}
