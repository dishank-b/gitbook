---
description: >-
  Describes the fundamental mathematics of tracking with explanation of Kalman
  Filter and Particle Filter
---

# Tracking

### Model for Tracking

#### State

State $$x(t)$$ is a vector of variable which denotes the system state at time $$t$$. For example state of system with a car on road along a axis can be defined by its position & velocity or by its position, velocity and acceleration.&#x20;

#### Observation

Many times, you does not have any information about the state of system but can only have some observation about it. Observation is generally denoted by $$y(t)$$or $$z(t)$$. Sometimes you can completely or partially observe the state of the system. For ex, in above example if can directly observe position & velocity then its fully observable and if you can observe either position or velocity then its partially observable. \
In case of object trackin, we consider object bouding boxes as its states $$x(t)$$and as we  can observe the image we call it the observation $$z(t)$$. But you will see that practically we consider x(t) as directly observable because we have using detectors we can directly get $$x(t)$$.

\
To understand this fully, we can draw parallel to control systems concept of state-space model:

$$
x(t+1) = Ax(x) + Bu(t) \\
y(t) = Cx(t) + Du(t)
$$

In this $$u(t)$$is the input to the system, which we can ignore in our computer tracking problem. So you can see that, our observation $$y(t)$$ directly depends upon the state $$x(t)$$.&#x20;

**Also, the above two equations are called transition model and observation model in our tracking literature.** As they denotes, how our model is gonna transition and what is the relation between bservation and state.&#x20;

![State and observation Diagram](../.gitbook/assets/untitled-diagram.png)

### Tracking: Prediction and Filtering

### Kalman Filter

### Particle Filter



### From the course course on Computer Vision

