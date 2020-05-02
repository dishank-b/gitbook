# Deep Reinforcement Learning

## Goal of Deep RL

As deep RL have parameters $$\theta$$ , hence our objective is to get $$\theta$$ such that **reward** of each state in an episode is maximized. 

![](../../.gitbook/assets/image%20%28103%29.png)

**Note: Here we are not considering discounted reward**

## Finite & Infinite Horizon Objective Function

![](../../.gitbook/assets/image%20%2862%29.png)

![](../../.gitbook/assets/image%20%28104%29.png)

### Stationary Distribution: Markov Chains

A **stationary distribution** of a [Markov chain](https://brilliant.org/wiki/markov-chains/) is a probability distribution that remains unchanged in the Markov chain as time progresses. Typically, it is represented as a row vector π whose entries are probabilities summing to 1, and given [transition matrix](https://brilliant.org/wiki/markov-chains/#transition-matrices) $$\textbf{P}$$ , it satisfies

$$
\pi = \pi \textbf{P}
$$

Once you are in a stationary distribution, you will remain in a stationary distribution. Stationery distribution is a vector conataining probabilities of being in state for each state in corresponding element.  
Seeing the equation above, eigen vector of a transition matrix P is always an stationary distribution. 

## Expectation makes objective function smooth

![](../../.gitbook/assets/image%20%28122%29.png)

Taking expectation of a function makes it smoother, allowing it differential wrt to the parameter. Look at example above. The reward function above is non-differentiable, but expectation makes it differentiable, making gradient based learning feasible for RL. 

## Types of RL Algos

![](../../.gitbook/assets/image%20%28135%29.png)

### Model-Based RL Algo

![](../../.gitbook/assets/image%20%2864%29.png)

### Value-Based RL Algo

![](../../.gitbook/assets/image%20%28112%29.png)

### Direct Policy Gradients

![](../../.gitbook/assets/image%20%2870%29.png)

### Actor-Critic

![](../../.gitbook/assets/image%20%28138%29.png)

## Trade-Offs

### Sample Efficiency

![](../../.gitbook/assets/image%20%2839%29.png)

**Off-Policy:** Able to improve the policy without generating new samples from that policy  
**On-policy:** each time the policy is changed, even a little bit, we need to generate new samples

* **Conventional Policy Gradient Methods are on-Policy. New samples are generated each time with a updated policy.** 
* **Actor-Critic method can either be on-policy or off-policy depending upon the details**
* **Model based are more efficient as it is intuitive itself, because having a model can reduce the need of samples.**

### Convergence and Stability

![](../../.gitbook/assets/image%20%2814%29.png)

* Model-based RL method are gradient descent to get the best model. i.e. we are fit the for the model but nowhere maximizing the reward. 

