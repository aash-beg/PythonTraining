#Sum of even numbers - list

lst = []
sum1 = 0
for i in range(50):
    if i % 2 == 0:
        lst.append(i)

for j in range(len(lst)):
    sum1 = sum1 + lst[j]

print(sum1)