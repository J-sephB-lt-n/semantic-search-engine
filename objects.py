from collections import namedtuple

Chunk = namedtuple("Chunk", "text start_index end_index chunk_num metadata")

ChunkMetadata = namedtuple(
    "ChunkMetadata", "source_doc chunk_algorithm chunk_algorithm_params"
)
