import re

from objects import Chunk


def chunk_by_paragraph(
    input_text: str,
    min_chunk_nchar: int = 10,
    paragraph_delimit_regex: str = r"\n\n",
) -> tuple[Chunk, ...]:
    """Splits up input text by paragraph (only including paragraphs at
    least `min_chunk_nchar` characters long

    Args:
       input_text (str): The text to split into chunks
       min_chunk_nchar (int): Chunks with fewer characters will be discarded
       paragraph_delimit_regex (str): Regex pattern used to identify paragraph breaks

    Returns:
        tuple[Chunk, ...]: A tuple of Chunk objects
    """
    chunks: list[Chunk] = []
    paragraph_breaks_found: list[tuple[int, int]] = (
        # including document start and end at paragraph breaks #
        [(0, 0)]
        + [
            x.span()
            for x in re.finditer(pattern=paragraph_delimit_regex, string=input_text)
        ]
        + [(len(input_text) - 1, len(input_text) - 1)]
    )
    parag_start_index_list = [x[1] for x in paragraph_breaks_found[:-1]]
    parag_end_index_list = [x[0] for x in paragraph_breaks_found[1:]]
    for parag_start, parag_end in zip(parag_start_index_list, parag_end_index_list):
        paragraph = input_text[parag_start:parag_end]
        left_stripped = paragraph.lstrip()
        if len(left_stripped) < len(paragraph):
            parag_start += len(paragraph) - len(left_stripped)
        right_stripped = paragraph.rstrip()
        if len(right_stripped) < len(paragraph):
            parag_end -= len(paragraph) - len(right_stripped)
        if parag_end - parag_start >= min_chunk_nchar:
            chunks.append(
                Chunk(
                    text=input_text[parag_start:parag_end],
                    start_index=parag_start,
                    end_index=parag_end,
                )
            )

    return tuple(chunks)
