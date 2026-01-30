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
st.write("Generator Master Prompt Infografis 3D Kualitas Museum (High-End Editorial)")

if not is_member:
    if user_pwd: 
        st.sidebar.error("❌ Password Salah!")
    st.info("💡 Silakan masukkan password akses di sidebar untuk mulai generate.")
    st.stop()

# --- 5. LOGIKA PAKET MEMBER ---
if is_pro:
    st.success("✅ Akses Aktif: Paket PRO")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Kreativ.ai")
else:
    st.success("✅ Akses Aktif: Paket HEMAT")
    st.info(f"💡 Watermark otomatis: **{custom_wm}**")

# --- 6. MESIN GENERATOR (OPTIMASI KUALITAS & FIX 404) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # SOLUSI ERROR 404: Mencari model yang tersedia secara dinamis
    model_name = 'gemini-1.5-flash' # Default
    try:
        # Cek apakah model flash tersedia, jika tidak pakai model pro
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if 'models/gemini-1.5-flash' in available_models:
            model_name = 'gemini-1.5-flash'
        elif 'models/gemini-1.5-pro' in available_models:
            model_name = 'gemini-1.5-pro'
        else:
            model_name = available_models[0].replace('models/', '')
    except:
        model_name = 'gemini-1.5-flash'

    model = genai.GenerativeModel(model_name)

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Anatomi Jantung atau Daur Hidup Kupu-Kupu")

    if st.button("Generate Master Prompt 🚀"):
        if topik:
            with st.spinner('Merancang visual 8K dengan standar museum...'):
                # INSTRUKSI "ULTRA-DETAIL" UNTUK MENYAMAI/MELEBIHI KOMPETITOR
                instruksi = f"""
                You are a Professional Prompt Engineer. Generate an intricate 3D Infographic Master Prompt in JSON for: '{topik}'.
                
                MUST FOLLOW THESE AESTHETIC RULES:
                1. CONCEPT: A cross-section isometric 'Diorama Box' or 'Cutaway Box' viewed from a 45-degree angle.
                2. VISUAL STYLE: Photorealistic miniature photography, handcrafted detailed modeling, museum diorama aesthetic.
                3. TEXTURE: Use 'resin glossy finish', '3D embossed typography', and 'realistic organic materials like carved wood or glass'.
                4. LIGHTING: Cinematic Chiaroscuro lighting, warm museum spotlights, and soft ambient occlusion shadows.
                5. CAMERA: Tilt-shift macro lens effect, shallow depth of field (sharp focus on subject, blurred background).
                
                STRICT JSON STRUCTURE (Return ONLY the JSON block):
                {{
                  "role": "professional_prompt_engineer",
                  "project_type": "editorial_3D_infographic_template",
                  "headline_section": {{
                    "text": "JUDUL DALAM BAHASA INDONESIA (Capslock)",
                    "style": "3D EMBOSSED bold typography"
                  }},
                  "main_visual_concept": "A hyper-realistic isometric diorama box of {topik}. Intricate miniature details, 8K resolution, realistic paper/resin textures, and studio lighting with dramatic shadows.",
                  "branding_footer": "By {custom_wm}",
                  "negative_prompt": "cartoon, low quality, blurry, messy layout, flat 2D, distorted text, penulisan kode warna"
                }}
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Hasil Generator (Kualitas Premium)")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.info(f"✅ Salin kode di atas. Hasil visual akan menyertakan watermark: **By {custom_wm}**")
                st.balloons()
        else:
            st.warning("Masukkan topik terlebih dahulu.")

except Exception as e:
    st.error(f"Terjadi kendala: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Visual Masa Depan")
