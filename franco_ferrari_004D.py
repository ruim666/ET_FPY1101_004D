def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por genero")
    print("2. Búsqueda de peliculas por rango de precio")
    print("3. Actualizar precio de pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except:
            print("Debe seleccionar una opción válida")


def validar_texto(texto):
    if texto.strip() != "":
        return True
    return False


def validar_clasificacion(clasificacion):
    if clasificacion == "A" or clasificacion == "B" or clasificacion == "C":
        return True
    return False


def validar_es_3d(es_3d_str):
    if es_3d_str.lower() == "s" or es_3d_str.lower() == "n":
        return True
    return False


def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        if precio > 0:
            return True
        return False
    except:
        return False


def validar_cupos(cupos_str):
    try:
        cupos = int(cupos_str)
        if cupos >= 0:
            return True
        return False
    except:
        return False


def buscar_codigo(funciones, codigo):
    if codigo in funciones:
        return True
    return False


def cupos_genero(peliculas, funciones, genero):
    genero_buscar = genero.lower()
    total_cupos = 0

    for codigo in peliculas:
        genero_actual = peliculas[codigo][1].lower()
        if genero_actual == genero_buscar:
            cupos_actual = funciones[codigo][1]
            total_cupos = total_cupos + cupos_actual

    print("El total de cupos disponibles es:", total_cupos)


def busqueda_precio(peliculas, funciones, p_min, p_max):
    resultados = []

    for codigo in funciones:
        precio = funciones[codigo][0]
        cupos = funciones[codigo][1]

        if precio >= p_min and precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]
            resultados.append(titulo + "--" + codigo)

    if len(resultados) == 0:
        print("No hay peliculas en ese rango de precios.")
    else:
        resultados.sort()
        print("Los peliculas encontrados son:", resultados)


def actualizar_precio(funciones, codigo, nuevo_precio):
    existe = buscar_codigo(funciones, codigo)
    if existe == False:
        return False
    else:
        funciones[codigo][0] = nuevo_precio
        return True


def agregar_pelicula(peliculas, funciones, codigo, titulo, genero, genero, clasificacion, es_3d, idioma, precio, cupos):
    if buscar_codigo(funciones, codigo) == True:
        return False
    else:
        es_3d_bool = False
        if es_3d == "s":
            es_3d_bool = True

        peliculas[codigo] = [titulo, genero, genero, clasificacion, es_3d_bool, idioma]
        funciones[codigo] = [precio, cupos]
        return True


def eliminar_pelicula(peliculas, funciones, codigo):
    existe = buscar_codigo(funciones, codigo)
    if existe == False:
        return False
    else:
        peliculas.pop(codigo)
        funciones.pop(codigo)
        return True

peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción ', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    
}


cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
   
}


while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        genero = input("Ingrese genero a consultar: ")
        cupos_genero(peliculas, funciones, genero)

    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    break
                else:
                    print("Debe ingresar valores enteros")
            except:
                print("Debe ingresar valores enteros")
        busqueda_precio(peliculas, funciones, p_min, p_max)

    elif opcion == 3:
        while True:
            codigo = input("Ingrese código del pelicula: ").upper()

            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        break
                    else:
                        print("Error: el precio debe ser un número entero mayor que cero.")
                except:
                    print("Error: el precio debe ser un número entero mayor que cero.")

            actualizado = actualizar_precio(funciones, codigo, nuevo_precio)
            if actualizado == True:
                print("Precio actualizado")
            else:
                print("El código no existe")

            reintentar = input("¿Desea actualizar otro precio (s/n)?: ").lower()
            if reintentar != "s":
                break

    elif opcion == 4:
        codigo = input("Ingrese código del pelicula: ").upper()
        titulo = input("Ingrese título: ")
        genero = input("Ingrese genero: ")
        genero = input("Ingrese género: ")
        clasificacion = input("Ingrese clasificación: ").upper()
        es_3d = input("¿Es es_3d? (s/n): ").lower()
        idioma = input("Ingrese idioma: ")
        precio_str = input("Ingrese precio: ")
        cupos_str = input("Ingrese cupos: ")

        codigo_ok = validar_texto(codigo) and buscar_codigo(funciones, codigo) == False
        titulo_ok = validar_texto(titulo)
        genero_ok = validar_texto(genero)
        genero_ok = validar_texto(genero)
        clasificacion_ok = validar_clasificacion(clasificacion)
        es_3d_ok = validar_es_3d(es_3d)
        idioma_ok = validar_texto(idioma)
        precio_ok = validar_precio(precio_str)
        cupos_ok = validar_cupos(cupos_str)

        if codigo_ok == False:
            print("Error: el código no puede estar vacío y no debe existir previamente.")
        elif titulo_ok == False:
            print("Error: el título no puede estar vacío.")
        elif genero_ok == False:
            print("Error: la genero no puede estar vacía.")
        elif genero_ok == False:
            print("Error: el género no puede estar vacío.")
        elif clasificacion_ok == False:
            print("Error: la clasificación debe ser exactamente 'A', 'B' o 'C'.")
        elif es_3d_ok == False:
            print("Error: para es_3d debe ingresar 's' o 'n'.")
        elif idioma_ok == False:
            print("Error: el idioma no puede estar vacío.")
        elif precio_ok == False:
            print("Error: el precio debe ser un número entero mayor que cero.")
        elif cupos_ok == False:
            print("Error: el cupos debe ser un número entero mayor o igual a cero.")
        else:
            precio = int(precio_str)
            cupos = int(cupos_str)
            agregado = agregar_pelicula(peliculas, funciones, codigo, titulo, genero, genero, clasificacion, es_3d, idioma, precio, cupos)
            if agregado == True:
                print("Película agregada")
            else:
                print("El código ya existe")

    elif opcion == 5:
        codigo = input("Ingrese código del pelicula a eliminar: ").upper()
        eliminado = eliminar_pelicula(peliculas, funciones, codigo)
        if eliminado == True:
            print("Película eliminada")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        break