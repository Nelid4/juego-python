import pygame
import constantes

class Personaje():
    def __init__(self, x, y, imagen):#define tamaño y forma del personaje
        self.imagen = imagen
        self.forma = pygame.Rect(0,0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)

    def dibujar(self, interfaz):#"dibuja" el personaje con color
        interfaz.blit(self.imagen, self.forma)
        # pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma) esto dibuja el rectangulo

    def movimiento(self, eje_x, eje_y):#define el movimiento WASD, a aprtir d donde esta + lo q se debe mover
        self.forma.x += eje_x
        self.forma.y += eje_y
