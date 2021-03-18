lst = [230, 43, 6400, 2, 46, 24, 867, 29]
x = -1
for i in range(len(lst)):
    if x >= lst[i]:
        x = x
    else:
        x = lst[i]

print('Max :', x)
y = lst[0]
for i in range(len(lst)):
    if y <= lst[i]:
        y = y
    else:
        y = lst[i]

print('Min :', y)