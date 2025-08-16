import streamlit as st


# ===========================
# Judul aplikasi
st.title("Chat dengan Model DeepSeek-R1")

# ===========================
# Ambil GitHub token dari Streamlit Secrets
# Pastikan di Streamlit Cloud sudah ditambahkan:
# [GITHUB]
# TOKEN = "ghp_...."
token = st.secrets["TOKEN"]

# Buat credential
import streamlit as st

# Ambil dari secrets
token = st.secrets["TOKEN"]

# Gunakan variabel 'token', bukan 'TOKEN'
credential = AzureKeyCredential(TOKEN)

# ===========================
# Buat client
client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=credential
)

# ===========================
# Input pengguna
user_input = st.text_input("Tulis pertanyaan kamu:")

# ===========================
# Tombol kirim
if st.button("Kirim"):
    if user_input.strip() != "":
        # Kirim pesan ke model
        response = client.complete(
            messages=[UserMessage(user_input)],
            model="deepseek/DeepSeek-R1",
            max_tokens=1024
        )

        # Tampilkan jawaban
        st.markdown("**Jawaban Model:**")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Silakan tulis pertanyaan terlebih dahulu!")
