---
description: Description of different clustering algorithms
---

# Clustering

## K Means Clustering

### Algorithm

The algorithm inputs are the number of clusters _Κ_ and the data set. The algorithms starts with initial estimates for the _Κ_ centroids, which can either be randomly generated or randomly selected from the data set. The algorithm then iterates between two steps:

*  Data assigment step:  
  Each centroid defines one of the clusters. In this step, each data point is assigned to its nearest centroid, based on the squared Euclidean distance. More formally, if $$c_i$$ is the collection of centroids in set _C_, then each data point _x_ is assigned to a cluster based on

                                                                          ![$$\underset{c\_i \in C}{\arg\min} \; dist\(c\_i,x\)^2$$](https://render.githubusercontent.com/render/math?math=%5Cunderset%7Bc_i%20%5Cin%20C%7D%7B%5Carg%5Cmin%7D%20%5C%3B%20dist%28c_i%2Cx%29%5E2&mode=display)

  where _dist_\( _·_ \) is the standard \( $$L_2$$ \) Euclidean distance. Let the set of data point assignments for each $$i_{th}$$ cluster centroid be $$S_i$$ .

* Centroid update step:  
  In this step, the centroids are recomputed. This is done by taking the mean of all data points assigned to that centroid's cluster.

                                                                            ![$$c\_i=\frac{1}{\|S\_i\|}\sum\_{x\_i \in S\_i x\_i}$$](https://render.githubusercontent.com/render/math?math=c_i%3D%5Cfrac%7B1%7D%7B%7CS_i%7C%7D%5Csum_%7Bx_i%20%5Cin%20S_i%7D%20x_i&mode=display)

The algorithm iterates between steps one and two until a stopping criteria is met \(i.e., no data points change clusters, the sum of the distances is minimized.   
**At optimum, the sum of distance of each point to its cluster centroid will be minimum.** 

### **Choosing K**

* Minimize the mean distance of data point to centroid : **Elbow Point** One of the metrics that is commonly used to compare results across different values of _K_ is the mean distance between data points and their cluster centroid. Since increasing the number of clusters will always reduce the distance to data points, increasing _K_ will _always_ decrease this metric, to the extreme of reaching zero when _K_ is the same as the number of data points. Mean distance to the centroid as a function of _K_ is plotted and the "elbow point," where the rate of decrease sharply shifts, can be used to roughly determine _K_.

## Hierarchical \(Agglomerative\) Clustering  

### Algorithm

Hierarchical clustering starts by treating each observation as a separate cluster. Then, it repeatedly executes the following two steps: 

*  identify the two clusters that are closest together.
* merge the two most similar clusters

![Steps of Hierarchical Clustering](../.gitbook/assets/image%20%2878%29.png)

![Dendogram, which shows association](../.gitbook/assets/image%20%2898%29.png)

### Linkage Criteria

After selecting a distance metric, it is necessary to determine from where distance is computed. For example, it can be computed between the two most similar parts of a cluster \(_single-linkage_\), the two least similar bits of a cluster \(_complete-linkage_\), the center of the clusters \(_mean_ or _average-linkage_\), or some other criterion. 

## Mean-Shift Clustering

Estimate modes of pdf

Mean shift considers feature space as a empirical probability density function. If the input is a set of points then Mean shift considers them as sampled from the underlying probability density function. If dense regions \(or clusters\) are present in the feature space , then they correspond to the mode \(or local maxima\) of the probability density function. We can also identify clusters associated with the given mode using Mean Shift.  
For each data point, Mean shift associates it with the nearby peak of the dataset’s probability density function. For each data point, Mean shift defines a window around it and computes the mean of the data point . Then it shifts the center of the window to the mean and repeats the algorithm till it converges. After each iteration, we can consider that the window shifts to a more denser region of the dataset.  
  
At the high level, we can specify Mean Shift as follows : 

* Fix a window around each data point.  
* Compute the mean of data within the window. 
* Shift the window to the mean and repeat till convergence.

![Three modes \(clusters\) of the probability distribution](../.gitbook/assets/image%20%2883%29.png)

**Kernel Density Estimation**

Kernel density estimation is a non parametric way to estimate the density function of a random variable. This is usually called as the Parzen window technique. Given a kernel K, bandwidth parameter h , Kernel density estimator for a given set of d-dimensional points is  


![](../.gitbook/assets/image%20%28132%29.png)



