---
description: >-
  BayesOD: A Bayesian Approach for Uncertainty Estimation in Deep Object
  Detectors
---

# BayesOD

Version1 - [https://arxiv.org/abs/1903.03838v1](https://arxiv.org/abs/1903.03838v1)

Version2 - [https://arxiv.org/abs/1903.03838v2](https://arxiv.org/abs/1903.03838v2)

## KeyPoints 

* Uncertainty measures such as covariance are outputs for boundign box regression and category classification. 
* MC dropout for Epistemic Uncertainty. Variance Regression for Aleatoric Uncertainty.
* Bayesian Inference to get posterior of bouding box using default anchor boxes as prior and bounding box regressor output as likelihood.
* NMS is replaced by Bayesian Inference to get final output.

## Uncertainty

#### Types:

* **Epistemic:** Epistemic uncertainty captures our ignorance about the models most suitable to explain our data. It is the uncertainty in the model’s parameters, usually as a result of the confusion about which model generated the training data, and can be explained away given enough representative training data points. **Basically it means, when we train out network it is possible that with somehwat different parameters we can get same output or error. Hence thier is set of models which can explain the data equally well. Hence the uncertainty that which model is the best of our task is Epistemic Uncertainty**
* **Aleatoric:** Uncertainty about the observation _y_ caused by a noisy data set _{x,y}._ It __results from the stochastic nature of the observed data, and persist in network output despite expanded training on additional data. **Basically it is the inherent noise which is always there when performing an experiment and collecting data.** 

#### Methods to measure uncertainty in neural networks:

* **Monte Carlo Dropout:**  Parameters are stochastically sampled through Monte-Carlo \(MC\) Dropout. The output detections of multiple stochastic runs are then clustered, and the sufficient statistics of the state distributions for every object instance are directly estimated from the cluster members. The main advantage of this formulation lies in treating the underlying structure of the deep object detector as a black box, allowing it to be applied to various architectures with little effort
* **Covariance Estimation:** Another way to estimate the uncertainty in object detection results is to directly provide estimates for the covariance matrix of the bounding box state B. These sampling free methods are usually faster than black box methods, since a single run of the deep object detector can estimate uncertainty.
* **\(Only for Object Detection\)Redundancy in the output of the deep object detector before NMS:** This method is only particulary for object detection using DL. They exploit redundancy in the output of the deep object detector before NMS to form spatially affiliated clusters of detection outputs, from which sufficient statistics for both object state distributions can be estimated.

## Formulation of BayesOD

BayesOD used RetinaNet as its object detection network. BayesOD made significant changes in the parts of formulation. But network architecture remains same. 

In the Formulation below following naming conventino is used:

* The bounding box state $$B$$ is modeled as a random variable drawn from a multivariate Gaussian distribution $$B ∼ N(µ, Σ)$$ , where $$µ ∈ R^n$$  is the distribution’s mean, and $$Σ ∈ R^{n×n}$$ is the distribution’s covariance matrix.
* the category state S is modeled as being drawn from a Categorical \(Multinoulli\) distribution $$S ∼ Cat(p1, . . . , pK)$$ , where $$p_k$$ describes the probability of the state $$S$$ being class $$k$$ written as $$p(S = ck)$$ .
* $$a_i$$ is an anchor associated with a portion of input scene denoted by $$x_i$$ 
* Output of per-anchor is denoted as: $$p(S|x_i, D, θ),  p(B|x_i, D, θ)$$ 
* Final output combine result of each anchor is: $$p(S|X, D, θ), p(B|X, D, θ)$$ - Joint where $$X$$ is the set of $$M$$ input scene portions $$[x_i | i = 1 . . .M]$$ associated with a single object instance.  **Generally we get from per-anchor to joint using NMS.**
* Note that throughout this section, outputs from the neural network are denoted with a ˆ. operator, and per-anchor variables are indexed with _i_. Variables not indexed with an _i_ represent accumulation over several anchors.

### Predicting uncertainty 

#### Epistemic Uncertainty

* To capture the epistemic uncertainty of a deep object detec- tion model, a prior distribution is imposed over its parameters θ to compute a posterior distribution $$p(θ|D)$$ over the set of all possible parameters given the training data.  A marginal distribution is then computed for every object state according to:

$$
p(\hat{y}_i|x_i, D) = \int_\theta p(\hat{y}_i|x_i, D,θ)p(θ|D)dθ
$$

where $$\hat{y}_i$$ is the output of the neural network, which can either be $$\hat{B}_i$$ or $$\hat{S}_i$$ for every anchor $$a_i$$ .

To calculate this marginal distribution, method in next point is used. 

* Uses Monte Carlo Dropout: MC dropout is MC sampling method for NN. Multiple inferences are done for single input with dropout enabled at test time.   Using the drawn samples, the sufficient statistics of the Gaussian marginal probability distribution describing the estimated bounding box state $$\hat{B}_i \sim N(\mu(x_i), \sum(x_i))$$ are estimated as follows:

$$
\mu(x_i) = \frac{1}{T}\sum_{t=1}^Tf(x_i, \theta_t) \\
\sigma_e(x_i) = \frac{1}{T}(\sum_{t=1}^Tf(x_i, \theta_t)f(x_i, \theta_t)^T) - \mu(x_i)\mu(x_i)^T
$$

where $$T$$ is the number of times MC-Dropout sampling is performed, and $$f(x_i, θ_t)$$ is the bounding box regression output of the neural network for the $$t^{th}$$ MC-Dropout run. The covariance matrix, $$\sigma_e$$ , captures the epistemic uncertainty in the estimated bounding box state $$\hat{B}_i$$.

*  Since the neural network outputs the parameters of a Categorical distribution rather than categorical samples, these parameters can be derived for the Categorical marginal con- ditional probability distribution $$\hat{S}_i ∼ Cat([\hat{p}_1 . . . \hat{p}_K])$$ as:

$$
\hat{p}_k = \frac{1}{T}\sum_{t=1}^T Softmax(g(x_i, \theta_t))_k
$$

where SoftMax\(.\) is the soft max function, and $$g(x_i, θ_t)_k$$ is the output logit of the $$k^{th}$$ category, estimated at the $$t^{th}$$ MC- Dropout run of the neural network.  
**Doubt: How do we get the class epistemic uncertainty here using these estimated categorical distribution parameters?**

#### **Aleatoric Uncertainty**

To capture aleatoric uncertainty for the bounding box state $$B$$ , the neural network is trained to estimate the elements of the diagonal of a per-anchor aleatoric covariance matrix $$\sigma_a(x_i)$$. The loss for _**every dimension**_ of the bounding box representation is modified as:

$$
L_{reg} = \frac{1}{N_{pos}} \sum_{i=1}^{N_{pos}}L(x_i) + \frac{1}{N_{neg}}\sum_{i=1}^{N_{neg}}\frac{1}{\sigma(x_i)^2} \\
L(x_i) = \frac{1}{2σ(x_i)^2} ||y_i − f(x_i)|| + \frac{1}{2}\log σ(x_i)^2
$$

where $$N_{pos}$$ is the number of positive anchors, $$N_{neg}$$ is the number of negative anchors. The first term of the proposed loss applied to the positive anchor set, while the second term encourages the model to increase the total variance of the bounding box state B of the negative anchors. The proposed modification is empirically found to provide better numeric stability while training with higher learning rates, and for a slightly more discriminative uncertainty measure over the original  
  
In the equation for $$L(x_i)$$ , $$y_i$$ is the ground truth regression target, \|\|.\|\| is an Lp norm. and $$σ(x_i)$$ is the estimated output variance. The first term of $$L(x_i)$$ serves as an intelligent robust regression loss, where the model is allowed to attenuate the effect of outliers in training examples by increasing their estimated variance. The second term acts as a regularizer, preventing the model from rejecting all training examples by always setting the variance to infinity. 

The aleatoric covariance matrix can then be constructed from the output regressed variances as: 

$$
\sigma_a(x_i) = diag([\sigma^1...\sigma^n]) \\
\sigma^j(x_i) = \frac{1}{T}\sum_{t=1}^T\sigma^j(x_i, \theta_t)
$$

Here n=4, which means bounding box have four dimension. where $$σ^j(x_i) $$ is the estimated variance of the $$j^{th}$$ element of the bounding box state B, at the $$t^{th}$$ MC-Dropout run of the neural network. The final output covariance $$\sigma(x_i)$$ of the state B can then be approximated as:

$$
\sigma(x_i) = \sigma_e(x_i) + \sigma_a(x_i)
$$

**Note: No aleatoric uncertainty were estimated for classification task. For reason give a read to:** [**https://arxiv.org/abs/1809.05590**](https://arxiv.org/abs/1809.05590)\*\*\*\*

### **Incorporating State Prior Distribution**

* Probablistically combine the per-anchor prior information to get the final estimate of state. 
* The per-anchor conditional posterior distribution describing the bounding box state B can be written as: $$p(B|x_i, D, \hat{B}_i) ∝ p( \hat{B}_i|x_ i, D, B)p(B|x_i)$$  where $$p( \hat{B}_i|x_ i, D, B)$$ is a Gaussian likelihood function described by the sufficient statistics $$ [µ(x_i), Σ(x_i)]$$ which is outputed by the network as shown [above](bayesod.md#epistemic-uncertainty).  $$p(B|x_i) ∼ N(µ_0, Σ_0)$$ is a predefined per-anchor prior distribution conditioned on the input $$x_i$$ and assumed to be independent of the data D. This prior basically equivalent to 9 defualt anchors which we choose.  
* Statistics for posterior are calculated using multivariate Gaussian conjugate update as:

$$
Σ'(x_i) = (Σ^{−1}_0 + Σ(x_i)^{−1})^{−1} \\
µ'(x_i) = Σ'(x_i)(Σ^{−1}_0 µ_0 + Σ(x_i)µ(x_i))
$$

* Similar techinque is applied with categorical distribution where Dirichlet function is used prior. Because after that posterior will also be Dirichlet. 

**Note: In above the prior is set as µ0 to the initial anchor position, and Σ0 to a matrix with large diagonal entries. This is actually not very informative prior for anchors and standard priors as have used in Retinanet or Faster RCNN. But if you find a way to ger informative prior for anchors, use them.**

### Bayesian Inference as a Replacement to **NMS**

* First clusters are formed over which Bayesian inference is performed rather than NMS to get the final output. Per-anchor outputs from the neural network are clustered using spatial affinity.
* **Clustering:** greedy clustering is performed using the output category scores $$[p_1', . . . , p_K']$$ , by choosing the anchor with the highest non-background score as the cluster center, adding any anchor with an intersection over union \(IOU\) greater than 0.5 to the cluster, and eliminating all members in the cluster from the original updated anchor set. The clustering process terminates when all updated anchors are assigned to a cluster, or when the number of clusters exceed a predefined number.
* The output of greedy anchor clustering is H anchor clusters, A, each containing an anchor set, \[a1, . . . , aM\]. M is not constant and can vary between clusters in the same frame. The first anchor, a1, has the highest score, and as such is considered the cluster center, and will be described with its posterior state distributions as calculated [above](bayesod.md#incorporating-state-prior-distribution).  We update the $$a_1$$bounding box using others in the cluster which is done as follows:

$$
p(B|X, D, [ \hat{B}_1, . . . , \hat{B}_M]) ∝ p(B|x_1, D, 
\hat{B}_1) \prod_{i=2}^M p( \hat{B}_i|x_i, D, B) \\
= N(µ''(X), Σ''(X))
$$

where X is the set of inputs \[xi \| i = 1 . . .M\] of the M cluster members. Also:

$$
Σ''(X) = (\sum_{i=1}^M Σ'(x_i)^{−1} )^{−1} \\
µ''(X) = Σ''(X)(\sum_{i=1}^M Σ''(xi)^{−1}µ'(x_i))
$$

* Similarly bayesian inference can be applied for category state $$S$$ .
* A major result from this subsection is that the two states of any object can be updated easily given an additional measurement from a different component of the robotic system using bayes theorem. 

![First: Proposed Anchor boxes, Second: Posterior with Proposed anchor boxes as prior and output from boundingbox regressor as liklihood,  Third: output after combining all outputs using bayesian inferencence inplace of NMS](../../.gitbook/assets/image%20%2860%29.png)

## Experiments and Results

Considered two classed of pedestrian and car only

### Metrics

* **Average Precision\(AP\)**: a standard metric used to evaluate the performance of object detectors. Throughout this section, AP is evaluated separately for the two categories at an IOU of 0.5.
* **Minimum Uncertainty Error \(MUE\):** used to determine the ability of an uncertainty measure to discriminate true positives from false positives, where a detection is determined to be a true positive if it has an IOU ≥ 0.5 with a same category ground-truth bounding box. False positives in this case could include poorly localized detections, or false detections result- ing from unknown unknowns. Hence:

$$
UE(\delta) = 0.5\frac{ |TP > δ|}{|TP|} + 0.5\frac{ |FP ≤ δ|}{|FP|}
$$

where δ is the uncertainty measure threshold. MUE is the best uncertainty error achievable by a detector at the best possible value of the threshold δ. The lowest MUE achievable by a detector is 0%.

* Gaussian MUE \(GMUE\) uses the entropy of the Gaussian distribution describing the state B as its uncertainty measure to be used to discriminate true positives from false positives. Similarly, Categorical MUE \(CMUE\) uses the entropy of the Categorical distribution describing the state S as its uncertainty measure.

### Results

BayesOD is seen to outperform all three methods on all performance metrics

Analysis as compared to other methods:

* For a meaningful uncertainty measure, the entropy, and hence the uncertainty in both states of a true positive should be lower than those of a false positive.
* For the Categorical entropy, all methods are shown to follow this intuitive trend to a certain extent.
* For the Gaussian entropy however, two of the three methods in the state of the art: Redundancy and Black Box result in exactly the opposite behaviour, where the mean of the Gaussian entropy of true positives is higher than that of the false positives.
* To hypothesise on why such behaviour occurs, one should observe the mechanism employed by these two methods to estimate the final covariance matrix of the state B. Both of these methods use the clustered output ofM stochastic runs to estimate a sample covariance matrix, with the only difference being that Black Box clusters the output of NMS, whereas Redundancy clusters the per-anchor output before NMS. Both of these methods lack adequate cluster merging, and explicit variance estimation, which reduces the discriminative power of their estimated uncertainty measure for the bounding box state B.
  * The first support for this hypothesis is that Sampling Free, a method that explicitly uses the per-anchor regressed covariance matrix, provides a 10.76% and 2.37% decrease in GMUE of the car and pedestrian categories over the second runner up from Black Box and Redundancy.

### Ablation Study

* Pushing the variance of negative anchors to increase during training provides a slightly more discriminative uncertainty in the bounding box state B.
* Explicit aleatoric covariance matrix estimation provides a slightly more discriminative uncertainty estimate of the bounding box state B.
* The gains in performance on CMUE can be explained through the per-anchor marginalization over neural net- work parameters. 
* Greedy Non-Maximum Suppression is detrimental to the discriminative power of the uncertainty in the bounding box state B.

## Resources

{% file src="../../.gitbook/assets/reading\_group\_bayesod\_july\_19\_2019.pdf" %}

