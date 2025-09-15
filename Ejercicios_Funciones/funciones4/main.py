import funci

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

ordenados = funci.buscar_mayor(num1, num2, num3)

print("Los números ordenados de mayor a menor son:", ordenados)