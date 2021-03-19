'''Write a Python program to count the number of strings where the string length is 2 or more and
 the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']'''

lst = ['abc', 'xyz', 'aba', '1221', 's09xs', 'kio']

count = 0

for i in range(len(lst)):
    if len(lst[i]) >= 2 and lst[i][0] == lst[i][-1]:
        print(lst[i])
        count += 1

print(count)
print ('*'* 50)

for x in lst:
    if len(x) >= 2 and x[0] == x[-1]:
        print(x)