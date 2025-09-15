import funcion

edad = int(input("Ingrese su edad: "))

if funcion.verificar_acceso(edad):
    print("Acceso permitido: eres mayor de edad.")
else:
    print("Acceso denegado: eres menor de edad.")