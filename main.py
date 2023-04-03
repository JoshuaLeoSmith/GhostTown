import pygame
import Constants
from Sprites.TileSprite import TileSprite
from Sprites.SpriteMapper import TileMapper
from pygame.locals import *
import pygame, sys, time, random
import numpy as np
import logging




stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    handlers=[logging.FileHandler("my_log.log", mode='w'),
                              stream_handler])



pygame.init()
scrn = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
display = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
ground = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))



f = open('assets/gameMapMedium.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()



view = [0,0]
zoom = 1.0
grass_tile = pygame.transform.scale(pygame.image.load('assets/tiles/grassTileReal2.png').convert_alpha(), (100,100))
cactus_tile = pygame.transform.scale(pygame.image.load('assets/tiles/cactus.png').convert_alpha(), (110,100))



def get_view():

    return map_data[view[0]: view[0] + 100][view[1]: view[1] + 100]



def generate_tiles():
    grass_tile_zoomed = pygame.transform.scale(grass_tile, (grass_tile.get_size()[0] * zoom, grass_tile.get_size()[1] * zoom))
    cactus_tile_zoomed = pygame.transform.scale(cactus_tile, (cactus_tile.get_size()[0] * zoom, cactus_tile.get_size()[1] * zoom))
    mouseX, mouseY = pygame.mouse.get_pos()

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            # if tile == 0:
            #     ground.blit(grass_tile_zoomed, (zoom * (x * 50 - y * 50) + (750 + view[0]),
            #                                     zoom * (x * 25 + y * 25) + (300 + view[1])))
            # elif tile == 1:
            #     ground.blit(cactus_tile_zoomed, (zoom * (x * 50 - y * 50) + (750 + view[0]),
            #                                      zoom * (x * 25 + y * 25) + (320 + view[1])))
            if tile == 0:
                ground.blit(grass_tile_zoomed, (zoom * ((x * 50 - y * 50) + (750 + view[0])),
                                                zoom * ((x * 25 + y * 25) + (300 + view[1]))))
            elif tile == 1:
                ground.blit(cactus_tile_zoomed, (zoom * ((x * 50 - y * 50) + (750 + view[0])),
                                                 zoom * ((x * 25 + y * 25) + (320 + view[1]))))


    # zoomed_ground = pygame.transform.scale(ground, (Constants.WINDOW_WIDTH * zoom, Constants.WINDOW_HEIGHT * zoom))
    # display.blit(zoomed_ground, (0,0))
    display.blit(ground, (0,0))



def get_resolution():

    return Constants.DEFAULT_DISPLAY[0] * zoom, Constants.DEFAULT_DISPLAY[1] * zoom

generate_tiles()
pygame.display.update()
while(True):
    display.fill((0, 0, 0))
    ground.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEWHEEL:
            if event.y > 0:
                logging.info("Zooming in")
                zoom += 0.05
                if zoom >= 1.25:
                    zoom = 1.25
            elif event.y < 0:
                logging.info("Zooming out")
                zoom -= 0.05
                if zoom <= 0.75:
                    zoom = 0.75
            logging.info("Zoom = " + str(zoom))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        view[0] += 5
    if keys[pygame.K_d]:
        view[0] -= 5
    if keys[pygame.K_w]:
        view[1] += 5
    if keys[pygame.K_s]:
        view[1] -= 5



    generate_tiles()

    scrn.blit(display, (0,0))
    pygame.display.update()


