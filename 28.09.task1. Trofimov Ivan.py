import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
FPS = 30


screen = pygame.display.set_mode((800, 800))
screen.fill(WHITE)
pygame.draw.circle(screen, YELLOW, (400, 400), 100)
pygame.draw.polygon(screen, BLACK, [(280, 280), (400, 330), (390, 345), (270, 300)])
pygame.draw.polygon(screen, BLACK, [(500, 300), (490, 290), (425, 330), (435, 340)])
pygame.draw.circle(screen, RED, (370, 360), 20)
pygame.draw.circle(screen, RED, (450, 360), 20)
pygame.draw.circle(screen, BLACK, (370, 360), 10)
pygame.draw.circle(screen, BLACK, (450, 360), 10)
pygame.draw.rect(screen, BLACK, (350, 430, 100, 20))

pygame.display.flip()

pygame.display.update()
clock = pygame.time.Clock()


finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()