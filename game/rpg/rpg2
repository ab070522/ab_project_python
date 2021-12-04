import random
class makeCh():

    def __init__(self):
        self.hp = random.randrange(200, 300)
        self.mp = random.randrange(100, 200)
        self.sword_damage = random.randrange(10, 13)
        self.magic_damage = random.randrange(10, 15)
        self.punch_damage = random.randrange(5, 7)

    def heal(self):
        no_play = 0
        if self.mp - 50 >= 0:
            self.mp = self.mp - 50
            self.hp = self.hp + 50
            print("after my character hp : {} , my character mp : {}".format(my.hp, my.mp))
        else:
            print("you're not enough mp")
            no_play = 1
        return self.hp, self.mp, no_play

    def sword(self):
        critical = random.randrange(10)
        if critical == 0:
            sword_damage = self.sword_damage + 5
        else:
            sword_damage = self.sword_damage
        return sword_damage

    def punch(self):
        number_of_punch = random.randrange(1, 7)
        damage_punch = self.punch_damage * number_of_punch

        return number_of_punch, damage_punch


my = makeCh()
print("my_character hp : {} , mp : {} , sword_damage : {} , magic_damage : {}".format(my.hp, my.mp , my.sword_damage , my.magic_damage))

b = makeCh()
print("b character hp : {} , mp : {} , sword_damage : {} , magic_damage : {}".format(b.hp , b.mp , b.sword_damage , b.magic_damage ))

while my.hp > 0 and b.hp > 0:

# my 공격
    no_play = 0
    print('')
    print('')
    skill = input("use a sword : s , use a magic : m , use a punch : p , use a heal : h. : ")

    #검 공격
    if skill == "s":
        my_sword = my.sword()
        b.hp = b.hp - my_sword
        print('')
        print('')
        print("after b character hp : {} , my character damage : {}".format(b.hp, my_sword))

    #마법 공격
    elif skill == "m":
        if my.mp > 30:
            my.mp = my.mp - 30
            b.hp = b.hp - my.magic_damage
            print("after b character hp : {} , my character mp : {} , magic_damage : {}".format(b.hp, my.mp , my.magic_damage))
        else:
            no_play = 1
            print("you're not enough mp")

    #힐
    elif skill == "h":
        my.heal()

    #펀치 a = 
    elif skill == "p":
        a, b = my.punch()

    else:
        no_play = 1
        print("pleas write the correct letters")

    # AI 공격
    b_weapon = random.randrange(3)
    if no_play == 1:
        no_play = 1

    #검 공격
    elif b_weapon == 0:
        b_sword = b.sword()
        my.hp = my.hp - b_sword

        print("after my character hp : {} , b character sword damage : {}".format(my.hp , b_sword))

    #마법 공격
    elif b_weapon == 1:
        my.hp = my.hp - b.magic_damage
        print("after my character hp : {} , b character magic damage : {} , b character mp : {}".format(my.hp , b.magic_damage , b.mp))

    #힐
    elif b_weapon == 2:
        b.heal()
