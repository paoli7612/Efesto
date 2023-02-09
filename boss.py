import os
from timer import timer
from myDisplay import display

class Boss:
    def __init__(self):
        pass

    @staticmethod
    def reset(*toDelete):
        import shutil
        for item in toDelete:
            if os.path.isdir(item):
                shutil.rmtree(item)
            elif os.path.isfile(item):
                os.remove(item)
            
    def crawler(self, link, outDir, maxArtisti=10000, maxCanzoni=10000):
        from crawler import Crawler
        if not os.path.exists(outDir):
            os.mkdir(outDir)
        @timer
        def crawler():
            Crawler(link, outDir, maxArtisti, maxCanzoni)
        crawler()
    
    def cleaner(self, inDir, outFile):
        from cleaner import Cleaner
        @timer
        def cleaner():
            Cleaner(inDir, outFile)
        cleaner()

    def invertedIndex(self, outFile, inFile):
        from invertedIndex import InvertedIndex
        @timer
        def invertedIndex():
            InvertedIndex(inFile, outFile)
        invertedIndex()

    def indexer(self, inFile, outFile):
        from indexer import Indexer
        @timer
        def indexer():
            Indexer(inFile, outFile)
        indexer()

    def whoosh(self, inFile, outFile):
        from myWhoosh import Whoosh
        @timer
        def whoosh():
            Whoosh.build(inFile, outFile)
        whoosh()

from myWhoosh import Whoosh
def searchWhoosh(artist='', tokens='', chords=''):
    w = Whoosh('whoosh')
    @timer
    def whooshSearch():
        rr = w.search(artist, tokens, chords)
        display(rr[:4])
    whooshSearch()

from invertedIndex import InvertedIndex
def searchInverted(what):
    i = InvertedIndex('ii.pickle')
    @timer
    def invertedIndexSearch():
        rr = i.search(what)
        display(rr[:4], True)
    invertedIndexSearch()