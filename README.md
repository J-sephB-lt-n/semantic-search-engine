# semantic-search-engine

Tool for searching for passages within a document

```bash
pdftotext TheEffectiveExecutive.pdf input_docs/TheEffectiveExecutive.txt
```

<https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5>

Note about cached huggingface models: the following opens up a UI for deleting models no longer needed:

```bash
pip install huggingface_hub[cli]
huggingface-cli delete-cache
```
