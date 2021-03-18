# Print factors of number
i = int(input('Enter the number :'))

for a in range(1, i+1):
    if i % a == 0:
        #print(int(i/a),'x',a, '=',i)
        print(a,end=',')