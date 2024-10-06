# Aca va la clase CatalogoPelicula y la logica del menu de opciones

# Importamos los modulos necesarios
import pelicula
from directorioCatalogo import DirectorioCatalogo
import os
from colorama import Fore, Style, init
import unicodedata

class CatalogoPelicula:
    def __init__(self, nombreCatalogo):
        self.nombreCatalogo = nombreCatalogo # Nombre es el nombre del catálogo
        self.ruta_archivo = nombreCatalogo + '.txt' # Ruta del archivo donde se va a guardar el catálogo
        self.directorio = "Catalogos" # Nombre del directorio
        self.ruta_directorio = os.path.join(os.getcwd(),self.directorio) # Ruta completa del directorio
        self.ruta_archivo_completo = os.path.join(self.ruta_directorio, self.ruta_archivo)  # Ruta completa del archivo de catálogo
    
    #Permite eliminar los acentos en el nombre del catálogo   
    def eliminar_acentos(nombreCatalogo):
        return ''.join(c for c in unicodedata.normalize('NFD', nombreCatalogo) if unicodedata.category(c) != 'Mn').title()
        
    # Permite validar si existe o no un catálogo de película
    def validar_catalogo(self):  # Si existe, nos lleva al catalogo
        DirectorioCatalogo.validar_directorio_catalogo(self.ruta_directorio)
        if os.path.exists(self.ruta_archivo_completo):
            print(f"Bienvenido al Catálogo de Películas de {self.nombreCatalogo}")
            return self.nombreCatalogo
        else: #Si no existe, lo crea
            with open(self.ruta_archivo_completo, 'a', encoding="utf-8") as file: 
                file.write("Película - Clasificación")
                print(f"✔️  Se creó el catálogo de {self.ruta_archivo} exitosamente.")
                print(f"Bienvenido al Catálogo de Películas de {self.nombreCatalogo}")
            return self.nombreCatalogo                
        
    #Permite ingresar la información del nombre del catálogo de películas
    def datos_catalogo():
        init()
        print(Fore.YELLOW)
        print("--- CREACIÓN DEL CATÁLOGO ---")
        print("Comencemos con el catálogo que deseas crear o modificar.\n")
        nombreCat = CatalogoPelicula.eliminar_acentos(input("Escribe el nombre del catálogo de películas: ").title() )       
        catalogoPeli = CatalogoPelicula(nombreCat)  
        catalogoPeli.creacion_catalogo()
        print(Style.RESET_ALL, end="")
        
    # Permite agregar una película al catálogo correspondiente
    def agregar_pelicula(self):
        init()
        print(Fore.YELLOW)
        print("--- AGREGAR PELÍCULA ---")
        nombrePelicula = input("Escribe el nombre de la película: ").title()
        clasificacionPelicula = input(f"Escribe la clasificación de la película ({nombrePelicula}): ").title()
        peli = pelicula.Pelicula(nombrePelicula,clasificacionPelicula) # Llamamos a la clase Pelicula para la creacion del objeto
        resultado = peli.buscar_pelicula(self.ruta_archivo_completo, nombrePelicula) # Corroboramos si la pelicula ya existe
        if resultado == False: # Si no existe, la crea
            with open(self.ruta_archivo_completo, "a", encoding="utf-8") as file:
                file.write(f"\n{peli.get_nombre()} - {peli.clasificacion}")
            print(f" ✔️  La película {peli.get_nombre()} se registro exitosamente.")
        else: # Si ya existe, avisa con un mensaje
            print(f"⚠️  La película {peli.get_nombre()} ya está registrada en el catálogo {self.nombreCatalogo}.")
        print(Style.RESET_ALL, end="")
        
    # Funcion para listar todas las peliculas dentro de un catalogo buscado
    def listar_peliculas(self):
        init()
        print(Fore.MAGENTA)
        print("---MOSTRAR PELÍCULAS---")
        try: 
            if self.nombreCatalogo:
                with open(self.ruta_archivo_completo, 'r', encoding="utf-8") as file:
                    print(f"Películas del catálogo {self.nombreCatalogo}: \n")
                    contenidoCatalogo = file.read()
                    print(contenidoCatalogo)
        except:
            print("⚠️  Lo sentimos. El catálogo ingresado no existe o esta escrito de forma incorrecta.")
        print(Style.RESET_ALL, end="")
        
    # Funcion que permite al usuario eliminar un catalogo si así lo desea
    def eliminar_catalogo(self):
        init()
        print(Fore.YELLOW)
        print("--- ELIMINAR CATÁLOGO ---")
        confirmacion = ""
        while confirmacion not in ["Si", "No"]:
            confirmacion = input(f'¿Está seguro que desea borrar el catálogo {self.nombreCatalogo} de forma permanente? (Si/No): ').title()
            if confirmacion not in ["Si", "No"]:
                print("❌  Error: Solo se permite una opción de Si o No.")
        
        if confirmacion == 'Si': #and catalogoAEliminar == self.nombreCatalogo:
            if os.path.exists(self.ruta_archivo_completo): # Se corrobora que el catálogo exista y lo elimina.
                os.remove(self.ruta_archivo_completo)
                print(f"🗑️  El catálogo {self.nombreCatalogo} se elimino con exito.")
                print("Crea un nuevo catálogo de películas:")
                CatalogoPelicula.datos_catalogo()
                return True
            else: # Si el catalogo no existe o esta mal escrito, avisa al usuario. 
                print(f"El catálogo {self.nombreCatalogo} no existe. Asegurese de haber escrito bien el nombre.")
        else:
            print("Ha seleccionado no eliminar el catálogo.")
            CatalogoPelicula.datos_catalogo() # Vuelve al menu inicial
            return False
        print(Style.RESET_ALL, end="")
            
    #Permite la opción de cambiar a otro catálogo de películas
    def cambiar_catalogo(self):
        init()
        print(Fore.YELLOW)
        print("--- CAMBIAR CATÁLOGO ---")        
        confirmacion = ""
        while confirmacion not in ["Si", "No"]:
            confirmacion = input(f"¿Quieres cambiar a otro catálogo de películas? (Si/No): ").title()
            if confirmacion not in ["Si", "No"]:
                print("❌  Error: Solo se permite una opción de Si o No.")
        
        if confirmacion == "Si":
            print("🔄  Haz elegido cambiar de catálogo de películas.")
            CatalogoPelicula.datos_catalogo()
            return True
        else:
            print(f"Haz regresado al menú del catálogo de películas de {self.nombreCatalogo}.")
            print(Style.RESET_ALL, end="")
            return False
        
    #Permite mostrar todas las opciones disponibles para trabajar en el catálogo de películas
    def mostrar_menu_opciones(self):
        init()
        print(Fore.BLUE)
        try:
            opcion = int(input(f"--- Menú del Catálogo {self.nombreCatalogo} --- \n"
                        "1) Agregar película\n"
                        "2) Mostrar Catálogo de películas \n"
                        "3) Eliminar Catálogo de películas \n"
                        "4) Cambiar otro Catálogo de películas \n"
                        "5) Salir \n"
                        "Tu opción: "))
            print(Style.RESET_ALL, end="")
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
                return opcion
            else:
                print("❌  Error: Solo se permite un número del 1 al 5.")
                return CatalogoPelicula.mostrar_menu_opciones()  
        except ValueError:
            print("❌  Error: Solo se permite un número del 1 al 5.")
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
                if CatalogoPelicula.eliminar_catalogo(self):
                    break
            elif opcion == 4:
                if CatalogoPelicula.cambiar_catalogo(self):                                
                    break
            else:
                init()
                print(Fore.MAGENTA)
                print("¡Gracias por visitar el Catálogo de Películas! 🎥 ✨ \n")
                print("¡Hasta la próxima y que tengas un día de película! 🍿👋")
                print(Style.RESET_ALL, end="")
                break

# Permite al usuario ingresar el catalógo de las peliculas
init()
print(Fore.MAGENTA)
print("--- ✨ 🎥 ¡Bienvenido al Catálogo de Películas! 🎥 ✨---")
print(Style.RESET_ALL, end="")
CatalogoPelicula.datos_catalogo()
