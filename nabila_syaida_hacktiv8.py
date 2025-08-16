import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage

# Ambil token dari secret
token = st.secrets["GITHUB"]["TOKEN"]
credential = AzureKeyCredential(token)

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=credential
)
