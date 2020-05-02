---
description: Using Bayesian inference in deep learning
---

# Bayesian Deep Learning

### Bayesian Neural Network

The idea behind Bayesian Neural Network is to model the network's wights $$W$$as a distribution $$p(W|T)$$conditioned on the training data $$T$$, instead of a deterministic vairable.   
By placing a prior over the weights e.g. $$W \sim N(0,I)$$, the network training can be interpreted as determining a posterior over the weights given the training data: $$p(W|T)$$.   
However, evaluating this posterior is not tractable without approximation techniques. 

### Bayesian Inference

![](../../.gitbook/assets/image%20%28130%29.png)

### Priors in weights in NNs

We can apply this process to neural networks and come up with the probability distribution over the network weights, $$w$$ , given the training data, $$p ( w|D )$$ .

![](../../.gitbook/assets/image%20%28136%29.png)

![](../../.gitbook/assets/image%20%2828%29.png)

![](../../.gitbook/assets/image%20%2820%29.png)

![](../../.gitbook/assets/image%20%2823%29.png)

![](../../.gitbook/assets/image%20%2882%29.png)

{% file src="../../.gitbook/assets/bayesiandeeplearning.pdf" caption="Bayesian Learning of weights in NN" %}

#### Take away

When you add the **"Regularization or Weight Decay",** it simply assumes that my weights follows zero centered gaussian distribution. Hence, it is a way to incorporate a prior.  

### Resources

{% embed url="https://slideslive.com/38923183/deep-learning-with-bayesian-principles" %}

Neurips 2019 talk - **See at 19:00**, interesting

* [https://www.cs.cmu.edu/afs/cs/academic/class/15782-f06/slides/bayesian.pdf](https://www.cs.cmu.edu/afs/cs/academic/class/15782-f06/slides/bayesian.pdf)
* [https://stats.stackexchange.com/a/335422](https://stats.stackexchange.com/a/335422)

