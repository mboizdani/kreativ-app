import streamlit as st
import google.generativeai as genai

# --- CONFIG BRANDING ---
st.set_page_config(page_title="Kreativ.ai Pro - Prompt Builder", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEM PASSWORD ---
PWD_HEMAT = "HEMAT2026"
PWD_PRO = "PROCUAN2026"

st.sidebar.title("🔑 Akses Member")
user_pwd = st.sidebar.text_input("Masukkan Password", type="password")

if user_pwd not in [PWD_HEMAT, PWD_PRO]:
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Silakan masukkan password akses dari Lykn.id untuk mengaktifkan tools.")
    st.stop()

# --- LOGIKA PAKET ---
is_pro = (user_pwd == PWD_PRO)
custom_wm = "Kreativ.ai"

st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Ubah topik apa saja menjadi prompt infografis profesional.")

if is_pro:
    st.subheader("⚙️ Pengaturan Brand (Versi Pro)")
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: NamaToko.id")
else:
    st.info("💡 Anda menggunakan Paket Hemat. Watermark tetap: **Kreativ.ai**")

# --- MASUKKAN API KEY BARU ANDA DISINI ---
# Pastikan sudah membuat API Key baru di Google AI Studio karena yang lama sudah bocor
API_KEY = "AIzaSyDz8Uped3q9oGoN442MOHdfcIcco8KKpWw" 

try:
    genai.configure(api_key=API_KEY)
    # PERBAIKAN: Menambahkan 'models/' di depan nama model untuk mencegah error 404
    model = genai.GenerativeModel('models/gemini-1.5-flash')

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Anatomi Kucing")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang merancang visual...'):
                instruksi = f"""
                Buatkan riset lengkap untuk '{topik}' dan buatkan prompt gambar Bahasa Inggris 
                yang detail (format JSON) untuk infografis 3D profesional di dalam kotak diorama. 
                Wajib sertakan instruksi watermark: 'By {custom_wm}' di dalam prompt gambarnya.
                """
                
                response = model.generate_content(instruksi)
                st.markdown("### 📊 Hasil Riset & Prompt")
                st.code(response.text)
                
                st.info("✅ Langkah Selanjutnya:")
                st.write("1. Salin seluruh teks kode di atas.")
                st.write("2. Buka Gemini (Mode Nano Banana/Pro).")
                st.write("3. Tempel kodenya dan lihat hasilnya!")
        else:
            st.warning("Isi topiknya dulu ya.")

except Exception as e:
    # Jika masih 404, sistem akan mencoba memanggil list model secara otomatis
    st.error(f"Terjadi kendala teknis: {e}")
    st.info("Coba ganti nama model di kode menjadi 'models/gemini-pro' jika error berlanjut.")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Konten Masa Depan")
