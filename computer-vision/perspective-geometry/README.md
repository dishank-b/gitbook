# Projective Geometry

## **Camera Model and Parameters**

* **World Frame: a fixed coordinate system for representing objects \(points, lines, surfaces, etc.\) in the world.**
* **Camera Frame: coordinate system that uses the camera center as its origin \(and the optic axis as the Z-axis\)**
* **Image or retinal plane: plane on which the image is formed, note that the image plane is measured in camera frame coordinates \(mm\)**
* **Image Frame: coordinate system that measures pixel locations in the image plane.**
* **Intrinsic Parameters: Camera parameters that are internal and fixed to a particular camera/digitization setup. Allow a mapping between camera coordinates and pixel coordinates in the image frame\`.**
* **Extrinsic Parameters: Camera parameters that are external to the camera and may change with respect to the world frame. Define the location and orientation of the camera with respect to the world frame.**

## Homogenous Representation

![](../../.gitbook/assets/image%20%2827%29.png)

Each point  `(x,y)` in the image is actually a ray in 3D world, the ray can be reresented as `(kx, ky,k)` and when `k=1` it gives the point in the image.   
Get it like this, all the point on the ray in the 3D world will be at the same point on image. Also, that ray will through the center of the camera.   
Hence homogenous representation is basically way to denote the 2D point in image. 

#### Example:

Lets consider three points $$x=[6,9,3]$$ , $$y=[12,18,6]$$ and `z=[2,3,1]` in 3D world, these 3 points lie on the same ray passing through the origin. So, basically all these three point will be at map to same point in the image plane. And the point $$z$$ is the point which lie exactly at the image plane. Hence so given a point $$ (x,y)$$ in the image place, it can map to any point $$(kx, ky,k)  \forall k$$ and this is called **projective space.**

## **Homography**

![](../../.gitbook/assets/image%20%28123%29.png)

Homography is the condition when image of same plane is taken with two different position. There is a mapping between two points $$x$$ and $$x'$$ in both images respectively which represent the same point $$X$$ in the 3D world. This mapping between coordinates of the image of same plane is called **Homography.**

### **Matrix**

![](../../.gitbook/assets/image%20%28102%29.png)

* The homography preserves the colliniearity of points. i.e. if three points are collinear in one image then they will be collinear even after the homography. 
* Since $$H$$ and $$kH$$ will be same here, hence numper of unknown in $$H$$ are 8 and not 9.
* Since 8 unknowns, hence we will need 4 corresponding points to find the $$H$$

## Camera Geometry/Single View Geometry

### Camera Model

![](../../.gitbook/assets/image%20%2855%29.png)

### Projection Matrix: From 3D to image coordinates

![](../../.gitbook/assets/image%20%2871%29.png)

![](../../.gitbook/assets/image%20%2885%29.png)



![](../../.gitbook/assets/image%20%287%29.png)

![](../../.gitbook/assets/image%20%28124%29.png)

* **This is important as it can be used to find relation between 3D world and 2D image.**
* ![](https://lh5.googleusercontent.com/mRwOBoL8tsjyvA6T48uX2tAFXOdfYL-uE1qu-BDyKBfzQRHZNzj5Ctp7HROX58ZXpIDGzjas7Yb2lwwZdugotlfyk_ziqZMjZXMJbUfG5KPrH2jEfx7L62KOfd9Mgxivyp4Dxa3l)
* **Here x,y,z are coordinate in 3D world and u,v are coordinate of those points in image.** ![](https://lh3.googleusercontent.com/-52L-VrPHn6Aj3QOy32dXQdFwUF7n9H9KfsWunOPoBXeQ2KcD5YUgPhRRCQjdTgI7ZtoZg--JXbjUq-8o2DrqQOJeVb2ytxLfgIdnXAy-nP77zRP21XrsTP96Bd4nULBF8fFATqT)
* ![](https://lh4.googleusercontent.com/7fP0DB2CrHsAmYQC0Jr-y55qdKFbpHv1p7IBPSQ6BesMdG1JaQSeANatAJGh9OFwrwtNBVqEnF-wksbcOxx28NKfMmnuWY1M1GBHXWVEaaISj3Bt274f8oRJF8gh_7k_poT9WEIQ)  **Therefor all pairs of parallel lines in 3D world meet at a point in image.**
* **Depth From Stereo For these we need following information:-**
  * **Info about relative position and orientation of two cameras wrt each other.**
  * **Point correspondence in two images from camera.**
* ![](https://lh5.googleusercontent.com/7LAcEggdVMdr04IJkRRkWDBGRSGqmht5NSqwNoZtNwZzI3J_3xTcmw6_lFSPdt2X_DfVhZFdAt_YOnip5FP4ncPgmD2Vhq4ZSG0gnIumPEGxd6c2RItos195up9geER-Fad_5g8a)
* ![](https://lh4.googleusercontent.com/Bv5b_1P486ore3GM91afYGI_vxZn8HqxXBtAUroL_FqaxCVPftYoMgJtlc5shnHr8HnWoEbTvMEpItrwm23tJ6_X3vnO9neB2vZouWkmutx8ODhXubt76OWBT-uBkc4jwlFmjoEN)
* **Lectures 200-205 are important.**
* **Lecture 219-227 are for extrinsic geometry of camera\(Camera-world transform.\)**
* **Intrinsic Matrix:-** ![](https://lh4.googleusercontent.com/DH6EiNf5zrlSGVMy0canoA0RF2DWMfymrvNbsHSunNLCG3-Z-vH-tmJ6AOZIyyC9_BapC7t11EI_OO4laG66_7eFiZxGcBVRFAg58b-qxkq31QGxntgui86R3iGa8LPbQwtLUO7q)  **\(u,v\) are pixel coordinate in image.**
* **Essential Matrix is a geometric constraint between world coordinate of point in image taken by different camera position. X\`EX = 0.  X\` and X are vector of point in two camera coordinate system. The E matrix is composed of Rotation and Translation Matrix between two camera coordinate system.**

**Fundamental Matrix defines the relation of a point in two image coordinates.  
P\`FP=0, Where P and P\` are coordinates of a point in two images.Fundamental Matrix is composed of Extrinsic & Intrinsic Parameters. F matrix is always singular.  
Hence F matrix is sufficient to find corresponding point in two images taken from different camera position and from different camera intrinsics.  
  
Also Homographies are also used as relation between two planes of images. Therefore, fundamental matrix and homography matrix has some relation between them.**  


