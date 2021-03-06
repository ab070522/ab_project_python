import random
def make_map():

    tic_map = [" " for i in range(9)]

    return tic_map

def put_avatar(tic_map):
    while True:
        pos = int(input("enter your location : " ))
        if tic_map[pos - 1] == " ":
            tic_map[pos - 1] = "x"

            return tic_map

def put_AI_avatar(tic_map):
    while True:
        AI = random.randrange(1, 10)
        if tic_map[AI - 1] == " ":
            tic_map[AI - 1] = "o"

            return tic_map

def print_map(tic_map):
    print("ㅣ " + tic_map[0] + " ㅣ " + tic_map[1] + " ㅣ " + tic_map[2] + " ㅣ ")
    print("---------------")
    print("ㅣ " + tic_map[3] + " ㅣ " + tic_map[4] + " ㅣ " + tic_map[5] + " ㅣ ")
    print("---------------")
    print("ㅣ " + tic_map[6] + " ㅣ " + tic_map[7] + " ㅣ " + tic_map[8] + " ㅣ ")
    print("---------------")

def find_bingo(num):
    score = 0
    if [3] == num and tic_map[4] == num and tic_map[5] == num:
        if num == 'x':
            score = 1
        else:
            score = -1
    elif [6] == num and tic_map[7] == num and tic_map[8] == num:
        bingo = 1
    elif [0] == num and tic_map[4] == num and tic_map[8] == num:
        bingo = 1
    elif [2] == num and tic_map[4] == num and tic_map[6] == num:
        bingo = 1
    elif [0] == num and tic_map[3] == num and tic_map[6] == num:
        bingo = 1
    elif [1] == num and tic_map[4] == num and tic_map[7] == num:
        bingo = 1
    elif [2] == num and tic_map[5] == num and tic_map[8] == num:
        bingo = 1
    else:
        bingo = 0
    return bingo

#맵 만들기
tic_map = make_map()

#말 놓기
bingo = 0

while bingo == 0:
    tic_map = put_avatar(tic_map)
    bingo = find_bingo("x")
    tic_map = put_AI_avatar(tic_map)
    print_map(tic_map)
    bingo = find_bingo("o")

