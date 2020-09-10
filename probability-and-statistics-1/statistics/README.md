# Statistics

### Random Sample

A collection of IID random variables is called a random sample. The number of random variables sampled is called size of sample. 

### Statistics

A statistic is a function of random sample or the random variables that describes the random sample in some way. For example, the sample mean, median, mode are statistics that describes the random variables. Example of statistics:  range, variance, mean, mode, median, IQ. 

Whenever we use these statics to estimate some parameter of the population from where the sample is taken we call it **Estimator.**

### Central Limit Theorem 

Sample mean follows Gaussian distribution when the sample size is large. 

**sampling distribution of the sample means** approaches a [normal distribution](https://www.statisticshowto.com/probability-and-statistics/normal-distributions/) as the [sample size](https://www.statisticshowto.com/probability-and-statistics/find-sample-size/) gets larger — _no matter what the shape of the population distribution_. This fact holds especially true for sample sizes over 30. 

### **Independent and Identically Distributed** 

A collection of [random variables](https://en.wikipedia.org/wiki/Random_variable) is **independent and identically distributed** if each random variable has the same [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution) as the others and all are mutually [independent](https://en.wikipedia.org/wiki/Independence_%28probability_theory%29). By mutually independent we mean that observation of one doesn't affect the other, they are not connected to each other in any way. In an example of dice rolls, one roll doesn't affect the future or past rolls. 

**Note: Random variables that are identically distributed don’t necessarily have to have the same probability**. A flipped coin can be modeled by a[ binomial distribution](https://www.statisticshowto.com/probability-and-statistics/binomial-theorem/binomial-distribution-formula/) and generally has a 50% chance of a heads \(or tails\). But let’s say the coin was weighted so that the probability of a heads was 49.5% and tails was 50.5%. Although the coin flips are IID, they do not have equal probabilities.Two \(real-valued\) random variables $$X$$ and $$Y$$ are _identically distributed_ if$$P(X≤x)=P(Y≤x)$$for all $$x∈R$$. 

