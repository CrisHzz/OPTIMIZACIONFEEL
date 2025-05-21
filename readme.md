# Feel The Distribution - Static Site

Este proyecto es una aplicación web estática construida con Reflex para mostrar distribuciones estadísticas de manera interactiva.

## Despliegue en Render

Para desplegar este sitio estático en Render:

1. Crea una cuenta en [Render](https://render.com) si aún no tienes una.
2. Conecta tu repositorio de GitHub/GitLab/Bitbucket.
3. Selecciona "New Web Service" o "Blueprint" en el dashboard de Render.
4. Selecciona este repositorio.
5. Render detectará automáticamente el archivo `render.yaml` y configurará el despliegue como un sitio estático.
6. Confirma la configuración y haz clic en "Create".

El sitio se desplegará automáticamente y Render proporcionará una URL para acceder a tu sitio.

## Estructura del Proyecto

- `FeelTheDistribution/`: Contiene la aplicación principal de Reflex
- `pages/`: Componentes de página para cada sección
- `styles/`: Estilos CSS personalizados
- `media/`: Archivos multimedia originales
- `media_optimized/`: Versiones optimizadas de los archivos multimedia (generadas durante el despliegue)
- `assets/`: Otros recursos estáticos

## Desarrollo Local

Para ejecutar este proyecto localmente:

1. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

2. Inicializa Reflex:
   ```
   python -m reflex init
   ```

3. Ejecuta en modo desarrollo:
   ```
   python -m reflex run
   ```

4. Para generar una versión estática:
   ```
   python -m reflex export --frontend-only
   ```
   
   Los archivos estáticos se generarán en la carpeta `.web/_static/`.

## Optimización de Imágenes

Durante el despliegue, todas las imágenes se optimizan automáticamente usando el script `optimize_media.py`. Si deseas optimizar las imágenes localmente, ejecuta:

```
python optimize_media.py
```

```bash
reflex run
