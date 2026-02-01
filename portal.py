import streamlit as st
import pandas as pd

# 1. Google Sheets CSV Bağlantısı (Düzenlediğiniz linki buraya tırnak içine yapıştırın)
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTD2yZrgEbIJ3KoCmGBFVc9xo6esKZKNB42iKHmXfJ_YFzA5v251a_4m6MG0F_nHQmnOCoxPXCQ1t6L/pub?output=csv"

st.set_page_config(page_title="Nusaybin SB Anadolu Lisesi BB Portalı", layout="centered")

# 2. Şifre Sorgulama Fonksiyonu
def bilgileri_getir(no):
    try:
        df = pd.read_csv(SHEET_CSV_URL)
        # Sütun isimleri tablonuzdakilerle birebir aynı olmalı
        sonuc = df[df['Okul Numaranız'].astype(str) == str(no)]
        return sonuc
    except:
        return None

# 3. Arayüz Tasarımı
st.title("💻 Bilgisayar Bilimi Portalı")
st.write("Nusaybin Süleyman Bölünmez Anadolu Lisesi")

okul_no = st.text_input("Okul Numaranı Gir ve Enter'a Bas:", placeholder="Örn: 1234")

if okul_no:
    veri = bilgileri_getir(okul_no)
    if veri is not None and not veri.empty:
        # Tablonuzdaki sütun başlıklarına göre bilgileri çekiyoruz
        ad = veri['Adınız ve Soyadınız'].values[0]
        tc = veri['TC Kimlik No'].values[0]
        sifre = veri['Eba/Canva Şifreniz'].values[0]
        
        st.success(f"Merhaba {ad}!")
        st.info(f"🆔 **TC Kimlik No:** {tc}")
        st.info(f"🔐 **Canva/EBA Şifresi:** {sifre}")
        
        st.divider()
        st.subheader("📅 2. Hafta Görevi: Tasarım Temelleri")
        st.write("Kazanım: Hazır tasarım şablonlarını düzenleme yöntemlerini kavrar.")
        st.markdown("- Canva'ya giriş yap.\n- Bir afiş şablonu seç.\n- Görsel hiyerarşiye dikkat ederek düzenle.")
    else:
        st.error("Numara bulunamadı! Lütfen formu doldurduğundan emin ol.")