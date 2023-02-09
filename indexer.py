import requests, os
from preprocessing import preprocessing, removeFew, maxWord
class Indexer:
    def __init__(self, IN_FILE, OUT_FILE):
        with open(IN_FILE, 'r', encoding='utf-8') as file:
            outFile = open(OUT_FILE, 'w', encoding='utf-8')
            for row in file:
                row = row.strip()
                try:
                    p, text, chords = row.split(' { } ')
                    if not bool(text.strip()):
                        continue
                    ll = preprocessing(text)
                    _, m = maxWord(ll)
                    ll = removeFew(ll, m/3)
                    outFile.write(p + ' { } ' + str(ll) + " { } " + str(chords) + "\n")
                except: pass

if __name__ == '__main__':
    i = Indexer("testi.txt", "indice.txt")