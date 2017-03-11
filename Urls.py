import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

"""Grabing urls and body tags:"""

nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)


"""Can also specify classes"""
for div in soup.find_all('div', class_='body'):
    print(div.text)
