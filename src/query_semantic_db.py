import pickle
from typing import Final

import lancedb
from sentence_transformers import SentenceTransformer

from src.objects import Chunk, ChunkMetadata


with open("./prepped_input_data.pickle", "rb") as file:
    chunks = pickle.load(file)

embed_model = SentenceTransformer(
    "Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True
)


db = lancedb.connect("databases/semantic")
tbl = db.open_table("docs_lookup")


query = input("Please enter your query: ")
embed_query = embed_model.encode(query)
closest = tbl.search(embed_query).limit(3).to_list()
