import streamlit as st
import google.generativeai as genai

# Tampilan Branding
st.set_page_config(page_title="Kreativ.ai - Prompt Builder", page_icon="🚀")
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi prompt infografis profesional.")

# --- BAGIAN PENTING: TEMPEL API KEY ANDA DI SINI ---
# Ganti teks di dalam tanda kutip dengan kode yang Anda copy dari Google AI Studio tadi
API_KEY = "TEMPEL_KODE_AIza_ANDA_DI_SINI"

if API_KEY != "TEMPEL_KODE_AIza_ANDA_DI_SINI":
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Manfaat Hidup Sehat")
    
    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang bekerja...'):
                instruksi = f"Buatkan riset lengkap untuk '{topik}' dan buatkan prompt gambar bahasa Inggris yang detail untuk infografis 3D profesional dengan watermark 'Kreativ.ai'."
                response = model.generate_content(instruksi)
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.code(response.text)
                st.info("Salin teks di atas ke Gemini untuk jadi gambar!")
        else:
            st.warning("Isi topiknya dulu ya.")
