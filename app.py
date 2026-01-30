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

# --- 2. PENGATURAN PASSWORD ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. SISTEM LOGIN SIDEBAR ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password Akses", type="password")

if user_pwd:
    if user_pwd not in [PWD_HEMAT, PWD_PRO]:
        st.sidebar.error("❌ Password Salah! Cek email dari Lykn.id.")
        st.stop()
else:
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Silakan masukkan password akses Anda di sidebar untuk memulai.")
    st.stop()

# --- 4. LOGIKA PAKET & WATERMARK ---
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

st.title("🎨 Kreativ.ai Prompt Generator")

if is_pro:
    st.success("✅ Akses Aktif: Paket PRO (Custom Watermark)")
    # UPDATE: Placeholder menggunakan nama brand Anda agar melekat di pengguna
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Kreativ.ai atau NamaBrandAnda")
else:
    st.success("✅ Akses Aktif: Paket HEMAT (Watermark Kreativ.ai)")
    st.info("💡 Watermark otomatis: **Kreativ.ai**")

# --- 5. KONFIGURASI API ---
API_KEY = "AIzaSyDz8Uped3q9oGoN442MOHdfcIcco8KKpWw" 

try:
    genai.configure(api_key=API_KEY)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel(available_models[0])

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Ekosistem Laut")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang merancang visual...'):
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
                
                st.markdown("### 📊 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.info("✅ Langkah Selanjutnya:")
                st.write(f"1. Salin kode di atas.")
                st.write("2. Tempel ke **Gemini** atau **ChatGPT Pro** untuk hasil terbaik. Jika tidak punya Pro, bisa gunakan **ChatGPT Gratis**.")
                st.write(f"3. Hasil gambar akan otomatis menyertakan watermark: **By {custom_wm}**")
        else:
            st.warning("Isi topiknya dulu.")

except Exception as e:
    st.error(f"Terjadi kendala: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
