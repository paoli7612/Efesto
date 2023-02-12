from whoosh.qparser import QueryParser
import os
from whoosh.fields import *
from whoosh import index, query
from preprocessing import preprocessing
from snenerizer import Snenerizer

class Whoosh:
    def __init__(self, inFolder):
        self.ix = index.open_dir(inFolder)

    def search(self, artist, tokens, chords):
        with self.ix.searcher() as searcher:
            qq = list()
            if artist:
                qq.append(query.Term('artist', artist))
            if tokens:
                tokens = preprocessing(tokens)
                for t in tokens:
                    qq.append(query.Term('tokens', t[0]))
            if chords:
                chords = preprocessing(chords, True)
                for c in chords:
                    qq.append(query.Term('chords', c))
            q = query.And(qq)

            print("Query whoosh:", q)

            results = searcher.search(q)
            table = list()
            for hit in results:
                fields = hit.fields()
                table.append([fields['title'], fields['artist'], fields['score']])
            return table

    @staticmethod
    def build(indexFile, outDir):
        schema = Schema(title=TEXT(stored=True),
                artist=TEXT(stored=True),
                chords=TEXT(stored=True),
                tokens=TEXT(stored=False),
                score=NUMERIC(stored=True))
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        ix = index.create_in(outDir, schema)
        writer = ix.writer()
        snenerizer = Snenerizer()

        for row in open(indexFile, 'r', encoding='utf-8'):
            p, tokens, chords = row.split(' { } ')
            artist, titolo = p.split('.')
            tt = eval(tokens)
            tokens = str()
            for t, c in tt:
                tokens += t + " "
            score = snenerizer.analizza(row)
            writer.add_document(title=titolo, artist=artist, tokens=tokens, chords=chords.lower(), score=score)
        writer.commit()
    
if __name__ == '__main__':
    Whoosh.build('indice.txt', 'whoosh')
   