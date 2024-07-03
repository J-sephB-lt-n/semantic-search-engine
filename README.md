# semantic-search-engine

Tool for searching for passages within a document

```bash
pdftotext TheEffectiveExecutive.pdf input_docs/TheEffectiveExecutive.txt
python -m steps.chunk_input # input written to /chunked_input/
python -m observe.chunk_stats.py
python -m observe.view_chunks.py --chunkfile "chunked_input/" --chunknums="TODO"
```

<https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5>

Note about cached huggingface models: the following opens up a UI for deleting models no longer needed:

```bash
pip install huggingface_hub[cli]
huggingface-cli delete-cache
```

# TODO

- Investigate different chunking strategies

- Investigate ANN, indexing, distnace metrics etc. in lancedb

- Investigate different chunking strategies

- Implement batch data insert into semantic database
