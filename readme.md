# Feel the Distribution

## Ejecución local

Para ejecutar el proyecto localmente:

```bash
reflex run
```

## Despliegue optimizado en Render

Este proyecto está optimizado para consumir menos de 515MB de memoria en Render. Las siguientes optimizaciones se han aplicado:

1. **Optimización de requisitos**: Solo se instalan las dependencias necesarias.
2. **Optimización de procesamiento de imágenes**: Se utiliza `optimize_media.py` para reducir el tamaño de los activos multimedia.
3. **Carga perezosa de datos**: Los datasets se cargan solo cuando son necesarios.
4. **Optimización de memoria para Pandas y NumPy**: Se utilizan dtypes más eficientes y se liberan recursos no utilizados.
5. **Monitorización de memoria en tiempo real**: Se verifica periódicamente el uso de memoria.

### Para desplegar en Render:

1. Crea un nuevo Web Service en Render
2. Configura el entorno Python 3.9
3. Usa el siguiente comando de construcción: `pip install -r requirements.txt`
4. Usa el siguiente comando de inicio: `PYTHON_ENV=production python optimize_media.py && PYTHONMALLOC=malloc MALLOC_TRIM_THRESHOLD_=100000 reflex run --env prod`

Alternativamente, Render detectará el Procfile incluido y lo usará automáticamente.

## Variables de entorno importantes

- `PYTHON_ENV=production`: Activa las optimizaciones de memoria
- `MAX_WORKERS=1`: Limita el número de workers para reducir el consumo de memoria
- `WEB_CONCURRENCY=1`: Limita la concurrencia web para reducir el consumo de memoria

## Solución de problemas

Si experimentas problemas de memoria:

1. Ejecuta el script de optimización de media: `python optimize_media.py`
2. Asegúrate de que `memory_optimization.py` se importa correctamente
3. Ajusta los umbrales de memoria en `memory_optimization.py` si es necesario

```bash
reflex run
