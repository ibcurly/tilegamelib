
from tilegamelib.screen import Screen
from tilegamelib.frame import Frame
from tilegamelib.tile_factory import TileFactory
from tilegamelib.tiled_map import TiledMap
from tilegamelib.vector import Vector
from pygame import Rect
import pygame
import time


if __name__ == '__main__':
    fruitmap = """################
#..aa..bb..cc..#
#..aa..bb..cc..#
#cc..dd..ee..ff#
#cc..dd..ee..ff#
#..bb..cc..ee..#
#..bb..cc..ee..#
#ee..ff..gg..hh#
#ee..ff..gg..hh#
#..aa..bb..cc..#
#..aa..bb..cc..#
#cc..dd..ee..ff#
#cc..dd..ee..ff#
################"""

    screen = Screen(Vector(800,550), 'data/background.png')
    frame = Frame(screen, Rect(64, 64, 320, 320))
    tile_factory = TileFactory('data/tiles.conf')
    tm = TiledMap(frame, tile_factory)

    tm.set_map(fruitmap)
    tm.draw()
    pygame.display.update()
    for i in range(0, 132, 2) + range(132, 0, -2):
        tm.offset = Vector(i, i)
        screen.clear()
        tm.draw()
        pygame.display.update()
        time.sleep(0.05)