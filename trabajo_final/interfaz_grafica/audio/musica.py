import pygame
import os

VOLUMEN = 0.03

# Obtiene la ruta absoluta del directorio raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Crea las rutas absolutas correctas
MUSICA_PRINCIPAL = os.path.join(BASE_DIR, "assets", "musica_pokemon.mp3")
EFECTO_CLICK = os.path.join(BASE_DIR, "assets", "pokemon_boton.wav")

VOLUMEN_MUSICA = VOLUMEN

def reproducir_musica(ruta, loop=True):
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
    pygame.mixer.music.play(-1 if loop else 0)

def detener_musica():
    pygame.mixer.music.stop()

def pausar_musica():
    pygame.mixer.music.pause()

def reanudar_musica():
    pygame.mixer.music.unpause()

def cambiar_volumen(valor):
    pygame.mixer.music.set_volume(valor)

def cargar_efecto(ruta):
    efecto = pygame.mixer.Sound(ruta)
    efecto.set_volume(VOLUMEN_MUSICA + 0.2)
    return efecto

def reproducir_efecto(efecto):
    efecto.play()