#Declarar un array de 10 enteros. Cargarlo por teclado
#Calcular y mostrar la suma de todos los elementos.

vec_numeros = [0] * 10

for i in range(len(vec_numeros)):
    vec_numeros[i] = int(input("ingresar numeros: "))

suma_numeros = 0
for i in range(len(vec_numeros)):
    suma_numeros += vec_numeros[i]

print(f"la suma de los numeros es: {suma_numeros}")
    