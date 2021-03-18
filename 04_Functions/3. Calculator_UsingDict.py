def add(x, y):
    z = x + y
    print("Sum is", z)

def sub(x, y):
    z = x - y
    print("Sub is", z)

def div(x, y):
    z = x / y
    print("Div is", z)

def mul(x, y):
    z = x * y
    print("Mul is", z)

print ("""
Press 1 for Add
Press 2 for Sub
Press 3 for Div
Press 4 for Mul
""")

ch = int(input("Enter your choice : "))

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

# 1. Using If Else
# 2. Without If Else

operator = {1: add, 2: sub, 3: div, 4: mul}

operator[ch](num_1, num_2)

