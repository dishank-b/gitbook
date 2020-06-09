# Generative vs Discriminative

{% embed url="https://stackoverflow.com/a/15137512" %}

{% embed url="https://stackoverflow.com/a/879591" %}

More formally, given a set of data instances X and a set of labels Y:

* **Generative** models capture the joint probability p\(X, Y\), or just p\(X\) if there are no labels.
* **Discriminative** models capture the conditional probability p\(Y \| X\).

A generative model includes the distribution of the data itself, and tells you how likely a given example is. For example, models that predict the next word in a sequence are typically generative models \(usually much simpler than GANs\) because they can assign a probability to a sequence of words.

### Modeling Probabilities <a id="modeling-probabilities"></a>

Neither kind of model has to return a number representing a probability. You can model the distribution of data by imitating that distribution.

For example, a discriminative classifier like a [decision tree](http://wikipedia.org/wiki/Decision_tree_learning) can label an instance without assigning a probability to that label. Such a classifier would still be a model because the distribution of all predicted labels would model the real distribution of labels in the data.

Similarly, a generative model can model a distribution by producing convincing "fake" data that looks like it's drawn from that distribution.

**Both generative and discriminative models can estimate probabilities \(but they don't have to\).**

#### **Advantages of Generative Model**

* They are are less prone to overfitting. As they understand/learn the whole data distribution rather than the boundary.

#### Disadvantages of Generative Model

* Prone to outliers
* Need large data to learn the distribution. 

### Generative modelling vs Discriminative modelling.

**When we say modelling the distribution, we mean - learning a model which represents the distribution of the random variable.** 

### Example

{% embed url="https://youtu.be/gwV7spVO5Z0" %}



Let's say you have following system:

* Computer receives telephone call  
* Measures the pitch of the voice
* Tells if it's a male or female.

$$x=\text{pitch}$$, $$y=\text{male,female}$$

#### Generative Modelling. 

The computer will learn the distribution of pitches for both the gender. i.e it will learn $$p(x|y=\text{male})$$and $$p(x|y=\text{female})$$. In this we are basically modelling how the pitches vary according to the gender. 

Note basically learning the joint distribution $$p(x,y)$$as you learned $$p(x|y)$$and you can know distribution of $$p(y)$$simply by counting the number of each type of gender samples you are getting during the training. Hence $$p(x,y) = p(x|y)p(y)$$

Now after modelling, computer will see what are chances of given a pitch it belongs to $$p(x|y=\text{male})$$ or $$p(x|y=\text{female})$$. The one with the maximum likelihood wins.

#### Discriminative Modelling

In this you will simply model the boundary between  $$p(y=\text{male}|x)$$and $$p(y=\text{female}|x)$$. So now given a pitch you can tells what's the probability of pitch belonging to female or male. It doesn't learn anything about the distribution of pitch about any of the gender. 



