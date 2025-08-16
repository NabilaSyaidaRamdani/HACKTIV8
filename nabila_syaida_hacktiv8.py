import streamlit as st
from openai import OpenAI

st.title("Chat dengan Model OpenAI")

# Ambil API Key dari Streamlit secrets
api_key = st.secrets["TOKEN"]

# Buat client OpenAI
client = OpenAI(api_key=api_key)

# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

# Tombol kirim
if st.button("Kirim"):
    if user_input.strip() != "":
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # model OpenAI, bisa ganti misalnya gpt-4o
            messages=[
                {"role": "system", "content": "You are a helpful data science assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=512,
            temperature=0.7,
        )

        st.markdown("**Jawaban Model:**")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Silakan tulis pertanyaan terlebih dahulu!")
