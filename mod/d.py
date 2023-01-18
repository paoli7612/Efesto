from nltk.corpus import wordnet
print(wordnet.synsets('dog'))
print(wordnet.synsets('cat', wordnet.VERB))