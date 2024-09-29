
import os
import stat

class DirectorioCatalogo:
    # Permite validar el directorio donde se guardaran los catálogos de las películas
    @staticmethod
    def validar_directorio_catalogo(ruta_directorio):
        os.makedirs(ruta_directorio, mode=0o775, exist_ok=True)
        DirectorioCatalogo.quitar_atributo_solo_lectura(ruta_directorio)
    
    # Quitar el atributo de solo lectura en todos los archivos del directorio catálogo
    @staticmethod
    def quitar_atributo_solo_lectura(carpeta):  
        # Recorrer todos los archivos en la carpeta
        for root, dirs, files in os.walk(carpeta):
            for archivo in files:
                ruta_archivo = os.path.join(root, archivo)

                # Eliminar el atributo de solo lectura en Windows
                if not os.access(ruta_archivo, os.W_OK):
                    os.chmod(ruta_archivo, stat.S_IWRITE) 