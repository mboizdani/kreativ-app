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

# Contoh JSON Statis (Tampilan Lebar & Mewah)
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
    if user_pwd: 
        st.sidebar.error("❌ Password Salah! Cek email dari Lykn.id.")
    
    st.info("👋 **Selamat Datang!** Silakan coba kualitas Master Prompt kami secara gratis di bawah ini.")
    
    # Navigasi Radio (Pilihan Tema Gratis)
    choice = st.radio("Pilih Tema Master Prompt Gratis:", ["🦴 Anatomi Tubuh", "🌊 Ekosistem Laut"], horizontal=True)
    
    if choice == "🦴 Anatomi Tubuh":
        st.markdown("### 📊 Master Prompt (Anatomi)")
        st.code(str(TRIAL_ANATOMI).replace("'", '"'), language='json')
            
    elif choice == "🌊 Ekosistem Laut":
        st.markdown("### 📊 Master Prompt (Laut)")
        st.code(str(TRIAL_LAUT).replace("'", '"'), language='json')

    st.success("☝️ Salin seluruh kode di atas ke Gemini atau ChatGPT!")
    st.markdown("---")
    st.warning("🔒 **Fitur Topik Kustom Terkunci.** Masukkan password di sidebar atau beli akses di Lykn.id untuk membuat topik kustom dengan brand Anda sendiri.")
    st.stop()

# --- 5. LOGIKA PAKET MEMBER (Hanya muncul jika login berhasil) ---
if is_pro:
    st.success("✅ Akses Aktif: Paket PRO (Custom Watermark)")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Kreativ.ai")
else:
    st.success("✅ Akses Aktif: Paket HEMAT (Watermark Tetap)")
    st.info("💡 Watermark otomatis: **Kreativ.ai**")

# --- 6. KONFIGURASI API (MENGGUNAKAN SECRETS) ---
try:
    # Mengambil API KEY secara aman dari Streamlit Secrets
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Mencari model otomatis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel(available_models[0])

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Cara Kerja Mesin Jet")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang merancang visual modular...'):
                instruksi = f"""
                You are a Professional Prompt Engineer. Generate a Modular 3D Infographic JSON for: '{topik}'.
                STRICT JSON STRUCTURE (Return ONLY JSON):
                {{
                  "headline_text": "JUDUL DALAM BAHASA INDONESIA",
                  "main_topic": "highly detailed visual of {topik}",
                  "visual_type": "educational infographic poster",
                  "design_style": "editorial modular design",
                  "main_visual_description": "A stunning central 3D isometric scene of {topik}. Ultra-realistic textures, 8K resolution, and studio lighting.",
                  "supporting_visuals": "3 floating 3D modules below the main scene with clear educational callouts.",
                  "render_quality": "Masterpiece quality, photorealistic, sharp focus on all text elements",
                  "branding_requirement": {{
                    "mandatory_watermark": "By {custom_wm}",
                    "position": "Bottom Right corner",
                    "instruction": "Strictly render the text 'By {custom_wm}' as a clear, readable digital watermark on the bottom right corner."
                  }},
                  "negative_prompt": "blurry text, messy layout, missing watermark, cartoonish"
                }}
                Content: Indonesian. Visual Descriptions: English.
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Master Prompt Eksklusif")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.info(f"✅ Langkah Selanjutnya: Salin kode di atas. Hasil akan menyertakan watermark: **By {custom_wm}**")
                st.balloons()
        else:
            st.warning("Silakan masukkan topik riset Anda.")

except Exception as e:
    st.error(f"Terjadi kendala teknis. Pastikan GEMINI_API_KEY sudah terpasang di Streamlit Secrets. Error: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
