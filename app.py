import streamlit as st

# Configuración inicial de la página estilo web interactiva
st.set_page_config(
    page_title="El Conocimiento Sentipensante",
    page_icon="🧠",
    layout="centered"
)

# Estilos personalizados para darle un toque "humanizado" y limpio
st.markdown("""
    <style>
    .main-title {
        font-size: 2.6rem;
        color: #1A365D;
        text-align: center;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #4A5568;
        text-align: center;
        margin-bottom: 30px;
    }
    .postura-box {
        background-color: #F7FAFC;
        border-left: 5px solid #E53E3E;
        padding: 20px;
        border-radius: 4px;
        margin-bottom: 25px;
    }
    .footer {
        text-align: center;
        color: #A0AEC0;
        font-size: 0.8rem;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# PANTALLA 1: PORTADA PRINCIPAL
# ==============================================================================
st.markdown('<div class="main-title">El Conocimiento Sentipensante</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Rompiendo la Burbuja Intelectual • Humanismo, Sociedad y Ética</div>', unsafe_allow_html=True)
st.divider()

# ==============================================================================
# PANTALLA 2: EL ANZUELO DINÁMICO (Elemento sorpresa / Curiosidad)
# ==============================================================================
st.subheader("💡 Para empezar: Un dilema de nuestro tiempo")
st.write(
    "Imagina que existe una tecnología o una pastilla capaz de darte una vida perfecta: "
    "sin filas, sin deudas, sin trancones y con tu título universitario asegurado en la mano sin tener que abrir un solo libro."
)

# Encuesta interactiva en tiempo real
opcion_pastilla = st.radio(
    "**¿Te la tomarías de inmediato?**",
    ["Selecciona una opción...", "¡Sí, de una! Deme dos.", "No, ni riesgos."],
    index=0
)

if opcion_pastilla == "¡Sí, de una! Deme dos.":
    st.error(
        "🚨 **¡Caíste en la trampa!** Al elegir la comodidad absoluta, acabas de elegir lo que el filósofo "
        "**Estanislao Zuleta** llamaba un *'océano de mermelada sagrada'*. Cuando eliminamos las dificultades y "
        "los problemas de la vida, también extinguimos la necesidad de pensar, de desear y de construirnos como humanos. "
        "Nos volvemos dependientes y sumisos."
    )
elif opcion_pastilla == "No, ni riesgos.":
    st.success(
        "🌱 **¡Excelente intuición crítica!** Has elegido el camino de la dificultad. Como argumentaba "
        "**Estanislao Zuleta**, el verdadero crecimiento humano y la madurez radican en la capacidad de asumir la "
        "complejidad, el esfuerzo y la superación de nuestras propias contradicciones. Pensar duele, pero nos hace libres."
    )

st.divider()

# ==============================================================================
# PANTALLA 3: INTRODUCCIÓN FORMAL
# ==============================================================================
st.subheader("📌 Introducción: La encrucijada de la educación y la ética")
st.write(
    "La educación moderna corre el grave riesgo de convertirse en una fábrica de especialistas de escritorio. "
    "Profesionales con excelentes capacidades técnicas, pero completamente aislados de las realidades e injusticias "
    "del territorio donde habitan."
)
st.write(
    "Frente a esto, **la ética no puede ser un catálogo inerte de normas morales abstractas** o códigos de conducta "
    "para memorizar antes de un examen. La ética es la fuerza viva que vincula de manera indisoluble el destino del "
    "individmo con el bienestar y las luchas del tejido social."
)

with st.expander("🔍 Haz clic aquí para ver el núcleo de nuestra investigación"):
    st.info(
        "A través de esta bitácora interactiva, analizaremos cómo el intelectualismo, la filosofía de vida "
        "y el compromiso de un pueblo se entrelazan para transformar la teoría en una práctica de transformación real."
    )

st.divider()

# ==============================================================================
# PANTALLA 4: TESIS CENTRAL Y POSTURA CRÍTICA
# ==============================================================================
st.subheader("✊ Nuestra Postura Crítica (Tesis)")

st.markdown(
    """
    <div class="postura-box">
        <strong>Sostenemos que:</strong> El ser humano no es un ente biológico aislado ni un robot procesador de datos. 
        <strong>El verdadero conocimiento y la ética se configuran y validan únicamente en el territorio.</strong> 
        Asumimos una posición radicalmente crítica frente al saber neutral y aséptico de oficina: la ciencia y la técnica 
        carecen de valor humano si no se nutren del compromiso con el pueblo y de la transformación activa de la realidad social.
    </div>
    """, 
    unsafe_allow_html=True
)

st.write("Defendemos esta postura a través de **tres argumentos fundamentales** basados en las lecturas:")

# Uso de pestañas de Streamlit para organizar la información de manera secuencial y lógica
tab1, tab2, tab3 = st.tabs([
    "🧠 Arg 1: Intelectualismo y Sentido Común", 
    "⏳ Arg 2: Filosofía de Vida", 
    "❤️ Arg 3: Compromiso del Pueblo"
])

# ==============================================================================
# PANTALLA 5: ARGUMENTO 1
# ==============================================================================
with tab1:
    st.markdown("### Argumento 1: Descolonizar la Razón y valorar el Sentido Común")
    st.write(
        "**La crítica al dogma:** Históricamente, la academia nos ha vendido la idea de que la única ciencia válida "
        "es la que viene en libros del primer mundo, elaborada en laboratorios aislados y bajo métodos eurocéntricos."
    )
    st.write(
        "**El respaldo conceptual (Antonio Gramsci):** Todo ser humano es un filósofo en potencia. Las creencias, las "
        "vivencias y el 'sentido común' de la gente de a pie no constituyen ignorancia; representan núcleos de buen sentido "
        "y sabiduría popular indispensables para entender la realidad. La verdadera ética exige integrar el saber académico "
        "con el saber comunitario para desmontar las estructuras hegemónicas de opresión."
    )
    
    # Elemento sorpresa / Curiosidad dentro del tab
    if st.checkbox("👁️ Revelar mensaje oculto sobre la ciencia neutral"):
        st.warning("⚠️ **Dato crítico:** La ciencia nunca es neutral; siempre responde a los intereses económicos y de poder de la época.")

# ==============================================================================
# PANTALLA 6: ARGUMENTO 2
# ==============================================================================
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

# ==============================================================================
# PANTALLA 7: ARGUMENTO 3
# ==============================================================================
with tab3:
    st.markdown("### Argumento 3: El Intelectual Sentipensante y el Poder Popular")
    st.write(
        "**El divorcio absurdo:** La herencia colonial ha fracturado al ser humano, separando la razón (la cabeza) "
        "de la emoción (el corazón), lo que produce profesionales sumisos e insensibles ante las crisis sociales."
    )
    st.write(
        "**El respaldo conceptual (Orlando Fals Borda):** A través de la *Investigación Acción Participativa (IAP)*, se plantea "
        "que la filosofía de vida del universitario debe ser convertirse en un sujeto **'sentipensante'**. Esto significa combinar "
        "el rigor de la ciencia con el corazón y la empatía por las luchas populares. El investigador no va a 'estudiar' a la "
        "comunidad como si fuera un objeto de laboratorio; se une a ella para co-crear conocimiento emancipador y generar "
        "poder popular."
    )

st.divider()

# ==============================================================================
# PANTALLA 8: GAMIFICACIÓN / ACTIVIDAD DEL PÚBLICO (Simulador ético)
# ==============================================================================
st.subheader("🎮 Actividad Interactiva: El simulador de decisiones éticas")
st.write(
    "**El Caso:** Una comunidad rural en Colombia sufre por falta de acceso a agua potable. "
    "Un grupo de ingenieros extranjeros diseña un software de distribución automatizada de alta tecnología sin consultar "
    "a los líderes locales. La comunidad rechaza el sistema porque altera sus sistemas comunitarios tradicionales de "
    "organización del territorio."
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

st.divider()

# ==============================================================================
# PANTALLA 9: CONCLUSIONES GENERALES
# ==============================================================================
st.subheader("🏁 Conclusión: Hacia una ética enraizada en la realidad")

st.write(
    "- **Dialéctica Hombre-Sociedad:** No podemos realizarnos como individuos plenos si ignoramos la estructura social, "
    "la historia y el territorio que nos sostiene. La individualidad sin comunidad es un espejismo alienante.\n"
    "- **El verdadero Humanismo:** No reside en acumular diplomas académicos en la pared ni en dictar discursos morales impecables. "
    "El humanismo es *praxis*: la capacidad real de poner la ciencia y la técnica al servicio de la emancipación colectiva.\n"
    "- **El legado ético permanente:** Ser fieles a los aportes de Zuleta, Fals Borda y Gramsci implica rechazar con rebeldía las "
    "verdades empaquetadas, amar la dificultad que trae la diferencia y asumir el compromiso inquebrantable de caminar, pensar y "
    "sentir junto al pueblo."
)

# Sección interactiva final para captar atención
st.text_input("💬 Deja aquí tu propio compromiso como profesional sentipensante (Reflexión para el profesor):")

# ==============================================================================
# PANTALLA 10: CIERRE ESTÉTICO Y REFERENCIAS
# ==============================================================================
st.markdown("---")
st.markdown("<p style='text-align: center; font-style: italic; font-size: 1.2rem; color: #2C5282;'>\"La ciencia no es neutral, y el científico tampoco debe serlo ante la injusticia.\"</p>", unsafe_allow_html=True)

with st.expander("📚 Referencias del Material de Estudio"):
    st.caption("- Zuleta, E. — *Elogio de la dificultad y otros ensayos*")
    st.caption("- Rincón Díaz, J. A. — *La Investigación Acción Participativa como filosofía de vida del intelectual crítico* (Aportes de Orlando Fals Borda)")
    st.caption("- Gramsci, A. — *El sentido común y la formación del intelectual*")

st.markdown('<div class="footer">Desarrollado en Streamlit con enfoque humano y crítico • 2026</div>', unsafe_allow_html=True)
