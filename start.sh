#!/bin/bash

# Configuración para producción
export PYTHON_ENV=production

# Optimizar medios
python optimize_media.py

# Configuración de memoria
export PYTHONMALLOC=malloc
export MALLOC_TRIM_THRESHOLD_=100000

# Configuración del puerto
export PORT=${PORT:-8000}

# Limpieza
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -delete

# Iniciar aplicación
reflex run --env prod 