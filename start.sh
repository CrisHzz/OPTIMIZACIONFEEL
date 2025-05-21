#!/bin/bash

# Configuración para producción
export PYTHON_ENV=production

# Reducir el uso de memoria
export MALLOC_ARENA_MAX=2
export PYTHONMALLOC=malloc
export MALLOC_TRIM_THRESHOLD_=100000
export NODE_OPTIONS="--max-old-space-size=400"

# Configuración del puerto (debe ser el que Render asigna)
export PORT=${PORT:-10000}
echo "Configurando puerto: $PORT"

# Optimizar medios
python optimize_media.py

# Limpieza agresiva
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete
python -c "import gc; gc.collect()"

# Inicializar Reflex
python -m reflex init

# Mostrar puertos en uso
echo "Puertos actualmente en uso:"
netstat -tulpn 2>/dev/null || echo "netstat no disponible"

# Iniciar aplicación con uvicorn directamente
echo "Iniciando servidor en 0.0.0.0:$PORT"
uvicorn create_app:asgi_app --host 0.0.0.0 --port $PORT 