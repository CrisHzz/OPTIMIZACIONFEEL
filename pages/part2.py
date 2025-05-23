import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""
    ...


def part2() -> rx.Component:
    return rx.container(
        rx.color_mode.button(
            position="top-right", 
            class_name="bg-white text-black hover:bg-gray-200 transition-colors px-4 py-2 rounded-lg border-6 border-white-400 shadow-md"
        ),
        rx.vstack(
            rx.box(
                rx.hstack(
                    rx.heading(
                        "FeelTheDistribution",
                        size="8",
                        class_name="text-white font-bold pl-4",
                    ),
                    rx.hstack(
                        rx.link(
                            "Part 1", 
                            href="/part1", 
                            class_name="text-white hover:text-purple-300 transition-colors px-4 py-2 rounded-lg hover:bg-purple-900/30"
                        ),
                        rx.link(
                            "Part 2", 
                            href="/part2", 
                            class_name="text-white hover:text-purple-300 transition-colors px-4 py-2 rounded-lg hover:bg-purple-900/30"
                        ),
                        rx.link(
                            "Part 3",
                            href="/part3", 
                            class_name="text-white hover:text-purple-300 transition-colors px-4 py-2 rounded-lg hover:bg-purple-900/30"
                        ),
                        rx.link(
                            "Bibliografías", 
                            href="/bibliografias", 
                            class_name="text-white hover:text-purple-300 transition-colors px-4 py-2 rounded-lg hover:bg-purple-900/30"
                        ),
                        spacing="8",
                    ),
                    width="100%",
                    justify="between",
                    align="center",
                    padding="6",
                    class_name="bg-gradient-to-r from-purple-900/50 to-black/50 backdrop-blur-sm rounded-2xl shadow-2xl border border-purple-500/20",
                ),
                class_name="w-full mb-8",
            ),
            rx.box(
                rx.heading(
                    "Part 2: Análisis de la relación entre variables de proceso y consumo energético",
                    size="8",
                    class_name="text-white mb-4",
                ),

                rx.text(
                    """Caso de estudio: Eficiencia Energética en Procesos Industriales

                    Una planta industrial está interesada en entender y optimizar el consumo energético de uno de sus procesos 
                    principales. Se sospecha que el consumo de energía (kWh) está relacionado con la velocidad de producción 
                    (unidades/hora). Se han recolectado datos de 50 jornadas de producción, registrando ambas variables.""",
                    class_name="text-white mb-4",
                    style={"white-space": "pre-line"},
                ),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell(
                                "jornada",
                                class_name="text-white"
                            ),
                            rx.table.column_header_cell(
                                "velocidad_produccion", 
                                class_name="text-white"
                            ),
                            rx.table.column_header_cell(
                                "consumo_energia",
                                class_name="text-white" 
                            )
                        )
                    ),
                    rx.table.body(
                        rx.table.row(
                            rx.table.cell("1.0", class_name="text-white"),
                            rx.table.cell("92.0", class_name="text-white"),
                            rx.table.cell("126.1", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("2.0", class_name="text-white"),
                            rx.table.cell("97.0", class_name="text-white"), 
                            rx.table.cell("127.3", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("3.0", class_name="text-white"),
                            rx.table.cell("123.0", class_name="text-white"),
                            rx.table.cell("148.0", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("4.0", class_name="text-white"),
                            rx.table.cell("101.0", class_name="text-white"),
                            rx.table.cell("144.5", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("5.0", class_name="text-white"),
                            rx.table.cell("102.0", class_name="text-white"),
                            rx.table.cell("129.3", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("6.0", class_name="text-white"),
                            rx.table.cell("126.0", class_name="text-white"),
                            rx.table.cell("166.0", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("7.0", class_name="text-white"),
                            rx.table.cell("107.0", class_name="text-white"),
                            rx.table.cell("120.1", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("8.0", class_name="text-white"),
                            rx.table.cell("81.0", class_name="text-white"),
                            rx.table.cell("120.6", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("9.0", class_name="text-white"),
                            rx.table.cell("90.0", class_name="text-white"),
                            rx.table.cell("123.2", class_name="text-white")
                        ),
                        rx.table.row(
                            rx.table.cell("10.0", class_name="text-white"),
                            rx.table.cell("93.0", class_name="text-white"),
                            rx.table.cell("126.6", class_name="text-white")
                        )
                    ),
                    
                    variant="surface",
                    class_name="bg-black",
                    
                ),
                rx.text(
                        "Referencias: Brindados por la actividad",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                class_name="p-8 rounded-2xl w-full bg-gradient-to-br from-black to-purple-800 shadow-lg overflow-x-auto",
            ),
            rx.box(
                rx.heading(
                    "A) Análisis descriptivo y gráfico de los datos",
                    size="8",
                    class_name="text-white mb-4",
                ),
                rx.heading(
                    "Medidas de tendencia central",
                    size="6",
                    class_name="text-white mb-4",
                ),
                rx.text(
                    "Existen varios tipos de medidas que nos sirven para darle sentido y valor a los datos, sea desde el apartado básico como entender el promedio, cómo se desvían sus datos del centro y hasta qué forma y comportamiento tienen ellos [33][34]",
                    style={"white-space": "pre-line"},
                    class_name="text-white mb-4",),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Medida", class_name="text-white"),
                                rx.table.column_header_cell("Velocidad de producción", class_name="text-white"),
                                rx.table.column_header_cell("Consumo de energía", class_name="text-white")
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("Media", class_name="text-white"),
                                rx.table.cell("100.56", class_name="text-white"),
                                rx.table.cell("131.91", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("Mediana", class_name="text-white"),
                                rx.table.cell("99.0", class_name="text-white"),
                                rx.table.cell("131.7", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("Moda", class_name="text-white"),
                                rx.table.cell("93.0", class_name="text-white"),
                                rx.table.cell("136.7", class_name="text-white")
                            )
                        ),
                        variant="surface",
                        class_name="bg-black",
                    ),
                    rx.text(
                        "Referencias: [2][5] Tabla creada con numpy y matplotlib.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.text(
                        "Las medidas de tendencia central revelan patrones importantes: la velocidad de producción muestra una ligera asimetría positiva (media=100.56 > mediana=99.0 > moda=93.0), mientras que el consumo de energía presenta una distribución más simétrica entre media (131.91) y mediana (131.7), con algunos valores atípicos altos indicados por la moda (136.7). Esto sugiere un proceso productivo con velocidades variables pero un consumo energético relativamente estable.",
                        class_name="text-white mb-4",
                    ),
                    rx.heading(
                        "Medidas de dispersión",
                        size="6",
                        class_name="text-white mb-4 pt-4",

                    ),
                    rx.text(
                        "Las medidas de dispersión nos indican qué tan dispersos están los datos alrededor de su valor central [35][37]. La desviación estándar, varianza y rango nos ayudan a entender la variabilidad de los datos.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Medida", class_name="text-white"),
                                rx.table.column_header_cell("Velocidad de producción", class_name="text-white"),
                                rx.table.column_header_cell("Consumo de energía", class_name="text-white")
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("Desviación estándar", class_name="text-white"),
                                rx.table.cell("13.83", class_name="text-white"),
                                rx.table.cell("14.04", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("Varianza", class_name="text-white"), 
                                rx.table.cell("191.23", class_name="text-white"),
                                rx.table.cell("197.05", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("Rango", class_name="text-white"),
                                rx.table.cell("62.0", class_name="text-white"),
                                rx.table.cell("61.5", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("Coeficiente de variación", class_name="text-white"),
                                rx.table.cell("0.138", class_name="text-white"),
                                rx.table.cell("0.106", class_name="text-white")
                            )
                        ),
                        
                        variant="surface",
                        class_name="bg-black",
                    ),
                    rx.text(
                        "Referencias: [2][5] Tabla creada con numpy y matplotlib.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.text(
                        "Podemos observar que tanto la velocidad de producción como el consumo de energía muestran niveles similares de variabilidad. La desviación estándar y varianza son ligeramente mayores en el consumo de energía, indicando una dispersión levemente superior. Sin embargo, el coeficiente de variación es menor en el consumo de energía (0.106 vs 0.138), lo que sugiere que, en términos relativos, este parámetro es más estable.",
                        class_name="text-white mb-4"
                    ),
                    rx.heading(
                        "Medidas de forma",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Las medidas de forma nos indican la asimetría y la forma de la distribución de los datos [34][35]. La asimetría nos dice si los datos están sesgados hacia un lado, mientras que la curtosis nos indica la 'altura' de la distribución.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Medida", class_name="text-white"),
                                rx.table.column_header_cell("Velocidad de producción", class_name="text-white"),
                                rx.table.column_header_cell("Consumo de energía", class_name="text-white")
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("Asimetría", class_name="text-white"),
                                rx.table.cell("0.197", class_name="text-white"),
                                rx.table.cell("0.149", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("Curtosis", class_name="text-white"),
                                rx.table.cell("-0.299", class_name="text-white"), 
                                rx.table.cell("-0.547", class_name="text-white")
                            )
                        ),
                        
                        variant="surface",
                        class_name="bg-black",
                    ),
                    rx.text(
                        "Referencias: [2][5] Tabla creada con numpy y matplotlib.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.text(
                        "Los valores de asimetría positivos pero cercanos a 0 (0.197 y 0.149) indican que ambas variables tienen una distribución ligeramente sesgada hacia la derecha, pero bastante simétrica. La curtosis negativa en ambos casos (-0.299 y -0.547) sugiere que las distribuciones son más planas que una distribución normal (platicúrticas), con colas más ligeras y picos menos pronunciados.",
                        class_name="text-white mb-4"
                    ),
                    rx.heading(
                        "Gráfico de histograma",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El histograma es una representación gráfica de los datos a través del tiempo y poder evidenciar cómo es la distribución de los datos [33][34]",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/histogram2.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                    ),
                    rx.text(
                        "Referencias: [3][9] Histograma creado con Matplotlib para visualizar la distribución de datos.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),

                    rx.heading(
                        "Gráfico de dispersión",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El gráfico de dispersión nos permite ver por encima la distribución de los datos, datos atípicos y encontrar qué tipo de correlación existe entre las variables que se están analizando [33][34]",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/scatter.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                    ),
                    rx.text(
                        "Referencias: [3][10] Gráfico de dispersión creado con Matplotlib para visualizar la correlación.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.heading(
                        "B) El coeficiente de correlación",
                        size="7",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El coeficiente de correlación es una medida estadística que indica la fuerza y dirección de la relación lineal entre dos variables [21][33][43]. Varía entre -1 y 1, donde 1 indica una correlación positiva perfecta, -1 una correlación negativa perfecta y 0 ninguna correlación.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        """• Tamaño de muestra: 50

• Coeficiente de correlación: 0.764

• Estadístico t: 8.210

• Valor p: 1.064e-10

• Alpha: 0.05

• Hipótesis nula: No hay correlación entre las variables.

• Hipótesis alternativa: Existe una correlación significativa entre las variables.

• Rechazamos la hipótesis nula. La correlación es estadísticamente significativa.""",
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto font-mono",
                        style={"white-space": "pre-line"},
                    ),
                    
                    rx.text(
                        "El coeficiente de correlación entre las 2 variables es de 0.764,\npor lo tanto hay CORRELACIÓN LINEAL ALTA.",
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto font-mono",
                        style={"white-space": "pre-line"},
                    ),
                    rx.text(
                        "Referencias: [7][25][32] ",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.heading(
                        "C) Regresión lineal simple",
                        size="7",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.heading( 
                        "Recomendación de modelo de regresión",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Existen varios tipos de modelos de regresión que nos pueden servir para desarrollar este proyecto [33][42][21], todo depende del tipo de datos que se tienen, la cantidad de variables, el peso de estas para la predicción entre muchas otras características. En este caso a pesar de plantear 3 tipos de modelo de regresión, la regresión lineal es la que mejor se adapta a los datos y el comportamiento de estos, ridge y lasso nos darían el mismo rendimiento pues las condiciones para estos no son las indicadas y el R2 nos da igual en los 3 casos",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        """--- Evaluación de modelos (R² con cross-validation) ---

                        Regresión Lineal: R² promedio = 0.4171
                        Ridge: R² promedio = 0.4171 
                        Lasso: R² promedio = 0.4171

                        --- Resultados ---

                        ✅ Modelo recomendado: Regresión Lineal
                        Valores de R² promedio:
                        {'Regresión Lineal': 0.4171, 'Ridge': 0.4171, 'Lasso': 0.4171}""",
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto font-mono",
                        style={"white-space": "pre-line"},
                    ),
                    rx.text(
                        "Referencias: [2][21][4][47] Evaluación de modelos de regresión lineal, Ridge y Lasso utilizando Scikit-learn.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.heading(
                        "Estandarización del dataset",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "La estandarización es un proceso que transforma los datos para que tengan una media de 0 y una desviación estándar de 1 [33][34]. Esto es útil para comparar variables que están en diferentes escalas o unidades. Ayuda bastante a la hora de alimentar nuestro modelo o regresión haciendo los datos más pequeños y disminuir el tiempo de entreno",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/standardDataset.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                    ),
                    rx.text(
                        "Referencias: [2][5] Estandarización de datos utilizando NumPy y Pandas.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.heading(
                        "Implementación de regresión lineal",
                        size="7",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Ahora ya encontramos el tipo de regresión adecuada para el conjunto de datos [4][21], gracias a ello podemos crear una regresión lineal que permitirá hacer una predicción dada una variable independiente",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",

                    ),
                    rx.markdown(
                        "$$Y= WX + b $$",
                    
               
                    ),
                    rx.text(
                        "Donde W son los pesos y b el sesgo de la regresión lineal",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "LinearRegression()",
                        font_family="monospace",
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto font-mono",
                    ),
                    rx.heading(
                        "Entreno del modelo, pesos y sesgos de este",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Vamos a entrenar nuestro modelo utilizando aproximadamente un 70% para los datos de entreno y un 30% para los datos de testeo [34][38][47], esto nos permitirá ver si el modelo es capaz de predecir los datos que no ha visto antes, además de visualizar el peso y sesgo del modelo",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "El peso (Coeficiente) del modelo es [0.8283] y su sesgo (intercepto) es -0.02370000071823597",
                        font_family="monospace",
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto font-mono",
                    ),
                    rx.markdown(
                        "$$ Y = 0.8283X -0.0237 $$"
                    ),
                    rx.text(
                        "Evaluación del rendimiento de la regresión lineal",
                        size="6",
                        class_name="text-white mb-4 pt-4 font-bold",
                    ),

                    rx.text(
                        "Existen varias métricas para evaluar nuestro rendimiento del modelo [21][33][34], en este caso usaremos el error cuadrático medio, el coeficiente de determinación y la raíz del error cuadrático medio",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),

                    rx.vstack(
                        rx.text(
                            "Resultados de la regresión lineal:",
                            font_family="monospace",
                            class_name="text-white font-bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("MSE: 0.3605"),
                            rx.list_item("RMSE: 0.6004"), 
                            rx.list_item("R²: 0.4150"),
                            class_name="text-white mb-4",
                        ),
                        rx.text(
                            "Interpretación:",
                            font_family="monospace",
                            class_name="text-white font-bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("El modelo explica el 41.50% de la variabilidad en los datos"),
                            rx.list_item("El error promedio en las predicciones es de 0.6004 unidades"),
                            rx.list_item("El modelo presenta una precisión muy baja; esto puede deberse a registros limitados o baja calidad de los datos"),
                            class_name="text-white",
                        ),
                        class_name="bg-black p-4 rounded-lg my-4 w-full overflow-auto font-mono",
                    ),
                    rx.text(
                        "Referencias: [2][4][21] Evaluación del rendimiento de la regresión lineal utilizando Scikit-learn.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    
                    # Nueva sección para validación del modelo (punto d)
                    rx.heading(
                        "D) Validación del Modelo de Regresión",
                        size="7",
                        class_name="text-white mb-4 pt-6",
                    ),
                    rx.text(
                        "La validación del modelo es un paso crucial para determinar si un modelo de regresión lineal es adecuado para los datos [22][23]. Esta validación incluye verificar los supuestos del modelo, realizar pruebas de hipótesis para los parámetros, construir intervalos de confianza y analizar los residuos.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    
                    rx.code_block(
                        """## Validación del Modelo de Regresión Lineal
**NOTA: Algunas pruebas estadísticas avanzadas no están disponibles. Instale statsmodels para análisis completo: pip install statsmodels**

### 1. Verificación de Supuestos

**Normalidad de residuos:**
- Test Shapiro-Wilk: p-valor = 0.9867
- Conclusión: Los residuos SIGUEN una distribución normal
    
**Homocedasticidad:**
- Test Breusch-Pagan: p-valor = 0.0047
- Conclusión: Los residuos NO presentan varianza constante (no hay homocedasticidad), lo que indica que la variabilidad de los errores cambia a lo largo de las predicciones

**Independencia de residuos:**
- Estadístico Durbin-Watson: 0.0000
- Conclusión: Los residuos NO SON independientes

### 2. Pruebas de Hipótesis para los Parámetros

**Intercepto (β₀):**
- Valor: -0.0237
- p-valor: 0.0000
- Conclusión: El intercepto es ESTADÍSTICAMENTE NO SIGNIFICATIVO

**Pendiente (β₁):**
- Valor: 0.8283
- p-valor: 0.0000
- Conclusión: La pendiente es ESTADÍSTICAMENTE SIGNIFICATIVA

### 3. Intervalos de Confianza (95%)

**Intercepto (β₀):**
- IC 95%: [0.0000, 0.0000]

**Pendiente (β₁):**
- IC 95%: [0.0000, 0.0000]

### 4. Análisis de Residuos

Se han generado los siguientes gráficos para analizar visualmente los residuos:
- Residuos vs Valores ajustados: permite verificar linealidad y homocedasticidad
- Gráfico Q-Q: permite verificar normalidad de residuos
- Histograma de residuos: muestra la distribución de los errores

**Conclusión general:**
El modelo NO CUMPLE con todos los supuestos de regresión lineal.
La pendiente del modelo es SIGNIFICATIVA, lo que indica que EXISTE una relación lineal entre la velocidad de producción y el consumo de energía.""",
                        language="markdown",
                        show_line_numbers=False,
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto",
                    ),
                    
                    rx.heading(
                        "Análisis Visual de Residuos",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El análisis visual de los residuos es fundamental para verificar los supuestos del modelo de regresión lineal [3][6][8]. A continuación se presentan gráficos que nos ayudan a evaluar dichos supuestos:",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    
                    rx.cond(
                        True,  # Condición siempre verdadera para mostrar los gráficos
                        rx.vstack(
                            rx.heading(
                                "Residuos vs Valores Ajustados",
                                size="5",
                                class_name="text-white text-center font-bold mt-6"
                            ),
                            rx.text(
                                "Este gráfico permite visualizar si los residuos se distribuyen de manera aleatoria alrededor de cero, lo que indicaría que el modelo es apropiado [44]. Patrones en este gráfico pueden revelar problemas con el modelo.",
                                class_name="text-white mb-4 text-center"
                            ),
                            rx.image(
                                src='/residuos_vs_ajustados.png',
                                height="500px",
                                class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 object-contain",
                            ),
                            rx.text(
                                "Referencias: [3][13][19] Gráfico de residuos vs valores ajustados creado con Seaborn y Statsmodels.",
                                class_name="text-gray-400 text-sm mb-4 text-center italic",
                            ),
                            
                            rx.heading(
                                "Gráfico Q-Q de Residuos",
                                size="5",
                                class_name="text-white text-center font-bold mt-6"
                            ),
                            rx.text(
                                "El gráfico Q-Q compara los cuantiles de los residuos con los cuantiles teóricos de una distribución normal [13]. Si los puntos siguen aproximadamente la línea diagonal, los residuos siguen una distribución normal.",
                                class_name="text-white mb-4 text-center"
                            ),
                            rx.image(
                                src='/qq_residuos.png',
                                height="500px",
                                class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 object-contain",
                            ),
                            rx.text(
                                "Referencias: [3][15] Gráfico Q-Q para evaluar normalidad de residuos creado con Matplotlib.",
                                class_name="text-gray-400 text-sm mb-4 text-center italic",
                            ),
                            
                            rx.heading(
                                "Histograma de Residuos",
                                size="5",
                                class_name="text-white text-center font-bold mt-6"
                            ),
                            rx.text(
                                "El histograma muestra la distribución de los residuos [43]. Idealmente, debería seguir una forma aproximadamente normal y centrada en cero, lo que indicaría que los errores del modelo son aleatorios.",
                                class_name="text-white mb-4 text-center"
                            ),
                            rx.image(
                                src='/histograma_residuos.png',
                                height="500px",
                                class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 object-contain",
                            ),
                            rx.text(
                                "Referencias: [3][9] Histograma de residuos creado con Matplotlib para verificar la distribución de errores.",
                                class_name="text-gray-400 text-sm mb-4 text-center italic",
                            ),
                            width="100%",
                            spacing="4",
                            class_name="mb-6",
                        )
                    ),
                    
                    rx.text(
                        "En base a esta validación, podemos concluir si el modelo de regresión lineal es adecuado para predecir el consumo de energía en función de la velocidad de producción, y cuáles son sus limitaciones y fortalezas.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    
                    # Nueva sección para el punto e: Utilización del modelo
                    rx.heading(
                        "E) Aplicación y Optimización del Modelo",
                        size="7",
                        class_name="text-white mb-4 pt-6",
                    ),
                    rx.text(
                        "En esta sección aplicaremos el modelo para realizar predicciones específicas, construir intervalos de predicción, optimizar la eficiencia energética y proporcionar recomendaciones concretas para la empresa [16][21].",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.code_block(
                        """## Aplicación y Optimización del Modelo

### 1. Predicción de Consumo Energético

Para una velocidad de producción de **85.00 unidades/hora**:
- Consumo energético predicho: **119.84 kWh**

### 2. Intervalo de Predicción del 95%

El intervalo de predicción con 95% de confianza para el consumo energético es:
- Límite inferior: **114.34 kWh**
- Límite superior: **125.34 kWh**

Esto significa que, con una confianza del 95%, el consumo energético real estará dentro de este rango.

### 3. Optimización de la Eficiencia Energética

La velocidad de producción que minimiza el consumo energético por unidad producida es:
- Velocidad óptima: **133.00 unidades/hora**
- Consumo energético correspondiente: **157.08 kWh**
- Eficiencia energética óptima: **1.1810 kWh/unidad**

### 4. Recomendaciones para Optimizar la Eficiencia Energética

1. **Ajustar la velocidad de producción**: Establecer la velocidad de producción lo más cercana posible a 133.00 unidades/hora para minimizar el consumo energético por unidad producida.

2. **Implementar monitoreo continuo**: Desarrollar un sistema de monitoreo que registre en tiempo real la velocidad de producción y el consumo energético para mantener la operación en el punto óptimo.

3. **Planificar producción en lotes óptimos**: Organizar los ciclos de producción para operar principalmente en el rango de mayor eficiencia, evitando arranques y paradas frecuentes que pueden ser menos eficientes.

4. **Mantenimiento preventivo**: Establecer un programa de mantenimiento preventivo para asegurar que los equipos operen cerca de su eficiencia óptima.

5. **Análisis periódico**: Reevaluar regularmente la relación entre velocidad y consumo para detectar cambios en el proceso que puedan alterar el punto óptimo de operación.""",
                        language="markdown",
                        show_line_numbers=False,
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto",
                    ),
                    
                    rx.heading(
                        "Visualización de la Eficiencia Energética",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El siguiente gráfico muestra la relación entre la velocidad de producción y la eficiencia energética (consumo por unidad producida) [41][45]. El punto marcado en rojo representa la velocidad óptima que minimiza el consumo energético por unidad.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/eficiencia_vs_velocidad.png',
                        height="600px",
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 object-contain",
                    ),
                    rx.text(
                        "Referencias: [3][4][21] Gráfico de eficiencia energética creado con Matplotlib y modelos de Scikit-learn.",
                        class_name="text-gray-400 text-sm mb-8 text-center italic",
                    ),
                    rx.heading(
                        "Conclusiones",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Podemos concluir que este modelo no es adecuado para hacer producciones en un ambiente más laboral y operativo, pues demuestra una tasa de variabilidad muy baja generando una confianza baja a la hora de hacer una predicción, por lo tanto NO SE RECOMIENDA SU USO. Sin embargo, para motivos académicos se usará.",
                        class_name="text-white mb-4",
                    ),

                class_name="p-8 rounded-2xl w-full bg-gradient-to-br from-black to-purple-800 shadow-lg overflow-x-auto",
            ),
                
            align="center",
            justify="center",
            spacing="8",
            width="100%",
        ),
        class_name="min-h-screen bg-gradient-to-br from-black to-purple-800 p-8",
    )

app = rx.App()
app.add_page(part2)

#e
