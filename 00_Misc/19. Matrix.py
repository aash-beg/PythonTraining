i = int(input('Enter row :'))
j = int(input('Enter column :'))

for x in range(0, i):
    for y in range(0, j):
        print(x*y, end=' ')
    print('\n')

