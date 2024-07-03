import pytest
from objects import Chunk
from chunking_functions import chunk_by_fixed_size


def test_chunk_by_paragraph():
    # Test case 1: Regular input with multiple paragraphs
    input_text = "abcdefghijklmnop\nqrst\n\nuvwxyz"
    assert chunk_by_fixed_size(input_text, chunk_nchar=8) == (
        Chunk(text="abcdefgh", start_index=0, end_index=7),
        Chunk(text="ijklmnop", start_index=8, end_index=15),
        Chunk(text="\nqrst\n\nu", start_index=16, end_index=23),
        Chunk(text="vwxyz", start_index=24, end_index=28),
    )

    assert chunk_by_fixed_size(input_text, chunk_nchar=10, overlap_nchar=4) == (
        Chunk(text="abcdefghij", start_index=0, end_index=9),
        Chunk(text="ghijklmnop", start_index=6, end_index=15),
        Chunk(text="mnop\nqrst\n", start_index=12, end_index=21),
        Chunk(text="rst\n\nuvwxy", start_index=18, end_index=27),
        Chunk(text="vwxyz", start_index=24, end_index=28),
    )


if __name__ == "__main__":
    pytest.main()
