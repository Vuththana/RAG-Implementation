import chromadb


class ChromaStore:
    def __init__(
        self,
        db_path="./chroma_db",
        collection_name="documents"
    ):
        self.client = chromadb.PersistentClient(
            path=db_path
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add(
        self,
        ids,
        documents,
        embeddings,
        metadatas=None
    ):
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )
    def search(
        self,
        query_embedding,
        n_results=5
    ):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
    def clear(self):
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.create_collection(
            name=self.collection.name
        )