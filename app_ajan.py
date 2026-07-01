import streamlit as st
from groq import Groq

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="AetherAI", page_icon="🌌")

st.title("🌌 AetherAI")
st.subheader("Akademik Destek Asistanın")

# 2. Doğrudan Groq İstemcisi (LangChain olmadan)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Akademik bir soru sor..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Kozmik veriler işleniyor..."):
            # Doğrudan Groq API çağrısı
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Soru: {prompt}. Akademik ve açıklayıcı cevap ver."}],
                model="llama3-8b-8192", # Daha hafif bir model
            )
            cevap = chat_completion.choices[0].message.content
            st.markdown(cevap)
            st.session_state.messages.append({"role": "assistant", "content": cevap})