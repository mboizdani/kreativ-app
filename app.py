import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURASI BRANDING ---
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
        st.sidebar.error("❌ Password Salah!")
        st.stop()
else:
    st.title("🚀 Selamat Datang di Kreativ.ai")
    st.info("Masukkan password akses Anda di sidebar untuk memulai.")
    st.stop()

# --- 4. LOGIKA PAKET ---
is_pro = (user_pwd == PWD_PRO)
# Jika hemat, watermark dikosongkan. Jika pro, bisa diisi.
branding_text = "" 

st.title("🎨 Kreativ.ai Prompt Generator")

if is_pro:
    st.success("✅ Akses Aktif: Paket PRO (Custom Watermark)")
    branding_text = st.text_input("Masukkan Nama Brand/Watermark:", placeholder="Contoh: By RobiBarik")
else:
    st.success("✅ Akses Aktif: Paket HEMAT (Tanpa Watermark)")
    branding_text = "" # Kosong untuk paket hemat

# --- 5. KONFIGURASI API (PASTIKAN PAKAI KEY BARU) ---
API_KEY = "AIzaSyDz8Uped3q9oGoN442MOHdfcIcco8KKpWw" 

try:
    genai.configure(api_key=API_KEY)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel(available_models[0])

    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Reproduksi Hewan")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner('Sedang men-generate kode prompt...'):
                # INSTRUKSI SUPER KETAT: Hanya boleh JSON, tidak boleh mengobrol!
                instruksi = f"""
                You are a Professional Prompt Engineer. 
                Task: Generate a HIGH-DETAIL 3D Infographic JSON for the topic: '{topik}'.
                
                STRICT RULES:
                1. Return ONLY the raw JSON code. No conversational filler, no 'Sure', no 'Here is your code'.
                2. Use the following JSON structure exactly:
                {{
                  "role": "professional_prompt_engineer",
                  "project_type": "editorial_3D_infographic_template",
                  "output_settings": {{ "output_format": "high-resolution vertical infographic poster", "aspect_ratio": "2:3", "resolution": "8K", "language": "Indonesian" }},
                  "headline_section": {{ "headline_text": "JUDUL DALAM BAHASA INDONESIA", "headline_style": "3D EMBOSSED bold typography" }},
                  "data_sections": [ {{ "title": "Poin 1", "description": "Penjelasan detail" }}, "...sampai 5 poin" ],
                  "main_visual_section": {{ "visual_concept": "3D Isometric Diorama Box", "visual_description": "Hyper-realistic description of {topik} inside a box" }},
                  "design_details": {{ "branding": "Wajib sertakan teks '{branding_text}' di pojok bawah" }},
                  "negative_prompt": "flat, cartoon, lowres"
                }}
                3. Language for content: Indonesian. 
                4. Language for visual_description: English.
                """
                
                response = model.generate_content(instruksi)
                
                st.markdown("### 📊 Master Prompt JSON")
                # Membersihkan teks jika AI masih bandel kasih kata-kata pembuka
                clean_json = response.text.replace("```json", "").replace("```", "").strip()
                st.code(clean_json, language='json')
                
                st.info("✅ Salin semua kode di atas dan tempel langsung ke Gemini Nano Banana Pro.")
        else:
            st.warning("Isi topiknya dulu.")

except Exception as e:
    st.error(f"Terjadi kendala: {e}")

st.markdown("---")
st.caption("© 2026 Kreativ.ai | Lisensi Member Premium")
