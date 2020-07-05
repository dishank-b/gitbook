# Chapter 4: Optimization

## Overflow & Underflow

Underflow occurs when numbers near zero are rounded to zero. Overflow occurs when numbers with large magnitude are approximated as ∞ or −∞.

One example of a function that must be stabilized against underflow and overflow is the softmax function. The softmax function is often used to predict the probabilities associated with a multinoulli distribution. The softmax function is defined to be 

$$
softmax( x_i ) = \frac{exp(x_i) }{ \sum^n_{j=1}exp(x_j )}
$$

Consider what happens when all of the $$x_i$$ are equal to some constant $$c$$. Analytically, we can see that all of the outputs should be equal to $$1/n$$ . Numerically, this may not occur when c has large magnitude. If c is very negative, then exp\(c\) will underflow. This means the denominator of the softmax will become 0, so the final result is undefined. When c is very large and positive, $$exp(c)$$ will overflow, again resulting in the expression as a whole being undefined. Both of these difficulties can be resolved by instead evaluating softmax\(z \) where $$z = x − \max _i x_i$$ .

Simple algebra shows that the value of the softmax function is not changed analytically by adding or subtracting a scalar from the input vector. Subtracting max i x i results in the largest argument to exp being 0, which rules out the possibility of overflow. Likewise, at least one term in the denominator has a value of 1, which rules out the possibility of underflow in the denominator leading to a division by zero.

There is still one small problem. Underflow in the numerator can still cause the expression as a whole to evaluate to zero. This means that if we implement log softmax\(x\) by first running the softmax subroutine then passing the result to the log function, we could erroneously obtain −∞. Instead, we must implement a separate function that calculates log softmax in a numerically stable way.

## Jacobian

Sometimes we need to find all of the partial derivatives of a function whose input and output are both vectors. The matrix containing all such partial derivatives is known as a Jacobian matrix. Specifically, if we have a function $$\boldsymbol f : R^m → R^n$$ , then the Jacobian matrix $$\boldsymbol J ∈ R^{n × m}$$ of $$f$$ is defined such that $$J_{i,j} = \frac{∂}{∂x_j} f ( x_i )$$.

## 2nd Order Optimization

We are also sometimes interested in a derivative of a derivative. This is known as a second derivative. We can think of the second derivative as measuring **curvature**.

When our function has multiple input dimensions, there are many second derivatives. These derivatives can be collected together into a matrix called the **Hessian matrix**. The Hessian matrix $$H ( f )( x )$$ is defined such that

![](../.gitbook/assets/image%20%28161%29.png)

Equivalently, the Hessian is the Jacobian of the gradient. Anywhere that the second partial derivatives are continuous, the differential operators are commutative, i.e. their order can be swapped:

![](../.gitbook/assets/image%20%28162%29.png)

This implies that $$H_{i,j} = H_{j,i}$$ , so the Hessian matrix is symmetric at such points. Most of the functions we encounter in the context of deep learning have a symmetric Hessian almost everywhere. Because the Hessian matrix is real and symmetric, we can decompose it into a set of real eigenvalues and an orthogonal basis of eigenvectors.

Refer to the whole section of Hessian of DL book. It's quite interesting.

## Lipschitz Continuous

A lipschitz continuous function is a function $$f$$whose rate of change if bounded by a Lipschitz constant $$\mathcal L$$.

$$
\forall x, \forall y, |f(x)-f(y)|\leq \mathcal L ||x-y||_2
$$

This property is useful for it ensures that small change in input made by algorithm such as gradient descent will have small change in the output. 

## Constrained Optimization

Use Karush–Kuhn–Tucker approach for this, which is more generalized form of Lagrangian multipliers. 

