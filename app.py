import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PENGATURAN PASSWORD ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. SISTEM LOGIN SIDEBAR ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password", type="password")

if user_pwd:
    if user_pwd not in [PWD_HEMAT, PWD_PRO]:
        st.sidebar.error("❌ Password Salah! Cek email dari Lykn.id.")
        st.stop()
else:
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Masukkan password akses Anda di sidebar untuk memulai.")
    st.stop()

# --- 4. LOGIKA PAKET & WATERMARK ---
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

st.title("🎨 Kreativ.ai Prompt Generator")

if is_pro:
    st.success("✅ Akses Aktif: Paket PRO (Custom Watermark)")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: DigitalArt.id")
else:
    st.success("✅ Akses Aktif: Paket HEMAT (Watermark Kreativ.ai)")
    st.info("💡 Watermark otomatis: **Kreativ.ai**")

# --- 5. KONFIGURASI API ---
API_KEY = "AIzaSyDz8Uped3q9oGoN442MOHdfcIcco8KKpWw" 

try:
    genai.configure(api_key=API_KEY)
    
    # Deteksi model otomatis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    if available_models:
        model = genai.GenerativeModel(available_models[0])
    else:
        st.error("API Key bermasalah atau model tidak ditemukan.")
        st.stop()

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Klasifikasi Hewan")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang merancang visual modular...'):
                # INSTRUKSI VERSI OPTIMASI TEKS & WATERMARK TETAP
                instruksi = f"""
                You are a Professional Prompt Engineer. Generate a Modular 3D Infographic JSON for: '{topik}'.
                
                STRICT JSON STRUCTURE (Return ONLY JSON):
                {{
                  "headline_text": "JUDUL DALAM BAHASA INDONESIA",
                  "main_topic": "detailed visual of {topik}",
                  "visual_type": "educational infographic poster",
                  "design_style": "editorial modular design",
                  "main_visual_description": "A central 3D isometric scene showing {topik}. Use high-quality textures and studio lighting.",
                  "supporting_visuals": "3 smaller 3D isometric floating modules below the main scene zooming in on specific details.",
                  "callout_titles": ["Detail 1", "Detail 2", "Detail 3"],
                  "render_quality": "ultra high resolution, clear readable text, no blurry parts",
                  "ui_style": "flat vector UI elements with clean lines overlaying 3D models for readability",
                  "branding": {{
                    "watermark_text": "By {custom_wm}",
                    "watermark_position": "Bottom Right corner, distinct from the artwork",
                    "style": "Professional subtle typography"
                  }},
                  "negative_prompt": "blurry text, small unreadable labels, messy layout, cartoon"
                }}
                
                Content must be in Indonesian. Visual descriptions in English.
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.info("✅ Langkah Selanjutnya:")
                st.write("1. Salin kode di atas.")
                st.write("2. Tempel ke Gemini (Nano Banana) atau ChatGPT.")
                st.write(f"3. Watermark **'By {custom_wm}'** akan berada di pojok bawah.")
        else:
            st.warning("Isi topiknya dulu.")

except Exception as e:
    st.error(f"Terjadi kendala: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Lisensi Member Premium")
