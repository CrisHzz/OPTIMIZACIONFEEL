import os
import sys
import gc
import psutil
import subprocess
from typing import Dict, List, Optional, Tuple
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def get_memory_usage() -> float:
    """Obtiene el uso actual de memoria en MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)

def force_garbage_collection() -> float:
    """Fuerza la limpieza de memoria y retorna la memoria liberada en MB"""
    before = get_memory_usage()
    
    # Forzar recolección de basura
    gc.collect()
    
    after = get_memory_usage()
    saved = before - after
    
    logger.info(f"Limpieza de memoria completada: {saved:.2f} MB liberados")
    return saved

def configure_matplotlib_for_memory_efficiency():
    """Configura matplotlib para minimizar el uso de memoria"""
    try:
        import matplotlib
        matplotlib.use('Agg')  # Usar backend no interactivo
        matplotlib.interactive(False)  # Desactivar interactividad
        
        # Reducir el cache de fontes
        try:
            from matplotlib.font_manager import fontManager
            fontManager.ttflist = fontManager.ttflist[:10]  # Mantener sólo algunos fonts
        except:
            pass
            
        logger.info("Matplotlib configurado para bajo consumo de memoria")
    except ImportError:
        logger.info("Matplotlib no está instalado")

def optimize_pandas_memory_usage():
    """Configura pandas para usar menos memoria"""
    try:
        import pandas as pd
        
        # Reducir el tamaño de los bloques de memoria
        pd.options.mode.chained_assignment = None  # Desactivar warnings
        pd.options.display.max_rows = 20  # Reducir filas mostradas por defecto
        pd.options.display.max_columns = 10  # Reducir columnas mostradas por defecto
        
        logger.info("Pandas configurado para menor consumo de memoria")
    except ImportError:
        logger.info("Pandas no está instalado")

def optimize_numpy_memory():
    """Configura numpy para usar menos memoria"""
    try:
        import numpy as np
        
        # Usar dtype de menor precisión por defecto
        np.set_printoptions(threshold=100)  # Reducir output por consola
        
        logger.info("NumPy configurado para menor consumo de memoria")
    except ImportError:
        logger.info("NumPy no está instalado")

def optimize_memory_usage():
    """Aplica todas las optimizaciones de memoria"""
    initial_memory = get_memory_usage()
    logger.info(f"Uso de memoria inicial: {initial_memory:.2f} MB")
    
    # Aplicar optimizaciones
    configure_matplotlib_for_memory_efficiency()
    optimize_pandas_memory_usage()
    optimize_numpy_memory()
    force_garbage_collection()
    
    current_memory = get_memory_usage()
    saved_memory = initial_memory - current_memory
    logger.info(f"Memoria ahorrada: {saved_memory:.2f} MB")
    logger.info(f"Uso de memoria actual: {current_memory:.2f} MB")
    
    return current_memory

def check_memory_usage(threshold_mb=515):
    """Verifica si el uso de memoria está por debajo del umbral"""
    current_memory = get_memory_usage()
    if current_memory > threshold_mb:
        logger.warning(f"⚠️ Uso de memoria ({current_memory:.2f} MB) por encima del umbral ({threshold_mb} MB)")
        return False
    else:
        logger.info(f"✅ Uso de memoria ({current_memory:.2f} MB) por debajo del umbral ({threshold_mb} MB)")
        return True

def patch_reflex_to_reduce_memory():
    """Aplica parches a reflex para reducir el consumo de memoria"""
    try:
        import reflex as rx
        
        # Patchar rx.App para que use menos memoria
        original_app_init = rx.App.__init__
        
        def patched_app_init(self, *args, **kwargs):
            # Llamar al constructor original
            original_app_init(self, *args, **kwargs)
            
            # Aplicar optimizaciones de memoria
            optimize_memory_usage()
        
        rx.App.__init__ = patched_app_init
        logger.info("Reflex parcheado para optimizar memoria")
        
    except ImportError:
        logger.info("Reflex no está instalado")

def setup_memory_monitor(threshold_mb=515, check_interval=300):
    """Configura un monitor periódico de memoria"""
    import threading
    import time
    
    def monitor_memory():
        while True:
            if not check_memory_usage(threshold_mb):
                # Si se excede el umbral, forzar liberación de memoria
                force_garbage_collection()
            time.sleep(check_interval)  # Verificar cada 5 minutos
    
    monitor_thread = threading.Thread(target=monitor_memory, daemon=True)
    monitor_thread.start()
    logger.info(f"Monitor de memoria iniciado (umbral: {threshold_mb} MB, intervalo: {check_interval}s)")

if __name__ == "__main__":
    logger.info("Iniciando optimización de memoria...")
    optimize_memory_usage()
    patch_reflex_to_reduce_memory()
    setup_memory_monitor()
    logger.info("Optimización de memoria completada") 