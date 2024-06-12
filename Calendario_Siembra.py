import os
import colorama

# Aca definimos las especies y sus elementos.
'''Creamos un diccionario "Especie" cuyas claves son las especies, 
y los valores de estas son otro diccionario cuyas claves son los parametros de siembra,
y los valores de estas son los datos para cada parametro  '''
Especies = {
    "Acelga": {
        "Momento de siembra":"otoño, primavera",
        "Metodo de siembra": "Directa o en almacigo",
        "Profundidad de siembra": "2 cm.",
        "Distancia entre plantas": "15 a 20 cm.",
        "Distancia entre surcos" : "50 a 70 cm.",
        "Tiempo de germinacion": "7 a 9 dias",
        "Trasplante (si aplica)": "20 a 40 dias",
        "Tiempo de cosecha": "60 a 80 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "facil cultivo, resistente, se recomienda re siembra mes a mes. "
    },
    "Ajo": {
        "Momento de siembra":"otoño",
        "Metodo de siembra": "Directa",
        "Profundidad de siembra": "2 cm.",
        "Distancia entre plantas": "10 a 15 cm.",
        "Distancia entre surcos" : "35 a 45 cm.",
        "Tiempo de germinacion": "n/a",
        "Trasplante (si aplica)": "n/a",
        "Tiempo de cosecha": "240 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario, no encharcar",
        "plagas/observaciones": "facil cultivo, resistente. "
    },

    "Apio": {
        "Momento de siembra":"otoño, invierno",
        "Metodo de siembra": "Almacigo",
        "Profundidad de siembra": "0,2 cm.",
        "Distancia entre plantas": "20 a 30  cm.",
        "Distancia entre surcos" : " 70 cm.",
        "Tiempo de germinacion": "15 a 20 dias",
        "Trasplante (si aplica)": "70 dias",
        "Tiempo de cosecha": "120 a 140 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "asdasda "
    },
    "Cebolla y verdeo": {
        "Momento de siembra":"otoño",
        "Metodo de siembra": "directa o en almacigo",
        "Profundidad de siembra": "1 cm.",
        "Distancia entre plantas": "10 a 15 cm.",
        "Distancia entre surcos" : "35 a 45 cm.",
        "Tiempo de germinacion": "8 a 10 dias",
        "Trasplante (si aplica)": "20 dias",
        "Tiempo de cosecha": "100 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "cortar cabezas florales cuando empeizan a abrirse "
    },
    "Chaucha": {
        "Momento de siembra":"primavera, verano",
        "Metodo de siembra": "Directa",
        "Profundidad de siembra": "3 a 5 cm.",
        "Distancia entre plantas": "20 a 30 cm.",
        "Distancia entre surcos" : "70 a 80 cm.",
        "Tiempo de germinacion": "7 a 8 dias",
        "Trasplante (si aplica)": "n/a",
        "Tiempo de cosecha": "90 a 120  dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "necesita tutor o grilla"
    },
    "Habas": {
        "Momento de siembra":"otoño, invierno",
        "Metodo de siembra": "directa o en almacigo",
        "Profundidad de siembra": "0,5 cm.",
        "Distancia entre plantas": "15 cm.",
        "Distancia entre surcos" : "40 cm.",
        "Tiempo de germinacion": "7 a 8 dias",
        "Trasplante (si aplica)": "20 dias",
        "Tiempo de cosecha": "90 a 120 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "necesita tutor o grilla "
    },
   "Lechuga": {
       "Momento de siembra":"todo el año",
        "Metodo de siembra": "directa o en almacigo",
        "Profundidad de siembra": "0,5 cm.",
        "Distancia entre plantas": "15 a 20 cm.",
        "Distancia entre surcos" : "25 a 40 cm.",
        "Tiempo de germinacion": "7 a 8 dias",
        "Trasplante (si aplica)": "20 a 40 dias",
        "Tiempo de cosecha": "60 a 90 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "cortar planta entera cuando asoma florescencia "
    },
    "Pimiento": {
        "Momento de siembra": "invierno",
        "Metodo de siembra": "almacigo",
        "Profundidad de siembra": "3 a 5 cm.",
        "Distancia entre plantas": "40 a 45 cm.",
        "Distancia entre surcos" : "70 a 80 cm.",
        "Tiempo de germinacion": "3 a 5 dias",
        "Trasplante (si aplica)": "40 a 60 dias",
        "Tiempo de cosecha": "90  a 120 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "siembra en almacigo protegido, se transplanta en setiembre "
    },
    "Puerro": {
        "Momento de siembra":"otoño, primavera",
        "Metodo de siembra": "directa o en almacigo",
        "Profundidad de siembra": "1 a 2 cm.",
        "Distancia entre plantas": "15 cm.",
        "Distancia entre surcos" : "40 cm.",
        "Tiempo de germinacion": "8 a 10 dias",
        "Trasplante (si aplica)": "20 a 30 dias",
        "Tiempo de cosecha": "120 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "cortar florescencia cuando empieza a abrir "
    },
    "Rabanito": {
        "Momento de siembra":"todo el año",
        "Metodo de siembra": "directa o en almacigo",
        "Profundidad de siembra": "2 cm.",
        "Distancia entre plantas": "5 a 10 cm.",
        "Distancia entre surcos" : "40 a 45 cm.",
        "Tiempo de germinacion": "7 a 9 dias",
        "Trasplante (si aplica)": "20 a 40 dias",
        "Tiempo de cosecha": "90 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "asdasda "
    },

    "Remolacha": {
        "Momento de siembra":"otoño, primavera",
        "Metodo de siembra": "directa almacigo",
        "Profundidad de siembra": "2 cm.",
        "Distancia entre plantas": "8 a 10 cm.",
        "Distancia entre surcos" : "35 a 45 cm.",
        "Tiempo de germinacion": "7 a 9 dias",
        "Trasplante (si aplica)": "20 a 40 dias",
        "Tiempo de cosecha": "100 a 130 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "resistente,pero necesita buen riego"
    },

    "Rucula": {
        "Momento de siembra":"otoño, primavera",
        "Metodo de siembra": "directa",
        "Profundidad de siembra": "2 cm.",
        "Distancia entre plantas": "a chorrillo.",
        "Distancia entre surcos" : "40 a 45 cm.",
        "Tiempo de germinacion": "7 a 9 dias",
        "Trasplante (si aplica)": "n/a",
        "Tiempo de cosecha": "60 a 80 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "se recomienda siembra escalonada mensual"
    },

    "Tomate": {
        "Momento de siembra":"primavera",
        "Metodo de siembra": "almacigo",
        "Profundidad de siembra": "2 cm.",
        "Distancia entre plantas": "20 a 40 cm.",
        "Distancia entre surcos" : "80 a 90 cm.",
        "Tiempo de germinacion": "5 a 8 dias",
        "Trasplante (si aplica)": "40 a 60 dias",
        "Tiempo de cosecha": "120 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "cortar chupones, necesita tutor, o atadura "
    },

    "Zanahoria": {
        "Momento de siembra":"todo el año",
        "Metodo de siembra": "directa",
        "Profundidad de siembra": "1 a 2 cm.",
        "Distancia entre plantas": "chorrillo ralo.",
        "Distancia entre surcos" : "40 a 45 cm.",
        "Tiempo de germinacion": "10 a 15 dias",
        "Trasplante (si aplica)": "n/a dias",
        "Tiempo de cosecha": "100 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "necesita tierra profunda y aireada "
    },

    "Zapallo": {
        "Momento de siembra":"primavera, verano",
        "Metodo de siembra": "directa",
        "Profundidad de siembra": "2 cm.",
        "Distancia entre plantas": "100 a 150 cm.",
        "Distancia entre surcos" : "200 a 300 cm.",
        "Tiempo de germinacion": "5 a 10 dias",
        "Trasplante (si aplica)": "n/a",
        "Tiempo de cosecha": "180 a 200 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "no olvidar polinizar, puede tutorarse"
    },

    "Zapallito": {
        "Momento de siembra":"primavera, verano",
        "Metodo de siembra": "directa o en almacigo",
        "Profundidad de siembra": "1 a 2 cm.",
        "Distancia entre plantas": "80 a 100 cm.",
        "Distancia entre surcos" : "80 a 100 cm.",
        "Tiempo de germinacion": "5 a 10 dias",
        "Trasplante (si aplica)": "20 a 40 dias",
        "Tiempo de cosecha": "90 a 100 dias",
        "Abonado": "tierra abonada, compost",
        "Riego": "Al sustrato, diario",
        "plagas/observaciones": "no olvidar polinizar, puede tutorarse"
    },
    # ... otras especies ..
}

