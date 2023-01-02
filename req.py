import requests
from bs4 import BeautifulSoup

def canzone(url, nomeCanzone, nomeArtista):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    div = soup.find('div', {'class': 'chiave'})
    try:
        with  open('canzoni/' + nomeArtista.strip() + "." + nomeCanzone.strip(), 'w') as f:
            print(nomeCanzone)
            for r in div.text.split('\n'):
                r = r.strip()
                if not r:
                    continue
                chords = False
                for c in ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']:
                    if c in r:
                        chords = True
                if (chords):
                    continue
                f.write(r + '\n')
    except:
        pass
def artista(url, nomeArtista):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    divs = soup.find_all('div', {'class': 'archives'})
    for div in divs:
        nomeCanzone = div.text
        canzone(div.find('a')['href'], nomeCanzone, nomeArtista)

def sito(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    div = soup.find('ul', {'id': 'italiani'})
    links = div.find_all('a')

    for link in links:
        artista(link['href'], link.text)

sito('https://www.accordiespartiti.it/accordi-chitarra/')