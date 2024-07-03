"""Prints out text from consecutive random chunks"""

import argparse
import pickle
import random

from objects import Chunk, ChunkMetadata

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-f",
    "--chunk_file",
    help="Chunk filepath to select random chunks from",
    required=True,
)
args = arg_parser.parse_args()

with open(args.chunk_file, "rb") as file:
    chunks: list[Chunk] = pickle.load(file)

N_CONSECUTIVE_CHUNKS: int = 2
random_start_index: int = random.randint(0, len(chunks) - N_CONSECUTIVE_CHUNKS)

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
