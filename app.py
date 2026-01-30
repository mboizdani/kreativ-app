import streamlit as st
import google.generativeai as genai

# --- 1. UI PREMIUM & BRANDING ---
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
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Masukkan kunci akses...")

if user_pwd != PWD_PRO:
    if user_pwd: st.sidebar.error("❌ Kunci Akses Salah!")
    st.info("🔓 Masukkan Access Key untuk mengaktifkan Mesin Visual 8K.")
    st.stop()

# --- 3. DASHBOARD UTAMA ---
st.title("🚀 Prompt Generator Infografis Pro")
st.markdown("#### *Professional Editorial 3D Infographic Engine - 8K Ultra-HD*")
st.markdown("---")

# --- 4. PANEL KONTROL (SUNTIKAN LOGIKA KOMPETITOR) ---
col1, col2 = st.columns(2)
with col1:
    style_visual = st.selectbox("🎨 Pilih Gaya Visual (Mode Estetik):", [
        "DIORAMA (Museum Exhibit Style)", "ISOMETRIC (Educational Editorial)", 
        "PAPERCUT (Intricate Layered)", "CLAYMORPHIC (3D Clay Art)",
        "HYPER-REALISTIC (Scientific Visualization)"
    ])
with col2:
    branding_name = st.text_input("Identity / Watermark Brand:", value="Kreativ.ai")

topik = st.text_area("Apa materi yang ingin dibuatkan infografisnya?", placeholder="Contoh: Anatomi Burung Hantu, Sistem Tata Surya, atau Cara Kerja Jantung...")

# --- 5. CORE ENGINE (PENGUNCIAN MODEL & LOGIKA KOMPETITOR) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Auto-detect model aktif (Flash 1.5 - Jatah 1.500/hari)
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    target_model = next((m for m in models if "1.5-flash" in m), models[0])
    
    if st.button("Generate Master Prompt ⚡"):
        if topik:
            with st.spinner(f'Merancang visual editorial gaya {style_visual}...'):
                # SUNTIKAN INSTRUKSI "RESEP RAHASIA" KOMPETITOR
                instruksi = f"""
                You are a Professional Senior Prompt Engineer specializing in editorial 3D infographic templates. 
                Generate an intricate JSON-based master prompt for: '{topik}'.
                
                STRICT VISUAL RULES (ATM LOGIC):
                1. STYLE: {style_visual}. Use Isometric perspective with extreme depth of field.
                2. STRUCTURE: Headline, Subheadline (Indonesian), Main 3D Diorama, 3 Data Sections with icons, and Impact Section.
                3. ICON LOGIC: Icons must be 3D models of the ACTUAL object (no abstract/vector icons).
                4. RENDER: 8K resolution, volumetric lighting, photorealistic textures (resin, wood, or glass).
                5. RATIO: Strictly 2:3.
                6. WATERMARK: 'By {branding_name}' at Bottom Center.
                
                NEGATIVE PROMPT: No cartoon, no 2D, no flat vector, no English text for labels.
                RETURN ONLY THE JSON BLOCK.
                """
                
                model = genai.GenerativeModel(target_model)
                response = model.generate_content(instruksi)
                
                st.markdown("### 💎 Hasil Master Prompt (Kualitas Editorial 8K)")
                st.code(response.text.replace("```json", "").replace("```", "").strip(), language='json')
                
                # --- 6. INSTRUKSI PENGGUNA SIMPEL ---
                st.markdown("---")
                st.markdown("### ✅ Cara Pakai (Sangat Mudah):")
                st.markdown(f"""
                1. **Klik Ikon Salin** pada kotak hitam di atas.
                2. Buka **ChatGPT** (Gratis/Pro) atau Gemini.
                3. **Tempel & Kirim.**
                
                *Note: ChatGPT lebih disarankan untuk penulisan teks yang lebih rapi.*
                """)
                st.balloons()
        else:
            st.warning("Silakan masukkan topik materi terlebih dahulu.")
except Exception as e:
    st.error(f"Sistem sedang sinkronisasi data: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Professional 8K Visual Solution")
