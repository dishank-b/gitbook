# Gaussian YOLOv3

Link of paper - [https://arxiv.org/abs/1904.04620](https://arxiv.org/abs/1904.04620)

### Summary

Integrated uncertainty prediction with YOLOv3. Hence they have real-time one-stage object detection with uncertainty. They use two benchmark BDD and Kitti. 

### Methodology 

* The YOLOv3 has three predictions boxes per grid cell, where each prediction box consists of bbox coordinated, objectness scores, class scores. The object is detected using product of class and object score. 
* **The localization uncertainty of box which is predicted in the proposed method, can be used as bbox score, which will be used for how uncertain the bbox is. So, we will have objectness score, class score and bbox score.**  Note: The objectness score does not reflect the reliability of bbox, hence doesn't denote the uncertainty of the box
* For training, they use the negative log liklihood loss for regression. Whereas for objectness and class, the loss doesn't change. 
* The proposed algorithm applies localization uncertainty for the detection criteria such that bbox with uncertainty is filtered through the detection process.  $$Cr = \sigma(Object) \times \sigma(Class_i) \times(1-Uncertainty_{aver}) $$ 
* **They use different IOU threshold for different classes such as 0.7 for cars, 0.5 cyclist and pedestrian.  - This can be usefull, as I am getting less recall in normal faster rcnn. This can be useful.** 
* Anchor size is extracted using K-means clustering for each training set. 

### Insights/Discussions

* They plot IOU vs uncertainty for car objetcs. They found that as the uncertianty decreases IOU increase. Hence car objects with lower uncertainty  have better IOU. Hence prediction is closer to GT.  So, predicted uncertainty is good to represent confidence of prediction and used to detect false positives.
* Better results than normal YOLOvs. 
* They claim to increase the True Positives and significantly reducing the False Positive. 

