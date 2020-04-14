---
description: Efficient TensorFlow usuage
---

# TensorFlow

* Try to not use feed dicts for input. tf.data is good for input pipeline.
* Fused Batch Norm is comparative faster than non-fused batch norm implementation.
* You can use compile TF to use intel MKL to speed ups.

The only functionality I’m struggling with, is the `.shuffle(buffer_size)`function. This, like the `map()` and `.batch()` function, can be applied on a dataset, to create a new dataset, loads the first `buffer_size` elements into memory and shuffles them. [Here](https://github.com/tensorflow/tensorflow/issues/7951#issuecomment-305435143) I explained the problem, given an example, that can arise from this function, that we as users need to be aware of. But in short: If your initial list of samples \(image path + label\) is ordered, so that you all samples of the first class in the beginning, followed by all samples of the second class etc., and your `buffer_size` is smaller than the number of samples you have of each class, you will have batches with samples of only one class and your model will not train. Therefore we need to take care of an initial shuffling ourselves and not rely on TensorFlows shuffling.





**Tensorflow in Practise**

 **-**[**https://github.com/vahidk/EffectiveTensorflow**](https://github.com/vahidk/EffectiveTensorflow)  
****

* **Debugging Steps:**
  * **Step 1: Check the architecture**
  * **Step 2: Check the hyper-parameters of neural network**
  * **Step 3: Check the Complexity of network**
  * **Step 4: Check the Structure of Input data**
  * **Step 5: Check the Distribution of data**
* **Static and Dynamic Shapes:  .get\_shape\(\) - gives the static shape of the tensor. = Static tf.shape\(x\) - returns the op to get the shape of x at the runtime.  = Dynamic  Note: The static shape is very useful to debug your code with print so you can check your tensors have the right shapes.**
* **Getting Validation and training loss using same loss op.  Loss\_op = tf.losse\(something\)**
  * **Now if you want val loss and train loss on same plot. -Then make two writers - When adding the training\_loss\_summ, add it to one writer. - When adding the validation\_loss\_summ, add it to 2nd writer**
  * **If you want two plot, one having training error and other having val error. Then just create two loss\_summ ops with same loss\_ops.** 
* **tf.AUTOREUSE -** 
  *  **tf.AUTO\_REUSE which tells TensorFlow to create a new variable if a variable with the same name doesn't exist, and reuse otherwise:**
  * **with tf.variable\_scope\("scope", reuse=tf.AUTO\_REUSE\):   features1 = tf.layers.conv2d\(image1, filters=32, kernel\_size=3\)   features2 = tf.layers.conv2d\(image2, filters=32, kernel\_size=3\)**
* **Python ops:  def py\_input\_fn\(\):     actual\_data = np.random.normal\(size=\[100\]\)     return actual\_data  data = tf.py\_func\(py\_input\_fn, \[\], \(tf.float32\)\)**
* * **Python ops allow you to convert a regular Python function to a TensorFlow operation.**
* **DataSet API is also useful.** 
* **Overload Operators:**
  * **z = -x  \# z = tf.negative\(x\)**
  * **z = x + y  \# z = tf.add\(x, y\)**
  * **z = x - y  \# z = tf.subtract\(x, y\)**
  * **z = x \* y  \# z = tf.mul\(x, y\)**
  * **z = x / y  \# z = tf.div\(x, y\)**
  * **z = x // y  \# z = tf.floordiv\(x, y\)**
  * **z = x % y  \# z = tf.mod\(x, y\)**
  * **z = x \*\* y  \# z = tf.pow\(x, y\)**
  * **z = x @ y  \# z = tf.matmul\(x, y\)**
  * **z = x &gt; y  \# z = tf.greater\(x, y\)**
  * **z = x &gt;= y  \# z = tf.greater\_equal\(x, y\)**
  * **z = x &lt; y  \# z = tf.less\(x, y\)**
  * **z = x &lt;= y  \# z = tf.less\_equal\(x, y\)**
  * **z = abs\(x\)  \# z = tf.abs\(x\)**
  * **z = x & y  \# z = tf.logical\_and\(x, y\)**
  * **z = x \| y  \# z = tf.logical\_or\(x, y\)**
  * **z = x ^ y  \# z = tf.logical\_xor\(x, y\)**
  * **z = ~x  \# z = tf.logical\_not\(x\)**
* **Order of Execution and Control Dependencies. Directly see this from the above mentioned website. This defines the order of execution of ops which may not be much clear while making the graphs.** 
* **Some Important Fucntions in TF:**
  * **Tf.cond - Works as if in python**
  * **Tf.where -** 
  * **tf.TensorArray - This allow growing tensor array, with no definite shape.**
* **Make sure that when using softmax, you have to computer e^x, now that float value can only store upto 3.40282e+38, a hence max value of x allowed is ln\(3.40282e+38\) = 88.7, hence have to make sure that activation of final layer is below that value.** 
* **See the batch norm specified in the last of above website.** 
* **Batch Norm Issues:**
  * **See the bookmarks in DL folder.** 
  * **Use update\_graphkey as before train\_op. Or use update\_collection=None as parameters in contrib batch\_norm.**
  * **Also make right use of reuse parameter in the function.**  
* **Small batch size is better than large batch size for less generalization gap.**

