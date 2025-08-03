# V-JEPA / V-JEPA 2

## V-JEPA

<figure><img src="../.gitbook/assets/image (183).png" alt=""><figcaption></figcaption></figure>

### Keypoints

* Unsupervised/Self supervised learning for feature prediction/repsentation.
* More importantly, learning predictive features, ie latent representation that is predictive of the underlying observation.&#x20;
* This is under the hypothesis that we as humans don't really work at pixel level, but on the abstract latent representation of pixel images.&#x20;
* Models trained with feature prediction are superior to pixel prediction approaches under a frozen evaluation protocol (attentive probing - this is alternative to linear probing?) and are competitive with pixel prediction under full fine-tuning, while using significantly shorter training schedules (Tables 5 and 6).

### Approach

* Imagine video as multiple frames stacked together, making a spatio-temporal vector.&#x20;
* Tubes of videos are masked - patches at same location in each frames are masked. The masking is random, ie multiple tubes across spatial-temporal dimensions are masked. <img src="../.gitbook/assets/image (184).png" alt="" data-size="original">
* Y is the masked patched tube whereas the x is the remaining.&#x20;
*   X is passed to the encoder to get the latest/feature representation, predictor learns to predict masked feature presentation, given the x's feature representation and z - which is the location of masked featurs. \


    <figure><img src="../.gitbook/assets/image (185).png" alt=""><figcaption></figcaption></figure>
*   Then feature/latent presentation is predicted by encoder for y, and then L1 loss is computed. \


    <figure><img src="../.gitbook/assets/image (186).png" alt=""><figcaption></figcaption></figure>
* Pooling stretegy to use feature presentation for downstream tasks
  * Instead of using linear probing - you train a linear layer taking feature/latent vector as input and output as being whatever your downstream tasks requires, they use attentive probing - we learn a cross-attention layer with a learnable query token. The output of the crossattention layer is then added back to the query token (residual connection), and then fed into two-layer MLP with a single GeLU activation, followed by a LayerNorm, and finally a linear classifier.



## V-JEPA 2

V-JEPA 2 uses V-JEPA as a pre-training step. \


<figure><img src="../.gitbook/assets/image (188).png" alt=""><figcaption></figcaption></figure>

### Approach

* Pre-training\
  ![](<../.gitbook/assets/image (190).png>)
  * Scaling done compared to V-JEPA
    * Data Scaling - 2 M to 22M videos
    * Params - 300M to 1 B
    * Longer training
    * Higher resolution (256->384) and longer videos (16->64 frames)
  * Used RoPE (Rotary Position Embedding) as opposed to absolute sin-cos positino embedding from V-JEPA
  * To process a video\
    with our transformer encoder, we first patchify it as a sequence of tubelets of size 2 × 16 × 16 (T × H × W) and employ the same multiblock masking strategy as in V-JEPA.
  * We leverage the warmup-constant-decay schedule to efficiently scale to higher\
    resolution video and longer video clips by training on shorter, lower-resolution clips during the warmup and constant phases, and then increasing resolution and/or clip-length during the final decay phase.
* Post-training\
  ![](<../.gitbook/assets/image (189).png>)
  * Encoder is kept frozen from pre-training
  * Train frame-causal action-conditioned world model which is the "predictor" in V-JEPA
    * 300M param transformer model with block causal attention.&#x20;
    * Predicts latent representation of next/future video grames given action and previous  latent representation. &#x20;
    * Trained on 62 hour of unlabelled interaction data - by unlablled it should mean no reward data, or type of task, etc. Videos are generally 3-4 second long.&#x20;
  * Input to the model
    * About 4 seconds of videos, videos are samples at 256x256, sampled at 4 fps. Hence yielding 16 frames per video as input. Denoted by $$(x_k)_{k \in [16]}$$. \
      The robot’s end-effector state in each observation is denoted by the\
      sequence $$(s_k)_{k∈[16]}$$. Constructed a sequence of actions $$(a_k)_{k∈[15]}$$ by computing the change in end-effector state between adjacent frames.
    * We use V-JEPA 2 encoder E(·) as an image encoder and encode each frame independently in a given clip to obtain a sequence of feature maps $$(z_k)_{k∈[16]}$$
  * Loss
    *   Feature consistency loss, learning the predictor.&#x20;

        <figure><img src="../.gitbook/assets/image (191).png" alt=""><figcaption></figcaption></figure>


    * Two-step Rollout loss, to improve's model's ability to do autoregressive rollouts. ![](<../.gitbook/assets/image (192).png>)
      * Use T=2 here.&#x20;
* Inference - Planning using learn model via MPC to infer actions.&#x20;
  * Given an image of the goal state, we leverage V-JEPA 2-AC for downstream tasks\
    by planning. Specifically, at each time step, we plan an action sequence for a fixed time horizon by minimizing a goal-conditioned energy function.
  * Given a goal image, you plan actoins via MPC such that your actions taken you the goal images' latent representation.&#x20;



### Architectural details

* Encoder - 1 B params
* Encoder pre-training with 1M hours of video -&#x20;



### Experimental Details

* Action conditioned predictor trained on Droid dataset - 62 hours of data.&#x20;
* Droid Dataset
  * exocentric videos of franka arm
  * Corresponding to each frame, we have end-effectors state (position, rotation and gripper state)

###
