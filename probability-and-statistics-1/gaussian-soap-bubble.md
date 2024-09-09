# Gaussian Soap Bubble

{% embed url="https://www.inference.vc/high-dimensional-gaussian-distributions-are-soap-bubble/" %}

{% embed url="https://dibyaghosh.com/blog/probability/highdimensionalgeometry.html" %}

{% embed url="https://people.eecs.berkeley.edu/~jrs/189/lec/22.pdf" %}

* In high dimensions, gaussian distribution are indistinguishable from uniform distribution on the unit sphere.&#x20;
* To see how low dimensional analogy will extend to high dimension, normalization gaussian and then checking the effects can be good technique.&#x20;

So introduce this problem in mathematical form:

Let's have d-dimensional standard guassian RV. $$X= [x_1, x_2, ...x_d]$$where $$x_i \sim \mathcal{N}(0,1)$$.&#x20;

Now our intuition will say that probability distribution of $$X$$will have most of its mass around mean = 0, which is the case in 1 and 2 dimensional gaussian. But in high dimension it's not like this. Not of the mass i.e if many points were to sample from $$X$$, most of them will lie at a certain radius determined by $$d$$.&#x20;

Let consider the euclidean norm of RV $$X$$and call it $$Y = \sqrt{X} = \sqrt{\sum_i x_i^2}$$, now we know that $$Y \sim \chi_k$$where $$k$$is dimensian of standard gaussian RV $$X$$.&#x20;

Now&#x20;

$$
E[Y] = \mu_Y = \sqrt{2}\frac{ \Gamma(\frac{k+1}{2})}{ \Gamma(\frac{k}{2})} \\
\approx \lim_{k \rightarrow \inf} \sqrt{k-\frac{1}{2}}
$$

which means if we have 10000 dimensional standard normal, then the mean of the norm is around 100. This means that most of the samples lie on the sphere of radius 100.&#x20;

![Histrogram of norm of 1000 samples of 10000 dimensional standard normal random variable](../.gitbook/assets/figure\_1.png)

&#x20;
