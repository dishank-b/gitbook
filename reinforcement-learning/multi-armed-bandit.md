# Multi-armed Bandit

This problem is about allocation of fixed resources between competing (alternative) choices in a way to maximize the expected gain. The choice's properties are only partially known when doing the allocation and can only be better understood as time passes and you have more observation about each choice's return based on your allocation, etc.

Basically, you start with a system which have multiple options, each option when chosen can provide some return, based on it's probability distribtion. But when you start, you have no information about each option's inherent return distribution. And you are the user who wanted to allocated their resources to this different options in this system and maximize their total return. So as time passes, you interact with machines, allocating your resources and observing each machine's return. Hence, the problem here is to come with a strategy to allocate resources overtime when only partial information is available about the option.&#x20;

This also related with exploration-exploitation dilemma, since at each time you have two options - put your resources in the maximum return option untill now, or you use your resources to find out if possible any other machine might be giving even higher return?&#x20;

### Solution

One way to solve this problem is using Thompson sampling. Check the article on it.&#x20;

[thompson-sampling.md](../probability-and-statistics-1/sampling/thompson-sampling.md "mention")

