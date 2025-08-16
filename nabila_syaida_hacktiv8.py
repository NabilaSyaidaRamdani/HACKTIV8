import streamlit as st
from huggingface_hub import InferenceClient

st.title("Chat dengan Model Hugging Face")

# Ambil token
hf_token = st.secrets["TOKEN"]

# Gunakan model yang support text-generation
client = InferenceClient(model="gpt2", token=hf_token)

# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

if user_input:
    response = client.text_generation(user_input, max_new_tokens=100)
    st.markdown("**Jawaban Model:**")
    st.write(response)
