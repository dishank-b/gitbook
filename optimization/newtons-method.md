# Newton's Method

### Find Root of non-linear function

Used to find the roots of an function $$f(x)=0$$. It uses taylor series expansion for that. It's an iterative process. Let $$x_0$$be initial starting point. Let's say next point is $$x_1 = x_0 + \Delta x$$, which is the root of the $$f(x)=0$$. Then $$0 = f(x+\Delta x) = f(x) + \Delta x f'(x)$$. Which means $$\Delta x = -\frac{f(x)}{f'(x)}$$.

### Finding minimum of a function

Let's say you have a function $$f(x)$$whose minimum you want to find, this means $$f'(x)=0$$. Hence you can just use newton's method to find root of $$f'(x)=0$$. This will find the minimum of $$f(x)$$if $$f''(x)>0$$.&#x20;

So&#x20;

