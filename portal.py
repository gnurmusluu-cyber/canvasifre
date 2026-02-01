import streamlit as st
import pandas as pd

# 1. Google Sheets CSV Bağlantısı (Kendi linkinizi buraya tırnak içine yapıştırın)
# Önemli: Linkin sonu '/export?format=csv' ile bitmelidir.
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTD2yZrgEbIJ3KoCmGBFVc9xo6esKZKNB42iKHmXfJ_YFzA5v251a_4m6MG0F_nHQmnOCoxPXCQ1t6L/pub?output=csv"

st.set_page_config(page_title="Nusaybin SB Anadolu Lisesi BB Portalı", layout="centered")

# Sayfa Başlığı ve Okul Bilgisi
st.title("🛡️ Bilgisayar Bilimi Ders Portalı")
st.caption("Bilişim Teknolojileri Öğretmeni - Süleyman Bölünmez Anadolu Lisesi")

# 2. Akıllı Veri Çekme Fonksiyonu
def verileri_yukle():
    try:
        # Veriyi çek ve sütun başlıklarındaki gizli boşlukları temizle
        df = pd.read_csv(SHEET_CSV_URL)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"Veri tabanına bağlanılamadı. Hata: {e}")
        return None

# 3. Giriş ve Şifre Sorgulama Paneli
okul_no = st.text_input("Okul Numaranı Gir ve Enter'a Bas:", placeholder="Örn: 1234")

if okul_no:
    df = verileri_yukle()
    
    if df is not None:
        # Okul numarası sütununu metne çevir ve ara
        # Sütun isminin 'Okul Numaranız' olduğundan emin olun
        df['Okul Numaranız'] = df['Okul Numaranız'].astype(str).str.strip()
        ogrenci = df[df['Okul Numaranız'] == str(okul_no).strip()]
        
        if not ogrenci.empty:
            # Bilgileri değişkenlere ata
            ad_soyad = ogrenci['Adınız ve Soyadınız'].values[0]
            tc_no = ogrenci['TC Kimlik No'].values[0]
            eba_sifre = ogrenci['Eba/Canva Şifreniz'].values[0]
            sinif = ogrenci['Sınıfınız'].values[0]

            # Öğrenci Karşılama Ekranı
            st.success(f"Hoş geldin, {ad_soyad.upper()}!")
            
            c1, c2 = st.columns(2)
            with c1:
                st.info(f"🆔 **TC Kimlik No:**\n\n{tc_no}")
            with c2:
                st.warning(f"🔐 **EBA/Canva Şifren:**\n\n{eba_sifre}")
            
        
            
            st.link_button("Canva Uygulamasını Aç", "https://www.canva.com")
            
        else:
            st.error("Girdiğin numara sistemde bulunamadı. Lütfen formu doldurduğundan veya numaranı doğru yazdığından emin ol.")

# 4. Alt Bilgi
st.markdown("---")
st.caption("⚠️ Bu bilgiler sadece ders içi kullanım içindir. Bilgilerini kimseyle paylaşma.")