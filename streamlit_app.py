import streamlit as st
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Nexus AI - Oráculo Multiverso", page_icon="🧠")

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# --- CEREBRO DE LA IA (Modo Lógica Real) ---
# Pesos configurados para que los factores negativos pesen mucho
W0 = np.array([[-6.5, -4.5, 3.2, 5.0], [-7.4, -5.6, 4.3, 6.9]])
W1 = np.array([[-12.5], [-5.8], [4.7], [10.2]])

st.title("🧠 Nexus AI: Decisiones Inteligentes")

# 1. Selector de modo
modo = st.selectbox(
    "Selecciona el escenario de consulta:",
    ("Instituto", "Banco", "Supervivencia")
)

# 2. Descripción dinámica según el modo
if modo == "Instituto":
    st.write("✨ **Descripción:** Analiza si tus deberes compensan la presión de los exámenes para permitirte tiempo de ocio.")
    label_1, label_2 = "😇 Deberes hechos", "📚 Exámenes cerca"
    ayuda_2 = "1.0 significa que el examen es mañana mismo."
elif modo == "Banco":
    st.write("🏦 **Descripción:** Evaluación de riesgo crediticio basada en tu capital disponible y tus deudas actuales.")
    label_1, label_2 = "💰 Ahorros totales", "💸 Deudas pendientes"
    ayuda_2 = "1.0 significa que tienes deudas muy altas."
else:
    st.write("🧟 **Descripción:** Cálculo de probabilidad de éxito en un encuentro hostil basado en tus recursos.")
    label_1, label_2 = "🔋 Energía actual", "🧟 Proximidad del peligro"
    ayuda_2 = "1.0 significa que el peligro está justo frente a ti."

st.divider()

# 3. Sliders de entrada
col1, col2 = st.columns(2)
with col1:
    v1 = st.slider(label_1, 0.0, 1.0, 0.5)
with col2:
    val_negativo = st.slider(label_2, 0.0, 1.0, 0.5, help=ayuda_2)
    # Inversión lógica: más examen/deuda/peligro = menos probabilidad
    v2 = 1.0 - val_negativo

# 4. Botón de ejecución
if st.button("🚀 CONSULTAR AL ORÁCULO", use_container_width=True):
    entrada = np.array([v1, v2])
    l1 = sigmoid(np.dot(entrada, W0))
    pred = sigmoid(np.dot(l1, W1))[0]
    prob = float(pred * 100)
    
    st.divider()
    
    # Mostrar resultado con colores lógicos
    if prob >= 80:
        st.balloons()
        st.success(f"### RESULTADO: {prob:.1f}%")
        st.write("**Veredicto:** Las condiciones son muy favorables. Tienes luz verde para proceder.")
    elif prob >= 40:
        st.warning(f"### RESULTADO: {prob:.1f}%")
        st.write("**Veredicto:** Situación de riesgo moderado. Se recomienda precaución o mejorar los datos de entrada.")
    else:
        st.error(f"### RESULTADO: {prob:.1f}%")
        st.write("**Veredicto:** Probabilidad insuficiente. Los factores negativos superan los recursos disponibles.")

st.divider()
st.caption(f"Nexus AI v11.0 | Escenario activo: {modo}")
