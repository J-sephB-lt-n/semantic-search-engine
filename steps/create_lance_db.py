"""Creates Lance database for storing and querying the chunk embedding vectors
"""

import pathlib
import shutil

import lancedb
from lancedb.pydantic import LanceModel, Vector


class ChunkVector(LanceModel):
    chunk_num: int
    source_doc: str
    chunk_alg: str
    chunk_alg_params: str
    char_start_index: int
    char_end_index: int
    vector: Vector(1024)
    text: str


if pathlib.Path("./.lancedb").exists():
    shutil.rmtree("./.lancedb")
    print("removed existing ./.lancedb")

db = lancedb.connect("./.lancedb")
print("Created database ./.lancedb")
for path in pathlib.Path("./chunked_input").iterdir():
    if path.is_file() and path.suffix == ".pickle":
        db.create_table(
            path.stem,
            schema=ChunkVector,
        )

print("Created tables in ./.lancedb :")
for table_name in db.table_names():
    print("\t* ", table_name)
