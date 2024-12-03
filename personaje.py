import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):#define tamaño y forma del personaje
        self.animaciones = animaciones
        self.frame_index = 0
        self.updte_time = pygame.time.get_ticks()#almacena milisegundos desde que se inicio pygame

        self.imagen = animaciones[self.frame_index]
        self.forma = pygame.Rect(0,0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)
        self.flip = False #mientras sea flase, el jugador no voltea

    def dibujar(self, interfaz):#"dibuja" el personaje con color
        imagen_flip = pygame.transform.flip(self.imagen, self.flip,False)#mueve la imagen dependiendo de a donde va el personaje
        interfaz.blit(imagen_flip, self.forma)
        # pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma) esto dibuja el rectangulo

    def movimiento(self, eje_x, eje_y):#define el movimiento WASD, a aprtir d donde esta + lo q se debe mover
        self.forma.x += eje_x
        self.forma.y += eje_y

        if eje_x < 0:#flip para izquierda
            self.flip = True
        if eje_x > 0:#flip para derecha
            self.flip = False

    def update(self):
        cooldown_animacion = 300 #tiempo que tardara en cambiarse la imagen del personaje
        self.imagen = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.updte_time >= cooldown_animacion:
            self.frame_index += 1
            self.updte_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index =0
