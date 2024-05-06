# Entropy

Entropy is the expected amount of information in an event.

$$
H(p) = - E[\log p] = \sum p\log p
$$

KL divergence

$$
KL(p|q) = E_p[\log \frac{p}{q}] = \sum p\log \frac{p}{q} \\ = H_p(q)-H(p) \\ = \text{cross entropy - entropy}
$$

Mutual information - attempt to measure the correlation between to RV

$$
f(x) = x * e^{2 pi i \xi x}
$$
