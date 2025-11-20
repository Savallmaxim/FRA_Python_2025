import pygame
#iniciar pygame
pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
FONDO = (217, 186, 85)
ANCHO = 800
ALTO = 600

fuente = pygame.font.SysFont(None, 60)
#funcion mostrar pantalla

def mostrar_pantalla(texto):
    pantalla.fill(BLANCO)
    texto_render = fuente.render(texto, True, NEGRO)
    pantalla.blit(texto_render, (ANCHO / 2 - texto_render.get_with() / 2, 50))

#declaramos botones
btn_play_img = pygame.transform.scale(pygame.image.load("play.png", (120, 80)))
btn_opciones_img = pygame.transform.scale(pygame.image.load("opciones.png", (120, 80)))
btn_salir_img = pygame.transform.scale(pygame.image.load("salir.png", (120, 80)))
#posicionar botones para detectar clicks
btn_play_rect = btn_play_img.get_rect(topleft=(ANCHO /2 - btn_play_img.get_width() /2, 80))
btn_opciones_rect = btn_opciones_img.get_rect(topleft=(ANCHO /2 - btn_opciones_img.get_width() /2, 80))
btn_salir_rect = btn_salir_img.get_rect(topleft=(ANCHO /2 - btn_salir_img.get_width() /2, 80))
#creamos la ventana principal
pantalla = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Generala Pokemon")

#bucle principal
while True:
    #gestionar eventos(por ejemplo. cerrar la ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if estado == "menu":
            if btn_play_rect.collidepoint(evento.pos):
                estado = "jugar"
            elif btn_opciones_rect.collidepoint(evento.pos):
                estado = "opciones"
            elif btn_salir_rect.collidepoint(evento.pos):
                estado = "salir"
            
            if estado == "menu":
                pantalla.fill(NEGRO)
                pantalla.blit(btn_play_img, btn_play_rect.topleft)
                pantalla.blit(btn_opciones_img, btn_opciones_rect.topleft)
                pantalla.blit(btn_salir_img, btn_salir_rect.topleft)
                
            elif estado == "jugar":
                mostrar_pantalla("pantalla de jugar")
            elif estado == "creditos":
                pass

    #dibujar pantalla(rellenamos de un color)
    pantalla.fill(FONDO)

    #actualizar pantalla
    pygame.display.update()