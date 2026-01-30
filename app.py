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
    st.info("💡 Silakan masukkan password akses di sidebar untuk mulai generate prompt spektakuler.")
    st.stop()

# --- 5. LOGIKA PAKET MEMBER ---
if is_pro:
    st.success("✅ Akses Aktif: Paket PRO")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Kreativ.ai")
else:
    st.success("✅ Akses Aktif: Paket HEMAT")
    st.info(f"💡 Watermark otomatis: **{custom_wm}**")

# --- 6. MESIN GENERATOR (OPTIMASI KUALITAS KOMPETITOR) ---
try:
    # Mengambil API KEY secara aman dari Streamlit Secrets
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Perbaikan Error 404: Menggunakan inisialisasi model yang lebih aman
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Anatomi Jantung atau Cara Kerja Mesin")

    if st.button("Generate Master Prompt 🚀"):
        if topik:
            with st.spinner('Merancang visual 8K dengan standar editorial...'):
                # INSTRUKSI "ULTRA-DETAIL" UNTUK MENYAMAI/MELEBIHI KOMPETITOR
                instruksi = f"""
                You are a Professional Prompt Engineer. Generate an intricate 3D Infographic Master Prompt in JSON for: '{topik}'.
                The prompt MUST strictly follow these aesthetic rules to ensure high-end museum quality:
                
                1. CONCEPT: A cross-section isometric 'Diorama Box' viewed from a 45-degree angle.
                2. VISUAL STYLE: Photorealistic miniature photography, handcrafted detailed modeling, museum diorama aesthetic.
                3. TEXTURE: Use 'resin glossy finish', 'carved textures', '3D embossed typography', and 'realistic organic materials'.
                4. LIGHTING: Cinematic Chiaroscuro lighting, warm museum spotlights, and soft ambient occlusion shadows.
                5. CAMERA: Tilt-shift macro lens effect, shallow depth of field (bokeh background).
                
                STRICT JSON STRUCTURE (Return ONLY the JSON block):
                {{
                  "role": "professional_prompt_engineer",
                  "project_type": "editorial_3D_infographic_template",
                  "headline_section": {{
                    "text": "JUDUL DALAM BAHASA INDONESIA (Capslock)",
                    "style": "3D EMBOSSED bold typography resembling carved signage"
                  }},
                  "main_visual": "A stunning, hyper-realistic isometric diorama box of {topik}. Intricate miniature details, 8K resolution, photorealistic paper and resin textures, studio lighting with dramatic shadows.",
                  "branding_footer": "By {custom_wm}",
                  "negative_prompt": "cartoon, low quality, blurry, messy layout, flat 2D, human hands, distorted text"
                }}
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Hasil Generator (Kualitas Premium)")
                # Menampilkan hasil bersih tanpa markdown tambahan
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
