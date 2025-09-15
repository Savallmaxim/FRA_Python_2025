def cargar_titulos(titulos, ejemplares, cant_libros):
    print("\n--- CARGUE LOS TITULOS Y EJEMPLARES ---")
    while cant_libros < 20:
        titulo = input("ingrese el titulo del libro (o fin para terminar): ")
        if titulo == "fin":
            break
        cantidad = int(input("ingrese cantidad de ejemplares: "))
        titulos[cant_libros] = titulo
        ejemplares[cant_libros] = cantidad
        cant_libros += 1
    return cant_libros


def mostrar_catalogo(titulos, ejemplares, cant_libros):
    print("\n--- CATALOGO COMPLETO ---")
    if cant_libros == 0:
        print("no hay libros cargados")
    else:
        for i in range(cant_libros):
            print(titulos[i], "->", ejemplares[i], "copias")


def consultar_disponibilidad(titulos, ejemplares, cant_libros):
    print("\n--- CONSULTAR DISPONIBILIDAD ---")
    buscar = input("ingrese el titulo a consultar: ")
    encontrado = False
    for i in range(cant_libros):
        if titulos[i] == buscar:
            print(titulos[i], "->", ejemplares[i], "copias")
            encontrado = True
    if not encontrado:
        print("ese titulo no esta en el catalogo")


def listar_agotados(titulos, ejemplares, cant_libros):
    print("\n--- TITULOS AGOTADOS ---")
    hay_agotados = False
    for i in range(cant_libros):
        if ejemplares[i] == 0:
            print(titulos[i])
            hay_agotados = True
    if not hay_agotados:
        print("no hay titulos agotados")


def agregar_titulo(titulos, ejemplares, cant_libros):
    print("\n--- AGREGUE UN NUEVO TITULO ---")
    if cant_libros < 20:
        nuevo = input("ingrese el titulo del nuevo libro: ")
        repetido = False
        for i in range(cant_libros):
            if titulos[i] == nuevo:
                repetido = True
        if repetido:
            print("ese titulo ya existe")
        else:
            cantidad = int(input("ingrese cantidad de ejemplares: "))
            titulos[cant_libros] = nuevo
            ejemplares[cant_libros] = cantidad
            cant_libros += 1
    else:
        print("no se pueden agregar mas titulos")
    return cant_libros


def actualizar_ejemplares(titulos, ejemplares, cant_libros):
    print("\n--- ACTUALIZAR EJEMPLARES ---")
    libro = input("ingrese el titulo del libro: ")
    encontrado = False
    for i in range(cant_libros):
        if titulos[i] == libro:
            cambio = int(input("ingrese cantidad a modificar (positiva=devolución, negativa=préstamo): "))
            ejemplares[i] = ejemplares[i] + cambio
            if ejemplares[i] < 0:
                ejemplares[i] = 0
            print("ejemplares actualizados:", titulos[i], "->", ejemplares[i], "copias")
            encontrado = True
    if not encontrado:
        print("ese titulo no esta en el catalogo")
