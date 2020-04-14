---
description: 'Notes on Probability, Statistics and more'
---

# Probability & Statistics

### Brief Introduction

{% file src="../.gitbook/assets/probs\_stats.pdf" caption="Very good comprehended summary" %}

### Notation

* Uppercase $$X$$ denotes a random variable
* Uppercase $$P(X)$$ denotes the probability distribution over that variable
* Lowercase $$x∼P(X)$$ denotes a value $$x$$ sampled \(∼\) from the probability distribution $$P(X)$$ via some generative process.
* Lowercase $$p(X)$$ is the density function of the distribution of $$X$$. It is a scalar function over the measure space of $$X$$.
* $$p(X=x)$$\(shorthand $$p(x)$$\) denotes the density function evaluated at a particular value x. 

### Probability vs Liklihood

{% embed url="https://youtu.be/pYxNSUDSFH4" %}

When you say probability, is a number between 0 to 1 for some event to happen. Whereas liklihood is the value which tells relative chances of some event to happen. To understand better, lets consider a constinuous random variable with gaussian distribution with mean $$\mu$$ and stddev $$\sigma$$. Now if what's the probability of random variable to be exactly say s $$\mu$$, it's 0. But it's liklihood is greatest. Probability is given by area under curve of distribution, whereas liklihood is the value at the point on the distribution curve. 

### Stationarity 

If a process is stationery then it means that its density \(probability distribution\) doesn't change with time.

### Why liklihood function is not pdf?

{% embed url="https://stats.stackexchange.com/questions/31238/what-is-the-reason-that-a-likelihood-function-is-not-a-pdf" %}

{% embed url="http://www.medicine.mcgill.ca/epidemiology/hanley/bios601/Likelihood/Likelihood.pdf" %}

### Inverse transform sampling

The problem that the inverse transform sampling method solves is as follows:

* ![X](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) be a [random variable](https://en.wikipedia.org/wiki/Random_variable) whose distribution can be described by the [cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function) ![F\_{X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/062f285db773e329f6c270cb6b65fa076996c941).
* We want to generate values of![X](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) which are distributed according to this distribution.

The inverse transform sampling method works as follows:

1. [Generate a random number](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) ![u](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3e6bb763d22c20916ed4f0bb6bd49d7470cffd8) from the standard uniform distribution in the interval ![\[0,1\]](https://wikimedia.org/api/rest_v1/media/math/render/svg/738f7d23bb2d9642bab520020873cccbef49768d), e.g. from ![{\displaystyle U\sim \mathrm {Unif} \[0,1\].}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a9e3cdfcf6e4924900b93b518404f5cc72450b08)
2. Find the inverse of the desired CDF, e.g. ![{\displaystyle F\_{X}^{-1}\(x\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d4e3b49252612dfa2bcf7d6a20ba1266a198cce1).
3. Compute ![{\displaystyle X=F\_{X}^{-1}\(u\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2c4b8c18425bf8195c62fe4b5777bb79a8c0f38c). The computed random variable![X](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) has distribution![F\_X\(x\)](https://wikimedia.org/api/rest_v1/media/math/render/svg/242727215e028fc47529c5bd7035e88cc0da25e0).

Expressed differently, given a continuous uniform variable ![U](https://wikimedia.org/api/rest_v1/media/math/render/svg/458a728f53b9a0274f059cd695e067c430956025) in ![\[0,1\]](https://wikimedia.org/api/rest_v1/media/math/render/svg/738f7d23bb2d9642bab520020873cccbef49768d) and an [invertible](https://en.wikipedia.org/wiki/Inverse_function) cumulative distribution function ![F\_{X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/062f285db773e329f6c270cb6b65fa076996c941), the random variable![{\displaystyle X=F\_{X}^{-1}\(U\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d47e8c0c30eb57acfb6a06cf5a9345483e583192) has distribution ![F\_{X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/062f285db773e329f6c270cb6b65fa076996c941) \(or, ![X](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) is distributed ![F\_{X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/062f285db773e329f6c270cb6b65fa076996c941)\).

So, this can be basically use to draw samples from different probability distributions. 

#### Sampling from Categorical Distribution 

{% embed url="https://stackoverflow.com/questions/7109633/how-to-obtain-a-random-sample-from-a-categorical-distribution-using-matlabs-ran" %}

### Support of Function \(Function can be probability density\)

In mathematics, the support of a real-valued function f **is the subset of the domain containing those elements which are not mapped to zero**.

 The **set-theoretic support** of f, written **supp\(f\)**, is the set of points in X where f is non-zero, and X is domain of f. 

$$
supp(f) = \{x \in X | f(x) \neq 0\}
$$

The support of f is the smallest subset of X with the property that f is zero on the subset's complement. If f\(x\) = 0 for all but a finite number of points x in X, then f is said to have **finite support**.

#### Support of Random Variable

In case of probability distribution, the support of random variable on which distribution is used is same as the support of probability density function. They are used interchangebly many times.  

For [discrete random variables](https://www.statlect.com/glossary/discrete-random-variable), it is the set of all the realizations that have a strictly positive probability of being observed.

Example If a discrete random variable ![X](https://www.statlect.com/images/support-of-a-random-variable__1.png) has [probability mass function](https://www.statlect.com/glossary/probability-mass-function)![\[eq1\]](https://www.statlect.com/images/support-of-a-random-variable__2.png)its support, denoted by ![R\_X](https://www.statlect.com/images/support-of-a-random-variable__3.png), is![\[eq2\]](https://www.statlect.com/images/support-of-a-random-variable__4.png)

