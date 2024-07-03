"""
Combines all text files in /input_docs_txt/ into a single document, then chunks 
this master document using various different approaches, writing the 
results to /chunked_input/ as .pickle files
"""

import json
import itertools
import pathlib
import pickle
from typing import Final

from chunking_functions import chunk_by_fixed_size, chunk_by_paragraph
from objects import Chunk, ChunkMetadata

INPUT_DIRPATH: Final[str] = "./input_docs_txt"
OUTPUT_DIRPATH: Final[str] = "./chunked_input"

for path in pathlib.Path(OUTPUT_DIRPATH).iterdir():
    if path.is_file() and path.name != ".gitkeep":
        path.unlink()
        print(f"Deleted file [{path}]")

input_docs = {}
for path in pathlib.Path(INPUT_DIRPATH).iterdir():
    if path.is_file() and path.suffix == ".txt":
        with open(path, "r", encoding="utf-8") as file:
            input_docs[path.name] = file.read()

for chunker in (
    {"func": chunk_by_fixed_size, "params": {"chunk_nchar": 100, "overlap_nchar": 0}},
    {
        "func": chunk_by_fixed_size,
        "params": {"chunk_nchar": 100, "overlap_nchar": 20},
    },
):
    chunks: list[Chunk] = []
    for doc_name, text in input_docs.items():
        chunk_counter = itertools.count()
        for chunk in chunker["func"](text, **chunker["params"]):
            chunks.append(
                Chunk(
                    text=chunk.text,
                    start_index=chunk.start_index,
                    end_index=chunk.end_index,
                    chunk_num=chunk.chunk_num,
                    metadata=ChunkMetadata(
                        source_doc=doc_name,
                        chunk_algorithm=chunker["func"].__name__,
                        chunk_algorithm_params=json.dumps(chunker["params"]),
                    ),
                )
            )
    chunk_algorithm_desc = (
        chunker["func"].__name__
        + "-"
        + "-".join([f"{k}{v}" for k, v in chunker["params"].items()])
    )
    output_filepath = f"{OUTPUT_DIRPATH}/{chunk_algorithm_desc}.pickle"
    with open(output_filepath, "wb") as file:
        pickle.dump(chunks, file, protocol=pickle.HIGHEST_PROTOCOL)
        print(f"exported file [{output_filepath}")
