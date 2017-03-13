import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebKitWidgets import QWebPage
#from PyQt5.QtWebKit import QWebPage


import bs4 as bs
import urllib.request


class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
sauce = client_response.mainFrame().toHtml()


#sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
js_test = soup.find('p',class_='jstest')
print(js_test.text)
#print(soup)



















