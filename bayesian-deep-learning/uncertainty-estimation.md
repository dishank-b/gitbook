# Uncertainty

[https://www.slideshare.net/samchoi7/modeling-uncertainty-in-deep-learning](https://www.slideshare.net/samchoi7/modeling-uncertainty-in-deep-learning)

## Types of Uncertainties

![](<../.gitbook/assets/image (141).png>)

{% embed url="https://www.stat.berkeley.edu/~aldous/157/Papers/Fox_Ulkumen.pdf" %}

{% embed url="http://www.stat.columbia.edu/~gelman/stuff_for_blog/ohagan.pdf" %}

### Bayesian Neural Network

In Bayesian Inference, we aim to **find a posterior distribution** over the random variables of our interests given a prior distribution which (posterior) is **intractable** in many cases.

![](<../.gitbook/assets/image (53).png>)

Lets suppose that we have a posterior distribution, even in that case exact inference i.e getting output probability distribution, is very likely to be intractable as well, as it contains integral wrt the ditribution over the latent variable. See above. Like you may get a point estimate but getting the whole probability distribution is likely to be intractbale.&#x20;

![](<../.gitbook/assets/image (41).png>)

### Varitional Inference

Following the above, variational inference is used to approximate the (intractable) posterior distribution with (tractable) variational distribution with respect to the KL divergence.&#x20;

![](<../.gitbook/assets/image (89).png>)

Minimizing the KL divergence is equivalent to maximizing the evidence lower bound **(ELBO)** which also contains the integral with respect to the distribuiton over latent variables.

![](<../.gitbook/assets/image (49).png>)

Here instead of posterior distribution we only need an liklihood, as can be seen above, to compute the ELBO. \
\
Here we do the reparametrization now

![](<../.gitbook/assets/image (73).png>)