#funcion para limpiar la pantalla.
'''En esta Funcion:
Llamamos al modulo os 
para utilizar el metodo cls o clear,
segun el sistema operativo'''
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

#funcion para buscar por especie.
def buscar_por_especie(busqueda_especie):
    '''
    En esta función:
    Luego de obtener los elementos de la especie buscada
    se construye un string "detalles_formateados" dentro de un bucle for,
    añadiendo cada clave y valor junto con un salto de línea \n al final.
    Esto asegura que cada par clave-valor se imprima en una nueva línea,
    manteniendo la legibilidad. Luego le damos color.
    '''
    print(colorama.Fore.RED + "*" * 50)
    print(colorama.Fore.GREEN + "Usted eligió Búsqueda por Especie.")
    print(colorama.Fore.RED + "*" * 50)
    # Convertimos el argumento a minúsculas para la comparación.
    busqueda_especie = busqueda_especie.lower()
    # Buscamos en el diccionario convirtiendo las claves a minúsculas.
    busqueda = {k.lower(): v for k, v in Especies.items()}.get(busqueda_especie)
    if busqueda:
        # si busqueda es True (valor encontrado), se crea una string vacia.
        detalles_formateados = ""
        #se itera sobre el Diccionario obteneiendo claves y valores relacionados a la busqueda.
        for clave, valor in busqueda.items():
            #y se agregan a la string vacia formateados para presentar una salida agradable.
            detalles_formateados += f"{colorama.Fore.GREEN + clave}: {colorama.Fore.RESET + valor}\n"
        print(f"{colorama.Fore.YELLOW + busqueda_especie}:\n{detalles_formateados}")
    else:
        print(f"{busqueda_especie} no encontrada en la estructura de datos.")


