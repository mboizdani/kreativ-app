import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; font-size: 18px; }
    .stButton>button:hover { background-color: #ff3333; box-shadow: 0px 0px 15px #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA PASSWORD ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. SISTEM LOGIN SIDEBAR ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password Akses", type="password")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

# --- 4. TAMPILAN UTAMA ---
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Generator Master Prompt 3D Kualitas Editorial & Sains (High-End)")

if not is_member:
    if user_pwd: 
        st.sidebar.error("❌ Password Salah!")
    st.info("💡 Silakan masukkan password akses di sidebar untuk mulai generate prompt spektakuler.")
    st.stop()

# --- 5. LOGIKA PAKET MEMBER ---
if is_pro:
    st.success("✅ Akses Aktif: Paket PRO")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Kreativ.ai")
else:
    st.success("✅ Akses Aktif: Paket HEMAT")
    st.info(f"💡 Watermark otomatis: **{custom_wm}**")

# --- 6. MESIN GENERATOR (ULTRA-DEEP JSON) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Deteksi model secara dinamis untuk menghindari 404
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'gemini-1.5-flash'
    if 'models/gemini-1.5-flash' in available_models:
        model_name = 'gemini-1.5-flash'
    else:
        model_name = available_models[0].replace('models/', '')

    model = genai.GenerativeModel(model_name)

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Daur Hidup Kupu-Kupu atau Anatomi Mesin")

    if st.button("Generate Master Prompt 🚀"):
        if topik:
            with st.spinner('Merancang Master Prompt JSON super detail...'):
                # INSTRUKSI UNTUK MENGHASILKAN STRUKTUR JSON YANG SANGAT DALAM
                instruksi = f"""
                You are a Professional Prompt Engineer specialized in 3D Infographics. 
                Generate an intricate, high-resolution 3D Infographic Master Prompt in JSON for the topic: '{topik}'.
                
                The output JSON must be extremely deep and structured exactly like this:
                - headline_text: (Title in Indonesian, caps)
                - main_topic: (Detailed English explanation)
                - visual_type: (e.g., biological infographic poster)
                - design_style: (e.g., editorial modular design)
                - main_visual_description: (A very detailed isometric 3D scene description with environment details)
                - supporting_visuals: (Zoom-in modules, cross-sections, or macroscopic views)
                - branding_watermark: "By {custom_wm}"
                - callout_titles: (Min 4 technical points in Indonesian)
                - data_elements: (Flow arrows, icons, scale indicators)
                - style_references: (e.g., National Geographic, Scientific Journals)
                - render_style: (Detail textures like chitin, silk, metal, wood grain)
                - negative_prompt: (cartoon, low resolution, blurry, messy layout)
                - aspect_ratio: "4:5"
                
                Ensure the branding "By {custom_wm}" is strictly embedded in the footer/watermark section.
                Return ONLY the JSON code block.
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Hasil Generator (Standar Kompetitor)")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.info(f"✅ Salin kode di atas. Master Prompt ini sudah dioptimasi untuk render 8K dengan watermark: **By {custom_wm}**")
                st.balloons()
        else:
            st.warning("Masukkan topik terlebih dahulu.")

except Exception as e:
    st.error(f"Terjadi kendala: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Visual Masa Depan")
