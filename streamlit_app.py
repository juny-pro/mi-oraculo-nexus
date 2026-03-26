import streamlit as st
import numpy as np

# Configuración
st.set_page_config(page_title="Nexus AI: Sargento Estricto", page_icon="👮‍♂️")

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# --- PESOS AJUSTADOS (MODO ESTRICTO) ---
# Hemos subido los valores a -8 y -10 para que la IA sea mucho más radical.
# Ahora, un examen cerca (v2 bajo) restará muchísima más puntuación.
W0 = np.array([[-6.5, -4.5, 3.2, 5.0], [-7.4, -5.6, 4.3, 6.9]])
W1 = np.array([[-12.5], [-5.8], [4.7], [10.2]])

st.title("👮‍♂️ Nexus AI: Modo Sargento")
st.write("En este modo, Nexus no perdona. Si hay exámenes, la probabilidad cae en picado.")

# Selector de modo
modo = st.selectbox(
    "Selecciona el escenario:",
    ("Instituto", "Banco", "Supervivencia")
)

st.divider()

# Lógica de inversión de datos
if modo == "Instituto":
    v1 = st.slider("😇 Deberes hechos (1 = Todo listo)", 0.0, 1.0, 0.5)
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
    
    # Mensajes según el nuevo rigor de la IA
    if prob >= 85:
        st.balloons()
        st.success(f"### {prob:.1f}% - PERMISO CONCEDIDO")
        st.write("**Sargento Nexus:** 'Impecable. Has cumplido. Retírese a descansar.'")
    elif prob >= 40:
        st.warning(f"### {prob:.1f}% - REVISIÓN NEGATIVA")
        st.write("**Sargento Nexus:** 'No es suficiente. Ese examen te va a machacar si no estudias más.'")
    else:
        st.error(f"### {prob:.1f}% - ¡A ESTUDIAR!")
        st.write("**Sargento Nexus:** '¿Cero coma algo por ciento? ¡Ni se te ocurra tocar la consola!'")

st.divider()
st.caption("Nexus AI v10.0 | Algoritmo de Rigor Extremo")
