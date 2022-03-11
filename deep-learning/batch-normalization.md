# Batch Normalization

## Why Batch Normalization is considered a Regularization technique?

Regularization is something which helps prevent overfitting, how does batch-normalization do that?

### Normalization of Input Space

We know that, model is learnt better input of our model is normalized, that's the reason we always normalize our input. Normalized data gives better representation of data instead specific data points. Now that's okay for data itself. But what about in between features in layers of neural network. So basically batch-norm normalize the features gives better feature representation for the neural networks to learn weights in more general sense and bit agnostic to exact data points.&#x20;

Hence, normalization improves weight learning in sense that it makes it more general, hence batch-normalization is also regularization. It's affects weights indirectly rather directly like in dropout or weight decay.&#x20;

But the thing is what if, for some layer features need to be normalize, in that case we have `gamma` and `beta` as learnable parameters. Network learn these in order to unnormalize the normalize features according to as much needed. So on one hand, we do the normalization for more general presentation, and on the other hand we give network the ability to transform the normalized features as need to preserves it's representation ability.&#x20;

### Noise Induction Behavior

One more reason batch-norm is said to be regularization because it is said to add noise in the training - each sample appears multiple times, each time within a different batch of other samples, chosen randomly. This means that the statistics computed for the normalization of the batch containing this sample are slightly different each time, adding a form of non-determinism to the behavior of the network on this sample during training.\
Batch norm is similar to dropout in the sense that it multiplies each hidden unit by a random value at each step of training. In this case, the random value is the standard deviation of all the hidden units in the minibatch. Because different examples are randomly chosen for inclusion in the minibatch at each step, the standard deviation randomly fluctuates.\
Batch norm also subtracts a random value (the mean of the minibatch) from each hidden unit at each step.\
Both of these sources of noise mean that every layer has to learn to be robust to a lot of variation in its input, just like with dropout.\


**But it is believed that normalization of input space is more convincing reason for batch-norm to work rather than the noise inducing behavior.**&#x20;

**Advantages of Batch Normalization:**

* Normalized data makes the network bit robust of inter-distributional change.&#x20;
* Increase the learning rate
* Reduce the need for dropout and other regularization techniques.
* Achieves higher accuracy.
* Resolves the problem of covariance shift as it weakens the coupling between the initial layers parameters and later layers parameters, thus changes to the layers are independent of each other, therefore speeding the learning process of the network.

## What is Batch Normalization

{% embed url="https://www.jeremyjordan.me/batch-normalization/" %}

{% embed url="https://towardsdatascience.com/pitfalls-of-batch-norm-in-tensorflow-and-sanity-checks-for-training-networks-e86c207548c8" %}

There is debate about whether to use the Batch Norm layer before or after the activation function. Many convincing arguments are there which suggests that batch norm layer should be used after the activation function whereas in the original paper, batch norm layer is used before activation.&#x20;

{% embed url="https://www.reddit.com/r/MachineLearning/comments/67gonq/d_batch_normalization_before_or_after_relu/" %}

**During implementation many times people simply use learnable parameters of batch norm which are** $$\gamma$$**and** $$\beta$$**to be constant set as** $$1$$**and** $$0$$**respectively. Hence in this setting batch-norm only normalize the features and doesn't allow to learn it scale and shift accordingly. This generally doesn't affect very much I guess, as doing shift and scale is simple an affine transformation which we are already doing in conv layers.**&#x20;

## Theory Behind Batch Normalization

{% embed url="https://arxiv.org/abs/1805.11604" %}

{% embed url="https://myrtle.ai/learn/how-to-train-your-resnet-7-batch-norm/" %}

{% embed url="https://twitter.com/dcpage3/status/1171867587417952260" %}



## Fusing Batch-Norm parameters with Conv parameters at Run-time

{% embed url="https://tehnokv.com/posts/fusing-batchnorm-and-conv/" %}

{% embed url="https://github.com/AlexeyAB/yolo2_light/issues/5#issuecomment-422355409" %}

## Fixed or Frozen Batch-Norm during Fine-Tuning

In fine-tuning if batch size is too small to do batch norm then it can degrade the performance. Then we convert the BN layer to simple affine layer as follows

$$
\hat x = \frac{x-\mu}{\sqrt {\sigma^2 +\epsilon}} \times \gamma + \beta
$$

Where $$\mu$$and $$\sigma^2$$are estimated mean and variance during training using moving average. $$\gamma$$and $$\beta$$are learned parameters. And all these parameters can be combines to create a simple affine transform.

$$
\hat x = \gamma\times \frac{x}{\sqrt {\sigma^2 +\epsilon}}  + \beta -\frac{\mu\gamma}{\sqrt {\sigma^2 +\epsilon}}  \\ 
\\
= \gamma'x+\beta'
$$

So during fine tuning we have parameters $$\gamma'$$and $$\beta'$$whose values are $$\frac{\gamma}{\sqrt {\sigma^2 +\epsilon}}$$ and $$\beta -\frac{\mu\gamma}{\sqrt {\sigma^2 +\epsilon}}$$ respectively.&#x20;

As such, the BN layers become linear activations with constant offsets and scales ($$\beta'$$and $$\gamma'$$), and BN statistics ($$\mu$$and $$\sigma^2$$ )are not updated during fine-tuning. So this is basically a fixed layer behaving like an activation function particularly as an affine transform with parameters $$\gamma'$$and $$\beta'$$.

**NOTE: Now you don't have batch normalization here i.e there is no activation normalization with batch statistics.**&#x20;

#### Why and When to do this?

In the case when our batch statistics are not good representation of actual statistics, in this case there will be difference in testing vs training normalization as there is difference in statistics which will lead to different training and testing performance.&#x20;

So, if your fine-tuning dataset is small and different from the pre-trained dataset then your fine-tuning batch-statics may not be equal to population statistics as moving average of population statistics will be dominated by pre-trained data. Hence, in this case you simply freeze the batch-norm layer and there is no issue of statistics at all.&#x20;

**But if you have large fine-tuning dataset and if training goes for long enough then your final population statistics will same as fine-tuning dataset. In that case you may not need to freeze the batch-norm layer. Also if your fine-tune dataset is similar to pre-train dataset.**&#x20;

#### **Thing which can be done**&#x20;

Now during fine-tuning we can do one thing if we want - make $$\gamma'$$and $$\beta'$$learnable parameters which are initialized with above values instead of keeping them fixed during fine-tuning.&#x20;

## Issues with Batch Normalization

* Different parameters used to compute normalized output during training and inference
  * How are we sure that using estimated mean and variance are better than using batch mean and variance during testing. Testing and Training is only similar if batch estimates are similar to estimated (population) mean which we are gonna use at testing.&#x20;
* BN’s error increases rapidly when the batch size becomes smaller, caused by inaccurate batch statistics estimation.
  * it is required for BN to work with a sufficiently large batch size ( 32 per worker). A small batch leads to inaccurate estimation of the batch statistics, and reducing BN’s batch size increases the model error dramatically
  * They introduced group norm for this.&#x20;
* Non-i.i.d minibatches can have a detrimental effect on models with batchnorm. For e.g. in a metric learning scenario, for a minibatch of size 32, we may randomly select 16 labels then choose 2 examples for each of these labels, the examples interact at every layer and may cause model to overfit to the specific distribution of minibatches and suffer when used on individual examples.
* The pre-computed statistics may also change when the target data distribution changes. These issues lead to inconsistency at training, transferring, and testing time.\


## Caveats

{% embed url="https://www.alexirpan.com/2017/04/26/perils-batch-norm.html" %}

