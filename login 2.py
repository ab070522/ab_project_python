for number in range(2, 10):
    for i in range(1, 10):
        print( '{} x {} = {}'.format(number, i, number * i))

while True :
  for pwd in range(len(temp_pwd)):
        if temp_pwd[pwd] == '!' or temp_pwd[pwd] == '@' or temp_pwd[pwd] == '#':
            countpwd = 1
            break
        if countpwd == 0:
            print('input pwd !, @, #')



#import random
#a = []
#for i in range(100):
#    b = random.randrange(1, 6)
#    a.append(b)
#count_list = [0,0,0,0,0]
#for i in range(len(a)):
#    num = a[i] -1
#    count_list[num] += 1

