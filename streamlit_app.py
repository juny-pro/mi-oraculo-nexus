import streamlit as st
import numpy as np
import random

st.set_page_config(page_title="Nexus AI - Equilibrio Real", page_icon="⚖️")

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# --- PESOS EQUILIBRADOS ---
# Hemos ajustado los pesos para que el 0 absoluto sea el centro de la curva
W0 = np.array([[-5.0, -3.0, 3.0, 5.0], [-5.0, -3.0, 3.0, 5.0]])
W1 = np.array([[-10.0], [-5.0], [5.0], [10.0]])
# El Bias (Sesgo) ahora es 0 para que (0,0) tienda al centro (0.5)
BIAS = 0.0 

st.title("⚖️ Nexus AI: El Oráculo Equilibrado")

modo = st.selectbox(
    "Selecciona el escenario:",
    ("Instituto", "Banco", "Supervivencia Zombie", "Deportes", "Citas", "Cripto", "Cocina")
)

# Descripciones (Manteniendo las que querías)
descripciones = {
    "Instituto": ("Deberes hechos", "Exámenes cerca", "Analizando esfuerzo vs presión."),
    "Banco": ("Ahorros", "Deudas", "Evaluando solvencia financiera."),
    "Supervivencia Zombie": ("Energía", "Peligro", "Cálculo de huida o combate."),
    "Deportes": ("Tu Forma", "Nivel Rival", "Probabilidad de victoria."),
    "Citas": ("Química", "Red Flags", "Predicción de éxito social."),
    "Cripto": ("Inversión", "Caída Mercado", "Probabilidad de ganancia."),
    "Cocina": ("Ingredientes", "Distracción", "¿Será comestible?")
}

info = descripciones[modo]
st.info(f"✨ **Escenario:** {info[2]}")

col1, col2 = st.columns(2)
with col1:
    v1 = st.slider(info[0], 0.0, 1.0, 0.0) # Empezamos en 0
with col2:
    v2_raw = st.slider(info[1], 0.0, 1.0, 0.0) # Empezamos en 0

if st.button("🧠 PROCESAR"):
    # Lógica de balance: v1 suma, v2 resta
    # Si ambos son 0, la entrada es 0, y sigmoid(0) es exactamente 0.5 (50%)
    entrada = np.array([v1, -v2_raw]) 
    
    l1 = sigmoid(np.dot(entrada, W0) + BIAS)
    pred = sigmoid(np.dot(l1, W1) + BIAS)[0]
    
    # Añadimos un micro-ruido para que no sea un 50.000000 exacto y aburrido
    ruido = random.uniform(-0.0001, 0.0001)
    prob = float((pred + ruido) * 100)
    
    st.divider()
    st.write(f"**Análisis de señales crudas finalizado.**")
    
    if prob >= 70.0:
        st.success(f"### PROBABILIDAD: {prob:.6f}%")
        st.write("Veredicto: Condiciones favorables.")
    elif prob >= 40.0:
        st.warning(f"### PROBABILIDAD: {prob:.6f}%")
        st.write("Veredicto: Incertidumbre detectada. Punto de equilibrio.")
    else:
        st.error(f"### PROBABILIDAD: {prob:.6f}%")
        st.write("Veredicto: Riesgo extremo. Probabilidad mínima.")

st.divider()
st.caption("Nexus Engine v15.0 | Zero-Point Balance")
