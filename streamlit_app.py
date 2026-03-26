import streamlit as st
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Nexus AI - El Oráculo", page_icon="🧠")

# --- MINI PESTAÑA DE AYUDA ---
with st.expander("❓ ¿Cómo usar a Nexus? (Guía de Rangos)"):
    st.write("""
    **Niveles de Nexus:**
    * **90% - 100%:** ¡Libertad total!
    * **70% - 89%:** Buen camino, tienes permiso.
    * **50% - 69%:** Zona gris, haz algo más.
    * **0% - 49%:** ¡A trabajar!
    
    *Ejemplo: Si pones Deberes en 0.8 y Exámenes en 0.2, verás una probabilidad realista.*
    """)

# --- MOTOR DE LA IA (Pesos suavizados para ver más variedad) ---
def sigmoid(x): return 1 / (1 + np.exp(-x))

# Pesos ajustados para que la curva no sea tan radical
W0 = np.array([[-2.5, -1.5, 1.2, 2.0], [-2.4, -1.6, 1.3, 1.9]])
W1 = np.array([[-3.5], [-1.8], [1.7], [3.2]])

st.title("🧠 Nexus AI: Tu Decisor Inteligente")
st.write("Analizando variables para optimizar tu tiempo...")

st.divider()

# Sliders para entrada de datos
col1, col2 = st.columns(2)
with col1:
    v1 = st.slider("😇 Nivel de Deberes", 0.0, 1.0, 0.5)
with col2:
    v2 = st.slider("📚 Presión de Exámenes", 0.0, 1.0, 0.5)

if st.button("🔥 CONSULTAR A NEXUS", use_container_width=True):
    # Cálculo de la IA
    entrada = np.array([v1, v2])
    l1 = sigmoid(np.dot(entrada, W0))
    pred = sigmoid(np.dot(l1, W1))[0]
    prob = float(pred * 100)
    
    st.divider()
    
    # --- RANGOS Y FRASES GENERALES ---
    if prob >= 90:
        st.balloons()
        st.success(f"### RESULTADO: {prob:.1f}%")
        st.subheader("🟢 RANGO: EXCELENCIA")
        st.write("**Frase de Nexus:** 'Tu situación es óptima. Los datos indican que puedes ignorar tus responsabilidades un rato sin consecuencias.'")
        
    elif prob >= 70:
        st.success(f"### RESULTADO: {prob:.1f}%")
        st.subheader("🔵 RANGO: APROBADO SEGURO")
        st.write("**Frase de Nexus:** 'Vas por buen camino. Tienes un margen de confianza alto para descansar o jugar.'")
        
    elif prob >= 50:
        st.warning(f
