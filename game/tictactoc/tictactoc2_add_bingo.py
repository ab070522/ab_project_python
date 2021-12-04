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

        if tic_map[0] == "x" and tic_map[1] == "x" :
            tic_map[2] = "o"

        else:

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
    bingo = 0
    if tic_map[3] == num and tic_map[4] == num and tic_map[5] == num:
        bingo = 1
    elif tic_map[6] == num and tic_map[7] == num and tic_map[8] == num:
        bingo = 1
    elif tic_map[0] == num and tic_map[4] == num and tic_map[8] == num:
        bingo = 1
    elif tic_map[2] == num and tic_map[4] == num and tic_map[6] == num:
        bingo = 1
    elif tic_map[0] == num and tic_map[3] == num and tic_map[6] == num:
        bingo = 1
    elif tic_map[1] == num and tic_map[4] == num and tic_map[7] == num:
        bingo = 1
    elif tic_map[2] == num and tic_map[5] == num and tic_map[8] == num:
        bingo = 1
    elif tic_map[0] == num and tic_map[1] == num and tic_map[2] == num:
        bingo = 1
    return bingo

#맵 만들기
tic_map = make_map()

#말 놓기
bingo = 0
answer = 0

while bingo == 0:
    tic_map = put_avatar(tic_map)
    bingo += find_bingo("x")
    if bingo == 1:
        answer = 1
    tic_map = put_AI_avatar(tic_map)
    print_map(tic_map)
    bingo += find_bingo("o")


if bingo == 2:
    print("draw")
elif answer == 1:
    print("player win")
else:
    print("AI win")
