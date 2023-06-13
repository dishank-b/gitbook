---
description: L1 vs L2
---

# Regularization

## From the perspective of constraint

We should the regularization terms in the loss function as a lagrange multiplier term in the lagrange technique where regularization term is basically the constraint from the perspective of lagrange method. And there is difference between L1 and L2 constraint curves as shown in the article below, L2 constraint curve is basically a circle while L1 has different curve equation.&#x20;

{% embed url="https://waterprogramming.wordpress.com/2017/02/22/dealing-with-multicollinearity-a-brief-overview-and-introduction-to-tolerant-methods/" %}

{% embed url="https://datascience.stackexchange.com/questions/39613/regularization-in-simple-math-explained" %}

{% embed url="https://explained.ai/regularization/L1vsL2.html" %}

## From the perspective of gradient penalty

The gradient of L1 terms is always $$1$$, irrespective of the value/magnitude of weight. Hence there will always of gradient penalty in the total loss, leading to smaller values of weight i.e leading to 0 unless the actually loss function take the weight to the value where the loss is minimized. hence  weights corresponding to the features that doesn't influence output will be naturally settle at zero. Whereas, for L2 regularization, the gradient penalty depends upon of the value of the weight. Hence, the gradient penalty goes down as the weight goes down, hence for smaller weights the gradient penalty of L2 regularization is less than L1. Hence, L2 regularization doesn't take weights all the way to 0.

{% embed url="https://explained.ai/regularization/L1vsL2.html" %}

{% embed url="https://satishkumarmoparthi.medium.com/why-l1-norm-creates-sparsity-compared-with-l2-norm-3c6fa9c607f4" %}

