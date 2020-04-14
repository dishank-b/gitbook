---
description: This papers shows where normal Conv fails.
---

# An intriguing failing of convolutional neural networks and the CoordConv solution

Paper : [https://arxiv.org/pdf/1807.03247.pdf](https://arxiv.org/pdf/1807.03247.pdf)

In this paper, author shows that when we try to learn the mapping from Cartesian coordinate to pixel in image, the convolution network fails i.e \[x,y\] -&gt; images with pixel at \[x,y\] painted. 

### The CoordConv layer

The proposed CoordConv layer is a simple extension to the standard convolutional layer.\The CoordConv layer can be implemented as a simple extension of standard convolution in which extra channels are instantiated and filled with \(constant, untrained\) coordinate information, after which they are concatenated channel-wise to the input representation and a standard convolutional layer is applied. Figure 3 depicts the operation where two coordinates, i and j, are added. Concretely, the i coordinate channel is an h×w rank-1 matrix with its first row filled with 0’s, its second row with 1’s, its third with 2’s, etc. The j coordinate channel is similar, but with columns filled in with constant values instead of rows. In all experiments, we apply a final linear scaling of both i and j coordinate values to make them fall in the range \[−1, 1\].



![Here i coordinate channel have 0th row filled with 0, 1st row filled with 1 and so on. Similarly, j coordinate channel have 0th column filled with 0 and 1st column fillled with 1 and so on ](../.gitbook/assets/image%20%2810%29.png)

Before conv was translation invarient, but as we are also giving coordinate information in form of channel in coordconv, they are not translation invarient. Hence, using cordconv can be useful when there is a mapping from image to coordinates or vice versa.  
CoordConv with weights connected to input coordinates set by initialization or learning to zero will be translation invariant and thus mathematically equivalent to ordinary convolution. If weights are nonzero, the function will contain some degree of translation dependence, the precise form of which will ideally depend on the task being solved.

This also sates that in object detection where output is coordinates of bounding box around object, using cord conv can increase the IoU by 24%.

### Conclusion:

Using coordConv can be very useful. It lets the filter know where are they in image and hence making it translation invariant. This propertly canbe useful when our input-output are related to coordinate and pixels. 

