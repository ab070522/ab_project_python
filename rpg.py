import random
class makeCh():

    def __init__(self):
        self.hp = random.randrange(100, 200)
        self.mp = random.randrange(200,250)
        self.sword_damage = random.randrange(10, 15)
        self.magic_damage = random.randrange(14, 18)
a = makeCh()
print("my_character hp : {} , mp : {} , sword_damage : {} , magic_damage : {}".format(my.hp, my.mp , my.sword_damage , my.magic_damage))

b = makeCh()
print("b character hp : {} , mp : {} , damage : {} , magic_damage : {}".format(b.hp , b.mp , b.sword_damage , b.magic_damage ))

while a.hp > 0 and b.hp > 0:

    weapon = input("검을 사용할려면 s 을, 마법을 사용할려면 m 을 쳐주십시오 : ")
    if weapon == "s":
        b.hp = b.hp - my.sword_damage
        print("after b character hp : {} my character damage".format(b.hp , my.sword_damage))
    elif weapon == "m":
        if my.mp > 30:
            my.mp = my.mp - 30
            b.hp = b.hp - my.magic_damage
            print("after b character hp : {} my character mp : {} , magic_damage : {}".format(b.hp, my.mp , ))
        else:
            print("you're not enough mp")
            break
    b_weapon = random.randrange(2)
    if b_weapon == 0:
        my.hp = my.hp - b.damage
    print("after my character hp : {} , b character danage : {}".format(my.hp , b.damage))
else:
