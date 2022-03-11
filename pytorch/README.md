# Pytorch

[https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e](https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e)

## Things to be kept in mind

Converting a Torch Tensor to a NumPy array and vice versa is a breeze.

**The Torch Tensor and NumPy array will share their underlying memory locations (if the Torch Tensor is on CPU), and changing one will change the other.**

```python
a = torch.ones(5)
print(a)

# tensor([1., 1., 1., 1., 1.])

b = a.numpy()
print(b)

# [1. 1. 1. 1. 1.]

a.add_(1)
print(a)
print(b)

# tensor([2., 2., 2., 2., 2.])
# [2. 2. 2. 2. 2.]
```

#### Tensoroard in PyTorch

* The `add_image()`function takes image input in the shape of `[C,H,W]`and in the `dtype` of `uint8` or `float` type in range of `0.0 to 1.0`.Also it either takes `tensor or np.array` as an input.

#### General Guidelines:

* Fucntion from `F` does not have any parameters associated with them, there are merely funcitons such as relu, etc. So if you do `F.conv2D` you will have to pass the weights and bias parameters additionally. But if do `nn.Conv2D` then it will define the weights itself.&#x20;
* Make sure to set old the tensor associated with training to put them on `.to(device)` using it.&#x20;
* use `.item()` to print the value of an tensor
* Before collecting a new set of gradients with `loss.backward()` and doing backpropagation with `optimiser.step()`, it's necessary to manually zero the gradients of the parameters being optimised with `optimiser.zero_grad()`. By default, PyTorch _accumulates_ gradients, which is very handy when you don't have enough resources to calculate all the gradients you need in one go.
* One way to cut the computation graph is to use `.detach()`, which you may use when passing on a hidden state when training RNNs with truncated backpropagation-through-time. It's also handy when differentiating a loss where one component is the output of another network, but this other network shouldn't be optimised with respect to the loss - examples include training a discriminator from a generator's outputs in GAN training, or training the policy of an actor-critic algorithm using the value function as a baseline (e.g. A2C). Another technique for preventing gradient calculations that is efficient in GAN training (training the generator from the discriminator) and typical in fine-tuning is to loop through a networks parameters and set `param.requires_grad = False`.

### Autograd

[https://towardsdatascience.com/pytorch-autograd-understanding-the-heart-of-pytorchs-magic-2686cd94ec95](https://towardsdatascience.com/pytorch-autograd-understanding-the-heart-of-pytorchs-magic-2686cd94ec95)

This class is an engine to calculate derivatives (Jacobian-vector product to be more precise). It records a graph of all the operations performed on a gradient enabled tensor and creates an acyclic graph called the dynamic computational graph. The leaves of this graph are input tensors and the roots are output tensors. Gradients are calculated by tracing the graph from the root to the leaf and multiplying every gradient in the way using the chain rule.

For each iteration, several gradients are calculated and something called a computation graph is built for storing these gradient functions. PyTorch does it by building a Dynamic Computational Graph (DCG). This graph is built from scratch in every iteration providing maximum flexibility to gradient calculation. For example, for a forward operation (function)`Mul` a backward operation (function) called `MulBackward`is dynamically integrated in the backward graph for computing the gradient.

#### Computation Graph (DCG):

```python
import torch

# Creating the graph
x = torch.tensor(1.0, requires_grad = True)
y = torch.tensor(2.0)
z = x * y

# Displaying
for i, name in zip([x, y, z], "xyz"):
    print(f"{name}\ndata: {i.data}\nrequires_grad: {i.requires_grad}\n\
grad: {i.grad}\ngrad_fn: {i.grad_fn}\nis_leaf: {i.is_leaf}\n")
```

![](<../.gitbook/assets/image (32).png>)

**Data**: It’s the data a variable is holding. _**x**_ holds a 1x1 tensor with the value equal to 1.0 while _**y**_ holds 2.0. **z** holds the product of two i.e. 2.0

**requires\_grad**: This member, if true starts tracking all the operation history and forms a backward graph for gradient calculation. For an arbitrary tensor _**a** _ It can be manipulated in-place as follows: `a.requires_grad_(True).`

**grad:** grad holds the value of gradient. If `requires_grad` is False it will hold a None value. Even if `requires_grad` is True, it will hold a None value unless `.backward()` function is called from some other node. For example, if you call `out.backward()` for some variable _**out**_ that involved _**x**_ in its calculations then `x.grad` will hold **∂out/∂x**.

**grad\_fn:** This is the backward function used to calculate the gradient.

**is\_leaf**: A node is leaf if :

1. It was initialized explicitly by some function like `x = torch.tensor(1.0)` or `x = torch.randn(1, 1)` (basically all the tensor initializing methods discussed at the beginning of this post).
2. It is created after operations on tensors which all have `requires_grad = False.`
3. It is created by calling `.detach()` method on some tensor.

On calling `backward()`, gradients are populated only for the nodes which have both `requires_grad` and `is_leaf` True. Gradients are of the output node from which `.backward()` is called, w.r.t other leaf nodes.

On turning `requires_grad = True` PyTorch will start tracking the operation and store the gradient functions at each step as follows:

![](<../.gitbook/assets/image (25).png>)

#### -detach()

{% embed url="http://www.bnikolic.co.uk/blog/pytorch-detach.html" %}

* `.detach()` is used to break the gradient flow from a variable. Ex

```python
y=x**2
z=x.detach()**3
r=(y+z).sum()

r.backward()
x.grad
>>> tensor([2., 2., 2., 2., 2., 2., 2., 2., 2., 2.])
```

Here as you can see that `z=x.detach()`, hence gradient will not flow through `z` for x and only will flow through `y`.&#x20;

**Note:** Any in-place change on x.detach() will cause errors when x is needed in backward. Example:

```python
a = torch.arange(5., requires_grad=True)
b = a**2
c = a.detach() # error with detach(), wrong result with .data
c.zero_()
b.sum().backward()
print(a.grad)
```

In this there will an error because `c=a.detach()` and afterwards and in-place operation of `c.zero_()` is applied which changes the value of `a` but the `b.backward()` is called which will need to find the gradient of `a` with its original values.

* **backward() and retain\_graph=True**

Backward is the function which actually calculates the gradient through the backward graph all the way up to every **leaf node** traceable from the calling **root tensor**. The calculated gradients are then stored in `.grad` of every leaf node. **Root tensor** is the tensor on which the backward() is being called.&#x20;

{% embed url="https://jdhao.github.io/2017/11/12/pytorch-computation-graph/" %}

* **register\_buffer():**

These are used to tracks those Tensors of the model which are not parameters of the model but still needed to be tracked, such as the running mean and variance of the batchnorm layer. For these tensors we use buffers. These are not updated using sgd when called using model.parameters().  They are loaded with state\_dict().&#x20;

