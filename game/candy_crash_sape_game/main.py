
import pygame
import random
import mouse

screen = pygame.display.set_mode((400, 400))


pygame.display.set_caption('candy crash sape game')

redImg = pygame.image.load('red.png')
blueImg = pygame.image.load('blue.png')
greenImg = pygame.image.load('green.png')
orangeImg = pygame.image.load('orange.png')
PurpleImg = pygame.image.load('Purple.png')
black = (0, 0, 0)
map_color = (1, 205, 249)

run = True
while run:
    screen.fill(map_color)

    y = 20
    for i in range(5):
        x = 10
        for a in range(5):
            random = random.randrange(5)
            if random == 0:
                screen.blit(redImg, (x, y))
            elif random == 1:
                screen.blit(blueImg, (x, y))
            elif random == 2:
                screen.blit(greenImg, (x, y))

            x += 80
        y += 80

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

    pygame.display.update()
