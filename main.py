# juego_principal.py

import random
# 1. IMPORTS REEMPLAZADOS: Ahora importamos las funciones de los módulos de niveles
from niveles_y_archivos import cargar_configuracion_nivel, guardar_puntaje_csv
from plantilla_puntaje import generar_plantilla_puntaje, tabla_puntajes_tematica


def tirar_dado(dados):
    while len(dados) < 5:
        dado = random.randint(1, 6)
        dados.append(dado)


# 2. FUNCIÓN posibles_jugadas (Mantenida o Reemplazada con Simulación)
# Esta función es necesaria para que el juego continúe con el flujo de categorías 1-10.
def posibles_jugadas(dados, puntajes):
    """
    Función de simulación para asignar una categoría y puntaje.
    En tu código final, esta función debe calcular el puntaje real.
    """
    # Simulación simple: elije la primera categoría disponible (1-10)
    for cat in range(1, 11):
        if puntajes.get(cat) is None:  # Uso de .get() o acceso directo, dependiendo del archivo plantilla_puntaje
            # Puntos simulados: 5 si es categoría 1-6, 20 si es especial
            puntos_simulados = 20
            if cat <= 6:
                # Simulación de puntaje basado en el primer dado
                puntos_simulados = dados[0] * cat 
            return cat, puntos_simulados
    return 1, 0 # Fallback si no quedan categorías


def ronda():
    # 3. CARGAR CONFIGURACIÓN DEL NIVEL (Inicio de la partida)
    config = cargar_configuracion_nivel(nivel=1)
    if config is None:
        print("El juego no puede iniciar: Error de carga de nivel. Asegúrate de tener 'niveles.json'.")
        return

    # 4. INICIALIZACIÓN DE PUNTAJES DINÁMICA
    puntajes = generar_plantilla_puntaje(config)

    cant_categorias = 10
    turnos = 3

    while cant_categorias > 0:
        print(f'\n--- INICIO DE RONDA. Categorías restantes: {cant_categorias} ---')
        dados = []  # reinicia los dados para cada ronda

        for turno in range(turnos):
            print(f'\n<<< TURNO JUGADOR - TIRO {turno + 1} de {turnos} >>>')
            print('-' * 40)
            print('Posición: (1\t) | (2\t) | (3\t) | (4\t) | (5\t) |')
            print('         ',('-' * 39), '|')

            tirar_dado(dados)
            print(f'Valor: \t {dados[0]:^5}\t  | {dados[1]:^2} \t  | {dados[2]:^2} \t  | {dados[3]:^2} \t  | {dados[4]:^2} \t  |')

            # 🔹 Solo permitir elegir dados en los dos primeros tiros
            if turno < 2: # Se cambió de `turno < 3` a `turno < 2` para reflejar "dos primeros tiros" (0 y 1)
                desea_conservar = input(
                    'Ingrese las posiciones de los dados a conservar (1-5), separadas por coma, o ENTER para tirar todos: '
                ).strip()

                if desea_conservar == "":
                    dados = []  # tirar todos
                else:
                    posiciones = desea_conservar.split(",")
                    dados_conservados = []

                    for pos in posiciones:
                        if pos.isdigit():
                            indice = int(pos) - 1
                            if 0 <= indice < len(dados):
                                dados_conservados.append(dados[indice])
                            else:
                                print('Posición fuera de rango (1–5).')
                        else:
                            print('Ingrese solo números válidos, por ejemplo: 1,3,5')
                            dados_conservados = []
                            break

                    dados = dados_conservados
                    print(f'DADOS CONSERVADOS: {dados}')
                    if len(dados) == 5:
                        print('Has conservado los 5 dados')
                        break
            
            # Si es el tercer tiro (turno 2), se termina la fase de tiradas
            if turno == 2:
                break

        categoria, puntos = posibles_jugadas(dados, puntajes)
        puntajes[categoria] = puntos
        
        # 5. MOSTRAR TABLA TEMÁTICA y CALCULAR TOTAL
        puntaje_total_actual = tabla_puntajes_tematica(puntajes, config)
        cant_categorias -= 1

    # -------------------------------------------------------------
    # IV. Guardado del Archivo al Finalizar
    # -------------------------------------------------------------
    print('\n\n=== ¡FIN DEL JUEGO! ===')
    print(f"🏆 Tu puntaje final es: **{puntaje_total_actual}** puntos.")

    # Pedir nombre del jugador y guardar en CSV
    nombre_jugador = input("Introduce tu nombre para guardar tu puntaje: ").strip()

    if nombre_jugador != "": # Verificamos si la cadena no está vacía
        guardar_puntaje_csv(nombre_jugador, puntaje_total_actual)
    else:
        print("El puntaje no se guardó. Debes ingresar un nombre.")


# Ejecución del juego
if __name__ == '__main__':
    ronda()