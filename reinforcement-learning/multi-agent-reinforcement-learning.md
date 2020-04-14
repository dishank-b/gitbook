---
description: About Multi Agent Reinforcement Learning
---

# Multi Agent Reinforcement Learning

MARL have more complex framework which is generalisation of the Markov decision process, it is called Stochastic or Markov Games.

### Markov Games:

A Markov game is a tuple $$(n, S, A_1, ..., A_n, T, R_1, ..., R_n)$$ where:

• n is the number of agents  
• S = {S1, ..., SN} is a finite set of environment states,   
• Ak is the action set of player k,   
• T : S ×A× S → \[0, 1\] is the state transition probability function,   
• Rk : S ×A× S → R is the reward function of player k. Where

Where Ak\(si\) denotes the set of actions available to agent k when it is in state i. Consequently, the reward function Rk and the transition probability T also depend on this state si, on the next state sj, and on a joint action ai = \(ai 1, ...ai n\) from this state. The reward of agent k for their action in time step t is thus rk,t+1 = Rk\(si, ai, sj\). The expected return as we defined in the introduction changes in the same way; it is now also dependent on the joint action ai.

### Types:

* Based on Cooperation
  * Fully Cooperative - there is no conflict between the agents’ goals, which is the case when they all have the same reward function
  * Fully Competitive - the agents have completely conflicting goals \(e.g. opposite re- ward functions\)
  * Mixed - the setting is neither fully cooperative nor fully competitive: there is no constraint on the reward function.
* Based on Observability
  * Independent Learners - Agents do not observe each other. This does not change the fact that other agents’ actions could influence the environment, but it will be considered as noise.
  * Joint action learners - where agents actually observe each other. 

