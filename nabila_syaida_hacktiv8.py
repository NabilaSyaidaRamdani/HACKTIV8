import streamlit as st
from openai import OpenAI

st.title("Chat dengan Model OpenAI")

# Ambil API Key dari Streamlit secrets
api_key = st.secrets["TOKEN"]

# Buat client OpenAI
client = OpenAI(api_key=api_key)

# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")
