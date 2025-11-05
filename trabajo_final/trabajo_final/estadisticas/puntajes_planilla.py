      # crea dicc de puntajes
def generar_plantilla_puntaje(config):
    puntajes = {}
    for i in range(1, 11):
        puntajes[i] = None
    return puntajes

        # muestra la tabla de puntajes
def tabla_puntajes_tematica(puntajes, config):
   
    especiales_orden = ['Escalera', 'Full', 'Poker', 'Generala']
    
    print('\n' + '-'*40)
    print(f'PLANTILLA DE PUNTAJES ({config["tema"].upper()})') 
    print('-'*40)
    
    puntaje_total = 0
    
   # muestra las categorias del 1 al 6 sin las especiales
    for item in config['categorias_tematicas']:
        nombre = f"[{item['nombre']}]"
        puntos = puntajes[item['valor']]

        if puntos is not None:
            valor_mostrar = str(puntos)
            puntaje_total += puntos
        else:
            valor_mostrar = '-'
            
        print(f"{nombre:<15} : {valor_mostrar}")
            
    print('-'*40)
    
           # muestra categorias especiales
    for i, nombre_clave in enumerate(especiales_orden):
        indice = i + 7
        # muestra las relgas de puntaje
        puntos_regla = config['reglas_puntaje_especial'][nombre_clave]
        
        nombre_display = f"[{nombre_clave} ({puntos_regla})]"
        puntos = puntajes[indice]
        
        if puntos is not None:
            valor_mostrar = str(puntos)
            puntaje_total += puntos
        else:
            valor_mostrar = '-'
            
        print(f"{nombre_display:<15} : {valor_mostrar}")
            
    print('-'*40)
    print(f"PUNTAJE TOTAL: {puntaje_total}\n")
    
    return puntaje_total