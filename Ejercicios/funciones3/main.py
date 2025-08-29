import funtri

print("----CALCULADORA DE AREA DE UN TRIANGULO----")
b = float(input("INGRESE LA BASE DE TU TRIANGULO: "))
h = float(input("INGRESE LA ALTURA DE TU TRIANGULO: "))

resultado_area = funtri.area_triangulo(b, h)

print(f"El area de tu triangulo es: {resultado_area}")