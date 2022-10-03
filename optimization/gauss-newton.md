# Gauss-Newton

It is an extension of Newton's method used **non-linear least square problems** where you **don't need to calculate the Hessian**. &#x20;

&#x20;The formulation is something like $$m$$functions $$r = (r_1, ......, r_m)$$ which are called residuals, with $$n$$ variables/parameters to be optimized $$\beta = (\beta_1, ......., \beta_n)$$.&#x20;

And we want to minimize the sum of sqaures

$$
S(\beta) = \sum_i^m r_i(\beta)^2
$$

Update equation for this comes out to be:

![](<../.gitbook/assets/image (165).png>)

and most of the time we have residual $$r_i(\beta)$$as $$r_i(\beta) = y_i - f(x_i, \beta)$$ _._&#x20;

​**Now just apply Newton's method in this and in the calculation of Hessian of the function, just ignore the 2nd order term, the hessian will basically be some function of jaobian.** &#x20;
