import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

text = "This film is so good"
score = sia.polarity_scores(text)['compound']

print("punteggio", score)
if score > 0.03:
    print("Il testo è positivo.")
elif score < -0.03:
    print("Il testo è negativo.")
else:
    print("Il testo è neutro.")