import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage, SystemMessage

st.set_page_config(page_title="GENAI Chat", page_icon="🤖")

st.title("GENAI Chat Bot")
st.write("Chat dengan model DeepSeek-R1 dari GitHub via Azure API")

# Ambil token dari Streamlit Secrets
try:
    token = st.secrets["GITHUB"]["TOKEN"]
except KeyError:
    st.error("Secret GITHUB/TOKEN belum ditambahkan di Streamlit Cloud!")
    st.stop()

# Credential & Client
credential = AzureKeyCredential(token)
client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=credential,
)

# Sidebar untuk parameter
max_tokens = st.sidebar.slider("Max Tokens", min_value=256, max_value=2048, value=512, step=128)

# Load chat log (jika ada)
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# Input user
user_input = st.text_input("Kamu:", "")

if user_input:
    st.session_state.chat_log.append(f"User: {user_input}")
    
    # Kirim ke model
    try:
        response = client.complete(
            messages=[UserMessage(user_input)],
            model="deepseek/DeepSeek-R1",
            max_tokens=max_tokens,
        )
        bot_response = response.choices[0].message.content
    except Exception as e:
        bot_response = f"Error saat request ke API: {e}"
    
    st.session_state.chat_log.append(f"Bot: {bot_response}")

# Tampilkan chat log
for msg in st.session_state.chat_log:
    st.write(msg)

# Optional: save chat log ke file
with open("chat_log.txt", "w", encoding="utf-8") as f:
    for msg in st.session_state.chat_log:
        f.write(msg + "\n")
