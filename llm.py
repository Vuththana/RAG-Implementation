import requests
class Llm:
    llm_response: str
    def __init__(self, url="http://localhost:8000/v1/chat/completions", model_name="Qwen/Qwen2.5-0.5B-Instruct", system_content="", user_content=""):
        response = requests.post(url, json={
            "model": model_name,
            "messages": [{"role": "system", "content": system_content}, {"role":"user", "content": user_content}],
            "stream": False,
            "temperature": 0.3,
        })
        self.llm_response = response.json()["choices"][0]["message"]["content"]
    def get_result(self):
        return self.llm_response
