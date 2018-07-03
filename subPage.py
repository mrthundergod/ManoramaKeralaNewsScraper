import lxml, urllib.request
from bs4 import BeautifulSoup as bs

def parseSubPage(url):
  sauce = urllib.request.urlopen(url)
  soup =bs(sauce, 'lxml')

  leSoup = soup.find('div',class_='story-body article-content')
  body = leSoup.p.text
  print(body)

if __name__=='__main__':
  url = 'https://english.manoramaonline.com/news/kerala/2018/07/03/abhimanyu-first-student-die-maharajas-campus-kochi.html'
  hello(url)