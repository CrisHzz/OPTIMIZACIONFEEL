import os
import reflex as rx

# Configuración de la aplicación
config = rx.Config(
    app_name="FeelTheDistribution",
    static_dir="assets",  # Configurar la carpeta de archivos estáticos
    port=int(os.environ.get("PORT", 10000)),
    frontend_port=int(os.environ.get("PORT", 10000)),
    backend_port=int(os.environ.get("PORT", 10000))
)