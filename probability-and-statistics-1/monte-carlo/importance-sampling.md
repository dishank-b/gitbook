# Importance Sampling

Let's say we have two distribution $$f(x)$$​ and $$g(x).$$​Now the problem is let's say you want to estimate the expectation of $$g(x)$$​but you can't sample from it, hence you won't be able to use sample mean to estimate the expectation. So what we do here is, we use samples from $$f(x)$$​to estimate the expectation of $$g(x)$$​.&#x20;

So we know we can estimate the expectation of $$f(x)$$​ using sample mean by:

$$
E_f[x] \approx \frac{1}{n} \sum_{i=1}^n x_i, \space x_i \sim f(x)
$$

​Now to estimate $$E_g[x]$$ we go trick

$$
E_g[x] = \sum xg(x) = \sum x\frac{g(x)}{f(x)} f(x) = E_f[x\frac{g(x)}{f(x)}]\approx \frac{1}{n} \sum_{i=1}^n x_i\frac{g(x_i)}{f(x_i)}, \space x_i \sim f(x)
$$

### Importance Sampling to estimate probability using Monte Carlo Method

{% embed url="https://youtu.be/pAbQHKr_Zqo" %}

{% embed url="https://youtu.be/C3p2wI4RAi8" %}
