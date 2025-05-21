import os
import sys
from PIL import Image
import shutil

def optimize_images(source_folder='media', output_folder='media_optimized', quality=80, max_size=(800, 800)):
    """
    Optimiza imágenes reduciendo su calidad y tamaño
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, source_folder)
            output_path = os.path.join(output_folder, relative_path)
            
            # Crear directorios de salida si no existen
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Optimizar imágenes
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                try:
                    with Image.open(file_path) as img:
                        # Redimensionar si es necesario
                        if img.width > max_size[0] or img.height > max_size[1]:
                            img.thumbnail(max_size, Image.Resampling.LANCZOS)
                        
                        # Guardar con calidad reducida
                        img.save(output_path, optimize=True, quality=quality)
                        print(f"Optimizada: {file_path} -> {output_path}")
                except Exception as e:
                    print(f"Error al optimizar {file_path}: {e}")
                    # Copiar el archivo original en caso de error
                    shutil.copy2(file_path, output_path)
            
            # Copiar otros archivos que no son imágenes
            elif not file.lower().endswith(('.mp4', '.mov', '.avi')):  # Excluir archivos de video grandes
                shutil.copy2(file_path, output_path)
                print(f"Copiado: {file_path} -> {output_path}")

if __name__ == "__main__":
    # Si se pasa un argumento, usarlo como carpeta de origen
    source = sys.argv[1] if len(sys.argv) > 1 else 'media'
    optimize_images(source_folder=source)
    print(f"\nOptimización completada. Los archivos optimizados están en 'media_optimized'")
    print("Para usar los archivos optimizados, reemplaza la carpeta 'media' por 'media_optimized'") 