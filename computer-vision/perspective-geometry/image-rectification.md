# Image Rectification

Image rectification is related to the multi-camera or stereo camera setting. When you have images from two camera, you need image rectification. Let's see what is this and how it's done.&#x20;

**Image rectification** is a transformation process used to project images onto a common image plane.

* It is used in [computer stereo vision](https://en.wikipedia.org/wiki/Computer\_stereo\_vision) to simplify the problem of finding matching points between images (i.e. the [correspondence problem](https://en.wikipedia.org/wiki/Correspondence\_problem)).
* It is used in [geographic information systems](https://en.wikipedia.org/wiki/Geographic\_information\_system) to merge images taken from multiple perspectives into a common map coordinate system.

### Why do we need rectification and What does it do

Finding point matches in stereo vision is restricted by [epipolar geometry](https://en.wikipedia.org/wiki/Epipolar\_geometry): Each pixel's match in another image can only be found on a line called the epipolar line. If two images are coplanar, i.e. they were taken such that the right camera is only offset horizontally compared to the left camera (not being moved towards the object or rotated), then each pixel's epipolar line is horizontal and at the same vertical position as that pixel. However, in general settings (the camera did move towards the object or rotate) the epipolar lines are slanted. Image rectification warps both images such that they appear as if they have been taken with only a horizontal displacement and as a consequence all epipolar lines are horizontal, which slightly simplifies the stereo matching process.

![](<../../.gitbook/assets/image (4).png>)

### Image Rectification Diagram

![](<../../.gitbook/assets/image (148).png>)

### Algorithm

![](<../../.gitbook/assets/image (47).png>)

![](<../../.gitbook/assets/image (145).png>)

![](<../../.gitbook/assets/image (82).png>)

{% embed url="http://www.cs.cmu.edu/~16385/s17/Slides/13.1_Stereo_Rectification.pdf" %}

