import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="4 years", layout="centered")

# CSS Styling buat nuansa hangat & lembut
st.markdown("""
    <style>
        .title-text {
            font-family: 'Comic Sans MS', cursive;
            font-size: 36px;
            color: #d29ecb;
            text-align: center;
        }
        .sub-text {
            font-family: 'Verdana';
            font-size: 16px;
            color: #444444;
            text-align: center;
        }
        .highlight {
            background-color: #fff3f8;
            padding: 10px;
            border-radius: 12px;
            border: 1px solid #f1cce2;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title-text">🌼 untukmu 1461 hari yang akan datang 🌼</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">still with you💗</div><br>', unsafe_allow_html=True)

# Section 1: Intro
st.markdown('<div class="highlight">', unsafe_allow_html=True)
st.markdown("### 🌸 ada apa yaa hari ini?")
st.markdown("""
hari ini, tepatnya tanggal 21 september 2025...
hari dimana kita sudah bersama selama 4 tahun, bukan waktu yang singkat buat kita...
teput tangann untukk kitaa berduaa karena sudah sejauh inii...
aku hanya ingin merayakan kecil kecilan dengan ini, tapi cintanya besar besaran.

""")
st.markdown('</div>', unsafe_allow_html=True)

# Foto slideshow
st.markdown("## 🌟 Beberapa Kenangan Kita 🌟")
foto_list = [
    ("first.jpg", "Ini waktu pertama kali kita foto bareng... awkward bangett yaa wkwk 💞"),
    ("sebelum.jpg", "inii poto terakhir kita sebelum hari ini"),
    ("masih kosong.png", "bisa kali foto yang sekarang disimpen disini, hehe")
]

if "index" not in st.session_state:
    st.session_state.index = 0

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Sebelumnya"):
        st.session_state.index = (st.session_state.index - 1) % len(foto_list)

with col3:
    if st.button("➡️ Selanjutnya"):
        st.session_state.index = (st.session_state.index + 1) % len(foto_list)

img_path, caption = foto_list[st.session_state.index]
image = Image.open(img_path)
col2.image(image, caption=caption, use_column_width=True)

# Honest Button
st.divider()
st.markdown("aku tau kenapa kamu suka sama aku, pasti karena aku ganteng kan? hehe")
if st.button("iyaa dong"):
    st.success("iyaa sihh pastii akuu udahh tau koo")
if st. button("ga"):
    st.success("ga salahh lagiii lahh emangg gantengg bangett 💖")

# Surat dari Afii
st.markdown("#### 📜 bisa kalii dibuka surat kecilnyaa:")
if st.button("💖 Buka Surat"):
    st.info("""
    🌷 Cantikk... makasii yaa. udahh mauu sama akuu selama 4 tahunn inii, ini bukan waktu yang sebentar
    sudah banyak maaf yangg diberikann masing2 dari kita sampai sekarang.
    
   akuu harapp kita bisa saling sayang, saling mengerti, saling memahami, saling bisa menurunkan ego masing2
   dan saling2 yang lainnyaa.

   maaf ya kaloo selama ini akuu banyakk salahh ke kamu, kamu ga se seneng itu sama akuu, akuu mintaa maaf yaa
   mungkin ga banyak yang mauu aku ungkapin disini karena lebih enak untuk mengungkapkan langsung.
    
    i love you for everything we ever done 🤍.
    """)

# Footer
st.divider()
st.caption("""
🪷 ilove us...

darimu 1460 hari yang lalu.

21 september 2025.🌸  
""")
