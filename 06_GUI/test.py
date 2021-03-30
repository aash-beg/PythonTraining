from tkinter import *
from tkinter.font import Font
import urllib.request as url
import bs4

window = Tk()
window.geometry('600x500')

main_label = Label(window, text="IMDB Movie Search",
                   font=Font(size=18), fg='Red')
main_label.pack()

label_name = Label(window, text="Enter Movie Name",
                font=Font(size=16), fg='red')
label_name.place(x=20, y=50)

entry_name = Entry(window, font=Font(size=16), fg='red')
entry_name.place(x=300, y=50)

label_rating = Label(window, text ='Rating', font=Font(size=16), fg='red')
label_rating.place(x=20, y=150)

entry_rating = Entry(window, font=Font(size=16), fg='red')
entry_rating.place(x=300, y=150)

label_info = Label(window, text ='Rating', font=Font(size=16), fg='red')
label_info.place(x=20, y=250)

entry_info = Entry(window, font=Font(size=16), fg='red')
entry_info.place(x=300, y=150)

movie = entry_name.get()
path = "https://www.imdb.com/find?q={}".format(movie)
response = url.urlopen(path)

page = bs4.BeautifulSoup(response, 'lxml')
td = page.find('td', class_='result_text')
a_tag = td.find('a')

href = a_tag.attrs['href']
path = "https://www.imdb.com" + href
response = url.urlopen(path)
page = bs4.BeautifulSoup(response, 'lxml')

rating = page.find('div', class_='ratingValue')
rt = rating.text.strip()

entry_rating.delete(0, len(entry_rating.get()))
entry_rating.insert(rt)

subtext = page.find('div', class_='subtext')
subtext = subtext.text.split()
subtext = ' '.join(subtext)
st = subtext

entry_info.delete(0, len(entry_info.get()))
entry_info.insert(st)

window.mainloop()