#funcion para buscar por estacion.
'''En este código, la función buscar_por_estacion realiza los siguientes pasos:
1- Imprime un mensaje indicando que se eligió la búsqueda por estación.
2 - Inicializa una lista para almacenar las especies que coinciden con la estación proporcionada.
3 - Itera sobre las especies y sus detalles.
4 - Divide el valor de "Momento de siembra" en una lista de estaciones y convierte cada estación a minúsculas para la comparación.
5 - Verifica si la estación proporcionada está en la lista de estaciones.
Si se encuentra una coincidencia, agrega la especie a la lista busqueda_estacion.
6 - Formatea y muestra los detalles de las especies encontradas.
Si no se encuentran coincidencias, imprime un mensaje indicando que no se encontraron especies para la estación proporcionada.'''
def buscar_por_estacion(estacion):
    print(colorama.Fore.RED + "*" * 50)
    print(colorama.Fore.GREEN + "Usted a seleccionado: Busqueda por estacion.")
    print(colorama.Fore.RED + "*" * 50)
    #formateamos el argumento recibido pasandolo a minusculas y sacandole espacios
    estacion = estacion.lower().strip()
    #creamos una lista vacia
    busqueda_estacion = []
    # iteramos sobre el diccionario Especies
    for especie, detalles in Especies.items():
        #obtenemos los detalles de la clave "Momento de siembra"
        momento_de_siembra = detalles.get("Momento de siembra", "")
        #formatea los valores encontrados ( estaciones) a minusculas, sin espacios y separados por coma.
        estaciones = [e.strip().lower() for e in momento_de_siembra.split(',')]
        # y si la estacion buscada esta en la especie iterada, la agrega a la lista antes creada
        if estacion in estaciones:
            busqueda_estacion.append(especie)
    # aca si la lista tiene contenido (True), o sea encontro especies que contienen la estacion buscada.
    if busqueda_estacion:
        #imprime un mensaje formateado
        limpiarPantalla()
        print(colorama.Fore.RESET + f"Especies que se pueden sembrar en {colorama.Fore.YELLOW + estacion.capitalize()}:")
        #iterando en cada especie y mostrandolas.
        for especie in busqueda_estacion:
            print(colorama.Fore.GREEN + f"- {especie}")
        #aca se pregunta si se quiere ver en detalle alguna especie.
        ver_detalles = input("¿Quieres ver los detalles de alguna especie? (s/n): ").strip().lower()
        #y de confirmar con s o S (gracias al formateo ,strip y .lower en el input).
        if ver_detalles == "s":
            #se pregunta que especie quiere ver.
            especie_seleccionada = input("Escribe el nombre de la especie que quieres ver: ").strip().capitalize()
            # aca se verifica que le especie elegida este en el diccionario.
            if especie_seleccionada in busqueda_estacion:
                #se obtienen sus detalles
                detalles = Especies[especie_seleccionada]
                #y se crea una cadena vacia.
                detalles_formateados = ""
                #donde luego de iterar sobre las claves y valores de la lista.
                for clave, valor in detalles.items():
                    #se formatea para una linda salida.
                    detalles_formateados += f"{colorama.Fore.GREEN + clave}: {colorama.Fore.RESET + valor}\n"
                    limpiarPantalla()    
                print(f"{colorama.Fore.YELLOW + especie_seleccionada}:\n{detalles_formateados}")
            else:
                #aca se avisa si la especie no fue encontrada
                print(f"La especie {especie_seleccionada} no está en la lista de especies para {estacion}.")
    else:
        # aca se avisa que no hay especie con ese criterio de busqueda.
        print(f"No se encontraron especies para el momento de siembra: {estacion}")

    
