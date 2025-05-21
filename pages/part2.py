import reflex as rx
from rxconfig import config
from data_processing.point2 import dataset_2_short, dataset_dispersion2, dataset_dispersion2, dataset_form2

class State(rx.State):
    """The app state."""
    ...


def part2() -> rx.Component:
    return rx.container(
        rx.color_mode.button(
            position="top-right", 
            class_name="bg-yellow-500 text-black hover:bg-yellow-600 transition-colors px-4 py-2 rounded-lg"
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
                            "Bibliografias", 
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
                    "Dataset Parte #2",
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
                            *[
                                rx.table.column_header_cell(
                                    col,
                                    class_name="text-white"
                                )
                                for col in dataset_2_short.columns
                            ]
                        )
                    ),
                    rx.table.body(
                        *[
                            rx.table.row(
                                *[
                                    rx.table.cell(
                                        str(value),
                                        class_name="text-white"
                                    )
                                    for value in row
                                ]
                            )
                            for row in dataset_2_short.values
                        ]
                    ),
                    variant="surface",
                    class_name="bg-black",
                ),
                class_name="p-8 rounded-2xl w-full bg-gradient-to-br from-black to-purple-800 shadow-lg overflow-x-auto",
            ),
            rx.box(
                rx.heading(
                    "Medidas de tendencia central, dispersión y forma",
                    size="8",
                    class_name="text-white mb-4",
                ),
                rx.heading(
                    "Medidas de tendencia central",
                    size="6",
                    class_name="text-white mb-4",
                ),
                rx.text(
                    "Existen varios tipos de medidas que nos sirven para darle sentido a valor a los datos sea desde el apartado basico como entender el promedio, como se desvian sus datos del centro y hasta que forma y comportamiento tienen ellos",
                    style={"white-space": "pre-line"},
                    class_name="text-white mb-4",),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                *[
                                    rx.table.column_header_cell(
                                        col,
                                        class_name="text-white"
                                    )
                                    for col in dataset_dispersion2.columns
                                ]
                            )
                        ),
                        rx.table.body(
                            *[
                                rx.table.row(
                                    *[
                                        rx.table.cell(
                                            str(value),
                                            class_name="text-white"
                                        )
                                        for value in row
                                    ]
                                )
                                for row in dataset_dispersion2.values
                            ]
                        ),
                        variant="surface",
                        class_name="bg-black",
                    ),
                    rx.heading(
                        "Medidas de dispersión",
                        size="6",
                        class_name="text-white mb-4 pt-4",

                    ),
                    rx.text(
                        "Las medidas de dispersión nos indican qué tan dispersos están los datos alrededor de su valor central. La desviación estándar, varianza y rango nos ayudan a entender la variabilidad de los datos.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                *[
                                    rx.table.column_header_cell(
                                        col,
                                        class_name="text-white"
                                    )
                                    for col in dataset_dispersion2.columns
                                ]
                            )
                        ),
                        rx.table.body(
                            *[
                                rx.table.row(
                                    *[
                                        rx.table.cell(
                                            str(value),
                                            class_name="text-white"
                                        )
                                        for value in row
                                    ]
                                )
                                for row in dataset_dispersion2.values
                            ]
                        ),
                        variant="surface",
                        class_name="bg-black",
                    ),
                    rx.heading(
                        "Medidas de forma",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Las medidas de forma nos indican la asimetría y la forma de la distribución de los datos. La asimetría nos dice si los datos están sesgados hacia un lado, mientras que la curtosis nos indica la 'altura' de la distribución.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                *[
                                    rx.table.column_header_cell(
                                        col,
                                        class_name="text-white"
                                    )
                                    for col in dataset_form2.columns
                                ]
                            )
                        ),
                        rx.table.body(
                            *[
                                rx.table.row(
                                    *[
                                        rx.table.cell(
                                            str(value),
                                            class_name="text-white"
                                        )
                                        for value in row
                                    ]
                                )
                                for row in dataset_form2.values
                            ]
                        ),
                        variant="surface",
                        class_name="bg-black",
                    ),
                    rx.heading(
                        "Grafico de histograma",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El histograma es una representación gráfica de los datos a traves del tiempo y poder evidenciar como es la distribucion de los datos",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/histogram2.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg overflow-x-auto",
                    ),

                    rx.heading(
                        "Grafico de dispersion",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El grafico de dispersion nos permite ver por encima la distribucion de los datos , datos atipicos y encontrar que tipo de correlacion existe entre las variables que se estan analizando",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/scatter.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg overflow-x-auto",
                    ),
                    rx.heading(
                        "Encontrar la coeficiente de correlacion entre las variables",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El coeficiente de correlación es una medida estadística que indica la fuerza y dirección de la relación lineal entre dos variables. Varía entre -1 y 1, donde 1 indica una correlación positiva perfecta, -1 una correlación negativa perfecta y 0 ninguna correlación.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "El coeficiente de correlacion entre las 2 variables es de 0.764,\npor lo tanto hay CORRELACION LINEAL ALTA.",
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto font-mono",
                        style={"white-space": "pre-line"},
                    ),
                    rx.heading( 
                        "Recomendación de modelo de regresión",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Existen varios tipos de modelos de regresion que nos pueden servir para desarollar este proyecto , todo depende del tipo de datos que se tienen , la cantidad de variables , el peso de estas para la prediccion entre muchas otras caracteristicas. En este caso a pesar de plantear 3 tipos de modelo de regresion , la regresion lineal es la que mejor se adapta a los datos y el comportamiento de estos, ridge y lasso nos darian el mismo rendimiento pues las condiciones para estos no son las indicadas y el R2 nos da igual en los 3 casos",
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
                    rx.heading(
                        "Estandarizacion del dataset",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "La estandarización es un proceso que transforma los datos para que tengan una media de 0 y una desviación estándar de 1. Esto es útil para comparar variables que están en diferentes escalas o unidades. ayuda bastante a la hora de alimentar nuestro modelo o regresion haciendo los datos mas pequeños y disminuir el tiempo de entreno",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/standardDataset.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg overflow-x-auto",
                    ),
                    rx.heading(
                        "Implementacion de regresion lineal",
                        size="7",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Ahora ya encontramos el tipo de regresion adecuada para el conjunto de datos , gracias a ello podemos crear una regresion lineal que permitira hacer una prediccion dada una variable indepediente",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",

                    ),
                    rx.markdown(
                        "$$Y= WX + b $$",
                    
               
                    ),
                    rx.text(
                        "Donde W son los pesos y b el sesgo de la regresion lineal",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "LinearRegression()",
                        font_family="monospace",
                        class_name="bg-black text-white p-4 rounded-lg my-4 w-full overflow-auto font-mono",
                    ),
                    rx.heading(
                        "Entreno del modelo , pesos y sesgos de este",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Vamos a entrenar nuestro modelo utilizando aproximadamente un 70% para los datos de entreno y un 30% para los datos de testeo, esto nos permitira ver si el modelo es capaz de predecir los datos que no ha visto antes , ademas de visualizar el peso y sesgo del modelo",
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
                        "Evaluacion del rendimiento de la regresion lineal",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),

                    rx.text(
                        "Existen varias metricas para evaluar nuestro rendimiento del modelo , en este caso usaremos el error cuadratico medio , el coeficiente de determinacion y la raiz del error cuadratico medio",
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
                    
                    # Nueva sección para validación del modelo (punto d)
                    rx.heading(
                        "Validación del Modelo de Regresión",
                        size="7",
                        class_name="text-white mb-4 pt-6",
                    ),
                    rx.text(
                        "La validación del modelo es un paso crucial para determinar si un modelo de regresión lineal es adecuado para los datos. Esta validación incluye verificar los supuestos del modelo, realizar pruebas de hipótesis para los parámetros, construir intervalos de confianza y analizar los residuos.",
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
- Test Breusch-Pagan: p-valor = 0.0000
- Conclusión: NO EXISTE homocedasticidad (varianza constante)

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
                        "El análisis visual de los residuos es fundamental para verificar los supuestos del modelo de regresión lineal. A continuación se presentan gráficos que nos ayudan a evaluar dichos supuestos:",
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
                                "Este gráfico permite visualizar si los residuos se distribuyen de manera aleatoria alrededor de cero, lo que indicaría que el modelo es apropiado. Patrones en este gráfico pueden revelar problemas con el modelo.",
                                class_name="text-white mb-4 text-center"
                            ),
                            rx.image(
                                src='/residuos_vs_ajustados.png',
                                height="500px",
                                class_name="p-4 rounded-2xl bg-black shadow-lg mb-8 object-contain",
                            ),
                            
                            rx.heading(
                                "Gráfico Q-Q de Residuos",
                                size="5",
                                class_name="text-white text-center font-bold mt-6"
                            ),
                            rx.text(
                                "El gráfico Q-Q compara los cuantiles de los residuos con los cuantiles teóricos de una distribución normal. Si los puntos siguen aproximadamente la línea diagonal, los residuos siguen una distribución normal.",
                                class_name="text-white mb-4 text-center"
                            ),
                            rx.image(
                                src='/qq_residuos.png',
                                height="500px",
                                class_name="p-4 rounded-2xl bg-black shadow-lg mb-8 object-contain",
                            ),
                            
                            rx.heading(
                                "Histograma de Residuos",
                                size="5",
                                class_name="text-white text-center font-bold mt-6"
                            ),
                            rx.text(
                                "El histograma muestra la distribución de los residuos. Idealmente, debería seguir una forma aproximadamente normal y centrada en cero, lo que indicaría que los errores del modelo son aleatorios.",
                                class_name="text-white mb-4 text-center"
                            ),
                            rx.image(
                                src='/histograma_residuos.png',
                                height="500px",
                                class_name="p-4 rounded-2xl bg-black shadow-lg mb-8 object-contain",
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
                        "Aplicación y Optimización del Modelo",
                        size="7",
                        class_name="text-white mb-4 pt-6",
                    ),
                    rx.text(
                        "En esta sección aplicaremos el modelo para realizar predicciones específicas, construir intervalos de predicción, optimizar la eficiencia energética y proporcionar recomendaciones concretas para la empresa.",
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
                        "El siguiente gráfico muestra la relación entre la velocidad de producción y la eficiencia energética (consumo por unidad producida). El punto marcado en rojo representa la velocidad óptima que minimiza el consumo energético por unidad.",
                        style={"white-space": "pre-line"},
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/eficiencia_vs_velocidad.png',
                        height="600px",
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-8 object-contain",
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
