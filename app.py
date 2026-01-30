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

st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password", type="password")

if user_pwd not in [PWD_HEMAT, PWD_PRO]:
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Silakan masukkan password akses dari Lykn.id untuk mengaktifkan tools.")
    st.stop()

# --- 3. LOGIKA PAKET ---
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi riset materi dan prompt gambar profesional.")

if is_pro:
    st.subheader("⚙️ Pengaturan Brand (Versi Pro)")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: NamaToko.id")
else:
    st.info("💡 Anda menggunakan Paket Hemat. Watermark tetap: **Kreativ.ai**")

# --- 4. KONFIGURASI API (GANTI DENGAN KEY BARU) ---
# Gunakan API Key baru yang Anda buat di Google AI Studio
API_KEY = "AIzaSyDz8Uped3q9oGoN442MOHdfcIcco8KKpWw" 

try:
    genai.configure(api_key=API_KEY)
    
    # Deteksi model otomatis untuk mencegah error 404
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
                # Perbaikan instruksi agar tidak menyebabkan SyntaxError
                instruksi = f"""
                Tugas: Buat riset mendalam dan prompt gambar untuk topik: '{topik}'.
                
                1. Sajikan riset materi dalam Bahasa Indonesia (Judul menarik & 5 Poin materi utama).
                2. Buatkan satu 'Master Prompt' dalam Bahasa Inggris untuk membuat gambar infografis.
                
                Aturan Master Prompt Gambar:
                - Konsep: Hyper-realistic 3D Isometric Diorama Box.
                - Detail: Photorealistic textures, museum lighting, 8K render resolution.
                - Branding: Wajib tertulis secara jelas 'By {custom_wm}' di pojok bawah gambar.
                
                Sajikan Master Prompt tersebut di dalam kotak kode (code block) agar mudah disalin.
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.write(response.text)
                
                st.info("✅ Langkah Selanjutnya:")
                st.write("1. Salin 'Master Prompt' (teks bahasa Inggris) di atas.")
                st.write("2. Buka Gemini (Mode Nano Banana/Pro).")
                st.write("3. Tempel kodenya dan lihat hasilnya!")
        else:
            st.warning("Isi topiknya dulu ya.")

except Exception as e:
    st.error(f"Terjadi kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
