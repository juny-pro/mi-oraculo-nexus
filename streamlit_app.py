import streamlit as st
import numpy as np
import random

# Configuración de la página
st.set_page_config(page_title="Nexus AI - Multiverso Pro", page_icon="♾️")

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# --- MOTOR NEURAL (Ajustado para máximo rigor) ---
W0 = np.array([[-6.8, -4.2, 3.5, 5.2], [-7.5, -5.8, 4.0, 6.5]])
W1 = np.array([[-13.2], [-6.1], [5.2], [10.8]])

st.title("♾️ Nexus AI: El Oráculo Multiverso")

# 1. Selector de Escenario Expandido
modo = st.selectbox(
    "Selecciona el plano de realidad a consultar:",
    ("Instituto", "Banco", "Supervivencia Zombie", "Citas / Amistad", "Deportes / Competición")
)

st.divider()

# 2. Lógica de descripciones y etiquetas dinámicas
if modo == "Instituto":
    st.info("📚 **Análisis Académico:** Evalúa si el esfuerzo realizado en tareas compensa la presión de exámenes inminentes.")
    l1, l2 = "✍️ Deberes Completados", "📅 Proximidad del Examen"
    txt_ok, txt_risk, txt_fail = "Libertad total.", "Riesgo de suspenso.", "Estudio obligatorio."

elif modo == "Banco":
    st.info("🏦 **Riesgo Financiero:** Cálculo de solvencia para préstamos basado en liquidez frente a deuda acumulada.")
    l1, l2 = "💰 Ahorros Disponibles", "💸 Deudas / Créditos"
    txt_ok, txt_risk, txt_fail = "Préstamo aprobado.", "Aval adicional requerido.", "Riesgo de impago alto."

elif modo == "Supervivencia Zombie":
    st.info("🧟 **Protocolo de Supervivencia:** Probabilidad de éxito en combate cuerpo a cuerpo según fatiga y distancia del enemigo.")
    l1, l2 = "🔋 Energía Física", "⚠️ Distancia del Zombie"
    txt_ok, txt_risk, txt_fail = "Victoria asegurada.", "Huye si puedes.", "Muerte inminente."

elif modo == "Citas / Amistad":
    st.info("❤️ **Social Dynamics:** Predice el éxito de una salida o declaración basándose en química y 'red flags'.")
    l1, l2 = "✨ Interés Percibido", "🚩 Señales de Alerta"
    txt_ok, txt_risk, txt_fail = "Conexión total.", "Zona de amistad/duda.", "Rechazo detectado."

else: # Deportes
    st.info("🏆 **Rendimiento Deportivo:** Probabilidad de ganar el partido según tu forma física y el nivel del rival.")
    l1, l2 = "💪 Tu Forma Física", "🔥 Nivel del Oponente"
    txt_ok, txt_risk, txt_fail = "Campeón indiscutible.", "Partido reñido.", "Derrota técnica."

# 3. Sliders
col1, col2 = st.columns(2)
with col1:
    v1 = st.
