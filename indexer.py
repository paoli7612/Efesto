
# importiamo le classi di Whoosh di cui avremo bisogno
from whoosh import index
from whoosh.fields import *
from whoosh.qparser import QueryParser
import os, glob
# definiamo il schema per il nostro indice
schema = Schema(titolo=TEXT(stored=True), artista=TEXT, testo=TEXT)

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = index.create_in("indexdir", schema)
writer = ix.writer()

folder = 'canzoni'
for filepath in glob.glob(folder + '/*.txt'):
    try:
        file = filepath.split("\\")[1]
        artista, titolo = file.split(".")[:2]
        testo = open(filepath, 'r').read()
        writer.add_document(titolo=titolo, artista=artista, testo=testo)
    except: pass
writer.commit()
