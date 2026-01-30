import streamlit as st
import google.generativeai as genai

# --- 1. BRANDING PRODUK ---
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
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Kunci akses...")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
is_pro = (user_pwd == PWD_PRO)
branding_name = "Kreativ.ai"

# --- 4. DASHBOARD UTAMA ---
st.title("🚀 Prompt Generator Infografis Pro")
st.markdown("#### *Ubah Ide Menjadi Infografis 3D Mewah Kualitas 8K*")
st.markdown("---")

if not is_member:
    if user_pwd: st.sidebar.error("❌ Key Salah!")
    st.info("🔓 **Sistem Terkunci.** Masukkan *Access Key* di samping untuk mulai.")
    st.stop()

# --- 5. PANEL KONTROL ---
if is_pro:
    st.success("💎 **Akses Premium Aktif**")
    branding_name = st.text_input("Ganti Watermark Brand Anda:", value="Kreativ.ai")
else:
    st.success("🌟 **Akses Standar Aktif**")

# --- 6. CORE ENGINE (TRI-MODEL FALLBACK SYSTEM) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    topik = st.text_input("Topik Infografis:", placeholder="Contoh: Anatomi Tokek, Daur Hidup Katak, dll.")

    if st.button("Generate Master Prompt Sekarang ⚡"):
        if topik:
            with st.spinner('Merancang struktur infografis 8K...'):
                instruksi = f"""
                Act as a Professional Senior Visual Strategist. Generate an intricate 3D Infographic Master Prompt in JSON for: '{topik}'.
                1. CONCEPT: Isometric 'Diorama Box' with extreme depth.
                2. INFOGRAPHIC: Include headline, subheadline, and 3-4 data segments in Indonesian.
                3. QUALITY: 8K, macro textures, museum diorama style.
                4. ASPECT RATIO: Strictly "2:3".
                5. WATERMARK: Text 'By {branding_name}' at the BOTTOM CENTER.
                RETURN ONLY JSON CODE.
                """
                
                # --- SISTEM COBA 3 KALI (ANTI-404) ---
                response = None
                model_names = ['gemini-1.5-flash', 'models/gemini-1.5-flash', 'gemini-1.5-pro']
                
                for m_name in model_names:
                    try:
                        model = genai.GenerativeModel(m_name)
                        response = model.generate_content(instruksi)
                        if response: break 
                    except:
                        continue
                
                if response:
                    st.markdown("### 📊 Master Prompt JSON")
                    clean_json = response.text.replace("```json", "").replace("```", "").strip()
                    st.code(clean_json, language='json')
                    
                    st.markdown("---")
                    st.markdown("### ✅ Cara Pakai (Sangat Mudah):")
                    st.markdown(f"""
                    1. **Salin Kode:** Klik ikon salin pada kotak hitam di atas.
                    2. **Buka AI Gambar:** Gunakan **ChatGPT** (Paling Bagus) atau Gemini.
                    3. **Tempel & Kirim:** Masukkan kode tadi ke chat AI dan tekan Enter.
                    """)
                    st.balloons()
                else:
                    st.error("⚠️ Semua model sedang sibuk. Mohon tunggu 30 detik lalu klik tombol lagi.")
        else:
            st.warning("Isi topik dulu ya.")

except Exception as e:
    st.error(f"Kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Infografis Pro 8K")
