# Probablistic Equations

### Joint Probability

$$
p(a,b) = p(a|b)p(b) = p(b|a)p(a)
$$

###  Marginalization or Total Probability Theorem 

When variable `b` is dependent/independent on variable `a` then we have:

$$
p(b) = \int_{a}p(b,a) da = \int_{a}p(b|a)p(a) da = 
\sum_i p(b|a_i)p(a_i)
$$

Here we say the distribution $$b$$ is marginalized wrt to distribution $$a$$ .

Note that $$a_i$$are disjoint for $$i=1,2,...$$ 

#### Marginalization as Expected Value

$$
p_X(x) = \int_y p_{X|Y}(x|y) p_Y(y)dy = E_Y[p_{X|Y}(x|y)]
$$

Intuitively, the marginal probability of X is computed by examining the conditional probability of X given a particular value of Y, and then averaging this conditional probability over the distribution of all values of Y.

This follows from the definition of expected value \(after applying the law of the unconscious statistician\)

### Conditional Probability

$$
P(A|B) = Probability\; of\; A, given\; B = \frac{P(A \cap B)}{P(B)} = \frac{\text{# of A and B}  }{\text{# of B}}
$$

i.e "If I know B is the case, then what is the probability that A is also the case"

To understand the intuition behind the concept of conditional probability, note that if B has occurred then we know that the selected ω belongs to B. Therefore, when evaluating A, one should ignore all ω’s that are not in B. Thus, a revised measure of the likeliness of A should depend on P\(A ∩ B\). Intuitively this is equivalent to reducing the effective sample space from Ω to B ⊂ Ω. However, according to the second axiom of probability, the total probability measure must be equal to one. Hence, we re-scale P\(A ∩ B\) by P\(B\) to obtain P\(Ω\|B\) = P\(B\|B\) = 1.

**Example:** Consider rolling a dice example: Ω = {1, 2, . . . , 6}. Let A = {6} and B = {2, 4, 6}. In this example, the unconditional probability of rolling a six is P\(A\) = 1/6. Now suppose you know that a player rolled an even number, however, you do not know what number exactly. In that case, you can update the probability of rolling a six to P\(A\|B\) = P\(A ∩ B\)/P\(B\) = P\({6}\)/P\({2, 4, 6}\) = 1/3.

There is one more way to express conditional probability, let me take an to explain it. Suppose you have to tell if a person is man or women given he/she have long hair. How would you calculate that. You are having information about ratio of male to female and percentage of long hair in each of gender i.e you have $$P(m), P(w), P(long\; hair | w), P(long\; hair | m)$$and we have to find $$P(w|lh) \;or \; P(m|lh)$$, note that $$P(w|lh) +P(m|lh) = 1$$ , hence finding anyone will suffice. Using Bayes Theorem:

$$
P(w | lh) = \frac{P(lh|w)P(w)}{P(lh)} \\
P(w | lh) = \frac{P(lh|w)P(w)}{P(lh|w)P(w)+P(lh|m)P(m)} \\
P(w | lh) = \frac{P(lh,w)}{P(lh, m)+P(lh,w)}
$$

This shows that $$P(w|lh)$$ is the just the ratio of women with long here to the total people with long hair. 

### Bayes Theorem/ Conditional Probability

Using joint probability equation:

$$
p(a|b) = \frac{p(a,b)}{p(b)} = \frac{p(b|a)p(a)}{p(b)}
$$

A common scenario for applying the Bayes Rule formula is when you want to know the probability of something “unobservable” given an “observed” event.

Considering conditionality in  **Bayes theorem**, let's say that we condition the probability $$p(a|b)$$ on some event $$c$$. So it is basically probability of $$a$$ given \($$b$$conditioned on $$c$$ \)now. Now will just conditional the every probability on $$c$$in above equation. So we get:

$$
p(a|b,c) =  \frac{p(b|a,c)p(a|c)}{p(b|c
)}
$$

Also, using **total probability theorem** 

$$
p(a|b) = \frac{p(b|a)p(a)}{\int_{a}p(b|a)p(a) da}
$$

### Bayes with Relative Probabilities 

There are times when we would like to use Bayes Theorem to update a belief, but there is no way to calculate the probability of the event observed, P\(F\). All hope is not lost. In such situations we can still calculate the relative probability of events. For example, imagine we would like to answer the question, is even A or event B more likely given an observation F. We can express this mathematically as calculating whether P\(A\|F\)/P\(B\|F\) is greater than or equal to 1. Both of those terms can be expanded using Bayes, and when they are expanded the P\(F\) term cancels out: 

![](../.gitbook/assets/image%20%2856%29.png)

### Distributing two variables over Third Variable

$$
p(a,b|c) = p(a|b,c)p(b|c) = p(b|a,c)p(a|c)
$$

### Event independence 

When events $$x$$ and $$y$$ are independent of each other, then

$$
\begin{align*}
p(x,y)&=p(x)p(y)           &  p(x|y) &= p(x)              &  p(y|x)=p(y)
\end{align*}
$$

### Conditional Independence

In this, two event $$x$$ and $$y$$ are indepentent given some event $$z$$ , i.e if you know the value of $$z$$ then $$x$$ and $$y$$ become independent of each other which initially they were not.   
**Note: Coniditional Indpendence doesn't imply normal independence.** 

$$
\begin{align*}
p(x,y|z)&=p(x|z)p(y|z)           &  p(x|y,z) &= p(x|z)              &  p(y|x,z)=p(y|z)
\end{align*}
$$

### Chain Rule of Probability

$$
p(a,b,c,d) = p(a|b,c,d)p(b|c,d)p(c|d)p(d)
$$

### Marginalization of Conditional Probability

$$
p(a|b) = \frac{p(a,b)}{p(b)} = \frac{\sum_c p(a,b,c) }{p(b)} = \frac{\sum_c p(a,c|b)p(b)}{p(b)} = \sum_c p(a,c|b)
$$

### Breaking Independence 

But I wanted to pass on this surprising insight so that you have a more full understanding of probability. If two events E and F are independent, it is possible that there exists another event G such that E\|G is no longer independent of F\|G. As an example, Let’s say a person has a fever \(G\) if they either have malaria \(E\) or have an infection \(F\). We are going to assume that getting malaria \(E\) and having an infection \(F\) are independent: knowing if a person has malaria does not tell us if they have an infection. Now, a patient walks into a hospital with a fever \(G\). Your belief that the patient has malaria, given that they have a fever, P\(E\|G\), is high and your belief that the patient has an infection given that they have a fever, P\(F\|G\), is high. Both explain the fever. Interestingly, at this point in time \(conditioned on G\), given our knowledge that the patient has a fever, gaining the knowledge that the patient has malaria will change your belief the patient has an infection! The malaria explains why the patient has a fever, and so the alternate explanation becomes less likely. The two events \(which were previously independent\) are dependent now that we have conditioned on the patient having a fever.



{% file src="../.gitbook/assets/probability\_summary.pdf" caption="Brief Summary of probability theorems/equations" %}

#### Resources

* [https://medium.com/@laumannfelix/statistics-probability-fundamentals-2-cbb1239f9605](https://medium.com/@laumannfelix/statistics-probability-fundamentals-2-cbb1239f9605)

