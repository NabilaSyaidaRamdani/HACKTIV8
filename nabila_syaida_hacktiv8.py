# ===========================
# Set GitHub token
# ===========================
os.environ["GITHUB_TOKEN"] = "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"
credential = AzureKeyCredential(os.environ["GITHUB_TOKEN"])

# ===========================
# Buat client
# ===========================
client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=credential,
)

# ===========================
# Fungsi chat single-turn
# ===========================
def chat(user_input, temperature=0.7):
    response = client.complete(
        messages=[UserMessage(user_input)],
        model="deepseek/DeepSeek-R1",
        max_tokens=500,
        temperature=temperature
    )
    output = response.choices[0].message.content.strip()

    # Simpan log chat
    with open("chat_log.txt", "a") as f:
        f.write(f"User: {user_input}\nBot: {output}\n\n")

    return output

# ===========================
# Streamlit UI
# ===========================
st.title("GENAI Chat Deployment Demo")

# Slider untuk creativity
temp = st.slider("Set creativity (temperature)", 0.0, 1.0, 0.7, 0.05)

# Input user
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    output = chat(user_input, temperature=temp)
    st.text_area("Bot:", value=output, height=200)







