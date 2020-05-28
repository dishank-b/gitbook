---
description: 'Notes on Probability, Statistics and more'
---

# Probability & Statistics

## Probability Vs Statistics

### Probability

The two disciplines are closely related but they’re not identical. Probability theory is “the doctrine of chances”. It’s a branch of mathematics that tells you how often different kinds of events will happen. For example, all of these questions are things you can answer using probability theory:

* What are the chances of a fair coin coming up heads 10 times in a row?
* If I roll two six sided dice, how likely is it that I’ll roll two sixes?
* How likely is it that five cards drawn from a perfectly shuffled deck will all be hearts?
* What are the chances that I’ll win the lottery?

Notice that all of these questions have something in common. In each case the “truth of the world” is known, and my question relates to the “what kind of events” will happen. In the first question I **know** that the coin is fair, so there’s a 50% chance that any individual coin flip will come up heads. In the second question, I **know** that the chance of rolling a 6 on a single die is 1 in 6. In the third question I **know** that the deck is shuffled properly. And in the fourth question, I **know** that the lottery follows specific rules. You get the idea. The critical point is that probabilistic questions start with a known _model_ of the world, and we use that model to do some calculations.

The underlying model can be quite simple. For instance, in the coin flipping example, we can write down the model like this: P\(heads\)=0.5P\(heads\)=0.5 which you can read as “the probability of heads is 0.5”.

As we’ll see later, in the same way that percentages are numbers that range from 0% to 100%, probabilities are just numbers that range from 0 to 1. When using this probability model to answer the first question, I don’t actually know exactly what’s going to happen. Maybe I’ll get 10 heads, like the question says. But maybe I’ll get three heads. That’s the key thing: in probability theory, the **model** is known, but the **data** are not.

### Statistics

So that’s probability. What about statistics? Statistical questions work the other way around. In statistics, we don't know the truth about the world. All we have is the data, and it is from the data that we want to **learn** the truth about the world. Statistical questions tend to look more like these:

* If my friend flips a coin 10 times and gets 10 heads, are they playing a trick on me?
* If five cards off the top of the deck are all hearts, how likely is it that the deck was shuffled?
* If the lottery commissioner’s spouse wins the lottery, how likely is it that the lottery was rigged?

This time around, the only thing we have are data. What I **know** is that I saw my friend flip the coin 10 times and it came up heads every time. And what I want to _infer_ is whether or not I should conclude that what I just saw was actually a fair coin being flipped 10 times in a row, or whether I should suspect that my friend is playing a trick on me. The data I have look like this:

```text
H H H H H H H H H H H
```

and what I’m trying to do is work out which “model of the world” I should put my trust in. If the coin is fair, then the model I should adopt is one that says that the probability of heads is 0.5; that is, P\(heads\)=0.5P\(heads\)=0.5. If the coin is not fair, then I should conclude that the probability of heads is **not** 0.5, which we would write as P\(heads\)≠0.5P\(heads\)≠0.5. In other words, the statistical inference problem is to figure out which of these probability models is right. Clearly, the statistical question isn’t the same as the probability question, but they’re deeply connected to one another. Because of this, a good introduction to statistical theory will start with a discussion of what probability is and how it works.

### Difference

Think probability as a model of system. Given a probability \(model\), your system **will produce the data according to that probability model**. Hence probability has to do with that **model.**

Think statistics as about data generated from some probability distribution. You only have the generated data but that probability model of that data may be unknown. Hence **here you use to that data to infer about the probability model**. Hence statistics has to do with that **data.**

**Hence, probability and statistics are two components of a complete system.** 

