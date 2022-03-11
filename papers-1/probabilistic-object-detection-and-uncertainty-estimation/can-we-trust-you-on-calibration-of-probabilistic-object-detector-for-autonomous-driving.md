---
description: >-
  This papaer discusses the idea of caliberating the probability which is used
  in proababilistic object detector
---

# Can We Trust You? On Calibration of Probabilistic Object Detector for Autonomous Driving

****[**https://arxiv.org/abs/1906.02530**](https://arxiv.org/abs/1909.12358)****

### Summary

This paper discusses the idea of calibrating the uncertainty/probabilities predicted in the probabilistic object detectors. They show three methods for calibration namely - isotonoic regression, temperature scaling and calibration loss.&#x20;

#### What is meant by calibrated probability?

So, It is said to be calibrated probability if the predicted probability is equal to the empiriacal probabililty. For ex, if detector makes prediction with 0.9 probability, then 90% of those prediction should be correct. Hence, the uncertainty of detector should match the natural frequency.

![](<../../.gitbook/assets/image (81).png>)

### Uncertainty Recalibration

#### Isotonic Regression

Let $$p=F_r(y_r)$$be the predicted probability from the network. In this we learn an auxiliary model based on isotnoic regression $$p \rightarrow g(p)$$. So basically we learn a model $$g(.)$$. We learn the model based on recalibration dataset which comes from validation dataset.  The recalibration dataset is defines as $${(F_r^n(y_r^n), \hat{P}(F_r(y_r)))}_{n=1}^N$$ where N is total length of validation dataset and $$\hat{P}(F_r(y_r))$$refers to the empirical probability. **See the paper as how the empirical probability is calculated.**

#### Temperature Scaling

Simply, $$\hat{\sigma} \leftarrow \sigma^2 / T$$, where learn the optimal value of $$T$$based on the Negative log liklihood score on the recalibration dataset.

#### Calibration Loss

$$
L_{calib} = || \sigma_x^2 - (y-u_x) \cdot (y-u_x) ||
$$

Just add this calibration loss to the original regression loss.&#x20;

### Conclusion

* The isotonic regression performs better than the other two and all three performs better than uncalibrated vanilla probabilistic detectors.&#x20;



\
\
&#x20;&#x20;
