import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

class _App:
    def __init__(self, text, isChords=False):
        if isChords:
            text = text.lower()
            self.index = text.split()
            return
        # print(text)            # Hei ciao sto usando whatsapp ciao
        tokens = self.A_analysis(text)
        # print(tokens)          # ['Hei', 'ciao', 'sto', 'usando', 'whatsapp', 'ciao']
        tokens = self.B_stopwords(tokens)  
        # print(tokens)          # ['Hei', 'ciao', 'usando', 'whatsapp', 'ciao']
        tokens = self.C_stemming(tokens)
        # print(tokens)          # ['hei', 'cia', 'usand', 'whatsapp', 'cia']  
        index = self.D_count(tokens)
        # print(index)           # [('hei', 1), ('cia', 2), ('usand', 1), ('whatsapp', 1)]
        self.index = self.E_sort(index)
        # print(self.index)      # [('cia', 2), ('whatsapp', 1), ('usand', 1), ('hei', 1)]

    def A_analysis(self, text):
        return nltk.word_tokenize(text)

    def B_stopwords(self, tokens):
        ntokens = list()
        for t in tokens:
            if not t in stopwords.words('italian'):
                ntokens.append(t)
        return ntokens

    def C_stemming(self, tokens):
        ntokens = list()
        stemmer_snowball = SnowballStemmer('italian')
        for t in tokens:
            ntokens.append(stemmer_snowball.stem(t))
        return ntokens

    def D_count(self, tokens):
        index = dict()
        for t in tokens:
            if t in index.keys():
                index[t] += 1
            else:
                index[t] = 1

        index = list(index.items())
        return index

    def E_sort(self, index):
        index.sort(key=lambda x: x[1])
        index.reverse()
        return index

def preprocessing(text, isChord=False):
    a = _App(text, isChord)
    l = a.index
    return l

def removeFew(index, n=1):
    index = filter(lambda x: n < x[1], index)
    return list(index)

def maxWord(index):
    if not index:
        return tuple()
    mword = index[0]
    return mword

if __name__ == '__main__':
    frase = input("dammi una frase: ")
    l = preprocessing(frase)
    print(l)