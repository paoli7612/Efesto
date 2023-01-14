from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk
nltk.download('omw')

with open('ww1.txt') as f:
    text = f.read()

print("_ TESTO CARICATO")
print(text[:700] + "...")
print()

# 1. analysis
tokens = nltk.word_tokenize(text) 

print("_ ANALYSIS")
print(", ".join(tokens[:20]) + "...")
print()

#2. stopwords
_tok = tokens
tokens = list()

for t in _tok:
    if not t in stopwords.words('italian'):
        tokens.append(t)

print("_ STOPWORDS")
print(", ".join(tokens[:20]) + "...")
print()

# 3. stemming 
stemmer = SnowballStemmer("italian")
_tok = tokens
tokens = list()
for t in _tok:
    w = stemmer.stem(t)
    tokens.append(w)

print("_ STEMMING")
print(", ".join(tokens[:20]) + "...")
print()

ww = tokens
print(", ".join(nltk.pos_tag(ww)[:20]) + "...")
