import streamlit as st
import google.generativeai as genai

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

# --- 3. GOLDEN SAMPLE (RAHASIA KOMPETITOR: SAMBAL MATAH) ---
# Ini adalah "DNA" yang kita curi. AI akan dipaksa meniru struktur ini.
GOLDEN_SAMPLE = """
{
  "project_type": "editorial_3D_infographic_template",
  "output_settings": { "aspect_ratio": "2:3", "resolution": "8K", "language": "Indonesian" },
  "headline_section": {
    "headline_text": "JUDUL TOPIK (CAPS): SUB-JUDUL MENARIK",
    "headline_style": { "font": "3D EMBOSSED bold typography", "color": "#HEX", "position": "top" },
    "subheadline_text": "Penjelasan singkat yang memikat."
  },
  "main_visual_section": {
    "visual_concept": "Nama Konsep Visual",
    "visual_description": "ENGLISH: An intricate isometric 3D diorama of... [Describe the main scene in extreme detail, mentioning textures, lighting, and composition]. The scene is well-lit, emphasizing vibrant colors.",
    "visual_style": ["ultra-realistic 3D", "cinematic editorial", "educational"],
    "camera": { "angle": "isometric floating perspective", "depth_of_field": "high" }
  },
  "data_visualization_sections": [
    {
      "section_title": "JUDUL BAGIAN 1 (KOMPONEN/BAHAN)",
      "visual_style_rule": "Icon must visually represent the exact object being explained. No abstract icons.",
      "visual_type": "icon-based 3D explanation",
      "content_points": [
        { 
          "title": "Nama Poin", 
          "description": "INDONESIA: Penjelasan detail...", 
          "icon_description": "ENGLISH: A photorealistic 3D icon of [Object], rendered in [Material], matching real-world form." 
        }
      ]
    },
    {
      "section_title": "JUDUL BAGIAN 2 (PROSES/LANGKAH)",
      "visual_style_rule": "Use visual highlighting only if topic involves movement.",
      "visual_type": "3D process highlight",
      "content_points": [
        { "process_name": "Langkah 1", "process_description": "INDONESIA: Penjelasan langkah..." }
      ]
    }
  ],
  "impact_section": {
    "section_title": "FAKTA & DAMPAK",
    "layout": "three-column visual cards",
    "impacts": [
      { 
        "impact_title": "Judul Dampak", 
        "visual_description": "ENGLISH: A miniature 3D scene of...", 
        "impact_text": "INDONESIA: Penjelasan dampak..." 
      }
    ]
  },
  "design_details": {
    "render_quality": "ultra-detailed, 8K render",
    "texture": "ENGLISH: [List specific textures: wood, glass, resin, metal, etc.]",
    "shadow": "soft ambient occlusion with subtle directional light",
    "depth": "layered composition with clear foreground and background"
  },
  "strict_visual_policy": {
    "forbidden_text": ["hex color codes", "rgb values", "icon references", "debug labels"]
  }
}
"""

# --- 4. DASHBOARD & ENGINE ---
st.title("💎 Prompt Generator Infografis Pro")
st.caption("Engine: Gemini 1.5 Pro (Structure Cloning Mode)")

col1, col2 = st.columns(2)
with col1:
    style_visual = st.selectbox("🎨 Gaya Visual:", ["DIORAMA", "ISOMETRIC", "PAPERCUT", "CLAYMORPHIC", "HYPER-REALISTIC"])
with col2:
    branding_name = st.text_input("Brand/Watermark:", value="Kreativ.ai")

topik = st.text_area("Topik Materi:", placeholder="Contoh: Daur Hidup Kupu-Kupu, Cara Kerja Mesin Diesel, Resep Nasi Goreng...")

# --- CORE LOGIC ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Auto-detect (Cari Pro dulu, baru Flash)
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    target_model = next((m for m in models if "1.5-pro" in m), next((m for m in models if "1.5-flash" in m), models[0]))

    if st.button("GENERATE PROMPT 🚀"):
        if topik:
            with st.spinner('Sedang menduplikasi struktur kompetitor...'):
                # PROMPT SAKTI: ONE-SHOT CLONING
                instruksi = f"""
                Act as a World-Class Prompt Engineer.
                
                OBJECTIVE: Create a high-end JSON Prompt for the topic: '{topik}'.
                STYLE: {style_visual}.
                
                REFERENCE: Use the provided "GOLDEN SAMPLE" JSON below as the strict template.
                
                INSTRUCTIONS:
                1. STRUCTURE: You MUST follow the exact keys and nesting of the GOLDEN SAMPLE.
                2. LANGUAGE: Content MUST be Indonesian. Visual Descriptions MUST be English.
                3. DEPTH: Mimic the richness of the descriptions (e.g., mention textures, lighting, materials).
                4. LOGIC: Apply the rule "Icon must visually represent the exact object".
                5. BRANDING: Watermark 'By {branding_name}' at Bottom Center.
                
                GOLDEN SAMPLE (DO NOT COPY CONTENT, ONLY STRUCTURE):
                {GOLDEN_SAMPLE}
                
                OUTPUT: JSON ONLY for '{topik}'.
                """
                
                model = genai.GenerativeModel(target_model)
                response = model.generate_content(instruksi)
                
                st.markdown("### ✅ Hasil Prompt (Kualitas Kompetitor)")
                st.code(response.text.replace("```json", "").replace("```", "").strip(), language='json')
                st.success("Selesai! Struktur ini 100% mengikuti logika 'Tools 2' kompetitor.")
        else:
            st.warning("Isi topiknya dulu bosku.")

except Exception as e:
    st.error(f"Error Teknis: {e}")
    
