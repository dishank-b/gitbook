# Dataset/ Data loader

{% embed url="https://medium.com/speechmatics/how-to-build-a-streaming-dataloader-with-pytorch-a66dd891d9dd" %}

* collate\_fn:\
  It takes list of samples, where you get each sample form \_\_getitem\_\_() func of your dataset. So it this function basically get list of $$n$$samples, where n is your batch\_size. And turn it into batch sample.&#x20;
