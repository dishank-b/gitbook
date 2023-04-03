# Dilated Convolutions

In simple terms, dilated convolution is just a convolution applied to input with defined gaps. With this definitions, given our input is an 2D image, dilation rate k=1 is normal convolution and k=2 means skipping one pixel per input and k=4 means skipping 3 pixels. In dilated convolutions the change is in the filter and not features. The filters (weights) skips the input according to dilation rate.&#x20;

![Dilated Convolution](<../.gitbook/assets/image (18).png>)

[https://www.quora.com/What-is-the-difference-between-dilated-convolution-and-convolution+stride](https://www.quora.com/What-is-the-difference-between-dilated-convolution-and-convolution+stride)\
This gives explanation of how dilated convolution are different from convolutions with strides.

In short, dilated convolution is a simple but effective idea and you might consider it in two cases;

1. Detection of fine-details by processing inputs in higher resolutions.
2. Broader view of the input to capture more contextual information.
3. Faster run-time with less parameters
