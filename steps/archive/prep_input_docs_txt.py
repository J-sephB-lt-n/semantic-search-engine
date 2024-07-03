"""
Creates the file prepped_input_data.pickle by combining all of the input 
documents in /input_docs_txt/ into a single document, then 
separating this into chunks 

Script usage:
    $ python -m src.prep_input_docs_txt
"""

import json
import pathlib
import pickle
import re
import warnings
from typing import Final

from src.objects import Chunk, ChunkMetadata

MAX_CHUNK_NCHARS: Final[int] = 500  # longer chunks are discarded
OUTPUT_FILEPATH: Final[str] = "./prepped_input_data.pickle"

chunk_counts: dict[str, int] = {}

chunks: list[Chunk] = []
for path in pathlib.Path("./input_docs_txt").iterdir():
    if path.is_file() and path.suffix == ".txt":
        chunk_counts[path.name] = {
            "n_chunks_total": 0,
            "n_chunks_discarded": 0,
        }
        with open(path, "r", encoding="utf-8") as file:
            all_text: str = file.read()
            for chunk in all_text.split("."):
                chunk_counts[path.name]["n_chunks_total"] += 1
                chunk = re.sub(r"\s+", " ", chunk.strip())
                if len(chunk) > MAX_CHUNK_NCHARS:
                    chunk_counts[path.name]["n_chunks_discarded"] += 1
                    warnings.warn(
                        f'Discarded chunk of length {len(chunk):,} "{chunk[:MAX_CHUNK_NCHARS]}..."'
                    )
                else:
                    chunks.append(
                        Chunk(text=chunk, metadata=ChunkMetadata(source_name=path.name))
                    )

print("\n--SUMMARY OF DATA PREPROCESSING--")
print(json.dumps(chunk_counts, indent=4))

with open(OUTPUT_FILEPATH, "wb") as file:
    pickle.dump(chunks, file, protocol=pickle.HIGHEST_PROTOCOL)

print(f"Exported prepped input data to {OUTPUT_FILEPATH}")
