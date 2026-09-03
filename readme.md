## RAG Application (Learning Purpose)

### Description
This is not fully set up with state and content, the LLM doesn't have any memory on previous conversation. I have only configured it to access external sources of my CV pdf files and using the recursive chunking strategy to chunk the extracted text to embedded and storing it to **ChromaDB**.

**Running Model with Docker**

```bash
docker run \                                                                 
  --gpus all \
  -d \
  --name ai \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  -p 8000:8000 \
  --ipc=host \
  vllm/vllm-openai:latest \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --gpu-memory-utilization 0.6
```

**Setting up a virtual environment**
```bash
python3 venv venv
```

**Activating the virtual enviroment**
```bash
source venv/bin/activate
```

**Installing required packages**
```bash
uv pip install torch>=2.13.0" transformers streamlit chromadb requests pypdf
```
**Running streamlit**
```bash
streamlit main.py
```

You can now access via [http://localhost:8501](http://localhost:8501/)