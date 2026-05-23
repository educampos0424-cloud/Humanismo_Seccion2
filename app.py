import base64

# Let's create an elegant, structured HTML presentation storyboard or guide layout for the user
# that they can download as a PDF or copy directly. It will be designed meticulously.
# First, let's write out the full content of the presentation, meticulously structuring each slide.

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Estructura de Presentación Interactiva - Genially</title>
    <style>
        * {
            box-sizing: border-box;
        }
        @page {
            size: A4;
            margin: 18mm 15mm;
            background-color: #f4f6f8;
            @bottom-right {
                content: "Página " counter(page);
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-size: 8pt;
                color: #718096;
            }
        }
        body {
            margin: 0;
            padding: 0;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #2d3748;
            line-height: 1.6;
            font-size: 10.5pt;
            background-color: #f4f6f8;
        }
        .header-banner {
            background: linear-gradient(135deg, #1a365d, #2a4365);
            color: white;
            padding: 25px 20px;
            border-radius: 6px;
            margin-bottom: 25px;
        }
        .header-banner h1 {
            margin: 0;
            font-size: 18pt;
            font-weight: bold;
            letter-spacing: -0.5px;
        }
        .header-banner p {
            margin: 8px 0 0 0;
            font-size: 11pt;
            color: #e2e8f0;
        }
        .intro-box {
            background-color: #fff;
            border-left: 5px solid #3182ce;
            padding: 15px;
            margin-bottom: 25px;
            border-radius: 0 6px 6px 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .slide-container {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 25px;
            page-break-inside: avoid;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }
        .slide-header {
            border-bottom: 2px solid #edf2f7;
            padding-bottom: 8px;
            margin-bottom: 12px;
        }
        .slide-num {
            font-size: 9pt;
            font-weight: bold;
            color: #3182ce;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .slide-title {
            font-size: 13pt;
            color: #1a365d;
            margin: 4px 0 0 0;
            font-weight: bold;
        }
        .section-label {
            font-weight: bold;
            font-size: 9.5pt;
            color: #4a5568;
            margin-top: 10px;
            margin-bottom: 4px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .content-box {
            background-color: #f7fafc;
            border: 1px solid #edf2f7;
            padding: 12px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .content-box p, .content-box ul {
            margin: 0;
            padding-left: 15px;
        }
        .content-box li {
            margin-bottom: 4px;
        }
        .interactive-badge {
            background-color: #ebf8ff;
            border: 1px dashed #4299e1;
            color: #2b6cb0;
            padding: 10px;
            border-radius: 5px;
            font-size: 9.5pt;
        }
        .math {
            font-family: 'Times New Roman', serif;
            font-style: italic;
            font-weight: bold;
            color: #2b6cb0;
        }
        .tag {
            display: inline-block;
            background-color: #e2e8f0;
            color: #4a5568;
            font-size: 8pt;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: bold;
            margin-right: 5px;
        }
    </style>
</head>
<body>

    <div class="header-banner">
        <h1>Guión Técnico y de Contenido para Genially</h1>
        <p>Materia: Humanismo, Sociedad y Ética | Formato: Presentación Interactiva Autónoma</p>
    </div>

    <div class="intro-box">
        <strong>Nota de Diseño para Genially:</strong> Este documento contiene el mapa exacto de pantallas. Como es una presentación que el profesor o público leerá de forma autónoma a través de una pantalla, los textos combinan rigor conceptual (basado en Estanislao Zuleta, Orlando Fals Borda y Antonio Gramsci) con un tono humano y crítico ("sentipensante"). Incluye botones interactivos, ventanas flotantes ("pop-ups") y elementos gamificados para mantener la atención al 100%.
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 1 - Portada Principal</div>
            <div class="slide-title">El Conocimiento Sentipensante: Rompiendo la Burbuja Intelectual</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box" style="background-color: #1a365d; color: white;">
            <h2 style="margin:0; font-size:15pt;">El Conocimiento Sentipensante</h2>
            <p style="padding:0; margin-top:5px; color:#cbd5e0;">Un análisis ético y crítico de la relación entre el Hombre y la Sociedad en América Latina.</p>
            <p style="padding:0; margin-top:15px; font-size:9pt; color:#a0aec0;">Materia: Humanismo, Sociedad y Ética</p>
        </div>
        <div class="section-label">Componente Interactivo (Genially):</div>
        <div class="interactive-badge">
            ⚡ <strong>Botón Central Animado:</strong> "Hacer clic para iniciar la experiencia crítica" (Activa la transición hacia la siguiente pantalla).
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 2 - El Anzuelo Dinámico</div>
            <div class="slide-title">¿Elegirías la Pastilla de la Felicidad Artificial?</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box">
            <p><strong>El Dilema Técnico:</strong> Imagina que existe una tecnología capaz de darte una vida perfecta: sin filas, sin deudas, sin problemas y con tu título universitario asegurado sin abrir un solo libro.</p>
            <p style="margin-top: 8px; font-weight: bold; text-align: center;">¿Te la tomarías?</p>
        </div>
        <div class="section-label">Componente Interactivo (Encuesta / Ramificación):</div>
        <div class="interactive-badge">
            🔘 <strong>Dos botones interactivos para el usuario:</strong>
            <ul>
                <li><strong>Botón SI:</strong> Al dar clic, abre un Pop-up que dice: <em>"¡Caste en la trampa! Acabas de elegir un 'océano de mermelada sagrada'. Como decía Estanislao Zuleta, la comodidad absoluta extingue la necesidad de pensar."</em></li>
                <li><strong>Botón NO:</strong> Al dar clic, abre un Pop-up que dice: <em>"¡Bien pensado! Has elegido el camino de la dificultad. El verdadero crecimiento humano radica en el esfuerzo y la superación de contradicciones."</em></li>
            </ul>
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 3 - Introducción Formal</div>
            <div class="slide-title">Introducción: La Encrucijada de la Educación y la Ética</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box">
            <ul>
                <li><strong>El Aislamiento Técnico:</strong> La educación moderna corre el riesgo de convertirse en una fábrica de especialistas desconectados de las problemáticas reales de su comunidad.</li>
                <li><strong>El Rol de la Ética:</strong> No es un catálogo inerte de normas de comportamiento; es la fuerza viva que une el destino del individuo con el tejido social.</li>
                <li><strong>La Propuesta:</strong> A través de esta bitácora interactiva, analizaremos cómo el intelectualismo y el compromiso popular transforman la teoría abstracta en una práctica de vida transformadora.</li>
            </ul>
        </div>
        <div class="section-label">Componente Interactivo (Genially):</div>
        <div class="interactive-badge">
            ℹ️ <strong>Ícono de bombilla flotante:</strong> Al pasar el ratón (Hover), despliega el texto: <em>"Aprender a pensar por cuenta propia es, ante todo, un acto de responsabilidad ética y colectiva."</em>
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 4 - Tesis y Postura Crítica</div>
            <div class="slide-title">Nuestra Postura: El Hombre como Nodo Social</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box" style="border-left: 4px solid #e53e3e;">
            <p style="font-weight: bold; font-size: 11pt; color: #9b2c2c;">Nuestra Tesis Central:</p>
            <p>El ser humano no es un ente biológico aislado ni un robot procesador de datos. <strong>El verdadero conocimiento y la ética se configuran en el territorio.</strong> Sostenemos una postura crítica frente al conocimiento neutral de escritorio: el saber carece de valor si no se nutre del compromiso con el pueblo y la transformación de la realidad compartida.</p>
        </div>
        <div class="section-label">Componente Interactivo (Genially):</div>
        <div class="interactive-badge">
            🔍 <strong>3 Botones en forma de Engranaje (Los Tres Pilares):</strong> Cada uno abre una ventana con los nombres de los autores clave analizados: <em>Zuleta (Filosofía de vida)</em>, <em>Fals Borda (Compromiso del pueblo)</em>, y <em>Gramsci (Sentido común)</em>.
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 5 - Argumento 1 (Intelectualismo)</div>
            <div class="slide-title">Argumento 1: Descolonizar la Razón y el Sentido Común</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box">
            <ul>
                <li><strong>La falacia de la neutralidad:</strong> Tradicionalmente nos enseñan que la única ciencia válida es aquella producida bajo estándares eurocéntricos y en laboratorios aislados.</li>
                <li><strong>El Sentido Común (Gramsci):</strong> Todo ser humano es un filósofo en potencia. Las creencias y saberes populares no son "ignorancia", sino la base del pensamiento crítico de una sociedad.</li>
                <li><strong>El reto:</strong> Integrar el saber académico con la sabiduría comunitaria para deconstruir las estructuras hegemónicas de poder.</li>
            </ul>
        </div>
        <div class="section-label">Componente Interactivo (Genially):</div>
        <div class="interactive-badge">
            💡 <strong>Elemento Sorpresa (Lupa interactiva):</strong> Al arrastrar una lupa sobre la frase "sabiduría comunitaria", se revela un mensaje oculto: <em>"El saber popular es ciencia en resistencia."</em>
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 6 - Argumento 2 (Filosofía de Vida)</div>
            <div class="slide-title">Argumento 2: Elogio de la Dificultad contra el Dogma</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box">
            <ul>
                <li><strong>El peligro de la verdad absoluta:</strong> Las sociedades que buscan unanimidad y paraísos sin esfuerzo caen irremediablemente en el totalitarismo y el estancamiento intelectual (Zuleta).</li>
                <li><strong>La filosofía como riesgo:</strong> La vida es una autoproducción riesgosa en el tiempo. Pensar éticamente exige abrazar la complejidad y la duda metódica.</li>
                <li><strong>Comunicación incompleta:</strong> El respeto por el otro nace cuando aceptamos que nuestra propia verdad es parcial y requiere del diálogo comunitario.</li>
            </ul>
        </div>
        <div class="section-label">Componente Interactivo (Genially):</div>
        <div class="interactive-badge">
            ⚠️ <strong>Botón interactivo "Peligro: Dogmatismo":</strong> Al pulsarlo, emite un efecto visual y abre un recuadro con una cita potente de Estanislao Zuleta sobre el miedo a la diferencia.
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 7 - Argumento 3 (Compromiso del Pueblo)</div>
            <div class="slide-title">Argumento 3: El Concepto de Ser Sentipensante (IAP)</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box">
            <ul>
                <li><strong>El divorcio cartesiano:</strong> La academia ha separado históricamente la razón (la cabeza) de la emoción (el corazón), creando tecnócratas indiferentes.</li>
                <li><strong>La Investigación Acción Participativa (Fals Borda):</strong> Propone al intelectual crítico cuya filosofía de vida es sumergirse en la realidad popular para co-crear conocimiento emancipador.</li>
                <li><strong>Poder Popular:</strong> La investigación científica adquiere validez ética solo cuando se convierte en un instrumento de liberación para los pueblos oprimidos.</li>
            </ul>
        </div>
        <div class="section-label">Componente Interactivo (Genially):</div>
        <div class="interactive-badge">
            ❤️ <strong>Infografía Interactiva (Cabeza + Corazón):</strong> Al pulsar sobre el cerebro se despliega "Razón Rigurosa", al pulsar sobre el corazón se despliega "Empatía Social". Ambos confluyen en un botón central dinámico: <em>"Sentipensar"</em>.
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 8 - Gamificación / Actividad del Público</div>
            <div class="slide-title">Actividad Interactiva: El Simulador de Decisiones Éticas</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box" style="background-color: #fffaf0; border: 1px solid #feebc8;">
            <p><strong>El Caso:</strong> Una comunidad rural tiene problemas críticos de acceso al agua potable. Un grupo de científicos extranjeros diseña un software de distribución automatizada de alta tecnología sin consultar a los líderes locales. La comunidad rechaza el sistema porque altera sus formas ancestrales de organización del territorio.</p>
            <p style="margin-top: 8px; font-weight: bold;">Como profesional ético, ¿cuál es tu decisión?</p>
        </div>
        <div class="section-label">Opciones Interactivas (Ramificación de juego):</div>
        <div class="interactive-badge">
            🎮 <strong>Tres botones de respuesta interactiva:</strong>
            <ul>
                <li><strong>Opción A (Imponer el software):</strong> Despliega: ❌ <em>"Incorrecto. Caíste en el colonialismo intelectual. Priorizaste la técnica sobre la sociedad."</em></li>
                <li><strong>Opción B (Ignorar el problema):</strong> Despliega: ❌ <em>"Incorrecto. Adoptaste una postura apática, violando el principio de compromiso social."</em></li>
                <li><strong>Opción C (Aplicar los principios de la IAP):</strong> Despliega:  <em>"¡Excelente! Sentarse con la comunidad, reconocer su saber local y co-diseñar la solución es el camino sentipensante."</em></li>
            </ul>
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 9 - Conclusión Integrada</div>
            <div class="slide-title">Conclusión: Hacia una Ética Enraizada en el Territorio</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box" style="border-left: 4px solid #319795;">
            <ul>
                <li><strong>La Síntesis:</strong> La relación entre hombre y sociedad es dialéctica. No podemos construirnos como individuos plenos si ignoramos la estructura social que nos sostiene.</li>
                <li><strong>El Sentido del Humanismo:</strong> No reside en la acumulación pasiva de diplomas académicos, sino en la praxis: la capacidad de usar la ciencia y la técnica como herramientas colectivas de emancipación.</li>
                <li><strong>El Legado Ético:</strong> Ser fiel a los aportes de Zuleta y Fals Borda significa rechazar las verdades preconcebidas, valorar la complejidad de la diferencia y mantener vivo el compromiso de caminar junto al pueblo.</li>
            </ul>
        </div>
        <div class="section-label">Componente Interactivo (Genially):</div>
        <div class="interactive-badge">
            📌 <strong>Caja de Reflexión Pop-up:</strong> Un botón final que titila y dice <em>"Tu Compromiso Hoy"</em>. Al pulsarlo, muestra un cuadro de texto abierto para que quien visualice la presentación deje su propia conclusión personal.
        </div>
    </div>

    <div class="slide-container">
        <div class="slide-header">
            <div class="slide-num">Pantalla 10 - Cierre Estético y Referencias</div>
            <div class="slide-title">Fin de la Bitácora Interactiva</div>
        </div>
        <div class="section-label">Texto Visible en Pantalla:</div>
        <div class="content-box" style="text-align: center; background-color: #2d3748; color: white;">
            <p style="font-size: 13pt; font-weight: bold;">"La ciencia no es neutral, el científico tampoco debe serlo ante la injusticia."</p>
            <p style="font-size: 9pt; color: #cbd5e0; margin-top: 10px;">¡Gracias por recorrer este camino de pensamiento crítico!</p>
        </div>
        <div class="section-label">Referencias del Material de Estudio (Desplegable interactivo):</div>
        <div class="content-box" style="font-size: 8.5pt; color: #4a5568;">
            • Zuleta, E. - <em>Elogio de la dificultad y otros ensayos</em><br>
            • Fals Borda, O. - <em>La Investigación Acción Participativa como filosofía de vida</em><br>
            • Gramsci, A. - <em>El sentido común y la formación del intelectual</em>
        </div>
    </div>

</body>
</html>
"""

# Let's write the file and compile it via Weasyprint
with open("Guion_Genially_Humanismo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

from weasyprint import HTML
HTML("Guion_Genially_Humanismo.html").write_pdf("Guion_Genially_Humanismo.pdf")
print("PDF generated successfully.")
