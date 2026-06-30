import PyPDF2
from groq import Groq


# 1. PDF OKUMA FONKSİYONU
def pdf_metnini_cikar(pdf_yolu):
    metin = ""
    with open(pdf_yolu, 'rb') as dosya:
        okuyucu = PyPDF2.PdfReader(dosya)
        for sayfa in okuyucu.pages:
            metin += sayfa.extract_text() + "\n"
    return metin


# 2. YAPAY ZEKA İLE KONUŞMA FONKSİYONU
def yapay_zekaya_soru_sor(pdf_metni, soru):
    client = Groq(api_key="")

    icerik = f"DERS NOTLARI:\n{pdf_metni}\n\nSORU: {soru}"

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system",
             "content": "Sen bir öğretmensin. Soruları SADECE sana verilen DERS NOTLARI'na dayanarak yanıtla."},
            {"role": "user", "content": icerik}
        ]
    )
    print("💬 CEVAP:", completion.choices[0].message.content)


# 3. BURADAN ÇALIŞTIRIYORUZ
if __name__ == "__main__":
    dosya_adim = "dersnotu.pdf"

    print("📄 PDF okunuyor...")
    notlar = pdf_metnini_cikar(dosya_adim)

    print("🤖 Yapay zekaya soruluyor...")
    yapay_zekaya_soru_sor(notlar, "Bu notların ana konusu nedir?")
