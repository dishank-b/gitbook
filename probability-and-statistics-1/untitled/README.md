---
description: Notes on Statistics
---

# Statistics

### Law of Large Numbers <a id="standard-deviation-vs-standard-error"></a>

When samples from data becomes large then sample mean would tend to population mean. But this only holds when variance is finite, which is usually the case.

### Central Limit Theorem

**The mean always follow normal distribtuion, even if population doesn't.** 

**The d**istribution of sample means for an independent random variable, wll get closer to a normal distribution as the size of samples grow bigger and bigger, even if the original population distribution isn't normal itself. 

\*\*\*\*[**https://youtu.be/rBjft49MAO8?list=PL8dPuuaLjXtNM\_Y-bUAhblSAdWRnmBUcr**](https://youtu.be/rBjft49MAO8?list=PL8dPuuaLjXtNM_Y-bUAhblSAdWRnmBUcr) **- This video explain how central limit theorem works and sample mean distribution will always be normal even if population distribution isn't.**

**PROOF of CLT???????????????????**

### Standard Deviation Vs Standard Error <a id="standard-deviation-vs-standard-error"></a>

​[https://keydifferences.com/difference-between-standard-deviation-and-standard-error.html](https://keydifferences.com/difference-between-standard-deviation-and-standard-error.html) [https://youtu.be/A82brFpdr9g](https://youtu.be/A82brFpdr9g)​

**Standard Deviation:** Measures the amount of variability or dispersion for a subject set of data from the mean. It gives the deviation in the population itself from the mean of population. 

**Standard Error:** It is used to measure the statistical accuracy of an estimate. It is primarily used in the process of testing hypothesis and estimating interval. For ex: **Standard Error of Mean:** Measures how far the sample mean of the data is likely to be from the true population mean. You might have observed that different samples batches, with identical size, drawn from the same population, will give diverse values of statistic under consideration, i.e. sample mean. Standard Error \(SE\) provides, the standard deviation in different values of the sample mean. It is used to make a comparison between sample means across the populations.​  

$$
SE = \frac{SD}{\sqrt{N}} \; \; \; \;\;\; N \; is \; the \; sample \; size
$$

### Standard Deviation <a id="standard-deviation"></a>

1 SD covers 68.2% of data. 2 SD covers about 95% of data.

### Law of Iterative Expectation or Law of Total Expectation:

$$
E_Y[E[X|Y]] = \sum_{y\in Y}E[X|Y=y]P_Y(y) = \sum_{y\in Y}\left(\sum_{x\in X}xP_X(x|Y=y)\right)P_Y(y)\\ = \sum_{x\in X}x\left(\sum_{y\in Y}P_X(x|Y=y)P_Y(y)\right) =\sum_{x\in X}xP_X(x)\\ = E[X]
$$

### Maximum Liklihood Estimate

Suppose we want to find an distribution to explain some data. Assume we choose normal distribution to explain the data and to a normal distribution have two params: mean and variance. Now we have to find best mean and variance for normal distribution so that they can explain the data well i.e reducing the KL divergence.   
  
SO we will choose mean such that the liklihood of data given that mean must be maximum. SO when a mean choosen maximizing the liklihood of data it is called maximum liklihood estimate of mean.   
  
Similarly, if any parameter is choosen to explain tha given data and found out such that maximizing the liklihood, it is called maximum liklihood estimate.   


Let's talk mathmatics:

$$
\theta^* = \max_\theta  P(\theta|data) \\
 = \max_\theta \frac{P(data|\theta)P(\theta)}{P(data)}
$$

Here $$P(\theta|data)$$ is called posterior, $$P(data|\theta)$$ is liklihood as this shows the liklihood of observing the data given the $$\theta$$ and $$P(\theta)$$ is called prior. It shows the what is probability of having some particular $$\theta$$ , generally $$P(\theta)$$ is uniform ,showing that all values of $$\theta$$ are equally likely and we does't favour any value. 

Now $$P(data)$$ doesnt depend upon on $$\theta$$and $$P(\theta)$$ is already uniform. Therefore

$$
\theta^* = \max_\theta P(data| \theta)
$$

Hecne when we find $$\theta$$ using above formula in which the chosen $$\theta$$, maximize the liklihood of data, it is called maximizing liklihood estimation. 

