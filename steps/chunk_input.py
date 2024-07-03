"""
Chunks every text file in /input_docs_txt/ using various different
approaches, writing the results to /chunked_input/ as a .pickle file
"""

import pathlib
import pickle
from typing import Final

from chunking_functions import chunk_by_fixed_size, chunk_by_paragraph

INPUT_DIRPATH: Final[str] = "./input_docs_txt"
OUTPUT_DIRPATH: Final[str] = "./chunked_input"

for path in pathlib.Path(OUTPUT_DIRPATH).iterdir():
    if path.is_file() and path.name != ".gitkeep":
        path.unlink()
        print(f"Deleted file [{path}]")

for path in pathlib.Path(INPUT_DIRPATH).iterdir():
    if path.is_file() and path.suffix == ".txt":
        with open(path, "r", encoding="utf-8") as file:
            input_text = file.read()
        for chunker in (
            {"func": chunk_by_fixed_size, "params": {"chunk_nchar": 100}},
            {
                "func": chunk_by_fixed_size,
                "params": {"chunk_nchar": 100, "overlap_nchar": 20},
            },
        ):
            chunks = chunker["func"](input_text, **chunker["params"])
            chunker_desc = (
                chunker["func"].__name__
                + "-"
                + "-".join([f"{k}{v}" for k, v in chunker["params"].items()])
            )
            output_filepath = f"{OUTPUT_DIRPATH}/{path.stem}-{chunker_desc}.pickle"
            with open(output_filepath, "wb") as file:
                pickle.dump(chunks, file, protocol=pickle.HIGHEST_PROTOCOL)
                print(f"exported file [{output_filepath}")
