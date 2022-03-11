---
description: Z49+53
---

# Fine Tuning or Transfer Learning

### Freezing and Unfreezing Layers

As we know, the final set of layers (i.e., the “head”) are our fully connected layers along with our softmax classifier.

When performing fine-tuning, we actually _sever_ the head of the network, and **build a new fully connected head** and **place it on top of the original architecture** (**Figure 2**, _right_).

The new FC layer head is randomly initialized (just like any other layer in a new network) and connected to the body of the original network.

However, there is a problem:

Our CONV layers which are before fully connected layers have already learned rich, discriminative filters while our FC layers are brand new and totally random.

If we allow the gradient to backpropagate from these random values all the way through the network, we risk destroying these powerful features in the conv layers as well.&#x20;

**To circumvent this problem, we instead let our FC head “warm up” by (ironically) “freezing” all layers in the body of the network.** Training data is forward propagated through the network as we usually would; however, the backpropagation is stopped after the FC layers, which allows these layers to start to learn patterns from the highly discriminative CONV layers.\
After the FC head has started to learn patterns in our dataset, we can pause training, unfreeze the body, and continue training, _but with a very small learning rate_ — we do not want to alter our CONV filters dramatically.\


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

SO during fine tuning we can have parameters $$\gamma'$$and $$\beta'$$which can be initialized from the pre-trained parameters as $$\frac{\gamma}{\sqrt {\sigma^2 +\epsilon}}$$ and $$\beta -\frac{\mu\gamma}{\sqrt {\sigma^2 +\epsilon}}$$ respectively. Now during fine-tuning we can simply update $$\gamma'$$and $$\beta'$$using gradient descent as we optimized $$\gamma$$and $$\beta$$during pre-training.&#x20;

This removes the the dependency of calculating batch mean or variance during fine-tuning as results can be degrading if batch\_size is too small to get good batch mean and variance. Or if distribution of pre-training and fine-tuning is different, then the $$\mu$$and $$\sigma^2$$which is calculated on pre-training distribution is not good to be used with fine-tuning.&#x20;

### Image Normalization

