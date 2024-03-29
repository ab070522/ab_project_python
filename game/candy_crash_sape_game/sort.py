import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAP_COLOR = (82, 130, 137)
GAME_WIDTH = 400
GAME_HEIGHT = 400

def make_draw_line():
     for i in range(5):
         for u in range(5):
             screen.blit(color_list[random_color_list[i][u]], (position_list[5*i+u-1][0], position_list[5*i+u-1][1]))

    for i in range(1, 6):
        pygame.draw.line(screen, BLACK, (80 * i, 0), (80 * i, 400), 5)
        pygame.draw.line(screen, BLACK, (0, 80 * i), (400, 80 * i), 5)

def get_image_list():
    color = {}
    RED = pygame.image.load("red.PNG").convert()
    PURPLE = pygame.image.load("purple.PNG").convert()
    ORANGE = pygame.image.load("orange.PNG").convert()
    GREEN = pygame.image.load("green.PNG").convert()
    BLUE = pygame.image.load("blue.PNG").convert()

    color["R"] = RED
    color["P"] = PURPLE
    color["O"] = ORANGE
    color["G"] = GREEN
    color["B"] = BLUE

    return color

def make_random_matrix(imgs_dict):

    game_matrix = []

    num = ["R", "P", "O", "G", "B", "Y"]


    for i in range(5):
        for j in range(5):
            random_num = random.randrange(6)
            game_matrix.append(imgs_dict[num[random_num]])

    print(game_matrix)

def make_position_fin_list(list):
    position_fin_list = []
    for i in range(len(list)):
        xy = []
        c = list[i][0] + 81
        d = list[i][1] + 81
        xy.append(c)
        xy.append(d)
        position_fin_list.append(xy)
    return position_fin_list

 def change_block():
     print((position_list.index(start)+1)%5, (position_list.index(finish)+1)%5)
     change_block_a = random_color_list[(position_list.index(start)+1)//5][(position_list.index(start)+1)%5]
     change_block_b = random_color_list[(position_list.index(finish)+1)//5][(position_list.index(finish)+1)%5]
     random_color_list[(position_list.index(start)+1)//5][(position_list.index(start)+1)%5] = change_block_b
     random_color_list[(position_list.index(finish)+1)//5][(position_list.index(finish)+1)%5] = change_block_a
     x_a = None
     x_b = None
     return x_a, x_b

screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('candy crash saga')

# 좌표에 랜덤 블럭 넣기, 리스트에 블럭 색 정리
img_dict = get_image_list()
game_matrix = make_random_matrix(img_dict) #좌표리스트
position_fin_list = make_position_fin_list(position_list)

print(position_list)
start = 0
finish = 0
x_a = None
y_a = None
x_b = None
y_b = None
print(random_color_list)
# 게임 실행
run = True
screen.fill(MAP_COLOR)
make_draw_line()

# 계산을 통해 x, y의 좌표를 간단히 변환 시켜주는 작업.
def get_position(x, y):

    kan_x = GAME_WIDTH // 5
    kan_y = GAME_HEIGHT // 5

    matrix_x = x // kan_x
    matrix_y = y // kan_y

    return matrix_x, matrix_y


while run:

    # Event 처리
    for even in pygame.event.get():
        if even.type == pygame.MOUSEBUTTONDOWN:
            down_x, down_y = pygame.mouse.get_pos()
            d_x, d_y = get_position(down_x, down_y)

        elif even.type == pygame.MOUSEBUTTONUP:
            up_x, up_x = pygame.mouse.get_pos()
            u_x, u_y = get_position(up_x, up_x)

    able_action = [[-1, 0], [1,0], [0, -1], [0, 1]]

     for u in range(5):
         for i in range(5):
             if random_color_list[u][i] == random_color_list[u][i] == random_color_list[u][i]:
                 pass

     if x_a != None:
         for i in range(5):
             for u in range(5):
                 if position_list[5*i+u][0] <= x_a and position_list[5*i+u][1] <= y_a and position_fin_list[5*i+u][0] > x_a and position_fin_list[5*i+u][1] > y_a:
                     start = position_list[5*i+u]
     if x_b != None:
         for i in range(5):
             for u in range(5):
                 if position_list[5*i+u][0] <= x_b and position_list[5*i+u][1] <= y_b and position_fin_list[5*i+u][0] > x_b and position_fin_list[5*i+u][1] > y_b:
                     finish = position_list[5*i+u]

         if finish != start:
             if start[0]+45 < finish[0] and start[0]+150 > finish[0] and start[1] == finish[1]:
                 x_a, x_b = change_block()
             elif start[0]-45 > finish[0] and start[0]-150 < finish[0] and start[1] == finish[1]:
                 x_a, x_b = change_block()
             elif start[1]+45 < finish[1] and start[1]+150 > finish[1] and start[0] == finish[0]:
                 x_a, x_b = change_block()
             elif start[1]-45 > finish[1] and start[1]-150 < finish[1] and start[0] == finish[0]:
                 x_a, x_b = change_block()



    pygame.display.update()
