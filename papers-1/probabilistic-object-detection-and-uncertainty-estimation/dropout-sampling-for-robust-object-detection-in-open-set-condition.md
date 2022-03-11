---
description: Investigates dropout sampling object detection
---

# Dropout Sampling for Robust Object Detection in Open-Set Condition

### Summary

This papers shows object detection in open-set. They show that dropout sampling can be effective to reduce the false-positive for the unknown classes (those classes which were not in the training dataset) in the testing dataset.

### Methodology

#### Dropout sampling&#x20;

In this, multiple inferences are made with same input with dropout layer being active. Hence, we get multiple output for the same input. This is a variational inference technique as it helps to obtain rather intractable infereces.&#x20;

#### Bayesian Perpective

**Basic Idea:** Model the network's wights $$W$$as a distribution $$p(W|T)$$conditioned on the training data $$T$$, instead of a deterministic point estimate vairable. &#x20;

**How:**\
Placing a prior over the weights e.g. $$W \sim N(0,I)$$, the network training can be interpreted as determining a posterior over the weights given the training data: $$p(W|T)$$. However, evaluating this posterior is not tractable without approximation techniques. Where $$T$$is the training data

**See What's Bayesian here:**\
&#x20;**-** Prior: $$W \sim N(0,I)$$\
&#x20;\- Liklihood: Training of network is basically liklihood estimation\
&#x20;\- Posterior: Final trained wieght distribution  $$p(W|T)$$ is the posterior

**Approximation to Intractable Inference:**\
****Let $$I$$be the input to the network, then bayesian inference of the ouput is:

$$
p(y|I,T) = \int p(y|I,w)p(w|T)dw \approx \frac{1}{n}\sum_{i=1}^n s_i
$$

where $$n$$is the number of times the inference is done and $$s_i$$is the ouput at $$i^{th}$$inference in which $$w_i$$is used which is sampled using dropout.

**Final:**\
Then basically they use the **Entropy** of the above classification output $$p(y|I,T)$$ to threshold between the unknown and known classes. If the entropy is high, then the detected output is mostly from an outlier class.

### Insights

* Using entropy over average of output is better than single output. As aerage gives better approximation of posterior.&#x20;
