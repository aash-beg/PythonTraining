def calc1(x, y, opr):
    z = x + opr + y
    result = eval(z)
    return result

print ("""
Press 1 for Add
Press 2 for Sub
Press 3 for Div
Press 4 for Mul
""")

ch = int(input("Input Choice: "))

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

operator = {
    1: '+',
    2: '-',
    3: '/',
    4: '*'
}

out = calc1(num1, num2, operator.get(ch))
print('Result is',out)