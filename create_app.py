import reflex as rx

# Asegurarse de que la configuración de Reflex se carga primero
import rxconfig

# Importar la aplicación principal
from FeelTheDistribution.FeelTheDistribution import app

# Compilar la app para la exportación estática
app._compile()

# Para uso con reflex export
asgi_app = app.build() 