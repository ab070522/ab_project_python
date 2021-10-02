#import random
#bridge = []
#life = 8

#for i in range(8):
#    a = random.randrange(2)
#    bridge.append(a)
#count = 0
#while life != 0 or count != 7:

#    ch = int(input('Enter your choice 방탄 or dead : (0, 1) '))

#    if bridge[count] == ch:
#        count += 1
#        print('축하해 이번엔 살았어')
#    else:
#        print('dead')
#        life -= 1

#if count == 7:
#    print('kkkkkkkkk')

tic_map = [' ' for i in range(9)]
my_tic = 0
you_tic = 0
for i in range(9):
    my_tic = int(input('put number '))
    if tic_map[my_tic] == ' ':
        tic_map[my_tic] = 'x'
    print(tic_map)
    you_tic = int(input('put number '))
    if tic_map[you_tic] == ' ':
        tic_map[you_tic] = 'o'
    print(tic_map)
    if 