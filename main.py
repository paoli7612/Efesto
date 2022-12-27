import nltk
#nltk.download('omw-1.4')

test = "Hi, my name is Tommaso Paoli and i live in Losanna My i you he she it We you they"
tokens = nltk.word_tokenize(test)

print(tokens)

# stopwords
stopwords = nltk.corpus.stopwords.words('english')

wnl = nltk.WordNetLemmatizer()
for t in tokens:
    print(t + "\t", wnl.lemmatize(t), end="")
    if (wnl.lemmatize(t) in stopwords):
        print("\tSTOPWORD", end="")
    if (t in stopwords):
        print("\tsecopwords", end="")
    print()