import requests
from lxml import html

url = "https://www.nomorelyrics.net/a.html"

urls = set()

def explore(url):
    if url in urls:
        return
    print("explore", url)
    urls.add(url)
    page = requests.get(url)
    webpage = html.fromstring(page.content)
    for k in webpage.xpath('//a/@href')[:90]:
        text = url
        if not url[-1] == '/':
            text = ""
            for u in url.split('/')[:-1]:
                text += u+"/"
        explore(text+str(k).replace("/", ""))

explore(url)
