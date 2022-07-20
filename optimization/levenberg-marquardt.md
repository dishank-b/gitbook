# Levenberg–Marquardt

Levenberg-Marquardt is also an optimization used for non-linear least square problems. &#x20;

The LMA interpolates between the [Gauss–Newton algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton\_algorithm) (GNA) and the method of [gradient descent](https://en.wikipedia.org/wiki/Gradient\_descent). LMA can also be viewed as [Gauss–Newton](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton) using a [trust region](https://en.wikipedia.org/wiki/Trust\_region) approach.

### Adaptive Lambda λ

The (non-negative) damping factor ![\lambda](https://wikimedia.org/api/rest\_v1/media/math/render/svg/b43d0ea3c9c025af1be9128e62a18fa74bedda2a) is adjusted at each iteration. If reduction of cost ![S](https://wikimedia.org/api/rest\_v1/media/math/render/svg/4611d85173cd3b508e67077d4a1252c9c05abca2) is rapid, a smaller value can be used, bringing the algorithm closer to the [Gauss–Newton algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton\_algorithm), whereas if an iteration gives insufficient reduction in the residual, ![\lambda](https://wikimedia.org/api/rest\_v1/media/math/render/svg/b43d0ea3c9c025af1be9128e62a18fa74bedda2a) can be increased, giving a step closer to the gradient-descent direction.&#x20;

