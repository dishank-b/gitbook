# iCaRL: Incremental Classifier and Representation Learning

## Summary

New training strategy to learning in class-incremental setting without catastrophic forgetting. Only the training data for a small number of classes has to be present at the same time and new classes can be added progressively. 

It simultaneously learns classifiers and feature representations in the class-incremental setting. 

Conponents:

* classification by a nearest-mean-of-examplars rule
* prioritized exemplar selection based on herding.
* representation learning using knowledge distillation and prototype rehearsal. 

## Background

**Class Incremental Setting**: When stream of data is provided to train and different classes occur at different time. Computational requirement and memory footprint should remain bounded. 

**Catastrophic forgetting:** When naively use SGD for training in class incremental training, the classification accuracy deteriorates as more classed comes, because network forgets about previous classes seen during training. 

## Methodology

**Classification:** sets $$P1, ...P_t$$of exemplar images, each set corresponding to each class of image. Total number of exemplar images never exceeds parameter K. 

**mean-of-exemplars classifier:**

![](../.gitbook/assets/image%20%28163%29.png)

**Training:** This procedure determines the update of network weights and exemplar sets, etc. 

![](../.gitbook/assets/image%20%28164%29.png)

**Architecture:** We interpret the network as a trainable feature extractor, ϕ : X → Rd, fol- lowed by a single classification layer with as many sigmoid output nodes as classes observed so far. All feature vectors are L2-normalized, and the results of any operation on feature vectors, e.g. averages, are also re-normalized, which we do not write explicitly to avoid a cluttered notation.



