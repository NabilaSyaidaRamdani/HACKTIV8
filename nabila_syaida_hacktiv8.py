import streamlit as st

st.title('Nabila Syaida')

# Ambil token dari Streamlit Secrets
token = st.secrets["API_KEY"]
credential = AzureKeyCredential(token)

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=credential
)
