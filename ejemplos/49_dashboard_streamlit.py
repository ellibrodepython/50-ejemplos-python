# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install streamlit pandas
# 2. Ejecuta el script: streamlit run 49_dashboard_streamlit.py
# 3. Abre el navegador en: http://localhost:8501

# Fuente:
# https://data.worldbank.org/indicator/SP.DYN.LE00.IN

import streamlit as st
import pandas as pd
df = pd.read_csv("49_dashboard_streamlit.csv", skiprows=3)

st.title("🌎 Esperanza de Vida Mundial")

df = df[['Country Name'] + [str(year) for year in range(1960, 2023)]]
df.set_index('Country Name', inplace=True)

p = st.multiselect("✅ Selecciona países", df.index)
st.line_chart(df.loc[p].T)