import streamlit as st
from openai import OpenAI

# Judul aplikasi
st.title("💬 Chat dengan Model OpenAI")

# Ambil API Key dari Streamlit secrets
api_key = st.secrets["TOKEN"]

# Buat client OpenAI
client = OpenAI(api_key=api_key)

# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

# Jika ada input
if st.button("Kirim"):
    if user_input.strip():
        try:
            # Panggil API OpenAI
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # bisa diganti gpt-4o, gpt-4.1, dsb
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=512,
                temperature=0.7,
            )

            # Tampilkan jawaban
            st.subheader("Jawaban Model:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Terjadi error: {e}")
    else:
        st.warning("Silakan tulis pertanyaan terlebih dahulu!")
