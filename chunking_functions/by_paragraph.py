def chunk_by_paragraph(input_text: str, min_nchar: int = 10) -> list[str]:
    """Splits up input text by paragraph (only including paragraphs at
    least `min_nchar` characters long"""
    return [
        paragraph.strip()
        for paragraph in input_text.split("\n\n")
        if len(paragraph) >= min_nchar
    ]
