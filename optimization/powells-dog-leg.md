# Powell's dog leg

Similarly to the [Levenberg–Marquardt algorithm](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt\_algorithm), it combines the [Gauss–Newton algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton\_algorithm) with [gradient descent](https://en.wikipedia.org/wiki/Gradient\_descent), but it uses an explicit [trust region](https://en.wikipedia.org/wiki/Trust\_region). At each iteration, if the step from the Gauss–Newton algorithm is within the trust region, it is used to update the current solution. If not, the algorithm searches for the minimum of the [objective function](https://en.wikipedia.org/wiki/Objective\_function) along the steepest descent direction, known as Cauchy point. If the Cauchy point is outside of the trust region, it is truncated to the boundary of the latter and it is taken as the new solution. If the Cauchy point is inside the trust region, the new solution is taken at the intersection between the trust region boundary and the line joining the Cauchy point and the Gauss-Newton step (dog leg step) .



