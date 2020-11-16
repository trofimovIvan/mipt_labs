import pygame
import random
from pygame.math import Vector2
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 1000
HEIGHT = 800
FPS = 30
size = (70, 70)

bulle_img = pygame.image.load('C:/Users/Home/PycharmProjects/untitled2/img/explosion.png')
tank_img = pygame.image.load('C:/Users/Home/PycharmProjects/python_mipt_labs/img/tank1.png')
tower_img = pygame.image.load('C:/Users/Home/PycharmProjects/python_mipt_labs/img/tower.png')
plane1_img_list = [pygame.image.load('C:/Users/Home/PycharmProjects/python_mipt_labs/img/plane1.png'),
                   pygame.image.load('C:/Users/Home/PycharmProjects/python_mipt_labs/img/plane1_rev.png')]
plane2_img_list = [pygame.image.load('C:/Users/Home/PycharmProjects/python_mipt_labs/img/plane2.png'),
                   pygame.image.load('C:/Users/Home/PycharmProjects/python_mipt_labs/img/plane2_rev.png')]

bullet2_img = pygame.image.load('C:/Users/Home/PycharmProjects/python_mipt_labs/img/bullet2.png')
bomb_img_clean = pygame.image.load('C:/Users/Home/PycharmProjects/python_mipt_labs/img/bomb100.png')
bomb_img = pygame.transform.scale(bomb_img_clean, (50, 50))


tower_surf = pygame.Surface((int(tower_img.get_size()[0] *2), tower_img.get_size()[1]))
tower_surf_clean = tower_surf.copy()

tower_surf2 = pygame.Surface((int(tower_img.get_size()[0] *2), tower_img.get_size()[1]))
tower_surf_clean2 = tower_surf.copy()
image_clean = tower_img.copy()
rot = 0 # angle of rotating tower
rot2 = 0
force = 0 # force to charging shoot
force2 = 0

def radian(angle):
    return angle / 180 * math.pi

def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotate(surface, angle)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect

