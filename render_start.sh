#!/bin/bash

# Script para iniciar la aplicación en Render con optimizaciones de memoria
echo "Starting FeelTheDistribution with memory optimizations..."

# Establecer la variable de entorno para producción
export PYTHON_ENV=production

# Establecer el puerto para la aplicación
export PORT=${PORT:-8000}
echo "Using PORT: $PORT"

# Optimizar imágenes primero
echo "Optimizing media assets..."
python optimize_media.py

# Establecer límites de memoria para Python
export PYTHONMALLOC=malloc
export MALLOC_TRIM_THRESHOLD_=100000

# Limpiar archivos temporales y cache
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -delete
find . -name ".DS_Store" -delete

# Inicializar el proyecto Reflex
echo "Initializing Reflex..."
python -m reflex init

# Compilar el proyecto
echo "Compiling Reflex project..."
python -m reflex build

# Iniciar la aplicación con uvicorn directamente
echo "Starting application with uvicorn..."
uvicorn create_app:asgi_app --host 0.0.0.0 --port $PORT 