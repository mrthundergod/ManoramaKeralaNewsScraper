import lxml, urllib.request
from bs4 import BeautifulSoup as bs
from subPage import *


def getPage():
  url = "https://english.manoramaonline.com/news/kerala.html"
  sauce = urllib.request.urlopen(url)
  soup = bs(sauce, 'lxml')
  #print(soup.prettify())
  return(soup)

def parsePage(soup):
  titles=[]
  bodies=[]
  links=[]
  #for newsBlock in leSoup.find_All('li', 'listing'):
  #print(newsBlock.prettify())
    #print(newsBlock)
  for ssoup in soup.findAll('div', class_= 'section-listing-story-body'):
  
    title = ssoup.a.text
    body= ssoup.p.text
    link = ssoup.a['href']
    titles.append(title)
    bodies.append(body)
    links.append(link)
    

  for i in range(len(titles)):
    print (titles[i] +' :\n'+ bodies[i] + '\n' + links[i]+'\n\n')

  return links, titles



if __name__=='__main__':
  soup=getPage()
  link, titles = parsePage(soup)
  lolBody=[]
  for j in range(len(titles)):
    bodyData = parseSubPage(link[j])
    lolBody.append(bodyData)

  print(bodyData)

