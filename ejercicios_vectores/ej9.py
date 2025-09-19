#Cargar un array de 10 enteros. 
#Reemplazar todos los elementos pares por cero 
# y mostrar el array resultante.

array = [0] * 10

for i in range(10):
    array[i] = int(input(f"Ingrese el número {i+1}: "))

for i in range(10):
    if array[i] % 2 == 0:
        array[i] = 0

print("\nArray resultante:")
for i in range(10):
    print(array[i], end=" ")
