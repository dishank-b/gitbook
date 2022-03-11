---
description: >-
  Directly parametrise the policy instead of value or action-value function and
  optimize it.
---

# Policy Gradient

In this we will directly optimize the policy without using the value function. We will use policy gradient to optimize the policy.&#x20;

$$
\pi_\theta(s,a) = P[a|s,\theta]
$$

**Advantage:**

* Effective in high-dimensional or continous action spaces
* Can learn stochastic policies

**Disadvantages:**

* Typically converges to local rather global minima.
* Evaluating a policy is typically ineffcient and high variance.

## Policy Objective Function

We will optimise the parameters of policy funtiuon wrt to certain objective funtion $$J(\theta)$$ , which are as follows:

* d
* d
* $$E_{s_1 \sim p(s_1)}[V^\pi(s_1)]$$&#x20;

## Policy Gradient Algo

![](<../../../.gitbook/assets/image (69).png>)

Here $$\theta$$ parametrize the policy. \
The green box have a model which can estimate the return. Blue box use gradient descent to update the policy using the estimated return. Now run the updated policy to generate more samples.&#x20;

### Policy Differentiation (Policy Gradient Theorem)

![](<../../../.gitbook/assets/image (19).png>)

In above image we are calculting the gradient of objective function. Note the the gradient is calculated in term of gradient of log of probability of trajectory and total reward of the trajectory. \
**Note: Here is** $$\pi_\theta$$ **does not mean policy but the probability distribution.** $$\pi_\theta(\tau) = p_\theta(\tau)$$ ****&#x20;

![](<../../../.gitbook/assets/image (108).png>)

**Finally,** the gradient of of objecting funtion is written in terms of expectation of gradient of log of policy multiplied by total reward.&#x20;

$$
\triangledown_\theta J(\theta) = E_{\tau \sim \pi_\theta(\tau)}[\triangledown_\theta \log p_\theta(\tau)r(\tau)] \\ 
= E_{\tau \sim p_\theta(\tau)}[(\sum_t\triangledown_\theta \log \pi_\theta(a_t|s_t))(\sum_t r(s_t, a_t))]
$$

**Note: Here the term inside the gradient will be zero 0 for deterministic policy. Hence for now this will work only for stochastic policy**

### Policy Gradient Vs Maximum Likelihood

![](<../../../.gitbook/assets/image (45).png>)

Here you can see that the **log term** in policy gradient is similar to the **maximum liklihood** loss in the supervised learning.&#x20;

**So we can compute the policy gradient similary to the way we calculate the maximum liklihood gradient.**&#x20;

One thing to note here, here is that in policy gradient the log term is weighted by reward. Hence, it helps to weight the log term according to the goodness or badess of the trajectory which is defined by reward. Hence we can increase the liklihood of trajectory weighted by its reward. **** Reward help us to increase probabilities of certain policies whereas simply using maximum likelihood will increase probabilty of all policies**. Hence the updated policy makes the trajectory with more reward more probable than the trajectory with less reward.**&#x20;

### Problems with Policy Gradient: High Variance

