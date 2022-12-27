import requests
from lxml import html

links = set()

def explore(link):
    if link in links:
        return
    print("EXPLORE " + link)
    links.add(link)
    page = requests.get(link)
    webpage = html.fromstring(page.content)
    for k in webpage.xpath('//a/@href')[:3]:
        print(link+k)
        explore(link+k)


explore("https://www.nomorelyrics.net")