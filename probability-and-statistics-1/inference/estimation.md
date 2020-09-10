---
description: 'Lets talk about estimators, estimates, etc'
---

# Estimation

### Estimation

As you know in statistics we try to understand a **large** population on the basis of information available in a **small** sample. Among what we mean by "understand" is to know the values of the population **parameters**. These populations parameters partially describes the population or say distribution of population. The game here is to use **suitable** sample **statistics** to _**estimate**_ population **parameters**. For example, we may like to use the sample mean $$\bar x$$ as an estimate for the population mean $$\mu$$ .

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

#### Random Variables are functions or mathematical procedures and hence Estimators. 

An _estimator_ is a definite mathematical procedure \(a random variable is also a function\) that comes up with a number \(the _estimate_\) for any possible set of data that a particular problem could produce. That number is intended to represent some definite numerical property \(g\(θ\)\) of the data-generation process; we might call this the "estimand."

**NOTE: Often** $$\hat \theta$$is used to denote both estimator and estimate. The meaning should be clear from the context. Estimator $$\hat \theta$$ is a random variable and have distribution associated with it. Estimate $$\hat \theta$$is realization of estimator for some particular sample, basically a point sampled form estimator's distribution. 

### Are you a Good Estimator?

Are are estimators for? Estimators are for estimating some population parameters. But now the thing is you can have multiple estimators for same population parameters. For example you can use $$\frac{\sum X_i}{n}$$  
as estimator for estimating mean or you can also use $$\frac{\sum X_i}{n-1}$$. How do you know which one is better and what makes you actually use $$\frac{\sum X_i}{n}$$ to estimate population mean.   
To answer this, you have to analyse some properties of the estimators and based on those properties you decide which estimator is good. What properties are used to analyse estimators?

* Estimator's sampling distribution
* Bias of Estimator - Related to sampling distribution
* Variance of Estimator- Related to sampling distribution

### Distribution of Estimator

{% embed url="http://www.bristol.ac.uk/medical-school/media/rms/red/sampling\_variation\_and\_sampling\_distributions.html" %}

{% embed url="https://youtu.be/IoTgFiso8sA" %}



How does estimators works? You take an sample from the population, you calculate an estimate from the sample defined by your estimator. Now you have an estimate of some population parameter. Now if you draw other sample from the population, you can again estimate the parameter. 

* Visualize calculating an estimator over and over with different samples from the same population, i.e. take a sample, calculate an estimate using that rule, then repeat.
* This process yields sampling distribution for the estimator

**Distribution of estimator is also called Sampling Distribution of estimator.** 

Basically, an estimator is also a random variable, so it will also have an distribution associated with it. You can get this distribution by having multiple estimates using multiple sample from the populations. 

We look at the mean of this sampling distribution to see what value our estimates are centered around. This is basically the expectation \(expected value\) of estimator $$E[\hat \theta]$$ . $$\hat \theta$$is our estimator. 

The spread of this distribution is the variance of the estimator. $$Var[\hat \theta]$$

**If you will think about it our distribution of estimator is basically the distribution of parameter. I mean that parameter** $$\theta$$**is actually a fixed constant \(most of the times unknown\), it's just a point value and not a random variable so it can't have distribution. But to get that actual point value of** $$\theta$$**we get multiple estimates and those estimates actually makes the distribution. Hence this how we get parameter's distribution, but it is actually estimator's.   
Note that how people can easily use word parameter in place of it's estimator. Be carefully because many times when people are talking about parameter, they might actually mean it's estimator.  Hence, many times you can use parameter instead of estimator because we  know that actual value of parameter is unknown, hence talking about parameter means talking about our understanding of parameter which is it's estimator.** 

**Remember whenever someone say distribution of parameter, it means distribution of parameter's estimator. Because most of the time actual parameter is unknown and hence we try to find out that parameter's value, but we can actually only find a distribution using multiple estimates of that parameter.** 

#### Example:

Let's say we have parameter $$g$$\(gravity\), note it is a fixed constant, it's just that we don't know it's value hence unknown. What are we gonna do to get the value of $$g$$. We are gonna setup a physics experiment using which we will try to estimate the value of $$g$$. So this experiment is some mathematical procedure using which we gonna try to estimate value of $$g$$. **Hence this experiment is nothing but basically an estimator.** But will write mathematical equation of this experiment which will make more clear that how this experiment is an estimator. What physics experiment can you think to estimate $$g$$? I think can two of either free fall experiment or pendulum. Basically drop a ball from height $$h$$and measure it's velocity at ground, this is represent by $$v^2=2gh$$. Or measure time period of a pendulum, $$T=2\pi \sqrt \frac{g}{L}$$. When I said these experiment is our estimator, how? These experiment gives us the mathematical procedure to estimate $$g$$. Hence basically these equations is our estimator. Let's we choose free body experiment. Then we have estimator $$\boldsymbol{ \hat g} = \frac{v^2}{2h}$$. This is estimator is given by mathematical equation \(procedure\) which is given by experiment. Hence the experiment is the estimator. Now let's say we did the experiment 5 times and got following measurement for $$ v = [10,20,15,25,20]$$and $$h=[5, 22, 11,32,20]$$. Using these value we get following estimates $$\hat g$$for actual parameter g $$[10.00,9.09, 10.22,9.26, 10 ]$$. So, these are the estimates for the parameter $$g$$. These values basically gives us the distribution of parameter $$g$$but actually is distribution of estimator $$\boldsymbol {\hat g}$$. Now expectation of$$\boldsymbol {\hat g}$$$$=\frac{10.00+9.09+10.22+9.26+ 10}{5} = 9.71$$. 

