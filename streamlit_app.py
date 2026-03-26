import streamlit as st
import numpy as np
import random

# Configuración
st.set_page_config(page_title="Nexus AI - Real Brain", page_icon="🧠")

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# --- CEREBRO CON RUIDO ---
W0 = np.array([[-6.5, -4.5, 3.2, 5.0], [-7.4, -5.6, 4.3, 6.9]])
W1 = np.array([[-12.5], [-5.8], [4.7], [10.2]])

st.title("🧠 Nexus AI: Procesamiento Real")

modo = st.selectbox(
    "Escenario:",
    ("Instituto", "Banco", "Supervivencia")
)

if modo == "Instituto":
    st.write("Analizando variables académicas...")
    l1, l2 = "Deberes", "Exámenes"
elif modo == "Banco":
    st.write("Evaluando riesgo financiero...")
    l1, l2 = "Ahorros", "Deudas"
else:
    st.write("Simulando encuentro hostil...")
    l1, l2 = "Energía", "Peligro"

st.divider()

v1 = st.slider(l1, 0.0, 1.0, 0.5)
val_neg = st.slider(l2, 0.0, 1.0, 0.5)
v2 = 1.0 - val_neg

if st.button("🚀 INICIAR CÁLCULO NEURAL"):
    # Añadimos un pequeño error aleatorio (ruido) para que no sea perfecto
    ruido = random.uniform(-0.02, 0.02)
    
    entrada = np.array([v1, v2])
    layer1 = sigmoid(np.dot(entrada, W0))
    # Aplicamos el ruido al resultado final
    pred = sigmoid(np.dot(layer1, W1))[0] + ruido
    
    # Aseguramos que no se pase de 0 o 100
    prob = max(0, min(100, float(pred * 100)))
    
    st.divider()
    
    # Mostramos MUCHOS decimales para que se vea el cálculo crudo
    st.code(f"Procesando señales... Resultado bruto: {prob}%")

    if prob >= 87.34:
        st.success(f"### PROBABILIDAD: {prob:.4f}%")
        st.write("Veredicto: Los parámetros indican un éxito casi total.")
    elif prob >= 42.15:
        st.warning(f"### PROBABILIDAD: {prob:.4f}%")
        st.write("Veredicto: Datos inestables. Hay demasiada interferencia negativa.")
    else:
        st.error(f"### PROBABILIDAD: {prob:.4f}%")
        st.write("Veredicto: Colapso de probabilidad. El sistema recomienda abortar.")

st.divider()
st.caption("Nexus AI v12.0 | Raw Neural Data Mode")
