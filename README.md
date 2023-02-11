# Progetto gestione dell'informazione
### Paoli Tommaso

## Panoramica
Il progetto consiste nella creazione di un motore di ricerca e nella amministrazione dei dati che il motore dovrà utilizzare per soddisfare le ricerche degli utenti. Si è deciso gi raccogliere i dati da un sito di testi e accordi di canzoni italiane e inglesi

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

- Sentiment analysis
- 

# 1. Preparazione dei dati
**crawler**: Scarichiamo il corpus di documenti dal sito <a href="https://www.accordiespartiti.it/">***accordiespartiti.it***</a>
- tramite il modulo *request* scaricheremo delle pagine dal sito per ogni **artista** e guarderemo tute le sue **canzoni** scaricandone sia il **testo** sia gli **accordi**
- Ogni canzone verrà salvata come file di testo proprio come appare sul sito e avrà come nome: ***[nome artista].[nome canzone].canzone.txt***

**cleaner**: Per lavorare con tutti questi dati abbiamo preferito "ordinarli"
- Questo strumento guarderà tutte le canzoni scaricate in precedenza dal crawler
- Rimuove righe e spazi vuoti
- Rimuove le righe per le tablature (se presenti)
- Racchiude tutto in unico file ***testi.txt*** contenente per ogni riga una canzone:
  - nome artista
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