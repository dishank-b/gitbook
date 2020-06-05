# Batch Normalization

## Why Batch Normalization is considered a Regularization technique?

Regularization is something which helps prevent overfitting, how does batch-normalization do that?

### Normalization of Input Space

We know that, model is learnt better input of our model is normalized, that's the reason we always normalize our input. Normalized data gives better representation of data instead specific data points. Now that's okay for data itself. But what about in between features in layers of neural network. So basically batch-norm normalize the features gives better feature representation for the neural networks to learn weights in more general sense and bit agnostic to exact data points. 

Hence, normalization improves weight learning in sense that it makes it more general, hence batch-normalization is also regularization. It's affects weights indirectly rather directly like in dropout or weight decay. 

But the thing is what if, for some layer features need to be normalize, in that case we have `gamma` and `beta` as learnable parameters. Network learn these in order to unnormalize the normalize features according to as much needed. So on one hand, we do the normalization for more general presentation, and on the other hand we give network the ability to transform the normalized features as need to preserves it's representation ability. 

### Noise Induction Behavior

One more reason batch-norm is said to be regularization because it is said to add noise in the training - each sample appears multiple times, each time within a different batch of other samples, chosen randomly. This means that the statistics computed for the normalization of the batch containing this sample are slightly different each time, adding a form of non-determinism to the behavior of the network on this sample during training.  
Batch norm is similar to dropout in the sense that it multiplies each hidden unit by a random value at each step of training. In this case, the random value is the standard deviation of all the hidden units in the minibatch. Because different examples are randomly chosen for inclusion in the minibatch at each step, the standard deviation randomly fluctuates.  
Batch norm also subtracts a random value \(the mean of the minibatch\) from each hidden unit at each step.  
Both of these sources of noise mean that every layer has to learn to be robust to a lot of variation in its input, just like with dropout.  


**But it is believed that normalization of input space is more convincing reason for batch-norm to work rather than the noise inducing behavior.** 

**Advantages of Batch Normalization:**

* Normalized data makes the network bit robust of distributional change. 
* Increase the learning rate
* Reduce the need for dropout and other regularization techniques.
* Achieves higher accuracy.
* Resolves the problem of covariance shift as it weakens the coupling between the initial layers parameters and later layers parameters, thus changes to the layers are independent of each other, therefore speeding the learning process of the network.

## What is Batch Normalization

{% embed url="https://www.jeremyjordan.me/batch-normalization/" %}

{% embed url="https://towardsdatascience.com/pitfalls-of-batch-norm-in-tensorflow-and-sanity-checks-for-training-networks-e86c207548c8" %}



## Theory Behind Batch Normalization

{% embed url="https://arxiv.org/abs/1805.11604" %}

## Fusing Batch-Norm parameters with Conv parameters at Run-time

{% embed url="https://tehnokv.com/posts/fusing-batchnorm-and-conv/" %}

## Issues with Batch Normalization

* Different parameters used to compute normalized output during training and inference
  * How are we sure that using estimated mean and variance are better than using batch mean and variance during testing. Testing and Training is only similar if batch estimates are similar to estimated \(population\) mean which we are gonna use at testing. 
* Using Batch Norm with small minibatches
* Non-i.i.d minibatches can have a detrimental effect on models with batchnorm. For e.g. in a metric learning scenario, for a minibatch of size 32, we may randomly select 16 labels then choose 2 examples for each of these labels, the examples interact at every layer and may cause model to overfit to the specific distribution of minibatches and suffer when used on individual examples.
* When fine-tuning network on different data.  

## Caveats

{% embed url="https://www.alexirpan.com/2017/04/26/perils-batch-norm.html" %}



