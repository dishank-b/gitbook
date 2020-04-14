---
description: This is one of first paper on style transfer.
---

# A Neural Algorithm of Artistic Style - A.Gatys

Paper: [https://arxiv.org/pdf/1508.06576.pdf](https://arxiv.org/pdf/1508.06576.pdf)

### Summary:

This paper shows how to transfer style of one image to other image preserving its content. In this paper, a photograph is chosen, and then style images is chosen from some famous paintings and then style form paintings is applied on content photograph.

###  Key Points:

* When we train the CNN for object recognition, then as we go down the network, the input image is transformed into representations that increasingly care about the actual content of the image compared to its detailed pixel values.
* Higher layers in the network capture the high-level content in terms of objects and their arrangement in the input image.
* This paper make use of idea to update the input images using back prop instead of weights. Here we differentiate the loss wrt input image instead of weight, to minimise the loss. 
* Max pooling is replaced by average pooling for better gradient flow and also average fooling generate more smooth results.

### Method:

![Figure 1: Convolutional Neural Network \(CNN\). A given input image is represented as a set of filtered images at each processing stage in the CNN. While the number of different filters increases along the processing hierarchy, the size of the filtered images is reduced by some downsampling mechanism \(e.g. max-pooling\) leading to a decrease in the total number of units per layer of the network. Content Reconstructions. We can visualise the information at different processing stages in the CNN by reconstructing the input image from only know- ing the network&#x2019;s responses in a particular layer. We reconstruct the input image from from layers &#x2018;conv1 1&#x2019; \(a\), &#x2018;conv2 1&#x2019; \(b\), &#x2018;conv3 1&#x2019; \(c\), &#x2018;conv4 1&#x2019; \(d\) and &#x2018;conv5 1&#x2019; \(e\) of the orig- inal VGG-Network. We find that reconstruction from lower layers is almost perfect \(a,b,c\). In higher layers of the network, detailed pixel information is lost while the high-level content of the image is preserved \(d,e\). Style Reconstructions. On top of the original CNN representations we built a new feature space that captures the style of an input image. The style representation computes correlations between the different features in different layers of the CNN. We recon- struct the style of the input image from style representations built on different subsets of CNN layers \( &#x2018;conv1 1&#x2019; \(a\), &#x2018;conv1 1&#x2019; and &#x2018;conv2 1&#x2019; \(b\), &#x2018;conv1 1&#x2019;, &#x2018;conv2 1&#x2019; and &#x2018;conv3 1&#x2019; \(c\), &#x2018;conv1 1&#x2019;, &#x2018;conv2 1&#x2019;, &#x2018;conv3 1&#x2019; and &#x2018;conv4 1&#x2019; \(d\), &#x2018;conv1 1&#x2019;, &#x2018;conv2 1&#x2019;, &#x2018;conv3 1&#x2019;, &#x2018;conv4 1&#x2019; and &#x2018;conv5 1&#x2019; \(e\)\). This creates images that match the style of a given image on an increasing scale while discarding information of the global arrangement of the scene.](../.gitbook/assets/image%20%2830%29.png)

The network used here is VGG19, they use only conv layers of the network. 

Let $$\vec{p}$$ be the photograph and $$\vec{a}$$ be the artwork. The loss function we minimise is:  
                          $$L_{total}(\vec{p},\vec{a},\vec{x} ) = αL_{content}(\vec{p},\vec{x} )+ βL_{style}(\vec{a},\vec{x} )$$   
So let $$\vec{p}$$ and $$\vec{x}$$ be the original content image and the image that is generated and $$P^l$$ and $$F^l$$ their respective feature representation in layer l. We then define the squared-error loss between the two feature representations  
                                           $$L_{content}(\vec{p},\vec{x},l ) = \frac{1}{2}\sum_{i,j}(F_{ij}^l-P_{ij}^l)^2$$   
from which the gradient with respect to the image $$\vec{x}$$ can be computed using standard error back-propagation. Thus we can change the initially random image $$\vec{x}$$ until it generates the same response in a certain layer of the CNN as the original image $$\vec{p}$$ .

On top of the CNN responses in each layer of the network we built a style representation that computes the correlations between the different filter responses, where the expectation is taken over the spatial extend of the input image. These feature correlations are given by the Gram matrix Gl ∈ RNl×Nl , where Gl ij is the inner product between the vectorised feature map i and j in layer l:  
                                                                  $$G_{ij}^l = \sum_{k}F_{ik}^lF_{jk}^l$$   
To generate a texture that matches the style of a given image \(Fig 1, style reconstructions\), we use gradient descent from a white noise image to find another image that matches the style representation of the original image. This is done by minimising the mean-squared distance between the entries of the Gram matrix from the original image and the Gram matrix of the image to be generated. So let ?a and ?x be the original image and the image that is generated and Al and Gl their respective style representations in layer l. The contribution of that layer to the total loss is then  
                                                                   $$E_l = \frac{1}{4N_l^2M_l^2}\sum_{ij}(G_{ij}^l-A_{ij}^l)^2$$   
Total loss is  
                                                    $$L_{style}(\vec{a},\vec{x}) = \sum_{l=0}^Lw_lE_l$$   
 where wl are weighting factors of the contribution of each layer to the total loss.

### References:

* Gatys, L. A., Ecker, A. S. & Bethge, M. Texture synthesis and the controlled generation of natural stimuli using convolutional neural networks. arXiv:1505.07376 \[cs, q-bio\] \(2015\). URL [http://arxiv.org/abs/1505.07376](http://arxiv.org/abs/1505.07376). ArXiv: 1505.07376.
* Mahendran, A. & Vedaldi, A. Understanding Deep Image Representations by Inverting Them. arXiv:1412.0035 \[cs\] \(2014\). URL [http://arxiv.org/abs/1412.0035](http://arxiv.org/abs/1412.0035). ArXiv: 1412.0035.



