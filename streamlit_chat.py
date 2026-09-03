import streamlit as st

def chatbot():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
                st.write(message["content"])

    query = st.chat_input("Enter your message here")

    if query:
        st.session_state.messages.append({
            "role" :"user",
            "content": query
        })
        return query

    return None