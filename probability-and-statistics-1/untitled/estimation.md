---
description: 'Lets talk about estimators, estimates, etc'
---

# Estimation

### Estimation

As you know in statistics we try to understand a **large** population on the basis of information available in a **small** sample. Among what we mean by "understand" is to know the values of the population **parameters**. The game here is to use **suitable** sample **statistics** to _**estimate**_ population **parameters**. For example, we may like to use the sample mean $$\bar x$$ as an estimate for the population mean $$\mu$$ .

So mostly when we will be talking about estimations, we will talk about estimating:

* Parameter of distributions $$\boldsymbol{\theta}$$, for example if we assume our population to follow Gaussian distribution, then we will estimated its mean and variance. 
* Parameters of some model$$\boldsymbol{w}$$, for example in our neural networks we estimate the weights of our network using gradients based on loss.
* Output, for example we have output of neural network as $$\hat{y}$$, which is basically estimation.   

### Estimator  & Estimate

An estimator is basically a **random variable** $$X$$, a random variable have set of possible values which it can realize as part of experiment called as its **Sample Space**. Generally an estimator is an statistic, for ex: sample mean $$\bar X$$ which is an statistic is an estimator for population mean $$\mu$$. _For example, a neural network is an **estimator.**_

An estimate is basically **number** $$x$$**which is realization of estimator** $$X$$as part of some experiment. Hence, $$x$$will definitely lie in Sample Space of $$X$$. 

For example, we say that the sample mean X is an estimator of the population mean m and the computed value x of X is an estimate of m. The estimator is a sampling random variable and the estimate is a number. Similarly, the sample standard deviation $$S$$ is an estimator of the population standard deviation $$\sigma$$ and the computed value $$s$$ of $$S$$ is an estimate of $$\sigma$$.

Example: I got a sample and I take the variance $$S$$of that sample.  
The sample that you take is a random sample from your population, so the sample variance $$S$$ is \(at least before you actually take the sample of the population and compute the sample variance\) itself a random variable. If you can figure out the distribution of the sample variance, then you can find its expected value.  
In general, once we have the sample in place, the estimator that we compute is a fixed value that depends on the actual sample that we got. **Until we've taken the sample, it's a random variable that we can analyze in terms of expected value, variance, etc.**

Note the estimate depends upon the actual value of data you sampled, where as estimator is just a random variable without any value assigned to it. 

#### Slightly different definition for an estimator:

an _estimator_ is a definite mathematical procedure \(a random variable is also a function\) that comes up with a number \(the _estimate_\) for any possible set of data that a particular problem could produce. That number is intended to represent some definite numerical property \(g\(θ\)\) of the data-generation process; we might call this the "estimand."  


### Bias of Estimator

Bias is the tendency of a statistic or estimate to **overestimate** or **underestimate** a parameter. See [here](statistic-vs-parameter.md) to get what is difference between statistic and a parameter.  Bias is a property of the estimator. 

Mathematically, the **bias** \(or **bias function**\) of an [estimator](https://en.wikipedia.org/wiki/Estimator) is the difference between this estimator's [expected value](https://en.wikipedia.org/wiki/Expected_value) and the true value of the parameter being estimated. I.e difference between mean of estimated value from different samples and actual population parameter. Note that it's not the difference with single estimated value but with mean of different estimated values over different samples. 

Let $$\hat \theta$$ be an estimator and $$\theta$$ be an parameter or estimand. Then Bias is given by 

$$
Bias(\hat \theta) = E[\hat \theta] - \theta
$$

Note the expectation in the above formula. 

Suppose we have a [statistical model](https://en.wikipedia.org/wiki/Statistical_model), parameterized by a real number θ, giving rise to a probability distribution for observed data, ![P\_{\theta }\(x\)=P\(x\mid \theta \)](https://wikimedia.org/api/rest_v1/media/math/render/svg/cf0c92a2f9f331565f351f716b59a2d1167eebbf), and a statistic ![{\hat {\theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0eaae56d74c5844e86caeed8ae205ff9e413bba) which serves as an [estimator](https://en.wikipedia.org/wiki/Estimator) of θ based on any observed data ![x](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4). That is, we assume that our data follow some unknown distribution ![P\(x\mid \theta \)](https://wikimedia.org/api/rest_v1/media/math/render/svg/88296f80b46f26a18ff8e11652dd7ca556f2fb8c) \(where θ is a fixed constant that is part of this distribution, but is unknown\), and then we construct some estimator![{\hat {\theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0eaae56d74c5844e86caeed8ae205ff9e413bba) that maps observed data to values that we hope are close to θ. The **bias** of ![{\hat {\theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0eaae56d74c5844e86caeed8ae205ff9e413bba) relative to ![\theta ](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e5ab2664b422d53eb0c7df3b87e1360d75ad9af) is defined as![{\displaystyle \operatorname {Bias} \_{\theta }\[\,{\hat {\theta }}\,\]=\operatorname {E} \_{x\mid \theta }\[\,{\hat {\theta }}\,\]-\theta =\operatorname {E} \_{x\mid \theta }\[\,{\hat {\theta }}-\theta \,\],}](https://wikimedia.org/api/rest_v1/media/math/render/svg/82a9c6501a54260ed0edd2f03923719b9f2db906)

where ![{\displaystyle \operatorname {E} \_{x\mid \theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d54ff58946b27eaddcb35b7c337af8cbc4be8efa) denotes [expected value](https://en.wikipedia.org/wiki/Expected_value) over the distribution ![P\(x\mid \theta \)](https://wikimedia.org/api/rest_v1/media/math/render/svg/88296f80b46f26a18ff8e11652dd7ca556f2fb8c), i.e. averaging over all possible observations![x](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4). The second equation follows since θ is measurable with respect to the conditional distribution![P\(x\mid \theta \)](https://wikimedia.org/api/rest_v1/media/math/render/svg/88296f80b46f26a18ff8e11652dd7ca556f2fb8c).

An estimator is said to be **unbiased** if its bias is equal to zero for all values of parameter θ.