### Bias of Estimator

When you draw a sample and calculate an estimate of some population parameter, that estimate might not be exactly equal to the actual population parameter, there will be some error between actual parameter and single estimate i.e. an estimate may overestimate or underestimate the parameter. 

But that's the beauty of statistics, you don't need to restrict yourself to a single estimate, instead you can draw more samples and calculate multiple estimate for the same parameter. Now all of these estimates may be bit more or less than the actual value of parameter. **So, the actual thing to measure how good is your estimator is not single estimate rather the mean of all the estimates.** Hence, for a good estimator, mean of all the estimate should be equal to the actual population whereas individual estimates can be bit more or less compared to actual value of parameter. How do calculate the mean of all estimates? Simple, it's the expectation of the estimator i.e $$E[\hat \theta]$$.

Although it should be clear that why mean of estimates is just expectation of the estimator, I will have a take on it. So, it is clear that estimator$$\hat \theta$$is just and random variable, and every random variable have some distribution associated with it, in this case distribution of estimator is called sampling distribution. Now what are estimates, the estimates are simply the point sampled from the estimator's distribution. So, mean of estimates is simply the mean of points sampled from a RV's distribution and what is the mean of points sampled from some RV's distribution? It's the mean or expectation of that RV itself. Hence, mean of estimate is mean/expectation $$E[\hat \theta]$$of the random variable $$\hat \theta$$which is our estimator. 

Bias is the tendency of a estimator to **overestimate** or **underestimate** a parameter. See [here](statistic-vs-parameter.md) to get what is difference between statistic and a parameter.  Bias is a property of the estimator. 

