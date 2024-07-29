import streamlit as st
import pandas as pd
import altair as alt

# page config

st.set_page_config(
    page_title="Grafik Cuaca",
    page_icon="📊",
    layout="centered"
)

# Konfigurasi tema
alt.themes.enable("dark")

# Baca file CSV
df = pd.read_csv("prediksi.csv")

# Konversi kolom DATE menjadi tipe datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Tambahkan kolom tahun
df['YEAR'] = df['DATE'].dt.year

# Filter data berdasarkan tahun yang dipilih
with st.sidebar:
    st.title('Prediksi Cuaca')
    year_list = df['YEAR'].unique().astype(str)  # Ambil tahun dari data
    selected_year = st.selectbox('Pilih tahun prediksi', year_list)

filtered_df = df[df['YEAR'] == int(selected_year)]

st.write(f"### 📊 Grafik Prediksi Cuaca tahun {selected_year}")

chart = alt.Chart(filtered_df).transform_fold(
    ['suhu', 'curah hujan', 'kelembaban udara'],
    as_=['Prediksi', 'Nilai']
).mark_line().encode(
    x='DATE:T',
    y='Nilai:Q',
    color='Prediksi:N'
).properties(
    width=800,
    height=400
)

st.altair_chart(chart)

average_temperature = filtered_df['suhu'].mean()
average_curah = filtered_df['curah hujan'].mean()
average_kelembaban = filtered_df['kelembaban udara'].mean()*100


# kolom rincian

st.header("Rincian prediksi cuaca")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌡️ Suhu rata-rata")
    st.write(f"Suhu rata rata pada tahun {selected_year} adalah {average_temperature:.2f}°F.")
    

with col2:
    st.markdown("### 🌧️ Curah hujan rata-rata")
    st.write(f"Curah hujan rata rata pada tahun {selected_year} adalah {average_curah:.2f} mm")
    
with col3:
    st.markdown("### ☁️ Kelembaban udara rata-rata")
    st.write(f"Kelembaban udara rata rata pada tahun {selected_year} adalah {average_kelembaban:.1f}%")



