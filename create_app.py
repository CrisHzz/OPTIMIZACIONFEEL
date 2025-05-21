import os
import sys
import reflex as rx

# Asegurarse de que la configuración de Reflex se carga primero
import rxconfig

# Importar la aplicación principal
from FeelTheDistribution.FeelTheDistribution import app

# Exponer la aplicación ASGI directamente para que Uvicorn/Gunicorn la use
asgi_app = app.prepare_app()

# Esta función es para uso con Gunicorn
def create_app():
    return asgi_app

# Permitir import directo
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"Aplicación ASGI creada y lista para ser servida en puerto {port}") 