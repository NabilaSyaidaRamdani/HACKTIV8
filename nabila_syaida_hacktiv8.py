import streamlit as st
from openai import OpenAI

st.title("Chat dengan Model DeepSeek-R1")

# Ambil token GitHub dari secrets
token = st.secrets["TOKEN"]

# Buat client
client = OpenAI(
    base_url="https://models.github.ai/v1",
    api_key=token,
)

# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

# Tombol kirim
if st.button("Kirim"):
    if user_input.strip() != "":
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=1024
        )

        st.markdown("**Jawaban Model:**")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Silakan tulis pertanyaan terlebih dahulu!")
