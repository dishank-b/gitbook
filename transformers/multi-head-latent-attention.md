# Multi-head Latent Attention

How to reduce KV cache size compared to alternative methods such as group-query attention or multi-query attention.&#x20;



<figure><img src="../.gitbook/assets/image (180).png" alt=""><figcaption></figcaption></figure>

**In Multi-query attention,** basically there's single key value shared across all the attention heads, instead of key value for each of the head.&#x20;

In this way, we have have to cache smaller size of key-value. But this leads to to compromising on the model performance as we are reducing the parameters of the model.&#x20;

## Multi Head Latent Attention

**How do we get key and value**

Let $$x$$ be the input, and how we can get key and value $$k,v$$, is by using a full-connected layer i.e multiplying by dense matrixes $$W_k \in \mathcal{R}^{(n_h \times d_{head}) \times d_{model}}$$ and $$W_v \in \mathcal{R}^{(n_h \times d_{head}) \times d_{model}}$$, where $$n_h, d_{head}, d_{model}$$ are number of heads, vector dim in each head, model dimension respectively.&#x20;

$$
k = W_kx\\
v = W_vx
$$

**DeepSeek's Trick**

Force this input vector transformation to key-values to be low rank. i.e &#x20;

Instead of going from $$d_{model} \rightarrow n_h \times d_{head}$$, we do $$d_{model} \rightarrow l_{dim} \quad \text{and} \quad l_{dim} \rightarrow n_h \times d_{head}$$. Where $$l$$ will be the dimension of the latent vector when going from $$x \rightarrow k,v$$. **And instead of caching** $$k,v$$ **we cahce lower dimensional vector** $$l$$. $$x\in \mathcal{R}^{L \times d_{model}}$$

How we do this mathematically

$$
l_k = xW^l\\
k = l_kW^k_l
$$

Similiary for value

$$
l_v = W^lx\\
v = W^v_l l_v
$$

And this basically means that big matrix such as $$W_k \in \mathcal{R}^{(n_h \times d_{head}) \times d_{model}}$$ and $$W_v \in \mathcal{R}^{(n_h \times d_{head}) \times d_{model}}$$ has been decomposed into lower rank matrices.&#x20;

**But just caching** $$l_k,l_v$$ **would mean that during inference, we would have to waste some inference compute to get** $$k,v$$ **from** $$l_k,l_v$$ by up-projecting.&#x20;

**Another Clever trick here**

&#x20;Instead of up-projecting from latent to actual and value. We can merge that up-projection for key with q matrix and for v, we can merge the up-projection with the output linear projection layer.&#x20;



\==============================



The reason low-rank compression is so effective is because there’s plenty of information overlap between what different attention heads need to know about. If we used low-rank compression on the key and value vectors of individual heads instead of all keys and values of all heads stacked together, the method would simply be equivalent to using a smaller head dimension to begin with and we would get no gain. Exploiting the fact that different heads need access to the same information is essential for the mechanism of multi-head latent attention.

Methods such as grouped-query attention exploit the possibility of the same overlap, but they do so ineffectively by forcing attention heads that are grouped together to all respond similarly to queries. In other words, information sharing becomes coupled to having identical behavior in some restricted sense, a clearly undesirable property. Low-rank compression, on the other hand, allows the same _information_ to be used in _very different ways_ by different heads. In theory, this could even have beneficial regularizing effects on training, and DeepSeek reports finding such effects in their technical reports.

I see this as one of those innovations that look obvious in retrospect but that require a good understanding of what attention heads are actually doing to come up with. Once you see the approach, it’s immediately obvious that it cannot be any worse than grouped-query attention and it’s also likely to be significantly better. However, coming up with the idea of trying this is another matter.