* **Prediction:-** \
  ****![](https://lh4.googleusercontent.com/Demu25ZEzS6egpxowbNv9jFustshMo-CLFdaVm5qHoKFdoT4qbh-E3EPgS\_oLWRDmowiYUFbKUBPu6tNppwvqqIkvRecnXDXUxsPml4SYsIsBTYhLZUrUQ2P-iizk25QIxWh2Je0)
* **Correction :-**\
  ****![](https://lh3.googleusercontent.com/utONDfYkUnkagI\_P7\_pkioUsS2L57WJ3JNClDrKIWXXHgsOnesBr37spJi0-Y7FbHDwhnFzW1BJCwWjjZvgUC6ShGi3Fn0khufRQKkN3w7VrD7b7TSW2pn0c8yevf8vNsP7ULSdY)
* **The Summary Video for 7B-L1 is very good for overall concept.**

**Kalman Filter:-**&#x20;

* **Linear Model:-**\
  **Linear Dynamics Model -** ![](https://lh4.googleusercontent.com/z1TL5liNUEuaTJyiLtUJtRE89xqC0410HQYT2fqiKcqSwBKi4hf2gLPuqN1LSGlCgYEpv1l7rL9VLzkteHOg3K-gAjoYtIhzXfkBrUXS\_b\_wW6H4Qe7RvXiqhuXw02zbnHRBrwJA)****\
  **Linear measurement model -** ![](https://lh5.googleusercontent.com/kiGAdtKO3OAGeDIYhWKMsmUF6qNMsBSFo93WA8sSduTdABsBW9lS2m9uu1tMNkFc0i8rVumn6EDRsKyAYr-OJTSHRN8eVn\_qKZbxLe1BeUHMuCi43PgiBdVGIV2uNtLKCmx5OU0c)
* ![](https://lh4.googleusercontent.com/iCvwB-dYFKRfm7dBIsZyNzeQAA3sbQ11t0k7ScZBss-s5y9LCNKPEhzdsHodCUBa3Kj2Sthup0SdNgoJkg6VQuEhE0PTsxzM16tVvv\_GVo0fJWQ7cstJtu9fwOHAaqZ807L6IdLO)
* **Tracking with Kalman Filter:-**\
  ****![](https://lh6.googleusercontent.com/t5RCdeJjlvS-csB726vvz\_Mvyk\_PG6USLeNRiIJ3nxybXT4v6ULD8WtbeQfxI5mfwYMG5zt2xVWWKZGi\_Y9IFgZ9MuD3IWTsSQzHuophg-dXXaEL4NP\_OeC8WGQhJ1uSx6zwpIx7) **** ![](https://lh6.googleusercontent.com/L3bRzaYVE7epHU\_ZwRdzsC8sOMidBiHgggWqxGJgp0OVY22\_DIoWoq\_or9BVB\_RBgHQKmtbROIMJaCdbuUItcWppXLAd9jSUtI2VHXeqtRJ9rzoIiLMBXElSb7aAClHLhii3cBm7)
* **Extended Kalman Filter is used for NON-LINEAR Models.**&#x20;

**Particle Filter**

* **Watch this for basic idea :-** [**https://youtu.be/aUkBa1zMKv4**](https://youtu.be/aUkBa1zMKv4) ****&#x20;
* **Note that they assume that MAP OF ENVIRONMENT IS KNOWN.**
* ![](https://lh6.googleusercontent.com/c3nw5RqL9KE-5mBONGh\_Y0pFoBaQcwLLZiFOp2nj8TzLcAuovS4jJJhoSYqOWlv0vgE8snvYSMFYLdCkgBK5\_mOWpo5f4VYAfXemtCQXzYUJCmN-1Cdy2mglJJGX0bpr6\_L1D9bL)
* **Bayes Filter :-**\
  ****![](https://lh3.googleusercontent.com/ylF0inTzWSwRZFLYDENrQz5LzsBekvYQp8FFXbp-88BgOcjAEUKPFhJGZFxULiJROnz4GJEacukrW5AxgXKie782g1IjfcWqVmVsM3qLmK9178BzZjHjBzQNNYMqOqLdS704nUor) **** ![](https://lh6.googleusercontent.com/7YdnDVQFHwq\_tEf0sk0OPqgbEZj\_3MDUkdDUavEJ-KZ30eQYtGLtffYISQdQIe7rcXODGwkJ7eBbVBLLXvsuW26Q2XukyEEMpDccWb8i\_Y5H0ZHMRW8DLx6Han-tVqswiCWHceuy)****\
  **Here P(z|x) is probability that if given particle at x then what is probability of measurement z at there.**\
  ****![](https://lh5.googleusercontent.com/3cVmLbLBPcMrTCFPiG7aY5FmbTBg2VWD2GypkQiVMGGp6Dz43skA6D\_9QLD7-K4FXH2l8taKSTcYbe\_2k6db0qRsMWSkYhw4M3W4Mn4YwbRn-NMemJykBmyY0\_RUOQOZljLiMXmk)
* ![](https://lh4.googleusercontent.com/Z3FdEKqvccFNkSQi4r\_pYKdqWa-lgr4\_061lQKljkzpBFA5Ihe2pTjvOtRsd5CbhJmQcbjJGG-tLK-LDAN1Pycd0zFqmVOO202WsCH6mrGm413wLG3BhttiRy8aGN9FS3LfHv8Ur)****\
  ****![](https://lh4.googleusercontent.com/oLHJQlUZ7Cdrqmkx2Ejd9jaH-870PrrBzXv\_APd1X9NVdIVD4NySxtG4czyqCxi-6oFtThw43IRkRzFqK7lq8vtyz6FaQf0fTKRxTuz0LiFkU2eIxFT7vhgZcizLOLdFgNVDihDG)****\
  ****![](https://lh3.googleusercontent.com/7qaeK5XJB0Zw6HQ8iXQ00brVIdFpU4L4jnGdfn1JG8iEhk5IW2pHZj1qbV\_A15GR3L\_X14D6WQkSTgp-H-07Oz9yzgyrvWZRs2rnRc3GoiRRmqdqISmcPtn6feTRDDfP2y9ZR6xE)****\
  ****![](https://lh4.googleusercontent.com/0o6u2jcteyighYyE3THBCvgBzrMhEvOEYmOeVBIYmCz3aUQQNAEJ90yy7QxT-yJ-bbcNmMaTbfwrqBrhnsV\_qC8pmSZo8EIpdLR5IKrbehQzvGQzxUelWR6vW6TdNAzkJS5DdcMP)****\
  ****![](https://lh3.googleusercontent.com/vvoDOHXzToDGlCWDr5ZgvoupNWNl6JB6p1dr-XiaV8ZCCBqLp8MVtEBsX2JHhBOfE8\_Xq4wqRcM5uZIsFP\_yaFwm-SUjDCNy0KBdJFrT4ko5KJQvjLz1XS5s0tuxOZRE0JfsJxsc)
* **7C - L2 - Very good for understanding robot motion using particle filters.**
* **9th video 7C-L3 particle filter for practical consideration is important.**
