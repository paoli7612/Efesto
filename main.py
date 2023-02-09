from boss import Boss, searchInverted, searchWhoosh
import random

LINK = 'https://www.accordiespartiti.it/accordi-chitarra/'
CANZONI_DIR = 'canzoni'
TESTI_FILE = 'testi.txt'
INDICE_FILE = 'indice.txt'
INVERTEDINDEX_FILE = 'ii.pickle'
WHOOSH_DIR = 'whoosh'
paths = TESTI_FILE, INDICE_FILE, INVERTEDINDEX_FILE, WHOOSH_DIR

if __name__ == '__main__':
    # cancella tutti i documenti e il corpus di documenti
    Boss.reset(*paths, CANZONI_DIR)

    b = Boss()

    # avvia il crawler e scarica tutte le canzoni
    b.crawler(LINK, CANZONI_DIR)
    
    # avvia il cleaner che da un primo passaggio ai file delle canzoni
    b.cleaner(CANZONI_DIR, TESTI_FILE)

    # Avvia l'indexer che prepara il corpus all'inverted index e l'indice di whoosh
    b.indexer(TESTI_FILE, INDICE_FILE)
    
    # Crea l'inverted index
    b.invertedIndex(INVERTEDINDEX_FILE, INDICE_FILE)
    
    # Crea l'indice whoosh
    b.whoosh(INDICE_FILE, WHOOSH_DIR)
    
    # Seleziona un termine generico da cercare
    cerca = ['amore', 'soldi', 'potere', 'sacrificio', 'forza'][random.randint(0, 4)]
    
    # cerca il termine tramite entrambi gli indici
    print("Vado a cercare la parola:", cerca)
    searchWhoosh(cerca)
    searchInverted(cerca)
