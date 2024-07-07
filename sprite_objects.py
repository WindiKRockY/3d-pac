import pygame
from settings import *
from collections import deque
from ray_casting import mapping
from numba.core import types
from numba.typed import Dict
from numba import int32


pygame.init()

class Sprites:
    def __init__(self):
        self.sprite_parameters = {
            'explosion' : {
                'sprite' : pygame.image.load('sprite/explosion/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift' : 0.1,
                'scale' : (0.6,0.6),
                'side' : 40,
                'animation' : deque(
                    [pygame.image.load(f'sprite/explosion/anim/{i}.png').convert_alpha() for i in range(11)]),
                'death_animation' : deque(
                    [pygame.image.load(f'sprite/explosion/anim/{i}.png').convert_alpha() for i in range(11)]),
                'is_dead' : None,
                'dead_shift' : 1.0,
                'animation_dist' : 800,
                'animation_speed' : 10,
                'blocked' : False,
                'flag' : 'decor',
                'obj_action' : []
            },
            'red_sprite': {
                'sprite': pygame.image.load('sprite/enemys/red_sprite.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6,0.6),
                'side' : 40,
                'animation': deque(
                    [pygame.image.load(f'sprite/enemys/red_sprite.png').convert_alpha() for i in range(1)]),
                'death_animation': deque([pygame.image.load(f'sprite/dead/animation/{i}.png')
                                          .convert_alpha() for i in range(4)]),
                'is_dead': None,
                'dead_shift': 1.0,
                'animation_dist': 800,
                'animation_speed': 10,
                'blocked': True,
                'flag' : 'npc',
                'obj_action' : []
            },
            'blue_sprite': {
                'sprite': pygame.image.load('sprite/enemys/blue_sprite.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6,0.6),
                'side' : 40,
                'animation': deque(
                    [pygame.image.load(f'sprite/enemys/red_sprite.png').convert_alpha() for i in range(1)]),
                'death_animation': deque([pygame.image.load(f'sprite/dead/animation/{i}.png')
                                          .convert_alpha() for i in range(4)]),
                'is_dead': None,
                'dead_shift': 1.0,
                'animation_dist': 800,
                'animation_speed': 10,
                'blocked': True,
                'flag' : 'npc',
                'obj_action' : []
            },
            'green_sprite': {
                'sprite': pygame.image.load('sprite/enemys/green_sprite.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6,0.6),
                'side' : 40,
                'animation': deque(
                    [pygame.image.load(f'sprite/enemys/red_sprite.png').convert_alpha() for i in range(1)]),
                'death_animation': deque([pygame.image.load(f'sprite/dead/animation/{i}.png')
                                          .convert_alpha() for i in range(4)]),
                'is_dead': None,
                'dead_shift': 1.0,
                'animation_dist': 800,
                'animation_speed': 10,
                'blocked': True,
                'flag' : 'npc',
                'obj_action' : []
            },
        }
        # self.sprite_types = {
        #     'red_sprite' : pygame.image.load('sprite/enemys/red_sprite.png').convert_alpha(),
        #     'blue_sprite' : pygame.image.load('sprite/enemys/blue_sprite.png').convert_alpha(),
        #     'coin' : [pygame.image.load(f'sprite/coin/{i}.png').convert_alpha() for i in range(8)]
            
        # }
        
        self.list_of_objects = [
            SpriteObject(self.sprite_parameters['red_sprite'], (7.1,2.1)),
            SpriteObject(self.sprite_parameters['red_sprite'],(5.9,2.1)),
            SpriteObject(self.sprite_parameters['blue_sprite'], (8.8,2.5)),
            SpriteObject(self.sprite_parameters['blue_sprite'] ,(8.8,5.6)),
            SpriteObject(self.sprite_parameters['green_sprite'] ,(7.7,5.5)),
            #SpriteObject(self.sprite_parameters['coin'],(7,4)),
            SpriteObject(self.sprite_parameters['explosion'],(8,4)),
            
            
        ]
# @property
#     def sprite_shot(self):
#         if player_pos.dete
        
    @property
    def pos(self):
        return (self.x, self.y)
        
@property
def blocked_doors(self):
    blocked_doors = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
    for obj in self.list_of_objects:
        if obj.flag in {'door_h', 'door_v'} and obj.blocked:
            i, j = mapping(obj.x, obj.y)
            blocked_doors[(i, j)] = 0
    return blocked_doors

        
class SpriteObject:
    def __init__(self, parameters, pos):
        self.object = parameters['sprite'].copy()
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation'].copy()
        # ---------------------
        self.death_animation = parameters['death_animation'].copy()
        self.is_dead = parameters['is_dead']
        self.dead_shift = parameters['dead_shift']
        # ---------------------
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.flag = parameters['flag']
        self.obj_action = parameters['obj_action'].copy()
        self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.side = parameters['side']
        self.dead_animation_count = 0
        self.animation_count = 0
        self.npc_action_trigger = False
        self.door_open_trigger = False
        self.door_prev_pos = self.y if self.flag == 'door_h' else self.x
        self.delete = False
        if self.viewing_angles:
            if len(self.object) == 8:
                self.sprite_angles = [frozenset(range(338, 361)) | frozenset(range(0, 23))] + \
                                     [frozenset(range(i, i + 45)) for i in range(23, 338, 45)]
            else:
                self.sprite_angles = [frozenset(range(348, 361)) | frozenset(range(0, 11))] + \
                                     [frozenset(range(i, i + 23)) for i in range(11, 348, 23)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player):
        

        dx, dy = self.x - player.x, self.y - player.y
        self.distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        self.theta = math.atan2(dy, dx)
        gamma = self.theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI
        self.theta -= 1.4 * gamma

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        self.distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and self.distance_to_sprite > 30:
            self.proj_height = min(int(PROJ_COEFF / self.distance_to_sprite),
                                   DOUBLE_HEIGHT if self.flag not in {'door_h', 'door_v'} else HEIGHT)
            sprite_width = int(self.proj_height * self.scale[0])
            sprite_height = int(self.proj_height * self.scale[1])
            half_sprite_width = sprite_width // 2
            half_sprite_height = sprite_height // 2
            shift = half_sprite_height * self.shift
            half_proj_height = self.proj_height // 2
            shift = half_proj_height * self.shift

            if self.is_dead and self.is_dead != 'immortal':
                sprite_object = self.dead_animation()
                shift = half_sprite_height * self.dead_shift
                sprite_height = int(sprite_height / 1.3)
            elif self.npc_action_trigger:
                sprite_object = self.npc_in_action()
            else:
                self.object = self.visible_sprite()
                sprite_object = self.sprite_animation()

        
            #масштабуання по висоті ,проекції і т.д
            sprite_pos = (current_ray * SCALE - half_sprite_width, HALF_HEIGHT - half_sprite_height + shift)
            sprite = pygame.transform.scale(sprite_object, (sprite_width, sprite_height))
            return (self.distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)
    
    def sprite_animation(self):
        if self.animation and self.distance_to_sprite < self.animation_dist:
                sprite_object = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0
                return sprite_object
        return self.object

    def visible_sprite(self):
        if self.viewing_angles:
                if self.theta < 0:
                    self.theta += DOUBLE_PI
                self.theta = 360 - int(math.degrees(self.theta))

                for angles in self.sprite_angles:
                    if self.theta in angles:
                       return self.sprite_positions[angles]
        return self.object
    
    def dead_animation(self):
        if len(self.death_animation):
            if self.dead_animation_count < self.animation_speed:
                self.dead_sprite = self.death_animation[0]
                self.dead_animation_count += 1
            else:
                self.dead_sprite = self.death_animation.popleft()
                self.dead_animation_count = 0
        return self.dead_sprite

    def npc_in_action(self):
        sprite_object = self.obj_action[0]
        if self.animation_count < self.animation_speed:
            self.animation_count += 1
        else:
            self.obj_action.rotate()
            self.animation_count = 0
        return sprite_object
                        
    @property
    def pos(self):
        return (self.x, self.y)