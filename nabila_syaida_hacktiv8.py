import streamlit as st
from huggingface_hub import InferenceClient

st.title("Chat dengan Model Hugging Face")

# Ambil token dari Streamlit secrets
api_key = st.secrets["TOKEN"]

# Buat client Hugging Face
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.3",  # contoh model gratis
    token=api_key
)

# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

# Tombol kirim
if st.button("Kirim"):
    if user_input.strip() != "":
        response = client.text_generation(
            user_input,
            max_new_tokens=200,
            temperature=0.7
        )
        st.markdown("**Jawaban Model:**")
        st.write(response)
    else:
        st.warning("Silakan tulis pertanyaan terlebih dahulu!")
