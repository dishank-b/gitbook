# Bayes Theorem

Remember that one way to understand bayes theorem is ratio. Let' see how

Lets say we want to calculate $$p(a|b)$$, now here we are asking that given $$b$$ is done, what's the probabililty that $$a$$ has been done?  
  
Example:  Let's say we have two coins, one is fair and other one is baised with two head. Now we take one coin randomly and flip it. Now, we see that we got head, what is the probability that chosen coin is fair one? So here $$ b=  \text{getting head}$$and $$ a = \text{coin being fair} $$

Here the solution is simply the ratio of:  \# of ways in which two can get the head with fair coin to the total \# number of ways in which you can get an head. To write is mathemcatically:

$$
p(fair|head) = \frac{P(\text{head with fair coin})}{P(head)} = \frac{P(\text{head with fair coin})}{P(\text{head with fair coin})+P(\text{head with biased coin})}
$$

Now to write the above in bayes theorem terms.   
Note that $$P(\text{head with fair}) = P(head|fair)*P(fair)$$ and $$P(\text{head with bias}) = P(head|bias)*P(bias)$$. 

Hence the **Bayes Theorem** can be written as:

$$
p(fair|head) = \frac{P(head|fair)*P(fair)}{P(head|fair)*P(fair)+P(head|bias)*P(bias)}
$$

which is of the form of **Orignial Bayes Theorem**:

$$
p(a|b) = \frac{p(b|a)p(a)}{p(b)} = \frac{p(b|a)p(a)}{\sum_i p(b|a_i)p(a_i)}
$$



### Resources

* [https://youtu.be/OqmJhPQYRc8](https://youtu.be/OqmJhPQYRc8)



