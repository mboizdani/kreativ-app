import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI BRANDING ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #ff3333; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PENGATURAN PASSWORD (GANTI DISINI) ---
PWD_HEMAT = "HEMAT2026"  # Berikan ini ke pembeli Paket 19rb
PWD_PRO = "PROCUAN2026" # Berikan ini ke pembeli Paket 49rb

# --- 3. CEK AKSES ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password", type="password")

if user_pwd not in [PWD_HEMAT, PWD_PRO]:
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Silakan masukkan password yang Anda dapatkan dari Lykn.id untuk mengaktifkan tools.")
    st.image("https://via.placeholder.com/800x400.png?text=Akses+Terkunci+-+Beli+di+Lykn.id", use_container_width=True)
    st.stop()

# --- 4. LOGIKA FITUR BERDASARKAN PASSWORD ---
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai" # Default untuk paket hemat

st.title("🎨 Kreativ.ai Prompt Generator Pro")
st.success(f"Akses Aktif: {'Paket PRO (Custom Watermark)' if is_pro else 'Paket HEMAT (Watermark Tetap)'}")

if is_pro:
    st.subheader("⚙️ Pengaturan Brand")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: NamaToko.id")
else:
    st.info("💡 Anda menggunakan Paket Hemat. Watermark dikunci pada: **Kreativ.ai**")

# --- 5. EKSEKUSI GENERATOR ---
API_KEY = "AIzaSyA9cbVtTFvvpc_AUUsGA1VNCKcoIffiUKc"

try:
    genai.configure(api_key=API_KEY)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = available_models[0] if available_models else 'gemini-1.5-flash'
    model = genai.GenerativeModel(model_name)

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Anatomi Tubuh Manusia")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang merancang visual...'):
                # Menggunakan Struktur JSON Mantap (Adopsi Kompetitor)
                instruksi = f"""
                Role: Professional Prompt Engineer for Kreativ.ai.
                Task: Create 3D infographic JSON for '{topik}'.
                Output Settings: 8K Resolution, Indonesian Language, Isometric Diorama Box style.
                Strict Visual Rule: The branding/watermark MUST be written as 'By {custom_wm}'.
                Return only JSON.
                """
                
                response = model.generate_content(instruksi)
                st.markdown("### 📊 Hasil Arsitektur & Prompt")
                st.code(response.text, language='json')
                st.info(f"Salin kode di atas ke Gemini Nano Banana. Watermark: By {custom_wm}")
        else:
            st.warning("Isi topiknya dulu ya.")

except Exception as e:
    st.error(f"Terjadi kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
