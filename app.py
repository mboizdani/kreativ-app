import streamlit as st
import google.generativeai as genai

# Branding
st.set_page_config(page_title="Kreativ.ai - Prompt Builder", page_icon="🚀")
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi prompt infografis profesional.")

# API KEY
API_KEY = "AIzaSyA9cbVtTFvvpc_AUUsGA1VNCKcoIffiUKc"

# Inisialisasi Langsung
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Tips Trading Crypto")

if st.button("Proses Sekarang ✨"):
    if topik:
        with st.spinner('Kreativ.ai sedang bekerja...'):
            try:
                instruksi = f"Riset topik '{topik}' secara mendalam. Berikan Judul, 5 poin materi, dan Master Prompt bahasa Inggris untuk gambar Infografis 3D profesional."
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.code(response.text)
                st.info("Salin teks di atas ke Gemini untuk membuat gambar!")
            except Exception as e:
                st.error(f"Ada kendala: {e}")
    else:
        st.warning("Silakan isi topiknya dulu ya.")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
