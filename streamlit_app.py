import streamlit as st
import numpy as np

# Configuración
st.set_page_config(page_title="Nexus AI Corregida", page_icon="🧠")

def sigmoid(x): return 1 / (1 + np.exp(-x))

# Pesos ajustados para que las decisiones sean lógicas
W0 = np.array([[-2.5, -1.5, 1.2, 2.0], [-2.4, -1.6, 1.3, 1.9]])
W1 = np.array([[-3.5], [-1.8], [1.7], [3.2]])

st.title("🧠 Nexus AI: El Oráculo Lógico")
st.write("Ahora Nexus entiende que los exámenes son presión negativa.")

# Selector de modo
modo = st.selectbox(
    "Selecciona el escenario:",
    ("Instituto", "Banco", "Supervivencia")
)

st.divider()

# --- AQUÍ ESTÁ EL TRUCO ---
if modo == "Instituto":
    v1 = st.slider("😇 Deberes hechos (1 = Todo listo)", 0.0, 1.0, 0.5)
    # Invertimos: si pones 1 en exámenes, la IA recibe un 0 (presión máxima)
    val_examenes = st.slider("📚 Proximidad de Exámenes (1 = Mañana mismo)", 0.0, 1.0, 0.5)
    v2 = 1.0 - val_examenes 

elif modo == "Banco":
    v1 = st.slider("💰 Ahorros (1 = Muchos)", 0.0, 1.0, 0.5)
    val_deudas = st.slider("💸 Deudas pendientes (1 = Muchas deudas)", 0.0, 1.0, 0.5)
    v2 = 1.0 - val_deudas

else:
    v1 = st.slider("🔋 Energía (1 = A tope)", 0.0, 1.0, 0.5)
    val_daño = st.slider("🧟 Distancia del Zombie (1 = Encima de ti)", 0.0, 1.0, 0.5)
    v2 = 1.0 - val_daño

if st.button("🔥 CONSULTAR A NEXUS", use_container_width=True):
    entrada = np.array([v1, v2])
    l1 = sigmoid(np.dot(entrada, W0))
    pred = sigmoid(np.dot(l1, W1))[0]
    prob = float(pred * 100)
    
    st.divider()
    
    # Mensajes lógicos
    if prob >= 80:
        st.balloons()
        st.success(f"### {prob:.1f}% - ¡ADELANTE!")
        st.write("**Nexus dice:** 'Todo bajo control. Disfruta.'")
    elif prob >= 45:
        st.warning(f"### {prob:.1f}% - CUIDADO")
        st.write("**Nexus dice:** 'Estás en el límite. Haz algo productivo primero.'")
    else:
        st.error(f"### {prob:.1f}% - DENEGADO")
        st.write("**Nexus dice:** 'Prioridades, por favor. Ponte a trabajar.'")

st.divider()
st.caption("Nexus AI v9.5 | Lógica de inversión de datos activada")
