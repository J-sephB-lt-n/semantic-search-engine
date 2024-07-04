"""Prints out text from consecutive random chunks 
(select input file by file index)"""

import argparse
import pathlib
import pickle
import random

from objects import Chunk, ChunkMetadata

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(dest="chunk_file_index", type=int)
args = arg_parser.parse_args()

chunked_input_filepaths: list[str] = [
    str(x) for x in pathlib.Path("./chunked_input").iterdir() if x.suffix == ".pickle"
]
selected_chunked_input_filepath: str = chunked_input_filepaths[args.chunk_file_index]
with open(selected_chunked_input_filepath, "rb") as file:
    chunks: list[Chunk] = pickle.load(file)

N_CONSECUTIVE_CHUNKS: int = 2
random_start_index: int = random.randint(0, len(chunks) - N_CONSECUTIVE_CHUNKS)

print(f"Printing random lines from {selected_chunked_input_filepath}")
for idx in range(N_CONSECUTIVE_CHUNKS):
    chunk_idx = random_start_index + idx
    chunk = chunks[chunk_idx]
    print(
        f"""
--- Chunk {chunk.chunk_num} in {chunk.metadata.source_doc} ---
{chunk.metadata.chunk_algorithm}
{chunk.metadata.chunk_algorithm_params}
{chunk.text}

"""
    )
