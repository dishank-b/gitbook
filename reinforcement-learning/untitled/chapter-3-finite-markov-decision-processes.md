# Chapter 3: Finite Markov Decision Processes

* You take a action a\_t at a time-step in state s\_t and in response to that action you get response(reward)  r\_t+1 just after that, in next time step and also get into new state s\_t+1.
* S0, A0, R1, S1, A1, R2, S2, A2, R3, . . .  this sequence defines a MDP.&#x20;
* Markov Property:- Future is independent of the past given the present.
* Finite MDP - Have finite element in S,A,R set
*

<div align="left">

<img src="../../.gitbook/assets/image (132).png" alt="p defines the dynamics of the MDP">

</div>

<div align="left">

<img src="../../.gitbook/assets/image (67).png" alt="State transition probabilities">

</div>

<div align="left">

<img src="../../.gitbook/assets/image (85).png" alt="reward">

</div>

![bellman recursive equation](<../../.gitbook/assets/image (134).png>)

