import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

# 1. AYARLAR
# Streamlit'in secrets.toml dosyasından anahtarları çek
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
except:
    st.error("HATA: secrets.toml dosyan bulunamadı veya içindeki anahtar isimleri yanlış.")
    st.stop()

# 2. ARAÇLAR VE MODEL
search_tool = TavilySearchResults(tavily_api_key=TAVILY_API_KEY)
llm = ChatGroq(api_key=GROQ_API_KEY, model_name="llama-3.3-70b-versatile")

# 3. ARAYÜZ
st.title("🤖 Süper Yapay Zeka Ajanı")
soru = st.text_input("Ne araştırmamı istersin?")

if st.button("Araştır"):
    if soru:
        with st.spinner("Ajanım internette araştırıyor..."):
            try:
                # İnternette ara
                arama_sonucu = search_tool.run(soru)

                # Arama sonucunu modele gönder ve özetlet
                mesaj = f"Kullanıcı sorusu: {soru} \n\n İnternetten bulunan bilgiler: {arama_sonucu}"
                yanit = llm.invoke(mesaj)

                st.write(yanit.content)
            except Exception as e:
                st.error(f"Ajan çalışırken bir hata oluştu: {e}")
    else:
        st.warning("Lütfen bir soru gir.")