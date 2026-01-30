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

if user_pwd:
    if user_pwd not in [PWD_HEMAT, PWD_PRO]:
        st.sidebar.error("❌ Password Salah! Silakan cek kembali email dari Lykn.id.")
        st.stop()
else:
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Silakan masukkan password akses Anda di menu samping untuk memulai.")
    st.stop()

# --- 4. LOGIKA PAKET & WATERMARK ---
is_pro = (user_pwd == PWD_PRO)
# Default watermark untuk demo/pembeli hemat adalah Kreativ.ai
custom_wm = "Kreativ.ai"

st.title("🎨 Kreativ.ai Prompt Generator")

if is_pro:
    st.success("✅ Akses Aktif: Paket PRO (Custom Watermark)")
    # Placeholder diubah agar anonim (tidak menyebut nama pribadi)
    custom_wm = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: StudioVisual.ai")
else:
    st.success("✅ Akses Aktif: Paket HEMAT (Watermark Kreativ.ai)")
    st.info("💡 Watermark otomatis: **Kreativ.ai**")

# --- 5. KONFIGURASI API ---
# Gunakan API Key baru yang Anda buat di Google AI Studio
API_KEY = "AIzaSyDz8Uped3q9oGoN442MOHdfcIcco8KKpWw" 

try:
    genai.configure(api_key=API_KEY)
    
    # Deteksi model otomatis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    if available_models:
        model = genai.GenerativeModel(available_models[0])
    else:
        st.error("Model tidak ditemukan. Cek API Key Anda.")
        st.stop()

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Anatomi Tubuh Manusia")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Kreativ.ai sedang merancang visual super powerful...'):
                # INSTRUKSI VERSI POWERFUL (Struktur Lebih Detail & Teknis)
                instruksi = f"""
                You are a Professional Prompt Engineer. Generate a HIGH-DETAIL 3D Infographic JSON for the topic: '{topik}'.
                
                STRICT RULES:
                1. Return ONLY raw JSON code. No conversational text.
                2. Structure must include: infographic_title, infographic_description, output_settings (8K, Indonesian, Isometric Diorama Box, Studio Lighting), and 'branding'.
                3. Branding details: watermark_text must be 'By {custom_wm}', position: 'Bottom Right'.
                4. Diorama_box_properties: include dimensions_hint and material_hint (minimalistic, transparent layers).
                5. Content: Create 5-6 detailed sections/systems relevant to '{topik}' with visual_representation (color_palette, highlight_color) and 4 key_details each.
                6. Visual style must be hyper-realistic, museum-quality diorama.
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                # Pembersihan output agar siap tempel
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.info("✅ Langkah Selanjutnya:")
                st.write("1. Salin semua kode di atas.")
                st.write("2. Tempel ke AI pembuat gambar favorit Anda (Gemini Nano Banana Pro, ChatGPT Plus, atau DALL-E 3).")
                st.write(f"3. Hasil gambar akan otomatis memiliki watermark: **By {custom_wm}**")
        else:
            st.warning("Isi topiknya dulu ya.")

except Exception as e:
    st.error(f"Terjadi kendala teknis: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Lisensi Member Premium")
