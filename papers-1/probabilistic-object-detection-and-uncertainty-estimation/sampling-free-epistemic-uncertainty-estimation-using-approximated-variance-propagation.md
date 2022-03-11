---
description: Proposed sampling free method for epistemic uncertainty prediction
---

# \*Sampling Free Epistemic Uncertainty Estimation using Approximated Variance Propagation

### Summary

Sampling free method for epistemic uncertainty estimation. There method is based on forward propagation of uncertainty through the network, for this you don't have to change the loss function or architecture of your model.&#x20;

### Methodology

* There method is based on the concept of error propagation. \


![](<../../.gitbook/assets/image (5).png>)

Here A and B are independent hence, $$\sigma_c^2 = (\frac{\partial f_1}{\partial A})^2 \sigma_A^2+(\frac{\partial f_1}{\partial B})^2 \sigma_B^2$$ and similarly for D. But since C and D are not indepedent, same can not be defined for E. So, we will have to use full covariance matrix of C and D. Writing everything in terms of full covariance matrix we get.&#x20;

$$
\textstyle \sum_{C,D} = J\sum_{A,B}J^T \\ 
\sum_E = (\frac{\partial}{\partial C}, \frac{\partial}{\partial D})^T f_3(C,D)
$$

Where $$J$$ is the Jacobian of the vector valued function $$f = (f_1(A,B), f_2(A,B))^T$$.&#x20;

* So basically, we will have dropout layers in the network, dropout layer introduces the variance in the output. These dropout or batchnorm layers are called noise-layer in the paper. These noise layers for ex dropout layer introduces the variance in the output by randomly on & off the connections.&#x20;
* Based on the above formulation of the propogation in the error, the error introduced by these noise layers is propagated to the output, which is said to be the uncertainty/variance of the output.&#x20;

### Insights/Discussion

* Said to be work at the level of MC dropout, which is considered to be a baseline for this.&#x20;
* _Something to be added about OOD samples.............................................._

### Points to be taken

* Combining this method for epistemic uncertainty along with uncertainty estmitation using traditional method will be a new method. This should allow us to get better results across datasets.&#x20;
* The localization of dropout layer within the archicteture is irrelevant for the quality of uncertainty estimation.&#x20;