class Gun(pygame.sprite.Sprite):
    '''Class Gun. It is body of tank'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tank_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0
        self.rect.center = (size[0] // 2, HEIGHT - size[1] // 2 - 50) #center of tank
        self.health = 10


    def update(self):
        '''This function updates position on the screen. K_LEFT - move left, K_RIGHT - move right. Tank stops when
        you do not push buttons
        This function calls in main body at sprite.update group.'''
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_LEFT]:
            self.speedx = -10
        if key_list[pygame.K_RIGHT]:
            self.speedx = 10
        self.rect.x += self.speedx

        if self.rect.x >= WIDTH - 20:
            self.rect.x = WIDTH - 20
        if self.rect.x <= 20:
            self.rect.x = 20
        self.speedx = 0


class Tower(pygame.sprite.Sprite):
    '''Class Tower -- tower of tank.
    Args : x, y - position of tower at the tank
            speedx, speedy - speed of tank tower. (Takes Gun() speed) '''
    def __init__(self, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = tower_surf
        self.rect = self.image.get_rect()

        tower_surf_clean.blit(tower_img, (self.rect[0] + 100, self.rect[1]))

        self.image.set_colorkey(BLACK)
        self.rect.x = x
        self.rect.y = y
        self.pos_tower = (x + 10, y + 30)
        self.speedx = speedx
        self.speedy = speedy
        self.pos = Vector2(self.rect.x , self.rect.y )
        self.offset = Vector2(-2, 0)
        self.pivot = (self.rect[0], self.rect[1])


    def update(self):
        '''function updates tower on the screen. Tower rotates when you press A or D key. Tower charging when you
        press SPACE.'''
        global force
        key_list = pygame.key.get_pressed()

        if key_list[pygame.K_a]:
            self.rotate_a()

        if key_list[pygame.K_d]:
            self.rotate_d()
        if key_list[pygame.K_SPACE]:
            force += 1



        self.rect.center = self.pos_tower # gives center of tower position of begininng center. This is
        # takes tower at the tank
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def rotate_a(self):
        '''function rotates tower when you press a'''
        global tower_img, rot, tower_surf
        rot += 5

        tower_surf, self.pos = rotate(tower_surf_clean, rot, self.pivot, self.offset)
        self.image.set_colorkey(BLACK)


    def rotate_d(self):
        '''function rotates tower when you press d'''
        global tower_img, rot, tower_surf
        rot -= 5

        tower_surf, self.pos = rotate(tower_surf_clean, rot, self.pivot, self.offset)
        self.image.set_colorkey(BLACK)

class Tower2(pygame.sprite.Sprite):
    '''Class Tower -- tower of tank.
    Args : x, y - position of tower at the tank
            speedx, speedy - speed of tank tower. (Takes Gun() speed) '''
    def __init__(self, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = tower_surf2
        self.rect = self.image.get_rect()

        tower_surf_clean2.blit(tower_img, (self.rect[0] + 100 , self.rect[1]))

        self.image.set_colorkey(BLACK)
        self.rect.x = x -30
        self.rect.y = y
        self.pos_tower = (x , y + 30)
        self.speedx = speedx
        self.speedy = speedy
        self.pos = Vector2(self.rect.x , self.rect.y + 30)
        self.offset = Vector2(-2, 0)
        self.pivot = (self.rect[0], self.rect[1])

    def update(self):
        '''function updates tower on the screen. Tower rotates when you press A or D key. Tower charging when you
        press SPACE.'''
        global force2
        key_list = pygame.key.get_pressed()

        if key_list[pygame.K_a]:
            self.rotate_a()

        if key_list[pygame.K_d]:
            self.rotate_d()
        if key_list[pygame.K_SPACE]:
            force2 += 1

        self.rect.center = self.pos_tower # gives center of tower position of begininng center. This is
        # takes tower at the tank
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def rotate_a(self):
        '''function rotates tower when you press a'''
        global tower_img, rot2, tower_surf2
        rot2 += 5

        tower_surf2, self.pos = rotate(tower_surf_clean2, rot2, self.pivot, self.offset)
        self.image.set_colorkey(BLACK)


    def rotate_d(self):
        '''function rotates tower when you press d'''
        global tower_img, rot2, tower_surf2
        rot2 -= 5

        tower_surf2, self.pos = rotate(tower_surf_clean2, rot2, self.pivot, self.offset)
        self.image.set_colorkey(BLACK)

class Bullet(pygame.sprite.Sprite):
    '''Class Bullet. First type of bullet. It is dropping by gravity force.
    Args:   x, y - position where bullet will be created
            speedx, speedy - speed of bullet    '''
    def __init__(self, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulle_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x

        self.speedy = speedy
        self.speedx = speedx

    def update(self):
        '''function updates bullet on the screen'''
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.speedy += 3

class Bullet2(pygame.sprite.Sprite):
    '''Class Bullet2. Second type of bullet. It is not dropping under gravity force? fly straight.
        Args: x, y - coordinates where bullet will be created
                speedx, speedy - speed of bullet'''
    def __init__(self, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet2_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x

        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        '''function updates bullet on the screen'''
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Target1(pygame.sprite.Sprite):
    '''Class Target1. This is the first type of plane. It flies straight. Spawns randomly'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        cords = (random.randint(100, WIDTH), random.randint(0, HEIGHT - 400))

        self.image = plane1_img_list[0]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = cords
        self.speedx = random.randint(-20, 20)
        self.speedy = 0
        self.time_bomb = 5000


    def update(self):
        '''function updates position on the screen. It changes towards of moving when plane hits with walls'''
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.speedx < 0:
            self.image = plane1_img_list[1]
        if self.rect.x >= WIDTH:
            self.speedx *= -1
            self.image = plane1_img_list[1]
        if self.rect.x <= 0:
            self.speedx *= -1
            self.image = plane1_img_list[0]

