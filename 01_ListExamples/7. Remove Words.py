text_1 = 'Python is a programming language'
text_1 = text_1.split()
print(text_1)
stopwords = ['is', 'a']
text_2 = []
for items in text_1:
    if items not in stopwords:
        text_2.append(items)

print(text_2)