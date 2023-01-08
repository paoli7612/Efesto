
from whoosh import index
from whoosh.fields import *

from whoosh.qparser import QueryParser

ix = index.open_dir("indexdir")

artista = input("artista? ('' default): ")
titolo = input("titolo? ('' default): ")
testo = input("testo? ('' default): ")

query = input("cosa: ")
with ix.searcher() as searcher:
    query = QueryParser("testo", ix.schema).parse(query)
    results = searcher.search(query)
    for hit in results:
        print(hit.fields())