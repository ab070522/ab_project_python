id_list = []
pwd_list=[]



for i in range(5):
    while True:
        count = 0

        temp_id = input("enter the your id: ")

        for c in range(len(id_list)):
            if id_list[c] == temp_id :
                count = 1


        if count == 0:
            print('ok id chek')
            break
        print('again try id overlap')

    id_list.append(temp_id)
    temp_pwd = input('enter the your pwd: ')
    pwd_list.append(temp_pwd)
    print('id pwd make!! id : {} pwd : {}'.format(id_list, pwd_list))
