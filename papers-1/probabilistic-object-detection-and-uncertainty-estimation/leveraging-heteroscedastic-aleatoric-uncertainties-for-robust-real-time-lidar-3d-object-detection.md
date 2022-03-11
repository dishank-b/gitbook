# Leveraging Heteroscedastic Aleatoric Uncertainties for Robust Real-Time LiDAR 3D Object Detection

Link of paper: [https://arxiv.org/abs/1809.05590](https://arxiv.org/abs/1809.05590)

### Summary

* Proposes:  **Real time -  LiDAR 3D object Detection - alearotric uncertainties.**
* They also uses probabilistic 2 stage detector and model aleatoric uncertainties using additional auxiliary layers along with boudning box and classification layers. &#x20;

### Methodoly

* They transformed 3D point cloud to the bird's eye view and then pass it as the input to the network.&#x20;
* They used same base architecture as Faster RCNN.
* Added extra fully connected layers to output uncertainties, which is pretty standard.&#x20;

![](<../../.gitbook/assets/image (68).png>)

* **They also predict uncertainties for RPN network. Although the RPN predicted undercertainties is not been used further in the architecure i.e either with NMS or postprocessing, but it is used for RPN regression loss attenuation.**
* They regress $$\log \sigma^2$$instead of $$\sigma^2$$for numerical stability.&#x20;

![](<../../.gitbook/assets/image (87).png>)

### Insights/Discussion

* Aleatoric undertainties are self contained in the softmax scores for classification.&#x20;
* Aleatoric uncertainty increases loss robustness against noist data. i.e. if some one input have large $$\sigma$$then it will factor down the loss contribution in the total loss. Hence, it is said the using uncertainty helps to igmore the noisy label.&#x20;
* Modelling uncertainties in both of RPN and fast rcnn head gets better performance than uncertainty in only one of them.
* The RPN and Fast RCNN head uncertainties are highly correlated.&#x20;
* Far and occluded objects have higher uncertainties then near and easy objects.

### To be kept in Mind

* According to hypothesis, the objects which are occluded or distance should have higher uncertainty. Now, we should test that the variance which we learnt and call uncertainty, support this hypothesis or not?
* _No need to explicitely model classic aleatoric unceratinties, as they are self-contained from the softmax scores which follow the categorical distribution. ?_\
  _hecen , softmax scores can be used as measure of uncertainty for classification._&#x20;
* So instead of ingoring noisy labels, shouldn't it be something like that we can extract as much information from noisy samples as well.&#x20;
* We should try to use focal loss with two stage, which is opposite to ignoring outliers which have high variance.&#x20;

