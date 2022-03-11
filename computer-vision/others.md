# Others



* **Robust Estimator :- It is used while model fitting when suppose there is line to be fit and there is a point which lies outside of normal points through line. Then that point add up large error and disturb the equation of line. There fore instead of minimizing error directly we minimize some other function of error so that it makes model robust of outliers (noise) points.**&#x20;
* **RANSAC :-  (This shit is way too coool...)**\
  **It is used for model fitting (line fitting), such that it ignores the outliers and make a correct model out of data points.**
  * **Algo :- Randomly picks some points, define the model using those points. Loop until you find best model (the one with most inliers.)**
  * **Minimal Set :- Smallest number of samples from which model can be fitted.**
  * ![](https://lh4.googleusercontent.com/\_pY7IyiWsW1nJVRLlWGZMWlHIfDalxpNwoGqr0j1Ui3SNq-0RSSZjG46\_jUft2bv24YC8F-Q4h--feY4B6rO\_HKvomCEgw-xZVe\_7lZfsqCD13RAXwWhN3CgSA0gbIHZnQN4Afrj)
  * **Here this threshold t is the parameter which we have to choose..**
  * ![](https://lh6.googleusercontent.com/SC10t5JCkamsc1c22rNr70GT1B3BR3BCYBwJdEGqfdqIR3J8YeiBhyo2W2ewepw5T0o-OsBvjmCflIqOBkpoQHHrTAadiztmoYS9Jnjh2lpw4r0wONYpWwa78RUfNfutNN4hKQ4U)
  * **For calculating value of N see video 367.**
* **Hence, We Use RANSAC For fitting the homography model using the features find in the two images.**

**Classification :-**&#x20;

**Principle Component Analysis :-**&#x20;

* [**http://www.cs.otago.ac.nz/cosc453/student\_tutorials/principal\_components.pdf**](http://www.cs.otago.ac.nz/cosc453/student\_tutorials/principal\_components.pdf) **- PCA Theory**
* **Principal components are directions vectors in feature space along which points have greater variance.**
* **These are used for dimensionality reduction. So suppose we have 1000 dimension vector, then we reduce it to only the dimensions in which the points varies the most.**&#x20;
* **Here the axis with most variance is first component and the one othogonal to it would be second component.**
* **The direction along the maximum of variance of data is the eigen vector of largest eigen value of data covariance matrix.**
* **Eigen Vectors of a Matrix are always Orthogonal to each other.**
* **Subtract the MEAN from data for it to work better.**

### &#x20;****&#x20;

### **Binary Morphology :-**&#x20;

* ![](https://lh4.googleusercontent.com/ZVDQZzAWRc8GrIG5etDVKjk8qNzE\_m0JJgvRHfnke4J8PQxntUuS-uBbSL7bJtad875uMMKSY7lXaNgOKKsZcyA2UVdSGEVAsJmQ90AMWuoblAuJ4qtUurUFjc83muhn9ZN0-aFw)
* **Connected Component analysis for finding blobs in binary images.**
* **Opening followed by closing us used to remove noise and connect the strcuture.**

**Homography**\
****

**The homography is a limited image transformation model, which in the case of general camera motion is only valid when the observed scene is planar, or the camera is orthographic. If the scene is non-planar, and the camera is perspective, then the homography is valid if the camera motion is limited to rotation only. The homography is not valid when the camera undergoes translational motion while observing a non-planar scene. Under these circumstances, homography will be valid only for some areas of the images, the areas for which the homography is not valid will appear to “move” in the motion compensated imagery, and will be falsely detected as moving objects.**\
****\
****

**Guided Image Filtering**\
****

**The guided filter can perform as an edge-preserving smoothing operator like the popular bilateral filter, but has better behavior near the edges. Derived from a local linear model, the guided filter generates the filtering output by considering the content of a guidance image, which can be the input image itself or another different image.**

**We demonstrate that the guided filter is both effective and efficient in a great variety of computer vision and computer graphics applications including noise reduction, detail smoothing/enhancement, HDR compression, im-**

**age matting/feathering, haze removal, and joint upsampling. Simple explicit linear translation-invariant (LTI) filters like Gaussian filter, Laplacian filter, and Sobel filter are widely used in image blurring/sharpening, edge detec-**

**tion, and feature extraction \[3]. The kernels of LTI filters are spatially invariant and independent of any image content. But in many cases, we may want to incorporate additional information from a given guidance image during the filtering process. For example, in colorization \[7] the output chrominance channels should have consistent edges with the given luminance channel; in image matting \[2] the output alpha matte should capture the thin structures like hair in the image.**\
****
