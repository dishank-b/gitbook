---
description: This describes techniques to have stable GAN training
---

# Making GANs train

* Batch Norm and weight initialization are important.  When I used Batch norm in discriminator, is was showing NaNs, as soon as I removed batch norm network start training which is very different from normal behaviour. Generally introducing batch norm helps in model learn, but here the case is reverse. 
* When weight initialisation is careful, you may choose to not have batch norm.
* Discriminator should be little weaker than generator for stable training. Many times it happens that discriminator get very powerful over training and having its loss 0. But generator couldn't learn anything. 
* Always have sigmoid at last layer of discriminator if discriminator loss is showing NaN. 
* Leaky Relu is very amazing for to be used in hidden layers\(not the last layer\) of generator and discriminator. They allow sufficient gradient to be flow back to generator, hence generator weights also updates and not allowing discriminator to get over powerfull. But make sure to use sigmoid in last layers.

### Pix2Pix:

* Images are in range \[-1, 1\]
* In generator, gan loss weight is 1.0 and L1 loss weight is 100.0.
* beta1 in adam optimizer is 0.5.
* discriminator output is scalar, and activation function is sigmoid. batch norm is used in all layer just not in the last layer. discriminator uses leaky relu as activation function in all middle layers.
* encoder of generator use batch norm and leaky relu. initial three layer of decoder in the generator uses dropout with prob 0.5, and decoder uses use relu as activation functions. Last layer of encoder of generator have no activation.
* Output of generator have tanh activation function.
* batch norm momentum is 0.9 in yenchenlin implementation and 0.1 in affinelayer implementation. **Doubt here**
* In the loss use eps=1e-12 with dis\_fake or dis\_real i.e. log\(dis\_fake + eps\)
* Use std\_dev=0.02 for initializaing weights of truncated normal initializers.
* affinelayer implementation of pix2pix have 4x4 kernels.

![](../.gitbook/assets/image%20%28144%29.png)

* Note two things in above. 
  * Adding of discriminator dependency on the generator optimizer.
  * using of ema above for updating loss or something. 

