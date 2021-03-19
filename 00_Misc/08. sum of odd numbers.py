# Sum of odd numbers
import math
i= int(input("Enter a number:"))
x= 0
for i in range(0, math.floor(i/2)+1):
    x=x+(2*i+1)
print(x)