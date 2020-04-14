# Posterior Predictive Distribution

## Posterior Predictive

Unlike classical learning algorithm, Bayesian algorithms do not attempt to identify “best-fit” models of the data \(or similarly, **make “best guess” predictions** for new test inputs\). Instead, they compute a posterior distribution over models \(or similarly, **compute posterior predictive distributions** for new test inputs\). These distributions provide a useful way to quantify our uncertainty in model estimates, and to exploit our knowledge of this uncertainty in order to make more robust predictions on new test points. Mathematically it is written as below using marginalization:

$$
p(y|\boldsymbol D) = \int_\boldsymbol\theta p(y|\boldsymbol\theta)p(\boldsymbol\theta|\boldsymbol D) d\boldsymbol\theta
$$

where $$y$$is new prediction and $$\boldsymbol D$$is the datapoints sampled from distribution with unknown parameters $$\boldsymbol\theta$$. And we estimate the posterior $$p(\boldsymbol\theta|\boldsymbol D)$$using bayesian inference as:

$$
p(\boldsymbol\theta|\boldsymbol D) = \frac{p(\boldsymbol D|\boldsymbol\theta)p(\boldsymbol\theta)}{p(\boldsymbol D)}
$$

