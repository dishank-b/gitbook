# Diffusion Models

### In a nutshell:

Repetitive refining of a sample to get a final good image.&#x20;

* This repetitive sampling makes the generation process slow.

## Forward Process

They take the input image $$x_0$$ and gradually add Gaussian noise to it through a series of $$T$$ steps. We will call this the forward process. Notably, this is unrelated to the forward pass of a neural network.

Basically, at each time step you add some noise to the sample. So you start with the image, and then keep adding Gaussian noise until it becomes just noise.&#x20;

## Reverse Process

In this, a neural network is trained to reverse the noise-adding process. In this the network is trained to predict a "less" noise sample given a noise sample, basically the opposite of the forward process at a time $$t$$.

## Resources

Very good way to understand image generation from auto-regression to diffusion point of view.&#x20;

Diffusion model from the perspective of samples lying on data manifold and probablility density assosiated with them&#x20;

{% embed url="https://youtu.be/1pgiu--4W3I" %}

Diffusion model from the perspective of score matching, langevin-dynamics,&#x20;

{% embed url="https://youtu.be/Fk2I6pa6UeA" %}

Spectrum of diffusion vs Auto-regression

{% embed url="https://youtu.be/zc5NTeJbk-k?list=PLXmbE5IFg3EEoSAzuqbu7o8Kh8FFhTFPc" %}

{% embed url="https://youtu.be/i2qSxMVeVLI" %}

{% embed url="https://lilianweng.github.io/posts/2021-07-11-diffusion-models/#reverse-diffusion-process" %}
