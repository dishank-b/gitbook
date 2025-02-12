# Speculative Decoding

{% embed url="https://research.google/blog/looking-back-at-speculative-decoding/" %}

* Faster **inference** for LLMs
* Parallel token computation
* For predicting 10 token in a sentence, 10 runs/decoding steps of LLMs has to be done (in series).
  * Slow
* Key observations about generation with LLMs
  * Some token are easier to predict, some need more compute/remembrance to predict.
    * "what's the square root of 7? Square root of _**7**_ is **2.blah blah**"
    * In above sentence, **7** is simply copying previous token, where as for **2.blah blah** we will gave to do some computation.
  * Memory is the bottleneck with GPUs, because parallelisation is very efficient for computation.&#x20;
    * Memory read/write is about 100 times slower than compute. i.e for every byte read in to memory, we can do about 100 compute operations in the meanwhile we read&#x20;

{% embed url="https://storage.googleapis.com/gweb-research2023-media/media/SpeculativeDecoding-0-AIO.mp4" %}

### [Speculative Execution](https://en.wikipedia.org/wiki/Speculative_execution)

Perform some operation in speculation of it happing in the future. ex, you are uploading an instagram image -> Already upload the image on the server when you editing in the instagram app locally, now if you actually move head with uploading, image will be uploaded instantly as it was uploading in the background, if you don't move ahead and discard your edits, then remove the uploaded image.&#x20;

### Speculative Sampling



### Speculative Decoding

* Use smaller network as proxy true model. Keep predicting with it and use larger model as verifier (true) model.
*   The prediction is done with a smaller model here

    <figure><img src="../.gitbook/assets/image (175).png" alt=""><figcaption></figcaption></figure>

{% embed url="https://medium.com/ai-science/speculative-decoding-make-llm-inference-faster-c004501af120" %}

{% embed url="https://arxiv.org/pdf/2211.17192" %}

## Multi-token prediction for Sepculative Decoding

{% embed url="https://epoch.ai/gradient-updates/how-has-deepseek-improved-the-transformer-architecture" %}



