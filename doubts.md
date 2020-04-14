---
description: >-
  This page have list of some tricky doubts regarding theory concepts, or use of
  some functions in some libraries, etc.
---

# Silly mistakes and solutions

### Changing Image data type:

* It is said that image is uint8, i.e  0 to 255. Now as soon as I convert it to float does it value range from 0 to 1 or it change to 0.0 to 255.0? [http://scikit-image.org/docs/dev/user\_guide/data\_types.html](http://scikit-image.org/docs/dev/user_guide/data_types.html) Something like mentioned in the link.   [http://answers.opencv.org/question/13115/cannot-view-16-bit-grey-level-images/](http://answers.opencv.org/question/13115/cannot-view-16-bit-grey-level-images/)  - This shows how the value of the image should range in order to correctly show them using opencv.

### Momentum and decay for exponential moving average:

$$
movingMean_t = momentum*movingMean + (1-momentum)*value
$$

Generally $$momenum=0.9$$ .   
When using batch norm in tensorflow. _**layers.batchnorm\(\)**_ have momentum parameter with value _**0.99**_  which is right, but _**contrib.layers.batchnorm\(\)**_ have parameter decay with default value  _**0.999**_  which is alright , as here _**decay=momentum and not decay=1-momentum**_



