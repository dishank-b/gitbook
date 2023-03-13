# Lagrange Multiplier

Nice was to look at lagrange, which might also be related to implicit function theorem:

$$
\min_x f(x) \quad \text{s.t.} \quad C(x)=0
$$

To solve the above minimization problem, we can use lagrange multiplier as follows

$$
\mathcal{L}(x,\lambda) = f(x) + \lambda C(x) \\
g(\lambda) = \mathcal L(x^*(\lambda), \lambda) \quad \text{where} \quad x^* = \arg \min_x \mathcal L(x, \lambda)
$$
