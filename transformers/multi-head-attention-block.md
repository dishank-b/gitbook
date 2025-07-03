# Multi-head Attention Block

## Attention Block

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt="" width="342"><figcaption><p>Scaled dot-product attension</p></figcaption></figure>

Each of $$Q,K,V$$ are linear projection of token embeddings.&#x20;

$$
\text{Attention(Q,K,V) = \text{softmax}}(\frac{QK^T}{\sqrt{d_k}})V
$$

## Multihead Attention

Now the same Attention block is applied mulitple time in parallel, then the result is concatenated.&#x20;

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

