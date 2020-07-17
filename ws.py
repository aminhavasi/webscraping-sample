import requests
import bs4
page=requests.get('https://en.m.wikipedia.org/wiki/List_of_authors_by_name:_A')



soup=bs4.BeautifulSoup(page.content)

names=soup.findAll('a')

for name in names:
    if name.string is None:
        
        continue
    if(name.string[0]=='J') and len(name.string)>1:
        print(name.string)