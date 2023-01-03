import os
from whoosh import index
from whoosh.fields import Schema, TEXT

# Define the schema for the index
schema = Schema(title=TEXT, content=TEXT)

# Create the index in the current directory
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = index.create_in("indexdir", schema)

# Open a writer to add documents to the index
writer = ix.writer()

for f in os.listdir('./canzoni'):
    print(f)
    file = open('./canzoni/' + f, 'r')
    try:
        writer.add_document(title=f, content=file.read())
    except: pass

# Commit the changes
writer.commit()

# Perform a search
with ix.searcher() as searcher:
    results = searcher.find("content", "denuncia")
    for result in results:
        print(result)