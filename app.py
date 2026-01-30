import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Kreativ.ai - Prompt Builder", page_icon="🚀")
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi prompt infografis profesional.")

# API KEY (Sudah benar punya Anda)
API_KEY = "AIzaSyA9cbVtTFvvpc_AUUsGA1VNCKcoIffiUKc"

try:
    # Inisialisasi AI
    genai.configure(api_key=API_KEY)
    
    # Menggunakan model flash yang paling ringan dan stabil
    model = genai.GenerativeModel('models/gemini-1.5-flash')

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Manfaat Hidup Sehat")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang bekerja...'):
                # Instruksi lebih detail agar hasil "Spektakuler"
                instruksi = (
                    f"Riset topik '{topik}' dan buatkan: "
                    "1. Judul menarik, 2. Lima poin materi inti, "
                    "3. Satu Master Prompt bahasa Inggris untuk AI Image Generator dengan gaya "
                    "Professional 3D Infographic, clean layout, high resolution, soft lighting."
                )
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.code(response.text)
                st.info("Salin teks di atas ke Gemini untuk membuat gambar!")
        else:
            st.warning("Silakan isi topiknya dulu ya.")

except Exception as e:
    st.error(f"Terjadi kendala teknis: {e}")
    st.info("Coba refresh halaman atau cek API Key Anda.")

# Footer Branding
st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
