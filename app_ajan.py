import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="AetherAI", page_icon="🌌", layout="centered")

# 2. CSS Teması
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); color: #e0e0e0; }
    h1, h2, h3 { color: #c4a1ff !important; text-shadow: 2px 2px 8px #000; }
    [data-testid="stChatMessage"] { background-color: rgba(255, 255, 255, 0.05); border: 1px solid rgba(196, 161, 255, 0.3); border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌌 AetherAI")
st.subheader("Kozmik Akademik Asistanın")

# 3. Beyin (API) Tanımları
llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.1-70b-versatile")
# search = TavilySearchResults(tavily_api_key=st.secrets["TAVILY_API_KEY"]) # Şimdilik sadece Groq'u kullanıyoruz

# 4. Sohbet Geçmişini Başlat
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Geçmiş mesajları ekranda tut
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Sohbet Mantığı (Giriş kutusu)
if prompt := st.chat_input("Akademik bir soru sor..."):
    # Kullanıcı mesajını ekle ve göster
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Asistan cevabı (Sadece Groq ile)
    with st.chat_message("assistant"):
        with st.spinner("Kozmik veriler işleniyor..."):
            cevap = llm.invoke(f"Soru: {prompt}. Lütfen bu soruya akademik, detaylı ve açıklayıcı bir cevap ver.")
            st.markdown(cevap.content)
            st.session_state.messages.append({"role": "assistant", "content": cevap.content})