<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

# Progetto gestione dell'informazione
<div class="w3-center">
<h3>Paoli Tommaso <b>152542</b><h3>
</div>


## Panoramica
Il progetto consiste nella creazione di un motore di ricerca e nella amministrazione dei dati che il motore dovrà utilizzare per soddisfare le ricerche degli utenti. Si è deciso di raccogliere i dati da un sito di testi e accordi di canzoni italiane e inglesi

# Indice
1. Preparazione dei dati
   - Recupero dei dati
   - Preprocessing dei dati
2. Preparazione degli indici
   - Inverted Index
   - Whoosh
3. Ricerche
   - Interfaccia utente
   - Composizione query
4. Sorgenti
   - main.py
   - cli.py
- Preprocessing
- Sentiment analysis


# 1. Preparazione dei dati
Il corpus di documenti viene preparato in due parti: i file vengono scaricati dal sito e poi vengono preparati per le strutture dati attue alla ricerca.

**crawler**: Scarichiamo il corpus di documenti dal sito <a href="https://www.accordiespartiti.it/">***accordiespartiti.it***</a>
- tramite il modulo *request* scaricheremo delle pagine dal sito per ogni **artista** e guarderemo tute le sue **canzoni** scaricandone sia il **testo** sia gli **accordi**
- Ogni canzone verrà salvata come file di testo proprio come appare sul sito e avrà come nome: ***[nome artista].[nome canzone].canzone.txt***

**cleaner**: Per lavorare con tutti questi dati abbiamo preferito "ordinarli"
- Questo strumento guarderà tutte le canzoni scaricate in precedenza dal crawler
- Rimuove righe e spazi vuoti
- Rimuove le righe per le tablature (se presenti)
- Racchiude tutto in unico file ***testi.txt*** contenente, per ogni riga, una canzone:
  - nome artista
  - ___ PUNTO ___
  - titolo canzone
  - ___ SEPARATORE ___
  - testo canzone
  - ___ SEPARATORE ___
  - set degli accordi

I separatori sono solo dei caratteri arbitrari scelti dal programmatore per semplificare il codice " { } "

**indexer**:
In previsione di preparare l'**inverted index** e **whoosh** si è preferito attuare un'operazione molto "laboriosa" subito
- Questo strumento prendera il file ***testi.txt*** riscrivendolo
- Sostituisce però tutti i testi con gli stessi testi "preprocessati"
  - Rimarranno unicamente i token in forma base delle parole "significanti" presenti più volte con annessa la loro "frequenza"
- Questa operazione è risultata essere la più "costosa" per il sistema

# 2 Preparazione degli indici
**invertedIndex**: Tramite le funzionalità base del python creiamo il nostro **inverted index**
- Tramite il modulo pickle salveremo il nostro "insieme di liste" all'interno di un file
  
**whoosh**: 
Lo schema sarà cosi:
<table>
<tr><th>titolo</th><th>artista</th><th>tokens</th><th>accordi</th><th>Punteggio sentiment</th></tr>
<tr>
<td>Titolo della canzone</td>
<td>Nomi degli artisti della canzone</td>
<td>Lista dei token principali della canzone</td>
<td>Set degli accordi</td>
<td>Punteggio di sentiment associato al testo e al titolo della canzone</td>
</table>

# 3. Ricerche
Per testare il progetto si è deciso di preparare un'interfaccia a linea di comando che, una volta avviata andrà a caricarsi gli indici creati in precedenza, e permetterà all'utente di specificare se vuole fare una ricerca di una parola tramite **inverted index** o fare una ricerca più "approfondita" tramite **whoosh**

**main.py**
Avviandolo vengono eseguite tutte le fasi del progetto per poi evvettuare alcune ricerche. Per ogni fase vengono mostrati anche i tempi di esecuzione.

Mostriamo ora un esecuzione di prova gia eseguita con le relative tempistiche. 
<table class="w3-table-all">
<tr>
<td></td>
<td>Crawler</td>
<td>Cleaner</td>
<td>Indexer</td>
<td>InvertedIndex</td>
<td>Whoosh</td>
</tr>
<tr>
<th>Secondi</th>
<td>7888.57</td>
<td>80.74</td>
<td>545.86</td>
<td>0.67</td>
<td>14.46</td>
</tr>
</table>

<br>
<br>
<br>
<br>
<br>

# Preprocessing
Per questo progetto si è deciso di applicare un preprocessing un filo più "aggressivo" di come è stato studiato, e quindi verranno più spesse ignorate parole anche apparentemente significanti. Inoltre parlando di testi di canzoni si è deciso di non dare la minima importanza all'ordine delle parole ma solo al loro significato e la loro frequenza in ogni testo.
Per quanto riguarda gli accordi si è presa in considerazione la misurazione della tonica di ogni canzone. (Si è deciso di ignorare i cambi di tonalità). Per ogni canzone verrà memorizzato un set con tutti gli accordi apparsi una o più volte.
Dopo aver recuperato i token della canzone, (puliti stemmati e senza stopwords), vengono contate le frequenze all'interno del testo. Infine vengono rimossi tutti i token che non sono presenti almeno 1/3 delle volte che è presente il primo token.

# Main.py



```python
   # cancella tutti i documenti e il corpus di documenti ( se presenti )
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
```