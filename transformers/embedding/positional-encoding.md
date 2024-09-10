# Positional Encoding

**Position Encoding**

Position encoding allows for adding the positional information to the tokens, this preserves the seqeuencial nature of the token. Because self-attention block are permutation invariant ie order of input tokens are shuffled, the output is still same. Hence we need to inject positional information of each token as well. For that we use position encoding, we calculate potition encoding  for dimension $$d$$which is same dimension as word embedding, for each position in the sequence. Remeber, that the position encoding is independent of the what token it is, ie two different tokens in the same positon in the sequence will have the same position encoding. &#x20;

Remember there is no learning happening here.  Just a function that maps the position to a vector representation.&#x20;

Different types of position encoding:

* Absolute  - Sin and cos function - used in original transformer paper.&#x20;
* Relative
* Rotatry

{% hint style="info" %}
The positional encoding are added to the word embeddings to get the final input to the transofrmer model. But note that we can also just concatenate the position encoding to the word embedding instead of adding them. But this will end up increase the model size - the dimension of vector per token that's input to the model.  &#x20;
{% endhint %}

{% embed url="https://kazemnejad.com/blog/transformer_architecture_positional_encoding/" %}

**Position Embedding**

So in case of embedding, they are learned vector representation similar to how we learn word embeddings. Just that in word embedding we use token id to index the table to get corresponding vector, where as in Position embedding we use the position in the sequence to index the table to get corresponding vector.&#x20;

{% embed url="https://stats.stackexchange.com/a/573525" %}

## Why not Concatenating Positional Encoding instead of Summing

{% embed url="https://github.com/tensorflow/tensor2tensor/issues/1591" %}

{% embed url="https://www.reddit.com/r/MachineLearning/comments/cttefo/comment/exs7d08/" %}

## Why using sine and cosine

{% embed url="https://blog.timodenk.com/linear-relationships-in-the-transformers-positional-encoding/" %}

## PE as bottleneck in increased context length during testing

## Rotary Position Embedding

