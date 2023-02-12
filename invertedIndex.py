import pickle
from preprocessing import preprocessing

class InvertedIndex:
    def __init__(self, OUT_FILE, IN_FILE=None):
        self.tokens = dict()
        if IN_FILE == None:
            with open(OUT_FILE, 'rb') as file:
                self.tokens = pickle.load(file)
        else:
            self.build(OUT_FILE, IN_FILE)

    def search(self, what):
        q = preprocessing(what)[0][0]
        results = list()
        for d in self.tokens[q]:
            artista, canzone = d[0].split('.')
            n = d[1]
            results.append((canzone, artista, n))
        results = sorted(results, key=lambda x: x[2])
        results.reverse()
        return results

    def build(self, IN_FILE, OUT_FILE):
        for row in open(IN_FILE, 'r', encoding='utf-8'):
            p, text, chords = row.split(' { } ')
            d = eval(text)
            for t, c in d:
                self.add(t, c, p)
        with open(OUT_FILE, "wb") as handle:
            pickle.dump(self.tokens, handle)

    def add(self, t, c, p):
        if t in self.tokens.keys():
            self.tokens[t].append((p, c))
        else:
            self.tokens[t] = [(p, c)]
        
if __name__ == '__main__':
    InvertedIndex('indice.txt', 'ii.pickle')
    