import os
import sys
import reflex as rx
import asyncio

# Asegurarse de que la configuración de Reflex se carga primero
import rxconfig

# Importar la aplicación principal
from FeelTheDistribution.FeelTheDistribution import app

# En Reflex 0.7.12 necesitamos construir la aplicación ASGI de forma diferente
from reflex.compiler import compiler

# Obtener la aplicación ASGI compilada
# En Reflex 0.7.12, necesitamos compilar la app antes de exponerla
app._compile()

# Exponer la aplicación ASGI directamente para que Uvicorn/Gunicorn la use
from reflex.app import app as reflex_app
asgi_app = reflex_app

# Esta función es para uso con Gunicorn
def create_app():
    return asgi_app

# Permitir import directo
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"Aplicación ASGI creada y lista para ser servida en puerto {port}") 