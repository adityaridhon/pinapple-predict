import streamlit as st
import base64

# Konfigurasi halaman
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    initial_sidebar_state="auto"
)

# Membaca gambar dan mengubahnya menjadi base64
def load_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

adit_url = load_image("images/adit.jpg")
arya_url = load_image("images/arya.jpg")
fatwa_url = load_image("images/fatwa.jpg")

# Konten halaman
st.write("# Hai, selamat datang👋")
st.write("Perkenalkan kami dari Institut Teknologi Kalimantan. Proyek ini berjudul **SISTEM PREDIKSI CUACA BERBASIS WEB DENGAN METODE RIDGE REGRESSION DAN RULE BASE PADA SISTEM PAKAR UNTUK OPTIMALISASI PANEN TANAMAN BUAH NANAS DI DAERAH PENYANGGA IBU KOTA NUSANTARA** yang secara singkat ditujukan kepada para petani buah nanas di daerah sekitar penyangga Ibu Kota Nusantara untuk melihat keberhasilan panen buah nanas berdasarkan prediksi cuaca di masa depan yang diprediksi menggunakan Artificial Intellegence.")

st.write("## Latar Belakang")
st.write("Ketidakpastian dalam prediksi cuaca sering mengakibatkan kerugian signifikan bagi petani buah nanas, terutama dalam menentukan waktu panen yang optimal. Tujuan dari proyek ini adalah mengembangkan tingkat akurasi prediksi cuaca menggunakan artificial intelligence sehingga membantu petani untuk menentukan waktu panen yang tepat agar memaksimalkan hasil panen serta mendukung pertanian yang lebih cerdas dan berkelanjutan. Proyek ini akan menggunakan metode ridge regression dan metode Rule Based Forward Chaining yang berguna untuk menganalisis data cuaca dan memberikan rekomendasi waktu panen yang optimal. Diharapkan bahwa dengan menggunakan model AI ini, petani akan dapat mengurangi kerugian akibat cuaca buruk dan meningkatkan hasil panen mereka. Proyek ini tidak hanya akan membantu petani mengoptimalkan waktu panen, tetapi juga berkontribusi pada ketahanan pangan dengan mengurangi risiko kerugian panen akibat cuaca yang tidak terduga.")

st.write("## Tim Kami")

left_co, cent_co, last_co = st.columns(3)

card_style = """
    <style>
    .card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    .card img {
        border-radius: 10px;
        max-width: 100%;
        height: auto;
    }
    .card p {
        margin: 10px 0 0 0;
        font-size: 17px;
        color: grey;
        font-weight: semi-bold;
    }
    </style>
"""

st.markdown(card_style, unsafe_allow_html=True)

# Card 1
with left_co:
    st.markdown(
        f'''
        <div class="card">
            <img src="data:image/jpg;base64,{adit_url}" alt="img">
            <p>Aditya Ridho Nugroho</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

# Card 2
with cent_co:
    st.markdown(
        f'''
        <div class="card">
            <img src="data:image/jpg;base64,{arya_url}" alt="img">
            <p>Arya Zaky Pradipta</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

# Card 3
with last_co:
    st.markdown(
        f'''
        <div class="card">
            <img src="data:image/jpg;base64,{fatwa_url}" alt="img">
            <p>Muhammad Fatwa Al Choiri</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.write("## Kontak")

# Informasi Kontak
contact_info = """
    <div class="contact">
        <p>Untuk informasi lebih lanjut, silakan hubungi kami melalui email:</p>
        <p><a href="mailto:11231003@student.itk.ac.id" target="_blank">11231003@student.itk.ac.id (Adit)</a></p>
        <p><a href="mailto:11231003@student.itk.ac.id" target="_blank">11231013@student.itk.ac.id (Arya)</a></p>
        <p><a href="mailto:11231003@student.itk.ac.id" target="_blank">11231055@student.itk.ac.id (Fatwa)</a></p>
    </div>
    <style>
    .contact {
        font-size: 18px;
        color: #333;
        margin-top: 10px;
    }
    .contact a {
        color: black;
        text-decoration: none;
    }
    .contact a:hover {
        text-decoration: underline;
    }
    </style>
"""

st.markdown(contact_info, unsafe_allow_html=True)
