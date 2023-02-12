import requests, os
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, url, OUT_DIR, MAXArtisti, MAXCanzoni):
        self.outDir = OUT_DIR
        if not os.path.exists(OUT_DIR):
            os.mkdir(OUT_DIR)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")
        for div in soup.find('ul', {'id': 'italiani'}).find_all('a')[:MAXArtisti]:
            nomeArtista = div.text
            self.artista(div['href'], nomeArtista, MAXCanzoni)

    def artista(self, url, nomeArtista, MAXCanzoni):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")
        for div in soup.find_all('div', {'class': 'archives'})[:MAXCanzoni]:
            nomeCanzone = div.text
            self.canzone(div.find('a')['href'], nomeCanzone.strip(), nomeArtista.strip())
            
    def canzone(self, url, nomeCanzone, nomeArtista):
        if os.path.exists('canzoni/' + nomeArtista + "." + nomeCanzone + ".canzone.txt"):
            print("[!]", nomeArtista, nomeCanzone, "download gia effettuato", "[!]")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")
        try:
            text = soup.find('div', {'class': 'chiave'}).text
            with open(os.path.join(self.outDir, nomeArtista + "." + nomeCanzone + ".canzone.txt"), 'w', encoding="utf-8") as f:
                f.write(text)
        except:
            pass



if __name__ == '__main__':
    # scarico primi 3 artisti, prime 3 canzoni
    c = Crawler('https://www.accordiespartiti.it/accordi-chitarra/', 'canzoni', 10, 3)
