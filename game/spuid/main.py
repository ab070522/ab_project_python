import random
bridge = []
life = 8

for i in range(8):
    a = random.randrange(2)
    bridge.append(a)
count = 0
while life != 0 or count != 7:

    ch = int(input('Enter your choice 방탄 or dead : (0, 1) '))

    if bridge[count] == ch:
        count += 1
        print('축하해 이번엔 살았어')
    else:
        print('dead')
        life -= 1

if count == 7:
    print('kkkkkkkkk')
