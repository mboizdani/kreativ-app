import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI VISUAL & BRANDING ---
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

# --- 2. AKSES KEAMANAN ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. SIDEBAR: LOGIN ---
st.sidebar.markdown("### 🏛️ Member Portal")
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Masukkan kunci akses...")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
branding_name = "Kreativ.ai"

# --- 4. TAMPILAN UTAMA ---
st.title("🚀 Prompt Generator Infografis Pro")
st.markdown("#### *Ubah Ide Menjadi Infografis 3D Mewah Kualitas 8K*")
st.markdown("---")

if not is_member:
    if user_pwd: 
        st.sidebar.error("❌ Kunci Akses Salah!")
    st.info("🔓 **Sistem Terkunci.** Silakan masukkan *Access Key* di samping untuk mulai membuat infografis.")
    st.stop()

# --- 5. PANEL KONTROL ---
if is_pro:
    st.success("💎 **Akses Premium:** Mode Custom Branding")
    branding_name = st.text_input("Ganti Watermark Brand Anda:", placeholder="Contoh: Kreativ.ai")
    if not branding_name:
        branding_name = "Kreativ.ai"
else:
    st.success("🌟 **Akses Standar:** Mode Kreativ.ai Branding")

# --- 6. MESIN GENERATOR (DEEP INFOGRAPHIC LOGIC) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'gemini-1.5-flash'
    if 'models/gemini-1.5-flash' in available_models:
        model_name = 'gemini-1.5-flash'
    else:
        model_name = available_models[0].replace('models/', '')

    model = genai.GenerativeModel(model_name)

    st.markdown("### 🧬 Konsep Infografis")
    topik = st.text_input("Apa yang ingin Anda buat infografisnya?", placeholder="Contoh: Daur Hidup Kupu-Kupu, Anatomi Tokek, dll.")

    if st.button("Generate Master Prompt ⚡"):
        if topik:
            with st.spinner('Merancang struktur infografis 8K...'):
                # INSTRUKSI FINAL: RASIO 2:3 & KUALITAS KOMPETITOR
                instruksi = f"""
                You are a Professional Prompt Engineer. Generate an intricate 3D Infographic Master Prompt in JSON for: '{topik}'.
                
                STRICT PARAMETERS:
                1. ASPECT RATIO: Strictly "2:3" (High-resolution vertical poster).
                2. CONCEPT: Cross-section isometric 'Diorama Box' with extreme depth.
                3. INFOGRAPHIC: Include headline, subheadline, 3 data sections with icons, and impact section in Indonesian.
                4. QUALITY: 8K resolution, photorealistic miniature photography, macro textures.
                5. BRANDING: Place high-contrast text 'By {branding_name}' at the BOTTOM CENTER.
                
                OUTPUT ONLY JSON:
                {{
                  "role": "professional_prompt_engineer",
                  "headline": "JUDUL DALAM BAHASA INDONESIA",
                  "branding": "By {branding_name} (Bottom Center)",
                  "visual_description": "Hyper-realistic isometric diorama box of {topik}. 8K, macro textures, studio lighting.",
                  "data_sections": ["Minimum 3 technical points in Indonesian"],
                  "render_settings": {{ "ratio": "2:3", "resolution": "8K" }},
                  "negative_prompt": "cartoon, low res, blurry, flat, missing watermark"
                }}
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                # --- 7. INSTRUKSI SIMPEL UNTUK PENGGUNA ---
                st.markdown("---")
                st.markdown("### ✅ Cara Pakai (Simpel):")
                st.markdown(f"""
                1. **Salin Kode:** Klik ikon salin pada kotak hitam di atas.
                2. **Buka AI Gambar:** Gunakan **ChatGPT** (Sangat Disarankan karena hasil lebih rapi) atau **Gemini**.
                3. **Tempel & Kirim:** Masukkan kode tadi ke chat AI Anda.
                
                *Tips: Meskipun bisa di versi gratis, hasil di **ChatGPT Plus/Pro** adalah yang terbaik untuk tulisan yang rapi.*
                """)
                st.balloons()
        else:
            st.warning("Silakan isi topik terlebih dahulu.")

except Exception as e:
    st.error(f"Terjadi kendala teknis. Pastikan API Key benar. Error: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Infografis Pro 8K")
