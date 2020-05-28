# Problems of Bayesian Inference

### Intractable Liklihood

The Bayes theorem tells us that the computation of the posterior requires three terms: a prior, a likelihood and an evidence. The first two can be expressed easily as they are part of the assumed model \(in many situation, the prior and the likelihood are explicitly known\). However, the third term, that is a normalisation factor, requires to be computed such that

![](https://miro.medium.com/max/390/1*A5g85OCd_hFhnmL-dMnauA@2x.png)

Although in low dimension this integral can be computed without too much difficulties, **it can become intractable in higher dimensions**. In this last case, the exact computation of the posterior distribution is practically infeasible and some approximation techniques have to be used to get solutions to problems that require to know this posterior \(such as mean computation, for example\).

### Problems

Even after having the bayesian inference equation, it is many times impossible to calculate the posterior distribution because of Intractable marginal liklihood. Only if following condition holds, you can get the posterior:

* The parameter space is discrete and finite: $$\Omega = (\theta_1, \dots, \theta_p)$$ ;  in this case the marginal likelihood can be computed as a finite sum: $$f_{Y}(\mathbf{y}) = \sum_{i=1}^p f_{\mathbf{Y}|\Theta}(\mathbf{y_i}|\theta_i) f_{\Theta}(\theta_i).$$ 
  * If this condition doesn't hold true and the parameters space is continuous, then the summation becomes an integral which almost intractable to calculate and hence we can't do bayesian inference. In this condition we use **Variational Inference. In which we basically approximate the the liklihood by other model.** [**Go here for that.**](../../deep-learning/varitaional-inference.md) ****
* The prior distribution is a conjugate prior for the sampling distribution \(liklihood\). In this condition, posterior can be caluculated analytically and liklihood can also be calculated. 

