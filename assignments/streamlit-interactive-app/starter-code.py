import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Interfaz interactiva", layout="wide")

st.title("Interfaz web interactiva con Streamlit")
st.write("Carga un CSV o usa el dataset de ejemplo incluido para explorar datos.")

@st.cache_data
def load_sample_data():
    # Genera un dataset de ejemplo si no se sube ninguno
    import numpy as np
    n = 200
    df = pd.DataFrame({
        "category": np.random.choice(["A", "B", "C"], size=n),
        "x": pd.date_range("2023-01-01", periods=n, freq="D"),
        "value": (np.random.randn(n).cumsum() + 50).round(2),
        "score": (np.random.rand(n) * 100).round(1),
    })
    return df

uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = load_sample_data()

st.sidebar.header("Controles")
cols = list(df.columns)
numeric_cols = df.select_dtypes(include="number").columns.tolist()
date_cols = df.select_dtypes(include=["datetime64[ns]"]).columns.tolist()

x_col = st.sidebar.selectbox("Eje X", options=cols, index=cols.index(cols[0]))
y_col = st.sidebar.selectbox("Eje Y", options=numeric_cols, index=0 if numeric_cols else 0)

if date_cols:
    date_col = date_cols[0]
    df[date_col] = pd.to_datetime(df[date_col])
    min_date = df[date_col].min()
    max_date = df[date_col].max()
    date_range = st.sidebar.date_input("Rango de fechas", [min_date, max_date])
    if len(date_range) == 2:
        start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        df = df[(df[date_col] >= start) & (df[date_col] <= end)]

st.header("Resumen de datos")
st.write(df.describe(include='all'))

st.header("Vista previa filtrada")
st.dataframe(df.head(50))

st.header("Visualización")
chart = alt.Chart(df).mark_line().encode(
    x=x_col,
    y=y_col,
    color='category:N'
).interactive()

st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.write("Sugerencias: añade más controles, validación de entrada y más visualizaciones.")
