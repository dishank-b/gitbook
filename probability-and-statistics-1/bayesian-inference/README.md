---
description: Notes on Bayesian Inference
---

# Bayesian Inference

Bayesian inference refers to [statistical inference](https://en.wikipedia.org/wiki/Statistical_inference) where uncertainty in inferences is quantified using probability. In classical [frequentist inference](https://en.wikipedia.org/wiki/Frequentist_inference), model [parameters](https://en.wikipedia.org/wiki/Parameter) and hypotheses are considered to be fixed. Probabilities are not assigned to parameters or hypotheses in frequentist inference. For example, it would not make sense in frequentist inference to directly assign a probability to an event that can only happen once, such as the result of the next flip of a fair coin. However, it would make sense to state that the proportion of heads [approaches one-half](https://en.wikipedia.org/wiki/Law_of_large_numbers) as the number of coin flips increases.[\[7\]](https://en.wikipedia.org/wiki/Bayesian_statistics#cite_note-wakefield2013-7)

[Statistical models](https://en.wikipedia.org/wiki/Statistical_models) specify a set of statistical assumptions and processes that represent how the sample data is generated. Statistical models have a number of parameters that can be modified. For example, a coin can be represented as samples from a [Bernoulli distribution](https://en.wikipedia.org/wiki/Bernoulli_distribution), which models two possible outcomes. The Bernoulli distribution has a single parameter equal to the probability of one outcome, which in most cases is the probability of landing on heads. Devising a good model for the data is central in Bayesian inference. In most cases, models only approximate the true process, and may not take into account certain factors influencing the data.[\[1\]](https://en.wikipedia.org/wiki/Bayesian_statistics#cite_note-bda-1) I**n Bayesian inference, probabilities can be assigned to model parameters. Parameters can be represented as** [**random variables**](https://en.wikipedia.org/wiki/Random_variable)**. Bayesian inference uses Bayes' theorem to update probabilities after more evidence is obtained or known.**[\[1\]](https://en.wikipedia.org/wiki/Bayesian_statistics#cite_note-bda-1)[\[8\]](https://en.wikipedia.org/wiki/Bayesian_statistics#cite_note-congdon2014-8)

## What is Bayesian Inference?

Bayesian inference is about inferring the distribution of some random variable of event $$A$$given the other event $$B$$. As follows. 

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

This is normal way of seeing Bayes Theorem for two events. Now let us see it in terms of hypothesis \(belief\) and observed data.

$$
P(h|D) = \frac{P(D|h)P(h)}{P(D)}
$$

where $$h$$ denotes a _**hypothesis**_ and $$D$$ denotes _**observed data.**_ Hence using this Bayes theorem we want to find the distribution of hypothesis given the _**observed data** i.e probability of different hypothesis being true given the data._ 

**Explanation:** Here $$P(h)$$ is our **prior or prior belief** about some statistic, then we have $$P(D|h)$$which is called **likelihood** and represents observing some actual data given the hypothesis, also called sampling distribution for this reason. After this we get our $$P(h|D)$$ called **posterior** and this represents our updated believe about the statistic after observing the data $$\boldsymbol{D}$$ **.   
Note:** Here $$\boldsymbol{P(D)}$$ denoted the distribution of data. Now as $$\boldsymbol{P(D)}$$ doesn't depend upon $$\boldsymbol{h}$$ , it does not provide any information to update the hypothesis.   
  
__[https://youtu.be/5NMxiOGL39M](https://youtu.be/5NMxiOGL39M) - Make sure to understand the graph shown between 16:50-19:13  
In this videos after 19:20 he tells about how to use **prior** $$\boldsymbol{P(h)}$$ which will finally affect the calculation of $$\boldsymbol{P(h|D)}$$ .

## Bayesian vs Non-Bayesian Estimates 

Generally when using maximum likelihood estimate we assume uniform prior i.e we do not assume any belief about **hypothesis** $$\boldsymbol{h}$$ , means we assume that all hypothesis in the hypothesis space are equally likely . When we assume uniform prior then most likely $$\boldsymbol{h}$$ found using bayes theorem is called maximum likelihood estimate and this method is called maximum likelihood estimation because to get the posterior we use the likelihood and choose the $$\boldsymbol{h}$$ for which likelihood is maximum. When using **MLE is a non-bayesian estimate** as it doesn't make use of any prior. 

But many times we can have some bias for specific hypothesis i.e have some prior, like knowing that value of hypothesis will always be in some range $$[a,b]$$ means $$P(h<a) = 0 \; \; and \; \; P(h>b) = 0 $$ . When we use the prior and doesn't assume it to be uniform, then we use both likelihood and prior to choose the hypothesis $$\boldsymbol{h}$$ , we call it **Maximum A Posteriori \(MAP\). This is called Bayesian Estimate.** 

**Bayesian Estimate** are more narrower than non-bayesian due to use of prior which makes distribution more confined. And generally give more closer and accurate distribution. Using beliefs allows us to get more confident answer.   
But sometimes using bayesian can be wrong, like what if you have wrong prior i.e you said some values are impossible then bayesian estimate will not consider those values, but may be those value are possible and should not have probability **zero.**   

![](../../.gitbook/assets/image%20%28100%29.png)

**Note:** Lets say you are using bayesian inference, but your prior ininformative i.e. it is uniform or doesn't really favour any prior parameter/hypothesis. Then does bayesian inference is any better than non-bayesian estimation? So baiscally, it seems that bayesian inference is only useful when you actually have some prior information, and using ininformative prior is not of any good. 

**Baye's Factor:** The amount of information we learned about the hypothesis using the data observed. 

We can use Baye's factor to tell which hypothesis is more likely to to be true given the data.   
[https://youtu.be/9TDjifpGj-k?list=PL8dPuuaLjXtNM\_Y-bUAhblSAdWRnmBUcr](https://youtu.be/9TDjifpGj-k?list=PL8dPuuaLjXtNM_Y-bUAhblSAdWRnmBUcr)

## Bayesian Inference for Parameters given Data

Instead of $$h$$, you can have $$\boldsymbol \theta$$which is basically parameter vector of some model/distribution which you think might have generated the data $$D$$. So we basically get

$$
p(\theta|D) = \frac{p(D|\theta)p(\theta)}{p(D)}
$$

Let's say you have $$D= \{y_1, y_2, .. y_n\}$$, this data is generated by some model/distribution whose parameters you don't know. But you generally make an assumption about the family of distriubiton from  which the data might have been sampled, like is it sampled from gaussian distribution or piosson distribution. In case of gaussian, $$\theta = [\mu, \sigma]$$will be your unknown parameters. 

Now your **parameter** $$\theta$$**is a random variable** whose distribution you want to estimate given the data $$D$$, which you can do using above bayesian inference equation.   
$$p(\theta)$$is the prior distribution i.e. your previous belief about the random variable $$\theta$$before seeing the data $$D$$. 

$$p(D|\theta)$$is your liklihood, because it tells about the liklhood of observing data given parameters $$\theta$$. One think to note here is that this liklihood is not a pdf and only an function of $$\theta$$ . It is not an pdf in the sense because in $$p(D|\theta)$$ your $$D$$is not any random variable. See [this](../) for more on this. But still, the value of $$p(D|\theta)$$gives you the liklihood \(probability\) of observing $$D$$as a function of $$\theta$$. Considering $$y_i$$as iid, we can write

$$
p(D|\theta) = \Pi_{i=1}^n p(y_i|\theta)
$$

Why I said, that above is not an pdf but only liklihood is because $$y_i$$is not random variable but $$\theta$$is. You just calculate the liklihood of $$y_i$$. 

### Calculating posterior as weighted average of priors

Let's look at an interesting take to understand posterior 

![](../../.gitbook/assets/image%20%2850%29.png)

So basically, here you have some priors already which you think can explain your data. Now instead of choosign one prior which is case of point-based estimation, you assign a score to each prior which basically denotes how liklely that prior is or what is the probability of that prior is. And this score is nothing but the liklihood calcualted using the prior. Now to make it into probability Distribution, you normalise it. 

### How to use Bayesian Learning principles in Deep Learning?

{% embed url="https://slideslive.com/38923183/deep-learning-with-bayesian-principles" %}



## Resources

* [https://brohrer.github.io/how\_bayesian\_inference\_works.html](https://brohrer.github.io/how_bayesian_inference_works.html)

{% file src="../../.gitbook/assets/how-bayesian-inference-works.pdf" caption="Slides for the Video" %}

* [https://vioshyvo.github.io/Bayesian\_inference/index.html](https://vioshyvo.github.io/Bayesian_inference/index.html) - Complete Bayesian Inference Notes. 



### 

