import streamlit as st
from gtts import gTTS
from streamlit_audio_recorder import audio_recorder
import os

st.title("🎤 Süper Yapay Zeka Ajanı")

st.subheader("Sesli Sohbet")
audio_bytes = audio_recorder()

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    st.write("Sesin algılandı, işleniyor...")

user_input = st.text_input("Ne araştırmamı istersin?")

if user_input:
    ai_cevabi = "Bu konuda araştırma yaptım ve şu sonuçlara ulaştım..." 
    st.write(ai_cevabi)


 # Metni sese çevir ve oynat
    def metni_seslendir(metin):
        tts = gTTS(text=metin, lang='tr')
        tts.save("cevap.mp3")
        st.audio("cevap.mp3")


    metni_seslendir(ai_cevabi)
