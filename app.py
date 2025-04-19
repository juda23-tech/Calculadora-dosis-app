
import streamlit as st
from PIL import Image

# Cargar el logotipo
logo = Image.open("logo_calculadora_dosis.png")
st.image(logo, width=200)

st.title("Calculadora de Dosis Médica")

st.markdown(
    "Esta aplicación permite calcular la dosis de un medicamento basada en el peso del paciente, "
    "la dosis requerida por kg y la concentración del medicamento."
)

# Entradas del usuario
peso = st.number_input("Peso del paciente (kg)", min_value=0.0, step=0.1)
dosis_kg = st.number_input("Dosis requerida por kg (mg/kg)", min_value=0.0, step=0.1)
concentracion = st.number_input("Concentración del medicamento (mg/mL)", min_value=0.0, step=0.1)

# Cálculo
if st.button("Calcular dosis"):
    if peso > 0 and dosis_kg > 0 and concentracion > 0:
        dosis_total_mg = peso * dosis_kg
        volumen_ml = dosis_total_mg / concentracion

        st.success(f"Dosis total: {dosis_total_mg:.2f} mg")
        st.success(f"Volumen a administrar: {volumen_ml:.2f} mL")
    else:
        st.warning("Por favor, introduce valores válidos en todos los campos.")

st.markdown("---")
st.caption("Proyecto creado por Judá - 2025")
