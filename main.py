#! /usr/bin/python

__author__ = "Dj_System"
__date__ = "$09/07/2022 19:53:00 $"

from pygame.locals import *
from assets import *
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Flappy Bird')
    background = Item(window_width, background_height, 'background')
    logo = Item(logo_width, 50, 'logo')
    logo.update(((window_width - logo_width) / 2, 100))
    punctuation = Item(punctuation_width, 150, 'score')
    punctuation.update(((window_width - punctuation_width) / 2, 100))
    restart = Item(restart_width, 50, 'restart')
    restart.update(((window_width - restart_width) / 2, 275))
    flappy = Game()
    while True:
        background.show()
        if not flappy.collision:
            flappy.bird.fly(flappy.starting)
            flappy.ground.move()
        if not flappy.starting:
            logo.show()
        else:
            flappy.pipe1.update((flappy.column1.posX, flappy.column1.posY))
            flappy.pipe2.update((flappy.column1.posX, flappy.column1.posY - pipe_distanceY - pipe_height))
            flappy.pipe3.update((flappy.column2.posX, flappy.column2.posY))
            flappy.pipe4.update((flappy.column2.posX, flappy.column2.posY - pipe_distanceY - pipe_height))
            flappy.column1.draw(window)
            flappy.column2.draw(window)
            if not flappy.collision:
                flappy.column1.move(0)
                flappy.column2.move(flappy.column1.posX)
                if flappy.column1.posX + pipe_width == flappy.bird.posX or \
                        flappy.column2.posX + pipe_width == flappy.bird.posX:
                    flappy.punctuation += 1
                flappy.show_punctuation()
            else:
                flappy.bird.stop()
                punctuation.show()
                restart.show()
            flappy.ground.rect.left = flappy.bird.posX
            for pipe in flappy.column1.sprites():
                if flappy.bird.rect.colliderect(pipe.rect):
                    flappy.collision = True
                    break
            for pipe in flappy.column2.sprites():
                if flappy.bird.rect.colliderect(pipe.rect):
                    flappy.collision = True
                    break
            if flappy.bird.rect.colliderect(flappy.ground.rect):
                flappy.collision = True
        flappy.ground.show()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                flappy.bird.flying = True
                flappy.bird.down_time = 0
                flappy.accumulator += 1
                if flappy.accumulator == 1:
                    flappy.bird.rotated = True
                    flappy.starting = True
                else:
                    flappy.bird.rotated = False
                if flappy.collision:
                    if restart.posX < pygame.mouse.get_pos()[0] < restart.posX + restart.width and \
                            restart.posY < pygame.mouse.get_pos()[1] < restart.posY + restart.height:
                        flappy = Game()
                break
        pygame.display.update()
        pygame.time.Clock().tick(40)


if __name__ == "__main__":
    main()
