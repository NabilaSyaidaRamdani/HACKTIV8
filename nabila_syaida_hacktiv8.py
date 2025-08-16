import streamlit as st
from openai import OpenAI

st.title("Chat dengan Model DeepSeek-R1")

# Ambil token dari Streamlit secrets
token = st.secrets["TOKEN"]

# Buat client
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=token,
)

# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

# Tombol kirim
if st.button("Kirim"):
    if user_input.strip() != "":
       response = client.chat.completions.create(
    model="deepseek-ai/deepseek-r1",
    messages=[
        {"role": "system", "content": "You are a helpful data science assistant."},
        {"role": "user", "content": user_input}
    ],
    max_tokens=512,
    temperature=0.7,  # lebih kreatif
)

        st.markdown("**Jawaban Model:**")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Silakan tulis pertanyaan terlebih dahulu!")
