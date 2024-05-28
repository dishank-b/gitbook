# Tokenziation

Tokenization is a way to break down a string of continuous text into small individual chunks called tokens, each token can be a word/character/sub-word.&#x20;

Different tokenization schemes can be used based on different aspects.&#x20;

So let's say your tokenizer divided the whole text corpus into $$T$$ tokens i.e. there are your text is divided into total $$T$$chunks of smaller words, characters, sub-words, etc. **Now this** $$T$$ **becomes the Vocabulary size of your model.**&#x20;

Each token has an `token_id` $$\in [1, T]$$.&#x20;

{% embed url="https://huggingface.co/learn/nlp-course/chapter2/4" %}

