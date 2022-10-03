# Monte Carlo Estimators

### Resources

* [https://www.pbr-book.org/3ed-2018/Monte\_Carlo\_Integration/The\_Monte\_Carlo\_Estimator](https://www.pbr-book.org/3ed-2018/Monte\_Carlo\_Integration/The\_Monte\_Carlo\_Estimator)
* [http://faculty.washington.edu/yenchic/17Sp\_403/Lec2\_MonteCarlo.pdf](http://faculty.washington.edu/yenchic/17Sp\_403/Lec2\_MonteCarlo.pdf)

### Summary

Let's say we have to compute some quantity, which is difficult to compute, let's say some integral of a difficult function $$f$$. Then what we do in this method, sample some points from some distribution and then evaluate that function on those points and then do some computation of those function evaluation at those points to estimate the quantity in interest.&#x20;

It's basically using sampling from some simple known distribution to estimate something difficult. By evaluating the quantity on those samples points and taking average of all those to estimate the quantity.&#x20;

### First Principal

I think the first principal which monte carlo methods use is the relation between expectation vs integration. This relation relates the problems of numerical computation (computing some difficult quantity) to problem of expectation computation which can be easily computed as numerical average.&#x20;

Let's say the difficult numerical computation is finding a integral of very difficult function $$f$$, now the $$f$$​ is very difficult such that analytic integration of $$f$$​ which is $$\int_0^1 f(x)dx$$​ not is not feasible. So how do we estimate this integral

so now we can write $$\int_0^1 f(x)dx$$​as

$$
\int_0^1 f(x)dx = \int_0^1 f(x) \cdot 1dx = E_{x\sim U[0,1]}[f(x)]
$$

​So we converted the problem of integration to finding the expected value. Now to estimate $$E_{x\sim U[0,1]}[f(x)]$$we can use average. So we can calculate $$E[f(x)] = \frac{1}{N} \sum_{i=1}^N f(x_i)$$where $$x_i \sim U[0,1]$$.  Now since the the interval of integration was \[0,1] and we used Uniform distribution to sample the points, we could directly take the average of function evaluated at sample points. But if the can choose which distribution $$p(x)$$​ to use to sample $$x$$​ to evaluate $$f$$​at. So for any arbitrary $$p(x)$$​we can write the above integral as.

$$
\int f(x) dx = \int \frac{f(x)}{p(x)} p(x) dx = E_{x\sim p(x)}[\frac{f(x)}{p(x)}]
$$

​So basically this will give unbiased estimator to estimate the integral. The choice of $$p(x)$$​ dictates the convergence of monte carlo estimate to true value of integral.&#x20;

The factor of $$\frac{1}{p(x)}$$​relates to the concept of **Importance Sampling** because when we sample $$x$$ according to $$p(x)$$we need to counter that effect, hence downweighting by that factor.&#x20;
