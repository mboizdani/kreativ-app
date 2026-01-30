import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI BRANDING ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PENGATURAN PASSWORD & DATA ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# Contoh JSON Statis untuk Free Trial
TRIAL_ANATOMI = {
    "headline_text": "ANATOMI TUBUH MANUSIA: SISTEM INTERNAL",
    "main_topic": "Detailed 3D human anatomy overview",
    "main_visual_description": "A stunning 3D isometric diorama of a human torso in a glass box. Showing skeletal, muscular, and circulatory systems with glowing accents.",
    "branding": "By Kreativ.ai",
    "note": "Ini adalah contoh kualitas 8K Kreativ.ai. Beli Paket Pro untuk topik kustom & brand sendiri!"
}

TRIAL_LAUT = {
    "headline_text": "EKOSISTEM LAUT: KEHIDUPAN TERUMBU KARANG",
    "main_topic": "Deep sea ecosystem 3D visualization",
    "main_visual_description": "Vibrant 3D underwater diorama with coral reefs, sharks, and schools of fish. Realistic water caustic lighting and 8K textures.",
    "branding": "By Kreativ.ai",
    "note": "Kualitas visual spektakuler! Ingin buat topik lain? Cek paket hemat/pro kami."
}

# --- 3. SISTEM LOGIN SIDEBAR ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password untuk Akses Penuh", type="password")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

# --- 4. TAMPILAN UTAMA ---
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah ide menjadi infografis 3D kelas dunia.")

if not is_member:
    st.info("👋 **Selamat Datang!** Silakan coba kualitas kami secara gratis di bawah ini.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎁 Coba Gratis: Anatomi"):
            st.markdown("### 📊 Master Prompt (Anatomi)")
            st.code(str(TRIAL_ANATOMI), language='json')
            st.success("☝️ Salin kode di atas ke Gemini atau ChatGPT!")
            
    with col2:
        if st.button("🎁 Coba Gratis: Laut"):
            st.markdown("### 📊 Master Prompt (Laut)")
            st.code(str(TRIAL_LAUT), language='json')
            st.success("☝️ Salin kode di atas ke Gemini atau ChatGPT!")

    st.markdown("---")
    st.warning("🔒 **Fitur Topik Kustom Terkunci.** Silakan masukkan password di sidebar atau beli akses di Lykn.id untuk membuat topik apa pun dengan brand Anda sendiri.")
    st.stop()

# --- 5. LOGIKA MEMBER (Hanya muncul jika password benar) ---
if is_pro:
    st.success("✅ Akses Aktif: Paket PRO")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Kreativ.ai")
else:
    st.success("✅ Akses Aktif: Paket HEMAT")
    st.info("💡 Watermark otomatis: **Kreativ.ai**")

# --- 6. KONFIGURASI API ---
API_KEY = "TEMPEL_API_KEY_BARU_DI_SINI" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    topik = st.text_input("Apa topik kustom Anda?", placeholder="Contoh: Cara Kerja Mesin Roket")

    if st.button("Generate Prompt Kustom ✨"):
        if topik:
            with st.spinner('Merancang visual eksklusif Anda...'):
                instruksi = f"Generate 3D Infographic JSON for: '{topik}' with branding 'By {custom_wm}'. Use modular 3D isometric style, 8K, photorealistic. Return ONLY JSON."
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Hasil Eksklusif Anda")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                st.balloons()
        else:
            st.warning("Masukkan topik dulu ya.")

except Exception as e:
    st.error(f"Kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
