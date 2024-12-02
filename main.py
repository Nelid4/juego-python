import pygame
import constantes
from personaje import Personaje


pygame.init()#inicio pygame

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))#establece tamaño de la ventana
jugador_imagen = pygame.image.load("recursos/img/jugador/run1.png")
jugador = Personaje(100,500, jugador_imagen)#donde aprece el personaje inicialmente

pygame.display.set_caption("Mi primer juego")

# variables de movimiento del juego
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

reloj = pygame.time.Clock()#controla frame rate, velocidad de movimiento

corriendo = True
while corriendo:

    ventana.fill(constantes.COLOR_FONDO)#color del fondo
    eje_x = 0
    eje_y = 0

    if mover_derecha == True:#definiendo pixel por movimiento
        eje_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        eje_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        eje_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        eje_y = constantes.VELOCIDAD

    jugador.movimiento(eje_x, eje_y)#mover al personaje

    reloj.tick(constantes.FPS) #defino cuadros por segundo
    jugador.dibujar(ventana) #dibuja el personaje

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:#evento para que se mantenga la ventana(registra exit)
            corriendo = False

        if event.type == pygame.KEYDOWN:#escuchando eventos WASD
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_d:
                mover_derecha = True

        if event.type == pygame.KEYUP:
            mover_abajo = False
            mover_derecha = False
            mover_izquierda = False
            mover_arriba = False


    pygame.display.update()#indispensabe, actualiza

pygame.quit()