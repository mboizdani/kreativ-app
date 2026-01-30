import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI HALAMAN ---
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

# JSON Statis Premium (Setara Kompetitor)
TRIAL_ANATOMI = {
    "headline_text": "ANATOMI TUBUH MANUSIA: SISTEM INTERNAL",
    "visual_description": "A hyper-realistic 3D isometric diorama box. Inside the cutaway box is a detailed model of the human torso. High-quality textures for skeletal and muscular systems. Museum spotlighting, 8K resolution.",
    "branding": "By Kreativ.ai",
    "note": "Beli Paket Pro untuk topik kustom & brand sendiri!"
}

TRIAL_LAUT = {
    "headline_text": "EKOSISTEM LAUT: TERUMBU KARANG 3D",
    "visual_description": "A vibrant 3D underwater diorama box. Featuring coral reefs, sharks, and marine life with realistic water caustic lighting. Detailed miniature photography style, 8K render.",
    "branding": "By Kreativ.ai",
    "note": "Akses fitur kustom tanpa batas di Paket Hemat/Pro!"
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
    if user_pwd: 
        st.sidebar.error("❌ Password Salah! Cek email dari Lykn.id.")
    
    st.info("👋 **Selamat Datang!** Silakan coba kualitas Master Prompt kami secara gratis di bawah ini.")
    
    choice = st.radio("Pilih Tema Master Prompt Gratis:", ["🦴 Anatomi Tubuh", "🌊 Ekosistem Laut"], horizontal=True)
    
    if choice == "🦴 Anatomi Tubuh":
        st.markdown("### 📊 Master Prompt (Anatomi)")
        st.code(str(TRIAL_ANATOMI).replace("'", '"'), language='json')
            
    elif choice == "🌊 Ekosistem Laut":
        st.markdown("### 📊 Master Prompt (Laut)")
        st.code(str(TRIAL_LAUT).replace("'", '"'), language='json')

    st.success("☝️ Salin kode di atas ke Gemini (Mode Nano Banana) atau ChatGPT Pro/Gratis!")
    st.markdown("---")
    st.warning("🔒 **Fitur Topik Kustom Terkunci.** Masukkan password di sidebar atau beli akses di Lykn.id untuk membuat topik kustom dengan brand Anda sendiri.")
    st.stop()

# --- 5. LOGIKA PAKET MEMBER ---
if is_pro:
    st.success("✅ Akses Aktif: Paket PRO (Custom Watermark)")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Kreativ.ai")
else:
    st.success("✅ Akses Aktif: Paket HEMAT (Watermark Tetap)")
    st.info("💡 Watermark otomatis: **Kreativ.ai**")

# --- 6. KONFIGURASI API (MENGGUNAKAN SECRETS) ---
try:
    # Mengambil API KEY secara aman dari Streamlit Secrets (Anti-Leaked)
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Mencari model otomatis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel(available_models[0])

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Cara Kerja Mesin Jet")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang merancang visual modular setara kualitas Pro...'):
                instruksi = f"""
                You are a Professional Prompt Engineer. Generate a Master 3D Infographic JSON for: '{topik}'.
                
                STRICT STRUCTURE (Return ONLY JSON):
                {{
                  "headline_text": "JUDUL DALAM BAHASA INDONESIA",
                  "main_visual_section": {{
                    "visual_concept": "3D Isometric Diorama Box",
                    "visual_description": "Hyper-realistic miniature photography style. A cutaway box showing {topik} with extreme detail, photorealistic textures, museum spotlighting, and shallow depth of field.",
                    "visual_style": ["photorealistic", "museum diorama", "tilt-shift macro", "8K render"]
                  }},
                  "data_sections": ["Detailed biological/technical points in Indonesian"],
                  "branding_requirement": {{
                    "mandatory_watermark": "By {custom_wm}",
                    "position": "Bottom Right corner",
                    "instruction": "Strictly render the text 'By {custom_wm}' as a clear digital watermark."
                  }},
                  "negative_prompt": "cartoon, low resolution, messy layout, missing watermark"
                }}
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Master Prompt Eksklusif")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.info(f"✅ Salin kode di atas. Hasil akan menyertakan watermark: **By {custom_wm}**")
                st.balloons()
        else:
            st.warning("Silakan masukkan topik riset Anda.")

except Exception as e:
    st.error(f"Terjadi kendala teknis. Pastikan GEMINI_API_KEY sudah terpasang di Secrets. Error: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
