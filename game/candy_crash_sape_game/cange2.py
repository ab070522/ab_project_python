import pygame
import random

RED = (225, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAP_COLOR = (82, 130, 137)
GAME_WIDTH = 400
GAME_HEIGHT = 400
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


def make_position_matrix():
    pos_matrix = [[], [], [], [], []]

    for i in range(5):
        for j in range(5):
            kan_x = GAME_WIDTH // 5
            kan_y = GAME_HEIGHT // 5
            x = i * kan_x
            y = j * kan_y
            pos_matrix[i].append([x, y])

    return pos_matrix


def draw_line():
    for i in range(1, 6):
        pygame.draw.line(screen, BLACK, (80 * i, 0), (80 * i, 400), 5)
        pygame.draw.line(screen, BLACK, (0, 80 * i), (400, 80 * i), 5)


def draw_img(game_matrix):
    for i in range(5):
        for u in range(5):
            x, y = pos_matrix[i][u]
            screen.blit(game_matrix[i][u], (x+10, y+10))


def get_image_list():
    color = {}
    RED = pygame.image.load("red.PNG").convert()
    PURPLE = pygame.image.load("purple.png").convert()
    ORANGE = pygame.image.load("orange.png").convert()
    GREEN = pygame.image.load("green.png").convert()
    BLUE = pygame.image.load("blue.png").convert()
    YELLOW = pygame.image.load("yellow.png").convert()

    color["R"] = RED
    color["P"] = PURPLE
    color["O"] = ORANGE
    color["G"] = GREEN
    color["B"] = BLUE
    color["Y"] = YELLOW

    return color


# 계산을 통해 x, y의 좌표를 간단히 변환 시켜주는 작업.
def get_position(x, y):
    kan_x = GAME_WIDTH // 5
    kan_y = GAME_HEIGHT // 5

    matrix_x = x // kan_x
    matrix_y = y // kan_y

    return matrix_x, matrix_y


def make_random_matrix(imgs_dict):
    game_matrix = [[], [], [], [], []]

    num = ["R", "P", "O", "G", "B", "Y"]

    for i in range(5):
        for j in range(5):
            random_num = random.randrange(6)
            game_matrix[i].append(imgs_dict[num[random_num]])

    return game_matrix


pygame.display.set_caption('candy crash saga')

# 좌표에 랜덤 블럭 넣기, 리스트에 블럭 색 정리
img_dict = get_image_list()
game_matrix = make_random_matrix(img_dict)  # 좌표리스트
pos_matrix = make_position_matrix()

# position_fin_list = make_position_fin_list(position_list)
#
# print(position_list)
start = 0
finish = 0
x_a = None
y_a = None
x_b = None
y_b = None
# print(random_color_list)
# 게임 실행
run = True
screen.fill(MAP_COLOR)
draw_line()

while run:

    # print(game_matrix[0][0])

    draw_img(game_matrix)

    # Event 처리
    able_action = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for even in pygame.event.get():
        if even.type == pygame.MOUSEBUTTONDOWN:
            down_x, down_y = pygame.mouse.get_pos()
            d_x, d_y = get_position(down_x, down_y)
            x, y = pos_matrix[d_x][d_y]

        elif even.type == pygame.MOUSEBUTTONUP:
            up_x, up_y = pygame.mouse.get_pos()
            u_x, u_y = get_position(up_x, up_y)

            for i in range(4):
                if able_action[i][i] == [d_x - u_x][d_y - u_y]:
                    game_matrix[u_x][u_y], game_matrix[d_x][d_y] = game_matrix[d_x][d_y], game_matrix[u_x][u_y]

            print("aaa", u_x, u_y)







    # for u in range(5):
    #     for i in range(5):
    #         if random_color_list[u][i] == random_color_list[u][i] == random_color_list[u][i]:
    #             pass
    #
    # if x_a != None:
    #     for i in range(5):
    #         for u in range(5):
    #             if position_list[5*i+u][0] <= x_a and position_list[5*i+u][1] <= y_a and position_fin_list[5*i+u][0] > x_a and position_fin_list[5*i+u][1] > y_a:
    #                 start = position_list[5*i+u]
    # if x_b != None:
    #     for i in range(5):
    #         for u in range(5):
    #             if position_list[5*i+u][0] <= x_b and position_list[5*i+u][1] <= y_b and position_fin_list[5*i+u][0] > x_b and position_fin_list[5*i+u][1] > y_b:
    #                 finish = position_list[5*i+u]
    #
    #     if finish != start:
    #         if start[0]+45 < finish[0] and start[0]+150 > finish[0] and start[1] == finish[1]:
    #             x_a, x_b = change_block()
    #         elif start[0]-45 > finish[0] and start[0]-150 < finish[0] and start[1] == finish[1]:
    #             x_a, x_b = change_block()
    #         elif start[1]+45 < finish[1] and start[1]+150 > finish[1] and start[0] == finish[0]:
    #             x_a, x_b = change_block()
    #         elif start[1]-45 > finish[1] and start[1]-150 < finish[1] and start[0] == finish[0]:
    #             x_a, x_b = change_block()
    #

    pygame.display.update()