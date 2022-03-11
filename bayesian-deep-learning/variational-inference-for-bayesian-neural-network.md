# Variational Inference for Bayesian Neural Network

Bayesian neural networks differ from plain neural networks in that their weights are assigned a probability distribution instead of a single value or point estimate. These probability distributions describe the uncertainty in weights and can be used to estimate uncertainty in predictions. Training a Bayesian neural network via variational inference learns the parameters of these distributions instead of the weights directly.

### Variational Inference

An analytical solution for the posterior $$p(w|D)$$ in neural networks is untractable. We therefore have to approximate the true posterior with a variational distribution $$q(w|θ)$$ of known functional form whose parameters we want to estimate.\
\
What this means is that here we want to lean a probability distribution for the weight the w instead of a point value. But learning an actual ditribution is difficult, so now we approximate it with existing any distributions such as gaussian, etc. Where these distributions can be defined using some parameters $$\theta$$ .&#x20;

This can be done by minimizing the [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler\_divergence) between $$q(w|θ)$$ and the true posterior $$p(w|D)$$ w.r.t. to _**θ**_. It can be shown that the corresponding optimization objective or cost function can be written as

$$
F(D,\theta) = KL(q(w|\theta)||p(w|D)) = KL(q(w|\theta)||p(w)) - E_{q(w|\theta)}\log p(D|w)
$$

This loss function is called is variational free energy. First term is called complexity cost and the secong term is the expeted value of the liklihood w.r.t. the variational distribution and is called the liklihood cost. Also:

$$
F(D,\theta) =  E_{q(w|\theta)}\log q(w|\theta) - E_{q(w|\theta)}\log p(w)- E_{q(w|\theta)}\log p(D|w)
$$

We see that all three terms in equation above are expectations w.r.t. the variational distribution $$q(w|θ)$$ . The cost function can therefore be approximated by drawing [Monte Carlo](https://en.wikipedia.org/wiki/Monte\_Carlo\_method) samples $$w^i$$ from q(w|θ).

For example, we’ll use a Gaussian distribution for the variational posterior, parameterized by $$θ=(μ,σ)$$ where μ is the mean vector of the distribution and σ the standard deviation vector. The elements of $$σ$$ are the elements of a diagonal covariance matrix which means that weights are assumed to be uncorrelated. Instead of parameterizing the neural network with weights $$w$$ directly we parameterize it with $$μ$$ and $$σ$$ and therefore double the number of parameters compared to a plain neural network.

### Resources

* [https://dasayan05.github.io/blog-tut/2019/11/20/inference-in-pgm.html](https://dasayan05.github.io/blog-tut/2019/11/20/inference-in-pgm.html)\
  Describes using varitional inference with latent variables, graphical models, etc. Good for understanding
