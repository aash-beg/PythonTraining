# Guess the number

import random

x = random.randint(1, 100)

flag = True
while flag:
    n = int(input("Guess a number between 1 to 100 :"))
    if n < x:
        print(f"Number is greater than {n}")
    elif n > x:
        print(f"Number is lesser than {n}")
    elif n == x:
        print("Guess is correct")
        flag= False
