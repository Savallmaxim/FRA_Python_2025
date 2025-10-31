MAX = 10

def ingr_txt(mensaje):
    texto = ""
    while texto == "":
        texto = input(mensaje)
        if texto == "":
            print("ERROR! Este campo no puede quedar en blanco!!!")
    return texto

def num_es_entero(cadena):
    if not cadena:
        return False
    
    for caracter in cadena:
        if not ('0' <= caracter <= '9'):
            return False
    return True

def ingresar_puntuacion(mensaje):
    while True:
        entrada = input(mensaje)
        
        if not num_es_entero(entrada):
            print("ERROR! Debe ingresar un numero entero positivo!")
            continue
        
        numero = int(entrada)
        
        if 1 <= numero <= 10:
            return numero
        else:
            print("ERROR! La puntuacion debe estar entre 1 y 10!")

# datos de los empleados

def ingresar_datos(nombres, puntuaciones, comentarios, cantidad_cargada, max_tamano):
    
    if cantidad_cargada >= max_tamano:
        print(f"El registro esta lleno(Máximo {max_tamano} empleados)")
        return cantidad_cargada

    while cantidad_cargada < max_tamano:
        i = cantidad_cargada 
        print(f"\n--- Empleado {i + 1} de {max_tamano} ---")
        
        nombres[i] = ingr_txt("Ingrese nombre completo: ")
        puntuaciones[i] = ingresar_puntuacion("Ingrese puntuacion de desempeño (1-10): ")
        comentarios[i] = ingr_txt("Ingrese comentario del supervisor: ")

        cantidad_cargada += 1
        
        if cantidad_cargada < max_tamano: 
            continuar = ""
            while continuar != "s" and continuar != "n":
                continuar = input("Desea ingresar otro empleado? (s/n): ")
            
            if continuar == "n":
                break
            
    print(f"\nCarga de datos finalizada, {cantidad_cargada} empleados registrados!")
    return cantidad_cargada
    
# mostrar todos los registros

def mostrar_registros(nombres, puntuaciones, comentarios, cantidad_cargada):
    if cantidad_cargada == 0:
        print("-No hay datos de empleados cargados--")
        return
        
    suma_puntuaciones = 0

    print("\n--- REGISTRO DE DESEMPEÑO ---")
    for i in range(cantidad_cargada):
        nombre = nombres[i]
        puntuacion = puntuaciones[i]
        comentario = comentarios[i]
        
        print(f"{i + 1}. nombre: {nombre} | puntuacion: {puntuacion} | comentario: {comentario}")
        suma_puntuaciones += puntuacion
        
    promedio_desempeno = suma_puntuaciones / cantidad_cargada 
    print(f"\npromedio general de desempeño: {promedio_desempeno:.2f}")

# ordenar empleados

def ordenar_empleados(nombres, puntuaciones, comentarios, cantidad_cargada):
    if cantidad_cargada == 0:
        print("no hay datos cargados para ordenar")
        return
    
    n = cantidad_cargada
  #---  
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if puntuaciones[j] > puntuaciones[j + 1]:
                
                puntuaciones[j], puntuaciones[j + 1] = puntuaciones[j + 1], puntuaciones[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                comentarios[j], comentarios[j + 1] = comentarios[j + 1], comentarios[j]
    
    print("\n--- REGISTROS ORDENADOS (menor a mayor) ---")
    for i in range(cantidad_cargada):
        print(f"{i + 1}. puntuacion: {puntuaciones[i]} | nombre: {nombres[i]} | comentario: {comentarios[i]}")
  #---

#bloque inicial

if __name__ == "__main__":
    lista_nombres = [""] * MAX
    lista_puntuaciones = [0] * MAX
    lista_comentarios = [""] * MAX
    cantidad_cargada = 0 

    while True:
        print("\n\n---- REGISTRO DE DESEMPEÑO DE EMPLEADOS -----")
        print("1. Ingresar datos de los empleados")
        print("2. Mostrar todos los registros y promedio")
        print("3. Ordenar empleados por puntuacion (Menor a Mayor)")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cantidad_cargada = ingresar_datos(lista_nombres, lista_puntuaciones, lista_comentarios, cantidad_cargada, MAX)
        elif opcion == "2":
            mostrar_registros(lista_nombres, lista_puntuaciones, lista_comentarios, cantidad_cargada)
        elif opcion == "3":
            ordenar_empleados(lista_nombres, lista_puntuaciones, lista_comentarios, cantidad_cargada)
        elif opcion == "4":
            print("Programa terminado!")
            break
        else:
            print("Opcion invalida, intente nuevamente!")