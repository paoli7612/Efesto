
from whoosh import index
from whoosh.fields import *
from whoosh.qparser import QueryParser

ix = index.open_dir("indexdir")
artista, titolo, testo = None, None, None
artista = input("artista? ('' default): ")
if not artista:
    titolo = input("titolo? ('' default): ")
    if not titolo:
        testo = input("testo? ('' default): ")
if not (artista or titolo or testo):
    exit()
with ix.searcher() as searcher:
    if artista:
        print("Cerco per artista " + artista)
        query = QueryParser("artista", ix.schema).parse(artista)
    elif titolo:
        print("Cerco per titolo " + titolo)
        query = QueryParser("titolo", ix.schema).parse(titolo)
    else:
        print("Cerco dal testo " + testo)
        query = QueryParser("testo", ix.schema).parse(testo)

    results = searcher.search(query, limit=10000)
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Artista", "Titolo", "path"]
    for hit in results:
        fields = hit.fields()
        table.add_row([fields['artista'], fields['titolo'], fields['path']])
    print(table)