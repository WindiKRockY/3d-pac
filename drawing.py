import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map

pygame.init()

class Drawing():
    def __init__(self,win,win_map):
        self.win = win
        self.win_map = win_map
        self.font = pygame.font.SysFont('Arial',36 , bold= True)
        self.textures = { 1 :pygame.image.load('images/wall.png').convert(),
                        2 :pygame.image.load('images/ghost_wall.png').convert(),
                        'S' :pygame.image.load('images/sky.jpg').convert(),
                        'F' :pygame.image.load('images/floor.png').convert(),
                        'C':pygame.image.load("sCoins.png").convert(),
                         }
        
    def background(self,angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.win.blit(self.textures['S'] , (sky_offset, 0))
        self.win.blit(self.textures['S'] , (sky_offset - WIDTH, 0))
        self.win.blit(self.textures['S'] , (sky_offset + WIDTH, 0))
        # floor_offset = +10 * math.degrees(angle) % WIDTH
        # self.win.blit(self.textures['F'] , (floor_offset, HALF_HEIGHT))
        # self.win.blit(self.textures['F'] , (floor_offset - WIDTH, HALF_HEIGHT))
        # self.win.blit(self.textures['F'] , (floor_offset + WIDTH, HALF_HEIGHT))
        #self.win.blit(self.textures['F'], (0,HALF_HEIGHT,WIDTH,HALF_HEIGHT ))
        
        pygame.draw.rect(self.win, BLACK ,(0,HALF_HEIGHT,WIDTH,HALF_HEIGHT))
        
    def world(self,world_objects):
        for obj in sorted(world_objects , key= lambda n: n[0],reverse= True):
            if obj[0]:
                _, object , object_pos = obj
                self.win.blit(object , object_pos)
        
    def fps(self,clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps , 0 ,GRAY)
        self.win.blit(render , FPS_POS)
        
    def mini_map(self,player):
        self.win_map.fill(BLACK)
        map_x , map_y = player.x // MAP_SCALE , player.y //MAP_SCALE
        pygame.draw.line(self.win_map , WHITE , (map_x , map_y) , (map_x + 10 * math.cos(player.angle),
                                                                             map_y + 10 * math.sin(player.angle)))
        pygame.draw.circle(self.win_map, YELLOW, (int(map_x), int(map_y)) , 5 )
        for x , y in mini_map:
            pygame.draw.rect(self.win_map,BLUE, (x , y , MAP_TILE  ,MAP_TILE ))
        self.win.blit(self.win_map,MAP_POS)