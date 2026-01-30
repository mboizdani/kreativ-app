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

# --- 2. AKSES KEAMANAN ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. LOGIN SYSTEM ---
st.sidebar.markdown("### 🏛️ Member Portal")
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Masukkan kunci akses...")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
branding_name = "Kreativ.ai"

# --- 4. DASHBOARD UTAMA ---
st.title("🚀 Prompt Generator Infografis Pro")
st.markdown("#### *Ubah Ide Menjadi Infografis 3D Mewah Kualitas 8K*")
st.markdown("---")

if not is_member:
    if user_pwd: st.sidebar.error("❌ Key Salah!")
    st.info("🔓 **Sistem Terkunci.** Silakan masukkan *Access Key* di samping untuk mulai.")
    st.stop()

# --- 5. PANEL KONTROL ---
if is_pro:
    st.success("💎 **Akses Premium Aktif**")
    branding_name = st.text_input("Ganti Watermark Brand Anda:", value="Kreativ.ai")
else:
    st.success("🌟 **Akses Standar Aktif**")

# --- 6. CORE ENGINE (AUTOMATIC MODEL FINDER) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # MENCARI MODEL TERSEDIA (ANTI-404) & MENGUNCI 1.5 FLASH (ANTI-429)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    # Mencari model 1.5-flash (jatah 1.500/hari) dan abaikan versi 2.5 (limit 20)
    target_model = next((m for m in available_models if "1.5-flash" in m and "2.5" not in m), None)
    
    if not target_model:
        target_model = "models/gemini-1.5-flash" # Fallback manual
    
    model = genai.GenerativeModel(target_model)

    topik = st.text_input("Topik Infografis:", placeholder="Contoh: Anatomi Tokek, Daur Hidup Katak, dll.")

    if st.button("Generate Master Prompt Sekarang ⚡"):
        if topik:
            with st.spinner('Merancang struktur infografis 8K...'):
                instruksi = f"""
                Act as a Professional Senior Visual Strategist. Generate an intricate 3D Infographic Master Prompt in JSON for: '{topik}'.
                STRICT DESIGN RULES:
                1. CONCEPT: Isometric 'Diorama Box' with extreme depth.
                2. INFOGRAPHIC: Include headline, subheadline, and 3-4 technical data segments in Indonesian.
                3. QUALITY: 8K resolution, photorealistic macro textures, museum diorama style.
                4. ASPECT RATIO: Strictly "2:3" (Vertical).
                5. WATERMARK: Clear text 'By {branding_name}' at the BOTTOM CENTER.
                
                OUTPUT ONLY JSON CODE.
                """
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                # --- 7. PANDUAN SIMPEL ---
                st.markdown("---")
                st.markdown("### ✅ Cara Pakai (Sangat Mudah):")
                st.markdown(f"""
                1. **Salin Kode:** Klik ikon salin pada kotak hitam di atas.
                2. **Buka AI Gambar:** Gunakan **ChatGPT** (Sangat Disarankan) atau Gemini.
                3. **Tempel & Kirim:** Masukkan kode tadi ke chat AI dan tekan Enter.
                
                *Note: Untuk hasil tulisan paling rapi dan detail mewah, gunakan **ChatGPT**.*
                """)
                st.balloons()
        else:
            st.warning("Isi topik dulu ya.")

except Exception as e:
    if "429" in str(e):
        st.error("⚠️ Batas harian model terbaru tercapai. Namun sistem sudah kami alihkan. Silakan KLIK LAGI tombol Generate di atas.")
    else:
        st.error(f"Kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Infografis Pro 8K")
