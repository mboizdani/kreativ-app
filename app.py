import streamlit as st
import google.generativeai as genai

# --- 1. BRANDING & UI ---
st.set_page_config(page_title="Prompt Generator Infografis Pro", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #FF4B4B, #FF8C00); 
        color: white; border: none; font-weight: bold; font-size: 18px;
    }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. AKSES KEAMANAN ---
PWD_PRO = "PROCUAN2026"
user_pwd = st.sidebar.text_input("Access Key", type="password")

if user_pwd != PWD_PRO:
    if user_pwd: st.sidebar.error("❌ Key Salah")
    st.info("🔓 Masukkan Access Key Premium")
    st.stop()

# --- 3. DASHBOARD ---
st.title("🚀 Prompt Generator Infografis Pro")
st.markdown("#### *The Ultimate Editorial 3D Engine (Competitor Level)*")

# --- 4. INPUT ---
col1, col2 = st.columns(2)
with col1:
    style_visual = st.selectbox("🎨 Gaya Visual:", ["DIORAMA (Best)", "ISOMETRIC", "PAPERCUT", "CLAYMORPHIC", "HYPER-REALISTIC"])
with col2:
    branding_name = st.text_input("Brand/Watermark:", value="Kreativ.ai")

topik = st.text_area("Topik Materi:", placeholder="Contoh: Daur Hidup Kupu-Kupu, Tata Surya, Struktur Jantung...")

# --- 5. CORE ENGINE (CLONING STRUKTUR KOMPETITOR) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Auto-Scanner Model (Anti-404)
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    target_model = next((m for m in models if "1.5-flash" in m), models[0])

    if st.button("Generate Master Prompt ⚡"):
        if topik:
            with st.spinner('Menerapkan logika visual tingkat tinggi...'):
                # INI KUNCINYA: TEMPLATE JSON PERSIS PUNYA KOMPETITOR
                instruksi = f"""
                Act as a Professional Prompt Engineer. Generate a JSON output for: '{topik}' using style '{style_visual}'.
                
                YOU MUST FOLLOW THIS EXACT JSON STRUCTURE (Do not change keys):
                
                {{
                  "role": "professional_prompt_engineer",
                  "project_type": "editorial_3D_infographic_template",
                  "reusable": true,
                  "output_settings": {{
                    "output_format": "high-resolution vertical infographic poster",
                    "aspect_ratio": "2:3",
                    "resolution": "8K",
                    "language": "Indonesian"
                  }},
                  "headline_section": {{
                    "headline_text": "JUDUL KAPITAL",
                    "headline_style": {{ "font": "3D EMBOSSED bold typography", "color": "HEX", "position": "top" }},
                    "subheadline_text": "Penjelasan singkat",
                    "subheadline_style": {{ "font": "Modern clean sans-serif", "color": "HEX" }}
                  }},
                  "main_visual_section": {{
                    "visual_concept": "Nama Konsep Visual",
                    "visual_description": "Deskripsi sangat detail tentang scene utama diorama 3D...",
                    "visual_style": ["ultra-realistic 3D", "cinematic editorial", "educational"],
                    "camera": {{ "angle": "isometric floating perspective", "depth_of_field": "high" }}
                  }},
                  "color_palette": {{ "primary": "HEX", "secondary": "HEX", "accent": "HEX", "background": "HEX" }},
                  "data_visualization_sections": [
                    {{
                      "section_title": "JUDUL BAGIAN 1",
                      "section_purpose": "Tujuan bagian ini",
                      "visual_style_rule": "Icon must visually represent the exact object being explained. No abstract icons.",
                      "visual_type": "icon-based 3D explanation",
                      "content_points": [
                        {{ "title": "Poin 1", "description": "Isi", "icon_description": "3D icon description..." }},
                        {{ "title": "Poin 2", "description": "Isi", "icon_description": "3D icon description..." }}
                      ]
                    }},
                    {{
                      "section_title": "JUDUL BAGIAN 2 (PROSES)",
                      "section_purpose": "Menjelaskan proses",
                      "visual_style_rule": "Use visual highlighting only if topic involves movement. Flow arrows appear ONLY when real process exists.",
                      "visual_type": "3D process highlight",
                      "map_region": "Lokasi di visual utama",
                      "content_points": [
                         {{ "process_name": "Nama Proses", "process_description": "Deskripsi" }}
                      ]
                    }}
                  ],
                  "impact_section": {{
                    "section_title": "FAKTA & DAMPAK",
                    "layout": "three-column visual cards",
                    "impacts": [
                      {{ "impact_title": "Judul", "visual_description": "Miniature 3D scene...", "impact_text": "Isi teks" }}
                    ]
                  }},
                  "design_details": {{
                    "render_quality": "ultra-detailed, 8K render",
                    "texture": "detail tekstur material...",
                    "shadow": "soft ambient occlusion",
                    "depth": "layered composition"
                  }},
                  "background_design": {{ "background_type": "Soft gradient...", "decorative_elements": "subtle patterns..." }},
                  "branding_footer": {{
                    "credit_text": "Sumber Data | Infografis 2026",
                    "disclaimer": "Visualisasi artistik edukasi"
                  }},
                  "ai_model_recommendation": ["Midjourney v6", "DALL-E 3"],
                  "negative_prompt": ["cartoon", "flat", "low res", "blurry", "bad anatomy", "text glitch", "hex codes"],
                  "strict_visual_policy": {{
                    "visible_text_policy": "design_text_only",
                    "forbidden_text": ["hex color codes", "rgb values", "icon references"],
                    "violation_handling": "remove all forbidden text from visual output"
                  }}
                }}
                
                IMPORTANT:
                - Use Indonesian for all Content text.
                - Use English for all Visual Descriptions.
                - Watermark text: 'By {branding_name}'.
                - Ensure the 'visual_style_rule' logic is applied exactly like the example structure.
                """
                
                model = genai.GenerativeModel(target_model)
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Master Prompt (Struktur Kompetitor)")
                st.code(response.text.replace("```json", "").replace("```", "").strip(), language='json')
                
                st.markdown("---")
                st.markdown("### ✅ Cara Pakai:")
                st.markdown("1. Salin kode di atas.\n2. Tempel ke **ChatGPT**.\n3. Hasilnya akan **sama persis** strukturnya dengan tools kompetitor.")
                st.balloons()
        else:
            st.warning("Isi topik dulu ya.")
except Exception as e:
    st.error(f"Sistem sedang sinkronisasi: {e}")
