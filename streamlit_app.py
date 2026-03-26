import streamlit as st
import numpy as np

# Configuración
st.set_page_config(page_title="Nexus AI", page_icon="🧠")

# --- NUEVA SECCIÓN: GUÍA PARA TUS AMIGOS ---
with st.expander("📖 ¿Cómo funciona esto? (Lee aquí)"):
    st.write("""
    ¡Bienvenido al Oráculo Nexus! Esta IA ha sido entrenada con 50,000 épocas para ayudarte a decidir.
    
    **Ejemplo práctico:**
    1. Si has terminado los deberes, pon el primer slider en **1.00**.
    2. Si no tienes exámenes cerca, pon el segundo slider en **0.00**.
    3. Dale al botón y Nexus te dirá si puedes jugar.
    
    *Recuerda: Si sale 'Revisión Manual', es que estás en la zona gris. ¡Esfuérzate un poco más!*
    """)

# --- EL RESTO DEL CÓDIGO ---
st.title("🧠 Nexus AI: ¿Qué hago hoy?")
st.write("Introduce tus datos y deja que la Inteligencia Artificial decida por ti.")

def sigmoid(x): return 1 / (1 + np.exp(-x))
W0 = np.array([[-6.3, -4.2, 3.8, 5.1], [-6.4, -4.1, 3.7, 5.0]])
W1 = np.array([[-9.5], [-4.5], [4.4], [9.3]])

st.divider()
st.subheader("📊 Tus Datos Actuales")

col1, col2 = st.columns(2)
with col1:
    dato_1 = st.slider("Deberes / Responsabilidad", 0.0, 1.0, 0.5)
with col2:
    dato_2 = st.slider("Exámenes / Presión", 0.0, 1.0, 0.5)

if st.button("🔥 CONSULTAR A NEXUS", use_container_width=True):
    entrada = np.array([dato_1, dato_2])
    l1 = sigmoid(np.dot(entrada, W0))
    prediccion = sigmoid(np.dot(l1, W1))[0]
    
    st.divider()
    prob = prediccion * 100
    if prob > 80:
        st.balloons()
        st.success(f"### RESULTADO: {prob:.2f}% - ¡DALE CAÑA!")
    elif prob < 20:
        st.error(f"### RESULTADO: {prob:.2f}% - ¡PELIGRO!")
    else:
        st.warning(f"### RESULTADO: {prob:.2f}% - REVISIÓN MANUAL")

st.divider()
st.caption("Nexus AI v7.5 - Creado por un futuro Ingeniero de IA")
