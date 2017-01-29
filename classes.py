import os
import sys
from random import randint

import pygame
from pygame.locals import *

ancho_logo, ancho_puntaje, ancho_reinicio, ancho_tubo, ancho_ventana = 200, 100, 150, 48, 384
alto_fondo, alto_tubo, alto_tubo_min, alto_ventana = 425, 300, 50, 525
COLOR_BLANCO, COLOR_NEGRO = (255, 255, 255), (0, 0, 0)
distanciaX_tubos, distanciaY_tubos = (ancho_ventana - ancho_tubo)/2, 100
RUTA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
velocidad = 3
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))


class ColumnaTubos(pygame.sprite.Group):
    def __init__(self, separacion):
        pygame.sprite.Group.__init__(self)
        if separacion > 0:
            self.posX = ancho_tubo + distanciaX_tubos + separacion
        else:
            self.posX = 2*ancho_ventana
        self.posY = randint(alto_tubo_min + distanciaY_tubos, alto_fondo - alto_tubo_min)

    def mover(self, separacion):
        self.posX -= velocidad
        if self.posX < -1 * ancho_tubo:
            if separacion > 0:
                self.posX = ancho_tubo + distanciaX_tubos + separacion
            else:
                self.posX = ancho_ventana
            self.posY = randint(alto_tubo_min + distanciaY_tubos, alto_fondo - alto_tubo_min)


class Item(pygame.sprite.Sprite):
    def __init__(self, ancho, alto, ruta_imagen):
        pygame.sprite.Sprite.__init__(self)
        self.ancho = ancho
        self.alto = alto
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(RUTA_PROYECTO, 'img/' + ruta_imagen + '.png')).convert_alpha(), (self.ancho, self.alto))
        self.rect = self.image.get_rect()

    def dibujar(self):
        ventana.blit(self.image, self.rect)

    def update(self, posicion):
        self.posX = posicion[0]
        self.posY = posicion[1]
        self.rect.left = self.posX
        self.rect.top = self.posY


class Numero():
    def __init__(self, coordenadas_blanco, coordenadas_negro):
        self.coordenadas_blanco = coordenadas_blanco
        self.coordenadas_negro = coordenadas_negro

    def dibujar(self):
        pygame.draw.polygon(ventana, COLOR_NEGRO, self.coordenadas_negro)
        pygame.draw.polygon(ventana, COLOR_BLANCO, self.coordenadas_blanco)


#Nice numbers
cero = Numero(((186, 50), (177, 50), (177, 100), (207, 100), (207, 50), (186, 50), (186, 92), (198, 92), 
                  (198, 58), (186, 58)), 
                  ((189, 47), (174, 47), (174, 103), (210, 103), (210, 47), (189, 47), (189, 89), (195, 89), 
				       (195, 61), (189, 61)))
uno = Numero(((184.5, 50), (184.5, 65), (189.5, 65), (189.5, 100), (199.5, 100), (199.5, 50)), 
                 ((181.5, 47), (181.5, 68), (186.5, 68), (186.5, 103), (202.5, 103), (202.5, 47)))
dos = Numero(((177, 50), (177, 65), (189.5, 65), (189.5, 70), (177, 70), (177, 100), (207, 100), 
                  (207, 85), (194.5, 85), (194.5, 80), (207, 80), (207, 50)), 
                  ((174, 47), (174, 68), (186.5, 68), (186.5, 72), (174, 72), (174, 103), (210, 103), (210, 89), 
				       (195, 61), (189, 61)))
#tres = Numero()
cuatro = Numero(((175, 100), (187, 100), (187, 120), (192, 120), (192, 100), (205, 100), (205, 150), (192, 150), 
                    (192, 137), (175, 137)), 
                    ((173, 98), (208, 98), (208, 153), (190, 153), (190, 140), (173, 140)))
#cinco = Numero()
#seis = Numero()
siete = Numero(((175, 100), (205, 100), (205, 150), (192, 150), (192, 117), (187, 117), (187, 127), (175, 127)), 
                   ((173, 98), (208, 98), (208, 153), (190, 153), (190, 130), (173, 130)))
#ocho = Numero()
#nueve = Numero()


class Ave(Item):
    def __init__(self):
        Item.__init__(self, 45, 33, 'bird2')
        self.angulo_inicial = 22.5
        self.angulo_final = 270
        self.arriba = True
        self.eleva = False
        self.estado = 1
        self.posX = ancho_ventana / 4 + 48
        self.posY = 225
        self.posY_inicial = self.posY
        self.rota = False
        self.tiempo_bajada = 0
        self.tiempo_aleteo = 6
        self.velocidad = 0.5
        self.aux_estado = self.tiempo_aleteo
        self.imagenes = {}
        self.imagenes_rotadas = {}
        for i in range(1, 4):
            imagen = pygame.transform.scale(pygame.image.load(os.path.join(RUTA_PROYECTO, 'img/bird' + str(i) + '.png')).convert_alpha(), (self.ancho, self.alto))
            self.imagenes[self.tiempo_aleteo * i] = imagen
            self.imagenes_rotadas[self.tiempo_aleteo * i] = pygame.transform.rotate(imagen, self.angulo_inicial)

    def volar(self, start):
        if self.rota:
            self.imagenes = self.imagenes_rotadas
            ave_rotada = self.imagenes[self.tiempo_aleteo]
            self.rect.width = ave_rotada.get_rect().width
            self.rect.height = ave_rotada.get_rect().height
        if not start:
            if self.arriba:
                if self.posY < self.posY_inicial + 6:
                    self.posY += self.velocidad
                else:
                    self.arriba = False
            else:
                if self.posY > self.posY_inicial - 3:
                    self.posY -= self.velocidad
                else:
                    self.arriba = True
        else:
            if self.eleva:
                self.posY -= 35  # 33
                self.eleva = False
            else:
                self.tiempo_bajada += 0.75
                self.posY += 0.25 * self.tiempo_bajada
        self.update((self.posX, self.posY))
        if self.estado % self.tiempo_aleteo == 0:
            ventana.blit(self.imagenes[self.estado], self.rect)
            self.aux_estado = self.estado
        else:
            ventana.blit(self.imagenes[self.aux_estado], self.rect)
        if self.estado != self.tiempo_aleteo * len(self.imagenes):
            self.estado += 1
        else:
            self.estado = 1

    def detener(self):
        ave_rotada = pygame.transform.rotate(self.image, self.angulo_final)
        self.rect.top = alto_fondo - self.ancho
        ventana.blit(ave_rotada, self.rect)


class Piso(Item):
    def __init__(self):
        Item.__init__(self, 25, alto_ventana - alto_fondo, 'ground')
        self.posX = 2 * ancho_ventana

    def dibujar(self):
        for i in range(1, self.posX / self.ancho + 2):
            self.rect.left, self.rect.top = self.posX - self.ancho * i, alto_fondo
            ventana.blit(self.image, self.rect)

    def mover(self):
        self.posX -= velocidad
        if self.posX < ancho_ventana:
            self.posX = 2 * ancho_ventana


class Tubo(Item):
    def __init__(self, invertido):
        Item.__init__(self, ancho_tubo, alto_tubo, 'pipe')
        if invertido:
            self.image = pygame.transform.flip(self.image, False, True)
