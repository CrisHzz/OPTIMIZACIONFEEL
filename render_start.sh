#!/bin/bash

# Script para iniciar la aplicación en Render con optimizaciones de memoria
echo "Starting FeelTheDistribution with memory optimizations..."

# Establecer la variable de entorno para producción
export PYTHON_ENV=production

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

# Iniciar la aplicación con límite de memoria para uvicorn workers
echo "Starting application with optimized settings..."
reflex run --env prod 