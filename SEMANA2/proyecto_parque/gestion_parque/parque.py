precios = {
    "Montaña Rusa": 1500,
    "Casa del Terror": 1200,
    "Carrusel": 800
}

def mostrar_atracciones():
    print("\nAtracciones disponibles:")
    for i, (atraccion, precio) in enumerate(precios.items(), start=1):
        print(f"{i}. {atraccion} (${precio})")

def obtener_atraccion(numero):
    lista_atracciones = list(precios.keys())
    if 1 <= numero <= len(lista_atracciones):
        return lista_atracciones[numero - 1]
    else:
        return None

def puede_subir(edad, atraccion):
    if atraccion == "Montaña Rusa":
        return edad >= 12
    elif atraccion == "Casa del Terror":
        return edad >= 6
    elif atraccion == "Carrusel":
        return True
    else:
        return False

def calcular_precio(atraccion):
    return precios.get(atraccion, 0)

def registrar_visita():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    cant_atracciones = int(input("¿Cuántas atracciones quiere usar?(Maximo 3): "))

    atracciones_elegidas = []
    atracciones_permitidas = []
    costo_total = 0

    for i in range(cant_atracciones):
        mostrar_atracciones()
        try:
            numero = int(input(f"Elija la atracción #{i+1} (ingrese número): "))
        except ValueError:
            print("Entrada inválida.")
            continue

        eleccion = obtener_atraccion(numero)

        if not eleccion:
            print("Opción inválida.")
            continue

        atracciones_elegidas.append(eleccion)

        if puede_subir(edad, eleccion):
            atracciones_permitidas.append(eleccion)
            costo_total += calcular_precio(eleccion)
            print(f"Puede subir a {eleccion}")
        else:
            print(f"No puede subir a {eleccion} por su edad.")

    resumen = {
        "nombre": nombre,
        "edad": edad,
        "atracciones_elegidas": atracciones_elegidas,
        "atracciones_permitidas": atracciones_permitidas,
        "costo_total": costo_total
    }
    return resumen

def mostrar_resumen(resumen):
    print("\n--- RESUMEN ---")
    print(f"Visitante: {resumen['nombre']} ({resumen['edad']} años)")
    print("Atracciones elegidas:", resumen["atracciones_elegidas"])
    print("Atracciones permitidas:", resumen["atracciones_permitidas"])
    print(f"Costo total a pagar: ${resumen['costo_total']}")