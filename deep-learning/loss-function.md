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
Loss = \sum_c y_c log(ypred_c) // y_c is ground truth label
</code></pre>

Now using the chain rule we can find the gradient $$\nabla_w \mathcal{L}$$ of $$\mathcal{L}$$ with respect to the weights $$w$$.&#x20;

$$
\frac{\partial \mathcal{L}}{\partial w} = \frac{\partial \mathcal{L}}{\partial y}\cdot\frac{\partial \mathcal{y}}{\partial \text{logit}}\cdot\frac{\partial \mathcal{\text{logit}}}{\partial w}
$$

