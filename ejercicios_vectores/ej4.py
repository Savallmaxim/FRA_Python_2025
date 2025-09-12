#Cargar un array de 8 enteros. Contar cuántos son mayores 
#al valor 100 e informar el resultado.

vec_num = [0] * 8

for i in range(len(vec_num)):
    vec_num[i] = float(input("ingresar número: "))

contador = 0

for i in range(len(vec_num)):
   if vec_num[i] > 100:
       contador += 1

print("Cantidad de números mayores a 100: ", contador)
