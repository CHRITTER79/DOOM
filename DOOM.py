from typing_extensions import Self
import pygame as pg
import sys
from settings import *

class Game:
    def __init__(Self):
     pg.init()
    Self.screen = pg.display.set_mode(RES)
    Self.clock = pg.time.Clock()

    def new_game(Self):
        pass

    def update(Self):
        pg.display.flip()
        Self.clock.tick(FPS)
        pg.display.set_caption(f'{Self.clock.get_fps() :.1f}')

    def draw(Self):
        Self.screen.fill('black')

    def check_events(Self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(Self):
        while True:
            Self.check_events()
            Self.update()
            Self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
