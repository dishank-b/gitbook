# Covariance and Correlation

## Covariance 

Covariance is a measure of how much two random variables vary together.

* If X and Y are independent then $$Cov(X, Y ) = 0$$ .  **Warning**: The converse is false: **zero covariance does not always imply independence**. 

![Zero Covariance doesn&apos;t mean Independent variables](../../.gitbook/assets/image%20%2827%29.png)

The key point is that $$Cov(X, Y )$$ measures the linear relationship between X and Y . In the above example $$X$$ and $$X^2$$ have a quadratic relationship that is completely missed by $$Cov(X, Y )$$.

* $$Cov(X1 + X2, Y ) = Cov(X1, Y ) + Cov(X2, Y )$$ 

## Correlation

The units of covariance $$Cov(X, Y )$$ are ‘units of $$X$$ times units of $$Y$$ ’. This makes it hard to compare covariances: **if we change scales then the covariance changes as well. Correlation is a way to remove the scale from the covariance**

$$
Cor(X, Y ) = ρ = \frac{Cov(X,Y)}{σ_x σ_y}
$$

* ρ is dimensionless \(it’s a ratio!\).
* −1 ≤ ρ ≤ 1. ****Furthermore,  ρ = +1 if and only if Y = aX + b with a &gt; 0,  ρ = −1 if and only if Y = aX + b with a &lt; 0.

Knowing squared correlation\( $$ρ^2$$ \) helps to determine the variance in one variable given the other variable. If is $$ρ^2$$ 0.7 between x and y, it means that x predict 70% variation in y.

{% file src="../../.gitbook/assets/mit18\_05s14\_reading7b.pdf" caption="Covariance & Coorelation" %}

## **Coorelation Doesn't Mean Causality**

Correlation doesn't equal causation i.e if x and y are highly correlated doesn't means that either of x or y is cause of other. 

Causation can be only determined by probabilty graphs. 

