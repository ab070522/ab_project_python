import random


#ef make_random_list():
#    a = []
#    for i in range(10):
#        random_nom = random.randrange(1, 100)
#        a.append(random_nom)
#    return a

#def find_max_value(a):
#    max_value = a[0]
#    for i in range(len(a)):
#        if max_value < a[i]:
#            max_value = a[i]
#    result = max_value
#    return max_value

#temp_list = make_random_list()
#result = find_max_value(temp_list)
#print(result)

def r_s_p(my_hand, com_hand, my_cion, com_coin):


    if my_hand == "r" and com_hand == "r" or my_hand == "s" and com_hand == "s" or my_hand == "p" and com_hand == "p":
        print("drawn")
    elif my_hand == "r" and com_hand == "p" or my_hand == "s" and com_hand == "r" or my_hand == "p" and com_hand == "s" :
        print("computer win")
        my_cion -= 200
        com_coin  += 200
    elif my_hand == "r" and com_hand == "s" or my_hand == "s" and com_hand == "p" or my_hand == "p" and com_hand == "r":
        print("player win")

        my_cion += 200
        com_coin -= 200
    return my_cion, com_coin




my_coin = 600
com_coin = 600
com_hand = 0

while my_coin > 0 and my_coin <1200:
    my_hand = input("press R, S, P : ")

    com_r_s_p = random.randrange(3)
    if com_r_s_p == 0:
        com_hand = "r"
    elif com_r_s_p == 1:
        com_hand = "s"
    else:
        com_hand = "p"

    print('my hand')
    print(my_hand)
    print('computer hand')
    print(com_hand)

    answer = r_s_p(my_hand, com_hand, my_coin, com_coin)

    print('my coin and computer coin')
    print(r_s_p)

    print('computer coin')
    print(com_coin)
if my_coin == 0:
    print('!!!player win!!!')
elif com_coin == 0:
    print('!!!computer win!!!')