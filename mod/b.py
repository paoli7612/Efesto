from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk

with open('ww1.txt') as f:
    text = f.read()

print("_ TESTO CARICATO")
print(text[:200] + "...")
print()

# 1. analysis
tokens = nltk.word_tokenize(text) 

print("_ ANALYSIS")
print(", ".join(tokens[:100]) + "...")
print()

#2. stopwords
_tok = tokens
tokens = list()

for t in _tok:
    if not t in stopwords.words('italian'):
        tokens.append(t)

print("_ STOPWORDS")
print(", ".join(tokens[:100]) + "...")
print()

# 3. lemmatize 
_tok = tokens
tokens = list()

wnl = nltk.WordNetLemmatizer()
for t in _tok:
    t = wnl.lemmatize(t, 'v')
    tokens.append(t)

print("_ STEMMING")
print(", ".join(tokens[:100]) + "...")
print()
