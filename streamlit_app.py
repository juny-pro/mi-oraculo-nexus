import streamlit as st
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Nexus AI Multi-Modo", page_icon="🌐")

# --- LÓGICA DE LA IA ---
def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# Pesos equilibrados para que no dé siempre 100%
W0 = np.array([[-2.5, -1.5, 1.2, 2.0], [-2.4, -1.6, 1.3, 1.9]])
W1 = np.array([[-3.5], [-1.8], [1.7], [3.2]])

# --- INTERFAZ ---
st.title("🌐 Nexus AI: El Oráculo Multiverso")
st.write("Selecciona un escenario y deja que la red neuronal analice tus posibilidades.")

# Selector de modo
modo = st.selectbox(
    "¿Qué quieres consultar hoy?",
    ("Instituto: ¿Puedo jugar?", "Banco: ¿Me dan el préstamo?", "Supervivencia: ¿Ataco al Zombie?")
)

st.divider()

# Configuración según el modo elegido
if modo == "Instituto: ¿Puedo jugar?":
    label_1, label_2 = "😇 Deberes hechos", "📚 Exámenes cerca"
    ayuda = "0 = Nada hecho, 1 = Todo perfecto."
elif modo == "Banco: ¿Me dan el préstamo?":
    label_1, label_2 = "💰 Ahorros en cuenta", "💼 Estabilidad laboral"
    ayuda = "0 = Pobreza, 1 = Millonario/Trabajo fijo."
else:
    label_1, label_2 = "🔋 Energía/Vida", "⚔️ Calidad del arma"
    ayuda = "0 = Débil, 1 = Guerrero Legendario."

# Sliders dinámicos
col1, col2 = st.columns(2)
with col1:
    v1 = st.slider(label_1, 0.0, 1.0, 0.5, help=ayuda)
with col2:
    v2 = st.slider(label_2, 0.0, 1.0, 0.5)

if st.button("🔥 CONSULTAR A NEXUS", use_container_width=True):
    # Cálculo
    entrada = np.array([v1, v2])
    l1 = sigmoid(np.dot(entrada, W0))
    pred = sigmoid(np.dot(l1, W1))[0]
    prob = float(pred * 100)
    
    st.divider()
    
    # --- RESULTADOS PERSONALIZADOS POR RANGO ---
    if prob >= 90:
        st.balloons()
        st.success(f"### RESULTADO: {prob:.1f}% - EXCELENCIA")
        if modo == "Instituto: ¿Puedo jugar?": fr = "¡Libertad total! Vete a jugar ya."
        elif modo == "Banco: ¿Me dan el préstamo?": fr = "Préstamo concedido. Eres cliente VIP."
        else: fr = "¡Victoria fácil! Lo vas a destrozar."
        
    elif prob >= 65:
        st.info(f"### RESULTADO: {prob:.1f}% - FAVORABLE")
        if modo == "Instituto: ¿Puedo jugar?": fr = "Tienes permiso, pero no te pases con las horas."
        elif modo == "Banco: ¿Me dan el préstamo?": fr = "Aprobado, pero con intereses estándar."
        else: fr = "Ganarás, pero saldrás con alguna herida."
        
    elif prob >= 40:
        st.warning(f"### RESULTADO: {prob:.1f}% - RIESGO MODERADO")
        if modo == "Instituto: ¿Puedo jugar?": fr = "Haz una tarea más y vuelve a preguntarme."
        elif modo == "Banco: ¿Me dan el préstamo?": fr = "Necesitamos que alguien te avale."
        else: fr = "Mejor huye. Tienes un 50/50 de morir."
        
    else:
        st.error(f"### RESULTADO: {prob:.1f}% - DENEGADO")
        if modo == "Instituto: ¿Puedo jugar?": fr = "¡Ponte a estudiar ahora mismo!"
        elif modo == "Banco: ¿Me dan el préstamo?": fr = "Operación rechazada. No tienes fondos."
        else: fr = "Muerte segura. No te acerques a ese zombie."

    st.subheader(f"💬 Nexus dice: {fr}")

st.divider()
st.caption("Nexus AI v9.0 | Multiverso Neural")
