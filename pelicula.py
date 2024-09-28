# En este archivo va la clase pelicula

class Pelicula:
    def __init__(self, nombre, clasificacion):
        self.__nombre = nombre # Nombre es un atributo privado
        self.clasificacion = clasificacion # Clasificación de la película
        
    # Metodo getter para obtener el nombre de la pelicula
    def get_nombre(self):
        return self.__nombre