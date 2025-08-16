import streamlit as st

# Ambil token dari secret
token = st.secrets["GITHUB"]["TOKEN"]
credential = AzureKeyCredential(token)

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=credential
)
