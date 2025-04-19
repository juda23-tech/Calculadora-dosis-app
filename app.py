import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Calculadora de Dosis Médicas", layout="wide")

# Ocultar el menú y footer de Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Cargar logotipo
logo = Image.open("logo_calculadora_dosis.png")

# Layout de bienvenida con columnas
col1, col2 = st.columns([1, 3])
with col1:
    st.image(logo, width=150)
with col2:
    st.title("Calculadora de Dosis Médicas")
    st.markdown("""
    Bienvenido a la **Calculadora de Dosis Médicas**, una herramienta sencilla y precisa para el cálculo de dosis en función del peso corporal del paciente y la dosis por kilogramo.

    Desarrollado por **Judá** como parte de un proyecto educativo y de impacto social.
    """)

# Botón para acceder a la calculadora
st.markdown("---")
if st.button("Ingresar a la calculadora"):
    st.session_state["mostrar_calculadora"] = True

# Lógica de la calculadora
if "mostrar_calculadora" in st.session_state and st.session_state["mostrar_calculadora"]:
    st.header("Calculadora de Dosis")

    peso = st.number_input("Peso del paciente (kg):", min_value=0.0, format="%.2f")
    dosis_kg = st.number_input("Dosis por kg (mg/kg):", min_value=0.0, format="%.2f")

    if st.button("Calcular dosis total"):
        dosis_total = peso * dosis_kg
        st.success(f"Dosis total: **{dosis_total:.2f} mg**")
    else:
        st.warning("Por favor, introduce valores válidos en todos los campos.")

st.markdown("---")
st.caption("Proyecto creado por Judá - 2025")
