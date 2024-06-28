from collections import namedtuple

Chunk = namedtuple("Chunk", "text metadata")
ChunkMetadata = namedtuple("ChunkMetadata", "source_name")