class Target2(pygame.sprite.Sprite):
    '''class Target2. It is a plane2 with special move. It is moving up and down in time'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cords = (random.randint(100, WIDTH), random.randint(0, HEIGHT - 400))
        self.image = plane2_img_list[0]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = cords
        self.speedx = random.randint(-30, 30)
        self.speedy = random.randint(-30, 30)
        self.pos = self.rect.center
        self.time_bomb = 2000

    def update(self):
        '''Updates position on the screen'''
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.speedx < 0:
            self.image = plane2_img_list[1]
        if self.rect.x >= WIDTH:
            self.speedx *= -1
            self.image = plane2_img_list[1]
        if self.rect.x <= 0:
            self.speedx *= -1
            self.image = plane2_img_list[0]
        if abs(self.rect.y - self.pos[1]) > 100:
            self.speedy *= -1

class Bomb(pygame.sprite.Sprite):
    '''Class bombs. Its hurts tanks when they falls on it.
     Args :  x, y - position of bomb
                speedx - speed of bomb'''
    def __init__(self, x, y, speedx):
        pygame.sprite.Sprite.__init__(self)
        self.image = bomb_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx
        self.speedy = 0

    def update(self):
        '''function updates bombs position on the screen'''
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.speedy += 3


def force_bar_draw(surf, x, y, pct):
    '''Args :  surf - surface where force bar will be draw
                x, y - coordinates where force bar will be draw
                pct - scale that shows how much bar will be draw'''
    if pct > 50:
        pct = 50
    bar_lenght = 5
    bar_height = 20
    fill = pct * bar_lenght
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, BLACK, fill_rect)

def new_target1():
    '''Creates Target1 on the screen'''
    target_list.pop(0)
    targ = Target1()
    target_sprite.add(targ)
    target_list.append(targ)
    target_list[0], target_list[1] = target_list[1], target_list[0]

def new_target2():
    '''Creates Target2 on the screen'''
    target_list.pop(1)
    targ = Target2()
    target_sprite2.add(targ)
    target_list.append(targ)


def drop_the_bomb(x, y, speedx):
    '''Function creates a bomb on the screen.
        Args :  x, y - coordinates where bomb will be created
                speedx - speed of bomb'''
    bomb = Bomb(x, y, speedx)
    target_sprite.add(bomb)
    bomb_sprite.add(bomb)


def bullet_cords(gun_pos, angle):
    ''':Args :  gun_pos - coordinates of tower
                angle - angle of rotates tower
        returns : position of bullet, Tuple'''
    angle = radian(angle)
    w, h = tower_img.get_size()
    gun_lenght = math.sqrt(w**2 + h**2)
    return gun_pos[0] + gun_lenght* math.cos(angle)  , gun_pos[1] - gun_lenght* math.sin(angle)

def bullet_speed(force,angle):
    ''':arg : force - force to charge bullet
                angle - angle of rotates
        :return speedx, speedy - Tuple'''
    angle = radian(angle)
    return force*math.cos(angle), force * math.sin(angle)

def shoot(gun_pos, force_a, angle):
    ''':argument : gun_pos position of tower, where bullet will be created
                    force_a - force to charge bullet
                    angle - angle of rotates
        Function creates bullet sprite that depends on what tank you are'''
    global balls2, bullet_sprite

    x1, y1 = bullet_cords(gun_pos, angle)
    vx, vy = bullet_speed(force_a, angle)
    if bullet1:
        bullet = Bullet(x1 , y1, vx, -vy)
        bullet_sprite.add(bullet)
    if bullet2 and balls2 > 0:
        bullet = Bullet2(x1, y1, vx, -vy)
        balls2 -= 1
        bullet_sprite.add(bullet)

def show_management():
    '''Function create menu with instructions'''
    text_obj = pygame.font.SysFont(None, 36)
    menu = []
    menu.append(text_obj.render('Движение танка - стрелками', 1, BLACK))
    menu.append(text_obj.render('Клавиши А и D - поворот башни', 1, BLACK))
    menu.append(text_obj.render('Пробел - зарядить пушку, S - выстрел', 1, BLACK))
    menu.append(text_obj.render('Смена оружия - клавиши 1 и 2', 1, BLACK))
    menu.append(text_obj.render('Переключаться между танками Q и E', 1, BLACK))
    menu.append(text_obj.render('Кнопка меню - TAB, выйти из меню - ESC', 1, BLACK))
    i = 0
    for text in menu:
        screen.blit(text, (WIDTH//2 - 200, -200 + HEIGHT//2 + i))
        i += 50

def draw_green_balls(balls2):
    '''Args : balls2 : - number of balls
        Function creates text on the screen that shows how many second type bullet you have'''
    text_obj = pygame.font.SysFont(None, 24)
    text = text_obj.render('Осталось {} снарядов 2-ого типа'.format(balls2), 1, BLACK)
    screen.blit(text, (WIDTH - 300, 50))

def draw_your_weapon():
    '''Function draws on the screen what type of weapon do you have'''
    text_obj = pygame.font.SysFont(None, 36)
    if bullet1:
        text = text_obj.render('1 - тип снарядов', 1, BLACK)
    if bullet2:
        text = text_obj.render('2 - тип снарядов', 1, BLACK)
    if not bullet1 and not bullet2:
        text = text_obj.render('Вы не выбрали тип снарядов', 1, BLACK)
    screen.blit(text, (0, 50))

def drop_bombs(time, t1, t2):
    '''Args: time - time to create new bomb, integer
                t1 - Target1 type
                t2 - Target2 type
        Function creates a bombs'''
    if time > t1.time_bomb:
        t1.time_bomb = time + 4000
        drop_the_bomb(t1.rect.x, t1.rect.bottom, t1.speedx)
    if time > t2.time_bomb:
        t2.time_bomb = time + 2000
        drop_the_bomb(t2.rect.x, t2.rect.bottom, t2.speedx)

def health_bar_draw1(surf, x, y, pct):
    '''Args : surf - surface where health bar will be drawn
                x, y - position where health bar will be drawn, integer
                pct - scale that shows how much healt do you have
        Function draws health bar'''
    if pct < 0:
        pct = 0
    bar_lenght = 30
    bar_height = 20
    fill = (pct) * bar_lenght
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    text_obj = pygame.font.SysFont(None, 30)
    text = text_obj.render('HP ', 1, BLACK)
    surf.blit(text, (x - 50, y))
    pygame.draw.rect(surf, RED, fill_rect)

def tank():
    '''Function that responds on what tank you are. You will be on tank1 if tank1 = True, or tank2 if tank2 = True'''
    global tank1, tank2, tower, tower2
    if tank1:

        tower.kill()
        tower = Tower(gun.rect.centerx, gun.rect.y + 30, gun.speedx, gun.speedy)
        gun_sprite.add(tower)
        gun_sprite.update()
    if tank2:
        tower2.kill()
        tower2 = Tower2(gun2.rect.centerx, gun2.rect.y + 30, gun2.speedx, gun2.speedy)
        gun_sprite2.add(tower2)
        gun_sprite2.update()


def hits():
    '''Function checks if there is hits and makes a decision what to do. It removes one points health if
    bombs hits a tank, 3 points if tank hits another tank, it removes plane if bullet hits a plane'''
    hit_list = pygame.sprite.groupcollide(target_sprite, bullet_sprite, True, True)
    hit2_list = pygame.sprite.groupcollide(target_sprite2, bullet_sprite, True, True)
    bomb_hit = pygame.sprite.spritecollide(gun, bomb_sprite, True)
    bomb_hit2 = pygame.sprite.spritecollide(gun2, bomb_sprite, True)
    if tank1:
        tank_hits = pygame.sprite.spritecollide(gun2, bullet_sprite, True)

    if tank2:
        tank_hits = pygame.sprite.spritecollide(gun, bullet_sprite, True)
    for hit in hit_list:
        if hit:
            new_target1()
    for hit in hit2_list:
        if hit:
            new_target2()
    for hit in bomb_hit:
        if hit:
            gun.health -= 1
    for hit in bomb_hit2:
        if hit:
            gun2.health -= 1
    for hit in tank_hits:
        if hit and tank1:
            gun2.health -= 3
        if hit and tank2:
            gun.health -= 3

def update_screen():
    '''Function updates all sprites and another staff on the screen'''
    target_sprite.update()
    target_sprite2.update()
    bullet_sprite.update()
    screen.fill(WHITE)
    if gun.health > 0:
        gun_sprite.draw(screen)
    if gun2.health > 0:
        gun_sprite2.draw(screen)
    if show_menu:
        show_management()
    draw_green_balls(balls2)
    force_bar_draw(screen, 0, 0, force)
    force_bar_draw(screen, WIDTH - 300, 0, force2)
    draw_your_weapon()
    health_bar_draw1(screen, 50, 100, gun.health)
    health_bar_draw1(screen, WIDTH - 350, 100, gun2.health)
    target_sprite.draw(screen)
    target_sprite2.draw(screen)
    bullet_sprite.draw(screen)
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

gun_sprite = pygame.sprite.Group()
gun_sprite2 = pygame.sprite.Group()

bullet_sprite = pygame.sprite.Group()
target_sprite = pygame.sprite.Group()
target_sprite2 = pygame.sprite.Group()
bomb_sprite = pygame.sprite.Group()


gun = Gun()
target = Target1()
target2 = Target2()
gun2 = Gun()

gun2.rect.center = (WIDTH - 500, HEIGHT - 100)
target_list = [target, target2]

tower = Tower(gun.rect.centerx, gun.rect.centery, gun.speedx, gun.speedy)
tower_surf.blit(tower_img, (tower_surf.get_rect()[0] + 100, tower_surf.get_rect()[1]))

tower2 = Tower2(gun2.rect.centerx, gun2.rect.y + 30, gun2.speedx, gun2.speedy)
tower2.rotate_a()



gun_sprite.add(gun)
gun_sprite.add(tower)
gun_sprite2.add(gun2)
gun_sprite2.add(tower2)
target_sprite.add(target)
target_sprite2.add(target2)

running = True
first_click = True
show_menu = False
balls2 = 10
bullet1 = False
bullet2 = False
tank1 = True
tank2 = False
while running:
    clock.tick(FPS)
    if force >= 50:
        force = 50
    if balls2 <= 0:
        balls2 = 0
    if force2 >= 50:
        force2 = 50

    time = pygame.time.get_ticks()
    drop_bombs(time, target_list[0], target_list[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                bullet1 = True
                bullet2 = False
            if event.key == pygame.K_2:
                bullet1 = False
                bullet2 = True
            if event.key == pygame.K_s:
                if tank1 and force != 0:
                    if not bullet2 or (bullet2 and balls2 > 0):
                        shoot(tower.pos, force, rot)
                        force = 0
                if tank2 and force2 != 0:
                    if not bullet2 or (bullet2 and balls2 > 0):
                        shoot(tower2.pos, force2, rot2)
                        force2 = 0
            if event.key == pygame.K_TAB:
                show_menu = True
            if event.key == pygame.K_ESCAPE:
                show_menu = False
            if event.key == pygame.K_q and gun.health > 0:
                tank1 = True
                tank2 = False
            if event.key == pygame.K_e and gun2.health > 0:
                tank1 = False
                tank2 = True



    hits()
    tank()
    update_screen()


pygame.quit()