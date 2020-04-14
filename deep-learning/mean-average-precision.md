---
description: What is mAP?
---

# Mean Average Precision

This one used threshold of object to make the PR curve. This one seem a very good explanation and clearing the doubts about some small competition dependent changes in the definition of mAP. 

{% embed url="https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3" %}

The one below uses ranking based on confidence score to make the PR cureve. 

{% embed url="https://medium.com/@jonathan\_hui/map-mean-average-precision-for-object-detection-45c121a31173" %}

AP is averaged over all categories or/and over different values of IoU. Traditionally, this is called “mean average precision” \(mAP\). 

[https://github.com/Cartucho/mAP/blob/master/main.py](https://github.com/Cartucho/mAP/blob/master/main.py) - Code for MAP

