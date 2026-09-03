from pypdf import PdfReader

from chunk import recursive_chunk
from embedder import Embedder
from vector import ChromaStore
from pathlib import Path

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
store = ChromaStore()
store.clear()
pdf_files = Path("data").glob("*.pdf")
documents = []
ids = []
for pdf_path in pdf_files:
    pdf = PdfReader(pdf_path)
    for page_number, page in enumerate(pdf.pages):
        text = page.extract_text()
        if not text:
            continue
        chunks = recursive_chunk(
            text,
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        documents.append(text)
        ids.append(f"{pdf_path.stem}_page_{page_number + 1}")

embedder = Embedder(input=documents)
embeddings = embedder.get_result()
store.add(ids=ids,documents=documents,embeddings=embeddings)