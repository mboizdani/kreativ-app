import streamlit as st
import google.generativeai as genai

# --- 1. PREMIUM BRANDING ---
st.set_page_config(page_title="Prompt Generator Infografis Pro", page_icon="🎨", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4em; 
        background: linear-gradient(45deg, #FF4B4B, #FF8C00); 
        color: white; border: none; font-weight: bold; font-size: 20px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. AKSES MEMBER ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. LOGIN SYSTEM ---
st.sidebar.markdown("### 🏛️ Member Portal")
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Kunci akses...")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
branding_name = "Kreativ.ai"

# --- 4. DASHBOARD ---
st.title("🚀 Prompt Generator Infografis Pro")
st.markdown("#### *The Ultimate 8K High-Definition Infographic Engine*")
st.markdown("---")

if not is_member:
    if user_pwd: st.sidebar.error("❌ Key Salah!")
    st.info("🔓 **Sistem Terkunci.** Masukkan *Access Key* di sidebar untuk mulai.")
    st.stop()

# --- 5. MEMBER CONTROL ---
if is_pro:
    st.success("💎 **Akses Premium Aktif**")
    branding_name = st.text_input("Identity / Watermark Brand:", value="Kreativ.ai")
else:
    st.success("🌟 **Akses Standar Aktif**")

# --- 6. CORE ENGINE (SMART MODEL SELECTOR) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # MENCARI MODEL TERSEDIA SECARA DINAMIS (ANTI-404)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    # Prioritas 1: gemini-1.5-flash (Jatah 1.500/hari)
    # Prioritas 2: gemini-1.5-pro
    # Prioritas 3: Model apa pun yang tersedia
    selected_model = next((m for m in available_models if "1.5-flash" in m), 
                          next((m for m in available_models if "1.5-pro" in m), 
                          available_models[0]))
    
    model = genai.GenerativeModel(selected_model)

    topik = st.text_input("Materi apa yang ingin Anda buat?", placeholder="Contoh: Anatomi Tokek, Daur Hidup Katak, dll.")

    if st.button("Generate Master Prompt Sekarang ⚡"):
        if topik:
            with st.spinner('Merancang struktur infografis 8K...'):
                instruksi = f"""
                You are a Professional Senior Visual Strategist. Generate an intricate 3D Infographic Master Prompt in JSON for: '{topik}'.
                STRICT RULES:
                1. CONCEPT: Isometric 'Diorama Box' with extreme depth.
                2. INFOGRAPHIC: Include headline, subheadline, and 3-4 data segments in Indonesian.
                3. QUALITY: 8K, macro textures, photorealistic miniature style.
                4. ASPECT RATIO: Strictly "2:3".
                5. WATERMARK: Bold text 'By {branding_name}' at the BOTTOM CENTER.
                
                OUTPUT ONLY JSON.
                """
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                # --- 7. CARA PAKAI SIMPEL ---
                st.markdown("---")
                st.markdown("### ✅ Cara Pakai (Sangat Mudah):")
                st.markdown(f"""
                1. **Salin Kode:** Klik ikon salin di kotak hitam atas.
                2. **Buka AI Gambar:** Gunakan **ChatGPT** (Paling Bagus) atau Gemini.
                3. **Tempel & Kirim:** Masukkan kode ke chat AI Anda.
                
                *Note: Hasil terbaik (tulisan rapi & detail) ada di ChatGPT.*
                """)
                st.balloons()
        else:
            st.warning("Isi topik dulu ya.")

except Exception as e:
    st.error(f"Kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Professional 8K Infographic Solution")
