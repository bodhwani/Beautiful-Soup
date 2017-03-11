import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
#print(soup)
"""
Some basic commands :
print(soup.p)
print(soup.title.string)
print(soup.find_all('p'))
print(soup.get_text())
Get all the text in your website.
print(url.get('href'))
"""
