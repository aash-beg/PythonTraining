# print all even numbers
import math
n = int(input("Enter a number: "))

for n in range(1, math.floor(n/2)+1):
    print(2*n, end=',')

