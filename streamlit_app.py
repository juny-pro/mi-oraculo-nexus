import streamlit as st
import numpy as np

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Nexus AI Decision", page_icon="🧠", layout="centered")

# --- EL MOTOR DE LA IA (Nexus Engine) ---
def sigmoid(x): return 1 / (1 + np.exp(-x))

# Pesos ya entrenados (para que la App cargue instantáneo)
# Estos números son el "cerebro" que Nexus aprendió tras las 50,000 épocas
W0 = np.array([[-6.3, -4.2, 3.8, 5.1], [-6.4, -4.1, 3.7, 5.0]])
W1 = np.array([[-9.5], [-4.5], [4.4], [9.3]])

# --- DISEÑO DE LA APP ---
st.title("🧠 Nexus AI: ¿Qué hago hoy?")
st.write("Introduce tus datos y deja que la Inteligencia Artificial decida por ti.")

st.divider()

# Sliders (Barras deslizantes) para que sea más visual
st.subheader("📊 Tus Datos Actuales")

col1, col2 = st.columns(2)

with col1:
    dato_1 = st.slider("Deberes / Responsabilidad", 0.0, 1.0, 0.5, help="0 = Nada hecho, 1 = Todo listo")

with col2:
    dato_2 = st.slider("Exámenes / Presión", 0.0, 1.0, 0.5, help="0 = Relax total, 1 = Examen mañana")

# --- LÓGICA DE DECISIÓN ---
if st.button("🔥 CONSULTAR A NEXUS", use_container_width=True):
    # Cálculo rápido (Inferencia)
    entrada = np.array([dato_1, dato_2])
    l1 = sigmoid(np.dot(entrada, W0))
    prediccion = sigmoid(np.dot(l1, W1))[0]

    st.divider()

    # Mostrar resultado con colores
    prob = prediccion * 100
    if prob > 80:
        st.balloons()
        st.success(f"### RESULTADO: {prob:.2f}% - ¡DALE CAÑA!")
        st.write("Nexus dice: **Tienes luz verde.** Puedes viciar, salir o descansar. ¡Te lo has ganado!")
    elif prob < 20:
        st.error(f"### RESULTADO: {prob:.2f}% - ¡PELIGRO!")
        st.write("Nexus dice: **Ni se te ocurra.** Ponte a estudiar o terminar tus cosas antes de que sea tarde.")
    else:
        st.warning(f"### RESULTADO: {prob:.2f}% - REVISIÓN MANUAL")
        st.write("Nexus dice: **Estás en la cuerda floja.** Termina una cosa más y vuelve a preguntarme.")

st.divider()
st.caption("Nexus AI v7.5 - Creado por un futuro Ingeniero de IA")
