# Uncertainty

[https://www.slideshare.net/samchoi7/modeling-uncertainty-in-deep-learning](https://www.slideshare.net/samchoi7/modeling-uncertainty-in-deep-learning)

## Types of Uncertainties

![](../.gitbook/assets/image%20%28141%29.png)

{% embed url="https://www.stat.berkeley.edu/~aldous/157/Papers/Fox\_Ulkumen.pdf" %}

{% embed url="http://www.stat.columbia.edu/~gelman/stuff\_for\_blog/ohagan.pdf" %}



#### 

#### 



### Dropout as a Bayesian approximation

Neural network with dropout applied before every weigth layer while training as well as testing, is mathematically equivalent to an approximation to a well known Bayesian Model.

### Bayesian Neural Network

In Bayesian Inference, we aim to **find a posterior distribution** over the random variables of our interests given a prior distribution which \(posterior\) is **intractable** in many cases.

![](../.gitbook/assets/image%20%2853%29.png)

Lets suppose that we have a posterior distribution, even in that case exact inference i.e getting output probability distribution, is very likely to be intractable as well, as it contains integral wrt the ditribution over the latent variable. See above. Like you may get a point estimate but getting the whole probability distribution is likely to be intractbale. 

![](../.gitbook/assets/image%20%2841%29.png)

### Varitional Inference

Following the above, variational inference is used to approximate the \(intractable\) posterior distribution with \(tractable\) varitional distribution with respect to the KL divergence. 

![](../.gitbook/assets/image%20%2889%29.png)

Minimizing the KL divergence is equivalent to maximizing the evidence lower bound **\(ELBO\)** which also contains the integral with respect to the distribuiton over latent variables.

![](../.gitbook/assets/image%20%2849%29.png)

Here instead of posterior distribution we only need an liklihood, as can be seen above, to compute the ELBO.   
  
Here we do the reparametrization now

![](../.gitbook/assets/image%20%2873%29.png)

