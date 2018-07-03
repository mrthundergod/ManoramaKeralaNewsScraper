import lxml, urllib.request
from bs4 import BeautifulSoup as bs
from subPage import *


def getPage():
  url = "https://english.manoramaonline.com/news/kerala.html"
  sauce = urllib.request.urlopen(url)
  soup = bs(sauce, 'lxml')
  return(soup)

def parsePage(soup):
  titles=[]
  links=[]

  for ssoup in soup.findAll('div', class_= 'section-listing-story-body'):
  
    title = ssoup.a.text
    link = ssoup.a['href']
    titles.append(title)
    links.append(link)

  return links, titles

def makeDict(titles, body):
  dicX=dict(zip(titles, body))
  return dicX

if __name__=='__main__':
  soup=getPage()
  link, titles = parsePage(soup)
  lolBody=[]
  for j in range(16):
    bodyData = parseSubPage(link[j])
    lolBody.append(bodyData)

  dataDiX = makeDict(titles, lolBody)
  print(dataDiX)