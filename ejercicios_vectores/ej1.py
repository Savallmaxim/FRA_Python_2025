#Declarar un array de 5 enteros. Cargarlo por teclado y 
#mostrar su contenido por pantalla usando un ciclo for

vec_numeros = [0] *5

for i in range(len(vec_numeros)):
    vec_numeros[i] = int(input("ingresar numeros: "))

for i in range(len(vec_numeros)):
    print(f"los numeros son {i + 1} : {vec_numeros[i]}")
    