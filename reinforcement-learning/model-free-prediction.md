---
description: Doing things without knowing the model.
---

# Model Free Prediction and Control

## Prediction

Prediction in this context simply means, predicting the state or state-action value function. It's same as **Policy Evaluation.** Where policy evaluation simply seems "evaluating" the policy ie. find the value function under the policy.&#x20;

### Monte-Carlo Policy Evaluation

In this method, to find the values of states, We perform episodes and the returns from all episodes are averaged for each state to gets its value. Basically here we calculate $$G_t = R_{t+1} + \gamma R_{t+2} + ...$$ by getting R from episodes ( $$S_1,A_1,R_2,S_2,A_2,R_3,...$$ ). Hence V(S) = average of all $$G_t$$ generated from episodes.&#x20;

Monte Carlo learning is **unbiased with high variance** (opposite to TD learning, which is biased with low variance)

MC policy evaluation uses empirical mean return instead of expected return

Two types: First Time and Every Time

#### First-Time:

* To evaluate state s&#x20;
* The first time-step t that state s is visited in an episode,&#x20;
* Increment counter N(s) ← N(s) + 1&#x20;
* Increment total return S(s) ← S(s) + G t&#x20;
* Value is estimated by mean return V (s) = S(s)/N(s)&#x20;
* By law of large numbers, V (s) → v π (s) as N(s) → ∞

#### Every-Time:

* To evaluate state s&#x20;
* Every time-step t that state s is visited in an episode,&#x20;
* Increment counter N(s) ← N(s) + 1&#x20;
* Increment total return S(s) ← S(s) + G t&#x20;
* Value is estimated by mean return V (s) = S(s)/N(s)&#x20;
* Again, V (s) → v π (s) as N(s) → ∞

![Understand this for clear distinction](<../.gitbook/assets/image (20).png>)

#### Incremental Update:

* Update V (s) incrementally after episode S 1 , A 1 , R 2 , ..., S T&#x20;
* For each state S t with return G t \
  &#x20;                         $$N(S_t) \leftarrow N(S_t) +1$$ \
  &#x20;             $$V(S_t) \leftarrow V(S_t) + \frac{1}{N(S_T)}(G_t - V(S_t))$$&#x20;
* In non-stationary problems, it can be useful to track a running mean, i.e. forget old episodes. \
  &#x20;                         $$V(S_t) \leftarrow V(S_t) + \alpha(G_t - V(S_t))$$&#x20;

### TD Learning

Simplest TD learning algorithm: TD(0)

* Update value V(s) towards the **estimated return** $$R_t + \gamma V(S_{t+1})$$ instead of $$G_t$$ as in monte carlo.\
  &#x20;$$V(s_t) \leftarrow V(s_t) + \alpha(R_{t+1}+\gamma V(S_{t+1}) - V(S_t))$$&#x20;
* $$R_t + \gamma V(S_{t+1})$$ is called the TD Target
* And $$\delta_t = R_t + \gamma V(S_{t+1}) - V(s_t)$$  is called the TD error

This approximation is essentially the one-step application of the Bellman operator on the estimate of V. This idea is called **bootstrapping** and is a cornerstone of temporal difference learning.

### Advantages & Disadvantages of Both:

* TD can learn online after every step. MC must wait for the episode to complete before return is known.&#x20;
* TD works in non-terminating environment. MC works only in terminating environment.&#x20;

### Bias-Variance Trade Off

* Return $$G_t = R_{t+1} + \gamma R_{t+2} + ..$$ is unbiased estimate of $$v_\pi(s_t)$$&#x20;
* TD Target $$R_t + \gamma V(S_{t+1})$$ is biased estimate of $$v_\pi(s_t)$$because return(G\_t) is empirical and TD target is just the guess of value function.
* TD target have lower variance as compared to return( $$G_t$$ ):
  * Return depends on many stochastic action, transitions, rewards.
  * TD target depends on only one stochastic action, transition, rewards.&#x20;

