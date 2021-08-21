#a = int(input())

#a = (a % 2)

#if a == 0:
 #   print("even")

#else:
#  print("odd")

#---------------------------

#for i in range(1, 11):
#    print("*" * i)

#a = int(input())
#count = 0
#or i in range(2, a):
#    if a % i == 0:
 #       count += 1
#if count == 0:
#    print("prime")
#else:
#    print("not prime")

import random
a = []
for i in range(10):
    b = random.randrange(10)
    a.append(b)

print(a)

max_valve = a[0]
for i in range(len(a)):
    if max_valve > a [i]:
        max_valve = a[i]

print(max_valve)