# Probability

## Notation

* Uppercase $$X$$ denotes a random variable
* Uppercase $$P(X)$$ denotes the probability distribution over that variable
* Lowercase $$x∼P(X)$$ denotes a value $$x$$ sampled \(∼\) from the probability distribution $$P(X)$$ via some generative process.
* Lowercase $$p(X)$$ is the density function of the distribution of $$X$$. It is a scalar function over the measure space of $$X$$.
* $$p(X=x)$$\(shorthand $$p(x)$$\) denotes the density function evaluated at a particular value x. 

## Summary

{% embed url="https://static1.squarespace.com/static/54bf3241e4b0f0d81bf7ff36/t/55e9494fe4b011aed10e48e5/1441352015658/probability\_cheatsheet.pdf" %}

## What Is Probability

Let’s suppose I want to bet on a soccer game between two teams of robots, **Arduino Arsenal** and **C Milan**. After thinking about it, I decide that there is an 80% probability that **Arduino Arsenal** winning. What do I mean by that? Here are three possibilities…

* They’re robot teams, so I can make them play over and over again, and if I did that, **Arduino Arsenal** would win 8 out of every 10 games on average.
* For any given game, I would only agree that betting on this game is only “fair” if a $1 bet on **C Milan** gives a $5 payoff \(i.e. I get my $1 back plus a $4 reward for being correct\), as would a $4 bet on **Arduino Arsenal** \(i.e., my $4 bet plus a $1 reward\).
* My subjective “belief” or “confidence” in an **Arduino Arsenal** victory is four times as strong as my belief in a **C Milan** victory.

### The Frequentist View

It defines probability as a _long-run frequency_. Suppose we were to try flipping a fair coin, over and over again. By definition, this is a coin that has $$P(H)=0.5$$. What might we observe? It basically defines probability in term of the frequency of happening of event. In this case, number of times we get Heads si the probability of Head. 

The frequentist definition of probability has some desirable characteristics. First, it is objective: the probability of an event is **necessarily** grounded in the world. The only way that probability statements can make sense is if they refer to \(a sequence of\) events that occur in the physical universe. Second, it is unambiguous: any two people watching the same sequence of events unfold, trying to calculate the probability of an event, must inevitably come up with the same answer.

The frequentist definition has a narrow scope. There are lots of things out there that human beings are happy to assign probability to in everyday language, but cannot \(even in theory\) be mapped onto a hypothetical sequence of events. For instance, if a meteorologist comes on TV and says, “the probability of rain in Adelaide on 2 November 2048 is 60%” we humans are happy to accept this. But it’s not clear how to define this in frequentist terms. There’s only one city of Adelaide, and only 2 November 2048. There’s no infinite sequence of events here, just a once-off thing. Frequentist probability genuinely **forbids** us from making probability statements about a single event.

### The Bayesian View

**Bayesian view** of probability is often called the subjectivist view. The most common way of thinking about subjective probability is to define the probability of an event as the **degree of belief** that an intelligent and rational agent assigns to that truth of that event. 

However, in order for this approach to work, we need some way of operationalising “degree of belief”. One way that you can do this is to formalise it in terms of “rational gambling”, though there are many other ways. Suppose that I believe that there’s a 60% probability of rain tomorrow. If someone offers me a bet: if it rains tomorrow, then I win $5, but if it doesn’t rain then I lose $5. Clearly, from my perspective, this is a pretty good bet. On the other hand, if I think that the probability of rain is only 40%, then it’s a bad bet to take.

The main advantage is that it allows you to assign probabilities to any event you want to. You don’t need to be limited to those events that are repeatable. The main disadvantage \(to many people\) is that we can’t be purely objective – specifying a probability requires us to specify an entity that has the relevant degree of belief. This entity might be a human, an alien, a robot, or even a statistician, but there has to be an intelligent agent out there that believes in things. To many people this is uncomfortable: it seems to make probability arbitrary. While the Bayesian approach does require that the agent in question be rational \(i.e., obey the rules of probability\), it does allow everyone to have their own beliefs; I can believe the coin is fair and you don’t have to, even though we’re both rational.

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

