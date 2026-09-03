import requests
class Embedder:
    embed_response: str
    def __init__(self, url="http://localhost:11434/api/embed", model_name="nomic-embed-text-v2-moe", input=""):
        response = requests.post(url, json={
            "model": model_name,
            "input": input
        })
        response.raise_for_status()
        self.embed_response = response.json()["embeddings"]
    def get_result(self):
        return self.embed_response
