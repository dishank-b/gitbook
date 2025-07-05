# CLIP

Very crucial paper in terms of getting text and images onto the same representation space. This paper introduces, how to learn embedding for both images and text on to shared representation space.&#x20;

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### Kye points

* Training works with paired image-caption pairs.
* Contrastive learning objective.
* The Model can be used for classification.&#x20;
* The classification is here zero-shot, so clip is zero shot classifier.&#x20;
* CLIP is competitive with other supervised ResNet classifiers.&#x20;
* The CNN encoder + Text encoder are trained from scratch.&#x20;

### Baseline architecture&#x20;

1.  CNN + BoW caption encoding prediction. \
    **Step-by-step Baseline (CNN → BoW Text):**

    1. **Image Encoder**: A CNN (e.g., ResNet-50) encodes the input image into a feature vector.
    2. **MLP or Linear Head**: The image feature vector is passed through a simple MLP or linear layer.
    3. **Output Layer**: The final output layer has dimensionality equal to the vocabulary size. The output is a multi-label prediction (each position represents the likelihood of a particular word appearing in the caption).
    4. **Training Objective**: Binary cross-entropy loss is used against the BoW representation of the caption (i.e., a 0/1 vector indicating which words are present).

    **This is effectively a multi-label classification task.**
2.  CNN + Text Transformer for full caption prediction.&#x20;

    This is the **VirTex-style setup**, which is much heavier:

    **Step-by-step Captioning Pipeline (CNN + Transformer):**

    1. **Image Encoder**: A CNN (e.g., ResNet-50) processes the image into a visual feature map (or a global feature vector, depending on the architecture).
    2. **Visual Features to Text**: These visual features are passed to a **Transformer decoder** or a full **encoder-decoder** architecture. The transformer autoregressively **generates the caption token-by-token**.
    3. **Training Objective**: Cross-entropy loss is used to train the model to predict the next word in the caption given the image and previous words.

    This is a **sequence generation task**, which is **much more computationally intensive** and harder to train — especially from scratch.\
    \


    In a setup similar to VirTex or early CLIP experiments:\
    CNN + Transformer **Decoder-only** (like GPT)

    * You have:
      * A CNN (e.g. ResNet) that outputs a **global feature vector** (e.g. 2048D).
      * A Transformer **decoder** that autoregressively generates text.

    **🔄 How to Connect Them**

    1. **Linear Projection**:\
       Project the CNN feature vector to the same dimensionality as the transformer's hidden size (e.g., 768D for GPT-2).
    2.  **Use as Prefix**:\
        Treat this projected image embedding as a **“pseudo-token”** — prepend it to the token embeddings of the caption.

        ```
        cssCopyEdit[Image_Embed] + [Token1, Token2, ..., TokenN]
        ```
    3. **Positional Embedding**:\
       Assign the image vector a position (e.g., position 0). Then add positional embeddings as usual.
    4. **Causal Masking**:\
       Use causal masking so that the model can attend to the image embedding and the previous tokens only.



    #### CNN + Transformer **Encoder-Decoder**

    This is more like traditional seq2seq translation (e.g., Vision → Text).

    **🔄 How to Connect Them**

    1.  **CNN Outputs a Grid**:\
        Instead of a global feature vector, use intermediate CNN feature maps (e.g., from a ResNet stage) shaped like:

        ```
        cssCopyEdit[C, H, W] → flatten to → [HW, C]
        ```

        So the image becomes a sequence of visual tokens — very similar to how ViT works.
    2. **Project to Hidden Size**:\
       Each \[C]-dim vector is linearly projected to match the transformer's hidden size (e.g., 512 or 768).
    3. **Add Positional Embeddings**:\
       Use learned or sinusoidal 2D positional embeddings for each patch.
    4. **Feed to Transformer Encoder**:\
       The encoder receives this sequence of visual embeddings (with position info) and encodes them.
    5. **Text Decoder Cross-Attends to Encoder Outputs**:\
       The Transformer decoder generates the caption token-by-token, attending (via cross-attention) to the image encoder outputs.

### Training

#### Contrastive Pre-training part

* You have paired image/text.&#x20;
* You pass them through respective image and text encoders, to get their respective embedding/latent representations.&#x20;
* You do the dot/inner product for each of the images and text in the dataset. You will get a 2D matrix that will have scalar dot product between all the images and text, as shown in image (a) above.&#x20;
* For each image, there's one dot product that should be higher than others, the dot produdct with its own text embedding. And it should be zero with others.&#x20;
* So you can assume to have a softmax classification loss for each image row and similarly for each column, to train/fine-tune the image and text encoder.&#x20;
* **Caveat -**&#x20;
  * There's no loss to make the embedding of similar looking images same.
  * Or there might me more images/text pair of similar objects. And if they are in the same batch, you would penalize theire embedding dot product which is not desirable.&#x20;

### Inference

* For the available classes, you create dummy text caption. like given a class dog, caption could be - "A photo of dog".
  * For 1K classes, you have 1k text/captions.&#x20;
* Now given an image, you get its embedding from the image encoder. Get text embedding for all the generated class captions.&#x20;
* Choose the text with highest dot product with image embedding, choose the class corresponding to that text caption.&#x20;

### Architecture

* Text encoder is a transformer, the embedding corresponding to the last token is the sequence is the embedding.&#x20;
* For the image encoder, you can use ResNet or Vision transformer.&#x20;



<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