#funcion para agregar Especie.
'''En esta funcion:
Creamos un diccionario vacio con clave "Nombre de la especie"
al que vamos llenando a traves de ir pidiendo al usuario
cargar cada uno de sus elementos
que luego se agrega a nuestra coleccion de especies'''
def Agregar_especie():
    print(colorama.Fore.RED + "*" * 50)
    print(colorama.Fore.GREEN + "Usted a seleccionado: Agregar una especie.")
    print(colorama.Fore.RED + "*" * 50)
    #aca creamos un diccionario vacio.
    especie_elementos = {}
    # donde se almacenan los valores ingresados por input, asociados a cada clave.
    #aca el nombre de la especie
    especie_nombre = input(colorama.Fore.RESET + "Ingresa el nombre de la especie: ")
    # y en los siguientes renglones  se piden los valores de cada clave
    especie_elementos["Nombre"] = especie_nombre
    especie_elementos["Momento de siembra"] = input("Momento de siembra: ")
    especie_elementos["Método de siembra"] = input("Método de siembra: ")
    especie_elementos["Profundidad de siembra"] = input("Profundidad de siembra: ")
    especie_elementos["Distancia entre plantas"] = input("Distancia entre plantas: ")
    especie_elementos["Distancia entre surcos"] = input("Distancia entre surcos: ")
    especie_elementos["Tiempo de germinacion: "] = input("Tiempo de germinacion: ")
    especie_elementos["Trasplante (si aplica)"] = input("Trasplante (si aplica): ")
    especie_elementos["Tiempo de cosecha"] = input("Tiempo de cosecha: ")
    especie_elementos["Abonado"] = input("Abonado: ")
    especie_elementos["Riego"]  = input("Riego: ")
    especie_elementos["plagas/observaciones"] = input("Plagas/observaciones: ")
    #aca damos confirmacion.
    print(f"La especie {especie_nombre} se ha agregado con exito!.")
    return especie_elementos

