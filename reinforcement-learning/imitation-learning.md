# Imitation Learning

## Behaviour Cloning

It is simple the supervised learning of state and action pair. State is the input and action is the output.&#x20;

### Problems with imitation learning

*   We have a demonstration data distribution called $$D = P(\tau)$$, now lets day we trained an algorithm on $$D$$ , now say we run the algo then the algo will make an error which will lead to obsevations which are not in the training data, and in that case the error will keep on increasae.  **Error Explode**\


    <img src="../.gitbook/assets/image (6).png" alt="Once state deviates from training, the error exploes and state keep deviating" data-size="original">\
    \
    Let us say that out learnt policy is $$\pi_{\theta}(a_t|o_t)$$ , now what above means is $$p_{data}(o_t) \neq p_\pi(o_t)$$ . \
    \
    Hence we solve this problem, we have find a way to make $$p_{data}(o_t) = p_\pi(o_t)$$
* For same state, there might be different actions in the training data.&#x20;
* If something new state comes up, that might not be in the training data.&#x20;
* Training data may not have correct action for given state, then the training will also be wrong as it is simple behaviour cloning. Hence, performance is bounded by the ability of person collecting the data.&#x20;
* Problems associated with supervised learning i.e. saddle points, convergence, etc. &#x20;
* Humans are not good at demonstration for everything. Ex: You demonstrate how to drive a car, but may not be able to demonstrate the movement of all joints for a humanoid. Hence, collecting human training data for every kind of problem is not possible. &#x20;

### Solution for error explode problem.&#x20;

*   Here in the above image, they have left and right camera, so basically they also training data with left and right image pair with corrected action. Hence when a vehicle drift out, training data have samples similar to those. Hence, it will be able to correct the trajectory of the vehicle. \
    In general terms, we can add noise to out collected distribution to create more training data along with corrected actions for the noise. Hence in this way, we will have an algorithm trained on data, such that it can correct itself when go wrong.

    ![](<../.gitbook/assets/image (42).png>)\
    https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf
* **DAgger: Dataset Aggregation**\
  If run it for long enough and some assumptions are true, then this is guaranteed to work. \
  IT solves the problem of distributional drift. &#x20;

![](<../.gitbook/assets/image (150).png>)

* If your model is so perfect that it doesn't make mistakes, then it is safe to assume that there will be no distributional shift and behaviour cloning will directly work.&#x20;

### Problem with data collection in Imitation Learning

* **Non-Markovian Behaviour:**\
  While collecting data, driver take action not only based on current state but the previous states. \
  Hence, for two same state, there may be different actions due to different history. \
  **Solution:** Instead of taking action based on current state, take previous states also into consideration. Hence take previous states also in the input. \
  You can **RNN** for including the temporal dimension.&#x20;
*   **MultiModal Behaviour:**\
    Different actions for same state in training data. \
    **Solution:** \
    For discrete actions, it is not really a problem. Because at the softmax ouput, we can get probability mass as two equally probable actions.\
    For continuous actions, we generally ouput as gaussian distribution as we use MSE loss most of the times, \
    So, it gets difficult to output two equally probable actions. For this we can use&#x20;

    * **Output a mixture of Gaussians:**\
      Outputs N means, N variances, and N weights adding upto one. &#x20;

    ![Mixture of Gaussian](<../.gitbook/assets/image (96).png>)

    * **Latent Vairable Model:**\
      Inject some noise (random number) along with the input state
    * **Autoregressive Discretization:**\
      Discretize the continous n dimensional varibale into n variables.&#x20;



## Inverse RL

Find the reward function given the expert trajectories.&#x20;