### Batch MC and TD

MC and TD converge: V (s) → v π (s) as experience → ∞

Batch Mode: having k episodes only

$$
S_1^1, a_1^1, r_2^1,...S_{T_1}^1\\.\\.\\.\\s1^k, a_1^k, r_2^k,...S_{T_k}^k
$$

* Repeatedly sample episode $$k \in [1,K]$$&#x20;
* Apply for MC or TD(0) to episode k.

### Certainty Equivalence

* MC converges to solution with minimum least squared error
  * best fit to the observed returns\
    &#x20;                      $$\sum_{k=1}^K\sum_{t=1}^{T_k}(G_t^k-V(S_t^k))^2$$&#x20;
*   TD(0) converges to the solution of max likelihood Markov model

    * Solution to the MDP best fits the data\
      &#x20;$$\widehat{P_{s,s'}^a} = \frac{1}{N(s,a)}\sum_{k=1}^K\sum_{t=1}^{T_k}1(s_t^k, a_t^k, s_{t+1}^k = s,a,s') \\ \widehat{R_s^a} = \frac{1}{N(s,a)}\sum_{k=1}^K\sum_{t=1}^{T_k}1(s_t^k,a_t^k = s,a)r_t^k$$&#x20;


* TD exploits Markov property
* MC does not exploit markov property

### Bootstrapping and Sampling

* Bootstrapping: updates involves an estimate
  * MC does not bootstrap
  * DP bootstraps
  * TD bootstraps
* Smapling: update samples an expectation
  * MC samples
  * DP does not samples
  * TD samples

### TD(λ)

#### n-step prediction

* n=1 (TD(0)), $$G_t^1 = R_{t+1} + \gamma V(S_{t+1})$$&#x20;
* n=2 , $$G_t^2 = R_{t+1} + \gamma R_{t+2} +  \gamma^2V(S_{t+2})$$&#x20;
* like so on
* n= $$\infty$$ (MC), $$G_t^\infty = R_{t+1} + \gamma R_{t+2} + ...... + \gamma^{T-1}R_T$$

#### λ-return

The λ-return $$G_t^\lambda$$ combines all the n-step returns $$G_t^n$$&#x20;

$$
G_t^\lambda = (1-\lambda)\sum_{n=1}^\infty\lambda^{n-1}G_t^n
$$

Here $$\lambda = 0$$ is TD(0) which is 1 step TD and $$\lambda = 1$$ is MC.&#x20;

#### forward-view TD(λ)

Update the value function towards the λ-return.&#x20;

$$
V(S_t) \leftarrow V(S_t) + \alpha(G_t^\lambda - V(S_t))
$$

Like MC, this also need complete episodes as this also require MC update to calculate λ-return.&#x20;

#### backward-view and Eligibillty Traces

## Control

Control in this context means how to control ie. what actions to take in the environment.&#x20;

### Off-Policy Vs On-Policy

In Off-Policy method the agent learns the value function for the optimal policy but acts according to another policy. \
On-policy methods mean the agent learns the value function of the policy dictating its behavior

### On-Policy MC Control

Policy Evaluation: MC policy  Evaluation, Q\
Policy Imporvement: $$\epsilon- greedy$$ policy improvement

#### $$\epsilon$$- Greedy Exploaration

Let there be $$m$$ actions. We will try to assign non-zero probability to every action. But greedy actions should be given more probability. WIth probabiltiy $$1-\epsilon$$ choose the greedy action. and with probability $$\epsilon$$ choose a random action.

$$
\pi(a|s) = \begin{cases}\epsilon/m+1-\epsilon & \text{if }a^*=arg \max_{a \in A} Q(s,a)\\\frac{\epsilon}{m} & otherwise\end{cases}
$$

### Temporal-Difference Learning: Sarsa(λ)

$$
Q(S,A) \leftarrow Q(S,A) + \alpha(R+\gamma Q(S',A') - Q(S,A))
$$

