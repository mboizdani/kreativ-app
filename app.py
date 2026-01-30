import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI VISUAL PREMIUM ---
st.set_page_config(page_title="Kreativ.ai - The Ultimate 3D Prompt Engine", page_icon="🎨")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        height: 3.8em; 
        background: linear-gradient(45deg, #FF4B4B, #FF8C00); 
        color: white; 
        border: none; 
        font-weight: bold; 
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover { 
        transform: scale(1.02);
        box-shadow: 0px 5px 15px rgba(255, 75, 75, 0.4);
    }
    /* Menghilangkan header default streamlit untuk kesan profesional */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. KONFIGURASI AKSES ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. SIDEBAR: AUTHENTICATION ---
st.sidebar.markdown("### 🏛️ Member Portal")
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Enter your key...")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

# --- 4. DASHBOARD UTAMA ---
st.title("🚀 Kreativ.ai: 3D Visualization Engine")
st.markdown("#### *Transforming Ideas into High-End 8K Cinematic Visuals*")
st.markdown("---")

if not is_member:
    if user_pwd: 
        st.sidebar.error("❌ Invalid Access Key!")
    st.info("🔓 **Sistem Terkunci.** Silakan masukkan *Access Key* Anda di sidebar untuk mengaktifkan mesin generator.")
    st.stop()

# --- 5. PANEL KONTROL MEMBER ---
if is_pro:
    st.success("💎 **Akses Premium Aktif:** Mode Custom Branding")
    custom_wm = st.text_input("Identity / Watermark Brand Anda:", placeholder="Contoh: StudioBarik.ai")
else:
    st.success("🌟 **Akses Standar Aktif:** Mode Kreativ.ai Branding")
    st.info(f"💡 Watermark Otomatis: **{custom_wm}**")

# --- 6. CORE ENGINE (ULTRA-DEEP PROMPT LOGIC) ---
try:
    # Mengambil API KEY secara aman
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Deteksi model paling stabil secara dinamis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'gemini-1.5-flash'
    if 'models/gemini-1.5-flash' in available_models:
        model_name = 'gemini-1.5-flash'
    else:
        model_name = available_models[0].replace('models/', '')

    model = genai.GenerativeModel(model_name)

    st.markdown("### 🧬 Konsep Visual")
    topik = st.text_input("Topik atau Materi yang Ingin Divisualisasikan:", placeholder="Contoh: Mekanisme Sel Manusia, Arsitektur Modern, dll.")

    if st.button("Generate Master Prompt ⚡"):
        if topik:
            with st.spinner('Membangun struktur data visual 8K...'):
                # INSTRUKSI PROFIL TINGGI (High-End Editorial Strategy)
                instruksi = f"""
                Act as a Professional Senior Prompt Engineer. 
                Generate a complex 3D Infographic Master Prompt in JSON for: '{topik}'.
                
                The output must strictly include these professional parameters:
                1. CONCEPT: A Cross-section isometric 'Diorama Box' with extreme depth.
                2. VISUAL QUALITY: 8K resolution, photorealistic miniature photography style.
                3. TEXTURES: Macro level details (resin, fibrous paper, glass, embossed metal).
                4. LIGHTING: Cinematic Chiaroscuro lighting with sharp museum spotlights and ambient occlusion.
                5. STRUCTURE: Modular editorial layout with floating supporting visuals and labels.
                
                JSON Requirements (English output for prompt sections, Indonesian for text content):
                {{
                  "role": "professional_visual_strategist",
                  "headline_text": "JUDUL MATERI (CAPSLOCK)",
                  "main_topic": "Strategic visual breakdown of {topik}",
                  "visual_style": "High-end editorial 3D diorama",
                  "main_visual_description": "Extremely detailed description of the central 3D scene...",
                  "supporting_modules": "Floating 3D zoom-in sections showing internal structures",
                  "branding_identity": "By {custom_wm}",
                  "callout_labels": ["Minimum 4 technical points in Indonesian"],
                  "render_settings": {{
                    "resolution": "8K",
                    "lighting": "Studio spotlighting",
                    "camera": "Tilt-shift macro lens"
                  }},
                  "negative_prompt": "cartoon, messy, flat, blurry, low resolution, inaccurate anatomy/structure"
                }}
                
                Return ONLY the JSON code block.
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.success(f"✅ **Master Prompt Berhasil Dibuat.** Salin kode di atas ke AI Visual Anda (ChatGPT/Gemini).")
                st.markdown(f"> **Note:** Hasil visual akan menyertakan identitas: **By {custom_wm}**")
                st.balloons()
        else:
            st.warning("Silakan isi topik terlebih dahulu.")

except Exception as e:
    st.error(f"Sistem sedang sibuk atau konfigurasi API salah. Error: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Advanced Prompt Engineering Solution")
