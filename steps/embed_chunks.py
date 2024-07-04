"""Generate vector representations of the chunks under each 
chunking method"""

import pathlib
import pickle

import lancedb
from sentence_transformers import SentenceTransformer

from objects import Chunk, ChunkMetadata

chunked_input_filepaths: list[pathlib.Path] = [
    path
    for path in pathlib.Path("./chunked_input").iterdir()
    if path.is_file() and path.suffix == ".pickle"
]

db = lancedb.connect("./.lancedb")
embed_model = SentenceTransformer(
    "Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True
)

for input_num, input_path in enumerate(chunked_input_filepaths, start=1):
    print("Started chunk", input_num, "of", len(chunked_input_filepaths))
    with open(input_path, "rb") as file:
        chunks = pickle.load(file)
    table = db.open_table(input_path.stem)
    table.add(
        [
            {
                "chunk_num": c.chunk_num,
                "source_doc": c.metadata.source_doc,
                "chunk_alg": c.metadata.chunk_algorithm,
                "chunk_alg_params": c.metadata.chunk_algorithm_params,
                "char_start_index": c.start_index,
                "char_end_index": c.end_index,
                "vector": embed_model.encode(c.text),
                "text": c.text,
            }
            for c in chunks
        ]
    )
