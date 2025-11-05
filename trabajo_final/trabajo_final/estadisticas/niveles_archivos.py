import json
import csv
import os

def cargar_configuracion_nivel(archivo_json="niveles.json", nivel=1):
    f = open(archivo_json, 'r', encoding='utf-8')
    data = json.load(f)
    f.close() 
#ingresa a nivel del json
    for config in data: 
        if config["nivel"] == nivel:
            return config
    return None

# guardado de nombre y nivel del jugador
def guardar_puntaje_csv(nombre_jugador, puntaje_total, archivo_csv="puntajes_generala.csv"):
    
    es_nuevo_archivo = not os.path.exists(archivo_csv)
    
    # Abre el archivo para agregar contenido
    f = open(archivo_csv, 'a', encoding='utf-8', newline='') 
    
    escritor_csv = csv.writer(f)
    
    # Uso de writerows para escribir filas (sustituyendo .writerow)
    if es_nuevo_archivo:
        # Escribe el encabezado
        escritor_csv.writerows([['Nombre', 'Puntaje']]) 
    
    # Escribe los datos del jugador
    escritor_csv.writerows([[nombre_jugador, puntaje_total]])
    
    f.close()

    print(f"\nPuntaje de {nombre_jugador} ({puntaje_total}) guardado en '{archivo_csv}'")