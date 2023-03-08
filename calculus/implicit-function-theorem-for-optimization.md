# Implicit Function Theorem for optimization

### Intuition of Implicit differentiation

Implicit differentiation is mainly used for when we have implicit functions.&#x20;

Think about a function $$g(x,y)=c$$, now this function implicitly defines a relation between the variables x and y. $$x^2+y^2 = 1$$ is an example of such a function, where x and y are points on circle of radius 1.&#x20;

Now, the point of implict differentiation is that in a very you can define a explicit function in a very local region of the graph such that: $$y=h(x)$$. but this hold for only very near points of $$(x,y)$$.  And how you find this $$y=h(x)$$ is given by implicit differentiation the contraint $$g(x,y)=c\$$

So you differentiaite on both side and you get&#x20;

$$
dg = \frac{\partial g}{\partial x} dx + \frac{\partial g}{\partial y}dy = 0 \\ \quad \\
\frac{dy}{dx} = - \frac{\frac{\partial g}{\partial x}}{\frac{\partial g}{\partial y}}
$$

Now this $$\frac{dy}{dx}$$ defines a locally applicable $$y=h(x)$$, as you can just integrate the differentiable equation to find the h(x).&#x20;

**This is called Implicit Function Theorem.**&#x20;

{% embed url="https://math.stackexchange.com/questions/1178594/optimization-with-implicit-differentiation" %}

{% embed url="https://torchopt.readthedocs.io/en/latest/implicit_diff/implicit_diff.html" %}



{% embed url="https://mml-book.github.io/neurips2020/09-implicit-diff.pdf" %}

{% embed url="https://youtu.be/iSIk_koZ3sA" %}



{% embed url="http://mathonline.wikidot.com/the-implicit-differentiation-formulas" %}
