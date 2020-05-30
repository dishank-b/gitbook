# Sampling-Based Inference

Let's say you have some probabilistic model and want to do some inference. You the problem is intractable and are you not able to find analytical solution for it. What would you do?

Simple, generate samples based on your distribution and check what behaviour of your samples for inference. 

## Monte Carlo Sampling

the samples are independent of each other, as in the coin toss example above. These algorithms are called Monte Carlo methods.

## Markov Chain Monte Carlo \(MCMC\)

For problems with many variables, generating good quality independent samples is difficult, and therefore, we generate _dependent_ samples, that is, each new sample is random, but close to the last sample. Such algorithms are called Markov Chain Monte Carlo \(MCMC\) methods, because the samples form a “Markov chain”.

