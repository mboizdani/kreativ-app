import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI BRANDING ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; font-size: 18px; }
    .stButton>button:hover { background-color: #ff3333; box-shadow: 0px 0px 15px #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA PASSWORD & CONTOH (UPDATED QUALITY) ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# Contoh JSON Statis yang sudah di-upgrade kualitasnya
TRIAL_ANATOMI = {
    "role": "professional_prompt_engineer",
    "headline": "ANATOMI MANUSIA: SISTEM INTERNAL",
    "visual_concept": "Cross-section 3D Isometric Diorama Box",
    "visual_description": "A hyper-realistic miniature photography style of a human torso inside a museum glass diorama. Featuring 3D embossed organs with realistic textures (muscles, bones, veins). Use shallow depth of field and dramatic studio spotlighting.",
    "branding": "By Kreativ.ai",
    "render_quality": "8K, Photorealistic, Cinematic Lighting"
}

# --- 3. SISTEM LOGIN SIDEBAR ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password Akses", type="password")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

# --- 4. TAMPILAN UTAMA & FREE TRIAL ---
st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Generator Prompt Infografis 3D Kualitas Museum (8K Resolution)")

if not is_member:
    if user_pwd: 
        st.sidebar.error("❌ Password Salah!")
    
    st.info("👋 **Mode Demo:** Coba kualitas Master Prompt kami secara gratis.")
    choice = st.radio("Pilih Contoh Tema:", ["🦴 Anatomi Tubuh", "🦖 Anatomi Tokek (Gaya Kompetitor)"], horizontal=True)
    
    if "Anatomi Tubuh" in choice:
        st.code(str(TRIAL_ANATOMI).replace("'", '"'), language='json')
    else:
        st.write("💡 *Klik tombol untuk melihat kualitas setara kompetitor.*")
        if st.button("Lihat Prompt Gaya Kompetitor"):
            st.code('{"role": "professional_prompt_engineer", "headline": "ANATOMI TOKEK: MASTER ADAPTASI", "visual_concept": "Gecko Natural Habitat Diorama Box", "style": "photorealistic miniature photography, museum diorama, tilt-shift macro lens", "branding": "By Kreativ.ai"}', language='json')

    st.success("☝️ Salin kode ke Gemini (Nano Banana) atau ChatGPT!")
    st.stop()

# --- 5. LOGIKA MEMBER PRO ---
if is_pro:
    st.success("✅ Akses Aktif: Paket PRO")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Kreativ.ai")
else:
    st.success("✅ Akses Aktif: Paket HEMAT")
    st.info("💡 Watermark: **Kreativ.ai**")

# --- 6. MESIN GENERATOR (UPGRADED TO COMPETITOR QUALITY) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Mekanisme Kerja Jantung")

    if st.button("Generate Master Prompt 🚀"):
        if topik:
            with st.spinner('Sedang merancang instruksi visual kualitas tinggi...'):
                # INSTRUKSI SUPER DETAIL AGAR HASIL SEPERTI KOMPETITOR
                instruksi = f"""
                Create a professional editorial 3D infographic Master Prompt in JSON for: '{topik}'.
                The prompt must force the AI to create:
                1. A 'Museum Diorama Box' or 'Cutaway Box' structure.
                2. 'Photorealistic miniature photography' style with 'tilt-shift macro lens' effect.
                3. High-contrast 'Chiaroscuro lighting' with museum spotlights.
                4. Textures must be described as: 'Handcrafted detailed modeling', 'Resin finish', '3D embossed typography'.
                5. Add mandatory watermark text: 'By {custom_wm}' on the bottom right corner.
                
                Structure:
                {{
                  "role": "professional_prompt_engineer",
                  "headline": "JUDUL DALAM BAHASA INDONESIA",
                  "main_visual": "Hyper-realistic isometric diorama box of {topik}. Intense detail, 8K, studio lighting.",
                  "style_rules": ["museum diorama", "photorealistic miniature", "cinematic shadows"],
                  "branding": "By {custom_wm}"
                }}
                Return ONLY JSON code.
                """
                response = model.generate_content(instruksi)
                st.markdown("### 💎 Hasil Generator (Kualitas Pro)")
                st.code(response.text.replace("```json", "").replace("```", "").strip(), language='json')
                st.balloons()
except Exception as e:
    st.error(f"Error: {e}")
