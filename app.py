import streamlit as st
import google.generativeai as genai

# Konfigurasi Tampilan
st.set_page_config(page_title="Kreativ.ai - Prompt Builder", page_icon="🚀")
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi prompt infografis profesional.")

# API KEY Anda
API_KEY = "AIzaSyA9cbVtTFvvpc_AUUsGA1VNCKcoIffiUKc"

try:
    genai.configure(api_key=API_KEY)
    
    # MENCARI MODEL OTOMATIS (Solusi Anti-Error 404)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # Pilih model pertama yang tersedia (biasanya gemini-pro atau gemini-1.5-flash)
    model_name = available_models[0] if available_models else 'gemini-pro'
    model = genai.GenerativeModel(model_name)

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Manfaat Hidup Sehat")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner(f'Kreativ.ai menggunakan {model_name}...'):
                instruksi = f"Riset topik '{topik}' secara mendalam. Berikan Judul, 5 poin materi, dan Master Prompt bahasa Inggris untuk gambar Infografis 3D profesional."
                response = model.generate_content(instruksi)
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.code(response.text)
                st.info("Salin teks di atas ke Gemini untuk jadi gambar!")
        else:
            st.warning("Isi topiknya dulu ya.")

except Exception as e:
    st.error(f"Koneksi API bermasalah. Pastikan API Key benar. Error: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
