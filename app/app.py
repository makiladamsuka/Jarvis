import streamlit as st
from apiclient import api

st.title("Jarvis")
st.caption("Hello, I am Jarvis, your AI assistant. How can I help you today?")


user_input = st.chat_input("Ask me anything...", key="user_input")
if user_input:
    with st.spinner('thinking...'):
        response = api(user_input)
        st.write(response)

