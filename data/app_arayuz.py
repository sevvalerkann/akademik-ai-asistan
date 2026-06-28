import streamlit as st
import PyPDF2
from groq import Groq


# 1. PDF OKUMA
def pdf_metnini_cikar(pdf_dosyasi):
    okuyucu = PyPDF2.PdfReader(pdf_dosyasi)
    metin = ""
    for i, sayfa in enumerate(okuyucu.pages):
        # Sayfa numaralarını da ekliyoruz ki hoca "nereden buldun?" dediğinde gösterelim
        metin += f"\n--- SAYFA {i + 1} ---\n" + sayfa.extract_text()
    return metin


# 2. AYARLAR VE ARAYÜZ
st.set_page_config(page_title="Akademik Asistan", layout="wide")
st.title("🎓 Akademik Eğitim Asistanı")

# Sidebar (Kenar Çubuğu) Geliştirmesi
with st.sidebar:
    st.header("Dosya ve Ayarlar")
    uploaded_file = st.file_uploader("Ders notlarını yükle (PDF)", type=["pdf"])
    api_key = st.text_input("Groq API Anahtarın:", type="password")
    if st.button("Sohbeti Temizle"):
        st.session_state.messages = []

# Hafıza Başlatma
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. MANTIK VE İŞLEYİŞ
if uploaded_file and api_key:
    notlar = pdf_metnini_cikar(uploaded_file)

    # Sohbeti Ekrana Bas
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ders notu hakkında ne öğrenmek istersin?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Çağrısı
        client = Groq(api_key=api_key)

        # Profesyonel Prompt: Kaynak belirtmesini zorunlu kılıyoruz
        sistem_mesaji = """Sen akademik bir asistansın. 
        1. Sadece sana verilen ders notlarını kullan. 
        2. Yanıt verirken bilgiyi hangi sayfadan aldığını mutlaka belirt (Örn: 'Sayfa 3'e göre...'). 
        3. Bilgi notlarda yoksa 'Notlarda bu bilgiye rastlayamadım' de."""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sistem_mesaji}] +
                     [{"role": "user", "content": f"NOTLAR:\n{notlar}\n\nSORU: {prompt}"}]
        )

        cevap = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": cevap})
        with st.chat_message("assistant"):
            st.markdown(cevap)
elif not api_key:
    st.warning("Lütfen sol tarafa Groq API anahtarını gir.")
else:
    st.info("Lütfen bir PDF dosyası yükle ve analize başla!")