# Embedding

## What are Embeddings

Embedding are basically vector (numerical) representations of words (tokens). You input a token (number representation of a word or sub-word) and it output a vector to represent that token. Embedding enables you to represent words into vectors that can be used in your model.&#x20;

Embedding of words generally follows some structure, such as, embedding of similar words are close to each other in the vector space.&#x20;

There are different methods to train embedding. Based on different losses and different tasks, embedding can be learnt differently.&#x20;

### Examples of embedding:

* One-hot encoding - Basically each word will be a one hot vecor. Hence there to represents all the words in your corpus, the vector length will be equal to all the unique words in your corpus. **Which is way too high of input dimension to process.**
* Word2Vec - Neural network based approach to learn a NN to output a vector of corresponding input.&#x20;
* BERT Embeddings

## Embedding Layer

Let's say that the each token is represented as a $$d$$ dimensional vector.&#x20;

Then we can imagine Embedding layer as a weight matrix or  lookup table denoted by $$W$$ of dimensions $$T \times d$$, where $$T$$ is the vocabulary size. So now whenever we have token $$t_i$$, we can just lookup the Embedding table/ weight matrix at the row $$t_i$$ and that row is the $$d$$ dimensional vector embedding of the token.&#x20;

This could also be looked as  $$x^TW$$ where is $$x$$ one hot vector to represent $$t_i$$ i.e $$x[idx] == 1 \space\text{if} \space idx==t_i \space else \space 0$$. This operation basically gives you the row $$t_i$$ from the &#x20;

## Tokenization to Embeddings pipeline

{% embed url="https://tinkerd.net/blog/machine-learning/bert-embeddings/" %}

{% embed url="https://youtu.be/5MaWmXwxFNQ" %}

{% embed url="https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/" %}
