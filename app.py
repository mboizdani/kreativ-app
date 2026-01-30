import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI BRANDING ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #ff3333; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA PASSWORD & CONTOH FREE TRIAL ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# Contoh JSON Statis (Full Width Experience)
TRIAL_ANATOMI = {
    "headline_text": "ANATOMI TUBUH MANUSIA: SISTEM INTERNAL",
    "main_topic": "Detailed 3D human anatomy overview",
    "visual_type": "educational biological infographic poster",
    "design_style": "editorial modular design",
    "main_visual_description": "A stunning central 3D isometric scene of a human torso in a glass box. High-quality textures showing skeletal and muscular systems.",
    "branding": "By Kreativ.ai",
    "render_quality": "8K resolution, photorealistic",
    "note": "Akses fitur kustom & brand sendiri dengan Paket Pro!"
}

TRIAL_LAUT = {
    "headline_text": "EKOSISTEM LAUT: TERUMBU KARANG 3D",
    "main_topic": "Deep sea ecosystem 3D visualization",
    "visual_type": "educational nature infographic",
    "design_style": "editorial modular design",
    "main_visual_description": "Vibrant 3D underwater diorama with coral reefs, sharks, and schools of fish. Realistic water caustic lighting.",
    "branding": "By Kreativ.ai",
    "render_quality": "8K resolution, photorealistic",
    "note": "Dapatkan visual spektakuler lainnya di Paket Hemat/Pro!"
}

# --- 3. SISTEM LOGIN SIDEBAR ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password Akses", type="password")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

# --- 4. TAMPILAN UTAMA & LOGIKA FREE TRIAL ---
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah ide menjadi infografis 3D kelas dunia.")

if not is_member:
    if user_pwd: # Jika password diisi tapi salah
        st.sidebar.error("❌ Password Salah! Cek email dari Lykn.id.")
    
    st.info("👋 **Selamat Datang!** Silakan coba kualitas Master Prompt kami secara gratis di bawah ini.")
    
    # Navigasi Radio agar tampilan lebar dan gagah
    choice = st.radio("Pilih Tema Master Prompt Gratis:", ["🦴 Anatomi
