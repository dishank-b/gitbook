---
description: A guide to research
---

# How To Do Research

#### Guides

* ML Specific: [http://joschu.net/blog/opinionated-guide-ml-research.html](http://joschu.net/blog/opinionated-guide-ml-research.html)
* [http://www.cs.virginia.edu/\~robins/YouAndYourResearch.html](http://www.cs.virginia.edu/\~robins/YouAndYourResearch.html)
* [http://michaelnielsen.org/blog/principles-of-effective-research/](http://michaelnielsen.org/blog/principles-of-effective-research/)

## Few Types of the Good Research Direction

* Groundbreaking result that changed your perspective on some problem - This means result which shows very interesting or unexpected result, that might not be very obvious or are different than expectation.
* An algorithmic idea that's reusable - it's a idea that is kind of fundamental and not very specific for particular use. For example, dropout, batchnorm, anchors/region proposals, SAC, DDPG, etc are fundamental algorithms.&#x20;
* Deep insight about some recurring questions - This seems very related to the 1st point.&#x20;

## Choosing Problems

### Honing Your Taste

This is about the art of assesing problem statements. More of a over time development thing. Comes with the experience and repition. But few things to do:

* Read a lot of papers, and assess them critically.&#x20;
  * Critical assesment is very important, it allows you to see what is lacking the paper and where you might improve that thing. Also is there any flaw/problem which might induce new direction in the topic.&#x20;
* Talking to people about their research. Going to reading groups.

### **Idea-Driven vs Goal-Driven Research**

* **Idea-driven:** Follow some sector of the literature. As you read a paper showing how to do X, you have an idea of how to do X even better. Then you embark on a project to test your idea.
* **Goal-driven:** Develop a vision of some new AI capabilities you’d like to achieve, and solve problems that bring you closer to that goal. (Below, I give a couple case studies from my own research, including the goal of using reinforcement learning for 3D humanoid locomotion.) In your experimentation, you test a variety of existing methods from the literature, and then you develop your own methods that improve on them.

One major downside of idea-driven research is that there’s a high risk of getting scooped or duplicating the work of others. Researchers around the world are reading the same literature, which leads them to similar ideas. To make breakthroughs with idea-driven research, you need to develop an exceptionally deep understanding of your subject, and a perspective that diverges from the rest of the community—some can do it, but it’s difficult.

Goal driven research can also be much more motivating. You can wake up every morning and imagine achieving your goal—what the result would look like and how you would feel. That makes it easier to stick to a long-running research program with ups and downs

Basically sub-goals of your goal-driven research can be idea-driven research. But should always have the bigger picture in your mind. And your main goal should be a thesis and not only a paper.&#x20;

**Goal Driven Research: Restrict Yourself to General Solutions**

One pitfall of goal-driven research is taking your goal too literally. If you have a specific capability in mind, there’s probably some way to achieve it in an uninteresting way that doesn’t advance the field of machine learning. You should constrain your search to solutions that seem general and can be applied to other problems.

For example, while working on robotic locomotion, I avoided incorporating domain information into the solution—the goal was to achieve locomotion in simulation, _in a way that was general and could be applied to other problems_. I did a bit of feature engineering and reward shaping in order to see the first signs of life, but I was careful to keep my changes simple and not let them affect the algorithm I was developing. Now that I am using videogames as a testbed, I make sure that my algorithmic ideas are not specific to this setting—that they equally well could be applied to robotics.

### Aim High

* Always choose a work which gives 10x improvement rather than 10% improvement. But you can have sub-goals which give 10% increment for your 10x improvement.&#x20;
* Never choose unimportant problems. Always choose something that's more a fundamental goal in itself.&#x20;
* During your day-to-day work, you’ll make incremental improvements in performance and in understanding. But these small steps should be moving you towards a larger goal that represents a non-incremental advance.
* If you are working on incremental ideas, be aware that their usefulness depends on their complexity. A method that slightly improves on the baseline better be very simple, otherwise no one will bother using it—not even you. If it gives a 10% improvement, it better be 2 lines of code, whereas if it's a 50% improvement, it can add 10 lines of code, etc. (I’m just giving these numbers for illustration, the actual numbers will obviously depend on the domain.)
* Go back and look at the list of machine learning achievements you admire the most. Does your long-term research plan have the potential to reach the level of those achievements? If you can’t see a path to something that you’d be proud of, then you should revise your plan so it does have that potential.

## Making Continual Progress

* Keep a notebook, where you record your ideas and progress.
  * Create a entry for each day. Write about  experimental findings, insights (which might come from me, my colleagues, or things I read), code progress (what did I implement), and next steps / future work.&#x20;
  * Review your notebook from time to time, it will help you filling missing pieces which might be there from last time. Will help you to build up on your old ideas with your new knowledge.
* &#x20;When to switch problems/methods is art you need to excel at research. Sometime, it is of very importance to know that now it's time to change the problem, you should realise if it's a lost cause and not wasting your time in pursuing it.&#x20;
  * But don't keep switching frequently. Sometimes the idea has the potential to work, it just more time to work.&#x20;

## Personal Development

* You should allocate some fraction of your time towards improving your general knowledge of ML as opposed to working on your current project.
* You should choose a small set of relevant textbooks and theses to gradually work through. Don't just read papers, textbooks are more dense way to absorb knowledge.&#x20;
* You can also read PhD thesis. They are also exhaustive source of information about one particular subtopic. &#x20;
* Besides reading seminal papers and reimplementing them, you should also keep track of the less exceptional papers being published in your field. Reading and skimming the incoming papers with a critical eye helps you notice the trends in your field (perhaps you notice that a lot of papers are using some new technique and getting good results—maybe you should investigate it). It also helps you build up your taste by observing the dependency graph of ideas—which ideas become widely used and open the door to other ideas.

****

