#Cargar un array de 6 enteros y mostrarlo invertido, 
#es decir, desde el último al primero.

vec_num = [0] * 6

for i in range(len(vec_num)):
    vec_num[i] = int(input(f"ingresar número: "))

print("Números invertidos: ")

for i in range(len(vec_num) -1, -1, -1):
    print(vec_num[i])