# print all odd numbers
import math
n = int(input("Enter a number: "))

for n in range(0, math.floor(n/2)):
    print(2*n+1, end=',')

