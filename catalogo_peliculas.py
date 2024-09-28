# Aca va la clase CatalogoPelicula y la  logica del menu

import pelicula
import os

class CatalogoPelicula:
    def __init__(self, nombreCatalogo):
        self.nombreCatalogo = nombreCatalogo # Nombre es el nombre del catálogo
        self.ruta_archivo = nombreCatalogo + '.txt' # Ruta del archivo donde se va a guardar el catálogo
        self.ruta_completa = os.path.join(os.getcwd(),"Catalogos", self.ruta_archivo) #Establecer la ruta donde se guardarán los catalogos

    # Permite validar si existe o no un catálogo de película
    def validar_Catalogo(self):        
        if os.path.exists(self.ruta_completa):
            print(f"Bienvenido al Catálogo de {self.nombreCatalogo}")
            return self.nombreCatalogo
        else:
            with open(self.ruta_completa, 'a', encoding="utf-8") as file:  # 'a' modo append para agregar o crear el archivo del catalgo de la pelicula
                file.write("Película - Clasificación")
                print(f"Se creó el catálogo de {self.ruta_archivo} exitosamente.")
                print(f"Bienvenido al Catálogo de {self.nombreCatalogo}")
            return self.nombreCatalogo
    
    # Permite agregar una película al catálogo correspondiente
    def agregar_Pelicula(self):
        nombrePelicula = input("Escribe el nombre de la película: ").title()
        clasificacionPelicula = input(f"Escribe la clasificación de la película ({nombrePelicula}): ").title()
        peli = pelicula.Pelicula(nombrePelicula,clasificacionPelicula)
        with open(self.ruta_completa, "a", encoding="utf-8") as file:
            file.write(f"\n{peli.get_nombre()} - {peli.clasificacion}")
        print(f"La película {peli.get_nombre()} se registro exitosamente.")
    
#Ejemplos para probar las funcionalidades mientras se implementa el metodo    
catalogo = CatalogoPelicula("terror")
print(catalogo.validar_Catalogo())
catalogo.agregar_Pelicula()











