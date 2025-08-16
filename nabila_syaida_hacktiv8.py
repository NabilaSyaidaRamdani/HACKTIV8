import streamlit as st
from openai import OpenAI

# ===========================
# Judul aplikasi
st.title("Chat dengan Model DeepSeek-R1")

# ===========================
# Ambil token GitHub dari Streamlit Secrets
# Pastikan di Streamlit Cloud sudah ditambahkan:
# TOKEN = "ghp_xxx..."
token = st.secrets["TOKEN"]

# ===========================
# Buat client GitHub Models
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=token,
)

# ===========================
# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

# ===========================
# Tombol kirim
if st.button("Kirim"):
    if user_input.strip() != "":
        # Kirim ke model DeepSeek-R1
        response = client.chat.completions.create(
            model="deepseek-r1",   # 👈 perbaikan nama model
            messages=[{"role": "user", "content": user_input}],
            max_tokens=1024
        )

        # Tampilkan jawaban
        st.markdown("**Jawaban Model:**")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Silakan tulis pertanyaan terlebih dahulu!")
