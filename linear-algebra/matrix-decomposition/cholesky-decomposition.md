# Cholesky Decomposition

Let's say $$A$$ is symmetric positive definite matrix, then

$$
A = LL^T
$$

Where $$L$$is a lower triangular matrix.&#x20;

**Note the cholesky decomposition is unique i.e matrix** $$L$$**is unique for a given** $$A$$**.**&#x20;

### How to use Cholesky Decomposition

The Cholesky decomposition is mainly used for the numerical solution of [linear equations](https://en.wikipedia.org/wiki/System\_of\_linear\_equations) ![\mathbf {Ax} =\mathbf {b}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/e68388b7df59f536a3bef4e70def2f2bb36f48c0). If **A** is symmetric and positive definite, then we can solve![\mathbf {Ax} =\mathbf {b}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/e68388b7df59f536a3bef4e70def2f2bb36f48c0) by first computing the Cholesky decomposition ![{\displaystyle \mathbf {A} =\mathbf {LL} ^{\mathrm {\*} \}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/15eb22028dcd9bb93da3f1ac1b8a4302752d030c), then solving ![{\displaystyle \mathbf {Ly} =\mathbf {b} }](https://wikimedia.org/api/rest\_v1/media/math/render/svg/2baf49aa432951eeb845b101d7be2c8a00e56b5c) for **y** by [forward substitution](https://en.wikipedia.org/wiki/Forward\_substitution), and finally solving ![{\displaystyle \mathbf {L^{\*}x} =\mathbf {y} }](https://wikimedia.org/api/rest\_v1/media/math/render/svg/0be4f63d9fbfd83220193f8e7a07e1fae29b91a0) for **x** by [back substitution](https://en.wikipedia.org/wiki/Back\_substitution).

### Square Root

For $$A = LL^T$$, $$L$$could be thought of as square root of matrix $$A$$, though mind that it's not a unique square root, many other matrix can be also be thought of as square root of $$A$$.

### Application of Cholesky decomposition

$$
\Sigma = LL^T
$$

Geometrically, the Cholesky matrix transforms uncorrelated variables into variables whose variances and covariances are given by Σ. In particular, if you generate _p_ standard normal variates, the Cholesky transformation maps the variables into variables for the multivariate normal distribution with covariance matrix Σ and centered at the origin.&#x20;

{% embed url="https://blogs.sas.com/content/iml/2012/02/08/use-the-cholesky-transformation-to-correlate-and-uncorrelate-variables.html" %}
