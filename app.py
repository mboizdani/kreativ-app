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
st.markdown("#### *Transforming Ideas into High-End 8K Infographic Visuals*")
st.markdown("---")

if not is_member:
    if user_pwd: 
        st.sidebar.error("❌ Invalid Access Key!")
    st.info("🔓 **Sistem Terkunci.** Silakan masukkan *Access Key* Anda di sidebar untuk mengaktifkan mesin generator.")
    st.stop()

# --- 5. PANEL KONTROL MEMBER ---
if is_pro:
    st.success("💎 **Akses Premium Aktif:** Mode Custom Branding")
    custom_wm = st.text_input("Identity / Watermark Brand Anda:", placeholder="Contoh: Kreativ.ai")
    if not custom_wm:
        custom_wm = "Kreativ.ai"
else:
    st.success("🌟 **Akses Standar Aktif:** Mode Kreativ.ai Branding")
    st.info(f"💡 Watermark Otomatis: **{custom_wm}**")

# --- 6. CORE ENGINE (DEEP INFOGRAPHIC PROMPT ENGINEERING) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Deteksi model secara dinamis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'gemini-1.5-flash'
    if 'models/gemini-1.5-flash' in available_models:
        model_name = 'gemini-1.5-flash'
    else:
        model_name = available_models[0].replace('models/', '')

    model = genai.GenerativeModel(model_name)

    st.markdown("### 🧬 Konsep Infografis")
    topik = st.text_input("Topik atau Materi yang Ingin Dibuat Infografisnya:", placeholder="Contoh: Anatomi Tokek, Daur Hidup Kupu-Kupu, Strategi Perang, dll.")

    if st.button("Generate Master Prompt ⚡"):
        if topik:
            with st.spinner('Merancang struktur infografis modular 8K...'):
                # INSTRUKSI DIOPTIMASI UNTUK KEDALAMAN DATA SETARA KOMPETITOR
                instruksi = f"""
                Act as a Professional Senior Visual Strategist and Prompt Engineer. 
                Generate a complex, high-resolution 3D Infographic Master Prompt in JSON for the topic: '{topik}'.
                
                The output JSON must be extremely deep and informative, forcing the AI to create:
                1. CONCEPT: A cross-section isometric 'Diorama Box' viewed from an angle.
                2. INFOGRAPHIC STRUCTURE: Include headline_section, main_visual_section, data_visualization_sections (min 3 segments), and impact_section.
                3. DATA DETAILS: Break down the topic into technical content_points, each with a title, description, and 3D icon_description.
                4. VISUAL STYLE: Photorealistic miniature photography, handcrafted detailed modeling, museum diorama aesthetic.
                5. BRANDING: Strictly place a high-contrast bold digital text watermark 'By {custom_wm}' at the BOTTOM CENTER. It must be completely separate from any 3D elements.
                
                JSON Template Structure (Output ONLY JSON):
                {{
                  "role": "professional_prompt_engineer",
                  "project_type": "editorial_3D_infographic_template",
                  "headline_section": {{
                    "headline_text": "JUDUL DALAM BAHASA INDONESIA (CAPSLOCK)",
                    "subheadline_text": "Penjelasan singkat dalam Bahasa Indonesia"
                  }},
                  "main_visual_section": {{
                    "visual_concept": "Detailed description of the 3D diorama box content",
                    "visual_style": ["photorealistic miniature", "museum style", "8K render"]
                  }},
                  "data_visualization_sections": [
                    {{
                      "section_title": "SEGMENTASI INFO 1",
                      "content_points": [{{ "title": "Point 1", "description": "Detail...", "icon_description": "3D icon of..." }}]
                    }}
                  ],
                  "branding_footer": {{
                    "text": "By {custom_wm}",
                    "position": "Bottom Center (Crucial)",
                    "style": "Clean bold high-contrast digital watermark"
                  }},
                  "design_details": {{ "render_quality": "8K", "texture": "detailed macro textures", "shadow": "dramatic museum lighting" }},
                  "negative_prompt": "cartoon, flat, messy layout, missing watermark, low resolution, blurry"
                }}
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.success(f"✅ **Master Prompt Berhasil Dibuat.**")
                st.markdown(f"> **Note:** Watermark **By {custom_wm}** terkunci di posisi Tengah Bawah untuk konsistensi.")
                st.balloons()
        else:
            st.warning("Silakan isi topik terlebih dahulu.")

except Exception as e:
    st.error(f"Sistem sedang sibuk. Error: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Advanced Prompt Engineering Solution")