* The gradient above is which is estimated by $$E_{\tau \sim \pi_\theta(\tau)}[\triangledown_\theta \log p_\theta(\tau)r(\tau)]$$ have high variance. Meaning if we estimate this quantity with finite number of samples and you repeat this process many times, everytime you reevaluate the graient, you will get different estimate and these estimates will be different from each other.&#x20;
* This leads to poor convergence.&#x20;
* Why do we have high varinace? Explanation: [https://youtu.be/XGmd3wcyDg8?list=PLkFD6\_40KJIxJMR-j5A1mkxK26gh\_qg37\&t=1690](https://youtu.be/XGmd3wcyDg8?list=PLkFD6\_40KJIxJMR-j5A1mkxK26gh\_qg37\&t=1690)&#x20;
* The video will explain, that **this method is very senstive to the reward formulation. Just adding a constant to the reward function can affect the policy gradient very much.**&#x20;

### Reducing the Variance&#x20;

* Policy at time $$t'$$ should not affect the reward at time $$t$$ if $$t'>t$$. To make sure that our objective follows this law if make sure some changes in the formula for policy gradient.&#x20;

$$
\triangledown_\theta J(\theta) 
= \frac{1}{N}\sum_{i=1}^
N\sum_{t=1}^T\triangledown_\theta \log \pi_\theta(a_t^i|s_t^i)(\sum_{t=1}^T r(s_t^i, a_t^i))
$$

instead of using above formula which is orignial one, we will change it to below

$$
\triangledown_\theta J(\theta) 
= \frac{1}{N}\sum_{i=1}^
N\sum_{t=1}^T\triangledown_\theta \log \pi_\theta(a_t^i|s_t^i)(\sum_{t'=t}^T r(s_t^i, a_t^i))
$$

**This ensures that policy at time** $$t$$ **is affects only the rewards which comes after time** $$t$$ **for every trajectory collected. i.e the decision I take now can only change my future reward and not the past ones. Hence while updating the gradient, we only consider the rewards after time** $$t$$ **to update policy at time t.** \
**The above equation reduces to:**

$$
\triangledown_\theta J(\theta) 
= \frac{1}{N}\sum_{i=1}^
N\sum_{t=1}^T\triangledown_\theta \log \pi_\theta(a_t^i|s_t^i)Q_{i,t}
$$

**Why does doing this reduces variance?:**\
****Simply beacuse the now we are adding less numbers in the sum of reward, hence this will simply reduce the variance. i.e. smaller numbers leads to smaller variance.&#x20;

* Using **Baseline**

What above formula do is,  like if all the rewards are positive then all the probabilities will go up.  \
So instead of multiply $$\log \pi$$ by sum of rewards we should multiply it by the reward minus the average reward. This will make things more rewarding than usual to go up and things less rewarding than usual go down. Something better than expected will be more likely and worse than expected will be less likely.&#x20;

$$
\triangledown_\theta J(\theta) 
= \frac{1}{N}\sum_{i=1}^
N\triangledown_\theta \log \pi_\theta(\tau)(r(\tau)-b) \\
b = \frac{1}{N}\sum_i^Nr(\tau)
$$

**The above formula is an unbiased estimater of the gradient.**

_**Link:**_ [_**https://youtu.be/XGmd3wcyDg8?list=PLkFD6\_40KJIxJMR-j5A1mkxK26gh\_qg37**_](https://youtu.be/XGmd3wcyDg8?list=PLkFD6\_40KJIxJMR-j5A1mkxK26gh\_qg37)_****_\
_**The above part states that in finite horizon problme, a optimal policy is a time variant policy i.e it changes with time. But when using neural network we restrict our policy class to be time invarient policy as same network is used at every time step.**_ &#x20;

### Analysing the Variance in Gradient

![](<../../../.gitbook/assets/image (92).png>)

## Policy Objective in term of Action-Value function

![](<../../../.gitbook/assets/image (1).png>)

Here we write the policy optimization objective in terms of action-value of $$S_1$$ .

In simpler terms our **RL objective is:**  $$E_{s_1 \sim p(s_1)}[V^\pi(s_1)]$$

**Note: Here we are not considering discounted reward**

![](<../../../.gitbook/assets/image (117).png>)

## Policy Optimization

Find $$\theta$$ which maximizes $$J(\theta)$$ .

$$
\triangle \theta = \alpha \triangledown_\theta J(\theta)
$$

where $$\triangledown_\theta J(\theta)$$ is the policy gradient

### Monte-Carlo Policy Gradient

This have high variance

### Actor-Critic Policy Gradient

use a critic to estimate the action-value function, $$Q_w(s,a) \approx Q^{\pi_\theta}(s,a)$$&#x20;

Actor-critic algorithms maintain two sets of parameters:\
\- Critic Updates action-value function parameters w\
\- Actor Updates policy parameters θ, in direction suggested by critic

Algorithm follow an approximate policy gradient:

$$
\triangledown_\theta J(\theta) \approx E_{\pi_\theta}[\triangledown_\theta \log\pi_\theta(s,a)Q_w(s,a)] \\
\triangle\theta = \alpha \triangledown_\theta\log\pi_\theta(s,a)Q_w(s,a)
$$

**The critic added is just solving the familiar problem of policy evaluation i.e how good is current policy learnt by the actor.**&#x20;

#### Action-Value(Q) Actor-Critic Algorithm

Using linear value fn approx. $$Q_w(s,a) = \phi(s,a)^Tw$$ \
&#x20;\- Critic updates w by linear TD(0)\
&#x20;\- Actor Updates $$\theta$$ by policy gradient

Algorithm:

![](<../../../.gitbook/assets/image (8).png>)

#### Compatible Function Approximation

#### Advantage Function Actor Critic

Subtracting baseline function B(s) from the policy gradient **reduces variance** without changing expectation.&#x20;

A good baseline function is state value function B(s) = V(s). \
Hence we rewrite the policy gradient using the advantage function $$A^{\pi_\theta}(s,a)$$&#x20;

$$
A^{\pi_\theta}(s,a) = Q^{\pi_\theta}(s,a) - V^{\pi_\theta}(s,a) \\
\triangledown_\theta J(\theta) = E_{\pi_\theta}[\triangledown_\theta \log\pi_\theta(s,a)A^{\pi_\theta}(s,a)]
$$

**Estimating the Advantage Function:**

****

#### **Eligibility Traces**

**Natural Policy Gradient**

****
