import nltk
from nltk.corpus import stopwords

text = "This is a test"
tokens = nltk.word_tokenize(text) 
print("TOKENS", tokens)
wnl = nltk.WordNetLemmatizer()

ww = list()
for t in tokens:
    if not t in stopwords.words('english'):
        print("non stopword: ",wnl.lemmatize(t))
        ww.append(t)



for w, t in nltk.pos_tag(ww):
    print(w, t)