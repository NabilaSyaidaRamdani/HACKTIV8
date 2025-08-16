import streamlit as st
from huggingface_hub import InferenceClient

st.title("Chat dengan Model Hugging Face")

# Ambil token dari secrets
hf_token = st.secrets["TOKEN"]

# Pilih model Hugging Face (gratis & open)
# Kamu bisa ganti model_id sesuai kebutuhan, misalnya "google/flan-t5-base"
client = InferenceClient(model="gpt2", token=hf_token)

# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

if user_input:
    response = client.text_generation(user_input, max_new_tokens=200)
    st.markdown("**Jawaban Model:**")
    st.write(response)
