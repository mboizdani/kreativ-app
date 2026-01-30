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
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. AKSES KEAMANAN ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. LOGIN SYSTEM ---
st.sidebar.markdown("### 🏛️ Member Portal")
user_pwd = st.sidebar.text_input("Access Key", type="password", placeholder="Kunci akses...")

is_member = user_pwd in [PWD_HEMAT, PWD_PRO]
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
if user_pwd == PWD_PRO:
    st.success("💎 **Akses Premium Aktif**")
    branding_name = st.text_input("Identity / Watermark Brand:", value="Kreativ.ai")
else:
    st.success("🌟 **Akses Standar Aktif**")

# --- 6. CORE ENGINE (SIMPLE STABLE MODE) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    topik = st.text_input("Materi apa yang ingin Anda buat?", placeholder="Contoh: Anatomi Tokek, Daur Hidup Katak, dll.")

    if st.button("Generate Master Prompt Sekarang ⚡"):
        if topik:
            with st.spinner('Merancang struktur infografis 8K...'):
                instruksi = f"Generate 3D Infographic Master Prompt JSON for: '{topik}'. Rule: 8K, Isometric, 2:3 ratio, Indonesian labels, Watermark 'By {branding_name}' at bottom center. Return ONLY JSON."
                
                # CARA PEMANGGILAN PALING STABIL
                try:
                    # Mencoba model paling ringan (Flash)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(instruksi)
                    
                    st.markdown("### 📊 Master Prompt JSON")
                    clean_json = response.text.replace("```json", "").replace("```", "").strip()
                    st.code(clean_json, language='json')
                    
                    st.markdown("---")
                    st.markdown("### ✅ Cara Pakai (Sangat Mudah):")
                    st.markdown("1. **Salin Kode** di atas.\n2. **Tempel ke ChatGPT** (Disarankan) atau Gemini.\n3. **Kirim** dan lihat hasilnya!")
                    st.balloons()
                except Exception as e_inner:
                    st.error(f"⚠️ Server Google sedang padat. Silakan klik tombol sekali lagi. ({e_inner})")
        else:
            st.warning("Isi topik dulu ya.")
except Exception as e:
    st.error(f"Kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Professional 8K Infographic Solution")
