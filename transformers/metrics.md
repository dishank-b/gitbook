# Metrics

## BLUE

&#x20;Used to compare generated translations,

Compared n-grams generated translation to the n-grams of ground truth reference translation.  n-grams essentially means chunks of n words. &#x20;

Average of precision of n-grams over different values of n

{% embed url="https://youtu.be/M05L1DhFqcw" %}

## ROUGE

Used for text summarization&#x20;

Compared n-grams of generated summary to the n-grams of ground truth reference summary.   &#x20;

calculate recall and precision of n-grams then calculate the F1 score.

Can do this for difference value of n.&#x20;

## Perplexity

This is piece about relation between - perplexity and bits-per-character (from information in sentence perspective), this helps understand how perplexity/cross entropy relates to information-theoretic motivation.

Metric to evaluate language models.

Perplexity is an exponent of cross entropy loss of generated output.&#x20;

<figure><img src="../.gitbook/assets/image (167).png" alt=""><figcaption></figcaption></figure>
