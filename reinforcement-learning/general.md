# General

## Discrete vs Continuous Action Space

Lets suppose you parametrize the policy using a neural network. Then the network will take state as input and ouput the action. 

If you have **discrete action space** then you can **use softmax at the output layer**. As this will allow you assign probability to individual actions.   
If you have **continuous action space**  then you can use reparametrization trick and then **output the mean and std dev** at the output layer of the network. Then using gaussian distribution of predicted mean and std dev, you can generate continuous actions.  

## Inverse Reinforcement Learning

Figuring goal using demonstration.

## POMDP: Partially Observable MDP

![](../.gitbook/assets/image%20%2822%29.png)



