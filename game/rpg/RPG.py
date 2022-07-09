import pygame

## pygame 기능 사용을 시작하는 명령어 ##
pygame.init()





## 컬러 세팅 ##
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

#---------------------------------------------------------------------------

## 게임 창 설정 ##
screen_width = 640 # 가로 크기
screen_height = 489 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill(WHITE) #하얀색으로 배경 채우기

pygame.display.set_caption("RPG") # 창 이름 설정

#FPS 설정
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("imgs/backgrond.jpg")

#-----------------------------------------------------------------------------------

#캐릭터 불러오기
character = pygame.image.load("imgs/level_1.png")
character_size = character.get_rect().size #캐릭터 이미지 사이즈 구하기
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기

#캐릭터의 기준 좌표를 캐릭터의 왼쪽 상단으로 둔다.
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 절반의 중간에 위치. 좌우로 움직이는 변수
character_y_pos = (screen_height / 2) - (character_height / 2) #이미지가 화면 세로의 가장 아래 위치

#캐릭터 이동 좌표
to_x = 0
to_y = 0

#캐릭터 이동 속도 변수
charcter_speed = 0.2

#-------------------------------------------------------------------------------------------

#하트 불러오기
heart = pygame.image.load("imgs/heart.png")
heart_2 = pygame.image.load("imgs/heart.png")
heart_size = heart.get_rect().size #캐릭터 이미지 사이즈 구하기
heart_width = heart_size[0] #캐릭터 가로 크기
heart_height = heart_size[1] #캐릭터 세로 크기



#이벤트 루프
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running:
    dt = clock.tick(60) #초당 프레임 수 fps 설정
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False

        if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
            if event.key == pygame.K_a: #왼쪽 방향키가 눌렸을 때
                to_x -= charcter_speed
            elif event.key == pygame.K_d: #오른쪽 방향키가 눌렸을 때
                to_x += charcter_speed
            elif event.key == pygame.K_s: #아래쪽 방향키가 눌렸을 때
                to_y += charcter_speed
            elif event.key == pygame.K_w: #위쪽 방향키가 눌렸을 때
                to_y -= charcter_speed

        if event.type == pygame.KEYUP: #방향키를 뗐을 때 캐릭터 멈춤
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #왼쪽, 오른쪽 경계 정하기
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #위, 아래쪽 경계 정하기
    if character_y_pos < 0:
        character_y_pos = 0

    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정
    screen.blit(character, (character_x_pos, character_y_pos)) #배경에 캐릭터 그려주기
    screen.blit(heart, (heart_width-50, heart_height-50))
    pygame.display.update()


#pygame 종료
pygame.quit()