Every time-step:\
\- Policy Evaluation: Sarsa using above equation\
\- Police Improvement: $$\epsilon$$ - Greedy policy improvement

![Sarsa](<../.gitbook/assets/image (30).png>)

#### n-step Sarsa:

This same as n step return in TD(λ).&#x20;

* n=1 (sarsa), $$q_t^1 = R_{t+1} + \gamma Q(S_{t+1})$$&#x20;
* n=2 , $$q_t^2 = R_{t+1} + \gamma R_{t+2} +  \gamma^2Q(S_{t+2})$$&#x20;
* like so on
* n= $$\infty$$ (MC), $$q_t^\infty = R_{t+1} + \gamma R_{t+2} + ...... + \gamma^{T-1}R_T$$

#### Forward View Sarsa(λ)

$$
q_t^\lambda = (1-\lambda)\sum_{n=1}^\infty\lambda^{n-1}q_t^n \\
Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha(q_t^\lambda - Q(S_t,A_t))
$$

#### Backward View Sarsa(λ)

$$
E_t(s,a) = \gamma \lambda E_{t-1}(s,a) + 1(S_t=s, A_t=a)
$$

Q(s,a) is updated for every state s and action a. In proportion to TD-error $$\delta_t$$ and eligibility trace $$E_t(s,a)$$&#x20;

$$
\delta_t = R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t) \\
Q(s,a) \leftarrow Q(s,a) + \alpha\delta_tE_t(s,a)
$$

#### Sarsa(λ) Algorithm:

![sarsa](<../.gitbook/assets/image (143).png>)

### Off-Policy Learning

Evaluate target policy (generally optimal policy) $$\pi(a|s)$$ to compute $$v_\pi(s)$$ or $$q_\pi(s,a)$$, while following behaviour policy $$\mu(a|s)$$to take actions in the environment when interacting.&#x20;

$$
\{S_1, A_1, R_2,...,S_T\} \sim \mu
$$

This allows:

* Learn from observing humans or other agents
* Learn about optimal policy while following exploratory policy
* learn about multiple policies while following one policy

#### Importance Sampling

Estimate the expectation of a different distribution

$$
E_{X\sim P}[f(X)] = \sum P(X)f(X)\\
= \sum Q(X)\frac{P(X)}{Q(X)}f(X)\\
= E_{X\sim Q}[\frac{P(X)}{Q(X)}f(X)]
$$

![Off-Policy Monte Carlo](<../.gitbook/assets/image (151).png>)

![](<../.gitbook/assets/image (3) (1).png>)

### Q-Learning: Off-Policy TD Control

It is the model-free algorithm i.e. it focus on learning the value function and use these estimates to get an optimal policy.&#x20;