Mathematically, the **bias** \(or **bias function**\) of an [estimator](https://en.wikipedia.org/wiki/Estimator) is the difference between this estimator's [expected value](https://en.wikipedia.org/wiki/Expected_value) and the true value of the parameter being estimated. I.e difference between mean of estimated value from different samples and actual population parameter. Note that it's not the difference with single estimated value but with mean of different estimated values over different samples. 

Let $$\hat \theta$$ be an estimator and $$\theta$$ be an parameter or estimand. Then Bias is given by 

$$
Bias(\hat \theta) = E[\hat \theta] - \theta
$$

Note the expectation in the above formula. 

Suppose we have a [statistical model](https://en.wikipedia.org/wiki/Statistical_model), parameterized by a real number θ, giving rise to a probability distribution for observed data, ![P\_{\theta }\(x\)=P\(x\mid \theta \)](https://wikimedia.org/api/rest_v1/media/math/render/svg/cf0c92a2f9f331565f351f716b59a2d1167eebbf), and a statistic ![{\hat {\theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0eaae56d74c5844e86caeed8ae205ff9e413bba) which serves as an [estimator](https://en.wikipedia.org/wiki/Estimator) of θ based on any observed data ![x](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4). That is, we assume that our data follow some unknown distribution ![P\(x\mid \theta \)](https://wikimedia.org/api/rest_v1/media/math/render/svg/88296f80b46f26a18ff8e11652dd7ca556f2fb8c) \(where θ is a fixed constant that is part of this distribution, but is unknown\), and then we construct some estimator![{\hat {\theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0eaae56d74c5844e86caeed8ae205ff9e413bba) that maps observed data to values that we hope are close to θ. The **bias** of ![{\hat {\theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0eaae56d74c5844e86caeed8ae205ff9e413bba) relative to ![\theta ](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e5ab2664b422d53eb0c7df3b87e1360d75ad9af) is defined as![{\displaystyle \operatorname {Bias} \_{\theta }\[\,{\hat {\theta }}\,\]=\operatorname {E} \_{x\mid \theta }\[\,{\hat {\theta }}\,\]-\theta =\operatorname {E} \_{x\mid \theta }\[\,{\hat {\theta }}-\theta \,\],}](https://wikimedia.org/api/rest_v1/media/math/render/svg/82a9c6501a54260ed0edd2f03923719b9f2db906)

**where** ![{\displaystyle \operatorname {E} \_{x\mid \theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d54ff58946b27eaddcb35b7c337af8cbc4be8efa) **denotes** [**expected value**](https://en.wikipedia.org/wiki/Expected_value) **over the distribution** ![P\(x\mid \theta \)](https://wikimedia.org/api/rest_v1/media/math/render/svg/88296f80b46f26a18ff8e11652dd7ca556f2fb8c)**, i.e. averaging over all possible observations**![x](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4)**.** The second equation follows since θ is measurable with respect to the conditional distribution![P\(x\mid \theta \)](https://wikimedia.org/api/rest_v1/media/math/render/svg/88296f80b46f26a18ff8e11652dd7ca556f2fb8c).

An estimator is said to be **unbiased** if its **bias is equal to zero** for all values of parameter θ.

Ever notices why we use $$s^2 = \frac{\sum (x_i - \bar x)^2}{n-1}$$this formula as estimator for population variance and **not** $$s^2 = \frac{\sum (x_i - \bar x)^2}{n}$$, even later being the formula for population variance. There answer lies in the bias of both estimators. $$\bar x$$is sample mean \(also an estimator for population mean, hence also a random variable\). Note the in the above estimators, $$x_i$$are still random variable sampled from population distribution and not values, until they are actually observed. 

### Variance of Estimator

For an estimator we would want that very concentrated towards the actual value of parameter. Hence, and ideal estimator would be with less variance. Shouldn't need to reiterate but as estimator is a random variable, hence it will have variance. Also, having less variance means that all the estimates are very close to each other.  **One thing to note here is that, even if let's say all the estimates of estimator are very close to each other and far from actual value. Still the estimator will have low variance. Hence the variance of estimator is indicator of how much the estimates are spread among themselves and not of how much they are spread from actual value of parameter.** 

For example, variance of sample mean $$\bar x = \frac{\sum x_i}{n}$$is $$\frac {\sigma^2}{n}$$, where $$\sigma^2$$is the population variance. 

### Mean Square Error of Estimator

So, what do we have up until now? We have bias of estimator, which tells us how much mean of our estimates is far from actual value. We have variance, which tell how much estimates are spread/concentrated among themselves. 

But one important thing is still there to tell - how much out estimates are spread from actual value of parameter. This we can tell using Mean Square Error of the estimator. 

If one or more of the estimators are biased, it may be harder to choose between them. For example, one estimator may have a very small bias and a small variance, while another is unbiased but has a very large variance. In this case, you may prefer the biased estimator over the unbiased one.

 Mean square error \(MSE\) is a criterion which tries to take into account concerns about both bias and variance of estimators.

$$
MSE(\hat \theta) = E[(\hat \theta-\theta)^2]
$$

MSE measures the expected value of square of error of estimate $$\hat \theta$$ from actual value $$\theta$$. 

Let's write MSE in one more form

$$
MSE(\hat \theta) = E[(\hat \theta-\theta)^2] \\
= E[((\hat \theta-\bar\theta)-(\theta-\bar \theta))^2]\\
= E[(\hat \theta-\bar\theta)^2 + (\theta-\bar \theta)^2 -2(\hat \theta-\bar\theta)(\theta-\bar \theta) ] \\
= E[(\hat \theta-\bar\theta)^2] + E[ (\theta-\bar \theta)^2] -2E[(\hat \theta-\bar\theta)(\theta-\bar \theta)]
$$

where $$\bar \theta = E[\hat \theta]$$, is mean of the estimator. Now $$(\theta-\bar \theta)$$is constant for this expectation \(think about it, it is\). Therefore, $$E[(\theta-\bar \theta)^2] = (\theta-\bar \theta)^2$$ and $$E[(\hat \theta-\bar\theta)(\theta-\bar \theta)] = (\theta-\bar \theta)E[(\hat \theta-\bar\theta)] = 0$$because $$E[(\hat \theta-\bar\theta)] = 0$$. Hence, we get

$$
MSE(\hat \theta) = Var(\hat \theta) + (\bar \theta-\theta)^2 \\
= Var(\hat \theta) + Bias^2
$$

### Estimation Error

Imagine that we have a point estimate $$\hat \theta$$ for population parameter $$\theta$$. Even with a good point estimate, there is very likely to be some error \( $$\hat \theta$$ = θ not likely\) . We can express this error of estimation, denoted ε, as ε = \| $$\hat \theta$$ − θ\| . This is the number of units that our estimate, $$\hat \theta$$, is off from θ \(doesn’t take into account the direction of the error\).

Note that since the estimator $$\hat \theta$$ is a RV, the error $$\epsilon$$ is also random. We can use the sampling distribution of $$\hat \theta$$to help place some bounds on how big the error is likely to be. Note how much our estimation is related to mean square error. 

