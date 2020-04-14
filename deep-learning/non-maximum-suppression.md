# Non-Maximum Suppression

\*\*\*\*[**https://www.coursera.org/lecture/convolutional-neural-networks/non-max-suppression-dvrjH**](https://www.coursera.org/lecture/convolutional-neural-networks/non-max-suppression-dvrjH) **- this is enough to understand NMS.**

When multiple proposals may correspond to a single object, which renders all but one proposal to be false-positive. Non-maximum suppression \(NMS\) solves this problem by clustering proposals by spatial closeness measured with IoU and keeping only the most confident proposals among each cluster.

Two of NMS: 

* Greedy
* Optimal

### Greedy

![Greedy NMS algo](../.gitbook/assets/image%20%28140%29.png)

### Optimal

![](../.gitbook/assets/image%20%2874%29.png)

### Hyper-parameters

**Score Threshold**

Any proposals with confidence less than the score threshold are rejected.

**Overlap Threshold**

Two proposals are considered to be in the same cluster when their IoU is larger than the overlap threshold

