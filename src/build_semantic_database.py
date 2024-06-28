import pathlib
import pickle

import pymilvus
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from src.objects import Chunk, ChunkMetadata

with open("./prepped_input_data.pickle", "rb") as file:
    chunks = pickle.load(file)

embed_model = SentenceTransformer(
    "Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True
)

pathlib.Path("databases/embeddings.db").unlink(missing_ok=True)
milvus_client = pymilvus.MilvusClient("databases/embeddings.db")

milvus_client.create_collection(
    collection_name="lookup_docs",
    dimension=1024,
    schema=pymilvus.CollectionSchema(
        fields=[
            pymilvus.FieldSchema(
                name="id",
                dtype=pymilvus.DataType.INT64,
                is_primary=True,
            ),
            pymilvus.FieldSchema(
                name="embedding", dtype=pymilvus.DataType.FLOAT_VECTOR, dim=1024
            ),
            pymilvus.FieldSchema(
                name="source_name", dtype=pymilvus.DataType.VARCHAR, max_length=999
            ),
        ]
    ),
)

for idx, chunk in tqdm(enumerate(chunks)):
    milvus_client.insert(
        collection_name="lookup_docs",
        data=[
            {
                "id": idx,
                "embedding": embed_model.encode(chunk.text),
                "source_name": chunk.metadata.source_name,
            }
        ],
    )

milvus_client.close()
