# En este archivo va la clase pelicula

class Pelicula:
    def __init__(self, nombre, genero):
        self.__nombre = nombre # Nombre es un atributo privado
        self.genero = genero
        
    # Metodo getter para obtener el nombre de la pelicula
    def get_nombre(self):
        return self.__nombre