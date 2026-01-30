import streamlit as st
import google.generativeai as genai

# Konfigurasi Branding Kreativ.ai
st.set_page_config(page_title="Kreativ.ai - Prompt Builder", page_icon="🚀")
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi prompt infografis profesional.")

# API KEY Anda
API_KEY = "AIzaSyA9cbVtTFvvpc_AUUsGA1VNCKcoIffiUKc"

# Inisialisasi AI (Menggunakan versi yang paling stabil)
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Tips Sukses Jualan Online")

if st.button("Proses Sekarang ✨"):
    if topik:
        with st.spinner('Kreativ.ai sedang meriset data...'):
            try:
                # Instruksi agar hasil prompt Spektakuler
                instruksi = (
                    f"Riset topik '{topik}' secara mendalam. "
                    "Berikan Judul menarik, 5 poin materi utama, "
                    "dan buatkan satu Master Prompt bahasa Inggris yang sangat detail untuk "
                    "membuat gambar '3D Isometric Professional Infographic' dengan pencahayaan lembut."
                )
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.code(response.text)
                st.info("Salin teks di atas ke Gemini untuk membuat gambar!")
                
            except Exception as e:
                # Jika masih ada error, gunakan model alternatif secara otomatis
                try:
                    alt_model = genai.GenerativeModel('gemini-pro')
                    response = alt_model.generate_content(instruksi)
                    st.code(response.text)
                except:
                    st.error(f"Maaf, ada kendala teknis pada server: {e}")
    else:
        st.warning("Silakan isi topiknya dulu ya.")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
