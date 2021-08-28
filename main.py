#i = 1
#while i < 5:
 #   print("hi", i)
  #  i = i + 1


#i = 1
#while i < 8:
#    print(i * "*")
#    i = i + 1
for i in range(1, 100):
     a = i % 10
     b = i // 10
     first_if = a != 0 and a % 3 == 0
     second_if = b % 3 == 0 and b != 0

     if first_if and second_if:
         print("**")
     elif first_if or second_if:
         print("*")
     else:
         print(i)


