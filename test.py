# importiamo le classi di Whoosh di cui avremo bisogno
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

# definiamo il schema per il nostro indice
schema = Schema(title=TEXT(stored=True), content=TEXT)

# creiamo un nuovo indice in una nuova directory
ix = create_in("indexdir", schema)

# apriamo il nostro indice per aggiungere documenti
writer = ix.writer()

# aggiungiamo alcuni documenti all'indice
writer.add_document(title="First document", content="This is the first document we've added!")
writer.add_document(title="Second document", content="This is the second document we've added!")

# facciamo il commit delle modifiche
writer.commit()

# ora possiamo fare delle ricerche sull'indice
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    print(results.fields(0))