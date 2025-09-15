from fun_menu import *

titulos = [""] * 20
ejemplares = [0] * 20
cant_libros = 0

opcion = 0
while opcion != 7:
    print("\n---- MENU ----")
    print("1-Cargar titulos y ejemplares")
    print("2-Mostrar catalogo completo")
    print("3-Consultar disponibilidad")
    print("4-Listar titulos agotados")
    print("5-Agregar un nuevo titulo")
    print("6-Actualizar ejemplares (prestamo o devolución)")
    print("7-Salir")

    opcion = int(input("ingrese una opción: "))

    if opcion == 1:
        cant_libros = cargar_titulos(titulos, ejemplares, cant_libros)
    elif opcion == 2:
        mostrar_catalogo(titulos, ejemplares, cant_libros)
    elif opcion == 3:
        consultar_disponibilidad(titulos, ejemplares, cant_libros)
    elif opcion == 4:
        listar_agotados(titulos, ejemplares, cant_libros)
    elif opcion == 5:
        cant_libros = agregar_titulo(titulos, ejemplares, cant_libros)
    elif opcion == 6:
        actualizar_ejemplares(titulos, ejemplares, cant_libros)
    elif opcion == 7:
        print("programa terminado")
    else:
        print("opcion invalida, intente de nuevo")