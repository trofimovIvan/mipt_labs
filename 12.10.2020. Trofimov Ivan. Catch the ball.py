import random
import pygame
import tkinter

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]




def new_ball():
    '''it draws new ball on the screen. Each ball have paramters - color, coordinate, radius and velocity.
    Function returns parametrs, so i can change coordinate later'''
    global x, y, r, color, v_x, v_y
    x = random.randint(100,600)
    y = random.randint(100,600)
    r = random.randint(30,50)
    v_x = random.randint(-10, 10)
    v_y = random.randint(-10, 10)
    is_clicked = False
    color = COLORS[random.randint(0, 5)]
    parametrs = [color, [x, y], r, v_x, v_y]
    pygame.draw.circle(screen, color, (x, y), r)
    return parametrs

def boss_mob():
    '''function creates boss surface. Image of boss loads from my directory. You can change directory and
    your image will be different. As new_ball() function it returns boss parametrs'''
    global x, y, v_x, v_y
    x = random.randint(100, 800)
    y = random.randint(100, 800)
    v_x = random.randint(-20, 20)
    v_y = random.randint(-20, 20)

    boss_image_surf = pygame.image.load('C:/Users/Home/PycharmProjects/untitled2/img/fly-1.png')

    boss_image_surf_scale = pygame.transform.scale(boss_image_surf,
                                                   (boss_image_surf.get_width()//5, boss_image_surf.get_height()//5))
    boss_image_rect = boss_image_surf_scale.get_rect()
    boss_image_rect.center = (x, y)

    boss_parametrs = [boss_image_rect, v_x, v_y, boss_image_surf_scale]
    return boss_parametrs


def draw_boss_on_the_screen(boss, time_indicate):
    '''It draws boss on the screen as a surface. Boss reflects from walls. Boss changes velocity every time
    when time_inicate is True -- this is a special thing'''
    boss[0].x += boss[1]
    boss[0].y += boss[2]

    if boss[0].x <= 0 or boss[0].x >= 800:
        boss[1] *= -1
        boss[3] = pygame.transform.rotate(boss[3], 180)
    if boss[0].y <= 50 or boss[0].y >= 600:
        boss[2] *= -1

    if time_indicate:
        boss[1] = random.randint(-20, 20)
        boss[2] = random.randint(-20, 20)


    screen.blit(boss[3], boss[0])

def draw_ball(surf, color, cor, radius):
    pygame.draw.circle(surf, color, cor, radius)

def draw_balls_on_the_screen(surf, list):
    '''this function draws balls on the surf. It takes surf, where it should draw balls. list - ball list
    where is new_ball() parametrs. '''
    for i in range(len(list)):
        list[i][1][0] += list[i][3]
        list[i][1][1] += list[i][4]
        if list[i][1][0] >= 1000 or list[i][1][0] <= 50:
            list[i][3] *= -1
        if list[i][1][1] >= 800 or list[i][1][1] <= 50:
            list[i][4] *= -1
        draw_ball(surf, list[i][0], list[i][1], list[i][2])

def draw_score(score):
    '''Takes score and draws it on the screen'''
    score_obj = pygame.font.SysFont(None, 36)
    text = score_obj.render('score = {}'.format(score), 1, YELLOW)
    screen.blit(text, (500, 50))

def draw_timer(time):
    '''takes time and draws it on the screen'''
    time_obj = pygame.font.SysFont(None, 36)
    time_text = time_obj.render('time = {}'.format(time), 1, YELLOW)
    screen.blit(time_text, (100, 50))

def draw_number_of_balls(list_1):
    '''takes list of balls and draws on the screen number of balls'''
    num_obj = pygame.font.SysFont(None, 36)
    num_text = num_obj.render('number of balls = {}'.format(len(balls_list)), 1, YELLOW)
    screen.blit(num_text, (800, 50))



def player_name():
    '''Creates window where you sould put your name and press button to play. It was made on tkinter
    When player clicks on the button window destroys and game begins'''
    def command_button():
        name = field_to_write.get()
        print(name, file=list_of_the_best_players, end=' ')
        window.destroy()
    window = tkinter.Tk()
    window.geometry('400x200')
    text_window = tkinter.Label(window, text='Put your name and press ready ', font=('Arial', 20))
    text_window.grid(column=1, row=0)
    field_to_write = tkinter.Entry(window, width=36)
    field_to_write.grid(column=1, row=1)
    button_to_click = tkinter.Button(window, text='Ready', command=command_button)
    button_to_click.grid(column=1, row=2)
    window.mainloop()

def old_list_of_the_best_players():
    '''reads file with the best players'''
    list_of_the_best_players = open('list_of_the_best_players.txt', 'r')
    players_list_lines = list_of_the_best_players.readlines()
    players_list_lines_format = []
    for line in players_list_lines:
        players_list_lines_format.append(line.split())
    list_of_the_best_players.close()
    return players_list_lines_format

def add_new_player():
    '''adds new player`s name and score'''

    list_of_the_best_players = open('list_of_the_best_players.txt', 'r')
    new_player = list_of_the_best_players.readline().split()

    players_list_lines.append(new_player)
    list_of_the_best_players.close()

    list_of_the_best_players = open('list_of_the_best_players.txt', 'w')
    for line in players_list_lines:
        print(line, file=list_of_the_best_players)

    list_of_the_best_players.close()



players_list_lines = old_list_of_the_best_players()

list_of_the_best_players = open('list_of_the_best_players.txt', 'w')

player_name()
pygame.init()
FPS = 50
screen = pygame.display.set_mode((1200, 1200))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
balls_list = [] #list, where will be all balls. There will be new_ball() paramentrs
time_create_new_mob = 4 #this variable responds for creating new ball
does_boss_exist = False
ind = True
time_to_change_boss_move = 12
change_boss_move = False #time_indicate, which will be in the boss_mob() function
#create first three balls
for i in range(3):
    balls_list.append(new_ball())
while not finished:
    clock.tick(FPS)
    time = pygame.time.get_ticks() / 1000
    num = len(balls_list)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            for i in range(num - 1):
                #gets score if you clicked on the ball
                if (event.pos[0] - balls_list[i][1][0])**2 + (event.pos[1] - balls_list[i][1][1])**2 <= balls_list[i][2]**2:
                    print('YEP!')
                    balls_list.pop(i)
                    score += 1
                    break
            if does_boss_exist:
                #it gives more score for the click on boss
                if (event.pos[0] - fly_boss[0].x)**2 + (event.pos[1] - fly_boss[0].y)**2 <= fly_boss[3].get_width()**2:
                    score += 5

    if time >= time_create_new_mob:
        balls_list.append(new_ball())
        time_create_new_mob += 1 #to create new ball through 1 time
    if time >= 50 or len(balls_list) >= 20:
        finished = True

    if time >= 10 and ind:
        #ind variable responds to not create more bosses on the screen. Default - ind = True. When boss
        #exisits ind = False and its not create more bosses

        does_boss_exist = True
        fly_boss = boss_mob()
        ind = False

    if does_boss_exist and score <= 20:
        draw_boss_on_the_screen(fly_boss, change_boss_move)
        change_boss_move = False
        if time >= time_to_change_boss_move:
            change_boss_move = True
            time_to_change_boss_move += 2

    draw_number_of_balls(balls_list)
    draw_balls_on_the_screen(screen, balls_list)
    draw_score(score)
    draw_timer(time)

    pygame.display.update()
    screen.fill(BLACK)

    
pygame.QUIT

print(score, file=list_of_the_best_players)
list_of_the_best_players.close()

add_new_player()
