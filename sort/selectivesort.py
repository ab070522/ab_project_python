import random

numbers=[]

for i in range(5):
    number=random.randrange(100)
    numbers.append(number)
print(numbers)
print('')


for i in range(len(numbers)):
    smallest = i
    for line in range(smallest, len(numbers)):
        if numbers[smallest] > numbers[line]:
            smallest = line
    numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
    print(numbers)
