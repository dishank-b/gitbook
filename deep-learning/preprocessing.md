# PreProcessing

## Image Normalization

We'd like in this process for each feature to have a similar range so that our gradients don't go out of control \(and that we only need one global learning rate multiplier\).

**SO what we do is we take average over all the images over all the pixels independently of each channel.** 

Question is:

* Why not over all the images independently for each pixel and each channel. This will basically give you an mean image to be subtracted from over all the images. 
  * Because all pixels of the image share same weights and biases, hence it's important that we also take average over all pixels \(in spatial dimension\) as well. 
* Is taking average over all the pixels in an image is a good idea? Doesn't it mess up inter contrastive features of the image for each channel?
  * May be not, because contrastive 



