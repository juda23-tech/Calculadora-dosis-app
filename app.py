
import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Calculadora de Dosis Médicas", layout="wide")

# --- Estilos personalizados ---
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main {
        background-color: #ffffff;
        padding: 20px 40px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 20px;
    }
    h1, h2 {
        color: #003366;
    }
    .stButton button {
        background-color: #003366;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #0059b3;
    }
    .stRadio > label {
        font-size: 18px;
    }
    .stNumberInput > label {
        font-size: 18px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

# Logo
logo = Image.open("logo_calculadora_dosis.png")
col1, col2 = st.columns([1, 3])
with col1:
    st.image(logo, width=150)
with col2:
    st.title("Calculadora de Dosis Médicas")
    st.markdown("""
    Bienvenido a la **Calculadora de Dosis Médicas**, una herramienta precisa para el cálculo de dosis basado en peso corporal y concentración de medicamentos.

    Desarrollado por **Judá** como parte de un proyecto educativo y de impacto social.
    """)

st.markdown("---")

# --- Expander para mostrar la calculadora ---
with st.expander("Abrir Calculadora de Dosis", expanded=False):

    st.header("Calculadora de Dosis")

    # Paso 1: Unidad de peso
    unidad_peso = st.radio("Unidad del peso ingresado:", ("Kilogramos (kg)", "Libras (lb)"))
    peso_ingresado = st.number_input("Peso del paciente", min_value=0.0, step=0.1, format="%.2f")
    if unidad_peso == "Libras (lb)":
        peso = peso_ingresado * 0.453592
        st.write(f"Peso convertido a kg: {peso:.2f} kg")
    else:
        peso = peso_ingresado

    # Paso 2: Dosis requerida
    dosis_requerida = st.number_input("Dosis requerida por kg (mg/kg)", min_value=0.0, step=0.1, format="%.2f")

    # Paso 3: Medicamento frecuente
    st.subheader("Selecciona un medicamento frecuente (opcional)")
    medicamento = st.selectbox(
        "Medicamento:",
        ("Selecciona un medicamento", 
         "Amoxicilina suspensión 250 mg/5 mL",
         "Ibuprofeno suspensión 100 mg/5 mL",
         "Paracetamol suspensión 120 mg/5 mL",
         "Azitromicina suspensión 200 mg/5 mL",
         "Claritromicina suspensión 125 mg/5 mL",
         "Otro")
    )

    # Concentración según selección
    if medicamento == "Amoxicilina suspensión 250 mg/5 mL":
        concentracion = 250 / 5
        st.info("Concentración establecida automáticamente: 50 mg/mL")
    elif medicamento == "Ibuprofeno suspensión 100 mg/5 mL":
        concentracion = 100 / 5
        st.info("Concentración establecida automáticamente: 20 mg/mL")
    elif medicamento == "Paracetamol suspensión 120 mg/5 mL":
        concentracion = 120 / 5
        st.info("Concentración establecida automáticamente: 24 mg/mL")
    elif medicamento == "Azitromicina suspensión 200 mg/5 mL":
        concentracion = 200 / 5
        st.info("Concentración establecida automáticamente: 40 mg/mL")
    elif medicamento == "Claritromicina suspensión 125 mg/5 mL":
        concentracion = 125 / 5
        st.info("Concentración establecida automáticamente: 25 mg/mL")
    else:
        unidad_concentracion = st.radio("Unidad de la concentración del medicamento:", ("mg/mL", "μg/mL"))
        concentracion_ingresada = st.number_input("Concentración del medicamento", min_value=0.0, step=0.1, format="%.2f")
        if unidad_concentracion == "μg/mL":
            concentracion = concentracion_ingresada / 1000
            st.write(f"Concentración convertida a mg/mL: {concentracion:.4f} mg/mL")
        else:
            concentracion = concentracion_ingresada

    # Paso 4: Calcular dosis
    if st.button("Calcular dosis"):
        if peso <= 0:
            st.error("Error: El peso debe ser mayor que 0.")
        elif dosis_requerida <= 0:
            st.error("Error: La dosis requerida debe ser mayor que 0.")
        elif concentracion <= 0:
            st.error("Error: La concentración debe ser mayor que 0.")
        else:
            dosis_total_mg = peso * dosis_requerida
            volumen_a_administrar_ml = dosis_total_mg / concentracion

            st.success("Cálculo realizado exitosamente:")
            st.write(f"**Peso utilizado (en kg):** {peso:.2f}")
            st.write(f"**Dosis requerida:** {dosis_requerida:.2f} mg/kg")
            st.write(f"**Concentración utilizada:** {concentracion:.4f} mg/mL")
            st.write("---")
            st.write(f"**Fórmula aplicada:** ({peso:.2f} × {dosis_requerida:.2f}) ÷ {concentracion:.4f}")
            st.write(f"**Resultado final:** {volumen_a_administrar_ml:.2f} mL")

st.markdown("---")
st.caption("Proyecto creado por Judá - 2025")
st.markdown('</div>', unsafe_allow_html=True)
