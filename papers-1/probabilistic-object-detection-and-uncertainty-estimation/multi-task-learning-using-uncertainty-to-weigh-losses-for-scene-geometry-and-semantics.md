---
description: >-
  How uncertainty is used to weigh different losses in task where multiple
  losses are used.
---

# Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics

### Summary

They learn the task uncertainty \(homoscedastic uncertainty\), they use this uncertainty to wight the losses of different tasks. So when we have a training which have mutiple losses such as $$ L = \sum_i L_iw_i $$, then $$w_i$$is is not a hyperparameter here like traditional methods but is learnable uncertainty. They show this in the network where they jointy learn semantic segmentation and depth regression, hence classification and regression task. 

### Methodolgy

![Pipeline of the work](../../.gitbook/assets/image%20%2837%29.png)

When we learn multiple output of network such as in this case. The outputs have different units and dimensions, this raises a problem to asign different weights to different losses of outputs. 

**Homoscedastic Uncertainty:** It is an aleatoric uncertainty which is not dependent on the input data. It is not a model output, rather a quantity which stays constant for all input data and varies between different tasks.

#### Deriving losses using liklihood

Let $$f_W (x)$$ be the output of a neural network with weights $$W$$ on input $$x$$.  
For regrassion tasks, we define our  liklihood as a Gaussian with mean as model output:

$$
p(y|f _W (x)) = \mathcal{N} (f_W (x), σ^2 )
$$

where this $$\sigma^2$$ is the observation noise \(also task uncertainty in this case\). When we use maximize the liklihood for this, we get:

$$
log p(y|f_W (x)) ∝ \frac{−
1}{2\sigma^2}
||y − f ^W (x)||^ 2 − \log σ
$$

For classification we often squash the model output through a softmax function, and sample from the resulting probability vector:

$$
p(y|f_W (x)) = Softmax(f_W (x))
$$

Here the classification liklihood they squash the scaled version of the model output through a softmax function:

$$
p(y|f^W (x), σ) = Softmax(
\frac{1}{\sigma^2}
f^W (x))
$$

This can be interpreted as a Boltz- mann distribution \(also called Gibbs distribution\) where the input is scaled by σ 2 \(often referred to as temperature\). The log liklihood of this is given as 

$$
\log p(y = c|f^ W (x), σ) = \frac{1}{\sigma^2}
f_c ^W(x) - \log \sum_{c^`}\exp(\frac{1}{\sigma^2}
f_{c`} ^W(x))
$$

with $$f_c ^W (x)$$ the $$c’$$th element of the vector $$f^W(x)$$

Now let $$y_1, y_2$$be the model outputs corresponding to regression and classification, then:

$$
p(y _1 , y _2 |f_ W (x)) = p(y _1 |f_ W (x)) · p(y_2 |f_ W (x))
$$

The loss for this will the negative log liklihood of above which is given by:

$$
L(W, σ_1 , σ_2 ) = -\log p(y _1 , y _2=c |f_ W (x)) \\
= − \log \mathcal{N} (y_1 ; f^ W (x), σ_1 ^2 ) · Softmax(y_ 2 = c; f ^W (x), σ _2 ) \\
\approx \frac{1}{2\sigma_1^2}L_1(w) + \frac{1}{2\sigma_2^2}L_2(w) + \log \sigma_1 + \log \sigma_2
$$

where $$L_1 (W) = ||y_ 1 − f^ W (x)||^ 2$$ for the euclidean loss of $$y_1$$ and $$ L_2 (W) = − \log Softmax(y_2 , f^ W (x)) $$. 

Hence, here we mathematically derived the multi task loss using task uncertainty for each task. Using this loss formulation of classification and regression, you extend it to any of the multitask loss. 

### Insights/Discussions

* Using uncertainty for weighing the losses allows us to incorporate the problem for different dimension and units for different tasks in a multi task learning problem. 
* The unceratiainty are learnable parameters and does not depend on input but the task itself. 
* Looking logically, if the output of task is more spreaded i.e has larger units, then $$\sigma$$will be high. Hence normalizing the loss. Using $$\sigma$$basically normalize the loss and helps getting rid of units in the equation. 





