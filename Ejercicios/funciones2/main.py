import funcion

a = int(input("Ingrese un numero: "))
b = int(input("ingrese un segundo numero: "))

resultado_suma, resultado_resta, resultado_multi = funcion.operaciones(a,b)

print(f"La Suma de estos dos numeros da: {resultado_suma}")
print(f"La resta de estos dos numeros da: {resultado_resta}")
print(f"La multiplicacion de estos dos numeros da: {resultado_multi}")