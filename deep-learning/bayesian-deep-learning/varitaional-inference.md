# Varitaional Inference

#### **Statistical Inference**

It means infering \(concluding something\) about some variable given some evidences \(such as value of some other variables\).  

It means drawing conclusions based on data. There are a many contexts in which inference is desirable, and there are many approaches to performing inference.

**For ex:**  
if you have noisy \(x, y\) data that you think follow the pattern y = β0 + β1x + error, then you might want to estimate β0, β1, and the magnitude of the error.   
Here you are inferring about variables $$\beta_0$$ and $$\beta_1$$.

Statistical inference means drawing conclusions based on data. One context for inference is the parametric model, in which data are supposed to come from a certain distribution family, the members of which are distinguished by differing parameter values. The normal distribution family is one example.

## Varitional Inference

 Varitional Inference allow us to re-write statistical inference problems \(i.e. infer the value of a random variable given the value of another random variable\) as optimization problems \(i.e. find the parameter values that minimize some objective function\)

When you have intractable probability distribution $$p$$. Variational techniques will try to solve an optimization problem over a class of tractable distributions Q in order to find a q ∈ Q that is most similar to p.

For example, we can use **KL divergence** between $$p$$ and $$q$$, so that $$q$$ will be approximate to $$p$$ which intractable, hence we can use $$q$$ in place of $$p$$. 

$$
KL(q||p) = \sum_x q(x)\log \frac{q(x)}{p(x)}
$$

### Resources

* [https://dasayan05.github.io/blog-tut/2019/11/20/inference-in-pgm.html](https://dasayan05.github.io/blog-tut/2019/11/20/inference-in-pgm.html)
* [https://www.cs.princeton.edu/courses/archive/fall11/cos597C/lectures/variational-inference-i.pdf](https://www.cs.princeton.edu/courses/archive/fall11/cos597C/lectures/variational-inference-i.pdf)
* [https://blog.evjang.com/2016/08/variational-bayes.html](https://blog.evjang.com/2016/08/variational-bayes.html)

