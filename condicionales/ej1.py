# a partir del ingreso de la altura en centimetros de un jugador de baloncesto,
# el programa debera determinar la posicion del jugador en la cancha
# considerando los siguientes parametros
# -menos de 160cm: Base
# -entre 160cm y 179cm: Escolta
# -entre 180cm y 199cm: Alero
# -200cm o mas: ala-pivot o pivot

altura = int(input("ingrese su altura en cm: "))

if altura < 160:
    print("Altura Base")
elif altura >= 160 and altura <= 179:
    print("Altura Escolta")
elif altura >= 180 and altura <= 199:
    print("Altura Alero")
elif altura >= 200:
    print("Altura Pivot")