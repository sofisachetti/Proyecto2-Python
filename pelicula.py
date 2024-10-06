# En este archivo va la clase Pelicula y sus metododos

class Pelicula:
    def __init__(self, nombre, clasificacion):
        self.__nombre = nombre # Nombre es un atributo privado
        self.clasificacion = clasificacion # Clasificación de la película
        
    # Metodo getter para obtener el nombre de la pelicula
    def get_nombre(self):
        return self.__nombre
    
    #Permite buscar si existe una película en el cataálogo
    @staticmethod
    def buscar_pelicula(archivo, pelicula):
        with open(archivo, 'r', encoding="utf-8") as f:
            for linea in f:
                if pelicula in linea:
                    return True
        return False