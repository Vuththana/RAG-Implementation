def fixed_chunk(text: str, size: int=50, overlap:int=5) -> list[str] :
    chunks, start, step = [], 0, size - overlap

    while start < len(text):
        chunks.append(text[start:start + size])
        start += step
    return chunks