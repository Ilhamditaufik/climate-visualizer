import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load Data
df = pd.read_csv('data/suhu_seluruh_provinsi.csv')

# Sidebar Filter
st.sidebar.title("Filter Data")
provinsi = st.sidebar.selectbox("Pilih Provinsi", df["Provinsi"].unique())

# Filter data
filtered = df[df["Provinsi"] == provinsi]

# Judul
st.title("🌡️ Visualisasi Suhu Tahunan di Indonesia")
st.write(f"Data suhu rata-rata tahunan di provinsi {provinsi}")

# Plot
fig = px.line(filtered, x="Tahun", y="Suhu", markers=True, title="Perubahan Suhu")
st.plotly_chart(fig)

st.markdown("### Peta Interaktif Suhu di Indonesia")

# Pilih tahun
tahun_dipilih = st.slider("Pilih Tahun", min_value=2015, max_value=2020, value=2020)
# Baca data suhu lengkap dengan koordinat
df_suhu = pd.read_csv("suhu_dengan_koordinat.csv")

df_map = df_suhu[df_suhu["Tahun"] == tahun_dipilih]

# Peta suhu
fig_map = px.scatter_geo(
    df_map,
    lat="Latitude",
    lon="Longitude",
    hover_name="Provinsi",
    size="Suhu",
    color="Suhu",
    color_continuous_scale="OrRd",
    projection="natural earth",
    title=f"Peta Persebaran Suhu di Indonesia Tahun {tahun_dipilih}"
)
fig_map.update_layout(height=600)

st.plotly_chart(fig_map)

import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("suhu_dengan_koordinat.csv")

# Buat peta animasi
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Suhu",
    size="Suhu",
    hover_name="Provinsi",
    animation_frame="Tahun",
    projection="natural earth",
    color_continuous_scale="OrRd",
    title="Animasi Persebaran Suhu Udara di Indonesia (2015–2020)"
)

fig.update_layout(
    geo=dict(
        showland=True,
        landcolor="rgb(243, 243, 243)",
        showcountries=True,
        countrycolor="rgb(204, 204, 204)"
    )
)

fig.show()



