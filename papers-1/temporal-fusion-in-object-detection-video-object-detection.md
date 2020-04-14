---
description: Summaries of few paper in the above topic.
---

# Temporal Fusion in Object Detection/ Video Object Detection

## Feature Propagation

### [**Looking Fast and Slow: Memory-Guided Mobile Video Object Detection**](https://arxiv.org/pdf/1903.10172v1.pdf)

#### **Summary:**

* They also use Fast and Slow backbone architecture for detection at each frame. They have shows the evaluation for different number of times the small network is run after bigger network \(denoted by \tau in paper\). 
* They use SSD and Mobile and ahead of that they use memory \(LSTM\) to propagate previous state of feature map. 
* They used RL policy trained with sophisticated decision making \(rewards\) for adaptive keyframe selection \(choosing when the bigger network needs to be run\).



![](../.gitbook/assets/image%20%2842%29.png)

![](../.gitbook/assets/image%20%2873%29.png)

### [**TSM: Temporal Shift Module for Efficient Video Understanding**](https://arxiv.org/pdf/1811.08383v3.pdf.)

![](../.gitbook/assets/image%20%2815%29.png)

#### **Summary:**

* **This module helps then to shifts part of channels along the temporal dimension. Hence able to help propagate feature information across frames. This module is computational free**

![](../.gitbook/assets/image%20%2895%29.png)

### [**Mobile Video Object Detection with Temporally-Aware Feature Maps**](https://arxiv.org/pdf/1711.06368v2.pdf)

Basically, they add LSTM to feature map part, hence feature map at $$t$$ can use information from feature map at frame $$t-1$$. 

![](../.gitbook/assets/image%20%2833%29.png)

## Feature Aggregation over Frames

### \*\*\*\*[**Sequence Level Semantics Aggregation for Video Object Detection**](https://arxiv.org/pdf/1907.06390v2.pdf)

* They device somethign called Sequence Level Semantics Aggregation \(SELSA\) module. 
* instead of considering few nieghbouring frames for combinging features, they use complete complete video in global sense. 
* Existing works generally take video as sequential frames, and thus mainly utilize the temporal information to enhance the performance of a detector. For example, Flow Guided Feature Aggregation \(FGFA\) \[36\] uses at most 21 frames during training and testing, which is less than 5% of average video length. Here instead of taking a consecutive viewpoint, we propose to treat video as a bag of unordered frames and try to learn an invariant representation of each class on the full sequence level. _This reinterprets video object detection from a sequential detection task to a multi-shot detection task._
* Their method, find the semantic similarity between two regions proposals outputed by RPN in spatio-temporal dimension using cosine similarity. Now they use semantic similarity to do the feature aggregation of proposals.  That's it, so now every reference proposals is aggregated with nearest proposals and now they are passed ahead in network as normal proposal. 
* This method doesn't seem to be able to deployed in online setting. Or may be, if use instead of global we use proposals used till frame $$t$$i.e finding semantic similarity with proposals from past frames only.

![](../.gitbook/assets/image%20%28125%29.png)

\*\*\*\*

### [Towards High Performance Video Object Detection for Mobiles](https://arxiv.org/pdf/1804.05830v1.pdf)

* They propagate features on majority non-key frames while computing and aggregating features on sparse key frames.
* On all frames, we present Light Flow, a very small deep neural network to estimate feature flow, which offers instant availability on mobiles. On sparse key frame, we present flow-guided Gated Recurrent Unit \(GRU\) based feature aggregation, an effective aggregation on a memory-limited platform. Additionally, we also exploit a light image object detector for computing features on key frame, which leverage advanced and efficient techniques, such as depthwise separable convolution \[22\] and Light-Head R-CNN \[23\].

![](../.gitbook/assets/image%20%2857%29.png)

### [Object Detection in Video with Spatiotemporal Sampling Networks](https://arxiv.org/pdf/1803.05549.pdf)

* They propose a Spatiotemporal Sampling Network \(STSN\) that uses deformable convolutions across time for object detection in videos
* STSN performs object detection in a video frame by learning to spatially sample features from the adjacent frames.
* They train our STSN end-to-end on a large set of video frames labeled with bounding boxes.

![](../.gitbook/assets/image%20%28105%29.png)

## Motion Propogation/ Tracking based

### \*\*\*\*[**T-CNN: Tubelets with Convolutional Neural Networks for Object Detection from Videos**](https://arxiv.org/pdf/1604.02532.pdf)\*\*\*\*

* Box sequence of same object across different frames is called in **tubelet**. 
* A tubelet can be treated as a unit to apply the long-term constraint. Low detection confidence on some positive bounding boxes may result from moving blur, bad poses, or lack of enough training samples under particular poses. Therefore, if most bounding boxes of a tubelet have high confidence detection scores, the low confidence scores at certain frames should be increased to enforce its long-term consistency. 
* Temporal information is effectively incorporated into the proposed detection framework by locally propagating detection results across adjacent frames as well as globally revising detection confidences along tubelets generated from tracking algorithms.
* This is a global detector but can be adjusted for online working condition. They first do normal still-iamge image on all the frames and then improve the detection using post-processing techniques.  Post processing techniques are:
  * **Multi-context suppression:** This step is for removing false positives which might be there in certain frames. Read further from the paper itself.
  * **Motion-guided propagation:** This is for removing false negatives i.e. when objects presents are not detected in some frames. In this detections from one frame is propogated to other using optimal flow vector of each bouding box. 
* They do Tubelet Re-scoring which include high confidence socring, sptail max pooling and tubelet classification. It is mainly for gloabal consistency of short tebuelets. See from the paper what these actually means. 

![](../.gitbook/assets/image%20%2889%29.png)

### [Object Detection from Video Tubelets with Convolutional Neural Networks](https://arxiv.org/pdf/1604.04053.pdf)

![](../.gitbook/assets/image%20%28100%29.png)

* This work is share some of the authors from above paper and have kinda similar idea. 

## Using Optical Flow

### [Flow-Guided Feature Aggregation for Video Object Detection](https://arxiv.org/pdf/1703.10025v2.pdf)

* This is basically feature aggregration over frames using optical flow. 

![](../.gitbook/assets/image%20%28108%29.png)

