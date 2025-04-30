
import streamlit as st
from PIL import Image
from fpdf import FPDF
import base64

# Configuración de la página
st.set_page_config(page_title="Calculadora de Dosis Médicas", layout="wide")

# Inicializar historial
if "historial" not in st.session_state:
    st.session_state.historial = []

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
    st.title("💊 Calculadora de Dosis Médicas")
    st.markdown("""
    Bienvenido a la **Calculadora de Dosis Médicas**, una herramienta precisa para el cálculo de dosis basado en peso corporal y concentración de medicamentos.

    Desarrollado por **Judá** como parte de un proyecto educativo y de impacto social.
    """)

st.markdown("---")

with st.expander("Abrir Calculadora de Dosis", expanded=False):

    modo = st.radio("Selecciona el modo de cálculo:", 
                    ("Calcular dosis a administrar", "Calcular dosis recibida"))

    if modo == "Calcular dosis a administrar":

        unidad_peso = st.radio("Unidad del peso ingresado:", ("Kilogramos (kg)", "Libras (lb)"))
        peso_ingresado = st.number_input("Peso del paciente", min_value=0.0, step=0.1, format="%.2f")
        if unidad_peso == "Libras (lb)":
            peso = peso_ingresado * 0.453592
            st.write(f"Peso convertido a kg: {peso:.2f} kg")
        else:
            peso = peso_ingresado

        dosis_requerida = st.number_input("Dosis requerida por kg (mg/kg)", min_value=0.0, step=0.1, format="%.2f")

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

                st.session_state.historial.append({
                    "Peso (kg)": round(peso, 2),
                    "Dosis (mg/kg)": round(dosis_requerida, 2),
                    "Concentración (mg/mL)": round(concentracion, 2),
                    "Resultado (mL)": round(volumen_a_administrar_ml, 2)
                })

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.set_font("Arial", 'B', 14)
                pdf.cell(200, 10, txt="Informe de Cálculo de Dosis Médica", ln=True, align="C")
                pdf.set_font("Arial", size=12)
                pdf.ln(10)
                pdf.cell(200, 10, txt=f"Peso del paciente: {peso:.2f} kg", ln=True)
                pdf.cell(200, 10, txt=f"Dosis requerida: {dosis_requerida:.2f} mg/kg", ln=True)
                pdf.cell(200, 10, txt=f"Concentración: {concentracion:.4f} mg/mL", ln=True)
                pdf.ln(5)
                pdf.cell(200, 10, txt="Fórmula aplicada:", ln=True)
                pdf.cell(200, 10, txt=f"({peso:.2f} × {dosis_requerida:.2f}) ÷ {concentracion:.4f}", ln=True)
                pdf.cell(200, 10, txt=f"Resultado: {volumen_a_administrar_ml:.2f} mL", ln=True)
                pdf.ln(10)
                pdf.cell(200, 10, txt="Proyecto desarrollado por Judá - 2025", ln=True)

                pdf_output = pdf.output(dest='S').encode('latin1')
                b64_pdf = base64.b64encode(pdf_output).decode('utf-8')
                href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="dosis_calculada.pdf">Descargar resultado en PDF</a>'
                st.markdown(href, unsafe_allow_html=True)

    elif modo == "Calcular dosis recibida":
        unidad_peso = st.radio("Unidad del peso ingresado:", ("Kilogramos (kg)", "Libras (lb)"), key="radio2")
        peso_ingresado = st.number_input("Peso del paciente", min_value=0.0, step=0.1, format="%.2f", key="peso_inverso")
        if unidad_peso == "Libras (lb)":
            peso = peso_ingresado * 0.453592
            st.write(f"Peso convertido a kg: {peso:.2f} kg")
        else:
            peso = peso_ingresado

        unidad_concentracion = st.radio("Unidad de la concentración del medicamento:", ("mg/mL", "μg/mL"), key="unidad_inv")
        concentracion_ingresada = st.number_input("Concentración del medicamento", min_value=0.0, step=0.1, format="%.2f", key="conc_inv")
        if unidad_concentracion == "μg/mL":
            concentracion = concentracion_ingresada / 1000
            st.write(f"Concentración convertida a mg/mL: {concentracion:.4f} mg/mL")
        else:
            concentracion = concentracion_ingresada

        volumen_admin = st.number_input("Volumen administrado (mL)", min_value=0.0, step=0.1, format="%.2f")

        if st.button("Calcular dosis recibida"):
            if peso <= 0:
                st.error("Error: El peso debe ser mayor que 0.")
            elif concentracion <= 0:
                st.error("Error: La concentración debe ser mayor que 0.")
            elif volumen_admin <= 0:
                st.error("Error: El volumen debe ser mayor que 0.")
            else:
                dosis_total_mg = volumen_admin * concentracion
                dosis_por_kg = dosis_total_mg / peso

                st.success("Resultado del cálculo inverso:")
                st.write(f"**Dosis total administrada:** {dosis_total_mg:.2f} mg")
                st.write(f"**Dosis por kg:** {dosis_por_kg:.2f} mg/kg")
                st.write("---")
                st.write(f"**Fórmula aplicada:** ({volumen_admin:.2f} × {concentracion:.2f}) ÷ {peso:.2f}")

if st.session_state.historial:
    st.markdown("## Historial de cálculos realizados")
    st.dataframe(st.session_state.historial)

st.markdown("---")
st.caption("Proyecto creado por Judá - 2025")
st.markdown('</div>', unsafe_allow_html=True)
