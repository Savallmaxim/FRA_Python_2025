MAX_LIBROS = 20
titulos = [""] * MAX_LIBROS
ejemplares = [0] * MAX_LIBROS
cant_libros = 0

opcion = 0

while opcion != 7:
    print("\n---- MENU ----")
    print("1-Cargar titulos y ejemplares")
    print("2-Mostrar catalogo completo")
    print("3-Consultar disponibilidad")
    print("4-listar titulos agotados")
    print("5-agregar un nuevo titulo")
    print("6-Actualizar ejemplares (prestamo o devolución)")
    print("7-Salir")

    opcion = int(input("ingrese una opción: "))

    if opcion == 1:
        print("\n--- CARGUE LOS TITULOS Y EJEMPLARES ---")
        while cant_libros < MAX_LIBROS:
            titulo = input("ingrese el titulo del libro (o fin para terminar): ")
            if titulo == "fin":
                break
            cantidad = int(input("ingrese cantidad de ejemplares: "))
            titulos[cant_libros] = titulo
            ejemplares[cant_libros] = cantidad
            cant_libros += 1
    elif opcion == 2:
        print("\n--- CATALOGO COMPLETO ---")
        if cant_libros == 0:
            print("no hay libros cargados")
        else:
            for i in range(cant_libros):
                print(titulos[i], "->", ejemplares[i], "copias")
    elif opcion == 3:
        print("\n--- consultar disponibilidad ---")
        buscar = input("ingrese el titulo a consultar: ")
        encontrado = False
        for i in range(cant_libros):
            if titulos[i] == buscar:
                print(titulos[i], "->", ejemplares[i], "copias")
                encontrado = True
        if encontrado == False:
            print("ese titulo no esta en el catalogo")
    elif opcion == 4:
        print("\n--- TITULOS AGOTADOS ---")
        hay_agotados = False
        for i in range(cant_libros):
            if ejemplares[i] == 0:
                print(titulos[i])
                hay_agotados = True
        if hay_agotados == False:
            print("no hay titulos agotados")
    elif opcion == 5:
        print("\n--- AGREGUE UN NUEVO TITULO ---")
        if cant_libros < MAX_LIBROS:
            nuevo = input("ingrese el titulo del nuevo libro: ")
            repetido = False
            for i in range(cant_libros):
                if titulos[i] == nuevo:
                    repetido = True
            if repetido == True:
                print("ese titulo ya existe")
            else:
                cantidad = int(input("ingrese cantidad de ejemplares: "))
                titulos[cant_libros] = nuevo
                ejemplares[cant_libros] = cantidad
                cant_libros += 1
        else:
            print("no se pueden agregar mas titulos")
    elif opcion == 6:
        print("\n--- actualizar ejemplares ---")
        libro = input("ingrese el titulo del libro: ")
        encontrado = False
        for i in range(cant_libros):
            if titulos[i] == libro:
                cambio = int(input("ingrese cantidad a modificar (cantidad positiva = devolución - cantidad negativa = prestamo): "))
                #si pongo 2 se devulven 2 y se suman a los ejemplares, y si pongo -1 se le restan a los ejemplares y se muestran los que quedan
                ejemplares[i] = ejemplares[i] + cambio
                if ejemplares[i] < 0:
                    ejemplares[i] = 0
                print("ejemplares actualizados:", titulos[i], "->", ejemplares[i], "copias")
                encontrado = True
        if encontrado == False:
            print("ese titulo no esta en el catalogo")
    elif opcion == 7:
        print("programa terminado")
    else:
        print("opcion invalida, intente de nuevo")
