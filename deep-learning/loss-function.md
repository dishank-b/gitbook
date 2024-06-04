# Loss function

If you ever want weigh different losses when training using multiple losses such that both of them have same effect, weigh them according to magnitude of the gradients they give and not according to the magnitude of the loss. &#x20;

### Cross Entropy Loss

$$
\mathcal{L} = -\frac{1}{N}\sum_i^N \sum_c^C y_c^i \log \hat{y}^i_c
$$

#### Gradient Calculation

<pre><code><strong>// Let's consider that's it's single data point i.e N = 1
</strong><strong>logit = XW+b // c dimensional output where c is # of classes
</strong>ypred = e^logit_c/(\sum_c e^logit_c) // softmax to normalize logits
Loss = \sum_c y_c log(ypred_c) // y_c is ground truth label. 
</code></pre>

$$
z = Xw+b\\
\hat y = \text{softmax}(z)
$$

Now, here we will find the derivative of cross entropy loss with respect to $$z$$

$$
\frac{\partial \mathcal L}{\partial z} = \hat y  - y
$$

{% embed url="https://towardsdatascience.com/derivative-of-the-softmax-function-and-the-categorical-cross-entropy-loss-ffceefc081d1" %}



