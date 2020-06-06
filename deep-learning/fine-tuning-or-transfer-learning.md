---
description: Z49+53
---

# Fine Tuning or Transfer Learning

### Batch Normalization

If fine-tuning batch size is too small to do batch norm, or data distribution changed too much from the original training set. Then we convert the BN layer to simple affine layer as follows

$$
\hat x = \frac{x-\mu}{\sqrt {\sigma^2 +\epsilon}} \times \gamma + \beta
$$

This is our batch norm equations at test time or after the training is done. Where $$\mu$$and $$\sigma^2$$are estimated mean and variance during training using moving average. $$\gamma$$and $$\beta$$are learned parameters. And all these parameters can be combines to create a simple affine transform.

$$
\hat x = \gamma\times \frac{x}{\sqrt {\sigma^2 +\epsilon}}  + \beta -\frac{\mu\gamma}{\sqrt {\sigma^2 +\epsilon}}  \\ 
\\
= \gamma'x+\beta'
$$

SO during fine tuning we can have parameters $$\gamma'$$and $$\beta'$$which can be initialized from the pre-trained parameters as $$ \frac{\gamma}{\sqrt {\sigma^2 +\epsilon}}$$ and $$\beta -\frac{\mu\gamma}{\sqrt {\sigma^2 +\epsilon}}$$ respectively. Now during fine-tuning we can simply update $$\gamma'$$and $$\beta'$$using gradient descent as we optimized $$\gamma$$and $$\beta$$during pre-training. 

This removes the the dependency of calculating batch mean or variance during fine-tuning as results can be degrading if batch\_si+

\|ze is too small to get good batch mean and variance. Or if distribution of pre-training and fine-tuning is different, then the $$\mu$$and $$\sigma^2$$which is calculated on pre-training distribution is not good to be used with fine-tuning. 

### Image Normalization



