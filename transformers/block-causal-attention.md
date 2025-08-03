---
description: >-
  Allows for Linear scaling of attention calculation with respect to sequence
  length
---

# Block Causal Attention

{% embed url="https://chatgpt.com/share/688f654f-8b70-8007-810a-fa3400a1b2fe" %}

Vectorized way to general block causal mask

<pre class="language-python"><code class="lang-python"><strong>L, B = 16, 4
</strong><strong>
</strong><strong>idx = np.arange(L)          # [0, 1, …, L-1]
</strong>row = idx[:, None]             # shape [L, 1]
col = idx[None, :]             # shape [1, L]

same_block   = (row // B) == (col // B)
lower_tri    = (row %  B) >= (col %  B)
mask_bool    = same_block &#x26; lower_tri    # logical AND

print(np.where(mask_bool, 1, 0))
</code></pre>
