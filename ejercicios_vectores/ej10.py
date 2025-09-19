from funcion10 import buscar_numero

array = [2, 7, 6, 4, 5, 8]

num = int(input("ingrese el numero a buscar: "))

posi = buscar_numero(array, num)

if posi != -1:
    print(f" el numero {num} se encontra en la posicion: {posi}.")
else:
    print(f" el numero {num} no se encuentra en el array")