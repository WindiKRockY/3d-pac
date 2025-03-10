import math 

#Розширення
WIDTH = 1200
HEIGHT = 800
PENTA_HEIGHT = 5 * HEIGHT
DOUBLE_HEIGHT = 2 * HEIGHT

#Кадри
FPS = 60
FPS_POS = (WIDTH - 60 ,10)

#Розмір 
TILE = 100

#Половинки
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

#Кольори
GRAY = (128, 128, 128) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
RED = (220,0,0)
GREEN = (0,220,0)
PURPLE = (120,0,120)
SKY_BLUE = (0,186,255)
YELLOW = (220,220,0)
SANDY = (244,164,96)
DARKBROWN = (97,61,25)
DARKORANGE = (255,140,0)

#Позиція
player_pos = (HALF_WIDTH // 2 , HALF_HEIGHT - 50)
player_angle = 0
player_speed = 2

#Зона бачення
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

#Міні-карта
MINI_MAP_SCALE = 5
MINI_MAP_RES = (WIDTH // MINI_MAP_SCALE, HEIGHT // MINI_MAP_SCALE )
MAP_SCALE = 2 * MINI_MAP_SCALE 
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0,HEIGHT - HEIGHT // MINI_MAP_SCALE )

#Налаштування текстур(1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2

#Позиція спрайтів
DOUBLE_PI = 2 * math.pi
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS