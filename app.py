import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI BRANDING KREATIV.AI ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #ff3333; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PENGATURAN PASSWORD (SESUAIKAN DENGAN LYKN.ID) ---
PWD_HEMAT = "HEMAT2026"  # Untuk Paket Rp 19.000
PWD_PRO = "PROCUAN2026" # Untuk Paket Rp 49.000

# --- 3. SISTEM LOGIN SIDEBAR ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password Akses", type="password")

if user_pwd not in [PWD_HEMAT, PWD_PRO]:
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Silakan masukkan password akses yang Anda dapatkan dari Lykn.id untuk mengaktifkan tools.")
    st.image("https://via.placeholder.com/800x400.png?text=Akses+Terkunci+-+Beli+di+Lykn.id", use_container_width=True)
    st.stop()

# --- 4. LOGIKA PAKET & WATERMARK ---
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

st.title("🎨 Kreativ.ai Prompt Generator Pro")
st.success(f"Akses Aktif: {'Paket PRO (Custom Watermark)' if is_pro else 'Paket HEMAT (Watermark Tetap)'}")

if is_pro:
    st.subheader("⚙️ Pengaturan Brand (Versi Pro)")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: NamaToko.id")
else:
    st.info("💡 Anda menggunakan Paket Hemat. Watermark dikunci pada: **Kreativ.ai**")

# --- 5. KONFIGURASI API & MODEL ---
# GANTI DENGAN API KEY BARU ANDA DARI GOOGLE AI STUDIO
API_KEY = "AIzaSyDz8Uped3q9oGoN442MOHdfcIcco8KKpWw" 

try:
    genai.configure(api_key=API_KEY)
    
    # Mencari model yang tersedia secara otomatis (Anti Error 404)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    if available_models:
        model = genai.GenerativeModel(available_models[0])
    else:
        st.error("Model AI tidak ditemukan. Cek kembali API Key Anda.")
        st.stop()

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Anatomi Tubuh Manusia")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner(f'Kreativ.ai sedang merancang visual menggunakan {available_models[0]}...'):
                
                # INSTRUKSI TEGAS: Riset + Master Prompt
                instruksi = f"""
