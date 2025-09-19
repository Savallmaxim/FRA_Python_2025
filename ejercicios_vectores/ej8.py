#Cargar dos arrays de 5 elementos cada uno. 
#Comparar si ambos son iguales elemento a elemento
#y mostrar un mensaje indicando si son o no iguales.

array1 = [0] * 5
array2 = [0] * 5


print("cargar los primeros numeros:")
for i in range(5):
    array1[i] = int(input(f"ingrese el elemento {i+1} del primer array: "))

print("\ncargar los numeros a comparar:")
for i in range(5):
    array2[i] = int(input(f"ingrese el elemento {i+1} del segundo array: "))

#comparacion 
iguales = True
for i in range(5):
    if array1[i] != array2[i]:
        iguales = False
        break

if iguales:
    print("\n los dos arrays son iguales")
else:
    print("\n los arrays son diferentes")
