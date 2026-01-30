import streamlit as st
import google.generativeai as genai

# --- CONFIG ---
st.set_page_config(page_title="Prompt Generator Infografis Pro", page_icon="🚀")

# --- CORE ENGINE: MENCARI JALUR API YANG TERSEDIA ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # 1. Ambil semua daftar model yang mendukung generate content di akun Anda
    all_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    # 2. Cari yang paling stabil (1.5 Flash), jika tidak ada ambil apa saja yang ada
    # Ini mencegah error 404 karena sistem akan memilih model yang PASTI ADA
    active_model = next((m for m in all_models if "1.5-flash" in m), all_models[0] if all_models else None)
    
    st.title("PROMPT GENERATOR INFOGRAFIS PRO")
    topik = st.text_input("Topik:")

    if st.button("Generate"):
        if topik and active_model:
            model = genai.GenerativeModel(active_model)
            # Instruksi disingkat agar hemat kuota (Anti-429)
            res = model.generate_content(f"Buat Master Prompt JSON Infografis 3D 8K tentang: {topik}. Rasio 2:3. Watermark: By Kreativ.ai")
            st.code(res.text)
        else:
            st.error("Gagal koneksi ke AI. Coba ganti API Key Anda.")
except Exception as e:
    st.error(f"Sistem Google sedang maintenance: {e}")
