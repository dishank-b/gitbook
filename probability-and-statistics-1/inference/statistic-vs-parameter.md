# Estimator vs Parameter

A statistic describes samples where as Parameter describes the population. For example, $$\bar x$$ sample mean is an statics where as $$\mu$$ population mean is an parameter.&#x20;

Notice the use of different symbols to distinguish estimators(statistic) and parameters. More importantly, point estimates and parameters represent fundamentally different things.&#x20;

* Point estimates are calculated from the data; parameters are not.&#x20;
* Point estimates vary from study to study; parameters do not.
* Point estimates are random variables: parameters are constants.

Statics are estimators which are calculated based on samples to estimate some population parameter.&#x20;

### Interval Estimation

Estimators or statistics only give point estimate$$\bar x$$ of the parameter $$\theta$$. On the other hand we can also get some interval$$I$$such that we have $$P(\theta \in I)=\alpha$$, where $$\alpha$$is some threshold such as 90% or 95%. $$I$$is called **confidence interval.**

Let X be a [random sample](https://en.wikipedia.org/wiki/Random\_sample) from a [probability distribution](https://en.wikipedia.org/wiki/Probability\_distribution) with [statistical parameters](https://en.wikipedia.org/wiki/Statistical\_parameter) θ, which is a quantity to be estimated, and φ, representing quantities that are not of immediate interest. A confidence interval for the parameter θ, with confidence level or confidence coefficient γ, is an interval with random endpoints (u(X), v(X)), determined by the pair of [random variables](https://en.wikipedia.org/wiki/Random\_variable) u(X) and v(X), with the property:{\displaystyle {\Pr }\_{\theta ,\varphi }(u(X)<\theta \<v(X))=\gamma {\text{ for all \}}(\theta ,\varphi ).}![{\displaystyle {\Pr }\_{\theta ,\varphi }(u(X)<\theta \<v(X))=\gamma {\text{ for all \}}(\theta ,\varphi ).}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/e2b92b34537b69ec0cd51faeca399aa775564617)

The quantities φ in which there is no immediate interest are called [nuisance parameters](https://en.wikipedia.org/wiki/Nuisance\_parameter), as statistical theory still needs to find some way to deal with them. The number γ, with typical values close to but not greater than 1, is sometimes given in the form 1 − α (or as a percentage 100%·(1 − α)), where α is a small non-negative number, close to 0.

Here Prθ,φ indicates the probability distribution of X characterised by (θ, φ). An important part of this specification is that the random interval (u(X), v(X)) covers the unknown value θ with a high probability no matter what the true value of θ actually is.

Note that here Prθ,φ need not refer to an explicitly given parameterized family of distributions, although it often does. Just as the random variable X notionally corresponds to other possible realizations of x from the same population or from the same version of reality, the parameters (θ, φ) indicate that we need to consider other versions of reality in which the distribution of X might have different characteristics.

In a specific situation, when x is the outcome of the sample X, the interval (u(x), v(x)) is also referred to as a confidence interval for θ. Note that it is no longer possible to say that the (observed) interval (u(x), v(x)) has probability γ to contain the parameter θ. This observed interval is just one realization of all possible intervals for which the probability statement holds.

**See this link** [**https://en.wikipedia.org/wiki/Confidence\_interval**](https://en.wikipedia.org/wiki/Confidence\_interval)****

**to understand misunderstanding of confidence intervals, see the misunderstanding and example section of the page.**
