import reflex as rx
from rxconfig import config
class State(rx.State):
    """The app state."""
    ...

def part1() -> rx.Component:
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
                rx.vstack(
                    rx.heading(
                        "Part 1: Análisis de tiempos en procesos de producción ",
                        size="8",
                        class_name="text-white mb-4",
                    ),
                    rx.heading(
                        "Creación del conjunto de datos",
                        size="5",
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "Se crea un dataset usando las librerías de numpy [5] y pandas [2], estos nos generarán los datasets para este apartado. La columna Línea A (s) representa el tiempo que demora completar una operación en esta línea de operación para un producto, lo mismo con la columna Línea B (s). Siendo un total de 100 registros por cada línea de producción.",
                        class_name="text-white mb-8",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell(
                                    "Línea A (s)",
                                    class_name="text-white"
                                ),
                                rx.table.column_header_cell(
                                    "Línea B (s)", 
                                    class_name="text-white"
                                )
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("124.97", class_name="text-white"),
                                rx.table.cell("93.02", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("118.62", class_name="text-white"),
                                rx.table.cell("104.95", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("126.48", class_name="text-white"),
                                rx.table.cell("105.89", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("135.23", class_name="text-white"),
                                rx.table.cell("100.37", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("117.66", class_name="text-white"),
                                rx.table.cell("108.06", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("117.66", class_name="text-white"),
                                rx.table.cell("114.85", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("135.79", class_name="text-white"),
                                rx.table.cell("132.63", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("127.67", class_name="text-white"),
                                rx.table.cell("112.09", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("115.31", class_name="text-white"),
                                rx.table.cell("113.09", class_name="text-white")
                            ),
                            rx.table.row(
                                rx.table.cell("125.43", class_name="text-white"),
                                rx.table.cell("109.11", class_name="text-white")
                            )
                        ),
                        variant="surface",
                        class_name="bg-black mb-8 w-full",
                    ),
                    rx.text(
                        "Referencias: [2][5][38] Creado usando pandas con funciones de estadística.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.heading(
                        "A) Análisis descriptivo y visualización de datos",
                        size="7",
                        class_name="text-white",
                    ),
                    rx.heading(
                        "Medidas de tendencia central",
                        size="5",
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "Las medidas de tendencia central nos ayudan a entender el valor central o típico de nuestros datos [33][34]. La media nos da el promedio, la mediana el valor central y la moda el valor más frecuente.",
                        class_name="text-white mb-4",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Medida", class_name="text-white"),
                                rx.table.column_header_cell("Descripción", class_name="text-white"),
                                rx.table.column_header_cell("Línea A", class_name="text-white"),
                                rx.table.column_header_cell("Línea B", class_name="text-white"),
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("Media", class_name="text-white"),
                                rx.table.cell("Promedio de todos los valores", class_name="text-white"),
                                rx.table.cell("118.96 s", class_name="text-white"),
                                rx.table.cell("110.27 s", class_name="text-white"),
                            ),
                            rx.table.row(
                                rx.table.cell("Mediana", class_name="text-white"),
                                rx.table.cell("Valor central que divide el conjunto en dos partes iguales", class_name="text-white"),
                                rx.table.cell("119.0 s", class_name="text-white"),
                                rx.table.cell("110.0 s", class_name="text-white"),
                            ),
                            rx.table.row(
                                rx.table.cell("Moda", class_name="text-white"),
                                rx.table.cell("Valor que aparece con más frecuencia", class_name="text-white"),
                                rx.table.cell("120 s", class_name="text-white"),
                                rx.table.cell("111 s", class_name="text-white"),
                            ),
                        ),
                        variant="surface",
                        class_name="bg-black mb-4 w-full",
                    ),
                    rx.text(
                        "Referencias: [2][33] Creado usando pandas con funciones de estadística.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.text(
                        "El análisis muestra que la Línea B es más rápida que la Línea A, con una diferencia promedio de 8.7 segundos (118.96s vs 110.27s).",
                        class_name="text-white mb-4",
                    ),
                    rx.heading(
                        "Medidas de dispersión",
                        size="5",
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "Las medidas de dispersión nos indican qué tan dispersos están los datos alrededor de su valor central [34]. La desviación estándar, varianza y rango nos ayudan a entender la variabilidad de los datos.",
                        class_name="text-white mb-4",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Medida", class_name="text-white"),
                                rx.table.column_header_cell("Descripción", class_name="text-white"), 
                                rx.table.column_header_cell("Línea A", class_name="text-white"),
                                rx.table.column_header_cell("Línea B", class_name="text-white"),
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("Desviación estándar", class_name="text-white"),
                                rx.table.cell("Medida de dispersión respecto a la media", class_name="text-white"),
                                rx.table.cell("9.08 s", class_name="text-white"),
                                rx.table.cell("11.44 s", class_name="text-white"),
                            ),
                            rx.table.row(
                                rx.table.cell("Varianza", class_name="text-white"),
                                rx.table.cell("Promedio de las desviaciones al cuadrado", class_name="text-white"),
                                rx.table.cell("82.48 s²", class_name="text-white"),
                                rx.table.cell("130.97 s²", class_name="text-white"),
                            ),
                            rx.table.row(
                                rx.table.cell("Rango", class_name="text-white"),
                                rx.table.cell("Diferencia entre valor máximo y mínimo", class_name="text-white"),
                                rx.table.cell("44.72 s", class_name="text-white"),
                                rx.table.cell("55.67 s", class_name="text-white"),
                            ),
                            rx.table.row(
                                rx.table.cell("Coeficiente de variación", class_name="text-white"),
                                rx.table.cell("Variabilidad relativa respecto a la media", class_name="text-white"),
                                rx.table.cell("7.63%", class_name="text-white"),
                                rx.table.cell("10.38%", class_name="text-white"),
                            ),
                        ),
                        variant="surface",
                        class_name="bg-black mb-8 w-full",
                    ),
                    rx.text(
                        "Referencias: [2][33] Creado usando pandas con funciones de estadística.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.text(
                        "El análisis muestra que la Línea A tiene una desviación estándar de 9.08 segundos, lo que indica que los tiempos de producción son relativamente consistentes. En comparación, la Línea B tiene una desviación estándar de 11.44 segundos, también se sugiere una mayor variabilidad en los tiempos de producción con el coeficiente de variación del 10.38%. Esto significa que la Línea A es más predecible en términos de tiempos de producción, mientras que la Línea B presenta una mayor variabilidad.",
                        class_name="text-white mb-4",

                    ),
                    rx.heading(
                        "Medidas de forma",
                        size="5",
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "Las medidas de forma nos ayudan a entender la distribución de los datos [33][34]. La asimetría nos indica si la distribución está sesgada hacia la izquierda o derecha, mientras que la curtosis nos dice qué tan puntiaguda o plana es la distribución.",
                        class_name="text-white mb-4",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Medida", class_name="text-white"),
                                rx.table.column_header_cell("Descripción", class_name="text-white"),
                                rx.table.column_header_cell("Línea A", class_name="text-white"),
                                rx.table.column_header_cell("Línea B", class_name="text-white"),
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("Asimetría", class_name="text-white"),
                                rx.table.cell("Indica el grado y dirección de asimetría de la distribución", class_name="text-white"),
                                rx.table.cell("-0.18", class_name="text-white"),
                                rx.table.cell("0.39", class_name="text-white"),
                            ),
                            rx.table.row(
                                rx.table.cell("Curtosis", class_name="text-white"),
                                rx.table.cell("Indica qué tan puntiaguda o plana es la distribución", class_name="text-white"), 
                                rx.table.cell("-0.10", class_name="text-white"),
                                rx.table.cell("0.03", class_name="text-white"),
                            ),
                        ),

                        variant="surface",
                        class_name="bg-black mb-8 w-full",
                    ),

                    rx.text(
                        "Referencias: [2][33] Creado usando pandas con funciones de estadística.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.text(
                        "El análisis muestra que la Línea A tiene una asimetría de -0.18, lo que indica que está ligeramente sesgada a la izquierda, mientras que la Línea B tiene una asimetría de 0.39, indicando un sesgo a la derecha. La curtosis de ambas líneas es cercana a 0, lo que sugiere que ambas distribuciones son relativamente planas y no tienen colas pesadas.",
                        class_name="text-white mb-4",
                    ),
                    
                    # Gráficos
                    rx.heading(
                        "Gráficos: Histograma, boxplot y tallos de hojas",
                        size="7",
                        class_name="text-white mb-4 mt-8",
                    ),
                    rx.text(
                        "Entender cómo se ven nuestros datos gráficamente es parte fundamental en un análisis estadístico [33][34], aquí encontraremos el significado de las figuras y colores que le dan sentido a la estadística",
                        class_name="text-white mb-4",
                    ),
                    rx.heading(
                        "Gráfico de histograma",
                        size="6",
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "Un histograma es una representación gráfica de la distribución de un conjunto de datos [44]. Se utiliza para mostrar la frecuencia de los datos en intervalos específicos, lo que permite visualizar la forma de la distribución.",
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/histogram.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 w-full",
                    ),
                    rx.text(
                        "Referencias: [3][9] Creado usando Matplotlib con funciones de histograma.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.heading(
                        "Gráfico de boxplot",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "Un boxplot es una representación gráfica que muestra la distribución de un conjunto de datos a través de sus cuartiles [3][6][33]. Permite identificar la mediana, los cuartiles y valores de tipo outlier.",
                        class_name="text-white mb-4",
                    ),
                    rx.image(
                        src='/box_plot.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 w-full",
                    ),
                    rx.text(
                        "Referencias: [3][6][12] Creado usando Matplotlib y Seaborn para visualización de box plots.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.heading(
                        "Gráfico de tallos y hojas",
                        size="6",
                        class_name="text-white mb-4 pt-4",
                    ),
                    rx.text(
                        "El gráfico de tallos y hojas es un tipo de gráfico que permite ver la distribución de los datos manteniendo su orden original y su valor exacto [17][33], lo que lo hace especialmente útil para análisis exploratorios. A diferencia de otros gráficos como los histogramas, este conserva los valores individuales, permitiendo una inspección más precisa. Además, facilita la identificación de valores atípicos (outliers), la detección de la moda, y proporciona una visión clara de la simetría o asimetría en la distribución.",
                        class_name="text-white mb-4"
                    ),
                    rx.image(
                        src='/stem_comparison_tables.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 w-full",
                    ),
                    rx.text(
                        "Referencias: [3][17] Creado usando Matplotlib con funciones de gráficos de tallos y hojas.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    
                    # Identificar la distribución
                    rx.heading(
                        "B) Identificar la distribución indicada",
                        size="7",
                        class_name="text-white mb-4 mt-8",
                    ),
                    rx.text(
                        "Para identificar la distribución de los datos, se aplican pruebas de bondad de ajuste [25][32][33][34]. Estas pruebas comparan la distribución observada con varias distribuciones teóricas para determinar cuál se ajusta mejor a los datos. En este caso, se aplicaron las pruebas de Kolmogorov-Smirnov (KS) para las distribuciones Normal, Exponencial y Weibull.",
                        class_name="text-white mb-4",
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell(
                                    "Normal",
                                    class_name="text-white"
                                ),
                                rx.table.column_header_cell(
                                    "Exponencial", 
                                    class_name="text-white"
                                ),
                                rx.table.column_header_cell(
                                    "Weibull",
                                    class_name="text-white"
                                ),
                                rx.table.column_header_cell(
                                    "Mejor ajuste",
                                    class_name="text-white"
                                )
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell(
                                    "0.940",
                                    class_name="text-white"
                                ),
                                rx.table.cell(
                                    "5.82e-30",
                                    class_name="text-white"
                                ),
                                rx.table.cell(
                                    "0.824",
                                    class_name="text-white"
                                ),
                                rx.table.cell(
                                    "Normal",
                                    class_name="text-white"
                                )
                            ),
                            rx.table.row(
                                rx.table.cell(
                                    "0.651",
                                    class_name="text-white"
                                ),
                                rx.table.cell(
                                    "5.11e-29",
                                    class_name="text-white"
                                ),
                                rx.table.cell(
                                    "0.560",
                                    class_name="text-white"
                                ),
                                rx.table.cell(
                                    "Normal",
                                    class_name="text-white"
                                )
                            )
                        ),
                        variant="surface",
                        class_name="bg-black mb-8 w-full",
                    ),
                    
                    rx.text(
                        "En la tabla anterior, se presentan los resultados de las pruebas de bondad de ajuste para las distribuciones Normal, Exponencial y Weibull [2][7][8]. La columna 'Mejor ajuste' indica cuál distribución se ajusta mejor a los datos de cada línea de producción. Si el valor p es menor que el nivel de significancia (α = 0.05), se rechaza la hipótesis nula de que los datos siguen esa distribución.",
                        class_name="text-white mb-4 font-bold"
                    ),
                    rx.image(
                        src='/Línea_A_dist_fit.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 w-full",
                    ),
                    rx.text(
                        "Referencias: [3][18] Ajuste de distribución usando SciPy y visualización con Matplotlib.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.text(
                        "Se muestra el gráfico de la Línea A con la distribución Normal superpuesta. La línea azul representa la distribución Normal ajustada a los datos de la Línea A. Se observa que la distribución Normal se ajusta bastante bien a los datos.",
                        class_name="text-white mb-4"
                    ),
                    rx.image(
                        src='/Línea_B_dist_fit.png',
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 w-full",
                    ),
                    rx.text(
                        "Referencias: [3][18] Ajuste de distribución usando SciPy y visualización con Matplotlib.",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    rx.text(
                        "En el gráfico de la Línea B con la distribución Normal y weibull superpuesta. La línea azul representa la distribución Normal ajustada a los datos de la Línea B.",
                        class_name="text-white mb-4"
                    ),
                    rx.heading(
                        "C) Cálculos de probabilidad según la distribución ajustada", 
                        size="7",
                        class_name="text-white mb-4 mt-8",
                    ),
                    rx.text(
                        "Calcule la probabilidad de que un ciclo exceda el tiempo estándar establecido en 120 segundos. Determine el tiempo máximo que debe establecerse como estándar para garantizar que el 90% de los ciclos se completen dentro de ese tiempo.",
                        class_name="text-white mb-4",

                    ),
                    rx.text(
                                            """Línea A (distribución usada: Normal, mejor ajuste: Normal)
                    →  P(T>120) = 45.45%   |   t_90 = 130.60 s

                    Línea B (distribución usada: Normal, mejor ajuste: Normal)  
                    →  P(T>120) = 19.75%   |   t_90 = 124.93 s""",
                                            class_name="text-white bg-[#1e1e1e] p-4 rounded-lg font-mono mb-4 whitespace-pre",
                    ),
                    rx.text(
                        "Referencias: [3][18][32][33]",
                        class_name="text-gray-400 text-sm mb-4 text-center italic",
                    ),
                    
                    rx.heading(
                        "Interpretación de resultados",
                        size="6",
                        class_name="text-white mb-4 mt-4",
                    ),
                    rx.text(
                        "Los resultados del análisis probabilístico muestran lo siguiente:",
                        class_name="text-white mb-2",
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.text(
                                rx.text("Línea A: ", as_="span", class_name="font-bold"), 
                                "La probabilidad de que un ciclo exceda el tiempo estándar de 120 segundos es del 45.45%. Esto significa que casi la mitad de los ciclos de producción en esta línea sobrepasarán el tiempo establecido, lo cual indica una eficiencia comprometida."
                            )
                        ),
                        rx.list_item(
                            rx.text(
                                rx.text("Línea A (tiempo estándar para 90%): ", as_="span", class_name="font-bold"), 
                                "Para garantizar que el 90% de los ciclos se completen dentro del tiempo estándar, este debería establecerse en 130.60 segundos, lo que representa un incremento de 10.6 segundos respecto al valor actual."
                            )
                        ),
                        rx.list_item(
                            rx.text(
                                rx.text("Línea B: ", as_="span", class_name="font-bold"), 
                                "La probabilidad de que un ciclo exceda los 120 segundos es considerablemente menor, solo del 19.75%. Esto muestra que la Línea B es más eficiente y consistente en términos de tiempos de producción."
                            )
                        ),
                        rx.list_item(
                            rx.text(
                                rx.text("Línea B (tiempo estándar para 90%): ", as_="span", class_name="font-bold"), 
                                "Para garantizar que el 90% de los ciclos se completen a tiempo en esta línea, el estándar debería establecerse en 124.93 segundos, un incremento mucho menor de solo 4.93 segundos."
                            )
                        ),
                        class_name="text-white mb-4 pl-6",
                    ),
                    rx.text(
                        "Con base en estos resultados, podemos concluir que la Línea B presenta un mejor desempeño operativo en términos de tiempos de ciclo [3][16][32][33]. La menor variabilidad y el tiempo promedio más bajo en la Línea B sugieren que podría ser beneficioso analizar qué factores contribuyen a su mejor rendimiento para potencialmente implementarlos también en la Línea A y mejorar su eficiencia.",
                        class_name="text-white mb-4 font-bold",
                    ),
                    rx.heading(
                        "D) Intervalos de confianza al 95% para las líneas",
                        size="7",
                        class_name="text-white mb-4 mt-8",
                    ),
                    rx.text(
                        "Los intervalos de confianza al 95% para las medias de las líneas A y B son los siguientes [7][8][32][33][36]:",
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "IC 95% μ_A: 117.16 – 120.76",
                        class_name="text-white mb-2 font-mono bg-black/30 p-2 rounded whitespace-pre",
                    ),
                    rx.text(
                        "IC 95% μ_B: 108.00 – 112.54", 
                        class_name="text-white mb-4 font-mono bg-black/30 p-2 rounded whitespace-pre",
                    ),
                    rx.text(
                        "Esto significa que estamos un 95% seguros de que la media real del tiempo de producción para la Línea A está entre 117.16 y 120.76 segundos, mientras que para la Línea B está entre 108.00 y 112.54 segundos.",
                        class_name="text-white mb-4",
                    ),
                    
                    # Prueba de hipótesis
                    rx.heading(
                        "E) Prueba de hipótesis para comparar tiempos medios",
                        size="7",
                        class_name="text-white mb-4 mt-8",
                    ),
                    rx.text(
                        "Para determinar si existe una diferencia estadísticamente significativa entre los tiempos medios de ciclo de ambas líneas de producción, se realizó una prueba t de Student para muestras independientes [25][33][35] (también conocida como prueba t de Welch, ya que las varianzas son diferentes).",
                        class_name="text-white mb-4",
                    ),
                    rx.text(
                        "Prueba de hipótesis para comparar tiempos medios de ciclo:",
                        class_name="text-white mb-2 font-bold",
                    ),
                    rx.heading(
                        "Hipótesis:",
                        size="6", 
                        class_name="text-white mb-2",
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.text("H₀: μ_A = μ_B (No hay diferencia significativa entre los tiempos medios)")
                        ),
                        rx.list_item(
                            rx.text("H₁: μ_A ≠ μ_B (Existe diferencia significativa entre los tiempos medios)")
                        ),
                        class_name="text-white mb-4 pl-6",
                    ),
                    rx.heading(
                        "Resultados:",
                        size="6",
                        class_name="text-white mb-2", 
                    ),
                    rx.unordered_list(
                        rx.list_item(rx.text("Estadístico t: 5.9508")),
                        rx.list_item(rx.text("Valor p: 0.000000012784")),
                        rx.list_item(rx.text("Media Línea A: 118.96 segundos")),
                        rx.list_item(rx.text("Media Línea B: 110.27 segundos")),
                        rx.list_item(rx.text("Diferencia de medias: 8.69 segundos")),
                        class_name="text-white mb-4 pl-6",
                    ),
                    rx.heading(
                        "Interpretación:",
                        size="6",
                        class_name="text-white mb-2",
                    ),
                    rx.unordered_list(
                        rx.list_item(rx.text("Se rechaza la hipótesis nula (p < 0.05)")),
                        rx.list_item(rx.text("Existe evidencia estadísticamente significativa de que los tiempos medios de ciclo son diferentes")),
                        rx.list_item(rx.text("La Línea B es en promedio 8.69 segundos más rápida que la Línea A")),
                        rx.list_item(rx.text("Esta diferencia es estadísticamente significativa y tiene implicaciones prácticas para la gestión del proceso")),
                        class_name="text-white mb-4 pl-6",
                    ),
                    rx.text(
                        "Esta prueba nos permite tomar decisiones basadas en evidencia estadística sobre si las diferencias observadas en los tiempos de ciclo son significativas o podrían deberse al azar [36]. Los resultados tienen importantes implicaciones para la gestión del proceso, ya que nos ayudan a identificar si una línea de producción es significativamente más eficiente que la otra.",
                        class_name="text-white mb-4",
                    ),
                    
                    # Comparación con artículo científico
                    rx.heading(
                        "F) Comparación con artículo científico",
                        size="7",
                        class_name="text-white mb-4 mt-8",
                    ),
                    rx.image(
                        src='/article_image.png',
                        height="300px",
                        class_name="p-4 rounded-2xl bg-black shadow-lg mb-4 object-contain",
                    ),
                    rx.text(
                        "Referencias: Artículo científico comparativo citado en el texto.",
                        class_name="text-gray-400 text-sm mb-2 text-center italic",
                    ),
                    rx.text(
                        "Se realizó una comparación de las técnicas estadísticas utilizadas en este análisis con las del artículo 'Design the Abnormal Object Detection System Using Template Matching and Subtract Background Algorithm' [15], obtenido a través de la base de datos Springer de la universidad.",
                        class_name="text-white mb-4",
                    ),
                    rx.link(
                        "Artículo científico comparativo",
                        href="https://shibaura.elsevierpure.com/en/publications/design-the-abnormal-object-detection-system-using-template-matchi",
                        class_name="text-purple-300 hover:text-purple-500 transition-colors mb-4",
                    ),
                    rx.heading(
                        "Similitudes metodológicas",
                        size="6",
                        class_name="text-white mb-2",
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.text(
                                "Uso de distribuciones estadísticas para modelar el comportamiento de los datos: En nuestro análisis aplicamos pruebas de bondad de ajuste para identificar la distribución que mejor se adapta a los datos (Normal, Exponencial, Weibull), mientras que en el artículo se utilizan distribuciones estadísticas para modelar patrones normales y anómalos en la detección de objetos."
                            )
                        ),
                        rx.list_item(
                            rx.text(
                                "Aplicación de pruebas de hipótesis para la toma de decisiones: Nuestro análisis utiliza la prueba t para determinar si hay diferencia significativa entre líneas de producción; similarmente, el algoritmo de detección de objetos anómalos emplea pruebas estadísticas para decidir si un objeto se desvía significativamente del patrón esperado."
                            )
                        ),
                        rx.list_item(
                            rx.text(
                                "Análisis de variabilidad mediante medidas de dispersión: En ambos casos se utilizan medidas como la desviación estándar y la varianza para cuantificar y analizar la variabilidad de los datos, ya sea en tiempos de ciclo o en características de imágenes."
                            )
                        ),
                        class_name="text-white mb-4 pl-6",
                    ),
                    rx.heading(
                        "Diferencias metodológicas",
                        size="6",
                        class_name="text-white mb-2",
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.text(
                                "Dominio de aplicación: Nuestro análisis se centra en datos temporales (tiempos de ciclo en procesos productivos), mientras que el artículo trabaja con datos espaciales y visuales (detección de objetos en imágenes)."
                            )
                        ),
                        rx.list_item(
                            rx.text(
                                "Técnicas específicas: El artículo implementa algoritmos especializados como Template Matching y Subtract Background que no tienen equivalente directo en nuestro análisis estadístico tradicional de procesos industriales."
                            )
                        ),
                        rx.list_item(
                            rx.text(
                                "Métricas de evaluación: En nuestro caso utilizamos p-valores e intervalos de confianza para evaluar los resultados, mientras que el sistema de detección descrito en el artículo emplea métricas como precisión, recall y tasas de falsos positivos/negativos típicas del campo de visión por computadora."
                            )
                        ),
                        rx.list_item(
                            rx.text(
                                "Enfoque de modelado: Nuestro enfoque es paramétrico y basado en distribuciones teóricas conocidas, mientras que el artículo utiliza un enfoque híbrido que combina técnicas estadísticas con procesamiento de imágenes y aprendizaje por patrones."
                            )
                        ),
                        class_name="text-white mb-4 pl-6",
                    ),
                    rx.text(
                        "Esta comparación ilustra cómo los principios estadísticos se aplican en diversos campos, aunque con adaptaciones específicas según el dominio de aplicación [38][39]. Tanto nuestro análisis de procesos industriales como el sistema de detección de anomalías comparten fundamentos estadísticos, pero implementados de manera diferente según los objetivos específicos.",
                        class_name="text-white mb-4",
                    ),
                    
                    align="start",
                    spacing="4",
                    width="100%",
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
app.add_page(part1)
