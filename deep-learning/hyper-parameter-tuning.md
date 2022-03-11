# Hyper-parameter Tuning

* &#x20;**Adam optimizes better & less sensitive to hyper-parameters, SGD+Momentum has better generalization. So use Adam for initial testing, and hyperparameter-sweep+SGD+Momentum for SOTA.**
* **Cyclic learning rate like cosine annealing is SOTA. Just two-stage of initial high learning rate + small learning after that also works well.**
* **BatchNorm always help in learning as well as generalization; also use L2 regularization & normalize inputs**
* **Larger batch size hurts generalization**

## Optimizer

* SGD gives better generalization as compared to Adam.&#x20;
* ADAM gives faster convergence.&#x20;

## Batch Size

* Large batch methods tends to converge in sharp minimas, and having sharp minima leads to bad generalization. 4-32 are good small batch sizes to try.&#x20;
* We can also try starting with small batch sizes and then gradually increase the batch size with training. Though this is limited as in actual implementation we set the batch\_sizw in starting, and changing during the training will be incovenience.
* **Small batch sizes may also kind a provide more exploration in loss landscape as they tend to give not so smooth gradients.**&#x20;
  * **I found this in my object detection training, that training with 4 batch size gives better accuracy than batch size 12.**

{% embed url="https://arxiv.org/abs/1609.04836" %}

{% embed url="https://arxiv.org/abs/1206.5533" %}

## Learning Rate

* Learning rate highly depends upon the loss curve. High learning rate on steep curve will not less the weights converge or even diverge.&#x20;
* Good strategy is to start with high learning rate, but keep reducing the learning rate by some factor with training.&#x20;
* Use **Learning rate scheduler. Cyclic Cosine scheduler is SOTA**
* If you are using **Adam or any other adaptive learning rate optimizer** than you may not need to use learning rate decay.&#x20;

## **Fine-Tuning**

* **When doing fine-tuning, start with lower learning rate, as your model has been trained once already and now you need to do small changes, hence use smaller learning rate.**&#x20;
* **We** know that in deep networks, deeper layers have more rich feature representations as compared to initial layers. So, when fine-tuning we may be wanting to make change the deeper layers more than initial layers. **For this, you can freeze the initial layers as they have basic representation and you may not want to change that. Or you can have learning rate of initial layers lower as compared to learning rate of later layers.**  \
  ****So this will not change the weights of initial layers much as compared to deeper layers which affects most of your task and output.&#x20;

Can use resources mentioned in this blog.&#x20;

{% embed url="https://medium.com/udacity-pytorch-challengers/ideas-on-how-to-fine-tune-a-pre-trained-model-in-pytorch-184c47185a20" %}

{% embed url="https://arxiv.org/abs/1803.09820" %}

