# Sum of even numbers
import math
i= int(input("Enter a number:"))
x= 0
for i in range(1, math.floor(i/2)+1):
    x=x+2*i
print(x)