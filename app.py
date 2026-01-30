import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI VISUAL PREMIUM & LAYOUT ---
st.set_page_config(page_title="Kreativ.ai - The Ultimate 3D Infographic Engine", page_icon="🎨", layout="wide")

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
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Enter your key...")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
# Default branding tetap Kreativ.ai
custom_wm = "Kreativ.ai"

# --- 4. DASHBOARD UTAMA ---
st.title("🚀 Kreativ.ai: 3D Visualization Engine")
st.markdown("#### *The Future of 8K High-Definition Educational Infographics*")
st.markdown("---")

if not is_member:
    if user_pwd: 
        st.sidebar.error("❌ Invalid Access Key!")
    st.info("🔓 **Sistem Terkunci.** Masukkan *Access Key* di sidebar untuk mengaktifkan mesin generator infografis.")
    st.stop()

# --- 5. PANEL KONTROL MEMBER ---
if is_pro:
    st.success("💎 **Akses Premium Aktif:** Mode Custom Branding Aktif")
    custom_wm = st.text_input("Ganti Watermark Brand Anda:", placeholder="Contoh: Kreativ.ai")
    if not custom_wm:
        custom_wm = "Kreativ.ai"
else:
    st.success("🌟 **Akses Standar Aktif:** Mode Kreativ.ai Branding")
    st.info(f"💡 Watermark Otomatis: **{custom_wm}**")

# --- 6. CORE ENGINE (8K INFOGRAPHIC DEPTH LOGIC) ---
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
    topik = st.text_input("Apa yang ingin Anda visualisasikan hari ini?", placeholder="Contoh: Anatomi Burung Hantu, Mekanisme Mesin Turbo, dll.")

    if st.button("Generate Master Prompt Sekarang ⚡"):
        if topik:
            with st.spinner('Merancang struktur infografis 8K Ultra-HD...'):
                # INSTRUKSI FINAL: FOKUS FUNGSI INFOGRAFIS + KUALITAS ZOOM + WATERMARK TENGAH
                instruksi = f"""
                You are a Professional Senior Visual Strategist. Generate an intricate 3D Infographic Master Prompt in JSON for: '{topik}'.
                
                STRICT DESIGN RULES FOR UNBEATABLE QUALITY:
                1. INFOGRAPHIC FUNCTION: This is NOT just an aesthetic image. It must be a functional infographic with a central 'Diorama Box' subject surrounded by multiple floating data modules, icons, and technical labels in Indonesian.
                2. ZOOM QUALITY (8K): Force 'ultra-detailed macro textures' (microscopic detail on surfaces like paper, skin, or metal) to ensure the image remains sharp when zoomed.
                3. WATERMARK CONSISTENCY: Strictly place a clean, bold digital watermark 'By {custom_wm}' at the BOTTOM CENTER. It must be high-contrast and stand alone, not blending with the 3D objects.
                4. VISUAL STYLE: 3D Isometric, Museum Diorama, Cinematic Chiaroscuro lighting, photorealistic 8K render.

                JSON Output Requirements (English structure, Indonesian content):
                {{
                  "role": "professional_visual_strategist",
                  "headline": "JUDUL DALAM BAHASA INDONESIA (CAPSLOCK)",
                  "branding_identity": {{
                    "text": "By {custom_wm}",
                    "position": "Bottom Center (STRICT)",
                    "style": "High-contrast digital text"
                  }},
                  "main_visual_anatomy": "Extremely detailed description of the {topik} diorama including 8K macro textures...",
                  "infographic_modules": [
                    {{ "segment": "Bagian 1", "detail": "Penjelasan mendalam..." }},
                    {{ "segment": "Bagian 2", "detail": "Penjelasan mendalam..." }}
                  ],
                  "render_settings": {{ "resolution": "8K Ultra-HD", "lighting": "Museum spotlights", "texture_depth": "Macro level" }},
                  "negative_prompt": "blurry, low resolution, messy layout, missing watermark, cartoon, 2D"
                }}
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                # --- 7. PANDUAN LANGKAH SELANJUTNYA (SESUAI KESEPAKATAN) ---
                st.markdown("---")
                st.markdown("### ✅ Langkah Selanjutnya (Instruksi Penggunaan):")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("""
                    **1. Salin Kode JSON**
                    Klik ikon salin di pojok kanan atas kotak hitam di atas. Kode ini sudah dioptimasi untuk render visual 8K.
                    
                    **2. Pilih Platform AI Anda**
                    * **ChatGPT Pro/Plus (Sangat Disarankan):** Hasil paling realistis, teks paling rapi, dan layout paling fungsional.
                    * **ChatGPT Gratis:** Tetap bisa digunakan, namun kualitas visual mungkin standar.
                    * **Gemini (Mode Pro/Nano Banana):** Hasil visual spektakuler dan cepat, namun terkadang teks butuh penyesuaian.
                    """)
                with col2:
                    st.markdown(f"""
                    **3. Tempel & Generate**
                    Tempel kode JSON tersebut ke kolom chat AI pilihan Anda.
                    
                    **4. Tips Hasil Maksimal**
                    Jika watermark **By {custom_wm}** di tengah bawah belum muncul sempurna, cukup ketik: *"Add the branding text from the JSON at the bottom center"*.
                    """)
                st.balloons()
        else:
            st.warning("Silakan isi topik terlebih dahulu.")

except Exception as e:
    st.error(f"Koneksi API terganggu. Mohon coba lagi. Error: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Professional 8K Infographic Solution")
