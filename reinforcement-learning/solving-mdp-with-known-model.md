---
description: Planning by DP
---

# Solving MDP with known Model

When model is fully known, we use DP to evaluate the model and then improve the policy.&#x20;

### DP:

Dynamic Programming is a very general solution method for problems which have two properties:&#x20;

* Optimal substructure
  * &#x20;Principle of optimality applies&#x20;
  * Optimal solution can be decomposed into subproblems&#x20;
* Overlapping subproblems&#x20;
  * Subproblems recur many times&#x20;
  * Solutions can be cached and reused

### Policy Evaluation:

* Using **synchronous backups**, (**backup means update**)
  * At each iteration k + 1&#x20;
  * For all states s ∈ S&#x20;
  * Update $$V_{k+1}(s)$$ from $$V_k(s')$$&#x20;
  * where $$s'$$ is a successor state of s

$$
V_{k+1}(s) = E[r+\gamma V_k(s') | S_t=s] = \sum_a\pi(a|s)\sum_{s',r}P(s',r|s,a)(r+\gamma V_k(s'))
$$

### **Policy Improvement**

Based on the value functions, Policy Improvement generates a better policy π′≥ππ′≥π by acting greedily.

$$
Q_π(s,a)=𝔼[R_{t+1}+γV_π(S_{t+1})|S_t=s,A_t=a]=∑_{s′,r}P(s',r|s,a)(r+γV_π(s'))
$$

$$
\pi' = greedy(v_{\pi}) \\
\pi'(s) = arg \max_{a \in A} q_\pi(s,a)
$$

### Policy Iteration

The Generalized Policy Iteration (GPI) algorithm refers to an iterative procedure to improve the policy when combining policy evaluation and improvement.

Given a policy $$\pi$$ :

* Evaluate the policy  $$\pi$$ using **policy evaluation**
* Then perform policy improvement to improve the policy.\
  &#x20;$$\pi' = greedy(V_\pi)$$&#x20;
  * In case of deterministic policy we can do, $$\pi'(s) = arg \max_{a \in A} q_\pi(s,a)$$&#x20;
  * This improves the value from any state s over one step,\
    &#x20;$$q_\pi(s, \pi'(s)) = \max_{a\in A} q_\pi(s,a) \geq q_\pi(s, \pi(s)) = v_\pi(s)$$&#x20;

**This will always lead to the optimal policy**  $$\pi^*$$

### **Value Iteration**

Any optimal policy can be subdivided into two components:&#x20;

* An optimal first action $$A_*$$&#x20;
* Followed by an optimal policy from successor state S'

#### Deterministic Value Iteration

* If we know the solution to subproblems $$v_*(s')$$&#x20;
* Then solution to can be found by one-step lookahead\
  &#x20;$$v_*(s) = \max_{a \in A}(R_s^a + \gamma \sum_{s' \in S}P_{ss'}^aV_*(s'))$$
* we do this for every state until convergence&#x20;
* Start with the final rewards and work backwards

Using **synchronous backups**&#x20;

* At each iteration k + 1&#x20;
* For all states s ∈ S&#x20;
* Update $$v_{k+1}(s)$$ from $$v_k(s')$$&#x20;

Once we get the optimal value function, we can find the deterministic optimal policy using following:

$$
\pi^*(s) = arg \max_{a \in A} \sum_{s'\in S}P_{ss'}^a
$$

### Extension to DP:

* Synchronous\
  Synchronous value iteration stores two copies of value function\
  $$v_{new}(s) = \max_{a \in A}(R_s^a + \gamma \sum_{s' \in S}P_{ss'}^av_{old}(s')) \\v_{old} = v_{new}$$
* Asynchronous
  * In-place DP\
    This one just one value\
    $$v_{*}(s) = \max_{a \in A}(R_s^a + \gamma \sum_{s' \in S}P_{ss'}^av_{*}(s'))$$
  * Prioritised sweeping
  * Real-time dynamic programming
* Sample Backups\
  Using **sample rewards and sample transitions** {S, A, R, S\`}Instead of reward function R and transition dynamics P. **Sample is the keyword here.**&#x20;

### Convergence of Policy or Value Iteration.&#x20;

This can be proved using contraction mapping theorem.&#x20;
