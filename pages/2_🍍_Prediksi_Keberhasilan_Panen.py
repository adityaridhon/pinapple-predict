import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Prediksi Keberhasilan Panen",
    page_icon="🍍"
)

st.markdown('# 🍍 Prediksi Keberhasilan Panen Berdasarkan Tahun dan Bulan')

# Baca file CSV
df = pd.read_csv("prediksi.csv")

# Konversi kolom DATE menjadi tipe datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Tambahkan kolom tahun dan bulan
df['YEAR'] = df['DATE'].dt.year
df['MONTH'] = df['DATE'].dt.month

# Ambil tahun dari data dan buat pilihan
year_list = df['YEAR'].unique().astype(str)
selected_year = st.selectbox('Pilih tahun prediksi', year_list)

# Ambil bulan dari data dan buat pilihan
month_list = df[df['YEAR'] == int(selected_year)]['MONTH'].unique()
month_list.sort()
month_names = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
month_dict = dict(enumerate(month_names, start=1))
selected_month = st.selectbox('Pilih bulan prediksi', [month_dict[m] for m in month_list])

# Convert bulan yang dipilih menjadi angka
selected_month_num = list(month_dict.keys())[list(month_dict.values()).index(selected_month)]

# Filter data berdasarkan tahun dan bulan yang dipilih
filtered_df = df[(df['YEAR'] == int(selected_year)) & (df['MONTH'] == selected_month_num)]

# Hitung suhu rata-rata untuk bulan dan tahun yang dipilih
average_temperature = filtered_df['suhu'].mean()

# Tentukan rentang suhu dalam Fahrenheit
min_temp = 71
max_temp = 90

# Logika rekomendasi
if min_temp <= average_temperature <= max_temp:
    recommendation_message = "direkomendasikan untuk menanam tanaman nanas."
else:
    recommendation_message = "tidak direkomendasikan untuk menanam tanaman nanas."

# Tampilkan hasil rekomendasi

col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button("Prediksi keberhasilan panen", type="primary")

with col2:
    button2 = st.button('Reset', type="secondary")

if button1:
    st.write(f"Pada bulan {selected_month} tahun {selected_year}, suhu rata-rata adalah {average_temperature:.2f}°F.")
    st.write(f"Rekomendasi: {recommendation_message}")


    
