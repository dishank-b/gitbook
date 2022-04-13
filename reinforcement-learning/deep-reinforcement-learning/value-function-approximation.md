# Value Function Approximation

## Value Function Approximation

SO far we have represented value function using look-up table:\
\- Every state s has an entry V(s)\
\- Every state-action pair have an entry Q(s,a)

Now it is impossible to have V(s) entry if we have large number of states. Hence, to solve this we use **Value Function Approximator.** Which are basically functoins which can map state to its value i.e $$v: s \rightarrow a$$ .

## Stochastic Gradient Descent

$$
J(w) = E_\pi[(v_\pi(s)-\hat{v}(s,w))^2]
$$

Here, $$v_\pi$$ is the original taget and $$\hat{v}$$ is the value approximation function with parameters w. Now we will update the $$w$$ using gradient descent in order to minimize the the cost $$J(w)$$ . Hence

$$
\triangle w = \alpha (v_\pi(s)-\hat{v}(s,w))\triangledown_w\hat{v}
(s,w)
$$

But is the problem that we don't know the target value funtion $$v_\pi(s)$$ in reinforcement learning before hand . We will see below how to handle this problem.

## Different Value approximation

### Linear Function Approximation

**Feature Vector:** We represent state using a vector as below.&#x20;

![](<../../.gitbook/assets/image (112).png>)

Using this state feature vector and weights. Linear approximation is as follows:

$$
\hat{v}(s,w) = x(s)^Tw = \sum x_j(s)w_j
$$

Hence in this case update become:

$$
\triangle w = \alpha (v_\pi(s)-\hat{v}(s,w))x(s)
$$

**Table Lookup Features:** It is special case for linear function approximation. Here the state vector have all the states in itself. see below:\


![](<../../.gitbook/assets/image (55).png>)

## Incremental Prediction Algorithms

Here we talk about the ways in which we can substitute the value of $$v_\pi(s)$$ from the the weights.&#x20;

### Monte-Carlo with Value Funtoni Approx.

Use $$G_t$$ calucuated from the episodes here in place of $$v_\pi(s)$$. We will have \
&#x20;$$<(S_1, G_1), (S_2, G_2),...(S_T, G_T)>$$ , which will be ou training data.&#x20;

Hence using linear Monte-carlo policy evaluation, algorithm will be:

$$
\triangle w = \alpha (G_t-\hat{v}(s_t,w))x(s_t)
$$

**Monte-Carlo evaluation will converge to a local optimum.  Even with non-linear value funtion approximation.**&#x20;

### **TD Learning with value funtion approx.**

The TD-target $$R_{t+1} + γ v̂ (S_{t+1} , w)$$ is a biased sample of true value $$v_\pi(s_t)$$**.**&#x20;

Supervised learning can be applies using traingin data: $$<(S_1, R_2 + γ v̂ (S_2 , w)), (S_2, R_3 + γ v̂ (S_3 , w)),...(S_{T-1}, R_T)>$$

$$
\triangle w = \alpha (R_{t+1} + γ v̂ (S_{t+1} , w)-\hat{v}(s_t,w))x(s_t)
$$

Linear TD(0) coverges(close) to global optimum.&#x20;

### TD() with value funtion approximation.&#x20;

The λ-return $$G_t^λ$$ is also a biased sample of true value $$v_\pi(s_t)$$

Apply Supervised learning with following data: $$<(S_1, G_1^\lambda), (S_2, G_2^\lambda),...(S_T, G_T^\lambda)>$$

Forward View linear TD():

$$
\triangle w = \alpha (G_t^\lambda-\hat{v}(s_t,w))x(s_t)
$$

Backward view linear TD():

$$
\delta_t = R_{t+1} +  γ v̂ (S_{t+1} , w)-\hat{v}(s_t,w)\\
E_t = \gamma \lambda E_{t-1} + x(S_t)\\
\triangle w = \alpha \delta_t E_t
$$

Forward and backward view llinear TD() are equivalent.&#x20;

## Incremental Control Algorithms

Policy Evalutaion: Approximate policy evaluation: $$\hat{q}(.,.,w)  \approx q_\pi$$ \
Policy Improvement : $$\epsilon-greedy$$ policy improvement

Here

$$
J(w) = E_\pi[(q_\pi(S,A,w)-\hat{q}(S,A,w))^2]
$$

$$
\triangle w = \alpha (q_\pi(S,A,w)-\hat{q}(S,A,w))\triangle_w \hat{q}(S,A,w)
$$

### Linear approximation:

![](<../../.gitbook/assets/image (122).png>)

$$
\hat{q}(s,a,w) = x(s,a)^Tw = \sum x_j(s,a)w_j
$$

### Algorithms

Now we have to substitute a target for $$q_\pi(S,A)$$&#x20;

**MC:** The taget wiill be return $$G_t$$&#x20;

$$
\triangle w = \alpha (G_t-\hat{q}(S,A,w))\triangle_w \hat{q}(S,A,w)
$$

**TD(0):** The target is TD target $$R_{t+1} + γ \hat{q} (S_{t+1}, A_{t+1} , w)$$

$$
\triangle w = \alpha (R_{t+1} + γ \hat{q} (S_{t+1}, A_{t+1} , w)-\hat{q}(S,A,w))\triangle_w \hat{q}(S,A,w)
$$

**Same goes with forward and backward view TD(lambda).**

![Sarsa Control with action-value funtion approximation](<../../.gitbook/assets/image (129).png>)

### Gradient Temporal-Difference Learning



## Batch Methods

### Least Square Prediction

Given value function $$\hat{v}(s,w)$$ approximation amd experience D consisting of \<state, value> pairs. $$D = \{<s_1, v_1^\pi>,<s_2, v_2^\pi>,...<s_t, v_t^\pi>\}$$&#x20;

Learning paramters w for the best fitting value funtion$$\hat{v}(s,w)$$.

Least-square algorithm: find $$w$$ minimizing the least square error between apprx funtion and target values.&#x20;

$$
LS(w) = \sum_{t=1}^T(v_t^\pi - \hat{v}(s_t,w))^2 \\
=E_D[(v^\pi-\hat{v}(s,w))^2]
$$

#### SGD with experience replay

* Sample state, value from experience\
  &#x20;$$<s,v^\pi> \sim D$$
* Apply SGD update\
  &#x20;$$\triangle w = \alpha (v^\pi-\hat{v}(s,w))\triangledown_w\hat{v}(s,w)$$

This converges to least square solution

$$
w^\pi = arg \min_w LS(w)
$$

#### Experience Replay in Deep Q-Networks

![Deep Q network using experience replay](<../../.gitbook/assets/image (130).png>)

### Least Square Control

#### Least square Action-Value Function Approximation

Approximate action-value funtion.&#x20;

Minimize least square error between $$\hat{q}(s,a,w)$$ and $${q}_\pi(s,a,w)$$ from experiences generated using policy $$\pi$$ consisting of <(state, actoin), value> pairs $$D = \{<(s_1,a_1), v_1^\pi>,<(s_2,a_2), v_2^\pi>,...<(s_t,a_t), v_t^\pi>\}$$

![](<../../.gitbook/assets/image (93).png>)

![](<../../.gitbook/assets/image (147).png>)

![](<../../.gitbook/assets/image (51).png>)
