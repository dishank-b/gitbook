# Norms

Norms are mathematical concepts to measure the length of vector. 

Norm is any function that satisfy following properties:

* $$f(x)=0$$for all $$x=0$$
* $$f(x+y)>f(x)+f(y)$$, triangle inequality
* $$f(\alpha x)=|\alpha|f(x)$$for all scalar $$\alpha$$

### Example of Norms

#### L^p Norm

$$L^P$$norm is given as

$$
||x||_p = (\sum_i|x_i|^p)^{\frac{1}{p}}
$$

So, $$L^2$$is euclidean norm. Many times, square of $$L^2$$norm is used. Many times denoted simply by $$||x||$$. For vector $$x$$

$$
||x|| = x^Tx
$$

Many times $$L^1$$used when difference between zero and non-zero elements are more important. 

#### Max Norm

It is denoted by $$L^\infty$$. It is simply the absolute value of element with largest magnitude.

$$
||x||_\infty = \max_i |x_i|
$$

#### Frobenius Norm 

This is norm used for measure size of a matrix. 

$$
||A||_F = \sqrt{\sum_{i,j}A_{i,j}^2}
$$

