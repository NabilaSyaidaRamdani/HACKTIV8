import streamlit as st
from huggingface_hub import InferenceClient

st.title("Chat dengan Model Hugging Face")

# Ambil token dari secrets
api_key = st.secrets["TOKEN"]

# Buat client TANPA model dulu
client = InferenceClient(token=api_key)

# Input
user_input = st.text_input("Tulis pertanyaan kamu:")

if st.button("Kirim"):
    if user_input.strip() != "":
        # Langsung tentukan model di sini
        response = client.text_generation(
            model="mistralai/Mistral-7B-Instruct-v0.2",  # model instruksi gratis
            prompt=user_input,
            max_new_tokens=200,
            temperature=0.7,
        )
        st.markdown("**Jawaban Model:**")
        st.write(response)
    else:
        st.warning("Silakan tulis pertanyaan terlebih dahulu!")
