import streamlit as st
import google.generativeai as genai
import json

# --- 1. SETUP VISUAL ---
st.set_page_config(page_title="Prompt Generator Infografis Pro", page_icon="💎", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #080808; color: #fff; }
    .stButton>button { 
        width: 100%; border-radius: 8px; height: 3.5em; 
        background: linear-gradient(90deg, #FF512F 0%, #DD2476 100%); 
        color: #fff; border: none; font-weight: 800; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. AKSES KEAMANAN ---
PWD_PRO = "PROCUAN2026"
user_pwd = st.sidebar.text_input("Access Key", type="password")
if user_pwd != PWD_PRO:
    st.info("🔒 Masukkan Access Key Premium")
    st.stop()

# --- 3. HARD-CODED TEMPLATE (BAGIAN INI 100% MIRIP KOMPETITOR) ---
# Kita tidak minta AI bikin ini. Kita tempel paksa biar kualitasnya terkunci.
def get_template_structure(topik, style):
    return f"""
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
        "headline_text": "JUDUL TOPIK (CAPS): SUB-JUDUL MENARIK",
        "headline_style": {{
          "font": "3D EMBOSSED bold typography with relatable style to topic",
          "font_weight": "extra bold",
          "color": "#HEX",
          "alignment": "center",
          "position": "top"
        }},
        "subheadline_text": "Penjelasan singkat yang memikat tentang {topik}.",
        "subheadline_style": {{ "font": "3D EMBOS modern clean sans-serif", "color": "#HEX" }}
      }},
      "main_visual_section": {{
        "visual_concept": "The {topik} Diorama Concept",
        "visual_description": "ENGLISH DESCRIPTION: A comprehensive, dynamic isometric view of {topik}. The scene shows [DETAIL 1], [DETAIL 2], and [DETAIL 3]. Glowing translucent arrows clearly indicate the flow or process. The scene is well-lit, emphasizing textures, refractions, and volumetric elements.",
        "visual_style": [
          "ultra-realistic 3D",
          "cinematic editorial illustration",
          "educational scientific visualization",
          "magical environmental storytelling"
        ],
        "camera": {{
          "angle": "isometric floating perspective covering a large systemic cross-section",
          "depth_of_field": "high, focusing on the entire interconnected loop/system",
          "lighting": "bright, radiant studio lighting enhancing textures"
        }}
      }},
      "data_visualization_sections": [
        {{
          "section_title": "BAGIAN 1 (KOMPONEN UTAMA)",
          "section_purpose": "Menjelaskan komponen utama.",
          "visual_style_rule": "Icon must visually represent the exact object being explained. No abstract icons.",
          "visual_type": "icon-based 3D explanation",
          "content_points": [
            {{ "title": "Poin 1", "description": "Penjelasan...", "icon_description": "3D icon accurately shaped like [Object]..." }}
          ]
        }}
      ],
      "impact_section": {{
        "section_title": "FAKTA & DAMPAK",
        "layout": "three-column visual cards",
        "impacts": [
          {{ "impact_title": "Judul", "visual_description": "A miniature 3D scene of...", "impact_text": "Teks dampak..." }}
        ]
      }},
      "design_details": {{
        "render_quality": "ultra-detailed, 8K render, photorealistic textures",
        "texture": "shimmering surfaces, volumetric mist, translucent layers, highly detailed textures",
        "shadow": "soft ambient occlusion with realistic caustics",
        "depth": "layered composition with floating data particles"
      }},
      "strict_visual_policy": {{
        "visible_text_policy": "design_text_only",
        "forbidden_text": ["hex color codes", "rgb values", "icon references", "debug labels"],
        "violation_handling": "remove all forbidden text from visual output"
      }}
    }}
    """

# --- 4. DASHBOARD ---
st.title("💎 Prompt Generator Infografis Pro")
st.caption("Mode: Strict Template Filling (Kompetitor Clone)")

col1, col2 = st.columns(2)
with col1:
    style_visual = st.selectbox("🎨 Gaya Visual:", ["DIORAMA (Wajib)", "ISOMETRIC", "PAPERCUT"])
with col2:
    branding_name = st.text_input("Brand/Watermark:", value="Kreativ.ai")

topik = st.text_area("Topik Materi:", placeholder="Contoh: Daur Hidup Kupu-Kupu...")

# --- CORE ENGINE ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    target_model = next((m for m in models if "1.5-pro" in m), next((m for m in models if "1.5-flash" in m), models[0]))

    if st.button("GENERATE PROMPT 🚀"):
        if topik:
            with st.spinner('Mengisi template editorial...'):
                # KITA MINTA AI HANYA MENGISI BAGIAN KOSONG DARI TEMPLATE DI ATAS
                template_str = get_template_structure(topik, style_visual)
                
                instruksi = f"""
                Act as a World-Class Prompt Engineer.
                
                TASK: Fill in the content for the JSON Template below based on the topic: '{topik}'.
                
                RULES:
                1. KEEP the exact structure, keys, and fixed values (like 'visual_style', 'camera', 'design_details') EXACTLY as provided in the template. DO NOT CHANGE THEM.
                2. Only generate new content for: 'headline_text', 'subheadline_text', 'visual_description', 'data_visualization_sections', and 'impact_section'.
                3. Content Language: Indonesian.
                4. Visual Description Language: English (High-end, cinematic vocabulary).
                5. Watermark: 'By {branding_name}'.
                
                TEMPLATE TO FILL:
                {template_str}
                
                OUTPUT: COMPLETE FILLED JSON ONLY.
                """
                
                model = genai.GenerativeModel(target_model)
                response = model.generate_content(instruksi)
                
                st.markdown("### ✅ Hasil Prompt (Fixed Structure)")
                st.code(response.text.replace("```json", "").replace("```", "").strip(), language='json')
                st.success("Bagian style & teknis visual sekarang 100% sama dengan kompetitor.")
        else:
            st.warning("Isi topiknya dulu bosku.")

except Exception as e:
    st.error(f"Error Teknis: {e}")
