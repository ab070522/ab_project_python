import pygame
import random
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

x_a, y_a = 0, 0

run = True
move = False
while run:
    screen.fill(map_color)

    #  선 만드는 코드
    make_draw_line()

    #기본 그림 넣기
    xy = []
    blank_num = 0
    y = 20
    for i in range(5):

        x = 10
        for a in range(5):
            kk = []
            if blank[blank_num] == 0:
                screen.blit(redImg, (x, y))
                kk.append(x)
                kk.append(y)
                xy.append(kk)
            elif blank[blank_num] == 1:
                screen.blit(blueImg, (x, y))
                kk.append(x)
                kk.append(y)
                xy.append(kk)
            elif blank[blank_num] == 2:
                screen.blit(orangeImg, (x, y))
                kk.append(x)
                kk.append(y)
                xy.append(kk)
            elif blank[blank_num] == 3:
                screen.blit(PurpleImg, (x, y))
                kk.append(x)
                kk.append(y)
                xy.append(kk)
            elif blank[blank_num] == 4:
                screen.blit(greenImg, (x, y))
                kk.append(x)
                kk.append(y)
                xy.append(kk)
            x += 80
            blank_num += 1
        y += 80


    for even in pygame.event.get():

        #캔디 움직이기

        if even.type == pygame.MOUSEBUTTONDOWN:
            if x_a == 0 and y_a == 0:
                x_a, y_a = pygame.mouse.get_pos()
                with_draw = 5
                color_red = (225, 0, 0)
                pygame.draw.rect(screen, color_red, (20, 100, 50, 50), with_draw)

                for find_x in range(5):
                    if x_a < (find_x+1)*80:
                        x_a_ce = find_x
                        break
                for find_y in range(5):
                    if y_a < (find_y+1)*80:
                        y_a_ce = find_y
                        break
                print(x_a_ce, y_a_ce, "a")



            elif  x_a != 0 and y_a != 0:
                x_b, y_b = pygame.mouse.get_pos()
                for find_x in range(5):
                    if x_b < (find_x+1)*80:
                        x_b_ce = find_x
                        break
                for find_y in range(5):
                    if y_b < (find_y+1)*80:
                        y_b_ce = find_y
                        break
                print(x_b_ce, y_b_ce, "b")
                blank[x_a_ce + y_a_ce * 5], blank[x_b_ce + y_b_ce * 5] = blank[x_b_ce + y_b_ce * 5], blank[x_a_ce + y_a_ce * 5]

                x_a, y_a = 0, 0

                # 사각형 테두리 그리기
    with_draw = 5
    color_green = (225, 0, 0)

    pygame.draw.rect(screen, color_green, (좌표), with_draw)

    pygame.display.update()