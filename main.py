import pygame
from settings import * #імпортування папки "ssettings.py"
from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from interaction import Interaction

import math


pygame.init()

win = pygame.display.set_mode((WIDTH,HEIGHT))
win_map = pygame.Surface((MINI_MAP_RES))

sprites = Sprites()

clock = pygame.time.Clock() 

pygame.mouse.set_visible(False)
player = Player(sprites)
drawing = Drawing(win,win_map)
interaction = Interaction(player, sprites, drawing)

run = True
while run:
    #Обробка подій на екрані 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    player.movement()
    
    win.fill(BLACK)
    
    drawing.background(player.angle)
    walls = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects ])
    drawing.fps(clock)
    drawing.mini_map(player)
    
        
    pygame.display.flip()
    clock.tick()