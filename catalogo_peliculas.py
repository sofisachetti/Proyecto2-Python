# Aca va la clase CatalogoPelicula y la  logica del menu

import pelicula

class CatalogoPelicula:
    def __init__(self, nombreCatalogo):
        self.nombreCatalogo = nombreCatalogo # Nombre es el nombre del catalogo
        self.ruta_archivo = nombreCatalogo + '.txt' # Ruta del archivo donde se va a guardar el catalogo
        











#with open(cls.ruta_archivo, 'a') as file:  # 'a' modo append para agregar o crear el archivo