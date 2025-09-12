#Declarar un array de 6 números reales (floats).
#Cargarlo por teclado. Calcular y mostrar 
#el promedio de los valores.

vec_notas = [0] * 6

for i in range(len(vec_notas)):
    vec_notas[i] = float(input("ingresar notas: "))

suma_numeros = 0
for i in range(len(vec_notas)):
    suma_numeros += vec_notas[i]

promedio_notas = suma_numeros / len(vec_notas)

print(f"El promedio de las notas es: {promedio_notas}")
    