$$
Q(s,a)←Q(s,a)+α(r+γ\max_{a'\in A}Q(s',a')−Q(s,a))
$$

Where: \
&#x20;• Q(s, a) is the estimate for the action-value function of the pair s, a \
• α ∈ \[0, 1] is the learning rate that determines how “quickly” the new information will override the old information, \
• r + γ maxQ(s', a') is the learned value, which is composed of the immediate one- step reward and the estimate of the optimal future value.&#x20;

The idea behind this algorithm is to transform the Q∗ formula given in Equation below into an iterative approximation procedure. At each step, we update the current estimate of Q∗ by using estimates of the optimal future value.

The above equation comes from Bellman's action value optimality equation

$$
Q_*(s,a) = R_s^a + \gamma \sum_{s^`\in S}P_{ss'}^a \max_{a'} Q_*(s',a')
$$

![](<../.gitbook/assets/image (80).png>)

## Summary

![](<../.gitbook/assets/image (59).png>)

![](<../.gitbook/assets/image (95).png>)

### Exploration Vs Exploitation

On the one hand, exploitation denotes the behavior of agents that select an action because it is the “best” – supposed to yield the highest reward – action. This action is dictated by the optimal, or greedy policy. On the other hand, exploration is when the actions all have the same probability of being chosen by the agents. They literally explore all their possibilities. It is easy to understand that using exclusively one of these behaviors is not efficient.

### Why not pure-exploitation or pure-exploration is good?

Only exploration means that, at some point, the agent has correct estimates for all state-action pairs but never uses this knowledge to maximize its rewards. It kind of defeats the whole point of learning. Without exploration, the agent can achieve an optimal reward only if it already has correct state-action estimates. However, such estimates can only be achieved through exploration. For example, if we initialize all the estimates to 0, a pure-exploitation agent will choose one action and stick to this action if the reward is positive. If the reward is negative, it proceeds with another action and eventually ends up in the same situation. Imagine a system where all the rewards are positive. The first (randomly) chosen action gives the smallest possible reward; when in this state, the agent always chooses this action because its estimate is greater than the others (0). In the end, the agent is very far from the maximum reward it could have obtained if its estimates were more accurate.

### **wrt to Q-Learning:**

&#x20;In Walkins and Dayan (1992), it is proven that the Q-values converge to the optimal Q∗ if two conditions are met. <mark style="color:yellow;">One of them states that every state-action pair has to be visited infinitely often</mark>. Consequently, the agent’s policy needs to respect this condition. For this, we could simply use a policy where the actions are always chosen randomly with a uniform distribution over the action space. However, the global performance of the agent during the learning phase will be poor; we want it to maximize its return. <mark style="color:red;">These two opposite behaviors are called exploration and exploitation. Hence, to learn the good policy using Q-learning we have to maintain the balance between exploitation and exploration.</mark>&#x20;

### **Fix for This: ϵ-greedy**

The optimal action a∗ is selected with a probability 1 −  ϵ and a random action with a probability ϵ.

$$
a_t^* = arg \max_a Q_t(a)\\
a_t = \begin{cases}a_t^* & \text{with probability 1- }\epsilon\\ \text{random action} & \text{with probability } \epsilon\end{cases}
$$

### Deep Q-Networks

DQNs are deep learning models that combine deep convolutional neural networks with the Q-learning algorithm.An important contribution made by DQNs is the use of experience replay and a target network to stabilize the training of the Q action- value function approximation with deep neural networks. Q-network thus refers to a neural network function approximator of the Q-function:

$$
Q(s,a;\theta) \approx Q^*(s,a)
$$

where $$\theta$$ is the weight of the network

### Experience Replay Catastrophic

Catastrophic forgetting or catastrophic interference (Mccloskey and Cohen (1989), Rat- cliff (1990)) denotes the tendency of neural networks to suddenly forget information that they previously learned.

Experience replay (Lin, 1992) consists in maintaining a buffer of the old experiences and train the network against them.&#x20;

&#x20;      During the training, we use a buffer where previous experiences are stored. An experience consists of an observed state and action pair, the immediate reward obtained and the next state observed. When the buffer is full, new experiences usually replace the oldest ones in the buffer.&#x20;

To train the network, we sample a batch of experiences from the buffer and use them to apply the usual backpropagation algorithm.&#x20;

The advantage of this approach is that, by sampling these batches of experiences, we break the correlation between data that we get when the network is trained in the usual online fashion.

### Deep Q-Learning

The deep Q-learning algorithm uses experience replay. An agent’s experience at a time step t is denoted by et and is a tuple (st, at, rt, st+1) consisting of the current state st, the chosen action at, the reward rt and the next state st+1. The experiences for all the time steps are stored in a replay memory, over many episodes. We then apply minibatches updates to samples of experiences.

![Deep Q-Learning Procedure](<../.gitbook/assets/image (2) (1) (1) (1).png>)

Since the network serves as an approximator for the Q-function, each output neuron of this network corresponds to one valid action, and every action is mapped to an output neuron. Thus, after a feedforward pass of that network, the outputs are the estimated Q-values of the state-action pair defined by the input and the output’s corresponding action.
