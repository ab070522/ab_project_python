import random


def line(numbers):
    print(numbers)
    print('')
    for i in range(len(numbers)):

        for shake in range(len(numbers) - 1):
            print('')
            if numbers[shake] > numbers[shake + 1]:
                numbers[shake], numbers[shake+1] = numbers[shake+1], numbers[shake]


            print(numbers)
            print('')
    return numbers
numbers=[]

for i in range(5):
    number=random.randrange(100)
    numbers.append(number)
    line(numbers)

