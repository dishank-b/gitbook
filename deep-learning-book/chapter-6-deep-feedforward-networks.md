---
description: Deep neural networks starts here
---

# Chapter 6: Deep FeedForward Networks

### Affine Transformation - 

In geometry, an affine transformation, affine map\[1\] or an affinity is a function between affine spaces which **preserves points, straight lines and planes**. Also, sets of **parallel lines remain parallel after an affine transformation**. An affine transformation does not necessarily preserve angles between lines or distances between points, though it does **preserve ratios of distances between points lying on a straight line**.  
        If **X** and **Y**  are affine spaces, then every affine transformation **f : X → Y**  is of the form **x ↦ M x + b**, where _**M**_  is a linear transformation on **X** and **b** is a vector in **Y.**  
                      Unlike a purely linear transformation, an **affine map need not preserve the zero point in a linear space**. Thus, every linear transformation is affine, but not every affine transformation is linear.  
For real numbers, the map **x ↦ x + 1 is not linear** \(but is an **affine transformation; y = x + 1** is a linear equation, as the term is used in analytic geometry.\)

#### Properties preserved:

* collinearity
* Parallelism
* convexity
* ratios of length

### Adding a Hidden Layer:

When you add a hideen layer, you are doing an affine transformation followed by a non-linearization. Now in the new space generated often called feature space, it is possible to use a linear model which was not possible before affine+non-linear transformation. 

### Cost Function:

If you know model of P\(y\|x\), then -log P\(y\|x\) can be consider as loss function for a neural network to learn the model.  


