import streamlit as st

st.title('Nabila Syaida')
import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage

# Ambil token dari Streamlit Secrets
token = st.secrets["GITHUB_TOKEN"]
credential = AzureKeyCredential(token)

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=credential
)
