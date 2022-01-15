import pygame
import random
from pygame.locals import *
def make_draw_line():
    pygame.draw.line(screen, black, (80, 0), (80, 400), 5)
    pygame.draw.line(screen, black, (160, 0), (160, 400), 5)
    pygame.draw.line(screen, black, (240, 0), (240, 400), 5)
    pygame.draw.line(screen, black, (320, 0), (320, 400), 5)
    pygame.draw.line(screen, black, (400, 0), (400, 400), 5)

    pygame.draw.line(screen, black, (0, 80), (400, 80), 5)
    pygame.draw.line(screen, black, (0, 160), (400, 160), 5)
    pygame.draw.line(screen, black, (0, 240), (400, 240), 5)
    pygame.draw.line(screen, black, (0, 320), (400, 320), 5)
    pygame.draw.line(screen, black, (0, 400), (400, 400), 5)


screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('candy crash sape game')


redImg = pygame.image.load('red.png')
blueImg = pygame.image.load('blue.png')
greenImg = pygame.image.load('green.png')
orangeImg = pygame.image.load('orange.png')
PurpleImg = pygame.image.load('Purple.png')
rect = redImg.get_rect()
black = (0, 0, 0)
map_color = (1, 205, 249)
blank = []
for i in range(25):
    blank.append(random.randrange(5))

print(blank)
run = True
move = False
while run:
    screen.fill(map_color)

    #  선 만드는 코드
    make_draw_line()


    #기본 그림? 넣기
    blank_num = 0
    y = 20
    for i in range(5):
        x = 10
        for a in range(5):
            if blank[blank_num] == 0:
                screen.blit(redImg, (x, y))
            elif blank[blank_num] == 1:
                screen.blit(blueImg, (x, y))
            elif blank[blank_num] == 2:
                screen.blit(orangeImg, (x, y))
            elif blank[blank_num] == 3:
                screen.blit(PurpleImg, (x, y))
            elif blank[blank_num] == 4:
                screen.blit(greenImg, (x, y))
            x += 80
            blank_num += 1
        y += 80

    for even in pygame.event.get():

        #마우스 버튼 누를때
        if even.type == pygame.MOUSEBUTTONDOWN:
            x_a, y_a = pygame.mouse.get_pos()
        if even.type == pygame.MOUSEBUTTONDOWN:
            x_b, y_b = pygame.mouse.get_pos()
        if