#Funcion para modificar Especies.
'''En esta funcion:
Recorre y verifica que este la especie ingresada, 
Luego crea un diccionario que si no se deja vacio ( por eso el "or"),
ingresa y guarda los nuevos valores 
asociados a su clave modificando (o no),los previos '''
def Modificar_especie(nombre_especie):
    print(colorama.Fore.RED + "*" * 50)
    print(colorama.Fore.GREEN + "Usted ha seleccionado: Modificar una especie.")
    print(colorama.Fore.RED + "*" * 50)
    #aca si se encuentra la especie buscada en el diccionario Especies.
    if nombre_especie in Especies:
        #se crea un diccionario donde se pisan (input)o se dejan (enter) los valores asociados a cada clave.
        especie_elementos = Especies[nombre_especie]
        print(colorama.Fore.RESET +"Ingresa los nuevos valores para la especie:(deja vacío para mantener el valor actual):")
        especie_elementos["Momento de siembra"] = input("Nuevo momento de siembra: ") or especie_elementos["Momento de siembra"]
        especie_elementos["Método de siembra"] = input("Nuevo método de siembra: ") or especie_elementos["Método de siembra"]
        especie_elementos["Profundidad de siembra"] = input("Nueva profundidad de siembra: ") or especie_elementos["Profundidad de siembra"]
        especie_elementos["Distancia entre plantas"] = input("Nueva distancia entre plantas: ") or especie_elementos["Distancia entre plantas"]
        especie_elementos["Distancia entre surcos"] = input("Nueva distancia entre surcos: ") or especie_elementos["Distancia entre surcos"]
        especie_elementos["Tiempo de germinación"] = input("Nueva tiempo de germinación: ") or especie_elementos["Tiempo de germinación"]
        especie_elementos["Trasplante (si aplica)"] = input("Nuevo trasplante (si aplica): ") or especie_elementos["Trasplante (si aplica)"]
        especie_elementos["Tiempo de cosecha"] = input("Nuevo tiempo de cosecha: ") or especie_elementos["Tiempo de cosecha"]
        especie_elementos["Abonado"] = input("Nuevo abonado: ") or especie_elementos["Abonado"]
        especie_elementos["Riego"] = input("Nuevo riego: ") or especie_elementos["Riego"]
        especie_elementos["plagas/observaciones"] = input("Nuevas plagas/observaciones: ") or especie_elementos["plagas/observaciones"]
        #sobre escribe el nombre de la especie modficada en la clave correspondiente del diccionario "Especies".
        Especies[nombre_especie] = especie_elementos
        #imprime confirmacion.
        print("La especie '{}' ha sido modificada correctamente.".format(nombre_especie))
    # o avisa que no ha sido encontrada.
    else:
        print("La especie '{}' no existe en el diccionario.".format(nombre_especie))

#Funcion para eliminar Especie.
'''En esta funcion:
Eliminamos un diccionario dentro de Especies'''
def Eliminar_especie(nombre_especie):
    #si la especie es encontrada.
    if nombre_especie in Especies:
        #la borra del diccionario.
        del Especies[nombre_especie]
        #imprime confirmacion
        print(colorama.Fore.RESET +"La especie '{}' ha sido eliminada correctamente.".format(nombre_especie))
    # o avisa que no ha sido encontrada.    
    else:
        print("La especie '{}' no existe en el diccionario.".format(nombre_especie))

