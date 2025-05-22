import reflex as rx
from rxconfig import config
class State(rx.State):
    """The app state."""
    ...

def part3() -> rx.Component:
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
                    "Part 3 - Aplicando la estadistica en la vida real",
                    size="8",
                    class_name="text-white mb-4",
                ),
                rx.text(
                    "Aplicando estadística descriptiva e inferencial a problemas reales",
                    class_name="text-white text-xl mb-6",
                    style={"white-space": "pre-line"},
                ),
                
                # Contenido de los dos problemas planteados
                rx.vstack(
                    rx.box(
                        rx.heading(
                            "A) Problemas planteados",
                            size="6",
                            class_name="text-purple-300 mb-4",
                        ),
                        rx.text(
                            "Tenemos 2 problemas planteados que involucran la estadística descriptiva e inferencial, "
                            "que son útiles y dan significado de lo importante que es esta ciencia hoy en día.",
                            class_name="text-gray-200 mb-6",
                            style={"white-space": "pre-line"},
                        ),
                        class_name="w-full",
                    ),
                    
                    # Problema 1: Criptografía Estadística en Ciberseguridad
                    rx.box(
                        rx.heading(
                            "Problema 1: Criptografía Estadística en Ciberseguridad",
                            size="5",
                            class_name="text-purple-200 mb-3",
                        ),
                        rx.text(
                            "La criptografía moderna se sustenta en principios estadísticos y matemáticos que permiten proteger la información digital [29][55]. "
                            "Los algoritmos criptográficos utilizan propiedades estadísticas para generar claves seguras y evaluar su resistencia frente a ataques.",
                            class_name="text-gray-200 mb-2",
                        ),
                        rx.heading(
                            "Fundamentos estadísticos en criptografía",
                            size="6",
                            class_name="text-gray-300 mb-2",
                        ),
                        rx.unordered_list(
                            rx.list_item("Generación de números aleatorios y pseudoaleatorios [52][56]", class_name="text-gray-200"),
                            rx.list_item("Análisis de frecuencia para romper cifrados simples [53]", class_name="text-gray-200"),
                            rx.list_item("Pruebas estadísticas para validar la calidad de cifrados [52]", class_name="text-gray-200"),
                            rx.list_item("Distribuciones de probabilidad en la generación de claves [50][51]", class_name="text-gray-200"),
                            rx.list_item("Análisis de entropía para medir la fortaleza criptográfica [56]", class_name="text-gray-200"),
                            class_name="text-gray-200 mb-4 pl-6",
                        ),
                        rx.text(
                            "La criptografía asimétrica (RSA, ECC) depende de problemas matemáticamente difíciles como la factorización de números grandes "
                            "o el logaritmo discreto. La seguridad de estos sistemas se basa en la distribución estadística de números primos y "
                            "en la improbabilidad computacional de resolver ciertos problemas en tiempo polinómico [51][57].",
                            class_name="text-gray-200 mb-3",
                        ),
                        rx.heading(
                            "Aplicaciones de la estadística en ciberdefensa",
                            size="6",
                            class_name="text-gray-300 mb-2",
                        ),
                        rx.box(
                            rx.text(
                                "Visualización de propiedades estadísticas en criptografía",
                                class_name="text-white font-bold text-center mb-2",
                            ),
                            rx.text(
                                "• Distribuciones de frecuencia en datos cifrados vs. aleatorios",
                                class_name="text-gray-200 mb-1",
                            ),
                            rx.text(
                                "• Análisis de correlación entre texto plano y cifrado",
                                class_name="text-gray-200 mb-1",
                            ),
                            rx.text(
                                "• Medidas de entropía y aleatoriedad en secuencias cifradas",
                                class_name="text-gray-200 mb-1",
                            ),
                            rx.text(
                                "• Patrones estadísticos utilizados en criptoanálisis",
                                class_name="text-gray-200 mb-1",
                            ),
                            class_name="p-6 bg-black rounded-2xl shadow-lg mb-4 border border-purple-500/30",
                        ),
                        rx.text(
                            "Referencias: [52][56] Propiedades estadísticas del proceso de cifrado.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.text(
                            "El análisis estadístico es fundamental en la detección de anomalías y ataques cibernéticos. "
                            "Mediante la aplicación de pruebas de hipótesis, intervalos de confianza y análisis de regresión, "
                            "los sistemas de seguridad pueden identificar patrones sospechosos y distinguirlos del tráfico normal [57][58].",
                            class_name="text-gray-200 mb-3",
                        ),
                        rx.text(
                            "Un ejemplo concreto es el análisis estadístico del tiempo de ejecución (timing attacks), donde pequeñas "
                            "variaciones en el tiempo de procesamiento pueden revelar información sobre claves privadas. "
                            "Estos ataques se basan en análisis de varianza (ANOVA) y pruebas de correlación para extraer "
                            "información sensible de sistemas criptográficos [50][55].",
                            class_name="text-gray-200 mb-3",
                        ),
                        rx.heading(
                            "Criptografía cuántica y estadística",
                            size="6",
                            class_name="text-gray-300 mb-2",
                        ),
                        rx.text(
                            "La criptografía cuántica representa el futuro de la seguridad digital, utilizando principios de la mecánica cuántica "
                            "como la superposición y el entrelazamiento. Los protocolos como QKD (Quantum Key Distribution) dependen de "
                            "distribuciones estadísticas para detectar interceptaciones y garantizar la seguridad [51][57].",
                            class_name="text-gray-200 mb-3",
                        ),
                        rx.text(
                            "El análisis estadístico es esencial para garantizar que los sistemas criptográficos sean realmente seguros "
                            "y resistentes a diversos tipos de ataques, desde fuerza bruta hasta criptoanálisis diferencial y lineal.",
                            class_name="text-gray-200 mb-3",
                        ),
                        rx.box(
                            rx.text(
                                "Para más información sobre análisis estadístico en ciberseguridad, consultar:",
                                class_name="text-gray-200",
                            ),
                            rx.link(
                                "NIST Cryptographic Standards and Guidelines [58]",
                                href="https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines", 
                                class_name="text-blue-300 hover:text-blue-200 transition-colors",
                            ),
                            class_name="p-4 bg-purple-900/30 rounded-xl border border-purple-500/30 mb-8",
                        ),
                        class_name="w-full p-6 bg-gradient-to-br from-purple-900/40 to-black/40 rounded-2xl shadow-lg border border-purple-500/20 mb-6",
                    ),
                    
                    # Problema 2: El problema del Titanic
                    rx.box(
                        rx.heading(
                            "(A-B) Campo 2: Ciencia de datos y análisis (El problema del Titanic)",
                            size="5",
                            class_name="text-purple-200 mb-3",
                        ),
                        rx.text(
                            "Nuestro segundo campo es la ciencia de datos y el análisis de ello. La ingeniería de sistemas y "
                            "todas estas ciencias computacionales han dado oportunidad a la revolución actual de la inteligencia "
                            "artificial y la implementación de modelos matemáticos y estadísticos para la solución de problemas actuales [27][28]. "
                            "Con este campo queremos enfocarnos en problemas que utilicen estas ciencias que ya mencionamos y toda la "
                            "parte computacional moderna.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.text(
                            "Gracias a ello planteamos la siguiente aplicación de todo lo anterior y se trata del problema del Titanic [24]. "
                            "Nos plantean un dataset roto y real con muchos valores vacíos, campos faltantes y bastantes datos inexistentes "
                            "que provienen del incidente real del barco RMS TITANIC ocurrido el 14 de abril de 1912 en un recorrido desde "
                            "Reino Unido a Estados Unidos. La distorsión del tiempo, las personas fallecidas sin reconocer y las condiciones "
                            "estadísticas de ese tiempo generaron la pérdida de muchos datos y el significado del estado base del dataset.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.text(
                            "La misión es limpiarlo, eliminar variables no relevantes, identificar factores de supervivencia y crear "
                            "una solución predictiva para poder conocer según datos ingresados si una persona llega a sobrevivir o no.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.heading(
                            "Temas y conceptos aplicados en la solucion:",
                            size="6",
                            class_name="text-purple-200 mt-4 mb-2",
                        ),
                        rx.unordered_list(
                            rx.list_item("Estadística descriptiva"),
                            rx.list_item("Representaciones gráficas"),
                            rx.list_item("Métodos de optimización"),
                            rx.list_item("Normalización y estandarización de datos"),
                            rx.list_item("Funciones matemáticas (Función Sigmoid)"),
                            rx.list_item("Validación cruzada"),
                            rx.list_item("Métodos de entrenamiento"),
                            rx.list_item("Matrices de confusión"),
                            class_name="text-gray-200 mb-4 pl-6",
                        ),
                        rx.heading(
                            "Ciencias y campos fundamentales de la ciencia de datos:",
                            size="6",
                            class_name="text-purple-200 mb-2",
                        ),
                        rx.unordered_list(
                            rx.list_item("Matemáticas"),
                            rx.list_item("Estadística"),
                            rx.list_item("Cálculo"),
                            rx.list_item("Álgebra lineal"),
                            rx.list_item("Álgebra tensorial"),
                            rx.list_item("Física"),
                            rx.list_item("Trigonometría"),
                            rx.list_item("Geometría analítica"),
                            rx.list_item("Paradigmas matemáticos de programación"),
                            rx.list_item("Teoría de grafos"),
                            class_name="text-gray-200 mb-4 pl-6",
                        ),
                        rx.box(
                            rx.text(
                                "Este segundo campo sera nuestra elección y desarrollaremos como problema principal",
                                class_name="text-white font-semibold",
                            ),
                            class_name="p-4 bg-purple-700/40 rounded-xl border border-purple-500/30 mb-4 text-center",
                        ),
                        rx.heading(
                            "C) Obtencion de los datos",
                            size="6",
                            class_name="text-purple-200 mb-2",
                        ),
                        rx.text (
                            "Los datos fueron obtenidos de Kaggle. Kaggle es una aplicación-comunidad que reúne todo lo enfocado en el análisis de datos, desde datasets, modelos de machine learning y fundamentos matemáticos y estadísticos para resolver problemas. El dataset original es el siguiente:",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("pclass", class_name="text-white"),
                                    rx.table.column_header_cell("survived", class_name="text-white"), 
                                    rx.table.column_header_cell("name", class_name="text-white"),
                                    rx.table.column_header_cell("sex", class_name="text-white"),
                                    rx.table.column_header_cell("age", class_name="text-white"),
                                    rx.table.column_header_cell("sibsp", class_name="text-white"),
                                    rx.table.column_header_cell("parch", class_name="text-white"),
                                    rx.table.column_header_cell("ticket", class_name="text-white"),
                                    rx.table.column_header_cell("fare", class_name="text-white"),
                                    rx.table.column_header_cell("cabin", class_name="text-white"),
                                    rx.table.column_header_cell("embarked", class_name="text-white"),
                                    rx.table.column_header_cell("boat", class_name="text-white"),
                                    rx.table.column_header_cell("body", class_name="text-white"),
                                    rx.table.column_header_cell("home.dest", class_name="text-white")
                                )
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Allen, Miss. Elisabeth Walton", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("29.0", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("24160", class_name="text-white"),
                                    rx.table.cell("211.3375", class_name="text-white"),
                                    rx.table.cell("B5", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("2", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("St Louis, MO", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Allison, Master. Hudson Trevor", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("0.9167", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("2", class_name="text-white"),
                                    rx.table.cell("113781", class_name="text-white"),
                                    rx.table.cell("151.55", class_name="text-white"),
                                    rx.table.cell("C22 C26", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("11", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("Montreal, PQ / Chesterville, ON", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Allison, Miss. Helen Loraine", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("2.0", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("2", class_name="text-white"),
                                    rx.table.cell("113781", class_name="text-white"),
                                    rx.table.cell("151.55", class_name="text-white"),
                                    rx.table.cell("C22 C26", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("Montreal, PQ / Chesterville, ON", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Allison, Mr. Hudson Joshua Creighton", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("30.0", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("2", class_name="text-white"),
                                    rx.table.cell("113781", class_name="text-white"),
                                    rx.table.cell("151.55", class_name="text-white"),
                                    rx.table.cell("C22 C26", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("135.0", class_name="text-white"),
                                    rx.table.cell("Montreal, PQ / Chesterville, ON", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Allison, Mrs. Hudson J C (Bessie Waldo Daniels)", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("25.0", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("2", class_name="text-white"),
                                    rx.table.cell("113781", class_name="text-white"),
                                    rx.table.cell("151.55", class_name="text-white"),
                                    rx.table.cell("C22 C26", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("Montreal, PQ / Chesterville, ON", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Anderson, Mr. Harry", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("48.0", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("19952", class_name="text-white"),
                                    rx.table.cell("26.55", class_name="text-white"),
                                    rx.table.cell("E12", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("3", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("New York, NY", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Andrews, Miss. Kornelia Theodosia", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("63.0", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("13502", class_name="text-white"),
                                    rx.table.cell("77.9583", class_name="text-white"),
                                    rx.table.cell("D7", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("10", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("Hudson, NY", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Andrews, Mr. Thomas Jr", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("39.0", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("112050", class_name="text-white"),
                                    rx.table.cell("0.0", class_name="text-white"),
                                    rx.table.cell("A36", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("Belfast, NI", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Appleton, Mrs. Edward Dale (Charlotte Lamson)", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("53.0", class_name="text-white"),
                                    rx.table.cell("2", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("11769", class_name="text-white"),
                                    rx.table.cell("51.4792", class_name="text-white"),
                                    rx.table.cell("C101", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("D", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("Bayside, Queens, NY", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Artagaveytia, Mr. Ramon", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("71.0", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("PC 17609", class_name="text-white"),
                                    rx.table.cell("49.5042", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("C", class_name="text-white"),
                                    rx.table.cell("nan", class_name="text-white"),
                                    rx.table.cell("22.0", class_name="text-white"),
                                    rx.table.cell("Montevideo, Uruguay", class_name="text-white")
                                )
                            ),
                            variant="surface",
                            class_name="bg-black mb-8 w-full",
                        ),
                        rx.heading(
                            "D) Analisis estadistico ",
                            size="8",
                            class_name="text-purple-200 mb-2 font-bold",
                        ),
                        rx.text(
                            "Antes de comenzar con el análisis estadístico, voy a recordar que el proceso de limpieza fue muy largo y, por lo tanto, para no agobiar con tantos procesos, voy a resaltar lo más importante y los temas requeridos por la entrega.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.box(
                            rx.text(
                                "Si deseas ver el proceso completo que se hizo , ingresa al siguiente link (El desarollo esta en ingles)",
                                class_name="text-gray-200",
                            ),
                            rx.link(
                                "Link a Github",
                                href='https://github.com/CrisHzz/TitanicSurvivors/blob/main/DataCleaning/DatasetCleaning.ipynb'
                            ),
                            class_name="text-blue-300 hover:text-blue-200 transition-colors mb-8",
                        ),

                        rx.heading(
                            "Limpiar Nan Values", 
                            size="6",
                            class_name="text-purple-200 mb-2",
                        ),
                        rx.text(
                            "El primer paso es eliminar todos los NaN (Not a Number) que son los valores vacíos. y generan muchos problemas a la hora de realizar análisis estadísticos.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.image(
                            src='/datasetnan.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][24] Visualización de valores faltantes utilizando Pandas.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.heading(
                            "Eliminacion de variables (Sibsp y parch)",
                            size="6",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.text(
                            "Este conjunto de datos contiene datos innecesarios y es fundamental eliminar algunas columnas que no son útiles para el modelo. Sin embargo, otras columnas requieren un análisis para determinar si podemos prescindir de ellas. En este caso, vamos a analizar 2 variables para eliminar: (SibSp) y (Parch), que representan la cantidad de hermanos o cónyuges a bordo y la cantidad de padres o hijos a bordo respectivamente, para evidenciar si son relevantes para la supervivencia.",
                            class_name="text-gray-200 mb-4"
                        ),
                        rx.image(
                            src='/sibsp.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][3] Análisis de variable SibSp utilizando Pandas y Matplotlib.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.image(
                            src='/parch.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][3] Análisis de variable Parch utilizando Pandas y Matplotlib.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.text(
                            'Podemos concluir que la estructura familiar tuvo una influencia moderada en las probabilidades de supervivencia. Las personas que viajaban con un número pequeño de familiares (1-3) mostraron tasas de supervivencia más altas que aquellas que viajaban solas o con familias numerosas.\n\nSin embargo, esta variable por sí sola no es determinante. Las amplias barras de error en los gráficos indican una gran variabilidad, sugiriendo que otros factores como el género, la clase social y la edad probablemente jugaron un papel más decisivo',
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.heading(
                            "Costo del pasaje para la supervivencia",
                            size="6",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.text(
                            "El costo del pasaje es una variable que puede influir en la supervivencia. En este caso, vamos a analizar su impacto en la supervivencia de los pasajeros.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.image(
                            src='/fare.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][3][6] Análisis de tarifas utilizando Pandas, Matplotlib y Seaborn.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.text(
                            "El análisis muestra una clara correlación entre el precio del boleto y la supervivencia. Los datos revelan:",
                            class_name="text-gray-200 mb-2",
                        ),
                        rx.unordered_list(
                            [
                                rx.list_item(
                                    rx.text(
                                        "Tarifas bajas (£0 - £7.9): Tasa de supervivencia del 15% - 20%",
                                        class_name="text-gray-200"
                                    )
                                ),
                                rx.list_item(
                                    rx.text(
                                        "Tarifas medias (£14 - £27): Tasa de supervivencia del 40% - 45%",
                                        class_name="text-gray-200"
                                    )
                                ),
                                rx.list_item(
                                    rx.text(
                                        "Tarifas altas (£78 - £512): Tasa de supervivencia del 70% - 75%",
                                        class_name="text-gray-200"
                                    )
                                ),
                            ],
                            class_name="mb-4"
                        ),
                        rx.text(
                            "Los 'bins' son simplemente divisiones del rango de tarifas en 10 grupos iguales para facilitar el análisis visual. "
                            "Esta agrupación permite ver claramente cómo la tasa de supervivencia aumenta con el precio del boleto.\n\n"
                            "Esta variable es un fuerte predictor de supervivencia, probablemente porque refleja la clase social del pasajero, "
                            "que determinaba la ubicación del camarote (más cercano a la cubierta en primera clase) y el acceso prioritario a los botes salvavidas.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.heading(
                            "Edades faltantes en la media y llenado de valores en las cabinas y botes salvavidas",
                            size="6",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.text(
                            "El conjunto de datos presenta valores faltantes en tres variables importantes: edad, cabina y bote salvavidas. Para manejar estos datos faltantes [2][5][7]:\n\n"
                            "Para la edad, utilizamos la media como método de imputación. Esta decisión se basa en que la media es un estimador robusto que representa el valor típico de la edad de los pasajeros, minimizando el impacto en las distribuciones estadísticas y manteniendo la estructura general de los datos de edad.\n\n"
                            "En el caso de las cabinas (que son identificadores alfanuméricos que indican la ubicación del pasajero en el barco), creamos categorías especiales para aquellos registros sin asignación. Esto nos permite mantener la integridad del análisis sin perder información sobre los pasajeros sin cabina asignada.\n\n"
                            "De manera similar, para los botes salvavidas, asignamos identificadores especiales a aquellos registros sin información, permitiendo incluir estos casos en el análisis general de la distribución y uso de los botes salvavidas.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.image(
                            src='/meanclean.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][5][24] Limpieza de datos utilizando valores medios con Pandas y NumPy.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.heading(
                            "Compresion de graficas y analisis de supervivencia",
                            size="7",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.text(
                            "En esta sección, vamos a analizar gráficamente y a través de herramientas estadísticas diversos factores que pueden determinar la supervivencia de una persona en el Titanic. Este análisis nos permitirá comprender mejor las variables que influyeron en las probabilidades de sobrevivir al desastre.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.heading(
                            "Distribución de edades en el barco y en los embarques",
                            size="6",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.image(
                            src='/cakeage.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][3] Gráfico de pastel para distribución de edades creado con Matplotlib y Pandas.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.heading(
                            "Intervalo de confianza para encontrar la edad promedio",
                            size="4",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.image(
                            src='/confidentage.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][18][25] Intervalos de confianza para edad utilizando SciPy y Pandas.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.vstack(
                            rx.text(
                                "Tras analizar la edad promedio de los pasajeros del Titanic, podemos concluir que:",
                                class_name="text-gray-200",
                            ),
                            rx.ordered_list(
                                rx.list_item("La edad media de los pasajeros se encuentra entre 35.6 y 39.1 años, con un 95% de confianza."),
                                rx.list_item("Este intervalo relativamente estrecho nos indica que tenemos una buena estimación de la edad promedio real."),
                                rx.list_item("El análisis confirma que la mayoría de los pasajeros eran adultos de mediana edad, lo que coincide con el perfil demográfico de los viajeros transatlánticos de la época."),
                                rx.list_item("Tanto el método paramétrico (t de Student) como el no paramétrico (bootstrap) arrojan resultados similares, validando la robustez de nuestra estimación."),
                                class_name="text-gray-200 pl-6",
                            ),
                            rx.text(
                                "Este hallazgo es valioso para caracterizar correctamente a la población que viajaba en el Titanic y puede ayudar a contextualizar otros análisis demográficos y de supervivencia.",
                                class_name="text-gray-200",
                            ),
                            spacing="4",
                            class_name="mb-4",
                        ),

                        rx.heading(
                            "Mujeres vs Hombres , Quien sobrevive?",
                            size="4",
                            class_name="text-purple-200 mb-4",
                        ),

                        rx.image(
                            src='/survivors.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][3][6] Análisis de supervivencia por género utilizando Pandas, Matplotlib y Seaborn.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.text(
                            "El análisis revela que las mujeres tenían una tasa de supervivencia significativamente más alta que los hombres. "
                            "Esto sugiere que las mujeres recibieron un trato preferencial en la evacuación, De aqui sale famosa frase Mujeres y niños primero.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.heading(
                            "Puertos de embarque",
                            size="6",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.text(
                            "El RMS Titanic zarpó de Southampton, Inglaterra, y realizó escalas en Cherburgo, Francia, y Queenstown (actualmente Cobh), Irlanda ,vamos a analizar la distribucion de personas en los puertos de embarque ",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.image(
                            src='/embark.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [2][3][6] Análisis de puertos de embarque utilizando Pandas, Matplotlib y Seaborn.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.heading(
                            "Prueba de hipotesis: El dataset es lo suficientemente grande para crear un modelo predictivo con precision del 70%?",
                            size="6",
                            class_name="text-purple-200 mb-4",
                        ),

                        rx.text(
                            "A la hora de entrenar nuestro modelo, vamos a plantear una prueba de hipótesis [36][37] que nos permitirá determinar si la cantidad de datos es suficiente para obtener una precisión esperada del 70%. Para esto establecemos:",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.text(
                            "Hipótesis nula (H₀): La cantidad de datos no es suficiente para alcanzar un 70% de precisión.",
                            class_name="text-gray-200 font-bold mb-2",
                        ),
                        rx.text(
                            "Hipótesis alternativa (H₁): La cantidad de datos es suficiente para alcanzar un 70% de precisión.",
                            class_name="text-gray-200 font-bold mb-4",
                        ),
                        rx.text(
                            "Nivel de significancia (α): 0.05",
                            class_name="text-gray-200 font-bold mb-2",
                        ),
                        rx.text(
                            "Tamaño de la muestra (n): 351",
                            class_name="text-gray-200 font-bold mb-4",
                        ),
                        rx.image(
                            src='/hypothesis.png',
                            class_name="p-4 rounded-2xl bg-black shadow-lg mb-4",
                        ),
                        rx.text(
                            "Referencias: [18][25][36] Prueba de hipótesis utilizando SciPy y métodos estadísticos.",
                            class_name="text-gray-400 text-sm mb-4 text-center italic",
                        ),
                        rx.text(
                            "Teóricamente, el tamaño de la muestra no es lo suficientemente grande para obtener esa precisión esperada en terminos teoricos; "
                            "sin embargo, empíricamente y computacionalmente, obtenemos una precisión del 76%.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.heading(
                            "Dataset limpio",
                            size="7",
                            class_name="text-purple-200 mb-4",
                        ),
            
                        rx.text(
                            "Después de todo este largo proceso, obtuvimos nuestro dataset limpiando variables, justificando decisiones y obteniendo resultados. De un total de aproximadamente 1309 filas y 12 columnas, quedamos con 292 filas y 10 columnas. Realmente, es mucha la cantidad de datos e información que se perdió eliminando los valores vacíos, incoherentes y NaN, demostrando que este problema del Titanic, al haber ocurrido hace más de 100 años, perdió mucha información y es un milagro que en esos tiempos se pudiera haber obtenido al menos algunos datos de las personas.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.text(
                            "De las variables obtenidas, algunas serán descartadas para la predicción, ya sea por su uso para otros propósitos o porque no sirven para alimentar el modelo. Específicamente, descartaremos Name, Cabin, boat y survived (esta última tiene un uso para la clasificación, mas no para la predicción).",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("pclass", class_name="text-white"),
                                    rx.table.column_header_cell("survived", class_name="text-white"),
                                    rx.table.column_header_cell("name", class_name="text-white"), 
                                    rx.table.column_header_cell("sex", class_name="text-white"),
                                    rx.table.column_header_cell("age", class_name="text-white"),
                                    rx.table.column_header_cell("ticket", class_name="text-white"),
                                    rx.table.column_header_cell("fare", class_name="text-white"),
                                    rx.table.column_header_cell("cabin", class_name="text-white"),
                                    rx.table.column_header_cell("embarked", class_name="text-white"),
                                    rx.table.column_header_cell("boat", class_name="text-white")
                                )
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Allen, Miss. Elisabeth Walton", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("29.0", class_name="text-white"),
                                    rx.table.cell("24160", class_name="text-white"),
                                    rx.table.cell("211.3375", class_name="text-white"),
                                    rx.table.cell("B5", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("2", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Allison, Master. Hudson Trevor", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("0.92", class_name="text-white"),
                                    rx.table.cell("113781", class_name="text-white"),
                                    rx.table.cell("151.55", class_name="text-white"),
                                    rx.table.cell("C22 C26", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("11", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Allison, Miss. Helen Loraine", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("2.0", class_name="text-white"),
                                    rx.table.cell("113781", class_name="text-white"),
                                    rx.table.cell("151.55", class_name="text-white"),
                                    rx.table.cell("C22 C26", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("1000", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Allison, Mr. Hudson Joshua Creighton", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("30.0", class_name="text-white"),
                                    rx.table.cell("113781", class_name="text-white"),
                                    rx.table.cell("151.55", class_name="text-white"),
                                    rx.table.cell("C22 C26", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("1001", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Allison, Mrs. Hudson J C (Bessie Waldo Daniels)", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("25.0", class_name="text-white"),
                                    rx.table.cell("113781", class_name="text-white"),
                                    rx.table.cell("151.55", class_name="text-white"),
                                    rx.table.cell("C22 C26", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("1002", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Anderson, Mr. Harry", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("48.0", class_name="text-white"),
                                    rx.table.cell("19952", class_name="text-white"),
                                    rx.table.cell("26.55", class_name="text-white"),
                                    rx.table.cell("E12", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("3", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Andrews, Miss. Kornelia Theodosia", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("63.0", class_name="text-white"),
                                    rx.table.cell("13502", class_name="text-white"),
                                    rx.table.cell("77.9583", class_name="text-white"),
                                    rx.table.cell("D7", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("10", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Andrews, Mr. Thomas Jr", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("39.0", class_name="text-white"),
                                    rx.table.cell("112050", class_name="text-white"),
                                    rx.table.cell("0.0", class_name="text-white"),
                                    rx.table.cell("A36", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("1003", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("Appleton, Mrs. Edward Dale (Charlotte Lamson)", class_name="text-white"),
                                    rx.table.cell("female", class_name="text-white"),
                                    rx.table.cell("53.0", class_name="text-white"),
                                    rx.table.cell("11769", class_name="text-white"),
                                    rx.table.cell("51.4792", class_name="text-white"),
                                    rx.table.cell("C101", class_name="text-white"),
                                    rx.table.cell("S", class_name="text-white"),
                                    rx.table.cell("D", class_name="text-white")
                                ),
                                rx.table.row(
                                    rx.table.cell("1", class_name="text-white"),
                                    rx.table.cell("0", class_name="text-white"),
                                    rx.table.cell("Astor, Col. John Jacob", class_name="text-white"),
                                    rx.table.cell("male", class_name="text-white"),
                                    rx.table.cell("47.0", class_name="text-white"),
                                    rx.table.cell("PC 17757", class_name="text-white"),
                                    rx.table.cell("227.525", class_name="text-white"),
                                    rx.table.cell("C62 C64", class_name="text-white"),
                                    rx.table.cell("C", class_name="text-white"),
                                    rx.table.cell("1005", class_name="text-white")
                                )
                            ),
                            variant="surface",
                            class_name="bg-black mb-8 w-full",
                        ),
                        rx.heading(
                            "Nuestro modelo",
                            size="6",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.text(
                            "Para nuestro modelo, utilizamos una regresión logística [25][26], también conocida como función sigmoid. Esta técnica nos permite crear una clasificación de tipo binaria para obtener un resultado basado en una o más variables independientes. Las variables pasan por esta función y retornan un valor entre 0 y 1, donde los valores cercanos a 1 indican alta probabilidad de supervivencia, mientras que los valores cercanos a 0 indican baja probabilidad de supervivencia.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.text(
                            "En nuestro análisis, interpretamos los valores mayores a 0.6 como una supervivencia aceptable, siendo 1 una supervivencia casi perfecta. Por otro lado, los valores menores a 0.6 nos indican una probabilidad de supervivencia muy baja, casi nula. Esta función sigmoid nos permite transformar múltiples variables predictoras en una probabilidad clara y fácil de interpretar.",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.markdown(
                            """
### Función Logística (Sigmoid)

$$P(y=1|x) = \\frac{1}{1 + e^{-(\\beta_0 + \\beta_1 x_1 + \\beta_2 x_2 + ... + \\beta_n x_n)}}$$

Donde:
- $P(y=1|x)$ representa la probabilidad de supervivencia
- $\\beta_0$ es el término de sesgo o intercepto
- $\\beta_1, \\beta_2, ..., \\beta_n$ son los coeficientes del modelo
- $x_1, x_2, ..., x_n$ son las variables independientes (edad, género, tarifa, etc.)
- $e$ es la base del logaritmo natural (aproximadamente 2.71828)

Esta función transforma cualquier valor de entrada en un rango entre 0 y 1, ideal para representar probabilidades.
            """,
                            class_name="text-gray-200 bg-purple-900/20 p-4 rounded-xl border border-purple-500/30 mb-4 overflow-x-auto",
                        ),
                        rx.heading(
                            "E)Conclusiones",
                            size="7",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.vstack(
                            rx.text(
                                "El problema del Titanic es una excelente introducción al mundo del machine learning, la ciencia de datos y la estadística [29][30]. En este ejercicio, aplicamos todas estas técnicas para predecir un suceso histórico real, dividiéndolo en tres etapas fundamentales:",
                                class_name="text-gray-200 mb-4",
                            ),
                            rx.unordered_list(
                                rx.list_item("Limpieza de datos", class_name="text-gray-200"),
                                rx.list_item("Optimización y validación estadística", class_name="text-gray-200"),
                                rx.list_item("Creación del modelo predictivo", class_name="text-gray-200"),
                                spacing="2",
                                class_name="mb-4",
                            ),
                            rx.text(
                                "Los resultados obtenidos nos revelan conclusiones importantes:",
                                class_name="text-gray-200 mb-2",
                            ),
                            rx.box(
                                rx.unordered_list(
                                    rx.list_item("Las mujeres y niños tuvieron mayor probabilidad de supervivencia [46][49]", class_name="text-gray-200"),
                                    rx.list_item("El precio del pasaje influyó directamente en las posibilidades de salvarse", class_name="text-gray-200"),
                                    rx.list_item("La edad fue un factor determinante (siendo los muy jóvenes y ancianos más vulnerables)", class_name="text-gray-200"),
                                    rx.list_item("El puerto de embarque también jugó un papel significativo", class_name="text-gray-200"),
                                    spacing="2",
                                ),
                                class_name="p-4 bg-purple-900/20 rounded-xl border border-purple-500/30 mb-4",
                            ),
                            rx.text(
                                "Sin embargo, es importante notar que, debido a la antigüedad de los datos, enfrentamos desafíos con información faltante o errónea, lo que podría afectar la precisión de nuestras predicciones.",
                                class_name="text-gray-200 mb-4",
                            ),
                            rx.text(
                                "A pesar de identificar patrones claros, ninguna variable garantizaba una supervivencia del 100%, recordándonos la naturaleza trágica e impredecible de este acontecimiento histórico.",
                                class_name="text-gray-200 mb-4 font-bold",
                            ),
                            align="start",
                            spacing="2",
                        ),

                        rx.heading(
                            "Titanic Survivors SandBox",
                            size="8",
                            class_name="text-purple-200 mb-4",
                        ),
                        rx.text(
                            "Es hora de probar nuestro modelo. Ingresa a esta página para explorar la caja de arena del proyecto, donde podrás hacer una predicción de supervivencia llenando la siguiente información:",
                            class_name="text-gray-200 mb-4",
                        ),
                        rx.vstack(
                            rx.unordered_list(
                                rx.list_item("Age: Edad de la persona", class_name="text-gray-200 font-bold"),
                                rx.list_item("Gender: El género de la persona", class_name="text-gray-200 font-bold"), 
                                rx.list_item("Fare: El costo del pasaje", class_name="text-gray-200 font-bold"),
                                rx.list_item("Embarked: El puerto de embarque", class_name="text-gray-200 font-bold"),
                                spacing="2",
                            ),
                            class_name="mb-4",
                            align="start",
                        ),
                        rx.text(
                            "¿Podrías haber sobrevivido al Titanic? ¡Pruébalo ahora!",
                            class_name="text-purple-200 font-bold mb-4",
                        ),
                        rx.box(
                            rx.text(
                                "NOTA: Al entrar por primera vez, debes esperar un tiempo mientras carga la página. "
                                "Luego de eso, recarga la página y una vez que aparezca arriba que el estado del modelo "
                                "está en verde, podrás hacer las pruebas. Si no usas la página en 15 minutos, se volverá "
                                "a apagar y deberás volver a esperar.",
                                class_name="text-gray-200",
                            ),
                            rx.link(
                                "Ver implementación",
                                href="https://titanicjsw.onrender.com/", 
                                class_name="text-blue-300 hover:text-blue-200 transition-colors",
                            ),
                            class_name="p-4 bg-purple-900/30 rounded-xl border border-purple-500/30 mb-8",
                        ),

                        class_name="w-full p-6 bg-gradient-to-br from-purple-900/40 to-black/40 rounded-2xl shadow-lg border border-purple-500/20 mb-6",
                    ),
                    class_name="w-full",
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
app.add_page(part3)