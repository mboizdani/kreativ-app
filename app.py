import streamlit as st
import google.generativeai as genai

# Konfigurasi Branding Kreativ.ai
st.set_page_config(page_title="Kreativ.ai - Prompt Builder", page_icon="🚀")
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi prompt infografis profesional.")

# API KEY Anda yang sudah aktif
API_KEY = "AIzaSyA9cbVtTFvvpc_AUUsGA1VNCKcoIffiUKc"

# Inisialisasi AI
genai.configure(api_key=API_KEY)

topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Tips Sukses Trading Crypto")

if st.button("Proses Sekarang ✨"):
    if topik:
        with st.spinner('Kreativ.ai sedang meriset data...'):
            # Instruksi agar hasil prompt Spektakuler
            instruksi = (
                f"Riset topik '{topik}' secara mendalam. "
                "Berikan Judul menarik, 5 poin materi utama, "
                "dan buatkan satu Master Prompt bahasa Inggris yang sangat detail untuk "
                "membuat gambar '3D Isometric Professional Infographic' dengan pencahayaan lembut."
            )
            
            # LOGIKA BACKUP: Mencoba model Flash, jika gagal coba Pro
            try:
                # Coba jalur 1: Model Flash
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(instruksi)
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.code(response.text)
                st.info("Salin teks di atas ke Gemini untuk membuat gambar!")
            except Exception:
                try:
                    # Coba jalur 2: Model Pro (Lebih stabil untuk API versi lama)
                    model_pro = genai.GenerativeModel('gemini-pro')
                    response = model_pro.generate_content(instruksi)
                    st.markdown("### 📊 Hasil Riset & Prompt")
                    st.code(response.text)
                    st.info("Salin teks di atas ke Gemini untuk membuat gambar!")
                except Exception as e:
                    st.error(f"Maaf, server sedang sibuk. Silakan coba lagi beberapa saat. Error: {e}")
    else:
        st.warning("Silakan isi topiknya dulu ya.")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
