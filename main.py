#! /usr/bin/python

__author__ = "Dj_System"
__date__ = "$// :: $"

from classes import *

cero = Numero(((186, 80), (177, 80), (177, 130), (207, 130), (207, 80), (186, 80), (186, 122), (198, 122), 
                  (198, 88), (186, 88)), 
                  ((189, 77), (174, 77), (174, 133), (210, 133), (210, 77), (189, 77), (189, 119), (195, 119), 
				       (195, 91), (189, 91)))
uno = Numero(((184.5, 80), (184.5, 95), (189.5, 95), (189.5, 130), (199.5, 130), (199.5, 80)), 
                 ((181.5, 77), (181.5, 98), (186.5, 95), (186.5, 133), (202.5, 133), (202.5, 77)))
#dos = Numero()
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


def inicio():
    global cont, puntuacion, choque, empieza, ave, piso, columna1, columna2, tubo1, tubo2, tubo3, tubo4
    cont = 0
    puntuacion = 0
    choque = False
    empieza = False
    ave = Ave()
    piso = Piso()
    columna1 = ColumnaTubos(0)
    columna2 = ColumnaTubos(columna1.posX)
    tubo1 = Tubo(False)
    tubo2 = Tubo(True)
    tubo3 = Tubo(False)
    tubo4 = Tubo(True)
    columna1.add(tubo1, tubo2)
    columna2.add(tubo3, tubo4)


def dibuja_numero(num):
    if num == 0:
        cero.dibujar()
    elif num == 1:
        uno.dibujar()
    elif num == 2:
        pygame.draw.rect(ventana, (0, 0, 0), (173, 98, 35, 55))
        pygame.draw.rect(ventana, (255, 255, 255), (175, 100, 30, 50))
        pygame.draw.rect(ventana, (0, 0, 0), (173, 115, 20, 5))
        pygame.draw.rect(ventana, (0, 0, 0), (188, 132, 20, 5))
    elif num == 3:
        pygame.draw.rect(ventana, (0, 0, 0), (173, 98, 35, 55))
        pygame.draw.rect(ventana, (255, 255, 255), (175, 100, 30, 50))
        pygame.draw.rect(ventana, (0, 0, 0), (173, 115, 20, 5))
        pygame.draw.rect(ventana, (0, 0, 0), (173, 132, 20, 5))
    elif num == 4:
        cuatro.dibujar()
    elif num == 5:
        pygame.draw.rect(ventana, (0, 0, 0), (173, 98, 35, 55))
        pygame.draw.rect(ventana, (255, 255, 255), (175, 100, 30, 50))
        pygame.draw.rect(ventana, (0, 0, 0), (188, 115, 20, 5))
        pygame.draw.rect(ventana, (0, 0, 0), (173, 132, 20, 5))
    elif num == 6:
        pygame.draw.rect(ventana, (0, 0, 0), (173, 98, 35, 55))
        pygame.draw.rect(ventana, (255, 255, 255), (175, 100, 30, 50))
        pygame.draw.rect(ventana, (0, 0, 0), (188, 115, 20, 5))
        pygame.draw.rect(ventana, (0, 0, 0), (187, 132, 5, 5))
    elif num == 7:
        siete.dibujar()
    elif num == 8:
        pygame.draw.rect(ventana, (0, 0, 0), (173, 98, 35, 55))
        pygame.draw.rect(ventana, (255, 255, 255), (175, 100, 30, 50))
        pygame.draw.rect(ventana, (0, 0, 0), (187, 115, 5, 5))
        pygame.draw.rect(ventana, (0, 0, 0), (187, 132, 5, 5))
    elif num == 9:
        pygame.draw.rect(ventana, (0, 0, 0), (173, 98, 35, 55))
        pygame.draw.rect(ventana, (255, 255, 255), (175, 100, 30, 50))
        pygame.draw.rect(ventana, (0, 0, 0), (187, 115, 5, 5))
        pygame.draw.rect(ventana, (0, 0, 0), (173, 132, 20, 5))


def mostrar_puntuacion(score):
    if score > 0:
        while score > 0:
            dibuja_numero(score % 10)
            score /= 10
    else:
        dibuja_numero(score)


def main():
    global cont, puntuacion, choque, empieza, ave, piso, columna1, columna2, tubo1, tubo2, tubo3, tubo4
    pygame.init()
    pygame.display.set_caption('Flappy Bird')    
    fondo = Item(ancho_ventana, alto_fondo, 'background')
    logo = Item(ancho_logo, 50, 'logo')
    logo.update(((ancho_ventana - ancho_logo) / 2, 100))
    puntaje = Item(ancho_puntaje, 150, 'score')
    puntaje.update(((ancho_ventana - ancho_puntaje) / 2, 100))
    reinicio = Item(ancho_reinicio, 50, 'restart')
    reinicio.update(((ancho_ventana - ancho_reinicio) / 2, 275))
    inicio()
    while True:
        fondo.dibujar()
        if not choque:
            ave.volar(empieza)
            piso.mover()
        if not empieza:
            logo.dibujar()
        else:
            tubo1.update((columna1.posX, columna1.posY))
            tubo2.update((columna1.posX, columna1.posY - distanciaY_tubos - alto_tubo))
            tubo3.update((columna2.posX, columna2.posY))
            tubo4.update((columna2.posX, columna2.posY - distanciaY_tubos - alto_tubo))
            columna1.draw(ventana)
            columna2.draw(ventana)
            if not choque:
                columna1.mover(0)
                columna2.mover(columna1.posX)
                if columna1.posX + ancho_tubo == ave.posX or columna2.posX + ancho_tubo == ave.posX:
                    puntuacion += 1
                mostrar_puntuacion(puntuacion)
            else:
                ave.detener()
                puntaje.dibujar()
                reinicio.dibujar()
            piso.rect.left = ave.posX
            for tubo in columna1.sprites():
                if ave.rect.colliderect(tubo.rect):
                    choque = True
                    break
            for tubo in columna2.sprites():
                if ave.rect.colliderect(tubo.rect):
                    choque = True
                    break
            if ave.rect.colliderect(piso.rect):
                choque = True
        piso.dibujar()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ave.eleva = True
                ave.tiempo_bajada = 0
                cont += 1
                if cont == 1:
                    ave.rota = True
                    empieza = True
                else:
                    ave.rota = False
                if choque:
                    if (reinicio.posX < pygame.mouse.get_pos()[0] < reinicio.posX + reinicio.ancho and
                            reinicio.posY < pygame.mouse.get_pos()[1] < reinicio.posY + reinicio.alto):
                        inicio()
                break
        pygame.display.update()
        pygame.time.Clock().tick(40)

if __name__ == "__main__":
    main()
