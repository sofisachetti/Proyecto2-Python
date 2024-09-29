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
    
    # Funcion que permite al usuario eliminar un catalogo si así lo desea
    def eliminar_catalogo(self):
        catalogoAEliminar = input("Ingrese el nombre del catalogo que desee eliminar: ").lower()
        confirmacion = input(f'¿Está seguro que desea borrar el catálogo {catalogoAEliminar} de forma permanente? (Si/No): ').title()
        if confirmacion == 'Si' and catalogoAEliminar == self.nombreCatalogo:
            if os.path.exists(self.ruta_completa):
                os.remove(self.ruta_completa)
                print(f"El catalogo {catalogoAEliminar} se elimino con exito.")
            else:
                print(f"El catalogo {catalogoAEliminar} no existe. Asegurese de haber escrito bien el nombre.")
        elif confirmacion == 'No':
            print("Ha seleccionado no eliminar el catalogo.")
        else: 
            print("Opcion no valida. Debe responder con Si o No.")
    
    #Permite mostrar todas las opciones disponibles para trabajar en el catálogo de películas
    def mostrar_menu_opciones(self):
        try:
            opcion = int(input(f"--- Menú del Catálogo {self.nombreCatalogo} --- \n"
                        "1) Agregar pelicula\n"
                        "2) Mostrar Catálogo de peliculas \n"
                        "3) Eliminar Catálogo de peliculas \n"
                        "4) Salir \n"
                        "Tu opción: "))
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
                return opcion
            else:
                print("Error: Solo se permite un número del 1 al 4.")
                return CatalogoPelicula.mostrar_menu_opciones()  
        except ValueError:
            print("Error: Solo se permite un número del 1 al 4.")
            return CatalogoPelicula.mostrar_menu_opciones()
    


#Ejemplos para probar las funcionalidades mientras se implementa el metodo    
catalogo = CatalogoPelicula("terror")
print(catalogo.validar_Catalogo())
catalogo.agregar_Pelicula()

print(catalogo.eliminar_catalogo())

