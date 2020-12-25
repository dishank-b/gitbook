# Probabilistic View

A neural network can be viewed as probabilistic model $$p(y|x,w)$$ . For classification, $$y$$ is a set of classes and $$ p(y|x,w)$$ is a categorical distribution. For regression, $$y$$ is a continuous variable and $$p(y|x,w)$$ is a Gaussian distribution.

Given a training dataset $$D=\{x^i,y^i\}$$ we can construct the likelihood function $$p(D|w)=∏_ip(y^i, x^i |w)$$ which is a function of parameters $$w$$ . Maximizing the likelihood function gives the maximimum likelihood estimate \(MLE\) of $$w$$. The usual optimization objective during training is the negative log likelihood. For a categorical distribution this is the _cross entropy_ error function, for a Gaussian distribution this is proportional to the _sum of squares_ error function. MLE can lead to severe overfitting though.

Multiplying the likelihood with a prior distribution $$p(w)$$ is, by Bayes theorem, proportional to the posterior distribution $$p(w|D)∝p(D|w)p(w)$$ . Maximizing $$p(D|w)p(w)$$ gives the maximum a posteriori \(MAP\) estimate of $$. Computing the MAP estimate has a regularizing effect and can prevent overfitting. The optimization objectives here are the same as for **MLE plus a regularization term coming from the log prior**.

Both MLE and MAP give point estimates of parameters. If we instead had a full posterior distribution over parameters we could make predictions that take weight uncertainty into account. This is covered by the posterior predictive distribution $$p(y|x,D)=∫p(y|x,w)p(w|D)dw$$ in which the parameters have been marginalized out. This is equivalent to averaging predictions from an ensemble of neural networks weighted by the posterior probabilities of their parameters **w**.

