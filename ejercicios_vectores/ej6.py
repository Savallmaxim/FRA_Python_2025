#Cargar un array de 7 números enteros. 
#Determinar el valor más alto y en qué posición 
#se encuentra.

vec_num = [0] * 7

for i in range(len(vec_num)):
    vec_num[i] = int(input(f"ingresar número {i+1} : "))

maximo = vec_num[0]
posicion = 0

for i in range(1, len(vec_num)):
    if vec_num[i] > maximo:
        maximo = vec_num[i]
        posicion = i+1

print(f"El valor más alto es {maximo} y se encuentra en la posición {posicion}")

