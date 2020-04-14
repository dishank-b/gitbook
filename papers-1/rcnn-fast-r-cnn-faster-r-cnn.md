---
description: Explaining different object detection papers
---

# Object Detection

**Resources:**

* [https://lilianweng.github.io/lil-log/2017/12/31/object-recognition-for-dummies-part-3.html](https://lilianweng.github.io/lil-log/2017/12/31/object-recognition-for-dummies-part-3.html)
* [https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html\#retinanet](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html#retinanet)
* [https://medium.com/@jonathan\_hui/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359](https://medium.com/@jonathan_hui/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359) 
* [https://medium.com/@jonathan\_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088](https://medium.com/@jonathan_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088)
* [https://towardsdatascience.com/deep-learning-for-object-detection-a-comprehensive-review-73930816d8d9](https://towardsdatascience.com/deep-learning-for-object-detection-a-comprehensive-review-73930816d8d9)

## RCNN

Benchmarked on PASCAL VOC 2012. **MAP: 53.3%**

### **Funda:**

* Region proposals using **Selective Search\(SS\)**
  * **2000** proposals per image
* CNN over the proposals to output feaure vector of each proposal
* There is a set of class-specific linear SVMs. 
  * Each feature vector is passed through each of the class specific SVMs. 
  * Hence the feature vector is **scored** for each class using SVM of that class.
* Afterwards, **greedy non-maximal Suppresion** is applied\(independently for each class\) for final object Detection.
  * **For each class:**
    * **it rejects a region\(proposal\) if it has IOU overlap with a higher scoring region larger than a learned threshold**



![](../.gitbook/assets/image%20%2851%29.png)

### KeyPoints:

* **Warping:** Each proposal is reshaped to fixed dimension as CNN needs all input to be of same shape. 
* **Fine-Tuning:** The second principle contribution of this paper is to show that supervised pre-training on a large auxiliary dataset \(ILSVRC\), followed by domain- specific fine-tuning on a small dataset \(PASCAL\), is an effective paradigm for learning high-capacity CNNs when data is scarce.
* **Hard Negative Mining:** The hard negative examples are easily misclassified. We can explicitly find those false positive samples during the training loops and include them in the training data so as to improve the classifier.

### Training

They use all the independent models here without any shared computation and training, hence **training is multi-stage:**

* Selective Search - For Region Proposals
* CNN - For feature represenation for regions
* SVM - for classification
* Bounding Box Regressor - To get tighter bounding box.

**Advice: Consider the CNN and SVM as two different entities to be trained independently. With CNN we only need to learn feaure representation and with SVM we need to learn category classification using the learned feature representation.** 

#### Fine Tuning the CNN

* Last layer of CNN was classification layer\(softmax\) with \(N+1\) output classes. 1 is for backgroud and N is num of classes.
* Region proposals with ≥ 0.5 IoU overlap with a ground-truth box are labelled as positives for that box’s class and the rest as negatives.
* In eafch SGD iteration, we uni formly sample 32 positive windows \(over all classes\) and 96 background windows to construct a mini-batch of size 128. Means 32 regions proposal with 96 background windows.

#### Object Category Classifier \(SVM\)

* Regions with less 0.3 IoU overlap with annoated box were labelled negative. Positive examples are defined simply to be the ground-truth bounding boxes for each class.
* Once features are extracted and training labels are applied, we optimize one linear SVM per class.
* They used hard negative mining here. 

**Note: Discuss why positive and negative regions were labelled differently for fine tuning CNN and training SVM.** 

## **Fast R-CNN**

### Architecture:

* The whole image is passed through the CNN and then at the output we have a feature map. 
* Here also we have region proposals as in RCNN. **Now a region proposal in image is mapped to corresponding feature vector in output feaure map and the fixed-length feature vector is extracted using region of interest\(RoI\) pooling layer, from the feature map.** 
* Feature vector is passed through couple of fully connected layers which then divided into two branches: one outputs softmax probability for K+1 output classes and another layer that outputs four real-valued numbers for each of the K object classes. Each set of 4 values encodes refined bounding-box positions for one of the K classes.
* Non Max Suppresion in the last

![](../.gitbook/assets/image%20%2816%29.png)

#### RoI Pooling Layer- It is just a single max pool layer

The RoI pooling layer uses max pooling to convert the features inside any valid region of interest into a small fea- ture map with a fixed spatial extent ofH×W \(e.g., 7 × 7\). An RoI is a rectangular window into a conv feature map. Hence each region proposal in image is mapped to RoI in conv feature map. Each RoI is defined by a four-tuple \(r, c, h,w\) that specifies its top-left corner \(r, c\) and its height and width \(h,w\)  
  
-&gt; Lets say you have region proposal of say 50x50 in the image, this say becomes 20x20 into feature map. Now this 20x20 is max pooled using RoI layer to 7x7.   
Hence even if region of proposals are of differnt size, we get contant size feature represemataion \(HxW\). 

It is a type of max pooling to convert features in the projected region of the image of any size, h x w, into a small fixed window, H x W. The input region is divided into H x W grids, approximately every subwindow of size h/H x w/W. Then apply max-pooling in each grid.

![](../.gitbook/assets/image%20%28147%29.png)

### Training

They used pre-trained networks to initializing the training

#### **Finetuning**

In Fast R- CNN training, stochastic gradient descent \(SGD\) mini- batches are sampled hierarchically, first by sampling N im- ages and then by sampling R/N RoIs from each image. Critically, RoIs from the same image share computation and memory in the forward and backward passes. Making N small decreases mini-batch computation. For example, when using N = 2 and R = 128, the proposed training scheme is roughly 64× faster than sampling one RoI from 128 different images \(i.e., the R-CNN and SPPnet strategy\).

#### **Loss**

The first ****output layer outputs a discrete probability distri- bution \(per RoI\), $$p = (p_0, . . . , p_K)$$ , over K + 1 categories.  
The second sibling layer outputs bounding-box regression offsets, $$t^k = ( t^k_x , t^k_y , t^k_w, t^k_h ) $$ , for each of the K object classes, indexed by k.  


Each training RoI is labeled with a ground-truth class u and a ground-truth bounding-box regression target v. We use a multi-task loss L on each labeled RoI to jointly train for classification and bounding-box regression:

$$
L(p,u,t^u,v) = L_{cls}(p,u) + \lambda [u\geq1]L_{loc}(t^u, v) \\
L_{cls}(p,u) = -\log p_u
$$

\[u ≥ 1\] evaluates to 1 when u ≥ 1 and 0 otherwise. By convention the catch-all background class is labeled u = 0.

$$
L_{loc}(t_u, v) = \sum smooth_{L1}(t^u_i − v_i)
$$

$$
smooth_{L1}(x) = \begin{cases}0.5x^2 & |x| < 1\\|x|-0.5& otherwise\end{cases}
$$

#### Mini-Batch Sampling

During fine-tuning, each SGD mini-batch is constructed from N = 2 images, chosen uni- formly at random \(as is common practice, we actually iter- ate over permutations of the dataset\). We use mini-batches of size R = 128, sampling 64 RoIs from each image. As in RCNN, we take 25% of the RoIs from object proposals that have intersection over union \(IoU\) overlap with a ground- truth bounding box of at least 0.5. These RoIs comprise the examples labeled with a foreground object class, i.e. u ≥ 1. The remaining RoIs are sampled from object pro- posals that have a maximum IoU with ground truth in the in- terval \[0.1, 0.5\), following \[11\]. These are the background examples and are labeled with u = 0. The lower threshold of 0.1 appears to act as a heuristic for hard example mining \[8\]. During training, images are horizontally flipped with probability 0.5. No other data augmentation is used.

## Faster RCNN

### Resources

* [https://tryolabs.com/blog/2018/01/18/faster-r-cnn-down-the-rabbit-hole-of-modern-object-detection/](https://tryolabs.com/blog/2018/01/18/faster-r-cnn-down-the-rabbit-hole-of-modern-object-detection/)
* [http://www.telesens.co/2018/03/11/object-detection-and-classification-using-r-cnns/\#ITEM-1455-2](http://www.telesens.co/2018/03/11/object-detection-and-classification-using-r-cnns/#ITEM-1455-2) - better dimensional understanding
* [https://towardsdatascience.com/fasterrcnn-explained-part-1-with-code-599c16568cff](https://towardsdatascience.com/fasterrcnn-explained-part-1-with-code-599c16568cff)

Both region proposal generation and objection detection tasks are all done by the same CNN. 

This papers main contribution is to a CNN network called RPN \(region proposal network\) to generate region propsals instead of an dedicated region proposal algorithm such Selective Search which takes lot computation time. 

**Faster RCNN = RPN + Fast RCNN**

**They introduce novel “anchor” boxes that serve as references at multiple scales and aspect ratios.**

### Pipeline

![Faster-RCNN block diagram. The magenta colored blocks are active only during training. The numbers indicate size of the tensors.](../.gitbook/assets/image%20%28113%29.png)

![Pipeline](../.gitbook/assets/image%20%2811%29.png)

![pipeline](../.gitbook/assets/image%20%2838%29.png)

### **Architecture**

Faster R-CNN, is composed of two modules. The first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector that uses the proposed regions. ****The entire system is a single, unified network for object detection. The RPN tell Fast RCNN where to look. 

Network wise we have three:

* Feaure Network: A network such as VGG which converts a image to a corresponding feature map
* RPN: Generate Region Proposals which were earlier done using selective search in Fast RCNN
* Detection Network: It detects objects in the image using the generated feature map from featuer network and proposals generated from RPN. It is basically same as last part of Fast RCNN. 



![](../.gitbook/assets/image%20%2837%29.png)

#### Region Proposal Network \(RPN\)

A Region Proposal Network \(RPN\) takes an feature map \(of any size\) as input and outputs a set of rectangular object proposals, each with an objectness score.

Just assume the output of RPN to be as same of Selective Search\(SS\) in case of Fast RCNN. It just gives the region proposals. The regions proposals are described in RPN by its coordinate and objectiveness - does proposal contains an object or background.   
  
To generate region proposals, we slide a small network over the convolutional feature map output by the last shared convolutional layer - this is the last layer of feature network. This small network takes as input an n × n spatial window of the input convolutional feature map. Each sliding window is mapped to a lower-dimensional feature \(256-d for ZF and 512-d for VGG, with ReLU \[33\] following\). This feature is fed into two sibling fully- connected layers—a box-regression layer \(reg\) and a box-classification layer \(cls\). We use n = 3 in this paper, noting that the effective receptive field on the input image is large. This mini-network is illustrated at a single position in Figure below. Note that be- cause the mini-network operates in a sliding-window fashion, the fully-connected layers are shared across all spatial locations. This architecture is naturally im- plemented with an n×n convolutional layer followed by two sibling 1 × 1 convolutional layers \(for reg and cls, respectively\).

![RPN architecture](../.gitbook/assets/image%20%28116%29.png)

**Anchors:**

Every ‘pixel’ of the feature image is considered an anchor. Each anchor corresponds to a larger set of squares of pixel in the original image. 

At each sliding-window location in feature map, we simultaneously predict k region proposals. So the reg layer has 4k outputs encoding the coordinates of k boxes, and the cls layer outputs 2k scores that estimate probability of object or not object for each proposal. The k proposals are parameterized relative to k reference boxes, which we call **anchors boxes**. An anchor box is centered at the sliding window \(see above figure\), and is associated with a scale and aspect ratio. By default we use 3 scales and 3 aspect ratios, yielding k = 9 anchors at each sliding position. For a convolutional feature map of a size W×H \(typically ∼2,400\), there are WHk anchors in total.  
_The input that is required from the feature generation layer to generate anchor boxes is the shape of the tensor, not the full feature tensor itself_.

**It’s important to understand that even though anchors are defined based on the convolutional feature map, the final anchors reference the original image.** Description as follows:  
Since we only have convolutional and pooling layers, the dimensions of the feature map will be proportional to those of the original image. Mathematically, if the image was $$w \times h$$ , the feature map will end up $$w/r \times h/r$$ where $$r$$ is called _subsampling ratio_. If we define one anchor per spatial position of the feature map, the final image will end up with a bunch of anchors separated by rr pixels. In the case of VGG, **r = 16**.

[https://medium.com/@andersasac/anchor-boxes-the-key-to-quality-object-detection-ddf9d612d4f9](https://medium.com/@andersasac/anchor-boxes-the-key-to-quality-object-detection-ddf9d612d4f9)

**Multi-Scale Anchors as Regression References:**

There anchor-based method is built on a pyramid of anchors, which is more cost-efficient. Our method classifies and regresses bounding boxes with reference to anchor boxes of multiple scales and aspect ratios. It only relies on images and feature maps of a single scale, and uses filters \(sliding windows on the feature map\) of a single size. 

#### NMS - Non maximum Supression

In the fist step of reduction an operation called Non-Maximum Suppression \( NMS\) is used. NMS removes boxes that overlaps with other boxes that has higher scores \( scores are unnormalized probabilities , e.g. before softmax is applied to normalize\). About 2000 boxes are extracted during training phase \( the number is lower, about 300 for testing phase\). In the testing phase these boxes along with their scores go straight to the Detection Network. In the training phase the 2000 boxes are further reduced through **sampling** to about 256 before entering the Detection Network.

**Note:** There is region sampling even after NMS during training phase. Which samples regions from all the regions to go in the training. 

#### Detection Network \(Fast RCNN Part\)

This is detection network is the last part from Fast RCNN paper, part including the RoI pooling year and ahead. This network used the feature map from feature network and region proposals generated from RPN. Having the feature map and proposal, it applied RoI pooling and further outputs the final classes and bouding boxes.

**ROI Pooling:**

![](../.gitbook/assets/image%20%2834%29.png)

Crop the convolutional feature map using each proposal and then resize each crop to a fixed sized $$14 \times 14 \times \mathit{convdepth}$$ using interpolation \(usually bilinear\). After cropping, max pooling with a 2x2 kernel is used to get a final $$7 \times 7 \times \mathit{convdepth}$$feature map for each proposal.

![](../.gitbook/assets/image%20%28107%29.png)

\*\*\*\*

### Training

#### **For training RPNs** 

* **Classification:**  We assign a binary class label \(if object is in the region or not\) to each bouding box \(anchor box\). We assign: _Positive:_ ****label to two kinds of anchors: \(i\) the anchor/anchors with the highest Intersection-over- Union \(IoU\) overlap with a ground-truth box, or \(ii\) an anchor that has an IoU overlap higher than 0.7 with any ground-truth box. Usually the second condition is sufficient to determine the positive samples; but we still adopt the first condition for the reason that in some rare cases the second condition may find no positive sample.  _Negative_**:** to a non-positive anchor if its IoU ratio is lower than 0.3 for all ground-truth boxes.  Anchors that are neither positive nor negative do not contribute to the training objective.
* **Bounding Box regression:   
  T**o tighten the center and the size of the anchor boxes around the target.  
  This can be thought of as bounding-box regression from an anchor box to a nearby ground-truth box. In regession we map an input to an output. Here our input is coordinates of anchor box and output is coordinated of target.    
  
  **Bounding Box Regression Parameterization:**  
  The distance vector from the center of the ground truth box to the anchor box is taken and normalized to the size of the anchor box. That is the target delta vector for the center. The size target is the log of the ratio of size of each dimension of the ground truth over anchor box.  


  Variables $$x$$ , $$x_a$$ ****, and $$x^*$$ are for the predicted box, anchor box, and ground- truth box respectively. Basically $$x_a$$ is input, $$x$$ is output, $$x^*$$ is target output.  
  **It’s important to understand that even though anchors are defined based on the convolutional feature map, the final anchors reference the original image.** 



$$
t_x = \frac{x − x_a}{w_a}, t_y = \frac{y − y_a}{h_a} \\
t_w = log(w/w_a), t_h = log(h/h_a), \\ 
t_x^* = (x^∗ − x_a)/w_a, t^∗_y = (y^∗ − y_a)/h_a, \\
t^∗_w = log(w^∗/w_a), t^∗_h = log(h^∗/h_a)
$$

**Doubt:**   
Are these coordinates wrt to the original image or wrt to the feature map we obtain after backbone?  
**Ans:**   
[https://stackoverflow.com/questions/44259578/faster-rcnn-how-to-translate-coordinates](https://stackoverflow.com/questions/44259578/faster-rcnn-how-to-translate-coordinates)  
**All these coordinates are computed with respect to the original image. Hence these** $$x, x_a, x^*$$ are all referenced on the image size and not the feature map size.

Loss is same as to one used in _Faster RCNN_ .

$$
L(p_i,t_i) = \sum_iL_{cls}(p_i,p_i^*) + \lambda \sum_i p_i^*L_{reg}(t_i, t_i^*)
$$

**Nevertheless, our method achieves bounding-box regression by a different manner from previous RoI- based \(Region of Interest\) methods say Fast RCNN. In Fast RCNN bounding-box regression is performed on features pooled from arbitrarily sized RoIs, and the regression weights are shared by all region sizes. In our formula- tion, the features used for regression are of the same spatial size \(3 × 3\) on the feature maps. To account for varying sizes, a set of k bounding-box regressors are learned. Each regressor is responsible for one scale and one aspect ratio, and the k regressors do not share weights. As such, it is still possible to predict boxes of various sizes even though the features are of a fixed size/scale, thanks to the design of anchors.**

**Minibatch Sampling to Train RPN:** The RPN can be trained end-to-end by back- propagation and stochastic gradient descent \(SGD\) \[35\]. We follow the “image-centric” sampling strategy from Fast RCNN to train this network. Each mini-batch arises from a single image that contains many positive and negative example anchors. It is possible to optimize for the loss functions of all anchors, but this will bias towards negative samples as they are dominate. Instead, we randomly sample 256 anchors in an image to compute the loss function of a mini-batch, where the sampled positive and negative anchors have a ratio of up to 1:1. If there are fewer than 128 positive samples in an image, we pad the mini-batch with negative ones.

#### Detection Network Training

The Detection Network can be considered the removed layers \(top \) of the classification network that is used for features generation. Hence the starting weights can be pre-loaded from that network before training.

Training the Detection Network is similar to that of RPN. First, IOUs of all the 2000 or so ROIs generated by the NMS following RPN against each ground truth bounding box is calculated. Then the ROIs are labeled as foreground or background depending on the corresponding threshold values. Then a fixed number \( e.g. 256 \) ROIs are selected from the foreground and background ones. If there are not enough foreground and/or background ROIs to fill the fixed number, then some ROIs are duplicated at random.

The features are cropped \( and scaled \) to 14x14 \(eventually max-pooled to 7x7 before entering the Detection Network \) according to the size of the ROIs \(for this, ROI width and heights are scaled to the feature size\). Fig 4 shows examples of ROIs overlaid on the feature image. The set of cropped features for each image are passed through the Detection Network as a batch.The final dense layers output for each cropped feature, the score and bounding box for each class \( e.g. 256 x C, 256x4C in one-hot encoding form, where C is the number of classes\) .

To generate label for Detection Network classification, IOUs of all the ROIs and the ground truth boxes are calculated . Depending on IOU thresholds \( e.g. foreground above 0.5 , and background between 0.5 and 0.1\), labels are generated for a subset of ROIs. The difference with RPN is that here there are more classes. Classes are encoded in sparse form, instead of one-hot encoding. Following a similar approach to the RPN target generation, bounding box targets are also generated. However, these targets are in the compact form as mentioned previously, hence are expanded to the one-hot encoding for calculation of loss.

#### Training RPN and Detection at same time

Possible Methods:

* **Alternating training:** In this solution, we first train RPN, and use the proposals to train Fast R-CNN. The network tuned by Fast R-CNN is then used to initialize RPN, and this process is iterated. This is the solution that is used in all experiments in this paper.
* **Approximate joint training:** In this solution, the RPN and Fast R-CNN networks are merged into one network during training as in Figure 2. In each SGD iteration, the forward pass generates region propos- als which are treated just like fixed, pre-computed proposals when training a Fast R-CNN detector. The backward propagation takes place as usual, where for the shared layers the backward propagated signals from both the RPN loss and the Fast R-CNN loss are combined. This solution is easy to implement. But this solution ignores the derivative w.r.t. the proposal boxes’ coordinates that are also network responses, so is approximate. In our experiments, we have em- pirically found this solver produces close results, yet reduces the training time by about 25-50% comparing with alternating training. This solver is included in our released Python code.

In this paper, we adopt a pragmatic 4-step training algorithm to learn shared features via alternating optimization. In the first step, we train the RPN as described in Section 3.1.3. This network is initialized with an ImageNet-pre-trained model and fine-tuned end-to-end for the region proposal task. In the second step, we train a separate detection network by Fast R-CNN using the proposals generated by the step-1 RPN. This detection network is also initialized by the ImageNet-pre-trained model. At this point the two networks do not share convolutional layers. In the third step, we use the detector network to initialize RPN training, but we fix the shared convolutional layers and only fine-tune the layers unique to RPN. Now the two networks share convolutional layers. Finally, keeping the shared convolutional layers fixed, we fine-tune the unique layers of Fast R-CNN. As such, both networks share the same convolutional layers and form a unified network.

### Implementation

* For anchors, we use 3 scales with box areas of 1282, 2562, and 5122 pixels, and 3 aspect ratios of 1:1, 1:2, and 2:1.
* The anchor boxes that cross image boundaries need to be handled with care. During training, we ignore all cross-boundary anchors so they do not contribute to the loss. For a typical 1000 × 600 image, there will be roughly 20000 \(≈ 60 × 40 × 9\) anchors in total. With the cross-boundary anchors ignored, there are about 6000 anchors per image for training. If the boundary-crossing outliers are not ignored in training, they introduce large, difficult to correct error terms in the objective, and training does not converge. During testing, however, we still apply the fully convolutional RPN to the entire image. This may generate cross- boundary proposal boxes, which we clip to the image boundary.
* Some RPN proposals highly overlap with each other. To reduce redundancy, we adopt non-maximum suppression \(NMS\) on the proposal regions based on their cls scores. We fix the IoU threshold for NMS at 0.7, which leaves us about 2000 proposal regions per image. As we will show, NMS does not harm the ultimate detection accuracy, but substantially reduces the number of proposals. After NMS, we use the top-N ranked proposal regions for detection. In the following, we train Fast R-CNN using 2000 RPN pro- posals, but evaluate different numbers of proposals at test-time.

### Ablation Study

#### Scale and Ratio of Anchor boxes

![](../.gitbook/assets/image%20%28144%29.png)

**With 3 scales and 3 ratios, 69.9% mAP is obtained which is only little improvement over that of 3 scales and 1 ratio.** But still 3 scales and 3 ratios are used.

### Doubts:

* As we can see that Detection Network and RPN have similar losses and outputs. And the training for both is similar.  So can we ignore detection network altogether and instead of RPN having two clasess\(object and no object\), we train it for C classes of the actual classification. 

### Limitations:

* All these RCNN based objects only take regions to find the objects in it. They dont use complete image at once to localize object. 
* Not exactly real-time. Altough FasterRCNN can still be run at **5 FPS** normally, and may be more if tweakings are done. 

### Resources

{% embed url="https://towardsdatascience.com/fasterrcnn-explained-part-1-with-code-599c16568cff" %}

* Tuning Anchor boxes:  [https://medium.com/@andersasac/anchor-boxes-the-key-to-quality-object-detection-ddf9d612d4f9](https://medium.com/@andersasac/anchor-boxes-the-key-to-quality-object-detection-ddf9d612d4f9)

## Mask RCNN \([Paper](https://arxiv.org/pdf/1703.06870.pdf)\)

Mask R-CNN \([He et al., 2017](https://arxiv.org/pdf/1703.06870.pdf)\) extends Faster R-CNN to pixel-level [image segmentation](https://lilianweng.github.io/lil-log/2017/10/29/object-recognition-for-dummies-part-1.html#image-segmentation-felzenszwalbs-algorithm). The key point is to decouple the classification and the pixel-level mask prediction tasks. Based on the framework of [Faster R-CNN](https://lilianweng.github.io/lil-log/2017/12/31/object-recognition-for-dummies-part-3.html#faster-r-cnn), it added a third branch for predicting an object mask in parallel with the existing branches for classification and localization. The mask branch is a small fully-connected network applied to each RoI, predicting a segmentation mask in a pixel-to-pixel manner. 

### RoIAlign

Because pixel-level segmentation requires much more fine-grained alignment than bounding boxes, mask R-CNN improves the RoI pooling layer \(named “RoIAlign layer”\) so that RoI can be better and more precisely mapped to the regions of the original image.

The RoIAlign layer is designed to fix the location misalignment caused by quantization in the RoI pooling. RoIAlign removes the hash quantization, for example, by using x/16 instead of \[x/16\], so that the extracted features can be properly aligned with the input pixels. [Bilinear interpolation](https://en.wikipedia.org/wiki/Bilinear_interpolation) is used for computing the floating-point location values in the input.

### Loss Function

The multi-task loss function of Mask R-CNN combines the loss of classification, localization and segmentation mask where $$L_{cls}$$ and $$L_{box}$$are same as in Faster R-CNN.

The mask branch generates a mask of dimension $$m \times m$$  for each RoI and each class; $$K$$ classes in total. Thus, the total output is of size $$K⋅m^2$$ . Because the model is trying to learn a mask for each class, there is no competition among classes for generating masks.

$$L_{mask}$$ is defined as the average binary cross-entropy loss, only including k-th mask if the region is associated with the ground truth class 

$$
L_{mask}=\frac{−1}{m^2}∑_{1≤i,j≤m}[y_{ij}\log (\hat{y}^k_{ij})+(1−y_{ij})log⁡(1−\hat{y}^k_{ij})]
$$

where $$y_{ij}$$ is the label of a cell \(i, j\) in the true mask for the region of size $$m \times m$$ ; $$ŷ^k_{ij}$$ is the predicted value of the same cell in the mask learned for the ground-truth class k.

## RCNN Family in 1 figure

![RCNN Family Architecture](../.gitbook/assets/image%20%2899%29.png)

## YOLO: You look only once \([Paper](https://arxiv.org/abs/1506.02640)\)

### Limitations

* The limitation of YOLO algorithm is that it struggles with small objects within the image, for example it might have difficulties in detecting a flock of birds. This is due to the spatial constraints of the algorithm.

## RetinaNet \([Paper](https://arxiv.org/abs/1708.02002)\)

### Contribution

* Focal Loss: Paper states that the difference reason that the one stage detectors lags behind two stage detectors is because of the **foreground-background class imabalnce** during training. Hence they use Focal Loss which modify Cross entropy loss by down-weights the loss assigned to well-classified examples. 
* Paper states that: RetinaNet is able to match the speed of pervious one-satge detectors while surpassing the accuracy of all existing state-of-art two-stage detectors. **They emphasis that increase performance of RetinaNet is not due to novel architecture change but due to novel loss function.** 

### Focal Loss

The loss function is a dynamically scaled cross entropy loss, where the scaling factor decays to zero as confidence in the correct class increases. Intuitively, this scaling factor can automati- cally down-weight the contribution of easy examples during training and rapidly focus the model on hard examples.

**Focal loss proves to be better than its alternative techniques such as sampling heuristic and hard example mining**. 

#### Cross Entropy

One notable property of **CE loss**, which can be easily seen in its plot, is that even examples that are easily classified \( $$p >> 0.5$$ \) incur a loss with non-trivial magnitude. i.e when a model able to classify a easy example, then not much loss should be incurred but in CE even with high confidence, loss incurred is significant. 

$$
CE(p,y) = \sum y\log(p)
$$

#### Balanced Cross Entropy

A common method for addressing class imbalance is to introduce a weighting factor α ∈ \[0, 1\] for class 1 and 1−α for class −1. In practice α may be set by inverse class frequency or treated as a hyperparameter to set by cross validation.

$$
CE(p,y) = \sum_t \alpha_t y_t\log(p_t)\\\sum_t \alpha_t = 1
$$

While α balances the importance of positive/negative examples, it does not differentiate between easy/hard examples. Hence, for that we need focal loss.

#### Focal Loss Definition

Reshape the Cross Entropy function to down-weight easy examples and thus focus training on hard negatives.

$$
FL(p_t) = -(1-p_t)^\gamma\log(p_t)
$$

Here $$(1-p_t)^\gamma$$ is a weighting factor used to down-weight the easy classified examples. $$\gamma$$ is a tuned hyperparameter. In actual experiments, they have used $$\alpha $$   
balanced version of focal loss. This provide imporved results. 

$$
FL(p_t) = -\alpha_t(1-p_t)^\gamma\log(p_t)
$$

### Model Initialization in case of Class Imbalance

Binary classification models are by default initialized to have equal probability of outputting either y = −1 or 1. Under such an initialization, in the presence of class imbal- ance, the loss due to the frequent class can dominate total loss and cause instability in early training. To counter this, we introduce the concept of a ‘prior’ for the value of p es- timated by the model for the rare class \(foreground\) at the start oftraining. We denote the prior by π and set it so that the model’s estimated p for examples of the rare class is low, e.g. 0.01. We note that this is a change in model initializa- tion \(see §4.1\) and not of the loss function.  
**Question:** How do they actually implement this prior?   


### Architecture

RetinaNet composed of three sub networks:

* BackBone - Feature Pyramid Network 
  * Used for computing the feature map of entire map.
  * Mainly a off-the-shelf convolutional network. 
* Two Task specific networks
  * one subnetwork performs convolutional object classification. 
  * second is used for bounding box regression

![Architecture](../.gitbook/assets/image%20%28119%29.png)

#### FPN Backbone

In brief, FPN augments a stan- dard convolutional network with a top-down pathway and lateral connections so the network efficiently constructs a rich, multi-scale feature pyramid from a single resolution input image. Each level of the pyramid can be used for detecting objects at a different scale.

![FPN architecture \(taken from FPN paper\)](../.gitbook/assets/image%20%2847%29.png)

**In RetinaNet, they build FPN on top of ResNet**  
RetinaNet uses feature pyramid levels P3 to P7, where P3 to P5 are computed from the output of the corresponding ResNet residual stage \(C3 through C5\) using top-down and lateral connections just as in original FPN, P6 is obtained via a 3×3 stride-2 conv on C5, and P7 is computed by apply- ing ReLU followed by a 3×3 stride-2 conv on P6. This differs slightly from original FPN: \(1\) we don’t use the high-resolution pyramid level P2 for com- putational reasons, \(2\) P6 is computed by strided convolution instead of downsampling, and \(3\) we include P7 to improve large object detection.

#### Anchors

We use translation-invariant anchor boxes simi- lar to those in the RPN variant in \[20\]. The anchors have areas of 322 to 5122 on pyramid levels P3 to P7, respec- tively. As in \[20\], at each pyramid level we use anchors at three aspect ratios {1:2, 1:1, 2:1}. For denser scale cover- age than in \[20\], at each level we add anchors of sizes {20, 21/3, 22/3} of the original set of 3 aspect ratio anchors. This improve AP in our setting. In total there are A = 9 anchors per level and across levels they cover the scale range 32 - 813 pixels with respect to the network’s input image. Each anchor is assigned a length K one-hot vector of classification targets, where K is the number of object classes, and a 4-vector of box regression targets. We use the assignment rule from RPN \[28\] but modified for multi- class detection and with adjusted thresholds. Specifically, anchors are assigned to ground-truth object boxes using an intersection-over-union \(IoU\) threshold of 0.5; and to back- ground if their IoU is in \[0, 0.4\). As each anchor is assigned to at most one object box, we set the corresponding entry in its length K label vector to 1 and all other entries to 0. If an anchor is unassigned, which may happen with overlap in \[0.4, 0.5\), it is ignored during training.  
**\[20\] = FPN paper, \[28\] = Faster RCNN paper  
  
A surprisingly good AP \(30.3\) is achieved using just one square anchor. However, the AP can be improved by nearly 4 points \(to 34.0\) when using 3 scales and 3 aspect ratios per location.** 

#### **Classification SubNetwork**

The classification subnet predicts the probability of object presence at each spatial position for each of the A anchors and K object classes. This subnet is a small FCN attached to each FPN level; parameters of this subnet are shared across all pyramid levels. Its design is simple. Taking an input feature map with C channels from a given pyramid level, the subnet applies four 3×3 conv layers, each with C filters and each followed by ReLU activations, followed by a 3×3 conv layer with KA filters. Finally sigmoid activations are attached to output the KA binary predictions per spatial location, see Figure 3 \(c\). We use C = 256 and A = 9 in most experiments.

#### **Bounding Box Regressor SubNetwork**

In parallel with the object classi- fication subnet, we attach another small FCN to each pyra- mid level for the purpose of regressing the offset from each anchor box to a nearby ground-truth object, if one exists. The design of the box regression subnet is identical to the classification subnet except that it terminates in 4A linear outputs per spatial location**.**

### **Implementation and Training**

* To improve speed, we only decode box predictions from at most 1k top-scoring predictions per FPN level, after threshold- ing detector confidence at 0.05. The top predictions from all levels are merged and non-maximum suppression with a threshold of 0.5 is applied to yield the final detections. Focal
* When training RetinaNet, the focal loss is applied to all ∼100k anchors in each sampled image. This stands in contrast to common practice of using heuristic sampling \(RPN\) or hard example mining \(OHEM, SSD\) to select a small set of anchors \(e.g., 256\) for each minibatch. The total focal loss of an image is computed as the sum of the focal loss over all ∼100k anchors, normalized by the number ofanchors assigned to a ground-truth box. We per- form the normalization by the number of assigned anchors, not total anchors, since the vast majority of anchors are easy negatives and receive negligible loss values under the focal loss.
* We experiment with ResNet-50-FPN and ResNet-101-FPN backbones \[20\]. The base ResNet-50 and ResNet-101 models are pre-trained on ImageNet1k; we use the models released by \[16\]. New layers added for FPN are initialized as in \[20\]. All new conv layers except the final one in the RetinaNet subnets are initialized with bias b = 0 and a Gaussian weight fill with σ = 0.01. For the final conv layer of the classification subnet, we set the bias initializa- tion to b = −log\(\(1 − π\)/π\), where π specifies that at the start of training every anchor should be labeled as fore- ground with confidence of ∼π. We use π = .01 in all ex- periments, although results are robust to the exact value. As explained, this initialization prevents the large num- ber of background anchors from generating a large, desta- bilizing loss value in the first iteration of training.



## Comparison

Parameters that impact detector performance:

* Feature extractors \(VGG16, ResNet, Inception, MobileNet\) - **BackBone network**
* Output strides for the extractor. - **?**
* Input image resolutions.
* Matching strategy and IoU threshold \(how predictions are excluded in calculating loss\).
* Non-max suppression IoU threshold.
* Hard example mining ratio \(positive v.s. negative anchor ratio\).
* The number of proposals or predictions.
* Boundary box encoding.
* Use of multi-scale images in training or testing \(with cropping\).
* Which feature map layer\(s\) for object detection.
* Localization loss function.

### Benchmarking 

[https://medium.com/@jonathan\_hui/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359](https://medium.com/@jonathan_hui/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359) -   
**Wonderfull post for benchmarking of different object detection models.**

<table>
  <thead>
    <tr>
      <th style="text-align:left">Method</th>
      <th style="text-align:center">Dataset</th>
      <th style="text-align:center">Image size</th>
      <th style="text-align:center">mAP</th>
      <th style="text-align:center">FPS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">Faster RCNN</td>
      <td style="text-align:center">VOC 07 + 12</td>
      <td style="text-align:center">1000x600</td>
      <td style="text-align:center">70.4</td>
      <td style="text-align:center">
        <p>7 - VGG</p>
        <p>17 - ZF</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">SSD</td>
      <td style="text-align:center">07+012</td>
      <td style="text-align:center">
        <p>512x512</p>
        <p>300x300</p>
      </td>
      <td style="text-align:center">
        <p>76.8</p>
        <p>74.3</p>
      </td>
      <td style="text-align:center">
        <p>19</p>
        <p>46</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">
        <p>YOLO</p>
        <p>YOLOv2
          <br />YOLOv3</p>
      </td>
      <td style="text-align:center">
        <p>07+12</p>
        <p>07+12</p>
        <p><em>MS COCO</em>
        </p>
      </td>
      <td style="text-align:center">
        <p>448x448</p>
        <p>544x544</p>
        <p>416X416</p>
      </td>
      <td style="text-align:center">
        <p>63.4</p>
        <p>78.6</p>
        <p><em>31.0</em>
        </p>
      </td>
      <td style="text-align:center">
        <p>45</p>
        <p>40</p>
        <p>35</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">RetinaNet-101</td>
      <td style="text-align:center"><em>MS COCO</em>
      </td>
      <td style="text-align:center">500x500</td>
      <td style="text-align:center"><em>34.4</em>
      </td>
      <td style="text-align:center">11</td>
    </tr>
  </tbody>
</table>Bottomline is:

* Region based detectors like Faster R-CNN demonstrate a small accuracy advantage if real-time speed is not needed.
* Single shot detectors are here for real-time processing. But applications need to verify whether it meets their accuracy requirement.

### Google Comparision

[**https://arxiv.org/pdf/1611.10012.pdf?source=post\_page---------------------------**](https://arxiv.org/pdf/1611.10012.pdf?source=post_page---------------------------)  
**This is paper from google which compared Speed and Accuracy Trade-offs for Faster RCNN, RFCN and SSD. Must Read**

![Image from the paper](../.gitbook/assets/image%20%2853%29.png)

### Lessons learned

Some key findings from the Google Research paper:

* R-FCN and SSD models are faster on average but cannot beat the Faster R-CNN in accuracy if speed is not a concern.
* Faster R-CNN requires at least 100 ms per image.
* Use only low-resolution feature maps for detections hurts accuracy badly.
* Input image resolution impacts accuracy significantly. Reduce image size by half in width and height lowers accuracy by 15.88% on average but also reduces inference time by 27.4% on average.
* Choice of feature extractors impacts detection accuracy for Faster R-CNN and R-FCN but less reliant for SSD.
* Post processing includes non-max suppression \(which only run on CPU\) takes up the bulk of the running time for the fastest models at about 40 ms which caps speed to 25 FPS.
* If mAP is calculated with one single IoU only, use mAP@IoU=0.75.
* With an Inception ResNet network as a feature extractor, the use of stride 8 instead of 16 improves the mAP by a factor of 5%, but increased running time by a factor of 63%.

Most accurate

* The most accurate single model use Faster R-CNN using Inception ResNet with 300 proposals. It runs at 1 second per image.
* The most accurate model is an ensemble model with multi-crop inference. It achieves state-of-the-art detection on 2016 COCO challenge in accuracy. It uses the vector of average precision to select five most different models.

Fastest

* SSD with MobileNet provides the best accuracy tradeoff within the fastest detectors.
* SSD is fast but performs worse for small objects comparing with others.
* For large objects, SSD can outperform Faster R-CNN and R-FCN in accuracy with lighter and faster extractors.

Good balance between accuracy and speed

* Faster R-CNN can match the speed of R-FCN and SSD at 32mAP if we reduce the number of proposal to 50.

 





