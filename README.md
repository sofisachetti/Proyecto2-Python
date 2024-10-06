# CATÁLOGO DE PELÍCULAS 🎥
Esta herramienta está desarrollada para aquellos amantes de las películas que deseen llevar un control claro de las peliculas que vieron o que más les gustaron. A través de un sistema de catálogos para clasificar las películas por género, esta aplicación permite al usuario la creación y gestión de sus propios catálogos con las siguientes funcionalidades: agregar película (con título y clasificación), listar todas las películas de un catálogo y eliminar catálogo.

## Tecnologías utilizadas
- Python

## Requerimientos
El programa cuenta con el módulo Colorama que permite darle color a la consola y es necesario instalarlo previamente. Para estom diríjase a la terminal e ingrese el siguiente comando:

`pip install colorama`.

Si este comando no funciona, puede probar con el siguiente comando:

`conda install -c anaconda colorama`.

Esta instalación debe hacerse la primera vez que use el programa. 

## Inicio de la aplicación
1. Abrir Visual Studio Code y arrastrar la carpeta con el programa dentro e inicializar una nueva terminal.

2. Dentro de la terminal, primero hay que instalar el módulo Colorama, especificado previamente en los Requerimeitnos.

3. Una vez realizado el paso anterior, en la terminal debemos ingresar el siguiente comando de inicio: `python catalogo_peliculas.py`. Con esto se inicializa el programa.

## Menú de opciones y funcionalidades
Una vez inicializado el programa, se le dará la bienvenida y se le pedirá que ingrese el nombre de un catálogo. Si el catálogo es inexistente, el programa automáticamente lo crea para comenzar a trabajar en él. Si el catálogo ya existe, nos redirecciona al menú de opciones.

### Agregar película
Accedemos a esta opción ingresando el comando `1`.

Esta opción va a trabajar sobre el catálogo que ingresamos previamente al inicio del programa. Es decir, si elegimos el catálogo "Terror", las peliculas que se ingresen se guardarán dentro de ese catálogo. 

Dentro de funcionalidad "Agregar película", el programa nos pedirá que ingresemos el nombre de la película y luego su clasificación. Si la película no existe en el archivo, será creada. En caso de que ya existiera una película con ese nombre, el programa le dará aviso para que no existan duplicados.

Una vez ingresada la nueva película, nos devuelve automaticamente al menú de opciones para seguir gestionando el catálogo. 

### Mostrar catálogo de películas
A esta opción accedemos ingresando el comando `2`.

Eesta opción nos va a permitir ver todas las películas que se hayan guardado en nuestro catálogo. Una vez realizada la operación, el programa muestra nuevamente el menú de opciones. 

### Eliminar catálogo de películas
A esta opción se accede con el comando `3`.

Esta opción nos va a permitir eliminar el catálogo en su totalidad. El programa nos va a pedir una confirmación de Si/No para validar nuestra opción.

Si se confirma la operación, se elimina el catálogo elegido en su totalidad.

Si se decide no eliminar el catálogo, el programa retorna al inicio. 

### Cambiar a otro catálogo de películas
A esta opción se accede con el comando `4`.

Esta funcionalidad sirve si deseamos operar en otro catálogo. Para ello, el programa nos pedirá confirmación de salida con si/no. Si la respuesta es "No", volvemos al menú de opciones. Si la respuesta es "Si", el programa nos va a pedir que ingresemos el nombre del nuevo catálogo. 

### Salir
A esta opción se accede con el comando `5`.

Esta opción permite salir y cerrar el programa de forma correcta. Si deseamos volver a iniciarlo, debemos ingresar nuevamente el comando de inicialización. 