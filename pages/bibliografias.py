import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""
    ...

def bibliografias() -> rx.Component:
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
                rx.vstack(
                    rx.heading(
                        "Referencias Bibliográficas (IEEE)",
                        size="7",
                        class_name="text-white mb-4",
                    ),
                    
                    # Librerías y Frameworks con links a documentación
                    rx.heading(
                        "Librerías para Visualización y Análisis",
                        size="5",
                        class_name="text-purple-300 mb-4 mt-6",
                    ),
                    rx.box(
                        rx.text("[1] Reflex Team, \"Reflex: Build web apps in pure Python,\" GitHub, 2023. [Online]. Available: https://github.com/reflex-dev/reflex. Documentation: https://reflex.dev/docs/", class_name="text-white mb-2"),
                        
                        rx.text("[2] Wes McKinney et al., \"pandas: Python Data Analysis Library,\" 2023. [Online]. Available: https://pandas.pydata.org/. Documentation: https://pandas.pydata.org/docs/", class_name="text-white mb-2"),
                        
                        rx.text("[3] J. D. Hunter et al., \"Matplotlib: A 2D Graphics Environment,\" Computing in Science & Engineering, 2007. Documentation: https://matplotlib.org/stable/api/", class_name="text-white mb-2"),
                        
                        rx.text("[4] F. Pedregosa et al., \"Scikit-learn: Machine Learning in Python,\" Journal of Machine Learning Research, 2011. Documentation: https://scikit-learn.org/stable/user_guide.html", class_name="text-white mb-2"),
                        
                        rx.text("[5] S. van der Walt et al., \"The NumPy Array: A Structure for Efficient Numerical Computation,\" Computing in Science & Engineering, 2011. Documentation: https://numpy.org/doc/stable/reference/", class_name="text-white mb-2"),
                        
                        rx.text("[6] Seaborn Development Team, \"Seaborn: Statistical Data Visualization,\" 2023. [Online]. Available: https://seaborn.pydata.org/. Documentation: https://seaborn.pydata.org/api.html", class_name="text-white mb-2"),
                        
                        rx.text("[7] SciPy Developers, \"SciPy: Open Source Scientific Tools for Python,\" 2023. [Online]. Available: https://scipy.org/. Documentation: https://docs.scipy.org/doc/scipy/reference/", class_name="text-white mb-2"),
                        
                        rx.text("[8] Statsmodels Developers, \"Statsmodels: Statistical Models, Hypothesis Tests, and Data Exploration,\" 2023. [Online]. Available: https://www.statsmodels.org/. Documentation: https://www.statsmodels.org/stable/api.html", class_name="text-white mb-2"),
                        
                        class_name="mb-6",
                    ),
                    
                    # Documentación específica para gráficos
                    rx.heading(
                        "Documentación para Tipos de Gráficos",
                        size="5",
                        class_name="text-purple-300 mb-4 mt-6",
                    ),
                    rx.box(
                        rx.text("[9] Matplotlib Developers, \"Histograms,\" Matplotlib Documentation. [Online]. Available: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html", class_name="text-white mb-2"),
                        
                        rx.text("[10] Matplotlib Developers, \"Scatter Plots,\" Matplotlib Documentation. [Online]. Available: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html", class_name="text-white mb-2"),
                        
                        rx.text("[12] Matplotlib Developers, \"Box Plots,\" Matplotlib Documentation. [Online]. Available: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html", class_name="text-white mb-2"),
                        
                        rx.text("[13] Seaborn Developers, \"Residual Plots,\" Seaborn Documentation. [Online]. Available: https://seaborn.pydata.org/generated/seaborn.residplot.html", class_name="text-white mb-2"),
                        
                        rx.text("[15] Matplotlib Developers, \"QQ Plots,\" Matplotlib Documentation. [Online]. Available: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.qqplot.html", class_name="text-white mb-2"),
                        
                        rx.text("[16] Seaborn Developers, \"Pair Plots,\" Seaborn Documentation. [Online]. Available: https://seaborn.pydata.org/generated/seaborn.pairplot.html", class_name="text-white mb-2"),
                        
                        rx.text("[17] Matplotlib Developers, \"Stem Plots,\" Matplotlib Documentation. [Online]. Available: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html", class_name="text-white mb-2"),
                        
                        class_name="mb-6",
                    ),
                    
                    # Documentación específica para análisis estadístico
                    rx.heading(
                        "Métodos Estadísticos y Análisis de Datos",
                        size="5",
                        class_name="text-purple-300 mb-4 mt-6",
                    ),
                    rx.box(
                        rx.text("[18] SciPy Developers, \"Statistical Functions (scipy.stats),\" SciPy Documentation. [Online]. Available: https://docs.scipy.org/doc/scipy/reference/stats.html", class_name="text-white mb-2"),
                        
                        rx.text("[19] Statsmodels Developers, \"Linear Regression,\" Statsmodels Documentation. [Online]. Available: https://www.statsmodels.org/stable/regression.html", class_name="text-white mb-2"),
                        
                        rx.text("[21] Scikit-learn Developers, \"Linear Models,\" Scikit-learn Documentation. [Online]. Available: https://scikit-learn.org/stable/modules/linear_model.html", class_name="text-white mb-2"),
                        
                        rx.text("[22] Scikit-learn Developers, \"Cross Validation,\" Scikit-learn Documentation. [Online]. Available: https://scikit-learn.org/stable/modules/cross_validation.html", class_name="text-white mb-2"),
                        
                        rx.text("[23] Scikit-learn Developers, \"Model Evaluation,\" Scikit-learn Documentation. [Online]. Available: https://scikit-learn.org/stable/modules/model_evaluation.html", class_name="text-white mb-2"),
                        
                        rx.text("[24] Pandas Developers, \"Data Cleaning,\" Pandas Documentation. [Online]. Available: https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html", class_name="text-white mb-2"),
                        
                        rx.text("[25] SciPy Developers, \"Hypothesis Tests,\" SciPy Documentation. [Online]. Available: https://docs.scipy.org/doc/scipy/reference/stats.html#statistical-tests", class_name="text-white mb-2"),
                        
                        class_name="mb-6",
                    ),
                    
                    # Referencias para Libros de Estadística
                    rx.heading(
                        "Libros y Referencias de Estadística",
                        size="5",
                        class_name="text-purple-300 mb-4 mt-6",
                    ),
                    rx.box(
                                                
                        rx.text("[32] G. Casella and R. L. Berger, \"Statistical Inference,\" Cengage Learning, 2001.", class_name="text-white mb-2"),
                        
                        rx.text("[33] J. Rice, \"Mathematical Statistics and Data Analysis,\" Cengage Learning, 2006.", class_name="text-white mb-2"),
                        
                        rx.text("[34] R. V. Hogg, J. W. McKean, and A. T. Craig, \"Introduction to Mathematical Statistics,\" Pearson, 2012.", class_name="text-white mb-2"),
                        
                        rx.text("[36] E. L. Lehmann and J. P. Romano, \"Testing Statistical Hypotheses,\" Springer, 2005.", class_name="text-white mb-2"),
                        
                        rx.text("[37] S. S. Wilks, \"Mathematical Statistics,\" John Wiley & Sons, 1962.", class_name="text-white mb-2"),
                        
                        rx.text("[38] D. A. Freedman, \"Statistical Models: Theory and Practice,\" Cambridge University Press, 2009.", class_name="text-white mb-2"),
                        
                        rx.text("[40] K. V. Mardia, J. T. Kent, and J. M. Bibby, \"Multivariate Analysis,\" Academic Press, 1979.", class_name="text-white mb-2"),
                        
                        class_name="mb-6",
                    ),
                    
                    # Recursos del Titanic
                    rx.heading(
                        "Recursos del Titanic y Machine Learning",
                        size="5",
                        class_name="text-purple-300 mb-4 mt-6",
                    ),
                    rx.box(
                        rx.text("[42] Kaggle, \"Titanic - Machine Learning from Disaster,\" 2012. [Online]. Available: https://www.kaggle.com/c/titanic", class_name="text-white mb-2"),
                        
                        rx.text("[43] D. W. Hosmer and S. Lemeshow, \"Applied Logistic Regression,\" Wiley, 2000.", class_name="text-white mb-2"),
                                                
                        rx.text("[47] S. Raschka and V. Mirjalili, \"Python Machine Learning,\" Packt Publishing, 2019.", class_name="text-white mb-2"),
                        
                        rx.text("[48] The British Wreck Commissioner's Inquiry, \"Report on the Loss of the 'Titanic' (S.S.),\" Her Majesty's Stationery Office, 1912.", class_name="text-white mb-2"),
                        
                        rx.text("[49] Encyclopedia Titanica, \"Titanic Research Articles, Biographies and News,\" 2023. [Online]. Available: https://www.encyclopedia-titanica.org/", class_name="text-white mb-2"),
                        
                        class_name="mb-6",
                    ),
                    
                    # Recursos de Criptografía y Ciberseguridad
                    rx.heading(
                        "Criptografía y Ciberseguridad",
                        size="5",
                        class_name="text-purple-300 mb-4 mt-6",
                    ),
                    rx.box(
                        rx.text("[50] B. Schneier, \"Applied Cryptography: Protocols, Algorithms, and Source Code in C,\" Wiley, 2015.", class_name="text-white mb-2"),
                        
                        rx.text("[51] A. J. Menezes, P. C. van Oorschot, and S. A. Vanstone, \"Handbook of Applied Cryptography,\" CRC Press, 1996. [Online]. Available: http://cacr.uwaterloo.ca/hac/", class_name="text-white mb-2"),
                        
                        rx.text("[52] NIST, \"Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications,\" Special Publication 800-22, 2010. [Online]. Available: https://csrc.nist.gov/publications/detail/sp/800-22/rev-1a/final", class_name="text-white mb-2"),
                        
                        rx.text("[53] D. Kahn, \"The Codebreakers: The Comprehensive History of Secret Communication from Ancient Times to the Internet,\" Scribner, 1996.", class_name="text-white mb-2"),
                        
                        rx.text("[54] T. Dierks and E. Rescorla, \"The Transport Layer Security (TLS) Protocol,\" RFC 5246, 2008. [Online]. Available: https://datatracker.ietf.org/doc/html/rfc5246", class_name="text-white mb-2"),
                        
                        rx.text("[55] J. Katz and Y. Lindell, \"Introduction to Modern Cryptography,\" Chapman and Hall/CRC, 2020.", class_name="text-white mb-2"),
                        
                        rx.text("[56] C. E. Shannon, \"Communication Theory of Secrecy Systems,\" Bell System Technical Journal, vol. 28, no. 4, pp. 656-715, 1949.", class_name="text-white mb-2"),
                        
                        rx.text("[57] W. Stallings, \"Cryptography and Network Security: Principles and Practice,\" Pearson, 2017.", class_name="text-white mb-2"),
                        
                        rx.text("[58] NIST, \"Cryptographic Standards and Guidelines,\" Computer Security Resource Center. [Online]. Available: https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines", class_name="text-white mb-2"),
                        
                        class_name="mb-6",
                    ),
                    
                    width="100%",
                    spacing="4",
                    align="start",
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
app.add_page(bibliografias)