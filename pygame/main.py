import pygame
pygame.init()

ancho = 640
alto = 400

#crea ventana de 400x300 px
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Generala Pokemon")

reloj= pygame.time.Clock()

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    #color de ventana
    screen.fill((255, 255, 255))
    pygame.display.flip()

    #tiempo de ventana
    reloj.tick(60)

pygame.quit()