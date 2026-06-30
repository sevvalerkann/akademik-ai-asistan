import streamlit as st
from gtts import gTTS
from streamlit_audio_recorder import audio_recorder
import os

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
        tts = gTTS(text=ai_cevabi, lang='tr')
        tts.save("cevap.mp3")
        st.audio("cevap.mp3")

    st.session_state.messages.append({"role": "assistant", "content": ai_cevabi})
