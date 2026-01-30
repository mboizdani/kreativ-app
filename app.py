import streamlit as st
import google.generativeai as genai

# Konfigurasi Tampilan Kreativ.ai
st.set_page_config(page_title="Kreativ.ai - Prompt Builder", page_icon="🚀")
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi prompt infografis profesional.")

# API KEY Anda (Sudah benar)
API_KEY = "AIzaSyA9cbVtTFvvpc_AUUsGA1VNCKcoIffiUKc"

# Inisialisasi AI dengan model terbaru yang paling stabil
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Tips Sukses Trading Crypto")

if st.button("Proses Sekarang ✨"):
    if topik:
        with st.spinner('Kreativ.ai sedang meriset data...'):
            try:
                # Instruksi Strategis
                instruksi = (
                    f"Tolong buatkan riset mendalam untuk topik: {topik}. "
                    "Berikan Judul, 5 poin materi utama, dan buatkan prompt gambar "
                    "bahasa Inggris yang sangat detail untuk infografis 3D profesional."
                )
                
                # Memproses permintaan
                response = model.generate_content(instruksi)
                
                if response.text:
                    st.markdown("### 📊 Hasil Riset & Prompt")
                    st.code(response.text)
                    st.info("Salin teks di atas ke Gemini untuk membuat gambar!")
                else:
                    st.error("AI tidak memberikan respon. Coba ganti topik.")
                    
            except Exception as e:
                st.error(f"Terjadi kendala teknis: {e}")
                st.info("Saran: Coba klik 'Reboot App' di menu kanan bawah Streamlit.")
    else:
        st.warning("Silakan isi topiknya dulu ya.")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
