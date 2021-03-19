lst = [1, 2, 4, 1, 56, 436, 34, 41, 2, 56, 34, 132, 784]

unq_lst = []

for x in lst:
    if x not in unq_lst:
        unq_lst.append(x)

print(unq_lst)