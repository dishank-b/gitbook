# Entropy

**This measures the expected amount of information (bits) needed to describe the state of the variable, considering the distribution of probabilities across all potential states.**

**For example: In a two coins toss, if we need to tell the state of two coins, we need two bits to tell the state. Similar for a die roll, we will need** $$\log_2 6$$ **bits to tell the state of dice (i.e the number from 1-6).**&#x20;

In information theory, the major goal is for one person (a _transmitter_) to convey some message (over a _channel_) to another person (the _receiver_). To do so, the transmitter sends a series (possibly just one) partial messages that give clues towards the original message. The **information content** of one of these partial messages is a measure of how much uncertainty this resolves for the receiver. For instance,

* A partial message that cuts the number of possibilities in half transmits one **bit** of information about the message. For instance, if the transmitter were trying to transmit the result of a randomly chosen digit to the receiver, the partial message "the number is odd" would transmit one bit of information.
* A partial message that doesn't reduce the number of possibilities at all transmits **no** information at all; for instance, the partial message "the number is less than 10" transmits zero bits of information.

In essence, the "information content" can be viewed as how much useful information the message _actually_ contains.

The **entropy**, in this context, is the _expected_ number of bits of information contained in each message, taken over all possibilities for the transmitted message. For example, suppose the transmitter wanted to inform the receiver of the result of a 4-person tournament, where some of the players are better than others. The entropy of this message would be a weighted average of the amount of information each of the possible messages (i.e. "player 1 won", "player 2 won", "player 3 won", or "player 4 won") provides.

In essence, the "entropy" can be viewed as how much useful information a message is _expected_ to contain. It also provides a lower bound for the "size" of an encoding scheme, in the sense that the expected number of bits to be transmitted under some encoding scheme is at least the entropy of the message. An encoding scheme that manages to achieve this lower bound is called _lossless_.



Entropy is the expected amount of information in an event.

$$
H(p) = - E[\log p] = \sum p\log p
$$

KL divergence

$$
KL(p|q) = E_p[\log \frac{p}{q}] = \sum p\log \frac{p}{q} \\ = H_p(q)-H(p) \\ = \text{cross entropy - entropy}
$$

Mutual information - attempt to measure the correlation between to RV

$$
I(X;Y) = H(X)+H(Y) - H(X,Y)
$$
