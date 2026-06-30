import streamlit as st
from gtts import gTTS
#from streamlit_audiorecorder import st_audiorecorder
import os
import streamlit as st
from gtts import gTTS
import os

# --- AetherAI Derin Uzay Teması ---
st.set_page_config(page_title="AetherAI", page_icon="🌌")

st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #e0e0e0;
    }
    /* Başlık Rengi */
    h1, h2, h3 {
        color: #c4a1ff !important;
        text-shadow: 2px 2px 8px #000;
    }
    /* Sohbet Kutuları (Glassmorphism) */
    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(196, 161, 255, 0.3);
        border-radius: 15px;
    }
    /* Chat Giriş Kutusu */
    [data-testid="stChatInput"] {
        background-color: rgba(0, 0, 0, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- AetherAI Başlık ---
st.title("🌌 AetherAI")
st.subheader("Kozmik Akademik Asistanın")

# --- AetherAI Arayüz Ayarları ---
st.set_page_config(page_title="AetherAI", page_icon="✨")
st.title("✨ AetherAI")
st.subheader("Akademik Destek Asistanın")

# Sohbet geçmişini tutmak için session_state kullanımı
if "messages" not in st.session_state:
    st.session_state.messages = []

# Geçmiş mesajları ekranda tut
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Kullanıcı Girişi (Chat Arayüzü) ---
if prompt := st.chat_input("Bir şeyler sor..."):
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- AetherAI Cevabı ---
    with st.chat_message("assistant"):
        # Buraya Groq API yanıtın gelecek
        ai_cevabi = f"AetherAI olarak '{prompt}' konusunda araştırma yapıyorum..."
        st.markdown(ai_cevabi)

        # Sese çevir ve oynat
        #tts = gTTS(text=ai_cevabi, lang='tr')
        #tts.save("cevap.mp3")
        #st.audio("cevap.mp3")

    st.session_state.messages.append({"role": "assistant", "content": ai_cevabi})
