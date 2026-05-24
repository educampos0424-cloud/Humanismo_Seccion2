import streamlit as st
import pandas as pd
import altair as alt
import os

# Configuración inicial de la página
st.set_page_config(
    page_title="El Conocimiento Sentipensante",
    page_icon="🧠",
    layout="wide"
)

# Estilos personalizados premium con Glassmorphism y Gradientes
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    /* Ocultar la barra superior por completo */
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Ajustar espaciado superior al remover la barra */
    [data-testid="stMainBlockContainer"] {
        padding-top: 2.5rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Configuración de fuentes y fondo general */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
        color: #f1f5f9;
    }
    
    [data-testid="stSidebar"] {
        background-color: #090d16 !important;
        border-right: 1px solid #1e293b;
    }
    
    /* Resaltar títulos y encabezados */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    
    /* Título Principal */
    .glow-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding-top: 10px;
        margin-bottom: 5px;
        text-shadow: 0 0 40px rgba(168, 85, 247, 0.3);
    }
    
    .glow-subtitle {
        font-size: 1.3rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 35px;
        font-weight: 500;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    
    /* Subtítulos de sección (st.subheader / h3) */
    h3 {
        color: #38bdf8 !important; /* Celeste brillante */
        font-size: 1.7rem !important;
        margin-top: 2.2rem !important;
        margin-bottom: 1.2rem !important;
        border-left: 4px solid #a855f7; /* Borde morado destacado */
        padding-left: 12px !important;
        line-height: 1.35 !important;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
    }
    
    /* Encabezados en tarjetas (h4) */
    h4 {
        color: #f8fafc !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        margin-top: 0.8rem !important;
        margin-bottom: 0.8rem !important;
    }
    
    /* Otros títulos (h5) */
    h5 {
        color: #a855f7 !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-top: 1.2rem !important;
        margin-bottom: 0.8rem !important;
    }
    
    /* Estilos premium para el texto de todo el contenido */
    p, li, .stMarkdown p, .stMarkdown li {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.1rem !important;
        line-height: 1.8 !important;
        color: #cbd5e1 !important; /* Gris claro (slate-300) muy agradable a la vista */
        font-weight: 400 !important;
    }
    
    /* Color de la letra negro para las opciones del menú desplegable (Selectbox) */
    div[role="listbox"] li,
    div[role="listbox"] li *,
    [data-baseweb="popover"] li,
    [data-baseweb="popover"] li *,
    [data-baseweb="menu"] li,
    [data-baseweb="menu"] li *,
    ul[role="listbox"] li,
    ul[role="listbox"] li *,
    div[role="option"],
    div[role="option"] * {
        color: #000000 !important;
    }
    
    /* Resaltar negritas en todo el texto */
    strong, b {
        color: #f1f5f9 !important; /* Blanco brillante (slate-100) */
        font-weight: 700 !important;
    }
    
    /* Estilos para etiquetas de controles interactivos (ej: preguntas de radio/selectores) */
    label, .stRadio label, .stSelectbox label, .stTextInput label {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 600 !important;
        color: #f1f5f9 !important;
        font-size: 1.1rem !important;
    }
    
    /* Tarjetas Glassmorphism */
    .glass-card {
        background: rgba(30, 41, 59, 0.45);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 28px;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        margin-bottom: 25px;
        transition: transform 0.3s ease, border 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-2px);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    
    /* Sobrescribir estilos específicos para h3/p dentro de glass-card */
    .glass-card h3 {
        color: #c084fc !important;
        border-left: none !important;
        padding-left: 0 !important;
        margin-top: 0 !important;
        text-shadow: none !important;
    }
    
    .glass-card p {
        font-size: 1.15rem !important;
        line-height: 1.7 !important;
    }
    
    /* Bordes de neón para destacar */
    .neon-border-red {
        border-left: 6px solid #f43f5e;
    }
    
    .neon-border-cyan {
        border-left: 6px solid #06b6d4;
    }
    
    .neon-border-purple {
        border-left: 6px solid #a855f7;
    }
    
    .neon-border-green {
        border-left: 6px solid #10b981;
    }
    
    /* Estilo del pie de página */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 60px;
        padding-bottom: 20px;
    }
    
    /* Botones y radio interactivos */
    .stRadio > div {
        flex-direction: row;
        gap: 15px;
    }
    
    /* Caja de citas */
    .quote-box {
        font-style: italic;
        color: #38bdf8;
        border-left: 4px solid #38bdf8;
        padding-left: 18px;
        margin: 20px 0;
        font-size: 1.15rem;
        background: rgba(56, 189, 248, 0.05);
        padding: 12px 18px;
        border-radius: 0 8px 8px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar estados de la sesión para interactividad persistente
if 'voted_pill' not in st.session_state:
    st.session_state.voted_pill = None
if 'votes_pill_data' not in st.session_state:
    # Votos iniciales simulados
    st.session_state.votes_pill_data = {'Pastilla (Fácil)': 45, 'Dificultad (Real)': 135}
if 'commitments' not in st.session_state:
    st.session_state.commitments = []

# Barra lateral de navegación
st.sidebar.markdown("<h2 style='text-align: center; color: #a855f7;'>Navigation 🧠</h2>", unsafe_allow_html=True)
section = st.sidebar.radio(
    "Ir a la sección:",
    ["🏠 Inicio", "💡 El Dilema", "📌 Introducción y Ética", "✊ Tesis y Argumentos", "🎮 Simulador de Decisiones", "🏁 Conclusión y Cierre"],
    index=0
)

st.sidebar.divider()
st.sidebar.markdown(
    """
    <div style='text-align: center; font-size: 0.8rem; color: #64748b;'>
        <strong>Humanismo, Sociedad y Ética</strong><br>
        Sección 2 - Bitácora Interactiva
    </div>
    """,
    unsafe_allow_html=True
)

# Título Principal común a todas las secciones (excepto en Inicio)
if section != "🏠 Inicio":
    st.markdown('<div class="glow-title">El Conocimiento Sentipensante</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Rompiendo la Burbuja Intelectual • Humanismo, Sociedad y Ética</div>', unsafe_allow_html=True)
    st.divider()

# ==============================================================================
# SECCIÓN DE BIENVENIDA: INICIO
# ==============================================================================
if section == "🏠 Inicio":
    st.markdown(
        """<div class="glass-card" style="text-align: center; padding: 50px 30px; margin-top: 10px; border: 1px solid rgba(255, 255, 255, 0.15);">
<div style="font-size: 4rem; margin-bottom: 20px;">🎓</div>
<h1 style="font-size: 2.8rem !important; font-weight: 800 !important; background: linear-gradient(135deg, #38bdf8 0%, #a855f7 100%); -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; margin-bottom: 10px !important; letter-spacing: -0.02em; text-shadow: none !important;">Humanismo, Sociedad y Ética</h1>
<h3 style="font-size: 1.5rem !important; color: #94a3b8 !important; font-weight: 500 !important; margin-top: 0 !important; margin-bottom: 40px !important; border-left: none !important; padding-left: 0 !important; text-shadow: none !important;">Relación entre hombre y sociedad</h3>
<div style="display: flex; justify-content: center; gap: 40px; margin: 40px 0; flex-wrap: wrap;">
<div style="text-align: left; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 12px; min-width: 260px; border: 1px solid rgba(255,255,255,0.05);">
<span style="color: #a855f7; font-weight: 600; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em;">Elaborado por:</span>
<p style="font-size: 1.2rem !important; font-weight: 700 !important; color: #f1f5f9 !important; margin: 5px 0 0 0 !important;">Eduardo Campos Jiménez</p>
</div>
<div style="text-align: left; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 12px; min-width: 260px; border: 1px solid rgba(255,255,255,0.05);">
<span style="color: #38bdf8; font-weight: 600; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em;">Docente:</span>
<p style="font-size: 1.2rem !important; font-weight: 700 !important; color: #f1f5f9 !important; margin: 5px 0 0 0 !important;">Jorge Andrés Angarita Solano</p>
</div>
</div>
<div style="margin-top: 50px; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 30px;">
<p style="font-size: 1.3rem !important; font-weight: 600 !important; color: #f1f5f9 !important; letter-spacing: 0.05em;">UNIVERSIDAD SANTO TOMÁS</p>
<p style="font-size: 0.95rem !important; color: #64748b !important; margin-top: 5px !important;">Facultad de Humanidades • Decanatura de División de Universidad Abierta y a Distancia</p>
</div>
</div>""",
        unsafe_allow_html=True
    )

# ==============================================================================
# SECCIÓN 1: EL DILEMA
# ==============================================================================
elif section == "💡 El Dilema":
    st.subheader("💡 Para empezar: Un dilema de nuestro tiempo")
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.write(
            "Imagina que existe una tecnología o una pastilla capaz de darte una vida perfecta: "
            "sin filas, sin deudas, sin trancones, y con tu título universitario asegurado en la mano sin tener que abrir un solo libro."
        )
        
        opcion_pastilla = st.radio(
            "**¿Te la tomarías de inmediato?**",
            ["Selecciona una opción...", "¡Sí, de una! Deme dos.", "No, ni riesgos."],
            index=0
        )
        
        # Procesar decisión
        if opcion_pastilla != "Selecciona una opción...":
            if st.session_state.voted_pill is None:
                st.session_state.voted_pill = opcion_pastilla
                if opcion_pastilla == "¡Sí, de una! Deme dos.":
                    st.session_state.votes_pill_data['Pastilla (Fácil)'] += 1
                else:
                    st.session_state.votes_pill_data['Dificultad (Real)'] += 1
            
            if opcion_pastilla == "¡Sí, de una! Deme dos.":
                st.markdown(
                    """
                    <div class="glass-card neon-border-red">
                        <h4>🚨 ¡Caíste en la trampa!</h4>
                        Al elegir la comodidad absoluta, acabas de elegir lo que el filósofo 
                        <strong>Estanislao Zuleta</strong> llamaba un <em>'océano de mermelada sagrada'</em>. 
                        Cuando eliminamos las dificultades y los problemas de la vida, también extinguimos la necesidad 
                        de pensar, de desear y de construirnos como humanos. Nos volvemos dependientes y sumisos.
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            elif opcion_pastilla == "No, ni riesgos.":
                st.markdown(
                    """
                    <div class="glass-card neon-border-green">
                        <h4>🌱 ¡Excelente intuición crítica!</h4>
                        Has elegido el camino de la dificultad y la auto-superación. Como argumentaba 
                        <strong>Estanislao Zuleta</strong>, el verdadero crecimiento humano y la madurez radican en la 
                        capacidad de asumir la complejidad, el esfuerzo y la superación de nuestras propias contradicciones. 
                        Pensar duele, pero nos hace libres.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
    with col2:
        # Gráfico dinámico de las respuestas acumuladas en tiempo real
        if opcion_pastilla != "Selecciona una opción...":
            st.markdown("##### 📊 ¿Qué opina el público? (Votos en vivo)")
            df_votes = pd.DataFrame({
                'Decisión': list(st.session_state.votes_pill_data.keys()),
                'Votos': list(st.session_state.votes_pill_data.values())
            })
            
            chart = alt.Chart(df_votes).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
                x=alt.X('Decisión:N', axis=alt.Axis(labelAngle=0)),
                y='Votos:Q',
                color=alt.Color('Decisión:N', scale=alt.Scale(domain=['Pastilla (Fácil)', 'Dificultad (Real)'], range=['#f43f5e', '#10b981']), legend=None)
            ).properties(
                height=220
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("👈 Selecciona una respuesta para ver cómo afecta los votos en vivo y revelar la metáfora visual.")
            
    # Mostrar la imagen del océano de mermelada si ya votó
    if opcion_pastilla != "Selecciona una opción...":
        st.divider()
        st.subheader("🎨 Representación Conceptual: El Océano de Mermelada Sagrada")
        if os.path.exists("mermelada_sagrada.png"):
            st.image("mermelada_sagrada.png", caption="El Océano de Mermelada Sagrada — La trampa del confort absoluto sin retos ni pensamiento propio.", use_container_width=True)

# ==============================================================================
# SECCIÓN 2: INTRODUCCIÓN Y ÉTICA
# ==============================================================================
elif section == "📌 Introducción y Ética":
    st.subheader("📌 Introducción: La encrucijada de la educación y la ética")
    
    col1, col2 = st.columns([3, 2], gap="large")
    
    with col1:
        st.markdown(
            """
            <div class="glass-card neon-border-cyan">
                <h4>Fábrica de Especialistas de Escritorio</h4>
                La educación moderna corre el grave riesgo de convertirse en una fábrica de profesionales con 
                excelentes capacidades técnicas, pero completamente aislados de las realidades e injusticias del territorio donde habitan.
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.write(
            "Frente a esto, **la ética no puede ser un catálogo inerte de normas morales abstractas** o códigos de conducta "
            "para memorizar antes de un examen. La ética es la fuerza viva que vincula de manera indisoluble el destino del "
            "individuo con el bienestar y las luchas del tejido social."
        )
        
        with st.expander("🔍 Haz clic aquí para ver el núcleo de nuestra investigación"):
            st.info(
                "A través de esta bitácora interactiva, analizaremos cómo el intelectualismo, la filosofía de vida "
                "y el compromiso de un pueblo se entrelazan para transformar la teoría en una práctica de transformación real."
            )
            
    with col2:
        st.markdown("##### 🎥 Video Reflexivo: Investigación Acción Participativa")
        # Video educativo sobre Fals Borda y la IAP (método sentipensante)
        st.video("https://www.youtube.com/watch?v=68zC3G7jM3I")
        st.caption("Aportes de Orlando Fals Borda a la investigación en el territorio.")

# ==============================================================================
# SECCIÓN 3: TESIS Y ARGUMENTOS
# ==============================================================================
elif section == "✊ Tesis y Argumentos":
    st.subheader("✊ Nuestra Postura Crítica (Tesis)")
    
    st.markdown(
        """
        <div class="glass-card" style="background: rgba(168, 85, 247, 0.12); border: 1px solid rgba(168, 85, 247, 0.3);">
            <h3 style="color: #c084fc; margin-top: 0;">Nuestra Tesis</h3>
            <p style="font-size: 1.15rem; line-height: 1.6;">
                El ser humano no es un ente biológico aislado ni un robot procesador de datos. 
                <strong>El verdadero conocimiento y la ética se configuran y validan únicamente en el territorio.</strong> 
                Asumimos una posición radicalmente crítica frente al saber neutral y aséptico de oficina: la ciencia y la técnica 
                carecen de valor humano si no se nutren del compromiso con el pueblo y de la transformación activa de la realidad social.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.write("Defendemos esta postura a través de **tres argumentos fundamentales** basados en las lecturas:")
    
    # Pestañas interactivas de Streamlit
    tab1, tab2, tab3 = st.tabs([
        "🧠 Arg 1: Intelectualismo y Sentido Común", 
        "⏳ Arg 2: Filosofía de Vida (Zuleta)", 
        "❤️ Arg 3: Compromiso Sentipensante (Fals Borda)"
    ])
    
    with tab1:
        st.markdown("### Argumento 1: Descolonizar la Razón y valorar el Sentido Común")
        st.write(
            "**La crítica al dogma:** Históricamente, la academia nos ha vendido la idea de que la única ciencia válida "
            "es la que viene en libros del primer mundo, elaborada en laboratorios aislados y bajo métodos eurocéntricos."
        )
        st.markdown(
            """
            <div class="quote-box">
                "Todo ser humano es un filósofo en potencia." — Antonio Gramsci
            </div>
            """, unsafe_allow_html=True
        )
        st.write(
            "Las creencias, las vivencias y el 'sentido común' de la gente de a pie no constituyen ignorancia; "
            "representan núcleos de buen sentido y sabiduría popular indispensables para entender la realidad. La verdadera "
            "ética exige integrar el saber académico con el saber comunitario para desmontar las estructuras hegemónicas de opresión."
        )
        
        # Elemento sorpresa / curiosidad
        if st.checkbox("👁️ Revelar secreto sobre la ciencia neutral"):
            st.warning("⚠️ **Dato crítico:** La ciencia nunca es neutral; siempre responde a los intereses económicos, corporativos y de poder de la época.")

    with tab2:
        st.markdown("### Argumento 2: Elogio de la Dificultad contra el Dogmatismo")
        st.write(
            "**El peligro de los paraísos artificiales:** Las sociedades que caen en la trampa de buscar verdades absolutas, "
            "unanimidades y soluciones mágicas sin esfuerzo, terminan construyendo sistemas autoritarios, infiernos de intolerancia "
            "y un profundo estancamiento intelectual."
        )
        st.write(
            "**El respaldo conceptual (Estanislao Zuleta):** La vida es una *'autoproducción riesgosa en el tiempo'*. "
            "Asumir el humanismo y la ética implica abrazar la complejidad de la diferencia, dudar metódicamente de los discursos "
            "empaquetados y aceptar que la comunicación interhumana siempre es incompleta. Estudiar no es para volverse un técnico "
            "indiferente, sino para tener el valor de pensar por cuenta propia y cuestionar el orden establecido."
        )

    with tab3:
        st.markdown("### Argumento 3: El Intelectual Sentipensante y el Poder Popular")
        
        col_text, col_img = st.columns([5, 4], gap="medium")
        
        with col_text:
            st.write(
                "**El divorcio absurdo:** La herencia colonial ha fracturado al ser humano, separando la razón (la cabeza) "
                "de la emoción (el corazón), lo que produce profesionales sumisos e insensibles ante las crisis sociales."
            )
            st.write(
                "**El respaldo conceptual (Orlando Fals Borda):** A través de la *Investigación Acción Participativa (IAP)*, se plantea "
                "que la filosofía de vida del universitario debe ser convertirse en un sujeto **'sentipensante'**. Esto significa combinar "
                "el rigor de la ciencia con el corazón y la empatía por las luchas populares. El investigador no va a 'estudiar' a la "
                "comunidad como si fuera un objeto de laboratorio; se une a ella para co-crear conocimiento emancipador."
            )
        
        with col_img:
            if os.path.exists("sentipensante.png"):
                st.image("sentipensante.png", caption="Conocimiento Sentipensante — Razón científica articulada con sensibilidad social.", use_container_width=True)

# ==============================================================================
# SECCIÓN 4: SIMULADOR DE DECISIONES
# ==============================================================================
elif section == "🎮 Simulador de Decisiones":
    st.subheader("🎮 Actividad Interactiva: El simulador de decisiones éticas")
    
    st.markdown(
        """
        <div class="glass-card neon-border-purple">
            <strong>El Caso:</strong> Una comunidad rural en Colombia sufre por falta de acceso a agua potable. 
            Un grupo de ingenieros extranjeros diseña un software de distribución automatizada de alta tecnología sin consultar 
            a los líderes locales. La comunidad rechaza el sistema porque altera sus sistemas comunitarios tradicionales de 
            organización del territorio.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.write("**Como profesional ético y humanista de esta universidad, ¿qué decisión tomarías?**")
    
    decision = st.selectbox(
        "Elige tu acción:",
        [
            "Selecciona una estrategia...",
            "A) Imponer el software argumentando que la opinión técnica es superior a la tradición popular.",
            "B) Retirarte del proyecto alegando que la comunidad es ignorante y no quiere progresar.",
            "C) Sentarte con la comunidad, aplicar la IAP, valorar su saber local y rediseñar el sistema juntos."
        ]
    )
    
    if decision.startswith("A)"):
        st.error("❌ **Resultado desastroso:** Caíste en el colonialismo intelectual. Priorizaste la técnica fría sobre el tejido social. La comunidad boicoteará el software y el problema del agua continuará.")
    elif decision.startswith("B)"):
        st.error("❌ **Resultado apático:** Adoptaste una postura cobarde e indiferente, traicionando la responsabilidad ética e histórica del universitario frente a su pueblo.")
    elif decision.startswith("C)"):
        st.success("🎉 **¡Excelente decisión sentipensante!** Has derribado el muro entre investigador e investigado. Al fusionar la ciencia técnica con la sabiduría y organización del pueblo, la solución será sostenible, justa y liberadora. ¡Fals Borda estaría orgulloso!")
        st.balloons()  # Efecto sorpresa
        st.snow()      # Efecto sorpresa complementario

# ==============================================================================
# SECCIÓN 5: CONCLUSIÓN Y CIERRE
# ==============================================================================
elif section == "🏁 Conclusión y Cierre":
    st.subheader("🏁 Conclusión: Hacia una ética enraizada en la realidad")
    
    st.markdown(
        """
        <div class="glass-card neon-border-cyan">
            <ul>
                <li><strong>Dialéctica Hombre-Sociedad:</strong> No podemos realizarnos como individuos plenos si ignoramos la estructura social, la historia y el territorio que nos sostiene. La individualidad sin comunidad es un espejismo alienante.</li>
                <li><strong>El verdadero Humanismo:</strong> No reside en acumular diplomas académicos en la pared ni en dictar discursos morales impecables. El humanismo es <em>praxis</em>: la capacidad real de poner la ciencia y la técnica al servicio de la emancipación colectiva.</li>
                <li><strong>El legado ético permanente:</strong> Ser fieles a los aportes de Zuleta, Fals Borda y Gramsci implica rechazar con rebeldía las verdades empaquetadas, amar la dificultad que trae la diferencia y asumir el compromiso inquebrantable de caminar, pensar y sentir junto al pueblo.</li>
            </ul>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.divider()
    
    # Capturar la opinión del público de forma dinámica
    st.subheader("💬 Deja aquí tu propio compromiso sentipensante")
    new_commitment = st.text_input("Escribe tu compromiso como profesional frente a la sociedad:")
    
    if st.button("Enviar Compromiso 🚀"):
        if new_commitment.strip() != "":
            st.session_state.commitments.append(new_commitment)
            st.toast("¡Tu compromiso ha sido guardado exitosamente!", icon="🌱")
            st.success("¡Gracias por tu reflexión!")
        else:
            st.warning("Escribe algo antes de presionar el botón.")
            
    if st.session_state.commitments:
        st.write("**Compromisos compartidos de la clase (Simulado en sesión):**")
        for i, c in enumerate(st.session_state.commitments[::-1], 1):
            st.info(f"Reflexión #{i}: \"{c}\"")
            
    st.divider()
    
    # Cierre y referencias
    st.markdown("<p style='text-align: center; font-style: italic; font-size: 1.2rem; color: #38bdf8;'>\"La ciencia no es neutral, y el científico tampoco debe serlo ante la injusticia.\"</p>", unsafe_allow_html=True)
    
    with st.expander("📚 Referencias del Material de Estudio"):
        st.caption("- Zuleta, E. — *Elogio de la dificultad y otros ensayos*")
        st.caption("- Rincón Díaz, J. A. — *La Investigación Acción Participativa como filosofía de vida del intelectual crítico* (Aportes de Orlando Fals Borda)")
        st.caption("- Gramsci, A. — *El sentido común y la formación del intelectual*")

# Pie de página general
st.markdown('<div class="footer">Desarrollado en Streamlit con enfoque humano y crítico • 2026</div>', unsafe_allow_html=True)
