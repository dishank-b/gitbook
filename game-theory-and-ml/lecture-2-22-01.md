# Lecture 2 - 22/01

{% embed url="https://docs.google.com/presentation/d/17xPJWGJeAWkIWI8x7L8zl7mIek681lGpn5MCnydFB2A/edit#slide=id.gab813e4041_0_0" %}



## Prisoner's Dilemma

If agents do not cooperate, the best (global) outcome possible is missed.

## COP 21 Game

* N governments
* 2 actions per states
  * Do not pollute (Cost = 3)
  * Pollute (cost=1 and +1 for everyone)

What is the equilibrium? &#x20;

## Multi-Player Game

* Siimultaneous move games
* n players, each player pick a **strat** and occurs a loss.

$$
l_k(s_1, ...s_n) = l_k(s_k, s_{-k})
$$

**Goal of the player: Minimize their loss**

## Zero-Sum Two-player Games

Zero-sum: $$\sum_{k=1}^n l_k = 0$$

n=2

Action for each players: $$i \in [n] = {1,....,n}$$ and $$j \in [m]$$

### Game

$$
\min_{i\in[n]} \max_{j \in [m]} l_{ij}
$$

### Mix strategies

For example in the game of rock-paper-scissor

We have probabilities over actions of each player as $$p=[p1, p2, .... p_n] \in \Delta_n$$and $$q=[q1,q2, ..., q_m]  \in \Delta_m$$

$$\Delta_n := {p \in R^n: p_1+...p_n=1, p_i >= 0}$$

Payoff: $$l(p,q):= E_{i\sim p, j \sim q} [l_{ij}] = p^TLq$$

**Game:** $$\min_{p\in \Delta_n} \max_{q \in \Delta_m} p^TLq$$

## **Nash Equilibrium of a Game**

**Best worst-case move**

$$
s^* \in \text{NASH}  \implies l_k(s^*_k, s^*_{-k}) \leq l_k(s_k, s^*_{-k}) \forall s
$$

#### **Theorem**&#x20;

Any game with a finite set of players and a finite set of strategies has a Nash equilibrium of mixed strategies.&#x20;

\`

