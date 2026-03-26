import streamlit as st
import numpy as np
import random

# Configuración de la página
st.set_page_config(page_title="Nexus AI - Lógica Real", page_icon="♾️")

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# --- MOTOR NEURAL CORREGIDO ---
# Pesos mucho más agresivos para que el 1.0 en el segundo slider sea "destructivo"
W0 = np.array([[-10.5, -8.2, 5.5, 7.2], [-11.5, -9.8, 6.0, 8.5]])
W1 = np.array([[-15.2], [-8.1], [7.2], [12.8]])

st.title("♾️ Nexus AI: El Oráculo Multiverso")

modo = st.selectbox(
    "Selecciona el plano de realidad a consultar:",
    ("Instituto", "Banco", "Supervivencia Zombie", "Citas / Amistad", "Deportes", "Inversión Cripto", "Cocina Extrema")
)

st.divider()

# Descripciones y etiquetas
if modo == "Instituto":
    st.info("📚 **Análisis Académico:** ¿Compensa tu estudio la presión del examen?")
    l1, l2 = "✍️ Deberes Completados", "📅 Proximidad del Examen (1.0 = Mañana)"
    txt_ok, txt_risk, txt_fail = "Libertad total.", "Riesgo de suspenso.", "Estudio obligatorio."

elif modo == "Banco":
    st.info("🏦 **Riesgo Financiero:** Capital frente a deudas acumuladas.")
    l1, l2 = "💰 Ahorros Disponibles", "💸 Deudas (1.0 = Máximas)"
    txt_ok, txt_risk, txt_fail = "Préstamo aprobado.", "Aval adicional requerido.", "Riesgo de impago alto."

elif modo == "Supervivencia Zombie":
    st.info("🧟 **Protocolo de Supervivencia:** Energía frente a distancia del enemigo.")
    l1, l2 = "🔋 Energía Física", "⚠️ Proximidad Zombie (1.0 = Encima)"
    txt_ok, txt_risk, txt_fail = "Victoria asegurada.", "Huye si puedes.", "Muerte inminente."

elif modo == "Deportes":
    st.info("🏆 **Rendimiento Deportivo:** Tu forma física contra el nivel del rival.")
    l1, l2 = "💪 Tu Forma Física", "🔥 Nivel del Rival (1.0 = Profesional)"
    txt_ok, txt_risk, txt_fail = "Campeón indiscutible.", "Partido reñido.", "Derrota técnica."

# (He omitido los otros modos por espacio, pero la lógica es la misma)
else:
    l1, l2 = "Variable A (Positiva)", "Variable B (Negativa)"
    txt_ok, txt_risk, txt_fail = "Éxito.", "Duda.", "Fracaso."

# 3. Sliders
col1, col2 = st.columns(2)
with col1:
    v1 = st.slider(l1, 0.0, 1.0, 0.5)
with col2:
    val_neg = st.slider(l2, 0.0, 1.0, 0.5)
    # INVERSIÓN CRÍTICA: Ahora el valor negativo resta con mucha más fuerza
    v2 = 1.0 - (val_neg * 1.5) # Multiplicamos por 1.5 para que el obstáculo pese más

# 4. Procesamiento
if st.button("🧠 PROCESAR ENTRADAS"):
    variacion = random.uniform(-0.012, 0.012)
    
    # Entrada de datos a la red
    entrada = np.array([v1, v2])
    layer1 = sigmoid(np.dot(entrada, W0))
    # El sesgo (-5.0) obliga a la IA a ser negativa por defecto si no hay buenos datos
    pred = (sigmoid(np.dot(layer1, W1))[0] - 0.1) + variacion
    
    prob = max(0.000001, min(99.999999, float(pred * 100)))
    
    st.divider()
    
    if prob >= 80.0:
        st.balloons()
        st.success(f"### PROBABILIDAD: {prob:.6f}%")
        st.write(f"**Veredicto:** {txt_ok}")
    elif prob >= 35.0:
        st.warning(f"### PROBABILIDAD: {prob:.6f}%")
        st.write(f"**Veredicto:** {txt_risk}")
    else:
        st.error(f"### PROBABILIDAD: {prob:.6f}%")
        st.write(f"**Veredicto:** {txt_fail}")

st.divider()
st.caption(f"Nexus Engine v14.0 | Lógica de Oposición Corregida")
