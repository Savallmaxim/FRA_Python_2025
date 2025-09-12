#Cargar un array de 10 enteros. Solicitar al usuario un número 
#y verificar si se encuentra en el array.
#Informar la posición en caso afirmativo, o indicar que no se encuentra.

vec_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input("ingrese un número: "))

encontrado = False

for i in range(len(vec_num)):
    if vec_num[i] == numero:
        print(f"El numero {numero} se encuentra en la posición {i}")
        encontrado = True
        break

if not encontrado:
    print("el número no se encuentra en el array.")
