# Conjugate Priors

## Definition

In [Bayesian probability](https://en.wikipedia.org/wiki/Bayesian\_probability) theory, if the [posterior distributions](https://en.wikipedia.org/wiki/Posterior\_probability) p(θ | x) are in the same [probability distribution family](https://en.wikipedia.org/wiki/List\_of\_probability\_distributions) as the [prior probability distribution](https://en.wikipedia.org/wiki/Prior\_probability\_distribution) p(θ), the prior and posterior are then called **conjugate distributions,** and the prior is called a **conjugate prior** for the [likelihood function](https://en.wikipedia.org/wiki/Likelihood\_function). For example, the [Gaussian](https://en.wikipedia.org/wiki/Normal\_distribution) family is conjugate to itself (or self-conjugate) with respect to a Gaussian likelihood function: if the likelihood function is Gaussian, choosing a Gaussian prior over the mean will ensure that the posterior distribution is also Gaussian. This means that the Gaussian distribution is a conjugate prior for the likelihood that is also Gaussian.

A conjugate prior is an algebraic convenience, giving a [closed-form expression](https://en.wikipedia.org/wiki/Closed-form\_expression) for the posterior; otherwise [numerical integration](https://en.wikipedia.org/wiki/Numerical\_integration) may be necessary. Further, conjugate priors may give intuition, by more transparently showing how a likelihood function updates a prior distribution.

Consider the general problem of inferring a (continuous) distribution for a parameter θ given some datum or data x. From [Bayes' theorem](https://en.wikipedia.org/wiki/Bayes'\_theorem), the posterior distribution is equal to the product of the likelihood function ![\theta \mapsto p(x\mid \theta )\\!](https://wikimedia.org/api/rest\_v1/media/math/render/svg/96dfc31ae08ab5d02db0d99cef8b327f1f839164) and prior ![p(\theta )\\!](https://wikimedia.org/api/rest\_v1/media/math/render/svg/980b1be0ef55b780d356c0e862e0201d85cb83a7), normalized (divided) by the probability of the data ![p(x)\\!](https://wikimedia.org/api/rest\_v1/media/math/render/svg/f6443aa49b219e538b727f7fbdf10194d4225ba9):![{\displaystyle {\begin{aligned}p(\theta \mid x)&={\frac {p(x\mid \theta )\\,p(\theta )}{p(x)\}}\\\\&={\frac {p(x\mid \theta )\\,p(\theta )}{\int p(x\mid \theta ')\\,p(\theta ')\\,d\theta '\}}\end{aligned\}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/5e63aab92e95d8738f27c1ba7a61d8aba90359e3)

Let the likelihood function be considered fixed; the likelihood function is usually well-determined from a statement of the data-generating process, hence this liklihood faunction is also called sampling distribution. It is clear that different choices of the prior distribution p(θ) may make the integral more or less difficult to calculate, and the product p(x|θ) × p(θ) may take one algebraic form or another. For certain choices of the prior, the posterior has the same algebraic form as the prior (generally with different parameter values). Such a choice is a conjugate prior.

{% embed url="https://medium.com/paper-club/analytical-bayesian-inference-with-conjugate-priors-4a1d75ca799b" %}

**Check above to see how conjugate prior helps in analytically solve the posterior.**&#x20;

## Pseudo-observations/Priors Hyperparameters.

Priors Hyper parameters are the parameters of the prior distribution. For example, $$\alpha$$vector in dirichlet distribution, $$(\alpha, \beta)$$in Beta Distribution, etc.&#x20;

It is often useful to think of the hyperparameters of a conjugate prior distribution as corresponding to having observed a certain number of pseudo-observations with properties specified by the parameters.  In general, for nearly all conjugate prior distributions, the hyperparameters can be interpreted in terms of pseudo-observations. This can help both in providing an intuition behind the often messy update equations, as well as to help choose reasonable hyperparameters for a prior.

Look at the example here to understand: [https://en.wikipedia.org/wiki/Conjugate\_prior](https://en.wikipedia.org/wiki/Conjugate\_prior)

{% embed url="https://stats.stackexchange.com/questions/244917/what-exactly-is-the-alpha-in-the-dirichlet-distribution" %}

In the first answer, see how $$\alpha$$ represents Pseudo-count in Dirichlet Distribution. Basically, choosing the correct value of $$\alpha$$allows you to get the right prior about the parameters. Hence, those $$\alpha$$basically encoded the prior information you have. In the above exmample, and guess of how many balls of each color are there in the bag decided your prior and represents by appropriate value of $$\alpha$$. &#x20;

## Resources

{% embed url="https://people.eecs.berkeley.edu/~jordan/courses/260-spring10/other-readings/chapter9.pdf" %}

