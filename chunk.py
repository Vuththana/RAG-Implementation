def recursive_chunk(
    text,
    chunk_size=1000,
    chunk_overlap=200,
    separators=None
):
    if separators is None:
        separators = ["\n\n", "\n", ". ", " ", ""]

    if len(text) <= chunk_size:
        return [text.strip()]

    separator = separators[0]

    if separator == "":
        chunks = [
            text[i:i + chunk_size]
            for i in range(0, len(text), chunk_size - chunk_overlap)
        ]

        return [chunk.strip() for chunk in chunks if chunk.strip()]

    parts = text.split(separator)

    chunks = []
    current = ""

    for part in parts:
        candidate = current + separator + part if current else part

        if len(candidate) <= chunk_size:
            current = candidate
        else:
            if current:
                chunks.append(current.strip())

            if len(part) > chunk_size:
                chunks.extend(
                    recursive_chunk(
                        part,
                        chunk_size,
                        chunk_overlap,
                        separators[1:]
                    )
                )
                current = ""
            else:
                current = part

    if current:
        chunks.append(current.strip())

    return chunks