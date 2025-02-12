---
description: Different optimizers used in deep learning
---

# Optimizers

## Second Order Optimization&#x20;

Here second order derivatives called **Hessian** are used to optimize.&#x20;

**Note:** Only works when Hessian is positive everywhere i.e f(x) is convex i.e. it is convex optimization problem.&#x20;

Second order derivatives are said to better optimizer as they don't settle in saddle points.&#x20;

Ex:\
&#x20;• Newton

• Gauss-Newton

• Quasi-Newton

• BFGS, (L)BFGS

## Deep Learning Optimizers&#x20;

### Stochastic Gradient Descent

### Momentum

![Screenshot from 2017-05-08 19:29:28.png](https://lh3.googleusercontent.com/rMkf_NXeamSdnTQ1QDMFQ62CgHBq27OtbftWfc4wdpnXrCvDWjGosgeJMrvy9nYo97zfbKvoJnxL3YfwZu4fz17uRsUABB-6SgPOSPyg5PXveuMTkPAWlREfL770bLIOe3OafGwN)

### Nesterov accelerated gradient

![Screenshot from 2017-05-08 20:43:37.png](https://lh6.googleusercontent.com/BjPLQctJwuZeDadzLykAB9lJn0EYVmdkPTXzoOAfVow6LAj4Gb7klB_mTzkJNZvo6p69Jf-R2UPTZfxtJNhNz7U5wk7p42FCR7lqJUPagy1aZTvrzfB6dvdnLGO_Qfb2u-8kChkB)

### AdaGrad

Adaptive learning rate for each parameter according to its past gradient history. Parameters with less past gradients have high learning rate.&#x20;

![Screenshot from 2017-05-09 17:07:33.png](https://lh5.googleusercontent.com/7aj3XQ7SxottCicrIg0gCf9Unhcolys5UEKGKbEsnUV4EFcc8masxrtm4bcUXwvazgID70ggQeftrA-l7KD2bd_SMzz5WmwwLy0gm3orynOeOITQ_abJaKKybrq4W4IKrTIiX46T)

### Adadelta

![](<../.gitbook/assets/image (33).png>)



* &#x20;is an extension of Adagrad and it also tries to reduce Adagrad’s aggressive, monotonically reducing the learning rate
* It does this by **restricting the window of the past accumulated gradient to some fixed size of w. Running average at time&#x20;**_**t**_**&#x20;then depends on the previous average and the current gradient**

### RMSProp

* RMSProp tries to resolve Adagrad’s radically diminishing learning rates by **using a moving average of the squared gradient**. It utilizes the magnitude of the recent gradient descents to normalize the gradient.
* RMSProp divides the learning rate by the average of the exponential decay of squared gradients

![](<../.gitbook/assets/image (36).png>)

### Adam

{% embed url="https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c" %}



* Another method that **calculates the individual adaptive learning rate for each parameter from estimates of first and second moments of the gradients.**
* It also reduces the radically diminishing learning rates of Adagrad
* Adam can be viewed as a **combination of Adagrad, which works well on sparse gradients and RMSprop which works well in online and nonstationary settings**.
* **Adam implements the exponential moving average of the gradients to scale the learning rate instead of a simple average as in Adagrad. It keeps an exponentially decaying average of past gradients**
* Adam is computationally efficient and has very little memory requirement
* **Adam optimizer is one of the most popular gradient descent optimization algorithms**

![](<../.gitbook/assets/image (66).png>)

![](<../.gitbook/assets/image (140).png>)

![](<../.gitbook/assets/image (61).png>)

## Learning Rate Scheduler&#x20;

Learning Rate Scheduler works, if your loss is reaching plateau let's say after 20 epochs, then make sure to reduce the learning rate at epoch 20 and check the training then. See an example below.

![Loss curve for some training](<../.gitbook/assets/image (12).png>)

In the experiments done, which is shown by above loss curve, `learning rate` was decreased by factor of 0.5 at epoch 20 and 30. See how loss was saturated at epoch 20 but after reducing the learning rate the loss started decreasing and same behavior at epoch 30. See sort of spikes at epoch 20 and 30.

**NOTE:** Training with low learning rate in last times of training can lead to over-fitting as compared to training with high learning rate. Because small learning rate makes very small changes in weights which might be tuning the weights for training data only. On the other hand larger learning rate wouldn't let the network reach it optimal error. Hence should maintain a balance for training with smaller learning rate in last of the training. In the nutshell, don't train with small learning rate for more than what is require for optimal convergence.&#x20;
