from llm import Llm
from embedder import Embedder
from streamlit_chat import chatbot
from vector import ChromaStore
import streamlit as st

def get_ai_response(query):
    embedder = Embedder(input=query)
    response_embed = embedder.get_result()
    query_embedding = response_embed[0]
    store = ChromaStore()
    results = store.search(query_embedding=query_embedding, n_results=3)
    documents = results["documents"][0]
    context = "\n\n".join(documents)

    prompt = f"""
    Context:
    {context}
    
    Question:
    {query}
    
    Answer the question using the Context.  
    If it is not in the Context, say "I don't know".
    
    Answer:
    """

    llm = Llm(system_content=prompt, user_content=query)

    return llm.get_result()

query = chatbot()
if query:
    response = get_ai_response(query)
    st.session_state.messages.append({
        "role":"assistant",
        "content": response
    })
    st.rerun()