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

import streamlit as st

# Título principal
st.title("Calculadora de Dosis Médicas Mejorada")

# Entradas de datos
import streamlit as st

st.title("Calculadora de Dosis Médicas Mejorada")

# Selector de unidad de peso
unidad_peso = st.radio("Unidad del peso ingresado:", ("Kilogramos (kg)", "Libras (lb)"))

# Entrada de peso
peso_ingresado = st.number_input("Peso del paciente", min_value=0.0, step=0.1, format="%.2f")

# Conversión automática si elige libras
if unidad_peso == "Libras (lb)":
    peso = peso_ingresado * 0.453592
    st.write(f"Peso convertido a kg: {peso:.2f} kg")
else:
    peso = peso_ingresado

# Otras entradas
dosis_requerida = st.number_input("Dosis requerida por kg (mg/kg)", min_value=0.0, step=0.1, format="%.2f")
concentracion = st.number_input("Concentración del medicamento (mg/mL)", min_value=0.0, step=0.1, format="%.2f")

# Botón para calcular
if st.button("Calcular dosis"):

    # Validaciones
    if peso <= 0:
        st.error("Error: El peso debe ser mayor que 0.")
    elif dosis_requerida <= 0:
        st.error("Error: La dosis requerida debe ser mayor que 0.")
    elif concentracion <= 0:
        st.error("Error: La concentración debe ser mayor que 0.")
    else:
        # Cálculo
        dosis_total_mg = peso * dosis_requerida
        volumen_a_administrar_ml = dosis_total_mg / concentracion

        # Mostrar procedimiento
        st.success("Cálculo realizado exitosamente:")
        st.write(f"**Peso utilizado (en kg):** {peso:.2f}")
        st.write(f"**Dosis requerida:** {dosis_requerida:.2f} mg/kg")
        st.write(f"**Concentración:** {concentracion:.2f} mg/mL")
        st.write("---")
        st.write(f"**Fórmula aplicada:** ({peso:.2f} × {dosis_requerida:.2f}) ÷ {concentracion:.2f}")
        st.write(f"**Resultado final:** {volumen_a_administrar_ml:.2f} mL")

st.markdown("---")
st.caption("Proyecto creado por Judá - 2025")