#Funcion para listar las Especies.
'''En esta funcion:
Recorremos al diccionario con un for 
para extraer por separado las claves y valores y mostrarlas formateadas para 
mejor visibilidad y atractivo'''
def Listar_especies():
    print(colorama.Fore.RED + "*" * 50)
    print(colorama.Fore.GREEN + "Usted ha elegido: Listar especies existentes.")
    print(colorama.Fore.RED + "*" * 50)
    print("")
    print(colorama.Fore.GREEN + "Lista de especies:")
    print("")
    #aca se itera sobre el diccionario para extraer las claves y valores
    for especie, atributos in Especies.items():
        # y se imprime el nombre de la especie en un color
        print(colorama.Fore.YELLOW + especie + colorama.Fore.RESET)
        # y iterando sobre las claves y valores de cada especie  se formatean en distintos colores
        for atributo, valor in atributos.items():
            print(colorama.Fore.GREEN + "   {}: ".format(atributo) + colorama.Fore.RESET + "{}".format(valor))
        print()  # Agrega una línea en blanco para separar las especies

#Funcion para generar el menu
'''En esta funcion:
Creamos un menu formateado en el que le pedimos al usuario ingresar una opcion
segun su necesidad'''
def menu():
    limpiarPantalla()
    print(colorama.Fore.RED + "*" * 50)
    print(colorama.Fore.GREEN + "CALENDARIO ANUAL DE SIEMBRA HEMISFERIO SUR".center(45))
    print(colorama.Fore.RED + "*" * 50)
    print("")
    print(colorama.Fore.GREEN + "1" + colorama.Fore.RESET + " Para efectuar una busqueda por especie")
    print(colorama.Fore.GREEN + "2" + colorama.Fore.RESET + " Para efectuar una busqueda por estación")
    print(colorama.Fore.GREEN + "3" + colorama.Fore.RESET + " para agregar una especie")
    print(colorama.Fore.GREEN + "4" + colorama.Fore.RESET + " para modificar una especie")
    print(colorama.Fore.GREEN + "5" + colorama.Fore.RESET + " para eliminar una especie")
    print(colorama.Fore.GREEN + "6" + colorama.Fore.RESET + " para listar las especies existentes")
    print(colorama.Fore.GREEN + "7" + colorama.Fore.RESET + " para salir")
    op=int(input("seleccione una opción:"))
    return op
op=menu()

#Programa principal
'''Este es el programa principal:
Aqui a traves de un condicional, segun la opcion ingresada
se llama a la funcion requerida'''
while op != 7:
    match op:
        case 1:
            busqueda_especie = input(colorama.Fore.RESET + "Ingrese la especie buscada: ")
            limpiarPantalla()
            buscar_por_especie(busqueda_especie)
            input(colorama.Fore.RED + "Presione enter para continuar.")
        case 2:
            estacion = input(colorama.Fore.RESET + "Ingrese la estación buscada: ")
            limpiarPantalla()
            buscar_por_estacion(estacion)
            input(colorama.Fore.RED + "Presione enter para continuar.")
        case 3:
            limpiarPantalla()
            nueva_especie = Agregar_especie()
            Especies[nueva_especie["Nombre"]] = nueva_especie
            input(colorama.Fore.RED + "Presione enter para continuar.")
        case 4:
            limpiarPantalla()
            nombre_a_modificar = input("Ingresa el nombre de la especie que deseas modificar: ")
            Modificar_especie(nombre_a_modificar)
            input(colorama.Fore.RED + "Presione enter para continuar.")
        case 5:
            limpiarPantalla()
            print(colorama.Fore.RED + "*" * 50)
            print(colorama.Fore.GREEN+"Usted ha seleccionado: Eliminar una especie")
            print(colorama.Fore.RED + "*" * 50)
            nombre_a_eliminar = input(colorama.Fore.RESET +"Ingresa el nombre de la especie que deseas eliminar: ")
            confirmacion = input("Realmente quiere eliminar esta especie? s/n:")
            if confirmacion.lower() == "s": 
                Eliminar_especie(nombre_a_eliminar)
            else:
                print("Operacion cancelada por el usuario.")
            input(colorama.Fore.RED + "Presione enter para continuar.")
        case 6:
            limpiarPantalla()
            Listar_especies()
            input(colorama.Fore.RED + "Presione enter para continuar.")
        case _:
            print("Opcion no valida!.")
    op=menu()

    







