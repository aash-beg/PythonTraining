def calc1(x, y, opr):
    z = x + opr + y
    return eval(z)


num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
ch = (input("Enter operator (+, -, /, *): "))

out = calc1(num1, num2, ch)
out2 = {
    '+': 'Sum is',
    '-': 'Sub is',
    '/': 'Div is',
    '*': 'Mul is'
}

print(out2.get(ch), out)
