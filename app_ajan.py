import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

# 1. Sayfa Yapılandırması (Sadece bir kez en üstte olmalı)
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
search = TavilySearchResults(tavily_api_key=st.secrets["TAVILY_API_KEY"])

# 4. Sohbet Geçmişi
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Sohbet Mantığı (Tek bir giriş kutusu)
# Sohbet Mantığı
if prompt := st.chat_input("Akademik bir soru sor..."):
    # Mesajı geçmişe ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Arama ve Cevaplama bloğunu tamamen buraya, bloğun içine alıyoruz
    with st.chat_message("assistant"):
        with st.spinner("Kozmik veriler taranıyor..."):
            # Arama yap
            arama_sonucu = search.run(prompt)

            # Veriyi kırp (hata almamak için)
            ozet_sonuc = arama_sonucu[:2000] if arama_sonucu else "Veri bulunamadı."

            # Groq'a gönder
            cevap = llm.invoke(
                f"Soru: {prompt}. Aşağıdaki özet bilgiyi kullanarak akademik bir açıklama yap: {ozet_sonuc}")

            st.markdown(cevap.content)
            st.session_state.messages.append({"role": "assistant", "content": cevap.content})