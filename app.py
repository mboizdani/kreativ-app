import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI VISUAL PREMIUM ---
st.set_page_config(page_title="Prompt Generator Infografis Pro", page_icon="🎨", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        height: 4em; 
        background: linear-gradient(45deg, #FF4B4B, #FF8C00); 
        color: white; 
        border: none; 
        font-weight: bold; 
        font-size: 20px;
        transition: 0.3s;
    }
    .stButton>button:hover { 
        transform: scale(1.02);
        box-shadow: 0px 8px 20px rgba(255, 75, 75, 0.4);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA PASSWORD AKSES ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. SIDEBAR: MEMBER PORTAL ---
st.sidebar.markdown("### 🏛️ Member Portal")
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Masukkan kunci akses...")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
branding_name = "Kreativ.ai"

# --- 4. DASHBOARD UTAMA ---
st.title("🚀 Prompt Generator Infografis Pro")
st.markdown("#### *The Ultimate 8K High-Definition Infographic Engine*")
st.markdown("---")

if not is_member:
    if user_pwd: 
        st.sidebar.error("❌ Invalid Access Key!")
    st.info("🔓 **Sistem Terkunci.** Masukkan *Access Key* di sidebar untuk mengaktifkan mesin generator.")
    st.stop()

# --- 5. PANEL KONTROL MEMBER ---
if is_pro:
    st.success("💎 **Akses Premium Aktif:** Mode Custom Branding")
    branding_name = st.text_input("Identity / Watermark Brand Anda:", placeholder="Contoh: Kreativ.ai")
    if not branding_name:
        branding_name = "Kreativ.ai"
else:
    st.success("🌟 **Akses Standar Aktif:** Mode Kreativ.ai Branding")
    st.info(f"💡 Watermark Otomatis: **{branding_name}**")

# --- 6. CORE ENGINE (FIX ERROR 404 & DEEP LOGIC) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # PERBAIKAN PERMANEN ERROR 404: Mencari model yang tersedia secara dinamis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # Mencari model flash di dalam daftar model yang tersedia
    target_model = "gemini-1.5-flash"
    found_model = next((m for m in available_models if target_model in m), available_models[0])
    
    model = genai.GenerativeModel(found_model)

    st.markdown("### 🧬 Konsep Infografis")
    topik = st.text_input("Apa materi yang ingin Anda buat infografisnya?", placeholder="Contoh: Anatomi Tokek, Daur Hidup Kupu-Kupu, dll.")

    if st.button("Generate Master Prompt Sekarang ⚡"):
        if topik:
            with st.spinner('Merancang struktur infografis 8K Ultra-HD...'):
                instruksi = f"""
                Act as a Professional Senior Visual Strategist. Generate an intricate 3D Infographic Master Prompt in JSON for: '{topik}'.
                
                STRICT DESIGN RULES:
                1. INFOGRAPHIC FUNCTION: Must be a functional infographic with a central 'Diorama Box' surrounded by floating data modules and labels in Indonesian.
                2. ZOOM QUALITY: Force '8K resolution' and 'macro textures' to ensure extreme detail when zoomed.
                3. ASPECT RATIO: Strictly locked to '2:3' (Vertical Poster).
                4. WATERMARK: Strictly place a high-contrast digital watermark 'By {branding_name}' at the BOTTOM CENTER.
                5. VISUAL STYLE: 3D Isometric, Museum Diorama, Cinematic Chiaroscuro lighting.

                JSON Output (Indonesian Content):
                {{
                  "role": "professional_visual_strategist",
                  "headline": "JUDUL DALAM BAHASA INDONESIA",
                  "branding": "By {branding_name} at Bottom Center",
                  "visual_description": "8K hyper-realistic isometric diorama box of {topik} with macro textures...",
                  "infographic_elements": ["Technical points in Indonesian with 3D icons"],
                  "render_settings": {{ "ratio": "2:3", "resolution": "8K" }},
                  "negative_prompt": "cartoon, flat, messy, missing watermark, low resolution"
                }}
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                # --- 7. PANDUAN LANGKAH SELANJUTNYA (SIMPEL) ---
                st.markdown("---")
                st.markdown("### ✅ Cara Pakai (Sangat Mudah):")
                st.markdown(f"""
                1. **Salin Kode:** Klik ikon salin pada kotak hitam di atas.
                2. **Buka AI Gambar:** Gunakan **ChatGPT** (Sangat Disarankan) atau **Gemini**.
                3. **Tempel & Kirim:** Masukkan kode tadi ke kolom chat AI dan tekan Enter.
                
                *Note: Hasil terbaik untuk tulisan rapi dan detail mewah ada di **ChatGPT Pro/Gratis**.*
                """)
                st.balloons()
        else:
            st.warning("Silakan isi topik terlebih dahulu.")

except Exception as e:
    st.error(f"Terjadi kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Professional 8K Infographic Solution")
