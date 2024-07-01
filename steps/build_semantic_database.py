import pickle
import shutil

import lancedb
import pyarrow as pa
from lancedb.pydantic import Vector, LanceModel
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from src.objects import Chunk, ChunkMetadata

with open("./prepped_input_data.pickle", "rb") as file:
    chunks = pickle.load(file)

embed_model = SentenceTransformer(
    "Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True
)

shutil.rmtree("databases/semantic", ignore_errors=True)
db = lancedb.connect("databases/semantic")


class TableSchema(LanceModel):
    id: int
    vector: Vector(1024)
    source_name: str
    text: str


tbl = db.create_table("docs_lookup", schema=TableSchema, mode="overwrite")
for idx, chunk in enumerate(tqdm(chunks)):
    tbl.add(
        [
            {
                "id": idx,
                "vector": embed_model.encode(chunk.text),
                "source_name": chunk.metadata.source_name,
                "text": chunk.text,
            }
        ]
    )
