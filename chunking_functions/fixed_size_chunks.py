"""
Defines function for splitting text into chunks of fixed size (with optional overlap) 
"""

from objects import Chunk


def chunk_by_fixed_size(
    input_text: str, chunk_nchar: int, overlap_nchar: int = 0
) -> tuple[Chunk, ...]:
    """Chunks (splits) `input_text` into chunks of size `chunk_nchar`, optionally with
    content overlap of `overlap_nchar` characters between the chunks

    Args:
        input_text (str): The text to split into chunks
        chunk_nchar (int): How many characters go into each chunk
        overlap_nchar (int): How many characters in common between successive chunks

    Returns:
        tuple[Chunk, ...]: a tuple of Chunk objects
    """
    chunks: list[Chunk] = []
    current_index: int = 0
    while True:
        chunk_end_index = current_index + chunk_nchar - 1
        if chunk_end_index <= len(input_text):
            chunks.append(
                Chunk(
                    text=input_text[current_index : chunk_end_index + 1],
                    start_index=current_index,
                    end_index=chunk_end_index,
                )
            )
            current_index += chunk_nchar - overlap_nchar
        else:
            chunk_end_index = len(input_text) - 1
            chunks.append(
                Chunk(
                    text=input_text[current_index : chunk_end_index + 1],
                    start_index=current_index,
                    end_index=chunk_end_index,
                )
            )
            break

    return tuple(chunks)
