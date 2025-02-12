# KV Cache

### Practical Implications of KV Cache

[https://epoch.ai/gradient-updates/how-has-deepseek-improved-the-transformer-architecture#:\~:text=What%20is%20the%20KV%20cache%20and%20why%20does%20it%20matter%3F](kv-cache.md#practical-implications-of-kv-cache)

Store the key value for past tokens when auto regressively generating tokens. This is called KV Cache.

Size of KV cache per token = 2 (for key and value) \* attention head dim \* number of attention heads \* number of transformer blocks

if 1 byte for each float number, then for a KV cache size of 2.26M params, it's 4.7 MB per token. &#x20;

Now if you have let's say 100K of context size, then total cache size becomes = 470 GB of memory.&#x20;

That's around 140 ms of H100 time given the H100’s HBM bandwidth of 3.3 TB/s. The price per million tokens generated at $2 per hour per H100 would then be $80, around 5 times more expensive than Claude 3.5 Sonnet’s price to the customer (which is likely significantly above its cost to Anthropic itself).

**Hence, we would need to reduce this memory size by alot, using different techniques. --> Speculative Sampling with one of them**&#x20;



