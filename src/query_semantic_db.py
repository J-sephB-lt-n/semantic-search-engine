import pickle
from typing import Final

import pymilvus
from sentence_transformers import SentenceTransformer

from src.objects import Chunk, ChunkMetadata

QUERY: Final[str] = input("Please enter your query: ")

with open("./prepped_input_data.pickle", "rb") as file:
    chunks = pickle.load(file)

embed_model = SentenceTransformer(
    "Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True
)

milvus_client = pymilvus.MilvusClient("databases/embeddings.db")

closest = milvus_client.search(
    collection_name="lookup_docs",
    data=[embed_model.encode(QUERY)],
    limit=3,
    # search_params={"metric_type": "L2", "params": {}},
    # search_params={"metric_type": "COSINE", "params": {}},
)

milvus_client.close()
