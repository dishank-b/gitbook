---
description: >-
  This discuss about effect of numbers of neurons in a layer and number of
  layers for training a network
---

# Dimensionality of Layer Vs Number of Layers

Link : [http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/](http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)\
&#x20;         [https://cs.stanford.edu/people/karpathy/convnetjs//demo/classify2d.html](https://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html)

In networks, hidden layers change the representation of input such that transformed data becomes easy to classify. With each layer, the network transforms the data, creating a new _representation_.These representations, hopefully, make the data “nicer” for the network to classify. Above links demonstrate representation of data in each layer.&#x20;

Basically, each layer consists of an affine transformation( $$Wx+b$$ ) followed by pointwise application of a monotone activation function(tanh or sigmoid).

### Dimensions Vs NonLinearity:

![](http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/img/topology\_base.png)AA is red, BB is blue

Consider a two dimensional dataset with two classes A,B⊂ℝ2A,B⊂R2:

A={x|d(x,0)<1/3}A={x|d(x,0)<1/3}

B={x|2/3\<d(x,0)<1}\
\
**Claim**: It is impossible for a neural network to classify this dataset without having a layer that has 3 or more hidden units, regardless of number of layers in the network.\
\
Number of neurons in layers decides the dimension in which we want to transform our data. i.e. having three unit means that data will we transformed and represented in three dimensions.

![](<../.gitbook/assets/image (46).png>)

Now even we have 100 layers but all only 2 hidden neurons in each than network will not be able to classify the data, as it is not possible to separate the data in 2D. \
With only two hidden units, a network is topologically incapable of separating the data in this way, and doomed to failure on this dataset.

Now to separate this kind of data, one has to transform this in 3D, only then it can be separated. To represent this in 3D, one should have 3 neurons in a hidden layer.&#x20;

![Transformation of original data in 3D](<../.gitbook/assets/image (76).png>)

### Conclusion:

Number of neurons defines the dimension of representation of data. And number of layer defines the non-linearity in the network. You should have enough dimensions for data to being able to classified. &#x20;
