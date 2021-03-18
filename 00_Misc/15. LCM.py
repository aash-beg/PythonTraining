#LCM of 2 numbers
x = int(input('Enter first number :'))
y = int(input('Enter second number :'))

for i in range(1, x*y+1):
    if i % x == 0 and i % y == 0:
        print(i)
        break
