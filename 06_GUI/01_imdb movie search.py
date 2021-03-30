

import urllib.request as url

import bs4

movie = input("Enter movie name : ")
path = "https://www.imdb.com/find?q={}".format(movie)
response = url.urlopen(path)

page = bs4.BeautifulSoup(response, 'lxml')
td = page.find('td', class_='result_text')
a_tag = td.find('a')

href = a_tag.attrs['href']
path = "https://www.imdb.com" + href
#print(path)
response = url.urlopen(path)
page = bs4.BeautifulSoup(response, 'lxml')
title = page.find('h1')
print(title.text)

rating = page.find('div', class_='ratingValue')
if not rating:
    print("Rating Not Available")
else:
    print("Rating :", rating.text.strip())

subtext = page.find('div', class_='subtext')
subtext = subtext.text.split()
subtext = ' '.join(subtext)
print(subtext)

