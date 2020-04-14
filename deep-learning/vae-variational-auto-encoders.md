# VAE: Variational Auto-Encoders

[**https://wiseodd.github.io/techblog/2016/12/10/variational-autoencoder/**](https://wiseodd.github.io/techblog/2016/12/10/variational-autoencoder/) **- Probabilistic View**

[**http://kvfrans.com/variational-autoencoders-explained/**](http://kvfrans.com/variational-autoencoders-explained/) **- Neural Net View**  


* **Variational Autoencoders \(VAEs\) allow us to formalize the problem in the framework of probabilistic graphical models where we are maximizing a lower bound on the log likelihood of the data.**
* **VAE is rooted in bayesian inference, i.e. it wants to model the underlying probability distribution of data so that it could sample new data from that distribution.**
* **We add a constraint on the encoding network, that forces it to generate latent vectors \( latent variables, as opposed to** [**observable variables**](https://en.wikipedia.org/wiki/Observable_variable)**, are** [**variables**](https://en.wikipedia.org/wiki/Variable_%28mathematics%29) **that are not directly observed but are rather inferred \(through a** [**mathematical model**](https://en.wikipedia.org/wiki/Mathematical_model)**\) from other variables that are observed \(directly measured\).\) that roughly follow a unit gaussian distribution. It is this constraint that separates a variational autoencoder from a standard one.** ![](https://lh6.googleusercontent.com/zREoZfNlUt7wVVt1d5XAbGZmUgExq6Tf9SmBnxxMmdSKW2dlDRfCm0mAx-ZhAijhmF7rjaG_CzXEqvhf2FyFZFxQxqZsvxDmnaTE63pJxccbQ6KS5kqkLKTyskAoIkSpiUFyxaxM)
* **For our loss term, we sum up two separate losses: the generative loss, which is a mean squared error that measures how accurately the network reconstructed the images, and a latent loss, which is the KL divergence that measures how closely the latent variables match a unit gaussian. In order to optimize the KL divergence, we need to apply a simple reparameterization trick: instead of the encoder generating a vector of real values, it will generate a vector of means and a vector of standard deviations.e**
* **Reparameterization is a important part of VAE.** [**http://gregorygundersen.com/blog/2018/04/29/reparameterization/**](http://gregorygundersen.com/blog/2018/04/29/reparameterization/) **- Link to understand why reparameterization is needed.**

\*\*\*\*

