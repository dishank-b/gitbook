---
description: >-
  This page contains deep learning techniques which might help your model to
  converge fast, get higher accuracy, decrease run time, etc.
---

# Deep learning techniques

### **Prelu \(parametric relu\):**

This is just like leaky relu, but there the parameter alpha which happens _**y = alpha\*x when x&lt;0,**_ here this parameter is learn-able, hence its value changes during training. Author of paper claim that this provide better model fitting, and can have little overfitting risk.  

```text
f(x) = alpha * x for x < 0, f(x) = x for x >= 0,
where alpha is a learned array with the same shape as x.
```

### **Merging Batch Norm with Conv:**

[http://machinethink.net/blog/object-detection-with-yolo](http://machinethink.net/blog/object-detection-with-yolo/)/

We can merge the batch norm learned params gamma and beta with convolution layer weight and baises. This  allows to remove the batch norm layer at the inference time and allowing us to get the batch norm effect with less computation.

### **Deconvolutions introduce Checkerboard Artifacts:** 

{% embed url="https://distill.pub/2016/deconv-checkerboard/" %}

This blog by colah says that those checkerboard artifacts which we usually see in GANs, and other image generation models are due to use of Deconvolutions. 

Solution includes to make sure that kernel size is divisible by stride to avoid uneven activations. But still this is not fully effetive.   
The best way for upsampling is to first resize the input layer using nearest neighbour and then using the convolution layer on that. 

### Weight Decay and L2 reguralization:

When using L2 regularization in the update of weights we get    
``w` = w - lr*(2*ƛ*w + d(loss)/dw)``

But in update rule which generally have momentum with weight decay we have . `v' = 0.9*v - lr*(0.0005*w + d(loss)/dw)` and then ``w'=w+v``` This v is for momentum .  
Now there is paper which states that weight decay work best with adam optimizer.

### DenseNet:

![DenseNet architecture](../.gitbook/assets/image.png)

  
Here, For each layer, the feature-maps of all preceding layers are used as inputs, and its own feature-maps are used as inputs into all subsequent layers.  
Advantages:

* encourage feature reuse, and substantially reduce the number of parameters.
* they alleviate the vanishing-gradient problem
* strengthen feature propagation

A possibly counter-intuitive effect of this dense connec- tivity pattern is that it requires fewer parameters than tra- ditional convolutional networks, as there is no need to re- learn redundant feature-maps.

### Modelling Network Architecture for constrained time cost

In this, it shown how we can architecture, i.e depth\(no of layers\), feature map depth, stride, etc. Such that computation time doesn't change.  Trade offs in all these factors is discussed for maintaining time cost. 

#### A general architecture of CNN:

* 1st Stage: A convolution layer with large filter size \(7x7 or 11x11\) with less number of filters with pooling. 
* 2nd: A layer with 5x5 filters.
* 3rd: A layer with 3x3 filters.

#### Time Complexity of Neural Network:

![](../.gitbook/assets/image%20%2826%29.png)

Here l is the index of a convolutional layer, and d is the depth \(number of convolutional layers\). nl is the number of filters \(also known as “width”\) in the l-th layer. nl−1 is also known as the number of input channels of the l-th layer. sl is the spatial size \(length\) of the filter. ml is the spatial size of the output feature map. 

#### Trade Offs between depth, feature maps, filter size:

[https://arxiv.org/abs/1412.1710](https://arxiv.org/abs/1412.1710) - This papers rite all the trade offs between depth , no of feature maps in a layer, kernel size, etc. It states the depth is most important factor. And you can you can increase the depth uptp some extent without having time penalty on the compensation of kernel size, no of feature maps, spatial size of featuer maps.

### One hot Encoding:

One hot encoding is a process by which categorical variables are converted into a form that could be provided to ML algorithms to do a better job in prediction.

Suppose we have K categories, then one hot vector which represents the example will have value 1 at corresponding index and 0 elsewhere. Hence, it is useful to turn the categorical data to vector.  

### K Nearest Neighbour Layer:

{% embed url="http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/\#fn3\\" %}

In this, colah proposes k nearest neighbour layer instead of softmax.   
First what he did is, he trained a classification model of MNIST using softmax and say cross entropy loss. Now at test time, he drops the softmax layer and after the final layer he uses KNN to do the classification. Basically he used the KNN in feature space of input images. This gave better performance than softmax.   
  
Now how to put KNN at train time also instead of softmax.   
From the link:

> k-NN is differentiable with respect to the representation it’s acting on, because of the 1/distance weighting. As such, we can train a network directly for k-NN classification. This can be thought of as a kind of “nearest neighbor” layer that acts as an alternative to softmax.
>
> We don’t want to feedforward our entire training set for each mini-batch because that would be very computationally expensive. I think a nice approach is to classify each element of the mini-batch based on the classes of other elements of the mini-batch, giving each one a weight of 1/\(distance from classification target\).



