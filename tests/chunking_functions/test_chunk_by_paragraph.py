import pytest
from chunking_functions import chunk_by_paragraph
from objects import Chunk


def test_chunk_by_paragraph():
    # Test case 1: Regular input with multiple paragraphs
    input_text = "\n\n    sdf\n    SDFSDKJFNSDNFDSF\n\n    fsdniunfdsiudfnsufnsdunfsudinf\n    fuids8392jbke\n\n\n23\n\n   \n\n\n\n  123\n\n    "
    assert chunk_by_paragraph(input_text, min_chunk_nchar=3) == (
        Chunk(
            text="sdf\n    SDFSDKJFNSDNFDSF",
            start_index=6,
            end_index=30,
            chunk_num=0,
            metadata=None,
        ),
        Chunk(
            text="fsdniunfdsiudfnsufnsdunfsudinf\n    fuids8392jbke",
            start_index=36,
            end_index=84,
            chunk_num=1,
            metadata=None,
        ),
        Chunk(text="123", start_index=100, end_index=103, chunk_num=2, metadata=None),
    )


if __name__ == "__main__":
    pytest.main()
