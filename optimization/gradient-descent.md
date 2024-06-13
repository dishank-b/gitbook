# Gradient Descent

Simply use gradient information.

Let's say you have function $$f(x)$$ that you want to mimimize.&#x20;

With gradient descent to just iterate to move $$x$$ in the negative of the gradient i.e $$-f'(x)$$. Hence at each step, we take one gradient step as below

$$
\mathbf x_{t+1} = \mathbf x_{t} - \alpha f'(\mathbf x)
$$

Here $$\alpha$$is the step size, determines how big do we want to move in the direction of negative of gradient $$f'(\mathbf x )$$.&#x20;

**The above equation basically represents a eqn of line in vector form. Where the line start passes** $$\mathbf x_t$$ **in the direction of vector** $$f'(\mathbf x)$$**. For all the values of** $$\alpha$$**, you will be able to get all the points that lies on that line.**&#x20;

