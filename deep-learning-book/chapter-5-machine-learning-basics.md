# Chapter 5: Machine Learning Basics

### I.I.D Assumptions of data-generating process

Let's say we have have training and test dataset. Then the examples in each dataset are independent from each other i.e sampling of one example doesn't affect the sampling of others. So, for example, in object detection , we collect data inform of video and then annotate it. Now, it's very important that we shuffle the frames, otherwise examples in dataset will be in sequence of each other and hence not independent. Also, the training and test test should be identically distributed i.e it should not be the case that either of dataset is biased with some particular kind of examples, in other words, examples in each data should follow the same probability distribution. me

We call it data-generating distribution $$p_{data}$$.

