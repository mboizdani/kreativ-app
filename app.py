import streamlit as st
import google.generativeai as genai

# --- CONFIGURASI BRANDING KREATIV.AI ---
st.set_page_config(page_title="Kreativ.ai - Prompt Builder Pro", page_icon="🚀")

# CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; }
    </style>
    """, unsafe_url_code=True)

st.title("🎨 Kreativ.ai Prompt Generator")
st.write("Generate prompt infografis 3D kelas dunia hanya dalam hitungan detik.")

# API KEY (Sudah Terpasang)
API_KEY = "AIzaSyA9cbVtTFvvpc_AUUsGA1VNCKcoIffiUKc"

try:
    genai.configure(api_key=API_KEY)
    
    # Mencari model yang tersedia secara otomatis
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = available_models[0] if available_models else 'gemini-1.5-flash'
    model = genai.GenerativeModel(model_name)

    # --- INPUT USER ---
    topik = st.text_input("Apa topik infografis Anda?", placeholder="Contoh: Anatomi Kucing, Cara Kerja Blockchain, dll")

    if st.button("Proses Sekarang ✨"):
        if topik:
            with st.spinner(f'Kreativ.ai sedang merancang arsitektur visual untuk {topik}...'):
                
                # --- LOGIKA SYSTEM PROMPT (TIRU KOMPETITOR) ---
                # Menggunakan struktur JSON agar AI Gambar memberikan hasil presisi 
                instruksi_rahasia = f"""
                Anda adalah Professional Prompt Engineer untuk Kreativ.ai. 
                Tugas: Buat editorial 3D infographic template untuk topik: '{topik}'.

                FORMAT OUTPUT HARUS DALAM STRUKTUR JSON (TIDAK BOLEH ADA TEKS LAIN):
                {{
                  "role": "professional_prompt_engineer",
                  "project_type": "editorial_3D_infographic_template",
                  "output_settings": {{
                    "output_format": "high-resolution vertical infographic poster",
                    "aspect_ratio": "2:3",
                    "resolution": "8K",
                    "language": "Indonesian"
                  }},
                  "headline_section": {{
                    "headline_text": "JUDUL BESAR TOPIK DISINI",
                    "headline_style": "3D EMBOSSED bold typography with professional depth"
                  }},
                  "data_sections": "Riset materi mendalam 5 poin dalam Bahasa Indonesia",
                  "main_visual_section": {{
                    "visual_concept": "Hyper-realistic 3D Isometric Diorama Box",
                    "visual_description": "A stunning, intricate 3D illustration about {topik} inside a cutaway box. Featuring photorealistic textures, museum diorama style, and soft dimensional lighting."
                  }},
                  "design_details": {{
                    "render_quality": "ultra-detailed, 8K render, photorealistic textures",
                    "shadow": "realistic ambient occlusion",
                    "branding": "Wajib sertakan teks 'By Kreativ.ai' di pojok bawah gambar"
                  }},
                  "negative_prompt": "flat vector, low resolution, messy layout, text inside icons"
                }}
                """
                
                response = model.generate_content(instruksi_rahasia)
                
                # --- MENAMPILKAN HASIL ---
                st.markdown("### 📊 Hasil Arsitektur & Prompt Spektakuler")
                st.info("Salin seluruh kode JSON di bawah ini dan tempel ke Gemini Nano Banana (Mode Pro) atau ChatGPT.")
                st.code(response.text, language='json')
                
                st.success("TIPS: Pastikan Anda menggunakan mode 'Pro' atau 'Nano Banana Pro' untuk hasil gambar terbaik!")
        else:
            st.warning("Silakan masukkan topik infografis Anda terlebih dahulu.")

except Exception as e:
    st.error(f"Terjadi kendala teknis. Pastikan API Key Anda aktif. Error: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 Kreativ.ai | Solusi Digital Masa Depan | Powered by Gemini API")
