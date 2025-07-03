# Vision Transformers ViT

{% embed url="https://youtu.be/TrdevFK_am4" %}

<figure><img src="../.gitbook/assets/image (182).png" alt=""><figcaption></figcaption></figure>

### KeyPoints

* Trained using Cross entropy loss similar to CNNs
* Just instead of using CNNs, it uses transformers architecture.&#x20;
* Because of using transformers, we have to represent an image as patches, which means tokens.&#x20;

### How Image is tokenized and embedded

* Image is decomposed into patches of 16x16.&#x20;
* Let's say there are 9 patches, so each patch will have a position embedding. That can be learned in a lookup table. For example, if positoin embedding if of size 128, the table will have 128 columns and 9 rows, ie each row have 128 dimensional learnable vector. We can take that position embedding based on what's the location of patch. \
  You can add or concatenate the position embedding to the image patch embedding.&#x20;
* Now the image patch is of size 16x16. You flatten this, now you have 256 dimensional vector correcponding to the patch. Now you you can pass this patch vector through a MLP/linear projection and you will get your patch embedding. \
  This linear project is represented as $$E$$ of dimension, output\_dim x 256, where output\_dim is the dimension you want for your patch embedding to be. Then let's say your patch vector is $$v$$ which is 256 dimensional. Then you can get your patch embedding as $$Ev$$ . All the patch vectors are projected using the projection embedding matrix. \
  (**Note since image have 3 channels, it will be 16\*16\*3 dimension vector for the patch**)
* Now you have patch embedding and position embedding from lookup table, you can either add or concatenate these. And these are essentially the input to your transformer.&#x20;

### Training

ViT is trained using a simple classification loss. Each image has a class label, and the transformer is supposed to predict the class label.&#x20;

So for training transformers, each token has an output associated with it. And we have an target output corresponding to each token, that we use as reference to calculate the loss.&#x20;

In this case, a token with learnable embedding is appended in the beginning of image pathces input embedding sequences, token representing \`\[class]\`.&#x20;

At the end of transformer, the output corresponding to the first token, it used as the target, then the cross entropy loss is applied between the output and target class.&#x20;

### Pre-Training and Fine-tuning

* First there is a pre-trainign phase and then there is a fine-tunign phase, where the network's final layers is trained again for the new classes.&#x20;
* Pre-train the network on Imagenet 1k, imagenet 21K and JFT Dataset.
* Fine-tune on some other dataset,&#x20;

### Metrics for evaluations

* Fine-tuning accuracy on transfer datasets
* Few shot accuracy



