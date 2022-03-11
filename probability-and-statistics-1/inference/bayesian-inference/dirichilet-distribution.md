# Dirichlet Distribution/Process

## Dirichlet Distribution

Dirichlet distributions are commonly used as prior distributions in Bayesian statistics, and in fact the Dirichlet distribution is the conjugate prior of the categorical distribution and multinomial distribution.

The Dirichlet distribution of order K ≥ 2 with parameters α1, ..., αK > 0 has a [probability density function](https://en.wikipedia.org/wiki/Probability\_density\_function) with respect to [Lebesgue measure](https://en.wikipedia.org/wiki/Lebesgue\_measure) on the [Euclidean space](https://en.wikipedia.org/wiki/Euclidean\_space) **R**K−1 given by $${\displaystyle f\left(x_{1},\ldots ,x_{K};\alpha _{1},\ldots ,\alpha _{K}\right)={\frac {1}{\mathrm {B} ({\boldsymbol {\alpha }})}}\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}$$ where![{\displaystyle \\{x\_{k}\\}\_{k=1}^{k=K\}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/b2ca8af1aaad3b4dbc90a4c7770fa65517d96b05) belong to the standard![K-1](https://wikimedia.org/api/rest\_v1/media/math/render/svg/dd6e429474c269979f75b41db5d334243b3dccd3) [simplex](https://en.wikipedia.org/wiki/Simplex), or in other words: ![{\displaystyle \sum \_{i=1}^{K}x\_{i}=1{\mbox{ and \}}x\_{i}\geq 0{\mbox{ for all \}}i\in \[1,K\]}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/15e9f7b08d8d5bac07e921c61f2b6d5f35335a1f)

Here $$\alpha$$can be interpreted as "prior observation count". See [Pseudo-Observations](conjugate-priors.md).&#x20;

The [normalizing constant](https://en.wikipedia.org/wiki/Normalizing\_constant) is the multivariate [beta function](https://en.wikipedia.org/wiki/Beta\_function), which can be expressed in terms of the [gamma function](https://en.wikipedia.org/wiki/Gamma\_function): $${\displaystyle \mathrm {B} ({\boldsymbol {\alpha }})={\frac {\prod _{i=1}^{K}\Gamma (\alpha _{i})}{\Gamma \left(\sum _{i=1}^{K}\alpha _{i}\right)}},\qquad {\boldsymbol {\alpha }}=(\alpha _{1},\ldots ,\alpha _{K}).}$$&#x20;

### As Conjugate Prior

The Dirichlet distribution is the [conjugate prior](https://en.wikipedia.org/wiki/Conjugate\_prior) distribution of the [categorical distribution](https://en.wikipedia.org/wiki/Categorical\_distribution) (a generic [discrete probability distribution](https://en.wikipedia.org/wiki/Discrete\_probability\_distribution) with a given number of possible outcomes) and [multinomial distribution](https://en.wikipedia.org/wiki/Multinomial\_distribution) (the distribution over observed counts of each possible category in a set of categorically distributed observations). This means that if a data point has either a categorical or multinomial distribution, and the [prior distribution](https://en.wikipedia.org/wiki/Prior\_distribution) of the distribution's parameter (the vector of probabilities that generates the data point) is distributed as a Dirichlet, then the [posterior distribution](https://en.wikipedia.org/wiki/Posterior\_distribution) of the parameter is also a Dirichlet. Intuitively, in such a case, starting from what we know about the parameter prior to observing the data point, we then can update our knowledge based on the data point and end up with a new distribution of the same form as the old one. This means that we can successively update our knowledge of a parameter by incorporating new observations one at a time, without running into mathematical difficulties.

Formally, this can be expressed as follows. Given a model $${\displaystyle {\begin{array}{rcccl}{\boldsymbol {\alpha }}&=&\left(\alpha _{1},\ldots ,\alpha _{K}\right)&=&{\text{concentration hyperparameter}}\\\mathbf {p} \mid {\boldsymbol {\alpha }}&=&\left(p_{1},\ldots ,p_{K}\right)&\sim &\operatorname {Dir} (K,{\boldsymbol {\alpha }})\\\mathbb {X} \mid \mathbf {p} &=&\left(\mathbf {x} _{1},\ldots ,\mathbf {x} _{K}\right)&\sim &\operatorname {Cat} (K,\mathbf {p} )\end{array}}}$$&#x20;

then the following holds: $${\displaystyle {\begin{array}{rcccl}\mathbf {c} &=&\left(c_{1},\ldots ,c_{K}\right)&=&{\text{number of occurrences of category }}i\\\mathbf {p} \mid \mathbb {X} ,{\boldsymbol {\alpha }}&\sim &\operatorname {Dir} (K,\mathbf {c} +{\boldsymbol {\alpha }})&=&\operatorname {Dir} \left(K,c_{1}+\alpha _{1},\ldots ,c_{K}+\alpha _{K}\right)\end{array}}}$$&#x20;

This relationship is used in [Bayesian statistics](https://en.wikipedia.org/wiki/Bayesian\_statistics) to estimate the underlying parameter **p** of a [categorical distribution](https://en.wikipedia.org/wiki/Categorical\_distribution) given a collection of N samples. Intuitively, we can view the [hyperprior](https://en.wikipedia.org/wiki/Hyperprior) vector **α** as [pseudocounts](https://en.wikipedia.org/wiki/Pseudocount), i.e. as representing the number of observations in each category that we have already seen (or guessed). Then we simply add in the counts for all the new observations (the vector **c**) in order to derive the posterior distribution.

In Bayesian [mixture models](https://en.wikipedia.org/wiki/Mixture\_model) and other [hierarchical Bayesian models](https://en.wikipedia.org/wiki/Hierarchical\_Bayesian\_model) with mixture components, Dirichlet distributions are commonly used as the prior distributions for the [categorical variables](https://en.wikipedia.org/wiki/Categorical\_distribution) appearing in the models. See the section on [applications](https://en.wikipedia.org/wiki/Dirichlet\_distribution#Applications) below for more information.

### Dirichlet for Bayesian inference for Categorical/Multinomial Distribution

{% embed url="https://people.eecs.berkeley.edu/~stephentu/writeups/dirichlet-conjugate-prior.pdf" %}

{% embed url="http://blog.bogatron.net/blog/2014/02/02/visualizing-dirichlet-distributions/" %}

### Intuition of Dirichlet Distribution

Let's say you have baised die, i.e probability of every number (class) is not equal. So now we have a categorical/multinomial distribution with unknown parameters based on if you roll it once or multiple times respectively.&#x20;

Now you want to estimate the parameters of that categorical\multinomial distribution i.e what is the probability of each of the faces of die? Parameters of multinomial distribution is given as

$$
\boldsymbol{p} = [p_1, p_2, ... p_k] \text{ where  } \sum_ip_i = 1
$$

$$p_i$$denotes the the probability of output to belong to class $$i$$.&#x20;

So now how would estimate the parameters $$p_i$$which are basically of probability of class $$i$$.

**Solution:**

Roll out the dice many times, let's say 30. And denote the frequency of each of the output (classes). Let's we rolled the dice for $$n=30$$times, and we got outputs with the frequency $$\alpha_1=2, \alpha_2=4, \alpha_3=10, \alpha_4=4, \alpha_5=2, \alpha_6=8$$. Now what you think might be the value of parameter $$p_3$$, i would say $$\frac{\alpha_3}{\sum_j \alpha_j} = \frac{10}{30} = \frac{1}{3} = 0.33$$. So basically we are estimating the parameters which are Random Variable here using the simulations here. But note that $$p_3 = 0.33$$ is just an estimate i.e 0.33 is not the only value possible for $$p_3$$. Hence basically you can assocaite a probability distribution to each $$p_i$$based on $$\boldsymbol{\alpha}$$. This probability distribution of $$\boldsymbol{p}$$ based on $$\boldsymbol{\alpha}$$is nothing but the **Dirichlet Distribution.**&#x20;

And to be precise 0.33 is the mean of random variable $$p_3$$. So, for every $$i$$ we have $$E[p_i] = \frac{\alpha_i}{\sum_j \alpha_j}$$.

and the complete is distribution is given by&#x20;

$$
Dir(\boldsymbol{p}|
\alpha_1, \alpha_2,... \alpha_k) =\frac{ \Gamma (\sum_{i=1}^K \alpha_i)}{\Pi_{i=1}^K \Gamma(\alpha_i) } \Pi_{i=1}^K p_i^{\alpha_i-1}
$$

## Dirichlet Process

A Dirichlet process is a probability distribution, whose (process's) range is itself a set of probability distributions. It is often used in [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian\_inference) to describe the [prior](https://en.wikipedia.org/wiki/Prior\_probability) knowledge about the distribution of [random variables](https://en.wikipedia.org/wiki/Random\_variable)—how likely it is that the random variables are distributed according to one or another particular distribution.

The Dirichlet process is specified by a base distribution {\displaystyle H}![H](https://wikimedia.org/api/rest\_v1/media/math/render/svg/75a9edddcca2f782014371f75dca39d7e13a9c1b) and a positive [real number](https://en.wikipedia.org/wiki/Real\_number) {\displaystyle \alpha }![\alpha ](https://wikimedia.org/api/rest\_v1/media/math/render/svg/b79333175c8b3f0840bfb4ec41b8072c83ea88d3) called the concentration parameter (also known as scaling parameter). The base distribution is the [expected value](https://en.wikipedia.org/wiki/Expected\_value) of the process, i.e., the Dirichlet process draws distributions "around" the base distribution the way a [normal distribution](https://en.wikipedia.org/wiki/Normal\_distribution) draws real numbers around its mean. However, even if the base distribution is [continuous](https://en.wikipedia.org/wiki/Continuous\_distribution), the distributions drawn from the Dirichlet process are [almost surely](https://en.wikipedia.org/wiki/Almost\_surely) [discrete](https://en.wikipedia.org/wiki/Discrete\_distribution). The scaling parameter specifies how strong this discretization is: in the limit of {\displaystyle \alpha \rightarrow 0}![\alpha \rightarrow 0](https://wikimedia.org/api/rest\_v1/media/math/render/svg/1b2b1de74c597df1a88852a36f8ed46e3af14fb0), the realizations are all concentrated at a single value, while in the limit of {\displaystyle \alpha \rightarrow \infty }![\alpha \rightarrow \infty ](https://wikimedia.org/api/rest\_v1/media/math/render/svg/0337f6405bed43834d138cd765f090040bc81870) the realizations become continuous. Between the two extremes the realizations are discrete distributions with less and less concentration as {\displaystyle \alpha }![\alpha ](https://wikimedia.org/api/rest\_v1/media/math/render/svg/b79333175c8b3f0840bfb4ec41b8072c83ea88d3) increases.

The Dirichlet process can also be seen as the infinite-dimensional generalization of the [Dirichlet distribution](https://en.wikipedia.org/wiki/Dirichlet\_distribution). In the same way as the Dirichlet distribution is the [conjugate prior](https://en.wikipedia.org/wiki/Conjugate\_prior) for the [categorical distribution](https://en.wikipedia.org/wiki/Categorical\_distribution), the Dirichlet process is the conjugate prior for infinite, [nonparametric](https://en.wikipedia.org/wiki/Nonparametric\_statistics) discrete distributions. A particularly important application of Dirichlet processes is as a [prior probability](https://en.wikipedia.org/wiki/Prior\_probability) distribution in [infinite mixture models](https://en.wikipedia.org/wiki/Infinite\_mixture\_model).

{% embed url="https://www.cs.cmu.edu/~kbe/dp_tutorial.pdf" %}

## Resouces

* Detailed PDF on Dirichlet Distribution

