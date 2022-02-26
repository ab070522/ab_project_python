from glob import glob
def value(all_file):
    for i in range(int(len(all_file))):
        f = open('person {} .txt'.format(i + 1), 'r')
        lines = f.readlines()

        gender = lines[0].split(':')
        gender_value = gender[1].split('\n')
        gender_list.append(gender_value[0])

        age = lines[1].split(':')
        age_value = age[1].split('\n')
        age_list.append(age_value[0])

        point = lines[2].split(':')
        point_value = point[1].split('\n')
        point_list.append(point_value[0])

    return gender_list, age_list, point_list



all_file = glob("./*.txt")
gender_list = []
age_list = []
point_list = []
point = 0

value(all_file)

print("gender_list : " , gender_list)


woman = 0
man = 0
age_total = 0
point_total = 0

for total in range(len(all_file)):

    if gender_list[total] == ' woman ':
        woman += 1
    elif gender_list[total] ==' man ':
        man += 1

    age_total += int(age_list[total])
    point_total += int(point_list[total])

print("age_list : ", age_list)
print("point_list : ", point_list)
print("남자는 {} 명, 여자는 {} 명 입니다.".format(man, woman))
age_value = age_total // (int(len(all_file)))
print("평균 {}살 입니다".format(age_value))
point_value = point_total // (int(len(all_file)))
print("평균 {}점 입니다".format(point_value))
