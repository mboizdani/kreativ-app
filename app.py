import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI BRANDING ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PENGATURAN PASSWORD ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

# --- 3. SISTEM LOGIN SIDEBAR ---
st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password", type="password")

# Logika Pesan Error jika Password Salah
if user_pwd: # Jika user sudah mengetik sesuatu
    if user_pwd not in [PWD_HEMAT, PWD_PRO]:
        st.sidebar.error("❌ Password Salah! Silakan cek kembali email dari Lykn.id.")
        st.title("🚀 Akses Terkunci")
        st.warning("Maaf, password yang Anda masukkan tidak terdaftar.")
        st.stop()
else: # Jika kolom password masih kosong
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Silakan masukkan password akses Anda di menu samping (sidebar) untuk memulai.")
    st.stop()

# --- 4. LOGIKA PAKET (Hanya jalan jika password benar) ---
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

st.title("🎨 Kreativ.ai Prompt Generator")
st.success(f"Akses Aktif: {'Paket PRO (Custom Watermark)' if is_pro else 'Paket HEMAT (Watermark Tetap)'}")

if is_pro:
    st.subheader("⚙️ Pengaturan Brand (Versi Pro)")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: NamaToko.id")
else:
    st.info("💡 Anda menggunakan Paket Hemat. Watermark tetap: **Kreativ.ai**")

# --- 5. KONFIGURASI API (GANTI DENGAN KEY BARU) ---
API_KEY = "AIzaSyDz8Uped3q9oGoN442MOHdfcIcco8KKpWw" 

try:
    genai.configure(api_key=API_KEY)
    
    # Deteksi model otomatis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    if available_models:
        model = genai.GenerativeModel(available_models[0])
    else:
        st.error("Model AI tidak ditemukan. Pastikan API Key Anda benar.")
        st.stop()

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Anatomi Tubuh Manusia")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang merancang visual...'):
                instruksi = f"""
                Tugas: Buat riset mendalam dan prompt gambar untuk topik: '{topik}'.
                
                1. Sajikan riset materi dalam Bahasa Indonesia (Judul menarik & 5 Poin materi utama).
                2. Buatkan satu 'Master Prompt' dalam Bahasa Inggris untuk membuat gambar infografis.
                
                Aturan Master Prompt Gambar:
                - Konsep: Hyper-realistic 3D Isometric Diorama Box.
                - Detail: Photorealistic textures, museum lighting, 8K render.
                - Branding: Wajib tertulis secara jelas 'By {custom_wm}' di pojok bawah gambar.
                
                Sajikan Master Prompt tersebut di dalam kotak kode (code block) agar mudah disalin.
                """
                
                response = model.generate_content(instruksi)
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.write(response.text)
                
                st.info("✅ Langkah Selanjutnya: Salin Master Prompt di atas ke Gemini (Mode Nano Banana/Pro).")
        else:
            st.warning("Isi topiknya dulu ya.")

except Exception as e:
    st.error(f"Terjadi kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
