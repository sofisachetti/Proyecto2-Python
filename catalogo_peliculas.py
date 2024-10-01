# Aca va la clase CatalogoPelicula y la  logica del menu

# Importamos los modulos necesarios
import pelicula
from directorioCatalogo import DirectorioCatalogo
import os


class CatalogoPelicula:
    def __init__(self, nombreCatalogo):
        self.nombreCatalogo = nombreCatalogo # Nombre es el nombre del catálogo
        self.ruta_archivo = nombreCatalogo + '.txt' # Ruta del archivo donde se va a guardar el catálogo
        self.directorio = "Catalogos" # Nombre del directorio
        self.ruta_directorio = os.path.join(os.getcwd(),self.directorio) # Ruta completa del directorio
        self.ruta_archivo_completo = os.path.join(self.ruta_directorio, self.ruta_archivo)  # Ruta completa del archivo de catálogo
        
    # Permite validar si existe o no un catálogo de película
    def validar_catalogo(self):  
        DirectorioCatalogo.validar_directorio_catalogo(self.ruta_directorio)
        if os.path.exists(self.ruta_archivo_completo):
            print(f"Bienvenido al Catálogo de Películas de {self.nombreCatalogo}")
            return self.nombreCatalogo
        else:
            with open(self.ruta_archivo_completo, 'a', encoding="utf-8") as file:  # 'a' modo append para agregar o crear el archivo del catalgo de la pelicula
                file.write("Película - Clasificación")
                print(f"Se creó el catálogo de {self.ruta_archivo} exitosamente.")
                print(f"Bienvenido al Catálogo de Películas de {self.nombreCatalogo}")
            return self.nombreCatalogo                
        
    #Permite ingresar la información del nombre del catálogo de películas
    def datos_catalogo():
        print("--- CREACIÓN DEL CATÁLOGO ---")
        nombreCat = input("Escribe el nombre del catálogo de películas: ").title()
        catalogoPeli = CatalogoPelicula(nombreCat)  
        catalogoPeli.creacion_catalogo()
        
    # Permite agregar una película al catálogo correspondiente
    def agregar_pelicula(self):
        print("--- AGREGAR PELÍCULA ---")
        nombrePelicula = input("Escribe el nombre de la película: ").title()
        clasificacionPelicula = input(f"Escribe la clasificación de la película ({nombrePelicula}): ").title()
        peli = pelicula.Pelicula(nombrePelicula,clasificacionPelicula)
        resultado = peli.buscar_pelicula(self.ruta_archivo_completo, nombrePelicula)
        if resultado == False:
            with open(self.ruta_archivo_completo, "a", encoding="utf-8") as file:
                file.write(f"\n{peli.get_nombre()} - {peli.clasificacion}")
            print(f"La película {peli.get_nombre()} se registro exitosamente.")
        else:
            print(f"La película {peli.get_nombre()} ya está registrada en el catálogo {self.nombreCatalogo}.")

    # Funcion para listar todas las peliculas dentro de un catalogo buscado
    def listar_peliculas(self):
        print("---MOSTRAR PELÍCULAS---")
        catalogoListar = input("Escribe el nombre del catálogo: ").title()
        if catalogoListar == self.nombreCatalogo:
            with open(self.ruta_archivo_completo, 'r', encoding="utf-8") as file:
                print(f"Películas del catálogo {catalogoListar}: \n")
                contenidoCatalogo = file.read()
                print(contenidoCatalogo)
        else:
            print("Lo sentimos. El catálogo ingresado no existe o esta escrito de forma incorrecta.")
    
    # Funcion que permite al usuario eliminar un catalogo si así lo desea
    def eliminar_catalogo(self):
        print("--- ELIMINAR CATÁLOGO ---")
        catalogoAEliminar = input("Ingrese el nombre del catálogo que desee eliminar: ").title()
        confirmacion = ""
        while confirmacion not in ["Si", "No"]:
            confirmacion = input(f'¿Está seguro que desea borrar el catálogo {catalogoAEliminar} de forma permanente? (Si/No): ').title()
            if confirmacion not in ["Si", "No"]:
                print("Error: Solo se permite una opción de Si o No.")
        
        if confirmacion == 'Si' and catalogoAEliminar == self.nombreCatalogo:
            if os.path.exists(self.ruta_archivo_completo):
                os.remove(self.ruta_archivo_completo)
                print(f"El catálogo {catalogoAEliminar} se elimino con exito.")
                print("Crea un nuevo catálogo de películas:")
                return CatalogoPelicula.datos_catalogo()
            else:
                print(f"El catálogo {catalogoAEliminar} no existe. Asegurese de haber escrito bien el nombre.")
        elif confirmacion == 'No':
            print("Ha seleccionado no eliminar el catálogo.")

    #Permite la opción de cambiar a otro catálogo de películas
    def cambiar_catalogo(self):
        print("--- CAMBIAR CATÁLOGO ---")
        confirmacion = ""
        while confirmacion not in ["Si", "No"]:
            confirmacion = input(f"¿Quieres cambiar a otro catálogo de películas? (Si/No): ").title()
            if confirmacion not in ["Si", "No"]:
                print("Error: Solo se permite una opción de Si o No.")
            
        if confirmacion == "Si":
            print("Haz elegido cambiar de catálogo de películas.")
            return CatalogoPelicula.datos_catalogo()
        else:
            print(f"Haz regresado al menú del catálogo de películas de {self.nombreCatalogo}.")
        
    #Permite mostrar todas las opciones disponibles para trabajar en el catálogo de películas
    def mostrar_menu_opciones(self):
        try:
            opcion = int(input(f"--- Menú del Catálogo {self.nombreCatalogo} --- \n"
                        "1) Agregar película\n"
                        "2) Mostrar Catálogo de películas \n"
                        "3) Eliminar Catálogo de películas \n"
                        "4) Cambiar otro Catálogo de películas \n"
                        "5) Salir \n"
                        "Tu opción: "))
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
                return opcion
            else:
                print("Error: Solo se permite un número del 1 al 5.")
                return CatalogoPelicula.mostrar_menu_opciones()  
        except ValueError:
            print("Error: Solo se permite un número del 1 al 5.")
            return CatalogoPelicula.mostrar_menu_opciones()
    
    # Permite mostrar las opciones del menú para el catálogo de película
    def creacion_catalogo(self):
        CatalogoPelicula.validar_catalogo(self)
        while True:
            opcion = CatalogoPelicula.mostrar_menu_opciones(self)
            
            if opcion == 1:
                CatalogoPelicula.agregar_pelicula(self)
            elif opcion == 2:
                CatalogoPelicula.listar_peliculas(self)
            elif opcion == 3:
                CatalogoPelicula.eliminar_catalogo(self)
                break
            elif opcion == 4:
                CatalogoPelicula.cambiar_catalogo(self)
                break
            else:
                break


# Permite al usuario ingresar el catalógo de las peliculas
CatalogoPelicula.datos_catalogo()

