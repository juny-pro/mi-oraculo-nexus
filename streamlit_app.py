import streamlit as st
import numpy as np
import random

# Configuración de la página
st.set_page_config(page_title="Nexus AI - Multiverso Pro", page_icon="♾️")

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# --- MOTOR NEURAL (Ajustado para máximo rigor y caos de decimales) ---
W0 = np.array([[-6.8, -4.2, 3.5, 5.2], [-7.5, -5.8, 4.0, 6.5]])
W1 = np.array([[-13.2], [-6.1], [5.2], [10.8]])

st.title("♾️ Nexus AI: El Oráculo Multiverso")

# 1. Selector de Escenario Expandido
modo = st.selectbox(
    "Selecciona el plano de realidad a consultar:",
    ("Instituto", "Banco", "Supervivencia Zombie", "Citas / Amistad", "Deportes", "Inversión Cripto", "Cocina Extrema")
)

st.divider()

# 2. Lógica de descripciones y etiquetas dinámicas
if modo == "Instituto":
    st.info("📚 **Análisis Académico:** Evalúa si el esfuerzo en tareas compensa la presión de exámenes.")
    l1, l2 = "✍️ Deberes Completados", "📅 Proximidad del Examen"
    txt_ok, txt_risk, txt_fail = "Libertad total.", "Riesgo de suspenso.", "Estudio obligatorio."

elif modo == "Banco":
    st.info("🏦 **Riesgo Financiero:** Cálculo de solvencia basado en liquidez frente a deuda acumulada.")
    l1, l2 = "💰 Ahorros Disponibles", "💸 Deudas / Créditos"
    txt_ok, txt_risk, txt_fail = "Préstamo aprobado.", "Aval adicional requerido.", "Riesgo de impago alto."

elif modo == "Supervivencia Zombie":
    st.info("🧟 **Protocolo de Supervivencia:** Probabilidad de éxito según fatiga y distancia del enemigo.")
    l1, l2 = "🔋 Energía Física", "⚠️ Distancia del Zombie"
    txt_ok, txt_risk, txt_fail = "Victoria asegurada.", "Huye si puedes.", "Muerte inminente."

elif modo == "Citas / Amistad":
    st.info("❤️ **Social Dynamics:** Predice el éxito de una salida basado en química y alertas.")
    l1, l2 = "✨ Interés Percibido", "🚩 Señales de Alerta"
    txt_ok, txt_risk, txt_fail = "Conexión total.", "Zona de duda.", "Rechazo detectado."

elif modo == "Inversión Cripto":
    st.info("🪙 **Crypto Oracle:** Probabilidad de 'To the Moon' basada en FOMO y caída del mercado.")
    l1, l2 = "📈 Tu Inversión", "📉 Caída del Mercado (Crash)"
    txt_ok, txt_risk, txt_fail = "¡Ganancias masivas!", "Hold con miedo.", "Liquidación total."

elif modo == "Cocina Extrema":
    st.info("🍳 **Chef Neural:** ¿Será comestible o acabarás en el hospital?")
    l1, l2 = "🧂 Calidad de Ingredientes", "🔥 Nivel de Distracción"
    txt_ok, txt_risk, txt_fail = "Plato de 5 estrellas.", "Sabe raro pero se come.", "Llama a emergencias."

else: # Deportes
    st.info("🏆 **Rendimiento Deportivo:** Probabilidad de ganar según tu forma y el rival.")
    l1, l2 = "💪 Tu Forma Física", "🔥 Nivel del Oponente"
    txt_ok, txt_risk, txt_fail = "Campeón indiscutible.", "Partido reñido.", "Derrota técnica."

# 3. Sliders
col1, col2 = st.columns(2)
with col1:
    v1 = st.slider(l1, 0.0, 1.0, 0.5)
with col2:
    val_neg = st.slider(l2, 0.0, 1.0, 0.5)
    v2 = 1.0 - val_neg # Inversión lógica

# 4. Procesamiento
if st.button("🧠 PROCESAR ENTRADAS"):
    # Ruido para evitar la perfección
    variacion = random.uniform(-0.012, 0.012)
    
    entrada = np.array([v1, v2])
    layer1 = sigmoid(np.dot(entrada, W0))
    pred = (sigmoid(np.dot(layer1, W1))[0]) + variacion
    prob = max(0.000001, min(99.999999, float(pred * 100)))
    
    st.divider()
    
    # 5. Resultados con decimales crudos
    if prob >= 82.5:
        st.balloons()
        st.success(f"### PROBABILIDAD: {prob:.6f}%")
        st.write(f"**Veredicto:** {txt_ok}")
    elif prob >= 38.0:
        st.warning(f"### PROBABILIDAD: {prob:.6f}%")
        st.write(f"**Veredicto:** {txt_risk}")
    else:
        st.error(f"### PROBABILIDAD: {prob:.6f}%")
        st.write(f"**Veredicto:** {txt_fail}")

st.divider()
st.caption(f"Nexus Engine v13.5 | Modo: {modo} | Datos sin redondear")
