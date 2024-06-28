import pickle

from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from src.objects import Chunk, ChunkMetadata

with open("./prepped_input_data.pickle", "rb") as file:
    chunks = pickle.load(file)

embed_model = SentenceTransformer(
    "Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True
)

embed_model.encode(chunks[69].text)
