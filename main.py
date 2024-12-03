import pygame
import constantes
from personaje import Personaje


pygame.init()#inicio pygame

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))#establece tamaño de la ventana


pygame.display.set_caption("Mi primer juego")

animaciones = []
for i in range(4):
    jugador_imagen = pygame.image.load(f"recursos/img/jugador/run{i}.png")
    animaciones.append(jugador_imagen)

jugador = Personaje(100,500, animaciones)#donde aprece el personaje inicialmente
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
    
    jugador.update()

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