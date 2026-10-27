import streamlit as st
import praxa_rag
import random
import time

st.title("Praxa Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from the RAG system
    response = praxa_rag.get_response(prompt)

    # Display assistant message in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})