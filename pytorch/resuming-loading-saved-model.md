# Resuming/Loading Saved model

### Loading Model weights and optimizer

When you load pretrained weights for finetuning a network. Then after first iterations your loss actually increases than the pretrained network loss. It is because you didn't load the optimizer state, which may contains momentum of wights etc. And it takes few iterations to get the loss back to the pretrained converged loss value. 

Hence, if you want to finetune a model, you may want to load the optimizer as well. If you don't want to load the optimizer, then let the model train for first iterations untill it come back to it original converged loss and then you can do your own things.   
  
Note: If you only gonna use the pretrained model for evaluation and not gonna backprop though any loss, then you may not need to have optimizer state. 

### Batch norm Params

When you load the model, the running mean and variance are loaded for the batchnorm/dropout layers. Hence if you want to use it in eval mode, make sure to call `model.train().`



