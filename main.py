import lxml, urllib.request
from bs4 import BeautifulSoup as bs



def getPage():
  url = "https://english.manoramaonline.com/news/kerala.html"
  sauce = urllib.request.urlopen(url)
  soup = bs(sauce, 'lxml')
  #print(soup.prettify())
  return(soup)

def parsePage(soup):
  titles=[]
  bodies=[]
  #for newsBlock in leSoup.find_All('li', 'listing'):
  #print(newsBlock.prettify())
    #print(newsBlock)
  for ssoup in soup.findAll('div', class_= 'section-listing-story-body'):
  
    title = ssoup.a.text
    body= ssoup.p.text
    
    titles.append(title)
    bodies.append(body)

  for i in range(len(titles)):
    print (titles[i] +' :\n'+ bodies[i] + '\n\n')



if __name__=='__main__':
  soup=getPage()
  parsePage(soup)

